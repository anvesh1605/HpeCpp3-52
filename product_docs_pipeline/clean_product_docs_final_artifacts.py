"""Final deterministic cleanup for product-doc bullet and OCR artifacts.

This post-processes product documentation JSONL only. It does not touch
release-note preprocessing, does not generate new data, and does not use LLMs.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import shutil
from collections import Counter, defaultdict
from copy import deepcopy
from pathlib import Path
from typing import Any

from preprocess_product_docs import (
    _duplicate_questions_final,
    _final_issue_counts,
    _question_dedupe_key,
    _rows_with_underscore_version,
)
from run_low300_product_docs_stage import balance_reports, sample_review, write_csv as write_csv_rows
from project.src.product_doc_validator import (
    exact_qa_dedupe_key,
    is_event_log_source_misclassified_row,
    normalize,
    rows_with_grounding,
    validate_qa_row,
)


BASE_DIR = Path(__file__).resolve().parent
PRODUCT_DOC_DIR = BASE_DIR / "final_json" / "product_docs"
DEFAULT_INPUT_ROOT = PRODUCT_DOC_DIR / "full_product_docs"
DEFAULT_COMBINED_JSONL = PRODUCT_DOC_DIR / "train_chat_product_docs.jsonl"
DEFAULT_OUTPUT_JSONL = PRODUCT_DOC_DIR / "product_docs_final_clean.jsonl"
DEFAULT_REPORT_JSON = PRODUCT_DOC_DIR / "product_docs_final_cleanup_report.json"
DEFAULT_SUMMARY_CSV = PRODUCT_DOC_DIR / "full_product_docs_summary.csv"
DEFAULT_QUALITY_JSON = PRODUCT_DOC_DIR / "full_product_docs_quality_report.json"
DEFAULT_BALANCE_JSON = PRODUCT_DOC_DIR / "full_product_docs_balance_report.json"
DEFAULT_BALANCE_CSV = PRODUCT_DOC_DIR / "full_product_docs_balance_report.csv"
DEFAULT_SAMPLE_JSONL = PRODUCT_DOC_DIR / "final_product_docs_sample_review.jsonl"
DEFAULT_SAMPLE_CSV = PRODUCT_DOC_DIR / "final_product_docs_sample_review.csv"

TOPIC_FIELDS = ("section", "topic", "task")
TEXT_FIX_FIELDS = ("section", "topic", "task")
COMMAND_SYNTAX_FIELDS = ("command", "syntax")
COMMAND_REFERENCE_FAMILIES = {"cli_command_reference", "show_command_reference"}
TOPIC_FRAGMENT_FAMILIES = {
    "concept_explanation",
    "configuration_procedure",
    "security_policy",
    "routing_feature",
    "qos_policy",
    "web_ui_task",
    "feature_limitation",
    "troubleshooting",
    "monitoring_feature",
    "rest_api_reference",
    "snmp_mib_reference",
}

N_BULLET_PREFIX_RE = re.compile(r"^n\s+", re.IGNORECASE)
BULLET_PREFIX_RE = re.compile(
    r"^(?:n\s+|â€¢\s*|â—¦\s*|\u2022\s*|\u25e6\s*|-\s+|\*\s*)",
    re.IGNORECASE,
)
REST_OR_URL_RE = re.compile(r"(?:https?://|www\.|\*/rest/|^/?rest/|/rest/v\d|^\*/)", re.IGNORECASE)
REST_PATH_ONLY_RE = re.compile(r"^\*?/?rest/[A-Za-z0-9_./{}<>:-]+?\*?$", re.IGNORECASE)
INCOMPLETE_CONNECTOR_RE = re.compile(r"\b(?:except|and|or|for|with|from|to|using|of)$", re.IGNORECASE)
TABLE_FRAGMENT_EXACT = {
    "allowed vlan list",
    "frame ingress vlan id",
    "port vlan id",
    "remote management address",
}
GENERIC_FRAGMENT_EXACT = {
    "interface",
    "management address",
    "configuration management",
}
MANUAL_FORBIDDEN_TERMS = [
    '"section": "n ',
    '"topic": "n ',
    "n Configuration management",
    "n Frame ingress VLAN ID",
    "n Configuration information",
    "n Switch Configuration using templates",
    "n Management modules and the intake temperature sensor",
    "displaysthe",
    "informationabout",
    "linkstateforeachmember",
    "URL s",
    "X. 509",
]
MANUAL_N_ARTIFACT_RE = re.compile(
    r"\bn\s+(?:Configuration management|Frame ingress VLAN ID|Configuration information|"
    r"Switch Configuration using templates|Management modules and the intake temperature sensor)\b",
    re.IGNORECASE,
)
SEVERE_OCR_RE = re.compile(
    r"(?:displaysthe|informationabout|linkstateforeachmember|showthe|enterthecommand|"
    r"Specifiesthe|Selectsthe|Commandcontext)",
    re.IGNORECASE,
)
OCR_TERM_FIXES: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"displaysinformationaboutthe", re.IGNORECASE), "displays information about the"),
    (re.compile(r"displaysinformationabout", re.IGNORECASE), "displays information about"),
    (re.compile(r"displaysthecurrent", re.IGNORECASE), "displays the current"),
    (re.compile(r"displaysthe", re.IGNORECASE), "displays the"),
    (re.compile(r"showsinformationaboutthe", re.IGNORECASE), "shows information about the"),
    (re.compile(r"showsinformationabout", re.IGNORECASE), "shows information about"),
    (re.compile(r"showsversioninformationabout", re.IGNORECASE), "shows version information about"),
    (re.compile(r"showsthe", re.IGNORECASE), "shows the"),
    (re.compile(r"informationaboutthe", re.IGNORECASE), "information about the"),
    (re.compile(r"informationabout", re.IGNORECASE), "information about"),
    (re.compile(r"linkstateforeachmember", re.IGNORECASE), "link state for each member"),
    (re.compile(r"\bURL syntax\b", re.IGNORECASE), "URL format"),
    (re.compile(r"\bURL\s+s\b", re.IGNORECASE), "URLs"),
    (re.compile(r"\bX\.\s+509\b", re.IGNORECASE), "X.509"),
    (re.compile(r"\bWeb-UI\b", re.IGNORECASE), "Web UI"),
    (re.compile(r"\bCLI\s+s\b", re.IGNORECASE), "CLIs"),
    (re.compile(r"showthe", re.IGNORECASE), "show the"),
    (re.compile(r"enterthecommand", re.IGNORECASE), "enter the command"),
    (re.compile(r"Specifiesthe", re.IGNORECASE), "Specifies the"),
    (re.compile(r"Selectsthe", re.IGNORECASE), "Selects the"),
    (re.compile(r"Commandcontext", re.IGNORECASE), "Command context"),
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
    "n_bullet_prefix_rows_final",
    "final_bullet_fragment_rows_final",
    "final_ocr_rows_final",
    "event_log_source_misclassified_rows_final",
]


def normalize_text(text: Any) -> str:
    return re.sub(r"\s+", " ", str(text or "").replace("\xa0", " ")).strip()


def word_count(text: str) -> int:
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9_.:/<>-]*", text or ""))


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


def row_text_blob(row: dict[str, Any]) -> str:
    question, answer = row_messages(row)
    field_text = " ".join(str(row.get(field, "") or "") for field in TOPIC_FIELDS)
    return " ".join([field_text, question, answer])


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


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(strip_cleanup_metadata(row), ensure_ascii=False, sort_keys=False))
            handle.write("\n")


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def read_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8-sig", errors="replace"))
    except json.JSONDecodeError:
        return {}


def backup_path_for(path: Path, backup_suffix: str) -> Path:
    return path.with_name(f"{path.stem}{backup_suffix}{path.suffix}")


def grouped_by_source_path(rows: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[str(row.get("_cleanup_source_path", ""))].append(row)
    return grouped


def rows_equal(left: list[dict[str, Any]], right: list[dict[str, Any]]) -> bool:
    if len(left) != len(right):
        return False
    for left_row, right_row in zip(left, right):
        if strip_cleanup_metadata(left_row) != strip_cleanup_metadata(right_row):
            return False
    return True


def is_topic_sensitive_row(row: dict[str, Any]) -> bool:
    return str(row.get("data_family", "")) in TOPIC_FRAGMENT_FAMILIES


def strip_bullet_prefix(text: str) -> str:
    return BULLET_PREFIX_RE.sub("", normalize_text(text), count=1).strip()


def is_noisy_or_table_fragment(text: str, *, row: dict[str, Any] | None = None) -> bool:
    cleaned = normalize_text(text).strip(" .:-")
    lowered = cleaned.lower()
    if not cleaned:
        return True
    if REST_OR_URL_RE.search(cleaned) or REST_PATH_ONLY_RE.fullmatch(cleaned):
        return True
    if lowered in TABLE_FRAGMENT_EXACT or lowered in GENERIC_FRAGMENT_EXACT:
        return True
    if lowered.startswith("configuration management:") and REST_OR_URL_RE.search(cleaned):
        return True
    if re.search(r"\b(?:Frame ingress VLAN ID|Port VLAN ID|Allowed VLAN List|Remote Management Address)\b", cleaned, re.IGNORECASE):
        return True
    if INCOMPLETE_CONNECTOR_RE.search(cleaned):
        return True
    if row is not None and is_topic_sensitive_row(row):
        if word_count(cleaned) <= 2 and lowered in {"status", "statistics", "counters", "configuration"}:
            return True
    return False


def can_repair_topic(text: str) -> bool:
    cleaned = normalize_text(text).strip(" .:-")
    if not cleaned:
        return False
    if word_count(cleaned) < 2:
        return False
    if REST_OR_URL_RE.search(cleaned):
        return False
    if INCOMPLETE_CONNECTOR_RE.search(cleaned):
        return False
    return True


def replace_message_references(row: dict[str, Any], replacements: list[tuple[str, str]]) -> None:
    if not replacements:
        return
    messages = row.get("messages", [])
    if not isinstance(messages, list):
        return
    unique_replacements = []
    seen: set[tuple[str, str]] = set()
    for old, new in replacements:
        if not old or old == new or (old, new) in seen:
            continue
        unique_replacements.append((old, new))
        seen.add((old, new))
    for message in messages:
        if not isinstance(message, dict) or "content" not in message:
            continue
        content = str(message.get("content", "") or "")
        for old, new in unique_replacements:
            content = content.replace(old, new)
            content = re.sub(re.escape(normalize_text(old)), new, content)
        message["content"] = content


def clean_command_and_syntax_whitespace(row: dict[str, Any]) -> None:
    for field in COMMAND_SYNTAX_FIELDS:
        if field not in row or not isinstance(row.get(field), str):
            continue
        lines = [re.sub(r"[ \t]+", " ", line).strip() for line in str(row[field]).strip().splitlines()]
        row[field] = "\n".join(line for line in lines if line)


def replacement_with_case(match: re.Match[str], replacement: str) -> str:
    original = match.group(0)
    if original.isupper():
        return replacement.upper()
    if original[:1].isupper():
        return replacement[:1].upper() + replacement[1:]
    return replacement


def apply_ocr_fixes(text: str) -> tuple[str, int]:
    fixed = str(text or "")
    replacements = 0
    for pattern, replacement in OCR_TERM_FIXES:
        fixed, count = pattern.subn(lambda match: replacement_with_case(match, replacement), fixed)
        replacements += count
    return fixed, replacements


def apply_ocr_fixes_to_row(row: dict[str, Any]) -> int:
    fixed_terms = 0
    for field in TEXT_FIX_FIELDS:
        if field in row and isinstance(row.get(field), str):
            fixed, count = apply_ocr_fixes(str(row[field]))
            row[field] = fixed
            fixed_terms += count
    messages = row.get("messages", [])
    if isinstance(messages, list):
        for message in messages:
            if not isinstance(message, dict) or "content" not in message:
                continue
            fixed, count = apply_ocr_fixes(str(message.get("content", "") or ""))
            message["content"] = fixed
            fixed_terms += count
    return fixed_terms


def has_severe_ocr_row(row: dict[str, Any]) -> bool:
    return bool(SEVERE_OCR_RE.search(row_text_blob(row)))


def has_n_bullet_prefix_row(row: dict[str, Any]) -> bool:
    return any(N_BULLET_PREFIX_RE.match(normalize_text(row.get(field, ""))) for field in TOPIC_FIELDS)


def has_final_bullet_fragment_row(row: dict[str, Any]) -> bool:
    for field in TOPIC_FIELDS:
        value = normalize_text(row.get(field, ""))
        if not value:
            continue
        if BULLET_PREFIX_RE.match(value):
            return True
        if is_topic_sensitive_row(row) and is_noisy_or_table_fragment(value, row=row):
            return True
    return False


def manual_forbidden_counts(rows: list[dict[str, Any]]) -> dict[str, int]:
    serialized = "\n".join(json.dumps(strip_cleanup_metadata(row), ensure_ascii=False) for row in rows)
    return {term: serialized.count(term) for term in MANUAL_FORBIDDEN_TERMS}


def clean_one_row(row: dict[str, Any]) -> tuple[dict[str, Any] | None, Counter[str], str]:
    cleaned = deepcopy(row)
    counters: Counter[str] = Counter()
    replacements: list[tuple[str, str]] = []
    n_found = False
    n_repaired = False
    bullet_repaired = False

    if is_event_log_source_misclassified_row(cleaned):
        counters["event_log_source_misclassified_rows_found"] = 1
        counters["event_log_source_misclassified_rows_dropped"] = 1
        return None, counters, "event_log_source_misclassified"

    clean_command_and_syntax_whitespace(cleaned)

    for field in TOPIC_FIELDS:
        if field not in cleaned or not isinstance(cleaned.get(field), str):
            continue
        original = str(cleaned[field])
        normalized = normalize_text(original)
        cleaned[field] = normalized
        if not normalized:
            continue
        if N_BULLET_PREFIX_RE.match(normalized):
            n_found = True
            remainder = N_BULLET_PREFIX_RE.sub("", normalized, count=1).strip()
            if is_noisy_or_table_fragment(remainder, row=cleaned) or not can_repair_topic(remainder):
                counters["n_bullet_prefix_rows_found"] = 1
                counters["n_bullet_prefix_rows_dropped"] = 1
                counters["final_bullet_fragment_rows_dropped"] = 1
                return None, counters, "n_bullet_prefix_fragment"
            cleaned[field] = remainder
            replacements.append((original, remainder))
            replacements.append((normalized, remainder))
            n_repaired = True

    if n_found:
        counters["n_bullet_prefix_rows_found"] = 1
    if n_repaired:
        counters["n_bullet_prefix_rows_repaired"] = 1

    for field in TOPIC_FIELDS:
        if field not in cleaned or not isinstance(cleaned.get(field), str):
            continue
        normalized = normalize_text(cleaned[field])
        if not normalized or N_BULLET_PREFIX_RE.match(normalized):
            continue
        if BULLET_PREFIX_RE.match(normalized):
            remainder = strip_bullet_prefix(normalized)
            if can_repair_topic(remainder) and not is_noisy_or_table_fragment(remainder, row=cleaned):
                cleaned[field] = remainder
                replacements.append((normalized, remainder))
                bullet_repaired = True
            else:
                counters["final_bullet_fragment_rows_dropped"] = 1
                return None, counters, "bullet_fragment"

    if bullet_repaired:
        counters["final_bullet_fragment_rows_repaired"] = 1

    replace_message_references(cleaned, replacements)

    for field in TOPIC_FIELDS:
        value = normalize_text(cleaned.get(field, ""))
        if value and is_topic_sensitive_row(cleaned) and is_noisy_or_table_fragment(value, row=cleaned):
            counters["final_bullet_fragment_rows_dropped"] = 1
            return None, counters, "table_or_url_fragment"

    ocr_fixed = apply_ocr_fixes_to_row(cleaned)
    if ocr_fixed:
        counters["final_ocr_terms_fixed"] += ocr_fixed

    if has_severe_ocr_row(cleaned):
        counters["final_ocr_rows_dropped"] = 1
        return None, counters, "severe_ocr_artifact"

    if MANUAL_N_ARTIFACT_RE.search(row_text_blob(cleaned)):
        counters["final_bullet_fragment_rows_dropped"] = 1
        return None, counters, "manual_n_artifact"

    if has_final_bullet_fragment_row(cleaned):
        counters["final_bullet_fragment_rows_dropped"] = 1
        return None, counters, "final_bullet_fragment"

    return cleaned, counters, ""


def dedupe_and_validate_rows(
    rows: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], Counter[str], dict[str, Counter[str]], dict[str, list[dict[str, Any]]]]:
    kept: list[dict[str, Any]] = []
    drop_counts: Counter[str] = Counter()
    drop_counts_by_path: dict[str, Counter[str]] = defaultdict(Counter)
    examples: dict[str, list[dict[str, Any]]] = defaultdict(list)
    seen_qa: set[str] = set()
    seen_questions: set[str] = set()

    for row in rows:
        qa_key = exact_qa_dedupe_key(row)
        question_key = _question_dedupe_key(row)
        reason = ""
        if qa_key in seen_qa:
            reason = "exact_duplicate_after_cleanup"
        elif question_key and question_key in seen_questions:
            reason = "duplicate_question_after_cleanup"
        else:
            valid, validation_reason = validate_qa_row(row, require_grounding=True)
            if not valid:
                reason = f"validator_{validation_reason}"
        if reason:
            drop_counts[reason] += 1
            source_path = str(row.get("_cleanup_source_path", ""))
            drop_counts_by_path[source_path][reason] += 1
            if len(examples[reason]) < 20:
                question, answer = row_messages(row)
                examples[reason].append(
                    {
                        "source_path": source_path,
                        "source_line": row.get("_cleanup_source_line", ""),
                        "switch": row.get("switch", ""),
                        "version": row.get("version", ""),
                        "data_family": row.get("data_family", ""),
                        "section": row.get("section", ""),
                        "topic": row.get("topic", ""),
                        "task": row.get("task", ""),
                        "question": question,
                        "answer_preview": answer[:250],
                    }
                )
            continue
        seen_qa.add(qa_key)
        if question_key:
            seen_questions.add(question_key)
        kept.append(row)
    return kept, drop_counts, drop_counts_by_path, dict(examples)


def clean_rows(
    rows: list[dict[str, Any]],
) -> tuple[
    list[dict[str, Any]],
    Counter[str],
    dict[str, Counter[str]],
    dict[str, list[dict[str, Any]]],
]:
    first_pass: list[dict[str, Any]] = []
    counters: Counter[str] = Counter()
    drop_counts: Counter[str] = Counter()
    drop_counts_by_path: dict[str, Counter[str]] = defaultdict(Counter)
    examples: dict[str, list[dict[str, Any]]] = defaultdict(list)

    for row in rows:
        cleaned, row_counters, reason = clean_one_row(row)
        counters.update(row_counters)
        if reason:
            drop_counts[reason] += 1
            source_path = str(row.get("_cleanup_source_path", ""))
            drop_counts_by_path[source_path][reason] += 1
            if len(examples[reason]) < 20:
                question, answer = row_messages(row)
                examples[reason].append(
                    {
                        "source_path": source_path,
                        "source_line": row.get("_cleanup_source_line", ""),
                        "switch": row.get("switch", ""),
                        "version": row.get("version", ""),
                        "data_family": row.get("data_family", ""),
                        "section": row.get("section", ""),
                        "topic": row.get("topic", ""),
                        "task": row.get("task", ""),
                        "question": question,
                        "answer_preview": answer[:250],
                    }
                )
            continue
        if cleaned is not None:
            first_pass.append(cleaned)

    kept, dedupe_drops, dedupe_drops_by_path, dedupe_examples = dedupe_and_validate_rows(first_pass)
    drop_counts.update(dedupe_drops)
    for path, path_counts in dedupe_drops_by_path.items():
        drop_counts_by_path[path].update(path_counts)
    for reason, reason_examples in dedupe_examples.items():
        examples[reason].extend(reason_examples[: max(0, 20 - len(examples[reason]))])

    return kept, counters, drop_counts_by_path, dict(examples) | {"drop_reason_counts": [dict(drop_counts)]}


def duplicate_qa_pairs(rows: list[dict[str, Any]]) -> int:
    counts = Counter(exact_qa_dedupe_key(row) for row in rows)
    return sum(count - 1 for count in counts.values() if count > 1)


def event_log_ratio(rows: list[dict[str, Any]]) -> float:
    if not rows:
        return 0.0
    event_rows = sum(1 for row in rows if row.get("data_family") == "event_log_reference")
    return round(event_rows / len(rows), 6)


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


def final_artifact_counts(rows: list[dict[str, Any]]) -> dict[str, int]:
    return {
        "n_bullet_prefix_rows_final": sum(1 for row in rows if has_n_bullet_prefix_row(row)),
        "final_bullet_fragment_rows_final": sum(1 for row in rows if has_final_bullet_fragment_row(row)),
        "final_ocr_rows_final": sum(1 for row in rows if has_severe_ocr_row(row)),
        "event_log_source_misclassified_rows_final": sum(
            1 for row in rows if is_event_log_source_misclassified_row(row)
        ),
    }


def validation_drop_counts(rows: list[dict[str, Any]]) -> Counter[str]:
    drops: Counter[str] = Counter()
    for row in rows:
        valid, reason = validate_qa_row(row, require_grounding=True)
        if not valid:
            drops[reason] += 1
    return drops


def build_report(
    *,
    input_root: Path,
    output_jsonl: Path,
    total_rows_before: int,
    rows: list[dict[str, Any]],
    input_parse_errors: int,
    counters: Counter[str],
    drop_counts_by_path: dict[str, Counter[str]],
    examples: dict[str, list[dict[str, Any]]],
) -> dict[str, Any]:
    final_issues = _final_issue_counts(rows)
    data_family_counts = Counter(str(row.get("data_family", "")) for row in rows)
    validator_drops = validation_drop_counts(rows)
    drop_reason_counts = Counter()
    for path_counts in drop_counts_by_path.values():
        drop_reason_counts.update(path_counts)

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
        "n_bullet_prefix_rows_found": int(counters.get("n_bullet_prefix_rows_found", 0)),
        "n_bullet_prefix_rows_repaired": int(counters.get("n_bullet_prefix_rows_repaired", 0)),
        "n_bullet_prefix_rows_dropped": int(counters.get("n_bullet_prefix_rows_dropped", 0)),
        "final_bullet_fragment_rows_dropped": int(counters.get("final_bullet_fragment_rows_dropped", 0)),
        "final_bullet_fragment_rows_repaired": int(counters.get("final_bullet_fragment_rows_repaired", 0)),
        "final_ocr_terms_fixed": int(counters.get("final_ocr_terms_fixed", 0)),
        "final_ocr_rows_dropped": int(counters.get("final_ocr_rows_dropped", 0)),
        "event_log_source_misclassified_rows_found": int(
            counters.get("event_log_source_misclassified_rows_found", 0)
        ),
        "event_log_source_misclassified_rows_dropped": int(
            counters.get("event_log_source_misclassified_rows_dropped", 0)
        ),
        "event_log_ratio_after_cap": event_log_ratio(rows),
        "parameter_rows_generated": data_family_counts.get("command_parameter_reference", 0),
        "command_example_rows_generated": data_family_counts.get("command_example", 0),
        "data_family_counts": dict(sorted(data_family_counts.items())),
        "drop_reason_counts": dict(sorted(drop_reason_counts.items())),
        "validation_drops_if_revalidated": sum(validator_drops.values()),
        "validation_drop_reasons_if_revalidated": dict(sorted(validator_drops.items())),
        "final_issue_counts": dict(sorted(final_issues.items())),
        "manual_search_counts_final": manual_forbidden_counts(rows),
        "examples": {key: value for key, value in examples.items() if isinstance(value, list)},
    }
    report.update(final_artifact_counts(rows))
    for key in STRICT_ZERO_KEYS:
        if key in {
            "n_bullet_prefix_rows_final",
            "final_bullet_fragment_rows_final",
            "final_ocr_rows_final",
            "event_log_source_misclassified_rows_final",
        }:
            continue
        report.setdefault(key, int(final_issues.get(key, 0)))
    report["required_zero_checks"] = {key: int(report.get(key, 0) or 0) for key in STRICT_ZERO_KEYS}
    report["required_zero_checks_passed"] = all(value == 0 for value in report["required_zero_checks"].values())
    report["event_log_ratio_check_passed"] = report["event_log_ratio_after_cap"] <= 0.15
    report["manual_search_checks_passed"] = all(value == 0 for value in report["manual_search_counts_final"].values())
    report["ready_to_merge_with_release_notes"] = (
        report["jsonl_parse_errors"] == 0
        and report["input_jsonl_parse_errors"] == 0
        and report["required_zero_checks_passed"]
        and report["event_log_ratio_check_passed"]
        and report["manual_search_checks_passed"]
        and report["validation_drops_if_revalidated"] == 0
    )
    return report


def update_group_quality_report(
    *,
    train_path: Path,
    before_count: int,
    after_rows: list[dict[str, Any]],
    path_drop_counts: Counter[str],
    path_repair_counts: Counter[str],
) -> None:
    quality_path = train_path.parent / "quality_report.json"
    report = read_json(quality_path)
    after_count = len(after_rows)
    family_counts = Counter(str(row.get("data_family", "")) for row in after_rows)
    event_rows = family_counts.get("event_log_reference", 0)
    final_issues = _final_issue_counts(after_rows)
    artifact_final = final_artifact_counts(after_rows)

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
            "post_final_artifact_cleanup": {
                "applied": True,
                "rows_before": before_count,
                "rows_after": after_count,
                "rows_dropped": before_count - after_count,
                "drop_reason_counts": dict(sorted(path_drop_counts.items())),
                "repair_counts": dict(sorted(path_repair_counts.items())),
                **artifact_final,
            },
        }
    )
    report.update(dict(final_issues))
    report.update(artifact_final)
    write_json(quality_path, report)


def apply_cleaned_rows_to_full_tree(
    *,
    original_rows: list[dict[str, Any]],
    cleaned_rows: list[dict[str, Any]],
    drop_counts_by_path: dict[str, Counter[str]],
    repair_counts_by_path: dict[str, Counter[str]],
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
        if rows_equal(before_rows, after_rows):
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
            path_drop_counts=drop_counts_by_path.get(source_path, Counter()),
            path_repair_counts=repair_counts_by_path.get(source_path, Counter()),
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


def repair_counts_by_path(original_rows: list[dict[str, Any]], cleaned_rows: list[dict[str, Any]]) -> dict[str, Counter[str]]:
    original_by_id = {(row.get("_cleanup_source_path"), row.get("_cleanup_source_line")): row for row in original_rows}
    path_counts: dict[str, Counter[str]] = defaultdict(Counter)
    for row in cleaned_rows:
        key = (row.get("_cleanup_source_path"), row.get("_cleanup_source_line"))
        before = original_by_id.get(key)
        if before is None:
            continue
        source_path = str(row.get("_cleanup_source_path", ""))
        for field in TOPIC_FIELDS:
            before_value = normalize_text(before.get(field, ""))
            after_value = normalize_text(row.get(field, ""))
            if before_value != after_value:
                if N_BULLET_PREFIX_RE.match(before_value):
                    path_counts[source_path]["n_bullet_prefix_rows_repaired"] += 1
                elif BULLET_PREFIX_RE.match(before_value):
                    path_counts[source_path]["final_bullet_fragment_rows_repaired"] += 1
        before_blob = row_text_blob(before)
        after_blob = row_text_blob(row)
        if before_blob != after_blob:
            before_hits = sum(len(pattern.findall(before_blob)) for pattern, _ in OCR_TERM_FIXES)
            after_hits = sum(len(pattern.findall(after_blob)) for pattern, _ in OCR_TERM_FIXES)
            if before_hits > after_hits:
                path_counts[source_path]["final_ocr_terms_fixed"] += before_hits - after_hits
    return path_counts


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
            "final_artifact_cleanup": {
                "total_rows_before": report["total_rows_before"],
                "total_rows_after": report["total_rows_after"],
                "rows_dropped_total": report["rows_dropped_total"],
                "n_bullet_prefix_rows_found": report["n_bullet_prefix_rows_found"],
                "n_bullet_prefix_rows_repaired": report["n_bullet_prefix_rows_repaired"],
                "n_bullet_prefix_rows_dropped": report["n_bullet_prefix_rows_dropped"],
                "n_bullet_prefix_rows_final": report["n_bullet_prefix_rows_final"],
                "final_bullet_fragment_rows_dropped": report["final_bullet_fragment_rows_dropped"],
                "final_bullet_fragment_rows_repaired": report["final_bullet_fragment_rows_repaired"],
                "final_bullet_fragment_rows_final": report["final_bullet_fragment_rows_final"],
                "final_ocr_terms_fixed": report["final_ocr_terms_fixed"],
                "final_ocr_rows_dropped": report["final_ocr_rows_dropped"],
                "final_ocr_rows_final": report["final_ocr_rows_final"],
                "event_log_source_misclassified_rows_found": report[
                    "event_log_source_misclassified_rows_found"
                ],
                "event_log_source_misclassified_rows_dropped": report[
                    "event_log_source_misclassified_rows_dropped"
                ],
                "event_log_source_misclassified_rows_final": report[
                    "event_log_source_misclassified_rows_final"
                ],
            },
        }
    )
    write_json(quality_json, existing)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Clean final product-doc bullet/OCR artifacts.")
    parser.add_argument("--input-root", type=Path, default=DEFAULT_INPUT_ROOT)
    parser.add_argument("--combined-jsonl", type=Path, default=DEFAULT_COMBINED_JSONL)
    parser.add_argument("--output-jsonl", type=Path, default=DEFAULT_OUTPUT_JSONL)
    parser.add_argument("--report-json", type=Path, default=DEFAULT_REPORT_JSON)
    parser.add_argument("--summary-csv", type=Path, default=DEFAULT_SUMMARY_CSV)
    parser.add_argument("--quality-json", type=Path, default=DEFAULT_QUALITY_JSON)
    parser.add_argument("--apply-to-full-tree", action="store_true")
    parser.add_argument("--backup-suffix", default=".before_final_artifact_cleanup")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    original_rows, input_parse_errors = load_product_doc_rows(args.input_root)
    cleaned_rows, counters, drop_counts_by_path, examples = clean_rows(original_rows)
    write_jsonl(args.output_jsonl, cleaned_rows)

    path_repair_counts = repair_counts_by_path(original_rows, cleaned_rows)
    report = build_report(
        input_root=args.input_root,
        output_jsonl=args.output_jsonl,
        total_rows_before=len(original_rows),
        rows=cleaned_rows,
        input_parse_errors=input_parse_errors,
        counters=counters,
        drop_counts_by_path=drop_counts_by_path,
        examples=examples,
    )
    if args.apply_to_full_tree:
        report["full_product_docs_tree_apply"] = apply_cleaned_rows_to_full_tree(
            original_rows=original_rows,
            cleaned_rows=cleaned_rows,
            drop_counts_by_path=drop_counts_by_path,
            repair_counts_by_path=path_repair_counts,
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
    print(f"n bullet final: {report['n_bullet_prefix_rows_final']}")
    print(f"bullet fragment final: {report['final_bullet_fragment_rows_final']}")
    print(f"OCR artifact final: {report['final_ocr_rows_final']}")
    print(
        "Event-log source misclassified final: "
        f"{report['event_log_source_misclassified_rows_final']}"
    )
    print(f"Applied to full_product_docs tree: {report['full_product_docs_tree_apply']['applied']}")
    print(f"Ready to merge with release notes: {report['ready_to_merge_with_release_notes']}")
    print(f"Output JSONL: {args.output_jsonl}")
    print(f"Report JSON: {args.report_json}")


if __name__ == "__main__":
    main()
