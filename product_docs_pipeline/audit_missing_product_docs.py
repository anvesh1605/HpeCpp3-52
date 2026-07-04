"""Audit missing, zero-row, and low-output Aruba product-doc folders.

This script is intentionally separate from the product documentation parser. It
does not loosen validators or regenerate data; it only compares the raw
MarkItDown Markdown tree with the generated full product-doc output tree.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any


BASE_DIR = Path(__file__).resolve().parent
DEFAULT_RAW_ROOT = BASE_DIR / "markitdown_cli_output" / "Raw_Data_Product"
DEFAULT_OUTPUT_ROOT = BASE_DIR / "final_json" / "product_docs" / "full_product_docs"
DEFAULT_REPORT_DIR = BASE_DIR / "final_json" / "product_docs"
DEFAULT_FINAL_JSONL = BASE_DIR / "final_json" / "product_docs" / "train_chat_product_docs.jsonl"

LOW_ROW_RAW_MD_THRESHOLD = 10
LOW_ROW_FINAL_ROW_THRESHOLD = 50

REQUIRED_REVIEW_FOLDERS = {
    ("8100", "10_17_1000"),
    ("8100", "10_18"),
    ("8320", "10_17_1000"),
    ("8325", "10_18"),
    ("6100", "10_07"),
    ("6200", "10_07"),
    ("6200", "10_17_1000"),
    ("6200", "10_18"),
    ("8360", "10_07"),
}

COMMAND_LINE_RE = re.compile(
    r"^\s*(?:switch(?:\([^)]*\))?[>#]\s*)?"
    r"(?:show|clear|configure|config|copy|boot|checkpoint|erase|diag|ping|traceroute|"
    r"interface|vlan|vrf|router|ip|ipv6|aaa|access-list|snmp-server|logging|ntp|"
    r"radius|tacacs|crypto|ssh|https-server|rest|vsx|qos|class|policy|apply|"
    r"feature|bfd|erps|neighbor|redundancy|hsc|no)\b",
    re.IGNORECASE,
)
PAGE_HEADER_FOOTER_RE = re.compile(
    r"(?:AOS-CX\s*[\d.]+.*Guide\s*\|\s*User\s*Guide|"
    r"\b[A-Za-z][A-Za-z ]{1,80}\s*\|\s*\d+\b|"
    r"\bContents\s*\|\s*\d+\b|"
    r"\bAbout this Document\s*\|\s*\d+\b)",
    re.IGNORECASE,
)
SUPPORT_FRAGMENT_RE = re.compile(
    r"(?:Accessing Aruba Support|Accessing HPE Aruba Networking Support|"
    r"Aruba Support Portal|HPE Aruba Networking Support Services|"
    r"Support and Other Resources|Other useful sites|Documentation feedback|"
    r"End-of-Life information|Warranty information|Privacy|Terms of use)",
    re.IGNORECASE,
)
RELEASE_NOTE_RE = re.compile(
    r"(?:Resolved issues|Known issues|Fixed issues|Upgrade information|"
    r"Version history|Behavior changes|Symptom|Scenario|Workaround|Bug ID)",
    re.IGNORECASE,
)
OUTPUT_DUMP_RE = re.compile(
    r"(?:Status and Counters|^-{5,}$|^\s*(?:Port|Interface|VLAN|VRF|Name)\s+\S+\s+\S+|"
    r"\bswitch(?:\([^)]*\))?[>#])",
    re.IGNORECASE,
)
OCR_DAMAGE_RE = re.compile(
    r"(?:Thiscommand|Thisconfiguration|The noform|no formof|formofthis|"
    r"Specifies[a-z]{4,}|Configures[a-z]{4,}|Displays[a-z]{4,}|"
    r"[a-z]{20,}(?:command|configuration|interface|parameter)[a-z]{8,})",
    re.IGNORECASE,
)


REQUIRED_COLUMNS = [
    "switch",
    "version",
    "subversion",
    "folder_version",
    "raw_folder_exists",
    "raw_md_files",
    "raw_total_size_mb",
    "output_file_exists",
    "final_rows",
    "status",
    "reason",
    "raw_path",
    "output_path",
]

DIAGNOSTIC_COLUMNS = [
    "review_flag",
    "top_raw_files_by_size",
    "sample_headings_found",
    "contains_cli_commands",
    "contains_only_index_or_support_pages",
    "contains_tables_only",
    "contains_release_note_like_text",
    "contains_pdf_ocr_damage",
    "likely_reason",
    "heading_count",
    "command_like_lines",
    "table_like_lines",
    "page_header_footer_like_lines",
    "support_fragment_lines",
    "output_dump_indicator_lines",
    "release_note_like_lines",
    "ocr_damage_indicator_lines",
]

LOW_ROW_AUDIT_COLUMNS = [
    "switch",
    "version",
    "subversion",
    "folder_version",
    "raw_md_files",
    "final_rows",
    "rows_per_md_file",
    "row_count_status",
    "audit_priority",
    "reason",
    "raw_path",
    "output_path",
]


def parse_folder_version(folder_version: str) -> tuple[str, str]:
    match = re.match(r"^(\d+_\d+)_(.+)$", folder_version)
    if match:
        return match.group(1), match.group(2)
    return folder_version, "base"


def row_count(path: Path) -> int:
    if not path.exists():
        return 0
    with path.open("r", encoding="utf-8", errors="replace") as handle:
        return sum(1 for _ in handle)


def safe_read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def discover_raw_folders(raw_root: Path) -> dict[tuple[str, str], Path]:
    folders: dict[tuple[str, str], Path] = {}
    if not raw_root.exists():
        return folders
    for switch_dir in sorted(path for path in raw_root.iterdir() if path.is_dir()):
        for version_dir in sorted(path for path in switch_dir.iterdir() if path.is_dir()):
            folders[(switch_dir.name, version_dir.name)] = version_dir
    return folders


def discover_output_folders(output_root: Path) -> dict[tuple[str, str], Path]:
    folders: dict[tuple[str, str], Path] = {}
    if not output_root.exists():
        return folders
    for switch_dir in sorted(path for path in output_root.iterdir() if path.is_dir()):
        for version_dir in sorted(path for path in switch_dir.iterdir() if path.is_dir()):
            folders[(switch_dir.name, version_dir.name)] = version_dir
    return folders


def classify_status(
    *,
    raw_folder_exists: bool,
    raw_md_files: int,
    output_file_exists: bool,
    final_rows: int,
    raw_pdf_files: int = 0,
) -> tuple[str, str]:
    if not raw_folder_exists:
        return "raw_folder_missing", "No matching raw Markdown folder was found."
    if raw_md_files == 0:
        if raw_pdf_files > 0:
            return "markitdown_failed", "Raw folder has PDFs but no Markdown files."
        return "raw_folder_empty", "Raw folder exists but contains no Markdown files."
    if not output_file_exists:
        return "output_missing", "Raw Markdown exists, but train_chat.jsonl was not generated."
    if final_rows == 0:
        if raw_md_files >= LOW_ROW_RAW_MD_THRESHOLD:
            return "needs_manual_review", "Many raw Markdown files exist, but final output has zero rows."
        if raw_md_files < 5:
            return "all_rows_filtered", "Small raw folder produced zero rows after validation/filtering."
        return "zero_rows", "Raw Markdown exists, but final output has zero rows."
    if raw_md_files >= LOW_ROW_RAW_MD_THRESHOLD and final_rows < LOW_ROW_FINAL_ROW_THRESHOLD:
        return "low_rows", "Raw folder has many Markdown files but fewer than 50 final rows."
    return "ok", "Final output exists and row count is within the audit threshold."


def short_join(items: list[str], limit: int = 20, item_limit: int = 120) -> str:
    cleaned: list[str] = []
    for item in items[:limit]:
        text = re.sub(r"\s+", " ", item).strip()
        if len(text) > item_limit:
            text = text[: item_limit - 3].rstrip() + "..."
        if text:
            cleaned.append(text)
    return " | ".join(cleaned)


def inspect_raw_markdown(raw_path: Path, raw_md_files: list[Path]) -> dict[str, Any]:
    top_files = sorted(raw_md_files, key=lambda path: path.stat().st_size, reverse=True)[:5]
    headings: list[str] = []
    counters: Counter[str] = Counter()

    for md_file in raw_md_files:
        text = safe_read_text(md_file)
        for line in text.splitlines():
            stripped = line.strip()
            if not stripped:
                continue
            if stripped.startswith(("# ", "## ", "### ")):
                counters["headings"] += 1
                if len(headings) < 25:
                    headings.append(re.sub(r"^#{1,6}\s*", "", stripped))
            if COMMAND_LINE_RE.match(stripped) or stripped.lower().startswith("syntax:"):
                counters["command_like_lines"] += 1
            if "|" in stripped:
                counters["table_like_lines"] += 1
            if PAGE_HEADER_FOOTER_RE.search(stripped):
                counters["page_header_footer_like_lines"] += 1
            if SUPPORT_FRAGMENT_RE.search(stripped):
                counters["support_fragment_lines"] += 1
            if OUTPUT_DUMP_RE.search(stripped):
                counters["output_dump_indicator_lines"] += 1
            if RELEASE_NOTE_RE.search(stripped):
                counters["release_note_like_lines"] += 1
            if OCR_DAMAGE_RE.search(stripped):
                counters["ocr_damage_indicator_lines"] += 1
            counters["nonempty_lines"] += 1

    contains_cli = counters["command_like_lines"] >= 5
    contains_support_only = (
        counters["support_fragment_lines"] >= 10
        and counters["command_like_lines"] < 5
        and counters["headings"] < 20
    )
    contains_tables_only = (
        counters["table_like_lines"] >= 50
        and counters["table_like_lines"] > (counters["command_like_lines"] + counters["headings"]) * 3
    )
    contains_release_notes = counters["release_note_like_lines"] >= 5
    contains_ocr_damage = counters["ocr_damage_indicator_lines"] >= 5

    return {
        "top_raw_files_by_size": "; ".join(
            f"{path.name} ({path.stat().st_size / (1024 * 1024):.2f} MB)" for path in top_files
        ),
        "sample_headings_found": short_join(headings),
        "contains_cli_commands": contains_cli,
        "contains_only_index_or_support_pages": contains_support_only,
        "contains_tables_only": contains_tables_only,
        "contains_release_note_like_text": contains_release_notes,
        "contains_pdf_ocr_damage": contains_ocr_damage,
        "heading_count": counters["headings"],
        "command_like_lines": counters["command_like_lines"],
        "table_like_lines": counters["table_like_lines"],
        "page_header_footer_like_lines": counters["page_header_footer_like_lines"],
        "support_fragment_lines": counters["support_fragment_lines"],
        "output_dump_indicator_lines": counters["output_dump_indicator_lines"],
        "release_note_like_lines": counters["release_note_like_lines"],
        "ocr_damage_indicator_lines": counters["ocr_damage_indicator_lines"],
    }


def infer_likely_reason(row: dict[str, Any], diagnostics: dict[str, Any], quality_report: dict[str, Any] | None) -> str:
    status = row["status"]
    if status == "ok":
        return "ok"
    if status == "raw_folder_missing":
        return "raw folder is absent from MarkItDown output"
    if status == "raw_folder_empty":
        return "raw folder exists but contains no Markdown files"
    if status == "markitdown_failed":
        return "PDF conversion likely failed before Markdown generation"
    if status == "output_missing":
        return "preprocessing did not write train_chat.jsonl for this raw folder"

    if diagnostics.get("contains_pdf_ocr_damage"):
        return "raw Markdown shows OCR/spacing damage; strict quality filters likely removed noisy rows"
    if diagnostics.get("contains_only_index_or_support_pages"):
        return "raw Markdown appears mostly index/support/footer material"
    if diagnostics.get("contains_tables_only"):
        return "raw Markdown appears table/output-heavy; table-output filters likely removed rows"
    if diagnostics.get("contains_release_note_like_text"):
        return "raw Markdown has release-note-like content and is not product-doc training material"

    if quality_report:
        generated = int(quality_report.get("total_qa_rows_before_dedup", 0) or 0)
        validation_removed = int(quality_report.get("rows_removed_by_validation", 0) or 0)
        cap_removed = int(quality_report.get("rows_removed_by_cap", 0) or 0)
        final_rows = int(row.get("final_rows", 0) or 0)
        if generated > 0 and final_rows == 0:
            return (
                "rows were generated but removed by validators/caps "
                f"(generated={generated}, validation_removed={validation_removed}, cap_removed={cap_removed})"
            )
        if generated > final_rows and row["status"] == "low_rows":
            return (
                "low yield after validation/caps "
                f"(generated={generated}, final_rows={final_rows}, validation_removed={validation_removed}, cap_removed={cap_removed})"
            )

    if diagnostics.get("contains_cli_commands") and diagnostics.get("heading_count", 0) > 0:
        return "raw content looks useful; needs targeted parser/heading/source-type review"
    return "low or zero final rows require manual review"


def read_quality_report(output_dir: Path) -> dict[str, Any] | None:
    report_path = output_dir / "quality_report.json"
    if not report_path.exists():
        return None
    try:
        return json.loads(safe_read_text(report_path))
    except json.JSONDecodeError:
        return None


def build_audit_rows(raw_root: Path, output_root: Path) -> list[dict[str, Any]]:
    raw_folders = discover_raw_folders(raw_root)
    output_folders = discover_output_folders(output_root)
    keys = sorted(set(raw_folders) | set(output_folders))
    rows: list[dict[str, Any]] = []

    for switch, folder_version in keys:
        version, subversion = parse_folder_version(folder_version)
        raw_path = raw_folders.get((switch, folder_version), raw_root / switch / folder_version)
        output_dir = output_folders.get((switch, folder_version), output_root / switch / folder_version)
        output_path = output_dir / "train_chat.jsonl"

        raw_folder_exists = raw_path.exists()
        raw_md_files = sorted(raw_path.glob("*.md")) if raw_folder_exists else []
        raw_pdf_files = sorted(raw_path.glob("*.pdf")) if raw_folder_exists else []
        raw_total_size_mb = sum(path.stat().st_size for path in raw_md_files) / (1024 * 1024)
        output_file_exists = output_path.exists()
        final_rows = row_count(output_path) if output_file_exists else 0
        status, reason = classify_status(
            raw_folder_exists=raw_folder_exists,
            raw_md_files=len(raw_md_files),
            output_file_exists=output_file_exists,
            final_rows=final_rows,
            raw_pdf_files=len(raw_pdf_files),
        )

        review_flag = (
            status != "ok"
            or (switch, folder_version) in REQUIRED_REVIEW_FOLDERS
            or (len(raw_md_files) >= LOW_ROW_RAW_MD_THRESHOLD and final_rows < LOW_ROW_FINAL_ROW_THRESHOLD)
        )

        row: dict[str, Any] = {
            "switch": switch,
            "version": version,
            "subversion": subversion,
            "folder_version": folder_version,
            "raw_folder_exists": raw_folder_exists,
            "raw_md_files": len(raw_md_files),
            "raw_total_size_mb": round(raw_total_size_mb, 3),
            "output_file_exists": output_file_exists,
            "final_rows": final_rows,
            "status": status,
            "reason": reason,
            "raw_path": str(raw_path),
            "output_path": str(output_path),
            "review_flag": review_flag,
        }

        diagnostics: dict[str, Any] = {
            "top_raw_files_by_size": "",
            "sample_headings_found": "",
            "contains_cli_commands": False,
            "contains_only_index_or_support_pages": False,
            "contains_tables_only": False,
            "contains_release_note_like_text": False,
            "contains_pdf_ocr_damage": False,
            "heading_count": 0,
            "command_like_lines": 0,
            "table_like_lines": 0,
            "page_header_footer_like_lines": 0,
            "support_fragment_lines": 0,
            "output_dump_indicator_lines": 0,
            "release_note_like_lines": 0,
            "ocr_damage_indicator_lines": 0,
        }
        if review_flag and raw_md_files:
            diagnostics = inspect_raw_markdown(raw_path, raw_md_files)
        quality_report = read_quality_report(output_dir)
        row.update(diagnostics)
        row["likely_reason"] = infer_likely_reason(row, diagnostics, quality_report)
        if review_flag and (switch, folder_version) in REQUIRED_REVIEW_FOLDERS:
            row["reason"] = f"explicit review target; {row['reason']}"
        rows.append(row)

    return rows


def write_csv(rows: list[dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = REQUIRED_COLUMNS + DIAGNOSTIC_COLUMNS
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def write_json(data: Any, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def classify_row_count(raw_md_files: int, final_rows: int) -> tuple[str, str, str]:
    """Classify low-row output without automatically flagging every small folder."""
    if final_rows == 0:
        return "zero_rows", "must_check", "zero_rows: final_rows is 0, inspect raw files"
    if final_rows < 50:
        return "very_low_rows", "must_check", "very_low_rows: final_rows < 50"
    if final_rows < 150 and raw_md_files >= 10:
        return "suspicious_low_rows", "check", "suspicious_low_rows: final_rows < 150 but raw_md_files >= 10"
    if final_rows < 400 and raw_md_files >= 20:
        return "moderate_low_rows", "review_summary_only", "moderate_low_rows: final_rows < 400 but raw_md_files >= 20"
    return "ok", "no_action", "ok: row count is acceptable"


def build_low_row_audit_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    audit_rows: list[dict[str, Any]] = []
    for row in rows:
        raw_md_files = int(row.get("raw_md_files", 0) or 0)
        final_rows = int(row.get("final_rows", 0) or 0)
        row_count_status, audit_priority, reason = classify_row_count(raw_md_files, final_rows)
        if (row["switch"], row["folder_version"]) in REQUIRED_REVIEW_FOLDERS:
            audit_priority = "must_check"
            if row_count_status == "ok":
                row_count_status = "explicit_review_target"
                reason = "explicit review target requested by user"
        rows_per_md_file = round(final_rows / raw_md_files, 3) if raw_md_files else 0.0
        audit_rows.append(
            {
                "switch": row["switch"],
                "version": row["version"],
                "subversion": row["subversion"],
                "folder_version": row["folder_version"],
                "raw_md_files": raw_md_files,
                "final_rows": final_rows,
                "rows_per_md_file": rows_per_md_file,
                "row_count_status": row_count_status,
                "audit_priority": audit_priority,
                "reason": reason,
                "raw_path": row["raw_path"],
                "output_path": row["output_path"],
            }
        )
    return audit_rows


def write_low_row_audit_csv(rows: list[dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=LOW_ROW_AUDIT_COLUMNS, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def build_low_row_audit_summary(rows: list[dict[str, Any]]) -> dict[str, Any]:
    status_counts = Counter(str(row["row_count_status"]) for row in rows)
    priority_counts = Counter(str(row["audit_priority"]) for row in rows)
    flagged_rows = [
        row
        for row in rows
        if row["audit_priority"] in {"must_check", "check", "review_summary_only"}
    ]
    return {
        "total_folders": len(rows),
        "row_count_status_counts": dict(sorted(status_counts.items())),
        "audit_priority_counts": dict(sorted(priority_counts.items())),
        "flagged_folders": len(flagged_rows),
        "must_check_folders": [
            row
            for row in rows
            if row["audit_priority"] == "must_check"
        ],
        "check_folders": [
            row
            for row in rows
            if row["audit_priority"] == "check"
        ],
        "review_summary_only_folders": [
            row
            for row in rows
            if row["audit_priority"] == "review_summary_only"
        ],
    }


def load_jsonl_rows(path: Path) -> tuple[list[dict[str, Any]], int]:
    rows: list[dict[str, Any]] = []
    errors = 0
    if not path.exists():
        return rows, errors
    with path.open("r", encoding="utf-8", errors="replace") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                errors += 1
    return rows, errors


def final_jsonl_quality(final_jsonl: Path) -> dict[str, Any]:
    rows, parse_errors = load_jsonl_rows(final_jsonl)
    qa_pairs: Counter[tuple[str, str]] = Counter()
    questions: Counter[str] = Counter()
    data_families: Counter[str] = Counter()
    underscore_version_questions = 0

    for row in rows:
        messages = row.get("messages", [])
        user = ""
        assistant = ""
        if isinstance(messages, list):
            for message in messages:
                if not isinstance(message, dict):
                    continue
                if message.get("role") == "user":
                    user = str(message.get("content", ""))
                elif message.get("role") == "assistant":
                    assistant = str(message.get("content", ""))
        if user or assistant:
            qa_pairs[(user, assistant)] += 1
        if user:
            questions[user] += 1
            if re.search(r"\b10_\d{2}(?:_\d{4})?\b", user):
                underscore_version_questions += 1
        data_families[str(row.get("data_family", ""))] += 1

    exact_duplicate_qa_pairs = sum(count - 1 for count in qa_pairs.values() if count > 1)
    duplicate_questions_final = sum(count - 1 for count in questions.values() if count > 1)
    event_log_rows = data_families.get("event_log_reference", 0)
    event_log_ratio = event_log_rows / len(rows) if rows else 0.0

    return {
        "final_jsonl": str(final_jsonl),
        "total_rows": len(rows),
        "jsonl_parse_errors": parse_errors,
        "exact_duplicate_qa_pairs": exact_duplicate_qa_pairs,
        "duplicate_questions_final": duplicate_questions_final,
        "rows_with_underscore_version_question": underscore_version_questions,
        "event_log_rows": event_log_rows,
        "event_log_ratio": round(event_log_ratio, 6),
        "data_family_counts": dict(sorted(data_families.items())),
    }


def aggregate_group_quality(output_root: Path) -> dict[str, Any]:
    numeric_totals: Counter[str] = Counter()
    report_count = 0
    for report_path in output_root.rglob("quality_report.json"):
        try:
            report = json.loads(safe_read_text(report_path))
        except json.JSONDecodeError:
            continue
        report_count += 1
        for key, value in report.items():
            if isinstance(value, bool):
                continue
            if isinstance(value, int):
                numeric_totals[key] += value
            elif isinstance(value, float):
                numeric_totals[key] += value
    return {
        "quality_report_files": report_count,
        "numeric_totals": dict(sorted(numeric_totals.items())),
    }


def build_summary(rows: list[dict[str, Any]], final_jsonl: Path, output_root: Path) -> dict[str, Any]:
    status_counts = Counter(str(row["status"]) for row in rows)
    zero_or_low = [
        {
            "switch": row["switch"],
            "version": row["version"],
            "subversion": row["subversion"],
            "folder_version": row["folder_version"],
            "final_rows": row["final_rows"],
            "status": row["status"],
            "likely_reason": row["likely_reason"],
        }
        for row in rows
        if int(row["final_rows"]) == 0 or row["status"] == "low_rows"
    ]
    total_rows = sum(int(row["final_rows"]) for row in rows)
    raw_rows = [row for row in rows if row["raw_folder_exists"]]
    raw_with_md = [row for row in rows if row["raw_folder_exists"] and int(row["raw_md_files"]) > 0]
    output_missing = [
        row
        for row in raw_with_md
        if not row["output_file_exists"]
    ]
    zero_rows = [
        row
        for row in raw_with_md
        if row["output_file_exists"] and int(row["final_rows"]) == 0
    ]
    low_rows = [row for row in rows if row["status"] == "low_rows"]

    return {
        "total_product_doc_rows": total_rows,
        "total_switches": len({row["switch"] for row in raw_rows}),
        "total_switch_version_folders": len(rows),
        "raw_folders_accounted_for": len(raw_rows),
        "raw_folders_with_markdown": len(raw_with_md),
        "zero_row_folders_before": len(zero_rows),
        "zero_row_folders_after": len(zero_rows),
        "low_row_folders_before": len(low_rows),
        "low_row_folders_after": len(low_rows),
        "output_missing_before": len(output_missing),
        "output_missing_after": len(output_missing),
        "folders_rerun": 0,
        "rows_recovered": 0,
        "status_counts": dict(sorted(status_counts.items())),
        "still_zero_or_low_folders": zero_or_low,
        "final_jsonl_quality": final_jsonl_quality(final_jsonl),
        "group_quality_totals": aggregate_group_quality(output_root),
    }


def write_summary_csv(rows: list[dict[str, Any]], path: Path) -> None:
    fieldnames = [
        "switch",
        "version",
        "subversion",
        "folder_version",
        "raw_md_files",
        "final_rows",
        "status",
        "reason",
        "likely_reason",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Audit full product-doc output for missing/low folders.")
    parser.add_argument("--raw-root", type=Path, default=DEFAULT_RAW_ROOT)
    parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT_ROOT)
    parser.add_argument("--final-jsonl", type=Path, default=DEFAULT_FINAL_JSONL)
    parser.add_argument("--report-dir", type=Path, default=DEFAULT_REPORT_DIR)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    rows = build_audit_rows(args.raw_root, args.output_root)
    low_row_audit_rows = build_low_row_audit_rows(rows)
    low_row_audit_summary = build_low_row_audit_summary(low_row_audit_rows)
    summary = build_summary(rows, args.final_jsonl, args.output_root)
    summary["low_row_audit"] = low_row_audit_summary

    audit_csv = args.report_dir / "full_product_docs_missing_audit.csv"
    audit_json = args.report_dir / "full_product_docs_missing_audit.json"
    low_row_audit_csv = args.report_dir / "full_product_docs_low_row_audit.csv"
    low_row_audit_json = args.report_dir / "full_product_docs_low_row_audit.json"
    summary_csv = args.report_dir / "full_product_docs_summary.csv"
    quality_json = args.report_dir / "full_product_docs_quality_report.json"

    write_csv(rows, audit_csv)
    write_json({"summary": summary, "rows": rows}, audit_json)
    write_low_row_audit_csv(low_row_audit_rows, low_row_audit_csv)
    write_json({"summary": low_row_audit_summary, "rows": low_row_audit_rows}, low_row_audit_json)
    write_summary_csv(rows, summary_csv)
    write_json(summary, quality_json)

    print(f"Audit rows: {len(rows)}")
    print(f"Total rows: {summary['total_product_doc_rows']}")
    print(f"Zero-row folders: {summary['zero_row_folders_after']}")
    print(f"Low-row folders: {summary['low_row_folders_after']}")
    print(f"Output-missing folders: {summary['output_missing_after']}")
    print(f"Low-row must-check folders: {low_row_audit_summary['audit_priority_counts'].get('must_check', 0)}")
    print(f"Low-row check folders: {low_row_audit_summary['audit_priority_counts'].get('check', 0)}")
    print(
        "Low-row review-summary-only folders: "
        f"{low_row_audit_summary['audit_priority_counts'].get('review_summary_only', 0)}"
    )
    print(f"Audit CSV: {audit_csv}")
    print(f"Audit JSON: {audit_json}")
    print(f"Low-row audit CSV: {low_row_audit_csv}")
    print(f"Low-row audit JSON: {low_row_audit_json}")
    print(f"Summary CSV: {summary_csv}")
    print(f"Quality JSON: {quality_json}")


if __name__ == "__main__":
    main()
