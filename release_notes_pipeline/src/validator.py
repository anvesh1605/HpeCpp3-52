"""Minimal answer-level validation rules used by formatter quality checks."""

from __future__ import annotations

import re
from typing import Tuple

PASS = "pass"
FAIL = "fail"

INVISIBLE_CONTENT_RE = re.compile(r"scenario:\s*\d|shown below|figure\s+\d|table\s+\d", re.IGNORECASE)
VAGUE_CONDITION_PATTERNS = (
    "when this issue occurs",
    "when this issue is observed",
    "when this issue can",
)


def validate_answer(answer: str, answer_type: str) -> Tuple[str, str]:
    """Validate answer text with strict minimal reject rules."""
    if INVISIBLE_CONTENT_RE.search(answer):
        return FAIL, "references non-text content"

    if answer_type == "condition" and any(pattern in answer.lower() for pattern in VAGUE_CONDITION_PATTERNS):
        return FAIL, "no actionable trigger detail"

    return PASS, ""
