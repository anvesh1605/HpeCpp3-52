import argparse
import json
import re
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Set, Tuple


DEFAULT_RUNS = [
    {
        "label": "1000-step adapter",
        "preferred_dir": Path("outputs_inference/qwen25_15b_combined_1000steps"),
        "fallback_dir": None,
    },
    {
        "label": "metadata-context 1000-step adapter",
        "preferred_dir": Path("outputs_inference/qwen25_15b_metadatactx_1000steps"),
        "fallback_dir": None,
    },
    {
        "label": "3000-stage adapter",
        "preferred_dir": Path("outputs_inference/qwen25_15b_combined_3000steps"),
        "fallback_dir": Path("outputs_inference/qwen25_15b_combined_3000steps_fixed_safe"),
    },
]

PREDICTION_FILES = ["manual_predictions.jsonl", "test_subset_predictions.jsonl"]

UNKNOWN_PHRASES = [
    "not documented",
    "not found",
    "not specified",
    "not present",
    "not supported",
    "unavailable",
    "unknown",
]


def abstention_response(text: str) -> bool:
    normalized = normalize_text(text).lower()
    return bool(
        any(phrase in normalized for phrase in UNKNOWN_PHRASES)
        or re.search(r"\b(?:cannot|can't)\s+be\s+found\b", normalized)
        or re.search(r"\bno\s+(?:known\s+)?workaround(?:s)?\s+(?:is|are|was|were)?\s*(?:documented|mentioned|provided|available|known)\b", normalized)
    )

STOPWORDS = {
    "a",
    "about",
    "above",
    "after",
    "all",
    "also",
    "an",
    "and",
    "any",
    "are",
    "as",
    "at",
    "be",
    "been",
    "being",
    "by",
    "can",
    "does",
    "for",
    "from",
    "has",
    "have",
    "if",
    "in",
    "into",
    "is",
    "it",
    "its",
    "may",
    "not",
    "of",
    "on",
    "or",
    "provided",
    "remarks",
    "release",
    "released",
    "section",
    "should",
    "that",
    "the",
    "their",
    "then",
    "there",
    "this",
    "to",
    "under",
    "using",
    "version",
    "was",
    "were",
    "what",
    "when",
    "where",
    "which",
    "with",
}

TOKEN_EQUIVALENTS = {
    "configured": "configure",
    "configures": "configure",
    "configuration": "configure",
    "deleted": "remove",
    "deletes": "remove",
    "disabled": "disable",
    "disables": "disable",
    "displayed": "show",
    "displays": "show",
    "enabled": "enable",
    "enables": "enable",
    "removed": "remove",
    "removes": "remove",
    "shown": "show",
    "shows": "show",
}

COMMAND_PREFIXES = {
    "access-list",
    "boot",
    "class",
    "clear",
    "configure",
    "copy",
    "crypto",
    "debug",
    "erase",
    "interface",
    "ip",
    "ipv6",
    "no",
    "policy",
    "reload",
    "router",
    "show",
    "vlan",
}

CLI_DATA_FAMILIES = {
    "cli_command_reference",
    "show_command_reference",
}

CLI_QUESTION_PHRASES = (
    "what is the syntax",
    "what does the command do",
    "show command",
    "clear command",
    "configure command",
)

CLI_FILLER = {
    "command",
    "commands",
    "do",
    "does",
    "following",
    "format",
    "is",
    "of",
    "optional",
    "parameter",
    "parameters",
    "purpose",
    "syntax",
    "the",
    "usage",
    "use",
    "used",
    "what",
}

BAD_ERPS_EXPANSIONS = (
    "egress rate profile statistics",
    "error rate profile statistics",
    "error reporting per second",
    "extended route processing statistics",
)

PLACEHOLDER_MARKERS = (
    "<command>",
    "<bugid>",
    "<severity>",
    "unknown placeholder",
    "placeholder output",
    "template output",
    "the <command> command",
    "syntax: <command>",
    "event id: <id>",
)

CORRUPTED_GENERATION_MARKERS = (
    "ly i are given as theef prouba",
    "q:the: hpe uba product",
    "theef prouba",
    "<|im_start|>user",
)

MONTHS = {
    "january": "01",
    "jan": "01",
    "february": "02",
    "feb": "02",
    "march": "03",
    "mar": "03",
    "april": "04",
    "apr": "04",
    "may": "05",
    "june": "06",
    "jun": "06",
    "july": "07",
    "jul": "07",
    "august": "08",
    "aug": "08",
    "september": "09",
    "sep": "09",
    "sept": "09",
    "october": "10",
    "oct": "10",
    "november": "11",
    "nov": "11",
    "december": "12",
    "dec": "12",
}

GENERIC_VENDOR_TERMS = {
    "arista",
    "asa",
    "cisco",
    "fortinet",
    "ios xe",
    "ios-xe",
    "iosxe",
    "junos",
    "juniper",
    "nx-os",
    "nxos",
}

GENERIC_CONTEXT_TERMS = {
    "firmware",
    "pppoe",
    "router",
}


def normalize_text(value: Any) -> str:
    return str(value or "").replace("\r\n", "\n").replace("\r", "\n").strip()


def word_tokens(text: str) -> List[str]:
    return re.findall(r"[a-z0-9][a-z0-9_./-]*", normalize_text(text).lower())


def content_tokens(text: str) -> Set[str]:
    tokens: Set[str] = set()
    for token in word_tokens(text):
        parts = [part for part in re.split(r"[^a-z0-9]+", token) if part]
        for part in parts:
            if len(part) < 3 and not part.isdigit():
                continue
            if part in STOPWORDS:
                continue
            tokens.add(TOKEN_EQUIVALENTS.get(part, part))
    return tokens


def _normalize_bug_token(token: str) -> str:
    digits = re.sub(r"\D", "", token or "")
    return digits


def extract_bug_ids(text: str) -> List[str]:
    found: List[str] = []
    for token in re.findall(r"\b\d{6}\b", text or ""):
        normalized = _normalize_bug_token(token)
        if normalized and normalized not in found:
            found.append(normalized)
    bug_prefixed = re.findall(r"(?i)\bbug(?:\s+id)?\s*[:#-]?\s*([0-9][0-9_\-]{3,15})", text or "")
    for token in bug_prefixed:
        normalized = _normalize_bug_token(token)
        if normalized and normalized not in found:
            found.append(normalized)
    return found


def extract_category_labels(text: str) -> List[str]:
    labels: List[str] = []
    seen: Set[str] = set()
    patterns = (
        r"(?i)\b([A-Za-z][A-Za-z0-9 _/-]{1,40}?)\s*\(bug id\s*\d+\)",
        r"(?i)\bcategory of\s+([A-Za-z][A-Za-z0-9 _/-]{1,40}?)\b",
        r"(?i)\bbelongs to the\s+([A-Za-z][A-Za-z0-9 _/-]{1,40}?)\s+category\b",
        r"(?i)\b(?:is|are)\s+an?\s+([A-Za-z][A-Za-z0-9 _/-]{1,40}?)\s+bug\b",
    )
    for pattern in patterns:
        for raw_label in re.findall(pattern, normalize_text(text)):
            label = re.sub(r"\s+", " ", normalize_text(raw_label)).strip(" :;,.()[]{}")
            lowered = label.lower()
            if label and lowered not in seen:
                seen.add(lowered)
                labels.append(label)
    return labels


def is_category_question(question: str) -> bool:
    lowered = normalize_text(question).lower()
    return bool(
        "which category" in lowered
        or "what category" in lowered
        or ("category" in lowered and "belong" in lowered)
    )


def extract_event_ids(text: str) -> List[str]:
    """Extract explicitly labelled Event IDs without confusing unrelated numbers for IDs."""
    found: List[str] = []
    patterns = (
        r"(?i)\bevent\s*id\s*[:#-]?\s*(\d{3,6})\b",
        r"(?i)\beventid\s*[:#-]?\s*(\d{3,6})\b",
    )
    for pattern in patterns:
        for event_id in re.findall(pattern, normalize_text(text)):
            if event_id not in found:
                found.append(event_id)
    return found


def placeholder_template_output(text: str, reference: str = "") -> Tuple[bool, List[str]]:
    lowered = normalize_text(text).lower()
    reference_lower = normalize_text(reference).lower()
    reasons = [
        marker
        for marker in PLACEHOLDER_MARKERS
        if marker in lowered and marker not in reference_lower
    ]
    reasons.extend(marker for marker in CORRUPTED_GENERATION_MARKERS if marker in lowered)
    # CLI parameters such as <VRF-NAME>, <ID>, and <RINGID> are valid when the
    # same placeholder is supported by the reference syntax.
    placeholder_list = re.findall(r"<[^>\n]{1,40}>", lowered)
    placeholders = set(placeholder_list)
    reference_placeholders = set(re.findall(r"<[^>\n]{1,40}>", reference_lower))
    generic_names = {"<command>", "<bugid>", "<severity>", "<description>", "<id>"}
    unsupported_generic = [
        item for item in placeholder_list if item in generic_names and item not in reference_placeholders
    ]
    if len(unsupported_generic) >= 3:
        reasons.append("multiple_unresolved_placeholders")
    deduped: List[str] = []
    for reason in reasons:
        if reason not in deduped:
            deduped.append(reason)
    return bool(deduped), deduped


def token_repetition_loop(text: str) -> bool:
    tokens = word_tokens(text)
    if len(tokens) < 12:
        return False
    for n in (1, 2, 3, 4):
        grams = [tuple(tokens[i : i + n]) for i in range(0, len(tokens) - n + 1)]
        if not grams:
            continue
        counts = Counter(grams)
        most_common = counts.most_common(1)[0][1]
        if most_common >= 6 and most_common / len(grams) >= 0.35:
            return True
    return False


def continuous_substring_loop(text: str) -> bool:
    compact = re.sub(r"\s+", "", normalize_text(text).lower())
    if len(compact) < 24:
        return False
    if "traftraftraf" in compact or "theraftraf" in compact:
        return True
    if compact.count("traf") >= 8:
        return True
    if len(compact) >= 80 and len(set(compact)) <= 8:
        return True
    for size in range(3, 25):
        max_start = min(size, max(0, len(compact) - size * 4 + 1))
        for start in range(max_start):
            chunk = compact[start : start + size]
            if len(set(chunk)) <= 1:
                continue
            if chunk * 4 in compact:
                return True
    return False


def is_degenerate_prediction(text: str) -> bool:
    stripped = normalize_text(text)
    if not stripped:
        return True
    return continuous_substring_loop(stripped) or token_repetition_loop(stripped)


def extract_dates(text: str) -> Set[str]:
    lowered = normalize_text(text).lower()
    dates: Set[str] = set()
    month_names = "|".join(sorted(MONTHS, key=len, reverse=True))

    for day, month, year in re.findall(rf"\b(\d{{1,2}})\s+({month_names})\s+(\d{{4}})\b", lowered):
        dates.add(f"{year}-{MONTHS[month]}-{int(day):02d}")
    for month, day, year in re.findall(rf"\b({month_names})\s+(\d{{1,2}})(?:st|nd|rd|th)?[,]?\s+(\d{{4}})\b", lowered):
        dates.add(f"{year}-{MONTHS[month]}-{int(day):02d}")
    for year, month, day in re.findall(r"\b(20\d{2})[-/](\d{1,2})[-/](\d{1,2})\b", lowered):
        dates.add(f"{year}-{int(month):02d}-{int(day):02d}")
    for day, month, year in re.findall(r"\b(\d{1,2})[-/](\d{1,2})[-/](20\d{2})\b", lowered):
        dates.add(f"{year}-{int(month):02d}-{int(day):02d}")
    return dates


def commandish(text: str) -> bool:
    return bool(
        re.search(
            r"(?mi)^\s*(show|clear|configure|copy|crypto|interface|ip|ipv6|no|policy|router|vlan)\b",
            normalize_text(text),
        )
    )


def _cli_tokens_from_fragment(fragment: str) -> List[str]:
    tokens = [token for token in word_tokens(fragment) if token not in CLI_FILLER]
    if not tokens:
        return []
    if tokens[0] not in COMMAND_PREFIXES and not any(token in COMMAND_PREFIXES for token in tokens[:3]):
        return []
    return tokens[:12]


def reference_cli_fragments(question: str, reference: str) -> List[str]:
    text = normalize_text(reference)
    fragments: List[str] = []
    fragments.extend(re.findall(r"`([^`]+)`", text))
    for line in text.splitlines():
        if re.search(r"(?i)\bsyntax\b", line) or re.match(r"\s*(show|clear|configure|copy|crypto|interface|ip|ipv6|no|policy|router|vlan)\b", line, re.I):
            fragments.append(line)
    if not fragments and re.search(r"(?i)\bsyntax\b", question):
        fragments.append(question)
    return fragments


def extract_reference_cli_tokens(question: str, reference: str) -> List[str]:
    required: List[str] = []
    for fragment in reference_cli_fragments(question, reference):
        explicit_syntax = bool(re.search(r"(?i)\bsyntax\s*[:=-]", fragment))
        fragment = re.sub(r"(?i)^.*?\bsyntax\s*[:=-]\s*", "", fragment)
        tokens = _cli_tokens_from_fragment(fragment)
        if explicit_syntax and not tokens:
            tokens = [token for token in word_tokens(fragment) if token not in CLI_FILLER][:12]
        for token in tokens:
            if token not in required:
                required.append(token)
    return required


def extract_reference_cli_base_command(question: str, reference: str) -> str:
    for fragment in reference_cli_fragments(question, reference):
        fragment = re.sub(r"(?i)^.*?\bsyntax\s*(?:of\b.*?\bis)?\s*[:=-]?\s*", "", fragment)
        tokens = re.findall(r"[a-z0-9][a-z0-9_./-]*|[\[\]<>{}]", fragment.lower())
        try:
            start = next(idx for idx, token in enumerate(tokens) if token in COMMAND_PREFIXES)
        except StopIteration:
            continue
        base: List[str] = []
        for token in tokens[start:]:
            if token in {"[", "<", "{", "]", ">", "}"}:
                break
            if token in CLI_FILLER:
                continue
            base.append(token)
            if len(base) >= 6:
                break
        if base:
            return " ".join(base)
    required = extract_reference_cli_tokens(question, reference)
    if required and required[0] in COMMAND_PREFIXES:
        return " ".join(required[: min(3, len(required))])
    return ""


def is_cli_reference_row(row: Dict[str, Any], required_cli_tokens: Sequence[str]) -> bool:
    data_family = normalize_text(row.get("data_family")).lower()
    question = normalize_text(row.get("question")).lower()
    if data_family in CLI_DATA_FAMILIES:
        return True
    if any(phrase in question for phrase in CLI_QUESTION_PHRASES):
        return True
    if "syntax" in question and "command" in question:
        return True
    return bool(required_cli_tokens and any(token in COMMAND_PREFIXES for token in required_cli_tokens[:3]))


def contains_token_sequence(tokens: Sequence[str], needle: Sequence[str]) -> bool:
    if not needle:
        return True
    if len(needle) > len(tokens):
        return False
    for idx in range(0, len(tokens) - len(needle) + 1):
        if list(tokens[idx : idx + len(needle)]) == list(needle):
            return True
    return False


def extract_cli_command_spans(text: str) -> List[List[str]]:
    fragments: List[str] = []
    normalized = normalize_text(text)
    fragments.extend(re.findall(r"`([^`]+)`", normalized))
    for line in normalized.splitlines():
        clean = line.strip().strip("`")
        clean = re.sub(r"^\s*(?:[-*]|\d+[.)]|[>|#])\s*", "", clean)
        if re.match(r"(show|clear|configure|copy|crypto|interface|ip|ipv6|no|policy|router|vlan)\b", clean, re.I):
            fragments.append(clean)

    spans: List[List[str]] = []
    seen: Set[Tuple[str, ...]] = set()
    for fragment in fragments:
        tokens = _cli_tokens_from_fragment(fragment)
        if not tokens:
            continue
        if tokens[0] == "no" and (len(tokens) == 1 or tokens[1] in {"known", "specific", "workaround", "workarounds", "issue", "issues"}):
            continue
        key = tuple(tokens)
        if key not in seen:
            seen.add(key)
            spans.append(tokens)
    return spans


def unsupported_extra_cli(
    pred_cli_spans: Sequence[Sequence[str]],
    required_cli_tokens: Sequence[str],
    base_tokens: Sequence[str],
) -> Tuple[bool, List[str]]:
    allowed = set(required_cli_tokens) | set(base_tokens)
    reasons: List[str] = []
    for span in pred_cli_spans:
        tokens = list(span)
        if not tokens:
            continue
        if base_tokens and not contains_token_sequence(tokens, base_tokens):
            same_family = (
                len(tokens) > 1
                and len(base_tokens) > 1
                and tokens[0] == base_tokens[0]
                and tokens[1] == base_tokens[1]
            )
            if not same_family:
                reasons.append("different_command:" + " ".join(tokens[:4]))
        extras = [
            token
            for token in tokens
            if token not in allowed
            and token not in CLI_FILLER
            and not re.fullmatch(r"\d+", token)
        ]
        if extras:
            reasons.append("unsupported_tokens:" + ",".join(extras[:6]))
    deduped: List[str] = []
    for reason in reasons:
        if reason not in deduped:
            deduped.append(reason)
    return bool(deduped), deduped[:8]


def erps_acronym_hallucination(row: Dict[str, Any], prediction: str) -> bool:
    context = f"{normalize_text(row.get('question'))}\n{normalize_text(row.get('reference'))}".lower()
    pred = normalize_text(prediction).lower()
    if "erps" not in context or "erps" not in pred:
        return False
    return any(expansion in pred for expansion in BAD_ERPS_EXPANSIONS)


def is_cli_syntax_case(question: str, reference: str, required_cli_tokens: Sequence[str]) -> bool:
    q = question.lower()
    has_reference_syntax = bool(reference_cli_syntax_fragments(reference))
    if not required_cli_tokens and not has_reference_syntax:
        return False
    return (
        "syntax" in q
        or "exact cli" in q
        or "exact command" in q
        or has_reference_syntax
    )


def reference_says_no_workaround(reference: str) -> bool:
    return bool(
        re.search(
            r"(?i)\bno\s+(?:known\s+)?workaround(?:s)?\s+(?:is|are|was|were)?\s*(?:documented|mentioned|provided|available|known)?",
            normalize_text(reference),
        )
        or re.search(r"(?i)\bworkaround(?:s)?\s*[:=-]\s*(?:none|n/a|not documented)", normalize_text(reference))
    )


def invents_workaround(prediction: str) -> bool:
    text = normalize_text(prediction).lower()
    if any(phrase in text for phrase in UNKNOWN_PHRASES) and "workaround" in text and "no workaround" in text:
        return False
    action_terms = [
        "apply the workaround",
        "configure",
        "execute",
        "firmware",
        "follow these steps",
        "reboot",
        "reload",
        "restart",
        "run the",
        "troubleshoot",
        "upgrade",
        "update",
        "workaround is to",
    ]
    return any(term in text for term in action_terms) or commandish(prediction)


def _allowed_model_tokens(row: Dict[str, Any]) -> Set[str]:
    allowed_text = " ".join(
        normalize_text(row.get(key))
        for key in ("question", "reference", "switch", "version", "sub_version")
    )
    allowed = set(re.findall(r"\b\d{4,5}[a-z]?\b", allowed_text.lower()))
    allowed.update(extract_bug_ids(allowed_text))
    for date in extract_dates(allowed_text):
        allowed.add(date[:4])
    return allowed


def generic_hallucination(row: Dict[str, Any], prediction: str) -> Tuple[bool, List[str]]:
    q_ref = f"{normalize_text(row.get('question'))}\n{normalize_text(row.get('reference'))}".lower()
    pred = normalize_text(prediction).lower()
    reasons: List[str] = []

    for term in sorted(GENERIC_VENDOR_TERMS):
        if term in pred and term not in q_ref:
            reasons.append(term)

    for term in sorted(GENERIC_CONTEXT_TERMS):
        if term in pred and term not in q_ref:
            if term == "router" and ("route" in q_ref or "routing" in q_ref):
                continue
            reasons.append(term)

    allowed_models = _allowed_model_tokens(row)
    pred_models = set(re.findall(r"\b\d{4,5}[a-z]?\b", pred))
    pred_years = set(re.findall(r"\b20\d{2}\b", pred))
    extra_models = sorted(model for model in pred_models - allowed_models - pred_years if model not in extract_bug_ids(pred))
    if extra_models and re.search(r"\b(model|series|switch|device|platform)\b", pred):
        reasons.extend(f"unexpected_model:{model}" for model in extra_models[:5])

    return bool(reasons), reasons


def keyword_overlap(reference: str, prediction: str) -> Optional[float]:
    ref_tokens = content_tokens(reference)
    if not ref_tokens:
        return None
    pred_tokens = content_tokens(prediction)
    return len(ref_tokens & pred_tokens) / max(len(ref_tokens), 1)


def semantic_token_metrics(reference: str, prediction: str) -> Tuple[Optional[float], Optional[float], Optional[float]]:
    ref_tokens = content_tokens(reference)
    if not ref_tokens:
        return None, None, None
    pred_tokens = content_tokens(prediction)
    common = len(ref_tokens & pred_tokens)
    recall = common / max(len(ref_tokens), 1)
    precision = common / max(len(pred_tokens), 1)
    f1 = 0.0 if precision + recall == 0 else 2 * precision * recall / (precision + recall)
    return precision, recall, f1


def score_from_semantic(
    precision: Optional[float], recall: Optional[float], f1: Optional[float], reference_available: bool
) -> int:
    if f1 is None or recall is None or precision is None:
        return 5 if reference_available else 4
    if f1 >= 0.78 and recall >= 0.75:
        return 10
    if f1 >= 0.62 and recall >= 0.60:
        return 8
    if f1 >= 0.45:
        return 6
    if f1 >= 0.28:
        return 4
    if f1 > 0:
        return 2
    return 1


def normalize_cli_syntax(value: str) -> str:
    text = normalize_text(value).lower().replace("–", "-").replace("—", "-")
    text = re.sub(r"^\s*(?:syntax\s*:\s*)", "", text)
    text = re.sub(r"^\s*(?:[-*]|\d+[.)])\s*", "", text)
    text = re.sub(r"\s*([|\[\]{}<>])\s*", r"\1", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip(" .;:")


def reference_cli_syntax_fragments(reference: str) -> List[str]:
    text = normalize_text(reference)
    body = ""
    match = re.search(r"(?is)\bsyntax\s*:\s*(.+)$", text)
    if match:
        body = match.group(1)
    else:
        match = re.search(r"(?is)\bsyntax\b.+?\bis\s*:\s*(.+)$", text)
        if match:
            body = match.group(1)
    if not body:
        return []
    fragments: List[str] = []
    for line in body.splitlines() or [body]:
        cleaned = re.sub(r"^\s*(?:[-*]|\d+[.)])\s*", "", line).strip()
        normalized = normalize_cli_syntax(cleaned)
        if normalized:
            fragments.append(normalized)
    if len(fragments) == 1 and fragments[0].startswith("-"):
        fragments[0] = fragments[0].lstrip("- ")
    return list(dict.fromkeys(fragments))


def exact_cli_syntax_preserved(reference: str, prediction: str) -> Tuple[bool, List[str], List[str]]:
    required = reference_cli_syntax_fragments(reference)
    if not required:
        return True, [], []
    prediction_normalized = normalize_cli_syntax(prediction)
    missing = [fragment for fragment in required if fragment not in prediction_normalized]
    return not missing, required, missing


def score_band(score: int) -> str:
    if score == 10:
        return "factually correct"
    if score >= 8:
        return "mostly correct"
    if score >= 5:
        return "partially correct"
    if score >= 3:
        return "weak/generic"
    if score >= 1:
        return "mostly wrong"
    return "degenerate/no meaningful answer"


def strict_review(row: Dict[str, Any]) -> Dict[str, Any]:
    question = normalize_text(row.get("question"))
    reference = normalize_text(row.get("reference"))
    prediction = normalize_text(row.get("prediction"))
    pred_lower = prediction.lower()
    reference_available = bool(reference)
    degenerate = is_degenerate_prediction(prediction)
    answer_words = len(prediction.split())

    requested_bug_ids = sorted(set(extract_bug_ids(question)) | set(extract_bug_ids(reference)))
    predicted_bug_ids = sorted(set(extract_bug_ids(prediction)))
    missing_bug_ids = [bug_id for bug_id in requested_bug_ids if bug_id not in predicted_bug_ids]
    fake_bug_ids = [bug_id for bug_id in predicted_bug_ids if bug_id not in requested_bug_ids]
    wrong_bug_id = bool(requested_bug_ids and (missing_bug_ids or fake_bug_ids))

    requested_category_labels = sorted(set(extract_category_labels(reference)))
    predicted_category_labels = sorted(set(extract_category_labels(prediction)))
    wrong_category_label = bool(
        is_category_question(question)
        and requested_category_labels
        and not (set(label.lower() for label in requested_category_labels) & set(label.lower() for label in predicted_category_labels))
    )

    requested_event_ids = sorted(set(extract_event_ids(question)) | set(extract_event_ids(reference)))
    predicted_event_ids = sorted(set(extract_event_ids(prediction)))
    missing_event_ids = [event_id for event_id in requested_event_ids if event_id not in predicted_event_ids]
    fake_event_ids = [event_id for event_id in predicted_event_ids if event_id not in requested_event_ids]
    wrong_event_id = bool(requested_event_ids and (missing_event_ids or fake_event_ids))
    placeholder_bad, placeholder_reasons = placeholder_template_output(prediction, reference)

    ref_dates = sorted(extract_dates(reference))
    pred_dates = sorted(extract_dates(prediction))
    date_preserved = not ref_dates or bool(set(ref_dates) & set(pred_dates))
    wrong_date = bool(ref_dates and not date_preserved)

    required_cli_tokens = extract_reference_cli_tokens(question, reference)
    cli_syntax_case = is_cli_syntax_case(question, reference, required_cli_tokens)
    cli_row = is_cli_reference_row(row, required_cli_tokens)
    metadata_command = normalize_text(row.get("command") or row.get("command_name"))
    reference_cli_base_command = metadata_command or extract_reference_cli_base_command(question, reference)
    reference_cli_base_tokens = word_tokens(reference_cli_base_command)
    pred_word_tokens = word_tokens(prediction)
    pred_cli_spans = extract_cli_command_spans(prediction)
    correct_command_name = (
        not cli_row
        or not reference_cli_base_tokens
        or contains_token_sequence(pred_word_tokens, reference_cli_base_tokens)
    )
    pred_tokens = set(word_tokens(prediction))
    missing_cli_tokens = [token for token in required_cli_tokens if token not in pred_tokens]
    exact_syntax_ok, reference_syntax_fragments, missing_syntax_fragments = exact_cli_syntax_preserved(
        reference, prediction
    )
    strict_cli_syntax_failure = bool(cli_row and cli_syntax_case and not exact_syntax_ok)
    preserves_cli_syntax = not strict_cli_syntax_failure
    wrong_cli_syntax = strict_cli_syntax_failure
    raw_unsupported_extra_cli, unsupported_extra_cli_reasons = unsupported_extra_cli(
        pred_cli_spans,
        required_cli_tokens,
        reference_cli_base_tokens,
    )
    unsupported_extra_cli_flag = bool(cli_row and raw_unsupported_extra_cli)
    if not unsupported_extra_cli_flag:
        unsupported_extra_cli_reasons = []
    acronym_bad = erps_acronym_hallucination(row, prediction)
    old_cli_hallucination = bool(cli_row and pred_cli_spans)
    non_cli_invented_cli = (
        not cli_row
        and bool(pred_cli_spans)
        and not required_cli_tokens
        and not commandish(reference)
    )
    cli_hallucination = bool((cli_row and unsupported_extra_cli_flag) or non_cli_invented_cli)

    no_workaround_expected = reference_says_no_workaround(reference)
    invented_workaround = no_workaround_expected and invents_workaround(prediction)

    generic_bad, generic_reasons = generic_hallucination(row, prediction)
    overlap = keyword_overlap(reference, prediction)
    semantic_precision, semantic_recall, semantic_f1 = semantic_token_metrics(reference, prediction)
    grounded = semantic_f1 is None or semantic_f1 >= 0.45
    switch = normalize_text(row.get("switch"))
    switch_head = switch.split("/")[0].split("_")[0] if switch else ""
    version = normalize_text(row.get("version")).replace("_", ".")
    sub_version = normalize_text(row.get("sub_version"))
    has_switch = not switch or switch in prediction or (switch_head and switch_head in prediction)
    has_version = not version or version in prediction or version in question or version in reference
    has_sub_version = not sub_version or sub_version in prediction or sub_version in question or sub_version in reference
    asks_unknown = any(term in question.lower() for term in ("999999", "not present", "unknown", "if this bug is not present"))
    unknownish = abstention_response(prediction)
    reference_unknownish = reference_available and abstention_response(reference)
    correct_abstention = bool(unknownish and reference_unknownish)
    false_abstention = bool(unknownish and reference_available and not reference_unknownish)

    answers_directly = bool(prediction) and answer_words >= 4 and not degenerate
    score_caps: List[Tuple[int, str]] = []
    if degenerate:
        score_caps.append((0, "repetition_loop"))
        answers_directly = False
    if wrong_bug_id:
        score_caps.append((2, "wrong_or_fake_bug_id"))
        answers_directly = False
    if fake_bug_ids:
        score_caps.append((2, "fake_bug_id"))
        answers_directly = False
    if wrong_category_label:
        score_caps.append((2, "wrong_category_label"))
        answers_directly = False
    if wrong_event_id:
        score_caps.append((2, "wrong_event_id"))
        answers_directly = False
    if fake_event_ids:
        score_caps.append((2, "fake_event_id"))
        answers_directly = False
    if placeholder_bad:
        score_caps.append((0, "placeholder_or_template_output"))
        answers_directly = False
    if wrong_cli_syntax:
        score_caps.append((3, "wrong_cli_syntax"))
        answers_directly = False
    if not correct_command_name:
        score_caps.append((3, "wrong_command_name"))
        answers_directly = False
    if unsupported_extra_cli_flag:
        score_caps.append((3, "unsupported_extra_cli"))
        answers_directly = False
    if acronym_bad:
        score_caps.append((3, "acronym_meaning_hallucination"))
        answers_directly = False
    if wrong_date:
        score_caps.append((2, "wrong_release_date"))
        answers_directly = False
    if invented_workaround:
        score_caps.append((1, "invented_workaround"))
        answers_directly = False
    if generic_bad:
        score_caps.append((2, "generic_or_vendor_hallucination"))
        answers_directly = False
    if cli_hallucination:
        score_caps.append((3, "hallucinated_cli"))
        answers_directly = False
    if reference_available and semantic_f1 is not None and semantic_f1 < 0.25:
        score_caps.append((3, "low_semantic_token_f1"))
        answers_directly = False

    base_score = 0 if degenerate else score_from_semantic(
        semantic_precision, semantic_recall, semantic_f1, reference_available
    )
    if not reference_available and requested_bug_ids:
        base_score = min(base_score, 5)
    if not answers_directly:
        base_score = min(base_score, 4)

    score_max = min([cap for cap, _ in score_caps], default=10)
    score = min(base_score, score_max)

    return {
        "score": int(score),
        "score_band": score_band(int(score)),
        "score_max": int(score_max),
        "score_cap_reasons": [reason for _, reason in score_caps],
        "fake_bug_ids": fake_bug_ids,
        "missing_bug_ids": missing_bug_ids,
        "requested_bug_ids": requested_bug_ids,
        "predicted_bug_ids": predicted_bug_ids,
        "requested_category_labels": requested_category_labels,
        "predicted_category_labels": predicted_category_labels,
        "fake_event_ids": fake_event_ids,
        "missing_event_ids": missing_event_ids,
        "requested_event_ids": requested_event_ids,
        "predicted_event_ids": predicted_event_ids,
        "reference_dates": ref_dates,
        "prediction_dates": pred_dates,
        "is_cli_row": bool(cli_row),
        "reference_cli_base_command": reference_cli_base_command,
        "predicted_cli_spans": [" ".join(span) for span in pred_cli_spans],
        "required_cli_tokens": required_cli_tokens,
        "missing_cli_tokens": missing_cli_tokens,
        "reference_cli_syntax_fragments": reference_syntax_fragments,
        "missing_cli_syntax_fragments": missing_syntax_fragments,
        "unsupported_extra_cli_reasons": unsupported_extra_cli_reasons,
        "generic_hallucination_reasons": generic_reasons,
        "placeholder_template_reasons": placeholder_reasons,
        "reference_keyword_overlap": None if overlap is None else round(overlap, 4),
        "semantic_token_precision": None if semantic_precision is None else round(semantic_precision, 4),
        "semantic_token_recall": None if semantic_recall is None else round(semantic_recall, 4),
        "semantic_token_f1": None if semantic_f1 is None else round(semantic_f1, 4),
        "checks": {
            "repetition_loop": bool(degenerate),
            "not_degenerate": not degenerate,
            "loop_fixed": not degenerate,
            "answers_directly": bool(answers_directly),
            "answer_length_reasonable": not degenerate and 5 <= answer_words <= 140,
            "preserves_requested_bug_id": not wrong_bug_id,
            "preserves_requested_category_label": not wrong_category_label,
            "wrong_category_label": bool(wrong_category_label),
            "preserves_switch": bool(has_switch),
            "preserves_version": bool(has_version),
            "preserves_sub_version": bool(has_sub_version),
            "avoids_fake_bug_ids": not fake_bug_ids,
            "event_id_preserved": not wrong_event_id,
            "wrong_event_id": bool(wrong_event_id),
            "avoids_fake_event_ids": not fake_event_ids,
            "placeholder_template_output": bool(placeholder_bad),
            "is_cli_row": bool(cli_row),
            "correct_command_name": bool(correct_command_name),
            "preserves_real_cli_syntax_when_known": bool(preserves_cli_syntax),
            "wrong_cli_syntax": bool(wrong_cli_syntax),
            "unsupported_extra_cli": bool(unsupported_extra_cli_flag),
            "avoids_hallucinated_cli": not cli_hallucination,
            "cli_hallucination": bool(cli_hallucination),
            "legacy_cli_hallucination": bool(old_cli_hallucination),
            "acronym_meaning_hallucination": bool(acronym_bad),
            "date_preserved": bool(date_preserved),
            "avoids_fake_workarounds": not invented_workaround,
            "generic_hallucination": bool(generic_bad),
            "reference_keyword_grounded": bool(grounded),
            "uses_not_found_when_unavailable": not asks_unknown or unknownish,
            "correct_abstention": correct_abstention,
            "false_abstention": false_abstention,
            "abstention_expected": bool(reference_unknownish),
        },
    }


def read_jsonl(path: Path) -> Iterable[Dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                yield json.loads(line)


def write_jsonl(path: Path, rows: Iterable[Dict[str, Any]]) -> int:
    count = 0
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
            count += 1
    return count


def compact_text(text: str, limit: int = 220) -> str:
    compact = re.sub(r"\s+", " ", normalize_text(text))
    if len(compact) > limit:
        return compact[: limit - 3] + "..."
    return compact


def format_metric(value: Optional[float]) -> str:
    if value is None:
        return "n/a"
    return f"{value:.4f}"


def summarize_rows(rows: List[Dict[str, Any]]) -> Dict[str, Any]:
    total = len(rows)

    def count_check(name: str, expected: bool = True) -> int:
        return sum(1 for row in rows if bool(row["strict_review"]["checks"].get(name)) is expected)

    def rate(numerator: int, denominator: int) -> Optional[float]:
        if denominator <= 0:
            return None
        return round(numerator / denominator, 4)

    wrong_bug_rows = [
        row
        for row in rows
        if row["strict_review"]["requested_bug_ids"]
        and not row["strict_review"]["checks"]["preserves_requested_bug_id"]
    ]
    wrong_category_rows = [
        row
        for row in rows
        if row["strict_review"]["requested_category_labels"]
        and not row["strict_review"]["checks"]["preserves_requested_category_label"]
    ]
    fake_bug_rows = [row for row in rows if row["strict_review"]["fake_bug_ids"]]
    bug_rows = [row for row in rows if row["strict_review"]["requested_bug_ids"]]
    category_rows = [row for row in rows if row["strict_review"]["requested_category_labels"]]
    event_rows = [row for row in rows if row["strict_review"]["requested_event_ids"]]
    wrong_event_rows = [row for row in event_rows if row["strict_review"]["checks"]["wrong_event_id"]]
    fake_event_rows = [event_id for row in rows for event_id in row["strict_review"]["fake_event_ids"]]
    missing_event_rows = [event_id for row in rows for event_id in row["strict_review"]["missing_event_ids"]]
    cli_rows = [row for row in rows if row["strict_review"]["checks"]["is_cli_row"]]
    command_name_rows = [row for row in cli_rows if row["strict_review"]["reference_cli_base_command"]]
    syntax_rows = [row for row in cli_rows if row["strict_review"]["reference_cli_syntax_fragments"]]
    correct_command_name_rows = [
        row for row in command_name_rows if row["strict_review"]["checks"]["correct_command_name"]
    ]
    wrong_cli_rows = [row for row in syntax_rows if row["strict_review"]["checks"]["wrong_cli_syntax"]]
    unsupported_extra_cli_rows = [row for row in cli_rows if row["strict_review"]["checks"]["unsupported_extra_cli"]]
    cli_hallucination_rows = [row for row in rows if row["strict_review"]["checks"]["cli_hallucination"]]
    legacy_cli_hallucination_rows = [row for row in rows if row["strict_review"]["checks"]["legacy_cli_hallucination"]]
    acronym_rows = [row for row in rows if row["strict_review"]["checks"]["acronym_meaning_hallucination"]]
    wrong_date_rows = [row for row in rows if not row["strict_review"]["checks"]["date_preserved"]]
    date_rows = [row for row in rows if row["strict_review"].get("reference_dates")]
    workaround_rows = [row for row in rows if not row["strict_review"]["checks"]["avoids_fake_workarounds"]]
    generic_rows = [row for row in rows if row["strict_review"]["checks"]["generic_hallucination"]]
    degenerate_rows = [row for row in rows if row["strict_review"]["checks"]["repetition_loop"]]
    placeholder_rows = [row for row in rows if row["strict_review"]["checks"]["placeholder_template_output"]]
    correct_abstention_rows = [row for row in rows if row["strict_review"]["checks"].get("correct_abstention")]
    false_abstention_rows = [row for row in rows if row["strict_review"]["checks"].get("false_abstention")]
    abstention_reference_rows = [row for row in rows if row["strict_review"]["checks"].get("abstention_expected")]
    scores = [row["strict_review"]["score"] for row in rows]
    good_rows = [row for row in rows if row["strict_review"]["score"] >= 8]
    bad_rows = [row for row in rows if row["strict_review"]["score"] < 8]

    degenerate_count = len(degenerate_rows)
    near_zero_loop_threshold = max(1, total // 100)
    return {
        "total_predictions": total,
        "degenerate_predictions": degenerate_count,
        "repetition_loop_predictions": degenerate_count,
        "loop_fixed": degenerate_count <= near_zero_loop_threshold,
        "wrong_bug_id_predictions": len(wrong_bug_rows),
        "wrong_category_label_predictions": len(wrong_category_rows),
        "fake_bug_id_predictions": len(fake_bug_rows),
        "bug_id_reference_rows": len(bug_rows),
        "bug_id_accuracy": rate(len(bug_rows) - len(wrong_bug_rows), len(bug_rows)),
        "category_reference_rows": len(category_rows),
        "category_label_accuracy": rate(len(category_rows) - len(wrong_category_rows), len(category_rows)),
        "event_id_reference_rows": len(event_rows),
        "event_id_correct_rows": len(event_rows) - len(wrong_event_rows),
        "event_id_accuracy": rate(len(event_rows) - len(wrong_event_rows), len(event_rows)),
        "wrong_event_id_count": len(wrong_event_rows),
        "fake_event_id_count": len(fake_event_rows),
        "missing_event_id_count": len(missing_event_rows),
        "wrong_cli_syntax_predictions": len(wrong_cli_rows),
        "cli_reference_rows": len(cli_rows),
        "cli_syntax_rows": len(syntax_rows),
        "command_name_rows": len(command_name_rows),
        "command_name_accuracy": rate(len(correct_command_name_rows), len(command_name_rows)),
        "command_syntax_preservation": rate(len(syntax_rows) - len(wrong_cli_rows), len(syntax_rows)),
        "wrong_cli_syntax_rate": rate(len(wrong_cli_rows), len(syntax_rows)),
        "unsupported_extra_cli_predictions": len(unsupported_extra_cli_rows),
        "unsupported_extra_cli_rate": rate(len(unsupported_extra_cli_rows), len(cli_rows)),
        "cli_hallucination_predictions": len(cli_hallucination_rows),
        "cli_hallucination_rate": rate(len(cli_hallucination_rows), total),
        "no_cli_hallucination_rate": rate(total - len(cli_hallucination_rows), total),
        "legacy_cli_hallucination_predictions": len(legacy_cli_hallucination_rows),
        "legacy_cli_hallucination_rate": rate(len(legacy_cli_hallucination_rows), total),
        "acronym_meaning_hallucination_predictions": len(acronym_rows),
        "acronym_meaning_hallucination_rate": rate(len(acronym_rows), total),
        "wrong_date_predictions": len(wrong_date_rows),
        "date_reference_rows": len(date_rows),
        "date_accuracy": rate(len(date_rows) - len(wrong_date_rows), len(date_rows)),
        "invented_workaround_predictions": len(workaround_rows),
        "generic_hallucination_predictions": len(generic_rows),
        "placeholder_template_predictions": len(placeholder_rows),
        "correct_abstention_predictions": len(correct_abstention_rows),
        "false_abstention_predictions": len(false_abstention_rows),
        "abstention_reference_rows": len(abstention_reference_rows),
        "average_score": round(sum(scores) / max(total, 1), 2),
        "good_predictions_count": len(good_rows),
        "bad_predictions_count": len(bad_rows),
        "non_degenerate_predictions": count_check("not_degenerate"),
    }


def partition_summaries(rows: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    reference_backed = [row for row in rows if normalize_text(row.get("reference"))]
    manual_without_reference = [row for row in rows if not normalize_text(row.get("reference"))]
    return {
        "all_predictions": summarize_rows(rows),
        "reference_backed_factual_tests": summarize_rows(reference_backed),
        "manual_smoke_tests": summarize_rows(manual_without_reference),
        # Legacy aliases retained for existing report consumers.
        "reference_backed_predictions": summarize_rows(reference_backed),
        "manual_without_reference": summarize_rows(manual_without_reference),
    }


def strict_holdout_gate(candidate: Dict[str, Any], baseline: Dict[str, Any]) -> Dict[str, Any]:
    """Apply the approved strict generated-answer gate to one holdout suite."""

    def numeric(summary: Dict[str, Any], key: str) -> float:
        value = summary.get(key)
        return float(value) if value is not None else 0.0

    bug_errors_candidate = candidate["wrong_bug_id_predictions"] + candidate["fake_bug_id_predictions"]
    bug_errors_baseline = baseline["wrong_bug_id_predictions"] + baseline["fake_bug_id_predictions"]
    event_errors_candidate = (
        candidate["wrong_event_id_count"]
        + candidate["fake_event_id_count"]
        + candidate["missing_event_id_count"]
    )
    event_errors_baseline = (
        baseline["wrong_event_id_count"]
        + baseline["fake_event_id_count"]
        + baseline["missing_event_id_count"]
    )
    checks = {
        "strict_score_delta_at_least_0_25": candidate["average_score"] - baseline["average_score"] >= 0.25,
        "bug_id_accuracy_higher": numeric(candidate, "bug_id_accuracy") > numeric(baseline, "bug_id_accuracy"),
        "event_id_accuracy_higher": numeric(candidate, "event_id_accuracy") > numeric(baseline, "event_id_accuracy"),
        "cli_syntax_accuracy_higher": numeric(candidate, "command_syntax_preservation")
        > numeric(baseline, "command_syntax_preservation"),
        "command_name_accuracy_not_lower": numeric(candidate, "command_name_accuracy")
        >= numeric(baseline, "command_name_accuracy"),
        "combined_bug_errors_lower": bug_errors_candidate < bug_errors_baseline,
        "wrong_bug_ids_not_higher": candidate["wrong_bug_id_predictions"]
        <= baseline["wrong_bug_id_predictions"],
        "fake_bug_ids_not_higher": candidate["fake_bug_id_predictions"]
        <= baseline["fake_bug_id_predictions"],
        "combined_event_errors_lower": event_errors_candidate < event_errors_baseline,
        "wrong_event_ids_not_higher": candidate["wrong_event_id_count"] <= baseline["wrong_event_id_count"],
        "fake_event_ids_not_higher": candidate["fake_event_id_count"] <= baseline["fake_event_id_count"],
        "wrong_cli_syntax_lower": candidate["wrong_cli_syntax_predictions"]
        < baseline["wrong_cli_syntax_predictions"],
        "date_errors_not_higher": candidate["wrong_date_predictions"] <= baseline["wrong_date_predictions"],
        "workaround_errors_not_higher": candidate["invented_workaround_predictions"]
        <= baseline["invented_workaround_predictions"],
        "generic_hallucinations_not_higher": candidate["generic_hallucination_predictions"]
        <= baseline["generic_hallucination_predictions"],
        "zero_loops": candidate["repetition_loop_predictions"] == 0,
        "zero_templates": candidate["placeholder_template_predictions"] == 0,
    }
    delta_keys = (
        "average_score",
        "bug_id_accuracy",
        "event_id_accuracy",
        "command_syntax_preservation",
        "command_name_accuracy",
        "wrong_bug_id_predictions",
        "fake_bug_id_predictions",
        "wrong_event_id_count",
        "fake_event_id_count",
        "missing_event_id_count",
        "wrong_cli_syntax_predictions",
        "wrong_date_predictions",
        "invented_workaround_predictions",
        "generic_hallucination_predictions",
        "repetition_loop_predictions",
        "placeholder_template_predictions",
    )
    deltas = {
        key: round(numeric(candidate, key) - numeric(baseline, key), 4)
        for key in delta_keys
    }
    return {
        "passed": all(checks.values()),
        "checks": checks,
        "deltas": deltas,
        "failed_checks": [name for name, passed in checks.items() if not passed],
    }


def verdict(label: str, summary: Dict[str, Any], comparison_summary: Optional[Dict[str, Any]] = None) -> str:
    total = max(summary["total_predictions"], 1)
    hard_fails = (
        summary["wrong_bug_id_predictions"]
        + summary["fake_bug_id_predictions"]
        + summary["wrong_event_id_count"]
        + summary["wrong_cli_syntax_predictions"]
        + summary["wrong_date_predictions"]
        + summary["generic_hallucination_predictions"]
        + summary["placeholder_template_predictions"]
    )
    if summary["degenerate_predictions"] / total >= 0.50:
        return "not usable; inference/evaluation path produced mostly degenerate repeated output"
    if hard_fails / total >= 0.25:
        if label.lower().startswith("3000"):
            return (
                "baseline only; do not continue training blindly. Many factual hard failures remain, "
                "so use a new training/eval format with metadata/context in the input prompt before 6000 steps"
            )
        return "not usable as final; too many factual hard failures"
    if summary["average_score"] >= 8 and summary["good_predictions_count"] > summary["bad_predictions_count"]:
        return "candidate for more manual testing; factual correctness is stronger but still needs spot checks"
    if comparison_summary and summary["average_score"] > comparison_summary.get("average_score", 0):
        return "improved over comparison run but still baseline only"
    return "baseline only; not good enough for demo/final"


def focusfix_comparison_verdict(run_summaries: Dict[str, Dict[str, Any]]) -> Optional[str]:
    checkpoint500_entry = next(
        (
            (label, summary)
            for label, summary in run_summaries.items()
            if "focusfix" in label.lower() and "checkpoint-500" in label.lower()
        ),
        None,
    )
    focus_entry = next(
        (
            (label, summary)
            for label, summary in run_summaries.items()
            if "focusfix" in label.lower() and "checkpoint" not in label.lower()
        ),
        None,
    )
    metadata_entry = next(
        (
            (label, summary)
            for label, summary in run_summaries.items()
            if "metadata-context" in label.lower()
            and "1000" in label.lower()
            and "focusfix" not in label.lower()
        ),
        None,
    )
    old_entry = next(
        (
            (label, summary)
            for label, summary in run_summaries.items()
            if "combined" in label.lower() and "3000" in label.lower()
        ),
        None,
    )
    checkpoint_entry = next(
        (
            (label, summary)
            for label, summary in run_summaries.items()
            if "focusfix" in label.lower() and "checkpoint-250" in label.lower()
        ),
        None,
    )
    if checkpoint500_entry and metadata_entry:
        _, checkpoint500 = checkpoint500_entry
        _, metadata = metadata_entry
        hard_failure = bool(
            checkpoint500["degenerate_predictions"]
            or checkpoint500["placeholder_template_predictions"]
        )
        better = bool(
            not hard_failure
            and checkpoint500["average_score"] > metadata["average_score"]
            and checkpoint500["wrong_bug_id_predictions"] <= metadata["wrong_bug_id_predictions"]
            and checkpoint500["fake_bug_id_predictions"] <= metadata["fake_bug_id_predictions"]
            and (checkpoint500["event_id_accuracy"] or 0.0) >= (metadata["event_id_accuracy"] or 0.0)
            and (checkpoint500["command_name_accuracy"] or 0.0) >= (metadata["command_name_accuracy"] or 0.0)
            and (checkpoint500["command_syntax_preservation"] or 0.0)
            >= (metadata["command_syntax_preservation"] or 0.0)
            and checkpoint500["wrong_cli_syntax_predictions"] <= metadata["wrong_cli_syntax_predictions"]
        )
        if better:
            return "focusfix checkpoint-500 is better than metadatactx_1000 and is the current best adapter."
        return (
            "focusfix checkpoint-500 is not better than metadatactx_1000 under the strict decision metrics. "
            "Keep metadatactx_1000 as the current best adapter."
        )

    if focus_entry and metadata_entry and checkpoint_entry:
        _, focus = focus_entry
        _, metadata = metadata_entry
        _, checkpoint = checkpoint_entry

        def usable(summary: Dict[str, Any]) -> bool:
            return not summary["degenerate_predictions"] and not summary["placeholder_template_predictions"]

        def beats(candidate: Dict[str, Any], baseline: Dict[str, Any]) -> bool:
            return (
                usable(candidate)
                and candidate["average_score"] > baseline["average_score"]
                and candidate["wrong_bug_id_predictions"] <= baseline["wrong_bug_id_predictions"]
                and candidate["fake_bug_id_predictions"] <= baseline["fake_bug_id_predictions"]
                and (candidate["event_id_accuracy"] or 0.0) >= (baseline["event_id_accuracy"] or 0.0)
                and (candidate["command_syntax_preservation"] or 0.0)
                >= (baseline["command_syntax_preservation"] or 0.0)
                and candidate["wrong_cli_syntax_predictions"] <= baseline["wrong_cli_syntax_predictions"]
            )

        if beats(focus, metadata):
            return "focusfix_1500 metadata-prompt is the current best adapter."
        if beats(checkpoint, metadata):
            return "focusfix checkpoint-250 metadata-prompt is the current best adapter."
        return (
            "Keep metadatactx_1000 as the current best adapter. Both focusfix continuations were worse or failed "
            "a hard output-quality gate. Do not reject the manual-corrected dataset; the continuation settings were not ideal."
        )

    if not focus_entry or not metadata_entry or not old_entry:
        return None

    _, focus = focus_entry
    _, metadata = metadata_entry
    _, old = old_entry
    if focus["placeholder_template_predictions"] or focus["degenerate_predictions"]:
        return "Reject focusfix_1500 immediately: placeholder/template or repetition-loop output is present."

    lower_score = focus["average_score"] < metadata["average_score"]
    more_fake_bug = focus["fake_bug_id_predictions"] > metadata["fake_bug_id_predictions"]
    more_wrong_cli = focus["wrong_cli_syntax_predictions"] > metadata["wrong_cli_syntax_predictions"]
    if lower_score or more_fake_bug or more_wrong_cli:
        return (
            "Do not continue focusfix_1500. It regressed on strict score, fake Bug IDs, or wrong CLI syntax; "
            "test checkpoint-250 from the same run next."
        )

    event_improved = (focus["event_id_accuracy"] or 0.0) > (metadata["event_id_accuracy"] or 0.0)
    bug_improved = (focus["bug_id_accuracy"] or 0.0) > (metadata["bug_id_accuracy"] or 0.0)
    cli_improved = (focus["command_syntax_preservation"] or 0.0) > (metadata["command_syntax_preservation"] or 0.0)
    score_improved = focus["average_score"] > metadata["average_score"]
    beats_old = focus["average_score"] > old["average_score"]
    if score_improved and event_improved and bug_improved and cli_improved and beats_old:
        return "focusfix_1500 is the current best adapter; all required strict metrics improved."
    return (
        "focusfix_1500 is not yet proven better than metadatactx_1000 on every required strict metric. "
        "Do not continue training automatically."
    )


def report_examples(rows: List[Dict[str, Any]], reverse: bool) -> List[str]:
    ordered = sorted(rows, key=lambda row: row["strict_review"]["score"], reverse=reverse)[:5]
    if not ordered:
        return ["- none"]
    lines: List[str] = []
    for row in ordered:
        review = row["strict_review"]
        caps = ",".join(review["score_cap_reasons"]) or "none"
        lines.append(
            f"- score {review['score']}/10 | caps={caps} | Q: {compact_text(row.get('question'), 160)}\n"
            f"  A: {compact_text(row.get('prediction'), 220)}"
        )
    return lines


def report_cli_examples(rows: List[Dict[str, Any]], title: str, limit: int = 4) -> List[str]:
    selected = rows[:limit]
    if not selected:
        return [f"### {title}", "", "- none"]
    lines = [f"### {title}", ""]
    for row in selected:
        review = row["strict_review"]
        checks = review["checks"]
        lines.append(
            f"- score {review['score']}/10 | cli_hallucination={str(checks['cli_hallucination']).lower()} | "
            f"wrong_syntax={str(checks['wrong_cli_syntax']).lower()} | "
            f"unsupported_extra_cli={str(checks['unsupported_extra_cli']).lower()}"
        )
        lines.append(f"  Q: {compact_text(row.get('question'), 180)}")
        lines.append(f"  Ref: {compact_text(row.get('reference'), 180)}")
        lines.append(f"  A: {compact_text(row.get('prediction'), 240)}")
        if review.get("missing_cli_tokens"):
            lines.append(f"  Missing syntax tokens: {', '.join(review['missing_cli_tokens'])}")
        if review.get("unsupported_extra_cli_reasons"):
            lines.append(f"  Unsupported CLI reasons: {', '.join(review['unsupported_extra_cli_reasons'])}")
        if checks.get("acronym_meaning_hallucination"):
            lines.append("  ERPS acronym meaning hallucination: true")
    return lines


def write_report(
    output_dir: Path,
    run_summaries: Dict[str, Dict[str, Any]],
    all_rows_by_run: Dict[str, List[Dict[str, Any]]],
    partitions_by_run: Dict[str, Dict[str, Dict[str, Any]]],
    source_notes: List[str],
    baseline_label: Optional[str] = None,
) -> None:
    lines: List[str] = [
        "# Strict Aruba Inference Rescore",
        "",
        "This report rescored existing inference JSONL files without generating new model outputs.",
        "All factual scores and accept/reject metrics below use only reference-backed test rows. Manual prompts without reference answers are reported separately as smoke tests.",
        "",
        "## Source Notes",
        "",
    ]
    lines.extend(f"- {note}" for note in source_notes)

    lines.extend(["", "## Old CLI Hallucination Metric Behavior", ""])
    lines.append(
        "The old behavior overcounted CLI hallucination by treating CLI-looking answers on CLI reference rows "
        "as hallucinated. The corrected behavior allows command syntax on CLI rows and separates wrong syntax "
        "from unsupported extra commands or parameters."
    )
    lines.extend(
        [
            "",
            "| Run | Legacy CLI hallucination rate | New CLI hallucination rate | CLI rows | Unsupported extra CLI rate | Wrong CLI syntax rate |",
            "|---|---:|---:|---:|---:|---:|",
        ]
    )
    for label, summary in run_summaries.items():
        lines.append(
            f"| {label} | {format_metric(summary['legacy_cli_hallucination_rate'])} | "
            f"{format_metric(summary['cli_hallucination_rate'])} | {summary['cli_reference_rows']} | "
            f"{format_metric(summary['unsupported_extra_cli_rate'])} | {format_metric(summary['wrong_cli_syntax_rate'])} |"
        )

    lines.extend(
        [
            "",
            "## Summary",
            "",
            "| Run | Factual rows | Degenerate | Placeholder | Wrong Bug ID | Fake Bug ID | Event ID Acc | Wrong Event ID | Fake Event ID | Missing Event ID | Cmd Name Acc | Syntax Preserve | Wrong CLI Syntax Rate | Avg Score | Good | Bad |",
            "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for label, summary in run_summaries.items():
        lines.append(
            f"| {label} | {summary['total_predictions']} | {summary['degenerate_predictions']} | {summary['placeholder_template_predictions']} | "
            f"{summary['wrong_bug_id_predictions']} | {summary['fake_bug_id_predictions']} | "
            f"{format_metric(summary['event_id_accuracy'])} | {summary['wrong_event_id_count']} | {summary['fake_event_id_count']} | {summary['missing_event_id_count']} | "
            f"{format_metric(summary['command_name_accuracy'])} | {format_metric(summary['command_syntax_preservation'])} | "
            f"{format_metric(summary['wrong_cli_syntax_rate'])} | "
            f"{summary['average_score']:.2f} | {summary['good_predictions_count']} | {summary['bad_predictions_count']} |"
        )

    comparison = run_summaries.get(baseline_label) if baseline_label else run_summaries.get("1000-step adapter")
    lines.extend(["", "## Verdicts", ""])
    for label, summary in run_summaries.items():
        lines.append(f"- {label}: {verdict(label, summary, comparison if comparison is not summary else None)}")

    if baseline_label and baseline_label in run_summaries:
        lines.extend(["", "## Explicit Baseline Comparison", ""])
        baseline = run_summaries[baseline_label]
        for label, summary in run_summaries.items():
            if label == baseline_label:
                continue
            gate = strict_holdout_gate(summary, baseline)
            lines.append(f"### {label} versus {baseline_label}")
            lines.append("")
            lines.append(f"- Strict holdout gate: {'PASS' if gate['passed'] else 'FAIL'}")
            lines.append(f"- Failed checks: {', '.join(gate['failed_checks']) or 'none'}")
            lines.append("- Candidate-minus-baseline deltas:")
            for key, value in gate["deltas"].items():
                lines.append(f"  - {key}: {value:+.4f}")
            lines.append("")

    for label, rows in all_rows_by_run.items():
        summary = run_summaries[label]
        partitions = partitions_by_run[label]
        reference_summary = partitions["reference_backed_factual_tests"]
        manual_summary = partitions["manual_smoke_tests"]
        all_summary = partitions["all_predictions"]
        reference_rows = [row for row in rows if normalize_text(row.get("reference"))]
        manual_rows = [row for row in rows if not normalize_text(row.get("reference"))]
        lines.extend(
            [
                "",
                f"## {label}",
                "",
                f"- Total predictions: {all_summary['total_predictions']}",
                f"- Reference-backed factual tests: {summary['total_predictions']}",
                f"- Manual smoke tests: {manual_summary['total_predictions']} (excluded from factual scores)",
                f"- Degenerate predictions: {summary['degenerate_predictions']}",
                f"- Placeholder/template predictions: {summary['placeholder_template_predictions']}",
                f"- Repetition-loop predictions: {summary['repetition_loop_predictions']}",
                f"- Loop fixed: {str(summary['loop_fixed']).lower()}",
                f"- Wrong bug ID predictions: {summary['wrong_bug_id_predictions']}",
                f"- Fake bug ID predictions: {summary['fake_bug_id_predictions']}",
                f"- Bug ID accuracy: {format_metric(summary['bug_id_accuracy'])}",
                f"- Event ID accuracy: {format_metric(summary['event_id_accuracy'])}",
                f"- Wrong Event ID count: {summary['wrong_event_id_count']}",
                f"- Fake Event ID count: {summary['fake_event_id_count']}",
                f"- Missing Event ID count: {summary['missing_event_id_count']}",
                f"- Wrong CLI syntax predictions: {summary['wrong_cli_syntax_predictions']}",
                f"- Command name accuracy: {format_metric(summary['command_name_accuracy'])}",
                f"- Command syntax preservation: {format_metric(summary['command_syntax_preservation'])}",
                f"- Wrong CLI syntax rate: {format_metric(summary['wrong_cli_syntax_rate'])}",
                f"- Unsupported extra CLI rate: {format_metric(summary['unsupported_extra_cli_rate'])}",
                f"- CLI hallucination rate: {format_metric(summary['cli_hallucination_rate'])}",
                f"- No CLI hallucination rate: {format_metric(summary['no_cli_hallucination_rate'])}",
                f"- ERPS acronym meaning hallucination rate: {format_metric(summary['acronym_meaning_hallucination_rate'])}",
                f"- Wrong date predictions: {summary['wrong_date_predictions']}",
                f"- Invented workaround predictions: {summary['invented_workaround_predictions']}",
                f"- Generic hallucination predictions: {summary['generic_hallucination_predictions']}",
                f"- Average score: {summary['average_score']:.2f}",
                f"- Good predictions count: {summary['good_predictions_count']}",
                f"- Bad predictions count: {summary['bad_predictions_count']}",
                "",
                "### Evidence Split",
                "",
                (
                    f"- reference_backed_factual_tests: {reference_summary['total_predictions']} | "
                    f"average score {reference_summary['average_score']:.2f} | "
                    f"good {reference_summary['good_predictions_count']} | "
                    f"bad {reference_summary['bad_predictions_count']}"
                ),
                (
                    f"- manual_smoke_tests: {manual_summary['total_predictions']} | "
                    f"average score {manual_summary['average_score']:.2f} | "
                    "these are smoke tests and cannot establish factual correctness by themselves"
                ),
                "",
                "### 5 Best Reference-Backed Predictions",
                "",
                *report_examples(reference_rows, reverse=True),
                "",
                "### 5 Worst Reference-Backed Predictions",
                "",
                *report_examples(reference_rows, reverse=False),
                "",
                "### Common Failure Patterns",
                "",
                f"- Repetition/degenerate collapse: {summary['degenerate_predictions']}",
                f"- Missing or wrong requested bug IDs: {summary['wrong_bug_id_predictions']}",
                f"- Fake bug IDs: {summary['fake_bug_id_predictions']}",
                f"- Wrong Event IDs: {summary['wrong_event_id_count']}",
                f"- Fake Event IDs: {summary['fake_event_id_count']}",
                f"- Missing Event IDs: {summary['missing_event_id_count']}",
                f"- Wrong or incomplete CLI syntax: {summary['wrong_cli_syntax_predictions']}",
                f"- Unsupported extra CLI: {summary['unsupported_extra_cli_predictions']}",
                f"- Corrected CLI hallucination: {summary['cli_hallucination_predictions']}",
                f"- ERPS acronym meaning hallucination: {summary['acronym_meaning_hallucination_predictions']}",
                f"- Wrong/missing release dates: {summary['wrong_date_predictions']}",
                f"- Invented workarounds: {summary['invented_workaround_predictions']}",
                f"- Generic/vendor hallucinations: {summary['generic_hallucination_predictions']}",
                f"- Placeholder/template output: {summary['placeholder_template_predictions']}",
            ]
        )

        wrong_syntax_examples = sorted(
            [row for row in reference_rows if row["strict_review"]["checks"]["wrong_cli_syntax"]],
            key=lambda row: row["strict_review"]["checks"]["cli_hallucination"],
        )
        real_cli_hallucination_examples = [
            row for row in reference_rows if row["strict_review"]["checks"]["cli_hallucination"]
        ]
        non_hallucinated_cli_examples = [
            row
            for row in reference_rows
            if row["strict_review"]["checks"]["is_cli_row"]
            and row["strict_review"]["predicted_cli_spans"]
            and not row["strict_review"]["checks"]["cli_hallucination"]
        ]
        lines.extend(["", "### Corrected CLI Metric Examples", ""])
        lines.extend(report_cli_examples(wrong_syntax_examples, "Wrong syntax, not automatically hallucination"))
        lines.extend([""])
        lines.extend(report_cli_examples(real_cli_hallucination_examples, "Real CLI hallucination"))
        lines.extend([""])
        lines.extend(report_cli_examples(non_hallucinated_cli_examples, "Non-hallucinated CLI answers"))
        if summary["cli_hallucination_rate"] == 1.0:
            lines.extend(
                [
                    "",
                    "### CLI Hallucination Rate Stayed 1.0 Evidence",
                    "",
                    "The corrected metric still reports 1.0 for this run; examples above show unsupported extra CLI or non-CLI command invention.",
                ]
            )

    lines.extend(
        [
            "",
            "## Final Evaluator Calibration Note",
            "",
            "The old CLI hallucination metric was overcounting hallucination. CLI command reference rows should be allowed to contain command syntax. The corrected metric now reports wrong syntax, unsupported extra CLI, and true CLI hallucination separately.",
        ]
    )

    comparison_verdict = focusfix_comparison_verdict(run_summaries)
    if comparison_verdict:
        lines.extend(["", "## Final Focusfix Verdict", "", comparison_verdict])

    (output_dir / "strict_rescore_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def resolve_run_dir(run: Dict[str, Any]) -> Tuple[Optional[Path], str]:
    preferred = run["preferred_dir"]
    required = [preferred / name for name in PREDICTION_FILES]
    if all(path.exists() for path in required):
        return preferred, f"{run['label']}: used requested directory {preferred}"
    fallback = run.get("fallback_dir")
    if fallback:
        fallback_required = [fallback / name for name in PREDICTION_FILES]
        if all(path.exists() for path in fallback_required):
            missing = ", ".join(str(path) for path in required if not path.exists())
            return fallback, f"{run['label']}: requested files missing ({missing}); used fallback {fallback}"
    missing = ", ".join(str(path) for path in required if not path.exists())
    return None, f"{run['label']}: skipped because required files are missing ({missing})"


def rescore_run(label: str, source_dir: Path, output_dir: Path) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for filename in PREDICTION_FILES:
        source_path = source_dir / filename
        for idx, row in enumerate(read_jsonl(source_path), start=1):
            row = dict(row)
            row["source_file"] = str(source_path)
            row["source_row"] = idx
            row["strict_review"] = strict_review(row)
            rows.append(row)

    run_dir = output_dir / safe_label(label)
    run_dir.mkdir(parents=True, exist_ok=True)
    write_jsonl(run_dir / "strict_rescored_predictions.jsonl", rows)
    (run_dir / "summary.json").write_text(json.dumps(partition_summaries(rows), indent=2), encoding="utf-8")
    return rows


def safe_label(label: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", label.lower()).strip("_")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Strictly rescore existing Aruba AOS-CX inference JSONL outputs.")
    parser.add_argument("--output_dir", type=Path, default=None)
    parser.add_argument("--input_dir", type=Path, default=None)
    parser.add_argument("--label", default="3000-stage adapter")
    parser.add_argument(
        "--baseline_label",
        default=None,
        help="Exact label of the comparison run that acts as the explicit strict baseline.",
    )
    parser.add_argument(
        "--comparison_run",
        action="append",
        default=[],
        metavar="LABEL=DIR",
        help="Additional prediction directory to rescore and compare; may be repeated.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = args.output_dir or Path("outputs_inference") / f"strict_rescore_{stamp}"
    output_dir.mkdir(parents=True, exist_ok=True)

    source_notes: List[str] = []
    run_summaries: Dict[str, Dict[str, Any]] = {}
    all_rows_by_run: Dict[str, List[Dict[str, Any]]] = {}
    partitions_by_run: Dict[str, Dict[str, Dict[str, Any]]] = {}

    runs = DEFAULT_RUNS
    if args.input_dir:
        runs = [{"label": args.label, "preferred_dir": args.input_dir, "fallback_dir": None}]
        for spec in args.comparison_run:
            label, separator, directory = spec.partition("=")
            if not separator or not label.strip() or not directory.strip():
                raise ValueError(f"Invalid --comparison_run value: {spec!r}; expected LABEL=DIR")
            runs.append(
                {
                    "label": label.strip(),
                    "preferred_dir": Path(directory.strip()),
                    "fallback_dir": None,
                }
            )

    for run in runs:
        source_dir, note = resolve_run_dir(run)
        source_notes.append(note)
        if source_dir is None:
            continue
        rows = rescore_run(run["label"], source_dir, output_dir)
        all_rows_by_run[run["label"]] = rows
        partitions = partition_summaries(rows)
        # Factual metrics deliberately exclude manual prompts without a reference answer.
        run_summaries[run["label"]] = partitions["reference_backed_factual_tests"]
        partitions_by_run[run["label"]] = partitions

    (output_dir / "strict_rescore_summary.json").write_text(
        json.dumps(run_summaries, indent=2),
        encoding="utf-8",
    )
    decisions: Dict[str, Any] = {}
    if args.baseline_label:
        if args.baseline_label not in run_summaries:
            raise ValueError(
                f"--baseline_label {args.baseline_label!r} was not found; available labels: {list(run_summaries)}"
            )
        baseline = run_summaries[args.baseline_label]
        decisions = {
            label: strict_holdout_gate(summary, baseline)
            for label, summary in run_summaries.items()
            if label != args.baseline_label
        }
        (output_dir / "strict_rescore_decision.json").write_text(
            json.dumps(
                {"baseline_label": args.baseline_label, "candidates": decisions},
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
    write_report(
        output_dir,
        run_summaries,
        all_rows_by_run,
        partitions_by_run,
        source_notes,
        args.baseline_label,
    )
    print(f"Strict rescore written to {output_dir}")
    for label, summary in run_summaries.items():
        print(
            f"{label}: total={summary['total_predictions']} avg={summary['average_score']:.2f} "
            f"good={summary['good_predictions_count']} bad={summary['bad_predictions_count']} "
            f"degenerate={summary['degenerate_predictions']} wrong_bug={summary['wrong_bug_id_predictions']} "
            f"fake_bug={summary['fake_bug_id_predictions']} wrong_cli={summary['wrong_cli_syntax_predictions']} "
            f"wrong_date={summary['wrong_date_predictions']}"
        )


if __name__ == "__main__":
    main()
