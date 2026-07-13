from __future__ import annotations

import re
from typing import Dict, List

try:
    from .config import ALLOWED_SWITCH_FAMILIES
except ImportError:  # pragma: no cover
    from config import ALLOWED_SWITCH_FAMILIES


def normalize_whitespace(text: object) -> str:
    if text is None:
        return ""
    return re.sub(r"\s+", " ", str(text)).strip()


def normalize_switch_name(value: str) -> str:
    cleaned = normalize_whitespace(value)
    if not cleaned:
        return ""
    lowered = cleaned.lower()
    for candidate in sorted(ALLOWED_SWITCH_FAMILIES, key=len, reverse=True):
        if lowered == candidate.lower():
            return candidate
    return cleaned


def extract_switch_candidates(question: str) -> List[str]:
    text = normalize_whitespace(question)
    lowered = text.lower()
    matches: List[str] = []
    for candidate in sorted(ALLOWED_SWITCH_FAMILIES, key=len, reverse=True):
        pattern = re.escape(candidate.lower())
        if re.search(rf"(?<![A-Za-z0-9_]){pattern}(?![A-Za-z0-9_])", lowered):
            matches.append(candidate)
    generic_matches = re.findall(r"\b(?:Aruba\s+)?(\d{4,5}[A-Za-z]?)\b", text, flags=re.IGNORECASE)
    for item in generic_matches:
        normalized = normalize_switch_name(item)
        if normalized in ALLOWED_SWITCH_FAMILIES and normalized not in matches:
            matches.append(normalized)
    return matches


def extract_version(question: str) -> Dict[str, str]:
    text = normalize_whitespace(question)
    match = re.search(
        r"\bAOS-CX\s+(\d+\.\d+)(?:\.(\d+))?\b|\bAOS-CX\s+(\d+_\d+)(?:_(\d+))?\b",
        text,
        flags=re.IGNORECASE,
    )
    if not match:
        return {}
    major_minor = match.group(1) or (match.group(3) or "").replace("_", ".")
    sub_version = match.group(2) or match.group(4) or ""
    version = major_minor
    version_full = f"{major_minor}.{sub_version}" if sub_version else major_minor
    return {
        "version": version,
        "sub_version": sub_version,
        "version_full": version_full,
    }


def extract_bug_id(question: str) -> str:
    text = normalize_whitespace(question)
    match = re.search(r"\bBug(?:\s+ID)?\s+(\d{4,7})\b", text, flags=re.IGNORECASE)
    return match.group(1) if match else ""


def extract_command(question: str) -> str:
    text = normalize_whitespace(question)
    patterns = [
        r"\bsyntax\s+of\s+the\s+(.+?)\s+command\b",
        r"\bwhat\s+does\s+the\s+(.+?)\s+command\s+do\b",
        r"\boutput\s+of\s+the\s+(.+?)\s+command\b",
        r"\bcommand\s+syntax\s+is\s+listed\s+for\s+(.+?)(?:\s+on\s+|\?)",
        r"\bcli\s+syntax\s+for\s+(.+?)(?:\s+in\s+|\?)",
        r"\bshow\s+me\s+the\s+output\s+of\s+(.+?)(?:\s+command|\?)",
        r"\bhow\s+(?:can|do)\s+i\s+(.+?)(?:\?|$)",
        r"\bhow\s+(?:can|do)\s+you\s+(.+?)(?:\?|$)",
    ]
    for pattern in patterns:
        match = re.search(pattern, text, flags=re.IGNORECASE)
        if match:
            command = normalize_whitespace(match.group(1)).strip("`'\" ")
            command = re.sub(r"^(?:check|view|display|see)\s+", "", command, flags=re.IGNORECASE).strip()
            command = re.sub(r"\bdetails\b$", "", command, flags=re.IGNORECASE).strip()
            return re.sub(r"\s+", " ", command).strip()
    backtick = re.search(r"`([^`]+)`", text)
    if backtick:
        return normalize_whitespace(backtick.group(1))
    return ""


def extract_topic(question: str) -> str:
    text = normalize_whitespace(question)
    patterns = [
        r"\bwhat\s+does\s+the\s+guide\s+say\s+about\s+(.+?)\??$",
        r"\bwhat\s+is\s+(.+?)\??$",
        r"\bhow\s+do\s+you\s+configure\s+(.+?)\??$",
        r"\bhow\s+do\s+you\s+troubleshoot\s+(.+?)\??$",
        r"\bhow\s+(?:can|do)\s+i\s+check\s+(.+?)\s+details\??$",
        r"\bhow\s+(?:can|do)\s+i\s+view\s+(.+?)\??$",
        r"\bhow\s+(?:can|do)\s+i\s+display\s+(.+?)\??$",
        r"\bwhich\s+switches\s+support\s+(.+?)\??$",
        r"\bwhat\s+platforms\s+are\s+listed\s+for\s+(.+?)\??$",
        r"\bwhat\s+should\s+be\s+checked\s+before\s+configuring\s+(.+?)\??$",
        r"\bwhat\s+limitation\s+is\s+mentioned\s+for\s+(.+?)\??$",
        r"\bwhat\s+caveat\s+is\s+documented\s+for\s+(.+?)\??$",
        r"\bwhat\s+requirement\s+is\s+documented\s+for\s+(.+?)\??$",
        r"\bwhat\s+snmp\s+mib\s+information\s+is\s+documented\s+for\s+(.+?)\??$",
        r"\bwhat\s+event\s+log\s+information\s+is\s+documented\s+for\s+(.+?)\??$",
    ]
    for pattern in patterns:
        match = re.search(pattern, text, flags=re.IGNORECASE)
        if match:
            value = normalize_whitespace(match.group(1)).strip("`'\" ")
            value = re.sub(r"\b(?:in|on)\s+(?:AOS-CX|Aruba)\b.*$", "", value, flags=re.IGNORECASE).strip()
            return value
    return ""


def detect_question_type(question: str, predicted_intent: str = "") -> str:
    text = normalize_whitespace(question).lower()
    if predicted_intent:
        if predicted_intent in {"cli_syntax", "show_command_syntax"}:
            return "cli_syntax"
        if predicted_intent in {"cli_output", "show_command_meaning"}:
            return "cli_output"
    if any(phrase in text for phrase in ("what is the syntax", "command syntax", "cli syntax", "syntax of")):
        return "cli_syntax"
    if re.search(r"\bwhat\s+does\s+the\s+.+?\s+command\s+do\b", text):
        return "cli_output"
    if "output of" in text:
        return "cli_output"
    if "workaround" in text:
        return "bug_workaround"
    if "scenario" in text:
        return "bug_scenario"
    if "symptom" in text or "issue was resolved" in text:
        return "bug_symptom"
    if re.search(
        r"\b(?:what\s+should\s+be\s+checked\s+before|what\s+prerequisite\s+does\s+the\s+guide\s+list\s+for|what\s+is\s+required\s+before|what\s+does\s+the\s+guide\s+say\s+is\s+required\s+before)\b",
        text,
    ):
        return "configuration_procedure"
    if "troubleshoot" in text or "troubleshooting" in text:
        return "troubleshooting"
    if "caveat" in text:
        return "caveat"
    if "limitation" in text:
        return "limitation"
    if "requirement" in text:
        return "requirement"
    if "since which version" in text or "from which version" in text:
        return "version_support"
    if re.search(
        r"\bhow\s+(?:can|do)\s+i\s+(?:clear|show|configure|enable|disable|reset|remove|add|set|display|view|check)\b",
        text,
    ):
        return "cli_syntax"
    if any(
        phrase in text
        for phrase in (
            "route scale",
            "supported route scale",
            "maximum routes",
            "maximum supported routes",
            "route capacity",
            "capacity of routes",
            "routes supported",
            "member number range",
            "supported capacity",
            "stack members",
        )
    ):
        return "capacity_or_scale"
    if ("support" in text and "which" in text) or "what platforms" in text or "what switches" in text:
        return "support_matrix"
    if "step" in text or "how do you configure" in text or "how can i" in text:
        return "configuration_procedure"
    return "generic"


def _canonicalize_topic(question_type: str, topic: str, question: str) -> str:
    cleaned_topic = normalize_whitespace(topic)
    lowered_topic = cleaned_topic.lower()
    lowered_question = normalize_whitespace(question).lower()
    if question_type == "support_matrix":
        if lowered_topic == "vsf commands":
            return "show vsf"
        if lowered_topic == "vsf topology commands":
            return "show vsf topology"
        if lowered_topic.endswith(" commands") and lowered_topic.startswith("vsf "):
            stem = lowered_topic[: -len(" commands")].strip()
            if stem:
                return f"show {stem}"
        if "which switches support vsf commands" in lowered_question:
            return "show vsf"
    if question_type == "configuration_procedure":
        if "before configuring" in lowered_question and "vsx lag" in lowered_question:
            return "VSX LAG member port"
        if "loop protection" in lowered_question and "vsx" in lowered_question:
            return "VSX loop protection configuration"
        if "secondary interface matching" in lowered_question and "vsx" in lowered_question:
            return "VSX secondary interface matching"
    return cleaned_topic


def extract_entities(question: str, predicted_intent: str = "") -> Dict[str, str]:
    switch_candidates = extract_switch_candidates(question)
    version_parts = extract_version(question)
    question_type = detect_question_type(question, predicted_intent)
    topic = _canonicalize_topic(question_type, extract_topic(question), question)
    entities: Dict[str, str] = {
        "question_type": question_type,
        "command": extract_command(question),
        "topic": topic,
        "bug_id": extract_bug_id(question),
    }
    if switch_candidates:
        entities["switch"] = switch_candidates[0]
    entities.update(version_parts)
    if question_type == "version_support":
        match = re.search(r"\bsupports\s+(.+?)(?:\?|$)", normalize_whitespace(question), flags=re.IGNORECASE)
        if match:
            support_feature = normalize_whitespace(match.group(1)).strip("`'\" ")
            if support_feature and support_feature.lower() not in {"aos-cx", "aruba"}:
                entities["feature"] = support_feature
    if question_type == "capacity_or_scale" and not entities.get("topic"):
        entities["topic"] = "route scale"

    feature = ""
    if question_type in {"caveat", "limitation", "requirement", "support_matrix", "version_support"}:
        feature = entities["topic"]
    elif question_type == "capacity_or_scale":
        feature = entities.get("topic", "")
    if feature:
        entities["feature"] = feature
    return {key: value for key, value in entities.items() if normalize_whitespace(value)}
