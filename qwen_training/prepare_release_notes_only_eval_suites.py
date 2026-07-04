#!/usr/bin/env python3
"""Build release-notes-only strict inference suites from the release validation split."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Sequence, Tuple

from prepare_stratified_master_split import fact_group_key, normalize, qa, read_jsonl, sha256, write_jsonl


DEFAULT_SPLIT_DIR = Path("Data/final_json_release_repaired_v1/release_only_stratified_seed42")
SOURCE_DISJOINT_ROWS = 100
LEGACY_ROWS = 65


def digest(seed: int, value: str) -> str:
    return hashlib.sha256(f"{seed}|{value}".encode("utf-8")).hexdigest()


def canonical_row(rows: Sequence[Dict[str, Any]], seed: int, salt: str) -> Dict[str, Any]:
    def key(row: Dict[str, Any]) -> Tuple[int, str, str]:
        return (
            1 if normalize(row.get("augmentation_type")) else 0,
            digest(seed, f"{salt}|{fact_group_key(row)}|{normalize(qa(row)[0])}"),
            digest(seed + 1, json.dumps(row, sort_keys=True, ensure_ascii=False)),
        )

    return sorted(rows, key=key)[0]


def source_type(row: Mapping[str, Any]) -> str:
    return normalize(row.get("source_type")) or "missing"


def build_group_index(rows: Sequence[Dict[str, Any]], seed: int) -> Dict[str, Dict[str, Any]]:
    grouped: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[fact_group_key(row)].append(row)
    return {group_key: canonical_row(items, seed, group_key) for group_key, items in grouped.items()}


def proportional_quotas(counts: Mapping[str, int], total: int) -> Dict[str, int]:
    if total <= 0:
        return {}
    keys = sorted(counts)
    count_sum = sum(int(counts[key]) for key in keys)
    if count_sum <= 0:
        raise ValueError("Cannot allocate quotas from an empty pool")
    raw = {key: total * int(counts[key]) / count_sum for key in keys}
    quotas = {key: int(raw[key]) for key in keys}
    remainder = total - sum(quotas.values())
    if remainder > 0:
        ranking = sorted(
            keys,
            key=lambda key: (- (raw[key] - quotas[key]), -int(counts[key]), key),
        )
        for key in ranking[:remainder]:
            quotas[key] += 1
    return {key: quota for key, quota in quotas.items() if quota > 0}


def select_groups(
    pool: Mapping[str, List[str]],
    rows_by_group: Mapping[str, Dict[str, Any]],
    total: int,
    seed: int,
    label: str,
) -> List[Dict[str, Any]]:
    counts = {source: len(groups) for source, groups in pool.items() if groups}
    quotas = proportional_quotas(counts, total)
    selected_groups: List[str] = []
    for source in sorted(quotas):
        candidates = sorted(pool[source], key=lambda group: digest(seed, f"{label}|{source}|{group}"))
        if len(candidates) < quotas[source]:
            raise ValueError(f"Not enough groups for {label}/{source}: need {quotas[source]}, have {len(candidates)}")
        selected_groups.extend(candidates[: quotas[source]])
    if len(selected_groups) != total:
        raise AssertionError(f"{label} expected {total} groups, selected {len(selected_groups)}")
    return [rows_by_group[group] for group in sorted(selected_groups, key=lambda group: digest(seed + 1, f"{label}|{group}"))]


def build_suite_manifest(
    suite_rows: Sequence[Dict[str, Any]],
    train_rows: Sequence[Dict[str, Any]],
    suite_path: Path,
    train_path: Path,
    seed: int,
) -> Dict[str, Any]:
    suite_questions = {normalize(qa(row)[0]) for row in suite_rows}
    suite_facts = {fact_group_key(row) for row in suite_rows}
    train_questions = {normalize(qa(row)[0]) for row in train_rows}
    train_facts = {fact_group_key(row) for row in train_rows}
    return {
        "seed": seed,
        "rows": len(suite_rows),
        "zero_fact_group_overlap_with_train": len(suite_facts & train_facts) == 0,
        "zero_exact_question_overlap_with_train": len(suite_questions & train_questions) == 0,
        "duplicate_questions": len(suite_questions) != len(suite_rows),
        "family_counts": dict(Counter(normalize(row.get("data_family")) for row in suite_rows)),
        "source_type_counts": dict(Counter(source_type(row) for row in suite_rows)),
        "files": {
            "train": {"path": str(train_path), "sha256": sha256(train_path)},
            "suite": {"path": str(suite_path), "sha256": sha256(suite_path)},
        },
    }


def build_suites(split_dir: Path, seed: int, overwrite: bool) -> Dict[str, Any]:
    train_path = split_dir / "train_chat_release_only.jsonl"
    validation_path = split_dir / "val_chat_release_only.jsonl"
    if not train_path.is_file():
        raise FileNotFoundError(train_path)
    if not validation_path.is_file():
        raise FileNotFoundError(validation_path)

    train_rows = read_jsonl(train_path)
    validation_rows = read_jsonl(validation_path)
    rows_by_group = build_group_index(validation_rows, seed)

    validation_groups_by_source: Dict[str, List[str]] = defaultdict(list)
    for row in validation_rows:
        validation_groups_by_source[source_type(row)].append(fact_group_key(row))
    for source in validation_groups_by_source:
        validation_groups_by_source[source] = sorted(set(validation_groups_by_source[source]))

    suite_specs = [
        ("release_source_disjoint100", SOURCE_DISJOINT_ROWS, seed),
        ("release_legacy65", LEGACY_ROWS, seed + 1),
    ]
    used_groups: set[str] = set()
    summary: Dict[str, Any] = {"seed": seed, "split_dir": str(split_dir), "suites": {}}
    for label, total, suite_seed in suite_specs:
        available_pool: Dict[str, List[str]] = defaultdict(list)
        for source, groups in validation_groups_by_source.items():
            remaining = [group for group in groups if group not in used_groups]
            if remaining:
                available_pool[source].extend(remaining)
        suite_rows = select_groups(available_pool, rows_by_group, total, suite_seed, label)
        suite_groups = {fact_group_key(row) for row in suite_rows}
        if used_groups & suite_groups:
            raise AssertionError(f"Suite overlap detected for {label}")
        used_groups.update(suite_groups)

        suite_path = split_dir / f"{label}.jsonl"
        if suite_path.exists() and not overwrite:
            raise FileExistsError(f"Refusing to overwrite existing suite file: {suite_path}")
        write_jsonl(suite_path, suite_rows)
        manifest = build_suite_manifest(
            suite_rows,
            train_rows,
            suite_path,
            train_path,
            suite_seed,
        )
        manifest_path = split_dir / f"{label}_manifest.json"
        manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
        summary["suites"][label] = {
            "path": str(suite_path),
            "manifest": str(manifest_path),
            "rows": len(suite_rows),
            "sha256": sha256(suite_path),
        }
        summary.setdefault("_suite_groups", {})[label] = sorted(suite_groups)
        summary.setdefault("_suite_questions", {})[label] = sorted({normalize(qa(row)[0]) for row in suite_rows})

    suite_group_sets = summary.get("_suite_groups", {})
    suite_question_sets = summary.get("_suite_questions", {})
    source_groups = set(suite_group_sets.get("release_source_disjoint100", []))
    legacy_groups = set(suite_group_sets.get("release_legacy65", []))
    source_questions = set(suite_question_sets.get("release_source_disjoint100", []))
    legacy_questions = set(suite_question_sets.get("release_legacy65", []))
    summary["zero_fact_group_overlap_between_suites"] = len(source_groups & legacy_groups) == 0
    summary["zero_exact_question_overlap_between_suites"] = len(source_questions & legacy_questions) == 0
    summary.pop("_suite_groups", None)
    summary.pop("_suite_questions", None)

    summary_path = split_dir / "release_eval_suites_manifest.json"
    summary_path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return summary


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--split_dir", type=Path, default=DEFAULT_SPLIT_DIR)
    parser.add_argument("--seed", type=int, default=43)
    parser.add_argument("--overwrite", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    build_suites(args.split_dir, args.seed, args.overwrite)


if __name__ == "__main__":
    main()
