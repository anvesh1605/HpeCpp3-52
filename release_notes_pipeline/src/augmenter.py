"""Data augmentation for QA pairs."""

from __future__ import annotations

import logging
import random
import re
from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from tqdm import tqdm

try:
    from .qa_generator import LLMConfig
except ImportError:  # pragma: no cover
    from qa_generator import LLMConfig

LOGGER = logging.getLogger(__name__)

PARAPHRASE_PROMPT = PromptTemplate.from_template(
    """
Paraphrase this question without changing factual meaning.
Keep it concise and natural.
Return only the rewritten question.

Question: {question}
Context: {context}
""".strip()
)

FOLLOW_UP_PROMPT = PromptTemplate.from_template(
    """
Create one short follow-up user question for this QA pair.
It should be context-aware and suitable for a multi-turn chat.
Return only the question.

Question: {question}
Answer: {answer}
Context: {context}
""".strip()
)


@dataclass
class AugmentationConfig:
    include_negative: bool = False
    include_multiturn: bool = False
    seed: int = 42


def _normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.replace("\xa0", " ")).strip()


def _normalize_question(text: str) -> str:
    question = _normalize(text)
    question = re.sub(r"[.?!\s]+$", "", question)
    return f"{question}?" if question else question


class DataAugmenter:
    """Augments QA pairs with paraphrases, variations, and optional negatives/multi-turn."""

    def __init__(self, llm_config: LLMConfig, aug_config: AugmentationConfig) -> None:
        self.llm_config = llm_config
        self.aug_config = aug_config
        self.random = random.Random(aug_config.seed)
        self.model = self._build_model(llm_config)
        self.paraphrase_chain = (PARAPHRASE_PROMPT | self.model | StrOutputParser()) if self.model else None
        self.followup_chain = (FOLLOW_UP_PROMPT | self.model | StrOutputParser()) if self.model else None

    @staticmethod
    def _build_model(config: LLMConfig):
        provider = config.provider.lower().strip()
        if provider == "mock":
            return None
        if provider == "openai":
            from langchain_openai import ChatOpenAI

            return ChatOpenAI(
                model=config.model,
                temperature=max(0.0, min(config.temperature, 0.4)),
                timeout=config.timeout_seconds,
            )
        if provider == "ollama":
            from langchain_ollama import ChatOllama

            return ChatOllama(model=config.model, temperature=max(0.0, min(config.temperature, 0.4)))
        return None

    @staticmethod
    def _rule_paraphrase(question: str) -> str:
        behavior_match = re.match(r"^How is (.+) described in this note\??$", question, flags=re.IGNORECASE)
        if behavior_match:
            return _normalize_question(f"Explain {behavior_match.group(1)} in this note")

        replacements = [
            (r"^What is\b", "Explain"),
            (r"^What are\b", "Explain"),
            (r"^What happens\b", "Describe behavior when"),
            (r"^How does\b", "Explain how"),
            (r"^How is\b", "Describe"),
            (r"^Why does\b", "Explain why"),
            (r"^Why is\b", "What is the reason"),
        ]
        rewritten = question
        for pattern, replacement in replacements:
            rewritten = re.sub(pattern, replacement, rewritten, flags=re.IGNORECASE)
        if rewritten == question:
            rewritten = f"Can you explain: {question[0].lower() + question[1:]}" if question else question
        return _normalize_question(rewritten)

    @staticmethod
    def _question_variation(question: str) -> str:
        variation = question.strip()
        if not variation:
            return variation

        behavior_match = re.match(r"^How is (.+) described in this note\??$", variation, flags=re.IGNORECASE)
        if behavior_match:
            variation = f"Describe {behavior_match.group(1)} in this note."
        elif re.match(r"^What is\b", variation, flags=re.IGNORECASE):
            variation = re.sub(r"^What is\b", "Explain", variation, flags=re.IGNORECASE)
        elif re.match(r"^What happens\b", variation, flags=re.IGNORECASE):
            variation = re.sub(r"^What happens\b", "Describe behavior when", variation, flags=re.IGNORECASE)
        elif re.match(r"^Why is\b", variation, flags=re.IGNORECASE):
            variation = re.sub(r"^Why is\b", "Explain why", variation, flags=re.IGNORECASE)
        elif re.match(r"^How does\b", variation, flags=re.IGNORECASE):
            variation = re.sub(r"^How does\b", "Explain how", variation, flags=re.IGNORECASE)
        else:
            variation = f"Please explain {question[0].lower() + question[1:]}"
        return _normalize_question(variation)

    def _paraphrase(self, question: str, context: str) -> str:
        if self.paraphrase_chain:
            try:
                rewritten = self.paraphrase_chain.invoke({"question": question, "context": context})
                rewritten = _normalize(rewritten)
                if rewritten:
                    return _normalize_question(rewritten)
            except Exception as exc:  # pylint: disable=broad-except
                LOGGER.warning("Paraphrase LLM failed, using rule-based fallback: %s", exc)
        return self._rule_paraphrase(question)

    def _follow_up_question(self, question: str, answer: str, context: str) -> str:
        if self.followup_chain:
            try:
                followup = self.followup_chain.invoke(
                    {"question": question, "answer": answer, "context": context}
                )
                followup = _normalize(followup)
                if followup:
                    return _normalize_question(followup)
            except Exception as exc:  # pylint: disable=broad-except
                LOGGER.warning("Follow-up LLM failed, using fallback: %s", exc)
        return _normalize_question("Can you summarize the practical impact of this behavior")

    def _negative_samples(self, records: Sequence[Dict[str, object]]) -> List[Dict[str, object]]:
        if len(records) < 2:
            return []
        negatives: List[Dict[str, object]] = []
        answers = [str(record.get("answer", "")) for record in records if record.get("answer")]
        for record in records:
            question = str(record.get("question", ""))
            answer = str(record.get("answer", ""))
            if not question or not answer:
                continue
            candidate_answers = [candidate for candidate in answers if candidate != answer]
            if not candidate_answers:
                continue
            wrong_answer = self.random.choice(candidate_answers)
            negatives.append(
                {
                    **record,
                    "answer": wrong_answer,
                    "is_negative": True,
                    "augmentation_type": "negative_sample",
                }
            )
        return negatives

    @staticmethod
    def _dedupe(records: Iterable[Dict[str, object]]) -> List[Dict[str, object]]:
        seen = set()
        unique: List[Dict[str, object]] = []
        for record in records:
            key = (
                str(record.get("question", "")).lower().strip(),
                str(record.get("answer", "")).lower().strip(),
                bool(record.get("is_negative", False)),
            )
            if key in seen:
                continue
            seen.add(key)
            unique.append(record)
        return unique

    def augment(
        self,
        qa_records: Sequence[Dict[str, object]],
    ) -> Tuple[List[Dict[str, object]], List[Dict[str, object]], List[Dict[str, object]]]:
        positives: List[Dict[str, object]] = []
        multiturn_records: List[Dict[str, object]] = []

        for record in tqdm(qa_records, desc="Augmenting QA", unit="pair"):
            question = _normalize(str(record.get("question", "")))
            answer = _normalize(str(record.get("answer", "")))
            context = _normalize(str(record.get("context", "")))
            if not question or not answer:
                continue

            base = {**record, "question": question, "answer": answer, "context": context, "is_negative": False}
            base["augmentation_type"] = "original"
            positives.append(base)

            paraphrased_question = self._paraphrase(question, context)
            if paraphrased_question.lower() != question.lower():
                positives.append(
                    {
                        **base,
                        "question": paraphrased_question,
                        "augmentation_type": "paraphrase",
                    }
                )

            varied_question = self._question_variation(question)
            if varied_question.lower() not in {question.lower(), paraphrased_question.lower()}:
                positives.append(
                    {
                        **base,
                        "question": varied_question,
                        "augmentation_type": "question_variation",
                    }
                )

            if self.aug_config.include_multiturn:
                followup_question = self._follow_up_question(question, answer, context)
                multiturn_records.append(
                    {
                        "source_type": "release_notes_only_multiturn",
                        "messages": [
                            {"role": "user", "content": question},
                            {"role": "assistant", "content": answer},
                            {"role": "user", "content": followup_question},
                            {"role": "assistant", "content": answer},
                        ],
                        "version": record.get("version", ""),
                        "sub_version": record.get("sub_version", ""),
                        "source": record.get("source", ""),
                        "category": record.get("category", "overview"),
                        "tags": record.get("tags", []),
                    }
                )

        positives = self._dedupe(positives)
        negatives = self._negative_samples(positives) if self.aug_config.include_negative else []
        negatives = self._dedupe(negatives)
        LOGGER.info(
            "Augmentation complete: %s positives, %s negatives, %s multi-turn records",
            len(positives),
            len(negatives),
            len(multiturn_records),
        )
        return positives, negatives, multiturn_records
