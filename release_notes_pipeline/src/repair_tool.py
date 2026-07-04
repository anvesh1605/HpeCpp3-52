"""Rule-based repair tool for network engineering QA chat JSONL datasets."""

from __future__ import annotations

import argparse
import json
import logging
import re
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

LOGGER = logging.getLogger(__name__)

BUG_ID_RE = re.compile(r"Bug ID\s*([A-Za-z0-9-]+)", re.IGNORECASE)
WHY_QUESTION_RE = re.compile(r"^Why is (.+?) important for operations\?$", re.IGNORECASE)
REASON_QUESTION_RE = re.compile(r"^What is the reason (.+?) important for operations\?$", re.IGNORECASE)
MARKER_OCCURS = re.compile(r"^It occurs when\s+(.+)$", re.IGNORECASE)
MARKER_RESULTS = re.compile(r"^This results in\s+(.+)$", re.IGNORECASE)
MARKER_MATTERS = re.compile(r"^This matters because\s+(.+)$", re.IGNORECASE)
WHEN_CLAUSE_RE = re.compile(r"^When\s+(.+?),\s*(.+)$", re.IGNORECASE)
WORD_RE = re.compile(r"\b[A-Za-z][A-Za-z0-9/-]*\b")
CONNECTOR_START_RE = re.compile(r"^(when|after|during|while|in)\b", re.IGNORECASE)
DANGLING_ENDINGS = ("particularly", "specifically")
DISALLOWED_ANSWER_PHRASES = (
    "it occurs when",
    "this results in",
    "this matters because",
    "the issue is observed",
    "the problem is seen",
    "the issue occurs in the following",
)
MIN_MEANINGFUL_WORDS = 8

PROTOCOL_UPPER = {
    "SNMP",
    "PTP",
    "BGP",
    "OSPF",
    "VLAN",
    "VSX",
    "LAG",
    "PBR",
    "VRF",
    "STP",
    "GNSS",
    "SYNCE",
    "ICMP",
}

BOILERPLATE_PATTERNS = [
    "release note covers software versions",
    "known open issues with this branch of the software",
    "modern, fully programmable operating system",
    "higher availability and dynamic software process changes",
    "version number will display",
    "for 8100 switches",
]

QUESTION_PRIORITY = [
    re.compile(r"^Under what condition does .+ issue occur\?$", re.IGNORECASE),
    re.compile(r"^What workaround is recommended", re.IGNORECASE),
    re.compile(r"^How would an engineer identify", re.IGNORECASE),
    re.compile(r"^What symptom occurs", re.IGNORECASE),
    re.compile(r"^How is .+ behavior described", re.IGNORECASE),
]


def _normalize_space(text: str) -> str:
    return re.sub(r"\s+", " ", text.replace("\xa0", " ")).strip()


def _normalize_sentence_end(text: str) -> str:
    text = _normalize_space(text).rstrip(" .;")
    return f"{text}." if text else text


def _lowercase_first(text: str) -> str:
    if not text:
        return text
    match = re.match(r"^([A-Za-z0-9/-]+)(.*)$", text)
    if not match:
        return text
    first = match.group(1)
    rest = match.group(2)
    if len(first) > 1 and (first.isupper() or first in {"ESXi", "SyncE"}):
        return text
    if len(first) == 1:
        return first.lower() + rest
    return first[0].lower() + first[1:] + rest


def _remove_dangling_tail(text: str) -> str:
    value = _normalize_space(text).rstrip(" .;:,")
    lowered = value.lower()
    for dangling in DANGLING_ENDINGS:
        suffix = f" {dangling}"
        if lowered.endswith(suffix):
            value = value[: -len(suffix)].rstrip(" ,;:")
            lowered = value.lower()
    return value


def _contains_disallowed_phrase(text: str) -> bool:
    lowered = text.lower()
    return any(phrase in lowered for phrase in DISALLOWED_ANSWER_PHRASES)


def _meaningful_word_count(text: str) -> int:
    return len(WORD_RE.findall(text))


def _connector_sentence_start(text: str) -> str:
    value = _normalize_space(text)
    if not value:
        return ""
    match = CONNECTOR_START_RE.match(value)
    if not match:
        return value
    connector = match.group(1).capitalize()
    remainder = value[len(match.group(1)) :].lstrip()
    if not remainder:
        return connector
    return f"{connector} {_lowercase_first(remainder)}"


def _extract_user_assistant(messages: object) -> Tuple[str, str]:
    question = ""
    answer = ""
    if not isinstance(messages, list):
        return question, answer
    for message in messages:
        if not isinstance(message, dict):
            continue
        role = _normalize_space(str(message.get("role", ""))).lower()
        content = _normalize_space(str(message.get("content", "")))
        if role == "user" and content and not question:
            question = content
        if role == "assistant" and content and not answer:
            answer = content
    return question, answer


def _fix_mixed_case_acronyms(text: str) -> str:
    desired_case = {
        "snmp": "SNMP",
        "ptp": "PTP",
        "bgp": "BGP",
        "ospf": "OSPF",
        "vlan": "VLAN",
        "vlans": "VLANs",
        "vsx": "VSX",
        "lag": "LAG",
        "pbr": "PBR",
        "vrf": "VRF",
        "stp": "STP",
        "gnss": "GNSS",
        "synce": "SyncE",
        "icmp": "ICMP",
        "esxi": "ESXi",
    }

    def replace_word(match: re.Match[str]) -> str:
        token = match.group(0)
        canonical = desired_case.get(token.lower())
        if canonical:
            return canonical
        upper = token.upper()
        if upper in PROTOCOL_UPPER:
            return upper
        return token

    return WORD_RE.sub(replace_word, text)


def _rewrite_why_question(question: str) -> str:
    question = _normalize_space(question).rstrip(".")
    match = WHY_QUESTION_RE.match(question)
    if match:
        topic = match.group(1).strip()
        return f"Under what condition does the {topic} issue occur?"
    match = REASON_QUESTION_RE.match(question)
    if match:
        topic = match.group(1).strip()
        return f"Under what condition does the {topic} issue occur?"
    return f"{question}?" if not question.endswith("?") else question


def _is_boilerplate(answer: str) -> bool:
    lowered = answer.lower()
    return any(pattern in lowered for pattern in BOILERPLATE_PATTERNS)


def _is_unrecoverable_truncation(answer: str) -> bool:
    if "..." in answer:
        return True
    normalized = _normalize_space(answer)
    # Likely clipped phrase endings, e.g. "assigned an."
    if re.search(r"\b(an|the|to|of|in|for|with)\.$", normalized.lower()):
        return True
    return False


def _split_prefix_body(answer: str) -> Tuple[str, str]:
    answer = _normalize_space(answer)
    if ":" not in answer:
        return "", answer
    prefix, body = answer.split(":", 1)
    return _normalize_space(prefix), _normalize_space(body)


def _extract_category_from_answer(answer: str) -> str:
    prefix, _ = _split_prefix_body(answer)
    if not prefix:
        return ""
    category = re.sub(r"\(Bug ID[^)]*\)", "", prefix, flags=re.IGNORECASE).strip(" -")
    return _normalize_space(category)


def _extract_bug_id(answer: str) -> str:
    match = BUG_ID_RE.search(answer)
    return match.group(1) if match else ""


def _strip_symptom_condition_clause(text: str) -> str:
    value = _normalize_space(text).rstrip(".")
    if not value:
        return ""
    marker = value.lower().find(" when ")
    if marker == -1:
        return value
    stripped = value[:marker].strip(" ,;:")
    return stripped or value


def _normalize_trigger_text(text: str) -> str:
    value = _normalize_space(text).rstrip(".")
    if not value:
        return ""
    lowered = value.lower()
    replacements = [
        ("this issue occurs when ", "when "),
        ("this issue may occur when ", "when "),
        ("this issue can occur when ", "when "),
        ("this issue occurs after ", "after "),
        ("this issue is observed during ", "during "),
        ("this issue occurs in ", "in "),
        ("this issue can occur in ", "in "),
        ("this issue occurs in the following workflows: ", "in the following workflows where "),
        ("this issue can occur in the following workflows: ", "in the following workflows where "),
    ]
    for prefix, replacement in replacements:
        if lowered.startswith(prefix):
            value = replacement + value[len(prefix) :]
            break
    return _remove_dangling_tail(value.strip(" ,;"))


def _complete_condition_sentence(trigger: str, symptom: str) -> str:
    trigger_text = _normalize_trigger_text(trigger)
    symptom_text = _remove_dangling_tail(symptom)
    if not trigger_text or not symptom_text:
        return ""
    result_clause = _lowercase_first(symptom_text.rstrip("."))
    if CONNECTOR_START_RE.match(trigger_text):
        sentence = _normalize_sentence_end(f"{_connector_sentence_start(trigger_text)}, {result_clause}")
    else:
        sentence = _normalize_sentence_end(f"When {_lowercase_first(trigger_text)}, {result_clause}")
    if _contains_disallowed_phrase(sentence):
        return ""
    return sentence


def _extract_signal_phrases(body: str) -> Tuple[str, str]:
    fragments = [piece.strip() for piece in re.split(r"(?<=[.!?])\s+", body) if piece.strip()]
    if not fragments:
        return "", ""

    symptom = fragments[0].rstrip(".")
    trigger = ""
    for fragment in fragments[1:]:
        clean = fragment.rstrip(".")
        occurs = MARKER_OCCURS.match(clean)
        if occurs:
            trigger = occurs.group(1).strip()
            continue
        results = MARKER_RESULTS.match(clean)
        if results:
            # result describes symptom detail
            if not symptom:
                symptom = results.group(1).strip()
            continue
        matters = MARKER_MATTERS.match(clean)
        if matters:
            if not trigger:
                trigger = matters.group(1).strip()
            continue
        if clean and not trigger and (
            "when " in clean.lower()
            or "after " in clean.lower()
            or "during " in clean.lower()
            or "while " in clean.lower()
            or clean.lower().startswith("in ")
        ):
            trigger = clean

    when_match = WHEN_CLAUSE_RE.match(symptom)
    if when_match:
        trigger = trigger or when_match.group(1).strip()
        symptom = when_match.group(2).strip()

    if not trigger:
        lowered = symptom.lower()
        when_idx = lowered.find(" when ")
        if when_idx != -1:
            trigger = symptom[when_idx + 6 :].strip()
            symptom = symptom[:when_idx].strip(" ,;")

    symptom = _remove_dangling_tail(symptom)
    trigger = _normalize_trigger_text(trigger)
    return _normalize_space(symptom).rstrip("."), _normalize_space(trigger).rstrip(".")


def _rewrite_answer(answer: str, intent: str) -> str:
    answer = _fix_mixed_case_acronyms(_normalize_space(answer))
    prefix, body = _split_prefix_body(answer)
    if not body:
        return ""

    category = _extract_category_from_answer(answer)
    bug_id = _extract_bug_id(answer)
    if not category or not bug_id:
        return ""
    normalized_prefix = f"{category} (Bug ID {bug_id})"

    symptom, trigger = _extract_signal_phrases(body)
    if intent == "condition":
        if not trigger:
            return ""
        text = _complete_condition_sentence(trigger, symptom)
        if not text:
            return ""
    else:
        if not symptom:
            return ""
        text = _normalize_sentence_end(_remove_dangling_tail(symptom))
    text = _fix_mixed_case_acronyms(text)
    if _contains_disallowed_phrase(text):
        return ""
    if _meaningful_word_count(text) < MIN_MEANINGFUL_WORDS:
        return ""
    if _remove_dangling_tail(text).lower() != text.rstrip(".").lower():
        return ""
    return f"{normalized_prefix}: {text}"


def _question_intent(question: str) -> str:
    lowered = question.lower()
    if lowered.startswith("why is") or "important for operations" in lowered:
        return "condition"
    if lowered.startswith("under what condition") or "trigger" in lowered:
        return "condition"
    return "symptom"


def _canonical_question(intent: str, category: str, bug_id: str) -> str:
    topic = f"{category} Bug {bug_id}".strip()
    if intent == "condition":
        return f"Under what condition does the {topic} issue occur?"
    return f"What symptom occurs in {topic}?"


def _answer_body(answer: str) -> str:
    _, body = _split_prefix_body(answer)
    return _normalize_space(body)


def _question_has_bug_id(question: str) -> bool:
    return bool(re.search(r"\bbug\s+[A-Za-z0-9-]+\b", question, flags=re.IGNORECASE))


def _is_compliant_entry(question: str, answer: str) -> bool:
    category = _extract_category_from_answer(answer)
    bug_id = _extract_bug_id(answer)
    if not category or not bug_id:
        return False
    if _is_boilerplate(answer) or _is_unrecoverable_truncation(answer):
        return False
    body = _answer_body(answer)
    if not body:
        return False
    if _contains_disallowed_phrase(body):
        return False
    if _meaningful_word_count(body) < MIN_MEANINGFUL_WORDS:
        return False
    if _remove_dangling_tail(body).lower() != body.rstrip(".").lower():
        return False
    if not _question_has_bug_id(question):
        return False

    intent = _question_intent(question)
    if intent == "condition":
        if not re.search(r"\b(when|after|during|while|in)\b", body, flags=re.IGNORECASE):
            return False
        if "," not in body:
            return False
    return True


def _question_priority(question: str) -> int:
    for index, pattern in enumerate(QUESTION_PRIORITY):
        if pattern.search(question):
            return index
    return len(QUESTION_PRIORITY) + 1


def _dedupe_semantic(rows: Iterable[Dict[str, str]]) -> List[Dict[str, str]]:
    grouped: Dict[Tuple[str, str], Dict[str, str]] = {}
    for row in rows:
        bug_id = row.get("bug_id") or "no_bug"
        intent = _question_intent(row["question"])
        key = (bug_id, intent)
        if key not in grouped:
            grouped[key] = row
            continue

        existing = grouped[key]
        current_rank = _question_priority(row["question"])
        existing_rank = _question_priority(existing["question"])
        if current_rank < existing_rank:
            grouped[key] = row
            continue
        if current_rank == existing_rank and len(row["answer"]) > len(existing["answer"]):
            grouped[key] = row

    return list(grouped.values())


def repair_records(records: Iterable[Dict[str, object]]) -> List[Dict[str, object]]:
    cleaned: List[Dict[str, str]] = []
    for raw in records:
        messages = raw.get("messages")
        question, answer = _extract_user_assistant(messages)
        if not question or not answer:
            continue

        normalized_question = _rewrite_why_question(_fix_mixed_case_acronyms(question))
        normalized_answer = _fix_mixed_case_acronyms(_normalize_space(answer))
        if _is_compliant_entry(normalized_question, normalized_answer):
            category = _extract_category_from_answer(normalized_answer)
            bug_id = _extract_bug_id(normalized_answer)
            cleaned.append(
                {
                    "question": normalized_question,
                    "answer": normalized_answer,
                    "category": category,
                    "bug_id": bug_id,
                    "intent": _question_intent(normalized_question),
                }
            )
            continue

        intent = _question_intent(normalized_question)
        repaired_answer = _rewrite_answer(normalized_answer, intent=intent)
        if not repaired_answer:
            continue
        if _is_boilerplate(repaired_answer):
            continue
        if _is_unrecoverable_truncation(repaired_answer):
            continue

        category = _extract_category_from_answer(repaired_answer)
        bug_id = _extract_bug_id(repaired_answer)
        if not category or not bug_id:
            continue
        cleaned.append(
            {
                "question": _canonical_question(intent, category, bug_id),
                "answer": repaired_answer,
                "category": category,
                "bug_id": bug_id,
                "intent": intent,
            }
        )

    deduped = _dedupe_semantic(cleaned)
    output: List[Dict[str, object]] = []
    for row in deduped:
        output.append(
            {
                "messages": [
                    {"role": "user", "content": row["question"]},
                    {"role": "assistant", "content": row["answer"]},
                ]
            }
        )
    return output


def load_jsonl(path: Path) -> List[Dict[str, object]]:
    rows: List[Dict[str, object]] = []
    if not path.exists():
        raise FileNotFoundError(f"Input JSONL not found: {path}")
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                payload = json.loads(line)
            except json.JSONDecodeError:
                LOGGER.warning("Skipping invalid JSON on line %s", line_number)
                continue
            if isinstance(payload, dict):
                rows.append(payload)
    return rows


def write_jsonl(rows: Iterable[Dict[str, object]], output_path: Path) -> int:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with output_path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
            count += 1
    return count


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Repair chat JSONL QA training data.")
    parser.add_argument("--input-jsonl", type=Path, required=True)
    parser.add_argument("--output-jsonl", type=Path, required=True)
    parser.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING", "ERROR"])
    return parser.parse_args()


def configure_logging(level: str) -> None:
    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )


def main() -> None:
    args = parse_args()
    configure_logging(args.log_level)
    raw_records = load_jsonl(args.input_jsonl)
    repaired = repair_records(raw_records)
    written = write_jsonl(repaired, args.output_jsonl)
    LOGGER.info("Repaired %s input rows into %s output rows at %s", len(raw_records), written, args.output_jsonl)


if __name__ == "__main__":
    main()
