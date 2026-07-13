# End-to-End Product LSTM Data Preparation

This guide explains how release-notes and product-documentation data move from raw `train_chat.jsonl` rows into the final LSTM-ready dataset used in the current repo.

It focuses on the exact scripts in this repo, how each script changes the row, and where each important snippet lives in the source file.

## What This Pipeline Does

The pipeline does four things:

1. Reads release-note or product-doc QA rows from `train_chat.jsonl`.
2. Detects intent, extracts slots, and cleans noisy text.
3. Moves weak or uncertain rows to review instead of forcing bad training data.
4. Converts the accepted rows into the final compact LSTM schema.

The important rule throughout the pipeline is simple:

- keep technical tokens exact
- clean only obvious extraction noise
- do not invent commands, versions, Event IDs, bug IDs, or procedures
- move uncertain rows to review instead of training on them

## Why Release Notes and Product Docs Look Similar

Both data types follow the same overall path:

- raw QA row in
- intent detection
- slot extraction
- deterministic cleanup
- review routing for weak rows
- optional Ollama repair for safe review rows
- validation
- final LSTM conversion

The difference is mostly in the intent map and the answer formatting:

- release notes focus on bugs, version history, caveats, compatibility, supported products, and upgrade/downgrade guidance
- product docs focus on CLI syntax, CLI meaning, event logs, procedures, concepts, SNMP MIBs, troubleshooting, requirements, caveats, and limitations

## End-to-End Data Flow

```text
raw release_notes or product_docs train_chat.jsonl
  -> convert_product_docs_simple_lstm.py
  -> convert_product_docs_pipeline.py
  -> cleanup_product_conversion.py
  -> cleanup_product_docs_final.py
  -> repair_product_docs_ollama_tree.py
  -> validate_dataset.py
  -> convert_product_docs_all_switches.py
  -> convert_lstm_dataset.py
  -> repair_dataset.py
  -> prepare_clean_inference_suite.py
  -> run_clean_pilot1000.ps1
  -> run_clean_checkpoint_selection.ps1
```

For bulk runs, `convert_product_docs_all_switches.py` mirrors the original switch/version tree and creates per-folder outputs, then merges them into all-switch summaries.

## Script Map With Line Numbers

| Script | Key source lines | Role in the flow |
|---|---:|---|
| `convert_product_docs_simple_lstm.py` | `16-306`, `518-561` | Simple one-file product-doc conversion |
| `convert_product_docs_pipeline.py` | `113-129`, `163-245`, `299-380`, `946-1060`, `1284-` | Main deterministic release-notes and product-doc pipeline |
| `convert_product_docs_all_switches.py` | `95-146`, `190-278`, `281-340` | Bulk runner for all switch/version folders |
| `cleanup_product_conversion.py` | `59-89`, `526-655`, `903-` | Deterministic cleanup and review routing |
| `cleanup_product_docs_final.py` | `21-44`, `621-` | Strict final cleanup pass |
| `repair_product_docs_ollama_tree.py` | `28-29`, `194-290`, `431-` | Ollama repair for review rows only |
| `validate_dataset.py` | `53-110`, `222-` | Validation gate before training |
| `convert_lstm_dataset.py` | `179-245`, `248-438`, `464-616`, `619-711` | Final compact LSTM schema builder for both release notes and product docs |
| `repair_dataset.py` | `23-29`, `266-364`, `592-743` | Split builder and fact grouping |
| `prepare_clean_inference_suite.py` | `26-137` | Balanced inference suite builder |
| `run_clean_pilot1000.ps1` | `1-101` | Training launch script |
| `run_clean_checkpoint_selection.ps1` | `1-120` | Checkpoint scoring and selection |

The line numbers above are from the current checked-in files in this repo.

## How Data Travels Through the Pipeline

Think of one row as a package that passes through a series of checkpoints:

1. The row is read from JSONL.
2. The assistant/question and answer are extracted.
3. The row is classified into an intent.
4. Switch, version, command, topic, Event ID, or other slots are preserved.
5. The answer is cleaned only if it still means the same thing.
6. If the row looks weak, generic, or unsafe, it is moved to review.
7. Accepted rows are written as clean dataset rows.
8. Later scripts re-clean, validate, split, and prepare training inputs.
9. The final schema is converted into the LSTM-ready output.

The next sections show that flow script by script.

## Script 1: `convert_product_docs_simple_lstm.py`

Source lines:

- intent helpers and regexes: `16-184`
- target cleanup and slot building: `187-306`
- CLI entry point: `518-561`

Representative snippet:

```python
if family in {"cli_command_reference", "show_command_reference"} or source_type == "product_cli_reference" or command:  # detect CLI-style rows
    if is_show_command(command, question, answer) or family == "show_command_reference":  # detect show-command rows
        ...  # choose show-command handling
    if has_syntax_signal(question):  # question asks for syntax
        return "cli_syntax"  # label as syntax intent
    if has_meaning_signal(question):  # question asks for meaning
        return "cli_meaning"  # label as meaning intent

slots["switch"] = collapse(row.get("switch"))  # preserve switch model
slots["version"] = display_version(row.get("version"))  # normalize version format
```

What it does:

- detects whether the row is CLI syntax, CLI meaning, show-command syntax, or show-command meaning
- preserves switch and version exactly
- extracts the command from the row if it is present
- produces the first simple LSTM-style row structure for one file

How the data travels:

- raw row in
- question/answer extracted
- intent selected
- slots filled
- target cleaned
- final row written or review row created

This script is the simplest version of the conversion logic. It is useful for pilots and isolated file tests, especially when you want to inspect one release-notes file or one product-doc file at a time.

## Script 2: `convert_product_docs_pipeline.py`

Source lines:

- extraction and domain detection: `163-194`
- product intent logic: `299-365`
- main row processing loop: `946-1060`
- entry point: `1284-`

Representative snippet:

```python
question, answer = extract_qa(row)  # pull the raw question and answer
intent = intent_from_row(row, question, answer)  # detect the product intent
slots = build_slots(intent, row, question, answer)  # preserve structured metadata
input_text = build_input_text(intent, row, question, answer)  # build the model prompt
target_value, noise_applied = clean_target_value(intent, raw_target)  # remove safe noise
```

What it does:

- reads one source file and processes it row by row
- keeps only `product_docs` rows
- classifies the row into a product intent
- builds the input prompt text used by the dataset
- cleans the answer in a deterministic way
- sends weak or broken rows to review

How the data travels:

- `extract_qa` pulls the user/assistant pair
- `source_domain` verifies the row belongs to product docs
- `intent_from_row` decides the intent
- `build_slots` preserves metadata
- `build_input_text` normalizes the question text into the final prompt style
- `clean_target_value` removes obvious prefixes and noise
- the row is either written to dataset or sent to review

This is the main single-file deterministic pipeline. It handles the common logic for both release notes and product docs, then branches by intent.

## Script 3: `convert_product_docs_all_switches.py`

Source lines:

- input discovery and per-file execution: `95-146`
- merged all-switch output builder: `190-278`
- CLI and worker control: `281-340`

Representative snippet:

```python
discovered = sorted(path for path in input_root.rglob("train_chat.jsonl") if path.is_file())  # find every input file
with ProcessPoolExecutor(max_workers=workers) as executor:  # run per-file conversions in parallel
    ...  # submit and collect worker results
write_jsonl(output_root / "all_switches_product_dataset.jsonl", clean_rows)  # merged clean rows
write_jsonl(output_root / "all_switches_product_review.jsonl", review_rows)  # merged review rows
```

What it does:

- finds every `train_chat.jsonl` under the input root
- runs the conversion in parallel
- preserves the original switch/version folder tree
- writes per-folder outputs
- merges all per-folder outputs into all-switch files

How the data travels:

- one file per switch/version is converted independently
- each converted folder keeps its own dataset, review file, report, and sample file
- the merged pass then reads all of those outputs and creates a single consolidated dataset

This is the script that turns a directory tree into a mirrored output tree.

## Script 4: `cleanup_product_conversion.py`

Source lines:

- artifact fixes: `59-89`
- target cleanup and review logic: `526-655`
- entry point: `903-`

Representative snippet:

```python
COMMON_ARTIFACT_FIXES = {
    "pingsnetworkhosts": "pings network hosts",  # fix merged words
    "currentworkingdirectory": "current working directory",  # restore spacing
    "thenumberofpackets": "the number of packets",  # restore token boundaries
}  # common deterministic artifact map

def clean_target_value(row: Mapping[str, Any]) -> Tuple[str, Dict[str, int]]:  # normalize the answer text
    ...  # apply cleanup and decide whether the row is safe
```

What it does:

- fixes obvious PDF-extraction corruption
- normalizes broken spacing and merged words
- keeps technical tokens intact
- moves weak or generic rows to review

How the data travels:

- accepted rows from the first conversion pass go in
- the cleaner normalizes only the obvious artifacts
- rows that still look too weak or too generic go to review
- the cleaned row is kept only if it is still safe for training

This script is one of the main “make it cleaner, but do not change the fact” stages.

## Script 5: `cleanup_product_docs_final.py`

Source lines:

- final cleanup rules: `21-44`
- entry point: `621-`

Representative snippet:

```python
EVENT_BAD_RE = re.compile(
    r"(?i)(?:Description:\s*Event ID|Information\s+Information|Warning\s+Warning|Error\s+Error|Severity:\s*<log>|\b<log>\b)"
)  # detect event-log boilerplate and placeholder noise

def collapse(value: Any) -> str:  # flatten whitespace and simple extraction noise
    ...  # produce a compact cleaned string
```

What it does:

- catches event-log and template noise
- strips repeated headings and bad extraction fragments
- performs the strict final cleanup pass before validation

How the data travels:

- rows already cleaned once are checked again
- event-log boilerplate and repeated “bad” patterns are removed
- final rows become more uniform before validation or repair

This script is the last deterministic cleanup gate before training-facing data is trusted.

## Script 6: `repair_product_docs_ollama_tree.py`

Source lines:

- allowed repair reasons: `28-29`
- prompt generation and model call: `194-290`
- main orchestration: `431-`

Representative snippet:

```python
def ollama_prompt(row: Mapping[str, Any]) -> str:  # build the strict repair prompt
    ...  # embed the row and repair rules
    "Preserve CLI commands exactly.\n"  # do not alter command text
    "Preserve Event IDs exactly.\n"  # do not alter Event IDs
    "Preserve AOS-CX versions exactly.\n"  # do not alter versions

def run_ollama(row: Mapping[str, Any], model: str, fallback_model: str) -> Tuple[Optional[Dict[str, Any]], str]:  # call local Ollama
    proc = subprocess.run(["ollama", "run", model], ...)  # run the formatter/repair model
```

What it does:

- repairs only review rows, never the already-clean rows
- sends the row to Ollama with a strict repair prompt
- validates the returned JSON
- rejects bad or unsafe repairs

How the data travels:

- review row in
- Ollama suggests a repair
- validation checks confidence, target text, command preservation, and Event ID preservation
- accepted repairs go into the repaired dataset
- rejected rows remain in review remaining

This script is intentionally narrow. It is not a general rewrite stage.

## Script 7: `validate_dataset.py`

Source lines:

- validation logic: `53-110`
- CLI entry point: `222-`

Representative snippet:

```python
if is_cli_row(row):
    command = command_value(row)  # recover the CLI command
    syntax = syntax_value(row)  # recover the exact syntax text
    if is_syntax_question(question):  # verify syntax-question alignment
        expected = f"Syntax: {syntax}"  # exact syntax answer required
        ...  # compare and report mismatches
```

What it does:

- checks that required fields are present
- verifies exact syntax answers where syntax is expected
- ensures CLI metadata is normalized
- rejects corruption that slipped through earlier stages

How the data travels:

- cleaned dataset rows are read
- each row is checked against the rules for its intent
- any mismatch is reported before the dataset is considered final

This is the last safety check before the clean data is trusted.

## Script 8: `convert_lstm_dataset.py`

Source lines:

- source/intent definitions: `179-245`
- product intent and answer cleanup: `248-438`
- fact key and final row construction: `464-616`
- file conversion and entry point: `619-711`

Representative snippet:

```python
domain = source_domain(row)  # choose release_notes or product_docs
intent = detect_intent(row, question, answer)  # map the row to an LSTM intent
answer_type = answer_type_for_intent(intent)  # map to the compact answer label
target_value = clean_target_value(intent, row, question, answer)  # normalize the factual answer
slots = {  # keep the important metadata
    "switch": collapse(row.get("switch")) or None,  # switch model
    "version": display_version(row.get("version")) or None,  # AOS-CX version
    "command": command_value(row) or None,  # command when relevant
}
record = {  # final LSTM-ready output row
    "input_text": clean_question(question, row),  # normalized prompt text
    "labels": {"intent": intent, "source_domain": domain, "answer_type": answer_type},  # training labels
    "slots": slots,  # structured metadata
    "fact_key": build_fact_key(row, intent, answer_type, question, answer),  # dedupe / grouping key
    "target_value": target_value,  # factual answer content
    "answer_template": answer_template_for_intent(intent),  # answer style used later
    "final_answer": final_answer_for_intent(intent, target_value, row, question),  # rendered answer text
}
```

What it does:

- converts both release notes and product docs into the final compact LSTM schema
- preserves source domain and intent
- preserves switch, version, sub_version, command, bug ID, and Event ID where needed
- builds a stable `fact_key`
- formats the final answer using an intent-specific template

How the data travels:

- the cleaned product row comes in
- the domain and intent are detected again at the final schema layer
- the answer is normalized into `target_value`
- slots are copied forward
- the final LSTM record is emitted

This is the script that turns the cleaning pipeline into actual training-ready JSONL records for both release notes and product docs.

## Script 9: `repair_dataset.py`

Source lines:

- split filenames and default inputs: `23-29`
- fact grouping: `266-364`
- JSONL I/O and entry point: `592-743`

Representative snippet:

```python
DEFAULT_INPUTS = (
    Path("Data/all_switches/train_chat_all_clean_validated.jsonl"),  # cleaned training rows
    Path("Data/all_switches/val_chat_all_clean.jsonl"),  # cleaned validation rows
    Path("Data/all_switches/test_chat_all_clean.jsonl"),  # cleaned test rows
)

SPLIT_FILENAMES = {  # standard split file names
    "train": "train_chat_all_clean.jsonl",  # train split
    "validation": "val_chat_all_clean.jsonl",  # validation split
    "test": "test_chat_all_clean.jsonl",  # test split
}
```

What it does:

- defines the cleaned train/validation/test split files
- groups rows by fact so duplicate facts do not leak across splits
- preserves the cleaned data while preparing split-specific files

How the data travels:

- cleaned rows are grouped by fact key
- the script prepares stable split files
- later evaluation and training use these exact files

This script is what turns cleaned rows into reproducible training splits.

## Script 10: `prepare_clean_inference_suite.py`

Source lines:

- inference quotas and category logic: `26-61`
- suite preparation: `68-138`

Representative snippet:

```python
QUOTAS = {  # balanced evaluation budget by category
    "cli_syntax": 20,  # syntax-heavy rows
    "cli_description": 15,  # descriptive CLI rows
    "cli_negative": 5,  # unsupported CLI examples
    "release_notes_bug": 20,  # bug-related rows
    "version_history": 10,  # version-history rows
    "event_log": 10,  # event-log rows
    "concept": 10,  # concept questions
    "other": 10,  # remaining rows
}
```

What it does:

- builds a balanced inference suite
- keeps the test suite fact-group-disjoint from training and validation
- caps categories so the suite is not dominated by one intent

How the data travels:

- cleaned split files are read
- rows are categorized
- a balanced sample is selected
- the manifest is written with file hashes

This script helps evaluation stay balanced and reproducible.

## Script 11: `run_clean_pilot1000.ps1`

Source lines:

- launcher setup and GPU pinning: `1-22`
- training arguments: `23-52`
- process launch and logs: `61-101`

Representative snippet:

```powershell
$arguments = @(  # build the trainer command line
    $trainScript,  # training entry script
    "--data_path", "final_json_clean\all_switches\train_chat_all_clean.jsonl",  # train dataset
    "--val_data_path", "final_json_clean\all_switches\val_chat_all_clean.jsonl",  # validation dataset
    "--model_name", "Qwen/Qwen2.5-3B-Instruct",  # base model
    "--template", "chatml",  # chat formatting
    "--output_dir", "outputs_final\qwen25_3b_clean_pilot1000"  # output directory
)
```

What it does:

- launches the pilot training run
- pins the GPU by UUID
- redirects stdout, stderr, and GPU telemetry into logs
- records launch and completion metadata

How the data travels:

- training does not change the source dataset
- it reads the cleaned train/val files
- it writes model outputs and logs separately

This script is the handoff from prepared data to actual model training.

## Script 12: `run_clean_checkpoint_selection.ps1`

Source lines:

- preflight and checkpoint checks: `1-49`
- per-suite evaluation: `52-98`
- checkpoint selection call: `100-120`

Representative snippet:

```powershell
$results["${label}:clean_balanced100"] = Invoke-Suite $label $adapter "clean_balanced100" $suite 100  # evaluate on balanced suite
$results["${label}:legacy50_regression"] = Invoke-Suite $label $adapter "legacy50_regression" $legacy 50  # evaluate regression suite
```

What it does:

- scores multiple checkpoints against the balanced inference suite
- also checks a legacy regression suite
- selects the best epoch without changing the data

How the data travels:

- trained adapters are loaded
- inference is run on held-out evaluation sets
- metrics are collected
- the best checkpoint is selected

This is the post-training evaluation and selection stage.

## Sample Walkthrough: Product Docs

Here is one concrete product-doc example showing how data moves through the pipeline.

### Raw input row

```json
{
  "source_type": "product_cli_reference",
  "data_family": "cli_command_reference",
  "switch": "4100i",
  "version": "10_09",
  "command": "pwd",
  "question": "For 4100i AOS-CX 10.09, what does the pwd command do?",
  "answer": "The pwd command displays the currentworkingdirectory."
}
```

### Stage 1: question and answer extraction

`convert_product_docs_pipeline.py:163-175` and `convert_lstm_dataset.py:168-176` read the user/assistant pair from the row.

The row already has direct `question` and `answer` fields, so the scripts do not need to reconstruct them from messages.

### Stage 2: domain and intent detection

`convert_lstm_dataset.py:179-245` and `convert_product_docs_pipeline.py:248-286` decide that this is a product-doc CLI row.

Why it becomes `cli_meaning`:

- the text says “what does”
- the row has a command
- the data family is CLI reference

### Stage 3: slot preservation

`convert_product_docs_simple_lstm.py:241-286`, `convert_product_docs_pipeline.py:334-365`, and `convert_lstm_dataset.py:578-586` preserve the important metadata:

- switch: `4100i`
- version: `10.09`
- command: `pwd`
- topic: `pwd`

This is where the row keeps its identity.

### Stage 4: answer cleaning

The answer text contains a PDF-spacing artifact:

- `currentworkingdirectory`

`cleanup_product_conversion.py:59-89` normalizes common artifacts like that.

`cleanup_product_docs_final.py:21-44` performs a stricter final cleanup pass.

After cleanup, the answer becomes:

```text
The pwd command displays the current working directory.
```

### Stage 5: review check

`convert_product_docs_pipeline.py:289-306` and `convert_lstm_dataset.py:452-461` check whether the row is empty, generic, placeholder-only, or otherwise unsafe.

This sample survives because:

- it has a real command
- it has a real explanation
- it preserves switch/version/command
- it is not generic filler

### Stage 6: final LSTM row

`convert_lstm_dataset.py:529-599` turns the row into the final compact record:

```json
{
  "input_text": "For 4100i AOS-CX 10.09, what does the pwd command do?",
  "labels": {
    "intent": "cli_meaning",
    "source_domain": "product_docs",
    "answer_type": "cli_meaning"
  },
  "slots": {
    "switch": "4100i",
    "version": "10.09",
    "command": "pwd",
    "topic": "pwd"
  },
  "fact_key": "product_docs|4100i|10.09||cli_meaning|pwd|cli_meaning",
  "target_value": "The pwd command displays the current working directory.",
  "answer_template": "{target_value}",
  "final_answer": "The pwd command displays the current working directory."
}
```

### Step-by-step comments for the sample

```python
question = "For 4100i AOS-CX 10.09, what does the pwd command do?"  # asks for command meaning
command = "pwd"  # the exact CLI command
version = "10.09"  # preserve version exactly
switch = "4100i"  # preserve switch model exactly
target_value = "The pwd command displays the current working directory."  # cleaned factual answer
```

### What happened to the row

- It started as a raw product-doc QA row.
- It was classified as a CLI meaning question.
- Its command and version were preserved.
- Its target text was cleaned.
- It passed the safety checks.
- It became a training-ready LSTM row.

## Sample Walkthrough: Release Notes

Here is a release-notes example showing the same shared flow with a different intent family.

### Raw input row

```json
{
  "source_type": "release_notes_compatibility",
  "data_family": "release_notes",
  "switch": "10000",
  "version": "10.13",
  "sub_version": "0005",
  "question": "For 10000 AOS-CX 10.13.0005, what compatibility information is documented?",
  "answer": "Compatibility information: This release is compatible with Aruba Central and AOS-CX 10.13 feature updates."
}
```

### Stage 1: intent detection

`convert_lstm_dataset.py:207-245` maps `release_notes_compatibility` to `release_compatibility`.

That means:

- this is a release-notes row
- the intent is compatibility-related
- the row should not be forced into a generic bucket

### Stage 2: slot preservation

`convert_lstm_dataset.py:464-490` and `convert_lstm_dataset.py:578-599` preserve:

- switch: `10000`
- version: `10.13`
- sub_version: `0005`
- topic/fact key: derived from the release-note topic or hash

### Stage 3: answer shaping

`convert_lstm_dataset.py:332-347` gives the release-note answer template:

```text
Compatibility information: {target_value}
```

The cleaned target value keeps the documented compatibility statement and does not turn it into a generic answer.

### Stage 4: final release-note LSTM row

```json
{
  "input_text": "For 10000 AOS-CX 10.13.0005, what compatibility information is documented?",
  "labels": {
    "intent": "release_compatibility",
    "source_domain": "release_notes",
    "answer_type": "compatibility"
  },
  "slots": {
    "switch": "10000",
    "version": "10.13",
    "sub_version": "0005",
    "topic": "compatibility"
  },
  "fact_key": "release_notes|10000|10.13|0005|compatibility|compatibility|compatibility",
  "target_value": "This release is compatible with Aruba Central and AOS-CX 10.13 feature updates.",
  "answer_template": "Compatibility information: {target_value}",
  "final_answer": "Compatibility information: This release is compatible with Aruba Central and AOS-CX 10.13 feature updates."
}
```

### What happened to the row

- It started as a raw release-note QA row.
- It was classified as a compatibility intent.
- Its switch, version, and sub-version were preserved.
- The compatibility statement was kept factual and specific.
- It became a training-ready LSTM row.

## Why Review Rows Exist

Some rows are not safe to train on immediately. They are moved to review when they are:

- too generic
- empty
- missing a command where a command is required
- corrupted by extraction noise
- missing a markdown match
- too long or too noisy to trust
- likely to change meaning if auto-repaired

This is deliberate. The goal is to protect the training set from weak or fabricated answers.

## What Is Preserved

Across the pipeline, the following are preserved exactly whenever they appear:

- CLI commands
- switch names
- AOS-CX versions
- sub-versions
- Bug IDs
- Event IDs
- product names
- VRF
- VSX
- VLAN
- IPv4 / IPv6
- SNMP OIDs
- placeholders such as `<VLAN-ID>`, `<VRF-NAME>`, and `<IP-ADDR>`

## Final Output Path

The final cleaned conversion path is:

```text
raw train_chat.jsonl
  -> deterministic conversion
  -> cleanup
  -> review separation
  -> optional Ollama repair for review rows
  -> validation
  -> final LSTM JSONL
  -> split preparation
  -> training and checkpoint selection
```

## Short Version for a Slide

If you need a one-slide summary, use this:

1. Read raw product-doc `train_chat.jsonl`.
2. Detect intent and extract slots.
3. Clean extraction noise and route weak rows to review.
4. Repair only safe review rows with Ollama.
5. Validate the accepted rows.
6. Convert the clean rows into final LSTM JSONL.
7. Build train/val/test splits and the balanced inference suite.
8. Run training and select the best checkpoint.

If you want, I can also turn this into a shorter presentation-friendly version with a 6-box flow diagram and speaker notes.
