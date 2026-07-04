# Product Docs Build Pipeline

This folder contains only the scripts needed to build the Aruba AOS-CX `full_product_docs` tree from raw documentation through deterministic preprocessing and final cleanup.

## Included

- `convert_with_markitdown_cli.ps1`
- `preprocess_product_docs.py`
- `audit_missing_product_docs.py`
- `rerun_missing_product_docs.py`
- `run_low300_product_docs_stage.py`
- `clean_product_docs_command_headings.py`
- `clean_product_docs_final_artifacts.py`
- Shared helpers under `project/src/`
  - `product_doc_parser.py`
  - `product_doc_qa_generator.py`
  - `product_doc_validator.py`
  - `__init__.py`

## Intentionally excluded

- Ollama repair scripts
- manual repair / pilot scripts
- enhancement / fine-tuning scripts
- monitoring helpers
- full product documentation trees
- Markdown output trees
- PDFs
- large JSONL datasets
- generated outputs
- logs
- model files
- checkpoints
- release-note preprocessing scripts

## Notes

- Code was copied as-is.
- No preprocessing or repair jobs were run during this copy step.
- No logic was changed.
