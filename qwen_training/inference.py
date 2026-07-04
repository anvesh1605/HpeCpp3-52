import argparse
from pathlib import Path
from typing import Any, Dict

import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ADAPTER_PATH = REPO_ROOT / "models" / "qwen"
DEFAULT_MODEL_NAME = "Qwen/Qwen2.5-3B-Instruct"

SYSTEM_PROMPT = (
    "You are an Aruba AOS-CX release-notes assistant.\n"
    "You answer using the provided release-note training data only.\n"
    "Preserve documented release-note facts exactly, including bug IDs when present, categories, symptoms, causes, workarounds, "
    "release dates, version history, supported products, compatibility, certifications, and procedures when known.\n"
    "Do not invent unsupported bug IDs, workarounds, affected versions, release dates, product mappings, compatibility claims, or configuration steps.\n"
    "If the information is not documented in the training data, say it is not documented."
)

TEMPLATES: Dict[str, Dict[str, str]] = {
    "chatml": {
        "system_prefix": "<|im_start|>system\n",
        "system_suffix": "<|im_end|>\n",
        "user_prefix": "<|im_start|>user\n",
        "user_suffix": "<|im_end|>\n",
        "assistant_prefix": "<|im_start|>assistant\n",
    },
    "llama": {
        "system_prefix": "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\n",
        "system_suffix": "<|eot_id|>",
        "user_prefix": "<|start_header_id|>user<|end_header_id|>\n\n",
        "user_suffix": "<|eot_id|>",
        "assistant_prefix": "<|start_header_id|>assistant<|end_header_id|>\n\n",
    },
    "llama3": {
        "system_prefix": "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\n",
        "system_suffix": "<|eot_id|>",
        "user_prefix": "<|start_header_id|>user<|end_header_id|>\n\n",
        "user_suffix": "<|eot_id|>",
        "assistant_prefix": "<|start_header_id|>assistant<|end_header_id|>\n\n",
    },
    "tinyllama": {
        "system_prefix": "<|system|>\n",
        "system_suffix": "</s>\n",
        "user_prefix": "<|user|>\n",
        "user_suffix": "</s>\n",
        "assistant_prefix": "<|assistant|>\n",
    },
    "gemma": {
        "system_prefix": "<start_of_turn>user\n",
        "system_suffix": "\n\n",
        "user_prefix": "",
        "user_suffix": "<end_of_turn>\n",
        "assistant_prefix": "<start_of_turn>model\n",
    },
    "phi": {
        "system_prefix": "<|system|>\n",
        "system_suffix": "<|end|>\n",
        "user_prefix": "<|user|>\n",
        "user_suffix": "<|end|>\n",
        "assistant_prefix": "<|assistant|>\n",
    },
    "plain": {
        "system_prefix": "### System:\n\n",
        "system_suffix": "\n\n",
        "user_prefix": "### Instruction:\n\n",
        "user_suffix": "\n\n",
        "assistant_prefix": "### Response:\n\n",
    },
}

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
    return text.strip()


def build_inference_prompt(
    switch: str,
    version: str,
    sub_version: str,
    source_type: str,
    data_family: str,
    question: str,
    template_name: str,
) -> str:
    template = TEMPLATES[template_name]
    metadata = [
        f"Switch: {normalize_text(switch)}" if switch else "",
        f"Version: {normalize_text(version)}" if version else "",
        f"Sub-version: {normalize_text(sub_version)}" if sub_version else "",
        f"Source type: {normalize_text(source_type)}" if source_type else "",
        f"Data family: {normalize_text(data_family)}" if data_family else "",
    ]
    context = SYSTEM_PROMPT + "\n\n" + "\n".join(line for line in metadata if line)
    user = f"Question:\n{normalize_text(question)}"
    return (
        f"{template['system_prefix']}{context}{template['system_suffix']}"
        f"{template['user_prefix']}{user}{template['user_suffix']}"
        f"{template['assistant_prefix']}"
    )


def load_model(model_name: str, adapter_path: str):
    use_bf16 = torch.cuda.is_available() and torch.cuda.is_bf16_supported()
    compute_dtype = torch.bfloat16 if use_bf16 else torch.float16
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=compute_dtype,
        bnb_4bit_use_double_quant=True,
    )

    tokenizer = AutoTokenizer.from_pretrained(adapter_path, trust_remote_code=True, use_fast=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    kwargs = {
        "quantization_config": bnb_config,
        "device_map": "auto",
        "trust_remote_code": True,
        "torch_dtype": compute_dtype,
    }
    base = AutoModelForCausalLM.from_pretrained(model_name, **kwargs)
    base.resize_token_embeddings(len(tokenizer))
    model = PeftModel.from_pretrained(base, adapter_path)
    model.eval()
    return model, tokenizer


def generate(
    model,
    tokenizer,
    prompt: str,
    max_new_tokens: int,
    temperature: float,
    top_p: float,
    repetition_penalty: float,
) -> str:
    inputs = tokenizer(prompt, return_tensors="pt")
    inputs = {key: value.to(model.device) for key, value in inputs.items()}
    input_len = inputs["input_ids"].shape[1]
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            temperature=temperature,
            top_p=top_p,
            do_sample=temperature > 0,
            repetition_penalty=repetition_penalty,
            pad_token_id=tokenizer.eos_token_id,
        )
    decoded = tokenizer.decode(outputs[0][input_len:], skip_special_tokens=True).strip()
    return decoded or "This information is not documented in the available training data."


def interactive_loop(model, tokenizer, args):
    print("Aruba AOS-CX Assistant | type 'quit', 'exit', or 'q' to end.")
    while True:
        question = input("You: ").strip()
        if question.lower() in {"quit", "exit", "q"}:
            print("Session ended.")
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
        answer = generate(model, tokenizer, prompt, args.max_new_tokens, args.temperature, args.top_p, args.repetition_penalty)
        print(f"Assistant: {answer}\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Inference for Aruba AOS-CX LoRA adapter")
    parser.add_argument("--model_name", default=DEFAULT_MODEL_NAME)
    parser.add_argument("--base_model", default=DEFAULT_MODEL_NAME)
    parser.add_argument("--adapter_path", type=Path, default=DEFAULT_ADAPTER_PATH)
    parser.add_argument("--template", default="chatml", choices=list(TEMPLATES.keys()))
    parser.add_argument("--switch", default="")
    parser.add_argument("--version", default="")
    parser.add_argument("--sub_version", default="")
    parser.add_argument("--source_type", default="")
    parser.add_argument("--data_family", default="")
    parser.add_argument("--question", default=None)
    parser.add_argument("--temperature", type=float, default=0.1)
    parser.add_argument("--top_p", type=float, default=0.9)
    parser.add_argument("--max_new_tokens", type=int, default=256)
    parser.add_argument("--repetition_penalty", type=float, default=1.1)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    model_name = args.model_name or args.base_model or DEFAULT_MODEL_NAME
    model, tokenizer = load_model(model_name, args.adapter_path)

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
        answer = generate(model, tokenizer, prompt, args.max_new_tokens, args.temperature, args.top_p, args.repetition_penalty)
        print(f"Q: {args.question}")
        print(f"A: {answer}")
    else:
        interactive_loop(model, tokenizer, args)


if __name__ == "__main__":
    main()
