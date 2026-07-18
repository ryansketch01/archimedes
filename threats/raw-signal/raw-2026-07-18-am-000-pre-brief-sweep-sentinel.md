---
raw_id: raw-2026-07-18-am-000
collected_at: 2026-07-18T07:35:00-04:00
run_id: pre-brief-20260718-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: multi
  source_name: "Pre-brief sweep sentinel (coverage record)"
  source_url: null
  published_at: null
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [sweep-record]
triage_tags: [sweep_sentinel, coverage_record, non_flash]
iocs_extracted: false
iocs_count: 0
text_word_count: 0
promoted: false
ttl_expires_at: 2026-10-16T07:35:00-04:00
---

# Pre-brief collection sweep — 2026-07-18 morning (07:30 EDT)

Coverage record for the 08:00 morning-brief pre-brief collection. Window:
**2026-07-17T17:30:00-04:00 → 2026-07-18T07:30:00-04:00** (~14h). The 00:00
(commit cd9acd2) and 06:00 (commit 32405b7) FLASH sweeps were both clean
(0 candidates, 0 triggers; VT-041/043 KEV deadlines quiet) and covered the
18:00–06:00 sub-window; any tracked-topic items dated before ~06:00 EDT would
have been absorbed there (none surfaced). Saturday cadence — low source volume.

## Sources queried (healthy)

| Source | Result |
|---|---|
| bleepingcomputer | RSS 200; 0 items in window (15 in feed, most recent pre-window) |
| securityweek | RSS 200; 0 items in window (10 in feed) |
| the-record | RSS 200; 0 items in window (5 in feed) |
| krebs | RSS 200; 0 items in window |
| sans-isc | RSS 200; 0 items in window |
| unit42 (feedburner) | RSS 200; 0 items in window (last activity 2026-07-17 17:56 UTC, pre-window) |
| mstic (MS Security Blog feed) | RSS 200; 0 items in window (last-modified 2026-07-17 18:39 UTC) |
| rapid7 | RSS 200; **1 item in window — raw-signaled (am-001, WordPress Core CVE-2026-63030)** |
| crowdstrike | RSS 200; 10 dateless marketing/product items (persistent barren pattern) — 0 threat-intel in window, all discarded |
| wired-security | RSS 200; 2 in-window items — both discarded (see below) |
| cisa-advisories (all.xml) | RSS 200; 0 items in window (30 in feed) |
| cisa-kev (JSON) | catalog still v2026.07.16; most-recent adds dated 2026-07-16 (VT-041 SharePoint / VT-045 / VT-046 FortiSandbox) already tracked; **0 net-new adds dated 2026-07-17 or 2026-07-18** |

## Raw-signal files written this sweep (1)

- **am-001** — Rapid7 (A, provisional) ETR on **CVE-2026-63030 "wp2shell"** —
  critical unauthenticated RCE in WordPress Core REST API batch endpoint
  (GHSA Critical / CVSS 7.5; fixed 6.9.5 / 7.0.2 / 7.1 Beta 2; no ITW, no public
  PoC yet, imminent-PoC assessment). Net-new CVE, NOT an A&D/roster/vuln-index
  hit — raw-signaled for grader adjudication as a notable net-new critical
  unauth RCE in ubiquitous software (same grader-call basis as Siemens ROX II
  am-001 2026-07-17). Possible `vuln_watch_keywords` candidate on CVE/KEV/
  exploitation escalation.

## KEV-deadline / tracked-vuln watch (quiet — no state change this window)

- **VT-043 CVE-2026-46817** (Oracle E-Business Suite / Payments unauth takeover,
  actively exploited): KEV due date **2026-07-18 (today)**. No new KEV entry,
  no exploitation-escalation reporting, no A&D-victim disclosure in window.
  Already carried in v16 index + 2026-07-16 morning brief as an UPDATE.
- **VT-041 CVE-2026-58644** (SharePoint on-prem unauth RCE, actively exploited):
  KEV due **2026-07-19**. Quiet this window (Rapid7 corroboration already
  captured 2026-07-17 pm-002).
- **VT-045 / VT-046** (Fortinet FortiSandbox OS command injection): KEV due
  **2026-07-19**. Quiet this window.
- **VT-042 LegacyHive / Nightmare Eclipse** (Windows profsvc LPE, no CVE, vendor
  silent): no CVE assignment, no MSRC advisory, no ITW in window.

## Discarded (no watchlist / roster / vuln-index match)

- Wired "Your Period Tracker Is (Probably) Spying on You" (Security News This
  Week roundup, 2026-07-18 06:30 EDT) — privacy/consumer roundup. Sub-bullet
  references "Russian cyberspies turn to infrastructure hacking" and a DHS
  breach, but as un-detailed roundup pointers with no retrievable body (Wired
  article bodies blocked via WebFetch per source-health) and no named roster
  actor / A&D / tracked CVE. Flagged for orchestrator awareness only (possible
  APT28 / Sandworm-adjacent Russian-infra angle — operator may manually retrieve
  if the topic warrants follow-up); NOT raw-signaled.
- Wired "Prompt Injection Attacks Are Thwarting AI Hacking Agents" (Ars Technica
  cross-post, 2026-07-18 05:00 EDT) — defensive AI-agent research; no A&D /
  roster / vuln nexus.
- CrowdStrike feed — 10 dateless items, all product/marketing/AI-governance
  content (persistent barren pattern); the "July 2026 Patch Tuesday" item is the
  already-covered 2026-07-14 batch, not fresh in-window. All discarded.

## Source-health note

All queried RSS/JSON sources returned 200 and parsed cleanly; no new stale flips
or recoveries this sweep. **mandiant**: feedburner RSS (`feeds.feedburner.com/Mandiant`)
retried once per the >=24h-since-stale rule — 404 again (persistent dead path;
failure_count advanced, stale state retained; direct cloud.google.com HTML path
NOT exercised this pre-brief pass — scope). **msrc** and **ars-security** carry
prior stale state (not retried this pass). No credential exposure observed. No
prohibited-query patterns. No active-recon tooling invoked (passive OSINT +
first-party feeds only). No Splunk first-party enrichment required (no new IOCs
this window).
