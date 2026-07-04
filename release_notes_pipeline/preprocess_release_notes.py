"""Deterministic Aruba AOS-CX Markdown release-note preprocessing.

Core flow:
Markdown files -> section-aware structured records -> deterministic Q&A
-> validation -> training-compatible JSONL.

This script intentionally does not use LangChain, Ollama, or internet access for
core extraction. LLM repair can be layered on later, after deterministic output.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


FAKE_BUG_IDS = {
    "000000",
    "111111",
    "123456",
    "222222",
    "333333",
    "444444",
    "555555",
    "666666",
    "777777",
    "789012",
    "888888",
    "999999",
}

PLACEHOLDER_INLINE_RE = re.compile(
    r"<(?:description from the table|real description from the table|step one|real step one)>|"
    r"\bTBD\b",
    re.IGNORECASE,
)
BUG_ID_RE = re.compile(r"\b\d{5,7}\b")
WHITESPACE_RE = re.compile(r"\s+")
LABEL_RE = re.compile(
    r"(?i)(?:^|[\s.;|])(?P<label>symptom|symtom|scenario|workaround)\s*(?::|-|\u2013|\u2014)?\s*"
)
URL_END_RE = re.compile(r"https?://\S+$", re.IGNORECASE)
CODE_LIKE_END_RE = re.compile(
    r"(?:^|\s)(?:show|start-shell|sudo|systemctl|boot|copy|configure|exit|ip)\s+[A-Za-z0-9_./<>-]+$",
    re.IGNORECASE,
)
COMMAND_LIST_WORKAROUND_RE = re.compile(
    r"Issue the following commands in order:\s*(?:\*\s*)?"
    r"start-shell\s*(?:[;*]\s*|\s+)"
    r"sudo\s+bash\s*(?:[;*]\s*|\s+)"
    r"systemctl\s+restart_jitterentropy-rngd\s*(?:[;*]\s*|\s+)"
    r"exit\s*(?:[;*]\s*|\s+)"
    r"exit\s*(?:[;*]\s*|\s+)"
    r"show\s+aruba-central\.?",
    re.IGNORECASE,
)
MALFORMED_LOGGED_OUT_RE = re.compile(r"\b(?:ogged|ll+ogged) out\b", re.IGNORECASE)
MALFORMED_REPEATED_LETTERS_RE = re.compile(r"\bll{2,}[A-Za-z]*\b")
BROKEN_MOBILITY_CONDUCTOR_RE = re.compile(
    r"\b(?:if\s+mobility conductor does|mobility conductor\.\s+does)\b",
    re.IGNORECASE,
)
MISSING_LABEL_PUNCTUATION_RE = re.compile(r"(?<=[A-Za-z0-9)\"])\s+(Scenario:|Workaround:)")
BROKEN_TPM_QUOTE_RE = re.compile(
    r'(?<!")Central source connection status"\s+field\s+in\s+the\s+"show aruba-central"',
    re.IGNORECASE,
)
KNOWN_COMMAND_LIST_WORKAROUND = (
    "Issue the following commands in order: start-shell; sudo bash; "
    "systemctl restart_jitterentropy-rngd; exit; exit; show aruba-central."
)
BAD_UPGRADE_PROCEDURE_ENDING = (
    "Use the boot system <BOOT-BANK> command to initiate the upgrade. "
    "On the switch console port an output similar to the following will be displayed "
    "as various components are being updated:."
)
GOOD_UPGRADE_PROCEDURE_ENDING = (
    "Use the boot system <BOOT-BANK> command to initiate the upgrade. "
    "On the switch console port, output similar to the documented example will be displayed "
    "as various components are being updated."
)
BAD_OUTPUT_PATTERNS = (
    "{_}",
    "llogged",
    "llll",
    "PER certificate",
    "'Get'a",
    "updated:.",
    "event of of",
    "with in the system",
    "Best practices is",
    "depending its capability",
    "depending on its capability",
    "webUI (Bug ID",
    "Central Scenario:",
    "Scenario: Workaround:",
)
CATEGORY_CASE_VARIANTS = {
    "webUI": "WebUI",
    "Webui": "WebUI",
    "WEBUI": "WebUI",
}
QUESTION_GROUNDING_RE = re.compile(r"^For\s+.+?\s+AOS-CX\s+\d+(?:\.\d+){1,2},\s+", re.IGNORECASE)

SECTION_DEFS: dict[str, dict[str, Any]] = {
    "sections_index": {
        "section": "Sections Index",
        "source_type": "release_notes_toc",
        "kind": "skip",
    },
    "_sections_index": {
        "section": "Sections Index",
        "source_type": "release_notes_toc",
        "kind": "skip",
    },
    "fixes": {
        "section": "Resolved Issues",
        "source_type": "release_notes_resolved_issues",
        "kind": "bug",
    },
    "resolved_issues": {
        "section": "Resolved Issues",
        "source_type": "release_notes_resolved_issues",
        "kind": "bug",
    },
    "issues": {
        "section": "Known Issues",
        "source_type": "release_notes_known_issues",
        "kind": "bug",
    },
    "known_issues": {
        "section": "Known Issues",
        "source_type": "release_notes_known_issues",
        "kind": "bug",
    },
    "caveats": {
        "section": "Feature Caveats",
        "source_type": "release_notes_caveats",
        "kind": "feature_caveats",
    },
    "feature_caveats": {
        "section": "Feature Caveats",
        "source_type": "release_notes_caveats",
        "kind": "feature_caveats",
    },
    "compatibility_interoperability": {
        "section": "Compatibility and Interoperability",
        "source_type": "release_notes_compatibility",
        "kind": "compatibility",
    },
    "compatibility": {
        "section": "Compatibility and Interoperability",
        "source_type": "release_notes_compatibility",
        "kind": "compatibility",
    },
    "interoperability": {
        "section": "Compatibility and Interoperability",
        "source_type": "release_notes_compatibility",
        "kind": "compatibility",
    },
    "products_supported": {
        "section": "Products Supported",
        "source_type": "release_notes_supported_products",
        "kind": "products",
    },
    "supported_products": {
        "section": "Products Supported",
        "source_type": "release_notes_supported_products",
        "kind": "products",
    },
    "manual_configuration_restore_for_software_downgrade": {
        "section": "Manual Configuration Restore for Software Downgrade",
        "source_type": "release_notes_downgrade_restore",
        "kind": "downgrade_restore",
    },
    "downgrade_restore": {
        "section": "Manual Configuration Restore for Software Downgrade",
        "source_type": "release_notes_downgrade_restore",
        "kind": "downgrade_restore",
    },
    "performing_the_software_upgrade": {
        "section": "Performing the Software Upgrade",
        "source_type": "release_notes_upgrade_procedure",
        "kind": "upgrade_procedure",
    },
    "software_upgrade": {
        "section": "Performing the Software Upgrade",
        "source_type": "release_notes_upgrade_procedure",
        "kind": "upgrade_procedure",
    },
    "upgrade_procedure": {
        "section": "Performing the Software Upgrade",
        "source_type": "release_notes_upgrade_procedure",
        "kind": "upgrade_procedure",
    },
    "industry_and_government_certifications": {
        "section": "Industry and Government Certifications",
        "source_type": "release_notes_certifications",
        "kind": "certifications",
    },
    "certifications": {
        "section": "Industry and Government Certifications",
        "source_type": "release_notes_certifications",
        "kind": "certifications",
    },
    "license_written_offer": {
        "section": "License Written Offer",
        "source_type": "legal_license",
        "kind": "license",
    },
    "license": {
        "section": "License Written Offer",
        "source_type": "legal_license",
        "kind": "license",
    },
    "version_history": {
        "section": "Version History",
        "source_type": "release_notes_version_history",
        "kind": "version_history",
    },
    "overview": {
        "section": "Overview",
        "source_type": "release_notes_overview",
        "kind": "skip",
    },
    "enhancements": {
        "section": "Enhancements",
        "source_type": "release_notes_enhancements",
        "kind": "skip",
    },
    "important_information": {
        "section": "Important Information",
        "source_type": "release_notes_important_information",
        "kind": "skip",
    },
    "upgrade_information": {
        "section": "Upgrade Information",
        "source_type": "release_notes_upgrade_information",
        "kind": "skip",
    },
    "aos_cx_and_netedit_compatibility_matrix": {
        "section": "AOS-CX and NetEdit Compatibility Matrix",
        "source_type": "release_notes_netedit_compatibility_matrix",
        "kind": "skip",
    },
}

COLUMN_ALIASES = {
    "bug_id": {"bug id", "bug id.", "bugid", "bug", "id", "issue id", "defect id"},
    "category": {"category", "feature area", "area", "module", "component"},
    "description": {"description", "issue description", "remarks", "remark"},
    "feature": {"feature", "component"},
    "browser": {"browser"},
    "minimum_supported_version": {
        "minimum supported versions",
        "minimum supported version",
        "minimum version",
        "supported version",
    },
    "product_number": {"product number", "product no", "product no.", "sku"},
    "product_name": {"product name", "product", "name"},
    "minimum_software_version": {"minimum software version", "minimum aos-cx version"},
    "version_number": {"version number", "version"},
    "release_date": {"release date", "date"},
    "remarks": {"remarks", "remark", "description"},
}

NOISE_PATTERNS = [
    r"^cookie preferences",
    r"^do not sell",
    r"^close$",
    r"^greenlake",
    r"^hpe resources",
    r"^legal & financial",
    r"^hpe account details",
    r"^my hpe account",
    r"^sign out$",
    r"^hpe home$",
    r"^products and solutions$",
    r"^support center$",
    r"^skip to main content",
    r"^menu toggle$",
    r"^home$",
    r"^manage$",
    r"^products$",
    r"^dashboard$",
    r"^applications$",
    r"^devices$",
    r"^english$",
    r"^\d+ result\(s\) found$",
    r"^no result found$",
    r"^table of contents$",
    r"^back to top$",
    r"^copyright",
    r"^all rights reserved",
    r"^privacy statement",
    r"^terms of use",
    r"^financial services",
]
NOISE_RE = re.compile("|".join(f"(?:{item})" for item in NOISE_PATTERNS), re.IGNORECASE)

FOOTER_NAV_PHRASES = (
    "Related Products",
    "Recently Viewed",
    "On This Page",
    "Legal Disclaimer",
    "How to buy",
    "Follow HPE on",
    "Company",
    "Support",
    "Careers",
    "Investor relations",
    "Warranty check",
    "Product return and recycling",
    "Software and drivers",
    "Feedback",
    "View more",
)
FOOTER_NAV_RE = re.compile(
    r"\b(?:" + "|".join(re.escape(phrase) for phrase in FOOTER_NAV_PHRASES) + r")\b",
    re.IGNORECASE,
)

SAFE_TEXT_REPLACEMENTS = (
    ("Symtom", "Symptom"),
    ("comand-line", "command-line"),
    ("lower-prority", "lower-priority"),
    ("werenot", "were not"),
    ("REST daemon.2", "REST daemon."),
    ("GRE.,", "GRE,"),
    ("UBTclient", "UBT client"),
    ("In the event of of", "In the event of"),
    ("in the event of of", "in the event of"),
    (" to other mobility conductor", " to another mobility conductor"),
    ("does not have a have license", "does not have a license"),
    ("Once the primary mobility conductor reachable", "Once the primary mobility conductor is reachable"),
    ("once the primary mobility conductor reachable", "once the primary mobility conductor is reachable"),
    ("can occur of a user issues", "can occur if a user issues"),
    ("best practices is", "best practice is"),
    ("depending its capability", "depending on its capability"),
    ("depending on its capability:", "depending on interface capability."),
    ("depending on its capability", "depending on interface capability"),
    ("Best practices is", "Best practice is"),
    ("with in the system", "within the system"),
)


def apply_safe_text_replacements(text: str) -> str:
    for broken, fixed in SAFE_TEXT_REPLACEMENTS:
        text = text.replace(broken, fixed)
    text = re.sub(r"\ban DUT\b", "a DUT", text)
    text = re.sub(r"\ba if\b", "if", text)
    return MALFORMED_LOGGED_OUT_RE.sub("logged out", text)


def normalize_text(text: str) -> str:
    text = (text or "").replace("\xa0", " ")
    text = text.replace("\\_", "_")
    mojibake_replacements = {
        "\u00e2\u20ac\u0090": "-",
        "\u00e2\u20ac\u0091": "-",
        "\u00e2\u20ac\u201c": "-",
        "\u00e2\u20ac\u201d": "-",
        "\u00e2\u20ac\u02dc": "'",
        "\u00e2\u20ac\u2122": "'",
        "\u00e2\u20ac\u0153": '"',
        "\u00e2\u20ac\u009d": '"',
        "\u00e2\u20ac\u00a2": "*",
    }
    for broken, fixed in mojibake_replacements.items():
        text = text.replace(broken, fixed)
    text = apply_safe_text_replacements(text)
    for dash in ("\u2010", "\u2011", "\u2012", "\u2013", "\u2014", "\u2212"):
        text = text.replace(dash, "-")
    text = text.replace(" * ", " ")
    text = text.replace(". * ", ". ")
    return WHITESPACE_RE.sub(" ", text).strip()


def cleanup_known_command_lists(text: str) -> str:
    return COMMAND_LIST_WORKAROUND_RE.sub(KNOWN_COMMAND_LIST_WORKAROUND, text)


def cleanup_user_based_tunnel_text(text: str) -> str:
    if "mobility conductor" not in text or "license" not in text:
        return text
    text = text.replace(
        "if mobility conductor does not have a license to on-board the DUT but mobility conductor. does have adequate licenses",
        "if the primary mobility conductor does not have a license to onboard the DUT but the backup mobility conductor does have adequate licenses",
    )
    text = text.replace(
        "if mobility conductor does not have a license to onboard the DUT but mobility conductor. does have adequate licenses",
        "if the primary mobility conductor does not have a license to onboard the DUT but the backup mobility conductor does have adequate licenses",
    )
    text = text.replace(
        "if mobility conductor does not have a license",
        "if the primary mobility conductor does not have a license",
    )
    text = text.replace(
        "but mobility conductor. does have adequate licenses",
        "but the backup mobility conductor does have adequate licenses",
    )
    return text.replace("on-board the DUT", "onboard the DUT")


def cleanup_tpm_quote_text(text: str) -> str:
    if "Central source connection status" not in text or "show aruba-central" not in text:
        return text
    expected = (
        'the "Central source connection status" field in the "show aruba-central" '
        'command will read "connection_failure"'
    )
    text = re.sub(
        r'the error\s+"?Central source connection status"?\s+field\s+in\s+the\s+"show aruba-central"\s+'
        r'command\s+will\s+read\s+"connection_failure"',
        expected,
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(
        r'the\s+"?Central source connection status"?\s+field\s+in\s+the\s+"show aruba-central"\s+'
        r'command\s+will\s+read\s+"connection_failure"',
        expected,
        text,
        flags=re.IGNORECASE,
    )
    return text


def normalize_label_punctuation(text: str) -> str:
    return MISSING_LABEL_PUNCTUATION_RE.sub(r". \1", text)


def final_text_cleanup(text: str) -> str:
    text = normalize_text(text)
    if not text:
        return ""

    text = text.replace(BAD_UPGRADE_PROCEDURE_ENDING, GOOD_UPGRADE_PROCEDURE_ENDING)
    text = text.replace(BAD_UPGRADE_PROCEDURE_ENDING[:-1], GOOD_UPGRADE_PROCEDURE_ENDING)

    if "PER certificate" in text and re.search(
        r"\b(certificate|corrupt certificate|upload|WebUI certificate management)\b",
        text,
        re.IGNORECASE,
    ):
        text = text.replace("PER certificate", "PEM certificate")

    replacements = (
        ("'Get'a", "'Get' a"),
        ("updated:.", "updated:"),
        ("{_}", ""),
        ("event of of", "event of"),
        ("with in the system", "within the system"),
        ("Best practices is", "Best practice is"),
        ("best practices is", "best practice is"),
        ("Once the primary mobility conductor reachable", "Once the primary mobility conductor is reachable"),
        ("once the primary mobility conductor reachable", "once the primary mobility conductor is reachable"),
        ("depending on its capability:", "depending on interface capability."),
        ("depending its capability", "depending on interface capability"),
        ("depending on its capability", "depending on interface capability"),
        ("REST daemon.2", "REST daemon."),
        ("comand-line", "command-line"),
        ("lower-prority", "lower-priority"),
        ("werenot", "were not"),
        ("have a have license", "have a license"),
    )
    for broken, fixed in replacements:
        text = text.replace(broken, fixed)

    text = re.sub(r"\ban DUT\b", "a DUT", text)
    text = re.sub(r"\ba if\b", "if", text)
    text = MALFORMED_LOGGED_OUT_RE.sub("logged out", text)
    text = cleanup_known_command_lists(text)
    text = cleanup_tpm_quote_text(text)
    text = normalize_label_punctuation(text)
    text = re.sub(r"\s+([,.;:])", r"\1", text)
    text = text.replace('" .', '".')
    return WHITESPACE_RE.sub(" ", text).strip()


def normalize_answer_punctuation(text: str) -> str:
    text = final_text_cleanup(text)
    if not text:
        return ""
    text = re.sub(r":\s*\.", ":", text)
    text = re.sub(r"\.\s+\.", ".", text)
    text = re.sub(r"(?<!\d)\.{2,}(?!\d)", ".", text)
    while text.endswith(".."):
        text = text[:-1]
    text = text.rstrip()
    if not text:
        return ""
    if text.endswith((".", "?", "!", ":", ">", ")", "]", '"')):
        return text
    if URL_END_RE.search(text) or CODE_LIKE_END_RE.search(text):
        return text
    return f"{text}."


def finalize_answer_text(text: str) -> str:
    return normalize_answer_punctuation(text)


def slug(text: str) -> str:
    text = normalize_text(text).lower().replace("&", " and ")
    text = re.sub(r"[^a-z0-9]+", "_", text)
    return text.strip("_")


def clean_inline_markdown(text: str) -> str:
    text = text or ""
    text = re.sub(r"!\[[^\]]*]\([^)]+\)", "", text)
    text = re.sub(r"\[([^\]]+)]\(([^)]+)\)", r"\1 (\2)", text)
    text = text.replace("**", "").replace("__", "").replace("`", "")
    text = text.replace("<br>", " ").replace("<br/>", " ").replace("<br />", " ")
    text = text.replace("&nbsp;", " ").replace("&amp;", "&")
    text = re.sub(r"\b(Symptom|Symtom|Scenario|Workaround):(?=\S)", r"\1: ", text, flags=re.IGNORECASE)
    return normalize_text(text.strip(" \t|"))


def is_noise_line(line: str) -> bool:
    cleaned = clean_inline_markdown(line).strip(" -*+#")
    if not cleaned:
        return True
    if NOISE_RE.search(cleaned):
        return True
    if cleaned.startswith("[") and "support.hpe.com" in cleaned.lower():
        return True
    return False


def contains_footer_navigation(text: str) -> bool:
    return bool(FOOTER_NAV_RE.search(normalize_text(text)))


def clean_markdown(text: str) -> str:
    lines: list[str] = []
    previous = ""
    for raw_line in (text or "").splitlines():
        line = raw_line.rstrip()
        if is_noise_line(line):
            continue
        normalized_line = normalize_text(line)
        if normalized_line and normalized_line == previous:
            continue
        lines.append(line)
        previous = normalized_line
    return "\n".join(lines).strip()


def discover_md_files(input_root: Path) -> list[Path]:
    return sorted(
        path
        for path in Path(input_root).rglob("*.md")
        if path.is_file()
        and ".venv" not in path.parts
        and ".markitdown_venv" not in path.parts
        and ".markitdown_venv312" not in path.parts
    )


def classify_section(file_path: Path, markdown_text: str) -> dict[str, Any]:
    file_key = slug(file_path.stem)
    heading_text = " ".join(
        clean_inline_markdown(line.lstrip("# "))
        for line in markdown_text.splitlines()
        if line.lstrip().startswith("#")
    )
    haystack = slug(f"{file_key} {heading_text}")
    for key, rule in sorted(SECTION_DEFS.items(), key=lambda item: len(item[0]), reverse=True):
        if file_key == key or file_key.startswith(f"{key}_") or key in haystack:
            return {"key": key, **rule}
    return {
        "key": file_key,
        "section": file_path.stem.replace("_", " ").strip().title(),
        "source_type": "release_notes_unclassified",
        "kind": "unclassified",
    }


def split_table_line(line: str) -> list[str]:
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    cells: list[str] = []
    current: list[str] = []
    escaped = False
    for char in line:
        if char == "\\" and not escaped:
            escaped = True
            current.append(char)
            continue
        if char == "|" and not escaped:
            cells.append(clean_inline_markdown("".join(current)))
            current = []
            continue
        current.append(char)
        escaped = False
    cells.append(clean_inline_markdown("".join(current)))
    return cells


def is_table_separator(line: str) -> bool:
    cells = split_table_line(line)
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell.strip()) for cell in cells if cell.strip())


def normalize_column_name(name: str) -> str:
    key = slug(name).replace("_", " ").strip()
    for canonical, aliases in COLUMN_ALIASES.items():
        if key in aliases:
            return canonical
    return slug(name)


def parse_markdown_tables(text: str) -> list[dict[str, Any]]:
    lines = text.splitlines()
    tables: list[dict[str, Any]] = []
    index = 0
    while index < len(lines) - 1:
        if "|" not in lines[index] or not is_table_separator(lines[index + 1]):
            index += 1
            continue
        raw_headers = split_table_line(lines[index])
        headers = [normalize_column_name(header) for header in raw_headers]
        rows: list[dict[str, str]] = []
        index += 2
        while index < len(lines) and "|" in lines[index].strip():
            if is_table_separator(lines[index]):
                index += 1
                continue
            cells = split_table_line(lines[index])
            if len(cells) > len(headers):
                cells = cells[: len(headers) - 1] + [" | ".join(cells[len(headers) - 1 :])]
            while len(cells) < len(headers):
                cells.append("")
            row = {headers[pos]: cells[pos] for pos in range(len(headers)) if headers[pos]}
            if any(value for value in row.values()):
                rows.append(row)
            index += 1
        tables.append({"headers": headers, "rows": rows})
    return tables


def cell(row: dict[str, str], *names: str) -> str:
    for name in names:
        value = row.get(name, "")
        if value:
            return clean_inline_markdown(value)
    return ""


def is_valid_bug_id(value: str) -> bool:
    return bool(re.fullmatch(r"\d{5,7}", value or "")) and value not in FAKE_BUG_IDS


def sentence(text: str) -> str:
    return normalize_answer_punctuation(text)


def lower_first(text: str) -> str:
    text = final_text_cleanup(text)
    if not text:
        return ""
    return text[0].lower() + text[1:]


def parse_bug_description(description: str) -> dict[str, str]:
    original = clean_inline_markdown(description)
    result = {
        "description": original,
        "symptom": "",
        "scenario": "",
        "workaround": "",
    }
    matches = list(LABEL_RE.finditer(original))
    if not matches:
        return result
    for pos, match in enumerate(matches):
        label = match.group("label").lower()
        if label == "symtom":
            label = "symptom"
        start = match.end()
        end = matches[pos + 1].start() if pos + 1 < len(matches) else len(original)
        value = normalize_text(original[start:end].strip(" :-;|"))
        if label in result and value:
            result[label] = value
    return result


def base_record(meta: dict[str, str], section: dict[str, Any], source_file: Path) -> dict[str, Any]:
    return {
        "source_type": section["source_type"],
        "switch": meta["switch"],
        "version": meta["version"],
        "sub_version": meta["sub_version"],
        "section": section["section"],
        "source_file": str(source_file),
    }


def parse_bug_table(
    tables: list[dict[str, Any]],
    meta: dict[str, str],
    section: dict[str, Any],
    source_file: Path,
) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for table in tables:
        headers = set(table["headers"])
        if not {"category", "bug_id", "description"}.issubset(headers):
            continue
        for row in table["rows"]:
            category = cell(row, "category", "feature")
            bug_id_match = BUG_ID_RE.search(cell(row, "bug_id", "id"))
            bug_id = bug_id_match.group(0) if bug_id_match else ""
            description = cell(row, "description", "remarks")
            parsed = parse_bug_description(description)
            record = {
                **base_record(meta, section, source_file),
                "category": category,
                "bug_id": bug_id,
                **parsed,
            }
            records.append(record)
    return records


def parse_feature_caveats(
    tables: list[dict[str, Any]], meta: dict[str, str], section: dict[str, Any], source_file: Path
) -> list[dict[str, Any]]:
    records = []
    for table in tables:
        if "feature" not in table["headers"]:
            continue
        for row in table["rows"]:
            feature = cell(row, "feature")
            description = cell(row, "description", "remarks")
            if feature or description:
                records.append(
                    {
                        **base_record(meta, section, source_file),
                        "feature": feature,
                        "description": description,
                    }
                )
    return records


def parse_compatibility(
    tables: list[dict[str, Any]], meta: dict[str, str], section: dict[str, Any], source_file: Path
) -> list[dict[str, Any]]:
    records = []
    for table in tables:
        if "browser" not in table["headers"]:
            continue
        for row in table["rows"]:
            records.append(
                {
                    **base_record(meta, section, source_file),
                    "browser": cell(row, "browser"),
                    "minimum_supported_version": cell(row, "minimum_supported_version"),
                }
            )
    return records


def parse_products_supported(
    tables: list[dict[str, Any]], meta: dict[str, str], section: dict[str, Any], source_file: Path
) -> list[dict[str, Any]]:
    records = []
    for table in tables:
        if "product_number" not in table["headers"]:
            continue
        for row in table["rows"]:
            product_name = cell(row, "product_name")
            if not product_name and "description" in row:
                product_name = cell(row, "description")
            records.append(
                {
                    **base_record(meta, section, source_file),
                    "product_number": cell(row, "product_number"),
                    "product_name": product_name,
                    "minimum_software_version": cell(row, "minimum_software_version"),
                }
            )
    return records


def parse_version_history(
    tables: list[dict[str, Any]], meta: dict[str, str], section: dict[str, Any], source_file: Path
) -> list[dict[str, Any]]:
    records = []
    for table in tables:
        if "version_number" not in table["headers"]:
            continue
        for row in table["rows"]:
            records.append(
                {
                    **base_record(meta, section, source_file),
                    "version_number": cell(row, "version_number"),
                    "release_date": cell(row, "release_date"),
                    "remarks": cell(row, "remarks", "description"),
                }
            )
    return records


def remove_table_blocks(text: str) -> str:
    output: list[str] = []
    in_table = False
    for line in text.splitlines():
        if "|" in line and line.strip().startswith("|"):
            in_table = True
            continue
        if in_table and "|" in line:
            continue
        in_table = False
        output.append(line)
    return "\n".join(output)


def meaningful_lines(text: str) -> list[str]:
    cleaned = remove_table_blocks(clean_markdown(text))
    lines = []
    for raw in cleaned.splitlines():
        line = clean_inline_markdown(raw.lstrip("#>").strip())
        line = re.sub(r"^\s*[-+*]\s+", "", line)
        if len(line) < 3 or is_noise_line(line):
            continue
        if line.lower().startswith("http"):
            continue
        lines.append(line)
    return lines


def find_section_start(lines: list[str], section_title: str) -> int:
    section_key = slug(section_title)
    best = 0
    for index, line in enumerate(lines):
        line_key = slug(line)
        if line_key == section_key or section_key in line_key:
            best = index + 1
    return best


def find_exact_heading(lines: list[str], title: str) -> int:
    target = slug(title)
    for index, raw_line in enumerate(lines):
        stripped = raw_line.strip()
        if not stripped.startswith("#"):
            continue
        heading = clean_inline_markdown(stripped.lstrip("#").strip())
        if slug(heading) == target:
            return index
    return -1


def procedure_block_lines(text: str, section_title: str) -> list[str]:
    lines = clean_markdown(text).splitlines()
    heading_index = find_exact_heading(lines, section_title)
    if heading_index < 0:
        return []

    in_procedure = False
    block: list[str] = []
    for raw_line in lines[heading_index + 1 :]:
        stripped = raw_line.strip()
        cleaned = clean_inline_markdown(stripped.lstrip("#>").strip())
        if not cleaned:
            continue
        if contains_footer_navigation(cleaned):
            break
        if stripped.startswith("#"):
            heading_key = slug(cleaned)
            if heading_key == "procedure":
                in_procedure = True
                continue
            if heading_key in {"about_this_task"}:
                in_procedure = False
                continue
            if heading_key in {"results", "related_products", "recently_viewed", "on_this_page"}:
                break
            if in_procedure:
                break
            continue
        if in_procedure:
            block.append(raw_line)
    return block


def extract_ordered_or_bulleted_steps(lines: list[str]) -> list[str]:
    numbered_steps: list[tuple[int, str]] = []
    bullet_steps: list[str] = []
    in_code_block = False
    for raw_line in lines:
        stripped = raw_line.strip()
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue
        cleaned = clean_inline_markdown(stripped)
        if not cleaned or contains_footer_navigation(cleaned):
            continue
        is_top_level = raw_line == raw_line.lstrip()
        numbered = re.match(r"^(\d+)[.)]\s+(.+)$", cleaned) if is_top_level else None
        if numbered:
            numbered_steps.append((int(numbered.group(1)), sentence(numbered.group(2))))
            continue
        bullet = re.match(r"^[-+*]\s+(.+)$", cleaned) if is_top_level else None
        if bullet:
            bullet_steps.append(sentence(bullet.group(1)))
    if numbered_steps:
        return [step for _, step in sorted(numbered_steps, key=lambda item: item[0])]
    return bullet_steps


def parse_procedure_page(
    text: str, meta: dict[str, str], section: dict[str, Any], source_file: Path
) -> list[dict[str, Any]]:
    block = procedure_block_lines(text, section["section"])
    procedure = extract_ordered_or_bulleted_steps(block)
    if not procedure:
        return []
    return [
        {
            **base_record(meta, section, source_file),
            "task": section["section"],
            "procedure": procedure,
            "description": " ".join(procedure),
        }
    ]


def parse_certifications(
    text: str, meta: dict[str, str], section: dict[str, Any], source_file: Path
) -> list[dict[str, Any]]:
    lines = meaningful_lines(text)
    start = find_section_start(lines, section["section"])
    body = lines[start:]
    useful = [
        line
        for line in body
        if any(token.lower() in line.lower() for token in ("Common Criteria", "FIPS", "DoDIN", "Approved Product"))
    ]
    if not useful:
        useful = body[:6]
    content = normalize_text(" ".join(useful))
    links = re.findall(r"https?://[^\s)]+", text)
    if not content:
        return []
    return [
        {
            **base_record(meta, section, source_file),
            "content": content,
            "links": sorted(set(links)),
        }
    ]


def parse_license_written_offer(
    text: str, meta: dict[str, str], section: dict[str, Any], source_file: Path
) -> list[dict[str, Any]]:
    lines = meaningful_lines(text)
    start = find_section_start(lines, section["section"])
    content = normalize_text(" ".join(lines[start:]))
    if not content:
        return []
    return [
        {
            **base_record(meta, section, source_file),
            "content": content,
        }
    ]


def parse_records_from_file(
    file_path: Path, markdown_text: str, meta: dict[str, str]
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    cleaned = clean_markdown(markdown_text)
    section = classify_section(file_path, cleaned)
    tables = parse_markdown_tables(cleaned)
    kind = section["kind"]
    if kind == "bug":
        records = parse_bug_table(tables, meta, section, file_path)
    elif kind == "feature_caveats":
        records = parse_feature_caveats(tables, meta, section, file_path)
    elif kind == "compatibility":
        records = parse_compatibility(tables, meta, section, file_path)
    elif kind == "products":
        records = parse_products_supported(tables, meta, section, file_path)
    elif kind == "version_history":
        records = parse_version_history(tables, meta, section, file_path)
    elif kind in {"downgrade_restore", "upgrade_procedure"}:
        records = parse_procedure_page(cleaned, meta, section, file_path)
    elif kind == "certifications":
        records = parse_certifications(cleaned, meta, section, file_path)
    elif kind == "license":
        records = parse_license_written_offer(cleaned, meta, section, file_path)
    elif kind == "skip":
        records = []
    else:
        records = []
    return records, {"section": section["section"], "kind": kind, "tables": len(tables)}


def validate_record(record: dict[str, Any]) -> tuple[bool, str]:
    section = record.get("section", "")
    source_type = record.get("source_type", "")
    if source_type in {"release_notes_known_issues", "release_notes_resolved_issues"}:
        if not record.get("category"):
            return False, "bug_missing_category"
        if not is_valid_bug_id(str(record.get("bug_id", ""))):
            return False, "fake_or_invalid_bug_id"
        if not record.get("description"):
            return False, "bug_missing_description"
    elif source_type == "release_notes_caveats":
        if not record.get("feature") or not record.get("description"):
            return False, "caveat_missing_required_field"
    elif source_type == "release_notes_compatibility":
        if not record.get("browser") or not record.get("minimum_supported_version"):
            return False, "compatibility_missing_required_field"
    elif source_type == "release_notes_supported_products":
        if not record.get("product_number") or not record.get("product_name") or not record.get("minimum_software_version"):
            return False, "product_missing_required_field"
    elif source_type == "release_notes_version_history":
        if not record.get("version_number") or not record.get("release_date"):
            return False, "version_history_missing_required_field"
    elif source_type in {"release_notes_downgrade_restore", "release_notes_upgrade_procedure"}:
        if not record.get("task") or not record.get("procedure"):
            return False, "procedure_missing_required_field"
        if any(contains_footer_navigation(step) for step in record.get("procedure", [])):
            return False, "procedure_contains_navigation_footer"
    elif source_type == "release_notes_certifications":
        if not record.get("content"):
            return False, "certification_missing_content"
    elif source_type == "legal_license":
        if not record.get("content"):
            return False, "license_missing_content"
    else:
        return False, f"unhandled_section:{section}"
    return True, "kept"


TEXT_CLEANUP_FIELDS = {
    "description",
    "symptom",
    "scenario",
    "workaround",
    "feature",
    "browser",
    "product_name",
    "remarks",
    "content",
}


def normalize_category_casing(category: Any) -> tuple[str, bool]:
    normalized = normalize_text(str(category or ""))
    if normalized in CATEGORY_CASE_VARIANTS:
        return CATEGORY_CASE_VARIANTS[normalized], True
    return normalized, False


def cleanup_record_text(record: dict[str, Any]) -> tuple[dict[str, Any], Counter]:
    cleaned = dict(record)
    counts: Counter = Counter()

    if "category" in cleaned:
        category, changed = normalize_category_casing(cleaned.get("category"))
        if changed:
            counts["category_case_normalized"] += 1
        cleaned["category"] = category

    for field in TEXT_CLEANUP_FIELDS:
        value = cleaned.get(field)
        if not isinstance(value, str):
            continue
        command_match = bool(COMMAND_LIST_WORKAROUND_RE.search(value))
        new_value = final_text_cleanup(value)
        is_ubt_context = (
            normalized_key_text(cleaned.get("feature")) == "user based tunnel"
            or ("mobility conductor" in new_value and "license" in new_value)
        )
        if is_ubt_context:
            new_value = cleanup_user_based_tunnel_text(new_value)
        if new_value != value:
            counts["typo_cleanup_applied"] += 1
            counts["final_cleanup_applied_count"] += 1
        if command_match and new_value != value:
            counts["command_list_cleanup_applied"] += 1
        cleaned[field] = new_value

    if isinstance(cleaned.get("procedure"), list):
        new_steps: list[str] = []
        procedure_changed = False
        for step in cleaned["procedure"]:
            step_text = str(step)
            command_match = bool(COMMAND_LIST_WORKAROUND_RE.search(step_text))
            new_step = final_text_cleanup(step_text)
            if new_step != step_text:
                counts["typo_cleanup_applied"] += 1
                counts["final_cleanup_applied_count"] += 1
                procedure_changed = True
            if command_match and new_step != step_text:
                counts["command_list_cleanup_applied"] += 1
            new_steps.append(new_step)
        cleaned["procedure"] = new_steps
        if procedure_changed and cleaned.get("source_type") in {
            "release_notes_downgrade_restore",
            "release_notes_upgrade_procedure",
        }:
            new_description = final_text_cleanup(" ".join(new_steps))
            if new_description != cleaned.get("description"):
                counts["typo_cleanup_applied"] += 1
                counts["final_cleanup_applied_count"] += 1
            cleaned["description"] = new_description

    return cleaned, counts


def metadata_payload(record: dict[str, Any]) -> dict[str, Any]:
    allowed = {
        "source_type",
        "switch",
        "version",
        "sub_version",
        "section",
        "category",
        "bug_id",
        "description",
        "symptom",
        "scenario",
        "workaround",
        "feature",
        "browser",
        "minimum_supported_version",
        "product_number",
        "product_name",
        "minimum_software_version",
        "version_number",
        "release_date",
        "remarks",
        "task",
        "procedure",
        "topic",
    }
    return {key: value for key, value in record.items() if key in allowed and value not in ("", None, [])}


def qa_row(record: dict[str, Any], question: str, answer: str) -> dict[str, Any]:
    return {
        **metadata_payload(record),
        "messages": [
            {"role": "user", "content": normalize_text(question)},
            {"role": "assistant", "content": finalize_answer_text(answer)},
        ],
    }


def release_version_display(record: dict[str, Any]) -> str:
    version = normalize_text(str(record.get("version", ""))).replace("_", ".")
    sub_version = normalize_text(str(record.get("sub_version", ""))).replace("_", ".")
    if version and sub_version:
        return f"{version}.{sub_version}"
    return version or sub_version


def has_question_grounding(question: str) -> bool:
    return bool(QUESTION_GROUNDING_RE.match(normalize_text(question)))


def ground_question_with_version(row: dict[str, Any]) -> dict[str, Any]:
    messages = row.get("messages", [])
    if not isinstance(messages, list) or len(messages) != 2:
        return row
    question = normalize_text(messages[0].get("content", ""))
    if not question or has_question_grounding(question):
        return row
    switch = normalize_text(str(row.get("switch", "")))
    version_display = release_version_display(row)
    if not switch or not version_display:
        return row
    grounded = f"For {switch} AOS-CX {version_display}, {lower_first(question)}"
    new_row = dict(row)
    new_messages = [dict(messages[0]), dict(messages[1])]
    new_messages[0]["content"] = normalize_text(grounded)
    new_row["messages"] = new_messages
    return new_row


def normalize_for_exact_qa_dedupe(value: Any) -> str:
    return WHITESPACE_RE.sub(" ", str(value or "").strip()).casefold()


def exact_qa_dedupe_key(row: dict[str, Any]) -> str:
    messages = row.get("messages", [{}, {}])
    question = messages[0].get("content", "") if len(messages) > 0 else ""
    answer = messages[1].get("content", "") if len(messages) > 1 else ""
    return f"{normalize_for_exact_qa_dedupe(question)}||{normalize_for_exact_qa_dedupe(answer)}"


def bug_prefix(record: dict[str, Any]) -> str:
    return f"{record['category']} (Bug ID {record['bug_id']}):"


def generate_bug_qa(record: dict[str, Any], max_qa_per_bug: int = 5) -> list[dict[str, Any]]:
    prefix = bug_prefix(record)
    category = record["category"]
    bug_id = record["bug_id"]
    if record["source_type"] == "release_notes_known_issues":
        summary_q = f"What known issue is documented for {category} Bug {bug_id}?"
    else:
        summary_q = f"What issue was resolved in {category} Bug {bug_id}?"
    rows = [
        qa_row(record, summary_q, f"{prefix} {sentence(record['description'])}"),
    ]
    if record["source_type"] == "release_notes_known_issues":
        rows.append(
            qa_row(record, f"Which category is affected by Bug {bug_id}?", f"{prefix} This bug affects the {category} category.")
        )
    else:
        rows.append(
            qa_row(record, f"Which category does Bug {bug_id} belong to?", f"{prefix} This bug belongs to the {category} category.")
        )
    if record.get("symptom"):
        rows.append(
            qa_row(
                record,
                f"What symptom occurs in {category} Bug {bug_id}?",
                f"{prefix} The symptom is: {sentence(record['symptom'])}",
            )
        )
    if record.get("scenario"):
        rows.append(
            qa_row(
                record,
                f"Under what scenario does {category} Bug {bug_id} occur?",
                f"{prefix} {sentence(record['scenario'])}",
            )
        )
    if record.get("workaround"):
        rows.append(
            qa_row(
                record,
                f"What is the workaround for {category} Bug {bug_id}?",
                f"{prefix} The documented workaround is: {sentence(record['workaround'])}",
            )
        )
    else:
        rows.append(
            qa_row(
                record,
                f"What is the workaround for {category} Bug {bug_id}?",
                f"{prefix} No workaround is documented in the release notes.",
            )
        )
    limit = max(0, min(int(max_qa_per_bug), 5))
    return rows[:limit]


def ordered_procedure_text(steps: list[str]) -> str:
    return " ".join(f"{index}. {sentence(step)}" for index, step in enumerate(steps, start=1))


def caveat_question(feature: str, occurrence: int) -> str:
    if occurrence == 1:
        return f"What caveat is documented for {feature}?"
    if occurrence == 2:
        return f"What limitation is mentioned for {feature}?"
    return f"What additional caveat is documented for {feature}?"


def generate_qa(
    record: dict[str, Any],
    include_legal: bool = False,
    caveat_occurrence: int = 1,
    max_qa_per_bug: int = 5,
) -> list[dict[str, Any]]:
    source_type = record.get("source_type")
    if source_type in {"release_notes_known_issues", "release_notes_resolved_issues"}:
        return generate_bug_qa(record, max_qa_per_bug=max_qa_per_bug)
    if source_type == "release_notes_caveats":
        answer = f"Feature Caveat: {record['feature']} - {sentence(record['description'])}"
        return [
            qa_row(record, caveat_question(record["feature"], caveat_occurrence), answer),
        ]
    if source_type == "release_notes_compatibility":
        answer = (
            f"Compatibility: {record['browser']} requires minimum supported version "
            f"{record['minimum_supported_version']}."
        )
        return [
            qa_row(record, f"What is the minimum supported version for {record['browser']}?", answer),
            qa_row(record, f"Which version of {record['browser']} is supported?", answer),
        ]
    if source_type == "release_notes_supported_products":
        answer = (
            f"Supported Product: {record['product_number']} - {record['product_name']} "
            f"requires minimum software version {record['minimum_software_version']}."
        )
        return [
            qa_row(record, f"What product is listed for product number {record['product_number']}?", answer),
            qa_row(record, f"What is the minimum software version for {record['product_name']}?", answer),
            qa_row(record, f"Which minimum software version is required for {record['product_number']}?", answer),
        ]
    if source_type == "release_notes_version_history":
        answer = (
            f"Version History: Version {record['version_number']} was released on "
            f"{record['release_date']}. Remarks: {record.get('remarks', '')}."
        )
        return [
            qa_row(record, f"When was version {record['version_number']} released?", answer),
            qa_row(record, f"What remarks are listed for version {record['version_number']}?", answer),
        ]
    if source_type == "release_notes_downgrade_restore":
        steps = record.get("procedure", [])
        answer = (
            "Downgrade Restore: To restore configuration after a software downgrade, "
            f"follow the documented procedure in order: {ordered_procedure_text(steps)}"
        )
        return [
            qa_row(record, "How do you restore configuration after a software downgrade?", answer),
            qa_row(record, "What is the manual configuration restore procedure for software downgrade?", answer),
        ]
    if source_type == "release_notes_upgrade_procedure":
        steps = record.get("procedure", [])
        answer = (
            "Upgrade Procedure: To perform the software upgrade, follow the documented "
            f"procedure in order: {ordered_procedure_text(steps)}"
        )
        return [
            qa_row(record, "How do you perform the software upgrade?", answer),
            qa_row(record, "What are the steps to perform the software upgrade?", answer),
        ]
    if source_type == "release_notes_certifications":
        content = sentence(record["content"])
        answer = f"Certification: {content}"
        return [
            qa_row(record, "Where can product certification details be found?", answer),
            qa_row(record, "Which certification references are mentioned in the release notes?", answer),
        ]
    if source_type == "legal_license" and include_legal:
        answer = (
            "License Written Offer: This product includes code licensed under the GNU "
            "General Public License, the GNU Lesser General Public License, and other "
            "open-source licenses. A complete machine-readable copy of the corresponding "
            "source code is available upon request from Hewlett Packard Enterprise as "
            "described in the written offer."
        )
        return [qa_row(record, "What does the license written offer state?", answer)]
    return []


def word_count(text: str) -> int:
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9_.-]*", text or ""))


def has_double_period(text: str) -> bool:
    return bool(re.search(r"(?<!\d)\.\s*\.(?!\d)", text or ""))


def final_cleanup_issue_counts(text: str) -> Counter:
    text = text or ""
    counts: Counter = Counter()
    if re.search(r"\bll+ogged\b", text, re.IGNORECASE):
        counts["malformed_logged_out_count"] += 1
    if MALFORMED_REPEATED_LETTERS_RE.search(text):
        counts["malformed_repeated_letters_count"] += 1
    if BROKEN_MOBILITY_CONDUCTOR_RE.search(text):
        counts["broken_mobility_conductor_count"] += 1
    if BROKEN_TPM_QUOTE_RE.search(text):
        counts["broken_tpm_quote_count"] += 1
    if MISSING_LABEL_PUNCTUATION_RE.search(text):
        counts["missing_symptom_scenario_punctuation_count"] += 1
    if "{_}" in text:
        counts["bad_markup_remaining"] += 1
    return counts


def bad_output_patterns_in_answer(text: str) -> list[str]:
    found = [pattern for pattern in BAD_OUTPUT_PATTERNS if pattern in (text or "")]
    found.extend(final_cleanup_issue_counts(text).keys())
    return found


def validate_qa_row(row: dict[str, Any]) -> tuple[bool, str]:
    messages = row.get("messages")
    if not isinstance(messages, list) or len(messages) != 2:
        return False, "invalid_messages"
    if messages[0].get("role") != "user" or messages[1].get("role") != "assistant":
        return False, "invalid_message_roles"
    question = normalize_text(messages[0].get("content", ""))
    answer = finalize_answer_text(messages[1].get("content", ""))
    if not question or not answer:
        return False, "empty_question_or_answer"
    if PLACEHOLDER_INLINE_RE.search(answer):
        return False, "placeholder_answer"
    if has_double_period(answer):
        return False, "double_period_answer"
    if bad_output_patterns_in_answer(answer):
        return False, "bad_output_pattern"
    if answer.lower().strip(" .") in {"n/a", "unknown", "tbd"}:
        return False, "invalid_whole_answer"
    simple = row.get("source_type") in {
        "release_notes_compatibility",
        "release_notes_supported_products",
        "release_notes_version_history",
    }
    if not simple and word_count(answer) < 8:
        return False, "short_answer"
    if row.get("bug_id") and not is_valid_bug_id(str(row["bug_id"])):
        return False, "fake_or_invalid_bug_id"
    return True, "kept"


def normalized_key_text(value: Any) -> str:
    return normalize_text(str(value or "")).casefold()


def bug_question_type(row: dict[str, Any]) -> str:
    question = normalized_key_text(row.get("messages", [{}])[0].get("content", ""))
    if question.startswith("what issue was resolved") or question.startswith("what known issue is documented"):
        return "summary"
    if question.startswith("which category"):
        return "category"
    if question.startswith("what symptom occurs"):
        return "symptom"
    if question.startswith("under what scenario"):
        return "scenario"
    if "workaround" in question:
        return "workaround"
    return question or "unknown"


def qa_dedupe_key(row: dict[str, Any]) -> tuple[Any, ...]:
    source_type = str(row.get("source_type", ""))
    if source_type == "release_notes_caveats":
        return (
            "caveat",
            normalized_key_text(row.get("switch")),
            normalized_key_text(source_type),
            normalized_key_text(row.get("feature")),
            normalized_key_text(row.get("description")),
        )
    if source_type == "release_notes_supported_products":
        return (
            "product",
            normalized_key_text(row.get("switch")),
            normalized_key_text(row.get("product_number")),
            normalized_key_text(row.get("product_name")),
            normalized_key_text(row.get("minimum_software_version")),
        )
    if source_type == "release_notes_compatibility":
        return (
            "compatibility",
            normalized_key_text(row.get("switch")),
            normalized_key_text(row.get("browser")),
            normalized_key_text(row.get("minimum_supported_version")),
        )
    if source_type == "release_notes_version_history":
        return (
            "version_history",
            normalized_key_text(row.get("switch")),
            normalized_key_text(row.get("version_number")),
            normalized_key_text(row.get("release_date")),
            normalized_key_text(row.get("remarks")),
        )
    if source_type in {"release_notes_known_issues", "release_notes_resolved_issues"}:
        return (
            "bug",
            normalized_key_text(row.get("switch")),
            normalized_key_text(row.get("version")),
            normalized_key_text(row.get("sub_version")),
            normalized_key_text(row.get("section")),
            normalized_key_text(row.get("bug_id")),
            bug_question_type(row),
        )
    messages = row.get("messages", [{}, {}])
    question = messages[0].get("content", "") if len(messages) > 0 else ""
    answer = messages[1].get("content", "") if len(messages) > 1 else ""
    return (
        "transcript",
        normalized_key_text(row.get("switch")),
        normalized_key_text(row.get("version")),
        normalized_key_text(row.get("sub_version")),
        normalized_key_text(source_type),
        normalized_key_text(question),
        normalized_key_text(answer),
    )


def dedupe_qa_rows(rows: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], Counter]:
    kept: list[dict[str, Any]] = []
    keys: set[str] = set()
    drops: Counter = Counter()
    for row in rows:
        key = exact_qa_dedupe_key(row)
        if key in keys:
            drops["exact_qa_duplicate"] += 1
            continue
        keys.add(key)
        kept.append(row)
    return kept, drops


def write_jsonl(rows: list[dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            messages = row.get("messages", [])
            if isinstance(messages, list) and len(messages) == 2:
                messages[0]["content"] = normalize_text(messages[0].get("content", ""))
                messages[1]["content"] = finalize_answer_text(messages[1].get("content", ""))
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def write_quality_report(report: dict[str, Any], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")


def write_json(payload: Any, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


def run(args: argparse.Namespace) -> dict[str, Any]:
    input_root = Path(args.input_root)
    output_dir = Path(args.output_root) / args.switch_name / args.version / args.sub_version
    final_jsonl = Path(args.final_jsonl) if args.final_jsonl else Path("final_json") / args.switch_name / args.version / "train_chat.jsonl"
    meta = {"switch": args.switch_name, "version": args.version, "sub_version": args.sub_version}

    md_files = discover_md_files(input_root)
    report: dict[str, Any] = {
        "input_files": len(md_files),
        "sections_processed": Counter(),
        "rows_extracted_by_section": Counter(),
        "qa_generated_by_section": Counter(),
        "qa_kept_by_section": Counter(),
        "qa_dropped_by_section": Counter(),
        "drop_reasons": Counter(),
        "unique_bug_ids": set(),
        "fake_bug_ids_removed": 0,
        "duplicates_removed": 0,
        "double_period_answers": 0,
        "bad_markup_remaining": 0,
        "typo_cleanup_applied": 0,
        "procedure_noise_rows_dropped": 0,
        "section_counts": Counter(),
        "qa_counts_by_source_type": Counter(),
        "qa_counts_by_source_type_before": Counter(),
        "qa_counts_by_source_type_after": Counter(),
        "category_case_normalized": 0,
        "command_list_cleanup_applied": 0,
        "malformed_logged_out_count": 0,
        "malformed_repeated_letters_count": 0,
        "broken_mobility_conductor_count": 0,
        "broken_tpm_quote_count": 0,
        "missing_symptom_scenario_punctuation_count": 0,
        "final_cleanup_applied_count": 0,
        "total_rows_before_dedup": 0,
        "total_rows_after_dedup": 0,
        "global_exact_qa_duplicates_removed": 0,
        "generic_rows_before_cap": 0,
        "generic_rows_after_cap": 0,
        "generic_rows_removed_by_cap": 0,
        "question_grounding_enabled": bool(args.ground_questions_with_version),
        "rows_with_switch_version_in_question": 0,
        "question_grounding_ratio": 0.0,
        "warnings": [],
        "output_paths": {},
    }

    records: list[dict[str, Any]] = []
    for md_file in md_files:
        text = md_file.read_text(encoding="utf-8", errors="replace")
        parsed_records, file_info = parse_records_from_file(md_file, text, meta)
        section = file_info["section"]
        report["sections_processed"][section] += 1
        if not parsed_records and file_info["kind"] in {"downgrade_restore", "upgrade_procedure"}:
            report["warnings"].append(f"No real procedure steps found in {md_file}")
        elif not parsed_records and file_info["kind"] not in {"unclassified", "skip"}:
            report["warnings"].append(f"No records extracted from {md_file}")
        if file_info["kind"] == "unclassified":
            report["warnings"].append(f"Unclassified markdown file skipped: {md_file}")
        for record in parsed_records:
            record, cleanup_counts = cleanup_record_text(record)
            for key, count in cleanup_counts.items():
                report[key] += count
            valid, reason = validate_record(record)
            if not valid:
                report["drop_reasons"][reason] += 1
                if reason == "fake_or_invalid_bug_id":
                    report["fake_bug_ids_removed"] += 1
                if reason == "procedure_contains_navigation_footer":
                    report["procedure_noise_rows_dropped"] += 1
                continue
            records.append(record)
            report["rows_extracted_by_section"][record["section"]] += 1
            report["section_counts"][record["section"]] += 1
            if record.get("bug_id"):
                report["unique_bug_ids"].add(record["bug_id"])

    generated_rows: list[dict[str, Any]] = []
    caveat_occurrences: Counter[str] = Counter()
    for record in records:
        caveat_occurrence = 1
        if record.get("source_type") == "release_notes_caveats":
            caveat_key = normalized_key_text(record.get("feature"))
            caveat_occurrences[caveat_key] += 1
            caveat_occurrence = caveat_occurrences[caveat_key]
        rows = generate_qa(
            record,
            include_legal=args.include_legal,
            caveat_occurrence=caveat_occurrence,
            max_qa_per_bug=args.max_qa_per_bug,
        )
        generated_rows.extend(rows)
        report["qa_generated_by_section"][record["section"]] += len(rows)

    if args.ground_questions_with_version:
        generated_rows = [ground_question_with_version(row) for row in generated_rows]

    valid_rows: list[dict[str, Any]] = []
    for row in generated_rows:
        report["qa_counts_by_source_type_before"][row.get("source_type", "")] += 1
        valid, reason = validate_qa_row(row)
        if valid:
            valid_rows.append(row)
        else:
            report["drop_reasons"][reason] += 1
            report["qa_dropped_by_section"][row.get("section", "")] += 1

    report["total_rows_before_dedup"] = len(valid_rows)
    kept_rows, duplicate_drops = dedupe_qa_rows(valid_rows)
    report["total_rows_after_dedup"] = len(kept_rows)
    report["duplicates_removed"] = sum(duplicate_drops.values())
    report["global_exact_qa_duplicates_removed"] = sum(duplicate_drops.values())
    for reason, count in duplicate_drops.items():
        report["drop_reasons"][reason] += count

    for row in kept_rows:
        report["qa_kept_by_section"][row.get("section", "")] += 1
        report["qa_counts_by_source_type"][row.get("source_type", "")] += 1
        report["qa_counts_by_source_type_after"][row.get("source_type", "")] += 1
        question = row.get("messages", [{}])[0].get("content", "")
        if has_question_grounding(question):
            report["rows_with_switch_version_in_question"] += 1
        answer = row.get("messages", [{}, {}])[1].get("content", "")
        if has_double_period(answer):
            report["double_period_answers"] += 1
        bad_patterns = bad_output_patterns_in_answer(answer)
        if bad_patterns:
            report["bad_markup_remaining"] += 1
            report["warnings"].append(
                f"Bad cleanup pattern(s) remain in answer for {row.get('source_type', '')}: {', '.join(bad_patterns)}"
            )
        row_text = json.dumps(row, ensure_ascii=False)
        for issue_name, issue_count in final_cleanup_issue_counts(row_text).items():
            if issue_name == "bad_markup_remaining":
                continue
            report[issue_name] += issue_count
            report["warnings"].append(
                f"Final cleanup issue remains in row for {row.get('source_type', '')}: {issue_name}"
            )

    if kept_rows:
        report["question_grounding_ratio"] = round(report["rows_with_switch_version_in_question"] / len(kept_rows), 4)
        if report["question_grounding_ratio"] < 0.8:
            report["warnings"].append(
                f"Only {report['question_grounding_ratio']:.1%} of rows have switch/version grounding in the user question."
            )

    structured_path = output_dir / "structured_records.json"
    train_path = output_dir / "train_chat.jsonl"
    quality_path = output_dir / "quality_report.json"
    write_json(records, structured_path)
    write_jsonl(kept_rows, train_path)
    write_jsonl(kept_rows, final_jsonl)

    output_paths = {
        "structured_records": str(structured_path),
        "train_chat": str(train_path),
        "quality_report": str(quality_path),
        "final_jsonl": str(final_jsonl),
    }
    report["output_paths"] = output_paths
    report["structured_records_extracted"] = len(records)
    report["qa_rows_generated"] = len(generated_rows)
    report["qa_rows_kept"] = len(kept_rows)
    report["unique_bug_ids"] = sorted(report["unique_bug_ids"])

    for key in (
        "sections_processed",
        "rows_extracted_by_section",
        "qa_generated_by_section",
        "qa_kept_by_section",
        "qa_dropped_by_section",
        "drop_reasons",
        "section_counts",
        "qa_counts_by_source_type",
        "qa_counts_by_source_type_before",
        "qa_counts_by_source_type_after",
    ):
        report[key] = dict(report[key])

    write_quality_report(report, quality_path)
    return report


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Deterministically preprocess Aruba AOS-CX Markdown release notes into JSONL."
    )
    parser.add_argument("--input-root", required=True)
    parser.add_argument("--output-root", required=True)
    parser.add_argument("--switch-name", required=True)
    parser.add_argument("--version", required=True)
    parser.add_argument("--sub-version", required=True)
    parser.add_argument("--final-jsonl")
    parser.add_argument("--write-intermediate", action="store_true")
    parser.add_argument("--include-legal", action="store_true")
    parser.add_argument("--max_qa_per_bug", type=int, default=5)
    parser.add_argument("--ground_questions_with_version", action=argparse.BooleanOptionalAction, default=True)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    report = run(args)
    print(f"Files processed: {report['input_files']}")
    print(f"Structured records extracted: {report['structured_records_extracted']}")
    print(f"Q&A rows generated: {report['qa_rows_generated']}")
    print(f"Q&A rows kept: {report['qa_rows_kept']}")
    if report.get("question_grounding_ratio", 1.0) < 0.8:
        print(f"WARNING: only {report['question_grounding_ratio']:.1%} of rows have switch/version grounding.")
    print("Output paths:")
    for name, path in report["output_paths"].items():
        print(f"  {name}: {path}")


if __name__ == "__main__":
    main(sys.argv[1:])
