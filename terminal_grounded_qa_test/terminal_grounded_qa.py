from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
import sys
import re
from typing import Dict, Optional

import torch
from torch import nn
from torch.nn.utils.rnn import pack_padded_sequence

MODULE_DIR = Path(__file__).resolve().parent
if str(MODULE_DIR) not in sys.path:
    sys.path.insert(0, str(MODULE_DIR))

try:
    from .config import (
        ALLOWED_SWITCH_FAMILIES,
        MIN_LOOKUP_SCORE,
        MIN_MODEL_CONFIDENCE,
        PRODUCT_BILSTM_PATH,
        QWEN_MODEL_PATH,
        RELEASE_BILSTM_PATH,
        RELEASE_LIKE_INTENTS,
        SAFE_NO_MATCH,
        SYNTAX_LIKE_INTENTS,
    )
    from .entity_extract import extract_entities, extract_switch_candidates, normalize_switch_name, normalize_whitespace
    from .lookup import find_best_match, load_all_rows
    from .qwen_runner import QwenFormatter
except ImportError:  # pragma: no cover
    from config import (
        ALLOWED_SWITCH_FAMILIES,
        MIN_LOOKUP_SCORE,
        MIN_MODEL_CONFIDENCE,
        PRODUCT_BILSTM_PATH,
        QWEN_MODEL_PATH,
        RELEASE_BILSTM_PATH,
        RELEASE_LIKE_INTENTS,
        SAFE_NO_MATCH,
        SYNTAX_LIKE_INTENTS,
    )
    from entity_extract import extract_entities, extract_switch_candidates, normalize_switch_name, normalize_whitespace
    from lookup import find_best_match, load_all_rows
    from qwen_runner import QwenFormatter


class SimpleTokenizer:
    def __init__(self, vocab: Dict[str, int]) -> None:
        self.vocab = dict(vocab)
        self.pad_token = "<pad>"
        self.unk_token = "<unk>"
        self.vocab.setdefault(self.pad_token, 0)
        self.vocab.setdefault(self.unk_token, 1)

    @staticmethod
    def tokenize(text: str) -> list[str]:
        import re

        return re.findall(r"[A-Za-z0-9_]+|[^\w\s]", text.lower())

    def encode(self, text: str, max_length: int) -> list[int]:
        tokens = self.tokenize(text)[:max_length]
        if not tokens:
            tokens = [self.unk_token]
        return [self.vocab.get(token, self.vocab[self.unk_token]) for token in tokens]


class LSTMIntentModel(nn.Module):
    def __init__(
        self,
        vocab_size: int,
        embedding_dim: int,
        hidden_size: int,
        num_layers: int,
        num_labels: int,
        dropout: float,
    ) -> None:
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim, padding_idx=0)
        self.lstm = nn.LSTM(
            input_size=embedding_dim,
            hidden_size=hidden_size,
            num_layers=num_layers,
            batch_first=True,
            bidirectional=True,
        )
        self.dropout = nn.Dropout(dropout)
        self.classifier = nn.Linear(hidden_size * 2, num_labels)

    def forward(self, input_ids: torch.Tensor, lengths: torch.Tensor) -> torch.Tensor:
        embedded = self.dropout(self.embedding(input_ids))
        packed = pack_padded_sequence(embedded, lengths.cpu(), batch_first=True, enforce_sorted=False)
        _, (hidden, _) = self.lstm(packed)
        forward_hidden = hidden[-2]
        backward_hidden = hidden[-1]
        features = torch.cat([forward_hidden, backward_hidden], dim=1)
        features = self.dropout(features)
        return self.classifier(features)


@dataclass
class ModelBundle:
    name: str
    path: str
    model: nn.Module
    tokenizer: SimpleTokenizer
    label_names: list[str]
    max_length: int


def load_lstm_bundle(name: str, model_path: str, device: torch.device) -> ModelBundle:
    payload = torch.load(model_path, map_location=device)
    config = dict(payload.get("config", {}))
    tokenizer = SimpleTokenizer(payload["vocab"])
    label_names = list(config.get("label_names") or [value for _, value in sorted(dict(payload.get("id_to_label", {})).items())])
    model = LSTMIntentModel(
        vocab_size=len(tokenizer.vocab),
        embedding_dim=int(config.get("embedding_dim", 256)),
        hidden_size=int(config.get("hidden_size", 256)),
        num_layers=int(config.get("num_layers", 2)),
        num_labels=len(label_names),
        dropout=float(config.get("dropout", 0.3)),
    ).to(device)
    model.load_state_dict(payload["model_state_dict"])
    model.eval()
    return ModelBundle(
        name=name,
        path=model_path,
        model=model,
        tokenizer=tokenizer,
        label_names=label_names,
        max_length=int(config.get("max_length", 96)),
    )


def predict_intent(question: str, bundle: ModelBundle, device: torch.device) -> tuple[str, float]:
    cleaned = normalize_whitespace(question)
    ids = bundle.tokenizer.encode(cleaned, bundle.max_length)
    input_ids = torch.tensor([ids], dtype=torch.long, device=device)
    lengths = torch.tensor([len(ids)], dtype=torch.long, device=device)
    with torch.inference_mode():
        logits = bundle.model(input_ids, lengths)
        probabilities = torch.softmax(logits, dim=-1)[0]
    score, predicted_id = torch.max(probabilities, dim=-1)
    return bundle.label_names[int(predicted_id)], float(score.item())


class TerminalGroundedQA:
    def __init__(self) -> None:
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.release_bundle = load_lstm_bundle("release", str(RELEASE_BILSTM_PATH), self.device)
        self.product_bundle = load_lstm_bundle("product", str(PRODUCT_BILSTM_PATH), self.device)
        self.rows = load_all_rows()
        self.qwen = QwenFormatter(QWEN_MODEL_PATH)

    def predict(self, question: str) -> Dict[str, object]:
        release_intent, release_conf = predict_intent(question, self.release_bundle, self.device)
        product_intent, product_conf = predict_intent(question, self.product_bundle, self.device)
        if release_intent in RELEASE_LIKE_INTENTS:
            predicted_source = "release"
            predicted_intent = release_intent
            predicted_confidence = release_conf
        elif release_conf > product_conf + 0.12:
            predicted_source = "release"
            predicted_intent = release_intent
            predicted_confidence = release_conf
        else:
            predicted_source = "product"
            predicted_intent = product_intent
            predicted_confidence = product_conf
        return {
            "predicted_source": predicted_source,
            "predicted_intent": predicted_intent,
            "predicted_confidence": predicted_confidence,
            "model_votes": {
                "release": {"intent": release_intent, "confidence": release_conf},
                "product": {"intent": product_intent, "confidence": product_conf},
            },
        }

    @staticmethod
    def _has_release_note_cues(entities: Dict[str, str], question: str) -> bool:
        version = normalize_whitespace(entities.get("version_full") or entities.get("version"))
        switch = normalize_whitespace(entities.get("switch"))
        topic = normalize_whitespace(entities.get("topic"))
        feature = normalize_whitespace(entities.get("feature"))
        lowered = normalize_whitespace(question).lower()
        release_markers = (
            "mentioned",
            "caveat",
            "known issue",
            "known issues",
            "workaround",
            "resolved issue",
            "bug",
            "symptom",
            "scenario",
            "feature caveat",
            "user based tunnel",
            "ubt",
        )
        has_release_marker = any(marker in lowered for marker in release_markers)
        return bool(version and switch and (topic or feature) and has_release_marker)

    def _choose_lookup_source(
        self,
        question: str,
        predicted_source: str,
        raw_predicted_intent: str,
        question_type: str,
        entities: Dict[str, str],
    ) -> str:
        lookup_source = str(predicted_source)
        if question_type in {
            "cli_syntax",
            "cli_output",
            "support_matrix",
            "version_support",
            "configuration_procedure",
            "troubleshooting",
            "capacity_or_scale",
            "requirement",
            "caveat",
        }:
            return "product"
        if question_type == "limitation":
            if self._has_release_note_cues(entities, question):
                return "release"
            return "product"
        if raw_predicted_intent in RELEASE_LIKE_INTENTS:
            return "release"
        return lookup_source

    def _legacy_answer(self, question: str, selected_switch: str) -> Dict[str, object]:
        normalized_question = normalize_whitespace(question)
        prediction = self.predict(normalized_question)
        entities = extract_entities(normalized_question, str(prediction["predicted_intent"]))
        raw_predicted_intent = str(prediction["predicted_intent"])
        question_type = str(entities.get("question_type", ""))
        if self._looks_general(normalized_question, entities):
            final_answer = ""
            answer_mode = "general_qwen"
            bypass_qwen = False
            if self.qwen.available:
                try:
                    final_answer = self.qwen.answer_general(normalized_question)
                except Exception as exc:
                    final_answer = ""
                    lookup_error = str(exc)
                else:
                    lookup_error = ""
            else:
                lookup_error = "qwen_unavailable"
            if not final_answer:
                final_answer = self._safe_math_answer(normalized_question)
                if final_answer:
                    answer_mode = "general_math"
            if not final_answer:
                final_answer = "I can help with that. Try asking a more specific question."
                answer_mode = "general_fallback"
            return {
                **prediction,
                "raw_lstm_intent": raw_predicted_intent,
                "lookup_intent": "general",
                "extracted_entities": entities,
                "lookup_context": "general",
                "answer_mode": answer_mode,
                "matched_dataset_row": None,
                "target_value": "",
                "final_answer": final_answer,
                "lookup_status": lookup_error or "general_question",
                "lookup_score": 0.0,
                "top_candidates": [],
                "bypass_qwen": bypass_qwen,
            }
        lookup_intent = raw_predicted_intent
        if question_type in {
            "cli_syntax",
            "cli_output",
            "support_matrix",
            "version_support",
            "configuration_procedure",
            "troubleshooting",
            "capacity_or_scale",
            "limitation",
            "requirement",
            "caveat",
        }:
            lookup_intent = question_type
        lookup_source = str(prediction["predicted_source"])
        if question_type in {
            "cli_syntax",
            "cli_output",
            "support_matrix",
            "version_support",
            "configuration_procedure",
            "troubleshooting",
            "capacity_or_scale",
            "limitation",
            "requirement",
            "caveat",
        }:
            lookup_source = "product"
        elif raw_predicted_intent in RELEASE_LIKE_INTENTS:
            lookup_source = "release"
        lookup = find_best_match(
            question=normalized_question,
            predicted_source=lookup_source,
            predicted_intent=lookup_intent,
            entities=entities,
            selected_switch=selected_switch,
            rows=self.rows,
            min_lookup_score=MIN_LOOKUP_SCORE,
        )
        target_raw = lookup.get("target_value", "")
        target_value = str(target_raw).strip() if target_raw is not None else ""
        final_answer = SAFE_NO_MATCH
        bypass_qwen = True
        answer_mode = "no_match"
        if lookup.get("matched") and prediction["predicted_confidence"] >= MIN_MODEL_CONFIDENCE:
            final_answer = target_value
            if str(prediction["predicted_intent"]) not in SYNTAX_LIKE_INTENTS and entities.get("question_type") != "cli_syntax":
                bypass_qwen = False
                answer_mode = "grounded_qwen"
                try:
                    final_answer = self.qwen.format_conversational_answer(normalized_question, target_value)
                except Exception as exc:
                    final_answer = target_value
                    lookup["qwen_error"] = str(exc)
                    answer_mode = "grounded_raw"
            else:
                answer_mode = "grounded_raw"
        else:
            lookup["lookup_reason"] = lookup.get("lookup_reason", "low_confidence_or_no_match")
            if self._looks_general(normalized_question, entities):
                bypass_qwen = False
                answer_mode = "general_qwen"
                if self.qwen.available:
                    try:
                        final_answer = self.qwen.answer_general(normalized_question)
                    except Exception as exc:
                        lookup["qwen_error"] = str(exc)
                        final_answer = ""
                if not final_answer:
                    final_answer = self._safe_math_answer(normalized_question)
                    if final_answer:
                        answer_mode = "general_math"
                if not final_answer:
                    final_answer = "I’m not sure."
                    answer_mode = "general_fallback"
        return {
            **prediction,
            "raw_lstm_intent": raw_predicted_intent,
            "lookup_intent": lookup_intent,
            "extracted_entities": entities,
            "lookup_context": lookup.get("lookup_context"),
            "answer_mode": answer_mode,
            "matched_dataset_row": lookup.get("matched_row"),
            "target_value": target_value,
            "final_answer": final_answer,
            "lookup_status": lookup.get("lookup_reason"),
            "lookup_score": lookup.get("score", 0.0),
            "top_candidates": lookup.get("top_candidates", []),
            "bypass_qwen": bypass_qwen,
        }
    def answer(self, question: str, selected_switch: str) -> Dict[str, object]:
        normalized_question = normalize_whitespace(question)
        prediction = self.predict(normalized_question)
        entities = extract_entities(normalized_question, str(prediction["predicted_intent"]))
        raw_predicted_intent = str(prediction["predicted_intent"])
        question_type = str(entities.get("question_type", ""))

        lookup_intent = raw_predicted_intent
        if question_type in {
            "cli_syntax",
            "cli_output",
            "support_matrix",
            "version_support",
            "configuration_procedure",
            "troubleshooting",
            "capacity_or_scale",
            "limitation",
            "requirement",
            "caveat",
        }:
            lookup_intent = question_type
        lookup_source = self._choose_lookup_source(
            normalized_question,
            str(prediction["predicted_source"]),
            raw_predicted_intent,
            question_type,
            entities,
        )

        lookup = find_best_match(
            question=normalized_question,
            predicted_source=lookup_source,
            predicted_intent=lookup_intent,
            entities=entities,
            selected_switch=selected_switch,
            rows=self.rows,
            min_lookup_score=MIN_LOOKUP_SCORE,
        )
        target_raw = lookup.get("target_value", "")
        target_value = str(target_raw).strip() if target_raw is not None else ""
        matched_and_reliable = bool(lookup.get("matched")) and bool(target_value) and prediction["predicted_confidence"] >= MIN_MODEL_CONFIDENCE
        has_domain_signal = any(
            normalize_whitespace(entities.get(key, ""))
            for key in ("switch", "version", "version_full", "command", "topic", "feature", "bug_id")
        ) or question_type != "generic"
        lookup_context = str(lookup.get("lookup_context") or "")
        lookup_is_reliable = matched_and_reliable and (
            lookup_context == "selected_context" or has_domain_signal
        )
        is_syntax_question = (
            question_type in SYNTAX_LIKE_INTENTS
            or raw_predicted_intent in SYNTAX_LIKE_INTENTS
            or lookup_intent in SYNTAX_LIKE_INTENTS
        )

        final_answer = ""
        answer_mode = "qwen_fallback"
        grounded = False
        target_value_used = False
        bypass_qwen = False

        if lookup_is_reliable:
            grounded = True
            target_value_used = True
            if is_syntax_question:
                final_answer = target_value
                answer_mode = "direct_target_value"
                bypass_qwen = True
            else:
                answer_mode = "grounded_qwen"
                try:
                    final_answer = self.qwen.format_conversational_answer(normalized_question, target_value)
                except Exception as exc:
                    lookup["qwen_error"] = str(exc)
                    final_answer = target_value
                    answer_mode = "direct_target_value"
                    bypass_qwen = True
        else:
            if matched_and_reliable and lookup_context == "broader_context" and not has_domain_signal:
                lookup["lookup_reason"] = "broader_context_not_reliable"
            else:
                lookup["lookup_reason"] = lookup.get("lookup_reason", "low_confidence_or_no_match")
            if self.qwen.available:
                try:
                    final_answer = self.qwen.answer_general(normalized_question)
                except Exception as exc:
                    lookup["qwen_error"] = str(exc)
                    final_answer = ""
            if not final_answer:
                final_answer = "I'm not sure."

        return {
            **prediction,
            "raw_lstm_intent": raw_predicted_intent,
            "lookup_intent": lookup_intent,
            "extracted_entities": entities,
            "lookup_context": lookup.get("lookup_context"),
            "answer_mode": answer_mode,
            "grounded": grounded,
            "target_value_used": target_value_used,
            "matched_dataset_row": lookup.get("matched_row"),
            "target_value": target_value,
            "final_answer": final_answer,
            "lookup_status": lookup.get("lookup_reason"),
            "lookup_score": lookup.get("score", 0.0),
            "top_candidates": lookup.get("top_candidates", []),
            "bypass_qwen": bypass_qwen,
        }


def prompt_switch_family() -> str:
    print("Allowed switch families:")
    for value in ALLOWED_SWITCH_FAMILIES:
        print(f"- {value}")
    while True:
        selected = normalize_switch_name(input("\nEnter switch family: "))
        if selected in ALLOWED_SWITCH_FAMILIES:
            return selected
        print("Invalid switch family. Please choose one from the allowed list.")


def maybe_switch_context(selected_switch: str) -> Optional[str]:
    while True:
        answer = normalize_whitespace(
            input(f"Switch family [{selected_switch}] (Enter to keep): ")
        )
        if not answer:
            return selected_switch
        if answer.lower() in {"exit", "quit"}:
            return None
        question_switch = normalize_switch_name(answer)
        if question_switch in ALLOWED_SWITCH_FAMILIES:
            return question_switch
        print("Invalid switch family. Please choose one from the allowed list.")


def switch_from_question(question: str, current_switch: str) -> Optional[str]:
    candidates = extract_switch_candidates(question)
    for candidate in candidates:
        normalized = normalize_switch_name(candidate)
        if normalized in ALLOWED_SWITCH_FAMILIES and normalized != current_switch:
            return normalized
    return None


def print_result(result: Dict[str, object]) -> None:
    print("\nPredicted source/intent:")
    print(f"- source: {result['predicted_source']}")
    print(f"- intent: {result['predicted_intent']}")
    print(f"- confidence: {result['predicted_confidence']:.4f}")
    if result.get("raw_lstm_intent"):
        print(f"- raw_lstm_intent: {result['raw_lstm_intent']}")
    if result.get("lookup_intent"):
        print(f"- lookup_intent: {result['lookup_intent']}")
    print("\nExtracted entities:")
    print(json.dumps(result["extracted_entities"], indent=2, ensure_ascii=False))
    print("\nModel votes:")
    print(json.dumps(result.get("model_votes", {}), indent=2, ensure_ascii=False))
    print("\nMatched dataset row:")
    print(json.dumps(result["matched_dataset_row"], indent=2, ensure_ascii=False) if result["matched_dataset_row"] else "None")
    print("\nTarget value:")
    print(result["target_value"] or SAFE_NO_MATCH)
    print("\nFinal answer:")
    print(result["final_answer"])
    if result.get("answer_mode"):
        print(f"Answer mode: {result['answer_mode']}")
    if "grounded" in result:
        print(f"Grounded: {result['grounded']}")
    if "target_value_used" in result:
        print(f"Target value used: {result['target_value_used']}")
    print(f"\nLookup status: {result['lookup_status']}")
    if result.get("lookup_context"):
        print(f"Lookup context: {result['lookup_context']}")
    print(f"Lookup score: {float(result['lookup_score']):.2f}")
    print(f"Bypass Qwen: {result['bypass_qwen']}")
    top_candidates = result.get("top_candidates", [])
    if top_candidates:
        print("\nTop candidates:")
        for candidate in top_candidates:
            row = candidate.get("row", {}) if isinstance(candidate, dict) else {}
            status = candidate.get("status", "unknown") if isinstance(candidate, dict) else "unknown"
            score = float(candidate.get("score", 0.0) or 0.0) if isinstance(candidate, dict) else 0.0
            intent = row.get("intent", "") if isinstance(row, dict) else ""
            summary_bits = [f"- #{candidate.get('rank', '?')} {status} score={score:.2f} intent={intent}"]
            if isinstance(row, dict):
                if row.get("switch"):
                    summary_bits.append(f"switch={row['switch']}")
                if row.get("version_full"):
                    summary_bits.append(f"version={row['version_full']}")
                if row.get("command"):
                    summary_bits.append(f"command={row['command']}")
                if row.get("feature"):
                    summary_bits.append(f"feature={row['feature']}")
                if row.get("topic"):
                    summary_bits.append(f"topic={row['topic']}")
            reason = candidate.get("rejection_reason") if isinstance(candidate, dict) else None
            if reason:
                summary_bits.append(f"reason={reason}")
            print(" | ".join(summary_bits))


def main() -> None:
    qa = TerminalGroundedQA()
    selected_switch = prompt_switch_family()
    print(f"\nLoaded models on: {qa.device}")
    print(f"Release BiLSTM: {RELEASE_BILSTM_PATH}")
    print(f"Product BiLSTM: {PRODUCT_BILSTM_PATH}")
    print("Type 'exit' to quit.\n")
    while True:
        next_switch = maybe_switch_context(selected_switch)
        if next_switch is None:
            break
        selected_switch = next_switch
        print(f"\nUsing switch context: {selected_switch}")
        question = normalize_whitespace(input("Question: "))
        if not question:
            continue
        if question.lower() in {"exit", "quit"}:
            break
        question_switch = switch_from_question(question, selected_switch)
        if question_switch is not None:
            if question_switch != selected_switch:
                print(f"Auto-switched switch context from {selected_switch} to {question_switch} based on the question.")
                selected_switch = question_switch
                print(f"Using switch context: {selected_switch}")
        result = qa.answer(question, selected_switch)
        print_result(result)
        print()


if __name__ == "__main__":
    main()
