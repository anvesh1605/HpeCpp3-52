# Product LSTM

This folder contains the Product Documentation LSTM scripts copied from the current project for use in `aruba-qa-assistant`.

## Folder Purpose

These scripts support the product-documentation LSTM pipeline:
- deterministic conversion from product QA/chat rows into LSTM-ready JSONL
- cleanup and repair of noisy product rows
- validation and inference-suite preparation
- Ollama-based repair for uncertain product rows

## Product LSTM Flow

Typical flow:
1. Convert product documentation into structured LSTM rows.
2. Clean extraction artifacts and normalize answers.
3. Move uncertain rows into review.
4. Repair safe review rows with Ollama when needed.
5. Validate the final dataset and prepare inference/evaluation support files.

## How It Differs From Release LSTM

- Product LSTM focuses on product documentation QA, not release notes.
- It includes cleanup and repair logic for CLI, concept, event-log, SNMP, troubleshooting, requirement, caveat, and limitation rows.
- Release LSTM scripts stay separate because their intent set, review rules, and repair logic are different.

## Intentionally Excluded

This folder does not include:
- trained model files
- checkpoints
- patched full datasets
- generated outputs
- logs
- evaluation results
- inference outputs

## Notes

- No logic was changed while copying these files.
- No patching, training, or evaluation was run as part of this copy.
