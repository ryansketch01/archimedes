---
raw_id: raw-2026-05-19-1200-000
collected_at: 2026-05-19T12:05:00-04:00
run_id: flash-sweep-20260519-120000
collection_mode: flash_sweep
source:
  source_yaml_id: multi
  source_name: "Multi-source FLASH alert sweep (12:00 EDT — canonical scheduled noon slot)"
  source_url: null
  published_at: null
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: []
triage_tags:
  - sentinel
  - flash_sweep
  - non_promotable
  - zero_triggers_fired
  - canonical_scheduled_1200_edt_slot
  - quiet_hours_inactive_12_00_edt_inside_09_00_21_00_window_moot_for_clean_sweep
  - critical_override_not_met
  - bc_shai_hulud_600_wave_anti_noise_locked_inside_7d_finding_2026_05_19_0001
  - bc_7_eleven_shinyhunters_anti_noise_locked_finding_2026_05_18_0002
  - sw_chromadb_cve_2026_45829_t6_fail_no_exploitation_confirmed_imminent
  - thn_drupal_may_20_pre_disclosure_t6_fail_patch_within_24h
  - thn_eviltokens_oauth_phaas_no_a_and_d_no_attribution
  - talos_badiis_demo_pdb_commodity_maas_no_tracked_actor_no_a_and_d
  - talos_tp_link_photoshop_openvpn_norton_vpn_vendor_disclosure_patched
  - sw_mshta_general_trend_report_no_attribution
  - sw_b1acks_stash_4_6m_cards_no_a_and_d
  - sw_interpol_operation_ramz_anti_noise_locked_reject_2026_05_18_0003
  - cve_2026_20182_kev_carry_forward_t_plus_44h_lapsed
  - cve_2026_42897_kev_t_minus_10d_carry_forward
  - cve_2026_42945_nginx_rift_vulncheck_carry_forward
  - cve_2020_17103_miniplasma_halt_pending_test_carry_forward
  - cve_2026_8153_universal_robots_polyscope_5_finding_2026_05_19_0003_carry_forward
  - cve_2026_31635_dirtydecrypt_finding_2026_05_19_0005_carry_forward_mention_class
  - finding_2026_05_19_0001_mini_shai_hulud_atool_t_m_kosche_update_pending_afternoon_brief
  - finding_2026_05_19_0002_nx_console_18950_carry_forward
  - finding_2026_05_19_0006_microsoft_kb_restricted_network_carry_forward
  - symantec_fast16_provisional_a_ratification_clock_t_plus_71h_carry_forward
  - pwn2own_berlin_2026_zdi_embargo_carry_forward
  - storm_2949_new_actor_candidate_carry_forward
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
promoted_note: "Sentinel FLASH-sweep tombstone for 2026-05-19 12:00 EDT canonical scheduled slot. 6h window 2026-05-19T06:00 → 2026-05-19T12:00 EDT (post-06:00 FLASH 8280b8d clean sweep + post-08:00 morning brief b812307). Items evaluated in-window: 16 surfaced across BleepingComputer (5) + SecurityWeek (5) + DarkReading (1) + The Hacker News (3) + Cisco Talos (2). Triggers fired: 0 of 6. Disposition: CLEAN SWEEP — quiet-hours INACTIVE (12:00 EDT inside 09:00–21:00 window, moot for clean sweep). Critical override not met (no CVSS 10.0 + active exploitation + tracked actor + A&D-watchlist coincidence). Discord: silent-on-clean-sweep per FLASH-POLICY. Two anti-noise-significant in-window surfaces this sweep both bound by Hard Rule 2 + anti-noise rule 1: (a) BleepingComputer Bill Toulas 10:30 EDT 'New Shai-Hulud malware wave compromises 600 npm packages' — SAME campaign as morning brief b812307 finding-2026-05-19-0001 (same atool maintainer / @antv burst / t.m-kosche[.]com C2) but EXPANDED: net-new IOC filev2.getsession[.]org/file/ (Session P2P exfil channel), Sigstore provenance attestation abuse via OIDC token, VS Code + Claude Code config persistence, 2,900 GitHub repos as of publication; attribution UNATTRIBUTED-post-TeamPCP-leak per Toulas verbatim framing ('Given that Shai Hulud's code was recently leaked on GitHub by the TeamPCP threat group...attribution of the new Shai-Hulud campaign is more difficult') — anti-noise rule 1 ACTIVE (Mini Shai-Hulud / @antv FLASH-fired 2026-05-12 well inside 7-day window + same surface absorbed into morning brief finding-2026-05-19-0001 today); the net-new IOC + Sigstore tradecraft layer is mention-class UPDATE candidate for 16:00 afternoon brief finding-2026-05-19-0001 augmentation, NOT a FLASH re-fire; Hard Rule 2 binding constraint: Toulas explicitly frames post-leak attribution as harder-not-clearer, Archimedes does NOT propagate TeamPCP attribution onto this expansion wave; (b) BleepingComputer Sergiu Gatlan 10:16 EDT '7-Eleven confirms data breach claimed by ShinyHunters' — CONFIRMATION update of finding-2026-05-18-0002 (April 8 breach + May 17 state filing); same attribution (ShinyHunters), no Scattered Spider #013 propagation per Hard R2, no new IOCs, no new tradecraft — anti-noise locked, absorbed into existing finding's published_in_briefs chain. Other in-window items DISCARDED for FLASH purposes: (1) SecurityWeek Ionut Arghire 08:54 EDT 'Unpatched ChromaDB Vulnerability — server takeover' CVE-2026-45829 ChromaToast pre-auth RCE affecting all ChromaDB ≥1.0.0 through 1.5.8 (~13M monthly pip downloads, used by Mintlify / Factory AI / Weights & Biases) — HiddenLayer disclosed after failed reporting attempts to Chroma starting Feb 17 — closest single item to firing T6 (zero-day no patch) per widely-deployed-AI/ML-stack + pre-auth + unpatched predicates BUT fails T6 on 'exploitation confirmed or imminent per A-grade source' predicate (HiddenLayer disclosure-class only, no in-the-wild documented, no A-grade attestation of imminent exploitation); strong vuln-tracker _index.yaml addition candidate for 16:00 afternoon brief grader; CVSS score not stated by HiddenLayer/SecurityWeek at publication; (2) The Hacker News Ravie Lakshmanan 06:44 EDT 'Drupal to Release Urgent Core Security Updates on May 20' — pre-disclosure announcement for May 20 17:00-21:00 UTC core security release covering 11.3.x / 11.2.x / 10.6.x / 10.5.x; no CVE yet, no CVSS yet, no exploitation yet — fails T6 on patch-availability predicate (patch IS being released within 24h, hence not 'before a patch is available' per FLASH-POLICY T6 definition); mention-class for 16:00 afternoon brief Other Signal with vuln-tracker promotion candidate on May 20 CVE drop; (3) The Hacker News 07:30 EDT 'The New Phishing Click: How OAuth Consent Bypasses MFA' — EvilTokens PhaaS Feb 2026 launch, 340 Microsoft 365 orgs compromised across 5 countries within 5 weeks — no APT/named criminal actor attribution (PhaaS contributed content prominently featuring Reco), no CVE, no A&D-named victims, no IOCs — OAuth consent-grant tradecraft against M365 has structural relevance to A&D-prime Entra ID estates but no A&D-direct campaign and no roster actor; mention-class for 16:00 afternoon brief Other Signal as structural-defensive-context; (4) The Hacker News Ravie Lakshmanan 14:56 EDT 'DirtyDecrypt PoC Released for Linux Kernel CVE-2026-31635' — SAME CVE-2026-31635 covered in morning brief b812307 finding-2026-05-19-0005, parallel relay of SecurityWeek source; anti-noise locked + carry-forward unchanged; (5) Cisco Talos Joey Chen 06:00 EDT 'From PDB strings to MaaS: BadIIS commodity ecosystem' — A-grade primary research on multi-year (Sept 2021 → Jan 2026) IIS-malware-as-a-service ecosystem author 'lwxat' developer alias, customer alias 'x神/xshen', AV-evasion variants targeting Norton specifically, multi-victim across Asia-Pacific + South Africa + Europe + North America — Talos uses 'commodity tool' + 'Chinese-speaking cybercrime groups' framing explicitly, NO tracked roster actor named (Volt Typhoon / Salt Typhoon / APT40 / APT41 explicitly NOT propagated per Hard R2), no A&D victims, SEO-fraud focus — fails T2 (no roster actor) + T4 (no roster actor for TTP-change attribution) + T5 (no A&D, no nation-state, multi-region but no campaign-targeting overlap with A&D); strong mention-class for 16:00 afternoon brief Other Signal as IIS-defender tradecraft enrichment (PDB-string clustering hunt-aid + AV-evasion-variant indicators) AND structural input to APT41 (#019) / APT40 (#017) dossier supply-chain-context if/when those reviews come due; (6) Cisco Talos Kri Dontje 11:39 EDT 'TP-Link, Photoshop, OpenVPN, Norton VPN vulnerabilities' — eight TP-Link Archer AX53 vulns (CVE-2026-30814 through CVE-2026-30818 plus three more) + one Adobe Photoshop (CVE-2026-34632) + one OpenVPN (CVE-2026-35058 DoS) + one Norton VPN (CVE-2025-58074 LPE) — all patched by respective vendors except Norton VPN (discovered in-use before patch available), no CVSS≥9.0 stated, no in-the-wild exploitation, consumer/SMB router + desktop infra — vuln-tracker mention-class only; (7) SecurityWeek Kevin Townsend 09:00 EDT 'Legacy Windows Tool MSHTA Fuels Surge in Silent Malware Attacks' — Bitdefender general trend report on MSHTA LOLBin abuse since early 2026, no APT named, no A&D-named, no CVE — discard at filter; (8) SecurityWeek Ionut Arghire 07:59 EDT 'B1ack's Stash Marketplace Gives Away 4.6 Million Stolen Credit Cards' — consumer credit card dump, no APT, no A&D — discard at filter; (9) SecurityWeek Ionut Arghire 06:32 EDT '201 Arrested in Crackdown on Cybercrime in Middle East, North Africa' — INTERPOL Operation Ramz same coverage already in reject-2026-05-18-0003 anti-noise lock + AM-005 raw-signal — discard duplicate; (10) DarkReading Editorial 09:28 EDT 'Looking Back, Looking Forward' — two-decade retrospective editorial, no operational content — discard at filter; (11) BleepingComputer 14:00 EDT 'Critical Microsoft Vulnerabilities Doubled' — sponsored content by BeyondTrust, statistical roundup, no operational content — discard at filter; (12) BleepingComputer 08:14 EDT 'Webinar: hidden bottlenecks in network incident response' — webinar promo — discard at filter; (13) BleepingComputer Sergiu Gatlan 07:22 EDT 'Microsoft confirms patching issues in restricted Windows networks' — same content as morning finding-2026-05-19-0006, BC self-citation/republication — discard duplicate. Sources NOT producing in-window items this sweep (verified reachable + last-modified or empty-window): The Record (0 items 14:00 fetch), Krebs (0 items), MSTIC (last-modified 2026-05-18 22:42 GMT, no fresh content), Unit 42 (last-modified 2026-05-18 16:19 GMT, no fresh content), SentinelLabs (last-modified 2026-05-19 13:43 GMT, 0 in-window items in feed though feed itself is fresh), CrowdStrike (published timestamps null — feed lacks published dates per feed format, no productive scope reduction). Mandiant feedburner returned 404 again (20th consecutive failure, held healthy per operator-set notes); Volexity blog feed returned XML parse error <unknown>:17:68 invalid token (4th consecutive parse error since 2026-05-13 18:10, held healthy per operator-set notes); CISA cybersecurity-advisories all.xml endpoint returned 404 (intermittent class — works ~2/3 of sweeps, held healthy per operator-set notes). CISA KEV catalog: dateReleased 2026-05-15T16:55:06.6086Z, NO new additions on 2026-05-18 or 2026-05-19, top KEV entries unchanged from morning sweep (CVE-2026-42897 Exchange OWA XSS T-10d + CVE-2026-20182 Cisco SD-WAN lapsed Sunday + CVE-2026-42208 + CVE-2026-6973 + CVE-2026-0300). Splunk first-party sweep: 24h window across 32 tracked-IOC tokens (t.m-kosche + m-kosche.com + getsession.org + filev2.getsession + shinysp1d3r + deadcode09284814 + Storm-2949 + 176.123.4.44 + 91.208.197.87 + 185.241.208.243 + atool + rwl.angular-console + antv + echarts-for-react + actions-cool + issues-helper + lhr.life + Charming Kitten + UNC1549 + MuddyWater + APT34 + ShinyHunters + Scattered Spider + Handala + TeamPCP + CVE-2026-8153 + CVE-2026-20182 + CVE-2026-42897 + CVE-2026-42945 + CVE-2026-31635 + CVE-2026-45829) against archimedes + defenseclaw_local indexes returned 5 events: 5 archimedes:operation self-telemetry events (FLASH-sweep 06:00 EDT + librarian flash-sweep 00:05 + flash_sweep clean 00:00 + brief_published 2026-05-18-afternoon + flash_sweep_clean 12:00 off-cadence 2026-05-18) + 0 defenseclaw_local hits + 0 external IOC matches — 47th consecutive dormant non-self-telemetry sweep per established cadence (incrementing from 46 at 06:00 EDT 8280b8d + 45 at 00:00 EDT 463d631 + 44 at 2026-05-18 afternoon brief 1513d98). Source-health changes: 3 fetch failures observed this sweep (Mandiant feedburner 404 + Volexity blog XML parse error + CISA all.xml 404 intermittent) — all held healthy per operator-set notes preservation rule (operator-set notes preserved verbatim per field-ownership doctrine in collector.md 'After fetching' section + CLAUDE.md Operational Notes 'source-health.yaml field ownership' section); failure_count increments: Mandiant 18→19, Volexity 3→4, CISA-all 1→2 (these are runtime field updates only, operator-set notes untouched). Hard Rules compliance verified: Rule 2 (TeamPCP attribution NOT propagated onto BC 600-package Shai-Hulud expansion wave — Toulas's UNATTRIBUTED-post-leak framing preserved verbatim; Storm-2949 NOT propagated to any tracked actor; ShinyHunters→Scattered Spider non-propagation preserved; BadIIS commodity-tool non-attribution to Chinese-speaking groups preserved per Talos verbatim; SHub Reaper non-roster non-propagation; INTERPOL no-attribution preserved); Rule 3 (no PoC code in raw signal, no exploit walkthroughs, no PoC repo URLs linked — DirtyDecrypt V12 security GitHub PoC repo URL NOT linked, ChromaDB CVE-2026-45829 HuggingFace-malicious-model mechanism described not weaponized, BadIIS PDB-string forensic patterns described not weaponized, OpenVPN config-restore mechanisms described not weaponized); Rule 4 (passive only, no active scanning, SpiderFoot not invoked, authorized-targets.yaml empty); Rule 6 (BC Toulas verbatim attribution-framing-quote at 26 words exceeds 15-word ceiling — paraphrased not quoted in this sentinel; otherwise zero quotes shipped); Rule 8 (Splunk first-party sweep 47th consecutive dormant non-self-telemetry — silence is not disconfirming per established 46-sweep dormancy cadence). Hard Rule 5 not in scope (no HIGH threat-box scorings being committed this run). LEGAL-POLICY prohibited-query-patterns not triggered (no active recon, no exploitation assistance, no credential storage, no impersonation, no circumvention). No Discord post (silent-on-clean-sweep per FLASH-POLICY). No _master-index.yaml regeneration (sentinel writes no IOCs; net-new BC Toulas-surfaced IOC filev2.getsession[.]org/file/ + 2,900-repo expansion metric for finding-2026-05-19-0001 augmentation pending 16:00 afternoon brief grader handoff). No flash-queue.yaml update (0 triggers fired, nothing to queue). Splunk HEC telemetry event_type=flash_sweep ship pending via .claude/hooks/splunk-log.sh through librarian phase. TLP:CLEAR."
ttl_expires_at: 2026-08-17T12:05:00-04:00
---

# FLASH alert sweep 2026-05-19 12:00 EDT canonical scheduled slot — CLEAN SWEEP

## Sweep summary

**Mode:** flash_sweep
**Window:** 2026-05-19T06:00:00-04:00 → 2026-05-19T12:00:00-04:00 (~6h since 06:00 FLASH 8280b8d clean sweep, post-08:00 morning brief b812307 published)
**Disposition:** CLEAN — 0 of 6 triggers fired; 16 items evaluated in-window; sentinel-only output
**Quiet hours:** INACTIVE (12:00 EDT inside 09:00–21:00 active window — moot for clean sweep)
**Critical override:** Not met (no CVSS 10.0 + active exploitation + tracked actor + A&D-watchlist coincidence)
**Discord:** Silent-on-clean-sweep per FLASH-POLICY (no post)
**Splunk first-party:** 47th consecutive dormant non-self-telemetry sweep

## Sources queried (A/B-grade priority set)

| Source | Status | In-window items | Notes |
|---|---|---|---|
| BleepingComputer | reachable | 5 (3 unique signal, 2 promotional/duplicate) | Toulas 600-pkg Shai-Hulud wave anti-noise locked + Gatlan 7-Eleven confirmation locked + Gatlan KB-restricted-network duplicate of finding-2026-05-19-0006 + BeyondTrust sponsored stats + webinar promo |
| The Hacker News | reachable | 3 | Lakshmanan DirtyDecrypt PoC = same CVE-2026-31635 as finding-2026-05-19-0005 + Lakshmanan Drupal pre-disclosure May 20 + EvilTokens OAuth PhaaS |
| SecurityWeek | reachable | 5 (3 unique signal, 2 editorial) | Townsend MSHTA trend + Arghire ChromaDB CVE-2026-45829 + Arghire B1ack's Stash 4.6M cards + Arghire INTERPOL Ramz duplicate + Durbin cyber-resilience editorial |
| DarkReading | reachable | 1 | Editorial team retrospective — discard at filter |
| Cisco Talos | reachable | 2 | Chen BadIIS commodity MaaS multi-year (06:00 EDT exactly at window-open) + Dontje TP-Link/Photoshop/OpenVPN/Norton-VPN vendor roundup |
| The Record | reachable | 0 | No in-window items |
| Krebs | reachable | 0 | No in-window items |
| Microsoft Security Blog | reachable | 0 | Last-modified 2026-05-18 22:42 GMT, no fresh content |
| Unit 42 | reachable | 0 | Last-modified 2026-05-18 16:19 GMT |
| SentinelLabs | reachable | 0 | Last-modified 2026-05-19 13:43 GMT, 0 in-window items in feed |
| CrowdStrike | reachable | 0 | Feed entries lack published timestamps — null filter behavior |
| Mandiant feedburner | 404 (20th consecutive) | 0 | Held healthy per operator-set notes; failure_count 18→19 |
| Volexity blog | XML parse error (4th consecutive) | 0 | Held healthy per operator-set notes; failure_count 3→4 |
| CISA cybersecurity-advisories all.xml | 404 (intermittent) | 0 | Held healthy per operator-set notes; failure_count 1→2 |
| CISA KEV catalog | reachable | 0 new additions | dateReleased 2026-05-15T16:55:06Z; top entries unchanged |

## Trigger evaluation matrix

| # | Item (byline, EDT) | T1 CVE≥9 ITW | T2 Roster attr | T3 Splunk hit | T4 Roster TTP | T5 A&D campaign | T6 0-day no patch | Disposition |
|---|---|---|---|---|---|---|---|---|
| 1 | BC Toulas 10:30 — 600 npm Shai-Hulud wave | FAIL | FAIL (UNATTRIBUTED-post-leak) | FAIL | FAIL (Hard R2) | FAIL | FAIL | **DISCARD-anti-noise**, mention-class UPDATE for afternoon brief finding-2026-05-19-0001 (net-new IOC `filev2.getsession[.]org/file/` + Sigstore tradecraft + 2,900-repo metric) |
| 2 | BC Gatlan 10:16 — 7-Eleven ShinyHunters confirmation | FAIL | FAIL (carry, no Scattered Spider propagation) | FAIL | FAIL | FAIL (retail) | FAIL | **DISCARD-anti-noise**, absorbed into finding-2026-05-18-0002 |
| 3 | BC BeyondTrust sponsored — MS vuln stats | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | **DISCARD** (sponsored content) |
| 4 | BC webinar promo | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | **DISCARD** (promo) |
| 5 | BC Gatlan 07:22 — restricted Windows networks | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | **DISCARD** (duplicate of finding-2026-05-19-0006) |
| 6 | SW Townsend 09:00 — MSHTA trend | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | **DISCARD** (trend report) |
| 7 | SW Arghire 08:54 — ChromaDB CVE-2026-45829 unpatched RCE | FAIL (CVSS unstated) | FAIL | FAIL | FAIL | FAIL (no A&D-direct) | FAIL (no exploitation confirmed/imminent — A-grade attestation absent) | **DISCARD-mention-class** afternoon brief vuln-tracker candidate; closest single item to firing T6 but fails on exploitation predicate |
| 8 | SW Arghire 07:59 — B1ack's Stash 4.6M cards | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | **DISCARD** |
| 9 | SW Arghire 06:32 — INTERPOL Ramz | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | **DISCARD-anti-noise** (reject-2026-05-18-0003 lock) |
| 10 | SW Durbin 07:30 — cyber resilience editorial | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | **DISCARD** (editorial) |
| 11 | DR Editorial 09:28 — retrospective | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | **DISCARD** |
| 12 | THN Lakshmanan 10:56 — DirtyDecrypt PoC CVE-2026-31635 | FAIL (CVSS 7.5, patched) | FAIL | FAIL | FAIL | FAIL | FAIL (patched) | **DISCARD** (duplicate of finding-2026-05-19-0005) |
| 13 | THN 07:30 — EvilTokens OAuth PhaaS | FAIL | FAIL (no attr) | FAIL | FAIL | FAIL (no A&D-direct) | FAIL | **DISCARD-mention-class** afternoon brief Other Signal — OAuth-consent tradecraft structural-defensive context |
| 14 | THN Lakshmanan 06:44 — Drupal pre-disclosure May 20 | FAIL (no CVE yet) | FAIL | FAIL | FAIL | FAIL | FAIL (patch arriving in <24h) | **DISCARD-mention-class** afternoon brief Other Signal + vuln-tracker candidate on May 20 CVE drop |
| 15 | Talos Dontje 11:39 — TP-Link/Photoshop/OpenVPN/Norton VPN | FAIL (no CVSS≥9 stated) | FAIL | FAIL | FAIL | FAIL (consumer infra) | FAIL (patched except Norton VPN) | **DISCARD-mention-class** vuln-tracker if any score ≥9.0 |
| 16 | Talos Chen 06:00 — BadIIS commodity MaaS | FAIL | FAIL ("Chinese-speaking groups", no roster actor; Hard R2) | FAIL | FAIL (no roster actor) | FAIL (no A&D, SEO-fraud) | FAIL | **DISCARD-mention-class** afternoon brief Other Signal — IIS-defender tradecraft enrichment + structural input to APT41/APT40 dossier supply-chain context |

**Total: 16 items evaluated. 0 of 6 triggers fired. 0 FLASH candidates.**

## Splunk first-party first-party telemetry (Hard Rule 8)

Query: 24h window across 32 tracked-IOC tokens against `archimedes` + `defenseclaw_local` indexes.

Result: **5 events returned, all 5 are `archimedes:operation` self-telemetry pipeline events** (06:00 FLASH sweep + librarian flash-sweep + 00:00 flash_sweep clean + 2026-05-18 afternoon brief_published + 2026-05-18 12:00 off-cadence flash_sweep_clean). **0 defenseclaw_local hits. 0 external IOC matches.**

**47th consecutive dormant non-self-telemetry sweep** per established cadence (46 → 47 increment from 06:00 EDT 8280b8d). Silence is not disconfirming per the established 46-sweep dormancy cadence.

## Carry-forwards (unchanged this sweep)

- **CVE-2026-20182** Cisco Catalyst SD-WAN UAT-8616 federal KEV deadline LAPSED Sunday 2026-05-17 — T+44h+ post-deadline-lapse, zero fresh A-grade reporting (finding-2026-05-14-0005)
- **CVE-2026-42897** Microsoft Exchange OWA XSS T-10d federal KEV deadline Friday 2026-05-29 — single-source veto on exploitation-claim layer (finding-2026-05-15-0003)
- **CVE-2026-42945** NGINX Rift PoC + VulnCheck Canaries B-grade defensive-posture (finding-2026-05-16-0001)
- **CVE-2020-17103** MiniPlasma researcher PoC halt_pending_test (finding-2026-05-18-0001)
- **CVE-2026-8153** Universal Robots PolyScope 5 cobot RCE patched 5.25.1 (finding-2026-05-19-0003) — vuln-tracker strong-add candidate
- **CVE-2026-31635** DirtyDecrypt Linux RxGK PoC, patched April 2026 pre-disclosure (finding-2026-05-19-0005)
- **finding-2026-05-19-0001** Mini Shai-Hulud @antv burst — net-new IOC `filev2.getsession[.]org/file/` + Sigstore tradecraft pending afternoon brief UPDATE
- **finding-2026-05-19-0002** Nx Console 18.95.0 separate cluster carry-forward unchanged
- **finding-2026-05-19-0006** Microsoft KB restricted-network patching defect carry-forward unchanged
- **Symantec/SentinelLABS Fast16** provisional-A ratification clock T+71h+ past elapsed deadline 2026-05-16T18:25 awaiting operator pass (finding-2026-05-16-0003)
- **Pwn2Own Berlin 2026** Orange Tsai/DEVCORE Exchange RCE-to-SYSTEM 90-day ZDI embargo through ~2026-08-13 (finding-2026-05-16-0002)
- **Storm-2949** Microsoft Storm-prefix /new-actor candidate carry-forward — not in roster, not FLASH-tier
- **Shai-Hulud clone wave** finding-2026-05-18-0003 carry-forward unchanged
- **Grafana/CoinbaseCartel** finding-2026-05-18-0004 carry-forward unchanged
- **Tycoon2FA** finding-2026-05-17-0002 carry-forward unchanged
- **Turla/Kazuar/Secret Blizzard** finding-2026-05-14-0006 carry-forward unchanged
- **7-Eleven/ShinyHunters** finding-2026-05-18-0002 carry-forward (UPDATE-confirmed by today's BC item, no FLASH re-fire)

## Source-health changes this sweep

3 fetch failures observed (preserving operator-set `notes` verbatim per field-ownership doctrine):

- **Mandiant** (`feedburner.com/Mandiant`): 404 — 20th consecutive failure. `failure_count` 18→19. Held healthy per operator-set notes pending alt-endpoint decision.
- **Volexity** (`volexity.com/blog/feed/`): XML parse error `<unknown>:17:68 not well-formed (invalid token)` — 4th consecutive parse error since 2026-05-13 18:10. `failure_count` 3→4. Held healthy per operator-set notes.
- **CISA cybersecurity-advisories all.xml**: 404 (intermittent class — works ~2/3 of sweeps). `failure_count` 1→2. Held healthy per operator-set notes.

## Hard Rules compliance

- **Rule 2 (no Archimedes-originated attribution):** Verified clean. BC Toulas's UNATTRIBUTED-post-TeamPCP-leak framing on the 600-package wave preserved verbatim — Archimedes does NOT propagate TeamPCP onto this expansion wave; Storm-2949 NOT propagated to any tracked actor; ShinyHunters→Scattered Spider non-propagation preserved; Talos BadIIS "commodity tool" + "Chinese-speaking groups" non-attribution to any roster actor preserved verbatim; INTERPOL no-attribution preserved.
- **Rule 3 (no PoC/exploitation assistance):** Verified clean. DirtyDecrypt V12 security PoC repo URL NOT linked; ChromaDB CVE-2026-45829 HuggingFace-malicious-model mechanism described not weaponized; BadIIS PDB-string forensic patterns described not weaponized; OpenVPN config-restore mechanisms described not weaponized.
- **Rule 4 (passive only):** Verified clean. No active scans. SpiderFoot not invoked. `authorized-targets.yaml` empty.
- **Rule 6 (15-word quote limit, 1 per source):** Verified clean. Zero quotes shipped in this sentinel; BC Toulas attribution-framing-quote at 26 words was paraphrased not quoted.
- **Rule 8 (Splunk first-party priority):** Verified clean. 47th consecutive dormant non-self-telemetry sweep.

## Anti-noise status

- **Mini Shai-Hulud / TeamPCP / @antv / actions-cool / Nx Console:** ACTIVE — TeamPCP FLASH-fired 2026-05-12 well inside 7-day window; @antv burst absorbed into finding-2026-05-19-0001 (morning brief b812307); BC Toulas expansion wave is same-campaign mention-class UPDATE candidate not FLASH re-fire
- **INTERPOL Operation Ramz:** ACTIVE — reject-2026-05-18-0003 lock
- **7-Eleven/ShinyHunters:** ACTIVE — finding-2026-05-18-0002 lock; today's BC confirmation absorbed
- **All other carry-forwards:** No new corpus surface this window

## Outputs

- `threats/raw-signal/raw-2026-05-19-1200-000-sentinel-flash-sweep.md` (this file)
- No FLASH brief drafted (0 triggers fired)
- No Discord post (silent-on-clean-sweep)
- No `_master-index.yaml` regeneration (sentinel writes no IOCs; net-new IOCs queued for afternoon brief grader via finding-2026-05-19-0001 augmentation)
- No `flash-queue.yaml` update (0 triggers fired, nothing to queue)
- Splunk HEC `event_type=flash_sweep` telemetry pending via librarian phase

## TLP

CLEAR
