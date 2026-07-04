#!/usr/bin/env python3
"""Convert Aruba release-note and product-doc chat rows into an LSTM JSONL.

The converter accepts either `train_chat.jsonl` files directly or directories
that contain them. It emits a compact row schema with `input_text`, `labels`,
`slots`, `fact_key`, `target_value`, `answer_template`, and `final_answer`.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, Iterator, List, Mapping, MutableMapping, Optional, Sequence, Tuple


SUPPORTED_SOURCE_DOMAINS = {"release_notes", "product_docs"}

RELEASE_INTENTS = {
    "bug_category",
    "bug_symptom",
    "bug_scenario",
    "bug_workaround",
    "bug_known_issue",
    "bug_resolved_issue",
    "version_release_date",
    "version_remarks",
    "release_caveat",
    "release_certification",
    "release_compatibility",
    "release_downgrade_restore",
    "release_supported_products",
    "release_upgrade_procedure",
    "release_generic",
}

PRODUCT_INTENTS = {
    "cli_syntax",
    "cli_meaning",
    "show_command_syntax",
    "show_command_meaning",
    "event_log_meaning",
    "configuration_procedure",
    "concept_explanation",
    "snmp_mib_info",
    "troubleshooting",
    "product_caveat",
    "product_requirement",
    "product_limitation",
    "product_generic",
}

INTENTS = RELEASE_INTENTS | PRODUCT_INTENTS

ANSWER_TYPES = {
    "category",
    "symptom",
    "scenario",
    "workaround",
    "known_issue",
    "resolved_issue",
    "release_date",
    "remarks",
    "caveat",
    "certification",
    "compatibility",
    "downgrade_restore",
    "supported_products",
    "upgrade_procedure",
    "cli_syntax",
    "cli_meaning",
    "show_syntax",
    "show_meaning",
    "event_meaning",
    "procedure",
    "concept",
    "snmp_mib",
    "troubleshooting",
    "requirement",
    "limitation",
    "generic",
}

RELEASE_SOURCE_TYPES = {
    "release_notes_caveats",
    "release_notes_certifications",
    "release_notes_compatibility",
    "release_notes_downgrade_restore",
    "release_notes_known_issues",
    "release_notes_resolved_issues",
    "release_notes_supported_products",
    "release_notes_upgrade_procedure",
    "release_notes_version_history",
}

PRODUCT_FAMILIES = {
    "cli_command_reference",
    "show_command_reference",
    "event_log_reference",
    "configuration_procedure",
    "concept_explanation",
    "snmp_mib_reference",
    "troubleshooting",
    "feature_limitation",
    "monitoring_feature",
    "routing_feature",
    "rest_api_reference",
}

PRODUCT_SOURCE_PREFIX = "product_"
RELEASE_SOURCE_PREFIX = "release_notes_"

PRODUCT_JSONL_BASENAMES = {"train_chat.jsonl"}

CLI_SYNTAX_RE = re.compile(
    r"(?i)(?:\bwhat\s+is\s+the\s+(?:exact\s+)?syntax\b|\bexact\s+syntax\b|"
    r"\bcommand\s+syntax\b|\bsyntax\s+of\b|\bgive\s+(?:me\s+)?the\s+(?:exact\s+)?syntax\b|"
    r"\bshow\s+the\s+syntax\b|\bsyntax\b)"
)
REMARKS_RE = re.compile(r"(?i)\bremarks?\b")
RELEASE_DATE_RE = re.compile(r"(?i)\b(?:when\b|released\b|release date\b)")
BUG_CATEGORY_RE = re.compile(r"(?i)\b(?:what|which)\s+category\b|\bbelongs to\b")
BUG_SYMPTOM_RE = re.compile(r"(?i)\bsymptom\b|\bwhat issue\b|\bwhat problem\b")
BUG_SCENARIO_RE = re.compile(r"(?i)\bscenario\b|\bunder what scenario\b|\bwhen does\b|\bunder what condition")
BUG_WORKAROUND_RE = re.compile(r"(?i)\bworkaround\b|\bhow do i work around\b|\bwhat should be done\b")
REQUIREMENT_RE = re.compile(
    r"(?i)\b(requirement|required|requires|prerequisite|prerequisites|needed|need to|must)\b"
)
LIMITATION_RE = re.compile(
    r"(?i)\b(limitation|limitations|not supported|unsupported|cannot|can't|unable to|restriction|not available)\b"
)
CAVEAT_RE = re.compile(r"(?i)\b(caveat|warning|caution|important note|important)\b")
PLACEHOLDER_RE = re.compile(r"(?i)\b(?:tbd|todo|placeholder|n/?a|none|null|unknown)\b")
BUG_ID_RE = re.compile(r"\b(\d{5,7})\b")
VERSION_RE = re.compile(r"\b(\d{1,2}\.\d{1,2}(?:\.\d{3,5})?)\b")
COMMAND_RE = re.compile(r"(?i)\b(show|clear|configure|copy|crypto|debug|erase|interface|ip|ipv6|no|policy|reload|router|vlan)\b")


def normalize(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "").replace("\r\n", "\n").replace("\r", "\n")).strip()


def collapse(value: Any) -> str:
    return re.sub(r"\s+", " ", normalize(value))


def lower(value: Any) -> str:
    return collapse(value).casefold()


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def short_hash(*parts: Any, size: int = 10) -> str:
    seed = "\n".join(collapse(part) for part in parts)
    return sha256_text(seed)[:size]


def display_version(value: Any) -> str:
    text = collapse(value)
    return text.replace("_", ".")


def first_message(row: Mapping[str, Any], role: str) -> str:
    for message in row.get("messages") or []:
        if isinstance(message, Mapping) and lower(message.get("role")) == role:
            return collapse(message.get("content"))
    return ""


def extract_qa(row: Mapping[str, Any]) -> Tuple[str, str]:
    return first_message(row, "user"), first_message(row, "assistant")


def source_domain(row: Mapping[str, Any]) -> str:
    source_type = lower(row.get("source_type"))
    data_family = lower(row.get("data_family"))
    if source_type.startswith(RELEASE_SOURCE_PREFIX) or data_family.startswith(RELEASE_SOURCE_PREFIX):
        return "release_notes"
    if (
        source_type.startswith(PRODUCT_SOURCE_PREFIX)
        or source_type == "product_documentation"
        or data_family in PRODUCT_FAMILIES
    ):
        return "product_docs"
    return "other"


def is_show_command(command: str, question: str, answer: str) -> bool:
    text = " ".join(filter(None, (command, question, answer))).casefold()
    return bool(re.search(r"\bshow\b", text))


def has_syntax_signal(question: str, answer: str) -> bool:
    return bool(CLI_SYNTAX_RE.search(question) or re.search(r"(?i)\bsyntax\s*:", answer))


def has_meaning_signal(question: str, answer: str) -> bool:
    text = " ".join((question, answer))
    return bool(re.search(r"(?i)\bwhat does\b|\bwhat is\b|\bdescribe\b|\bmeaning\b", text))


def release_intent(row: Mapping[str, Any], question: str, answer: str) -> str:
    source_type = lower(row.get("source_type"))
    q = lower(question)
    a = lower(answer)

    if source_type == "release_notes_known_issues":
        if BUG_CATEGORY_RE.search(q):
            return "bug_category"
        if BUG_SYMPTOM_RE.search(q):
            return "bug_symptom"
        if BUG_SCENARIO_RE.search(q):
            return "bug_scenario"
        if BUG_WORKAROUND_RE.search(q):
            return "bug_workaround"
        return "bug_known_issue"

    if source_type == "release_notes_resolved_issues":
        if BUG_CATEGORY_RE.search(q):
            return "bug_category"
        if BUG_SYMPTOM_RE.search(q):
            return "bug_symptom"
        if BUG_SCENARIO_RE.search(q):
            return "bug_scenario"
        if BUG_WORKAROUND_RE.search(q):
            return "bug_workaround"
        return "bug_resolved_issue"

    if source_type == "release_notes_version_history":
        return "version_remarks" if REMARKS_RE.search(q) or REMARKS_RE.search(a) else "version_release_date"

    mapping = {
        "release_notes_caveats": "release_caveat",
        "release_notes_certifications": "release_certification",
        "release_notes_compatibility": "release_compatibility",
        "release_notes_downgrade_restore": "release_downgrade_restore",
        "release_notes_supported_products": "release_supported_products",
        "release_notes_upgrade_procedure": "release_upgrade_procedure",
    }
    return mapping.get(source_type, "release_generic")


def product_intent(row: Mapping[str, Any], question: str, answer: str) -> str:
    family = lower(row.get("data_family"))
    source_type = lower(row.get("source_type"))
    command = command_value(row)
    text = " ".join(
        collapse(part)
        for part in (
            question,
            answer,
            row.get("section"),
            row.get("topic"),
            row.get("document_title"),
            row.get("source_file"),
        )
        if collapse(part)
    )
    if family in {"cli_command_reference", "show_command_reference"} or source_type == "product_cli_reference" or command:
        if is_show_command(command, question, answer) or family == "show_command_reference":
            return "show_command_syntax" if has_syntax_signal(question, answer) else "show_command_meaning"
        return "cli_syntax" if has_syntax_signal(question, answer) else "cli_meaning"
    if family == "event_log_reference" or source_type == "product_event_log_reference":
        return "event_log_meaning"
    if family == "configuration_procedure":
        return "configuration_procedure"
    if family == "concept_explanation":
        return "concept_explanation"
    if family == "snmp_mib_reference":
        return "snmp_mib_info"
    if family == "troubleshooting":
        return "troubleshooting"
    if family == "feature_limitation":
        return "product_limitation"
    if LIMITATION_RE.search(text):
        return "product_limitation"
    if REQUIREMENT_RE.search(text):
        return "product_requirement"
    if CAVEAT_RE.search(text):
        return "product_caveat"
    return "product_generic"


def detect_intent(row: Mapping[str, Any], question: str, answer: str) -> str:
    domain = source_domain(row)
    if domain == "release_notes":
        return release_intent(row, question, answer)
    if domain == "product_docs":
        return product_intent(row, question, answer)
    return "release_generic"


def answer_type_for_intent(intent: str) -> str:
    mapping = {
        "bug_category": "category",
        "bug_symptom": "symptom",
        "bug_scenario": "scenario",
        "bug_workaround": "workaround",
        "bug_known_issue": "known_issue",
        "bug_resolved_issue": "resolved_issue",
        "version_release_date": "release_date",
        "version_remarks": "remarks",
        "release_caveat": "caveat",
        "release_certification": "certification",
        "release_compatibility": "compatibility",
        "release_downgrade_restore": "downgrade_restore",
        "release_supported_products": "supported_products",
        "release_upgrade_procedure": "upgrade_procedure",
        "release_generic": "generic",
        "cli_syntax": "cli_syntax",
        "cli_meaning": "cli_meaning",
        "show_command_syntax": "show_syntax",
        "show_command_meaning": "show_meaning",
        "event_log_meaning": "event_meaning",
        "configuration_procedure": "procedure",
        "concept_explanation": "concept",
        "snmp_mib_info": "snmp_mib",
        "troubleshooting": "troubleshooting",
        "product_caveat": "caveat",
        "product_requirement": "requirement",
        "product_limitation": "limitation",
        "product_generic": "generic",
    }
    return mapping[intent]


def answer_template_for_intent(intent: str) -> str:
    if intent in {"cli_syntax", "show_command_syntax"}:
        return "Syntax: {target_value}"
    if intent == "release_caveat":
        return "Caveat: {target_value}"
    if intent == "release_certification":
        return "Certification information: {target_value}"
    if intent == "release_compatibility":
        return "Compatibility information: {target_value}"
    if intent == "release_downgrade_restore":
        return "Downgrade/restore information: {target_value}"
    if intent == "release_supported_products":
        return "Supported products: {target_value}"
    if intent == "release_upgrade_procedure":
        return "Upgrade procedure: {target_value}"
    return "{target_value}"


def command_value(row: Mapping[str, Any]) -> str:
    return collapse(row.get("command") or row.get("command_name"))


def _extract_version_token(text: str) -> str:
    match = VERSION_RE.search(text)
    return match.group(1) if match else ""


def topic_or_hash(row: Mapping[str, Any], question: str, answer: str, intent: str) -> str:
    candidates: List[str] = []
    if intent.startswith("bug_"):
        candidates.extend([row.get("category"), row.get("feature"), row.get("section"), row.get("topic"), row.get("bug_id")])
    elif intent in {"version_release_date", "version_remarks"}:
        candidates.extend([row.get("version_number"), _extract_version_token(question), _extract_version_token(answer), row.get("section"), row.get("topic")])
    elif intent.startswith("release_"):
        candidates.extend([row.get("topic"), row.get("feature"), row.get("section"), row.get("browser"), row.get("product_name"), row.get("source_file")])
    elif intent in {"cli_syntax", "cli_meaning", "show_command_syntax", "show_command_meaning"}:
        candidates.extend([command_value(row), row.get("topic"), row.get("section"), row.get("document_title"), row.get("source_file")])
    else:
        candidates.extend([row.get("topic"), row.get("section"), row.get("document_title"), row.get("source_file")])

    for candidate in candidates:
        cleaned = collapse(candidate)
        if cleaned:
            return cleaned
    return short_hash(question, answer)


def strip_leading_prefix(text: str, patterns: Sequence[str]) -> str:
    value = collapse(text)
    for pattern in patterns:
        value = re.sub(pattern, "", value, flags=re.I).strip()
    return value


def clean_target_value(intent: str, row: Mapping[str, Any], question: str, answer: str) -> str:
    value = collapse(answer)

    if intent.startswith("bug_"):
        value = re.sub(r"^[^(]+\s*\(Bug ID\s+\d+\):\s*", "", value, flags=re.I)
        return value

    if intent == "version_release_date":
        value = re.sub(r"(?i)^version history:\s*", "", value).strip()
        remarks = re.split(r"(?i)\s+remarks?:\s*", value, maxsplit=1)[0].strip()
        return remarks

    if intent == "version_remarks":
        match = re.search(r"(?is)\bremarks?\s*:\s*(.+)$", value)
        if match:
            return re.split(r"\n|(?<=\.)\s+(?=[A-Z])", collapse(match.group(1)), maxsplit=1)[0].strip()
        return value

    if intent == "release_caveat":
        value = re.sub(r"(?i)^feature caveat:\s*", "", value).strip()
        parts = re.split(r"\s+-\s+", value, maxsplit=1)
        return parts[1].strip() if len(parts) == 2 else value

    if intent == "release_certification":
        return strip_leading_prefix(value, [r"^certification information:\s*", r"^certification:\s*"])

    if intent == "release_compatibility":
        return strip_leading_prefix(value, [r"^compatibility information:\s*", r"^compatibility:\s*"])

    if intent == "release_downgrade_restore":
        return strip_leading_prefix(value, [r"^downgrade/restore information:\s*", r"^downgrade/restore:\s*"])

    if intent == "release_supported_products":
        return strip_leading_prefix(value, [r"^supported products:\s*"])

    if intent == "release_upgrade_procedure":
        return strip_leading_prefix(value, [r"^upgrade procedure:\s*"])

    if intent in {"cli_syntax", "show_command_syntax"}:
        syntax_match = re.search(r"(?is)\bsyntax\s*:\s*(.+)$", value)
        if syntax_match:
            return collapse(syntax_match.group(1))
        return value

    if intent in {"cli_meaning", "show_command_meaning"}:
        if re.search(r"(?is)\bsyntax\s*:\s*", value):
            return re.split(r"(?is)\bsyntax\s*:\s*", value, maxsplit=1)[0].strip()
        return value

    if intent == "event_log_meaning":
        return strip_leading_prefix(value, [r"^event id\s*:\s*", r"^event meaning\s*:\s*"])

    return value


def final_answer_for_intent(intent: str, target_value: str, row: Mapping[str, Any], question: str) -> str:
    template = answer_template_for_intent(intent)
    if template == "{target_value}":
        return target_value
    return template.format(target_value=target_value, version=display_version(row.get("version")), sub_version=collapse(row.get("sub_version")))


def clean_question(question: str, row: Mapping[str, Any]) -> str:
    return collapse(question)


def should_review(intent: str, target_value: str, question: str, answer: str) -> Optional[str]:
    if not collapse(question):
        return "missing_question"
    if not collapse(answer):
        return "missing_answer"
    if PLACEHOLDER_RE.search(answer):
        return "placeholder_answer"
    if not collapse(target_value):
        return "empty_target_value"
    return None


def build_fact_key(row: Mapping[str, Any], intent: str, answer_type: str, question: str, answer: str) -> str:
    domain = source_domain(row)
    switch = collapse(row.get("switch"))
    version = display_version(row.get("version"))
    sub_version = collapse(row.get("sub_version"))
    topic = topic_or_hash(row, question, answer, intent)

    if domain == "release_notes":
        if intent.startswith("bug_"):
            bug_id = collapse(row.get("bug_id")) or collapse(BUG_ID_RE.search(" ".join((question, answer))).group(1) if BUG_ID_RE.search(" ".join((question, answer))) else "")
            if not bug_id:
                bug_id = short_hash(question, answer)
            return f"release_notes|{switch}|{version}|{sub_version}|bug|{bug_id}|{answer_type}"
        if intent in {"version_release_date", "version_remarks"}:
            version_token = collapse(row.get("version_number")) or _extract_version_token(" ".join((question, answer))) or f"{version}.{sub_version}"
            return f"release_notes|{switch}|{version}|{sub_version}|version_history|{version_token}|{answer_type}"
        if intent.startswith("release_"):
            topic_key = topic if topic else short_hash(question, answer)
            kind = intent.removeprefix("release_")
            return f"release_notes|{switch}|{version}|{sub_version}|{kind}|{topic_key}|{kind}"
        return f"release_notes|{switch}|{version}|{sub_version}|generic|{topic}|generic"

    if domain == "product_docs":
        topic_key = topic if topic else short_hash(question, answer)
        return f"product_docs|{switch}|{version}|{sub_version}|{intent}|{topic_key}|{answer_type}"

    return f"other|{switch}|{version}|{sub_version}|{intent}|{topic}|{answer_type}"


def load_jsonl(path: Path) -> Iterator[Dict[str, Any]]:
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
            yield row


def find_input_files(inputs: Sequence[Path]) -> List[Path]:
    discovered: List[Path] = []
    seen: set[Path] = set()
    for path in inputs:
        if path.is_file():
            if path.name in PRODUCT_JSONL_BASENAMES and path not in seen:
                discovered.append(path)
                seen.add(path)
            continue
        if not path.is_dir():
            raise FileNotFoundError(path)
        for candidate in path.rglob("*.jsonl"):
            if candidate.name not in PRODUCT_JSONL_BASENAMES:
                continue
            if any(part.lower() in {".venv", ".venv3070", "__pycache__", "outputs", "logs"} for part in candidate.parts):
                continue
            if candidate not in seen:
                discovered.append(candidate)
                seen.add(candidate)
    return sorted(discovered)


def convert_row(row: Mapping[str, Any], source_path: Path) -> Tuple[Optional[Dict[str, Any]], Optional[Dict[str, Any]]]:
    question, answer = extract_qa(row)
    if not question or not answer:
        review = {
            "source_file": str(source_path),
            "source_type": row.get("source_type"),
            "data_family": row.get("data_family"),
            "switch": row.get("switch"),
            "version": row.get("version"),
            "sub_version": row.get("sub_version"),
            "question": question,
            "answer": answer,
            "reason": "missing_question_or_answer",
        }
        return None, review

    domain = source_domain(row)
    if domain not in SUPPORTED_SOURCE_DOMAINS:
        review = {
            "source_file": str(source_path),
            "source_type": row.get("source_type"),
            "data_family": row.get("data_family"),
            "switch": row.get("switch"),
            "version": row.get("version"),
            "sub_version": row.get("sub_version"),
            "question": question,
            "answer": answer,
            "reason": f"unsupported_source_domain:{domain}",
        }
        return None, review

    intent = detect_intent(row, question, answer)
    if intent not in INTENTS:
        review = {
            "source_file": str(source_path),
            "source_type": row.get("source_type"),
            "data_family": row.get("data_family"),
            "switch": row.get("switch"),
            "version": row.get("version"),
            "sub_version": row.get("sub_version"),
            "question": question,
            "answer": answer,
            "reason": f"unsupported_intent:{intent}",
        }
        return None, review

    answer_type = answer_type_for_intent(intent)
    target_value = clean_target_value(intent, row, question, answer)
    review_reason = should_review(intent, target_value, question, answer)
    slots = {
        "switch": collapse(row.get("switch")) or None,
        "version": display_version(row.get("version")) or None,
        "sub_version": collapse(row.get("sub_version")) or None,
        "bug_id": collapse(row.get("bug_id")) or None,
        "event_id": collapse(row.get("event_id")) or None,
        "command": command_value(row) or None,
        "topic": topic_or_hash(row, question, answer, intent) or None,
    }
    record = {
        "input_text": clean_question(question, row),
        "labels": {
            "intent": intent,
            "source_domain": domain,
            "answer_type": answer_type,
        },
        "slots": slots,
        "fact_key": build_fact_key(row, intent, answer_type, question, answer),
        "target_value": target_value,
        "answer_template": answer_template_for_intent(intent),
        "final_answer": final_answer_for_intent(intent, target_value, row, question),
    }
    review = None
    if review_reason:
        review = {
            "source_file": str(source_path),
            "source_type": row.get("source_type"),
            "data_family": row.get("data_family"),
            "switch": row.get("switch"),
            "version": row.get("version"),
            "sub_version": row.get("sub_version"),
            "intent": intent,
            "answer_type": answer_type,
            "question": question,
            "answer": answer,
            "target_value": target_value,
            "reason": review_reason,
        }
    return record, review


def convert_files(input_files: Sequence[Path]) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]], Dict[str, Any]]:
    rows_out: List[Dict[str, Any]] = []
    review_rows: List[Dict[str, Any]] = []
    counts: Counter[str] = Counter()
    domain_counts: Counter[str] = Counter()
    intent_counts: Counter[str] = Counter()
    review_counts: Counter[str] = Counter()
    files: List[Dict[str, Any]] = []

    for path in input_files:
        file_rows = 0
        file_reviews = 0
        for row in load_jsonl(path):
            file_rows += 1
            converted, review = convert_row(row, path)
            if converted is not None:
                rows_out.append(converted)
                counts[converted["labels"]["intent"]] += 1
                domain_counts[converted["labels"]["source_domain"]] += 1
                intent_counts[converted["labels"]["intent"]] += 1
            if review is not None:
                review_rows.append(review)
                file_reviews += 1
                review_counts[review["reason"]] += 1
        files.append({"path": str(path), "rows_scanned": file_rows, "review_rows": file_reviews})

    report = {
        "input_files": files,
        "rows_written": len(rows_out),
        "review_rows_written": len(review_rows),
        "rows_by_source_domain": dict(sorted(domain_counts.items())),
        "rows_by_intent": dict(sorted(intent_counts.items())),
        "review_reasons": dict(sorted(review_counts.items())),
    }
    return rows_out, review_rows, report


def write_jsonl(path: Path, rows: Iterable[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    script_dir = Path(__file__).resolve().parent
    data_root = script_dir.parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        dest="inputs",
        action="append",
        type=Path,
        default=None,
        help="Input JSONL file or directory. May be supplied multiple times.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=data_root / "lstm_conversion" / "lstm_dataset.jsonl",
        help="Output JSONL file for the converted LSTM rows.",
    )
    parser.add_argument(
        "--review-output",
        type=Path,
        default=data_root / "lstm_conversion" / "lstm_review_rows.jsonl",
        help="Output JSONL file for rows that need manual review.",
    )
    parser.add_argument(
        "--report-output",
        type=Path,
        default=data_root / "lstm_conversion" / "lstm_conversion_report.json",
        help="Output JSON report summarizing the conversion.",
    )
    parser.add_argument("--force", action="store_true", help="Overwrite existing outputs.")
    args = parser.parse_args(argv)
    if not args.inputs:
        args.inputs = [
            data_root / "full_product_docs",
            data_root / "release notes",
        ]
    return args


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)
    output_paths = [args.output, args.review_output, args.report_output]
    if not args.force:
        for path in output_paths:
            if path.exists():
                raise FileExistsError(f"Refusing to overwrite {path}; pass --force")

    input_files = find_input_files(args.inputs)
    if not input_files:
        raise FileNotFoundError("No input JSONL files found")

    rows_out, review_rows, report = convert_files(input_files)
    write_jsonl(args.output, rows_out)
    write_jsonl(args.review_output, review_rows)

    report = {
        **report,
        "files": {
            "output": {"path": str(args.output), "sha256": sha256_file(args.output)},
            "review_output": {"path": str(args.review_output), "sha256": sha256_file(args.review_output)},
        },
    }
    args.report_output.parent.mkdir(parents=True, exist_ok=True)
    args.report_output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
