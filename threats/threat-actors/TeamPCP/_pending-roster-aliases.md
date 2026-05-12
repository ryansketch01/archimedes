# TeamPCP — Pending Roster Alias Additions

Operator decision required. Surfaced by `finding-2026-05-12-FLASH-0001` (Mini Shai-Hulud npm + PyPI worm) via Snyk corroboration analysis. Librarian does NOT auto-add to `threats/threat-actors/_roster.yaml` per operator-decision rule for actor-identity changes.

## Proposed aliases (from Snyk byline analysis)

| Alias | Source | First Surface | Notes |
|---|---|---|---|
| DeadCatx3 | Snyk (Stephen Thoemmes) | 2026-05-12-FLASH-0001 | New alias; not in any prior Archimedes-corpus source |
| PCPcat | Snyk (Stephen Thoemmes) | 2026-05-12-FLASH-0001 | New alias; not in any prior Archimedes-corpus source |
| ShellForce | Snyk (Stephen Thoemmes) | 2026-05-12-FLASH-0001 | New alias; not in any prior Archimedes-corpus source |
| CipherForce | Snyk (Stephen Thoemmes) | 2026-05-12-FLASH-0001 | New alias; not in any prior Archimedes-corpus source |

## Source citation

- **Snyk blog post** (Stephen Thoemmes byline) — Mini Shai-Hulud Mini Shai-Hulud npm + PyPI worm coverage, 2026-05-12; aliases listed in the "Threat actor: TeamPCP / DeadCatx3 / PCPcat / ShellForce / CipherForce" identification block.
- **Provisional grade A** for Snyk (awaiting ratification per `infrastructure/source-grade-log.md` 2026-05-12 entry).

## Why librarian did not auto-add

Per CLAUDE.md operating convention (Hard Rule 2 attribution discipline + actor-profiler ownership of `_roster.yaml`), the librarian ships what others produced and does NOT modify actor identity. Alias additions to `_roster.yaml` are an actor-profiler responsibility, executed under the `/update-tracking` or `/new-actor` workflows where the actor-profiler's dossier-side methodology runs.

## Recommended operator action

One of:

1. **Run `/update-tracking 001`** — actor-profiler will read this file, integrate aliases into `_roster.yaml` actors[0].aliases, and update the TeamPCP dossier (which does not yet exist as of 2026-05-12 — `threats/threat-actors/TeamPCP/` was created today as part of this pending-aliases write).
2. **Defer to next scheduled review** — TeamPCP `next_review_due: 2026-06-16` per `_roster.yaml`; alias additions could roll into that scoring run.
3. **Hold pending corroboration** — wait for a second independent A-grade source (Wiz, Mandiant, Unit 42, MSTIC, CrowdStrike) to surface the same aliases before adding. The current single-source-attribution (Snyk only) on alias-naming is conservative.

## Detection-engineering note

Aliases are tracked-actor metadata used for cross-reporting cross-walks (e.g., a future report naming "PCPcat" should resolve back to TeamPCP #001 in our roster). Aliases themselves are NOT IOCs in the operational-blocking sense — they're string-match aids for grader/analyst future-attribution work.

---

**Created:** 2026-05-12 by librarian during FLASH-0001 commit cycle (run `librarian-flash-20260512-060000`)
**Owner:** actor-profiler (on next `/update-tracking 001` invocation)
**Related:** `threats/threat-actors/_roster.yaml` actors[0]; `threats/findings/finding-2026-05-12-FLASH-0001.md` IOCs section
