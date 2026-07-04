"""End-to-end pipeline: HTML -> cleaned JSON -> QA -> augmentation -> chat JSONL."""

from __future__ import annotations

import argparse
import json
import logging
import re
import shutil
from pathlib import Path
from typing import Any, Dict, List, Sequence, Tuple

from dotenv import load_dotenv

try:
    from .augmenter import AugmentationConfig, DataAugmenter
    from .formatter import (
        build_rich_dataset,
        extract_issue_metadata,
        enforce_quality_rules,
        dedupe_chat_transcripts,
        has_issue_markers,
        recover_issue_metadata,
        save_json as save_formatter_json,
        write_chat_jsonl,
    )
    from .parser import parse_html_directory, save_json as save_parser_json
    from .qa_generator import LLMConfig, QAGenerator
except ImportError:  # pragma: no cover
    from augmenter import AugmentationConfig, DataAugmenter
    from formatter import (
        build_rich_dataset,
        extract_issue_metadata,
        enforce_quality_rules,
        dedupe_chat_transcripts,
        has_issue_markers,
        recover_issue_metadata,
        save_json as save_formatter_json,
        write_chat_jsonl,
    )
    from parser import parse_html_directory, save_json as save_parser_json
    from qa_generator import LLMConfig, QAGenerator

LOGGER = logging.getLogger(__name__)
BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_PATH_ATTRS = (
    "cleaned_json",
    "qa_json",
    "augmented_json",
    "negative_json",
    "multiturn_json",
    "rich_json",
    "final_jsonl",
    "quality_report_json",
)
FULL_RELEASE_RE = re.compile(r"\b10[._](\d{2})[._](\d{4})\b", re.IGNORECASE)
BRANCH_RELEASE_RE = re.compile(r"\b10[._](\d{2})\b", re.IGNORECASE)
RELEASE_SECTION_RE = re.compile(
    r"(?:for\s+[^|]*?\s+in\s+aos-cx|aos-cx)\s*10[._](\d{2})(?:[._](\d{4}))?",
    re.IGNORECASE,
)


def _path(value: str) -> Path:
    return Path(value).expanduser().resolve()


def _slugify_switch_name(value: str) -> str:
    cleaned = re.sub(r"[^a-z0-9._-]+", "_", value.strip().lower())
    cleaned = cleaned.strip("._-")
    return cleaned or "switch"


def _with_suffix(path: Path, suffix: str) -> Path:
    suffixes = "".join(path.suffixes)
    stem = path.name[: -len(suffixes)] if suffixes else path.name
    if stem.lower().endswith(f"_{suffix.lower()}"):
        return path
    return path.with_name(f"{stem}_{suffix}{suffixes}")


def _apply_switch_suffix(args: argparse.Namespace) -> str:
    if not args.switch_name:
        return ""
    switch_key = _slugify_switch_name(args.switch_name)
    for attr in OUTPUT_PATH_ATTRS:
        setattr(args, attr, _with_suffix(getattr(args, attr), switch_key))
    args.switch_name = switch_key
    return switch_key


def _load_json_records(path: Path) -> List[Dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError(f"Expected a JSON array in {path}")

    records: List[Dict[str, Any]] = []
    for index, record in enumerate(data):
        if not isinstance(record, dict):
            raise ValueError(
                f"Expected object records in {path}, got {type(record).__name__} at index {index}"
            )
        records.append(record)
    return records


def _extract_message_content(messages: Sequence[Dict[str, Any]], role: str) -> str:
    wanted_role = role.lower().strip()
    for message in messages:
        if not isinstance(message, dict):
            continue
        message_role = str(message.get("role", "")).strip().lower()
        if message_role != wanted_role:
            continue
        content = str(message.get("content", "")).strip()
        if content:
            return content
    return ""


def _normalize_release_text(value: str) -> str:
    collapsed = re.sub(r"\s+", " ", value.strip())
    return re.sub(r"\s*([._])\s*", r"\1", collapsed)


def _format_version_token(major_minor: str) -> str:
    return f"10_{major_minor}"


def _extract_release_tokens(text: str) -> Tuple[str, str]:
    if not text:
        return "", ""

    normalized = _normalize_release_text(text)
    header = normalized.split("|", 1)[0]
    for candidate in (header, normalized):
        section_match = RELEASE_SECTION_RE.search(candidate)
        if section_match:
            major_minor = section_match.group(1)
            sub_version = section_match.group(2) or ""
            return _format_version_token(major_minor), sub_version

        full_match = FULL_RELEASE_RE.search(candidate)
        if full_match:
            major_minor, sub_version = full_match.group(1), full_match.group(2)
            return _format_version_token(major_minor), sub_version

        branch_match = BRANCH_RELEASE_RE.search(candidate)
        if branch_match:
            return _format_version_token(branch_match.group(1)), ""
    return "", ""


def _infer_switch_name(configured_switch: str, input_dir: Path) -> str:
    switch = configured_switch.strip().lower()
    if switch:
        return switch
    match = re.search(r"aruba_(.+?)_html_content", input_dir.name.lower())
    if match:
        return _slugify_switch_name(match.group(1))
    inferred = _slugify_switch_name(input_dir.name)
    return inferred if inferred != "switch" else "unknown"


def _annotate_export_metadata(
    records: Sequence[Dict[str, Any]],
    switch_name: str,
    input_dir: Path,
) -> List[Dict[str, Any]]:
    resolved_switch = _infer_switch_name(switch_name, input_dir)
    annotated: List[Dict[str, Any]] = []

    for record in records:
        version = str(record.get("version", "")).strip()
        sub_version = str(record.get("sub_version", "")).strip()
        for candidate in (
            str(record.get("source_path", "")),
            str(record.get("context", "")),
            str(record.get("source", "")),
            str(record.get("question", "")),
            str(record.get("answer", "")),
        ):
            if version and sub_version:
                break
            detected_version, detected_sub_version = _extract_release_tokens(candidate)
            if not detected_version:
                continue
            if not version:
                version = detected_version
            if detected_version == version and detected_sub_version and not sub_version:
                sub_version = detected_sub_version

        annotated.append(
            {
                **record,
                "switch": resolved_switch,
                "version": version,
                "sub_version": sub_version,
            }
        )

    bug_to_release: Dict[str, set] = {}
    for record in annotated:
        bug_id = str(record.get("bug_id", "")).strip()
        version = str(record.get("version", "")).strip()
        sub_version = str(record.get("sub_version", "")).strip()
        if bug_id and version:
            bug_to_release.setdefault(bug_id, set()).add((version, sub_version))

    for record in annotated:
        version = str(record.get("version", "")).strip()
        if version:
            continue
        bug_id = str(record.get("bug_id", "")).strip()
        candidates = bug_to_release.get(bug_id, set())
        if len(candidates) != 1:
            continue
        inferred_version, inferred_sub_version = next(iter(candidates))
        record["version"] = inferred_version
        if inferred_sub_version:
            record["sub_version"] = inferred_sub_version

    unique_sub_versions_by_version: Dict[str, set] = {}
    for record in annotated:
        version = str(record.get("version", "")).strip()
        sub_version = str(record.get("sub_version", "")).strip()
        if version and sub_version:
            unique_sub_versions_by_version.setdefault(version, set()).add(sub_version)

    for record in annotated:
        version = str(record.get("version", "")).strip()
        sub_version = str(record.get("sub_version", "")).strip()
        if version and not sub_version:
            candidates = unique_sub_versions_by_version.get(version, set())
            if len(candidates) == 1:
                record["sub_version"] = next(iter(candidates))

        record["version"] = str(record.get("version", "")).strip() or "unknown"
        record["sub_version"] = str(record.get("sub_version", "")).strip() or "unknown"

    return annotated


def _organized_final_json_root(final_jsonl_path: Path) -> Path:
    parent = final_jsonl_path.parent
    if parent.name.lower() == "final_jsonl":
        return parent.parent / "final_json"
    return parent / "final_json"


def _release_tree_path(template_path: Path, switch_name: str, version: str, sub_version: str) -> Path:
    return template_path.parent / (switch_name or "unknown") / version / sub_version / template_path.name


def _group_records_by_release_pairs(records: Sequence[Dict[str, Any]]) -> Dict[Tuple[str, str], List[Dict[str, Any]]]:
    grouped: Dict[Tuple[str, str], List[Dict[str, Any]]] = {}
    for record in records:
        version = str(record.get("version", "unknown")).strip() or "unknown"
        sub_version = str(record.get("sub_version", "unknown")).strip() or "unknown"
        grouped.setdefault((version, sub_version), []).append(record)
    return grouped


def _save_release_tree_json(
    records: Sequence[Dict[str, Any]],
    output_path: Path,
    switch_name: str,
) -> Dict[str, Dict[str, int]]:
    grouped = _group_records_by_release_pairs(records)
    counts: Dict[str, Dict[str, int]] = {}
    for (version, sub_version), grouped_records in sorted(grouped.items()):
        tree_path = _release_tree_path(output_path, switch_name, version, sub_version)
        save_formatter_json(grouped_records, tree_path)
        counts.setdefault(version, {})[sub_version] = len(grouped_records)
    return counts


def _write_version_subversion_partitioned_jsonl(
    records: Sequence[Dict[str, Any]],
    switch_name: str,
    final_jsonl_path: Path,
) -> Dict[str, Dict[str, int]]:
    root_dir = _organized_final_json_root(final_jsonl_path)
    switch_dir = root_dir / (switch_name or "unknown")
    if switch_dir.exists():
        shutil.rmtree(switch_dir, ignore_errors=True)
    switch_dir.mkdir(parents=True, exist_ok=True)

    grouped = _group_records_by_release(records)
    counts_by_release: Dict[str, Dict[str, int]] = {}
    for version in sorted(grouped):
        counts_by_release[version] = {}
        for sub_version in sorted(grouped[version]):
            grouped_records = grouped[version][sub_version]
            output_path = switch_dir / version / sub_version / "train_chat.jsonl"
            counts_by_release[version][sub_version] = write_chat_jsonl(grouped_records, output_path)
    LOGGER.info("Saved organized final JSONL by version/sub-version under %s", switch_dir)
    return counts_by_release


def _organized_release_json_root(output_path: Path) -> Path:
    return output_path.parent / "by_release"


def _group_records_by_release(records: Sequence[Dict[str, Any]]) -> Dict[str, Dict[str, List[Dict[str, Any]]]]:
    grouped: Dict[str, Dict[str, List[Dict[str, Any]]]] = {}
    for record in records:
        version = str(record.get("version", "unknown")).strip() or "unknown"
        sub_version = str(record.get("sub_version", "unknown")).strip() or "unknown"
        grouped.setdefault(version, {}).setdefault(sub_version, []).append(record)
    return grouped


def _write_release_partitioned_json(
    records: Sequence[Dict[str, Any]],
    switch_name: str,
    output_path: Path,
) -> Dict[str, Dict[str, int]]:
    root_dir = _organized_release_json_root(output_path)
    switch_dir = root_dir / (switch_name or "unknown")
    switch_dir.mkdir(parents=True, exist_ok=True)
    grouped = _group_records_by_release(records)

    keep_versions = set(grouped.keys())
    for existing_dir in switch_dir.iterdir():
        if not existing_dir.is_dir():
            continue
        if existing_dir.name in keep_versions:
            keep_sub_versions = set(grouped[existing_dir.name].keys())
            for sub_dir in existing_dir.iterdir():
                if not sub_dir.is_dir():
                    continue
                if sub_dir.name in keep_sub_versions:
                    continue
                shutil.rmtree(sub_dir, ignore_errors=True)
            continue
        shutil.rmtree(existing_dir, ignore_errors=True)

    counts_by_version: Dict[str, Dict[str, int]] = {}
    for version in sorted(grouped):
        counts_by_version[version] = {}
        for sub_version in sorted(grouped[version]):
            target_path = switch_dir / version / sub_version / output_path.name
            target_path.parent.mkdir(parents=True, exist_ok=True)
            target_path.write_text(
                json.dumps(grouped[version][sub_version], indent=2, ensure_ascii=False),
                encoding="utf-8",
            )
            counts_by_version[version][sub_version] = len(grouped[version][sub_version])

    LOGGER.info("Saved organized JSON tree by version/sub-version under %s", switch_dir)
    return counts_by_version


def _write_version_partitioned_jsonl(
    records: Sequence[Dict[str, Any]],
    switch_name: str,
    final_jsonl_path: Path,
) -> Dict[str, Dict[str, int]]:
    root_dir = _organized_final_json_root(final_jsonl_path)
    switch_dir = root_dir / (switch_name or "unknown")
    switch_dir.mkdir(parents=True, exist_ok=True)
    grouped = _group_records_by_release(records)

    keep_versions = set(grouped.keys())
    for existing_dir in switch_dir.iterdir():
        if not existing_dir.is_dir():
            continue
        if existing_dir.name in keep_versions:
            keep_sub_versions = set(grouped[existing_dir.name].keys())
            for sub_dir in existing_dir.iterdir():
                if not sub_dir.is_dir():
                    continue
                if sub_dir.name in keep_sub_versions:
                    continue
                shutil.rmtree(sub_dir, ignore_errors=True)
            continue
        shutil.rmtree(existing_dir, ignore_errors=True)

    counts_by_version: Dict[str, Dict[str, int]] = {}
    for version in sorted(grouped):
        counts_by_version[version] = {}
        for sub_version in sorted(grouped[version]):
            output_path = switch_dir / version / sub_version / "train_chat.jsonl"
            counts_by_version[version][sub_version] = write_chat_jsonl(grouped[version][sub_version], output_path)
    LOGGER.info("Saved organized final JSONL by version/sub-version under %s", switch_dir)
    return counts_by_version


def _infer_artifact_root_from_checkpoint(checkpoint: Path) -> Path:
    """Infer the run root from a checkpoint path when resuming in repair-only mode."""
    resolved = checkpoint.expanduser().resolve()
    for parent in resolved.parents:
        if parent.name.lower() in {"processed_json", "augmented", "final_jsonl", "final_json"}:
            return parent.parent
    return resolved.parent


def _repair_issue_style_records(
    records: Sequence[Dict[str, Any]],
    switch_name: str,
) -> Tuple[List[Dict[str, Any]], Dict[str, int]]:
    repaired: List[Dict[str, Any]] = []
    stats = {
        "repair_input_records": len(records),
        "repaired_records": 0,
        "dropped_records": 0,
        "recovered_category_count": 0,
        "recovered_bug_id_count": 0,
        "records_with_metadata_source": 0,
    }

    for record in records:
        source_texts = [
            str(record.get("context", "")),
            str(record.get("answer", "")),
            str(record.get("question", "")),
            str(record.get("title", "")),
            str(record.get("issue_description", "")),
            str(record.get("description", "")),
            str(record.get("summary", "")),
            str(record.get("metadata", "")),
            str(record.get("source", "")),
            str(record.get("source_path", "")),
        ]
        if any(text.strip() for text in source_texts):
            stats["records_with_metadata_source"] += 1

        original_category = str(record.get("category_name", "")).strip()
        original_bug_id = str(record.get("bug_id", "")).strip()
        recovered = recover_issue_metadata(record)
        category_name = recovered["category_name"].strip()
        bug_id = recovered["bug_id"].strip()

        if not category_name and not bug_id and not any(text.strip() for text in source_texts):
            stats["dropped_records"] += 1
            continue

        repaired.append(
            {
                **record,
                "category_name": category_name or original_category,
                "bug_id": bug_id or original_bug_id,
                "source_type": recovered["source_type"],
                "switch": switch_name,
            }
        )
        stats["repaired_records"] += 1
        if not original_category and category_name:
            stats["recovered_category_count"] += 1
        if not original_bug_id and bug_id:
            stats["recovered_bug_id_count"] += 1

    return repaired, stats


def _load_preferred_multiturn_records(
    checkpoint_root: Path,
    switch_name: str,
    fallback_path: Path,
    input_dir: Path,
) -> List[Dict[str, Any]]:
    preferred_path = checkpoint_root / "augmented" / f"multiturn_conversations_{switch_name}.json"
    source_path = preferred_path if preferred_path.exists() else fallback_path
    if not source_path.exists():
        LOGGER.warning("No multiturn checkpoint found at %s or %s", preferred_path, fallback_path)
        return []

    records = _load_json_records(source_path)
    LOGGER.info("Loaded multiturn checkpoint %s (%s records)", source_path, len(records))
    return _annotate_export_metadata(records, switch_name=switch_name, input_dir=input_dir)


def _run_resume_repair_only(args: argparse.Namespace) -> Dict[str, Any]:
    switch_name = str(args.switch_name)
    checkpoint_root = _infer_artifact_root_from_checkpoint(args.resume_from_qa_json)
    output_paths = {
        "cleaned_json": checkpoint_root / "processed_json" / f"cleaned_contexts_{switch_name}.json",
        "qa_json": checkpoint_root / "processed_json" / f"qa_pairs_{switch_name}.json",
        "augmented_json": checkpoint_root / "augmented" / f"augmented_qa_{switch_name}.json",
        "negative_json": checkpoint_root / "augmented" / f"negative_samples_{switch_name}.json",
        "multiturn_json": checkpoint_root / "augmented" / f"multiturn_conversations_{switch_name}.json",
        "rich_json": checkpoint_root / "augmented" / f"rich_dataset_{switch_name}.json",
        "final_jsonl": checkpoint_root / "final_jsonl" / f"train_chat_{switch_name}.jsonl",
        "quality_report_json": checkpoint_root / "augmented" / f"quality_report_{switch_name}.json",
    }

    qa_pairs = _load_json_records(args.resume_from_qa_json)
    LOGGER.info(
        "Repair-only resume from QA checkpoint %s (%s records) under %s",
        args.resume_from_qa_json,
        len(qa_pairs),
        checkpoint_root,
    )

    repaired_pairs, repair_stats = _repair_issue_style_records(qa_pairs, switch_name=switch_name)
    save_formatter_json(repaired_pairs, output_paths["qa_json"])
    _save_release_tree_json(repaired_pairs, output_paths["qa_json"], switch_name)
    _write_release_partitioned_json(
        repaired_pairs,
        switch_name=switch_name,
        output_path=output_paths["qa_json"],
    )

    quality_records, quality_stats = enforce_quality_rules(
        repaired_pairs,
        min_grounding_score=args.min_grounding_score,
        min_quality_score=args.min_quality_score,
        semantic_dedup_threshold=None,
    )
    quality_records = _annotate_export_metadata(
        quality_records,
        switch_name=switch_name,
        input_dir=args.input_dir,
    )
    quality_stats = {
        **quality_stats,
        "resumed": True,
        "repair_only": True,
        "resumed_from": str(args.resume_from_qa_json),
        "repair_input_records": len(qa_pairs),
        "repaired_records": repair_stats["repaired_records"],
        "dropped_records": repair_stats["dropped_records"],
        "recovered_category_count": repair_stats["recovered_category_count"],
        "recovered_bug_id_count": repair_stats["recovered_bug_id_count"],
        "records_with_metadata_source": repair_stats["records_with_metadata_source"],
        **repair_stats,
    }

    multiturn_records = _load_preferred_multiturn_records(
        checkpoint_root=checkpoint_root,
        switch_name=switch_name,
        fallback_path=args.multiturn_json,
        input_dir=args.input_dir,
    )

    save_formatter_json(quality_records, output_paths["augmented_json"])
    _save_release_tree_json(quality_records, output_paths["augmented_json"], switch_name)
    _write_release_partitioned_json(
        quality_records,
        switch_name=switch_name,
        output_path=output_paths["augmented_json"],
    )

    combined_chat_records = list(quality_records) + list(multiturn_records)
    deduped_chat_records, duplicate_transcripts_removed = dedupe_chat_transcripts(combined_chat_records)

    rich_dataset = build_rich_dataset(deduped_chat_records)
    save_formatter_json(rich_dataset, output_paths["rich_json"])
    _save_release_tree_json(rich_dataset, output_paths["rich_json"], switch_name)
    _write_release_partitioned_json(
        rich_dataset,
        switch_name=switch_name,
        output_path=output_paths["rich_json"],
    )

    jsonl_rows = write_chat_jsonl(deduped_chat_records, output_paths["final_jsonl"])
    versioned_jsonl_rows = _write_version_subversion_partitioned_jsonl(
        deduped_chat_records,
        switch_name=switch_name,
        final_jsonl_path=output_paths["final_jsonl"],
    )

    output_paths["quality_report_json"].parent.mkdir(parents=True, exist_ok=True)
    quality_stats.update(
        {
            "quality_kept_records": len(quality_records),
            "multiturn_conversations_merged": len(multiturn_records),
            "duplicate_transcripts_removed": duplicate_transcripts_removed,
            "final_transcript_rows": len(deduped_chat_records),
            "final_jsonl_row_count": jsonl_rows,
        }
    )
    output_paths["quality_report_json"].write_text(json.dumps(quality_stats, indent=2), encoding="utf-8")
    LOGGER.info("Saved quality report to %s", output_paths["quality_report_json"])

    summary = {
        "input_record_count": len(qa_pairs),
        "repaired_record_count": repair_stats["repaired_records"],
        "dropped_record_count": repair_stats["dropped_records"],
        "recovered_category_count": repair_stats["recovered_category_count"],
        "recovered_bug_id_count": repair_stats["recovered_bug_id_count"],
        "multiturn_conversations_merged": len(multiturn_records),
        "duplicate_transcripts_removed": duplicate_transcripts_removed,
        "final_jsonl_row_count": jsonl_rows,
        "jsonl_rows_by_version_subversion": versioned_jsonl_rows,
        "quality_stats": quality_stats,
        "repair_only": True,
        "checkpoint_root": str(checkpoint_root),
    }
    LOGGER.info("Repair-only pipeline summary: %s", json.dumps(summary, indent=2))
    return summary


def combine_chat_jsonl_files(input_paths: Sequence[Path], output_path: Path) -> int:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    seen = set()
    written = 0

    with output_path.open("w", encoding="utf-8") as writer:
        for input_path in input_paths:
            if not input_path.exists():
                LOGGER.warning("Skipping missing JSONL file: %s", input_path)
                continue

            with input_path.open("r", encoding="utf-8") as reader:
                for line_number, raw_line in enumerate(reader, start=1):
                    line = raw_line.strip()
                    if not line:
                        continue

                    try:
                        payload = json.loads(line)
                    except json.JSONDecodeError:
                        LOGGER.warning(
                            "Skipping invalid JSON at %s:%s",
                            input_path,
                            line_number,
                        )
                        continue

                    messages = payload.get("messages", []) if isinstance(payload, dict) else []
                    if not isinstance(messages, list):
                        LOGGER.warning("Skipping invalid chat format at %s:%s", input_path, line_number)
                        continue

                    key = _chat_transcript_key(payload if isinstance(payload, dict) else {})
                    if key in seen:
                        continue
                    seen.add(key)

                    canonical = _chat_payload(payload if isinstance(payload, dict) else {})
                    if not canonical:
                        LOGGER.warning("Skipping incomplete chat row at %s:%s", input_path, line_number)
                        continue
                    writer.write(json.dumps(canonical, ensure_ascii=False) + "\n")
                    written += 1

    LOGGER.info("Combined %s rows into %s", written, output_path)
    return written


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build chat fine-tuning data from raw HTML files.")
    parser.add_argument("--input-dir", type=_path, default=BASE_DIR / "data/raw_html")
    parser.add_argument(
        "--cleaned-json",
        type=_path,
        default=BASE_DIR / "data/processed_json/cleaned_contexts.json",
    )
    parser.add_argument(
        "--qa-json",
        type=_path,
        default=BASE_DIR / "data/processed_json/qa_pairs.json",
    )
    parser.add_argument(
        "--augmented-json",
        type=_path,
        default=BASE_DIR / "data/augmented/augmented_qa.json",
    )
    parser.add_argument(
        "--negative-json",
        type=_path,
        default=BASE_DIR / "data/augmented/negative_samples.json",
    )
    parser.add_argument(
        "--multiturn-json",
        type=_path,
        default=BASE_DIR / "data/augmented/multiturn_conversations.json",
    )
    parser.add_argument(
        "--rich-json",
        type=_path,
        default=BASE_DIR / "data/augmented/rich_dataset.json",
    )
    parser.add_argument(
        "--final-jsonl",
        type=_path,
        default=BASE_DIR / "data/final_jsonl/train_chat.jsonl",
    )
    parser.add_argument(
        "--quality-report-json",
        type=_path,
        default=BASE_DIR / "data/augmented/quality_report.json",
    )
    parser.add_argument(
        "--switch-name",
        default="",
        help="Optional switch/model name used to suffix all output files (example: 8100 -> train_chat_8100.jsonl).",
    )
    parser.add_argument(
        "--combine-jsonl",
        type=_path,
        nargs="+",
        default=None,
        help="Optional list of per-switch JSONL files to combine into one training file.",
    )
    parser.add_argument(
        "--combined-jsonl",
        type=_path,
        default=BASE_DIR / "data/final_jsonl/train_chat_combined.jsonl",
        help="Output path used with --combine-jsonl.",
    )
    parser.add_argument("--provider", choices=["mock", "openai", "ollama"], default="mock")
    parser.add_argument("--model", default="gpt-4o-mini")
    parser.add_argument("--temperature", type=float, default=0.2)
    parser.add_argument("--timeout-seconds", type=int, default=60)
    parser.add_argument("--num-pairs-per-context", type=int, default=2)
    parser.add_argument("--max-files", type=int, default=None)
    parser.add_argument("--max-contexts", type=int, default=None)
    parser.add_argument("--max-entries", type=int, default=None)
    parser.add_argument("--include-negative", action="store_true")
    parser.add_argument("--include-multiturn", action="store_true")
    parser.add_argument("--min-grounding-score", type=float, default=0.62)
    parser.add_argument("--min-quality-score", type=float, default=0.72)
    parser.add_argument("--semantic-dedup-threshold", type=float, default=0.96)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING", "ERROR"])
    parser.add_argument(
        "--resume-from-qa-json",
        type=_path,
        default=None,
        help=(
            "Resume from an existing QA JSON checkpoint. With the default mock provider this uses "
            "repair-only export mode; with an LLM provider it reruns augmentation plus downstream stages."
        ),
    )
    parser.add_argument(
        "--resume-from-augmented-json",
        type=_path,
        default=None,
        help="Resume from an existing augmented JSON checkpoint and rerun only downstream stages.",
    )
    return parser.parse_args()


def configure_logging(log_level: str) -> None:
    logging.basicConfig(
        level=getattr(logging, log_level.upper(), logging.INFO),
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )


def run_pipeline(args: argparse.Namespace) -> Dict[str, Any]:
    if args.resume_from_qa_json and args.resume_from_augmented_json:
        raise ValueError("Use only one resume checkpoint at a time.")

    if args.resume_from_qa_json:
        if args.provider != "mock":
            LOGGER.info("Ignoring provider=%s in repair-only resume mode.", args.provider)
        return _run_resume_repair_only(args)

    cleaned_entries: List[Dict[str, Any]] = []
    qa_pairs: List[Dict[str, Any]] = []
    augmented_records: List[Dict[str, Any]] = []
    negative_records: List[Dict[str, Any]] = []
    multiturn_records: List[Dict[str, Any]] = []

    if args.resume_from_augmented_json:
        if args.include_negative or args.include_multiturn:
            raise ValueError(
                "Resuming from an augmented JSON checkpoint cannot recreate negative or multi-turn outputs. "
                "Resume from the QA checkpoint instead if you need those artifacts."
            )
        quality_records = _load_json_records(args.resume_from_augmented_json)
        LOGGER.info(
            "Resuming from augmented checkpoint %s (%s records)",
            args.resume_from_augmented_json,
            len(quality_records),
        )
        quality_stats: Dict[str, Any] = {
            "resumed": True,
            "resumed_from": str(args.resume_from_augmented_json),
            "kept_records": len(quality_records),
        }
        quality_records = _annotate_export_metadata(
            quality_records,
            switch_name=str(args.switch_name),
            input_dir=args.input_dir,
        )
    else:
        if args.resume_from_qa_json:
            qa_pairs = _load_json_records(args.resume_from_qa_json)
            LOGGER.info(
                "Resuming from QA checkpoint %s (%s records)",
                args.resume_from_qa_json,
                len(qa_pairs),
            )
        else:
            cleaned_entries = parse_html_directory(
                input_dir=args.input_dir,
                max_files=args.max_files,
                max_entries=args.max_entries,
            )
            save_parser_json(cleaned_entries, args.cleaned_json)

            qa_generator = QAGenerator(
                LLMConfig(
                    provider=args.provider,
                    model=args.model,
                    temperature=args.temperature,
                    timeout_seconds=args.timeout_seconds,
                )
            )
            qa_pairs = qa_generator.generate(
                cleaned_entries,
                num_pairs_per_context=args.num_pairs_per_context,
                max_contexts=args.max_contexts,
            )
            save_parser_json(qa_pairs, args.qa_json)

        augmenter = DataAugmenter(
            llm_config=LLMConfig(
                provider=args.provider,
                model=args.model,
                temperature=args.temperature,
                timeout_seconds=args.timeout_seconds,
            ),
            aug_config=AugmentationConfig(
                include_negative=args.include_negative,
                include_multiturn=args.include_multiturn,
                seed=args.seed,
            ),
        )
        augmented_records, negative_records, multiturn_records = augmenter.augment(qa_pairs)
        quality_records, quality_stats = enforce_quality_rules(
            augmented_records,
            min_grounding_score=args.min_grounding_score,
            min_quality_score=args.min_quality_score,
            semantic_dedup_threshold=args.semantic_dedup_threshold,
        )
        quality_records = _annotate_export_metadata(
            quality_records,
            switch_name=str(args.switch_name),
            input_dir=args.input_dir,
        )

    save_formatter_json(quality_records, args.augmented_json)
    _save_release_tree_json(quality_records, args.augmented_json, str(args.switch_name))
    _write_release_partitioned_json(
        quality_records,
        switch_name=str(args.switch_name),
        output_path=args.augmented_json,
    )
    if args.include_negative:
        negative_with_metadata = _annotate_export_metadata(
            negative_records,
            switch_name=str(args.switch_name),
            input_dir=args.input_dir,
        )
        save_formatter_json(negative_with_metadata, args.negative_json)
        _save_release_tree_json(negative_with_metadata, args.negative_json, str(args.switch_name))
        _write_release_partitioned_json(
            negative_with_metadata,
            switch_name=str(args.switch_name),
            output_path=args.negative_json,
        )
    if args.include_multiturn:
        multiturn_with_metadata = _annotate_export_metadata(
            multiturn_records,
            switch_name=str(args.switch_name),
            input_dir=args.input_dir,
        )
        save_formatter_json(multiturn_with_metadata, args.multiturn_json)
        _save_release_tree_json(multiturn_with_metadata, args.multiturn_json, str(args.switch_name))
        _write_release_partitioned_json(
            multiturn_with_metadata,
            switch_name=str(args.switch_name),
            output_path=args.multiturn_json,
        )

    rich_dataset = build_rich_dataset(quality_records)
    save_formatter_json(rich_dataset, args.rich_json)
    _save_release_tree_json(rich_dataset, args.rich_json, str(args.switch_name))
    _write_release_partitioned_json(
        rich_dataset,
        switch_name=str(args.switch_name),
        output_path=args.rich_json,
    )
    jsonl_rows = write_chat_jsonl(quality_records, args.final_jsonl)
    versioned_jsonl_rows = _write_version_subversion_partitioned_jsonl(
        quality_records,
        switch_name=str(args.switch_name),
        final_jsonl_path=args.final_jsonl,
    )
    args.quality_report_json.parent.mkdir(parents=True, exist_ok=True)
    args.quality_report_json.write_text(json.dumps(quality_stats, indent=2), encoding="utf-8")
    LOGGER.info("Saved quality report to %s", args.quality_report_json)

    summary = {
        "cleaned_contexts": len(cleaned_entries),
        "qa_pairs": len(qa_pairs),
        "augmented_positive_pairs": len(augmented_records),
        "quality_filtered_pairs": len(quality_records),
        "negative_pairs": len(negative_records),
        "multiturn_records": len(multiturn_records),
        "jsonl_rows": jsonl_rows,
        "jsonl_rows_by_version_subversion": versioned_jsonl_rows,
        "quality_stats": quality_stats,
    }
    LOGGER.info("Pipeline summary: %s", json.dumps(summary, indent=2))
    return summary


def main() -> None:
    load_dotenv()
    args = parse_args()
    configure_logging(args.log_level)
    if args.combine_jsonl:
        combine_chat_jsonl_files(args.combine_jsonl, args.combined_jsonl)
        return

    switch_name = _apply_switch_suffix(args)
    if switch_name:
        LOGGER.info("Running pipeline for switch=%s", switch_name)
    run_pipeline(args)


if __name__ == "__main__":
    main()
