param(
    [string]$RunStamp = (Get-Date -Format 'yyyyMMdd_HHmmss')
)

$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '.')).Path
Set-Location -LiteralPath $root

$python = (Resolve-Path '.\.venv312\Scripts\python.exe').Path
$trainScript = (Resolve-Path '.\train.py').Path
$inferScript = (Resolve-Path '.\run_inference_1000step_adapter.py').Path

$trainData = 'Data\all_switches\train_chat_all_clean_validated.jsonl'
$valData = 'Data\all_switches\val_chat_all_clean.jsonl'
$trainOutput = Join-Path $root "outputs_final\tinyllama_all_data_1epoch_qlora_$RunStamp"
$inferOutput = Join-Path $root "outputs_inference\tinyllama_all_data_1epoch_qlora_$RunStamp_train_smoke"

$trainOut = Join-Path $root "logs\tinyllama_all_data_1epoch_qlora_$RunStamp.train.out.log"
$trainErr = Join-Path $root "logs\tinyllama_all_data_1epoch_qlora_$RunStamp.train.err.log"
$inferOut = Join-Path $root "logs\tinyllama_all_data_1epoch_qlora_$RunStamp.traininfer.out.log"
$inferErr = Join-Path $root "logs\tinyllama_all_data_1epoch_qlora_$RunStamp.traininfer.err.log"
$launcherLog = Join-Path $root "logs\tinyllama_all_data_1epoch_qlora_$RunStamp.launcher.log"

function Write-RunLog([string]$Message) {
    $line = "$(Get-Date -Format o) | $Message"
    $line | Add-Content -LiteralPath $launcherLog -Encoding utf8
    Write-Output $line
}

function Require-Dir([string]$Path) {
    if (-not (Test-Path -LiteralPath $Path -PathType Container)) {
        throw "Required directory is missing: $Path"
    }
}

function Require-File([string]$Path) {
    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
        throw "Required file is missing: $Path"
    }
}

Require-Dir (Split-Path -Parent $launcherLog)
Require-File (Join-Path $root $trainData)
Require-File (Join-Path $root $valData)

if (Test-Path -LiteralPath $trainOutput) {
    throw "Refusing to overwrite existing training output: $trainOutput"
}
if (Test-Path -LiteralPath $inferOutput) {
    throw "Refusing to overwrite existing inference output: $inferOutput"
}

$env:CUDA_DEVICE_ORDER = 'PCI_BUS_ID'
$env:CUDA_VISIBLE_DEVICES = '1'
$env:PYTHONUTF8 = '1'

Write-RunLog "Starting TinyLlama QLoRA 1-epoch run on combined data."
Write-RunLog "Train data: $trainData"
Write-RunLog "Val data: $valData"
Write-RunLog "Training output: $trainOutput"
Write-RunLog "Training logs: $trainOut / $trainErr"

$trainArgs = @(
    $trainScript,
    '--data_path', $trainData,
    '--val_data_path', $valData,
    '--model_name', 'TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    '--template', 'tinyllama',
    '--output_dir', $trainOutput,
    '--max_length', '512',
    '--batch_size', '2',
    '--grad_accum', '8',
    '--epochs', '1',
    '--lr', '2e-4',
    '--lora_r', '16',
    '--lora_alpha', '32',
    '--lora_dropout', '0.05',
    '--max_grad_norm', '0.1',
    '--warmup_ratio', '0.03',
    '--weight_decay', '0.0',
    '--optim', 'paged_adamw_32bit',
    '--logging_steps', '10',
    '--save_steps', '1000',
    '--checkpoint_steps', '1000,2000,3000',
    '--save_total_limit', '4',
    '--bf16',
    '--no-select_best_by_eval_loss',
    '--no-teacher_eval_during_training',
    '--stop_on_nan',
    '--run_name', "tinyllama-all-data-1epoch-qlora-$RunStamp"
)

$trainProc = Start-Process -FilePath $python -ArgumentList $trainArgs -WorkingDirectory $root `
    -WindowStyle Hidden -PassThru -RedirectStandardOutput $trainOut -RedirectStandardError $trainErr
Write-RunLog "Training PID: $($trainProc.Id)"
$trainProc.WaitForExit()
$trainProc.Refresh()
if ($trainProc.ExitCode -ne 0) {
    Write-RunLog "Training failed with exit code $($trainProc.ExitCode)"
    exit $trainProc.ExitCode
}
Write-RunLog "Training completed successfully."

$adapterPath = Join-Path $trainOutput 'lora_adapters'
Write-RunLog "Starting train-set inference smoke test."
Write-RunLog "Inference output: $inferOutput"
Write-RunLog "Inference logs: $inferOut / $inferErr"

$inferArgs = @(
    $inferScript,
    '--model_name', 'TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    '--adapter_path', $adapterPath,
    '--output_dir', $inferOutput,
    '--test_data_path', $trainData,
    '--subset_size', '25',
    '--manual_limit', '6',
    '--max_length', '512',
    '--max_new_tokens', '120',
    '--repetition_penalty', '1.1',
    '--no_repeat_ngram_size', '4'
)

$inferProc = Start-Process -FilePath $python -ArgumentList $inferArgs -WorkingDirectory $root `
    -WindowStyle Hidden -PassThru -RedirectStandardOutput $inferOut -RedirectStandardError $inferErr
Write-RunLog "Inference PID: $($inferProc.Id)"
$inferProc.WaitForExit()
$inferProc.Refresh()
if ($inferProc.ExitCode -ne 0) {
    Write-RunLog "Inference failed with exit code $($inferProc.ExitCode)"
    exit $inferProc.ExitCode
}
Write-RunLog "Inference completed successfully."
Write-RunLog "Done. Training output: $trainOutput"
Write-RunLog "Done. Inference output: $inferOutput"
