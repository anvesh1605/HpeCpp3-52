param(
    [string]$ProjectRoot = "E:\52\test4_html\project",
    [string]$RawRoot = "E:\52\test4_html\markitdown_Raw_Data"
)

$ErrorActionPreference = "Stop"

$Preprocess = Join-Path $ProjectRoot "preprocess_release_notes.py"
$Postprocess = Join-Path $ProjectRoot "postprocess_final_json.py"
$OutputRoot = Join-Path $ProjectRoot "data\processed_md"
$FinalRoot = Join-Path $ProjectRoot "final_json"
$LogPath = Join-Path $ProjectRoot "run_all_release_notes.log"
$ProgressPath = Join-Path $ProjectRoot "run_all_release_notes.progress.json"

function Get-SwitchName {
    param([string]$FolderName)
    $name = $FolderName -replace '^Aruba_', ''
    $name = $name -replace '(?i)_html_content$', ''
    return $name
}

function Write-ProgressJson {
    param(
        [int]$Total,
        [int]$Done,
        [int]$Failed,
        [string]$Current,
        [string]$Status
    )
    [ordered]@{
        total = $Total
        done = $Done
        failed = $Failed
        current = $Current
        status = $Status
        updated_at = (Get-Date).ToString("s")
    } | ConvertTo-Json | Set-Content -LiteralPath $ProgressPath -Encoding UTF8
}

$targets = @()
foreach ($switchDir in Get-ChildItem -Directory -LiteralPath $RawRoot) {
    $switchName = Get-SwitchName $switchDir.Name
    foreach ($versionDir in Get-ChildItem -Directory -LiteralPath $switchDir.FullName) {
        foreach ($subVersionDir in Get-ChildItem -Directory -LiteralPath $versionDir.FullName) {
            if (Get-ChildItem -LiteralPath $subVersionDir.FullName -Recurse -Filter "*.md" -File -ErrorAction SilentlyContinue | Select-Object -First 1) {
                $targets += [pscustomobject]@{
                    SwitchName = $switchName
                    Version = $versionDir.Name
                    SubVersion = $subVersionDir.Name
                    InputRoot = $subVersionDir.FullName
                    FinalJsonl = Join-Path $FinalRoot (Join-Path $switchName (Join-Path $versionDir.Name (Join-Path $subVersionDir.Name "train_chat.jsonl")))
                }
            }
        }
    }
}

$total = $targets.Count
$done = 0
$failed = 0

"[$(Get-Date -Format s)] Starting full preprocessing run. Targets: $total" | Set-Content -LiteralPath $LogPath -Encoding UTF8
Write-ProgressJson -Total $total -Done $done -Failed $failed -Current "" -Status "running"

foreach ($target in $targets) {
    $current = "$($target.SwitchName)/$($target.Version)/$($target.SubVersion)"
    Write-ProgressJson -Total $total -Done $done -Failed $failed -Current $current -Status "running"
    "[$(Get-Date -Format s)] START $current" | Add-Content -LiteralPath $LogPath -Encoding UTF8

    $output = & python $Preprocess `
        --input-root $target.InputRoot `
        --output-root $OutputRoot `
        --switch-name $target.SwitchName `
        --version $target.Version `
        --sub-version $target.SubVersion `
        --final-jsonl $target.FinalJsonl `
        --write-intermediate 2>&1

    $exitCode = $LASTEXITCODE
    $output | Add-Content -LiteralPath $LogPath -Encoding UTF8
    if ($exitCode -eq 0) {
        $done += 1
        "[$(Get-Date -Format s)] OK $current" | Add-Content -LiteralPath $LogPath -Encoding UTF8
    }
    else {
        $failed += 1
        "[$(Get-Date -Format s)] FAIL $current exit_code=$exitCode" | Add-Content -LiteralPath $LogPath -Encoding UTF8
    }
}

Write-ProgressJson -Total $total -Done $done -Failed $failed -Current "global dedupe/cap" -Status "postprocessing"
"[$(Get-Date -Format s)] START global dedupe/cap" | Add-Content -LiteralPath $LogPath -Encoding UTF8
$postprocessOutput = & python $Postprocess `
    --final-json-root $FinalRoot `
    --processed-root $OutputRoot `
    --ground_questions_with_version `
    --cap_generic_sections 2>&1
$postprocessExitCode = $LASTEXITCODE
$postprocessOutput | Add-Content -LiteralPath $LogPath -Encoding UTF8
if ($postprocessExitCode -eq 0) {
    "[$(Get-Date -Format s)] OK global dedupe/cap" | Add-Content -LiteralPath $LogPath -Encoding UTF8
}
else {
    $failed += 1
    "[$(Get-Date -Format s)] FAIL global dedupe/cap exit_code=$postprocessExitCode" | Add-Content -LiteralPath $LogPath -Encoding UTF8
}

Write-ProgressJson -Total $total -Done $done -Failed $failed -Current "" -Status "complete"
"[$(Get-Date -Format s)] Complete. Done: $done Failed: $failed Total: $total" | Add-Content -LiteralPath $LogPath -Encoding UTF8
