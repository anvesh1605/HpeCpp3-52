"""Formatting helpers for rich JSON and final chat JSONL exports."""

from __future__ import annotations

import json
import logging
import re
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Sequence, Tuple

LOGGER = logging.getLogger(__name__)

try:
    from sklearn.feature_extraction.text import TfidfVectorizer
except ImportError:  # pragma: no cover
    TfidfVectorizer = None

try:
    from .validator import FAIL, validate_answer
except ImportError:  # pragma: no cover
    from validator import FAIL, validate_answer

CATEGORY_RE = (
    re.compile(r"Category:\s*([^;|]+)", re.IGNORECASE),
    re.compile(r"^\s*([^:()|;]+?)\s*\(Bug ID\s*[^)]+\)\s*:?", re.IGNORECASE),
)
BUG_ID_RE = (
    re.compile(r"Bug ID:\s*([^;|]+)", re.IGNORECASE),
    re.compile(r"\(Bug ID\s*([^)]+)\)", re.IGNORECASE),
)
ISSUE_CATEGORY_LABEL_RE = re.compile(
    r"(?:^|[;\n|])\s*(?:issue\s*)?category(?:\s*name)?\s*[:=]\s*([^\n;|]+)",
    re.IGNORECASE,
)
ISSUE_BUG_LABEL_RE = re.compile(
    r"(?:^|[;\n|])\s*(?:bug\s*(?:id)?|issue\s*id)\s*[:=#]\s*([A-Za-z0-9-]+)",
    re.IGNORECASE,
)
BUG_IN_PARENS_RE = re.compile(
    r"\(\s*Bug\s*(?:ID|id)?\s*[:=#]?\s*([A-Za-z0-9-]+)\s*\)",
    re.IGNORECASE,
)
BRACKET_PAIR_RE = re.compile(r"\[\s*([^\[\]]+?)\s*\]\s*\[\s*([A-Za-z0-9-]+)\s*\]")
CATEGORY_BUG_PAIR_RE = re.compile(
    r"\b(?:in|for|on|when|after|during|while)\s+(.+?)\s+Bug\s+([A-Za-z0-9-]+)\b",
    re.IGNORECASE,
)
BARE_BUG_RE = re.compile(r"\bBug\s+([A-Za-z0-9-]*\d[A-Za-z0-9-]*)\b", re.IGNORECASE)
INLINE_CATEGORY_BUG_RE = re.compile(
    r"^\s*([A-Za-z0-9][A-Za-z0-9/&+.,\-\s]{0,120}?)\s*\(\s*Bug\s*(?:ID|id)?\s*[:=#]?\s*([A-Za-z0-9-]+)\s*\)",
    re.IGNORECASE,
)
SYMPTOM_RE = re.compile(r"Symptom\s*:?\s*(.+?)(?:\s+Scenario\s*:|\s+Workaround\s*:|$)", re.IGNORECASE)
SCENARIO_RE = re.compile(r"Scenario\s*:?\s*(.+?)(?:\s+Workaround\s*:|$)", re.IGNORECASE)
REL_TOPIC_RE = re.compile(r"(related to )(.+?)( in this release note\?)", re.IGNORECASE)
HOW_BEHAVIOR_RE = re.compile(r"How is (.+?) behavior described", re.IGNORECASE)
EXPLAIN_BEHAVIOR_RE = re.compile(r"(Explain|Describe)\s+(.+?)\s+behavior in this note\?", re.IGNORECASE)
WORD_RE = re.compile(r"[a-z0-9]+")
MEANINGFUL_WORD_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9/-]*")
SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+")
CONNECTOR_START_RE = re.compile(r"^(when|after|during|while|in)\b", re.IGNORECASE)
DISALLOWED_ANSWER_PHRASES = (
    "it occurs when",
    "this results in",
    "this matters because",
    "the issue is observed",
    "the problem is seen",
    "the issue occurs in the following",
)
DANGLING_ENDINGS = ("particularly", "specifically")
MIN_MEANINGFUL_WORDS = 8
ACRONYM_CASE_MAP = {
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
BOILERPLATE_PATTERNS = [
    "the following are known open issues with this branch of the software",
    "this release note covers software versions",
    "version number will display",
    "modern, fully programmable operating system",
    "higher availability and dynamic software process changes",
]
STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "by",
    "for",
    "from",
    "if",
    "in",
    "is",
    "it",
    "of",
    "on",
    "or",
    "that",
    "the",
    "this",
    "to",
    "when",
    "with",
}


def _normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text.replace("\xa0", " ")).strip()


def _iter_text_values(value: object) -> Iterable[str]:
    if value is None:
        return
    if isinstance(value, str):
        yield value
        return
    if isinstance(value, Mapping):
        for nested in value.values():
            yield from _iter_text_values(nested)
        return
    if isinstance(value, (list, tuple, set)):
        for nested in value:
            yield from _iter_text_values(nested)
        return
    yield str(value)


def _looks_like_category(value: str) -> bool:
    cleaned = _normalize_text(value).strip(" ;:|[]()")
    if not cleaned:
        return False
    lowered = cleaned.lower()
    return lowered not in {"category", "issue category", "issue", "bug", "bug id", "n/a", "na", "none"}


def _normalize_bug_value(value: str) -> str:
    cleaned = _normalize_text(value).strip(" ;:|[]()")
    if not cleaned:
        return ""
    lowered = cleaned.lower()
    if lowered in {"n/a", "na", "none", "unknown", "unknown bug", "bug", "bug id", "issue", "issue id"}:
        return ""
    if not re.search(r"\d", cleaned):
        return ""
    cleaned = re.sub(r"^(?:bug\s*(?:id)?|issue\s*id)\s*[:=#]?\s*", "", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"^bug\s+", "", cleaned, flags=re.IGNORECASE)
    cleaned = cleaned.strip(" ;:|[]().")
    return cleaned


def _clean_category_candidate(value: str) -> str:
    cleaned = _normalize_text(value).strip(" ;:|[]()")
    if not cleaned:
        return ""
    cleaned = re.sub(r"^(?:issue\s*)?category(?:\s*name)?\s*[:=]\s*", "", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"^(?:category|issue)\s*[:=]\s*", "", cleaned, flags=re.IGNORECASE)
    cleaned = re.split(
        r"\s*\(\s*Bug\s*(?:ID|id)?\s*[:=#]?\s*[A-Za-z0-9-]+\s*\)",
        cleaned,
        maxsplit=1,
    )[0]
    cleaned = re.split(r"[;|]", cleaned, maxsplit=1)[0]
    cleaned = cleaned.split(":", 1)[0]
    cleaned = _normalize_text(cleaned).strip(" ;:|[]()")
    return cleaned if _looks_like_category(cleaned) else ""


def _extract_issue_metadata_from_text(text: str) -> Tuple[str, str]:
    normalized = _normalize_text(text)
    if not normalized:
        return "", ""

    category = ""
    bug_id = ""

    for pattern in (ISSUE_CATEGORY_LABEL_RE, INLINE_CATEGORY_BUG_RE, BRACKET_PAIR_RE, CATEGORY_BUG_PAIR_RE):
        match = pattern.search(normalized)
        if not match:
            continue
        if match.lastindex and match.lastindex >= 2:
            candidate_category = _clean_category_candidate(match.group(1))
            candidate_bug = _normalize_bug_value(match.group(2))
            if candidate_category and not category:
                category = candidate_category
            if candidate_bug and not bug_id:
                bug_id = candidate_bug
        else:
            candidate_category = _clean_category_candidate(match.group(1))
            if candidate_category and not category:
                category = candidate_category

    for pattern in (ISSUE_BUG_LABEL_RE, BUG_IN_PARENS_RE, BARE_BUG_RE):
        match = pattern.search(normalized)
        if not match:
            continue
        candidate_bug = _normalize_bug_value(match.group(1))
        if candidate_bug:
            bug_id = bug_id or candidate_bug
            break

    return category, bug_id


def _collect_metadata_text_sources(*sources: object) -> List[str]:
    collected: List[str] = []
    for source in sources:
        if source is None:
            continue
        if isinstance(source, str):
            cleaned = _normalize_text(source)
            if cleaned:
                collected.append(cleaned)
            continue
        if isinstance(source, Mapping):
            for value in source.values():
                if isinstance(value, str):
                    cleaned = _normalize_text(value)
                    if cleaned:
                        collected.append(cleaned)
                elif isinstance(value, (list, tuple)):
                    for nested in value:
                        if isinstance(nested, str):
                            cleaned = _normalize_text(nested)
                            if cleaned:
                                collected.append(cleaned)
                else:
                    cleaned = _normalize_text(str(value))
                    if cleaned:
                        collected.append(cleaned)
            continue
        if isinstance(source, (list, tuple, set)):
            for value in source:
                if isinstance(value, str):
                    cleaned = _normalize_text(value)
                else:
                    cleaned = _normalize_text(str(value))
                if cleaned:
                    collected.append(cleaned)
            continue
        cleaned = _normalize_text(str(source))
        if cleaned:
            collected.append(cleaned)
    return collected


def _normalize_question(text: str) -> str:
    question = _normalize_text(text).rstrip(".?! ")
    return f"{question}?" if question else ""


def _extract_field(regex: re.Pattern[str], text: str) -> str:
    match = regex.search(text)
    return _normalize_text(match.group(1)) if match else ""


def _extract_first_match(patterns: Sequence[re.Pattern[str]], text: str) -> str:
    for pattern in patterns:
        match = pattern.search(text)
        if not match:
            continue
        for group in match.groups():
            value = _normalize_text(str(group))
            if value:
                return value
    return ""


def _extract_category(answer: str, context: str) -> str:
    for text in (context, answer):
        category, _ = _extract_issue_metadata_from_text(text)
        if category:
            return category
    return ""


def _extract_bug_id(answer: str, context: str) -> str:
    for text in (context, answer):
        _, bug_id = _extract_issue_metadata_from_text(text)
        if bug_id:
            return bug_id
    return ""


def recover_issue_metadata(record: Dict[str, object]) -> Dict[str, str]:
    """Recover category, bug ID, and source type from any available record fields."""
    category_name = _normalize_text(str(record.get("category_name", "")))
    if not _looks_like_category(category_name):
        category_name = ""

    bug_id = _normalize_bug_value(str(record.get("bug_id", "")))

    for text in (
        record.get("category_name", ""),
        record.get("bug_id", ""),
        record.get("title", ""),
        record.get("issue_description", ""),
        record.get("description", ""),
        record.get("summary", ""),
        record.get("context", ""),
        record.get("answer", ""),
        record.get("question", ""),
        record.get("metadata", ""),
        record.get("source", ""),
        record.get("source_path", ""),
    ):
        if category_name and bug_id:
            break
        if text is None:
            continue
        candidate_text = _normalize_text(text) if isinstance(text, str) else _normalize_text(str(text))
        if not candidate_text:
            continue
        candidate_category, candidate_bug = _extract_issue_metadata_from_text(candidate_text)
        if category_name and bug_id:
            break
        if not category_name and candidate_category:
            category_name = candidate_category
        if not bug_id and candidate_bug:
            bug_id = candidate_bug

    source_type = _normalize_text(str(record.get("source_type", "")))
    if not source_type:
        messages = record.get("messages")
        if isinstance(messages, list) and len(messages) > 2:
            source_type = "release_notes_only_multiturn"
        else:
            source_type = "release_notes_only"

    return {
        "category_name": category_name,
        "bug_id": bug_id,
        "source_type": source_type,
    }


def has_issue_markers(*sources: object) -> bool:
    """Return True when any source contains recoverable category and bug ID metadata."""
    for source in sources:
        if source is None:
            continue
        text = _normalize_text(source) if isinstance(source, str) else _normalize_text(str(source))
        if not text:
            continue
        category_name, bug_id = _extract_issue_metadata_from_text(text)
        if category_name and bug_id:
            return True
    return False


def extract_issue_metadata(
    answer: str,
    context: str,
    question: str = "",
    title: str = "",
    issue_description: str = "",
    metadata: object = None,
) -> Tuple[str, str]:
    """Extract category and bug ID from the available record text."""
    text_sources = _collect_metadata_text_sources(
        answer,
        context,
        question,
        title,
        issue_description,
        metadata if metadata is not None else "",
    )
    category_name = ""
    bug_id = ""
    for text in text_sources:
        if category_name and bug_id:
            break
        candidate_category, candidate_bug = _extract_issue_metadata_from_text(text)
        if not category_name and candidate_category:
            category_name = candidate_category
        if not bug_id and candidate_bug:
            bug_id = candidate_bug
    return category_name, bug_id


def _extract_symptom(text: str) -> str:
    match = SYMPTOM_RE.search(text)
    if not match:
        return ""
    return _normalize_text(match.group(1)).rstrip(".")


def _extract_scenario(text: str) -> str:
    match = SCENARIO_RE.search(text)
    if not match:
        return ""
    return _normalize_text(match.group(1)).rstrip(".")


def _extract_condition_from_text(text: str) -> str:
    value = _normalize_text(text)
    if ":" in value:
        value = value.split(":", 1)[1]
    value = value.strip().rstrip(".")
    if not value:
        return ""
    when_match = re.search(r"\b(when|after|during|while|in)\b\s+(.+)$", value, flags=re.IGNORECASE)
    if when_match:
        return _normalize_text(f"{when_match.group(1)} {when_match.group(2)}").rstrip(".")
    return value


def _strip_symptom_condition_clause(text: str) -> str:
    value = _normalize_text(text).rstrip(".")
    if not value:
        return ""
    lowered = value.lower()
    marker = lowered.find(" when ")
    if marker == -1:
        return value
    stripped = value[:marker].strip(" ,;:")
    return stripped or value


def _first_sentence(text: str) -> str:
    parts = [part.strip() for part in SENTENCE_SPLIT_RE.split(_normalize_text(text)) if part.strip()]
    return parts[0].rstrip(".") if parts else ""


def _lowercase_sentence_start(text: str) -> str:
    value = _normalize_text(text).strip()
    if not value:
        return ""
    match = re.match(r"^([A-Za-z0-9/-]+)(.*)$", value)
    if not match:
        return value
    first_word = match.group(1)
    rest = match.group(2)
    if len(first_word) > 1 and (first_word.isupper() or first_word in {"ESXi", "SyncE"}):
        return value
    if len(first_word) == 1:
        return first_word.lower() + rest
    return first_word[0].lower() + first_word[1:] + rest


def _lowercase_after_connector(text: str) -> str:
    value = _normalize_text(text).strip()
    if not value:
        return ""
    match = CONNECTOR_START_RE.match(value)
    if not match:
        return value
    connector = match.group(1)
    remainder = value[len(connector) :].lstrip()
    if not remainder:
        return connector.capitalize()
    remainder = _lowercase_sentence_start(remainder)
    return f"{connector.capitalize()} {remainder}"


def _remove_dangling_tail(text: str) -> str:
    value = _normalize_text(text).rstrip(" .;:,")
    lowered = value.lower()
    for dangling in DANGLING_ENDINGS:
        suffix = f" {dangling}"
        if lowered.endswith(suffix):
            value = value[: -len(suffix)].rstrip(" ,;:")
            lowered = value.lower()
    return value


def _contains_disallowed_answer_phrase(text: str) -> bool:
    lowered = text.lower()
    return any(phrase in lowered for phrase in DISALLOWED_ANSWER_PHRASES)


def _fix_acronym_case(text: str) -> str:
    def replace_word(match: re.Match[str]) -> str:
        token = match.group(0)
        return ACRONYM_CASE_MAP.get(token.lower(), token)

    return re.sub(r"\b[A-Za-z][A-Za-z0-9/-]*\b", replace_word, text)


def _meaningful_word_count(text: str) -> int:
    return len(MEANINGFUL_WORD_RE.findall(text))


def _normalize_scenario_trigger(text: str) -> str:
    value = _normalize_text(text).rstrip(".")
    if not value:
        return ""
    lowered = value.lower()
    replacements = [
        ("this issue occurs when ", "when "),
        ("this issue may occur when ", "when "),
        ("this issue can occur when ", "when "),
        ("this issue is observed during ", "during "),
        ("this issue occurs after ", "after "),
        ("this issue may occur after ", "after "),
        ("this issue occurs in ", "in "),
        ("this issue can occur in ", "in "),
        ("this issue occurs in the following workflows: ", "in the following workflows where "),
        ("this issue can occur in the following workflows: ", "in the following workflows where "),
    ]
    for prefix, replacement in replacements:
        if lowered.startswith(prefix):
            value = replacement + value[len(prefix) :]
            lowered = value.lower()
            break
    return _remove_dangling_tail(value.strip(" ,;"))


def _build_symptom_sentence(symptom: str) -> str:
    cleaned = _remove_dangling_tail(symptom)
    if not cleaned:
        return ""
    cleaned = cleaned.strip()
    if not re.search(
        r"\b(is|are|does|do|fails?|drops?|blocks?|prevents?|shows?|takes?|causes?|transitions?|experiences?|becomes?|remains?|has|have|contains?|include[s]?)\b",
        cleaned,
        re.IGNORECASE,
    ):
        return ""
    sentence = f"{cleaned.rstrip('.')}."
    if _contains_disallowed_answer_phrase(sentence):
        return ""
    return _fix_acronym_case(sentence)


def _is_result_redundant(trigger: str, result: str) -> bool:
    trigger_norm = _normalize_text(trigger).lower()
    result_norm = _normalize_text(result).lower()
    if not trigger_norm or not result_norm:
        return False
    if result_norm in trigger_norm:
        return True
    if SequenceMatcher(None, trigger_norm, result_norm).ratio() >= 0.72:
        return True
    trigger_tokens = [token for token in _tokenize(trigger_norm) if token not in STOPWORDS]
    result_tokens = [token for token in _tokenize(result_norm) if token not in STOPWORDS]
    if not result_tokens:
        return False
    trigger_token_set = set(trigger_tokens)
    overlap = sum(1 for token in result_tokens if token in trigger_token_set)
    return (overlap / len(result_tokens)) >= 0.60


def _build_condition_sentence(trigger: str, _result: str) -> str:
    trigger_text = _normalize_scenario_trigger(trigger)
    if not trigger_text:
        return ""

    if CONNECTOR_START_RE.match(trigger_text):
        sentence = f"{_lowercase_after_connector(trigger_text)}, the issue is triggered."
    else:
        sentence = f"When {_lowercase_sentence_start(trigger_text)}, the issue is triggered."
    if _contains_disallowed_answer_phrase(sentence):
        return ""
    return _fix_acronym_case(sentence)


def _rewrite_question_topic(question: str, category: str) -> str:
    updated = _normalize_question(question)
    if not updated:
        return updated

    updated = re.sub(r"\bthis item\b", category, updated, flags=re.IGNORECASE)
    updated = REL_TOPIC_RE.sub(lambda m: f"{m.group(1)}{category}{m.group(3)}", updated)
    updated = HOW_BEHAVIOR_RE.sub(lambda _: f"How is {category} behavior described", updated)
    updated = EXPLAIN_BEHAVIOR_RE.sub(lambda m: f"{m.group(1)} {category} behavior in this note?", updated)
    return _normalize_question(updated)


def _canonicalize_question_style(question: str) -> str:
    updated = _normalize_question(question)
    updated = re.sub(r"^(Can you explain:\s*)", "", updated, flags=re.IGNORECASE)
    updated = re.sub(r"^(Please explain\s+)", "", updated, flags=re.IGNORECASE)
    return _normalize_question(updated)


def _question_type(question: str) -> str:
    lowered = question.lower()
    if lowered.startswith("why is") or "important for operations" in lowered:
        return "disallowed"
    if "under what condition" in lowered or "trigger" in lowered:
        return "condition"
    if "what symptom occurs" in lowered or "key issue" in lowered:
        return "symptom"
    return "symptom"


def _canonical_question(category: str, bug_id: str, answer_type: str) -> str:
    topic = f"{category} Bug {bug_id}".strip()
    if answer_type == "condition":
        return f"Under what condition does the {topic} issue occur?"
    return f"What symptom occurs in {topic}?"


def _is_boilerplate_answer(answer: str) -> bool:
    lowered = answer.lower()
    return any(pattern in lowered for pattern in BOILERPLATE_PATTERNS)


def _build_specific_answer(question: str, answer: str, context: str, category: str, bug_id: str) -> str:
    symptom_from_context = _extract_symptom(context)
    symptom_from_answer = _extract_symptom(answer)
    scenario_from_context = _extract_scenario(context)
    scenario_from_answer = _extract_scenario(answer)
    answer_body = _normalize_text(answer.split(":", 1)[1]) if ":" in answer else _normalize_text(answer)
    symptom = _remove_dangling_tail(symptom_from_context or symptom_from_answer or _first_sentence(answer_body))
    scenario = _normalize_scenario_trigger(scenario_from_context or scenario_from_answer)

    if "..." in answer and not symptom:
        return ""
    answer_type = _question_type(question)
    if answer_type == "disallowed":
        return ""

    if not category or not bug_id:
        return ""
    prefix = f"{category} (Bug ID {bug_id})"

    if answer_type == "condition":
        scenario_fallback = _normalize_scenario_trigger(_extract_condition_from_text(answer_body))
        condition_text = scenario or scenario_fallback or _normalize_scenario_trigger(_extract_condition_from_text(symptom))
        if not condition_text:
            return ""
        condition_sentences = [
            part.strip().rstrip(".")
            for part in SENTENCE_SPLIT_RE.split(condition_text)
            if part.strip()
        ]
        trigger = condition_sentences[0] if condition_sentences else ""
        scenario_result = condition_sentences[1] if len(condition_sentences) > 1 else ""
        result = _remove_dangling_tail(symptom or scenario_result or _first_sentence(answer_body))
        sentence = _build_condition_sentence(trigger, result)
        if not sentence:
            return ""
        return f"{prefix}: {sentence}"

    if not symptom:
        return ""
    sentence = _build_symptom_sentence(symptom)
    if not sentence:
        return ""
    return f"{prefix}: {sentence}"


def _inject_bug_id_in_question(question: str, category: str, bug_id: str) -> str:
    if not category or not bug_id:
        return question
    lowered = question.lower()
    if f"bug {bug_id.lower()}" in lowered:
        return question
    escaped = re.escape(category)
    return re.sub(escaped, f"{category} Bug {bug_id}", question, count=1, flags=re.IGNORECASE)


def _extract_answer_core(answer: str) -> str:
    if ":" in answer:
        return _normalize_text(answer.split(":", 1)[1])
    return _normalize_text(answer)


def _tokenize(text: str) -> List[str]:
    return WORD_RE.findall(text.lower())


def _token_overlap_score(answer: str, context: str) -> float:
    answer_tokens = [token for token in _tokenize(answer) if token not in STOPWORDS]
    context_tokens = set(token for token in _tokenize(context) if token not in STOPWORDS)
    if not answer_tokens:
        return 0.0
    overlap = sum(1 for token in answer_tokens if token in context_tokens)
    return overlap / len(answer_tokens)


def _max_fuzzy_sentence_score(answer: str, context: str) -> float:
    candidate_chunks = [chunk.strip() for chunk in re.split(r"[.;]\s+", context) if chunk.strip()]
    if not candidate_chunks:
        return 0.0
    lowered_answer = answer.lower()
    return max(SequenceMatcher(None, lowered_answer, chunk.lower()).ratio() for chunk in candidate_chunks)


def _grounding_score(answer: str, context: str) -> float:
    answer_core = _extract_answer_core(answer)
    context_norm = _normalize_text(context)
    if not answer_core or not context_norm:
        return 0.0

    answer_lower = answer_core.lower()
    context_lower = context_norm.lower()
    exact_substring = 1.0 if answer_lower in context_lower else 0.0
    token_score = _token_overlap_score(answer_core, context_norm)
    fuzzy_score = _max_fuzzy_sentence_score(answer_core, context_norm)
    return max(exact_substring, token_score, fuzzy_score)


def _quality_score(question: str, answer: str, context: str, grounding: float) -> float:
    answer_tokens = _tokenize(answer)
    question_tokens = _tokenize(question)
    has_bug = 1.0 if "bug id" in answer.lower() else 0.0
    question_has_bug = 1.0 if re.search(r"\bbug\b", question, flags=re.IGNORECASE) else 0.0
    has_prefix = 1.0 if ":" in answer else 0.0
    has_question_mark = 1.0 if question.endswith("?") else 0.0
    no_placeholder = 1.0 if "this item" not in question.lower() else 0.0
    no_ellipsis = 1.0 if "..." not in answer else 0.0
    length_ok = 1.0 if 8 <= len(answer_tokens) <= 75 else 0.0
    question_length_ok = 1.0 if 5 <= len(question_tokens) <= 24 else 0.0
    context_presence = 1.0 if len(_tokenize(context)) >= 12 else 0.0

    specificity = (0.40 * has_bug) + (0.20 * question_has_bug) + (0.20 * has_prefix) + (0.20 * length_ok)
    clarity = (0.35 * has_question_mark) + (0.25 * no_placeholder) + (0.25 * no_ellipsis) + (0.15 * question_length_ok)
    score = (0.60 * grounding) + (0.25 * specificity) + (0.10 * clarity) + (0.05 * context_presence)
    return round(min(1.0, max(0.0, score)), 4)


def _semantic_text(record: Dict[str, object]) -> str:
    question = _normalize_question(str(record.get("question", ""))).lower()
    answer = _normalize_text(str(record.get("answer", ""))).lower()
    return f"{question} || {answer}"


def _semantic_deduplicate(
    records: List[Dict[str, object]],
    threshold: float,
) -> Tuple[List[Dict[str, object]], int, str]:
    if len(records) <= 1:
        return records, 0, "skipped_too_small"

    texts = [_semantic_text(record) for record in records]
    question_types = [_question_type(str(record.get("question", ""))) for record in records]
    bug_ids = [str(record.get("bug_id", "")).strip().lower() for record in records]
    order = sorted(
        range(len(records)),
        key=lambda index: (
            float(records[index].get("quality_score", 0.0)),
            len(texts[index]),
        ),
        reverse=True,
    )

    if TfidfVectorizer is None:
        kept_texts = set()
        kept_indices: List[int] = []
        dropped = 0
        for index in order:
            text = texts[index]
            if text in kept_texts:
                dropped += 1
                continue
            kept_texts.add(text)
            kept_indices.append(index)
        kept_indices = sorted(kept_indices)
        return [records[index] for index in kept_indices], dropped, "exact_fallback"

    try:
        vectorizer = TfidfVectorizer(analyzer="char_wb", ngram_range=(3, 5))
        matrix = vectorizer.fit_transform(texts)
    except Exception as exc:  # pylint: disable=broad-except
        LOGGER.warning("Semantic dedup TF-IDF failed (%s). Falling back to exact dedup.", exc)
        kept_texts = set()
        kept_indices = []
        dropped = 0
        for index in order:
            text = texts[index]
            if text in kept_texts:
                dropped += 1
                continue
            kept_texts.add(text)
            kept_indices.append(index)
        kept_indices = sorted(kept_indices)
        return [records[index] for index in kept_indices], dropped, "exact_fallback"

    kept_indices: List[int] = []
    dropped = 0
    for index in order:
        if not kept_indices:
            kept_indices.append(index)
            continue

        comparable = [
            kept
            for kept in kept_indices
            if question_types[kept] == question_types[index] and bug_ids[kept] == bug_ids[index]
        ]
        if not comparable:
            kept_indices.append(index)
            continue

        similarities = (matrix[index] @ matrix[comparable].T).toarray().ravel()
        max_similarity = float(similarities.max()) if similarities.size else 0.0
        if max_similarity >= threshold:
            dropped += 1
            continue
        kept_indices.append(index)

    kept_indices = sorted(kept_indices)
    return [records[index] for index in kept_indices], dropped, "tfidf_char_ngram"


def enforce_quality_rules(
    records: Iterable[Dict[str, object]],
    min_grounding_score: float = 0.62,
    min_quality_score: float = 0.72,
    semantic_dedup_threshold: float | None = 0.96,
) -> Tuple[List[Dict[str, object]], Dict[str, object]]:
    """Apply strict QA hygiene rules before exporting training data."""
    cleaned: List[Dict[str, object]] = []
    stats: Dict[str, object] = {
        "input_records": 0,
        "dropped_negative": 0,
        "dropped_boilerplate": 0,
        "dropped_missing_category_or_bug_id": 0,
        "dropped_non_specific": 0,
        "dropped_answer_rule_violation": 0,
        "dropped_references_non_text_content": 0,
        "dropped_vague_condition_trigger": 0,
        "dropped_unfixable_truncation": 0,
        "dropped_empty_question_or_answer": 0,
        "dropped_low_grounding": 0,
        "dropped_low_quality": 0,
        "rewritten_questions": 0,
        "semantic_dedup_threshold": semantic_dedup_threshold,
        "min_grounding_score": min_grounding_score,
        "min_quality_score": min_quality_score,
    }

    for record in records:
        stats["input_records"] += 1
        if record.get("is_negative"):
            stats["dropped_negative"] += 1
            continue

        question = _normalize_question(str(record.get("question", "")))
        answer = _normalize_text(str(record.get("answer", "")))
        context = _normalize_text(str(record.get("context", "")))

        if not question or not answer:
            stats["dropped_empty_question_or_answer"] += 1
            continue

        if _is_boilerplate_answer(answer):
            stats["dropped_boilerplate"] += 1
            continue

        recovered_metadata = recover_issue_metadata(record)
        category = _normalize_text(str(recovered_metadata.get("category_name", "")))
        bug_id = _normalize_text(str(recovered_metadata.get("bug_id", "")))
        if not category or not bug_id:
            stats["dropped_missing_category_or_bug_id"] += 1
            continue
        answer_type = _question_type(question)
        if answer_type == "disallowed":
            stats["dropped_non_specific"] += 1
            continue
        specific_answer = _build_specific_answer(question, answer, context, category, bug_id)
        if not specific_answer:
            if "..." in answer:
                stats["dropped_unfixable_truncation"] += 1
            else:
                stats["dropped_non_specific"] += 1
            continue
        specific_answer = re.sub(
            r",?\s+(the issue is triggered|the issue is observed|the issue occurs)\.?$",
            ".",
            specific_answer,
            flags=re.IGNORECASE,
        )

        validation_status, validation_reason = validate_answer(specific_answer, answer_type)
        if validation_status == FAIL:
            if validation_reason == "references non-text content":
                stats["dropped_references_non_text_content"] += 1
            elif validation_reason == "no actionable trigger detail":
                stats["dropped_vague_condition_trigger"] += 1
            stats["dropped_answer_rule_violation"] += 1
            continue

        rewritten_question = _rewrite_question_topic(question, category) if category else question
        rewritten_question = _canonicalize_question_style(rewritten_question)
        rewritten_question = _canonical_question(category, bug_id, answer_type)
        answer_core = _extract_answer_core(specific_answer)
        if (
            _meaningful_word_count(answer_core) < MIN_MEANINGFUL_WORDS
            or _contains_disallowed_answer_phrase(answer_core)
            or _remove_dangling_tail(answer_core).lower() != answer_core.rstrip(".").lower()
        ):
            stats["dropped_answer_rule_violation"] += 1
            continue
        if rewritten_question != question:
            stats["rewritten_questions"] += 1

        grounding = _grounding_score(specific_answer, context)
        if grounding < min_grounding_score:
            stats["dropped_low_grounding"] += 1
            continue

        quality = _quality_score(rewritten_question, specific_answer, context, grounding)
        if quality < min_quality_score:
            stats["dropped_low_quality"] += 1
            continue

        cleaned.append(
            {
                **record,
                "question": rewritten_question,
                "answer": specific_answer,
                "context": context,
                "category": record.get("category", "overview"),
                "category_name": category,
                "bug_id": bug_id,
                "grounding_score": grounding,
                "quality_score": quality,
            }
        )

    # Disambiguate question text when category has multiple bug IDs.
    category_to_bug_ids: Dict[str, set] = {}
    for record in cleaned:
        category = str(record.get("category_name", "")).strip()
        bug_id = str(record.get("bug_id", "")).strip()
        if not category or not bug_id:
            continue
        category_to_bug_ids.setdefault(category.lower(), set()).add(bug_id)
    for record in cleaned:
        category = str(record.get("category_name", "")).strip()
        bug_id = str(record.get("bug_id", "")).strip()
        if not category or not bug_id:
            continue
        if len(category_to_bug_ids.get(category.lower(), set())) <= 1:
            continue
        original = str(record.get("question", ""))
        updated = _inject_bug_id_in_question(original, category, bug_id)
        record["question"] = updated

    if semantic_dedup_threshold is None:
        deduped = cleaned
        dropped_semantic = 0
        method = "disabled"
    else:
        deduped, dropped_semantic, method = _semantic_deduplicate(cleaned, threshold=semantic_dedup_threshold)
    stats["dropped_semantic_duplicates"] = dropped_semantic
    stats["semantic_dedup_method"] = method
    stats["kept_records"] = len(deduped)
    stats["dropped_total"] = stats["input_records"] - len(deduped)
    if deduped:
        stats["avg_quality_score"] = round(
            sum(float(record.get("quality_score", 0.0)) for record in deduped) / len(deduped), 4
        )
        stats["avg_grounding_score"] = round(
            sum(float(record.get("grounding_score", 0.0)) for record in deduped) / len(deduped), 4
        )
    else:
        stats["avg_quality_score"] = 0.0
        stats["avg_grounding_score"] = 0.0

    LOGGER.info(
        "Quality enforcement complete. kept=%s dropped=%s stats=%s",
        len(deduped),
        stats["dropped_total"],
        stats,
    )
    return deduped, stats


def save_json(data: Sequence[Dict[str, object]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(list(data), indent=2, ensure_ascii=False), encoding="utf-8")
    LOGGER.info("Saved %s records to %s", len(data), output_path)


def build_rich_dataset(records: Iterable[Dict[str, object]]) -> List[Dict[str, object]]:
    rich_records: List[Dict[str, object]] = []
    for record in records:
        if record.get("is_negative"):
            continue
        messages = _normalize_chat_messages(record)
        payload: Dict[str, object] = {
            "switch": str(record.get("switch", "")).strip(),
            "version": str(record.get("version", "")).strip(),
            "sub_version": str(record.get("sub_version", "")).strip(),
            "source_type": str(record.get("source_type", "")).strip(),
            "category_name": str(record.get("category_name", "")).strip(),
            "bug_id": str(record.get("bug_id", "")).strip(),
            "question": str(record.get("question", "")).strip(),
            "answer": str(record.get("answer", "")).strip(),
            "context": str(record.get("context", "")).strip(),
            "category": str(record.get("category", "overview")).strip() or "overview",
            "tags": list(record.get("tags", [])) if isinstance(record.get("tags"), list) else [],
            "grounding_score": float(record.get("grounding_score", 0.0)),
            "quality_score": float(record.get("quality_score", 0.0)),
        }
        if messages:
            payload["messages"] = [{"role": role, "content": content} for role, content in messages]
        else:
            payload["messages"] = [
                {"role": "user", "content": payload["question"]},
                {"role": "assistant", "content": payload["answer"]},
            ]
        rich_records.append(
            payload
        )
    return rich_records


def _normalize_chat_messages(record: Dict[str, object]) -> List[Tuple[str, str]]:
    messages = record.get("messages", [])
    normalized: List[Tuple[str, str]] = []
    if isinstance(messages, list) and messages:
        for message in messages:
            if not isinstance(message, dict):
                continue
            role = _normalize_text(str(message.get("role", ""))).lower()
            content = _normalize_text(str(message.get("content", "")))
            if not role or not content:
                continue
            normalized.append((role, content))
        if normalized:
            return normalized

    question = _normalize_text(str(record.get("question", "")))
    answer = _normalize_text(str(record.get("answer", "")))
    if question and answer:
        return [("user", question), ("assistant", answer)]
    return []


def _chat_transcript_key(record: Dict[str, object]) -> Tuple[Tuple[str, str], ...]:
    return tuple((role, content.lower()) for role, content in _normalize_chat_messages(record))


def dedupe_chat_transcripts(records: Iterable[Dict[str, object]]) -> Tuple[List[Dict[str, object]], int]:
    """Deduplicate chat records by their full normalized transcript."""
    unique_records: List[Dict[str, object]] = []
    seen = set()
    duplicates_removed = 0
    for record in records:
        if record.get("is_negative"):
            continue
        key = _chat_transcript_key(record)
        if not key:
            continue
        if key in seen:
            duplicates_removed += 1
            continue
        seen.add(key)
        unique_records.append(record)
    return unique_records, duplicates_removed


def _chat_payload(record: Dict[str, object]) -> Dict[str, object]:
    messages = _normalize_chat_messages(record)
    if not messages:
        return {}

    payload = {
        "source_type": str(record.get("source_type", "release_notes_only")).strip() or "release_notes_only",
        "switch": str(record.get("switch", "")).strip(),
        "version": str(record.get("version", "")).strip(),
        "sub_version": str(record.get("sub_version", "")).strip(),
        "messages": [{"role": role, "content": content} for role, content in messages],
    }
    return payload


def write_chat_jsonl(records: Iterable[Dict[str, object]], output_path: Path) -> int:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    seen = set()
    with output_path.open("w", encoding="utf-8") as handle:
        for record in records:
            if record.get("is_negative"):
                continue
            key = _chat_transcript_key(record)
            if not key:
                continue
            if key in seen:
                continue
            seen.add(key)

            payload = _chat_payload(record)
            if not payload:
                continue
            handle.write(json.dumps(payload, ensure_ascii=False) + "\n")
            count += 1
    LOGGER.info("Saved %s JSONL chat rows to %s", count, output_path)
    return count
