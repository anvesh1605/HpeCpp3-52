#!/usr/bin/env python3
"""Create a deterministic strict holdout with no question or fact-key overlap with training."""

from __future__ import annotations

import argparse
import json
import random
from pathlib import Path
from typing import Any, Dict, List, Sequence, Set, Tuple

from prepare_focus_replay_pilot import (
    fact_key,
    family_counts,
    question_key,
    read_jsonl,
    read_legacy_questions,
    reference,
    says_no_workaround,
    sha256,
    shuffled,
    take_unique,
    write_jsonl,
)


QUOTAS = {
    "cli_command_reference": 20,
    "show_command_reference": 15,
    "release_notes_bug": 15,
    "event_log_reference": 15,
    "release_notes_generic": 5,
    "concept_explanation": 15,
    "configuration_procedure": 5,
    "broad": 10,
}
TARGET_FAMILIES = set(QUOTAS) - {"broad"}


def select_holdout(candidates: Sequence[Dict[str, Any]], rng: random.Random) -> List[Dict[str, Any]]:
    by_family: Dict[str, List[Dict[str, Any]]] = {}
    for row in candidates:
        by_family.setdefault(str(row.get("data_family", "")), []).append(row)
    used_questions: Set[str] = set()
    used_facts: Set[Tuple[str, ...]] = set()
    selected: List[Dict[str, Any]] = []
    for family, quota in QUOTAS.items():
        pool = (
            [row for row in candidates if row.get("data_family") not in TARGET_FAMILIES]
            if family == "broad"
            else by_family.get(family, [])
        )
        pool = shuffled(pool, rng)
        if family == "release_notes_bug":
            no_workaround = [row for row in pool if says_no_workaround(reference(row))]
            remainder = [row for row in pool if not says_no_workaround(reference(row))]
            # Only four source-disjoint no-workaround facts exist; retain all four.
            first = take_unique(no_workaround, 4, used_questions, used_facts)
            selected.extend(first)
            selected.extend(take_unique(remainder + no_workaround, quota - len(first), used_questions, used_facts))
        else:
            selected.extend(take_unique(pool, quota, used_questions, used_facts))
    if len(selected) != 100:
        raise AssertionError(f"Expected 100 rows, selected {len(selected)}")
    return selected


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--train_path", type=Path, default=Path("Data/all_switches/train_chat_all_clean_validated.jsonl"))
    parser.add_argument("--test_path", type=Path, default=Path("Data/all_switches/test_chat_all_clean.jsonl"))
    parser.add_argument("--inference_script", type=Path, default=Path("run_inference_1000step_adapter.py"))
    parser.add_argument("--output", type=Path, default=Path("Data/all_switches/strict_holdout_source_disjoint_100_seed43.jsonl"))
    parser.add_argument("--manifest", type=Path, default=Path("Data/all_switches/strict_holdout_source_disjoint_100_seed43_manifest.json"))
    parser.add_argument("--seed", type=int, default=43)
    parser.add_argument("--overwrite", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    existing = [path for path in (args.output, args.manifest) if path.exists()]
    if existing and not args.overwrite:
        raise FileExistsError(f"Refusing to overwrite existing outputs: {existing}")
    train_rows = read_jsonl(args.train_path)
    test_rows = read_jsonl(args.test_path)
    legacy_questions = read_legacy_questions(args.inference_script, test_rows)
    train_questions = {question_key(row) for row in train_rows}
    train_facts = {fact_key(row) for row in train_rows}
    candidates = [
        row
        for row in test_rows
        if question_key(row) not in train_questions
        and fact_key(row) not in train_facts
        and question_key(row) not in legacy_questions
    ]
    rows = select_holdout(candidates, random.Random(args.seed))
    random.Random(args.seed).shuffle(rows)
    questions = {question_key(row) for row in rows}
    facts = {fact_key(row) for row in rows}
    if len(questions) != 100 or len(facts) != 100:
        raise AssertionError("Source-disjoint holdout must contain unique questions and fact keys")
    if questions & train_questions or facts & train_facts:
        raise AssertionError("Training overlap detected in source-disjoint holdout")
    if questions & legacy_questions:
        raise AssertionError("Legacy-65 overlap detected in source-disjoint holdout")
    write_jsonl(args.output, rows)
    manifest = {
        "seed": args.seed,
        "source_files": {
            str(args.train_path): {"rows": len(train_rows), "sha256": sha256(args.train_path)},
            str(args.test_path): {"rows": len(test_rows), "sha256": sha256(args.test_path)},
            str(args.inference_script): {"sha256": sha256(args.inference_script)},
        },
        "holdout": {
            "path": str(args.output),
            "rows": len(rows),
            "candidate_rows_before_sampling": len(candidates),
            "family_counts": family_counts(rows),
            "no_workaround_bug_rows": sum(
                says_no_workaround(reference(row)) for row in rows if row.get("data_family") == "release_notes_bug"
            ),
            "sha256": sha256(args.output),
        },
        "exclusions": {
            "legacy_questions": len(legacy_questions),
            "exact_question_overlap_with_train": 0,
            "fact_key_overlap_with_train": 0,
        },
    }
    args.manifest.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(manifest, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
