#!/usr/bin/env python3
"""Validate the cleaned Aruba AOS-CX JSONL splits."""

from __future__ import annotations

import argparse
import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Set, Tuple

from repair_dataset import (
    DATE_RE,
    DESCRIPTION_QUESTION_RE,
    NOT_DOCUMENTED_ANSWER,
    NOISE_PATTERNS,
    SPLIT_FILENAMES,
    TARGET_VERSION_RE,
    command_value,
    exact_bug_id,
    extract_qa,
    fact_group_key,
    has_noise,
    is_cli_row,
    is_description_question,
    is_syntax_question,
    is_version_history_row,
    normalize,
    option_present,
    read_jsonl,
    sha256_file,
    syntax_value,
)


def find_nonfinite_or_null(value: Any, path: str = "$") -> List[str]:
    errors: List[str] = []
    if value is None:
        errors.append(f"{path} is null")
    elif isinstance(value, float) and not math.isfinite(value):
        errors.append(f"{path} is non-finite")
    elif isinstance(value, Mapping):
        for key, item in value.items():
            errors.extend(find_nonfinite_or_null(item, f"{path}.{key}"))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            errors.extend(find_nonfinite_or_null(item, f"{path}[{index}]"))
    return errors


def validate_row(row: Mapping[str, Any], split: str, line_number: int) -> List[str]:
    prefix = f"{split}:{line_number}"
    errors: List[str] = []
    question, answer = extract_qa(row)
    messages = row.get("messages")
    if not isinstance(messages, list) or len(messages) < 2:
        errors.append(f"{prefix}: messages must contain user and assistant")
    if not question:
        errors.append(f"{prefix}: empty user content")
    if not answer:
        errors.append(f"{prefix}: empty assistant content")
    for detail in find_nonfinite_or_null(row):
        errors.append(f"{prefix}: {detail}")
    if has_noise(f"{question} {answer} {syntax_value(row)}"):
        errors.append(f"{prefix}: corruption pattern remains")

    if is_cli_row(row):
        command = command_value(row)
        syntax = syntax_value(row)
        if normalize(row.get("data_family")) != "cli_command_reference":
            errors.append(f"{prefix}: CLI data_family is not normalized")
        if normalize(row.get("source_type")) != "product_cli_reference":
            errors.append(f"{prefix}: CLI source_type is not product_cli_reference")
        if not command:
            errors.append(f"{prefix}: CLI command is empty")
        if normalize(row.get("command_name")) != normalize(command):
            errors.append(f"{prefix}: command_name does not match command")
        if is_syntax_question(question):
            expected = f"Syntax: {syntax}"
            if not syntax:
                errors.append(f"{prefix}: syntax question has no syntax field")
            elif answer != expected:
                errors.append(f"{prefix}: syntax answer is not exact")
        if is_description_question(question) and "syntax:" in answer.casefold():
            errors.append(f"{prefix}: description answer includes syntax")
        if row.get("augmentation_type") == "cli_syntax_paraphrase":
            if answer != f"Syntax: {syntax}":
                errors.append(f"{prefix}: paraphrase changed exact syntax answer")
        if row.get("augmentation_type") == "unsupported_cli_option":
            option = str(row.get("unsupported_option") or "")
            if answer != NOT_DOCUMENTED_ANSWER:
                errors.append(f"{prefix}: unsupported-option answer is not canonical")
            if not option:
                errors.append(f"{prefix}: unsupported option metadata is empty")
            elif option_present(option, command, [syntax]):
                errors.append(f"{prefix}: negative option appears in command/syntax")

    if normalize(row.get("data_family")) == "release_notes_bug":
        bug_id = exact_bug_id(row, question, answer)
        if not bug_id:
            errors.append(f"{prefix}: Bug row has no Bug ID")
        elif bug_id not in answer:
            errors.append(f"{prefix}: Bug ID is not preserved in assistant answer")

    if is_version_history_row(row):
        if re.search(r"(?i)\bwhen\b|\brelease\s+date\b|\breleased\b", question):
            if not TARGET_VERSION_RE.search(answer) or not DATE_RE.search(answer):
                errors.append(f"{prefix}: release-date answer lacks exact version/date")
        elif re.search(r"(?i)\bremarks?\b", question):
            if "remarks:" not in answer.casefold():
                errors.append(f"{prefix}: version remarks answer is not normalized")
    return errors


def distribution(rows: Iterable[Mapping[str, Any]], field: str) -> Counter[str]:
    return Counter(str(row.get(field) or "") for row in rows)


def max_distribution_delta(
    split_rows: Mapping[str, Sequence[Mapping[str, Any]]], field: str
) -> float:
    total = Counter()
    for rows in split_rows.values():
        total.update(distribution(rows, field))
    all_count = sum(total.values()) or 1
    worst = 0.0
    for split, rows in split_rows.items():
        split_counts = distribution(rows, field)
        split_total = len(rows) or 1
        for value, count in total.items():
            worst = max(worst, abs(split_counts[value] / split_total - count / all_count))
    return round(worst, 6)


def validate_directory(data_dir: Path, max_error_examples: int = 100) -> Dict[str, Any]:
    split_rows: Dict[str, List[Dict[str, Any]]] = {}
    errors: List[str] = []
    file_info: Dict[str, Any] = {}
    question_locations: Dict[str, Set[str]] = defaultdict(set)
    group_locations: Dict[str, Set[str]] = defaultdict(set)
    duplicate_questions: Counter[str] = Counter()
    metrics: Counter[str] = Counter()

    for split, filename in SPLIT_FILENAMES.items():
        path = data_dir / filename
        if not path.is_file():
            errors.append(f"Missing split: {path}")
            split_rows[split] = []
            continue
        rows: List[Dict[str, Any]] = []
        seen_questions: Set[str] = set()
        try:
            iterator = read_jsonl(path)
            for line_number, row in enumerate(iterator, 1):
                rows.append(row)
                row_errors = validate_row(row, split, line_number)
                if row_errors and len(errors) < max_error_examples:
                    errors.extend(row_errors[: max_error_examples - len(errors)])
                question, _ = extract_qa(row)
                question_key = normalize(question)
                if question_key in seen_questions:
                    duplicate_questions[split] += 1
                seen_questions.add(question_key)
                question_locations[question_key].add(split)
                group_locations[fact_group_key(row)].add(split)
                metrics["rows"] += 1
                metrics[f"rows_{split}"] += 1
                metrics["cli_rows"] += int(is_cli_row(row))
                metrics["syntax_rows"] += int(is_cli_row(row) and is_syntax_question(question))
                metrics["bug_rows"] += int(normalize(row.get("data_family")) == "release_notes_bug")
                metrics["version_history_rows"] += int(is_version_history_row(row))
                metrics["paraphrase_rows"] += int(row.get("augmentation_type") == "cli_syntax_paraphrase")
                metrics["negative_rows"] += int(row.get("augmentation_type") == "unsupported_cli_option")
        except Exception as exc:
            errors.append(f"Failed reading {path}: {exc}")
        split_rows[split] = rows
        file_info[split] = {
            "path": str(path),
            "rows": len(rows),
            "sha256": sha256_file(path) if path.is_file() else None,
        }

    question_overlap = {key: sorted(value) for key, value in question_locations.items() if len(value) > 1}
    group_overlap = {key: sorted(value) for key, value in group_locations.items() if len(value) > 1}
    if question_overlap:
        errors.append(f"Exact-question overlap across splits: {len(question_overlap)}")
    if group_overlap:
        errors.append(f"Fact-group overlap across splits: {len(group_overlap)}")
    if sum(duplicate_questions.values()):
        errors.append(f"Duplicate questions within splits: {dict(duplicate_questions)}")

    report = {
        "valid": not errors,
        "data_dir": str(data_dir),
        "files": file_info,
        "metrics": dict(metrics),
        "validation": {
            "error_count": len(errors),
            "error_examples": errors[:max_error_examples],
            "exact_question_overlap_count": len(question_overlap),
            "fact_group_overlap_count": len(group_overlap),
            "duplicate_questions_within_splits": dict(duplicate_questions),
            "max_distribution_delta": {
                field: max_distribution_delta(split_rows, field)
                for field in ("source_type", "data_family", "switch", "version")
            },
        },
    }
    return report


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", type=Path, default=Path("final_json_clean/all_switches"))
    parser.add_argument("--report-path", type=Path, default=None)
    parser.add_argument("--max-error-examples", type=int, default=100)
    return parser.parse_args(argv)


def main() -> None:
    args = parse_args()
    report = validate_directory(args.data_dir, args.max_error_examples)
    report_path = args.report_path or args.data_dir / "validation_report.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Valid: {report['valid']}")
    print(f"Rows: {report['metrics'].get('rows', 0)}")
    print(f"CLI rows: {report['metrics'].get('cli_rows', 0)}")
    print(f"Syntax rows: {report['metrics'].get('syntax_rows', 0)}")
    print(f"Bug rows: {report['metrics'].get('bug_rows', 0)}")
    print(f"Version-history rows: {report['metrics'].get('version_history_rows', 0)}")
    print(f"Exact-question overlap: {report['validation']['exact_question_overlap_count']}")
    print(f"Fact-group overlap: {report['validation']['fact_group_overlap_count']}")
    print(f"Errors: {report['validation']['error_count']}")
    print(f"Report: {report_path}")
    if not report["valid"]:
        for error in report["validation"]["error_examples"][:20]:
            print(f"ERROR: {error}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
