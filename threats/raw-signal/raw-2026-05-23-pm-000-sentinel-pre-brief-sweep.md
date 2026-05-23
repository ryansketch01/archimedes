---
raw_id: raw-2026-05-23-pm-000-sentinel-pre-brief-sweep
collected_at: 2026-05-23T15:35:00-04:00
run_id: pre-brief-20260523-153000
collection_mode: pre_brief_collection
test: false
source:
  source_yaml_id: archimedes-internal
  source_name: "Archimedes collector sentinel"
  source_url: null
  published_at: 2026-05-23T15:35:00-04:00
sweep_window:
  start: 2026-05-23T08:00:00-04:00
  end: 2026-05-23T15:35:00-04:00
  duration_h: 7.5
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [sentinel_pre_brief_sweep_summary]
triage_tags:
  - sentinel
  - pre_brief_collection_summary
  - sweep_window_7p5h
  - afternoon_brief_input
promoted: false
ttl_expires_at: 2026-08-21T15:35:00-04:00
---

# 2026-05-23 Afternoon Pre-Brief Collection Sentinel

## Sweep Window
2026-05-23T08:00:00-04:00 → 2026-05-23T15:35:00-04:00 (7.5h overlap from morning brief publication)

## Run ID
pre-brief-20260523-153000

## Mode
pre_brief_collection (Mode 1 per collector subagent definition)

## Sources Queried (Productive vs Quiet)

| Source | Endpoint | Status | Items in Window | Productive Hits |
|---|---|---|---|---|
| The Hacker News | feedburner.com/TheHackersNews | healthy | 2 | npm staged publishing rollout; Packagist 8-pkg supply-chain attack |
| Snyk | snyk.io/blog/feed/ | healthy | 1 | Laravel-Lang Supply Chain Advisory (Snyk first-party) |
| BleepingComputer | /feed | healthy | 1 | CINEMAGOAL piracy bust (LE op; no CTI value, no A&D, discarded per Mode 1) |
| Ars Technica root | /feed | healthy | 1 | SpaceX Starship V3 V3 test flight (A&D-adjacent kinetic-not-cyber, awareness; not raw-signaled) |
| Dark Reading | /rss.xml | healthy | 2 | events-only (no threat content) |
| SecurityWeek | feedburner | healthy | 0 | (PM quiet) |
| The Record | /feed | healthy | 0 | |
| Krebs on Security | /feed | healthy | 0 | |
| Unit 42 | feedburner | healthy | 0 | (06:00 FLASH already captured UNC1549 publication; PM quiet) |
| MSTIC | /security/blog/feed | healthy | 0 | |
| SentinelLabs | labs/rss/ | healthy | 0 | |
| Recorded Future | /feed | healthy | 0 | |
| ISC SANS | rssfeed.xml | healthy | 0 | |
| Proofpoint | /us/rss.xml | healthy | 0 | |
| WeLiveSecurity (ESET) | /en/rss/feed/ | healthy | 0 | |
| Rapid7 | /blog/rss/ | healthy | 0 | |
| GitHub Blog | /feed/ | healthy | 0 | |
| LiteSpeed Blog | /feed/ | healthy | 0 | (advisory pre-window; already captured FLASH-0600-002 + am-005) |
| CISA Advisories | all.xml | healthy | 0 | |
| CISA KEV | known_exploited_vulnerabilities.json | healthy | 0 | (no new entries since 2026-05-22 CVE-2026-9082 Drupal add already captured) |
| Mandiant | feedburner.com/Mandiant | DEGRADED — see source-health | n/a | continued feedburner shutdown (16th+ consecutive 404; held healthy) |
| Sophos | news.sophos.com/en-us/feed/ | DEGRADED | n/a | 404 again — confirms AM sweep observation (held healthy pending operator alt-endpoint) |
| Cisco Talos | blog.talosintelligence.com/feeds/posts/default | DEGRADED | n/a | 404 — same as AM (held healthy) |
| Wiz Research | blog/feed.xml or /rss.xml | DEGRADED | n/a | 404 on both candidate paths (held healthy) |
| Socket | blog/rss | DEGRADED | n/a | 404 same as AM (held healthy; no top-level entry change) |

## Splunk First-Party Probes (Mode 4 enrichment)
- Packagist campaign IOCs (`parikhpreyash4`, `gvfsd-network`, `systemd-network-helper-aa5c751f`, `DebugChromium.exe`, `flipboxstudio.info`) across archimedes + defenseclaw_local (-30d): **0 hits**.
- Indexes remain dormant pattern across 60+ consecutive sweeps; absence is not informative.

## VirusTotal Enrichment Delta (Productive)
- `flipboxstudio[.]info` (Laravel-Lang C2 carried from AM-001):
  - AM sweep (12:42 UTC): 3 malicious + 1 suspicious / 47 harmless / 33 undetected
  - PM sweep (16:57 UTC): **10 malicious + 1 suspicious / 47 harmless / 33 undetected**
  - Detection ramped **3.3x in ~4 hours** (Kaspersky, Sophos, Fortinet, ADMINUSLabs, Forcepoint ThreatSeeker, CRDF, Certego, Lionic, SOCRadar, VIPRE)
  - alphaMountain.ai categorizes as "Suspicious"; no registrar / creation-date in VT record (privacy-protected registration)
  - This delta is recorded in `raw-2026-05-23-pm-003-snyk-laravel-lang-supply-chain-advisory-primary-vt-detection-escalation.md` for grader / finding-2026-05-23-0007 carry-forward.

## Raw-Signal Files Written This Sweep
1. `raw-2026-05-23-pm-001-thn-github-npm-staged-publishing-2fa-allow-flags-supply-chain-controls.md` — GitHub/npm controls announcement (TeamPCP context referenced; not a new attack; ecosystem-defense surface)
2. `raw-2026-05-23-pm-002-thn-socket-packagist-8-package-supply-chain-attack-github-hosted-linux-malware-parikhpreyash4.md` — NEW Composer/Packagist supply-chain attack; eight packages; package.json-postinstall cross-ecosystem injection; GitHub-hosted Linux binary; UNATTRIBUTED per Socket
3. `raw-2026-05-23-pm-003-snyk-laravel-lang-supply-chain-advisory-primary-vt-detection-escalation.md` — Snyk first-party advisory primary on Laravel-Lang campaign (corroborates AM-001 THN/Socket/Aikido relay chain); confirms ~700 versions across 4 packages, named four Snyk advisory IDs, full IOC set including DebugChromium.exe Windows artifact + `/var/run/secrets/` `/proc/[pid]/environ` runtime patterns; carries forward VT detection escalation 3→10 malicious

## FLASH Triggers Evaluated for Grader Attention

**NONE** this sweep produce a NEW FLASH outside what already entered the morning-brief candidate pool. Specifically:

- **Trigger 1 (critical-cve-exploited):** No new CVE with active exploitation surfaced in window. Carry-forward locks active: LiteSpeed CVE-2026-48172 (FLASH-0600-002 + am-005 NVD-confirmation), Drupal CVE-2026-9082 (FLASH-1800-001 + am-006 carry-forward).
- **Trigger 2 (tracked-actor-attribution):** No new tracked-actor attribution in window. Packagist 8-package campaign is explicitly UNATTRIBUTED per Socket. npm Staged Publishing references TeamPCP but only as ecosystem-defense context (existing tracked actor; not new attribution).
- **Trigger 3 (first-party-ioc-hit):** Splunk indexes remain dormant; zero hits this sweep across Packagist + Laravel-Lang IOC set (-30d).
- **Trigger 4 (tracked-actor-ttp-change):** No additional in-window TTP change for any tracked actor. UNC1549 Unit 42 publication remains the active candidate from 06:00 FLASH (raw-2026-05-23-flash-0600-001).
- **Trigger 5 (ad-sector-campaign):** Packagist 8-pkg campaign has no A&D-direct victim named (Composer/Laravel ecosystem broadly; eight unrelated PHP packages; no enterprise-victim disclosure). Laravel-Lang Snyk primary names no A&D-direct victim. SpaceX Starship is kinetic-aerospace not cyber.
- **Trigger 6 (zero-day-no-patch):** None — Packagist packages have been removed from registry (effectively patched), Laravel-Lang campaign disclosure includes Composer ecosystem mitigations, no zero-day-without-patch in window.

## Carry-Forward Items for 16:00 Afternoon Brief Grader/Briefer

From morning-brief candidate pool plus PM additions:
- **UNC1549 Unit 42 tradecraft evolution** (FLASH-0600-001) → Iran Cyber Watch standing section + sector-focus (historical A&D framing)
- **LiteSpeed CVE-2026-48172** (FLASH-0600-002 + am-005) → Tracked Vulnerabilities (likely new tracking entry for vuln-tracker)
- **Laravel-Lang PHP campaign** (am-001 THN/Socket/Aikido + pm-003 Snyk first-party + VT detection escalation 3→10) → Supply Chain Watch candidate; the Snyk primary closes the AM 'primary not retrieved' flag and the VT delta is real-time threat-intel quality signal
- **Packagist 8-package supply-chain attack** (pm-002) → grader's choice on Supply Chain Watch grouping vs. discrete finding; Socket primary distinguishes mechanism from Laravel-Lang (package.json postinstall + GitHub-hosted Linux binary vs. helpers.php autoload-files); UNATTRIBUTED so does not aggregate to TeamPCP
- **npm Staged Publishing rollout** (pm-001) → ecosystem-defense narrative item; not a finding (no attack), but useful brief context against the Laravel-Lang + Packagist supply-chain cluster
- **Russian Kosmos 2610-2613 / ICEYE** (am-004) → Sector Focus: Aerospace & Defense (space-domain ISR adjacent; grader may carry forward)
- **CVE-2026-9082 Drupal / CISA KEV form / Underminr CDN-tenant bypass** (am-002, am-003, am-006) → Coverage continuation / standing-sections / awareness

## Source-Health Notes (Runtime Updates Applied)
- thehackernews: successful fetch (2 in-window items; productive sweep) — last_successful_fetch advanced to 2026-05-23T15:35:00-04:00
- snyk: successful fetch (1 in-window item; PRODUCTIVE — first time a Snyk RSS surfaced an in-window threat-intel primary in this corpus) — last_successful_fetch advanced
- bleepingcomputer: successful fetch (1 in-window item, discarded per Mode 1)
- ars-security (workaround root path): successful fetch (1 in-window item; A&D-adjacent kinetic, awareness-only)
- mandiant / sophos / cisco-talos / wiz-research / socket: 404 pattern unchanged from AM (held healthy pending operator alt-endpoint identification)
- All other A/B-grade priority sources reachable with zero in-window items per quiet PM cadence
