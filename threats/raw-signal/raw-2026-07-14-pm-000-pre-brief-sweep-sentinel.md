---
raw_id: raw-2026-07-14-pm-000
collected_at: 2026-07-14T15:43:30-04:00
run_id: pre-brief-20260714-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: multiple
  source_name: Afternoon pre-brief sweep sentinel (2026-07-14 15:30 EDT)
  source_url: null
  published_at: 2026-07-14T15:43:30-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [sweep-record]
triage_tags: [sweep_sentinel, non_promotable_record]
iocs_extracted: false
iocs_count: 0
text_word_count: 0
promoted: false
ttl_expires_at: 2026-10-12T15:43:30-04:00
---

# Afternoon pre-brief collection sweep — 2026-07-14 15:30 EDT (window ~07:30→15:30 EDT, 8h)

Sweep record for the 16:00 EDT afternoon brief. Patch-Tuesday-heavy window (Microsoft + Adobe + SAP + VMware all shipped). This is a bookkeeping sentinel, not a promotable finding.

## Sources queried (healthy per source-health.yaml)

- **bleepingcomputer** — RSS 200, 15 items in feed, 10 in 8h window. PRODUCTIVE (pm-001, pm-002, pm-006; plus filtered items below).
- **securityweek** — RSS 200, 10 items in feed, 5 in window. PRODUCTIVE (pm-003, pm-005, pm-008; MS Patch Tuesday corroborates pm-001).
- **the-record** — RSS 200, 5 items in feed, 3 in window. PRODUCTIVE (pm-007; 2 filtered).
- **cisa-kev** — JSON catalog v2026.07.14 (released 2026-07-14) directly retrieved. 4 in-window adds: CVE-2026-56155 (MS ADFS) + CVE-2026-56164 (MS SharePoint) → folded into pm-001; CVE-2026-15409 + CVE-2026-15410 (SonicWall SMA1000) → pm-004.
- **splunk (archimedes + defenseclaw_local)** — health ping OK (Frank, Splunk 10.2.2, license OK). Sentinel tstats last 24h: archimedes 24 events, defenseclaw_local 0 (sparse, consistent with roster note). No new first-party IOCs to hunt this window (Patch Tuesday zero-days ship without published IOCs). First-party clean.

Not re-queried this sweep (FLASH/pre-brief scope + known state; no in-window lead required them): cisa-advisories all.xml, nvd (no fresh non-Patch-Tuesday CVE lead requiring lastModified pivot), unit42, mstic, krebs, crowdstrike (persistently barren), sans-isc, rapid7, wired-security, shodan/virustotal (no enrichment trigger).

Stale / skipped per health rules: **mandiant** (feedburner 404 long-entrenched; direct-HTML path is the operator-pending workaround — not exercised this sweep), **msrc** (feed parse error, content reaches corpus via relays), **ars-security** (security path retired; root-feed workaround), **github-advisories** (406; per-repo GHSA fallback). No stale flips this sweep; no recovery attempts warranted (all under known-workaround states).

## Raw-signal written this sweep (8 substantive)

- pm-001 — Microsoft July 2026 Patch Tuesday: 570/622 flaws (count conflict recorded), two exploited zero-days KEV-listed same day (CVE-2026-56155 ADFS EoP, CVE-2026-56164 SharePoint EoP), one publicly-disclosed BitLocker bypass (CVE-2026-50661).
- pm-002 — Progress ShareFile zero-day CONFIRMED + patched (path traversal, SZC 5.x/6.x → 5.12.5/6.0.2; CVE reserved-unpublished). Resolution of tracked emergency-shutdown topic.
- pm-003 — Adobe ColdFusion July critical cluster (8 CVEs, Priority 1; fixed CF2025 u11 / CF2023 u22). Adjacent to tracked VT-017 (CVE-2026-48282).
- pm-004 — CISA KEV two SonicWall SMA1000 adds (CVE-2026-15409 SSRF, CVE-2026-15410 admin code injection) — active exploitation, remote-access appliance.
- pm-005 — VMware Avi Load Balancer, 7 vulns (CVE-2026-47865 critical auth bypass … CVE-2026-47871 dir traversal). No ITW per vendor. [12:00 handoff]
- pm-006 — M365 phishing kits Jalisco + OmegaLord, MFA bypass via OAuth device-code + phone capture (ReliaQuest). No atomic IOCs. [12:00 handoff]
- pm-007 — Dutch AIVD/MIVD advisory: unspecified Russian intelligence service compromising IP cameras to spy on NATO logistics + Ukraine shipments. Generic attribution preserved verbatim (Hard Rule 2). [12:00 handoff]
- pm-008 — ClaudeBleed / Claude for Chrome flaw persists across 8 releases (Manifold; latest 1.0.80). No CVE, no ITW. Tracked-topic continuation. [12:00 handoff]

## Filtered / discarded (documented, not raw-signaled)

- "Nearly 300 GitHub repos pose as legit software to push malware" (BC, Bill Toulas) — commodity infostealer, unattributed threat actor, no A&D / roster / vuln hit.
- "LastPass, Bitwarden users targeted with fake security alerts" (BC) — commodity consumer credential phishing; no A&D / roster / vuln hit. (Was noted at 12:00; does not clear Mode 1 filter — documented here.)
- "You Don't Have to Run an Exploit…" (BC) — sponsored (Picus Software). Filtered.
- "Microsoft Entra ID gets passkeys default authentication starting September" (BC) — product roadmap news, not threat intel. Filtered.
- "Microsoft releases Windows 10 KB5099539 ESU" + "Windows 11 KB5101650 & KB5099414 cumulative updates" (BC) — Patch-Tuesday delivery subsets; folded into pm-001.
- "SAP warns of critical flaws in NetWeaver and Commerce Cloud" (BC) — ANTI-NOISE; already raw-2026-07-14-am-002 + finding-2026-07-14-0002 (VT-024/025/026).
- "Synopsys Finds No Evidence of Data Breach Amid Bosch Hack Claims" (SecurityWeek) — D1R extortion claim (denied). Neither Synopsys nor Bosch on aerospace-defense.yaml watchlist; D1R not a roster actor. No hit — documented.
- "US unseals indictment against alleged operators of Russian bulletproof hosting service" (The Record — Media Land / ML Cloud, St. Petersburg) — cybercrime-infrastructure takedown; no roster actor named, no A&D, no tracked vuln. Documented (awareness only).
- "Finland issues wanted notice for hacker behind Vastaamo psychotherapy breach" (The Record) — no A&D / roster / vuln hit. Filtered.

## Notes for downstream

- Grader 16:00 queue: pm-001..pm-008 (the four 12:00-FLASH non-FLASH handoffs are now on disk as pm-005..pm-008; pm-001..pm-004 are net-new in-window Patch-Tuesday/KEV material). ClaudeBleed (pm-008), VMware Avi (pm-005), M365 kits (pm-006), Russian camera advisory (pm-007) were pre-flagged at the 12:00 sweep.
- vuln-tracker candidates surfaced: ShareFile CVE-pending watch (pm-002); ColdFusion July cluster cross-ref to VT-017 (pm-003); SonicWall SMA1000 KEV (pm-004); VMware Avi (pm-005). Patch Tuesday exploited zero-days (pm-001) are KEV-listed and A&D-structural.
- No policy violations, no credential exposure, no controlled-information triggers this sweep.
