"""Batch parser for turning HTML files into clean structured JSON."""

from __future__ import annotations

import json
import logging
import re
from pathlib import Path
from typing import Dict, List, Optional, Sequence

from tqdm import tqdm

try:
    from .html_cleaner import clean_html_file
except ImportError:  # pragma: no cover
    from html_cleaner import clean_html_file

LOGGER = logging.getLogger(__name__)
SUPPORTED_SUFFIXES = {".html", ".htm"}
VERSION_DIR_RE = re.compile(r"^10[_\.]\d{2}$", re.IGNORECASE)
SUB_VERSION_DIR_RE = re.compile(r"^\d{4}$")


def _release_from_path(input_dir: Path, file_path: Path) -> tuple[str, str, str]:
    try:
        relative = file_path.relative_to(input_dir)
    except ValueError:
        return "", "", ""

    relative_posix = relative.as_posix()
    parts = relative.parts
    if len(parts) < 3:
        return relative_posix, "", ""
    version_dir, sub_version_dir = parts[0], parts[1]
    if not VERSION_DIR_RE.match(version_dir):
        return relative_posix, "", ""
    if not SUB_VERSION_DIR_RE.match(sub_version_dir):
        return relative_posix, "", ""
    version = version_dir.replace(".", "_").lower()
    return relative_posix, version, sub_version_dir


def discover_html_files(input_dir: Path) -> List[Path]:
    if not input_dir.exists():
        raise FileNotFoundError(f"Input directory does not exist: {input_dir}")
    files = [path for path in input_dir.rglob("*") if path.suffix.lower() in SUPPORTED_SUFFIXES]
    return sorted(files)


def deduplicate_entries(entries: Sequence[Dict[str, str]]) -> List[Dict[str, str]]:
    seen = set()
    unique_entries: List[Dict[str, str]] = []
    for entry in entries:
        key = (entry["source"].lower().strip(), entry["type"].lower().strip(), entry["context"].lower().strip())
        if key in seen:
            continue
        seen.add(key)
        unique_entries.append(entry)
    return unique_entries


def prioritize_entries(entries: Sequence[Dict[str, str]]) -> List[Dict[str, str]]:
    """Prioritize bug-like table contexts so capped runs keep high-value rows."""

    def is_bug_context(entry: Dict[str, str]) -> bool:
        context = entry.get("context", "")
        if not context:
            return False
        return "Category:" in context and "Bug ID:" in context

    return sorted(
        entries,
        key=lambda entry: (
            not is_bug_context(entry),
            0 if entry.get("type", "").lower() == "table" else 1,
            entry.get("source", "").lower(),
        ),
    )


def parse_html_directory(
    input_dir: Path,
    max_files: Optional[int] = None,
    max_entries: Optional[int] = None,
) -> List[Dict[str, str]]:
    files = discover_html_files(input_dir)
    if max_files:
        files = files[:max_files]

    LOGGER.info("Discovered %s HTML files under %s", len(files), input_dir)
    all_entries: List[Dict[str, str]] = []
    for file_path in tqdm(files, desc="Cleaning HTML", unit="file"):
        file_entries = clean_html_file(file_path)
        source_path, version, sub_version = _release_from_path(input_dir, file_path)
        for entry in file_entries:
            if source_path:
                entry["source_path"] = source_path
            if version:
                entry["version"] = version
            if sub_version:
                entry["sub_version"] = sub_version
        all_entries.extend(file_entries)
        if max_entries and len(all_entries) >= max_entries:
            all_entries = all_entries[:max_entries]
            LOGGER.info("Reached max_entries=%s, stopping early.", max_entries)
            break

    unique_entries = deduplicate_entries(all_entries)
    prioritized_entries = prioritize_entries(unique_entries)
    LOGGER.info("Produced %s unique entries from %s raw entries.", len(prioritized_entries), len(all_entries))
    return prioritized_entries


def save_json(data: Sequence[Dict[str, object]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(list(data), indent=2, ensure_ascii=False), encoding="utf-8")
    LOGGER.info("Saved %s records to %s", len(data), output_path)
