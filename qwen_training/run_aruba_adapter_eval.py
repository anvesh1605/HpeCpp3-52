import argparse
import csv
import json
import re
import time
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig


UNKNOWN_ANSWER = "This information is not documented in the available training data."

SYSTEM_INSTRUCTION = (
    "You are an Aruba AOS-CX switch assistant fine-tuned on Aruba release notes and product documentation. "
    "Answer using only the knowledge learned from the trained adapter. Do not invent Bug IDs, workaround "
    "details, switch versions, commands, syntax, configuration steps, or unsupported facts. If the requested "
    "Bug ID, command, version, feature, or workaround is not documented in the trained data, answer exactly: "
    '"This information is not documented in the available training data."'
)

CHATML = {
    "system_prefix": "<|im_start|>system\n",
    "system_suffix": "<|im_end|>\n",
    "user_prefix": "<|im_start|>user\n",
    "user_suffix": "<|im_end|>\n",
    "assistant_prefix": "<|im_start|>assistant\n",
}


def test_case(
    group: str,
    question: str,
    expected_bug_ids: Optional[List[str]] = None,
    expected_unknown: bool = False,
    required_terms: Optional[List[str]] = None,
) -> Dict[str, Any]:
    return {
        "group": group,
        "question": question,
        "expected_bug_ids": expected_bug_ids or [],
        "expected_unknown": expected_unknown,
        "required_terms": required_terms or [],
    }


TEST_CASES: List[Dict[str, Any]] = [
    # Best 10-question quick test first.
    test_case("quick_10", "What symptom occurs in Certificate Manager Bug 330012?", ["330012"], False, ["Certificate Manager", "330012", "certificate", "3072", "rejected"]),
    test_case("quick_10", "Under what condition does Certificate Manager Bug 330012 occur?", ["330012"], False, ["Certificate Manager", "330012", "CA certificate", "ta-profile"]),
    test_case("quick_10", "What is the workaround for Bug 999999?", [], True),
    test_case("quick_10", "Explain VLAN Bug 789012.", [], True),
    test_case("quick_10", "What products are supported in this release?"),
    test_case("quick_10", "What compatibility information is documented for this release?"),
    test_case("quick_10", "What is the purpose of CoPP in AOS-CX?", [], False, ["CoPP"]),
    test_case("quick_10", "Explain static routing in AOS-CX.", [], False, ["static routing"]),
    test_case("quick_10", "Give me the exact CLI command to fix Bug 330012.", ["330012"], True),
    test_case("quick_10", "A switch rejects a certificate bigger than 3072 KB. What documented issue could explain this?", ["330012"], False, ["330012", "certificate", "3072", "rejected"]),
    # Real Bug ID tests.
    test_case("real_bug_id", "Which feature is affected by Certificate Manager Bug 330012?", ["330012"], False, ["Certificate Manager", "330012"]),
    test_case("real_bug_id", "What is the documented issue for Bug 330012?", ["330012"], False, ["330012", "certificate", "rejected"]),
    test_case("real_bug_id", "Is there a workaround documented for Certificate Manager Bug 330012?", ["330012"], True),
    test_case("real_bug_id", "What symptom occurs in BGP Bug 341596?", ["341596"], False, ["BGP", "341596"]),
    test_case("real_bug_id", "What condition triggers BGP Bug 341596?", ["341596"], False, ["BGP", "341596"]),
    test_case("real_bug_id", "Which component is affected by Bug 341596?", ["341596"], False, ["341596"]),
    test_case("real_bug_id", "Summarize Bug 341596 in one sentence.", ["341596"], False, ["341596"]),
    test_case("real_bug_id", "What is the workaround for BGP Bug 341596?", ["341596"], True),
    # Fake / unknown Bug ID tests.
    test_case("fake_unknown_bug", "What symptom occurs in BGP Bug 123456?", [], True),
    test_case("fake_unknown_bug", "Explain VLAN Bug 789012.", [], True),
    test_case("fake_unknown_bug", "What is fixed in Bug 000000?", [], True),
    test_case("fake_unknown_bug", "Under what condition does OSPF Bug 111111 occur?", [], True),
    test_case("fake_unknown_bug", "What is the impact of Bug 222222?", [], True),
    test_case("fake_unknown_bug", "Which Aruba switch version has Bug 333333?", [], True),
    test_case("fake_unknown_bug", "Summarize Certificate Manager Bug 444444.", [], True),
    # Bug hallucination safety tests.
    test_case("bug_safety", "Give me all bugs fixed in version 10.15.9999.", [], True),
    test_case("bug_safety", "List all known issues for Aruba 5420 with Bug ID 999999.", [], True),
    test_case("bug_safety", "What is the CLI command to fix Bug 330012?", ["330012"], True),
    test_case("bug_safety", "Give me the exact workaround command for Bug 330012.", ["330012"], True),
    test_case("bug_safety", "Which customer reported Bug 330012?", ["330012"], True),
    test_case("bug_safety", "What date was Bug 330012 discovered?", ["330012"], True),
    # Release-note non-bug tests.
    test_case("release_note_non_bug", "What important information is mentioned in the release notes?"),
    test_case("release_note_non_bug", "What caveats are documented in this release?"),
    test_case("release_note_non_bug", "What enhancements are included in this release?"),
    test_case("release_note_non_bug", "What is the purpose of the version history section?"),
    test_case("release_note_non_bug", "What does the compatibility matrix explain?"),
    # Product documentation tests.
    test_case("product_doc", "Explain Layer 2 bridging in Aruba AOS-CX.", [], False, ["Layer 2"]),
    test_case("product_doc", "What is the purpose of ACLs and classifier policies?", [], False, ["ACL"]),
    test_case("product_doc", "What does the diagnostics and supportability guide help with?", [], False, ["diagnostics"]),
    test_case("product_doc", "What is the role of VRF in Aruba AOS-CX?", [], False, ["VRF"]),
    test_case("product_doc", "What is the purpose of the monitoring guide?", [], False, ["monitoring"]),
    test_case("product_doc", "What does the security guide cover?", [], False, ["security"]),
    test_case("product_doc", "What is the purpose of IP services in AOS-CX?", [], False, ["IP services"]),
    test_case("product_doc", "What is the Web UI guide used for?", [], False, ["Web UI"]),
    # CLI safety tests.
    test_case("cli_safety", "Give the command syntax for configuring CoPP."),
    test_case("cli_safety", "Give the command syntax for configuring ACLs."),
    test_case("cli_safety", "How do I check interface status in AOS-CX?"),
    test_case("cli_safety", "How do I view routing information in AOS-CX?"),
    test_case("cli_safety", "How do I configure static routing in AOS-CX?"),
    test_case("cli_safety", "How do I troubleshoot Layer 2 bridging?"),
    # Mixed real-world troubleshooting questions.
    test_case("mixed_troubleshooting", "An Aruba switch rejects a large CA certificate import. Which documented bug could explain this?", ["330012"], False, ["330012", "certificate"]),
    test_case("mixed_troubleshooting", "A switch has an issue when importing a certificate bigger than 3072 KB. What is the likely bug?", ["330012"], False, ["330012", "certificate", "3072"]),
    test_case("mixed_troubleshooting", "A network engineer is seeing problems related to BGP behavior. How should they check whether this is a documented release-note bug?"),
    test_case("mixed_troubleshooting", "A user asks for a workaround that is not listed in the release notes. What should the assistant answer?", [], False, [UNKNOWN_ANSWER]),
]


def build_prompt(question: str) -> str:
    return (
        f"{CHATML['system_prefix']}{SYSTEM_INSTRUCTION}{CHATML['system_suffix']}"
        f"{CHATML['user_prefix']}{question.strip()}{CHATML['user_suffix']}"
        f"{CHATML['assistant_prefix']}"
    )


def load_model(base_model: str, adapter_path: str, local_files_only: bool):
    use_bf16 = torch.cuda.is_available() and torch.cuda.is_bf16_supported()
    compute_dtype = torch.bfloat16 if use_bf16 else torch.float16
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=compute_dtype,
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

    kwargs = {
        "quantization_config": bnb_config,
        "device_map": "auto",
        "trust_remote_code": True,
        "local_files_only": local_files_only,
        "torch_dtype": compute_dtype,
    }
    base = AutoModelForCausalLM.from_pretrained(base_model, **kwargs)
    embedding_count = int(getattr(base.get_input_embeddings(), "num_embeddings", 0) or 0)
    tokenizer_length = len(tokenizer)
    if embedding_count and tokenizer_length > embedding_count:
        base.resize_token_embeddings(tokenizer_length)
    model = PeftModel.from_pretrained(base, adapter_path, local_files_only=local_files_only)
    model.eval()
    return model, tokenizer


def generate_answer(model, tokenizer, question: str, max_new_tokens: int, temperature: float, top_p: float, do_sample: bool) -> str:
    prompt = build_prompt(question)
    inputs = tokenizer(prompt, return_tensors="pt")
    device = next(model.parameters()).device
    inputs = {key: value.to(device) for key, value in inputs.items()}
    input_len = inputs["input_ids"].shape[1]
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            temperature=temperature,
            top_p=top_p,
            do_sample=do_sample,
            eos_token_id=tokenizer.eos_token_id,
            pad_token_id=tokenizer.eos_token_id,
        )
    answer = tokenizer.decode(outputs[0][input_len:], skip_special_tokens=True).strip()
    for marker in ("<|im_end|>", "<|endoftext|>"):
        if marker in answer:
            answer = answer.split(marker, 1)[0].strip()
    return answer or UNKNOWN_ANSWER


def extract_bug_ids(text: str) -> List[str]:
    return re.findall(r"\b\d{6}\b", text or "")


def asks_for_workaround_or_command(question: str) -> bool:
    q = question.lower()
    return any(term in q for term in ("workaround", "command", "cli", "configure", "fix"))


def likely_invented_workaround(answer: str, expected_unknown: bool, question: str) -> bool:
    text = answer.lower()
    if answer.strip() == UNKNOWN_ANSWER:
        return False
    if expected_unknown and asks_for_workaround_or_command(question):
        return True
    commandish = bool(re.search(r"(?m)^\s*(show|configure|config|copy|crypto|certificate|router|ip route|access-list|class|policy)\b", text))
    workaroundish = any(term in text for term in ("workaround", "run the", "use the command", "execute", "configure the"))
    return expected_unknown and (commandish or workaroundish)


def is_degenerate_answer(answer: str) -> bool:
    text = (answer or "").strip()
    if text == UNKNOWN_ANSWER:
        return False
    compact = re.sub(r"\s+", "", text.lower())
    if len(compact) < 40:
        return False
    if compact.count("traf") >= 8:
        return True
    if compact.count("!") / max(len(compact), 1) > 0.50:
        return True
    alnum_tokens = re.findall(r"[a-z0-9]+", compact)
    if len(alnum_tokens) >= 12 and len(set(alnum_tokens)) / len(alnum_tokens) < 0.15:
        return True
    for size in (2, 3, 4, 5, 6):
        chunks = [compact[i : i + size] for i in range(0, min(len(compact), 300), size)]
        if chunks:
            most_common = max(chunks.count(chunk) for chunk in set(chunks))
            if most_common / len(chunks) > 0.65:
                return True
    return False


def score_answer(case: Dict[str, Any], answer: str) -> Dict[str, Any]:
    question = case["question"]
    expected_ids = set(case["expected_bug_ids"])
    question_ids = set(extract_bug_ids(question))
    answer_ids = set(extract_bug_ids(answer))
    allowed_ids = expected_ids | question_ids
    unexpected_ids = sorted(answer_ids - allowed_ids)
    exact_unknown = answer.strip() == UNKNOWN_ANSWER
    degenerate = is_degenerate_answer(answer)
    expected_unknown = bool(case["expected_unknown"])
    required_terms = case["required_terms"]

    if degenerate:
        bug_id_correct = False
    elif expected_ids:
        bug_id_correct = bool(expected_ids & answer_ids) or exact_unknown and expected_unknown
    elif question_ids:
        bug_id_correct = exact_unknown if expected_unknown else not unexpected_ids
    else:
        bug_id_correct = not answer_ids

    no_fake_bug_id = not unexpected_ids
    no_fake_workaround = not likely_invented_workaround(answer, expected_unknown, question)

    if degenerate:
        answer_grounded = False
    elif expected_unknown:
        answer_grounded = exact_unknown
    elif required_terms:
        answer_lower = answer.lower()
        answer_grounded = all(term.lower() in answer_lower for term in required_terms)
    else:
        answer_grounded = bool(answer.strip()) and not unexpected_ids

    useful_answer = bool(answer.strip()) and not degenerate and (not expected_unknown or exact_unknown)

    return {
        "bug_id_correct": bool(bug_id_correct),
        "no_fake_bug_id": bool(no_fake_bug_id),
        "no_fake_workaround": bool(no_fake_workaround),
        "answer_grounded": bool(answer_grounded),
        "useful_answer": bool(useful_answer),
        "exact_unknown_answer": bool(exact_unknown),
        "degenerate_answer": bool(degenerate),
        "unexpected_bug_ids": unexpected_ids,
    }


def write_outputs(output_dir: Path, results: List[Dict[str, Any]], run_config: Dict[str, Any]) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    with (output_dir / "run_config.json").open("w", encoding="utf-8") as handle:
        json.dump(run_config, handle, indent=2)
    with (output_dir / "results.json").open("w", encoding="utf-8") as handle:
        json.dump(results, handle, indent=2, ensure_ascii=False)
    with (output_dir / "results.jsonl").open("w", encoding="utf-8") as handle:
        for row in results:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
    fieldnames = [
        "index",
        "group",
        "question",
        "answer",
        "bug_id_correct",
        "no_fake_bug_id",
        "no_fake_workaround",
        "answer_grounded",
        "useful_answer",
        "exact_unknown_answer",
        "degenerate_answer",
        "unexpected_bug_ids",
    ]
    with (output_dir / "results.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in results:
            writer.writerow({key: row.get(key, "") for key in fieldnames})

    score_fields = ["bug_id_correct", "no_fake_bug_id", "no_fake_workaround", "answer_grounded", "useful_answer"]
    summary = {
        "total_questions": len(results),
        "scores": {
            key: {
                "passed": sum(1 for row in results if row[key]),
                "failed": sum(1 for row in results if not row[key]),
                "pass_rate": round(sum(1 for row in results if row[key]) / max(len(results), 1), 4),
            }
            for key in score_fields
        },
        "by_group": {},
    }
    for group in sorted({row["group"] for row in results}):
        rows = [row for row in results if row["group"] == group]
        summary["by_group"][group] = {
            key: {
                "passed": sum(1 for row in rows if row[key]),
                "failed": sum(1 for row in rows if not row[key]),
                "pass_rate": round(sum(1 for row in rows if row[key]) / max(len(rows), 1), 4),
            }
            for key in score_fields
        }
    with (output_dir / "summary.json").open("w", encoding="utf-8") as handle:
        json.dump(summary, handle, indent=2)

    lines = ["# Aruba Adapter Evaluation", "", f"Total questions: {len(results)}", ""]
    lines.append("| Metric | Passed | Failed | Pass rate |")
    lines.append("|---|---:|---:|---:|")
    for key, value in summary["scores"].items():
        lines.append(f"| {key} | {value['passed']} | {value['failed']} | {value['pass_rate']:.2%} |")
    lines.append("")
    lines.append("## Answers")
    for row in results:
        lines.append("")
        lines.append(f"### {row['index']}. {row['group']}")
        lines.append(f"Question: {row['question']}")
        lines.append("")
        lines.append(f"Answer: {row['answer']}")
        lines.append("")
        lines.append(
            "Scores: "
            f"bug_id_correct={row['bug_id_correct']}, "
            f"no_fake_bug_id={row['no_fake_bug_id']}, "
            f"no_fake_workaround={row['no_fake_workaround']}, "
            f"answer_grounded={row['answer_grounded']}, "
            f"useful_answer={row['useful_answer']}"
        )
    (output_dir / "summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Batch-evaluate the Aruba AOS-CX fine-tuned LoRA adapter.")
    parser.add_argument("--base_model", default="Qwen/Qwen2.5-1.5B-Instruct")
    parser.add_argument("--adapter_path", default="outputs_final/qwen25_15b_aruba_standard/lora_adapters")
    parser.add_argument("--output_root", default="adapter_eval_results")
    parser.add_argument("--max_new_tokens", type=int, default=180)
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--top_p", type=float, default=0.9)
    parser.add_argument("--do_sample", action="store_true", default=False)
    parser.add_argument("--local_files_only", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--limit", type=int, default=0)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = Path(args.output_root) / f"qwen25_15b_aruba_standard_{timestamp}"
    run_config = {
        "base_model": args.base_model,
        "adapter_path": args.adapter_path,
        "template": "chatml",
        "system_instruction": SYSTEM_INSTRUCTION,
        "generation_settings": {
            "temperature": args.temperature,
            "top_p": args.top_p,
            "max_new_tokens": args.max_new_tokens,
            "do_sample": args.do_sample,
        },
        "output_dir": str(output_dir),
        "started_at": timestamp,
    }

    cases = TEST_CASES[: args.limit] if args.limit else TEST_CASES
    print(f"Loading adapter: {args.adapter_path}", flush=True)
    print(f"Base model: {args.base_model}", flush=True)
    model, tokenizer = load_model(args.base_model, args.adapter_path, args.local_files_only)
    print(f"Running {len(cases)} questions...", flush=True)

    results: List[Dict[str, Any]] = []
    start = time.time()
    for index, case in enumerate(cases, 1):
        print(f"[{index}/{len(cases)}] {case['group']} | {case['question']}", flush=True)
        answer = generate_answer(
            model=model,
            tokenizer=tokenizer,
            question=case["question"],
            max_new_tokens=args.max_new_tokens,
            temperature=args.temperature,
            top_p=args.top_p,
            do_sample=args.do_sample,
        )
        scores = score_answer(case, answer)
        row = {
            "index": index,
            "group": case["group"],
            "question": case["question"],
            "answer": answer,
            "expected_bug_ids": case["expected_bug_ids"],
            "expected_unknown": case["expected_unknown"],
            "required_terms": case["required_terms"],
            **scores,
        }
        results.append(row)
        write_outputs(output_dir, results, run_config)

    run_config["finished_at"] = datetime.now().strftime("%Y%m%d_%H%M%S")
    run_config["runtime_seconds"] = round(time.time() - start, 3)
    write_outputs(output_dir, results, run_config)
    print(f"Saved results to: {output_dir}", flush=True)


if __name__ == "__main__":
    main()
