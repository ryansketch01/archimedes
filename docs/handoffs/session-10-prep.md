# Session 10 Prep — Hardening + Production Schedule Enablement

Forward-looking, not retrospective. Session 10 is the **launch
session** — once the 8 Task Scheduler entries are armed and
verified, Archimedes runs unattended on the cadence in CLAUDE.md
"Daily Rhythm." First unattended brief fires Tue 2026-05-05 at
08:00 EDT.

Sessions 9 and 10 are stacked on Mon 2026-05-04. Session 10 starts
only after Session 9 ships a real morning brief AND a real FLASH
brief end-to-end. **If Session 9 doesn't ship clean, Session 10
defers** — production launch slips to Tue/Wed.

## Session 10 deliverable

By end of Monday:

1. All 8 Task Scheduler entries installed on Frank per the template
   in `infrastructure/scheduler/archimedes-task-template.xml`.
2. At least one task manually triggered via `schtasks /Run` and
   verified end-to-end (Splunk paired events landed, Discord posted
   if applicable, log file written).
3. The remaining 7 tasks left enabled but **not** manually triggered
   — let the scheduler fire them on their natural cadence.
4. A short post-launch monitoring note added to the Session 10
   handoff documenting what Tuesday's first unattended runs should
   produce and how to verify.

**Gate:** `schtasks /Query /TN "Archimedes\*"` lists 8 enabled
tasks; one has been successfully manually triggered; the manual
trigger produced expected Splunk events and Discord post.

## Pre-Session 10 checklist

### 1. Confirm Session 9 actually shipped clean

Open by reading `docs/handoffs/session-9.md` (the retrospective
written at end of Session 9). Verify:

- Real morning brief committed and posted to `#intel-briefs`
- FLASH brief end-to-end ran (synthetic trigger or real, both fine)
- Test-fixture exclusion clause restored after FLASH testing
- No outstanding subagent quirks the prep didn't anticipate

If any of those failed, **stop and surface to Ryan before installing
any scheduled task.** A broken pipeline running on a schedule is
worse than a manually-fired pipeline.

### 2. Confirm Frank's Task Scheduler service is running

```
Get-Service Schedule
```

Should show `Running`. If not, start it (`Start-Service Schedule`).
Should be running by default on Win11 Pro.

### 3. Confirm `claude` CLI auth is valid for unattended runs

The headless wrapper invokes `claude -p`. That uses the local
authentication state. Run a one-shot smoke test:

```
claude -p "Reply OK" --output-format text
```

Should return `OK` cleanly. If it prompts for re-auth, log in
interactively first — Task Scheduler's user context inherits the
saved auth state, but a stale token blocks unattended runs.

### 4. Have Frank's user password ready

The template uses `LogonType: Password` with `Run whether user is
logged on or not` so 00:00 / 06:00 firings work even at the lock
screen. Task Scheduler asks for the password during `schtasks
/Create /XML ... /RU rtske /RP <password>` import. Required for
each of the 8 imports.

## Open design questions

### Q1: Install all 8 at once, or stage?

Three options:

- **A. Install + enable all 8 immediately.** Fastest path to
  "production." Risk: if a phase prompt is wrong, all 8 fail in
  similar ways before you notice.
- **B. Install 1 (alert-sweep-noon — runs frequently, low-impact),
  observe one full cycle, then install the other 7.** Safer but
  forces a delay between Session 10 and full launch.
- **C. Install all 8 disabled, then enable them one at a time over
  2-3 days.** Compromise but slow.

**Lean: A.** Sessions 6-9 already validated each component. The
stop-after-first-failure pattern is already baked into Task
Scheduler (`MultipleInstancesPolicy: IgnoreNew`). If a prompt is
wrong, it's wrong the same way for all 8 phases — better to find
that out at install time than after one phase has been "verified"
in isolation.

### Q2: Trigger one manually, or trust the schedule?

After install, do you fire one with `schtasks /Run` to validate, or
wait for the next natural cadence?

**Lean: trigger one.** Specifically the `alert-sweep-noon` or
`alert-sweep-evening` task (they have the cheapest prompt — exit
silently if no triggers). One manual fire takes ~2 minutes,
validates the unattended invocation pattern, produces Splunk events
to confirm the Tuesday-morning behavior. Cheap insurance.

### Q3: Dead-man's-switch alert

CLAUDE.md mentions a "dead-man's-switch" pattern for catching
missed scheduled runs. Three options:

- **A. Build now.** Splunk saved search that alerts if no
  `archimedes:scheduler` event with `phase=morning-brief` in the
  last 24 hours.
- **B. Defer to the May 8 Splunk Ops scheduled agent.** That
  agent's charter explicitly includes drafting saved searches.
  Less duplication of work.
- **C. Skip entirely.** First-week monitoring is manual.

**Lean: B.** The May 8 agent will produce a designed-from-scratch
alert that integrates with the dashboards/saved-searches it also
drafts. Building it ad-hoc Monday means doing the work twice.

For Tuesday-Friday's unattended runs without the alert: you'll
need to spot-check Splunk manually each morning (`index=archimedes
sourcetype=archimedes:scheduler phase=morning-brief earliest=-24h`).
Five minutes a day until the agent ships.

### Q4: First-day cadence — pause briefs, or let them all fire?

Session 10 finishes Monday EOD. Tuesday's cadence per CLAUDE.md:
- 00:00 (Mon→Tue night) alert-sweep-midnight
- 06:00 alert-sweep-dawn
- 07:30 pre-brief-morning
- 08:00 morning-brief
- 12:00 alert-sweep-noon
- 15:30 pre-brief-afternoon
- 16:00 afternoon-brief
- 18:00 alert-sweep-evening

If you want to slow the unveiling, disable the 00:00/06:00 alert
sweeps for the first 24 hours and let the day-shift cadence run.
Lean: **let them all fire**. The alert sweeps mostly exit silently
(no triggers); they're cheap; if they break they break safely.

## Recommended Session 10 staging plan

Three steps. Each takes ~30 minutes including verification.

### Stage 1 — Install all 8 tasks

For each phase in CLAUDE.md daily rhythm:

```
$phase = "morning-brief"      # repeat for each
$time = "2026-05-05T08:00:00" # adjust per phase per CLAUDE.md
$repo = "C:\Users\rtske\Projects\archimedes"

# Substitute placeholders in the template
(Get-Content infrastructure\scheduler\archimedes-task-template.xml) `
  -replace '__PHASE__', $phase `
  -replace '__TIME__', $time `
  -replace '__REPO_ROOT__', $repo `
  | Set-Content "$env:TEMP\archimedes-$phase.xml" -Encoding utf8

schtasks /Create /XML "$env:TEMP\archimedes-$phase.xml" `
  /TN "Archimedes\$phase" /RU rtske /RP <password>
```

**Gate:** `schtasks /Query /TN "Archimedes\*"` lists all 8 with
`Status: Ready` and the right `Next Run Time`.

### Stage 2 — Trigger one manually for live validation

Pick `alert-sweep-noon` (cheapest — exits silently if no triggers,
short runtime, frequent enough that one extra fire is invisible):

```
schtasks /Run /TN "Archimedes\alert-sweep-noon"
```

Watch:
- `logs/scheduler/2026-05-04/alert-sweep-noon-*.log` appears
- `index=archimedes sourcetype=archimedes:scheduler
   phase=alert-sweep-noon earliest=-15m` shows started + completed
- If the sweep produced a finding, FLASH brief lands in
  `#flash-alerts`

**Gate:** all three observations confirm. If any fail, stop —
production launch defers until the failure is understood.

### Stage 3 — Document and adjourn

Update `docs/handoffs/session-10.md` (the retrospective) with:
- Which 8 tasks installed (for future cleanup reference)
- The manual-trigger result
- A "Tuesday morning checklist" for Ryan: what to look for at 08:30
  EDT to confirm the first unattended morning brief shipped

## Risk flags for Session 10

1. **First unattended run is Tuesday 08:00 EDT.** Nobody is
   watching. If it fails silently, you find out at 08:30 when no
   Discord notification arrived.

2. **Stored password in Task Scheduler.** Best practice; not a
   security concern on Frank's BitLocker'd local-only setup. Worth
   knowing the password is committed to Task Scheduler's encrypted
   credential store — rotating Ryan's account password requires
   re-importing all 8 tasks.

3. **Wake-to-run depends on power settings.** If Frank's BIOS or
   power plan disables wake-from-sleep, the 00:00/06:00 sweeps miss
   silently. Worth a one-time check before adjourning Session 10:
   `powercfg /a` to see what wake states are enabled.

4. **Token billing on production cadence.** ~6M tokens/month per
   the Session 7 prep estimate. First week's burn is observable
   in your usage dashboard — flag if the rate exceeds projection.

5. **Discord channel pollution if pipeline misbehaves at scale.**
   Manual-fire test runs are limited; production cadence runs 8
   times daily forever. A briefer regression that only surfaces on
   the 5th unattended run could pollute `#intel-briefs` with bad
   content. Worth a daily pre-flight grep through the morning brief
   for the first week.

## Verification gates

In order. Each one cheap, each one gates the next.

1. Session 9 retrospective shows real brief + FLASH both clean.
2. `Get-Service Schedule` shows Running.
3. Headless `claude -p "Reply OK"` returns OK.
4. Stage 1: all 8 tasks installed; `schtasks /Query` confirms.
5. Stage 2: manual trigger of `alert-sweep-noon` produces Splunk
   started + completed events with matching run_id.
6. Stage 3: Session 10 handoff written, "Tuesday morning checklist"
   for Ryan included.

## Time budget estimate

- Pre-session checklist: 15 min (assuming Session 9 verifications
  carry forward)
- Stage 1 (8 task imports + verification): 60 min
- Stage 2 (manual trigger + Splunk verify + Discord verify): 30 min
- Stage 3 (handoff write): 30 min

**Total: ~2.25 hours.** Smaller than Session 9 because the work is
mostly procedural — install, verify, document.

## What gets cut from Session 10 if scope slips

- Dead-man's-switch alert (defer to May 8 Splunk Ops agent — see Q3)
- Splunk dashboard / saved searches (same)
- The wake-from-sleep verification (do post-launch if you don't get
  to it)
- Multi-task manual-trigger verification (one is enough; the
  remaining 7 will fire on their natural cadence Tuesday)

## What does NOT get cut

- All 8 task installs. Half-installed = production runs on a
  partial cadence, gaps where briefs/sweeps don't fire.
- Stage 2 manual trigger. Without a live validation, Session 10
  just hopes the schedule works. Spend the 30 minutes.
- Session 10 retrospective with Tuesday morning checklist. Ryan
  needs to know what to look for when the first unattended brief
  fires while he's having coffee.

## Pre-session memory write (for future-me)

When Session 10 starts cold, the first thing to do is read
`docs/handoffs/session-9.md` and confirm the gates 1-6 above.
**Don't open Session 10 if Session 9 didn't ship.** Production
launch is the last action of the sprint; there's no tolerance for
"we'll fix it after launch."

If Stage 2's manual trigger surfaces a failure, the right move is
to disable all 8 tasks (`schtasks /Change /TN "Archimedes\*"
/DISABLE`) and surface the failure to Ryan. Better a delayed
launch than 8 tasks misbehaving overnight.

---

*Drafted at end of Session 8 (2026-05-03). Targeted for Session 10
start (Mon 2026-05-04, same-day after Session 9 ships clean).*
