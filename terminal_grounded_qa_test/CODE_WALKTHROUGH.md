# Terminal Grounded QA Walkthrough

This document explains the end-to-end flow inside `terminal_grounded_qa_test/`.
It covers:

- what each file does
- what each important function does
- how data moves from a user question to the final answer
- where switch context, lookup, and Qwen formatting happen

## High-Level Picture

The folder is a terminal-only grounded QA pipeline. It is not the training code.
It consumes:

- release-note BiLSTM checkpoints
- product BiLSTM checkpoints
- grounded dataset rows from release notes, product docs, synthetic rows, and manual overrides
- a fine-tuned Qwen model for answer formatting and general fallback

## Flow In Order

### 1. Data collection and validation

This is where the training data is gathered, cleaned, split, and validated before the checkpoints are created.

The main training sources are:

- `Data/Release_Notes`
- `Data/product_docs_final`
- `Data/product_docs_final_repaired`
- `Data/aruba_aoscx_product_documentation_dataset_hpe_validated.jsonl`
- `Data/product_docs_final_repaired/manual_grounding_overrides.jsonl`
- `imporved_data_addition/`

The important training steps are:

1. Read raw JSONL rows.
2. Normalize questions, slots, and target values.
3. Reject bad or duplicate rows.
4. Convert raw rows into a training record structure.
5. Split the records into train, validation, and test sets.
6. Validate during training and keep the best checkpoint by validation macro F1.
7. Write reports, confusion matrices, and sample predictions.

### 2. Training

The BiLSTM training scripts build the checkpoints that the terminal app loads later.

Training happens through:

- [`train_lstm_gpu.py`](../train_lstm_gpu.py)
- [`train_release_lstm.py`](../train_release_lstm.py)
- [`train_product_lstm.py`](../train_product_lstm.py)

In short:

- `train_lstm_gpu.py` holds the shared conversion and training engine.
- `train_release_lstm.py` trains release-note data.
- `train_product_lstm.py` reuses the same engine with product-specific intents and data paths.

### Training Code Snippets

These are the key snippets to show when explaining how the training side works.

#### Shared record collection

```python
def collect_records(data_paths: Sequence[Path]) -> Tuple[List[Dict[str, object]], Dict[str, int], int]:
    records: List[Dict[str, object]] = []  # final cleaned rows that will train the model
    reasons: Counter[str] = Counter()  # counts why rows were dropped
    scanned = 0  # total raw lines seen across all files
    seen = set()  # dedupe key store

    for root in data_paths:  # loop over each configured data root
        for path in _iter_jsonl_paths(root):  # expand folders into JSONL files
            ...
            record, reason = row_to_record(row, str(path), line_no, context)  # convert raw row into training format
            if reason is not None:  # skip rows that failed validation
                reasons[reason] += 1  # keep a reason count for reporting
                continue
            key = (  # build a stable dedupe key
                normalize_text(record["input_text"]),
                normalize_text(record["intent"]),
                normalize_text(record["target_value"]),
            )
            if key in seen:  # drop exact duplicate training rows
                reasons["duplicate"] += 1
                continue
            seen.add(key)  # remember the row so it is not reused
            records.append(record)  # keep the cleaned row
```

What this does:

- walks every input JSONL source
- converts raw rows into a consistent training record shape
- removes malformed rows and duplicates
- counts why rows were filtered out so you can audit data quality later

Why it matters:

- this is the first gate before any training happens
- if the data is noisy here, the model learns noisy behavior
- the filter counts in `training_report.json` come from this stage

#### Train / validation / test split

```python
def split_by_intent(records: Sequence[Dict[str, object]], seed: int):
    rng = random.Random(seed)  # fixed seed so the split is reproducible
    by_intent: Dict[str, List[Dict[str, object]]] = defaultdict(list)  # bucket rows by label
    for record in records:  # walk all cleaned records
        by_intent[str(record["intent"])].append(dict(record))  # group by intent

    train: List[Dict[str, object]] = []  # training subset
    val: List[Dict[str, object]] = []  # validation subset
    test: List[Dict[str, object]] = []  # test subset

    for intent in SELECTED_INTENTS:  # preserve class coverage for every label we care about
        group = by_intent.get(intent, [])  # get all rows for one intent
        rng.shuffle(group)  # shuffle within that intent only
        ...
        train.extend(group[:n_train])  # put the main portion into train
        val.extend(group[n_train : n_train + n_val])  # reserve validation rows
        test.extend(group[n_train + n_val : n_train + n_val + n_test])  # reserve test rows
```

What this does:

- groups rows by intent
- shuffles each intent group with a fixed seed
- splits each intent into train, validation, and test parts

Why it matters:

- the split stays balanced across labels instead of being random across the full dataset
- this makes validation more trustworthy
- small intents do not get lost in the split

#### Validation and best checkpoint selection

```python
for epoch in range(1, args.epochs + 1):
    train_loss = train_epoch(model, train_loader, criterion, optimizer, device)  # update weights on train data
    val_loss, val_report, val_matrix, y_true, y_pred, confidences = evaluate(
        model, val_loader, criterion, label_names, device  # measure performance on held-out validation rows
    )

    macro_f1 = float(val_report["macro_f1"])  # compare model quality using macro F1
    if macro_f1 > best_val_macro_f1:  # keep only the best validation checkpoint
        best_val_macro_f1 = macro_f1  # update best validation score
        best_epoch = epoch  # remember which epoch won
        best_state = deepcopy(model.state_dict())  # snapshot model weights
```

What this does:

- trains one epoch
- runs validation after that epoch
- measures macro F1 on the validation set
- saves the model weights only when validation improves

Why it matters:

- the checkpoint is selected by validation quality, not just training loss
- this prevents overfitting from becoming the saved model
- `best_model.pt` is the best validation checkpoint, not necessarily the last epoch

#### Product training overrides

```python
base.SELECTED_INTENTS = PRODUCT_INTENTS  # replace release labels with product labels
base.INTENT_ALIAS_MAP = PRODUCT_INTENT_ALIAS_MAP  # allow product intent aliases
base.NEGATIVE_SAMPLE_ROWS = PRODUCT_NEGATIVE_ROWS  # use product-specific negatives
base.DEFAULT_DATA_PATHS = [  # product training data sources
    Path(r"C:\Hpe\Train\Data\product_docs_final_repaired\manual_grounding_overrides.jsonl"),  # corrected manual examples
    Path(r"C:\Hpe\Train\Data\product_docs_final_repaired"),  # repaired product corpus
    Path(r"C:\Hpe\Train\Data\product_docs_final"),  # original product corpus
    Path(r"C:\Hpe\Train\imporved_data_addition"),  # synthetic merged rows
    Path(r"C:\Hpe\Train\Data\aruba_aoscx_product_documentation_dataset_hpe_validated.jsonl"),  # validated product JSONL
]
```

What this does:

- tells the shared trainer to use product-specific labels
- points the trainer at the product data sources
- includes the manual override file and validated JSONL in the product corpus

Why it matters:

- this is why the product checkpoint behaves differently from the release checkpoint
- the product model learns from product-doc questions, not release-note questions
- changing these paths changes the actual training corpus

### Snippet Line Map

Use these line numbers when you want to point to the exact source block in the code:

| Snippet | Source file lines |
| --- | --- |
| Shared record collection | `train_release_lstm.py:306` and `train_release_lstm.py:373` |
| Train/validation/test split | `train_lstm_gpu.py:429` |
| Validation and best checkpoint selection | `train_lstm_gpu.py:560` and `train_lstm_gpu.py:589` |
| Product training overrides | `train_product_lstm.py:1` |
| Question parsing | `entity_extract.py:211` |
| Intent prediction | `terminal_grounded_qa.py:139` |
| Source choice and answer routing | `terminal_grounded_qa.py:208` and `terminal_grounded_qa.py:369` |
| Manual override exact match | `lookup.py:552` |
| Candidate scoring | `lookup.py:460` |
| Rejection reasons | `lookup.py:399` |
| Qwen formatting | `qwen_runner.py:159` and `qwen_runner.py:290` |
| Terminal loop | `terminal_grounded_qa.py:490` and `terminal_grounded_qa.py:570` |

### Sample Journey

Sample question:

`How can I bring up a 6300 in VSX mode?`

This is how the data moves through the system:

1. The question is entered in the terminal loop in `terminal_grounded_qa.py:570`.
2. `maybe_switch_context` asks for switch context before the question turn in `terminal_grounded_qa.py:490`.
3. The question is normalized and passed into `TerminalGroundedQA.answer` in `terminal_grounded_qa.py:369`.
4. `predict_intent` runs both BiLSTMs in `terminal_grounded_qa.py:139` and `terminal_grounded_qa.py:151`.
5. `extract_entities` pulls out switch, version, topic, and question type in `entity_extract.py:211`.
6. `_choose_lookup_source` decides whether the lookup should prefer release or product rows in `terminal_grounded_qa.py:208`.
7. `find_best_match` scores grounded rows in `lookup.py:583`.
8. `_row_score` and `_intent_rejection_reason` decide which rows stay and which rows are rejected in `lookup.py:460` and `lookup.py:399`.
9. The best row should be the manual override row added for VSX setup, stored in `Data/product_docs_final_repaired/manual_grounding_overrides.jsonl`.
10. If the row is trusted, the raw target value is returned or passed to Qwen for formatting in `qwen_runner.py:290`.

Why this sample matters:

- it shows the full path from user question to trained-model vote to lookup to final answer
- it shows how the override file influences the final result during training and runtime
- it shows where the switch context affects the answer

### 3. Runtime answer flow

After training, the terminal app uses the saved checkpoints and dataset rows to answer questions.

The live runtime flow is:

1. The app starts in [`terminal_grounded_qa.py`](./terminal_grounded_qa.py).
2. It loads the release and product BiLSTM checkpoints.
3. It loads all grounded rows through [`lookup.py`](./lookup.py).
4. It loads Qwen through [`qwen_runner.py`](./qwen_runner.py).
5. It asks the user for a switch family.
6. Before every question, it asks for switch context again.
7. It auto-switches context if the question itself mentions a different allowed switch.
8. It predicts intent with both BiLSTMs.
9. It extracts entities from the question.
10. It chooses whether lookup should prefer release or product rows.
11. It finds the best matching dataset row.
12. It either returns the raw target value, formats it with Qwen, or falls back to Qwen general knowledge.

### Runtime Flow With Snippets

This is the part you can present as the live data journey. The same question moves through each snippet in order.

#### Step 1. Start the terminal and ask for switch context

Source lines:

- [`main`](./terminal_grounded_qa.py#L570)
- [`maybe_switch_context`](./terminal_grounded_qa.py#L490)
- [`switch_from_question`](./terminal_grounded_qa.py#L505)

Snippet:

```python
while True:
    next_switch = maybe_switch_context(selected_switch)
    if next_switch is None:
        break
    selected_switch = next_switch
    print(f"\nUsing switch context: {selected_switch}")
    question = normalize_whitespace(input("Question: "))
    ...
    question_switch = switch_from_question(question, selected_switch)
    if question_switch is not None:
        if question_switch != selected_switch:
            print(f"Auto-switched switch context from {selected_switch} to {question_switch} based on the question.")
            selected_switch = question_switch
```

What happens here:

- the terminal asks which switch family is active
- Enter keeps the same context
- if the question mentions another allowed switch, the session auto-switches

Why it matters:

- the selected switch becomes a lookup filter later
- without the correct context, the right row may not be searched first

#### Step 2. Predict source and intent with both BiLSTMs

Source lines:

- [`predict_intent`](./terminal_grounded_qa.py#L139)
- [`TerminalGroundedQA.predict`](./terminal_grounded_qa.py#L159)

Snippet:

```python
release_intent, release_conf = predict_intent(question, self.release_bundle, self.device)
product_intent, product_conf = predict_intent(question, self.product_bundle, self.device)
if release_intent in RELEASE_LIKE_INTENTS:
    predicted_source = "release"
    predicted_intent = release_intent
    predicted_confidence = release_conf
elif release_conf > product_conf + 0.12:
    predicted_source = "release"
    predicted_intent = release_intent
    predicted_confidence = release_conf
else:
    predicted_source = "product"
    predicted_intent = product_intent
    predicted_confidence = product_conf
```

What happens here:

- the same question is run through the release BiLSTM and the product BiLSTM
- the app compares both votes
- release-like intents can force release routing
- otherwise the higher-confidence model wins

Why it matters:

- this is the first domain split
- it decides whether the lookup should bias toward release-note rows or product-doc rows

#### Step 3. Extract entities from the question

Source lines:

- [`extract_entities`](./entity_extract.py#L211)

Snippet:

```python
def extract_entities(question: str, predicted_intent: str = "") -> Dict[str, str]:
    switch_candidates = extract_switch_candidates(question)  # detect switch names in the question
    version_parts = extract_version(question)  # extract version and sub-version text
    question_type = detect_question_type(question, predicted_intent)  # classify the question shape
    topic = _canonicalize_topic(question_type, extract_topic(question), question)  # normalize topic text
    entities: Dict[str, str] = {
        "question_type": question_type,  # store the question type for routing
        "command": extract_command(question),  # pull out CLI command text if present
        "topic": topic,  # store the normalized topic
        "bug_id": extract_bug_id(question),  # capture bug IDs when they appear
    }
```

What happens here:

- the question is turned into structured signals
- the code extracts switch, version, command, topic, and bug ID hints
- the question is classified as syntax, limitation, support matrix, config procedure, and so on

Why it matters:

- the lookup layer uses these extracted entities to rank rows
- a natural question becomes a more precise grounded query

#### Step 4. Choose lookup source and search the corpus

Source lines:

- [`_choose_lookup_source`](./terminal_grounded_qa.py#L208)
- [`find_best_match`](./lookup.py#L583)

Snippet:

```python
lookup_source = self._choose_lookup_source(
    normalized_question,
    str(prediction["predicted_source"]),
    raw_predicted_intent,
    question_type,
    entities,
)

lookup = find_best_match(
    question=normalized_question,
    predicted_source=lookup_source,
    predicted_intent=lookup_intent,
    entities=entities,
    selected_switch=selected_switch,
    rows=self.rows,
    min_lookup_score=MIN_LOOKUP_SCORE,
)
```

What happens here:

- the app decides whether the first search should prefer release or product rows
- then it searches all loaded grounded rows
- the selected switch, predicted intent, and extracted entities all go into ranking

Why it matters:

- this is the core grounding step
- if the source is wrong, the best row may never be considered first

#### Step 5. Rank and reject candidates

Source lines:

- [`_row_score`](./lookup.py#L460)
- [`_intent_rejection_reason`](./lookup.py#L399)

Snippet:

```python
def _row_score(question: str, predicted_intent: str, entities: Dict[str, str], row: GroundedRow, selected_switch: str) -> float:
    score = 0.0
    if switch_matches(selected_switch, row.switch, allow_groups=False):
        score += 42.0
    elif switch_matches(selected_switch, row.switch, allow_groups=True):
        score += 28.0
    ...
    if row.dataset_name == "manual_override":
        score += 30.0
    elif row.dataset_name == "product_docs_validated":
        score += 16.0
    elif row.dataset_name == "product_docs":
        score += 8.0
    score += _capacity_or_scale_score_adjustment(question, row, {**entities, "predicted_intent": predicted_intent})
    return score
```

What happens here:

- candidate rows get numeric scores
- switch, version, command, topic, and intent matches all add score
- manual overrides and validated rows get priority
- capacity-or-scale questions get extra bias and penalties

And rejection is controlled by:

```python
def _intent_rejection_reason(predicted_intent: str, row_intent: str) -> Optional[str]:
    normalized_predicted = _normalize_intent(predicted_intent)
    normalized_row = _normalize_intent(row_intent)
    if not normalized_predicted or not normalized_row:
        return "missing_intent_metadata"
    if normalized_row in _allowed_row_intents(normalized_predicted):
        return None
    return f"intent mismatch: predicted {normalized_predicted} does not allow {normalized_row}"
```

Why it matters:

- the highest-score row still has to pass intent rules
- rejected candidates are explainable because the system keeps the rejection reason

#### Step 6. Decide the final answer mode

Source lines:

- [`TerminalGroundedQA.answer`](./terminal_grounded_qa.py#L369)
- [`QwenFormatter.format_conversational_answer`](./qwen_runner.py#L290)

Snippet:

```python
if lookup_is_reliable:
    grounded = True
    target_value_used = True
    if is_syntax_question:
        final_answer = target_value
        answer_mode = "direct_target_value"
        bypass_qwen = True
    else:
        answer_mode = "grounded_qwen"
        try:
            final_answer = self.qwen.format_conversational_answer(normalized_question, target_value)
        except Exception as exc:
            lookup["qwen_error"] = str(exc)
            final_answer = target_value
            answer_mode = "direct_target_value"
            bypass_qwen = True
```

What happens here:

- syntax questions return the exact target value
- grounded explanation questions go through Qwen for readable formatting
- if Qwen fails, the code falls back to the raw target value

Why it matters:

- grounded answers stay accurate
- syntax answers stay exact
- the final answer is stable even if formatting fails

### Sample Journey With Snippets

Sample question:

`How can I bring up a 6300 in VSX mode?`

Here is how this exact question travels through the code:

1. `main()` in `terminal_grounded_qa.py:570` opens the terminal loop and asks for switch context.
2. `maybe_switch_context()` in `terminal_grounded_qa.py:490` keeps or changes the active switch.
3. The question is sent to `TerminalGroundedQA.answer()` in `terminal_grounded_qa.py:369`.
4. `predict_intent()` runs on both release and product checkpoints in `terminal_grounded_qa.py:139`.
5. `extract_entities()` in `entity_extract.py:211` pulls out switch and topic clues from the text.
6. `_choose_lookup_source()` in `terminal_grounded_qa.py:208` decides whether release or product should be preferred.
7. `find_best_match()` in `lookup.py:583` ranks rows from the loaded corpora.
8. `_row_score()` in `lookup.py:460` boosts the row that best matches VSX setup.
9. `_intent_rejection_reason()` in `lookup.py:399` filters out rows with the wrong intent.
10. If the manual override row is the best match, Qwen formats it in `qwen_runner.py:290`.

What to say in the presentation:

- the question is first normalized by the terminal app
- the models vote on the domain and intent
- entity extraction turns the question into searchable hints
- lookup compares the question against the training rows
- scoring and intent rules decide the winner
- Qwen only rewrites the grounded answer, it does not invent the answer

### 4. Output and debugging

The final result is printed with:

- predicted source and intent
- extracted entities
- model votes
- matched dataset row
- target value
- final answer
- lookup status
- top candidates and rejection reasons

## Important Code Snippets

These are the smallest code pieces that explain the core behavior.

### 1. Shared config

This is where the folder points to the trained checkpoints and the data sources.

```python
QWEN_MODEL_PATH = Path(r"E:\52\Train_w\Train\outputs_final\qwen25_15b_qlora_1epoch_20260706_225219\merged_full_model")
RELEASE_BILSTM_PATH = Path(r"C:\Hpe\Train\outputs_release_lstm\all_switches\best_model.pt")
PRODUCT_BILSTM_PATH = Path(r"C:\Hpe\Train\outputs_product_lstm\all_switches\best_model.pt")
MANUAL_GROUNDED_OVERRIDE_PATH = PROJECT_ROOT / "Data" / "product_docs_final_repaired" / "manual_grounding_overrides.jsonl"
```

### 2. Product training overrides

This is how the product model reuses the shared training engine while swapping in product-specific data and intents.

```python
base.SELECTED_INTENTS = PRODUCT_INTENTS
base.INTENT_ALIAS_MAP = PRODUCT_INTENT_ALIAS_MAP
base.NEGATIVE_SAMPLE_ROWS = PRODUCT_NEGATIVE_ROWS
base.DEFAULT_DATA_PATHS = [
    Path(r"C:\Hpe\Train\Data\product_docs_final_repaired\manual_grounding_overrides.jsonl"),
    Path(r"C:\Hpe\Train\Data\product_docs_final_repaired"),
    Path(r"C:\Hpe\Train\Data\product_docs_final"),
    Path(r"C:\Hpe\Train\imporved_data_addition"),
    Path(r"C:\Hpe\Train\Data\aruba_aoscx_product_documentation_dataset_hpe_validated.jsonl"),
]
```

### 3. Question parsing

This is the part that turns a raw question into structured fields.

```python
def extract_entities(question: str, predicted_intent: str = "") -> Dict[str, str]:
    switch_candidates = extract_switch_candidates(question)
    version_parts = extract_version(question)
    question_type = detect_question_type(question, predicted_intent)
    topic = _canonicalize_topic(question_type, extract_topic(question), question)
    entities: Dict[str, str] = {
        "question_type": question_type,
        "command": extract_command(question),
        "topic": topic,
        "bug_id": extract_bug_id(question),
    }
```

What this does:

- pulls structured fields out of a free-form question
- identifies switch, version, command, topic, and bug ID hints
- gives the lookup layer more precise signals than plain text alone

Why it matters:

- lookup quality depends heavily on these extracted fields
- if entity extraction is wrong, the right row may be ranked too low
- this is where natural questions get turned into grounded lookup hints

### 4. Intent prediction

This is the shared BiLSTM inference path.

```python
def predict_intent(question: str, bundle: ModelBundle, device: torch.device) -> tuple[str, float]:
    cleaned = normalize_whitespace(question)  # normalize spacing before tokenization
    ids = bundle.tokenizer.encode(cleaned, bundle.max_length)  # turn text into token IDs
    input_ids = torch.tensor([ids], dtype=torch.long, device=device)  # add batch dimension
    lengths = torch.tensor([len(ids)], dtype=torch.long, device=device)  # tell the LSTM the sequence length
    with torch.inference_mode():  # no gradients during inference
        logits = bundle.model(input_ids, lengths)  # run the BiLSTM classifier
        probabilities = torch.softmax(logits, dim=-1)[0]  # convert logits to probabilities
    score, predicted_id = torch.max(probabilities, dim=-1)  # pick the top intent
    return bundle.label_names[int(predicted_id)], float(score.item())  # return intent and confidence
```

What this does:

- tokenizes the question
- runs the BiLSTM
- converts logits into probabilities
- returns the top intent and its confidence

Why it matters:

- this is the model vote used before lookup
- release and product models both run here
- the confidence helps decide whether to trust the grounded path

### 5. Source choice and answer routing

This is where the app decides release vs product, then grounded vs fallback.

```python
lookup_source = self._choose_lookup_source(
    normalized_question,  # normalized user question text
    str(prediction["predicted_source"]),  # source suggested by the BiLSTM vote
    raw_predicted_intent,  # raw predicted intent label
    question_type,  # parsed question type
    entities,  # extracted lookup hints
)

lookup = find_best_match(
    question=normalized_question,  # question text used for similarity scoring
    predicted_source=lookup_source,  # release or product search preference
    predicted_intent=lookup_intent,  # the intent we expect to match
    entities=entities,  # structured hints for ranking
    selected_switch=selected_switch,  # active switch context
    rows=self.rows,  # all grounded rows available to search
    min_lookup_score=MIN_LOOKUP_SCORE,  # minimum score required to accept a row
)
```

What this does:

- decides whether the question should look in release rows or product rows first
- sends the question, intent, entities, and selected switch into the grounded lookup
- returns the best matching row and its score

Why it matters:

- this is the core routing step between prediction and final answer
- a good lookup source choice prevents cross-domain mistakes
- the final answer depends on this row being correct

### 6. Manual override exact match

This is the fast path for the corrected examples.

```python
def _manual_override_exact_match(question: str, rows: Iterable[GroundedRow]) -> Optional[GroundedRow]:
    normalized_question = normalize_whitespace(question).lower()  # normalize the incoming question
    if not normalized_question:  # skip empty questions
        return None
    for row in rows:  # scan all available rows
        if row.dataset_name != "manual_override":  # only manual overrides use this shortcut
            continue
        if normalize_whitespace(row.input_text).lower() == normalized_question:  # exact text match
            return row  # return the corrected row immediately
    return None
```

What this does:

- checks whether the question exactly matches a corrected manual override row
- returns that row immediately if it exists

Why it matters:

- this gives known corrected examples top priority
- it is useful for small, high-confidence fixes that should never be outranked

### 7. Candidate scoring

This is the logic that ranks possible rows and applies intent and route-scale bias.

```python
def _row_score(question: str, predicted_intent: str, entities: Dict[str, str], row: GroundedRow, selected_switch: str) -> float:
    score = 0.0  # start from zero
    if switch_matches(selected_switch, row.switch, allow_groups=False):  # exact switch match
        score += 42.0
    elif switch_matches(selected_switch, row.switch, allow_groups=True):  # grouped switch match
        score += 28.0
    ...
    if row.dataset_name == "manual_override":  # manual fixes are strongest
        score += 30.0
    elif row.dataset_name == "product_docs_validated":  # validated product rows get a boost
        score += 16.0
    elif row.dataset_name == "product_docs":  # regular product rows get a smaller boost
        score += 8.0
    score += _capacity_or_scale_score_adjustment(question, row, {**entities, "predicted_intent": predicted_intent})  # route-scale tuning
    return score  # final numeric relevance score
```

What this does:

- gives each candidate row a numeric relevance score
- rewards switch, version, command, topic, and intent matches
- boosts validated and manual override rows
- adds special handling for capacity-or-scale questions

Why it matters:

- this is the ranking engine for grounded lookup
- the row with the highest score wins if it is also allowed by intent rules
- the scoring tweaks are what keep obvious wrong answers from winning

### 8. Rejection reasons

This is what gives you the explainable "why was this candidate rejected?" output.

```python
def _intent_rejection_reason(predicted_intent: str, row_intent: str) -> Optional[str]:
    normalized_predicted = _normalize_intent(predicted_intent)  # normalize predicted label
    normalized_row = _normalize_intent(row_intent)  # normalize candidate row label
    if not normalized_predicted or not normalized_row:  # missing metadata is a rejection
        return "missing_intent_metadata"
    if normalized_row in _allowed_row_intents(normalized_predicted):  # allow mapped aliases
        return None
    return f"intent mismatch: predicted {normalized_predicted} does not allow {normalized_row}"  # hard reject
```

What this does:

- checks whether a candidate row's intent is allowed for the predicted intent
- rejects rows that are not in the allowed alias set

Why it matters:

- this is the hard guardrail that blocks bad cross-intent matches
- it keeps the system explainable because rejected rows have a visible reason

### 9. Qwen formatting

This is the part that rewrites a grounded answer into nicer bullet points.

```python
def format_grounded_answer(self, question: str, grounded_answer: str) -> str:
    answer = normalize_whitespace(grounded_answer)  # clean up incoming text
    if not answer:  # nothing to format
        return answer
    prompt = (
        f"Question: {question}\n\n"  # include the user question for context
        f"Target value:\n{grounded_answer}\n\n"  # give Qwen only the grounded content
        "Instruction:\n"
        "Answer the question using the target_value.\n"  # no extra facts
        "Format the answer in bullet points.\n"  # make it readable
        "Keep compound labels together, such as Feature Caveat or Known Issue.\n"  # preserve labels
        "If the target_value contains Symptom, Scenario, Workaround, Cause, or Fix, make them separate bullets.\n"  # structured output
        "Keep the answer short and clear."  # keep it concise
    )
```

What this does:

- asks Qwen to rewrite the grounded answer into a cleaner bullet format
- tells Qwen not to add facts
- keeps labels like Feature Caveat or Known Issue together

Why it matters:

- grounded answers stay accurate but become easier to read
- if Qwen changes important details, the validator falls back to the original grounded text

### 10. Terminal loop

This is the main interactive loop that prompts for switch context, asks the question, and prints the result.

```python
while True:
    next_switch = maybe_switch_context(selected_switch)  # ask whether to keep or change switch context
    if next_switch is None:  # exit or quit
        break
    selected_switch = next_switch  # update the active context
    print(f"\nUsing switch context: {selected_switch}")  # show the current context
    question = normalize_whitespace(input("Question: "))  # read the user question
    if not question:  # skip empty input
        continue
    question_switch = switch_from_question(question, selected_switch)  # detect switch hints inside the question
    if question_switch is not None and question_switch != selected_switch:  # auto-switch if the question names another switch
        print(f"Auto-switched switch context from {selected_switch} to {question_switch} based on the question.")
        selected_switch = question_switch  # apply the auto-switch
```

What this does:

- keeps asking for switch context before each question
- lets Enter keep the current switch
- auto-switches if the question mentions another allowed switch

Why it matters:

- this makes the interaction explicit and predictable
- the switch context affects which rows the lookup can consider
- this is why the terminal behaves like a guided conversation instead of a free-form chat

## File Map

### [`config.py`](./config.py)

This file holds the shared constants for the whole folder.

Important items:

- `QWEN_MODEL_PATH`
- `RELEASE_BILSTM_PATH`
- `PRODUCT_BILSTM_PATH`
- `PRODUCT_VALIDATED_DATA_PATH`
- `MANUAL_GROUNDED_OVERRIDE_PATH`
- `RELEASE_DATA_ROOT`
- `PRODUCT_AGGREGATE_PATHS`
- `PRODUCT_FALLBACK_ROOTS`
- `SYNTHETIC_DATA_PATHS`
- `ALLOWED_SWITCH_FAMILIES`
- `RELEASE_LIKE_INTENTS`
- `SYNTAX_LIKE_INTENTS`
- `INTENT_ALIAS_MAP`
- `PRODUCT_INTENT_CANONICAL_MAP`
- `CAPACITY_OR_SCALE_KEYWORDS`
- `CAPACITY_OR_SCALE_PENALTY_KEYWORDS`
- `MIN_LOOKUP_SCORE`
- `MIN_MODEL_CONFIDENCE`
- `TOP_K_CANDIDATES`
- `SAFE_NO_MATCH`

Code reference:

- [`config.py`](./config.py#L1)

### [`entity_extract.py`](./entity_extract.py)

This file turns raw questions into structured signals:

- switch family
- version
- bug ID
- command
- topic
- question type

Important functions:

- [`normalize_whitespace`](./entity_extract.py#L12)
- [`normalize_switch_name`](./entity_extract.py#L18)
- [`extract_switch_candidates`](./entity_extract.py#L29)
- [`extract_version`](./entity_extract.py#L45)
- [`extract_bug_id`](./entity_extract.py#L65)
- [`extract_command`](./entity_extract.py#L71)
- [`extract_topic`](./entity_extract.py#L96)
- [`detect_question_type`](./entity_extract.py#L124)
- [`_canonicalize_topic`](./entity_extract.py#L186)
- [`extract_entities`](./entity_extract.py#L211)

### [`lookup.py`](./lookup.py)

This file loads the datasets and ranks grounded rows.

Important structures and functions:

- [`GroundedRow`](./lookup.py#L47)
- [`read_jsonl`](./lookup.py#L66)
- [`dotted_version`](./lookup.py#L82)
- [`infer_release_intent`](./lookup.py#L90)
- [`_product_labels`](./lookup.py#L130)
- [`_product_slots`](./lookup.py#L135)
- [`_product_intent`](./lookup.py#L147)
- [`_product_target_value`](./lookup.py#L155)
- [`load_release_rows`](./lookup.py#L185)
- [`_row_from_product`](./lookup.py#L231)
- [`load_product_rows`](./lookup.py#L274)
- [`load_synthetic_rows`](./lookup.py#L309)
- [`load_all_rows`](./lookup.py#L327)
- [`switch_matches`](./lookup.py#L339)
- [`_same_intent_family`](./lookup.py#L351)
- [`_intent_rejection_reason`](./lookup.py#L399)
- [`_capacity_or_scale_score_adjustment`](./lookup.py#L414)
- [`_row_score`](./lookup.py#L460)
- [`_manual_override_exact_match`](./lookup.py#L552)
- [`find_best_match`](./lookup.py#L583)

### [`qwen_runner.py`](./qwen_runner.py)

This file is responsible for answer formatting and general fallback.

Important pieces:

- `SYSTEM_PROMPT`
- `GENERAL_SYSTEM_PROMPT`
- `_GROUNDING_LABELS`
- `_STRUCTURED_LABEL_HEADS`
- [`format_grounded_answer_text`](./qwen_runner.py#L159)
- [`QwenFormatter`](./qwen_runner.py#L193)

### [`terminal_grounded_qa.py`](./terminal_grounded_qa.py)

This is the interactive CLI entry point.

Important pieces:

- `SimpleTokenizer`
- `LSTMIntentModel`
- `ModelBundle`
- [`load_lstm_bundle`](./terminal_grounded_qa.py#L114)
- [`predict_intent`](./terminal_grounded_qa.py#L139)
- `TerminalGroundedQA`
- [`prompt_switch_family`](./terminal_grounded_qa.py#L479)
- [`maybe_switch_context`](./terminal_grounded_qa.py#L490)
- [`switch_from_question`](./terminal_grounded_qa.py#L505)
- [`print_result`](./terminal_grounded_qa.py#L514)
- [`main`](./terminal_grounded_qa.py#L570)

## End-to-End Data Flow

### 1. Startup

The terminal app starts in [`main`](./terminal_grounded_qa.py#L570).

It creates a `TerminalGroundedQA` instance, which:

- chooses the device
- loads the release BiLSTM checkpoint
- loads the product BiLSTM checkpoint
- loads all grounded rows from release/product/synthetic sources
- prepares Qwen for formatting and fallback

Code reference:

- [`TerminalGroundedQA.__init__`](./terminal_grounded_qa.py#L151)

### 2. Initial switch selection

The app first calls [`prompt_switch_family`](./terminal_grounded_qa.py#L479).

This prints the allowed switch families from `config.py` and forces the user to pick one.

That selected switch becomes the current context for the session.

### 3. Per-question switch confirmation

Before every question turn, the CLI calls [`maybe_switch_context`](./terminal_grounded_qa.py#L490).

This is why the terminal keeps asking:

- keep the current switch
- enter a new switch
- exit

If the user types a valid switch family, the session context changes immediately.
If the user just presses Enter, the current switch is kept.

### 4. Auto switch detection from the question

After the question is entered, [`switch_from_question`](./terminal_grounded_qa.py#L505) scans the question text.

It uses [`extract_switch_candidates`](./entity_extract.py#L29) to detect switch families mentioned directly in the question.

If the question mentions another allowed switch, the CLI auto-switches context and prints that change.

This keeps the session context consistent with the user's question.

### 5. Intent prediction with both BiLSTMs

The app calls [`predict_intent`](./terminal_grounded_qa.py#L139) twice:

- once with the release checkpoint
- once with the product checkpoint

Each checkpoint is loaded through [`load_lstm_bundle`](./terminal_grounded_qa.py#L114).

The model is a compact bidirectional LSTM defined by [`LSTMIntentModel`](./terminal_grounded_qa.py#L71).

The output is a small prediction bundle:

- predicted intent
- confidence
- per-model votes

This is not the final answer yet. It is only one signal used in routing.

### 6. Entity extraction

The question is normalized and passed into [`extract_entities`](./entity_extract.py#L211).

That function builds a dictionary with structured fields such as:

- `switch`
- `version`
- `version_full`
- `sub_version`
- `command`
- `topic`
- `feature`
- `bug_id`
- `question_type`

The helper functions that power this step are:

- [`extract_version`](./entity_extract.py#L45)
- [`extract_bug_id`](./entity_extract.py#L65)
- [`extract_command`](./entity_extract.py#L71)
- [`extract_topic`](./entity_extract.py#L96)
- [`detect_question_type`](./entity_extract.py#L124)
- [`_canonicalize_topic`](./entity_extract.py#L186)

This entity dictionary is the main bridge between free-form language and grounded lookup.

### 7. Choosing release vs product lookup

The answer path in [`TerminalGroundedQA.answer`](./terminal_grounded_qa.py#L151) decides which corpus to prefer.

The decision is based on:

- predicted source from the two BiLSTMs
- question type
- release-like intent markers
- limitation/release-note cues

Relevant helper:

- [`_choose_lookup_source`](./terminal_grounded_qa.py#L151)

For example:

- syntax-like questions are pushed toward product
- release caveat/limitation questions can be routed to release when the question carries release-note cues

### 8. Candidate lookup

The core retrieval step is [`find_best_match`](./lookup.py#L583).

It works in layers:

1. Exact manual override match
2. Selected-context candidates
3. Broader fallback candidates

#### 8.1 Exact override

[`_manual_override_exact_match`](./lookup.py#L552) checks whether the user question matches a manual override row exactly.

That path is intentionally strong, because it is used for corrected examples that should win immediately.

#### 8.2 Row loading

All rows are gathered by [`load_all_rows`](./lookup.py#L327), which combines:

- release rows from `Data/Release_Notes`
- product rows from product corpus folders and validated data
- manual override rows
- synthetic rows

#### 8.3 Scope and ranking

`find_best_match` builds candidate scopes and then scores them with [`_row_score`](./lookup.py#L460).

Important scoring signals:

- switch match
- version match
- bug ID match
- command match
- topic match
- feature match
- intent compatibility
- dataset priority
- text similarity
- token overlap
- question-type specific bonuses
- capacity-or-scale bonuses and penalties

#### 8.4 Intent rejection

Before a row can be selected, [`_intent_rejection_reason`](./lookup.py#L399) checks whether the row's intent is allowed.

This is where hard rejection happens unless the alias map allows the mismatch.

That prevents obvious wrong matches from being returned just because the text is similar.

#### 8.5 Why candidates were rejected

`find_best_match` returns `top_candidates` with:

- rank
- score
- status
- rejection_reason
- row summary

This is what the terminal prints later so you can see why a candidate lost.

### 9. Capacity-or-scale special handling

The lookup has extra bias for route scale and capacity questions.

The adjustment happens in [`_capacity_or_scale_score_adjustment`](./lookup.py#L414).

This boosts rows that mention:

- route scale
- capacity
- maximum routes
- supported route scale
- stack members

It penalizes rows that look like they are about:

- minimum version
- version support
- supported versions

This helps route-scale questions avoid version-support noise.

### 10. Final answer decision

Once lookup returns a candidate, [`TerminalGroundedQA.answer`](./terminal_grounded_qa.py#L151) decides how to present it.

There are three main outcomes:

- `direct_target_value`
  - used for CLI syntax
  - returns the grounded command string exactly
- `grounded_qwen`
  - used for grounded explanatory answers
  - passes the grounded `target_value` to Qwen for formatting only
- `qwen_fallback`
  - used when no reliable grounded answer is found
  - sends only the user question to Qwen

The CLI syntax bypass is controlled by:

- [`SYNTAX_LIKE_INTENTS`](./config.py#L77)

The grounded formatting is handled by:

- [`QwenFormatter.format_conversational_answer`](./qwen_runner.py#L193)

### 11. Qwen formatting and fallback

The Qwen wrapper lives in [`QwenFormatter`](./qwen_runner.py#L193).

Important methods:

- `_lazy_load`
- `_encode_prompt`
- `_generate_text`
- `validate`
- `format_grounded_answer`
- `format_conversational_answer`
- `answer_general`

The grounded formatter uses a strict prompt:

- rewrite the target value
- keep it concise
- keep bullet points
- do not add new facts

If Qwen changes important tokens, `validate` rejects the output and the code falls back to the raw grounded answer.

The text cleanup utilities that make the final output readable are:

- [`format_grounded_answer_text`](./qwen_runner.py#L159)
- `_merge_structured_lines_v2`
- `_split_label_segments_v2`
- `_split_inline_list_items`

### 12. Printing the answer

The final `result` dictionary is printed by [`print_result`](./terminal_grounded_qa.py#L514).

It shows:

- predicted source and intent
- extracted entities
- model votes
- matched dataset row
- target value
- final answer
- answer mode
- grounding flags
- lookup status
- lookup score
- top candidates and rejection reasons

This is what makes the terminal version easy to debug.

## How the Data Shapes Look

### Question

Input from the user is just a string.

### Prediction

The BiLSTM predictions are a dictionary with:

- `predicted_source`
- `predicted_intent`
- `predicted_confidence`
- `model_votes`

### Entities

The entity extractor returns a dictionary with structured lookup hints.

### Lookup result

`find_best_match` returns a dictionary with:

- `matched`
- `lookup_reason`
- `lookup_context`
- `matched_row`
- `target_value`
- `score`
- `top_candidates`

### Final result

`TerminalGroundedQA.answer` merges everything into a single output object.

That output is what the terminal prints.

## Important Behavior Rules

### Switch handling

- ask for switch context every turn
- keep current context on Enter
- auto-switch if the question mentions another allowed switch

### Lookup behavior

- keep intent rejection strict
- allow mismatches only through the alias map
- prefer manual overrides when exact matches exist
- use selected context first, then broader fallback

### Answer behavior

- syntax questions return exact grounded text
- grounded explanatory answers are formatted by Qwen
- ungrounded questions use Qwen general knowledge when possible

## Where To Look When Something Goes Wrong

If the answer is wrong, inspect these layers in order:

1. [`entity_extract.py`](./entity_extract.py)
2. [`terminal_grounded_qa.py`](./terminal_grounded_qa.py)
3. [`lookup.py`](./lookup.py)
4. [`qwen_runner.py`](./qwen_runner.py)

Typical failure sources:

- wrong switch context
- wrong question type
- bad command/topic extraction
- wrong corpus routing
- wrong intent aliasing
- Qwen formatting noise

## Short Summary

The folder follows this sequence:

`question -> switch context -> entity extraction -> BiLSTM voting -> source selection -> grounded lookup -> candidate ranking -> Qwen formatting or fallback -> printed answer`

That is the complete runtime story for `terminal_grounded_qa_test/`.

## Training Pipeline

This folder does not train the BiLSTMs itself, but the runtime depends on the training scripts that produced the checkpoints it loads.

The training chain is split across three files:

- [`train_lstm_gpu.py`](../train_lstm_gpu.py)
- [`train_release_lstm.py`](../train_release_lstm.py)
- [`train_product_lstm.py`](../train_product_lstm.py)

### Shared training code

[`train_lstm_gpu.py`](../train_lstm_gpu.py#L1) contains the reusable release-note training and conversion logic that the other scripts build on.

It provides:

- the `LSTMIntentModel`
- JSONL conversion helpers
- dataset cleaning
- train/validation/test splitting
- validation evaluation
- best-model training loop
- classification report generation
- sample prediction export

Key helpers:

- [`convert_row`](../train_lstm_gpu.py#L271)
- [`read_and_convert`](../train_lstm_gpu.py#L323)
- [`split_by_intent`](../train_lstm_gpu.py#L429)
- [`evaluate`](../train_lstm_gpu.py#L560)
- [`train_model`](../train_lstm_gpu.py#L589)
- [`compute_classification_report`](../train_lstm_gpu.py#L667)
- [`save_prediction_samples`](../train_lstm_gpu.py#L764)

### Release training flow

[`train_release_lstm.py`](../train_release_lstm.py#L1) is the main training script for the release-note model.

It does the following:

1. Reads release-note JSONL files from `Data/Release_Notes`.
2. Uses [`collect_records`](../train_release_lstm.py#L373) to scan and normalize rows.
3. Uses [`row_to_record`](../train_release_lstm.py#L306) to convert each raw row into a training record.
4. Filters to the selected release intents.
5. Uses [`split_by_intent`](../train_release_lstm.py#L429) to make a stratified train/val/test split.
6. Builds PyTorch data loaders with [`build_loader`](../train_release_lstm.py#L486).
7. Trains the BiLSTM.
8. Validates on the validation split every epoch with [`evaluate`](../train_release_lstm.py#L547).
9. Stops early when validation performance stops improving.
10. Re-evaluates the best model on train, val, and test.
11. Writes the checkpoint and reports to `outputs_release_lstm/all_switches`.

Validation details:

- the model is judged primarily by validation macro F1
- `best_epoch` is chosen from validation performance
- `training_report.json` stores train/val/test metrics and the confusion matrix
- `samples_eval.md` stores example predictions for quick review

### Product training flow

[`train_product_lstm.py`](../train_product_lstm.py#L1) is a thin configuration layer over the release training script.

It reuses the same training engine but overrides:

- the intent set
- the alias map
- the negative examples
- the data sources
- the output directory

The product data sources currently include:

- repaired product docs
- original product docs
- the validated product JSONL
- synthetic merged data
- the manual override file now stored under `Data/product_docs_final_repaired/`

At runtime, `train_product_lstm.py` sets:

- `base.SELECTED_INTENTS`
- `base.INTENT_ALIAS_MAP`
- `base.NEGATIVE_SAMPLE_ROWS`
- `base.DEFAULT_DATA_PATHS`

Then it calls `base.main()`, which means it uses the same:

- record collection
- deduplication
- train/val/test split
- validation loop
- best-model selection
- report writing

### Where the split happens

The split is not random across the whole dataset. It is stratified by intent.

The logic is in:

- [`split_by_intent`](../train_lstm_gpu.py#L429)

What it does:

- groups rows by intent
- shuffles each intent group with a fixed seed
- assigns roughly 80 percent to train
- assigns roughly 10 percent to validation
- assigns roughly 10 percent to test
- keeps tiny classes from collapsing by forcing at least one example into train

That means validation is intent-balanced instead of a blind global split.

### What validation checks

Validation happens in two places:

1. During training, every epoch runs [`evaluate`](../train_lstm_gpu.py#L560) on the validation loader.
2. After training, the best model is re-evaluated on train, val, and test and saved into the training report.

The validation metrics include:

- accuracy
- macro precision
- macro recall
- macro F1
- per-class precision/recall/F1
- confusion matrix

The selected checkpoint is the one with the best validation macro F1.

### What the saved reports tell you

The checkpoint folders contain the proof of the training run:

- `best_model.pt`
- `vocab.json`
- `label_encoder.json`
- `training_report.json`
- `training_metrics.csv`
- `confusion_matrix.json`
- `samples_eval.md`

For example:

- release training report: [`outputs_release_lstm/all_switches/training_report.json`](../outputs_release_lstm/all_switches/training_report.json)
- product training report: [`outputs_product_lstm/all_switches/training_report.json`](../outputs_product_lstm/all_switches/training_report.json)

Those reports show:

- how many rows were scanned
- how many were kept
- why rows were filtered out
- how the train/val/test split was built
- what the best epoch was
- how strong validation/test accuracy was

So if you want to know "where is the code getting data from", the answer is:

- release training reads `Data/Release_Notes`
- product training reads the repaired/original product doc folders plus the validated and override JSONL sources
- the actual training engine comes from `train_lstm_gpu.py`
- the product script only reconfigures that engine
