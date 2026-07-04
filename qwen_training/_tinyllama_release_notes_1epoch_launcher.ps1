$ErrorActionPreference = 'Stop'
$root = 'E:\52\Train_w\Train'
Set-Location -LiteralPath $root

$python = Join-Path $root '.venv312\Scripts\python.exe'
$trainScript = Join-Path $root 'train.py'
$inferScript = Join-Path $root 'run_inference_1000step_adapter.py'

$trainData = 'Data\all_switches\release_notes_only_structured_full\release_notes_only_structured_full_train.jsonl'
$valData = 'Data\all_switches\release_notes_only_structured_full\release_notes_only_structured_full_val.jsonl'
$trainOutput = Join-Path $root 'outputs_final\tinyllama_release_notes_only_fullfacts_1epoch_qlora_20260629_000000'
$inferOutput = Join-Path $root 'outputs_inference\tinyllama_release_notes_only_fullfacts_1epoch_qlora_20260629_000000_train_smoke'

$trainOut = Join-Path $root 'logs\tinyllama_release_notes_only_fullfacts_1epoch_qlora_20260629_000000.train.out.log'
$trainErr = Join-Path $root 'logs\tinyllama_release_notes_only_fullfacts_1epoch_qlora_20260629_000000.train.err.log'
$inferOut = Join-Path $root 'logs\tinyllama_release_notes_only_fullfacts_1epoch_qlora_20260629_000000.traininfer.out.log'
$inferErr = Join-Path $root 'logs\tinyllama_release_notes_only_fullfacts_1epoch_qlora_20260629_000000.traininfer.err.log'
$launcherLog = Join-Path $root 'logs\tinyllama_release_notes_only_fullfacts_1epoch_qlora_20260629_000000.launcher.log'

function Write-RunLog([string]$Message) {
    $line = "$(Get-Date -Format o) | $Message"
    $line | Add-Content -LiteralPath $launcherLog -Encoding utf8
    Write-Output $line
}

New-Item -ItemType Directory -Force -Path (Split-Path -Parent $trainOut) | Out-Null
New-Item -ItemType Directory -Force -Path (Split-Path -Parent $inferOut) | Out-Null

if (Test-Path -LiteralPath $trainOutput) {
    throw "Refusing to overwrite existing training output: $trainOutput"
}
if (Test-Path -LiteralPath $inferOutput) {
    throw "Refusing to overwrite existing inference output: $inferOutput"
}

$env:CUDA_DEVICE_ORDER = 'PCI_BUS_ID'
$env:CUDA_VISIBLE_DEVICES = '1'
$env:PYTHONUTF8 = '1'

Write-RunLog "Starting TinyLlama QLoRA 1-epoch training"
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
    '--checkpoint_steps', '1000,2000',
    '--save_total_limit', '4',
    '--bf16',
    '--no-select_best_by_eval_loss',
    '--no-teacher_eval_during_training',
    '--stop_on_nan',
    '--run_name', 'tinyllama-release-notes-only-fullfacts-1epoch-qlora-20260629_000000'
)

$trainProc = Start-Process -FilePath $python -ArgumentList $trainArgs -WorkingDirectory $root -WindowStyle Hidden -PassThru -RedirectStandardOutput $trainOut -RedirectStandardError $trainErr
Write-RunLog "Training PID: $($trainProc.Id)"
$trainProc.WaitForExit()
$trainProc.Refresh()
if ($trainProc.ExitCode -ne 0) {
    Write-RunLog "Training failed with exit code $($trainProc.ExitCode)"
    exit $trainProc.ExitCode
}
Write-RunLog 'Training completed successfully.'

$adapterPath = Join-Path $trainOutput 'lora_adapters'
Write-RunLog "Starting train-set inference smoke test"
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

$inferProc = Start-Process -FilePath $python -ArgumentList $inferArgs -WorkingDirectory $root -WindowStyle Hidden -PassThru -RedirectStandardOutput $inferOut -RedirectStandardError $inferErr
Write-RunLog "Inference PID: $($inferProc.Id)"
$inferProc.WaitForExit()
$inferProc.Refresh()
if ($inferProc.ExitCode -ne 0) {
    Write-RunLog "Inference failed with exit code $($inferProc.ExitCode)"
    exit $inferProc.ExitCode
}
Write-RunLog 'Inference completed successfully.'
Write-RunLog "Done. Train output: $trainOutput"
Write-RunLog "Done. Inference output: $inferOutput"
