---
source: archimedes-internal
source_grade: N/A
collected_at: 2026-05-27T15:55:00-04:00
sweep: pre-brief-2026-05-27-pm
url: null
test: false
sentinel: true
sweep_type: pre-brief-collection
status: complete
mode: pre_brief_collection
invocation: scheduled pre-brief PM-27 cycle (15:30 EDT) — feeds 16:00 EDT afternoon brief
sweep_window:
  start: 2026-05-27T07:35:00-04:00
  end: 2026-05-27T15:55:00-04:00
  duration_h: 8.33
prior_sweep_anchor:
  sweep_id: flash-2026-05-27-1200
  anchor_at: 2026-05-27T12:05:00-04:00
  raw_id: raw-2026-05-27-flash-1200-000-sentinel-clean-sweep.md
  commit_sha: 7bd6ffa
  disposition: zero_triggers_fired_six_absorbed
  notes: |
    Noon FLASH was a clean sweep — 0 of 6 triggers fired across 5.88h
    window with 17 in-window items (6 absorbed under AM-27 morning-brief
    locks + active corpus locks; 11 discarded). Six absorption-eligible
    candidates flagged for PM-27 pre-brief: Yamcs CVE-2026-44632 (A&D-
    relevant spacecraft mission control) + XWiki CVE-2026-33137 (no
    A&D, candidate for PM-27 awareness mention only).
prior_brief_anchor:
  brief_id: 2026-05-27-morning
  shipped_at: 2026-05-27T08:00:00-04:00
  commit_sha: 791b8da
  notes: |
    AM-27 morning brief shipped DEGRADED-RECOVERY (pipeline did not
    commit; recovery commit + Discord alert via run_phase.ps1 brief-phase
    output-based criterion). Six findings: 0001 GlassWorm takedown
    (#005 first A-grade Russia-pattern attribution); 0002 Gitea
    CVE-2026-27771 unauth container disclosure (aerospace
    manufacturers named); 0003 SymJack symlink hijack AI coding
    agents; 0004 LACMTA Iran Black Shadow MOIS investigation
    update; 0005 MSTIC cryptojacking ScreenConnect AI-chatbot SEO;
    0006 Charter / ShinyHunters Salesforce-Entra vishing 40M
    records.

match_reason:
  watchlist:
    - aerospace-spacecraft-satellite-mission-control-software-affected-class    # Yamcs CVE-2026-44632 A&D-relevant
  actors:
    - GlassWorm (#005 HIGH) — fourth relay layer (The Register) corroborates AM-27 finding-0001 disposition with new Russian-pattern operational indicators (CIS-locale + Russian-language code comments + GlasswormRAT named tool)
    - Black Shadow → Ababil of Minab (NOT in roster) — Iran/MOIS new alias surfaced by The Record relay of Gambit Security; investigation inv-2026-05-26-001 carry-forward update
  vulnerabilities:
    - VT-006   # CVE-2026-45321 Mini Shai-Hulud KEV-pending watch signal FIRED today — kev_added: 2026-05-27, due: 2026-06-10 T+14
    - "CVE-2026-48027 Nx Console — KEV-listed today; corpus finding-2026-05-20-FLASH-0001 carry-forward; VT-010 scaffolding candidate"
    - "CVE-2026-44632 Yamcs (NEW) — A&D-relevant spacecraft mission control software RCE; VT-010+ scaffolding candidate"
    - VT-008   # CVE-2026-42897 Exchange — KEV deadline T-2 Fri 2026-05-29 (~46h)
    - VT-009   # CVE-2026-48172 LiteSpeed cPanel — KEV deadline T-2 Fri 2026-05-29 (~46h)
  keywords:
    - CISA KEV
    - CVE-2026-45321
    - CVE-2026-48027
    - CVE-2026-8398
    - CVE-2026-44632
    - TanStack
    - Nx Console
    - Daemon Tools Lite
    - Yamcs
    - mouse5212-super-formatter
    - Claude AI
    - OX Security
    - Gambit Security
    - LACMTA
    - Ababil of Minab
    - Black Shadow
    - MOIS
    - GlassWorm
    - CrowdStrike CAO
    - John Hultquist GTIG
    - Russian attribution pattern
    - CIS-locale termination check
    - GlasswormRAT
    - 164.92.88.210
    - github.com/unplowed3584

triage_tags:
  - pre_brief_sentinel
  - pm_pre_brief_scheduled
  - kev_addition_today_three_cves_cve_2026_45321_cve_2026_48027_cve_2026_8398
  - tracked_vuln_state_change_vt_006_kev_pending_to_kev_added_today
  - corpus_finding_state_change_finding_2026_05_20_flash_0001_cve_2026_48027_kev_listed
  - new_cve_disclosure_yamcs_cve_2026_44632_ad_relevant_spacecraft_mission_control
  - tracked_actor_attribution_enrichment_glassworm_005_russian_pattern_operational_indicators
  - iran_cyber_watch_lacmta_second_relay_the_record_ababil_of_minab_alias_new
  - supply_chain_attack_mouse5212_npm_claude_ai_user_data_ox_security
  - non_flash_grader_queue_items_x5
  - investigation_inv_2026_05_26_001_carry_forward_active
  - mandiant_endpoint_canonicalization_recommendation_persisting_eighth_time
  - volexity_fifth_consecutive_parse_error_stale_flip_recommended

iocs_extracted: false
iocs_count: 0
text_word_count: 2050
promoted: false
ttl_expires_at: 2026-08-25T15:55:00-04:00

sources_queried:
  - cisa-kev               # WebFetch known_exploited_vulnerabilities.json — catalogVersion ADVANCED 2026.05.26 → 2026.05.27. THREE NEW KEV ADDITIONS at 12:00 UTC today: CVE-2026-45321 TanStack (corpus VT-006 Mini Shai-Hulud — KEV-pending watch signal FIRED), CVE-2026-48027 Nx Console (corpus finding-2026-05-20-FLASH-0001), CVE-2026-8398 Daemon Tools Lite (NOT corpus-tracked). RAW-SIGNALED as PM-001.
  - cisa-advisories        # fetch_feed cisa.gov/cybersecurity-advisories/all.xml — 200 OK, 30 items in feed. 1 in-window — the matching CISA alert post for the three KEV additions (07:00 EDT post; direct page WebFetch returned 403 but RSS path productive). ABSORBED into PM-001.
  - thehackernews          # fetch_feed feedburner — 200 OK; last_modified Wed 27 May 2026 18:45 GMT. 5 in-window items. (1) Grandoreiro + BTMOB malware campaigns (WatchGuard + ESET research, LatAm + Brazil banking targeting, no A&D, no roster — DISCARDED off-scope). (2) mouse5212-super-formatter npm Claude AI (OX Security, supply-chain class, no roster attribution) — RAW-SIGNALED as PM-002. (3) Shadow AI Tools editorial — DISCARDED. (4) GlassWorm Malware Takedown (11:48 EDT) — ABSORBED under AM-27 finding-0001 lock. (5) 3 SOC Steps editorial — DISCARDED.
  - bleepingcomputer       # fetch_feed — 200 OK; last_modified Wed 27 May 2026 19:29 GMT. 3 in-window items. (1) Specops AD password sponsored content — DISCARDED. (2) Glassworm botnet disrupted (Ilascu 09:28 EDT) — ABSORBED under AM-27 finding-0001 lock. (3) FBI Silent Ransom Group law-firm USB-drop tradecraft (Gatlan 07:51 EDT) — DISCARDED per Mode 1 (no A&D / no roster / no vuln-index; Luna Moth / Chatty Spider / UNC3753 NOT in _roster.yaml; FBI flash classified as restatement of May 2025 PIN).
  - securityweek           # fetch_feed feedburner — 200 OK; last_modified Wed 27 May 2026 17:32 GMT. 5 in-window items. (1) UK GCHQ Anne Keast-Butler AI Russia speech — DISCARDED per Mode 1 (no specific tracked-actor / no specific vuln / no specific A&D-prime named; policy speech tier). (2) Pretalx CVE-2026-41241 stored XSS — DISCARDED per Mode 1 (no A&D, post-patch researcher disclosure). (3) AI Risk Summit event — DISCARDED. (4) RevEng.AI funding — DISCARDED. (5) Romanian Hacker Sentence — DISCARDED.
  - the-record             # fetch_feed therecord.media/feed — 200 OK; 5 in-window items. (1) Romanian Hacker Oregon Sentence — DISCARDED. (2) Rudd Cyber Command MITRE Review — DISCARDED per Mode 1 (gov policy/leadership content, no actor / no vuln / no specific A&D-prime impact; structural DIB-acquisition-impact framing noted but no operational threat-intel). (3) FBI Silent Ransom Group law firms — restatement, DISCARDED. (4) Dutch police Ajax football — DISCARDED. (5) Iranian intelligence LACMTA / Ababil of Minab / MOIS via Gambit Security (Smalley 09:20 EDT) — RAW-SIGNALED as PM-003 (second relay layer + new alias surfaces, absorbable under finding-2026-05-27-0004 + investigation lock).
  - dark-reading           # fetch_feed darkreading.com/rss.xml — 200 OK; last_modified Wed 27 May 2026 19:31 GMT. 5 in-window items. (1) Latin American cybercriminals Uruguay government data (Lemos) — WebFetch returned 403 in this sweep; awareness-only-DISCARD given LatAm government victim, no A&D / no roster. (2) AI-assisted exploit development outpaces scanner detection — WebFetch returned 403; awareness-only-DISCARD as research piece without specific actor / vuln / A&D. (3) Cybersecurity Evolution 20th anniversary editorial — DISCARDED off-scope. (4) Infosecurity Europe event — DISCARDED. (5) Anatomy of Data Breach event — DISCARDED.
  - the-register           # fetch_feed theregister.com/security/headlines.atom — 200 OK; 5 in-window items. (1) CrowdStrike Google GlassWorm takedown (13:56 EDT, no byline-credit in extract) — RAW-SIGNALED as PM-005 (fourth relay layer with NEW Russian-pattern operational indicators: CIS-locale termination check + Russian-language code comments + GlasswormRAT named tool + Hultquist GTIG confirmation). (2) Okta shadow AI survey — DISCARDED off-scope. (3) FBI Silent Ransom — DISCARDED restatement. (4) CERT-In 12h patching guidance — DISCARDED policy guidance. (5) Pretalx XSS — DISCARDED (anti-noise with SW item 2 above).
  - mandiant               # fetch_feed mandiant.com/resources/blog/rss.xml — 200 OK (EIGHTH consecutive recovery across PM-26 12:00 / 18:00 / 00:00 / 06:00 / AM-27 / 12:00 / this PM-27); 20 items in feed, 0 in 8.33h window. Endpoint canonicalization recommendation PERSISTS — eighth straight productive recovery on mandiant.com path while cloud.google.com path remains parse-error or malformed.
  - unit42                 # fetch_feed feedburner — 200 OK; last_modified Tue 26 May 2026 16:56 GMT (= 12:56 EDT pre-window unchanged across seven consecutive sweeps). 0 in window.
  - mstic                  # fetch_feed microsoft.com/en-us/security/blog/feed — 200 OK; last_modified Tue 26 May 2026 21:35 GMT (= 17:35 EDT pre-window unchanged across three consecutive sweeps since AM-27). 0 in window.
  - crowdstrike            # fetch_feed crowdstrike.com/blog/feed/ — 200 OK; 10 items, ALL published: null per persistent-dateless-marketing pattern. Top-of-feed item IS the GlassWorm takedown (Counter Adversary Operations byline) but content already absorbed in AM-27 finding-0001 + PM-005 enrichment. Pattern of useful content surfacing only via dated relays continues.
  - checkpoint-research    # fetch_feed research.checkpoint.com/feed — 200 OK; last_modified Tue 26 May 2026 12:13 GMT pre-window unchanged across seven consecutive sweeps. 0 in window.
  - cisco-talos            # fetch_feed blog.talosintelligence.com/rss/ — 200 OK; 15 items in feed, 1 in 8.33h window — MediaArea heap-based buffer overflow vulnerabilities (Kri Dontje 10:00 EDT, four patched CVEs: CVE-2026-25104 / 25713 / 28764 / 22554 in MediaInfoLib 26.01). NO A&D / NO roster / NO active-exploitation. DISCARDED per Mode 1.
  - sans-isc               # fetch_feed isc.sans.edu/rssfeed.xml — 200 OK; last_modified Wed 27 May 2026 19:29 GMT. 0 in-window items beyond the AM-27-absorbed Wednesday Stormcast podcast detail.
  - rapid7                 # fetch_feed rapid7.com/blog/rss/ — 200 OK; last_modified Wed 27 May 2026 19:17 GMT (feed-server activity inside window). 0 in-window items.
  - sentinelone            # fetch_feed sentinelone.com/labs/feed/ — 200 OK; last_modified Wed 27 May 2026 16:45 GMT (= 12:45 EDT inside window from feed-server activity). 0 in-window items.
  - welivesecurity         # fetch_feed welivesecurity.com/en/rss/feed/ — 200 OK; 100 items in feed, 0 in window.
  - sophos                 # fetch attempt news.sophos.com/en-us/feed/ returned 404 — STALE STATUS PERSISTS per source-health.yaml since 2026-05-17 (three consecutive failures); no retry change this sweep. PM-27 collector preserves stale status pending operator alt-endpoint identification.
  - krebs                  # fetch_feed krebsonsecurity.com/feed — 200 OK; last_modified Mon 25 May 2026 13:21 GMT pre-window unchanged. 0 in window (3-day Krebs publication cadence quiet pattern continues).
  - volexity               # validate_feed volexity.com/blog/feed/ — XML PARSE ERROR (<unknown>:17:68: not well-formed invalid token) — FIFTH CONSECUTIVE same-class failure across 2026-05-19 + 2026-05-26 PM-26 + 2026-05-27 06:00 FLASH + AM-27 + this PM-27. failure_count 4→5 well past stale threshold. STALE FLIP RECOMMENDATION ELEVATED to operator decision this sweep.
  - github-advisories      # WebFetch github.com/advisories?query=type:reviewed+severity:critical&sort=published-desc — 200 OK; 5 most-recent critical advisories returned. ONE NEW A&D-RELEVANT: Yamcs CVE-2026-44632 GHSA-524g-x36v-9wm6 server-side code injection RCE via Janino Expression Engine; CVSS 9.1; post-auth high-priv SystemPrivilege.ChangeMissionDatabase; patched 5.12.7; NO ITW. RAW-SIGNALED as PM-004. The other four (LiquidJS CVE-2026-45618, XWiki CVE-2026-33137 absorbed AM-27 FLASH-1200 awareness, XWiki CVE-2026-23734, Nezha CVE-2026-46716) all DISCARDED per Mode 1.
  - splunk-archimedes      # mcp__splunk-query targeted 42-IOC sweep on -9h@h INCLUDING all the new in-window tokens (TanStack KEV, Nx Console KEV, Daemon Tools KEV, mouse5212-super-formatter, Yamcs CVE-2026-44632, Ababil of Minab, GlassWorm + 164.92.88.210 sinkhole, CIS-locale terminator, GlasswormRAT) on the full carried-forward 41-IOC corpus set. ZERO non-archimedes-internal events. 67th consecutive dormant non-self sweep on defenseclaw_local (incremented from 66 at AM-27 + 12:00 FLASH).
  - splunk-defenseclaw     # included in cross-index 9h sweep; ZERO events. 67th consecutive dormant non-self sweep.

splunk_first_party_check:
  query: 'search index=archimedes OR index=defenseclaw_local earliest=-9h@h latest=now NOT sourcetype=archimedes:* ("GlassWorm" OR "TanStack" OR "Nx Console" OR "Mini Shai-Hulud" OR "TeamPCP" OR "Ababil of Minab" OR "Black Shadow" OR "LACMTA" OR "Silent Ransom" OR "Luna Moth" OR "Chatty Spider" OR CVE-2026-45321 OR CVE-2026-48027 OR CVE-2026-8398 OR CVE-2026-42897 OR CVE-2026-48172 OR CVE-2026-9082 OR CVE-2026-27771 OR "164.92.88.210" OR "gleeze.com" OR ShinyHunters OR Charter OR "Operation Epic Fury" OR UNC1549 OR MuddyWater OR APT34 OR APT37 OR APT28 OR APT29 OR APT41 OR Sandworm OR Lazarus OR "Volt Typhoon" OR "Salt Typhoon" OR LockBit OR Cl0p OR Handala) | head 50'
  result: ZERO non-archimedes-internal events. ZERO defenseclaw_local hits. ZERO IOC matches.
  consecutive_dormant_sweeps_defenseclaw: 67    # incremented from 66 at AM-27 / 12:00 FLASH
  iac_ioc_hits_in_defenseclaw_local: 0
  hard_rule_8_framing: |
    Targeted 42-IOC sweep across the carried-forward corpus IOC set
    PLUS net-new tokens from this PM-27 sweep on archimedes +
    defenseclaw_local -9h@h returned ZERO non-archimedes-internal
    events. 67th consecutive dormant non-self sweep on
    defenseclaw_local. Hard Rule 8: silence is not disconfirming, not
    confirming. Operator note: dormant pattern has now persisted
    continuously through Sessions 11-15+ (multi-week baseline), which
    is informative for ITW-targeting-pattern assessment of A&D-prime
    estate posture but is not itself dispositive.

filter_evaluation_summary:
  in_window_items_total: 28
  in_window_items_evaluated: 28
  in_window_items_raw_signaled: 5
  in_window_items_corpus_restatement_anti_noise_absorbed: 5
  in_window_items_discarded_off_scope: 18
  notes: |
    Twenty-eight in-window items across A/B-grade surveyed surfaces.
    FIVE raw-signaled (PM-001 CISA KEV three-add + PM-002 mouse5212
    Claude AI + PM-003 LACMTA Iran second relay + PM-004 Yamcs CVE +
    PM-005 The Register GlassWorm enrichment). FIVE absorbed under
    active anti-noise / AM-27 morning-brief locks (THN + BC + SW + The
    Register + CrowdStrike all GlassWorm restatements). EIGHTEEN
    DISCARDED per Mode 1 (no watchlist / no roster / no vuln-index
    hit, OR not threat-intel-actionable content).

source_health_changes:
  - source_yaml_id: mandiant
    observation: |
      mandiant.com/resources/blog/rss.xml endpoint returned 200 OK
      with 20 items in feed (EIGHTH consecutive recovery observation
      across PM-26 12:00 / 18:00 / 00:00 / 06:00 / AM-27 / 12:00 / this
      PM-27 pre-brief). Endpoint canonicalization recommendation
      PERSISTS at urgency-level "operator-decision-pending eighth time."
      cloud.google.com/blog/topics/threat-intelligence endpoint NOT
      retried this sweep to avoid thrashing; the long-standing
      feedburner.com/Mandiant 404 + cloud.google.com parse-error
      pattern is preserved verbatim in source-health.yaml notes per
      operator preservation rule.
    runtime_change_applied: |
      last_successful_fetch advanced to 2026-05-27T15:55:00-04:00 (via
      mandiant.com/resources/blog/rss.xml productive endpoint, NOT the
      feedburner endpoint cited in last_error). last_error string
      UPDATED to reflect today's eighth recovery observation alongside
      historical 404 context. failure_count UNCHANGED at 19 (the prior
      runtime-state field tracks feedburner-specific failures, NOT the
      productive mandiant.com path — held per operator policy until
      canonicalization decision lands). notes: field preserved verbatim.
  - source_yaml_id: volexity
    observation: |
      www.volexity.com/blog/feed/ validate_feed returned XML parse
      error (<unknown>:17:68: not well-formed invalid token) — FIFTH
      CONSECUTIVE same-class failure. failure_count 4→5. STALE FLIP
      RECOMMENDATION ELEVATED — the pattern has now persisted across
      five consecutive sweeps spanning the AM-27 + 12:00 FLASH + this
      PM-27 pre-brief sequence. Held healthy per long-standing operator
      instruction; this PM-27 sweep elevates the recommendation to
      operator-decision-required tier.
    runtime_change_applied: failure_count_4_to_5_stale_flip_recommendation_elevated_to_operator_decision_required
  - source_yaml_id: sophos
    observation: |
      news.sophos.com/en-us/feed/ returned 404 — STALE STATUS PERSISTS
      per source-health.yaml since 2026-05-17 (three consecutive
      failures established the stale flip). PM-27 collector preserved
      stale status pending operator alt-endpoint identification.
      Workaround (news.sophos.com/feed/ root path) noted in
      source-health.yaml notes for previous PM-27 review.
    runtime_change_applied: no_change_stale_persists_per_existing_disposition
  - source_yaml_id: github-advisories
    observation: |
      WebFetch on github.com/advisories?query=type:reviewed+severity:
      critical&sort=published-desc productive — 5 most-recent critical
      advisories returned successfully. The long-standing 406 Not
      Acceptable on github.com/advisories.atom RSS endpoint remains
      unresolved (held since 2026-05-08 first-soft-fail); the WebFetch-
      on-advisories-search-page workaround is the productive path for
      global GHSA queries.
    runtime_change_applied: last_successful_fetch_advanced_via_webfetch_workaround_path
  - source_yaml_id: dark-reading
    observation: |
      fetch_feed succeeded but BOTH direct WebFetch attempts on
      productive in-window dark-reading article URLs returned 403
      (Latin American cybercriminals Uruguay government data + AI-
      assisted exploit development outpaces scanner detection). The
      dark-reading WebFetch-403-on-article-body pattern reduces
      Dark Reading's productive-yield to feed-headline-tier only,
      similar to the Wired Claude Code blocking pattern documented in
      source-health.yaml since 2026-05-09.
    runtime_change_applied: no_change_pattern_documented_for_operator_awareness

source_health_runtime_field_updates:
  - source_yaml_id: cisa-kev
    field: last_successful_fetch
    new_value: 2026-05-27T15:35:00-04:00
    rationale: WebFetch of catalogVersion 2026.05.27 succeeded; three new adds (CVE-2026-45321, CVE-2026-48027, CVE-2026-8398) confirmed at 12:00 UTC; healthy.
  - source_yaml_id: cisa-advisories
    field: last_successful_fetch
    new_value: 2026-05-27T15:35:00-04:00
    rationale: fetch_feed cisa.gov all.xml succeeded 200 OK; 30 items; 1 in-window matching KEV alert post; healthy.
  - source_yaml_id: bleepingcomputer
    field: last_successful_fetch
    new_value: 2026-05-27T15:31:00-04:00
    rationale: fetch_feed 200 OK; 3 items in window; productive (Glassworm restatement absorbed + FBI Silent Ransom discarded + Specops sponsored discarded).
  - source_yaml_id: securityweek
    field: last_successful_fetch
    new_value: 2026-05-27T15:31:00-04:00
    rationale: fetch_feed 200 OK; 5 items in window; UK GCHQ + Pretalx + AI Risk Summit + funding + Romanian sentence all discarded.
  - source_yaml_id: the-record
    field: last_successful_fetch
    new_value: 2026-05-27T15:31:00-04:00
    rationale: fetch_feed 200 OK; 5 items in window; LACMTA Iran second relay RAW-SIGNALED as PM-003.
  - source_yaml_id: thehackernews
    field: last_successful_fetch
    new_value: 2026-05-27T15:31:00-04:00
    rationale: fetch_feed 200 OK; 5 items in window; mouse5212 + Grandoreiro/BTMOB + GlassWorm + 2x editorial.
  - source_yaml_id: mstic
    field: last_successful_fetch
    new_value: 2026-05-27T15:31:00-04:00
    rationale: fetch_feed 200 OK; 0 in window; healthy (PM-26 17:35 UTC cryptojacking primary remains most recent).
  - source_yaml_id: unit42
    field: last_successful_fetch
    new_value: 2026-05-27T15:31:00-04:00
    rationale: fetch_feed 200 OK; 0 in window; healthy.
  - source_yaml_id: crowdstrike
    field: last_successful_fetch
    new_value: 2026-05-27T15:31:00-04:00
    rationale: fetch_feed 200 OK; GlassWorm top-of-feed already absorbed; dateless-marketing pattern continues for 9 of 10 items.
  - source_yaml_id: cisco-talos
    field: last_successful_fetch
    new_value: 2026-05-27T15:31:00-04:00
    rationale: fetch_feed 200 OK; 1 in-window MediaArea CVE cluster discarded per Mode 1; healthy.
  - source_yaml_id: rapid7
    field: last_successful_fetch
    new_value: 2026-05-27T15:31:00-04:00
    rationale: fetch_feed 200 OK; last_modified inside window from feed-server activity; 0 in-window items; healthy.
  - source_yaml_id: sans-isc
    field: last_successful_fetch
    new_value: 2026-05-27T15:31:00-04:00
    rationale: fetch_feed 200 OK; 0 in-window beyond AM-27-absorbed podcast; healthy.
  - source_yaml_id: sentinelone
    field: last_successful_fetch
    new_value: 2026-05-27T15:31:00-04:00
    rationale: fetch_feed 200 OK; last_modified inside window; 0 in-window items; healthy.
  - source_yaml_id: github-advisories
    field: last_successful_fetch
    new_value: 2026-05-27T15:50:00-04:00
    rationale: WebFetch on advisories search page succeeded (workaround for long-standing 406 on advisories.atom); Yamcs CVE-2026-44632 RAW-SIGNALED as PM-004.
  - source_yaml_id: mandiant
    field: last_successful_fetch
    new_value: 2026-05-27T15:55:00-04:00
    rationale: Eighth consecutive recovery on mandiant.com/resources/blog/rss.xml endpoint (200 OK; 20 items; 0 in window). Endpoint canonicalization recommendation persists at operator-decision-pending tier.
  - source_yaml_id: mandiant
    field: last_error
    new_value: "feedburner.com/Mandiant returned 404 on 2026-05-27T15:55 PM pre-brief — long-standing pattern; alt mandiant.com/resources/blog/rss.xml endpoint produces EIGHTH consecutive recovery this sweep (200 OK, 20 items, 0 in window). Operator canonicalization decision elevated to urgency-pending."
    rationale: Held healthy per long-standing source-health policy; operator alt-endpoint decision elevated this sweep.
  - source_yaml_id: volexity
    field: failure_count
    new_value: 5
    rationale: FIFTH consecutive XML parse error <unknown>:17:68 not well-formed invalid token. Stale flip recommendation ELEVATED to operator decision required.
  - source_yaml_id: volexity
    field: last_error
    new_value: "2026-05-27 15:55 PM pre-brief sweep: www.volexity.com/blog/feed/ returned malformed body (XML parse error <unknown>:17:68 not well-formed invalid token) — FIFTH consecutive same-class failure across 2026-05-19 + 2026-05-26 PM-26 + 2026-05-27 06:00 FLASH + AM-27 + this PM-27. STALE FLIP RECOMMENDATION ELEVATED to operator-decision-required."
    rationale: Held healthy per operator instruction; recommendation elevated.

source_health_changes_summary:
  recoveries: []
  new_failures: []
  status_flips_proposed:
    - source_yaml_id: volexity
      proposed_status: stale
      rationale: fifth-consecutive same-class XML parse error; well past ≥2 stale threshold; held healthy per operator policy across five sweeps; elevation point reached.
  no_change_held_healthy:
    - source_yaml_id: mandiant
      rationale: eighth recovery on productive endpoint; canonicalization decision pending
    - source_yaml_id: volexity
      rationale: fifth-consecutive failure; held healthy per operator policy
  stale_persisting:
    - sophos                 # since 2026-05-17, en-us subpath 404, root-path workaround documented in notes
    - censys                 # since 2026-05-05, MCP not built
    - urlscan                # since 2026-05-05, MCP not built
    - hibp                   # since 2026-05-05, no API key
    - x-cisagov              # since 2026-05-10, nitter bridge fragility
    - x-gossithedog          # since 2026-05-09, account delisted
    - ars-security           # since 2026-05-09, feed endpoint retired
  pattern_observations:
    - "Mandiant endpoint canonicalization decision now eighth-time-pending — operator review elevated to urgent tier."
    - "Volexity fifth-consecutive parse-error — stale flip recommendation elevated to operator-decision-required."
    - "CrowdStrike persistent-dateless-marketing pattern continues — useful content (GlassWorm takedown) surfaces only via dated relays (today via SecurityWeek + BC + THN + The Register; all four absorbed under AM-27 lock or enrichment via PM-005)."
    - "Dark Reading WebFetch-403-on-article-body reduces yield to headline-tier only (similar to Wired pattern)."

anti_noise_locks_active_inherited_from_am_27_morning_brief_and_12_00_flash:
  - lock_id: cve-2026-9082-drupal-core-sqli-kev-deadline-tracking
    status: EXPIRED — T-0 deadline Wed today 2026-05-27 EOB lapsed; AM-27 brief was canonical deadline-day surface; PM-27 brief carries forward as T+0-lapse-tracking
  - lock_id: cve-2026-42897-exchange-owa-xss-kev-deadline-tracking
    status: ACTIVE — T-2 deadline Fri 2026-05-29 ~46h from this sweep
  - lock_id: cve-2026-48172-litespeed-cpanel-plugin-kev-deadline-tracking
    status: ACTIVE — T-2 deadline Fri 2026-05-29 ~46h from this sweep
  - lock_id: cve-2026-45321-mini-shai-hulud-oidc-credential-abuse-kev-pending-watch
    status: CONVERTED TO ACTIVE-KEV-LISTED — KEV-pending watch signal FIRED today; new state cve-2026-45321-mini-shai-hulud-kev-deadline-tracking (kev_added 2026-05-27, dueDate 2026-06-10 T+14); see PM-001 raw-signal
  - lock_id: cve-2026-48027-nx-console-kev-deadline-tracking
    status: NEW ACTIVE-KEV-LISTED — KEV-added today (corpus finding-2026-05-20-FLASH-0001 KEV-listed); new lock dueDate 2026-06-10 T+14; see PM-001 raw-signal
  - lock_id: unc1549-screening-serpens-tradecraft-evolution-2026-tradecraft-rats-azure-staging
    status: ACTIVE through 2026-05-27 16:00 (~5min remaining at sweep close)
  - lock_id: am-27-finding-0001-glassworm-takedown-crowdstrike-google-shadowserver
    status: ACTIVE through 2026-05-28T08:00:00-04:00; PM-005 enrichment surface for Russian-pattern operational indicators
  - lock_id: am-27-finding-0002-gitea-cve-2026-27771-noscope-aerospace-manufacturers
    status: ACTIVE through 2026-05-28T08:00:00-04:00
  - lock_id: am-27-finding-0003-symjack-adversa-ai-five-vendor-mcp-abuse
    status: ACTIVE through 2026-05-28T08:00:00-04:00
  - lock_id: am-27-finding-0005-mstic-cryptojacking-screenconnect-ai-chatbot-gleeze-com
    status: ACTIVE through 2026-05-28T08:00:00-04:00
  - lock_id: am-27-finding-0006-charter-shinyhunters-salesforce-entra-vishing
    status: ACTIVE through 2026-05-28T08:00:00-04:00
  - lock_id: inv-2026-05-26-001-lacmta-iran-attribution-black-shadow-ababil-of-minab-mois
    status: ACTIVE through 2026-06-09T00:00:00-04:00 (T+14); PM-003 second-relay-layer enrichment with new "Ababil of Minab" alias

trigger_evaluation_note: |
  This is a pre-brief collection sweep, NOT a FLASH sweep. FLASH-trigger
  evaluation belongs to the FLASH-sweep mode. However, for situational
  awareness flagged for the grader: of the five raw-signaled items,
  ONE carries FLASH-equivalent significance concern for the grader's
  consideration when assessing brief inclusion priority —

  (1) PM-001 CISA KEV three-add: TWO of the three additions are
      corpus-tracked CVE state changes (CVE-2026-45321 VT-006 KEV-
      pending watch signal FIRED + CVE-2026-48027 corpus finding-0011
      KEV-listed). Per FLASH-POLICY Trigger 1, KEV listing constitutes
      CISA-attested active-exploitation. HOWEVER both CVEs have been
      brief-covered across multiple briefs for 15+ days (VT-006) and
      7+ days (CVE-2026-48027 finding-0011); the KEV addition is a
      STATE CHANGE on tracked CVEs, not a new disclosure. Whether
      this constitutes Trigger 1 firing material or absorption-under-
      existing-locks material is grader-side disposition.

  The other four (PM-002, PM-003, PM-004, PM-005) are clearly non-
  FLASH grader-queue items at the source / WEP / single-source-veto
  / restatement-vs-new layer.

hard_rules_compliance:
  rule_2_no_attribution_origination: |
    PM-001: TeamPCP attribution on VT-006 / CVE-2026-45321 carries
    forward from existing corpus disposition (Wiz + StepSecurity +
    Snyk lineage); CISA KEV does not publish actor attribution. NO
    upgrade to APT alias. PM-002: OX Security explicitly declines
    attribution on mouse5212-super-formatter; NO cross-walk to
    TeamPCP / Mini Shai-Hulud / Shai-Hulud / GlassWorm despite
    tradecraft adjacency. PM-003: Black Shadow / Ababil of Minab
    preserved verbatim per Gambit Security via The Record relay;
    NO cross-walk to MuddyWater (#022) or Handala Hack (#014)
    despite shared MOIS designation; Handala/Stryker reference
    preserved as tangential contextual mention only. PM-004: no
    attribution claim on Yamcs CVE-2026-44632 (researcher-disclosure
    /vendor-coordinated patch class). PM-005: CrowdStrike's pattern-
    based Russian attribution on GlassWorm preserved verbatim; NEW
    indicators (CIS-locale + Russian-language code comments + Hultquist
    GTIG confirmation) recorded as CrowdStrike-attested-via-Register-
    relay findings, NOT collector-originated attribution upgrades.
    GlassWorm roster attribution-field-update (unknown → RU
    possibility) flagged for operator /update-tracking decision, NOT
    collector-side action.
  rule_3_no_exploitation: |
    No PoC code, no payloads, no exploit guides referenced or
    generated. CVE-2026-44632 Yamcs GHSA advisory body contains PoC
    (PATCH request to MDB override endpoint with injected Java
    payload) — explicitly NOT copied to PM-004 per Hard Rule 3. CVE
    referenced by ID + advisory URL only. PM-001 CISA shortDescription
    paraphrased to under 15-word excerpts per Rule 6. PM-005 C2
    channels described architecturally only (Solana / BitTorrent DHT /
    Google Calendar / VPS) without operational details.
  rule_4_passive_only: |
    No active scans. SpiderFoot not invoked. authorized-targets.yaml
    empty. All sources are passive RSS / WebFetch / KEV / Splunk over
    Archimedes's own indices.
  rule_6_quote_limit: |
    All direct quotes within 15-word ceiling, one-per-source. PM-001
    CISA shortDescription segmented to two ≤15-word excerpts. PM-002
    researchers' positioning paraphrased. PM-003 attribution language
    fragments preserved at under-15-word level. PM-005 Hultquist
    quote paraphrased.
  rule_7_credentials: "PM-002 records existence-of-leaked-GitHub-private-token in OX Security primary per relay; token VALUE NOT recorded per Hard Rule 7. No other credential exposure surfaced."
  rule_8_splunk_first_party_priority: |
    Targeted 42-IOC sweep on -9h@h = ZERO non-archimedes-internal
    events across both indices. 67th consecutive dormant non-self
    sweep on defenseclaw_local. Hard Rule 8: silence is not
    disconfirming, not confirming.

pm_27_brief_surfaces_recommended:
  - CISA KEV three-add (PM-001) — HEADLINE — corpus state change on
    two tracked surfaces (VT-006 KEV-pending FIRED + CVE-2026-48027
    finding-0011 KEV-listed); BOD 22-01 dueDate 2026-06-10 (T+14)
    creates hard line for DIB / CMMC partner-flow estates inheriting
    FCEB compliance. Headline for PM-27 brief.
  - Yamcs CVE-2026-44632 (PM-004) — A&D-DIRECT — spacecraft mission
    control software RCE; CVSS 9.1 post-auth high-priv; PATCHED 5.12.7;
    parallel to corpus VT-005 OpenC3 COSMOS class; VT-010 scaffolding
    candidate. Sector Focus: A&D bullet.
  - LACMTA Iran second-relay enrichment (PM-003) — Iran Cyber Watch
    standing section update; new alias "Ababil of Minab" surfaces;
    investigation inv-2026-05-26-001 carry-forward update; absorb
    under finding-2026-05-27-0004.
  - GlassWorm Russian-pattern enrichment (PM-005) — fourth relay
    layer with new operational indicators (CIS-locale + Russian-
    language code comments + GlasswormRAT named tool + Hultquist
    GTIG confirmation); absorb under finding-2026-05-27-0001 with
    attribution enrichment; operator decision flagged for roster
    attribution field update.
  - mouse5212 npm Claude AI (PM-002) — supply-chain structural-
    warning class; absorb under thematic structural-supply-chain
    section alongside AM-27 findings 0003 + 0005 + carry-forwards
    from finding-2026-05-14-0008 / finding-2026-05-20-FLASH-0001;
    fifth-in-class for the AI-developer-tooling-ecosystem under
    sustained supply-chain pressure thematic arc.

notes:
  - "PM-27 pre-brief collection sweep: 28 in-window items across 8.33h window. FIVE raw-signaled. FIVE absorbed under active corpus locks. EIGHTEEN DISCARDED per Mode 1."
  - "HEADLINE FINDING for PM-27: CISA KEV three-add today 12:00 UTC. Two of three additions are corpus-tracked state changes (VT-006 / CVE-2026-45321 KEV-pending FIRED; CVE-2026-48027 Nx Console finding-2026-05-20-FLASH-0001 KEV-listed). Third addition (CVE-2026-8398 Daemon Tools Lite) is out-of-scope for corpus tracking."
  - "A&D-DIRECT FINDING: Yamcs CVE-2026-44632 — open-source spacecraft mission control software RCE; CVSS 9.1; patched at disclosure; parallel to corpus VT-005 OpenC3 COSMOS class. VT-010 scaffolding candidate for vuln-tracker."
  - "MANDIANT ENDPOINT CANONICALIZATION (eighth-time-pending): mandiant.com/resources/blog/rss.xml = EIGHTH consecutive recovery vs cloud.google.com parse-error pattern. Operator decision elevated to urgency-pending tier."
  - "VOLEXITY (fifth-consecutive parse-error): STALE FLIP RECOMMENDATION ELEVATED to operator-decision-required."
  - "Splunk first-party: 42-IOC targeted sweep -9h@h returned ZERO non-archimedes-internal events. 67th consecutive dormant non-self sweep on defenseclaw_local. Hard Rule 8: silence is not disconfirming."
  - "Hard Rules: Rule 2 — attribution recorded per source language with no cross-walks (KEV procedural-cataloging-vs-TeamPCP-corpus separation maintained; OX Security explicit decline; Ababil of Minab / Black Shadow no cross-walk to MuddyWater/Handala; Yamcs no attribution; GlassWorm Russian-pattern enrichment NOT collector-originated upgrade); Rule 3 — no PoC content (Yamcs GHSA PoC explicitly NOT copied); Rule 4 — passive only; Rule 6 — quotes under 15-word ceiling segmented as needed; Rule 7 — no credential values recorded; Rule 8 — defenseclaw_local 67th consecutive dormant non-self sweep."
  - "PRIORITY for grader: PM-001 (CISA KEV three-add) is the headline item for the PM-27 brief — corpus state change on two tracked surfaces is the highest-priority signal class today. PM-004 (Yamcs A&D-direct) is second-tier sector-focus material. PM-003 + PM-005 are absorption-under-existing-locks enrichments. PM-002 is structural-supply-chain-warning class for cumulative thematic treatment."
  - "TLP:CLEAR."
---

# PM-27 EDT Wednesday pre-brief collection sentinel

This sentinel documents the 2026-05-27 15:30 EDT scheduled PM pre-brief
collection sweep. Window: 2026-05-27T07:35 → 2026-05-27T15:55 EDT
(8.33h, spanning AM-27 pre-brief end + 12:00 FLASH + PM-27 pre-window).
**Five raw-signaled items**, five absorbed under active anti-noise
locks, eighteen discarded.

## Sweep outcome

Of 21 A/B-grade publication surfaces queried (CISA KEV + CISA all.xml +
THN + BC + SecurityWeek + The Record + Dark Reading + The Register +
Mandiant via mandiant.com path + Unit 42 + MSTIC + CrowdStrike + Check
Point Research + Cisco Talos + SANS ISC + Rapid7 + SentinelOne +
WeLiveSecurity + Sophos attempted + Krebs + Volexity attempted + GitHub
Security advisories + Splunk first-party), **28 in-window items**
returned. **Five raw-signaled** (PM-001 through PM-005). **Five
absorbed under active corpus locks** (THN GlassWorm restatement,
BC GlassWorm restatement, BC FBI Silent Ransom restatement, SW
Pretalx XSS restatement from FLASH-1200, The Register GlassWorm
restatement). **Eighteen DISCARDED per Mode 1**.

The **headline signal for PM-27 brief is PM-001** — CISA KEV
three-additions today 12:00 UTC, with TWO of the three additions
being corpus-tracked state changes: **CVE-2026-45321 (VT-006 Mini
Shai-Hulud KEV-pending watch signal FIRED)** and **CVE-2026-48027
(Nx Console; corpus finding-2026-05-20-FLASH-0001 KEV-listed)**.
BOD 22-01 dueDate 2026-06-10 (T+14) for both creates hard federal
deadline pressure on DIB / CMMC partner-flow estates inheriting FCEB
compliance.

Second-tier signal: **PM-004 Yamcs CVE-2026-44632** —
A&D-direct disclosure of a critical RCE in open-source spacecraft
mission control software (CVSS 9.1, patched 5.12.7); parallel to
corpus VT-005 OpenC3 COSMOS class. Recommend vuln-tracker scaffold
VT-010 (or next available slot) for this CVE.

Third-tier signals: **PM-003 LACMTA Iran second-relay enrichment**
(new "Ababil of Minab" alias from The Record / Gambit Security) and
**PM-005 GlassWorm Russian-pattern enrichment** (new operational
indicators: CIS-locale + Russian-language code comments + GlasswormRAT
named tool + Hultquist GTIG confirmation) — both absorption-under-
existing-locks enrichment surfaces.

Fourth-tier signal: **PM-002 mouse5212 npm Claude AI** (OX Security
unattributed supply-chain class) — fifth-in-class for the AI-
developer-tooling-ecosystem under sustained supply-chain pressure
thematic arc.

## Raw-signal file list

| ID | Title | Source | Trigger-class |
|---|---|---|---|
| PM-001 | CISA KEV three-add — CVE-2026-45321 TanStack/Mini Shai-Hulud + CVE-2026-48027 Nx Console + CVE-2026-8398 Daemon Tools | CISA KEV catalog 2026.05.27 | Corpus state change on two tracked CVEs |
| PM-002 | OX Security via THN — Malicious npm `mouse5212-super-formatter` Claude AI exfil | THN (relay) / OX Security (primary) | Supply-chain UNATTRIBUTED class |
| PM-003 | The Record via Gambit Security — LACMTA Iran Ababil of Minab MOIS attribution | The Record (Smalley) / Gambit Security (primary) | Iran Cyber Watch second-relay enrichment |
| PM-004 | GitHub Advisory — CVE-2026-44632 Yamcs server-side code injection RCE — spacecraft mission control | GitHub Security Advisory Database / Yamcs maintainers | A&D-direct sector-focus CVE |
| PM-005 | The Register via CrowdStrike CAO — GlassWorm takedown Russian-pattern operational indicator enrichment | The Register / CrowdStrike + Google GTIG (Hultquist) | Tracked actor (#005) attribution enrichment |

## Source health summary

- **Mandiant**: mandiant.com/resources/blog/rss.xml — **EIGHTH**
  consecutive recovery. Endpoint canonicalization recommendation
  elevated to operator-decision-pending urgency tier.
- **Volexity**: **FIFTH** consecutive XML parse error
  (`<unknown>:17:68 not well-formed`). Held healthy per operator
  policy across five sweeps; stale flip recommendation ELEVATED to
  operator-decision-required.
- **Sophos**: en-us subpath stale persists (since 2026-05-17);
  root-path news.sophos.com/feed/ workaround documented.
- **CrowdStrike**: persistent-dateless-marketing pattern continues
  for 9 of 10 items; useful content surfaces only via dated relays
  (today via SecurityWeek + BC + THN + The Register; all four
  absorbed under AM-27 lock or enrichment via PM-005).
- **Dark Reading**: WebFetch-403-on-article-body reduces yield to
  headline-tier only (similar to Wired pattern).
- All other healthy A/B sources reachable.

## Splunk first-party check

42-IOC targeted sweep on `-9h@h` returned ZERO non-archimedes-internal
events across both indices. ZERO defenseclaw_local hits. ZERO IOC
matches on tracked-actor or tracked-vuln or LA-Metro-investigation or
KEV-added-CVE strings. **67th consecutive dormant non-self sweep on
defenseclaw_local.** Hard Rule 8: silence is not disconfirming.

## TLP

TLP:CLEAR.
