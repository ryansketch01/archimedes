---
raw_id: raw-2026-07-13-pm-000-pre-brief-sweep-sentinel
collected_at: 2026-07-13T15:33:00-04:00
run_id: pre-brief-20260713-153000
collection_mode: pre_brief_collection
test: false
sweep_window_start: 2026-07-13T07:30:00-04:00
sweep_window_end: 2026-07-13T15:30:00-04:00
source:
  source_yaml_id: multiple
  source_name: Pre-brief collection sweep sentinel (multi-source)
  source_url: null
  published_at: 2026-07-13T15:30:00-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [pre-brief-coverage-record]
triage_tags: [pre_brief_sentinel, coverage_record, non_flash]
iocs_extracted: false
iocs_count: 0
text_word_count: 0
promoted: false
ttl_expires_at: 2026-10-11T15:33:00-04:00
---

# Pre-brief collection sweep — 15:30 EDT 2026-07-13 (feeds 16:00 afternoon brief)

Coverage record for the PM pre-brief collection. Window:
**2026-07-13T07:30 → 2026-07-13T15:30 EDT (8h).** Prior in-window touchpoint that
already swept the 07:30→12:00 portion: the 12:00 FLASH sweep (0 FLASH candidates;
routed 3 in-window non-FLASH items to the 16:00 grader queue — EU/UK GRU sanctions
[already raw-2026-07-13-am-001], RabbitMQ OAuth takeover, Zimbra critical RCE).

## Result — 3 substantive items raw-signaled this sweep

- **raw-2026-07-13-pm-001** — RabbitMQ CVE-2026-5721 (CVSS 8.7) unauthenticated
  OAuth client-secret disclosure → broker takeover; secondary CVE-2026-57221
  (5.3). Patch available; no ITW; disclosed by Miggo. This is the "RabbitMQ OAuth
  takeover" the 12:00 FLASH routed to the 16:00 grader queue. NON-FLASH.
  Widely-deployed enterprise middleware; A&D relevance STRUCTURAL (no prime named).
- **raw-2026-07-13-pm-002** — CISA active-exploitation warning on Joomla iCagenda
  (CVE-2026-48939) + Balbooa Forms (CVE-2026-56291) arbitrary-file-upload RCE.
  **Vuln-index match: tracked VT-020 + VT-021.** Fresh active-exploitation
  reporting detail (iCagenda exploited hours before June-16 patch; Balbooa zero-day
  since July 8). Dedup relationship to the 07-10/07-11 KEV coverage — surfaced here
  for vuln-tracker state-fold, NOT re-litigation. NON-FLASH.
- **raw-2026-07-13-pm-003** — CISA KEV addition CVE-2008-4128 (Cisco IOS 12.4
  multiple CSRF). Fresh KEV add; catalog version bumped 2026.07.10 → 2026.07.13.
  Legacy CVE (2008), CSRF class; low modern criticality but a genuine in-window KEV
  signal (explicit collection priority). NON-FLASH; vuln-tracker awareness.

## Sources queried (healthy set)

| Source | Grade | In-window result (07:30→15:30) |
|---|---|---|
| bleepingcomputer (RSS) | B | 5 items: Joomla active-exploit (→ **pm-002**, vuln-index match); CrashStealer macOS infostealer (discarded — commodity, no A&D/roster/vuln); Lidl retail breach (discarded — non-A&D); Varonis Entra CTF (discarded — sponsored); UK NCA charges vs Russian Coms spoofing platform (discarded — cybercrime LE, no roster/A&D). |
| securityweek (RSS) | B(prov) | 3 items: RabbitMQ CVE-2026-5721 (→ **pm-001**); GhostExodus hacker-conversation profile (discarded — no fresh intel); Cyber M&A June roundup (discarded — business news). |
| the-record (RSS) | A(vendor) | 2 items: US Treasury sanctions First VPN Service (1VPNS) + Ukrainian admin + Belarusian cryptor dev (discarded — ransomware-adjacent sanctions/LE, no roster actor named, no A&D); Ksenia Sobchak Telegram-channel breach (discarded — no A&D/roster/vuln). |
| cisa-kev (JSON) | A | **1 new add** in window: CVE-2008-4128 (Cisco IOS 12.4 CSRF), dateAdded 2026-07-13; catalogVersion 2026.07.13 → **raw-signaled pm-003**. |
| splunk archimedes / defenseclaw_local | first-party | Reachable. Over -9h: only Archimedes' OWN operational telemetry (archimedes:operation ×5, archimedes:scheduler ×7); defenseclaw_local 0 events. Zero tracked-IOC hits (Trigger 3 clean). Hard Rule 8 — silent first-party does not disconfirm anything. |
| unit42, mstic, the-record(vendor blog), sans-isc, krebs, cisa-advisories | A/B | Not separately productive this narrow PM window; media RSS (bc/sw/record) carried the in-window load. cisa-advisories all.xml: 0 new in-window ICS/advisory items beyond KEV JSON delta above. |

## Discarded (noted, not promoted)

- **BleepingComputer — CrashStealer (macOS infostealer posing as Apple crash
  reporter, Bill Toulas).** Commodity credential/keychain/wallet stealer. No
  roster actor, no A&D prime, no tracked CVE. Discarded per Mode 1.
- **BleepingComputer — Lidl online-shop breach via service provider.** Retail /
  consumer-PII breach. Non-A&D. Discarded.
- **BleepingComputer — UK charges 5 linked to "Russian Coms" caller-ID spoofing
  platform (NCA).** Cybercrime LE action; Russia-nexus but no roster actor,
  no A&D nexus, no vuln. Discarded (noted: Russia-cyber thematic cluster with the
  morning's EU/UK sanctions, distinct event).
- **The Record — US Treasury sanctions First VPN Service (1VPNS) + Ukrainian admin
  + Belarusian cryptor developer.** Ransomware-enabling-infrastructure sanctions.
  Ransomware watch is not an active standing section; no roster actor named
  (ransomware groups referenced generically). Discarded (noted: parallels the
  morning EU/UK sanctions theme; sanctions/LE action, no A&D anchor).
- **The Record — Ksenia Sobchak Telegram-channel breach.** Russian-journalist
  account compromise / info-op. No A&D, no roster, no vuln. Discarded.
- **SecurityWeek — GhostExodus (Jesse McGraw) hacker-conversation profile;
  Cyber M&A June roundup.** Non-threat-intel editorial/business. Discarded.
- **Zimbra critical RCE (12:00-FLASH grader-queue reference, AM-discarded).**
  Re-checked: no fresh SecurityWeek/BleepingComputer in-window item beyond the
  07-13 06:03 EDT SecurityWeek piece already dispositioned this morning
  (raw-2026-07-13-am-000). No CVE assigned in the relay; not a tracked vuln; no
  actor; no A&D prime. Held out per collector discipline — awareness flag stands
  for grader/vuln-tracker if a CVE + exploitation/KEV surfaces. Not re-signaled
  (anti-noise; already logged AM).

## Source-health outcomes

**Healthy sources fetched this sweep returned HTTP 200; no new stale flips.**
Per instruction, runtime-field updates are REPORTED here for the orchestrator to
apply to `source-health.yaml`; operator `notes` fields preserved verbatim (not
touched by collector). Observations:

- **bleepingcomputer, securityweek, the-record, cisa-kev (JSON), cisa-advisories
  (all.xml), splunk-archimedes, splunk-defenseclaw** — all healthy / reachable
  this sweep. Recommend `last_successful_fetch` → 2026-07-13T15:30-04:00 for the
  sources actually fetched; `failure_count` 0.
- **Stale sources (unchanged, not thrashed):** mandiant (feedburner 404,
  direct-HTML path operator-pending); msrc (feed parse error, stale 2026-05-30);
  ars-security (security-only feed retired, stale 2026-05-09; root-feed workaround
  not swept). dragos (blog feed 404, 1 failure; held healthy, not swept — cadence
  multi-day). None hit the ≥24h-retry-once threshold in a state-changing way.

## Net assessment

Quiet-to-moderate PM window. One net-new critical enterprise-infra vuln
(RabbitMQ pre-auth OAuth-secret disclosure, patch available) and one KEV-tracked
active-exploitation update (Joomla VT-020/VT-021), plus a legacy Cisco IOS KEV
backfill add. No roster-actor activity in-window (the day's roster relevance —
Sandworm sanctions — landed in the AM brief). No FLASH-class triggers: RabbitMQ is
below the 9.0 active-exploitation floor with a patch out; Joomla is already tracked
and KEV-listed; the Cisco KEV add is a 2008 CSRF. No signal manufactured;
disciplined discards logged.
