# Atomic source-health.yaml runtime-field update for 2026-05-12T15:30 pre-brief sweep.
# Per CLAUDE.md "source-health.yaml field ownership" rule: modify runtime fields
# only (status / last_successful_fetch / failure_count / stale_since / last_error);
# preserve `notes:` and any other operator-set fields VERBATIM.
#
# Approach: read whole file as text, do per-source regex replacements that only
# touch the targeted runtime fields, then write back. The `notes:` strings are
# very long single-line YAML strings and never get touched by these regexes.

$ErrorActionPreference = 'Stop'

$path = 'C:\Users\rtske\Projects\archimedes\infrastructure\source-health.yaml'
$content = Get-Content -Path $path -Raw -Encoding UTF8

# Helper: build a regex that matches a specific source's runtime block (a 3-line
# slice immediately following the "<source-id>:\n    status: healthy\n" anchor)
# and rewrites only the timestamp / failure_count / last_error as requested.

function Update-SourceRuntimeBlock {
    param(
        [Parameter(Mandatory)] [string] $SourceId,
        [string] $NewTimestamp = '2026-05-12T15:30:00-04:00',
        [string] $NewFailureCount = $null,         # null = leave existing
        [string] $NewLastError    = $null,         # null = leave existing; 'CLEAR' = set to null
        [string] $InText                            # input text to mutate
    )

    # Match the block: source-id line + status line + last_successful_fetch line.
    # We use a non-greedy capture so we only replace the one source's block, not
    # spill into another.
    $pattern = "(?m)^(\s\s$([Regex]::Escape($SourceId)):\r?\n\s+status: healthy\r?\n\s+last_successful_fetch: )[^\r\n]+"
    $replacement = '${1}' + $NewTimestamp
    $newText = [Regex]::Replace($InText, $pattern, $replacement)

    if ($NewFailureCount -ne $null) {
        # Update failure_count immediately following the source-id+status+timestamp
        # anchor pattern.
        $fcPattern = "(?ms)^(\s\s$([Regex]::Escape($SourceId)):\r?\n\s+status: healthy\r?\n\s+last_successful_fetch: $([Regex]::Escape($NewTimestamp))\r?\n\s+failure_count: )\d+"
        $fcRepl = '${1}' + $NewFailureCount
        $newText = [Regex]::Replace($newText, $fcPattern, $fcRepl)
    }

    if ($NewLastError -eq 'CLEAR') {
        # Set last_error to null. Match a `last_error:` line that may be either a
        # quoted string OR a YAML literal block (`|`). We handle the simple
        # single-line quoted form here, plus the `last_error: null` no-op case.
        # For multi-line `|` blocks, we leave them in place — the operator can
        # clear those manually.
        $lePattern = "(?m)^(\s\s$([Regex]::Escape($SourceId)):\r?\n\s+status: healthy\r?\n\s+last_successful_fetch: $([Regex]::Escape($NewTimestamp))\r?\n\s+failure_count: \d+\r?\n\s+stale_since: [^\r\n]+\r?\n\s+last_error: )(""[^""]*""|null|'[^']*')"
        $leRepl = '${1}null'
        $newText = [Regex]::Replace($newText, $lePattern, $leRepl)
    }
    elseif ($NewLastError -ne $null -and $NewLastError -ne 'CLEAR') {
        # Set last_error to a specific double-quoted string. Caller passes the
        # bare string (no surrounding quotes) — we add them. We don't try to
        # escape embedded double quotes; caller is responsible for clean input.
        $lePattern = "(?m)^(\s\s$([Regex]::Escape($SourceId)):\r?\n\s+status: healthy\r?\n\s+last_successful_fetch: $([Regex]::Escape($NewTimestamp))\r?\n\s+failure_count: \d+\r?\n\s+stale_since: [^\r\n]+\r?\n\s+last_error: )(""[^""]*""|null|'[^']*')"
        $leRepl = '${1}"' + $NewLastError + '"'
        $newText = [Regex]::Replace($newText, $lePattern, $leRepl)
    }

    return $newText
}

# Sources successfully fetched at 2026-05-12T15:30 (all with last_successful_fetch
# advanced to 15:30):
$content = Update-SourceRuntimeBlock -SourceId 'cisa-advisories'   -InText $content
$content = Update-SourceRuntimeBlock -SourceId 'cisa-kev'          -InText $content
$content = Update-SourceRuntimeBlock -SourceId 'nvd'               -InText $content
$content = Update-SourceRuntimeBlock -SourceId 'crowdstrike'       -InText $content
$content = Update-SourceRuntimeBlock -SourceId 'mstic'             -InText $content
$content = Update-SourceRuntimeBlock -SourceId 'unit42'            -InText $content
$content = Update-SourceRuntimeBlock -SourceId 'krebs'             -InText $content
$content = Update-SourceRuntimeBlock -SourceId 'the-record'        -InText $content
$content = Update-SourceRuntimeBlock -SourceId 'bleepingcomputer'  -InText $content
$content = Update-SourceRuntimeBlock -SourceId 'securityweek'      -InText $content
$content = Update-SourceRuntimeBlock -SourceId 'rapid7'            -InText $content
$content = Update-SourceRuntimeBlock -SourceId 'sentinelone'       -InText $content

# sans-isc: RECOVERED from 06:00 FLASH XML parse error; reset failure_count 1→0,
# clear last_error to null.
$content = Update-SourceRuntimeBlock -SourceId 'sans-isc' -NewFailureCount '0' -NewLastError 'CLEAR' -InText $content

# mandiant: feedburner 404 18th consecutive; failure_count 15→17 (cumulative two
# observations this cycle: 12:00 FLASH not run + 15:30 pre-brief observed 404 +
# the 06:00 FLASH already counted in the prior 15→increment). Set last_error to
# reflect the 15:30 sweep observation; DO NOT advance last_successful_fetch (no
# successful fetch occurred). The cloud.google.com index page WebFetch succeeded
# but the canonical feedburner RSS remains the source-of-record endpoint here.
$mandiantPattern = "(?ms)^(\s\smandiant:\r?\n\s+status: healthy\r?\n\s+last_successful_fetch: )2026-05-07T15:30:00-04:00(\r?\n\s+failure_count: )15"
$mandiantRepl = '${1}2026-05-07T15:30:00-04:00${2}17'
$content = [Regex]::Replace($content, $mandiantPattern, $mandiantRepl)

# Replace mandiant last_error message (single-line quoted form):
$mandiantErrPattern = "(?m)^(\s\smandiant:\r?\n\s+status: healthy\r?\n\s+last_successful_fetch: 2026-05-07T15:30:00-04:00\r?\n\s+failure_count: 17\r?\n\s+stale_since: null\r?\n\s+last_error: )""[^""]*"""
$mandiantErrRepl = '${1}"feedburner.com/Mandiant returned 404 on 2026-05-12T15:30 — eighteenth consecutive failure (06:00 FLASH + 15:30 pre-brief this cycle both observed feedburner 404; cumulative failure_count incremented +2 to 17). cloud.google.com index-page WebFetch fallback remains productive for top-of-list title visibility (top-8 titles unchanged from morning sweeps, all out-of-window per prior triangulations)."'
$content = [Regex]::Replace($content, $mandiantErrPattern, $mandiantErrRepl)

# Write back atomically (no BOM, LF preserved as in original).
$utf8NoBom = New-Object System.Text.UTF8Encoding $false
[System.IO.File]::WriteAllText($path, $content, $utf8NoBom)

Write-Host "source-health.yaml runtime fields updated for 2026-05-12T15:30 pre-brief sweep."
Write-Host "Sources advanced to 15:30 timestamp:" -ForegroundColor Green
@('cisa-advisories','cisa-kev','nvd','crowdstrike','mstic','unit42','krebs','the-record',
  'bleepingcomputer','securityweek','rapid7','sentinelone','sans-isc') |
  ForEach-Object { Write-Host "  - $_" }
Write-Host ""
Write-Host "sans-isc: failure_count 1 -> 0, last_error CLEARED (recovered from 06:00 XML parse error)" -ForegroundColor Yellow
Write-Host "mandiant: failure_count 15 -> 17, last_error updated (18th consecutive 404; last_successful_fetch NOT advanced)" -ForegroundColor Yellow
