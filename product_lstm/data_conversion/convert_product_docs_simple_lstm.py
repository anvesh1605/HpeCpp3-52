#!/usr/bin/env python3
"""Convert product documentation chat rows into a simple LSTM JSONL dataset."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Dict, Iterable, Iterator, List, Mapping, Optional, Sequence, Tuple


CLI_SYNTAX_RE = re.compile(
    r"(?i)(?:\bwhat\s+is\s+the\s+(?:exact\s+)?syntax\b|\bexact\s+syntax\b|"
    r"\bcommand\s+syntax\b|\bsyntax\s+of\b|\bgive\s+(?:me\s+)?the\s+(?:exact\s+)?syntax\b|"
    r"\bshow\s+the\s+syntax\b|\bsyntax\b)"
)
CLI_MEANING_RE = re.compile(r"(?i)\bwhat\s+does\b|\bwhat\s+is\b|\bdescribe\b|\bmeaning\b")
CONFIG_RE = re.compile(r"(?i)\bhow\s+do\s+you\s+configure\b|\bconfigure\b")
CONCEPT_RE = re.compile(r"(?i)\bwhat\s+is\b|\bconcept\b|\bwhat\s+does\s+the\s+guide\s+say\s+about\b")
SNMP_RE = re.compile(r"(?i)\bsnmp\b|\bmib\b")
EVENT_RE = re.compile(r"(?i)\bevent\s+log\b|\bevent\s+id\b")
TROUBLESHOOT_RE = re.compile(r"(?i)\btroubleshoot\b|\btroubleshooting\b")
LIMITATION_RE = re.compile(
    r"(?i)\b(limitation|limitations|not supported|unsupported|cannot|can't|unable to|restriction|not available)\b"
)
REQUIREMENT_RE = re.compile(
    r"(?i)\b(requirement|required|requires|prerequisite|prerequisites|needed|need to|must)\b"
)
CAVEAT_RE = re.compile(r"(?i)\b(caveat|warning|caution|important note|important)\b")
PLACEHOLDER_RE = re.compile(r"(?i)<(?:COMMAND|FEATURE|TOPIC|OBJECT_NAME|OBJECT|VALUE|PARAMETER|PLACEHOLDER|ANSWER)>")
VERSION_RE = re.compile(r"\b(\d{1,2}\.\d{1,2}(?:\.\d{3,5})?)\b")


def normalize(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "").replace("\r\n", "\n").replace("\r", "\n")).strip()


def collapse(value: Any) -> str:
    return re.sub(r"\s+", " ", normalize(value))


def lower(value: Any) -> str:
    return collapse(value).casefold()


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def short_hash(*parts: Any, size: int = 10) -> str:
    seed = "\n".join(collapse(part) for part in parts)
    return sha256_text(seed)[:size]


def display_version(value: Any) -> str:
    return collapse(value).replace("_", ".")


def first_message(row: Mapping[str, Any], role: str) -> str:
    for message in row.get("messages") or []:
        if isinstance(message, Mapping) and lower(message.get("role")) == role:
            return collapse(message.get("content"))
    return ""


def extract_qa(row: Mapping[str, Any]) -> Tuple[str, str]:
    question = first_message(row, "user") or collapse(row.get("question"))
    answer = first_message(row, "assistant") or collapse(row.get("answer"))
    return question, answer


def command_value(row: Mapping[str, Any], question: str = "", answer: str = "") -> str:
    explicit = collapse(row.get("command") or row.get("command_name"))
    if explicit:
        return explicit

    text = question
    patterns = [
        r"(?i)\bwhat is the syntax of the (?P<command>.+?) command\b",
        r"(?i)\bwhat is the syntax of (?P<command>.+?) command\b",
        r"(?i)\bwhat is the syntax of the (?P<command>.+?)\b",
        r"(?i)\bwhat does the (?P<command>.+?) command do\b",
        r"(?i)\bwhat does the (?P<command>.+?) do\b",
        r"(?i)\bsyntax:\s*(?P<command>.+?)(?:[.\n]|$)",
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return collapse(match.group("command"))
    return ""


def primary_topic(row: Mapping[str, Any], question: str, answer: str) -> str:
    candidates = [
        row.get("topic"),
        row.get("feature"),
        row.get("object_name"),
        row.get("section"),
        row.get("document_title"),
        row.get("source_file"),
    ]
    for candidate in candidates:
        cleaned = collapse(candidate)
        if cleaned:
            return cleaned

    for text in (question, answer):
        match = re.search(r"(?i)\babout\s+(.+?)(?:\?|$)", text)
        if match:
            return collapse(match.group(1))
    return short_hash(question, answer)


def source_domain(row: Mapping[str, Any]) -> str:
    source_type = lower(row.get("source_type"))
    data_family = lower(row.get("data_family"))
    if source_type.startswith("product_") or data_family:
        return "product_docs"
    return "other"


def is_show_command(command: str, question: str, answer: str) -> bool:
    text = " ".join(filter(None, (command, question, answer))).casefold()
    return bool(re.search(r"\bshow\b", text))


def has_syntax_signal(question: str) -> bool:
    return bool(CLI_SYNTAX_RE.search(question))


def has_meaning_signal(question: str) -> bool:
    return bool(CLI_MEANING_RE.search(question))


def product_intent(row: Mapping[str, Any], question: str, answer: str) -> str:
    family = lower(row.get("data_family"))
    source_type = lower(row.get("source_type"))
    command = command_value(row, question, answer)
    text = " ".join(
        collapse(part)
        for part in (
            question,
            answer,
            row.get("section"),
            row.get("topic"),
            row.get("document_title"),
            row.get("source_file"),
        )
        if collapse(part)
    )

    if family in {"cli_command_reference", "show_command_reference"} or source_type == "product_cli_reference" or command:
        if is_show_command(command, question, answer) or family == "show_command_reference":
            if has_syntax_signal(question):
                return "show_command_syntax"
            if has_meaning_signal(question):
                return "show_command_meaning"
            return "show_command_syntax" if command else "show_command_meaning"
        if has_syntax_signal(question):
            return "cli_syntax"
        if has_meaning_signal(question):
            return "cli_meaning"
        return "cli_syntax" if command else "cli_meaning"
    if family == "event_log_reference" or source_type == "product_event_log_reference" or EVENT_RE.search(text):
        return "event_log_meaning"
    if family == "configuration_procedure" or CONFIG_RE.search(text):
        return "configuration_procedure"
    if family == "concept_explanation" or (CONCEPT_RE.search(text) and not command):
        return "concept_explanation"
    if family == "snmp_mib_reference" or SNMP_RE.search(text):
        return "snmp_mib_info"
    if family == "troubleshooting" or TROUBLESHOOT_RE.search(text):
        return "troubleshooting"
    if family == "feature_limitation" or LIMITATION_RE.search(text):
        return "product_limitation"
    if REQUIREMENT_RE.search(text):
        return "product_requirement"
    if CAVEAT_RE.search(text):
        return "product_caveat"
    return "product_generic"


def clean_target_value(intent: str, answer: str) -> str:
    value = collapse(answer)
    if intent in {"cli_syntax", "show_command_syntax"}:
        match = re.search(r"(?is)\bsyntax\s*:\s*(.+)$", value)
        if match:
            return collapse(match.group(1))
        return value
    if intent in {"cli_meaning", "show_command_meaning"}:
        value = re.split(r"(?is)\bsyntax\s*:\s*", value, maxsplit=1)[0].strip()
        return value
    if intent == "event_log_meaning":
        value = re.sub(r"(?is)^event\s+id\s*:\s*", "", value).strip()
        value = re.sub(r"(?is)^event\s+meaning\s*:\s*", "", value).strip()
        return value
    return value


def build_input_text(intent: str, row: Mapping[str, Any], question: str, answer: str) -> str:
    switch = collapse(row.get("switch"))
    version = display_version(row.get("version"))
    command = command_value(row, question, answer)
    topic = primary_topic(row, question, answer)
    prompt_topic = re.sub(r"(?i)^about\s+", "", topic).strip()
    feature = collapse(row.get("feature")) or topic
    object_name = collapse(row.get("object_name")) or topic
    event_id = collapse(row.get("event_id"))

    if switch and version:
        if intent in {"cli_syntax", "show_command_syntax"} and command:
            return f"For {switch} AOS-CX {version}, what is the syntax of the {command} command?"
        if intent in {"cli_meaning", "show_command_meaning"} and command:
            return f"For {switch} AOS-CX {version}, what does the {command} command do?"
        if intent == "configuration_procedure" and feature:
            return f"For {switch} AOS-CX {version}, how do you configure {feature}?"
        if intent == "concept_explanation" and prompt_topic:
            return f"For {switch} AOS-CX {version}, what is {prompt_topic}?"
        if intent == "snmp_mib_info" and object_name:
            return f"For {switch} AOS-CX {version}, what SNMP MIB information is documented for {object_name}?"
        if intent == "event_log_meaning" and (event_id or prompt_topic):
            subject = event_id or prompt_topic
            return f"For {switch} AOS-CX {version}, what does the event log entry {subject} mean?"
        if intent == "troubleshooting" and prompt_topic:
            return f"For {switch} AOS-CX {version}, how do you troubleshoot {prompt_topic}?"
        if intent == "product_caveat" and prompt_topic:
            return f"For {switch} AOS-CX {version}, what caveat is documented for {prompt_topic}?"
        if intent == "product_requirement" and prompt_topic:
            return f"For {switch} AOS-CX {version}, what requirement is documented for {prompt_topic}?"
        if intent == "product_limitation" and prompt_topic:
            return f"For {switch} AOS-CX {version}, what limitation is documented for {prompt_topic}?"
        if prompt_topic:
            return f"For {switch} AOS-CX {version}, what does the guide say about {prompt_topic}?"
    return collapse(question)


def build_slots(intent: str, row: Mapping[str, Any], question: str, answer: str) -> Dict[str, str]:
    slots: Dict[str, str] = {}
    for key in ("switch", "version"):
        value = collapse(row.get(key))
        if key == "version":
            value = display_version(value)
        if value:
            slots[key] = value

    sub_version = collapse(row.get("sub_version"))
    if sub_version:
        slots["sub_version"] = sub_version

    command = command_value(row, question, answer)
    if command and intent in {
        "cli_syntax",
        "cli_meaning",
        "show_command_syntax",
        "show_command_meaning",
    }:
        slots["command"] = command

    bug_id = collapse(row.get("bug_id"))
    if bug_id:
        slots["bug_id"] = bug_id

    event_id = collapse(row.get("event_id"))
    if event_id:
        slots["event_id"] = event_id

    feature = collapse(row.get("feature"))
    topic = primary_topic(row, question, answer)
    object_name = collapse(row.get("object_name"))

    if intent == "configuration_procedure" and (feature or topic):
        slots["feature"] = feature or topic
    elif intent == "concept_explanation" and topic:
        slots["topic"] = topic
    elif intent == "snmp_mib_info" and (object_name or topic):
        slots["object_name"] = object_name or topic
    elif intent in {"event_log_meaning", "troubleshooting", "product_caveat", "product_requirement", "product_limitation", "product_generic"} and topic:
        slots["topic"] = topic
    elif intent in {"cli_syntax", "cli_meaning", "show_command_syntax", "show_command_meaning"} and topic and "topic" not in slots:
        slots["topic"] = topic

    return slots


def review_reason(intent: str, question: str, answer: str, target_value: str, slots: Mapping[str, str]) -> Optional[str]:
    q = collapse(question)
    a = collapse(answer)
    if not q:
        return "empty_input_text"
    if not target_value:
        return "empty_target_value"
    if intent in {"cli_syntax", "show_command_syntax", "cli_meaning", "show_command_meaning"} and not slots.get("command"):
        return "missing_command"
    if PLACEHOLDER_RE.search(a) or PLACEHOLDER_RE.search(target_value):
        return "generic_template_text"
    if "syntax" in q.casefold() and intent not in {"cli_syntax", "show_command_syntax"}:
        return "intent_mismatch"
    if re.search(r"(?i)\bhow do you configure\b", q) and intent != "configuration_procedure":
        return "intent_mismatch"
    if not a:
        return "empty_target_value"
    return None


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


def find_input_files(inputs: Sequence[Path]) -> List[Path]:
    discovered: List[Path] = []
    seen: set[Path] = set()
    for path in inputs:
        if path.is_file():
            if path.name == "train_chat.jsonl" and path not in seen:
                discovered.append(path)
                seen.add(path)
            continue
        if not path.is_dir():
            raise FileNotFoundError(path)
        for candidate in path.rglob("train_chat.jsonl"):
            if any(part.lower() in {".venv", "__pycache__", "outputs", "logs"} for part in candidate.parts):
                continue
            if candidate not in seen:
                discovered.append(candidate)
                seen.add(candidate)
    return sorted(discovered)


def write_jsonl(path: Path, rows: Iterable[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def convert_file(path: Path) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]], Dict[str, Any]]:
    dataset_rows: List[Dict[str, Any]] = []
    review_rows: List[Dict[str, Any]] = []
    rows_by_intent: Counter[str] = Counter()
    review_reasons: Counter[str] = Counter()
    seen: set[str] = set()
    counts = {
        "rows_scanned": 0,
        "rows_written": 0,
        "review_rows": 0,
        "invalid_jsonl_lines": 0,
        "empty_input_text": 0,
        "empty_target_value": 0,
        "duplicates_removed": 0,
    }

    print(f"[INPUT] reading file {path}")
    for line_number, row in load_jsonl(path):
        counts["rows_scanned"] += 1
        print(f"[ROW] processing row number {line_number}")

        question, answer = extract_qa(row)
        if source_domain(row) != "product_docs":
            reason = "unsupported_source_domain"
            review_rows.append(
                {
                    "source_file": str(path),
                    "row_number": line_number,
                    "question": question,
                    "answer": answer,
                    "reason": reason,
                }
            )
            counts["review_rows"] += 1
            review_reasons[reason] += 1
            print("[REVIEW] review row written")
            continue

        intent = product_intent(row, question, answer)
        print(f"[INTENT] detected intent {intent}")

        slots = build_slots(intent, row, question, answer)
        print(f"[SLOTS] extracted slots {json.dumps(slots, ensure_ascii=False)}")

        target_value = clean_target_value(intent, answer)
        print(f"[TARGET] extracted target_value {target_value}")

        reason = review_reason(intent, question, answer, target_value, slots)
        if reason:
            review_rows.append(
                {
                    "source_file": str(path),
                    "row_number": line_number,
                    "question": question,
                    "answer": answer,
                    "intent": intent,
                    "slots": slots,
                    "target_value": target_value,
                    "reason": reason,
                }
            )
            counts["review_rows"] += 1
            review_reasons[reason] += 1
            print("[REVIEW] review row written")
            continue

        input_text = build_input_text(intent, row, question, answer)
        if not collapse(input_text):
            counts["empty_input_text"] += 1
            reason = "empty_input_text"
            review_rows.append(
                {
                    "source_file": str(path),
                    "row_number": line_number,
                    "question": question,
                    "answer": answer,
                    "intent": intent,
                    "slots": slots,
                    "target_value": target_value,
                    "reason": reason,
                }
            )
            counts["review_rows"] += 1
            review_reasons[reason] += 1
            print("[REVIEW] review row written")
            continue

        record = {
            "input_text": input_text,
            "intent": intent,
            "slots": slots,
            "target_value": target_value,
        }
        dedupe_key = json.dumps(record, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
        if dedupe_key in seen:
            counts["duplicates_removed"] += 1
            continue
        seen.add(dedupe_key)
        dataset_rows.append(record)
        rows_by_intent[intent] += 1
        counts["rows_written"] += 1
        print("[WRITE] dataset row written")

    report = {
        "rows_scanned": counts["rows_scanned"],
        "rows_written": counts["rows_written"],
        "review_rows": counts["review_rows"],
        "rows_by_intent": dict(sorted(rows_by_intent.items())),
        "review_reasons": dict(sorted(review_reasons.items())),
        "invalid_jsonl_lines": counts["invalid_jsonl_lines"],
        "empty_input_text": counts["empty_input_text"],
        "empty_target_value": counts["empty_target_value"],
        "duplicates_removed": counts["duplicates_removed"],
    }
    print(f"[QUALITY] final valid rows {counts['rows_written']}")
    return dataset_rows, review_rows, report


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    script_dir = Path(__file__).resolve().parent
    data_root = script_dir.parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        dest="inputs",
        action="append",
        type=Path,
        default=None,
        help="Input JSONL file or directory. May be supplied multiple times.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=data_root / "lstm_conversion" / "test_dataset.json",
        help="Output JSONL file for the dataset rows.",
    )
    parser.add_argument(
        "--review-output",
        type=Path,
        default=data_root / "lstm_conversion" / "test_review.jsonl",
        help="Output JSONL file for review rows.",
    )
    parser.add_argument(
        "--report-output",
        type=Path,
        default=data_root / "lstm_conversion" / "test_report.json",
        help="Output JSON file for the conversion report.",
    )
    parser.add_argument("--force", action="store_true", help="Overwrite existing outputs.")
    args = parser.parse_args(argv)
    if not args.inputs:
        args.inputs = [data_root / "full_product_docs"]
    return args


def main(argv: Optional[Sequence[str]] = None) -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    args = parse_args(argv)
    input_files = find_input_files(args.inputs)
    if not input_files:
        raise FileNotFoundError("No train_chat.jsonl files found")

    output_paths = [args.output, args.review_output, args.report_output]
    if not args.force:
        for path in output_paths:
            if path.exists():
                raise FileExistsError(f"Refusing to overwrite {path}; pass --force")

    if len(input_files) != 1:
        raise ValueError("This simple converter expects one input file at a time")

    dataset_rows, review_rows, report = convert_file(input_files[0])
    write_json(args.output, dataset_rows)
    print("[OUTPUT] saved dataset")
    write_jsonl(args.review_output, review_rows)
    print("[OUTPUT] saved review file")
    args.report_output.parent.mkdir(parents=True, exist_ok=True)
    args.report_output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("[OUTPUT] saved report")
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
