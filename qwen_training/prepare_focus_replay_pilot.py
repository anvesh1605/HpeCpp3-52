#!/usr/bin/env python3
"""Build the deterministic 50/50 focus-replay pilot and leakage-controlled holdout."""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import random
import re
from collections import Counter
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence, Set, Tuple


FOCUS_QUOTAS = {
    "release_notes_bug": 250,
    "cli_command_reference": 200,
    "show_command_reference": 150,
    "event_log_reference": 200,
    "release_notes_generic": 200,
}

REPLAY_QUOTAS = {
    "release_notes_bug": 150,
    "cli_command_reference": 150,
    "show_command_reference": 100,
    "event_log_reference": 100,
    "release_notes_generic": 100,
    "concept_explanation": 200,
    "snmp_mib_reference": 50,
    "configuration_procedure": 50,
    "routing_feature": 30,
    "monitoring_feature": 20,
    "rest_api_reference": 20,
    "feature_limitation": 10,
    "troubleshooting": 10,
    "security_policy": 5,
    "web_ui_task": 5,
}

HOLDOUT_QUOTAS = {
    "cli_command_reference": 20,
    "show_command_reference": 15,
    "release_notes_bug": 20,
    "event_log_reference": 15,
    "release_notes_generic": 15,
    "broad": 15,
}

TARGET_FAMILIES = set(HOLDOUT_QUOTAS) - {"broad"}
DATE_PATTERN = re.compile(
    r"(?i)(?:\b20\d{2}[-/]\d{1,2}[-/]\d{1,2}\b|"
    r"\b\d{1,2}\s+(?:jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|jun(?:e)?|"
    r"jul(?:y)?|aug(?:ust)?|sep(?:t(?:ember)?)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)\s+20\d{2}\b|"
    r"\b(?:jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|jun(?:e)?|jul(?:y)?|"
    r"aug(?:ust)?|sep(?:t(?:ember)?)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)\s+\d{1,2},?\s+20\d{2}\b)"
)


def normalize(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip().lower()


def message_content(row: Dict[str, Any], role: str) -> str:
    return next(
        (str(item.get("content", "")) for item in row.get("messages", []) if item.get("role") == role),
        "",
    )


def question_key(row: Dict[str, Any]) -> str:
    return normalize(message_content(row, "user"))


def reference(row: Dict[str, Any]) -> str:
    return message_content(row, "assistant")


def fact_key(row: Dict[str, Any]) -> Tuple[str, ...]:
    fields = (
        normalize(row.get("data_family")),
        normalize(row.get("source_file")),
        normalize(row.get("section")),
        normalize(row.get("topic")),
        normalize(row.get("command")),
        normalize(row.get("switch")),
        normalize(row.get("version")),
        normalize(row.get("sub_version")),
    )
    if any(fields[1:5]):
        return fields
    return fields + (question_key(row),)


def says_no_workaround(text: str) -> bool:
    lowered = normalize(text)
    return bool(
        re.search(r"\bno\s+(?:known\s+|documented\s+|specific\s+)?workarounds?\b", lowered)
        or "workaround is not documented" in lowered
        or "workaround is not available" in lowered
    )


def has_release_date(text: str) -> bool:
    return bool(DATE_PATTERN.search(text or ""))


def read_jsonl(path: Path) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON at {path}:{line_number}: {exc}") from exc
            validate_chatml_row(row, path, line_number)
            rows.append(row)
    return rows


def validate_chatml_row(row: Dict[str, Any], path: Path | str, line_number: int) -> None:
    messages = row.get("messages")
    if not isinstance(messages, list):
        raise ValueError(f"Missing messages list at {path}:{line_number}")
    user = message_content(row, "user").strip()
    assistant = message_content(row, "assistant").strip()
    if not user or not assistant:
        raise ValueError(f"Missing non-empty user/assistant content at {path}:{line_number}")


def read_legacy_questions(inference_script: Path, test_rows: Sequence[Dict[str, Any]]) -> Set[str]:
    tree = ast.parse(inference_script.read_text(encoding="utf-8"), filename=str(inference_script))
    manual_cases: List[Dict[str, Any]] = []
    for node in tree.body:
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        targets = node.targets if isinstance(node, ast.Assign) else [node.target]
        if any(isinstance(target, ast.Name) and target.id == "MANUAL_CASES" for target in targets):
            manual_cases = ast.literal_eval(node.value)
            break
    if len(manual_cases) != 15:
        raise ValueError(f"Expected 15 MANUAL_CASES in {inference_script}, found {len(manual_cases)}")
    questions = {normalize(case.get("question")) for case in manual_cases}
    questions.update(question_key(row) for row in test_rows[:50])
    if len(questions) != 65:
        raise ValueError(f"Expected 65 unique legacy questions, found {len(questions)}")
    return questions


def shuffled(rows: Iterable[Dict[str, Any]], rng: random.Random) -> List[Dict[str, Any]]:
    result = list(rows)
    rng.shuffle(result)
    return result


def take_unique(
    rows: Iterable[Dict[str, Any]],
    count: int,
    used_questions: Set[str],
    used_facts: Set[Tuple[str, ...]],
    reserve_selected_facts: bool = True,
) -> List[Dict[str, Any]]:
    selected: List[Dict[str, Any]] = []
    for row in rows:
        question = question_key(row)
        fact = fact_key(row)
        if not question or question in used_questions or fact in used_facts:
            continue
        selected.append(row)
        used_questions.add(question)
        if reserve_selected_facts:
            used_facts.add(fact)
        if len(selected) == count:
            return selected
    raise ValueError(f"Could select only {len(selected)}/{count} unique rows")


def select_holdout(
    candidates: Sequence[Dict[str, Any]], rng: random.Random
) -> List[Dict[str, Any]]:
    selected: List[Dict[str, Any]] = []
    used_questions: Set[str] = set()
    used_facts: Set[Tuple[str, ...]] = set()
    by_family: Dict[str, List[Dict[str, Any]]] = {}
    for row in candidates:
        by_family.setdefault(str(row.get("data_family", "")), []).append(row)

    for family, quota in HOLDOUT_QUOTAS.items():
        if family == "broad":
            pool = [row for row in candidates if row.get("data_family") not in TARGET_FAMILIES]
        else:
            pool = by_family.get(family, [])
        pool = shuffled(pool, rng)
        if family == "release_notes_bug":
            priority = [row for row in pool if says_no_workaround(reference(row))]
            remainder = [row for row in pool if not says_no_workaround(reference(row))]
            first = take_unique(priority, 8, used_questions, used_facts)
            selected.extend(first)
            selected.extend(take_unique(remainder + priority, quota - len(first), used_questions, used_facts))
        elif family == "release_notes_generic":
            priority = [row for row in pool if has_release_date(reference(row))]
            remainder = [row for row in pool if not has_release_date(reference(row))]
            first = take_unique(priority, 8, used_questions, used_facts)
            selected.extend(first)
            selected.extend(take_unique(remainder + priority, quota - len(first), used_questions, used_facts))
        else:
            selected.extend(take_unique(pool, quota, used_questions, used_facts))
    if len(selected) != 100:
        raise AssertionError(f"Holdout size is {len(selected)}, expected 100")
    return selected


def select_by_quotas(
    rows: Sequence[Dict[str, Any]],
    quotas: Dict[str, int],
    rng: random.Random,
    excluded_questions: Set[str],
    excluded_facts: Set[Tuple[str, ...]],
    bug_no_workaround_minimum: int = 0,
) -> List[Dict[str, Any]]:
    selected: List[Dict[str, Any]] = []
    used_questions = set(excluded_questions)
    used_facts = set(excluded_facts)
    by_family: Dict[str, List[Dict[str, Any]]] = {}
    for row in rows:
        by_family.setdefault(str(row.get("data_family", "")), []).append(row)
    for family, quota in quotas.items():
        pool = shuffled(by_family.get(family, []), rng)
        if family == "release_notes_bug" and bug_no_workaround_minimum:
            priority = [row for row in pool if says_no_workaround(reference(row))]
            remainder = [row for row in pool if not says_no_workaround(reference(row))]
            first = take_unique(
                priority,
                bug_no_workaround_minimum,
                used_questions,
                used_facts,
                reserve_selected_facts=False,
            )
            selected.extend(first)
            selected.extend(
                take_unique(
                    remainder + priority,
                    quota - len(first),
                    used_questions,
                    used_facts,
                    reserve_selected_facts=False,
                )
            )
        else:
            selected.extend(
                take_unique(
                    pool,
                    quota,
                    used_questions,
                    used_facts,
                    reserve_selected_facts=False,
                )
            )
    return selected


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_jsonl(path: Path, rows: Sequence[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")


def family_counts(rows: Sequence[Dict[str, Any]]) -> Dict[str, int]:
    return dict(sorted(Counter(str(row.get("data_family", "")) for row in rows).items()))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--focus_path", type=Path, default=Path("Data/all_switches/clean_repair_focus_manual_fixed.jsonl"))
    parser.add_argument("--replay_path", type=Path, default=Path("Data/all_switches/train_chat_all_clean.jsonl"))
    parser.add_argument("--test_path", type=Path, default=Path("Data/all_switches/test_chat_all_clean.jsonl"))
    parser.add_argument("--inference_script", type=Path, default=Path("run_inference_1000step_adapter.py"))
    parser.add_argument("--pilot_output", type=Path, default=Path("Data/all_switches/repair_pilot_50focus_50replay_seed42.jsonl"))
    parser.add_argument("--holdout_output", type=Path, default=Path("Data/all_switches/strict_holdout_unseen_100_seed42.jsonl"))
    parser.add_argument("--manifest_output", type=Path, default=Path("Data/all_switches/repair_pilot_50focus_50replay_seed42_manifest.json"))
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--overwrite", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    outputs = [args.pilot_output, args.holdout_output, args.manifest_output]
    existing = [path for path in outputs if path.exists()]
    if existing and not args.overwrite:
        raise FileExistsError(f"Refusing to overwrite existing outputs: {existing}")

    rng = random.Random(args.seed)
    focus_rows = read_jsonl(args.focus_path)
    replay_rows = read_jsonl(args.replay_path)
    test_rows = read_jsonl(args.test_path)
    legacy_questions = read_legacy_questions(args.inference_script, test_rows)
    focus_questions = {question_key(row) for row in focus_rows}
    replay_questions = {question_key(row) for row in replay_rows}

    holdout_candidates = [
        row
        for row in test_rows
        if question_key(row) not in focus_questions
        and question_key(row) not in replay_questions
        and question_key(row) not in legacy_questions
    ]
    holdout_rows = select_holdout(holdout_candidates, rng)
    holdout_questions = {question_key(row) for row in holdout_rows}
    holdout_facts = {fact_key(row) for row in holdout_rows}

    focus_selected = select_by_quotas(
        focus_rows,
        FOCUS_QUOTAS,
        rng,
        legacy_questions | holdout_questions,
        holdout_facts,
        bug_no_workaround_minimum=100,
    )
    selected_focus_questions = {question_key(row) for row in focus_selected}
    replay_selected = select_by_quotas(
        replay_rows,
        REPLAY_QUOTAS,
        rng,
        legacy_questions | holdout_questions | focus_questions | selected_focus_questions,
        holdout_facts,
    )

    pilot_rows = focus_selected + replay_selected
    rng.shuffle(pilot_rows)
    rng.shuffle(holdout_rows)

    pilot_questions = [question_key(row) for row in pilot_rows]
    if len(pilot_rows) != 2000 or len(set(pilot_questions)) != 2000:
        raise AssertionError("Pilot must contain exactly 2,000 unique questions")
    if set(pilot_questions) & holdout_questions:
        raise AssertionError("Pilot/holdout question leakage detected")
    if {fact_key(row) for row in pilot_rows} & holdout_facts:
        raise AssertionError("Pilot/holdout fact-key leakage detected")
    if set(pilot_questions) & legacy_questions:
        raise AssertionError("Pilot/legacy-65 question leakage detected")
    if len(focus_selected) != 1000 or len(replay_selected) != 1000:
        raise AssertionError("Pilot is not exactly 50/50 focus and replay")

    write_jsonl(args.pilot_output, pilot_rows)
    write_jsonl(args.holdout_output, holdout_rows)
    manifest = {
        "seed": args.seed,
        "source_files": {
            str(args.focus_path): {"rows": len(focus_rows), "sha256": sha256(args.focus_path)},
            str(args.replay_path): {"rows": len(replay_rows), "sha256": sha256(args.replay_path)},
            str(args.test_path): {"rows": len(test_rows), "sha256": sha256(args.test_path)},
            str(args.inference_script): {"sha256": sha256(args.inference_script)},
        },
        "pilot": {
            "path": str(args.pilot_output),
            "rows": len(pilot_rows),
            "focus_rows": len(focus_selected),
            "replay_rows": len(replay_selected),
            "family_counts": family_counts(pilot_rows),
            "focus_family_counts": family_counts(focus_selected),
            "replay_family_counts": family_counts(replay_selected),
            "no_workaround_focus_bug_rows": sum(
                says_no_workaround(reference(row)) for row in focus_selected if row.get("data_family") == "release_notes_bug"
            ),
            "sha256": sha256(args.pilot_output),
        },
        "holdout": {
            "path": str(args.holdout_output),
            "rows": len(holdout_rows),
            "candidate_rows_before_sampling": len(holdout_candidates),
            "family_counts": family_counts(holdout_rows),
            "no_workaround_bug_rows": sum(
                says_no_workaround(reference(row)) for row in holdout_rows if row.get("data_family") == "release_notes_bug"
            ),
            "release_date_rows": sum(
                has_release_date(reference(row)) for row in holdout_rows if row.get("data_family") == "release_notes_generic"
            ),
            "sha256": sha256(args.holdout_output),
        },
        "exclusions": {
            "legacy_questions": len(legacy_questions),
            "pilot_holdout_question_overlap": 0,
            "pilot_holdout_fact_overlap": 0,
            "pilot_legacy_question_overlap": 0,
        },
    }
    args.manifest_output.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(manifest, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
