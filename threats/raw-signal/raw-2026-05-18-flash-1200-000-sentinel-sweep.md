---
raw_id: raw-2026-05-18-flash-1200-000
collected_at: 2026-05-18T12:05:00-04:00
run_id: flash-sweep-20260518-120000-off-cadence
collection_mode: flash_sweep
source:
  source_yaml_id: multi
  source_name: "Multi-source FLASH sweep (operator-triggered off-cadence, 12:00 EDT Monday)"
  source_url: null
  published_at: null
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: []
triage_tags:
  - sentinel
  - flash_sweep_clean
  - operator_triggered_off_cadence
  - dormant_splunk_sweep_43
  - scheduled_1200_window
  - quiet_hours_inactive
  - non_promotable
  - cve_2026_20182_kev_deadline_post_lapsed_t_plus_14h
  - cve_2026_42897_kev_t_minus_11d
  - symantec_provisional_a_clock_fired_t_plus_41h
  - shinyhunters_coinbasecartel_cluster_refinement_observed
  - grafana_breach_named_victim_detail_layer_refinement
  - cyera_first_corpus_surface_openclaw_claw_chain_patched
  - npm_clone_family_extension_anti_noise_lock
  - multivendor_critical_patch_roundup_ivanti_fortinet_sap_vmware_n8n
  - healthcare_breach_aggregate_no_attribution_observed
iocs_extracted: false
iocs_count: 0
text_word_count: 0
promoted: false
promoted_note: "Sentinel tombstone — non-promotable per established precedent (raw-2026-05-17-flash-*-000 chain through raw-2026-05-18-flash-0000-000 / 0600-000 immediate predecessors). Operator-triggered off-cadence sweep at 12:00 EDT post-08:00 morning brief b812307 (Hard Rule 2 + LEGAL-POLICY compliant); 6h fresh window since 06:00 FLASH a8121bc. Quiet-hours INACTIVE (12:00 EDT inside 09:00-21:00 active window — any trigger would have qualified for live #flash-alerts post, but 0 of 6 triggers fired). Eight in-window items evaluated and all DISCARDED for FLASH purposes: (1) SecurityWeek 'Claw Chain OpenClaw' Ionut Arghire 08:14 EDT — Cyera-originating four-CVE chain (CVE-2026-44112 CVSS 9.6 race condition + CVE-2026-44113/44115/44118), OpenClaw AI assistant, >60,000 publicly accessible instances, PATCHED April 23 (26d before publication), no active-exploitation claim, no tracked actor; Cyera not in source-grades.yaml first corpus surface (conservative-grade-pending evaluation if pursued; consistent with Sysdig 2026-05-14 / Zellic 2026-05-14 / depthfirst 2026-05-14 first-surface pattern); Trigger 1 FAIL (no A-grade source, no exploitation) + Trigger 6 FAIL (patched before disclosure); status-update CANDIDATE for vuln-tracker addition to _index.yaml if A&D-prime adoption of OpenClaw AI assistant emerges in subsequent surfaces. (2) SecurityWeek 'Millions Impacted Across Several US Healthcare Data Breaches' Eduard Kovacs 08:58 EDT — multi-victim aggregate digest covering NYC Health and Hospitals 1.8M + Nacogdoches Memorial 2.5M + Erie Family Health Centers 570K + Florida Physician Specialists 276K + Coastal Carolina Health Care 110K + Western Orthopaedics 110K; explicit 'None of these healthcare data breaches appears to have been claimed by known cybercrime groups' no-attribution language preserved verbatim per Hard Rule 2; healthcare sector NOT A&D watchlist; all 6 triggers FAIL. (3) BleepingComputer 'Grafana says stolen GitHub token...' Bill Toulas 09:46 EDT — net-new detail layer on Grafana cluster previously discarded in 06:00 FLASH a8121bc as item #3; cluster narrowing observed verbatim: BleepingComputer 'CoinbaseCartel consists of ShinyHunters and Lapsus$ affiliates' DROPS Scattered Spider from prior SecurityWeek 'Coinbase Cartel linked to ShinyHunters, Scattered Spider, and Lapsus$' framing per Hard Rule 2 narrower-source-preferred treatment; NEW IOC-class indicator 'shinysp1d3r' in-memory tool referenced (researchers unnamed by source — relay-of-unnamed-researchers attribution chain, Archimedes does NOT propagate); 'no evidence customer data or personal information was exposed' / 'customer systems remained unaffected' Grafana victim self-disclosure scope-bounding preserved; no A-grade vendor (Mandiant / CrowdStrike / Unit 42 / MSTIC / Volexity / Bitdefender / ESET / Symantec / Talos) cited; Trigger 2 FAIL — CoinbaseCartel + ShinyHunters + Lapsus$ all NOT in _roster.yaml; Scattered Spider (#013 HIGH) is in roster but is NOT attributed to Grafana incident by this BleepingComputer source (narrower framing); Hard Rule 2 + LEGAL-POLICY no-attribution-laundering binding constraint prevents Archimedes propagating Scattered-Spider-from-the-prior-SecurityWeek-relay to Grafana; anti-noise rule 1 active on Grafana cluster (T+6h since first observed); status-update CANDIDATE for 16:00 afternoon brief grader as cluster-anchor refinement and ShinyHunters / CoinbaseCartel /new-actor candidate set. (4) THN 'Ivanti, Fortinet, SAP, VMware, n8n Patch RCE...' Ravie Lakshmanan 06:54 EDT (16:24 IST) — multi-vendor patch roundup covering Ivanti Xtraction CVE-2026-8043 CVSS 9.6 + Fortinet FortiAuthenticator CVE-2026-44277 CVSS 9.1 + Fortinet FortiSandbox CVE-2026-26083 CVSS 9.1 + SAP S/4HANA CVE-2026-34260 CVSS 9.6 + SAP Commerce Cloud CVE-2026-34263 CVSS 9.6 + VMware Fusion CVE-2026-41702 CVSS 7.8 + n8n CVE-2026-42231 / 42232 / 44791 / 44789 / 44790 CVSS 9.4 all; ALL patched at publication, NO active-exploitation claims for any cohort item, no CISA KEV addition mentioned, no tracked actor; Trigger 1 FAIL uniformly across all cohort items + Trigger 6 FAIL uniformly (patches available before publication); status-update CANDIDATE for vuln-tracker evaluation if any cohort item enters A&D-prime enterprise inventory exposure context (Fortinet FortiAuthenticator + FortiSandbox + SAP S/4HANA all widely-deployed in Tier-1 SDLCs but no operator-mandated tracking yet). (5) THN 'Developer Workstations Are Now Part of the Software Supply Chain' 07:23 EDT (16:53 IST) — opinion/digest editorial covering 'three supply chain campaigns... within 48 hours' (Mini Shai-Hulud / Mini Sha1-Hulud clones / TeamPCP / node-ipc / OpenAI TanStack carry-forward set), no novel attribution, no novel CVE, no novel IOC, mention-class only; anti-noise rule 1 active on overlapping carry-forwards. (6) THN 'Weekly Recap: Exchange 0-Day, npm Worm, Fake AI Repo, Cisco Exploit and More' 09:50 EDT (19:20 IST) — pure weekly digest covering CVE-2026-42897 + Shai-Hulud / TeamPCP + Fake AI Repo + CVE-2026-20182 Cisco Catalyst SD-WAN — all carry-forwards already evaluated; no novel content. (7) THN 'Four Malicious npm Packages Deliver Infostealers and Phantom Bot DDoS Malware' Ravie Lakshmanan 04:57 EDT (14:27 IST) — Ox Security primary attributes Shai-Hulud clones to single npm user 'deadcode09284814' EXPLICITLY distinct from TeamPCP (verbatim: actor 'repurposed publicly released code rather than being affiliated with TeamPCP itself'); 4 packages chalk-tempalte (825 downloads) + @deadcode09284814/axios-util (284) + axois-utils (963) + color-style-utils (934); Phantom Bot Golang DDoS botnet HTTP/TCP/UDP + infostealer + Shai-Hulud worm clone payload triple-deliverable; NEW C2 IOCs 87e0bbc636999b.lhr[.]life + 80.200.28[.]28:2222 + edcf8b03c84634.lhr[.]life + GitHub indicator 'A Mini Sha1-Hulud has Appeared'; same cluster as 06:00 FLASH a8121bc Item #2 (already absorbed into morning brief b812307 as Other Signal mention-class with dependency-tree-quarantine watchlist recommendation); Trigger 2 FAIL (UNATTRIBUTED clone-publisher not roster — Ox attribution-discipline preserved per Hard Rule 2); anti-noise rule 1 active. (8) THN 'MiniPlasma Windows 0-Day...' 04:57 EDT (14:27 IST) — third relay of BleepingComputer Lawrence Abrams 2026-05-17 18:30 EDT originating coverage already evaluated in 00:00 FLASH 9c61bdb + 06:00 FLASH a8121bc + absorbed into finding-2026-05-18-0001 morning brief b812307; anti-noise rule 1 fully bound. Hard Rules compliance verified: Rule 2 (no Archimedes-originated attribution across 6 distinct relay-frames — CoinbaseCartel cluster-narrowing preserved-as-source-said, Scattered Spider non-propagation to Grafana, Cyera OpenClaw vendor framing preserved, healthcare aggregate explicit no-attribution preserved, npm clone-publisher UNATTRIBUTED preservation, MiniPlasma anti-noise lock); Rule 3 (no PoC repo URLs linked — depthfirst CVE-2026-42945 GitHub, V12 security CVE-2026-31635 GitHub, Chaotic-Eclipse/Nightmare-Eclipse MiniPlasma PoC all not linked); Rule 4 (no active scanning, SpiderFoot not invoked, authorized-targets.yaml empty); LEGAL-POLICY prohibited-query-patterns not triggered (no active recon, no exploitation assistance, no credential storage, no impersonation, no circumvention)."
ttl_expires_at: 2026-08-16T12:05:00-04:00
---

# FLASH sweep 2026-05-18 12:00 EDT (operator-triggered off-cadence, Monday midday post-morning-brief) — CLEAN

## Sweep summary

**Mode:** flash_sweep (operator-triggered off-cadence, 12:00 EDT Monday window — coincides with the canonical 12:00 scheduled sweep slot but the orchestrator's pulse was via operator instruction not Task Scheduler)
**Window:** 2026-05-18T06:00:00-04:00 → 2026-05-18T12:05:00-04:00 (~6h since 06:00 FLASH a8121bc)
**Trigger evaluation outcome:** 0 of 6 FLASH triggers fired.
**Disposition:** clean sweep — no candidates promoted to grader; no escalation; no Discord post.
**Quiet-hours state:** INACTIVE (12:00 EDT inside 09:00–21:00 EDT active window per FLASH-POLICY.md — had any trigger fired, post would have been LIVE to `#flash-alerts`, NOT queued). Critical-override conditions NOT met across any in-window item (no CVSS 10.0 + active exploitation + tracked actor + A&D watchlist entity coincidence).

## Sources queried (active A-grade / B-grade priority set)

| Source | Status | In-window items | Notes |
|---|---|---|---|
| **BleepingComputer** | reachable 200 | 3 items | Items: Grafana detail layer (09:46 EDT, Item #3 below); Microsoft Win11 KB5089549 install issue (04:33 EDT — Microsoft technical-operations class, not threat-intel, DISCARDED at filter); Microsoft Win11 resizable taskbar (07:14 EDT — Microsoft non-security feature, DISCARDED at filter) |
| **SecurityWeek** | reachable 200 | 5 in-window items + 3 already-evaluated in 06:00 FLASH a8121bc carry-forward (Shai-Hulud worm clones / Grafana / NGINX VulnCheck) | Items: Claw Chain OpenClaw (08:14 EDT, Item #1 below); Healthcare aggregate (08:58 EDT, Item #2 below); 7-Eleven ShinyHunters (already absorbed into finding-2026-05-18-0002 morning brief b812307) |
| **The Hacker News** | reachable 200 via feedburner.com/TheHackersNews | 5 in-window items + carry-forwards | Items: Ivanti/Fortinet/SAP/VMware/n8n (06:54 EDT, Item #4); Developer Workstations editorial (07:23 EDT, Item #5); Weekly Recap (09:50 EDT, Item #6); Four Malicious npm Packages (04:57 EDT, Item #7 — same cluster as 06:00 FLASH a8121bc Item #2); MiniPlasma (04:57 EDT, Item #8 — already absorbed into finding-2026-05-18-0001) |
| **The Record** | reachable 200 | 0 in-window | Feed last-modified 2026-05-15T19:31 GMT pre-window |
| **Unit 42** | reachable 200 | 0 in-window | Feed last update 2026-05-15 (Gremlin Stealer Evolution — pre-window) |
| **DarkReading** | reachable 200 | 0 net-new | "The Boring Stuff is Dangerous Now" Shlomie Liberow forward-dated 2026-05-18T13:00 GMT — already discarded in 2026-05-17 18:00 + 2026-05-18 00:00 + 06:00 FLASH sweeps; anti-noise applies |
| **CISA all.xml** | reachable 200 | 0 in-window | Feed unchanged from 06:00 FLASH state |
| **CISA KEV JSON** | not directly WebFetched | — | Relies on CISA all.xml master feed (0 in-window items); KEV state unchanged from 06:00 FLASH state (CVE-2026-42897 due 2026-05-29 / CVE-2026-20182 federal deadline LAPSED end-of-day 2026-05-17 T+14h+ / CVE-2026-42208 / CVE-2026-6973 / CVE-2026-0300 — all carry-forwards) |
| **Mandiant feedburner** | known persistent 404 | — | Skipped per source-health (~20+ consecutive failures) |
| **MSTIC** | reachable 200 | 0 in-window | Feed last-modified pre-window |
| **CrowdStrike** | not re-tested | — | Marketing-only pattern persists per source-health |
| **Cisco Talos** | not re-tested | — | feeds/posts/default broken-path; canonical workaround not re-tested this FLASH-fast sweep |
| **SANS ISC** | not re-tested | — | Transient parse-error class from 00:00 FLASH; not validated this sweep |
| **Sophos** | known 404 | — | Carried stale per source-health |
| **GitHub Advisories Atom** | known persistent 406 | — | Not re-tested |

## Splunk first-party non-self-telemetry sweep (Hard Rule 8)

**Sweep tokens (30d window):** OpenClaw, CoinbaseCartel, shinysp1d3r, CVE-2026-44113, CVE-2026-44115, CVE-2026-44118, CVE-2026-44112, CVE-2026-8043, CVE-2026-44277, CVE-2026-26083, CVE-2026-34260, CVE-2026-34263, CVE-2026-41702, CVE-2026-42231, CVE-2026-42232, CVE-2026-44791, CVE-2026-44789, CVE-2026-44790, Cyera, FortiAuthenticator, FortiSandbox, Xtraction, "S/4HANA", "Coinbase Cartel".

**Result:** 14 archimedes:operation + 16 archimedes:scheduler self-telemetry events in -24h (consistent with normal cadence). 3 defenseclaw_local:json events at 2026-04-20 10:47 EDT (well outside FLASH Trigger 3 24h-recency window — these are background events whose match was on a related term not the FLASH-trigger CVE/cluster token, time-bounded retrieval confirms 0 hits on the actual trigger tokens). **No first-party IOC hit within Trigger 3 24h window.** 43rd consecutive dormant non-self-telemetry sweep. Silence is not disconfirming per established 42-sweep dormancy cadence.

## FLASH trigger evaluation per item

### Item 1 — SecurityWeek "Claw Chain OpenClaw" (Ionut Arghire, 08:14 EDT)

- **CVEs:** CVE-2026-44112 (race condition CVSS 9.6) + CVE-2026-44113/44115/44118 (3 additional sandbox-escape chain links)
- **Originating researcher:** Cyera (first corpus surface — NOT in `source-grades.yaml`; conservative provisional-grade-pending evaluation parallel to Sysdig 2026-05-14, Zellic 2026-05-14, depthfirst 2026-05-14, V12 security 2026-05-17 first-surface pattern)
- **Product:** OpenClaw AI assistant; >60,000 publicly accessible instances
- **Patch status:** PATCHED April 23 (reported April 22 + fix next day; 26 days before public disclosure)
- **Active exploitation:** None claimed
- **Threat actor:** None
- **A&D relevance:** No (OpenClaw is consumer/general AI assistant class — LangFlow / AnythingLLM / Flowise category, no operator-mandated A&D-prime adoption observed)
- **Trigger 1 FAIL:** No A-grade source (Cyera unknown to corpus), no active-exploitation claim
- **Trigger 6 FAIL:** Patched 26 days before disclosure (patch-absence leg FAILS), no A-grade exploitation attestation
- **Disposition:** status-update CANDIDATE for vuln-tracker addition to `_index.yaml` if Cyera surface recurs OR A&D-prime adoption of OpenClaw emerges; first-corpus-surface vendor flagged for next librarian source-grade audit pickup pending operator ratification approach

### Item 2 — SecurityWeek "Millions Impacted Across Several US Healthcare Data Breaches" (Eduard Kovacs, 08:58 EDT)

- **Victim aggregate:** NYC Health and Hospitals 1.8M + Nacogdoches Memorial Hospital 2.5M + Erie Family Health Centers 570K + Florida Physician Specialists 276K + Coastal Carolina Health Care 110K + Western Orthopaedics 110K (~5.4M aggregate records)
- **Incident timing:** Various (Nov 2025 – Feb 2026 for NYC Health; Dec 2025 – Jan 2026 for Erie; two days in Nov 2025 for Florida; >1y pre-announcement detection for Coastal Carolina)
- **Attribution:** **"None of these healthcare data breaches appears to have been claimed by known cybercrime groups."** (verbatim, preserved per Hard Rule 2)
- **Sector:** Healthcare — NOT in `aerospace-defense.yaml` watchlist
- **CVE / actor:** None
- **Disposition:** ALL 6 triggers FAIL. Sector-misaligned aggregate digest, no Archimedes tracking justification.

### Item 3 — BleepingComputer "Grafana says stolen GitHub token..." (Bill Toulas, 09:46 EDT)

- **Net-new detail layer on prior Grafana cluster** (06:00 FLASH a8121bc Item #3 = SecurityWeek Eduard Kovacs 04:34 EDT; same cluster, +5h47m of evolution)
- **Cluster narrowing observed:** BleepingComputer verbatim: **"CoinbaseCartel consists of ShinyHunters and Lapsus$ affiliates"** — DROPS Scattered Spider from the prior SecurityWeek "Coinbase Cartel linked to ShinyHunters, Scattered Spider, and Lapsus$" framing. Hard Rule 2 narrower-source-preferred treatment applies; Scattered Spider (#013 HIGH) is NOT attributed to Grafana incident by this BleepingComputer source.
- **NEW IOC-class indicator:** "shinysp1d3r" in-memory tool referenced by unnamed researchers ("researchers identified the gang's use of an in-memory tool called 'shinysp1d3r'"). Relay-of-unnamed-researchers attribution chain — Archimedes does NOT propagate as Archimedes-attested IOC per Hard Rule 2.
- **Grafana victim self-disclosure scope-bounding:** "no evidence that customer data or personal information was exposed"; "customer systems remained unaffected"; source code downloaded but bounded scope confirmed.
- **A-grade vendor coverage:** None cited (no Mandiant / CrowdStrike / Unit 42 / MSTIC / Volexity / Bitdefender / ESET / Symantec / Talos in BleepingComputer source — only FBI ransomware-payment guidance reference).
- **Trigger 2 FAIL:** CoinbaseCartel + ShinyHunters + Lapsus$ all NOT in `_roster.yaml`. Scattered Spider (#013 HIGH) IS in roster but is NOT attributed to Grafana by this source (narrower BleepingComputer framing drops it from prior SecurityWeek multi-step relay). Hard Rule 2 + LEGAL-POLICY no-attribution-laundering binding constraint prevents propagation.
- **Anti-noise rule 1:** Active on Grafana cluster (T+6h since 06:00 FLASH a8121bc first observation). Status-update CANDIDATE for 16:00 afternoon brief grader as cluster-anchor refinement layer + ShinyHunters / CoinbaseCartel `/new-actor` candidate set if subsequent A-grade vendor surfaces (Mandiant / CrowdStrike / Unit 42 / MSTIC) corroborate the cluster lineage with named methodology.
- **Disposition:** DISCARDED for FLASH purposes; status-update class for afternoon brief grader.

### Item 4 — THN "Ivanti, Fortinet, SAP, VMware, n8n Patch RCE..." (Ravie Lakshmanan, 06:54 EDT)

Multi-vendor patch roundup. All cohort items:

| Vendor | CVE | Product | CVSS | Patch | Exploitation | KEV |
|---|---|---|---|---|---|---|
| Ivanti | CVE-2026-8043 | Xtraction (before 2026.2) | 9.6 | Fixed in 2026.2 | None claimed | None |
| Fortinet | CVE-2026-44277 | FortiAuthenticator | 9.1 | Fixed in 6.5.7/6.6.9/8.0.3 | None claimed | None |
| Fortinet | CVE-2026-26083 | FortiSandbox / Cloud / PaaS | 9.1 | Fixed in 4.4.9/5.0.2 etc. | None claimed | None |
| SAP | CVE-2026-34260 | S/4HANA | 9.6 | Patched | None claimed | None |
| SAP | CVE-2026-34263 | Commerce Cloud | 9.6 | Patched | None claimed | None |
| VMware | CVE-2026-41702 | Fusion | 7.8 | Fixed in 26H1 | None claimed | None |
| n8n | CVE-2026-42231 | n8n xml2js | 9.4 | Fixed 1.123.32 / 2.17.4 / 2.18.1 | None claimed | None |
| n8n | CVE-2026-42232 | n8n XML Node | 9.4 | Fixed 1.123.32 / 2.17.4 / 2.18.1 | None claimed | None |
| n8n | CVE-2026-44791 | n8n (CVE-2026-42232 bypass) | 9.4 | Fixed 1.123.43 / 2.20.7 / 2.22.1 | None claimed | None |
| n8n | CVE-2026-44789 | n8n HTTP Request | 9.4 | Fixed 1.123.43 / 2.20.7 / 2.22.1 | None claimed | None |
| n8n | CVE-2026-44790 | n8n Git node | 9.4 | Fixed 1.123.43 / 2.20.7 / 2.22.1 | None claimed | None |

- **Trigger 1 FAIL** uniformly (active-exploitation leg fails on every cohort item)
- **Trigger 6 FAIL** uniformly (all patched at publication; exploitation-confirmed-or-imminent leg fails)
- **A&D relevance:** Fortinet FortiAuthenticator + FortiSandbox + SAP S/4HANA all widely-deployed in A&D-prime enterprise SDLCs (Boeing / Lockheed / Northrop / Raytheon / L3Harris / BAE / General Dynamics typical inventory). Status-update CANDIDATE for vuln-tracker evaluation if any cohort enters operator-mandated tracking.
- **Disposition:** DISCARDED for FLASH purposes; multi-CVE status-update class for vuln-tracker review.

### Item 5 — THN "Developer Workstations Are Now Part of the Software Supply Chain" (07:23 EDT, 16:53 IST)

- Opinion/digest editorial covering "three supply chain campaigns ... within 48 hours" — overlapping Mini Shai-Hulud / Mini Sha1-Hulud clones / TeamPCP / node-ipc / OpenAI TanStack carry-forward set
- No novel attribution, no novel CVE, no novel IOC
- Mention-class only, anti-noise rule 1 active on overlapping carry-forwards
- All 6 triggers FAIL

### Item 6 — THN "Weekly Recap: Exchange 0-Day, npm Worm, Fake AI Repo, Cisco Exploit and More" (09:50 EDT, 19:20 IST)

- Pure weekly digest covering CVE-2026-42897 Exchange + Shai-Hulud / TeamPCP npm worm + Fake AI Repo + CVE-2026-20182 Cisco Catalyst SD-WAN — all carry-forwards already evaluated in prior briefs
- No novel content
- All 6 triggers FAIL

### Item 7 — THN "Four Malicious npm Packages Deliver Infostealers and Phantom Bot DDoS Malware" (Ravie Lakshmanan, 04:57 EDT / 14:27 IST)

- **Same cluster as 06:00 FLASH a8121bc Item #2** (SecurityWeek Ionut Arghire 05:45 EDT "First Shai-Hulud Worm Clones Emerge")
- **Ox Security primary attribution language (verbatim):** chalk-tempalte "contains a direct clone of the Shai-Hulud source code that TeamPCP leaked last week," suggesting actor "repurposed publicly released code rather than being affiliated with TeamPCP itself."
- **Actor identifier:** single npm user "deadcode09284814" (UNATTRIBUTED; explicitly distinct from TeamPCP)
- **Package set (download counts at time of THN publication):**
  - chalk-tempalte: 825 downloads
  - @deadcode09284814/axios-util: 284 downloads
  - axois-utils: 963 downloads
  - color-style-utils: 934 downloads
- **Payload triple:** Phantom Bot Golang DDoS botnet (HTTP/TCP/UDP) + information stealers (credential harvesters) + Shai-Hulud worm clone (chalk-tempalte specifically)
- **NEW C2 IOCs (Ox Security per THN relay):**
  - 87e0bbc636999b.lhr[.]life (subdomain on lhr.life localhost-tunneling service)
  - 80.200.28[.]28:2222 (direct IP+port C2)
  - edcf8b03c84634.lhr[.]life (subdomain on lhr.life)
  - GitHub indicator: repositories with description "A Mini Sha1-Hulud has Appeared"
- **Anti-noise rule 1:** Active (T+6h since 06:00 FLASH a8121bc evaluation as Item #2). Already absorbed into morning brief b812307 as Other Signal mention-class with dependency-tree-quarantine watchlist recommendation.
- **Trigger 2 FAIL:** UNATTRIBUTED clone-publisher; deadcode09284814 not in roster; Ox attribution-discipline preserved per Hard Rule 2 (NOT propagated to TeamPCP)
- **Disposition:** DISCARDED for FLASH purposes; IOC-augmentation CANDIDATE for afternoon brief vt-006 carry-forward refinement (the C2 indicators + Mini Sha1-Hulud GitHub repo descriptor are net-new vs. morning brief b812307 mention-class which lacked the IOC layer).

### Item 8 — THN "MiniPlasma Windows 0-Day..." (04:57 EDT, 14:27 IST)

- Third relay of BleepingComputer Lawrence Abrams 2026-05-17 18:30 EDT originating coverage
- Already evaluated in 00:00 FLASH 9c61bdb + 06:00 FLASH a8121bc
- Already absorbed into finding-2026-05-18-0001 morning brief b812307 (B2/likely cluster anchor with ACH non-diagnostic among 4 substantive hypotheses; halt_pending_test on PoC-effectiveness layer pending Microsoft MSRC / A-grade vendor reproduction)
- Anti-noise rule 1 fully bound
- All 6 triggers FAIL

## Carry-forward state (unchanged from morning brief b812307 + 06:00 FLASH a8121bc except where noted)

- **CVE-2026-20182** Cisco Catalyst SD-WAN federal KEV: deadline LAPSED end-of-day Sunday 2026-05-17. **T+14h post-lapsed at sweep time.** Zero fresh A-grade reporting from Mandiant / Volexity / Unit 42 / MSTIC / CrowdStrike since the deadline lapsed. UAT-8616 attribution per Cisco Talos carry-forward with visibility-skew caveat (finding-2026-05-14-0005 carry-forward chain).
- **CVE-2026-42897** Microsoft Exchange OWA XSS federal KEV: T-11d (Friday 2026-05-29 deadline). >48h+ single-source-veto on exploitation-claim layer holds; MSRC remains sole originating attester (Mandiant / Volexity / Unit 42 / MSTIC / CrowdStrike all silent through ~72h+ since FLASH a8121bc; finding-2026-05-15-0003 carry-forward).
- **CVE-2026-42945** NGINX Rift PoC (depthfirst) VulnCheck Canaries dual-relay SecurityWeek + The Hacker News scanner-class probe defensive-telemetry refinement (B-grade defensive-posture observation NOT A-grade attestation of confirmed production exploitation per Hard Rule 2; finding-2026-05-16-0001 carry-forward).
- **Symantec / SentinelLABS Fast16 framework** provisional-A ratification clock: T+41h35m past elapsed deadline 2026-05-16T18:25 awaiting operator pass. (Symantec nuclear-weapons-simulations sabotage-intent surface via The Hacker News 2026-05-18 02:46 EDT relay continues to strengthen ratification case; finding-2026-05-16-0003 sector-focus carry-forward.)
- **Pwn2Own Berlin 2026 final wrap** Orange Tsai / DEVCORE Exchange RCE-to-SYSTEM chain under standard 90-day ZDI vendor-coordinated-disclosure embargo through ~2026-08-13 (final totals $1.298M / 47 zero-days / DEVCORE Master of Pwn 50.5 points / $505K rewards; finding-2026-05-16-0002 carry-forward).
- **Turla/Kazuar/Secret Blizzard D+2 relay layer** duplicate-locked against finding-2026-05-14-0006 / reject-2026-05-16-0001 anti-noise rule 1 active (no new relay surface this window).
- **Tycoon2FA device-code PhaaS** absorbed into finding-2026-05-17-0002 per afternoon brief 005596f (commodity criminal PhaaS, no tracked actor, anti-noise rule 1 active, no re-fire).
- **MiniPlasma / CVE-2020-17103** absorbed into finding-2026-05-18-0001 morning brief b812307 (B2/likely cluster anchor with halt_pending_test on PoC-effectiveness layer).
- **7-Eleven April 8 / ShinyHunters Salesforce campaign** absorbed into finding-2026-05-18-0002 morning brief b812307 (B2/likely cluster anchor with explicit Hard Rule 2 + LEGAL-POLICY no-attribution-laundering non-propagation of Coinbase Cartel ecosystem-lineage to 7-Eleven; ShinyHunters `/new-actor` candidate flagged at conservative MEDIUM).
- **Shai-Hulud npm worm clones (Mini Sha1-Hulud / chalk-tempalte / axois-utils / @deadcode09284814 set)** mention-class in morning brief b812307 Other Signal with dependency-tree-quarantine watchlist recommendation; THN Ox Security cluster-refinement at 04:57 EDT adds C2 IOC layer that may merit afternoon brief promotion to status-update class as VT-006 / Mini Shai-Hulud lineage carry-forward refinement.

## Net-new status-update candidates surfaced for 16:00 afternoon brief grader

1. **Grafana cluster — CoinbaseCartel attribution refinement** (BleepingComputer Bill Toulas 09:46 EDT — narrower "CoinbaseCartel consists of ShinyHunters and Lapsus$ affiliates" framing dropping Scattered Spider from prior SecurityWeek 04:34 EDT multi-step relay; in-memory tool "shinysp1d3r" referenced; bounded victim scope verified; cluster-anchor candidate pending A-grade vendor corroboration)
2. **Shai-Hulud worm clone IOCs net-new layer** (THN Ravie Lakshmanan 04:57 EDT relay of Ox Security — C2 domains + IP + GitHub "Mini Sha1-Hulud" descriptor; status-update refinement of morning brief b812307 mention-class to add IOC layer for VT-006 carry-forward)
3. **Multi-vendor critical-RCE patch roundup** (Ivanti Xtraction + Fortinet FortiAuthenticator/FortiSandbox + SAP S/4HANA + SAP Commerce Cloud + VMware Fusion + n8n five-CVE — vuln-tracker evaluation candidate for A&D-prime enterprise inventory exposure; no operator-mandated tracking yet)
4. **OpenClaw "Claw Chain" four-CVE patched cluster** (SecurityWeek Ionut Arghire 08:14 EDT — Cyera-originating; first corpus surface for Cyera; CVE-2026-44112 CVSS 9.6 patched 26 days before disclosure; >60,000 publicly accessible instances; status-update / source-grades.yaml first-surface flag)
5. **Healthcare data-breach aggregate** (SecurityWeek Eduard Kovacs 08:58 EDT — sector-misaligned, no tracking justification but mention-class for sector-context completeness)

## Hard Rules compliance

- **Rule 2 (no Archimedes-originated attribution):** No first-time attribution claims across 6 distinct relay-frames evaluated. CoinbaseCartel cluster-narrowing preserved-as-source-said; Scattered Spider non-propagation to Grafana per BleepingComputer narrower framing; Cyera OpenClaw vendor framing preserved without Archimedes-elevation; healthcare aggregate explicit no-attribution preserved verbatim; npm clone-publisher UNATTRIBUTED preservation per Ox Security; MiniPlasma anti-noise lock prevents re-evaluation.
- **Rule 3 (no exploitation assistance):** No PoC repo URLs linked anywhere — depthfirst CVE-2026-42945 GitHub, V12 security CVE-2026-31635 GitHub, Chaotic-Eclipse/Nightmare-Eclipse MiniPlasma PoC, Ox Security npm clone GitHub repos all not linked in this sentinel.
- **Rule 4 (no third-party scanning):** No active scanning; SpiderFoot not invoked; `authorized-targets.yaml` empty; passive collection only.
- **Rule 6 (15-word quote / one-per-source):** Sentinel contains verbatim BleepingComputer attribution chain "CoinbaseCartel consists of ShinyHunters and Lapsus$ affiliates" (7 words) and SecurityWeek "None of these healthcare data breaches appears to have been claimed by known cybercrime groups" (15 words — at limit, one quote from that source) plus Ox Security verbatim chalk-tempalte attribution "contains a direct clone of the Shai-Hulud source code that TeamPCP leaked last week" (14 words) — within 15-word limit, one quote per source.
- **Rule 8 (Splunk first-party priority):** Sweep performed across 24 tokens (CVEs + actor cluster names + vendor product names + researcher firm Cyera); 43rd consecutive dormant non-self-telemetry result; silence is not disconfirming per established dormancy cadence.
- **LEGAL-POLICY:** Prohibited-query-patterns not triggered (no active recon, no exploitation assistance, no credential storage, no impersonation, no circumvention). No targets in `authorized-targets.yaml`. All source fetches are passive WebFetch / mcp__rss-bridge / mcp__splunk-query reads on authorized public feeds or first-party indexes.

## Source-health change log

No source-health changes this sweep. All A-grade / B-grade priority sources reachable on first attempt except Mandiant feedburner (known persistent 404, skipped per source-health prior state), Sophos (known 404, carried stale), GitHub Advisories Atom (known persistent 406), CrowdStrike (marketing-only, not re-tested), Cisco Talos (broken path, not re-tested). No `failure_count` increments triggered by this sweep.

## Run identifier

`flash-sweep-20260518-120000-off-cadence` — operator-triggered off-cadence pulse; coincides with canonical 12:00 EDT scheduled slot but invocation pulse was via operator instruction not Task Scheduler. Result is equivalent to a clean scheduled FLASH sweep. Librarian handoff: log `run_complete` + `flash_sweep_clean` to Splunk per FLASH-POLICY silent-exit convention; no Discord post; commit raw-signal sentinel to git via standard cadence.
