#!/usr/bin/env python3
"""Clean and convert release-note JSONL for switch 10000 with local Ollama.

The script preserves the input folder structure under the output root, writes a
combined cleaned JSONL plus review/report/sample files, and streams progress to
stdout so the caller can tail a log file in real time.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, MutableMapping, Optional, Sequence, Tuple

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPT_DIR.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from scripts.repair_dataset_v2 import normalize, read_jsonl, write_jsonl


DEFAULT_INPUT_ROOT = Path(r"E:\52\Train\Train\Data\final_json")
DEFAULT_OUTPUT_ROOT = Path(
    r"E:\52\Train\Train\Data\all_switches\ollama_release_notes_cleaning\release_notes_10000_cleaned"
)
DEFAULT_MODEL = "qwen2.5-coder:7b"
OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
TARGET_SWITCH = "10000"

VERSION_GROUNDING_PREFIX = re.compile(
    rf"(?i)^for\s+{re.escape(TARGET_SWITCH)}\s+aos-cx\s+\d+\.\d+\.\d{{4,5}},\s*"
)
ANY_GROUNDING_PREFIX = re.compile(
    r"(?i)^for\s+(?:\d+\s+)?aos-cx\s+\d+\.\d+\.\d{4,5},\s*"
)
BUG_ID_RE = re.compile(r"\bbug(?:\s+id)?\s*[:#-]?\s*(\d{4,8})\b", re.I)
EVENT_ID_RE = re.compile(r"\bevent(?:\s+id)?\s*[:#-]?\s*(\d{3,8})\b", re.I)


def eprint(message: str) -> None:
    print(message, flush=True)


def extract_qa(row: Mapping[str, Any]) -> Tuple[str, str]:
    question = ""
    answer = ""
    for message in row.get("messages") or []:
        if not isinstance(message, Mapping):
            continue
        role = str(message.get("role") or "").strip().lower()
        content = str(message.get("content") or "").strip()
        if role == "user" and not question:
            question = content
        elif role == "assistant" and not answer:
            answer = content
    return question, answer


def set_qa(row: MutableMapping[str, Any], question: str, answer: str) -> None:
    row["messages"] = [
        {"role": "user", "content": question.strip()},
        {"role": "assistant", "content": answer.strip()},
    ]


def version_display(version: str, sub_version: str) -> str:
    return f"{str(version).replace('_', '.')}.{str(sub_version).strip()}"


def iter_source_files(input_root: Path, switch: str) -> List[Path]:
    switch_root = input_root / switch
    if not switch_root.is_dir():
        raise FileNotFoundError(f"Missing switch folder: {switch_root}")
    return sorted(path for path in switch_root.rglob("train_chat.jsonl") if path.is_file())


def ground_question(question: str, row: Mapping[str, Any], enabled: bool) -> str:
    text = str(question or "").strip()
    if not text or not enabled:
        return text
    text = ANY_GROUNDING_PREFIX.sub("", text).strip()
    prefix = f"For {row.get('switch')} AOS-CX {version_display(row.get('version', ''), row.get('sub_version', ''))}, "
    if VERSION_GROUNDING_PREFIX.match(text):
        return text
    return prefix + text[0].lower() + text[1:] if text else prefix


def classify_row(row: Mapping[str, Any], question: str) -> str:
    source_type = normalize(row.get("source_type"))
    section = normalize(row.get("section"))
    q = normalize(question)
    if "version history" in section or source_type.endswith("version_history"):
        return "version_history"
    if "what category" in q or "which category" in q:
        return "bug_category"
    if "workaround" in q:
        return "bug_workaround"
    if "scenario" in q or "under what scenario" in q:
        return "bug_scenario"
    if "symptom" in q or "what issue was resolved" in q or "what issue" in q:
        return "bug_symptom"
    if row.get("bug_id"):
        return "bug_generic"
    return "generic"


def canonical_data_family(row: Mapping[str, Any]) -> str:
    existing = str(row.get("data_family") or "").strip()
    if existing:
        return existing
    if str(row.get("bug_id") or "").strip():
        return "release_notes_bug"
    return "release_notes_generic"


def safe_strip_code_fences(text: str) -> str:
    value = str(text or "").strip()
    if value.startswith("```"):
        value = re.sub(r"^```(?:json)?\s*", "", value, flags=re.I)
        value = re.sub(r"\s*```$", "", value)
    return value.strip()


def call_ollama(prompt: str, model: str, timeout_s: int = 180) -> Dict[str, Any]:
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "format": "json",
        "options": {
            "temperature": 0,
            "seed": 42,
            "num_ctx": 8192,
        },
    }
    req = urllib.request.Request(
        OLLAMA_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout_s) as resp:
        raw = json.loads(resp.read().decode("utf-8"))
    text = safe_strip_code_fences(str(raw.get("response") or ""))
    return json.loads(text)


def build_prompt(row: Mapping[str, Any], question: str, answer: str) -> str:
    metadata = {
        "source_type": row.get("source_type"),
        "section": row.get("section"),
        "category": row.get("category"),
        "feature": row.get("feature"),
        "bug_id": row.get("bug_id"),
        "event_id": row.get("event_id"),
        "version": row.get("version"),
        "sub_version": row.get("sub_version"),
        "version_number": row.get("version_number"),
        "release_date": row.get("release_date"),
        "remarks": row.get("remarks"),
        "product_number": row.get("product_number"),
        "product_name": row.get("product_name"),
        "minimum_software_version": row.get("minimum_software_version"),
    }
    source_blob = json.dumps(metadata, ensure_ascii=False, separators=(",", ":"))
    return (
        "You are cleaning HPE Aruba AOS-CX release-note training data.\n"
        "Return raw JSON only.\n"
        "Do not use markdown or code fences.\n"
        "Do not invent facts.\n"
        "Do not change bug IDs, event IDs, version numbers, release dates, or categories.\n"
        "Keep the question short and fine-tuning ready.\n"
        "If the wording is weak or unclear, keep the safest cleaned version and set needs_review true.\n\n"
        f"Source metadata: {source_blob}\n"
        f"Original question: {question}\n"
        f"Original answer: {answer}\n\n"
        "Return a JSON object with these keys exactly:\n"
        '{"cleaned_question":"...","cleaned_answer":"...","needs_review":true,"reason":"..."}'
    )


def parse_model_output(parsed: Dict[str, Any], question: str, answer: str) -> Tuple[str, str, bool, str]:
    cleaned_question = str(parsed.get("cleaned_question") or question or "").strip()
    cleaned_answer = str(parsed.get("cleaned_answer") or answer or "").strip()
    needs_review = bool(parsed.get("needs_review", False))
    reason = str(parsed.get("reason") or "").strip()
    return cleaned_question, cleaned_answer, needs_review, reason


def canonical_bug_answer(row: Mapping[str, Any], kind: str, answer: str) -> str:
    category = str(row.get("category") or row.get("feature") or "Bug").strip()
    bug_id = str(row.get("bug_id") or "").strip()
    if not bug_id:
        return answer.strip()
    symptom = str(row.get("symptom") or "").strip()
    scenario = str(row.get("scenario") or "").strip()
    workaround = str(row.get("workaround") or "").strip()
    if kind == "bug_category":
        return f"{category} (Bug ID {bug_id}): This bug belongs to the {category} category."
    if kind == "bug_workaround":
        if workaround:
            return f"{category} (Bug ID {bug_id}): The documented workaround is: {workaround}."
        return f"{category} (Bug ID {bug_id}): No workaround is documented in the release notes."
    if kind == "bug_scenario":
        if scenario:
            if scenario.lower().startswith("this issue may occur when"):
                return f"{category} (Bug ID {bug_id}): {scenario[0].upper() + scenario[1:]}."
            if scenario.lower().startswith("this issue occurs when"):
                return f"{category} (Bug ID {bug_id}): {scenario[0].upper() + scenario[1:]}."
            return f"{category} (Bug ID {bug_id}): This issue may occur when {scenario}."
        return answer.strip()
    if kind == "bug_symptom" and symptom:
        return f"{category} (Bug ID {bug_id}): The symptom is: {symptom}."
    if kind == "version_history":
        version_number = str(row.get("version_number") or "").strip()
        release_date = str(row.get("release_date") or "").strip()
        remarks = str(row.get("remarks") or "").strip()
        base = f"Version History: Version {version_number} was released on {release_date}."
        if remarks:
            return f"{base} Remarks: {remarks}."
        return base
    cleaned = answer.strip().rstrip(".")
    if cleaned:
        return f"{category} (Bug ID {bug_id}): {cleaned}."
    return f"{category} (Bug ID {bug_id}):"


def simple_variant_question(row: Mapping[str, Any], kind: str) -> Optional[str]:
    bug_id = str(row.get("bug_id") or "").strip()
    version_number = str(row.get("version_number") or "").strip()
    if kind == "bug_category" and bug_id:
        return f"Which category does Bug {bug_id} belong to?"
    if kind == "bug_symptom" and bug_id:
        return f"What is the symptom of Bug {bug_id}?"
    if kind == "bug_workaround" and bug_id:
        return f"What is the workaround for Bug {bug_id}?"
    if kind == "bug_scenario" and bug_id:
        return f"Under what scenario does Bug {bug_id} occur?"
    if kind == "version_history" and version_number:
        return f"When was version {version_number} released?"
    return None


def grounded_question_row(row: Mapping[str, Any], question: str) -> str:
    if VERSION_GROUNDING_PREFIX.match(question):
        return question
    return ground_question(question, row, enabled=True)


def build_clean_row(
    row: Mapping[str, Any],
    question: str,
    answer: str,
    needs_review: bool,
    question_variant: bool,
) -> Dict[str, Any]:
    cleaned = dict(row)
    cleaned["data_family"] = canonical_data_family(row)
    cleaned["needs_review"] = bool(needs_review)
    cleaned["question_variant"] = bool(question_variant)
    set_qa(cleaned, question, answer)
    return cleaned


def validate_and_fix(
    row: Mapping[str, Any],
    kind: str,
    question: str,
    answer: str,
    needs_review: bool,
    ground_questions: bool,
) -> Tuple[str, str, bool, bool]:
    fixed = False
    final_question = grounded_question_row(row, question) if ground_questions else str(question).strip()
    final_answer = str(answer).strip()
    bug_id = str(row.get("bug_id") or "").strip()
    event_id = str(row.get("event_id") or "").strip()

    if bug_id:
        canonical = canonical_bug_answer(row, kind, final_answer)
        if "bug id" not in normalize(final_answer) or bug_id not in final_answer:
            final_answer = canonical
            fixed = True
        if kind == "bug_category" and "belongs to" not in normalize(final_answer):
            final_answer = canonical
            fixed = True
        if kind == "bug_symptom" and "symptom" not in normalize(final_answer):
            final_answer = canonical
            fixed = True
        if kind == "bug_workaround" and "workaround" not in normalize(final_answer):
            final_answer = canonical
            fixed = True
        if kind == "bug_scenario" and "scenario" not in normalize(final_answer) and "when" not in normalize(final_answer):
            final_answer = canonical
            fixed = True

    if kind == "version_history":
        canonical = canonical_bug_answer(row, kind, final_answer)
        if str(row.get("version_number") or "").strip() not in final_answer or str(row.get("release_date") or "").strip() not in final_answer:
            final_answer = canonical
            fixed = True

    if event_id and event_id not in final_answer:
        fixed = True
    if fixed:
        needs_review = True

    return final_question, final_answer, needs_review, fixed


def classify_and_clean(
    row: Mapping[str, Any],
    model: str,
    ground_questions: bool,
) -> Tuple[Dict[str, Any], Optional[Dict[str, Any]], str, bool, bool, bool, Optional[Dict[str, Any]]]:
    original_question, original_answer = extract_qa(row)
    kind = classify_row(row, original_question)
    prompt = build_prompt(row, original_question, original_answer)
    model_error = False
    try:
        parsed = call_ollama(prompt, model=model)
        cleaned_question, cleaned_answer, needs_review, reason = parse_model_output(parsed, original_question, original_answer)
    except Exception as exc:
        model_error = True
        cleaned_question, cleaned_answer = original_question, original_answer
        needs_review = True
        reason = f"ollama_error: {exc}"

    cleaned_question, cleaned_answer, needs_review, fixed = validate_and_fix(
        row,
        kind,
        cleaned_question,
        cleaned_answer,
        needs_review,
        ground_questions,
    )

    cleaned_row = build_clean_row(
        row=row,
        question=cleaned_question,
        answer=cleaned_answer,
        needs_review=needs_review,
        question_variant=False,
    )

    review_row = None
    if needs_review or model_error or fixed:
        review_row = {
            "source_type": row.get("source_type"),
            "switch": row.get("switch"),
            "version": row.get("version"),
            "sub_version": row.get("sub_version"),
            "data_family": cleaned_row.get("data_family"),
            "question_kind": kind,
            "question_variant": False,
            "needs_review": bool(needs_review),
            "reason": reason,
            "original_question": original_question,
            "original_answer": original_answer,
            "cleaned_question": cleaned_question,
            "cleaned_answer": cleaned_answer,
        }
        if row.get("bug_id") is not None:
            review_row["bug_id"] = row.get("bug_id")
        if row.get("event_id") is not None:
            review_row["event_id"] = row.get("event_id")

    variant_question = simple_variant_question(row, kind)
    variant_row = None
    if variant_question:
        variant_question = variant_question.strip()
        variant_clean = build_clean_row(
            row=row,
            question=variant_question,
            answer=cleaned_answer,
            needs_review=needs_review,
            question_variant=True,
        )
        variant_row = variant_clean

    return cleaned_row, variant_row, kind, needs_review, model_error, fixed, review_row


def process_row(
    row: Mapping[str, Any],
    *,
    model: str,
    ground_questions: bool,
) -> Tuple[Dict[str, Any], Optional[Dict[str, Any]], str, bool, bool, bool, Optional[Dict[str, Any]]]:
    return classify_and_clean(row=row, model=model, ground_questions=ground_questions)


def sample_bucket(kind: str) -> str:
    if kind == "bug_category":
        return "category"
    if kind == "bug_symptom":
        return "bug symptom"
    if kind == "bug_workaround":
        return "bug workaround"
    if kind == "bug_scenario":
        return "bug scenario"
    if kind == "version_history":
        return "version history"
    return "other"


def write_markdown_samples(path: Path, samples: Mapping[str, List[Dict[str, Any]]]) -> None:
    lines = ["# Release Notes Cleaning Samples", ""]
    for title in ("bug symptom", "bug scenario", "bug workaround", "category", "version history"):
        lines.append(f"## {title.title()}")
        bucket = samples.get(title, [])
        if not bucket:
            lines.append("_No samples collected._")
        else:
            for idx, row in enumerate(bucket[:5], 1):
                lines.append(f"{idx}. `{json.dumps(row, ensure_ascii=False, separators=(',', ':'))}`")
        lines.append("")
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def build_report(
    *,
    input_rows_scanned: int,
    switch_rows_selected: int,
    output_rows_written: int,
    question_variants_created: int,
    rows_marked_needs_review: int,
    duplicates_removed: int,
    json_errors_fixed: int,
    bug_ids_preserved_count: int,
    event_ids_preserved_count: int,
    version_numbers_preserved_count: int,
    categories_preserved_count: int,
    grounded_rows: int,
    source_type_counts_before: Counter,
    source_type_counts_after: Counter,
    data_family_counts_after: Counter,
) -> Dict[str, Any]:
    return {
        "input_rows_scanned": input_rows_scanned,
        "switch_rows_selected": switch_rows_selected,
        "output_rows_written": output_rows_written,
        "question_variants_created": question_variants_created,
        "rows_marked_needs_review": rows_marked_needs_review,
        "duplicates_removed": duplicates_removed,
        "json_errors_fixed": json_errors_fixed,
        "bug_ids_preserved_count": bug_ids_preserved_count,
        "event_ids_preserved_count": event_ids_preserved_count,
        "version_numbers_preserved_count": version_numbers_preserved_count,
        "categories_preserved_count": categories_preserved_count,
        "rows_with_switch_version_in_question": grounded_rows,
        "rows_with_switch_version_in_question_pct": round((grounded_rows / output_rows_written) * 100.0, 2)
        if output_rows_written
        else 0.0,
        "source_type_counts_before": dict(sorted(source_type_counts_before.items())),
        "source_type_counts_after": dict(sorted(source_type_counts_after.items())),
        "data_family_counts_after": dict(sorted(data_family_counts_after.items())),
    }


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-root", type=Path, default=DEFAULT_INPUT_ROOT)
    parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT_ROOT)
    parser.add_argument("--switch", default=TARGET_SWITCH)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--workers", type=int, default=4, help="Parallel Ollama worker count")
    parser.add_argument("--force", action="store_true", help="Replace an existing output directory")
    parser.add_argument(
        "--ground_questions_with_version",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Prepend switch/version grounding to most user questions.",
    )
    args = parser.parse_args(argv)

    input_root = args.input_root.resolve()
    output_root = args.output_root.resolve()
    output_switch_root = output_root / args.switch
    if output_root.exists() and any(output_root.iterdir()) and not args.force:
        raise FileExistsError(f"Output already exists under {output_root}; pass --force to replace it")
    if args.workers < 1:
        parser.error("--workers must be >= 1")

    eprint(f"[START] model: {args.model}")
    eprint(f"[INPUT] reading input path: {input_root}")
    eprint(f"[OUTPUT] root: {output_root}")
    eprint(f"[WORKERS] parallel ollama workers: {args.workers}")

    source_files = iter_source_files(input_root, args.switch)
    eprint(f"[FILTER] switch {args.switch} rows selected from {len(source_files)} source files")

    input_rows_scanned = 0
    switch_rows_selected = 0
    duplicates_removed = 0
    json_errors_fixed = 0
    question_variants_created = 0
    rows_marked_needs_review = 0
    bug_ids_preserved_count = 0
    event_ids_preserved_count = 0
    version_numbers_preserved_count = 0
    categories_preserved_count = 0
    grounded_rows = 0

    source_type_counts_before: Counter = Counter()
    source_type_counts_after: Counter = Counter()
    data_family_counts_after: Counter = Counter()

    per_file_rows: Dict[Path, List[Dict[str, Any]]] = defaultdict(list)
    combined_rows: List[Dict[str, Any]] = []
    review_rows: List[Dict[str, Any]] = []
    samples: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    seen_keys: set[str] = set()

    staged_rows: List[Tuple[Tuple[int, int], Path, Dict[str, Any]]] = []
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {}
        for file_index, input_file in enumerate(source_files, 1):
            rel_path = input_file.relative_to(input_root)
            eprint(f"[FILE] ({file_index}/{len(source_files)}) {rel_path}")
            for line_index, row in enumerate(read_jsonl(input_file), 1):
                input_rows_scanned += 1
                source_type_counts_before[str(row.get("source_type") or "")] += 1
                if str(row.get("switch") or "") != args.switch:
                    continue
                switch_rows_selected += 1
                eprint(f"[CLEAN] row {switch_rows_selected} {rel_path}:{line_index}")
                future = executor.submit(
                    process_row,
                    row,
                    model=args.model,
                    ground_questions=args.ground_questions_with_version,
                )
                futures[future] = (file_index, line_index, rel_path, row)

        for future in as_completed(futures):
            file_index, line_index, rel_path, row = futures[future]
            cleaned_row, variant_row, kind, needs_review, model_error, fixed, review_row = future.result()
            if model_error:
                json_errors_fixed += 1
            if needs_review:
                rows_marked_needs_review += 1
            staged_rows.append(((file_index, line_index), output_switch_root / rel_path, cleaned_row))

            if review_row is not None:
                review_rows.append(review_row)

            eprint(f"[OLLAMA] worker finished {rel_path}:{line_index} needs_review {str(bool(cleaned_row.get('needs_review'))).lower()}")

            if variant_row is not None:
                staged_rows.append(((file_index, line_index + 1_000_000), output_switch_root / rel_path, variant_row))
                question_variants_created += 1
                eprint("[WRITE] variant row staged")

    staged_rows.sort(key=lambda item: item[0])
    for _, file_path, cleaned_row in staged_rows:
        question, answer = extract_qa(cleaned_row)
        dedup_key = normalize(question) + "||" + normalize(answer)
        if dedup_key in seen_keys:
            duplicates_removed += 1
            continue
        seen_keys.add(dedup_key)
        combined_rows.append(cleaned_row)
        per_file_rows[file_path].append(cleaned_row)
        source_type_counts_after[str(cleaned_row.get("source_type") or "")] += 1
        data_family_counts_after[str(cleaned_row.get("data_family") or "")] += 1

        if cleaned_row.get("bug_id") is not None:
            bug_ids_preserved_count += 1
        if cleaned_row.get("event_id") is not None:
            event_ids_preserved_count += 1
        if cleaned_row.get("version") is not None:
            version_numbers_preserved_count += 1
        if cleaned_row.get("category") is not None:
            categories_preserved_count += 1
        if VERSION_GROUNDING_PREFIX.match(question):
            grounded_rows += 1

        bucket = sample_bucket(classify_row(cleaned_row, question))
        if len(samples[bucket]) < 5:
            samples[bucket].append(
                {
                    "source_type": cleaned_row.get("source_type"),
                    "question": question,
                    "answer": answer,
                    "needs_review": cleaned_row.get("needs_review"),
                }
            )

    output_switch_root.mkdir(parents=True, exist_ok=True)
    review_path = output_root / "release_notes_10000_cleaning_review.jsonl"
    report_path = output_root / "release_notes_10000_cleaning_report.json"
    samples_path = output_root / "release_notes_10000_cleaned_samples.md"

    # Write mirrored per-file outputs first so the folder tree stays intact.
    for file_path, rows in sorted(per_file_rows.items(), key=lambda item: str(item[0])):
        file_path.parent.mkdir(parents=True, exist_ok=True)
        write_jsonl(file_path, rows)

    output_rows_written = len(combined_rows)
    write_jsonl(review_path, review_rows)

    report = build_report(
        input_rows_scanned=input_rows_scanned,
        switch_rows_selected=switch_rows_selected,
        output_rows_written=output_rows_written,
        question_variants_created=question_variants_created,
        rows_marked_needs_review=rows_marked_needs_review,
        duplicates_removed=duplicates_removed,
        json_errors_fixed=json_errors_fixed,
        bug_ids_preserved_count=bug_ids_preserved_count,
        event_ids_preserved_count=event_ids_preserved_count,
        version_numbers_preserved_count=version_numbers_preserved_count,
        categories_preserved_count=categories_preserved_count,
        grounded_rows=grounded_rows,
        source_type_counts_before=source_type_counts_before,
        source_type_counts_after=source_type_counts_after,
        data_family_counts_after=data_family_counts_after,
    )
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown_samples(samples_path, samples)

    eprint(f"[QUALITY] valid JSONL rows {output_rows_written}")
    eprint(f"[QUALITY] duplicates removed {duplicates_removed}")
    eprint(f"[QUALITY] final output rows {output_rows_written}")
    eprint("[OUTPUT] saved cleaned JSONL tree under mirrored version folders")
    eprint(f"[OUTPUT] saved review JSONL: {review_path}")
    eprint(f"[OUTPUT] saved report JSON: {report_path}")
    eprint(f"[OUTPUT] saved samples MD: {samples_path}")
    eprint(f"[OUTPUT] mirrored folder tree: {output_switch_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
