#!/usr/bin/env python3
"""Deterministically repair the cleaned release-note tree for switch 10000.

The script reads the current cleaned tree, fixes question/answer formatting,
keeps only exact question+answer deduplication, and writes a new tree-shaped
output under test4_html without calling Ollama.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, MutableMapping, Optional, Sequence, Tuple

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPT_DIR.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from scripts.repair_dataset_v2 import normalize, read_jsonl, write_jsonl


DEFAULT_INPUT_ROOT = Path(
    r"E:\52\Train\Train\Data\all_switches\ollama_release_notes_cleaning\release_notes_10000_cleaned\10000"
)
DEFAULT_OUTPUT_ROOT = Path(r"E:\52\test4_html\project\final_json\release_notes_10000_fixed_tree")
TARGET_SWITCH = "10000"

GROUNDING_PREFIX_RE = re.compile(r"(?i)^for\s+\d+\s+aos-cx\s+\d+\.\d+\.\d{4,5},\s*")
BUG_ID_RE = re.compile(r"\bbug(?:\s+id)?\s*[:#-]?\s*(\d{4,8})\b", re.I)
WHITESPACE_RE = re.compile(r"\s+")
REPEATED_WORD_RE = re.compile(r"\b(\w+)(?:\s+\1\b)+", re.I)
SUSPICIOUS_MARKERS = (
    "no functional impact",
    "intermittent",
    "sporadic",
    "rare timing",
    "potentially",
    "could occur",
    "may occur",
)
SCENARIO_PREFIXES = (
    "this issue may occur when",
    "this issue can occur when",
    "this issue occurs when",
    "this issue can occur if",
    "scenario:",
)


def eprint(message: str) -> None:
    print(message, flush=True)


def clean_spaces(text: Any) -> str:
    return WHITESPACE_RE.sub(" ", str(text or "").strip())


def version_display(row: Mapping[str, Any]) -> str:
    version = str(row.get("version") or "").strip().replace("_", ".")
    sub_version = str(row.get("sub_version") or "").strip()
    if not sub_version or sub_version in {"0", "0000"}:
        return version
    return f"{version}.{sub_version}"


def grounding_prefix(row: Mapping[str, Any]) -> str:
    return f"For {row.get('switch')} AOS-CX {version_display(row)}, "


def ground_question(question: str, row: Mapping[str, Any]) -> str:
    text = clean_spaces(question)
    if not text:
        return text
    while GROUNDING_PREFIX_RE.match(text):
        text = GROUNDING_PREFIX_RE.sub("", text).strip()
    prefix = grounding_prefix(row)
    if not text:
        return prefix.rstrip(", ")
    body = text[0].lower() + text[1:] if text[:1].isupper() else text
    return prefix + body


def extract_qa(row: Mapping[str, Any]) -> Tuple[str, str]:
    question = ""
    answer = ""
    for message in row.get("messages") or []:
        if not isinstance(message, Mapping):
            continue
        role = str(message.get("role") or "").strip().lower()
        content = clean_spaces(message.get("content"))
        if role == "user" and not question:
            question = content
        elif role == "assistant" and not answer:
            answer = content
    return question, answer


def set_qa(row: MutableMapping[str, Any], question: str, answer: str) -> None:
    row["messages"] = [
        {"role": "user", "content": clean_spaces(question)},
        {"role": "assistant", "content": clean_spaces(answer)},
    ]


def strip_prefix_once(text: str, prefixes: Sequence[str]) -> str:
    value = clean_spaces(text)
    lowered = value.casefold()
    for prefix in prefixes:
        if lowered.startswith(prefix.casefold()):
            return value[len(prefix) :].lstrip(" :-")
    return value


def extract_bug_id(row: Mapping[str, Any], question: str, answer: str) -> str:
    explicit = str(row.get("bug_id") or "").strip()
    if explicit:
        return explicit
    match = BUG_ID_RE.search(f"{question} {answer}")
    return match.group(1) if match else ""


def sentence(text: Any) -> str:
    value = clean_spaces(text).strip().strip('"').strip("'")
    if not value:
        return value
    value = REPEATED_WORD_RE.sub(r"\1", value)
    value = re.sub(r"\s+([,.!?;:])", r"\1", value)
    if value and value[-1] not in ".!?":
        value += "."
    return value


def normalize_scenario(text: Any) -> str:
    value = clean_spaces(text)
    if not value:
        return value
    lowered = value.casefold()
    changed = True
    while changed:
        changed = False
        for prefix in SCENARIO_PREFIXES:
            if lowered.startswith(prefix):
                value = value[len(prefix) :].lstrip(" :-")
                lowered = value.casefold()
                changed = True
    for marker in SCENARIO_PREFIXES[:-1]:
        idx = lowered.find(marker)
        if idx > 0:
            value = value[idx + len(marker) :].lstrip(" :-")
            lowered = value.casefold()
            break
    value = REPEATED_WORD_RE.sub(r"\1", value)
    value = re.sub(r"\bthis issue may occur when this issue can occur if\b", "This issue can occur if", value, flags=re.I)
    value = re.sub(r"\bthis issue may occur when this issue occurs when\b", "This issue occurs when", value, flags=re.I)
    value = re.sub(r"\bthis issue may occur when this issue may occur when\b", "This issue may occur when", value, flags=re.I)
    value = sentence(value)
    if value.startswith(("If ", "When ", "While ")) and ". " in value:
        first, rest = value.split(". ", 1)
        value = f"{first}, {rest}"
    return value


def classify_row(row: Mapping[str, Any], question: str, answer: str) -> str:
    source_type = normalize(row.get("source_type"))
    section = normalize(row.get("section"))
    q = normalize(question)
    a = normalize(answer)
    if "version history" in section or source_type.endswith("version_history"):
        return "version_history"
    if row.get("bug_id"):
        if "workaround" in q or "no workaround" in a:
            return "workaround"
        if "category" in q or "belong" in q or "affected by" in q:
            return "category"
        if "what issue was resolved" in q or "resolved issue" in q or "issue was resolved" in q:
            return "resolved_issue"
        if "what known issue" in q or "known issue" in q:
            return "known_issue"
        if "symptom" in q or "what issue occurs" in q:
            return "symptom"
        if "scenario" in q:
            return "scenario"
        if source_type == "release_notes_known_issues":
            return "known_issue"
        if source_type == "release_notes_resolved_issues":
            return "resolved_issue"
        return "bug_generic"
    if source_type == "release_notes_caveats":
        return "caveat"
    if source_type == "release_notes_compatibility":
        return "compatibility"
    if source_type == "release_notes_supported_products":
        return "supported_product"
    if source_type == "release_notes_upgrade_procedure":
        return "upgrade_procedure"
    if source_type == "release_notes_downgrade_restore":
        return "downgrade_restore"
    return "generic"


def build_answer(row: Mapping[str, Any], kind: str, original_answer: str) -> Tuple[str, bool, str]:
    bug_id = extract_bug_id(row, *extract_qa(row))
    category = str(row.get("category") or row.get("feature") or "").strip()
    symptom = clean_spaces(row.get("symptom") or "")
    scenario = normalize_scenario(row.get("scenario") or "")
    workaround = clean_spaces(row.get("workaround") or "")
    version_number = clean_spaces(row.get("version_number") or "")
    release_date = clean_spaces(row.get("release_date") or "")
    remarks = clean_spaces(row.get("remarks") or "")
    needs_review = False
    fix_reason = ""

    if kind == "category" and bug_id and category:
        answer = f"Bug {bug_id} belongs to the {category} category."
        return answer, False, "category"

    if kind == "symptom" and bug_id and symptom:
        symptom = strip_prefix_once(symptom, ("The symptom is:", "Symptom:",))
        if symptom and symptom[0].isupper() and ". " in symptom and symptom.startswith(("If ", "When ", "While ")):
            first, rest = symptom.split(". ", 1)
            symptom = f"{first}, {rest}"
        answer = f"Bug {bug_id} symptom: {sentence(symptom).rstrip('.')}"
        return answer, False, "symptom"

    if kind == "scenario" and bug_id and scenario:
        answer = f"Bug {bug_id} scenario: {scenario.rstrip('.')}"
        if any(marker in scenario.casefold() for marker in SUSPICIOUS_MARKERS):
            needs_review = True
            fix_reason = "scenario appears weak"
        return answer, needs_review, fix_reason or "scenario"

    if kind == "workaround" and bug_id:
        if workaround:
            answer = f"Bug {bug_id} workaround: {sentence(workaround).rstrip('.')}"
            return answer, False, "workaround"
        return f"Bug {bug_id}: No workaround is documented in the release notes.", False, "workaround_missing"

    if kind == "known_issue" and bug_id:
        parts = [f"Bug {bug_id} known issue: {sentence(symptom).rstrip('.') if symptom else clean_spaces(original_answer).rstrip('.')}."]
        if scenario:
            parts.append(f"Scenario: {scenario.rstrip('.')}.")
        if workaround:
            parts.append(f"Workaround: {sentence(workaround).rstrip('.')}.")
        answer = " ".join(parts)
        if any(marker in answer.casefold() for marker in SUSPICIOUS_MARKERS):
            needs_review = True
            fix_reason = "known issue appears weak"
        return answer, needs_review, fix_reason or "known_issue"

    if kind == "resolved_issue" and bug_id:
        parts = [f"Bug {bug_id} resolved issue: {sentence(symptom).rstrip('.') if symptom else clean_spaces(original_answer).rstrip('.')}."]
        if scenario:
            parts.append(f"Scenario: {scenario.rstrip('.')}.")
        answer = " ".join(parts)
        if any(marker in answer.casefold() for marker in SUSPICIOUS_MARKERS):
            needs_review = True
            fix_reason = "resolved issue appears weak"
        return answer, needs_review, fix_reason or "resolved_issue"

    if kind == "version_history" and version_number and release_date:
        answer = f"Version {version_number} was released on {release_date}."
        return answer, False, "version_history"

    if kind == "caveat":
        feature = clean_spaces(row.get("feature") or "")
        description = clean_spaces(row.get("description") or original_answer)
        if feature and description:
            return f"{feature} - {description}", False, "caveat"
        return sentence(description or original_answer), False, "caveat"

    if kind == "compatibility":
        browser = clean_spaces(row.get("browser") or "")
        min_version = clean_spaces(row.get("minimum_supported_version") or "")
        if browser and min_version:
            return f"{browser} requires minimum supported version {min_version}.", False, "compatibility"
        return sentence(original_answer), False, "compatibility"

    if kind == "supported_product":
        product_number = clean_spaces(row.get("product_number") or "")
        product_name = clean_spaces(row.get("product_name") or "")
        min_sw = clean_spaces(row.get("minimum_software_version") or "")
        if product_number and product_name and min_sw:
            return f"{product_number} - {product_name} requires minimum software version {min_sw}.", False, "supported_product"
        return sentence(original_answer), False, "supported_product"

    if kind == "upgrade_procedure":
        procedure = row.get("procedure") or []
        if isinstance(procedure, list) and procedure:
            text = " ".join(clean_spaces(step) for step in procedure[:4])
            return sentence(text), False, "upgrade_procedure"
        return sentence(original_answer), False, "upgrade_procedure"

    if kind == "downgrade_restore":
        procedure = row.get("procedure") or []
        if isinstance(procedure, list) and procedure:
            text = " ".join(clean_spaces(step) for step in procedure[:3])
            return sentence(text), False, "downgrade_restore"
        return sentence(original_answer), False, "downgrade_restore"

    if bug_id:
        return f"Bug {bug_id}: {sentence(original_answer).rstrip('.')}", True, "bug_generic"

    return sentence(original_answer), True, "generic"


def fix_row(row: Mapping[str, Any]) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    original_question, original_answer = extract_qa(row)
    kind = classify_row(row, original_question, original_answer)
    fixed_question = ground_question(original_question, row)
    fixed_answer, needs_review, fix_reason = build_answer(row, kind, original_answer)
    if kind == "version_history":
        data_family = "release_notes_generic"
    else:
        data_family = str(row.get("data_family") or "").strip() or "release_notes_generic"
    if kind in {"category", "symptom", "scenario", "workaround", "known_issue", "resolved_issue", "version_history"}:
        needs_review = False if not needs_review else True
    if kind == "scenario" and any(marker in fixed_answer.casefold() for marker in SUSPICIOUS_MARKERS):
        needs_review = True
    if kind in {"known_issue", "resolved_issue"} and any(marker in fixed_answer.casefold() for marker in SUSPICIOUS_MARKERS):
        needs_review = True

    cleaned = dict(row)
    cleaned["data_family"] = data_family
    cleaned["needs_review"] = bool(needs_review)
    cleaned["question_variant"] = False
    set_qa(cleaned, fixed_question, fixed_answer)

    review = {
        "source_type": row.get("source_type"),
        "switch": row.get("switch"),
        "version": row.get("version"),
        "sub_version": row.get("sub_version"),
        "data_family": data_family,
        "question_kind": kind,
        "question_variant": False,
        "needs_review": bool(needs_review),
        "reason": fix_reason,
        "original_question": original_question,
        "original_answer": original_answer,
        "cleaned_question": fixed_question,
        "cleaned_answer": fixed_answer,
    }
    if row.get("bug_id") is not None:
        review["bug_id"] = row.get("bug_id")
    if row.get("version_number") is not None:
        review["version_number"] = row.get("version_number")
    if row.get("release_date") is not None:
        review["release_date"] = row.get("release_date")
    return cleaned, review


@dataclass
class FileResult:
    input_path: Path
    rel_path: Path
    rows: List[Tuple[Tuple[int, int], Dict[str, Any]]]
    reviews: List[Dict[str, Any]]
    stats: Counter
    bug_categories: Dict[str, set]
    samples_clean: List[Dict[str, Any]]
    samples_review: List[Dict[str, Any]]


def process_file(input_root: Path, input_path: Path) -> FileResult:
    rel_path = input_path.relative_to(input_root)
    rows: List[Tuple[Tuple[int, int], Dict[str, Any]]] = []
    reviews: List[Dict[str, Any]] = []
    stats: Counter = Counter()
    bug_categories: Dict[str, set] = defaultdict(set)
    samples_clean: List[Dict[str, Any]] = []
    samples_review: List[Dict[str, Any]] = []

    for line_index, row in enumerate(read_jsonl(input_path), 1):
        cleaned, review = fix_row(row)
        question, answer = extract_qa(cleaned)
        key = normalize(question) + "||" + normalize(answer)
        rows.append(((int(rel_path.parts[0]) if rel_path.parts and rel_path.parts[0].isdigit() else 0, line_index), cleaned))
        stats[f"kind:{review['question_kind']}"] += 1
        if cleaned.get("needs_review"):
            stats["needs_review_true"] += 1
            if len(samples_review) < 10:
                samples_review.append(review)
        else:
            stats["needs_review_false"] += 1
            if len(samples_clean) < 10:
                samples_clean.append(
                    {
                        "question": question,
                        "answer": answer,
                        "source_type": cleaned.get("source_type"),
                        "data_family": cleaned.get("data_family"),
                    }
                )
        if cleaned.get("bug_id") is not None:
            bug_categories[str(cleaned.get("bug_id"))].add(str(cleaned.get("category") or ""))
        if review["question_kind"] == "version_history":
            stats["version_history_rows_fixed"] += 1
        if review["question_kind"] == "category":
            stats["category_rows_fixed"] += 1
        if review["question_kind"] == "symptom":
            stats["symptom_rows_fixed"] += 1
        if review["question_kind"] == "scenario":
            stats["scenario_rows_fixed"] += 1
        if review["question_kind"] == "workaround":
            stats["workaround_rows_fixed"] += 1
        if review["question_kind"] in {"category", "symptom", "scenario", "workaround"}:
            stats["generic_variants_fixed"] += int(not original_has_grounding(row))
        if review["question_kind"] == "version_history" and str(review.get("data_family")) == "release_notes_generic":
            stats["data_family_changed_to_version_history"] += 1
        reviews.append(review)
    stats["input_rows_read"] = len(rows)
    return FileResult(input_path, rel_path, rows, reviews, stats, bug_categories, samples_clean, samples_review)


def original_has_grounding(row: Mapping[str, Any]) -> bool:
    q, _ = extract_qa(row)
    return bool(GROUNDING_PREFIX_RE.match(q))


def write_report(
    output_root: Path,
    *,
    input_rows_read: int,
    output_rows_written: int,
    duplicates_removed: int,
    generic_variants_fixed: int,
    needs_review_false: int,
    needs_review_true: int,
    category_rows_fixed: int,
    symptom_rows_fixed: int,
    scenario_rows_fixed: int,
    workaround_rows_fixed: int,
    version_history_rows_fixed: int,
    data_family_changed_to_version_history: int,
    conflicting_bug_ids: Dict[str, List[str]],
    samples_clean: List[Dict[str, Any]],
    samples_review: List[Dict[str, Any]],
) -> Dict[str, Any]:
    report = {
        "input rows read": input_rows_read,
        "output rows written": output_rows_written,
        "duplicates removed": duplicates_removed,
        "generic variants removed or fixed": generic_variants_fixed,
        "rows marked needs_review false": needs_review_false,
        "rows marked needs_review true": needs_review_true,
        "category rows fixed": category_rows_fixed,
        "symptom rows fixed": symptom_rows_fixed,
        "scenario rows fixed": scenario_rows_fixed,
        "workaround rows fixed": workaround_rows_fixed,
        "version-history rows fixed": version_history_rows_fixed,
        "data_family changed to release_notes_generic": data_family_changed_to_version_history,
        "conflicting Bug IDs found": len(conflicting_bug_ids),
        "conflicting_bug_ids": conflicting_bug_ids,
        "sample 10 clean rows": samples_clean[:10],
        "sample 10 needs_review rows": samples_review[:10],
    }
    (output_root / "release_notes_10000_fixed_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    lines = ["# Release Notes 10000 Repair Report", ""]
    for key, value in report.items():
        if key.startswith("sample "):
            continue
        lines.append(f"- {key}: {value}")
    lines.append("")
    lines.append("## Sample Clean Rows")
    for item in samples_clean[:10]:
        lines.append(f"- `{json.dumps(item, ensure_ascii=False, separators=(',', ':'))}`")
    lines.append("")
    lines.append("## Sample Needs Review Rows")
    for item in samples_review[:10]:
        lines.append(f"- `{json.dumps(item, ensure_ascii=False, separators=(',', ':'))}`")
    (output_root / "release_notes_10000_fixed_report.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return report


def write_samples_md(output_root: Path, samples_clean: List[Dict[str, Any]], samples_review: List[Dict[str, Any]]) -> None:
    lines = ["# Release Notes 10000 Samples", ""]
    lines.append("## Clean Rows")
    for item in samples_clean[:10]:
        lines.append(f"- `{json.dumps(item, ensure_ascii=False, separators=(',', ':'))}`")
    lines.append("")
    lines.append("## Needs Review Rows")
    for item in samples_review[:10]:
        lines.append(f"- `{json.dumps(item, ensure_ascii=False, separators=(',', ':'))}`")
    (output_root / "release_notes_10000_fixed_samples.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-root", type=Path, default=DEFAULT_INPUT_ROOT)
    parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT_ROOT)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args(argv)

    if args.workers < 1:
        parser.error("--workers must be >= 1")

    input_root = args.input_root.resolve()
    output_root = args.output_root.resolve()
    output_tree_root = output_root / TARGET_SWITCH
    if output_root.exists() and any(output_root.iterdir()) and not args.force:
        raise FileExistsError(f"Output already exists under {output_root}; pass --force to replace it")

    eprint(f"[INPUT] reading cleaned JSONL: {input_root}")
    eprint(f"[OUTPUT] root: {output_root}")
    eprint(f"[WORKERS] parallel workers: {args.workers}")

    input_files = sorted(path for path in input_root.rglob("train_chat.jsonl") if path.is_file())
    eprint(f"[INPUT] source files: {len(input_files)}")

    results: List[FileResult] = []
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {executor.submit(process_file, input_root, path): path for path in input_files}
        for future in as_completed(futures):
            path = futures[future]
            result = future.result()
            results.append(result)
            eprint(f"[FILE] processed {result.rel_path}")
            eprint(f"[FIX] category row fixed: {result.stats['category_rows_fixed']}")
            eprint(f"[FIX] symptom row fixed: {result.stats['symptom_rows_fixed']}")
            eprint(f"[FIX] scenario row fixed: {result.stats['scenario_rows_fixed']}")
            eprint(f"[FIX] workaround row fixed: {result.stats['workaround_rows_fixed']}")
            eprint(f"[FIX] version-history row fixed: {result.stats['version_history_rows_fixed']}")
            eprint(f"[FIX] generic variant fixed: {result.stats['generic_variants_fixed']}")
            eprint(f"[REVIEW] needs_review true: {result.stats['needs_review_true']}")
            eprint(f"[REVIEW] needs_review false: {result.stats['needs_review_false']}")

    results.sort(key=lambda item: str(item.rel_path))
    output_tree_root.mkdir(parents=True, exist_ok=True)

    all_rows: List[Tuple[Tuple[int, int, str], Dict[str, Any]]] = []
    all_reviews: List[Dict[str, Any]] = []
    conflict_map: Dict[str, set] = defaultdict(set)
    samples_clean: List[Dict[str, Any]] = []
    samples_review: List[Dict[str, Any]] = []
    aggregate = Counter()

    for result in results:
        all_reviews.extend(result.reviews)
        aggregate.update(result.stats)
        for bug_id, categories in result.bug_categories.items():
            conflict_map[bug_id].update({c for c in categories if c})
        for ordinal, row in result.rows:
            all_rows.append(((ordinal[0], ordinal[1], str(result.rel_path)), row))
        for item in result.samples_clean:
            if len(samples_clean) < 10:
                samples_clean.append(item)
        for item in result.samples_review:
            if len(samples_review) < 10:
                samples_review.append(item)

    all_rows.sort(key=lambda item: item[0])
    deduped_rows: List[Dict[str, Any]] = []
    seen_keys: set[str] = set()
    duplicates_removed = 0
    for _, row in all_rows:
        question, answer = extract_qa(row)
        key = normalize(question) + "||" + normalize(answer)
        if key in seen_keys:
            duplicates_removed += 1
            continue
        seen_keys.add(key)
        deduped_rows.append(row)

    per_file_rows: Dict[Path, List[Dict[str, Any]]] = defaultdict(list)
    for row, result in zip(deduped_rows, [None] * len(deduped_rows)):
        pass
    # Rebuild per-file rows from the sorted rows to preserve the tree structure.
    for _, row in all_rows:
        question, answer = extract_qa(row)
        key = normalize(question) + "||" + normalize(answer)
        if key not in seen_keys:
            continue
    # Second pass with file mapping.
    seen_keys.clear()
    for result in results:
        for _, row in result.rows:
            question, answer = extract_qa(row)
            key = normalize(question) + "||" + normalize(answer)
            if key in seen_keys:
                continue
            seen_keys.add(key)
            rel_out = output_tree_root / result.rel_path
            per_file_rows[rel_out].append(row)

    conflicting_bug_ids = {
        bug_id: sorted(categories)
        for bug_id, categories in conflict_map.items()
        if len(categories) > 1
    }
    final_rows = [row for rows in per_file_rows.values() for row in rows]
    final_needs_review_true = sum(1 for row in final_rows if bool(row.get("needs_review")))
    final_needs_review_false = len(final_rows) - final_needs_review_true
    for row in final_rows:
        row.pop("needs_review", None)

    for path, rows in sorted(per_file_rows.items(), key=lambda item: str(item[0])):
        path.parent.mkdir(parents=True, exist_ok=True)
        write_jsonl(path, rows)

    review_path = output_root / "release_notes_10000_fixed_review.jsonl"
    write_jsonl(review_path, all_reviews)
    write_samples_md(output_root, samples_clean, samples_review)

    report = write_report(
        output_root,
        input_rows_read=sum(result.stats["input_rows_read"] for result in results),
        output_rows_written=len(final_rows),
        duplicates_removed=duplicates_removed,
        generic_variants_fixed=aggregate["generic_variants_fixed"],
        needs_review_false=final_needs_review_false,
        needs_review_true=final_needs_review_true,
        category_rows_fixed=aggregate["category_rows_fixed"],
        symptom_rows_fixed=aggregate["symptom_rows_fixed"],
        scenario_rows_fixed=aggregate["scenario_rows_fixed"],
        workaround_rows_fixed=aggregate["workaround_rows_fixed"],
        version_history_rows_fixed=aggregate["version_history_rows_fixed"],
        data_family_changed_to_version_history=aggregate["data_family_changed_to_version_history"],
        conflicting_bug_ids=conflicting_bug_ids,
        samples_clean=samples_clean,
        samples_review=samples_review,
    )

    eprint(f"[QUALITY] valid JSONL rows {report['output rows written']}")
    eprint(f"[QUALITY] duplicates removed {duplicates_removed}")
    eprint(f"[QUALITY] final rows {report['output rows written']}")
    eprint(f"[OUTPUT] saved fixed JSONL tree: {output_tree_root}")
    eprint(f"[OUTPUT] saved review JSONL: {review_path}")
    eprint(f"[OUTPUT] saved fixed report: {output_root / 'release_notes_10000_fixed_report.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
