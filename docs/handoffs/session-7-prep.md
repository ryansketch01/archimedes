# Session 7 Prep — Scheduler + Headless Invocation

Forward-looking, not retrospective. This is the Session 7 starting
checklist so the real session opens with answered questions instead of
exploration overhead.

## Session 7 deliverable

A `scripts/run_brief.ps1` (or `.sh`) wrapper that, when invoked,
launches Claude Code in headless mode with a phase-specific prompt,
captures stdout/stderr to a log file, and returns a meaningful exit
code. Plus 8 Windows Task Scheduler entries that fire the wrapper at
the cadence in CLAUDE.md. **Schedules drafted but NOT enabled** —
enabling is a Session 10 step.

**Gate:** invoking the wrapper manually with phase=`morning-brief`
produces a brief file in `threats/briefs/` (synthetic content fine —
real-data testing is Session 8 / 9).

## Pre-Session 7 checklist (do these before starting)

### 1. Confirm headless Claude Code CLI shape

The expected pattern is `claude -p "<prompt>"` (one-shot headless
mode), but I haven't verified it from this repo. Before Session 7
opens, run a smoke test from Frank's terminal:

```
cd C:\Users\rtske\Projects\archimedes
claude -p "List the contents of CLAUDE.md hard rules section" --output-format text
```

Note what flags exist for:
- Output format (`--output-format text|json|stream-json`)
- MCP server enablement (`--mcp-config` or auto-loaded from `.mcp.json`)
- Permission mode (`--permission-mode bypassPermissions`? — needed for
  unattended runs)
- Model selection (`--model`)
- Timeout
- Log file destination

If the CLI has changed shape since this prep note was written, the
wrapper design assumptions below shift accordingly.

### 2. Confirm Frank's Task Scheduler context

Decisions to settle before Session 7:
- **Run as which user?** Should be Ryan's account (so `.env` and
  Discord token are accessible via user-profile paths). NOT SYSTEM.
- **Run only when logged on, or always?** If Frank reboots overnight,
  "only when logged on" misses 06:00 firings. Consider "Run whether
  user is logged on or not" with stored credentials.
- **Wake the computer to run?** Probably yes for the 00:00 / 06:00
  alert sweeps. Otherwise Frank must stay awake.
- **Network availability check?** Task Scheduler can require
  "Start only if any network connection is available" — useful to
  prevent failed runs when Frank's Wi-Fi is briefly down.

### 3. Confirm Claude Code billing posture

8 scheduled invocations per day × ~30 days/month = ~240 sessions.
Per-session token cost depends on prompt size and how many subagents
fire. Rough budget check:
- Pre-brief collection (07:30, 15:30): collector only, ~5–10k tokens
- Morning/afternoon brief (08:00, 16:00): full pipeline (collector +
  grader + analyst + red-team + briefer + librarian),
  ~50–100k tokens each
- Alert sweeps (00:00, 06:00, 12:00, 18:00): collector narrow scope,
  most exit silently, ~3–8k tokens

Eyeball: ~200k tokens/day × 30 = 6M tokens/month. Confirm that's in
budget before enabling any schedule. If it's tight, **defer the
00:00 / 06:00 sweeps** — they're the lowest-yield firings (everything
queues to 09:00 anyway).

## Open design questions

### Q1: PowerShell or Bash for the wrapper?

**Lean: PowerShell.** Windows-native, no Git Bash dependency, plays
better with Task Scheduler logging conventions. The bash convention
elsewhere in the repo is for hook contracts that Claude Code itself
invokes — those run in Claude's bash. The Task Scheduler wrapper is a
different boundary (OS-level), so matching the OS norm makes sense.

Implication: PowerShell 5.1 quirks documented in the system prompt
(no `&&`, no `??`, UTF-16 default encoding) all apply. Use here-strings
for prompt text, `Out-File -Encoding utf8` if writing logs.

### Q2: Single wrapper with `--phase` arg, or 8 separate scripts?

**Lean: single wrapper.** All 8 firings differ only in the prompt
text. A `run_phase.ps1 -Phase morning-brief` form keeps the surface
small and the logic in one place. The 8 Task Scheduler entries each
pass a different `-Phase` value.

### Q3: Where do logs land?

Need a place for Task Scheduler output capture so failures are
debuggable. Options:
- `logs/scheduler/YYYY-MM-DD/<phase>-<HHMM>.log` — simple, grep-able
- Splunk via splunk-log.sh after each run — eats our own dog food,
  queryable
- Both — log file for raw stdout/stderr, Splunk for structured
  pipeline metadata

**Lean: both.** Log file for traceback-level debugging; Splunk event
for "did the 08:00 run actually fire and complete?" metric.

### Q4: How does the wrapper know if Claude Code "succeeded"?

Claude Code's exit code reflects process termination, not whether the
brief was actually published. Two definitions of success:
- **Process success:** `claude -p` exited 0 (no crash, no API error)
- **Pipeline success:** the brief file exists in `threats/briefs/`
  AND was committed to git AND was posted to Discord

The wrapper should check the latter — verify the expected output
artifacts exist after the run completes. If process exited 0 but no
brief file was written, that's a failure to escalate.

## Recommended prompt drafts (one per phase)

These are the texts the wrapper passes to `claude -p`. Each is short —
trust the agent to consult CLAUDE.md and follow the runbook. Tighten
or expand based on Session 7 testing.

| Phase | Cron (EDT) | Prompt |
|---|---|---|
| `pre-brief-morning` | 07:30 | `Run pre-brief collection for the 08:00 morning brief per CLAUDE.md Pipeline — Scheduled Brief.` |
| `morning-brief` | 08:00 | `Run the 08:00 morning brief pipeline per CLAUDE.md. Grade, analyze, brief, deliver.` |
| `alert-sweep-noon` | 12:00 | `Run a FLASH alert sweep per doctrine/FLASH-POLICY.md. Exit silently if no triggers.` |
| `pre-brief-afternoon` | 15:30 | `Run pre-brief collection for the 16:00 afternoon brief per CLAUDE.md Pipeline — Scheduled Brief.` |
| `afternoon-brief` | 16:00 | `Run the 16:00 afternoon brief pipeline per CLAUDE.md. Grade, analyze, brief, deliver.` |
| `alert-sweep-evening` | 18:00 | `Run a FLASH alert sweep per doctrine/FLASH-POLICY.md. Exit silently if no triggers.` |
| `alert-sweep-midnight` | 00:00 | `Run a FLASH alert sweep per doctrine/FLASH-POLICY.md. Quiet hours active — queue any triggers.` |
| `alert-sweep-dawn` | 06:00 | `Run a FLASH alert sweep per doctrine/FLASH-POLICY.md. Quiet hours active — queue any triggers.` |

Subagents are NOT invoked from the prompt — the orchestrator decides
based on CLAUDE.md and the phase. This is the correct level of
abstraction; pushing subagent choreography into prompts would
duplicate doctrine.

## Risk flags for Session 7

1. **Headless Claude Code may not auto-enable project MCPs.** If
   `claude -p` doesn't pick up `.mcp.json` automatically, the
   collector subagent can't reach Splunk / VT / Shodan. Smoke-test
   this early: `claude -p "Use mcp__splunk-query__health to test the
   Splunk MCP connection."` from headless — if it returns the health
   check, MCPs are auto-loaded.

2. **Permission prompts deadlock unattended runs.** If any tool
   triggers a permission prompt mid-pipeline, the headless session
   hangs forever. Need `--permission-mode bypassPermissions` (or
   pre-grant via `.claude/settings.local.json` allow-list). The
   existing allow-list only covers 2 splunk-query tools — needs
   expansion.

3. **Subagent invocation in headless mode is unverified.** I've seen
   subagents work in interactive Claude Code sessions but never in
   `-p` mode. If they don't fire, the pipeline collapses to a
   single-orchestrator flow which is materially weaker. **First thing
   to test in Session 7.**

4. **Long-running pipelines may exceed Task Scheduler's default
   timeout.** Morning brief might take 5–10 min. Default scheduler
   timeout is 72 hours, but if any per-call timeout (Claude Code's
   own) is shorter, we'll hit it.

5. **Stale process on the next firing.** If 08:00 brief takes longer
   than 4 hours (it shouldn't, but…), the 12:00 alert sweep collides.
   Wrapper should check for an existing lock file before starting and
   either skip-with-log or wait.

## Suggested Session 7 verification gates

Build them in order. Each gate must pass before the next is attempted.

1. Headless `claude -p "echo test"` returns within 30s with sane output.
2. Headless `claude -p "Use mcp__splunk-query__health"` returns the
   health check (proves MCPs auto-load).
3. Headless `claude -p "Use the collector subagent to..."` actually
   invokes the subagent (proves subagent invocation works in `-p`).
4. PowerShell wrapper invokes Claude with a hardcoded test prompt and
   captures output to a log file.
5. PowerShell wrapper with `-Phase morning-brief` produces a brief
   file in `threats/briefs/` with synthetic raw signal seeded.
6. Splunk event logged for the run via splunk-log.sh.
7. (Stretch) One Task Scheduler entry created for the test wrapper
   and triggered manually via Run Now — no actual schedule yet.

If gates 1–3 fail, **stop the sprint** and re-evaluate. Headless +
MCPs + subagents is the load-bearing assumption underneath the entire
production-schedule plan. If any of those don't work, the architecture
needs rethinking before Session 8.

## Time budget estimate

- Gates 1–3 (headless MCP + subagent verification): 60 min
- Wrapper design + draft: 45 min
- Wrapper smoke test (gates 4–5): 60 min
- Splunk integration (gate 6): 30 min
- Task Scheduler one-shot test (gate 7): 30 min
- Buffer for fixes: 60 min

**Total: ~4 hours.** If gates 1–3 all pass cleanly, Session 7 finishes
ahead of schedule and Session 8 absorbs the surplus.

## What gets cut from Session 7 if scope slips

- Multi-phase wrapper logic (start with `morning-brief` only, add the
  other 7 phases in Session 8)
- Splunk run-logging integration (defer to Session 8)
- Task Scheduler one-shot test (defer to Session 10 enable step)
- Failure-mode handling (escalation, retry, lock files) — defer to
  Session 10

## Pre-session memory write (for future-me)

When Session 7 starts cold, the first thing to do is read this file
plus `docs/handoffs/session-6.md`. Then run the three smoke tests in
"Suggested Session 7 verification gates" steps 1–3. Don't write any
wrapper code until gates 1–3 pass. If any of them fails, surface to
Ryan immediately rather than working around it — those are
architectural assumptions, not implementation details.

---

*Drafted at end of Session 6 (2026-05-01). Targeted for Session 7
start (Mon 2026-05-04).*
