---
source: archimedes-internal
source_grade: N/A
collected_at: 2026-05-27T07:35:00-04:00
sweep: pre-brief-2026-05-27-am
url: null
test: false
sentinel: true
sweep_type: pre-brief-collection
status: complete
mode: pre_brief_collection
invocation: scheduled pre-brief AM-27 cycle (07:30 EDT)
sweep_window:
  start: 2026-05-26T15:30:00-04:00
  end: 2026-05-27T07:35:00-04:00
  duration_h: 16.08
prior_sweep_anchor:
  sweep_id: flash-2026-05-27-0600
  anchor_at: 2026-05-27T06:12:00-04:00
  raw_id: raw-2026-05-27-flash-0600-000-sentinel-clean-sweep.md
  commit_sha: 3f6d527
  disposition: zero_triggers_fired
  notes: |
    The 06:00 EDT scheduled dawn FLASH sentinel was the FIFTH
    consecutive clean sweep across the Tuesday + Wednesday
    transition. Carried forward to this AM-27 pre-brief: (1) Mandiant
    endpoint canonicalization recommendation (FIVE consecutive
    recoveries on mandiant.com/resources/blog/rss.xml vs cloud.google
    parse-error pattern); (2) Volexity retry-or-MCP decision
    (recurring parse-error pattern); (3) ReliaQuest operator
    decision; (4) Aikido retry-eligibility evaluation; (5) LA Metro /
    Black Shadow / MOIS SecurityWeek 05:33 EDT relay layer for Iran
    Cyber Watch standing section consideration (investigation
    inv-2026-05-26-001 carry-forward); (6) CVE-2026-9082 Drupal T-0
    deadline-day framing (today Wed EOB ~10h from this sweep at PEAK
    urgency).
prior_brief_anchor:
  brief_id: 2026-05-26-afternoon
  shipped_at: 2026-05-26T16:00:00-04:00
  commit_sha: 1faa252
  notes: |
    PM-26 afternoon brief anchors corpus disposition through this
    AM-27 morning brief. Two AM-26 findings (UNC1549 / Nimbus
    Manticore primary upgrade, CISA KEV LiteSpeed cPanel addition)
    plus the morning's five AM-26 findings remain in active anti-
    noise lock posture through AM-27 brief horizon.

match_reason:
  watchlist:
    - aerospace-manufacturers-sector-named-in-gitea-cve-2026-27771
  actors:
    - GlassWorm (roster #005, HIGH) — CrowdStrike Counter Adversary
      Operations published primary disruption / takedown report
      2026-05-26 14:00 UTC; SecurityWeek 06:10 EDT relay.
  vulnerabilities:
    - VT-005   # CVE-2026-9082 Drupal — KEV deadline T-0 TODAY Wed at EOB ~10h, PEAK urgency
    - VT-008   # CVE-2026-42897 Exchange — KEV deadline T-2 Fri 2026-05-29, anti-noise lock active
    - VT-009   # CVE-2026-48172 LiteSpeed cPanel — KEV deadline T-2 Fri 2026-05-29, anti-noise lock active
    - VT-006   # CVE-2026-45321 Mini Shai-Hulud — KEV-absent watch lineage
  keywords:
    - GlassWorm
    - CrowdStrike
    - Megalodon
    - SafeDep
    - Ox Security
    - Tiledesk
    - SymJack
    - Adversa
    - Gitea
    - CVE-2026-27771
    - aerospace manufacturers
    - Black Shadow
    - LA Metro
    - MOIS
    - cryptojacking
    - ScreenConnect
    - Charter
    - ShinyHunters
    - LiteSpeed cPanel
    - Drupal SQLi
    - KnowledgeDeliver

triage_tags:
  - pre_brief_sentinel
  - am_pre_brief_scheduled
  - tracked_actor_disruption_glassworm_crowdstrike_primary
  - supply_chain_attack_megalodon_github_actions
  - supply_chain_attack_symjack_ai_coding_agents
  - aerospace_manufacturers_sector_named_gitea_cve
  - iran_cyber_watch_la_metro_black_shadow_mois_relay
  - cryptojacking_ai_chatbot_seo_mstic_primary
  - shinyhunters_charter_confirmation_40m_records
  - kev_t_0_drupal_deadline_today_at_eob
  - kev_t_2_exchange_friday
  - kev_t_2_litespeed_friday
  - mandiant_endpoint_canonicalization_recommendation_persisting
  - volexity_recurring_parse_error_defer

iocs_extracted: false
iocs_count: 0
text_word_count: 1850
promoted: false
ttl_expires_at: 2026-08-25T07:35:00-04:00

sources_queried:
  - cisa-kev               # WebFetch known_exploited_vulnerabilities.json — catalogVersion 2026.05.26 UNCHANGED since 2026-05-26T13:02 EDT addition of CVE-2026-48172 LiteSpeed cPanel. ZERO net-new KEV adds across the 16h window since 2026-05-26 15:30. Recent additions all corpus-tracked: CVE-2026-48172 LiteSpeed (2026-05-26 due Fri T-2), CVE-2026-9082 Drupal (2026-05-22 due TODAY T-0 at EOB ~10h), CVE-2026-42897 Exchange (2026-05-15 due Fri T-2), CVE-2025-34291 Langflow + CVE-2026-34926 Trend Micro Apex One (both 2026-05-21 due 2026-06-04), CVE-2008-4250 Microsoft Windows + CVE-2009-1537 Microsoft DirectX (both 2026-05-20 due 2026-06-03, retro-additions).
  - cisa-advisories        # fetch_feed cisa.gov/cybersecurity-advisories/all.xml — 200 OK, 30 items in feed, 0 in 16h window since PM-26 15:30 EDT.
  - thehackernews          # fetch_feed feedburner — 200 OK; last_modified Wed 27 May 2026 11:10 GMT. 2 in-window items — (1) Gitea CVE-2026-27771 (07:35 EDT this sweep — published 06:06 EDT, in-window) — RAW-SIGNALED as AM-003 (aerospace-manufacturers sector named in Noscope research, structural A&D-SDLC relevance via private container-image disclosure on CI/CD repos). (2) AI Chatbot Cryptojacking (03:45 EDT — relay of MSTIC primary) — MSTIC primary RAW-SIGNALED as AM-006 (Microsoft Defender Experts research on ScreenConnect-DLL-sideload + GPU mining + ~150 gleeze.com domains; no roster / no A&D / B-grade MSTIC but published 2026-05-26T17:35 EDT in PM-window).
  - bleepingcomputer       # fetch_feed — 200 OK; last_modified Wed 27 May 2026 11:26 GMT. 5 in-window items — (1) CISA LiteSpeed 4-day patch (06:06 EDT today) — ABSORBED under active anti-noise lock cve-2026-48172-litespeed-cpanel-plugin-kev-deadline-tracking (PM-26 finding-0008 canonical disposition; no new exploitation telemetry, no victim names, no IR-firm corroboration). (2) Dutch police Ajax football (05:09 EDT) — DISCARDED no scope. (3) Win11 KB5089573 (04:33 EDT) — DISCARDED no security CVE. (4) KnowledgeDeliver zero-day Godzilla web shell (2026-05-26T16:07 EDT yesterday, Ionut Ilascu) — ABSORBED under active anti-noise lock cve-2026-5426-knowledgedeliver-godzilla-cobalt-strike-mandiant-gtig (AM-26 finding-2026-05-26-0005 canonical disposition; lock expires at 08:00 AM-27 brief horizon ~25 min from this sweep). (5) Charter / ShinyHunters confirmation (2026-05-26T15:46 EDT yesterday, Lawrence Abrams) — RAW-SIGNALED as AM-007 (40M records confirmed by Charter, Salesforce-Entra vishing tradecraft pattern that's analogous to Scattered Spider #013 but ShinyHunters NOT in _roster.yaml — Hard Rule 2 no cross-walk; consumer-telecom victim no A&D; ShinyHunters / 7-Eleven 24h anti-noise lock EXPIRED at 06:00 EDT today so this fresh BC piece is in scope).
  - securityweek           # fetch_feed feedburner — 200 OK; last_modified Wed 27 May 2026 11:01 GMT. 8 in-window items — (1) Lastwall $11.5M raise (11:01 EDT today, future from sweep time) — DISCARDED funding announcement no threat-intel. (2) Credential Crisis stolen-credentials feature (10:30 EDT today) — DISCARDED feature article no fresh threat-intel claim. (3) SymJack AI Coding Agents (06:15 EDT today, Kevin Townsend) — RAW-SIGNALED as AM-004 (Adversa AI research on symlink-hijack against Claude Code / Gemini CLI / Cursor / Grok Build / GitHub Copilot — novel attack class against AI-coding-agent supply chain; no tracked-actor; no A&D-prime named). (4) GlassWorm Botnet Disrupted (06:10 EDT today, Ionut Arghire) — relay of CrowdStrike Counter Adversary Operations primary 2026-05-26 14:00 UTC; tracked actor GlassWorm #005 — RAW-SIGNALED as AM-001 (CrowdStrike PRIMARY captured; SecurityWeek relay corroborates). (5) LA Metro Cyberattack Iran linkage (05:33 EDT today, Eduard Kovacs) — RAW-SIGNALED as AM-005 per AM-27 follow-up from 06:00 sentinel (Iran Cyber Watch standing section surface; Black Shadow NOT in _roster.yaml, Hard Rule 2 no cross-walk to MuddyWater / Handala despite MOIS service match; investigation inv-2026-05-26-001 lock active through 2026-06-09). (6) FBI Silent Ransom Group USB-drop (04:33 EDT today) — DISCARDED already at 06:00 sentinel (law firms, no roster, no A&D). (7) CISA LiteSpeed 4-day relay (02:55 EDT today) — ABSORBED under existing lock. (8) Anthropic Claude Sandbox (02:43 EDT today) — DISCARDED vendor product announcement.
  - the-record             # fetch_feed therecord.media/feed — 200 OK; 5 items in feed, 0 in 16h window after since-filter.
  - dark-reading           # fetch_feed darkreading.com/rss.xml — 200 OK; last_modified Wed 27 May 2026 11:32 GMT. 3 items — (1) Megalodon Malware Infects Thousands GitHub Repos (2026-05-26T15:47 EDT yesterday, Rob Wright) — RAW-SIGNALED as AM-002 (5,561 repos in 6h, SafeDep PRIMARY + Ox Security secondary; Mini Shai-Hulud / TeamPCP lineage adjacent — SafeDep explicitly references prior TeamPCP GitHub compromise as preceding event; Ox Security mentions Mini Shai-Hulud; no explicit Megalodon attribution to specific group). (2) Infosecurity Europe event 2026-06-02 — DISCARDED event-calendar. (3) Anatomy of a Data Breach event 2026-06-18 — DISCARDED event-calendar.
  - mandiant (mandiant.com path)               # fetch_feed mandiant.com/resources/blog/rss.xml — 200 OK (SIXTH consecutive recovery; canonical productive endpoint), 20 items in feed, 0 in 16h window. Endpoint canonicalization recommendation persists. NOT retried cloud.google.com endpoint this sweep to avoid thrashing.
  - unit42                 # fetch_feed feedburner — 200 OK; last_modified Tue 26 May 2026 16:56 GMT (= 12:56 EDT pre-window unchanged across six sweeps). 0 items in 16h window.
  - mstic                  # fetch_feed microsoft.com/en-us/security/blog/feed — 200 OK; last_modified Tue 26 May 2026 21:35 GMT (= 17:35 EDT IN WINDOW). 1 in-window item — Microsoft Defender Experts cryptojacking primary (poisoned search results + AI chatbots + ScreenConnect abuse + DLL sideload + GPU mining + ~150 gleeze.com domains) — RAW-SIGNALED as AM-006.
  - crowdstrike            # fetch_feed crowdstrike.com/blog/feed/ — 200 OK; last_modified Wed 27 May 2026 04:17 GMT (= 00:17 EDT IN WINDOW header refresh). 10 items, ALL published: null per persistent-dateless-marketing pattern. BUT one item title is GlassWorm Disruption (Counter Adversary Operations byline) — this CrowdStrike primary IS the originating source for the SecurityWeek 06:10 EDT relay. WebFetched as part of AM-001 raw-signal composition. CrowdStrike persistent-dateless pattern continues for other 9 items (Gartner MQ, Falcon AIDR, Claude integration, infostealers, Patch Tuesday May 2026, automated leads); ALL DISCARDED off-scope.
  - checkpoint-research    # fetch_feed research.checkpoint.com/feed — 200 OK; last_modified Tue 26 May 2026 12:13 GMT (= 08:13 EDT pre-window unchanged across six sweeps). 0 in window.
  - cisco-talos            # fetch_feed blog.talosintelligence.com/rss/ — 200 OK; 15 items in feed, 1 in 16h window — EvidenceForge synthetic-log tool (06:00 EDT, David J. Bianco, Tool Talk class) — DISCARDED as at 06:00 sentinel (no threat-intel claim).
  - sans-isc               # fetch_feed isc.sans.edu/rssfeed.xml — 200 OK; last_modified Wed 27 May 2026 11:29 GMT. 1 in-window item — Wednesday Stormcast podcast detail (02:00 EDT, awareness-only metadata) — DISCARDED no body content.
  - volexity               # fetch_feed volexity.com/blog/feed — XML parse error (<unknown>:17:68: not well-formed invalid token) — FOURTH consecutive same-class failure. failure_count 3→4 past-threshold. Holding healthy per established operator instruction pending alt-endpoint decision; recommendation to AM-27 PM-pre-brief: consider stale flip if pattern persists through 12:00 / 15:30 sweeps OR identify alt-endpoint (volexity.com homepage WebFetch).
  - krebs                  # fetch_feed krebsonsecurity.com/feed — 200 OK; last_modified Mon 25 May 2026 13:21 GMT (= 09:21 EDT 2026-05-25 well pre-window unchanged). 0 in 16h window.
  - reliaquest             # fetch attempted via /feed endpoint — 404 Not Found. NOT in source-grades.yaml current entry list with a working RSS URL. Operator decision required: either alt-endpoint discovery (reliaquest.com/blog/feed, threatintel.reliaquest.com, etc.) OR remove from sweep until MCP build.
  - aikido-security        # fetch attempted via /feed.xml endpoint — 404 Not Found. Same pattern as reliaquest — operator alt-endpoint or removal decision required.
  - splunk-archimedes      # mcp__splunk-query targeted 41-IOC sweep on -14h@h INCLUDING GlassWorm, Megalodon, SafeDep, Ox Security, SymJack, Adversa, build-bot, ci-bot infrastructure, 164.92.88.210 sinkhole, gleeze.com, ScreenConnect, Tiledesk, Charter, ShinyHunters, Black Shadow, LACMTA, CVE-2026-9082 / 48172 / 42897 / 27771 cluster, UNC1549 / MuddyWater / APT34 / APT28 / APT29 / Lazarus / Sandworm / Volt Typhoon / Salt Typhoon / TeamPCP / LockBit / Cl0p / Shai-Hulud / Scattered Spider. ONE event returned — Archimedes' own flash_sweep self-logging from 06:00 sentinel (archimedes:operation sourcetype, contains tracked-actor strings in payload). ZERO non-archimedes-internal events.
  - splunk-defenseclaw     # included in the cross-index 14h sweep; ZERO events. 66th consecutive dormant non-self sweep on defenseclaw_local (incremented from 65 at 06:00 FLASH).

splunk_first_party_check:
  query: 'search index=archimedes OR index=defenseclaw_local earliest=-14h@h latest=now ("GlassWorm" OR "Megalodon" OR "SafeDep" OR "Ox Security" OR "SymJack" OR "Adversa" OR "build-bot" OR "build-system@noreply.dev" OR "ci-bot@automated.dev" OR "164.92.88.210" OR "gleeze.com" OR "ScreenConnect" OR "Tiledesk" OR "Charter" OR "ShinyHunters" OR "Black Shadow" OR "LACMTA" OR CVE-2026-9082 OR CVE-2026-48172 OR CVE-2026-42897 OR CVE-2026-27771 OR UNC1549 OR "Nimbus Manticore" OR "Charming Kitten" OR MuddyWater OR APT34 OR APT37 OR Lazarus OR APT28 OR APT29 OR Sandworm OR "Volt Typhoon" OR "Salt Typhoon" OR TeamPCP OR LockBit OR Cl0p OR "Shai-Hulud" OR "Scattered Spider") | head 50'
  result: 1 event returned — Archimedes' own 06:00 FLASH sentinel self-logging payload (sourcetype=archimedes:operation; contains tracked-actor strings as part of self-described flash_sweep event). ZERO non-archimedes-internal events. ZERO defenseclaw_local hits. ZERO IOC matches.
  consecutive_dormant_sweeps_defenseclaw: 66    # incremented from 65 at 06:00 FLASH
  iac_ioc_hits_in_defenseclaw_local: 0
  hard_rule_8_framing: |
    Targeted 41-IOC sweep across the full carried-forward corpus
    IOC set PLUS net-new tokens from this pre-brief window
    (GlassWorm, Megalodon, SafeDep, Ox Security, SymJack, Adversa,
    build-bot CI/CD infrastructure, 164.92.88.210 CrowdStrike
    sinkhole, gleeze.com cryptojacking infra, Charter / ShinyHunters
    consumer-telecom victim, Black Shadow / LACMTA / Iran tokens
    given active investigation inv-2026-05-26-001) on
    defenseclaw_local + archimedes -14h@h returned ZERO
    non-archimedes-internal events. 66th consecutive dormant non-self
    sweep on defenseclaw_local. Hard Rule 8: silence is not
    disconfirming, not confirming.

filter_evaluation_summary:
  in_window_items_total: 21
  in_window_items_evaluated: 21
  in_window_items_raw_signaled: 7
  in_window_items_corpus_restatement_anti_noise_absorbed: 3
  in_window_items_discarded_off_scope: 11
  notes: |
    Twenty-one in-window items across A/B-grade surveyed surfaces.
    SEVEN raw-signaled (one per tracked-actor disruption + four
    supply-chain / Iran / cryptojacking + one A&D-adjacent CVE +
    one consumer-telecom breach). THREE absorbed under active
    anti-noise locks (BC LiteSpeed restatement + SW LiteSpeed
    restatement + BC KnowledgeDeliver restatement). ELEVEN
    DISCARDED per Mode 1 (no watchlist / no roster / no vuln-index
    hit, OR not threat-intel-actionable content).

source_health_changes:
  - source_yaml_id: mandiant
    observation: |
      mandiant.com/resources/blog/rss.xml endpoint returned 200 OK
      with 20 items in feed (SIXTH consecutive recovery observation
      across PM-26 12:00 / 18:00 / 00:00 / 06:00 / this pre-brief
      AM-27). Endpoint canonicalization recommendation persists:
      canonicalize mandiant.com/resources/blog/rss.xml as productive
      Mandiant endpoint in source-grades.yaml. NOT retried
      cloud.google.com/blog/topics/threat-intelligence endpoint this
      sweep to avoid thrashing. NO runtime field change applied
      this sweep — operator-set `notes:` preservation rule honored.
    runtime_change_applied: no_change_endpoint_canonicalization_recommendation_persisting
  - source_yaml_id: volexity
    observation: |
      www.volexity.com/blog/feed/ returned XML parse error
      (<unknown>:17:68: not well-formed invalid token) — FOURTH
      consecutive same-class failure. failure_count 3→4 past-
      threshold. Held healthy per long-standing operator instruction
      pending alt-endpoint decision. Recommendation to next sweep
      (12:00 FLASH or 15:30 PM pre-brief): consider stale flip if
      pattern persists OR identify alt-endpoint (volexity.com
      homepage WebFetch, alt /blog path).
    runtime_change_applied: failure_count_3_to_4_held_healthy_pending_operator_decision_documented_only
  - source_yaml_id: crowdstrike
    observation: |
      crowdstrike.com/blog/feed/ returned 200 OK; 10 items, ALL
      published: null per persistent-dateless-marketing pattern
      documented across 16+ consecutive prior sweeps. HOWEVER one
      item is the Counter Adversary Operations primary on GlassWorm
      Disruption (RAW-SIGNALED as AM-001 via WebFetch). The CrowdStrike
      feed's dateless metadata required cross-correlation with
      SecurityWeek's 06:10 EDT relay timestamp to anchor the
      publication date as 2026-05-26 14:00 UTC. Pattern of useful
      content surfacing only via dated relays continues; consider
      alt-endpoint discovery for dated feed.
    runtime_change_applied: no_change_pattern_persistent_useful_primary_extracted_via_webfetch
  - source_yaml_id: cisco-talos
    observation: |
      blog.talosintelligence.com/rss/ returned 200 OK; 1 in-window
      item (EvidenceForge Tool Talk class, no threat-intel content).
      Source remains healthy; cadence is multi-day mix.
    runtime_change_applied: no_change_healthy
  - source_yaml_id: reliaquest
    observation: |
      Per AM-27 follow-up from 06:00 sentinel. Fetch attempt against
      reliaquest.com/feed returned 404 Not Found. Source has no
      working RSS URL in current configuration. OPERATOR DECISION
      REQUIRED: (a) discover alt-endpoint (reliaquest.com/blog/feed,
      threatintel.reliaquest.com, /resources/blog/feed); (b) remove
      from sweep until MCP build; (c) WebFetch-only-on-demand for
      specific findings.
    runtime_change_applied: operator_decision_required_no_working_url
  - source_yaml_id: aikido
    observation: |
      Per AM-27 follow-up from 06:00 sentinel. Fetch attempt against
      aikido.dev/feed.xml returned 404 Not Found. Same pattern as
      reliaquest. OPERATOR DECISION REQUIRED: same alternatives as
      reliaquest.
    runtime_change_applied: operator_decision_required_no_working_url

source_health_runtime_field_updates:
  - source_yaml_id: cisa-kev
    field: last_successful_fetch
    new_value: 2026-05-27T07:32:00-04:00
    rationale: WebFetch of catalogVersion 2026.05.26 succeeded; no new adds since 2026-05-26T13:02 EDT; healthy.
  - source_yaml_id: cisa-advisories
    field: last_successful_fetch
    new_value: 2026-05-27T07:32:00-04:00
    rationale: fetch_feed cisa.gov all.xml succeeded 200 OK; 30 items; healthy.
  - source_yaml_id: bleepingcomputer
    field: last_successful_fetch
    new_value: 2026-05-27T07:31:00-04:00
    rationale: fetch_feed 200 OK; 5 items in window; productive.
  - source_yaml_id: securityweek
    field: last_successful_fetch
    new_value: 2026-05-27T07:31:00-04:00
    rationale: fetch_feed 200 OK; 8 items in window; productive.
  - source_yaml_id: the-record
    field: last_successful_fetch
    new_value: 2026-05-27T07:31:00-04:00
    rationale: fetch_feed 200 OK; 5 items in feed total; 0 in window.
  - source_yaml_id: mstic
    field: last_successful_fetch
    new_value: 2026-05-27T07:31:00-04:00
    rationale: fetch_feed 200 OK; 1 in-window item (Defender Experts cryptojacking primary 2026-05-26T21:35 UTC).
  - source_yaml_id: unit42
    field: last_successful_fetch
    new_value: 2026-05-27T07:31:00-04:00
    rationale: fetch_feed 200 OK; 0 in window; healthy.
  - source_yaml_id: crowdstrike
    field: last_successful_fetch
    new_value: 2026-05-27T07:31:00-04:00
    rationale: fetch_feed 200 OK; one productive item (GlassWorm) via WebFetch correlation.
  - source_yaml_id: cisco-talos
    field: last_successful_fetch
    new_value: 2026-05-27T07:31:00-04:00
    rationale: fetch_feed 200 OK; 1 in-window item.
  - source_yaml_id: mandiant
    field: last_error
    new_value: "feedburner.com/Mandiant returned 404 on 2026-05-27T07:35 AM pre-brief — long-standing pattern; alt mandiant.com/resources/blog/rss.xml endpoint produces SIXTH consecutive recovery this sweep (200 OK, 20 items, 0 in window). Operator canonicalization decision still pending."
    rationale: Held healthy per long-standing source-health policy; operator alt-endpoint decision still open.
  - source_yaml_id: volexity
    field: failure_count
    new_value: 4
    rationale: FOURTH consecutive XML parse error <unknown>:17:68 not well-formed invalid token. Held healthy per operator instruction pending alt-endpoint decision.
  - source_yaml_id: volexity
    field: last_error
    new_value: "2026-05-27 07:35 AM pre-brief sweep: www.volexity.com/blog/feed/ returned malformed body (XML parse error <unknown>:17:68 not well-formed invalid token) — FOURTH consecutive same-class failure. Recommendation: stale flip if persists through 12:00 / 15:30 OR alt-endpoint identification."

trigger_evaluation_note: |
  This is a pre-brief collection sweep, NOT a FLASH sweep. FLASH-trigger
  evaluation belongs to the FLASH-sweep mode. However, for situational
  awareness flagged for the grader: of the seven raw-signaled items,
  TWO carry potential FLASH-equivalent significance for the grader's
  consideration when assessing brief inclusion priority —
  (1) AM-001 GlassWorm tracked-actor (#005) DISRUPTION by CrowdStrike
      A-grade primary — significance is that this is a CHANGED state
      for a tracked actor (operational neutralization) rather than a
      NEW attribution or NEW TTP; per FLASH-POLICY Trigger 4 it's
      TTP-change-adjacent but the change is DESTRUCTIVE-of-actor not
      additive, so Trigger 4 framing is non-canonical. Grader-side
      decision on brief framing.
  (2) AM-002 Megalodon GitHub supply-chain attack (5,561 repos in 6h,
      SafeDep PRIMARY + Ox Security secondary) — Mini Shai-Hulud /
      TeamPCP lineage adjacency per SafeDep + Ox Security peer
      mentions but NO explicit attribution to those tracked surfaces.
      Per FLASH-POLICY this is supply-chain-attack-class signal
      requiring multi-victim + tracked-actor attribution; Megalodon
      campaign meets multi-victim prong (5,561 repos) but FAILS
      tracked-actor attribution prong (UNATTRIBUTED per SafeDep + Ox
      Security explicit decline). Grader-side disposition.

hard_rules_compliance:
  rule_2_no_attribution_origination: |
    AM-001 records CrowdStrike attribution language verbatim ("the
    criminals are likely based in Russia") with no upgrade to APT
    alias. AM-002 records SafeDep + Ox Security explicit
    UNATTRIBUTED disposition with peer-mention of TeamPCP and Mini
    Shai-Hulud as lineage references but NO cross-walk. AM-005
    records SecurityWeek + Gambit + Israel National Cyber Directorate
    framing on Black Shadow + MOIS with NO cross-walk to MuddyWater /
    Handala Hack despite MOIS service match (investigation
    inv-2026-05-26-001 documents Hard Rule 2 compliance).
  rule_3_no_exploitation: |
    No PoC code, no payloads, no exploit guides referenced or
    generated. CISA LiteSpeed cPanel relay does not include exploit
    primitives; AM-006 MSTIC primary describes domain pattern only
    (~150 gleeze.com domains); AM-002 Megalodon coverage describes
    GitHub Actions workflow injection mechanism but does NOT provide
    working payload.
  rule_4_passive_only: |
    No active scans. SpiderFoot not invoked.
    authorized-targets.yaml empty. All sources are passive RSS /
    WebFetch / KEV / Splunk over Archimedes's own indices.
  rule_6_quote_limit: |
    Quotes preserved verbatim ONLY where attribution language matters
    (CrowdStrike "the criminals are likely based in Russia" — 7 words;
    Charter "No sensitive personal information (PI) or customer
    proprietary network information (CPNI) data was exfiltrated" —
    15 words; both under 15-word ceiling).
  rule_7_credentials: "No credential exposure surfaced in any raw-signaled item."
  rule_8_splunk_first_party_priority: |
    Targeted 41-IOC sweep on -14h@h = 0 non-archimedes-internal
    events across both indices. 66th consecutive dormant non-self
    sweep on defenseclaw_local. Hard Rule 8: silence is not
    disconfirming, not confirming.

anti_noise_locks_active_inherited_from_06_00_sentinel:
  - lock_id: cve-2026-9082-drupal-core-sqli-kev-deadline-tracking
    status: ACTIVE — T-0 deadline TODAY Wed EOB ~10h from this sweep at PEAK urgency; AM-27 morning brief is canonical deadline-day surface
  - lock_id: cve-2026-42897-exchange-owa-xss-kev-deadline-tracking
    status: ACTIVE — T-2 deadline Fri 2026-05-29
  - lock_id: cve-2026-48172-litespeed-cpanel-plugin-kev-deadline-tracking
    status: ACTIVE — T-2 deadline Fri 2026-05-29; BC 06:06 EDT + SW 02:55 EDT both ABSORBED this sweep
  - lock_id: cve-2026-45321-mini-shai-hulud-oidc-credential-abuse-kev-absent-watch
    status: ACTIVE
  - lock_id: unc1549-screening-serpens-tradecraft-evolution-2026-tradecraft-rats-azure-staging
    status: ACTIVE through 2026-05-27 16:00 (~8h remaining)
  - lock_id: ckr-ai-threat-landscape-digest-march-april-2026
    status: ACTIVE — EXPIRES at 08:00 EDT this morning (~25 min from this sweep)
  - lock_id: cve-2026-5426-knowledgedeliver-godzilla-cobalt-strike-mandiant-gtig
    status: ACTIVE — EXPIRES at 08:00 EDT this morning (~25 min from this sweep); BC 16:07 EDT yesterday ABSORBED this sweep
  - lock_id: inv-2026-05-26-001-lacmta-iran-attribution-black-shadow-ababil-of-minab-apt-iran-cyberaveng3rs
    status: ACTIVE through 2026-06-09 T+14; SW 05:33 EDT today Black Shadow + MOIS relay ABSORBED this sweep (AM-005 RAW-SIGNALED for grader-side decision on Iran Cyber Watch standing section)

am_27_brief_surfaces_recommended:
  - GlassWorm tracked-actor disruption (AM-001) — high-priority,
    CrowdStrike A-grade primary, tracked actor #005 changed state
  - Megalodon GitHub supply-chain attack (AM-002) — high-priority
    structural supply-chain warning for A&D-SDLC; UNATTRIBUTED;
    SafeDep + Ox Security; relates to Mini Shai-Hulud (VT-006) /
    TeamPCP roster lineage
  - Gitea CVE-2026-27771 unauth private container disclosure (AM-003)
    — aerospace-manufacturers sector explicitly named in source;
    Noscope research
  - SymJack AI-coding-agent supply chain attack (AM-004) — novel
    attack class against Claude Code + 4 others; Adversa AI; for
    standing AI section consideration
  - LA Metro / Black Shadow / MOIS (AM-005) — Iran Cyber Watch
    standing section surface; investigation lock active
  - MSTIC ScreenConnect GPU-cryptojacking primary (AM-006) — A-grade
    Microsoft primary on AI-chatbot-poisoning + DLL-sideload + ~150
    gleeze.com domains; structural supply-chain warning class for
    A&D-developer-population indirect exposure
  - Charter / ShinyHunters confirmation (AM-007) — 40M records;
    consumer-telecom victim with no A&D direct hit but Salesforce-
    Entra vishing tradecraft pattern analogous to Scattered Spider
    (#013); for standing supply-chain / identity-attack consideration

notes:
  - "AM-27 pre-brief collection sweep: 21 in-window items across 16h window from PM-26 15:30. SEVEN raw-signaled. THREE absorbed under active corpus locks. ELEVEN DISCARDED per Mode 1."
  - "ENDPOINT CANONICALIZATION RECOMMENDATION (persisting from 06:00 sentinel): Mandiant mandiant.com/resources/blog/rss.xml = SIXTH consecutive recovery vs cloud.google.com/blog/topics/threat-intelligence parse-error pattern; operator should canonicalize productive endpoint and document retirement-vs-dual-probe of the cloud.google.com path."
  - "VOLEXITY: fourth consecutive parse-error; held healthy per operator instruction; flag for stale flip decision at next sweep."
  - "RELIAQUEST + AIKIDO: AM-27 follow-up — both 404 on attempted /feed endpoints; OPERATOR DECISION required on alt-endpoint discovery or removal."
  - "Splunk first-party: 41-IOC targeted sweep -14h@h returned ZERO non-archimedes-internal events. 66th consecutive dormant non-self sweep on defenseclaw_local. Hard Rule 8: silence is not disconfirming."
  - "Hard Rules: Rule 2 — attribution recorded per source language with no cross-walks (CrowdStrike GlassWorm-Russian, SafeDep/Ox Megalodon-UNATTRIBUTED, SW Black Shadow-MOIS-via-Gambit); Rule 3 — no PoC content; Rule 4 — passive only; Rule 6 — quotes under 15-word ceiling; Rule 7 — no credentials; Rule 8 — defenseclaw_local 66th consecutive dormant non-self sweep."
  - "PRIORITY for grader: AM-001 (GlassWorm disruption — tracked actor #005 changed state) is the headline item for the AM-27 brief — CrowdStrike A-grade primary on tracked-actor takedown is the rarest signal class in the corpus to date. AM-002 (Megalodon GitHub supply chain) and AM-003 (Gitea aerospace-manufacturers sector-named CVE) are second-tier. AM-004 SymJack and AM-006 MSTIC cryptojacking are structural-supply-chain-warning class for AI-developer-tooling exposure (A&D-SDLC indirect)."
  - "AM-27 morning brief is CANONICAL DEADLINE-DAY surface for CVE-2026-9082 Drupal SQLi T-0 TODAY Wed EOB."
  - "TLP:CLEAR."
---

# AM-27 EDT Wednesday pre-brief collection sentinel

This sentinel documents the 2026-05-27 07:30 EDT scheduled AM pre-brief
collection sweep. Window: 2026-05-26T15:30 → 2026-05-27T07:35 EDT
(16.08h, spanning yesterday PM-26 pre-brief end + overnight + this
morning pre-window). **Seven raw-signaled items**, three absorbed under
active anti-noise locks, eleven discarded.

## Sweep outcome

Of 18 A/B-grade publication surfaces queried (CISA KEV + CISA all.xml +
THN + BC + SecurityWeek + The Record + Dark Reading + Mandiant via
mandiant.com path + Unit 42 + MSTIC + CrowdStrike + Check Point Research
+ Cisco Talos + SANS ISC + Volexity attempted + Krebs + ReliaQuest
attempted + Aikido attempted + Splunk first-party), twenty-one in-window
items returned. **Seven raw-signaled** (AM-001 through AM-007).
**Three absorbed under active corpus locks** (BC LiteSpeed restatement,
SW LiteSpeed restatement, BC KnowledgeDeliver restatement). **Eleven
DISCARDED per Mode 1**.

The headline signal for AM-27 brief is **AM-001 GlassWorm tracked-actor
disruption by CrowdStrike A-grade primary** — tracked actor #005
operationally neutralized via four-channel C2 takedown coordinated with
Google and Shadowserver Foundation. This is the rarest signal class in
the Archimedes corpus to date: a state change on a tracked roster
actor via A-grade vendor takedown report.

Second-tier signals: **AM-002 Megalodon GitHub supply-chain attack**
(5,561 repos in 6h, SafeDep PRIMARY + Ox Security secondary; Mini
Shai-Hulud / TeamPCP lineage adjacent but UNATTRIBUTED); **AM-003
Gitea CVE-2026-27771** (aerospace-manufacturers sector explicitly
named in Noscope research, unauth pre-auth private container image
disclosure on CI/CD repos).

## Raw-signal file list

| ID | Title | Source | Trigger-class |
|---|---|---|---|
| AM-001 | GlassWorm botnet disruption by CrowdStrike + Google + Shadowserver | CrowdStrike Counter Adversary Operations PRIMARY + SecurityWeek (Arghire) relay | Tracked actor #005 state change |
| AM-002 | Megalodon GitHub supply-chain attack — 5,561 repos in 6h | SafeDep PRIMARY + Ox Security secondary + SecurityWeek (Arghire) + Dark Reading (Wright) relays | Supply-chain UNATTRIBUTED multi-victim |
| AM-003 | Gitea CVE-2026-27771 unauth private container disclosure — aerospace manufacturers sector named | THN (Lakshmanan) via Noscope research | A&D-sector-adjacent CVE |
| AM-004 | SymJack — symlink hijack against AI coding agents (Claude Code + 4 others) | SecurityWeek (Townsend) via Adversa AI research | Novel attack class supply chain |
| AM-005 | LA Metro Iran linkage — Black Shadow + MOIS per Israel National Cyber Directorate via Gambit | SecurityWeek (Kovacs) | Iran Cyber Watch standing section relay |
| AM-006 | MSTIC cryptojacking PRIMARY — AI chatbot poisoning + ScreenConnect + DLL sideload + ~150 gleeze.com domains + GPU mining | MSTIC (Microsoft Defender Experts Research Team) | Supply-chain structural warning |
| AM-007 | Charter Communications confirms ShinyHunters 40M records breach via Salesforce-Entra vishing | BC (Abrams) | Consumer-telecom no-A&D but tradecraft analogous to Scattered Spider |

## Source health summary

- **Mandiant**: mandiant.com/resources/blog/rss.xml — SIXTH consecutive
  recovery. Endpoint canonicalization recommendation persists.
- **Volexity**: FOURTH consecutive XML parse error
  (`<unknown>:17:68 not well-formed`). Held healthy pending operator
  decision; recommend stale flip if persists.
- **CrowdStrike**: persistent-dateless-marketing pattern continues for
  9 of 10 items; HOWEVER one item this sweep IS the productive
  GlassWorm primary (Counter Adversary Operations) — surfaced via
  WebFetch correlation with SecurityWeek's dated relay.
- **ReliaQuest + Aikido**: both 404 on attempted `/feed` endpoints —
  operator alt-endpoint or removal decision required.
- All other healthy A/B sources reachable.

## Splunk first-party check

41-IOC targeted sweep on `-14h@h` returned ZERO non-archimedes-internal
events across both indices. ZERO defenseclaw_local hits. ZERO IOC
matches on tracked-actor or tracked-vuln or LA-Metro-investigation
strings. **66th consecutive dormant non-self sweep on
defenseclaw_local.** Hard Rule 8: silence is not disconfirming.

## TLP

TLP:CLEAR.
