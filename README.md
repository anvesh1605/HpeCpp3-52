# Aruba AOS-CX QA Assistant

Aruba AOS-CX QA Assistant is a grounded domain-specific question answering system for Aruba networking support content. It is designed to answer queries from **release notes** and **product documentation** using a hybrid architecture built around **fine-tuned Qwen**, **BiLSTM**, **deterministic lookup**, and **validation**.

The system helps users ask questions about:

- release-note bugs and caveats
- CLI syntax and command meaning
- configuration procedures
- troubleshooting steps
- limitations and known issues
- version history and release details
- product concepts and feature explanations

The current runtime flow is:

```text
User Question
-> Frontend UI
-> Backend Runtime
-> Slot Extraction
-> BiLSTM Supporting Module
-> Deterministic Lookup
-> Grounded Answer / target_value
-> Fine-tuned Qwen
-> Validation
-> Final Answer
```

---

## Contents

- Features
- Architecture
- Repository Layout
- Training Flow
- Runtime Flow
- Model Roles
- Main Pipelines
- Prerequisites
- Configuration
- Run Locally
- Deployment / Demo
- Troubleshooting
- Contributors

---

## Features

- Grounded QA assistant for Aruba AOS-CX release notes and product documentation
- Fine-tuned **Qwen** used as the **main final answer generation model**
- **BiLSTM** used as the **supporting module for intent prediction and routing**
- Deterministic lookup used as the **factual source of truth**
- Validation layer to ensure Qwen output preserves technical facts
- Supports questions about:
  - Bug IDs
  - caveats
  - CLI syntax
  - command meanings
  - configuration procedures
  - version history
  - troubleshooting content
- Release-note preprocessing pipeline for training-ready JSONL generation
- Product-documentation preprocessing pipeline for structured QA dataset generation
- LSTM data conversion pipeline for intent training
- Web-based chat interface for live usage and demo

---

## Architecture

### High-Level Architecture

```text
Raw Release Notes                Raw Product Documentation
        |                                   |
        v                                   v
Release Notes Preprocessing        Product Documentation Preprocessing
        |                                   |
        +---------------+-------------------+
                        v
               Clean Final JSONL Datasets
                        |
          +-------------+-------------+
          v                           v
LSTM Data Conversion Pipeline    Qwen Fine-Tuning
          |                           |
          v                           v
BiLSTM Training              Fine-tuned Qwen Model
          |                           |
          v                           v
Saved LSTM Artifacts         Main Final Answer Generation Model
          +-------------+-------------+
                        v
                  Backend Runtime
                        |
         +--------------+--------------+
         v                             v
   Slot Extraction              Frontend / API Flow
         |
         v
 BiLSTM Supporting Module
         |
         v
 Deterministic Lookup
         |
         v
 Grounded Answer / target_value
         |
         v
 Fine-tuned Qwen
         |
         v
 Validation
         |
         v
 Final Answer
```

---

## Repository Layout

```text
.
+-- backend/                  Backend runtime and API orchestration
+-- frontend/                 Frontend chat UI
+-- release_notes_pipeline/   Release-notes preprocessing pipeline
+-- product_docs_pipeline/    Product-documentation preprocessing pipeline
+-- release_lstm/             Release-note BiLSTM utilities
+-- product_lstm/             Product-doc LSTM conversion and training
+-- qwen_training/            Qwen fine-tuning and evaluation utilities
+-- scraper/                  Aruba portal scraping utilities
+-- deploy/                   Deployment and demo setup files
+-- README.md                 Project overview
```

---

## Training Flow

The project has two main offline data sources:

- **Raw Release Notes**
- **Raw Product Documentation**

These are processed separately and then combined into clean training-ready datasets.

### Offline / Training Flow

```text
Raw Release Notes
-> Release Notes Preprocessing Pipeline
-> Clean Final JSONL

Raw Product Documentation
-> Product Documentation Preprocessing Pipeline
-> Clean Final JSONL

Clean Final JSONL
-> LSTM Data Conversion Pipeline
-> BiLSTM Training
-> Saved LSTM Artifacts

Clean Final JSONL
-> Qwen Fine-Tuning
-> Fine-tuned Qwen Model
```

---

## Runtime Flow

At runtime, the system does not directly trust model memory for facts.

Instead:

1. The user sends a question from the frontend
2. The backend extracts slots from the question
3. The BiLSTM supporting module predicts the user intent
4. Deterministic lookup retrieves the factual grounded answer
5. The grounded answer is passed to the fine-tuned Qwen model
6. Qwen generates the final user-facing response
7. Validation checks whether facts are preserved
8. The final answer is shown to the user

---

## Model Roles

### Fine-tuned Qwen
- Main final answer generation model
- Receives grounded answer / `target_value` as input
- Generates the final user-facing response

### BiLSTM
- Supporting module for intent prediction and routing
- Helps identify the query type before answer generation
- Does **not** generate the final answer

### Deterministic Lookup
- Retrieves factual `target_value` / grounded answer
- Acts as the source of truth

### Validation
- Ensures the final Qwen response preserves:
  - Bug IDs
  - versions
  - CLI syntax
  - dates
  - symptoms
  - workaround meaning
  - command names and critical facts

---

## Main Pipelines

## 1. Release Notes Preprocessing

Main flow:

```text
Raw Collection
-> HTML to Markdown
-> Preprocessing
-> Answer Repair
-> Deduplication
-> Validation
-> Final Output
```

What it does:
- collects raw release-note source files
- organizes data by switch / version / sub_version
- converts source HTML to Markdown
- parses known issues, resolved issues, caveats, and version history
- generates grounded QA rows
- repairs weak or malformed rows where needed
- removes duplicates
- validates consistency
- saves clean training-ready JSONL

---

## 2. Product Documentation Preprocessing

Main flow:

```text
Raw PDFs
-> Markdown Conversion
-> Product-Doc Parsing
-> QA Generation
-> Validation & Filtering
-> Answer Repair
-> Final Reports
```

What it does:
- processes Aruba product documentation
- converts PDFs to Markdown
- parses commands, sections, topics, and concepts
- generates chat-style QA rows
- filters duplicates and broken rows
- removes command-heading noise, OCR leftovers, and table artifacts
- produces final reports and dataset summaries

---

## 3. LSTM Data Conversion

What it does:
- converts cleaned JSONL into LSTM-ready data
- builds:
  - intent labels
  - `target_value`
  - slot metadata
- supports both release-note and product-doc question types

Typical slots:
- switch
- version
- sub_version
- bug_id
- command
- feature
- topic

---

## 4. BiLSTM Training

What it does:
- trains BiLSTM on question text
- learns intent prediction and routing behavior
- saves:
  - trained model
  - vocab
  - label encoder
  - inference-ready artifacts

---

## 5. Qwen Fine-Tuning

What it does:
- fine-tunes compact Qwen on grounded Aruba QA data
- uses training-ready chat-style JSONL
- produces the final answer-generation model used at runtime

---

## Prerequisites

For local development:

- Python 3.x
- required Python packages from backend and training utilities
- Node.js and npm
- Git
- prepared local model files if running full inference
- prepared local dataset / lookup artifacts

For demo / deployment:

- frontend and backend configured correctly
- local model and runtime files available
- optional ngrok setup for temporary public sharing

---

## Configuration

Typical runtime components depend on:

- backend configuration
- model paths
- lookup/index paths
- frontend API configuration
- deployment environment values

You should configure:

- backend runtime settings
- frontend API base URL
- local model directories
- lookup artifact locations
- deployment/demo environment values where needed

---

## Run Locally

### 1. Start the backend

Example:

```bash
cd backend
uvicorn main:app --host 0.0.0.0 --port 8010
```

### 2. Start the frontend

Example:

```bash
cd frontend
npm install
npm run dev -- --host 0.0.0.0 --port 3030
```

### 3. Open the frontend

Example local URL:

```text
http://localhost:3030
```

---

## Deployment / Demo

For temporary live demo:

- keep backend running locally
- keep frontend running locally
- expose frontend/backend through ngrok if needed
- ensure local model/data artifacts are available
- keep the machine online during the demo

The repo stores **code and documentation**.  
Large files such as models, outputs, and local runtime datasets should generally remain outside normal Git pushes unless explicitly required.

---

## Troubleshooting

### Wrong syntax or index-like answers shown
- backend should reject TOC/index-style contaminated answers
- deterministic lookup should return only clean grounded answers
- Qwen should not guess syntax from bad lookup text

### Frontend cannot reach backend
- confirm backend is running
- confirm frontend API URL is correct
- check local port configuration

### Model output changes facts
- review validation logic
- ensure lookup remains the factual source
- ensure grounded answer is passed correctly into Qwen

### Stale or incorrect runtime output
- confirm correct model files are loaded
- confirm correct lookup artifacts are available
- restart backend after major configuration changes

---

## Contributors

- Anvesh
- Siddant
- Aaditya
- Srushti
- Joshua

---

## Summary

This project builds a grounded Aruba AOS-CX QA assistant in which:

- **BiLSTM predicts intent**
- **deterministic lookup retrieves the grounded answer**
- **fine-tuned Qwen generates the final answer**
- **validation checks the final response before it is shown to the user**

## License

This project was developed for **Hewlett Packard Enterprise (HPE)** as part of an internal project.

Licensing, usage, distribution, and access rights are subject to **HPE internal policies**.