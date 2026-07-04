param(
    [switch]$Force,
    [int]$MaxParallel = 6,
    [string]$SourceDataRoot,
    [string]$OutputRoot,
    [switch]$UseDocumentIntelligence,
    [string]$ResumeLog
)

$ErrorActionPreference = "Stop"

$SourceRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
if ([string]::IsNullOrWhiteSpace($SourceDataRoot)) {
    $SourceDataRoot = Join-Path $SourceRoot "Raw_Data_Product"
}
if ([string]::IsNullOrWhiteSpace($OutputRoot)) {
    $OutputRoot = Join-Path $SourceRoot "markitdown_cli_output"
}

$SourceDataRoot = [System.IO.Path]::GetFullPath($SourceDataRoot)
$OutputRoot = [System.IO.Path]::GetFullPath($OutputRoot)
$MarkItDown = Join-Path $SourceRoot ".markitdown_venv312\Scripts\markitdown.exe"
$RepoSrc = Join-Path $SourceRoot "tools\markitdown-main\packages\markitdown\src"
$LogRoot = Join-Path $OutputRoot "_logs"
$RunStarted = Get-Date
$RunId = $RunStarted.ToString("yyyyMMdd_HHmmss")
$CsvLogPath = Join-Path $LogRoot "conversion_$RunId.csv"
$LatestCsvLogPath = Join-Path $LogRoot "conversion_latest.csv"
$StatusPath = Join-Path $LogRoot "conversion_status.txt"
$StdoutLogPath = Join-Path $LogRoot "conversion_$RunId.stdout.log"

$DocIntelEndpoint = $env:AZURE_DOCUMENT_INTELLIGENCE_ENDPOINT
if ([string]::IsNullOrWhiteSpace($DocIntelEndpoint)) {
    $DocIntelEndpoint = $env:AZURE_DOC_INTEL_ENDPOINT
}
if ([string]::IsNullOrWhiteSpace($DocIntelEndpoint)) {
    $DocIntelEndpoint = $env:MARKITDOWN_DOC_INTEL_ENDPOINT
}
$UseDocIntel = $UseDocumentIntelligence -and -not [string]::IsNullOrWhiteSpace($DocIntelEndpoint)
$AzureApiKey = $env:AZURE_API_KEY

if ($MaxParallel -lt 1) {
    throw "MaxParallel must be at least 1."
}
if (-not (Test-Path -LiteralPath $SourceDataRoot)) {
    throw "Source data root not found: $SourceDataRoot"
}
if (-not (Test-Path -LiteralPath $MarkItDown)) {
    throw "MarkItDown CLI not found at $MarkItDown"
}
if (-not (Test-Path -LiteralPath $RepoSrc)) {
    throw "MarkItDown repo source not found at $RepoSrc"
}
if ($UseDocumentIntelligence -and -not $UseDocIntel) {
    throw "UseDocumentIntelligence was requested, but no Document Intelligence endpoint was found in the environment."
}

if ([string]::IsNullOrWhiteSpace($env:PYTHONPATH)) {
    $env:PYTHONPATH = $RepoSrc
}
else {
    $env:PYTHONPATH = "$RepoSrc;$($env:PYTHONPATH)"
}

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

function ConvertTo-CsvField {
    param(
        [AllowNull()][object]$Value
    )

    if ($null -eq $Value) {
        $Text = ""
    }
    else {
        $Text = [string]$Value
    }
    $Text = $Text.Replace("`r", " ").Replace("`n", " ")
    return '"' + $Text.Replace('"', '""') + '"'
}

function Add-ContentWithRetry {
    param(
        [string]$Path,
        [string]$Value
    )

    for ($Attempt = 1; $Attempt -le 10; $Attempt += 1) {
        try {
            Add-Content -LiteralPath $Path -Value $Value -Encoding UTF8
            return
        }
        catch {
            Start-Sleep -Milliseconds (200 * $Attempt)
        }
    }

    Write-Warning "Could not write log line to $Path because the file is locked."
}

function Set-ContentWithRetry {
    param(
        [string]$Path,
        [string[]]$Value
    )

    for ($Attempt = 1; $Attempt -le 10; $Attempt += 1) {
        try {
            Set-Content -LiteralPath $Path -Value $Value -Encoding UTF8
            return
        }
        catch {
            Start-Sleep -Milliseconds (200 * $Attempt)
        }
    }

    Write-Warning "Could not update $Path because the file is locked."
}

function Add-CsvLog {
    param(
        [object]$Record
    )

    $Fields = @(
        $Record.Timestamp,
        $Record.Status,
        $Record.InputPath,
        $Record.OutputPath,
        $Record.DurationSeconds,
        $Record.ExitCode,
        $Record.ErrorMessage
    ) | ForEach-Object { ConvertTo-CsvField $_ }

    $Line = $Fields -join ","
    Add-ContentWithRetry -Path $CsvLogPath -Value $Line
    Add-ContentWithRetry -Path $LatestCsvLogPath -Value $Line
}

function Write-ConversionStatus {
    $RunningJobs = (Get-Job -State Running).Count
    $Done = $script:Converted + $script:Skipped + $script:Failed
    if ($script:TotalFiles -gt 0) {
        $Percent = [Math]::Round(($Done / $script:TotalFiles) * 100, 2)
    }
    else {
        $Percent = 100
    }

    $Elapsed = New-TimeSpan -Start $RunStarted -End (Get-Date)
    $StatusLines = @(
        "run_id=$RunId",
        "started=$($RunStarted.ToString('s'))",
        "updated=$((Get-Date).ToString('s'))",
        "source_root=$SourceDataRoot",
        "output_root=$OutputRoot",
        "repo_source=$RepoSrc",
        "mode=$(if ($UseDocIntel) { 'azure_document_intelligence' } else { 'local_repo' })",
        "force=$Force",
        "max_parallel=$MaxParallel",
        "total_pdfs=$script:TotalFiles",
        "queued=$script:Queued",
        "converted=$script:Converted",
        "skipped=$script:Skipped",
        "failed=$script:Failed",
        "done=$Done",
        "percent=$Percent",
        "running_jobs=$RunningJobs",
        "elapsed=$($Elapsed.ToString())",
        "csv_log=$CsvLogPath",
        "latest_csv_log=$LatestCsvLogPath",
        "resume_log=$ResumeLog",
        "resume_converted_count=$script:ResumeConvertedCount",
        "stdout_log=$StdoutLogPath"
    )

    Set-ContentWithRetry -Path $StatusPath -Value $StatusLines
}

function Receive-FinishedJobs {
    $FinishedJobs = @(Get-Job | Where-Object { $_.State -in @("Completed", "Failed", "Stopped") })

    foreach ($Job in $FinishedJobs) {
        if ($Job.State -eq "Completed") {
            $Results = @(Receive-Job -Job $Job)
            if ($Results.Count -eq 0) {
                $script:Failed += 1
                Add-CsvLog ([PSCustomObject]@{
                    Timestamp = (Get-Date).ToString("s")
                    Status = "failed"
                    InputPath = ""
                    OutputPath = ""
                    DurationSeconds = ""
                    ExitCode = ""
                    ErrorMessage = "Job completed without returning a result."
                })
            }

            foreach ($Result in $Results) {
                if ($Result.Success) {
                    $script:Converted += 1
                    $Status = "converted"
                }
                else {
                    $script:Failed += 1
                    $Status = "failed"
                }

                Add-CsvLog ([PSCustomObject]@{
                    Timestamp = (Get-Date).ToString("s")
                    Status = $Status
                    InputPath = $Result.InputPath
                    OutputPath = $Result.OutputPath
                    DurationSeconds = $Result.DurationSeconds
                    ExitCode = $Result.ExitCode
                    ErrorMessage = $Result.ErrorMessage
                })
            }
        }
        else {
            $script:Failed += 1
            Add-CsvLog ([PSCustomObject]@{
                Timestamp = (Get-Date).ToString("s")
                Status = "failed"
                InputPath = ""
                OutputPath = ""
                DurationSeconds = ""
                ExitCode = ""
                ErrorMessage = "PowerShell job ended with state $($Job.State): $($Job.ChildJobs[0].JobStateInfo.Reason.Message)"
            })
        }

        Remove-Job -Job $Job -Force
    }

    if ($FinishedJobs.Count -gt 0) {
        Write-ConversionStatus
    }
}

New-Item -ItemType Directory -Force -Path $OutputRoot | Out-Null
New-Item -ItemType Directory -Force -Path $LogRoot | Out-Null

$ResumeConverted = New-Object 'System.Collections.Generic.HashSet[string]' ([System.StringComparer]::OrdinalIgnoreCase)
if (-not [string]::IsNullOrWhiteSpace($ResumeLog)) {
    if (-not (Test-Path -LiteralPath $ResumeLog)) {
        throw "Resume log not found: $ResumeLog"
    }

    Import-Csv -LiteralPath $ResumeLog |
        Where-Object { $_.status -eq "converted" -and -not [string]::IsNullOrWhiteSpace($_.input_path) } |
        ForEach-Object { $null = $ResumeConverted.Add($_.input_path) }
}
$script:ResumeConvertedCount = $ResumeConverted.Count

$CsvHeader = "timestamp,status,input_path,output_path,duration_seconds,exit_code,error_message"
Set-ContentWithRetry -Path $CsvLogPath -Value @($CsvHeader)
Set-ContentWithRetry -Path $LatestCsvLogPath -Value @($CsvHeader)

$Files = Get-ChildItem -LiteralPath $SourceDataRoot -File -Recurse -Filter *.pdf |
    Sort-Object FullName

$script:TotalFiles = $Files.Count
$script:Queued = 0
$script:Converted = 0
$script:Skipped = 0
$script:Failed = 0

Write-ConversionStatus

Write-Host "Source root: $SourceDataRoot"
Write-Host "Output root: $OutputRoot"
Write-Host "Mode: $(if ($UseDocIntel) { 'Azure Document Intelligence' } else { 'local repo MarkItDown' })"
Write-Host "Force regenerate: $Force"
Write-Host "Total PDFs: $script:TotalFiles"
Write-Host "Status file: $StatusPath"
Write-Host "CSV log: $CsvLogPath"

foreach ($File in $Files) {
    $RelativeFile = Get-RelativePath -BasePath $SourceRoot -TargetPath $File.FullName
    $RelativeParent = Split-Path -Parent $RelativeFile
    $TargetName = [System.IO.Path]::GetFileNameWithoutExtension($RelativeFile) + ".md"
    $TargetDir = Join-Path $OutputRoot $RelativeParent
    $TargetFile = Join-Path $TargetDir $TargetName

    if ($ResumeConverted.Contains($File.FullName) -and (Test-Path -LiteralPath $TargetFile)) {
        $script:Skipped += 1
        Add-CsvLog ([PSCustomObject]@{
            Timestamp = (Get-Date).ToString("s")
            Status = "resume_skipped"
            InputPath = $File.FullName
            OutputPath = $TargetFile
            DurationSeconds = 0
            ExitCode = 0
            ErrorMessage = "Already converted in resume log."
        })
        if (($script:Skipped % 50) -eq 0) {
            Write-ConversionStatus
        }
        continue
    }

    if ((Test-Path -LiteralPath $TargetFile) -and -not $Force) {
        $script:Skipped += 1
        Add-CsvLog ([PSCustomObject]@{
            Timestamp = (Get-Date).ToString("s")
            Status = "skipped"
            InputPath = $File.FullName
            OutputPath = $TargetFile
            DurationSeconds = 0
            ExitCode = 0
            ErrorMessage = "Output already exists."
        })
        if (($script:Skipped % 50) -eq 0) {
            Write-ConversionStatus
        }
        continue
    }

    New-Item -ItemType Directory -Force -Path $TargetDir | Out-Null

    while ((Get-Job -State Running).Count -ge $MaxParallel) {
        Receive-FinishedJobs
        if ((Get-Job -State Running).Count -ge $MaxParallel) {
            $RunningJobs = @(Get-Job -State Running)
            if ($RunningJobs.Count -gt 0) {
                Wait-Job -Job $RunningJobs -Any | Out-Null
            }
        }
    }

    $script:Queued += 1
    $JobsArgs = @(
        $MarkItDown,
        $File.FullName,
        $TargetFile,
        $UseDocIntel,
        $DocIntelEndpoint,
        $AzureApiKey,
        $RepoSrc
    )

    Start-Job -ScriptBlock {
        param($CliPath, $InputPath, $OutputPath, $UseDocIntel, $DocIntelEndpoint, $AzureApiKey, $RepoSrc)

        $ErrorActionPreference = "Stop"
        $Started = Get-Date

        try {
            if (-not [string]::IsNullOrWhiteSpace($RepoSrc)) {
                if ([string]::IsNullOrWhiteSpace($env:PYTHONPATH)) {
                    $env:PYTHONPATH = $RepoSrc
                }
                else {
                    $env:PYTHONPATH = "$RepoSrc;$($env:PYTHONPATH)"
                }
            }

            if (-not [string]::IsNullOrWhiteSpace($AzureApiKey)) {
                $env:AZURE_API_KEY = $AzureApiKey
            }

            $CliArgs = @($InputPath, "-o", $OutputPath)
            if ($UseDocIntel) {
                $CliArgs += @("-d", "-e", $DocIntelEndpoint)
            }

            $CliOutput = & $CliPath @CliArgs 2>&1
            if ($null -eq $LASTEXITCODE) {
                $ExitCode = 0
            }
            else {
                $ExitCode = $LASTEXITCODE
            }

            $Duration = [Math]::Round(((Get-Date) - $Started).TotalSeconds, 3)
            $Message = ($CliOutput | ForEach-Object { $_.ToString() }) -join " "

            [PSCustomObject]@{
                InputPath = $InputPath
                OutputPath = $OutputPath
                Success = ($ExitCode -eq 0)
                DurationSeconds = $Duration
                ExitCode = $ExitCode
                ErrorMessage = $Message
            }
        }
        catch {
            $Duration = [Math]::Round(((Get-Date) - $Started).TotalSeconds, 3)
            [PSCustomObject]@{
                InputPath = $InputPath
                OutputPath = $OutputPath
                Success = $false
                DurationSeconds = $Duration
                ExitCode = ""
                ErrorMessage = $_.Exception.Message
            }
        }
    } -ArgumentList $JobsArgs | Out-Null

    if (($script:Queued % 25) -eq 0) {
        Write-Host "Queued $script:Queued / $script:TotalFiles. Converted $script:Converted, skipped $script:Skipped, failed $script:Failed."
        Write-ConversionStatus
    }
}

while ((Get-Job).Count -gt 0) {
    Receive-FinishedJobs
    if ((Get-Job).Count -gt 0) {
        $RemainingJobs = @(Get-Job)
        if ($RemainingJobs.Count -gt 0) {
            Wait-Job -Job $RemainingJobs -Any | Out-Null
        }
    }
}

Write-ConversionStatus

Write-Host "Done."
Write-Host "Source files found: $script:TotalFiles"
Write-Host "Files converted: $script:Converted"
Write-Host "Files skipped: $script:Skipped"
Write-Host "Failures: $script:Failed"
Write-Host "Status file: $StatusPath"
Write-Host "CSV log: $CsvLogPath"

if ($script:Failed -gt 0) {
    exit 1
}
