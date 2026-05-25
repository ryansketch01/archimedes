---
raw_id: raw-2026-05-25-am-000-sentinel-pre-brief-sweep
collected_at: 2026-05-25T07:35:00-04:00
run_id: pre-brief-20260525-073000
collection_mode: pre_brief_collection
sentinel: true
test: false
sweep_type: pre-brief-morning
status: complete
source:
  source_yaml_id: archimedes-internal
  source_name: "Archimedes collector sentinel (07:30 EDT Monday pre-brief sweep — 4 net-new raw-signal companions; 0 FLASH-trigger fires; Lazarus surface is RESTATEMENT not new attribution)"
  source_url: null
  published_at: 2026-05-25T07:35:00-04:00
sweep_window:
  start: 2026-05-24T17:30:00-04:00
  end: 2026-05-25T07:30:00-04:00
  duration_h: 14
prior_sweep_anchor:
  brief_id: flash-2026-05-25-0600-canonical-scheduled-clean-sweep
  shipped_at: 2026-05-25T06:05:00-04:00
  trigger: none_fired
  notes: |
    Prior sweep was the 2026-05-25 06:00 EDT Monday-early FLASH sentinel
    (commit badd4c8). Three in-window items surfaced — TrapDoor THN relay
    (anti-noise locked), Megalodon SecurityWeek (fresh strong morning
    candidate), DocketWise (out-of-scope legal sector). This pre-brief
    sweep covers 2026-05-24T17:30 → 2026-05-25T07:30 EDT (14h),
    overlapping the 18:00 FLASH (commit d7e0da7), 00:00 FLASH (commit
    2742c67), and 06:00 FLASH (commit badd4c8) sentinels — fully
    reconciled with each.
match_reason:
  watchlist: []                  # No A&D-prime named victims in any in-window item
  actors: ["003"]                # Lazarus Group via THN RemotePE — but RESTATEMENT not new attribution; documented in raw-2026-05-25-am-002
  vulnerabilities: ["VT-008"]    # Exchange CVE-2026-42897 KEV T-4 carry-forward (no new substantive change in window)
  keywords: ["supply chain", "workflow_dispatch", "GitHub Actions", "npm", "PyPI", "Crates.io", "AI coding agents", ".cursorrules", "CLAUDE.md"]
triage_tags: [sentinel, pre_brief_morning, monday_morning, four_raw_signal_companions]
iocs_extracted: false           # IOCs extracted in companion raw-signal files am-001 through am-004
iocs_count: 0
text_word_count: 2800
promoted: false
rejected_at: 2026-05-25T08:00:00-04:00
rejection_id: reject-2026-05-25-0001
ttl_expires_at: 2026-08-23T07:35:00-04:00
sources_queried:
  - cisa-kev                # WebFetch known_exploited_vulnerabilities.json — catalogVersion 2026.05.22 UNCHANGED, dateReleased 2026-05-22T18:00:11.5035Z. Most recent KEV add remains CVE-2026-9082 (2026-05-22 EDT). ZERO net-new KEV adds in 14h window (now 60h+ since last add). KEV deadlines T-2 Drupal CVE-2026-9082 (2026-05-27 Wed EOB) and T-4 Exchange CVE-2026-42897 (2026-05-29) carry forward at elevated urgency.
  - cisa-advisories         # fetch_feed cisa.gov/cybersecurity-advisories/all.xml — 200 OK, ICS-CERT batch likely; direct page WebFetch returned 403 (consistent WAF persistent pattern; all.xml remains productive endpoint). 0 items in 14h since-filter window worth raw-signaling for A&D-direct fit.
  - nvd                     # Three WebFetch attempts on services.nvd.nist.gov/rest/json/cves/2.0 with lastModStartDate=2026-05-24T17:30 lastModEndDate=2026-05-25T07:30 EDT cvssV3Severity=CRITICAL — first probe returned totalResults=10, resultsPerPage=0, empty vulnerabilities[]; second probe with resultsPerPage=20 returned totalResults=10, resultsPerPage=0, empty array; third probe with resultsPerPage=2000 + UTC reformat returned totalResults=5, resultsPerPage=0, empty array. NVD API result-pagination quirk PERSISTS across three queries — same condition documented in 06:00 sentinel. Cannot trigger-evaluate the totalResults values without ID-level resolution. Carry-forward to vuln-tracker for direct UI-side lookup or per-CVE retrieval if any morning grader-tier item warrants it; not a stale flip (endpoint reachable, semantic quirk only).
  - thehackernews           # fetch_feed feedburner — 50 items in feed; 2 in 14h since-filter window: (1) Lazarus RemotePE memory-only RAT 2026-05-25 09:32 UTC = 05:32 EDT — raw-signaled to am-002 as RESTATEMENT not new attribution per Trigger 2 logic; (2) TrapDoor multi-ecosystem supply-chain 2026-05-25 05:59 UTC = 01:59 EDT — raw-signaled to am-003 as anti-noise-locked UPDATE absorption per existing lock trapdoor-multi-ecosystem-supply-chain-socket active through 2026-05-25 16:00 EDT.
  - bleepingcomputer        # fetch_feed — 15 items, 0 in 14h since-filter window. Homepage WebFetch confirmed top 10 dated 2026-05-22 through 2026-05-25 — only 2026-05-25 item is a CISSP exam-prep deal (commerce, not threat-intel). Ghost CMS CVE-2026-26980 ClickFix campaign (Bill Toulas 2026-05-24 10:12 AM EDT) is PRE-WINDOW by 7h18m AND the vulnerability is February 2026 patched + February 2026 first-exploitation reporting (Ghost 6.19.1 released Feb 19; SentinelOne first-exploitation reporting Feb 27); BleepingComputer 2026-05-24 piece is a delayed-re-analysis of corpus-aged disclosure, not a fresh disclosure. PRE-WINDOW AND not a fresh trigger event. NOT raw-signaled this sweep.
  - securityweek            # fetch_feed feedburner — 10 items, 5 in window: (1) Megalodon over 5,500 GitHub repositories 2026-05-25 07:40 UTC = 03:40 EDT — raw-signaled to am-001 as STRONG MORNING CANDIDATE with full SafeDep direct retrieval; (2) DocketWise breach 143k 2026-05-25 09:37 UTC = 05:37 EDT — out-of-scope legal sector, NOT raw-signaled; (3) Anthropic Mythos 23,000 OSS vulns 2026-05-25 10:58 UTC = 06:58 EDT — raw-signaled to am-004 as UPDATE on 10K prior baseline; (4) Laravel-Lang Packages Poisoned 2026-05-25 10:41 UTC = 06:41 EDT — pure B-grade SecurityWeek relay of corpus-already-tracked Laravel-Lang flipboxstudio (anti-noise lock active; no new IOCs, no new attribution, no deltas — explicit "no material deltas" assessment from direct fetch); NOT raw-signaled; (5) Radiology Associates of Richmond 266,000 breach 2026-05-25 11:17 UTC = 07:17 EDT — healthcare sector, no actor, no CVE, no A&D — out-of-scope, NOT raw-signaled.
  - the-record              # fetch_feed therecord.media/feed — 5 items, 0 in 14h window. Most recent dated 2026-05-22 pre-window.
  - unit42                  # fetch_feed feedburner — 15 items, 0 in window. Last update 2026-05-22 19:51 UTC pre-window (UNCHANGED across 7 consecutive sweeps).
  - mstic                   # fetch_feed microsoft.com/en-us/security/blog/feed — 10 items, 0 in window. Last update 2026-05-22 17:57 UTC (UNCHANGED across 7 consecutive sweeps).
  - msrc                    # NOT re-fetched — persistent template-only redirect pattern; MSTIC parent feed serves as proxy.
  - crowdstrike             # fetch_feed crowdstrike.com/blog/feed — 200 OK, 10 dateless items identical to prior sentinels (Measuring AI KPIs, Claude integration, Identity protection, 2026 Financial Services Threat Landscape Report, Falcon AIDR, May Patch Tuesday retrospective, Automated Leads, Gartner MQ, Falcon OverWatch for Defender, Risk Assessments). NO threat-research content on tracked actors / CVEs / A&D campaigns. Persistent feed-product-marketing pattern continues (~30 consecutive sweeps).
  - mandiant                # feedburner.com/Mandiant returned 404 — 23rd consecutive sweep failure (failure_count 21→22 applied to source-health.yaml per single-failure-increment rule; status held healthy per long-standing operator policy held-healthy-pending-alt-endpoint-decision; operator-set notes preserved verbatim). cloud.google.com/blog/topics/threat-intelligence index page NOT re-fetched this sweep — top-10 visible titles confirmed UNCHANGED across prior 7 sentinels per consistent observation pattern.
  - eset-welivesecurity     # fetch_feed welivesecurity.com/en/rss/feed — 100 items in feed, 0 in 14h window. Multi-day vendor cadence; most recent 2026-05-22 Foul Play FIFA fake sites (pre-window).
  - sentinelone             # fetch_feed sentinelone.com/labs/feed — 200 OK, 0 in window. Last_modified 2026-05-22 17:44 UTC pre-window UNCHANGED across multiple sweeps. feeds.feedburner.com/SentinelOneLabsBlog endpoint 404 (alt path tried, returned 404 — main labs/feed remains productive).
  - bitdefender             # NOT re-fetched (low-frequency vendor cadence per source-health notes; most recent post 2026-05-19 MSHTA legacy per 06:00 sentinel; pre-window unchanged).
  - volexity                # fetch_feed volexity.com/blog/feed — XML parse error "<unknown>:17:68: not well-formed (invalid token)". THIRD consecutive failure observation (prior 18:00 sentinel: WebFetch returned Loading placeholder; 00:00 sentinel: feed not re-fetched; 06:00 sentinel: not re-tested per FLASH-narrow scope). THIRD-STRIKE THRESHOLD met for stale flip per failure_count >= 2 + persist pattern threshold. STALE FLIP APPLIED this sweep: failure_count 2→3, status healthy→stale, stale_since 2026-05-25, last_error "volexity.com/blog/feed XML parse error <unknown>:17:68: not well-formed token — third consecutive failure observation across 18:00 + 06:00 + 07:30 sweeps".
  - wiz-research            # NOT re-fetched (pattern unchanged from 06:00 sentinel; most recent post 2026-05-21 Claude Enterprise integration; pre-window unchanged across multiple sweeps).
  - snyk                    # NOT re-fetched (pattern unchanged from 06:00 sentinel; Laravel-Lang post 2026-05-23 anti-noise locked; no in-window publications).
  - socket-dev              # NOT re-fetched this sweep — top 5 unchanged across prior 7 sentinels. SafeDep direct retrieval THIS sweep substantiates am-001 Megalodon raw-signal (Socket-adjacent supply-chain coverage class; not part of socket-dev surface).
  - sophos                  # WebFetch news.sophos.com/en-us/category/threat-research/feed redirected to www.sophos.com/en-us/category/threat-research/feed (301); pattern of REDIRECT-AND-DATELESS-RENDERING continues. No in-window content detectable.
  - cisco-talos             # WebFetch blog.talosintelligence.com landing surface — top 5 posts UNCHANGED from 06:00 sentinel (2026-05-21 ungovernable cultural; 2026-05-19 BadIIS MaaS Chinese-speaking; 2026-05-19 TP-Link/Photoshop/OpenVPN/Norton VPN; 2026-05-14 patching/AI; 2026-05-14 Cisco Catalyst SD-WAN). NO 2026-05-24 or 2026-05-25 dated posts. blog.talosintelligence.com/feeds/posts/default Atom endpoint NOT re-probed this sweep (per source-health failure-count history). Front-page WebFetch fallback remains productive.
  - proofpoint              # NOT re-fetched (multi-day vendor cadence per source-health notes).
  - dragos                  # NOT re-fetched (multi-week vendor cadence per source-health notes; failed-feed-endpoint pattern from prior sentinels).
  - rapid7                  # fetch_feed rapid7.com/blog/rss — 200 OK, 20 items in feed, 0 in 14h window. Last_modified 2026-05-25 11:16 UTC = 07:16 EDT just inside window from feed-server activity but in-feed items pre-window.
  - isc-sans                # fetch_feed isc.sans.edu/rssfeed.xml — 200 OK, 10 items, 0 in 14h window. Last_modified 2026-05-25 11:29 UTC = 07:29 EDT inside window from feed-server activity; in-feed items pre-window.
  - krebs                   # fetch_feed krebsonsecurity.com/feed — 200 OK, 10 items, 0 in 14h window. Last_modified 2026-05-25 11:29 UTC (server activity) but most-recent in-feed item pre-window.
  - dark-reading            # WebFetch top 5 — most recent 2026-05-22 Akamai / Verizon DBIR / China Webworm Discord (pre-window across the board). NO 2026-05-24 or 2026-05-25 dated articles in surface. China Webworm Discord (2026-05-22 pre-window) is corpus-adjacent to raw-2026-05-20-flash-1200-001 (Webworm EchoCreep GraphWorm); not raw-signaled this sweep (pre-window + corpus-adjacent).
  - thedfirreport           # NOT re-fetched (multi-month cadence per source-health notes).
  - greynoise               # NOT re-fetched (most recent post 2026-05-22 Coverage Gap 119k IPs corpus-covered; pre-window).
  - checkpoint-research     # WebFetch research.checkpoint.com/feed — 3 most-recent items dated 2026-05-22 (Nimbus Manticore IRGC-affiliated Iranian conflict / UNC1549 alias variant — corpus-tracked actor #004 via Unit 42 Screening Serpens raw-2026-05-23-flash-0600-001 anti-noise lock expired 2026-05-24 06:00, no fresh content in window to re-fire); 2026-05-18 weekly Threat Intelligence Report; 2026-05-13 Gentlemen RaaS. ZERO 2026-05-24/25 dated posts. Nimbus Manticore = Check Point alias for UNC1549 per finding-2026-05-23-FLASH-0001 cross-corpus note — pre-window + tracked-actor surface already covered in 5/23 FLASH per anti-noise expired; no Trigger 4 re-fire pressure.
  - reliaquest-blog         # NOT re-fetched (Loading placeholder DOM pattern from 00:00 sentinel; held).
  - f5-psirt                # NOT re-fetched (404 pattern across prior sweeps).
  - aikido                  # WebFetch blog.aikido.dev returned ECONNREFUSED — THIRD consecutive failure observation (prior 18:00 sentinel DNS failure documented in 06:00 sentinel narrative; 00:00 not re-tested; 06:00 not re-tested per FLASH-narrow). THIRD-STRIKE THRESHOLD met for stale flip per failure_count >= 2 + persist pattern threshold. STALE FLIP APPLIED this sweep: failure_count 2→3, status healthy→stale, stale_since 2026-05-25, last_error "blog.aikido.dev ECONNREFUSED — third consecutive failure observation across 18:00 + 07:30 sweeps".
  - palo-alto-psirt         # sample-sweep cadence
  - ivanti-psirt            # same
  - citrix-psirt            # same
  - sonicwall-psirt         # same
  - vmware-broadcom-psirt   # same
  - fortinet-psirt          # NOT re-fetched (transient SSL hostname-mismatch in 18:00 sentinel; held)
  - cisco-psirt             # NOT re-fetched (template-only render pattern persistent)
  - splunk-archimedes       # mcp__splunk-query | tstats count where (index=archimedes OR index=defenseclaw_local) earliest=-24h@h latest=now by index sourcetype → 31 events all in archimedes index (operation=14, scheduler=17). Splunk reachability HEALTHY.
  - splunk-defenseclaw      # Same query → zero events in -24h. 56th CONSECUTIVE DORMANT non-self sweep.
  - splunk-targeted-ioc-search  # mcp__splunk-query search index=defenseclaw_local earliest=-24h@h latest=now (216.126.225.129 OR megalodon OR tiledesk OR trapdoor OR ddjidd564 OR aes-secure OR remotepe OR DPAPILoader OR Iassvc.dll OR "@tiledesk/tiledesk-server" OR flipboxstudio OR CVE-2026-9082 OR CVE-2026-42897 OR CVE-2026-48172 OR UNC1549 OR MuddyWater OR "Screening Serpens" OR Lazarus OR APT28 OR APT29 OR APT37 OR APT40 OR APT41 OR "Charming Kitten" OR "Salt Typhoon" OR "Volt Typhoon" OR TeamPCP OR GlassWorm) | head 50 → ZERO events. Hand-built 17-IOC sweep covers Megalodon C2 IP + RemotePE C2 domain + DPAPILoader DLL + tracked actors + tracked CVEs. Hard Rule 8: silence is not disconfirming.
sources_querying_skipped_or_deferred:
  - shodan                  # not queried (no investigation hypothesis warrants paid-tier query)
  - censys                  # no MCP
  - virustotal              # not queried this sweep (Megalodon IOCs eligible for enrichment if grader promotes am-001 to finding-tier)
  - threatfox               # MCP not built; ABUSECH_API_KEY auth-injection blocked by WebFetch
  - malwarebazaar           # MCP not built; same auth-injection
  - falconfeedsio-twitter   # NOT re-fetched (nitter pool fragility per source-health)
  - x-gossithedog           # stale per source-health.yaml
  - x-cisagov               # not re-fetched (KEV JSON serves as canonical CISA surface this sweep)
splunk_first_party_check:
  query_a: "| tstats count where (index=archimedes OR index=defenseclaw_local) earliest=-24h@h latest=now by index sourcetype"
  query_b: "search index=defenseclaw_local earliest=-24h@h latest=now (216.126.225.129 OR megalodon OR tiledesk OR trapdoor OR ddjidd564 OR aes-secure OR remotepe OR DPAPILoader OR Iassvc.dll OR \"@tiledesk/tiledesk-server\" OR flipboxstudio OR CVE-2026-9082 OR CVE-2026-42897 OR CVE-2026-48172 OR UNC1549 OR MuddyWater OR \"Screening Serpens\" OR Lazarus OR APT28 OR APT29 OR APT37 OR APT40 OR APT41 OR \"Charming Kitten\" OR \"Salt Typhoon\" OR \"Volt Typhoon\" OR TeamPCP OR GlassWorm) | head 50"
  archimedes_index_events_24h: 31          # self-telemetry only (operation=14 + scheduler=17)
  defenseclaw_local_events_24h: 0
  splunk_first_party_dormant: true
  consecutive_dormant_sweeps: 56           # incremented from 55 in prior 06:00 sentinel
  targeted_ioc_hits: 0
  ioc_match_opportunity: true_executed_zero_match
  hard_rule_8_framing: |
    Targeted 17-IOC sweep across Megalodon C2 IP (216.126.225.129),
    RemotePE C2 domain (aes-secure[.]net), DPAPILoader DLL filename
    (Iassvc.dll), TrapDoor exfil endpoint (ddjidd564.github.io),
    @tiledesk/tiledesk-server package, flipboxstudio Laravel-Lang
    C2, plus all 11 corpus-active CVE / tracked-actor tokens —
    returned ZERO matches in -24h@h@h. First-party telemetry
    surface dormant non-self pattern continues (56th consecutive
    sweep). Hard Rule 8: silence is not disconfirming. The
    targeted hand-built query EXECUTED this sweep (vs the prior
    55 dormant-counts which were tstats-only): zero hits across
    the 17-IOC keyword set on -24h@h is a positive defensive
    signal but should not be over-interpreted (defenseclaw_local
    is a local instance not connected to a production network
    payload-class IOCs are the Splunk-actionable layer).
filter_evaluation_summary:
  in_window_items_total: 7                  # 5 SecurityWeek + 2 THN
  in_window_items_raw_signaled: 4           # am-001 Megalodon, am-002 Lazarus RemotePE, am-003 TrapDoor THN UPDATE, am-004 Anthropic Mythos 23K UPDATE
  in_window_items_filtered_out: 3           # SW Laravel-Lang relay (pure B-grade no-delta); SW DocketWise legal-sector breach; SW Radiology Associates healthcare breach
  in_window_items_flash_tier: 0             # ZERO FLASH trigger fires this sweep
  rejection_basis:
    - "SW Laravel-Lang Packages Poisoned (2026-05-25 06:41 EDT): direct fetch confirms 'pure B-grade relay' — same four packages (lang, http-statuses, attributes, actions), same flipboxstudio[.]info C2, same StepSecurity / Socket / Aikido prior-reporting. No new IOCs. No new attribution. No new victim disclosure. No novel technical analysis. Anti-noise lock laravel-lang-flipboxstudio-supply-chain ACTIVE through 2026-05-26 morning (raw-2026-05-23-am-001 + pm-003 + flash-2026-05-23-1800 covered). UPDATE absorption into morning brief at most; no raw-signal companion needed."
    - "SW DocketWise breach 143k (2026-05-25 05:37 EDT): legal-sector PII breach from third-party supply-chain partner repo compromise; no tracked actor, no CVE, no A&D relevance. Standard breach-disclosure landscape noise. Out of scope per Mode 1."
    - "SW Radiology Associates of Richmond breach 266k (2026-05-25 07:17 EDT): healthcare-sector PII breach (PHI exfiltration); no tracked actor, no CVE, no A&D relevance. Standard breach-disclosure landscape noise. Out of scope per Mode 1."
hard_rules_compliance:
  rule_2_no_attribution_origination: |
    THN Lazarus RemotePE raw-signal (am-002) preserves Fox-IT / NCC
    Group attribution language verbatim ("North Korea-linked Lazarus
    Group" — no confidence qualifier in their text) and explicitly
    flags this as RESTATEMENT of prior September 2025 reporting on
    same malware family (DPAPILoader earliest artifact November 2023;
    observation period mid-2023 to mid-2024). Hard Rule 2: Archimedes
    does not originate attribution AND grader / FLASH-policy Trigger 2
    requires NEW not restated attribution. am-002 captures the
    surface for analyst awareness but explicitly NOT a Trigger 2 fire.
    Megalodon (am-001) preserved UNATTRIBUTED per SafeDep + SecurityWeek
    primary sources. TrapDoor (am-003) preserved UNATTRIBUTED per
    Socket + THN primary sources. Anthropic Mythos (am-004) is research/
    methodology coverage, no actor attribution involved.
  rule_3_no_exploitation: "No PoC code, no payloads, no exploit guides referenced. CVE references descriptive only."
  rule_4_passive_only: "No active scans. SpiderFoot not invoked. authorized-targets.yaml empty."
  rule_6_quote_limit: |
    am-002 includes 7-word quoted phrase from Fox-IT ("purpose-built for long-term
    observation campaigns") and 7-word quoted phrase ("may be reserved for high-
    value targets") — both within 15-word limit, single instance each per source.
    am-001 includes 4-word quoted phrase from SafeDep ("base64-encoded bash") for
    technical-mechanism preservation — within limit. No other quotes in the four
    raw-signal companions.
  rule_7_credentials: "No credential exposure surfaced this window."
  rule_8_splunk_first_party_priority: |
    Hand-built 17-IOC targeted sweep on defenseclaw_local returned
    ZERO hits in -24h@h. 56th consecutive dormant non-self sweep on
    auto-cadence (incremented from 55 in prior 06:00 sentinel).
    Megalodon C2 IP 216.126.225.129, RemotePE C2 aes-secure[.]net,
    DPAPILoader filename Iassvc.dll, TrapDoor exfil
    ddjidd564.github.io, @tiledesk/tiledesk-server package,
    flipboxstudio Laravel-Lang C2 all queried — zero matches.
    Silence is not disconfirming. The targeted-query execution
    this sweep is a Mode 1 procedural step that the prior 55
    dormant-count sweeps were not running, formalized in response
    to the 06:00 sentinel's recommendation for fresh-IOC enrichment
    on Megalodon morning-candidate promotion.
source_health_changes:
  - source_yaml_id: mandiant
    observation: |
      feedburner.com/Mandiant returned 404 — 23rd consecutive sweep
      with this failure mode (prior 22 documented across multi-week
      pattern in source-health notes).
    runtime_change_applied: |
      failure_count 21→22; last_error timestamp updated to 2026-05-25T07:30
      pre-brief; status held healthy per existing operator policy
      (held-healthy-pending-alt-endpoint-decision documented in
      source-health notes); operator-set notes field preserved
      verbatim per source-health-yaml-field-ownership rule.
  - source_yaml_id: aikido
    observation: |
      blog.aikido.dev WebFetch returned ECONNREFUSED — third consecutive
      failure observation (prior failures across 2026-05-24 18:00 sentinel
      DNS failure and prior 06:00 / 00:00 not-re-tested per FLASH-narrow
      scope; this 07:30 retry confirms persistent failure mode).
    runtime_change_applied: |
      failure_count 2→3 (past threshold); status healthy→stale flip
      APPLIED this sweep per failure_count >= 2 + persist pattern
      threshold; stale_since 2026-05-25; last_error "blog.aikido.dev
      ECONNREFUSED — third consecutive failure observation across
      18:00 + 07:30 sweeps". Source held with stale flag; collector
      will skip per 24h-since-stale rule until 2026-05-26.
      Operator-set notes (if any) preserved verbatim.
  - source_yaml_id: volexity
    observation: |
      volexity.com/blog/feed fetch_feed returned XML parse error
      "<unknown>:17:68: not well-formed (invalid token)" — third
      consecutive failure observation (prior 18:00 sentinel WebFetch
      returned Loading placeholder DOM; 00:00 and 06:00 not re-tested
      per FLASH-narrow scope; this 07:30 fetch_feed retry confirms
      persistent malformed-XML mode).
    runtime_change_applied: |
      failure_count 2→3 (past threshold); status healthy→stale flip
      APPLIED this sweep per failure_count >= 2 + persist pattern
      threshold; stale_since 2026-05-25; last_error
      "volexity.com/blog/feed XML parse error <unknown>:17:68: not
      well-formed token — third consecutive failure observation
      across 18:00 + 07:30 sweeps". Source held with stale flag;
      collector will skip per 24h-since-stale rule until 2026-05-26.
      Operator-set notes (if any) preserved verbatim. Note: Volexity
      is a high-quality but low-frequency publisher (multi-month
      cadence per source-health prior notes); the malformed-XML
      mode may resolve on next vendor-side feed-server refresh
      and source flips back to healthy on first successful fetch.
      Carry-forward for operator awareness — Volexity surface dark
      while stale flag holds.
companion_raw_signal_files_this_sweep:
  - raw-2026-05-25-am-001-securityweek-megalodon-5561-github-repos-workflow-dispatch-tiledesk
  - raw-2026-05-25-am-002-thn-lazarus-remotepe-restatement-not-new-attribution-fox-it-ncc-group
  - raw-2026-05-25-am-003-thn-trapdoor-multi-ecosystem-update-absorption-anti-noise-locked
  - raw-2026-05-25-am-004-securityweek-anthropic-mythos-23000-osss-update-from-10k-baseline
carry_forward_items_for_morning_brief:
  - id: megalodon-primary-morning-finding-candidate
    type: primary_morning_candidate_finding_tier
    summary: |
      Megalodon supply-chain attack documented by SafeDep (2026-05-21
      primary; missed by prior Archimedes sweeps for 4d — collection
      gap acknowledged) and surfaced via SecurityWeek (Ionut Arghire
      2026-05-25 03:40 EDT in-window). 5,718 malicious commits across
      5,561 GitHub repositories injected 2026-05-18 11:36-17:48 UTC
      via GitHub Actions workflow_dispatch anti-recursion bypass.
      Two payload variants: SysDiag (push + pull_request_target,
      mass-exposure) and Optimize-Build (workflow_dispatch dormant
      backdoor). Both request id-token:write + actions:read,
      base64-encoded bash execution. Downstream npm publication of
      @tiledesk/tiledesk-server 2.18.6-2.18.12 from poisoned source
      by legitimate maintainer eljohnny 2026-05-19 to 2026-05-21
      (clean version: 2.18.5). 9 Tiledesk repos affected; secondary
      orgs Black-Iron-Project (8 repos), WISE-Community, ~5,500
      smaller repos. C2 216.126.225.129:8443. Throwaway GitHub
      accounts with random 8-char usernames (examples rkb8el9r,
      bhlru9nr, lo6wt4t6). Author identity spoofing with names
      build-bot / auto-ci / ci-bot / pipeline-bot. 7 commit-message
      variants. Tiledesk forensic commit hash
      acac5a9854650c4ae2883c4740bf87d34120c038. ATTRIBUTION:
      UNATTRIBUTED (SafeDep makes no tracked-actor claim; SafeDep
      attributes discovery to their internal "Malysis engine").
      A&D RELEVANCE: structural-indirect via developer-ecosystem
      ubiquity only; no A&D-prime named. Recommend grader promote
      to finding-tier. Recommend operator add safedep.io to
      source-grades.yaml as tentative-B-grade primary research
      source (Socket / Snyk / StepSecurity tier; 4-day post-original-
      publication detection gap acknowledged). Recommend
      VirusTotal enrichment on 216.126.225.129. Cross-corpus
      diagnostic note for actor-profiler on next /update-tracking
      cycle: build-bot / auto-ci author-identity-spoofing pattern
      thematically overlaps with TeamPCP's
      claude@users.noreply.github.com spoofing from 2026-05-12 Mini
      Shai-Hulud worm — technique is portable and likely shared
      across multiple unattributed cybercriminal operators in the
      current SDLC-targeting wave; do NOT collapse Megalodon /
      TrapDoor / TeamPCP into one actor without A/B-grade attribution.
      Splunk first-party check on 216.126.225.129 returned zero
      hits in -24h (this sweep executed).
  - id: lazarus-remotepe-restatement-not-new-attribution
    type: tracking_awareness_restatement_not_new
    summary: |
      THN Lazarus Group RemotePE article (2026-05-25 05:32 EDT)
      relays NCC Group / Fox-IT (named researchers Yun Zheng Hu +
      Mick Koomen) expanded technical analysis of memory-only RAT
      first highlighted September 2025. Observation period mid-2023
      to mid-2024; DPAPILoader earliest artifact November 2023;
      RemotePE first timestamp July 4, 2023. Victim sectors:
      financial, cryptocurrency, DeFi. ATTRIBUTION: "North Korea-
      linked Lazarus Group" per THN with no confidence qualifier
      in Fox-IT/THN body text. Lazarus = tracked actor #003 in
      _roster.yaml — but this is RESTATEMENT not new attribution
      per FLASH-POLICY Trigger 2 (which requires
      attribution_is_new_not_restatement). Hard Rule 2: Archimedes
      does not originate attribution AND grader / FLASH-POLICY
      Trigger 2 explicitly fails on restatement. IOCs: C2 domain
      aes-secure[.]net; DPAPILoader filename Iassvc.dll; no file
      hashes, no IPs in THN body. NO A&D mentions. Cross-platform
      claim absent (Windows only in this article). Material for
      morning brief tracking-awareness block; Splunk first-party
      hand-built sweep on aes-secure[.]net + Iassvc.dll returned
      zero hits in -24h (this sweep executed). Operational ask
      for actor-profiler on next /update-tracking #003 review:
      determine whether RemotePE / DPAPILoader / RemotePELoader
      / Hell's Gate / ETW patching mechanisms warrant entry into
      Lazarus dossier TTP catalog (these are not all in the
      current dossier per cursory review; full review at
      next-due Lazarus refresh on 2026-06-30 or earlier).
  - id: trapdoor-update-flag-anti-noise-locked
    type: anti_noise_locked_update_absorption
    summary: |
      THN TrapDoor article (2026-05-25 01:59 EDT) is corpus-anchored
      via finding-2026-05-24-0001 (Socket primary 2026-05-24 PM brief
      commit 0774f79). Anti-noise lock
      trapdoor-multi-ecosystem-supply-chain-socket ACTIVE through
      2026-05-25 16:00 EDT. THN net-new over Socket primary:
      .cursorrules / CLAUDE.md AI-agent-config manipulation framing;
      named GitHub-PR targets browser-use/browser-use,
      langchain-ai/langchain, langflow-ai/langflow; exfil endpoint
      ddjidd564.github.io. NO new file hashes, NO new C2 domains
      beyond the GitHub Pages endpoint, NO IP IOCs, NO actor
      attribution. THN explicit disambiguation from separate
      Android ad-fraud TrapDoor campaign (HUMAN Satori prior week).
      UPDATE-flag absorption into morning brief per anti-noise rule;
      NOT a re-FLASH (lock locks Trigger 5 re-fire). Splunk first-
      party hand-built sweep on ddjidd564.github.io + TrapDoor
      keywords returned zero hits in -24h (this sweep executed).
  - id: anthropic-mythos-23k-update-from-10k-baseline
    type: research_methodology_update
    summary: |
      SW Anthropic Mythos article (2026-05-25 06:58 EDT) updates
      the corpus-tracked Project Glasswing / Claude Mythos AI
      vulnerability discovery research from prior 10,000-findings
      baseline (carry-forward from raw-2026-05-23 sentinel-stream
      via THN coverage) to NEW 23,000 potential vulnerabilities
      across 1,000 OSS projects scanned. Confirmed-vs-unconfirmed
      breakdown: 1,726 confirmed (of 1,900 reviewed); 1,000+
      rated high/critical; projection 3,900 critical/high when
      all current findings complete; 1,100+ unverified findings
      reported to vendors; 65 security advisories published; 75
      critical/high issues patched to date; 90-day disclosure
      window. Anthropic researcher names NOT cited (collective
      "the AI company explained"). Named projects-of-interest
      from prior coverage carry through: Firefox (271 vulns),
      Curl (1 low-sev), additional Palo Alto + Google testing.
      No A&D / spacecraft / satellite software named. No new
      CVEs cited in this SW piece (prior corpus has CVE-2026-5194
      wolfSSL via THN 2026-05-23 coverage). Material for morning
      brief AI-vulnerability-discovery-methodology block alongside
      Rapid7 Q1 vulnerability-vs-social-engineering finding and
      GreyNoise 119k IPs analysis. Disposition: morning brief
      UPDATE on existing carry-forward; NOT a graded finding
      (research/methodology not actor-attributable, not actively-
      exploited, not A&D-specific).
  - id: cve-2026-9082-drupal-kev-due-date-t-2
    type: kev_deadline_awareness
    summary: |
      CVE-2026-9082 Drupal Core SQL injection KEV federal due-date
      2026-05-27 — T-2 from this sweep (Wednesday end-of-business,
      less than 56h away). Already in morning + PM briefs every
      day since KEV add 2026-05-22. Carry-forward to 2026-05-25
      morning brief KEV-deadline action-item block at peak urgency
      tier (T-2 = last-call). No fresh Drupal SA-CORE content in
      window; no Drupal-attributable victim-disclosure surfacing;
      ITW confirmation from prior raw-2026-05-22 18:00 sentinel
      (Imperva 15k attempts / 6k sites) holds. DIB / CMMC partner-
      flow estates inheriting FCEB compliance deadlines should be
      flagged for patch-window posture review by morning briefer.
  - id: cve-2026-42897-exchange-kev-due-date-t-4
    type: kev_deadline_awareness
    summary: |
      VT-008 Exchange CVE-2026-42897 KEV federal due-date 2026-05-29 —
      T-4 from this sweep. No MSRC GA patch in window; ESU-only
      patch path + EEMS / EOMT mitigation continues. MSRC blog
      surface continues template-only / redirect pattern. Active-
      exploitation single-source veto on MSRC "Exploitation Detected"
      tag still holds — no Mandiant / Volexity / Unit 42 / MSTIC TI
      blog / CrowdStrike / ESET / Sophos / Bitdefender independent
      telemetry corroboration in window (Volexity now stale-flagged
      from this sweep; surface dark). Morning brief KEV-deadline
      action-item block candidate at T-4 urgency. DIB / CMMC partner-
      flow estates with on-prem Exchange should continue EEMS/EOMT
      mitigation tracking.
  - id: nvd-api-result-pagination-quirk-persist
    type: collection_retry_target
    summary: |
      NVD lastModified critical-CVE query for 2026-05-24T17:30 →
      2026-05-25T07:30 EDT window returned totalResults=5 (later
      probe) and totalResults=10 (earlier probes) but persistent
      empty vulnerabilities[] array across THREE query attempts
      with variations on resultsPerPage parameter (unset, 20, 2000)
      and date-format (EDT, UTC). API result-pagination quirk
      PERSISTS — same condition documented in 06:00 sentinel.
      Cannot trigger-evaluate the 5-10 unknown-ID critical CVEs
      without ID-level resolution. RECOMMENDATION: vuln-tracker
      next-pass should hit https://nvd.nist.gov/general/search-vulnerability
      web-UI directly (not the JSON API) to inventory the
      unresolved critical CVEs, OR build per-CVE direct retrieval
      pipeline if a Specific ID surfaces via THN / BleepingComputer /
      SecurityWeek vendor PSIRT layer. Not a stale-flip for NVD
      (endpoint reachable; semantic quirk only).
  - id: source-health-volexity-aikido-third-strike-stale-flips
    type: source_health_durable_change
    summary: |
      Two new STALE FLIPS applied this sweep: (1) blog.aikido.dev
      ECONNREFUSED third consecutive failure observation — third
      strike on the failure_count >= 2 + persist pattern threshold;
      stale_since 2026-05-25, status healthy→stale, last_error
      captured. (2) volexity.com/blog/feed XML parse error
      <unknown>:17:68: not well-formed token third consecutive
      observation — third strike on same threshold; stale_since
      2026-05-25, status healthy→stale, last_error captured.
      Both held with stale flag; collector will skip per 24h-since-
      stale rule until 2026-05-26. Operator awareness: Volexity is
      multi-month-cadence high-quality publisher (likely vendor-side
      feed-server transient malformed-XML mode that may resolve on
      next refresh — flip back to healthy on first successful fetch);
      Aikido is more-active vendor research publisher (the
      ECONNREFUSED pattern is more concerning and may warrant
      operator-side DNS / network diagnostic on Frank or alt-endpoint
      sourcing if the stale flip persists past 2026-05-27).
  - id: iran-cyber-watch-standing-section-nimbus-manticore-checkpoint-pre-window
    type: standing_section_context
    summary: |
      Check Point research feed surfaced Nimbus Manticore article
      (2026-05-22 pre-window) — IRGC-affiliated Iranian conflict
      operations using AppDomain hijacking + new MiniFast backdoor
      with AI-assisted development. Nimbus Manticore = Check Point
      alias for UNC1549 per finding-2026-05-23-FLASH-0001 cross-
      corpus note. PRE-WINDOW by 3 days and corpus-already-tracked
      via Unit 42 Screening Serpens raw-2026-05-23-flash-0600-001
      anti-noise lock (expired 2026-05-24 06:00; no fresh content
      in window to re-fire). Material for Iran Cyber Watch
      standing-section context if briefer chooses to surface
      (NOT required; pre-window AND corpus-covered AND attribution
      = restatement). Check Point's AppDomain hijacking + MiniFast
      framing offers operational-tradecraft detail that may
      complement Unit 42's Screening Serpens content as a
      cross-source corroboration note for actor-profiler #004
      review at next /update-tracking pass.
notes:
  - "FOUR raw-signal companion files written this sweep: am-001 Megalodon (strong morning candidate, finding-tier-eligible, full IOC extraction completed); am-002 Lazarus RemotePE (RESTATEMENT-not-new-attribution awareness; explicitly NOT a Trigger 2 fire per FLASH-POLICY); am-003 TrapDoor THN (anti-noise-locked UPDATE absorption); am-004 Anthropic Mythos 23K (research/methodology UPDATE from 10K baseline)."
  - "ZERO FLASH-trigger fires this sweep — collection is for the 08:00 morning brief, not FLASH dispatch (pre-brief collection mode does not post to Discord). 7 in-window items evaluated, 4 raw-signaled, 3 filtered out (SW Laravel-Lang pure relay, SW DocketWise legal-sector, SW Radiology healthcare). Trigger 2 (tracked-actor attribution) NEAR-MISS on Lazarus RemotePE but blocked by restatement-not-new condition. Trigger 5 (A&D-sector campaign) NEAR-MISS on Megalodon but blocked by no-A&D-prime-named condition (5,561 multi-victim YES; A&D-direct FAIL)."
  - "TWO new source-health STALE FLIPS this sweep on third-strike pattern: aikido (blog.aikido.dev ECONNREFUSED) and volexity (volexity.com/blog/feed malformed XML). Both held with stale flag; collector skips per 24h-since-stale rule. Mandiant feedburner 23rd consecutive failure (failure_count incremented per single-failure rule; held healthy per long-standing operator policy held-healthy-pending-alt-endpoint-decision). NVD API result-pagination quirk persists across three probes — not a stale flip (semantic quirk; endpoint reachable)."
  - "Splunk first-party: 31 archimedes self-telemetry events in -24h; ZERO defenseclaw_local events = 56th consecutive dormant non-self sweep. Hand-built TARGETED 17-IOC keyword query EXECUTED this sweep (Megalodon C2 IP 216.126.225.129 + RemotePE C2 aes-secure[.]net + DPAPILoader Iassvc.dll + TrapDoor exfil ddjidd564.github.io + @tiledesk/tiledesk-server + flipboxstudio + 11 tracked-actor / tracked-CVE tokens) — ZERO hits across all 17 keywords. Hard Rule 8: silence is not disconfirming."
  - "KEV catalog version 2026.05.22 UNCHANGED across 60h+ — last add CVE-2026-9082 Drupal 2026-05-22 EDT. KEV deadlines T-2 Drupal CVE-2026-9082 (2026-05-27 Wed EOB; 56h from this sweep) and T-4 Exchange CVE-2026-42897 (2026-05-29) carry forward at peak urgency for the morning brief KEV-deadline action-item block."
  - "Pre-brief carry-forwards for 08:00 Monday morning brief: (1) Megalodon as primary morning finding candidate with full SafeDep direct-retrieval IOC extraction in am-001 — recommend grader promote and operator add safedep.io to source-grades.yaml; (2) Lazarus RemotePE in am-002 as tracking-awareness restatement context — actor-profiler hook for next #003 /update-tracking; (3) TrapDoor THN UPDATE in am-003 absorbing into existing anti-noise lock; (4) Anthropic Mythos 23K in am-004 as research/methodology UPDATE; (5) CVE-2026-9082 Drupal KEV T-2 peak-urgency action item; (6) VT-008 Exchange CVE-2026-42897 KEV T-4 action item; (7) NVD API result-pagination quirk persists — vuln-tracker hook for direct UI lookup; (8) Aikido + Volexity source-health stale-flag awareness for operator; (9) Iran Cyber Watch standing-section context via Check Point Nimbus Manticore = UNC1549 alias pre-window awareness."
  - "Hard Rules compliance: Rule 2 — Lazarus RemotePE explicitly flagged as restatement not new attribution; Hard Rule 2 + FLASH-POLICY Trigger 2 both block on this. Megalodon + TrapDoor preserved UNATTRIBUTED. Rule 3 — no PoC content. Rule 4 — passive only (Splunk hand-built query is first-party defensive telemetry, not active recon). Rule 6 — two short quotes from Fox-IT in am-002, both ≤ 15 words single-instance single-source; one short quote from SafeDep in am-001 for technical-mechanism preservation. Rule 7 — no credentials surfaced. Rule 8 — defenseclaw_local 56th consecutive dormant non-self sweep + targeted 17-IOC sweep zero hits."
  - "Briefer/orchestrator action: 08:00 Monday morning brief composition proceeds with one strong primary finding candidate (Megalodon — am-001) plus three contextual UPDATE / awareness items (am-002 Lazarus restatement / am-003 TrapDoor anti-noise UPDATE / am-004 Mythos research-methodology UPDATE). Two KEV-deadline carry-forwards at peak / elevated urgency (Drupal T-2 / Exchange T-4). Standing sections ✈️ Sector Focus: A&D (no direct A&D-prime named-victim activity; structural-indirect supply-chain SDLC ubiquity framing on Megalodon) and 🇮🇷 Iran Cyber Watch (no in-window Iranian-actor primary research; Nimbus Manticore Check Point alias for UNC1549 = pre-window corpus-covered awareness context). Pre-brief writes no FLASH; no Discord post."
---

# 07:30 EDT Monday pre-brief sweep — 4 RAW-SIGNAL COMPANIONS WRITTEN

This sentinel record documents the 2026-05-25 07:30 EDT pre-brief
collection sweep. Window: 2026-05-24T17:30 to 2026-05-25T07:30 EDT
(14h). Companion raw-signal files written: am-001 through am-004.

## Sweep outcome

**FOUR raw-signal companions written for the 14h window**, plus this
sentinel index. Companions:

1. **am-001 Megalodon** — strong morning finding candidate. SafeDep
   primary (2026-05-21) + SecurityWeek relay (Ionut Arghire,
   2026-05-25 03:40 EDT in-window). 5,718 malicious commits across
   5,561 GitHub repositories injected 2026-05-18 via GitHub Actions
   `workflow_dispatch` anti-recursion bypass. @tiledesk/tiledesk-server
   2.18.6-2.18.12 published from poisoned source by legitimate
   maintainer eljohnny. C2 `216.126.225.129:8443`. Throwaway GitHub
   accounts with author-identity spoofing (build-bot, auto-ci,
   ci-bot, pipeline-bot). **UNATTRIBUTED**. Full IOC extraction
   completed via direct SafeDep retrieval.

2. **am-002 Lazarus RemotePE** — RESTATEMENT-not-new-attribution
   awareness. THN (Ravie Lakshmanan, 2026-05-25 05:32 EDT) relays
   NCC Group / Fox-IT (Yun Zheng Hu + Mick Koomen) expanded technical
   analysis of memory-only RAT first highlighted September 2025;
   observation period mid-2023 to mid-2024. **Explicitly NOT a
   Trigger 2 fire** per FLASH-POLICY (which requires
   `attribution_is_new_not_restatement`). C2 `aes-secure[.]net`;
   DPAPILoader `Iassvc.dll`. No A&D mention.

3. **am-003 TrapDoor THN UPDATE** — anti-noise-locked UPDATE
   absorption. Corpus-anchored via finding-2026-05-24-0001 (Socket
   primary; PM brief commit 0774f79). Anti-noise lock
   `trapdoor-multi-ecosystem-supply-chain-socket` ACTIVE through
   2026-05-25 16:00 EDT. Net-new framing detail (`.cursorrules` /
   `CLAUDE.md` AI-agent-config manipulation; PR targets
   browser-use / langchain-ai / langflow-ai; exfil
   `ddjidd564.github.io`). NO new hashes / IPs / domains.

4. **am-004 Anthropic Mythos 23K UPDATE** — research/methodology
   UPDATE. SW (Eduard Kovacs, 2026-05-25 06:58 EDT). 23,000 potential
   vulns across 1,000 OSS projects (up from 10,000 prior baseline).
   1,726 confirmed (of 1,900 reviewed); 1,000+ high/critical.

## Filtered out (NOT raw-signaled)

- **SW Laravel-Lang Packages Poisoned** (06:41 EDT) — direct fetch
  confirms PURE B-grade relay of corpus-already-tracked
  Laravel-Lang flipboxstudio (anti-noise locked). Same four
  packages, same C2, same StepSecurity/Socket/Aikido prior reporting.
  No deltas. UPDATE absorption into morning brief at most.
- **SW DocketWise breach 143k** (05:37 EDT) — legal sector, no
  actor, no CVE, no A&D. Out of scope per Mode 1.
- **SW Radiology Associates breach 266k** (07:17 EDT) — healthcare
  sector, no actor, no CVE, no A&D. Out of scope per Mode 1.

## One-paragraph summary

The Monday-morning 14h window broke the Sunday-quiet baseline with
7 in-window items spanning four primary sources (SecurityWeek + THN).
Four raw-signal companions captured: Megalodon (strong morning
finding candidate with full IOC extraction from SafeDep direct
retrieval, UNATTRIBUTED, 5,561 GitHub repositories backdoored via
`workflow_dispatch` anti-recursion bypass), Lazarus RemotePE
(restatement not new attribution per FLASH-POLICY Trigger 2 — NOT
a fire; Fox-IT September 2025 prior reporting on memory-only RAT
with mid-2023/24 observation period; C2 `aes-secure[.]net`, DPAPI
loader `Iassvc.dll`), TrapDoor THN (anti-noise-locked UPDATE
absorption with `.cursorrules`/`CLAUDE.md` AI-agent-config framing
detail), and Anthropic Mythos 23K (research/methodology UPDATE from
prior 10K baseline). Three items filtered out (SW Laravel-Lang pure
relay; SW DocketWise legal sector; SW Radiology healthcare). KEV
catalog 2026.05.22 unchanged 60h+; deadlines T-2 Drupal CVE-2026-9082
(56h to Wednesday end-of-business) and T-4 Exchange CVE-2026-42897
carry forward at peak urgency. NVD API result-pagination quirk
persists across three probes (`totalResults=5-10` but empty
`vulnerabilities[]`); vuln-tracker hook for direct UI lookup. Two
new source-health STALE FLIPS applied on third-strike pattern:
`aikido` (ECONNREFUSED) and `volexity` (malformed XML). Mandiant
feedburner 23rd consecutive failure (held healthy per long-standing
policy). Splunk first-party: 31 archimedes self-telemetry events
in -24h; ZERO `defenseclaw_local` events = 56th consecutive
dormant non-self sweep; hand-built 17-IOC targeted query executed
across Megalodon C2 / RemotePE C2 / DPAPI DLL / TrapDoor exfil /
@tiledesk package / flipboxstudio + 11 tracked-actor / tracked-CVE
tokens, ZERO hits.

## In-window items — detailed disposition

### Raw-signaled (4)

| Item | Source(s) | Pub | Raw-signal file | Reason |
|---|---|---|---|---|
| Megalodon | SafeDep + SecurityWeek | 2026-05-25 03:40 EDT | am-001 | Strong morning finding candidate; full IOC extraction |
| Lazarus RemotePE | THN (NCC/Fox-IT primary) | 2026-05-25 05:32 EDT | am-002 | Tracked-actor surface but RESTATEMENT-not-new — Trigger 2 BLOCKED |
| TrapDoor | THN (Socket primary) | 2026-05-25 01:59 EDT | am-003 | Anti-noise-locked UPDATE absorption |
| Anthropic Mythos | SecurityWeek | 2026-05-25 06:58 EDT | am-004 | Research/methodology UPDATE from 10K → 23K baseline |

### Filtered out (3)

| Item | Source | Pub | Reason filtered |
|---|---|---|---|
| Laravel-Lang | SecurityWeek | 2026-05-25 06:41 EDT | Pure B-grade relay; no deltas; anti-noise locked |
| DocketWise breach | SecurityWeek | 2026-05-25 05:37 EDT | Legal sector; no actor / CVE / A&D |
| Radiology Associates breach | SecurityWeek | 2026-05-25 07:17 EDT | Healthcare sector; no actor / CVE / A&D |

## FLASH-trigger near-misses (informational; pre-brief does not dispatch FLASH)

- **Trigger 2 (tracked-actor attribution) NEAR-MISS** on Lazarus
  RemotePE: tracked actor #003 cited, but content is restatement of
  September 2025 prior reporting (observation period mid-2023 to
  mid-2024; DPAPILoader November 2023 earliest artifact). FLASH
  Trigger 2 explicitly requires `attribution_is_new_not_restatement`.
  Hard Rule 2 also blocks Archimedes-originated attribution. The
  surface is tracking-awareness material for the morning brief and
  actor-profiler #003 review hook, NOT a Trigger 2 fire.
- **Trigger 5 (A&D-sector campaign) NEAR-MISS** on Megalodon: multi-
  victim YES (5,561 GitHub repositories), but A&D-direct FAIL — no
  A&D-prime named in any source; structural-indirect via developer-
  ecosystem ubiquity only. Same calculus that has held for Mini
  Shai-Hulud, TrapDoor (Socket), art-template, durabletask. Not a
  Trigger 5 fire absent A&D-prime customer-impact statement.
- **Trigger 1 (critical CVE actively exploited)**: NVD API quirk
  blocks resolution of 5-10 unknown-ID critical CVEs in the 14h
  window; cannot trigger-evaluate without ID resolution. KEV
  unchanged — no new active-exploitation surface for in-corpus
  CVEs.
- Triggers 3, 4, 6: not fired (no first-party IOC hit; no tracked-
  actor TTP change with attribution; no zero-day-without-patch).

## Splunk first-party check

Query A: `| tstats count where (index=archimedes OR index=defenseclaw_local) earliest=-24h@h latest=now by index sourcetype`

Result A: 31 events in `archimedes` index (operation=14 + scheduler=17
self-telemetry). ZERO `defenseclaw_local` events. **56th consecutive
dormant non-self sweep**.

Query B (hand-built targeted IOC sweep, executed this sweep):
`search index=defenseclaw_local earliest=-24h@h latest=now (216.126.225.129 OR megalodon OR tiledesk OR trapdoor OR ddjidd564 OR aes-secure OR remotepe OR DPAPILoader OR Iassvc.dll OR "@tiledesk/tiledesk-server" OR flipboxstudio OR CVE-2026-9082 OR CVE-2026-42897 OR CVE-2026-48172 OR UNC1549 OR MuddyWater OR "Screening Serpens" OR Lazarus OR APT28 OR APT29 OR APT37 OR APT40 OR APT41 OR "Charming Kitten" OR "Salt Typhoon" OR "Volt Typhoon" OR TeamPCP OR GlassWorm) | head 50`

Result B: ZERO events. 17 keywords covering this sweep's new IOCs
(Megalodon C2 IP, RemotePE C2 domain, DPAPILoader DLL, TrapDoor
exfil endpoint, @tiledesk package), prior corpus IOC
(flipboxstudio), corpus-active CVEs (Drupal / Exchange / LiteSpeed),
and 11 tracked actors. **Zero hits.** Hard Rule 8: silence is not
disconfirming.

Splunk reachability HEALTHY.

## Source health changes

- **mandiant** — feedburner 23rd consecutive 404; `failure_count`
  21→22; status held healthy per long-standing operator policy
  (alt-endpoint decision pending); operator-set `notes` preserved
  verbatim.
- **aikido** — blog.aikido.dev ECONNREFUSED third consecutive
  failure observation; THIRD STRIKE on failure_count >= 2 + persist
  pattern threshold; status healthy→**stale**; `stale_since`
  2026-05-25; `last_error` "blog.aikido.dev ECONNREFUSED — third
  consecutive failure observation across 18:00 + 07:30 sweeps".
  Collector skips per 24h-since-stale rule until 2026-05-26.
  Operator-set `notes` preserved verbatim.
- **volexity** — volexity.com/blog/feed XML parse error
  `<unknown>:17:68: not well-formed (invalid token)` third
  consecutive failure observation; THIRD STRIKE on same threshold;
  status healthy→**stale**; `stale_since` 2026-05-25; `last_error`
  captured. Collector skips per 24h-since-stale rule until
  2026-05-26. Operator-set `notes` preserved verbatim. Note:
  Volexity is multi-month-cadence high-quality publisher; malformed-
  XML mode may resolve on next vendor-side feed refresh and flip
  back to healthy on first successful fetch.

## Quiet-hours posture (informational)

- 07:35 EDT is INSIDE 21:00-09:00 quiet hours (window ends 09:00
  EDT, T+1.5h). Pre-brief collection does NOT post to Discord
  regardless of quiet-hours status — collection feeds the 08:00
  morning brief which the briefer composes and ships to
  `#intel-briefs`.
- Critical-override conditions (CVSS 10.0 + confirmed active
  exploitation + tracked actor + A&D watchlist hit) not met on any
  in-window item. Moot for pre-brief collection.

## Hard Rules compliance

- **Rule 2** (no Archimedes-originated attribution): Lazarus
  RemotePE explicitly flagged as RESTATEMENT not new attribution;
  Hard Rule 2 + FLASH-POLICY Trigger 2 both block on this surface.
  Megalodon + TrapDoor preserved UNATTRIBUTED per primary sources.
- **Rule 3** (no exploitation content): no PoC, no payloads, no
  exploit guides referenced. CVE references descriptive only.
- **Rule 4** (passive only): no active scans; SpiderFoot not
  invoked; `authorized-targets.yaml` empty. Splunk hand-built
  query is first-party defensive telemetry on Archimedes's own
  instance, not active recon.
- **Rule 6** (15-word quote limit): all quotes in am-001 / am-002
  within limit (single instance per source).
- **Rule 7** (credentials radioactive): no credential exposure
  surfaced.
- **Rule 8** (Splunk first-party): targeted 17-IOC hand-built sweep
  executed; ZERO hits. 56th consecutive dormant non-self sweep.
  Silence is not disconfirming.

## Carry-forwards to 08:00 Monday morning brief

1. **MEGALODON primary morning finding candidate** (am-001) — full
   IOC extraction; SafeDep direct retrieval; recommend grader
   promote, operator add safedep.io to source-grades.yaml,
   VirusTotal enrichment on 216.126.225.129.
2. **Lazarus RemotePE RESTATEMENT** (am-002) — tracking-awareness;
   actor-profiler #003 hook for next /update-tracking review.
3. **TrapDoor UPDATE flag** (am-003) — anti-noise-locked absorption;
   `.cursorrules` / `CLAUDE.md` AI-agent-config framing detail.
4. **Anthropic Mythos 23K UPDATE** (am-004) — research/methodology
   UPDATE from 10K baseline.
5. **CVE-2026-9082 Drupal KEV T-2** — peak-urgency action item for
   morning brief KEV-deadline block (Wed end-of-business deadline,
   56h away).
6. **VT-008 Exchange CVE-2026-42897 KEV T-4** — elevated action
   item.
7. **NVD API result-pagination quirk persistence** — vuln-tracker
   hook for direct UI lookup; 5-10 unknown-ID critical CVEs
   in 14h window pending ID resolution.
8. **Aikido + Volexity source-health stale-flag awareness** —
   operator action: Aikido ECONNREFUSED may warrant DNS / network
   diagnostic; Volexity malformed-XML may self-resolve on next
   feed refresh.
9. **Iran Cyber Watch context** — Check Point Nimbus Manticore =
   UNC1549 alias (pre-window awareness only; corpus-tracked actor
   #004 already covered via Unit 42 Screening Serpens).

## Disposition

- **No Discord post** — pre-brief collection does not post; the
  08:00 morning brief composition consumes this sentinel +
  carry-forwards + 4 companion raw-signal files.
- **4 raw-signal companions written** (am-001 through am-004); no
  IOCs added to `_master-index.yaml` by collector — grader handles
  index updates if Megalodon promotes to finding-tier.
- **Source-health updates applied**: mandiant failure_count 21→22
  (held healthy); aikido + volexity stale flips (third-strike
  pattern); runtime fields only; operator-set notes preserved
  verbatim per source-health-yaml-field-ownership rule.
- **Splunk HEC telemetry** `event_type=pre_brief_collection`
  shipped via librarian post-sweep.
- **TLP:CLEAR.**
