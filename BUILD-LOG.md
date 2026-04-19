# Archimedes Build Log

Session-by-session record of what was built, decisions made, and what's next.
Keeps context durable across sessions and preserves the build history.

---

## Session 1 — Scaffold & Doctrine

**Date:** 2026-04-18
**Status:** ✅ Complete

### What was built

**Project root (5 files)**
- `CLAUDE.md` — orchestrator charter (persona, cadence, pipelines, hard rules)
- `README.md` — public-facing project description
- `.gitignore` — excludes secrets, caches, quarantine, runtime state
- `.env.example` — complete environment variable template
- `pyproject.toml` — Python deps (minimal: pyyaml, requests, dotenv, splunk-sdk)

**Doctrine (9 files) — `doctrine/`**
- `INTEL-GRADING.md` — NATO Admiralty Scale + 6 additions (checklists, corroboration rules, dual-grade tech sources, single-source veto, inclusion thresholds, grade revisions)
- `INTEL-BRIEF-STANDARDS.md` — Smart Brevity + 7 additions (layered format, configurable watches, explicit SB rules, FLASH template, pre-flight checklist, queryable coverage log, retraction linkage)
- `INTEL-OPERATIONS.md` — runbook + 8 changes (merged alerts/FLASH, midday dropped, structured watchlists, YAML roster, Pi retired, weekly synthesis, failure handling)
- `THREAT-BOX-METHODOLOGY.md` — Piazza framework + 5 additions (machine-readable scoring, Admiralty tie-in, HIGH human sign-off, review policy, IOC corroboration bonus)
- `ACTOR-PROFILE-STANDARD.md` — codifies APT28 structure as template
- `FLASH-POLICY.md` — quiet hours (9am–9pm EDT) + critical override + queue logic
- `RETRACTION-POLICY.md` — correction procedures, never silent delete
- `LEGAL-POLICY.md` — legal policy + 8 additions (prohibited patterns, authorized targets, ITAR/EAR, attribution standards, violation handling, GDPR, enforcement)
- `LEGAL-POLICY-CHANGELOG.md` — v1.0.0 initial

**Infrastructure configs (6 files) — `infrastructure/`**
- `watchlists/aerospace-defense.yaml` — 15 companies with tickers, aliases, subs, domains
- `watch-config.yaml` — standing sections (Iran + A&D active; 6 more stubbed)
- `flash-policy.yaml` — machine-readable FLASH triggers, quiet hours, override
- `authorized-targets.yaml` — empty seed (human-only editing)
- `source-grades.yaml` — 42 sources, 33 active at v1, with dual-grade tech sources
- `source-grade-log.md` — ledger for grade change history

**Intel corpus (5 files) — `threats/`**
- `threat-actors/_roster.yaml` — all 22 actors with aliases, attribution, threat levels
- `threat-actors/APT28/profile.md` — migrated with full frontmatter (exemplar)
- `threat-actors/APT28/iocs.md` — migrated with frontmatter
- `threat-actors/APT28/iocs.yaml` — full IOC sidecar (30 indicators, 4 hunt queries)
- `threat-actors/APT28/threat-box.yaml` — exemplar scoring, awaiting `/approve-scoring 006`
- `vulnerabilities/_index.yaml` — 3 zero-days stubbed
- `briefs/_coverage-log.yaml` — anti-repetition log with schema
- `iocs/_master-index.yaml` — generated index (APT28 only at v1)

**Scripts (2 files) — `scripts/`**
- `migrate-actor.py` — port an actor from old C3PO repo
- `regenerate-ioc-index.py` — rebuild master index nightly

**Directory stubs (`.gitkeep` files)**
- `.claude/agents/`, `.claude/skills/`, `.claude/commands/`, `.claude/hooks/`
- `threats/findings/`, `threats/raw-signal/`, `threats/campaigns/`
- `interfaces/discord-bot/`, `interfaces/dashboard/`
- `scheduler/systemd/`, `mcp-servers/`
- `tests/fixtures/`, `tests/briefs/`, `quarantine/`

### Decisions made

- **Target profile:** `ad-prime-v1` — mid-to-large US A&D contractor
- **Persona:** confident CTI analyst; Star Wars framing dropped entirely
- **Cadence:** 2 scheduled briefs (08:00, 16:00 EDT) + 4 FLASH sweeps + 3 weeklies
- **FLASH quiet hours:** 21:00–09:00 EDT (queue + catchup); critical override for CVSS 10 + exploitation + tracked actor + A&D hit
- **Splunk:** local PC, DefenseClaw feeds `defenseclaw_local` index, Archimedes uses `archimedes` index
- **Claude plan:** Max 5x ($100/mo)
- **Discord:** existing bot repurposed
- **LobsterPi:** retired from this project

### What's NOT in this scaffold (coming in later sessions)

- Subagent definitions (Session 2)
- Skills (Session 2)
- MCP server configs (Session 3)
- `settings.json` (Session 3)
- Slash commands (Session 4)
- Scheduler systemd units (Session 5)
- Discord bot code (Session 6)
- Flask dashboard (Session 6)
- Evals vs. old C3PO (Session 8)

### Prep for Session 2

When resuming:
1. Unzip into your `archimedes` private GitHub repo
2. `cd archimedes && pip install -e ".[all]"`
3. Copy `.env.example` → `.env` and fill in what you have now (Splunk credentials, Discord token; sources can wait)
4. Initial git commit
5. Come back for Session 2 — subagent definitions

### Known items to address in Session 2

- Subagent tool scopes and write permissions per the architecture table in CLAUDE.md
- Skills for: admiralty-grading, smart-brevity, threat-box-scoring, sat-ach, sat-kac, ioc-extraction
- First-pass subagent prompts that reference the doctrine correctly
- The `collector` subagent in particular needs careful design since it's the most resource-intensive

---

*Template for future sessions:*

```
## Session N — Title

**Date:** YYYY-MM-DD
**Status:** In progress / Complete / Blocked

### What was built
### Decisions made
### What's NOT in this session
### Prep for Session N+1
### Known items to address
```
