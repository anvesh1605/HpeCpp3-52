#!/usr/bin/env python3
"""Select an adapter using strict holdout and legacy-suite metrics only."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any, Dict, List, Tuple

from strict_rescore_inference_outputs import strict_holdout_gate


HARD_FAILURE_KEYS = (
    "wrong_bug_id_predictions",
    "fake_bug_id_predictions",
    "wrong_event_id_count",
    "fake_event_id_count",
    "missing_event_id_count",
    "wrong_cli_syntax_predictions",
    "wrong_date_predictions",
    "invented_workaround_predictions",
    "generic_hallucination_predictions",
    "repetition_loop_predictions",
    "placeholder_template_predictions",
)


def read_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_candidate(spec: str) -> Tuple[str, str]:
    label, separator, adapter = spec.partition("=")
    if not separator or not label.strip() or not adapter.strip():
        raise ValueError(f"Invalid --candidate value {spec!r}; expected LABEL=ADAPTER_PATH")
    return label.strip(), adapter.strip()


def parse_suite(spec: str) -> Tuple[str, Path]:
    label, separator, directory = spec.partition("=")
    if not separator or not label.strip() or not directory.strip():
        raise ValueError(f"Invalid suite {spec!r}; expected LABEL=RESCORE_DIR")
    return label.strip(), Path(directory.strip())


def legacy_gate(candidate: Dict[str, Any], baseline: Dict[str, Any]) -> Dict[str, Any]:
    checks = {
        "strict_score_regression_within_0_10": candidate["average_score"] >= baseline["average_score"] - 0.10,
        **{
            f"{key}_not_higher": candidate[key] <= baseline[key]
            for key in HARD_FAILURE_KEYS
        },
    }
    return {
        "passed": all(checks.values()),
        "checks": checks,
        "failed_checks": [name for name, passed in checks.items() if not passed],
        "strict_score_delta": round(candidate["average_score"] - baseline["average_score"], 4),
    }


def critical_metric_mean(summary: Dict[str, Any]) -> float:
    values = [
        float(summary.get(key) or 0.0)
        for key in (
            "bug_id_accuracy",
            "event_id_accuracy",
            "command_syntax_preservation",
            "command_name_accuracy",
        )
    ]
    return sum(values) / len(values)


def combined_error_count(summary: Dict[str, Any]) -> int:
    return sum(int(summary.get(key) or 0) for key in HARD_FAILURE_KEYS)


def checkpoint_step(label: str) -> int:
    match = re.search(r"checkpoint[-_ ]?(\d+)", label, re.I)
    return int(match.group(1)) if match else 10**9


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--primary_suite", action="append", default=[], metavar="LABEL=RESCORE_DIR")
    parser.add_argument("--legacy_suite", action="append", default=[], metavar="LABEL=RESCORE_DIR")
    parser.add_argument("--baseline", action="append", default=[], metavar="LABEL=ADAPTER_PATH")
    parser.add_argument("--fallback_baseline_label", default=None)
    # Legacy flags are retained for the completed 1.5B pilot's selector invocation.
    parser.add_argument("--holdout_rescore_dir", type=Path, default=None)
    parser.add_argument("--legacy_rescore_dir", type=Path, default=None)
    parser.add_argument("--baseline_label", default=None)
    parser.add_argument("--baseline_adapter", default=None)
    parser.add_argument("--candidate", action="append", required=True, metavar="LABEL=ADAPTER_PATH")
    parser.add_argument("--output_dir", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    candidates = dict(parse_candidate(spec) for spec in args.candidate)
    baselines = dict(parse_candidate(spec) for spec in args.baseline)
    if args.baseline_label or args.baseline_adapter:
        if not args.baseline_label or not args.baseline_adapter:
            raise ValueError("--baseline_label and --baseline_adapter must be provided together.")
        baselines.setdefault(args.baseline_label, args.baseline_adapter)
    if not baselines:
        raise ValueError("At least one --baseline LABEL=ADAPTER_PATH is required.")
    primary_suites = dict(parse_suite(spec) for spec in args.primary_suite)
    legacy_suites = dict(parse_suite(spec) for spec in args.legacy_suite)
    if args.holdout_rescore_dir:
        primary_suites.setdefault("holdout", args.holdout_rescore_dir)
    if args.legacy_rescore_dir:
        legacy_suites.setdefault("legacy", args.legacy_rescore_dir)
    if not primary_suites or not legacy_suites:
        raise ValueError("Provide at least one --primary_suite and one --legacy_suite.")
    required_labels = set(baselines) | set(candidates)
    primary = {
        label: read_json(directory / "strict_rescore_summary.json")
        for label, directory in primary_suites.items()
    }
    legacy = {
        label: read_json(directory / "strict_rescore_summary.json")
        for label, directory in legacy_suites.items()
    }
    for suite_label, summary in {**primary, **legacy}.items():
        missing = required_labels - set(summary)
        if missing:
            raise ValueError(f"Suite {suite_label!r} is missing labels: {sorted(missing)}")

    results: Dict[str, Any] = {}
    for label, adapter in candidates.items():
        primary_results = {
            suite_label: {
                baseline_label: strict_holdout_gate(summary[label], summary[baseline_label])
                for baseline_label in baselines
            }
            for suite_label, summary in primary.items()
        }
        legacy_results = {
            suite_label: {
                baseline_label: legacy_gate(summary[label], summary[baseline_label])
                for baseline_label in baselines
            }
            for suite_label, summary in legacy.items()
        }
        passed = all(
            result["passed"]
            for suite in primary_results.values()
            for result in suite.values()
        ) and all(
            result["passed"]
            for suite in legacy_results.values()
            for result in suite.values()
        )
        source_suite = primary.get("source_disjoint") or next(iter(primary.values()))
        primary_scores = [summary[label]["average_score"] for summary in primary.values()]
        primary_critical_means = [critical_metric_mean(summary[label]) for summary in primary.values()]
        primary_errors = [combined_error_count(summary[label]) for summary in primary.values()]
        results[label] = {
            "adapter_path": adapter,
            "primary_suites": primary_results,
            "legacy_suites": legacy_results,
            "passed": passed,
            "selection_values": {
                "source_disjoint_strict_score": source_suite[label]["average_score"],
                "mean_primary_strict_score": round(sum(primary_scores) / len(primary_scores), 6),
                "critical_metric_mean": round(sum(primary_critical_means) / len(primary_critical_means), 6),
                "combined_strict_error_count": sum(primary_errors),
                "checkpoint_step": checkpoint_step(label),
            },
        }

    passing = [label for label, result in results.items() if result["passed"]]
    if passing:
        selected_label = max(
            passing,
            key=lambda label: (
                results[label]["selection_values"]["source_disjoint_strict_score"],
                results[label]["selection_values"]["mean_primary_strict_score"],
                results[label]["selection_values"]["critical_metric_mean"],
                -results[label]["selection_values"]["combined_strict_error_count"],
                -results[label]["selection_values"]["checkpoint_step"],
            ),
        )
        selected_adapter = candidates[selected_label]
        verdict = f"Select {selected_label}; it passed both strict suites and won the approved tie-break order."
    else:
        selected_label = args.fallback_baseline_label or args.baseline_label or next(iter(baselines))
        if selected_label not in baselines:
            raise ValueError(f"Fallback baseline {selected_label!r} was not provided in --baseline.")
        selected_adapter = baselines[selected_label]
        verdict = "Neither candidate passed every strict gate; keep metadatactx_1000 and do not continue training."

    payload = {
        "selection_basis": "strict_generated_answer_metrics_only",
        "eval_loss_used": False,
        "baselines": baselines,
        "primary_suites": {label: str(path) for label, path in primary_suites.items()},
        "legacy_suites": {label: str(path) for label, path in legacy_suites.items()},
        "selected_label": selected_label,
        "selected_adapter": selected_adapter,
        "automatic_continuation_allowed": False,
        "verdict": verdict,
        "candidates": results,
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "strict_checkpoint_selection.json").write_text(
        json.dumps(payload, indent=2) + "\n", encoding="utf-8"
    )
    lines: List[str] = [
        "# Strict Checkpoint Selection",
        "",
        "Eval loss was not used for checkpoint selection.",
        "",
        f"- Selected label: {selected_label}",
        f"- Selected adapter: `{selected_adapter}`",
        "- Automatic continuation: disabled",
        f"- Final verdict: {verdict}",
        "",
        "## Candidate Gates",
        "",
    ]
    for label, result in results.items():
        lines.extend(
            [
                f"### {label}",
                "",
                f"- Overall: {'PASS' if result['passed'] else 'FAIL'}",
                f"- Source-disjoint score: {result['selection_values']['source_disjoint_strict_score']:.2f}",
                f"- Mean primary score: {result['selection_values']['mean_primary_strict_score']:.2f}",
                "",
            ]
        )
        for suite_label, baseline_results in result["primary_suites"].items():
            for baseline_label, gate in baseline_results.items():
                lines.append(
                    f"- Primary {suite_label} vs {baseline_label}: {'PASS' if gate['passed'] else 'FAIL'} | "
                    f"failures: {', '.join(gate['failed_checks']) or 'none'}"
                )
        for suite_label, baseline_results in result["legacy_suites"].items():
            for baseline_label, gate in baseline_results.items():
                lines.append(
                    f"- Legacy {suite_label} vs {baseline_label}: {'PASS' if gate['passed'] else 'FAIL'} | "
                    f"failures: {', '.join(gate['failed_checks']) or 'none'}"
                )
        lines.append("")
    (args.output_dir / "strict_checkpoint_selection.md").write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
