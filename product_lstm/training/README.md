# Product LSTM Training Scripts

This folder contains the Product Documentation LSTM training, evaluation, and inference scripts copied from the local project.

## What this folder is for

- Train the Product LSTM intent classifier
- Evaluate the Product LSTM model
- Run Product LSTM inference
- Keep the Product LSTM utility code used by the training and evaluation flow

## What Product LSTM does

- Predicts product-documentation intent only
- Does not generate final user answers
- Provides intent classification signals for the downstream QA pipeline

## Answer flow in the full system

- Deterministic lookup retrieves the factual `target_value`
- Qwen or Ollama formats the final user-facing answer
- The LSTM is a supporting model for routing and intent prediction

## Files intentionally excluded from GitHub

- JSONL datasets
- Trained model files
- Tokenizer pickles
- Label encoder pickles
- Output reports
- Checkpoints
- Logs
- Product-doc repair scripts
- Product-doc dataset conversion scripts
- Backend files
- Frontend files

## Notes

- The scripts were copied without changing logic.
- Shared LSTM runtime dependencies are kept in the repo separately and were not modified here.
