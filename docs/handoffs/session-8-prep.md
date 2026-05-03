# Session 8 Prep — First Synthetic End-to-End Brief

Forward-looking, not retrospective. Session 8 is the highest-risk
session of the sprint — it's where every subagent has to chain
together for the first time. Treat it as integration-testing day, not
feature-build day.

## Session 8 deliverable

A morning-brief file in `threats/briefs/` produced by chaining the
real Archimedes subagents (collector → grader → analyst →
red-team-analyst → briefer → librarian), seeded by synthetic
raw-signal, and posted to a non-production Discord channel. **Real
data does not flow until Session 9.**

**Gate:** the brief reads like a real brief (lead, sections, citations,
WEP, no banned phrases) and lands in Discord without manual
intervention beyond the wrapper invocation.

## Pre-Session 8 checklist

### 1. Audit every subagent's `.md` definition

Run before opening Session 8. For each file in `.claude/agents/`,
verify:

- **Tools grant is complete** — does it have what its runbook needs?
  (e.g. librarian needs Bash for `git`, hooks; actor-profiler needs
  `mcp__splunk-query__search` for IOC lookups)
- **No stale path references** — Sessions 5/6 renamed scripts and
  added hooks. Each reference to `splunk-log.py` should be
  `splunk_log.py`; same for `regenerate_ioc_index.py`,
  `migrate_actor.py`. Hooks should be `.claude/hooks/discord-post.sh`
  and `.claude/hooks/splunk-log.sh`.
- **Hard-rule acknowledgement** is present for the subagent's domain
  (e.g. grader must reference INTEL-GRADING.md single-source veto;
  librarian must reference the HIGH-scoring sign-off gate)
- **Empty-input behavior is specified** — what does the grader do
  with no raw-signal? What does the briefer do with no findings?
  These edge cases are where pipelines silently break.

The Session 5 doc-update grep covered the most-trafficked agents but
NOT all of them. There are likely lingering dash-named references in
agents I didn't touch.

### 2. Decide the test Discord channel strategy

Three options, my lean is **Option B**:

- **A. Reuse `#commands`.** Post test briefs there, prefix subject
  with `[TEST]`. Pros: zero setup. Cons: noisy for control traffic;
  long briefs clutter the channel.
- **B. Add a `DISCORD_CHANNEL_TEST` env var + Discord channel.**
  Update `discord_post.py` `CHANNEL_ENV_MAP` with `test` entry, add
  the channel ID to `.env`. Pros: clean separation, consistent with
  the symbolic-channel pattern. Cons: 5 minutes of Discord setup,
  one config change.
- **C. Add a `--dry-run` flag to the librarian's posting path that
  logs instead of posting.** Pros: no test channel needed. Cons:
  doesn't actually exercise the Discord transport, so it's a weaker
  test.

If you go with B, do the Discord-side setup (create channel, copy ID)
before opening Session 8.

### 3. Design the synthetic raw-signal seed

The grader has to accept the seed for the brief to fire. Design it to
PASS the credibility checklist so we exercise the downstream path,
not the rejection path.

Two seed files, both in `threats/raw-signal/`:

- `2026-05-05-test-cve-2026-12345.md` — a fictitious critical CVE in
  a plausible aerospace-defense product. Frontmatter:
  `source: cisa-advisories` (A1 grade), `test: true` (so future
  filters can exclude). Body: severity, affected products, exploit
  status. ~200 words. **Use a CVE ID that does not exist** (e.g.
  CVE-2099-99999) so we can't accidentally publish real-world
  misinformation.
- `2026-05-05-test-actor-mention.md` — a fictitious sighting of a
  tracked Iranian actor (e.g. APT34) in a plausible vendor blog
  context. Frontmatter: `source: mandiant`, `test: true`. Body:
  TTP details, target sector, ~150 words.

Mark both with `test: true` in frontmatter so we can grep them out
after Session 8/9 testing.

### 4. Confirm token budget

Session 7 estimated 50-100k tokens for a morning-brief pipeline. With
debugging iterations, plan for 5-7 full runs = 350-700k tokens.
That's a meaningful chunk of a Max session. Confirm it's in budget
before starting Session 8.

If budget is tight, drop the analyst + red-team stages from the test
runs (the brief still produces, just with weaker analysis).

## Open design questions

### Q1: Run the full pipeline at once, or stage subagents one at a time?

**Lean: stage them, then chain.** "Unit test before integration test"
applied to subagents. See "Recommended Session 8 staging plan" below
for the order. If you go straight to the full `morning-brief` prompt
on first attempt, debugging requires unwinding 5 layers at once.

### Q2: How does the orchestrator know about the synthetic seed?

Options:
- Tell the orchestrator explicitly in the prompt: `Use only
  threats/raw-signal/2026-05-05-test-*.md`. Risks: orchestrator may
  ignore the constraint.
- Move all real raw-signal aside temporarily so the seed is the only
  thing collector finds. Risks: forgetful cleanup; real signal lost
  if test crashes.
- Add a `test_mode: true` config flag the collector reads. Risks:
  feature creep, more code surface.

**Lean: explicit prompt constraint.** Cheapest, no code changes,
visible in logs. Verify the orchestrator obeys it in stage A.

### Q3: Cleanup after Session 8 test runs

Stuff that gets created during testing and shouldn't pollute prod:
- Synthetic raw-signal files (mark with `test: true`, delete after)
- Test findings in `threats/findings/` (add `test: true` filter to
  grader's promotion logic? Or just delete)
- Test brief files in `threats/briefs/` (rename to
  `2026-05-05-TEST-morning.md` so prod-brief globs skip them)
- Test Discord posts (manually delete from the test channel)
- Test git commits (DO NOT commit any test artifacts to main; keep
  on the worktree branch for this session, then squash/drop)

**Lean: keep all test artifacts on the worktree branch.** Don't merge
to main until Session 9 produces a real brief and we know the
pipeline works.

### Q4: When does each subagent's prompt get refined?

If a subagent misbehaves in stage A-F, two paths:
- **Refine the runbook in `.claude/agents/<name>.md`** — durable fix,
  improves all future runs
- **Refine the orchestrator's prompt in `run_phase.ps1`** — quicker,
  but doesn't fix the agent for next time

**Lean: prefer runbook refinement.** Surface the failure in the
agent's `.md`, not the orchestrator's prompt. Keeps the orchestrator
prompt short (per Session 7 design decision).

## Recommended Session 8 staging plan

Six stages plus a final integration run. Each gate is "this stage
produces a usable artifact for the next stage." Don't proceed if a
gate fails.

### Stage A — Collector alone

```
claude -p "Use the collector subagent. Scope: only read
threats/raw-signal/2026-05-05-test-*.md (no external sources). Report
the parsed raw-signal items and source-grades that would apply."
```

**Gate:** collector returns a structured list of the two synthetic
items. No external API calls made (verify in the log — no
mcp__shodan__*, no mcp__virustotal__*, no rss fetches).

### Stage B — Grader on synthetic raw-signal

```
claude -p "Use the grader subagent. Process all un-promoted raw-signal
files matching 2026-05-05-test-*.md. Apply admiralty-grading per
INTEL-GRADING.md. Promote eligible items to threats/findings/ or
log to _rejection-log.yaml with reasoning."
```

**Gate:** at least one promoted finding in `threats/findings/`
with admiralty digraph, source citations, and `test: true`
frontmatter inherited.

### Stage C — Analyst on the promoted finding

```
claude -p "Use the analyst subagent. Apply the sat-ach skill (or
sat-kac, your choice) to the finding produced in stage B. Write the
analysis section into the finding's frontmatter."
```

**Gate:** finding's `analysis_sections` field is populated with an ACH
matrix or KAC output.

### Stage D — Red-team on the analyzed finding

```
claude -p "Use the red-team-analyst subagent. Challenge the finding
produced in stage C. Update its red_team_review field."
```

**Gate:** `red_team_review` field populated with either sign-off or
flagged weaknesses.

### Stage E — Briefer

```
claude -p "Use the briefer subagent. Compose a morning brief from the
findings in threats/findings/ that have status=approved. Write to
threats/briefs/2026-05-05-TEST-morning.md. Run the smart-brevity
pre-flight checklist."
```

**Gate:** brief file exists with valid frontmatter, lead sentence,
sections, and pre-flight checklist passed.

### Stage F — Librarian (Discord post + Splunk log)

```
claude -p "Use the librarian subagent. Take the brief at
threats/briefs/2026-05-05-TEST-morning.md and: (1) post it to the
TEST Discord channel via .claude/hooks/discord-post.sh, (2) log the
delivery to Splunk via .claude/hooks/splunk-log.sh. DO NOT git
commit — this is a test artifact."
```

**Gate:** brief lands in test Discord channel; Splunk has the
delivery event.

### Stage G — Full integration run

Only after A-F all pass:

```
.\scripts\run_phase.ps1 -Phase morning-brief
```

**Gate:** wrapper exit 0; brief file produced; Discord posted;
Splunk paired events. If this works, **Session 8 is done.** If it
fails after A-F all passed individually, the failure is in
orchestrator chaining (highest-value bug to find).

## Risk flags for Session 8

1. **The orchestrator may skip subagents.** A short prompt like "Run
   the morning brief pipeline" trusts the model to know which
   subagents to invoke and in what order. The model may take
   shortcuts (do the work itself instead of delegating). Watch for
   this in stage G logs — if the orchestrator never calls the Agent
   tool with subagent_type=grader, the pipeline isn't actually
   running per CLAUDE.md.

2. **Tool permission gaps.** Each subagent runs with its own tool
   grants. With `--permission-mode bypassPermissions` at the wrapper
   level, all tools are allowed — but if a subagent's `.md` declares
   `tools:` narrowly and the orchestrator tries to invoke a tool
   the subagent doesn't have, that's a different failure mode.

3. **Subagent infinite loops.** SAT-heavy subagents (analyst,
   red-team-analyst) can loop on poor-quality findings. Wrapper
   timeout is currently the only backstop. Consider adding a
   per-subagent max-iteration heuristic to runbooks.

4. **Briefer produces brief that fails its own pre-flight.** The
   smart-brevity skill has a 12-item checklist. If the brief fails,
   does the briefer regenerate? Get stuck? Skip and ship? Behavior
   in headless mode is unverified.

5. **Librarian commits test artifacts to git.** The librarian's
   default behavior is to commit. We DON'T want test commits in main.
   Either prompt the librarian explicitly NOT to commit, or stay on
   the worktree branch and squash before merge.

6. **Cleanup of test artifacts is forgettable.** Test raw-signal,
   findings, briefs, Discord posts, and Splunk events all need to
   age out or be deliberately removed. Add a TODO for Session 9 to
   verify nothing test-flagged leaks into the real morning brief.

## Suggested Session 8 verification gates

(The staging plan above IS the verification gates — A through G in
order. Don't skip ahead.)

## Time budget estimate

- Pre-session checklist (subagent audit, seed design, channel setup): 60 min
- Stages A-F (one subagent at a time, ~10 min each + debugging): 90-120 min
- Stage G (full integration, debugging): 60 min
- Cleanup (delete test artifacts, verify no leakage): 30 min

**Total: ~4-5 hours.** Plan for the high end. Session 8 carries the
sprint's deadline risk.

## What gets cut from Session 8 if scope slips

- Stages C, D (analyst + red-team) can be skipped on the first run.
  The brief will be weaker but the pipeline still demonstrates
  end-to-end flow.
- Stage F (librarian) can be skipped if Discord posting works
  (smoke-tested in Session 6) — verify the brief file is correct
  shape, defer Discord wiring to Session 9.
- Stage G (full integration) can slip to Session 9 if A-E take
  longer than budgeted. Session 9's first real brief becomes the
  first integration test instead of synthetic.

## What does NOT get cut

- Stage A (collector with explicit scope constraint). If we can't
  control the orchestrator's input, we can't test anything safely.
- Stage B (grader). If grading doesn't promote our seed, the
  pipeline is dead-stuck.
- Cleanup at end. Leaving test artifacts in the repo or in Discord
  is a real-world risk worth not punting.

## Pre-session memory write (for future-me)

When Session 8 starts cold, the first thing to do is read this file
plus `docs/handoffs/session-7-prep.md` (for the headless-invocation
patterns) and `docs/handoffs/session-6.md` (for the broader sprint
context). Then run the pre-session checklist BEFORE invoking any
subagent. The audit, the seed design, and the channel decision are
all faster to do up-front than to debug mid-session.

If stage A fails (collector ignores the scope constraint), surface to
Ryan immediately — that's a fundamental orchestrator behavior issue
that probably can't be worked around with prompt engineering alone.

---

*Drafted at end of Session 7 (2026-05-03). Targeted for Session 8
start (Tue 2026-05-05).*
