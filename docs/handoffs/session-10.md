# Session 10 — Production Schedule Enablement (Retrospective)

**Date:** 2026-05-05 (Tuesday)
**Status:** Production cadence live on Frank. Two unattended fires verified end-to-end same day. First unattended morning brief fires Wednesday 2026-05-06 08:00 EDT.

---

## Summary

Session 10 was supposed to be a Monday-evening installation session with the first unattended fire on Tuesday morning. It slipped: the planned Monday-night Session 10 conversation never opened, so when 2026-05-06 08:00 EDT arrived there was nothing for Windows Task Scheduler to fire. We recovered same-day:

1. Manually shipped the morning brief at ~10:00 EDT via the wrapper.
2. Patched and installed 6-of-8 Task Scheduler entries before 16:00 EDT.
3. Verified the launch live at 16:00 EDT (afternoon-brief fired unattended, end-to-end clean).
4. Verified again at 18:00 EDT (alert-sweep-evening, silent sweep, exit 0).
5. Bootstrapped `infrastructure/source-health.yaml` and provisioned 3 new OSINT API keys (free), unlocking 11 additional sources.

**The launch is live.** Wednesday 2026-05-06 08:00 EDT is the first unattended morning brief.

---

## What landed (commits on origin/main)

| SHA | Description |
|---|---|
| `5404834` | brief: 2026-05-05 morning — 6 findings (UNC1549, Charming Kitten, FortiManager KEV, IIS HTTP.sys 0day, Cisco ASA, Siemens SIMATIC) |
| `3049bce` | infra: scheduler — bump ExecutionTimeLimit PT30M→PT60M |
| `8dee546` | brief: 2026-05-05 afternoon — 3 findings (MSTIC AitM, DAEMON Tools, Ollama CVE-2026-7482) |

## What changed locally (intentionally not committed)

- **6 Task Scheduler entries** installed under `\Archimedes\` — all in `Ready` state with correct `NextRunTime`. XML import files generated in `$env:TEMP`, used once, not retained in repo.
- **3 API keys** added to `.env` (gitignored): `ABUSECH_API_KEY`, `GITHUB_TOKEN`, `YOUTUBE_API_KEY`. Each verified live before flipping source-health.
- **`infrastructure/source-health.yaml`** created (gitignored — runtime state per `.gitignore` line 55). 45 sources tracked: 42 healthy, 3 stale.

---

## Validations

### Unattended fires verified

| Time (EDT) | Phase | run_id | Duration | Exit | Outcome |
|---|---|---|---|---|---|
| 16:00:02 | afternoon-brief | `afternoon-brief-20260505-160002` | 24:27 | 0 | Brief published, Discord posted (msg 1501318435974418482), commit `8dee546`, push held pending review |
| 18:00:02 | alert-sweep-evening | `alert-sweep-evening-20260505-180001` | 3:32 | 0 | Silent sweep, no triggers |

Both fires produced complete `started` + `completed` event pairs in Splunk via the wrapper's pre/post logging.

### Configuration validations

- **`InteractiveToken` LogonType works** with the user's PIN/Windows Hello account. No password storage required by Task Scheduler. Tasks fire while user is logged in (locked screen is fine).
- **PT60M ExecutionTimeLimit** holds: afternoon brief ran 24:27, well under the limit. Original PT30M would have hard-killed the morning brief's 68-min outlier (caused by the pre-brief scope-creep bug, see Session 11 backlog).
- **PowerShell execution policy bypass** works as designed in the task template (`-ExecutionPolicy Bypass -File ...`). Manual wrapper invocations from a fresh PS session must add `-ExecutionPolicy Bypass` themselves.
- **`claude -p` headless auth** stable across the day. Two pipeline runs and four standalone smoke tests, no re-auth required.

### API key verifications (each tested live)

| Key | Test result |
|---|---|
| `ABUSECH_API_KEY` | ThreatFox `get_iocs` returned 895 IOCs from last 24h |
| `GITHUB_TOKEN` | `/user` auth OK; `/search/code` returned 2136 sample matches; rate limits clean (5000 core/h, 30 search/min, 10 code_search/min) |
| `YOUTUBE_API_KEY` | `search.list` returned; quota 10000 units/day |

### Source-health bootstrap result

- 45 active sources tracked (matches `source-grades.yaml`)
- 42 healthy / 3 stale at session close
- Three remaining stale: `censys`, `urlscan` (key in `.env` but no MCP), `hibp` (no key, paid)
- 11 sources newly unlocked vs. start of session: `threatfox`, `malwarebazaar`, `github-codesearch`, plus 8 YouTube channels

---

## What broke (and how it was handled)

### 1. Session 10 didn't open Monday night
The Sunday evening plan called for a Monday-night Session 10 conversation that would install the 8 task entries before Tuesday morning. That conversation never happened. When 08:00 EDT 2026-05-05 arrived, no tasks existed — the morning brief didn't fire silently. Recovered by manually invoking the wrapper at ~08:54 EDT, which produced today's `5404834` morning brief at 10:02 EDT (~2 hours late but real).

**Lesson:** install-session-late-Sunday-or-Monday-evening is a fragile pattern when the operator gets pulled away. Tasks should be installable from any session, not specifically a "Session 10."

### 2. Wrapper appeared hung for ~67 min during recovery morning brief
The `pre-brief-morning` phase prompt in `scripts/run_phase.ps1` says *"Run pre-brief collection only"* but the orchestrator interpreted it as "run the entire pipeline including grading, briefing, posting, and committing." The result was correct (brief shipped) but the wrapper looked stuck for an alarming length of time. Diagnosed via process inspection (claude PID 20612, 46 sec CPU, responsive); ultimately self-completed. **Real scope-creep bug deferred to Session 11.**

### 3. PowerShell execution policy blocked first manual wrapper attempt
`Get-ExecutionPolicy -List` showed `Undefined` at all scopes (defaults to `Restricted` on workstation). My first background invocation failed with "running scripts is disabled." Re-ran with explicit `-ExecutionPolicy Bypass`. The production task template already uses this flag, so unattended runs are unaffected.

### 4. PowerShell-to-XML encoding mismatch on first XML regeneration
The `archimedes-task-template.xml` file is stored as UTF-8 but its XML declaration claims `encoding="UTF-16"`. My first regeneration script read with `-Encoding Unicode` (treating UTF-8 bytes as UTF-16 LE), which produced CJK-character mojibake. The substitution silently failed; the resulting XMLs were corrupt. Fixed by reading as UTF-8 and writing UTF-16 LE BOM. **Pre-existing file inconsistency, deferred to Session 11.**

### 5. Password-based LogonType broke on PIN/Windows Hello
The default task template uses `<LogonType>Password</LogonType>` with `WakeToRun=true` so 00:00 / 06:00 sweeps work even at the lock screen. But Frank logs in via PIN; there's no password to provide to `schtasks /Create /RP`. Switched the install's XMLs to `<LogonType>InteractiveToken</LogonType>` (template on-disk left as-is). Tradeoff: `WakeToRun` is now ineffective — Task Scheduler can't wake Frank from sleep without a stored credential. Practical impact:

- 12:00 / 16:00 / 18:00 / 08:00 fires: ✅ work fine (Frank awake)
- 00:00 / 06:00 fires: ⚠️ may miss if Frank is asleep (mitigation deferred — see backlog)

### 6. Librarian held push for review on afternoon brief
Today's morning brief auto-pushed (commit `5404834` landed on origin/main automatically). Today's afternoon brief did NOT auto-push (commit `8dee546` stayed local until manual `git push`). The wrapper log explicitly stated *"Push to `origin/main` is held pending your authorization."* Inconsistent behavior between morning and afternoon — same code path, same tooling. Possibly a heuristic in the librarian based on "first unattended Task Scheduler fire" being treated more conservatively. **Doctrine clarification deferred to Session 11.**

### 7. Splunk `brief_published` event payload regressed
The morning brief's `brief_published` event included `discord_post_status`, `target_channel`, `finding_ids`, `iocs_count`, `actor_refs`, `cve_refs`. The afternoon brief's event had only `word_count` and `preflight_result`. Discord post itself succeeded (verified via Splunk message-ID and the wrapper log) — just the structured telemetry was thinned. **Real telemetry regression; affects the dashboard panels designed earlier in the session. Deferred to Session 11.**

### 8. UNC1549 + Charming Kitten dossiers don't exist on disk
The morning brief's two actor-attributed findings flagged 17 new IOCs for ingestion into UNC1549 (#004) and Charming Kitten (#011) sidecars. The actor-profiler halted on Mode-1 ground-truth check: `_roster.yaml` lists both actors with `dossier:` paths and `last_reviewed` dates, but no dossier files have ever been written. The 17 IOCs are captured in the actor-profiler's halt response (this conversation) but NOT yet on disk. **Session 11 should scaffold both dossiers and ingest the IOCs.**

### 9. ABUSECH vs ABUSEIPDB key confusion
User registered at https://auth.abuse.ch (correct site) but pasted the abuse.ch key onto the line previously labeled `ABUSEIPDB_API_KEY` (different service). Variable name corrected; key value preserved. Worth a one-liner in `.env.example` clarifying these are separate services.

---

## What to watch — Wednesday 2026-05-06 08:30 EDT

The 08:00 EDT morning-brief Task Scheduler entry fires for the first time unattended. By 08:30 EDT (allowing for ~25 min pipeline runtime), all of these should be true. **If any are not, see "If something went wrong" below.**

### Healthy state checklist

| Check | Where to look | Expected |
|---|---|---|
| 1. Discord brief post | `#intel-briefs` channel | New post timestamped ~08:25-08:30 EDT |
| 2. Brief file | `threats/briefs/2026-05-06-morning.md` | Exists on disk |
| 3. Splunk wrapper events | `index=archimedes sourcetype=archimedes:scheduler phase=morning-brief earliest=@d` | Two events: `started` ~08:00, `completed` ~08:25-08:30 with `exit_code=0` |
| 4. Splunk brief published | `index=archimedes sourcetype=archimedes:operation event_type=brief_published brief_id=2026-05-06-morning earliest=@d` | One event |
| 5. Local git commit | `git log main` from `C:\Users\rtske\Projects\archimedes` | New commit `brief: 2026-05-06 morning — N findings (...)` |
| 6. Origin git commit | `git log origin/main` after `git fetch` | Same commit OR commit absent (see librarian-hold note below) |
| 7. Wrapper log | `logs/scheduler/2026-05-06/morning-brief-0800.log` | Exists with completion summary |

**Librarian-hold note:** if (5) is true but (6) is not, the librarian held the push (same behavior we saw on today's afternoon brief). That's not a failure — the brief is committed safely locally. Push with:

```powershell
cd C:\Users\rtske\Projects\archimedes
git push origin main
```

### If something went wrong

If any of (1)-(7) is missing, run these checks in order:

1. **Did the task fire at all?**
   ```
   schtasks /Query /TN "Archimedes\morning-brief" /FO LIST /V
   ```
   Look at `Last Run Time` and `Last Result`. `Last Result` of `0` = ran successfully; non-zero = check the wrapper log; `267011` (TASK_NEVER_RAN) = task never fired (was Frank awake at 08:00?).

2. **If the task ran but didn't produce a brief**, read the wrapper log:
   ```
   Get-Content "C:\Users\rtske\Projects\archimedes\logs\scheduler\2026-05-06\morning-brief-0800.log" -Tail 80
   ```
   The last 50 lines summarize the pipeline outcome.

3. **If the wrapper log is empty or missing**, check Task Scheduler's own event log for errors:
   ```
   Get-WinEvent -LogName "Microsoft-Windows-TaskScheduler/Operational" -MaxEvents 20 |
     Where-Object { $_.Message -like '*Archimedes*morning-brief*' }
   ```

4. **If Splunk events are missing entirely**, the wrapper failed before its pre-flight log step (most likely cause: `claude` CLI auth expired or `splunk_log.py` couldn't reach HEC). Test with:
   ```
   claude -p "Reply OK" --output-format text
   ```

5. **If Frank was asleep at 08:00 EDT**, the task didn't fire (`InteractiveToken` cannot wake from sleep). Check power plan: `powercfg /a` and `powercfg /lastwake`. Mitigation deferred to Session 11.

---

## Session 11 backlog

In rough priority order. Items 1-4 affect production stability; 5-9 are quality improvements; 10-13 are nice-to-haves.

### Production stability (do first)

1. **Pre-brief prompt scope-creep fix.** `scripts/run_phase.ps1` lines 69, 72: rewrite prompts to be unambiguously "collect only — do not grade, do not brief, do not commit, do not post." Then add the 2 deferred tasks (`pre-brief-morning`, `pre-brief-afternoon`) to Task Scheduler. Without this fix, installing those tasks creates double-brief regressions (07:30 + 08:00 each fire the full pipeline).

2. **Librarian push doctrine.** Decide and document: when does the librarian auto-push vs hold for review? Today's morning auto-pushed; afternoon held. Pick one, write the rule into the librarian agent definition, test.

3. **Power plan / wake-from-sleep strategy for overnight sweeps.** With `InteractiveToken`, Task Scheduler cannot wake Frank for 00:00 / 06:00 sweeps. Three options:
   - Configure Frank to never sleep (simple; trades electricity)
   - Add a local password to the user account just for tasks (defeats PIN convenience)
   - Use S4U logon (no password but limited rights — needs testing for collector network access)
   - Accept that 00:00 / 06:00 sweeps are best-effort

4. **Splunk `brief_published` event payload regression.** Investigate why afternoon brief's event omits `discord_post_status`, `target_channel`, `finding_ids`, `iocs_count`, `actor_refs`, `cve_refs` (all of which the morning brief had). Affects the dashboard panels designed earlier today; without this fix, the Discord-status traffic light won't work.

### Quality improvements

5. **Scaffold UNC1549 + Charming Kitten dossiers.** 17 IOCs from today's morning brief are captured in this session's actor-profiler halt response but not yet on disk. Mode-1 scaffold for both, populate `iocs.md` / `iocs.yaml` from the captured extraction, leave `profile.md` as first-pass draft (7-day deadline) and `threat-box.*` as scoring template (14-day deadline).

6. **Findings missing `published_in_briefs` back-write.** Findings 0001, 0002 (today's morning), and likely 0007-0009 (today's afternoon) have empty `published_in_briefs: []` fields despite being in shipped briefs. Librarian should back-write this on commit.

7. **Template encoding fix.** `infrastructure/scheduler/archimedes-task-template.xml` is UTF-8 but declares `encoding="UTF-16"`. Either re-encode the file as UTF-16 LE BOM or change the declaration to `encoding="UTF-8"`. Pre-existing issue; cost a regeneration cycle today.

8. **Template default LogonType + scheduler/README.md update.** The XML template defaults to `Password` LogonType, which doesn't work with PIN/Hello accounts. Either swap default to `InteractiveToken` (with explicit warning about WakeToRun ineffectiveness) or document the override path in `infrastructure/scheduler/README.md`. Plus add the manual `-ExecutionPolicy Bypass` note for non-Task-Scheduler invocations.

9. **`source-health.yaml` runtime stability.** The collector overwrites entries on each fetch, which will erode the helpful `notes:` strings the bootstrap added (especially for the 3 remaining stale sources: `censys`, `urlscan`, `hibp`). Either teach the collector to preserve operator-set notes, or move "stale because no MCP" to a separate config file.

### Nice-to-haves

10. **Build the missing MCPs.** In rough priority order: `mcp__rss-bridge` (highest impact — unlocks ~25 of 33 healthy RSS sources from WebFetch fallback), `mcp__youtube` (reduces WebFetch load against 8 YT channels), `mcp__urlscan` and `mcp__censys` (small APIs, currently can't authenticate without MCP). Each is real engineering work — Session 11+ scope.

11. **`scripts/regenerate_ioc_index.py` cp1252 print bug.** Cosmetic only — file writes succeed. Fix the print encoding when convenient.

12. **AbuseIPDB integration decision.** Key already in `.env` (48 chars, ABUSEIPDB_API_KEY) but no entry in `source-grades.yaml`. Either add it as an enrichment source (B-grade for facts, F for attribution) or remove the unused key.

13. **HIBP API key (~$3.50/month).** Deferred during Session 10. Decide whether to provision when paid-API budget is reviewed.

---

## Numbers from today

- **2 unattended pipeline fires** verified end-to-end (afternoon-brief, alert-sweep-evening)
- **3 git commits** to origin/main (morning brief, template patch, afternoon brief)
- **9 findings** shipped (6 morning + 3 afternoon)
- **3 OSINT API keys** provisioned and verified live (free)
- **11 sources** flipped from stale to healthy
- **6 Task Scheduler tasks** installed (`alert-sweep-midnight`, `alert-sweep-dawn`, `morning-brief`, `alert-sweep-noon`, `afternoon-brief`, `alert-sweep-evening`)
- **2 tasks deferred** (`pre-brief-morning`, `pre-brief-afternoon`) pending the prompt scope-creep fix
- **42 of 45** active sources marked healthy in `source-health.yaml`

---

## What does NOT roll into Session 11 prep

These were considered and explicitly closed today, NOT deferred:

- **InteractiveToken vs Password LogonType decision** — InteractiveToken is the right default for this user. Password-based won't be revisited.
- **PT30M timeout** — replaced with PT60M; no longer in scope.
- **Whether to install all 8 tasks today or 6** — 6 is the correct answer until the pre-brief prompt is fixed.
- **HIBP buy decision** — explicitly deferred (Session 11 backlog #13).
- **Manual brief on launch day** — handled this morning; no further action needed.

---

*Session 10 closed 2026-05-05 ~19:00 EDT. Production cadence is live. Wednesday 2026-05-06 08:00 EDT is the launch event for unattended morning briefs.*
