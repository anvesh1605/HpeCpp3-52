#!/usr/bin/env python3
"""Build a deterministic grouped-stratified master train/validation split."""

from __future__ import annotations

import argparse
import hashlib
import json
import random
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence, Tuple


def normalize(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "").strip()).lower()


def qa(row: Dict[str, Any]) -> Tuple[str, str]:
    question = answer = ""
    for message in row.get("messages") or []:
        if message.get("role") == "user" and not question:
            question = str(message.get("content") or "").strip()
        elif message.get("role") == "assistant" and not answer:
            answer = str(message.get("content") or "").strip()
    return question, answer


def extract_number(pattern: str, *values: Any) -> str:
    for value in values:
        match = re.search(pattern, str(value or ""), re.I)
        if match:
            return match.group(1)
    return ""


def fact_group_key(row: Dict[str, Any]) -> str:
    question, answer = qa(row)
    family = normalize(row.get("data_family"))
    source = normalize(row.get("source_type"))
    switch = normalize(row.get("switch"))
    version = normalize(row.get("version"))
    sub_version = normalize(row.get("sub_version"))
    if family == "release_notes_bug":
        bug_id = normalize(row.get("bug_id")) or extract_number(r"\b(?:bug(?:\s+id)?\s*[:#-]?\s*)?(\d{5,7})\b", question, answer)
        return f"bug|{switch}|{version}|{sub_version}|{bug_id or normalize(question)}"
    if family == "event_log_reference":
        event_id = normalize(row.get("event_id")) or extract_number(r"\bevent(?:\s+id)?\s*[:#-]?\s*(\d{3,8})\b", question, answer)
        return f"event|{switch}|{version}|{event_id or normalize(row.get('topic')) or normalize(question)}"
    command = normalize(row.get("command") or row.get("command_name"))
    topic = normalize(row.get("topic"))
    title = normalize(row.get("document_title"))
    if command or family in {"cli_command_reference", "show_command_reference"}:
        identity = command or normalize(row.get("section")) or topic or normalize(question)
        return f"command|{source}|{switch}|{version}|{identity}"
    if title or topic:
        return f"topic|{source}|{family}|{switch}|{version}|{title}|{topic or normalize(row.get('section'))}"
    return f"question|{source}|{family}|{normalize(question)}"


def stratum_key(row: Dict[str, Any]) -> str:
    return f"{normalize(row.get('data_family'))}|{normalize(row.get('source_type'))}"


def read_jsonl(path: Path) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}:{line_number}: {exc}") from exc
            question, answer = qa(row)
            if not question or not answer or not row.get("data_family") or not row.get("source_type"):
                raise ValueError(f"{path}:{line_number}: invalid chat or metadata row")
            rows.append(row)
    return rows


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_jsonl(path: Path, rows: Iterable[Dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")


def distribution(rows: Sequence[Dict[str, Any]], field: str) -> Counter[str]:
    return Counter(normalize(row.get(field)) or "missing" for row in rows)


def max_percentage_delta(all_rows: Sequence[Dict[str, Any]], subset: Sequence[Dict[str, Any]], field: str) -> float:
    full = distribution(all_rows, field)
    part = distribution(subset, field)
    keys = set(full) | set(part)
    return round(max((abs(full[key] / len(all_rows) - part[key] / len(subset)) for key in keys), default=0.0), 6)


def grouped_stratified_split(rows: Sequence[Dict[str, Any]], validation_ratio: float, seed: int) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    groups: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for row in rows:
        groups[fact_group_key(row)].append(row)
    strata: Dict[str, List[Tuple[str, List[Dict[str, Any]]]]] = defaultdict(list)
    for key, items in groups.items():
        labels = {stratum_key(item) for item in items}
        if len(labels) == 1:
            stratum = next(iter(labels))
        else:
            families = {normalize(item.get("data_family")) for item in items}
            if len(families) != 1:
                raise ValueError(f"Fact group spans data families: {key}: {sorted(families)}")
            stratum = f"{next(iter(families))}|__mixed_source_fact__"
        strata[stratum].append((key, items))

    validation_keys = set()
    for stratum in sorted(strata):
        candidates = list(strata[stratum])
        random.Random(f"{seed}:{stratum}").shuffle(candidates)
        target = round(sum(len(items) for _, items in candidates) * validation_ratio)
        if len(candidates) >= 2 and target == 0:
            target = 1
        selected = 0
        for key, items in candidates:
            if selected >= target:
                break
            before = abs(target - selected)
            after = abs(target - (selected + len(items)))
            if after <= before or selected == 0:
                validation_keys.add(key)
                selected += len(items)

    train = [row for row in rows if fact_group_key(row) not in validation_keys]
    validation = [row for row in rows if fact_group_key(row) in validation_keys]
    random.Random(seed + 1).shuffle(train)
    random.Random(seed + 2).shuffle(validation)
    return train, validation


def duplicate_question_count(rows: Sequence[Dict[str, Any]]) -> int:
    counts = Counter(normalize(qa(row)[0]) for row in rows)
    return sum(count - 1 for count in counts.values() if count > 1)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--train_path", type=Path, required=True)
    parser.add_argument("--validation_path", type=Path, required=True)
    parser.add_argument("--test_path", type=Path, required=True)
    parser.add_argument("--output_dir", type=Path, required=True)
    parser.add_argument("--validation_ratio", type=float, default=0.05)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--effective_batch_size", type=int, default=8)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not 0 < args.validation_ratio < 0.5:
        raise ValueError("validation_ratio must be between 0 and 0.5")
    if args.output_dir.exists():
        raise FileExistsError(f"Refusing to overwrite output directory: {args.output_dir}")
    input_paths = [args.train_path.resolve(), args.validation_path.resolve(), args.test_path.resolve()]
    output_resolved = args.output_dir.resolve()
    if any(output_resolved == path or output_resolved in path.parents for path in input_paths):
        raise ValueError("Output directory must not contain or replace an input file")

    original_hashes = {str(path): sha256(path) for path in input_paths}
    rows = read_jsonl(args.train_path) + read_jsonl(args.validation_path)
    all_questions = [normalize(qa(row)[0]) for row in rows]
    if len(all_questions) != len(set(all_questions)):
        raise ValueError("Input train+validation pool contains duplicate questions")
    train, validation = grouped_stratified_split(rows, args.validation_ratio, args.seed)
    train_facts = {fact_group_key(row) for row in train}
    validation_facts = {fact_group_key(row) for row in validation}
    train_questions = {normalize(qa(row)[0]) for row in train}
    validation_questions = {normalize(qa(row)[0]) for row in validation}

    args.output_dir.mkdir(parents=True)
    train_out = args.output_dir / "train_chat_stratified.jsonl"
    validation_out = args.output_dir / "val_chat_stratified.jsonl"
    write_jsonl(train_out, train)
    write_jsonl(validation_out, validation)
    # Transformers 4.57 computes update steps per epoch with floor division.
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
        "epoch_checkpoint_steps": [steps_per_epoch, steps_per_epoch * 2, steps_per_epoch * 3],
        "validation": {
            "exact_question_overlap": len(train_questions & validation_questions),
            "fact_group_overlap": len(train_facts & validation_facts),
            "train_duplicate_questions": duplicate_question_count(train),
            "validation_duplicate_questions": duplicate_question_count(validation),
            "max_distribution_delta": {
                field: max_percentage_delta(rows, validation, field)
                for field in ("data_family", "source_type", "switch", "version")
            },
        },
        "counts": {
            "train_by_data_family": dict(sorted(distribution(train, "data_family").items())),
            "validation_by_data_family": dict(sorted(distribution(validation, "data_family").items())),
            "train_by_source_type": dict(sorted(distribution(train, "source_type").items())),
            "validation_by_source_type": dict(sorted(distribution(validation, "source_type").items())),
        },
        "files": {
            "inputs": {path: {"sha256": digest} for path, digest in original_hashes.items()},
            "train": {"path": str(train_out), "sha256": sha256(train_out)},
            "validation": {"path": str(validation_out), "sha256": sha256(validation_out)},
            "untouched_test": {"path": str(args.test_path), "sha256": sha256(args.test_path)},
        },
    }
    if any(report["validation"][key] for key in ("exact_question_overlap", "fact_group_overlap", "train_duplicate_questions", "validation_duplicate_questions")):
        raise RuntimeError(f"Split validation failed: {report['validation']}")
    if original_hashes[str(args.test_path.resolve())] != sha256(args.test_path):
        raise RuntimeError("Test dataset changed while building the split")
    (args.output_dir / "manifest.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
