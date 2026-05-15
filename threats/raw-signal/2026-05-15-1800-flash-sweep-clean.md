---
raw_id: 2026-05-15-1800-flash-sweep-clean
collected_at: 2026-05-15T18:05:00-04:00
run_id: flash-sweep-20260515-180000
collection_mode: flash_sweep
disposition: silent_exit_clean_sweep
sweep_window:
  start: 2026-05-15T12:00:00-04:00
  end: 2026-05-15T18:00:00-04:00
  hours: 6
quiet_hours_active: false        # 18:00 EDT is within active hours 09:00-21:00
sources_queried: 15
sources_skipped_stale: 7
items_fetched_in_window: 7
items_matching_watchlists_or_actors: 1     # only the MSTIC/THN Turla item; node-ipc + Pwn2Own + Funnel Builder + Exchange Pwn2Own all anti-noise-deduplicated against earlier today
items_promoted_to_raw_signal: 1            # the MSTIC/Turla awareness item (raw-2026-05-15-flash-1800-001)
flash_candidates: 0
flash_candidates_list: []
critical_override_applied: false
hard_rule_8_dormant_streak_consecutive_sweeps: 27   # 27th consecutive dormant non-self-telemetry sweep (matches 12:00 +1)
---

# 2026-05-15 18:00 EDT FLASH sweep — clean (0 triggers)

## Disposition

Zero FLASH triggers fired across 15 queryable sources in the 12:00-18:00 EDT window. Silent exit per FLASH-POLICY anti-noise rules. One in-window raw-signal written for awareness (MSTIC/Turla — does not fire any trigger; non-FLASH operator-action item for morning brief + `/new-actor Turla` candidate).

## Trigger evaluation summary

| Trigger | Fired | Reason |
|---|---|---|
| T1 critical-cve-exploited | no | Funnel Builder WordPress (Sansec, 40K installs, actively exploited) has no CVE assigned and Sansec is unrated in source-grades.yaml — fails A-grade requirement. Exchange CVE-2026-42897 anti-noise lock active to 2026-05-16 06:00 EDT (24h since 06:00 FLASH). |
| T2 tracked-actor-attribution | no | MSTIC Turla / Secret Blizzard / Kazuar surface (genuinely material, definitive FSB Center 16 attribution, A-grade source) but Turla is NOT in _roster.yaml — fails tracked-actor precondition. Operator-action: `/new-actor Turla` candidate. |
| T3 first-party-ioc-hit | no | Splunk -24h sweep zero hits across tracked-IOC corpus and zero hits in defenseclaw_local. 27th consecutive dormant non-self-telemetry sweep. |
| T4 tracked-actor-ttp-change | no | MSTIC Kazuar architectural evolution (modular P2P + EWS C2 + leader election + Protobuf + working-hours blackout) is genuinely a NEW capability tier — but T4 requires attributable_actor in _roster.yaml (per flash-policy.yaml line 67). Turla untracked. |
| T5 active-ad-campaign | no | MSTIC names "government and diplomatic sector in Europe and Central Asia, as well as systems in Ukraine" — NO A&D-prime, NO Tier-1/2 supplier, NO ITAR entity, NO US-government-contractor victim. THORChain $10.7M crypto theft (The Record relay, no actor named, no A&D angle). |
| T6 zero-day-no-patch | no | Pwn2Own Berlin Day 2 Exchange chain (Orange Tsai/DEVCORE) anti-noise lock active to 2026-05-16 16:00 EDT (24h since 16:00 afternoon brief coverage). All Day 2 Pwn2Own zero-days remain under standard 90-day vendor embargo. Funnel Builder WordPress flaw is patched (FunnelKit 3.15.0.3 released 2026-05-14) — patch_available is true, fails T6. |

## Active anti-noise locks (rolled forward to this sweep)

| Topic | Lock until |
|---|---|
| exchange-cve-2026-42897 | 2026-05-16T06:00:00-04:00 |
| teampcp-shai-hulud-release | 2026-05-16T06:00:00-04:00 |
| teampcp-mistral-450-repos | 2026-05-16T08:00:00-04:00 |
| cisco-sd-wan-cve-2026-20182 | 2026-05-16T08:00:00-04:00 |
| copy-fail-kev-eod-deadline | 2026-05-16T08:00:00-04:00 |
| node-ipc-four-firm-consensus | 2026-05-16T16:00:00-04:00 |
| pwn2own-berlin-day2-exchange-chain | 2026-05-16T16:00:00-04:00 |

## In-window non-FLASH awareness items (handed forward to morning brief)

1. **MSTIC: Turla / Secret Blizzard Kazuar P2P-botnet evolution** — see `raw-2026-05-15-flash-1800-001-mstic-turla-secret-blizzard-kazuar-p2p-botnet-evolution.md`. A-grade primary, four published SHA-256 IOCs, EWS-over-Exchange-mailbox C2 channel intersects this week's Exchange-on-prem exposure pattern. `/new-actor Turla` operator candidate. Promote as Layer 1 ICYMI item in morning brief.

## Source health observations (this sweep)

- **Splunk**: reachable, version 10.2.2, license OK. defenseclaw_local index zero events in -24h (27th consecutive dormant non-self-telemetry sweep — this is environmental, not a Splunk failure).
- **Healthy**: bleepingcomputer (3 in-window items), thehackernews (1 in-window item), therecord (1 in-window item), securityweek (0 in-window items), cisa-kev (1 entry corroborating CVE-2026-42897 already covered), cisa-advisories (0 in-window items).
- **Single-observation parse failure this sweep**: msrc-blog-feed (XML parse error at offset 126:158) — this matches the pattern observed in 12:00 sweep ("msrc-blog-index" listed under single_observation_404_or_parse_errors). NOT promoting to stale yet; will reassess on third consecutive failure.
- **Carry-over stale (no change this sweep)**: ars-security (failure_count 3 since 2026-05-09), censys (no MCP), urlscan (no MCP), hibp (no MCP, no key), x-cisagov (failure_count 3 since 2026-05-10 WebFetch fragility), x-gossithedog (failure_count 4 since 2026-05-09).
- **mandiant-feedburner sustained failure**: failure_count 18, 9 days failing per 12:00 sweep telemetry — overdue for escalation to operator (separate ticket; not blocking this sweep).
- **No source-health.yaml writes this sweep** — runtime field changes would have been MSTIC primary 200-OK + THN 200-OK + BleepingComputer 200-OK + The Record 200-OK + CISA-KEV 200-OK + Talos 304-or-empty + Unit42 304-or-empty + SecurityWeek 304-or-empty. No new failures, no recoveries from stale state, no field flips. Operator-set `notes` fields preserved verbatim per collector field-ownership rule.

## Disposition: exit silently

No Discord post. No grader handoff for FLASH path. The MSTIC/Turla awareness item is on disk for the morning briefer + actor-profiler to pick up at 07:30 pre-brief collection.
