param(
    [string]$RunStamp = (Get-Date -Format 'yyyyMMdd_HHmmss')
)

$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '.')).Path
Set-Location -LiteralPath $root

$python = (Resolve-Path '.\.venv312\Scripts\python.exe').Path
$builderScript = (Resolve-Path '.\build_tinyllama_all_roots_trainchat_split.py').Path
$trainScript = (Resolve-Path '.\train.py').Path
$inferScript = (Resolve-Path '.\run_inference_1000step_adapter.py').Path

$splitDir = Join-Path $root "Data\all_switches\tinyllama_all_roots_trainchat_seed42"
$trainData = Join-Path $splitDir 'train_chat_all_roots_train.jsonl'
$valData = Join-Path $splitDir 'train_chat_all_roots_val.jsonl'
$builderOut = Join-Path $root "logs\tinyllama_all_roots_trainchat_1epoch_qlora_$RunStamp.builder.out.log"
$builderErr = Join-Path $root "logs\tinyllama_all_roots_trainchat_1epoch_qlora_$RunStamp.builder.err.log"
$trainOutput = Join-Path $root "outputs_final\tinyllama_all_roots_trainchat_1epoch_qlora_$RunStamp"
$inferOutput = Join-Path $root "outputs_inference\tinyllama_all_roots_trainchat_1epoch_qlora_$RunStamp_train_smoke"
$trainOut = Join-Path $root "logs\tinyllama_all_roots_trainchat_1epoch_qlora_$RunStamp.train.out.log"
$trainErr = Join-Path $root "logs\tinyllama_all_roots_trainchat_1epoch_qlora_$RunStamp.train.err.log"
$inferOut = Join-Path $root "logs\tinyllama_all_roots_trainchat_1epoch_qlora_$RunStamp.traininfer.out.log"
$inferErr = Join-Path $root "logs\tinyllama_all_roots_trainchat_1epoch_qlora_$RunStamp.traininfer.err.log"
$launcherLog = Join-Path $root "logs\tinyllama_all_roots_trainchat_1epoch_qlora_$RunStamp.launcher.log"

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
Require-File $builderScript

if (Test-Path -LiteralPath $splitDir) {
    Remove-Item -LiteralPath $splitDir -Recurse -Force
}
if (Test-Path -LiteralPath $trainOutput) {
    throw "Refusing to overwrite existing training output: $trainOutput"
}
if (Test-Path -LiteralPath $inferOutput) {
    throw "Refusing to overwrite existing inference output: $inferOutput"
}

$env:CUDA_DEVICE_ORDER = 'PCI_BUS_ID'
$env:CUDA_VISIBLE_DEVICES = '1'
$env:PYTHONUTF8 = '1'

Write-RunLog "Building train/val split from raw train_chat.jsonl roots."
Write-RunLog "Final JSON root: E:\52\Train_w\Train\Data\final_json"
Write-RunLog "Product docs root: E:\52\Train_w\Train\Data\product_docs\full_product_docs"

$builderArgs = @(
    $builderScript,
    '--final_json_root', 'E:\52\Train_w\Train\Data\final_json',
    '--product_docs_root', 'E:\52\Train_w\Train\Data\product_docs\full_product_docs',
    '--output_dir', $splitDir,
    '--validation_ratio', '0.05',
    '--seed', '42'
)
$builderProc = Start-Process -FilePath $python -ArgumentList $builderArgs -WorkingDirectory $root `
    -WindowStyle Hidden -PassThru -RedirectStandardOutput $builderOut -RedirectStandardError $builderErr
Write-RunLog "Builder PID: $($builderProc.Id)"
$builderProc.WaitForExit()
$builderProc.Refresh()
$builderExit = $builderProc.ExitCode
if ($builderExit -and $builderExit -ne 0) {
    Write-RunLog "Builder failed with exit code $builderExit"
    exit $builderProc.ExitCode
}
Require-File $trainData
Require-File $valData
Write-RunLog "Split built successfully."
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
    '--batch_size', '4',
    '--grad_accum', '4',
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
    '--checkpoint_steps', '1000,3000,5000,7000',
    '--save_total_limit', '4',
    '--bf16',
    '--no-select_best_by_eval_loss',
    '--no-teacher_eval_during_training',
    '--stop_on_nan',
    '--run_name', "tinyllama-all-roots-trainchat-1epoch-qlora-$RunStamp"
)

$trainProc = Start-Process -FilePath $python -ArgumentList $trainArgs -WorkingDirectory $root `
    -WindowStyle Hidden -PassThru -RedirectStandardOutput $trainOut -RedirectStandardError $trainErr
Write-RunLog "Training PID: $($trainProc.Id)"
$trainProc.WaitForExit()
$trainProc.Refresh()
$trainExit = $trainProc.ExitCode
if ($trainExit -and $trainExit -ne 0) {
    Write-RunLog "Training failed with exit code $trainExit"
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
$inferExit = $inferProc.ExitCode
if ($inferExit -and $inferExit -ne 0) {
    Write-RunLog "Inference failed with exit code $inferExit"
    exit $inferProc.ExitCode
}
Write-RunLog "Inference completed successfully."
Write-RunLog "Done. Training output: $trainOutput"
Write-RunLog "Done. Inference output: $inferOutput"
