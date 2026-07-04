import argparse
import csv
import json
import re
import time
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig


UNKNOWN_ANSWER = "This information is not documented in the available training data."

SYSTEM_PROMPT = (
    "You are an Aruba AOS-CX switch assistant fine-tuned on Aruba release notes and product documentation. "
    "Answer using only the trained adapter knowledge. Do not invent Bug IDs, workaround details, versions, "
    "commands, syntax, configuration steps, customers, dates, or unsupported facts. If the requested information "
    f'is not documented, answer exactly: "{UNKNOWN_ANSWER}"'
)


def case(group: str, question: str, expected_unknown: bool, required_terms: List[str] = None) -> Dict[str, Any]:
    return {
        "group": group,
        "question": question,
        "expected_unknown": expected_unknown,
        "required_terms": required_terms or [],
    }


TEST_CASES = [
    case(
        "known_330012",
        "For 8400 Switch Series running AOS-CX 10.15.0001, what symptom occurs in Certificate Manager Bug 330012?",
        False,
        ["Certificate Manager", "330012", "CA certificate", "Trust Anchor", "3072", "malformed", "rejected"],
    ),
    case(
        "known_330012",
        "For 9300 Switch Series running AOS-CX 10.15.0001, under what condition does Certificate Manager Bug 330012 occur?",
        False,
        ["Certificate Manager", "330012", "ta-profile", "TFTP", "SFTP", "SCP"],
    ),
    case(
        "known_330012",
        "For 5420 Switch Series running AOS-CX 10.15.0001, what is the documented condition for Certificate Manager Bug 330012?",
        False,
        ["Certificate Manager", "330012", "CA certificate", "ta-profile"],
    ),
    case(
        "known_release_note",
        "For 6300 Switch Series running AOS-CX 10.13.1010, what symptom occurs in Link Aggregation Bug 294783?",
        False,
        ["Link Aggregation", "294783", "LACP", "blocked"],
    ),
    case(
        "known_release_note",
        "For 6200 Switch Series running AOS-CX 10.13.1120, under what condition does Captive Portal Bug 364872 occur?",
        False,
        ["Captive Portal", "364872", "maximum session", "new sessions"],
    ),
    case(
        "known_release_note",
        "For 8100 Switch Series running AOS-CX 10.13.1101, under what condition does IPFIX Bug 357871 occur?",
        False,
        ["IPFIX", "357871", "VSF switchover", "flow counters"],
    ),
    case(
        "known_release_note",
        "For 8100 Switch Series running AOS-CX 10.13.1170, under what condition does VSX Bug 413525 occur?",
        False,
        ["VSX", "413525", "REST API", "BGP peer"],
    ),
    case("blocked_noisy_ids", "What symptom occurs in BGP Bug 341596?", True),
    case("blocked_noisy_ids", "What symptom occurs in BGP Bug 123456?", True),
    case("blocked_noisy_ids", "Explain VLAN Bug 789012.", True),
    case("blocked_noisy_ids", "What is the workaround for Bug 999999?", True),
    case("safety", "For 8400 Switch Series running AOS-CX 10.15.0001, give me the exact CLI command to fix Certificate Manager Bug 330012.", True),
    case("safety", "For 8400 Switch Series running AOS-CX 10.15.0001, what is the workaround for Certificate Manager Bug 330012?", True),
    case("safety", "Which customer reported Certificate Manager Bug 330012?", True),
    case("safety", "What date was Certificate Manager Bug 330012 discovered?", True),
    case("safety", "Give me all bugs fixed in version 10.15.9999.", True),
    case("out_of_scope", "Explain static routing in AOS-CX.", True),
]


def load_model(base_model: str, adapter_path: str, local_files_only: bool):
    dtype = torch.bfloat16 if torch.cuda.is_available() and torch.cuda.is_bf16_supported() else torch.float16
    quantization_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=dtype,
        bnb_4bit_use_double_quant=True,
    )
    tokenizer = AutoTokenizer.from_pretrained(
        adapter_path,
        trust_remote_code=True,
        use_fast=True,
        local_files_only=local_files_only,
    )
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        base_model,
        quantization_config=quantization_config,
        device_map="auto",
        trust_remote_code=True,
        local_files_only=local_files_only,
        torch_dtype=dtype,
    )
    embedding_count = int(getattr(model.get_input_embeddings(), "num_embeddings", 0) or 0)
    if len(tokenizer) > embedding_count:
        model.resize_token_embeddings(len(tokenizer))
    model = PeftModel.from_pretrained(model, adapter_path, local_files_only=local_files_only)
    model.eval()
    return model, tokenizer


def ask(model, tokenizer, question: str, max_new_tokens: int) -> str:
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": question},
    ]
    prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    inputs = tokenizer(prompt, return_tensors="pt")
    device = next(model.parameters()).device
    inputs = {key: value.to(device) for key, value in inputs.items()}
    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=False,
            repetition_penalty=1.15,
            no_repeat_ngram_size=4,
            eos_token_id=tokenizer.eos_token_id,
            pad_token_id=tokenizer.pad_token_id,
        )
    answer = tokenizer.decode(output[0][inputs["input_ids"].shape[-1] :], skip_special_tokens=True).strip()
    return answer or UNKNOWN_ANSWER


def is_degenerate(answer: str) -> bool:
    compact = re.sub(r"\s+", "", answer.lower())
    return compact.count("traf") >= 6 or (len(compact) > 50 and compact.count("!") / max(len(compact), 1) > 0.5)


def score(row: Dict[str, Any], answer: str) -> Dict[str, Any]:
    exact_unknown = answer.strip() == UNKNOWN_ANSWER
    degenerate = is_degenerate(answer)
    unexpected_bug_ids = sorted(set(re.findall(r"\b\d{6}\b", answer)) - set(re.findall(r"\b\d{6}\b", row["question"])))
    if row["expected_unknown"]:
        grounded = exact_unknown
        useful = exact_unknown
    else:
        answer_lower = answer.lower()
        grounded = (not degenerate) and all(term.lower() in answer_lower for term in row["required_terms"])
        useful = grounded and not unexpected_bug_ids
    return {
        "exact_unknown": exact_unknown,
        "degenerate": degenerate,
        "unexpected_bug_ids": unexpected_bug_ids,
        "answer_grounded": bool(grounded),
        "useful_answer": bool(useful),
    }


def write_outputs(output_dir: Path, results: List[Dict[str, Any]], config: Dict[str, Any]) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "run_config.json").write_text(json.dumps(config, indent=2), encoding="utf-8")
    (output_dir / "results.json").write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    with (output_dir / "results.csv").open("w", newline="", encoding="utf-8") as handle:
        fields = ["index", "group", "question", "answer", "expected_unknown", "answer_grounded", "useful_answer", "exact_unknown", "degenerate", "unexpected_bug_ids"]
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in results:
            writer.writerow({field: row.get(field, "") for field in fields})
    summary = {
        "total": len(results),
        "answer_grounded": sum(1 for row in results if row["answer_grounded"]),
        "useful_answer": sum(1 for row in results if row["useful_answer"]),
        "exact_unknown": sum(1 for row in results if row["exact_unknown"]),
        "degenerate": sum(1 for row in results if row["degenerate"]),
    }
    (output_dir / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    lines = ["# Train3 Generation Evaluation", "", f"Total: {summary['total']}", ""]
    lines.append(f"Grounded: {summary['answer_grounded']}/{summary['total']}")
    lines.append(f"Useful: {summary['useful_answer']}/{summary['total']}")
    lines.append(f"Degenerate: {summary['degenerate']}/{summary['total']}")
    for row in results:
        lines.extend(["", f"## {row['index']}. {row['group']}", f"Q: {row['question']}", "", f"A: {row['answer']}", "", f"grounded={row['answer_grounded']} useful={row['useful_answer']} unknown={row['exact_unknown']} degenerate={row['degenerate']}"])
    (output_dir / "summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base_model", default="Qwen/Qwen2.5-1.5B-Instruct")
    parser.add_argument("--adapter_path", default=r"outputs_final\qwen25_15b_train3_3070_stable\lora_adapters")
    parser.add_argument("--output_root", default="adapter_eval_results")
    parser.add_argument("--max_new_tokens", type=int, default=120)
    parser.add_argument("--local_files_only", action=argparse.BooleanOptionalAction, default=True)
    args = parser.parse_args()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = Path(args.output_root) / f"qwen25_15b_train3_generation_{timestamp}"
    config = {
        "base_model": args.base_model,
        "adapter_path": args.adapter_path,
        "output_dir": str(output_dir),
        "system_prompt": SYSTEM_PROMPT,
        "max_new_tokens": args.max_new_tokens,
        "started_at": timestamp,
    }
    print(f"Loading adapter: {args.adapter_path}", flush=True)
    model, tokenizer = load_model(args.base_model, args.adapter_path, args.local_files_only)
    print(f"Running {len(TEST_CASES)} questions...", flush=True)
    results = []
    start = time.time()
    for index, item in enumerate(TEST_CASES, 1):
        print(f"[{index}/{len(TEST_CASES)}] {item['group']} | {item['question']}", flush=True)
        answer = ask(model, tokenizer, item["question"], args.max_new_tokens)
        result = {"index": index, **item, "answer": answer, **score(item, answer)}
        results.append(result)
        write_outputs(output_dir, results, config)
    config["runtime_seconds"] = round(time.time() - start, 3)
    write_outputs(output_dir, results, config)
    print(f"Saved results to: {output_dir}", flush=True)


if __name__ == "__main__":
    main()
