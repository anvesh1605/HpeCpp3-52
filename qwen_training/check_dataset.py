import argparse
import json
import math
import re
from collections import Counter
from pathlib import Path
from typing import Any, Dict, List, Tuple


VALID_ROLES = {"system", "user", "assistant"}
REQUIRED_FIELDS = ("source_type", "data_family", "switch", "version", "sub_version")
PRODUCT_PREFIX = "product_"
RELEASE_PREFIX = "release_notes_"
PRODUCT_FAMILIES = {
    "cli_command_reference",
    "show_command_reference",
    "concept_explanation",
    "configuration_procedure",
    "event_log_reference",
    "security_policy",
    "routing_feature",
    "qos_policy",
    "monitoring_feature",
    "troubleshooting",
}

PLACEHOLDER_PATTERNS = [
    r"^(todo|tbd|placeholder|n/?a|none|null|unknown)\.?$",
    r"^lorem ipsum\b",
    r"^answer goes here\.?$",
    r"^not available\.?$",
    r"^coming soon\.?$",
]


def normalize_text(value: Any, preserve_newlines: bool = False) -> str:
    text = str(value or "")
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    if preserve_newlines:
        lines = [re.sub(r"[ \t]+", " ", line).strip() for line in text.split("\n")]
        return "\n".join(line for line in lines if line).strip()
    return re.sub(r"\s+", " ", text).strip()


def word_count(text: str) -> int:
    return len(re.findall(r"\b\S+\b", text or ""))


def is_bad_scalar(value: Any) -> bool:
    if value is None:
        return True
    if isinstance(value, float) and math.isnan(value):
        return True
    if isinstance(value, str) and value.strip().lower() in {"nan", "none", "null"}:
        return True
    return False


def has_null_or_nan(value: Any) -> bool:
    if is_bad_scalar(value):
        return True
    if isinstance(value, dict):
        return any(has_null_or_nan(item) for item in value.values())
    if isinstance(value, list):
        return any(has_null_or_nan(item) for item in value)
    return False


def canonical(text: str) -> str:
    return re.sub(r"\s+", " ", normalize_text(text).lower()).strip()


def first_content(messages: Any, role: str) -> str:
    if not isinstance(messages, list):
        return ""
    for message in messages:
        if isinstance(message, dict) and normalize_text(message.get("role", "")).lower() == role:
            return normalize_text(message.get("content", ""), preserve_newlines=(role == "assistant"))
    return ""


def placeholder_answer(answer: str) -> bool:
    text = normalize_text(answer).lower()
    if not text or len(text) <= 4:
        return True
    return any(re.search(pattern, text, flags=re.IGNORECASE) for pattern in PLACEHOLDER_PATTERNS)


def domain(row: Dict[str, Any]) -> str:
    source_type = normalize_text(row.get("source_type", "")).lower()
    data_family = normalize_text(row.get("data_family", "")).lower()
    if source_type.startswith(PRODUCT_PREFIX) or data_family in PRODUCT_FAMILIES or source_type == "product_documentation":
        return "product_docs"
    if source_type.startswith(RELEASE_PREFIX) or data_family.startswith(RELEASE_PREFIX):
        return "release_notes"
    return "other"


def row_score(row: Dict[str, Any]) -> Tuple[int, int, int, int]:
    answer = first_content(row.get("messages"), "assistant")
    metadata_score = sum(1 for key in ("source_type", "data_family", "switch", "version", "sub_version", "document_title", "section", "command", "syntax") if normalize_text(row.get(key, "")))
    has_bug = int(bool(re.search(r"\b\d{5,7}\b", answer) or normalize_text(row.get("bug_id", ""))))
    has_command = int(bool(normalize_text(row.get("command", "")) or normalize_text(row.get("syntax", ""))))
    return (metadata_score, has_bug + has_command, min(word_count(answer), 350), -abs(word_count(answer) - 80))


def choose_better(a: Dict[str, Any], b: Dict[str, Any]) -> Dict[str, Any]:
    return max((a, b), key=row_score)


def validate_row(row: Any, args: argparse.Namespace) -> Tuple[bool, List[str], Dict[str, str]]:
    reasons: List[str] = []
    example: Dict[str, str] = {}

    if not isinstance(row, dict):
        return False, ["bad_json_object"], example

    messages = row.get("messages")
    if "messages" not in row:
        reasons.append("missing_messages")
    elif not isinstance(messages, list):
        reasons.append("bad_messages")
    elif not messages:
        reasons.append("empty_messages")

    if not isinstance(messages, list):
        return False, reasons, example

    malformed_roles = []
    for message in messages:
        if not isinstance(message, dict):
            malformed_roles.append("not_dict")
            continue
        role = normalize_text(message.get("role", "")).lower()
        if role not in VALID_ROLES:
            malformed_roles.append(role or "missing")
    if malformed_roles:
        reasons.append("malformed_roles")

    user = first_content(messages, "user")
    assistant = first_content(messages, "assistant")
    if not any(isinstance(message, dict) and normalize_text(message.get("role", "")).lower() == "user" for message in messages):
        reasons.append("missing_user_message")
    if not any(isinstance(message, dict) and normalize_text(message.get("role", "")).lower() == "assistant" for message in messages):
        reasons.append("missing_assistant_message")
    if not user:
        reasons.append("empty_user")
    if not assistant:
        reasons.append("empty_assistant")
    if user and word_count(user) < args.min_question_words:
        reasons.append("too_short_question")
    if assistant and word_count(assistant) < args.min_answer_words:
        reasons.append("too_short_answer")
    if placeholder_answer(assistant):
        reasons.append("placeholder_answer")
    if "```" in assistant and args.reject_code_fences:
        reasons.append("answer_has_code_fence")
    if has_null_or_nan(row):
        reasons.append("bad_null_nan")

    for field in REQUIRED_FIELDS:
        if not normalize_text(row.get(field, "")):
            reasons.append(f"missing_{field}")

    if reasons:
        example = {
            "question": user[:240],
            "answer": assistant[:240],
            "reasons": ", ".join(reasons),
        }
    return not reasons, reasons, example


def dedupe_valid_rows(rows: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], int, int, int]:
    exact_seen: Dict[Tuple[str, str], Dict[str, Any]] = {}
    exact_duplicate_qa = 0
    for row in rows:
        key = (canonical(first_content(row.get("messages"), "user")), canonical(first_content(row.get("messages"), "assistant")))
        if key in exact_seen:
            exact_seen[key] = choose_better(exact_seen[key], row)
            exact_duplicate_qa += 1
        else:
            exact_seen[key] = row

    question_seen: Dict[str, Dict[str, Any]] = {}
    duplicate_questions_found = 0
    duplicate_question_rows_dropped = 0
    for row in exact_seen.values():
        qkey = canonical(first_content(row.get("messages"), "user"))
        if qkey in question_seen:
            question_seen[qkey] = choose_better(question_seen[qkey], row)
            duplicate_questions_found += 1
            duplicate_question_rows_dropped += 1
        else:
            question_seen[qkey] = row
    return list(question_seen.values()), exact_duplicate_qa, duplicate_questions_found, duplicate_question_rows_dropped


def load_and_validate(args: argparse.Namespace) -> Dict[str, Any]:
    raw_valid_rows: List[Dict[str, Any]] = []
    reason_counts: Counter = Counter()
    examples: List[Dict[str, Any]] = []
    rows_by_source_type: Counter = Counter()
    rows_by_data_family: Counter = Counter()
    rows_by_switch: Counter = Counter()
    rows_by_version: Counter = Counter()
    rows_by_document_title: Counter = Counter()
    missing_metadata_fields: Counter = Counter()
    total_rows = 0
    parse_errors = 0
    very_long_answers = 0

    with open(args.data_path, "r", encoding="utf-8-sig") as handle:
        for line_no, line in enumerate(handle, start=1):
            line = line.strip()
            if not line:
                continue
            total_rows += 1
            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                parse_errors += 1
                reason_counts["jsonl_parse_error"] += 1
                if len(examples) < args.max_examples:
                    examples.append({"line": line_no, "reasons": "jsonl_parse_error", "error": str(exc)})
                continue

            valid, reasons, example = validate_row(row, args)
            if isinstance(row, dict):
                for field in REQUIRED_FIELDS:
                    if not normalize_text(row.get(field, "")):
                        missing_metadata_fields[field] += 1
                assistant = first_content(row.get("messages"), "assistant")
                if word_count(assistant) > args.max_answer_words:
                    very_long_answers += 1
                    if args.drop_long_answers:
                        valid = False
                        reasons = list(reasons) + ["very_long_answer"]

            if valid:
                raw_valid_rows.append(row)
            else:
                for reason in reasons:
                    reason_counts[reason] += 1
                if len(examples) < args.max_examples:
                    example["line"] = line_no
                    examples.append(example)

    clean_rows, exact_duplicate_qa, duplicate_questions_found, duplicate_question_rows_dropped = dedupe_valid_rows(raw_valid_rows)

    for row in clean_rows:
        rows_by_source_type[normalize_text(row.get("source_type", "")) or "missing"] += 1
        rows_by_data_family[normalize_text(row.get("data_family", "")) or "missing"] += 1
        rows_by_switch[normalize_text(row.get("switch", "")) or "missing"] += 1
        rows_by_version[normalize_text(row.get("version", "")) or "missing"] += 1
        rows_by_document_title[normalize_text(row.get("document_title", "")) or "missing"] += 1

    total_clean = len(clean_rows)
    product_rows = sum(1 for row in clean_rows if domain(row) == "product_docs")
    release_rows = sum(1 for row in clean_rows if domain(row) == "release_notes")
    event_rows = sum(1 for row in clean_rows if normalize_text(row.get("data_family", "")).lower() == "event_log_reference")

    duplicate_questions_final = len(clean_rows) - len({canonical(first_content(row.get("messages"), "user")) for row in clean_rows})
    exact_duplicate_qa_final = len(clean_rows) - len({(canonical(first_content(row.get("messages"), "user")), canonical(first_content(row.get("messages"), "assistant"))) for row in clean_rows})

    report: Dict[str, Any] = {
        "total_rows": total_rows,
        "valid_rows_before_dedup": len(raw_valid_rows),
        "valid_rows_final": total_clean,
        "bad_rows": total_rows - len(raw_valid_rows),
        "jsonl_parse_errors": parse_errors,
        "drop_reasons": dict(sorted(reason_counts.items())),
        "exact_duplicate_qa": exact_duplicate_qa,
        "exact_duplicate_qa_final": exact_duplicate_qa_final,
        "duplicate_questions": duplicate_questions_found,
        "duplicate_question_rows_dropped": duplicate_question_rows_dropped,
        "duplicate_questions_final": duplicate_questions_final,
        "rows_by_source_type": dict(rows_by_source_type),
        "rows_by_data_family": dict(rows_by_data_family),
        "rows_by_switch": dict(rows_by_switch),
        "rows_by_version": dict(rows_by_version),
        "rows_by_document_title": dict(rows_by_document_title),
        "missing_metadata_fields": dict(missing_metadata_fields),
        "missing_source_type": missing_metadata_fields.get("source_type", 0),
        "missing_data_family": missing_metadata_fields.get("data_family", 0),
        "missing_switch": missing_metadata_fields.get("switch", 0),
        "missing_version": missing_metadata_fields.get("version", 0),
        "missing_sub_version": missing_metadata_fields.get("sub_version", 0),
        "missing_messages": reason_counts.get("missing_messages", 0),
        "empty_messages": reason_counts.get("empty_messages", 0),
        "empty_user": reason_counts.get("empty_user", 0),
        "empty_assistant": reason_counts.get("empty_assistant", 0),
        "very_long_answers": very_long_answers,
        "event_log_rows": event_rows,
        "event_log_ratio": event_rows / total_clean if total_clean else 0.0,
        "product_doc_rows": product_rows,
        "product_docs_ratio": product_rows / total_clean if total_clean else 0.0,
        "release_note_rows": release_rows,
        "release_notes_ratio": release_rows / total_clean if total_clean else 0.0,
        "examples": examples,
    }

    Path(args.report_path).parent.mkdir(parents=True, exist_ok=True)
    with open(args.report_path, "w", encoding="utf-8") as handle:
        json.dump(report, handle, indent=2, ensure_ascii=False)

    if args.write_clean_path:
        Path(args.write_clean_path).parent.mkdir(parents=True, exist_ok=True)
        with open(args.write_clean_path, "w", encoding="utf-8") as handle:
            for row in clean_rows:
                handle.write(json.dumps(row, ensure_ascii=False) + "\n")

    return report


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate final Aruba AOS-CX combined chat JSONL before QLoRA training")
    parser.add_argument("--data_path", required=True)
    parser.add_argument("--report_path", default="train_dataset_check_report.json")
    parser.add_argument("--write_clean_path", default=None)
    parser.add_argument("--min_question_words", type=int, default=5)
    parser.add_argument("--min_answer_words", type=int, default=8)
    parser.add_argument("--max_answer_words", type=int, default=1000)
    parser.add_argument("--max_words", type=int, default=None, help="Backward-compatible alias for --max_answer_words")
    parser.add_argument("--max_examples", type=int, default=25)
    parser.add_argument("--drop_long_answers", action="store_true")
    parser.add_argument("--reject_code_fences", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.max_words is not None:
        args.max_answer_words = args.max_words
    report = load_and_validate(args)
    printable = {key: value for key, value in report.items() if key != "examples"}
    print(json.dumps(printable, indent=2, ensure_ascii=False))
    if report["examples"]:
        print("\nExamples:")
        for example in report["examples"][: args.max_examples]:
            print(json.dumps(example, ensure_ascii=False))

    hard_fail = (
        report["jsonl_parse_errors"] > 0
        or report["bad_rows"] > 0
        or report["exact_duplicate_qa_final"] > 0
        or report["duplicate_questions_final"] > 0
    )
    return 1 if hard_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
