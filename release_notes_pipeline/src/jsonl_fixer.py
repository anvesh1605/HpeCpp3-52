"""Deterministic JSONL formatter for chat data quality fixes."""

from __future__ import annotations

import json
import logging
import re
from pathlib import Path
from typing import Any

LOGGER = logging.getLogger(__name__)

# Passive filler patterns to replace
PASSIVE_FILLERS = {
    r"the issue is observed": "the issue occurs",
    r"the problem is seen": "the issue occurs",
    r"this is observed": "this occurs",
    r"is observed in": "occurs in",
    r"is seen in": "occurs in",
}

# Fragment fixes (missing conjunctions, etc.)
FRAGMENT_PATTERNS = {
    r"transition multiple times between acquiring, frequency locked": "transitions multiple times between acquiring and frequency locked",
    r"transitions multiple times between acquiring, frequency locked": "transitions multiple times between acquiring and frequency locked",
}

# Lowercase after colon patterns (answers should be capitalized)
LOWERCASE_AFTER_COLON = re.compile(r":\s+([a-z])")


def fix_passive_fillers(text: str) -> str:
    """Replace passive filler phrases with active ones."""
    for pattern, replacement in PASSIVE_FILLERS.items():
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    return text


def fix_fragments(text: str) -> str:
    """Fix incomplete/fragmented phrases."""
    for pattern, replacement in FRAGMENT_PATTERNS.items():
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    return text


def capitalize_after_colon(text: str) -> str:
    """Capitalize first letter after colon in answer."""
    def replacer(match):
        return ": " + match.group(1).upper()
    return LOWERCASE_AFTER_COLON.sub(replacer, text)


def fix_answer(answer: str) -> str:
    """Apply all answer fixes."""
    answer = fix_passive_fillers(answer)
    answer = fix_fragments(answer)
    answer = capitalize_after_colon(answer)
    answer = answer.strip()
    return answer


def fix_jsonl_line(line: str) -> dict[str, Any] | None:
    """
    Parse and fix a single JSONL line.
    Returns dict if valid, None if malformed.
    """
    line = line.strip()
    if not line:
        return None
    
    try:
        obj = json.loads(line)
    except json.JSONDecodeError as e:
        LOGGER.warning(f"Malformed JSON line, skipping: {e}")
        return None
    
    # Ensure structure
    if "messages" not in obj or not isinstance(obj["messages"], list):
        LOGGER.warning(f"Invalid messages structure, skipping: {obj}")
        return None
    
    if len(obj["messages"]) < 2:
        LOGGER.warning(f"Expected 2+ messages, got {len(obj['messages'])}")
        return None
    
    # Fix the messages
    messages = obj["messages"]
    for msg in messages:
        if msg.get("role") == "assistant" and "content" in msg:
            msg["content"] = fix_answer(msg["content"])
    
    return obj


def fix_jsonl_file(input_path: Path, output_path: Path) -> int:
    """
    Read malformed JSONL, fix it, write valid JSONL.
    Handles entries that are missing closing braces.
    Returns count of fixed entries.
    """
    fixed_count = 0
    
    with open(input_path, "r", encoding="utf-8") as infile:
        lines = infile.readlines()
    
    objects = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Fix missing closing brace - if line ends with ], add }
        if line.endswith("],"):
            line = line[:-1] + "}"  # Remove comma, add closing brace
        elif line.endswith("]"):
            line = line + "}"  # Add closing brace
        
        # Try to parse
        try:
            obj = json.loads(line)
            
            # Validate structure
            if "messages" not in obj or not isinstance(obj["messages"], list):
                LOGGER.warning(f"Invalid messages structure")
                continue
            
            # Fix the assistant content
            for msg in obj["messages"]:
                if msg.get("role") == "assistant" and "content" in msg:
                    msg["content"] = fix_answer(msg["content"])
            
            objects.append(obj)
            fixed_count += 1
            
        except json.JSONDecodeError as e:
            LOGGER.warning(f"Failed to parse line: {e}")
    
    # Write fixed JSONL
    with open(output_path, "w", encoding="utf-8") as outfile:
        for obj in objects:
            outfile.write(json.dumps(obj, ensure_ascii=False) + "\n")
    
    LOGGER.info(f"Fixed {fixed_count} entries from {input_path} -> {output_path}")
    return fixed_count


def main() -> None:
    """CLI entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Fix and reformat JSONL chat data.")
    parser.add_argument("--input-jsonl", type=Path, required=True, help="Input JSONL file")
    parser.add_argument("--output-jsonl", type=Path, required=True, help="Output JSONL file")
    
    args = parser.parse_args()
    
    logging.basicConfig(level=logging.INFO)
    
    count = fix_jsonl_file(args.input_jsonl, args.output_jsonl)
    print(f"Done. Fixed {count} entries.")


if __name__ == "__main__":
    main()
