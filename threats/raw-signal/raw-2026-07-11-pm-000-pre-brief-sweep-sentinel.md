---
raw_id: raw-2026-07-11-pm-000
collected_at: 2026-07-11T15:36:00-04:00
run_id: pre-brief-20260711-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: sentinel
  source_name: Pre-brief sweep sentinel (coverage record)
  source_url: null
  published_at: null
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [sweep-coverage-record]
triage_tags: [sentinel, coverage_record, non_flash, clean_sweep]
iocs_extracted: false
iocs_count: 0
text_word_count: 0
promoted: false
ttl_expires_at: 2026-10-09T15:36:00-04:00
test: false
---

# Pre-brief collection sweep — 2026-07-11 afternoon (feeds 16:00 brief)

Coverage record for the 15:30 EDT afternoon pre-brief collection. Window:
**2026-07-11T07:30 EDT → 2026-07-11T15:30 EDT** (~8h since the morning collection;
14h lookback to ~2026-07-11T01:30 EDT applied for safety per doctrine). Prior
collection touchpoints: last pre-brief 2026-07-11 07:30 (morning brief published
2026-07-11 — quiet cycle, 0 net-new findings; ColdFusion CVE-2026-48282 BOD 22-01
deadline lapsed 07-10 UPDATE, per commit dd475c3); last FLASH sweep 2026-07-11 12:00
(0 candidates, clean — CISA KEV no new adds, Splunk 0 IOC hits, in-window ACSC
CMS-exploitation campaign dispositioned commodity/no-A&D-nexus/no-attribution and
absorbed under one-topic-per-24h, per commit 9681627).

## Result

- **0 substantive raw-signal written** this sweep. No in-window item survives the
  A&D-watchlist / roster / vuln-index filter (Mode 1 procedure).
- **0 FLASH triggers** fired. All in-window items are commodity / non-tracked /
  no-A&D-nexus, or already dispositioned (anti-noise).
- **First-party Splunk: clean.** 0 non-Archimedes events in both `archimedes` and
  `defenseclaw_local` over 24h (`NOT sourcetype=archimedes:*` → 0). Targeted keyword
  sweep across tracked CVEs + roster actors returned 4 hits — ALL
  `archimedes:brief` / `archimedes:operation` pipeline self-references (own
  brief-cycle logs matching CVE/actor tokens in payloads), 0 `defenseclaw_local`,
  0 external observations. Trigger 3 (first-party-ioc-hit) cannot fire on the
  dormant non-Archimedes stream.
- **CISA KEV: no new adds.** Most recent `dateAdded` remains 2026-07-10 (Balbooa
  Forms CVE-2026-56291 + iCagenda CVE-2026-48939 — already captured as
  `raw-2026-07-11-am-001`). Zero 07-11 adds.

## Sources queried (healthy set)

| Source | Result in-window |
|---|---|
| bleepingcomputer (RSS) | 2 items; both dispositioned — ACSC CMS campaign (anti-noise, already handled 12:00 FLASH); Ghostcommit (anti-noise, already handled am-000) |
| securityweek (RSS) | 1 item; discarded (GitHub ghost-account recon — no roster/vuln/A&D hit) |
| the-record (RSS) | 0 items in-window |
| unit42 (feedburner RSS) | 0 items in-window (The Gentlemen ransomware was pre-window / am-000) |
| mstic (parent feed RSS) | 0 items in-window (feed last_modified 2026-07-10 21:42 UTC) |
| cisco-talos (RSS) | 0 items in-window |
| cisa-kev (JSON) | 0 new adds since morning; most recent dateAdded = 2026-07-10 (am-001 pair); no 07-11 adds |
| cisa-advisories (all.xml) | 0 items in-window |
| sans-isc (RSS) | 1 item; discarded (Wireshark 4.6.7 — anti-noise, already handled am-000) |
| krebs (RSS) | 0 items in-window (feed last_modified 2026-07-09 13:52 UTC) |
| splunk-archimedes / splunk-defenseclaw | clean; 0 non-Archimedes events in 24h; targeted sweep = 4 archimedes-internal self-references only |

## Item dispositions (in-window, filtered)

**BleepingComputer (2):**
1. *Australia warns of global campaign targeting vulnerable CMS platforms* (Bill
   Toulas, 2026-07-11 10:18 EDT) — ACSC alert on a global exploitation campaign
   against vulnerable CMS platforms and plugins. Same topic already dispositioned
   at the 2026-07-11 12:00 FLASH sweep (commodity / no-A&D-nexus / no-attribution,
   absorbed under one-topic-per-24h per commit 9681627). No named CVE, no roster
   actor, no A&D prime. **Discarded** per Mode 1 + anti-noise. BleepingComputer
   relay corroborates the prior 12:00 disposition.
2. *'Ghostcommit' hides prompt injection in images to fool AI agents, steal
   secrets* (Ax Sharma, 2026-07-11 05:03 EDT) — already dispositioned in
   `raw-2026-07-11-am-000` (morning sweep). Pre-window for this afternoon window;
   **anti-noise applies.**

**SecurityWeek (1):**
1. *Ghost Accounts Abuse GitHub API in Mass Recon Campaign* (Ionut Arghire,
   2026-07-11 13:30 EDT) — Datadog research: 50+ dormant "ghost" GitHub accounts
   (registered 2-5 years ago) enumerating repositories and members via public
   GitHub API endpoints; some cases showed private-repo data exfiltration.
   WebFetch confirmed: **no threat actor named/attributed, no CVEs, no A&D or
   other victims named, no IOCs (usernames/domains/IPs/hashes), no sectors
   specified.** Fails all three filters (A&D / roster / vuln-index).
   **Discarded** per Mode 1. Awareness only: extends the recurring
   GitHub / dev-supply-chain reconnaissance theme (adjacent to the am-000
   Ghostcommit item and the prior GitHub-org-breach corpus surfaces).

**SANS ISC (1):** *Wireshark 4.6.7 Released* (2026-07-11 05:07 EDT) — already
dispositioned in `raw-2026-07-11-am-000` (tool release, 12 vulns fixed). Pre-window
for this afternoon; **anti-noise applies.**

## Awareness items (out-of-scope for raw-signal; orchestrator/analyst discretion)

1. **GitHub ghost-account API recon campaign (SecurityWeek / Arghire; Datadog
   research)** — dormant-account reconnaissance mapping GitHub orgs/repos/members,
   with some private-repo exfiltration. No actor, no CVE, no A&D victim, no IOCs
   at surface. Continues the GitHub / dev-supply-chain reconnaissance theme that
   also produced Ghostcommit (07-11 am) and the recurring GitHub-org-breach
   thread. Revisit if a downstream report names an A&D-adjacent org, a tracked
   actor, or publishes IOCs. Not raw-signaled (no A&D / roster / vuln hit).
2. **ACSC global CMS-exploitation campaign (BleepingComputer / Toulas)** — already
   dispositioned at 12:00 FLASH; commodity mass-CMS exploitation, no A&D nexus,
   no attribution. Carried here only for coverage completeness. Revisit if
   attribution or an A&D/DIB victim surfaces.

## FLASH-eligibility / A&D-relevance assessment

- **FLASH-eligible: none.** No item meets any of the 6 FLASH triggers. No critical
  CVE with active exploitation net-new (KEV static since 07-10), no new attribution
  to a tracked actor, no first-party IOC hit (Splunk dormant), no tracked-actor TTP
  change, no A&D-sector campaign, no zero-day-without-patch.
- **A&D-relevant: none.** No watchlist prime (Lockheed / Boeing / RTX / Northrop /
  GD / BAE / L3Harris / Leidos / SAIC / Thales / GE Aerospace / Safran / Honeywell /
  Airbus / Elbit) named in any in-window item.
- **Net assessment:** clean afternoon sweep, consistent with the recently-quiet
  cycle (morning was 0 net-new findings). No signal manufactured.

## Source-health changes proposed (runtime fields only; operator `notes` preserved verbatim)

- **bleepingcomputer, securityweek, the-record, unit42, mstic, cisco-talos,
  cisa-advisories, cisa-kev, sans-isc, krebs** — all fetched cleanly (HTTP 200);
  set `status: healthy`, `failure_count: 0`,
  `last_successful_fetch: 2026-07-11T15:30:00-04:00`, `last_error: null`.
  Preserve each entry's operator `notes` verbatim.
- **splunk-archimedes, splunk-defenseclaw** — reachable; only Archimedes-internal
  sourcetypes; `status: healthy`, `last_successful_fetch: 2026-07-11T15:30:00-04:00`.
- **mandiant** — not re-fetched this sweep (RSS-path persistent 404 pattern;
  direct-HTML fallback cadence multi-day). Carry prior `stale` state; operator
  canonical-swap decision still pending.
- No new stale flips this sweep. Previously-stale sources (msrc, ars-security,
  censys, urlscan, hibp, x-cisagov, x-gossithedog, threatfox/malwarebazaar
  MCP-pending) not re-tested — outside productive pre-brief scope; carry prior state.
