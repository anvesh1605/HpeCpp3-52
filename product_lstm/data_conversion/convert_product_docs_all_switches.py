#!/usr/bin/env python3
"""Bulk convert product documentation into a mirrored LSTM-ready tree.

This wrapper runs the existing deterministic product-doc converter once per
`train_chat.jsonl` file, preserves the original switch/version directory
structure under a new output root, and then writes merged all-switch artifacts.
Ollama is intentionally disabled at this stage.
"""

from __future__ import annotations

import argparse
import contextlib
import json
import os
import sys
from collections import Counter, defaultdict
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path
from typing import Any, Dict, Iterable, Iterator, List, Mapping, Optional, Sequence, Tuple

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPT_DIR.parent

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from scripts import convert_product_docs_pipeline as pipeline


def collapse(value: Any) -> str:
    return pipeline.collapse(value)


def load_jsonl(path: Path) -> Iterator[Dict[str, Any]]:
    with path.open("r", encoding="utf-8-sig") as handle:
        for line in handle:
            if not line.strip():
                continue
            row = json.loads(line)
            if not isinstance(row, dict):
                raise ValueError(f"Expected object row in {path}")
            yield row


def write_jsonl(path: Path, rows: Iterable[Mapping[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(dict(row), ensure_ascii=False, separators=(",", ":")) + "\n")


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def relative_switch_version(input_file: Path, input_root: Path) -> Tuple[str, str]:
    relative_parent = input_file.parent.relative_to(input_root)
    parts = relative_parent.parts
    if len(parts) < 2:
        raise ValueError(f"Expected switch/version folders under {input_root}, got {input_file}")
    return parts[0], "/".join(parts[1:])


def output_dir_for(input_file: Path, input_root: Path, output_root: Path) -> Path:
    return output_root / input_file.parent.relative_to(input_root)


def record_key(row: Mapping[str, Any]) -> str:
    return json.dumps(dict(row), sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def sample_clean_row(row: Mapping[str, Any]) -> Dict[str, Any]:
    slots = row.get("slots") or {}
    return {
        "input_text": collapse(row.get("input_text")),
        "intent": collapse(row.get("intent")),
        "slots": slots,
        "target_value": collapse(row.get("target_value")),
    }


def sample_review_row(row: Mapping[str, Any]) -> Dict[str, Any]:
    slots = row.get("slots") or {}
    return {
        "input_text": collapse(row.get("input_text")),
        "intent": collapse(row.get("intent")),
        "slots": slots,
        "target_value": collapse(row.get("target_value")),
        "review_reason": collapse(row.get("review_reason")),
    }


def choose_input_files(input_root: Path) -> List[Path]:
    if input_root.is_file():
        return [input_root] if input_root.name == "train_chat.jsonl" else []
    discovered = sorted(
        path
        for path in input_root.rglob("train_chat.jsonl")
        if path.is_file()
        and not any(part.lower() in {".venv", "__pycache__", "logs", "outputs"} for part in path.parts)
    )
    return discovered


def run_one_file(
    input_file: Path,
    input_root: Path,
    output_root: Path,
    log_root: Path,
) -> Tuple[Path, Path, Path, Path]:
    output_dir = output_dir_for(input_file, input_root, output_root)
    output_dir.mkdir(parents=True, exist_ok=True)
    switch_name, version_path = relative_switch_version(input_file, input_root)
    log_path = log_root / switch_name / f"{version_path.replace('/', '__')}.log"
    log_path.parent.mkdir(parents=True, exist_ok=True)

    args = [
        "--input",
        str(input_file),
        "--output",
        str(output_dir / "product_dataset.jsonl"),
        "--review-output",
        str(output_dir / "product_review.jsonl"),
        "--report-output",
        str(output_dir / "product_report.json"),
        "--samples-output",
        str(output_dir / "product_samples.md"),
        "--force",
    ]

    print(f"[RUN] {input_file.relative_to(input_root)}")
    with log_path.open("w", encoding="utf-8", newline="\n") as log_handle:
        with contextlib.redirect_stdout(log_handle), contextlib.redirect_stderr(log_handle):
            exit_code = pipeline.main(args)
    if exit_code != 0:
        raise RuntimeError(f"Conversion failed for {input_file} (exit code {exit_code})")

    print(f"[DONE] {input_file.relative_to(input_root)}")
    return (
        output_dir / "product_dataset.jsonl",
        output_dir / "product_review.jsonl",
        output_dir / "product_report.json",
        output_dir / "product_samples.md",
    )


def run_one_file_worker(
    input_file: Path,
    input_root: Path,
    output_root: Path,
    log_root: Path,
) -> Tuple[Path, Path, Path, Path, Path]:
    output_dir = output_dir_for(input_file, input_root, output_root)
    output_dir.mkdir(parents=True, exist_ok=True)
    switch_name, version_path = relative_switch_version(input_file, input_root)
    log_path = log_root / switch_name / f"{version_path.replace('/', '__')}.log"
    log_path.parent.mkdir(parents=True, exist_ok=True)

    args = [
        "--input",
        str(input_file),
        "--output",
        str(output_dir / "product_dataset.jsonl"),
        "--review-output",
        str(output_dir / "product_review.jsonl"),
        "--report-output",
        str(output_dir / "product_report.json"),
        "--samples-output",
        str(output_dir / "product_samples.md"),
        "--force",
    ]

    with log_path.open("w", encoding="utf-8", newline="\n") as log_handle:
        with contextlib.redirect_stdout(log_handle), contextlib.redirect_stderr(log_handle):
            exit_code = pipeline.main(args)
    if exit_code != 0:
        raise RuntimeError(f"Conversion failed for {input_file} (exit code {exit_code})")

    return (
        output_dir / "product_dataset.jsonl",
        output_dir / "product_review.jsonl",
        output_dir / "product_report.json",
        output_dir / "product_samples.md",
        input_file,
    )


def build_merged_outputs(
    produced: Sequence[Tuple[Path, Path, Path, Path, Path]],
    output_root: Path,
) -> Dict[str, Any]:
    clean_rows: List[Dict[str, Any]] = []
    review_rows: List[Dict[str, Any]] = []
    rows_by_switch: Counter[str] = Counter()
    rows_by_version: Counter[str] = Counter()
    rows_by_intent: Counter[str] = Counter()
    review_reasons: Counter[str] = Counter()
    invalid_jsonl_lines = 0
    empty_input_text = 0
    empty_target_value = 0
    duplicates_removed = 0
    rows_fixed_deterministically = 0
    markdown_matched_rows = 0
    markdown_missing_rows = 0
    top_commands: Counter[str] = Counter()
    top_event_ids: Counter[str] = Counter()
    samples_clean: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    samples_review: Dict[str, List[Dict[str, Any]]] = defaultdict(list)

    seen_clean: set[str] = set()

    for dataset_path, review_path, report_path, _samples_path, input_file in produced:
        report = json.loads(report_path.read_text(encoding="utf-8"))
        rows_fixed_deterministically += int(report.get("rows_fixed_deterministically", 0))
        markdown_matched_rows += int(report.get("markdown_matched_rows", 0))
        markdown_missing_rows += int(report.get("markdown_missing_rows", 0))
        invalid_jsonl_lines += int(report.get("invalid_jsonl_lines", 0))
        empty_input_text += int(report.get("empty_input_text", 0))
        empty_target_value += int(report.get("empty_target_value", 0))
        review_reasons.update(report.get("review_reasons") or {})

        switch_name, version_path = relative_switch_version(input_file, ROOT_DIR / "full_product_docs")
        version_key = f"{switch_name}/{version_path}"

        for row in load_jsonl(dataset_path):
            key = record_key(row)
            if key in seen_clean:
                duplicates_removed += 1
                continue
            seen_clean.add(key)
            clean_rows.append(row)
            intent = collapse(row.get("intent"))
            rows_by_switch[switch_name] += 1
            rows_by_version[version_key] += 1
            rows_by_intent[intent] += 1
            command = collapse((row.get("slots") or {}).get("command"))
            event_id = collapse((row.get("slots") or {}).get("event_id"))
            if command:
                top_commands[command] += 1
            if event_id:
                top_event_ids[event_id] += 1
            if len(samples_clean[intent]) < 3:
                samples_clean[intent].append(sample_clean_row(row))

        for row in load_jsonl(review_path):
            review_rows.append(row)
            reason = collapse(row.get("review_reason")) or "review"
            if len(samples_review[reason]) < 3:
                samples_review[reason].append(sample_review_row(row))

    merged_report = {
        "total_rows_scanned": sum(int(json.loads(report_path.read_text(encoding="utf-8")).get("rows_scanned", 0)) for _dp, _rp, report_path, _sp, _if in produced),
        "total_rows_written": len(clean_rows),
        "total_review_rows": len(review_rows),
        "rows_by_switch": dict(sorted(rows_by_switch.items())),
        "rows_by_version": dict(sorted(rows_by_version.items())),
        "rows_by_intent": dict(sorted(rows_by_intent.items())),
        "review_reasons": dict(sorted(review_reasons.items())),
        "invalid_jsonl_lines": invalid_jsonl_lines,
        "empty_input_text": empty_input_text,
        "empty_target_value": empty_target_value,
        "duplicates_removed": duplicates_removed,
        "rows_fixed_deterministically": rows_fixed_deterministically,
        "markdown_matched_rows": markdown_matched_rows,
        "markdown_missing_rows": markdown_missing_rows,
        "top_50_commands": top_commands.most_common(50),
        "top_50_event_ids": top_event_ids.most_common(50),
        "sample_clean_rows_per_intent": {intent: rows for intent, rows in sorted(samples_clean.items())},
        "sample_review_rows_per_reason": {reason: rows for reason, rows in sorted(samples_review.items())},
    }

    write_jsonl(output_root / "all_switches_product_dataset.jsonl", clean_rows)
    write_jsonl(output_root / "all_switches_product_review.jsonl", review_rows)
    write_json(output_root / "all_switches_product_report.json", merged_report)

    return merged_report


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input-root",
        type=Path,
        default=ROOT_DIR / "full_product_docs",
        help="Root directory containing switch/version train_chat.jsonl files.",
    )
    parser.add_argument(
        "--output-root",
        type=Path,
        default=ROOT_DIR / "lstm_conversion" / "converted_product",
        help="Root directory for mirrored product conversion outputs.",
    )
    parser.add_argument(
        "--log-root",
        type=Path,
        default=ROOT_DIR / "lstm_conversion" / "converted_product" / "_logs",
        help="Directory for per-version conversion logs.",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=max(1, (os.cpu_count() or 4) // 2),
        help="Parallel worker process count.",
    )
    parser.add_argument("--force", action="store_true", help="Overwrite existing outputs.")
    return parser.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    try:
        import sys as _sys

        _sys.stdout.reconfigure(encoding="utf-8", errors="replace", line_buffering=True)
        _sys.stderr.reconfigure(encoding="utf-8", errors="replace", line_buffering=True)
    except Exception:
        pass

    args = parse_args(argv)
    input_root = args.input_root.resolve()
    output_root = args.output_root.resolve()
    log_root = args.log_root.resolve()

    if not input_root.exists():
        raise FileNotFoundError(input_root)

    if output_root.exists() and not args.force:
        raise FileExistsError(f"Refusing to overwrite {output_root}; pass --force")
    if args.workers < 1:
        raise ValueError("--workers must be >= 1")

    input_files = choose_input_files(input_root)
    if not input_files:
        raise FileNotFoundError(f"No train_chat.jsonl files found under {input_root}")

    output_root.mkdir(parents=True, exist_ok=True)
    log_root.mkdir(parents=True, exist_ok=True)

    produced: List[Tuple[Path, Path, Path, Path, Path]] = []
    print(f"[WORKERS] parallel workers: {args.workers}")
    with ProcessPoolExecutor(max_workers=args.workers) as executor:
        futures = {}
        for input_file in input_files:
            switch_name, version_path = relative_switch_version(input_file, input_root)
            log_path = log_root / switch_name / f"{version_path.replace('/', '__')}.log"
            print(f"[RUN] {input_file.relative_to(input_root)} log={log_path}")
            futures[executor.submit(run_one_file_worker, input_file, input_root, output_root, log_root)] = input_file

        for future in as_completed(futures):
            dataset_path, review_path, report_path, samples_path, input_file = future.result()
            produced.append((dataset_path, review_path, report_path, samples_path, input_file))
            print(f"[DONE] {input_file.relative_to(input_root)}")

    merged_report = build_merged_outputs(produced, output_root)
    print("[OUTPUT] saved per-version product conversion tree")
    print("[OUTPUT] saved merged all-switch product outputs")
    print(json.dumps(merged_report, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
