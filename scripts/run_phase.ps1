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
    'pre-brief-morning'    = 'Pre-brief COLLECTION ONLY for 08:00 morning brief. Invoke the collector subagent only — do NOT invoke grader, analyst, red-team-analyst, briefer, or librarian. Output: raw-signal files written to threats/raw-signal/ per the collector subagent definition. Do NOT grade, do NOT promote findings, do NOT compose any brief, do NOT post to Discord, do NOT commit, do NOT update _coverage-log.yaml. The 08:00 morning-brief phase consumes your raw-signal output and runs the rest of the pipeline. Return after raw-signal files are written.' + $TestExclusion
    'morning-brief'        = 'Run the 08:00 morning brief pipeline per CLAUDE.md. Grade, analyze, brief, deliver.' + $TestExclusion
    'alert-sweep-noon'     = 'Run a FLASH alert sweep per doctrine/FLASH-POLICY.md. Exit silently if no triggers.' + $TestExclusion
    'pre-brief-afternoon'  = 'Pre-brief COLLECTION ONLY for 16:00 afternoon brief. Invoke the collector subagent only — do NOT invoke grader, analyst, red-team-analyst, briefer, or librarian. Output: raw-signal files written to threats/raw-signal/ per the collector subagent definition. Do NOT grade, do NOT promote findings, do NOT compose any brief, do NOT post to Discord, do NOT commit, do NOT update _coverage-log.yaml. The 16:00 afternoon-brief phase consumes your raw-signal output and runs the rest of the pipeline. Return after raw-signal files are written.' + $TestExclusion
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

# Helper: post an operator alert to a Discord channel via discord_post.py.
# Returns $true on success, $false on any failure. Always non-fatal — a
# down Discord must never abort the wrapper or clobber the phase exit code.
# Uses --message-file (not stdin) per the PS 5.1 stdin-piping quirk, and
# does NOT use 2>&1 on the native exe (NativeCommandError under Stop).
function Send-DiscordAlert {
    param(
        [string]$Message,
        [string]$Channel = 'commands'
    )
    $tmp = New-TemporaryFile
    $utf8NoBom = New-Object System.Text.UTF8Encoding $false
    [System.IO.File]::WriteAllText($tmp.FullName, $Message, $utf8NoBom)
    Push-Location $RepoRoot
    try {
        & uv run python scripts/discord_post.py --channel $Channel --message-file $tmp.FullName --quiet
        return ($LASTEXITCODE -eq 0)
    } catch {
        return $false
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

# --- Brief-phase completion check + degraded-recovery commit ---
# A brief phase that dies mid-pipeline (e.g. org usage limit hit before the
# librarian commits) leaves the brief + findings + raw-signal UNTRACKED on
# disk. The catchup `git push` below is a no-op on untracked files, so the
# corpus is silently stranded — exactly the 2026-05-21 morning incident.
#
# For the two brief phases we use an OUTPUT-based success criterion, not the
# exit code alone: success means "the expected brief file exists AND is
# committed clean". If the brief is uncommitted, we auto-commit the day's
# corpus with a [DEGRADED-RECOVERY] marker (NEVER posted to Discord — a human
# reviews before any ship). If gitleaks or another pre-commit hook blocks the
# recovery commit, it stays orphaned but the operator alert below still fires.
#
# Telemetry: brief_committed / recovery_commit_exit / alert_sent feed the
# completed event so dashboards can see incomplete brief phases.
$RecoveryCommit = $null   # $null = not attempted; 0 = ok; non-zero = commit blocked/failed
$AlertNeeded = $false
$AlertReason = $null
$BriefType = $null
if ($Phase -eq 'morning-brief')   { $BriefType = 'morning' }
if ($Phase -eq 'afternoon-brief') { $BriefType = 'afternoon' }

if ($BriefType) {
    $BriefRel = "threats/briefs/$DateStr-$BriefType.md"
    $BriefAbs = Join-Path $RepoRoot $BriefRel
    Push-Location $RepoRoot
    try {
        # Non-empty porcelain output => the brief file has uncommitted changes
        # (untracked '??' or modified ' M'). Empty => committed clean or absent.
        $briefStatus = & git status --porcelain -- $BriefRel
        $briefUncommitted = [bool]$briefStatus
        $briefExists = Test-Path $BriefAbs

        if ($briefUncommitted) {
            # Orphaned brief on disk — stage today's corpus and commit with marker.
            $recoveryPaths = @($BriefRel)
            Get-ChildItem -Path (Join-Path $RepoRoot 'threats/findings') -Filter "finding-$DateStr-*.md" -ErrorAction SilentlyContinue |
                ForEach-Object { $recoveryPaths += "threats/findings/$($_.Name)" }
            Get-ChildItem -Path (Join-Path $RepoRoot 'threats/raw-signal') -Filter "raw-$DateStr-*.md" -ErrorAction SilentlyContinue |
                ForEach-Object { $recoveryPaths += "threats/raw-signal/$($_.Name)" }
            foreach ($idx in @('threats/briefs/_coverage-log.yaml', 'threats/briefs/_rejection-log.yaml')) {
                if (& git status --porcelain -- $idx) { $recoveryPaths += $idx }
            }

            & git add -- $recoveryPaths
            $commitMsg = "[DEGRADED-RECOVERY] brief: $DateStr $BriefType - pipeline did not commit`n`n" +
                "The $BriefType brief phase ended with claude -p exit=$ClaudeExit but left the brief " +
                "and its corpus uncommitted on disk (librarian phase did not complete - usage limit, " +
                "transport error, or interrupted run). run_phase.ps1 auto-committed the day's corpus " +
                "for audit completeness.`n`nNOT posted to Discord. Review before any manual ship; the " +
                "brief frontmatter may say status: published optimistically.`n`nRun id: $RunId`n`n" +
                "Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
            & git commit -m $commitMsg | ForEach-Object { $_ }
            $RecoveryCommit = $LASTEXITCODE
            $AlertNeeded = $true
            $AlertReason = if ($RecoveryCommit -eq 0) {
                "Orphaned corpus auto-committed (DEGRADED-RECOVERY) - review before manual ship."
            } else {
                "Auto-recovery commit FAILED (exit=$RecoveryCommit, likely a blocked pre-commit hook) - corpus is still ORPHANED on disk, manual recovery needed."
            }
        } elseif (-not $briefExists -and $ClaudeExit -ne 0) {
            $AlertNeeded = $true
            $AlertReason = "Pipeline died before the briefer wrote a brief - no corpus to recover."
        } elseif ($ClaudeExit -ne 0) {
            # Brief committed clean but claude still reported a non-zero exit.
            $AlertNeeded = $true
            $AlertReason = "Brief is committed but the phase reported exit=$ClaudeExit - inspect the log for a post-commit failure."
        }
    } finally {
        Pop-Location
    }
}

# --- Catchup push: ensure any commits the librarian made are on origin/main ---
# The librarian's `git push` step (Mode 1 procedure step 8) is empirically
# non-deterministic — Wed 2026-05-06 auto-pushed all 6 phases cleanly, Tue
# afternoon and Thu morning held 1-2 commits without explanation despite
# identical doctrine. This wrapper-level push is belt-and-suspenders:
#   - If the librarian already pushed, `git push` is a no-op ("Everything
#     up-to-date") and exit 0
#   - If the librarian held, this catches up before the next phase fires
#   - Push failure (network, auth) is non-fatal — claude phase itself
#     succeeded, commits stay local until next phase or operator catches up
# Telemetry: catchup_push_exit field added to the completed event so dash-
# board panels can surface push reliability without guessing.
$PushExit = 0
Push-Location $RepoRoot
try {
    # Do NOT use 2>&1 here. git push prints "Everything up-to-date" to stderr,
    # PS 5.1 wraps that as NativeCommandError under $ErrorActionPreference=Stop,
    # and we'd misreport a clean no-op as exit=-1. Let stderr flow to parent;
    # Task Scheduler captures both streams. We only care about the exit code.
    & git push origin main | ForEach-Object {
        # stdout lines (rare for git push) get appended to our log
        $_
    }
    $PushExit = $LASTEXITCODE
} catch {
    # Reachable only on PS-level exceptions (cmd not found, etc.) — not git
    # exit codes. -2 is distinct from -1 (the prior bug's signature) so any
    # leftover -1 in old Splunk events is unambiguously the old bug.
    $PushExit = -2
} finally {
    Pop-Location
}

# Append push result to log file (visible in interactive runs and Task Scheduler captures)
$utf8NoBomPushLog = New-Object System.Text.UTF8Encoding $false
[System.IO.File]::AppendAllText($LogFile, "`r`n[run_phase.ps1] catchup push exit=$PushExit`r`n", $utf8NoBomPushLog)

# --- Operator alert: page the commands channel on an incomplete brief phase ---
# Only brief phases set $AlertNeeded (above). Non-fatal: a Discord failure
# here must not change the phase exit code. The recovery commit (if any) has
# already been pushed by the catchup step, so the alert can point at git.
$AlertSent = $null   # $null = not attempted
if ($AlertNeeded) {
    $alertMsg = ":red_circle: **Archimedes pipeline FAILURE** - $BriefType brief ($DateStr)`n" +
        "Phase '$Phase' ended with exit=$ClaudeExit. **The brief was NOT posted to #intel-briefs.**`n" +
        "$AlertReason`n" +
        "Run id: $RunId`n" +
        "Log: $LogFile"
    $AlertSent = Send-DiscordAlert -Message $alertMsg -Channel 'commands'
    [System.IO.File]::AppendAllText($LogFile, "[run_phase.ps1] failure alert sent=$AlertSent reason=$AlertReason`r`n", $utf8NoBomPushLog)
}

# --- Post-flight: log "completed" event ---
$endEvent = @{
    run_id              = $RunId
    phase               = $Phase
    status              = if ($ClaudeExit -eq 0) { 'completed' } else { 'failed' }
    exit_code           = $ClaudeExit
    duration_sec        = $DurationSec
    log_file            = $LogFile
    catchup_push_exit   = $PushExit
    recovery_commit_exit = $RecoveryCommit
    alert_sent          = $AlertSent
    alert_reason        = $AlertReason
}
[void](Send-SplunkEvent -EventData $endEvent)

exit $ClaudeExit
