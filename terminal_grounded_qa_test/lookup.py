from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

try:
    from .config import (
        CAPACITY_OR_SCALE_KEYWORDS,
        CAPACITY_OR_SCALE_PENALTY_KEYWORDS,
        INTENT_ALIAS_MAP,
        PRODUCT_AGGREGATE_PATHS,
        PRODUCT_FALLBACK_ROOTS,
        PRODUCT_INTENT_CANONICAL_MAP,
        MANUAL_GROUNDED_OVERRIDE_PATH,
        PRODUCT_VALIDATED_DATA_PATH,
        RELEASE_DATA_ROOT,
        RELEASE_LIKE_INTENTS,
        SAFE_NO_MATCH,
        SYNTHETIC_DATA_PATHS,
        TOP_K_CANDIDATES,
    )
    from .entity_extract import extract_entities, normalize_switch_name, normalize_whitespace
except ImportError:  # pragma: no cover
    from config import (
        CAPACITY_OR_SCALE_KEYWORDS,
        CAPACITY_OR_SCALE_PENALTY_KEYWORDS,
        INTENT_ALIAS_MAP,
        PRODUCT_AGGREGATE_PATHS,
        PRODUCT_FALLBACK_ROOTS,
        PRODUCT_INTENT_CANONICAL_MAP,
        MANUAL_GROUNDED_OVERRIDE_PATH,
        PRODUCT_VALIDATED_DATA_PATH,
        RELEASE_DATA_ROOT,
        RELEASE_LIKE_INTENTS,
        SAFE_NO_MATCH,
        SYNTHETIC_DATA_PATHS,
        TOP_K_CANDIDATES,
    )
    from entity_extract import extract_entities, normalize_switch_name, normalize_whitespace


@dataclass
class GroundedRow:
    source: str
    dataset_name: str
    input_text: str
    intent: str
    target_value: str
    slots: Dict[str, str]
    switch: str = ""
    version: str = ""
    sub_version: str = ""
    version_full: str = ""
    command: str = ""
    feature: str = ""
    topic: str = ""
    bug_id: str = ""
    source_file: str = ""
    raw: Dict[str, Any] = field(default_factory=dict, repr=False)


def read_jsonl(path: Path) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            raw = line.strip()
            if not raw:
                continue
            try:
                value = json.loads(raw)
            except json.JSONDecodeError:
                continue
            if isinstance(value, dict):
                rows.append(value)
    return rows


def dotted_version(version: str, sub_version: str = "") -> str:
    base = normalize_whitespace(version).replace("_", ".")
    sub = normalize_whitespace(sub_version)
    if base and sub and base.count(".") == 1:
        return f"{base}.{sub}"
    return base


def infer_release_intent(row: Dict[str, Any], question: str) -> str:
    source_type = normalize_whitespace(row.get("source_type", "")).lower()
    lowered = normalize_whitespace(question).lower()
    if source_type == "release_notes_resolved_issues":
        if "category" in lowered:
            return "bug_category"
        if "workaround" in lowered:
            return "bug_workaround"
        if "scenario" in lowered:
            return "bug_scenario"
        return "bug_symptom"
    if source_type == "release_notes_known_issues":
        if "workaround" in lowered:
            return "bug_workaround"
        if "scenario" in lowered:
            return "bug_scenario"
        return "bug_symptom"
    if source_type == "release_notes_caveats":
        return "release_caveat"
    if source_type == "release_notes_version_history":
        return "release_date"
    if source_type == "release_notes_upgrade_procedure":
        return "configuration_procedure"
    if source_type == "release_notes_downgrade_restore":
        return "configuration_procedure"
    if source_type == "release_notes_supported_products":
        return "support_matrix"
    if source_type == "release_notes_compatibility":
        return "requirement"
    if source_type == "release_notes_certifications":
        return "concept_explanation"
    return "concept_explanation"


def _message_value(messages: Any, index: int) -> str:
    if not isinstance(messages, list) or len(messages) <= index or not isinstance(messages[index], dict):
        return ""
    return normalize_whitespace(messages[index].get("content", ""))


def _product_labels(raw: Dict[str, Any]) -> Dict[str, Any]:
    labels = raw.get("labels")
    return labels if isinstance(labels, dict) else {}


def _product_slots(raw: Dict[str, Any], labels: Dict[str, Any]) -> Dict[str, str]:
    slots: Dict[str, str] = {}
    for candidate in (raw.get("slots"), labels.get("slots")):
        if not isinstance(candidate, dict):
            continue
        for key, value in candidate.items():
            normalized_value = normalize_whitespace(value)
            if normalized_value:
                slots[normalize_whitespace(key)] = normalized_value
    return slots


def _product_intent(raw: Dict[str, Any], labels: Dict[str, Any]) -> str:
    intent = normalize_whitespace(raw.get("intent", "")) or normalize_whitespace(labels.get("intent", ""))
    if not intent:
        intent = normalize_whitespace(labels.get("answer_type", "")) or normalize_whitespace(raw.get("answer_type", ""))
    canonical = PRODUCT_INTENT_CANONICAL_MAP.get(intent.lower(), intent)
    return normalize_whitespace(canonical)


def _product_target_value(raw: Dict[str, Any], labels: Dict[str, Any]) -> str:
    for candidate in (
        raw.get("target_value"),
        raw.get("final_answer"),
        labels.get("target_value"),
        labels.get("final_answer"),
        labels.get("answer_text"),
        raw.get("answer_text"),
    ):
        if candidate is None:
            continue
        text = str(candidate).strip()
        if text:
            return text
    return ""


def _dedupe_product_row_key(row: GroundedRow) -> tuple[str, ...]:
    return (
        normalize_whitespace(row.source).lower(),
        normalize_whitespace(row.dataset_name).lower(),
        normalize_whitespace(row.switch).lower(),
        normalize_whitespace(row.version_full).lower(),
        normalize_whitespace(row.intent).lower(),
        normalize_whitespace(row.command).lower(),
        normalize_whitespace(row.topic).lower(),
        normalize_whitespace(row.target_value).lower(),
    )


def load_release_rows() -> List[GroundedRow]:
    rows: List[GroundedRow] = []
    if not RELEASE_DATA_ROOT.exists():
        return rows
    for path in sorted(RELEASE_DATA_ROOT.rglob("train_chat.jsonl")):
        for raw in read_jsonl(path):
            question = _message_value(raw.get("messages"), 0)
            answer = _message_value(raw.get("messages"), 1)
            if not question or not answer:
                continue
            switch = normalize_switch_name(raw.get("switch", ""))
            version = normalize_whitespace(raw.get("version", ""))
            sub_version = normalize_whitespace(raw.get("sub_version", ""))
            version_full = dotted_version(version, sub_version)
            slots = {
                "switch": switch,
                "version": version.replace("_", "."),
                "sub_version": sub_version,
                "version_full": version_full,
                "feature": normalize_whitespace(raw.get("feature", "")),
                "bug_id": normalize_whitespace(raw.get("bug_id", "")),
                "category": normalize_whitespace(raw.get("category", "")),
                "topic": normalize_whitespace(raw.get("section", "")),
            }
            rows.append(
                GroundedRow(
                    source="release",
                    dataset_name="release_notes",
                    input_text=question,
                    intent=infer_release_intent(raw, question),
                    target_value=answer,
                    slots={key: value for key, value in slots.items() if value},
                    switch=switch,
                    version=version.replace("_", "."),
                    sub_version=sub_version,
                    version_full=version_full,
                    feature=slots.get("feature", ""),
                    topic=slots.get("topic", ""),
                    bug_id=slots.get("bug_id", ""),
                    source_file=str(path),
                    raw=raw,
                )
            )
    return rows


def _row_from_product(raw: Dict[str, Any], dataset_name: str, source_file: str, source: str) -> Optional[GroundedRow]:
    labels = _product_labels(raw)
    question = normalize_whitespace(
        raw.get("input_text", "")
        or labels.get("input_text", "")
        or raw.get("question", "")
        or labels.get("question", "")
        or raw.get("prompt", "")
        or labels.get("prompt", "")
    )
    intent = _product_intent(raw, labels)
    target_value = _product_target_value(raw, labels)
    slots = _product_slots(raw, labels)
    if not question or not intent or not target_value:
        return None
    switch = normalize_switch_name(slots.get("switch", ""))
    version_full = normalize_whitespace(slots.get("version_full", "") or slots.get("version", "") or labels.get("version_full", "") or labels.get("version", ""))
    version_parts = version_full.split(".")
    version = ".".join(version_parts[:2]) if len(version_parts) >= 2 else version_full
    sub_version = version_parts[2] if len(version_parts) >= 3 else ""
    topic = normalize_whitespace(slots.get("topic", "") or labels.get("topic", ""))
    feature = normalize_whitespace(slots.get("feature", "") or labels.get("feature", ""))
    command = normalize_whitespace(slots.get("command", "") or labels.get("command", ""))
    return GroundedRow(
        source=source,
        dataset_name=dataset_name,
        input_text=question,
        intent=intent,
        target_value=target_value,
        slots={normalize_whitespace(k): normalize_whitespace(v) for k, v in slots.items() if normalize_whitespace(v)},
        switch=switch,
        version=version,
        sub_version=sub_version,
        version_full=version_full or dotted_version(version, sub_version),
        command=command,
        feature=feature,
        topic=topic,
        bug_id=normalize_whitespace(slots.get("bug_id", "") or labels.get("bug_id", "")),
        source_file=source_file,
        raw=raw,
    )


def load_product_rows() -> List[GroundedRow]:
    rows: List[GroundedRow] = []
    seen: set[tuple[str, ...]] = set()

    def add_rows(paths: Iterable[Path], dataset_name: str, source: str) -> None:
        for path in paths:
            if not path.exists() or not path.is_file():
                continue
            for raw in read_jsonl(path):
                row = _row_from_product(raw, dataset_name, str(path), source)
                if row is None:
                    continue
                key = _dedupe_product_row_key(row)
                if key in seen:
                    continue
                seen.add(key)
                rows.append(row)

    add_rows([MANUAL_GROUNDED_OVERRIDE_PATH], "manual_override", "product")
    add_rows([PRODUCT_VALIDATED_DATA_PATH], "product_docs_validated", "product")
    add_rows(PRODUCT_AGGREGATE_PATHS, "product_docs", "product")
    fallback_paths: List[Path] = []
    for root in PRODUCT_FALLBACK_ROOTS:
        if not root.exists():
            continue
        fallback_paths.extend(
            path
            for pattern in ("product_dataset_repaired.jsonl", "product_dataset_final.jsonl", "all_switches_product_dataset_final.jsonl")
            for path in sorted(root.rglob(pattern))
        )
    add_rows(fallback_paths, "product_docs", "product")
    add_rows(SYNTHETIC_DATA_PATHS, "synthetic_merged", "synthetic")
    return rows


def load_synthetic_rows() -> List[GroundedRow]:
    rows: List[GroundedRow] = []
    seen_questions: set[tuple[str, str]] = set()
    for path in SYNTHETIC_DATA_PATHS:
        if not path.exists():
            continue
        for raw in read_jsonl(path):
            row = _row_from_product(raw, "synthetic_merged", str(path), "synthetic")
            if row is None:
                continue
            key = (row.input_text.lower(), row.intent.lower())
            if key in seen_questions:
                continue
            seen_questions.add(key)
            rows.append(row)
    return rows


def load_all_rows() -> List[GroundedRow]:
    return load_release_rows() + load_product_rows() + load_synthetic_rows()


def _tokenize(text: str) -> List[str]:
    return re.findall(r"[A-Za-z0-9_]+", normalize_whitespace(text).lower())


def _switch_tokens(value: str) -> List[str]:
    return [token for token in normalize_whitespace(value).split("_") if token]


def switch_matches(selected_switch: str, row_switch: str, allow_groups: bool) -> bool:
    selected = normalize_switch_name(selected_switch).lower()
    row_value = normalize_switch_name(row_switch).lower()
    if not selected or not row_value:
        return False
    if selected == row_value:
        return True
    if not allow_groups:
        return False
    return selected in [token.lower() for token in _switch_tokens(row_value)]


def _same_intent_family(predicted_intent: str, row_intent: str, question_type: str) -> bool:
    left = predicted_intent.lower()
    right = row_intent.lower()
    if left == right:
        return True
    syntax_family = {"cli_syntax", "show_command_syntax"}
    output_family = {"cli_output", "cli_meaning", "show_command_meaning", "event_log_meaning", "event_id_meaning", "snmp_mib_info"}
    explanation_family = {
        "cli_meaning",
        "concept_explanation",
        "configuration_procedure",
        "product_caveat",
        "product_limitation",
        "product_requirement",
        "troubleshooting",
        "support_matrix",
        "version_support",
        "capacity_or_scale",
        "requirement",
        "limitation",
    }
    release_family = RELEASE_LIKE_INTENTS
    if left in syntax_family and right in syntax_family:
        return True
    if left in output_family and right in output_family:
        return True
    if left in explanation_family and right in explanation_family:
        return True
    if left in release_family and right in release_family:
        return True
    if question_type == "cli_syntax" and right in syntax_family:
        return True
    if question_type == "cli_output" and right in output_family:
        return True
    return False


def _normalize_intent(value: str) -> str:
    return normalize_whitespace(value).lower()


def _allowed_row_intents(predicted_intent: str) -> set[str]:
    normalized = _normalize_intent(predicted_intent)
    aliases = {_normalize_intent(alias) for alias in INTENT_ALIAS_MAP.get(normalized, set())}
    aliases.add(normalized)
    return aliases


def _intent_rejection_reason(predicted_intent: str, row_intent: str) -> Optional[str]:
    normalized_predicted = _normalize_intent(predicted_intent)
    normalized_row = _normalize_intent(row_intent)
    if not normalized_predicted or not normalized_row:
        return "missing_intent_metadata"
    if normalized_row in _allowed_row_intents(normalized_predicted):
        return None
    return f"intent mismatch: predicted {normalized_predicted} does not allow {normalized_row}"


def _text_has_any(text: str, phrases: Iterable[str]) -> bool:
    lowered = normalize_whitespace(text).lower()
    return any(phrase in lowered for phrase in phrases)


def _capacity_or_scale_score_adjustment(question: str, row: GroundedRow, entities: Dict[str, str]) -> float:
    predicted_intent = _normalize_intent(entities.get("predicted_intent", ""))
    question_type = _normalize_intent(entities.get("question_type", ""))
    if predicted_intent != "capacity_or_scale" and question_type != "capacity_or_scale":
        return 0.0

    combined_text = " ".join(
        normalize_whitespace(part)
        for part in (row.input_text, row.target_value, row.topic, row.feature)
        if normalize_whitespace(part)
    )
    bonus = 0.0
    if _text_has_any(combined_text, CAPACITY_OR_SCALE_KEYWORDS):
        bonus += 12.0
    if _text_has_any(combined_text, ("route scale", "capacity", "maximum routes", "supported route scale")):
        bonus += 8.0
    if _text_has_any(combined_text, ("member number range", "stack members")):
        bonus += 8.0
    if _text_has_any(combined_text, CAPACITY_OR_SCALE_PENALTY_KEYWORDS):
        bonus -= 10.0
    if _text_has_any(combined_text, ("minimum version", "supports versions", "supported versions", "version support")):
        bonus -= 8.0
    question_lower = normalize_whitespace(question).lower()
    if any(phrase in question_lower for phrase in ("route scale", "maximum routes", "supported route scale", "capacity")) and any(
        phrase in normalize_whitespace(row.input_text).lower() for phrase in ("route scale", "capacity", "maximum routes", "supported route scale")
    ):
        bonus += 6.0
    if any(phrase in question_lower for phrase in ("supported capacity", "member number range")) and any(
        phrase in combined_text.lower() for phrase in ("member number range", "up to", "range")
    ):
        bonus += 6.0
    return bonus


def _field_score(query_value: str, row_value: str) -> float:
    left = normalize_whitespace(query_value).lower()
    right = normalize_whitespace(row_value).lower()
    if not left or not right:
        return 0.0
    if left == right:
        return 1.0
    if left in right or right in left:
        return 0.82
    return SequenceMatcher(None, left, right).ratio()


def _row_score(question: str, predicted_intent: str, entities: Dict[str, str], row: GroundedRow, selected_switch: str) -> float:
    question_type = normalize_whitespace(entities.get("question_type", ""))
    query_command = normalize_whitespace(entities.get("command", "")).lower()
    row_command = normalize_whitespace(row.command).lower()
    query_topic = normalize_whitespace(entities.get("topic", "")).lower()
    row_topic = normalize_whitespace(row.topic).lower()
    query_feature = normalize_whitespace(entities.get("feature", "")).lower()
    row_feature = normalize_whitespace(row.feature).lower()
    score = 0.0
    if switch_matches(selected_switch, row.switch, allow_groups=False):
        score += 42.0
    elif switch_matches(selected_switch, row.switch, allow_groups=True):
        score += 28.0
    if entities.get("version_full"):
        version_score = _field_score(entities["version_full"], row.version_full or row.version)
        if version_score >= 0.99:
            score += 24.0
        elif version_score >= 0.75:
            score += 15.0
    elif entities.get("version"):
        version_score = _field_score(entities["version"], row.version)
        if version_score >= 0.99:
            score += 18.0
        elif version_score >= 0.75:
            score += 12.0
    if entities.get("bug_id") and entities["bug_id"] == row.bug_id:
        score += 24.0
    if query_command:
        if query_command == row_command:
            score += 60.0
        elif query_command in row_command or row_command in query_command:
            score += 40.0
        else:
            command_score = max(_field_score(query_command, row_command), _field_score(query_command, row.input_text))
            score += command_score * 22.0
    if query_topic:
        if query_topic == row_topic:
            score += 18.0
        elif query_topic in row_topic or row_topic in query_topic:
            score += 12.0
        else:
            topic_score = max(_field_score(query_topic, row_topic), _field_score(query_topic, row_feature), _field_score(query_topic, row.input_text))
            score += topic_score * 16.0
    if query_feature:
        if query_feature == row_feature:
            score += 14.0
        elif query_feature in row_feature or row_feature in query_feature:
            score += 10.0
        else:
            feature_score = max(_field_score(query_feature, row_feature), _field_score(query_feature, row_topic), _field_score(query_feature, row.input_text))
            score += feature_score * 16.0

    normalized_predicted = _normalize_intent(predicted_intent)
    normalized_row = _normalize_intent(row.intent)
    if normalized_predicted and normalized_predicted == normalized_row:
        score += 20.0
    elif normalized_row in _allowed_row_intents(normalized_predicted):
        score += 12.0
    if _same_intent_family(predicted_intent, row.intent, question_type):
        score += 14.0
    if row.dataset_name == "manual_override":
        score += 30.0
    elif row.dataset_name == "product_docs_validated":
        score += 16.0
    elif row.dataset_name == "product_docs":
        score += 8.0
    elif row.source == "synthetic":
        score -= 8.0
    text_ratio = SequenceMatcher(None, question.lower(), row.input_text.lower()).ratio()
    overlap_left = set(_tokenize(question))
    overlap_right = set(_tokenize(row.input_text))
    overlap = len(overlap_left & overlap_right) / max(1, len(overlap_left | overlap_right))
    score += text_ratio * 11.0
    score += overlap * 12.0
    if question_type == "cli_syntax" and normalized_row in {"cli_syntax", "show_command_syntax"}:
        score += 30.0
    elif question_type == "cli_syntax" and query_command:
        score -= 35.0
    if question_type == "cli_output" and row.intent not in {"cli_output", "show_command_meaning", "event_log_meaning", "event_id_meaning", "snmp_mib_info"}:
        score -= 12.0
    if question_type == "cli_output" and normalized_row in {"cli_output", "show_command_meaning", "event_log_meaning", "event_id_meaning", "snmp_mib_info"}:
        score += 16.0
    if question_type == "support_matrix" and normalized_row in {"support_matrix", "version_support"}:
        score += 16.0
    if question_type == "configuration_procedure" and normalized_row == "configuration_procedure":
        score += 16.0
    if question_type == "troubleshooting" and normalized_row == "troubleshooting":
        score += 16.0
    score += _capacity_or_scale_score_adjustment(question, row, {**entities, "predicted_intent": predicted_intent})
    return score


def _manual_override_exact_match(question: str, rows: Iterable[GroundedRow]) -> Optional[GroundedRow]:
    normalized_question = normalize_whitespace(question).lower()
    if not normalized_question:
        return None
    for row in rows:
        if row.dataset_name != "manual_override":
            continue
        if normalize_whitespace(row.input_text).lower() == normalized_question:
            return row
    return None


def summarize_row(row: GroundedRow) -> Dict[str, Any]:
    return {
        "source": row.source,
        "dataset_name": row.dataset_name,
        "intent": row.intent,
        "switch": row.switch,
        "version": row.version,
        "sub_version": row.sub_version,
        "version_full": row.version_full,
        "command": row.command,
        "feature": row.feature,
        "topic": row.topic,
        "bug_id": row.bug_id,
        "input_text": row.input_text,
        "source_file": row.source_file,
        "slots": row.slots,
    }


def find_best_match(
    question: str,
    predicted_source: str,
    predicted_intent: str,
    entities: Dict[str, str],
    selected_switch: str,
    rows: Iterable[GroundedRow],
    min_lookup_score: float,
) -> Dict[str, Any]:
    question = normalize_whitespace(question)
    all_rows = list(rows)
    exact_override = _manual_override_exact_match(question, all_rows)
    if exact_override is not None:
        override_row = summarize_row(exact_override)
        return {
            "matched": True,
            "final_answer": exact_override.target_value,
            "lookup_reason": "manual_override_exact_match",
            "lookup_context": "selected_context",
            "matched_row": override_row,
            "target_value": exact_override.target_value,
            "score": 999.0,
            "rejected_candidates": [],
            "top_candidates": [
                {
                    "rank": 1,
                    "score": 999.0,
                    "status": "selected",
                    "rejection_reason": None,
                    "row": override_row,
                }
            ],
        }
    preferred_sources = {"release"} if predicted_source == "release" else {"product", "synthetic"}

    def build_scope_candidates(allow_groups: bool, broaden: bool) -> List[GroundedRow]:
        if broaden:
            return [row for row in all_rows if row.source in preferred_sources]
        return [
            row
            for row in all_rows
            if row.source in preferred_sources and switch_matches(selected_switch, row.switch, allow_groups=allow_groups)
        ]

    def rank_candidates(scope_rows: List[GroundedRow]) -> List[Dict[str, Any]]:
        return sorted(
            (
                {
                    "row": row,
                    "score": _row_score(question, predicted_intent, entities, row, selected_switch),
                }
                for row in scope_rows
            ),
            key=lambda item: item["score"],
            reverse=True,
        )

    def choose_from_ranked(ranked: List[Dict[str, Any]], scope_name: str) -> Dict[str, Any]:
        if not ranked:
            return {
                "matched": False,
                "final_answer": SAFE_NO_MATCH,
                "lookup_reason": f"no_ranked_candidates:{scope_name}",
                "lookup_context": scope_name,
                "matched_row": None,
                "target_value": "",
                "score": 0.0,
                "rejected_candidates": [],
                "top_candidates": [],
            }

        selected_candidate: Optional[Dict[str, Any]] = None
        for item in ranked:
            row = item["row"]
            score = float(item["score"])
            rejection_reason = _intent_rejection_reason(predicted_intent, row.intent)
            if rejection_reason is None and score < min_lookup_score:
                rejection_reason = f"score {score:.2f} below minimum {min_lookup_score:.2f}"
            if rejection_reason is None:
                selected_candidate = item
                break

        if selected_candidate is None:
            candidate_reviews: List[Dict[str, Any]] = []
            for index, item in enumerate(ranked[:TOP_K_CANDIDATES], start=1):
                row = item["row"]
                score = float(item["score"])
                rejection_reason = _intent_rejection_reason(predicted_intent, row.intent)
                if rejection_reason is None and score < min_lookup_score:
                    rejection_reason = f"score {score:.2f} below minimum {min_lookup_score:.2f}"
                candidate_reviews.append(
                    {
                        "rank": index,
                        "score": score,
                        "status": "rejected",
                        "rejection_reason": rejection_reason or "no eligible candidate",
                        "row": summarize_row(row),
                    }
                )
            return {
                "matched": False,
                "final_answer": SAFE_NO_MATCH,
                "lookup_reason": f"no_eligible_candidate:{scope_name}",
                "lookup_context": scope_name,
                "matched_row": None,
                "target_value": "",
                "score": 0.0,
                "rejected_candidates": candidate_reviews,
                "top_candidates": candidate_reviews,
            }

        best = selected_candidate
        top_candidates: List[Dict[str, Any]] = []
        for index, item in enumerate(ranked[:TOP_K_CANDIDATES], start=1):
            row = item["row"]
            score = float(item["score"])
            rejection_reason = _intent_rejection_reason(predicted_intent, row.intent)
            if rejection_reason is None and score < min_lookup_score:
                rejection_reason = f"score {score:.2f} below minimum {min_lookup_score:.2f}"
            if row is best["row"]:
                rejection_reason = None
                status = "selected"
            else:
                status = "rejected"
                if rejection_reason is None:
                    rejection_reason = "lower score than selected candidate"
            top_candidates.append(
                {
                    "rank": index,
                    "score": score,
                    "status": status,
                    "rejection_reason": rejection_reason,
                    "row": summarize_row(row),
                }
            )
        return {
            "matched": True,
            "final_answer": best["row"].target_value,
            "lookup_reason": f"matched:{scope_name}",
            "lookup_context": scope_name,
            "matched_row": summarize_row(best["row"]),
            "target_value": best["row"].target_value,
            "score": best["score"],
            "rejected_candidates": [item for item in top_candidates if item.get("status") != "selected"],
            "top_candidates": top_candidates,
        }

    selected_scope_rows = build_scope_candidates(allow_groups=False, broaden=False)
    if not selected_scope_rows:
        selected_scope_rows = build_scope_candidates(allow_groups=True, broaden=False)
    selected_attempt = choose_from_ranked(rank_candidates(selected_scope_rows), "selected_context")
    if selected_attempt["matched"]:
        return selected_attempt

    broader_scope_rows = build_scope_candidates(allow_groups=True, broaden=True)
    broader_attempt = choose_from_ranked(rank_candidates(broader_scope_rows), "broader_context")
    if broader_attempt["matched"]:
        return broader_attempt

    if selected_attempt.get("top_candidates"):
        selected_attempt["lookup_reason"] = "selected_context_exhausted"
    if broader_attempt.get("top_candidates"):
        broader_attempt["lookup_reason"] = "broader_context_exhausted"
    return broader_attempt if broader_attempt.get("top_candidates") else selected_attempt
