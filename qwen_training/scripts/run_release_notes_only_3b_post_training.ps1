param(
    [Parameter(Mandatory = $true)]
    [int]$TrainingPid,
    [Parameter(Mandatory = $true)]
    [string]$TrainingOutput,
    [Parameter(Mandatory = $true)]
    [string]$TrainingStdout,
    [Parameter(Mandatory = $true)]
    [string]$TrainingStderr,
    [Parameter(Mandatory = $true)]
    [string]$LogPath,
    [Parameter(Mandatory = $true)]
    [string]$SplitManifest,
    [Parameter(Mandatory = $true)]
    [string]$SuiteManifest,
    [string]$RunStamp = 'manual'
)

$ErrorActionPreference = 'Stop'
$workspace = (Resolve-Path '.').Path
$python = (Resolve-Path '.\.venv312\Scripts\python.exe').Path
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
    [string]$Label,
    [string]$AdapterPath,
    [string]$SuiteLabel,
    [string]$DataPath,
    [int]$Rows
) {
    $output = Join-Path $workspace "outputs_inference\qwen25_3b_release_notes_only_1epoch_stratified_${Label}_${SuiteLabel}"
    $stdout = Join-Path $workspace "logs\qwen25_3b_release_notes_only_1epoch_stratified_${Label}_${SuiteLabel}_$RunStamp.out.log"
    $stderr = Join-Path $workspace "logs\qwen25_3b_release_notes_only_1epoch_stratified_${Label}_${SuiteLabel}_$RunStamp.err.log"
    if (Test-Path -LiteralPath $output) {
        $existingReview = Join-Path $output 'strict_inference_review.json'
        if (Test-Path -LiteralPath $existingReview -PathType Leaf) {
            $existingMetrics = (Get-Content -LiteralPath $existingReview -Raw | ConvertFrom-Json).metrics
            Write-RunLog "Reusing completed candidate=$Label suite=$SuiteLabel score=$($existingMetrics.average_score) output=$output"
            return $output
        }
        throw "Refusing to overwrite incomplete inference output: $output"
    }
    $arguments = @(
        'run_inference_1000step_adapter.py',
        '--model_name', $modelName,
        '--adapter_path', $AdapterPath,
        '--output_dir', $output,
        '--test_data_path', $DataPath,
        '--subset_size', "$Rows",
        '--manual_limit', '0',
        '--max_length', '512',
        '--max_new_tokens', '160',
        '--repetition_penalty', '1.0',
        '--no_repeat_ngram_size', '0',
        '--local_files_only'
    )
    Write-RunLog "Starting candidate=$Label suite=$SuiteLabel rows=$Rows adapter=$AdapterPath"
    $process = Start-Process -FilePath $python -ArgumentList $arguments -WorkingDirectory $workspace `
        -RedirectStandardOutput $stdout -RedirectStandardError $stderr -WindowStyle Hidden -PassThru
    $process.WaitForExit()
    $process.Refresh()
    if ($null -ne $process.ExitCode -and $process.ExitCode -ne 0) {
        throw "Inference failed: candidate=$Label suite=$SuiteLabel exit=$($process.ExitCode) stderr=$stderr"
    }
    $review = Join-Path $output 'strict_inference_review.json'
    Require-File $review
    $metrics = (Get-Content -LiteralPath $review -Raw | ConvertFrom-Json).metrics
    Write-RunLog "Completed candidate=$Label suite=$SuiteLabel score=$($metrics.average_score) good=$($metrics.good_predictions_count) bug_acc=$($metrics.bug_id_accuracy) event_acc=$($metrics.event_id_accuracy) date_acc=$($metrics.date_accuracy) command_acc=$($metrics.command_name_accuracy) syntax_acc=$($metrics.command_syntax_preservation) errors=$($metrics.wrong_bug_id_predictions),$($metrics.wrong_event_id_count),$($metrics.wrong_date_predictions),$($metrics.wrong_cli_syntax_predictions)"
    return $output
}

Write-RunLog "Waiting for training PID $TrainingPid"
while (Get-Process -Id $TrainingPid -ErrorAction SilentlyContinue) {
    Start-Sleep -Seconds 60
}
Start-Sleep -Seconds 10
Write-RunLog 'Training process ended; validating training artifacts.'

$failurePattern = '(?i)(Traceback|CUDA out of memory|OutOfMemoryError|stopping training due to non-finite|stopping training due to NaN/Inf metrics|NaNStoppingCallback)'
if (Select-String -LiteralPath $TrainingStdout, $TrainingStderr -Pattern $failurePattern -Quiet -ErrorAction SilentlyContinue) {
    throw "Training logs contain a fatal pattern; evaluation will not start."
}

Require-File $SplitManifest
Require-File $SuiteManifest
$splitDir = Split-Path -Parent $SplitManifest
$sourceDisjoint = Join-Path $splitDir 'release_source_disjoint100.jsonl'
$legacy65 = Join-Path $splitDir 'release_legacy65.jsonl'
Require-File $sourceDisjoint
Require-File $legacy65

function Find-Checkpoints([string]$Root) {
    Get-ChildItem -LiteralPath $Root -Directory |
        Where-Object { $_.Name -match '^checkpoint-\d+$' } |
        Sort-Object { [int]($_.Name -replace '^checkpoint-', '') }
}

$epochs = [ordered]@{}
foreach ($checkpoint in Find-Checkpoints $trainingRoot) {
    $epochs[$checkpoint.Name] = $checkpoint.FullName
}
$finalAdapter = Join-Path $trainingRoot 'lora_adapters'
if (Test-Path -LiteralPath $finalAdapter -PathType Container) {
    $epochs['final'] = $finalAdapter
}
if ($epochs.Count -eq 0) {
    throw "No checkpoints found under $trainingRoot"
}
foreach ($entry in $epochs.GetEnumerator()) {
    Require-Adapter $entry.Value
}
Require-File (Join-Path $trainingRoot 'eval_metrics.json')

$results = [ordered]@{}
foreach ($entry in $epochs.GetEnumerator()) {
    $label = $entry.Key
    $adapter = $entry.Value
    $results["${label}:release_source_disjoint100"] = Invoke-Inference $label $adapter 'release_source_disjoint100' $sourceDisjoint 100
    $results["${label}:release_legacy65"] = Invoke-Inference $label $adapter 'release_legacy65' $legacy65 65
}

$selectorArgs = @('select_best_epoch.py')
foreach ($entry in $epochs.GetEnumerator()) {
    $selectorArgs += @('--epoch', "$($entry.Key)=$($entry.Value)")
}
foreach ($entry in $results.GetEnumerator()) {
    $selectorArgs += @('--result', "$($entry.Key)=$($entry.Value)")
}
$selectorArgs += @(
    '--primary_suites', 'release_source_disjoint100',
    '--legacy_suite', 'release_legacy65',
    '--output_dir', $trainingRoot,
    '--allow_hard_failure_fallback',
    '--copy_best'
)
$selectorOut = Join-Path $workspace "logs\qwen25_3b_release_notes_only_1epoch_stratified_$RunStamp.best_epoch_selector.out.log"
$selectorErr = Join-Path $workspace "logs\qwen25_3b_release_notes_only_1epoch_stratified_$RunStamp.best_epoch_selector.err.log"
$selector = Start-Process -FilePath $python -ArgumentList $selectorArgs -WorkingDirectory $workspace `
    -RedirectStandardOutput $selectorOut -RedirectStandardError $selectorErr -WindowStyle Hidden -PassThru
$selector.WaitForExit()
$selector.Refresh()
if ($null -ne $selector.ExitCode -and $selector.ExitCode -ne 0) {
    throw "Checkpoint selector failed: exit=$($selector.ExitCode) stderr=$selectorErr"
}

$selectionPath = Join-Path $trainingRoot 'best_epoch_selection.json'
Require-File $selectionPath
$selection = Get-Content -LiteralPath $selectionPath -Raw | ConvertFrom-Json
if (-not $selection.selected_epoch) {
    throw 'All checkpoint candidates failed hard gates'
}
Require-Adapter (Join-Path $trainingRoot 'best_lora_adapters')
$completion = [ordered]@{
    completed_at = (Get-Date).ToString('o')
    selected_epoch = $selection.selected_epoch
    selected_adapter = $selection.selected_adapter
    copied_best_adapter = (Join-Path $trainingRoot 'best_lora_adapters')
    split_manifest = $SplitManifest
    suite_manifest = $SuiteManifest
    results = $results
    selection = $selectionPath
    run_log = $LogPath
}
$completion | ConvertTo-Json -Depth 6 | Set-Content -LiteralPath (Join-Path $trainingRoot 'training_run_validation.json') -Encoding utf8
Write-RunLog "Selection complete: selected=$($selection.selected_epoch) best=$(Join-Path $trainingRoot 'best_lora_adapters')"
