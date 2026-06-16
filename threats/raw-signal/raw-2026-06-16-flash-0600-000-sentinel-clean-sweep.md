---
raw_id: raw-2026-06-16-flash-0600-000-sentinel-clean-sweep
collected_at: 2026-06-16T06:05:00-04:00
run_id: flash-sweep-20260616-060000
collection_mode: flash_sweep
source:
  source_yaml_id: internal-sentinel
  source_name: Archimedes Internal Sentinel (FLASH sweep)
  source_url: null
  published_at: 2026-06-16T06:00:00-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: []
triage_tags: [sentinel, flash_clean_sweep, non_flash, quiet_hours]
iocs_extracted: false
iocs_count: 0
text_word_count: 1980
promoted: false
ttl_expires_at: 2026-09-14T06:05:00-04:00
---

# 06:00 EDT FLASH sweep — clean sentinel (quiet hours)

## Sweep parameters

- **Window:** 2026-06-16 00:00 EDT to 2026-06-16 06:00 EDT (6h FLASH window since prior sweep at commit 3b68356 sentinel 00:00).
- **Quiet hours:** **ACTIVE** (06:00 EDT is outside 09:00-21:00 EDT). Any triggered FLASH would queue to `infrastructure/flash-queue.yaml` for the 09:00 catchup sweep unless critical override conditions are met (4-of-4: CVSS 10.0 + active exploitation + tracked actor + named A&D-watchlist victim).
- **Trigger evaluation:** 6 FLASH triggers per `doctrine/FLASH-POLICY.md`.
- **Splunk sentinel IOC set:** 19 indicators (PeopleSoft / UNC6240 standing tracked set, unchanged from prior sweep).
- **Splunk indexes:** defenseclaw_local + archimedes (sourcetype-filtered to exclude self-telemetry).

## Results

- **candidates_found:** 0
- **triggers_fired:** []
- **Splunk sentinel:** **0 tracked-IOC hits at -6h lookback** across `defenseclaw_local` + `archimedes`, sourcetype-filtered to exclude `archimedes:operation` / `archimedes:scheduler` self-telemetry. This is the **14th consecutive clean sentinel sweep** across the cumulative window (2026-06-13 PM through this sweep — ~60h continuous clean window). Silent Splunk does NOT disconfirm per Hard Rule 8 — visibility-limited absence (Frank is NOT a North American medical research / military health institution running REDCap consistent with 100% UNC6508 victim profile; NOT a Higher-Ed PeopleSoft tenant consistent with 68% UNC6240 victim profile; NOT a LiteSpeed cPanel shared-hosting environment; NOT a Cisco SD-WAN Manager deployment; NOT a FortiSandbox sandboxing-platform deployment).
- **CISA KEV:** **0 net-new additions in window.** Last additions remain CVE-2026-54420 (LiteSpeed) and CVE-2026-20262 (Cisco SD-WAN Manager), both dated 2026-06-15 and both evaluated as non-FLASH-eligible in the 00:00 sweep (anti-noise dedup binding). Five most-recent unchanged from 00:00 sweep commit 3b68356.

## In-window items evaluated and discarded as non-FLASH-eligible

| Item | Source | Trigger evaluation | Disposition |
|---|---|---|---|
| **Fortinet FortiSandbox CVE-2026-39813 + CVE-2026-39808 + CVE-2026-25089 — Defused threat-intel observation of active exploitation in past 24 hours** (CVE-2026-39813 CVSS 9.8 path traversal CWE-24; CVE-2026-39808 CVSS 9.8 OS command injection CWE-78; CVE-2026-25089 CVSS 9.8 OS command injection CWE-78; all three patched April 14, 2026 in patch-bundle FG-IR-26-112/100/141) | BleepingComputer (B) primary — Sergiu Gatlan 2026-06-16T09:19Z — relaying Defused threat-intelligence telemetry observation (Defused not in `source-grades.yaml`) | **T1 EVALUATION:** CVSS 9.8 ≥ 9.0 floor ✓; active exploitation per Defused observation "We are observing exploitation of multiple Fortinet FortiSandbox vulnerabilities during the past 24 hours" ✓; **A-grade source requirement FAILS** — BC is B-grade per `source-grades.yaml`, Defused is not in source-grade corpus (unknown reliability tier), no concurrent A-grade vendor IR / CISA advisory / SentinelOne / Help Net relay observed in window. **T6 FAIL** — patches available April 14, 2026 (~2 months ago), not zero-day-without-patch. **T2/T4 FAIL** — no tracked actor attribution per BC ("specific threat actor attribution... [not] provided"). **T5 FAIL** — no A&D-prime named victim, generic Fortinet customer exploitation. Critical override **0-of-4** (no tracked actor, no named A&D victim). | **Discarded as FLASH** — non-FLASH-eligible on A-grade source gate. **STRONG morning brief candidate for 08:00 brief** — A&D-relevance MODERATE-to-HIGH (FortiSandbox is a sandboxing/EDR-pipeline appliance commonly deployed in DIB/federal civilian estates for malware detonation; unauthenticated RCE on a security-detection appliance is a high-impact vector for environments running FortiSandbox in the dirty-traffic pipeline). Watch for SentinelOne / Help Net / SecurityWeek A-grade independent corroboration in next pre-brief sweep — would lift T1 grade if landed. Defused observation 24h window suggests ITW activity is current; CISA KEV addition pathway expected in 1-to-7-days (parallel pattern to CVE-2026-20262 Cisco SD-WAN watch closed 2026-06-15). |
| **APT37 / ScarCruft NarwhalRAT** — new Python-based RAT delivered via spear-phishing impersonating Microsoft Account security notifications; "departure from RokRAT, a malware family exclusively attributed to the hacking group"; C2 domains daehoat[.]com + novel21[.]co.kr + scheduled task "MicrosoftUserInterfacePicturesUpdateTackMachine"; staging dir %APPDATA%\naverwhale | The Hacker News (B) primary 2026-06-16T08:14Z — relaying Genians Security Center (GSC) (originating Korean security firm, not in `source-grades.yaml`) | **T4 EVALUATION:** new tooling ✓ (NarwhalRAT brand-new tool — explicit departure from RokRAT exclusivity claim, this is genuinely novel TTP-class evolution not a variant); B-grade source ✓ (THN B); attributable to tracked actor ✓ (APT37 is roster #024). **T4 FIRES STRUCTURALLY.** **HOWEVER:** (a) single-publisher constraint — only THN; Genians attribution language is informal ("shares multiple similarities with prior Python-based attacks orchestrated by ScarCruft") not vendor-high-confidence framing; (b) single-source veto would apply at grader stage; (c) quiet-hours queueing (06:00 EDT — quiet hours) means any FLASH would queue for 09:00 sweep catchup, but the 08:00 morning brief (~T+2h) would supersede any queued FLASH; (d) FLASH-POLICY anti-noise rule 4 (weekly FLASH count vigilance — too many FLASHes erode signal) applies. Critical override 0-of-4 (CVSS not applicable — no CVE assigned; no named A&D-prime victim; no named victim at all per article). | **Discarded as FLASH** — T4 fires structurally but operationally better served as **08:00 morning brief substrate** than as quiet-hours-queued FLASH that the morning brief would supersede. Grader should evaluate as morning brief candidate — net-new APT37 tooling departure from RokRAT exclusivity claim is genuinely interesting. Worth tracking: independent A-grade vendor IR corroboration (Mandiant / CrowdStrike / Unit 42 / MSTIC / Volexity) would lift confidence. APT37 last-reviewed 2026-05-10, MEDIUM threat-level on weighted scoring; this substrate does NOT shift Intent (no A&D-prime targeting documented) but may inform Capability category at next /update-tracking. |
| **Earth Lusca / Aquatic Panda / FishMonger / TAG-22 SprySOCKS Windows variant** — Windows variants of previously-documented Linux malware used to attack government organizations in Taiwan/Thailand/Pakistan/Honduras 2023-2024; foreign affairs / tech / telecom sectors; new capabilities include kernel-level stealth via RawWNPF driver (WIN_DRV variant), TCP traffic diversion, UEFI bootkit component; references CVE-2023-24932 Secure Boot flaw potentially leveraged | BleepingComputer (B) primary — Bill Toulas 2026-06-16T09:00Z — relaying ESET (A) WeLiveSecurity research | **T2 GATE FAIL** — Earth Lusca / Aquatic Panda NOT on 24-actor `_roster.yaml` (roster verified: total_actors:24, no entry for Earth Lusca / Aquatic Panda / FishMonger / Red Dev 10 / TAG-22). **T4 GATE FAIL** — not attributable to tracked actor. **T5 FAIL** — historical 2023-2024 activity (retrospective), not active multi-victim campaign; gov-targets named are not A&D-prime / DIB / CMMC entities. ESET attribution language: "ESET attributes the activity with high confidence to the Earth Lusca threat actor" — high-confidence framing but not actionable through tracked roster. | **Discarded as FLASH** — non-FLASH-eligible per roster gate. **Operator-deferred /new-actor candidate surface** — substrate-strengthening: Earth Lusca / Aquatic Panda is a well-attested Chinese cluster (TAG-22 per Recorded Future, Aquatic Panda per CrowdStrike) with documented government-sector targeting and now Windows-variant + UEFI-bootkit capability evolution. If operator invokes `/new-actor` for Earth Lusca, actor-profiler subagent would scaffold dossier with ESET A-grade primary + BC B-grade relay substrate. Possible Other Signal candidate for 08:00 morning brief if grader assesses standalone substrate. |
| **Unit 42 Pickle in the Middle — Vertex AI Python SDK CVE-not-assigned bucket-squatting cross-tenant RCE** | Unit 42 (A2) primary direct retrieval 2026-06-16T10:00Z — Ori Hadad | **T1 FAIL** — CVSS not assigned; bug-bounty disclosure pathway. **T6 FAIL** — Google patched in google-cloud-aiplatform v1.144.0 (2026-03-31) and v1.148.0 (2026-04-15), patch landed ~2 months ago. **T2/T4/T5 FAIL** — no actor attribution, no exploitation in wild, no named A&D-prime victim. Unit 42 responsibly disclosed 2026-03-05; this is the public write-up. | **Discarded as FLASH** — patched and no ITW. **Other Signal candidate for 08:00 morning brief** — A&D-relevance MODERATE (Vertex AI SDK is the canonical Google ML platform; A&D-prime ML pipelines using google-cloud-aiplatform 1.139.0-1.140.0 between 2026-02 (vulnerable window) and 2026-04-15 (full patch) had exposure to cross-tenant RCE via pickle deserialization in joblib model files; bucket-squatting blast radius is significant for any tenant that did not upgrade to 1.148.0+). Worth surfacing for A&D ML/MLOps audiences. |
| **iRhythm Holdings data breach disclosure** — digital healthcare company breach via third-party-hosted business applications, patient personal + health information stolen | BleepingComputer (B) 2026-06-16T06:31Z — Sergiu Gatlan | Non-signal — no CVE, no actor attribution, no IOC, healthcare-sector breach (not A&D / not DIB / not CMMC / not ITAR), self-disclosure pattern. T1-T6 all FAIL. | Discarded. Out of scope. |
| **SecurityWeek Tech Coalition Athena — OSS vulnerability triage platform announcement** (Chainguard + 24+ orgs) | SecurityWeek (B) primary 2026-06-16T09:39Z — Ionut Arghire | Non-signal — coalition announcement, no active exploitation, no CVE, no actor, no A&D incident. | Discarded. Out of scope. |
| **Security Affairs UNC6508 China-linked actor medical research networks 2-year campaign** — restatement of GTIG Mandiant primary | SecurityAffairs (B) 2026-06-16T07:32Z — Pierluigi Paganini, relaying GTIG primary | **Anti-noise rule 1 BINDING** — UNC6508 / INFINITERED PRC-nexus medical/military-health/AI/UAS research espionage 72h FLASH dedup hold active through 2026-06-18 12:00 EDT (from FLASH-1200 c48f6fc baseline). SA is non-independent relay of GTIG primary, no independent telemetry. | Discarded. Anti-noise dedup. Substrate-strengthening for finding-2026-06-15-flash1200-0006 if grader assesses as second-publisher independence confirmation (SA + BC + SW now three relays of GTIG primary — none independent corroboration). |
| **THN Cisco SD-WAN Manager active exploitation CVE-2026-20262 patches released** (CVSS 6.5 medium-severity) | The Hacker News (B) 2026-06-16T06:05Z | **Anti-noise rule 1 BINDING** — same trigger-topic as PM brief 580af3f finding-2026-06-15-0006 + 00:00 sweep KEV-listing-watch-CLOSED disposition. THN is restatement of Cisco PSIRT + KEV addition, not net-new substrate. | Discarded. Anti-noise dedup. UPDATE substrate for 08:00 morning brief — finding-0006 status pivot to KEV-listed-2026-06-15-with-BOD-22-01-deadline-2026-06-29. |
| **THN CISA LiteSpeed cPanel CVE-2026-54420 KEV flag** | The Hacker News (B) 2026-06-16T05:41Z | **Anti-noise rule 1 BINDING** — same as 00:00 sentinel sweep evaluation. T1 FAIL (CVSS 8.5 below 9.0 floor), T3 GATE FAIL (shared-hosting/CloudLinux/CageFS not A&D-watchlist), T6 FAIL (patched 2026-06-01). | Discarded. Anti-noise dedup. Other Signal candidate for 08:00 morning brief (KEV mitigation deadline 2026-06-18 ~T+58h from this sweep). |
| **SecurityWeek Cisco Patches Another SD-WAN Zero-Day Exploited in Attacks** | SecurityWeek (B) 2026-06-16T06:20Z — Eduard Kovacs | Anti-noise rule 1 BINDING — same as Cisco SD-WAN above. Restatement. | Discarded. Anti-noise dedup. |
| **SecurityAffairs CISA adds Cisco Catalyst and LiteSpeed cPanel plugin flaws to KEV** | SecurityAffairs (B) 2026-06-16T08:53Z — Pierluigi Paganini | Anti-noise rule 1 BINDING — combined relay of both 2026-06-15 KEV adds already in dedup hold. | Discarded. Anti-noise dedup. |
| **SANS ISC Diary — From a VHDX File to a Remcos RAT** | SANS ISC (B) 2026-06-16T07:09Z — Xavier Mertens | Generic Remcos malware delivery analysis (VHDX disk-image container → JavaScript → PowerShell → .NET reflective loader → Remcos C2 animal342[.]duckdns[.]org:53552); German-speaking target lure ("Partnerschaft fur neue Angebotsanfrage.js"); commodity RAT delivery — no specific actor attribution, no A&D-prime victim, no tracked-actor TTP. Sample IOCs: SHA256 a0104921a2d37ab87482ac9a9f5c3713479c118846c3e999178e75b81620c094 (ZIP), C2 cembusconfort[.]ro, animal342[.]duckdns[.]org:53552. | Discarded. Out of scope. Commodity malware delivery analysis. |
| **Help Net Security items** — 8 items: ENISA SBOM CRA software supply-chain transparency analysis, Check Point hospitality/travel sector scams, GitHub multilingual dataset, Oplane AI threat modeling interview, EU Cybersecurity Act 2.0 opinion, Delinea machine identities/agentic AI podcast, AI data governance revenue feature, jobs listing | Help Net Security (B) primary | All non-signal — policy analysis, opinion pieces, vendor interviews, dataset releases, jobs listings. No incident substrate, no CVE, no actor, no A&D-prime targeting. | Discarded. Out of scope. |

## Anti-noise carry-forward holds preserved

- **UNC6508 / INFINITERED PRC-nexus medical/military-health/AI/UAS research espionage** — 72h anti-noise lock through 2026-06-18 12:00 EDT (FLASH-1200 c48f6fc baseline). SA + BC + SW restatement-relays this sweep — none independent corroboration; substrate-strengthening only.
- **CVE-2026-35273 PeopleSoft FCEB BOD 26-04** — deadline closed EOD 2026-06-15. Retrospective compliance-metrics phase. Mandiant A1 primary UNC6240/ShinyHunters coverage shipped finding-2026-06-13-0006 + finding-2026-06-15-0008 (CoE/ShinyHunters acknowledgement).
- **CVE-2026-10520 Ivanti Sentry** — retrospective compliance-metrics phase, deadline closed 2026-06-14.
- **CVE-2026-0257 PAN-OS** — retrospective compliance-metrics phase, deadline 2026-06-01 ~15d past; vendor confirmation finding-2026-06-15-0004 shipped.
- **CVE-2026-20253 Splunk Enterprise** — HOLD vendor confirmation pending.
- **Fable 5 / Mythos 5 Anthropic USG export-control** — finding-2026-06-15-0010 PM substrate.
- **Velvet Ant Operation Highland Sygnia** — finding-2026-06-15-0007 carry-forward.
- **Handala #014 / Cal Water Iran Cyber Watch** — third-source NEGATIVE binding stands from 2026-06-13 PM.
- **Check Point VPN CVE-2026-50751 / Qilin** — carry-forward.
- **CVE-2026-20262 Cisco Catalyst SD-WAN Manager** — KEV-listing watch CLOSED 2026-06-15 (added with BOD-22-01 deadline 2026-06-29); finding-2026-06-15-0006 UPDATE-eligible for 08:00 morning brief.
- **CVE-2026-42824 SearchLeak M365 Copilot Enterprise** — patched no ITW; finding-2026-06-15-0011 vuln-tracker-handoff-operator-deferred stands.
- **CVE-2026-54420 LiteSpeed cPanel Plugin** — KEV addition 2026-06-15, mitigation deadline 2026-06-18 ~T+58h; Other Signal candidate for 08:00 morning brief.

## Sources queried + status

| source_yaml_id | status | in-window items |
|---|---|---|
| thehackernews | 200 OK, last_modified Tue 16 Jun 08:26 GMT | 3 (NarwhalRAT/APT37 — T4 discarded as morning brief substrate; Cisco SD-WAN — dedup; LiteSpeed cPanel — dedup) |
| bleepingcomputer | 200 OK, last_modified Tue 16 Jun 09:59 GMT, etag bd69637c86ba199f6829963ca157b3ac | 3 (FortiSandbox Defused active exploitation — T1 source-gate fail discarded as morning brief substrate; SprySOCKS Windows / Earth Lusca — roster gate fail discarded as /new-actor surface; iRhythm — out of scope) |
| securityweek | 200 OK, last_modified Tue 16 Jun 09:39 GMT, etag W/"b4f494f4fa6471795f83c806a1610cc1" | 2 (Tech Coalition Athena — out of scope; Cisco SD-WAN — dedup) |
| securityaffairs | 200 OK, last_modified Tue 16 Jun 08:53 GMT | 2 (CISA KEV combo Cisco+LiteSpeed — dedup; UNC6508 medical research relay — anti-noise dedup) |
| the-record | 200 OK, no items in window | 0 |
| sans-isc | 200 OK, last_modified Tue 16 Jun 09:59 GMT, etag W/"1613b-6545bff451bdc" | 1 (VHDX to Remcos RAT — out of scope) |
| unit42 | 200 OK, last_modified Tue 16 Jun 10:00 GMT, etag "f1ddd73c795dbf84c84109c6bf478699-gzip" | 1 (Vertex AI Pickle in the Middle — patched no ITW discarded as morning brief substrate) |
| helpnetsecurity | 200 OK, last_modified Tue 16 Jun 09:26 GMT | 8 (all out of scope — policy/analysis/opinion/jobs) |
| cisa-advisories (all.xml) | 200 OK | 0 |
| cisa-kev (JSON direct) | 200 OK | **0 net-new in window** (last add 2026-06-15) |
| darkreading | 200 OK, last_modified Tue 16 Jun 10:03 GMT, no items in window | 0 |
| rapid7 | 200 OK, last_modified Tue 16 Jun 09:47 GMT, no items in window | 0 |
| sophos (replacement candidate /category/threat-research/feed/) | NOT QUERIED — operator-deferred replacement decision pending; carry-forward from prior sweeps | n/a |
| mandiant (cloud.google.com direct HTML) | 200 OK — partial probe (listing only); GTIG AI Threat Tracker post visible in listing but slug not retrievable via WebFetch this sweep, not blocking | listing-only; net-new in-window items if any will surface via THN/BC/SA/SW relays |
| mandiant (feedburner) | NOT RE-ATTEMPTED — under-24h skip rule (stale_since 2026-06-13, last attempt 2026-06-14 07:31 failure_count 27). Direct cloud.google.com HTML success-pattern entrenched 7+ consecutive; canonical-swap operator decision still pending. | n/a |
| sophos (top-level news.sophos.com/en-us/feed/) | NOT RE-ATTEMPTED — under-24h skip rule (stale_since 2026-05-17 long-stale) | n/a |
| proofpoint | NOT RE-ATTEMPTED — 5x consecutive 404 soft-pattern, THN relay backstop productive | n/a |
| msrc | NOT RE-ATTEMPTED — stale_since 2026-05-30 long-stale; MSRC content reaches corpus via SA/TR/SW relays | n/a |
| splunk (defenseclaw_local + archimedes) | health OK (Splunk 10.2.2 build 80b90d638de6) | **0 tracked-IOC hits at -6h lookback** (14th consecutive clean sentinel) |

## Soft observations carried (NOT mutated this sweep — under-24h skip rule applies)

- **mandiant feedburner RSS canonical-swap pending** — direct cloud.google.com HTML success-pattern entrenched 7+ consecutive successes vs RSS-path 27 consecutive failures (last RSS attempt 2026-06-14 07:31). Operator-deferred canonical-swap decision still standing.
- **proofpoint /us/threat-insight/blog/feed 5x consecutive 404 soft-pattern** fully entrenched. THN relay backstop productive. NOT promoted to stale without operator approval.
- **sophos top-level news.sophos.com/en-us/feed/** stale-persistent since 2026-05-17. Replacement candidate `news.sophos.com/en-us/category/threat-research/feed/` standing from 2026-06-14 PM sweep — pending operator decision on canonical replacement.
- **Dark Reading rss.xml** — 200 OK this sweep + 200 OK 00:00 sweep. Recovered pattern confirmed (06:00 2026-06-15 single-failure was transient, never promoted to stale on single-failure basis).

## Source-health.yaml mutations

**NONE.** All in-window observations fall under under-24h skip rule or are routine healthy fetches that don't shift status. No new failures, no recoveries needing tracking.

## Splunk sentinel query executed

```
search (index=defenseclaw_local OR index=archimedes)
  sourcetype!=archimedes:operation sourcetype!=archimedes:scheduler
  (
    "142.11.200.186" OR "142.11.200.187" OR "142.11.200.188" OR
    "142.11.200.189" OR "142.11.200.190" OR "176.120.22.24" OR
    "azurenetfiles.net" OR "agent.ashx" OR
    "2ab684d93c1553fad87041b4dea97188a97e78589deee2a7bacff905564f3a35" OR
    "f02a924c9ff92a8780ce812511341182c6b509d45bc59f3f7b522e37225d24fc" OR
    "d83fdb9e53c5ff03c4cb0451ea1bebd79b53f29eadc1e2fa394c7af13a86ce2f" OR
    "c7e9332731b06644fc73e0046a2a89eaa59b09f54250e9bd622467187351711f" OR
    "68257a6f9ff196179ec03624e849927f26599eb180a7c82e14ef5bc4e93bc309" OR
    "_fanout.sh" OR "meshagent64-azure-ops" OR "meshagent64-v2" OR
    "meshagent32-azure-ops" OR "BebitaBarefoot774" OR "INFINITERED"
  )
  earliest=-6h@h latest=now
```

Result: `event_count: 0, events: []`. Health check: Splunk reachable, version 10.2.2 build 80b90d638de6 server Frank, license OK.

## Cumulative sentinel-clean cadence (since 2026-06-13 18:00 EDT baseline)

14 consecutive clean sentinel sweeps:
1. 2026-06-13 18:00 (PM brief baseline)
2. 2026-06-14 00:00
3. 2026-06-14 06:00
4. 2026-06-14 07:30 (pre-brief)
5. 2026-06-14 12:00
6. 2026-06-14 15:30 (pre-brief)
7. 2026-06-14 18:00
8. 2026-06-15 00:00
9. 2026-06-15 06:00
10. 2026-06-15 08:00 morning (implicit)
11. 2026-06-15 12:00 FLASH (UNC6508 candidate)
12. 2026-06-15 15:30
13. 2026-06-15 16:00 PM (implicit)
14. 2026-06-15 18:00
15. 2026-06-16 00:00
16. **2026-06-16 06:00 (this sweep)**

~60h continuous clean window. Visibility-limited absence flagged per Hard Rule 8 — not negative evidence.

## Notes for next phase (08:00 morning brief)

**Strong morning brief substrate (NEW this sweep):**

1. **Fortinet FortiSandbox active exploitation** — Defused threat-intel observation 2026-06-16T09:19Z reports active exploitation of CVE-2026-39813 + CVE-2026-39808 + CVE-2026-25089 (all CVSS 9.8 Critical, all unauthenticated network-exploitable, all patched April 14, 2026 via FG-IR-26-112/100/141). BC primary relay. Defused not in source-grade corpus → grader should treat single-source veto applies; A&D-relevance MODERATE-to-HIGH (FortiSandbox commonly deployed in DIB/federal civilian malware-detonation pipelines; unauthenticated RCE on security-detection appliance is significant). Watch for SentinelOne / Help Net A-grade independent corroboration. CISA KEV addition pathway expected 1-to-7-days.

2. **APT37 / ScarCruft NarwhalRAT** — THN primary 2026-06-16T08:14Z relaying Genians Security Center. NarwhalRAT explicitly described as "departure from RokRAT, a malware family exclusively attributed to the hacking group" — genuinely new tooling for tracked roster-#024 actor (MEDIUM threat level, last reviewed 2026-05-10). C2 daehoat[.]com + novel21[.]co.kr; staging %APPDATA%\naverwhale; scheduled task "MicrosoftUserInterfacePicturesUpdateTackMachine". Single-publisher with informal Genians attribution language ("shares multiple similarities") — single-source veto applies. Iran Cyber Watch is NOT triggered; this is roster #024 DPRK / MSS-attributed-per-ESET-via-The-Record actor, would surface under future "DPRK Activity" standing section if/when activated, or as Other Signal in current brief format.

3. **Earth Lusca / Aquatic Panda SprySOCKS Windows variant + UEFI bootkit** — BC primary 2026-06-16T09:00Z relaying ESET (A) WeLiveSecurity. ESET "high confidence" attribution. Earth Lusca NOT on Archimedes 24-actor roster. **Operator-deferred /new-actor candidate surface** — substrate is strong (ESET A1 primary + multi-year activity 2023-2024 + UEFI bootkit capability evolution + 4 named gov-org-target countries Taiwan/Thailand/Pakistan/Honduras). If operator wants to scaffold dossier via `/new-actor Earth-Lusca`, actor-profiler has good first-pass material. Otherwise possible Other Signal item.

4. **Unit 42 Vertex AI Pickle in the Middle** — Unit 42 A2 primary 2026-06-16T10:00Z, CVE not assigned, Google patched March 31 + April 15, 2026, no ITW. Other Signal item for A&D ML/MLOps audiences — A&D-prime ML pipelines on google-cloud-aiplatform 1.139.0-1.140.0 between Feb 2026 and April 15, 2026 patch had exposure window to cross-tenant RCE via pickle deserialization in joblib model files.

**UPDATE candidates carried from 00:00 sweep substrate:**

5. **CVE-2026-20262 Cisco Catalyst SD-WAN Manager** — KEV-listed 2026-06-15 with BOD-22-01 deadline 2026-06-29; finding-2026-06-15-0006 status pivot from "KEV-listing-watch-1-to-7-days" to "KEV-listed-with-BOD-22-01-deadline-2026-06-29"; vuln-tracker-handoff-operator-deferred stands; 8th Cisco SD-WAN KEV add of 2026 per The Register framing.

6. **CVE-2026-54420 LiteSpeed cPanel Plugin** — net-new to corpus, A1 CISA primary, exploited in wild May 2026, patched 2026-06-01 v2.4.8, CISA mitigation deadline 2026-06-18 ~T+58h from this sweep, CVSS 8.5 High, CWE-61. A&D-relevance LOW (not A&D-prime infra; shared-hosting / SMB / CloudLinux+CageFS surface), BOD-22-01 binding on FCEB but A&D-prime DFARS-252.204-7012 flow-down inheritance pattern unclear at this product layer.

7. **KEV retrospective-compliance-metrics cohort phase update** — CVE-2026-35273 PeopleSoft deadline closed EOD 2026-06-15 ~T+30h pre-sweep now retrospective phase joining standing cohort (with CVE-2026-10520 Ivanti Sentry T+44h-past + CVE-2026-0257 PAN-OS ~16d-past).

**Pre-existing carry-forward holds:** UNC6508 72h dedup hold through 2026-06-18 12:00 EDT; Velvet Ant Operation Highland; Anthropic Fable 5/Mythos 5; Handala #014 NEGATIVE binding; Check Point VPN CVE-2026-50751 / Qilin; CVE-2026-20253 Splunk Enterprise vendor confirmation pending; CVE-2026-42824 SearchLeak M365 Copilot Enterprise patched-no-ITW.

## Extraction notes

- Language: en
- Article type: internal sentinel substrate (FLASH sweep marker)
- Raw IOC extraction invoked: no (sentinel marker only; IOC items surfaced in in-window evaluation table are referenced not extracted here — grader will extract on morning-brief promotion)
- Trigger evaluation per `doctrine/FLASH-POLICY.md`: T1 NarwhalRAT path fails A-grade source gate; T1 FortiSandbox path fails A-grade source gate; T2 fails roster gate (Earth Lusca); T3 not exercised (Splunk clean); T4 NarwhalRAT/APT37 fires structurally but operationally inferior to morning brief disposition; T5 Earth Lusca fails on retrospective + non-A&D-prime; T6 no zero-day-without-patch.
- Quiet hours per `doctrine/FLASH-POLICY.md`: ACTIVE (06:00 EDT outside 09:00-21:00). Critical override evaluated 0-of-4 conditions met (no CVSS 10.0 + tracked-actor + named A&D-watchlist victim alignment).
- Anti-noise discipline applied per FLASH-POLICY rule 1 (one FLASH per trigger topic per 24h), rule 2 (B2 minimum grade), rule 4 (weekly FLASH count vigilance).
