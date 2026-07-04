"""QA generation pipeline built on top of LangChain."""

from __future__ import annotations

import json
import logging
import re
from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Sequence

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from tqdm import tqdm

LOGGER = logging.getLogger(__name__)

JSON_BLOCK_RE = re.compile(r"(\[[\s\S]*\]|\{[\s\S]*\})")
SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+")
CATEGORY_RE = re.compile(r"Category:\s*([^;|]+)", re.IGNORECASE)
BUG_ID_RE = re.compile(r"Bug ID:\s*([^;|]+)", re.IGNORECASE)
SYMPTOM_RE = re.compile(r"Symptom\s*:?\s*(.+?)(?:\s+Scenario\s*:|\s+Workaround\s*:|$)", re.IGNORECASE)
SCENARIO_RE = re.compile(r"Scenario\s*:?\s*(.+?)(?:\s+Workaround\s*:|$)", re.IGNORECASE)
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

DEFAULT_TAGS = ["AOS-CX", "release-notes"]
TAG_CANDIDATES = (
    "BGP",
    "OSPF",
    "VLAN",
    "VSX",
    "SNMP",
    "LAG",
    "PTP",
    "PBR",
    "interface",
    "routing",
)

QA_PROMPT = PromptTemplate.from_template(
    """
You create high-quality QA training data for network engineering assistants.

Context:
{context}

Instructions:
- Generate exactly {num_pairs} QA pairs per context.
- Use one question per type: symptom question, trigger/condition question.
- Symptom question -> answer describes only the observable failure in full detail.
- Condition question -> answer must be a complete sentence with a main clause and result.
- Never repeat the symptom as the answer to a condition question.
- Every answer format: "Category (Bug ID X): <one complete sentence>."
- Every answer must have at least 8 meaningful words after the prefix colon.
- Never start an answer with a fragment. Avoid standalone starts like "After X.", "When X.", "During X." without a main clause and result.
- Never end an answer with dangling words like "particularly." or "specifically."
- Never use passive filler phrases: "the issue is observed", "the problem is seen", "the issue occurs in the following".
- Never use connector phrases: "It occurs when", "This results in", "This matters because".
- Never ask "Why is X important for operations?"
- Always include the bug ID in the question. Example: "What symptom occurs in BGP Bug 341596?"
- Preserve all bug IDs, protocol names, and technical terms exactly.
- If a trigger or symptom cannot be determined from context, skip that entry.
- Return valid JSON only. No markdown, no preamble, no outer array.

Required output -- one JSON object per line:
{{"messages": [{{"role": "user", "content": "<question>"}}, {{"role": "assistant", "content": "<answer>"}}]}}
""".strip()
)


@dataclass
class LLMConfig:
    provider: str = "mock"
    model: str = "gpt-4o-mini"
    temperature: float = 0.2
    timeout_seconds: int = 60


def _normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text.replace("\xa0", " ")).strip()


def _extract_field(regex: re.Pattern[str], text: str) -> str:
    match = regex.search(text)
    if not match:
        return ""
    return _normalize_text(match.group(1))


def _shorten(text: str, max_words: int = 34) -> str:
    cleaned = _normalize_text(text).strip(" ;")
    if not cleaned:
        return ""
    parts = cleaned.split()
    if len(parts) <= max_words:
        return cleaned.rstrip(".")
    return " ".join(parts[:max_words]).rstrip(".")


def _structured_parts(context: str) -> Dict[str, str]:
    category = _extract_field(CATEGORY_RE, context)
    bug_id = _extract_field(BUG_ID_RE, context)
    symptom = _shorten(_extract_field(SYMPTOM_RE, context), max_words=72)
    scenario = _shorten(_extract_field(SCENARIO_RE, context), max_words=96)
    return {
        "category": category,
        "bug_id": bug_id,
        "symptom": symptom,
        "scenario": scenario,
    }


def _prefix(category: str, bug_id: str) -> str:
    if category and bug_id:
        return f"{category} (Bug ID {bug_id})"
    if category:
        return category
    if bug_id:
        return f"Issue (Bug ID {bug_id})"
    return "Issue"


def _remove_dangling_tail(text: str) -> str:
    value = _normalize_text(text).rstrip(" .;:,")
    lowered = value.lower()
    for dangling in DANGLING_ENDINGS:
        suffix = f" {dangling}"
        if lowered.endswith(suffix):
            value = value[: -len(suffix)].rstrip(" ,;:")
            lowered = value.lower()
    return value


def _word_count(text: str) -> int:
    return len(re.findall(r"\b[A-Za-z0-9][A-Za-z0-9/-]*\b", text))


def _contains_disallowed_phrase(text: str) -> bool:
    lowered = text.lower()
    return any(phrase in lowered for phrase in DISALLOWED_ANSWER_PHRASES)


def _normalize_trigger_text(text: str) -> str:
    value = _remove_dangling_tail(text).rstrip(".")
    if not value:
        return ""
    lowered = value.lower()
    replacements = [
        ("this issue occurs when ", "when "),
        ("this issue may occur when ", "when "),
        ("this issue can occur when ", "when "),
        ("this issue occurs after ", "after "),
        ("this issue may occur after ", "after "),
        ("this issue is observed during ", "during "),
        ("this issue occurs in ", "in "),
        ("this issue can occur in ", "in "),
        ("this issue occurs in the following workflows: ", "in the following workflows where "),
        ("this issue can occur in the following workflows: ", "in the following workflows where "),
    ]
    for prefix, replacement in replacements:
        if lowered.startswith(prefix):
            return replacement + value[len(prefix) :]
    return value


def _lowercase_sentence_start(text: str) -> str:
    value = _normalize_text(text)
    if not value:
        return ""
    match = re.match(r"^([A-Za-z0-9/-]+)(.*)$", value)
    if not match:
        return value
    first = match.group(1)
    rest = match.group(2)
    if len(first) > 1 and (first.isupper() or first in {"ESXi", "SyncE"}):
        return value
    if len(first) == 1:
        return first.lower() + rest
    return first[0].lower() + first[1:] + rest


def _sentence(text: str) -> str:
    cleaned = _remove_dangling_tail(text)
    if not cleaned:
        return ""
    return f"{cleaned.rstrip('.')}."


def _condition_sentence(trigger: str, symptom: str) -> str:
    trigger_text = _normalize_trigger_text(trigger)
    symptom_text = _remove_dangling_tail(symptom)
    if not trigger_text or not symptom_text:
        return ""
    if CONNECTOR_START_RE.match(trigger_text):
        trigger_text = trigger_text[0].upper() + trigger_text[1:]
        remainder = _lowercase_sentence_start(symptom_text)
        sentence = f"{trigger_text}, {remainder.rstrip('.')}."
    else:
        trigger_low = _lowercase_sentence_start(trigger_text)
        remainder = _lowercase_sentence_start(symptom_text)
        sentence = f"When {trigger_low}, {remainder.rstrip('.')}."
    if _contains_disallowed_phrase(sentence):
        return ""
    return sentence


def _safe_tags(tags: object, context: str, source: str) -> List[str]:
    final_tags = list(DEFAULT_TAGS)
    if isinstance(tags, list):
        final_tags.extend([_normalize_text(str(tag)) for tag in tags if str(tag).strip()])
    ctx_upper = context.upper()
    for candidate in TAG_CANDIDATES:
        if candidate in ctx_upper:
            final_tags.append(candidate)
    final_tags.append(source.replace(".html", ""))
    # stable unique preserving order
    seen = set()
    ordered = []
    for tag in final_tags:
        key = tag.lower()
        if key in seen:
            continue
        seen.add(key)
        ordered.append(tag)
    return ordered[:8]


def _infer_category(context: str) -> str:
    lowered = context.lower()
    if "workaround" in lowered or "limitation" in lowered or "known issue" in lowered:
        return "limitation"
    if "configure" in lowered or "enable" in lowered or "set " in lowered:
        return "configuration"
    if "symptom" in lowered or "error" in lowered or "fails" in lowered:
        return "troubleshooting"
    if "scenario" in lowered or "behavior" in lowered or "when" in lowered:
        return "behavior"
    return "overview"


def _extract_json_object(raw_output: str) -> object:
    try:
        return json.loads(raw_output)
    except json.JSONDecodeError:
        match = JSON_BLOCK_RE.search(raw_output)
        if not match:
            return []
        try:
            return json.loads(match.group(1))
        except json.JSONDecodeError:
            return []


def _extract_message_content(payload: object, role: str) -> str:
    if not isinstance(payload, list):
        return ""
    for item in payload:
        if not isinstance(item, dict):
            continue
        if _normalize_text(str(item.get("role", ""))).lower() != role:
            continue
        content = _normalize_text(str(item.get("content", "")))
        if content:
            return content
    return ""


def _parse_jsonl_objects(raw_output: str) -> List[Dict[str, object]]:
    records: List[Dict[str, object]] = []
    lines = [line.strip() for line in raw_output.splitlines() if line.strip()]
    for line in lines:
        try:
            parsed = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(parsed, dict):
            records.append(parsed)
    return records


def _ensure_pair_list(payload: object) -> List[Dict[str, object]]:
    if isinstance(payload, list):
        return [item for item in payload if isinstance(item, dict)]
    if isinstance(payload, dict):
        if "qa_pairs" in payload and isinstance(payload["qa_pairs"], list):
            return [item for item in payload["qa_pairs"] if isinstance(item, dict)]
        return [payload]
    return []


def _first_sentence(text: str, max_chars: int = 280) -> str:
    sentences = [segment.strip() for segment in SENTENCE_SPLIT_RE.split(text) if segment.strip()]
    if not sentences:
        return text[:max_chars].strip()
    sentence = sentences[0]
    if len(sentence) <= max_chars:
        return sentence
    return sentence[: max_chars - 3].rstrip() + "..."


def _topic_from_context(context: str) -> str:
    category = _extract_field(CATEGORY_RE, context)
    if category:
        return category
    for tag in TAG_CANDIDATES:
        if tag in context.upper():
            return tag
    return "this item"


class QAGenerator:
    """Generates QA pairs row-by-row from cleaned context entries."""

    def __init__(self, config: LLMConfig) -> None:
        self.config = config
        self.model = self._build_model(config)
        self.chain = (QA_PROMPT | self.model | StrOutputParser()) if self.model else None

    @staticmethod
    def _build_model(config: LLMConfig):
        provider = config.provider.lower().strip()
        if provider == "mock":
            LOGGER.warning("Using mock QA generation mode (no external LLM calls).")
            return None

        if provider == "openai":
            try:
                from langchain_openai import ChatOpenAI
            except ImportError as exc:  # pragma: no cover
                raise ImportError("Missing dependency langchain-openai. Install requirements.txt") from exc
            return ChatOpenAI(
                model=config.model,
                temperature=config.temperature,
                timeout=config.timeout_seconds,
            )

        if provider == "ollama":
            try:
                from langchain_ollama import ChatOllama
            except ImportError as exc:  # pragma: no cover
                raise ImportError("Missing dependency langchain-ollama. Install requirements.txt") from exc
            return ChatOllama(
                model=config.model,
                temperature=config.temperature,
                num_predict=384,
            )

        raise ValueError("Unsupported provider. Use one of: mock, openai, ollama")

    def _mock_pairs(self, context: str, source: str, num_pairs: int) -> List[Dict[str, object]]:
        topic = _topic_from_context(context)
        parts = _structured_parts(context)
        category_name = parts["category"] or topic
        bug_id = parts["bug_id"]
        symptom = parts["symptom"] or _first_sentence(context, max_chars=300).rstrip(".")
        scenario = parts["scenario"] or _extract_field(SCENARIO_RE, context)
        category = _infer_category(context)
        if not category_name or not bug_id:
            return []
        display_topic = f"{category_name} Bug {bug_id}"

        templates = [
            f"What symptom occurs in {display_topic}?",
            f"Under what condition does the {display_topic} issue occur?",
        ]

        symptom_sentence = _sentence(symptom)
        condition_sentence = _condition_sentence(_first_sentence(scenario, max_chars=420), symptom)
        if (
            not symptom_sentence
            or _contains_disallowed_phrase(symptom_sentence)
            or _word_count(symptom_sentence) < MIN_MEANINGFUL_WORDS
        ):
            return []
        if not condition_sentence or _word_count(condition_sentence) < MIN_MEANINGFUL_WORDS:
            return []

        pairs: List[Dict[str, object]] = []
        for index in range(num_pairs):
            question = templates[index % len(templates)]
            if index % len(templates) == 0:
                detail = symptom_sentence
            else:
                detail = condition_sentence
            prefix = _prefix(category_name, bug_id)
            answer = f"{prefix}: {detail.rstrip('.')}."
            answer = answer.replace("  ", " ")
            pairs.append(
                {
                    "question": question,
                    "answer": answer,
                    "category": category,
                    "tags": _safe_tags([], context, source),
                }
            )
        return pairs

    def _llm_pairs(self, context: str, source: str, num_pairs: int) -> List[Dict[str, object]]:
        if not self.chain:
            return []

        raw_output = self.chain.invoke({"context": context, "num_pairs": num_pairs})
        candidates = _parse_jsonl_objects(raw_output)
        if not candidates:
            parsed_payload = _extract_json_object(raw_output)
            candidates = _ensure_pair_list(parsed_payload)

        normalized: List[Dict[str, object]] = []
        for candidate in candidates:
            question = ""
            answer = ""

            if isinstance(candidate, dict) and isinstance(candidate.get("messages"), list):
                question = _extract_message_content(candidate.get("messages"), "user")
                answer = _extract_message_content(candidate.get("messages"), "assistant")
            else:
                question = _normalize_text(str(candidate.get("question", "")))
                answer = _normalize_text(str(candidate.get("answer", "")))

            if not question or not answer:
                continue
            category = _normalize_text(str(candidate.get("category", ""))).lower() or _infer_category(context)
            tags = _safe_tags(candidate.get("tags", []), context, source)
            normalized.append(
                {
                    "question": question,
                    "answer": answer,
                    "category": category,
                    "tags": tags,
                }
            )
        return normalized[:num_pairs]

    def generate_for_entry(self, entry: Dict[str, str], num_pairs: int = 2) -> List[Dict[str, object]]:
        context = _normalize_text(entry["context"])
        source = entry["source"]
        source_path = str(entry.get("source_path", "")).strip()
        version = str(entry.get("version", "")).strip()
        sub_version = str(entry.get("sub_version", "")).strip()
        content_type = entry.get("type", "paragraph")

        generated: List[Dict[str, object]]
        if self.chain:
            generated = self._llm_pairs(context, source, num_pairs=num_pairs)
            if not generated:
                LOGGER.warning("LLM QA generation failed for %s. Falling back to mock mode.", source)
                generated = self._mock_pairs(context, source, num_pairs=num_pairs)
        else:
            generated = self._mock_pairs(context, source, num_pairs=num_pairs)

        output: List[Dict[str, object]] = []
        for pair in generated:
            output.append(
                {
                    "question": pair["question"],
                    "answer": pair["answer"],
                    "context": context,
                    "category": pair.get("category", _infer_category(context)),
                    "tags": pair.get("tags", _safe_tags([], context, source)),
                    "source": source,
                    "source_path": source_path,
                    "type": content_type,
                    "version": version,
                    "sub_version": sub_version,
                }
            )
        return output

    def generate(
        self,
        entries: Sequence[Dict[str, str]],
        num_pairs_per_context: int = 2,
        max_contexts: Optional[int] = None,
    ) -> List[Dict[str, object]]:
        if max_contexts:
            entries = entries[:max_contexts]

        qa_records: List[Dict[str, object]] = []
        for entry in tqdm(entries, desc="Generating QA", unit="context"):
            try:
                qa_records.extend(self.generate_for_entry(entry, num_pairs=num_pairs_per_context))
            except Exception as exc:  # pylint: disable=broad-except
                LOGGER.exception("Failed QA generation for source=%s: %s", entry.get("source"), exc)
        LOGGER.info("Generated %s QA records from %s contexts.", len(qa_records), len(entries))
        return self._deduplicate(qa_records)

    @staticmethod
    def _deduplicate(records: Iterable[Dict[str, object]]) -> List[Dict[str, object]]:
        seen = set()
        deduped: List[Dict[str, object]] = []
        for record in records:
            key = (
                str(record.get("question", "")).lower().strip(),
                str(record.get("answer", "")).lower().strip(),
                str(record.get("context", "")).lower().strip(),
            )
            if key in seen:
                continue
            seen.add(key)
            deduped.append(record)
        return deduped
