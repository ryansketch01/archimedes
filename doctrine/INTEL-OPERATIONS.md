# INTEL-OPERATIONS.md — Operational Runbook

> **Archimedes doctrine — operations.**
> The procedural companion to the grading and brief standards. This is how Archimedes actually runs day-to-day.

---

## Daily Schedule

| Time (EDT) | Event | Output channel |
|---|---|---|
| 00:00 | Alert sweep | FLASH if triggered (queued outside 9am–9pm) |
| 06:00 | Alert sweep | FLASH if triggered (queued) |
| 07:30 | Pre-brief collection | raw-signal to disk |
| **08:00** | **Morning Brief** | Discord `#intel-briefs` |
| 12:00 | Alert sweep | FLASH if triggered |
| 15:30 | Pre-brief collection | raw-signal to disk |
| **16:00** | **Afternoon Brief** | Discord `#intel-briefs` |
| 18:00 | Alert sweep | FLASH if triggered |

## Weekly Schedule

| Day | Time | Event | Output |
|---|---|---|---|
| Wednesday | 10:30 | Threat Detection Weekly | Discord `#intel-briefs` |
| Friday | 12:00 | Threat Actor Summary | Discord `#intel-briefs` |
| Sunday | 10:00 | Weekly Synthesis | Discord `#intel-briefs` |

---

## Pipeline — Scheduled Brief

Canonical flow for Morning and Afternoon briefs.

### Phase 1 — Pre-brief collection (30 min before brief)

**Driver:** systemd timer fires `claude -p "Run pre-brief collection" --output-format stream-json`

**Subagent:** `collector`

**Inputs:**
- `infrastructure/source-grades.yaml` (active sources)
- `infrastructure/source-health.yaml` (skip stale sources)
- `infrastructure/watchlists/*.yaml` (filters)

**Process:**
1. Query each source MCP for items matching watchlist tags
2. Filter for time window (last 14h for morning, last 8h for afternoon)
3. Write each item as `threats/raw-signal/raw-YYYY-MM-DD-{id}.md` with minimal frontmatter
4. Update `source-health.yaml` for any timeouts/errors

**Output:** Raw signal files on disk. No grading performed yet.

### Phase 2 — Grading (at brief time)

**Driver:** systemd timer fires `claude -p "Generate morning brief" --output-format stream-json`

**Subagent:** `grader`

**Inputs:**
- All un-promoted raw-signal from last 24h
- `doctrine/INTEL-GRADING.md`
- `threats/threat-actors/_roster.yaml` (actor attribution lookup)

**Process:**
1. Cluster raw signal by topic/actor/vuln
2. For each cluster:
   - Apply credibility checklist
   - Run independent corroboration analysis
   - Decide promote vs. reject
3. Promoted clusters → write `threats/findings/finding-YYYY-MM-DD-{id}.md`
4. Rejected clusters → log to `threats/findings/_rejection-log.yaml`

**Output:** Graded findings with full frontmatter, including `inclusion.eligible_for`.

### Phase 3 — Red-team review (conditional)

**Subagent:** `red-team-analyst`

**Condition:** Only runs on findings with WEP ≥ "very likely"

**Process:**
1. Read each HIGH-confidence finding
2. Construct the strongest counterargument
3. Either flag weakness (downgrade required) or approve (sign-off)
4. Update finding's `red_team_review` field

### Phase 4 — Brief composition

**Subagent:** `briefer`

**Inputs:**
- Approved findings where `inclusion.eligible_for` contains the brief type
- `threats/briefs/_coverage-log.yaml` (anti-repetition)
- `infrastructure/watch-config.yaml` (standing sections)
- `doctrine/INTEL-BRIEF-STANDARDS.md`

**Process:**
1. Draft brief per structure
2. Run pre-flight checklist
3. Regenerate any failing sections
4. Write `threats/briefs/YYYY-MM-DD-{type}.md`
5. Update `_coverage-log.yaml`

### Phase 5 — Delivery & commit

**Subagent:** `librarian`

**Process:**
1. Invoke `.claude/hooks/discord-post.sh` with brief file
2. Invoke `.claude/hooks/splunk-log.sh` with brief metadata
3. Commit all changes: `git add . && git commit -m "<type> brief YYYY-MM-DD" && git push`
4. Regenerate `threats/iocs/_master-index.yaml` if new IOCs were added

---

## Pipeline — FLASH Alert

Lighter pipeline for async triggers.

**Driver:** systemd timer fires every 6 hours (00/06/12/18 EDT)

**Flow:**

```
1. collector runs narrow FLASH-trigger check
   → returns candidates or empty

2. If empty:
   → log "flash_sweep_clean" to Splunk
   → exit

3. If candidates:
   → grader applies fast-path single-item grading
   → red-team-analyst if HIGH confidence
   → briefer produces FLASH format per doctrine

4. Quiet hours check (FLASH-POLICY.md):
   → if inside 09:00–21:00 EDT → post to Discord #flash-alerts
   → if outside → queue to infrastructure/flash-queue.yaml
   → if critical override conditions → bypass quiet hours, post immediately

5. librarian commits, logs, updates indices
```

---

## Watchlists

### A&D Vendor Watchlist

Structured file: `infrastructure/watchlists/aerospace-defense.yaml`. Contains company names, tickers, aliases, subsidiaries, and domains. The collector uses this as a filter during pre-brief collection — any raw signal mentioning a watchlist entity gets higher priority.

### Tracked Actors

Structured file: `threats/threat-actors/_roster.yaml`. 22 actors at v1. The collector checks raw signal for actor aliases and tags findings accordingly.

### Tracked Vulnerabilities

Structured file: `threats/vulnerabilities/_index.yaml`. Active zero-days and critical CVEs under ongoing tracking.

---

## Failure Handling

### Scheduled Brief Failure

- **Retry:** 3 times with exponential backoff (1min, 5min, 15min)
- **On final failure:**
  - Post to Discord: "⚠️ [Brief type] failed to generate at [time]. Investigating."
  - Log to Splunk: `run_id`, `error`, `partial_state`
  - Preserve collected signal (do not lose the raw collection)
  - Attempt degraded brief: ship what we have with clear caveat

### Alert Sweep Failure

- **Retry:** 1 time after 10 min
- **On final failure:**
  - Silent: log to Splunk, do not post to Discord
  - Rationale: noisy failures are worse than missed sweeps

### Source API Failure

- Mark source `stale` in `source-health.yaml` after 2 consecutive failures
- Exclude from grading while stale
- Auto-recover on next successful fetch
- Log grade impact (findings dependent on stale sources get flagged)

### Subagent Context Overflow

- If a subagent exceeds its context budget, the orchestrator:
  - Logs the overflow event
  - Retries with a narrower scope (e.g., shorter time window)
  - Escalates to human if retry also fails

---

## Source Management

### Source Grades

Pre-assigned in `infrastructure/source-grades.yaml`. Derived from `doctrine/INTEL-GRADING.md`. The grader reads this file for every finding.

### Source Health

Runtime state in `infrastructure/source-health.yaml` (gitignored). Tracks last-successful-fetch, failure count, current status. Updated by collector after each run.

### Source Grade Revisions

Manual or agent-proposed grade changes logged to `infrastructure/source-grade-log.md`. See `doctrine/INTEL-GRADING.md` for rules.

---

## Actor Profile Maintenance

### Review Cadence

Every actor profile carries `last_reviewed` and `next_review_due` in frontmatter. The `actor-profiler` subagent runs a weekly task:

1. Find the actor with the oldest `next_review_due`
2. Run a fresh collection pass focused on that actor
3. Update profile with new intel, TTPs, IOCs
4. Re-attest `last_reviewed` and push `next_review_due` forward 90 days
5. If HIGH threat level changes proposed, post to `#actor-review` for human sign-off

### New Actor Intake

Use the `/new-actor <name>` slash command. Triggers the full `actor-profiler` workflow per `doctrine/ACTOR-PROFILE-STANDARD.md`.

---

## Splunk Integration

### Write Path (HEC)

Events shipped to Splunk `archimedes` index:

| Event type | When |
|---|---|
| `brief_published` | Every scheduled or FLASH brief |
| `finding_promoted` | Every raw signal promoted to finding |
| `finding_rejected` | Every cluster the grader declined |
| `ioc_added` | Every new IOC added to any actor |
| `source_health_change` | Source went stale/recovered |
| `grade_revision` | Source grade changed |
| `run_start` / `run_complete` / `run_failed` | Operational telemetry |
| `command_executed` | Every slash command |
| `policy_violation` | Any hard-rule violation attempt |

Shipped via `.claude/hooks/splunk-log.sh` using HEC token from `.env`.

### Read Path (REST API via MCP)

The collector and `ioc-hunt` subagents query Splunk via a custom MCP server (Session 3). Indexes queried:

- `archimedes` — the agent's own event stream
- `defenseclaw_local` — first-party telemetry from DefenseClaw

First-party hits carry A-grade source reliability and unlock the `very likely` WEP threshold per `doctrine/INTEL-GRADING.md` single-source veto exception.

---

## Infrastructure

| Component | Host | Port | Purpose |
|---|---|---|---|
| Archimedes (Claude Code) | Your PC | — | Orchestrator, subagents |
| Splunk Free | Your PC | 8000/8088/8089 | Telemetry sink + queryable store |
| DefenseClaw | Your PC | — | First-party telemetry source (feeds Splunk) |
| Discord bot | Your PC | — | Delivery interface |
| Flask dashboard | Your PC | 5000 | Browse interface |
| Git repo | Your PC + GitHub | — | Version-controlled intel corpus |

**Security note:** Splunk Free has no authentication — exposed only to localhost. Never bind to 0.0.0.0.

---

## Git Discipline

- Every brief run commits to `main` with a descriptive message
- Raw signal lives on `wip/pre-brief-{type}` branches until promotion
- Rejected clusters stay in `_rejection-log.yaml` for audit trail (do not delete)
- Generated indices (`_master-index.yaml`) regenerate on each run — do not hand-edit
- `.env`, `quarantine/`, and runtime state files are gitignored — never commit

---

## Run Identifiers

Every run gets a `run_id` of the form `{type}-YYYYMMDD-HHMMSS` used across Splunk events, commit messages, and log lines for traceability.

---

*Last reviewed: Session 1 scaffold*
