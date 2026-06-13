---
raw_id: raw-2026-06-13-pm-002
collected_at: 2026-06-13T15:35:30-04:00
run_id: pre-brief-20260613-153000
collection_mode: pre_brief_collection
sources:
  - source_yaml_id: securityweek
    source_name: SecurityWeek
    source_url: https://www.securityweek.com/npm-12-will-change-script-execution-behavior-to-prevent-supply-chain-attacks/
    published_at: 2026-06-13T11:52:58-04:00
    byline: Ionut Arghire
  - source_yaml_id: github-blog-self-disclosure
    source_name: GitHub Blog (NPM 12 roadmap announcement — referenced)
    source_url: null  # SecurityWeek references GitHub announcement; direct GitHub URL not extracted this sweep
    published_at: 2026-06-13T00:00:00-04:00  # approximate; SecurityWeek attributes "the source of these announcements" to GitHub
    byline: GitHub
match_reason:
  watchlist: [supply_chain_npm_ecosystem]
  actors: [Shai-Hulud, TeamPCP]  # roster: TeamPCP (#001) HIGH; Shai-Hulud NOT on _roster.yaml — flag for actor-profiler /new-actor evaluation (operator-deferred candidate similar to Velvet Ant)
  vulnerabilities: []
  keywords: [NPM 12, npm install, preinstall, postinstall, prepare, binding.gyp, package.json, allowlist, npm approve-scripts, --allow-remote, supply chain]
triage_tags: [carry_forward_resolution_NEW_DETAIL, supply_chain_defensive_roadmap, npm_ecosystem, ttp_landscape_change, defer_to_briefer]
iocs_extracted: true
iocs_count: 0  # defensive product roadmap — no IOCs
text_word_count: 720
promoted: true
promoted_to_finding: finding-2026-06-13-0005
promoted_at: 2026-06-13T16:12:00-04:00
promoted_by: grader
promotion_run_id: afternoon-20260613-160000
ttl_expires_at: 2026-09-11T15:35:30-04:00
flash_trigger_evaluation:
  trigger_evaluation: ALL_FAIL
  notes: "Defensive product roadmap, no CVE, no exploitation, no actor attack-action — opposite of FLASH triggers. Eligible for inclusion in 16:00 afternoon brief as supply-chain ecosystem context continuing the developer-tooling-supply-chain cluster (AUR / Atomic Arch / NanoClaw / Tenet Agentjacking from 2026-06-12 afternoon brief)."
---

# NPM 12 default behavior change — install scripts blocked by default (carry-forward from 12:00 FLASH)

## Headline

GitHub announced via SecurityWeek 2026-06-13 11:52 EDT that **NPM 12 (expected July 2026)** will change the default behavior of `npm install` so that **`preinstall`, `install`, `postinstall`, and `prepare` scripts from dependencies will no longer execute unless explicitly allowed**. Native `node-gyp` builds (packages with `binding.gyp` and no explicit install script) will also be affected by default. Git dependencies and remote URL (HTTPS tarball) dependencies will require explicit flags (`--allow-remote`) to resolve. The change is motivated by recent NPM supply-chain attacks — SecurityWeek explicitly names **TeamPCP** and **Shai-Hulud** as the campaigns the change is responding to.

Item carry-forward-deferred from 06-13 12:00 FLASH sweep to this pre-brief (NOT a FLASH candidate; defensive roadmap, not an attack).

## What is changing in NPM 12

| Default behavior change | Detail |
|---|---|
| `preinstall` scripts from deps | Blocked unless explicitly allowed |
| `install` scripts from deps | Blocked unless explicitly allowed |
| `postinstall` scripts from deps | Blocked unless explicitly allowed |
| `prepare` scripts (git / file / link deps) | Blocked |
| Native `node-gyp` builds (`binding.gyp` without explicit install script) | Affected |
| Git dependencies resolution at install | Won't resolve unless allowed |
| Remote URL (HTTPS tarball) dependencies | Won't resolve unless `--allow-remote` flag set |

## Opt-in / allowlist mechanic

Developers run `npm approve-scripts --allow-scripts-pending` which generates an allowlist written to `package.json`. Trusted packages are approved; others remain blocked. This is functionally equivalent to the security-aware approach already taken by `pnpm` and `bun`, brought to npm as default.

## Timing

- **NPM 12 release expected:** July 2026 (per SecurityWeek)
- **Preparation upgrade path:** developers can upgrade to **NPM 11.16.0 or later** now to prepare
- **No CVE attached:** this is a defensive product change, not a vulnerability remediation

## Threat-actor / campaign references (verbatim short quote, ≤15 words)

SecurityWeek references two named campaigns motivating the change:

- **TeamPCP** — "exploited automatic script execution during npm install" (≤15 words).
- **Shai-Hulud** — described as a "self-replicating worm" that "weaponized binding.gyp files" (≤15 words).

Both campaigns are described as having "infected thousands of developers with malware."

## Roster cross-walk

- **TeamPCP (#001)** — already on `_roster.yaml`, threat_level HIGH, tracked_since 2026-03-18, dossier `threats/threat-actors/TeamPCP/`. This NPM 12 change is a structural defensive response to TeamPCP's documented TTP (automatic install-script execution). Material for the TeamPCP dossier's TTP-evolution timeline.
- **Shai-Hulud** — **NOT on `_roster.yaml`**. This is the second roster-gap candidate this week (after Velvet Ant from 2026-06-12 afternoon brief). Flag for actor-profiler `/new-actor` evaluation post-brief; operator-deferred handoff appropriate (no immediate Hard Rule 5 gate fire — Shai-Hulud is a self-replicating worm not yet documented targeting A&D primes).
- **GlassWorm (#005)** — already on `_roster.yaml`, HIGH, NOT mentioned in this article (continuing pattern: GlassWorm dormant in current reporting cycle).
- **ShinyHunters / UNC6240** — separately covered in raw-2026-06-13-pm-005 below.

## Cross-cluster context

This continues the **supply-chain-of-developer-tooling cluster** noted in the 2026-06-12 afternoon brief (AUR 400+ packages / Atomic Arch Rust stealer + eBPF / NanoClaw rejected / Tenet Agentjacking 85% success rate against Claude Code + Cursor). NPM 12's structural default-block is the most aggressive ecosystem-level defensive response in the cluster. Material for the briefer's continuing supply-chain narrative.

## Source-chain audit

| Source | Type | Authority |
|---|---|---|
| GitHub blog (referenced) | Vendor primary on own product roadmap | A — direct vendor disclosure; URL not directly retrieved this sweep, deferred to grader |
| SecurityWeek 2026-06-13 | News-tier 1st publisher | B — full A&D-relevant news coverage |

**Independence check:** Single-source (SecurityWeek relays GitHub directly). Direct retrieval of the GitHub blog post would lift this from B (news-tier first publisher) to A (vendor direct on own product roadmap). Operator-confidence threshold for finding promotion: GitHub's announcement is highly stable as a defensive product roadmap (low information-extraction risk), so single-source-with-direct-vendor-reference is treated as sufficient under INTEL-GRADING.md's defensive-roadmap pattern.

## Extraction notes

- Language: en
- Article type: News-tier coverage of vendor product roadmap
- Raw IOC extraction invoked: yes — none surfaced (defensive roadmap)

## IOCs (from ioc-extraction skill)

```yaml
iocs: []  # defensive product roadmap, no malicious indicators

attribution_claims:
  - actor: TeamPCP
    cluster_id: "001"  # _roster.yaml
    confidence_language_used_by_source: "exploited automatic script execution during npm install"
    attribution_authority: SecurityWeek paraphrasing earlier industry reporting
    note: "Not a new attribution — TeamPCP's TTP already documented in dossier. This is a defensive-response framing."
  - actor: Shai-Hulud
    cluster_id: NOT_ON_ROSTER
    confidence_language_used_by_source: "self-replicating worm that weaponized binding.gyp files"
    attribution_authority: SecurityWeek paraphrasing earlier industry reporting
    note: "Roster-gap candidate. Flag for actor-profiler /new-actor evaluation post-brief."
```

## Carry-forward resolution

**Carry-forward item 2 (NPM 12) — RESOLVED with material new detail.**

- New ecosystem-supply-chain reporting: **YES** — full technical mechanic now public (block default, allowlist via `npm approve-scripts`, `--allow-remote` flag, prepare-script gating, git/file/link dep treatment, binding.gyp coverage)
- Package-takeover events: **NO** (this is a defensive change; no new attack)
- Related Sonatype/Snyk/GitHub advisories: **YES** (GitHub itself is the announcement source per SecurityWeek)
- Recommended action: Grader evaluate for new finding. Briefer continues supply-chain cluster narrative. Actor-profiler flagged for Shai-Hulud `/new-actor` consideration (operator-deferred candidate, second this week after Velvet Ant).
