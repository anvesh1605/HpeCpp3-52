import argparse
import json
import random
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple


UNKNOWN_ANSWER = "This information is not documented in the available training data."

FAKE_OR_NOISY_BUG_IDS = {
    "000000",
    "111111",
    "123456",
    "123457",
    "123458",
    "123459",
    "222222",
    "234567",
    "333333",
    "341596",
    "345678",
    "444444",
    "456789",
    "567890",
    "789012",
    "901234",
    "999999",
}

# Keep only high-confidence train2 rows that we inspected and know are internally consistent.
TRAIN2_ALLOWLIST_BUG_IDS = {"330012"}

GLOBAL_SAFETY_QUESTIONS = [
    "What symptom occurs in BGP Bug 123456?",
    "What is the workaround for Bug 999999?",
    "Explain VLAN Bug 789012.",
    "What is fixed in Bug 000000?",
    "Under what condition does OSPF Bug 111111 occur?",
    "What is the impact of Bug 222222?",
    "Which Aruba switch version has Bug 333333?",
    "Summarize Certificate Manager Bug 444444.",
    "Give me all bugs fixed in version 10.15.9999.",
    "List all known issues for Aruba 5420 with Bug ID 999999.",
]


def normalize_text(value: Any) -> str:
    text = str(value or "")
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    replacements = {
        "\u2010": "-",
        "\u2011": "-",
        "\u2012": "-",
        "\u2013": "-",
        "\u2014": "-",
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u00a0": " ",
        "Ã¢â‚¬Â": "-",
        "Ã¢â‚¬â€œ": "-",
        "Ã¢â‚¬â€": "-",
        "Ã¢â‚¬Ëœ": "'",
        "Ã¢â‚¬â„¢": "'",
        "Ã¢â‚¬Å“": '"',
        "Ã¢â‚¬Â": '"',
        "Ã‚ ": " ",
    }
    for bad, good in replacements.items():
        text = text.replace(bad, good)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def load_jsonl(path: Path) -> Iterable[Tuple[int, Dict[str, Any]]]:
    with path.open("r", encoding="utf-8-sig") as handle:
        for line_no, line in enumerate(handle, 1):
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            if isinstance(row, dict):
                yield line_no, row


def first_message(row: Dict[str, Any], role: str) -> str:
    for message in row.get("messages", []):
        if str(message.get("role", "")).lower() == role:
            return normalize_text(message.get("content", ""))
    return ""


def version_display(version: Any, sub_version: Any) -> str:
    version_text = normalize_text(version).replace("_", ".")
    sub_text = normalize_text(sub_version)
    if version_text and sub_text:
        return f"{version_text}.{sub_text}"
    return version_text or sub_text or "unknown"


def extract_bug_id(question: str, answer: str) -> Optional[str]:
    answer_match = re.search(r"\bBug ID\s*[:#-]?\s*(\d{5,7})\b", answer, flags=re.IGNORECASE)
    if answer_match:
        return answer_match.group(1)
    question_match = re.search(r"\bBug(?: ID)?\s*[:#-]?\s*(\d{5,7})\b", question, flags=re.IGNORECASE)
    return question_match.group(1) if question_match else None


def extract_category(question: str, answer: str) -> Optional[str]:
    prefix_match = re.match(r"\s*([^(:]{2,90})\s*\(\s*Bug ID\s+\d{5,7}\s*\)\s*:", answer, flags=re.IGNORECASE)
    if prefix_match:
        category = normalize_text(prefix_match.group(1))
        if category.lower() not in {"category", "category network", "category network engineering"}:
            return category

    question_match = re.search(r"\bin\s+(.+?)\s+Bug\s+\d{5,7}\b", question, flags=re.IGNORECASE)
    if question_match:
        category = normalize_text(question_match.group(1))
        category = re.sub(r"^(the|a|an)\s+", "", category, flags=re.IGNORECASE)
        if 2 <= len(category) <= 80 and "bug id" not in category.lower():
            return category
    return None


def extract_fact(answer: str) -> str:
    if "):" in answer:
        fact = answer.split("):", 1)[1]
    else:
        fact = re.sub(r"^\s*[^:]{2,120}:\s*", "", answer)
    return normalize_text(fact)


def qa_kind(question: str) -> str:
    lowered = question.lower()
    if "symptom" in lowered or "observable failure" in lowered:
        return "symptom"
    if "condition" in lowered or "trigger" in lowered or "when " in lowered:
        return "condition"
    if "workaround" in lowered:
        return "workaround"
    return "issue"


def is_malformed_question(question: str) -> bool:
    lowered = question.lower()
    if re.search(r"\bbug\s+\d{5,7}\s*\):", lowered):
        return True
    if len(question.split()) < 5:
        return True
    if "traceback" in lowered:
        return True
    return False


def parse_record(row: Dict[str, Any], source_name: str, split: str, line_no: int) -> Tuple[Optional[Dict[str, Any]], Optional[str]]:
    question = first_message(row, "user")
    answer = first_message(row, "assistant")
    if not question or not answer:
        return None, "missing_message"
    if is_malformed_question(question):
        return None, "malformed_question"
    bug_id = extract_bug_id(question, answer)
    if not bug_id:
        return None, "missing_bug_id"

    if source_name == "train2" and bug_id not in TRAIN2_ALLOWLIST_BUG_IDS:
        return None, "train2_not_allowlisted"
    if source_name != "train2" and bug_id in FAKE_OR_NOISY_BUG_IDS:
        return None, "fake_or_noisy_bug_id"

    category = extract_category(question, answer)
    if not category:
        return None, "missing_category"

    fact = extract_fact(answer)
    if len(fact.split()) < 4:
        return None, "short_fact"
    if "no workaround is documented" in fact.lower():
        return None, "workaround_fact"

    switch = normalize_text(row.get("switch", ""))
    version = normalize_text(row.get("version", ""))
    sub_version = normalize_text(row.get("sub_version", ""))
    if not switch or not version or not sub_version:
        return None, "missing_context"

    return {
        "source_name": source_name,
        "source_split": split,
        "source_line": line_no,
        "switch": switch,
        "version": version,
        "sub_version": sub_version,
        "version_display": version_display(version, sub_version),
        "bug_id": bug_id,
        "category": category,
        "fact": fact,
        "kind": qa_kind(question),
        "original_question": question,
        "original_answer": answer,
    }, None


def make_row(record: Dict[str, Any], question: str, answer: str, family: str = "release_notes_bug") -> Dict[str, Any]:
    return {
        "source_type": "train3_clean_release_notes",
        "data_family": family,
        "switch": record.get("switch", ""),
        "version": record.get("version", ""),
        "sub_version": record.get("sub_version", ""),
        "section": "Known Issues",
        "document_title": "Aruba AOS-CX release notes",
        "bug_id": record.get("bug_id", ""),
        "category": record.get("category", ""),
        "messages": [
            {"role": "user", "content": normalize_text(question)},
            {"role": "assistant", "content": normalize_text(answer)},
        ],
    }


def positive_answer(record: Dict[str, Any]) -> str:
    return f"{record['category']} (Bug ID {record['bug_id']}): {record['fact']}"


def positive_questions(record: Dict[str, Any]) -> List[str]:
    switch = record["switch"]
    ver = record["version_display"]
    category = record["category"]
    bug_id = record["bug_id"]
    kind = record["kind"]

    questions = []
    if kind == "symptom":
        questions.extend(
            [
                f"For {switch} Switch Series running AOS-CX {ver}, what symptom occurs in {category} Bug {bug_id}?",
                f"In AOS-CX {ver} on {switch}, what is the documented symptom for {category} Bug ID {bug_id}?",
            ]
        )
    elif kind == "condition":
        questions.extend(
            [
                f"For {switch} Switch Series running AOS-CX {ver}, under what condition does {category} Bug {bug_id} occur?",
                f"In AOS-CX {ver} on {switch}, what trigger or condition is documented for {category} Bug ID {bug_id}?",
            ]
        )
    else:
        questions.extend(
            [
                f"For {switch} Switch Series running AOS-CX {ver}, what is documented for {category} Bug {bug_id}?",
                f"In AOS-CX {ver} on {switch}, summarize {category} Bug ID {bug_id}.",
            ]
        )

    original = record["original_question"]
    if not is_malformed_question(original):
        questions.append(f"For {switch} Switch Series running AOS-CX {ver}, {original[0].lower() + original[1:]}")
    return questions


def negative_questions(record: Dict[str, Any], fake_bug_id: str) -> List[str]:
    switch = record["switch"]
    ver = record["version_display"]
    category = record["category"]
    bug_id = record["bug_id"]
    return [
        f"For {switch} Switch Series running AOS-CX {ver}, what symptom occurs in {category} Bug {fake_bug_id}?",
        f"For {switch} Switch Series running AOS-CX {ver}, what is the workaround for {category} Bug {bug_id}?",
        f"For {switch} Switch Series running AOS-CX {ver}, give me the exact CLI command to fix {category} Bug {bug_id}.",
    ]


def add_unique(rows: List[Dict[str, Any]], seen: set, row: Dict[str, Any]) -> None:
    user = row["messages"][0]["content"].lower()
    assistant = row["messages"][1]["content"].lower()
    key = (row.get("switch"), row.get("version"), row.get("sub_version"), user, assistant)
    if key not in seen:
        rows.append(row)
        seen.add(key)


def collect_records() -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    sources = []
    for split in ("train", "val", "test"):
        sources.append(("final_json", split, Path("final_json/all_switches") / f"{split}_chat_all_clean.jsonl"))
        sources.append(("train2", split, Path("train2/all_switches") / f"{split}_chat_all_clean.jsonl"))

    records: List[Dict[str, Any]] = []
    report: Dict[str, Any] = {
        "source_files": {},
        "drop_reasons": Counter(),
        "kept_by_source": Counter(),
        "kept_by_bug_id": Counter(),
    }

    for source_name, split, path in sources:
        if not path.exists():
            continue
        loaded = 0
        kept = 0
        for line_no, row in load_jsonl(path):
            loaded += 1
            record, reason = parse_record(row, source_name, split, line_no)
            if record is None:
                report["drop_reasons"][reason or "unknown"] += 1
                continue
            records.append(record)
            kept += 1
            report["kept_by_source"][f"{source_name}:{split}"] += 1
            report["kept_by_bug_id"][record["bug_id"]] += 1
        report["source_files"][str(path)] = {"loaded": loaded, "kept": kept}

    unique = {}
    for record in records:
        key = (
            record["switch"],
            record["version"],
            record["sub_version"],
            record["bug_id"],
            record["category"].lower(),
            record["kind"],
            record["fact"].lower(),
        )
        unique.setdefault(key, record)
    return list(unique.values()), report


def build_dataset(seed: int) -> Tuple[Dict[str, List[Dict[str, Any]]], Dict[str, Any]]:
    random.seed(seed)
    records, report = collect_records()
    fake_cycle = ["123456", "789012", "999999", "000000", "111111", "222222", "333333", "444444"]

    splits = {"train": [], "val": [], "test": []}
    seen_by_split = {name: set() for name in splits}

    for index, record in enumerate(records):
        split = record["source_split"] if record["source_split"] in splits else "train"
        answer = positive_answer(record)
        for question in positive_questions(record):
            add_unique(splits[split], seen_by_split[split], make_row(record, question, answer))

        fake_bug = fake_cycle[index % len(fake_cycle)]
        for question in negative_questions(record, fake_bug):
            add_unique(
                splits[split],
                seen_by_split[split],
                make_row(record, question, UNKNOWN_ANSWER, family="release_notes_safety_refusal"),
            )

    safety_template = {
        "switch": "",
        "version": "",
        "sub_version": "",
        "bug_id": "",
        "category": "",
    }
    for question in GLOBAL_SAFETY_QUESTIONS:
        add_unique(
            splits["train"],
            seen_by_split["train"],
            make_row(safety_template, question, UNKNOWN_ANSWER, family="release_notes_safety_refusal"),
        )

    for split_rows in splits.values():
        random.shuffle(split_rows)

    report["records_after_dedup"] = len(records)
    report["output_counts"] = {split: len(rows) for split, rows in splits.items()}
    report["output_family_counts"] = {
        split: Counter(row.get("data_family", "") for row in rows) for split, rows in splits.items()
    }
    report["kept_by_source"] = dict(report["kept_by_source"])
    report["kept_by_bug_id"] = dict(report["kept_by_bug_id"].most_common(30))
    report["drop_reasons"] = dict(report["drop_reasons"])
    report["unknown_answer"] = UNKNOWN_ANSWER
    report["fake_or_noisy_bug_ids_blocked"] = sorted(FAKE_OR_NOISY_BUG_IDS)
    report["train2_allowlist_bug_ids"] = sorted(TRAIN2_ALLOWLIST_BUG_IDS)
    return splits, report


def write_jsonl(path: Path, rows: List[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build clean train3 dataset from trusted Aruba release-note rows.")
    parser.add_argument("--output_dir", default="train3/all_switches")
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    splits, report = build_dataset(seed=args.seed)
    write_jsonl(output_dir / "train_chat_all_clean.jsonl", splits["train"])
    write_jsonl(output_dir / "val_chat_all_clean.jsonl", splits["val"])
    write_jsonl(output_dir / "test_chat_all_clean.jsonl", splits["test"])
    with (output_dir / "dataset_report.json").open("w", encoding="utf-8") as handle:
        json.dump(report, handle, indent=2, ensure_ascii=False)

    print(json.dumps(report["output_counts"], indent=2))
    print(f"Wrote train3 dataset to {output_dir}")


if __name__ == "__main__":
    main()
