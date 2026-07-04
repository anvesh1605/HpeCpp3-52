param(
    [string]$RunStamp = (Get-Date -Format 'yyyyMMdd_HHmmss')
)

$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
Set-Location -LiteralPath $root

$python = (Resolve-Path '.\.venv312\Scripts\python.exe').Path
$trainScript = (Resolve-Path '.\train.py').Path
$splitScript = (Resolve-Path '.\prepare_release_notes_only_split.py').Path
$suitesScript = (Resolve-Path '.\prepare_release_notes_only_eval_suites.py').Path
$postTrainingScript = (Resolve-Path '.\scripts\run_release_notes_only_3b_post_training.ps1').Path

$gpuUuid = 'GPU-f1d815f0-db71-9d96-3a88-155d7c032f68'
$env:CUDA_DEVICE_ORDER = 'PCI_BUS_ID'
$env:CUDA_VISIBLE_DEVICES = $gpuUuid
$env:PYTHONUTF8 = '1'

$splitDir = Join-Path $root 'Data\final_json_release_repaired_v1\release_only_stratified_seed42'
$splitManifest = Join-Path $splitDir 'manifest.json'
$suiteSummary = Join-Path $splitDir 'release_eval_suites_manifest.json'
$trainingOutput = Join-Path $root 'outputs_final\qwen25_3b_release_notes_only_1epoch_stratified'
$sanityOutput = Join-Path $root "outputs_debug\qwen25_3b_release_notes_only_sanity_$RunStamp"

$launcherOut = Join-Path $root "logs\qwen25_3b_release_notes_only_1epoch_stratified_$RunStamp.launcher.out.log"
$launcherErr = Join-Path $root "logs\qwen25_3b_release_notes_only_1epoch_stratified_$RunStamp.launcher.err.log"
$launcherLog = Join-Path $root "logs\qwen25_3b_release_notes_only_1epoch_stratified_$RunStamp.log"
$gpuLog = Join-Path $root "logs\qwen25_3b_release_notes_only_1epoch_stratified_$RunStamp.gpu.csv"
$launchPath = Join-Path $root "logs\qwen25_3b_release_notes_only_1epoch_stratified_$RunStamp.launch.json"
$completionPath = Join-Path $root "logs\qwen25_3b_release_notes_only_1epoch_stratified_$RunStamp.completion.json"
$postTrainingLog = Join-Path $root "logs\qwen25_3b_release_notes_only_1epoch_stratified_$RunStamp.post_training.log"

function Write-RunLog([string]$Message) {
    $line = "$(Get-Date -Format o) | $Message"
    $line | Add-Content -LiteralPath $launcherLog -Encoding utf8
    Write-Host $line
}

function Require-File([string]$Path) {
    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
        throw "Required file is missing: $Path"
    }
}

function Require-Dir([string]$Path) {
    if (-not (Test-Path -LiteralPath $Path -PathType Container)) {
        throw "Required directory is missing: $Path"
    }
}

function Invoke-Python([string[]]$Arguments, [string]$Stdout, [string]$Stderr) {
    $process = Start-Process -FilePath $python -ArgumentList $Arguments -WorkingDirectory $root `
        -WindowStyle Hidden -PassThru -RedirectStandardOutput $Stdout -RedirectStandardError $Stderr
    $process.WaitForExit()
    $process.Refresh()
    if ($null -ne $process.ExitCode -and $process.ExitCode -ne 0) {
        throw "Python command failed with exit code $($process.ExitCode): $($Arguments -join ' ')"
    }
}

Require-Dir (Split-Path -Parent $launcherLog)
Require-Dir (Split-Path -Parent $gpuLog)

if (-not (Test-Path -LiteralPath $splitManifest -PathType Leaf)) {
    Write-RunLog "Preparing release-only split: $splitDir"
    Invoke-Python @(
        $splitScript,
        '--input_path', 'Data\final_json_release_repaired_v1\release_notes_final_clean.jsonl',
        '--output_dir', $splitDir,
        '--test_path', 'Data\all_switches\test_chat_all_clean.jsonl',
        '--validation_ratio', '0.05',
        '--seed', '42',
        '--effective_batch_size', '8'
    ) "$launcherLog.split.out.log" "$launcherLog.split.err.log"
}
Require-File $splitManifest

if (-not (Test-Path -LiteralPath $suiteSummary -PathType Leaf)) {
    Write-RunLog "Preparing release-only inference suites: $splitDir"
    Invoke-Python @(
        $suitesScript,
        '--split_dir', $splitDir,
        '--seed', '43'
    ) "$launcherLog.suites.out.log" "$launcherLog.suites.err.log"
}
Require-File $suiteSummary

$manifest = Get-Content -LiteralPath $splitManifest -Raw | ConvertFrom-Json
$stepsPerEpoch = [int]$manifest.steps_per_epoch
if ($stepsPerEpoch -le 0) {
    throw "Invalid steps_per_epoch in manifest: $stepsPerEpoch"
}
$checkpointSteps = New-Object System.Collections.Generic.List[int]
for ($step = 1000; $step -lt $stepsPerEpoch; $step += 1000) {
    [void]$checkpointSteps.Add($step)
}
if (-not $checkpointSteps.Contains($stepsPerEpoch)) {
    [void]$checkpointSteps.Add($stepsPerEpoch)
}
$checkpointStepsText = ($checkpointSteps -join ',')

Write-RunLog "Checkpoint schedule: $checkpointStepsText"

$sanityArgs = @(
    $trainScript,
    '--data_path', (Join-Path $splitDir 'train_chat_release_only.jsonl'),
    '--val_data_path', (Join-Path $splitDir 'val_chat_release_only.jsonl'),
    '--model_name', 'Qwen/Qwen2.5-3B-Instruct',
    '--template', 'chatml',
    '--output_dir', $sanityOutput,
    '--max_length', '512',
    '--batch_size', '1',
    '--grad_accum', '8',
    '--epochs', '1',
    '--sanity_steps', '20',
    '--lr', '8e-6',
    '--lora_r', '8',
    '--lora_alpha', '16',
    '--lora_dropout', '0.05',
    '--max_grad_norm', '0.1',
    '--warmup_ratio', '0.03',
    '--weight_decay', '0.0',
    '--optim', 'paged_adamw_32bit',
    '--logging_steps', '10',
    '--save_steps', '1000',
    '--checkpoint_steps', '1000',
    '--save_total_limit', '2',
    '--bf16',
    '--no-select_best_by_eval_loss',
    '--no-teacher_eval_during_training',
    '--stop_on_nan',
    '--run_name', "qwen25-3b-release-notes-only-sanity-$RunStamp"
)

Write-RunLog "Starting sanity run: output=$sanityOutput"
$sanityStdout = Join-Path $root "logs\qwen25_3b_release_notes_only_sanity_$RunStamp.out.log"
$sanityStderr = Join-Path $root "logs\qwen25_3b_release_notes_only_sanity_$RunStamp.err.log"
$sanityGpu = Join-Path $root "logs\qwen25_3b_release_notes_only_sanity_$RunStamp.gpu.csv"
$sanityGpuProcess = Start-Process -FilePath 'nvidia-smi.exe' -ArgumentList @(
    '--id=1',
    '--query-gpu=timestamp,index,name,pci.bus_id,uuid,utilization.gpu,memory.used,memory.total,temperature.gpu,power.draw',
    '--format=csv,noheader,nounits',
    '--loop-ms=10000'
) -WindowStyle Hidden -PassThru -RedirectStandardOutput $sanityGpu
$sanityProcess = Start-Process -FilePath $python -ArgumentList $sanityArgs -WorkingDirectory $root `
    -WindowStyle Hidden -PassThru -RedirectStandardOutput $sanityStdout -RedirectStandardError $sanityStderr
$sanityProcess.WaitForExit()
if (-not $sanityGpuProcess.HasExited) {
    Stop-Process -Id $sanityGpuProcess.Id -Force
}
if ($null -ne $sanityProcess.ExitCode -and $sanityProcess.ExitCode -ne 0) {
    throw "Sanity run failed with exit code $($sanityProcess.ExitCode). Check $sanityStdout and $sanityStderr"
}
if (Select-String -LiteralPath $sanityStdout, $sanityStderr -Pattern '(?i)(Traceback|CUDA out of memory|OutOfMemoryError|stopping training due to non-finite|stopping training due to NaN/Inf metrics|NaNStoppingCallback)' -Quiet -ErrorAction SilentlyContinue) {
    throw "Sanity logs contain a fatal pattern; refusing to start full training."
}
Write-RunLog "Sanity run completed successfully."

if (Test-Path -LiteralPath $trainingOutput) {
    throw "Refusing to overwrite existing training output: $trainingOutput"
}
New-Item -ItemType Directory -Path $trainingOutput -Force | Out-Null

$trainingArgs = @(
    $trainScript,
    '--data_path', (Join-Path $splitDir 'train_chat_release_only.jsonl'),
    '--val_data_path', (Join-Path $splitDir 'val_chat_release_only.jsonl'),
    '--model_name', 'Qwen/Qwen2.5-3B-Instruct',
    '--template', 'chatml',
    '--output_dir', $trainingOutput,
    '--max_length', '512',
    '--batch_size', '1',
    '--grad_accum', '8',
    '--epochs', '1',
    '--lr', '8e-6',
    '--lora_r', '8',
    '--lora_alpha', '16',
    '--lora_dropout', '0.05',
    '--max_grad_norm', '0.1',
    '--warmup_ratio', '0.03',
    '--weight_decay', '0.0',
    '--optim', 'paged_adamw_32bit',
    '--logging_steps', '10',
    '--save_steps', '1000',
    '--checkpoint_steps', $checkpointStepsText,
    '--save_total_limit', '8',
    '--bf16',
    '--no-select_best_by_eval_loss',
    '--no-teacher_eval_during_training',
    '--stop_on_nan',
    '--run_name', "qwen25-3b-release-notes-only-1epoch-$RunStamp"
)

$trainOut = Join-Path $root "logs\qwen25_3b_release_notes_only_1epoch_stratified_$RunStamp.out.log"
$trainErr = Join-Path $root "logs\qwen25_3b_release_notes_only_1epoch_stratified_$RunStamp.err.log"
$trainGpu = Join-Path $root "logs\qwen25_3b_release_notes_only_1epoch_stratified_$RunStamp.gpu.csv"
$trainLaunchPath = Join-Path $root "logs\qwen25_3b_release_notes_only_1epoch_stratified_$RunStamp.launch.json"
$trainCompletionPath = Join-Path $root "logs\qwen25_3b_release_notes_only_1epoch_stratified_$RunStamp.completion.json"

Write-RunLog "Launching full training: output=$trainingOutput"
$gpuProcess = Start-Process -FilePath 'nvidia-smi.exe' -ArgumentList @(
    '--id=1',
    '--query-gpu=timestamp,index,name,pci.bus_id,uuid,utilization.gpu,memory.used,memory.total,temperature.gpu,power.draw',
    '--format=csv,noheader,nounits',
    '--loop-ms=10000'
) -WindowStyle Hidden -PassThru -RedirectStandardOutput $trainGpu
$trainingProcess = Start-Process -FilePath $python -ArgumentList $trainingArgs -WorkingDirectory $root `
    -WindowStyle Hidden -PassThru -RedirectStandardOutput $trainOut -RedirectStandardError $trainErr

$launch = [ordered]@{
    started_at = (Get-Date).ToString('o')
    launcher_pid = $PID
    training_pid = $trainingProcess.Id
    gpu_monitor_pid = $gpuProcess.Id
    cuda_visible_devices = $gpuUuid
    physical_gpu = 'NVIDIA GeForce RTX 5070 Ti'
    physical_bus = '65:00.0'
    physical_uuid = $gpuUuid
    output_dir = $trainingOutput
    stdout = $trainOut
    stderr = $trainErr
    gpu_log = $trainGpu
    completion = $trainCompletionPath
    checkpoint_steps = $checkpointStepsText
    split_manifest = $splitManifest
    suites_manifest = $suiteSummary
    sanity_output = $sanityOutput
}
$launch | ConvertTo-Json -Depth 6 | Set-Content -LiteralPath $trainLaunchPath -Encoding UTF8

$evalArgs = @(
    '-File', $postTrainingScript,
    '-TrainingPid', "$($trainingProcess.Id)",
    '-TrainingOutput', $trainingOutput,
    '-TrainingStdout', $trainOut,
    '-TrainingStderr', $trainErr,
    '-LogPath', $postTrainingLog,
    '-SplitManifest', $splitManifest,
    '-SuiteManifest', $suiteSummary,
    '-RunStamp', $RunStamp
)
$evalProcess = Start-Process -FilePath 'powershell' -ArgumentList $evalArgs -WorkingDirectory $root `
    -WindowStyle Hidden -PassThru

$launch += [ordered]@{
    post_training_pid = $evalProcess.Id
    post_training_log = $postTrainingLog
}
$launch | ConvertTo-Json -Depth 6 | Set-Content -LiteralPath $trainLaunchPath -Encoding UTF8
Write-RunLog "Training launcher ready. launch=$trainLaunchPath"
Write-RunLog "Monitor logs: stdout=$trainOut stderr=$trainErr gpu=$trainGpu sanity=$sanityStdout,$sanityStderr post_training=$postTrainingLog"
