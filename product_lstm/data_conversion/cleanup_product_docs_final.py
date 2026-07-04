#!/usr/bin/env python3
"""Strict cleanup pass for product-documentation LSTM data."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from collections import Counter
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, Iterable, Iterator, List, Mapping, Optional, Sequence, Tuple


WHITESPACE_RE = re.compile(r"\s+")
PAGE_ONLY_RE = re.compile(r"^\s*\d+\s*$")
PUBLIC_RE = re.compile(r"(?i)\bpublic\b")
PAGE_FRAGMENT_RE = re.compile(r"(?i)\b(?:page|pp\.?|p\.)\s*\d+\b|\b\d{1,4}\b$")
BROKEN_SPACING_RE = re.compile(r"(?i)\b(?:Ran ge|wit h|fo r|entri es|re se t|com man d)\b")
NOTE_RE = re.compile(r"(?i)\bnote\b")
NOTE_NOISE_RE = re.compile(r"(?i)\bdocumented in this guide\b|\bpublic\b|\btable of contents\b")
EVENT_BAD_RE = re.compile(
    r"(?i)(?:Description:\s*Event ID|Information\s+Information|Warning\s+Warning|Error\s+Error|Severity:\s*<log>|\b<log>\b)"
)
EVENT_REPEAT_SEVERITY_RE = re.compile(r"(?i)\b(Information|Warning|Error)(?:\s+\1)+\b")
MULTI_COMMAND_RE = re.compile(r"(?i)\s-\s*(?:show|no|clear|access-list|ip\s|vlan\s)")
SYNTAX_MULTI_BULLET_RE = re.compile(r"(?m)^\s*[-*]\s+\S+")
HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+(.+?)\s*$")

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPT_DIR.parent


def collapse(value: Any) -> str:
    text = str(value or "").replace("\r\n", "\n").replace("\r", "\n")
    text = text.replace("\f", " ")
    text = WHITESPACE_RE.sub(" ", text).strip()
    return text


def normalize(value: Any) -> str:
    return collapse(value).casefold()


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def short_hash(*parts: Any, size: int = 10) -> str:
    seed = "\n".join(collapse(part) for part in parts)
    return sha256_text(seed)[:size]


def display_version(value: Any) -> str:
    return collapse(value).replace("_", ".")


def load_jsonl(path: Path) -> Iterator[Tuple[int, Dict[str, Any]]]:
    with path.open("r", encoding="utf-8-sig") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON in {path}:{line_number}: {exc}") from exc
            if not isinstance(row, dict):
                raise ValueError(f"Expected object row in {path}:{line_number}")
            yield line_number, row


@lru_cache(maxsize=1024)
def load_markdown_lines(path_str: str) -> Tuple[str, ...]:
    path = Path(path_str)
    text = path.read_text(encoding="utf-8", errors="replace")
    return tuple(text.splitlines())


@lru_cache(maxsize=128)
def markdown_files_for_root(root_str: str, switch: str, version: str) -> Tuple[str, ...]:
    version_folder = version.replace(".", "_")
    root = Path(root_str) / "Raw_Data_Product" / switch / version_folder
    if not root.exists():
        return tuple()
    return tuple(str(path) for path in sorted(root.rglob("*.md")))


@lru_cache(maxsize=32)
def markdown_heading_index_for_root(root_str: str, switch: str, version: str) -> Dict[str, Tuple[str, int]]:
    index: Dict[str, Tuple[str, int]] = {}
    for file_str in markdown_files_for_root(root_str, switch, version):
        try:
            lines = load_markdown_lines(file_str)
        except OSError:
            continue
        for idx, line in enumerate(lines):
            match = HEADING_RE.match(line)
            if not match:
                continue
            heading = normalize_heading(match.group(1))
            if not heading or heading in index:
                continue
            index[heading] = (file_str, idx)
    return index


def candidate_texts(row: Mapping[str, Any]) -> List[str]:
    intent = normalize(row.get("intent"))
    slots = row.get("slots") or {}
    text = collapse(row.get("input_text"))
    candidates: List[str] = []

    command = collapse(slots.get("command"))
    topic = collapse(slots.get("topic"))
    feature = collapse(slots.get("feature"))
    object_name = collapse(slots.get("object_name"))
    event_id = collapse(slots.get("event_id"))

    if intent in {"cli_syntax", "cli_meaning", "show_command_syntax", "show_command_meaning"} and command:
        candidates.append(command)
        if command.startswith("show "):
            candidates.append(command)
    if intent == "event_log_meaning" and event_id:
        candidates.extend([f"Event ID: {event_id}", f"Event ID {event_id}", event_id])
    if intent == "configuration_procedure" and feature:
        candidates.extend([feature, f"Configuring {feature}"])
    if intent == "concept_explanation" and topic:
        candidates.extend([topic, topic.removeprefix("About ").strip()])
    if intent == "snmp_mib_info" and object_name:
        candidates.extend([object_name])
    if intent in {"troubleshooting", "product_caveat", "product_requirement", "product_limitation", "product_generic"} and topic:
        candidates.extend([topic])

    # Fallbacks from the prompt text.
    patterns = [
        r"(?i)^for\s+.+?,\s*what is the syntax of the (.+?) command\?",
        r"(?i)^for\s+.+?,\s*what does the (.+?) command do\?",
        r"(?i)^for\s+.+?,\s*how do you configure (.+?)\?",
        r"(?i)^for\s+.+?,\s*what is (.+?)\?",
        r"(?i)^for\s+.+?,\s*what event log information is documented for event id (\d+)\?",
        r"(?i)^for\s+.+?,\s*what snmp mib information is documented for (.+?)\?",
        r"(?i)^for\s+.+?,\s*how do you troubleshoot (.+?)\?",
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            candidates.append(collapse(match.group(1)))

    unique: List[str] = []
    seen: set[str] = set()
    for candidate in candidates:
        key = normalize(candidate)
        if key and key not in seen:
            seen.add(key)
            unique.append(candidate)
    return unique


def normalize_heading(value: str) -> str:
    text = collapse(value)
    text = re.sub(r"^[#>*\-\s]+", "", text)
    return normalize(text)


def extract_excerpt(lines: Sequence[str], heading_index: int, max_lines: int = 20) -> str:
    window: List[str] = []
    for line in lines[heading_index : heading_index + max_lines]:
        text = collapse(line)
        if not text:
            if window:
                break
            continue
        if text == "Public" or PAGE_ONLY_RE.match(text):
            continue
        window.append(text)
    return "\n".join(window)


def find_markdown_match(row: Mapping[str, Any], markdown_roots: Sequence[Path]) -> Tuple[Optional[Path], Optional[str], str]:
    slots = row.get("slots") or {}
    switch = collapse(slots.get("switch"))
    version = display_version(slots.get("version"))
    if not switch or not version:
        return None, None, ""

    candidates = candidate_texts(row)
    search_roots = [root for root in markdown_roots if root.exists()]
    for root in search_roots:
        heading_index = markdown_heading_index_for_root(str(root), switch, version)
        if not heading_index:
            continue
        for candidate in candidates:
            cand_norm = normalize_heading(candidate)
            if not cand_norm:
                continue
            hit = heading_index.get(cand_norm)
            if hit is not None:
                file_str, idx = hit
                path = Path(file_str)
                excerpt = extract_excerpt(load_markdown_lines(file_str), idx)
                return path, candidate, excerpt
    return None, None, ""


def strip_page_fragments(text: str) -> Tuple[str, bool]:
    original = text
    cleaned = collapse(text)
    changed = False
    cleaned = PUBLIC_RE.sub("", cleaned)
    if cleaned != original:
        changed = True
    # Remove common trailing page fragments like "access-list copy 23."
    cleaned2 = re.sub(r"(?i)\s+\b(?:page|pp\.?|p\.)?\s*\d+\b\.?$", "", cleaned).strip()
    if cleaned2 != cleaned:
        cleaned = cleaned2
        changed = True
    cleaned = WHITESPACE_RE.sub(" ", cleaned).strip(" -")
    return cleaned, changed


def split_sentences(text: str) -> List[str]:
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z])", collapse(text))
    return [part.strip() for part in parts if part.strip()]


def shorten_note_target(text: str) -> Tuple[str, bool, bool]:
    cleaned = collapse(text)
    if not cleaned or "note" not in cleaned.casefold():
        return cleaned, False, False
    if NOTE_NOISE_RE.search(cleaned):
        return "", False, True
    parts = re.split(r"(?i)\bNOTE\b", cleaned, maxsplit=1)
    head = collapse(parts[0])
    tail = collapse(parts[1]) if len(parts) > 1 else ""
    if tail and len(tail.split()) <= 24 and not re.search(r"\|{2,}|[•\[\]]", tail):
        tail_sentence = split_sentences(tail)[0] if split_sentences(tail) else tail
        if head:
            result = f"{head} NOTE {tail_sentence}".strip()
        else:
            result = tail_sentence
        return WHITESPACE_RE.sub(" ", result).strip(), True, False
    if head and len(head.split()) <= 30 and not re.search(r"\|{2,}|[•\[\]]", head):
        return head, True, False
    return "", False, True


def is_syntax_intent(intent: str) -> bool:
    return intent in {"cli_syntax", "show_command_syntax"}


def is_meaning_intent(intent: str) -> bool:
    return intent in {"cli_meaning", "show_command_meaning"}


def is_event_intent(intent: str) -> bool:
    return intent == "event_log_meaning"


def word_count(text: str) -> int:
    return len(re.findall(r"[A-Za-z0-9_<>\-]+", collapse(text)))


def validate_or_review(
    row: Mapping[str, Any],
    markdown_file: Optional[Path],
    matched_section: Optional[str],
    source_excerpt: str,
    target_value: str,
) -> Optional[str]:
    intent = normalize(row.get("intent"))
    input_text = collapse(row.get("input_text"))
    slots = row.get("slots") or {}
    command = collapse(slots.get("command"))
    event_id = collapse(slots.get("event_id"))
    target = collapse(target_value)

    if not input_text:
        return "empty_input_text"
    if not target:
        return "empty_target_value"
    if not markdown_file:
        return "markdown_file_not_found"
    if not matched_section:
        return "markdown_section_not_matched"

    if is_event_intent(intent):
        if not event_id:
            return "missing_event_id"
        if EVENT_BAD_RE.search(target) or EVENT_REPEAT_SEVERITY_RE.search(target):
            return "event_template_or_repeated_severity"
        if re.fullmatch(rf"(?i)event id[:\s]*{re.escape(event_id)}\.?", target):
            return "event_template_or_repeated_severity"
        if re.search(r"(?i)\bno real event message\b", target):
            return "event_template_or_repeated_severity"
        if word_count(target) > 60:
            return "event_template_or_repeated_severity"

    if "note" in target.casefold():
        if word_count(target) > 100:
            return "note_row_too_long"
        if NOTE_NOISE_RE.search(target):
            return "note_row_moved_to_review"

    if is_syntax_intent(intent):
        if not command:
            return "missing_command"
        if target.startswith("-"):
            return "multi_command_syntax_rows_moved_to_review"
        if SYNTAX_MULTI_BULLET_RE.search(target):
            return "multi_command_syntax_rows_moved_to_review"
        if MULTI_COMMAND_RE.search(target) or " - show " in target.casefold() or " - no " in target.casefold():
            return "multi_command_syntax_rows_moved_to_review"
        if target.casefold().startswith("no ") and "what is the syntax" in input_text.casefold():
            return "no_form_syntax_rows_moved_to_review"
        if " - " in target and word_count(target) > 18:
            return "multi_command_syntax_rows_moved_to_review"

    if is_meaning_intent(intent):
        if word_count(target) > 50:
            return "long_target_rows_moved_to_review"
        if re.search(r"(?i)^\s*(?:show|access-list|interface|vlan|no)\b", target) and not re.search(
            r"(?i)\b(command|enables|copies|displays|shows|configures|allows|means|removes|sets|creates)\b",
            target,
        ):
            return "meaning_is_only_syntax"

    if intent == "concept_explanation" and word_count(target) > 80:
        return "long_target_rows_moved_to_review"
    if intent == "configuration_procedure" and word_count(target) > 100:
        return "long_target_rows_moved_to_review"

    if NOTE_RE.search(target) and word_count(target) > 80:
        return "note_row_moved_to_review"
    if BROKEN_SPACING_RE.search(target):
        return "broken_spacing_artifact"
    if "documented in this guide" in target.casefold():
        return "generic_targets_moved_to_review"
    return None


def clean_target_for_row(row: Mapping[str, Any]) -> Tuple[str, Dict[str, int]]:
    intent = normalize(row.get("intent"))
    target = collapse(row.get("target_value"))
    counts: Dict[str, int] = {}
    if not target:
        return "", counts

    cleaned, changed = strip_page_fragments(target)
    if changed:
        counts["page_fragments_removed"] = counts.get("page_fragments_removed", 0) + 1

    if is_event_intent(intent):
        return cleaned, counts

    if "note" in cleaned.casefold():
        shortened, shortened_ok, moved = shorten_note_target(cleaned)
        if shortened_ok:
            counts["note_rows_shortened"] = counts.get("note_rows_shortened", 0) + 1
            cleaned = shortened
        elif moved:
            counts["note_rows_moved_to_review"] = counts.get("note_rows_moved_to_review", 0) + 1
            return "", counts

    cleaned = WHITESPACE_RE.sub(" ", cleaned).strip(" -")
    return cleaned, counts


def safe_json_dump(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_jsonl(path: Path, rows: Iterable[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def maybe_format_with_ollama(
    row: Mapping[str, Any],
    source_excerpt: str,
    target_value: str,
    model: str,
    fallback_model: str,
) -> Tuple[str, bool, bool]:
    row_json = json.dumps(row, ensure_ascii=False, separators=(",", ":"))
    prompt = (
        "You are formatting HPE Aruba AOS-CX product-documentation LSTM training data.\n\n"
        "Do not add facts.\n"
        "Do not invent commands.\n"
        "Do not invent syntax.\n"
        "Do not invent parameters.\n"
        "Do not change placeholders.\n"
        "Only clean formatting, grammar, and extraction noise.\n"
        "Return only valid JSON.\n\n"
        f"Input row:\n{row_json}\n\n"
        f"Source markdown excerpt:\n{source_excerpt}\n\n"
        "Required output:\n"
        '{\n  "fixed_target_value": "...",\n  "changed_facts": false,\n  "needs_review": false,\n  "reason": "..."\n}\n'
    )

    def run_model(name: str) -> Optional[Dict[str, Any]]:
        try:
            proc = subprocess.run(
                ["ollama", "run", name],
                input=prompt,
                capture_output=True,
                text=True,
                encoding="utf-8",
                timeout=180,
                check=False,
            )
        except FileNotFoundError:
            return None
        if proc.returncode != 0:
            return None
        match = re.search(r"\{.*\}", (proc.stdout or "").strip(), re.S)
        if not match:
            return None
        try:
            parsed = json.loads(match.group(0))
        except json.JSONDecodeError:
            return None
        return parsed if isinstance(parsed, dict) else None

    parsed = run_model(model) or (run_model(fallback_model) if fallback_model != model else None)
    if not parsed:
        return target_value, False, False
    fixed = collapse(parsed.get("fixed_target_value"))
    changed_facts = bool(parsed.get("changed_facts", False))
    needs_review = bool(parsed.get("needs_review", False))
    if changed_facts or needs_review or not fixed:
        return target_value, False, False
    return fixed, True, fixed != collapse(target_value)


def build_review_row(
    row: Mapping[str, Any],
    target_value: str,
    reason: str,
    markdown_file: Optional[Path],
    matched_section: Optional[str],
    ollama_used: bool,
) -> Dict[str, Any]:
    slots = row.get("slots") or {}
    source_file = collapse(row.get("source_file"))
    document_title = collapse(row.get("document_title"))
    return {
        "input_text": collapse(row.get("input_text")),
        "intent": collapse(row.get("intent")),
        "slots": slots,
        "target_value": collapse(target_value),
        "review_reason": reason,
        "source_file": source_file,
        "document_title": document_title,
        "section": collapse(slots.get("topic") or slots.get("feature") or slots.get("command") or slots.get("event_id")),
        "matched_markdown_file": str(markdown_file) if markdown_file else "",
        "matched_section": matched_section or "",
        "ollama_used": bool(ollama_used),
        "status": "needs_markdown_repair",
    }


def process_input_row(
    row: Mapping[str, Any],
    markdown_roots: Sequence[Path],
    use_ollama: bool,
    ollama_model: str,
    fallback_model: str,
    counts: Counter,
) -> Tuple[Optional[Dict[str, Any]], Optional[Dict[str, Any]]]:
    print("[CHECK] validating row")
    target_value, cleanup_counts = clean_target_for_row(row)
    for key, value in cleanup_counts.items():
        counts[key] += value
    if cleanup_counts.get("page_fragments_removed"):
        print("[FIX] page fragment removed")
    if cleanup_counts.get("note_rows_shortened"):
        print("[FIX] NOTE shortened")

    markdown_file, matched_section, source_excerpt = find_markdown_match(row, markdown_roots)
    if markdown_file is None:
        counts["markdown_missing_rows"] += 1
    else:
        counts["markdown_matched_rows"] += 1

    review_reason = validate_or_review(row, markdown_file, matched_section, source_excerpt, target_value)
    if review_reason:
        review_row = build_review_row(row, target_value, review_reason, markdown_file, matched_section, False)
        counts["rows_moved_to_review_not_deleted"] += 1
        counts["review_reasons"][review_reason] += 1
        if review_reason == "event_template_or_repeated_severity":
            counts["event_template_rows_moved_to_review"] += 1
            print("[REVIEW] event template row moved to review")
        elif review_reason == "note_row_shortened":
            counts["note_rows_shortened"] += 1
            print("[FIX] NOTE shortened")
        elif review_reason == "note_row_moved_to_review":
            counts["note_rows_moved_to_review"] += 1
            print("[REVIEW] NOTE row moved to review")
        elif review_reason == "multi_command_syntax_rows_moved_to_review":
            counts["multi_command_syntax_rows_moved_to_review"] += 1
            print("[REVIEW] multi-command syntax moved to review")
        elif review_reason == "no_form_syntax_rows_moved_to_review":
            counts["no_form_syntax_rows_moved_to_review"] += 1
            print("[REVIEW] no-form syntax moved to review")
        return None, review_row

    if use_ollama and source_excerpt and target_value:
        print("[OLLAMA] formatting only")
        fixed, used, changed = maybe_format_with_ollama(
            row, source_excerpt, target_value, model=ollama_model, fallback_model=fallback_model
        )
        if used and changed:
            counts["rows_formatted_by_ollama"] += 1
            target_value = fixed
        elif used:
            counts["ollama_rejected_rows"] += 1

    final_row = {
        "input_text": collapse(row.get("input_text")),
        "intent": collapse(row.get("intent")),
        "slots": row.get("slots") or {},
        "target_value": collapse(target_value),
    }

    if not final_row["input_text"]:
        counts["empty_input_text"] += 1
        review_row = build_review_row(row, target_value, "empty_input_text", markdown_file, matched_section, False)
        counts["rows_moved_to_review_not_deleted"] += 1
        counts["review_reasons"]["empty_input_text"] += 1
        return None, review_row
    if not final_row["target_value"]:
        counts["empty_target_value"] += 1
        review_row = build_review_row(row, target_value, "empty_target_value", markdown_file, matched_section, False)
        counts["rows_moved_to_review_not_deleted"] += 1
        counts["review_reasons"]["empty_target_value"] += 1
        return None, review_row

    return final_row, None


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    data_root = ROOT_DIR
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input-dataset",
        type=Path,
        default=data_root / "lstm_conversion" / "pilot_product_5" / "dataset.jsonl",
        help="Input product dataset JSONL.",
    )
    parser.add_argument(
        "--input-review",
        type=Path,
        default=data_root / "lstm_conversion" / "pilot_product_5" / "review.jsonl",
        help="Input product review JSONL.",
    )
    parser.add_argument(
        "--markdown-root",
        dest="markdown_roots",
        action="append",
        type=Path,
        default=None,
        help="Markdown source root. May be supplied multiple times.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=data_root / "lstm_conversion" / "product_lstm_dataset_final.json",
        help="Output JSON file for clean dataset rows.",
    )
    parser.add_argument(
        "--review-output",
        type=Path,
        default=data_root / "lstm_conversion" / "product_lstm_review_final.json",
        help="Output JSON file for review rows.",
    )
    parser.add_argument(
        "--report-output",
        type=Path,
        default=data_root / "lstm_conversion" / "product_lstm_report_final.json",
        help="Output JSON file for the report.",
    )
    parser.add_argument(
        "--samples-output",
        type=Path,
        default=data_root / "lstm_conversion" / "product_lstm_samples_final.json",
        help="Output JSON file with representative samples.",
    )
    parser.add_argument("--force", action="store_true", help="Overwrite existing outputs.")
    parser.add_argument("--use-ollama", action="store_true", help="Enable Ollama formatting after validation.")
    parser.add_argument("--ollama-model", type=str, default="qwen2.5:7b-instruct")
    parser.add_argument("--ollama-fallback-model", type=str, default="qwen2.5-coder:7b")
    args = parser.parse_args(argv)
    if not args.markdown_roots:
        args.markdown_roots = [data_root / "markitdown_cli_output(product)", data_root / "markitdown_cli_output"]
    return args


def write_samples(path: Path, dataset_rows: Sequence[Mapping[str, Any]], review_rows: Sequence[Mapping[str, Any]], report: Mapping[str, Any]) -> None:
    payload = {
        "report": report,
        "final_samples": list(dataset_rows)[:10],
        "review_samples": list(review_rows)[:10],
    }
    safe_json_dump(path, payload)


def main(argv: Optional[Sequence[str]] = None) -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
        try:
            sys.stdout.reconfigure(line_buffering=True)
        except Exception:
            pass
        try:
            sys.stderr.reconfigure(line_buffering=True)
        except Exception:
            pass
    except Exception:
        pass

    print("[START] product final cleanup")
    args = parse_args(argv)
    print("[INPUT] reading dataset and existing review file")

    for path in (args.output, args.review_output, args.report_output, args.samples_output):
        if path.exists() and not args.force:
            raise FileExistsError(f"Refusing to overwrite {path}; pass --force")

    counts = Counter(
        {
            "rows_scanned": 0,
            "rows_written": 0,
            "review_rows": 0,
            "rows_moved_to_review_not_deleted": 0,
            "event_template_rows_moved_to_review": 0,
            "note_rows_shortened": 0,
            "note_rows_moved_to_review": 0,
            "multi_command_syntax_rows_moved_to_review": 0,
            "no_form_syntax_rows_moved_to_review": 0,
            "page_fragments_removed": 0,
            "rows_formatted_by_ollama": 0,
            "ollama_rejected_rows": 0,
            "invalid_jsonl_lines": 0,
            "empty_input_text": 0,
            "empty_target_value": 0,
            "duplicates_removed_from_final_only": 0,
        }
    )
    counts["review_reasons"] = Counter()
    rows_by_intent = Counter()

    dataset_rows: List[Dict[str, Any]] = []
    review_rows: List[Dict[str, Any]] = []
    seen_dataset: set[str] = set()

    def ingest_input(path: Path, is_review: bool = False) -> Iterator[Mapping[str, Any]]:
        nonlocal counts
        for line_number, row in load_jsonl(path):
            counts["rows_scanned"] += 1
            yield row

    for row in ingest_input(args.input_review, is_review=True):
        review_rows.append(row)
        counts["review_rows"] += 1
        counts["review_reasons"][collapse(row.get("review_reason")) or "existing_review"] += 1

    for row in ingest_input(args.input_dataset, is_review=False):
        final_row, review_row = process_input_row(
            row,
            markdown_roots=args.markdown_roots,
            use_ollama=args.use_ollama,
            ollama_model=args.ollama_model,
            fallback_model=args.ollama_fallback_model,
            counts=counts,
        )
        if review_row is not None:
            review_rows.append(review_row)
            counts["review_rows"] += 1
            continue
        if final_row is None:
            continue
        dedupe_key = json.dumps(final_row, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
        if dedupe_key in seen_dataset:
            counts["duplicates_removed_from_final_only"] += 1
            continue
        seen_dataset.add(dedupe_key)
        dataset_rows.append(final_row)
        rows_by_intent[collapse(final_row.get("intent"))] += 1
        counts["rows_written"] += 1
        print("[WRITE] clean row written")

    # Carry over review rows, but ensure valid JSON objects and keep exact order.
    seen_review: set[str] = set()
    final_review_rows: List[Dict[str, Any]] = []
    for row in review_rows:
        cleaned_row = row if isinstance(row, dict) else {"value": row}
        key = json.dumps(cleaned_row, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
        if key in seen_review:
            continue
        seen_review.add(key)
        final_review_rows.append(cleaned_row)

    report = {
        "rows_scanned": counts["rows_scanned"],
        "rows_written": counts["rows_written"],
        "review_rows": len(final_review_rows),
        "rows_moved_to_review_not_deleted": counts["rows_moved_to_review_not_deleted"],
        "event_template_rows_moved_to_review": counts["event_template_rows_moved_to_review"],
        "note_rows_shortened": counts["note_rows_shortened"],
        "note_rows_moved_to_review": counts["note_rows_moved_to_review"],
        "multi_command_syntax_rows_moved_to_review": counts["multi_command_syntax_rows_moved_to_review"],
        "no_form_syntax_rows_moved_to_review": counts["no_form_syntax_rows_moved_to_review"],
        "page_fragments_removed": counts["page_fragments_removed"],
        "rows_formatted_by_ollama": counts["rows_formatted_by_ollama"],
        "ollama_rejected_rows": counts["ollama_rejected_rows"],
        "invalid_jsonl_lines": counts["invalid_jsonl_lines"],
        "empty_input_text": counts["empty_input_text"],
        "empty_target_value": counts["empty_target_value"],
        "duplicates_removed_from_final_only": counts["duplicates_removed_from_final_only"],
        "rows_by_intent": dict(sorted(rows_by_intent.items())),
        "review_reasons": dict(sorted(counts["review_reasons"].items())),
    }

    safe_json_dump(args.output, dataset_rows)
    print("[OUTPUT] final dataset saved")
    safe_json_dump(args.review_output, final_review_rows)
    print("[OUTPUT] final review saved")
    safe_json_dump(args.report_output, report)
    print("[OUTPUT] final report saved")
    write_samples(args.samples_output, dataset_rows, final_review_rows, report)
    print("[QUALITY] final checks complete")
    print(
        json.dumps(
            {
                **report,
                "dataset_sha256": sha256_file(args.output),
                "review_sha256": sha256_file(args.review_output),
            },
            indent=2,
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
