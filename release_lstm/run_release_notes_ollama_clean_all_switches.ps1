param(
    [string]$InputRoot = 'E:\52\Train\Train\Data\final_json',
    [string]$OutputRoot = 'E:\52\Train\Train\Data\all_switches\ollama_release_notes_cleaning',
    [string]$Model = 'qwen2.5-coder:7b',
    [int]$Workers = 8,
    [string[]]$ExcludeSwitch = @('10000')
)

$ErrorActionPreference = 'Stop'
$script = 'E:\52\Train\Train\scripts\run_release_notes_10000_ollama_clean.py'

if ($Workers -lt 1) {
    throw '--Workers must be >= 1'
}

$switchDirs = Get-ChildItem -LiteralPath $InputRoot -Directory | Where-Object { $ExcludeSwitch -notcontains $_.Name } | Sort-Object Name
Write-Host "[INPUT] root: $InputRoot"
Write-Host "[OUTPUT] root: $OutputRoot"
Write-Host "[MODEL] $Model"
Write-Host "[WORKERS] $Workers"
Write-Host "[SWITCHES] $($switchDirs.Name -join ', ')"

foreach ($switchDir in $switchDirs) {
    $switch = $switchDir.Name
    $switchOutput = Join-Path $OutputRoot ("release_notes_{0}_cleaned" -f $switch)
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
    & python @args
    $exitCode = $LASTEXITCODE
    Write-Host "[SWITCH] end $switch exit_code=$exitCode"
    if ($exitCode -ne 0) {
        Write-Host "[SWITCH] continuing after failure: $switch"
    }
}

Write-Host '[DONE] all non-10000 switches processed'
