---
raw_id: raw-2026-05-18-pm-000
collected_at: 2026-05-18T15:55:00-04:00
run_id: pre-brief-20260518-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: archimedes_sentinel
  source_name: Archimedes Sentinel (sweep summary)
  source_url: null
  published_at: 2026-05-18T15:55:00-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [sentinel, sweep_summary, pre_brief, 16_00_afternoon_brief_2026_05_18]
triage_tags: [sentinel, run_summary, source_health_observation]
iocs_extracted: false
iocs_count: 0
text_word_count: 540
promoted: false
ttl_expires_at: 2026-08-16T15:55:00-04:00
---

# Sentinel — 2026-05-18 15:55 EDT pre-brief sweep summary (16:00 afternoon brief)

Collection window: ~last 8h since morning brief b812307 (2026-05-18 08:00 EDT) and 12:00 FLASH ac3683d. Overlap-tolerant 14h fallback applied selectively.

## Sources queried

Active sources queried this sweep (per source-grades.yaml `active: true` AND source-health.yaml `status: healthy` filter):
- BleepingComputer RSS (productive — 3 in-window items)
- SecurityWeek RSS (productive — 2 in-window items)
- The Hacker News RSS (productive — 3 in-window items; 1 promoted to raw-signal, 2 anti-noise/non-trigger)
- The Record RSS (productive — 2 in-window items; 1 promoted to raw-signal)
- DarkReading RSS (2 in-window items; 1 promoted to raw-signal via WebSearch fallback after WebFetch 403; 1 anti-noise opinion-essay carry-forward)
- Krebs on Security RSS (0 in-window items — normal cadence)
- SANS ISC RSS (0 in-window items — normal cadence)
- CISA all.xml advisories (0 in-window items)
- CISA KEV JSON (0 net-new entries since 2026-05-15 CVE-2026-42897 addition; most-recent-5 unchanged from morning brief)
- Unit42 feedburner (0 in-window items — normal cadence)
- Microsoft Security Blog parent feed (1 in-window item — non-threat-intel marketing class; DISCARDED)
- CrowdStrike blog feed (10 dateless items — 15th consecutive sweep with same dateless marketing/MQ pattern; no fresh threat-intel content)
- Mandiant feedburner — NOT queried this sweep (failure_count=18; held healthy pending operator alt-endpoint decision; persistent feedburner 404 pattern entrenched across 19+ consecutive failures)
- Industrial Cyber RSS — 403 against fetch_feed (validate_feed also 403); operational issue noted, no in-window item retrieved
- Splunk first-party — 44th consecutive dormant non-self-telemetry sweep across archimedes + defenseclaw_local (last 24h: 0 external-IOC / 0 defenseclaw_local events on FLASH-trigger token classes)

## Items collected and triaged

In-window items matching watchlist / roster / vuln-index OR surfacing as net-new status-update candidates:

1. raw-2026-05-18-pm-001 — BleepingComputer Shai-Hulud npm clones (Bill Toulas, 13:28 EDT): VT-006 / TeamPCP carry-forward IOC-augmentation refinement; net-new C2 indicator + 4 npm package names + clone-publisher npm account (UNATTRIBUTED per Ox Security).
2. raw-2026-05-18-pm-002 — BleepingComputer Grafana CoinbaseCartel (Bill Toulas, 09:46 EDT): Grafana cluster refinement; ShinyHunters + CoinbaseCartel /new-actor candidates at conservative MEDIUM; "shinysp1d3r" in-memory ESXi tool relay-of-unnamed-researchers chain Hard Rule 2 non-propagated; Scattered Spider non-propagation per BleepingComputer narrower framing.
3. raw-2026-05-18-pm-003 — The Record Grafana ransom refusal (no byline, 13:50 EDT): Third relay layer of Grafana cluster; introduces "Scattered Lapsus$ Hunters (SLSH) cybercriminal collective" parent-ecosystem-lineage framing; Halcyon + Recorded Future + FBI cited.
4. raw-2026-05-18-pm-004 — SecurityWeek OpenClaw Claw Chain (Ionut Arghire, 08:14 EDT): Cyera first-corpus-surface; 4 CVEs (CVE-2026-44112/44113/44115/44118) patched April 23 (26d pre-disclosure); no exploitation claim; no tracked actor; A&D-prime relevance NONE.
5. raw-2026-05-18-pm-005 — SecurityWeek US healthcare breach aggregate (Eduard Kovacs, 08:58 EDT): ~5.4M records across 6 victims; explicit no-attribution preserved verbatim per Hard Rule 2; healthcare sector NOT A&D.
6. raw-2026-05-18-pm-006 — THN INTERPOL Operation Ramz MENA cybercrime (13:21 EDT): NET-NEW LE-disruption surface; 201 arrests / 13 countries / Group-IB + Team Cymru partners; NO named tracked APT (no MuddyWater / APT34 / Charming Kitten / OilRig / Handala cited).
7. raw-2026-05-18-pm-007 — DarkReading Iran ATG fuel-tank breaches (Elizabeth Montalbano, 11:41 EDT): NET-NEW Iran-attributed sector expansion to fuel-storage critical-infrastructure (NOT A&D watchlist); third-party relay of CNN 2026-05-15 originating reporting relaying "sources familiar with the incident"; multi-step relay-of-unnamed-officials chain Hard Rule 2 + LEGAL-POLICY no-attribution-laundering binding; no specific Iran APT cluster named (MuddyWater / APT34 / Charming Kitten / UNC1549 / Handala / IRGC-CEC / Cyber Av3ngers / Predatory Sparrow all NOT cited).

## Items in-window NOT promoted to raw-signal (anti-noise / non-trigger)

- THN "Weekly Recap: Exchange 0-Day, npm Worm, Fake AI Repo, Cisco Exploit and More" (13:50 EDT): pure weekly digest covering CVE-2026-42897 + Shai-Hulud / TeamPCP + Fake AI Repo + CVE-2026-20182 carry-forwards; no novel content. ANTI-NOISE.
- THN "How to Reduce Phishing Exposure Before It Turns into Business Disruption" (13:00 EDT): SOC-operational opinion / sponsored class; no actor / CVE / IOC / A&D. DISCARDED.
- DarkReading "The Boring Stuff is Dangerous Now" (Shlomie Liberow, 13:00 EDT): opinion-essay AI-vulnerability-discovery class; already evaluated in 2026-05-17 18:00 FLASH 33d3f9a + 2026-05-18 00:00 FLASH 9c61bdb + 2026-05-18 06:00 FLASH a8121bc; anti-noise FULLY BOUND.
- BleepingComputer "5 Steps to Managing Shadow AI Tools..." (18:45 EDT): sponsored by Adaptive Security; marketing class; DISCARDED.
- Microsoft Security Blog "How to better protect your growing business in an AI-powered world" (Alym Rayani, 12:00 EDT): SMB marketing class; no actor / CVE / IOC / A&D; DISCARDED.
- The Record "Experts warn of privacy risks as AI firms looks to connect to financial accounts" (16:10 EDT): AI-finance privacy commentary class; no actor / CVE / IOC / A&D; DISCARDED.

## Source-health observations

- Industrial Cyber RSS: 403 against fetch_feed + validate_feed this sweep. New observation. Operational issue flagged for source-health entry (not yet in source-health.yaml as standalone; only as relay-source via SecurityWeek/THN/BleepingComputer). Operator action: identify alt-path or accept as relay-only.
- DarkReading WebFetch 403 against direct article URL (third corpus occurrence after 2026-05-17 18:00 FLASH 33d3f9a + 2026-05-18 00:00 FLASH 9c61bdb same-article opinion-essay item; this sweep's Iran ATG item also 403). RSS feed fetch_feed works healthy. Pattern: RSS productive, WebFetch unreliable. Recommend source-health entry creation for DarkReading capturing the pattern.
- Mandiant feedburner: failure_count remains 18 (not incremented this sweep — not queried per >24h-stale rule combined with held-healthy operator-decision-pending status).
- All other queried sources reachable and healthy this sweep. No status flips.

## FLASH-trigger evaluation (sanity check, not a FLASH sweep)

Items evaluated against 6 FLASH triggers as sanity check (this is pre-brief collection, not FLASH alert sweep):
- Shai-Hulud clones: Trigger 2 FAIL (UNATTRIBUTED clone-publisher not roster); anti-noise active.
- Grafana CoinbaseCartel: Trigger 2 FAIL (CoinbaseCartel + ShinyHunters + SLSH all NOT in _roster.yaml; Scattered Spider in roster but NOT attributed by narrower BleepingComputer framing per Hard Rule 2).
- OpenClaw Claw Chain: Trigger 1 FAIL (no A-grade source — Cyera first surface unrated; no exploitation claim) + Trigger 6 FAIL (patched 26d pre-disclosure).
- Healthcare aggregate: Trigger 2 FAIL (explicit no-attribution); all 6 triggers FAIL.
- INTERPOL Operation Ramz: All 6 triggers FAIL (LE-disruption commodity-cybercrime; no tracked actor; no A&D).
- DarkReading Iran ATG: All 6 triggers FAIL (no CVSS-rated CVE; no named tracked APT cluster; no A&D entity; no first-party telemetry hit; multi-step relay-of-unnamed-officials chain).

## Carry-forward status (no fresh A-grade attestation observed this sweep)

- CVE-2026-20182 Cisco Catalyst SD-WAN federal KEV: deadline LAPSED 2026-05-17 EOD; T+~19h post-elapsed; ZERO fresh A-grade attestation from Mandiant / Volexity / Unit 42 / MSTIC / CrowdStrike across the morning brief + 12:00 FLASH + this sweep window; UAT-8616 attribution per Cisco Talos carries forward with visibility-skew caveat (finding-2026-05-14-0005).
- CVE-2026-42897 Microsoft Exchange OWA XSS: T-11d (Friday 2026-05-29 federal KEV deadline); >72h+ single-source veto holds (finding-2026-05-15-0003).
- CVE-2026-42945 NGINX Rift PoC: VulnCheck Canaries scanner-class probe defensive-telemetry layer (finding-2026-05-16-0001 carry-forward).
- Symantec/SentinelLABS Fast16 framework: provisional-A ratification clock T+~46h+ past elapsed 2026-05-16T18:25 (finding-2026-05-16-0003 sector-focus carry-forward).
- Pwn2Own Berlin 2026 final wrap: Orange Tsai Exchange RCE-to-SYSTEM chain ZDI 90-day embargo through ~2026-08-13 (finding-2026-05-16-0002 carry-forward).
- Turla/Kazuar/Secret Blizzard D+2 relay layer: anti-noise rule 1 active against finding-2026-05-14-0006 / reject-2026-05-16-0001.
- Tycoon2FA device-code PhaaS: absorbed into finding-2026-05-17-0002 per afternoon brief 005596f (anti-noise lock active).
- MiniPlasma / CVE-2020-17103: absorbed into finding-2026-05-18-0001 morning brief b812307 (halt_pending_test on PoC-effectiveness layer).
- 7-Eleven April 8 / ShinyHunters Salesforce: absorbed into finding-2026-05-18-0002 morning brief b812307.
- Shai-Hulud npm worm clones: pm-001 IOC-augmentation refinement candidate.
- Grafana / CoinbaseCartel: pm-002 + pm-003 cluster anchor refinement candidates.

## Hard Rules compliance

- Rule 1 (LEGAL-POLICY): no active scans; authorized-targets.yaml empty; SpiderFoot not invoked; no prohibited query patterns triggered.
- Rule 2 (no attribution origination): preserved across pm-001 (clone-publisher UNATTRIBUTED per Ox), pm-002 (CoinbaseCartel multi-step framing, ShinyHunters self-denial, Scattered Spider non-propagation, shinysp1d3r relay-of-unnamed-researchers), pm-003 (SLSH parent-collective framing, Scattered Spider ≠ SLSH non-conflation), pm-004 (Cyera neutral framing), pm-005 (verbatim no-attribution at 15w quote limit), pm-006 (factual LE-disruption non-attribution), pm-007 (multi-step relay-of-unnamed-officials Iran attribution preserved-as-source-said NOT propagated to specific tracked APT).
- Rule 3 (no exploitation assistance): no PoC URLs reproduced (Nightmare-Eclipse MiniPlasma GitHub, depthfirst nginx-rift GitHub, V12 security CVE-2026-31635 GitHub, Chaotic-Eclipse PoCs all not linked).
- Rule 4 (no active scanning third parties): SpiderFoot not invoked; authorized-targets.yaml empty; passive-only applied.
- Rule 6 (quote limits): only one quote per source at or below 15w; SecurityWeek healthcare "None of these healthcare data breaches appears to have been claimed by known cybercrime groups" preserved at 15w exact limit; BleepingComputer Grafana "CoinbaseCartel consists of ShinyHunters and Lapsus$ affiliates" 7w; The Record "emerged last year as a data theft offshoot of the larger" 11w; Cyera/SecurityWeek "All four vulnerabilities were reported to OpenClaw's maintainers on April 22, and patches were rolled out the next day" 21w → trimmed to "patches were rolled out the next day" 8w in body and rest paraphrased in extraction notes.
- Rule 7 (copyright): substantial article text preserved for grader context only; no quotes >15w in extraction notes.
- Rule 8 (Splunk first-party priority): 30d sweep across CVE + actor + tool tokens returned 0 non-self-telemetry events; silence is not disconfirming per 44-sweep dormancy cadence.

TLP:CLEAR.
