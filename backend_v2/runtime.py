from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import re
from typing import Any, Dict, Optional
from uuid import uuid4

import torch

from backend_v2.config import (
    BACKEND_CACHE_DIR,
    DATA_ROOT,
    FRONTEND_DIR,
    MODEL_ROOT,
    PRODUCT_LSTM_MODEL_PATH,
    RELEASE_LSTM_MODEL_PATH,
)
from terminal_grounded_qa_test.entity_extract import normalize_switch_name, normalize_whitespace
from terminal_grounded_qa_test.terminal_grounded_qa import TerminalGroundedQA, switch_from_question
from terminal_grounded_qa_test.qwen_runner import format_grounded_answer_text


def _clean(value: object) -> str:
    return normalize_whitespace(value)


_GROUNDING_NOISE_TOKENS = {
    "answer",
    "answers",
    "bullet",
    "bullets",
    "cause",
    "causes",
    "cav",
    "details",
    "description",
    "feature",
    "fix",
    "note",
    "notes",
    "scenario",
    "scenarios",
    "symptom",
    "symptoms",
    "target",
    "value",
    "workaround",
}


def _token_set(text: object) -> set[str]:
    return {
        token.lower()
        for token in re.findall(r"[A-Za-z0-9_./:-]+", normalize_whitespace(text))
        if token
    }


def _bulletize_text(text: object) -> str:
    normalized = normalize_whitespace(text)
    if not normalized:
        return normalized
    raw_lines = [line.strip() for line in str(text).splitlines() if line.strip()]
    if len(raw_lines) <= 1:
        return f"- {normalized}"
    bullets = []
    for line in raw_lines:
        cleaned = normalize_whitespace(line)
        bullets.append(f"- {cleaned}")
    return "\n".join(bullets)


def _strip_leading_markup(value: object) -> str:
    return re.sub(r"^[\s\-\*\d\.\)]+", "", normalize_whitespace(value)).strip()


def _bulletize_text_safe(text: object) -> str:
    normalized = normalize_whitespace(text)
    if not normalized:
        return normalized
    raw_lines = [line.strip() for line in str(text).splitlines() if line.strip()]
    if len(raw_lines) <= 1:
        return f"- {_strip_leading_markup(normalized)}"
    return "\n".join(f"- {_strip_leading_markup(line)}" for line in raw_lines)


def _is_grounded_rewrite_clean(question: str, target_value: object, final_answer: object) -> bool:
    target_tokens = _token_set(target_value)
    answer_tokens = _token_set(final_answer)
    if not target_tokens or not answer_tokens:
        return False

    question_tokens = _token_set(question)
    extra_tokens = {
        token
        for token in answer_tokens - target_tokens
        if token not in question_tokens and token not in _GROUNDING_NOISE_TOKENS
    }
    if not extra_tokens:
        return True

    overlap = len(target_tokens & answer_tokens) / max(1, len(target_tokens))
    if overlap >= 0.85 and len(extra_tokens) <= 1:
        return True
    return False


@dataclass
class AnswerService:
    qa: TerminalGroundedQA
    sessions: Dict[str, Dict[str, Any]] = field(default_factory=dict)

    @classmethod
    def create(cls, device: Optional[torch.device] = None) -> "AnswerService":
        _ = device  # kept for API compatibility with the existing backend factory
        return cls(qa=TerminalGroundedQA())

    @property
    def device(self) -> torch.device:
        return self.qa.device

    def new_session_id(self) -> str:
        return uuid4().hex

    def _session(self, session_id: str) -> Dict[str, Any]:
        if session_id not in self.sessions:
            self.sessions[session_id] = {
                "selected_switch": "",
                "selected_version": "",
                "selected_sub_version": "",
                "domain": "auto",
                "last_question": "",
                "last_answer_mode": "",
                "last_lookup_status": "",
            }
        return self.sessions[session_id]

    def chat(
        self,
        question: str,
        session_id: Optional[str] = None,
        domain: str = "auto",
        selected_switch: str = "",
        selected_version: str = "",
        selected_sub_version: str = "",
        show_debug: bool = False,
    ) -> Dict[str, object]:
        _ = show_debug  # terminal QA already returns rich diagnostics; keep the signature stable
        session_id = session_id or self.new_session_id()
        session = self._session(session_id)

        effective_switch = normalize_switch_name(selected_switch or session.get("selected_switch", ""))
        question_switch = switch_from_question(question, effective_switch or "")
        auto_switched = bool(question_switch and question_switch != effective_switch)
        if question_switch:
            effective_switch = question_switch

        result = self.qa.answer(question, effective_switch)
        if result.get("answer_mode") == "grounded_qwen":
            raw_final_answer = result.get("final_answer", "")
            target_value = result.get("target_value", "")
            if raw_final_answer and target_value:
                if _is_grounded_rewrite_clean(question, target_value, raw_final_answer):
                    cleaned_final_answer = format_grounded_answer_text(raw_final_answer)
                else:
                    cleaned_final_answer = format_grounded_answer_text(target_value)
                    result = {
                        **result,
                        "debug": {
                            **(result.get("debug", {}) if isinstance(result.get("debug", {}), dict) else {}),
                            "grounded_qwen_sanitized": True,
                            "grounded_qwen_raw_answer": raw_final_answer,
                        },
                    }
                if cleaned_final_answer:
                    result = {**result, "final_answer": cleaned_final_answer}
        resolved_domain = str(result.get("predicted_source") or "").strip() or (_clean(domain) if _clean(domain) in {"release", "product"} else "auto")

        session.update(
            {
                "selected_switch": effective_switch,
                "selected_version": _clean(selected_version or session.get("selected_version", "")),
                "selected_sub_version": _clean(selected_sub_version or session.get("selected_sub_version", "")),
                "domain": resolved_domain,
                "last_question": question,
                "last_answer_mode": result.get("answer_mode", ""),
                "last_lookup_status": result.get("lookup_status", ""),
                "last_selected_switch_auto_switched": auto_switched,
            }
        )

        debug = {
            "model_votes": result.get("model_votes", {}),
            "extracted_entities": result.get("extracted_entities", {}),
            "top_candidates": result.get("top_candidates", []),
            "switch_auto_switched": auto_switched,
            "session": {
                "selected_switch": effective_switch,
                "selected_version": session.get("selected_version", ""),
                "selected_sub_version": session.get("selected_sub_version", ""),
                "domain": resolved_domain,
            },
        }

        response: Dict[str, object] = {
            "session_id": session_id,
            "conversation_id": session_id,
            "domain": resolved_domain,
            "requested_domain": _clean(domain) or "auto",
            "selected_switch": effective_switch,
            "selected_version": session.get("selected_version", ""),
            "selected_sub_version": session.get("selected_sub_version", ""),
            "question": question,
            "predicted_source": result.get("predicted_source"),
            "predicted_intent": result.get("predicted_intent"),
            "predicted_confidence": result.get("predicted_confidence"),
            "raw_lstm_intent": result.get("raw_lstm_intent"),
            "model_votes": result.get("model_votes", {}),
            "slots": result.get("extracted_entities", {}),
            "extracted_entities": result.get("extracted_entities", {}),
            "lookup_context": result.get("lookup_context"),
            "answer_mode": result.get("answer_mode"),
            "grounded": result.get("grounded"),
            "target_value_used": result.get("target_value_used"),
            "matched_dataset_row": result.get("matched_dataset_row"),
            "target_value": result.get("target_value"),
            "final_answer": result.get("final_answer"),
            "lookup_status": result.get("lookup_status"),
            "lookup_score": result.get("lookup_score"),
            "top_candidates": result.get("top_candidates", []),
            "bypass_qwen": result.get("bypass_qwen"),
            "qwen_loaded": self.qa.qwen.available,
            "qwen_model_path": str(self.qa.qwen.model_path),
            "qwen_error": getattr(self.qa.qwen, "_load_error", None),
            "debug": debug,
            "answer_source": result.get("predicted_source"),
            "source_type": result.get("predicted_source"),
            "data_family": result.get("predicted_source"),
            "confidence": result.get("predicted_confidence"),
            "similarity": result.get("lookup_score"),
        }
        return response

    def health(self) -> Dict[str, object]:
        qwen_error = getattr(self.qa.qwen, "_load_error", None)
        return {
            "device": str(self.device),
            "qwen_loaded": self.qa.qwen.available,
            "qwen_model_path": str(self.qa.qwen.model_path),
            "qwen_error": qwen_error or None,
            "release_lstm_path": str(RELEASE_LSTM_MODEL_PATH),
            "product_lstm_path": str(PRODUCT_LSTM_MODEL_PATH),
            "model_root": str(MODEL_ROOT),
            "data_root": str(DATA_ROOT),
            "frontend_dir": str(FRONTEND_DIR),
            "backend_cache_dir": str(BACKEND_CACHE_DIR),
            "release_rows": len([row for row in self.qa.rows if getattr(row, "source", "") == "release"]),
            "product_rows": len([row for row in self.qa.rows if getattr(row, "source", "") == "product"]),
            "synthetic_rows": len([row for row in self.qa.rows if getattr(row, "source", "") == "synthetic"]),
        }


