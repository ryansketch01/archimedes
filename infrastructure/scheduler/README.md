# Archimedes Scheduler — Windows Task Scheduler Configuration

Frank runs the Archimedes scheduled brief and FLASH alert pipelines via
Windows Task Scheduler. This directory holds the task XML template and
the install procedure. **Tasks are NOT installed automatically by
checkout** — installation is a deliberate Session 10 step.

**Production status (as of 2026-05-06):** 6 of 8 phases installed and
firing on schedule. The 2 deferred (`pre-brief-morning`,
`pre-brief-afternoon`) await the Session 11 prompt scope-creep fix
(see "Known issues" below).

## What runs when

Per `CLAUDE.md` "Daily Rhythm", 8 phases fire daily (times in EDT):

| Phase | Time | Trigger | Notes |
|---|---|---|---|
| `alert-sweep-midnight` | 00:00 | FLASH sweep | Quiet hours — triggers queue |
| `alert-sweep-dawn` | 06:00 | FLASH sweep | Quiet hours — triggers queue |
| `pre-brief-morning` | 07:30 | Collector pre-sweep | Feeds 08:00 brief |
| `morning-brief` | 08:00 | Full brief pipeline | Posts to `#intel-briefs` |
| `alert-sweep-noon` | 12:00 | FLASH sweep | Active hours |
| `pre-brief-afternoon` | 15:30 | Collector pre-sweep | Feeds 16:00 brief |
| `afternoon-brief` | 16:00 | Full brief pipeline | Posts to `#intel-briefs` |
| `alert-sweep-evening` | 18:00 | FLASH sweep | Active hours |

Each phase is a separate task. Wrapper: `scripts/run_phase.ps1
-Phase <phase-name>`. The wrapper handles prompt selection, headless
`claude -p` invocation, log capture, and Splunk event bracketing.

## Install procedure

For each phase, generate a substituted XML and import it. The default
template uses `LogonType: InteractiveToken` which means **no password
needed at import time** — but tasks only fire while rtske is logged in.
See "Logon type decision" below for the trade-off.

### Recommended substitution (PowerShell)

This pattern reads the UTF-8 source template and writes UTF-8 output
matching the declaration (which is `encoding="UTF-8"` since 2026-05-06):

```powershell
$template = [System.IO.File]::ReadAllText(
    "C:\Users\rtske\Projects\archimedes\infrastructure\scheduler\archimedes-task-template.xml",
    [System.Text.Encoding]::UTF8)

$phase = "morning-brief"             # one of the 8 phase names
$time  = "2026-05-08T08:00:00"       # ISO timestamp for first run
$repo  = "C:\Users\rtske\Projects\archimedes"

$xml = $template `
    .Replace('__PHASE__', $phase) `
    .Replace('__TIME__', $time) `
    .Replace('__REPO_ROOT__', $repo)

[System.IO.File]::WriteAllText(
    "$env:TEMP\archimedes-$phase.xml",
    $xml,
    [System.Text.Encoding]::UTF8)
```

### Import (default — InteractiveToken, no password)

```powershell
schtasks /Create /XML "$env:TEMP\archimedes-morning-brief.xml" /TN "Archimedes\morning-brief"
```

That's it. No `/RU` or `/RP` — the XML's `<Principals>` block defines
the user and the InteractiveToken logon type.

### Import (Password override, if you want overnight wake-from-sleep)

If you have a local account password and want `WakeToRun=true` to
actually work for 00:00 / 06:00 fires:

1. Edit the substituted XML — change `<LogonType>InteractiveToken</LogonType>`
   to `<LogonType>Password</LogonType>`
2. Import with explicit credentials:
   ```powershell
   schtasks /Create /XML "$env:TEMP\archimedes-morning-brief.xml" /TN "Archimedes\morning-brief" /RU rtske /RP <password>
   ```

### Verify

```powershell
schtasks /Query /TN "Archimedes\*" /FO LIST /V
```

Expected: each task in `Status: Ready`, `Next Run Time` matching its
schedule, `Logon Mode` showing "Interactive only" (default) or
"Interactive/Background" (Password override).

### Manual trigger to test

```powershell
schtasks /Run /TN "Archimedes\<phase-name>"
```

## Decisions baked into the template

- **User context: rtske, NOT SYSTEM.** SYSTEM cannot reach the user's
  `.env`, OAuth tokens, or `%USERPROFILE%` — required for `.env`
  loading and `claude` CLI auth.
- **Logon type: InteractiveToken (default).** Works with PIN /
  Windows Hello accounts; no stored password required. Tasks fire
  while rtske is logged in (locked screen is fine). See "Logon type
  decision" below for the WakeToRun trade-off.
- **Wake the computer to run** (`<WakeToRun>true</WakeToRun>`).
  Effective ONLY with Password logon type. With the default
  InteractiveToken, the system cannot wake itself for triggers —
  00:00 / 06:00 sweeps may miss if Frank is asleep at trigger time.
- **Start only if any network connection is available.** Prevents
  failed runs when Frank's Wi-Fi is briefly down on resume.
- **Stop the task if it runs longer than 60 minutes.** Bumped from
  30 min in Session 10 (commit `3049bce`) after observing brief runs
  approach the 30-min ceiling. Normal brief runtime is 25-30 min;
  60 gives ~2× headroom while keeping hung-process containment under
  an hour.
- **Restart on failure: 1 attempt, 5 min later.** Retry once on
  transient failures; if the second attempt also fails, the missed
  brief surfaces via Splunk dashboard (no separate dead-man's-switch
  alerting yet — see Session 11 backlog item).
- **Do not run a new instance if previous still running.** Avoids the
  pile-up scenario where 12:00 sweep collides with a stuck 08:00
  brief.

## Logon type decision

The default `InteractiveToken` was chosen during the Session 10 install
because the operator account uses PIN / Windows Hello rather than a
traditional password. There's no stored password for `schtasks /Create
/RP` to consume.

| | InteractiveToken (default) | Password (override) |
|---|---|---|
| Account type | PIN / Hello / passwordless | Local account with password |
| Install command | No `/RU` or `/RP` needed | `/RU rtske /RP <password>` |
| Fires while logged in (active or locked) | ✅ | ✅ |
| Fires while signed out | ❌ | ✅ |
| WakeToRun effective (wakes from sleep) | ❌ | ✅ |
| Password rotation requirement | None | Re-import all 8 tasks if password changes |

If overnight 00:00 / 06:00 sweeps matter and Frank goes to sleep, you
need the Password override. Otherwise InteractiveToken is simpler and
matches the operator's normal login flow.

## What the template assumes about the runtime environment

- `claude` CLI is on PATH for the rtske user account.
- `uv` is on PATH (for the wrapper's Splunk-log invocation).
- Repository is at the path baked into `__REPO_ROOT__`.
- `.env` is populated with all `[active]` vars (per `.env.example`).
- `.mcp.json` enables the MCPs the agents need.
- `.claude/settings.local.json` allow-list covers tools the wrapper's
  prompts will trigger (or `--permission-mode bypassPermissions`
  in the wrapper does the same — currently the wrapper uses bypass).

## Manual wrapper invocation (outside Task Scheduler)

If you need to run the wrapper directly — for testing a phase prompt,
catching up after a missed scheduled fire, or debugging — be aware of
the PowerShell execution policy gotcha:

```powershell
# This will FAIL if your execution policy is Restricted (default on workstations):
.\scripts\run_phase.ps1 -Phase morning-brief

# Use this instead — it matches what the Task Scheduler XML does:
powershell.exe -NoProfile -ExecutionPolicy Bypass `
    -File "C:\Users\rtske\Projects\archimedes\scripts\run_phase.ps1" `
    -Phase morning-brief
```

Task Scheduler invocations don't hit this because the XML's `<Arguments>`
already include `-ExecutionPolicy Bypass`. Manual invocations from a
fresh PowerShell session need to add it themselves.

## Known issues

- **`pre-brief-morning` and `pre-brief-afternoon` not yet installed.**
  These two phase prompts in `scripts/run_phase.ps1` cause the
  orchestrator to run the *full* brief pipeline rather than just
  collection. Installing them as-scheduled would create a double-brief
  regression (07:30 + 08:00 each fire the full pipeline). Fix is in
  Session 11 backlog item #1; until then, the morning-brief and
  afternoon-brief tasks do their own collection inline.

- **InteractiveToken means no overnight wake.** Documented above; if
  Frank sleeps overnight, the 00:00 and 06:00 sweeps miss. Decide
  whether to (a) configure Frank to never sleep, (b) provision a local
  account password and switch to the Password override, or (c) accept
  best-effort overnight sweeps.

## Disabling vs deleting

To pause all scheduled runs without losing the task definitions:

```
schtasks /Change /TN "Archimedes\*" /DISABLE
```

Re-enable with `/ENABLE`. Tasks survive reboots either way.

## Related

- Wrapper script: `scripts/run_phase.ps1`
- Phase prompts: defined in the wrapper's `$PhasePrompts` hashtable
- Logs: `logs/scheduler/YYYY-MM-DD/<phase>-<HHMM>.log`
- Splunk events: `index=archimedes sourcetype=archimedes:scheduler`
