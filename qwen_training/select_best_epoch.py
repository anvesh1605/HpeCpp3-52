#!/usr/bin/env python3
"""Select and copy the best epoch adapter from strict inference reports."""

from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path
from statistics import mean
from typing import Any, Dict, Tuple


DEFAULT_PRIMARY_SUITES = ("source_disjoint", "factual_recall")
DEFAULT_LEGACY_SUITE = "legacy65"
CRITICAL = (
    "bug_id_accuracy",
    "event_id_accuracy",
    "command_syntax_preservation",
    "command_name_accuracy",
    "date_accuracy",
)
ERRORS = (
    "wrong_bug_id_predictions", "fake_bug_id_predictions", "wrong_event_id_count", "fake_event_id_count",
    "missing_event_id_count", "wrong_cli_syntax_predictions", "wrong_date_predictions",
    "invented_workaround_predictions", "generic_hallucination_predictions", "false_abstention_predictions",
    "repetition_loop_predictions", "placeholder_template_predictions",
)


def assignment(value: str) -> Tuple[str, str]:
    label, separator, path = value.partition("=")
    if not separator or not label or not path:
        raise ValueError(f"Expected LABEL=PATH, got {value!r}")
    return label, path


def result_assignment(value: str) -> Tuple[str, str, Path]:
    left, path = assignment(value)
    epoch, separator, suite = left.partition(":")
    if not separator:
        raise ValueError(f"Expected EPOCH:SUITE=DIR, got {value!r}")
    return epoch, suite, Path(path)


def metrics(directory: Path) -> Dict[str, Any]:
    payload = json.loads((directory / "strict_inference_review.json").read_text(encoding="utf-8"))
    return payload["metrics"]


def numeric(value: Any) -> float:
    return 0.0 if value is None else float(value)


def epoch_number(label: str) -> int:
    match = re.search(r"(\d+)", label)
    return int(match.group(1)) if match else 10**9


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--epoch", action="append", required=True, metavar="LABEL=ADAPTER")
    parser.add_argument("--result", action="append", required=True, metavar="EPOCH:SUITE=DIR")
    parser.add_argument("--output_dir", type=Path, required=True)
    parser.add_argument("--copy_best", action="store_true")
    parser.add_argument(
        "--primary_suites",
        default=",".join(DEFAULT_PRIMARY_SUITES),
        help="Comma-separated primary suite labels used for ranking.",
    )
    parser.add_argument("--legacy_suite", default=DEFAULT_LEGACY_SUITE)
    parser.add_argument(
        "--allow_hard_failure_fallback",
        action="store_true",
        help="If every candidate has a loop/template failure, select the candidate with the fewest hard failures.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    primary_suites = tuple(item.strip() for item in args.primary_suites.split(",") if item.strip())
    if not primary_suites:
        raise ValueError("At least one primary suite is required")
    legacy_suite = args.legacy_suite.strip()
    if not legacy_suite:
        raise ValueError("legacy_suite cannot be empty")
    epochs = dict(assignment(value) for value in args.epoch)
    reports: Dict[str, Dict[str, Dict[str, Any]]] = {label: {} for label in epochs}
    report_paths: Dict[str, Dict[str, str]] = {label: {} for label in epochs}
    for value in args.result:
        epoch, suite, directory = result_assignment(value)
        if epoch not in epochs:
            raise ValueError(f"Result references unknown epoch: {epoch}")
        reports[epoch][suite] = metrics(directory)
        report_paths[epoch][suite] = str(directory)
    required = set(primary_suites) | {legacy_suite}
    for epoch, suites in reports.items():
        missing = required - set(suites)
        if missing:
            raise ValueError(f"{epoch} is missing suites: {sorted(missing)}")

    summaries: Dict[str, Dict[str, Any]] = {}
    for epoch, suites in reports.items():
        hard_failures = sum(numeric(summary.get("repetition_loop_predictions")) + numeric(summary.get("placeholder_template_predictions")) for summary in suites.values())
        primary = [suites[name] for name in primary_suites]
        critical_values = [numeric(summary.get(key)) for summary in primary for key in CRITICAL]
        summaries[epoch] = {
            "adapter_path": epochs[epoch],
            "eligible": hard_failures == 0,
            "hard_failure_count": int(hard_failures),
            "mean_primary_strict_score": round(mean(numeric(summary.get("average_score")) for summary in primary), 6),
            "critical_metric_mean": round(mean(critical_values), 6),
            "combined_strict_error_count": int(sum(numeric(summary.get(key)) for summary in primary for key in ERRORS)),
            "legacy_strict_score": numeric(suites[legacy_suite].get("average_score")),
            "epoch_number": epoch_number(epoch),
            "suite_metrics": suites,
            "suite_paths": report_paths[epoch],
        }
    eligible = [label for label, summary in summaries.items() if summary["eligible"]]
    selection_mode = "eligible_only"
    selection_pool = eligible
    if not selection_pool and args.allow_hard_failure_fallback:
        selection_pool = list(summaries)
        selection_mode = "fewest_hard_failures_fallback"
    selected = max(
        selection_pool,
        key=lambda label: (
            -summaries[label]["hard_failure_count"] if selection_mode != "eligible_only" else 0,
            summaries[label]["mean_primary_strict_score"], summaries[label]["critical_metric_mean"],
            -summaries[label]["combined_strict_error_count"], summaries[label]["legacy_strict_score"],
            -summaries[label]["epoch_number"],
        ),
        default=None,
    )
    args.output_dir.mkdir(parents=True, exist_ok=True)
    payload = {
        "selected_epoch": selected,
        "selected_adapter": epochs.get(selected) if selected else None,
        "validation_loss_used": False,
        "selection_mode": selection_mode,
        "primary_suites": list(primary_suites),
        "legacy_suite": legacy_suite,
        "epochs": summaries,
    }
    (args.output_dir / "best_epoch_selection.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    lines = ["# Best Epoch Selection", "", "Validation loss was not used for selection.", "", f"- Selected epoch: {selected or 'none'}", ""]
    for label, summary in sorted(summaries.items(), key=lambda item: item[1]["epoch_number"]):
        lines.extend([
            f"## {label}", "", f"- Eligible: {str(summary['eligible']).lower()}",
            f"- Mean primary strict score: {summary['mean_primary_strict_score']:.4f}",
            f"- Critical metric mean: {summary['critical_metric_mean']:.4f}",
            f"- Combined strict errors: {summary['combined_strict_error_count']}",
            f"- Legacy strict score: {summary['legacy_strict_score']:.4f}", "",
        ])
    (args.output_dir / "best_epoch_selection.md").write_text("\n".join(lines), encoding="utf-8")
    if selected and args.copy_best:
        source = Path(epochs[selected])
        destination = args.output_dir / "best_lora_adapters"
        if destination.exists():
            raise FileExistsError(f"Refusing to overwrite {destination}")
        shutil.copytree(
            source,
            destination,
            ignore=shutil.ignore_patterns(
                "optimizer.pt",
                "scheduler.pt",
                "rng_state*.pth",
                "trainer_state.json",
                "training_args.bin",
            ),
        )
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
