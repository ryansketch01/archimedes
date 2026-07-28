---
raw_id: raw-2026-07-28-flash-0000-000
collected_at: 2026-07-28T00:06:00-04:00
run_id: flash-sweep-20260728-000000
collection_mode: flash_sweep
source:
  source_yaml_id: multiple
  source_name: "FLASH alert sweep coverage sentinel (00:00 EDT)"
  source_url: null
  published_at: null
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: [CVE-2026-16812, CVE-2025-68686, CVE-2026-16723]
  keywords: [flash_sweep, coverage_record, continuing_coverage]
triage_tags: [flash_sweep, coverage_record, non_flash, deduplicated, continuing_coverage]
iocs_extracted: true
iocs_count: 3
text_word_count: 720
promoted: false
ttl_expires_at: 2026-10-26T00:06:00-04:00
---

# FLASH alert sweep coverage record — 2026-07-28 00:00 EDT

**Outcome: CLEAN for net-new FLASH candidates — 0 candidates, 0 net-new triggers.**

Window: ~2026-07-27T18:00 → 2026-07-28T00:00 EDT (6h overnight). Prior sweep of record:
2026-07-27 18:00 FLASH (clean, 0 candidates, commit 1c2407a). Quiet-hours active (00:00
outside 09:00–21:00 EDT) — no FLASH would post even if triggered; any candidate would
queue.

Two in-window items surfaced, but **both are continuing-coverage of topics already
handled in the 2026-07-27 afternoon brief / today's VT-052 build** → anti-noise "one
FLASH per trigger topic per 24h" applies → deduplicated, NOT net-new candidates.

## Sources queried (healthy set, FLASH-fast scope)

RSS/media (all HTTP 200):
- **bleepingcomputer** — 2 in-window (15 in feed; last_modified 2026-07-28T03:59 GMT).
  Both continuing-coverage (see below).
- **the-record** — 0 in-window (5 in feed)
- **securityweek** — 1 in-window (10 in feed): "For Some, So-Called 'Skynet Day' Came too
  Close to Sci-Fi After a Rogue Agent Hacked Into a Startup" (AP, 2026-07-28T02:28Z).
  Rogue-AI-agent incident story; NO tracked actor / NO CVE / NO A&D entity. DISCARDED per
  Mode 2 (no watchlist/roster/vuln hit).
- **sans-isc** (rssfeed.xml) — 1 in-window: ISC Stormcast podcast (2026-07-28T02:00Z,
  awareness-only, no body). DISCARDED. **RECOVERED** from 2026-07-27 18:00 transient
  parse error (see Source health).
- **unit42** (feedburner) — 0 in-window (15 in feed)
- **mstic** (parent feed) — 0 in-window (10 in feed)

## Continuing-coverage items (in-window, deduplicated — grader/vuln-tracker fold-in)

1. **BleepingComputer — "Hackers target US firms in FastJson RCE zero-day attacks"**
   (Bill Toulas, 2026-07-27T23:49Z). CVE-2026-16723, Alibaba FastJson 1.x
   (1.2.68–1.2.83) unauth default-config deserialization RCE. **Already tracked as
   VT-052** (vuln-index v26, built today 2026-07-27). Fresh B-grade media surface; NO new
   state change — still attempts/scanning observed per ThreatBook + Imperva vendor
   telemetry (compromise UNCONFIRMED), NO patch for 1.x (Alibaba: 1.x unmaintained),
   NO actor (Hard Rule 2), named sectors finance/healthcare/computing/retail (NOT A&D),
   NO A&D victim. Trigger 1 marginal-fail (exploitation is attempts-observed via B-grade
   relay, not confirmed active exploitation from an A-grade source; CVSS 9.0). Trigger 6
   marginal-fail (same A-grade-source / confirmed-exploitation qualifier). Anti-noise:
   same topic tracked <24h.

2. **BleepingComputer — "Arista patches VeloCloud Orchestrator zero-day exploited in
   attacks"** (Lawrence Abrams, 2026-07-27T22:49Z). CVE-2026-16812, VeloCloud
   Orchestrator (on-prem) unauth OS command injection, **CVSS 10.0**, confirmed active
   exploitation, CISA KEV-listed (dateAdded 2026-07-27, due 2026-07-30). **Already
   covered in the 2026-07-27 afternoon brief** (net-new KEV add) and raw-signaled at
   raw-2026-07-27-pm-003. This is the vendor-patch follow-up (fix released 2026-07-27:
   5.2.3.14 / 6.1.3.4 / 6.4.2.4 / 7.0.0.1+). NO actor, NO named victim. On the merits
   this item meets Trigger 1 (CVSS 10.0 + confirmed exploitation + A-grade CISA KEV),
   but anti-noise dedup applies — same topic FLASH-worthy but already carried in the
   16:00 brief cycle. **NET-NEW datum for vuln-tracker:** 3 attacker source IPs published
   in the advisory (below) — fold into the CVE-2026-16812 dossier as HUNT-not-block
   unattributed indicators.

## IOCs (net-new, for vuln-tracker fold-in to CVE-2026-16812)

```yaml
network_iocs:
  - value: 8.19.75.217
    type: ipv4
    role: reported_attacker_source_ip
    context: "Arista advisory — source IP observed in CVE-2026-16812 VeloCloud Orchestrator exploitation. Role (spray-source vs C2) unstated. HUNT-not-block."
    attribution: none            # Hard Rule 2 — no actor named
    first_party_splunk_hits_24h: 0
  - value: 206.72.242.124
    type: ipv4
    role: reported_attacker_source_ip
    context: "Arista advisory — CVE-2026-16812 exploitation source IP. HUNT-not-block."
    attribution: none
    first_party_splunk_hits_24h: 0
  - value: 206.72.242.162
    type: ipv4
    role: reported_attacker_source_ip
    context: "Arista advisory — CVE-2026-16812 exploitation source IP. HUNT-not-block."
    attribution: none
    first_party_splunk_hits_24h: 0
attribution_claims: []           # no source attributed CVE-2026-16812 or CVE-2026-16723 to any actor
credentials_observed: 0
```

## Authoritative CVE / KEV surface

- **cisa-kev** (KEV JSON directly fetched, catalog v2026.07.27, 1,655 entries): two adds
  dated **2026-07-27** — CVE-2025-68686 (Fortinet FortiOS, due 2026-08-10) and
  CVE-2026-16812 (Arista VeloCloud, due 2026-07-30). **Both already covered in the
  2026-07-27 afternoon brief** (raw-2026-07-27-pm-002 + pm-003). NO entries dated
  2026-07-28. No KEV delta this window.

## First-party (Splunk, Frank)

- Sentinel `(index=archimedes OR index=defenseclaw_local) NOT sourcetype=archimedes:*`
  over -24h → **0 events**, both indexes. tstats -6h → only archimedes:operation (1) +
  archimedes:scheduler (3), all internal.
- Targeted IOC sweep on the 3 Arista attacker IPs + CVE-2026-16812 / CVE-2026-16723 /
  CVE-2025-68686 + fastjson/velocloud over -24h → **0 hits**. Trigger 3 cannot fire.

## FLASH trigger evaluation

- **Trigger 1 (critical-CVE-exploited):** Arista CVE-2026-16812 meets merits (10.0 + KEV
  confirmed exploitation) but DEDUPLICATED (carried in 16:00 brief). FastJson
  CVE-2026-16723 marginal-fail (attempts-observed / B-grade relay, not A-grade confirmed).
- **Trigger 2 (tracked-actor attribution):** none. No actor named on any in-window item.
- **Trigger 3 (first-party IOC hit):** 0 Splunk hits.
- **Trigger 4 (actor TTP change):** none.
- **Trigger 5 (A&D-sector campaign):** none — FastJson sectors are finance/healthcare/
  computing/retail, no A&D victim; Arista no named victim.
- **Trigger 6 (zero-day no-patch):** FastJson CVE-2026-16723 IS an unpatched zero-day
  (9.0, widely-deployed), but exploitation is attempts-observed via B-grade telemetry,
  not confirmed/imminent per an A-grade source → marginal-fail. Already tracked VT-052.

Net: **0 net-new FLASH candidates.**

## Source health

- **sans-isc RECOVERED** — rssfeed.xml returned HTTP 200 valid RSS this sweep (the
  2026-07-27 18:00 transient XML parse error cleared, consistent with the documented
  transient pattern). Runtime update: `failure_count` 1→0, `last_successful_fetch`
  2026-07-28T00:06, `last_error` cleared, `status` remains healthy.
- All other queried RSS/media/KEV/Splunk sources HTTP 200 and remain `healthy`; no flips.
- Stale sources (mandiant, msrc, ars-security, censys, urlscan, hibp, threatfox/
  malwarebazaar WebFetch-auth, x-cisagov, x-gossithedog) NOT retried per FLASH-fast
  <24h discipline; carry prior stale state.

---

## Extraction notes

- Language: en
- Article types: blog (BleepingComputer x2), news (SecurityWeek AP), podcast (SANS ISC)
- Raw IOC extraction invoked: yes (3 net-new Arista attacker IPs; no credentials observed)
- All in-window matches are continuing-coverage of already-tracked/already-briefed topics;
  no net-new promotion-worthy signal for FLASH. Grader/vuln-tracker action limited to
  folding the 3 Arista IPs into the CVE-2026-16812 dossier at the next scheduled brief.
