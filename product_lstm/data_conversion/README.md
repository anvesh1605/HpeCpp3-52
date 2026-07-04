# Product LSTM Data Conversion

This folder contains only the Product Documentation LSTM data-conversion and preparation scripts.

## What this folder does

- Converts product documentation QA rows into LSTM-ready records.
- Prepares rows as `question + intent + target_value`.
- Keeps `target_value` as the factual lookup answer.
- Supports cleanup, weak-row filtering, validation, repair, and split preparation.

## Notes on answers

- `target_value` is the direct factual answer used by the LSTM dataset.
- Qwen/Ollama-formatted answers, when they exist in the source project, are kept separate from this conversion folder.

## Intentionally excluded

- JSONL datasets
- repaired datasets
- generated outputs
- logs
- checkpoints
- trained model files

No training, inference, evaluation, or dataset generation is performed from the files in this folder.
