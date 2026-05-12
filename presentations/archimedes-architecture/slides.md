# Archimedes Architecture Walkthrough · slide-by-slide spec

> Drop-into-your-own-template version of `archimedes-architecture.pptx`. Same 32-slide outline, same speaker notes. For senior engineer / architect audiences — Claude-familiar, intent is rebuild-from-scratch.
>
> **Engineering handoff framing.** Real file paths. Real code. Real subagent inventory. Less storytelling than the other two decks.

**Total: 32 slides · ~45 min · ~85s per slide**

---

## Slide 1 — Title

**Layout:** Centered hero. No banner.

**Title:** Archimedes
**Subtitle:** Architecture Walkthrough — How to Rebuild It
**Byline:** [Presenter name] · [Date] · For: senior engineers / architects familiar with Claude + MCP

**Speaker notes:**
Engineering-handoff framing — not marketing, not discovery. This deck is structured so that after 45 minutes the audience could start building their own Archimedes-shaped system. Open with: "I'll spend roughly 45 minutes walking through the architecture. The intent is that you leave knowing what to build, in what order, with what invariants must hold. Stop me with questions; I'll dwell on whatever isn't landing." Reference the other two decks if context helps — overview was problem-driven, Athena was forward-looking proposal. This is the engineering-deep-dive.

---

## §0 — Mental model

## Slide 2 — The whole system in one picture

**Subtitle:** Four layers. Doctrine cuts across all four.

**Layout:** 5 stacked rounded boxes top-to-bottom, plus an orange "DOCTRINE" ribbon running down the left margin spanning all 5.

| # | Layer | Body |
|---|---|---|
| 1 | **HUMAN OPERATOR** (red) | Approves HIGH scoring · names new actors · ratifies sources · reviews retractions |
| 2 | **ORCHESTRATOR (Claude Code)** (dark blue) | Schedules · delegates · holds the run state across subagent invocations |
| 3 | **9 SUBAGENTS — each with own context, write scope, doctrine** (blue) | collector · grader · analyst · red-team-analyst · actor-profiler · vuln-tracker · briefer · librarian + delegate-only orchestrator |
| 4 | **MCP WRAPPERS + HOOKS — the tool interface** (blue) | Splunk · VirusTotal · Shodan · Censys · urlscan · theHarvester · SpiderFoot · RSS / discord-post.sh · splunk-log.sh |
| 5 | **EXTERNAL — sources of truth and side effects** (green) | OSINT feeds · Splunk indexes · git · Discord · Task Scheduler |

**Speaker notes:**
This is the map. Spend a full minute on it. Five layers, top to bottom: human operator (approves the high-stakes calls), orchestrator (Claude Code instance that delegates), subagents (9 specialized roles with isolated contexts), tools (MCPs + hooks), external (where the data lives and where side effects land). Doctrine is the orange ribbon down the left — it cuts across all five layers because every layer reads from it. Reference this slide throughout the rest of the deck when introducing each layer's details.

---

## Slide 3 — Five load-bearing invariants

**Subtitle:** If your rebuild preserves these five, the rest is implementation detail.

**Bullets:**

1. **Doctrine as code** — Every behavior the agent exhibits traces back to a versioned .md file. No prompts hidden in subagent code; no logic that contradicts the doctrine files. If you can't grep for the rule in `doctrine/`, the rule doesn't exist.
2. **Subagent context isolation** — Each subagent gets the minimum context to do its job. Orchestrator never reads raw articles. Briefer never sees the coverage log. Red-team never wrote the primary finding. Lower error rate by construction.
3. **Librarian-only side effects** — Only the librarian writes to git, Splunk, or Discord. Other subagents can write to disk inside their scope but the externalization happens in one place — easy to audit, easy to LEGAL-POLICY-scan, easy to rate-limit.
4. **Human approval gates on high-stakes calls** — HIGH threat-box scoring → `/approve-scoring`. New actor → `/new-actor`. Source-grade ratification → human review. The agent proposes; the human approves on anything with reputational consequences.
5. **Audit trail is additive, never silent** — Retractions append to the original, never overwrite. Source-grade downgrades log to `source-grade-log.md`. Every policy refusal logs to `policy-violations.yaml`. Git history + Splunk events + Discord posts together reconstruct any action.

**Speaker notes:**
These are the five things that, if preserved, the rebuild will still be Archimedes-shaped — even if you use Python where I used Bash, or OpenCTI where I used markdown, or Teams where I used Discord. If you break any of these in the rebuild, you've built something different. Worth showing the audience this slide twice — once now (so they have the frame) and once at the rebuild-guide section (so they remember which lines not to cross).

---

## Slide 4 — On-disk layout

**Subtitle:** What lives where. Real directory tree, abbreviated.

**Layout:** Full-width monospace block (light gray background), ~38 lines.

```
archimedes/
├── doctrine/                       6 .md files — agent's working memory
│   ├── LEGAL-POLICY.md             prohibited queries, ITAR boundary, copyright
│   ├── INTEL-GRADING.md            Admiralty 6×6, WEP, single-source-veto
│   ├── INTEL-BRIEF-STANDARDS.md    Layer 1/Layer 2 spec, preflight checklist
│   ├── THREAT-BOX-METHODOLOGY.md   per-category scoring, evidence-min tables
│   ├── RETRACTION-POLICY.md        additive retractions, 72h auto-downgrade
│   └── FLASH-POLICY.md             7 triggers, quiet hours, critical override
│
├── .claude/
│   ├── agents/                     9 subagent definition .md files
│   ├── skills/                     reusable skill bundles (smart-brevity, ach, kac…)
│   ├── commands/                   slash-command definitions
│   └── hooks/                      bash scripts for deterministic side effects
│       ├── discord-post.sh         POST to Discord via webhook
│       └── splunk-log.sh           HEC ingest to Splunk
│
├── mcps/                           8 MCP wrappers — uv workspace members
│   ├── splunk-query/  virustotal/  shodan-mcp/  rss-bridge/
│   ├── urlscan/  censys/  theharvester/  spiderfoot/
│
├── threats/                        the corpus — agent writes; humans review
│   ├── raw-signal/                 collector output (un-promoted)
│   ├── findings/                   grader output (promoted, graded)
│   ├── briefs/                     briefer output (Layer 1 + Layer 2)
│   ├── threat-actors/<actor>/      per-actor dossier
│   ├── vulnerabilities/<cve>/      per-CVE tracking
│   └── iocs/_master-index.yaml     regenerated indexes
│
├── infrastructure/                 agent-readable YAML config
│   ├── source-grades.yaml          which sources, which grades, which categories
│   ├── source-health.yaml          runtime health state (gitignored)
│   ├── watch-config.yaml           standing brief sections + watchlists
│   ├── authorized-targets.yaml     Hard Rule 4 — only these may be actively scanned
│   └── scheduler/                  Windows Task Scheduler XML templates
│
├── scripts/                        Python helpers (not subagents)
│   ├── run_phase.ps1               wrapper for scheduled brief invocation
│   ├── splunk_log.py               HEC log helper
│   ├── regenerate_ioc_index.py     index regen
│   └── discord_listener.py         inbound /command bridge
│
├── docs/handoffs/                  session retrospectives (session-N.md)
├── pyproject.toml                  root project + uv workspace declaration
├── uv.lock                         locked dependency graph
└── CLAUDE.md                       agent charter + operational notes log
```

**Speaker notes:**
Walk through top-to-bottom. Three things to emphasize: (1) doctrine/ at the top — these six files are the agent's working memory; the rebuild starts here. (2) .claude/ contains everything the agent runtime needs — agents, skills, commands, hooks; the equivalent in your stack might be different (Claude Code uses this layout, other Claude runtimes have their own). (3) threats/ is the corpus — the agent's output lives here, versioned in git. This is what makes the system auditable: every brief, every finding, every dossier, every retraction is a markdown file in git history.

---

## §1 — Doctrine layer

## Slide 5 — The six doctrine files

**Subtitle:** The agent's working memory. Versioned in git. Reviewable by analysts and engineers.

**Layout:** 4-column table.

| Doctrine file | Governs | Read by | When |
|---|---|---|---|
| **LEGAL-POLICY.md** | prohibited queries · authorized targets · ITAR · copyright | every subagent (before any tool call) | session start + on update |
| **INTEL-GRADING.md** | Admiralty 6×6 · WEP · single-source-veto · corroboration | grader | on every finding promotion |
| **INTEL-BRIEF-STANDARDS.md** | Layer 1/Layer 2 · preflight checklist · word/char budgets | briefer | on every brief compose |
| **THREAT-BOX-METHODOLOGY.md** | per-category composite scoring · evidence-min tables | actor-profiler | on every `/update-tracking` |
| **RETRACTION-POLICY.md** | when to retract vs correct · additive · 72h auto-downgrade | grader + librarian | on retraction trigger |
| **FLASH-POLICY.md** | 7 triggers · quiet hours · critical override · 72h clock | collector + grader | on every FLASH sweep |

**Speaker notes:**
Six files. Each one governs a slice of the agent's behavior. The "Read by" column maps doctrine to subagent — the librarian doesn't read THREAT-BOX-METHODOLOGY because it doesn't score actors; the grader doesn't read INTEL-BRIEF-STANDARDS because it doesn't compose briefs. Minimal-required-context, applied even to doctrine. This pattern is load-bearing — without it, every subagent loads every doctrine file and the context bloat costs accuracy and latency.

---

## Slide 6 — Anatomy of a doctrine file

**Subtitle:** Real excerpt from `doctrine/INTEL-GRADING.md`

**Layout:** Full-width markdown code block.

```markdown
# INTEL-GRADING.md — Intelligence Source Grading System

> **Archimedes doctrine — grading.**
> This file is authoritative. Every finding's digraph must be
> justifiable against this document.

---

## Source Reliability (A–F)

| Grade | Label                | Description                                  |
|-------|----------------------|----------------------------------------------|
| A     | Completely Reliable  | Consistent, verified track record.           |
| B     | Usually Reliable     | Strong track record, minor inaccuracies.    |
| C     | Fairly Reliable      | Right before, but enough errors for caution. |
| D     | Not Usually Reliable | More misses than hits. Lead, not finding.   |
| E     | Unreliable           | History of false/misleading information.    |
| F     | Cannot Be Judged     | New, unknown, no track record yet.          |

## Credibility Assessment Checklist (authoritative)

### 1 — Confirmed — ALL of:
  - Multiple independent A/B-grade sources
  - No public contradictions in 24h corroboration window
  - First-party Splunk telemetry if applicable

### 2 — Probably True — ALL of:
  - One A-grade source
  - Plausibility test passes (consistent with known TTPs)
  - No active contradictions

### 3 — Possibly True — single source, cannot confirm or deny.

[...continues for 4, 5, 6...]
```

**Speaker notes:**
Three structural patterns to call out: (1) Authority statement at the top — "this file is authoritative." The grader subagent is instructed to defer to this file over its own judgment. (2) Lookup tables — Admiralty grades, WEP probability bands, evidence-minimum tables for threat-box. The agent uses these like a dev uses a switch statement. (3) Checklist-style rules — "ALL of these conditions must hold" or "ANY of these triggers" — written as if for human auditors, applied by the agent as decision logic. Doctrine files are plain English, but they read like code. That's intentional.

---

## Slide 7 — Hard Rules — the immutable refusal boundary

**Subtitle:** From CLAUDE.md. Agent refuses even when prompted to bypass. Logged to `policy-violations.yaml`.

**Bullets:**

1. **Legal policy is non-negotiable** — If LEGAL-POLICY prohibits it, refuse even if user insists. Log the attempt.
2. **Never originate attribution** — Agent only reports what other sources have attributed, citing them.
3. **No exploitation, ever** — No PoC code, payloads, exploit guides — not for testing, research, or "educational" purposes.
4. **Never scan third parties** — Active recon only against targets in `authorized-targets.yaml`. SpiderFoot + theHarvester MCPs enforce module-level allowlists.
5. **Human sign-off for HIGH threat levels** — When actor-profiler proposes HIGH, posts to `#actor-review` and waits for `/approve-scoring`. Does not auto-commit.
6. **15-word quote limit, one quote per source** — Copyright compliance. Hard-enforced in preflight checklist.
7. **Credentials are radioactive** — If a query surfaces credentials, never store them. Count, report exposure, discard.
8. **Splunk first-party > external** — When first-party telemetry contradicts external sources, first-party wins. The external source gets graded down.

**Speaker notes:**
Hard Rules are the audit-defense layer. They're enforced at three levels: in doctrine prose (agent reads and respects), in subagent definitions (every subagent has "before any action — consult LEGAL-POLICY" as step 0), and in code at the MCP wrappers (allowlist + refusal before HTTP call). Three levels of defense in depth. Removing any one weakens the system. If a rebuild changes the Hard Rules list — e.g. adds rule 9, removes rule 7 — that's fine, but make sure the new list is enforced at all three levels.

---

## Slide 8 — Skills — reusable analytic procedures

**Subtitle:** `.claude/skills/<name>/` — invoked by subagents, share procedures across them.

**Bullets:**

- **smart-brevity/** — Brief composition rules. Banned phrases, active voice, lead-with-impact, preflight checklist. Invoked by briefer on every brief. Has `references/` subdirectory: banned-phrases.md, brief-templates.md, preflight-checklist.md.
- **admiralty-grading/** — Source reliability + credibility evaluation procedure. Invoked by grader on every finding promotion. Generates the digraph the grader writes to the finding's frontmatter.
- **sat-ach/** — Analysis of Competing Hypotheses — structured analytic technique. Builds an N×M matrix of hypotheses × evidence, ranks by inconsistency count. Invoked by analyst (primary) and red-team-analyst (contrarian).
- **sat-kac/** — Key Assumptions Check — surface load-bearing premises that the finding rests on. Invoked by analyst when a finding's WEP is "likely" or higher.
- **threat-box-scoring/** — Per-category composite scoring procedure with evidence-minimum table enforcement. Invoked by actor-profiler. Outputs the proposed threat-box.yaml; routes HIGH proposals to the `/approve-scoring` gate.
- **ioc-extraction/** — Pull indicators from finding body text — IPs, domains, hashes, CVEs, actor mentions, MITRE IDs. Invoked by collector.

**Speaker notes:**
Skills are like libraries — reusable procedures the subagents call. They live under `.claude/skills/<name>/`. Each has a SKILL.md (the main procedure) and usually a references/ subdirectory with lookup tables or templates. Pattern: when two subagents need the same procedure, factor it into a skill. The grader and the analyst both need ACH; sat-ach is the skill they both call. For a rebuild: skills aren't strictly necessary — you could inline the procedures into each subagent — but they pay off as soon as you have any procedure shared across multiple roles.

---

## §2 — Subagents

## Slide 9 — Subagent inventory

**Subtitle:** 9 subagents, each with isolated context, write scope, doctrine read, tool set.

**Layout:** 5-column table.

| Subagent | Role | Write scope | Doctrine read | Tools |
|---|---|---|---|---|
| **collector** | raw OSINT collection + watchlist filter | `threats/raw-signal/` | FLASH-POLICY, LEGAL-POLICY | WebFetch, WebSearch, MCP tools |
| **grader** | promote raw → finding · apply Admiralty + WEP | `threats/findings/` | INTEL-GRADING, RETRACTION | Read, Write, Edit, Splunk |
| **analyst** | SAT / ACH / KAC structured analysis | findings (analysis sections) | INTEL-GRADING, SAT skills | Read, Write, Edit |
| **red-team-analyst** | challenge HIGH-confidence findings | findings (red_team section) | sat-ach (contrarian) | Read, Edit |
| **actor-profiler** | dossier maintenance + threat-box scoring | `threats/threat-actors/*/` | THREAT-BOX, ACTOR-STANDARD | Read, Write, Edit, Splunk |
| **vuln-tracker** | CVE tracking · KEV monitoring | `threats/vulnerabilities/*/` | NVD + KEV refs | Read, Write, WebFetch |
| **briefer** | compose all brief types · Layer 1 + Layer 2 | `threats/briefs/` | INTEL-BRIEF-STANDARDS | Read, Write, Edit |
| **librarian** | commit · post Discord · log Splunk · regen indices | git + Splunk + Discord + indices | RETRACTION-POLICY | Read, Bash, Edit |

**Speaker notes:**
Eight defined subagents + the orchestrator (which is a 9th, with no write scope of its own — it only delegates). Walk through them top to bottom; the table is dense but every column matters: Role is the elevator pitch. Write scope is what files/systems they're allowed to modify. Doctrine read is which .md files load into their context. Tools is the tool subset they're given (e.g. red-team-analyst only gets Read + Edit — can't write new files, only modify findings). The minimal tool surface per subagent is part of context isolation — fewer tools = simpler decision space = lower error rate.

---

## Slide 10 — Anatomy of a subagent definition

**Subtitle:** Real excerpt — `.claude/agents/briefer.md` (frontmatter + structure)

**Layout:** Full-width code block.

```markdown
---
name: briefer
description: Use to compose every Archimedes brief from graded findings.
  Invoke for scheduled morning brief (08:00 EDT), scheduled afternoon brief
  (16:00 EDT), async FLASH alerts ... Reads approved findings, the coverage
  log for anti-repetition, watch-config for standing sections, and doctrine.
  Invokes the smart-brevity skill always — drafts prose, runs the 13-item
  pre-flight checklist, regenerates failing sections until all pass.
  Writes only to threats/briefs/. Does not post to Discord (librarian's job),
  does not grade (grader's job), does not run SATs (analyst's job).
tools: Read, Write, Edit, Glob, Grep
model: opus
---

# Briefer Subagent

## Role
You are the briefer. You take the graded, analyzed, red-teamed findings
the other subagents produced and compose them into the documents Ryan
actually reads: six brief types plus retractions.

## Before any action — consult LEGAL-POLICY
- Hard Rule 6 (quote discipline) is your operational constraint
- ITAR/export-control check on every brief

## Procedure — scheduled brief (Morning or Afternoon)
1. Load inputs (findings, coverage log, watch-config)
2. Filter by digraph ≥ B2, by freshness window
3. Categorize into sections per INTEL-BRIEF-STANDARDS
4. Apply correlation callouts
5. Compose Layer 1 + Layer 2
6. Run 13-item preflight checklist (smart-brevity skill)
7. Write file, update _coverage-log.yaml, back-write findings
```

**Speaker notes:**
Three load-bearing parts of every subagent definition: (1) Frontmatter — name, description (this is the elevator pitch the orchestrator reads when deciding who to delegate to), tools (the minimum set), model (haiku for cheap, sonnet for medium, opus for complex). (2) Role + scope — written in second person ("you are the briefer") — Claude reads this as identity. Clear delineation of what this subagent does NOT do is as important as what it does. (3) Procedure — numbered steps. This is the agent's runbook. When the orchestrator delegates, the subagent reads its own definition and follows the procedure.

---

## Slide 11 — Context isolation — what each subagent sees vs. doesn't

**Subtitle:** The counterintuitive insight: less context per agent = lower error rate.

**Bullets:**

- **orchestrator** — schedule, delegation directives, pipeline state. Never reads raw articles. Never sees graded findings in detail.
- **collector** — source list, watchlists, time window. Never reads coverage log. Never sees prior briefs.
- **grader** — raw signal from current sweep, INTEL-GRADING, historical-source health. Never sees brief text.
- **analyst** — the finding it's analyzing + analytic framework references. Never sees other findings.
- **red-team-analyst** — ONE finding + the analyst's own analysis. Cannot have written the primary — contrarian by construction.
- **briefer** — approved findings + coverage log + watch-config + doctrine. Never reads raw signal.
- **librarian** — the file or files it's about to ship + the change summary. Never composes content.

**Footer (green callout, centered):**

Why this matters: agents hallucinate against context they don't need. Giving the briefer access to raw articles makes it tempted to re-grade. Giving the red-team the primary author's reasoning makes it harder to disagree. Minimum context = minimum surface for the wrong inference.

**Speaker notes:**
This is the most counterintuitive design choice in the system. The instinct is "give the model everything it might need." The opposite works better — minimal scope per agent, with the orchestrator handling cross-agent state. Show one concrete example: red-team-analyst. It's contrarian by construction because it didn't write the primary finding. If you gave it the same context the analyst had, it would naturally converge on the same conclusion (anchoring bias). By keeping the contexts separate, you create the conditions for genuine disagreement.

---

## Slide 12 — The grading chain — case study

**Subtitle:** One CVE-attribution claim traced through collector → grader → analyst → red-team

**Layout:** 5 stacked colored boxes (blue, dark blue, dark blue, red, green), each with a title and 2-3 sentences of body.

1. **collector** — Picks up Rapid7 blog post via RSS. Filters against watchlist (MuddyWater = tracked actor → KEEP). Writes `raw-signal/2026-05-06-1218-rapid7-muddywater.md` with minimal frontmatter. No grading.
2. **grader** — Reads the raw signal. Applies INTEL-GRADING: Rapid7 provisional A · single source → credibility 2 max. Single-source-veto caps forward claim at "likely." Promotes to `findings/finding-2026-05-06-FLASH-0002.md` with digraph A2, wep likely, corroboration.independent=false, 72h auto-downgrade clock set.
3. **analyst** — Reads ONLY this finding + sat-ach / sat-kac skills. Builds ACH matrix of attribution hypotheses (TeamPCP / MuddyWater / unattributed). Records analysis_sections.ach + .kac on the finding. Flags `red_team_review_required` because WEP=likely on single source — not "very likely" but close.
4. **red-team-analyst** — Receives just this finding + analyst's analysis. Argues FOR rejected hypotheses. Tests for confirmation bias. Either confirms the assessment (signs off) or flags weaknesses. Writes findings.red_team_review section.
5. **→ next: briefer** reads this finding (along with others promoted same window) and composes Layer 1 + Layer 2. Briefer never re-grades. Librarian never re-composes. Each subagent stays in its lane.

**Speaker notes:**
Trace one real finding through the chain. The MuddyWater / Rapid7 example actually happened — this is the FLASH-0002 finding referenced in CLAUDE.md's operational notes. Five stages, each with a different subagent, each with isolated context. The grader doesn't speculate beyond what INTEL-GRADING permits. The analyst doesn't grade. The red-team doesn't analyze — it challenges. Strict separation of concerns. Outcome: that finding's attribution leg eventually auto-downgraded to C3 (possibly true) when the 72h corroboration window closed unbroken. The discipline pays off.

---

## Slide 13 — The librarian — the only writer to side effects

**Subtitle:** LEGAL-POLICY content scan + git + Splunk + Discord, in that order, every time.

**Bullets:**

- **Why one writer** — Every external publication funnels through one agent — easy to audit, easy to rate-limit, easy to add a LEGAL-POLICY content-scan gate before anything leaves the building.
- **Mode-based procedure catalog (8 modes)** — Mode 1: post scheduled brief · Mode 2: post FLASH (with quiet-hours/critical-override logic) · Mode 3: process FLASH queue at 09:00 · Mode 4: actor-profiler commit · Mode 5: vuln-tracker commit · Mode 6: retraction · Mode 7: source-grade update · Mode 8: index regen.
- **Tools = Bash, Read, Edit, Glob, Grep** — Bash for hook invocation (`.claude/hooks/discord-post.sh`, `splunk-log.sh`, git commands). Read + Edit for the file(s) being shipped. **NO Write** — librarian doesn't author content.
- **Hook layer for deterministic side effects** — Discord posts go through `discord-post.sh`; Splunk events through `splunk-log.sh`. Bash scripts, not subagents — no LLM cost on every post, deterministic behavior, easy to debug.
- **LEGAL-POLICY content scan is the gate** — Every Discord post preceded by content scan: no credentials, no TLP:RED, no ITAR-questionable detail. If anything trips, halt and flag. The librarian is the last gate before content becomes public.
- **Wrapper catchup-push** — `scripts/run_phase.ps1` runs `git push origin main` at end of every phase. If librarian's push hung or skipped, wrapper catches up. Belt-and-suspenders against subagent variance.

**Speaker notes:**
The librarian is the system's most important subagent for safety. Concentrating all side effects in one place is a load-bearing pattern: it means there's exactly one piece of code (the librarian's LEGAL-POLICY scan step) that decides whether content goes public. Other subagents can write to disk (briefer to threats/briefs/, grader to threats/findings/), but nothing leaves the local filesystem without librarian's blessing. The mode catalog is just how we organize the librarian's procedures — could be one giant procedure, but the modes make the doctrine easier to reason about.

---

## Slide 14 — The orchestrator — what it does and never does

**Subtitle:** Claude Code session itself. Schedules. Delegates. Never analyzes or writes.

**Layout:** Two columns — DOES (green header) / NEVER DOES (red header).

### DOES

- Receive trigger (scheduled / FLASH / on-demand)
- Read pipeline doctrine (which subagents in what order)
- Delegate to subagents via Task tool
- Pass minimal context between subagent invocations
- Track run state across handoffs
- Surface high-stakes decisions to operator
- Handle pipeline failures (retry / degrade / abort)

### NEVER DOES

- Read raw articles (collector's job)
- Grade findings (grader's job)
- Compose brief content (briefer's job)
- Write to git, Splunk, or Discord (librarian's job)
- Make attribution claims (no one's job — Hard Rule 2)
- Approve HIGH scoring (operator's job — Hard Rule 5)
- Read `.env` or anything credential-bearing

**Speaker notes:**
The orchestrator is what you start with when you open Claude Code in this repo. It reads CLAUDE.md, knows the agent's identity, and waits for triggers. When a trigger fires (you typed `/brief morning`, or the scheduled task invoked `claude -p`), the orchestrator looks at the pipeline doctrine in CLAUDE.md and delegates. Two non-obvious things in the "never does" column: it never composes brief content (even if it knows what the brief should say) and it never makes attribution claims. Both of those would violate the role separation — and Hard Rule 2 specifically.

---

## §3 — MCPs + tool integration

## Slide 15 — MCP architecture

**Subtitle:** Model Context Protocol — stdio + JSON-RPC between Claude Code and tool servers.

**Bullets:**

- **MCP = Model Context Protocol** — Open spec from Anthropic. Defines stdio+JSON-RPC contract between an LLM runtime (Claude Code) and a tool server. Tools are discovered at runtime via `tools/list`; called via `tools/call`.
- **Each MCP is its own process** — Claude Code spawns the MCP server as a subprocess on session start. `.mcp.json` declares "this server is named X, run command Y in directory Z." Server lives as long as the Claude Code session.
- **FastMCP — our framework choice** — Python wrapper around the MCP spec. Decorator-style tool definition. Handles protocol plumbing; we write the tool functions.
- **Per-MCP isolated venv** — uv workspace member per MCP. Each has its own pyproject.toml + dependencies + tests. Why: dependency conflicts between MCPs (e.g. SpiderFoot wants CherryPy 18; theHarvester wants dnspython 2.3) — isolation prevents them.
- **Tools surface as `mcp__<server>__<tool>`** — From the agent's perspective: `mcp__shodan__lookup_host`, `mcp__virustotal__lookup_file`, `mcp__theharvester__enumerate`, `mcp__spiderfoot__passive_scan`. Namespace per server.

**Speaker notes:**
If your audience knows MCP, this is review. If they don't, this is foundational. Three things to land: (1) MCP is a protocol, not a library — your rebuild can use any MCP client/server library (Python, TypeScript, Rust). (2) Tool servers are subprocesses — keeps them isolated, lets you crash one without taking down the agent. (3) The naming convention `mcp__<server>__<tool>` is how the agent thinks about tool calls — every tool reference in this codebase uses that exact pattern.

---

## Slide 16 — Anatomy of an MCP wrapper

**Subtitle:** Real directory structure — `mcps/spiderfoot/`

**Layout:** Full-width directory tree.

```
mcps/spiderfoot/
├── pyproject.toml                  # spiderfoot-mcp; httpx + mcp[cli] + pydantic
├── README.md                       # public-facing doc — what tools, what auth
└── src/spiderfoot_mcp/
    ├── __init__.py                 # version + main() entry point
    ├── config.py                   # pydantic-settings; reads .env
    │                               # SPIDERFOOT_URL, _USERNAME, _PASSWORD,
    │                               # _SCAN_TIMEOUT_SECONDS, _POLL_INTERVAL_SECONDS
    ├── exceptions.py               # SpiderFootError + 6 subclasses
    │                               # SpiderFootConnectionError, AuthError,
    │                               # RequestError, PolicyError, ScanError,
    │                               # TimeoutError(scan_id)
    ├── models.py                   # pydantic models + PASSIVE_MODULE_ALLOWLIST
    │                               # the load-bearing safety primitive
    ├── policy.py                   # validate_modules() — refuse non-passive
    │                               # before any HTTP call
    ├── spiderfoot_client.py        # synchronous httpx client
    │                               # start_scan, get_scan_status, export_results,
    │                               # run_passive_scan (orchestrates poll loop)
    └── server.py                   # @mcp.tool() decorated entry points
                                    # passive_scan, list_modules, health

tests/
├── test_config.py                  # config-loader unit tests
├── test_policy.py                  # allowlist enforcement — 14 cases
└── test_client.py                  # respx-mocked HTTP behavior — 23 cases
```

**Speaker notes:**
Same 8-file structure for every MCP. Pattern stabilized after the third MCP — once you see it twice you can predict where everything lives. Three files are mandatory: `config.py` (env loading), `<name>_client.py` (the HTTP wrapper), `server.py` (the @mcp.tool() decorated endpoints). The other three (`exceptions.py`, `models.py`, `policy.py`) appear when the MCP has policy enforcement to do (like SpiderFoot's passive allowlist) or a complex domain model (like theHarvester's source list). Simpler MCPs (like rss-bridge) can skip `policy.py`.

---

## Slide 17 — The load-bearing safety primitive — `policy.py`

**Subtitle:** Real code from `mcps/spiderfoot/src/spiderfoot_mcp/` — Hard Rule 4 enforced before any HTTP call.

**Layout:** Full-width dark code block.

```python
# models.py — the allowlist + prohibited list (data)

PASSIVE_MODULE_ALLOWLIST: tuple[str, ...] = (
    "sfp_dnsresolve", "sfp_whois", "sfp_crt", "sfp_certspotter",
    "sfp_archiveorg", "sfp_threatfox", "sfp_virustotal",
    "sfp_bingsearch", "sfp_duckduckgo", "sfp_hibp_pastes",
    # ... 45 entries total
)

PROHIBITED_MODULES: tuple[str, ...] = (
    "sfp_tool_nmap",     "sfp_tool_nuclei",   "sfp_spider",
    "sfp_dnsbrute",      "sfp_screenshot",    "sfp_portscan_tcp",
    "sfp_bingsharedip",
)

# policy.py — the enforcement (logic)

def validate_modules(modules: list[str] | None) -> list[str]:
    """Refuse non-passive modules BEFORE any HTTP call. Hard Rule 4."""
    if not modules:
        return list(DEFAULT_MODULES)

    cleaned, rejected, prohibited_hits = [], [], []
    for raw in modules:
        stripped = raw.strip().removeprefix("module_")
        lower = stripped.lower()
        if lower not in _ALLOWLIST_LOWERCASE:
            if lower in (m.lower() for m in PROHIBITED_MODULES):
                prohibited_hits.append(stripped)
            else:
                rejected.append(stripped)
            continue
        cleaned.append(canonical_case(lower))

    if prohibited_hits or rejected:
        raise SpiderFootPolicyError(
            f"Module(s) refused: {prohibited_hits + rejected}. "
            "See LEGAL-POLICY.md SpiderFoot section."
        )
    return cleaned

# server.py — wired in BEFORE the HTTP call
@mcp.tool()
def passive_scan(target: str, modules: list[str] | None = None) -> dict:
    cleaned = validate_modules(modules)   # ← raises if non-passive
    return run_scan(target, cleaned)
```

**Speaker notes:**
This is the single most important code pattern in the system. Hard Rule 4 ("never scan third parties") is enforced as a function call BEFORE the HTTP request. The agent literally cannot make SpiderFoot scan an unauthorized target with an active module — the wrapper refuses with a PolicyError at the input boundary. The same pattern shows up in theharvester (PASSIVE_SOURCE_ALLOWLIST), in WebFetch (LEGAL-POLICY check on URLs), in WebSearch (prohibited query patterns). Rebuild lesson: encode your policy at the integration layer, not in prose-only doctrine. Doctrine tells the agent what to do; allowlists make it impossible to do otherwise.

---

## Slide 18 — MCP inventory

**Subtitle:** 8 wrappers — what each surfaces, auth model, policy enforcement.

| MCP | What it surfaces | Auth model | Policy enforcement |
|---|---|---|---|
| **splunk-query** | first-party telemetry · SPL search · health | Basic auth (REST 8089) | no allowlist · query rate limit |
| **virustotal** | domain / IP / file / URL reputation | API key header | rate-limit aware |
| **shodan-mcp** | host lookup · search_hosts · count · CDN | API key query param | no scan; index lookup only |
| **rss-bridge** | direct RSS/Atom feed fetch + ETag cache | none (public feeds) | feed list curated |
| **urlscan** | search · lookup · submit_scan | API-Key header | submit gated; search unmetered |
| **censys** | host search · cert search · host lookup | Basic (API_ID:API_SECRET) | v2 only; index lookup |
| **theharvester** | subdomain / host / IP enum via 45 sources | none + per-source keys | PASSIVE_SOURCE_ALLOWLIST |
| **spiderfoot** | passive_scan against self-hosted SF daemon | optional HTTP Basic | PASSIVE_MODULE_ALLOWLIST |

**Footer (italic, centered):**

Every MCP follows the same pattern: pydantic-settings config, httpx client, FastMCP server, respx-mocked unit tests, live-validation tests behind credentials. Two MCPs (theHarvester, SpiderFoot) carry explicit module-level allowlists because they wrap tools that could otherwise perform active recon.

**Speaker notes:**
Eight wrappers. Six just index-lookup or fetch passive data — those don't need allowlists, they need rate-limit and auth discipline. Two (theharvester, spiderfoot) wrap tools that CAN perform active recon — those carry mandatory allowlists at the wrapper level. Rebuild: start with the index-lookup wrappers (VT, Shodan, Censys, urlscan, RSS). Add the active-recon-capable ones (theHarvester, SpiderFoot) only when you've validated the allowlist pattern. Splunk-query is special — that's first-party, not OSINT, treated differently per Hard Rule 8.

---

## §4 — Pipelines

## Slide 19 — Scheduled brief pipeline

**Subtitle:** 08:00 morning, 16:00 afternoon. Five phases. ~25-40 min wall-clock end-to-end.

**Layout:** 5 horizontal rows. Left column = time (dark blue), right column = phase + body.

| Time (EDT) | Phase | Body |
|---|---|---|
| **07:30** | **pre-brief collection** | collector subagent · WebFetch + RSS + MCP tools · writes to `threats/raw-signal/` · returns count + source-health deltas |
| **~07:55** | **grading (clustering + Admiralty)** | grader subagent · reads all un-promoted raw signal · clusters by topic/actor/vuln · applies INTEL-GRADING · writes to `threats/findings/` |
| **~08:00** | **red-team review (conditional)** | red-team-analyst · ONLY if any finding has WEP ≥ very_likely · reads 1 finding at a time · writes red_team_review section |
| **~08:05** | **brief composition** | briefer · reads findings + coverage-log + watch-config · composes Layer 1 + Layer 2 · 13-item preflight · regenerates failed sections |
| **~08:08** | **ship** | librarian · LEGAL-POLICY scan · extract Layer 2 to temp file · `discord-post.sh #intel-briefs` · `splunk-log.sh brief_published` · git commit + push |

**Speaker notes:**
Five phases for a scheduled brief. The 07:30 phase is split out so the agent has time to collect signal before composing — collector runs ahead of brief, grader+briefer run on brief time. Red-team-analyst is conditional: only invoked if any finding has WEP ≥ very_likely. Most briefs don't hit that threshold (5 of 5 actor scorings did NOT escalate to red-team because Intent capped below the trigger). Wall-clock end-to-end is ~25-40 min. Failure handling per phase: collector retry → degrade with caveat; grader hard-fail → halt pipeline; red-team hard-fail → ship brief with red_team_review=NOT_PERFORMED flag; briefer fail → BRIEF GENERATION FAILED message to Discord; librarian fail → commit but no Discord post.

---

## Slide 20 — FLASH pipeline — async, faster

**Subtitle:** Every 6h. Same subagents, narrower scope. Quiet hours + critical override.

**Layout:** Three columns side by side. Each with a colored header band and a body block.

### 7 TRIGGERS (blue)

```
1.  Critical CVE actively exploited
2.  New attribution to a tracked actor
3.  Major breach in scope
4.  Tracked actor TTP change
5.  Sector-specific zero-day
6.  Zero-day with no patch
7.  Supply-chain compromise
```

### QUIET HOURS LOGIC (dark blue)

```
Active hours: 09:00 – 21:00 EDT

Inside active hours → POST
Outside + critical override → POST
Outside + no override → QUEUE

Critical override = ALL of:
  · CVSS 10
  · Confirmed active exploitation
  · Tracked actor named
  · A&D watchlist hit
```

### 72h AUTO-DOWNGRADE (red)

```
Single-source FLASHes ship with a
72h clock. If no independent A/B-grade
corroboration arrives within window:

  attribution leg drops A2 → C3
  campaign forensics hold
  retraction additive in coverage log

Live-tested 2026-05-09 on the
MuddyWater / Rapid7 FLASH-0002.
Fired clean.
```

**Speaker notes:**
FLASH is the answer to "what if something breaks between scheduled briefs?" Same subagent chain, but narrower scope: collector runs only against FLASH-eligible triggers, grader fast-paths single findings, red-team conditional, briefer composes FLASH format (shorter than scheduled brief), librarian posts to #flash-alerts. Quiet hours protect operators from being woken at 3 AM unless the threat genuinely warrants it. The critical-override threshold has fired exactly once in production — that's the calibration target. False FLASHes erode operator trust faster than missed FLASHes. 72h auto-downgrade is how we handle single-source attribution responsibly: ship the FLASH because it's load-bearing, but commit to retracting/downgrading if independent corroboration doesn't arrive.

---

## Slide 21 — On-demand commands — Discord bridge

**Subtitle:** `scripts/discord_listener.py` listens for slash commands; routes to orchestrator.

| Command | Purpose | Pipeline invoked |
|---|---|---|
| `/investigate <target>` | Deep dive on actor / domain / hash / CVE / campaign | collector → grader → analyst → briefer |
| `/ioc-hunt <indicator>` | Check IOC against repo + Splunk + external sources | collector → librarian (Splunk search) |
| `/cve <cve-id>` | Vuln research deep-dive against NVD + KEV + actors | vuln-tracker → briefer |
| `/new-actor <name>` | Scaffold new actor dossier from scratch | actor-profiler → librarian |
| `/update-tracking` | Refresh actor whose 90-day review is nearest due | actor-profiler → librarian |
| `/approve-scoring <id>` | Operator sign-off on a HIGH actor threat-box scoring | actor-profiler → librarian |
| `/brief <type>` | Manually trigger a scheduled-type brief | full scheduled-brief pipeline |
| `/flash` | Manually run a FLASH sweep | full FLASH pipeline |
| `/help` | List commands | discord_listener.py local |

**Footer (italic, gray box):**

`discord_listener.py` runs as a Windows Task Scheduler entry — polls Discord for messages from `DISCORD_OPERATOR_USER_ID` only · validates the slash command · spawns `claude -p` with the command + args as the prompt · streams the response back to the channel · logs the exchange.

**Speaker notes:**
On-demand is where the agent becomes interactive. Without the Discord listener, Archimedes is autonomous-only — runs on a schedule, can't be asked questions. The listener adds operator-in-the-loop. Security note: only DISCORD_OPERATOR_USER_ID can invoke commands. Messages from any other author are ignored. Single-operator design today; could extend to a team via roster YAML if multi-operator support is needed. Each slash command invokes a subset of the standard pipeline.

---

## Slide 22 — Layer 1 + Layer 2 — one file, two audiences

**Subtitle:** Briefer writes both sections in one .md file. Librarian extracts Layer 2 to post to Discord.

**Layout:** Full-width markdown code block (light gray).

```markdown
threats/briefs/2026-05-11-morning.md  (Layer 1 — the canonical record)

---
brief_id: 2026-05-11-morning
published_at: 2026-05-11T08:00:00-04:00
authored_by: archimedes-briefer
findings_referenced: [finding-2026-05-11-0001, finding-2026-05-11-0002]
word_count: 731
tlp: CLEAR
---

# Morning Brief — 2026-05-11

**[lead-with-impact sentence linked to source]**...
Per Hard Rule 2, the TeamPCP attribution to Checkmarx Jenkins AST is a
restatement of prior reporting...

## Active Threats
**[Headline link](https://...)** ... Digraph: B2 · WEP: likely
(procedural facts only — relational/attribution layer carries lower WEP)
· finding-2026-05-11-0001.

🔗 Connects to: Actor #001 TeamPCP (HIGH, roster) — Jenkins AST plugin
distribution channel is the first appearance of CI/CD-pipeline-poisoning
in the TeamPCP TTP register; dossier update queued via actor-profiler.

[... 700 more words ...]

## 📣 Discord Summary                                   ← Layer 2, last section

Good morning. Here's your 0800 brief — Monday, May 11.

🚨 **Active Threats**

• **[Checkmarx Jenkins AST plugin compromised...](https://www.securityweek.com/...)**
  Checkmarx warned Friday May 9 of a malicious Jenkins AST plugin...
  **DIB CI/CD:** pin to fix version *now*, capture plugin hashes for IOC backfill.

[... ≤1900 chars, natural-language dates, source-linked headlines ...]
```

**Speaker notes:**
Layer 1 is the analyst-grade record — full doctrine framings, Admiralty + WEP citations, Hard Rule 2 annotations, single-source-veto notes, Splunk first-party caveats. ~700 words. Lives in git forever. Layer 2 is the Discord summary — Smart Brevity, natural-language dates, source-linked headlines, ~250 words, ≤1900 chars. The librarian extracts only Layer 2 (heading-to-EOF read) and posts that to #intel-briefs. ONE canonical file, TWO renderings, two audiences. Rebuild lesson: per-audience rendering is a doctrine concern (INTEL-BRIEF-STANDARDS specifies the format) and a librarian responsibility (extraction + delivery), but it's authored by the briefer in one pass. Don't split it across two subagents.

---

## Slide 23 — Retraction handling — additive, never silent

**Subtitle:** When something ships wrong, the record of being wrong becomes part of the record.

**Bullets:**

- **Retraction vs. correction** — RETRACTION = factually wrong / materially misleading / doctrine-violating. CORRECTION = typo / wrong link / wording change without meaning shift.
- **Retraction is ALWAYS additive** — Original brief file stays in `threats/briefs/`, unmodified. New retraction note APPENDED to the brief. Coverage-log entry gets retraction block. Discord retraction post in `#intel-briefs`. Never delete; never edit-to-remove.
- **72h auto-downgrade clock** — Single-source FLASHes ship with an auto-downgrade clock built into the finding frontmatter. Conditions for downgrade are SPECIFIED on the finding itself (no second A/B-grade source AND no Splunk hit AND no CISA pickup → drop attribution leg to C3). When the clock fires unbroken, librarian does in-place frontmatter downgrade — NOT a full retraction (campaign forensics hold; only the attribution leg moves).
- **Tested live on MuddyWater 2026-05-09** — FLASH-0002 (Rapid7 single-source MuddyWater attribution) shipped 2026-05-06 12:18 EDT with a 72h clock. Clock fired unbroken at 2026-05-09 12:18 EDT. Librarian updated finding frontmatter: digraph A2 → C3, digraph_split.attribution_leg → C3, campaign forensics held at A2. Coverage log got the supersession entry. Morning brief 2026-05-10 carried the supersession in narrative.
- **Pattern check after every retraction** — Was grading process followed? Did red-team catch anything? What would have prevented this? If 3+ retractions trace to the same source in 90 days, actor-profiler proposes a source-grade downgrade.

**Speaker notes:**
Retraction handling is the single most under-built feature in most agent systems. The instinct is "fix the error and move on." That destroys auditability. Archimedes' pattern: every retraction is additive. Every retraction is logged. Every retraction triggers a pattern-check. After 3 retractions traced to the same source, the source itself gets graded down — that's the system learning.

---

## §5 — Infrastructure + ops

## Slide 24 — Scheduler — Windows Task Scheduler + PowerShell wrapper

**Subtitle:** 8 scheduled tasks. `infrastructure/scheduler/` holds the templates.

| Task name | Time | What it does |
|---|---|---|
| flash-sweep-0000 | 00:00 EDT | FLASH sweep · queue if quiet hours |
| flash-sweep-0600 | 06:00 EDT | FLASH sweep · queue if quiet hours |
| pre-brief-morning | 07:30 EDT | Collector pre-pass · raw signal → disk · no brief |
| morning-brief | 08:00 EDT | Full scheduled-brief pipeline · 5 phases |
| flash-sweep-1200 | 12:00 EDT | FLASH sweep |
| pre-brief-afternoon | 15:30 EDT | Collector pre-pass · raw signal → disk |
| afternoon-brief | 16:00 EDT | Full scheduled-brief pipeline · 5 phases |
| flash-sweep-1800 | 18:00 EDT | FLASH sweep |

**Code block — wrapper pattern (light gray):**

```powershell
# scripts/run_phase.ps1 (excerpt)

$ErrorActionPreference = 'Stop'
$phaseId = "morning-brief-$(Get-Date -Format yyyyMMdd-HHmmss)"

# Splunk: started event
& uv run python scripts/splunk_log.py --event-file $eventFile

# Invoke claude -p with the phase prompt
& claude -p "Execute the $phase pipeline. Mode 1 if scheduled brief."

# Catchup-push (mitigates librarian push variance)
$exitCode = & git push origin main; if ($?) { 0 } else { $LASTEXITCODE }

# Splunk: completed event with catchup_push_exit
& uv run python scripts/splunk_log.py --event-file $completedEvent
```

**Speaker notes:**
8 Windows Task Scheduler entries. XML templates in `infrastructure/scheduler/`. Each task invokes `scripts/run_phase.ps1` with the phase name as an argument. The wrapper does three things: (1) logs Splunk "started" event with run_id, (2) invokes `claude -p` with the phase prompt, (3) logs Splunk "completed" event with exit code + catchup-push status. The catchup-push pattern (Session 11 discovery) compensates for the librarian's intermittent push behavior — if librarian skipped `git push origin main`, the wrapper does it. `catchup_push_exit` field in Splunk events tracks the outcome for dashboard visibility.

---

## Slide 25 — Hooks — bash scripts for deterministic side effects

**Subtitle:** `.claude/hooks/` — why hooks not subagents (no LLM cost, deterministic, easy to debug)

**Layout:** Full-width dark code block.

```bash
.claude/hooks/discord-post.sh

#!/usr/bin/env bash
# Post a message file to a Discord channel via webhook.
# Invoked by librarian: bash discord-post.sh --channel intel-briefs --message-file <path>

set -euo pipefail

CHANNEL=""; MESSAGE_FILE=""; FLASH=false
while [[ $# -gt 0 ]]; do
    case "$1" in
        --channel)      CHANNEL="$2"; shift 2 ;;
        --message-file) MESSAGE_FILE="$2"; shift 2 ;;
        --flash)        FLASH=true; shift ;;
    esac
done

# Resolve webhook URL by channel name (from .env)
case "$CHANNEL" in
    intel-briefs)   WEBHOOK="$DISCORD_WEBHOOK_INTEL_BRIEFS" ;;
    flash-alerts)   WEBHOOK="$DISCORD_WEBHOOK_FLASH_ALERTS" ;;
    actor-review)   WEBHOOK="$DISCORD_WEBHOOK_ACTOR_REVIEW" ;;
    *) echo "Unknown channel: $CHANNEL"; exit 1 ;;
esac

# Read message body; truncate at 2000 chars if needed (Discord limit)
BODY=$(cat "$MESSAGE_FILE")
if [[ ${#BODY} -gt 2000 ]]; then
    echo "WARN: body >2000 chars; truncating"
    BODY="${BODY:0:1997}..."
fi

# POST
curl -X POST -H "Content-Type: application/json" \
     -d "$(jq -Rs '{content: .}' <<< "$BODY")" \
     "$WEBHOOK"

echo "POSTED to #$CHANNEL"   # parsed by librarian for status
```

**Speaker notes:**
Three hooks total: discord-post.sh, splunk-log.sh, and a couple others for index regen. Why hooks instead of subagents? (1) No LLM cost — bash scripts run free, deterministic, fast. (2) Deterministic behavior — Discord post either succeeds or fails based on HTTP status, not on model reasoning. (3) Easy to debug — you can run the hook by hand from the command line. Rebuild lesson: distinguish between "I need the model to decide" (subagent) and "I need the model to invoke a thing that always does the same operation" (hook). Hooks handle the second case. Don't make Claude write JSON to a webhook on every brief; have Claude invoke a hook that does that.

---

## Slide 26 — Audit trail — three logs that reconstruct any action

**Subtitle:** Together: git + Splunk + Discord = full provenance for everything the agent did.

**Bullets:**

- **git history — the corpus changes** — Every brief committed. Every finding committed. Every dossier update. Every doctrine revision. 60+ commits/week typical. Provenance is queryable: `git log --since`, `git blame`, `git log -p <file>`. Co-Authored-By: Claude trailer on every commit makes agent-vs-human authorship explicit.
- **Splunk events — operational telemetry** — Sourcetype: `archimedes:operation`. Events: `run_started`, `run_completed`, `brief_published`, `git_committed`, `flash_queued`, `threat_box_scoring_completed`, `discord_format_preview_posted`, `retraction_logged`, `policy_violation`. Indexed for dashboarding + alerting on agent behavior.
- **Discord channels — delivery log** — `#intel-briefs` (scheduled briefs + Layer 2 summaries). `#flash-alerts` (FLASH posts). `#actor-review` (HIGH-scoring proposals + retraction proposals). `#commands` (operator slash commands + responses). Every channel post has a message ID; ID recorded in Splunk.
- **Cross-reference via run_id** — Every scheduled phase has a run_id (e.g., `morning-brief-20260511-080000`). The run_id appears in the git commit message, the Splunk event, and the Discord post. Three logs joined on one key.
- **Refusal logging — `policy-violations.yaml`** — Every Hard Rule refusal logged with timestamp, subagent, section, attempted_action, triggering_prompt (sanitized), reason. Auditable record of what the agent WAS asked to do but refused.

**Speaker notes:**
Auditability is what makes the agent defensible in a regulated environment. Five years from now, if someone asks "how did the agent arrive at this attribution on 2026-05-06," the answer is: git log + Splunk events + Discord posts joined on run_id. That same auditability is also how you debug agent behavior. When the briefer makes a weird choice, you can pull the run_id, find the Splunk events, see what input it received, check the doctrine version in git at that commit. Rebuild lesson: design for audit BEFORE you have anything to audit. Adding it later is exponentially harder.

---

## Slide 27 — Configuration — what's where, what's gitignored

**Subtitle:** Three classes: secrets (.env), agent-readable YAML (`infrastructure/`), runtime state (gitignored YAML).

| File | Git status | Contents |
|---|---|---|
| `.env` | gitignored | API keys · Discord webhooks · Splunk HEC token · ANTHROPIC_API_KEY (deliberately unset; use Claude Max) |
| `.env.example` | committed | Schema template · variable names + comments · NO secret values · current with the real .env |
| `infrastructure/source-grades.yaml` | committed | Source → grade + category mapping · 45 entries · ratification log in source-grade-log.md |
| `infrastructure/source-health.yaml` | gitignored | Runtime: status · last_successful_fetch · failure_count · stale_since · last_error · operator notes preserved |
| `infrastructure/watch-config.yaml` | committed | Standing brief sections · sector watchlists · FLASH triggers · silent_day_template |
| `infrastructure/authorized-targets.yaml` | committed | Hard Rule 4 enforcement list · only these targets may be actively scanned |
| `infrastructure/watchlists/*.yaml` | committed | Per-watchlist YAML: A&D, ransomware, etc. Used by collector to filter raw signal |
| `infrastructure/flash-queue.yaml` | gitignored | Quiet-hours FLASH queue · 09:00 catchup sweep processes it |
| `threats/threat-actors/_roster.yaml` | committed | 23-actor roster · per-actor primary_name, aliases, attribution, dossier path, scoring counters |
| `threats/vulnerabilities/_index.yaml` | committed | Tracked CVE index |
| `threats/iocs/_master-index.yaml` | committed | Regenerated by librarian on IOC changes · `scripts/regenerate_ioc_index.py` |

**Speaker notes:**
Configuration discipline: secrets gitignored, schemas committed, runtime state gitignored, operator-set context preserved. Two notable patterns: (1) `.env.example` mirrors the actual `.env` structure — anyone cloning the repo can copy-rename to get a working schema; (2) `source-health.yaml` has a mix of runtime fields (collector overwrites) and operator-set fields (notes preserved verbatim) — collector subagent doctrine specifies the field ownership boundary. If your rebuild has separate operator-set context that should survive runtime overwrites, codify which fields the agent owns vs. the operator owns — same pattern.

---

## Slide 28 — Testing — per-MCP suites + the 13-item preflight

**Subtitle:** 231 unit tests across 8 MCPs. Live validation patterns where mocks aren't enough.

**Bullets:**

- **Per-MCP pytest suites** — Each MCP has its own `tests/` directory. `test_config.py` (env loading), `test_<name>_client.py` (respx-mocked HTTP), `test_policy.py` (where applicable), `test_integration.py` (live tests behind credentials, skipped by default). 231 unit tests passing across 8 MCPs.
- **respx for HTTP mocking** — All HTTP wrappers tested with respx — register expected requests + canned responses, run the client, assert. No real network in unit tests.
- **Live validation for third-party tools** — Mocks based on documentation are confidence-without-verification. theHarvester 4.10.1 + SpiderFoot 4.0.0 each surfaced 3 bugs that unit tests couldn't have caught: API shape drift, off-by-one in scanstatus parsing, wrong JSON endpoint. Fix: live-test against real services.
- **Preflight checklist — 13 items** — `.claude/skills/smart-brevity/references/preflight-checklist.md`. Briefer runs this checklist before every brief publication. ALL must pass or regenerate. Items: source URL present, Admiralty digraph, coverage-log respected, lead-with-impact, banned phrases zero, standing sections present, WEP vocabulary, word count in range, actor/vuln links, TLP marked, single-source veto, quote discipline, Layer 2 section compliant.
- **Doctrine review as a test phase** — When doctrine changes, walk through every subagent that reads it and ask: does the change break anything? When INTEL-BRIEF-STANDARDS got Layer 2, briefer.md + librarian.md + preflight-checklist.md all needed coordinated updates.

**Speaker notes:**
Testing across three layers: unit tests for MCP wrappers (231 passing), preflight checklist for brief composition (13 items), live validation against real services (catches the 6 real bugs mocks missed). Doctrine changes need their own test phase — when you change a .md file, walk through every subagent that reads it. This is similar to schema changes in a database: a schema change isn't just a SQL migration, it's a coordinated update across all the code that reads the schema.

---

## §6 — Rebuild guide

## Slide 29 — Minimum viable Archimedes

**Subtitle:** The smallest version that delivers value. Then iterate.

**Layout:** Directory tree (light gray) + italic footer paragraph.

```
minimum-viable/
├── doctrine/
│   └── INTEL-GRADING.md            # ONE doctrine file. Admiralty + WEP.
│
├── .claude/
│   ├── agents/
│   │   ├── grader.md               # ONE subagent. Promotes raw → graded.
│   │   └── briefer.md              # ONE subagent. Composes the brief.
│   └── hooks/
│       └── discord-post.sh         # ONE delivery channel.
│
├── mcps/
│   └── rss-bridge/                 # ONE MCP. RSS feed fetcher.
│
├── threats/
│   ├── raw-signal/                 # collector output (manual to start)
│   ├── findings/                   # grader output
│   └── briefs/                     # briefer output
│
├── .env                            # DISCORD_WEBHOOK_URL only
├── pyproject.toml
└── CLAUDE.md                       # the agent's identity
```

**Footer (italic, centered):**

Start here. Run it manually for a week — operator pulls articles from feeds, drops them into `raw-signal/`, invokes the grader, invokes the briefer, posts to Discord via the hook. As friction surfaces, add the next piece: collector subagent → more MCPs → librarian subagent → scheduler → more doctrine files. Each addition replaces one source of manual work. The minimum viable version proves the value before you commit to building the rest.

**Speaker notes:**
The trap is building Archimedes top-down — full doctrine, all 9 subagents, all 8 MCPs, scheduler, hooks, audit trail — before any of it has produced a single brief. That'll fail. The MVP version: one doctrine file, two subagents, one MCP, one delivery channel. Run it manually for a week. The friction tells you what to build next. This pattern (build the load-bearing thin slice; add to it from real friction) is also what Archimedes itself did — Session 1 had ONE doctrine file (LEGAL-POLICY) and one subagent (the grader was first). Everything else accreted over 13 sessions.

---

## Slide 30 — Recommended build order

**Subtitle:** What to add when. Time estimates assume the team is familiar with Claude + MCP.

| When | Add | Why now |
|---|---|---|
| Week 1 | Doctrine + identity | Write CLAUDE.md + 1-2 doctrine files. No code yet. Just the agent's job description. |
| Week 1 | Grader subagent + RSS MCP | Build the grading path end-to-end against canned input. Run manually. |
| Week 2 | Briefer subagent | Add brief composition. Hand-craft 3-5 sample briefs first; reverse-engineer the prompt from the samples. |
| Week 2 | Discord delivery (hook) | discord-post.sh + webhook URL in .env. Ship the first brief to a channel. |
| Week 3 | Librarian subagent + git | Move side effects (commit, post, log) into the librarian. Test the LEGAL-POLICY content scan gate. |
| Week 3 | Collector subagent | Replace manual feed-pulling with the collector. Add 5+ MCPs (VT, Shodan, urlscan, RSS, web search). |
| Week 4 | Scheduler | Task Scheduler XMLs · run_phase.ps1 wrapper · Splunk telemetry. First fully autonomous brief. |
| Week 4 | Analyst + red-team | Add SAT skills + the analyst chain. Trigger red-team conditional on WEP threshold. |
| Week 5 | Actor profiles + vulns | Add actor-profiler + vuln-tracker. Hard Rule 5 gate to #actor-review. |
| Week 5 | Retraction handling | RETRACTION-POLICY + 72h auto-downgrade clock. Test on a hypothetical bad finding. |
| Week 6 | On-demand / Discord listener | scripts/discord_listener.py + the slash command surface. Now interactive. |
| Week 6 | Hardening + observability | Splunk dashboards. Refusal logging. Audit-trail end-to-end tests. Production cutover. |

**Speaker notes:**
Six weeks for a working version. Each week is two additions. The order matters: doctrine + identity before any code; grader + briefer before collector (so you can test on canned data first); manual operation in weeks 1-3, autonomous in week 4 once scheduler is in. The order I listed is the order Archimedes evolved through Sessions 1-7 — there's a reason; do it the way it grew.

---

## Slide 31 — What to skip / defer

**Subtitle:** Things Archimedes has that you probably don't need on day 1.

**Bullets:**

- **The web dashboard** — `interfaces/dashboard/` is an empty placeholder. Originally planned as a Flask UI for browsing the corpus. Deferred indefinitely because the Discord listener (`/cve`, `/investigate`, `/ioc-hunt`) covers the interactive-query need and the markdown corpus is browsable in GitHub or any editor. Skip unless you need a non-technical-stakeholder browser.
- **8 MCP wrappers on day 1** — Start with 1-3. RSS bridge covers most feeds. VirusTotal covers IOC enrichment. Splunk-query covers first-party. Add more when you hit a "this would be easier with X" moment. theHarvester + SpiderFoot can wait until you need passive recon.
- **All 9 subagents** — Start with 2-3. Grader + briefer covers the load-bearing path. Add collector (week 3), librarian (week 3), scheduler (week 4), analyst (week 4), red-team (week 4), actor-profiler (week 5), vuln-tracker (week 5). Building all 9 before anything ships is the failure mode.
- **Per-actor red-team variant** — We have red-team-analyst for findings. We also drafted a per-actor red-team for scoring runs — never built because the regular red-team chain was sufficient. Skip until proven necessary.
- **On-demand investigation slash commands beyond `/investigate` + `/ioc-hunt`** — The full list (8 slash commands) accreted over time. Start with 2-3 (`/investigate` + `/ioc-hunt` + `/help`). `/new-actor`, `/update-tracking`, `/approve-scoring` matter once you have an actor corpus to maintain.
- **FLASH if your cadence permits** — Scheduled briefs cover most operational needs. FLASH is the answer to "CVE-10 broke at 3 AM, page me now." If your operators don't need that pager-style escalation, scheduled briefs alone are sufficient.

**Speaker notes:**
Half the system isn't needed for V1. The dashboard is the most expensive thing we never built. FLASH is the most expensive thing we DID build that might not justify the cost for every team. Take what makes the agent shape work for your team; defer what doesn't until you feel the pain.

---

## Slide 32 — Q&A

**Layout:** Big centered "Questions?" + subtitle + presenter contact.

**Title:** Questions?
**Subtitle (italic):** Where would you start?
**Footer:** [Presenter name] · [Email / Slack / Teams handle]

**Speaker notes:**
Likely questions to be ready for:
- **Token cost at this volume** — order of magnitude per month, not exact.
- **Why Claude over Anthropic API direct** — Claude Code's subagent runtime is the value-add; building the same with bare API would be 3-4 months of agent-runtime work before the CTI work starts.
- **What about open-source LLMs** — possible but harder; the long-context + tool-use + structured-output discipline is where Claude is strongest.
- **How long to a rebuild** — 6 weeks for a working version with the team familiar; 12 weeks if learning Claude as you go.
- **What broke that you wish you'd known earlier** — schtasks UTF-16 LE BOM, PYTHONHOME poisoning under uv run, librarian push variance. All documented in CLAUDE.md operational notes.

---

*End of deck. 32 slides, ~45 minutes, ~85 seconds per slide.*

*This markdown corresponds 1:1 with `archimedes-architecture.pptx` — pick whichever surface is friendlier for your template-merge workflow.*
