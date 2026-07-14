---
raw_id: raw-2026-07-14-am-000
collected_at: 2026-07-14T07:35:00-04:00
run_id: pre-brief-20260714-073000
collection_mode: pre_brief_collection
test: false
source:
  source_yaml_id: sentinel
  source_name: Pre-brief collection sentinel (coverage record)
  source_url: null
  published_at: null
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [pre-brief-coverage-record]
triage_tags: [sentinel, coverage_record, non_flash]
iocs_extracted: false
iocs_count: 0
text_word_count: 0
promoted: false
ttl_expires_at: 2026-10-12T07:35:00-04:00
---

# Pre-brief collection — 2026-07-14 07:30 EDT (feeds 08:00 morning brief)

Coverage record for the scheduled 07:30 EDT pre-brief collection. Window:
**2026-07-13T17:30 EDT → 2026-07-14T07:30 EDT** (14h). Full healthy source
set queried (broader than the FLASH-fast subset). Prior touchpoints in the
window: 18:00 FLASH (07-13), 00:00 FLASH (07-14, clean — commit 91a60d3),
06:00 FLASH (07-14, clean — commit 07d304f).

## Result — 2 net-new raw-signal files written

| raw_id | Topic | Source (grade) | Match |
|---|---|---|---|
| raw-2026-07-14-am-001 | MSTIC — ShinyHunters OAuth abuse; Storm-3138 named for June-2026 Klue compromise | MSTIC (A) | roster actor **Icarus (#025)** via the Klue incident |
| raw-2026-07-14-am-002 | SAP July-2026 Patch Day critical cluster (CVE-2026-44747 9.9 NetWeaver ABAP + CVE-2026-27690 9.1 Approuter + CVE-2026-44761 9.1 Commerce Cloud) | SecurityWeek (B) / SAP + Onapsis | vuln-tracking candidate (critical CVEs, A&D-structural ERP) |

Both are **non-FLASH** morning-brief grader-queue items (no active
exploitation asserted; MSTIC item is defensive guidance + attribution
development on an already-tracked incident).

## Sources queried (healthy set)

| Source | Result in-window (17:30 07-13 → 07:30 07-14) |
|---|---|
| bleepingcomputer (RSS) | 2 items — Windows Search cosmetic (discard, noise); US OFAC VPN/malware sanctions (= 1VPNS, already queued 00:00 + fuller 06:00; anti-noise) |
| securityweek (feedburner RSS) | 5 items — SAP critical cluster (**RAW-SIGNALED am-002**); Russian-router advisory (anti-noise, see below); Valarian funding (discard); Jscrambler NPM (already awareness-only, handed 06:00); CMMC Phase 2 suspension (already raw-2026-07-14-flash-0600-001; anti-noise) |
| the-record (RSS) | 1 item — Lidl customer-data theft via third-party provider (retail; no A&D/roster/vuln; discard) |
| mstic (microsoft security blog RSS) | 1 item — ShinyHunters OAuth abuse (**RAW-SIGNALED am-001**) |
| unit42 (feedburner RSS) | 0 items after since-filter |
| krebs (RSS) | 0 items after since-filter |
| sans-isc (RSS) | 1 item — Stormcast podcast (no threat-intel body; discard) |
| cisa-advisories (all.xml) | 0 items after since-filter |
| cisa-kev (JSON) | 0 net-new adds since 06:00; most recent dateAdded remains CVE-2008-4128 (2026-07-13, already handled as housekeeping) |
| splunk archimedes / defenseclaw_local | reachable (Splunk 10.2.2); 0 non-archimedes events + 0 tracked-IOC hits over 24h; own operational telemetry only (Hard Rule 8 — visibility-bounded null) |

Stale/excluded sources not queried this sweep: **mandiant** (feedburner 404 —
direct-HTML path operator-pending; carries prior stale state), **msrc** (feed
parse error, stale 2026-05-30), **ars-security** (security-only path retired,
stale 2026-05-09), **dragos** (blog RSS 404, prior soft-fail — CISA ICS via
all.xml remains the OT surface). No change to their status this sweep.

## Anti-noise / already-handled (NOT re-raw-signaled)

- **US + allies Russian critical-infrastructure router advisory** (SecurityWeek,
  07-14 06:51 EDT; FSB Center 16 / Berserk Bear / Static Tundra / Ghost
  Blizzard; DIB named among targeted sectors; CVE-2018-0171 + CVE-2008-4128).
  This is a B-grade relay/restatement of the joint advisory **already
  raw-signaled 07-13 (raw-2026-07-13-flash-0600-001) and already PROMOTED to
  finding-2026-07-13-0002**. Anti-noise applies — corroboration of an existing
  finding, not new signal. FSB Center 16 remains a standing `/new-actor`
  candidate (roster gap: no FSB-attributed actor tracked; operator discretion).
- **CMMC Phase 2 suspension** — already raw-2026-07-14-flash-0600-001
  (A&D-watchlist, morning-brief standing-section candidate). Not duplicated.
- **Jscrambler NPM supply-chain compromise** — already handed to the 08:00
  grader queue as awareness-only at the 06:00 sweep; fails watchlist/roster/
  vuln-index match (no A&D prime, no roster actor, no exploited critical CVE).
  Held as awareness-only, no dedicated raw-signal (consistent with 06:00 handling).
- **1VPNS / OFAC VPN+malware-provider sanctions** — queued 00:00, fuller
  writeup 06:00. Anti-noise.
- **CVE-2008-4128 KEV add** — 2008-vintage Cisco IOS CSRF, MEDIUM, EOL SOHO
  router; handled as KEV housekeeping (raw-2026-07-13-pm-003). No new KEV adds
  since. Not re-signaled.

## Discarded (no watchlist / roster / vuln-index match, per Mode 1)

Microsoft Windows Search cosmetic update; Valarian $50M funding round; Lidl
third-party customer-data theft (retail); SANS Stormcast podcast (no body).

## Policy / legal

No prohibited query patterns. No active reconnaissance (authorized-targets.yaml
not engaged). No credentials surfaced in any fetched item. All fetches passive
OSINT + first-party Splunk read. Copyright discipline observed on all
raw-signal bodies (no > 15-word verbatim quote per source).

## Source-health outcomes

- All fetched sources returned HTTP 200 and are healthy. **No new stale flips**
  and no recoveries this sweep. Per the no-substantive-change convention and the
  field-ownership rule, **no writes were made to `source-health.yaml`** —
  operator-set `notes` preserved verbatim; runtime fields unchanged (last
  substantive health touch remains 2026-07-11 15:30). The four standing stale/
  degraded sources (mandiant, msrc, ars-security, dragos) carry prior state.

## Net assessment

Modest-signal pre-brief. Standout item is the **MSTIC (A-grade) ShinyHunters
post naming Storm-3138 for the June-2026 Klue compromise** — a same-incident
attribution/label development directly implicating roster actor **Icarus
(#025)** and its standing SAT-KAC / SAT-ACH open questions (route to
actor-profiler awareness alongside the grader). Second item is the **SAP
critical CVE cluster** (CVSS 9.9 NetWeaver ABAP) as a net-new vuln-tracking
candidate. Everything else in window is anti-noise or out-of-scope. Two files
handed to the 08:00 grader; the flash-queue items (CMMC, Jscrambler, 1VPNS,
CVE-2008-4128) remain in the grader's 24h un-promoted pool.
