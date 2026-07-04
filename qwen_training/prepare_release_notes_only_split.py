#!/usr/bin/env python3
"""Build a deterministic grouped-stratified split for release-notes-only training."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict

from prepare_stratified_master_split import (
    distribution,
    duplicate_question_count,
    fact_group_key,
    grouped_stratified_split,
    max_percentage_delta,
    normalize,
    qa,
    read_jsonl,
    sha256,
    write_jsonl,
)


DEFAULT_INPUT = Path("Data/final_json_release_repaired_v1/release_notes_final_clean.jsonl")
DEFAULT_OUTPUT_DIR = Path("Data/final_json_release_repaired_v1/release_only_stratified_seed42")
DEFAULT_TEST_PATH = Path("Data/all_switches/test_chat_all_clean.jsonl")


def validate_release_only(rows: list[Dict[str, Any]], source_path: Path) -> None:
    for index, row in enumerate(rows, start=1):
        source_type = normalize(row.get("source_type"))
        data_family = normalize(row.get("data_family"))
        if not source_type.startswith("release_notes_") and not data_family.startswith("release_notes_"):
            raise ValueError(
                f"{source_path}:{index}: expected release-notes-only row, got source_type={source_type!r} "
                f"data_family={data_family!r}"
            )


def build_manifest(args: argparse.Namespace, rows: list[Dict[str, Any]], train: list[Dict[str, Any]], validation: list[Dict[str, Any]]) -> Dict[str, Any]:
    train_questions = {normalize(qa(row)[0]) for row in train}
    validation_questions = {normalize(qa(row)[0]) for row in validation}
    train_facts = {fact_group_key(row) for row in train}
    validation_facts = {fact_group_key(row) for row in validation}

    steps_per_epoch = len(train) // args.effective_batch_size
    report = {
        "seed": args.seed,
        "validation_ratio_requested": args.validation_ratio,
        "input_rows": len(rows),
        "train_rows": len(train),
        "validation_rows": len(validation),
        "validation_ratio_actual": round(len(validation) / len(rows), 6),
        "effective_batch_size": args.effective_batch_size,
        "steps_per_epoch": steps_per_epoch,
        "epoch_checkpoint_steps": [steps_per_epoch],
        "validation": {
            "exact_question_overlap": len(train_questions & validation_questions),
            "fact_group_overlap": len(train_facts & validation_facts),
            "train_duplicate_questions": duplicate_question_count(train),
            "validation_duplicate_questions": duplicate_question_count(validation),
            "max_distribution_delta": {
                field: max_percentage_delta(rows, validation, field)
                for field in ("data_family", "source_type", "switch", "version", "sub_version")
            },
        },
        "counts": {
            "train_by_data_family": dict(sorted(distribution(train, "data_family").items())),
            "validation_by_data_family": dict(sorted(distribution(validation, "data_family").items())),
            "train_by_source_type": dict(sorted(distribution(train, "source_type").items())),
            "validation_by_source_type": dict(sorted(distribution(validation, "source_type").items())),
        },
        "files": {
            "input": {
                "path": str(args.input_path.resolve()),
                "sha256": sha256(args.input_path),
            },
            "train": {
                "path": str(args.output_dir / "train_chat_release_only.jsonl"),
                "sha256": sha256(args.output_dir / "train_chat_release_only.jsonl"),
            },
            "validation": {
                "path": str(args.output_dir / "val_chat_release_only.jsonl"),
                "sha256": sha256(args.output_dir / "val_chat_release_only.jsonl"),
            },
            "untouched_test": {
                "path": str(args.test_path.resolve()),
                "sha256": sha256(args.test_path),
            },
        },
    }
    if any(
        report["validation"][key]
        for key in ("exact_question_overlap", "fact_group_overlap", "train_duplicate_questions", "validation_duplicate_questions")
    ):
        raise RuntimeError(f"Split validation failed: {report['validation']}")
    return report


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input_path", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output_dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--test_path", type=Path, default=DEFAULT_TEST_PATH)
    parser.add_argument("--validation_ratio", type=float, default=0.05)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--effective_batch_size", type=int, default=8)
    parser.add_argument("--overwrite", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not 0 < args.validation_ratio < 0.5:
        raise ValueError("validation_ratio must be between 0 and 0.5")
    if args.output_dir.exists() and not args.overwrite:
        raise FileExistsError(f"Refusing to overwrite output directory: {args.output_dir}")
    args.output_dir.mkdir(parents=True, exist_ok=True)

    rows = read_jsonl(args.input_path)
    validate_release_only(rows, args.input_path)

    train, validation = grouped_stratified_split(rows, args.validation_ratio, args.seed)
    train_out = args.output_dir / "train_chat_release_only.jsonl"
    validation_out = args.output_dir / "val_chat_release_only.jsonl"
    write_jsonl(train_out, train)
    write_jsonl(validation_out, validation)

    manifest = build_manifest(args, rows, train, validation)
    manifest_path = args.output_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
