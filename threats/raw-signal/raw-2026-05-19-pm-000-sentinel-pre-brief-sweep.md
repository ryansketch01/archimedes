---
raw_id: raw-2026-05-19-pm-000
collected_at: 2026-05-19T15:55:00-04:00
run_id: pre-brief-20260519-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: multi
  source_name: "Multi-source pre-brief collection sweep (15:30 EDT — feeds 16:00 afternoon brief)"
  source_url: null
  published_at: null
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: []
triage_tags:
  - sentinel
  - pre_brief_sweep_afternoon
  - non_promotable
  - fox_tempest_net_new_actor_cluster_pm_001_pm_002_pm_003
  - vanilla_tempest_storm_0501_storm_2561_storm_0249_microsoft_taxonomy_roster_gap
  - shai_hulud_mass_wave_639_versions_323_packages_pm_004_anti_noise_locked_vt006
  - drupal_psa_pre_disclosure_2026_05_20_pm_005
  - cve_2026_45829_chromadb_unpatched_rce_pm_006
  - eviltokens_phaas_oauth_device_code_pm_007_tradecraft_class_overlap_tycoon2fa_storm_2949
  - huawei_vrp_zero_day_luxembourg_post_telecom_pm_008
  - bitdefender_mshta_legacy_lolbin_trend_pm_009
  - cisa_ics_day_139_batch_siemens_ruggedcom_ape1808_cvss_10_cve_2026_0300_amplification_pm_010
  - cve_2026_20182_kev_carry_forward_t_plus_46h_lapsed
  - cve_2026_42897_kev_t_minus_10d_carry_forward
  - cve_2026_42945_nginx_rift_vulncheck_carry_forward
  - cve_2020_17103_miniplasma_halt_pending_test_carry_forward
  - symantec_fast16_provisional_a_ratification_clock_t_plus_73h_carry_forward
  - storm_2949_new_actor_candidate_carry_forward
  - mini_shai_hulud_cluster_locked_vt006_anti_noise_amplification_via_pm_004
  - shai_hulud_clone_wave_finding_2026_05_18_0003_carry_forward
  - grafana_coinbasecartel_finding_2026_05_18_0004_carry_forward
  - tycoon2fa_finding_2026_05_17_0002_carry_forward_eviltokens_tradecraft_class_overlap_pm_007
  - turla_kazuar_secret_blizzard_finding_2026_05_14_0006_carry_forward
  - seven_eleven_shinyhunters_finding_2026_05_18_0002_carry_forward
  - dormant_splunk_sweep_48
iocs_extracted: false
iocs_count: 0
text_word_count: 0
promoted: false
ttl_expires_at: 2026-08-17T15:55:00-04:00
---

# Pre-brief collection sweep 2026-05-19 15:30 EDT (feeds 16:00 afternoon brief)

## Sweep summary

**Mode:** pre_brief_collection
**Window:** 2026-05-19T07:30:00-04:00 → 2026-05-19T15:30:00-04:00 (~8h since morning brief b812307 + 12:00 FLASH sentinel)
**Disposition:** PRODUCTIVE — 10 raw-signal items written (pm-001 through pm-010); 1 sentinel tombstone (pm-000, this file).

## Sources queried (A/B-grade priority set)

| Source | Status | In-window items | Raw-signal disposition |
|---|---|---|---|
| **Microsoft MSTIC** | reachable 200 | **1** | pm-001 Fox Tempest MSaaS disruption (A1 originating) |
| **BleepingComputer** | reachable 200 | 6 in feed | pm-004 Shai-Hulud 639 versions / 323 packages mass wave (B2; net-new scale); others DISCARDED (Microsoft driver roadmap = product roadmap not threat-intel; Teams macOS prompts = UX not threat-intel; 7-Eleven update = anti-noise finding-2026-05-18-0002; sponsored BeyondTrust = filtered; webinar = filtered) |
| **The Hacker News** | reachable 200 | 3 | pm-007 EvilTokens OAuth device-code PhaaS (B2); DirtyDecrypt PoC = anti-noise (covered by am-009 morning); Trapdoor Android ad fraud = DISCARDED per Mode 1 (no A&D / no tracked actor / commodity ad-fraud class) |
| **SecurityWeek** | reachable 200 | 6 | pm-002 Fox Tempest relay (B2); pm-005 Drupal PSA (B2); pm-006 ChromaDB CVE-2026-45829 (B2); pm-009 Bitdefender MSHTA trend (B2); B1ack's Stash dump = DISCARDED per Mode 1 (carding cybercrime no A&D / no tracked actor); Cyber Resilience editorial = DISCARDED |
| **The Record** | reachable 200 | 3 | pm-003 Fox Tempest relay (B2); pm-008 Huawei VRP zero-day Luxembourg POST telecom (B2); UK deepfakes regulator = DISCARDED per Mode 1 (regulation news, no threat-intel) |
| **Dark Reading** | reachable 200 | 2 | Editorial reflection = DISCARDED; virtual event = DISCARDED |
| **CISA all.xml** | reachable 200 | **5** | pm-010 CISA ICS day-139 batch with Siemens RUGGEDCOM APE1808 + CVE-2026-0300 PAN-OS amplification (A1 cluster) |
| **CrowdStrike** | reachable 200 | 0 in-window via since-filter | Same 10 dateless items pattern as morning; Patch Tuesday May 2026 WebSearch-confirmed published 2026-05-12 pre-window |
| **SentinelLabs** | reachable 200 | 0 | |
| **Unit 42** | reachable 200 | 0 | |
| **SANS ISC** | reachable 200 | 0 | |
| **Krebs** | reachable 200 | 0 | |
| **Mandiant index page** | reachable 200 | 0 net-new | BlackFile UNC6671 (2026-05-15, pre-window) and GTIG AI Threat Tracker (2026-05-11, pre-window) at top; no fresh in-window posts. Feedburner 404 pattern continues. |
| **Talos blog** | **404** | source failure | blog.talosintelligence.com/feeds/posts/default 404 — third consecutive failure (failure_count 2→3 past-threshold); held healthy per operator-set notes pending alt-endpoint decision |
| **Volexity blog** | **parse error** | source failure | www.volexity.com/blog/feed/ malformed body XML parse error — fourth consecutive failure (failure_count 3→4 past-threshold); held healthy per operator-set notes |
| **Sophos** | **404** | source failure | news.sophos.com/en-us/feed/ 404 — fourth consecutive failure (failure_count 3→4 past-threshold); already stale per prior sweep, remains stale |

## Headline items this sweep

**Lead item — Fox Tempest malware-signing-service disrupted (multi-source A1+B2+B2 cluster):**
Microsoft MSTIC (A1) named **Fox Tempest** as the operator of a malware-signing-as-a-service (MSaaS) platform `signspace[.]cloud`, abusing Microsoft Artifact Signing to generate >1,000 fraudulent short-lived (72h) code-signing certificates over the May 2025 → May 2026 operational window. Microsoft DCU disrupted the infrastructure via U.S. District Court action unsealed 2026-05-19. Downstream actors: **Vanilla Tempest** (Rhysida ransomware), **Storm-0501**, **Storm-2561** (SEO poisoning / fake VPN), **Storm-0249**. Ransomware families enabled: Rhysida, INC, Qilin, Akira, BlackByte. Other malware: Oyster/Broomstick, Lumma Stealer, Vidar. Industry partner: Cloudzy. Sectors impacted downstream: healthcare, education, government, financial services. Geographic: US, France, India, China. IOCs (per MSTIC): signspace[.]cloud + GitHub `code-signing-service` repo + 2 SHA-1 cert fingerprints + 3 SHA-256 malware samples. **Roster gap**: Fox Tempest, Vanilla Tempest, Storm-0501, Storm-2561, Storm-0249 all NOT in `_roster.yaml`. /new-actor candidates for grader determination.

**Substantive expansion — Shai-Hulud mass wave (BleepingComputer relay of Socket / Endor Labs / Aikido Security / StepSecurity / Microsoft):**
**639 malicious npm versions** across **323 packages** published in a ~1h window on 2026-05-19 ~02:00 UTC, pivoting from compromised `atool` npm account in the `@antv` namespace. **~2,900 malicious GitHub repos** generated. Cluster Mini-Shai-Hulud-family but explicitly hedged by source: attribution is "more difficult" because TeamPCP's code was leaked on GitHub, used by others now. Net-new IOC: `t.m-kosche.com` (Microsoft credential-shipping endpoint), `filev2.getsession[.]org/file/` (Session P2P exfil). Persistence: VS Code + Claude Code config backdoors. Encryption: AES-256-GCM + RSA-OAEP wrapping. Sigstore + OIDC token abuse for legitimate-signing appearance. Anti-noise rule 1 locks FLASH-purposes to VT-006 (already FLASH-fired 2026-05-12); this raw-signal is grader-queue for VT-006 augmentation, finding-2026-05-18-0003 expansion, or net-new finding determination.

**Vulnerability cluster:**
- **CVE-2026-0300 amplification** via Siemens RUGGEDCOM APE1808 ICS-appliance class (CISA ICSA-26-139-02, CVSS 10.0) — federal KEV deadline LAPSED 2026-05-09 now T+10d+; the OT/ICS deployment surface adds DIB-supplier-facility risk on top of the IT-firewall surface
- **Drupal "highly critical" pre-disclosure** for 2026-05-20 17:00-21:00 UTC patch window (PSA only; CVE/CVSS embargoed)
- **CVE-2026-45829** ChromaDB pre-auth RCE via HuggingFace model loading — unpatched as of 1.5.8, ~73% of internet-accessible deployments affected (HiddenLayer first-citation)
- **ScadaBR four-CVE cluster** (CVE-2026-8602/8603/8604/8605, CVSS 9.1) — unauthenticated RCE in critical-manufacturing/dams/chemical/energy/water SCADA software

**Telecom infrastructure:**
- **Huawei VRP zero-day** behind Luxembourg POST nationwide outage 2025-07-23 — 10 months post-incident disclosure, no CVE assigned, no public Huawei advisory, no targeted-attack attribution per The Record investigation

**Tradecraft trend:**
- **EvilTokens** OAuth device-code PhaaS (340+ M365 orgs in 5 weeks; CSA research relay) — tradecraft-class overlap with Tycoon2FA finding-2026-05-17-0002 and Storm-2949 morning carry-forward, but explicitly NOT attributed by source
- **MSHTA legacy LOLBIN** abuse trend per Bitdefender Labs — Lumma / Amatera / ClipBanker / PurpleFox / Emmenhtal / HTA CountLoader family-class trend, no actor attribution

## Carry-forward themes preserved unchanged

Per upstream morning brief b812307 + 12:00 FLASH sentinel:

- **CVE-2026-20182** Cisco Catalyst SD-WAN UAT-8616 — federal KEV deadline LAPSED Sunday 2026-05-17 now T+46h+ post-deadline-lapse (finding-2026-05-14-0005 carry-forward)
- **CVE-2026-42897** Microsoft Exchange OWA XSS — federal KEV deadline T-10d Friday 2026-05-29 (finding-2026-05-15-0003 carry-forward)
- **CVE-2026-42945** NGINX Rift PoC + VulnCheck Canaries (finding-2026-05-16-0001 carry-forward)
- **CVE-2020-17103** MiniPlasma researcher PoC halt_pending_test (finding-2026-05-18-0001 carry-forward)
- **Symantec/SentinelLABS Fast16** provisional-A ratification clock T+73h+ past elapsed deadline 2026-05-16T18:25 (finding-2026-05-16-0003 carry-forward)
- **Pwn2Own Berlin 2026** Orange Tsai/DEVCORE Exchange RCE-to-SYSTEM ZDI embargo through ~2026-08-13 (finding-2026-05-16-0002)
- **Storm-2949** net-new MSTIC actor cluster — strong /new-actor candidate; possibly expanded to a Tempest/Storm broader cluster review with Fox Tempest pm-001 net-new addition this afternoon
- **Turla/Kazuar/Secret Blizzard** D+4 anti-noise rule 1 active (finding-2026-05-14-0006)
- **Tycoon2FA** device-code PhaaS — anti-noise rule 1 active (finding-2026-05-17-0002); EvilTokens pm-007 tradecraft-class overlap noted
- **7-Eleven/ShinyHunters** finding-2026-05-18-0002 — BleepingComputer 14:16 EDT confirms 7-Eleven officially confirmed the April 8 breach; anti-noise applies
- **Shai-Hulud npm clone wave** finding-2026-05-18-0003 — pm-004 today's mass wave is a meaningful expansion data point
- **Grafana / CoinbaseCartel / ShinyHunters / SLSH** finding-2026-05-18-0004 + finding-2026-05-17-0001

## Splunk first-party sweep

30-token query across `archimedes` + `defenseclaw_local` indexes over -30d returned:

```
45 events sourcetype=archimedes:operation index=archimedes
0 events index=defenseclaw_local
0 external IOC matches
```

**48th consecutive dormant non-self-telemetry sweep** per established cadence (+1 from morning b812307 sentinel's 47-sweep streak). Silence is not disconfirming per the established dormancy precedent across the b812307 / 1513d98 / a8121bc / ac3683d / 463d631 / 8280b8d chain.

## Source-health changes proposed

Runtime-fields-only edits per CLAUDE.md operator-vs-runtime field ownership doctrine. Operator-set `notes` fields preserved verbatim.

- `cisco-talos` failure_count 2→3 (past-threshold; held healthy per operator-set instruction; alt-endpoint decision still pending — third consecutive 404 in three sweep windows)
- `volexity` failure_count 3→4 (past-threshold; held healthy per operator-set instruction; fourth consecutive malformed-body parse error)
- `sophos` remains stale (no change — fourth consecutive 404, already at stale per morning brief)
- `bleepingcomputer` last_successful_fetch 2026-05-19T07:30 → 2026-05-19T15:30 (productive sweep)
- `thehackernews` last_successful_fetch 2026-05-19T07:30 → 2026-05-19T15:30 (productive sweep)
- `securityweek` last_successful_fetch 2026-05-19T07:30 → 2026-05-19T15:30 (productive sweep)
- `the-record` last_successful_fetch 2026-05-19T07:30 → 2026-05-19T15:30 (productive sweep)
- `mstic` last_successful_fetch 2026-05-19T07:30 → 2026-05-19T15:30 (productive sweep — Fox Tempest)
- `cisa-advisories` last_successful_fetch 2026-05-19T07:30 → 2026-05-19T15:30 (productive sweep — ICS-CERT day-139 batch)
- `splunk-archimedes` last_successful_fetch 2026-05-12T06:00 → 2026-05-19T15:30 (productive — 45 self-telemetry events confirming dormancy streak)
- `splunk-defenseclaw` last_successful_fetch 2026-05-12T06:00 → 2026-05-19T15:30 (productive — 0 hits, confirming dormancy)
- `sans-isc` last_successful_fetch 2026-05-19T07:30 → 2026-05-19T15:30 (0 items in window but feed reachable)
- `krebs` last_successful_fetch 2026-05-19T07:30 → 2026-05-19T15:30 (0 items in window but feed reachable)

## Hard Rules compliance verified this sweep

- **Rule 1** (legal-policy): no prohibited query patterns triggered. SpiderFoot not invoked. authorized-targets.yaml empty.
- **Rule 2** (no Archimedes-originated attribution): Fox Tempest preserved as "Microsoft assesses" framing; Vanilla Tempest / Storm-* preserved as Microsoft taxonomy; Shai-Hulud new wave preserves "attribution ... more difficult" hedge; EvilTokens NOT propagated to Tycoon2FA or Storm-2949; Huawei VRP zero-day preserves "no evidence ... specifically directed" hedge; Bitdefender MSHTA trend has no actor attribution.
- **Rule 3** (no exploitation assistance): zero PoC code, zero exploit walkthroughs across pm-001 through pm-010. DirtyDecrypt PoC URL not linked. Artifact Signing abuse described conceptually only. ChromaDB `kwargs` mechanism described at trust-boundary level only. Drupal PSA had no exploitation detail (embargoed). Shai-Hulud loader walk-through not copied.
- **Rule 4** (no third-party scanning): passive only across all items. No active scans of signspace[.]cloud (defunct), Huawei devices, ChromaDB internet-accessible instances, or any other infrastructure.
- **Rule 5** (HIGH threat-level human sign-off): not in scope this sweep — no actor scoring performed.
- **Rule 6** (15-word quote limit + 1 quote per source): zero quotes shipped in this sentinel. Quotes managed individually in pm-001 through pm-010 where attribution-language fidelity required source-verbatim preservation; all in compliance.
- **Rule 7** (copyright discipline): substantial text included in raw-signal bodies for grader context per collector charter; quote-limit applied separately to extraction notes.
- **Rule 8** (Splunk first-party priority): Splunk sweep returned only self-telemetry pipeline events — silence is not disconfirming per the established 47-sweep + 1-this-sweep = 48-sweep dormancy cadence.

LEGAL-POLICY prohibited-query-patterns not triggered. Hard Rule 5 not in scope. No Discord post (collection-phase tombstone). No _master-index.yaml regeneration (sentinel writes no IOCs; net-new IOCs from pm-001 through pm-010 will be handled by afternoon grader via VT-006 augmentation, finding creation for Fox Tempest cluster, vuln-tracker queue evaluation for CVE-2026-45829 + Drupal PSA + ScadaBR cluster, and/or roster gap evaluation for Fox Tempest / Vanilla Tempest / Storm-0501 / Storm-2561 / Storm-0249).

TLP:CLEAR.
