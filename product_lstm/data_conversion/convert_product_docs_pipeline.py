#!/usr/bin/env python3
"""Convert and repair Aruba product-documentation chat rows into LSTM JSONL."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, Iterable, Iterator, List, Mapping, Optional, Sequence, Tuple


SUPPORTED_PRODUCT_INTENTS = {
    "cli_syntax",
    "cli_meaning",
    "show_command_syntax",
    "show_command_meaning",
    "event_log_meaning",
    "configuration_procedure",
    "concept_explanation",
    "snmp_mib_info",
    "troubleshooting",
    "product_limitation",
    "product_requirement",
    "product_caveat",
    "product_generic",
}

CLI_SYNTAX_RE = re.compile(
    r"(?i)(?:\bwhat\s+is\s+the\s+(?:exact\s+)?syntax\b|\bexact\s+syntax\b|"
    r"\bcommand\s+syntax\b|\bsyntax\s+of\b|\bgive\s+(?:me\s+)?the\s+(?:exact\s+)?syntax\b|"
    r"\bshow\s+the\s+syntax\b|\bsyntax\b)"
)
CLI_MEANING_RE = re.compile(r"(?i)\bwhat\s+does\b|\bwhat\s+is\b|\bmeaning\b|\bpurpose\b")
CONFIG_RE = re.compile(r"(?i)\bhow\s+do\s+you\s+configure\b|\bconfigure\b")
CONCEPT_RE = re.compile(r"(?i)\bwhat\s+is\b|\bwhat\s+does\s+the\s+guide\s+say\s+about\b|\bconcept\b")
SNMP_RE = re.compile(r"(?i)\bsnmp\b|\bmib\b")
EVENT_RE = re.compile(r"(?i)\bevent\s+log\b|\bevent\s+id\b")
TROUBLESHOOT_RE = re.compile(r"(?i)\btroubleshoot\b|\btroubleshooting\b")
LIMITATION_RE = re.compile(
    r"(?i)\b(limitation|limitations|not supported|unsupported|cannot|can't|unable to|restriction|not available)\b"
)
REQUIREMENT_RE = re.compile(r"(?i)\b(requirement|required|requires|prerequisite|prerequisites|must)\b")
CAVEAT_RE = re.compile(r"(?i)\b(caveat|warning|caution|important note|important)\b")
MOJIBAKE_FIXES = {
    "Â©": "©",
    "Ã¢â‚¬Â¢": "-",
    "Ã¢â€”Â¦": "-",
    "Ã¢â‚¬â€œ": "-",
    "Ã¢â‚¬â€": "-",
    "Ã¢â‚¬Å“": '"',
    "Ã¢â‚¬Â": '"',
    "Ã¢â‚¬â„¢": "'",
    "Ã‚": "",
    "â€“": "-",
    "â€”": "-",
    "â€œ": '"',
    "â€": '"',
    "â€˜": "'",
    "â€™": "'",
    "Â": "",
}
TEXT_NOISE_RE = re.compile(
    r"(?i)(?:\bdocumented in this guide\b|\bpublic\b|\bpage\s+\d+\b|\btable of contents\b)"
)
BROKEN_SPACING_RE = re.compile(r"(?i)\b(?:Ran ge|wit h|fo r|entri es|re se t|com man d)\b")
PAGE_NUMBER_ONLY_RE = re.compile(r"^\s*\d+\s*$")
DOT_LEADER_RE = re.compile(r"\.{6,}\s*\d+\s*$")
LABEL_RE = re.compile(r"(?i)^(syntax|message|category|severity|description|parameters?|usage|examples?)\s*:?\s*$")
SYNTAX_PREFIX_RE = re.compile(r"(?is)^\s*syntax\s*:?\s*")
SECTION_MARKER_RE = re.compile(
    r"(?i)^(syntax|parameters?|usage|examples?|description|about this task|procedure|steps?|notes?|"
    r"message|category|severity|event id)\b"
)
PLACEHOLDER_RE = re.compile(r"<[^>]+>")
MULTI_COMMAND_BULLET_RE = re.compile(r"(?m)^\s*[-*]\s+\S+")
WHITESPACE_RE = re.compile(r"\s+")
STOP_WORDS = {
    "the",
    "a",
    "an",
    "of",
    "and",
    "or",
    "to",
    "for",
    "with",
    "in",
    "on",
    "by",
    "what",
    "is",
    "does",
    "do",
    "does",
    "how",
    "you",
    "guide",
    "say",
    "about",
    "this",
    "that",
    "command",
    "information",
}


def clean_text(value: Any) -> str:
    text = str(value or "").replace("\r\n", "\n").replace("\r", "\n")
    for bad, good in MOJIBAKE_FIXES.items():
        text = text.replace(bad, good)
    text = text.replace("\f", "\n")
    text = WHITESPACE_RE.sub(" ", text).strip()
    return text


def clean_line(value: Any) -> str:
    text = str(value or "").replace("\r\n", "\n").replace("\r", "\n")
    for bad, good in MOJIBAKE_FIXES.items():
        text = text.replace(bad, good)
    text = text.replace("\f", "")
    text = text.strip()
    text = WHITESPACE_RE.sub(" ", text)
    return text


def collapse(value: Any) -> str:
    return WHITESPACE_RE.sub(" ", clean_text(value)).strip()


def normalize_key(value: Any) -> str:
    return collapse(value).casefold()


def display_version(value: Any) -> str:
    return collapse(value).replace("_", ".")


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def short_hash(*parts: Any, size: int = 10) -> str:
    seed = "\n".join(collapse(part) for part in parts)
    return sha256_text(seed)[:size]


def sentence(value: Any) -> str:
    text = collapse(value)
    if not text:
        return ""
    text = re.sub(r"\s+([,.!?;:])", r"\1", text)
    if text[-1] not in ".!?":
        text += "."
    return text


def extract_qa(row: Mapping[str, Any]) -> Tuple[str, str]:
    question = collapse(row.get("question"))
    answer = collapse(row.get("answer"))
    for message in row.get("messages") or []:
        if not isinstance(message, Mapping):
            continue
        role = normalize_key(message.get("role"))
        content = collapse(message.get("content"))
        if role == "user" and not question:
            question = content
        elif role == "assistant" and not answer:
            answer = content
    return question, answer


def source_domain(row: Mapping[str, Any]) -> str:
    source_type = normalize_key(row.get("source_type"))
    data_family = normalize_key(row.get("data_family"))
    if source_type.startswith("product_") or data_family in {
        "cli_command_reference",
        "show_command_reference",
        "concept_explanation",
        "configuration_procedure",
        "event_log_reference",
        "snmp_mib_reference",
        "troubleshooting",
        "feature_limitation",
        "feature_requirement",
        "product_caveat",
    }:
        return "product_docs"
    return "other"


def command_value(row: Mapping[str, Any], question: str = "", answer: str = "") -> str:
    explicit = collapse(row.get("command") or row.get("command_name"))
    if explicit:
        return explicit
    text = f"{question} {answer}"
    patterns = [
        r"(?i)\bwhat is the syntax of the (?P<command>.+?) command\b",
        r"(?i)\bwhat is the syntax of (?P<command>.+?) command\b",
        r"(?i)\bwhat does the (?P<command>.+?) command do\b",
        r"(?i)\bwhat does the (?P<command>.+?) do\b",
        r"(?i)\bsyntax:\s*(?P<command>.+?)(?:[.\n]|$)",
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return collapse(match.group("command"))
    return ""


def topic_value(row: Mapping[str, Any], question: str, answer: str) -> str:
    candidates = [
        row.get("topic"),
        row.get("feature"),
        row.get("object_name"),
        row.get("section"),
        row.get("document_title"),
    ]
    for candidate in candidates:
        text = collapse(candidate)
        if text:
            return text
    for text in (question, answer):
        match = re.search(r"(?i)\babout\s+(.+?)(?:\?|$)", text)
        if match:
            return collapse(match.group(1))
    return ""


def feature_value(row: Mapping[str, Any], question: str, answer: str) -> str:
    text = collapse(row.get("feature"))
    if text:
        return text
    return topic_value(row, question, answer)


def object_name_value(row: Mapping[str, Any], question: str, answer: str) -> str:
    text = collapse(row.get("object_name"))
    if text:
        return text
    return topic_value(row, question, answer)


def event_id_value(row: Mapping[str, Any], question: str, answer: str) -> str:
    text = collapse(row.get("event_id"))
    if text:
        return text
    match = re.search(r"(?i)\bevent\s+id\s*[:#-]?\s*(\d{3,8})\b", f"{question} {answer}")
    return match.group(1) if match else ""


def intent_from_row(row: Mapping[str, Any], question: str, answer: str) -> str:
    family = normalize_key(row.get("data_family"))
    source_type = normalize_key(row.get("source_type"))
    command = command_value(row, question, answer)
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

    if family in {"cli_command_reference", "show_command_reference"} or source_type.startswith("product_cli") or command:
        if command.casefold().startswith("show ") or family == "show_command_reference" or source_type.startswith(
            "product_show"
        ):
            return "show_command_syntax" if CLI_SYNTAX_RE.search(question) else "show_command_meaning"
        return "cli_syntax" if CLI_SYNTAX_RE.search(question) else "cli_meaning"
    if family == "event_log_reference" or source_type == "product_event_log_reference" or EVENT_RE.search(text):
        return "event_log_meaning"
    if family == "configuration_procedure" or CONFIG_RE.search(text):
        return "configuration_procedure"
    if family == "concept_explanation" or (CONCEPT_RE.search(text) and not command):
        return "concept_explanation"
    if family == "snmp_mib_reference" or SNMP_RE.search(text):
        return "snmp_mib_info"
    if family == "troubleshooting" or TROUBLESHOOT_RE.search(text):
        return "troubleshooting"
    if family == "feature_limitation" or LIMITATION_RE.search(text):
        return "product_limitation"
    if family == "feature_requirement" or REQUIREMENT_RE.search(text):
        return "product_requirement"
    if family == "product_caveat" or CAVEAT_RE.search(text):
        return "product_caveat"
    return "product_generic"


def build_input_text(intent: str, row: Mapping[str, Any], question: str, answer: str) -> str:
    switch = collapse(row.get("switch"))
    version = display_version(row.get("version"))
    command = command_value(row, question, answer)
    topic = topic_value(row, question, answer)
    feature = feature_value(row, question, answer)
    object_name = object_name_value(row, question, answer)
    event_id = event_id_value(row, question, answer)

    if switch and version:
        if intent in {"cli_syntax", "show_command_syntax"} and command:
            return f"For {switch} AOS-CX {version}, what is the syntax of the {command} command?"
        if intent in {"cli_meaning", "show_command_meaning"} and command:
            return f"For {switch} AOS-CX {version}, what does the {command} command do?"
        if intent == "configuration_procedure" and feature:
            return f"For {switch} AOS-CX {version}, how do you configure {feature}?"
        if intent == "concept_explanation" and topic:
            return f"For {switch} AOS-CX {version}, what is {topic}?"
        if intent == "snmp_mib_info" and object_name:
            return f"For {switch} AOS-CX {version}, what SNMP MIB information is documented for {object_name}?"
        if intent == "event_log_meaning" and event_id:
            return f"For {switch} AOS-CX {version}, what event log information is documented for Event ID {event_id}?"
        if intent == "troubleshooting" and topic:
            return f"For {switch} AOS-CX {version}, how do you troubleshoot {topic}?"
        if intent == "product_caveat" and topic:
            return f"For {switch} AOS-CX {version}, what caveat is documented for {topic}?"
        if intent == "product_requirement" and topic:
            return f"For {switch} AOS-CX {version}, what requirement is documented for {topic}?"
        if intent == "product_limitation" and topic:
            return f"For {switch} AOS-CX {version}, what limitation is documented for {topic}?"
        if intent == "product_generic" and topic:
            return f"For {switch} AOS-CX {version}, what does the guide say about {topic}?"
    return collapse(question)


def build_slots(intent: str, row: Mapping[str, Any], question: str, answer: str) -> Dict[str, str]:
    slots: Dict[str, str] = {}
    switch = collapse(row.get("switch"))
    version = display_version(row.get("version"))
    if switch:
        slots["switch"] = switch
    if version:
        slots["version"] = version

    sub_version = collapse(row.get("sub_version"))
    if sub_version:
        slots["sub_version"] = sub_version

    command = command_value(row, question, answer)
    if command and intent in {"cli_syntax", "cli_meaning", "show_command_syntax", "show_command_meaning"}:
        slots["command"] = command

    event_id = event_id_value(row, question, answer)
    if event_id and intent == "event_log_meaning":
        slots["event_id"] = event_id

    feature = feature_value(row, question, answer)
    topic = topic_value(row, question, answer)
    object_name = object_name_value(row, question, answer)
    if intent == "configuration_procedure" and feature:
        slots["feature"] = feature
    elif intent in {"concept_explanation", "troubleshooting", "product_caveat", "product_requirement", "product_limitation", "product_generic"} and topic:
        slots["topic"] = topic
    elif intent == "snmp_mib_info" and object_name:
        slots["object_name"] = object_name

    return slots


def clean_source_lines(lines: Sequence[str]) -> List[str]:
    cleaned: List[str] = []
    for line in lines:
        text = clean_line(line)
        if not text:
            cleaned.append("")
            continue
        if text == "Public":
            continue
        if PAGE_NUMBER_ONLY_RE.match(text):
            continue
        cleaned.append(text)
    return cleaned


def is_toc_like(line: str) -> bool:
    text = clean_line(line)
    if not text:
        return False
    return bool(DOT_LEADER_RE.search(text) or text.lower().startswith("table of contents"))


def score_section_candidate(lines: Sequence[str], idx: int, intent: str, candidate: str) -> int:
    window = [clean_line(line) for line in lines[idx + 1 : idx + 28]]
    prev = [clean_line(line) for line in lines[max(0, idx - 5) : idx]]
    score = 10
    text = " ".join(window)
    if any(is_toc_like(line) for line in prev + window[:3]):
        score -= 50
    if re.search(r"(?i)\bsyntax\b", text):
        score += 40
    if re.search(r"(?i)\bmessage\b", text):
        score += 40
    if re.search(r"(?i)\bseverity\b", text):
        score += 30
    if re.search(r"(?i)\bdescription\b", text):
        score += 20
    if re.search(r"(?i)\bprocedure\b|\bsteps?\b|\babout this task\b", text):
        score += 20
    if sum(len(line) for line in window if line) > 120:
        score += 10
    if len(candidate) > 0:
        score += min(len(candidate), 20)
    return score


def candidate_headings(row: Mapping[str, Any], question: str, answer: str) -> List[str]:
    candidates: List[str] = []
    for key in ("section", "topic", "command", "document_title"):
        text = collapse(row.get(key))
        if text:
            candidates.append(text)
            if text.casefold().startswith("about "):
                candidates.append(text[6:].strip())
    event_id = event_id_value(row, question, answer)
    if event_id:
        candidates.append(f"Event ID: {event_id}")
    command = command_value(row, question, answer)
    if command:
        candidates.append(command)
    for value in candidates[:]:
        if value.endswith(".md"):
            candidates.append(value[:-3])
    unique: List[str] = []
    seen: set[str] = set()
    for value in candidates:
        key = normalize_key(value)
        if key and key not in seen:
            seen.add(key)
            unique.append(value)
    return unique


def find_markdown_file(row: Mapping[str, Any], markdown_roots: Sequence[Path]) -> Optional[Path]:
    source_file = collapse(row.get("source_file"))
    switch = collapse(row.get("switch"))
    version = collapse(row.get("version"))
    rel = Path(source_file.replace("\\", "/")) if source_file else None
    basename = rel.name if rel else ""

    for root in markdown_roots:
        if not root.exists():
            continue
        direct_candidates: List[Path] = []
        if rel:
            direct_candidates.append(root / "Raw_Data_Product" / rel)
            direct_candidates.append(root / rel)
        if switch and version and basename:
            direct_candidates.append(root / "Raw_Data_Product" / switch / version / basename)
        for candidate in direct_candidates:
            if candidate.exists():
                return candidate
        if switch and version and basename:
            search_root = root / "Raw_Data_Product" / switch / version
            if search_root.exists():
                matches = list(search_root.rglob(basename))
                if matches:
                    return sorted(matches, key=lambda p: len(str(p)))[0]
    return None


@lru_cache(maxsize=512)
def load_markdown_lines(path_str: str) -> Tuple[str, ...]:
    path = Path(path_str)
    text = path.read_text(encoding="utf-8", errors="replace")
    return tuple(text.splitlines())


def normalize_heading(value: str) -> str:
    text = clean_line(value)
    text = re.sub(r"^[#>*\-\s]+", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.casefold().strip()


def match_markdown_section(lines: Sequence[str], row: Mapping[str, Any], question: str, answer: str) -> Tuple[Optional[int], Optional[str]]:
    candidates = candidate_headings(row, question, answer)
    best_idx: Optional[int] = None
    best_score = -10**9
    best_candidate: Optional[str] = None
    normalized_candidates = [normalize_heading(candidate) for candidate in candidates]

    for idx, line in enumerate(lines):
        normalized_line = normalize_heading(line)
        if not normalized_line:
            continue
        for candidate, normalized_candidate in zip(candidates, normalized_candidates):
            if normalized_line == normalized_candidate:
                score = score_section_candidate(lines, idx, intent_from_row(row, question, answer), candidate)
                if score > best_score:
                    best_idx = idx
                    best_score = score
                    best_candidate = candidate
    return best_idx, best_candidate


def extract_window(lines: Sequence[str], idx: int, max_lines: int = 140) -> List[str]:
    window = clean_source_lines(lines[idx : idx + max_lines])
    while window and not window[0]:
        window.pop(0)
    while window and not window[-1]:
        window.pop()
    return window


def first_label_index(lines: Sequence[str], labels: Sequence[str]) -> int:
    label_set = {label.casefold() for label in labels}
    for i, line in enumerate(lines):
        if clean_line(line).casefold() in label_set:
            return i
    return -1


def extract_first_paragraph(lines: Sequence[str], start_index: int = 0, stop_labels: Sequence[str] = ()) -> str:
    stop_set = {label.casefold() for label in stop_labels}
    buffer: List[str] = []
    started = False
    for line in lines[start_index:]:
        text = clean_line(line)
        if not text:
            if started:
                break
            continue
        lowered = text.casefold()
        if lowered in stop_set or SECTION_MARKER_RE.match(text):
            if started:
                break
            continue
        if text == "Public" or PAGE_NUMBER_ONLY_RE.match(text) or DOT_LEADER_RE.search(text):
            continue
        started = True
        buffer.append(text)
    return collapse(" ".join(buffer))


def extract_syntax_target(lines: Sequence[str]) -> str:
    for i, line in enumerate(lines):
        text = clean_line(line)
        if not text:
            continue
        if text.casefold().startswith("syntax"):
            tail = SYNTAX_PREFIX_RE.sub("", text).strip()
            if tail:
                return collapse(tail)
            for follow in lines[i + 1 : i + 10]:
                nxt = clean_line(follow)
                if not nxt:
                    if tail:
                        break
                    continue
                if LABEL_RE.match(nxt) or nxt.casefold().startswith("public"):
                    continue
                return collapse(nxt)
    return ""


def extract_command_meaning(lines: Sequence[str]) -> str:
    stop_labels = ("syntax", "parameters", "usage", "examples", "description")
    text = extract_first_paragraph(lines, 1, stop_labels=stop_labels)
    if text:
        return sentence(text)
    return ""


def extract_concept_like(lines: Sequence[str]) -> str:
    text = extract_first_paragraph(lines, 1, stop_labels=("syntax", "parameters", "usage", "examples"))
    if text:
        return sentence(text)
    return ""


def extract_configuration(lines: Sequence[str]) -> str:
    text = extract_first_paragraph(lines, 1, stop_labels=("syntax", "parameters", "usage", "examples"))
    if text:
        return sentence(text)
    return ""


def extract_snmp(lines: Sequence[str]) -> str:
    text = extract_first_paragraph(lines, 1, stop_labels=("syntax", "parameters", "usage", "examples"))
    if text:
        return sentence(text)
    return ""


def extract_event_meaning(lines: Sequence[str], event_id: str) -> str:
    fields: Dict[str, str] = {}
    pending: Optional[str] = None
    labels = {"message", "category", "severity", "description"}
    for line in lines:
        text = clean_line(line)
        if not text:
            continue
        if text.casefold().startswith("event id:") and event_id and event_id not in text:
            break
        lowered = text.casefold()
        if lowered in labels:
            pending = lowered
            continue
        if pending and pending not in fields:
            fields[pending] = text
            pending = None
    severity = fields.get("severity", "")
    message = fields.get("message", "")
    description = fields.get("description", "")
    category = fields.get("category", "")
    if not severity or not message:
        return ""
    parts = [f"Severity: {severity}", message]
    if description and description.casefold() != message.casefold():
        parts.append(description)
    if category and category.casefold() not in {message.casefold(), description.casefold()}:
        parts.append(category)
    return sentence(" ".join(parts))


def repair_target_from_markdown(intent: str, lines: Sequence[str], row: Mapping[str, Any], question: str, answer: str) -> str:
    if intent in {"cli_syntax", "show_command_syntax"}:
        syntax = extract_syntax_target(lines)
        if syntax:
            return syntax
        return ""
    if intent in {"cli_meaning", "show_command_meaning"}:
        return extract_command_meaning(lines)
    if intent in {"concept_explanation", "product_generic", "product_caveat", "product_requirement", "product_limitation", "troubleshooting"}:
        return extract_concept_like(lines)
    if intent == "configuration_procedure":
        return extract_configuration(lines)
    if intent == "snmp_mib_info":
        return extract_snmp(lines)
    if intent == "event_log_meaning":
        return extract_event_meaning(lines, event_id_value(row, question, answer))
    return ""


def clean_target_value(intent: str, raw_answer: str) -> Tuple[str, Dict[str, int]]:
    noise_counts = Counter()
    text = collapse(raw_answer)
    if not text:
        return "", {}
    before = text
    if "Public" in text:
        text = re.sub(r"(?i)\bpublic\b", "", text)
        noise_counts["public_removed"] += 1
    if PAGE_NUMBER_ONLY_RE.search(text):
        text = PAGE_NUMBER_ONLY_RE.sub("", text)
        noise_counts["page_noise_removed"] += 1
    if BROKEN_SPACING_RE.search(text):
        noise_counts["broken_spacing_detected"] += 1
    if intent in {"cli_syntax", "show_command_syntax"}:
        text = SYNTAX_PREFIX_RE.sub("", text).strip()
        if "Syntax:" in before and text != before:
            noise_counts["syntax_prefix_removed"] += 1
    if intent in {"cli_meaning", "show_command_meaning"}:
        text = re.split(r"(?is)\bsyntax\s*:?", text, maxsplit=1)[0].strip()
    if intent == "event_log_meaning":
        text = re.sub(r"(?is)^event\s+id\s*:\s*", "", text).strip()
        text = re.sub(r"(?is)^event\s+meaning\s*:\s*", "", text).strip()
    text = WHITESPACE_RE.sub(" ", text).strip(" -")
    return text, dict(noise_counts)


def intent_limits(intent: str) -> Optional[int]:
    return {
        "concept_explanation": 80,
        "configuration_procedure": 100,
        "cli_meaning": 50,
        "show_command_meaning": 50,
    }.get(intent)


def is_syntax_intent(intent: str) -> bool:
    return intent in {"cli_syntax", "show_command_syntax"}


def is_meaning_intent(intent: str) -> bool:
    return intent in {"cli_meaning", "show_command_meaning"}


def words(text: str) -> List[str]:
    return [token for token in re.findall(r"[A-Za-z0-9_<>\-]+", text.casefold()) if token not in STOP_WORDS]


def source_supports_target(target: str, excerpt: str, intent: str, row: Mapping[str, Any], question: str) -> bool:
    if not target:
        return False
    if TEXT_NOISE_RE.search(target) or TEXT_NOISE_RE.search(excerpt):
        return False
    if BROKEN_SPACING_RE.search(target):
        return False
    if is_syntax_intent(intent):
        command = command_value(row, question, excerpt)
        if not command:
            return False
        if target.startswith("-"):
            return False
        if MULTI_COMMAND_BULLET_RE.search(target):
            return False
        if target.casefold().startswith("no "):
            return False
        if command.casefold() not in excerpt.casefold():
            return False
        return True
    if intent == "event_log_meaning":
        if "<log>" in target or re.search(r"(?i)^severity:\s*<log>", target):
            return False
        if re.search(r"(?i)\bevent\s+id\b", target) and len(words(target)) <= 4:
            return False
        if not re.search(r"(?i)\bseverity\b", target):
            return False
        return True
    limit = intent_limits(intent)
    if limit and len(words(target)) > limit:
        return False
    target_words = [word for word in words(target) if len(word) > 2]
    excerpt_words = set(words(excerpt))
    overlap = sum(1 for word in target_words if word in excerpt_words)
    if not overlap and intent not in {"product_generic"}:
        return False
    return True


def validate_record(
    intent: str,
    question: str,
    target_value: str,
    slots: Mapping[str, str],
    row: Mapping[str, Any],
) -> Optional[str]:
    q = collapse(question)
    t = collapse(target_value)
    if not q:
        return "empty_input_text"
    if not t:
        return "empty_target_value"
    if is_syntax_intent(intent):
        if not slots.get("command"):
            return "missing_command"
        if t.startswith("-"):
            return "syntax_bullet_rows_moved_to_review"
        if MULTI_COMMAND_BULLET_RE.search(t):
            return "syntax_bullet_rows_moved_to_review"
        if t.casefold().startswith("no "):
            return "no_form_syntax_rows_moved_to_review"
        if len(words(t)) > 25:
            return "syntax_long_explanation"
        if PLACEHOLDER_RE.search(t) is False and not re.search(r"(?i)\b[a-z0-9]+(?:\s+\{[^}]+\}|\s+\[[^]]+\])", t) and " " not in t:
            return "syntax_incomplete"
    if is_meaning_intent(intent):
        if len(words(t)) > 50:
            return "long_target_rows_moved_to_review"
        if re.search(r"(?i)^\s*(?:show|access-list|interface|vlan|no)\b", t) and not re.search(r"(?i)\b(command|enables|copies|displays|shows|configures|allows|means)\b", t):
            return "meaning_is_only_syntax"
    if intent == "configuration_procedure" and len(words(t)) > 100:
        return "long_target_rows_moved_to_review"
    if intent == "concept_explanation" and len(words(t)) > 80:
        return "long_target_rows_moved_to_review"
    if intent == "event_log_meaning":
        if not slots.get("event_id"):
            return "missing_event_id"
        if "<log>" in t:
            return "event_template_rows_moved_to_review"
        if re.search(r"(?i)^severity:\s*<log>", t):
            return "event_template_rows_moved_to_review"
        if re.fullmatch(r"(?i)event id[:\s]*\d+", t):
            return "event_template_rows_moved_to_review"
        if len(words(t)) > 60:
            return "long_target_rows_moved_to_review"
    if TEXT_NOISE_RE.search(t) or TEXT_NOISE_RE.search(q):
        return "generic_targets_moved_to_review"
    if BROKEN_SPACING_RE.search(t):
        return "broken_spacing_artifact"
    if intent in {"product_caveat", "product_requirement", "product_limitation", "product_generic"} and len(words(t)) > 80:
        return "long_target_rows_moved_to_review"
    if intent in {"product_caveat", "product_requirement", "product_limitation", "product_generic"} and re.search(
        r"(?i)\bsee the guide\b|\bdocumented in this guide\b|\bpublic\b",
        t,
    ):
        return "generic_targets_moved_to_review"
    return None


def load_jsonl(path: Path) -> Iterator[Tuple[int, Dict[str, Any]]]:
    with path.open("r", encoding="utf-8-sig") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            row = json.loads(line)
            if not isinstance(row, dict):
                raise ValueError(f"Expected object row in {path}:{line_number}")
            yield line_number, row


def find_input_files(inputs: Sequence[Path], max_files: Optional[int] = None) -> List[Path]:
    discovered: List[Path] = []
    seen: set[Path] = set()
    for path in inputs:
        if path.is_file():
            if path.name == "train_chat.jsonl" and path not in seen:
                discovered.append(path)
                seen.add(path)
            continue
        if not path.exists():
            raise FileNotFoundError(path)
        for candidate in path.rglob("train_chat.jsonl"):
            if any(part.lower() in {".venv", "__pycache__", "logs", "outputs"} for part in candidate.parts):
                continue
            if candidate not in seen:
                discovered.append(candidate)
                seen.add(candidate)
    discovered = sorted(discovered)
    if max_files is not None:
        discovered = discovered[:max_files]
    return discovered


def write_jsonl(path: Path, rows: Iterable[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def call_ollama(prompt: str, model: str, timeout_s: int = 180) -> Optional[Dict[str, Any]]:
    try:
        proc = subprocess.run(
            ["ollama", "run", model],
            input=prompt,
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=timeout_s,
            check=False,
        )
    except FileNotFoundError:
        return None
    if proc.returncode != 0:
        return None
    text = (proc.stdout or "").strip()
    if not text:
        return None
    match = re.search(r"\{.*\}", text, re.S)
    if not match:
        return None
    try:
        data = json.loads(match.group(0))
    except json.JSONDecodeError:
        return None
    return data if isinstance(data, dict) else None


def maybe_format_with_ollama(
    row: Mapping[str, Any],
    source_excerpt: str,
    target_value: str,
    intent: str,
    model: str,
    fallback_model: str,
) -> Tuple[str, bool, Optional[str]]:
    row_json = json.dumps(row, ensure_ascii=False, separators=(",", ":"))
    prompt = (
        "You are formatting HPE Aruba AOS-CX product-documentation LSTM training data.\n\n"
        "Do not add facts.\n"
        "Do not invent commands.\n"
        "Do not invent CLI syntax.\n"
        "Do not invent parameters.\n"
        "Do not change placeholders such as <INTERVAL>, <VRF-NAME>, <ACL-NAME>, <ringid>, <id>.\n"
        "Only clean formatting, grammar, and extraction noise.\n"
        "Return only valid JSON.\n\n"
        f"Input row:\n{row_json}\n\n"
        f"Source markdown excerpt:\n{source_excerpt}\n\n"
        "Required output:\n"
        '{\n  "fixed_target_value": "...",\n  "changed_facts": false,\n  "needs_review": false,\n  "reason": "..."\n}\n\n'
        "Rules:\n"
        "- For cli_syntax/show_command_syntax, fixed_target_value must be only exact syntax.\n"
        "- For cli_meaning/show_command_meaning, fixed_target_value must explain command purpose, not just syntax.\n"
        "- For event_log_meaning, fixed_target_value must contain clean severity/message information.\n"
        "- Remove page labels, page numbers, Public, NOTE noise, broken spacing, and table fragments.\n"
        "- If source is unclear, set needs_review=true.\n"
    )
    parsed = call_ollama(prompt, model=model)
    if parsed is None and fallback_model and fallback_model != model:
        parsed = call_ollama(prompt, model=fallback_model)
    if not parsed:
        return target_value, False, "ollama_unavailable_or_invalid"
    fixed = collapse(parsed.get("fixed_target_value"))
    changed_facts = bool(parsed.get("changed_facts", False))
    needs_review = bool(parsed.get("needs_review", False))
    reason = collapse(parsed.get("reason"))
    if changed_facts or needs_review or not fixed:
        return target_value, False, reason or "ollama_rejected"
    if fixed == collapse(target_value):
        return target_value, False, None
    if not source_supports_target(fixed, source_excerpt, intent, row, extract_qa(row)[0]):
        return target_value, False, "ollama_changed_facts"
    return fixed, True, None


def build_review_row(
    input_text: str,
    intent: str,
    slots: Mapping[str, str],
    target_value: str,
    reason: str,
    row: Mapping[str, Any],
    markdown_file: Optional[Path],
    matched_section: Optional[str],
    ollama_used: bool,
) -> Dict[str, Any]:
    return {
        "input_text": input_text,
        "intent": intent,
        "slots": dict(slots),
        "target_value": target_value,
        "review_reason": reason,
        "source_file": collapse(row.get("source_file")),
        "document_title": collapse(row.get("document_title")),
        "section": collapse(row.get("section")),
        "matched_markdown_file": str(markdown_file) if markdown_file else "",
        "matched_section": matched_section or "",
        "ollama_used": bool(ollama_used),
        "status": "needs_markdown_repair",
    }


def process_file(
    path: Path,
    markdown_roots: Sequence[Path],
    use_ollama: bool,
    ollama_model: str,
    fallback_model: str,
    max_rows: Optional[int] = None,
) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]], Dict[str, Any], Dict[str, int]]:
    dataset_rows: List[Dict[str, Any]] = []
    review_rows: List[Dict[str, Any]] = []
    rows_by_intent: Counter[str] = Counter()
    review_reasons: Counter[str] = Counter()
    noise_counts: Counter[str] = Counter()
    seen_exact: set[str] = set()
    seen_input_text: Dict[str, str] = {}

    counts = Counter(
        {
            "rows_scanned": 0,
            "rows_written": 0,
            "review_rows": 0,
            "rows_moved_to_review_not_deleted": 0,
            "duplicates_removed_from_final_only": 0,
            "rows_fixed_deterministically": 0,
            "rows_fixed_from_markdown": 0,
            "rows_formatted_by_ollama": 0,
            "ollama_rejected_rows": 0,
            "markdown_matched_rows": 0,
            "markdown_missing_rows": 0,
            "invalid_jsonl_lines": 0,
            "empty_input_text": 0,
            "empty_target_value": 0,
            "generic_targets_moved_to_review": 0,
            "syntax_bullet_rows_moved_to_review": 0,
            "no_form_syntax_rows_moved_to_review": 0,
            "event_template_rows_moved_to_review": 0,
            "long_target_rows_moved_to_review": 0,
        }
    )

    print(f"[INPUT] reading file {path}")
    for line_number, row in load_jsonl(path):
        if max_rows is not None and counts["rows_scanned"] >= max_rows:
            break
        counts["rows_scanned"] += 1
        print(f"[ROW] processing row number {line_number}")

        question, answer = extract_qa(row)
        if source_domain(row) != "product_docs":
            reason = "unsupported_source_domain"
            review_rows.append(
                build_review_row("", "", {}, "", reason, row, None, None, False)
            )
            counts["review_rows"] += 1
            counts["rows_moved_to_review_not_deleted"] += 1
            review_reasons[reason] += 1
            print("[REVIEW] noisy row moved to review, not deleted")
            continue

        intent = intent_from_row(row, question, answer)
        if intent not in SUPPORTED_PRODUCT_INTENTS:
            intent = "product_generic"
        print(f"[INTENT] detected intent {intent}")

        slots = build_slots(intent, row, question, answer)
        print(f"[SLOTS] extracted slots {json.dumps(slots, ensure_ascii=False)}")

        input_text = build_input_text(intent, row, question, answer)
        print(f"[CHECK] validating row")

        markdown_file = find_markdown_file(row, markdown_roots)
        excerpt_text = ""
        matched_section = None
        if markdown_file:
            print("[MD] matching markdown file")
            lines = load_markdown_lines(str(markdown_file))
            match_idx, matched_candidate = match_markdown_section(lines, row, question, answer)
            if match_idx is not None:
                counts["markdown_matched_rows"] += 1
                matched_section = matched_candidate or collapse(row.get("section"))
                print("[MD] matched section")
                excerpt_lines = extract_window(lines, match_idx)
                excerpt_text = "\n".join(excerpt_lines)
            else:
                counts["markdown_missing_rows"] += 1
                reason = "markdown_section_not_matched"
                review_rows.append(
                    build_review_row(input_text, intent, slots, "", reason, row, markdown_file, None, False)
                )
                counts["review_rows"] += 1
                counts["rows_moved_to_review_not_deleted"] += 1
                review_reasons[reason] += 1
                print("[REVIEW] noisy row moved to review, not deleted")
                continue
        else:
            counts["markdown_missing_rows"] += 1
            reason = "markdown_file_not_found"
            review_rows.append(
                build_review_row(input_text, intent, slots, "", reason, row, None, None, False)
            )
            counts["review_rows"] += 1
            counts["rows_moved_to_review_not_deleted"] += 1
            review_reasons[reason] += 1
            print("[REVIEW] noisy row moved to review, not deleted")
            continue

        raw_target = answer
        target_value, noise_applied = clean_target_value(intent, raw_target)
        if noise_applied:
            for key, value in noise_applied.items():
                noise_counts[key] += value
        if target_value != collapse(raw_target):
            counts["rows_fixed_deterministically"] += 1
            print("[FIX] deterministic fix applied")

        if source_supports_target(target_value, excerpt_text, intent, row, question):
            pass
        else:
            repaired = repair_target_from_markdown(intent, excerpt_text.splitlines(), row, question, raw_target)
            if repaired:
                target_value = collapse(repaired)
                counts["rows_fixed_from_markdown"] += 1
                print("[REPAIR] repaired target from markdown")
            else:
                reason = "markdown_repair_failed"
                review_rows.append(
                    build_review_row(input_text, intent, slots, target_value, reason, row, markdown_file, matched_section, False)
                )
                counts["review_rows"] += 1
                counts["rows_moved_to_review_not_deleted"] += 1
                review_reasons[reason] += 1
                print("[REVIEW] noisy row moved to review, not deleted")
                continue

        if use_ollama and excerpt_text and target_value:
            print("[OLLAMA] formatting only")
            formatted, changed, ollama_reason = maybe_format_with_ollama(
                row,
                excerpt_text,
                target_value,
                intent,
                model=ollama_model,
                fallback_model=fallback_model,
            )
            if changed:
                target_value = formatted
                counts["rows_formatted_by_ollama"] += 1
                print("[OLLAMA] accepted formatting")
            elif ollama_reason:
                counts["ollama_rejected_rows"] += 1
                print("[OLLAMA] rejected because facts changed")

        review_reason = validate_record(intent, input_text, target_value, slots, row)
        if review_reason:
            review_rows.append(
                build_review_row(
                    input_text,
                    intent,
                    slots,
                    target_value,
                    review_reason,
                    row,
                    markdown_file,
                    matched_section,
                    bool(use_ollama and counts["rows_formatted_by_ollama"]),
                )
            )
            counts["review_rows"] += 1
            counts["rows_moved_to_review_not_deleted"] += 1
            review_reasons[review_reason] += 1
            if review_reason == "generic_targets_moved_to_review":
                counts["generic_targets_moved_to_review"] += 1
            elif review_reason == "syntax_bullet_rows_moved_to_review":
                counts["syntax_bullet_rows_moved_to_review"] += 1
            elif review_reason == "no_form_syntax_rows_moved_to_review":
                counts["no_form_syntax_rows_moved_to_review"] += 1
            elif review_reason == "event_template_rows_moved_to_review":
                counts["event_template_rows_moved_to_review"] += 1
            elif review_reason == "long_target_rows_moved_to_review":
                counts["long_target_rows_moved_to_review"] += 1
            print("[REVIEW] noisy row moved to review, not deleted")
            continue

        record = {
            "input_text": input_text,
            "intent": intent,
            "slots": slots,
            "target_value": target_value,
        }
        dedupe_key = json.dumps(record, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
        if dedupe_key in seen_exact:
            counts["duplicates_removed_from_final_only"] += 1
            continue

        previous_target = seen_input_text.get(input_text)
        if previous_target is not None and previous_target != target_value:
            reason = "same_input_text_different_target_value"
            review_rows.append(
                build_review_row(input_text, intent, slots, target_value, reason, row, markdown_file, matched_section, False)
            )
            counts["review_rows"] += 1
            counts["rows_moved_to_review_not_deleted"] += 1
            review_reasons[reason] += 1
            print("[REVIEW] noisy row moved to review, not deleted")
            continue

        seen_exact.add(dedupe_key)
        seen_input_text[input_text] = target_value
        dataset_rows.append(record)
        rows_by_intent[intent] += 1
        counts["rows_written"] += 1
        print("[WRITE] clean row written to final dataset")

    report = {
        "rows_scanned": counts["rows_scanned"],
        "rows_written": counts["rows_written"],
        "review_rows": counts["review_rows"],
        "rows_moved_to_review_not_deleted": counts["rows_moved_to_review_not_deleted"],
        "duplicates_removed_from_final_only": counts["duplicates_removed_from_final_only"],
        "rows_fixed_deterministically": counts["rows_fixed_deterministically"],
        "rows_fixed_from_markdown": counts["rows_fixed_from_markdown"],
        "rows_formatted_by_ollama": counts["rows_formatted_by_ollama"],
        "ollama_rejected_rows": counts["ollama_rejected_rows"],
        "markdown_matched_rows": counts["markdown_matched_rows"],
        "markdown_missing_rows": counts["markdown_missing_rows"],
        "rows_by_intent": dict(sorted(rows_by_intent.items())),
        "review_reasons": dict(sorted(review_reasons.items())),
        "noise_removed_counts": dict(sorted(noise_counts.items())),
        "invalid_jsonl_lines": counts["invalid_jsonl_lines"],
        "empty_input_text": counts["empty_input_text"],
        "empty_target_value": counts["empty_target_value"],
        "generic_targets_moved_to_review": counts["generic_targets_moved_to_review"],
        "syntax_bullet_rows_moved_to_review": counts["syntax_bullet_rows_moved_to_review"],
        "no_form_syntax_rows_moved_to_review": counts["no_form_syntax_rows_moved_to_review"],
        "event_template_rows_moved_to_review": counts["event_template_rows_moved_to_review"],
        "long_target_rows_moved_to_review": counts["long_target_rows_moved_to_review"],
    }
    print(f"[QUALITY] final checks complete ({counts['rows_written']} clean rows)")
    return dataset_rows, review_rows, report, dict(counts)


def write_samples(path: Path, dataset_rows: Sequence[Mapping[str, Any]], review_rows: Sequence[Mapping[str, Any]], report: Mapping[str, Any]) -> None:
    lines = ["# Product-doc conversion samples", ""]
    lines.append("## Report")
    lines.append("")
    for key in (
        "rows_scanned",
        "rows_written",
        "review_rows",
        "rows_fixed_deterministically",
        "rows_fixed_from_markdown",
        "rows_formatted_by_ollama",
        "markdown_matched_rows",
        "markdown_missing_rows",
    ):
        lines.append(f"- {key}: {report.get(key, 0)}")
    lines.append("")
    lines.append("## Final Samples")
    lines.append("")
    for row in list(dataset_rows)[:10]:
        lines.append(f"- {json.dumps(row, ensure_ascii=False)}")
    lines.append("")
    lines.append("## Review Samples")
    lines.append("")
    for row in list(review_rows)[:10]:
        lines.append(f"- {json.dumps(row, ensure_ascii=False)}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


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
        "--markdown-root",
        dest="markdown_roots",
        action="append",
        type=Path,
        default=None,
        help="Markdown source root. May be supplied multiple times.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=data_root / "lstm_conversion" / "product_lstm_dataset_final.jsonl",
        help="Output JSONL file for the clean dataset rows.",
    )
    parser.add_argument(
        "--review-output",
        type=Path,
        default=data_root / "lstm_conversion" / "product_lstm_review_final.jsonl",
        help="Output JSONL file for review rows.",
    )
    parser.add_argument(
        "--report-output",
        type=Path,
        default=data_root / "lstm_conversion" / "product_lstm_report_final.json",
        help="Output JSON file for the conversion report.",
    )
    parser.add_argument(
        "--samples-output",
        type=Path,
        default=data_root / "lstm_conversion" / "product_lstm_samples_final.md",
        help="Output markdown file with representative samples.",
    )
    parser.add_argument("--max-files", type=int, default=None, help="Limit the number of input files processed.")
    parser.add_argument("--max-rows", type=int, default=None, help="Limit the number of rows processed per file.")
    parser.add_argument("--use-ollama", action="store_true", help="Enable Ollama formatting after markdown repair.")
    parser.add_argument(
        "--ollama-model",
        type=str,
        default="qwen2.5:7b-instruct",
        help="Primary Ollama model for formatting.",
    )
    parser.add_argument(
        "--ollama-fallback-model",
        type=str,
        default="qwen2.5-coder:7b",
        help="Fallback Ollama model if the primary model is unavailable.",
    )
    parser.add_argument("--force", action="store_true", help="Overwrite existing outputs.")
    args = parser.parse_args(argv)
    if not args.inputs:
        args.inputs = [data_root / "full_product_docs"]
    if not args.markdown_roots:
        args.markdown_roots = [data_root / "markitdown_cli_output(product)", data_root / "markitdown_cli_output"]
    return args


def main(argv: Optional[Sequence[str]] = None) -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

    print("[START] product-doc LSTM final conversion")
    args = parse_args(argv)
    input_files = find_input_files(args.inputs, max_files=args.max_files)
    if not input_files:
        raise FileNotFoundError("No train_chat.jsonl files found")

    output_paths = [args.output, args.review_output, args.report_output, args.samples_output]
    if not args.force:
        for path in output_paths:
            if path.exists():
                raise FileExistsError(f"Refusing to overwrite {path}; pass --force")

    dataset_rows: List[Dict[str, Any]] = []
    review_rows: List[Dict[str, Any]] = []
    combined_report: Dict[str, Any] = {}
    aggregate_counts: Counter[str] = Counter()
    aggregate_intents: Counter[str] = Counter()
    aggregate_review_reasons: Counter[str] = Counter()
    aggregate_noise: Counter[str] = Counter()

    for input_file in input_files:
        print("[INPUT] reading product docs")
        rows, reviews, report, counts = process_file(
            input_file,
            markdown_roots=args.markdown_roots,
            use_ollama=args.use_ollama,
            ollama_model=args.ollama_model,
            fallback_model=args.ollama_fallback_model,
            max_rows=args.max_rows,
        )
        dataset_rows.extend(rows)
        review_rows.extend(reviews)
        combined_report["rows_scanned"] = combined_report.get("rows_scanned", 0) + report["rows_scanned"]
        combined_report["rows_written"] = combined_report.get("rows_written", 0) + report["rows_written"]
        combined_report["review_rows"] = combined_report.get("review_rows", 0) + report["review_rows"]
        combined_report["rows_moved_to_review_not_deleted"] = combined_report.get("rows_moved_to_review_not_deleted", 0) + report[
            "rows_moved_to_review_not_deleted"
        ]
        combined_report["duplicates_removed_from_final_only"] = combined_report.get("duplicates_removed_from_final_only", 0) + report[
            "duplicates_removed_from_final_only"
        ]
        combined_report["rows_fixed_deterministically"] = combined_report.get("rows_fixed_deterministically", 0) + report[
            "rows_fixed_deterministically"
        ]
        combined_report["rows_fixed_from_markdown"] = combined_report.get("rows_fixed_from_markdown", 0) + report[
            "rows_fixed_from_markdown"
        ]
        combined_report["rows_formatted_by_ollama"] = combined_report.get("rows_formatted_by_ollama", 0) + report[
            "rows_formatted_by_ollama"
        ]
        combined_report["ollama_rejected_rows"] = combined_report.get("ollama_rejected_rows", 0) + report["ollama_rejected_rows"]
        combined_report["markdown_matched_rows"] = combined_report.get("markdown_matched_rows", 0) + report["markdown_matched_rows"]
        combined_report["markdown_missing_rows"] = combined_report.get("markdown_missing_rows", 0) + report["markdown_missing_rows"]
        combined_report["invalid_jsonl_lines"] = combined_report.get("invalid_jsonl_lines", 0) + report["invalid_jsonl_lines"]
        combined_report["empty_input_text"] = combined_report.get("empty_input_text", 0) + report["empty_input_text"]
        combined_report["empty_target_value"] = combined_report.get("empty_target_value", 0) + report["empty_target_value"]
        combined_report["generic_targets_moved_to_review"] = combined_report.get("generic_targets_moved_to_review", 0) + report[
            "generic_targets_moved_to_review"
        ]
        combined_report["syntax_bullet_rows_moved_to_review"] = combined_report.get("syntax_bullet_rows_moved_to_review", 0) + report[
            "syntax_bullet_rows_moved_to_review"
        ]
        combined_report["no_form_syntax_rows_moved_to_review"] = combined_report.get("no_form_syntax_rows_moved_to_review", 0) + report[
            "no_form_syntax_rows_moved_to_review"
        ]
        combined_report["event_template_rows_moved_to_review"] = combined_report.get("event_template_rows_moved_to_review", 0) + report[
            "event_template_rows_moved_to_review"
        ]
        combined_report["long_target_rows_moved_to_review"] = combined_report.get("long_target_rows_moved_to_review", 0) + report[
            "long_target_rows_moved_to_review"
        ]
        aggregate_intents.update(report["rows_by_intent"])
        aggregate_review_reasons.update(report["review_reasons"])
        aggregate_noise.update(report["noise_removed_counts"])

    unique_dataset_rows: List[Dict[str, Any]] = []
    seen_dataset: set[str] = set()
    for row in dataset_rows:
        key = json.dumps(row, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
        if key in seen_dataset:
            continue
        seen_dataset.add(key)
        unique_dataset_rows.append(row)

    combined_report["rows_by_intent"] = dict(sorted(aggregate_intents.items()))
    combined_report["review_reasons"] = dict(sorted(aggregate_review_reasons.items()))
    combined_report["noise_removed_counts"] = dict(sorted(aggregate_noise.items()))

    write_jsonl(args.output, unique_dataset_rows)
    print("[OUTPUT] final dataset saved")
    write_jsonl(args.review_output, review_rows)
    print("[OUTPUT] review saved")
    write_json(args.report_output, combined_report)
    print("[OUTPUT] report saved")
    write_samples(args.samples_output, unique_dataset_rows, review_rows, combined_report)
    print("[QUALITY] final checks complete")
    print(
        json.dumps(
            {
                **combined_report,
                "dataset_sha256": sha256_file(args.output),
                "review_sha256": sha256_file(args.review_output),
            },
            indent=2,
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
