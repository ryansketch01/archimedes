# Archimedes Scheduler — Windows Task Scheduler Configuration

Frank runs the Archimedes scheduled brief and FLASH alert pipelines via
Windows Task Scheduler. This directory holds the task XML template and
the install procedure. **Tasks are NOT installed automatically by
checkout** — installation is a deliberate Session 10 step after
Sessions 8-9 verify the wrapper end-to-end with real data.

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

## Install procedure (Session 10, NOT yet run)

For each of the 8 phases above:

1. Copy `archimedes-task-template.xml` to a working file.
2. Edit the working file:
   - Replace `__PHASE__` with the phase name (e.g. `morning-brief`).
   - Replace `__TIME__` with the EDT time as `2026-05-08THH:MM:SS`
     (the date is the start date, recurrence picks up the time).
   - Confirm `__REPO_ROOT__` is the absolute path on Frank.
3. Import via PowerShell as Administrator:
   ```
   schtasks /Create /XML <working-file> /TN "Archimedes\<phase-name>" /RU rtske /RP <password>
   ```
4. Verify:
   ```
   schtasks /Query /TN "Archimedes\<phase-name>" /V
   ```
5. Manual trigger to test:
   ```
   schtasks /Run /TN "Archimedes\<phase-name>"
   ```

## Decisions baked into the template

- **User context: rtske, NOT SYSTEM.** SYSTEM cannot reach the user's
  `.env`, OAuth tokens, or `%USERPROFILE%` — required for `.env`
  loading and `claude` CLI auth.
- **Run whether user logged on or not.** Frank may be at the lock
  screen during 00:00 / 06:00 firings. Requires storing the user
  password (Task Scheduler prompts for it on import).
- **Wake the computer to run.** The 00:00 / 06:00 alert sweeps must
  fire even if Frank is asleep. Ensures FLASH triggers don't get
  silently missed.
- **Start only if any network connection is available.** Prevents
  failed runs when Frank's Wi-Fi is briefly down on resume.
- **Stop the task if it runs longer than 30 minutes.** A morning brief
  should finish in 5-10 minutes. 30 is a generous fail-safe.
- **Restart on failure: 1 attempt, 5 min later.** Retry once on
  transient failures; if the second attempt also fails, alert via the
  dead-man's-switch (Session 9+).
- **Do not run a new instance if previous still running.** Avoids the
  pile-up scenario where 12:00 sweep collides with a stuck 08:00
  brief.

## What the template assumes about the runtime environment

- `claude` CLI is on PATH for the rtske user account.
- `uv` is on PATH (for the wrapper's Splunk-log invocation).
- Repository is at the path baked into `__REPO_ROOT__`.
- `.env` is populated with all `[active]` vars (per `.env.example`).
- `.mcp.json` enables the MCPs the agents need.
- `.claude/settings.local.json` allow-list covers tools the wrapper's
  prompts will trigger (or `--permission-mode bypassPermissions`
  in the wrapper does the same — currently the wrapper uses bypass).

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
