param(
    [Parameter(Mandatory = $true)]
    [string]$RunStamp
)

$ErrorActionPreference = "Stop"
$root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
Set-Location -LiteralPath $root

$slug = "qwen25_3b_clean_pilot1000_$RunStamp"
$trainingOut = Join-Path $root "logs\$slug.out.log"
$trainingErr = Join-Path $root "logs\$slug.err.log"
$gpuLog = Join-Path $root "logs\$slug.gpu.csv"
$launchPath = Join-Path $root "logs\$slug.launch.json"
$completionPath = Join-Path $root "logs\$slug.completion.json"
$python = (Resolve-Path ".\.venv312\Scripts\python.exe").Path
$trainScript = (Resolve-Path ".\train.py").Path

$physicalGpuUuid = "GPU-f1d815f0-db71-9d96-3a88-155d7c032f68"
$env:CUDA_VISIBLE_DEVICES = $physicalGpuUuid
$env:PYTHONUTF8 = "1"

$arguments = @(
    $trainScript,
    "--data_path", "final_json_clean\all_switches\train_chat_all_clean.jsonl",
    "--val_data_path", "final_json_clean\all_switches\val_chat_all_clean.jsonl",
    "--model_name", "Qwen/Qwen2.5-3B-Instruct",
    "--template", "chatml",
    "--output_dir", "outputs_final\qwen25_3b_clean_pilot1000",
    "--max_length", "512",
    "--batch_size", "1",
    "--grad_accum", "8",
    "--epochs", "1",
    "--max_steps", "1000",
    "--lr", "1e-5",
    "--lora_r", "16",
    "--lora_alpha", "32",
    "--lora_dropout", "0.05",
    "--max_grad_norm", "0.3",
    "--warmup_ratio", "0.03",
    "--weight_decay", "0.0",
    "--optim", "paged_adamw_32bit",
    "--logging_steps", "10",
    "--eval_steps", "250",
    "--save_steps", "250",
    "--checkpoint_steps", "250,500,750,1000",
    "--save_total_limit", "5",
    "--no-select_best_by_eval_loss",
    "--no-teacher_eval_during_training",
    "--stop_on_nan",
    "--run_name", "qwen25-3b-clean-pilot1000"
)

$gpuArguments = @(
    "--id=1",
    "--query-gpu=timestamp,index,name,pci.bus_id,uuid,utilization.gpu,memory.used,memory.total,temperature.gpu,power.draw",
    "--format=csv,noheader,nounits",
    "--loop-ms=10000"
)

$gpuProcess = Start-Process -FilePath "nvidia-smi.exe" -ArgumentList $gpuArguments `
    -WindowStyle Hidden -PassThru -RedirectStandardOutput $gpuLog

$trainingProcess = Start-Process -FilePath $python -ArgumentList $arguments `
    -WindowStyle Hidden -PassThru -RedirectStandardOutput $trainingOut -RedirectStandardError $trainingErr

$launch = [ordered]@{
    started_at = (Get-Date).ToString("o")
    launcher_pid = $PID
    training_pid = $trainingProcess.Id
    gpu_monitor_pid = $gpuProcess.Id
    cuda_visible_devices = $physicalGpuUuid
    physical_gpu = "NVIDIA GeForce RTX 5070 Ti"
    physical_bus = "65:00.0"
    physical_uuid = "GPU-f1d815f0-db71-9d96-3a88-155d7c032f68"
    output_dir = (Join-Path $root "outputs_final\qwen25_3b_clean_pilot1000")
    stdout = $trainingOut
    stderr = $trainingErr
    gpu_log = $gpuLog
    completion = $completionPath
    command_arguments = $arguments
}
$launch | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath $launchPath -Encoding UTF8

$trainingProcess.WaitForExit()
$exitCode = $trainingProcess.ExitCode

if (-not $gpuProcess.HasExited) {
    Stop-Process -Id $gpuProcess.Id -Force
}

$completion = [ordered]@{
    completed_at = (Get-Date).ToString("o")
    exit_code = $exitCode
    output_dir = $launch.output_dir
    stdout = $trainingOut
    stderr = $trainingErr
    gpu_log = $gpuLog
}
$completion | ConvertTo-Json | Set-Content -LiteralPath $completionPath -Encoding UTF8
exit $exitCode
