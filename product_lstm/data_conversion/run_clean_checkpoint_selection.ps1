param(
    [Parameter(Mandatory = $true)]
    [string]$RunStamp
)

$ErrorActionPreference = "Stop"
$root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
Set-Location -LiteralPath $root
$python = (Resolve-Path ".\.venv312\Scripts\python.exe").Path
$trainingRoot = (Resolve-Path "outputs_final\qwen25_3b_clean_pilot1000").Path
$suite = (Resolve-Path "final_json_clean\all_switches\inference_balanced100.jsonl").Path
$legacy = (Resolve-Path "Data\all_switches\test_chat_all_clean.jsonl").Path
$runLog = Join-Path $root "logs\qwen25_3b_clean_checkpoint_selection_$RunStamp.log"
$completionPath = Join-Path $root "logs\qwen25_3b_clean_checkpoint_selection_$RunStamp.completion.json"
$gpuUuid = "GPU-f1d815f0-db71-9d96-3a88-155d7c032f68"
$env:CUDA_VISIBLE_DEVICES = $gpuUuid
$env:PYTHONUTF8 = "1"

function Write-RunLog([string]$Message) {
    $line = "$(Get-Date -Format o) | $Message"
    $line | Add-Content -LiteralPath $runLog -Encoding utf8
    Write-Host $line
}

function Require-File([string]$Path) {
    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
        throw "Required file is missing: $Path"
    }
}

function Require-Adapter([string]$Path) {
    Require-File (Join-Path $Path "adapter_config.json")
    Require-File (Join-Path $Path "adapter_model.safetensors")
}

$candidates = [ordered]@{
    checkpoint250 = Join-Path $trainingRoot "checkpoint-250"
    checkpoint500 = Join-Path $trainingRoot "checkpoint-500"
    checkpoint750 = Join-Path $trainingRoot "checkpoint-750"
    checkpoint1000 = Join-Path $trainingRoot "checkpoint-1000"
}
foreach ($entry in $candidates.GetEnumerator()) {
    Require-Adapter $entry.Value
}

$preflight = & $python -c "import torch; p=torch.cuda.get_device_properties(0); print(torch.cuda.get_device_name(0), p.total_memory, getattr(p, 'pci_bus_id', None))"
if ($LASTEXITCODE -ne 0 -or $preflight -notmatch "RTX 5070 Ti" -or $preflight -notmatch "17094344704") {
    throw "RTX 5070 Ti UUID preflight failed: $preflight"
}
Write-RunLog "GPU verified by UUID: $preflight"

$results = [ordered]@{}
function Invoke-Suite(
    [string]$Label,
    [string]$Adapter,
    [string]$SuiteLabel,
    [string]$DataPath,
    [int]$Rows
) {
    $output = Join-Path $root "outputs_inference\qwen25_3b_clean_pilot1000_${Label}_${SuiteLabel}"
    $stdout = Join-Path $root "logs\qwen25_3b_clean_pilot1000_${Label}_${SuiteLabel}_$RunStamp.out.log"
    $stderr = Join-Path $root "logs\qwen25_3b_clean_pilot1000_${Label}_${SuiteLabel}_$RunStamp.err.log"
    if (Test-Path -LiteralPath $output) {
        $existingReview = Join-Path $output "strict_inference_review.json"
        if (Test-Path -LiteralPath $existingReview -PathType Leaf) {
            $existingMetrics = (Get-Content -LiteralPath $existingReview -Raw | ConvertFrom-Json).metrics
            Write-RunLog "Reusing completed candidate=$Label suite=$SuiteLabel score=$($existingMetrics.average_score) output=$output"
            return $output
        }
        throw "Refusing to overwrite incomplete inference output: $output"
    }
    $arguments = @(
        "run_inference_1000step_adapter.py",
        "--adapter_path", $Adapter,
        "--output_dir", $output,
        "--test_data_path", $DataPath,
        "--subset_size", "$Rows",
        "--manual_limit", "0",
        "--max_length", "512",
        "--max_new_tokens", "160",
        "--repetition_penalty", "1.0",
        "--no_repeat_ngram_size", "0",
        "--local_files_only"
    )
    Write-RunLog "Starting candidate=$Label suite=$SuiteLabel rows=$Rows adapter=$Adapter"
    $process = Start-Process -FilePath $python -ArgumentList $arguments -WorkingDirectory $root `
        -RedirectStandardOutput $stdout -RedirectStandardError $stderr -WindowStyle Hidden -PassThru
    $process.WaitForExit()
    $process.Refresh()
    if ($null -ne $process.ExitCode -and $process.ExitCode -ne 0) {
        throw "Inference failed: candidate=$Label suite=$SuiteLabel exit=$($process.ExitCode) stderr=$stderr"
    }
    $review = Join-Path $output "strict_inference_review.json"
    Require-File $review
    $metrics = (Get-Content -LiteralPath $review -Raw | ConvertFrom-Json).metrics
    Write-RunLog "Completed candidate=$Label suite=$SuiteLabel score=$($metrics.average_score) good=$($metrics.good_predictions_count) bug_acc=$($metrics.bug_id_accuracy) event_acc=$($metrics.event_id_accuracy) date_acc=$($metrics.date_accuracy) command_acc=$($metrics.command_name_accuracy) syntax_acc=$($metrics.command_syntax_preservation) errors=$($metrics.wrong_bug_id_predictions),$($metrics.wrong_event_id_count),$($metrics.wrong_date_predictions),$($metrics.wrong_cli_syntax_predictions)"
    return $output
}

foreach ($entry in $candidates.GetEnumerator()) {
    $label = $entry.Key
    $adapter = $entry.Value
    $results["${label}:clean_balanced100"] = Invoke-Suite $label $adapter "clean_balanced100" $suite 100
    $results["${label}:legacy50_regression"] = Invoke-Suite $label $adapter "legacy50_regression" $legacy 50
}

$selectorArgs = @("select_best_epoch.py")
foreach ($entry in $candidates.GetEnumerator()) {
    $selectorArgs += @("--epoch", "$($entry.Key)=$($entry.Value)")
}
foreach ($entry in $results.GetEnumerator()) {
    $selectorArgs += @("--result", "$($entry.Key)=$($entry.Value)")
}
$selectorArgs += @(
    "--primary_suites", "clean_balanced100",
    "--legacy_suite", "legacy50_regression",
    "--output_dir", $trainingRoot,
    "--allow_hard_failure_fallback",
    "--copy_best"
)
$selectorOut = Join-Path $root "logs\qwen25_3b_clean_checkpoint_selector_$RunStamp.out.log"
$selectorErr = Join-Path $root "logs\qwen25_3b_clean_checkpoint_selector_$RunStamp.err.log"
$selector = Start-Process -FilePath $python -ArgumentList $selectorArgs -WorkingDirectory $root `
    -RedirectStandardOutput $selectorOut -RedirectStandardError $selectorErr -WindowStyle Hidden -PassThru
$selector.WaitForExit()
$selector.Refresh()
if ($null -ne $selector.ExitCode -and $selector.ExitCode -ne 0) {
    throw "Checkpoint selector failed: exit=$($selector.ExitCode) stderr=$selectorErr"
}

$selectionPath = Join-Path $trainingRoot "best_epoch_selection.json"
Require-File $selectionPath
$selection = Get-Content -LiteralPath $selectionPath -Raw | ConvertFrom-Json
if (-not $selection.selected_epoch) {
    throw "All checkpoint candidates failed hard gates"
}
Require-Adapter (Join-Path $trainingRoot "best_lora_adapters")
$completion = [ordered]@{
    completed_at = (Get-Date).ToString("o")
    selected_checkpoint = $selection.selected_epoch
    selected_adapter = $selection.selected_adapter
    copied_best_adapter = (Join-Path $trainingRoot "best_lora_adapters")
    suite = $suite
    results = $results
    selection = $selectionPath
    run_log = $runLog
}
$completion | ConvertTo-Json -Depth 6 | Set-Content -LiteralPath $completionPath -Encoding utf8
Write-RunLog "Selection complete: selected=$($selection.selected_epoch) best=$(Join-Path $trainingRoot 'best_lora_adapters')"
