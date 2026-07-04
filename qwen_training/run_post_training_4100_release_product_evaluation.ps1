param(
    [Parameter(Mandatory = $true)][int]$TrainingPid,
    [Parameter(Mandatory = $true)][string]$TrainingOutput,
    [Parameter(Mandatory = $true)][string]$TrainingStdout,
    [Parameter(Mandatory = $true)][string]$TrainingStderr,
    [Parameter(Mandatory = $true)][string]$LogPath,
    [string]$RunSlug = 'qwen25_3b_4100_release_product_from_1epoch',
    [string]$HoldoutPath = 'Data\all_switches\strict_holdout_4100_release_product.jsonl'
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

function Invoke-Inference([string]$Label, [string]$AdapterPath) {
    $output = Join-Path $workspace "outputs_inference\${RunSlug}_${Label}"
    if (Test-Path -LiteralPath $output) {
        throw "Refusing to overwrite inference output: $output"
    }
    $stdout = Join-Path $workspace "logs\${RunSlug}_${Label}.out.log"
    $stderr = Join-Path $workspace "logs\${RunSlug}_${Label}.err.log"
    if ((Test-Path -LiteralPath $stdout) -or (Test-Path -LiteralPath $stderr)) {
        throw "Refusing to overwrite inference logs for ${Label}"
    }
    $arguments = @(
        'run_inference_1000step_adapter.py',
        '--model_name', $modelName,
        '--adapter_path', $AdapterPath,
        '--output_dir', $output,
        '--test_data_path', $HoldoutPath,
        '--subset_size', '100',
        '--manual_limit', '0',
        '--max_length', '512',
        '--max_new_tokens', '120',
        '--repetition_penalty', '1.15',
        '--no_repeat_ngram_size', '4'
    )
    Write-RunLog "Starting strict inference: label=$Label adapter=$AdapterPath output=$output"
    $process = Start-Process -FilePath $python -ArgumentList $arguments -WorkingDirectory $workspace -RedirectStandardOutput $stdout -RedirectStandardError $stderr -WindowStyle Hidden -Wait -PassThru
    if ($process.ExitCode -ne 0) {
        throw "Inference failed: label=$Label exit=$($process.ExitCode) stderr=$stderr"
    }
    $review = Join-Path $output 'strict_inference_review.json'
    Require-File $review
    $metrics = (Get-Content -LiteralPath $review -Raw | ConvertFrom-Json).metrics
    Write-RunLog "Completed strict inference: label=$Label score=$($metrics.average_score) good=$($metrics.good_predictions_count) bad=$($metrics.bad_predictions_count) wrong_bug=$($metrics.wrong_bug_id_predictions) fake_bug=$($metrics.fake_bug_id_predictions) wrong_event=$($metrics.wrong_event_id_count) wrong_cli=$($metrics.wrong_cli_syntax_predictions) invented_workaround=$($metrics.invented_workaround_predictions) generic_hallucination=$($metrics.generic_hallucination_predictions) placeholder=$($metrics.placeholder_template_predictions)"
    return @{
        output = $output
        metrics = $metrics
    }
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

Require-File (Join-Path $trainingRoot 'training_args.json')
Require-File (Join-Path $trainingRoot 'eval_metrics.json')
Require-Adapter (Join-Path $trainingRoot 'lora_adapters')
foreach ($step in @('checkpoint-100', 'checkpoint-250', 'checkpoint-500')) {
    Require-Adapter (Join-Path $trainingRoot $step)
}

$env:CUDA_DEVICE_ORDER = 'PCI_BUS_ID'
$env:CUDA_VISIBLE_DEVICES = '1'
$gpuCheck = & $python -c "import torch; print(torch.cuda.get_device_name(0))"
if ($LASTEXITCODE -ne 0 -or $gpuCheck -notmatch 'RTX 5070 Ti') {
    throw "Evaluation GPU verification failed: $gpuCheck"
}
Write-RunLog "Evaluation GPU verified: $gpuCheck (CUDA_VISIBLE_DEVICES=1 with PCI ordering)"
Write-RunLog "Using strict holdout: $HoldoutPath"

$results = [ordered]@{}
$results['checkpoint100'] = Invoke-Inference 'checkpoint100' (Join-Path $trainingRoot 'checkpoint-100')
$results['checkpoint250'] = Invoke-Inference 'checkpoint250' (Join-Path $trainingRoot 'checkpoint-250')
$results['checkpoint500'] = Invoke-Inference 'checkpoint500' (Join-Path $trainingRoot 'checkpoint-500')
$results['final'] = Invoke-Inference 'final' (Join-Path $trainingRoot 'lora_adapters')

$ranked = $results.GetEnumerator() | Sort-Object {
    - [double]$_.Value.metrics.average_score
}, {
    [int]$_.Value.metrics.wrong_bug_id_predictions
}, {
    [int]$_.Value.metrics.fake_bug_id_predictions
}, {
    [int]$_.Value.metrics.wrong_event_id_count
}, {
    [int]$_.Value.metrics.wrong_cli_syntax_predictions
}, {
    [int]$_.Value.metrics.invented_workaround_predictions
}, {
    [int]$_.Value.metrics.generic_hallucination_predictions
}, {
    [int]$_.Value.metrics.placeholder_template_predictions
}
$selected = $ranked | Select-Object -First 1

$selection = [ordered]@{
    selected_label = $selected.Key
    selected_adapter = if ($selected.Key -eq 'final') { Join-Path $trainingRoot 'lora_adapters' } else { Join-Path $trainingRoot "checkpoint-$($selected.Key.Substring('checkpoint'.Length))" }
    strict_score_used = 'average_score'
    holdout_path = (Resolve-Path $HoldoutPath).Path
    checkpoints = @{}
}
foreach ($entry in $results.GetEnumerator()) {
    $selection.checkpoints[$entry.Key] = @{
        adapter = if ($entry.Key -eq 'final') { Join-Path $trainingRoot 'lora_adapters' } else { Join-Path $trainingRoot "checkpoint-$($entry.Key.Substring('checkpoint'.Length))" }
        output_dir = $entry.Value.output
        metrics = $entry.Value.metrics
    }
}

$selectionJson = $selection | ConvertTo-Json -Depth 8
$selectionJson | Set-Content -LiteralPath (Join-Path $trainingRoot 'best_checkpoint_selection.json') -Encoding utf8

$lines = @(
    '# Best Checkpoint Selection',
    '',
    '- Selection metric: average strict score',
    "- Selected checkpoint: $($selection.selected_label)",
    "- Selected adapter: $($selection.selected_adapter)",
    '',
    '## Checkpoints',
    ''
)
foreach ($entry in $results.GetEnumerator()) {
    $m = $entry.Value.metrics
    $lines += @(
        "### $($entry.Key)",
        "",
        "- Average strict score: $($m.average_score)",
        "- Wrong Bug ID count: $($m.wrong_bug_id_predictions)",
        "- Fake Bug ID count: $($m.fake_bug_id_predictions)",
        "- Wrong Event ID count: $($m.wrong_event_id_count)",
        "- Wrong CLI syntax count: $($m.wrong_cli_syntax_predictions)",
        "- Invented workaround count: $($m.invented_workaround_predictions)",
        "- Generic hallucination count: $($m.generic_hallucination_predictions)",
        "- Placeholder/template count: $($m.placeholder_template_predictions)",
        ""
    )
}
$lines | Set-Content -LiteralPath (Join-Path $trainingRoot 'best_checkpoint_selection.md') -Encoding utf8

$bestAdapter = $selection.selected_adapter
$bestDestination = Join-Path $trainingRoot 'best_lora_adapters'
if (Test-Path -LiteralPath $bestDestination) {
    throw "Refusing to overwrite $bestDestination"
}
Copy-Item -LiteralPath $bestAdapter -Destination $bestDestination -Recurse
Write-RunLog "Best checkpoint selected: $($selection.selected_label)"
Write-RunLog "Best adapter copied to: $bestDestination"
