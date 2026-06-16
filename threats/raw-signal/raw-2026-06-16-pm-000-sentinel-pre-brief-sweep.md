---
raw_id: raw-2026-06-16-pm-000-sentinel-pre-brief-sweep
collected_at: 2026-06-16T15:35:00-04:00
run_id: pre-brief-20260616-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: internal-sentinel
  source_name: Archimedes Internal Sentinel (pre-brief collection)
  source_url: null
  published_at: 2026-06-16T15:30:00-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: []
triage_tags: [sentinel, pre_brief_sweep, pm_brief_substrate]
iocs_extracted: false
iocs_count: 0
text_word_count: 1620
promoted: false
ttl_expires_at: 2026-09-14T15:35:00-04:00
---

# 15:30 EDT pre-brief collection — sentinel sweep for 16:00 PM brief

## Sweep parameters

- **Window:** 2026-06-16 07:30 EDT to 2026-06-16 15:30 EDT (~8h since 07:30 morning pre-brief collection, also captures items emerging after 08:00 morning brief commit `2bde07c` and 12:00 FLASH sweep commit `61eac22`).
- **Mode:** Mode 1 pre-brief collection.
- **Splunk sentinel IOC set:** 19 indicators (PeopleSoft / UNC6240 standing tracked set).
- **Splunk indexes queried:** `defenseclaw_local` + `archimedes` (sourcetype-filtered to exclude self-telemetry).
- **Source set:** active sources per `source-grades.yaml` + `source-health.yaml` (mandiant feedburner skipped under under-24h rule; sophos top-level + msrc + volexity + ars-security top-level remain stale; spiderfoot/censys/urlscan/hibp passive-only or stale).

## Splunk sentinel results

- **0 tracked-IOC hits at -8h lookback** across `defenseclaw_local` + `archimedes` for the 19-IOC standing set (REDCap / INFINITERED / UNC6508 / UNC6240 / PeopleSoft / CVE-2026-35273 / CVE-2026-20262 / CVE-2026-25089 / CVE-2026-39813 / CVE-2026-39808 / CVE-2026-54420 / CVE-2026-48558 / SimpleHelp / FortiSandbox / NarwhalRAT / FishMonger / Backdoor.Turn / DragonForce / Cal Water).
- **16th consecutive clean sentinel cumulative since 2026-06-13 18:00 EDT** (~72h+ continuous clean window across 2026-06-13 PM + 2026-06-14 00:00 + 06:00 + 07:30 + 12:00 + 15:30 + 18:00 + 2026-06-15 00:00 + 06:00 + 08:00 implicit + 12:00 FLASH + 15:30 + 16:00 PM implicit + 18:00 + 2026-06-16 00:00 + 06:00 + 08:00 implicit + 12:00 FLASH + this 15:30 pre-brief).
- Silent Splunk does NOT disconfirm per Hard Rule 8 — visibility-limited absence flagged not negative-evidence (Frank is NOT a North American medical research / military health institution running REDCap; NOT a Higher-Ed PeopleSoft tenant; NOT a LiteSpeed cPanel shared-hosting environment; NOT a Cisco SD-WAN Manager deployment; NOT a FortiSandbox sandboxing-platform deployment; NOT a California water utility).

## CISA KEV delta vs FLASH-1200 baseline (commit `61eac22`)

- **0 net-new KEV additions in window** since 12:00 sweep.
- Five most-recent KEV (unchanged): CVE-2026-54420 LiteSpeed cPanel (2026-06-15, deadline 2026-06-18 ~T+50h), CVE-2026-20262 Cisco Catalyst SD-WAN Manager (2026-06-15, deadline 2026-06-29 T-13d), CVE-2026-35273 PeopleSoft (2026-06-12, deadline closed EOD 2026-06-15 retrospective phase), CVE-2026-10520 Ivanti Sentry (2026-06-11, deadline 2026-06-14 retrospective phase), CVE-2026-11645 Google Chromium V8 (2026-06-09).
- **FortiSandbox 3-CVE cluster (CVE-2026-25089 / CVE-2026-39813 / CVE-2026-39808) NOT YET KEV-listed at this sweep** — anticipated 24-72h window per FLASH-1200 substrate carry-forward; still in pathway-pending state.

## In-window items collected (raw-signaled this sweep)

- **raw-2026-06-16-pm-001** — Dark Reading (Rob Wright byline) **SprySOCKS Windows Variant Abuses Kernel Drivers to Evade Detection**, 2026-06-16T20:11:48 UTC. **Substrate-strengthening UPDATE candidate** for finding-2026-06-16-0001 (ESET FishMonger SprySOCKS Windows variants). Third independent A&D-relevant journalistic relay of ESET-WeLiveSecurity primary (after THN-Lakshmanan + BC-Toulas this AM). Editorial-byline-not-vendor-PSIRT layer; original cluster identity (FishMonger / China-nexus / Honduras-Taiwan-Thailand-Pakistan government victims) preserved verbatim per Hard Rule 2.

- **raw-2026-06-16-pm-002** — CISA ICS Advisories 5-record **Rockwell Automation cluster** (icsa-26-167-01 through icsa-26-167-05), all dated 2026-06-16T12:00 UTC. **Net-new A1 government primary** on CompactLogix 5370 / Compact GuardLogix 5370 / ControlLogix 5570 / GuardLogix 5570 (CVE-2026-11317 DoS via CIP CVSS 7.5), RSLinx Classic (CVE-2020-13573 stack-overflow CVSS 7.5), FLEX I/O EtherNet/IP Adapters 1794-AENTR / 1794-AENTRXT (CVE-2026-0646 + CVE-2026-0647 CVSS **9.4** missing-auth + memory-leak), FactoryTalk Analytics PavilionX (CVE-2025-14272 missing-auth CVSS 7), CompactLogix 5370 L1/L2/L3 (CVE-2025-11694 CIP DoS CVSS 7.5). Critical Manufacturing sector deployment baseline; widely deployed in A&D industrial bases (manufacturing floors, supplier networks, factory-automation tenants). No active exploitation cited; standing vendor PSIRT advisories cross-walked into CISA ICS channel.

- **raw-2026-06-16-pm-003** — The Hacker News (Ravie Lakshmanan byline) **ClickFix Campaigns Expand Malware Delivery With New Loaders and Fake Update Lures**, 2026-06-16T17:41:28 UTC. **Substrate update** on /new-actor-Vice-Society operator-deferred candidacy via BlueVoyant-primary attribution: **"Lorem Ipsum Loader [...] attributed with high confidence to Vanilla Tempest (aka Rapid Brigantine, Vice Society, and Vice Spider)"** — Vanilla Tempest = MSTIC naming of Vice Society. Substrate-strengthening over FLASH-1200 Dark Reading single-publisher Vice Society linkage on Lorem Ipsum Malware/ClickFix. Three-loader cluster: BabaDeda (Morphisec), Lorem Ipsum (BlueVoyant), Potemkin (Huntress). Targets education/financial/architecture/legal/construction — NO A&D-prime named victim.

## In-window items evaluated and discarded (non-raw-signal-eligible)

- **SW-Kovacs Cal Water Investigating Iranian Hackers' Claims** (2026-06-16T11:53Z primary): out-of-A&D-scope California water utility; Handala #014 NOT on roster; Cal Water response statement "no indication of operational disruptions to its water and wastewater systems" REINFORCES Iran Cyber Watch third-source NEGATIVE binding from 2026-06-13 PM. Possible PM brief Other Signal one-liner status pivot from "NEGATIVE binding" to "victim publicly investigating denies operational impact" — operator-deferred Handala #014 dossier handoff. Anti-noise rule 1 BINDING — same trigger-topic already covered in carry-forward.
- **SW-Kovacs iRhythm Confirms Data Stolen in Hack** (2026-06-16T15:06Z) + **SA-Paganini iRhythm Hit by Cyberattack Patient Data Stolen and Ransom Demanded** (2026-06-16T19:19Z relay): out-of-A&D-scope digital healthcare cardiac monitoring; already rejected this AM as reject-2026-06-16-0003. Anti-noise rule 1 BINDING.
- **SW-Arghire Cybercrime Group Claims Novo Nordisk Hack 1.3TB FulcrumSec** (2026-06-16T12:32Z): out-of-A&D-scope pharma; FulcrumSec NOT on roster.
- **SA-Paganini Fortinet Warned as Three Critical FortiSandbox Bugs Come Under Attack** (2026-06-16T14:21Z) + **HNS-Zorz Attackers are exploiting FortiSandbox vulnerabilities** (2026-06-16T15:27Z): anti-noise rule 1 BINDING — same trigger-topic already covered in AM brief finding-2026-06-16-0002 and at FLASH-1200 noted as THN+SA+HNS triple-publisher independent relay of Defused-Cyber-IR-vendor observation. Substrate-strengthening only on observation layer; single-source veto on Defused itself still applies. **CISA KEV pathway NOT YET LISTED at this sweep** — anticipated 24-72h window.
- **HNS-Markovic Cybercriminals mask malicious communications through Microsoft Teams relays** (2026-06-16T14:22Z): anti-noise rule 1 BINDING — same trigger-topic already covered in AM brief finding-2026-06-16-0004 (Symantec DragonForce Backdoor.Turn). HNS independent B-grade second-publisher relay substrate-strengthening already noted at FLASH-1200. Symantec-attribution-language single-vendor-on-novel-TTP-layer veto persists. Possible PM brief UPDATE candidate substrate-strengthening only. Scattered-Spider/DragonForce linkage Hard-Rule-2 BINDING preserved.
- **HNS-Zorz SimpleHelp RMM flaw could give attackers full access to managed endpoints (CVE-2026-48558)** (2026-06-16T13:33Z): Horizon3.ai discoverer autonomous-AI-vulnerability-hunting. Patched late May 2026 v5.5.16-stable + v6.0-RC2. Vendor "not aware of malicious exploitation". CVSS not provided in article. Theoretical exploitation only — anti-noise rule 1 BINDING (already evaluated at FLASH-1200). Possible Other Signal one-liner for PM brief or 2026-06-17 morning if KEV-listed or active-exploitation surfaces. SimpleHelp lineage CVE-2025-1095/1096 ransomware-operator-exploitation watch-pattern lift.
- **BC-Toulas Steam Workshop abused to spread malware via Wallpaper Engine app** (2026-06-16T18:27Z): out-of-A&D-scope consumer gaming platform.
- **BC-Sharma UK to require ID or face scan before social media accounts** (2026-06-16T14:38Z): non-signal UK policy/regulation.
- **BC-Sponsored-Varonis GhostTree Attack Abused Recursive Windows Junctions to Hide Malware** (2026-06-16T14:17Z): sponsored-content Varonis defensive-research detection-engineering pattern only; no actor / no CVE / no A&D-prime named victim. Anti-noise rule 1 BINDING (same trigger-topic discarded at FLASH-1200).
- **BC-Gatlan FTC warns of record $3.5 billion losses to imposter scams in 2025** (2026-06-16T13:42Z): non-signal FTC consumer-protection statistics.
- **SW-Arghire White House Issues Memo to Bolster NSS Cybersecurity NSPM-12** (2026-06-16T11:41Z): non-signal National Security Systems policy memorandum.
- **SW Magnitude / Ent / TrustCloud / TekStream / AppViewX / Teleport / Radware Xploit Shield** (multiple, throughout window): industry-news/vendor-marketing/funding announcements. TekStream + Radware reference Anthropic Mythos as positioning — Mythos/Fable-5 finding-2026-06-15-0010 PM substrate carry-forward (already covered).
- **SW-Townsend Hacker Conversations: Isira Adithya** (2026-06-16T14:27Z): feature-interview-profile.
- **SW-Townsend AI and Cybersecurity – Everything You Wanted to Know** (2026-06-16T13:15Z): non-signal long-form feature analysis.
- **TR India temporarily blocks Telegram over medical exam cheating fears** (2026-06-16T15:38Z): non-signal India regulatory action.
- **THN Rokarolla Android Banking Trojan** (2026-06-16T13:10Z) + **DR Rokarolla Android Trojan Levels Up** (2026-06-16T17:32Z): commodity Android banking trojan; no actor / no A&D-prime named victim. Anti-noise rule 1 BINDING (same trigger-topic discarded at FLASH-1200).
- **THN Survey: 94% of Incidents Involve Anonymized Infrastructure** (2026-06-16T11:30Z): sponsored-research non-signal.
- **CrowdStrike blog feed**: 10 dateless marketing/announcement items (Falcon Exposure Management 3P, Continuous Identity for AI Agents, Patch Tuesday June 2026 analysis, ISO 42001:2023, Frost Radar). No CrowdStrike fresh threat research surfacing through RSS feed.

## Soft observations carried (under-24h skip rule applies — NOT mutated this sweep)

- **mandiant** feedburner RSS canonical-swap pending (last attempt 2026-06-14 07:31 failure_count 27, stale_since 2026-06-13). Direct cloud.google.com HTML success-pattern entrenched 9+ consecutive successes (this sweep top-8 retrieved: GTIG AI Threat Tracker / UNC6508 China-Nexus Medical / ShinyHunters PeopleSoft / Seeking Counsel US Law Firms / KnowledgeDeliver ViewState / PhaaS 2 Furious / BlackFile Vishing / UNC6692 Snow Flurries — all out-of-window already in corpus). RSS not re-attempted this sweep under under-24h rule; canonical-swap decision still operator-deferred.
- **proofpoint** /us/threat-insight/blog/feed 5x consecutive 404 soft-pattern fully entrenched. THN relay backstop productive.
- **sophos** top-level news.sophos.com/en-us/feed/ stale-persistent since 2026-05-17. Replacement candidate news.sophos.com/en-us/category/threat-research/feed/ standing.
- **Dark Reading** rss.xml RECOVERY-PERSISTENCE-CONFIRMED 200 OK this sweep (3 items in window, all relayed above). Recovery cumulative across multiple sweeps — pattern firmly transient.
- **msrc** stale_since 2026-05-30 long-stale; content reaches corpus via SA/TR/SW relays.

## Source-health runtime updates this sweep (preserve operator-set notes verbatim)

Per `source-health.yaml` field-ownership rule: runtime fields only (`status`, `last_successful_fetch`, `failure_count`, `stale_since`, `last_error`); operator-set `notes` preserved verbatim. Updates this sweep set `last_successful_fetch: 2026-06-16T15:35:00-04:00` for: cisa-advisories (5 ICS items in window), bleepingcomputer (4 items), securityweek (9 items), securityaffairs (2 items), helpnetsecurity (7 items), the-record (1 item), darkreading (3 items), sans-isc (0 items), krebs (0 items), mstic (0 items), crowdstrike (10 dateless items pattern persistent), unit42 (0 items), cisco-talos (0 items). No status flips; failure_counts unchanged.

## Notes for grader / briefer

- **finding-2026-06-16-0001 (ESET FishMonger SprySOCKS Windows)**: Dark Reading Rob Wright independent A&D-relevant journalistic relay — substrate-strengthening from THN+BC dual-publisher to THN+BC+DR triple-publisher; ESET-WeLiveSecurity single-vendor-IR-firm-on-cluster-identity-layer veto persists.
- **finding-2026-06-16-0002 (FortiSandbox 3-CVE)**: SA-Paganini + HNS-Zorz substrate-strengthening already noted at FLASH-1200 (no new substrate this sweep, only PM brief eligibility lift). CISA KEV pathway not yet listed.
- **finding-2026-06-16-0004 (Symantec DragonForce Backdoor.Turn)**: HNS-Markovic independent B-grade second-publisher relay already noted at FLASH-1200. Substrate-strengthening only.
- **finding-2026-06-15-0006 (Cisco SD-WAN CVE-2026-20262)**: no net-new substrate this sweep; KEV listing event closed at AM brief.
- **Net-new CISA Rockwell ICS cluster**: 5 advisories dated 2026-06-16, FLEX I/O at CVSS 9.4. Critical Manufacturing relevance — possible PM brief Other Signal A&D ICS one-liner or net-new finding candidacy at grader discretion.
- **Vice Society / Vanilla Tempest substrate update**: THN-Lakshmanan + BlueVoyant attribution preserved verbatim per Hard Rule 2 ("attributed with high confidence to Vanilla Tempest (aka Rapid Brigantine, Vice Society, and Vice Spider)") — substrate-strengthening on /new-actor-Vice-Society operator-deferred candidacy from FLASH-1200 Dark Reading single-publisher to FLASH-1200-DR + THN-BlueVoyant dual-publisher.
- **Cal Water/Handala #014 carry-forward**: SW-Kovacs primary status pivot from "NEGATIVE binding" to "victim publicly investigating denies operational impact" — possible PM brief Other Signal one-liner status pivot, operator-deferred Handala #014 dossier handoff if substrate strengthens further.
- **Anti-noise rule 1 binding**: 19 in-window items evaluated and discarded — no double-coverage on AM finding substrate or FLASH-1200 substrate.
