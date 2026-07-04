"""Safely rerun product-doc preprocessing for audit-flagged folders only.

Dry-run is the default. Use --execute to actually rerun eligible folders.
This script keeps the existing product-doc validators by calling
preprocess_product_docs.py with switch/version filters; it does not modify the
parser or release-note preprocessing.
"""

from __future__ import annotations

import argparse
import csv
import subprocess
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DEFAULT_RAW_ROOT = BASE_DIR / "markitdown_cli_output" / "Raw_Data_Product"
DEFAULT_OUTPUT_ROOT = BASE_DIR / "final_json" / "product_docs" / "full_product_docs"
DEFAULT_REPORT_DIR = BASE_DIR / "final_json" / "product_docs"
DEFAULT_AUDIT_CSV = DEFAULT_REPORT_DIR / "full_product_docs_missing_audit.csv"
DEFAULT_FINAL_JSONL = DEFAULT_REPORT_DIR / "train_chat_product_docs.jsonl"
DEFAULT_RERUN_LOG_DIR = DEFAULT_REPORT_DIR / "_rerun_logs"

DEFAULT_ELIGIBLE_STATUSES = {
    "zero_rows",
    "low_rows",
    "output_missing",
    "needs_manual_review",
}


def load_audit_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def is_truthy(value: str) -> bool:
    return str(value).strip().lower() in {"1", "true", "yes", "y"}


def eligible_rows(rows: list[dict[str, str]], statuses: set[str]) -> list[dict[str, str]]:
    selected: list[dict[str, str]] = []
    for row in rows:
        if row.get("status") not in statuses:
            continue
        if not is_truthy(row.get("raw_folder_exists", "")):
            continue
        try:
            raw_md_files = int(row.get("raw_md_files", "0") or 0)
        except ValueError:
            raw_md_files = 0
        if raw_md_files <= 0:
            continue
        selected.append(row)
    return selected


def count_jsonl_rows(path: Path) -> int:
    if not path.exists():
        return 0
    with path.open("r", encoding="utf-8", errors="replace") as handle:
        return sum(1 for _ in handle)


def rebuild_combined_jsonl(output_root: Path, final_jsonl: Path) -> int:
    final_jsonl.parent.mkdir(parents=True, exist_ok=True)
    total = 0
    train_files = sorted(output_root.glob("*/*/train_chat.jsonl"))
    with final_jsonl.open("w", encoding="utf-8", newline="") as out_handle:
        for train_file in train_files:
            with train_file.open("r", encoding="utf-8", errors="replace") as in_handle:
                for line in in_handle:
                    if not line.strip():
                        continue
                    out_handle.write(line if line.endswith("\n") else f"{line}\n")
                    total += 1
    return total


def run_preprocess_for_folder(
    *,
    row: dict[str, str],
    raw_root: Path,
    output_root: Path,
    temp_dir: Path,
    workers: int,
    python_exe: str,
) -> tuple[int, Path, Path]:
    switch = row["switch"]
    folder_version = row["folder_version"]
    temp_dir.mkdir(parents=True, exist_ok=True)
    safe_name = f"{switch}_{folder_version}".replace("/", "_").replace("\\", "_")
    temp_jsonl = temp_dir / f"{safe_name}.jsonl"
    stdout_log = temp_dir / f"{safe_name}.out.log"
    stderr_log = temp_dir / f"{safe_name}.err.log"
    command = [
        python_exe,
        "-u",
        "preprocess_product_docs.py",
        "--input-root",
        str(raw_root),
        "--output-root",
        str(output_root),
        "--final-jsonl",
        str(temp_jsonl),
        "--switch-name",
        switch,
        "--version",
        folder_version,
        "--workers",
        str(workers),
    ]
    with stdout_log.open("w", encoding="utf-8") as stdout_handle, stderr_log.open("w", encoding="utf-8") as stderr_handle:
        completed = subprocess.run(
            command,
            cwd=BASE_DIR,
            stdout=stdout_handle,
            stderr=stderr_handle,
            text=True,
            check=False,
        )
    return completed.returncode, stdout_log, stderr_log


def write_rerun_summary(
    *,
    path: Path,
    attempted: list[dict[str, str]],
    results: list[dict[str, object]],
    rows_before: int,
    rows_after: int,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "switch",
        "version",
        "subversion",
        "folder_version",
        "status",
        "old_final_rows",
        "new_final_rows",
        "rows_recovered",
        "returncode",
        "stdout_log",
        "stderr_log",
        "reason",
        "likely_reason",
    ]
    result_map = {(str(item["switch"]), str(item["folder_version"])): item for item in results}
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for row in attempted:
            result = result_map.get((row["switch"], row["folder_version"]), {})
            old_rows = int(row.get("final_rows", "0") or 0)
            new_rows = int(result.get("new_final_rows", old_rows) or 0)
            writer.writerow(
                {
                    "switch": row["switch"],
                    "version": row["version"],
                    "subversion": row["subversion"],
                    "folder_version": row["folder_version"],
                    "status": row["status"],
                    "old_final_rows": old_rows,
                    "new_final_rows": new_rows,
                    "rows_recovered": new_rows - old_rows,
                    "returncode": result.get("returncode", ""),
                    "stdout_log": result.get("stdout_log", ""),
                    "stderr_log": result.get("stderr_log", ""),
                    "reason": row.get("reason", ""),
                    "likely_reason": row.get("likely_reason", ""),
                }
            )
    print(f"Combined rows before rerun: {rows_before}")
    print(f"Combined rows after rerun: {rows_after}")
    print(f"Rerun summary CSV: {path}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Rerun product-doc preprocessing for audit-flagged folders.")
    parser.add_argument("--audit-csv", type=Path, default=DEFAULT_AUDIT_CSV)
    parser.add_argument("--raw-root", type=Path, default=DEFAULT_RAW_ROOT)
    parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT_ROOT)
    parser.add_argument("--final-jsonl", type=Path, default=DEFAULT_FINAL_JSONL)
    parser.add_argument("--log-dir", type=Path, default=DEFAULT_RERUN_LOG_DIR)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--python", default=sys.executable)
    parser.add_argument("--status", action="append", default=None, help="Eligible status to rerun. May be repeated.")
    parser.add_argument("--execute", action="store_true", help="Actually rerun folders. Default is dry-run.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    statuses = set(args.status or DEFAULT_ELIGIBLE_STATUSES)
    audit_rows = load_audit_rows(args.audit_csv)
    selected = eligible_rows(audit_rows, statuses)

    print(f"Eligible folders: {len(selected)}")
    for row in selected:
        print(
            f"{row['switch']}/{row['version']}/{row['folder_version']} "
            f"raw_md_files={row.get('raw_md_files', '0')} "
            f"old_final_rows={row.get('final_rows', '0')} "
            f"status={row.get('status', '')} "
            f"reason={row.get('likely_reason') or row.get('reason', '')}"
        )

    if not args.execute:
        print("Dry-run only. Re-run with --execute to overwrite eligible folder outputs.")
        return

    rows_before = count_jsonl_rows(args.final_jsonl)
    results: list[dict[str, object]] = []
    for index, row in enumerate(selected, start=1):
        print(f"[{index}/{len(selected)}] Rerunning {row['switch']} / {row['folder_version']}...")
        returncode, stdout_log, stderr_log = run_preprocess_for_folder(
            row=row,
            raw_root=args.raw_root,
            output_root=args.output_root,
            temp_dir=args.log_dir,
            workers=args.workers,
            python_exe=args.python,
        )
        train_path = args.output_root / row["switch"] / row["folder_version"] / "train_chat.jsonl"
        new_rows = count_jsonl_rows(train_path)
        print(f"  returncode={returncode} new_rows={new_rows}")
        results.append(
            {
                "switch": row["switch"],
                "folder_version": row["folder_version"],
                "returncode": returncode,
                "new_final_rows": new_rows,
                "stdout_log": str(stdout_log),
                "stderr_log": str(stderr_log),
            }
        )

    rows_after = rebuild_combined_jsonl(args.output_root, args.final_jsonl)
    write_rerun_summary(
        path=args.log_dir / "rerun_missing_product_docs_summary.csv",
        attempted=selected,
        results=results,
        rows_before=rows_before,
        rows_after=rows_after,
    )

    print("Regenerating audit and quality reports...")
    subprocess.run(
        [
            args.python,
            "audit_missing_product_docs.py",
            "--raw-root",
            str(args.raw_root),
            "--output-root",
            str(args.output_root),
            "--final-jsonl",
            str(args.final_jsonl),
            "--report-dir",
            str(DEFAULT_REPORT_DIR),
        ],
        cwd=BASE_DIR,
        check=False,
    )


if __name__ == "__main__":
    main()
