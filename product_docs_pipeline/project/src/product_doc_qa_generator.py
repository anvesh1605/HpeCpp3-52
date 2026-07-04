"""Deterministic Q&A generation for product documentation records."""

from __future__ import annotations

import re
from typing import Any

try:
    from .product_doc_parser import normalize_text
except ImportError:  # pragma: no cover
    from product_doc_parser import normalize_text


SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+")
SYNTAX_PREFIX_RE = re.compile(r"^\s*Syntax\s*:\s*", re.IGNORECASE)


def format_version_for_question(version: str) -> str:
    return str(version or "").replace("_", ".")


def _sentence(text: str) -> str:
    cleaned = normalize_text(text).strip()
    if not cleaned:
        return ""
    if cleaned.endswith((".", "?", "!", ":", "]", ")", ">")):
        return cleaned
    return f"{cleaned}."


def _ensure_period(text: str) -> str:
    cleaned = normalize_text(text).strip()
    if not cleaned:
        return ""
    if cleaned.endswith((".", "?", "!")):
        return cleaned
    return f"{cleaned}."


def _syntax_answer(syntax: str) -> str:
    return f"Syntax: {normalize_text(syntax)}"


def _command_description_sentence(command: str, description: str) -> str:
    cleaned = normalize_text(description).strip()
    if not cleaned:
        return f"The {command} command is documented in this guide."
    if cleaned[:1].isupper():
        cleaned = cleaned[0].lower() + cleaned[1:]
    if cleaned.lower().startswith(f"the {command.lower()} command "):
        return _ensure_period(cleaned)
    return _ensure_period(f"The {command} command {cleaned}")


def _cap_answer(text: str, max_chars: int = 1200) -> str:
    cleaned = normalize_text(text)
    if len(cleaned) <= max_chars:
        return cleaned
    cutoff = cleaned.rfind(". ", 0, max_chars)
    if cutoff < 240:
        cutoff = max_chars
    return cleaned[: cutoff + 1].strip()


def _question_prefix(record: dict[str, Any], ground: bool) -> str:
    if not ground:
        return ""
    switch = normalize_text(str(record.get("switch", ""))) or "unknown_from_product_doc"
    version = format_version_for_question(normalize_text(str(record.get("version", ""))) or "unknown_version")
    return f"For {switch} AOS-CX {version}, "


def _qa_row(record: dict[str, Any], question: str, answer: str) -> dict[str, Any]:
    payload = {
        "source_type": record.get("source_type", "product_documentation"),
        "data_family": record.get("data_family", "concept_explanation"),
        "switch": record.get("switch", "unknown_from_product_doc"),
        "version": record.get("version", "unknown_version"),
        "document_title": record.get("document_title", ""),
        "section": record.get("section", ""),
        "source_file": record.get("source_file", ""),
        "messages": [
            {"role": "user", "content": normalize_text(question)},
            {"role": "assistant", "content": _sentence(answer)},
        ],
    }
    optional_fields = (
        "command",
        "syntax",
        "sub_version",
        "subversion",
        "task",
        "topic",
        "method",
        "endpoint",
        "object_name",
        "oid",
        "event_id",
    )
    for field in optional_fields:
        value = record.get(field)
        if value:
            payload[field] = value
    return payload


def _command_subject(command: str) -> str:
    return f"the {command} command"


def _join_items(items: list[Any], max_items: int = 8) -> str:
    cleaned = [normalize_text(str(item)) for item in items if normalize_text(str(item))]
    return "; ".join(cleaned[:max_items])


def _example_text(examples: list[Any]) -> str:
    if not examples:
        return ""
    value = str(examples[0]).strip()
    value = re.sub(r"^```[A-Za-z0-9_-]*\s*", "", value)
    value = re.sub(r"\s*```$", "", value)
    return value.strip()


def _imperative_task(task: str) -> str:
    cleaned = normalize_text(task)
    replacements = (
        (r"^Configuring\b", "configure"),
        (r"^Enabling\b", "enable"),
        (r"^Disabling\b", "disable"),
        (r"^Creating\b", "create"),
        (r"^Adding\b", "add"),
        (r"^Removing\b", "remove"),
        (r"^Verifying\b", "verify"),
        (r"^Troubleshooting\b", "troubleshoot"),
        (r"^Installing\b", "install"),
        (r"^Upgrading\b", "upgrade"),
    )
    for pattern, replacement in replacements:
        if re.search(pattern, cleaned, flags=re.IGNORECASE):
            return re.sub(pattern, replacement, cleaned, count=1, flags=re.IGNORECASE)
    if cleaned[:1].isupper():
        return cleaned[0].lower() + cleaned[1:]
    return cleaned


def _is_bad_step(step: str) -> bool:
    cleaned = normalize_text(step).strip(" .;:")
    if not cleaned:
        return True
    lowered = cleaned.lower()
    if lowered in {"if", "then", "or", "and", "command to change it"}:
        return True
    if re.search(r"\b(?:if|then|or|and|to|with|from|for|when|where|that|the|a|an|of)$", lowered):
        return True
    if len(cleaned.split()) == 1 and len(cleaned) > 28:
        return True
    return False


def generate_command_qa(record: dict[str, Any], ground: bool = True) -> list[dict[str, Any]]:
    command = normalize_text(str(record.get("command", "")))
    if not command:
        return []
    prefix = _question_prefix(record, ground)
    subject = _command_subject(command)
    rows: list[dict[str, Any]] = []

    description = normalize_text(str(record.get("description", "")))
    syntax = normalize_text(str(record.get("syntax", "")))
    if description or syntax:
        command_answer = _command_description_sentence(command, description)
        if syntax:
            command_answer = f"{command_answer}\n{_syntax_answer(syntax)}"
        rows.append(
            _qa_row(
                record,
                f"{prefix}what does {subject} do?",
                command_answer,
            )
        )

    if syntax:
        rows.append(
            _qa_row(
                record,
                f"{prefix}what is the syntax of {subject}?",
                _syntax_answer(syntax),
            )
        )

    return rows


def generate_procedure_qa(record: dict[str, Any], ground: bool = True) -> list[dict[str, Any]]:
    task = normalize_text(str(record.get("task", "") or record.get("section", "")))
    steps = record.get("procedure", [])
    if not task or not isinstance(steps, list) or not steps:
        return []
    steps = [normalize_text(str(step)) for step in steps if not _is_bad_step(str(step))]
    if not steps:
        return []
    prefix = _question_prefix(record, ground)
    task_phrase = _imperative_task(task)
    step_text = " ".join(f"{index}. {normalize_text(str(step)).rstrip('.')}" for index, step in enumerate(steps[:12], start=1))
    command_text = ""
    commands = record.get("commands", [])
    if isinstance(commands, list) and commands:
        command_text = f" Commands shown in the procedure include: {_join_items(commands, max_items=6)}."
    answer = f"To {task_phrase}, follow the documented procedure: {step_text}.{command_text}"
    return [
        _qa_row(
            record,
            f"{prefix}how do you {task_phrase}?",
            answer,
        )
    ]


def _concept_question(record: dict[str, Any], ground: bool) -> str:
    prefix = _question_prefix(record, ground)
    topic = normalize_text(str(record.get("topic", "") or record.get("section", "this topic")))
    family = record.get("data_family", "")
    direct_topic = re.sub(r"\s+Overview$", "", topic, flags=re.IGNORECASE).strip()
    if family == "feature_limitation":
        return f"{prefix}what restrictions or notes are documented for {topic}?"
    if family == "troubleshooting":
        return f"{prefix}what troubleshooting information is documented for {topic}?"
    if family == "security_policy":
        return f"{prefix}what security policy information is documented for {topic}?"
    if family == "qos_policy":
        return f"{prefix}what QoS policy information is documented for {topic}?"
    if family == "routing_feature":
        return f"{prefix}what routing behavior is documented for {topic}?"
    if family == "monitoring_feature":
        return f"{prefix}what monitoring behavior is documented for {topic}?"
    if topic.lower().endswith(" overview") and direct_topic:
        return f"{prefix}what is {direct_topic}?"
    if re.fullmatch(r"[A-Z0-9-]{2,12}", topic):
        return f"{prefix}what is {topic}?"
    return f"{prefix}what does the guide say about {topic}?"


def generate_concept_qa(record: dict[str, Any], ground: bool = True) -> list[dict[str, Any]]:
    description = _cap_answer(str(record.get("description", "")), max_chars=1100)
    if not description:
        return []
    topic = normalize_text(str(record.get("topic", "") or record.get("section", "This topic")))
    answer_topic = re.sub(r"\s+Overview$", "", topic, flags=re.IGNORECASE).strip() or topic
    family = record.get("data_family", "")
    if family == "feature_limitation":
        answer = f"For {topic}, the guide documents the following restrictions, notes, or considerations: {description}"
    elif family == "troubleshooting":
        answer = f"For {topic}, the guide documents this troubleshooting information: {description}"
    else:
        answer = f"{answer_topic}: {description}"
    return [_qa_row(record, _concept_question(record, ground), answer)]


def generate_rest_qa(record: dict[str, Any], ground: bool = True) -> list[dict[str, Any]]:
    method = normalize_text(str(record.get("method", "")))
    endpoint = normalize_text(str(record.get("endpoint", "")))
    if not method or not endpoint:
        return []
    prefix = _question_prefix(record, ground)
    description = _cap_answer(str(record.get("description", "")), max_chars=800)
    answer = f"The REST API reference documents {method} {endpoint}."
    if description:
        answer += f" Details: {description}"
    return [_qa_row(record, f"{prefix}what REST API endpoint is documented for {method} {endpoint}?", answer)]


def generate_snmp_qa(record: dict[str, Any], ground: bool = True) -> list[dict[str, Any]]:
    oid = normalize_text(str(record.get("oid", "")))
    object_name = normalize_text(str(record.get("object_name", "")))
    description = _cap_answer(str(record.get("description", "")), max_chars=800)
    if not (oid or object_name or description):
        return []
    prefix = _question_prefix(record, ground)
    subject = object_name or oid or normalize_text(str(record.get("section", "this SNMP object")))
    answer = f"The SNMP MIB reference documents {subject}."
    if oid:
        answer += f" OID: {oid}."
    if description:
        answer += f" Description: {description}"
    return [_qa_row(record, f"{prefix}what SNMP MIB information is documented for {subject}?", answer)]


def generate_event_qa(record: dict[str, Any], ground: bool = True) -> list[dict[str, Any]]:
    event_id = normalize_text(str(record.get("event_id", "")))
    description = _cap_answer(str(record.get("description", "")), max_chars=800)
    if not (event_id or description):
        return []
    prefix = _question_prefix(record, ground)
    subject = event_id or normalize_text(str(record.get("section", "this event")))
    if event_id:
        answer = f"The event log reference documents Event ID {event_id}."
    else:
        answer = f"The event log reference documents event {subject}."
    severity = normalize_text(str(record.get("severity", "")))
    action = normalize_text(str(record.get("recommended_action", "")))
    if severity:
        answer += f" Severity: {severity}."
    if description:
        answer += f" Description: {description}"
    if action:
        answer += f" Recommended action: {action}."
    return [_qa_row(record, f"{prefix}what event log information is documented for {subject}?", answer)]


def generate_qa_for_record(record: dict[str, Any], ground: bool = True) -> list[dict[str, Any]]:
    family = record.get("data_family", "")
    if family in {"cli_command_reference", "show_command_reference"}:
        return generate_command_qa(record, ground=ground)
    if family in {"configuration_procedure", "web_ui_task", "troubleshooting"} and record.get("procedure"):
        return generate_procedure_qa(record, ground=ground)
    if family == "rest_api_reference":
        return generate_rest_qa(record, ground=ground)
    if family == "snmp_mib_reference":
        return generate_snmp_qa(record, ground=ground)
    if family == "event_log_reference":
        return generate_event_qa(record, ground=ground)
    return generate_concept_qa(record, ground=ground)


def generate_qa_rows(records: list[dict[str, Any]], ground: bool = True) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for record in records:
        rows.extend(generate_qa_for_record(record, ground=ground))
    return rows
