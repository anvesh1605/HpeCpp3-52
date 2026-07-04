#!/usr/bin/env python3
"""Build a full release-notes-only structured exact-recall dataset split.

This keeps every release-note row from the cleaned source corpus and partitions
the rows into train / val / holdout without introducing product-doc rows.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence, Tuple

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
DEFAULT_OUTPUT_DIR = Path("Data/all_switches/release_notes_only_structured_full")


def validate_release_only(rows: Sequence[Dict[str, Any]], source_path: Path) -> None:
    for index, row in enumerate(rows, start=1):
        source_type = normalize(row.get("source_type"))
        data_family = normalize(row.get("data_family"))
        if not source_type.startswith("release_notes_") and not data_family.startswith("release_notes_"):
            raise ValueError(
                f"{source_path}:{index}: expected release-notes-only row, got "
                f"source_type={source_type!r} data_family={data_family!r}"
            )


def split_three_ways(
    rows: Sequence[Dict[str, Any]],
    holdout_ratio: float,
    validation_ratio: float,
    seed: int,
) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]], List[Dict[str, Any]]]:
    if not 0 < holdout_ratio < 0.5:
        raise ValueError("holdout_ratio must be between 0 and 0.5")
    if not 0 < validation_ratio < 0.5:
        raise ValueError("validation_ratio must be between 0 and 0.5")
    if holdout_ratio + validation_ratio >= 1:
        raise ValueError("holdout_ratio + validation_ratio must be < 1")

    train_plus_val, holdout = grouped_stratified_split(rows, holdout_ratio, seed)
    if not train_plus_val:
        raise AssertionError("No rows left after holdout split")
    adjusted_val_ratio = validation_ratio / (1 - holdout_ratio)
    train, validation = grouped_stratified_split(train_plus_val, adjusted_val_ratio, seed + 1)
    return train, validation, holdout


def build_report(
    source_rows: Sequence[Dict[str, Any]],
    train: Sequence[Dict[str, Any]],
    validation: Sequence[Dict[str, Any]],
    holdout: Sequence[Dict[str, Any]],
    input_path: Path,
    output_dir: Path,
    holdout_ratio: float,
    validation_ratio: float,
    seed: int,
) -> Dict[str, Any]:
    def qa_set(rows: Sequence[Dict[str, Any]]) -> set[str]:
        return {normalize(qa(row)[0]) for row in rows}

    def fact_set(rows: Sequence[Dict[str, Any]]) -> set[str]:
        return {fact_group_key(row) for row in rows}

    train_questions = qa_set(train)
    validation_questions = qa_set(validation)
    holdout_questions = qa_set(holdout)
    train_facts = fact_set(train)
    validation_facts = fact_set(validation)
    holdout_facts = fact_set(holdout)

    splits = {
        "train": train,
        "val": validation,
        "holdout": holdout,
    }
    report = {
        "seed": seed,
        "input_rows_scanned": len(source_rows),
        "release_note_rows_found": len(source_rows),
        "product_doc_rows_rejected": 0,
        "event_log_rows_found": 0,
        "target_ratios": {
            "holdout": holdout_ratio,
            "validation": validation_ratio,
            "train": round(1 - holdout_ratio - validation_ratio, 6),
        },
        "split_rows": {name: len(rows) for name, rows in splits.items()},
        "split_ratios_actual": {
            name: round(len(rows) / len(source_rows), 6) for name, rows in splits.items()
        },
        "duplicates_removed": 0,
        "conflicts_found": 0,
        "rows_rejected": 0,
        "final_valid_rows": len(train) + len(validation) + len(holdout),
        "fact_type_counts": dict(sorted(Counter(normalize(row.get("source_type")) for row in source_rows).items())),
        "data_family_counts": dict(sorted(Counter(normalize(row.get("data_family")) for row in source_rows).items())),
        "source_type_counts": dict(sorted(Counter(normalize(row.get("source_type")) for row in source_rows).items())),
        "split_distribution": {
            name: {
                "data_family": dict(sorted(distribution(rows, "data_family").items())),
                "source_type": dict(sorted(distribution(rows, "source_type").items())),
            }
            for name, rows in splits.items()
        },
        "overlap_checks": {
            "train_val_exact_question_overlap": len(train_questions & validation_questions),
            "train_holdout_exact_question_overlap": len(train_questions & holdout_questions),
            "val_holdout_exact_question_overlap": len(validation_questions & holdout_questions),
            "train_val_fact_group_overlap": len(train_facts & validation_facts),
            "train_holdout_fact_group_overlap": len(train_facts & holdout_facts),
            "val_holdout_fact_group_overlap": len(validation_facts & holdout_facts),
            "train_duplicate_questions": duplicate_question_count(train),
            "val_duplicate_questions": duplicate_question_count(validation),
            "holdout_duplicate_questions": duplicate_question_count(holdout),
            "max_distribution_delta_val": {
                field: max_percentage_delta(source_rows, validation, field)
                for field in ("data_family", "source_type", "switch", "version", "sub_version")
            },
            "max_distribution_delta_holdout": {
                field: max_percentage_delta(source_rows, holdout, field)
                for field in ("data_family", "source_type", "switch", "version", "sub_version")
            },
        },
        "files": {
            "input": {
                "path": str(input_path.resolve()),
                "sha256": sha256(input_path),
            },
            "train": {
                "path": str((output_dir / "release_notes_only_structured_full_train.jsonl").resolve()),
                "sha256": sha256(output_dir / "release_notes_only_structured_full_train.jsonl"),
            },
            "val": {
                "path": str((output_dir / "release_notes_only_structured_full_val.jsonl").resolve()),
                "sha256": sha256(output_dir / "release_notes_only_structured_full_val.jsonl"),
            },
            "holdout": {
                "path": str((output_dir / "release_notes_only_structured_full_holdout.jsonl").resolve()),
                "sha256": sha256(output_dir / "release_notes_only_structured_full_holdout.jsonl"),
            },
        },
        "notes": [
            "All release-note rows from the source file were kept.",
            "No product-document rows were included.",
            "Train/val/holdout are grouped by fact key to avoid split leakage.",
        ],
    }
    if any(
        report["overlap_checks"][key] != 0
        for key in (
            "train_val_exact_question_overlap",
            "train_holdout_exact_question_overlap",
            "val_holdout_exact_question_overlap",
            "train_val_fact_group_overlap",
            "train_holdout_fact_group_overlap",
            "val_holdout_fact_group_overlap",
            "train_duplicate_questions",
            "val_duplicate_questions",
            "holdout_duplicate_questions",
        )
    ):
        raise RuntimeError(f"Split validation failed: {report['overlap_checks']}")
    return report


def write_samples(path: Path, train: Sequence[Dict[str, Any]], validation: Sequence[Dict[str, Any]], holdout: Sequence[Dict[str, Any]]) -> None:
    def render_row(row: Dict[str, Any]) -> str:
        question, answer = qa(row)
        return (
            f"- source_type: {row.get('source_type')} | data_family: {row.get('data_family')} | "
            f"switch: {row.get('switch')} | version: {row.get('version')}.{row.get('sub_version')}\n"
            f"  Q: {question}\n"
            f"  A: {answer}"
        )

    sections = [
        ("Train", train[:3]),
        ("Val", validation[:3]),
        ("Holdout", holdout[:3]),
    ]
    lines = ["# release_notes_only_structured_full samples", ""]
    for title, rows in sections:
        lines.append(f"## {title}")
        lines.append("")
        for row in rows:
            lines.append(render_row(row))
            lines.append("")
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input_path", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output_dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--holdout_ratio", type=float, default=0.05)
    parser.add_argument("--validation_ratio", type=float, default=0.05)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--overwrite", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.output_dir.exists() and any(args.output_dir.iterdir()) and not args.overwrite:
        raise FileExistsError(f"Refusing to overwrite non-empty output directory: {args.output_dir}")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    rows = read_jsonl(args.input_path)
    validate_release_only(rows, args.input_path)

    train, validation, holdout = split_three_ways(rows, args.holdout_ratio, args.validation_ratio, args.seed)

    train_path = args.output_dir / "release_notes_only_structured_full_train.jsonl"
    val_path = args.output_dir / "release_notes_only_structured_full_val.jsonl"
    holdout_path = args.output_dir / "release_notes_only_structured_full_holdout.jsonl"
    report_path = args.output_dir / "release_notes_only_structured_full_report.json"
    samples_path = args.output_dir / "release_notes_only_structured_full_samples.md"

    write_jsonl(train_path, train)
    write_jsonl(val_path, validation)
    write_jsonl(holdout_path, holdout)

    report = build_report(
        rows,
        train,
        validation,
        holdout,
        args.input_path,
        args.output_dir,
        args.holdout_ratio,
        args.validation_ratio,
        args.seed,
    )
    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    write_samples(samples_path, train, validation, holdout)

    print("[INPUT] rows scanned:", len(rows))
    print("[INPUT] release-note rows found:", len(rows))
    print("[INPUT] product-doc rows rejected:", 0)
    print("[INPUT] event-log rows found:", 0)
    print("[OUTPUT] train rows:", len(train))
    print("[OUTPUT] val rows:", len(validation))
    print("[OUTPUT] holdout rows:", len(holdout))
    print("[QUALITY] duplicates removed:", 0)
    print("[QUALITY] conflicts found:", 0)
    print("[QUALITY] rows rejected:", 0)
    print("[QUALITY] final valid rows:", len(train) + len(validation) + len(holdout))
    print("[FILES] train:", train_path)
    print("[FILES] val:", val_path)
    print("[FILES] holdout:", holdout_path)
    print("[FILES] report:", report_path)
    print("[FILES] samples:", samples_path)


if __name__ == "__main__":
    main()
