---
raw_id: raw-2026-05-25-pm-000-sentinel-pre-brief-sweep
collected_at: 2026-05-25T15:35:00-04:00
run_id: pre-brief-20260525-153000
collection_mode: pre_brief_collection
sentinel: true
test: false
sweep_type: pre-brief-afternoon
status: complete
source:
  source_yaml_id: archimedes-internal
  source_name: "Archimedes collector sentinel (15:30 EDT Monday pre-brief sweep — 2 net-new raw-signal companions; 0 FLASH-trigger fires; TeamPCP TTP-expansion consolidation + Russia-hosting LE takedown)"
  source_url: null
  published_at: 2026-05-25T15:35:00-04:00
sweep_window:
  start: 2026-05-25T07:30:00-04:00
  end: 2026-05-25T15:30:00-04:00
  duration_h: 8
prior_sweep_anchor:
  brief_id: flash-2026-05-25-1200-canonical-scheduled-clean-sweep
  shipped_at: 2026-05-25T12:05:00-04:00
  trigger: none_fired
  notes: |
    Prior sweep was the 2026-05-25 12:00 EDT Monday-noon FLASH sentinel
    (commit d647c85). Zero in-window FLASH-trigger fires. Three in-window
    items at noon all anti-noise-locked or out-of-scope (Ghost CMS THN +
    SW relay, Kali365 BleepingComputer, Krebs Netherlands flagged for
    16:00 PM-brief carry-forward, Check Point weekly report restating
    corpus-anchored items). This PM pre-brief sweep covers 2026-05-25T07:30
    → 15:30 EDT (8h), overlapping the 12:00 FLASH (commit d647c85) sweep
    boundary and feeding the 16:00 EDT afternoon brief.
match_reason:
  watchlist: []                  # No A&D-prime named victims in any in-window item
  actors: ["001"]                # TeamPCP via SANS ISC Hartman consolidation (corpus-tracked since 2026-03-18; multiple TTP additions through 2026-05-24)
  vulnerabilities: ["VT-006", "VT-008", "VT-007"]    # CVE-2026-45321 Mini Shai-Hulud carry-forward + CVE-2026-42897 Exchange KEV T-4 + CVE-2026-9082 Drupal KEV T-2
  keywords: ["TeamPCP", "Shai-Hulud", "framework leak", "durabletask", "Linux disk wiper", "Russian hosting", "Stark Industries", "MIRhosting", "WorkTitans", "PQHosting"]
triage_tags: [sentinel, pre_brief_afternoon, monday_afternoon, two_raw_signal_companions, teampcp_ttp_consolidation, russia_hosting_takedown]
iocs_extracted: false           # IOCs extracted in companion raw-signal files pm-001 and pm-002
iocs_count: 0
text_word_count: 1900
promoted: false
rejected_at: 2026-05-25T16:00:00-04:00
rejection_id: reject-2026-05-25-0004
ttl_expires_at: 2026-08-23T15:35:00-04:00

sources_queried:
  - cisa-kev                # WebFetch known_exploited_vulnerabilities.json — catalogVersion 2026.05.22 UNCHANGED, dateReleased 2026-05-22T18:00:11.5035Z. ZERO net-new KEV adds since AM and 12:00 sentinels (now 69h+ since last add CVE-2026-9082 Drupal 2026-05-22 EDT). Five most-recent unchanged: CVE-2026-9082 Drupal (2026-05-22, due 2026-05-27 = T-2), CVE-2025-34291 Langflow (2026-05-21, due 2026-06-04), CVE-2026-34926 Trend Micro Apex One (2026-05-21, due 2026-06-04), CVE-2008-4250 Windows MS08-067 (2026-05-20, due 2026-06-03), CVE-2009-1537 DirectX MS09-028 (2026-05-20, due 2026-06-03). KEV deadlines T-2 Drupal CVE-2026-9082 (2026-05-27 Wed EOB) and T-4 Exchange CVE-2026-42897 (2026-05-29) carry forward at peak urgency for 16:00 PM brief.
  - cisa-advisories         # fetch_feed cisa.gov/cybersecurity-advisories/all.xml — 200 OK, 30 items in feed, ZERO in-window 8h since-filter. Direct page WebFetch returned 403 (consistent WAF persistent pattern; all.xml remains productive endpoint). No fresh ICS-CERT batch in window.
  - nvd                     # WebFetch services.nvd.nist.gov rest/json/cves/2.0 lastModStartDate=2026-05-25T11:30 lastModEndDate=2026-05-25T15:30 EDT cvssV3Severity=CRITICAL → totalResults=2, resultsPerPage=0, empty array. NVD result-pagination quirk PERSISTS (same condition documented in AM sentinel — totalResults non-zero but empty vulnerabilities[]). Cannot trigger-evaluate without ID-level resolution. Carry-forward to vuln-tracker if any morning grader-tier item warrants direct UI-side lookup. Not a stale flip (endpoint reachable, semantic quirk only).
  - thehackernews           # fetch_feed feedburner — 50 items in feed; 3 in 8h since-filter window: (1) Weekly Recap 2026-05-25 14:13 UTC = 10:13 EDT — aggregator-tier digest of corpus-already-covered content, DISCARDED (consistent with 12:00 sentinel). (2) Ghost CMS CVE-2026-26980 QiAnXin XLab 2026-05-25 12:02 UTC = 08:02 EDT — corpus-tracked since 2026-05-24 12:00 FLASH sentinel + 2026-05-24 PM brief horizon-scanning; anti-noise lock applies (consistent with 12:00 sentinel). (3) THN Alert Firehose NDR product-marketing 2026-05-25 11:30 UTC — promotional, DISCARDED (consistent with 12:00 sentinel).
  - bleepingcomputer        # fetch_feed — 15 items, 2 in 8h since-filter window: (1) Anthropic Claude Mythos model rumor 2026-05-25 17:07 UTC = 13:07 EDT — UPDATE on AM am-004 SecurityWeek/Anthropic Mythos 23K OSS-vuln research baseline; speculative rumor on potential Claude Code deployment; no new attribution, no new IOCs, no new CVEs; anti-noise applies. NOT raw-signaled (consistent with AM/12:00 anti-noise pattern on this thread). (2) FBI Kali365 phishing-as-a-service warning 2026-05-25 12:45 UTC = 08:45 EDT — corpus-tracked since FBI PSA260521; anti-noise applies (consistent with 12:00 sentinel).
  - securityweek            # fetch_feed feedburner — 10 items, 2 in 8h since-filter window: (1) Ghost CMS Eduard Kovacs relay 2026-05-25 13:27 UTC = 09:27 EDT — pure SW relay of THN/QiAnXin XLab piece, anti-noise applies (consistent with 12:00 sentinel). (2) Oncology Institute breach 2026-05-25 12:17 UTC = 08:17 EDT — healthcare third-party-vendor breach (TriZetto-possibly), no actor / no CVE / no A&D, OUT OF SCOPE (consistent with 12:00 sentinel).
  - the-record              # fetch_feed therecord.media/feed — 5 items, 0 in 8h window. Most recent dated 2026-05-22 pre-window.
  - krebsonsecurity         # fetch_feed krebsonsecurity.com/feed — 10 items, 1 in 8h since-filter window: Netherlands 800-server seizure / MIRhosting + WorkTitans (BrianKrebs byline, 2026-05-25 13:21 UTC = 09:21 EDT). A-grade investigative journalism. Russia-aligned infrastructure-takedown story; cites "Russia-backed hacking groups" and "Russia's intelligence agencies" GENERICALLY without naming APT28 / Sandworm / APT29 directly. Corpus-relevant for the APT28 (#006) / Sandworm (#007) / APT29 (#009) infrastructure ecosystem context. FAILS Trigger 2 (no specific roster actor named); FAILS Trigger 5 (LE-takedown not active-campaign frame). Worth raw-signaling for grader awareness as a NET-NEW corpus item (not previously corpus-covered). RAW-SIGNALED to pm-002.
  - isc-sans                # fetch_feed isc.sans.edu/rssfeed.xml — 10 items, 3 in 8h since-filter window: (1) Microsoft Access VBA diary 2026-05-25 14:14 UTC = 10:14 EDT — defensive content / malware-analysis methodology; no actor / no IOC / no A&D, DISCARDED per Mode 1. (2) TeamPCP Supply Chain Campaign: Activity Through 2026-05-24 (Kenneth Hartman byline, Didier Stevens handler-on-duty, 2026-05-25 13:26 UTC = 09:26 EDT, diary #33016). (3) Identical-titled diary #33014 published 19 seconds earlier — appears to be a duplicate publication (same author, same content per WebFetch direct retrieval) — TREAT AS ONE ITEM. SUBSTANTIVE TEAMPCP CONSOLIDATION through 2026-05-24: framework source-code GitHub drop 2026-05-22 ("Love - TeamPCP" / "Change keys and C2 as needed" README; ≥3 forks within hours including FreeBSD variant) + durabletask Linux disk-wiper capability + CISA-explicitly-did-NOT-add CVE-2026-45321 to KEV defender observation. Three NET-NEW capability layers beyond AM/PM corpus-anchored items. RAW-SIGNALED to pm-001.
  - rapid7                  # fetch_feed rapid7.com/blog/rss — 200 OK, 20 items, 0 in 8h since-filter window. Last_modified 2026-05-25 19:18 UTC = 15:18 EDT just inside window from feed-server activity, but no in-feed items published in window.
  - unit42                  # fetch_feed feedburner — 15 items, 0 in 8h since-filter window. Last_modified 2026-05-25 16:19 UTC = 12:19 EDT just inside window from feed-server activity, but no in-feed items published in window (8th+ consecutive sweep with no fresh threat-research content).
  - mstic                   # fetch_feed microsoft.com/en-us/security/blog/feed — 10 items, 0 in 8h since-filter window. Last_modified 2026-05-22 17:57 UTC pre-window UNCHANGED across multiple sweeps.
  - crowdstrike             # fetch_feed crowdstrike.com/blog/feed — 200 OK, 10 dateless items unchanged from AM/12:00 sentinels (product-marketing slate). NO threat-research content in window. Pattern continues (~30 consecutive sweeps).
  - mandiant                # feedburner.com/Mandiant returned 404 — 25th consecutive sweep failure (failure_count 22→23 per single-failure-increment rule; status held healthy per long-standing operator policy held-healthy-pending-alt-endpoint-decision; operator-set notes preserved verbatim). cloud.google.com/blog/topics/threat-intelligence index page NOT re-fetched this sweep — top-10 visible titles confirmed UNCHANGED across prior 8 sentinels per consistent observation pattern.
  - eset-welivesecurity     # fetch_feed welivesecurity.com/en/rss/feed — 100 items in feed, 0 in 8h window. Most recent 2026-05-22 Foul Play FIFA pre-window.
  - sentinelone             # fetch_feed sentinelone.com/labs/feed — 200 OK, 0 in window. Last_modified 2026-05-25 17:18 UTC = 13:18 EDT inside window from feed-server activity, but no in-feed items published in window.
  - bitdefender             # WebFetch timeout after 60s (low-frequency vendor cadence per source-health notes; most recent post 2026-05-19 MSHTA legacy pre-window). Single timeout failure_count 1→2 deferred to next sweep per failure-only-on-prior-sweep-recurrence convention.
  - volexity                # NOT re-fetched — STALE-flagged at AM sweep (third-strike malformed-XML); 24h skip rule applies until 2026-05-26.
  - wiz-research            # NOT re-fetched (pattern unchanged from 12:00 sentinel; most recent post 2026-05-21 Claude Enterprise pre-window).
  - snyk                    # fetch_feed snyk.io/blog/feed — 1628 items in feed but 0 with publication-time inside 8h window.
  - socket-dev              # WebFetch socket.dev/blog landing — top 5 unchanged from AM sentinel: (1) TrapDoor 34-package crypto-stealer (anti-noise lock active through 2026-05-25 16:00 EDT per Megalodon-morning-brief); (2) Laravel Lang RCE backdoor 2026-05-23 (anti-noise locked); (3) Postinstall Hook 700+ GitHub Repos 2026-05-22 (corpus-tracked); (4) AI Has Taken Over OSS 2026-05-22 (editorial/no-IOC); (5) npm Granular Token Invalidation 2026-05-21 (corpus-anchored). NO 2026-05-24 or 2026-05-25 dated posts.
  - safedep                 # WebFetch safedep.io/blog — top 5 unchanged from AM/12:00 sentinels (most recent post 2026-05-21 Megalodon original; subsequent posts 2026-05-21 Polymarket, 2026-05-20 durabletask, 2026-05-20 art-template, 2026-05-19 Mini Shai-Hulud 314). NO 2026-05-24 or 2026-05-25 dated posts.
  - sysdig                  # WebFetch sysdig.com/blog — top 5 dated 2026-05-19 through 2026-05-21 (NVIDIA AI security, headless cloud security, Azure VMAccess, headless runtime, agentic AI runtime). NO 2026-05-24 or 2026-05-25 dated posts.
  - sophos                  # WebFetch news.sophos.com/en-us/category/threat-research/feed redirected to www.sophos.com/en-us/category/threat-research/feed (301); REDIRECT-AND-DATELESS-RENDERING pattern persists.
  - cisco-talos             # WebFetch blog.talosintelligence.com landing — top 5 UNCHANGED from AM/12:00 sentinels (2026-05-21 ungovernable cultural; 2026-05-19 BadIIS MaaS; 2026-05-19 TP-Link/Photoshop/OpenVPN/Norton VPN; 2026-05-14 patching/AI; 2026-05-14 Cisco Catalyst SD-WAN). NO 2026-05-24 or 2026-05-25 dated posts. blog.talosintelligence.com/feeds/posts/default Atom endpoint NOT re-probed this sweep.
  - proofpoint              # NOT re-fetched (multi-day vendor cadence per source-health).
  - dragos                  # NOT re-fetched (multi-week vendor cadence per source-health).
  - rapid7-blog             # (same as rapid7 above)
  - greynoise               # fetch_feed greynoise.io/blog/rss.xml — 100 items in feed, 0 in 8h window. Most recent 2026-05-22 21:09 UTC pre-window.
  - github-blog-security    # WebFetch github.blog/category/security — top entries 2026-05-20 GitHub internal-repos disclosure (corpus-anchored TeamPCP), 2026-05-15 bug-bounty quality update, 2026-04-28 Wiz GitHub RCE, 2026-04-14 entries. NO 2026-05-24 or 2026-05-25 dated posts.
  - zdi-blog                # WebFetch zerodayinitiative.com/blog — top 5 dated 2026-05-12 through 2026-05-16 (Pwn2Own Berlin Days 1-3 + May Patch Tuesday review). NO 2026-05-24 or 2026-05-25 dated posts.
  - checkpoint-research     # fetch_feed research.checkpoint.com/feed — 1 in 8h window: 25th May Threat Intelligence Report (2026-05-25 15:08 UTC = 11:08 EDT). Substantive items all corpus-restatements — 7-Eleven ShinyHunters retail (out-of-scope), GitHub VS Code 3,800 repos (TeamPCP corpus-anchored), Grafana ShinyHunters cluster (corpus-anchored), Kali365 PhaaS (anti-noise), AI threat landscape March-April digest (research/methodology), MS Defender CVE-2026-41091/45498 (UnDefend/RedSun corpus-anchored), Trend Micro Apex One CVE-2026-34926 (corpus-tracked KEV), Drupal CVE-2026-9082 (corpus-tracked KEV T-2), Nimbus Manticore IRGC Operation Epic Fury MiniFast backdoor (UNC1549 alias variant corpus-anchored via Unit 42 Screening Serpens raw-2026-05-23-flash-0600-001 anti-noise expired 2026-05-24 06:00; pre-window). DACH 124% hacktivism surge 2025 (retrospective context). Showboat Linux SOCKS5 international telco (corpus-anchored generic China-aligned). Laravel Lang Composer attack (anti-noise locked). Consistent with 12:00 sentinel — anti-noise applies across substantive items. ALL Trigger 2 fail on attribution_is_new_not_restatement; ALL Trigger 5 fail on anti-noise. Sole net-new Check Point material is Nimbus Manticore SEO-poisoning + career-themed phishing United States + Europe + Middle East delivering MiniFast — anti-noise to UNC1549 thread expired but corpus-anchored TTPs.
  - dark-reading            # WebFetch returned 403 (anti-bot pattern; per source-health, infrequent retries warranted). Skipped further direct retrieval this sweep.
  - x-cisagov               # NOT re-fetched (KEV JSON serves as canonical CISA surface this sweep).
  - x-falconfeedsio         # NOT re-fetched (nitter pool fragility per source-health).
  - x-gossithedog           # NOT re-fetched (stale per source-health.yaml; under skip rule).
  - splunk-archimedes       # mcp__splunk-query | tstats count where (index=archimedes OR index=defenseclaw_local) earliest=-24h@h latest=now by index sourcetype → 33 events all in archimedes index (operation=16, scheduler=17). Splunk reachability HEALTHY.
  - splunk-defenseclaw      # Same query → ZERO events in -24h on defenseclaw_local. 57th CONSECUTIVE DORMANT non-self sweep.
  - splunk-targeted-ioc-search  # mcp__splunk-query search index=defenseclaw_local OR index=archimedes earliest=-8h@h latest=now ("TeamPCP" OR "Shai-Hulud" OR "filev2.getsession.org" OR "seed1.getsession.org" OR "durabletask" OR "@antv" OR "Nx Console" OR "echarts-for-react" OR "size-sensor" OR "@tiledesk/tiledesk-server" OR "Megalodon" OR "216.126.225.129" OR CVE-2026-45321 OR CVE-2026-26980 OR CVE-2026-9082 OR CVE-2026-42897 OR "ghost-cms" OR "clo4shara" OR Kali365 OR MIRhosting OR WorkTitans OR Nesterenko OR "Stark Industries" OR PQHosting OR APT28 OR APT29 OR Sandworm OR UNC1549 OR MuddyWater OR Lazarus OR "Salt Typhoon" OR "Volt Typhoon" OR APT37 OR APT40 OR APT41 OR "Charming Kitten") NOT sourcetype=archimedes:* → ZERO events. Hand-built 37-token sweep covers TeamPCP TTP-expansion IOCs (framework Session-network C2 + durabletask + @antv ecosystem + Nx Console + Megalodon C2 IP), Krebs MIRhosting/WorkTitans/Nesterenko/Stark cluster, anti-noise-locked Ghost CMS/Kali365, all 5 tracked CVEs, and all 12 highest-priority tracked actors. Hard Rule 8: silence is not disconfirming.

sources_querying_skipped_or_deferred:
  - shodan                  # not queried (no investigation hypothesis warrants paid-tier query)
  - censys                  # no MCP (stale per source-health)
  - virustotal              # not queried this sweep (TeamPCP framework-leak hashes not surfaced; durabletask + Megalodon IOCs eligible for enrichment if grader promotes pm-001 to finding-tier)
  - threatfox               # MCP not built; ABUSECH_API_KEY auth-injection blocked by WebFetch
  - malwarebazaar           # MCP not built; same auth-injection
  - hibp                    # no MCP and no API key per source-health (stale)
  - urlscan                 # MCP not built (stale per source-health)
  - aikido                  # NOT re-fetched — STALE-flagged at AM sweep (third-strike ECONNREFUSED); 24h skip rule applies until 2026-05-26.
  - reliaquest-blog         # NOT re-fetched (Loading placeholder DOM pattern; held).
  - thedfirreport           # NOT re-fetched (multi-month cadence).
  - cisa-icscert            # subset of cisa-advisories aggregate, no new feed activity.
  - f5-psirt                # NOT re-fetched (404 pattern across prior sweeps).
  - cisco-psirt             # NOT re-fetched (template-only render pattern persistent).
  - palo-alto-psirt         # sample-sweep cadence.
  - ivanti-psirt            # same.
  - citrix-psirt            # same.
  - sonicwall-psirt         # same.
  - vmware-broadcom-psirt   # same.
  - fortinet-psirt          # NOT re-fetched (transient SSL hostname-mismatch in 18:00 sentinel; held).

splunk_first_party_check:
  query_a: "| tstats count where (index=archimedes OR index=defenseclaw_local) earliest=-24h@h latest=now by index sourcetype"
  result_a: "33 events all in archimedes index (operation=16, scheduler=17); ZERO events on defenseclaw_local in -24h@h"
  query_b: 'search index=defenseclaw_local OR index=archimedes earliest=-8h@h latest=now ("TeamPCP" OR "Shai-Hulud" OR "filev2.getsession.org" OR "seed1.getsession.org" OR "durabletask" OR "@antv" OR "Nx Console" OR "echarts-for-react" OR "size-sensor" OR "@tiledesk/tiledesk-server" OR "Megalodon" OR "216.126.225.129" OR CVE-2026-45321 OR CVE-2026-26980 OR CVE-2026-9082 OR CVE-2026-42897 OR "ghost-cms" OR "clo4shara" OR Kali365 OR MIRhosting OR WorkTitans OR Nesterenko OR "Stark Industries" OR PQHosting OR APT28 OR APT29 OR Sandworm OR UNC1549 OR MuddyWater OR Lazarus OR "Salt Typhoon" OR "Volt Typhoon" OR APT37 OR APT40 OR APT41 OR "Charming Kitten") NOT sourcetype=archimedes:*'
  result_b: ZERO events
  defenseclaw_dormant: true
  consecutive_dormant_sweeps: 57
  hard_rule_8_framing: |
    Targeted 37-token sweep across tracked actors + tracked CVEs +
    emergent in-window IOCs (TeamPCP framework Session-network C2 +
    durabletask + @antv ecosystem + Nx Console + Megalodon C2 IP +
    Krebs Russia-hosting cluster) returned ZERO matches in -8h@h.
    57th consecutive dormant non-self sweep on defenseclaw_local.
    Hard Rule 8: silence is not disconfirming — defenseclaw_local is
    structurally bounded by its narrow ingest scope.

filter_evaluation_summary:
  in_window_items_total: 14         # 3 THN + 2 BC + 2 SW + 1 Krebs + 3 ISC-SANS + 1 Check Point + 2 ICS-CERT batches (0 surfaced)
  in_window_items_evaluated: 14
  in_window_items_corpus_restatement: 8   # Ghost CMS THN + SW relay, Kali365 BC, Check Point items (4-5 distinct restatements), Mythos rumor BC (UPDATE to AM am-004)
  in_window_items_filtered_out: 4   # THN Alert Firehose (promotional), THN Weekly Recap (aggregator), SW Oncology Institute (healthcare/no actor/no CVE), MS Access VBA ISC (defensive content)
  in_window_items_flash_tier: 0     # ZERO FLASH-trigger fires this sweep
  in_window_items_raw_signaled: 2   # pm-001 (TeamPCP TTP-expansion consolidation), pm-002 (Krebs Russia-hosting LE takedown)

trigger_evaluation:
  trigger_1_critical_cve_exploited:
    fired: false
    reason: |
      Ghost CMS CVE-2026-26980 NEAR-MISS: CVSS 9.4 ✓; active exploitation ✓
      (QiAnXin XLab reports 700+ compromised including Harvard, Oxford,
      DuckDuckGo); A-grade-source requirement FAILS — THN and SW are
      B-grade, QiAnXin XLab is not in source-grades.yaml. Anti-noise rule
      applies (same CVE covered since 2026-05-24 BleepingComputer surface,
      evaluated by 2026-05-24 12:00 FLASH and PM-sweep, fails all 6
      triggers per prior sentinels). UPDATE absorption to 16:00 PM brief
      at most. No other in-window CVE meets CVSS ≥ 9.0 + active-exploitation
      + A-grade-source threshold this window.

  trigger_2_tracked_actor_attribution:
    fired: false
    reason: |
      SANS ISC TeamPCP consolidation (Hartman, ISC-SANS B-grade) cites
      Microsoft Security Blog (corpus-anchored 2026-05-20) + GitHub CISO
      Alexis Wales (corpus-anchored 2026-05-21) attribution layers; both
      already in corpus per finding-2026-05-20-FLASH-0001. The Activity
      Through 2026-05-24 framing introduces three NET-NEW capability layers
      (framework-source GitHub drop 2026-05-22, durabletask Linux disk-wiper,
      CISA explicitly-NOT-on-KEV defender observation) — these are TTP-CHANGE
      surfaces (Trigger 4 candidate), NOT new actor-attribution claims.
      The TeamPCP attribution itself is unchanged from corpus-anchored
      tracking. Trigger 2 FAILS on attribution_is_new_not_restatement.

      Krebs Netherlands MIRhosting/WorkTitans piece uses GENERIC "Russia-
      backed hacking groups" / "Russia's intelligence agencies" attribution
      WITHOUT naming specific tracked roster actors (APT28 / Sandworm /
      APT29 / NoName057 / Killnet). Trigger 2 FAILS on attributed_actor
      not in _roster.yaml — the attribution is to nation-state-generic
      not specific-actor. Even if generic "Russia-backed" were treated as
      pseudo-roster-hit, attribution would FAIL attribution_is_new because
      the underlying APT28/Sandworm/APT29 ecosystem-via-Russia-hosting
      pattern is corpus-anchored.

  trigger_3_first_party_ioc_hit:
    fired: false
    reason: |
      Splunk targeted IOC sweep over -8h@h on defenseclaw_local + archimedes
      indexes returned ZERO non-self events across 37 tokens (TeamPCP
      framework C2 + durabletask + @antv ecosystem + Nx Console + Megalodon
      C2 IP + Krebs Russia-hosting cluster + all 5 tracked CVEs + 12
      highest-priority tracked actors). 57th consecutive dormant
      non-archimedes-self sweep on defenseclaw_local.

  trigger_4_tracked_actor_ttp_change:
    fired: false
    reason: |
      SANS ISC TeamPCP consolidation (Hartman, 2026-05-25 13:26 UTC) DOES
      describe three NET-NEW TTP layers for TeamPCP (tracked actor #001):
      (1) framework source-code drop to GitHub on 2026-05-22 with "Love -
      TeamPCP" / "Change keys and C2 as needed" README + ≥3 forks within
      hours including FreeBSD variant (NOVEL: campaign-source-leak
      commoditization); (2) durabletask Linux disk-wiper capability
      (NOVEL: destructive-class addition to predominantly credential-theft
      tradecraft); (3) CISA explicitly did NOT add CVE-2026-45321 to KEV
      despite GitHub-internal compromise + Microsoft SDK trojanization
      (defender-context observation, not TTP per se).

      Trigger 4 conditions: source_grade in [A, B] ✓ (sans-isc B);
      attributable_actor in _roster.yaml ✓ (TeamPCP #001);
      article_describes_new_tooling_or_targeting_or_infrastructure ✓.
      BUT: ALL THREE TTP layers cite ORIGINATING sources (Microsoft Security
      Blog 2026-05-20, SafeDep durabletask 2026-05-20, etc.) that are
      ALREADY corpus-anchored. The Hartman piece is a CONSOLIDATION /
      TIMELINE SUMMARY — it does not present primary-source first-
      observation of any of the three layers. Per the FLASH-POLICY
      attribution_is_new_not_restatement standard applied to TTP claims,
      this FAILS — Hartman is the SECONDARY synthesizer not the originating
      observer.

      Specifically:
        - Framework source-code drop 2026-05-22: Hartman cites "documented
          by vendors" — vendor-originating source NOT named in the piece;
          requires direct vendor-primary retrieval to substantiate first-
          observation. Per Hard Rule 2 the framework-leak claim cannot
          be promoted on relay-only basis.
        - durabletask Linux disk-wiper: SafeDep 2026-05-20 primary
          ALREADY in corpus (safedep.io/blog top-5 unchanged across
          AM/12:00/PM sentinels) — re-statement.
        - CISA-not-on-KEV observation: contextual defender-observation,
          not vendor-research; corpus-trackable via librarian-side KEV
          observation, not a TTP.

      Trigger 4 marginally FAILS on the relay-vs-originating standard.
      Hartman's consolidation IS itself grader-actionable as a corpus
      TIMELINE / TTP-MAP UPDATE — raw-signal pm-001 captures this for
      grader awareness without firing the FLASH path.

      RECOMMEND: Grader should consider whether the Hartman consolidation
      warrants a finding-tier TeamPCP TTP-Map-Update entry. If the
      framework-source GitHub drop has direct vendor-primary substantiation
      reachable in the morning (operator may identify vendor name from
      Hartman's "documented by vendors" reference), promote to finding-tier
      and consider FLASH Trigger 4 re-evaluation.

  trigger_5_ad_sector_campaign:
    fired: false
    reason: |
      No in-window item describes active campaign with multi-victim against
      A&D sector. SANS ISC TeamPCP consolidation names downstream victims
      OpenAI, Grafana Labs, Mistral AI, GitHub — all AI / OSS / DevTools
      sector, not A&D-prime watchlist. Krebs Netherlands hosting-takedown
      LE-action frame, not active-campaign frame.

  trigger_6_zero_day_no_patch:
    fired: false
    reason: |
      No in-window item describes zero-day disclosed without patch.
      Ghost CMS CVE-2026-26980 patched in Ghost 6.19.1 (Feb 19, 2026);
      Drupal CVE-2026-9082 patched in 11.1.6/10.4.6/10.3.11/7.81 since
      2026-05-22; Exchange CVE-2026-42897 ESU-binary-patched + EEMS/EOMT
      mitigation path available.

  critical_override:
    fired: false
    reason: |
      CVSS 10.0 + active exploitation + tracked roster actor + A&D
      watchlist hit conditions ALL NOT satisfied this sweep. CVE-2026-26980
      is 9.4 (below 10.0); CVE-2026-9082 is 6.5; CVE-2026-42897 is 8.1.
      No A&D watchlist victims named in any in-window item.

flash_candidates: []                # ZERO FLASH-trigger fires this sweep
flash_candidates_count: 0
source_health_changes:
  - source: bitdefender
    change_type: deferred_failure_count
    rationale: |
      WebFetch timeout at 60s ceiling — single timeout failure_count 1→2
      deferred to next sweep per failure-only-on-prior-sweep-recurrence
      convention. Low-frequency vendor cadence per source-health notes;
      most recent post 2026-05-19 MSHTA legacy (pre-window across multiple
      sentinels). Held healthy; failure_count increment scheduled for
      operator review at next sweep if pattern repeats.
  - source: mandiant
    change_type: persistent_feedburner_404
    rationale: |
      25th consecutive feedburner 404 (failure_count 22→23 per
      single-failure-increment rule). Status held healthy per long-standing
      operator policy held-healthy-pending-alt-endpoint-decision. Operator-set
      notes preserved verbatim per CLAUDE.md field-ownership rule.
  - source: cisco-talos
    change_type: front_page_unchanged
    rationale: |
      Front-page top 5 unchanged from AM and 12:00 sentinels (2026-05-21
      ungovernable cultural at top; substantive 2026-05-19 BadIIS MaaS
      Chinese-speaking + 2026-05-19 TP-Link/Photoshop/OpenVPN/Norton VPN;
      2026-05-14 entries). Healthy; no failure_count change.
  - source: krebs
    change_type: productive_in_window
    rationale: |
      Brian Krebs 2026-05-25 09:21 EDT Netherlands MIRhosting/WorkTitans
      seizure — A-grade investigative journalism, NET-NEW corpus item
      (not previously covered). Healthy; last_successful_fetch advanced
      to 2026-05-25T15:30:00-04:00.
  - source: isc-sans
    change_type: productive_in_window
    rationale: |
      Kenneth Hartman 2026-05-25 09:26 EDT TeamPCP consolidation — B-grade
      academic-vendor-research-tier-equivalent (handler-on-duty: Didier
      Stevens). Substantive timeline + TTP consolidation through 2026-05-24
      with three NET-NEW capability layers (framework leak, Linux disk-wiper,
      CISA-NOT-on-KEV observation). Healthy; last_successful_fetch advanced
      to 2026-05-25T15:30:00-04:00.

ttp_dimension_flags:
  - dimension: supply_chain_framework_open_sourcing
    actor: TeamPCP (#001)
    novel: true
    novel_basis: "first observed instance in Archimedes corpus of campaign-source-code public drop with 'Change keys and C2 as needed' README + multi-fork follow-on within hours (including FreeBSD variant). Commoditization pattern previously hypothesized analytically; this is the first concrete instance per SANS ISC Hartman 2026-05-25 timeline."
    flag_for: grader
    notes: |
      Hartman names "documented by vendors" without naming vendor primary.
      Recommend morning grader verify vendor-primary reachability before
      promoting to finding-tier. If vendor primary substantiates the
      "Love - TeamPCP" / "Change keys and C2 as needed" framework drop,
      consider Trigger 4 re-evaluation at next pre-brief.
  - dimension: destructive_capability_addition
    actor: TeamPCP (#001)
    novel: true
    novel_basis: "durabletask Linux disk-wiper capability is a destructive-class TTP added to TeamPCP's predominantly credential-theft tradecraft. Hartman cites this as SafeDep primary — corpus-anchored from AM sentinels."
    flag_for: grader
    notes: |
      Verify SafeDep primary attestation of disk-wiper capability in
      durabletask 1.4.1/1.4.2/1.4.3. SafeDep blog 2026-05-20 primary
      already in AM/12:00/PM sentinel surfaces (top-5 unchanged across
      sentinels). The Linux disk-wiper claim is a substantive TTP-MAP
      UPDATE on TeamPCP — if confirmed, dossier update warranted for
      destructive-category recalibration in threat-box methodology.

awareness_items:
  - item: "CISA explicitly did NOT add CVE-2026-45321 (Mini Shai-Hulud / TeamPCP) to KEV catalog through 2026-05-22 release"
    source: SANS ISC Hartman 2026-05-25
    relevance: |
      Defender-context observation. Corpus has tracked this since 12:00
      sentinel (CVE-2026-45321 KEV-pending per VT-006 entry in _index.yaml;
      "Anticipated KEV addition; CISA has not added as of 2026-05-12 06:00
      EDT" 13-day-delayed). Hartman flags this as notable given the
      GitHub-internal-compromise + Microsoft-SDK-trojanization scope.
      Worth flagging in 16:00 PM brief as KEV-pending observation.
  - item: "Russia-aligned hosting infrastructure takedown context for APT28 / Sandworm / APT29 ecosystem"
    source: Krebs 2026-05-25
    relevance: |
      Stark Industries successor infrastructure (MIRhosting / WorkTitans /
      PQHosting) is named-source-of-attacks ecosystem for APT28 (#006) /
      Sandworm (#007) / APT29 (#009) operations against EU / Danish
      government / Russia-Ukraine geopolitical conflict. Krebs uses
      GENERIC "Russia-backed hacking groups" attribution — does NOT name
      tracked roster actors. LE-takedown of supporting infrastructure has
      ecosystem-disruption signal value for defender posture even without
      direct A&D-prime impact. Worth 16:00 PM brief framing as
      tracking-awareness / infrastructure-ecosystem context.
  - item: "Anthropic Claude Mythos model potentially shipping in Claude Code"
    source: BleepingComputer Mayank Parmar 2026-05-25 13:07 EDT
    relevance: |
      UPDATE on AM am-004 SecurityWeek/Anthropic Mythos 23K OSS-vuln
      research baseline. Speculative rumor about potential Claude Code
      deployment; no new attribution, no new IOCs, no new CVEs. Anti-noise
      applies. Not raw-signaled.
  - item: "Check Point Research 25th May Threat Intelligence Report"
    source: Check Point Research urias byline 2026-05-25 11:08 EDT
    relevance: |
      A-grade vendor weekly digest of corpus-anchored items (GitHub VS Code
      breach, Grafana, Kali365, Defender CVEs, Drupal KEV, Trend Micro KEV,
      Showboat, Laravel Lang). Substantive net-new material limited to
      Nimbus Manticore SEO-poisoning + career-themed phishing expansion
      (corpus-tracked as UNC1549 alias per finding-2026-05-23-FLASH-0001;
      pre-window anti-noise expired but contains net-new TTP). Worth grader
      consideration as supplementary corroboration on Nimbus Manticore
      MiniFast backdoor expansion, but no new raw-signal created this sweep
      (corpus-anchored anti-noise applies to the broader Nimbus Manticore
      thread; Check Point cross-corroboration on the same UNC1549 alias
      thread is supplementary, not primary).

carry_forwards_to_pm_brief:
  - cve-2026-9082-drupal-kev-due-date-t-2
  - cve-2026-42897-exchange-kev-due-date-t-4
  - teampcp-multi-ecosystem-supply-chain-expansion-2026
  - krebs-stark-industries-mirhosting-arrests-russia-ecosystem-context
  - megalodon-github-workflow-dispatch-2026
  - trapdoor-multi-ecosystem-supply-chain-2026
  - "8th-supply-chain-mass-compromise-pattern-multi-actor-convergence-ach-h2"

next_sweep: flash-2026-05-25-1800
next_sweep_eta: 2026-05-25T18:00:00-04:00
---

# Sentinel — 2026-05-25 PM pre-brief collection (15:30 EDT)

**Sweep state:** Two net-new raw-signal files produced — pm-001 (SANS ISC Hartman TeamPCP supply-chain consolidation Activity Through 2026-05-24 with three net-new TTP layers — framework source-code GitHub drop, durabletask Linux disk-wiper, CISA-NOT-on-KEV defender observation) and pm-002 (Krebs Netherlands MIRhosting/WorkTitans server seizure as Russia-aligned hosting ecosystem LE-takedown context for APT28/Sandworm/APT29 ecosystem operations). Zero FLASH-trigger fires this sweep — TeamPCP TTP-change candidate (Trigger 4) marginally fails on relay-vs-originating standard (Hartman is secondary synthesizer; vendor-primary on framework-leak claim not yet directly retrieved). Krebs piece uses GENERIC "Russia-backed hacking groups" attribution without naming specific tracked roster actors — Trigger 2 fails.

**Top corpus carry-forwards to 16:00 PM brief:**
1. **CVE-2026-9082 Drupal Core SQLi (PostgreSQL)** — KEV due Wednesday 2026-05-27 at T-2 (~36h from this sweep). Patch coverage on contractor portals + DIB-marketing microsites remains today's action item.
2. **CVE-2026-42897 Exchange OWA XSS** — KEV due Friday 2026-05-29 at T-4 (~84h). No MSRC GA patch this sweep (MSRC blog template-only); ESU+EEMS+EOMT mitigation path unchanged. Single-source-veto on MSRC active-exploitation tag holds (Mandiant + Volexity + Unit 42 + MSTIC + CrowdStrike silent on corroboration).
3. **TeamPCP supply-chain expansion through 2026-05-24** — SANS ISC Hartman consolidation introduces three net-new capability layers; pm-001 captures for grader timeline-update consideration. Hard Rule 2 framing on framework-leak claim: requires vendor-primary direct retrieval before finding-tier promotion.
4. **Krebs Netherlands MIRhosting/WorkTitans seizure** — Russia-aligned hosting ecosystem LE-takedown; pm-002 captures for grader/briefer context. Generic "Russia-backed" attribution without specific roster-actor naming.
5. **Megalodon GitHub workflow_dispatch backdoor + TrapDoor multi-ecosystem supply-chain** — both anti-noise locked through 16:00 EDT (Megalodon morning brief 2026-05-25 + TrapDoor 2026-05-24 PM brief).
6. **Pattern observation: 8th distinct supply-chain mass-compromise campaign in 14 days (multi-actor convergence ACH H2)** — corpus-tracked since morning brief; pm-001 reinforces TeamPCP component but does NOT collapse the multi-actor frame.

**First-party Splunk:** Zero `defenseclaw_local` events on the 37-token sentinel sweep (TeamPCP framework C2 + durabletask + @antv + Nx Console + Megalodon C2 + Krebs Russia-hosting cluster + all 5 tracked CVEs + 12 highest-priority tracked actors). **57th consecutive dormant non-self sweep.** Hard Rule 8 framing: first-party silence is neither confirming nor disconfirming.

**Source-health observations:**
- mandiant: 25th consecutive feedburner 404 (failure_count 22→23; held healthy per operator policy).
- bitdefender: WebFetch 60s timeout (single failure; deferred increment).
- All other A/B-grade priority sources reachable with expected cadence patterns.
- volexity + aikido: stale per AM sweep; under 24h skip rule until 2026-05-26.

---

## Extraction notes

- Language: en
- Sentinel publisher byline: Archimedes collector subagent
- Article type: sentinel
- Raw IOC extraction invoked: no (IOCs in companion raw-signal files pm-001 and pm-002)

## IOCs (from ioc-extraction skill)

None — sentinel.
