# Session 9 Prep — First Real Brief + FLASH Wiring

Forward-looking, not retrospective. Session 9 is the **last
major-feature session of the sprint** — Session 10 is hardening +
schedule enablement. Two new code paths get exercised: real OSINT
collection feeding a real brief, and the FLASH alert pipeline (which
is genuinely different from the morning-brief pipeline).

## Session 9 deliverable

Two artifacts in production channels by end of session:

1. A **real morning brief** in `threats/briefs/2026-05-NN-morning.md`,
   composed from actual collected signal (not test fixtures), posted
   to `#intel-briefs`, committed to the worktree branch (or main
   directly if you're ready to merge sprint work first).

2. A **FLASH alert end-to-end run** validating the alternate
   pipeline shape (collector narrow scope → grader fast path →
   briefer FLASH format → librarian quiet-hours logic →
   `#flash-alerts`).

**Gate:** both artifacts exist, both posted to their respective
channels, both Splunk-logged. Briefs read like real briefs (Session 8
proved a quiet-window brief looks right; Session 9 proves a
real-content brief looks right).

## Pre-Session 9 checklist

### 1. (Optional but recommended) Add APT34 to `_roster.yaml`

Surfaced by Session 8 grader. APT34 is an Iranian actor with
documented A&D targeting — high probability real OSINT picks up a
mention of it. Without a roster entry, Session 8-style "actor not in
roster" warnings will fire on every related finding.

Two options:
- Run `/new-actor APT34` and let `actor-profiler` build the dossier
  (5-10 min, ~30k tokens, produces threat-box scoring)
- Manual stub entry in `_roster.yaml` (faster, but defers the
  full dossier until later)

**Lean:** `/new-actor` if the token budget allows. Cleaner, durable.

### 2. Decide the merge strategy for the 9 sprint commits

Branch `claude/vigilant-taussig-991156` is now 9 commits ahead of
`origin/main`. Options:

- **A. Merge to main before Session 9 starts.** Production schedule
  in Session 10 will run from main, so the sprint work needs to be
  there eventually. Doing it now means Session 9 runs from a clean
  main checkout — also resolves the briefer-worktree-path-bug
  question (no worktree, no bug).
- **B. Keep on the worktree branch through Session 9.** Defer merge
  to Session 10's start. Pros: Session 9 work continues to land on
  the same branch; if anything breaks, the worktree is the rollback
  unit. Cons: production schedule + Session 9's real briefs land on
  a non-main branch.

**Lean: A (merge first).** Reasoning: Session 10's first action is
"enable production schedule" — that runs from main. The longer the
sprint work stays unmerged, the more interface drift can accumulate
between worktree and main. Merging now also tests whether the
briefer-worktree-path-bug from Session 8 was actually
worktree-specific.

### 3. Confirm OSINT API quotas before real collection

Real collection burns paid quota. Pre-session check:

- **VT free tier:** 4 req/min, 500 req/day. A morning-brief
  collection might use 10-30 VT lookups. Comfortable margin.
- **Shodan dev plan:** 100 query credits. Empirically `lookup_host`
  doesn't deduct (per CLAUDE.md Operational Notes), but `search_hosts`
  does. Stay under 10 search calls per session.
- **Splunk:** local, no quota concern.

If quotas are tight, constrain collector via prompt: "Limit external
MCP calls to 5 VT lookups + 3 Shodan searches max. Prefer Splunk
first-party data and free RSS/web sources."

### 4. Plant a FLASH trigger seed

FLASH triggers depend on real-world conditions per
`infrastructure/flash-policy.yaml`. Two ways to test the FLASH
pipeline:

- **Real trigger:** wait for one. Unpredictable. Bad for sprint
  deadline.
- **Synthetic trigger:** plant a raw-signal item that genuinely
  matches a documented FLASH trigger. Mark `test: true` so the
  morning-brief path skips it, but **do NOT include the test-fixture
  exclusion clause in the FLASH phase prompt for this run only**.

**Lean:** synthetic trigger, FLASH phase prompt temporarily
de-clauses the exclusion. After the test, restore the production
prompt with the exclusion clause.

A good FLASH-trigger seed candidate: a fictitious critical CVE in a
watchlist company's product, with confirmed exploitation language
(e.g., "active exploitation observed by [grade-A source]"). Matches
the `cvss_critical_with_active_exploit` trigger pattern.

### 5. Confirm token budget for Session 9

- Pre-session checklist (`/new-actor`, audits): ~50k tokens
- Real morning brief end-to-end: ~150-250k tokens (more than
  Session 8 because real findings are larger and more numerous)
- FLASH end-to-end: ~80-120k tokens (narrower scope)
- Debugging buffer: ~100k tokens

**Total: ~400-500k tokens.** Same range as Session 8.

## Open design questions

### Q1: Constrain the collector's scope, or let it run wide?

A real morning brief collection sweep can fetch from ~30 sources per
`source-grades.yaml`. That's slow and expensive on the first
attempt.

Options:
- Constrain: prompt the orchestrator to "limit collection to A-grade
  sources only for this run (CISA, Mandiant, NVD, MSTIC, CrowdStrike).
  Skip B/C-grade and Twitter/YouTube/RSS for the first real run."
- Let it run wide: full source-grades.yaml sweep. May produce 30+
  raw-signal files. Briefer may receive 5-10 findings.

**Lean: constrain on first attempt.** If the constrained run produces
a clean brief, expand on the second run. If the wide run produces
chaos, debugging it is harder than starting narrow and widening.

### Q2: How aggressive should grader's promotion be?

The grader applies the credibility checklist + admiralty-grading.
Some real-world A-grade source items will be borderline-promotable
("Possibly True" credibility on a single A-source). The grader's
default behavior is documented in INTEL-GRADING.md.

No prompt change recommended. Trust doctrine. **But** observe whether
the grader is too permissive (briefs full of speculation) or too
restrictive (briefs that miss real signal).

### Q3: FLASH brief — quiet-hours behavior on Wednesday afternoon

If we test FLASH at 13:00-15:00 EDT on Wednesday, that's inside
active hours (9am-9pm EDT per FLASH-POLICY). The brief should post
immediately, not queue. Worth confirming the orchestrator picks the
right path.

If we want to test the queue path, run it after 21:00 EDT or before
09:00 EDT. The queue itself stays in
`infrastructure/flash-queue.yaml` — easy to verify.

**Lean:** test active-hours behavior in Session 9, defer queue-drain
testing to Session 10.

## Recommended Session 9 staging plan

Session 8 already validated the staged subagent pattern. Session 9
can go straight to integration runs. Two attempts per code path,
stop-after-2 budget guardrail.

### Stage 1 — Real morning brief

```
.\scripts\run_phase.ps1 -Phase morning-brief
```

(Optionally with a constrained-collection clause appended via a
one-off wrapper-prompt edit, if Q1 lean is "constrain.")

**Gate:** real brief in `threats/briefs/2026-05-NN-morning.md` with
`test: false`, posted to `#intel-briefs`, Splunk paired events.

### Stage 2 — FLASH alert sweep

Plant the synthetic FLASH trigger first. Then, with the test-fixture
exclusion **temporarily lifted** for the FLASH phase only:

```
.\scripts\run_phase.ps1 -Phase alert-sweep-noon
```

**Gate:** FLASH brief in `threats/briefs/flash-2026-05-NN-HHMM.md`,
posted to `#flash-alerts` (NOT `#intel-briefs`), Splunk paired events
with FLASH-specific event type.

After the test, restore the test-fixture exclusion clause to the
FLASH phase prompts.

## Risk flags for Session 9

1. **Real data may surface subagent quirks the synthetic seeds
   didn't.** Hard Rule 2 (no originated attribution) gets a real
   stress test when the grader sees actual Mandiant or CrowdStrike
   attribution language. Watch for the briefer rewriting source
   claims as Archimedes claims.

2. **Real OSINT may surface IOCs that need extracting.** Session 8
   had `iocs_count: 0` everywhere. Session 9 will trigger the
   `ioc-extraction` skill at scale. The skill is well-tested in
   isolation but not at production scale.

3. **A real bad brief gets seen.** Discord posts go to
   `#intel-briefs` — production channel. If the briefer produces
   something off, you see it. Worth pre-flighting the first brief
   manually before the librarian posts (or accept that "first real
   brief might be cosmetically rough").

4. **Briefer worktree path bug may or may not reproduce.** If you
   merged to main first (Q2 option A), this is moot. If still on the
   worktree, expect the orchestrator to recover the same way Stage G
   did in Session 8.

5. **FLASH pipeline is unverified end-to-end.** Different code path,
   different format, different channel. Could surface its own bugs.
   Stop-after-2 guardrail applies.

6. **Token budget exhaustion if collection goes wide.** Constrain
   collector on first attempt (per Q1 lean) to avoid burning the
   budget before reaching the brief.

## Verification gates

In order. Don't skip ahead.

1. APT34 in roster (or stub) — only if you went with that option.
2. Sprint commits merged to main — only if you went with Q2 option A.
3. OSINT quota check — `query_credits` on Shodan, daily-quota on VT.
4. Stage 1 attempt 1: real morning brief end-to-end.
5. (If Stage 1 attempt 1 failed) Stage 1 attempt 2: with one
   targeted fix.
6. Stage 2 attempt 1: FLASH end-to-end.
7. (If Stage 2 attempt 1 failed) Stage 2 attempt 2: with one
   targeted fix.
8. Verify the FLASH-test fixture cleanup (deleted, exclusion clause
   restored).

## Time budget estimate

- Pre-session checklist: 30 min
- Stage 1 (real morning brief, with debugging): 60-90 min
- Stage 2 (FLASH end-to-end): 60-90 min
- Cleanup + commit + handoff write: 30 min

**Total: ~3-3.5 hours.** Smaller than Session 8 because the pipeline
is already validated.

## What gets cut from Session 9 if scope slips

- `/new-actor` for APT34 — defer to post-launch
- Briefer worktree path investigation — only if it actually
  reproduces in main; otherwise documented and forgotten
- Wide-source collection variant — first run constrained is enough
  to validate; widening can happen after launch
- Quiet-hours queue test — defer to Session 10

## What does NOT get cut

- Stage 1 (real morning brief). This is the central deliverable for
  the sprint's "up and running by Friday" goal.
- Test-fixture exclusion clause restoration after Stage 2. Forgetting
  this means Monday's production morning brief misses real signal it
  shouldn't miss.
- Splunk-paired-events verification — the dead-man's-switch in
  Session 10 depends on the started/completed event pattern being
  reliable.

## Pre-session memory write (for future-me)

When Session 9 starts cold, the first thing to do is read this file
plus `docs/handoffs/session-8.md` (for what the pipeline already
proved) and `docs/handoffs/session-7-prep.md` (for the headless
patterns). Then run the pre-session checklist BEFORE any pipeline
invocation. The merge decision (Q2) is the most consequential — it
shapes which directory subsequent commands run from.

If Stage 1 attempt 1 produces a clearly-wrong brief (e.g.,
hallucinated content, originated attribution, banned phrases), DO NOT
let the librarian post it. Halt manually, surface to Ryan.

---

*Drafted at end of Session 8 (2026-05-03). Targeted for Session 9
start (Mon 2026-05-04). Pulled in 3 days from the original Wed
2026-05-06 target. Sessions 9 and 10 will run same-day, collapsing
the original sprint plan from 5 sessions over 5 days into Sessions
9+10 in one sitting — production schedule enables Monday EOD,
first unattended brief fires Tue 2026-05-05 at 08:00 EDT (3 days
ahead of the original Friday 2026-05-08 launch). Build in a
mid-day pause between the two sessions to verify Session 9 stuck
before turning on the schedule. See `docs/handoffs/session-10-prep.md`
for the immediate follow-on plan.*
