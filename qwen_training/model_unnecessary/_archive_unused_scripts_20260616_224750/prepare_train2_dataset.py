import argparse
import hashlib
import json
import random
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple


def normalize_row(row: Dict[str, Any], source_file: Path, line_no: int) -> Dict[str, Any]:
    row = dict(row)
    row.setdefault("source_type", "release_notes_only")
    row.setdefault("data_family", "release_notes_bug" if "Bug" in json.dumps(row.get("messages", [])) else "unknown")
    row.setdefault("source_file", str(source_file).replace("\\", "/"))
    row.setdefault("source_line", line_no)
    return row


def first_message(row: Dict[str, Any], role: str) -> str:
    for message in row.get("messages", []):
        if str(message.get("role", "")).lower() == role:
            return str(message.get("content", "") or "").strip()
    return ""


def row_key(row: Dict[str, Any]) -> str:
    payload = {
        "switch": row.get("switch", ""),
        "version": row.get("version", ""),
        "sub_version": row.get("sub_version", ""),
        "user": first_message(row, "user"),
        "assistant": first_message(row, "assistant"),
    }
    encoded = json.dumps(payload, sort_keys=True, ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def valid_chat_row(row: Dict[str, Any]) -> Tuple[bool, str]:
    messages = row.get("messages")
    if not isinstance(messages, list) or not messages:
        return False, "missing_messages"
    user = first_message(row, "user")
    assistant = first_message(row, "assistant")
    if not user:
        return False, "missing_user"
    if not assistant:
        return False, "missing_assistant"
    if "raftraf" in assistant or "!!!!!" in assistant:
        return False, "degenerate_answer"
    return True, ""


def load_rows(paths: Iterable[Path]) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    seen = set()
    report: Dict[str, Any] = {
        "files": {},
        "bad_json_lines": [],
        "invalid_rows": {},
        "duplicate_rows": 0,
    }
    for path in paths:
        file_stats = {"valid": 0, "bad_json": 0, "invalid": 0}
        with path.open("r", encoding="utf-8-sig", errors="replace") as handle:
            for line_no, line in enumerate(handle, 1):
                text = line.strip()
                if not text:
                    continue
                try:
                    row = json.loads(text)
                except json.JSONDecodeError as exc:
                    file_stats["bad_json"] += 1
                    report["bad_json_lines"].append(
                        {
                            "file": str(path),
                            "line": line_no,
                            "error": str(exc),
                            "preview": text[:300],
                        }
                    )
                    continue
                row = normalize_row(row, path, line_no)
                ok, reason = valid_chat_row(row)
                if not ok:
                    file_stats["invalid"] += 1
                    report["invalid_rows"][reason] = report["invalid_rows"].get(reason, 0) + 1
                    continue
                key = row_key(row)
                if key in seen:
                    report["duplicate_rows"] += 1
                    continue
                seen.add(key)
                rows.append(row)
                file_stats["valid"] += 1
        report["files"][str(path)] = file_stats
    return rows, report


def write_jsonl(path: Path, rows: List[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="Prepare combined train2 all-switch JSONL splits.")
    parser.add_argument("--input_root", default="train2")
    parser.add_argument("--output_dir", default="train2/all_switches")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--val_ratio", type=float, default=0.05)
    parser.add_argument("--test_ratio", type=float, default=0.05)
    args = parser.parse_args()

    paths = sorted(Path(args.input_root).glob("gpu_run_*_llama3_8b/final_jsonl/*.jsonl"))
    rows, report = load_rows(paths)
    rng = random.Random(args.seed)
    rng.shuffle(rows)

    total = len(rows)
    test_count = int(total * args.test_ratio)
    val_count = int(total * args.val_ratio)
    test_rows = rows[:test_count]
    val_rows = rows[test_count : test_count + val_count]
    train_rows = rows[test_count + val_count :]

    output_dir = Path(args.output_dir)
    write_jsonl(output_dir / "train_chat_all_clean.jsonl", train_rows)
    write_jsonl(output_dir / "val_chat_all_clean.jsonl", val_rows)
    write_jsonl(output_dir / "test_chat_all_clean.jsonl", test_rows)

    report.update(
        {
            "input_files": len(paths),
            "total_clean_rows": total,
            "train_rows": len(train_rows),
            "val_rows": len(val_rows),
            "test_rows": len(test_rows),
            "seed": args.seed,
            "val_ratio": args.val_ratio,
            "test_ratio": args.test_ratio,
        }
    )
    with (output_dir / "dataset_report.json").open("w", encoding="utf-8") as handle:
        json.dump(report, handle, indent=2, ensure_ascii=False)
    print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
