"""Final low-row rerun and quality-audit stage for Aruba product docs.

This script is deliberately audit/recovery tooling around the existing product
documentation parser. It does not loosen validation filters, use LLMs, or touch
release-note preprocessing.
"""

from __future__ import annotations

import argparse
import csv
import json
import random
import shutil
import subprocess
import sys
import time
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from audit_missing_product_docs import parse_folder_version
from preprocess_product_docs import _duplicate_questions_final, _final_issue_counts, _rows_with_underscore_version
from project.src.product_doc_validator import validate_qa_row


BASE_DIR = Path(__file__).resolve().parent
DEFAULT_RAW_ROOT = BASE_DIR / "markitdown_cli_output" / "Raw_Data_Product"
DEFAULT_OUTPUT_ROOT = BASE_DIR / "final_json" / "product_docs" / "full_product_docs"
DEFAULT_REPORT_DIR = BASE_DIR / "final_json" / "product_docs"
DEFAULT_FINAL_JSONL = DEFAULT_REPORT_DIR / "train_chat_product_docs.jsonl"
LOW300_TARGET_CSV = DEFAULT_REPORT_DIR / "low300_rerun_targets.csv"
LOW300_TARGET_JSON = DEFAULT_REPORT_DIR / "low300_rerun_targets.json"
LOW300_RESULT_CSV = DEFAULT_REPORT_DIR / "low300_rerun_results.csv"
LOW300_QUALITY_JSON = DEFAULT_REPORT_DIR / "low300_rerun_quality_report.json"
FULL_SUMMARY_CSV = DEFAULT_REPORT_DIR / "full_product_docs_summary.csv"
FULL_QUALITY_JSON = DEFAULT_REPORT_DIR / "full_product_docs_quality_report.json"
BALANCE_JSON = DEFAULT_REPORT_DIR / "full_product_docs_balance_report.json"
BALANCE_CSV = DEFAULT_REPORT_DIR / "full_product_docs_balance_report.csv"
SAMPLE_JSONL = DEFAULT_REPORT_DIR / "final_product_docs_sample_review.jsonl"
SAMPLE_CSV = DEFAULT_REPORT_DIR / "final_product_docs_sample_review.csv"

STRICT_ZERO_COUNTERS = [
    "parameter_fragment_rows_final",
    "parameter_description_topic_rows_final",
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
    "fake_command_heading_rows_final",
    "fake_command_name_rows_final",
    "output_like_rows_final",
    "major_ocr_damage_rows_final",
    "spacing_ocr_rows_final",
    "configuration_dump_rows_final",
    "show_output_table_rows_final",
    "bullet_fragment_rows_final",
    "page_header_usecase_rows_final",
]


@dataclass(frozen=True)
class Target:
    switch: str
    version: str
    subversion: str
    folder_version: str
    raw_folder_exists: bool
    raw_md_files: int
    raw_total_size_mb: float
    old_final_rows: int
    rows_per_md_file: float
    row_count_status: str
    audit_priority: str
    rows_per_file_note: str
    raw_path: str
    output_path: str
    rerun_status: str
    reason: str


def count_lines(path: Path) -> int:
    if not path.exists():
        return 0
    with path.open("r", encoding="utf-8-sig", errors="replace") as handle:
        return sum(1 for line in handle if line.strip())


def read_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8-sig", errors="replace"))
    except json.JSONDecodeError:
        return {}


def load_jsonl(path: Path) -> tuple[list[dict[str, Any]], int]:
    rows: list[dict[str, Any]] = []
    parse_errors = 0
    if not path.exists():
        return rows, parse_errors
    with path.open("r", encoding="utf-8-sig", errors="replace") as handle:
        for line in handle:
            line = line.strip().lstrip("\ufeff")
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                parse_errors += 1
    return rows, parse_errors


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def classify_row_count(final_rows: int, raw_md_files: int) -> tuple[str, str]:
    if final_rows == 0:
        return "zero_rows", "must_check"
    if final_rows < 50:
        return "very_low_rows", "must_check"
    if final_rows < 150 and raw_md_files >= 10:
        return "suspicious_low_rows", "check"
    if final_rows < 300:
        return "low_rows", "rerun_with_quality_protection"
    return "ok", "no_action"


def rows_per_file_note(rows_per_md_file: float) -> str:
    if rows_per_md_file < 5:
        return "low_yield_check"
    if rows_per_md_file <= 20:
        return "acceptable_small_docs"
    return "good_yield"


def discover_targets(raw_root: Path, output_root: Path) -> list[Target]:
    targets: list[Target] = []
    for switch_dir in sorted(path for path in raw_root.iterdir() if path.is_dir()):
        for version_dir in sorted(path for path in switch_dir.iterdir() if path.is_dir()):
            switch = switch_dir.name
            folder_version = version_dir.name
            version, subversion = parse_folder_version(folder_version)
            raw_md_files = sorted(version_dir.glob("*.md"))
            raw_total_size_mb = sum(path.stat().st_size for path in raw_md_files) / (1024 * 1024)
            output_path = output_root / switch / folder_version / "train_chat.jsonl"
            final_rows = count_lines(output_path)
            if final_rows >= 300:
                continue
            raw_folder_exists = version_dir.exists()
            rows_per_md = round(final_rows / len(raw_md_files), 3) if raw_md_files else 0.0
            row_status, priority = classify_row_count(final_rows, len(raw_md_files))
            if not raw_folder_exists or not raw_md_files:
                rerun_status = "skipped_no_raw_markdown"
                reason = "raw folder is missing or contains no Markdown files"
            else:
                rerun_status = "pending"
                reason = "final_rows < 300; rerun for recovery testing with strict quality protection"
            targets.append(
                Target(
                    switch=switch,
                    version=version,
                    subversion=subversion,
                    folder_version=folder_version,
                    raw_folder_exists=raw_folder_exists,
                    raw_md_files=len(raw_md_files),
                    raw_total_size_mb=round(raw_total_size_mb, 3),
                    old_final_rows=final_rows,
                    rows_per_md_file=rows_per_md,
                    row_count_status=row_status,
                    audit_priority=priority,
                    rows_per_file_note=rows_per_file_note(rows_per_md),
                    raw_path=str(version_dir),
                    output_path=str(output_path),
                    rerun_status=rerun_status,
                    reason=reason,
                )
            )
    return targets


def target_to_row(target: Target) -> dict[str, Any]:
    return {
        "switch": target.switch,
        "version": target.version,
        "subversion": target.subversion,
        "folder_version": target.folder_version,
        "raw_folder_exists": target.raw_folder_exists,
        "raw_md_files": target.raw_md_files,
        "raw_total_size_mb": target.raw_total_size_mb,
        "old_final_rows": target.old_final_rows,
        "rows_per_md_file": target.rows_per_md_file,
        "row_count_status": target.row_count_status,
        "audit_priority": target.audit_priority,
        "rows_per_file_note": target.rows_per_file_note,
        "raw_path": target.raw_path,
        "output_path": target.output_path,
        "rerun_status": target.rerun_status,
        "reason": target.reason,
    }


def messages_pair(row: dict[str, Any]) -> tuple[str, str]:
    user = ""
    assistant = ""
    messages = row.get("messages") or []
    if isinstance(messages, list):
        for message in messages:
            if not isinstance(message, dict):
                continue
            if message.get("role") == "user":
                user = str(message.get("content", "") or "")
            elif message.get("role") == "assistant":
                assistant = str(message.get("content", "") or "")
    return user, assistant


def duplicate_qa_pairs(rows: list[dict[str, Any]]) -> int:
    counts: Counter[tuple[str, str]] = Counter(messages_pair(row) for row in rows)
    return sum(count - 1 for count in counts.values() if count > 1)


def event_log_ratio(rows: list[dict[str, Any]]) -> float:
    if not rows:
        return 0.0
    count = sum(1 for row in rows if row.get("data_family") == "event_log_reference")
    return count / len(rows)


def validate_candidate(candidate_dir: Path) -> dict[str, Any]:
    train_path = candidate_dir / "train_chat.jsonl"
    quality_path = candidate_dir / "quality_report.json"
    rows, parse_errors = load_jsonl(train_path)
    quality_report = read_json(quality_path)
    validation_drops: Counter[str] = Counter()
    for row in rows:
        valid, reason = validate_qa_row(row, require_grounding=True)
        if not valid:
            validation_drops[reason] += 1
    final_issues = _final_issue_counts(rows)
    event_ratio = float(quality_report.get("event_log_ratio_after_cap", event_log_ratio(rows)) or 0.0)
    checks: dict[str, Any] = {
        "jsonl_parse_errors": parse_errors,
        "exact_duplicate_qa_pairs": duplicate_qa_pairs(rows),
        "duplicate_questions_final": _duplicate_questions_final(rows),
        "rows_with_underscore_version_question": _rows_with_underscore_version(rows),
        "parameter_rows_generated": int(quality_report.get("parameter_rows_generated", 0) or 0),
        "command_example_rows_generated": int(quality_report.get("command_example_rows_generated", 0) or 0),
        "event_log_ratio_after_cap": event_ratio,
        "validation_drops_if_revalidated": sum(validation_drops.values()),
        "validation_drop_reasons_if_revalidated": dict(sorted(validation_drops.items())),
    }
    for key in STRICT_ZERO_COUNTERS:
        checks[key] = int(final_issues.get(key, 0) or quality_report.get(key, 0) or 0)
    failed = [
        key
        for key, value in checks.items()
        if (
            key != "event_log_ratio_after_cap"
            and key != "validation_drop_reasons_if_revalidated"
            and value != 0
        )
    ]
    if event_ratio > 0.15:
        failed.append("event_log_ratio_after_cap")
    return {
        "rows": rows,
        "row_count": len(rows),
        "checks": checks,
        "validation_passed": not failed,
        "failed_checks": failed,
    }


def safe_name(target: Target) -> str:
    return f"{target.switch}_{target.folder_version}".replace("/", "_").replace("\\", "_")


def run_one_target(
    *,
    target: Target,
    raw_root: Path,
    candidate_root: Path,
    log_dir: Path,
    output_root: Path,
    workers_per_folder: int,
    python_exe: str,
    execute: bool,
) -> dict[str, Any]:
    result = target_to_row(target)
    result.update(
        {
            "old_final_rows": target.old_final_rows,
            "new_final_rows": target.old_final_rows,
            "rows_recovered": 0,
            "rows_per_md_file_before": target.rows_per_md_file,
            "rows_per_md_file_after": target.rows_per_md_file,
            "validation_passed": False,
            "backup_path": "",
            "candidate_path": "",
            "stdout_log": "",
            "stderr_log": "",
            "duration_seconds": 0.0,
            "failed_checks": "",
        }
    )
    if not target.raw_folder_exists or target.raw_md_files <= 0:
        result["rerun_status"] = "skipped_no_raw_markdown"
        result["reason"] = "raw folder is missing or contains no Markdown files"
        return result
    if not execute:
        result["rerun_status"] = "dry_run"
        result["reason"] = "dry run; no parser command executed"
        return result

    start = time.monotonic()
    name = safe_name(target)
    final_jsonl = log_dir / f"{name}.final.jsonl"
    stdout_log = log_dir / f"{name}.out.log"
    stderr_log = log_dir / f"{name}.err.log"
    command = [
        python_exe,
        "-u",
        "preprocess_product_docs.py",
        "--input-root",
        str(raw_root),
        "--output-root",
        str(candidate_root),
        "--final-jsonl",
        str(final_jsonl),
        "--switch-name",
        target.switch,
        "--version",
        target.folder_version,
        "--workers",
        str(workers_per_folder),
    ]
    log_dir.mkdir(parents=True, exist_ok=True)
    with stdout_log.open("w", encoding="utf-8") as stdout_handle, stderr_log.open("w", encoding="utf-8") as stderr_handle:
        completed = subprocess.run(
            command,
            cwd=BASE_DIR,
            stdout=stdout_handle,
            stderr=stderr_handle,
            text=True,
            check=False,
        )
    duration = round(time.monotonic() - start, 1)
    candidate_dir = candidate_root / target.switch / target.folder_version
    candidate_train = candidate_dir / "train_chat.jsonl"
    result["stdout_log"] = str(stdout_log)
    result["stderr_log"] = str(stderr_log)
    result["candidate_path"] = str(candidate_train)
    result["duration_seconds"] = duration
    result["returncode"] = completed.returncode
    if completed.returncode != 0:
        result["rerun_status"] = "rejected_quality_failed"
        result["reason"] = f"parser subprocess failed with return code {completed.returncode}"
        return result

    validation = validate_candidate(candidate_dir)
    new_rows = int(validation["row_count"])
    rows_per_after = round(new_rows / target.raw_md_files, 3) if target.raw_md_files else 0.0
    result["new_final_rows"] = new_rows
    result["rows_recovered"] = new_rows - target.old_final_rows
    result["rows_per_md_file_after"] = rows_per_after
    result["validation_passed"] = bool(validation["validation_passed"])
    result["failed_checks"] = ";".join(validation["failed_checks"])
    result["validation_checks"] = validation["checks"]

    output_dir = output_root / target.switch / target.folder_version
    output_train = output_dir / "train_chat.jsonl"
    candidate_compare_path = output_dir / "train_chat.low300_candidate.jsonl"
    backup_path = output_dir / "train_chat.before_low300_rerun.jsonl"
    result["backup_path"] = str(backup_path)

    if not validation["validation_passed"]:
        output_dir.mkdir(parents=True, exist_ok=True)
        if candidate_train.exists():
            shutil.copy2(candidate_train, candidate_compare_path)
            result["candidate_path"] = str(candidate_compare_path)
        result["rerun_status"] = "rejected_quality_failed"
        result["reason"] = f"quality validation failed: {result['failed_checks']}"
        return result

    if new_rows < target.old_final_rows:
        output_dir.mkdir(parents=True, exist_ok=True)
        if candidate_train.exists():
            shutil.copy2(candidate_train, candidate_compare_path)
            result["candidate_path"] = str(candidate_compare_path)
        result["rerun_status"] = "needs_manual_compare"
        result["reason"] = "candidate passed quality but has fewer rows than existing output"
        return result

    output_dir.mkdir(parents=True, exist_ok=True)
    if output_train.exists():
        shutil.copy2(output_train, backup_path)
    for filename in ("train_chat.jsonl", "quality_report.json", "structured_records.json"):
        source = candidate_dir / filename
        if source.exists():
            shutil.copy2(source, output_dir / filename)
    result["candidate_path"] = str(candidate_train)
    result["rerun_status"] = "accepted_improved" if new_rows > target.old_final_rows else "accepted_unchanged"
    result["reason"] = "candidate passed quality and new_final_rows >= old_final_rows"
    return result


def rebuild_combined_jsonl(output_root: Path, final_jsonl: Path) -> int:
    final_jsonl.parent.mkdir(parents=True, exist_ok=True)
    temp_path = final_jsonl.with_suffix(".jsonl.low300_tmp")
    count = 0
    with temp_path.open("w", encoding="utf-8", newline="") as out_handle:
        for train_file in sorted(output_root.glob("*/*/train_chat.jsonl")):
            with train_file.open("r", encoding="utf-8-sig", errors="replace") as in_handle:
                for line in in_handle:
                    line = line.lstrip("\ufeff")
                    if not line.strip():
                        continue
                    out_handle.write(line if line.endswith("\n") else f"{line}\n")
                    count += 1
    temp_path.replace(final_jsonl)
    return count


def build_summary_rows(raw_root: Path, output_root: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for switch_dir in sorted(path for path in raw_root.iterdir() if path.is_dir()):
        for version_dir in sorted(path for path in switch_dir.iterdir() if path.is_dir()):
            switch = switch_dir.name
            folder_version = version_dir.name
            version, subversion = parse_folder_version(folder_version)
            raw_md_files = len(list(version_dir.glob("*.md")))
            output_path = output_root / switch / folder_version / "train_chat.jsonl"
            final_rows = count_lines(output_path)
            rows_per_md = round(final_rows / raw_md_files, 3) if raw_md_files else 0.0
            row_status, priority = classify_row_count(final_rows, raw_md_files)
            rows.append(
                {
                    "switch": switch,
                    "version": version,
                    "subversion": subversion,
                    "folder_version": folder_version,
                    "raw_md_files": raw_md_files,
                    "final_rows": final_rows,
                    "rows_per_md_file": rows_per_md,
                    "row_count_status": row_status,
                    "audit_priority": priority,
                    "raw_path": str(version_dir),
                    "output_path": str(output_path),
                }
            )
    return rows


def build_quality_summary(rows: list[dict[str, Any]], final_jsonl: Path) -> dict[str, Any]:
    jsonl_rows, parse_errors = load_jsonl(final_jsonl)
    final_issues = _final_issue_counts(jsonl_rows)
    exact_duplicates = duplicate_qa_pairs(jsonl_rows)
    duplicate_questions = _duplicate_questions_final(jsonl_rows)
    underscore_questions = _rows_with_underscore_version(jsonl_rows)
    event_ratio = event_log_ratio(jsonl_rows)
    required_zero = {
        "exact_duplicate_qa_pairs": exact_duplicates,
        "duplicate_questions_final": duplicate_questions,
        "syntax_command_root_mismatch_rows_final": final_issues.get("syntax_command_root_mismatch_rows_final", 0),
        "unbalanced_field_rows_final": final_issues.get("unbalanced_field_rows_final", 0),
        "output_like_rows_final": final_issues.get("output_like_rows_final", 0),
        "configuration_dump_rows_final": final_issues.get("configuration_dump_rows_final", 0),
        "show_output_table_rows_final": final_issues.get("show_output_table_rows_final", 0),
        "major_ocr_damage_rows_final": final_issues.get("major_ocr_damage_rows_final", 0),
        "spacing_ocr_rows_final": final_issues.get("spacing_ocr_rows_final", 0),
    }
    ready = (
        parse_errors == 0
        and event_ratio <= 0.15
        and all(value == 0 for value in required_zero.values())
    )
    status_counts = Counter(row["row_count_status"] for row in rows)
    priority_counts = Counter(row["audit_priority"] for row in rows)
    return {
        "total_product_doc_rows": len(jsonl_rows),
        "total_switches": len({row["switch"] for row in rows}),
        "total_switch_version_folders": len(rows),
        "jsonl_parse_errors": parse_errors,
        "exact_duplicate_qa_pairs": exact_duplicates,
        "duplicate_questions_final": duplicate_questions,
        "rows_with_underscore_version_question": underscore_questions,
        "event_log_ratio": round(event_ratio, 6),
        "row_count_status_counts": dict(sorted(status_counts.items())),
        "audit_priority_counts": dict(sorted(priority_counts.items())),
        "final_issue_counts": dict(sorted(final_issues.items())),
        "required_zero_checks": required_zero,
        "ready_to_combine_with_release_notes": ready,
    }


def balance_reports(final_jsonl: Path) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    rows, parse_errors = load_jsonl(final_jsonl)
    total = len(rows)
    dimensions = {
        "switch": Counter(),
        "version": Counter(),
        "source_type": Counter(),
        "data_family": Counter(),
        "document_title": Counter(),
    }
    for row in rows:
        for dimension in dimensions:
            value = str(row.get(dimension, "") or "unknown")
            dimensions[dimension][value] += 1
    csv_rows: list[dict[str, Any]] = []
    for dimension, counter in dimensions.items():
        for value, count in sorted(counter.items()):
            csv_rows.append(
                {
                    "dimension": dimension,
                    "value": value,
                    "count": count,
                    "percentage": round(count / total, 6) if total else 0.0,
                }
            )
    family_counts = dimensions["data_family"]
    cli_rows = family_counts.get("cli_command_reference", 0)
    show_rows = family_counts.get("show_command_reference", 0)
    concept_rows = family_counts.get("concept_explanation", 0)
    procedure_rows = family_counts.get("configuration_procedure", 0)
    security_rows = family_counts.get("security_policy", 0)
    routing_rows = family_counts.get("routing_feature", 0)
    event_rows = family_counts.get("event_log_reference", 0)
    summary = {
        "total_rows": total,
        "jsonl_parse_errors": parse_errors,
        "cli_command_reference_rows": cli_rows,
        "show_command_reference_rows": show_rows,
        "cli_plus_show_ratio": round((cli_rows + show_rows) / total, 6) if total else 0.0,
        "concept_rows": concept_rows,
        "procedure_rows": procedure_rows,
        "concept_plus_procedure_ratio": round(
            (concept_rows + procedure_rows + security_rows + routing_rows) / total,
            6,
        )
        if total
        else 0.0,
        "event_log_rows": event_rows,
        "event_log_ratio": round(event_rows / total, 6) if total else 0.0,
        "target_balance_guidance": {
            "cli_plus_show_ratio_preferred": "0.45 to 0.60",
            "concept_procedure_security_routing_ratio_preferred": "0.25 to 0.40",
            "event_log_ratio_required_max": 0.15,
        },
        "counts_by_switch": dict(sorted(dimensions["switch"].items())),
        "counts_by_version": dict(sorted(dimensions["version"].items())),
        "counts_by_source_type": dict(sorted(dimensions["source_type"].items())),
        "counts_by_data_family": dict(sorted(dimensions["data_family"].items())),
        "counts_by_document_title": dict(sorted(dimensions["document_title"].items())),
    }
    return summary, csv_rows


def sample_review(final_jsonl: Path, sample_size: int = 5, seed: int = 4100) -> list[dict[str, Any]]:
    rows, _ = load_jsonl(final_jsonl)
    rng = random.Random(seed)
    buckets: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        switch = str(row.get("switch", "") or "unknown")
        version = str(row.get("version", "") or "unknown")
        source_type = str(row.get("source_type", "") or "unknown")
        data_family = str(row.get("data_family", "") or "unknown")
        buckets[("switch_version", f"{switch}/{version}")].append(row)
        buckets[("source_type", source_type)].append(row)
        buckets[("data_family", data_family)].append(row)
    samples: list[dict[str, Any]] = []
    seen: set[tuple[str, str, str]] = set()
    for (basis, key), bucket_rows in sorted(buckets.items()):
        chosen = rng.sample(bucket_rows, min(sample_size, len(bucket_rows)))
        for row in chosen:
            question, answer = messages_pair(row)
            version_value = str(row.get("version", "") or "")
            version_base, subversion = parse_folder_version(version_value)
            sample = {
                "sample_basis": basis,
                "sample_key": key,
                "switch": row.get("switch", ""),
                "version": version_base,
                "subversion": subversion,
                "source_type": row.get("source_type", ""),
                "data_family": row.get("data_family", ""),
                "document_title": row.get("document_title", ""),
                "section": row.get("section", ""),
                "source_file": row.get("source_file", ""),
                "user_question": question,
                "assistant_answer": answer,
            }
            dedupe_key = (basis, key, question)
            if dedupe_key in seen:
                continue
            seen.add(dedupe_key)
            samples.append(sample)
    return samples


def run_stage(args: argparse.Namespace) -> dict[str, Any]:
    raw_root = args.raw_root
    output_root = args.output_root
    report_dir = args.report_dir
    final_jsonl = args.final_jsonl
    timestamp = args.run_id or time.strftime("%Y%m%d_%H%M%S")
    candidate_root = report_dir / "_low300_rerun_candidates" / f"run_{timestamp}"
    log_dir = report_dir / "_low300_rerun_logs" / f"run_{timestamp}"
    progress_log = log_dir / "low300_rerun_progress.log"
    log_dir.mkdir(parents=True, exist_ok=True)

    targets = discover_targets(raw_root, output_root)
    target_rows = [target_to_row(target) for target in targets]
    target_fieldnames = [
        "switch",
        "version",
        "subversion",
        "folder_version",
        "raw_folder_exists",
        "raw_md_files",
        "raw_total_size_mb",
        "old_final_rows",
        "rows_per_md_file",
        "row_count_status",
        "audit_priority",
        "rows_per_file_note",
        "raw_path",
        "output_path",
        "rerun_status",
        "reason",
    ]
    write_csv(LOW300_TARGET_CSV, target_rows, target_fieldnames)
    write_json(LOW300_TARGET_JSON, {"summary": {"folders_under_300_before": len(targets)}, "rows": target_rows})

    total_rows_before = sum(count_lines(path) for path in output_root.glob("*/*/train_chat.jsonl"))
    eligible = [target for target in targets if target.raw_folder_exists and target.raw_md_files > 0]
    results: list[dict[str, Any]] = []
    progress_log.write_text(
        f"Started low300 stage at {time.strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"Targets under 300: {len(targets)}\n"
        f"Eligible reruns: {len(eligible)}\n"
        f"Execute: {args.execute}\n",
        encoding="utf-8",
    )

    if args.execute:
        with ThreadPoolExecutor(max_workers=args.jobs) as executor:
            future_map = {
                executor.submit(
                    run_one_target,
                    target=target,
                    raw_root=raw_root,
                    candidate_root=candidate_root,
                    log_dir=log_dir,
                    output_root=output_root,
                    workers_per_folder=args.workers_per_folder,
                    python_exe=args.python,
                    execute=True,
                ): target
                for target in eligible
            }
            completed = 0
            for future in as_completed(future_map):
                target = future_map[future]
                completed += 1
                try:
                    result = future.result()
                except Exception as exc:  # noqa: BLE001 - keep batch running and report.
                    result = target_to_row(target)
                    result.update(
                        {
                            "new_final_rows": target.old_final_rows,
                            "rows_recovered": 0,
                            "rows_per_md_file_before": target.rows_per_md_file,
                            "rows_per_md_file_after": target.rows_per_md_file,
                            "validation_passed": False,
                            "rerun_status": "rejected_quality_failed",
                            "reason": f"exception during rerun: {exc}",
                            "backup_path": "",
                            "candidate_path": "",
                        }
                    )
                results.append(result)
                write_csv(LOW300_RESULT_CSV, results, LOW300_RESULT_COLUMNS)
                with progress_log.open("a", encoding="utf-8") as handle:
                    handle.write(
                        f"[{completed}/{len(eligible)}] {target.switch}/{target.folder_version} "
                        f"old={target.old_final_rows} new={result.get('new_final_rows')} "
                        f"status={result.get('rerun_status')}\n"
                    )
    else:
        for target in eligible:
            results.append(
                run_one_target(
                    target=target,
                    raw_root=raw_root,
                    candidate_root=candidate_root,
                    log_dir=log_dir,
                    output_root=output_root,
                    workers_per_folder=args.workers_per_folder,
                    python_exe=args.python,
                    execute=False,
                )
            )

    skipped = [
        target_to_row(target)
        | {
            "new_final_rows": target.old_final_rows,
            "rows_recovered": 0,
            "rows_per_md_file_before": target.rows_per_md_file,
            "rows_per_md_file_after": target.rows_per_md_file,
            "validation_passed": False,
            "backup_path": "",
            "candidate_path": "",
        }
        for target in targets
        if not target.raw_folder_exists or target.raw_md_files <= 0
    ]
    all_results = sorted(results + skipped, key=lambda row: (str(row["switch"]), str(row["folder_version"])))
    write_csv(LOW300_RESULT_CSV, all_results, LOW300_RESULT_COLUMNS)

    if args.execute:
        rebuild_combined_jsonl(output_root, final_jsonl)

    total_rows_after = sum(count_lines(path) for path in output_root.glob("*/*/train_chat.jsonl"))
    accepted = [row for row in all_results if str(row.get("rerun_status", "")).startswith("accepted_")]
    improved = [row for row in accepted if int(row.get("rows_recovered", 0) or 0) > 0]
    unchanged = [row for row in accepted if int(row.get("rows_recovered", 0) or 0) == 0]
    rejected = [row for row in all_results if row.get("rerun_status") == "rejected_quality_failed"]
    manual = [row for row in all_results if row.get("rerun_status") == "needs_manual_compare"]
    no_raw = [row for row in all_results if row.get("rerun_status") == "skipped_no_raw_markdown"]
    low300_summary = {
        "folders_under_300_before": len(targets),
        "folders_rerun": len(results) if args.execute else 0,
        "folders_skipped_no_raw": len(no_raw),
        "folders_improved": len(improved),
        "folders_unchanged": len(unchanged),
        "folders_rejected_quality_failed": len(rejected),
        "folders_needs_manual_compare": len(manual),
        "total_rows_before": total_rows_before,
        "total_rows_after": total_rows_after,
        "rows_recovered": total_rows_after - total_rows_before,
        "validation_passed_for_all_accepted_outputs": all(bool(row.get("validation_passed")) for row in accepted),
    }

    summary_rows = build_summary_rows(raw_root, output_root)
    write_csv(
        FULL_SUMMARY_CSV,
        summary_rows,
        [
            "switch",
            "version",
            "subversion",
            "folder_version",
            "raw_md_files",
            "final_rows",
            "rows_per_md_file",
            "row_count_status",
            "audit_priority",
            "raw_path",
            "output_path",
        ],
    )
    quality_summary = build_quality_summary(summary_rows, final_jsonl)
    quality_summary["low300_rerun"] = low300_summary
    write_json(FULL_QUALITY_JSON, quality_summary)
    write_json(LOW300_QUALITY_JSON, {"summary": low300_summary, "results": all_results, "final_quality": quality_summary})

    balance_summary, balance_csv_rows = balance_reports(final_jsonl)
    write_json(BALANCE_JSON, balance_summary)
    write_csv(BALANCE_CSV, balance_csv_rows, ["dimension", "value", "count", "percentage"])

    samples = sample_review(final_jsonl)
    write_csv(
        SAMPLE_CSV,
        samples,
        [
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
        ],
    )
    with SAMPLE_JSONL.open("w", encoding="utf-8", newline="") as handle:
        for sample in samples:
            handle.write(json.dumps(sample, ensure_ascii=False) + "\n")

    with progress_log.open("a", encoding="utf-8") as handle:
        handle.write(f"Finished low300 stage at {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        handle.write(f"Rows recovered: {low300_summary['rows_recovered']}\n")
        handle.write(f"Quality ready: {quality_summary['ready_to_combine_with_release_notes']}\n")

    return {
        "low300_summary": low300_summary,
        "quality_summary": quality_summary,
        "balance_summary": balance_summary,
        "sample_rows": len(samples),
        "progress_log": str(progress_log),
    }


LOW300_RESULT_COLUMNS = [
    "switch",
    "version",
    "subversion",
    "folder_version",
    "raw_md_files",
    "old_final_rows",
    "new_final_rows",
    "rows_recovered",
    "rows_per_md_file_before",
    "rows_per_md_file_after",
    "validation_passed",
    "rerun_status",
    "reason",
    "output_path",
    "backup_path",
    "candidate_path",
    "returncode",
    "duration_seconds",
    "failed_checks",
    "stdout_log",
    "stderr_log",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run final low300 product-doc rerun and audit stage.")
    parser.add_argument("--raw-root", type=Path, default=DEFAULT_RAW_ROOT)
    parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT_ROOT)
    parser.add_argument("--report-dir", type=Path, default=DEFAULT_REPORT_DIR)
    parser.add_argument("--final-jsonl", type=Path, default=DEFAULT_FINAL_JSONL)
    parser.add_argument("--python", default=sys.executable)
    parser.add_argument("--jobs", type=int, default=4, help="Concurrent switch/version rerun jobs.")
    parser.add_argument("--workers-per-folder", type=int, default=2, help="Parser workers per rerun job.")
    parser.add_argument("--run-id", default="", help="Optional stable run id for logs/candidates.")
    parser.add_argument("--execute", action="store_true", help="Actually rerun and overwrite accepted outputs.")
    return parser.parse_args()


def main() -> None:
    summary = run_stage(parse_args())
    low300 = summary["low300_summary"]
    quality = summary["quality_summary"]
    balance = summary["balance_summary"]
    print(f"Folders under 300 before: {low300['folders_under_300_before']}")
    print(f"Folders rerun: {low300['folders_rerun']}")
    print(f"Folders improved: {low300['folders_improved']}")
    print(f"Folders unchanged: {low300['folders_unchanged']}")
    print(f"Rejected quality failed: {low300['folders_rejected_quality_failed']}")
    print(f"Needs manual compare: {low300['folders_needs_manual_compare']}")
    print(f"Rows before: {low300['total_rows_before']}")
    print(f"Rows after: {low300['total_rows_after']}")
    print(f"Rows recovered: {low300['rows_recovered']}")
    print(f"Ready to combine with release notes: {quality['ready_to_combine_with_release_notes']}")
    print(f"Event log ratio: {quality['event_log_ratio']}")
    print(f"CLI+show ratio: {balance['cli_plus_show_ratio']}")
    print(f"Concept/procedure/security/routing ratio: {balance['concept_plus_procedure_ratio']}")
    print(f"Sample review rows: {summary['sample_rows']}")
    print(f"Progress log: {summary['progress_log']}")


if __name__ == "__main__":
    main()
