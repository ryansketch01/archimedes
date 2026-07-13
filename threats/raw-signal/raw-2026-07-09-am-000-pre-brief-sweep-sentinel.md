---
raw_id: raw-2026-07-09-am-000
collected_at: 2026-07-09T07:34:00-04:00
run_id: pre-brief-20260709-073000
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
triage_tags: [sentinel, coverage_record, non_flash]
iocs_extracted: false
iocs_count: 0
text_word_count: 0
promoted: false
ttl_expires_at: 2026-10-07T07:34:00-04:00
test: false
---

# Pre-brief collection sweep — 2026-07-09 morning (feeds 08:00 brief)

Coverage record for the 07:30 EDT pre-brief collection. Window:
**2026-07-08T17:30 EDT → 2026-07-09T07:30 EDT** (~14h). Prior collection
touchpoints: last pre-brief 2026-07-08 15:30; last FLASH sweep 2026-07-09
06:00 (0 candidates, clean; VT-011 RoguePlanet patch captured at
flash-0600-001).

## Result

- **1 substantive raw-signal written** this sweep: `raw-2026-07-09-am-001`
  (GhostLock / CVE-2026-43499 Linux kernel root-LPE + container escape —
  non-FLASH, vuln-tracker/grader awareness candidate; n-day, no ITW).
- **0 FLASH triggers** fired.
- **First-party Splunk: clean.** No non-Archimedes events in-window;
  targeted IOC/actor/CVE keyword sweep returned 0 external hits. Trigger 3
  (first-party-ioc-hit) cannot fire on the dormant non-Archimedes stream.

## Sources queried (healthy set)

| Source | Result in-window |
|---|---|
| bleepingcomputer (RSS) | 4 items; see dispositions below |
| securityweek (RSS) | 7 items; 1 captured (GhostLock), rest filtered |
| the-record (RSS) | 0 items in-window |
| unit42 (feedburner RSS) | 0 items in-window |
| mstic (parent feed RSS) | 0 items in-window |
| cisa-advisories (all.xml RSS) | 0 new advisories in-window |
| cisa-kev (JSON) | 0 new adds; most recent still 2026-07-07 (ColdFusion / Langflow / Joomla cluster) + 2026-07-01 (MS CVE-2026-45659) |
| sans-isc (RSS) | 2 items (Stormcast podcast; Belarus guest diary) — neither matches A&D/roster/vuln; discarded |
| rapid7 (RSS) | 0 items in-window |
| krebs (RSS) | 0 items in-window |
| mandiant (direct-HTML fallback) | reachable; index items out-of-window or already-tracked (see health note) |
| splunk-archimedes / splunk-defenseclaw | clean; only archimedes-internal sourcetypes (operation 4, scheduler 9 over 14h) |

## Item dispositions (in-window, filtered)

**BleepingComputer (4):**
1. *Microsoft to retire OWA Light client in Exchange Server* (Gatlan) — product-lifecycle change, not a security finding. No CVE / exploitation. Discarded (Exchange = A&D-relevant platform but this is not a threat item).
2. *Police arrest 5,811 suspects in global anti-fraud crackdown* (Gatlan) — LE operation, 97 countries. No roster actor / A&D / vuln. Discarded.
3. *AssuranceAmerica data breach exposes 6.9M drivers* (Gatlan) — consumer-insurance breach. No A&D / actor / vuln. Discarded.
4. *Microsoft patches RoguePlanet Defender zero-day* (Gatlan) — VT-011 tracked. **DEDUPLICATED** — already captured this morning at `raw-2026-07-09-flash-0600-001` (CVE-2026-50656, VT-011 state change). See corroboration note below.

**SecurityWeek (7):**
1. *GhostLock 15-Year-Old Linux Vulnerability* (Arghire) — **CAPTURED** as `raw-2026-07-09-am-001` (CVE-2026-43499).
2. *Microsoft Patches Defender 'RoguePlanet' Vulnerability* (Kovacs, CVE-2026-50656) — VT-011. **DEDUPLICATED** — same topic as flash-0600-001. Corroboration note below.
3. *Mount Royal University confirms data stolen in ransomware attack* (Arghire) — university ransomware. No A&D / roster / vuln. Discarded.
4. *AI Coding Tools Tricked Into Hacking Developer Machine — 'GhostApproval'* (Kovacs; Wiz research) — AI-coding-assistant / dev-tooling attack technique. No named A&D victim, no tracked actor, no tracked CVE. Awareness only (see below); not raw-signaled — technique-not-compromise and no watchlist/roster/vuln match.
5. *Chrome 150 patches 27 vulnerabilities* (Arghire) — routine browser patch (13 UAF, 2 critical). No tracked-vuln / A&D / active-exploitation. Discarded.
6. *8Layers raises $2.9M* (Arghire) — funding/business news. Discarded.
7. *Unpatched backdoor in Tenda firmware (CVE-2026-11405)* (Arghire) — consumer router. No A&D / roster / vuln-index match. Discarded.

**SANS ISC (2):** Stormcast podcast (awareness-only, no body); "HELP ME ESCAPE FROM BELARUS" guest diary — neither matches A&D / roster / vuln. Discarded.

## Anti-noise / corroboration note (RoguePlanet CVE-2026-50656 / VT-011)

The RoguePlanet Defender patch (CVE-2026-50656) was already raw-signaled at
`raw-2026-07-09-flash-0600-001` (BleepingComputer, Gatlan, ~01:42 EDT). This
pre-brief window surfaced **two additional in-window corroborating relays** the
grader can use for the morning brief without a duplicate raw-signal:
- SecurityWeek (Eduard Kovacs) — confirms CVE-2026-50656, Microsoft Malware
  Protection Engine update, "Chaotic Eclipse" series framing.
- BleepingComputer (Sergiu Gatlan) — same patch, post-June-Patch-Tuesday
  disclosure framing.
Per one-topic-per-24h anti-noise, no new raw-signal created; flagged here so
the grader sees the corroboration trail for VT-011's state transition
(unpatched → patched, CVE now assigned).

## Awareness items (out-of-scope for raw-signal; orchestrator/analyst discretion)

1. **GhostApproval (Wiz Research, via SecurityWeek/Kovacs)** — new AI-coding-assistant attack technique tricking AI coding tools into compromising the developer machine via a "decades-old technique." Dev-tooling supply-chain adjacency to the corpus's recurring theme (VT-006 Mini Shai-Hulud, VT-009 Nx Console). No named A&D victim / no tracked actor / no tracked CVE at this surface — not raw-signaled. Flag: if a follow-on report names a specific compromise or A&D-adjacent SDLC exposure, revisit.
2. **Mandiant index (direct-HTML)** — item "Public and Private Medical Community Targeted by China-Nexus Threat Actor Pursuing AI, Cyber, Medical, and National Defense Research" mentions *national defense research* targeting (A&D-adjacent). **Could not confirm in-window** from the undated index; the Mandiant index persistently displays out-of-window posts. Not raw-signaled per pre-brief scope discipline. Recommend orchestrator/analyst date-triangulate (WebSearch) if the China-nexus national-defense-research angle warrants follow-up. Other index items either out-of-window or already tracked (CVE-2026-20245 Cisco SD-WAN = VT-015; ShinyHunters PeopleSoft; Turla STOCKSTAY).

## Source-health changes proposed (runtime fields only; operator `notes` preserved verbatim)

- **mandiant** — RSS/feedburner path 404 again (Nth consecutive; retried once per >=24h-since-stale rule). `cloud.google.com/blog/topics/threat-intelligence` direct-HTML path SUCCEEDED again. Recommend: keep `status: stale` (canonical RSS path still broken), advance `failure_count`, update `last_attempt: 2026-07-09T07:30`, append direct-HTML-success observation to `last_error`. Canonical-swap operator decision still pending after many consecutive direct-HTML successes vs RSS-path failure.
- **cisa-kev, cisa-advisories, securityweek, bleepingcomputer, the-record, unit42, mstic, sans-isc, rapid7, krebs** — all fetched cleanly; set `status: healthy`, `failure_count: 0`, `last_successful_fetch: 2026-07-09T07:30`, `last_error: null`. Preserve each entry's operator `notes` verbatim.
- **splunk-archimedes, splunk-defenseclaw** — reachable; only Archimedes-internal sourcetypes; `status: healthy`, `last_successful_fetch: 2026-07-09T07:30`.
- No new stale flips this sweep. Previously-stale infra sources (msrc, ars-security, censys, urlscan, hibp, threatfox/malwarebazaar MCP-pending, x-cisagov, x-gossithedog) not re-tested — outside productive pre-brief scope; carry prior state.
