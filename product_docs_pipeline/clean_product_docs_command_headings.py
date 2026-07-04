"""Remove fake command-heading rows from the final product-doc JSONL tree.

This is deterministic post-processing for product documentation only. It does
not touch release-note preprocessing and does not use LLMs or augmentation.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import shutil
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from preprocess_product_docs import (
    _duplicate_questions_final,
    _final_issue_counts,
    _rows_with_underscore_version,
)
from run_low300_product_docs_stage import balance_reports, sample_review, write_csv as write_csv_rows
from project.src.product_doc_validator import (
    exact_qa_dedupe_key,
    is_fake_command_heading_row,
    is_fake_command_heading_text,
    normalize,
    rows_with_grounding,
    validate_qa_row,
)


BASE_DIR = Path(__file__).resolve().parent
DEFAULT_INPUT_ROOT = BASE_DIR / "final_json" / "product_docs" / "full_product_docs"
DEFAULT_COMBINED_JSONL = BASE_DIR / "final_json" / "product_docs" / "train_chat_product_docs.jsonl"
DEFAULT_OUTPUT_JSONL = BASE_DIR / "final_json" / "product_docs" / "product_docs_final_command_heading_clean.jsonl"
DEFAULT_REPORT_JSON = BASE_DIR / "final_json" / "product_docs" / "product_docs_fake_command_heading_report.json"
DEFAULT_SUMMARY_CSV = BASE_DIR / "final_json" / "product_docs" / "full_product_docs_summary.csv"
DEFAULT_QUALITY_JSON = BASE_DIR / "final_json" / "product_docs" / "full_product_docs_quality_report.json"
DEFAULT_BALANCE_JSON = BASE_DIR / "final_json" / "product_docs" / "full_product_docs_balance_report.json"
DEFAULT_BALANCE_CSV = BASE_DIR / "final_json" / "product_docs" / "full_product_docs_balance_report.csv"
DEFAULT_SAMPLE_JSONL = BASE_DIR / "final_json" / "product_docs" / "final_product_docs_sample_review.jsonl"
DEFAULT_SAMPLE_CSV = BASE_DIR / "final_json" / "product_docs" / "final_product_docs_sample_review.csv"

COMMAND_REFERENCE_FAMILIES = {"cli_command_reference", "show_command_reference"}
COMMAND_HISTORY_METADATA_RE = re.compile(r"\b(?:Command History|Command Information)\b", re.IGNORECASE)
MANUAL_FORBIDDEN_VALUES = [
    "BFD Commands",
    "Boot commands",
    "ERPS Commands",
    "HSC commands",
    "Interface commands",
    "IP-SLA commands",
    "QoS commands",
    "NTP commands",
    "SSH client commands",
    "VLAN commands",
    "Routing commands",
    "VSX commands",
]
MANUAL_FORBIDDEN_QUESTIONS = [
    "What does the Boot commands command do?",
    "What does the Interface commands command do?",
    "What does the QoS commands command do?",
]
STRICT_ZERO_KEYS = [
    "exact_duplicate_qa_pairs",
    "duplicate_questions_final",
    "rows_with_underscore_version_question",
    "parameter_rows_generated",
    "parameter_fragment_rows_final",
    "parameter_description_topic_rows_final",
    "command_example_rows_generated",
    "support_footer_rows_final",
    "chapter_title_rows_final",
    "document_title_rows_final",
    "command_metadata_section_rows_final",
    "generic_metadata_section_rows_final",
    "visual_caption_rows_final",
    "page_header_rows_final",
    "syntax_command_root_mismatch_rows_final",
    "unbalanced_syntax_rows_final",
    "unbalanced_field_rows_final",
    "fake_command_name_rows_final",
    "fake_command_heading_rows_final",
    "output_like_rows_final",
    "major_ocr_damage_rows_final",
    "spacing_ocr_rows_final",
    "configuration_dump_rows_final",
    "show_output_table_rows_final",
]


def row_messages(row: dict[str, Any]) -> tuple[str, str]:
    messages = row.get("messages", [])
    if not isinstance(messages, list):
        return "", ""
    user = ""
    assistant = ""
    for message in messages:
        if not isinstance(message, dict):
            continue
        if message.get("role") == "user":
            user = str(message.get("content", "") or "")
        elif message.get("role") == "assistant":
            assistant = str(message.get("content", "") or "")
    return user, assistant


def load_product_doc_rows(input_root: Path) -> tuple[list[dict[str, Any]], int]:
    rows: list[dict[str, Any]] = []
    parse_errors = 0
    for train_path in sorted(input_root.rglob("train_chat.jsonl")):
        with train_path.open("r", encoding="utf-8-sig", errors="replace") as handle:
            for line_number, line in enumerate(handle, 1):
                line = line.strip().lstrip("\ufeff")
                if not line:
                    continue
                try:
                    row = json.loads(line)
                except json.JSONDecodeError:
                    parse_errors += 1
                    continue
                row["_cleanup_source_path"] = str(train_path)
                row["_cleanup_source_line"] = line_number
                rows.append(row)
    return rows, parse_errors


def strip_cleanup_metadata(row: dict[str, Any]) -> dict[str, Any]:
    cleaned = dict(row)
    cleaned.pop("_cleanup_source_path", None)
    cleaned.pop("_cleanup_source_line", None)
    return cleaned


def is_command_history_metadata_contamination(row: dict[str, Any]) -> bool:
    if str(row.get("data_family", "")) not in COMMAND_REFERENCE_FAMILIES:
        return False
    _, answer = row_messages(row)
    return bool(COMMAND_HISTORY_METADATA_RE.search(answer))


def command_equals_syntax_heading(row: dict[str, Any]) -> bool:
    command = normalize(row.get("command", ""))
    syntax = normalize(row.get("syntax", ""))
    return bool(command and syntax and command.lower() == syntax.lower() and is_fake_command_heading_text(command))


def classify_drop(row: dict[str, Any]) -> str:
    if is_fake_command_heading_row(row):
        if command_equals_syntax_heading(row):
            return "syntax_equals_heading"
        return "fake_command_heading"
    if is_command_history_metadata_contamination(row):
        return "command_history_metadata"
    return ""


def duplicate_qa_pairs(rows: list[dict[str, Any]]) -> int:
    counts = Counter(exact_qa_dedupe_key(row) for row in rows)
    return sum(count - 1 for count in counts.values() if count > 1)


def event_log_ratio(rows: list[dict[str, Any]]) -> float:
    if not rows:
        return 0.0
    event_rows = sum(1 for row in rows if row.get("data_family") == "event_log_reference")
    return round(event_rows / len(rows), 6)


def manual_search_counts(rows: list[dict[str, Any]]) -> dict[str, Any]:
    forbidden_value_counts = {value: 0 for value in MANUAL_FORBIDDEN_VALUES}
    forbidden_question_counts = {question: 0 for question in MANUAL_FORBIDDEN_QUESTIONS}
    for row in rows:
        command = normalize(row.get("command", ""))
        syntax = normalize(row.get("syntax", ""))
        user, _ = row_messages(row)
        for value in MANUAL_FORBIDDEN_VALUES:
            if command == value or syntax == value:
                forbidden_value_counts[value] += 1
        for question in MANUAL_FORBIDDEN_QUESTIONS:
            if question in user:
                forbidden_question_counts[question] += 1
    return {
        "forbidden_command_or_syntax_values_final": forbidden_value_counts,
        "forbidden_command_or_syntax_values_total_final": sum(forbidden_value_counts.values()),
        "forbidden_questions_final": forbidden_question_counts,
        "forbidden_questions_total_final": sum(forbidden_question_counts.values()),
    }


def build_quality_report(
    *,
    input_root: Path,
    output_jsonl: Path,
    total_rows_before: int,
    rows: list[dict[str, Any]],
    input_parse_errors: int,
    drop_counts: Counter[str],
    fake_heading_found: int,
    syntax_equals_heading_found: int,
    metadata_found: int,
    examples: dict[str, list[dict[str, Any]]],
) -> dict[str, Any]:
    final_issues = _final_issue_counts(rows)
    data_family_counts = Counter(str(row.get("data_family", "")) for row in rows)
    validation_drops = Counter()
    for row in rows:
        valid, reason = validate_qa_row(row, require_grounding=True)
        if not valid:
            validation_drops[reason] += 1

    report: dict[str, Any] = {
        "input_root": str(input_root),
        "output_jsonl": str(output_jsonl),
        "total_rows_before": total_rows_before,
        "total_rows_after": len(rows),
        "rows_dropped_total": total_rows_before - len(rows),
        "input_jsonl_parse_errors": input_parse_errors,
        "jsonl_parse_errors": 0,
        "exact_duplicate_qa_pairs": duplicate_qa_pairs(rows),
        "duplicate_questions_final": _duplicate_questions_final(rows),
        "rows_with_underscore_version_question": _rows_with_underscore_version(rows),
        "fake_command_heading_rows_found": fake_heading_found,
        "fake_command_heading_rows_dropped": drop_counts["syntax_equals_heading"]
        + drop_counts["fake_command_heading"],
        "syntax_equals_heading_rows_found": syntax_equals_heading_found,
        "syntax_equals_heading_rows_dropped": drop_counts["syntax_equals_heading"],
        "command_history_metadata_rows_found": metadata_found,
        "command_history_metadata_rows_dropped": drop_counts["command_history_metadata"],
        "fake_command_heading_rows_final": sum(1 for row in rows if is_fake_command_heading_row(row)),
        "command_history_metadata_rows_final": sum(
            1 for row in rows if is_command_history_metadata_contamination(row)
        ),
        "event_log_ratio_after_cap": event_log_ratio(rows),
        "parameter_rows_generated": data_family_counts.get("command_parameter_reference", 0),
        "command_example_rows_generated": data_family_counts.get("command_example", 0),
        "drop_reason_counts": dict(sorted(drop_counts.items())),
        "data_family_counts": dict(sorted(data_family_counts.items())),
        "validation_drops_if_revalidated": sum(validation_drops.values()),
        "validation_drop_reasons_if_revalidated": dict(sorted(validation_drops.items())),
        "final_issue_counts": dict(sorted(final_issues.items())),
        "examples": examples,
    }
    for key in STRICT_ZERO_KEYS:
        report.setdefault(key, int(final_issues.get(key, 0)))
    report.update(manual_search_counts(rows))
    report["required_zero_checks"] = {key: int(report.get(key, 0) or 0) for key in STRICT_ZERO_KEYS}
    report["required_zero_checks_passed"] = all(value == 0 for value in report["required_zero_checks"].values())
    report["event_log_ratio_check_passed"] = report["event_log_ratio_after_cap"] <= 0.15
    report["manual_search_checks_passed"] = (
        report["forbidden_command_or_syntax_values_total_final"] == 0
        and report["forbidden_questions_total_final"] == 0
    )
    report["ready_to_merge_with_release_notes"] = (
        report["jsonl_parse_errors"] == 0
        and report["required_zero_checks_passed"]
        and report["event_log_ratio_check_passed"]
        and report["manual_search_checks_passed"]
    )
    return report


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(strip_cleanup_metadata(row), ensure_ascii=False, sort_keys=False))
            handle.write("\n")


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def clean_rows(
    rows: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], Counter[str], dict[str, Counter[str]], dict[str, list[dict[str, Any]]]]:
    kept: list[dict[str, Any]] = []
    drop_counts: Counter[str] = Counter()
    drop_counts_by_path: dict[str, Counter[str]] = defaultdict(Counter)
    examples: dict[str, list[dict[str, Any]]] = {
        "syntax_equals_heading": [],
        "fake_command_heading": [],
        "command_history_metadata": [],
    }
    for row in rows:
        reason = classify_drop(row)
        if reason:
            drop_counts[reason] += 1
            drop_counts_by_path[str(row.get("_cleanup_source_path", ""))][reason] += 1
            if len(examples[reason]) < 20:
                user, answer = row_messages(row)
                examples[reason].append(
                    {
                        "source_path": row.get("_cleanup_source_path", ""),
                        "source_line": row.get("_cleanup_source_line", ""),
                        "switch": row.get("switch", ""),
                        "version": row.get("version", ""),
                        "data_family": row.get("data_family", ""),
                        "command": row.get("command", ""),
                        "syntax": row.get("syntax", ""),
                        "question": user,
                        "answer_preview": answer[:300],
                    }
                )
            continue
        kept.append(row)
    return kept, drop_counts, drop_counts_by_path, examples


def grouped_by_source_path(rows: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[str(row.get("_cleanup_source_path", ""))].append(row)
    return grouped


def backup_path_for(path: Path, backup_suffix: str) -> Path:
    return path.with_name(f"{path.stem}{backup_suffix}{path.suffix}")


def read_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8-sig", errors="replace"))
    except json.JSONDecodeError:
        return {}


def update_group_quality_report(
    *,
    train_path: Path,
    before_count: int,
    after_rows: list[dict[str, Any]],
    drop_counts: Counter[str],
) -> None:
    quality_path = train_path.parent / "quality_report.json"
    report = read_json(quality_path)
    after_count = len(after_rows)
    family_counts = Counter(str(row.get("data_family", "")) for row in after_rows)
    event_rows = family_counts.get("event_log_reference", 0)
    final_issues = _final_issue_counts(after_rows)

    report.update(
        {
            "total_rows": after_count,
            "total_qa_rows_after_dedup": after_count,
            "exact_duplicate_qa_pairs": duplicate_qa_pairs(after_rows),
            "duplicate_questions_final": _duplicate_questions_final(after_rows),
            "rows_with_switch_version_grounding": rows_with_grounding(after_rows),
            "rows_with_underscore_version_in_question": _rows_with_underscore_version(after_rows),
            "source_type_counts": dict(sorted(Counter(str(row.get("source_type", "")) for row in after_rows).items())),
            "data_family_counts": dict(sorted(family_counts.items())),
            "document_title_counts": dict(sorted(Counter(str(row.get("document_title", "")) for row in after_rows).items())),
            "switch_counts": dict(sorted(Counter(str(row.get("switch", "")) for row in after_rows).items())),
            "version_counts": dict(sorted(Counter(str(row.get("version", "")) for row in after_rows).items())),
            "event_log_rows_after_cap": event_rows,
            "event_log_ratio_after_cap": round(event_rows / after_count, 4) if after_count else 0.0,
            "parameter_rows_generated": family_counts.get("command_parameter_reference", 0),
            "command_example_rows_generated": family_counts.get("command_example", 0),
            "post_command_heading_cleanup": {
                "applied": True,
                "rows_before": before_count,
                "rows_after": after_count,
                "rows_dropped": before_count - after_count,
                "fake_command_heading_rows_dropped": drop_counts["fake_command_heading"]
                + drop_counts["syntax_equals_heading"],
                "syntax_equals_heading_rows_dropped": drop_counts["syntax_equals_heading"],
                "command_history_metadata_rows_dropped": drop_counts["command_history_metadata"],
            },
            "fake_command_heading_rows_dropped_post_cleanup": drop_counts["fake_command_heading"]
            + drop_counts["syntax_equals_heading"],
            "syntax_equals_heading_rows_dropped_post_cleanup": drop_counts["syntax_equals_heading"],
            "command_history_metadata_rows_dropped_post_cleanup": drop_counts["command_history_metadata"],
            "fake_command_heading_rows_final": int(final_issues.get("fake_command_heading_rows_final", 0)),
            "command_history_metadata_rows_final": sum(
                1 for row in after_rows if is_command_history_metadata_contamination(row)
            ),
        }
    )
    report.update(dict(final_issues))
    write_json(quality_path, report)


def classify_row_count(raw_md_files: int, final_rows: int) -> tuple[str, str]:
    if final_rows == 0:
        return "zero_rows", "must_check"
    if final_rows < 50:
        return "very_low_rows", "must_check"
    if final_rows < 150 and raw_md_files >= 10:
        return "suspicious_low_rows", "check"
    if final_rows < 400 and raw_md_files >= 20:
        return "moderate_low_rows", "review_summary_only"
    return "ok", "no_action"


def update_summary_csv(summary_csv: Path) -> dict[str, Any]:
    if not summary_csv.exists():
        return {"updated": False, "reason": "summary CSV not found"}
    with summary_csv.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
        fieldnames = list(reader.fieldnames or [])

    updated = 0
    for row in rows:
        output_path = Path(str(row.get("output_path", "")))
        if not output_path.exists():
            continue
        final_rows = sum(1 for line in output_path.open("r", encoding="utf-8-sig", errors="replace") if line.strip())
        raw_md_files = int(row.get("raw_md_files", 0) or 0)
        status, priority = classify_row_count(raw_md_files, final_rows)
        row["final_rows"] = str(final_rows)
        row["rows_per_md_file"] = str(round(final_rows / raw_md_files, 3) if raw_md_files else 0.0)
        row["row_count_status"] = status
        row["audit_priority"] = priority
        updated += 1

    with summary_csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    return {"updated": True, "rows_updated": updated}


def update_balance_and_sample_reports(final_jsonl: Path) -> dict[str, Any]:
    balance_summary, balance_csv_rows = balance_reports(final_jsonl)
    write_json(DEFAULT_BALANCE_JSON, balance_summary)
    write_csv_rows(DEFAULT_BALANCE_CSV, balance_csv_rows, ["dimension", "value", "count", "percentage"])

    samples = sample_review(final_jsonl)
    sample_fieldnames = [
        "sample_basis",
        "sample_key",
        "switch",
        "version",
        "subversion",
        "source_type",
        "data_family",
        "document_title",
        "section",
        "source_file",
        "user_question",
        "assistant_answer",
    ]
    write_csv_rows(DEFAULT_SAMPLE_CSV, samples, sample_fieldnames)
    with DEFAULT_SAMPLE_JSONL.open("w", encoding="utf-8", newline="") as handle:
        for sample in samples:
            handle.write(json.dumps(sample, ensure_ascii=False) + "\n")
    return {"balance_rows": len(balance_csv_rows), "sample_rows": len(samples)}


def update_overall_quality_report(report: dict[str, Any], quality_json: Path) -> None:
    existing = read_json(quality_json)
    existing.update(
        {
            "total_product_doc_rows": report["total_rows_after"],
            "jsonl_parse_errors": report["jsonl_parse_errors"],
            "exact_duplicate_qa_pairs": report["exact_duplicate_qa_pairs"],
            "duplicate_questions_final": report["duplicate_questions_final"],
            "rows_with_underscore_version_question": report["rows_with_underscore_version_question"],
            "event_log_ratio": report["event_log_ratio_after_cap"],
            "final_issue_counts": report["final_issue_counts"],
            "required_zero_checks": report["required_zero_checks"],
            "ready_to_combine_with_release_notes": report["ready_to_merge_with_release_notes"],
            "command_heading_cleanup": {
                "total_rows_before": report["total_rows_before"],
                "total_rows_after": report["total_rows_after"],
                "rows_dropped_total": report["rows_dropped_total"],
                "fake_command_heading_rows_found": report["fake_command_heading_rows_found"],
                "fake_command_heading_rows_dropped": report["fake_command_heading_rows_dropped"],
                "syntax_equals_heading_rows_dropped": report["syntax_equals_heading_rows_dropped"],
                "command_history_metadata_rows_dropped": report["command_history_metadata_rows_dropped"],
                "fake_command_heading_rows_final": report["fake_command_heading_rows_final"],
            },
        }
    )
    write_json(quality_json, existing)


def apply_cleaned_rows_to_full_tree(
    *,
    original_rows: list[dict[str, Any]],
    cleaned_rows: list[dict[str, Any]],
    drop_counts_by_path: dict[str, Counter[str]],
    backup_suffix: str,
    combined_jsonl: Path,
    summary_csv: Path,
) -> dict[str, Any]:
    original_by_path = grouped_by_source_path(original_rows)
    cleaned_by_path = grouped_by_source_path(cleaned_rows)
    changed_files = 0
    unchanged_files = 0
    backups_created = 0
    rows_dropped = 0

    for source_path, before_rows in sorted(original_by_path.items()):
        if not source_path:
            continue
        train_path = Path(source_path)
        after_rows = cleaned_by_path.get(source_path, [])
        file_drop_counts = drop_counts_by_path.get(source_path, Counter())
        if len(after_rows) == len(before_rows) and not file_drop_counts:
            unchanged_files += 1
            continue
        backup_path = backup_path_for(train_path, backup_suffix)
        if not backup_path.exists():
            shutil.copy2(train_path, backup_path)
            backups_created += 1
        write_jsonl(train_path, after_rows)
        update_group_quality_report(
            train_path=train_path,
            before_count=len(before_rows),
            after_rows=after_rows,
            drop_counts=file_drop_counts,
        )
        changed_files += 1
        rows_dropped += len(before_rows) - len(after_rows)

    combined_backup = backup_path_for(combined_jsonl, backup_suffix)
    combined_backup_created = False
    if combined_jsonl.exists() and not combined_backup.exists():
        shutil.copy2(combined_jsonl, combined_backup)
        combined_backup_created = True
    write_jsonl(combined_jsonl, cleaned_rows)

    summary_update = update_summary_csv(summary_csv)
    balance_update = update_balance_and_sample_reports(combined_jsonl)
    return {
        "applied": True,
        "changed_train_chat_files": changed_files,
        "unchanged_train_chat_files": unchanged_files,
        "train_chat_backups_created": backups_created,
        "rows_dropped_from_tree": rows_dropped,
        "combined_jsonl": str(combined_jsonl),
        "combined_backup": str(combined_backup),
        "combined_backup_created": combined_backup_created,
        "summary_update": summary_update,
        "balance_and_sample_update": balance_update,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Clean fake command-heading rows from product-doc JSONL.")
    parser.add_argument("--input-root", type=Path, default=DEFAULT_INPUT_ROOT)
    parser.add_argument("--combined-jsonl", type=Path, default=DEFAULT_COMBINED_JSONL)
    parser.add_argument("--output-jsonl", type=Path, default=DEFAULT_OUTPUT_JSONL)
    parser.add_argument("--report-json", type=Path, default=DEFAULT_REPORT_JSON)
    parser.add_argument("--summary-csv", type=Path, default=DEFAULT_SUMMARY_CSV)
    parser.add_argument("--quality-json", type=Path, default=DEFAULT_QUALITY_JSON)
    parser.add_argument("--apply-to-full-tree", action="store_true")
    parser.add_argument("--backup-suffix", default=".before_command_heading_cleanup")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    rows, input_parse_errors = load_product_doc_rows(args.input_root)
    fake_heading_found = sum(1 for row in rows if is_fake_command_heading_row(row))
    syntax_equals_heading_found = sum(1 for row in rows if command_equals_syntax_heading(row))
    metadata_found = sum(1 for row in rows if is_command_history_metadata_contamination(row))

    cleaned_rows, drop_counts, drop_counts_by_path, examples = clean_rows(rows)
    write_jsonl(args.output_jsonl, cleaned_rows)
    report = build_quality_report(
        input_root=args.input_root,
        output_jsonl=args.output_jsonl,
        total_rows_before=len(rows),
        rows=cleaned_rows,
        input_parse_errors=input_parse_errors,
        drop_counts=drop_counts,
        fake_heading_found=fake_heading_found,
        syntax_equals_heading_found=syntax_equals_heading_found,
        metadata_found=metadata_found,
        examples=examples,
    )
    if args.apply_to_full_tree:
        report["full_product_docs_tree_apply"] = apply_cleaned_rows_to_full_tree(
            original_rows=rows,
            cleaned_rows=cleaned_rows,
            drop_counts_by_path=drop_counts_by_path,
            backup_suffix=args.backup_suffix,
            combined_jsonl=args.combined_jsonl,
            summary_csv=args.summary_csv,
        )
        update_overall_quality_report(report, args.quality_json)
    else:
        report["full_product_docs_tree_apply"] = {"applied": False}
    write_json(args.report_json, report)

    print(f"Rows before: {report['total_rows_before']}")
    print(f"Rows after: {report['total_rows_after']}")
    print(f"Rows dropped: {report['rows_dropped_total']}")
    print(f"Fake command-heading rows final: {report['fake_command_heading_rows_final']}")
    print(f"Applied to full_product_docs tree: {report['full_product_docs_tree_apply']['applied']}")
    print(f"Ready to merge with release notes: {report['ready_to_merge_with_release_notes']}")
    print(f"Output JSONL: {args.output_jsonl}")
    print(f"Report JSON: {args.report_json}")


if __name__ == "__main__":
    main()
