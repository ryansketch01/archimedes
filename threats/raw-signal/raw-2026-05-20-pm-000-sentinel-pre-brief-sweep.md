---
raw_id: raw-2026-05-20-pm-000
collected_at: 2026-05-20T15:30:00-04:00
run_id: pre-brief-20260520-153000
collection_mode: pre_brief_collection
test: false
source:
  source_yaml_id: multi
  source_name: "Multi-source pre-brief sweep (15:30 EDT Wednesday)"
  source_url: null
  published_at: null
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: []
triage_tags:
  - sentinel
  - pre_brief_sweep_summary
  - scheduled_1530_window
  - non_promotable
  - 4_items_raw_signaled_pm_001_pm_002_pm_003_pm_004
  - flash_1200_carry_forward_webworm_grafana_already_raw_signaled_in_flash_1200_001_002
  - splunk_first_party_zero_hits_49th_consecutive_dormant_sweep
  - cisa_kev_seven_additions_2026_05_20_microsoft_defender_pair_plus_five_historical
  - cisco_psirt_cve_2026_20223_cvss_10_0_secure_workload_third_cisco_authbypass_2026
  - anthropic_claude_code_sandbox_bypass_silently_patched
  - drupal_psa_2026_05_18_critical_pre_release_developing_event
  - microsoft_rampart_clarity_open_source_ai_red_team_tooling_release_awareness
  - cisa_advisories_all_xml_one_in_window_kev_addition_alert
  - bleepingcomputer_3_substantive_in_window_grafana_already_raw_signaled_drupal_now_pm_004
  - securityweek_5_in_window_3_substantive_yellowkey_anti_noise_anthropic_pm_003
  - the_hacker_news_5_in_window_3_substantive_github_anti_noise_webworm_anti_noise_fox_tempest_anti_noise_rampart_awareness
  - the_record_5_in_window_2_substantive_7_eleven_consumer_breach_discord_e2e
  - mandiant_feedburner_404_carry_forward_known_failure
  - dragos_feed_404_carry_forward
  - msrc_blog_feed_parse_failure_carry_forward
  - cisco_talos_blog_feed_404_carry_forward
  - mstic_one_item_in_window_rampart_clarity_already_in_thn_relay
  - sentinelone_sentinels_league_marketing_only_discarded
  - unit42_zero_in_window
  - rapid7_one_item_in_window_surface_command_marketing
  - krebs_zero_in_window
  - sans_isc_zero_in_window
iocs_extracted: false
iocs_count: 0
text_word_count: 1080
promoted: false
ttl_expires_at: 2026-08-18T15:30:00-04:00
---

# Pre-brief collection sweep — 2026-05-20 15:30 EDT (Wednesday afternoon)

Wednesday afternoon pre-brief collection. Time window: 2026-05-20T07:30
EDT to 2026-05-20T15:30 EDT (8 hours). De-dupe context preserved against
the 06:00 FLASH (TeamPCP GitHub-corp breach), the 07:30 AM pre-brief
(Mini Shai-Hulud @antv 320+ npm + Storm-2949 SSPR + YellowKey mitigation),
and the 12:00 FLASH (Webworm + Grafana TanStack continuation already
raw-signaled at flash-1200-001 + flash-1200-002).

## Sweep outcome

**4 net-new raw-signal files written (pm-001 through pm-004)** plus this
sentinel and carry-forward from the 12:00 FLASH for Webworm and Grafana
(already discrete raw-signal at flash-1200-001 + flash-1200-002).

### Raw-signaled this sweep (4)

1. **raw-2026-05-20-pm-001** — CISA KEV adds 7 entries 2026-05-20:
   CVE-2026-41091 Microsoft Defender EoP CWE-59 link-following + CVE-2026-45498
   Microsoft Defender DoS (fresh 2026 CVEs, no CVSS surfaced yet, no actor
   attribution per CISA, federal dueDate 2026-06-03) PLUS 5 historical
   CVEs (CVE-2008-4250 Conficker/MS08-067, CVE-2009-1537 DirectX,
   CVE-2009-3459 Adobe Acrobat, CVE-2010-0249/0806 Internet Explorer
   UAF). High A&D relevance on the Defender pair (Defender universally
   deployed across A&D Windows endpoint fleets). Trigger 1 evaluation
   candidate pending CVSS surfacing. Vuln-tracker handoff for the
   Defender pair.

2. **raw-2026-05-20-pm-002** — CVE-2026-20223 Cisco Secure Workload
   pre-auth REST API authentication bypass CVSS 10.0 (CWE-306 missing
   authentication for critical function; cross-tenant scope-changed).
   Cisco PSIRT vendor-self-disclosure (procedurally A-grade). Patched
   versions 3.10.8.3 + 4.0.3.17; SaaS already mitigated; on-prem 3.9 and
   earlier require migration. No ITW per PSIRT. Third Cisco-product
   authentication-bypass disclosure tracked in 2026 (after CVE-2026-20182
   SD-WAN + CVE-2026-20093 IMC). Strong vuln-tracker `_index.yaml`
   addition candidate. Direct A&D enterprise relevance (Secure Workload
   is the microsegmentation control plane in A&D data centers, formerly
   Cisco Tetration). Not a FLASH (no ITW + patches available).

3. **raw-2026-05-20-pm-003** — SecurityWeek (Eduard Kovacs) on Anthropic
   silently patching a Claude Code sandbox bypass (SOCKS5 hostname
   null-byte injection against network allowlist) in Claude Code 2.1.88
   on 2026-03-31 without CVE assignment or release-note mention.
   Researcher Aonan Guan (first Archimedes-corpus citation; first-surface
   provisional grade review candidate). Researcher describes prompt
   injection + sandbox-bypass chain for credential/token/env exfil.
   No ITW. Patched 7 weeks before disclosure. Indirect A&D relevance
   (Claude Code in enterprise SDLCs). Archimedes-corpus adjacency to
   raw-2026-05-20-am-001 Mini Shai-Hulud TeamPCP "Claude Code backdoor"
   TTP claim and to Microsoft RAMPART/Clarity release (awareness layer
   only). Not a FLASH.

4. **raw-2026-05-20-pm-004** — BleepingComputer (Bill Toulas) relays
   Drupal Security Team PSA-2026-05-18 announcing a critical Drupal core
   security release for 2026-05-20 17:00-21:00 UTC with "high
   exploitation risk" and "threat actors might develop exploits within
   hours" framing. No CVE / CVSS / vuln class disclosed at the PSA
   timepoint; embargo language preserved. Affected branches 11.3.x /
   11.2.x / 11.1.x / 10.6.x / 10.5.x / 10.4.x current-supported plus
   9.5 / 8.9 EOL hotfixes. Developing event — 18:00 EDT FLASH sweep
   should re-evaluate post-disclosure for Trigger 1 / Trigger 6.

### In-window items DISCARDED per Mode 1 procedure (no watchlist / roster / vuln-index hit) OR anti-noise to existing raw-signal

- **BleepingComputer — Grafana breach caused by missed token rotation
  after TanStack attack** (Bill Toulas, 2026-05-20 11:46 EDT). Already
  raw-signaled at raw-2026-05-20-flash-1200-002. **Anti-noise applies.**

- **The Hacker News — GitHub Breached: Employee Device Hack Led to
  Exfiltration of 3,800+ Internal Repos** (2026-05-20 07:38 EDT). Direct
  duplicate of finding-2026-05-20-FLASH-0001 (already published). **Anti-noise**.

- **The Hacker News — Webworm Deploys EchoCreep and GraphWorm Backdoors
  Using Discord and MS Graph API** (2026-05-20 08:51 EDT). Already
  raw-signaled at raw-2026-05-20-flash-1200-001. **Anti-noise applies.**
  ESET-originating; aerospace sector named at aggregate level but no A&D
  prime; Webworm / FishMonger / Aquatic Panda / SixLittleMonkeys / Space
  Pirates / APT17 cluster aliases NOT in `_roster.yaml`.

- **The Hacker News — Microsoft Takes Down Malware-Signing Service
  Behind Ransomware Attacks** (Microsoft Fox Tempest disruption,
  2026-05-20 10:36 EDT). Fox Tempest already extensively raw-signaled
  via MSTIC primary at raw-2026-05-19-pm-001 + relay raw-2026-05-19-pm-002
  (SecurityWeek) + raw-2026-05-19-pm-003 (The Record). **Anti-noise** —
  THN relay is a within-24h restatement of the MSTIC primary +
  takedown action coverage already absorbed into 2026-05-19 afternoon
  brief 1513d98.

- **SecurityWeek — Microsoft Rolls Out Mitigations for YellowKey
  BitLocker Bypass** (Ionut Arghire, 2026-05-20 11:39 EDT). Already
  raw-signaled at raw-2026-05-20-am-003 (Microsoft mitigation
  publication for CVE-2026-45585 YellowKey). SecurityWeek adds modest
  Will Dormann (Tharros Labs) commentary and Chaotic Eclipse exploit
  framing detail beyond the Microsoft advisory body, but the YellowKey
  topic itself is **anti-noise** to AM-003. The grader / briefer may
  fold the Dormann technical detail into the AM-003 finding context if
  needed.

- **The Hacker News + Microsoft Security Blog — Microsoft RAMPART
  (Pytest agentic AI red-team) + Clarity (sounding board for AI agent
  design) open-source tooling release** (2026-05-20 11:00-13:06 EDT,
  MSTIC byline Ram Shankar Siva Kumar + THN relay). Microsoft defensive
  tooling release — no actor / no IOC / no vuln. Awareness-only,
  industry-wide AI-agent security momentum signal. Tagged in PM-003
  Archimedes-corpus adjacency note. Not raw-signal-worthy as a
  standalone finding-class item.

- **Microsoft Security Blog — Securing the gaming culture of cultures**
  (Aaron Zollman Deputy CISO, 2026-05-20 12:00 EDT). Microsoft Deputy
  CISO blog series on gaming-platform security. No A&D / no actor / no
  vuln. **DISCARDED**.

- **SecurityWeek — 1Password Teams With OpenAI to Stop AI Coding Agents
  From Leaking Credentials** (Kevin Townsend, 2026-05-20 09:34 EDT).
  Industry partnership / product news. No actor / no vuln. **DISCARDED**.

- **SecurityWeek — AI-Powered App Attacks Are Faster, More Frequent and
  Harder to Stop** (Kevin Townsend, 2026-05-20 10:37 EDT). Digital.ai
  vendor threat report. Aggregate sector reporting; no fresh finding.
  **DISCARDED** (briefer-context only).

- **SecurityWeek — Quantum Bridge Raises $8 Million for Quantum-Safe Key
  Distribution Solution** (2026-05-20 11:45 EDT). Cybersecurity funding
  news. **DISCARDED**.

- **The Record — 7-Eleven confirms breach after ShinyHunters claims**
  (2026-05-20 12:05 EDT). Consumer / retail breach; 7-Eleven covered as
  ShinyHunters tertiary actor cluster in afternoon brief 2026-05-19
  1513d98. **Anti-noise / not A&D**.

- **The Record — Discord migrates all users to end-to-end encryption by
  default** (2026-05-20 12:29 EDT). Vendor product change; awareness only.
  **DISCARDED**.

- **The Record — FTC warns 12 major tech firms of violating Take It Down
  Act** (2026-05-20 13:29 EDT). Regulatory enforcement, NCII intimate
  imagery context. **DISCARDED** (not A&D / not threat-intel).

- **The Record — Ukraine probes teen suspect in cyber theft scheme
  targeting California online shoppers** (2026-05-20 12:33 EDT).
  E-commerce fraud LE coordination. **DISCARDED** (not A&D / not
  finding-class).

- **The Record — Texas, Florida top list of states reporting millions of
  dollars lost through crypto ATMs** (2026-05-20 09:04 EDT). Consumer
  fraud reporting. **DISCARDED**.

- **SentinelOne — Sentinels League 2026: Live Rankings for the Threat
  Hunting World Championship** (SentinelOne, 2026-05-20 09:00 EDT).
  Marketing post. **DISCARDED**.

- **Rapid7 — Operationalizing CTEM Faster: Build Surface Command
  Dashboards in Minutes** (Ed Montgomery, 2026-05-20 08:15 EDT). Product
  marketing post. **DISCARDED**.

- **NVD lastModified Critical window query 2026-05-20T15:30 → 19:30 UTC
  (CVSS Critical):** CVE-2026-43995 Flowise SSRF 9.8 (patched 3.1.0,
  CWE-918, no ITW, no A&D — DISCARDED); CVE-2026-24206 + 24213 + 24214
  NVIDIA Triton Inference Server cluster (CVSS 9.8 each, patched
  v26.03, no ITW per NVIDIA security advisory, no A&D-prime named —
  DISCARDED but the NVIDIA Triton inference server is a recognized
  ML-infrastructure product so the grader may want to track for the
  AI/agentic-cluster context); CVE-2025-31973 HCL BigFix Service
  Management 9.8 (outdated base image, no ITW, no A&D — DISCARDED).
  ONE in-window NVD Critical raw-signaled separately: CVE-2026-20223
  Cisco Secure Workload (pm-002).

- **CrowdStrike feed** — 10 items all `published: null`, marketing/MQ
  content (Falcon AIDR, CORDIAL+SNARKY SPIDER Falcon Shield, Magic
  Quadrant CTI Leader, Falcon OverWatch for Defender). 16th consecutive
  sweep with this pattern. **DISCARDED**.

- **Sophos News, WeLiveSecurity, Unit 42, SANS ISC, Krebs, Recorded
  Future** — 0 items in 8h window each. **No fresh content**.

### Source-health observations

**Sources with NEW failures this sweep:** None. All previously-failed
sources continue with carry-forward known-failure patterns.

**Sources with PERSISTENT carry-forward failures (no source-health
change required):**

- Mandiant `feeds.feedburner.com/Mandiant` — 404 carry-forward (~22nd
  consecutive failure on the feedburner endpoint; cloud.google.com
  index-page WebFetch path remains the productive alternative). Operator
  alt-endpoint decision still pending.
- Dragos `dragos.com/blog/feed/` — carry-forward (failure_count=1; below
  ≥2 stale threshold; multi-day publication cadence pattern continues).
- Cisco Talos `blog.talosintelligence.com/feeds/posts/default` — 404
  carry-forward (failure_count=2 from this morning's pre-brief sweep
  per source-grades.yaml notes; held healthy per operator instruction;
  alt-endpoint decision still pending).
- MSRC blog feed — XML parse failure carry-forward.
- Wiz.io blog feed `/blog/feed.xml` — 404 (collector's first
  observation on this endpoint this sweep; not yet a tracked failure
  pattern in source-health.yaml — collector flags for source-health
  first-entry addition at next runtime-update pass).
- Socket.dev blog feed `/blog/rss.xml` — 404 (collector's first
  observation; same socket source from source-health.yaml — first-entry
  failure recorded at 2026-05-16 07:30, this sweep adds a confirming
  observation).
- Industrial Cyber `industrialcyber.co/feed/` — 403 carry-forward
  (WAF/Akamai bot-block pattern continues from prior sweeps).
- Symantec `security.com/threat-intelligence/feed` — 404 carry-forward.

**Sources with successful in-window fetches:**

- BleepingComputer (3 items in 8h window, all 3 substantive — grafana
  anti-noise; Drupal PSA = pm-004; Specops sponsored = filtered)
- SecurityWeek (5 items in 8h window, 3 substantive — YellowKey relay
  anti-noise; Anthropic = pm-003; Quantum Bridge = filtered; AI-Powered
  App Attacks = filtered; 1Password = filtered)
- The Hacker News (5 items in 8h window, 0 substantive net-new — all
  relays / anti-noise / awareness)
- The Record (5 items in 8h window, 0 substantive A&D-class — consumer
  / regulatory / vendor product news)
- Microsoft Security Blog (2 items in 8h window — both awareness, both
  filtered)
- CISA all.xml (1 item in 8h window — KEV addition alert, pm-001)
- CISA KEV JSON (7 new entries — pm-001)
- NVD lastMod Critical (6 in-window Criticals — 1 raw-signaled, 5
  discarded)
- Rapid7 (1 item in window, marketing-filtered)
- SentinelOne (1 item in window, marketing-filtered)
- CrowdStrike (10 items dateless, marketing-filtered)
- Krebs, Sophos, WeLiveSecurity, Unit 42, SANS ISC, Recorded Future
  (0 items in window each — reachable)

## Splunk first-party check (Hard Rule 8)

Targeted IOC keyword sweep across `archimedes` + `defenseclaw_local`
indexes over -24h on CVE-2026-20223, Cisco Secure Workload, CVE-2026-41091,
CVE-2026-45498, Microsoft Defender, Webworm, EchoCreep, GraphWorm,
Fox Tempest, Drupal, PSA-2026-05-18, TeamPCP, Grafana, TanStack, Claude
Code: 4 hits — ALL `archimedes:operation` pipeline self-references from
this morning's TeamPCP / GitHub FLASH cycle (git_committed, flash_queued,
analyst_review_completed, finding_promoted). Zero non-Archimedes-internal
events.

NOT sourcetype=archimedes:* combined-index query over -24h: zero events.

**49th consecutive sweep with dormant non-self-telemetry stream
pattern.** Trigger 3 cannot fire.

## FLASH-trigger evaluation across all in-window items

- **Trigger 1 (critical CVE + active exploitation + A-grade):** CISA KEV
  +7 batch IS A-grade authority on active-exploitation status, but the
  two fresh 2026 Defender CVEs have no CVSS surfaced yet (NVD Awaiting
  Analysis; MSRC page returns header-only via WebFetch this sweep), so
  `cvss >= 9.0` is unverifiable. Five historical CVEs are KEV-routine
  and not standalone FLASH-worthy. Drupal PSA pre-disclosure has no CVE
  / CVSS / class published. **Does not fire** at the collector tier;
  grader may apply different judgment if MSRC publishes CVSS within
  brief composition window.
- **Trigger 2 (new attribution for tracked actor):** No new attribution
  for any tracked actor in window. (Webworm — China-aligned cluster —
  NOT in `_roster.yaml`; Fox Tempest NOT in `_roster.yaml`; both are
  anti-noise to earlier raw-signal.) Does not fire.
- **Trigger 3 (first-party Splunk IOC hit):** Dormant. Does not fire.
- **Trigger 4 (tracked actor TTP change):** TeamPCP TTP delta on
  Grafana / TanStack continuation is anti-noise to the 06:00 FLASH and
  the 12:00 FLASH absorption layer. Does not fire as a NEW Trigger 4
  surface.
- **Trigger 5 (A&D-sector multi-victim active campaign):** No A&D-prime
  victim named in any in-window surface. Does not fire.
- **Trigger 6 (zero-day no patch + CVSS≥8.0 + exploitation
  confirmed/imminent):** CVE-2026-20223 Cisco Secure Workload patched
  (3.10.8.3, 4.0.3.17; SaaS already mitigated). YellowKey CVSS 6.8
  below floor. Drupal PSA is pre-disclosure; patches scheduled
  17:00-21:00 UTC today. **Does not fire** at the collector tier.

**Pre-brief disposition: no fresh FLASH from this sweep. The 06:00 FLASH
on TeamPCP/GitHub-corp breach remains the published FLASH of the day
(queued-then-superseded by morning brief). 18:00 EDT FLASH sweep
inherits Drupal PSA-2026-05-18 as a post-disclosure re-evaluation
trigger candidate (Trigger 1 + Trigger 6).**

## Disposition

Sentinel file written for audit-trail completeness. 4 raw-signal items
handed off to grader for the 16:00 afternoon brief. Source-health.yaml
runtime fields will be updated to reflect last_successful_fetch on the
productive sources (cisa-advisories, cisa-kev, nvd, bleepingcomputer,
securityweek, thehackernews, the-record, mstic, rapid7, sentinelone,
krebs). No new failures introduced this sweep.
