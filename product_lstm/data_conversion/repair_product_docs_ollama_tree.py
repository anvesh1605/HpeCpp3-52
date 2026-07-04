#!/usr/bin/env python3
"""Repair converted product-documentation review rows with Ollama.

This script consumes the merged product review file plus the per-version clean
datasets produced by the deterministic product conversion stage. It repairs only
review rows that are safe to attempt, preserves the original switch/version tree
under a repaired output root, and writes merged all-switch repaired outputs.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, Iterator, List, Mapping, Optional, Sequence, Tuple


SCRIPT_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPT_DIR.parent

ALLOWED_OLLAMA_REASONS = {
    "meaning_is_only_syntax",
    "markdown_section_not_matched",
    "markdown_repair_failed",
    "same_input_text_different_target_value",
    "generic_targets_moved_to_review",
    "syntax_long_explanation",
    "long_target_rows_moved_to_review",
}

GENERIC_PATTERNS = (
    "documented in this guide",
    "this guide documents the command",
    "refer to the guide",
    "see the documentation",
    "see the guide",
    "the command is documented in this guide",
)

SYNTAX_HINT_RE = re.compile(
    r"(?i)\b(?:command|does|doesn't|means|meaning|purpose|documented|guide|documentation|"
    r"displays|shows|enables|configures|used to|usage|explanation|follow the documented procedure)\b"
)
GENERIC_ROW_RE = re.compile(
    r"(?i)^(?:the command is documented in this guide\.?|this guide documents the command\.?|"
    r"refer to the guide\.?|see the documentation\.?|see the guide\.?|documented in this guide\.?)$"
)
EVENT_ID_RE = re.compile(r"(?i)\bevent\s*id\s*[:#-]?\s*(\d{3,8})\b")
BUG_ID_RE = re.compile(r"(?i)\bbug\s*id\b|\bbug\s*#\b|\bbug-\d+\b")

WHITESPACE_RE = re.compile(r"\s+")


def collapse(value: Any) -> str:
    text = str(value or "").replace("\r\n", "\n").replace("\r", "\n").replace("\f", " ")
    return WHITESPACE_RE.sub(" ", text).strip()


def normalize(value: Any) -> str:
    return collapse(value).casefold()


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def short_hash(*parts: Any, size: int = 10) -> str:
    return sha256_text("\n".join(collapse(part) for part in parts))[:size]


def load_jsonl(path: Path) -> Iterator[Tuple[int, Dict[str, Any]]]:
    with path.open("r", encoding="utf-8-sig") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON in {path}:{line_number}: {exc}") from exc
            if not isinstance(row, dict):
                raise ValueError(f"Expected object row in {path}:{line_number}")
            yield line_number, row


def write_jsonl(path: Path, rows: Iterable[Mapping[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(dict(row), ensure_ascii=False, separators=(",", ":")) + "\n")


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_md(path: Path, lines: Sequence[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def get_slots(row: Mapping[str, Any]) -> Dict[str, Any]:
    slots = row.get("slots")
    return dict(slots) if isinstance(slots, Mapping) else {}


def get_switch_version_key(row: Mapping[str, Any]) -> Tuple[str, str]:
    source_file = collapse(row.get("source_file"))
    if source_file and "/" in source_file:
        parts = source_file.split("/")
        if len(parts) >= 2:
            return parts[0], parts[1]
    matched = collapse(row.get("matched_markdown_file"))
    if matched and "Raw_Data_Product" in matched:
        bits = matched.replace("\\", "/").split("/")
        try:
            idx = bits.index("Raw_Data_Product")
            return bits[idx + 1], bits[idx + 2]
        except Exception:
            pass
    slots = get_slots(row)
    switch = collapse(slots.get("switch"))
    version = collapse(slots.get("version")).replace(".", "_")
    sub_version = collapse(slots.get("sub_version"))
    if sub_version:
        version = f"{version}_{sub_version}"
    return switch, version


def version_key_string(row: Mapping[str, Any]) -> str:
    switch, version = get_switch_version_key(row)
    return f"{switch}/{version}" if switch and version else ""


def cleaned_review_reason(reason: str) -> str:
    reason = collapse(reason)
    return reason or "review"


def should_send_to_ollama(reason: str, target_value: str) -> bool:
    reason = cleaned_review_reason(reason)
    if reason not in ALLOWED_OLLAMA_REASONS:
        return False
    if not collapse(target_value):
        return False
    if reason == "meaning_is_only_syntax" and target_value.strip().startswith("-"):
        return False
    return True


def generic_target(text: str) -> bool:
    value = collapse(text)
    if not value:
        return True
    if GENERIC_ROW_RE.match(value):
        return True
    lower = value.casefold()
    return any(pattern in lower for pattern in GENERIC_PATTERNS)


def extract_command(row: Mapping[str, Any]) -> str:
    slots = get_slots(row)
    return collapse(slots.get("command"))


def extract_event_id(row: Mapping[str, Any]) -> str:
    slots = get_slots(row)
    event_id = collapse(slots.get("event_id"))
    if event_id:
        return event_id
    text = f"{collapse(row.get('input_text'))} {collapse(row.get('target_value'))}"
    match = EVENT_ID_RE.search(text)
    return match.group(1) if match else ""


def parse_ollama_json(text: str) -> Optional[Dict[str, Any]]:
    match = re.search(r"\{.*\}", text, re.S)
    if not match:
        return None
    try:
        parsed = json.loads(match.group(0))
    except json.JSONDecodeError:
        return None
    return parsed if isinstance(parsed, dict) else None


def ollama_prompt(row: Mapping[str, Any]) -> str:
    row_json = json.dumps(row, ensure_ascii=False, separators=(",", ":"))
    return (
        "You are repairing HPE Aruba AOS-CX product documentation QA data.\n\n"
        "Return only valid JSON.\n"
        "Do not invent unsupported commands, parameters, Event IDs, switch versions, or features.\n"
        "Preserve CLI commands exactly.\n"
        "Preserve Event IDs exactly.\n"
        "Preserve AOS-CX versions exactly.\n"
        "Preserve placeholders like <VLAN-ID>, <VRF-NAME>, <IP-ADDR> exactly.\n"
        "Do not add release-note bug information.\n"
        "Do not create fake Bug IDs.\n"
        "Do not use outside knowledge.\n\n"
        f"Input row:\n{row_json}\n\n"
        "Task:\n"
        "Repair the target_value if possible.\n\n"
        "Rules:\n"
        "1. If intent is cli_syntax or show_command_syntax, target_value must contain only exact command syntax.\n"
        "2. If intent is cli_meaning or show_command_meaning, explain what the command does in one or two concise sentences.\n"
        "3. If intent is event_log_meaning, preserve the Event ID and explain only what is documented.\n"
        "4. If intent is concept_explanation, give a concise documentation-style explanation.\n"
        '5. If the row cannot be repaired confidently, set status to "unrepairable".\n\n'
        "Return JSON in this exact format:\n"
        '{\n  "status": "repaired" or "unrepairable",\n  "target_value": "...",\n  "repair_reason": "...",\n  "confidence": "high" or "medium" or "low"\n}\n'
    )


def run_ollama(row: Mapping[str, Any], model: str, fallback_model: str) -> Tuple[Optional[Dict[str, Any]], str]:
    prompt = ollama_prompt(row)
    env = os.environ.copy()
    try:
        proc = subprocess.run(
            ["ollama", "run", model],
            input=prompt,
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=240,
            check=False,
            env=env,
        )
    except FileNotFoundError:
        return None, "ollama_not_available"
    if proc.returncode != 0:
        if fallback_model and fallback_model != model:
            try:
                proc = subprocess.run(
                    ["ollama", "run", fallback_model],
                    input=prompt,
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                    timeout=240,
                    check=False,
                    env=env,
                )
            except FileNotFoundError:
                return None, "ollama_not_available"
            if proc.returncode != 0:
                return None, "ollama_failed"
        else:
            return None, "ollama_failed"

    parsed = parse_ollama_json((proc.stdout or "").strip())
    if not parsed:
        return None, "ollama_invalid_json"
    return parsed, ""


def validate_repair(row: Mapping[str, Any], parsed: Mapping[str, Any]) -> Tuple[bool, str]:
    status = collapse(parsed.get("status")).casefold()
    target_value = collapse(parsed.get("target_value"))
    confidence = collapse(parsed.get("confidence")).casefold()
    repair_reason = collapse(parsed.get("repair_reason")) or "ollama_repair"
    intent = collapse(row.get("intent"))
    slots = get_slots(row)
    command = collapse(slots.get("command"))
    event_id = collapse(slots.get("event_id"))
    input_text = collapse(row.get("input_text"))

    if status != "repaired":
        return False, "unrepairable"
    if confidence not in {"high", "medium"}:
        return False, "low_confidence"
    if not target_value:
        return False, "empty_target_value"
    if generic_target(target_value):
        return False, "generic_target"
    if BUG_ID_RE.search(target_value):
        return False, "fake_bug_id"
    if event_id:
        ids = {match.group(1) for match in EVENT_ID_RE.finditer(target_value)}
        if ids and ids != {event_id}:
            return False, "event_id_changed"
    if command and normalize(command) not in normalize(target_value):
        return False, "command_changed"
    if intent in {"cli_syntax", "show_command_syntax"}:
        if SYNTAX_HINT_RE.search(target_value):
            return False, "syntax_contains_explanation"
        if not command or normalize(command) not in normalize(target_value):
            return False, "syntax_missing_command"
    if intent in {"cli_meaning", "show_command_meaning"} and word_count(target_value) < 4:
        return False, "meaning_too_short"
    if intent == "event_log_meaning" and event_id and event_id not in target_value:
        return False, "event_id_missing"
    if not input_text:
        return False, "empty_input_text"
    return True, repair_reason


def word_count(text: str) -> int:
    return len(re.findall(r"[A-Za-z0-9_<>\-]+", collapse(text)))


def build_repaired_record(row: Mapping[str, Any], target_value: str) -> Dict[str, Any]:
    return {
        "input_text": collapse(row.get("input_text")),
        "intent": collapse(row.get("intent")),
        "slots": get_slots(row),
        "target_value": collapse(target_value),
    }


def load_base_dataset(path: Path) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for _line_number, row in load_jsonl(path):
        rows.append(
            {
                "input_text": collapse(row.get("input_text")),
                "intent": collapse(row.get("intent")),
                "slots": get_slots(row),
                "target_value": collapse(row.get("target_value")),
            }
        )
    return rows


def build_samples_md(report: Mapping[str, Any], repaired: Sequence[Mapping[str, Any]], rejected: Sequence[Mapping[str, Any]]) -> List[str]:
    lines = ["# Ollama Repair Samples", ""]
    lines.append("## Report")
    lines.append("")
    for key in (
        "total_review_rows",
        "rows_sent_to_ollama",
        "rows_repaired",
        "rows_rejected",
        "rows_unrepairable",
        "rows_fixed_deterministically",
    ):
        lines.append(f"- {key}: {report.get(key, 0)}")
    lines.append("")
    lines.append("## Repaired Samples")
    lines.append("")
    for row in list(repaired)[:10]:
        lines.append(f"- {json.dumps(row, ensure_ascii=False)}")
    lines.append("")
    lines.append("## Rejected Samples")
    lines.append("")
    for row in list(rejected)[:10]:
        lines.append(f"- {json.dumps(row, ensure_ascii=False)}")
    return lines


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input-root",
        type=Path,
        default=ROOT_DIR / "lstm_conversion" / "converted_product",
        help="Source tree produced by deterministic product conversion.",
    )
    parser.add_argument(
        "--review-file",
        type=Path,
        default=ROOT_DIR / "lstm_conversion" / "converted_product" / "all_switches_product_review.jsonl",
        help="Merged review JSONL file to repair.",
    )
    parser.add_argument(
        "--dataset-file",
        type=Path,
        default=ROOT_DIR / "lstm_conversion" / "converted_product" / "all_switches_product_dataset.jsonl",
        help="Merged clean dataset JSONL file used as the repair base.",
    )
    parser.add_argument(
        "--output-root",
        type=Path,
        default=ROOT_DIR / "lstm_conversion" / "converted_product_repaired",
        help="Output tree root for repaired product data.",
    )
    parser.add_argument(
        "--merged-output-dataset",
        type=Path,
        default=ROOT_DIR / "lstm_conversion" / "all_switches_product_dataset_repaired.jsonl",
        help="Merged repaired dataset output.",
    )
    parser.add_argument(
        "--merged-output-review",
        type=Path,
        default=ROOT_DIR / "lstm_conversion" / "all_switches_product_review_remaining.jsonl",
        help="Merged remaining review output.",
    )
    parser.add_argument(
        "--merged-output-report",
        type=Path,
        default=ROOT_DIR / "lstm_conversion" / "all_switches_ollama_repair_report.json",
        help="Merged repair report output.",
    )
    parser.add_argument(
        "--merged-output-samples",
        type=Path,
        default=ROOT_DIR / "lstm_conversion" / "all_switches_ollama_repair_samples.md",
        help="Merged repair samples markdown output.",
    )
    parser.add_argument(
        "--ollama-model",
        "--ollama_model",
        dest="ollama_model",
        type=str,
        default="qwen2.5:7b-instruct",
        help="Primary Ollama model for repair.",
    )
    parser.add_argument(
        "--ollama-fallback-model",
        type=str,
        default="qwen2.5-coder:7b",
        help="Fallback Ollama model if the primary model is unavailable.",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=8,
        help="Number of parallel Ollama worker threads.",
    )
    parser.add_argument("--force", action="store_true", help="Overwrite existing outputs.")
    return parser.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace", line_buffering=True)
        sys.stderr.reconfigure(encoding="utf-8", errors="replace", line_buffering=True)
    except Exception:
        pass

    print("[START] product-doc Ollama repair")
    args = parse_args(argv)
    input_root = args.input_root.resolve()
    review_file = args.review_file.resolve()
    dataset_file = args.dataset_file.resolve()
    output_root = args.output_root.resolve()

    if not review_file.exists():
        raise FileNotFoundError(review_file)
    if not dataset_file.exists():
        raise FileNotFoundError(dataset_file)

    output_paths = [args.merged_output_dataset, args.merged_output_review, args.merged_output_report, args.merged_output_samples]
    for path in output_paths:
        if path.exists() and not args.force:
            raise FileExistsError(f"Refusing to overwrite {path}; pass --force")

    merged_review_rows = [row for _line, row in load_jsonl(review_file)]
    base_dataset_rows = [row for _line, row in load_jsonl(dataset_file)]
    base_dataset_by_tree: Dict[Tuple[str, str], List[Dict[str, Any]]] = defaultdict(list)
    for row in base_dataset_rows:
        base_dataset_by_tree[get_switch_version_key(row)].append(row)

    repaired_by_tree: Dict[Tuple[str, str], List[Dict[str, Any]]] = defaultdict(list)
    remaining_by_tree: Dict[Tuple[str, str], List[Dict[str, Any]]] = defaultdict(list)
    sample_repaired_by_tree: Dict[Tuple[str, str], List[Dict[str, Any]]] = defaultdict(list)
    sample_rejected_by_tree: Dict[Tuple[str, str], List[Dict[str, Any]]] = defaultdict(list)
    review_reasons_by_tree: Dict[Tuple[str, str], Counter[str]] = defaultdict(Counter)
    repair_reasons_by_tree: Dict[Tuple[str, str], Counter[str]] = defaultdict(Counter)
    rows_by_intent: Counter[str] = Counter()
    rows_by_switch: Counter[str] = Counter()
    rows_by_version: Counter[str] = Counter()
    remaining_review_reasons: Counter[str] = Counter()
    repair_reasons: Counter[str] = Counter()
    accepted_rows_global: List[Dict[str, Any]] = []
    remaining_rows_global: List[Dict[str, Any]] = []
    dataset_merged_rows: List[Dict[str, Any]] = []
    seen_dataset_keys: set[str] = set()
    seen_remaining_keys: set[str] = set()

    total_review_rows = len(merged_review_rows)
    rows_sent_to_ollama = 0
    rows_repaired = 0
    rows_rejected = 0
    rows_unrepairable = 0
    rows_fixed_deterministically = 0
    invalid_jsonl_lines = 0
    empty_input_text = 0
    empty_target_value = 0

    print(f"[INPUT] reading review file {review_file}")
    row_meta: List[Dict[str, Any]] = []
    ollama_results: Dict[int, Tuple[Optional[Dict[str, Any]], str]] = {}
    ollama_futures = {}

    with ThreadPoolExecutor(max_workers=max(1, int(args.workers))) as executor:
        for line_number, row in enumerate(merged_review_rows, start=1):
            print(f"[ROW] processing row number {line_number}")
            switch, version = get_switch_version_key(row)
            tree_key = (switch, version)
            review_reason = cleaned_review_reason(row.get("review_reason"))
            intent = collapse(row.get("intent"))
            rows_by_intent[intent] += 1
            if switch:
                rows_by_switch[switch] += 1
            if switch and version:
                rows_by_version[f"{switch}/{version}"] += 1
            review_reasons_by_tree[tree_key][review_reason] += 1

            target_value = collapse(row.get("target_value"))
            input_text = collapse(row.get("input_text"))
            if not input_text:
                empty_input_text += 1
            if not target_value:
                empty_target_value += 1

            row_meta.append(
                {
                    "line_number": line_number,
                    "row": row,
                    "tree_key": tree_key,
                    "review_reason": review_reason,
                    "target_value": target_value,
                    "send_to_ollama": should_send_to_ollama(review_reason, target_value),
                }
            )
            if row_meta[-1]["send_to_ollama"]:
                rows_sent_to_ollama += 1
                future = executor.submit(run_ollama, row, args.ollama_model, args.ollama_fallback_model)
                ollama_futures[future] = len(row_meta) - 1
                print(f"[OLLAMA] queued row number {line_number}")
            else:
                ollama_results[len(row_meta) - 1] = (None, "not_sent")

        for future in as_completed(ollama_futures):
            idx = ollama_futures[future]
            try:
                ollama_results[idx] = future.result()
                print(f"[OLLAMA] completed row number {row_meta[idx]['line_number']}")
            except Exception as exc:
                ollama_results[idx] = (None, f"ollama_exception:{exc}")
                print(f"[OLLAMA] failed row number {row_meta[idx]['line_number']}")

    for idx, meta in enumerate(row_meta):
        row = meta["row"]
        tree_key = meta["tree_key"]
        review_reason = meta["review_reason"]
        target_value = meta["target_value"]
        parsed, ollama_error = ollama_results.get(idx, (None, "missing_result"))

        if not meta["send_to_ollama"]:
            remaining_rows_global.append(row)
            remaining_by_tree[tree_key].append(row)
            remaining_review_reasons[review_reason] += 1
            print("[REVIEW] row not sent to Ollama")
            continue

        if parsed is None:
            rows_unrepairable += 1
            remaining_rows_global.append(row)
            remaining_by_tree[tree_key].append(row)
            remaining_review_reasons[review_reason] += 1
            if len(sample_rejected_by_tree[tree_key]) < 10:
                sample_rejected_by_tree[tree_key].append(
                    {
                        "input_text": collapse(row.get("input_text")),
                        "intent": collapse(row.get("intent")),
                        "review_reason": review_reason,
                        "target_value": target_value,
                        "reason": ollama_error,
                    }
                )
            print("[REVIEW] row kept for manual repair")
            continue

        ok, repair_reason = validate_repair(row, parsed)
        repair_reasons[repair_reason] += 1
        repair_reasons_by_tree[tree_key][repair_reason] += 1
        if ok:
            repaired_target = collapse(parsed.get("target_value"))
            repaired_row = build_repaired_record(row, repaired_target)
            dedupe_key = json.dumps(repaired_row, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
            if dedupe_key not in seen_dataset_keys:
                seen_dataset_keys.add(dedupe_key)
                repaired_by_tree[tree_key].append(repaired_row)
                accepted_rows_global.append(repaired_row)
                rows_repaired += 1
                rows_fixed_deterministically += 1
                if len(sample_repaired_by_tree[tree_key]) < 10:
                    sample_repaired_by_tree[tree_key].append(repaired_row)
                print("[WRITE] row repaired and accepted")
                continue

            rows_rejected += 1
            remaining_rows_global.append(row)
            remaining_by_tree[tree_key].append(row)
            remaining_review_reasons["duplicate"] += 1
            print("[REVIEW] repaired duplicate routed to remaining review")
            continue

        rows_rejected += 1
        if repair_reason == "unrepairable":
            rows_unrepairable += 1
        remaining_rows_global.append(row)
        remaining_by_tree[tree_key].append(row)
        remaining_review_reasons[review_reason] += 1
        if len(sample_rejected_by_tree[tree_key]) < 10:
            sample_rejected_by_tree[tree_key].append(
                {
                    "input_text": collapse(row.get("input_text")),
                    "intent": collapse(row.get("intent")),
                    "review_reason": review_reason,
                    "target_value": target_value,
                    "repair_reason": repair_reason,
                    "parsed_status": collapse(parsed.get("status")),
                }
            )
        print("[REVIEW] row kept for manual repair")

    # Build repaired per-version outputs.
    output_root.mkdir(parents=True, exist_ok=True)
    for tree_key, base_rows in sorted(base_dataset_by_tree.items()):
        switch, version = tree_key
        tree_dir = output_root / switch / version
        tree_dir.mkdir(parents=True, exist_ok=True)
        repaired_rows = list(base_rows)
        seen = {json.dumps(row, sort_keys=True, ensure_ascii=False, separators=(",", ":")) for row in repaired_rows}
        for row in repaired_by_tree.get(tree_key, []):
            key = json.dumps(row, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
            if key in seen:
                continue
            seen.add(key)
            repaired_rows.append(row)
        write_jsonl(tree_dir / "product_dataset_repaired.jsonl", repaired_rows)
        write_jsonl(tree_dir / "product_review_remaining.jsonl", remaining_by_tree.get(tree_key, []))

        per_version_report = {
            "switch": switch,
            "version": version,
            "total_review_rows": len(remaining_by_tree.get(tree_key, [])) + len(repaired_by_tree.get(tree_key, [])),
            "rows_sent_to_ollama": sum(1 for row in merged_review_rows if get_switch_version_key(row) == tree_key and should_send_to_ollama(cleaned_review_reason(row.get("review_reason")), collapse(row.get("target_value")))),
            "rows_repaired": len(repaired_by_tree.get(tree_key, [])),
            "rows_rejected": len(remaining_by_tree.get(tree_key, [])),
            "rows_unrepairable": sum(
                1
                for row in remaining_by_tree.get(tree_key, [])
                if cleaned_review_reason(row.get("review_reason")) in ALLOWED_OLLAMA_REASONS
            ),
            "rows_by_switch": {switch: len(repaired_rows)},
            "rows_by_version": {f"{switch}/{version}": len(repaired_rows)},
            "rows_by_intent": dict(Counter(collapse(row.get("intent")) for row in repaired_rows)),
            "repair_reasons": dict(sorted(repair_reasons_by_tree.get(tree_key, Counter()).items())),
            "remaining_review_reasons": dict(sorted(
                {
                    reason: count
                    for reason, count in review_reasons_by_tree.get(tree_key, Counter()).items()
                    if reason in {cleaned_review_reason(row.get("review_reason")) for row in remaining_by_tree.get(tree_key, [])}
                }.items()
            )),
            "ollama_model_used": args.ollama_model,
            "sample_repaired_rows": sample_repaired_by_tree.get(tree_key, [])[:10],
            "sample_rejected_rows": sample_rejected_by_tree.get(tree_key, [])[:10],
        }
        write_json(tree_dir / "ollama_repair_report.json", per_version_report)
        write_md(tree_dir / "ollama_repair_samples.md", build_samples_md(per_version_report, sample_repaired_by_tree.get(tree_key, []), sample_rejected_by_tree.get(tree_key, [])))

    # Build merged repaired dataset and remaining review outputs.
    for row in base_dataset_rows:
        key = json.dumps(row, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
        if key not in seen_dataset_keys:
            seen_dataset_keys.add(key)
            dataset_merged_rows.append(row)
    for row in accepted_rows_global:
        key = json.dumps(row, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
        if key not in seen_dataset_keys:
            seen_dataset_keys.add(key)
            dataset_merged_rows.append(row)

    merged_report = {
        "total_review_rows": total_review_rows,
        "rows_sent_to_ollama": rows_sent_to_ollama,
        "rows_repaired": rows_repaired,
        "rows_rejected": rows_rejected,
        "rows_unrepairable": rows_unrepairable,
        "rows_by_switch": dict(sorted(rows_by_switch.items())),
        "rows_by_version": dict(sorted(rows_by_version.items())),
        "rows_by_intent": dict(sorted(rows_by_intent.items())),
        "repair_reasons": dict(sorted(repair_reasons.items())),
        "remaining_review_reasons": dict(sorted(remaining_review_reasons.items())),
        "ollama_model_used": args.ollama_model,
        "invalid_jsonl_lines": invalid_jsonl_lines,
        "empty_input_text": empty_input_text,
        "empty_target_value": empty_target_value,
        "duplicates_removed": max(0, len(base_dataset_rows) + len(accepted_rows_global) - len(dataset_merged_rows)),
        "rows_fixed_deterministically": rows_fixed_deterministically,
        "sample_repaired_rows": accepted_rows_global[:10],
        "sample_rejected_rows": remaining_rows_global[:10],
    }

    write_jsonl(args.merged_output_dataset, dataset_merged_rows)
    write_jsonl(args.merged_output_review, remaining_rows_global)
    write_json(args.merged_output_report, merged_report)
    write_md(args.merged_output_samples, build_samples_md(merged_report, accepted_rows_global, remaining_rows_global))

    print("Ollama repair completed")
    print(f"Total review rows: {total_review_rows}")
    print(f"Rows sent to Ollama: {rows_sent_to_ollama}")
    print(f"Rows repaired: {rows_repaired}")
    print(f"Rows rejected: {rows_rejected}")
    print(f"Remaining review rows: {len(remaining_rows_global)}")
    print(f"Merged repaired dataset: {args.merged_output_dataset}")
    print(f"Merged remaining review file: {args.merged_output_review}")
    print("Verdict: complete")
    print(json.dumps(merged_report, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
