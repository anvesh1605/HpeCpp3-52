import argparse
import json
from pathlib import Path
import re
import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

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
    "the switch model, firmware version, and sub-version context provided. "
    "Do not include external URLs or source citations."
)

URL_RE = re.compile(r"https?://\S+|www\.\S+")

MOJIBAKE_REPLACEMENTS = {
    "\u00e2\u0080": "-",
    "\u00e2\u0080\u0093": "-",
    "\u00e2\u0080\u0094": "-",
    "\u00e2\u0080\u0098": "'",
    "\u00e2\u0080\u0099": "'",
    "\u00e2\u0080\u009c": '"',
    "\u00e2\u0080\u009d": '"',
    "\u00c2\u00a0": " ",
}


def normalize_text(value: str) -> str:
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


def strip_urls(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\((?:https?://|www\.)[^)]+\)", r"\1", text)
    text = URL_RE.sub("", text)
    text = re.sub(r"\s{2,}", " ", text)
    return text.strip()


def build_inference_prompt(
    switch: str,
    version: str,
    sub_version: str,
    question: str,
    template_name: str,
) -> str:
    template = TEMPLATES[template_name]
    switch = normalize_text(switch)
    version = normalize_text(version)
    sub_version = normalize_text(sub_version)
    question = normalize_text(question).strip()
    context = f"Switch: {switch} | Firmware: {version}.{sub_version}\n{SYSTEM_PROMPT}"
    prompt = (
        f"{template['system_prefix']}{context}{template['system_suffix']}"
        f"{template['user_prefix']}{question}{template['user_suffix']}"
        f"{template['assistant_prefix']}"
    )
    return prompt


def load_model(base_model: str, adapter_path: str):
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

    base = AutoModelForCausalLM.from_pretrained(
        base_model,
        quantization_config=bnb_config,
        device_map="auto",
        trust_remote_code=True,
        torch_dtype=compute_dtype,
    )
    base.resize_token_embeddings(len(tokenizer))
    model = PeftModel.from_pretrained(base, adapter_path)
    model.eval()
    return model, tokenizer


def generate(
    model,
    tokenizer,
    prompt: str,
    max_new_tokens: int = 256,
    temperature: float = 0.1,
    top_p: float = 0.9,
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
            do_sample=(temperature > 0),
            repetition_penalty=1.15,
            pad_token_id=tokenizer.eos_token_id,
        )

    new_tokens = outputs[0][input_len:]
    decoded = tokenizer.decode(new_tokens, skip_special_tokens=True)
    return strip_urls(decoded)


def get_suggestions(
    model,
    tokenizer,
    switch: str,
    version: str,
    sub_version: str,
    answer: str,
    template_name: str,
    max_new_tokens: int = 200,
    temperature: float = 0.3,
) -> str:
    """Generate suggestions based on the answer"""
    suggestion_question = f"Based on the following information, what are your recommendations?\n{answer[:500]}\nProvide 3-4 specific suggestions."
    prompt = build_inference_prompt(switch, version, sub_version, suggestion_question, template_name)
    suggestions = generate(model, tokenizer, prompt, max_new_tokens, temperature)
    return suggestions


def test_questions(
    model,
    tokenizer,
    template,
    switch,
    version,
    sub_version,
    generate_suggestions: bool = False,
):
    """Test with predefined questions"""
    test_cases = [
        "What is the most common bug in this switch model?",
        "How do I troubleshoot BGP issues?",
        "What firmware version is recommended?",
        "How do I enable high availability?",
        "What are the performance limitations of this model?",
        "How do I configure VLANs on this switch?",
        "What is the maximum packet throughput?",
        "How do I troubleshoot port down issues?",
    ]

    results = []
    
    print(f"\n{'='*80}")
    print(f"Testing on Switch: {switch} | Firmware: {version}.{sub_version} | Template: {template}")
    print(f"{'='*80}\n")

    for i, question in enumerate(test_cases, 1):
        print(f"\n[Test {i}/{len(test_cases)}]")
        print(f"Question: {question}")
        print("-" * 80)

        prompt = build_inference_prompt(switch, version, sub_version, question, template)
        
        # Generate answer
        answer = generate(model, tokenizer, prompt, max_new_tokens=256, temperature=0.1)
        print(f"Answer:\n{answer}\n")

        result = {
            "switch": switch,
            "version": version,
            "sub_version": sub_version,
            "template": template,
            "question": question,
            "answer": answer,
        }

        if generate_suggestions:
            print("Generating suggestions...")
            suggestions = get_suggestions(
                model,
                tokenizer,
                switch,
                version,
                sub_version,
                answer,
                template,
            )
            suggestions = strip_urls(suggestions)
            print(f"Suggestions:\n{suggestions}\n")
            result["suggestions"] = suggestions

        results.append(result)
        print("-" * 80)

    return results


def save_results(results, output_file):
    """Save test results to JSON"""
    with open(output_file, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {output_file}")


def main():
    parser = argparse.ArgumentParser(description="Test inference with answer-only generation")
    parser.add_argument("--base_model", type=str, required=True, help="Base model path")
    parser.add_argument("--adapter_path", type=str, required=True, help="LoRA adapter path")
    parser.add_argument("--template", type=str, default="tinyllama", choices=list(TEMPLATES.keys()), 
                       help="Chat template to use")
    parser.add_argument("--switch", type=str, default="6100", help="Switch model")
    parser.add_argument("--version", type=str, default="10_17", help="Firmware version")
    parser.add_argument("--sub_version", type=str, default="0001", help="Firmware sub-version")
    parser.add_argument("--max_new_tokens", type=int, default=256, help="Max tokens to generate")
    parser.add_argument("--temperature", type=float, default=0.1, help="Temperature for generation")
    parser.add_argument("--output_json", type=str, default="test_results.json", 
                       help="Output JSON file for results")
    parser.add_argument("--questions_file", type=str, default=None,
                       help="Optional JSON file with custom questions")
    parser.add_argument(
        "--with_suggestions",
        action="store_true",
        help="Also generate the optional suggestions field",
    )
    
    args = parser.parse_args()

    print("Loading model and adapter...")
    model, tokenizer = load_model(args.base_model, args.adapter_path)
    print("✓ Model loaded successfully\n")

    # Load custom questions if provided
    test_cases = None
    if args.questions_file and Path(args.questions_file).exists():
        with open(args.questions_file) as f:
            data = json.load(f)
            test_cases = data.get("questions", [])
        print(f"Loaded {len(test_cases)} custom questions from {args.questions_file}\n")

    # Run tests
    results = test_questions(
        model,
        tokenizer,
        args.template,
        args.switch,
        args.version,
        args.sub_version,
        generate_suggestions=args.with_suggestions,
    )

    # Save results
    save_results(results, args.output_json)
    print(f"\n✓ Testing completed! Results saved to {args.output_json}")


if __name__ == "__main__":
    main()
