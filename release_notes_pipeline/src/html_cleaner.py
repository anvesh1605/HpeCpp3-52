"""Utilities for extracting clean training contexts from raw HTML."""

from __future__ import annotations

import logging
import re
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set, Tuple

from bs4 import BeautifulSoup, Comment, Tag

LOGGER = logging.getLogger(__name__)

WHITESPACE_RE = re.compile(r"\s+")
PUNCT_ONLY_RE = re.compile(r"^[\W_]+$")
NOISE_TAGS = {
    "script",
    "style",
    "noscript",
    "iframe",
    "svg",
    "canvas",
    "template",
}
NOISE_SELECTORS = [
    "nav",
    "header",
    "footer",
    "aside",
    "form",
    ".navigation",
    ".sidenav",
    ".toc",
    ".breadcrumb",
    ".search",
    ".menu",
    ".off-canvas",
    ".title-bar",
    ".nav-search-wrapper",
    ".central-account-wrapper",
    "[role='navigation']",
    "[data-mc-ignore='true']",
]
CONTENT_SELECTORS = [
    "[data-mc-content-body='True']",
    "main",
    "article",
    ".body-container",
    ".main-section",
]
PARAGRAPH_TAGS = ("p", "li")


def _normalize_text(text: str) -> str:
    text = text.replace("\xa0", " ")
    text = WHITESPACE_RE.sub(" ", text).strip(" |;:-")
    return text


def _has_text(value: Optional[str]) -> bool:
    if not value:
        return False
    value = value.strip()
    return bool(value) and not bool(PUNCT_ONLY_RE.match(value))


def _drop_noise_nodes(soup: BeautifulSoup) -> None:
    for tag_name in NOISE_TAGS:
        for node in soup.find_all(tag_name):
            node.decompose()

    for selector in NOISE_SELECTORS:
        for node in soup.select(selector):
            node.decompose()

    for node in soup.find_all(attrs={"aria-hidden": "true"}):
        node.decompose()

    for node in soup.find_all(string=lambda text: isinstance(text, Comment)):
        node.extract()


def _content_root(soup: BeautifulSoup) -> Tag:
    candidates: List[Tag] = []
    for selector in CONTENT_SELECTORS:
        candidates.extend([node for node in soup.select(selector) if isinstance(node, Tag)])

    if not candidates:
        return soup.body or soup

    return max(candidates, key=lambda node: len(node.get_text(" ", strip=True)))


def _extract_table_headers(table: Tag) -> List[str]:
    header_row: Optional[Tag] = None
    thead = table.find("thead")
    if thead:
        header_row = thead.find("tr")
    if not header_row:
        first_row = table.find("tr")
        if first_row and first_row.find("th"):
            header_row = first_row

    if not header_row:
        return []

    headers = [_normalize_text(cell.get_text(" ", strip=True)) for cell in header_row.find_all(["th", "td"])]
    return [header for header in headers if _has_text(header)]


def _table_title(table: Tag) -> str:
    caption = table.find("caption")
    if caption:
        title = _normalize_text(caption.get_text(" ", strip=True))
        if _has_text(title):
            return title

    previous = table.find_previous(["h1", "h2", "h3", "h4", "h5", "h6"])
    if previous:
        title = _normalize_text(previous.get_text(" ", strip=True))
        if _has_text(title):
            return title

    return ""


def _row_is_header_like(cells: List[str], headers: List[str]) -> bool:
    if not cells or not headers:
        return False
    return [cell.lower() for cell in cells] == [header.lower() for header in headers]


def _format_table_row(headers: List[str], cells: List[str], title: str) -> str:
    if headers and len(headers) == len(cells):
        joined = "; ".join(f"{headers[index]}: {cell}" for index, cell in enumerate(cells) if _has_text(cell))
    else:
        joined = "; ".join(f"Column {index + 1}: {cell}" for index, cell in enumerate(cells) if _has_text(cell))

    if title:
        return f"{title} | {joined}"
    return joined


def _extract_table_entries(root: Tag, source: str) -> List[Dict[str, str]]:
    entries: List[Dict[str, str]] = []
    for table in root.find_all("table"):
        headers = _extract_table_headers(table)
        title = _table_title(table)
        rows = table.find_all("tr")
        for row in rows:
            cells = [_normalize_text(cell.get_text(" ", strip=True)) for cell in row.find_all(["td", "th"])]
            cells = [cell for cell in cells if _has_text(cell)]
            if not cells:
                continue
            if _row_is_header_like(cells, headers):
                continue

            context = _normalize_text(_format_table_row(headers, cells, title))
            if not _has_text(context):
                continue
            entries.append({"context": context, "type": "table", "source": source})

    return entries


def _is_inside_table(node: Tag) -> bool:
    return bool(node.find_parent("table"))


def _is_noise_paragraph(text: str) -> bool:
    lowered = text.lower()
    if len(text) < 45:
        return True
    noisy_tokens = ["skip to main content", "submit search", "all files", "account settings", "logout"]
    return any(token in lowered for token in noisy_tokens)


def _extract_paragraph_entries(root: Tag, source: str) -> List[Dict[str, str]]:
    entries: List[Dict[str, str]] = []
    for node in root.find_all(PARAGRAPH_TAGS):
        if not isinstance(node, Tag):
            continue
        if _is_inside_table(node):
            continue
        text = _normalize_text(node.get_text(" ", strip=True))
        if not _has_text(text):
            continue
        if _is_noise_paragraph(text):
            continue
        entries.append({"context": text, "type": "paragraph", "source": source})
    return entries


def _deduplicate_entries(entries: Iterable[Dict[str, str]]) -> List[Dict[str, str]]:
    deduped: List[Dict[str, str]] = []
    seen: Set[Tuple[str, str, str]] = set()
    for entry in entries:
        key = (
            entry["source"].strip().lower(),
            entry["type"].strip().lower(),
            entry["context"].strip().lower(),
        )
        if key in seen:
            continue
        seen.add(key)
        deduped.append(entry)
    return deduped


def clean_html_to_entries(html_text: str, source: str) -> List[Dict[str, str]]:
    """Convert raw HTML text into clean paragraph/table context entries."""
    soup = BeautifulSoup(html_text, "lxml")
    _drop_noise_nodes(soup)
    root = _content_root(soup)

    table_entries = _extract_table_entries(root, source)
    paragraph_entries = _extract_paragraph_entries(root, source)
    merged = _deduplicate_entries([*table_entries, *paragraph_entries])
    LOGGER.debug(
        "Extracted %s table entries and %s paragraph entries from %s",
        len(table_entries),
        len(paragraph_entries),
        source,
    )
    return merged


def clean_html_file(path: Path) -> List[Dict[str, str]]:
    """Read one HTML file and return clean entries."""
    source = path.name
    try:
        html_text = path.read_text(encoding="utf-8", errors="ignore")
        return clean_html_to_entries(html_text, source=source)
    except Exception as exc:  # pylint: disable=broad-except
        LOGGER.exception("Failed to parse %s: %s", path, exc)
        return []
