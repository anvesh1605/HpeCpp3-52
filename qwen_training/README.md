# Qwen / LLM Fine-Tuning Scripts

This folder contains the scripts used for Qwen and other local LLM fine-tuning / evaluation work in this repo.

## Expected input data

Typical inputs are JSONL training and evaluation splits built from the Aruba release-notes and switch training corpora, for example:

- `Data/all_switches/...`
- `Data/final_json/...`
- `Data/product_docs/full_product_docs/...` only when a specific training script explicitly calls for it

Large datasets are not committed here.

## Expected outputs

These scripts usually write:

- LoRA / QLoRA adapters
- training metrics and evaluation metrics
- inference review files
- checkpoint folders
- temporary logs and run manifests

Those outputs are intentionally excluded from GitHub.

## Excluded from this folder

Do not add:

- datasets
- model weights
- adapters
- checkpoints
- logs
- wandb runs
- generated outputs

## Notes

The scripts are copied here without logic changes so the GitHub repo can track the training and evaluation code separately from the larger workspace.
