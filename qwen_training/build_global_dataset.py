"""Build a leakage-safe global Aruba AOS-CX training dataset.

Updated for the final data layout where release-note JSONL files and final
product-documentation JSONL files are placed under one root, for example:

    E:\\52\\Train\\Train\\Data
      final_json\\...\\train_chat.jsonl
      full_product_docs\\...\\train_chat.jsonl

The script preserves the new product documentation source_type/data_family
values, removes stale backup JSONL files, validates chat rows, deduplicates,
optionally caps overrepresented groups, creates train/val/test splits, and
writes balance/sample-review reports.
"""

import argparse
import csv
import json
import math
import random
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple


PRODUCT_SOURCE_PREFIX = "product_"
RELEASE_SOURCE_PREFIX = "release_notes_"

PRODUCT_DATA_FAMILIES = {
    "cli_command_reference",
    "show_command_reference",
    "concept_explanation",
    "configuration_procedure",
    "event_log_reference",
    "feature_limitation",
    "qos_policy",
    "security_policy",
    "routing_feature",
    "monitoring_feature",
    "troubleshooting",
    "rest_api_reference",
    "snmp_mib_reference",
    "web_ui_task",
}

RELEASE_DATA_FAMILIES = {
    "release_notes_bug",
    "release_notes_caveat",
    "release_notes_known_issue",
    "release_notes_fix",
    "release_notes_enhancement",
    "release_notes_generic",
    "release_notes_non_bug",
}

BUG_SOURCE_TYPES = {
    "release_notes_known_issues",
    "release_notes_resolved_issues",
    "release_notes_fixes",
    "release_notes_only",
    "release_notes_bug",
}

FAKE_BUG_IDS = {
    "000000", "111111", "123456", "222222", "333333", "444444",
    "555555", "666666", "777777", "789012", "888888", "999999",
}

PLACEHOLDER_PATTERNS = (
    "lorem ipsum",
    "todo",
    "tbd",
    "replace me",
    "placeholder",
    "dummy text",
    "siddharthan sundaradoss",
)

IGNORED_DIR_NAMES = {
    "all_switches", "outputs", "outputs_final", "outputs_model_ab", "logs",
    "checkpoints", "wandb", ".venv", "__pycache__", "pycache",
}

ALLOWED_DATA_DIR_NAMES = {"final_json", "full_product_docs", "product_docs"}

FINAL_JSONL_NAMES = {
    "train_chat.jsonl",
    "release_notes_final_clean.jsonl",
    "product_docs_final_clean.jsonl",
    "combined_final_clean.jsonl",
}

SKIP_PATH_MARKERS = (
    "backup",
    "candidate",
    "sample",
    "review",
    "report",
    "before_",
    ".before_",
    "low300",
    "audit",
    "old",
    "tmp",
    "smoke",
    "test_",
)

MOJIBAKE_REPLACEMENTS = {
    "â€": "-", "â€“": "-", "â€”": "-", "â€˜": "'", "â€™": "'",
    "â€œ": '"', "â€": '"', "Â ": " ",
}

REAL_COMMAND_STARTERS = {
    "aaa", "access-list", "apply", "bfd", "boot", "class", "clear", "clock",
    "configure", "copy", "crypto", "debug", "dhcp", "interface", "ip", "ipv6",
    "lacp", "lldp", "logging", "mac", "mirror", "ntp", "policy", "qos",
    "radius-server", "router", "show", "snmp-server", "ssh", "tacacs-server",
    "vlan", "vrf", "vsx", "write", "ping", "traceroute", "erase", "checkpoint",
}


def parse_bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {"1", "true", "yes", "y", "on"}


def normalize_text(value: Any, preserve_newlines: bool = False) -> str:
    text = str(value or "")
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    try:
        repaired = text.encode("latin-1").decode("utf-8")
        if repaired.count("\ufffd") <= text.count("\ufffd"):
            text = repaired
    except (UnicodeEncodeError, UnicodeDecodeError):
        pass
    for bad, good in MOJIBAKE_REPLACEMENTS.items():
        text = text.replace(bad, good)
    if preserve_newlines:
        text = re.sub(r"[ \t]+", " ", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
    else:
        text = re.sub(r"\s+", " ", text)
    return text.strip()


def normalized_key_text(value: Any) -> str:
    return re.sub(r"\s+", " ", normalize_text(value).lower()).strip()


def word_count(value: str) -> int:
    return len(re.findall(r"\b\S+\b", value or ""))


def has_placeholder(text: str) -> bool:
    lowered = text.lower()
    return any(pattern in lowered for pattern in PLACEHOLDER_PATTERNS)


def is_skipped_jsonl(path: Path, data_root: Path) -> bool:
    rel = str(path.relative_to(data_root)).replace("\\", "/").lower()
    return any(marker in rel for marker in SKIP_PATH_MARKERS)


def iter_jsonl_files(data_root: Path, include_all_jsonl: bool = False) -> List[Path]:
    files: List[Path] = []
    for path in data_root.rglob("*.jsonl"):
        rel_parts_tuple = path.relative_to(data_root).parts
        if not rel_parts_tuple:
            continue
        if rel_parts_tuple[0] not in ALLOWED_DATA_DIR_NAMES:
            continue
        rel_parts = set(rel_parts_tuple[:-1])
        if rel_parts.intersection(IGNORED_DIR_NAMES):
            continue
        if is_skipped_jsonl(path, data_root):
            continue
        if not include_all_jsonl and path.name not in FINAL_JSONL_NAMES:
            # Avoid accidental ingestion of intermediate/debug JSONL files.
            continue
        files.append(path)
    return sorted(files)


def parse_folder_version(folder_version: str) -> Tuple[str, str]:
    text = normalize_text(folder_version).replace(".", "_")
    match = re.match(r"^(\d{2}_\d{2})_(\d+)$", text)
    if match:
        return match.group(1), match.group(2)
    return text, "base"


def normalize_version_pair(version_value: Any, sub_version_value: Any = "") -> Tuple[str, str]:
    version = normalize_text(version_value).replace(".", "_")
    sub_version = normalize_text(sub_version_value).replace(".", "_")
    parsed_version, parsed_sub_version = parse_folder_version(version)
    if parsed_version != version:
        version = parsed_version
        if not sub_version or sub_version == "base":
            sub_version = parsed_sub_version
    if not sub_version:
        sub_version = "base"
    return version, sub_version


def infer_path_metadata(path: Path, data_root: Path) -> Dict[str, str]:
    parts = path.relative_to(data_root).parts
    meta: Dict[str, str] = {}
    if not parts:
        return meta

    # Product docs layout: full_product_docs/<switch>/<folder_version>/train_chat.jsonl
    if parts[0] == "full_product_docs" and len(parts) >= 4:
        version, sub = normalize_version_pair(parts[2], "")
        meta.update({"switch": parts[1], "version": version, "sub_version": sub})
        return meta

    # Actual final-data layout seen on disk:
    # product_docs/full_product_docs/<switch>/<folder_version>/train_chat.jsonl
    if parts[0] == "product_docs" and len(parts) >= 5 and parts[1] == "full_product_docs":
        version, sub = normalize_version_pair(parts[3], "")
        meta.update({"switch": parts[2], "version": version, "sub_version": sub})
        return meta

    # Release notes layout: final_json/<switch>/<version>/<sub_version>/train_chat.jsonl
    if parts[0] == "final_json" and len(parts) >= 5:
        version, sub = normalize_version_pair(parts[2], parts[3])
        meta.update({"switch": parts[1], "version": version, "sub_version": sub})
        return meta

    # Generic recursive layout: <switch>/<folder_version>/train_chat.jsonl or <switch>/<version>/<sub>/train_chat.jsonl
    if len(parts) >= 4:
        meta["switch"] = parts[-4]
        meta["version"], meta["sub_version"] = normalize_version_pair(parts[-3], "")
    elif len(parts) >= 3:
        meta["switch"] = parts[0]
        meta["version"], meta["sub_version"] = normalize_version_pair(parts[1], "")
    return meta


def first_message(row: Dict[str, Any], role: str) -> str:
    for message in row.get("messages", []):
        if isinstance(message, dict) and str(message.get("role", "")).strip().lower() == role:
            return normalize_text(message.get("content", ""), preserve_newlines=(role == "assistant"))
    return ""


def is_product_source(source_type: str) -> bool:
    return normalize_text(source_type).startswith(PRODUCT_SOURCE_PREFIX)


def is_release_source(source_type: str) -> bool:
    return normalize_text(source_type).startswith(RELEASE_SOURCE_PREFIX)


def is_product_family(data_family: str) -> bool:
    return normalize_text(data_family) in PRODUCT_DATA_FAMILIES


def is_release_family(data_family: str) -> bool:
    return normalize_text(data_family) in RELEASE_DATA_FAMILIES or normalize_text(data_family).startswith("release_notes_")


def infer_source_type(row: Dict[str, Any], path: Path, data_root: Path, answer: str) -> str:
    source_type = normalize_text(row.get("source_type", ""))
    if source_type:
        return source_type
    rel = "/".join(path.relative_to(data_root).parts).lower()
    if "full_product_docs" in rel or "product_docs" in rel:
        return "product_documentation"
    if row.get("bug_id") or re.search(r"\bBug ID\b|\bBug\s+\d{5,7}\b", answer, re.IGNORECASE):
        return "release_notes_bug"
    return "release_notes_generic"


def infer_data_family(row: Dict[str, Any], source_type: str, question: str, answer: str) -> str:
    data_family = normalize_text(row.get("data_family", ""))
    if data_family:
        return data_family
    if is_product_source(source_type) or source_type == "product_documentation":
        # Fallback for old product-doc rows.
        if normalize_text(row.get("command") or row.get("command_name")):
            return "cli_command_reference"
        return "concept_explanation"
    if re.search(r"\bBug ID\b|\bBug\s+\d{5,7}\b", question + "\n" + answer, re.IGNORECASE):
        return "release_notes_bug"
    return "release_notes_generic"


def extract_bug_id(row: Dict[str, Any], question: str, answer: str) -> str:
    for value in (row.get("bug_id", ""), question, answer):
        match = re.search(r"\b(\d{5,7})\b", normalize_text(value))
        if match:
            return match.group(1)
    return ""


def infer_category(row: Dict[str, Any], answer: str) -> str:
    category = normalize_text(row.get("category", ""))
    if category:
        return category
    match = re.match(r"^([^(:]{2,80})\s*\(Bug ID\s+\d{5,7}\):", answer)
    if match:
        return normalize_text(match.group(1))
    section = normalize_text(row.get("section", ""))
    return section


def command_value(row: Dict[str, Any]) -> str:
    return normalize_text(row.get("command") or row.get("command_name") or "")


def infer_topic(row: Dict[str, Any], question: str, answer: str) -> str:
    for key in ("topic", "section", "command", "command_name", "document_title", "category"):
        value = normalize_text(row.get(key, ""))
        if value:
            return value
    return " ".join(normalize_text(question or answer).split()[:10])


def clean_messages(question: str, answer: str) -> List[Dict[str, str]]:
    return [
        {"role": "user", "content": normalize_text(question)},
        {"role": "assistant", "content": normalize_text(answer, preserve_newlines=True)},
    ]


def looks_like_fake_command_heading(text: str) -> bool:
    value = normalize_text(text)
    if not value:
        return False
    if re.fullmatch(r"[A-Za-z0-9 /+_.()&-]{2,80}\s+[Cc]ommands?", value):
        first = value.split()[0].lower()
        # Real commands such as "boot system" do not end with "commands".
        return first not in REAL_COMMAND_STARTERS or value.lower().endswith((" commands", " command"))
    return False


def validate_and_normalize(
    row: Dict[str, Any],
    path: Path,
    data_root: Path,
    args: argparse.Namespace,
) -> Tuple[Optional[Dict[str, Any]], Optional[str]]:
    if not isinstance(row, dict):
        return None, "not_json_object"
    messages = row.get("messages")
    if not isinstance(messages, list):
        return None, "missing_messages"

    question = first_message(row, "user")
    answer = first_message(row, "assistant")
    if not question:
        return None, "missing_user_message"
    if not answer:
        return None, "missing_assistant_message"
    if word_count(question) < args.min_question_words:
        return None, "question_too_short"
    if word_count(answer) < args.min_answer_words:
        return None, "answer_too_short"
    if has_placeholder(question) or has_placeholder(answer):
        return None, "placeholder_text"
    if "```" in answer:
        return None, "answer_contains_code_fence"

    path_meta = infer_path_metadata(path, data_root)
    source_type = infer_source_type({**path_meta, **row}, path, data_root, answer)
    data_family = infer_data_family(row, source_type, question, answer)
    product = is_product_source(source_type) or is_product_family(data_family) or source_type == "product_documentation"
    release = is_release_source(source_type) or is_release_family(data_family)

    switch = normalize_text(row.get("switch") or path_meta.get("switch") or "")
    version, sub_version = normalize_version_pair(
        row.get("version") or path_meta.get("version") or "",
        row.get("sub_version") or row.get("subversion") or path_meta.get("sub_version") or "base",
    )
    section = normalize_text(row.get("section", ""))

    if not switch:
        return None, "missing_switch"
    if not version:
        return None, "missing_version"
    if not source_type:
        return None, "missing_source_type"
    if not data_family:
        return None, "missing_data_family"

    base: Dict[str, Any] = {
        "source_type": source_type,
        "data_family": data_family,
        "switch": switch,
        "version": version,
        "sub_version": sub_version,
        "section": section,
        "messages": clean_messages(question, answer),
    }

    if product:
        cmd = command_value(row)
        if looks_like_fake_command_heading(cmd) or looks_like_fake_command_heading(row.get("syntax", "")):
            return None, "fake_command_heading"
        base.update(
            {
                "source_type": source_type if is_product_source(source_type) else "product_documentation",
                "data_family": data_family if is_product_family(data_family) else "concept_explanation",
                "document_title": normalize_text(row.get("document_title", "")),
                "source_file": normalize_text(row.get("source_file", "")),
                "topic": normalize_text(row.get("topic", "")) or infer_topic(row, question, answer),
            }
        )
        if cmd:
            base["command"] = cmd
            base["command_name"] = cmd
        syntax = normalize_text(row.get("syntax", ""), preserve_newlines=True)
        if syntax:
            base["syntax"] = syntax
        return base, None

    if release:
        bug_id = extract_bug_id(row, question, answer)
        category = infer_category(row, answer)
        if data_family == "release_notes_bug" or bug_id:
            if not re.fullmatch(r"\d{5,7}", bug_id or ""):
                return None, "bug_missing_or_invalid_bug_id"
            if bug_id in FAKE_BUG_IDS:
                return None, "bug_fake_bug_id"
            base.update({"bug_id": bug_id, "category": category or section or "Release Notes"})
            if not base["data_family"].startswith("release_notes_"):
                base["data_family"] = "release_notes_bug"
        else:
            if not base["data_family"].startswith("release_notes_"):
                base["data_family"] = "release_notes_generic"
        return base, None

    return base, None


def exact_key(row: Dict[str, Any]) -> Tuple[str, str]:
    return (normalized_key_text(first_message(row, "user")), normalized_key_text(first_message(row, "assistant")))


def question_key(row: Dict[str, Any]) -> str:
    return normalized_key_text(first_message(row, "user"))


def row_score(row: Dict[str, Any]) -> Tuple[int, int, int, int]:
    answer = first_message(row, "assistant")
    score = 0
    if command_value(row):
        score += 4
    if row.get("bug_id"):
        score += 4
    if row.get("document_title"):
        score += 2
    if row.get("section"):
        score += 1
    if row.get("source_file"):
        score += 1
    # Prefer concise but not tiny answers.
    words = word_count(answer)
    length_score = -abs(words - 45)
    return (score, length_score, len(answer), len(json.dumps(row, ensure_ascii=False)))


def choose_better(a: Dict[str, Any], b: Dict[str, Any]) -> Dict[str, Any]:
    return b if row_score(b) > row_score(a) else a


def deduplicate(rows: List[Dict[str, Any]], dedup_questions: bool = True) -> Tuple[List[Dict[str, Any]], int, int]:
    exact_seen: Dict[Tuple[str, str], Dict[str, Any]] = {}
    exact_dupes = 0
    for row in rows:
        key = exact_key(row)
        if key in exact_seen:
            exact_seen[key] = choose_better(exact_seen[key], row)
            exact_dupes += 1
        else:
            exact_seen[key] = row

    if not dedup_questions:
        return list(exact_seen.values()), exact_dupes, 0

    question_seen: Dict[str, Dict[str, Any]] = {}
    question_dupes = 0
    for row in exact_seen.values():
        key = question_key(row)
        if key in question_seen:
            question_seen[key] = choose_better(question_seen[key], row)
            question_dupes += 1
        else:
            question_seen[key] = row
    return list(question_seen.values()), exact_dupes, question_dupes


def domain(row: Dict[str, Any]) -> str:
    st = row.get("source_type", "")
    fam = row.get("data_family", "")
    if is_product_source(st) or is_product_family(fam) or st == "product_documentation":
        return "product_docs"
    if is_release_source(st) or is_release_family(fam):
        return "release_notes"
    return "other"


def cap_key(row: Dict[str, Any]) -> Tuple[str, str]:
    fam = row.get("data_family", "")
    dom = domain(row)
    if dom == "release_notes" and (row.get("bug_id") or fam == "release_notes_bug"):
        return ("release_bug", f"{row.get('switch')}|{row.get('version')}|{row.get('sub_version')}|{row.get('bug_id')}|{row.get('category')}")
    if dom == "product_docs":
        cmd = command_value(row)
        topic = infer_topic(row, first_message(row, "user"), first_message(row, "assistant"))
        return ("product", f"{row.get('source_type')}|{fam}|{row.get('switch')}|{row.get('version')}|{cmd or topic}")
    return ("other", f"{row.get('source_type')}|{fam}|{row.get('switch')}|{row.get('version')}|{row.get('section')}")


def cap_rows(rows: List[Dict[str, Any]], args: argparse.Namespace) -> List[Dict[str, Any]]:
    if not args.apply_group_caps:
        return rows
    grouped: Dict[Tuple[str, str], List[Dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[cap_key(row)].append(row)

    capped: List[Dict[str, Any]] = []
    rnd = random.Random(args.seed)
    for (kind, _), items in grouped.items():
        items = sorted(items, key=row_score, reverse=True)
        if kind == "release_bug" and args.max_records_per_bug > 0:
            capped.extend(items[: args.max_records_per_bug])
        elif kind == "product" and args.max_records_per_product_key > 0:
            capped.extend(items[: args.max_records_per_product_key])
        elif kind == "other" and args.max_records_per_topic > 0:
            capped.extend(items[: args.max_records_per_topic])
        else:
            capped.extend(items)
    rnd.shuffle(capped)
    return capped


def trim_to_ratio(rows: List[Dict[str, Any]], predicate, max_ratio: float, seed: int) -> List[Dict[str, Any]]:
    if max_ratio <= 0 or max_ratio >= 1:
        return rows
    selected = [r for r in rows if predicate(r)]
    others = [r for r in rows if not predicate(r)]
    # selected <= max_ratio * (selected + others)
    max_selected = int((max_ratio * len(others)) / max(1e-9, 1 - max_ratio)) if others else len(selected)
    if len(selected) <= max_selected:
        return rows
    selected = sorted(selected, key=row_score, reverse=True)[:max_selected]
    out = selected + others
    random.Random(seed).shuffle(out)
    return out


def enforce_ratios(rows: List[Dict[str, Any]], args: argparse.Namespace) -> List[Dict[str, Any]]:
    if not args.balance:
        return rows
    rows = trim_to_ratio(rows, lambda r: domain(r) == "product_docs", args.max_product_doc_ratio, args.seed)
    rows = trim_to_ratio(rows, lambda r: domain(r) == "release_notes", args.max_release_note_ratio, args.seed)
    rows = trim_to_ratio(rows, lambda r: r.get("data_family") == "event_log_reference", args.max_event_log_ratio, args.seed)
    return rows


def split_group_key(row: Dict[str, Any]) -> str:
    fam = row.get("data_family", "")
    q = question_key(row)
    if domain(row) == "release_notes" and row.get("bug_id"):
        return f"release_bug:{row.get('switch')}:{row.get('version')}:{row.get('sub_version')}:{row.get('bug_id')}"
    if domain(row) == "product_docs":
        cmd = command_value(row)
        topic = infer_topic(row, first_message(row, "user"), first_message(row, "assistant"))
        return f"product:{row.get('source_type')}:{fam}:{cmd or row.get('document_title')}:{topic}"
    return f"other:{row.get('source_type')}:{fam}:{' '.join(q.split()[:10])}"


def split_rows(rows: List[Dict[str, Any]], args: argparse.Namespace) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]], List[Dict[str, Any]]]:
    grouped: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[split_group_key(row)].append(row)
    groups = list(grouped.items())
    random.Random(args.seed).shuffle(groups)
    total = sum(len(items) for _, items in groups)
    train_target = int(total * args.train_ratio)
    val_target = int(total * args.val_ratio)
    train: List[Dict[str, Any]] = []
    val: List[Dict[str, Any]] = []
    test: List[Dict[str, Any]] = []
    for _, items in groups:
        if len(train) < train_target:
            train.extend(items)
        elif len(val) < val_target:
            val.extend(items)
        else:
            test.extend(items)
    return train, val, test


def counter_by(rows: Iterable[Dict[str, Any]], key: str) -> Dict[str, int]:
    return dict(Counter(normalize_text(row.get(key, "")) or "missing" for row in rows))


def count_exact_duplicates(rows: List[Dict[str, Any]]) -> int:
    counts = Counter(exact_key(r) for r in rows)
    return sum(c - 1 for c in counts.values() if c > 1)


def count_duplicate_questions(rows: List[Dict[str, Any]]) -> int:
    counts = Counter(question_key(r) for r in rows)
    return sum(c - 1 for c in counts.values() if c > 1)


def write_jsonl(path: Path, rows: List[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def write_csv(path: Path, rows: Sequence[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fields = list(rows[0].keys())
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def sample_review(rows: List[Dict[str, Any]], seed: int, per_group: int) -> List[Dict[str, Any]]:
    rnd = random.Random(seed)
    out: Dict[Tuple[str, str, str], Dict[str, Any]] = {}

    def add_samples(label: str, key_fn):
        groups: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
        for row in rows:
            groups[key_fn(row)].append(row)
        for key, items in groups.items():
            for item in rnd.sample(items, min(per_group, len(items))):
                out[(label, key, question_key(item))] = {
                    "sample_group": label,
                    "sample_key": key,
                    "switch": item.get("switch", ""),
                    "version": item.get("version", ""),
                    "sub_version": item.get("sub_version", ""),
                    "source_type": item.get("source_type", ""),
                    "data_family": item.get("data_family", ""),
                    "document_title": item.get("document_title", ""),
                    "section": item.get("section", ""),
                    "source_file": item.get("source_file", ""),
                    "user_question": first_message(item, "user"),
                    "assistant_answer": first_message(item, "assistant"),
                }

    add_samples("switch_version", lambda r: f"{r.get('switch')}|{r.get('version')}|{r.get('sub_version')}")
    add_samples("source_type", lambda r: r.get("source_type", "missing"))
    add_samples("data_family", lambda r: r.get("data_family", "missing"))
    return list(out.values())


def build_report(files: List[Path], loaded: int, valid: List[Dict[str, Any]], final: List[Dict[str, Any]], train: List[Dict[str, Any]], val: List[Dict[str, Any]], test: List[Dict[str, Any]], drops: Counter, exact_dupes: int, question_dupes: int) -> Dict[str, Any]:
    total = len(final)
    product_count = sum(1 for r in final if domain(r) == "product_docs")
    release_count = sum(1 for r in final if domain(r) == "release_notes")
    event_count = sum(1 for r in final if r.get("data_family") == "event_log_reference")
    cli_count = sum(1 for r in final if r.get("data_family") == "cli_command_reference")
    show_count = sum(1 for r in final if r.get("data_family") == "show_command_reference")
    concept_proc_count = sum(1 for r in final if r.get("data_family") in {"concept_explanation", "configuration_procedure", "security_policy", "routing_feature", "qos_policy", "monitoring_feature", "troubleshooting"})
    warnings: List[str] = []
    if total and product_count / total > 0.70:
        warnings.append("product docs ratio above 70%")
    if total and release_count / total > 0.70:
        warnings.append("release notes ratio above 70%")
    if total and event_count / total > 0.15:
        warnings.append("event log ratio above 15%")
    if total and (cli_count + show_count) / total > 0.65:
        warnings.append("CLI/show command rows above 65%")
    if count_duplicate_questions(final):
        warnings.append("duplicate questions remain")

    return {
        "total_files_found": len(files),
        "total_rows_loaded": loaded,
        "total_rows_valid_before_dedup": len(valid),
        "total_rows_final": total,
        "total_rows_dropped_by_validation": sum(drops.values()),
        "drop_reasons": dict(sorted(drops.items())),
        "jsonl_parse_errors": drops.get("invalid_json", 0),
        "missing_messages": drops.get("missing_messages", 0),
        "missing_source_type": drops.get("missing_source_type", 0),
        "missing_data_family": drops.get("missing_data_family", 0),
        "missing_switch": drops.get("missing_switch", 0),
        "missing_version": drops.get("missing_version", 0),
        "exact_duplicate_qa_removed": exact_dupes,
        "duplicate_questions_found": question_dupes,
        "duplicate_question_rows_dropped": question_dupes,
        "duplicate_question_rows_removed": question_dupes,
        "exact_duplicate_qa_final": count_exact_duplicates(final),
        "duplicate_questions_final": count_duplicate_questions(final),
        "product_doc_rows": product_count,
        "release_note_rows": release_count,
        "product_doc_ratio": product_count / total if total else 0.0,
        "release_note_ratio": release_count / total if total else 0.0,
        "event_log_rows": event_count,
        "event_log_ratio": event_count / total if total else 0.0,
        "cli_command_reference_rows": cli_count,
        "show_command_reference_rows": show_count,
        "cli_plus_show_ratio": (cli_count + show_count) / total if total else 0.0,
        "concept_procedure_policy_rows": concept_proc_count,
        "concept_procedure_policy_ratio": concept_proc_count / total if total else 0.0,
        "rows_by_data_family": counter_by(final, "data_family"),
        "rows_by_source_type": counter_by(final, "source_type"),
        "rows_by_switch": counter_by(final, "switch"),
        "rows_by_version": counter_by(final, "version"),
        "rows_by_document_title": counter_by(final, "document_title"),
        "final_train_count": len(train),
        "final_val_count": len(val),
        "final_test_count": len(test),
        "warnings": warnings,
    }


def make_balance_rows(rows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    total = max(len(rows), 1)
    output: List[Dict[str, Any]] = []
    for field in ("switch", "version", "source_type", "data_family", "document_title"):
        for value, count in Counter(normalize_text(r.get(field, "")) or "missing" for r in rows).most_common():
            output.append({"field": field, "value": value, "count": count, "percent": round(100 * count / total, 4)})
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description="Build final global Aruba AOS-CX train/val/test dataset")
    parser.add_argument("--data_root", default=r"E:\52\Train\Train\Data")
    parser.add_argument("--output_dir", default=r"E:\52\Train\Train\Data\all_switches")
    parser.add_argument("--train_ratio", type=float, default=0.90)
    parser.add_argument("--val_ratio", type=float, default=0.05)
    parser.add_argument("--test_ratio", type=float, default=0.05)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--dedup", type=parse_bool, default=True)
    parser.add_argument("--dedup_questions", type=parse_bool, default=True)
    parser.add_argument("--balance", type=parse_bool, default=True)
    parser.add_argument("--apply_group_caps", type=parse_bool, default=False, help="Set true to cap repeated bugs/commands/topics. Default keeps all clean rows.")
    parser.add_argument("--max_records_per_bug", type=int, default=8)
    parser.add_argument("--max_records_per_product_key", type=int, default=12)
    parser.add_argument("--max_records_per_topic", type=int, default=8)
    parser.add_argument("--max_product_doc_ratio", type=float, default=0.70)
    parser.add_argument("--max_release_note_ratio", type=float, default=0.55)
    parser.add_argument("--max_event_log_ratio", type=float, default=0.15)
    parser.add_argument("--min_question_words", type=int, default=5)
    parser.add_argument("--min_answer_words", type=int, default=8)
    parser.add_argument("--include_all_jsonl", action="store_true", help="Include every JSONL except backups. Not recommended unless the data root is clean.")
    parser.add_argument("--sample_per_group", type=int, default=5)
    args = parser.parse_args()

    if abs((args.train_ratio + args.val_ratio + args.test_ratio) - 1.0) > 1e-6:
        raise SystemExit("train_ratio + val_ratio + test_ratio must equal 1.0")

    data_root = Path(args.data_root)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    files = iter_jsonl_files(data_root, args.include_all_jsonl)
    loaded = 0
    valid_rows: List[Dict[str, Any]] = []
    drops: Counter = Counter()

    for path in files:
        with path.open("r", encoding="utf-8-sig") as handle:
            for line_no, line in enumerate(handle, start=1):
                line = line.strip()
                if not line:
                    continue
                try:
                    raw = json.loads(line)
                    loaded += 1
                except json.JSONDecodeError:
                    drops["invalid_json"] += 1
                    continue
                row, reason = validate_and_normalize(raw, path, data_root, args)
                if row is None:
                    drops[reason or "unknown"] += 1
                else:
                    valid_rows.append(row)

    rows = valid_rows
    exact_dupes = 0
    question_dupes = 0
    if args.dedup:
        rows, exact_dupes, question_dupes = deduplicate(rows, args.dedup_questions)
    rows = cap_rows(rows, args)
    rows = enforce_ratios(rows, args)
    random.Random(args.seed).shuffle(rows)
    train, val, test = split_rows(rows, args)

    write_jsonl(output_dir / "train_chat_all_clean.jsonl", train)
    write_jsonl(output_dir / "val_chat_all_clean.jsonl", val)
    write_jsonl(output_dir / "test_chat_all_clean.jsonl", test)
    write_jsonl(output_dir / "combined_chat_all_clean.jsonl", rows)
    write_jsonl(output_dir / "train_chat_all_clean_validated.jsonl", train)

    report = build_report(files, loaded, valid_rows, rows, train, val, test, drops, exact_dupes, question_dupes)
    with (output_dir / "dataset_report.json").open("w", encoding="utf-8") as handle:
        json.dump(report, handle, indent=2, ensure_ascii=False)

    balance_rows = make_balance_rows(rows)
    write_csv(output_dir / "balance_report.csv", balance_rows)
    with (output_dir / "balance_report.json").open("w", encoding="utf-8") as handle:
        json.dump({"summary": report, "breakdowns": balance_rows}, handle, indent=2, ensure_ascii=False)

    samples = sample_review(rows, args.seed, args.sample_per_group)
    write_jsonl(output_dir / "sample_review.jsonl", samples)
    write_csv(output_dir / "sample_review.csv", samples)

    print(f"Files found: {len(files)}")
    print(f"Rows loaded: {loaded}")
    print(f"Rows valid before dedup: {len(valid_rows)}")
    print(f"Rows final: {len(rows)}")
    print(f"Train/Val/Test: {len(train)}/{len(val)}/{len(test)}")
    print(f"Report: {output_dir / 'dataset_report.json'}")
    if report["warnings"]:
        print("Warnings:")
        for warning in report["warnings"]:
            print(f"- {warning}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
