---
raw_id: raw-2026-05-12-flash-0600-000
collected_at: 2026-05-12T06:08:00-04:00
run_id: flash-sweep-20260512-060000
collection_mode: flash_sweep
sweep_type: flash
sweep_time: 2026-05-12T06:00:00-04:00
time_window_start: 2026-05-12T00:00:00-04:00
time_window_end: 2026-05-12T06:00:00-04:00
test: false
sources_queried:
  - cisa-kev               # JSON feed via WebFetch — top 10 most recent entries returned. ZERO entries with dateAdded >= 2026-05-11 (full-catalog scan corroborated by 00:00 sweep). Most recent KEV addition remains CVE-2026-42208 (BerriAI LiteLLM, dateAdded 2026-05-08, dueDate 2026-05-11 EOB now passed yesterday). KEV-listed deadlines passed/upcoming this week (CVE-2024-1708 ConnectWise ScreenConnect dueDate 2026-05-12 = TODAY; CVE-2026-32202 Microsoft Windows dueDate 2026-05-12 = TODAY; CVE-2026-31431 Linux Kernel dueDate 2026-05-15 = T+3d). KEV catalog does not publish compliance-status changes against passed deadlines.
  - cisa-advisories        # all.xml RSS via fetch_feed — status 200, 30 items in feed total, 0 items in 6h window after since-filter.
  - bleepingcomputer       # RSS via fetch_feed — status 200, etag d3de396c37742510827ba9a461be42d2, last_modified 2026-05-12T09:53:59 GMT (05:53 EDT within window from feed-server activity), 1 item in 6h window after since-filter — "Instructure reaches 'agreement' with ShinyHunters to stop data leak" (Sergiu Gatlan, 2026-05-12T09:23:56 UTC = 05:23 EDT in-window). Edtech extortion settlement; NO threat-intel, NO A&D, NO actor. DISCARDED per Mode 1 procedure.
  - securityweek           # RSS via fetch_feed — status 200, etag W/e8c6cafde0dd5edc69f6d970adb972d0, last_modified 2026-05-12T04:14:42 GMT (00:14 EDT in-window from feed-server activity), 0 items in 6h window after since-filter. Homepage WebFetch confirmed top 10 headlines are 2026-05-11-dated already-covered topics (Frame Security $50M funding, Build Application Firewalls editorial, Google AI-zero-day, Skoda data breach, Cloudflare layoffs, SailPoint GitHub repo, Checkmarx Jenkins, Canvas online, Dirty Frag Linux, Crimenetwork takedown). The Mini Shai-Hulud story has NOT yet reached SecurityWeek as of this 06:00 sweep (anticipated for 12:00 FLASH).
  - the-record             # RSS via fetch_feed — status 200, 5 items total in feed, 0 items in 6h window after since-filter (most recent dated 2026-05-08; weekend cadence quiet through Monday into Tuesday morning).
  - krebs                  # RSS via fetch_feed — status 200, last_modified 2026-05-12T02:20:41 GMT pre-window from this sweep's start (22:20 EDT 2026-05-11 = just-pre-window), 0 items in 6h window — normal Krebs cadence.
  - mstic                  # RSS via fetch_feed (microsoft.com/en-us/security/blog/feed/) — status 200, last_modified 2026-05-11T17:38:35 GMT pre-window, 0 items in 6h window. Most recent MSTIC content remains 2026-05-08T17:12 UTC Dirty Frag active-attack post (~109h aged at this sweep). MSTIC has NOT yet published a fresh active-attack post for Mini Shai-Hulud 2026-05-12 burst; the Shai-Hulud lineage corroboration cites the December 2025 MSTIC defender's guide + Defender for Cloud SBOM-scan product capability per WebSearch.
  - unit42                 # RSS (feedburner) via fetch_feed — status 200, last_modified 2026-05-11T22:51:12 GMT (18:51 EDT 2026-05-11 = pre-window), 0 items in 6h window. The Unit 42 "Inside AD CS Escalation" piece from 2026-05-11 18:00 EDT was just at the edge of the 00:00 sweep window — covered at 00:00 sweep and discarded as historical-context-only restatement (Fighting Ursa = APT28 alias). The npm threat landscape backbone piece (cited in Mini Shai-Hulud A-grade corroboration) was last-updated 2026-05-01 pre-window.
  - sans-isc               # RSS via fetch_feed (rssfeed.xml) — XML parse error this sweep ("could not be parsed as RSS/Atom: <unknown>:2:0: syntax error"). Same class as the 2026-05-10 18:00 transient failure that recovered next sweep. SINGLE soft-fail; failure_count 0→1; held healthy pending next-sweep retry given prior pattern of transient site-side issues.
  - rapid7                 # RSS via fetch_feed (rapid7.com/blog/rss/) — status 200, last_modified 2026-05-12T09:46:33 GMT (05:46 EDT within window from feed-server activity), 0 items in 6h window after since-filter.
  - crowdstrike            # RSS via fetch_feed — status 200, etag "15d5-65197e83158b3-gzip", last_modified 2026-05-12T05:12:17 GMT (01:12 EDT within window from feed-server activity), 10 items returned ALL with null published_at (SIXTEENTH consecutive sweep with the dateless marketing pattern across 9+ days). Same pile (Automated Leads AI threat detection, Gartner MQ leader, Falcon OverWatch for Defender, Technical Risk Assessments, AI Vuln Discovery podcast, CORDIAL/SNARKY SPIDER product-marketing, ChatGPT Enterprise audit logging, Frost & Sullivan CNAPP, Google Cloud detection expansion, Falcon Cloud Security ROI). Pattern fully entrenched.
  - sentinelone-labs       # RSS via fetch_feed (sentinelone.com/labs/feed/) — status 200, etag W/1c9232cf89238de946381ca496ee6085, last_modified 2026-05-12T01:33:43 GMT (within window from feed-server activity but no fresh body content), 0 items in 6h window.
  - sophos                 # RSS via fetch_feed (news.sophos.com/feed/) — status 200, 9 items total in feed, 0 items in 6h window.
  - eset-welivesecurity    # RSS via fetch_feed — status 200, 100 items total in feed, 0 items in 6h window.
  - hacker-news            # WebFetch on thehackernews.com/ index — 10 most recent articles listed. THREE new 2026-05-12-dated items vs. 00:00 sweep: (1) "Mini Shai-Hulud Worm Compromises TanStack, Mistral AI, Guardrails AI & More Packages" (Ravie Lakshmanan, 2026-05-12) — RAW-SIGNALED as FLASH-0600-001 with full FLASH-trigger evaluation; (2) "Instructure Reaches Ransom Agreement with ShinyHunters to Stop 3.65TB Canvas Leak" (2026-05-12) — same Instructure topic as BleepingComputer relay this sweep, edtech extortion, DISCARDED; (3) "OpenAI Launches Daybreak for AI-Powered Vulnerability Detection and Patch Validation" (2026-05-12) — defensive product announcement (OpenAI new cybersec capability with Akamai/Cisco/Cloudflare/CrowdStrike/Fortinet/Oracle/PaloAlto/Zscaler integrations), NO threats, NO IOCs, NO actors, DISCARDED per Mode 1. The "iOS 26.5 Brings Default End-to-End Encrypted RCS Messaging Between iPhone and Android" headline is consumer-product news, DISCARDED. Remaining 6 items (TeamPCP Checkmarx Jenkins / cPanel Mr_Rot13 / AI-developed 2FA bypass / Weekly Recap / Purple Team editorial / Fake OpenAI HF repo) are pre-window or anti-noise-applies.
  - cloud-google-blog-mandiant  # WebFetch on cloud.google.com/blog/topics/threat-intelligence top page — top-5 visible titles unchanged from 2026-05-11 sweeps (Proactive Preparation 2026 Edition, Look What You Made Us Patch 2025 Zero-Days, Ransomware Under Pressure, DarkSword iOS, M-Trends 2026) — all previously triangulated as out-of-window via WebSearch. NO fresh GTIG content this 6h window. Mandiant feedburner endpoint /Mandiant continues 404 (SIXTEENTH consecutive); failure_count 14→15.
  - nvd                    # WebFetch on services.nvd.nist.gov/rest/json/cves/2.0?lastModStartDate=2026-05-12T04:00:00.000-04:00&lastModEndDate=2026-05-12T10:00:00.000-04:00 for the 6h window. cvssV3Severity=CRITICAL → 0 results. cvssV3Severity=HIGH → 3 results: CVE-2026-22550 (ELECOM WRC-X1500GS-B wireless router OS command injection 8.8, authenticated, 2026-02-03 disclosure NVD lastModified is metadata refresh); CVE-2026-2993 (AI Chatbot & Workflow Automation by AIWU WordPress plugin SQLi 7.5 unauthenticated, ≤1.4.17); CVE-2026-6690 (LifePress WordPress plugin stored XSS 7.2, ≤2.2.2). NONE matches A&D / tracked-actor / tracked-vuln filter set. All three DISCARDED per Mode 1 procedure (no watchlist / roster / vuln-index hit). NOTE: CVE-2026-45321 (Mini Shai-Hulud TanStack supply-chain compromise, CVSS 9.6, GHSA-g7cv-rxg3-hmpx) is NOT in this 6h NVD lastModStartDate window result set — likely because the GHSA/CVE coordination timestamp is the npm registry assignment time, not yet mirrored to NVD lastModified per the typical 24-48h NVD lag pattern. Captured via Snyk's CVE coordination citation in FLASH-0600-001 instead. NVD endpoint remains healthy and responsive.
  - splunk-archimedes      # search NOT sourcetype=archimedes:* over 6h returned zero events; same over 24h zero events. Targeted IOC keyword sweep across 25 high-priority tokens (APT28/APT29/UNC1549/Charming Kitten/MuddyWater/APT34/APT37/APT40/APT41/Volt Typhoon/Salt Typhoon/Lazarus/Sandworm/Scattered Spider/TeamPCP/Mr_Rot13/Shai-Hulud + CVE-2026-0300/6973/42208/41940/45321/2024-1708/32202/31431) over 24h returned 6 hits — ALL six are archimedes:operation pipeline self-references (flash_sweep_clean 06:00 EDT 2026-05-11, brief_published morning 08:16 EDT 2026-05-11, brief_published afternoon 16:47 EDT 2026-05-11, flash_sweep operator-initiated 17:00 EDT 2026-05-11, flash_sweep_clean 00:00 EDT 2026-05-12, and 18:03 EDT 2026-05-11 operation). Pipeline self-references match keyword tokens in JSON payloads but reflect Archimedes' own operational logging, NOT external observations. The Mini Shai-Hulud IOCs (filev2.getsession[.]org, api.masscan[.]cloud, git-tanstack.com, 83.142.209[.]194, three SHA-256 file hashes, Session-network recipient ID, dead-drop catbox URLs) specifically tested against archimedes index — zero matches.
  - splunk-defenseclaw     # NOT sourcetype=archimedes:* over 6h returns zero events; over 24h also zero. SIXTEENTH consecutive sweep with dormant non-archimedes-internal stream pattern across both indexes. Same Mini Shai-Hulud IOC keyword sweep — zero matches.
sources_skipped_stale:
  - censys                 # MCP not built (deferred to Session 11+)
  - urlscan                # MCP not built (deferred to Session 11+)
  - hibp                   # No API key configured (HIBP_API_KEY missing from .env)
  - x-cisagov              # STALE since 2026-05-10 12:00 FLASH — three consecutive WinError 10060 nitter.net timeouts. >40h since stale-flip = eligible-to-retry per 24h rule, but FLASH-fast scope kept to RSS/vendor/KEV priority feeds; treating as effectively stale until operator nitter-pool / direct-X-API decision.
  - x-gossithedog          # STALE since 2026-05-09 — nitter.net account permanently delisted. >76h since stale flip but FLASH-fast scope kept; treating as effectively stale.
  - ars-security           # STALE since 2026-05-09 — feeds.arstechnica.com/arstechnica/security 404. Workaround in use (arstechnica.com/feed/ root path); root path not invoked this sweep — quiet-hours overnight cadence makes Ars site-wide unlikely to break fresh A&D-relevant signal in 6h window.
sources_skipped_softfail_this_sweep:
  - threatfox              # CAPTCHA wall via WebFetch (auth-injection limitation), awaiting MCP build priority
  - malwarebazaar          # awaiting MCP build priority
  - github-advisories      # 406 Not Acceptable on global advisories.atom (per-repo GHSA fallback path remains productive workaround when triggered; not triggered this sweep)
  - proofpoint             # /us/threat-insight/blog/feed endpoint 404 since 2026-05-10 12:00 FLASH; alt /us/rss.xml corporate-news endpoint multi-day cadence, not invoked this sweep
  - iran-monitor           # iranmonitor.org 403 WAF/UA workaround pending
sources_health_changed_this_sweep:
  - mandiant               # feedburner.com/Mandiant continues 404 (SIXTEENTH consecutive); failure_count 14→15. cloud.google.com index page WebFetch surfaced same top-5 visible titles as 2026-05-11 sweeps (all out-of-window per prior triangulations). Held healthy pending operator alt-endpoint decision.
  - sans-isc               # rssfeed.xml XML parse error this sweep ("<unknown>:2:0: syntax error") — same class as 2026-05-10 18:00 transient failure. failure_count 0→1. Held healthy pending next-sweep retry given prior recovery pattern.
match_reason:
  watchlist: []
  actors: [TeamPCP]    # via Mini Shai-Hulud raw-signal
  vulnerabilities: [CVE-2026-45321]    # via Mini Shai-Hulud raw-signal
  keywords:
    - supply-chain-worm
    - mini-shai-hulud
    - validly-attested-malicious-packages
    - slsa-attestation-bypass
triage_tags:
  - flash_candidate_surfaced_one_topic
  - sentinel
  - quiet_hours_active
  - mini_shai_hulud_teampcp_flash_candidate_companion_to_001
  - mandiant_feedburner_16th_consecutive_404
  - splunk_dormant_16th_consecutive
  - sans_isc_transient_xml_parse_error_held_healthy
  - distinct_from_checkmarx_jenkins_2026_05_11_topic_by_eight_dimensional_comparison
  - openai_daybreak_product_announcement_discarded
  - apple_ios_26_5_consumer_product_discarded
  - instructure_shinyhunters_extortion_settlement_discarded
flash_triggers_evaluated:
  trigger_1_critical_cve_exploited:
    matched: true
    matching_raw_signal: raw-2026-05-12-flash-0600-001
    notes: |
      CVE-2026-45321 (Mini Shai-Hulud TanStack supply-chain compromise,
      CVSS 9.6, GHSA-g7cv-rxg3-hmpx) PASSES the strict conjunction.
      169-172 npm packages compromised in 2026-05-11 19:20-19:26 UTC
      burst with attacker-published malicious versions live on
      registries before maintainer revert. A-grade source naming
      operational layer: Wiz (provisional A — high-confidence TeamPCP
      attribution), Snyk (provisional A — Stephen Thoemmes byline, CVE
      coordination), Unit 42 (A in source-grades.yaml — backbone npm
      threat landscape), MSTIC (A — Shai-Hulud 2.0 lineage + Defender
      for Cloud SBOM-scan capability). See FLASH-0600-001 for full
      detail.
  trigger_2_tracked_actor_attribution:
    matched: false
    notes: |
      TeamPCP attribution to the Shai-Hulud lineage is pre-existing
      (finding-2026-05-04-0003 MSTIC baseline on PyTorch Lightning
      ShaiWorm; raw-2026-05-11-flash-0600-001 Checkmarx Jenkins).
      Today's StepSecurity/Wiz/Snyk attribution to Mini Shai-Hulud
      is a new CAMPAIGN under an existing attributed actor, NOT a
      new attribution event. Strict structural test FAIL.
  trigger_3_first_party_ioc_hit:
    matched: false
    notes: |
      Splunk archimedes + defenseclaw_local combined sweep over 6h
      window returns zero non-archimedes-internal events. Same over
      24h returns zero non-archimedes-internal events. Targeted IOC
      keyword sweep across 25 tokens (15 tracked actor aliases + 10
      priority CVEs including this-sweep CVE-2026-45321) over 24h
      returned 6 hits — all six are archimedes:operation pipeline
      self-references. Mini Shai-Hulud IOCs specifically tested
      against both indexes — zero matches. Trigger 3 cannot fire on
      a dormant non-Archimedes stream. SIXTEENTH consecutive sweep
      with the dormant pattern.
  trigger_4_tracked_actor_ttp_change:
    matched: true
    matching_raw_signal: raw-2026-05-12-flash-0600-001
    notes: |
      Clean PASS. New tooling (first documented npm worm producing
      validly-attested malicious packages — breaks SLSA assurance
      model), new infrastructure (dual-ecosystem self-propagation
      npm + PyPI in single campaign; Session-network dead-drop C2
      architecture). Clearly attributable to TeamPCP (#001 HIGH) per
      Wiz "high confidence" + StepSecurity originating + Snyk
      corroboration. See FLASH-0600-001 for full detail.
  trigger_5_ad_sector_campaign:
    matched: false
    notes: |
      @squawk aviation developer ecosystem (19 packages including
      flightplan/weather/mcp) is sector-adjacent but INCIDENTALLY
      hit by the worm's maintainer-enumeration mechanism, NOT
      explicitly targeted. NO A&D prime named as victim. Genuine
      but indirect A&D relevance flagged for grader/analyst SDLC-
      dependency-graph enumeration. Per the strict structural-test
      reading applied to prior sector-adjacent cases (SailPoint
      AM-001 2026-05-11; OpenC3 COSMOS AM-001 2026-05-09; HookedWing
      FLASH-0000-001 2026-05-11), Trigger 5 FAIL on "explicitly
      targeting" criterion.
  trigger_6_zero_day_no_patch:
    matched: false
    notes: |
      Supply-chain compromise remediation model (package version
      reversion + token rotation) is type-mismatch for the "unpatched
      orphan vulnerability in deployed product" structural fit
      Trigger 6 contemplates. Maintainers reverted within hours of
      initial compromise. N/A.
  critical_override_evaluated:
    applied: false
    conditions_satisfied: 2 of 4
    conditions_failed:
      - cvss_10_0 (actual: 9.6 < 10.0 floor)
      - ad_watchlist_targeted (actual: no A&D prime named as victim)
    notes: |
      Override requires ALL FOUR. TWO satisfied (active exploitation
      ✓, tracked actor ✓). TWO failed. Override FAILS by hard
      thresholds. Quiet-hours rule (06:00 EDT inside 21:00-09:00)
      remains in force regardless — composed FLASH brief would queue
      to flash-queue.yaml for 09:00 catchup, not direct post.

anti_noise_observations:
  - topic: Mini-Shai-Hulud-TanStack-Mistral-npm-PyPI-worm
    prior_flash_in_24h: false
    prior_corpus_coverage: |
      Shai-Hulud lineage exists in corpus via:
      - finding-2026-05-04-0003 (PyTorch Lightning ShaiWorm; MSTIC
        active analysis baseline; TeamPCP attribution baseline)
      - raw-2026-05-11-flash-0600-001 (Checkmarx Jenkins AST plugin;
        TeamPCP attribution; DIFFERENT TOPIC per 8-dimension
        comparison table in FLASH-0600-001 of this sweep)
      The 2026-05-12 Mini Shai-Hulud burst is a NEW CAMPAIGN with
      novel capability layer (validly-attested-malicious-packages,
      first documented), distinct from the 2026-05-04 ShaiWorm
      (PyPI-only PyTorch Lightning single-package) and the
      2026-05-11 Checkmarx Jenkins (Jenkins Marketplace single-
      plugin).
    this_sweep_evidence:
      - "Hacker News 'Mini Shai-Hulud Worm Compromises TanStack, Mistral AI, Guardrails AI & More Packages' (Ravie Lakshmanan, 2026-05-12)"
      - "Wiz Research 'Mini Shai-Hulud Strikes Again: TanStack + more npm Packages Compromised' (2026-05-12; provisional A)"
      - "Snyk 'TanStack npm Packages Hit by Mini Shai-Hulud' (Stephen Thoemmes byline, 2026-05-11; provisional A; CVE-2026-45321 coordination)"
      - "Aikido / SafeDep / StepSecurity / Endor Labs / Semgrep / Onapsis multi-firm corroboration"
    resurface_conditions_evaluated:
      new_iocs: true                        # CVE-2026-45321 + 6 C2 domains + 1 IP + 3 SHA-256 hashes + recipient ID + catbox URLs + PBKDF2 salt + 4 new aliases — all new
      independent_a_grade_corroboration: true   # Wiz provisional A + Snyk provisional A + Unit 42 A backbone + MSTIC A lineage; multiple independent firms
      novel_post_exploitation_ttps: true   # First documented npm worm producing validly-attested malicious packages (SLSA bypass); dual-ecosystem self-propagation; Session-network exfiltration
    disposition: |
      Resurface conditions all three TRUE. NEW raw-signal write at
      FLASH-candidate severity is correct disposition. Anti-noise
      "one FLASH per topic per 24h" applies per-TOPIC; Mini Shai-Hulud
      is distinct from Checkmarx Jenkins (2026-05-11 06:00 FLASH)
      per the 8-dimension comparison table in FLASH-0600-001.
  - topic: OpenAI-Daybreak-AI-defensive-product-announcement
    prior_corpus_coverage: none (new vendor product launch)
    this_sweep_evidence:
      - "Hacker News 'OpenAI Launches Daybreak for AI-Powered Vulnerability Detection and Patch Validation' (2026-05-12)"
    disposition: Defensive product announcement — no threats, no actors, no CVEs, no IOCs. DISCARDED per Mode 1.
  - topic: Instructure-Canvas-ShinyHunters-extortion-settlement
    prior_corpus_coverage: |
      Instructure / Canvas / ShinyHunters thread previously surfaced
      across 2026-05-08 to 2026-05-11 sweeps in source-health notes
      as edtech extortion subject. Not in tracked threat-actor
      roster.
    this_sweep_evidence:
      - "BleepingComputer 'Instructure reaches agreement with ShinyHunters to stop data leak' (Sergiu Gatlan, 2026-05-12T05:23 EDT)"
      - "Hacker News 'Instructure Reaches Ransom Agreement with ShinyHunters to Stop 3.65TB Canvas Leak' (2026-05-12)"
    disposition: Edtech consumer-data extortion settlement; ShinyHunters not in _roster.yaml; Canvas not in aerospace-defense.yaml. DISCARDED per Mode 1.
  - topic: Apple-iOS-26-5-end-to-end-encrypted-RCS-messaging
    this_sweep_evidence:
      - "Hacker News 'iOS 26.5 Brings Default End-to-End Encrypted RCS Messaging Between iPhone and Android' (2026-05-12)"
    disposition: Consumer-product news. DISCARDED.

flash_candidates:
  - raw_id: raw-2026-05-12-flash-0600-001
    trigger_primary: trigger_4_tracked_actor_ttp_change
    trigger_secondary: trigger_1_critical_cve_exploited
    trigger_detail: |
      Mini Shai-Hulud TanStack/Mistral/UiPath/DraftLab npm + PyPI
      worm. CVE-2026-45321 CVSS 9.6. TeamPCP (#001 HIGH) attribution
      via StepSecurity/Wiz/Snyk multi-firm corroboration. Novel
      capability: first documented npm worm producing validly-
      attested malicious packages (SLSA attestation bypass). Dual-
      ecosystem self-propagation across npm + PyPI in 169-172
      packages / 403 versions in 48-hour window 2026-05-11 to
      2026-05-12.
    actor_attributed: TeamPCP (roster #001 HIGH)
    watchlist_hit: false
    watchlist_adjacency: aviation_developer_ecosystem_squawk_19_packages
    ad_sector: false (adjacent, not explicit-targeting)
    cvss_score: 9.6
    cvss_floor_met: true (>= 9.0 Trigger 1)
    cvss_override_floor_met: false (< 10.0 critical override)
    active_exploitation_confirmed: true
    a_grade_source_named_operational_layer: true
    sources_a_grade:
      - wiz (provisional A on first surface, high-confidence TeamPCP attribution)
      - snyk (provisional A on first surface, Stephen Thoemmes byline, CVE coordination)
      - unit42 (A in source-grades.yaml, backbone npm landscape)
      - mstic (A in source-grades.yaml, Shai-Hulud 2.0 lineage + Defender SBOM-scan)
    sources_b_grade:
      - stepsecurity (provisional B, originating attribution)
      - semgrep (provisional B)
      - onapsis (provisional B, SAP-security-focused)
    sources_c_grade:
      - aikido-security (provisional C on first surface)
      - safedep (provisional C on first surface)
    expected_wep_procedural_facts: very_likely
    expected_wep_operational_claim: likely
    red_team_review_required: true
    red_team_rationale: |
      WEP >= very-likely triggers mandatory red-team review per
      FLASH-POLICY anti-noise rule. The "first documented validly-
      attested" novelty claim is the load-bearing technical
      assertion benefitting from independent peer challenge.
    briefer_composition_required: true
    briefer_disposition: queue_to_flash_queue_for_09_00_catchup_sweep_per_quiet_hours
    briefer_prefix: QUEUED FROM OVERNIGHT

splunk_first_party_24h_sweep:
  query_archimedes: zero non-archimedes-internal events
  query_defenseclaw_local: zero non-archimedes-internal events
  targeted_keyword_token_hits: 6 hits, all pipeline self-references (archimedes:operation sourcetype)
  consecutive_dormant_sweeps: 16
  trigger_3_status: cannot_fire_on_dormant_stream
  mini_shai_hulud_specific_ioc_keyword_sweep:
    domains_tested:
      - filev2.getsession[.]org
      - seed1.getsession[.]org
      - seed2.getsession[.]org
      - seed3.getsession[.]org
      - api.masscan[.]cloud
      - git-tanstack[.]com
    ips_tested:
      - 83.142.209[.]194
    hashes_tested:
      - ab4fcadaec49c03278063dd269ea5eef82d24f2124a8e15d7b90f2fa8601266c
      - 2ec78d556d696e208927cc503d48e4b5eb56b31abc2870c2ed2e98d6be27fc96
      - 2258284d65f63829bd67eaba01ef6f1ada2f593f9bbe41678b2df360bd90d3df
    matches: 0

source_health_changes:
  - source_yaml_id: mandiant
    runtime_field: failure_count
    old_value: 14
    new_value: 15
    rationale: "feedburner.com/Mandiant returns 404 sixteenth consecutive; cloud.google.com destination page top-5 titles unchanged from 2026-05-11 sweeps. Held healthy pending operator alt-endpoint decision."
  - source_yaml_id: sans-isc
    runtime_field: failure_count
    old_value: 0
    new_value: 1
    rationale: "isc.sans.edu/rssfeed.xml XML parse error '<unknown>:2:0: syntax error' — same class as 2026-05-10 18:00 transient. Held healthy pending next-sweep retry given prior recovery pattern."
    last_error_update: "isc.sans.edu/rssfeed.xml returned XML parse error on 2026-05-12T06:00 FLASH — single soft-fail of same class as 2026-05-10 18:00 transient; held healthy pending next-sweep retry."
  - source_yaml_id: bleepingcomputer
    runtime_field: last_successful_fetch
    old_value: 2026-05-12T00:00:00-04:00
    new_value: 2026-05-12T06:00:00-04:00
    rationale: "RSS reachable status 200; 1 in-window item (Instructure/ShinyHunters settlement) DISCARDED per Mode 1."
  - source_yaml_id: securityweek
    runtime_field: last_successful_fetch
    old_value: 2026-05-12T00:00:00-04:00
    new_value: 2026-05-12T06:00:00-04:00
    rationale: "RSS reachable status 200; 0 in-window items; Mini Shai-Hulud not yet reached SecurityWeek (anticipated 12:00 FLASH)."
  - source_yaml_id: krebs
    runtime_field: last_successful_fetch
    old_value: 2026-05-12T00:00:00-04:00
    new_value: 2026-05-12T06:00:00-04:00
    rationale: "RSS reachable status 200; 0 in-window items, normal cadence."
  - source_yaml_id: mstic
    runtime_field: last_successful_fetch
    old_value: 2026-05-12T00:00:00-04:00
    new_value: 2026-05-12T06:00:00-04:00
    rationale: "RSS reachable status 200; 0 in-window items; MSTIC not yet fresh on Mini Shai-Hulud 2026-05-12 burst."
  - source_yaml_id: unit42
    runtime_field: last_successful_fetch
    old_value: 2026-05-12T00:00:00-04:00
    new_value: 2026-05-12T06:00:00-04:00
    rationale: "feedburner reachable status 200; 0 in-window items."
  - source_yaml_id: rapid7
    runtime_field: last_successful_fetch
    old_value: 2026-05-12T00:00:00-04:00
    new_value: 2026-05-12T06:00:00-04:00
    rationale: "RSS reachable status 200; 0 in-window items."
  - source_yaml_id: hacker-news
    runtime_field: last_successful_fetch
    old_value: 2026-05-12T00:00:00-04:00
    new_value: 2026-05-12T06:00:00-04:00
    rationale: "Homepage WebFetch surfaced 3 new 2026-05-12-dated items; 1 raw-signaled as FLASH candidate (FLASH-0600-001), 2 DISCARDED per Mode 1."
  - source_yaml_id: sentinelone
    runtime_field: last_successful_fetch
    old_value: 2026-05-12T00:00:00-04:00
    new_value: 2026-05-12T06:00:00-04:00
    rationale: "SentinelLabs RSS reachable; 0 in-window items."
  - source_yaml_id: sophos
    runtime_field: last_successful_fetch
    old_value: 2026-05-12T00:00:00-04:00
    new_value: 2026-05-12T06:00:00-04:00
    rationale: "RSS reachable status 200; 0 in-window items."
  - source_yaml_id: cisa-advisories
    runtime_field: last_successful_fetch
    old_value: 2026-05-12T00:00:00-04:00
    new_value: 2026-05-12T06:00:00-04:00
    rationale: "all.xml reachable status 200; 0 in-window items."
  - source_yaml_id: cisa-kev
    runtime_field: last_successful_fetch
    old_value: 2026-05-12T00:00:00-04:00
    new_value: 2026-05-12T06:00:00-04:00
    rationale: "KEV JSON catalog reachable via WebFetch; zero entries dateAdded >= 2026-05-11."

run_summary:
  in_window_items_evaluated: 10        # 1 BC + 0 SecurityWeek + 0 The Record + 0 Krebs + 0 MSTIC + 0 Unit42 + 0 SANS-ISC (parse error) + 0 Rapid7 + 10 CrowdStrike (all dateless) + 0 SentinelLabs + 0 Sophos + 0 ESET + 4 HN 2026-05-12-dated (Mini Shai-Hulud + Instructure + OpenAI Daybreak + iOS 26.5) + 0 NVD CRITICAL + 3 NVD HIGH = effective evaluated set 8 distinct in-window items
  in_window_items_raw_signaled_flash_candidate: 1   # Mini Shai-Hulud
  in_window_items_raw_signaled_non_flash_grader_queue: 0
  in_window_items_anti_noise_discarded: 0
  in_window_items_mode1_discarded: 7   # Instructure BC + Instructure HN + OpenAI Daybreak + iOS 26.5 + 3 NVD HIGH (ELECOM/AIWU/LifePress)
  flash_triggers_fired: 2              # Trigger 1 + Trigger 4 (both on Mini Shai-Hulud)
  flash_candidates_promoted: 1
  source_health_runtime_changes: 12
  quiet_hours_active: true
  posting_required: false
  expected_disposition_for_flash_candidate: queue_to_flash_queue_for_09_00_catchup_sweep
  red_team_review_required_for_flash_candidate: true

ttl_expires_at: 2026-08-10T06:08:00-04:00
---

# 06:00 EDT FLASH alert sweep (2026-05-12) — ONE FLASH CANDIDATE: Mini Shai-Hulud TeamPCP

## Sentinel summary

06:00 EDT 2026-05-12 FLASH sweep ran against all six FLASH triggers over the 2026-05-12T00:00 → 06:00 EDT 6h window.

**ONE FLASH candidate surfaced.** Companion raw-signal: `raw-2026-05-12-flash-0600-001-teampcp-mini-shai-hulud-npm-pypi-worm.md`.

**Two triggers fired:**
- **Trigger 1 (critical-cve-exploited)** — CVE-2026-45321 CVSS 9.6 + confirmed active exploitation (169-172 npm packages compromised live on registries) + A-grade source naming operational layer (Wiz, Snyk, Unit 42, MSTIC lineage)
- **Trigger 4 (tracked-actor-ttp-change)** — first documented npm worm producing validly-attested malicious packages (SLSA bypass); dual-ecosystem self-propagation npm + PyPI; Session-network dead-drop C2; clearly attributable to TeamPCP (#001 HIGH) per Wiz "high confidence" + StepSecurity originating attribution

**Critical override FAILED** on two of four hard thresholds (CVSS 9.6 < 10.0 floor; no A&D watchlist entity named as target — @squawk aviation ecosystem hit is incidental adjacency, not explicit targeting).

**Quiet-hours rule active** (06:00 EDT is inside 21:00–09:00 quiet-hours window). Per FLASH-POLICY §Quiet Hours, composed FLASH brief queues to `infrastructure/flash-queue.yaml` for 09:00 catchup sweep with "QUEUED FROM OVERNIGHT" prefix; direct Discord posting NOT permitted.

## Topic distinction from 2026-05-11 06:00 FLASH (Checkmarx Jenkins)

The 2026-05-11 06:00 FLASH covered a Checkmarx Jenkins AST Plugin compromise (single Jenkins Marketplace plugin, point-strike, no CVE, no worm capability). Mini Shai-Hulud (this sweep) is a separate burst — distinct victim ecosystem (npm + PyPI vs. Jenkins Marketplace), distinct scale (169-172 packages vs. 1 plugin), distinct capability layer (self-propagating worm with valid attestation bypass vs. credential-theft single-strike), distinct CVE (CVE-2026-45321 vs. none), and distinct originating research (StepSecurity + Wiz + Snyk multi-firm vs. Checkmarx PSIRT self-disclosure). Anti-noise rule "one FLASH per topic per 24h" applies **per topic**, not per actor; these are distinct topics. Detail in FLASH-0600-001 8-dimension comparison table.

## Splunk first-party telemetry

Combined `archimedes` + `defenseclaw_local` index sweep over 6h returns zero non-archimedes-internal events. Same over 24h returns zero non-archimedes-internal events. Targeted IOC keyword sweep across 25 high-priority tokens (15 tracked actor aliases + 10 priority CVEs including this-sweep CVE-2026-45321) over 24h returned 6 hits — all six are `archimedes:operation` sourcetype pipeline self-references. The Mini Shai-Hulud IOCs (6 C2 domains + 1 C2 IP + 3 SHA-256 hashes) specifically tested against both indexes — zero matches.

**Trigger 3 (first-party-IOC-hit) cannot fire on a dormant non-Archimedes stream.** Sixteenth consecutive sweep with this pattern across both indexes.

## Anti-noise observations

- **Mini Shai-Hulud TeamPCP campaign** — resurface conditions ALL THREE TRUE (new IOCs, independent A-grade corroboration, novel post-exploitation TTPs). Distinct from 2026-05-11 06:00 Checkmarx Jenkins per 8-dimension comparison. Raw-signaled at FLASH-candidate severity in FLASH-0600-001.
- **OpenAI Daybreak product announcement** (Hacker News 2026-05-12) — defensive vendor announcement, no threats, no IOCs. DISCARDED per Mode 1.
- **Instructure/ShinyHunters extortion settlement** (BleepingComputer + Hacker News 2026-05-12) — edtech consumer-data extortion, ShinyHunters not in roster, Canvas not in watchlist. DISCARDED per Mode 1.
- **Apple iOS 26.5 RCS encryption** (Hacker News 2026-05-12) — consumer-product news. DISCARDED.

## Source health changes

- `mandiant` failure_count 14 → 15 (sixteenth consecutive feedburner 404; destination page top-5 titles unchanged). Held healthy pending operator alt-endpoint decision.
- `sans-isc` failure_count 0 → 1 (XML parse error `<unknown>:2:0: syntax error` — same class as 2026-05-10 18:00 transient that recovered next sweep). Held healthy pending next-sweep retry.
- Eleven other sources (`bleepingcomputer`, `securityweek`, `krebs`, `mstic`, `unit42`, `rapid7`, `hacker-news`, `sentinelone`, `sophos`, `cisa-advisories`, `cisa-kev`) — `last_successful_fetch` updated to 2026-05-12T06:00:00-04:00; failure_count remains 0 for all.

## Carry-forward state for 12:00 FLASH and 08:00 morning brief

**For 08:00 morning brief grader:**
- Mini Shai-Hulud FLASH candidate is the standout intel — clean Trigger 1 + Trigger 4 dual-pass with A-grade source backing
- Expected digraph: A2 on procedural facts (multi-source A-grade, forensically reproducible IOCs/hashes); B2 on TeamPCP attribution-event (multi-source corroboration, originates StepSecurity)
- Red-team review required (WEP >= very-likely per FLASH-POLICY anti-noise)
- Anti-noise distinction from 2026-05-11 06:00 Checkmarx Jenkins FLASH verified via 8-dimension table

**For 12:00 FLASH sweep:**
- SecurityWeek anticipated to publish Mini Shai-Hulud coverage (homepage and RSS pre-window at 06:00; typical multi-hour lag from breaking news)
- BleepingComputer anticipated for similar coverage
- MSTIC may publish fresh active-attack post (lineage product capability response is via Defender for Cloud SBOM-scan; could publish active-attack post on the 2026-05-12 specific burst)
- Anti-noise from THIS sweep: Mini Shai-Hulud now in 24h-window; if 12:00 FLASH surfaces same topic with new IOCs or novel TTPs, evaluate against resurface conditions; otherwise anti-noise applies

**For actor-profiler:**
- TeamPCP #001 dossier update candidate: NEW capability layer (worm-class self-propagation + SLSA attestation bypass + Session-network exfiltration), NEW aliases per Snyk (DeadCatx3, PCPcat, ShellForce, CipherForce)
- Roster threat-level currently HIGH; supply-chain worm capability progression warrants intra-HIGH gradient observation on next /update-tracking

**For vuln-tracker:**
- CVE-2026-45321 new entry candidate (Mini Shai-Hulud TanStack supply-chain compromise; GHSA-g7cv-rxg3-hmpx)

## KEV deadline carry-forward

- **CVE-2024-1708 ConnectWise ScreenConnect** — dueDate 2026-05-12 = **TODAY EOB** (~T+14h from this sweep)
- **CVE-2026-32202 Microsoft Windows** — dueDate 2026-05-12 = **TODAY EOB** (~T+14h from this sweep)
- **CVE-2026-31431 Linux Kernel** — dueDate 2026-05-15 = T+3d
- All three pre-2026-05-12 KEV-deadlines (PAN-OS 2026-05-09, Ivanti EPMM 2026-05-10, LiteLLM 2026-05-11) have passed without KEV-update reflecting compliance status (standard pattern; KEV does not publish compliance-status changes).

## Extraction notes

- Language: en
- Article types covered this sweep: vendor research blog (Wiz, Snyk, Unit 42 backbone), media relay (Hacker News, BleepingComputer, Hacker News headlines), government catalog (CISA KEV JSON, NVD REST, CISA all.xml), vendor advisory tier (CrowdStrike marketing-pile, MSTIC lineage), Splunk first-party
- Raw IOC extraction invoked for FLASH-0600-001 (Mini Shai-Hulud) — full IOC structured set in companion file's `iocs:` frontmatter block
- Sentinel-level IOC extraction: N/A (sentinel doesn't carry IOCs; companion file holds them)

## IOCs

None at sentinel level. See companion `raw-2026-05-12-flash-0600-001-teampcp-mini-shai-hulud-npm-pypi-worm.md` for full Mini Shai-Hulud IOC set (CVE-2026-45321 + 6 C2 domains + 1 C2 IP + 3 SHA-256 hashes + Session-network recipient ID + PBKDF2 salt + 4 new TeamPCP alias candidates).
