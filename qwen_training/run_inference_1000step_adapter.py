import argparse
import json
import logging
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

os.environ.setdefault("CUDA_DEVICE_ORDER", "PCI_BUS_ID")

import torch
from peft import PeftModel
from strict_rescore_inference_outputs import partition_summaries, strict_review, summarize_rows
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig


MODEL_NAME = "Qwen/Qwen2.5-3B-Instruct"
REPO_ROOT = Path(__file__).resolve().parents[1]
ADAPTER_PATH = REPO_ROOT / "models" / "qwen"
OUTPUT_DIR = Path("outputs_inference/qwen25_3b_release_notes_only_fullfacts_1epoch_stratified")
TEST_DATA_PATH = Path("Data/all_switches/release_notes_only_structured_full/release_notes_only_structured_full_holdout.jsonl")
UNKNOWN = "This information is not documented in the available training data."

SYSTEM_PROMPT = (
    "You are an Aruba AOS-CX release-notes assistant. "
    "Answer using only the trained Aruba release-note knowledge. "
    "Preserve switch, version, sub_version, bug IDs when present, feature names, symptoms, causes, workarounds, "
    "release dates, version history, supported products, compatibility, certifications, and procedure details exactly. "
    "Do not invent unsupported bug IDs, workarounds, affected versions, release dates, product mappings, compatibility claims, or configuration steps. "
    f"If the information is unavailable, say: {UNKNOWN}"
)

RELEASE_NOTES_CONTEXT_INSTRUCTION = (
    "You are answering from HPE Aruba AOS-CX release notes only. "
    "Focus on the documented release-note facts: resolved issues, caveats, known issues, "
    "supported products, version history, workarounds, release dates, and procedures when present. "
    "Do not invent unsupported details. If the answer is not documented in the provided training data, "
    "say that it is not documented."
)

SAFE_METADATA_FIELDS = [
    ("vendor", "HPE Aruba"),
    ("product_family", "AOS-CX"),
    ("switch", None),
    ("version", None),
    ("sub_version", None),
    ("source_type", None),
    ("data_family", None),
    ("document_title", None),
    ("section", None),
    ("topic", None),
    ("command", None),
]

ANSWER_LEAKING_CONTEXT_FIELDS = {
    "syntax",
    "release_date",
    "workaround",
    "symptom",
    "scenario",
    "category",
    "description",
    "answer",
    "remarks",
    "reference",
    "bug_details",
    "event_description",
}

CORRUPTED_GENERATION_MARKERS = (
    "ly i are given as theef prouba",
    "q:the: hpe uba product",
    "theef prouba",
    "<|im_start|>user",
)

CHATML = {
    "system_prefix": "<|im_start|>system\n",
    "system_suffix": "<|im_end|>\n",
    "user_prefix": "<|im_start|>user\n",
    "user_suffix": "<|im_end|>\n",
    "assistant_prefix": "<|im_start|>assistant\n",
}


MANUAL_CASE_SPECS = [
    ("release_notes_known_issues", lambda row: normalize_text(row.get("source_type")) == "release_notes_known_issues"),
    ("release_notes_resolved_issues", lambda row: normalize_text(row.get("source_type")) == "release_notes_resolved_issues"),
    ("release_notes_caveats", lambda row: normalize_text(row.get("source_type")) == "release_notes_caveats"),
    ("release_notes_version_history", lambda row: normalize_text(row.get("source_type")) == "release_notes_version_history"),
    ("release_notes_supported_products", lambda row: normalize_text(row.get("source_type")) == "release_notes_supported_products"),
    ("release_notes_upgrade_procedure", lambda row: normalize_text(row.get("source_type")) == "release_notes_upgrade_procedure"),
    ("release_notes_downgrade_restore", lambda row: normalize_text(row.get("source_type")) == "release_notes_downgrade_restore"),
    ("release_notes_compatibility", lambda row: normalize_text(row.get("source_type")) == "release_notes_compatibility"),
    ("release_notes_certifications", lambda row: normalize_text(row.get("source_type")) == "release_notes_certifications"),
    (
        "release_notes_generic_release_date",
        lambda row: normalize_text(row.get("source_type")) == "release_notes_generic" and bool(normalize_text(row.get("release_date"))),
    ),
    (
        "release_notes_generic_supported_product",
        lambda row: normalize_text(row.get("source_type")) == "release_notes_generic"
        and bool(normalize_text(row.get("product_number") or row.get("product_name"))),
    ),
    (
        "release_notes_generic_version_history",
        lambda row: normalize_text(row.get("source_type")) == "release_notes_generic"
        and bool(normalize_text(row.get("version_number") or row.get("minimum_software_version") or row.get("minimum_supported_version"))),
    ),
    (
        "release_notes_generic_procedure",
        lambda row: normalize_text(row.get("source_type")) == "release_notes_generic" and bool(normalize_text(row.get("procedure"))),
    ),
    (
        "release_notes_generic_remarks",
        lambda row: normalize_text(row.get("source_type")) == "release_notes_generic" and bool(normalize_text(row.get("remarks"))),
    ),
    (
        "release_notes_generic_symptom_workaround",
        lambda row: normalize_text(row.get("source_type")) == "release_notes_generic"
        and (
            bool(normalize_text(row.get("symptom")))
            or bool(normalize_text(row.get("workaround")))
            or bool(normalize_text(row.get("scenario")))
        ),
    ),
]


def build_manual_cases(test_data_path: Path, limit: Optional[int] = None) -> List[Dict[str, Any]]:
    if limit is not None and limit <= 0:
        return []
    rows = list(read_jsonl(test_data_path))
    selected: List[Dict[str, Any]] = []
    used_questions: set[str] = set()
    for label, predicate in MANUAL_CASE_SPECS:
        for row in rows:
            if not predicate(row):
                continue
            question, reference = extract_qa(row)
            if not question or not reference or question in used_questions:
                continue
            case = {
                "switch": normalize_text(row.get("switch")),
                "version": normalize_text(row.get("version")).replace("_", "."),
                "sub_version": normalize_text(row.get("sub_version")),
                "source_type": normalize_text(row.get("source_type")),
                "data_family": normalize_text(row.get("data_family")),
                "document_title": normalize_text(row.get("document_title")),
                "section": normalize_text(row.get("section")),
                "topic": normalize_text(row.get("topic")),
                "command": normalize_text(row.get("command") or row.get("command_name")),
                "question": question,
                "reference": reference,
                "manual_label": label,
            }
            selected.append(case)
            used_questions.add(question)
            break
    if limit is not None:
        return selected[:limit]
    return selected


def normalize_text(value: Any) -> str:
    return str(value or "").replace("\r\n", "\n").replace("\r", "\n").strip()


def compact_text(text: str, limit: int = 240) -> str:
    compact = re.sub(r"\s+", " ", normalize_text(text))
    return compact[: limit - 3] + "..." if len(compact) > limit else compact


def setup_logging(output_dir: Path) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    log_path = output_dir / "inference.log"
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[logging.FileHandler(log_path, encoding="utf-8"), logging.StreamHandler(sys.stdout)],
    )
    return log_path


def verify_adapter(adapter_path: Path) -> None:
    required = ["adapter_config.json", "adapter_model.safetensors"]
    missing = [name for name in required if not (adapter_path / name).exists()]
    if missing:
        raise FileNotFoundError(f"Missing adapter files in {adapter_path}: {', '.join(missing)}")


def gpu0_compute_processes() -> List[str]:
    try:
        gpu_query = subprocess.run(
            [
                "nvidia-smi",
                "--query-gpu=index,pci.bus_id",
                "--format=csv,noheader,nounits",
            ],
            check=True,
            text=True,
            capture_output=True,
        )
        bus_by_index: Dict[str, str] = {}
        for line in gpu_query.stdout.splitlines():
            parts = [part.strip() for part in line.split(",")]
            if len(parts) >= 2:
                bus_by_index[parts[0]] = parts[1]
        gpu0_bus = bus_by_index.get("0")
        if not gpu0_bus:
            return []

        proc_query = subprocess.run(
            [
                "nvidia-smi",
                "--query-compute-apps=pid,gpu_bus_id,process_name,used_memory",
                "--format=csv,noheader,nounits",
            ],
            check=True,
            text=True,
            capture_output=True,
        )
        busy: List[str] = []
        current_pid = str(os.getpid())
        for line in proc_query.stdout.splitlines():
            parts = [part.strip() for part in line.split(",")]
            if len(parts) >= 4 and parts[1] == gpu0_bus and parts[0] != current_pid:
                busy.append(line.strip())
        return busy
    except (FileNotFoundError, subprocess.CalledProcessError):
        return []


def release_notes_context(case: Dict[str, Any]) -> str:
    lines = ["Release notes context:"]
    for label, default_value in SAFE_METADATA_FIELDS:
        if label in ANSWER_LEAKING_CONTEXT_FIELDS:
            continue
        value = default_value if default_value is not None else case.get(label, "")
        if label == "command":
            value = case.get("command") or case.get("command_name", "")
        text = normalize_text(value)
        if text:
            lines.append(f"{label}: {text}")
    return "\n".join(lines)


def formatted_user_prompt(case: Dict[str, Any], question: str) -> str:
    return "\n\n".join(
        [
            RELEASE_NOTES_CONTEXT_INSTRUCTION,
            release_notes_context(case),
            f"Question:\n{normalize_text(question)}",
        ]
    ).strip()


def build_prompt(case: Dict[str, Any], question: str, tokenizer=None) -> str:
    user = formatted_user_prompt(case, question)
    if tokenizer is not None and hasattr(tokenizer, "apply_chat_template"):
        return tokenizer.apply_chat_template(
            [{"role": "user", "content": user}],
            tokenize=False,
            add_generation_prompt=True,
        )
    return f"{CHATML['user_prefix']}{user}{CHATML['user_suffix']}{CHATML['assistant_prefix']}"


def adapter_declared_base(adapter_path: Path) -> str:
    config_path = adapter_path / "adapter_config.json"
    if not config_path.is_file():
        raise FileNotFoundError(f"Adapter config is missing: {config_path}")
    payload = json.loads(config_path.read_text(encoding="utf-8"))
    declared = str(payload.get("base_model_name_or_path") or "").strip()
    if not declared:
        raise ValueError(f"Adapter does not declare base_model_name_or_path: {config_path}")
    return declared


def resolve_model_name(requested: Optional[str], adapter_path: Optional[Path], no_adapter: bool) -> str:
    if no_adapter:
        return str(requested or MODEL_NAME)
    if adapter_path is None:
        raise ValueError("adapter_path is required unless --no_adapter is used")
    declared = adapter_declared_base(adapter_path)
    if requested and requested != declared:
        raise ValueError(
            f"Requested base model {requested!r} does not match adapter-declared base {declared!r}"
        )
    return declared


def load_model(model_name: str, adapter_path: Optional[Path], local_files_only: bool, no_adapter: bool = False):
    use_bf16 = torch.cuda.is_available() and torch.cuda.is_bf16_supported()
    compute_dtype = torch.bfloat16 if use_bf16 else torch.float16
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=compute_dtype,
        bnb_4bit_use_double_quant=True,
    )
    tokenizer_source = model_name if no_adapter else adapter_path
    tokenizer = AutoTokenizer.from_pretrained(
        tokenizer_source,
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
    base = AutoModelForCausalLM.from_pretrained(model_name, **kwargs)

    embedding_count = int(getattr(base.get_input_embeddings(), "num_embeddings", 0) or 0)
    tokenizer_length = len(tokenizer)
    if embedding_count and tokenizer_length > embedding_count:
        base.resize_token_embeddings(tokenizer_length)

    model = base if no_adapter else PeftModel.from_pretrained(base, adapter_path, local_files_only=local_files_only)
    model.eval()
    if hasattr(model.config, "use_cache"):
        model.config.use_cache = True
    if getattr(model, "generation_config", None) is not None:
        model.generation_config.use_cache = True
    if torch.cuda.is_available():
        properties = torch.cuda.get_device_properties(0)
        logging.info(
            "INFERENCE_DEVICE name=%s total_memory=%s pci_bus_id=%s cuda_visible_devices=%s",
            torch.cuda.get_device_name(0),
            properties.total_memory,
            getattr(properties, "pci_bus_id", "unknown"),
            os.environ.get("CUDA_VISIBLE_DEVICES", ""),
        )
    return model, tokenizer


def generate_prediction(model, tokenizer, prompt: str, args: argparse.Namespace) -> str:
    old_truncation_side = getattr(tokenizer, "truncation_side", "right")
    tokenizer.truncation_side = "left"
    try:
        inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=args.max_length)
    finally:
        tokenizer.truncation_side = old_truncation_side
    device = next(model.parameters()).device
    inputs = {key: value.to(device) for key, value in inputs.items()}
    input_len = inputs["input_ids"].shape[1]
    im_end_id = tokenizer.convert_tokens_to_ids("<|im_end|>")
    eos_ids = [tokenizer.eos_token_id]
    if isinstance(im_end_id, int) and im_end_id >= 0 and im_end_id != tokenizer.eos_token_id:
        eos_ids.append(im_end_id)
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=args.max_new_tokens,
            do_sample=False,
            repetition_penalty=args.repetition_penalty,
            no_repeat_ngram_size=args.no_repeat_ngram_size,
            eos_token_id=eos_ids,
            pad_token_id=tokenizer.eos_token_id,
        )
    prediction = tokenizer.decode(outputs[0][input_len:], skip_special_tokens=False).strip()
    for marker in ("<|im_end|>", "<|endoftext|>"):
        if marker in prediction:
            prediction = prediction.split(marker, 1)[0].strip()
    for marker in ("<|im_start|>", "<|end|>", "<|assistant|>", "<|user|>", "<|system|>"):
        prediction = prediction.replace(marker, "")
    return prediction.strip() or UNKNOWN


def generation_looks_corrupted(prediction: str) -> bool:
    text = normalize_text(prediction).lower()
    if any(marker in text for marker in CORRUPTED_GENERATION_MARKERS):
        return True
    return text.startswith("context:") or text.startswith("question:")


def _token_repetition_loop(text: str) -> bool:
    tokens = re.findall(r"[a-zA-Z0-9_./-]+", (text or "").lower())
    if len(tokens) < 12:
        return False
    for n in (1, 2, 3, 4):
        grams = [tuple(tokens[i : i + n]) for i in range(0, len(tokens) - n + 1)]
        if not grams:
            continue
        most_common = max(grams.count(gram) for gram in set(grams))
        if most_common >= 6 and most_common / len(grams) >= 0.35:
            return True
    return False


def _continuous_substring_loop(text: str) -> bool:
    compact = re.sub(r"\s+", "", (text or "").lower())
    if len(compact) < 24:
        return False
    for size in range(3, 25):
        for start in range(0, min(size, len(compact) - size * 4 + 1)):
            chunk = compact[start : start + size]
            if len(set(chunk)) <= 1:
                continue
            repeated = chunk * 4
            if repeated in compact:
                return True
    return False


def legacy_generate_prediction(model, tokenizer, prompt: str, args: argparse.Namespace) -> str:
    inputs = tokenizer(prompt, return_tensors="pt")
    device = next(model.parameters()).device
    inputs = {key: value.to(device) for key, value in inputs.items()}
    input_len = inputs["input_ids"].shape[1]
    generation_kwargs = {
        "max_new_tokens": args.max_new_tokens,
        "do_sample": False,
        "top_p": args.top_p,
        "repetition_penalty": args.repetition_penalty,
        "eos_token_id": tokenizer.eos_token_id,
        "pad_token_id": tokenizer.eos_token_id,
    }
    with torch.no_grad():
        outputs = model.generate(**inputs, **generation_kwargs)
    prediction = tokenizer.decode(outputs[0][input_len:], skip_special_tokens=True).strip()
    for marker in ("<|im_end|>", "<|endoftext|>"):
        if marker in prediction:
            prediction = prediction.split(marker, 1)[0].strip()
    return prediction or UNKNOWN


def read_jsonl(path: Path, limit: Optional[int] = None) -> Iterable[Dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        for idx, line in enumerate(handle):
            if limit is not None and idx >= limit:
                break
            if line.strip():
                yield json.loads(line)


def extract_qa(row: Dict[str, Any]) -> Tuple[str, str]:
    messages = row.get("messages") or []
    question = ""
    reference = ""
    for message in messages:
        if message.get("role") == "user" and not question:
            question = normalize_text(message.get("content"))
        if message.get("role") == "assistant" and not reference:
            reference = normalize_text(message.get("content"))
    return question, reference


def _normalize_bug_token(token: str) -> str:
    token = re.sub(r"^[^\w]+|[^\w]+$", "", token or "")
    token = token.replace("_", "-")
    digits = re.sub(r"\D", "", token)
    if token.isdigit() or len(digits) >= 4:
        return digits or token.lower()
    return token.lower()


def bug_ids(text: str) -> List[str]:
    found: List[str] = []
    for token in re.findall(r"\b\d{6}\b", text or ""):
        normalized = _normalize_bug_token(token)
        if normalized and normalized not in found:
            found.append(normalized)
    bug_prefixed = re.findall(r"(?i)\bbug(?:\s+id)?\s*[:#-]?\s*([A-Za-z0-9][A-Za-z0-9_-]{2,15})", text or "")
    for token in bug_prefixed:
        normalized = _normalize_bug_token(token)
        if normalized and normalized not in found:
            found.append(normalized)
    return found


def command_like(text: str) -> bool:
    return bool(
        re.search(
            r"(?mi)^\s*(show|configure|config|copy|crypto|certificate|router|ip route|access-list|class|policy|vlan|interface)\b",
            text or "",
        )
    )


def is_degenerate_prediction(text: str) -> bool:
    compact = re.sub(r"\s+", "", (text or "").lower())
    if not compact:
        return True
    if "traftraftraf" in compact or "theraftraf" in compact:
        return True
    if compact.count("traf") >= 8:
        return True
    if len(compact) >= 80 and len(set(compact)) <= 8:
        return True
    return _token_repetition_loop(text) or _continuous_substring_loop(text)


def judge_prediction(question: str, prediction: str, case: Dict[str, Any], reference: str = "") -> Dict[str, Any]:
    row = {
        **case,
        "question": question,
        "reference": reference,
        "prediction": prediction,
    }
    review = strict_review(row)
    review["degenerate"] = bool(review["checks"]["repetition_loop"])
    return review


def strict_row(question: str, prediction: str, case: Dict[str, Any], reference: str = "") -> Dict[str, Any]:
    if generation_looks_corrupted(prediction):
        raise RuntimeError(f"Corrupted generation/decoding detected before scoring: {prediction[:160]}")
    return judge_prediction(question, prediction, case, reference)


def write_jsonl(path: Path, rows: Iterable[Dict[str, Any]]) -> int:
    count = 0
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
            count += 1
    return count


def run_manual(model, tokenizer, args: argparse.Namespace) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    manual_cases = build_manual_cases(args.test_data_path, args.manual_limit)
    for idx, case in enumerate(manual_cases, start=1):
        logging.info("Manual inference %s/%s", idx, len(manual_cases))
        prompt = build_prompt(case, case["question"], tokenizer)
        prediction = generate_prediction(model, tokenizer, prompt, args)
        review = strict_row(case["question"], prediction, case)
        rows.append(
            {
                **case,
                "reference": "",
                "prompt": prompt,
                "prediction": prediction,
                "adapter_path": str(args.adapter_path),
                "prompt_type": "release_notes_chatml",
                "model_name": args.model_name,
                "generation": {
                    "do_sample": False,
                    "temperature": 0.0,
                    "top_p": args.top_p,
                    "max_new_tokens": args.max_new_tokens,
                    "repetition_penalty": args.repetition_penalty,
                    "no_repeat_ngram_size": args.no_repeat_ngram_size,
                    "eos_token_id": ["tokenizer.eos_token_id", "<|im_end|>"],
                },
                "review": review,
                "strict_review": review,
            }
        )
    return rows


def run_subset(model, tokenizer, args: argparse.Namespace) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    if args.subset_size <= 0:
        return rows
    for idx, row in enumerate(read_jsonl(args.test_data_path, args.subset_size), start=1):
        question, reference = extract_qa(row)
        case = {
            "switch": normalize_text(row.get("switch")),
            "version": normalize_text(row.get("version")).replace("_", "."),
            "sub_version": normalize_text(row.get("sub_version")),
            "source_type": normalize_text(row.get("source_type")),
            "data_family": normalize_text(row.get("data_family")),
            "document_title": normalize_text(row.get("document_title")),
            "section": normalize_text(row.get("section")),
            "topic": normalize_text(row.get("topic")),
            "command": normalize_text(row.get("command") or row.get("command_name")),
        }
        logging.info("Subset inference %s/%s", idx, args.subset_size)
        prompt = build_prompt(case, question, tokenizer)
        prediction = generate_prediction(model, tokenizer, prompt, args)
        review = strict_row(question, prediction, case, reference)
        rows.append(
            {
                "question": question,
                "reference": reference,
                "prompt": prompt,
                "prediction": prediction,
                "adapter_path": str(args.adapter_path),
                "prompt_type": "release_notes_chatml",
                "model_name": args.model_name,
                **case,
                "review": review,
                "strict_review": review,
            }
        )
    return rows


def summarize_bool(rows: List[Dict[str, Any]], key: str) -> str:
    if not rows:
        return "n/a"
    total = len(rows)
    ok = sum(1 for row in rows if row.get("review", {}).get("checks", {}).get(key))
    return f"{ok}/{total}"


def compact_prediction(row: Dict[str, Any]) -> str:
    question = row.get("question", "")
    prediction = row.get("prediction", "")
    score = row.get("review", {}).get("score", 0)
    text = prediction.replace("\n", " ")
    if len(text) > 260:
        text = text[:257] + "..."
    return f"- score {score}/10 | Q: {question}\n  A: {text}"


def rows_with_strict_review(rows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    reviewed: List[Dict[str, Any]] = []
    for row in rows:
        item = dict(row)
        review = item.get("strict_review") or item.get("review")
        if not review or "checks" not in review or "is_cli_row" not in review.get("checks", {}):
            review = strict_review(item)
        item["strict_review"] = review
        item["review"] = review
        reviewed.append(item)
    return reviewed


def load_prediction_rows(directory: Path) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for filename in ("manual_predictions.jsonl", "test_subset_predictions.jsonl"):
        path = directory / filename
        if not path.exists():
            continue
        for row in read_jsonl(path):
            item = dict(row)
            item["source_file"] = str(path)
            rows.append(item)
    return rows_with_strict_review(rows)


def metric_counts(rows: List[Dict[str, Any]]) -> Dict[str, Any]:
    partitions = partition_summaries(rows)
    # Manual prompts have no reference answers, so they remain smoke tests only.
    summary = partitions["reference_backed_factual_tests"]
    manual_summary = partitions["manual_smoke_tests"]
    factual_rows = [row for row in rows if normalize_text(row.get("reference"))]
    bug_rows = [row for row in factual_rows if row["strict_review"].get("requested_bug_ids")]
    wrong_bug = summary["wrong_bug_id_predictions"]
    bug_id_accuracy = None if not bug_rows else round((len(bug_rows) - wrong_bug) / len(bug_rows), 4)
    return {
        **summary,
        "reference_backed_factual_tests": summary,
        "manual_smoke_tests": manual_summary,
        "bug_id_accuracy": bug_id_accuracy,
        "fake_bug_id_count": summary["fake_bug_id_predictions"],
        "wrong_release_date_count": summary["wrong_date_predictions"],
        "invented_workaround_count": summary["invented_workaround_predictions"],
        "generic_hallucination_count": summary["generic_hallucination_predictions"],
        "acronym_hallucination_count": summary["acronym_meaning_hallucination_predictions"],
    }


def report_prediction_lines(rows: List[Dict[str, Any]], reverse: bool, limit: int = 5) -> List[str]:
    ordered = sorted(rows, key=lambda row: row["strict_review"]["score"], reverse=reverse)[:limit]
    if not ordered:
        return ["- none"]
    lines: List[str] = []
    for row in ordered:
        review = row["strict_review"]
        caps = ", ".join(review.get("score_cap_reasons", [])) or "none"
        lines.append(f"- score {review['score']}/10 | caps={caps}")
        lines.append(f"  Q: {compact_text(row.get('question'), 180)}")
        if row.get("reference"):
            lines.append(f"  Ref: {compact_text(row.get('reference'), 180)}")
        lines.append(f"  A: {compact_text(row.get('prediction'), 240)}")
    return lines


def common_failure_patterns(rows: List[Dict[str, Any]], metrics: Dict[str, Any]) -> List[str]:
    patterns = [
        ("Repetition loop", metrics["repetition_loop_predictions"]),
        ("Wrong requested release-note ID", metrics["wrong_bug_id_predictions"]),
        ("Wrong release-note category", metrics["wrong_category_label_predictions"]),
        ("Fake release-note ID", metrics["fake_bug_id_predictions"]),
        ("Wrong Event ID", metrics["wrong_event_id_count"]),
        ("Fake Event ID", metrics["fake_event_id_count"]),
        ("Missing Event ID", metrics["missing_event_id_count"]),
        ("Wrong CLI syntax", metrics["wrong_cli_syntax_predictions"]),
        ("Unsupported extra CLI", metrics["unsupported_extra_cli_predictions"]),
        ("CLI hallucination", metrics["cli_hallucination_predictions"]),
        ("Wrong release date", metrics["wrong_date_predictions"]),
        ("Invented workaround", metrics["invented_workaround_predictions"]),
        ("Generic/vendor hallucination", metrics["generic_hallucination_predictions"]),
        ("Acronym hallucination", metrics["acronym_meaning_hallucination_predictions"]),
        ("Placeholder/template output", metrics["placeholder_template_predictions"]),
        ("False abstention", metrics["false_abstention_predictions"]),
    ]
    lines = [f"- {name}: {count}" for name, count in patterns if count]
    return lines or ["- No major strict failure pattern found."]


def release_note_family_summary(rows: List[Dict[str, Any]]) -> List[str]:
    grouped: Dict[str, List[Dict[str, Any]]] = {}
    for row in rows:
        family = normalize_text(row.get("data_family")) or "unknown"
        grouped.setdefault(family, []).append(row)
    lines: List[str] = []
    for family in sorted(grouped):
        family_rows = grouped[family]
        scores = [float(row["strict_review"]["score"]) for row in family_rows if row.get("strict_review")]
        average_score = round(sum(scores) / max(len(scores), 1), 2)
        lines.append(f"- {family}: {len(family_rows)} rows, average strict score {average_score:.2f}/10")
    return lines or ["- No release-note families found."]


def release_note_source_summary(rows: List[Dict[str, Any]]) -> List[str]:
    grouped: Dict[str, List[Dict[str, Any]]] = {}
    for row in rows:
        source = normalize_text(row.get("source_type")) or "unknown"
        grouped.setdefault(source, []).append(row)
    lines: List[str] = []
    for source in sorted(grouped):
        source_rows = grouped[source]
        scores = [float(row["strict_review"]["score"]) for row in source_rows if row.get("strict_review")]
        average_score = round(sum(scores) / max(len(scores), 1), 2)
        lines.append(f"- {source}: {len(source_rows)} rows, average strict score {average_score:.2f}/10")
    return lines or ["- No release-note sources found."]


def load_old_3000_comparison() -> Tuple[Optional[Dict[str, Any]], List[str]]:
    old_dir = Path("outputs_inference/qwen25_3b_release_notes_only_1epoch_stratified_checkpoint-3000_release_source_disjoint100")
    required = [old_dir / "manual_predictions.jsonl", old_dir / "test_subset_predictions.jsonl"]
    notes: List[str] = []
    if not all(path.exists() for path in required):
        notes.append(f"Old 3000 comparison skipped; missing files under {old_dir}.")
        return None, notes
    old_rows = load_prediction_rows(old_dir)
    metrics = metric_counts(old_rows)
    notes.append(f"Old 3000 comparison loaded from {old_dir}.")
    if (old_dir / "strict_inference_review.md").exists():
        notes.append(f"Old 3000 strict report exists: {old_dir / 'strict_inference_review.md'}.")
    return metrics, notes


def final_verdict(metrics: Dict[str, Any], old_metrics: Optional[Dict[str, Any]]) -> str:
    if metrics["degenerate_predictions"] > 0:
        return "Stop and debug generation/decoding before continuing."
    if metrics["placeholder_template_predictions"] > 0:
        return "Stop and clean template/placeholder training rows before continuing."
    if old_metrics:
        fewer_bug = metrics["wrong_bug_id_predictions"] < old_metrics.get("wrong_bug_id_predictions", 10**9)
        fewer_fake = metrics["fake_bug_id_predictions"] < old_metrics.get("fake_bug_id_predictions", 10**9)
        fewer_cli = metrics["wrong_cli_syntax_predictions"] < old_metrics.get("wrong_cli_syntax_predictions", 10**9)
        fewer_event = metrics["wrong_event_id_count"] < old_metrics.get("wrong_event_id_count", 10**9)
        if fewer_bug and fewer_fake and fewer_event and fewer_cli:
            return "Recommend continuing release-notes training from 1000 steps to 3000 steps."
    event_or_cli_failures = (
        metrics["wrong_event_id_count"]
        + metrics["wrong_cli_syntax_predictions"]
        + metrics["generic_hallucination_predictions"]
    )
    if event_or_cli_failures >= 10:
        return "Recommend fixing or oversampling CLI and event-log data before continuing."
    if metrics["average_score"] >= 7.5 and metrics["good_predictions_count"] >= metrics["bad_predictions_count"]:
        return "Promising baseline; continue release-notes training only after spot-checking failures."
    return "Baseline only; fix high-frequency strict failures before continuing."


def write_report(
    output_dir: Path,
    manual_rows: List[Dict[str, Any]],
    subset_rows: List[Dict[str, Any]],
    log_path: Path,
    args: argparse.Namespace,
) -> None:
    all_rows = rows_with_strict_review(manual_rows + subset_rows)
    metrics = metric_counts(all_rows)
    factual_rows = [row for row in all_rows if normalize_text(row.get("reference"))]
    manual_smoke = [row for row in all_rows if not normalize_text(row.get("reference"))]
    old_metrics, comparison_notes = load_old_3000_comparison()
    verdict = final_verdict(metrics, old_metrics)
    old_delta: Dict[str, Any] = {}
    if old_metrics:
        for key in (
            "degenerate_predictions",
            "wrong_bug_id_predictions",
            "fake_bug_id_predictions",
            "wrong_event_id_count",
            "fake_event_id_count",
            "missing_event_id_count",
            "wrong_cli_syntax_predictions",
            "cli_hallucination_predictions",
            "unsupported_extra_cli_predictions",
            "average_score",
        ):
            old_delta[key] = {
                "release_notes_1000": metrics.get(key),
                "old_3000": old_metrics.get(key),
            }

    payload = {
        "adapter_path": str(args.adapter_path),
        "model_name": args.model_name,
        "output_dir": str(args.output_dir),
        "log_path": str(log_path),
        "manual_predictions_path": str(output_dir / "manual_predictions.jsonl"),
        "test_subset_predictions_path": str(output_dir / "test_subset_predictions.jsonl"),
        "metrics": metrics,
        "reference_backed_factual_tests": metrics["reference_backed_factual_tests"],
        "manual_smoke_tests": metrics["manual_smoke_tests"],
        "old_3000_comparison": old_delta or None,
        "comparison_notes": comparison_notes,
        "common_failure_patterns": common_failure_patterns(all_rows, metrics),
        "final_verdict": verdict,
        "best_predictions": sorted(factual_rows, key=lambda row: row["strict_review"]["score"], reverse=True)[:5],
        "worst_predictions": sorted(factual_rows, key=lambda row: row["strict_review"]["score"])[:5],
    }
    (output_dir / "strict_inference_review.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")

    def fmt(value: Any) -> str:
        return "n/a" if value is None else str(value)

    lines = [
        "# Strict Release-Notes 1000-Step Inference Review",
        "",
        f"- Adapter loaded successfully: yes",
        f"- Model: {args.model_name}",
        f"- Adapter: {'none (base model only)' if args.no_adapter else args.adapter_path}",
        f"- Log file: {log_path}",
        f"- Reference-backed factual tests: {metrics['total_predictions']}",
        f"- Manual smoke tests: {len(manual_smoke)} (excluded from factual scores)",
        f"- Degenerate predictions: {metrics['degenerate_predictions']}",
        f"- Repetition-loop count: {metrics['repetition_loop_predictions']}",
        f"- Loop fixed: {str(metrics['loop_fixed']).lower()}",
        f"- Average strict score: {metrics['average_score']:.2f}/10",
        f"- Good prediction count: {metrics['good_predictions_count']}",
        f"- Bad prediction count: {metrics['bad_predictions_count']}",
        f"- Release-note ID accuracy: {fmt(metrics['bug_id_accuracy'])}",
        f"- Wrong requested release-note ID count: {metrics['wrong_bug_id_predictions']}",
        f"- Release-note category accuracy: {fmt(metrics['category_label_accuracy'])}",
        f"- Wrong release-note category count: {metrics['wrong_category_label_predictions']}",
        f"- Fake release-note ID count: {metrics['fake_bug_id_count']}",
        f"- Event ID accuracy: {fmt(metrics['event_id_accuracy'])}",
        f"- Wrong Event ID count: {metrics['wrong_event_id_count']}",
        f"- Fake Event ID count: {metrics['fake_event_id_count']}",
        f"- Missing Event ID count: {metrics['missing_event_id_count']}",
        f"- Wrong CLI syntax count: {metrics['wrong_cli_syntax_predictions']}",
        f"- CLI hallucination count: {metrics['cli_hallucination_predictions']}",
        f"- Unsupported extra CLI count: {metrics['unsupported_extra_cli_predictions']}",
        f"- Wrong release date count: {metrics['wrong_release_date_count']}",
        f"- Invented workaround count: {metrics['invented_workaround_count']}",
        f"- Generic hallucination count: {metrics['generic_hallucination_count']}",
        f"- Acronym hallucination count: {metrics['acronym_hallucination_count']}",
        f"- Placeholder/template output count: {metrics['placeholder_template_predictions']}",
        f"- Correct abstention count: {metrics['correct_abstention_predictions']}",
        f"- False abstention count: {metrics['false_abstention_predictions']}",
        f"- Abstention-reference rows: {metrics['abstention_reference_rows']}",
        f"- Manual questions tested: {len(manual_rows)}",
        f"- Test subset examples generated: {len(subset_rows)}",
        "",
        "## Release-Notes Coverage",
        "",
        *release_note_family_summary(factual_rows),
        "",
        "## Release-Notes Source Types",
        "",
        *release_note_source_summary(factual_rows),
        "",
        "## Strict Check Counts",
        "",
        f"- not_degenerate: {summarize_bool(factual_rows, 'not_degenerate')}",
        f"- repetition_loop: {summarize_bool(factual_rows, 'repetition_loop')}",
        f"- placeholder_template_output: {summarize_bool(factual_rows, 'placeholder_template_output')}",
        f"- answers_directly: {summarize_bool(factual_rows, 'answers_directly')}",
        f"- preserves_requested_bug_id: {summarize_bool(factual_rows, 'preserves_requested_bug_id')}",
        f"- event_id_preserved: {summarize_bool(factual_rows, 'event_id_preserved')}",
        f"- avoids_fake_event_ids: {summarize_bool(factual_rows, 'avoids_fake_event_ids')}",
        f"- avoids_fake_bug_ids: {summarize_bool(factual_rows, 'avoids_fake_bug_ids')}",
        f"- date_preserved: {summarize_bool(factual_rows, 'date_preserved')}",
        f"- preserves_real_cli_syntax_when_known: {summarize_bool(factual_rows, 'preserves_real_cli_syntax_when_known')}",
        f"- wrong_cli_syntax: {summarize_bool(factual_rows, 'wrong_cli_syntax')}",
        f"- unsupported_extra_cli: {summarize_bool(factual_rows, 'unsupported_extra_cli')}",
        f"- cli_hallucination: {summarize_bool(factual_rows, 'cli_hallucination')}",
        f"- acronym_meaning_hallucination: {summarize_bool(factual_rows, 'acronym_meaning_hallucination')}",
        f"- avoids_fake_workarounds: {summarize_bool(factual_rows, 'avoids_fake_workarounds')}",
        f"- generic_hallucination: {summarize_bool(factual_rows, 'generic_hallucination')}",
        f"- reference_keyword_grounded: {summarize_bool(factual_rows, 'reference_keyword_grounded')}",
        f"- correct_abstention: {summarize_bool(factual_rows, 'correct_abstention')}",
        f"- false_abstention: {summarize_bool(factual_rows, 'false_abstention')}",
        "",
        "## 5 Best Predictions",
        "",
        *report_prediction_lines(factual_rows, reverse=True),
        "",
        "## 5 Worst Predictions",
        "",
        *report_prediction_lines(factual_rows, reverse=False),
        "",
        "## Common Failure Patterns",
        "",
        *common_failure_patterns(all_rows, metrics),
        "",
        "## Old 3000 Comparison",
        "",
        *(f"- {note}" for note in comparison_notes),
    ]
    if old_delta:
        lines.extend(["", "| Metric | release_notes_1000 | old_3000 |", "|---|---:|---:|"])
        for key, values in old_delta.items():
            lines.append(f"| {key} | {values['release_notes_1000']} | {values['old_3000']} |")
    lines.extend(
        [
        "",
        "## Final Verdict",
        "",
        verdict,
    ])
    (output_dir / "strict_inference_review.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Inference test for the completed 1000-step Aruba AOS-CX LoRA adapter")
    parser.add_argument(
        "--model_name",
        default=None,
        help="Base model override. For adapters, omission safely uses adapter_config.json.",
    )
    parser.add_argument("--adapter_path", type=Path, default=ADAPTER_PATH)
    parser.add_argument("--output_dir", type=Path, default=OUTPUT_DIR)
    parser.add_argument("--test_data_path", type=Path, default=TEST_DATA_PATH)
    parser.add_argument("--subset_size", type=int, default=50)
    parser.add_argument("--manual_limit", type=int, default=None)
    parser.add_argument("--max_length", type=int, default=512)
    parser.add_argument("--max_new_tokens", type=int, default=160)
    parser.add_argument("--top_p", type=float, default=1.0)
    parser.add_argument("--repetition_penalty", type=float, default=1.0)
    parser.add_argument("--no_repeat_ngram_size", type=int, default=0)
    parser.add_argument("--local_files_only", action="store_true")
    parser.add_argument("--allow_gpu_busy", action="store_true")
    parser.add_argument("--no_adapter", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    args.model_name = resolve_model_name(args.model_name, args.adapter_path, args.no_adapter)
    log_path = setup_logging(args.output_dir)
    logging.info("Starting adapter inference")
    logging.info("MODEL_NAME=%s", args.model_name)
    logging.info("ADAPTER_PATH=%s", args.adapter_path.resolve() if not args.no_adapter else "none")
    logging.info("OUTPUT_DIR=%s", args.output_dir.resolve())
    logging.info("TEST_DATA_PATH=%s", args.test_data_path.resolve())
    logging.info("MAX_NEW_TOKENS=%s", args.max_new_tokens)
    logging.info("CUDA_VISIBLE_DEVICES=%s", os.environ.get("CUDA_VISIBLE_DEVICES", ""))
    if not args.no_adapter:
        verify_adapter(args.adapter_path)
    if not args.test_data_path.exists():
        raise FileNotFoundError(args.test_data_path)

    busy = gpu0_compute_processes()
    if busy and not args.allow_gpu_busy:
        logging.error("GPU 0 has active compute processes. Refusing to start inference: %s", busy)
        raise SystemExit(
            "GPU 0 is busy. Wait for training to finish, or pass --allow_gpu_busy if you intentionally want to share it."
        )

    model, tokenizer = load_model(args.model_name, args.adapter_path, args.local_files_only, args.no_adapter)
    manual_rows = run_manual(model, tokenizer, args)
    subset_rows = run_subset(model, tokenizer, args)

    manual_count = write_jsonl(args.output_dir / "manual_predictions.jsonl", manual_rows)
    subset_count = write_jsonl(args.output_dir / "test_subset_predictions.jsonl", subset_rows)
    write_report(args.output_dir, manual_rows, subset_rows, log_path, args)

    logging.info("Manual predictions written: %s", manual_count)
    logging.info("Subset predictions written: %s", subset_count)
    logging.info("Strict review markdown written: %s", args.output_dir / "strict_inference_review.md")
    logging.info("Strict review JSON written: %s", args.output_dir / "strict_inference_review.json")


if __name__ == "__main__":
    main()
