$ErrorActionPreference = "Stop"

$SourceRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$OutputRoot = Join-Path $SourceRoot "markitdown_cli_output"
$MarkItDown = Join-Path $SourceRoot ".markitdown_venv312\Scripts\markitdown.exe"
$MaxParallel = 6

function Get-RelativePath {
    param(
        [string]$BasePath,
        [string]$TargetPath
    )

    $BaseFullPath = [System.IO.Path]::GetFullPath($BasePath)
    $TargetFullPath = [System.IO.Path]::GetFullPath($TargetPath)
    if (-not $BaseFullPath.EndsWith([System.IO.Path]::DirectorySeparatorChar)) {
        $BaseFullPath += [System.IO.Path]::DirectorySeparatorChar
    }

    $BaseUri = New-Object System.Uri($BaseFullPath)
    $TargetUri = New-Object System.Uri($TargetFullPath)
    $RelativeUri = $BaseUri.MakeRelativeUri($TargetUri)
    return [System.Uri]::UnescapeDataString($RelativeUri.ToString()).Replace("/", "\")
}

if (-not (Test-Path -LiteralPath $MarkItDown)) {
    throw "MarkItDown CLI not found at $MarkItDown"
}

$SourceFolders = Get-ChildItem -LiteralPath $SourceRoot -Directory |
    Where-Object { $_.Name -like "Aruba_*" } |
    Sort-Object FullName

New-Item -ItemType Directory -Force -Path $OutputRoot | Out-Null

$DirectoriesMirrored = 0
foreach ($Folder in $SourceFolders) {
    $Dirs = @($Folder) + @(Get-ChildItem -LiteralPath $Folder.FullName -Directory -Recurse)
    foreach ($Dir in $Dirs) {
        $RelativeDir = Get-RelativePath -BasePath $SourceRoot -TargetPath $Dir.FullName
        New-Item -ItemType Directory -Force -Path (Join-Path $OutputRoot $RelativeDir) | Out-Null
        $DirectoriesMirrored += 1
    }
}

$Files = foreach ($Folder in $SourceFolders) {
    Get-ChildItem -LiteralPath $Folder.FullName -File -Recurse
}

$Jobs = New-Object System.Collections.Generic.List[object]
$Skipped = 0

foreach ($File in $Files) {
    $RelativeFile = Get-RelativePath -BasePath $SourceRoot -TargetPath $File.FullName
    $RelativeParent = Split-Path -Parent $RelativeFile
    $TargetName = [System.IO.Path]::GetFileNameWithoutExtension($RelativeFile) + ".md"
    $TargetDir = Join-Path $OutputRoot $RelativeParent
    $TargetFile = Join-Path $TargetDir $TargetName

    if (Test-Path -LiteralPath $TargetFile) {
        $Skipped += 1
        continue
    }

    New-Item -ItemType Directory -Force -Path $TargetDir | Out-Null

    while ((Get-Job -State Running).Count -ge $MaxParallel) {
        Wait-Job -Any -State Running | Out-Null
    }

    $Jobs.Add((Start-Job -ScriptBlock {
        param($CliPath, $InputPath, $OutputPath)
        & $CliPath $InputPath -o $OutputPath
        if ($LASTEXITCODE -ne 0) {
            throw "markitdown exited with code $LASTEXITCODE"
        }
        [PSCustomObject]@{
            InputPath = $InputPath
            OutputPath = $OutputPath
            Success = $true
        }
    } -ArgumentList $MarkItDown, $File.FullName, $TargetFile)) | Out-Null

    if (($Jobs.Count % 500) -eq 0) {
        Write-Host "Queued $($Jobs.Count) conversions, skipped $Skipped existing..."
    }
}

$Failures = New-Object System.Collections.Generic.List[string]
$Converted = 0

while ((Get-Job -State Running).Count -gt 0) {
    Wait-Job -Any -State Running | Out-Null
    $Completed = Get-Job -State Completed
    foreach ($Job in $Completed) {
        Receive-Job -Job $Job | Out-Null
        Remove-Job -Job $Job
        $Converted += 1
        if (($Converted % 500) -eq 0) {
            Write-Host "Finished $Converted conversions..."
        }
    }
    $Failed = Get-Job -State Failed
    foreach ($Job in $Failed) {
        $Reason = $Job.ChildJobs[0].JobStateInfo.Reason.Message
        $Failures.Add($Reason)
        Remove-Job -Job $Job
    }
}

$Remaining = Get-Job
foreach ($Job in $Remaining) {
    if ($Job.State -eq "Completed") {
        Receive-Job -Job $Job | Out-Null
        $Converted += 1
    }
    elseif ($Job.State -eq "Failed") {
        $Reason = $Job.ChildJobs[0].JobStateInfo.Reason.Message
        $Failures.Add($Reason)
    }
    Remove-Job -Job $Job -Force
}

Write-Host "Source root: $SourceRoot"
Write-Host "Output root: $OutputRoot"
Write-Host "Source folders: $($SourceFolders.Count)"
Write-Host "Directories mirrored: $DirectoriesMirrored"
Write-Host "Source files found: $($Files.Count)"
Write-Host "Files converted: $Converted"
Write-Host "Files skipped: $Skipped"
Write-Host "Failures: $($Failures.Count)"

foreach ($Failure in $Failures | Select-Object -First 100) {
    Write-Host "FAILED: $Failure"
}

if ($Failures.Count -gt 0) {
    exit 1
}
