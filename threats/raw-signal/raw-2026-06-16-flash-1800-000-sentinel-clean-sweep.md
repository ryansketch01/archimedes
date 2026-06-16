---
raw_id: raw-2026-06-16-flash-1800-000-sentinel-clean-sweep
collected_at: 2026-06-16T18:05:00-04:00
run_id: flash-sweep-20260616-180000
collection_mode: flash_sweep
source:
  source_yaml_id: internal-sentinel
  source_name: Archimedes Internal Sentinel (FLASH sweep)
  source_url: null
  published_at: 2026-06-16T18:00:00-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: []
triage_tags: [sentinel, flash_clean_sweep, non_flash, active_window]
iocs_extracted: false
iocs_count: 0
text_word_count: 1850
promoted: false
ttl_expires_at: 2026-09-14T18:05:00-04:00
---

# 18:00 EDT FLASH sweep — clean sentinel (active window)

## Sweep parameters

- **Window:** 2026-06-16 12:00 EDT to 2026-06-16 18:00 EDT (6h FLASH window since prior sweep at commit `61eac22` sentinel 12:00).
- **Active window:** **ACTIVE** (18:00 EDT is INSIDE 09:00-21:00 EDT). Any triggered FLASH would post directly to `#flash-alerts`. EXIT-SILENT per FLASH-POLICY: a clean sweep produces neither a Discord post nor a flash-queue entry regardless of active-window status. No triggered FLASH this sweep means nothing to post.
- **Trigger evaluation:** 6 FLASH triggers per `doctrine/FLASH-POLICY.md`.
- **Splunk sentinel IOC set:** 19-IOC PeopleSoft/UNC6240 standing set + 9-IOC UNC6508 sub-set + 13-IOC FishMonger SprySOCKS Windows (finding frontmatter held) + 5-IOC APT37 NarwhalRAT (finding frontmatter held).
- **Splunk indexes:** defenseclaw_local + archimedes (sourcetype-filtered to exclude `archimedes:operation` / `archimedes:scheduler` self-telemetry).

## Results

- **candidates_found:** 0
- **triggers_fired:** []
- **Splunk sentinel:** **0 tracked-IOC hits at -6h lookback** across `defenseclaw_local` + `archimedes`, sourcetype-filtered to exclude self-telemetry. This is the **16th consecutive clean sentinel sweep** across the cumulative window (2026-06-13 18:00 EDT through this sweep — ~72h continuous clean window). Per Hard Rule 8, silent Splunk does NOT disconfirm; visibility-limited absence flagged not negative-evidence. Frank is NOT a North American medical research / military health institution running REDCap (UNC6508 victim profile), NOT a Higher-Ed PeopleSoft tenant (UNC6240 victim profile), NOT a LiteSpeed cPanel shared-hosting environment, NOT a Cisco SD-WAN Manager deployment, NOT a FortiSandbox sandboxing-platform deployment, NOT a Rockwell programmable automation controller / FLEX I/O EtherNet/IP fieldbus adapter environment, NOT a California water utility per Cal Water/Handala carry-forward.
- **CISA KEV:** **1 net-new addition in window.** CVE-2026-48907 — Widget Factory Joomla Content Editor improper access control vulnerability allowing upload/execution of PHP code via creation of new editor profiles for unauthenticated users. dateAdded 2026-06-16. dueDate 2026-06-19 (~T+3d). knownRansomwareCampaignUse: Unknown. No CVSS in KEV entry. **Evaluated against FLASH triggers below; non-FLASH-eligible. A&D-relevance LOW (Joomla CMS is consumer/SMB website platform, not A&D-prime infrastructure pattern — same disposition as the LiteSpeed cPanel CVE-2026-54420 KEV-listing from AM brief).** Five most-recent KEV now: CVE-2026-48907 Joomla (2026-06-16 NEW), CVE-2026-54420 LiteSpeed (2026-06-15, mitigation deadline 2026-06-18 ~T+30h carry-forward Other Signal candidate), CVE-2026-20262 Cisco SD-WAN (2026-06-15, BOD-22-01 deadline 2026-06-29 T-13d countdown finding-2026-06-15-0006 UPDATE shipped AM brief 2bde07c), CVE-2026-35273 PeopleSoft (2026-06-12, deadline closed EOD 2026-06-15 retrospective phase), CVE-2026-10520 Ivanti Sentry (2026-06-11, retrospective phase).

## In-window items evaluated and discarded as non-FLASH-eligible

Sources swept (-6h lookback since 12:00 sweep): BleepingComputer, The Hacker News, SecurityWeek, Help Net Security, Security Affairs, CISA all.xml, ESET WeLiveSecurity, Dark Reading, Cisco Talos, Unit 42, Krebs on Security, The Register, plus CISA KEV catalog scan.

- **CVE-2026-48907 Widget Factory Joomla Content Editor KEV-listed 2026-06-16** — CISA KEV A1 government primary. T1 EVAL: no CVSS in KEV entry; no A-grade independent active-exploitation claim beyond KEV listing itself. T3 GATE FAIL: Joomla CMS is consumer/SMB website platform; Widget Factory is a third-party Joomla editor plugin (JCE — JoomlaContentEditor) — A&D-prime tenants typically run enterprise CMS (Drupal/Sitecore/AEM) or custom platforms, NOT shared-hosting Joomla with third-party editor plugins. dueDate 2026-06-19 ~T+3d gives FCEB time to patch. T2/T4 FAIL: no actor attribution from CISA. T5 FAIL: no A&D-prime named victim. T6 FAIL: vendor mitigations available per CISA "Apply mitigations in accordance with vendor instructions." Critical-override 0-of-4 conditions met. — **Discarded as non-FLASH-eligible; possible Other Signal one-liner for 2026-06-17 morning brief under KEV-compliance-cohort-tracking surface; A&D-relevance LOW operational-template only**.
- **Three critical Fortinet sandbox bugs splattered by unknown attackers — The Register relay** — TR relay of Defused-Cyber IR-vendor observation on FortiSandbox three-CVE cluster CVE-2026-25089 + CVE-2026-39813 + CVE-2026-39808. Anti-noise rule 1 BINDING: same trigger-topic already covered in AM brief 2bde07c as finding-2026-06-16-0002 (now strengthened from BC+THN dual-publisher to BC+THN+SA+HNS+TR quintuple-publisher journalistic relay of Defused single-IR-vendor observation; Defused itself remains single-IR-vendor source veto on Defused source layer persists). TR adds Fortinet researcher attribution detail (Loic Pantano for CVE-2026-39813; KPMG Spain's Samuel de Lucas Maroto for CVE-2026-39808). TR also notes Defused observation that exploit for CVE-2026-25089 "appeared to be vibe coded and may be faulty" — consistent with prior SA-Paganini observation. CISA KEV pathway NOT yet listed at this sweep time (~T+24h since AM brief substrate-strengthening expectation); expectation window extends 24-48h further. — **Discarded as anti-noise dedup; substrate-strengthening only on the journalistic-relay layer, not on the IR-vendor source layer; possible PM brief 2026-06-17 morning brief UPDATE candidate if CISA KEV lists or second IR-vendor corroborates**.
- **SprySOCKS Windows Variant Abuses Kernel Drivers to Evade Detection — Dark Reading-Rob Wright** — DR editorial relay of ESET-FishMonger SprySOCKS Windows substrate (WIN_DRV + WIN_PLUS variants attributed to FishMonger China-nexus cluster targeting Honduras/Taiwan/Thailand/Pakistan government/foreign-affairs/technology/telecommunications). Anti-noise rule 1 BINDING: same trigger-topic already covered in AM brief 2bde07c as finding-2026-06-16-0001 + PM brief 8fc1987 UPDATE pivot (BC + THN + DR triple-publisher journalistic relay of ESET primary, single-vendor-on-cluster-identity veto persists pending IR-vendor corroboration from Mandiant/CrowdStrike/Unit-42/MSTIC). DR adds no net-new technical substrate beyond ESET primary. — **Discarded as anti-noise dedup; substrate-strengthening already captured in PM brief UPDATE 8fc1987**.
- **Security Community Slams US Ban on Exporting Mythos, Fable — Dark Reading-Alexander Culafi** — DR coverage of open letter from security community asking US government to reverse export restrictions on Anthropic's Claude Fable 5 and Mythos 5 models. Anti-noise rule 1 BINDING: same trigger-topic already covered in PM brief 580af3f as finding-2026-06-15-0010 + carry-forward through AM brief 2bde07c + PM brief 8fc1987. DR coverage is editorial/policy framing (security community pushback), not net-new substrate on the export-control policy itself. T2/T4 FAIL: no actor attribution. T5 marginal: USG export-control policy affects A&D-prime AI procurement decisions broadly but no specific A&D-prime victim. T1/T3/T6 FAIL. — **Discarded as anti-noise dedup; possible Other Signal one-liner for 2026-06-17 morning brief if DR coverage of community pushback warrants a status-pivot UPDATE on finding-2026-06-15-0010**.
- **Google Vertex AI SDK Flaw Let Attackers Hijack Model Uploads via Bucket Squatting — Pickle in the Middle — THN relay of Unit 42** — Unit 42 published "Pickle in the Middle" via Palo Alto bug bounty; Unit 42 explicitly states they saw "no exploitation in the wild." T6 FAIL: patched by Google; no zero-day-without-patch. T1 FAIL: no CVSS disclosed in THN summary; no active exploitation. T2/T4 FAIL: no actor attribution. T5 marginal: Google Vertex AI is CSP-managed ML platform; A&D-relevance via ML/MLOps integration in defense-prime tenants pickle-deserialization-pattern broadly applicable to ML-pipeline supply-chain. Critical-override 0-of-4 conditions met. — **Discarded as non-FLASH-eligible; possible Other Signal one-liner for 2026-06-17 morning brief for A&D ML/MLOps operational template; carry-forward from 2026-06-16 06:00 FLASH sweep evaluation 2a90e4f also non-FLASH-eligible same disposition**.
- **ClickFix Campaigns Expand Malware Delivery With New Loaders and Fake Update Lures — THN** — Multiple ClickFix campaigns delivering three malware loaders (BabaDeda Loader, Lorem Ipsum Loader, Potemkin) per independent reports from Morphisec, BlueVoyant, and Huntress. BabaDeda observed April 2026 targeting education and financial organizations. Anti-noise rule 1 BINDING (partial): Lorem Ipsum Loader / BlueVoyant attribution already covered in PM brief 8fc1987 as reject-2026-06-16-0004 (Vice Society/Vanilla Tempest possibly-linked attribution rejected as out-of-A&D-scope, /new-actor candidacies operator-deferred). THN restatement adds BabaDeda (Morphisec) and Potemkin (Huntress) as third and fourth ClickFix variants under same operational TTP umbrella but neither Morphisec-attributed actor nor Huntress-attributed actor named in THN summary. T2/T4 FAIL: no tracked actor (Vice Society/Vanilla Tempest NOT on `_roster.yaml`, BabaDeda + Potemkin attribution not provided in summary). T5 FAIL: education + financial sectors NOT A&D-prime. T1/T6 FAIL. — **Discarded as anti-noise dedup + partial out-of-scope; possible Other Signal one-liner for ClickFix-umbrella TTP-operational-template surface tracking; /new-actor candidacy for Vice Society + Vanilla Tempest stands operator-deferred from PM brief 8fc1987**.
- **iRhythm Hit by Cyberattack, Patient Data Stolen and Ransom Demanded — Security Affairs-Paganini** — SA-Paganini relay of iRhythm SEC Form 8-K filing dated 2026-06-10. Anti-noise rule 1 BINDING: same trigger-topic already rejected as reject-2026-06-16-0003 in AM brief 2bde07c + SW-Kovacs ransom-demand confirmation discarded in 12:00 FLASH sweep 61eac22. SA-Paganini adds SEC 8-K procedural detail ("On June 9, 2026, iRhythm received an extortion demand from a threat actor claiming to have stolen proprietary data, protected health information, and other personal data") but no actor attribution / no ransomware group claim / no IOCs. T5 FAIL: iRhythm digital-healthcare-cardiac-monitoring NOT A&D/DIB/CMMC/ITAR. T1/T2/T3/T4/T6 FAIL. — **Discarded as anti-noise dedup; same out-of-scope rejection as AM brief reject-2026-06-16-0003**.
- **Malicious JetBrains Marketplace plugins steal AI API keys from developers — BleepingComputer-Lawrence Abrams** — 15 malicious plugins found on JetBrains Marketplace designed to steal AI API keys from developers. T2/T4 FAIL: no actor attribution (commodity supply-chain compromise pattern). T5 FAIL: no A&D-prime named victim; developer-targeted malware. T1/T6 FAIL: no CVE. A&D-relevance: developer-marketplace supply-chain pattern broadly applicable but not direct A&D-prime substrate; consistent with operational-template pattern from prior Hugging Face / npm / PyPI supply-chain compromises. — **Discarded as non-FLASH-eligible; possible Other Signal one-liner for developer-supply-chain operational-template surface tracking**.
- **New Rokarolla Android malware targets 217 banking, crypto apps — BleepingComputer-Bill Toulas + Dark Reading-Elizabeth Montalbano dual-publisher** — Anti-noise rule 1 BINDING: same trigger-topic already covered as discarded item in 12:00 FLASH sweep 61eac22 (THN Zimperium-zLabs primary, 217 banking/crypto apps, 137 remote commands, commodity Android banking trojan, no actor attribution, no A&D-prime victim). BC + DR add publisher relay but no net-new technical substrate beyond Zimperium-zLabs primary. T2/T4/T5 FAIL: no tracked actor / no A&D victim. T1/T6 FAIL. — **Discarded as anti-noise dedup; commodity Android banking trojan out-of-scope**.
- **Steam Workshop abused to spread malware via Wallpaper Engine app — BleepingComputer-Bill Toulas** — Threat actors abusing Steam Workshop community hub to push malware in wallpaper packages. T2/T4 FAIL: no actor attribution (commodity malvertising pattern). T5 FAIL: gaming platform NOT A&D-prime; consumer-targeted. T1/T6 FAIL: no CVE. — **Discarded as out-of-scope consumer commodity malware**.
- **Fileless Phantom Stealer Targets Browser Credentials — Dark Reading-Jai Vijayan** — In-memory malware infection chain with anti-analysis techniques targeting browser credentials. T2/T4 FAIL: no actor attribution (commodity infostealer pattern). T5 FAIL: no A&D-prime named victim. T1/T6 FAIL: no CVE. Hard Rule 7 watch: credentials radioactive — credential-content not stored, only metadata observation that infostealer family exists. — **Discarded as out-of-scope commodity infostealer**.
- **Python dev saved from disaster by intuition...and AI — The Register** — Long-form feature article on DPRK-linked LinkedIn recruiter social-engineering attack against Python dev Roman Imankulov; AI-vetted code review caught npm prepare-hook backdoor. T2 marginal: TR references "North Korean-linked scammers" generic-pattern attribution but does NOT name specific tracked actor (Lazarus / APT38 / Kimsuky etc.); Hard Rule 2 BINDING — Archimedes does NOT originate DPRK attribution from generic-pattern language. T5 FAIL: Python developer at crypto startup NOT A&D-prime. T1/T6 FAIL: no CVE. T4 marginal: AI-vetted-code-review-defense-pattern operational template worth noting but not actor TTP change. — **Discarded as out-of-scope individual targeting + Hard Rule 2 attribution-not-originated**.

## Soft observations carried not promoted (under-24h skip rule applies)

NOT mutated this sweep:

- **mandiant** feedburner RSS canonical-swap pending (last attempt 2026-06-14 07:31 failure_count 27 stale_since 2026-06-13 + direct cloud.google.com HTML success-pattern entrenched 8+ consecutive successes); RSS not re-attempted this sweep under under-24h-since-stale rule; canonical-swap decision still operator-deferred.
- **proofpoint** /us/threat-insight/blog/feed 5x consecutive 404 soft-pattern fully entrenched; THN relay backstop productive; NOT promoted to stale without operator approval.
- **sophos** top-level news.sophos.com/en-us/feed/ stale-persistent since 2026-05-17 replacement candidate news.sophos.com/en-us/category/threat-research/feed/ standing from 2026-06-14 PM sweep pending operator decision.
- **Dark Reading** rss.xml 200 OK this sweep + 200 OK in 12:00 + 06:00 + 00:00 sweeps; recovery-persistence cumulative ~24h cumulative pattern firmly transient; operator review of canonical RSS path closed.
- **msrc** stale_since 2026-05-30 long-stale; MSRC content reaches corpus via SA/TR/SW relays.
- **WeLiveSecurity** ESET RSS 100 items total in feed, 0 items in 6h window — normal multi-day cadence pattern; ESET-FishMonger primary already substrate of finding-2026-06-16-0001.
- **Talos Blog** 15 items total in feed, 0 items in 6h window — normal multi-day cadence.
- **Krebs on Security** 10 items total in feed, 0 items in 6h window — last_modified 2026-06-11T17:38 UTC ~5d stale ESES single-author publication cadence.
- **SecurityWeek** 10 items total in feed, 0 items in 6h window — last_modified 2026-06-16T17:46 UTC ~15min pre-sweep no in-window content beyond AM/PM brief substrate.
- **Help Net Security** 10 items total in feed, 0 items in 6h window — last_modified 2026-06-16T15:27 UTC ~2.5h pre-sweep.
- **Unit 42** feedburner 15 items total in feed, 0 items in 6h window — last_modified 2026-06-16T10:34 UTC pre-window.

## Anti-noise holds carried verbatim

- UNC6508/INFINITERED PRC-nexus medical/military-health/AI/UAS research espionage — 72h FLASH dedup through 2026-06-18 12:00 EDT from FLASH-1200 `c48f6fc` — T-42h remaining, zero net-new restatement this window.
- CVE-2026-35273 PeopleSoft FCEB BOD 26-04 deadline closed EOD 2026-06-15 retrospective-compliance-metrics phase.
- CVE-2026-10520 Ivanti Sentry retrospective compliance-metrics phase deadline 2026-06-14 closed.
- CVE-2026-0257 PAN-OS retrospective compliance-metrics phase deadline 2026-06-01 15d+ past, finding-2026-06-15-0004 PM substrate.
- CVE-2026-20253 Splunk Enterprise HOLD vendor confirmation pending.
- Fable 5/Mythos 5 Anthropic USG export-control finding-2026-06-15-0010 PM substrate (DR-Culafi PM substrate-strengthening this sweep on community-pushback layer, possible PM brief Other Signal one-liner candidate for 2026-06-17 morning).
- Velvet Ant Operation Highland Sygnia primary finding-2026-06-15-0007 carry-forward PM.
- Handala #014/Cal Water Iran Cyber Watch third-source NEGATIVE binding stands from 2026-06-13 PM, REINFORCED in PM brief 8fc1987 by Cal Water response statement 2026-06-16 SecurityWeek-Kovacs primary; status pivot already captured in PM brief 8fc1987 Other Signal note; Handala #014 dossier handoff next_review_due 2026-04-25 ~52d past operator-deferred.
- Check Point VPN CVE-2026-50751 / Qilin.
- CVE-2026-20262 Cisco Catalyst SD-WAN Manager vManage KEV-listed 2026-06-15, BOD-22-01 deadline 2026-06-29 T-13d countdown finding-2026-06-15-0006 status pivot UPDATE shipped in AM brief 2bde07c.
- CVE-2026-42824 SearchLeak M365 Copilot Enterprise patched-no-ITW finding-2026-06-15-0011 vuln-tracker-handoff operator-deferred.
- CVE-2026-54420 LiteSpeed cPanel Plugin KEV-listed 2026-06-15 mitigation deadline 2026-06-18 ~T+30h A&D-relevance LOW rejected AM as reject-2026-06-16-0001.
- CVE-2026-48907 Widget Factory Joomla Content Editor KEV-listed 2026-06-16 dueDate 2026-06-19 ~T+3d A&D-relevance LOW similar disposition pattern to CVE-2026-54420 — Other Signal one-liner candidate for 2026-06-17 morning brief.
- CVE-2026-25089 + CVE-2026-39813 + CVE-2026-39808 FortiSandbox 3-CVE cluster — covered in AM brief 2bde07c finding-2026-06-16-0002; this sweep adds TR relay (5th publisher); CISA KEV pathway NOT yet listed; expectation window extends 24-48h further.
- ESET FishMonger SprySOCKS Windows — covered in AM brief 2bde07c finding-2026-06-16-0001 + PM brief 8fc1987 UPDATE pivot (BC+THN+DR triple-publisher); single-vendor-on-cluster-identity veto persists.
- Genians APT37 NarwhalRAT — covered in AM brief 2bde07c finding-2026-06-16-0003.
- Symantec DragonForce Backdoor.Turn Teams TURN-relay — covered in AM brief 2bde07c finding-2026-06-16-0004 + PM substrate-strengthening BC+HNS dual-publisher; single-vendor-on-novel-TTP veto persists; Scattered-Spider/DragonForce linkage Hard Rule 2 BINDING.
- CISA Rockwell PSIRT five-advisory ICS cluster (ICSA-26-167-01 through -05, six CVEs) — covered in PM brief 8fc1987 finding-2026-06-16-0005.
- BlueVoyant ClickFix Vice Society/Vanilla Tempest — rejected PM brief 8fc1987 as reject-2026-06-16-0004; THN-restatement this sweep adds BabaDeda + Potemkin variants but no actor attribution shift; /new-actor candidacies operator-deferred.

## FLASH-POLICY application

- Active window 09:00-21:00 EDT: 18:00 EDT is **INSIDE** the active window.
- EXIT-SILENT per FLASH-POLICY: clean sweep produces neither a Discord post nor a flash-queue entry regardless of active-window status; only triggered FLASHes during active window post directly to `#flash-alerts` and only triggered FLASHes during quiet hours queue. No triggered FLASH this sweep means nothing to post or queue.
- Critical-override (4 conditions: CVSS 10.0 + active exploitation + tracked actor + A&D watchlist target): 0-of-4 conditions met; no candidate in window.
- Anti-noise rule 1 (one FLASH per trigger-topic per 24h): no in-window items overlap with a separate prior FLASH topic.
- Anti-noise rule 2 (B2 minimum grade): no in-window items met B2 minimum on FLASH-eligible content.
- Anti-noise rule 3 (red-team review for WEP ≥ "very likely"): no FLASH candidates generated.

## Source-health changes

None this sweep. All sources queried returned expected outcomes:

- **bleepingcomputer** 200 OK last_modified 2026-06-16T21:54 UTC (active feed-server activity inside window).
- **thn** 200 OK last_modified 2026-06-16T21:09 UTC (active feed-server activity inside window).
- **securityweek** 200 OK last_modified 2026-06-16T17:46 UTC.
- **helpnetsecurity** 200 OK last_modified 2026-06-16T15:27 UTC.
- **securityaffairs** 200 OK last_modified 2026-06-16T19:19 UTC.
- **cisa-advisories** (all.xml) 200 OK 30 items total, 0 in-window.
- **cisa-kev** 200 OK 1 net-new addition (CVE-2026-48907) evaluated above.
- **welivesecurity** 200 OK 100 items total, 0 in-window.
- **darkreading** rss.xml 200 OK last_modified 2026-06-16T22:01 UTC recovery-persistence confirmed cumulative ~24h.
- **talos** 200 OK 15 items total, 0 in-window.
- **unit42** 200 OK 15 items total, 0 in-window.
- **krebs** 200 OK 10 items total, 0 in-window (last_modified 2026-06-11 pre-window).
- **theregister** 200 OK 50 items total, 2 in-window (Python dev DPRK + Fortinet TR relay both evaluated above).

## Notes for next phase (00:00 EDT 2026-06-17 FLASH sweep — T+6h from this sweep)

- CISA KEV CVE-2026-48907 Widget Factory Joomla Content Editor — possible Other Signal one-liner for 2026-06-17 morning brief under KEV-compliance-cohort-tracking surface; A&D-relevance LOW.
- FortiSandbox 3-CVE cluster CISA KEV pathway expected within next 24-48h window; if KEV-listed by 06:00 sweep would close substrate-strengthening watch on finding-2026-06-16-0002 with UPDATE candidate for 06:00 morning brief.
- Fable 5/Mythos 5 export-control DR-Culafi PM substrate-strengthening on community-pushback layer — possible Other Signal one-liner for 2026-06-17 morning brief finding-2026-06-15-0010 carry-forward.
- ClickFix multi-loader umbrella (BabaDeda + Lorem Ipsum + Potemkin per Morphisec + BlueVoyant + Huntress) — watch-pattern for any actor attribution clearing _roster.yaml 24-actor cohort; substrate-pending Other Signal candidate.
- Standing Splunk sentinel cohort cumulative clean window now ~72h continuous; 16-consecutive-sweep clean streak; visibility-limited absence flagged not negative-evidence per Hard Rule 8.
- KEV retrospective-compliance-metrics phase cohort unchanged: CVE-2026-35273 PeopleSoft + CVE-2026-10520 Ivanti Sentry + CVE-2026-0257 PAN-OS; incoming countdown CVE-2026-20262 Cisco SD-WAN T-13d to deadline 2026-06-29; CVE-2026-54420 LiteSpeed deadline 2026-06-18 ~T+30h from this sweep; CVE-2026-48907 Joomla deadline 2026-06-19 ~T+3d from this sweep — two simultaneous near-term mitigation-deadline KEVs both A&D-relevance LOW.
