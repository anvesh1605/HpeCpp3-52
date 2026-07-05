# Metrics Summary

This folder keeps the main evaluation numbers needed for the repo.

## Product LSTM

- Best validation accuracy: `0.9996580027359782`
- Best validation macro F1: `0.7498081350729087`
- Train accuracy: `0.9999572320588487`
- Test accuracy: `0.9996580027359782`
- Test macro precision: `0.7496165644171779`
- Test macro recall: `0.75`
- Test macro F1: `0.7498081350729087`

### Product LSTM labels

- `cli_syntax`
- `concept_explanation`
- `data_not_available`
- `out_of_domain`

## Release Lookup

- Total questions: `322`
- Lookup found: `322`
- Lookup correct: `322`
- Lookup accuracy: `1.0`
- Lookup exact match: `1.0`
- Lookup token F1: `1.0`
- Lookup ROUGE-L: `1.0`

### Release intent accuracy

- `bug_category`: `1.0`
- `bug_scenario`: `1.0`
- `bug_symptom`: `1.0`
- `bug_workaround`: `1.0`
- `release_caveat`: `1.0`

## Qwen Answering

- Qwen used: `322`
- Qwen validation passed: `234`
- Qwen validation failed: `88`
- Final exact match: `0.531055900621118`
- Final token F1: `0.9373190263161308`
- Final ROUGE-L: `0.9371511565830436`

### Answer source counts

- `qwen_grounded`: `234`
- `lookup_fallback`: `88`

## Qwen Formatter

- Formatted correct: `257`
- Formatted exact match: `0.7981366459627329`
- Formatted token F1: `0.9237212018203876`
- Formatted ROUGE-L: `0.9165249115565405`
- Qwen used: `236`
- Qwen skipped: `86`
- Qwen accepted: `66`
- Qwen rejected: `170`

## Curated Test Bundle

- Total cases: `12`
- Good cases: `11`
- Known missing cases: `1`
- Product doc cases: `7`
- Release note cases: `5`
- Syntax cases: `1`

## Useful Repo Metrics To Keep

- Accuracy
- Macro precision
- Macro recall
- Macro F1
- Confusion matrix
- Lookup accuracy
- Lookup exact match
- Qwen validation pass rate
- Final exact match
- Formatted exact match
- Fallback rate

## Notes

- Product LSTM is the intent router.
- Deterministic lookup is the factual source.
- Qwen is a display-only formatter for grounded answers.
- The 5420 case is intentionally kept as a known missing-data example.
