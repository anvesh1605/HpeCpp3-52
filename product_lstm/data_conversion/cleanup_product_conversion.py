#!/usr/bin/env python3
"""Cleanup pass for converted product-documentation LSTM rows.

This script consumes the current converted product rows, cleans extraction
artifacts, filters weak rows into review, balances event-log rows, and writes a
final JSONL dataset plus review/report artifacts.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, Iterator, List, Mapping, Optional, Sequence, Tuple


SCRIPT_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPT_DIR.parent

WHITESPACE_RE = re.compile(r"\s+")
PAGE_ONLY_RE = re.compile(r"^\s*\d+\s*$")
PUBLIC_RE = re.compile(r"(?i)\bpublic\b")
PAGE_FRAGMENT_RE = re.compile(r"(?i)\b(?:page|pp\.?|p\.)\s*\d+\b")
TABLE_HEADER_RE = re.compile(r"(?i)^\s*\|\s*(?:parameter|description|value|name|field)\s*\|\s*(?:parameter|description|value|name|field)\s*\|?\s*$")
BROKEN_SPACING_RE = re.compile(r"(?i)\b(?:Ran ge|wit h|fo r|entri es|re se t|com man d|Bidrectional|un responsive|alloted t ime)\b")
EVENT_TEMPLATE_RE = re.compile(
    r"(?i)(?:\bthe event log reference documents event id\b|\bdescription:\s*event id\b|\bseverity:\s*information(?:\s+information)+\b)"
)
GENERIC_ANSWER_RE = re.compile(
    r"(?i)^(?:"
    r"the command is documented in this guide\.?|"
    r"this guide documents the command\.?|"
    r"refer to the guide\.?|"
    r"see the documentation\.?|"
    r"see the guide\.?|"
    r"documented in this guide\.?"
    r")$"
)
GENERIC_ANSWER_CONTAINS_RE = re.compile(
    r"(?i)\b(documented in this guide|this guide documents the command|refer to the guide|see the documentation|see the guide)\b"
)
GENERIC_TEMPLATE_RE = re.compile(r"(?i)\b(?:tbd|todo|placeholder|n/?a|none|null|unknown)\b")
SYNTAX_SIGNAL_RE = re.compile(
    r"(?i)(?:\bwhat\s+is\s+the\s+(?:exact\s+)?syntax\b|\bexact\s+syntax\b|\bsyntax\s+of\b|\bcommand\s+syntax\b|\bgive\s+(?:me\s+)?the\s+(?:exact\s+)?syntax\b|\bshow\s+the\s+syntax\b)"
)
VERSION_RE = re.compile(r"\b\d{1,2}\.\d{1,2}(?:\.\d{3,5})?\b")
SPLIT_CAMEL_RE = re.compile(r"(?<=[a-z])(?=[A-Z])")
MULTI_BULLET_RE = re.compile(r"(?m)^\s*[-*•]\s+\S+")
COMMAND_RE = re.compile(r"(?i)\b(show|clear|configure|copy|crypto|debug|erase|interface|ip|ipv6|no|policy|reload|router|vlan|bfd|erps|ping|arp|access-list|apply)\b")
EVENT_ID_RE = re.compile(r"(?i)\bevent\s+id\s*[:#-]?\s*(\d{3,8})\b")
COMMAND_IN_QUESTION_RE = re.compile(
    r"(?i)^for\s+.+?,\s*what does the (.+?) command do\?$|^for\s+.+?,\s*what is the syntax of the (.+?) command\?$"
)

COMMON_ARTIFACT_FIXES = {
    "pingsnetworkhosts": "pings network hosts",
    "currentworkingdirectory": "current working directory",
    "thenumberofpackets": "the number of packets",
    "currentworking": "current working",
    "un responsive": "unresponsive",
    "Bidrectional": "Bidirectional",
    "alloted t ime": "allotted time",
    "IPv 4": "IPv4",
    "IPv 6": "IPv6",
    "IPV 4": "IPv4",
    "IPV 6": "IPv6",
    "Co PP": "CoPP",
    "LL DP": "LLDP",
    "VS X": "VSX",
    "SN MP": "SNMP",
    "TC AM": "TCAM",
    "VR F": "VRF",
    "L 3": "L3",
    "O ID": "OID",
}


def collapse(value: Any) -> str:
    text = str(value or "").replace("\r\n", "\n").replace("\r", "\n").replace("\f", " ")
    text = text.replace("\u00a0", " ").replace("\u2022", "-").replace("�", "")
    text = WHITESPACE_RE.sub(" ", text).strip()
    return text


def normalize(value: Any) -> str:
    return collapse(value).casefold()


def display_version(value: Any) -> str:
    return collapse(value).replace("_", ".")


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def short_hash(*parts: Any, size: int = 10) -> str:
    seed = "\n".join(collapse(part) for part in parts)
    return sha256_text(seed)[:size]


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


def word_count(text: str) -> int:
    return len(re.findall(r"[A-Za-z0-9_<>\-]+", collapse(text)))


def first_message(row: Mapping[str, Any], role: str) -> str:
    for message in row.get("messages") or []:
        if isinstance(message, Mapping) and normalize(message.get("role")) == role:
            return collapse(message.get("content"))
    return ""


def extract_qa(row: Mapping[str, Any]) -> Tuple[str, str]:
    question = collapse(row.get("input_text")) or first_message(row, "user") or collapse(row.get("question"))
    answer = collapse(row.get("target_value")) or first_message(row, "assistant") or collapse(row.get("answer"))
    return question, answer


def get_slots(row: Mapping[str, Any]) -> Dict[str, Any]:
    slots = row.get("slots")
    return dict(slots) if isinstance(slots, Mapping) else {}


def get_switch_version(row: Mapping[str, Any]) -> Tuple[str, str]:
    slots = get_slots(row)
    switch = collapse(slots.get("switch") or row.get("switch"))
    version = display_version(slots.get("version") or row.get("version"))
    return switch, version


def get_command(row: Mapping[str, Any]) -> str:
    slots = get_slots(row)
    command = collapse(slots.get("command") or row.get("command") or row.get("command_name"))
    if command:
        return command
    question, answer = extract_qa(row)
    text = f"{question} {answer}"
    patterns = [
        r"(?i)\bwhat is the syntax of the (?P<command>.+?) command\b",
        r"(?i)\bwhat is the syntax of (?P<command>.+?) command\b",
        r"(?i)\bwhat does the (?P<command>.+?) command do\b",
        r"(?i)\bwhat does the (?P<command>.+?) do\b",
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return collapse(match.group("command"))
    return ""


def get_topic(row: Mapping[str, Any]) -> str:
    slots = get_slots(row)
    for key in ("topic", "feature", "object_name", "section"):
        value = collapse(slots.get(key) or row.get(key))
        if value:
            return value
    question, answer = extract_qa(row)
    match = re.search(r"(?i)\babout\s+(.+?)(?:\?|$)", f"{question} {answer}")
    if match:
        return collapse(match.group(1))
    return ""


def get_event_id(row: Mapping[str, Any]) -> str:
    slots = get_slots(row)
    value = collapse(slots.get("event_id") or row.get("event_id"))
    if value:
        return value
    question, answer = extract_qa(row)
    match = EVENT_ID_RE.search(f"{question} {answer}")
    return match.group(1) if match else ""


def split_sentences(text: str) -> List[str]:
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9])", collapse(text))
    return [part.strip() for part in parts if part.strip()]


def clean_pdf_artifacts(text: str) -> str:
    cleaned = collapse(text)
    if not cleaned:
        return ""
    cleaned = cleaned.replace("\u200b", "").replace("\u2060", "")
    cleaned = PUBLIC_RE.sub("", cleaned)
    cleaned = PAGE_FRAGMENT_RE.sub("", cleaned)
    cleaned = cleaned.replace("| Parameter | Description |", "")
    cleaned = cleaned.replace("| Parameter |", "")
    cleaned = cleaned.replace("| Description |", "")
    cleaned = re.sub(r"\s*\|\s*", " | ", cleaned)
    cleaned = re.sub(r"(?i)\bAOS-CX(?=\d)", "AOS-CX ", cleaned)
    cleaned = re.sub(r"(?i)(?<=\d)(?=AOS-CX)", " ", cleaned)
    cleaned = re.sub(r"(?<=\d)(?=[A-Z])", " ", cleaned)
    cleaned = SPLIT_CAMEL_RE.sub(" ", cleaned)
    for bad, good in COMMON_ARTIFACT_FIXES.items():
        cleaned = re.sub(re.escape(bad), good, cleaned, flags=re.I)
    cleaned = WHITESPACE_RE.sub(" ", cleaned).strip(" -|")
    return cleaned


def is_generic_answer(text: str) -> bool:
    value = collapse(text)
    if not value:
        return True
    if GENERIC_ANSWER_RE.match(value):
        return True
    if GENERIC_ANSWER_CONTAINS_RE.search(value) and word_count(value) <= 10:
        return True
    return False


def is_pdf_artifact_heavy(original: str, cleaned: str) -> bool:
    original_text = collapse(original)
    cleaned_text = collapse(cleaned)
    if not original_text:
        return False
    if TABLE_HEADER_RE.match(original_text):
        return True
    if "|" in original_text or "Public" in original_text or PAGE_FRAGMENT_RE.search(original_text):
        if cleaned_text != original_text:
            return True
    if re.search(r"(?i)\b[A-Z]{2,}-CX\d", original_text) or re.search(r"(?i)\b[a-z]{12,}\b", original_text):
        if cleaned_text and word_count(cleaned_text) <= 4:
            return True
    return False


def is_syntax_intent(intent: str) -> bool:
    return intent in {"cli_syntax", "show_command_syntax"}


def is_meaning_intent(intent: str) -> bool:
    return intent in {"cli_meaning", "show_command_meaning"}


def is_event_intent(intent: str) -> bool:
    return intent == "event_log_meaning"


def is_concept_intent(intent: str) -> bool:
    return intent == "concept_explanation"


def is_text_only_generic(text: str) -> bool:
    cleaned = clean_pdf_artifacts(text)
    return is_generic_answer(cleaned)


def looks_like_syntax_candidate(text: str, command: str) -> bool:
    value = collapse(text).rstrip(".")
    if not value:
        return False
    if is_generic_answer(value):
        return False
    if any(token in normalize(value) for token in ("documented in this guide", "refer to the guide", "see the documentation")):
        return False
    if word_count(value) > 25:
        return False
    if re.search(r"(?i)\b(command|does|doesn't|meaning|guide|documentation|documented)\b", value):
        return False
    if value.casefold().startswith("the syntax") or value.casefold().startswith("syntax"):
        return False
    if command and command.casefold() in value.casefold():
        return True
    if any(ch in value for ch in "<>[]{}") or value.casefold().startswith("no "):
        return True
    if re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9\-\s_<>{}\[\]|./]*", value):
        return True
    return False


def extract_syntax_candidates(text: str, command: str = "") -> List[str]:
    cleaned = clean_pdf_artifacts(text)
    cleaned = re.sub(r"(?is)^\s*(?:the\s+)?syntax(?:\s+of\s+the\s+command)?\s*(?:is|:)?\s*", "", cleaned).strip()
    if not cleaned:
        return []

    if command:
        matches = [match.start() for match in re.finditer(re.escape(command), cleaned, flags=re.I)]
        if len(matches) > 1 and matches[0] == 0:
            chunks: List[str] = []
            for index, start in enumerate(matches):
                end = matches[index + 1] if index + 1 < len(matches) else len(cleaned)
                chunk = collapse(cleaned[start:end]).rstrip(" .;")
                if chunk:
                    chunks.append(chunk)
            if len(chunks) > 1:
                cleaned = "\n".join(chunks)

    lines = [clean_pdf_artifacts(part) for part in re.split(r"[\r\n]+", cleaned)]
    candidates: List[str] = []
    for line in lines:
        if not line:
            continue
        if re.fullmatch(r"(?i)\s*[-*•]\s*", line):
            continue
        line = re.sub(r"(?i)^\s*[-*•]\s*", "", line).strip()
        if not line:
            continue
        if re.fullmatch(r".+\s-\s.+", line) and not re.search(r"[.?!]", line):
            pieces = [piece.strip() for piece in re.split(r"\s-\s", line) if piece.strip()]
            if len(pieces) > 1 and all(len(piece) <= 25 for piece in pieces):
                candidates.extend(pieces)
                continue
        if " | " in line and not re.search(r"[.?!]", line):
            pieces = [piece.strip() for piece in line.split(" | ") if piece.strip()]
            if len(pieces) > 1 and all(len(piece) <= 25 for piece in pieces):
                candidates.extend(pieces)
                continue
        candidates.append(line)

    deduped: List[str] = []
    seen: set[str] = set()
    command = command or get_command_from_text(cleaned)
    for candidate in candidates:
        key = normalize(candidate)
        if key in seen:
            continue
        if looks_like_syntax_candidate(candidate, command):
            seen.add(key)
            deduped.append(candidate.rstrip("."))
    return deduped


def get_command_from_text(text: str) -> str:
    match = COMMAND_IN_QUESTION_RE.search(text)
    if match:
        return collapse(match.group(1) or match.group(2) or "")
    return ""


def clean_syntax_value(row: Mapping[str, Any], target: str) -> str:
    command = get_command(row)
    cleaned = clean_pdf_artifacts(target)
    if not cleaned:
        return ""
    cleaned = re.sub(r"(?is)^\s*(?:the\s+)?syntax(?:\s+of\s+the\s+command)?\s*(?:is|:)?\s*", "", cleaned).strip()
    cleaned = re.sub(r"(?i)^\s*syntax\s*:\s*", "", cleaned).strip()
    cleaned = cleaned.replace(" - ", "\n")
    cleaned = WHITESPACE_RE.sub(" ", cleaned)

    candidates = extract_syntax_candidates(cleaned, command)
    if not candidates:
        candidates = extract_syntax_candidates(target, command)

    if candidates:
        return "\n".join(candidates)

    fallback = collapse(cleaned).rstrip(".")
    if looks_like_syntax_candidate(fallback, command):
        return fallback
    return ""


def extract_meaning_sentence(text: str, command: str) -> str:
    cleaned = clean_pdf_artifacts(text)
    cleaned = re.split(r"(?is)\bsyntax\s*:\s*", cleaned, maxsplit=1)[0].strip()
    sentences = split_sentences(cleaned)
    if not sentences:
        return ""
    prefix = f"the {command} command" if command else ""
    for sentence in sentences:
        value = sentence.strip()
        if not value:
            continue
        if is_generic_answer(value):
            continue
        if prefix and value.casefold().startswith(prefix.casefold()):
            return value.rstrip(".")
        if command and command.casefold() in value.casefold():
            return value.rstrip(".")
        if word_count(value) >= 4:
            return value.rstrip(".")
    return sentences[0].rstrip(".")


def extract_meaning_syntax(text: str) -> str:
    cleaned = clean_pdf_artifacts(text)
    match = re.search(r"(?is)\bsyntax\s*:\s*(.+)$", cleaned)
    if match:
        syntax = clean_syntax_value({}, match.group(1))
        if syntax:
            return syntax
    return ""


def clean_meaning_value(row: Mapping[str, Any], target: str) -> str:
    command = get_command(row)
    cleaned = clean_pdf_artifacts(target)
    cleaned = re.sub(r"(?i)\bthe event log reference documents event id \d+\.?\s*", "", cleaned)
    if is_generic_answer(cleaned):
        return ""

    syntax = extract_meaning_syntax(cleaned)
    cleaned = re.split(r"(?is)\bsyntax\s*:\s*", cleaned, maxsplit=1)[0].strip()
    meaning_sentence = extract_meaning_sentence(cleaned, command)
    if not meaning_sentence:
        return ""

    if command:
        prefix = f"The {command} command"
        if not meaning_sentence.casefold().startswith(prefix.casefold()):
            if meaning_sentence[:1].isupper():
                meaning_sentence = f"{prefix} {meaning_sentence[0].lower() + meaning_sentence[1:]}"
            else:
                meaning_sentence = f"{prefix} {meaning_sentence}"
    meaning_sentence = meaning_sentence.strip().rstrip(".")
    meaning_sentence = f"{meaning_sentence}."

    if syntax:
        return f"{meaning_sentence[:-1]} Syntax: {syntax.rstrip('.')}."
    return meaning_sentence


def select_key_points(sentences: Sequence[str], topic: str, max_points: int = 2) -> List[str]:
    points: List[str] = []
    topic_norm = normalize(topic)
    for sentence in sentences:
        value = collapse(sentence).rstrip(".")
        if not value or is_generic_answer(value):
            continue
        if topic_norm and normalize(value).startswith(topic_norm):
            continue
        if word_count(value) < 4:
            continue
        if re.search(r"(?i)\b(?:6200|6300|6400|8100|8325|8360|9300|10000)\b", value) and len(value.split()) > 15:
            continue
        if value not in points:
            points.append(value)
        if len(points) >= max_points:
            break
    return points


def clean_concept_value(row: Mapping[str, Any], target: str) -> str:
    topic = get_topic(row)
    cleaned = clean_pdf_artifacts(target)
    if is_generic_answer(cleaned):
        return ""
    sentences = split_sentences(cleaned)
    if not sentences:
        return ""

    definition = ""
    for sentence in sentences:
        value = collapse(sentence).rstrip(".")
        if not value or is_generic_answer(value):
            continue
        if topic and normalize(value).startswith(normalize(topic)):
            value = value[len(topic) :].lstrip(" :.-")
        definition = value.rstrip(".")
        break

    if not definition:
        return ""

    points = select_key_points(sentences[1:], topic, max_points=2)
    if points:
        return f"{topic}: {definition}. Key points: {'; '.join(points)}."
    return f"{topic}: {definition}."


def clean_event_value(row: Mapping[str, Any], target: str) -> str:
    event_id = get_event_id(row)
    cleaned = clean_pdf_artifacts(target)
    if is_generic_answer(cleaned):
        return ""
    cleaned = re.sub(r"(?i)\bthe event log reference documents event id \d+\.?\s*", "", cleaned)
    cleaned = re.sub(r"(?i)\bdescription:\s*event id:\s*\d+\.?\s*", "", cleaned)
    cleaned = re.sub(r"(?i)\bseverity:\s*(information|warning|error)(?:\s+\1)+\b", r"Severity: \1", cleaned)
    cleaned = re.sub(r"(?i)\bseverity:\s*<log>\b", "", cleaned)
    cleaned = WHITESPACE_RE.sub(" ", cleaned).strip(" -.")
    if not cleaned:
        return ""
    if event_id and re.fullmatch(rf"(?i)event id[:\s]*{re.escape(event_id)}\.?", cleaned):
        return ""
    if event_id and word_count(cleaned) == 0:
        return ""
    return cleaned


def clean_requirement_like_value(target: str) -> str:
    cleaned = clean_pdf_artifacts(target)
    if is_generic_answer(cleaned):
        return ""
    return cleaned


def clean_target_value(row: Mapping[str, Any]) -> Tuple[str, Dict[str, int]]:
    intent = collapse(row.get("intent"))
    target = collapse(row.get("target_value"))
    counts: Dict[str, int] = {}
    if not target:
        return "", counts

    cleaned = clean_pdf_artifacts(target)
    if cleaned != target:
        counts["pdf_artifact"] = counts.get("pdf_artifact", 0) + 1

    if is_syntax_intent(intent):
        cleaned = clean_syntax_value(row, cleaned)
    elif is_meaning_intent(intent):
        cleaned = clean_meaning_value(row, cleaned)
    elif is_event_intent(intent):
        cleaned = clean_event_value(row, cleaned)
    elif is_concept_intent(intent):
        cleaned = clean_concept_value(row, cleaned)
    else:
        cleaned = clean_requirement_like_value(cleaned)

    if is_syntax_intent(intent):
        lines = [WHITESPACE_RE.sub(" ", clean_pdf_artifacts(line)).strip(" -") for line in cleaned.splitlines()]
        cleaned = "\n".join(line for line in lines if line)
    else:
        cleaned = clean_pdf_artifacts(cleaned)
        cleaned = WHITESPACE_RE.sub(" ", cleaned).strip(" -")
    return cleaned, counts


def review_reason(row: Mapping[str, Any], cleaned_target: str) -> Optional[str]:
    intent = collapse(row.get("intent"))
    input_text = collapse(row.get("input_text"))
    slots = get_slots(row)
    command = collapse(slots.get("command"))
    event_id = collapse(slots.get("event_id"))
    target = collapse(cleaned_target)
    original = collapse(row.get("target_value"))

    if not input_text or not target:
        return "empty_fields"
    if is_text_only_generic(target) or is_text_only_generic(original):
        return "generic_answer"
    if GENERIC_TEMPLATE_RE.search(target):
        return "generic_answer"
    if any(marker in original for marker in ("| Parameter |", "| Description |", "AOS-CX10.", "Command-Line Interface Guide")) and word_count(target) <= 4:
        return "pdf_artifact"

    if is_syntax_intent(intent):
        if not command:
            return "bad_cli_syntax"
        if target.startswith("-") or MULTI_BULLET_RE.search(target):
            return "bad_cli_syntax"
        if target.casefold().startswith("no ") and "what is the syntax" in input_text.casefold():
            return "bad_cli_syntax"
        if word_count(target) > 25:
            return "too_long_target"
        if not looks_like_syntax_candidate(target, command) and "\n" not in target:
            return "bad_cli_syntax"
        return None

    if is_meaning_intent(intent):
        if word_count(target) < 4:
            return "too_short_target"
        if word_count(target) > 60:
            return "too_long_target"
        if re.search(r"(?i)^\s*(?:show|access-list|interface|vlan|no|ping|arp|bfd|erps)\b", target) and not re.search(
            r"(?i)\b(command|enables|copies|displays|shows|configures|allows|means|sets|removes)\b",
            target,
        ):
            return "bad_cli_syntax"
        return None

    if is_event_intent(intent):
        if not event_id:
            return "empty_fields"
        if word_count(target) < 5:
            return "event_log_repetitive"
        if EVENT_TEMPLATE_RE.search(target):
            return "event_log_repetitive"
        if re.fullmatch(rf"(?i)(?:description:\s*)?event id[:\s]*{re.escape(event_id)}\.?", target):
            return "event_log_repetitive"
        return None

    if is_concept_intent(intent):
        if word_count(target) < 4:
            return "too_short_target"
        if word_count(target) > 100:
            return "too_long_target"
        if GENERIC_ANSWER_CONTAINS_RE.search(target):
            return "generic_answer"
        return None

    if intent in {"configuration_procedure", "snmp_mib_info", "troubleshooting", "product_caveat", "product_requirement", "product_limitation", "product_generic"}:
        if word_count(target) < 3:
            return "too_short_target"
        if word_count(target) > 100:
            return "too_long_target"
        if GENERIC_ANSWER_CONTAINS_RE.search(target):
            return "generic_answer"
        if intent == "product_generic" and len(target.split()) <= 5:
            return "generic_answer"
        return None

    return None


def canonical_signature(row: Mapping[str, Any], cleaned_target: str) -> str:
    intent = collapse(row.get("intent"))
    slots = get_slots(row)
    command = collapse(slots.get("command"))
    topic = collapse(slots.get("topic") or slots.get("feature") or slots.get("object_name"))
    event_id = collapse(slots.get("event_id"))
    switch = collapse(slots.get("switch"))
    version = display_version(slots.get("version"))
    normalized = normalize(cleaned_target)
    normalized = VERSION_RE.sub("<version>", normalized)
    normalized = re.sub(r"\b\d{4,8}\b", "<num>", normalized)
    normalized = normalized.replace(switch.casefold(), "<switch>") if switch else normalized
    normalized = normalized.replace(version.casefold(), "<version>") if version else normalized
    key_bits = [intent, command, topic, event_id, normalized]
    return "||".join(collapse(bit) for bit in key_bits)


def exact_record_key(record: Mapping[str, Any]) -> str:
    return json.dumps(record, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def normalize_review_row(row: Mapping[str, Any], reason: str) -> Dict[str, Any]:
    review_row = dict(row)
    review_row["review_reason"] = reason
    if "target_value" not in review_row:
        review_row["target_value"] = collapse(row.get("target_value"))
    if "input_text" not in review_row:
        review_row["input_text"] = collapse(row.get("input_text"))
    if "intent" not in review_row:
        review_row["intent"] = collapse(row.get("intent"))
    if "slots" not in review_row or not isinstance(review_row["slots"], Mapping):
        review_row["slots"] = get_slots(row)
    return review_row


def make_review_row(row: Mapping[str, Any], reason: str, cleaned_target: str) -> Dict[str, Any]:
    slots = get_slots(row)
    review_row = {
        "input_text": collapse(row.get("input_text")),
        "intent": collapse(row.get("intent")),
        "slots": slots,
        "target_value": collapse(cleaned_target),
        "review_reason": reason,
    }
    for key in ("source_file", "document_title", "section", "matched_markdown_file", "matched_section", "status"):
        value = row.get(key)
        if value is not None and collapse(value):
            review_row[key] = collapse(value)
    return review_row


def sample_row(row: Mapping[str, Any]) -> Dict[str, Any]:
    slots = get_slots(row)
    return {
        "input_text": collapse(row.get("input_text")),
        "intent": collapse(row.get("intent")),
        "slots": slots,
        "target_value": collapse(row.get("target_value")),
    }


def sample_review_row(row: Mapping[str, Any]) -> Dict[str, Any]:
    slots = get_slots(row)
    return {
        "input_text": collapse(row.get("input_text")),
        "intent": collapse(row.get("intent")),
        "slots": slots,
        "target_value": collapse(row.get("target_value")),
        "review_reason": collapse(row.get("review_reason") or row.get("reason")),
    }


def process_dataset_rows(dataset_path: Path) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]], Dict[str, Any]]:
    clean_rows: List[Dict[str, Any]] = []
    review_rows: List[Dict[str, Any]] = []
    rows_by_intent: Counter[str] = Counter()
    review_reasons: Counter[str] = Counter()
    commands: Counter[str] = Counter()
    event_ids: Counter[str] = Counter()
    sample_clean_rows_per_intent: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    sample_review_rows: List[Dict[str, Any]] = []

    counts = Counter(
        {
            "rows_scanned": 0,
            "rows_written": 0,
            "rows_sent_to_review": 0,
            "duplicates_removed": 0,
            "invalid_jsonl_lines": 0,
        }
    )

    exact_seen: set[str] = set()
    signature_seen: set[str] = set()
    event_keep_count: Dict[Tuple[str, str], int] = defaultdict(int)
    event_keep_limit = 8

    print(f"[INPUT] reading file {dataset_path}")
    for line_number, row in load_jsonl(dataset_path):
        counts["rows_scanned"] += 1
        print(f"[ROW] processing row number {line_number}")

        input_text = collapse(row.get("input_text"))
        intent = collapse(row.get("intent"))
        slots = get_slots(row)

        if not input_text or not collapse(row.get("target_value")):
            cleaned_target = collapse(row.get("target_value"))
            reason = "empty_fields"
            review_row = make_review_row(row, reason, cleaned_target)
            review_rows.append(review_row)
            review_reasons[reason] += 1
            counts["rows_sent_to_review"] += 1
            print("[REVIEW] review row written")
            continue

        cleaned_target, clean_counts = clean_target_value(row)
        if clean_counts.get("pdf_artifact"):
            print("[FIX] pdf artifact cleaned")
        reason = review_reason(row, cleaned_target)

        if reason is None and is_event_intent(intent):
            switch, version = get_switch_version(row)
            group_key = (switch, version)
            score = 0
            if re.search(r"(?i)\bseverity\b", cleaned_target):
                score += 3
            if re.search(r"(?i)\bmessage\b|\bdescription\b", cleaned_target):
                score += 2
            if get_event_id(row):
                score += 1
            if word_count(cleaned_target) > 8:
                score += 1
            if EVENT_TEMPLATE_RE.search(cleaned_target):
                score -= 5
            if event_keep_count[group_key] >= event_keep_limit and score < 4:
                reason = "event_log_repetitive"
            else:
                event_keep_count[group_key] += 1

        if reason is not None:
            review_row = make_review_row(row, reason, cleaned_target)
            review_rows.append(review_row)
            review_reasons[reason] += 1
            counts["rows_sent_to_review"] += 1
            if reason == "duplicate":
                counts["duplicates_removed"] += 1
            print("[REVIEW] review row written")
            continue

        record = {
            "input_text": input_text,
            "intent": intent,
            "slots": slots,
            "target_value": cleaned_target,
        }

        exact_key = exact_record_key(record)
        if exact_key in exact_seen:
            review_row = make_review_row(row, "duplicate", cleaned_target)
            review_rows.append(review_row)
            review_reasons["duplicate"] += 1
            counts["duplicates_removed"] += 1
            counts["rows_sent_to_review"] += 1
            print("[REVIEW] review row written")
            continue

        signature = canonical_signature(row, cleaned_target)
        if signature in signature_seen:
            review_row = make_review_row(row, "duplicate", cleaned_target)
            review_rows.append(review_row)
            review_reasons["duplicate"] += 1
            counts["duplicates_removed"] += 1
            counts["rows_sent_to_review"] += 1
            print("[REVIEW] review row written")
            continue

        exact_seen.add(exact_key)
        signature_seen.add(signature)
        clean_rows.append(record)
        rows_by_intent[intent] += 1
        counts["rows_written"] += 1
        command = get_command(row)
        if command:
            commands[command] += 1
        event_id = get_event_id(row)
        if event_id:
            event_ids[event_id] += 1
        if len(sample_clean_rows_per_intent[intent]) < 3:
            sample_clean_rows_per_intent[intent].append(record)
        print("[WRITE] dataset row written")

    return clean_rows, review_rows, {
        "rows_scanned": counts["rows_scanned"],
        "rows_written": counts["rows_written"],
        "rows_sent_to_review": counts["rows_sent_to_review"],
        "duplicates_removed": counts["duplicates_removed"],
        "rows_by_intent": dict(sorted(rows_by_intent.items())),
        "review_reasons": dict(sorted(review_reasons.items())),
        "top_20_commands": commands.most_common(20),
        "top_20_event_ids": event_ids.most_common(20),
        "sample_clean_rows_per_intent": dict(sorted(sample_clean_rows_per_intent.items())),
    }


def process_review_rows(review_path: Optional[Path]) -> Tuple[List[Dict[str, Any]], Counter[str], List[Dict[str, Any]]]:
    rows: List[Dict[str, Any]] = []
    reasons: Counter[str] = Counter()
    samples: List[Dict[str, Any]] = []
    if review_path is None or not review_path.exists():
        return rows, reasons, samples

    print(f"[INPUT] reading file {review_path}")
    for line_number, row in load_jsonl(review_path):
        reason = collapse(row.get("review_reason") or row.get("reason")) or "existing_review"
        review_row = normalize_review_row(row, reason)
        rows.append(review_row)
        reasons[reason] += 1
        if len(samples) < 20:
            samples.append(
                {
                    "input_text": collapse(review_row.get("input_text")),
                    "intent": collapse(review_row.get("intent")),
                    "review_reason": reason,
                    "target_value": collapse(review_row.get("target_value")),
                }
            )
        print(f"[ROW] processing row number {line_number}")
        print("[REVIEW] existing review row carried over")
    return rows, reasons, samples


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    data_root = ROOT_DIR
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input-dataset",
        type=Path,
        default=data_root / "lstm_conversion" / "pilot_product_5" / "dataset.jsonl",
        help="Current converted product dataset JSONL.",
    )
    parser.add_argument(
        "--input-review",
        type=Path,
        default=data_root / "lstm_conversion" / "pilot_product_5" / "review.jsonl",
        help="Current converted product review JSONL.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=data_root / "lstm_conversion" / "product_conversion_clean.jsonl",
        help="Output JSONL file for clean product rows.",
    )
    parser.add_argument(
        "--review-output",
        type=Path,
        default=data_root / "lstm_conversion" / "product_conversion_review.jsonl",
        help="Output JSONL file for review rows.",
    )
    parser.add_argument(
        "--report-output",
        type=Path,
        default=data_root / "lstm_conversion" / "product_conversion_report.json",
        help="Output JSON file for the report.",
    )
    parser.add_argument("--force", action="store_true", help="Overwrite existing outputs.")
    return parser.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace", line_buffering=True)
        sys.stderr.reconfigure(encoding="utf-8", errors="replace", line_buffering=True)
    except Exception:
        pass

    print("[START] product conversion cleanup")
    args = parse_args(argv)

    for path in (args.output, args.review_output, args.report_output):
        if path.exists() and not args.force:
            raise FileExistsError(f"Refusing to overwrite {path}; pass --force")

    clean_rows, new_review_rows, dataset_report = process_dataset_rows(args.input_dataset)
    carried_review_rows, carried_review_reasons, carried_review_samples = process_review_rows(args.input_review)

    final_review_rows = carried_review_rows + new_review_rows
    review_reasons = Counter(dataset_report["review_reasons"])
    review_reasons.update(carried_review_reasons)

    unique_clean_rows: List[Dict[str, Any]] = []
    seen_clean: set[str] = set()
    for row in clean_rows:
        key = exact_record_key(row)
        if key in seen_clean:
            dataset_report["duplicates_removed"] += 1
            review_reasons["duplicate"] += 1
            continue
        seen_clean.add(key)
        unique_clean_rows.append(row)

    report = {
        "rows_scanned": dataset_report["rows_scanned"] + (len(carried_review_rows) if carried_review_rows else 0),
        "rows_written": len(unique_clean_rows),
        "rows_sent_to_review": len(final_review_rows),
        "duplicates_removed": dataset_report["duplicates_removed"],
        "rows_by_intent": dataset_report["rows_by_intent"],
        "review_reasons": dict(sorted(review_reasons.items())),
        "top_20_commands": dataset_report["top_20_commands"],
        "top_20_event_ids": dataset_report["top_20_event_ids"],
        "sample_clean_rows_per_intent": dataset_report["sample_clean_rows_per_intent"],
        "sample_review_rows": carried_review_samples + [sample_review_row(row) for row in new_review_rows[: max(0, 20 - len(carried_review_samples))]],
    }

    write_jsonl(args.output, unique_clean_rows)
    print("[OUTPUT] product conversion clean dataset saved")
    write_jsonl(args.review_output, final_review_rows)
    print("[OUTPUT] product conversion review saved")
    write_json(args.report_output, report)
    print("[OUTPUT] product conversion report saved")
    print("[QUALITY] final valid rows", len(unique_clean_rows))
    print(json.dumps({**report, "dataset_sha256": sha256_file(args.output), "review_sha256": sha256_file(args.review_output)}, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
