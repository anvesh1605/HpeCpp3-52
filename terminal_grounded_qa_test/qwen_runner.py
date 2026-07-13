from __future__ import annotations

import re
from pathlib import Path
from typing import Optional

import torch

try:
    from .config import QWEN_MAX_NEW_TOKENS, QWEN_MODEL_PATH
    from .entity_extract import normalize_whitespace
except ImportError:  # pragma: no cover
    from config import QWEN_MAX_NEW_TOKENS, QWEN_MODEL_PATH
    from entity_extract import normalize_whitespace


SYSTEM_PROMPT = """You are a concise Aruba AOS-CX assistant.
Rewrite the provided target_value into a clean final answer.
Use bullet points.
Use only the given target_value.
Do not add extra facts.
Do not hallucinate.
Do not over-explain.
"""

GENERAL_SYSTEM_PROMPT = """You are a fine-tuned Aruba AOS-CX assistant.
Answer from your learned knowledge.
Be clear and concise.
"""

_GROUNDING_LABELS = (
    "Feature Caveat",
    "Known Issue",
    "Symptom",
    "Scenario",
    "Workaround",
    "Cause",
    "Fix",
    "Note",
    "Limitation",
    "Requirement",
    "Impact",
    "Resolution",
    "Feature",
)


_STRUCTURED_LABEL_HEADS = {
    "feature",
    "known",
    "symptom",
    "scenario",
    "workaround",
    "cause",
    "fix",
    "note",
    "limitation",
    "requirement",
    "impact",
    "resolution",
}


def _strip_bullet_prefix_v2(value: str) -> str:
    return re.sub(r"^[\s\-\*\u2022\d\.\)]+", "", normalize_whitespace(value)).strip()


def _is_structured_heading_v2(line: str) -> bool:
    normalized = normalize_whitespace(line).rstrip(":").strip()
    if not normalized:
        return False
    return normalized.lower() in {label.lower() for label in _GROUNDING_LABELS}


def _merge_structured_lines_v2(lines: list[str]) -> list[str]:
    merged: list[str] = []
    index = 0
    while index < len(lines):
        current = lines[index].strip()
        if not current:
            index += 1
            continue

        next_line = lines[index + 1].strip() if index + 1 < len(lines) else ""
        current_lower = current.lower().rstrip(":")
        next_lower = next_line.lower()

        if current_lower == "feature" and next_lower.startswith("caveat:"):
            merged.append(f"Feature Caveat: {next_line.split(':', 1)[1].strip()}")
            index += 2
            continue
        if current_lower == "known" and next_lower.startswith("issue:"):
            merged.append(f"Known Issue: {next_line.split(':', 1)[1].strip()}")
            index += 2
            continue

        if current_lower in _STRUCTURED_LABEL_HEADS and next_line and not _is_structured_heading_v2(next_line):
            merged.append(f"{current.rstrip(':')}: {next_line}")
            index += 2
            continue

        merged.append(current)
        index += 1
    return merged


def _split_label_segments_v2(text: str) -> list[str]:
    normalized = normalize_whitespace(text)
    if not normalized:
        return []
    label_pattern = "|".join(sorted((re.escape(label) for label in _GROUNDING_LABELS), key=len, reverse=True))
    matches = list(re.finditer(rf"(?i)(?:^|\s)(?:{label_pattern})\s*:\s*", normalized))
    if not matches:
        return []
    segments: list[str] = []
    for index, match in enumerate(matches):
        label = normalize_whitespace(match.group(0)).rstrip(":").strip()
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(normalized)
        value = normalize_whitespace(normalized[start:end]).strip(" ;-")
        segment = f"{label}: {value}" if value else label
        segments.append(segment)
    return [segment for segment in segments if segment]


def _strip_bullet_prefix(value: str) -> str:
    return re.sub(r"^[\s\-\*•\d\.\)]+", "", normalize_whitespace(value)).strip()


def _split_label_segments(text: str) -> list[str]:
    normalized = normalize_whitespace(text)
    if not normalized:
        return []
    label_pattern = "|".join(sorted((re.escape(label) for label in _GROUNDING_LABELS), key=len, reverse=True))
    matches = list(re.finditer(rf"(?i)(?:^|\s)(?:{label_pattern})\s*:\s*", normalized))
    if not matches:
        return []
    segments: list[str] = []
    for index, match in enumerate(matches):
        label = normalize_whitespace(match.group(0)).rstrip(":").strip()
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(normalized)
        value = normalize_whitespace(normalized[start:end]).strip(" ;-")
        segment = f"{label}: {value}" if value else label
        segments.append(segment)
    return [segment for segment in segments if segment]


def _split_inline_list_items(text: str) -> list[str]:
    normalized = normalize_whitespace(text)
    if normalized.count(" - ") < 2:
        return [normalized]
    parts = [part.strip() for part in re.split(r"\s+-\s+", normalized) if part.strip()]
    if len(parts) < 2:
        return [normalized]
    return parts


def format_grounded_answer_text(text: str) -> str:
    normalized = normalize_whitespace(text)
    if not normalized:
        return normalized

    raw_lines = [line.strip() for line in str(text).splitlines() if line.strip()]
    if not raw_lines:
        raw_lines = [normalized]

    cleaned_lines = [_strip_bullet_prefix_v2(line) for line in raw_lines]
    cleaned_lines = [line for line in cleaned_lines if line]
    structured: list[str] = []
    for line in _merge_structured_lines_v2(cleaned_lines):
        segments = _split_label_segments_v2(line)
        if segments:
            for segment in segments:
                structured.extend(_split_inline_list_items(segment))
        else:
            structured.extend(_split_inline_list_items(line))

    seen: set[str] = set()
    bullets: list[str] = []
    for segment in structured:
        cleaned = normalize_whitespace(segment)
        if not cleaned:
            continue
        key = cleaned.lower()
        if key in seen:
            continue
        seen.add(key)
        bullets.append(f"- {cleaned}")
    return "\n".join(bullets) if bullets else f"- {normalized}"


class QwenFormatter:
    def __init__(self, model_path: Path = QWEN_MODEL_PATH) -> None:
        self.model_path = model_path
        self._tokenizer = None
        self._model = None
        self._load_error: Optional[str] = None

    @property
    def available(self) -> bool:
        return self._load_error is None and self.model_path.exists()

    def _lazy_load(self) -> None:
        if self._tokenizer is not None and self._model is not None:
            return
        if self._load_error is not None:
            raise RuntimeError(self._load_error)
        try:
            from transformers import AutoModelForCausalLM, AutoTokenizer
        except ModuleNotFoundError as exc:
            self._load_error = "transformers is not installed. Run: pip install transformers accelerate sentencepiece"
            raise RuntimeError(self._load_error) from exc
        try:
            self._tokenizer = AutoTokenizer.from_pretrained(self.model_path, trust_remote_code=True, use_fast=True)
            if self._tokenizer.pad_token is None:
                self._tokenizer.pad_token = self._tokenizer.eos_token or self._tokenizer.unk_token
            self._model = AutoModelForCausalLM.from_pretrained(
                self.model_path,
                trust_remote_code=True,
                torch_dtype="auto",
                device_map="auto",
            )
            self._model.eval()
        except Exception as exc:  # pragma: no cover
            self._load_error = f"Failed to load Qwen model: {exc}"
            raise RuntimeError(self._load_error) from exc

    def _encode_prompt(self, system_prompt: str, user_prompt: str) -> torch.Tensor:
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]
        if hasattr(self._tokenizer, "apply_chat_template"):
            encoded = self._tokenizer.apply_chat_template(
                messages,
                add_generation_prompt=True,
                tokenize=True,
                return_tensors="pt",
            )
            if hasattr(encoded, "input_ids"):
                return encoded.input_ids
            return encoded
        return self._tokenizer(f"{system_prompt}\n\n{user_prompt}", return_tensors="pt").input_ids

    def _generate_text(self, system_prompt: str, user_prompt: str) -> str:
        self._lazy_load()
        encoded = self._encode_prompt(system_prompt, user_prompt)
        device = getattr(self._model, "device", None)
        if device is not None and str(device) != "cpu":
            encoded = encoded.to(device)
        with torch.inference_mode():
            outputs = self._model.generate(
                encoded,
                max_new_tokens=QWEN_MAX_NEW_TOKENS,
                do_sample=False,
                pad_token_id=self._tokenizer.pad_token_id,
                eos_token_id=self._tokenizer.eos_token_id,
            )
        new_tokens = outputs[0][encoded.shape[-1]:]
        return normalize_whitespace(self._tokenizer.decode(new_tokens, skip_special_tokens=True))

    @staticmethod
    def _critical_tokens(text: str) -> set[str]:
        normalized = normalize_whitespace(text)
        tokens = set()
        tokens.update(re.findall(r"\b\d+\.\d+(?:\.\d+)?\b", normalized))
        tokens.update(re.findall(r"\b\d+\b", normalized))
        tokens.update(match.lower() for match in re.findall(r"\bBug(?:\s+ID)?\s+\d+\b", normalized, flags=re.IGNORECASE))
        tokens.update(
            token.lower()
            for token in re.findall(r"\b(?:[A-Z]{2,}[A-Z0-9_-]*|[A-Za-z]*\d+[A-Za-z0-9_-]*)\b", normalized)
            if len(token) >= 3
        )
        return {token for token in tokens if token}

    def validate(self, original: str, formatted: str) -> bool:
        left = self._critical_tokens(original)
        right_text = normalize_whitespace(formatted).lower()
        missing = [token for token in left if token.lower() not in right_text]
        if missing:
            return False
        left_words = set(re.findall(r"[A-Za-z0-9_]+", normalize_whitespace(original).lower()))
        right_words = set(re.findall(r"[A-Za-z0-9_]+", normalize_whitespace(formatted).lower()))
        if not left_words:
            return True
        overlap = len(left_words & right_words) / max(1, len(left_words))
        return overlap >= 0.45

    def format_grounded_answer(self, question: str, grounded_answer: str) -> str:
        answer = normalize_whitespace(grounded_answer)
        if not answer:
            return answer
        prompt = (
            f"Question: {question}\n\n"
            f"Target value:\n{grounded_answer}\n\n"
            "Instruction:\n"
            "Answer the question using the target_value.\n"
            "Format the answer in bullet points.\n"
            "Keep compound labels together, such as Feature Caveat or Known Issue.\n"
            "If the target_value contains Symptom, Scenario, Workaround, Cause, or Fix, make them separate bullets.\n"
            "Keep the answer short and clear."
        )
        formatted = self._generate_text(SYSTEM_PROMPT, prompt)
        candidate = formatted if formatted and self.validate(grounded_answer, formatted) else answer
        return format_grounded_answer_text(candidate)

    def format_conversational_answer(self, question: str, grounded_answer: str) -> str:
        return self.format_grounded_answer(question, grounded_answer)

    def answer_general(self, question: str) -> str:
        try:
            return self._generate_text(GENERAL_SYSTEM_PROMPT, question)
        except Exception:
            return ""
