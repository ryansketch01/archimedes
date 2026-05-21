---
raw_id: raw-2026-05-21-pm-000-sentinel
collected_at: 2026-05-21T15:32:00-04:00
run_id: pre-brief-20260521-153000
collection_mode: pre_brief_collection
sentinel: true
test: false
source:
  source_yaml_id: archimedes-internal
  source_name: "Archimedes collector sentinel — 2026-05-21 afternoon pre-brief sweep"
  source_url: null
  published_at: 2026-05-21T15:32:00-04:00
sweep_window:
  start: 2026-05-21T08:00:00-04:00
  end: 2026-05-21T15:30:00-04:00
sources_queried:
  - cisa-kev               # WebFetch known_exploited_vulnerabilities.json — 2 NEW KEV adds dated 2026-05-21: CVE-2025-34291 (Langflow CORS/SameSite refresh-token RCE) + CVE-2026-34926 (Trend Micro Apex One on-premise directory traversal); dueDate 2026-06-04 each. KnownRansomwareCampaignUse=Unknown both. Raw-signaled as PM-001 (procedural-facts + A&D-tier-2/3-EDR-deployment relevance for Trend Micro Apex One).
  - cisa-advisories        # all.xml fetch_feed 200, 5 in-window ICS advisories all dated 2026-05-21T12:00 UTC = 08:00 EDT (right at morning-brief cutoff, NOT in morning brief): ICSA-26-141-01 Hitachi Energy GMS600 CVSS 5.9 (Critical Manufacturing); ICSA-26-141-02 ABB B&R PCs CVSS unspecified (Energy, 9 CVEs from 2023 SinoCMS lineage); ICSA-26-141-03 ABB B&R Automation Studio CVSS 9.8 LEAD (Energy, 24+ CVE deep-dependency batch including 2015-2024 lineage); ICSA-26-141-04 ABB B&R Automation Runtime CVSS 6.1 (Energy, predictable identifiers + XSS + CSV formula injection); ICSA-26-141-05 ABB Terra AC Wallbox CVSS 6.1 (Energy, EV charger heap/buffer overflow). Raw-signaled batch as PM-006 (5-advisory ICS batch with ABB B&R Automation Studio CVSS 9.8 as lead).
  - nvd                    # REST API lastModStartDate=2026-05-21T12:00Z lastModEndDate=2026-05-21T19:30Z cvssV3Severity=CRITICAL → 13 results. Two A&D-relevant items: CVE-2026-41144 (NASA F´/F-Prime Flight Software arbitrary file write→RCE; NVD 9.8 vs vendor GitHub advisory 0.0/Low — CNA-vendor downgrade divergence pattern — raw-signaled as PM-003); CVE-2026-3593 (ISC BIND 9 DoH heap use-after-free; NVD 9.8 vs vendor ISC kb.isc.org assessment CVSS 7.4 — vendor-downgrade pattern; ISC explicitly states 'we are not aware of any active exploits' — raw-signaled as PM-007 adjacency to NLnet Unbound dual-criticals from morning brief finding-2026-05-21-0005). Other 11 entries non-A&D / consumer-software / metadata-refresh on 2023-vintage CVEs (Digital Ant E-Commerce SQLi 2023-3651, Exagate SYSGuard 2023-4669, Erlang OTP httpd 2026-23941 Mar 13 publication, pgx PostgreSQL Go driver 2026-41889 May 8 publication, ScadaBR 2026-8602/8603/8605 May 19 publication — already in CISA ICSA-26-139-03 from 2026-05-19, Taiko AG1000 SMS Alert Gateway 2026-9139 May 20, HP Linux Imaging hpcups 2026-8631 May 20, Avada Fusion Builder 2026-6279 — already DISCARDED at 06:00+morning sentinel as WordPress consumer/SMB, Divi Form Builder WordPress 2026-5118 May 21). All 11 DISCARDED per Mode 1 procedure.
  - mstic                  # Microsoft Security Blog feed 200, last_modified 2026-05-21T16:26 GMT, 1 in-window item — 'What's new in Microsoft Security: May 2026' by Alym Rayani (16:00 GMT = 12:00 EDT). Marketing roundup of Microsoft Purview DSPM + Entra ID Account recovery + Windows 365 for Agents + Microsoft Agent 365 + OCR additions to Data Security Investigations. NO threat intelligence content, NO CVE, NO actor, NO IOC, NO incident report. DISCARDED per Mode 1 procedure (non-threat-intel marketing content).
  - unit42                 # feedburner 200, last_modified 2026-05-21T16:27 GMT, 1 in-window item — 'The npm Threat Landscape: Attack Surface and Mitigations (Updated May 21)' by Unit 42 (15:30 GMT = 11:30 EDT). UPDATE on the npm Threat Landscape live-document covered yesterday and in this morning's brief finding-2026-05-21-0007. WebFetch confirms 2026-05-21 update added managed-threat-hunting XQL Cortex XDR query for Mini Shai-Hulud (tracks JavaScript-via-Bun + gh-auth-token credential access) PLUS Koi Agentic Endpoint Security defensive-control integration (delays automatic package updates). NO new IOCs, NO new CVEs, NO new actor attribution per WebFetch — focus on detection-engineering operationalization layer. Raw-signaled as PM-004 (procedural-facts upgrade to morning finding-0007 — defender-tooling layer additions, not attribution change).
  - mandiant               # feedburner persistent 404 (~19+ consecutive sweeps); cloud.google.com/blog/topics/threat-intelligence/rss/ alt malformed body (same pattern as prior sweeps); not separately WebFetched on index page this sweep — pattern entrenched, operator alt-endpoint decision still pending.
  - crowdstrike            # feed reachable but persistent dateless-marketing pattern (~18+ consecutive sweeps); 0 in-window threat-intel items.
  - rapid7                 # rapid7.com/blog/rss/ 200, last_modified 2026-05-21T19:17 GMT, 1 in-window item — 'Q1 2026 Threat Landscape Report: Zero-clicks, geopolitical tensions, and some wins for law enforcement' by Rapid7 Labs (13:00 GMT = 09:00 EDT). Quarterly aggregate — KEY FINDING: vulnerability exploitation surpassed social engineering as top initial access vector at 38% of total; over 50% of exploited vulns are zero-click network-facing; pure-extortion ransomware tactic shift; Iranian state-aligned + Russian + Chinese campaigns named (no specific actors). Raw-signaled as PM-005 (sector-strategic-context: defensive-posture implication that prime IR teams should re-weight perimeter / zero-click-network-facing-vuln patching cadence relative to social-engineering controls).
  - cisco-talos            # blog.talosintelligence.com RSS feed 200, 1 in-window item — 'The art of being ungovernable' Threat Source newsletter by William Largent (18:00 GMT = 14:00 EDT). Career-advice editorial framing with sub-mention of BadIIS commodity malware-as-a-service (Chinese-speaking cybercrime groups, lwxat developer alias, xshen customer alias). Original BadIIS post is 2026-05-19 (pre-window per WebFetch verification on /from-pdb-strings-to-maas-tracking-a-commodity-badiis-ecosystem/). NOT A&D / NOT tracked-actor / off-window for the dedicated post / commodity-MaaS-not-APT framing. DISCARDED per Mode 1 procedure (no watchlist / roster / vuln-index hit).
  - sentinelone            # SentinelLabs feed 200, last_modified 2026-05-21T16:47 GMT, 0 in-window items.
  - proofpoint             # /rss.xml 200, last_modified 2026-05-21T17:02 GMT, 1 in-window item — Proofpoint integrates with Claude Compliance API to extend data security to Claude (16:34 GMT = 12:34 EDT). Vendor product-integration press release, NO threat intelligence, NO CVE, NO actor, NO IOC. DISCARDED per Mode 1 procedure.
  - welivesecurity         # ESET feed 200, 0 items in window.
  - krebs                  # feed 200, last_modified 2026-05-19T14:19 GMT pre-window, 0 in-window items.
  - sans-isc               # RSS 200, last_modified 2026-05-21T19:29 GMT, 1 in-window item — 'Selective HTTP Proxying in Linux' diary by Didier Stevens (13:34 GMT = 09:34 EDT). Defensive-tooling diary, NO actor / NO CVE / NO IOC / NO A&D mention. DISCARDED per Mode 1 procedure (no watchlist / roster / vuln-index hit).
  - theregister-security   # atom 200, 2 in-window items — HackerOne axes IBB bug bounty payouts 75%+ reduction (19:27 GMT, ecosystem-policy editorial with Linux Torvalds AI-bug-report quote, NO threat intel content, DISCARDED); Myspace93 2021 breach plaintext 46k credentials surfaced by HIBP (12:20 GMT, breach-aggregator chronicle, NO A&D / NO roster / NO CVE, DISCARDED).
  - bleepingcomputer       # RSS 200, last_modified 2026-05-21T19:22 GMT, 1 in-window item via RSS — 'Google accidentally exposed details of unfixed Chromium flaw' by Bill Toulas (18:13 GMT = 14:13 EDT). Chromium Service Worker persistence RCE bug reported December 2022 by Lyra Rebane, marked fixed 2026-02-12 (without patch shipped), access restrictions removed 2026-05-20 making issue tracker entry publicly accessible for ~24h before re-restricted, but exploit still confirmed functional on Chrome Dev 150 + Edge 148 as of 2026-05-20. Universal Chromium-based browser exposure (Chrome, Edge, Brave, Opera, Vivaldi, Arc). Researcher Lyra Rebane: 'turning any Chromium-based browser into a permanent JS botnet member.' No CVE assigned per article. NO active exploitation reported but vendor exposure makes 'pretty easy.' Raw-signaled as PM-002 (universal-browser-RCE A&D dev-workstation exposure tier). Additional homepage WebFetch confirmed 10 total 2026-05-21 BleepingComputer headlines incl. Showboat/Calypso/Red Lamassu China-telecoms espionage at 14:00 GMT (anti-noise DEDUP'd against 12:00 FLASH sentinel discard — telecoms targeting NOT A&D, NOT tracked actor) and Cisco Secure Workload CVE-2026-20223 (anti-noise DEDUP'd against 2026-05-20 afternoon brief finding-2026-05-20-0001) and Microsoft Defender pair (anti-noise DEDUP'd against KEV-7 batch lock through 2026-05-21T16:00 + this morning's brief UPDATE finding).
  - thehackernews          # feedburner 200, last_modified 2026-05-21T18:46 GMT, 0 items in 3.5h since-12:00 window. Homepage WebFetch confirmed 6 total 2026-05-21 headlines: Showboat (12:00 FLASH DEDUP); ThreatsDay Bulletin aggregator (DISCARDED — multi-topic synthesis); Microsoft Defender pair (KEV-7 batch DEDUP); 9-year-old Linux CVE-2026-46333 (06:00 sentinel DISCARD — CVSS 5.5 below Trigger 1 floor + no A&D + commodity); GitHub Nx Console breach (morning brief DEDUP via finding-0002); Drupal SA-CORE-2026-004 CVE-2026-9082 (morning brief DEDUP via finding-0004).
  - securityweek           # RSS feed 200, last_modified 2026-05-21T12:04 GMT, 0 items in 3.5h since-12:00 window. Homepage WebFetch confirmed 5 total 2026-05-21 headlines: Cisco Secure Workload CVE-2026-20223 (2026-05-20 afternoon brief DEDUP); Drupal CVE-2026-9082 (morning brief DEDUP via finding-0004); Microsoft UnDefend/RedSun (morning brief DEDUP via finding-0001); Google Chrome AI vuln discovery surge 5:37 AM ET (morning sentinel DISCARDED — research-piece no CVEs); Supply Chain Security Crisis editorial (Black Kite repeated DISCARD from prior sweeps).
  - therecord              # feed 200, last_modified post 2026-05-21T19:01 GMT, 2 items in 3.5h since-12:00 window — Tech giants promise UK Ofcom child-protection changes (19:01 GMT, regulatory/policy DISCARDED no threat intel); Two Americans plead guilty India tech-support scam centers (18:02 GMT, LE-action DISCARDED no actor attribution to roster).
  - cybersecuritydive      # feeds/news/ 200, last_modified 2026-05-21T15:00 GMT, 0 items in 3.5h since-12:00 window. Prior 12:00 FLASH window's Grafana Labs / GitHub TanStack item already anti-noise DEDUP'd against this morning's brief.
  - splunk-first-party     # archimedes + defenseclaw_local indexes earliest=-8h, 0 non-self events. 1 archimedes:operation event = 12:00 EDT flash-sweep-clean self-telemetry from this morning's 12:00 FLASH sentinel run (handoff_notes flagged Calypso/Red Lamassu for actor-profiler /new-actor consideration). 6 archimedes:scheduler self-events. NO defenseclaw_local hits matching watchlists / IOC index. 53rd consecutive dormant non-self sweep across pre-brief + flash-sweep cadence.
match_reason:
  watchlist: []
  actors: []                       # no roster-actor activity surfaced in window
  vulnerabilities:
    - CVE-2025-34291               # Langflow CORS/SameSite refresh-token RCE — KEV-added 2026-05-21
    - CVE-2026-34926               # Trend Micro Apex One on-premise directory traversal — KEV-added 2026-05-21
    - CVE-2026-41144               # NASA F´ flight software arbitrary file write → RCE; NVD 9.8 vs vendor downgrade 0.0
    - CVE-2026-3593                # ISC BIND 9 DoH heap use-after-free; NVD 9.8 vs vendor 7.4
  keywords:
    - kev_double_add_2026_05_21
    - langflow_ai_orchestration
    - trend_micro_apex_one_on_premise
    - cisa_kev_actively_exploited
    - chromium_service_worker_rce
    - google_issue_tracker_accidental_exposure
    - edge_brave_opera_vivaldi_arc_chromium_lineage
    - browser_persistent_javascript_botnet_potential
    - nasa_fprime_flight_software
    - spacecraft_flight_software_rce
    - cve_to_vendor_score_divergence_pattern
    - unit_42_mini_shai_hulud_managed_threat_hunting
    - cortex_xdr_xql_detection_query
    - koi_agentic_endpoint_security
    - rapid7_q1_2026_threat_landscape
    - vulnerability_exploitation_top_iav_38_percent
    - zero_click_network_facing_50_percent
    - pure_extortion_ransomware_shift
    - cisa_ics_advisory_batch_2026_05_21
    - abb_br_automation_studio_cvss_9_8
    - hitachi_energy_gms600
    - abb_terra_ac_wallbox_ev_charger
    - critical_manufacturing_energy_sector
    - isc_bind_9_doh_heap_uaf
    - dns_over_https_attack_surface
    - nvd_vs_vendor_cvss_disagreement
triage_tags:
  - pre_brief_sentinel
  - sweep_complete
  - 7_5h_window
  - splunk_first_party_zero_hits_53rd_consecutive_dormant_sweep
  - kev_double_add_event
  - nasa_fprime_spacecraft_a_and_d_direct
  - cisa_ics_batch_5_advisories
  - unit_42_npm_landscape_update_third_24h_cycle
  - rapid7_q1_landscape_report
  - chromium_universal_browser_rce_exposure
  - mandiant_feedburner_persistent_404_unchanged_19th_consecutive_sweep
iocs_extracted: false
iocs_count: 0
text_word_count: 0
promoted: false
ttl_expires_at: 2026-08-19T15:32:00-04:00
---

# Archimedes collector sentinel — 2026-05-21 afternoon pre-brief sweep

## Summary

Productive sweep. 23 sources queried; 7 raw-signal files written (PM-001 through PM-007). Most consequential surfaces:

1. **CISA KEV double-add at 2026-05-21**: CVE-2025-34291 (Langflow AI orchestration platform CORS/SameSite refresh-token CORS-bypass RCE) + CVE-2026-34926 (Trend Micro Apex One on-premise directory traversal — pre-auth local injection of key table to deploy malicious code to agents). Federal-civilian deadline 2026-06-04 (both). Trend Micro Apex One direct A&D Tier-2/3 EDR-deployment relevance. Both KnownRansomwareCampaignUse=Unknown. Raw-signaled PM-001.

2. **NASA F´ (F Prime) flight software CVE-2026-41144**: NVD CVSS 9.8 CRITICAL (integer overflow → arbitrary file write → RCE on embedded targets) vs vendor GitHub advisory CVSS 0.0/Low — CNA-vendor downgrade divergence pattern identical to NVIDIA TRT-LLM cluster (this morning's AM-003) and Microsoft Defender pair codename-binding inversion. F Prime is NASA-developed open-source flight software framework used in spacecraft / CubeSats / lunar missions / planetary probes. Direct A&D relevance — primes building spacecraft components and university/research partners on NASA missions. Raw-signaled PM-003.

3. **Universal Chromium Service Worker RCE**: BleepingComputer (Bill Toulas) reports Google accidentally re-exposed an unfixed Chromium issue-tracker entry on 2026-05-20 (~24h public window). Original December 2022 Lyra Rebane report; marked "fixed" 2026-02-12 without patch shipped; researcher confirmed exploit still functional on Chrome Dev 150 + Edge 148 as of 2026-05-20. Affects all Chromium-derived browsers (Chrome, Edge, Brave, Opera, Vivaldi, Arc). Persistent background JavaScript execution after browser close — researcher characterization: "permanent JS botnet member." No CVE assigned. NO active exploitation reported but exposure makes "pretty easy" per researcher. A&D dev-workstation universal-browser-exposure tier. Raw-signaled PM-002.

4. **Unit 42 npm Threat Landscape Update May 21**: Live-document third 24h update cycle adds managed-threat-hunting Cortex XDR XQL query (tracks Bun-JavaScript + gh-auth-token credential access — Mini Shai-Hulud-specific detection) + Koi Agentic Endpoint Security defensive-control integration (delays automatic package updates). NO new IOCs / CVEs / actor attribution per WebFetch — detection-engineering operationalization layer, not attribution-layer change. Raw-signaled PM-004 as procedural-facts upgrade to this morning's finding-0007 (MSTIC + Unit 42 same-day MSH @antv co-publication).

5. **Rapid7 Q1 2026 Threat Landscape Report**: Vulnerability exploitation surpassed social engineering as the #1 initial access vector at 38% of total (up from sub-30% in prior quarters); over 50% of exploited vulnerabilities are zero-click network-facing (no auth, no user interaction). "Pure extortion" shift in ransomware (rapid exfil over encrypt). Iranian state-aligned + Russian + Chinese campaigns named at thematic level (no specific actor named in summary). Sector-strategic defensive-posture context for prime IR teams: re-weight perimeter / zero-click-network-facing patch cadence relative to social-engineering controls. Raw-signaled PM-005.

6. **CISA ICS 5-advisory batch dated 2026-05-21**: ABB B&R Automation Studio (ICSA-26-141-03) CVSS 9.8 LEAD — Energy sector critical-infrastructure deployment, 24+ CVE deep-dependency batch including 2015-2024 lineage updates. Plus ABB B&R PCs (-02, 9 CVEs, SinoCMS lineage), ABB B&R Automation Runtime (-04, 6.1 max), ABB Terra AC Wallbox EV charger (-05, 6.1), Hitachi Energy GMS600 (-01, 5.9 OpenSSL CVE-2022-4304 timing-side-channel). All Critical Manufacturing + Energy critical-infrastructure-sector deployment — defense supply chain relevance (ABB B&R is widespread in DIB manufacturing control systems). Published 12:00 UTC = 08:00 EDT, right at morning brief cutoff. Raw-signaled batch as PM-006.

7. **ISC BIND 9 CVE-2026-3593**: DNS-over-HTTPS heap use-after-free; NVD CVSS 9.8 vs vendor ISC kb.isc.org CVSS 7.4 — vendor-downgrade divergence pattern, third instance this sweep cycle. ISC explicitly states "we are not aware of any active exploits." DoH-specific attack surface (BIND 9.20.0-9.20.22 + 9.21.0-9.21.21). Adjacency interest to this morning's finding-0005 NLnet Labs Unbound dual criticals — same network-infrastructure layer at primes/suppliers running self-hosted recursive DNS. Raw-signaled PM-007.

## Non-productive surfaces (DEDUP / DISCARD trail preserved for grader visibility)

- **Showboat/Calypso/Red Lamassu China-telecoms espionage** (BleepingComputer + Hacker News): 12:00 FLASH sentinel DISCARD — telecoms NOT A&D, NOT tracked actor; flagged for actor-profiler /new-actor consideration via 12:00 FLASH handoff_notes.
- **Cisco Secure Workload CVE-2026-20223**: 2026-05-20 afternoon brief finding-2026-05-20-0001 anti-noise lock.
- **Microsoft Defender UnDefend/RedSun pair**: morning brief UPDATE-finding + KEV-7 batch lock through 2026-05-21T16:00.
- **9-year-old Linux Kernel CVE-2026-46333**: 06:00 sentinel + morning sentinel DISCARD — CVSS 5.5 below Trigger 1 floor.
- **Google Chrome AI vuln discovery surge**: morning sentinel DISCARD — research piece, no CVEs.
- **Cisco Talos BadIIS commodity MaaS**: Original post 2026-05-19 (pre-window). China-speaking cybercrime, off-roster, off-A&D.
- **HackerOne IBB payout cuts**: ecosystem-policy editorial, no threat intel.
- **Myspace93 2021 breach plaintext credentials**: legacy breach surfaced via HIBP, no A&D / no roster.
- **Microsoft Security Blog May 2026 roundup**: product marketing, no threat intel.
- **Proofpoint × Claude Compliance API**: product-integration press release, no threat intel.
- **The Record items**: UK Ofcom kids online + India call center scams, off-filter.

## Source-health changes this sweep

| Source | Status pre | Status post | Notes |
|---|---|---|---|
| (no flips this sweep) | — | — | All productive sources reachable; Mandiant feedburner persistent 404 unchanged (~19+ sweeps); Dragos/blog/feed/ 404 unchanged since 2026-05-13; ars-security feed 404 stale-skipped per under-24h rule (stale_since 2026-05-09 well past 24h — should be retry-eligible next sweep). |

## Extraction notes

- Pre-brief sweep window: 7.5h (08:00 → 15:30 EDT), substantially larger than typical 6h FLASH window
- 7 raw-signal files produced (PM-001 through PM-007) — productive sweep
- Splunk first-party check: 53rd consecutive dormant non-self sweep (no defenseclaw_local watchlist hits)
- No FLASH trigger evaluation this run (Mode 1 pre-brief, not Mode 2 FLASH); KEV double-add at 2026-05-21 would be evaluated against Trigger 1 (critical-CVE-exploited) at next 18:00 FLASH sweep — Langflow CORS-bypass is CVSS-pending (KEV listing does not include CVSS prima facie) and Trend Micro Apex One requires pre-auth local access (CWE-23) — neither obviously crosses Trigger 1 9.0 floor with active-exploitation prong without further enrichment
- 8 unique CVE references across PM-001 through PM-007 (CVE-2025-34291, CVE-2026-34926, CVE-2026-41144, CVE-2026-3593, plus ABB B&R Automation Studio dependency lineage CVEs in PM-006 batch frontmatter)
- Sentinel published before raw-signal PM-001 through PM-007 timestamps to anchor the sweep
