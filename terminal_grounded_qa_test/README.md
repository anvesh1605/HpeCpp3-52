# Terminal Grounded QA Test

This folder contains a separate terminal-only grounded QA experiment for the Aruba QA system.

It does not modify the current backend or frontend.

## Files

- `terminal_grounded_qa.py`
  - Interactive terminal runner.
  - Loads release and product BiLSTM checkpoints.
  - Collects switch family first, then answers repeated questions.
- `config.py`
  - Model paths, dataset paths, allowed switch families, and thresholds.
- `lookup.py`
  - Loads grounded dataset rows from release notes, product docs, the validated product JSONL, and synthetic merged data.
  - Applies hard switch filtering first, then composite-group fallback.
- `entity_extract.py`
  - Extracts switch, version, sub-version, command, topic, and bug ID from the question.
- `qwen_runner.py`
  - Runs Qwen only for formatting grounded non-syntax answers.
  - Falls back to raw `target_value` if Qwen changes important values.

## Behavior

1. Prints the allowed switch families.
2. Requires `Enter switch family:`
3. Before every question, asks for switch context again and lets Enter keep the current one.
4. Uses the selected switch as the first lookup context, then falls back to broader grounded contexts if the selected one has no good answer.
5. Predicts intent with:
   - release BiLSTM
   - product BiLSTM
6. Finds the best grounded `target_value` from the dataset.
7. For CLI syntax questions, including natural phrasing:
   - returns the exact grounded `target_value`
   - bypasses Qwen
8. For grounded explanation / bug / workaround / history style answers:
   - sends the grounded answer to Qwen for formatting only
   - validates the result
   - falls back to original grounded text if important values changed
9. For general non-document questions, like simple math or casual prompts:
   - uses Qwen directly when possible
   - falls back to a small friendly response if Qwen cannot answer

## Run

From `C:\Hpe\Train`:

```powershell
.venv312\Scripts\python.exe .\terminal_grounded_qa_test\terminal_grounded_qa.py
```

Or with your default Python:

```powershell
python .\terminal_grounded_qa_test\terminal_grounded_qa.py
```

## Dependencies

BiLSTM loading requires:

```powershell
pip install torch
```

Qwen formatting requires:

```powershell
pip install transformers accelerate sentencepiece
```

If Qwen cannot load, the script still returns the grounded `target_value`.

## Trained models

The terminal runner uses the latest checkpoints from this workspace:

- Release BiLSTM: `C:\Hpe\Train\outputs_release_lstm\all_switches\best_model.pt`
- Product BiLSTM: `C:\Hpe\Train\outputs_product_lstm\all_switches\best_model.pt`

## Output

For each question the script prints:

- predicted source / intent
- model votes from release and product BiLSTMs
- extracted entities
- matched dataset row
- target value
- final answer

## Safe fallback

If confidence is low or lookup is weak, the script returns:

`No reliable matching answer found in the current dataset.`
