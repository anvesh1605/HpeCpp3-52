import argparse
import csv
import json
import subprocess
import sys
import time
from pathlib import Path
from typing import Any, Dict, List


MODEL_REGISTRY: Dict[str, Dict[str, Any]] = {
    "qwen25_3b": {
        "model_name": "Qwen/Qwen2.5-3B-Instruct",
        "template": "chatml",
        "max_length": 1024,
        "batch_size": 2,
        "grad_accum": 8,
        "epochs": 2,
        "lr": 1e-4,
        "lora_r": 16,
        "lora_alpha": 32,
        "lora_dropout": 0.05,
        "priority": "tier1",
        "notes": "Recommended default candidate.",
    },
    "qwen25_15b": {
        "model_name": "Qwen/Qwen2.5-1.5B-Instruct",
        "template": "chatml",
        "max_length": 1024,
        "batch_size": 4,
        "grad_accum": 4,
        "epochs": 2,
        "lr": 1e-4,
        "lora_r": 16,
        "lora_alpha": 32,
        "lora_dropout": 0.05,
        "priority": "tier1",
        "notes": "Lightweight fallback if 3B is too slow.",
    },
    "qwen25_05b": {
        "model_name": "Qwen/Qwen2.5-0.5B-Instruct",
        "template": "chatml",
        "max_length": 768,
        "batch_size": 8,
        "grad_accum": 2,
        "epochs": 3,
        "lr": 2e-4,
        "lora_r": 16,
        "lora_alpha": 32,
        "lora_dropout": 0.05,
        "priority": "tier3",
        "notes": "Very small ablation model.",
    },
    "qwen25_coder_3b": {
        "model_name": "Qwen/Qwen2.5-Coder-3B-Instruct",
        "template": "chatml",
        "max_length": 1024,
        "batch_size": 2,
        "grad_accum": 8,
        "epochs": 2,
        "lr": 1e-4,
        "lora_r": 16,
        "lora_alpha": 32,
        "lora_dropout": 0.05,
        "priority": "tier2",
        "notes": "Useful comparison for CLI syntax and command-heavy product documentation.",
    },
    "qwen25_coder_15b": {
        "model_name": "Qwen/Qwen2.5-Coder-1.5B-Instruct",
        "template": "chatml",
        "max_length": 1024,
        "batch_size": 4,
        "grad_accum": 4,
        "epochs": 2,
        "lr": 1e-4,
        "lora_r": 16,
        "lora_alpha": 32,
        "lora_dropout": 0.05,
        "priority": "tier2",
        "notes": "Small command-syntax comparison model.",
    },
    "llama32_3b": {
        "model_name": "meta-llama/Llama-3.2-3B-Instruct",
        "template": "llama",
        "max_length": 1024,
        "batch_size": 2,
        "grad_accum": 8,
        "epochs": 2,
        "lr": 1e-4,
        "lora_r": 16,
        "lora_alpha": 32,
        "lora_dropout": 0.05,
        "priority": "tier1",
        "notes": "May require Hugging Face access approval.",
    },
    "phi35_mini": {
        "model_name": "microsoft/Phi-3.5-mini-instruct",
        "template": "chatml",
        "max_length": 1024,
        "batch_size": 2,
        "grad_accum": 8,
        "epochs": 2,
        "lr": 8e-5,
        "lora_r": 16,
        "lora_alpha": 32,
        "lora_dropout": 0.05,
        "priority": "tier1",
        "notes": "Strong compact reasoning candidate. Use slightly lower LR.",
    },
    "phi3_mini_4k": {
        "model_name": "microsoft/Phi-3-mini-4k-instruct",
        "template": "chatml",
        "max_length": 1024,
        "batch_size": 2,
        "grad_accum": 8,
        "epochs": 2,
        "lr": 8e-5,
        "lora_r": 16,
        "lora_alpha": 32,
        "lora_dropout": 0.05,
        "priority": "tier2",
        "notes": "Near 3.8B candidate; useful comparison with Phi-3.5-mini.",
    },
    "gemma3_4b": {
        "model_name": "google/gemma-3-4b-it",
        "template": "gemma",
        "max_length": 1024,
        "batch_size": 1,
        "grad_accum": 16,
        "epochs": 2,
        "lr": 8e-5,
        "lora_r": 16,
        "lora_alpha": 32,
        "lora_dropout": 0.05,
        "priority": "tier2",
        "notes": "Near 4B. May be gated and may need license acceptance.",
    },
    "gemma2_2b": {
        "model_name": "google/gemma-2-2b-it",
        "template": "gemma",
        "max_length": 1024,
        "batch_size": 2,
        "grad_accum": 8,
        "epochs": 2,
        "lr": 8e-5,
        "lora_r": 16,
        "lora_alpha": 32,
        "lora_dropout": 0.05,
        "priority": "tier2",
        "notes": "Smaller Gemma comparison. May require license acceptance.",
    },
    "tinyllama_11b": {
        "model_name": "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        "template": "tinyllama",
        "max_length": 768,
        "batch_size": 4,
        "grad_accum": 4,
        "epochs": 3,
        "lr": 2e-4,
        "lora_r": 16,
        "lora_alpha": 32,
        "lora_dropout": 0.05,
        "priority": "tier2",
        "notes": "Small proof-of-concept baseline.",
    },
    "stablelm2_16b": {
        "model_name": "stabilityai/stablelm-2-1_6b-chat",
        "template": "chatml",
        "max_length": 768,
        "batch_size": 4,
        "grad_accum": 4,
        "epochs": 3,
        "lr": 1e-4,
        "lora_r": 16,
        "lora_alpha": 32,
        "lora_dropout": 0.05,
        "priority": "tier2",
        "notes": "Compact comparison model.",
    },
    "smollm2_17b": {
        "model_name": "HuggingFaceTB/SmolLM2-1.7B-Instruct",
        "template": "chatml",
        "max_length": 768,
        "batch_size": 4,
        "grad_accum": 4,
        "epochs": 3,
        "lr": 1e-4,
        "lora_r": 16,
        "lora_alpha": 32,
        "lora_dropout": 0.05,
        "priority": "tier3",
        "notes": "Very small open model comparison.",
    },
    "minicpm3_4b": {
        "model_name": "openbmb/MiniCPM3-4B",
        "template": "chatml",
        "max_length": 1024,
        "batch_size": 1,
        "grad_accum": 16,
        "epochs": 2,
        "lr": 8e-5,
        "lora_r": 16,
        "lora_alpha": 32,
        "lora_dropout": 0.05,
        "priority": "tier3",
        "notes": "Near-4B optional candidate. Continue on error if unavailable or incompatible.",
    },
    "deepseek_r1_qwen_15b": {
        "model_name": "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B",
        "template": "chatml",
        "max_length": 1024,
        "batch_size": 4,
        "grad_accum": 4,
        "epochs": 2,
        "lr": 8e-5,
        "lora_r": 16,
        "lora_alpha": 32,
        "lora_dropout": 0.05,
        "priority": "tier3",
        "notes": "Reasoning-style distilled model. May produce verbose reasoning unless prompts are controlled.",
    },
}

MODEL_GROUPS = {
    "tier1": [key for key, value in MODEL_REGISTRY.items() if value["priority"] == "tier1"],
    "tier2": [key for key, value in MODEL_REGISTRY.items() if value["priority"] == "tier2"],
    "tier3": [key for key, value in MODEL_REGISTRY.items() if value["priority"] == "tier3"],
    "all": list(MODEL_REGISTRY.keys()),
}


def parse_bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {"1", "true", "yes", "y", "on"}


def expand_models(model_args: List[str]) -> List[str]:
    selected: List[str] = []
    for item in model_args:
        if item in MODEL_GROUPS:
            selected.extend(MODEL_GROUPS[item])
        elif item in MODEL_REGISTRY:
            selected.append(item)
        else:
            raise ValueError(f"Unknown model key or group: {item}")
    deduped: List[str] = []
    for key in selected:
        if key not in deduped:
            deduped.append(key)
    return deduped


def load_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def metric(metrics: Dict[str, Any], *names: str) -> float:
    for name in names:
        if name in metrics:
            try:
                return float(metrics[name])
            except (TypeError, ValueError):
                return 0.0
    return 0.0


def compute_overall_score(eval_metrics: Dict[str, Any], test_metrics: Dict[str, Any], product_doc_ratio: float) -> float:
    metrics = test_metrics or eval_metrics
    eval_loss = metric(eval_metrics, "eval_loss", "test_loss")
    normalized_eval_score = 1.0 / (1.0 + eval_loss) if eval_loss >= 0 else 0.0

    if product_doc_ratio < 0.10:
        weights = {
            "bug_id_accuracy": 0.35,
            "category_accuracy": 0.25,
            "command_syntax_preservation": 0.05,
            "command_name_accuracy": 0.05,
            "no_fake_bug_rate": 0.10,
            "keyword_overlap": 0.10,
            "normalized_eval_score": 0.10,
        }
    else:
        weights = {
            "bug_id_accuracy": 0.25,
            "category_accuracy": 0.15,
            "command_syntax_preservation": 0.20,
            "command_name_accuracy": 0.10,
            "no_fake_bug_rate": 0.10,
            "keyword_overlap": 0.10,
            "normalized_eval_score": 0.10,
        }

    score = (
        weights["bug_id_accuracy"] * metric(metrics, "test_bug_id_accuracy", "eval_bug_id_accuracy", "bug_id_accuracy")
        + weights["category_accuracy"] * metric(metrics, "test_category_accuracy", "eval_category_accuracy", "category_accuracy")
        + weights["command_syntax_preservation"] * metric(metrics, "test_command_syntax_preservation", "eval_command_syntax_preservation", "command_syntax_preservation")
        + weights["command_name_accuracy"] * metric(metrics, "test_command_name_accuracy", "eval_command_name_accuracy", "command_name_accuracy")
        + weights["no_fake_bug_rate"] * metric(metrics, "test_no_fake_bug_rate", "eval_no_fake_bug_rate", "no_fake_bug_rate")
        + weights["keyword_overlap"] * metric(metrics, "test_keyword_overlap", "eval_keyword_overlap", "keyword_overlap")
        + weights["normalized_eval_score"] * normalized_eval_score
    )
    return round(score, 6)


def build_train_command(args: argparse.Namespace, model_key: str, output_dir: Path) -> List[str]:
    cfg = MODEL_REGISTRY[model_key]
    return [
        sys.executable,
        "train.py",
        "--data_path",
        args.train_data,
        "--val_data_path",
        args.val_data,
        "--test_data_path",
        args.test_data,
        "--model_name",
        cfg["model_name"],
        "--template",
        cfg["template"],
        "--output_dir",
        str(output_dir),
        "--max_length",
        str(cfg["max_length"]),
        "--batch_size",
        str(cfg["batch_size"]),
        "--grad_accum",
        str(cfg["grad_accum"]),
        "--epochs",
        str(cfg["epochs"]),
        "--lr",
        str(cfg["lr"]),
        "--lora_r",
        str(cfg["lora_r"]),
        "--lora_alpha",
        str(cfg["lora_alpha"]),
        "--lora_dropout",
        str(cfg["lora_dropout"]),
        "--gradient_checkpointing",
        "--run_name",
        model_key,
    ]


def result_from_completed(model_key: str, output_dir: Path, duration: float, product_doc_ratio: float) -> Dict[str, Any]:
    cfg = MODEL_REGISTRY[model_key]
    eval_metrics = load_json(output_dir / "eval_metrics.json")
    test_metrics = load_json(output_dir / "test_metrics.json")
    model_info = load_json(output_dir / "model_info.json")
    return {
        "model_key": model_key,
        "model_name": cfg["model_name"],
        "status": "completed",
        "output_dir": str(output_dir),
        "eval_loss": metric(eval_metrics, "eval_loss"),
        "test_loss": metric(test_metrics, "test_loss"),
        "bug_id_accuracy": metric(test_metrics, "test_bug_id_accuracy", "bug_id_accuracy") or metric(eval_metrics, "eval_bug_id_accuracy", "bug_id_accuracy"),
        "category_accuracy": metric(test_metrics, "test_category_accuracy", "category_accuracy") or metric(eval_metrics, "eval_category_accuracy", "category_accuracy"),
        "command_name_accuracy": metric(test_metrics, "test_command_name_accuracy", "command_name_accuracy") or metric(eval_metrics, "eval_command_name_accuracy", "command_name_accuracy"),
        "command_syntax_preservation": metric(test_metrics, "test_command_syntax_preservation", "command_syntax_preservation") or metric(eval_metrics, "eval_command_syntax_preservation", "command_syntax_preservation"),
        "no_fake_bug_rate": metric(test_metrics, "test_no_fake_bug_rate", "no_fake_bug_rate") or metric(eval_metrics, "eval_no_fake_bug_rate", "no_fake_bug_rate"),
        "no_cli_hallucination_rate": metric(test_metrics, "test_no_cli_hallucination_rate", "no_cli_hallucination_rate") or metric(eval_metrics, "eval_no_cli_hallucination_rate", "no_cli_hallucination_rate"),
        "keyword_overlap": metric(test_metrics, "test_keyword_overlap", "keyword_overlap") or metric(eval_metrics, "eval_keyword_overlap", "keyword_overlap"),
        "overall_score": compute_overall_score(eval_metrics, test_metrics, product_doc_ratio),
        "train_runtime_seconds": metric(model_info, "train_runtime_seconds") or round(duration, 3),
        "notes": cfg["notes"],
    }


def write_summary(summary_file: Path, results: List[Dict[str, Any]]) -> None:
    summary_file.parent.mkdir(parents=True, exist_ok=True)
    ranked = sorted(
        results,
        key=lambda item: (
            item.get("overall_score", 0.0),
            item.get("bug_id_accuracy", 0.0),
            item.get("command_syntax_preservation", 0.0),
            -item.get("eval_loss", 999.0),
        ),
        reverse=True,
    )
    with summary_file.open("w", encoding="utf-8") as handle:
        json.dump(ranked, handle, indent=2, ensure_ascii=False)

    csv_path = summary_file.with_suffix(".csv")
    fieldnames = [
        "model_key",
        "model_name",
        "status",
        "output_dir",
        "eval_loss",
        "test_loss",
        "bug_id_accuracy",
        "category_accuracy",
        "command_name_accuracy",
        "command_syntax_preservation",
        "no_fake_bug_rate",
        "no_cli_hallucination_rate",
        "keyword_overlap",
        "overall_score",
        "train_runtime_seconds",
        "notes",
        "error",
    ]
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in ranked:
            writer.writerow({key: row.get(key, "") for key in fieldnames})


def read_product_doc_ratio(train_data: str) -> float:
    report_path = Path(train_data).parent / "dataset_report.json"
    report = load_json(report_path)
    return float(report.get("product_doc_ratio", 0.0) or 0.0)


def main() -> int:
    parser = argparse.ArgumentParser(description="Run compact model A/B experiments")
    parser.add_argument("--train_data", default="final_json/all_switches/train_chat_all_clean.jsonl")
    parser.add_argument("--val_data", default="final_json/all_switches/val_chat_all_clean.jsonl")
    parser.add_argument("--test_data", default="final_json/all_switches/test_chat_all_clean.jsonl")
    parser.add_argument("--output_root", default="outputs_model_ab")
    parser.add_argument("--models", nargs="+", default=["tier1"])
    parser.add_argument("--skip_existing", action="store_true")
    parser.add_argument("--dry_run", action="store_true")
    parser.add_argument("--continue_on_error", type=parse_bool, default=True)
    parser.add_argument("--summary_file", default="outputs_model_ab/experiment_summary.json")
    args = parser.parse_args()

    output_root = Path(args.output_root)
    output_root.mkdir(parents=True, exist_ok=True)
    product_doc_ratio = read_product_doc_ratio(args.train_data)
    if product_doc_ratio < 0.10:
        print("Warning: product documentation is less than 10% of dataset; scoring will emphasize bug metrics.")

    results: List[Dict[str, Any]] = []
    for model_key in expand_models(args.models):
        cfg = MODEL_REGISTRY[model_key]
        output_dir = output_root / model_key
        if args.skip_existing and (output_dir / "eval_metrics.json").exists():
            print(f"Skipping existing: {model_key}")
            results.append(result_from_completed(model_key, output_dir, 0.0, product_doc_ratio))
            continue

        cmd = build_train_command(args, model_key, output_dir)
        print(f"\n=== {model_key} ===")
        print(" ".join(cmd))
        if args.dry_run:
            results.append(
                {
                    "model_key": model_key,
                    "model_name": cfg["model_name"],
                    "status": "dry_run",
                    "output_dir": str(output_dir),
                    "notes": cfg["notes"],
                }
            )
            continue

        start = time.time()
        log_dir = output_dir / "logs"
        log_dir.mkdir(parents=True, exist_ok=True)
        with (log_dir / "train.out.log").open("w", encoding="utf-8") as stdout, (log_dir / "train.err.log").open("w", encoding="utf-8") as stderr:
            completed = subprocess.run(cmd, check=False, stdout=stdout, stderr=stderr)
        duration = time.time() - start
        if completed.returncode != 0:
            error = f"Training failed with exit code {completed.returncode}"
            result = {
                "model_key": model_key,
                "model_name": cfg["model_name"],
                "status": "failed",
                "output_dir": str(output_dir),
                "error": error,
                "notes": f"{cfg['notes']} Model may be gated, unavailable, or incompatible.",
            }
            results.append(result)
            write_summary(Path(args.summary_file), results)
            print(error)
            if not args.continue_on_error:
                return completed.returncode
            continue

        results.append(result_from_completed(model_key, output_dir, duration, product_doc_ratio))
        write_summary(Path(args.summary_file), results)

    write_summary(Path(args.summary_file), results)
    print(f"\nSummary: {args.summary_file}")
    print(f"CSV: {Path(args.summary_file).with_suffix('.csv')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
