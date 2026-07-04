import argparse
import json
import random
import re
from pathlib import Path
from typing import Any, Dict, List

TEMPLATES = {
    "tinyllama": {
        "system_prefix": "<|system|>\n",
        "system_suffix": "</s>\n",
        "user_prefix": "<|user|>\n",
        "user_suffix": "</s>\n",
        "assistant_prefix": "<|assistant|>\n",
        "assistant_suffix": "</s>\n",
        "response_template": "<|assistant|>\n",
    },
    "llama": {
        "system_prefix": "[INST] <<SYS>>\n",
        "system_suffix": "\n<</SYS>>\n\n",
        "user_prefix": "",
        "user_suffix": " [/INST] ",
        "assistant_prefix": "",
        "assistant_suffix": " </s><s>",
        "response_template": " [/INST] ",
    },
    "llama3": {
        "system_prefix": "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\n",
        "system_suffix": "<|eot_id|>",
        "user_prefix": "<|start_header_id|>user<|end_header_id|>\n\n",
        "user_suffix": "<|eot_id|>",
        "assistant_prefix": "<|start_header_id|>assistant<|end_header_id|>\n\n",
        "assistant_suffix": "<|eot_id|>",
        "response_template": "<|start_header_id|>assistant<|end_header_id|>\n\n",
    },
    "mistral": {
        "system_prefix": "",
        "system_suffix": "\n\n",
        "user_prefix": "[INST] ",
        "user_suffix": " [/INST]",
        "assistant_prefix": " ",
        "assistant_suffix": "</s>",
        "response_template": "[/INST]",
    },
    "gemma": {
        "system_prefix": "<bos>",
        "system_suffix": "\n",
        "user_prefix": "<start_of_turn>user\n",
        "user_suffix": "<end_of_turn>\n",
        "assistant_prefix": "<start_of_turn>model\n",
        "assistant_suffix": "<end_of_turn>\n",
        "response_template": "<start_of_turn>model\n",
    },
    "chatml": {
        "system_prefix": "<|im_start|>system\n",
        "system_suffix": "<|im_end|>\n",
        "user_prefix": "<|im_start|>user\n",
        "user_suffix": "<|im_end|>\n",
        "assistant_prefix": "<|im_start|>assistant\n",
        "assistant_suffix": "<|im_end|>\n",
        "response_template": "<|im_start|>assistant\n",
    },
}

SYSTEM_PROMPT = (
    "You are an expert HPE Aruba Networking switch support assistant. "
    "Answer questions about bugs, symptoms, and conditions accurately using "
    "the switch model, firmware version, and sub-version context provided."
)

SYMPTOM_VARIANTS = [
    "What symptom occurs in {component} Bug {bug_id}?",
    "What is the symptom of {component} bug #{bug_id}?",
    "Describe the symptom for {component} issue {bug_id}.",
    "What happens when {component} Bug {bug_id} is triggered?",
]

CONDITION_VARIANTS = [
    "Under what condition does the {component} Bug {bug_id} issue occur?",
    "When does {component} bug {bug_id} get triggered?",
    "What triggers {component} Bug {bug_id}?",
    "Describe the condition that causes {component} bug {bug_id}.",
]

MOJIBAKE_REPLACEMENTS = {
    "â€": "-",
    "â€“": "-",
    "â€”": "-",
    "â€˜": "'",
    "â€™": "'",
    "â€œ": '"',
    "â€": '"',
    "Â ": " ",
}


def normalize_text(value: Any) -> str:
    text = str(value or "")
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    try:
        repaired = text.encode("latin-1").decode("utf-8")
        if repaired.count("\ufffd") <= text.count("\ufffd"):
            text = repaired
    except (UnicodeEncodeError, UnicodeDecodeError):
        pass
    for bad, good in MOJIBAKE_REPLACEMENTS.items():
        text = text.replace(bad, good)
    return text


def build_prompt(sample: Dict[str, Any], template_name: str) -> str:
    template = TEMPLATES[template_name]
    switch = normalize_text(sample.get("switch", "unknown"))
    version = normalize_text(sample.get("version", "unknown"))
    sub_version = normalize_text(sample.get("sub_version", "unknown"))
    context = f"Switch: {switch} | Firmware: {version}.{sub_version}\n{SYSTEM_PROMPT}"

    parts = [f"{template['system_prefix']}{context}{template['system_suffix']}"]
    for message in sample.get("messages", []):
        role = str(message.get("role", "")).strip().lower()
        content = normalize_text(message.get("content", "")).strip()
        if role == "user":
            parts.append(f"{template['user_prefix']}{content}{template['user_suffix']}")
        elif role == "assistant":
            parts.append(
                f"{template['assistant_prefix']}{content}{template['assistant_suffix']}"
            )
    return "".join(parts)


def augment_sample(sample: Dict[str, Any], template_name: str) -> List[Dict[str, str]]:
    messages = sample.get("messages", [])
    user_message = ""
    assistant_message = ""
    for message in messages:
        role = str(message.get("role", "")).strip().lower()
        if role == "user" and not user_message:
            user_message = normalize_text(message.get("content", "")).strip()
        elif role == "assistant" and not assistant_message:
            assistant_message = normalize_text(message.get("content", "")).strip()

    if not user_message or not assistant_message:
        return []

    is_symptom = "symptom" in user_message.lower()
    component = assistant_message.split("(")[0].strip()
    bug_match = re.search(r"\b\d+\b", user_message)
    bug_id = bug_match.group(0) if bug_match else None

    if not component or not bug_id:
        return []

    variants = SYMPTOM_VARIANTS if is_symptom else CONDITION_VARIANTS
    selected = random.sample(variants, k=2)
    augmented_rows: List[Dict[str, str]] = []
    for variant in selected:
        paraphrased_question = variant.format(component=component, bug_id=bug_id)
        new_sample = {
            "switch": sample.get("switch", "unknown"),
            "version": sample.get("version", "unknown"),
            "sub_version": sample.get("sub_version", "unknown"),
            "messages": [
                {"role": "user", "content": paraphrased_question},
                {"role": "assistant", "content": assistant_message},
            ],
        }
        augmented_rows.append({"text": build_prompt(new_sample, template_name)})
    return augmented_rows


def convert(input_path: str, output_path: str, template_name: str, augment: bool, seed: int = 42):
    random.seed(seed)
    input_file = Path(input_path)
    output_file = Path(output_path)
    records: List[Dict[str, str]] = []

    with input_file.open("r", encoding="utf-8-sig") as infile:
        for line in infile:
            line = line.strip()
            if not line:
                continue
            sample = json.loads(line)
            records.append({"text": build_prompt(sample, template_name)})
            if augment:
                records.extend(augment_sample(sample, template_name))

    random.shuffle(records)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with output_file.open("w", encoding="utf-8") as outfile:
        for row in records:
            outfile.write(json.dumps(row, ensure_ascii=False) + "\n")

    print(f"Converted records: {len(records)}")
    print(f"Template: {template_name}")
    print(f"Augment: {augment}")
    if records:
        preview = records[0]["text"][:800]
        print("Preview:\n" + preview)


def main():
    parser = argparse.ArgumentParser(description="Convert Aruba bug JSONL to prompt-text JSONL")
    parser.add_argument("--input", type=str, required=True)
    parser.add_argument("--output", type=str, required=True)
    parser.add_argument("--template", type=str, default="llama3", choices=list(TEMPLATES.keys()))
    parser.add_argument("--augment", action="store_true")
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    convert(
        input_path=args.input,
        output_path=args.output,
        template_name=args.template,
        augment=args.augment,
        seed=args.seed,
    )


if __name__ == "__main__":
    main()
