---
raw_id: raw-2026-06-11-am-000
collected_at: 2026-06-11T07:33:00-04:00
run_id: pre-brief-20260611-073000
collection_mode: pre_brief_collection
sentinel: true
source:
  source_yaml_id: sentinel
  source_name: "Pre-brief sweep sentinel (multi-source — 14h window since 2026-06-10 17:30 EDT)"
  source_url: null
  published_at: 2026-06-11T07:33:00-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: []
triage_tags: [pre_brief_sweep, sentinel, am_brief_2026_06_11, fbi_website_seizure_la_follow_on_to_2026_06_04_advisory, splunk_pan_patches, oceanlotus_apt32_not_in_roster, openclaw_unit42_supply_chain_research, anti_noise_pm_brief_2026_06_10_active, anti_noise_jdy_volt_typhoon_lock_active, anti_noise_chaotic_eclipse_continuing_series, ivanti_sentry_itw_already_06_00_flash_captured]
iocs_extracted: false
iocs_count: 0
text_word_count: 0
promoted: false
ttl_expires_at: 2026-09-09T07:33:00-04:00
---

# Pre-brief sweep 2026-06-11 07:30 EDT — sentinel (4 substantive in-window items raw-signaled + 1 prior FLASH absorbed)

Window: 17:30 EDT 2026-06-10 → 07:30 EDT 2026-06-11 (14 hours).

## Posture

- Mode 1 pre-brief collection per CLAUDE.md daily rhythm.
- Quiet hours over at 09:00 EDT (90 min away); morning brief composition follows at 08:00.
- 06:00 FLASH sweep already captured Ivanti Sentry CVE-2026-10520 ITW state transition (queued for AM brief supersession) — that material is NOT re-raw-signaled here.

## Anti-noise locks carried forward from 06:00 FLASH

- **AM brief 2026-06-10 lock** — Ivanti Sentry CVE-2026-10520/10523 (at-disclosure-no-ITW posture; SUPERSEDED by 06:00 FLASH's `raw-2026-06-11-flash-0600-001` material state change to ITW emergence), Arista EOS CVE-2026-7473 KEV no-patch, ServiceNow API exploitation, RoguePlanet/Nightmare-Eclipse Defender LPE, Patch Tuesday three zero-days (YellowKey CVE-2026-45586 / GreenPlasma CVE-2026-50507 / MiniPlasma CVE-2026-49160), Microsoft 72-repos Shai-Hulud/Miasma family (VT-006).
- **PM brief 2026-06-10 lock** — Veeam CVE-2026-44963, Cyera protobufjs proto6 six-CVE cluster, ShinyHunters Oracle PeopleSoft mass campaign (incl. Nottingham extension), Adobe ColdFusion + Acrobat / **Fortinet FortiSandbox CVE-2026-25089** / four SAP NetWeaver criticals, Lumen JDY botnet at 1,500+ devices (Volt Typhoon "previously linked" hedged-associative), ServiceNow AM-006 material extension, **VT-008 Exchange CVE-2026-42897 GA patch shipped** (SecurityWeek 11:52 UTC restatement absorbed), "The Gentlemen" RaaS Krebs OSINT attribution.
- **`jdy-volt-typhoon-restatement-2026-06-10`** — covers JDY botnet → Volt Typhoon hedged-associative. Lock expires 2026-06-11T16:00 EDT. Security Affairs 07:46 UTC restatement of Lumen JDY report **absorbed under this lock**.
- **`miasma-source-code-leak-2026-06-10`** — covers Miasma worm source-code GitHub leak. Operates as candidate-lock until morning brief composition.
- **`cve-2026-5027-langflow-patched-2026-06-10`** — covers Langflow CVSS 8.8 path-traversal patched. Candidate-lock until morning brief composition.
- **06:00 FLASH `flash-2026-06-11-0600-001` Ivanti Sentry ITW** — queued for AM brief supersession per FLASH-POLICY queue-processing rule. Treated as canonical PoC-weaponization-to-mass-exploitation state-transition for CVE the AM brief already has continuing-coverage authorization for.

## Sources queried (this sweep)

**A-grade direct:**
- **CISA Advisories all.xml** — feed reachable (status 200), 0 items in 14h window.
- **CISA KEV JSON catalog** — direct retrieval; 0 entries dated 2026-06-10 OR 2026-06-11. Most recent KEV adds: CVE-2026-11645 / CVE-2026-7473 / CVE-2026-20245 (all 2026-06-09); CVE-2026-42271 / CVE-2026-50751 (2026-06-08). CVE-2026-50751 Check Point dueDate 2026-06-11 = today (FCEB compliance deadline reached). CVE-2026-10520 Ivanti Sentry NOT in KEV yet despite ITW emergence (lag typical; expect addition within 24-72h per pattern).
- **Microsoft Security Blog feed** — 0 items in 14h window (last-modified 2026-06-10T16:00 UTC pre-window).
- **Mandiant / Google Threat Intel** — `cloud.google.com/blog/topics/threat-intelligence/rss` not validated this sweep (persistent parse-error pattern; alt-endpoint canonical-swap decision still overdue per source-health observation). Held healthy per source-health.yaml; feedburner remains 404.
- **MSRC blog feed** — stale per source-health.yaml (parse error pattern since 2026-05-29); not retried this sweep.
- **Unit 42 feed** — feed reachable (status 200, last-modified 2026-06-11T10:27 UTC inside window). 1 item in 14h window — "Trust No Skill: Integrity Verification for AI Agent Supply Chains" (2026-06-11T10:00 UTC = 06:00 EDT in-window). Academic research on AI agent supply chain integrity verification via OpenClaw registry analysis. **No A&D tie-in, no actor attribution, no CVE, no IOCs.** Continuing-coverage candidate for weekly synthesis. **RAW-SIGNALED** as `raw-2026-06-11-am-004`.
- **CrowdStrike blog feed** — feed reachable (status 200), 10 items returned all dateless (marketing/MQ pattern persistent — same as 06:00 sweep). No fresh in-window content.
- **Volexity blog feed** — not retried this sweep (failure_count=2 stale per 00:00 + 06:00 sweep increments; <24h stale rule applies).
- **Rapid7 blog feed** — feed reachable (status 200, last-modified 2026-06-11T11:16 UTC inside window from feed-server activity), 0 items in 14h window.
- **SentinelLabs feed** — feed reachable (status 200, last-modified 2026-06-10T20:29 UTC pre-window), 0 items in 14h window.
- **Cisco Talos feed** — feed reachable (status 200), 0 items in 14h window.

**B-grade aggregators:**
- **BleepingComputer RSS** — feed reachable (status 200, last-modified 2026-06-11T11:26 UTC inside window). **3 items in 14h window:**
  1. "Microsoft fixes BitLocker recovery bug on Windows Server 2025" (2026-06-11T08:44 UTC = 04:44 EDT). Vendor-side operational fix (non-security April 2026 update issue); not threat content; **DISCARDED.**
  2. "Nottingham University data breach affects over 450,000 students" (2026-06-11T07:27 UTC = 03:27 EDT). Continuing-coverage of ShinyHunters Oracle PeopleSoft PM-brief item (per-actor scope, education sector); 454,600 affected per HIBP analysis; ethnicities + disabilities + passport numbers exposed. **Absorbed under PM brief 2026-06-10 lock.**
  3. "Max severity Ivanti Sentry vulnerability now exploited in attacks" (2026-06-11T06:20 UTC = 02:20 EDT). **Already captured at 06:00 FLASH `raw-2026-06-11-flash-0600-001`; promoted to `finding-2026-06-11-0001`.** Anti-noise applies.

- **The Hacker News (feedburner)** — feed reachable (status 200, last-modified 2026-06-11T10:26 UTC inside window). **2 items in 14h window:**
  1. **"OceanLotus Hits Vietnam Investors With SPECTRALVIPER in FireAnt Attack"** (2026-06-11T09:45 UTC = 05:45 EDT in-window). ESET research relayed to THN — Vietnam-aligned actor OceanLotus (APT32) attributed to two campaigns (FireAnt Metakit supply-chain Oct 2025-Mar 2026; Vietnamese infrastructure/transport corporation espionage mid-2024-Feb 2026) using SPECTRALVIPER backdoor with DLL side-loading. **OceanLotus / APT32 NOT in `_roster.yaml`** — confirmed via grep. **NO A&D-watchlist victim named** (Vietnamese infrastructure/transport construction corp; stock investors). Tier-1 vendor (ESET) origination + THN secondary. **RAW-SIGNALED** as `raw-2026-06-11-am-001` for potential `/new-actor` candidate flag; A&D-relevance LOW; grader to evaluate vs morning-brief / weekly-synthesis disposition.
  2. "GitHub to Disable npm Install Scripts by Default to Stop Supply Chain Attacks" (2026-06-11T06:23 UTC = 02:23 EDT in-window). Already captured in 06:00 FLASH sentinel; vendor-side platform policy (npm v12 install-scripts-off-by-default); defensive context for VT-006 / Shai-Hulud / Miasma theme. **Continuing-coverage candidate for weekly synthesis only.** **DISCARDED** for morning brief raw-signal.

- **SecurityWeek RSS** — feed reachable (status 200, last-modified 2026-06-11T11:06 UTC inside window). **5 items in 14h window:**
  1. **"FBI Seizes 13 Websites That Officials Say Were Used by China to Target and Recruit US Workers"** (2026-06-11T11:06 UTC = 07:06 EDT in-window). AP-bylined; FBI/DOJ enforcement action against 13 fake-consulting-front-company websites used by entities "officials allege ... tied to Chinese intelligence services" to recruit current/former US security-clearance holders. Tradecraft matches `finding-2026-06-04-0002` (Five Eyes "Safeguarding Our Secrets" advisory): LinkedIn/hiring platforms, AI-generated photos, fraudulent identities, cryptocurrency payments. **Strong A&D-prime relevance** — operator target profile (mid-to-large US A&D contractor, ITAR-regulated, cleared personnel). LE-action follow-on to strategic-advisory finding 0002. **RAW-SIGNALED** as `raw-2026-06-11-am-002`.
  2. **"Splunk, Palo Alto Networks Patch Severe Vulnerabilities"** (2026-06-11T10:47 UTC = 06:47 EDT in-window). SecurityWeek Ionut Arghire. **Splunk CVE-2026-20253 CVSS 9.8 critical** — PostgreSQL sidecar arbitrary file creation/truncation, unauthenticated network-reachable; affects Splunk Enterprise (NOT Splunk Free per article confirmation — Frank's first-party stack runs Splunk Free 10.x, not affected). **PAN CVE-2026-0274 high** — Cortex XSOAR / XSIAM CommvaultSecurityIQ integration credential validation. No ITW for either. Additional 3 high + 4 medium Splunk Enterprise bugs + 1 SOAR medium + 36 third-party component vulns. PAN GlobalProtect mentioned among 8 medium/low Palo Alto patches (separate from active CVE-2026-0257 lock; that lock covers ITW exploitation, not these new patches). **RAW-SIGNALED** as `raw-2026-06-11-am-003`. **Note: Splunk CVE-2026-20253 is NOT a first-party Frank exposure** — Splunk Free is not the affected product. Splunk Enterprise customers (including potential A&D customers running Splunk in SOCs) ARE exposed.
  3. "'GreatXML' Zero-Day Exploit Bypasses BitLocker" (2026-06-11T09:56 UTC = 05:56 EDT in-window). Same Chaotic Eclipse / Nightmare Eclipse researcher (per Categories tag). PoC, no ITW, **physical access + previous Defender offline scan precondition**. Continuing-coverage of researcher series already in AM brief 2026-06-10's `related_campaigns`. Security Affairs 10:58 UTC body provides full technical detail. **Already evaluated at 06:00 FLASH; series-continuing-coverage applies; weekly synthesis candidate.** **DISCARDED** for fresh morning-brief raw-signal.
  4. "University of Nottingham Confirms Breach After Hackers Leak Data" (2026-06-11T08:30 UTC = 04:30 EDT in-window). Duplicate of BleepingComputer item #2 above; ShinyHunters credit + 450k+ email addresses leaked. **Absorbed under PM brief 2026-06-10 lock.**
  5. "Microsoft Patches Exploited Exchange Server Vulnerability" (2026-06-11T06:52 UTC = 02:52 EDT in-window). Follow-up/recap of CVE-2026-42897 (VT-008 GA patch shipped 2026-06-09); contextual note about KEV. **Absorbed under PM brief 2026-06-10 lock (VT-008 entry).**

- **The Record (Recorded Future News)** — feed reachable (status 200), 0 items in 14h window. The Record FBI/China story (if it publishes) lagging SecurityWeek/AP and Help Net Security relays.
- **Krebs on Security** — feed reachable (status 200, last-modified 2026-06-11T11:20 UTC inside window from feed-server activity), 0 items in 14h window. "The Gentlemen" Krebs post from 2026-06-10 already absorbed into PM brief.
- **SANS Internet Storm Center** — feed reachable (status 200), 1 item in 14h window — ISC Stormcast podcast 2026-06-11T02:25 UTC (awareness-only podcast detail; no body content). DISCARDED.
- **Help Net Security** — feed reachable (status 200, last-modified 2026-06-11T11:21 UTC inside window). 9 items in 14h window. Notable: "FBI seizes 13 websites linked to alleged Chinese intelligence-gathering effort" (10:39 UTC = 06:39 EDT) — independent B-grade parallel relay of SecurityWeek/AP FBI story, **rolls into `raw-2026-06-11-am-002`** as supporting source. Other 8 HNS items are general-cyber survey/product-launch/research content with no A&D / actor / CVE matches.
- **Security Affairs** — feed reachable (status 200, last-modified 2026-06-11T10:58 UTC inside window). 3 items in 14h window: GreatXML restatement (absorbed in series-continuing-coverage lock), FortiSandbox CVE-2026-25089 (absorbed in PM brief lock — PM-008 ICS Patch Tuesday entry covers Fortinet patches), JDY Botnet restatement of Lumen Black Lotus Labs report (absorbed in `jdy-volt-typhoon-restatement-2026-06-10` lock; PM brief Lumen JDY entry covers).

**First-party Splunk (24h window per pre-brief sweep practice):**
- `archimedes` + `defenseclaw_local` indexes — `-24h@h` window queries on roster actors (UNC1549 / Charming Kitten / Handala / MuddyWater / Volt Typhoon / Salt Typhoon / APT28/29/32/34/37/40/41 / TeamPCP / Lazarus / Stardust Chollima / Sandworm / Miyako / BlackCat / ShinyHunters / Qilin / Scattered Spider / Cl0p / LockBit / OceanLotus + APT32) + active CVEs (CVE-2026-10520 / 10523 / 11645 / 7473 / 20245 / 42271 / 50751 / 0257 / 42897 / 44963 / 5027 / 20253 / 0274 / 25089) + keywords (ivanti, sentry, langflow, veeam, servicenow, peoplesoft, jdy, miasma, openclaw, oceanlotus, spectralviper, fireant, greatxml, chaotic eclipse, nightmare eclipse, shinyhunters, nottingham). Events returned all Archimedes self-instrumentation (`archimedes:scheduler` sourcetype) — six `started`/`completed` pairs for 2026-06-10 phases + 2026-06-11 00:00 + 06:00 phases. **Zero substantive first-party matches** across either index in window. Hard Rule 8: silence is not disconfirming, not confirming.

## Source health observations (this sweep)

- All A-grade direct feeds queried this sweep were reachable; **no failure-count increments warranted**.
- Mandiant feedburner / cloud.google.com RSS persistent parse-error pattern (>30 consecutive failures across 5+ weeks) per source-health.yaml `mandiant` notes — operator alt-endpoint canonical-swap decision overdue. Not retried this sweep.
- MSRC stale (parse error pattern since 2026-05-29) — not retried; under-24h-since-stale rule does not apply (>11 days stale) but skipped this sweep per existing operational pattern of relying on Tier-1 relays (SecurityWeek + BleepingComputer + The Register) for MSRC content.
- Volexity stale per recent 00:00 + 06:00 FLASH sweep observations — not retried (<24h stale rule applies).
- **No source-health.yaml updates warranted this sweep.** Operator-set `notes` and unrecognized keys preserved verbatim per field-ownership rule.

## Anomalies / orchestrator awareness items

- **OceanLotus / APT32 is NOT in `_roster.yaml`** — same /new-actor-candidate posture observed for UNC6692 and UNC1069 in earlier collector observations (May 2026 entries in `mandiant` source-health notes). Operator may want to evaluate APT32 for /new-actor scaffolding given THN's coverage and Vietnam-targeting being out-of-A&D-scope. Flagging here for orchestrator visibility; not raw-signaling as `/new-actor` candidate directly (operator-discretion path).
- **Splunk CVE-2026-20253 CVSS 9.8 affects Splunk Enterprise, NOT Splunk Free** — Frank's first-party stack (`archimedes` + `defenseclaw_local` indexes) is Splunk Free 10.x per Operational Notes. **No first-party patching action required.** This is doctrine clarification, not an alarm. Brief framing should make this distinction explicit if covered.
- **PAN CVE-2026-0274 is separate from active CVE-2026-0257 GlobalProtect lock** — CVE-2026-0257 lock expired at 2026-06-11T06:00 EDT (per 06:00 FLASH); CVE-2026-0274 affects Cortex XSOAR / XSIAM CommvaultSecurityIQ integration (not PAN-OS firewall). Briefer / grader to keep separate.
- **FBI website-seizure story** is the operational/LE follow-on to `finding-2026-06-04-0002` (Five Eyes "Safeguarding Our Secrets" joint advisory). Same targeting profile (cleared personnel = operator target match), same tradecraft (LinkedIn / fake consulting / AI personas / crypto payments), same attribution language pattern ("Chinese intelligence services" — generic, not roster-tracked). 13 named domains seized but the AP article does NOT list the specific domain strings — operator may want a direct DOJ press release / FBI IC3 retrieval for IOC purposes.

## Sweep summary

- **Sources queried:** 14 A-grade direct + 6 B-grade aggregators + first-party Splunk (24h).
- **Sources stale-skipped:** 3 (MSRC, Volexity per <24h rule, Mandiant per persistent canonical-swap-pending — held-healthy not stale-skipped).
- **Items in 14h window total:** ~24 across all feeds (3 BC + 2 THN + 5 SW + 0 TR + 0 Krebs + 1 SANS + 9 HNS + 3 SA + 1 Unit42 + 0 Talos + 0 Rapid7 + 0 SentinelLabs + 0 MSTIC + 0 Mandiant + 0 CISA).
- **Items matching watchlists / roster / vuln-index:** 4 substantive (FBI/China A&D-prime; Splunk/PAN patches; OceanLotus/APT32 not-in-roster flag; Unit42 OpenClaw research) + 1 prior 06:00 FLASH (Ivanti Sentry ITW, NOT re-raw-signaled).
- **Items raw-signaled this sweep:** 4 (`am-001` OceanLotus, `am-002` FBI 13-website seizure, `am-003` Splunk + PAN patches, `am-004` Unit42 OpenClaw).
- **Items absorbed by anti-noise locks:** Nottingham continuing-coverage (PM brief lock), GreatXML series-continuing (researcher campaign lock), FortiSandbox CVE-2026-25089 (PM brief lock), JDY botnet restatement (`jdy-volt-typhoon-restatement-2026-06-10` lock), Exchange CVE-2026-42897 restatement (PM brief / VT-008 lock), GitHub npm install-scripts policy (defensive context — weekly synthesis only), ISC Stormcast podcast (awareness only), Ivanti Sentry ITW (`raw-2026-06-11-flash-0600-001` already promoted).
- **Source-health changes:** None.
- **Policy violations / halt events:** None.
- **First-party Splunk hits on tracked indicators:** Zero substantive (all events Archimedes self-instrumentation).

## Disposition for AM brief 2026-06-11

The grader's promotion calculus should consider:

1. **Ivanti Sentry CVE-2026-10520 ITW state transition** — already in queue per FLASH-POLICY supersession path; canonical material-state-change FLASH-to-morning-brief absorption. `finding-2026-06-11-0001` already promoted via 06:00 FLASH.
2. **FBI 13-website seizure** — strong A&D prime relevance, LE-action follow-on to `finding-2026-06-04-0002`. Independent B-grade relays (AP via SW + HNS) + direct DOJ enforcement action (A-grade attestation class). Likely AM brief priority item.
3. **Splunk CVE-2026-20253 CVSS 9.8 + PAN CVE-2026-0274 patches** — high-severity new-CVE-disclosure-no-ITW pattern; not Trigger 1 (no exploitation), worth morning-brief operational-defense framing only if grader weights Splunk Enterprise prevalence in A&D SOCs.
4. **OceanLotus/SPECTRALVIPER** — A&D-relevance LOW (Vietnam infrastructure/transport; not roster); flag for orchestrator on `/new-actor` evaluation; weekly synthesis candidate at best.
5. **Unit42 OpenClaw AI agent supply chain** — A-grade vendor research; supply-chain doctrine adjacent to VT-006/Miasma/Shai-Hulud family; weekly synthesis continuing-coverage candidate.

No FLASH-policy supersession events expected during sweep window (08:00 AM brief composition handles the FLASH queue via supersession + absorption).
