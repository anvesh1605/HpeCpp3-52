#!/usr/bin/env python3
"""Create a deterministic, grouped-disjoint 100-row inference suite."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional, Sequence

from repair_dataset import (
    extract_qa,
    fact_group_key,
    is_cli_row,
    is_syntax_question,
    is_version_history_row,
    normalize,
    read_jsonl,
    sha256_file,
    write_jsonl,
)


DEFAULT_DATA_DIR = Path("final_json_clean/all_switches")
DEFAULT_OUTPUT = DEFAULT_DATA_DIR / "inference_balanced100.jsonl"
QUOTAS = {
    "cli_syntax": 20,
    "cli_description": 15,
    "cli_negative": 5,
    "release_notes_bug": 20,
    "version_history": 10,
    "event_log": 10,
    "concept": 10,
    "other": 10,
}


def digest(seed: int, value: str) -> str:
    return hashlib.sha256(f"{seed}|{value}".encode("utf-8")).hexdigest()


def category(row: Mapping[str, Any]) -> str:
    question, answer = extract_qa(row)
    if row.get("augmentation_type") == "unsupported_cli_option":
        return "cli_negative"
    if is_cli_row(row):
        if is_syntax_question(question) or normalize(answer).startswith("syntax:"):
            return "cli_syntax"
        return "cli_description"
    family = normalize(row.get("data_family"))
    if family == "release_notes_bug":
        return "release_notes_bug"
    if is_version_history_row(row):
        return "version_history"
    if family == "event_log_reference":
        return "event_log"
    if family == "concept_explanation":
        return "concept"
    return "other"


def question_key(row: Mapping[str, Any]) -> str:
    return normalize(extract_qa(row)[0])


def prepare(args: argparse.Namespace) -> Dict[str, Any]:
    data_dir = args.data_dir
    train_path = data_dir / "train_chat_all_clean.jsonl"
    val_path = data_dir / "val_chat_all_clean.jsonl"
    test_path = data_dir / "test_chat_all_clean.jsonl"
    for path in (train_path, val_path, test_path):
        if not path.is_file():
            raise FileNotFoundError(path)
    if args.output.exists() and not args.force:
        raise FileExistsError(f"Refusing to overwrite {args.output}; pass --force")

    train_groups = {fact_group_key(row) for row in read_jsonl(train_path)}
    val_groups = {fact_group_key(row) for row in read_jsonl(val_path)}
    train_questions = {question_key(row) for row in read_jsonl(train_path)}
    val_questions = {question_key(row) for row in read_jsonl(val_path)}

    candidates: Dict[str, Dict[str, Dict[str, Any]]] = defaultdict(dict)
    for row in read_jsonl(test_path):
        group = fact_group_key(row)
        qkey = question_key(row)
        if group in train_groups or group in val_groups:
            raise ValueError(f"Test fact group leaks into train/validation: {group}")
        if qkey in train_questions or qkey in val_questions:
            raise ValueError(f"Test question leaks into train/validation: {qkey}")
        label = category(row)
        existing = candidates[label].get(group)
        # Prefer canonical rows over generated paraphrases when both represent the same fact.
        if existing is None or (existing.get("augmentation_type") and not row.get("augmentation_type")):
            candidates[label][group] = row

    selected: List[Dict[str, Any]] = []
    counts: Counter[str] = Counter()
    for label, quota in QUOTAS.items():
        pool = list(candidates[label].values())
        pool.sort(key=lambda row: digest(args.seed, f"{label}|{fact_group_key(row)}|{question_key(row)}"))
        if len(pool) < quota:
            raise ValueError(f"Not enough {label} rows: need {quota}, have {len(pool)}")
        chosen = pool[:quota]
        selected.extend(chosen)
        counts[label] += len(chosen)

    selected.sort(key=lambda row: digest(args.seed + 1, question_key(row)))
    selected_groups = [fact_group_key(row) for row in selected]
    selected_questions = [question_key(row) for row in selected]
    if len(selected_groups) != len(set(selected_groups)):
        raise AssertionError("Selected suite contains repeated fact groups")
    if len(selected_questions) != len(set(selected_questions)):
        raise AssertionError("Selected suite contains duplicate questions")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    write_jsonl(args.output, selected)
    manifest = {
        "seed": args.seed,
        "rows": len(selected),
        "quotas": QUOTAS,
        "selected_counts": dict(counts),
        "zero_fact_group_overlap_with_train": True,
        "zero_fact_group_overlap_with_validation": True,
        "zero_exact_question_overlap_with_train": True,
        "zero_exact_question_overlap_with_validation": True,
        "files": {
            "train": {"path": str(train_path), "sha256": sha256_file(train_path)},
            "validation": {"path": str(val_path), "sha256": sha256_file(val_path)},
            "test": {"path": str(test_path), "sha256": sha256_file(test_path)},
            "suite": {"path": str(args.output), "sha256": sha256_file(args.output)},
        },
    }
    manifest_path = args.output.with_name(args.output.stem + "_manifest.json")
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, indent=2))
    return manifest


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--seed", type=int, default=43)
    parser.add_argument("--force", action="store_true")
    return parser.parse_args(argv)


if __name__ == "__main__":
    prepare(parse_args())
