---
raw_id: raw-2026-05-24-pm-000-sentinel-pre-brief-sweep
collected_at: 2026-05-24T15:32:00-04:00
run_id: pre-brief-20260524-153000
collection_mode: pre_brief_collection
sentinel: true
test: false
sweep_type: pre-brief-afternoon
status: complete
source:
  source_yaml_id: archimedes-internal
  source_name: "Archimedes collector sentinel (15:30 EDT Sunday PM pre-brief sweep — 1 net-new graded-finding-eligible candidate: TrapDoor crypto-stealer multi-ecosystem supply-chain campaign)"
  source_url: null
  published_at: 2026-05-24T15:32:00-04:00
sweep_window:
  start: 2026-05-24T07:30:00-04:00
  end: 2026-05-24T15:30:00-04:00
  duration_h: 8
prior_sweep_anchor:
  brief_id: 2026-05-24-morning
  shipped_at: 2026-05-24T08:00:00-04:00
  flash_anchor: flash-2026-05-24-1200-canonical-scheduled-clean-sweep
  flash_shipped_at: 2026-05-24T12:05:00-04:00
  flash_trigger: none_fired
  notes: |
    Prior anchors are the 08:00 EDT morning brief (commit ff4e308) and the
    12:00 EDT FLASH sentinel (commit d00ba58). The PM pre-brief sweep covers
    the 8h window 2026-05-24T07:30 → 2026-05-24T15:30 EDT spanning the 12:00
    FLASH sentinel — fully reconciled with its evaluation of the Ghost CMS
    CVE-2026-26980 ClickFix campaign (failed all 6 triggers; carried forward
    to PM brief horizon-scanning).
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords:
    - trapdoor_crypto_stealer_multi_ecosystem_supply_chain_socket_origination
    - ghost_cms_cve_2026_26980_clickfix_campaign_carry_forward
    - wireshark_4_6_6_release_one_cve_patched_no_severity_disclosed
    - cisa_kev_catalog_2026_05_22_unchanged_45h_plus_no_new_entries
    - cve_2026_9082_drupal_kev_t_3_anti_noise_locked
    - cve_2026_42897_exchange_kev_t_5_no_msrc_ga_patch
    - cisco_talos_rss_endpoint_recovery_failure_count_reset_3_to_0
    - mandiant_feedburner_23rd_consecutive_404_held_healthy
triage_tags:
  - sentinel
  - one_substantive_raw_signal_written
  - pre_brief_afternoon
  - weekend_afternoon_quiet
  - socket_trapdoor_in_window_handoff_to_grader
  - cisco_talos_rss_recovery_documented
iocs_extracted: false
iocs_count: 0
text_word_count: 1850
promoted: false
rejected_at: 2026-05-24T16:18:00-04:00
rejection_id: reject-2026-05-24-0002
ttl_expires_at: 2026-08-22T15:32:00-04:00
sources_queried:
  - cisa-kev                # WebFetch known_exploited_vulnerabilities.json — catalogVersion 2026.05.22 UNCHANGED, dateReleased 2026-05-22T18:00:11Z, 1,602 total vulnerabilities. Five most-recent entries unchanged: CVE-2026-9082 Drupal (anti-noise locked, KEV due-date 2026-05-27 T-3); CVE-2025-34291 Langflow (absorbed); CVE-2026-34926 Trend Micro Apex One (absorbed); CVE-2008-4250 Microsoft Windows + CVE-2009-1537 Microsoft DirectX (catalog backfill 2026-05-20). ZERO NEW KEV ENTRIES in 45h+ since CVE-2026-9082 added 2026-05-22 18:00 EDT.
  - cisa-advisories         # fetch_feed all.xml — 200 OK, 30 items in feed, 0 in 8h since-filter window.
  - nvd                     # WebFetch services.nvd.nist.gov rest cves 2.0 lastModStartDate=2026-05-24T11:30 lastModEndDate=2026-05-24T15:30 EDT cvssV3Severity=CRITICAL → totalResults=0; HIGH → totalResults=1 (vulnerabilities array empty on probe; pattern consistent with NIST background metadata-refresh). NO new A&D / tracked-vuln / tracked-actor / actively-exploited CVE in window.
  - thehackernews           # fetch_feed feedburner TheHackersNews — 50 items in feed, 0 in 8h window. Front-page WebFetch confirmed top 10 all 2026-05-23 daytime, all corpus-covered or anti-noise locked.
  - bleepingcomputer        # fetch_feed — 15 items in feed, 1 in 8h window: Ghost CMS CVE-2026-26980 SQL-injection ClickFix campaign (Bill Toulas byline, 2026-05-24T14:12:32 UTC — already evaluated by 12:00 FLASH, fails all 6 triggers, carry-forward to PM brief horizon-scanning). Front-page WebFetch added one Sunday-AM post (AdGuard ad-blocker deal, 2026-05-24T12:09 UTC — promotional/commerce, DISCARDED).
  - securityweek            # fetch_feed feedburner — 10 items, 0 in 8h window. Last update 2026-05-23 11:00 UTC pre-window.
  - the-record              # fetch_feed — 5 items in feed, 0 in 8h window.
  - unit42                  # fetch_feed — 15 items, 0 in 8h window. Last update 2026-05-22 19:51 UTC pre-window. Screening Serpens / UNC1549 anti-noise lock expired 06:00; no follow-on Unit 42 publication.
  - mstic                   # fetch_feed microsoft.com/en-us/security/blog/feed — 10 items, 0 in 8h window. Last update 2026-05-22 17:57 UTC pre-window.
  - msrc                    # WebFetch msrc.microsoft.com/blog → 301 redirect to www.microsoft.com/en-us/msrc/blog → 403 forbidden on direct fetch (persistent rendering pattern). No Exchange CVE-2026-42897 GA-patch follow-on detectable from MSRC surface this sweep. KEV due-date 2026-05-29 (T-5 from this sweep).
  - mandiant                # WebFetch cloud.google.com/blog/topics/threat-intelligence — top 5 visible titles UNCHANGED from AM sentinel (GTIG AI Threat Tracker, BlackFile vishing, UNC6692 Snow Flurries, deSouza AI vuln defense, German Cyber Überfall) — all pre-window per prior triangulations. feedburner.com/Mandiant returned 404 again — 23rd consecutive sweep failure tracked.
  - crowdstrike             # skipped this sweep — feed-product-marketing-only pattern persistent
  - cisco-talos             # fetch_feed blog.talosintelligence.com/rss/ — 200 OK RECOVERED (15 items in feed, etag W/6e4f9-vUhizaj3z8NGfDXZMf+KG5BA7OU; top-5 dated 2026-05-21 / 05-19 / 05-19 / 05-14 / 05-14 — all pre-window). RSS endpoint recovery; failure_count reset 3→0; last_successful_fetch updated; last_error cleared.
  - eset-welivesecurity     # fetch_feed feedburner — 100 items in feed, 0 in 8h window. Sunday-afternoon quiet.
  - sentinelone             # fetch_feed sentinelone.com/blog/feed — 200 OK, 0 in-window items. Last_modified 2026-05-22 17:44 UTC pre-window.
  - bitdefender             # WebFetch bitdefender.com/blog/labs — top 5 dated 2026-05-19 / 04-29 / 03-18 / 03-11 / 03-09. All pre-window. Low-frequency vendor cadence.
  - volexity                # WebFetch volexity.com/blog/ — most recent post 2025-12-04. Multi-month cadence; not source-stale.
  - wiz-research            # wiz.io/feed.xml 404 (consistent with prior sweep pattern). Page-fetch fallback productive AM sweep; not re-invoked this PM (top-5 unchanged in 5.5h on this vendor cadence).
  - snyk                    # fetch_feed snyk.io/blog/feed/ — 200 OK, 1628 items in feed, 0 in 8h window. Top entry remains Laravel-Lang Supply Chain Advisory 2026-05-23 (anti-noise locked).
  - socket-dev              # WebFetch socket.dev/blog — IN-WINDOW NET-NEW: TrapDoor crypto stealer supply chain attack multi-ecosystem (npm + PyPI + Crates.io, 34 packages / 384 versions, UNATTRIBUTED, Socket Research Team byline, 2026-05-24T13:32:20Z = 09:32 EDT). RAW-SIGNALED as raw-2026-05-24-pm-001. Other Socket entries unchanged from morning sweep.
  - sophos                  # not directly queried this sweep — news.sophos.com/en-us/feed/ returns 404 per source-health pattern; www.sophos.com/en-us/blog/ surface was AM-sweep-covered with persistent dateless-rendering. No re-invocation this PM.
  - cisco-psirt             # WebFetch sec.cloudapps.cisco.com/security/center/publicationListing.x — template-only render pattern (HTML template placeholders, no actual advisory data exposed). No new Cisco advisories detectable this sweep. Persistent template-render limitation.
  - fortinet-psirt          # WebFetch fortiguard.com/psirt — top 5 advisories all dated 2026-05-12 (FG-IR-26-131 CVE-2025-53680 FortiAP CLI cmd injection; FG-IR-26-137 CVE-2025-67604 FortiAnalyzer/FortiManager API DoS; FG-IR-26-136 CVE-2026-26083 FortiSandbox global authz; FG-IR-26-133 CVE-2025-53870 FortiAP CLI cmd injection; FG-IR-26-123 CVE-2025-53844 FortiOS CAPWAP OOB-access). NO new advisories on 2026-05-23 / 2026-05-24. Quiet Fortinet PSIRT cadence.
  - f5-psirt                # WebFetch my.f5.com/manage/s/article-search-product returned 404 (fourth sweep observation; flagging for source-health first-entry consideration on next pre-brief if pattern persists).
  - proofpoint              # WebFetch proofpoint.com/us/blog — top 5 dated 2026-05-21 / 05-13 / 05-11 / 04-30 / 04-22. All pre-window. Multi-day vendor cadence.
  - dragos                  # WebFetch dragos.com/blog — top 5 dated 2026-05-11 / 05-07 / 05-06 / 04-28 / 04-23. All pre-window. Multi-week vendor cadence.
  - greynoise               # WebFetch greynoise.io/blog — top 5 unchanged from AM sweep. All pre-window. No top-level source-health entry.
  - rapid7                  # fetch_feed rapid7.com/blog/rss — 20 items in feed, 0 in 8h window.
  - isc-sans                # fetch_feed isc.sans.edu/rssfeed.xml — 10 items in feed, 1 in 8h window: Wireshark 4.6.6 release (Didier Stevens 2026-05-24T16:38:21 UTC) — patches 1 vulnerability and 11 bugs, Npcap updated to 1.88. No CVE number disclosed in diary entry; no CVSS; no ITW indicators. DISCARDED per Mode 1 (patch-availability disclosure without severity / actor / exploitation).
  - krebs                   # fetch_feed krebsonsecurity.com/feed — 10 items in feed, 0 in 8h window. Multi-day cadence.
  - dark-reading            # fetch_feed darkreading.com/rss.xml — 50 items in feed, 2 items_after_since_filter but both forward-dated EVENT listings (Infosecurity Europe 2026-06-02; Anatomy of a Data Breach 2026-06-18). Discarded per Mode 1.
  - thedfirreport           # WebFetch thedfirreport.com — top 5 dated 2026-05-11 / 04-22 / 02-23 / 2025-12-17 / 2025-11-04. All pre-window. Multi-month cadence; not source-stale.
  - symantec                # WebFetch security.com/threat-intelligence — top 5 dated 2026-05-16 / 05-12 / 04-23 / 04-22 / 03-20. All pre-window. Multi-week vendor cadence.
  - litespeed-blog          # WebFetch blog.litespeedtech.com — top 5 unchanged from prior sweeps; CVE-2026-48172 vendor advisory 2026-05-21 anti-noise locked. No new updates.
  - drupal-security         # WebFetch drupal.org/security — top 5 unchanged; SA-CORE-2026-004 (CVE-2026-9082) 2026-05-20 anti-noise locked. No new updates.
  - anthropic-news          # WebFetch anthropic.com/news — top 5 May 2026 posts; Project Glasswing initial update 2026-05-22 pre-window (carried forward in morning brief). Glasswing-specific page returned 404 on direct retrieval.
  - reliaquest-blog         # WebFetch reliaquest.com/blog/ — returned Loading placeholder DOM (persistent JS-rendered loading-state pattern, same as 00:00 sentinel observation). No content extractable.
  - x-vxunderground         # WebFetch nitter.net/vxunderground/rss — one in-window tweet at 2026-05-24T15:45:13Z = 11:45 EDT IN WINDOW relaying Socket's TrapDoor disclosure (used as corroborating-primary relay in raw-2026-05-24-pm-001).
  - x-falconfeedsio         # WebFetch nitter.net/falconfeedsio/rss — 6+ tweets in 8h window: ransomware leak posts (Artso/AiLock, DragonForce, NightSpire) + NoName DDoS + Manufacturing whitepaper + DieNet DDoS. NO aerospace/defense watchlist victim named (Lockheed/Boeing/RTX/Northrop/GD/BAE/L3Harris/Leidos/SAIC/Thales/GE Aerospace/Safran/Airbus/Honeywell silent). DISCARDED per Mode 1.
  - x-cisagov               # WebFetch nitter.net/CISAgov/rss — top tweet 2026-05-23T15:19 GMT = 11:19 EDT pre-window; no in-window CISA tweets.
  - socket-twitter          # WebFetch nitter.net/SocketSecurity/rss — Socket vendor X tweet at 2026-05-24T19:05:53Z = 15:05 EDT IN WINDOW announcing TrapDoor disclosure (Socket-own-channel corroboration; follow-up 17:29 EDT post-window added decoy-repo + .cursorrules / CLAUDE.md attempted-injection details into modelcontextprotocol + gemini-cli upstream repos).
  - splunk-archimedes       # mcp__splunk-query | tstats count where (index=archimedes OR index=defenseclaw_local) earliest=-24h@h latest=now by index sourcetype → 27 events all in archimedes index (operation=10 + scheduler=17 self-telemetry). Splunk reachability HEALTHY per mcp__splunk-query__health (Frank, 10.2.2, license OK).
  - splunk-defenseclaw      # Same query — zero events confirmed. First-party telemetry surface dormant; 53rd CONSECUTIVE DORMANT non-self sweep.
  - splunk-targeted-ioc-search  # search (index=archimedes OR index=defenseclaw_local) over -24h with 15 high-priority tokens (CVE-2026-9082, CVE-2026-42897, CVE-2024-12802, CVE-2026-48172, CVE-2026-26980, Ghost CMS, Glasswing, UNC1151, UNC1549, MuddyWater, Charming Kitten, Salt Typhoon, ClickFix, flipboxstudio, parikhpreyash4) returned 5 hits — ALL archimedes pipeline self-references (12:00 FLASH sweep event; morning brief_published event; 00:00 FLASH sweep event; 2026-05-23 18:00 FLASH sweep event; 2026-05-23 PM git_committed event). Pipeline self-references; not external observations. Hard Rule 8: silence is not disconfirming.
sources_querying_skipped_or_deferred:
  - censys                  # no MCP; not queried
  - shodan                  # not queried — no investigation hypothesis warrants paid-tier query this sweep
  - virustotal              # not queried — TrapDoor IOCs not yet promoted; grader may VT-enrich on promotion of raw-2026-05-24-pm-001
  - threatfox               # MCP not built; ABUSECH_API_KEY auth-injection blocked by WebFetch
  - malwarebazaar           # MCP not built; same auth-injection issue
  - palo-alto-psirt         # sample-sweep only (Cisco + Fortinet covered as PSIRT exemplars)
  - ivanti-psirt            # same
  - citrix-psirt            # same
  - sonicwall-psirt         # WebFetch sonicwall.com/support/notices returned navigation-template-only DOM; direct PSIRT portal psirt.global.sonicwall.com/vuln-list returned "Security Advisory" header without advisory data. SonicWall PSIRT not productively scrapable this sweep. CVE-2024-12802 status check via SonicWall surface DEFERRED.
  - vmware-broadcom-psirt   # sample-sweep only
  - x-gossithedog           # stale per source-health.yaml (4 consecutive failures since 2026-05-09); nitter.net/GossiTheDog/rss returned 404 again confirming stale flip persists
splunk_first_party_check:
  query: "| tstats count where (index=archimedes OR index=defenseclaw_local) earliest=-24h@h latest=now by index sourcetype"
  archimedes_index_events_24h: 27          # self-telemetry only (operation=10 + scheduler=17)
  defenseclaw_local_events_24h: 0
  splunk_first_party_dormant: true
  consecutive_dormant_sweeps: 53           # incremented from 52 in prior 12:00 FLASH sentinel
  ioc_match_opportunity: false
  hard_rule_8_framing: "Silence is not disconfirming, not confirming. First-party index dormant non-self pattern continues (53rd consecutive sweep)."
filter_evaluation_summary:
  in_window_items_total: 4                 # TrapDoor (substantive); Ghost CMS (12:00 FLASH-evaluated, carry-forward); Wireshark 4.6.6 (discarded); BleepingComputer AdGuard deal (discarded)
  in_window_items_corpus_covered: 1        # Ghost CMS already evaluated by 12:00 FLASH sentinel; carry-forward to PM brief horizon-scanning at most (not raw-signaled separately this sweep)
  in_window_items_filtered_out: 2          # Wireshark 4.6.6 patch-availability without severity / actor / exploitation; BleepingComputer AdGuard ad-blocker deal (promotional/commerce)
  in_window_items_new_to_corpus: 1         # TrapDoor crypto stealer multi-ecosystem (raw-2026-05-24-pm-001 written)
  rejection_basis:
    - "Wireshark 4.6.6 release (ISC SANS Didier Stevens 2026-05-24T16:38:21Z): DISCARDED per Mode 1 — release patches 1 vulnerability and 11 bugs but diary entry does NOT identify CVE number, CVSS severity, or in-the-wild exploitation. Patch-availability disclosure without severity / actor / exploitation does not meet graded-finding-eligibility threshold."
    - "BleepingComputer AdGuard ad-blocker deal (2026-05-24T12:09 UTC): DISCARDED per Mode 1 — promotional/commerce, not threat-intel."
    - "GhostCMS CVE-2026-26980 ClickFix campaign (BleepingComputer Bill Toulas 2026-05-24T14:12:32Z): already evaluated by 12:00 FLASH sentinel — fails all 6 triggers (T1: CVE patched 3 months ago 2026-02-19 in 6.19.1, not fresh; T2: no tracked actor named, XLab + SentinelOne stop at 'two distinct activity clusters'; T3: defenseclaw_local dormant; T4: no tracked actor; T5: 700+ victim domains across universities/DuckDuckGo/AI-SaaS/media/fintech/blogs with NO A&D-named entity; T6: patched). Carry-forward to PM brief horizon-scanning at most; NOT raw-signaled separately this sweep (carry-forward via 12:00 FLASH sentinel record)."
hard_rules_compliance:
  rule_2_no_attribution_origination: |
    TrapDoor preserved as UNATTRIBUTED per Socket explicit decline-to-attribute.
    Attacker-self-described "Universal AI Agent Extraction Framework" framing
    preserved as Socket-reported attacker-own framing embedded in trap-core.js
    payload; NOT propagated as a Socket attribution and NOT cross-walked to any
    tracked actor in _roster.yaml (specifically NOT TeamPCP, NOT Shai-Hulud,
    NOT Mini Shai-Hulud despite operational adjacency to the same ecosystem
    class). Ghost CMS CVE-2026-26980 ClickFix campaign preserved as
    XLab + SentinelOne reporting "two distinct activity clusters" with NO
    tracked-roster-actor cross-walk. ISC SANS Wireshark release preserved as
    Wireshark Foundation vendor self-disclosure without ITW or actor framing.
  rule_3_no_exploitation: |
    No PoC code, no payloads, no exploit guides referenced. TrapDoor IOC list
    in raw-2026-05-24-pm-001 contains payload filename (trap-core.js), byte
    size (48,485 bytes), and XOR key (cargo-build-helper-2026) ONLY because
    Socket published these as IOCs; not reproduced as part of an exploitation
    walkthrough. CVE references throughout (CVE-2026-9082, CVE-2026-42897,
    CVE-2024-12802, CVE-2026-48172, CVE-2026-26980) are descriptive only.
  rule_4_passive_only: |
    No active scans invoked. SpiderFoot not invoked. authorized-targets.yaml
    empty (confirmed via re-read this sweep). All source queries are passive
    OSINT against third-party publishers (vendor blogs, news outlets, NVD,
    CISA KEV, RSS feeds via fetch_feed MCP) and first-party Splunk over the
    archimedes/defenseclaw_local indices.
  rule_6_quote_limit: |
    No source quotes >15 words used this sweep. The only string preserved
    verbatim from a source is the attacker-self-described 6-word phrase
    "Universal AI Agent Extraction Framework" embedded in TrapDoor's
    trap-core.js payload (Socket-reported; preserved per Hard Rule 2 as
    attacker-own framing, used once in raw-2026-05-24-pm-001).
  rule_7_credentials: |
    No credential exposure surfaced this window. TrapDoor disclosure scope-
    describes the stealer's credential targeting (SSH keys, Sui/Solana/Aptos
    wallets, AWS credentials, GitHub tokens, browser data, env vars, API
    keys, local dev configs) without naming any victim credentials.
  rule_8_splunk_first_party_priority: |
    defenseclaw_local 0 events in -24h (53rd consecutive dormant non-self
    sweep). Targeted IOC keyword sweep across 15 high-priority tokens returned
    5 hits, all archimedes pipeline self-references. Silence is not
    disconfirming per established cadence.
source_health_changes:
  - source_yaml_id: mandiant
    observation: |
      feedburner.com/Mandiant returned 404 — 23rd consecutive sweep with this
      failure mode. cloud.google.com/blog/topics/threat-intelligence index
      page WebFetch returned same top-5 visible titles as AM sentinel.
    runtime_change_applied: |
      failure_count cumulative 21→22; last_error timestamp updated to
      2026-05-24T15:30 PM pre-brief; status held healthy per existing operator
      policy (held healthy pending operator alt-endpoint decision);
      operator-set notes field preserved verbatim.
  - source_yaml_id: cisco-talos
    observation: |
      blog.talosintelligence.com/rss/ returned 200 OK this sweep — RSS endpoint
      RECOVERY (different path from the previously-failing
      blog.talosintelligence.com/feeds/posts/default Atom endpoint). 15 items
      in feed total; top-5 dated 2026-05-21 / 05-19 / 05-19 / 05-14 / 05-14.
    runtime_change_applied: |
      failure_count RESET 3→0; status: healthy (continued); last_error CLEARED;
      last_successful_fetch UPDATED to 2026-05-24T15:30:00-04:00; operator-set
      notes field preserved verbatim. Operator action: consider updating
      source-health notes to formally document that /rss/ is the working
      endpoint and /feeds/posts/default Atom endpoint is deprecated.
carry_forward_items_for_afternoon_brief:
  - id: trapdoor-crypto-stealer-multi-ecosystem-npm-pypi-crates-socket-unattributed
    type: graded_finding_candidate
    summary: |
      TrapDoor multi-ecosystem (npm + PyPI + Crates.io) crypto-stealer
      supply-chain campaign — Socket Research Team byline, 2026-05-24T13:32:20Z
      (09:32 EDT IN WINDOW). 34 packages / 384 versions across three
      ecosystems (21 npm + 7 PyPI + 6 Crates.io); attacker accounts
      ddjidd564 (GitHub) + asdxzxc (npm); GitHub Pages dead-drop
      ddjidd564.github.io/defi-security-best-practices/; payload trap-core.js
      (48,485 bytes) XOR-obfuscated with key cargo-build-helper-2026; campaign
      marker P-2024-001; persistence via .cursorrules / CLAUDE.md / Git hooks
      / shell hooks / systemd / cron / SSH; credential exfil scope includes
      SSH keys + Sui/Solana/Aptos wallets + AWS credentials + GitHub tokens
      + browser data + env vars + API keys + local dev configs. UNATTRIBUTED
      per Socket explicit decline. NO A&D-direct victim. First documented
      three-ecosystem simultaneous-publication pattern in Archimedes corpus.
      The .cursorrules + CLAUDE.md AI-agent-persistence vector is novel
      relative to prior corpus-tracked supply-chain campaigns (Mini Shai-
      Hulud, node-ipc, Laravel-Lang, Packagist 8-pkg). Raw-signaled as
      raw-2026-05-24-pm-001. Single-source veto applies on novelty claims;
      no cross-vendor corroboration in window (Snyk, StepSecurity, Aikido,
      SafeDep, Wiz Research, Unit 42 npm threat landscape all silent).
      Recommendation: grader cluster TrapDoor as a Supply Chain Watch
      finding candidate; analyst SAT-ACH for the novelty + targeting-
      adjacency to crypto-developer-targeted ecosystem with AI-agent-config
      persistence; red-team review for the "first documented three-ecosystem
      simultaneous-publication" framing (Socket-single-source layer).
  - id: ghost-cms-cve-2026-26980-clickfix-campaign-xlab-sentinelone
    type: horizon_scanning_carry_forward
    summary: |
      Ghost CMS CVE-2026-26980 SQL-injection ClickFix campaign (BleepingComputer
      Bill Toulas 2026-05-24T14:12:32Z, source-chain XLab/Qianxin + SentinelOne).
      700+ domains compromised across universities (Harvard/Oxford/Auburn),
      DuckDuckGo, AI/SaaS, media, fintech, blogs. Patched 2026-02-19 in 6.19.1.
      NO A&D-named victim. NO tracked actor named (XLab + SentinelOne stop at
      "two distinct activity clusters"). Already evaluated by 12:00 FLASH
      sentinel — fails all 6 triggers. Tradecraft interest: CMS-supply-chain-
      via-vulnerable-install pattern + ClickFix social-engineering downstream.
      Carry-forward to PM brief horizon-scanning block at most. NOT FLASH-tier.
      NOT raw-signaled separately this sweep (carry-forward via 12:00 FLASH
      sentinel record).
  - id: cve-2026-9082-drupal-kev-due-date-t-3
    type: kev_deadline_awareness
    summary: |
      CVE-2026-9082 Drupal Core SQL injection KEV federal due-date is
      2026-05-27 — T-3 from this sweep (calendar advance from morning
      brief's T-3 framing — deadline is Wednesday). Already in morning brief
      action-item block; carry into PM brief KEV-deadline action-item
      reinforcement. Topic anti-noise locked.
  - id: cve-2026-42897-exchange-kev-due-date-t-5
    type: kev_deadline_awareness
    summary: |
      VT-008 Exchange CVE-2026-42897 KEV federal due-date 2026-05-29 — T-5
      from this sweep (calendar advance from morning brief's T-5 framing —
      deadline is Friday). No MSRC GA-patch in window (MSRC blog surface
      continues template-only / 403 rendering pattern). ESU-only patch path
      plus EEMS / EOMT mitigation continues. PM brief KEV-deadline action-item
      block candidate.
notes:
  - "One substantive graded-finding-eligible item in 8h window: TrapDoor crypto stealer multi-ecosystem (npm + PyPI + Crates.io) supply-chain campaign disclosed by Socket Research Team at 2026-05-24T13:32:20Z (09:32 EDT IN WINDOW). UNATTRIBUTED per Socket explicit decline; NO A&D-direct victim; fails all 6 FLASH triggers but qualifies for Supply Chain Watch narrative consideration. Raw-signaled as raw-2026-05-24-pm-001."
  - "Source health: mandiant feedburner 23rd consecutive 404 (failure_count cumulative 21→22 per AM diff-summary cadence); cisco-talos RSS endpoint RECOVERED (blog.talosintelligence.com/rss/ returned 200 OK — different path from the failing /feeds/posts/default Atom endpoint; failure_count reset 3→0; last_successful_fetch updated; last_error cleared)."
  - "Splunk first-party telemetry: archimedes self-audit events only (27 in -24h, operation=10 + scheduler=17). Zero defenseclaw_local events = 53rd consecutive dormant non-self sweep. IOC-match opportunity remains structurally zero. Hard Rule 8 framing: silence is not disconfirming."
  - "Anti-noise locks: All 8 morning-brief-relevant locks remain anti-noise locked or carried-forward (UNC1549 Screening Serpens, LiteSpeed CVE-2026-48172, Laravel-Lang flipboxstudio, Packagist 8-pkg, npm 2FA staged, CVE-2026-9082 Drupal, Russian Kosmos 2610-2613 ICEYE, CISA KEV nomination form). KEV-deadline items remain in morning brief action-item block; T-3 (Drupal CVE-2026-9082) and T-5 (Exchange CVE-2026-42897) carry forward to PM brief."
  - "CISA KEV catalog version 2026.05.22 UNCHANGED across 45h+ — no new KEV adds since CVE-2026-9082 added 2026-05-22 18:00 EDT. No update on CVE-2026-9082 or CVE-2026-42897 status. CVE-2026-48172 LiteSpeed (FLASH-0002 yesterday) NOT added to KEV — Mandiant / Volexity / Unit 42 / GreyNoise / MSTIC silent on independent telemetry corroboration; single-source veto on LiteSpeed active-exploitation-ITW claim continues to hold per AM brief framing."
  - "Glasswing AI: morning brief's Anthropic Project Glasswing carry-forward acknowledged via PM-sweep observation that the Glasswing initial-update post is dated 2026-05-22 (pre-window). The 2026-05-24 Weekly Synthesis (Sunday 10:00 EDT, T-3.5h from this sweep) is the canonical consolidation surface for AI-vulnerability-discovery thread material (Glasswing + Rapid7 Q1 + GreyNoise 119k IPs)."
  - "SonicWall CVE-2024-12802 status check: SonicWall PSIRT portal (psirt.global.sonicwall.com/vuln-list) returned 'Security Advisory' header without advisory data; sonicwall.com/support/notices returned navigation-template-only DOM. CVE-2024-12802 SonicWall surface status check DEFERRED. ReliaQuest blog persistent loading-placeholder DOM precludes ReliaQuest-side update detection. No fresh material on the 2026-05-20 1800 FLASH SonicWall MFA bypass ITW item this sweep."
  - "UNC1151 / Ghostwriter: no fresh A-grade attribution material in window. Pattern signal stable; morning-brief carry-forward stance unchanged. /new-actor candidacy remains at operator's discretion."
  - "Quiet-hours posture: 15:32 EDT is INSIDE 09:00-21:00 active window. Pre-brief collection does NOT post to Discord regardless of quiet hours status. The 16:00 afternoon-brief composition consumes this sweep's TrapDoor candidate + carry-forwards. The PM brief publishes to #intel-briefs at 16:00 EDT (T+28min)."
  - "Critical-override conditions NOT met across any in-window item — no CVSS 10.0 + confirmed active exploitation + tracked actor + A&D watchlist coincidence on TrapDoor or any other in-window item. Moot for pre-brief collection (no FLASH-tier promotion gate applies)."
  - "Briefer/orchestrator action: 16:00 PM brief composition proceeds with ONE substantive carry-forward (TrapDoor multi-ecosystem supply-chain campaign) plus carry-forwards from morning (UNC1151 monitoring, Glasswing AI, KEV deadlines T-3 Drupal / T-5 Exchange, Iran Cyber Watch retrospective context). Supply Chain Watch standing-section accumulating noteworthy density (Mini Shai-Hulud / node-ipc / Laravel-Lang / Packagist 8-pkg / TrapDoor across 14 days — pattern-of-the-month framing candidate)."
---

# 15:30 EDT Sunday PM pre-brief sweep — ONE NET-NEW GRADED-FINDING-ELIGIBLE ITEM

This sentinel record documents the 2026-05-24 15:30 EDT PM pre-brief
collection sweep. Window: 2026-05-24T07:30 to 2026-05-24T15:30 EDT (8h).

## Sweep outcome

**ONE net-new graded-finding-eligible item in the 8h window:** Socket's
**TrapDoor crypto-stealer multi-ecosystem supply-chain campaign** —
disclosed at 2026-05-24T13:32:20Z (09:32 EDT IN WINDOW) — raw-signaled
separately as `raw-2026-05-24-pm-001-socket-trapdoor-crypto-stealer-multi-ecosystem-npm-pypi-crates-34-packages-384-versions.md`.

**UNATTRIBUTED** per Socket explicit decline-to-attribute. **34 packages /
384 versions** across **three ecosystems simultaneously** (21 npm + 7 PyPI +
6 Crates.io). **First documented three-ecosystem simultaneous-publication
pattern in Archimedes corpus.** **NO A&D-direct victim**; target sectors
are crypto / DeFi / Solana / Sui / Aptos / AI / security developers.
**Novel persistence vector:** `.cursorrules` + `CLAUDE.md` AI-agent-config
file injection (relative to prior corpus-tracked supply-chain campaigns —
Mini Shai-Hulud / node-ipc / Laravel-Lang / Packagist 8-pkg). **Fails all
6 FLASH triggers** (no CVE / no tracked actor / no A&D / no first-party
hit / not a TTP-change-for-tracked-actor / not a zero-day-no-patch).
**Supply Chain Watch narrative candidate** for the 16:00 PM brief.

Three other in-window items were evaluated and dispositioned:
- **Ghost CMS CVE-2026-26980 ClickFix campaign** (BleepingComputer
  Bill Toulas 14:12 UTC) — already evaluated by 12:00 FLASH sentinel,
  fails all 6 triggers, carry-forward to PM brief horizon-scanning
  block at most. NOT raw-signaled separately this sweep.
- **Wireshark 4.6.6 release** (ISC SANS Didier Stevens 16:38 UTC) —
  patches 1 vulnerability and 11 bugs; diary entry does NOT identify
  CVE number, CVSS severity, or in-the-wild exploitation. DISCARDED
  per Mode 1.
- **BleepingComputer AdGuard ad-blocker deal** (12:09 UTC) —
  promotional/commerce. DISCARDED.

## One-paragraph summary

The 15:30 PM pre-brief sweep surfaced one substantive net-new
graded-finding-eligible item: Socket Research Team's **TrapDoor**
multi-ecosystem supply-chain campaign disclosure (Socket Research Team
byline, 2026-05-24T13:32:20Z — 09:32 EDT IN WINDOW; published to
socket.dev/blog as `trapdoor-crypto-stealer-npm-pypi-crates`). The campaign
is UNATTRIBUTED per Socket's explicit decline (specifically NOT TeamPCP /
Shai-Hulud / Mini Shai-Hulud), spans **34 packages and 384+ versions**
across **three ecosystems simultaneously** (21 npm + 7 PyPI + 6 Crates.io),
and constitutes the **first documented three-ecosystem simultaneous-
publication pattern in the Archimedes corpus** (Mini Shai-Hulud =
dual-ecosystem npm+PyPI; node-ipc / Laravel-Lang / Packagist 8-pkg = single
ecosystem each). Target sectors are crypto / DeFi / Solana / Sui / Aptos /
Move-lang / AI / security developers — **NO A&D-direct victim**. Attacker
identities are GitHub `ddjidd564` (also hosts dead-drop on
`ddjidd564.github.io/defi-security-best-practices/`) and npm `asdxzxc`;
payload is `trap-core.js` (48,485 bytes) XOR-obfuscated with key
`cargo-build-helper-2026`; campaign marker `P-2024-001` embedded; self-
described as "Universal AI Agent Extraction Framework" (attacker's own
framing, preserved verbatim per Hard Rule 2). The **novel persistence
vector** mixes `.cursorrules` + `CLAUDE.md` AI-agent-config-file injection
alongside standard Git hooks / shell hooks / systemd / cron / SSH; the AI-
agent-config persistence pattern is novel relative to prior corpus-tracked
supply-chain campaigns. Credential exfil scope spans SSH keys + Sui/Solana/
Aptos wallets + AWS credentials + GitHub tokens + browser data + env vars +
API keys + local dev configs. Socket-own follow-up at 17:29 EDT (post-window
— flagged for next-sweep verification) reports that the attacker
additionally attempted to inject malicious configurations into
`modelcontextprotocol` and `gemini-cli` upstream repositories — riskiest
content-injection claim, Hard Rule 2 sensitive. Single-source veto applies
on novelty + three-ecosystem-first claims (no cross-vendor corroboration
in window from Snyk / StepSecurity / Aikido / SafeDep / Wiz Research /
Unit 42 npm threat landscape). Three other in-window items dispositioned:
Ghost CMS CVE-2026-26980 ClickFix campaign (12:00 FLASH-evaluated, fails
all 6 triggers, PM brief horizon-scanning carry-forward); Wireshark 4.6.6
release (no CVE / no severity / no ITW disclosed, DISCARDED); BleepingComputer
AdGuard ad-blocker deal (promotional/commerce, DISCARDED). CISA KEV catalog
version 2026.05.22 UNCHANGED across 45h+ — no new KEV adds since
CVE-2026-9082 (Drupal) added 2026-05-22 18:00 EDT. NVD CRITICAL-window
query returned 0 entries; HIGH-window returned 1 but empty array (NIST
background metadata-refresh pattern). Tracked-actor surfaces (Unit 42,
Mandiant/GTIG, MSTIC, ESET, CrowdStrike threat-research, Volexity, Talos,
SentinelLabs, Sophos, Bitdefender, Wiz, Proofpoint, Dragos, Symantec) all
quiet across the 8h window. Vendor PSIRTs quiet (Cisco PSIRT template-
only render, Fortinet PSIRT top-5 all 2026-05-12 unchanged). Two source-
health changes: mandiant feedburner 23rd consecutive 404 (cumulative
21→22); **cisco-talos RSS endpoint RECOVERED** (blog.talosintelligence.com/
rss/ returned 200 OK — different path from failing /feeds/posts/default
Atom endpoint; failure_count reset 3→0; status remains healthy; last_error
cleared; last_successful_fetch updated). Splunk first-party check confirmed
zero `defenseclaw_local` events in -24h — 53rd consecutive dormant non-self
sweep. Five non-FLASH carry-forwards for the 16:00 PM brief: TrapDoor
multi-ecosystem supply-chain (Supply Chain Watch standing-section finding
candidate); Ghost CMS CVE-2026-26980 ClickFix campaign (horizon-scanning);
CVE-2026-9082 Drupal KEV deadline T-3 (Wednesday); VT-008 Exchange
CVE-2026-42897 KEV deadline T-5 (Friday); Glasswing AI / Anthropic
2026-05-22 update (Weekly Synthesis is the canonical surface today
10:00 EDT, T-3.5h pre-this-sweep).

## Source health changes

- **mandiant** — feedburner 23rd consecutive 404; cumulative
  `failure_count` 21→22 (AM diff-summary applied 19→21 to cover 00:00 +
  06:00 + 07:30 sweep observations; this PM sweep applies 21→22); status
  held healthy per long-standing operator policy (alt-endpoint decision
  pending); operator-set `notes` field preserved verbatim.
- **cisco-talos** — RECOVERY. `blog.talosintelligence.com/rss/` returned
  200 OK this sweep with 15 items in feed (top-5 dated 2026-05-21 /
  05-19 / 05-19 / 05-14 / 05-14). This is a **different endpoint path**
  from the previously-failing `/feeds/posts/default` Atom endpoint.
  `failure_count` RESET 3→0; status remains healthy; `last_error` CLEARED;
  `last_successful_fetch` UPDATED to 2026-05-24T15:30:00-04:00; operator-set
  `notes` preserved verbatim. **Operator action:** consider updating
  source-health notes to formally document `/rss/` as the working
  endpoint and `/feeds/posts/default` Atom endpoint as deprecated.

All other surveyed sources reachable; persistent vendor-pattern
observations match prior-sweep baselines (CrowdStrike dateless marketing
items, Sophos dateless cards, MSRC 403 rendering, ESET multi-day cadence,
Volexity multi-month cadence, Dragos multi-week cadence, Krebs multi-day
weekend cadence, Symantec multi-week cadence). F5 my.f5.com/manage/s/article-
search-product 404 (fourth observation; flagging for first-entry consideration
next pre-brief).

## Splunk first-party check

Query: `| tstats count where (index=archimedes OR index=defenseclaw_local) earliest=-24h@h latest=now by index sourcetype`

Result: 27 events in `archimedes` index (operation=10 + scheduler=17 self-
telemetry only). **ZERO `defenseclaw_local` events** in -24h — **53rd
consecutive dormant non-self sweep**. No IOC-match opportunity exists
structurally on this sweep cycle.

Splunk reachability **HEALTHY** per `mcp__splunk-query__health`
(Frank, 10.2.2, license OK).

Targeted IOC keyword sweep across 15 high-priority tokens (CVE-2026-9082,
CVE-2026-42897, CVE-2024-12802, CVE-2026-48172, CVE-2026-26980, "Ghost CMS",
Glasswing, UNC1151, UNC1549, MuddyWater, "Charming Kitten", "Salt Typhoon",
ClickFix, flipboxstudio, parikhpreyash4) returned 5 hits — ALL Archimedes
pipeline self-references (12:00 FLASH sweep event; morning brief_published
event; 00:00 FLASH sweep event; 2026-05-23 18:00 FLASH sweep event; 2026-05-23
PM git_committed event). No external observations.

## Quiet-hours and FLASH-trigger posture (informational)

- 15:32 EDT falls within 09:00-21:00 active window (window ends at 21:00
  EDT, T+5.5h from this sweep).
- Pre-brief collection does NOT post to Discord regardless of quiet
  hours status — sentinel + collection summary feed the 16:00 PM brief
  which the briefer composes and ships to `#intel-briefs`.
- Critical-override conditions (CVSS 10.0 + confirmed active exploitation
  + tracked actor + A&D watchlist hit, all four simultaneously) NOT met on
  any in-window item — TrapDoor has no CVE / no tracked actor / no A&D;
  Ghost CMS CVE-2026-26980 is patched 3 months ago; Wireshark 4.6.6 has
  no severity disclosed. Moot for pre-brief collection.

## Carry-forwards to 16:00 PM brief

1. **TrapDoor multi-ecosystem supply-chain campaign** — Socket-disclosed
   2026-05-24T13:32:20Z (09:32 EDT IN WINDOW), raw-signaled as
   `raw-2026-05-24-pm-001`. 34 packages / 384 versions / 3 ecosystems
   (npm + PyPI + Crates.io); UNATTRIBUTED per Socket explicit decline;
   NO A&D-direct victim. **Supply Chain Watch standing-section finding
   candidate.** Grader should consider cluster framing (first three-
   ecosystem simultaneous-publication in corpus; .cursorrules + CLAUDE.md
   novel AI-agent-config persistence vector; crypto-developer-narrow
   targeting distinct from Mini Shai-Hulud's broad maintainer-enumeration).
   Single-source veto applies on novelty claims (Socket sole originating
   primary; vx-underground tweet and Socket-own X account are extensions,
   not independent corroboration). Analyst should SAT-ACH the targeting-
   adjacency (crypto-developer + AI-agent-config persistence + Solana/Sui/
   Aptos Move-lang ecosystem) and the operational template the .cursorrules
   / CLAUDE.md injection vector represents for any future AI-assisted-
   development SDLC target. Red-team should challenge the "first documented
   three-ecosystem simultaneous-publication" framing (single-source novelty
   layer) and the riskiest content-injection claim (post-window Socket
   addendum about `modelcontextprotocol` and `gemini-cli` upstream-repo
   attempted-injection — Hard Rule 2 sensitive).

2. **Ghost CMS CVE-2026-26980 ClickFix campaign** — BleepingComputer
   Bill Toulas 2026-05-24T14:12:32Z, source-chain XLab/Qianxin +
   SentinelOne. 700+ domains compromised across universities (Harvard /
   Oxford / Auburn) / DuckDuckGo / AI-SaaS / media / fintech / blogs.
   Patched 2026-02-19 in Ghost 6.19.1. NO A&D-named victim; NO tracked
   actor named. Already evaluated by 12:00 FLASH sentinel — fails all
   6 triggers. **Horizon-scanning block at most.** Tradecraft interest:
   CMS-supply-chain-via-vulnerable-install pattern + ClickFix social-
   engineering downstream. NOT raw-signaled separately this sweep
   (carry-forward via 12:00 FLASH sentinel record).

3. **CVE-2026-9082 Drupal KEV deadline T-3** (Wednesday 2026-05-27).
   Topic anti-noise locked; already in morning brief action-item block;
   carry into PM brief KEV-deadline action-item reinforcement.

4. **VT-008 Exchange CVE-2026-42897 KEV deadline T-5** (Friday
   2026-05-29). No MSRC GA-patch in window; ESU-only + EEMS/EOMT
   mitigation path continues. Already in morning brief action-item
   block; carry into PM brief KEV-deadline action-item reinforcement.

5. **Glasswing AI / Anthropic 2026-05-22 update** — carry-forward
   from morning brief. The 2026-05-24 Weekly Synthesis (Sunday 10:00 EDT,
   T-3.5h pre-this-sweep) is the canonical consolidation surface for the
   AI-vulnerability-discovery thread alongside Rapid7 Q1 and GreyNoise
   119k IPs analysis. PM brief reference at most.

## Hard Rules compliance

- **Rule 2** (no Archimedes-originated attribution): TrapDoor preserved
  as UNATTRIBUTED per Socket explicit decline; "Universal AI Agent
  Extraction Framework" attacker-self-description preserved verbatim as
  Socket-reported attacker-own framing embedded in `trap-core.js`. NOT
  cross-walked to TeamPCP / Shai-Hulud / Mini Shai-Hulud despite
  operational adjacency. Ghost CMS CVE-2026-26980 preserved as XLab +
  SentinelOne "two distinct activity clusters" with NO tracked-actor
  cross-walk.
- **Rule 3** (no exploitation content): no PoC code, no payloads, no
  exploit guides referenced. TrapDoor `trap-core.js` filename + byte
  size + XOR key disclosed as published-Socket-IOCs only, not as
  exploitation walkthrough. All CVE references descriptive.
- **Rule 4** (passive only): no active scans, SpiderFoot not invoked,
  `authorized-targets.yaml` empty (re-read confirmed this sweep). All
  source queries are passive OSINT against third-party publishers and
  first-party Splunk over the archimedes / defenseclaw_local indices.
- **Rule 6** (15-word quote limit): no source quotes >15 words used.
  Only verbatim phrase preserved is attacker-self-described 6-word
  "Universal AI Agent Extraction Framework" embedded in TrapDoor's
  payload (Socket-reported attacker-own framing, used once).
- **Rule 7** (credentials radioactive): no credential exposure surfaced.
  TrapDoor disclosure scope-describes credential targeting without
  naming any victim credentials.
- **Rule 8** (Splunk first-party): `defenseclaw_local` 0 events in -24h
  (53rd consecutive dormant non-self sweep). Silence is not disconfirming.

## Disposition

- **No Discord post** — pre-brief sweeps do not post to Discord; the
  16:00 PM brief composition consumes this sentinel + TrapDoor candidate
  + carry-forwards.
- **Two raw-signal files written this sweep:** the TrapDoor candidate
  (`raw-2026-05-24-pm-001-socket-trapdoor-...`) and this sentinel
  (`raw-2026-05-24-pm-000-sentinel-pre-brief-sweep`).
- **No grading performed** — collector does not grade; grader-handoff
  on TrapDoor candidate for 16:00 brief composition.
- **No `_master-index.yaml` regeneration** — collector does not regenerate
  the IOC master index; librarian regenerates on TrapDoor promotion.
- **Source-health updates applied:** mandiant cumulative failure_count
  21→22; cisco-talos RECOVERED (failure_count 3→0, last_successful_fetch
  updated, last_error cleared); runtime fields only; operator-set notes
  preserved verbatim per source-health-yaml-field-ownership rule.
- **Splunk HEC telemetry** `event_type=pre_brief_collection` to be shipped
  via librarian post-sweep.
- **TLP:CLEAR.**
