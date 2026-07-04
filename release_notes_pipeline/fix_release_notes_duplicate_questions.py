"""Final deterministic duplicate-question cleanup for release-note JSONL rows.

This script intentionally does not touch product-documentation preprocessing.
It reads release-note train_chat.jsonl files, writes one clean combined JSONL,
and reports duplicate-question fixes.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


WHITESPACE_RE = re.compile(r"\s+")
REPEATED_PUNCT_RE = re.compile(r"([?!.,:;])\1+")
BUG_ID_RE = re.compile(r"\bBug\s+(\d{5,7})\b", re.IGNORECASE)
QUESTION_GROUNDING_RE = re.compile(r"^(For\s+.+?\s+AOS-CX\s+\d+(?:\.\d+){1,2},\s+)(.*)$", re.IGNORECASE)
CATEGORY_QUESTION_RE = re.compile(
    r"\bwhich category (?:does|is affected by) bug \d{5,7} (?:belong to|affected by)\??|\bwhich category does bug \d{5,7} belong to\?",
    re.IGNORECASE,
)
KNOWN_CATEGORY_QUESTION_RE = re.compile(r"\bwhich category is affected by bug \d{5,7}\?", re.IGNORECASE)
BUG_DETAIL_QUESTION_RE = re.compile(
    r"\b(?:what symptom occurs|under what scenario|what is the workaround|what issue was resolved|what known issue is documented)\b",
    re.IGNORECASE,
)
PLACEHOLDER_RE = re.compile(r"\bTBD\b|Siddharthan Sundaradoss", re.IGNORECASE)


def normalize_spaces(value: Any) -> str:
    return WHITESPACE_RE.sub(" ", str(value or "").strip())


def normalize_question(question: Any) -> str:
    text = normalize_spaces(question).casefold()
    text = REPEATED_PUNCT_RE.sub(r"\1", text)
    return normalize_spaces(text)


def normalize_answer_for_compare(answer: Any) -> str:
    text = normalize_spaces(answer).casefold()
    text = REPEATED_PUNCT_RE.sub(r"\1", text)
    text = re.sub(r"\s+([,.;:?!])", r"\1", text)
    return text.rstrip(" .")


def exact_qa_key(row: dict[str, Any]) -> tuple[str, str]:
    question, answer = get_messages(row)
    return normalize_question(question), normalize_answer_for_compare(answer)


def get_messages(row: dict[str, Any]) -> tuple[str, str]:
    messages = row.get("messages", [])
    if not isinstance(messages, list) or len(messages) != 2:
        return "", ""
    return normalize_spaces(messages[0].get("content", "")), normalize_spaces(messages[1].get("content", ""))


def set_question(row: dict[str, Any], question: str) -> dict[str, Any]:
    new_row = dict(row)
    messages = row.get("messages", [])
    if isinstance(messages, list) and len(messages) == 2:
        new_messages = [dict(messages[0]), dict(messages[1])]
        new_messages[0]["content"] = normalize_spaces(question)
        new_row["messages"] = new_messages
    return new_row


def set_answer(row: dict[str, Any], answer: str) -> dict[str, Any]:
    new_row = dict(row)
    messages = row.get("messages", [])
    if isinstance(messages, list) and len(messages) == 2:
        new_messages = [dict(messages[0]), dict(messages[1])]
        new_messages[1]["content"] = normalize_spaces(answer)
        new_row["messages"] = new_messages
    return new_row


def contains_placeholder(row: dict[str, Any]) -> bool:
    return bool(PLACEHOLDER_RE.search(json.dumps(row, ensure_ascii=False)))


def category_label(row: dict[str, Any]) -> str:
    category = normalize_spaces(row.get("category"))
    if category:
        return category
    answer = get_messages(row)[1]
    match = re.match(r"(.+?)\s+\(Bug ID\s+\d{5,7}\):", answer)
    if match:
        return normalize_spaces(match.group(1))
    section = normalize_spaces(row.get("section"))
    return section


def human_join(values: list[str]) -> str:
    values = [value for value in values if value]
    if not values:
        return ""
    if len(values) == 1:
        return values[0]
    return f"{', '.join(values[:-1])} and {values[-1]}"


def extract_bug_id_from_question_or_row(row: dict[str, Any]) -> str:
    question = get_messages(row)[0]
    match = BUG_ID_RE.search(question)
    if match:
        return match.group(1)
    return normalize_spaces(row.get("bug_id"))


def is_bug_category_question(question: str) -> bool:
    normalized = normalize_question(question)
    return (
        bool(re.search(r"\bwhich category does bug \d{5,7} belong to\?", normalized))
        or bool(re.search(r"\bwhich category is affected by bug \d{5,7}\?", normalized))
    )


def is_bug_detail_question(row: dict[str, Any]) -> bool:
    question = get_messages(row)[0]
    return bool(row.get("bug_id")) and bool(BUG_DETAIL_QUESTION_RE.search(question))


def with_grounding_prefix(question: str, body: str) -> str:
    match = QUESTION_GROUNDING_RE.match(question)
    if match:
        return f"{match.group(1)}{body}"
    return body[:1].upper() + body[1:] if body else question


def make_bug_context_question(row: dict[str, Any], original_question: str) -> str:
    category = category_label(row)
    context = f"in the {category} category" if category else f"in the {normalize_spaces(row.get('section'))} section"
    match = QUESTION_GROUNDING_RE.match(original_question)
    body = match.group(2) if match else original_question
    body = body[:1].lower() + body[1:] if body else body
    if body.startswith("in the "):
        return original_question
    return with_grounding_prefix(original_question, f"{context}, {body}")


def topic_from_text(text: str, max_words: int = 10, max_chars: int = 90) -> str:
    text = normalize_spaces(text)
    text = re.sub(r"^(Feature Caveat:\s*[^-]+-\s*)", "", text, flags=re.IGNORECASE)
    first_sentence = re.split(r"(?<=[.!?])\s+", text)[0]
    words = first_sentence.split()
    topic = " ".join(words[:max_words]).strip(" .,:;")
    if len(topic) > max_chars:
        topic = topic[:max_chars].rsplit(" ", 1)[0].strip(" .,:;")
    return topic


def make_non_bug_context_question(row: dict[str, Any], original_question: str, index: int) -> str:
    source_type = normalize_spaces(row.get("source_type"))
    feature = normalize_spaces(row.get("feature"))
    description = normalize_spaces(row.get("description"))
    answer = get_messages(row)[1]
    if source_type == "release_notes_caveats" and feature:
        topic = topic_from_text(description or answer)
        if topic:
            return with_grounding_prefix(
                original_question,
                f"what caveat is documented for {feature} regarding {topic}?",
            )
    section = normalize_spaces(row.get("section")) or source_type or "release notes"
    body = f"in the {section} section entry {index}, {strip_grounding(original_question)}"
    return with_grounding_prefix(original_question, body)


def strip_grounding(question: str) -> str:
    match = QUESTION_GROUNDING_RE.match(question)
    body = match.group(2) if match else question
    return body[:1].lower() + body[1:] if body else body


def make_question_unique(question: str, index: int) -> str:
    question = normalize_spaces(question)
    suffix = f" entry {index}"
    if question.endswith("?"):
        return f"{question[:-1]} ({suffix.strip()})?"
    return f"{question} ({suffix.strip()})"


def data_family(row: dict[str, Any]) -> str:
    source_type = normalize_spaces(row.get("source_type"))
    section = normalize_spaces(row.get("section")).casefold()
    if row.get("bug_id"):
        return "release_notes_bug"
    if source_type == "release_notes_caveats" or "caveat" in section:
        return "release_notes_caveat"
    if source_type == "release_notes_known_issues" or "known issues" in section:
        return "release_notes_known_issue"
    if source_type == "release_notes_resolved_issues" or "resolved issues" in section or "fixes" in section:
        return "release_notes_fix"
    if "enhancement" in section:
        return "release_notes_enhancement"
    return "release_notes_generic"


def read_rows(input_root: Path) -> tuple[list[dict[str, Any]], int]:
    rows: list[dict[str, Any]] = []
    parse_errors = 0
    for path in sorted(input_root.rglob("train_chat.jsonl")):
        # Do not recursively consume generated combined outputs.
        if path.name != "train_chat.jsonl":
            continue
        with path.open("r", encoding="utf-8") as handle:
            for line_number, line in enumerate(handle, start=1):
                if not line.strip():
                    continue
                try:
                    row = json.loads(line)
                except json.JSONDecodeError:
                    parse_errors += 1
                    continue
                row["_source_jsonl"] = str(path)
                rows.append(row)
    return rows, parse_errors


def duplicate_question_stats(rows: list[dict[str, Any]]) -> tuple[int, int]:
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        question = get_messages(row)[0]
        groups[normalize_question(question)].append(row)
    duplicate_groups = [items for items in groups.values() if len(items) > 1]
    return len(duplicate_groups), sum(len(items) - 1 for items in duplicate_groups)


def remove_exact_duplicate_pairs(rows: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], int]:
    seen: set[tuple[str, str]] = set()
    kept: list[dict[str, Any]] = []
    dropped = 0
    for row in rows:
        key = exact_qa_key(row)
        if key in seen:
            dropped += 1
            continue
        seen.add(key)
        kept.append(row)
    return kept, dropped


def fix_duplicate_questions(rows: list[dict[str, Any]], report: dict[str, int]) -> list[dict[str, Any]]:
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        groups[normalize_question(get_messages(row)[0])].append(row)

    fixed: list[dict[str, Any]] = []
    for items in groups.values():
        if len(items) == 1:
            fixed.extend(items)
            continue

        question = get_messages(items[0])[0]
        answers = {normalize_answer_for_compare(get_messages(item)[1]) for item in items}

        if is_bug_category_question(question):
            categories = sorted({category_label(item) for item in items if category_label(item)}, key=str.casefold)
            bug_id = extract_bug_id_from_question_or_row(items[0])
            merged = dict(items[0])
            if categories:
                plural = "category" if len(categories) == 1 else "categories"
                verb = "affects" if KNOWN_CATEGORY_QUESTION_RE.search(normalize_question(question)) else "belongs to"
                answer = f"Bug {bug_id} {verb} the {human_join(categories)} {plural}."
                merged = set_answer(merged, answer)
                merged["category"] = "; ".join(categories)
            report["duplicate_question_rows_fixed_by_merge"] += len(items) - 1
            fixed.append(merged)
            continue

        if len(answers) == 1:
            fixed.append(items[0])
            report["duplicate_question_rows_dropped"] += len(items) - 1
            continue

        if all(is_bug_detail_question(item) for item in items):
            for item in items:
                new_question = make_bug_context_question(item, get_messages(item)[0])
                if normalize_question(new_question) != normalize_question(get_messages(item)[0]):
                    report["duplicate_question_rows_fixed_by_section_specific_question"] += 1
                fixed.append(set_question(item, new_question))
            continue

        for index, item in enumerate(items, start=1):
            new_question = make_non_bug_context_question(item, get_messages(item)[0], index)
            if normalize_question(new_question) != normalize_question(get_messages(item)[0]):
                report["duplicate_question_rows_fixed_by_section_specific_question"] += 1
            fixed.append(set_question(item, new_question))

    return fixed


def enforce_unique_questions(rows: list[dict[str, Any]], report: dict[str, int]) -> list[dict[str, Any]]:
    # Repeat until no normalized question has more than one row.
    for _ in range(3):
        groups: dict[str, list[int]] = defaultdict(list)
        for index, row in enumerate(rows):
            groups[normalize_question(get_messages(row)[0])].append(index)
        duplicate_groups = [indexes for indexes in groups.values() if len(indexes) > 1]
        if not duplicate_groups:
            return rows
        new_rows = list(rows)
        for indexes in duplicate_groups:
            for offset, row_index in enumerate(indexes, start=1):
                row = new_rows[row_index]
                question = get_messages(row)[0]
                unique_question = make_question_unique(question, offset)
                if normalize_question(unique_question) != normalize_question(question):
                    report["duplicate_question_rows_fixed_by_section_specific_question"] += 1
                new_rows[row_index] = set_question(row, unique_question)
        rows = new_rows
    return rows


def final_exact_duplicate_pair_count(rows: list[dict[str, Any]]) -> int:
    counter = Counter(exact_qa_key(row) for row in rows)
    return sum(1 for count in counter.values() if count > 1)


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            clean_row = {key: value for key, value in row.items() if key != "_source_jsonl"}
            handle.write(json.dumps(clean_row, ensure_ascii=False) + "\n")


def run(args: argparse.Namespace) -> dict[str, Any]:
    input_root = Path(args.input_root)
    output_jsonl = Path(args.output_jsonl)
    report_path = Path(args.report)

    rows, parse_errors = read_rows(input_root)
    total_rows_before = len(rows)
    duplicate_questions_found_before, duplicate_question_extra_rows = duplicate_question_stats(rows)

    report: dict[str, int] = {
        "total_rows_before": total_rows_before,
        "total_rows_after": 0,
        "jsonl_parse_errors": parse_errors,
        "exact_duplicate_qa_pairs": 0,
        "duplicate_questions_found_before": duplicate_questions_found_before,
        "duplicate_questions_found": duplicate_questions_found_before,
        "duplicate_question_extra_rows": duplicate_question_extra_rows,
        "duplicate_question_rows_fixed_by_merge": 0,
        "duplicate_question_rows_fixed_by_section_specific_question": 0,
        "duplicate_question_rows_dropped": 0,
        "duplicate_questions_final": 0,
        "rows_with_bug_id": 0,
        "rows_with_data_family": 0,
        "placeholder_rows_dropped": 0,
    }

    filtered: list[dict[str, Any]] = []
    for row in rows:
        if contains_placeholder(row):
            report["placeholder_rows_dropped"] += 1
            continue
        row["data_family"] = data_family(row)
        filtered.append(row)

    filtered, exact_dropped_initial = remove_exact_duplicate_pairs(filtered)
    report["duplicate_question_rows_dropped"] += exact_dropped_initial

    fixed = fix_duplicate_questions(filtered, report)
    fixed = enforce_unique_questions(fixed, report)
    fixed, exact_dropped_final = remove_exact_duplicate_pairs(fixed)
    report["duplicate_question_rows_dropped"] += exact_dropped_final
    fixed = enforce_unique_questions(fixed, report)

    duplicate_questions_final, _ = duplicate_question_stats(fixed)
    report["duplicate_questions_final"] = duplicate_questions_final
    report["exact_duplicate_qa_pairs"] = final_exact_duplicate_pair_count(fixed)
    report["total_rows_after"] = len(fixed)
    report["rows_with_bug_id"] = sum(1 for row in fixed if row.get("bug_id"))
    report["rows_with_data_family"] = sum(1 for row in fixed if row.get("data_family"))

    write_jsonl(output_jsonl, fixed)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    return report


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fix duplicate user-question conflicts in release-note JSONL rows.")
    parser.add_argument("--input-root", required=True)
    parser.add_argument("--output-jsonl", required=True)
    parser.add_argument("--report", required=True)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    report = run(args)
    print(f"Rows before: {report['total_rows_before']}")
    print(f"Rows after: {report['total_rows_after']}")
    print(f"Duplicate questions before: {report['duplicate_questions_found_before']}")
    print(f"Duplicate questions final: {report['duplicate_questions_final']}")
    print(f"Exact duplicate QA pairs final: {report['exact_duplicate_qa_pairs']}")
    if (
        report["jsonl_parse_errors"] != 0
        or report["exact_duplicate_qa_pairs"] != 0
        or report["duplicate_questions_final"] != 0
        or report["rows_with_data_family"] != report["total_rows_after"]
    ):
        raise SystemExit(1)


if __name__ == "__main__":
    main(sys.argv[1:])
