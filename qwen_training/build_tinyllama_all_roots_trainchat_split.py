#!/usr/bin/env python3
"""Build a TinyLlama training split from train_chat.jsonl under final_json and product_docs/full_product_docs."""

from __future__ import annotations

import argparse
import json
from types import SimpleNamespace
from collections import Counter
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence, Tuple

from build_global_dataset import validate_and_normalize
from prepare_stratified_master_split import distribution, grouped_stratified_split, qa, write_jsonl


DEFAULT_FINAL_JSON_ROOT = Path(r"E:\52\Train_w\Train\Data\final_json")
DEFAULT_PRODUCT_DOCS_ROOT = Path(r"E:\52\Train_w\Train\Data\product_docs\full_product_docs")
DEFAULT_OUTPUT_DIR = Path(r"E:\52\Train_w\Train\Data\all_switches\tinyllama_all_roots_trainchat_seed42")


def read_jsonl(path: Path) -> Iterable[Dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            line = line.strip()
            if not line:
                continue
            try:
                yield json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}:{line_number}: {exc}") from exc


def find_train_chat_files(root: Path) -> List[Path]:
    if not root.exists():
        raise FileNotFoundError(root)
    return sorted(path for path in root.rglob("train_chat.jsonl") if path.is_file())


def load_rows(
    files: Sequence[Path],
    data_root: Path,
    seen_questions: set[str] | None = None,
) -> List[Dict[str, Any]]:
    normalizer_args = SimpleNamespace(min_question_words=1, min_answer_words=1)
    rows: List[Dict[str, Any]] = []
    seen_questions = seen_questions if seen_questions is not None else set()
    drop_reasons: Counter[str] = Counter()
    for path in files:
        for line_number, row in enumerate(read_jsonl(path), 1):
            normalized, reason = validate_and_normalize(row, path, data_root, normalizer_args)
            if normalized is None:
                drop_reasons[reason or "unknown"] += 1
                continue
            question, _ = qa(normalized)
            qkey = question.strip().lower()
            if qkey in seen_questions:
                continue
            seen_questions.add(qkey)
            rows.append(normalized)
    return rows, drop_reasons


def summarize(rows: Sequence[Dict[str, Any]]) -> Dict[str, Any]:
    data_family_counts = Counter(str(row.get("data_family") or "missing") for row in rows)
    source_type_counts = Counter(str(row.get("source_type") or "missing") for row in rows)
    switch_counts = Counter(str(row.get("switch") or "missing") for row in rows)
    return {
        "total_rows": len(rows),
        "data_family_counts": dict(data_family_counts),
        "source_type_counts": dict(source_type_counts),
        "switch_counts": dict(switch_counts),
        "release_note_rows": sum(1 for row in rows if str(row.get("source_type") or "").startswith("release_notes_")),
        "product_doc_rows": sum(1 for row in rows if str(row.get("source_type") or "").startswith("product_")),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--final_json_root", type=Path, default=DEFAULT_FINAL_JSON_ROOT)
    parser.add_argument("--product_docs_root", type=Path, default=DEFAULT_PRODUCT_DOCS_ROOT)
    parser.add_argument("--output_dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--validation_ratio", type=float, default=0.05)
    parser.add_argument("--seed", type=int, default=42)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not 0 < args.validation_ratio < 0.5:
        raise ValueError("--validation_ratio must be between 0 and 0.5")
    if args.output_dir.exists():
        raise FileExistsError(f"Refusing to overwrite existing output directory: {args.output_dir}")

    final_files = find_train_chat_files(args.final_json_root)
    product_files = find_train_chat_files(args.product_docs_root)
    files = final_files + product_files
    if not files:
        raise FileNotFoundError("No train_chat.jsonl files found under the provided roots")

    seen_questions: set[str] = set()
    final_rows, final_drops = load_rows(files[: len(final_files)], args.final_json_root, seen_questions)
    product_rows, product_drops = load_rows(files[len(final_files) :], args.product_docs_root, seen_questions)
    rows = final_rows + product_rows
    train_rows, val_rows = grouped_stratified_split(rows, args.validation_ratio, args.seed)
    args.output_dir.mkdir(parents=True, exist_ok=False)
    write_jsonl(args.output_dir / "train_chat_all_roots_train.jsonl", train_rows)
    write_jsonl(args.output_dir / "train_chat_all_roots_val.jsonl", val_rows)
    write_jsonl(args.output_dir / "train_chat_all_roots_combined.jsonl", rows)

    report = {
        "final_json_root": str(args.final_json_root),
        "product_docs_root": str(args.product_docs_root),
        "files_scanned": len(files),
        "files_by_root": {
            "final_json": len(final_files),
            "product_docs_full_product_docs": len(product_files),
        },
        "summary": summarize(rows),
        "dropped_rows": {
            "final_json": dict(final_drops),
            "product_docs": dict(product_drops),
        },
        "train_count": len(train_rows),
        "validation_count": len(val_rows),
        "validation_ratio": args.validation_ratio,
        "train_distribution_source_type": dict(distribution(train_rows, "source_type")),
        "val_distribution_source_type": dict(distribution(val_rows, "source_type")),
    }
    (args.output_dir / "dataset_report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
