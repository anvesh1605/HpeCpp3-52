import argparse
from collections import Counter, defaultdict
import json
import logging
import math
import os
import re
import time
import warnings
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Sequence, Set, Tuple

import bitsandbytes as bnb
import evaluate
import numpy as np
import torch
import wandb
from datasets import Dataset, DatasetDict
from peft import LoraConfig, PeftModel, TaskType, get_peft_model, prepare_model_for_kbit_training
from torch.utils.data import WeightedRandomSampler
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    EarlyStoppingCallback,
    TrainerCallback,
    TrainingArguments,
    set_seed,
)

try:
    from trl import DataCollatorForCompletionOnlyLM, SFTTrainer
except ImportError:
    DataCollatorForCompletionOnlyLM = None
    from trl import SFTTrainer


LOGGER = logging.getLogger("train")

DEFAULT_MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
DEFAULT_TEMPLATE = "tinyllama"
DEFAULT_WEIGHT_FIELDS = ["data_family", "source_type", "section"]
DEFAULT_REPORT_FIELDS = ["source_type", "data_family", "section", "switch", "version", "sub_version"]
DEFAULT_MIN_SAMPLE_WEIGHT = 0.5
DEFAULT_MAX_SAMPLE_WEIGHT = 4.0
DEFAULT_WEIGHT_SMOOTHING = 1.0
MISSING_METADATA_VALUES = {"", "unknown", "n/a", "na", "none", "null", "<missing>"}

SYSTEM_PROMPT = (
    "You are an Aruba AOS-CX release-notes assistant.\n"
    "You answer using the provided release-note training data only.\n"
    "Preserve documented release-note facts exactly, including bug IDs when present, categories, symptoms, causes, workarounds, "
    "release dates, version history, supported products, compatibility, certifications, and procedures when known.\n"
    "Do not invent unsupported bug IDs, workarounds, affected versions, release dates, product mappings, compatibility claims, or configuration steps.\n"
    'If the information is not documented in the training data, answer exactly: "This information is not documented in the available training data."'
)

METADATA_CONTEXT_INSTRUCTION = (
    "You are answering from HPE Aruba AOS-CX release notes only. "
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
    "bug_details",
    "event_description",
}

TEMPLATES: Dict[str, Dict[str, str]] = {
    "chatml": {
        "system_prefix": "<|im_start|>system\n",
        "system_suffix": "<|im_end|>\n",
        "user_prefix": "<|im_start|>user\n",
        "user_suffix": "<|im_end|>\n",
        "assistant_prefix": "<|im_start|>assistant\n",
        "assistant_suffix": "<|im_end|>",
        "response_template": "<|im_start|>assistant\n",
    },
    "llama": {
        "system_prefix": "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\n",
        "system_suffix": "<|eot_id|>",
        "user_prefix": "<|start_header_id|>user<|end_header_id|>\n\n",
        "user_suffix": "<|eot_id|>",
        "assistant_prefix": "<|start_header_id|>assistant<|end_header_id|>\n\n",
        "assistant_suffix": "<|eot_id|>",
        "response_template": "<|start_header_id|>assistant<|end_header_id|>\n\n",
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
    "tinyllama": {
        "system_prefix": "<|system|>\n",
        "system_suffix": "</s>\n",
        "user_prefix": "<|user|>\n",
        "user_suffix": "</s>\n",
        "assistant_prefix": "<|assistant|>\n",
        "assistant_suffix": "</s>",
        "response_template": "<|assistant|>\n",
    },
    "gemma": {
        "system_prefix": "<start_of_turn>user\n",
        "system_suffix": "\n\n",
        "user_prefix": "",
        "user_suffix": "<end_of_turn>\n",
        "assistant_prefix": "<start_of_turn>model\n",
        "assistant_suffix": "<end_of_turn>",
        "response_template": "<start_of_turn>model\n",
    },
    "phi": {
        "system_prefix": "<|system|>\n",
        "system_suffix": "<|end|>\n",
        "user_prefix": "<|user|>\n",
        "user_suffix": "<|end|>\n",
        "assistant_prefix": "<|assistant|>\n",
        "assistant_suffix": "<|end|>",
        "response_template": "<|assistant|>\n",
    },
    "plain": {
        "system_prefix": "### System:\n\n",
        "system_suffix": "\n\n",
        "user_prefix": "### Instruction:\n\n",
        "user_suffix": "\n\n",
        "assistant_prefix": "### Response:\n\n",
        "assistant_suffix": "",
        "response_template": "### Response:\n\n",
    },
}

DEFAULT_TARGET_MODULES = [
    "q_proj",
    "k_proj",
    "v_proj",
    "o_proj",
    "gate_proj",
    "up_proj",
    "down_proj",
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

FAKE_BUG_IDS = {
    "000000",
    "111111",
    "123456",
    "222222",
    "333333",
    "444444",
    "555555",
    "666666",
    "777777",
    "789012",
    "888888",
    "999999",
}

CLI_WORDS = {
    "apply",
    "show",
    "configure",
    "interface",
    "vlan",
    "ip",
    "router",
    "access-list",
    "copp-policy",
    "policy",
    "class",
    "aaa",
    "radius",
    "bgp",
    "ospf",
    "vsx",
    "lag",
}

COMMAND_PREFIXES = {
    "access-list",
    "boot",
    "class",
    "clear",
    "configure",
    "copy",
    "crypto",
    "debug",
    "erase",
    "interface",
    "ip",
    "ipv6",
    "no",
    "policy",
    "reload",
    "router",
    "show",
    "vlan",
}

CLI_DATA_FAMILIES = {
    "cli_command_reference",
    "show_command_reference",
}

CLI_QUESTION_PHRASES = (
    "what is the syntax",
    "what does the command do",
    "show command",
    "clear command",
    "configure command",
)

CLI_FILLER = {
    "command",
    "commands",
    "do",
    "does",
    "following",
    "format",
    "is",
    "of",
    "optional",
    "parameter",
    "parameters",
    "purpose",
    "syntax",
    "the",
    "usage",
    "use",
    "used",
    "what",
}

BAD_ERPS_EXPANSIONS = (
    "egress rate profile statistics",
    "error rate profile statistics",
    "error reporting per second",
    "extended route processing statistics",
)

LAST_EVAL_REVIEWS: List[Dict[str, Any]] = []


PRODUCT_DATA_FAMILIES = {
    "cli_command_reference",
    "show_command_reference",
    "concept_explanation",
    "configuration_procedure",
    "event_log_reference",
    "feature_limitation",
    "qos_policy",
    "security_policy",
    "routing_feature",
    "monitoring_feature",
    "troubleshooting",
    "rest_api_reference",
    "snmp_mib_reference",
    "web_ui_task",
}


def is_product_family(family: str) -> bool:
    return normalize_text(family) in PRODUCT_DATA_FAMILIES


def command_value(sample: Dict[str, Any]) -> str:
    return normalize_text(sample.get("command") or sample.get("command_name") or "")


def normalize_text(value: Any, preserve_newlines: bool = False) -> str:
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
    if preserve_newlines:
        text = re.sub(r"[ \t]+", " ", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
    else:
        text = re.sub(r"\s+", " ", text)
    return text.strip()


def load_jsonl(path: str) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    with open(path, "r", encoding="utf-8-sig") as handle:
        for line_no, line in enumerate(handle, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON in {path}:{line_no}: {exc}") from exc
            if isinstance(row, dict):
                rows.append(row)
    return rows


def first_message(row: Dict[str, Any], role: str) -> str:
    for message in row.get("messages", []):
        if str(message.get("role", "")).strip().lower() == role:
            return normalize_text(message.get("content", ""), preserve_newlines=(role == "assistant"))
    return ""


def build_metadata_context(sample: Dict[str, Any]) -> str:
    lines = ["Context:"]
    for label, default_value in SAFE_METADATA_FIELDS:
        if label in ANSWER_LEAKING_CONTEXT_FIELDS:
            continue
        value = default_value if default_value is not None else sample.get(label, "")
        if label == "command":
            value = sample.get("command") or sample.get("command_name", "")
        text = normalize_text(value)
        if text:
            lines.append(f"{label}: {text}")
    return "\n".join(lines).strip()


def build_user_content_with_metadata(sample: Dict[str, Any], original_question: str) -> str:
    question = normalize_text(original_question, preserve_newlines=True)
    return "\n\n".join(
        [
            METADATA_CONTEXT_INSTRUCTION,
            build_metadata_context(sample),
            f"Question:\n{question}",
        ]
    ).strip()


def sanitize_message_content(content: Any, template_name: str) -> str:
    text = normalize_text(content, preserve_newlines=True)
    template = TEMPLATES[template_name]
    for marker in template.values():
        if marker and marker in text:
            text = text.replace(marker, " ")
    return normalize_text(text, preserve_newlines=True)


def build_prompt(sample: Dict[str, Any], template_name: str) -> str:
    template = TEMPLATES[template_name]
    if "text" in sample and "messages" not in sample:
        return normalize_text(sample["text"], preserve_newlines=True)

    prompt_parts = []
    for message in sample.get("messages", []):
        role = str(message.get("role", "")).strip().lower()
        content = sanitize_message_content(message.get("content", ""), template_name)
        if role == "user":
            content = sanitize_message_content(build_user_content_with_metadata(sample, content), template_name)
            prompt_parts.append(f"{template['user_prefix']}{content}{template['user_suffix']}")
        elif role == "assistant":
            prompt_parts.append(f"{template['assistant_prefix']}{content}{template['assistant_suffix']}")
    return "".join(prompt_parts)


def print_metadata_context_samples(dataset: Dataset, template_name: str, count: int = 3) -> None:
    if template_name != "chatml":
        return
    print("=== Metadata-context formatted samples ===")
    for index in range(min(count, len(dataset))):
        text = str(dataset[index]["text"])
        print(f"--- sample {index + 1} ---")
        print(text)


def validate_metadata_context_samples(dataset: Dataset, template_name: str, count: int = 3) -> None:
    if template_name != "chatml":
        return
    sample_count = min(count, len(dataset))
    leaking_markers = [f"{field}:" for field in ANSWER_LEAKING_CONTEXT_FIELDS]
    for index in range(sample_count):
        row = dataset[index]
        text = str(row["text"])
        if "<|im_start|>user\n" not in text or "<|im_start|>assistant\n" not in text or "<|im_end|>" not in text:
            raise ValueError(f"Formatted sample {index + 1} is missing ChatML markers.")
        if "User:" in text or "Assistant:" in text:
            raise ValueError(f"Formatted sample {index + 1} contains plain User:/Assistant: markers.")
        user_start = text.index("<|im_start|>user\n") + len("<|im_start|>user\n")
        user_end = text.index("<|im_end|>", user_start)
        assistant_start = text.index("<|im_start|>assistant\n") + len("<|im_start|>assistant\n")
        assistant_end = text.index("<|im_end|>", assistant_start) if "<|im_end|>" in text[assistant_start:] else len(text)
        user_text = text[user_start:user_end]
        assistant_text = text[assistant_start:assistant_end]
        context_text = user_text.split("Question:", 1)[0]
        if "Context:\n" not in user_text:
            raise ValueError(f"Formatted sample {index + 1} is missing metadata context in the user message.")
        if "Context:" in assistant_text or "vendor:" in assistant_text or "product_family:" in assistant_text:
            raise ValueError(f"Formatted sample {index + 1} injected metadata into the assistant answer.")
        if any(marker in context_text for marker in leaking_markers):
            raise ValueError(f"Formatted sample {index + 1} includes an answer-leaking context field.")
        reference_answer = str(row.get("reference_answer", "")).strip()
        if reference_answer and reference_answer not in assistant_text:
            raise ValueError(f"Formatted sample {index + 1} does not preserve the original assistant answer.")


def row_to_dataset_item(sample: Dict[str, Any], template_name: str) -> Dict[str, Any]:
    return {
        "text": build_prompt(sample, template_name),
        "source_type": normalize_text(sample.get("source_type", "")),
        "data_family": normalize_text(sample.get("data_family", "")),
        "switch": normalize_text(sample.get("switch", "")),
        "version": normalize_text(sample.get("version", "")),
        "sub_version": normalize_text(sample.get("sub_version", "")),
        "section": normalize_text(sample.get("section", "")),
        "document_title": normalize_text(sample.get("document_title", "")),
        "command_name": command_value(sample),
        "command": command_value(sample),
        "bug_id": normalize_text(sample.get("bug_id", "")),
        "category": normalize_text(sample.get("category", "")),
        "question": first_message(sample, "user"),
        "reference_answer": first_message(sample, "assistant"),
    }


def dataset_from_jsonl(path: str, template_name: str) -> Dataset:
    return Dataset.from_list([row_to_dataset_item(row, template_name) for row in load_jsonl(path)])


def is_missing_metadata_value(value: Any) -> bool:
    text = normalize_text(value).strip().lower()
    return text in MISSING_METADATA_VALUES


def metadata_category_value(row: Dict[str, Any], field: str) -> str:
    text = normalize_text(row.get(field, ""))
    return text if text and not is_missing_metadata_value(text) else "<missing>"


def dataset_field_distribution(dataset: Dataset, field: str) -> Dict[str, int]:
    counts: Counter[str] = Counter()
    for row in dataset:
        counts[metadata_category_value(row, field)] += 1
    return dict(counts.most_common())


def choose_weight_field(row: Dict[str, Any], weight_fields: Sequence[str]) -> Optional[Tuple[str, str]]:
    for field in weight_fields:
        value = normalize_text(row.get(field, ""))
        if value and not is_missing_metadata_value(value):
            return field, value
    return None


def _normalize_and_clip_weights(
    raw_weights: Sequence[float],
    min_sample_weight: float,
    max_sample_weight: float,
) -> List[float]:
    if not raw_weights:
        return []
    values = np.asarray(list(raw_weights), dtype=np.float64)
    finite_mask = np.isfinite(values)
    if not finite_mask.all():
        values = np.where(finite_mask, values, 1.0)
    mean_value = float(values.mean()) if values.size else 1.0
    if not math.isfinite(mean_value) or mean_value <= 0:
        mean_value = 1.0
    values = values / mean_value
    values = np.clip(values, min_sample_weight, max_sample_weight)
    clipped_mean = float(values.mean()) if values.size else 1.0
    if math.isfinite(clipped_mean) and clipped_mean > 0:
        values = np.clip(values / clipped_mean, min_sample_weight, max_sample_weight)
    return [float(value) for value in values.tolist()]


def build_weight_report(
    train_dataset: Dataset,
    weight_fields: Sequence[str],
    min_sample_weight: float,
    max_sample_weight: float,
    smoothing: float = DEFAULT_WEIGHT_SMOOTHING,
) -> Tuple[List[float], Dict[str, Any]]:
    selected_weight_fields = [field for field in weight_fields if field]
    raw_distributions = {field: dataset_field_distribution(train_dataset, field) for field in DEFAULT_REPORT_FIELDS}
    selected_field_counter: Counter[str] = Counter()
    selected_category_counter: Counter[str] = Counter()
    raw_sample_weights: List[float] = []
    sample_assignments: List[Dict[str, Any]] = []

    for row in train_dataset:
        selection = choose_weight_field(row, selected_weight_fields)
        if selection is None:
            raw_sample_weights.append(1.0)
            selected_field_counter["<equal_weight>"] += 1
            selected_category_counter["<equal_weight>"] += 1
            sample_assignments.append(
                {
                    "selected_field": "<equal_weight>",
                    "selected_category": "<equal_weight>",
                    "raw_weight": 1.0,
                }
            )
            continue

        field, category = selection
        selected_field_counter[field] += 1
        selected_category_counter[f"{field}={category}"] += 1
        field_counts = raw_distributions.get(field, {})
        category_count = int(field_counts.get(category, 0))
        category_total = int(sum(field_counts.values()))
        category_count = max(category_count, 1)
        raw_weight = (category_total + smoothing * max(len(field_counts), 1)) / (category_count + smoothing)
        raw_sample_weights.append(float(raw_weight))
        sample_assignments.append(
            {
                "selected_field": field,
                "selected_category": category,
                "raw_weight": float(raw_weight),
            }
        )

    final_weights = _normalize_and_clip_weights(raw_sample_weights, min_sample_weight, max_sample_weight)

    per_field_category_weights: Dict[str, Dict[str, float]] = {}
    per_field_estimated_distribution: Dict[str, Dict[str, float]] = {}
    for field in selected_weight_fields:
        by_category: Dict[str, List[float]] = defaultdict(list)
        for sample, final_weight in zip(sample_assignments, final_weights):
            if sample["selected_field"] == field:
                by_category[str(sample["selected_category"])].append(float(final_weight))
        if not by_category:
            continue
        total_weight = sum(sum(values) for values in by_category.values())
        per_field_category_weights[field] = {
            category: float(sum(values) / max(len(values), 1)) for category, values in sorted(by_category.items())
        }
        per_field_estimated_distribution[field] = {
            category: float(sum(values) / total_weight) if total_weight else 0.0
            for category, values in sorted(by_category.items())
        }

    selected_weight_array = np.asarray(final_weights, dtype=np.float64) if final_weights else np.asarray([1.0])
    sample_weight_stats = {
        "min": float(selected_weight_array.min()) if selected_weight_array.size else 1.0,
        "max": float(selected_weight_array.max()) if selected_weight_array.size else 1.0,
        "mean": float(selected_weight_array.mean()) if selected_weight_array.size else 1.0,
        "std": float(selected_weight_array.std()) if selected_weight_array.size else 0.0,
    }
    raw_sample_weight_stats = {
        "min": float(np.min(raw_sample_weights)) if raw_sample_weights else 1.0,
        "max": float(np.max(raw_sample_weights)) if raw_sample_weights else 1.0,
        "mean": float(np.mean(raw_sample_weights)) if raw_sample_weights else 1.0,
        "std": float(np.std(raw_sample_weights)) if raw_sample_weights else 0.0,
    }

    report = {
        "enabled": True,
        "weight_priority": list(selected_weight_fields),
        "min_sample_weight": float(min_sample_weight),
        "max_sample_weight": float(max_sample_weight),
        "smoothing": float(smoothing),
        "num_train_samples": int(len(train_dataset)),
        "raw_distributions": raw_distributions,
        "selected_field_usage": dict(selected_field_counter),
        "selected_category_usage": dict(selected_category_counter),
        "assigned_category_weights": per_field_category_weights,
        "estimated_sampling_distribution": per_field_estimated_distribution,
        "raw_sample_weight_stats": raw_sample_weight_stats,
        "final_sample_weight_stats": sample_weight_stats,
    }
    return final_weights, report


def print_weight_report(report: Dict[str, Any], limit: int = 12) -> None:
    print("=== Auto sample-weight report ===", flush=True)
    print(f"Weight priority: {', '.join(report.get('weight_priority', []))}", flush=True)
    final_stats = report.get("final_sample_weight_stats", {})
    min_weight = float(final_stats.get("min", 1.0))
    max_weight = float(final_stats.get("max", 1.0))
    mean_weight = float(final_stats.get("mean", 1.0))
    print(
        f"Final sample weights: min={min_weight:.4f} max={max_weight:.4f} mean={mean_weight:.4f}",
        flush=True,
    )
    for field, counts in report.get("raw_distributions", {}).items():
        print(f"Field distribution: {field}", flush=True)
        has_weights = field in report.get("assigned_category_weights", {})
        for category, count in list(counts.items())[:limit]:
            weight = report.get("assigned_category_weights", {}).get(field, {}).get(category)
            expected = report.get("estimated_sampling_distribution", {}).get(field, {}).get(category)
            weight_text = f"{weight:.4f}" if weight is not None else ("n/a" if not has_weights else "1.0000")
            expected_text = f"{expected:.4f}" if expected is not None else ("n/a" if not has_weights else "0.0000")
            print(
                f"  {category}: count={count} weight={weight_text} estimated_mass={expected_text}",
                flush=True,
            )
        if len(counts) > limit:
            print(f"  ... {len(counts) - limit} more categories", flush=True)


def save_weight_report(output_dir: Path, report: Dict[str, Any]) -> Path:
    path = output_dir / "weight_report.json"
    save_json(path, report)
    return path


def prepare_datasets(args: argparse.Namespace) -> DatasetDict:
    train_dataset = dataset_from_jsonl(args.data_path, args.template)
    if args.val_data_path:
        validation_dataset = dataset_from_jsonl(args.val_data_path, args.template)
    else:
        split = train_dataset.train_test_split(test_size=args.val_split, seed=args.seed)
        train_dataset = split["train"]
        validation_dataset = split["test"]

    datasets = {"train": train_dataset, "validation": validation_dataset}
    if args.test_data_path:
        datasets["test"] = dataset_from_jsonl(args.test_data_path, args.template)
    return DatasetDict(datasets)


def setup_tokenizer(model_name: str, template_name: str, max_length: int):
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True, use_fast=True)
    tokenizer.padding_side = "right"
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    if template_name == "gemma":
        tokenizer.add_special_tokens({"additional_special_tokens": ["<end_of_turn>"]})
    tokenizer.model_max_length = max_length
    return tokenizer


def resolve_precision(args: argparse.Namespace) -> Tuple[torch.dtype, bool, bool]:
    cuda_available = torch.cuda.is_available()
    bf16_supported = cuda_available and torch.cuda.is_bf16_supported()
    if args.bf16 and bf16_supported:
        return torch.bfloat16, True, False
    if args.bf16 and not bf16_supported:
        LOGGER.warning("BF16 requested but not supported; falling back to FP16 if CUDA is available.")
    if args.fp16 and cuda_available:
        return torch.float16, False, True
    if bf16_supported:
        return torch.bfloat16, True, False
    if cuda_available:
        return torch.float16, False, True
    return torch.float32, False, False


def setup_model(args: argparse.Namespace, tokenizer):
    compute_dtype, use_bf16, use_fp16 = resolve_precision(args)
    kwargs: Dict[str, Any] = {
        "device_map": "auto",
        "trust_remote_code": True,
        "torch_dtype": compute_dtype,
    }
    if args.qlora:
        kwargs["quantization_config"] = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=compute_dtype,
            bnb_4bit_use_double_quant=True,
        )
    model = AutoModelForCausalLM.from_pretrained(args.model_name, **kwargs)
    model.config.use_cache = False
    embedding_count = int(getattr(model.get_input_embeddings(), "num_embeddings", 0) or 0)
    tokenizer_length = len(tokenizer)
    if embedding_count and tokenizer_length > embedding_count:
        LOGGER.info("Resizing token embeddings from %s to %s.", embedding_count, tokenizer_length)
        model.resize_token_embeddings(tokenizer_length)
    elif embedding_count and tokenizer_length < embedding_count:
        LOGGER.info(
            "Keeping model token embeddings at %s; tokenizer length is %s.",
            embedding_count,
            tokenizer_length,
        )
    if args.qlora and args.gradient_checkpointing:
        model = prepare_model_for_kbit_training(model, use_gradient_checkpointing=True)
    elif args.qlora:
        model = prepare_model_for_kbit_training(model, use_gradient_checkpointing=False)
    elif args.gradient_checkpointing:
        model.gradient_checkpointing_enable(gradient_checkpointing_kwargs={"use_reentrant": False})
        if hasattr(model, "enable_input_require_grads"):
            model.enable_input_require_grads()
    return model, use_bf16, use_fp16


def resolve_target_modules(model) -> List[str]:
    module_names = [name for name, _ in model.named_modules()]
    detected = [
        candidate
        for candidate in DEFAULT_TARGET_MODULES
        if any(name.endswith(candidate) for name in module_names)
    ]
    if detected:
        return detected

    linear_like: List[str] = []
    for name, module in model.named_modules():
        if isinstance(module, torch.nn.Linear):
            leaf = name.split(".")[-1]
            if leaf not in linear_like:
                linear_like.append(leaf)
    if linear_like:
        LOGGER.warning("Default LoRA targets missing; auto-detected linear modules: %s", linear_like)
        return linear_like
    raise ValueError("Could not detect LoRA target modules for this model.")


def build_lora_config(args: argparse.Namespace, target_modules: List[str]) -> LoraConfig:
    return LoraConfig(
        task_type=TaskType.CAUSAL_LM,
        r=args.lora_r,
        lora_alpha=args.lora_alpha,
        lora_dropout=args.lora_dropout,
        bias="none",
        target_modules=target_modules,
        inference_mode=False,
    )


def find_subsequence(haystack: Sequence[int], needle: Sequence[int]) -> bool:
    if not needle or len(needle) > len(haystack):
        return False
    for idx in range(len(haystack) - len(needle) + 1):
        if list(haystack[idx : idx + len(needle)]) == list(needle):
            return True
    return False


def response_template_candidates(tokenizer, template_name: str) -> List[List[int]]:
    template = TEMPLATES[template_name]["response_template"]
    variants = [template, template.strip(), f" {template.strip()}", f"{template.strip()} "]
    candidates: List[List[int]] = []
    seen = set()
    for variant in variants:
        prefix_ids = tokenizer.encode("X", add_special_tokens=False)
        probe_ids = tokenizer.encode("X" + variant, add_special_tokens=False)
        ids = probe_ids[len(prefix_ids) :] if probe_ids[: len(prefix_ids)] == prefix_ids else tokenizer.encode(variant, add_special_tokens=False)
        key = tuple(ids)
        if ids and key not in seen:
            candidates.append(ids)
            seen.add(key)
    return candidates


def pick_response_template_ids(dataset: Dataset, tokenizer, template_name: str, max_length: int) -> List[int]:
    best_ids: List[int] = []
    best_hits = -1
    for candidate in response_template_candidates(tokenizer, template_name):
        hits = 0
        for row in dataset:
            input_ids = tokenizer(
                str(row["text"]),
                add_special_tokens=True,
                truncation=True,
                max_length=max_length,
            )["input_ids"]
            if find_subsequence(input_ids, candidate):
                hits += 1
        if hits > best_hits:
            best_hits = hits
            best_ids = candidate
    if best_hits > 0:
        LOGGER.info("Assistant response marker matched %s/%s train samples.", best_hits, len(dataset))
    return best_ids if best_hits > 0 else []


def safe_data_collator(tokenizer, response_ids: List[int], template_name: str):
    if DataCollatorForCompletionOnlyLM is None:
        LOGGER.warning("DataCollatorForCompletionOnlyLM unavailable; falling back to normal SFT loss.")
        return None
    response_template: Any = response_ids or TEMPLATES[template_name]["response_template"]
    try:
        return DataCollatorForCompletionOnlyLM(
            response_template=response_template,
            tokenizer=tokenizer,
            mlm=False,
        )
    except Exception as exc:
        LOGGER.warning("Could not create assistant-only loss collator (%s); falling back to normal SFT loss.", exc)
        return None


def extract_bug_ids(text: str) -> List[str]:
    return re.findall(r"\b(?:Bug ID|Bug|BUGID)[:\s-]*(\d{5,7})\b", text, flags=re.IGNORECASE)


def extract_category(text: str) -> str:
    match = re.match(r"\s*([^(:]{2,80})\s*\(Bug ID\s+\d{5,7}\):", text)
    return normalize_text(match.group(1)).lower() if match else ""


def extract_params(text: str) -> List[str]:
    return re.findall(r"<[^>]+>", text)


def extract_cli_terms(text: str) -> set:
    lowered = text.lower()
    terms = {word for word in CLI_WORDS if word in lowered}
    terms.update(re.findall(r"\b[a-z][a-z0-9-]+(?:\s+[a-z0-9-<>]+){0,3}\b", lowered))
    return terms


def word_tokens(text: str) -> List[str]:
    return re.findall(r"[a-z0-9][a-z0-9_./-]*", normalize_text(text).lower())


def _cli_tokens_from_fragment(fragment: str) -> List[str]:
    tokens = [token for token in word_tokens(fragment) if token not in CLI_FILLER]
    if not tokens:
        return []
    if tokens[0] not in COMMAND_PREFIXES and not any(token in COMMAND_PREFIXES for token in tokens[:3]):
        return []
    return tokens[:12]


def reference_cli_fragments(question: str, reference: str) -> List[str]:
    fragments: List[str] = []
    text = normalize_text(reference, preserve_newlines=True)
    fragments.extend(re.findall(r"`([^`]+)`", text))
    for line in text.splitlines():
        if re.search(r"(?i)\bsyntax\b", line) or re.match(
            r"\s*(show|clear|configure|copy|crypto|interface|ip|ipv6|no|policy|router|vlan)\b",
            line,
            re.I,
        ):
            fragments.append(line)
    if not fragments and re.search(r"(?i)\b(?:syntax|command)\b", question):
        fragments.append(question)
    return fragments


def extract_reference_cli_tokens(question: str, reference: str) -> List[str]:
    required: List[str] = []
    for fragment in reference_cli_fragments(question, reference):
        fragment = re.sub(r"(?i)^.*?\bsyntax\s*(?:of\b.*?\bis)?\s*[:=-]?\s*", "", fragment)
        tokens = _cli_tokens_from_fragment(fragment)
        for token in tokens:
            if token not in required:
                required.append(token)
    return required


def contains_token_sequence(tokens: Sequence[str], needle: Sequence[str]) -> bool:
    if not needle:
        return True
    if len(needle) > len(tokens):
        return False
    for idx in range(0, len(tokens) - len(needle) + 1):
        if list(tokens[idx : idx + len(needle)]) == list(needle):
            return True
    return False


def extract_reference_cli_base_command(question: str, reference: str, row: Optional[Dict[str, Any]] = None) -> str:
    if row:
        command = command_value(row)
        if command:
            return command.lower()
    text = f"{question}\n{reference}"
    match = re.search(
        r"\b((?:show|clear|configure|copy|crypto|interface|ip|ipv6|no|policy|router|vlan)"
        r"(?:\s+[a-z0-9][a-z0-9_./-]*){0,5})\s+command\b",
        normalize_text(text).lower(),
    )
    if match:
        return match.group(1)
    for fragment in reference_cli_fragments(question, reference):
        fragment = re.sub(r"(?i)^.*?\bsyntax\s*(?:of\b.*?\bis)?\s*[:=-]?\s*", "", fragment)
        tokens = re.findall(r"[a-z0-9][a-z0-9_./-]*|[\[\]<>{}]", fragment.lower())
        try:
            start = next(idx for idx, token in enumerate(tokens) if token in COMMAND_PREFIXES)
        except StopIteration:
            continue
        base: List[str] = []
        for token in tokens[start:]:
            if token in {"[", "<", "{", "]", ">", "}"}:
                break
            if token in CLI_FILLER:
                continue
            base.append(token)
            if len(base) >= 6:
                break
        if base:
            return " ".join(base)
    required = extract_reference_cli_tokens(question, reference)
    if required and required[0] in COMMAND_PREFIXES:
        return " ".join(required[: min(3, len(required))])
    return ""


def is_cli_related_row(family: str, question: str, reference: str, required_cli_tokens: Sequence[str]) -> bool:
    family = normalize_text(family).lower()
    q = normalize_text(question).lower()
    if family in CLI_DATA_FAMILIES:
        return True
    if any(phrase in q for phrase in CLI_QUESTION_PHRASES):
        return True
    if "syntax" in q and "command" in q:
        return True
    return bool(required_cli_tokens and any(token in COMMAND_PREFIXES for token in required_cli_tokens[:3]))


def extract_cli_command_spans(text: str) -> List[List[str]]:
    normalized = normalize_text(text, preserve_newlines=True)
    fragments: List[str] = []
    fragments.extend(re.findall(r"`([^`]+)`", normalized))
    for match in re.finditer(
        r"(?im)(?:^|[:\n])\s*((?:show|clear|configure|copy|crypto|interface|ip|ipv6|no|policy|router|vlan)\b[^\n`.;]*)",
        normalized,
    ):
        fragments.append(match.group(1))

    spans: List[List[str]] = []
    seen: Set[Tuple[str, ...]] = set()
    for fragment in fragments:
        tokens = _cli_tokens_from_fragment(fragment)
        if not tokens:
            continue
        if tokens[0] == "no" and (len(tokens) == 1 or tokens[1] in {"known", "specific", "workaround", "workarounds", "issue", "issues"}):
            continue
        key = tuple(tokens)
        if key not in seen:
            seen.add(key)
            spans.append(tokens)
    return spans


def unsupported_extra_cli(
    pred_cli_spans: Sequence[Sequence[str]],
    required_cli_tokens: Sequence[str],
    base_tokens: Sequence[str],
) -> Tuple[bool, List[str]]:
    allowed = set(required_cli_tokens) | set(base_tokens)
    reasons: List[str] = []
    for span in pred_cli_spans:
        tokens = list(span)
        if not tokens:
            continue
        if base_tokens and not contains_token_sequence(tokens, base_tokens):
            same_family = (
                len(tokens) > 1
                and len(base_tokens) > 1
                and tokens[0] == base_tokens[0]
                and tokens[1] == base_tokens[1]
            )
            if not same_family:
                reasons.append("different_command:" + " ".join(tokens[:4]))
        extras = [
            token
            for token in tokens
            if token not in allowed
            and token not in CLI_FILLER
            and not re.fullmatch(r"\d+", token)
        ]
        if extras:
            reasons.append("unsupported_tokens:" + ",".join(extras[:6]))
    deduped: List[str] = []
    for reason in reasons:
        if reason not in deduped:
            deduped.append(reason)
    return bool(deduped), deduped[:8]


def erps_acronym_hallucination(question: str, reference: str, prediction: str) -> bool:
    context = f"{question}\n{reference}".lower()
    pred = normalize_text(prediction).lower()
    if "erps" not in context or "erps" not in pred:
        return False
    return any(expansion in pred for expansion in BAD_ERPS_EXPANSIONS)


def mean(values: List[float]) -> float:
    return float(np.mean(values)) if values else 0.0


def keyword_overlap(prediction: str, reference: str) -> float:
    ref_terms = {term.lower() for term in re.findall(r"\b[A-Za-z][A-Za-z0-9_-]{2,}\b", reference)}
    pred_terms = {term.lower() for term in re.findall(r"\b[A-Za-z][A-Za-z0-9_-]{2,}\b", prediction)}
    if not ref_terms:
        return 1.0
    return len(ref_terms.intersection(pred_terms)) / len(ref_terms)


def extract_event_ids(text: str) -> List[str]:
    """Return explicitly labelled Event IDs without treating arbitrary numbers as IDs."""
    found: List[str] = []
    for pattern in (
        r"(?i)\bevent\s*id\s*[:#-]?\s*(\d{3,6})\b",
        r"(?i)\beventid\s*[:#-]?\s*(\d{3,6})\b",
    ):
        for event_id in re.findall(pattern, normalize_text(text)):
            if event_id not in found:
                found.append(event_id)
    return found


def extract_normalized_dates(text: str) -> Set[str]:
    months = {
        "jan": "01", "january": "01", "feb": "02", "february": "02",
        "mar": "03", "march": "03", "apr": "04", "april": "04", "may": "05",
        "jun": "06", "june": "06", "jul": "07", "july": "07", "aug": "08",
        "august": "08", "sep": "09", "sept": "09", "september": "09",
        "oct": "10", "october": "10", "nov": "11", "november": "11",
        "dec": "12", "december": "12",
    }
    lowered = normalize_text(text).lower()
    found: Set[str] = set()
    month_names = "|".join(sorted(months, key=len, reverse=True))
    for day, month, year in re.findall(rf"\b(\d{{1,2}})\s+({month_names})\s+(20\d{{2}})\b", lowered):
        found.add(f"{year}-{months[month]}-{int(day):02d}")
    for month, day, year in re.findall(
        rf"\b({month_names})\s+(\d{{1,2}})(?:st|nd|rd|th)?[,]?\s+(20\d{{2}})\b",
        lowered,
    ):
        found.add(f"{year}-{months[month]}-{int(day):02d}")
    for year, month, day in re.findall(r"\b(20\d{2})[-/](\d{1,2})[-/](\d{1,2})\b", lowered):
        found.add(f"{year}-{int(month):02d}-{int(day):02d}")
    for day, month, year in re.findall(r"\b(\d{1,2})[-/](\d{1,2})[-/](20\d{2})\b", lowered):
        found.add(f"{year}-{int(month):02d}-{int(day):02d}")
    return found


def reference_says_no_workaround(reference: str) -> bool:
    lowered = normalize_text(reference).lower()
    return bool(
        re.search(
            r"\b(no|not any|without)\s+(known\s+|documented\s+|specific\s+)?workarounds?\b",
            lowered,
        )
        or "no workaround is documented" in lowered
        or "no workaround is available" in lowered
        or "workaround is not documented" in lowered
        or "workaround is not available" in lowered
    )


def task_analysis_for_pair(
    prediction: str,
    reference: str,
    family: str = "",
    row: Optional[Dict[str, Any]] = None,
) -> Tuple[Dict[str, float], Dict[str, Any]]:
    pred_bugs = set(extract_bug_ids(prediction))
    ref_bugs = set(extract_bug_ids(reference))
    pred_events = set(extract_event_ids(prediction))
    ref_events = set(extract_event_ids(reference))
    pred_dates = extract_normalized_dates(prediction)
    ref_dates = extract_normalized_dates(reference)
    pred_category = extract_category(prediction)
    ref_category = extract_category(reference)
    pred_params = set(extract_params(prediction))
    ref_params = set(extract_params(reference))
    question = normalize_text((row or {}).get("question", ""))
    command_name = extract_reference_cli_base_command(question, reference, row)
    required_cli_tokens = extract_reference_cli_tokens(question, reference)
    cli_row = is_cli_related_row(family, question, reference, required_cli_tokens)
    pred_tokens = word_tokens(prediction)
    pred_token_set = set(pred_tokens)
    pred_cli_spans = extract_cli_command_spans(prediction)
    ref_cli_spans = extract_cli_command_spans(reference)
    base_tokens = word_tokens(command_name)
    command_name_accuracy = (
        float(contains_token_sequence(pred_tokens, base_tokens)) if command_name else None
    )
    command_syntax_preservation = (
        len([token for token in required_cli_tokens if token in pred_token_set]) / len(required_cli_tokens)
        if required_cli_tokens
        else None
    )
    wrong_cli_syntax = bool(cli_row and required_cli_tokens and command_syntax_preservation < 1.0)
    raw_unsupported_extra_cli, unsupported_extra_cli_reasons = unsupported_extra_cli(
        pred_cli_spans,
        required_cli_tokens,
        base_tokens,
    )
    unsupported_extra_cli_flag = bool(cli_row and raw_unsupported_extra_cli)
    non_cli_invented_cli = bool(not cli_row and pred_cli_spans and not ref_cli_spans and not required_cli_tokens)
    cli_hallucination_rate = float((cli_row and unsupported_extra_cli_flag) or non_cli_invented_cli)
    acronym_bad = erps_acronym_hallucination(question, reference, prediction)

    bug_row = bool(ref_bugs) or family == "release_notes_bug"
    event_row = bool(ref_events) or family == "event_log_reference"
    bug_id_accuracy = float(bool(ref_bugs.intersection(pred_bugs))) if ref_bugs else None
    event_id_accuracy = float(bool(ref_events.intersection(pred_events))) if ref_events else None
    date_preservation = float(ref_dates.issubset(pred_dates)) if ref_dates else None
    fake_bug_rate = float(bool(pred_bugs - ref_bugs)) if bug_row else None
    fake_event_rate = float(bool(pred_events - ref_events)) if event_row else None
    category_accuracy = float(ref_category in prediction.lower()) if ref_category else None
    parameter_preservation = (
        len(pred_params.intersection(ref_params)) / len(ref_params) if ref_params else None
    )
    no_workaround_row = reference_says_no_workaround(reference)
    workaround_hallucinated = bool(
        no_workaround_row
        and "workaround" in prediction.lower()
        and not reference_says_no_workaround(prediction)
    )
    length_ratio = min(len(prediction.split()), len(reference.split())) / max(len(prediction.split()), len(reference.split()), 1)

    metrics = {
        "bug_id_accuracy": bug_id_accuracy,
        "event_id_accuracy": event_id_accuracy,
        "date_preservation": date_preservation,
        "category_accuracy": category_accuracy,
        "answer_prefix_accuracy": float(bool(re.match(r"^[^:]+ \(Bug ID \d{5,7}\):", prediction))),
        "fake_bug_rate": fake_bug_rate,
        "no_fake_bug_rate": None if fake_bug_rate is None else 1.0 - fake_bug_rate,
        "fake_event_rate": fake_event_rate,
        "no_fake_event_rate": None if fake_event_rate is None else 1.0 - fake_event_rate,
        "no_workaround_hallucination_rate": (
            0.0 if workaround_hallucinated else 1.0
        ) if no_workaround_row else None,
        "switch_version_consistency": 1.0,
        "section_prefix_accuracy": float(":" in prediction[:80]),
        "section_consistency": keyword_overlap(prediction[:120], reference[:120]),
        "hallucinated_bug_rate": float(bool(pred_bugs and not ref_bugs)),
        "command_syntax_preservation": command_syntax_preservation,
        "command_name_accuracy": command_name_accuracy,
        "wrong_cli_syntax_rate": float(wrong_cli_syntax) if required_cli_tokens else None,
        "unsupported_extra_cli_rate": float(unsupported_extra_cli_flag) if cli_row else None,
        "parameter_preservation": parameter_preservation,
        "doc_prefix_accuracy": float(bool(re.match(r"^[A-Za-z0-9 -]+:", prediction))),
        "cli_hallucination_rate": cli_hallucination_rate if cli_row or non_cli_invented_cli else None,
        "no_cli_hallucination_rate": 1.0 - cli_hallucination_rate if cli_row or non_cli_invented_cli else None,
        "acronym_meaning_hallucination_rate": float(acronym_bad),
        "keyword_overlap": keyword_overlap(prediction, reference),
        "answer_length_reasonable": float(0.3 <= length_ratio <= 2.5),
        "source_type_accuracy": 0.0,
        "data_family_accuracy": 0.0,
    }

    if family == "release_notes_non_bug":
        metrics["answer_prefix_accuracy"] = metrics["section_prefix_accuracy"]
    if is_product_family(family) or family == "product_documentation":
        metrics["answer_prefix_accuracy"] = metrics["doc_prefix_accuracy"]
    details = {
        "prediction": prediction,
        "reference": reference,
        "family": family,
        "bug_id_applicable": bool(ref_bugs),
        "event_id_applicable": bool(ref_events),
        "date_applicable": bool(ref_dates),
        "command_name_applicable": bool(command_name),
        "cli_syntax_applicable": bool(required_cli_tokens),
        "no_workaround_applicable": bool(no_workaround_row),
        "is_cli_row": bool(cli_row),
        "reference_cli_base_command": command_name,
        "required_cli_tokens": required_cli_tokens,
        "missing_cli_tokens": [token for token in required_cli_tokens if token not in pred_token_set],
        "predicted_cli_spans": [" ".join(span) for span in pred_cli_spans],
        "wrong_cli_syntax": bool(wrong_cli_syntax),
        "unsupported_extra_cli": bool(unsupported_extra_cli_flag),
        "unsupported_extra_cli_reasons": unsupported_extra_cli_reasons if unsupported_extra_cli_flag else [],
        "cli_hallucination": bool(cli_hallucination_rate),
        "acronym_meaning_hallucination": bool(acronym_bad),
    }
    return metrics, details


def task_metrics_for_pair(prediction: str, reference: str, family: str = "", row: Optional[Dict[str, Any]] = None) -> Dict[str, Optional[float]]:
    metrics, _ = task_analysis_for_pair(prediction, reference, family, row)
    return metrics


def aggregate_metric_dicts(items: List[Dict[str, Optional[float]]]) -> Dict[str, float]:
    keys = sorted({key for item in items for key in item})
    aggregated: Dict[str, float] = {}
    for key in keys:
        values = [float(item[key]) for item in items if item.get(key) is not None]
        if not values:
            continue
        aggregated[key] = round(mean(values), 4)
        aggregated[f"{key}_applicable_rows"] = len(values)
    return aggregated


def finite_or_none(value: Any) -> Optional[float]:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    return number if math.isfinite(number) else None


def is_nan_or_inf(value: Any) -> bool:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return str(value).strip().lower() in {"nan", "inf", "-inf", "infinity", "-infinity"}
    return not math.isfinite(number)


class NaNStoppingCallback(TrainerCallback):
    def __init__(self, output_dir: str):
        self.output_dir = Path(output_dir)
        self.stopped_due_to_nan = False
        self.last_loss: Optional[float] = None
        self.last_grad_norm: Optional[float] = None
        self.nan_payload: Dict[str, Any] = {}

    def on_log(self, args, state, control, logs=None, **kwargs):
        logs = logs or {}
        if "loss" in logs and finite_or_none(logs.get("loss")) is not None:
            self.last_loss = float(logs["loss"])
        if "grad_norm" in logs and finite_or_none(logs.get("grad_norm")) is not None:
            self.last_grad_norm = float(logs["grad_norm"])

        loss_bad = "loss" in logs and is_nan_or_inf(logs.get("loss"))
        grad_bad = "grad_norm" in logs and is_nan_or_inf(logs.get("grad_norm"))
        if loss_bad or grad_bad:
            self.stopped_due_to_nan = True
            self.nan_payload = {
                "stopped_due_to_nan": True,
                "step": int(getattr(state, "global_step", 0) or 0),
                "loss": str(logs.get("loss", "")),
                "grad_norm": str(logs.get("grad_norm", "")),
                "recommendation": "Lower learning rate, reduce max_length, check dataset, use max_grad_norm.",
            }
            print(f"WARNING: stopping training due to NaN/Inf metrics: {self.nan_payload}")
            save_json(self.output_dir / "nan_failure_report.json", self.nan_payload)
            control.should_training_stop = True
        return control


def parse_checkpoint_steps(value: str) -> Tuple[int, ...]:
    if not str(value or "").strip():
        return ()
    parsed: List[int] = []
    for item in str(value).split(","):
        item = item.strip()
        if not item:
            continue
        try:
            step = int(item)
        except ValueError as exc:
            raise ValueError(f"Invalid checkpoint step {item!r}; expected positive integers separated by commas.") from exc
        if step <= 0:
            raise ValueError(f"Checkpoint steps must be positive, got {step}.")
        if step not in parsed:
            parsed.append(step)
    return tuple(sorted(parsed))


class ExactCheckpointCallback(TrainerCallback):
    """Request saves only at explicitly approved optimizer steps."""

    def __init__(self, checkpoint_steps: Sequence[int]):
        self.checkpoint_steps = frozenset(int(step) for step in checkpoint_steps)

    def on_step_end(self, args, state, control, **kwargs):
        if int(getattr(state, "global_step", 0) or 0) in self.checkpoint_steps:
            control.should_save = True
        return control


def compute_metrics_fn(tokenizer) -> Callable:
    rouge_metric = evaluate.load("rouge")
    bleu_metric = evaluate.load("bleu")

    def compute_metrics(eval_pred):
        global LAST_EVAL_REVIEWS
        logits, labels = eval_pred
        if isinstance(logits, (tuple, list)):
            logits = logits[0]
        pred_ids = logits if getattr(logits, "ndim", 0) == getattr(labels, "ndim", -1) else np.argmax(logits, axis=-1)
        pred_ids, aligned_labels = align_causal_predictions(pred_ids, labels)
        answer_mask = aligned_labels != -100
        pred_ids = np.where(answer_mask, pred_ids, tokenizer.pad_token_id)
        pred_ids = np.where(pred_ids < 0, tokenizer.pad_token_id, pred_ids)
        preds = tokenizer.batch_decode(pred_ids, skip_special_tokens=True)
        labels_for_decode = np.where(answer_mask, aligned_labels, tokenizer.pad_token_id)
        refs = tokenizer.batch_decode(labels_for_decode, skip_special_tokens=True)

        rouge_l = rouge_metric.compute(predictions=preds, references=refs, use_stemmer=True)["rougeL"]
        bleu = bleu_metric.compute(predictions=preds, references=[[ref] for ref in refs])["bleu"]
        exact = mean([float(pred.strip() == ref.strip()) for pred, ref in zip(preds, refs)])
        analyses = [task_analysis_for_pair(pred, ref) for pred, ref in zip(preds, refs)]
        task = {
            f"teacher_forced_{key}": value
            for key, value in aggregate_metric_dicts([metrics for metrics, _ in analyses]).items()
        }
        LAST_EVAL_REVIEWS = [details for _, details in analyses]
        return {
            "teacher_forced_rouge_l": round(float(rouge_l), 4),
            "teacher_forced_bleu": round(float(bleu), 4),
            "teacher_forced_exact_match": round(float(exact), 4),
            **task,
        }

    return compute_metrics


def align_causal_predictions(pred_ids: np.ndarray, labels: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """Align token-t predictions with token-(t+1) causal-LM labels."""
    pred_array = np.asarray(pred_ids)
    label_array = np.asarray(labels)
    if pred_array.ndim != 2 or label_array.ndim != 2:
        raise ValueError(
            f"Expected 2-D causal token arrays, got predictions={pred_array.shape}, labels={label_array.shape}"
        )
    if pred_array.shape != label_array.shape:
        raise ValueError(
            f"Causal token arrays must have identical shapes, got {pred_array.shape} and {label_array.shape}"
        )
    if pred_array.shape[1] < 2:
        return pred_array[:, :0], label_array[:, :0]
    return pred_array[:, :-1], label_array[:, 1:]


def preprocess_logits_for_metrics(logits, labels):
    if isinstance(logits, (tuple, list)):
        logits = logits[0]
    return torch.argmax(logits, dim=-1)


def build_training_arguments_kwargs(args: argparse.Namespace, use_bf16: bool, use_fp16: bool) -> Dict[str, Any]:
    effective_eval_steps = args.eval_steps or max(args.logging_steps, 200)
    effective_save_steps = args.save_steps or effective_eval_steps
    checkpoint_steps = parse_checkpoint_steps(args.checkpoint_steps)
    max_steps = args.sanity_steps if args.sanity_steps is not None else args.max_steps
    kwargs: Dict[str, Any] = {
        "output_dir": args.output_dir,
        "num_train_epochs": args.epochs,
        "max_steps": max_steps,
        "per_device_train_batch_size": args.batch_size,
        "per_device_eval_batch_size": 1,
        "gradient_accumulation_steps": args.grad_accum,
        "learning_rate": args.lr,
        "lr_scheduler_type": "cosine",
        "warmup_ratio": args.warmup_ratio,
        "weight_decay": args.weight_decay,
        "max_grad_norm": args.max_grad_norm,
        "optim": args.optim,
        "bf16": use_bf16,
        "fp16": use_fp16 and not use_bf16,
        "logging_steps": args.logging_steps,
        "eval_strategy": "steps" if args.teacher_eval_during_training else "no",
        "save_strategy": "no" if checkpoint_steps else "steps",
        "eval_steps": effective_eval_steps if args.teacher_eval_during_training else None,
        "save_steps": effective_save_steps if not checkpoint_steps else None,
        "eval_accumulation_steps": 1,
        "save_total_limit": args.save_total_limit,
        "load_best_model_at_end": args.select_best_by_eval_loss,
        "metric_for_best_model": "eval_loss" if args.select_best_by_eval_loss else None,
        "greater_is_better": False if args.select_best_by_eval_loss else None,
        "report_to": "wandb" if args.use_wandb else "none",
        "run_name": args.run_name,
        "seed": args.seed,
        "gradient_checkpointing": args.gradient_checkpointing,
        "gradient_checkpointing_kwargs": {"use_reentrant": False},
        "dataloader_num_workers": 0,
        "dataloader_pin_memory": torch.cuda.is_available(),
        "group_by_length": True,
        "packing": False,
        "save_safetensors": True,
    }
    if args.eval_only:
        kwargs.update(
            {
                "do_train": False,
                "do_eval": True,
                "eval_strategy": "no",
                "save_strategy": "no",
                "load_best_model_at_end": False,
                "gradient_checkpointing": False,
                "group_by_length": False,
            }
        )
    return compatible_training_args(kwargs)


def compatible_training_args(kwargs: Dict[str, Any]) -> Dict[str, Any]:
    cleaned = {key: value for key, value in kwargs.items() if value is not None}
    while True:
        try:
            TrainingArguments(**cleaned)
            return cleaned
        except TypeError as exc:
            message = str(exc)
            marker = "unexpected keyword argument '"
            if marker not in message:
                raise
            bad_key = message.split(marker, 1)[1].split("'", 1)[0]
            if bad_key == "eval_strategy" and "eval_strategy" in cleaned:
                cleaned["evaluation_strategy"] = cleaned.pop("eval_strategy")
                continue
            cleaned.pop(bad_key, None)


def build_trainer(
    model,
    tokenizer,
    training_args: TrainingArguments,
    datasets: DatasetDict,
    data_collator,
    args: argparse.Namespace,
    sample_weights: Optional[Sequence[float]] = None,
):
    callbacks = []
    nan_callback = None
    if args.stop_on_nan and not args.eval_only:
        nan_callback = NaNStoppingCallback(args.output_dir)
        callbacks.append(nan_callback)
    checkpoint_steps = parse_checkpoint_steps(args.checkpoint_steps)
    if checkpoint_steps and not args.eval_only:
        callbacks.append(ExactCheckpointCallback(checkpoint_steps))
    if (
        args.select_best_by_eval_loss
        and args.early_stopping_patience
        and args.early_stopping_patience > 0
        and not args.eval_only
    ):
        callbacks.append(EarlyStoppingCallback(early_stopping_patience=args.early_stopping_patience))
    kwargs = {
        "model": model,
        "tokenizer": tokenizer,
        "args": training_args,
        "train_dataset": datasets["train"],
        "eval_dataset": (
            {"validation": datasets["validation"], "test": datasets["test"]}
            if "test" in datasets
            else datasets["validation"]
        ),
        "dataset_text_field": "text",
        "data_collator": data_collator,
        "max_seq_length": args.max_length,
        "packing": args.packing,
        "compute_metrics": compute_metrics_fn(tokenizer),
        "preprocess_logits_for_metrics": preprocess_logits_for_metrics,
        "callbacks": callbacks,
    }
    if sample_weights is not None:
        kwargs["sample_weights"] = list(sample_weights)
    if data_collator is None:
        kwargs.pop("data_collator")

    trainer_class = WeightedSFTTrainer if sample_weights is not None else SFTTrainer
    while True:
        try:
            return trainer_class(**kwargs)
        except TypeError as exc:
            message = str(exc)
            marker = "unexpected keyword argument '"
            if marker not in message:
                raise
            bad_key = message.split(marker, 1)[1].split("'", 1)[0]
            if bad_key == "tokenizer":
                kwargs["processing_class"] = kwargs.pop("tokenizer")
                continue
            kwargs.pop(bad_key, None)


class WeightedSFTTrainer(SFTTrainer):
    def __init__(self, *args, sample_weights: Optional[Sequence[float]] = None, **kwargs):
        self.sample_weights = None if sample_weights is None else torch.as_tensor(list(sample_weights), dtype=torch.double)
        super().__init__(*args, **kwargs)

    def get_train_dataloader(self):
        if self.sample_weights is None:
            return super().get_train_dataloader()
        if self.train_dataset is None:
            return super().get_train_dataloader()
        if len(self.sample_weights) != len(self.train_dataset):
            raise ValueError(
                f"Sample-weight count ({len(self.sample_weights)}) does not match train dataset size ({len(self.train_dataset)})."
            )
        original_get_train_sampler = self._get_train_sampler

        def _weighted_sampler(dataset):
            return WeightedRandomSampler(
                weights=self.sample_weights,
                num_samples=len(self.sample_weights),
                replacement=True,
            )

        try:
            self._get_train_sampler = _weighted_sampler  # type: ignore[method-assign]
            return super().get_train_dataloader()
        finally:
            self._get_train_sampler = original_get_train_sampler  # type: ignore[method-assign]


def metrics_by_family_from_references(dataset: Dataset) -> Dict[str, Dict[str, float]]:
    grouped: Dict[str, List[Dict[str, float]]] = {}
    for row in dataset:
        family = row.get("data_family") or "unknown"
        grouped.setdefault(family, []).append(
            task_metrics_for_pair(row.get("reference_answer", ""), row.get("reference_answer", ""), family, row)
        )
    return {family: aggregate_metric_dicts(items) for family, items in grouped.items()}


def save_json(path: Path, payload: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, ensure_ascii=False)


def compact_text(text: str, limit: int = 240) -> str:
    compact = re.sub(r"\s+", " ", normalize_text(text))
    if len(compact) > limit:
        return compact[: limit - 3] + "..."
    return compact


def select_eval_examples(kind: str, limit: int = 5) -> List[Dict[str, Any]]:
    if kind == "wrong_cli_syntax":
        rows = [row for row in LAST_EVAL_REVIEWS if row["wrong_cli_syntax"]]
    elif kind == "real_cli_hallucination":
        rows = [row for row in LAST_EVAL_REVIEWS if row["cli_hallucination"]]
    elif kind == "non_hallucinated_cli":
        rows = [
            row
            for row in LAST_EVAL_REVIEWS
            if row["is_cli_row"] and row["predicted_cli_spans"] and not row["cli_hallucination"]
        ]
    else:
        rows = []
    return rows[:limit]


def write_corrected_eval_report(output_dir: Path, eval_metrics: Dict[str, Any], args: argparse.Namespace) -> None:
    old_metrics_path = output_dir / "eval_metrics.json"
    old_metrics: Dict[str, Any] = {}
    if old_metrics_path.exists():
        old_metrics = json.loads(old_metrics_path.read_text(encoding="utf-8"))

    examples = {
        "wrong_cli_syntax": select_eval_examples("wrong_cli_syntax"),
        "real_cli_hallucination": select_eval_examples("real_cli_hallucination"),
        "non_hallucinated_cli": select_eval_examples("non_hallucinated_cli"),
    }
    payload = {
        "adapter_path": args.adapter_path,
        "model_name": args.model_name,
        "val_data_path": args.val_data_path,
        "old_eval_cli_hallucination_rate": old_metrics.get("eval_cli_hallucination_rate"),
        "new_eval_cli_hallucination_rate": eval_metrics.get("eval_cli_hallucination_rate"),
        "corrected_eval_metrics": eval_metrics,
        "examples": examples,
    }
    save_json(output_dir / "corrected_eval_report.json", payload)

    def metric(name: str) -> Any:
        return eval_metrics.get(name, "n/a")

    lines = [
        "# Corrected Eval Report",
        "",
        "Evaluation-only run on the already trained adapter. No training was run.",
        "",
        "## Metrics",
        "",
        f"- Old eval_cli_hallucination_rate: {old_metrics.get('eval_cli_hallucination_rate', 'n/a')}",
        f"- New eval_cli_hallucination_rate: {metric('eval_cli_hallucination_rate')}",
        f"- eval_wrong_cli_syntax_rate: {metric('eval_wrong_cli_syntax_rate')}",
        f"- eval_unsupported_extra_cli_rate: {metric('eval_unsupported_extra_cli_rate')}",
        f"- eval_acronym_meaning_hallucination_rate: {metric('eval_acronym_meaning_hallucination_rate')}",
        f"- eval_command_syntax_preservation: {metric('eval_command_syntax_preservation')}",
        "",
    ]

    for title, key in (
        ("5 Examples Of Wrong CLI Syntax", "wrong_cli_syntax"),
        ("5 Examples Of Real CLI Hallucination", "real_cli_hallucination"),
        ("5 Examples Of CLI Answers That Are Not Hallucinations", "non_hallucinated_cli"),
    ):
        lines.extend([f"## {title}", ""])
        selected = examples[key]
        if not selected:
            lines.append("- none")
            lines.append("")
            continue
        for row in selected:
            lines.append(f"- Reference: {compact_text(row['reference'])}")
            lines.append(f"  Prediction: {compact_text(row['prediction'])}")
            if row["missing_cli_tokens"]:
                lines.append(f"  Missing CLI tokens: {', '.join(row['missing_cli_tokens'])}")
            if row["unsupported_extra_cli_reasons"]:
                lines.append(f"  Unsupported CLI reasons: {', '.join(row['unsupported_extra_cli_reasons'])}")
            if row["acronym_meaning_hallucination"]:
                lines.append("  ERPS acronym meaning hallucination: true")
        lines.append("")

    (output_dir / "corrected_eval_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


CORRUPTED_GENERATION_MARKERS = (
    "ly i are given as theef prouba",
    "q:the: hpe uba product",
    "q:the:",
    "theef prouba",
    "<|im_start|>user",
)


def inference_output_dir_for(output_dir: Path) -> Path:
    return Path("outputs_inference") / output_dir.name


def load_existing_trainer_eval_metrics(output_dir: Path) -> Dict[str, Any]:
    for path in (output_dir / "eval_metrics.json", output_dir / "corrected_eval_report.json"):
        if not path.exists():
            continue
        payload = json.loads(path.read_text(encoding="utf-8"))
        if "corrected_eval_metrics" in payload:
            payload = payload["corrected_eval_metrics"]
        return {key: float(value) if isinstance(value, (np.floating, np.integer)) else value for key, value in payload.items()}
    return {}


def trainer_eval_loss_summary(metrics: Dict[str, Any]) -> Dict[str, Any]:
    keep = {"eval_loss", "eval_runtime", "eval_samples_per_second", "eval_steps_per_second"}
    return {key: metrics[key] for key in keep if key in metrics}


def generation_prompt_for_row(row: Dict[str, Any], tokenizer, template_name: str) -> str:
    user_content = build_user_content_with_metadata(row, row.get("question", ""))
    if hasattr(tokenizer, "apply_chat_template"):
        return tokenizer.apply_chat_template(
            [{"role": "user", "content": user_content}],
            tokenize=False,
            add_generation_prompt=True,
        )
    template = TEMPLATES[template_name]
    return f"{template['user_prefix']}{user_content}{template['user_suffix']}{template['assistant_prefix']}"


def model_input_device(model) -> torch.device:
    try:
        return next(model.parameters()).device
    except StopIteration:
        return torch.device("cuda" if torch.cuda.is_available() else "cpu")


def generate_eval_prediction(model, tokenizer, prompt: str, args: argparse.Namespace) -> str:
    old_truncation_side = getattr(tokenizer, "truncation_side", "right")
    tokenizer.truncation_side = "left"
    try:
        inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=args.max_length)
    finally:
        tokenizer.truncation_side = old_truncation_side
    inputs = inputs.to(model_input_device(model))

    eos_token_ids: List[int] = []
    if tokenizer.eos_token_id is not None:
        eos_token_ids.append(int(tokenizer.eos_token_id))
    im_end_id = tokenizer.convert_tokens_to_ids("<|im_end|>")
    if isinstance(im_end_id, int) and im_end_id >= 0 and im_end_id not in eos_token_ids:
        eos_token_ids.append(im_end_id)
    pad_token_id = tokenizer.eos_token_id if tokenizer.eos_token_id is not None else tokenizer.pad_token_id

    with torch.inference_mode():
        outputs = model.generate(
            **inputs,
            max_new_tokens=args.eval_max_new_tokens,
            do_sample=False,
            repetition_penalty=1.15,
            no_repeat_ngram_size=4,
            eos_token_id=eos_token_ids or None,
            pad_token_id=pad_token_id,
        )
    generated_ids = outputs[0][inputs["input_ids"].shape[-1] :]
    prediction = tokenizer.decode(generated_ids, skip_special_tokens=False)
    return prediction.split("<|im_end|>")[0].strip()


def generation_looks_corrupted(prediction: str) -> bool:
    text = normalize_text(prediction, preserve_newlines=True).lower()
    if any(marker in text for marker in CORRUPTED_GENERATION_MARKERS):
        return True
    return text.startswith("context:\n") or text.startswith("question:\n")


def print_generation_sanity_examples(records: Sequence[Dict[str, Any]], count: int = 5) -> None:
    print("=== First 5 generated eval predictions before scoring ===", flush=True)
    for record in records[:count]:
        print(f"--- generated prediction {record['index']} ---", flush=True)
        print(compact_text(record["prediction"], limit=500), flush=True)


def write_jsonl(path: Path, records: Sequence[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def example_score(record: Dict[str, Any]) -> float:
    metrics = record.get("generation_metrics", {})
    return (
        float(metrics.get("keyword_overlap", 0.0))
        + float(metrics.get("bug_id_accuracy", 0.0))
        + float(metrics.get("command_syntax_preservation", 0.0))
        - float(metrics.get("wrong_cli_syntax_rate", 0.0))
        - float(metrics.get("unsupported_extra_cli_rate", 0.0))
        - float(metrics.get("cli_hallucination_rate", 0.0))
    )


def selected_generation_examples(records: Sequence[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    scored = sorted(records, key=example_score, reverse=True)
    valid_cli = [
        record
        for record in records
        if record["generation_details"]["is_cli_row"]
        and record["generation_details"]["predicted_cli_spans"]
        and not record["generation_details"]["wrong_cli_syntax"]
        and not record["generation_details"]["unsupported_extra_cli"]
        and not record["generation_details"]["cli_hallucination"]
    ]
    real_cli_hallucinations = [record for record in records if record["generation_details"]["cli_hallucination"]]
    return {
        "best_generated_predictions": scored[:5],
        "worst_generated_predictions": list(reversed(scored[-5:])),
        "valid_non_hallucinated_cli_examples": valid_cli[:5],
        "real_cli_hallucination_examples": real_cli_hallucinations[:5],
    }


def write_generation_broken_report(
    output_dir: Path,
    predictions_path: Path,
    records: Sequence[Dict[str, Any]],
    broken_records: Sequence[Dict[str, Any]],
    args: argparse.Namespace,
) -> None:
    payload = {
        "status": "broken",
        "reason": "Generated predictions contained corrupted prompt/logit fragments before scoring.",
        "adapter_path": args.adapter_path,
        "model_name": args.model_name,
        "val_data_path": args.val_data_path,
        "predictions_path": str(predictions_path),
        "generation_samples": len(records),
        "broken_examples": list(broken_records[:5]),
    }
    save_json(output_dir / "corrected_generation_eval_report.json", payload)
    lines = [
        "# Corrected Generation Eval Report",
        "",
        "Status: broken before scoring.",
        "",
        "Generated predictions contained corrupted prompt/logit fragments, so scoring was stopped.",
        "",
        f"Predictions JSONL: {predictions_path}",
        "",
        "## Broken Examples",
        "",
    ]
    for record in broken_records[:5]:
        lines.append(f"- Row {record['index']}: {compact_text(record['prediction'], 500)}")
    (output_dir / "corrected_generation_eval_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_generation_eval_report(
    output_dir: Path,
    predictions_path: Path,
    trainer_eval_metrics: Dict[str, Any],
    generation_metrics: Dict[str, Any],
    examples: Dict[str, List[Dict[str, Any]]],
    args: argparse.Namespace,
) -> None:
    payload = {
        "status": "ok",
        "adapter_path": args.adapter_path,
        "model_name": args.model_name,
        "val_data_path": args.val_data_path,
        "predictions_path": str(predictions_path),
        "trainer_eval_metrics_source": str(output_dir / "eval_metrics.json"),
        "eval_loss_from_trainer": trainer_eval_metrics.get("eval_loss"),
        "eval_runtime_from_trainer": trainer_eval_metrics.get("eval_runtime"),
        "eval_samples_per_second_from_trainer": trainer_eval_metrics.get("eval_samples_per_second"),
        "generation_metrics": generation_metrics,
        "examples": examples,
    }
    save_json(output_dir / "corrected_generation_eval_report.json", payload)

    def metric(name: str) -> Any:
        return generation_metrics.get(name, "n/a")

    def add_examples(lines: List[str], title: str, rows: Sequence[Dict[str, Any]]) -> None:
        lines.extend([f"## {title}", ""])
        if not rows:
            lines.extend(["- none", ""])
            return
        for row in rows:
            details = row["generation_details"]
            lines.append(f"- Row {row['index']}")
            lines.append(f"  Question: {compact_text(row['question'], 220)}")
            lines.append(f"  Reference: {compact_text(row['reference'], 260)}")
            lines.append(f"  Prediction: {compact_text(row['prediction'], 260)}")
            if details["missing_cli_tokens"]:
                lines.append(f"  Missing CLI tokens: {', '.join(details['missing_cli_tokens'])}")
            if details["unsupported_extra_cli_reasons"]:
                lines.append(f"  Unsupported CLI reasons: {', '.join(details['unsupported_extra_cli_reasons'])}")
        lines.append("")

    lines = [
        "# Corrected Generation Eval Report",
        "",
        "Evaluation-only generation run on the already trained adapter. No training was run.",
        "",
        f"Predictions JSONL: {predictions_path}",
        "",
        "## Metrics",
        "",
        f"- eval_loss from Trainer: {trainer_eval_metrics.get('eval_loss', 'n/a')}",
        f"- generation_rouge_l: {metric('generation_rouge_l')}",
        f"- generation_bleu: {metric('generation_bleu')}",
        f"- generation_keyword_overlap: {metric('generation_keyword_overlap')}",
        f"- generation_bug_id_accuracy: {metric('generation_bug_id_accuracy')}",
        f"- generation_command_syntax_preservation: {metric('generation_command_syntax_preservation')}",
        f"- generation_wrong_cli_syntax_rate: {metric('generation_wrong_cli_syntax_rate')}",
        f"- generation_unsupported_extra_cli_rate: {metric('generation_unsupported_extra_cli_rate')}",
        f"- generation_cli_hallucination_rate: {metric('generation_cli_hallucination_rate')}",
        f"- generation_acronym_meaning_hallucination_rate: {metric('generation_acronym_meaning_hallucination_rate')}",
        "",
    ]
    add_examples(lines, "5 Best Generated Predictions", examples["best_generated_predictions"])
    add_examples(lines, "5 Worst Generated Predictions", examples["worst_generated_predictions"])
    add_examples(lines, "5 Valid Non-Hallucinated CLI Examples", examples["valid_non_hallucinated_cli_examples"])
    add_examples(lines, "5 Real CLI Hallucination Examples", examples["real_cli_hallucination_examples"])
    (output_dir / "corrected_generation_eval_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def select_generation_eval_dataset(dataset: Dataset, limit: Optional[int]) -> Dataset:
    if not limit or limit <= 0 or len(dataset) <= limit:
        return dataset
    cli_indices: List[int] = []
    non_cli_indices: List[int] = []
    for index, row in enumerate(dataset):
        row_dict = dict(row)
        question = row_dict.get("question", "")
        reference = row_dict.get("reference_answer", "")
        required_cli_tokens = extract_reference_cli_tokens(question, reference)
        if is_cli_related_row(row_dict.get("data_family", ""), question, reference, required_cli_tokens):
            cli_indices.append(index)
        else:
            non_cli_indices.append(index)
    cli_target = min(len(cli_indices), max(20, limit // 4))
    non_cli_target = max(0, limit - cli_target)
    selected = non_cli_indices[:non_cli_target] + cli_indices[:cli_target]
    selected = selected[:limit]
    return dataset.select(selected)


def run_generation_eval(model, tokenizer, dataset: Dataset, args: argparse.Namespace, output_dir: Path) -> Dict[str, Any]:
    eval_dataset = select_generation_eval_dataset(dataset, args.eval_generation_limit)
    predictions_path = inference_output_dir_for(output_dir) / "eval_generated_predictions.jsonl"
    raw_records: List[Dict[str, Any]] = []
    sanity_printed = False

    for index, row in enumerate(eval_dataset):
        row_dict = dict(row)
        prompt = generation_prompt_for_row(row_dict, tokenizer, args.template)
        prediction = generate_eval_prediction(model, tokenizer, prompt, args)
        raw_records.append(
            {
                "index": index,
                "source_type": row_dict.get("source_type", ""),
                "data_family": row_dict.get("data_family", ""),
                "switch": row_dict.get("switch", ""),
                "version": row_dict.get("version", ""),
                "sub_version": row_dict.get("sub_version", ""),
                "section": row_dict.get("section", ""),
                "command": row_dict.get("command", ""),
                "question": row_dict.get("question", ""),
                "reference": row_dict.get("reference_answer", ""),
                "prompt": prompt,
                "prediction": prediction,
            }
        )
        if len(raw_records) == 5:
            print_generation_sanity_examples(raw_records)
            sanity_printed = True
            broken_records = [record for record in raw_records if generation_looks_corrupted(record["prediction"])]
            if broken_records:
                write_jsonl(predictions_path, raw_records)
                write_generation_broken_report(output_dir, predictions_path, raw_records, broken_records, args)
                raise RuntimeError(
                    "Eval generation is broken: generated predictions contain corrupted prompt/logit fragments. "
                    f"See {output_dir / 'corrected_generation_eval_report.md'}"
                )
        if (index + 1) % 10 == 0 or (index + 1) == len(eval_dataset):
            print(f"Generated {index + 1}/{len(eval_dataset)} eval predictions.", flush=True)

    if not sanity_printed:
        print_generation_sanity_examples(raw_records)
    broken_records = [record for record in raw_records if generation_looks_corrupted(record["prediction"])]
    if broken_records:
        write_jsonl(predictions_path, raw_records)
        write_generation_broken_report(output_dir, predictions_path, raw_records, broken_records, args)
        raise RuntimeError(
            "Eval generation is broken: generated predictions contain corrupted prompt/logit fragments. "
            f"See {output_dir / 'corrected_generation_eval_report.md'}"
        )

    rouge_metric = evaluate.load("rouge")
    bleu_metric = evaluate.load("bleu")
    preds = [record["prediction"] for record in raw_records]
    refs = [record["reference"] for record in raw_records]
    analyses = [
        task_analysis_for_pair(record["prediction"], record["reference"], record["data_family"], record)
        for record in raw_records
    ]
    task = aggregate_metric_dicts([metrics for metrics, _ in analyses])
    scored_records: List[Dict[str, Any]] = []
    for record, (metrics, details) in zip(raw_records, analyses):
        scored = dict(record)
        scored["generation_metrics"] = metrics
        scored["generation_details"] = details
        scored_records.append(scored)

    rouge_l = rouge_metric.compute(predictions=preds, references=refs, use_stemmer=True)["rougeL"]
    bleu = bleu_metric.compute(predictions=preds, references=[[ref] for ref in refs])["bleu"]
    generation_metrics = {
        "generation_samples": len(scored_records),
        "generation_rouge_l": round(float(rouge_l), 4),
        "generation_bleu": round(float(bleu), 4),
        "generation_keyword_overlap": task.get("keyword_overlap", 0.0),
        "generation_bug_id_accuracy": task.get("bug_id_accuracy", 0.0),
        "generation_command_syntax_preservation": task.get("command_syntax_preservation", 0.0),
        "generation_wrong_cli_syntax_rate": task.get("wrong_cli_syntax_rate", 0.0),
        "generation_unsupported_extra_cli_rate": task.get("unsupported_extra_cli_rate", 0.0),
        "generation_cli_hallucination_rate": task.get("cli_hallucination_rate", 0.0),
        "generation_acronym_meaning_hallucination_rate": task.get("acronym_meaning_hallucination_rate", 0.0),
    }
    write_jsonl(predictions_path, scored_records)
    examples = selected_generation_examples(scored_records)
    write_generation_eval_report(output_dir, predictions_path, load_existing_trainer_eval_metrics(output_dir), generation_metrics, examples, args)
    return {
        **generation_metrics,
        "predictions_path": str(predictions_path),
        "report_json": str(output_dir / "corrected_generation_eval_report.json"),
        "report_md": str(output_dir / "corrected_generation_eval_report.md"),
    }


def maybe_select_subset(dataset: Dataset, limit: Optional[int]) -> Dataset:
    if not limit or limit <= 0 or len(dataset) <= limit:
        return dataset
    return dataset.select(range(limit))


def find_nan_callback(trainer) -> Optional[NaNStoppingCallback]:
    for callback in getattr(trainer.callback_handler, "callbacks", []):
        if isinstance(callback, NaNStoppingCallback):
            return callback
    return None


def trainable_parameter_stats(model) -> Tuple[int, int, float]:
    trainable = 0
    total = 0
    for param in model.parameters():
        count = param.numel()
        total += count
        if param.requires_grad:
            trainable += count
    percent = (100.0 * trainable / total) if total else 0.0
    return trainable, total, percent


def print_startup_diagnostics(
    args: argparse.Namespace,
    datasets: DatasetDict,
    use_bf16: bool,
    use_fp16: bool,
    trainable_stats: Optional[Tuple[int, int, float]] = None,
) -> None:
    cuda_available = torch.cuda.is_available()
    gpu_name = torch.cuda.get_device_name(0) if cuda_available else "none"
    gpu_memory = "none"
    if cuda_available:
        try:
            free_bytes, total_bytes = torch.cuda.mem_get_info(0)
            gpu_memory = f"{round((total_bytes - free_bytes) / 1024**3, 2)} GiB used / {round(total_bytes / 1024**3, 2)} GiB total"
        except Exception:
            props = torch.cuda.get_device_properties(0)
            gpu_memory = f"{round(props.total_memory / 1024**3, 2)} GiB total"

    precision = "bf16" if use_bf16 else "fp16" if use_fp16 else "fp32"
    lines = [
        "=== Startup diagnostics ===",
        f"torch_version: {torch.__version__}",
        f"cuda_available: {cuda_available}",
        f"gpu_name: {gpu_name}",
        f"gpu_memory: {gpu_memory}",
        f"bf16_supported: {cuda_available and torch.cuda.is_bf16_supported()}",
        f"selected_precision: {precision}",
        f"model_name: {args.model_name}",
        f"quantization_mode: {'qlora_4bit_nf4_double_quant' if args.qlora else 'none_bf16_or_fp16_lora'}",
        f"lora_r_alpha_dropout: {args.lora_r}/{args.lora_alpha}/{args.lora_dropout}",
        f"max_length: {args.max_length}",
        f"batch_size: {args.batch_size}",
        f"grad_accum: {args.grad_accum}",
        f"effective_batch_size: {args.batch_size * args.grad_accum}",
        f"select_best_by_eval_loss: {args.select_best_by_eval_loss}",
        f"teacher_eval_during_training: {args.teacher_eval_during_training}",
        f"checkpoint_steps: {args.checkpoint_steps or 'scheduler-default'}",
        f"save_total_limit: {args.save_total_limit}",
        f"train_rows: {len(datasets['train'])}",
        f"validation_rows: {len(datasets['validation'])}",
    ]
    if trainable_stats:
        trainable, total, percent = trainable_stats
        lines.append(f"trainable_parameters: {trainable}")
        lines.append(f"all_parameters: {total}")
        lines.append(f"trainable_percent: {percent:.4f}")
    print("\n".join(lines))

    if not cuda_available:
        LOGGER.warning("CUDA is not available; training will be very slow on CPU.")
    if args.max_length > 1024:
        LOGGER.warning("max_length > 1024 can be slow and may increase NaN/OOM risk.")
    if cuda_available and args.batch_size > 1:
        total_gib = torch.cuda.get_device_properties(0).total_memory / 1024**3
        if total_gib <= 10:
            LOGGER.warning("batch_size > 1 on low VRAM GPU (%.1f GiB) may OOM; use batch_size=1.", total_gib)
    if args.eval_steps and args.eval_steps < 50:
        LOGGER.warning("eval_steps=%s is frequent and can slow training.", args.eval_steps)
    if args.save_steps and args.save_steps < 50:
        LOGGER.warning("save_steps=%s is frequent and can slow training.", args.save_steps)


def evaluate_only(args: argparse.Namespace) -> Dict[str, Any]:
    if not args.adapter_path:
        raise ValueError("--adapter_path is required when --eval_only is used.")
    if not args.val_data_path:
        raise ValueError("--val_data_path is required when --eval_only is used.")

    set_seed(args.seed)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    datasets = prepare_datasets(args)
    if len(datasets["validation"]) > 0:
        datasets["train"] = datasets["validation"].select([0])

    LOGGER.info("Eval-only validation samples: %s", len(datasets["validation"]))
    print(f"Eval-only validation samples: {len(datasets['validation'])}")

    tokenizer = setup_tokenizer(args.model_name, args.template, args.max_length)
    model, use_bf16, use_fp16 = setup_model(args, tokenizer)
    LOGGER.info("Loading adapter for eval-only run: %s", args.adapter_path)
    model = PeftModel.from_pretrained(model, args.adapter_path, is_trainable=False)
    for param in model.parameters():
        param.requires_grad_(False)
    model.eval()
    if hasattr(model.config, "use_cache"):
        model.config.use_cache = True
    if getattr(model, "generation_config", None) is not None:
        model.generation_config.use_cache = True

    print_startup_diagnostics(args, datasets, use_bf16, use_fp16, trainable_parameter_stats(model))
    trainer_eval_metrics = load_existing_trainer_eval_metrics(output_dir)
    if trainer_eval_metrics:
        print("Using existing Trainer eval_loss:", trainer_eval_metrics.get("eval_loss", "n/a"))
    else:
        print("Existing Trainer eval metrics were not found; generation report will use n/a for eval_loss.")

    generation_metrics = run_generation_eval(model, tokenizer, datasets["validation"], args, output_dir)
    combined_metrics = {**trainer_eval_loss_summary(trainer_eval_metrics), **generation_metrics}

    print("generation_cli_hallucination_rate:", generation_metrics.get("generation_cli_hallucination_rate"))
    print("generation_wrong_cli_syntax_rate:", generation_metrics.get("generation_wrong_cli_syntax_rate"))
    print("generation_unsupported_extra_cli_rate:", generation_metrics.get("generation_unsupported_extra_cli_rate"))
    print("generation_acronym_meaning_hallucination_rate:", generation_metrics.get("generation_acronym_meaning_hallucination_rate"))
    print("generation_command_syntax_preservation:", generation_metrics.get("generation_command_syntax_preservation"))
    print("Generated predictions:", generation_metrics.get("predictions_path"))
    print("Corrected generation eval report:", output_dir / "corrected_generation_eval_report.json")
    print("Corrected generation eval markdown:", output_dir / "corrected_generation_eval_report.md")
    return combined_metrics


def train(args: argparse.Namespace) -> Dict[str, float]:
    start_time = time.time()
    set_seed(args.seed)
    _ = bnb
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    if args.use_wandb:
        wandb.init(project=args.wandb_project, name=args.run_name, config=vars(args))

    datasets = prepare_datasets(args)
    if args.sanity_steps:
        datasets["train"] = maybe_select_subset(datasets["train"], args.debug_train_subset)
        datasets["validation"] = maybe_select_subset(datasets["validation"], args.debug_eval_subset)
        if "test" in datasets:
            datasets["test"] = maybe_select_subset(datasets["test"], args.debug_eval_subset)

    sample_weights: Optional[List[float]] = None
    if args.auto_sample_weights or args.save_weight_report:
        sample_weights, weight_report = build_weight_report(
            datasets["train"],
            args.weight_fields,
            args.min_sample_weight,
            args.max_sample_weight,
        )
        weight_report["enabled"] = bool(args.auto_sample_weights)
        weight_report["dataset_path"] = args.data_path
        weight_report["run_name"] = args.run_name
        print_weight_report(weight_report)
        weight_report_path = save_weight_report(output_dir, weight_report)
        print("Weight report saved to:", weight_report_path)

    print_metadata_context_samples(datasets["train"], args.template)
    validate_metadata_context_samples(datasets["train"], args.template)

    LOGGER.info("Train samples: %s | Validation samples: %s", len(datasets["train"]), len(datasets["validation"]))
    print(f"Train samples: {len(datasets['train'])} | Validation samples: {len(datasets['validation'])}")

    tokenizer = setup_tokenizer(args.model_name, args.template, args.max_length)
    model, use_bf16, use_fp16 = setup_model(args, tokenizer)

    if args.init_adapter_path:
        LOGGER.info("Loading existing adapter for continued training: %s", args.init_adapter_path)
        model = PeftModel.from_pretrained(model, args.init_adapter_path, is_trainable=True)
        target_modules = []
    else:
        target_modules = resolve_target_modules(model)
        LOGGER.info("Using LoRA target modules: %s", target_modules)
        model = get_peft_model(model, build_lora_config(args, target_modules))
    model.print_trainable_parameters()
    trainable_stats = trainable_parameter_stats(model)
    print_startup_diagnostics(args, datasets, use_bf16, use_fp16, trainable_stats)

    response_ids = pick_response_template_ids(datasets["train"], tokenizer, args.template, args.max_length)
    data_collator = safe_data_collator(tokenizer, response_ids, args.template)
    training_args = TrainingArguments(**build_training_arguments_kwargs(args, use_bf16, use_fp16))
    trainer = build_trainer(model, tokenizer, training_args, datasets, data_collator, args, sample_weights=sample_weights if args.auto_sample_weights else None)
    prepared_test_dataset = None
    if isinstance(trainer.eval_dataset, dict):
        prepared_test_dataset = trainer.eval_dataset.get("test")
        trainer.eval_dataset = trainer.eval_dataset["validation"]

    train_start = time.time()
    trainer.train(resume_from_checkpoint=args.resume_from_checkpoint)
    train_runtime = time.time() - train_start
    trainer.save_state()

    nan_callback = find_nan_callback(trainer)
    stopped_due_to_nan = bool(nan_callback and nan_callback.stopped_due_to_nan)

    if args.sanity_steps:
        eval_metrics = trainer.evaluate()
        final_loss = eval_metrics.get("eval_loss")
        loss_finite = finite_or_none(final_loss) is not None
        grad_norm_finite = True
        grad_norm = None
        if nan_callback and nan_callback.last_grad_norm is not None:
            grad_norm = nan_callback.last_grad_norm
            grad_norm_finite = math.isfinite(grad_norm)
        avg_seconds_per_step = train_runtime / max(float(trainer.state.global_step or 1), 1.0)
        sanity_report = {
            "sanity_steps_requested": args.sanity_steps,
            "global_step": int(trainer.state.global_step or 0),
            "final_sanity_loss": float(final_loss) if loss_finite else str(final_loss),
            "loss_finite": loss_finite,
            "last_grad_norm": grad_norm,
            "grad_norm_finite": grad_norm_finite,
            "average_seconds_per_step": round(avg_seconds_per_step, 4),
            "stopped_due_to_nan": stopped_due_to_nan,
            "recommendation": "continue" if loss_finite and grad_norm_finite and not stopped_due_to_nan else "stop",
        }
        save_json(output_dir / "sanity_report.json", sanity_report)
        print("Sanity report:", sanity_report)
        return {"eval_loss": float(final_loss) if loss_finite else float("nan")}

    if stopped_due_to_nan:
        LOGGER.warning("Training stopped due to NaN/Inf. Skipping final adapter save/evaluation.")
        return {"nan_failure": 1.0}

    adapter_dir = output_dir / "lora_adapters"
    tokenizer_dir = output_dir / "tokenizer"
    try:
        model.save_pretrained(adapter_dir, save_embedding_layers=False)
    except TypeError:
        model.save_pretrained(adapter_dir)
    tokenizer.save_pretrained(adapter_dir)
    tokenizer.save_pretrained(tokenizer_dir)

    eval_metrics = trainer.evaluate()
    eval_metrics = {key: float(value) if isinstance(value, (np.floating, np.integer)) else value for key, value in eval_metrics.items()}
    eval_metrics_by_family = metrics_by_family_from_references(datasets["validation"])
    save_json(output_dir / "eval_metrics.json", eval_metrics)
    save_json(output_dir / "eval_metrics_by_family.json", eval_metrics_by_family)

    test_metrics: Dict[str, Any] = {}
    test_metrics_by_family: Dict[str, Any] = {}
    if "test" in datasets:
        test_metrics = trainer.evaluate(eval_dataset=prepared_test_dataset, metric_key_prefix="test")
        test_metrics = {key: float(value) if isinstance(value, (np.floating, np.integer)) else value for key, value in test_metrics.items()}
        test_metrics_by_family = metrics_by_family_from_references(datasets["test"])
        save_json(output_dir / "test_metrics.json", test_metrics)
        save_json(output_dir / "test_metrics_by_family.json", test_metrics_by_family)

    eval_loss = eval_metrics.get("eval_loss")
    eval_report = {
        "run_name": args.run_name,
        "global_step": int(trainer.state.global_step or 0),
        "max_steps": args.max_steps,
        "sanity_steps": args.sanity_steps,
        "train_runtime_seconds": round(train_runtime, 3),
        "eval_loss_finite": finite_or_none(eval_loss) is not None,
        "stopped_due_to_nan": stopped_due_to_nan,
        "adapter_dir": str(adapter_dir),
        "eval_metrics": eval_metrics,
        "eval_metrics_by_family": eval_metrics_by_family,
        "test_metrics": test_metrics,
        "test_metrics_by_family": test_metrics_by_family,
    }
    save_json(output_dir / "eval_report.json", eval_report)

    save_json(output_dir / "training_args.json", vars(args))
    save_json(
        output_dir / "model_info.json",
        {
            "model_name": args.model_name,
            "template": args.template,
            "qlora": args.qlora,
            "load_in_4bit": args.qlora,
            "target_modules": target_modules,
            "torch_version": torch.__version__,
            "cuda_available": torch.cuda.is_available(),
            "cuda_device_count": torch.cuda.device_count(),
            "train_runtime_seconds": round(time.time() - start_time, 3),
        },
    )

    if args.use_wandb:
        wandb.log({**eval_metrics, **test_metrics})
        wandb.finish()

    print("Evaluation metrics:", eval_metrics)
    if test_metrics:
        print("Test metrics:", test_metrics)
    return eval_metrics


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="QLoRA fine-tuning for Aruba AOS-CX assistant")
    parser.add_argument("--data_path", required=True)
    parser.add_argument("--val_data_path", default=None)
    parser.add_argument("--test_data_path", default=None)
    parser.add_argument("--val_split", type=float, default=0.1)
    parser.add_argument("--model_name", default=DEFAULT_MODEL_NAME)
    parser.add_argument("--template", default=DEFAULT_TEMPLATE, choices=list(TEMPLATES.keys()))
    parser.add_argument("--output_dir", default="./outputs")
    parser.add_argument("--max_length", type=int, default=512)
    parser.add_argument("--batch_size", type=int, default=1)
    parser.add_argument("--grad_accum", type=int, default=8)
    parser.add_argument("--epochs", type=float, default=1)
    parser.add_argument("--lr", type=float, default=1e-5)
    parser.add_argument("--lora_r", type=int, default=8)
    parser.add_argument("--lora_alpha", type=int, default=16)
    parser.add_argument("--lora_dropout", type=float, default=0.05)
    parser.add_argument("--gradient_checkpointing", action="store_true")
    parser.add_argument("--bf16", action="store_true")
    parser.add_argument("--fp16", action="store_true")
    parser.add_argument("--eval_steps", type=int, default=None)
    parser.add_argument("--save_steps", type=int, default=None)
    parser.add_argument(
        "--checkpoint_steps",
        default="",
        help="Comma-separated exact optimizer steps to save. Overrides periodic checkpoint saving when set.",
    )
    parser.add_argument("--save_total_limit", type=int, default=2)
    parser.add_argument("--logging_steps", type=int, default=20)
    parser.add_argument("--early_stopping_patience", type=int, default=3)
    parser.add_argument(
        "--select_best_by_eval_loss",
        action=argparse.BooleanOptionalAction,
        default=True,
        help=(
            "Load the checkpoint with the lowest eval loss at the end. Disable for strict-generation "
            "checkpoint selection with --no-select_best_by_eval_loss."
        ),
    )
    parser.add_argument(
        "--teacher_eval_during_training",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Run teacher-forced validation during training. Final diagnostic validation still runs after training.",
    )
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--warmup_ratio", type=float, default=0.05)
    parser.add_argument("--weight_decay", type=float, default=0.01)
    parser.add_argument("--max_grad_norm", type=float, default=0.3)
    parser.add_argument("--optim", default="paged_adamw_32bit")
    parser.add_argument("--qlora", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--packing", action="store_true", default=False)
    parser.add_argument("--max_steps", type=int, default=-1)
    parser.add_argument("--sanity_steps", type=int, default=None)
    parser.add_argument("--stop_on_nan", action="store_true")
    parser.add_argument("--debug_train_subset", type=int, default=512)
    parser.add_argument("--debug_eval_subset", type=int, default=128)
    parser.add_argument("--init_adapter_path", default=None)
    parser.add_argument("--eval_only", action="store_true", default=False)
    parser.add_argument("--adapter_path", default=None)
    parser.add_argument("--eval_generation_limit", type=int, default=100)
    parser.add_argument("--eval_max_new_tokens", type=int, default=120)
    parser.add_argument("--resume_from_checkpoint", default=None)
    parser.add_argument("--use_wandb", action="store_true", default=False)
    parser.add_argument("--wandb_project", default="aruba-aos-cx-assistant")
    parser.add_argument("--run_name", default="qlora-run")
    parser.add_argument("--auto_sample_weights", action="store_true", default=False)
    parser.add_argument("--weight_fields", nargs="+", default=DEFAULT_WEIGHT_FIELDS)
    parser.add_argument("--min_sample_weight", type=float, default=DEFAULT_MIN_SAMPLE_WEIGHT)
    parser.add_argument("--max_sample_weight", type=float, default=DEFAULT_MAX_SAMPLE_WEIGHT)
    parser.add_argument("--save_weight_report", action="store_true", default=False)
    return parser.parse_args()


if __name__ == "__main__":
    warnings.filterwarnings("ignore", message=".*_check_is_size will be removed.*", category=FutureWarning)
    warnings.filterwarnings("ignore", message="`tokenizer` is deprecated.*", category=FutureWarning)
    logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(name)s | %(message)s")
    cli_args = parse_args()
    final_metrics = evaluate_only(cli_args) if cli_args.eval_only else train(cli_args)
    print("Final metrics:", final_metrics)
