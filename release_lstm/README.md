# Release LSTM

This folder contains the Release Notes LSTM scripts for the `aruba-qa-assistant` repo.

## What it does

- The LSTM predicts release-note intent and routing.
- Deterministic lookup remains the factual source of truth.
- Qwen is only used to format the already-retrieved lookup answer.

## Files included

- release-note LSTM training
- release-note LSTM inference
- release-note LSTM utilities
- release-note deterministic lookup helpers
- release-note runtime and formatter helpers

## Intentionally excluded

This folder does not include:

- datasets
- trained model files
- checkpoints
- logs
- generated outputs
- backend API files
- frontend files
- product-documentation scripts
- Qwen fine-tuning scripts

## Notes

- No logic was changed while copying these files.
- No training or inference was run as part of this copy.
