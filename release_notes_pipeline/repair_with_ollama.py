"""LLM-based JSONL repair utility using ChatOllama."""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Iterable, List


REPAIR_PROMPT = """
You are a dataset repair assistant for an Aruba AOS-CX release-notes fine-tuning dataset.

You are used inside a LangChain + Ollama pipeline.
The model may be llama3:8b, so follow the rules exactly and keep output simple.

TASK:
Repair and normalize existing JSONL records for training a compact networking LLM.

Each input record looks like:
{{
  "source_type": "release_notes_only",
  "switch": "...",
  "version": "...",
  "sub_version": "...",
  "messages": [
    {{"role": "user", "content": "..."}},
    {{"role": "assistant", "content": "..."}}
  ]
}}

GOAL:
Produce clean, factual, deduplicated Aruba release-notes QA records.

RULES:
- Keep only valid release-note records.
- Preserve source_type, switch, version, and sub_version.
- Preserve real category names exactly.
- Preserve real Bug IDs exactly.
- Do not invent new Bug IDs.
- Do not invent new symptoms, conditions, impacts, versions, switches, or workarounds.
- Remove fake-looking records such as Bug ID 123456, 789012, 000000, 999999, or placeholder categories.
- Remove generic or hallucinated category names.
- Remove duplicate or near-duplicate records.
- Repair grammar and incomplete sentences.
- Keep questions natural and useful for a network engineer.
- Keep answers concise and technical.

QUESTION RULES:
- The question must be clear.
- The question must mention either the Bug ID or the affected feature/category.
- Avoid repetitive wording.
- Do not create unsupported questions.

ANSWER RULES:
- Every answer must start exactly like:
  Category (Bug ID XXXXXX):

- Example:
  DHCP Snooping (Bug ID 325316): The switch drops valid DHCP packets when DHCP snooping is enabled on affected VLANs.

- The answer must describe only one main thing:
  symptom, condition, impact, or workaround.
- Do not mix unrelated facts.
- Do not use filler phrases like:
  "This issue occurs when"
  "It is observed that"
  "The problem is seen when"
- If no workaround is present in the input, write:
  Category (Bug ID XXXXXX): No workaround is documented.

DISCARD RULES:
Discard the record silently if:
- Bug ID is missing.
- Category is missing.
- Bug ID looks fake or placeholder.
- The answer is not grounded in the input.
- The question and answer do not match.
- The answer is too vague.
- The record is malformed.
- The record cannot be repaired confidently.

OUTPUT:
Return only valid JSONL.
One JSON object per line.
No markdown.
No explanation.
No code fence.

Output format:
{{"source_type":"release_notes_only","switch":"<switch>","version":"<version>","sub_version":"<sub_version>","messages":[{{"role":"user","content":"<repaired question>"}},{{"role":"assistant","content":"<repaired answer>"}}]}}

INPUT JSONL:
{entries}
""".strip()


def _call_ollama_generate(model: str, prompt: str, temperature: float, timeout_seconds: int) -> str:
    """Call the local Ollama HTTP API without importing LangChain."""
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": temperature,
            "num_predict": 2048,
            "num_ctx": 4096,
        },
    }
    data = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        "http://127.0.0.1:11434/api/generate",
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout_seconds) as response:
            response_payload = json.loads(response.read().decode("utf-8", errors="replace"))
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Ollama HTTP request failed: {exc}") from exc
    return str(response_payload.get("response", ""))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Repair chat JSONL dataset with an Ollama model.")
    parser.add_argument("--input-jsonl", type=Path, required=True)
    parser.add_argument("--output-jsonl", type=Path, required=True)
    parser.add_argument("--model", default="llama3:8b")
    parser.add_argument("--temperature", type=float, default=0.1)
    parser.add_argument("--timeout-seconds", type=int, default=60)
    parser.add_argument("--batch-size", type=int, default=20, help="Number of JSONL rows to repair per LLM call.")
    parser.add_argument(
        "--resume-output",
        action="store_true",
        help="Append to an existing output JSONL instead of overwriting it, and dedupe against existing lines.",
    )
    parser.add_argument(
        "--start-line",
        type=int,
        default=1,
        help="1-based input JSONL line number to start from. Use this to continue after a terminated run.",
    )
    return parser.parse_args()


def _valid_chat_object(payload: object) -> bool:
    if not isinstance(payload, dict):
        return False
    messages = payload.get("messages")
    if not isinstance(messages, list):
        return False
    if len(messages) < 2:
        return False
    user_found = False
    assistant_found = False
    for message in messages:
        if not isinstance(message, dict):
            return False
        role = str(message.get("role", "")).strip().lower()
        content = str(message.get("content", "")).strip()
        if not content:
            return False
        if role == "user":
            user_found = True
        if role == "assistant":
            assistant_found = True
    return user_found and assistant_found


def _chunked(items: List[str], size: int) -> Iterable[List[str]]:
    if size <= 0:
        size = 1
    for index in range(0, len(items), size):
        yield items[index : index + size]


def _load_jsonl_lines(path: Path) -> List[str]:
    return [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _sanitize_result(raw: str) -> tuple[List[str], int, int]:
    lines = [line.strip() for line in raw.splitlines() if line.strip()]
    kept: list[str] = []
    seen: set[str] = set()
    fixed = 0
    dropped = 0

    for line in lines:
        candidates = [line]
        candidates.append(re.sub(r"\"'\]\s*$", "\"}]}", line))
        candidates.append(re.sub(r"\"'\]\}\s*$", "\"}]}", line))
        accepted = None
        for candidate in candidates:
            try:
                parsed = json.loads(candidate)
            except json.JSONDecodeError:
                continue
            if not _valid_chat_object(parsed):
                continue
            normalized = json.dumps(parsed, ensure_ascii=False)
            accepted = normalized
            if candidate != line:
                fixed += 1
            break
        if accepted is None:
            dropped += 1
            continue
        if accepted in seen:
            continue
        seen.add(accepted)
        kept.append(accepted)

    return kept, fixed, dropped


def main() -> None:
    args = parse_args()
    input_lines = _load_jsonl_lines(args.input_jsonl)
    if args.start_line < 1:
        print("--start-line must be 1 or greater.", file=sys.stderr)
        raise SystemExit(1)
    if args.start_line > 1:
        skipped = min(args.start_line - 1, len(input_lines))
        input_lines = input_lines[skipped:]
    print(f"Using Ollama HTTP API with model={args.model}", flush=True)
    args.output_jsonl.parent.mkdir(parents=True, exist_ok=True)
    total_batches = max(1, (len(input_lines) + args.batch_size - 1) // args.batch_size)
    total_fixed = 0
    total_dropped = 0
    total_kept = 0
    seen: set[str] = set()
    existing_lines = 0

    if args.resume_output and args.output_jsonl.exists():
        for line in _load_jsonl_lines(args.output_jsonl):
            seen.add(line)
            existing_lines += 1

    print(
        f"Loaded {len(input_lines)} records from {args.input_jsonl}. "
        f"Processing {total_batches} batch(es) of up to {args.batch_size} records. "
        f"start_line={args.start_line}; existing_output_lines={existing_lines}",
        flush=True,
    )

    output_mode = "a" if args.resume_output else "w"
    with args.output_jsonl.open(output_mode, encoding="utf-8") as output_handle:
        for batch_index, batch in enumerate(_chunked(input_lines, args.batch_size), start=1):
            batch_entries = "\n".join(batch) + "\n"
            print(f"Batch {batch_index}/{total_batches}: sending {len(batch)} records to Ollama...", flush=True)
            try:
                result = _call_ollama_generate(
                    model=args.model,
                    prompt=REPAIR_PROMPT.format(entries=batch_entries),
                    temperature=args.temperature,
                    timeout_seconds=args.timeout_seconds,
                )
            except Exception as exc:  # pylint: disable=broad-except
                print(
                    f"Ollama repair failed on batch {batch_index}/{total_batches}: {exc}. "
                    f"Ensure Ollama is running and model '{args.model}' is installed.",
                    file=sys.stderr,
                )
                raise SystemExit(1)

            cleaned_lines, fixed_lines, dropped_lines = _sanitize_result(result)
            batch_kept = 0
            batch_dupes = 0
            for line in cleaned_lines:
                if line in seen:
                    batch_dupes += 1
                    continue
                seen.add(line)
                output_handle.write(line + "\n")
                batch_kept += 1

            output_handle.flush()
            total_fixed += fixed_lines
            total_dropped += dropped_lines
            total_kept += batch_kept
            print(
                f"Batch {batch_index}/{total_batches} complete: kept={batch_kept}, "
                f"duplicates_removed={batch_dupes}, fixed={fixed_lines}, dropped_invalid={dropped_lines}",
                flush=True,
            )

    if total_kept == 0:
        print("Ollama repair produced no valid JSONL lines.", file=sys.stderr)
        raise SystemExit(1)

    print(
        f"Done. kept={total_kept}, fixed_lines={total_fixed}, dropped_invalid_lines={total_dropped}.",
        flush=True,
    )


if __name__ == "__main__":
    main()
