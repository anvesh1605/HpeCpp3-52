param(
    [string]$InputRoot = 'E:\52\Data_1\final_json',
    [string]$OutputRoot = 'E:\52\Data_1\lstm_conversion\release_notes_final_json_all_switches_v1',
    [string]$Model = 'qwen2.5-coder:7b',
    [int]$Workers = 4,
    [int]$MaxParallelSwitches = 2,
    [string[]]$IncludeSwitch = @(
        '4100i',
        '5420',
        '6000',
        '6100',
        '6200',
        '6300_6300L_6400',
        '8100',
        '8320',
        '8325',
        '8360',
        '8400',
        '9300',
        '9300S_10040',
        '10000'
    )
)

$ErrorActionPreference = 'Stop'
$script = Join-Path $PSScriptRoot 'run_release_notes_10000_ollama_clean.py'
$python = Join-Path (Split-Path $PSScriptRoot -Parent) '.venv\Scripts\python.exe'
if (-not (Test-Path -LiteralPath $python)) {
    $python = (Get-Command python -CommandType Application -ErrorAction Stop).Source
}

if ($Workers -lt 1) {
    throw '--Workers must be >= 1'
}
if ($MaxParallelSwitches -lt 1) {
    throw '--MaxParallelSwitches must be >= 1'
}

$switchDirs = Get-ChildItem -LiteralPath $InputRoot -Directory | Where-Object { $IncludeSwitch -contains $_.Name } | Sort-Object Name
$logRoot = Join-Path $OutputRoot 'logs'
New-Item -ItemType Directory -Force -Path $OutputRoot, $logRoot | Out-Null

Write-Host "[INPUT] root: $InputRoot"
Write-Host "[OUTPUT] root: $OutputRoot"
Write-Host "[MODEL] $Model"
Write-Host "[WORKERS] per switch: $Workers"
Write-Host "[PARALLEL] max switches: $MaxParallelSwitches"
Write-Host "[INCLUDE] $($IncludeSwitch -join ', ')"
Write-Host "[SWITCHES] $($switchDirs.Name -join ', ')"

function Start-SwitchProcess {
    param(
        [System.IO.DirectoryInfo]$SwitchDir
    )

    $switch = $SwitchDir.Name
    $switchOutput = Join-Path $OutputRoot ("release_notes_{0}_cleaned" -f $switch)
    $stdout = Join-Path $logRoot ("release_notes_{0}.out.log" -f $switch)
    $stderr = Join-Path $logRoot ("release_notes_{0}.err.log" -f $switch)
    Write-Host "[SWITCH] start $switch"

    $args = @(
        $script,
        '--input-root', $InputRoot,
        '--output-root', $switchOutput,
        '--switch', $switch,
        '--model', $Model,
        '--workers', $Workers,
        '--force'
    )

    $proc = Start-Process -FilePath $python -ArgumentList $args -WorkingDirectory $PSScriptRoot -WindowStyle Hidden -PassThru -RedirectStandardOutput $stdout -RedirectStandardError $stderr
    [pscustomobject]@{
        Switch = $switch
        Process = $proc
        Stdout = $stdout
        Stderr = $stderr
        OutputRoot = $switchOutput
    }
}

$pendingIndex = 0
$active = New-Object 'System.Collections.Generic.List[object]'

while ($pendingIndex -lt $switchDirs.Count -or $active.Count -gt 0) {
    while ($pendingIndex -lt $switchDirs.Count -and $active.Count -lt $MaxParallelSwitches) {
        $active.Add((Start-SwitchProcess -SwitchDir $switchDirs[$pendingIndex]))
        $pendingIndex++
    }

    for ($i = $active.Count - 1; $i -ge 0; $i--) {
        $item = $active[$i]
        if ($item.Process.HasExited) {
            $item.Process.WaitForExit()
            Write-Host "[SWITCH] end $($item.Switch) exit_code=$($item.Process.ExitCode)"
            $active.RemoveAt($i)
        }
    }

    if ($pendingIndex -lt $switchDirs.Count -or $active.Count -gt 0) {
        Start-Sleep -Seconds 5
    }
}

Write-Host '[DONE] all switches processed'
