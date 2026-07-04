import argparse
import logging
import os
import warnings
from pathlib import Path
from typing import Optional

from inference import build_inference_prompt, generate, load_model


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MODEL_NAME = "Qwen/Qwen2.5-3B-Instruct"
DEFAULT_ADAPTER_PATH = REPO_ROOT / "models" / "qwen"

os.environ.setdefault("TRANSFORMERS_NO_ADVISORY_WARNINGS", "1")
warnings.filterwarnings("ignore", category=FutureWarning)
logging.getLogger("transformers").setLevel(logging.ERROR)
logging.getLogger("huggingface_hub").setLevel(logging.ERROR)
logging.getLogger("bitsandbytes").setLevel(logging.ERROR)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Ask a release-notes question against the trained Aruba assistant."
    )
    parser.add_argument(
        "--question",
        default=None,
        help="Ask one question and print the answer. If omitted, an interactive prompt starts.",
    )
    parser.add_argument(
        "--model_name",
        default=DEFAULT_MODEL_NAME,
        help=f"Base model name. Default: {DEFAULT_MODEL_NAME}",
    )
    parser.add_argument(
        "--adapter_path",
        default=DEFAULT_ADAPTER_PATH,
        help=f"LoRA adapter path. Default: {DEFAULT_ADAPTER_PATH}",
    )
    parser.add_argument("--template", default="chatml", help="Prompt template to use.")
    parser.add_argument("--switch", default="", help="Optional switch family metadata.")
    parser.add_argument("--version", default="", help="Optional version metadata.")
    parser.add_argument("--sub_version", default="", help="Optional sub-version metadata.")
    parser.add_argument("--source_type", default="", help="Optional source-type metadata.")
    parser.add_argument("--data_family", default="", help="Optional data-family metadata.")
    parser.add_argument("--temperature", type=float, default=0.0, help="Generation temperature.")
    parser.add_argument("--top_p", type=float, default=1.0, help="Top-p sampling value.")
    parser.add_argument("--max_new_tokens", type=int, default=160, help="Maximum answer length.")
    parser.add_argument(
        "--repetition_penalty",
        type=float,
        default=1.1,
        help="Repetition penalty for generation.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    print("Loading release-notes model...", flush=True)
    model, tokenizer = load_model(args.model_name, args.adapter_path)

    if args.question:
        prompt = build_inference_prompt(
            switch=args.switch,
            version=args.version,
            sub_version=args.sub_version,
            source_type=args.source_type,
            data_family=args.data_family,
            question=args.question,
            template_name=args.template,
        )
        answer = generate(
            model,
            tokenizer,
            prompt,
            args.max_new_tokens,
            args.temperature,
            args.top_p,
            args.repetition_penalty,
        )
        print(f"Answer: {answer}", flush=True)
        return

    print("Ready. Type a release-notes question and press Enter. Type quit to exit.", flush=True)
    while True:
        question = input("Question: ").strip()
        if question.lower() in {"quit", "exit", "q"}:
            print("Session ended.", flush=True)
            break
        prompt = build_inference_prompt(
            switch=args.switch,
            version=args.version,
            sub_version=args.sub_version,
            source_type=args.source_type,
            data_family=args.data_family,
            question=question,
            template_name=args.template,
        )
        answer = generate(
            model,
            tokenizer,
            prompt,
            args.max_new_tokens,
            args.temperature,
            args.top_p,
            args.repetition_penalty,
        )
        print(f"Answer: {answer}", flush=True)
        print("", flush=True)


if __name__ == "__main__":
    main()
