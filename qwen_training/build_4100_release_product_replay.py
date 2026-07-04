#!/usr/bin/env python3
"""Build a 4100/4100i release + product replay dataset and strict holdout."""

from __future__ import annotations

import argparse
import json
import re
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


DEFAULT_TRAIN = Path("Data/all_switches/train_chat_all_clean_validated.jsonl")
DEFAULT_VAL = Path("Data/all_switches/val_chat_all_clean.jsonl")
DEFAULT_SHORT = Path("Data/all_switches/release_notes_only_structured_short_train.jsonl")
DEFAULT_OUTPUT_DIR = Path("Data/all_switches")
DEFAULT_HOLDOUT = DEFAULT_OUTPUT_DIR / "strict_holdout_4100_release_product.jsonl"
DEFAULT_REPORT = DEFAULT_OUTPUT_DIR / "report_4100_release_product_replay.json"
DEFAULT_TRAIN_OUT = DEFAULT_OUTPUT_DIR / "train_4100_release_product_replay.jsonl"
DEFAULT_VAL_OUT = DEFAULT_OUTPUT_DIR / "val_4100_release_product_replay.jsonl"

UNRELATED_ONLY_SWITCHES = {
    "5420",
    "6100",
    "6200",
    "6300",
    "6400",
    "8100",
    "8320",
    "8325",
    "8400",
    "9300",
}

PRODUCT_SOURCE_TYPES = {
    "product_cli_reference",
    "product_fundamentals",
    "product_ip_routing",
    "product_ip_services",
    "product_link_aggregation",
    "product_monitoring",
    "product_diagnostics_supportability",
    "product_high_availability",
    "product_event_log_reference",
    "product_web_ui",
    "product_snmp_mib_reference",
    "product_security",
    "product_rest_api",
    "product_acls_classifier",
    "product_multicast",
    "product_telemetry",
    "configuration_procedure",
    "concept_explanation",
    "feature_limitation",
    "routing_feature",
    "monitoring_feature",
    "troubleshooting",
    "security_policy",
    "web_ui_task",
    "rest_api_reference",
    "snmp_mib_reference",
}

MIXED_SERIES_HINTS = (
    "4100i/6000/6100",
    "4100i/5420/6000/6100/6200",
    "4100 switch series",
    "all switch series",
    "4100i, 5420, 6000, 6100, 6200",
    "4100i 6000 6100",
    "4100i 5420 6000 6100 6200",
)

RELEASE_SELECTOR_ORDER = [
    "release_notes_bug",
    "release_notes_generic",
    "release_notes_supported_products",
    "release_notes_version_history",
    "release_notes_certifications",
]

HOLDOUT_SELECTORS: List[Tuple[str, int, Any]] = [
    ("release_notes_bug", 24, lambda row: normalize(row.get("data_family")) == "release_notes_bug"),
    ("release_notes_generic", 16, lambda row: normalize(row.get("data_family")) == "release_notes_generic"),
    (
        "release_notes_product",
        10,
        lambda row: normalize(row.get("source_type"))
        in {"release_notes_supported_products", "release_notes_version_history", "release_notes_certifications"},
    ),
    (
        "cli_reference",
        20,
        lambda row: normalize(row.get("data_family")) in {"cli_command_reference", "show_command_reference"}
        or normalize(row.get("source_type")) in {"product_cli_reference", "product_ip_routing"},
    ),
    (
        "event_reference",
        10,
        lambda row: normalize(row.get("data_family")) == "event_log_reference"
        or normalize(row.get("source_type")) == "product_event_log_reference",
    ),
    (
        "product_procedure",
        10,
        lambda row: normalize(row.get("source_type"))
        in {"product_fundamentals", "configuration_procedure", "concept_explanation", "troubleshooting", "feature_limitation"},
    ),
    (
        "product_misc",
        10,
        lambda row: normalize(row.get("source_type"))
        in {
            "product_ip_services",
            "product_ip_routing",
            "product_link_aggregation",
            "product_monitoring",
            "product_web_ui",
            "product_snmp_mib_reference",
            "product_high_availability",
            "product_security",
            "product_rest_api",
            "product_diagnostics_supportability",
            "product_acls_classifier",
            "product_multicast",
        },
    ),
]


def normalize_text(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()


def row_text(row: Dict[str, Any]) -> str:
    parts = [
        row.get("switch", ""),
        row.get("version", ""),
        row.get("sub_version", ""),
        row.get("source_type", ""),
        row.get("data_family", ""),
        row.get("document_title", ""),
        row.get("section", ""),
        row.get("topic", ""),
        row.get("source_file", ""),
    ]
    for message in row.get("messages") or []:
        parts.append(message.get("content", ""))
    return " | ".join(normalize_text(part) for part in parts if normalize_text(part))


def has_4100(row: Dict[str, Any]) -> bool:
    return bool(re.search(r"\b4100i?\b", row_text(row), flags=re.IGNORECASE))


def is_mixed_shared(row: Dict[str, Any]) -> bool:
    text = row_text(row).lower()
    if not has_4100(row):
        return False
    if any(hint in text for hint in MIXED_SERIES_HINTS):
        return True
    other_switches = any(re.search(rf"\b{switch}\b", text) for switch in UNRELATED_ONLY_SWITCHES)
    return other_switches and "4100" in text


def is_release_note(row: Dict[str, Any]) -> bool:
    family = normalize(row.get("data_family"))
    source_type = normalize(row.get("source_type"))
    return family.startswith("release_notes_") or source_type.startswith("release_notes_")


def is_product_doc(row: Dict[str, Any]) -> bool:
    family = normalize(row.get("data_family"))
    source_type = normalize(row.get("source_type"))
    return source_type.startswith("product_") or family in {
        "cli_command_reference",
        "show_command_reference",
        "event_log_reference",
        "snmp_mib_reference",
        "configuration_procedure",
        "concept_explanation",
        "feature_limitation",
        "routing_feature",
        "monitoring_feature",
        "troubleshooting",
        "security_policy",
        "web_ui_task",
        "rest_api_reference",
    }


def is_short_release(row: Dict[str, Any], source_path: Path) -> bool:
    data_family = normalize(row.get("data_family"))
    source_type = normalize(row.get("source_type"))
    if data_family.startswith("release_notes_only_structured_short_") or source_type.startswith("release_notes_only_structured_short_"):
        return True
    return source_path.name == DEFAULT_SHORT.name and has_4100(row)


def is_relevant_row(row: Dict[str, Any], source_path: Path) -> bool:
    if is_short_release(row, source_path):
        return True
    if not has_4100(row):
        return False
    switch = normalize(row.get("switch"))
    if switch in UNRELATED_ONLY_SWITCHES and not has_4100(row):
        return False
    if is_release_note(row):
        return True
    if is_mixed_shared(row):
        return True
    if is_product_doc(row):
        return True
    return False


def bucket(row: Dict[str, Any], source_path: Path) -> str:
    if is_short_release(row, source_path):
        return "short_release_notes"
    if is_release_note(row):
        return "release_notes"
    if is_mixed_shared(row):
        return "shared_replay"
    if is_product_doc(row):
        return "product_docs"
    return "other"


def bucket_row(row: Dict[str, Any]) -> str:
    data_family = normalize(row.get("data_family"))
    source_type = normalize(row.get("source_type"))
    if data_family.startswith("release_notes_only_structured_short_") or source_type.startswith("release_notes_only_structured_short_"):
        return "short_release_notes"
    if data_family.startswith("release_notes_") or source_type.startswith("release_notes_"):
        return "release_notes"
    if is_mixed_shared(row):
        return "shared_replay"
    if is_product_doc(row):
        return "product_docs"
    return "other"


def qa_pair(row: Dict[str, Any]) -> Tuple[str, str]:
    return qa(row)


def load_rows(paths: Sequence[Path]) -> List[Tuple[Path, Dict[str, Any]]]:
    rows: List[Tuple[Path, Dict[str, Any]]] = []
    for path in paths:
        for row in read_jsonl(path):
            rows.append((path, row))
    return rows


def select_unique_rows(
    rows: Sequence[Tuple[Path, Dict[str, Any]]],
    count: int,
    used_questions: set[str],
    used_facts: set[str],
    source_filter: Any = None,
) -> List[Dict[str, Any]]:
    selected: List[Dict[str, Any]] = []
    for source_path, row in rows:
        if source_filter is not None and not source_filter(source_path, row):
            continue
        question, answer = qa_pair(row)
        fact = fact_group_key(row)
        if not question or not answer:
            continue
        qkey = normalize(question)
        if qkey in used_questions or fact in used_facts:
            continue
        used_questions.add(qkey)
        used_facts.add(fact)
        selected.append(row)
        if len(selected) >= count:
            break
    return selected


def build_holdout(rows: Sequence[Tuple[Path, Dict[str, Any]]]) -> List[Dict[str, Any]]:
    holdout: List[Dict[str, Any]] = []
    used_questions: set[str] = set()
    used_facts: set[str] = set()
    for label, quota, predicate in HOLDOUT_SELECTORS:
        pool = [(path, row) for path, row in rows if not is_short_release(row, path) and predicate(row)]
        holdout.extend(select_unique_rows(pool, quota, used_questions, used_facts))

    if len(holdout) < 100:
        fallback_pool = [(path, row) for path, row in rows if not is_short_release(row, path)]
        holdout.extend(select_unique_rows(fallback_pool, 100 - len(holdout), used_questions, used_facts))

    if len(holdout) != 100:
        raise RuntimeError(f"Holdout size is {len(holdout)}, expected 100")
    return holdout


def sample_rows(rows: Sequence[Dict[str, Any]], predicate: Any, count: int) -> List[Dict[str, Any]]:
    result: List[Dict[str, Any]] = []
    used: set[str] = set()
    for row in rows:
        if not predicate(row):
            continue
        question, answer = qa_pair(row)
        qkey = normalize(question)
        if qkey in used:
            continue
        used.add(qkey)
        result.append(row)
        if len(result) >= count:
            break
    return result


def format_row(row: Dict[str, Any]) -> str:
    question, answer = qa_pair(row)
    return (
        f"- bucket={bucket_row(row)} | switch={row.get('switch')} | "
        f"family={row.get('data_family')} | source_type={row.get('source_type')}\n"
        f"  Q: {question}\n"
        f"  A: {answer}"
    )


def build_report(
    source_rows: Sequence[Tuple[Path, Dict[str, Any]]],
    train_rows: Sequence[Dict[str, Any]],
    val_rows: Sequence[Dict[str, Any]],
    holdout_rows: Sequence[Dict[str, Any]],
    rejected_count: int,
    duplicate_count: int,
    conflict_count: int,
    input_paths: Sequence[Path],
    output_dir: Path,
) -> Dict[str, Any]:
    selected_rows = list(train_rows) + list(val_rows)
    selected_bucket_counts = Counter(bucket_row(row) for row in selected_rows)
    held_bucket_counts = Counter(bucket_row(row) for row in holdout_rows)
    rel = selected_bucket_counts["release_notes"]
    prod = selected_bucket_counts["product_docs"]
    shared = selected_bucket_counts["shared_replay"]
    short = selected_bucket_counts["short_release_notes"]
    total_selected = len(selected_rows)
    ratios = {
        "release_notes": round(rel / total_selected, 6) if total_selected else 0.0,
        "product_docs": round(prod / total_selected, 6) if total_selected else 0.0,
        "shared_replay": round(shared / total_selected, 6) if total_selected else 0.0,
        "short_release_notes": round(short / total_selected, 6) if total_selected else 0.0,
    }
    report = {
        "input_rows_scanned": len(source_rows),
        "selected_rows_before_split": total_selected,
        "train_rows": len(train_rows),
        "val_rows": len(val_rows),
        "holdout_rows": len(holdout_rows),
        "bucket_counts_before_split": dict(sorted(selected_bucket_counts.items())),
        "holdout_bucket_counts": dict(sorted(held_bucket_counts.items())),
        "data_family_counts_before_split": dict(sorted(distribution(selected_rows, "data_family").items())),
        "source_type_counts_before_split": dict(sorted(distribution(selected_rows, "source_type").items())),
        "release_product_shared_short_ratios": ratios,
        "release_product_ratio": round(rel / prod, 6) if prod else None,
        "duplicates_removed": duplicate_count,
        "conflicts_found": conflict_count,
        "rows_rejected": rejected_count,
        "split_distribution": {
            "train": {
                "data_family": dict(sorted(distribution(train_rows, "data_family").items())),
                "source_type": dict(sorted(distribution(train_rows, "source_type").items())),
            },
            "val": {
                "data_family": dict(sorted(distribution(val_rows, "data_family").items())),
                "source_type": dict(sorted(distribution(val_rows, "source_type").items())),
            },
            "holdout": {
                "data_family": dict(sorted(distribution(holdout_rows, "data_family").items())),
                "source_type": dict(sorted(distribution(holdout_rows, "source_type").items())),
            },
        },
        "overlap_checks": {
            "train_val_exact_question_overlap": len({normalize(qa_pair(row)[0]) for row in train_rows} & {normalize(qa_pair(row)[0]) for row in val_rows}),
            "train_holdout_exact_question_overlap": len({normalize(qa_pair(row)[0]) for row in train_rows} & {normalize(qa_pair(row)[0]) for row in holdout_rows}),
            "val_holdout_exact_question_overlap": len({normalize(qa_pair(row)[0]) for row in val_rows} & {normalize(qa_pair(row)[0]) for row in holdout_rows}),
            "train_val_fact_group_overlap": len({fact_group_key(row) for row in train_rows} & {fact_group_key(row) for row in val_rows}),
            "train_holdout_fact_group_overlap": len({fact_group_key(row) for row in train_rows} & {fact_group_key(row) for row in holdout_rows}),
            "val_holdout_fact_group_overlap": len({fact_group_key(row) for row in val_rows} & {fact_group_key(row) for row in holdout_rows}),
            "train_duplicate_questions": duplicate_question_count(train_rows),
            "val_duplicate_questions": duplicate_question_count(val_rows),
            "holdout_duplicate_questions": duplicate_question_count(holdout_rows),
            "max_distribution_delta_val": {
                field: max_percentage_delta(selected_rows, val_rows, field)
                for field in ("data_family", "source_type", "switch", "version", "sub_version")
            },
            "max_distribution_delta_holdout": {
                field: max_percentage_delta(selected_rows, holdout_rows, field)
                for field in ("data_family", "source_type", "switch", "version", "sub_version")
            },
        },
        "files": {
            "inputs": {
                str(path.resolve()): {"sha256": sha256(path)}
                for path in input_paths
            },
            "train": {
                "path": str((output_dir / DEFAULT_TRAIN_OUT.name).resolve()),
                "sha256": sha256(output_dir / DEFAULT_TRAIN_OUT.name),
            },
            "val": {
                "path": str((output_dir / DEFAULT_VAL_OUT.name).resolve()),
                "sha256": sha256(output_dir / DEFAULT_VAL_OUT.name),
            },
            "holdout": {
                "path": str((output_dir / DEFAULT_HOLDOUT.name).resolve()),
                "sha256": sha256(output_dir / DEFAULT_HOLDOUT.name),
            },
        },
        "notes": [
            "4100/4100i rows were selected from the cleaned global train/val pool plus the structured short release-note file.",
            "The strict holdout is disjoint from the train/val split by fact-group and question.",
            "Shared replay rows are mixed-series Aruba docs that explicitly include 4100/4100i.",
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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--train_path", type=Path, default=DEFAULT_TRAIN)
    parser.add_argument("--val_path", type=Path, default=DEFAULT_VAL)
    parser.add_argument("--short_path", type=Path, default=DEFAULT_SHORT)
    parser.add_argument("--output_dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--validation_ratio", type=float, default=0.05)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--overwrite", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not 0 < args.validation_ratio < 0.5:
        raise ValueError("validation_ratio must be between 0 and 0.5")
    args.output_dir.mkdir(parents=True, exist_ok=True)

    train_rows = read_jsonl(args.train_path)
    val_rows = read_jsonl(args.val_path)
    short_rows = read_jsonl(args.short_path)
    all_rows: List[Tuple[Path, Dict[str, Any]]] = []
    all_rows.extend((args.train_path, row) for row in train_rows)
    all_rows.extend((args.val_path, row) for row in val_rows)
    all_rows.extend((args.short_path, row) for row in short_rows)

    scanned = len(train_rows) + len(val_rows) + len(short_rows)
    eligible = [(path, row) for path, row in all_rows if is_relevant_row(row, path)]
    if not eligible:
        raise RuntimeError("No 4100/4100i rows matched the selection rules")

    rejected_count = scanned - len(eligible)
    seen_questions: Dict[str, str] = {}
    seen_qas: set[Tuple[str, str]] = set()
    deduped: List[Tuple[Path, Dict[str, Any]]] = []
    duplicate_count = 0
    conflict_count = 0
    for source_path, row in eligible:
        question, answer = qa_pair(row)
        qkey = normalize(question)
        pair = (qkey, normalize(answer))
        if not question or not answer:
            continue
        if pair in seen_qas:
            duplicate_count += 1
            continue
        if qkey in seen_questions and seen_questions[qkey] != normalize(answer):
            conflict_count += 1
            continue
        seen_questions[qkey] = normalize(answer)
        seen_qas.add(pair)
        deduped.append((source_path, row))

    holdout = build_holdout([(path, row) for path, row in deduped if path != args.short_path])
    holdout_questions = {normalize(qa_pair(row)[0]) for row in holdout}
    holdout_facts = {fact_group_key(row) for row in holdout}
    remaining = [
        row
        for path, row in deduped
        if normalize(qa_pair(row)[0]) not in holdout_questions and fact_group_key(row) not in holdout_facts
    ]

    train_split, val_split = grouped_stratified_split(remaining, args.validation_ratio, args.seed)

    train_out = args.output_dir / DEFAULT_TRAIN_OUT.name
    val_out = args.output_dir / DEFAULT_VAL_OUT.name
    holdout_out = args.output_dir / DEFAULT_HOLDOUT.name
    report_out = args.output_dir / DEFAULT_REPORT.name
    if not args.overwrite:
        for path in (train_out, val_out, holdout_out, report_out):
            if path.exists():
                raise FileExistsError(f"Refusing to overwrite existing file: {path}")

    write_jsonl(train_out, train_split)
    write_jsonl(val_out, val_split)
    write_jsonl(holdout_out, holdout)

    report = build_report(
        deduped,
        train_split,
        val_split,
        holdout,
        rejected_count,
        duplicate_count,
        conflict_count,
        [args.train_path, args.val_path, args.short_path],
        args.output_dir,
    )
    report_out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    selected_rows = list(train_split) + list(val_split)
    selected_counts = Counter(bucket_row(row) for row in selected_rows)
    release_count = selected_counts["release_notes"]
    product_count = selected_counts["product_docs"]
    shared_count = selected_counts["shared_replay"]
    short_count = selected_counts["short_release_notes"]

    print(f"[DATA] total source rows scanned: {scanned}")
    print(f"[DATA] 4100/4100i release rows selected: {selected_counts['release_notes']}")
    print(f"[DATA] 4100/4100i product rows selected: {selected_counts['product_docs']}")
    print(f"[DATA] shared replay rows selected: {selected_counts['shared_replay']}")
    print(f"[DATA] structured short rows selected: {selected_counts['short_release_notes']}")
    print(f"[DATA] final train rows: {len(train_split)}")
    print(f"[DATA] final val rows: {len(val_split)}")
    print("[DISTRIBUTION] data_family counts:")
    print(json.dumps(dict(sorted(distribution(selected_rows, "data_family").items())), indent=2, ensure_ascii=False))
    print("[DISTRIBUTION] source_type counts:")
    print(json.dumps(dict(sorted(distribution(selected_rows, "source_type").items())), indent=2, ensure_ascii=False))
    print(
        "[DISTRIBUTION] release/product ratio: "
        f"{release_count}/{product_count} = {round((release_count / product_count), 6) if product_count else 'inf'}"
    )
    print(f"[QUALITY] duplicates removed: {duplicate_count}")
    print(f"[QUALITY] conflicts found: {conflict_count}")
    print(f"[QUALITY] rows rejected: {rejected_count}")

    print("[SAMPLES] show 5 release-note rows")
    for row in sample_rows(selected_rows, lambda r: bucket_row(r) == "release_notes", 5):
        print(format_row(row))
    print("[SAMPLES] show 5 product rows")
    for row in sample_rows(selected_rows, lambda r: bucket_row(r) == "product_docs", 5):
        print(format_row(row))
    print("[SAMPLES] show 5 CLI rows")
    for row in sample_rows(
        selected_rows,
        lambda r: normalize(r.get("data_family")) in {"cli_command_reference", "show_command_reference"}
        or normalize(r.get("source_type")) in {"product_cli_reference", "product_ip_routing"},
        5,
    ):
        print(format_row(row))
    print("[SAMPLES] show 5 no-workaround/version-history rows")
    for row in sample_rows(
        selected_rows,
        lambda r: (
            "no workaround" in row_text(r).lower()
            or normalize(r.get("source_type")) == "release_notes_version_history"
            or "version history" in row_text(r).lower()
        ),
        5,
    ):
        print(format_row(row))

    print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
