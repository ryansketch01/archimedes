---
raw_id: raw-2026-05-14-pm-000
collected_at: 2026-05-14T15:35:00-04:00
run_id: pre-brief-20260514-153000
collection_mode: pre_brief_collection
sweep_type: pre_brief
sweep_time: 2026-05-14T15:30:00-04:00
time_window_start: 2026-05-14T07:30:00-04:00
time_window_end: 2026-05-14T15:30:00-04:00
time_window_hours: 8
test: false
source:
  source_yaml_id: meta-sweep-tombstone
  source_name: "Pre-brief sentinel tombstone (PM sweep summary)"
  source_url: null
  published_at: 2026-05-14T15:30:00-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: []
triage_tags: [pre_brief_sentinel, audit_trail, non_flash]
iocs_extracted: false
iocs_count: 0
text_word_count: 0
promoted: false
promotion_disposition: non_promotable_sentinel_tombstone_no_grading_required
graded_at: 2026-05-14T15:55:00-04:00
graded_by: grader
grading_run_id: afternoon-20260514-160000
graded_disposition_rationale: "Sentinel tombstone summarizes the PM sweep — operational audit-trail artifact, not a substantive raw-signal candidate for grading. The 5 substantive items it references (PM-001 through PM-005) were graded individually under this same grading run. Sentinel is retained per 90-day raw-signal retention policy for audit-trail completeness but not promoted to a finding."
ttl_expires_at: 2026-08-12T15:35:00-04:00
---

# Pre-brief collection 2026-05-14 15:30 EDT — sweep summary

**5 substantive raw-signal files written (PM-001 Cisco Catalyst SD-WAN CVE-2026-20182 KEV+Talos UAT-8616, PM-002 MSTIC Secret Blizzard / Kazuar P2P botnet, PM-003 Salt Typhoon Azerbaijan O&G + Twill Typhoon cluster, PM-004 OpenAI confirms TanStack breach, PM-005 node-ipc backdoor 3 versions). 8h window 2026-05-14 07:30 EDT → 15:30 EDT bridges this morning's 08:00 brief through to the 16:00 afternoon brief.**

## Sweep window

2026-05-14T07:30:00-04:00 → 2026-05-14T15:30:00-04:00 (8h)

## Sources queried (12 productive, 1 rejected, ~10 in baseline-quiet/cached)

**A-grade / B-grade RSS feeds and direct WebFetch surfaces queried in this window:**

- **BleepingComputer RSS** — fetch_feed status 200, last_modified 2026-05-14T19:27 GMT (in-window from feed-server activity), 5 items in 8h window: (1) **OpenAI confirms security breach in TanStack supply chain attack** 2026-05-14T15:07 EDT — **RAW-SIGNALED AS PM-004** (TeamPCP attribution via Wiz/Snyk/Socket/Aikido chain extension to OpenAI; cert rotation; 2 employee devices); (2) **Pwn2Own Berlin Day 1** 2026-05-14T14:53 EDT — competition-demonstration, no tracked actor, no ITW, DISCARDED Mode 1; (3) **18-year-old NGINX vulnerability (Bill Toulas)** 2026-05-14T11:43 EDT — ANTI-NOISE LOCKOUT to 2026-05-15 (covered in AM-002 + finding-2026-05-14-0002), BUT adds new facts (DepthFirst AI vendor framing, Kevin Beaumont skeptical pushback, AlmaLinux RCE-not-trivial assessment, April 18/21 disclosure timeline) — recorded in this sentinel only, not separately raw-signaled; (4) NMFTA cargo theft sponsored 2026-05-14T15:21 EDT — sponsored content DISCARDED Mode 1; (5) **KongTuke Microsoft Teams social engineering (Bill Toulas)** 2026-05-14T08:12 EDT — ANTI-NOISE LOCKOUT (covered in 2026-05-13 16:00 afternoon brief finding-2026-05-13-0004 KongTuke / ModeloRAT / Octo Tempest / Rapid7).

- **SecurityWeek RSS** — fetch_feed status 200, last_modified 2026-05-14T17:23 GMT (in-window), 5 items in 8h window: (1) Data center security trade article 2026-05-14T10:00 EDT marketing content DISCARDED Mode 1; (2) **New Linux Kernel Vulnerability Fragnesia (Eduard Kovacs)** 2026-05-14T09:44 EDT — ANTI-NOISE LOCKOUT (covered in AM-003 + finding-2026-05-14-0003), adds the "similar to recently disclosed Dirty Frag and Copy Fail" cluster-framing language which corroborates the analyst's Linux LPE cluster framing in this morning's brief; (3) Mythos benchmarking 2026-05-14T09:00 EDT vendor-benchmarking content DISCARDED Mode 1; (4) Akamai acquires LayerX $205M 2026-05-14T08:55 EDT M&A news DISCARDED Mode 1 (LayerX is provisional C source; M&A event does not change grade pending operator review); (5) **Chinese APTs Expand Targets — Salt Typhoon Azerbaijan + Twill Typhoon (Ionut Arghire)** 2026-05-14T08:11 EDT — **RAW-SIGNALED AS PM-003** (Salt Typhoon piece is anti-noise to yesterday's 14:30 FLASH Bitdefender, BUT Twill Typhoon / Mustang Panda / Darktrace + Cisco Talos TernDoor framing is NEW content not in yesterday's coverage).

- **The Record RSS** — fetch_feed status 200, 1 item in 8h window: ODNI 2026 election security coordinator appointments 2026-05-14T14:21 EDT — governance/policy, NO actor, NO CVE, NO active exploitation — DISCARDED Mode 1.

- **Krebs on Security RSS** — fetch_feed status 200, last_modified 2026-05-13T10:43 GMT pre-window, 0 items in 8h window — normal cadence.

- **SANS ISC RSS** — fetch_feed status 200, last_modified 2026-05-14T19:29 GMT in-window from feed-server activity, 0 items in 8h window after since-filter.

- **CISA all.xml** — fetch_feed status 200, **18 items in 8h window**: (1) **CISA Adds One KEV — CVE-2026-20182 Cisco Catalyst SD-WAN Authentication Bypass** 2026-05-14T08:00 EDT — **RAW-SIGNALED AS PM-001** (active exploitation per CISA, Emergency Directive 26-03 referenced, dueDate 2026-05-17 = THREE-DAY federal deadline, CVSS 10.0, FedRAMP-Government deployment listed); (2)-(18) **CISA Siemens / Universal Robots ICS bulk batch** — 17 ICS-CERT advisories (icsa-26-134-01 through 17) all 2026-05-14T08:00 EDT publication, Critical Manufacturing sector across the board — Siemens ROS#, gWAP/Axios prototype-pollution, SIMATIC CN 4100 (multiple-CVE 9.6), Ruggedcom Rox 2.17.1 (multiple ICSAs), Simcenter Femap, Universal Robots Polyscope 5 (9.8 OS-command injection), Teamcenter (V2312/V2406/V2412/V2506/V2512 cohort), SENTRON 7KT PAC1261 Data Manager 9.1, Opcenter RDnL, Solid Edge, SIMATIC HMI, SIPROTEC 5, SIMATIC S7 PLC, Industrial Devices SCALANCE. None individually FLASH-trigger (no actor, no in-the-wild). Aggregated as **CISA Siemens / Universal Robots bulk-ICS cohort** — recorded in this sentinel only; not separately raw-signaled (sector-watchlist context for the briefer, no single-finding promotion candidate). Universal Robots Polyscope 5 CVE-2026-8153 9.8 unauthenticated-OS-command-injection on robot-OS is the highest-severity outlier; Tier-1 A&D primes deploying industrial robotics may be exposed but no public victim identification.

- **CISA KEV catalog** (JSON, catalogVersion 2026.05.14, dateReleased 2026-05-14T17:31:13Z) — **+1 entry vs morning sweep**: CVE-2026-20182 Cisco Catalyst SD-WAN added 2026-05-14, dueDate **2026-05-17 (3 days)**, CWE-287 Improper Authentication, knownRansomwareCampaignUse=Unknown, requiredAction references CISA Emergency Directive 26-03. CVE-2026-31431 Linux Kernel "Copy Fail" dueDate 2026-05-15 = TOMORROW (carry-over from morning).

- **Cisco Talos blog RSS** — fetch_feed status 200, 2 items in 8h window: (1) **Ongoing exploitation of Cisco Catalyst SD-WAN vulnerabilities** 2026-05-14T12:02 EDT (Cisco Talos byline) — **RAW-SIGNALED AS PM-001 (joint with CISA KEV add)** — primary research authoring UAT-8616 cluster, 10 post-exploit cluster IOC sets, March-2026 ORB infrastructure overlap, prior CVE-2026-20127 cohort exploitation pattern; (2) **The time of much patching is coming** 2026-05-14T14:00 EDT (Martin Lee Threat Source newsletter) — newsletter aggregate referencing "DOD contractor API flaw exposed military course data" (Schemata AI training platform via Strix research) AND second Linux LPE in 2 weeks framing (Fragnesia → Copy Fail cluster) AND TanStack/Mistral/UiPath supply-chain AND Checkmarx Jenkins compromise; newsletter not separately raw-signaled (aggregate-relay, primary substance is in the linked Talos zero-trust IR blog + the underlying ITW pieces).

- **Microsoft Security blog RSS** — fetch_feed status 200, last_modified 2026-05-14T18:24 GMT in-window, 3 items in 8h window: (1) **Defense in depth for autonomous AI agents** 2026-05-14T12:00 EDT — defensive-guidance content, NO actor, NO CVE, NO active exploitation, DISCARDED Mode 1; (2) **Kazuar: Anatomy of a nation-state botnet** 2026-05-14T11:00 EDT (Microsoft Threat Intelligence byline) — **RAW-SIGNALED AS PM-002** (MSTIC deep-dive on Secret Blizzard = Turla = VENOMOUS BEAR = Uroburos = Snake = Blue Python = WRAITH = ATG26, CISA-attributed to FSB Center 16, modular P2P botnet architecture, 4 sample SHA256, government/defense/MENA/Central Asia victimology, defense-departments-and-defense-related-companies-worldwide-targeting); (3) **Exploitable misconfigurations in AI apps on Kubernetes** 2026-05-14T10:20 EDT — Microsoft Defender for Cloud research on MCP servers exposed without auth + RCE class — adjacent to PraisonAI/AI-supply-chain theme but observational not actor-specific, single sentinel reference only.

- **The Hacker News RSS** — fetch_feed status 200, 6 items in 8h window: (1) **Cisco Catalyst SD-WAN Auth Bypass Actively Exploited** 2026-05-14T13:45 EDT — relay of Cisco PSIRT advisory + Rapid7 (Jonah Burgess + Stephen Fewer) discovery credit + Talos UAT-8616 connection, ANTI-NOISE LOCKOUT to PM-001 (THN is corroborating relay, not originating primary; THN clarifies CVSS 10.0 vs CISA-only "frequent attack vector" framing — recorded in PM-001 corroboration block); (2) **Stealer Backdoor Found in 3 Node-IPC Versions** 2026-05-14T13:22 EDT — relay of Socket + StepSecurity research — **RAW-SIGNALED AS PM-005** (3 npm versions backdoored, ~90 credential categories exfil, C2 sh.azurestaticprovider[.]net, atiertant maintainer no-publish-history account, dual-DNS-1.1.1.1+8.8.8.8 + DNS-TXT exfil, unattributed); (3) **ThreatsDay Bulletin** 2026-05-14T12:07 EDT — weekly newsletter, aggregate-relay, DISCARDED Mode 1 (sentinel-only reference); (4) **Ghostwriter Targets Ukrainian Government** 2026-05-14T10:00 EDT — ANTI-NOISE LOCKOUT to AM-001 (corroborates ESET FrostyNeighbor / finding-2026-05-14-0001; THN adds "Belarus-aligned" framing language + March-2026 onset timestamp + 10-min fingerprint cadence specificity; recorded in this sentinel only, not separately raw-signaled); (5) **PraisonAI CVE-2026-44338 Auth Bypass Targeted Within Hours** 2026-05-14T07:40 EDT — ANTI-NOISE LOCKOUT to AM-004 (corroborates Sysdig research + finding-2026-05-14-0004; THN adds "within four hours" framing language matching Sysdig 3h44m measurement, not separately raw-signaled); (6) **How AI Hallucinations Are Creating Real Security Risks** 2026-05-14T07:30 EDT — feature article, NO threat-intel surface, DISCARDED Mode 1.

- **DarkReading RSS** — fetch_feed status 200, 3 items in 8h window: (1) **'FrostyNeighbor' APT Carefully Targets Govt Orgs (Elizabeth Montalbano)** 2026-05-14T12:59 EDT — ANTI-NOISE LOCKOUT to AM-001 / finding-2026-05-14-0001 (DarkReading is corroborating relay of ESET, not originating primary); (2) AI cybersecurity investments Valley of Death 2026-05-14T09:00 EDT — industry-analysis content, NO threat-intel, DISCARDED Mode 1; (3) **Foxconn attack manufacturing cyber crisis (Jai Vijayan)** 2026-05-14T08:00 EDT — sector-context piece on Foxconn Nitrogen ransomware attack (covered in 2026-05-13 morning brief finding-2026-05-13-0002 via Wired primary) + 600 manufacturer hits / year framing; sector-context only, not new actor / new IOC; ANTI-NOISE to Foxconn finding-2026-05-13-0002, recorded in this sentinel only.

- **Mandiant / Google Threat Intel index page** — top-of-list visible items unchanged from this morning's sweep. Feedburner remains 404 (twenty-second consecutive failure pattern; held healthy pending operator alt-endpoint decision).

- **CrowdStrike blog feed** — fetch_feed status 200, 10 items, all dateless marketing rotation. NO fresh threat-research content in window. Pattern unchanged.

- **Palo Alto Unit 42 feedburner** — fetch_feed status 200, last_modified 2026-05-14T15:52 GMT in-window from feed-server activity, 0 items in 8h window after since-filter.

- **ESET WeLiveSecurity feed** — fetch_feed status 200, 0 items in 8h window after since-filter (FrostyNeighbor article surfaced this morning via direct WebFetch / AM-001).

- **Industrial Cyber RSS** — fetch_feed returned **403 Forbidden** (likely WAF / Akamai bot-blocking on this host; not source-grades canonical URL); held healthy from morning sweep (last_successful_fetch 2026-05-13T18:10 EDT).

- **Bitdefender Labs feed** — `bitdefender.com/blog/businessinsights/feed/` returned 404 via fetch_feed (anti-CSRF or RSS-not-published on the redirect-target URL); 06:00 + 07:30 FLASH-fast inheritance held healthy via WebFetch on the index page. Top-of-page unchanged this PM sweep (FamousSparrow Azerbaijani O&G post; ANTI-NOISE LOCKOUT to 2026-05-14 14:30 EDT, now expired — Salt Typhoon Azerbaijan content surfaces independently via SecurityWeek PM-003 with NEW Twill Typhoon framing from Darktrace + Talos).

**First-party telemetry (Splunk):**

- **`archimedes` + `defenseclaw_local` last-12h non-archimedes-internal sweep** — `index=archimedes OR index=defenseclaw_local earliest=-12h NOT sourcetype=archimedes:*` returned 0 events. **24th consecutive dormant sweep** with the non-archimedes-internal stream. Splunk health check reachable (Splunk 10.2.2 on Frank).

## Items raw-signaled this sweep (5)

| File | Source | Topic | Triage tags |
|---|---|---|---|
| PM-001 | CISA KEV + Cisco PSIRT + Talos (UAT-8616) + Rapid7 (Burgess/Fewer) + THN relay | **CVE-2026-20182 Cisco Catalyst SD-WAN Controller Auth Bypass — CVSS 10.0, KEV dueDate 2026-05-17 (3 days), active ITW exploitation clustered as UAT-8616 (sophisticated cluster active since at least 2023 per prior CVE-2026-20127), Emergency Directive 26-03, FedRAMP-Government deployment listed, NETCONF post-exploit + SSH-key + root-escalate pattern, ORB infrastructure overlap** | flash_candidate, critical-cve-exploited, tracked-actor-equivalent_uat-8616, ad_sector_direct_dib_fedramp, cve, kev, federal_deadline_3_days |
| PM-002 | Microsoft MSTIC (Microsoft Threat Intelligence byline) | **Secret Blizzard / Turla / VENOMOUS BEAR / Snake / Uroburos / Blue Python / WRAITH / ATG26 — Kazuar modular P2P botnet deep-dive — Kernel/Bridge/Worker architecture, leader-election protocol, EWS/HTTP/WSS fallback C2, 4 sample SHA256 published, CISA-attributed to FSB Center 16, government / defense / defense-related-companies-worldwide targeting, Aqua Blizzard lateral-targeting overlap in Ukraine, MENA + Central Asia + Europe geography** | non_flash, brief_update, new_actor_candidate, tracked-actor-attribution_secret_blizzard_NOT_in_roster, ad_sector_indirect_defense_related_companies_worldwide, malware_deep_dive |
| PM-003 | SecurityWeek (Ionut Arghire) + Bitdefender (Salt Typhoon primary) + Darktrace (Twill Typhoon primary) + Cisco Talos (TernDoor primary) | **Chinese-APT cluster — Salt Typhoon (Earth Estries / FamousSparrow / GhostEmperor / UNC2286) Azerbaijani oil-and-gas Dec25-Feb26 (anti-noise lockout to yesterday 14:30 FLASH partial) + Twill Typhoon (Bronze President / Camaro Dragon / Earth Preta / Mustang Panda / TA416) Asia-Pacific Sep25-Apr26 with FDMTP .NET RAT — NEW Twill Typhoon framing not in yesterday's coverage** | non_flash, brief_update, tracked-actor-attribution_salt_typhoon, possible_new_actor_candidate_twill_typhoon_mustang_panda, ad_sector_no_direct_critical_infra_indirect |
| PM-004 | BleepingComputer (Lawrence Abrams) + OpenAI primary disclosure | **OpenAI confirms 2 employee devices compromised in Mini Shai-Hulud / TanStack supply-chain attack — TeamPCP attribution carried forward — limited source-code-repo unauthorized access — code-signing-cert rotation for macOS/Windows/iOS/Android — pre-2026-06-12 macOS-app-cert-validity caveat — Microsoft Threat Intel referenced for Linux-malware-variants** | non_flash, brief_update, tracked-actor_teampcp, tracked-vuln_vt-006_mini_shai_hulud, ad_sector_indirect_squawk_aviation_namespace_dependency, named_victim_openai |
| PM-005 | The Hacker News + Socket + StepSecurity | **node-ipc 3 backdoored versions (9.1.6, 9.2.3, 12.0.1) published by atiertant-account with no-prior-publish-history (account compromise or unauthorized maintainer-addition) — ~90 credential categories exfil — C2 sh.azurestaticprovider[.]net — dual-DNS-resolver fallback 1.1.1.1+8.8.8.8 — HTTPS-POST + DNS-TXT-encoded exfil — UNATTRIBUTED (no Shai-Hulud lineage claim per primary research)** | non_flash, brief_update, unattributed, supply_chain, npm, ad_sector_indirect_dependency_graph_unknown, ioc-rich |

## Items NOT raw-signaled this sweep (anti-noise lockouts + sub-Mode-1)

| Item | Source | Reason |
|---|---|---|
| BleepingComputer NGINX Rift (Bill Toulas) 2026-05-14T11:43 EDT | BC | ANTI-NOISE LOCKOUT to AM-002 / finding-2026-05-14-0002; NEW facts (DepthFirst AI vendor framing, Beaumont skeptical pushback, AlmaLinux RCE-not-trivial, April-18/21 disclosure timeline) noted in this sentinel for grader awareness |
| SecurityWeek Fragnesia (Eduard Kovacs) 2026-05-14T09:44 EDT | SW | ANTI-NOISE LOCKOUT to AM-003 / finding-2026-05-14-0003; adds Dirty-Frag/Copy-Fail cluster-framing language corroborating analyst's Linux LPE cluster framing |
| THN Cisco SD-WAN Auth Bypass 2026-05-14T13:45 EDT | THN | Corroboration of PM-001 primary; CVSS 10.0 clarification + Rapid7 discoverer credit recorded in PM-001 corroboration block |
| THN Ghostwriter Ukrainian Govt 2026-05-14T10:00 EDT | THN | ANTI-NOISE LOCKOUT to AM-001 / finding-2026-05-14-0001; adds "Belarus-aligned" framing + 10-min fingerprint cadence + March-2026 onset specificity |
| THN PraisonAI 2026-05-14T07:40 EDT | THN | ANTI-NOISE LOCKOUT to AM-004 / finding-2026-05-14-0004; "within four hours" framing corroborates Sysdig 3h44m |
| DarkReading FrostyNeighbor (Elizabeth Montalbano) 2026-05-14T12:59 EDT | DR | ANTI-NOISE LOCKOUT to AM-001 |
| DarkReading Foxconn manufacturing crisis (Jai Vijayan) 2026-05-14T08:00 EDT | DR | ANTI-NOISE LOCKOUT to finding-2026-05-13-0002 Foxconn Nitrogen; adds "600 manufacturer hits / year" sector-context framing |
| BleepingComputer Pwn2Own Berlin Day 1 (Sergiu Gatlan) 2026-05-14T14:53 EDT | BC | Competition-demonstration, NO tracked actor, NO ITW, DISCARDED Mode 1 (routine Pwn2Own coverage) |
| BleepingComputer KongTuke Microsoft Teams (Bill Toulas) 2026-05-14T08:12 EDT | BC | ANTI-NOISE LOCKOUT to finding-2026-05-13-0004 KongTuke ModeloRAT (Rapid7 primary) |
| Microsoft Security Blog: Defense in depth for autonomous AI agents 2026-05-14T12:00 EDT | MSTIC | Defensive-guidance content, NO actor/CVE/ITW, DISCARDED Mode 1 |
| Microsoft Security Blog: Exploitable misconfigurations in AI apps on Kubernetes 2026-05-14T10:20 EDT | MSTIC | MCP-server exposure research adjacent to PraisonAI/AI-supply-chain theme, observational not actor-specific |
| THN ThreatsDay Bulletin 2026-05-14T12:07 EDT | THN | Aggregate-relay newsletter, not originating primary |
| The Record ODNI election security coordinators 2026-05-14T14:21 EDT | The Record | Governance/policy, NO threat-intel surface |
| SecurityWeek Mythos benchmarking + LayerX Akamai M&A + data-center marketing | SW | Industry-analysis content, NO threat-intel |
| 17 CISA Siemens / Universal Robots ICS-CERT advisories 2026-05-14T08:00 EDT | CISA | **Bulk Critical-Manufacturing-sector ICS-CERT cohort** — none individually FLASH-trigger (no actor, no ITW), aggregated as sector-watchlist context. Universal Robots Polyscope 5 CVE-2026-8153 9.8 unauth-OS-cmd-injection is highest-severity outlier (industrial-robotics, possible Tier-1 A&D exposure) but no public victim identification — held for briefer sector-context awareness, not raw-signaled |
| Talos: The time of much patching is coming (Martin Lee newsletter) 2026-05-14T14:00 EDT | Talos | Aggregate-relay newsletter; substantive references — Schemata AI training platform DOD-contractor API flaw (Strix research) — recorded in this sentinel only |

## Source-health state changes this sweep (5)

| Source | State change | Notes |
|---|---|---|
| `bleepingcomputer` | last_successful_fetch advance to 2026-05-14T15:30 EDT | 5 in-window items (1 raw-signaled, 3 anti-noise, 1 discarded, 1 sponsored) |
| `securityweek` | last_successful_fetch advance to 2026-05-14T15:30 EDT | 5 in-window items (1 raw-signaled, 1 anti-noise, 3 discarded marketing/M&A) |
| `the-record` | last_successful_fetch advance to 2026-05-14T15:30 EDT | 1 in-window item (governance, DISCARDED) |
| `cisa-advisories` | last_successful_fetch advance to 2026-05-14T15:30 EDT | 18 in-window items (1 KEV-add raw-signaled, 17 Siemens/UR ICS sector-watchlist context) |
| `cisa-kev` | last_successful_fetch advance to 2026-05-14T15:30 EDT; +1 catalog entry CVE-2026-20182 | catalogVersion 2026.05.14, dateReleased 2026-05-14T17:31:13Z |
| `mstic` | last_successful_fetch advance to 2026-05-14T15:30 EDT | Parent feed `microsoft.com/en-us/security/blog/feed/` 200 last_modified 2026-05-14T18:24 GMT in-window; 3 items (1 raw-signaled MSTIC Kazuar, 2 sentinel-reference). Threat-intel-specific subpath feed not re-tested this PM-fast sweep (am: 404 sporadic pattern). |
| `sans-isc` | last_successful_fetch advance to 2026-05-14T15:30 EDT; 0 items in 8h window | normal cadence |
| `krebs` | last_successful_fetch advance to 2026-05-14T15:30 EDT; 0 items in 8h window | normal cadence |
| `unit42` | last_successful_fetch advance to 2026-05-14T15:30 EDT; 0 items in 8h window | feedburner stable, no PA42 publication |
| `crowdstrike` | last_successful_fetch advance to 2026-05-14T15:30 EDT; 0 fresh threat-research items | continuing dateless-marketing pattern (~22 consecutive sweeps) |
| `mandiant` | failure_count: 19 → 20 (twenty-second consecutive feedburner 404) | cloud.google.com/blog/topics/threat-intelligence index page top-of-list unchanged; operator alt-endpoint decision still pending |
| `eset` | last_successful_fetch advance to 2026-05-14T15:30 EDT (RSS path); 0 items in 8h window | FrostyNeighbor article surfaced this morning via direct WebFetch / AM-001 |
| `industrialcyber-co` | unchanged | RSS feed returned 403 Forbidden this sweep; not a fail-count event (WAF / Akamai bot-blocking pattern, not failure of source); held healthy from yesterday's 18:10 EDT WebFetch |
| `bitdefender` | unchanged | feed-path 404; index-page WebFetch verified unchanged from morning sweep (post 14:30 FLASH lockout expiration, no fresh content; PM-003 surfaces Salt Typhoon Azerbaijan via SecurityWeek relay) |
| `splunk-archimedes`, `splunk-defenseclaw` | last_successful_fetch advance to 2026-05-14T15:30 EDT | 24th consecutive dormant sweep on non-archimedes-internal stream |
| `cisco-talos` (NOT in source-grades.yaml — first surface this run) | **PROVISIONAL A FIRST-CITATION FLAG** for librarian/operator | Cisco Talos is the originating primary on PM-001 (UAT-8616 SD-WAN cluster) — Tier-1 vendor research practice with first-party telemetry, named-byline (Cisco Talos collective), peer-reviewed publication history, ORB-network research lineage. Operator may ratify at A; conservative provisional A consistent with precedent applied to Mandiant / CrowdStrike / Unit 42 / MSTIC / Sophos / ESET / Dragos / SentinelOne / Wiz / Snyk / Bitdefender / Symantec / F5 / kernel-org-netdev. |
| `darktrace` (NOT in source-grades.yaml — first surface this run) | **PROVISIONAL FLAG** for librarian/operator | Darktrace is the originating primary on PM-003 Twill Typhoon analysis — Tier-1 vendor research practice with first-party telemetry, named-research-team byline, peer-reviewed APT publication history (Mustang Panda / TA416 tracking). Operator may ratify at A; provisional starting grade A recommended. |
| `socket` (NOT in source-grades.yaml — first surface this run) | **PROVISIONAL FLAG** for librarian/operator | Socket is the originating primary on PM-005 node-ipc 3-version backdoor — Tier-2 npm-security specialist vendor research; conservative provisional B starting grade per same precedent as StepSecurity / SafeDep / Aikido / Sysdig. |

## Anti-noise lockouts active

| Topic | Lockout expires | Source primary |
|---|---|---|
| Salt Typhoon Azerbaijan O&G | 2026-05-14T14:30 EDT (expired — but Twill Typhoon framing in PM-003 is new content, lockout does not apply to net-new actor cluster) | finding-2026-05-13-FLASH-0001 Bitdefender |
| Symantec MuddyWater / Seedworm Q1-2026 multi-victim | 2026-05-14T18:10 EDT (active) | finding-2026-05-13-FLASH-1800-0001 Symantec |
| ESET FrostyNeighbor / Ghostwriter / UNC1151 | 2026-05-15T08:00 EDT (active) | finding-2026-05-14-0001 ESET |
| F5 NGINX Rift K000160932 / CVE-2026-42945 | 2026-05-15T08:00 EDT (active) | finding-2026-05-14-0002 F5 |
| Linux LPE cluster (Copy Fail / Fragnesia / Dirty Frag) | 2026-05-15T08:00 EDT (active) | finding-2026-05-14-0003 BleepingComputer/Zellic/kernel-org-netdev |
| Sysdig PraisonAI scanner velocity CVE-2026-44338 | 2026-05-15T08:00 EDT (active) | finding-2026-05-14-0004 Sysdig |
| KongTuke / ModeloRAT (Rapid7 / Octo Tempest) | 2026-05-14T16:00 EDT (now-active during this brief cycle) | finding-2026-05-13-0004 Rapid7 |
| Foxconn Nitrogen ransomware | 2026-05-14T16:00 EDT (now-active during this brief cycle) | finding-2026-05-13-0002 Wired |
| BitLocker YellowKey/GreenPlasma PoCs | 2026-05-14T16:00 EDT (now-active during this brief cycle) | finding-2026-05-13-0003 BleepingComputer |

## FLASH-trigger evaluation for this sweep

**PM-001 (Cisco Catalyst SD-WAN CVE-2026-20182)** evaluates against `flash-policy.yaml` triggers:

- **Trigger 1 critical-cve-exploited**: CVSS 10.0 + active in-the-wild exploitation per CISA KEV + Talos UAT-8616 cluster + Rapid7 primary — **MATCH**. Source grade: CISA KEV is A1 procedural-fact; Cisco PSIRT is vendor-self-disclosure A1; Talos provisional A first-citation; Rapid7 provisional A (awaiting ratification but Tier-1 research practice). Cohort A2 minimum.
- **Trigger 2 tracked-actor-attribution**: UAT-8616 is NOT in `_roster.yaml`. The actor is a Talos-named cluster but not yet a tracked Archimedes actor. Decision: cluster name preserved per Hard Rule 2 ("UAT-8616 per Talos high confidence"). Trigger 2 does NOT fire (not a roster-tracked actor at evaluation time). Possible /new-actor candidacy: UAT-8616 has 2-year-plus track record across CVE-2026-20127 → CVE-2026-20182 with ORB-network infrastructure overlap; flag for operator review.
- **Trigger 5 ad-sector-campaign**: Cisco Catalyst SD-WAN deployment includes FedRAMP-Government tier explicitly named in Cisco PSIRT — A&D / DIB-direct exposure. CMMC + DFARS-216-7012-cleared environments using Cisco SD-WAN-Cloud-FedRAMP are in scope. Trigger 5 evaluates conditional MATCH (ad_sector + multi-victim — Talos cites "limited so far" exploitation — falls short of multi-victim-confirmed; partial match).
- **Trigger 6 zero-day-no-patch**: Cisco has released updates per Cisco PSIRT; patches available. Does NOT match Trigger 6.

**FLASH trigger decision**: PM-001 matches Trigger 1 (critical-cve-exploited) cleanly. The 3-day federal deadline (dueDate 2026-05-17) elevates urgency. This is a candidate for a 14:30-ish FLASH dispatch BUT the 16:00 brief is 90 minutes out — typical pattern is to roll into the afternoon brief unless trigger urgency demands faster cadence (FLASH-POLICY anti-noise rule: prefer brief incorporation over separate FLASH when the brief is within 2 hours).

**Recommendation to orchestrator**: route PM-001 to the 16:00 afternoon brief as lead finding, not as a separate FLASH. The KEV-deadline-3-days + CVSS 10.0 + active exploitation profile is brief-lead material.

**PM-002 (MSTIC Secret Blizzard / Kazuar)** does not match Trigger 1 (not exploitation-of-CVE), does not match Trigger 2 (not in roster), does not match Trigger 5 (no multi-victim active campaign — historical-targeting framing). Brief-update only.

**PM-003 (Salt Typhoon Azerbaijan + Twill Typhoon)** Salt Typhoon part is anti-noise lockout (post 14:30 FLASH expiration but no NEW Salt Typhoon-specific facts beyond yesterday). Twill Typhoon / Mustang Panda is new framing but not in roster as primary, so Trigger 2 does not fire on the cluster name. Brief-update only.

**PM-004 (OpenAI TanStack confirmation)** does not match Trigger 1 (Mini Shai-Hulud was previously raw-signaled via finding-2026-05-12-FLASH-0001), does match Trigger 5 (TanStack ecosystem multi-victim including OpenAI, ad_sector_indirect via @squawk namespace dependency-graph). Brief-update with possible promotion to confirmed-victim layer of VT-006 tracking.

**PM-005 (node-ipc 3-version backdoor)** is unattributed. Does not match Trigger 1 (auth-key compromise event, not CVE). Brief-update only with sector-watchlist context (dependency-graph unknown).

## Recommendation to orchestrator

- **PM-001 → afternoon brief lead** (CVSS 10.0 + KEV-dueDate-3-days + FedRAMP-Government deployment named + active ITW + UAT-8616 sophisticated cluster).
- **PM-002 → afternoon brief** (MSTIC Secret Blizzard / Kazuar deep-dive — new-actor candidacy flag, defense-departments-and-defense-related-companies-worldwide targeting language quoted verbatim per Hard Rule 2).
- **PM-003 → afternoon brief** as Iran-and-China-Cyber-Watch standing-section update (Salt Typhoon corroboration carry-forward + Twill Typhoon / Mustang Panda NEW cluster).
- **PM-004 → afternoon brief** as VT-006 Mini Shai-Hulud tracking update (OpenAI confirmed-victim, cert-rotation cadence).
- **PM-005 → afternoon brief** (node-ipc 3-version supply-chain — unattributed, fast-moving, dependency-graph-unknown).
