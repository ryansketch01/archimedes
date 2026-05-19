---
raw_id: raw-2026-05-19-am-000
collected_at: 2026-05-19T07:35:00-04:00
run_id: pre-brief-20260519-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: multi
  source_name: "Multi-source pre-brief collection sweep (07:30 EDT — feeds 08:00 morning brief)"
  source_url: null
  published_at: null
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: []
triage_tags:
  - sentinel
  - pre_brief_sweep
  - non_promotable
  - cve_2026_20182_kev_carry_forward_t_plus_38h_lapsed
  - cve_2026_42897_kev_t_minus_10d_carry_forward
  - cve_2026_42945_nginx_rift_vulncheck_carry_forward
  - cve_2020_17103_miniplasma_halt_pending_test_carry_forward
  - symantec_fast16_provisional_a_ratification_clock_t_plus_65h_carry_forward
  - storm_2949_new_actor_candidate_carry_forward
  - mini_shai_hulud_cluster_expansion_anti_noise_locked_vt006
  - shai_hulud_clone_wave_finding_2026_05_18_0003_carry_forward
  - grafana_coinbasecartel_finding_2026_05_18_0004_carry_forward
  - tycoon2fa_finding_2026_05_17_0002_carry_forward
  - turla_kazuar_secret_blizzard_finding_2026_05_14_0006_carry_forward
  - seven_eleven_shinyhunters_finding_2026_05_18_0002_carry_forward
  - dormant_splunk_sweep_47
iocs_extracted: false
iocs_count: 0
text_word_count: 0
promoted: false
promoted_note: "Sentinel pre-brief tombstone for 2026-05-19 morning collection cycle (07:30 EDT scheduled slot — feeds 08:00 morning brief). 14h window 2026-05-18T17:30 → 2026-05-19T07:30 EDT. FLASH-cycle predecessors: 18:00 EDT 2026-05-18 + 00:00 EDT 2026-05-19 + 06:00 EDT 2026-05-19 (sentinels-only, all clean). Net-new productive collection this sweep beyond the FLASH-06:00-sentinel captures: 5 raw-signal items written (am-001 through am-005). FLASH-06:00 surfaced 5 items (Nx Console 18.95.0 + actions-cool/issues-helper tag-redirect + @antv 323-package compromise + CVE-2026-31635 DirtyDecrypt PoC + CVE-2026-8153 Universal Robots PolyScope 5) that the FLASH sweep evaluated and discarded for FLASH-trigger purposes but flagged for morning grader consumption — they are written here as am-006 through am-010 for grader discoverability and frontmatter discipline rather than relying on the FLASH-06:00 sentinel narrative. Splunk first-party sweep across 30 tokens over 30d returned 40 archimedes:operation self-telemetry events + 0 defenseclaw_local hits + 0 external IOC matches — 47th consecutive dormant non-self-telemetry sweep per established cadence. Source-health changes: 2 source failures observed this sweep — same intermittent pattern as 06:00 FLASH (Talos blog https://blog.talosintelligence.com/feeds/posts/default returned 404 + Volexity blog https://www.volexity.com/blog/feed/ returned malformed body XML parse error <unknown>:17:68 not well-formed invalid token); failure_count increments for each per operator-set instruction (Talos failure_count 1→2 at-threshold; Volexity failure_count 2→3 past-threshold), but both held healthy pending operator alt-endpoint decision per intermittent-failure-pattern guidance from upstream brief 1513d98 + FLASH 06:00 sentinel. Other A/B-grade priority sources all reachable: BleepingComputer (3 in-window items, all surfaced — Microsoft Windows patching + INTERPOL + SHub Reaper macOS), The Hacker News (4 in-window items — 3 already covered in FLASH-06:00 + 1 net-new SEPPMail), SecurityWeek (4 in-window items — 2 already covered in FLASH-06:00 + 2 net-new INTERPOL relay + cyber-resilience editorial), The Record (0 in-window), DarkReading (1 in-window — Microsoft Exchange zero-day, relay of CVE-2026-42897 finding-2026-05-15-0003 carry-forward), MSTIC (0 fresh in-window — Storm-2949 from 00:00 sweep is now out-of-window), SentinelLabs (0 in-window), Unit 42 (0 in-window), Krebs (0 in-window), CISA KEV (no entries dated 2026-05-18 or 2026-05-19 — top 5 unchanged: CVE-2026-42897 + CVE-2026-20182 + CVE-2026-42208 + CVE-2026-6973 + CVE-2026-0300), CISA all.xml (0 in-window), SANS ISC (1 in-window — Stormcast podcast, awareness-only no body content, DISCARDED per Mode 1), Sophos (0 in-window), CrowdStrike (no fresh research). Hard Rules compliance: Rule 2 (no Archimedes-originated attribution across any item — TeamPCP propagation to Nx Console + actions-cool issue-helper explicitly REFUSED per Hard Rule 2 since those THN surfaces do not name TeamPCP themselves; Storm-2949 NOT propagated to any tracked actor; SHub Reaper non-roster non-propagation; SEPPMail no-attribution preserved verbatim; INTERPOL Operation Ramz no-attribution preserved verbatim), Rule 3 (no PoC code or exploit walkthroughs included in raw-signal frontmatter or extraction notes — V12 security CVE-2026-31635 GitHub PoC repo URL NOT linked; CVE-2026-8153 Claroty advisory PDF NOT linked at exploit-detail level; SEPPMail CVE-2026-2743 path-traversal Perl-reverse-shell scenario paraphrased not quoted; tag-redirect mechanism described not weaponized), Rule 4 (passive only, no active scanning, SpiderFoot not invoked, authorized-targets.yaml empty), Rule 6 (≤15 word quote limit + ≤1 quote per source: zero quotes shipped in this sentinel; quotes managed individually in am-001 through am-010 with paraphrase preferred), Rule 8 (Splunk first-party sweep returned only self-telemetry pipeline events — silence is not disconfirming per established 46-sweep dormancy cadence). LEGAL-POLICY prohibited-query-patterns not triggered. Hard Rule 5 not in scope. No Discord post (collection-phase tombstone). No _master-index.yaml regeneration (sentinel writes no IOCs; net-new IOCs from am-001 through am-010 will be handled by morning grader via VT-006 augmentation and/or new finding-creation as appropriate). TLP:CLEAR."
ttl_expires_at: 2026-08-17T07:35:00-04:00
---

# Pre-brief collection sweep 2026-05-19 07:30 EDT (feeds 08:00 morning brief)

## Sweep summary

**Mode:** pre_brief_collection
**Window:** 2026-05-18T17:30:00-04:00 → 2026-05-19T07:30:00-04:00 (~14h since prior pre-brief afternoon coverage cycle plus three FLASH cycles 18:00 / 00:00 / 06:00)
**Disposition:** PRODUCTIVE — 10 raw-signal items written (am-001 through am-010); 1 sentinel tombstone (am-000, this file).

## Sources queried (A/B-grade priority set)

| Source | Status | In-window items | Notes |
|---|---|---|---|
| BleepingComputer | reachable 200 | **3** | am-001 Microsoft Windows patching + am-002 INTERPOL (BC version) + am-003 SHub Reaper macOS |
| The Hacker News | reachable 200 | **4** | 3 covered in FLASH-06:00 (Nx Console, actions-cool, @antv) — promoted to am-006/007/008 for grader; 1 net-new (SEPPMail) → am-004 |
| SecurityWeek | reachable 200 | **4** | 2 covered in FLASH-06:00 (DirtyDecrypt, Universal Robots) — promoted to am-009/010; 1 net-new INTERPOL relay → am-005; 1 editorial discarded |
| The Record | reachable 200 | 0 | No in-window items |
| DarkReading | reachable 200 | 1 | Microsoft Exchange zero-day "no patch" relay — CVE-2026-42897 carry-forward, anti-noise applies, NOT raw-signaled separately (carry-forward to finding-2026-05-15-0003) |
| MSTIC | reachable 200 | 0 | Storm-2949 piece (00:00 sweep) now out-of-window |
| SentinelLabs | reachable 200 | 0 | |
| Unit 42 | reachable 200 | 0 | |
| Krebs | reachable 200 | 0 | |
| CISA KEV | reachable 200 | 0 | No additions since 2026-05-15; top 5 unchanged |
| CISA all.xml | reachable 200 | 0 | |
| SANS ISC | reachable 200 | 1 | Stormcast podcast, awareness-only, DISCARDED per Mode 1 |
| Sophos | reachable 200 | 0 | |
| **Talos blog** | **404** | source failure | blog.talosintelligence.com/feeds/posts/default 404 — failure_count 1→2 at-threshold; held healthy per operator-set notes |
| **Volexity blog** | **parse error** | source failure | www.volexity.com/blog/feed/ malformed body XML parse error — failure_count 2→3 past-threshold; held healthy per operator-set notes |

## Carry-forward themes preserved unchanged

Per upstream FLASH 06:00 sentinel and afternoon brief 1513d98:

- **CVE-2026-20182** Cisco Catalyst SD-WAN UAT-8616 — federal KEV deadline LAPSED Sunday 2026-05-17 now T+38h+ post-deadline-lapse with zero fresh A-grade reporting from Mandiant / Volexity / Unit 42 / MSTIC / CrowdStrike (finding-2026-05-14-0005 carry-forward chain)
- **CVE-2026-42897** Microsoft Exchange OWA XSS — federal KEV deadline T-10d Friday 2026-05-29; single-source veto on exploitation-claim layer holds (MSRC remains sole originating attester; finding-2026-05-15-0003 carry-forward; DarkReading 17:43 EDT 2026-05-18 relay is in-window but anti-noise applies — same MSRC source)
- **CVE-2026-42945** NGINX Rift PoC + VulnCheck Canaries scanner probes — B-grade defensive-posture observation NOT A-grade attestation (finding-2026-05-16-0001 carry-forward)
- **CVE-2020-17103** MiniPlasma researcher PoC — halt_pending_test on substantive layer pending MSRC or A-grade vendor reproduction (finding-2026-05-18-0001 carry-forward)
- **Symantec/SentinelLABS Fast16** — provisional-A ratification clock T+65h+ past elapsed deadline 2026-05-16T18:25 awaiting operator pass (finding-2026-05-16-0003)
- **Pwn2Own Berlin 2026** — Orange Tsai/DEVCORE Exchange RCE-to-SYSTEM chain 200K under standard 90-day ZDI vendor-coordinated-disclosure embargo through ~2026-08-13 (finding-2026-05-16-0002)
- **Turla/Kazuar/Secret Blizzard** — D+4 anti-noise rule 1 active (finding-2026-05-14-0006)
- **Tycoon2FA** device-code PhaaS — anti-noise rule 1 active (finding-2026-05-17-0002)
- **7-Eleven April 8 / ShinyHunters Salesforce** — finding-2026-05-18-0002
- **Shai-Hulud npm clone wave** (deadcode09284814) — finding-2026-05-18-0003
- **Grafana / CoinbaseCartel / ShinyHunters / SLSH** — finding-2026-05-18-0004 + finding-2026-05-17-0001
- **Storm-2949** net-new MSTIC actor cluster — strong /new-actor candidate for morning grader (Microsoft single-source originating-research; A&D-sector targeting NOT documented per Microsoft framing; identity-driven cloud-pivot tradecraft applicable to any A&D-prime running M365/Azure; per Hard Rule 2 NOT propagated to roster actor)

## Splunk first-party sweep

30-token query across `archimedes` + `defenseclaw_local` indexes over -30d returned:

```
40 events sourcetype=archimedes:operation index=archimedes
0 events index=defenseclaw_local
0 external IOC matches
```

47th consecutive dormant non-self-telemetry sweep per established cadence. Silence is not disconfirming per the established 46-sweep dormancy precedent across the b812307 / 1513d98 / a8121bc / ac3683d / 463d631 / 8280b8d chain.

## Source-health changes proposed

- `cisco-talos` failure_count 1→2 (at-threshold; held healthy per operator-set instruction; alt-endpoint decision still pending)
- `volexity` failure_count 2→3 (past-threshold; held healthy per operator-set instruction; alt-endpoint decision still pending)
- All other sources: last_successful_fetch advanced to 2026-05-19T07:30, no other status changes.
