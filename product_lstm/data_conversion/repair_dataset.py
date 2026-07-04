#!/usr/bin/env python3
"""Build a deterministic, cleaned Aruba AOS-CX fine-tuning dataset.

The source JSONL files are read-only. Outputs are written to a separate
directory and are replaced only when --force is supplied.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
import re
from collections import Counter, defaultdict
from copy import deepcopy
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Iterable, Iterator, List, Mapping, MutableMapping, Optional, Sequence, Tuple


DEFAULT_INPUTS = (
    Path("Data/all_switches/train_chat_all_clean_validated.jsonl"),
    Path("Data/all_switches/val_chat_all_clean.jsonl"),
    Path("Data/all_switches/test_chat_all_clean.jsonl"),
)
DEFAULT_OUTPUT_DIR = Path("final_json_clean/all_switches")
SPLIT_FILENAMES = {
    "train": "train_chat_all_clean.jsonl",
    "validation": "val_chat_all_clean.jsonl",
    "test": "test_chat_all_clean.jsonl",
}
NEGATIVE_OPTIONS = ("VLAN", "interface", "brief", "vsx-peer", "vrf", "all-vrfs")
NOT_DOCUMENTED_ANSWER = "This is not documented in the provided training data."

SYNTAX_QUESTION_RE = re.compile(
    r"(?i)(?:\bwhat\s+is\s+the\s+(?:exact\s+)?syntax\b|\bexact\s+syntax\b|"
    r"\bcommand\s+syntax\b|\bsyntax\s+of\b|\bshow\s+(?:me\s+)?the\s+syntax\b|"
    r"\bgive\s+(?:me\s+)?the\s+(?:exact\s+)?syntax\b)"
)
DESCRIPTION_QUESTION_RE = re.compile(
    r"(?i)(?:\bwhat\s+does\b.+\bdo\b|\bwhat\s+is\b.+\bused\s+for\b|"
    r"\bdescribe\b.+\bcommand\b|\bpurpose\s+of\b.+\bcommand\b)"
)
DATE_RE = re.compile(
    r"\b(?:released\s+on\s+|release\s+date\s*[:\-]?\s*)"
    r"(?P<date>\d{1,2}\s+[A-Za-z]+\s+\d{4})\b",
    re.I,
)
TARGET_VERSION_RE = re.compile(r"\bversion\s+(?P<version>\d{1,2}\.\d{1,2}\.\d{3,5})\b", re.I)
BUG_ID_RE = re.compile(r"\b(?:bug(?:\s+id)?\s*[:#-]?\s*)(\d{4,8})\b", re.I)
EVENT_ID_RE = re.compile(r"\bevent(?:\s+id)?\s*[:#-]?\s*(\d{3,8})\b", re.I)
NOISE_PATTERNS = tuple(
    re.compile(pattern, re.I)
    for pattern in (
        r"\bf\s+rom\b",
        r"\bavai\s+lable\b",
        r"\bcommannd\b",
        r"\bcleat\b",
        r"\beraps\b",
        r"\bclea\s+r\b",
        r"\bs\s+t\s+at\b",
        r"\uFFFD",
    )
)
MOJIBAKE_REPLACEMENTS = {
    "â€¢": "-",
    "â—¦": "-",
    "â€“": "-",
    "â€”": "-",
    "â€œ": '"',
    "â€": '"',
    "â€™": "'",
    "Â": "",
}
DESCRIPTION_CUT_RE = re.compile(
    r"(?i)(?:\s+Syntax\s*:|\n\s*Syntax\s*:|\s+Required\s*:|\s+Optional\s*:|"
    r"\s+Parameters?\s*:|\s+Command context\s*:|\s+Usage\s*:|\s+Default\s*:|"
    r"\s+Range\s*:|\s+Public\s+)"
)


def normalize(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "").strip()).casefold()


def stable_digest(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def clean_mojibake(value: str) -> str:
    text = str(value or "").replace("\r\n", "\n").replace("\r", "\n")
    for bad, good in MOJIBAKE_REPLACEMENTS.items():
        text = text.replace(bad, good)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" *\n *", "\n", text)
    return text.strip()


def has_noise(value: str) -> bool:
    return any(pattern.search(str(value or "")) for pattern in NOISE_PATTERNS)


def remove_nulls(value: Any) -> Any:
    if isinstance(value, dict):
        return {key: remove_nulls(item) for key, item in value.items() if item is not None}
    if isinstance(value, list):
        return [remove_nulls(item) for item in value if item is not None]
    if isinstance(value, float) and not math.isfinite(value):
        raise ValueError("Non-finite numeric value")
    return value


def extract_qa(row: Mapping[str, Any]) -> Tuple[str, str]:
    question = answer = ""
    for message in row.get("messages") or []:
        if not isinstance(message, Mapping):
            continue
        role = message.get("role")
        content = str(message.get("content") or "").strip()
        if role == "user" and not question:
            question = content
        elif role == "assistant" and not answer:
            answer = content
    return question, answer


def set_qa(row: MutableMapping[str, Any], question: str, answer: str) -> None:
    row["messages"] = [
        {"role": "user", "content": question.strip()},
        {"role": "assistant", "content": answer.strip()},
    ]


def is_cli_row(row: Mapping[str, Any]) -> bool:
    family = normalize(row.get("data_family"))
    source = normalize(row.get("source_type"))
    return bool(
        source == "product_cli_reference"
        or family in {"cli_command_reference", "show_command_reference"}
        or row.get("command")
        or row.get("command_name")
    )


def is_version_history_row(row: Mapping[str, Any]) -> bool:
    return bool(
        normalize(row.get("source_type")) == "release_notes_version_history"
        or normalize(row.get("section")) == "version history"
    )


def is_syntax_question(question: str) -> bool:
    return bool(SYNTAX_QUESTION_RE.search(question or ""))


def is_description_question(question: str) -> bool:
    return bool(DESCRIPTION_QUESTION_RE.search(question or ""))


def exact_bug_id(row: Mapping[str, Any], question: str, answer: str) -> str:
    explicit = str(row.get("bug_id") or "").strip()
    if explicit:
        return explicit
    match = BUG_ID_RE.search(f"{question} {answer}")
    return match.group(1) if match else ""


def extract_event_id(row: Mapping[str, Any], question: str, answer: str) -> str:
    explicit = str(row.get("event_id") or "").strip()
    if explicit:
        return explicit
    match = EVENT_ID_RE.search(f"{question} {answer}")
    return match.group(1) if match else ""


def command_value(row: Mapping[str, Any]) -> str:
    return clean_mojibake(str(row.get("command") or row.get("command_name") or "")).strip()


def syntax_value(row: Mapping[str, Any]) -> str:
    return clean_mojibake(str(row.get("syntax") or "")).strip()


def command_identity(row: Mapping[str, Any]) -> str:
    return "|".join(
        (
            normalize(command_value(row)),
            normalize(row.get("switch")),
            normalize(row.get("version")),
            normalize(row.get("sub_version")),
        )
    )


def clean_description(command: str, answer: str) -> str:
    text = clean_mojibake(answer)
    if not text or has_noise(text):
        return ""
    if len(text) > 900 and (
        "syntax:" in text.casefold()
        or len(re.findall(r"<[^>]+>", text)) >= 3
        or text.casefold().count("required:") + text.casefold().count("optional:") >= 2
    ):
        return ""
    text = DESCRIPTION_CUT_RE.split(text, maxsplit=1)[0].strip(" -\n")
    text = re.split(r"(?<=[.!?])\s+(?=[A-Z])", text, maxsplit=1)[0].strip()
    if not text or len(text) < 18 or len(text) > 450:
        return ""
    if re.search(r"(?i)\bis documented in (?:this|the) guide\b", text):
        return ""
    if re.search(r"(?i)\b(?:syntax|parameter value unit|table of contents)\b", text):
        return ""

    prefix_re = re.compile(r"(?i)^the\s+.+?\s+command\s+")
    if prefix_re.search(text):
        suffix = prefix_re.sub("", text, count=1).strip()
    else:
        suffix = text.strip()
        if suffix.casefold().startswith(command.casefold()):
            suffix = suffix[len(command) :].lstrip(" :-")
        if suffix.casefold().startswith("command "):
            suffix = suffix[8:].strip()
    if not suffix or len(suffix) < 8:
        return ""
    suffix = suffix[0].lower() + suffix[1:] if suffix[0].isupper() else suffix
    result = f"The {command} command {suffix}".strip()
    if result[-1] not in ".!?":
        result += "."
    return result


def clean_version_history(question: str, answer: str) -> str:
    source = clean_mojibake(answer)
    target_match = TARGET_VERSION_RE.search(question) or TARGET_VERSION_RE.search(source)
    if not target_match:
        return ""
    version = target_match.group("version")
    if re.search(r"(?i)\bwhen\b|\brelease\s+date\b|\breleased\b", question):
        date_match = DATE_RE.search(source)
        if not date_match:
            return ""
        return f"Version {version} was released on {date_match.group('date')}."
    if re.search(r"(?i)\bremarks?\b", question):
        remarks_match = re.search(r"(?is)\bRemarks?\s*:\s*(.+)$", source)
        if not remarks_match:
            return ""
        remarks = re.split(r"\n|(?<=\.)\s+(?=[A-Z])", remarks_match.group(1).strip(), maxsplit=1)[0].strip()
        if not remarks or len(remarks) > 320:
            return ""
        if remarks[-1] not in ".!?":
            remarks += "."
        return f"Version {version} remarks: {remarks}"
    return ""


def fact_group_key(row: Mapping[str, Any]) -> str:
    question, answer = extract_qa(row)
    family = normalize(row.get("data_family"))
    if family == "release_notes_bug":
        bug_id = exact_bug_id(row, question, answer)
        return f"bug|{normalize(bug_id) or stable_digest(normalize(question))}"
    if is_cli_row(row):
        return "cli|" + "|".join(
            (
                normalize(command_value(row)),
                normalize(row.get("switch")),
                normalize(row.get("version")),
                normalize(row.get("sub_version")),
                normalize(syntax_value(row)),
            )
        )
    if is_version_history_row(row):
        target = TARGET_VERSION_RE.search(question)
        return "version|" + "|".join(
            (
                normalize(row.get("switch")),
                normalize(row.get("version")),
                normalize(row.get("sub_version")),
                normalize(target.group("version") if target else question),
            )
        )
    if family == "event_log_reference":
        event_id = extract_event_id(row, question, answer)
        return "event|" + "|".join(
            (
                normalize(row.get("switch")),
                normalize(row.get("version")),
                normalize(event_id or row.get("topic") or question),
            )
        )
    identity = row.get("source_file") or row.get("document_title") or ""
    topic = row.get("topic") or row.get("section") or question
    return "fact|" + "|".join(
        (
            normalize(row.get("source_type")),
            family,
            normalize(row.get("switch")),
            normalize(row.get("version")),
            normalize(identity),
            normalize(topic),
        )
    )


def stratum_key(row: Mapping[str, Any]) -> str:
    return "|".join(
        (
            normalize(row.get("source_type")),
            normalize(row.get("data_family")),
            normalize(row.get("switch")),
            normalize(row.get("version")),
        )
    )


@dataclass
class RepairStats:
    input_rows: int = 0
    canonical_output_rows: int = 0
    output_rows: int = 0
    rows_skipped_due_to_noise: int = 0
    rows_skipped_invalid: int = 0
    rows_skipped_unsafe_cli: int = 0
    rows_skipped_unrepairable_version_history: int = 0
    duplicate_questions_removed: int = 0
    conflicting_questions_removed: int = 0
    cli_syntax_rows_repaired: int = 0
    cli_description_rows_repaired: int = 0
    version_history_rows_repaired: int = 0
    bug_rows_preserved: int = 0
    paraphrase_rows_added: int = 0
    negative_examples_added: int = 0
    other_rows_preserved: int = 0
    examples: Dict[str, List[Dict[str, Any]]] = field(default_factory=lambda: defaultdict(list))

    def record_example(self, kind: str, before: Mapping[str, Any], after: Mapping[str, Any]) -> None:
        if len(self.examples[kind]) >= 3:
            return
        before_q, before_a = extract_qa(before)
        after_q, after_a = extract_qa(after)
        self.examples[kind].append(
            {
                "before": {"question": before_q, "answer": before_a},
                "after": {"question": after_q, "answer": after_a},
            }
        )

    def as_dict(self) -> Dict[str, Any]:
        result = dict(self.__dict__)
        result.pop("examples", None)
        return result


def repair_row(source_row: Mapping[str, Any], stats: RepairStats) -> Optional[Dict[str, Any]]:
    stats.input_rows += 1
    row = remove_nulls(deepcopy(dict(source_row)))
    question, answer = extract_qa(row)
    if not question or not answer:
        stats.rows_skipped_invalid += 1
        return None
    question = clean_mojibake(question)
    answer = clean_mojibake(answer)
    if has_noise(question) or has_noise(answer):
        stats.rows_skipped_due_to_noise += 1
        return None

    family = normalize(row.get("data_family"))
    if family == "release_notes_bug":
        bug_id = exact_bug_id(row, question, answer)
        if not bug_id or bug_id not in f"{question} {answer}":
            stats.rows_skipped_invalid += 1
            return None
        row["bug_id"] = bug_id
        set_qa(row, question, answer)
        stats.bug_rows_preserved += 1
        stats.canonical_output_rows += 1
        return row

    if is_cli_row(row):
        command = command_value(row)
        syntax = syntax_value(row)
        if not command:
            stats.rows_skipped_unsafe_cli += 1
            return None
        row["data_family"] = "cli_command_reference"
        if normalize(row.get("source_type")).startswith("product_"):
            row["source_type"] = "product_cli_reference"
        row["command"] = command
        row["command_name"] = command
        if syntax:
            row["syntax"] = syntax

        if is_syntax_question(question):
            if not syntax or has_noise(syntax):
                stats.rows_skipped_unsafe_cli += 1
                return None
            set_qa(row, question, f"Syntax: {syntax}")
            stats.cli_syntax_rows_repaired += 1
            stats.record_example("cli_syntax", source_row, row)
        elif is_description_question(question):
            description = clean_description(command, answer)
            if not description:
                stats.rows_skipped_unsafe_cli += 1
                return None
            set_qa(row, question, description)
            stats.cli_description_rows_repaired += 1
            stats.record_example("cli_description", source_row, row)
        else:
            stats.rows_skipped_unsafe_cli += 1
            return None
        stats.canonical_output_rows += 1
        return row

    if is_version_history_row(row):
        cleaned = clean_version_history(question, answer)
        if not cleaned:
            stats.rows_skipped_unrepairable_version_history += 1
            return None
        set_qa(row, question, cleaned)
        stats.version_history_rows_repaired += 1
        stats.record_example("version_history", source_row, row)
        stats.canonical_output_rows += 1
        return row

    set_qa(row, question, answer)
    stats.other_rows_preserved += 1
    stats.canonical_output_rows += 1
    return row


def paraphrase_questions(row: Mapping[str, Any]) -> List[str]:
    switch = str(row.get("switch") or "").strip()
    version = str(row.get("version") or "").replace("_", ".").strip()
    sub_version = str(row.get("sub_version") or "").strip()
    display_version = version
    if sub_version and normalize(sub_version) not in {"base", "none", "n/a"}:
        display_version = f"{version}.{sub_version}"
    command = command_value(row)
    prefix = f"For {switch} AOS-CX {display_version},"
    return [
        f"{prefix} what is the syntax of the {command} command?",
        f"{prefix} give the exact syntax of {command}.",
        f"{prefix} what is the command syntax for {command}?",
        f"{prefix} show the syntax for {command}.",
        f"{prefix} how do I use the {command} command?",
    ]


def option_present(option: str, command: str, syntaxes: Iterable[str]) -> bool:
    haystack = " ".join((command, *syntaxes)).casefold().replace("_", "-")
    candidate = option.casefold().replace("_", "-")
    return bool(re.search(rf"(?<![a-z0-9-]){re.escape(candidate)}(?![a-z0-9-])", haystack))


def augment_cli_rows(
    canonical_rows: Sequence[Dict[str, Any]],
    stats: RepairStats,
    paraphrases_per_group: int,
    negatives_per_group: int,
) -> List[Dict[str, Any]]:
    augmented: List[Dict[str, Any]] = []
    syntax_groups: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    command_syntaxes: Dict[str, set[str]] = defaultdict(set)
    for row in canonical_rows:
        question, _ = extract_qa(row)
        syntax = syntax_value(row)
        if is_cli_row(row) and syntax:
            command_syntaxes[command_identity(row)].add(syntax)
            if is_syntax_question(question):
                syntax_groups[fact_group_key(row)].append(row)

    for group_key in sorted(syntax_groups):
        source = sorted(syntax_groups[group_key], key=lambda item: stable_digest(extract_qa(item)[0]))[0]
        _, source_answer = extract_qa(source)
        existing_questions = {normalize(extract_qa(item)[0]) for item in syntax_groups[group_key]}
        added = 0
        for question in paraphrase_questions(source):
            if added >= paraphrases_per_group:
                break
            if normalize(question) in existing_questions:
                continue
            item = deepcopy(source)
            set_qa(item, question, source_answer)
            item["augmentation_type"] = "cli_syntax_paraphrase"
            augmented.append(item)
            existing_questions.add(normalize(question))
            stats.paraphrase_rows_added += 1
            added += 1

        syntax_pool = command_syntaxes[command_identity(source)]
        negative_added = 0
        for option in NEGATIVE_OPTIONS:
            if negative_added >= negatives_per_group:
                break
            if option_present(option, command_value(source), syntax_pool):
                continue
            switch = str(source.get("switch") or "").strip()
            version = str(source.get("version") or "").replace("_", ".").strip()
            sub_version = str(source.get("sub_version") or "").strip()
            display_version = version if normalize(sub_version) in {"", "base", "none", "n/a"} else f"{version}.{sub_version}"
            question = (
                f"For {switch} AOS-CX {display_version}, is the {option} option documented "
                f"for the {command_value(source)} command?"
            )
            item = deepcopy(source)
            set_qa(item, question, NOT_DOCUMENTED_ANSWER)
            item["augmentation_type"] = "unsupported_cli_option"
            item["unsupported_option"] = option
            augmented.append(item)
            stats.negative_examples_added += 1
            negative_added += 1
    return augmented


def deduplicate_rows(rows: Sequence[Dict[str, Any]], stats: RepairStats) -> List[Dict[str, Any]]:
    by_question: Dict[str, Tuple[str, Dict[str, Any]]] = {}
    for row in rows:
        question, answer = extract_qa(row)
        key = normalize(question)
        answer_key = normalize(answer)
        if key not in by_question:
            by_question[key] = (answer_key, row)
            continue
        if by_question[key][0] == answer_key:
            stats.duplicate_questions_removed += 1
        else:
            stats.conflicting_questions_removed += 1
    return [pair[1] for pair in by_question.values()]


def grouped_stratified_split(
    rows: Sequence[Dict[str, Any]], seed: int, ratios: Mapping[str, float]
) -> Dict[str, List[Dict[str, Any]]]:
    if not math.isclose(sum(ratios.values()), 1.0, abs_tol=1e-9):
        raise ValueError("Split ratios must sum to 1.0")
    split_names = tuple(ratios)
    groups: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for row in rows:
        groups[fact_group_key(row)].append(row)

    stratum_totals: Counter[str] = Counter(stratum_key(row) for row in rows)
    global_targets = {name: len(rows) * ratios[name] for name in split_names}
    stratum_targets = {
        stratum: {name: total * ratios[name] for name in split_names}
        for stratum, total in stratum_totals.items()
    }
    current_global: Counter[str] = Counter()
    current_strata: Dict[str, Counter[str]] = defaultdict(Counter)
    assignments: Dict[str, str] = {}

    ordered_groups = sorted(
        groups,
        key=lambda key: (-len(groups[key]), stable_digest(f"{seed}|{key}")),
    )
    for group_key in ordered_groups:
        group_rows = groups[group_key]
        group_strata = Counter(stratum_key(row) for row in group_rows)
        scores: List[Tuple[float, str]] = []
        for split in split_names:
            global_need = max(global_targets[split] - current_global[split], 0.0)
            benefit = min(global_need, len(group_rows))
            for stratum, count in group_strata.items():
                need = max(stratum_targets[stratum][split] - current_strata[stratum][split], 0.0)
                benefit += 8.0 * min(need, count)
            overshoot = max(current_global[split] + len(group_rows) - global_targets[split], 0.0)
            tie = int(stable_digest(f"{seed}|{group_key}|{split}")[:12], 16) / float(16**12)
            scores.append((benefit - 0.25 * overshoot + tie * 1e-6, split))
        chosen = max(scores)[1]
        assignments[group_key] = chosen
        current_global[chosen] += len(group_rows)
        for stratum, count in group_strata.items():
            current_strata[stratum][chosen] += count

    result = {name: [] for name in split_names}
    for group_key, group_rows in groups.items():
        result[assignments[group_key]].extend(group_rows)
    for offset, split in enumerate(split_names):
        random.Random(seed + offset * 1009).shuffle(result[split])
    return result


def read_jsonl(path: Path) -> Iterator[Dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                row = json.loads(line, parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))
            except Exception as exc:
                raise ValueError(f"Invalid JSON at {path}:{line_number}: {exc}") from exc
            if not isinstance(row, dict):
                raise ValueError(f"Expected object at {path}:{line_number}")
            yield row


def write_jsonl(path: Path, rows: Iterable[Mapping[str, Any]]) -> int:
    count = 0
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(remove_nulls(dict(row)), ensure_ascii=False, allow_nan=False, separators=(",", ":")))
            handle.write("\n")
            count += 1
    return count


def write_json(path: Path, payload: Any) -> None:
    path.write_text(
        json.dumps(payload, ensure_ascii=False, allow_nan=False, indent=2) + "\n",
        encoding="utf-8",
    )


def distribution(rows: Iterable[Mapping[str, Any]], field_name: str) -> Dict[str, int]:
    return dict(sorted(Counter(str(row.get(field_name) or "") for row in rows).items()))


def ensure_safe_output(inputs: Sequence[Path], output_dir: Path, force: bool) -> None:
    resolved_inputs = {path.resolve() for path in inputs}
    resolved_output = output_dir.resolve()
    if resolved_output in resolved_inputs:
        raise ValueError("Output directory cannot be an input file")
    for path in resolved_inputs:
        if resolved_output == path.parent:
            raise ValueError("Refusing to write outputs beside/over source files")
    existing = [output_dir / name for name in (*SPLIT_FILENAMES.values(), "manifest.json")]
    if any(path.exists() for path in existing) and not force:
        raise FileExistsError(f"Output already exists under {output_dir}; pass --force to replace existing outputs")
    output_dir.mkdir(parents=True, exist_ok=True)


def build_dataset(args: argparse.Namespace) -> Dict[str, Any]:
    inputs = [Path(path) for path in args.input]
    for path in inputs:
        if not path.is_file():
            raise FileNotFoundError(path)
    output_dir = Path(args.output_dir)
    ensure_safe_output(inputs, output_dir, args.force)

    stats = RepairStats()
    canonical: List[Dict[str, Any]] = []
    for path in inputs:
        for source_row in read_jsonl(path):
            repaired = repair_row(source_row, stats)
            if repaired is not None:
                canonical.append(repaired)

    augmented = augment_cli_rows(
        canonical,
        stats,
        paraphrases_per_group=args.paraphrases_per_group,
        negatives_per_group=args.negatives_per_group,
    )
    cleaned = deduplicate_rows([*canonical, *augmented], stats)
    stats.output_rows = len(cleaned)

    splits = grouped_stratified_split(
        cleaned,
        seed=args.seed,
        ratios={"train": args.train_ratio, "validation": args.val_ratio, "test": args.test_ratio},
    )
    output_files: Dict[str, Dict[str, Any]] = {}
    for split, filename in SPLIT_FILENAMES.items():
        path = output_dir / filename
        rows_written = write_jsonl(path, splits[split])
        output_files[split] = {
            "path": str(path),
            "rows": rows_written,
            "sha256": sha256_file(path),
        }

    source_files = {
        str(path): {"rows": sum(1 for _ in read_jsonl(path)), "sha256": sha256_file(path)}
        for path in inputs
    }
    manifest = {
        "seed": args.seed,
        "ratios": {"train": args.train_ratio, "validation": args.val_ratio, "test": args.test_ratio},
        "paraphrases_per_cli_syntax_group": args.paraphrases_per_group,
        "negatives_per_cli_syntax_group": args.negatives_per_group,
        "source_files": source_files,
        "source_files_preserved": True,
        "output_files": output_files,
        "stats": stats.as_dict(),
        "split_distributions": {
            split: {
                field_name: distribution(rows, field_name)
                for field_name in ("source_type", "data_family", "switch", "version")
            }
            for split, rows in splits.items()
        },
    }
    write_json(output_dir / "manifest.json", manifest)
    write_json(output_dir / "repair_summary.json", stats.as_dict())
    write_json(output_dir / "examples_before_after.json", dict(stats.examples))

    print(f"Input rows: {stats.input_rows}")
    print(f"Output rows: {stats.output_rows}")
    print(f"Rows skipped due to noise: {stats.rows_skipped_due_to_noise}")
    print(f"CLI syntax rows repaired: {stats.cli_syntax_rows_repaired}")
    print(f"CLI description rows repaired: {stats.cli_description_rows_repaired}")
    print(f"Version history rows repaired: {stats.version_history_rows_repaired}")
    print(f"Bug rows preserved: {stats.bug_rows_preserved}")
    print(f"Paraphrase rows added: {stats.paraphrase_rows_added}")
    print(f"Negative examples added: {stats.negative_examples_added}")
    print(f"Train rows: {len(splits['train'])}")
    print(f"Validation rows: {len(splits['validation'])}")
    print(f"Test rows: {len(splits['test'])}")
    print(f"Manifest: {output_dir / 'manifest.json'}")
    return manifest


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", action="append", default=None, help="Input JSONL; repeat for multiple files")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--train-ratio", type=float, default=0.8)
    parser.add_argument("--val-ratio", type=float, default=0.1)
    parser.add_argument("--test-ratio", type=float, default=0.1)
    parser.add_argument("--paraphrases-per-group", type=int, default=4, choices=range(3, 6))
    parser.add_argument("--negatives-per-group", type=int, default=1, choices=range(0, 3))
    parser.add_argument("--force", action="store_true", help="Replace existing outputs, never source files")
    args = parser.parse_args(argv)
    if args.input is None:
        args.input = [str(path) for path in DEFAULT_INPUTS]
    if min(args.train_ratio, args.val_ratio, args.test_ratio) <= 0:
        parser.error("All split ratios must be positive")
    if not math.isclose(args.train_ratio + args.val_ratio + args.test_ratio, 1.0, abs_tol=1e-9):
        parser.error("Split ratios must sum to 1.0")
    return args


def main() -> None:
    build_dataset(parse_args())


if __name__ == "__main__":
    main()
