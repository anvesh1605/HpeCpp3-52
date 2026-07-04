param(
    [Parameter(Mandatory = $true)][int]$TrainingPid,
    [Parameter(Mandatory = $true)][string]$TrainingOutput,
    [Parameter(Mandatory = $true)][string]$TrainingStdout,
    [Parameter(Mandatory = $true)][string]$TrainingStderr,
    [Parameter(Mandatory = $true)][string]$LogPath,
[string]$EpochSpec = 'step1000:1000,step2000:2000,step3000:3000,step4000:4000,step5000:5000,step5321:5321',
[string]$RunSlug = 'qwen25_3b_release_notes_only_fullfacts_1epoch_stratified'
)

$ErrorActionPreference = 'Stop'
$workspace = (Resolve-Path '.').Path
$python = (Resolve-Path '.venv3070\Scripts\python.exe').Path
$modelName = 'Qwen/Qwen2.5-3B-Instruct'
$trainingRoot = [IO.Path]::GetFullPath($TrainingOutput)

function Write-RunLog([string]$Message) {
    $line = "$(Get-Date -Format o) | $Message"
    $line | Add-Content -LiteralPath $LogPath -Encoding utf8
    Write-Host $line
}

function Require-File([string]$Path) {
    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
        throw "Required file is missing: $Path"
    }
}

function Require-Adapter([string]$Path) {
    Require-File (Join-Path $Path 'adapter_config.json')
    Require-File (Join-Path $Path 'adapter_model.safetensors')
}

function Invoke-Inference(
    [string]$EpochLabel,
    [string]$AdapterPath,
    [string]$SuiteLabel,
    [string]$DataPath,
    [int]$SubsetSize,
    [int]$ManualLimit
) {
    $output = Join-Path $workspace "outputs_inference\${RunSlug}_${EpochLabel}_${SuiteLabel}"
    if (Test-Path -LiteralPath $output) {
        throw "Refusing to overwrite inference output: $output"
    }
    $stdout = Join-Path $workspace "logs\${RunSlug}_${EpochLabel}_${SuiteLabel}.out.log"
    $stderr = Join-Path $workspace "logs\${RunSlug}_${EpochLabel}_${SuiteLabel}.err.log"
    if ((Test-Path -LiteralPath $stdout) -or (Test-Path -LiteralPath $stderr)) {
        throw "Refusing to overwrite inference logs for ${EpochLabel}/${SuiteLabel}"
    }
    $arguments = @(
        'run_inference_1000step_adapter.py',
        '--model_name', $modelName,
        '--adapter_path', $AdapterPath,
        '--output_dir', $output,
        '--test_data_path', $DataPath,
        '--subset_size', "$SubsetSize",
        '--manual_limit', "$ManualLimit",
        '--max_length', '512',
        '--max_new_tokens', '120',
        '--repetition_penalty', '1.15',
        '--no_repeat_ngram_size', '4',
        '--local_files_only'
    )
    Write-RunLog "Starting strict inference: epoch=$EpochLabel suite=$SuiteLabel adapter=$AdapterPath output=$output"
    $process = Start-Process -FilePath $python -ArgumentList $arguments -WorkingDirectory $workspace -RedirectStandardOutput $stdout -RedirectStandardError $stderr -WindowStyle Hidden -Wait -PassThru
    if ($process.ExitCode -ne 0) {
        throw "Inference failed: epoch=$EpochLabel suite=$SuiteLabel exit=$($process.ExitCode) stderr=$stderr"
    }
    $review = Join-Path $output 'strict_inference_review.json'
    Require-File $review
    $metrics = (Get-Content -LiteralPath $review -Raw | ConvertFrom-Json).metrics
    Write-RunLog "Completed strict inference: epoch=$EpochLabel suite=$SuiteLabel score=$($metrics.average_score) good=$($metrics.good_predictions_count) bad=$($metrics.bad_predictions_count) bug_errors=$($metrics.wrong_bug_id_predictions) event_errors=$($metrics.wrong_event_id_count) cli_errors=$($metrics.wrong_cli_syntax_predictions) false_abstentions=$($metrics.false_abstention_predictions) loops=$($metrics.repetition_loop_predictions) placeholders=$($metrics.placeholder_template_predictions)"
    return $output
}

Write-RunLog "Waiting for training PID $TrainingPid"
while (Get-Process -Id $TrainingPid -ErrorAction SilentlyContinue) {
    Start-Sleep -Seconds 60
}
Start-Sleep -Seconds 10
Write-RunLog 'Training process ended; validating training artifacts.'

$failurePattern = 'Traceback|CUDA out of memory|OutOfMemoryError|Stopping training due to non-finite|NaNStoppingCallback'
if (Select-String -LiteralPath $TrainingStdout, $TrainingStderr -Pattern $failurePattern -Quiet -ErrorAction SilentlyContinue) {
    throw "Training logs contain a fatal pattern; evaluation will not start."
}

$epochs = [ordered]@{}
foreach ($token in $EpochSpec.Split(',', [StringSplitOptions]::RemoveEmptyEntries)) {
    $label, $step = $token.Split(':', 2)
    if (-not $label -or -not $step -or ($step -ne 'final' -and $step -notmatch '^\d+$')) {
        throw "Invalid EpochSpec token: $token"
    }
    $epochs[$label] = if ($step -eq 'final') {
        Join-Path $trainingRoot 'lora_adapters'
    } else {
        Join-Path $trainingRoot "checkpoint-$step"
    }
}
if ($epochs.Count -eq 0) {
    throw 'EpochSpec did not define any epoch checkpoints.'
}
foreach ($entry in $epochs.GetEnumerator()) {
    Require-Adapter $entry.Value
}
Require-Adapter (Join-Path $trainingRoot 'lora_adapters')
Require-File (Join-Path $trainingRoot 'eval_metrics.json')

$env:CUDA_DEVICE_ORDER = 'PCI_BUS_ID'
$env:CUDA_VISIBLE_DEVICES = '1'
$gpuCheck = & $python -c "import torch; print(torch.cuda.get_device_name(0))"
if ($LASTEXITCODE -ne 0 -or $gpuCheck -notmatch 'RTX 5070 Ti') {
    throw "Evaluation GPU verification failed: $gpuCheck"
}
Write-RunLog "Evaluation GPU verified: $gpuCheck (CUDA_VISIBLE_DEVICES=1 with PCI ordering)"

$sourceDisjoint = Join-Path $workspace 'Data\final_json_release_repaired_v1\release_only_stratified_seed42\release_source_disjoint100.jsonl'
$factualRecall = Join-Path $workspace 'Data\all_switches\release_notes_only_structured_full\release_notes_only_structured_full_holdout.jsonl'
$legacy = Join-Path $workspace 'Data\final_json_release_repaired_v1\release_only_stratified_seed42\release_legacy65.jsonl'
$results = [ordered]@{}
Write-RunLog 'Running release-note smoke test: subset_size=2 manual_limit=2'
$results['smoke:release_notes'] = Invoke-Inference 'smoke' (Join-Path $trainingRoot 'lora_adapters') 'smoke_release_notes' $factualRecall 2 2
foreach ($entry in $epochs.GetEnumerator()) {
    $label = $entry.Key
    $adapter = $entry.Value
    $results["${label}:source_disjoint"] = Invoke-Inference $label $adapter 'source_disjoint' $sourceDisjoint 100 0
    $results["${label}:factual_recall"] = Invoke-Inference $label $adapter 'factual_recall' $factualRecall 100 0
    $results["${label}:legacy65"] = Invoke-Inference $label $adapter 'legacy65' $legacy 50 15
}

$selectorArgs = @('select_best_epoch.py')
foreach ($entry in $epochs.GetEnumerator()) {
    $selectorArgs += @('--epoch', "$($entry.Key)=$($entry.Value)")
}
foreach ($entry in $results.GetEnumerator()) {
    $selectorArgs += @('--result', "$($entry.Key)=$($entry.Value)")
}
$selectorArgs += @('--output_dir', $trainingRoot, '--copy_best')
$selectorOut = Join-Path $workspace "logs\${RunSlug}_best_epoch_selector.out.log"
$selectorErr = Join-Path $workspace "logs\${RunSlug}_best_epoch_selector.err.log"
if ((Test-Path -LiteralPath $selectorOut) -or (Test-Path -LiteralPath $selectorErr)) {
    throw 'Refusing to overwrite best-epoch selector logs.'
}
$selector = Start-Process -FilePath $python -ArgumentList $selectorArgs -WorkingDirectory $workspace -RedirectStandardOutput $selectorOut -RedirectStandardError $selectorErr -WindowStyle Hidden -Wait -PassThru
if ($selector.ExitCode -ne 0) {
    throw "Best-epoch selector failed with exit $($selector.ExitCode)"
}

$selectionPath = Join-Path $trainingRoot 'best_epoch_selection.json'
Require-File $selectionPath
$selection = Get-Content -LiteralPath $selectionPath -Raw | ConvertFrom-Json
if (-not $selection.selected_epoch) {
    throw 'All epochs were rejected by hard strict gates; no best adapter was copied.'
}
Require-Adapter (Join-Path $trainingRoot 'best_lora_adapters')
$validation = [ordered]@{
    status = 'complete'
    completed_at = (Get-Date).ToString('o')
    training_output = $trainingRoot
    checkpoints = $epochs
    final_adapter = (Join-Path $trainingRoot 'lora_adapters')
    selected_epoch = $selection.selected_epoch
    selected_adapter = $selection.selected_adapter
    best_adapter = (Join-Path $trainingRoot 'best_lora_adapters')
    inference_results = $results
    training_logs = @{ stdout = $TrainingStdout; stderr = $TrainingStderr }
    post_training_log = $LogPath
}
$validation | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath (Join-Path $trainingRoot 'training_run_validation.json') -Encoding utf8
Write-RunLog "Post-training evaluation complete. Selected epoch=$($selection.selected_epoch) best_adapter=$(Join-Path $trainingRoot 'best_lora_adapters')"
