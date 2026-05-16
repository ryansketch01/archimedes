---
raw_id: raw-2026-05-16-flash-1130-000
collected_at: 2026-05-16T11:30:00-04:00
run_id: flash-sweep-20260516-113000
collection_mode: flash_sweep
sweep_type: on_demand
flash_sweep: true
disposition: clean
triggers_fired: 0
consecutive_dormant_splunk_sweeps: 31
source:
  source_yaml_id: archimedes-self
  source_name: "Archimedes collector — on-demand FLASH sweep sentinel"
  source_url: null
  published_at: 2026-05-16T11:30:00-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [sentinel, flash_sweep, on_demand, dedup_audit]
triage_tags: [sentinel, non_flash, dedup_audit, on_demand, splunk_self_telemetry_only]
iocs_extracted: false
iocs_count: 0
text_word_count: 380
promoted: false
ttl_expires_at: 2026-08-14T11:30:00-04:00
---

# FLASH sweep sentinel — 2026-05-16 11:30 EDT (on-demand)

Window: 2026-05-16 06:00 → 11:30 EDT (5h30m) — between scheduled 06:00 and 12:00 sweeps
Invocation: on-demand `/flash` (operator-initiated, not the 6h cadence)
Last prior sweep: 2026-05-16 06:00 EDT (clean, 0 triggers, 29th consecutive dormant non-self-telemetry Splunk sweep per commit d2560d4)
Intervening publication: 2026-05-16 08:00 morning brief (commit 3cc6118 — 30th consecutive dormant non-self-telemetry sweep noted there)
Quiet hours active: NO (11:30 EDT is well inside 09:00–21:00 active window) — any candidate would post, not queue

## Conclusion (top-line)

**Clean sweep, 0 FLASH triggers fired.** 31st consecutive dormant non-self-telemetry Splunk sweep. No carry-forward raw-signal written (all in-window items duplicate-locked against existing findings or carry-forwards already covered in morning brief 3cc6118). No quiet-hours queue activity. No critical override conditions met. Silent disposition per FLASH-POLICY.md "IF no triggers → log to splunk, exit silently."

## In-window items evaluated (and why each duplicate-locks)

Two items reached trigger evaluation; both rejected as duplicates of pre-existing finding / reject records:

1. **BleepingComputer (Bill Toulas) — Turla/Kazuar relay** (published 2026-05-16 10:15 EDT)
   - Topic: Turla / Snake-successor Kazuar P2P botnet, MSTIC-attributed
   - Disposition: **Duplicate-locked** against finding-2026-05-14-0006 (Turla/Kazuar, A1, MSTIC primary) and reject-2026-05-16-0001 (the THN relay already rejected this morning as same-day duplicate of the same MSTIC primary).
   - Anti-noise lock: `turla-kazuar-relay` topic key active since 2026-05-15 18:00 FLASH (a76b9f1). No new IOCs, no new victims, no new tradecraft — pure outlet-to-outlet relay layer on Day 2.
   - Trigger evaluation skipped (anti-noise pre-empts).

2. **The Hacker News — Kazuar relay** (published 2026-05-16 08:43 EDT)
   - Topic: same Turla/Kazuar story, THN editorial summary of MSTIC + Securelist
   - Disposition: **Duplicate-locked** — same anti-noise lock as above; THN relay was the trigger for reject-2026-05-16-0001 written by grader during morning brief promotion.
   - No new substantive content beyond what's in finding-2026-05-14-0006.

No other sources returned in-window content matching watchlist actors, watchlist CVEs, or A&D keywords. CISA KEV, vendor PSIRT pages, and primary intel-vendor RSS feeds (Mandiant, Talos, Unit 42, Securelist, Volexity, CrowdStrike) all returned 0 new in-window items.

## Splunk first-party check

Query: `index=defenseclaw_local earliest=-24h` — **0 non-self-telemetry events** in the last 24h.

This is the **31st consecutive dormant non-self-telemetry sweep**, carrying forward the streak:
- 28th: 0d1debe (2026-05-16 00:00 sweep)
- 29th: d2560d4 (2026-05-16 06:00 sweep)
- 30th: 3cc6118 (2026-05-16 08:00 morning brief)
- 31st: this sweep (2026-05-16 11:30 on-demand)

`index=archimedes` continues to show normal self-telemetry (scheduler heartbeats, operation events) — that's expected and not counted as "non-self" signal.

Streak interpretation per established practice: dormancy is itself a data point — operator's own infrastructure shows no security-relevant events; nothing on the Frank host is being scanned, exploited, or beaconing. Continues to support the Hard Rule 8 posture that first-party would beat any contradicting external claim if one arose.

## Source-health

No new failures. Pre-existing quirky paths from the 06:00 sweep persist (CISA Advisories all.xml 403, Talos RSS 404, MSRC blog feed XML parse, Google Cloud Threat Intel feed XML, Dragos feed 404, Bitdefender Business Insights feed 404, nitter.poast.org 403) — all are known-quirky/known-blocked alternate paths; A-grade primary set returned cleanly. No hard demotions proposed. No `source-health.yaml` writes needed.

## Carry-forward roster (unchanged from morning brief 3cc6118)

The active carry-forward set the next sweep / next brief inherits, all in lock against re-FLASH per anti-noise rules:

| Topic | Anti-noise lock | Source of truth |
|---|---|---|
| NGINX Rift CVE-2026-42945 PoC publication | `CVE-2026-42945` | finding-2026-05-14-0002 (updated this morning) |
| CVE-2026-42897 Exchange KEV addition | `CVE-2026-42897` | morning brief 3cc6118 + afternoon 2026-05-15 |
| CVE-2026-20182 Cisco SD-WAN KEV (T-1) | `CVE-2026-20182` | morning brief 3cc6118 + afternoon 2026-05-15 |
| Pwn2Own Berlin Day 2 Exchange chain (embargoed) | `pwn2own-day2-exchange` | morning brief 3cc6118 |
| node-ipc compromise (UNATTRIBUTED, 4-firm consensus) | `node-ipc-supply-chain` | finding-2026-05-15-0005 |
| Turla / Kazuar P2P botnet (MSTIC A1) | `turla-kazuar-relay` | finding-2026-05-14-0006 |

All locks remain active. Next FLASH eligibility for any of these requires material new development (e.g., NGINX Rift moves from PoC to active exploitation; CVE-2026-42897 named victim at a defense prime; Pwn2Own Day 2 chain embargo lifts with technical detail).

## What the next sweep (12:00 EDT scheduled) should expect

- Same carry-forward roster carries to 12:00 sweep.
- Quiet hours NOT active at 12:00 — any new trigger fire posts directly to `#flash-alerts`.
- Watch for: any vendor advisory on Pwn2Own Day 2 chain (Orange Tsai / DEVCORE Exchange chain still embargoed; vendor disclosure window 2026-07/08); any first KEV-deadline-day developments on CVE-2026-20182 (T-0 today is the federal deadline for Cisco SD-WAN); any new Turla/Kazuar primary content beyond Day 2 relay layer.
