# scripts/run_phase.ps1 — Headless Claude Code invocation wrapper for the
# Archimedes scheduled brief / FLASH alert pipeline.
#
# Called by Windows Task Scheduler at the 8 daily firing times defined in
# CLAUDE.md "Daily Rhythm". Each scheduled task passes a different -Phase.
# This script picks the right prompt, invokes `claude -p` headlessly with
# permission bypass (required for unattended runs), tees stdout to a log
# file under logs/scheduler/, and emits a structured event to Splunk
# bracketing the run so failures are queryable.
#
# Production phases (all 8 firings from CLAUDE.md):
#   pre-brief-morning       07:30 EDT  — collector pre-brief sweep
#   morning-brief           08:00 EDT  — full brief pipeline
#   alert-sweep-noon        12:00 EDT  — FLASH sweep
#   pre-brief-afternoon     15:30 EDT  — collector pre-brief sweep
#   afternoon-brief         16:00 EDT  — full brief pipeline
#   alert-sweep-evening     18:00 EDT  — FLASH sweep
#   alert-sweep-midnight    00:00 EDT  — FLASH sweep (queues if outside 9am-9pm)
#   alert-sweep-dawn        06:00 EDT  — FLASH sweep (queues)
#
# Test phase (Session 7 development only — not scheduled in production):
#   smoke-test  — minimal `claude -p "Reply OK"` to verify wrapper plumbing.
#
# Usage:
#   .\scripts\run_phase.ps1 -Phase smoke-test
#   .\scripts\run_phase.ps1 -Phase morning-brief
#
# Exit codes:
#   0  Success (claude -p returned 0)
#   2  Configuration error (bad phase, missing claude CLI)
#   3  Splunk pre-log failed (run aborted to preserve invariant: every run logged)
#   non-zero  Whatever claude -p returned

[CmdletBinding()]
param(
    [Parameter(Mandatory=$true)]
    [ValidateSet(
        'pre-brief-morning',
        'morning-brief',
        'alert-sweep-noon',
        'pre-brief-afternoon',
        'afternoon-brief',
        'alert-sweep-evening',
        'alert-sweep-midnight',
        'alert-sweep-dawn',
        'smoke-test'
    )]
    [string]$Phase,

    # If set, wrapper skips claude -p and only validates plumbing
    # (path resolution, log dir creation, Splunk roundtrip). Useful for
    # CI or "did the scheduler fire at all" checks without API spend.
    [switch]$DryRun
)

$ErrorActionPreference = 'Stop'

# Phase -> prompt mapping. Short prompts; trust the orchestrator to
# consult CLAUDE.md and follow doctrine. See docs/handoffs/session-7-prep.md
# for the rationale on prompt brevity.
# All production prompts include the test-fixture exclusion clause so
# unattended runs operate only on real signal. Test fixtures are
# left in place (they have ttl_expires_at and test: true frontmatter)
# but never propagate to briefs or Discord. Discovered Session 8
# Stage G: orchestrator otherwise stops to ask which signal to use.
$TestExclusion = ' Skip any raw-signal, findings, or briefs marked test: true.'

$PhasePrompts = @{
    'pre-brief-morning'    = 'Run pre-brief collection for the 08:00 morning brief per CLAUDE.md Pipeline - Scheduled Brief.' + $TestExclusion
    'morning-brief'        = 'Run the 08:00 morning brief pipeline per CLAUDE.md. Grade, analyze, brief, deliver.' + $TestExclusion
    'alert-sweep-noon'     = 'Run a FLASH alert sweep per doctrine/FLASH-POLICY.md. Exit silently if no triggers.' + $TestExclusion
    'pre-brief-afternoon'  = 'Run pre-brief collection for the 16:00 afternoon brief per CLAUDE.md Pipeline - Scheduled Brief.' + $TestExclusion
    'afternoon-brief'      = 'Run the 16:00 afternoon brief pipeline per CLAUDE.md. Grade, analyze, brief, deliver.' + $TestExclusion
    'alert-sweep-evening'  = 'Run a FLASH alert sweep per doctrine/FLASH-POLICY.md. Exit silently if no triggers.' + $TestExclusion
    'alert-sweep-midnight' = 'Run a FLASH alert sweep per doctrine/FLASH-POLICY.md. Quiet hours active - queue any triggers.' + $TestExclusion
    'alert-sweep-dawn'     = 'Run a FLASH alert sweep per doctrine/FLASH-POLICY.md. Quiet hours active - queue any triggers.' + $TestExclusion
    'smoke-test'           = 'Reply with the literal string OK and nothing else.'
}

# Resolve repo root from this script's location (scripts/ -> ..)
$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path

# Build log paths
$Now = Get-Date
$DateStr = $Now.ToString('yyyy-MM-dd')
$TimeStr = $Now.ToString('HHmm')
$RunId = "$Phase-$($Now.ToString('yyyyMMdd-HHmmss'))"
$LogDir = Join-Path $RepoRoot "logs/scheduler/$DateStr"
$LogFile = Join-Path $LogDir "$Phase-$TimeStr.log"
New-Item -ItemType Directory -Force -Path $LogDir | Out-Null

# Helper: emit an event to Splunk via the splunk-log hook.
# Returns $true on success, $false on failure. We check the return so
# the wrapper can preserve the invariant "every scheduled run is
# recorded in Splunk" — if pre-logging fails, the run aborts.
#
# Implementation note (PS 5.1 quirks):
#   - Native-exe stdin piping is unreliable in PS 5.1; use a temp file
#     and pass --event-file instead.
#   - Do NOT redirect native-exe stderr with 2>&1 — it wraps each line
#     in NativeCommandError and trips $ErrorActionPreference=Stop.
function Send-SplunkEvent {
    param([hashtable]$EventData)
    $json = $EventData | ConvertTo-Json -Compress -Depth 5
    $tmp = New-TemporaryFile
    # UTF-8 WITHOUT BOM — Python's json.loads rejects a BOM as invalid.
    # The default UTF8Encoding ([System.Text.Encoding]::UTF8) writes a
    # BOM, so we construct one explicitly.
    $utf8NoBom = New-Object System.Text.UTF8Encoding $false
    [System.IO.File]::WriteAllText($tmp.FullName, $json, $utf8NoBom)
    Push-Location $RepoRoot
    try {
        & uv run python scripts/splunk_log.py --event-file $tmp.FullName --sourcetype 'archimedes:scheduler' --quiet
        return ($LASTEXITCODE -eq 0)
    } finally {
        Pop-Location
        Remove-Item $tmp.FullName -Force -ErrorAction SilentlyContinue
    }
}

# --- Pre-flight: log "started" event ---
$startEvent = @{
    run_id     = $RunId
    phase      = $Phase
    status     = 'started'
    started_at = $Now.ToString('o')
    log_file   = $LogFile
    dry_run    = $DryRun.IsPresent
}
$preLogged = Send-SplunkEvent -EventData $startEvent
if (-not $preLogged) {
    # Use direct stderr write — Write-Error becomes terminating under
    # $ErrorActionPreference=Stop and would clobber our exit code.
    [Console]::Error.WriteLine("[run_phase.ps1] Splunk pre-log failed. Aborting run to preserve audit-trail invariant.")
    exit 3
}

# --- DryRun short-circuit ---
if ($DryRun) {
    Write-Output "[run_phase.ps1] DryRun: phase=$Phase repo=$RepoRoot log=$LogFile"
    $endEvent = @{
        run_id       = $RunId
        phase        = $Phase
        status       = 'completed'
        exit_code    = 0
        duration_sec = 0
        dry_run      = $true
    }
    [void](Send-SplunkEvent -EventData $endEvent)
    exit 0
}

# --- Invoke claude -p ---
$Prompt = $PhasePrompts[$Phase]
$StartTime = Get-Date

Push-Location $RepoRoot
try {
    # Stream claude's stdout: append each line to the log AND pass it
    # through so Task Scheduler / interactive callers see it live.
    # PS 5.1 quirks handled here:
    #   - Tee-Object has no -Encoding param (UTF-16 LE BOM default),
    #     and Add-Content -Encoding UTF8 still writes a BOM. Use
    #     [System.IO.File]::AppendAllText with explicit no-BOM UTF-8.
    #   - We do NOT use 2>&1 — that wraps native-exe stderr in
    #     NativeCommandError under $ErrorActionPreference=Stop.
    # Stderr flows naturally to the parent process and is captured
    # separately by Task Scheduler.
    $utf8NoBomLog = New-Object System.Text.UTF8Encoding $false
    # Pipe $null in so claude doesn't wait 3s for stdin data and emit
    # "no stdin data received" warnings. Equivalent to bash `< /dev/null`.
    $null | & claude -p $Prompt `
        --output-format text `
        --permission-mode bypassPermissions `
        | ForEach-Object {
            [System.IO.File]::AppendAllText($LogFile, "$_`r`n", $utf8NoBomLog)
            Write-Output $_
        }

    $ClaudeExit = $LASTEXITCODE
} finally {
    Pop-Location
}

$EndTime = Get-Date
$DurationSec = [int](($EndTime - $StartTime).TotalSeconds)

# --- Post-flight: log "completed" event ---
$endEvent = @{
    run_id       = $RunId
    phase        = $Phase
    status       = if ($ClaudeExit -eq 0) { 'completed' } else { 'failed' }
    exit_code    = $ClaudeExit
    duration_sec = $DurationSec
    log_file     = $LogFile
}
[void](Send-SplunkEvent -EventData $endEvent)

exit $ClaudeExit
