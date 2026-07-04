# Release Notes Pipeline

This folder contains the scripts used to prepare Aruba AOS-CX release-note data for training and repair.

## Included Scripts

- Markdown conversion helpers for raw source files
- Release-note preprocessing scripts
- Release-note postprocessing scripts
- Release-note repair scripts
- Duplicate-question cleanup scripts
- Validation and reporting utilities
- Shared helper modules under `src`

## Pipeline Purpose

The scripts here support the release-notes workflow from raw source material to cleaned training JSONL.

Typical flow:

1. Convert raw PDF or HTML source into Markdown.
2. Run release-note preprocessing to build structured records and Q&A rows.
3. Run postprocessing to apply grounding, deduplication, and caps.
4. Run repair and duplicate-fix steps for final training readiness.

## Intentionally Excluded

This folder does not include:

- large JSONL datasets
- generated outputs
- logs
- model files
- checkpoints
- zip archives
- PDFs or other raw source corpora

The goal is to keep this folder lightweight and source-code only.

