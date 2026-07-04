"""Dataset-level deterministic postprocessing for generated Aruba JSONL files.

This pass operates after per-release-folder extraction. It performs operations
that require global visibility across all generated training rows:

* switch/version grounding in user questions
* exact Q&A message-pair deduplication
* optional caps for highly repetitive generic source types
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


WHITESPACE_RE = re.compile(r"\s+")
QUESTION_GROUNDING_RE = re.compile(r"^For\s+.+?\s+AOS-CX\s+\d+(?:\.\d+){1,2},\s+", re.IGNORECASE)

GENERIC_SOURCE_TYPE_CAPS = {
    "release_notes_compatibility": 500,
    "release_notes_certifications": 300,
    "release_notes_supported_products": 1000,
    "release_notes_upgrade_procedure": 500,
    "release_notes_downgrade_restore": 500,
    "release_notes_version_history": 1500,
}


def normalize_text(text: Any) -> str:
    return WHITESPACE_RE.sub(" ", str(text or "").strip())


def normalize_for_exact_qa_dedupe(text: Any) -> str:
    return normalize_text(text).casefold()


def exact_qa_dedupe_key(row: dict[str, Any]) -> str:
    messages = row.get("messages", [{}, {}])
    question = messages[0].get("content", "") if len(messages) > 0 else ""
    answer = messages[1].get("content", "") if len(messages) > 1 else ""
    return f"{normalize_for_exact_qa_dedupe(question)}||{normalize_for_exact_qa_dedupe(answer)}"


def version_display(row: dict[str, Any]) -> str:
    version = normalize_text(row.get("version")).replace("_", ".")
    sub_version = normalize_text(row.get("sub_version")).replace("_", ".")
    if version and sub_version:
        return f"{version}.{sub_version}"
    return version or sub_version


def lower_first(text: str) -> str:
    text = normalize_text(text)
    if not text:
        return ""
    return text[0].lower() + text[1:]


def has_question_grounding(question: str) -> bool:
    return bool(QUESTION_GROUNDING_RE.match(normalize_text(question)))


def ground_question(row: dict[str, Any]) -> dict[str, Any]:
    messages = row.get("messages", [])
    if not isinstance(messages, list) or len(messages) != 2:
        return row
    question = normalize_text(messages[0].get("content", ""))
    if not question or has_question_grounding(question):
        return row
    switch = normalize_text(row.get("switch"))
    release = version_display(row)
    if not switch or not release:
        return row
    new_row = dict(row)
    new_messages = [dict(messages[0]), dict(messages[1])]
    new_messages[0]["content"] = f"For {switch} AOS-CX {release}, {lower_first(question)}"
    new_row["messages"] = new_messages
    return new_row


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSONL in {path} at line {line_number}: {exc}") from exc
    return rows


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def count_source_types(rows: list[dict[str, Any]]) -> dict[str, int]:
    return dict(Counter(str(row.get("source_type", "")) for row in rows))


def postprocess(args: argparse.Namespace) -> dict[str, Any]:
    final_json_root = Path(args.final_json_root)
    processed_root = Path(args.processed_root) if args.processed_root else None
    jsonl_files = sorted(final_json_root.rglob("train_chat.jsonl"))

    path_rows: list[tuple[Path, dict[str, Any]]] = []
    for path in jsonl_files:
        for row in read_jsonl(path):
            if args.ground_questions_with_version:
                row = ground_question(row)
            path_rows.append((path, row))

    rows_before_dedup = len(path_rows)
    source_counts_before = Counter(str(row.get("source_type", "")) for _, row in path_rows)

    seen: set[str] = set()
    deduped: list[tuple[Path, dict[str, Any]]] = []
    for path, row in path_rows:
        key = exact_qa_dedupe_key(row)
        if key in seen:
            continue
        seen.add(key)
        deduped.append((path, row))

    generic_rows_before_cap = sum(
        1 for _, row in deduped if str(row.get("source_type", "")) in GENERIC_SOURCE_TYPE_CAPS
    )

    capped: list[tuple[Path, dict[str, Any]]] = []
    cap_counts: Counter[str] = Counter()
    generic_rows_removed_by_cap = 0
    if args.cap_generic_sections:
        for path, row in deduped:
            source_type = str(row.get("source_type", ""))
            cap = GENERIC_SOURCE_TYPE_CAPS.get(source_type)
            if cap is not None:
                if cap_counts[source_type] >= cap:
                    generic_rows_removed_by_cap += 1
                    continue
                cap_counts[source_type] += 1
            capped.append((path, row))
    else:
        capped = deduped

    grouped: dict[Path, list[dict[str, Any]]] = defaultdict(list)
    for path, row in capped:
        grouped[path].append(row)

    for path in jsonl_files:
        rows = grouped.get(path, [])
        write_jsonl(path, rows)
        if processed_root:
            relative_path = path.relative_to(final_json_root)
            mirror_path = processed_root / relative_path
            write_jsonl(mirror_path, rows)

    final_rows = [row for _, row in capped]
    rows_with_grounding = sum(
        1
        for row in final_rows
        if has_question_grounding(row.get("messages", [{}])[0].get("content", ""))
    )
    grounding_ratio = rows_with_grounding / len(final_rows) if final_rows else 0.0
    warnings: list[str] = []
    if args.ground_questions_with_version and grounding_ratio < 0.8:
        warnings.append(f"Only {grounding_ratio:.1%} of rows have switch/version grounding in the user question.")

    generic_rows_after_cap = sum(
        1 for row in final_rows if str(row.get("source_type", "")) in GENERIC_SOURCE_TYPE_CAPS
    )
    report: dict[str, Any] = {
        "jsonl_files": len(jsonl_files),
        "total_rows_before_dedup": rows_before_dedup,
        "total_rows_after_dedup": len(deduped),
        "global_exact_qa_duplicates_removed": rows_before_dedup - len(deduped),
        "generic_rows_before_cap": generic_rows_before_cap,
        "generic_rows_after_cap": generic_rows_after_cap,
        "generic_rows_removed_by_cap": generic_rows_removed_by_cap,
        "cap_generic_sections_enabled": bool(args.cap_generic_sections),
        "generic_source_type_caps": GENERIC_SOURCE_TYPE_CAPS if args.cap_generic_sections else {},
        "question_grounding_enabled": bool(args.ground_questions_with_version),
        "rows_with_switch_version_in_question": rows_with_grounding,
        "question_grounding_ratio": round(grounding_ratio, 4),
        "qa_counts_by_source_type_before": dict(source_counts_before),
        "qa_counts_by_source_type_after": count_source_types(final_rows),
        "final_rows": len(final_rows),
        "warnings": warnings,
    }

    report_path = final_json_root / "global_quality_report.json"
    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    if processed_root:
        processed_report_path = processed_root / "global_quality_report.json"
        processed_report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    return report


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Globally dedupe and cap generated Aruba JSONL rows.")
    parser.add_argument("--final-json-root", required=True)
    parser.add_argument("--processed-root")
    parser.add_argument("--ground_questions_with_version", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--cap_generic_sections", action=argparse.BooleanOptionalAction, default=True)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    report = postprocess(args)
    print(f"JSONL files: {report['jsonl_files']}")
    print(f"Rows before global dedupe: {report['total_rows_before_dedup']}")
    print(f"Rows after global dedupe: {report['total_rows_after_dedup']}")
    print(f"Rows after caps: {report['final_rows']}")
    if report["warnings"]:
        for warning in report["warnings"]:
            print(f"WARNING: {warning}")


if __name__ == "__main__":
    main(sys.argv[1:])
