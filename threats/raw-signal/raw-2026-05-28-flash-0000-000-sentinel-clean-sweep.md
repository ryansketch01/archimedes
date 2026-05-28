---
source: archimedes-internal
source_grade: N/A
collected_at: 2026-05-28T00:05:00-04:00
sweep: flash-2026-05-28-0000
candidate_trigger: none_fired
url: null
test: false
sentinel: true
sweep_type: flash-midnight-scheduled
status: complete
triggers_fired: 0
sweep_window:
  start: 2026-05-27T18:00:00-04:00
  end: 2026-05-28T00:05:00-04:00
  duration_h: 6.08
prior_sweep_anchor:
  sweep_id: flash-2026-05-27-1800
  anchor_at: 2026-05-27T18:05:00-04:00
  raw_id: raw-2026-05-27-flash-1800-000-sentinel-clean-sweep.md
  commit_sha: 220e11f
  disposition: zero_triggers_fired
  notes: |
    18:00 evening FLASH was a clean sweep — 0 of 6 triggers fired on a
    2.08h window inside active hours. Sentinel + librarian commit
    220e11f. Seven consecutive clean sentinels across Tuesday +
    Wednesday transition; this 00:00 EDT Thursday midnight sweep
    becomes the eighth.
prior_brief_anchor:
  brief_id: 2026-05-27-afternoon
  shipped_at: 2026-05-27T16:00:00-04:00
  commit_sha: 23be30c
  notes: |
    PM-27 afternoon brief published with three new findings + two
    PM-enrichment amendments — CISA KEV three-add lead
    (CVE-2026-45321 VT-006 state transition, CVE-2026-48027 Nx
    Console VT-009 scaffold, CVE-2026-8398 consumer not corpus-
    tracked), Yamcs CVE-2026-44632 A&D-direct (VT-010 scaffold),
    Ox Security npm Claude AI user-data stealer (unattributed),
    GlassWorm + LACMTA Iran PM enrichments. Splunk first-party
    brief-publish event confirmed via -4h@h Splunk sweep at 18:00.
mode: flash_sweep
invocation: scheduled flash-0000 cycle (Thursday midnight)
match_reason:
  watchlist: []
  actors:
    - "#001 TeamPCP"            # Unit 42 "Out of the Crypt" landscape piece references TGR-CRI-1135 (TeamPCP) ~20 supply-chain attacks + May 2026 Shai-Hulud release. Already corpus-tracked under VT-006 lock + multiple findings; trends synthesis not net-new attribution.
    - "#018 Cl0p"               # Unit 42 piece references Hazy Scorpius (CLOP) Oracle EBS exploitation framing. Potential TTP-novelty signal — held below FLASH threshold; carry-forward to AM-28 grader for absorption evaluation.
  vulnerabilities:
    - VT-006                # CVE-2026-45321 TanStack — KEV-listed Wed 2026-05-27, due 2026-06-10 T+14, anti-noise lock active via PM-27 finding-0007
    - VT-008                # CVE-2026-42897 Exchange — KEV deadline T-1 Fri 2026-05-29, anti-noise lock active
    - VT-009                # CVE-2026-48027 Nx Console — KEV-listed Wed 2026-05-27, due 2026-06-10 T+14, anti-noise lock active via PM-27 finding-0007 + corpus finding-2026-05-20-FLASH-0001
    - VT-010                # CVE-2026-44632 Yamcs — patched at disclosure, anti-noise lock active via PM-27 finding-0009
    - "CVE-2026-48172 LiteSpeed cPanel — KEV deadline T-1 Fri 2026-05-29, anti-noise lock active"
    - "CVE-2026-9082 Drupal — KEV deadline T-0 expired EOB Wed 2026-05-27 (now T+~5h past deadline), anti-noise lock active"
  keywords: []
triage_tags:
  - flash_sentinel
  - flash_midnight_scheduled
  - clean_sweep
  - zero_triggers_fired
  - quiet_hours_post_no_dispatch_would_have_queued_if_triggered
  - kev_t_past_drupal_eob_wed_expired
  - kev_t_1_exchange_friday
  - kev_t_1_litespeed_friday
  - eighth_consecutive_clean_sweep_tuesday_through_thursday_midnight
  - post_pm_brief_overnight_window
  - unit42_extortion_economy_trends_piece_corpus_absorption_candidate_am_28
  - ksecurity_acer_nitrosense_cve_2026_9789_off_scope_consumer
  - investigation_inv-2026-05-26-001_carry_forward_active
iocs_extracted: false
iocs_count: 0
text_word_count: 1850
promoted: false
ttl_expires_at: 2026-08-26T00:05:00-04:00
sources_queried:
  - cisa-kev               # WebFetch known_exploited_vulnerabilities.json — catalogVersion 2026.05.27 UNCHANGED since noon/evening cycle. dateReleased 2026-05-27T17:08:41 UTC (= 13:08 EDT post-publication re-release with same three CVE adds). ZERO net-new KEV adds in 6.08h window since 18:00 FLASH.
  - cisa-advisories        # fetch_feed cisa.gov/cybersecurity-advisories/all.xml — 200 OK, 30 items in feed, 0 in 6.08h window.
  - nvd                    # WebFetch services.nvd.nist.gov/rest/json/cves/2.0 pubStartDate 2026-05-27T22:00 → 2026-05-28T00:00 EDT — 1 CVE published in window: CVE-2026-9789 (Acer NitroSense LPE, CVSS v4.0 8.5 HIGH, CWE-22/269/284/732, consumer software, not corpus-tracked). No CVSS-9.0+ A-grade vendor surface + no active-exploitation + no A&D-prime named. OFF-SCOPE per Mode 1 (consumer hardware utility, no active-exploitation claim).
  - thehackernews          # fetch_feed feedburner — 200 OK; last_modified Thu 28 May 2026 03:19 GMT (= 23:19 EDT IN-window header refresh). 0 items after since-filter on 50-item feed.
  - bleepingcomputer       # fetch_feed — 200 OK; last_modified Thu 28 May 2026 03:52 GMT (= 23:52 EDT IN-window header refresh). 0 in-window items after since-filter on 15-item feed.
  - securityweek           # fetch_feed feedburner — 200 OK; last_modified Wed 27 May 2026 17:32 GMT (= 13:32 EDT pre-window unchanged across the entire evening cycle). 0 in-window items.
  - the-record             # fetch_feed therecord.media/feed — 200 OK; 5 items in feed, 0 in 6.08h window.
  - the-register           # fetch_feed theregister.com/security/headlines.atom — 200 OK; 50 items in feed, 0 in 6.08h window.
  - dark-reading           # fetch_feed darkreading.com/rss.xml — 200 OK; last_modified Thu 28 May 2026 04:01 GMT (= 00:01 EDT IN-window header refresh). 2 in-window items: BOTH future-dated event-calendar entries (Infosecurity Europe 2026-06-02 + Anatomy of a Data Breach 2026-06-18), same RSS placeholders as 00:00/06:00/12:00/18:00 sweeps. DISCARDED per Mode 1 (event-calendar, not threat intel).
  - mandiant               # fetch_feed mandiant.com/resources/blog/rss.xml — 200 OK (SIXTH consecutive recovery); 20 items in feed; 0 in 6.08h window. The cloud.google.com/blog/topics/threat-intelligence/rss/ endpoint returned 404 ("not found") this sweep — confirms the canonicalization recommendation. AM-28 pre-brief should canonicalize mandiant.com endpoint + retire the cloud.google.com endpoint.
  - unit42                 # fetch_feed feedburner — 200 OK; last_modified Wed 27 May 2026 22:56 GMT (= 18:56 EDT IN-window). ONE in-window item: 2026-05-27T22:00:46 UTC (= 18:00:46 EDT) "Out of the Crypt: The Evolving Cyber Extortion Economy" by Matt Brady and Justin Moore. Tags: Bling Libra, Extortion, Frontier AI, Hazy Scorpius, Scattered LAPSUS$ Hunters, ShinyHunters, supply chain, Telegram, TGR-CRI-1135. STRATEGIC/ECONOMIC-TRENDS landscape piece — restates known attribution for TeamPCP (TGR-CRI-1135), Cl0p (Hazy Scorpius), ShinyHunters (Bling Libra); references BlackFile→Redact rebrand (CL-CRI-1116, NOT in roster). NO new attribution, NO net-new TTP publication with IOCs, NO A&D-prime named (targeted sectors: Professional Services / Healthcare / Consumer Services / Manufacturing / Construction). HELD BELOW FLASH THRESHOLD; carry-forward to AM-28 grader for absorption evaluation under existing VT-006 (TeamPCP/Shai-Hulud) + AM-27 finding-0007 (ShinyHunters/Charter) locks.
  - mstic                  # fetch_feed microsoft.com/en-us/security/blog/feed — 200 OK; last_modified Wed 27 May 2026 20:43 GMT (= 16:43 EDT pre-window). 0 items.
  - crowdstrike            # fetch_feed crowdstrike.com/blog/feed/ — 200 OK; last_modified Thu 28 May 2026 00:19 GMT (= 20:19 EDT IN-window header refresh). 10 items, ALL published: null per the established persistent-dateless-marketing pattern documented across 16+ consecutive prior sweeps. Top items: GlassWorm takedown (already absorbed in AM-27 finding-0001 + PM-27 enrichment), Gartner MQ leader announcements, product-feature posts, May 2026 Patch Tuesday analysis (predates sweep window). ALL DISCARDED per Mode 1.
  - checkpoint-research    # fetch_feed research.checkpoint.com/feed — 200 OK; last_modified Tue 26 May 2026 12:13 GMT (= 08:13 EDT 2026-05-26 pre-window unchanged). 0 items.
  - cisco-talos            # fetch_feed blog.talosintelligence.com/rss/ — 200 OK; 15 items in feed, 0 in 6.08h window.
  - sans-isc               # fetch_feed isc.sans.edu/rssfeed.xml — 200 OK; last_modified Thu 28 May 2026 03:59 GMT (= 23:59 EDT IN-window header refresh). 1 in-window item: 2026-05-28T02:00 UTC (= 22:00 EDT) "ISC Stormcast For Thursday, May 28th, 2026" — daily podcast placeholder. DISCARDED per Mode 1 (podcast index, content not in RSS body).
  - sophos                 # fetch_feed news.sophos.com security-operations/feed — 200 OK; last_modified Wed 27 May 2026 23:25 GMT (= 19:25 EDT IN-window header refresh). 0 in-window items in 15-item feed.
  - eset                   # fetch_feed welivesecurity.com/en/rss/feed — 200 OK; 100 items in feed, 0 in 6.08h window.
  - sentinelone            # fetch_feed sentinelone.com/labs/feed — 200 OK; last_modified Wed 27 May 2026 20:30 GMT (= 16:30 EDT pre-window). 0 items.
  - volexity               # fetch_feed volexity.com/blog/feed — PARSE ERROR ("<unknown>:17:68: not well-formed (invalid token)"). Recurring quirk; same as PM-26 18:00 / 00:00 / noon FLASH / 18:00 FLASH + this sweep (SIXTH consecutive observation). Failure count NOT incremented — known-pattern transient parse-error. Defer to AM-28 pre-brief collector for retry-or-MCP-build decision.
  - mandiant-cloud-google  # WebFetch cloud.google.com/blog/topics/threat-intelligence/rss/ — 404 "not found" this sweep. Confirms canonicalization rationale: mandiant.com/resources/blog/rss.xml is the productive endpoint; cloud.google.com endpoint appears to no longer serve RSS at this path. AM-28 pre-brief should canonicalize.
  - krebs                  # fetch_feed krebsonsecurity.com/feed — 200 OK; last_modified Mon 25 May 2026 13:21 GMT (= 09:21 EDT 2026-05-25 pre-window unchanged). 0 items.
  - splunk-archimedes      # mcp__splunk-query targeted 47-IOC sweep on -6h@h. ZERO events returned — no Archimedes self-telemetry in window either (no librarian operations since PM-27 brief publish at 18:00). 66th consecutive dormant non-self sweep increment.
  - splunk-defenseclaw     # included in the -6h@h cross-index sweep; 0 events. 66th consecutive dormant non-self sweep on defenseclaw_local.

splunk_first_party_check:
  query: 'search index=defenseclaw_local OR index=archimedes earliest=-6h@h latest=now ("Hazy Scorpius" OR "Bling Libra" OR "TGR-CRI-1135" OR "CL-CRI-1116" OR BlackFile OR Redact OR "Scattered LAPSUS" OR ShinyHunters OR "Cyber Extortion" OR "Cl0p" OR "TeamPCP" OR "Shai-Hulud" OR UNC1549 OR APT28 OR APT29 OR APT34 OR APT37 OR APT41 OR Sandworm OR "Volt Typhoon" OR "Salt Typhoon" OR Lazarus OR MuddyWater OR "Scattered Spider" OR LockBit OR "Charming Kitten" OR CVE-2026-9082 OR CVE-2026-42897 OR CVE-2026-48172 OR CVE-2026-45321 OR CVE-2026-48027 OR CVE-2026-44632 OR "Oracle EBS" OR "Oracle E-Business" OR Yamcs OR TanStack OR "Nx Console" OR LiteSpeed OR Drupal OR Exchange OR cPanel) | head 50'
  result: ZERO events returned. No Archimedes self-telemetry in -6h@h window (no librarian operations since PM-27 brief publication at 18:00 EDT). ZERO defenseclaw_local hits. ZERO IOC matches on tracked-actor or tracked-vuln strings.
  consecutive_dormant_sweeps_defenseclaw: 66
  iac_ioc_hits_in_defenseclaw_local: 0
  hard_rule_8_framing: |
    Targeted 47-IOC sweep across the carried-forward corpus IOC set
    PLUS the Unit 42 "Out of the Crypt" trends-piece actor names
    (Hazy Scorpius / Bling Libra / TGR-CRI-1135 / CL-CRI-1116 /
    BlackFile / Redact / Scattered LAPSUS / ShinyHunters / Oracle
    EBS / Oracle E-Business) on defenseclaw_local + archimedes in
    -6h@h returned ZERO events. Even Archimedes self-telemetry is
    absent — the only events expected would have been librarian
    operations, but PM-27 ran 16:30-16:35 EDT (pre-window). 66th
    consecutive dormant non-self sweep on defenseclaw_local. Hard
    Rule 8: silence is not disconfirming, not confirming.

filter_evaluation_summary:
  in_window_items_total: 6
  in_window_items_evaluated: 6
  in_window_items_corpus_absorption_carry_forward_to_am_28: 1
  in_window_items_flash_tier: 0
  in_window_items_discarded_off_scope: 5
  notes: |
    Six in-window items across all surveyed surfaces, ONE held for
    AM-28 grader absorption evaluation, FIVE discarded off-scope:

    (1) Unit 42 (Matt Brady + Justin Moore, 18:00:46 EDT, exactly
        46 seconds after the prior 18:00 FLASH sweep window closed):
        "Out of the Crypt: The Evolving Cyber Extortion Economy".
        Strategic landscape piece on the cyber extortion economy
        evolution. Tags: Bling Libra, Extortion, Frontier AI, Hazy
        Scorpius, Scattered LAPSUS$ Hunters, ShinyHunters, supply
        chain, Telegram, TGR-CRI-1135.

        Tracked-actor surface inventory:
          - TGR-CRI-1135 = TeamPCP (roster #001, HIGH). Article
            cites ~20 distinct supply-chain compromise attacks +
            May 2026 Shai-Hulud release. Both elements ALREADY
            corpus-tracked under VT-006 lock + multiple findings
            (finding-2026-05-12-* worm deployment, finding-2026-05-
            14 Mistral repos sale, finding-2026-05-15-FLASH-0001
            source-code release, finding-2026-05-19-0001 antv +
            actions-cool bridge, finding-2026-05-20-FLASH-0001
            GitHub-corp breach, finding-2026-05-27-0007 KEV state-
            transition). NO net-new attribution claim.
          - Hazy Scorpius = Cl0p (roster #018, HIGH). Article
            references Oracle EBS exploitation. Cl0p Oracle EBS
            angle is NOT explicitly covered in current corpus —
            historical Cl0p coverage focuses on MOVEit, GoAnywhere,
            Cleo file-transfer surfaces. Potential TTP-novelty
            signal, but article is a TRENDS SYNTHESIS not a specific
            CVE/IOC/victim publication. No CVE referenced, no IOCs
            published, no specific A&D victim named. HELD BELOW
            FLASH-trigger-4 threshold (categorical: trends piece,
            not "new tooling/targeting/infrastructure CLASS
            DOCUMENTED").
          - Bling Libra = ShinyHunters. ShinyHunters surfaced in
            AM-27 finding-2026-05-27-0007 (Charter 40M-records
            breach, vishing/Salesforce/Entra TTP, April 2026
            attribution). Article restates known TTPs (vishing,
            SaaS targeting, DDoS, media leaks). NO net-new
            attribution.
          - CL-CRI-1116 = BlackFile → "Redact" rebrand. NEITHER
            actor in _roster.yaml — Hard Rule 2 prevents Archimedes-
            side origination. The swatting-employees double-
            extortion tactic is novel framing but the actor is
            not roster-tracked. Carry-forward observation for
            actor-profiler /new-actor consideration ONLY if other
            A-grade sources name the same actor with the same
            tactic.
          - Scattered LAPSUS$ Hunters — alliance referenced as
            disbanded; Bling Libra "distanced themselves". Prior
            corpus coverage in brief 2026-05-18-afternoon + multiple
            _coverage-log entries. NOT in _roster.yaml as a unified
            entity; Scattered Spider IS roster #013 (aliases:
            UNC3944, Octo Tempest, 0ktapus, Scatter Swine, Muddled
            Libra, Starfraud — does NOT include "Scattered LAPSUS$
            Hunters"). NO Archimedes-side crosswalk per Hard Rule 2.

        Disposition: HELD BELOW FLASH threshold on all six prongs
        (see trigger_evaluation block below). CARRY-FORWARD to
        AM-28 pre-brief grader for absorption evaluation as
        supplementary context under existing VT-006 + AM-27
        finding-0007 + Cl0p (no active lock) corpus coverage.
        Recommended absorption framing: "Unit 42 trends synthesis
        — restates TeamPCP/Cl0p/ShinyHunters known activity; novel
        Cl0p Oracle EBS framing requires independent corroboration
        before WEP elevation; BlackFile→Redact rebrand is candidate
        actor-profiler /new-actor evaluation NOT FLASH-tier."

    (2) DarkReading "Infosecurity Europe" event listing (future
        2026-06-02). RSS placeholder, repeated all day. DISCARDED
        per Mode 1 (event-calendar, not threat intel).

    (3) DarkReading "[Virtual Event] Anatomy of a Data Breach"
        (future 2026-06-18). RSS placeholder, repeated all day.
        DISCARDED per Mode 1 (event-calendar, not threat intel).

    (4) SANS ISC "ISC Stormcast For Thursday, May 28th, 2026"
        (22:00 EDT 2026-05-27). Daily podcast index placeholder;
        no content in RSS body. DISCARDED per Mode 1 (podcast
        index, not actionable threat intel).

    (5) NVD CVE-2026-9789 (Acer NitroSense LPE, CVSS v4.0 8.5
        HIGH, CWE-22/269/284/732, published 2026-05-28). Consumer
        hardware utility software, NOT widely deployed in DIB/A&D
        operational environments. No active-exploitation claim.
        Does NOT meet Trigger 1 (no CVSS 9.0+ on v3 + no active
        exploitation), does NOT meet Trigger 6 (consumer utility
        not "widely deployed product" + no active exploitation
        confirmed/imminent). DISCARDED per Mode 1.

    (6) CrowdStrike Patch Tuesday May 2026 analysis. Pre-window
        publication (article dateless; topic refers to May 2026
        Patch Tuesday which was 2026-05-13 — well pre-window).
        Same persistent-dateless-marketing pattern. DISCARDED per
        Mode 1.

    Zero items met FLASH-trigger criteria on any prong.

trigger_evaluation:
  trigger_1_critical_cve_exploited:
    fired: false
    reason: |
      ZERO net-new in-window CVE publications meeting Trigger 1
      thresholds. KEV catalog version 2026.05.27 UNCHANGED across
      the entire 6.08h evening + overnight cycle. No catalog flip
      since Wed 13:08 EDT post-publication re-release (with the
      same three additions from noon: CVE-2026-45321 TanStack,
      CVE-2026-48027 Nx Console, CVE-2026-8398 Daemon Tools Lite
      — all corpus-absorbed in PM-27 finding-2026-05-27-0007).

      NVD published ONE in-window CVE: CVE-2026-9789 Acer
      NitroSense LPE, CVSS v4.0 8.5 HIGH. Consumer hardware utility
      software, NOT corpus-tracked, NO active-exploitation claim,
      assigner UUID-only (not a recognized A-grade vendor PSIRT).
      Fails Trigger 1 on CVSS v3 9.0+ prong AND on active-
      exploitation prong AND on A-grade source prong.

      ZERO in-window CVE publications across A-grade vendor surfaces
      (Mandiant / Unit 42 / MSTIC / CKR / Cisco Talos / SANS ISC /
      CrowdStrike / Sophos / ESET / SentinelOne) describing a
      critical CVE with current active exploitation. Trigger 1
      categorical-fail.

      Recent KEV additions all corpus-tracked under active locks:
      CVE-2026-45321 TanStack (2026-05-27 due 2026-06-10 T+14),
      CVE-2026-48027 Nx Console (2026-05-27 due 2026-06-10 T+14),
      CVE-2026-48172 LiteSpeed (2026-05-26 due Fri T-1),
      CVE-2026-9082 Drupal (2026-05-22 due Wed 2026-05-27 EOB
      — now T+~5h PAST DEADLINE for federal civilian estates;
      operational catch-up window for tracked DIB/CMMC partners
      whose business day is closed),
      CVE-2026-42897 Exchange (2026-05-15 due Fri T-1).
  trigger_2_tracked_actor_attribution:
    fired: false
    reason: |
      ONE in-window publication touches tracked actors but does
      NOT meet "new attribution" prong:

      Unit 42 "Out of the Crypt" (18:00:46 EDT) restates TeamPCP
      (TGR-CRI-1135, roster #001) and Cl0p (Hazy Scorpius, roster
      #018) and ShinyHunters (Bling Libra) attribution. All three
      attribution claims are CORPUS-ESTABLISHED:
        - TeamPCP attribution lineage in VT-006 + multiple findings
          across 2026-05-12 / 14 / 15 / 19 / 20 / 27
        - Cl0p RU-attribution + RaaS-class established in roster
          2026-04-14
        - ShinyHunters attribution + Charter incident framing in
          AM-27 finding-2026-05-27-0007

      Doctrine explicitly excludes "re-reporting prior
      attribution" from Trigger 2. Bling Libra = ShinyHunters,
      Hazy Scorpius = Cl0p, TGR-CRI-1135 = TeamPCP are vendor-
      specific aliases of already-tracked actors, not novel
      attribution chains.

      Mandiant / MSTIC / CKR / Cisco Talos / SentinelOne / Sophos /
      ESET all last-modified pre-window. No new tracked-actor
      attribution publications across A-grade vendor surfaces or
      B-grade media relays in the 6.08h window.

      Trigger 2 categorical-fail on novelty prong.
  trigger_3_first_party_ioc_hit:
    fired: false
    reason: |
      Targeted 47-IOC sweep on defenseclaw_local + archimedes
      -6h@h returned ZERO events. No Archimedes self-telemetry in
      window either — no librarian operations since PM-27 brief
      publication at 18:00 EDT (PM-27 librarian-20260527-160030
      run completed at 16:35 EDT, well pre-window). ZERO
      defenseclaw_local hits. ZERO IOC matches on tracked-actor
      or tracked-vuln strings.

      The sweep included (a) freshly KEV-listed corpus IOCs
      (CVE-2026-45321 TanStack, CVE-2026-48027 Nx Console),
      (b) carried-forward KEV IOCs (CVE-2026-9082 Drupal, now
      T+~5h past deadline; CVE-2026-42897 Exchange T-1;
      CVE-2026-48172 LiteSpeed cPanel T-1), (c) PM-27 Yamcs
      CVE-2026-44632, (d) full roster actor names, (e) Unit 42
      trends-piece actor names (Hazy Scorpius / Bling Libra /
      TGR-CRI-1135 / CL-CRI-1116 / BlackFile / Redact / Scattered
      LAPSUS / ShinyHunters / Oracle EBS / Oracle E-Business).

      66th consecutive dormant non-self sweep on defenseclaw_local.
      Hard Rule 8: silence is not disconfirming, not confirming.
  trigger_4_tracked_actor_ttp_change:
    fired: false
    reason: |
      ONE in-window publication touches tracked-actor TTPs but does
      NOT meet "new TTP DOCUMENTED" prong:

      Unit 42 "Out of the Crypt" references Cl0p (Hazy Scorpius)
      Oracle EBS exploitation. Cl0p's historical mass-exploitation
      pattern targets file-transfer surfaces (MOVEit 2023,
      GoAnywhere 2023, Cleo 2024). The Oracle EBS framing is NOT
      explicitly covered in Archimedes's current Cl0p corpus
      footprint and is POTENTIALLY a new targeting surface.

      However, doctrine Trigger 4 requires "new tooling, new
      targeting, or new infrastructure class DOCUMENTED" — the
      Unit 42 piece is a STRATEGIC LANDSCAPE SYNTHESIS, not a
      specific tooling/targeting/infrastructure publication with
      victim names, CVE references, IOCs, or technical detail.
      The Oracle EBS reference is a trend observation embedded
      in a 2026-trends synthesis, not a "new TTP DOCUMENTED" in
      the doctrinal sense.

      The BlackFile→Redact rebrand + swatting-as-extortion tactic
      is also a TTP-novelty observation but applies to an actor
      (CL-CRI-1116) that is NOT in _roster.yaml — Hard Rule 2
      prevents Archimedes-side actor-roster origination.

      Trigger 4 categorical-fail on "DOCUMENTED" prong (trends
      synthesis ≠ documented TTP publication) AND on attributable-
      to-tracked-actor prong for the BlackFile→Redact case.

      Held for AM-28 grader: the Cl0p Oracle EBS framing warrants
      a follow-up retrieval — does any A-grade vendor have a
      specific Cl0p / Oracle EBS technical publication / CVE
      reference / victim publication? If a second independent
      A-grade source publishes specific Cl0p Oracle EBS activity
      with IOCs or named victims, that becomes a Trigger 4
      candidate. The current Unit 42 trends-piece reference alone
      is below threshold.
  trigger_5_ad_sector_campaign:
    fired: false
    reason: |
      ZERO in-window A&D-sector campaign publications. NO
      watchlist-prime named in any in-window item (Lockheed
      Martin / Boeing / RTX / Northrop Grumman / General Dynamics
      / BAE Systems / L3Harris / Leidos / SAIC / Thales / GE
      Aerospace / Safran all silent).

      Unit 42 "Out of the Crypt" names targeted sectors:
      Professional Services / Healthcare / Consumer Services /
      Manufacturing / Construction. A&D is NOT in the named
      sector list. No multi-victim A&D framing.

      Trigger 5 categorical-fail on A&D-sector prong AND multi-
      victim-A&D prong.
  trigger_6_zero_day_no_patch:
    fired: false
    reason: |
      ZERO in-window zero-day disclosures without patch. KEV
      catalog unchanged. No A-grade vendor surface published a
      pre-patch zero-day in the 6.08h window.

      NVD's lone in-window publication (CVE-2026-9789 Acer
      NitroSense LPE) does not meet Trigger 6 on patch-availability
      (Acer's status not surveyed but the consumer-utility class
      + lack of A-grade source publication + lack of active
      exploitation = categorical fail regardless of patch state).

      Trigger 6 categorical-fail on disclosure-without-patch prong
      AND A-grade-corroboration prong AND exploitation-imminent
      prong.

anti_noise_locks_active:
  - lock_id: cve-2026-9082-drupal-core-sqli-kev-deadline-tracking
    source_anchor: continuous from 2026-05-22 FLASH; rolling brief-tier coverage; finding-2026-05-26-0004 morning absorption
    expires_at: rolling — recurring brief surface
    status: ACTIVE — T+~5h PAST deadline for federal civilian estates (Wed EOB 2026-05-27 expired); operational catch-up window for DIB/CMMC partners whose business day closed before deadline
  - lock_id: cve-2026-42897-exchange-owa-xss-kev-deadline-tracking
    source_anchor: continuous from 2026-05-15 FLASH-0001 lineage
    expires_at: rolling — recurring brief surface
    status: ACTIVE — T-1 deadline Fri 2026-05-29 ~40h from this sweep
  - lock_id: cve-2026-48172-litespeed-cpanel-plugin-kev-deadline-tracking
    source_anchor: PM-26 afternoon brief finding-2026-05-26-0008
    expires_at: rolling — recurring brief surface
    status: ACTIVE — T-1 deadline Fri 2026-05-29 ~40h from this sweep
  - lock_id: cve-2026-45321-tanstack-mini-shai-hulud-kev-listed-vt-006-state-transition
    source_anchor: PM-27 afternoon brief finding-2026-05-27-0007 (KEV-listing state-change)
    expires_at: rolling — recurring brief surface
    status: ACTIVE — T+14 deadline Wed 2026-06-10
  - lock_id: cve-2026-48027-nx-console-kev-listed-finding-2026-05-20-flash-0001-codification
    source_anchor: PM-27 afternoon brief finding-2026-05-27-0007 (KEV-listing of prior corpus surface)
    expires_at: rolling — recurring brief surface
    status: ACTIVE — T+14 deadline Wed 2026-06-10; VT-009 scaffolded
  - lock_id: cve-2026-44632-yamcs-spacecraft-mission-control-rce-patched
    source_anchor: PM-27 afternoon brief finding-2026-05-27-0009 (A&D-direct vendor-coordinated patch disclosure)
    expires_at: rolling — recurring brief surface
    status: ACTIVE — patched 5.12.7 at disclosure; VT-010 scaffolded
  - lock_id: ai-chatbot-cryptojacking-screenconnect-mstic-2026-05-27
    source_anchor: AM-27 finding-2026-05-27-0005 (MSTIC primary)
    expires_at: 2026-05-28T08:00:00-04:00 (~8h from this sweep)
    status: ACTIVE — BC 17:31 EDT 2nd relay layer absorbed in PM-27 sentinel; no further relays this window
  - lock_id: cisa-kev-three-add-2026-05-27-catalog-version-state-change
    source_anchor: PM-27 afternoon brief finding-2026-05-27-0007
    expires_at: rolling — recurring brief surface
    status: ACTIVE — catalog version 2026.05.27 unchanged across entire evening cycle
  - lock_id: lacmta-iran-attribution-investigation-inv-2026-05-26-001
    source_anchor: PM-27 afternoon brief finding-2026-05-27-0004 (Gambit + The Record relays + Ababil-of-Minab alias surface)
    expires_at: 2026-06-09T16:00:00-04:00 (T+13 carry-forward window)
    status: ACTIVE
  - lock_id: glassworm-takedown-roster-005-russian-attribution-pattern
    source_anchor: AM-27 finding-2026-05-27-0001 + PM-27 enrichment via The Register fourth relay (CIS-locale + Russian code comments)
    expires_at: 2026-05-28T16:00:00-04:00 (~16h from this sweep)
    status: ACTIVE — #005 nation field stays `unknown`; CrowdStrike single-source veto unchanged
  - lock_id: shinyhunters-charter-40m-records-vishing-salesforce-entra-april-2026
    source_anchor: AM-27 finding-2026-05-27-0007 (Charter confirms 40M-records breach)
    expires_at: 2026-05-28T08:00:00-04:00 (~8h from this sweep)
    status: ACTIVE — Unit 42 trends-piece "Bling Libra" relay absorbed below as supplementary context for AM-28 grader

hard_rules_compliance:
  rule_2_no_attribution_origination: |
    Unit 42 "Out of the Crypt" introduces vendor-specific aliases
    (Bling Libra = ShinyHunters, Hazy Scorpius = Cl0p, TGR-CRI-
    1135 = TeamPCP). These are restatements of already-tracked
    actor identities under different vendor taxonomies, NOT new
    attribution claims. No Archimedes-side crosswalk performed —
    aliases preserved verbatim as Unit 42 published them.
    BlackFile → Redact rebrand for CL-CRI-1116 is preserved as
    Unit 42's claim; CL-CRI-1116 is NOT in _roster.yaml and
    Archimedes does NOT crosswalk or originate. Scattered LAPSUS$
    Hunters preserved as Unit 42's framing; Archimedes does NOT
    crosswalk to Scattered Spider (#013) per Hard Rule 2.
  rule_3_no_exploitation: |
    No PoC code, no payloads, no exploit guides referenced or
    generated. Unit 42 trends piece references exploitation
    patterns (Oracle EBS targeting, supply-chain compromise via
    malicious code injection, vishing) at a strategic/landscape
    level — no attack-step detail.
  rule_4_passive_only: |
    No active scans. SpiderFoot not invoked. authorized-
    targets.yaml empty. All sources passive RSS / WebFetch /
    KEV / NVD / Splunk over Archimedes's own indices.
  rule_6_quote_limit: |
    No direct quotes used in this sentinel. Sweep summary only
    describes Unit 42 article content; full article retrieval +
    quote-budgeted citation deferred to AM-28 grader if absorbed
    into finding.
  rule_7_credentials: "No credential exposure surfaced this window."
  rule_8_splunk_first_party_priority: |
    Targeted 47-IOC sweep (incl. Unit 42 actor names) on -6h@h =
    ZERO events. ZERO defenseclaw_local hits; ZERO IOC matches.
    66th consecutive dormant non-self sweep on defenseclaw_local.
    Even Archimedes self-telemetry absent (no librarian operations
    since 18:00 EDT). Hard Rule 8: silence is not disconfirming.

source_health_changes:
  - source_yaml_id: mandiant
    observation: |
      mandiant.com/resources/blog/rss.xml endpoint returned 200 OK
      with 20 items in feed (SIXTH consecutive recovery observation
      across PM-26 12:00 / 18:00 / 00:00 / noon FLASH / 18:00 FLASH
      + this sweep). The cloud.google.com/blog/topics/threat-
      intelligence/rss/ endpoint returned 404 ("not found") on this
      sweep — direct retrieval confirms the canonicalization
      recommendation. AM-28 pre-brief collector should canonicalize
      mandiant.com/resources/blog/rss.xml as the productive
      Mandiant endpoint in source-grades.yaml + retire the
      cloud.google.com/blog/topics/threat-intelligence/rss/
      endpoint (or update the path if cloud.google.com hosts the
      content at a different URL).
    runtime_change_applied: no_change_endpoint_canonicalization_recommendation_carry_forward_to_am_pre_brief_with_404_evidence
  - source_yaml_id: volexity
    observation: |
      volexity.com/blog/feed/ returned parse error
      "<unknown>:17:68: not well-formed (invalid token)" — SIXTH
      consecutive observation. Failure count NOT incremented
      because this is a known-pattern transient parse-error issue.
      Defer to AM-28 pre-brief collector for retry-or-MCP-build
      decision.
    runtime_change_applied: no_change_known_pattern_transient_parse_error_carry_forward
  - source_yaml_id: crowdstrike
    observation: |
      crowdstrike.com/blog/feed/ returned 200 OK + 10 items, ALL
      published: null per the established persistent-dateless-
      marketing pattern documented across 16+ consecutive prior
      sweeps in source-health.yaml. Pattern unchanged.
    runtime_change_applied: no_change_pattern_persistent
  - source_yaml_id: unit42
    observation: |
      feeds.feedburner.com/Unit42 returned 200 OK + 15 items;
      last_modified 2026-05-27T22:56:47 UTC (= 18:56 EDT, IN-window
      refresh). ONE in-window publication: "Out of the Crypt: The
      Evolving Cyber Extortion Economy" at 2026-05-27T22:00:46 UTC
      (= 18:00:46 EDT, exactly 46 seconds after the 18:00 FLASH
      window closed). Unit 42 endpoint healthy.
    runtime_change_applied: no_change_endpoint_healthy_in_window_publication_held_below_flash_threshold
  - source_yaml_id: reliaquest
    observation: NOT re-queried this sweep — narrowed scheduled-FLASH scope. Defer to AM-28 pre-brief collector.
    runtime_change_applied: no_change_retry_deferred_to_am_pre_brief
  - source_yaml_id: aikido
    observation: NOT re-queried this sweep — narrowed scheduled-FLASH scope. Defer to AM-28 pre-brief collector.
    runtime_change_applied: no_change_retry_deferred_to_am_pre_brief

flash_dispatch_disposition:
  candidates_total: 0
  candidates_per_trigger:
    trigger_1_critical_cve_exploited: 0
    trigger_2_tracked_actor_attribution: 0
    trigger_3_first_party_ioc_hit: 0
    trigger_4_tracked_actor_ttp_change: 0
    trigger_5_ad_sector_campaign: 0
    trigger_6_zero_day_no_patch: 0
  near_misses_documented: 1
  near_miss_detail: |
    Unit 42 "Out of the Crypt" 18:00:46 EDT is the closest in-window
    item to a FLASH-trigger fire. Documented near-miss on Trigger
    2 (touches three tracked actors but restates known attribution)
    and Trigger 4 (Cl0p Oracle EBS framing is potentially new TTP
    but published in a trends-synthesis context, not as a documented
    tooling/targeting publication). Held BELOW threshold;
    CARRY-FORWARD to AM-28 grader for absorption as supplementary
    context. If a second independent A-grade source publishes
    specific Cl0p Oracle EBS technical content with IOCs/victims/
    CVE-references, that secondary publication would meet Trigger 4
    novelty + DOCUMENTED prongs and could fire a FLASH at that time.
  quiet_hours_status: outside_active_hours_00_05_edt_quiet_hours_21_to_09
  critical_override_evaluated: false # No CVSS 10.0 + active exploitation + tracked actor + A&D watchlist hit simultaneously in window
  discord_post_required: false       # Zero triggers fired
  invocation_disposition: scheduled_midnight_flash_clean_sweep_no_discord_post_no_queue_required_unit42_trends_piece_carry_forward_to_am_28_grader

notes:
  - "ZERO FLASH-trigger fires this sweep — 0 of 6 triggers fired. Clean sweep. 6.08h window 2026-05-27T18:00 → 2026-05-28T00:05 EDT spans Wed evening into Thu midnight. 00:05 EDT is OUTSIDE active hours (09:00 → 21:00) — would have queued to flash-queue.yaml (not posted directly) if any trigger had fired."
  - "Six in-window items across all surveyed surfaces. ONE held for AM-28 grader absorption: Unit 42 'Out of the Crypt: The Evolving Cyber Extortion Economy' (18:00:46 EDT, Matt Brady + Justin Moore) — strategic landscape piece on the cyber extortion economy evolution. Tags: Bling Libra (ShinyHunters), Extortion, Frontier AI, Hazy Scorpius (Cl0p), Scattered LAPSUS$ Hunters, ShinyHunters, supply chain, Telegram, TGR-CRI-1135 (TeamPCP). Restates known attribution for three tracked actors (TeamPCP #001, Cl0p #018, plus AM-27 ShinyHunters); introduces Cl0p Oracle EBS framing as potential TTP-novelty signal but at a trends-synthesis level — held below Trigger 4 'DOCUMENTED' threshold. BlackFile → Redact rebrand for CL-CRI-1116 (NOT in roster) is candidate for actor-profiler /new-actor evaluation but NOT FLASH-tier. FIVE discarded off-scope (DarkReading event-calendar x2, SANS ISC daily podcast index, NVD CVE-2026-9789 Acer NitroSense consumer LPE 8.5 v4.0, CrowdStrike Patch Tuesday dateless retrospective)."
  - "KEV catalog version 2026.05.27 UNCHANGED across the entire 6.08h window. ZERO net-new KEV adds since Wed 13:08 EDT post-publication re-release. CVE-2026-9082 Drupal SQLi NOW T+~5h PAST DEADLINE (Wed EOB 2026-05-27 expired) for federal civilian estates; operational catch-up window for DIB/CMMC partners. CVE-2026-42897 Exchange + CVE-2026-48172 LiteSpeed cPanel both T-1 Fri 2026-05-29 (~40h from this sweep). CVE-2026-45321 TanStack + CVE-2026-48027 Nx Console NEW Wed 2026-05-27 T+14 Wed 2026-06-10. CVE-2026-44632 Yamcs patched at disclosure."
  - "Splunk first-party: targeted 47-IOC sweep on defenseclaw_local + archimedes -6h@h returned ZERO events. No Archimedes self-telemetry in window either (no librarian operations since PM-27 publication at 18:00 EDT; PM-27 librarian-20260527-160030 run completed at 16:35 EDT pre-window). ZERO defenseclaw_local hits; ZERO IOC matches on tracked-actor or tracked-vuln strings. 66th consecutive dormant non-self sweep on defenseclaw_local. Hard Rule 8: silence is not disconfirming, not confirming."
  - "Source health: mandiant.com/resources/blog/rss.xml = SIXTH consecutive recovery (200 OK + 20 items, 0 in window). cloud.google.com/blog/topics/threat-intelligence/rss/ endpoint returned 404 — confirms canonicalization recommendation (AM-28 pre-brief collector should canonicalize mandiant.com as productive endpoint + retire/relocate cloud.google.com path). Volexity recurring parse-error SIXTH consecutive observation (defer to AM-28). CrowdStrike persistent-dateless-marketing pattern continues (10 items, all dateless, 16+ consecutive sweeps). Unit 42 healthy + in-window publication. ReliaQuest + Aikido NOT re-queried this sweep (narrowed scope; defer to AM-28 pre-brief collector)."
  - "Hard Rules compliance: Rule 2 — no attribution origination (Unit 42 alias surface preserved verbatim, no Archimedes-side crosswalk for TGR-CRI-1135/Hazy Scorpius/Bling Libra/CL-CRI-1116/Scattered LAPSUS$); Rule 3 — no PoC content (Unit 42 trends piece references exploitation patterns at strategic level, no attack-step detail); Rule 4 — passive only; Rule 6 — no direct quotes; Rule 7 — no credentials; Rule 8 — defenseclaw_local 66th consecutive dormant non-self sweep."
  - "Quiet-hours posture: 00:05 EDT is OUTSIDE active hours (09:00-21:00). FLASH dispatch would have QUEUED to flash-queue.yaml (NOT posted directly to #flash-alerts) if any trigger had fired. Zero triggers fired = no queue entry needed. Critical-override conditions (CVSS 10.0 + confirmed active exploitation + tracked actor + A&D watchlist hit, all four simultaneously) NOT met on any in-window item. CVE-2026-48172 LiteSpeed cPanel REMAINS the only carry-forward CVSS 10.0 + active-exploitation surface, but no tracked actor + no A&D-watchlist prime named, so fails 2 of 4 override prongs (same posture as all sweeps today)."
  - "Carry-forward to AM-28 pre-brief: (1) Unit 42 'Out of the Crypt' for grader absorption evaluation as supplementary context to existing VT-006 (TeamPCP) + Cl0p (#018, no active lock — new TTP-trend signal) + AM-27 finding-0007 (ShinyHunters/Charter) corpus; (2) Mandiant endpoint canonicalization with 404 evidence on cloud.google.com path; (3) Volexity retry-or-MCP-build decision (6 consecutive parse-errors); (4) ReliaQuest + Aikido retry eligibility; (5) BlackFile → Redact (CL-CRI-1116) candidate for actor-profiler /new-actor evaluation IF future A-grade sources name the same actor with the same swatting tactic."
  - "Streak: EIGHTH consecutive clean sentinel sweep across Tuesday + Wednesday + Thursday-midnight transition (Tuesday 06:00 / 12:00 / 18:00 + Wednesday 00:00 / 06:00 / 12:00 / 18:00 + Thursday 00:00 = 8 sentinels, zero FLASH dispatches). Overnight Wed→Thu transition cadence is consistent with established pattern: A-grade vendor wave (Mandiant / Unit 42 / MSTIC / CKR / Cisco Talos / Sophos / ESET / SentinelOne) mostly silent post-publication-horizon — Unit 42 18:00:46 EDT trends piece is the lone in-window A-grade publication and held below FLASH threshold; B-grade media silent (THN / BC / SW / The Record / DarkReading / The Register / Krebs). 06:00 EDT Thursday dawn sweep is the next FLASH evaluation window before AM-28 pre-brief collection at 07:30 EDT."
  - "Disposition: NO Discord post (zero FLASH triggers fired). NO queue entry needed (zero triggers fired). Sentinel raw-signal written to threats/raw-signal/raw-2026-05-28-flash-0000-000-sentinel-clean-sweep.md for librarian commit + Splunk flash_sweep_clean event."
  - "TLP:CLEAR."
---

# 00:00 EDT Thursday FLASH sentinel — CLEAN SWEEP (scheduled midnight cycle)

This sentinel documents the 2026-05-28 00:00 EDT scheduled midnight
FLASH collection sweep, the first FLASH phase of Thursday's daily
cadence. Window: 2026-05-27T18:00 to 2026-05-28T00:05 EDT (6.08h,
OUTSIDE active hours 09:00 to 21:00, post-PM-27-brief overnight
window). **Zero FLASH-trigger fires. 0 of 6 triggers fired.**

## Sweep outcome

**ZERO FLASH candidates** across all six triggers. Of 22 A/B-grade
publication surfaces queried (CISA KEV / CISA all-advisories / NVD +
Mandiant via two endpoints + Unit 42 / MSTIC / CKR / Cisco Talos /
CrowdStrike / SANS ISC / Sophos / ESET / SentinelOne + THN / BC /
SecurityWeek / TheRecord / TheRegister / DarkReading / Krebs +
Splunk first-party + Volexity attempted), only four surfaces returned
in-window items totaling six:

- **Unit 42** (Matt Brady + Justin Moore, 18:00:46 EDT — exactly 46
  seconds after the 18:00 FLASH window closed): "Out of the Crypt:
  The Evolving Cyber Extortion Economy" — strategic landscape piece
  on the cyber extortion economy evolution. Tracked-actor surface:
  TGR-CRI-1135 = TeamPCP (roster #001, restated), Hazy Scorpius =
  Cl0p (roster #018, restated + Oracle EBS framing), Bling Libra =
  ShinyHunters (AM-27 finding-0007 actor, restated). New actor
  surface: CL-CRI-1116 = BlackFile → "Redact" rebrand (NOT in
  roster). **Held below FLASH threshold; carry-forward to AM-28
  grader.**
- **DarkReading** (two future-dated event-calendar entries, same RSS
  placeholders as 00:00 / 06:00 / 12:00 / 18:00 sweeps). DISCARDED.
- **SANS ISC** (22:00 EDT 2026-05-27): "ISC Stormcast For Thursday,
  May 28th, 2026" — daily podcast index placeholder; no content in
  RSS body. DISCARDED.
- **NVD** (lone in-window publication): CVE-2026-9789 Acer NitroSense
  LPE, CVSS v4.0 8.5 HIGH, consumer hardware utility. No active
  exploitation, no A-grade vendor publication, not corpus-tracked.
  DISCARDED.
- **CrowdStrike**: Patch Tuesday May 2026 retrospective + nine other
  dateless marketing items. DISCARDED per persistent-dateless pattern.

This is the **eighth consecutive clean sentinel sweep** across the
Tuesday + Wednesday + Thursday-midnight transition (Tuesday 06:00 /
12:00 / 18:00 + Wednesday 00:00 / 06:00 / 12:00 / 18:00 + Thursday
00:00 = 8 sentinels, zero FLASH dispatches). Overnight cadence is
consistent with the established pattern: A-grade vendor wave mostly
silent post-publication-horizon; Unit 42 18:00:46 EDT trends piece is
the lone in-window A-grade publication and held below FLASH threshold
on every prong.

## In-window items — disposition table

| Item | Source | Time (EDT) | Disposition |
|---|---|---|---|
| Out of the Crypt: Cyber Extortion Economy | Unit 42 (Brady + Moore) | 18:00:46 | CARRY-FORWARD AM-28 grader — strategic landscape piece restates TeamPCP/Cl0p/ShinyHunters attribution; Cl0p Oracle EBS framing potential TTP-novelty signal below DOCUMENTED threshold |
| CVE-2026-9789 Acer NitroSense LPE | NVD | 2026-05-28 (published) | DISCARDED — consumer hardware utility, CVSS v4.0 8.5, no active exploitation, no A-grade vendor publication |
| ISC Stormcast May 28th, 2026 | SANS ISC | 22:00 (Wed) | DISCARDED — daily podcast index placeholder, no content in RSS body |
| Infosecurity Europe event listing | DarkReading | future 2026-06-02 | DISCARDED (event-calendar, repeated all day, same as four prior sweeps) |
| Anatomy of a Data Breach virtual event | DarkReading | future 2026-06-18 | DISCARDED (event-calendar, repeated all day, same as four prior sweeps) |
| Patch Tuesday May 2026 analysis | CrowdStrike | dateless | DISCARDED — dateless retrospective per persistent-marketing pattern (May Patch Tuesday was 2026-05-13, well pre-window) |

## Surfaces queried — table

| Source | Class | Status | Last_modified | In-window items |
|---|---|---|---|---|
| CISA KEV catalog | A1 | unchanged | catalogVersion 2026.05.27, dateReleased Wed 13:08 EDT post-publication re-release | 0 net-new since Wed noon |
| CISA all-advisories | A1 | 200 | (30 items in feed) | 0 |
| NVD | A1 | 200 | API | 1 (CVE-2026-9789 Acer NitroSense LPE DISCARDED off-scope consumer) |
| The Hacker News | B | 200 | 23:19 EDT (header refresh) | 0 |
| BleepingComputer | B | 200 | 23:52 EDT (header refresh) | 0 |
| SecurityWeek | B | 200 | Wed 13:32 EDT pre-window unchanged | 0 |
| The Record | A | 200 | (5 items in feed) | 0 |
| The Register | B | 200 | (50 items in feed) | 0 |
| Dark Reading | B | 200 | 00:01 EDT (header refresh) | 2 (both event-calendar DISCARDED) |
| Mandiant (mandiant.com path) | A | 200 | (20 items in feed; SIXTH consecutive recovery) | 0 |
| Mandiant (cloud.google.com path) | A | 404 | not-found this sweep | not-evaluated; confirms canonicalization to mandiant.com path |
| Unit 42 | A | 200 | 18:56 EDT (header refresh, IN-window) | 1 ("Out of the Crypt" CARRY-FORWARD to AM-28 grader) |
| MSTIC | A | 200 | Wed 16:43 EDT pre-window | 0 |
| CrowdStrike | A (degraded) | 200 | 20:19 EDT (header refresh) | 10 items dateless persistent-marketing pattern; ALL discarded |
| Check Point Research | A | 200 | 2026-05-26 08:13 EDT pre-window unchanged | 0 |
| Cisco Talos | A | 200 | (15 items in feed) | 0 |
| SANS ISC | B | 200 | 23:59 EDT (header refresh) | 1 (Stormcast podcast index DISCARDED) |
| Sophos | A | 200 | 19:25 EDT (header refresh) | 0 in 15-item feed |
| ESET / WeLiveSecurity | A | 200 | (100 items in feed) | 0 |
| SentinelOne / SentinelLabs | A | 200 | 16:30 EDT pre-window | 0 |
| Volexity | A | parse-error | recurring quirk (6th consecutive observation) | unable to evaluate |
| Krebs on Security | B | 200 | 2026-05-25 09:21 EDT pre-window | 0 |
| Splunk defenseclaw_local | A1 (first-party) | healthy | -6h@h | 0 IOC hits (66th consecutive dormant non-self sweep) |
| Splunk archimedes | (self-telemetry) | healthy | -6h@h | 0 events (no librarian operations in -6h since PM-27 brief publication at 18:00) |

## FLASH-trigger evaluation

| Trigger | Result | Reason |
|---|---|---|
| 1: Critical CVE exploited | FAIL | Zero net-new in-window CVE publications meeting threshold; KEV catalog unchanged; NVD's lone in-window CVE-2026-9789 Acer NitroSense LPE is consumer software, CVSS v4.0 8.5 (not v3 9.0+), no active exploitation, no A-grade vendor publication |
| 2: New tracked-actor attribution | FAIL | Unit 42 piece restates TeamPCP/Cl0p/ShinyHunters attribution under vendor-specific aliases (TGR-CRI-1135 / Hazy Scorpius / Bling Libra); doctrine explicitly excludes "re-reporting prior attribution"; no new tracked-actor attribution publications across A-grade vendor surfaces |
| 3: First-party Splunk IOC hit | FAIL | 47-IOC sweep -6h@h returned 0 events; no Archimedes self-telemetry in window either; ZERO defenseclaw_local hits; 66th consecutive dormant non-self sweep |
| 4: Tracked-actor TTP change | FAIL | Unit 42 Cl0p Oracle EBS framing is potentially new TTP for #018 but published as strategic-landscape-synthesis embed, not as DOCUMENTED tooling/targeting publication with IOCs/victims/CVE-references; trends-piece reference alone is below threshold; BlackFile→Redact (CL-CRI-1116) NOT in roster |
| 5: A&D-sector campaign | FAIL | Zero in-window publications naming any watchlist A&D prime; Unit 42 names targeted sectors Professional Services / Healthcare / Consumer Services / Manufacturing / Construction (A&D NOT in named list); no multi-victim A&D framing |
| 6: Zero-day without patch | FAIL | Zero in-window zero-day disclosures without patch; KEV catalog unchanged; NVD's lone in-window CVE-2026-9789 fails on A-grade-source + active-exploitation prongs regardless of patch state |

## Splunk first-party check

Primary query (47 IOCs including Unit 42 trends-piece actor names,
-6h@h):
```
search index=defenseclaw_local OR index=archimedes earliest=-6h@h latest=now
  ("Hazy Scorpius" OR "Bling Libra" OR "TGR-CRI-1135" OR "CL-CRI-1116" OR
   BlackFile OR Redact OR "Scattered LAPSUS" OR ShinyHunters OR
   "Cyber Extortion" OR "Cl0p" OR "TeamPCP" OR "Shai-Hulud" OR
   UNC1549 OR APT28 OR APT29 OR APT34 OR APT37 OR APT41 OR Sandworm OR
   "Volt Typhoon" OR "Salt Typhoon" OR Lazarus OR MuddyWater OR
   "Scattered Spider" OR LockBit OR "Charming Kitten" OR
   CVE-2026-9082 OR CVE-2026-42897 OR CVE-2026-48172 OR
   CVE-2026-45321 OR CVE-2026-48027 OR CVE-2026-44632 OR
   "Oracle EBS" OR "Oracle E-Business" OR Yamcs OR TanStack OR
   "Nx Console" OR LiteSpeed OR Drupal OR Exchange OR cPanel)
  | head 50
```

**Result: 0 events.** No Archimedes self-telemetry in -6h@h window
either — no librarian operations since PM-27 brief publication at
18:00 EDT (PM-27 librarian-20260527-160030 run completed at 16:35
EDT, well pre-window). ZERO defenseclaw_local hits. ZERO IOC matches
on tracked-actor or tracked-vuln strings.

**66th consecutive dormant non-self sweep on defenseclaw_local.**
Hard Rule 8: silence is not disconfirming.

## Anti-noise locks honored

Eleven anti-noise locks at this sweep — all honored. Zero in-window
items absorbed under active locks; the Unit 42 trends piece is HELD
FOR CARRY-FORWARD to AM-28 grader rather than absorbed at FLASH-tier
(decision: AM-28 grader evaluates absorption as supplementary context
to VT-006 + AM-27 finding-0007 + #018 Cl0p baseline; FLASH-tier
absorption would over-credit a trends-synthesis piece as fresh
operational intel).

1. **CVE-2026-9082 Drupal KEV** — rolling, T+~5h PAST deadline (Wed
   EOB 2026-05-27 expired); operational catch-up window for DIB/CMMC
   partners whose business day closed before deadline
2. **CVE-2026-42897 Exchange KEV** — rolling, T-1 deadline Fri ~40h
3. **CVE-2026-48172 LiteSpeed cPanel KEV** — rolling, T-1 deadline Fri
   ~40h
4. **CVE-2026-45321 TanStack KEV** — rolling, T+14 deadline 2026-06-10
   (VT-006 state-transition)
5. **CVE-2026-48027 Nx Console KEV** — rolling, T+14 deadline
   2026-06-10 (VT-009 scaffolded)
6. **CVE-2026-44632 Yamcs spacecraft mission-control RCE** — rolling
   (VT-010 scaffolded; patched at disclosure)
7. **MSTIC cryptojacking ScreenConnect AI-chatbot SEO poisoning** —
   ACTIVE through 2026-05-28 08:00 EDT (~8h from this sweep)
8. **CISA KEV three-add 2026-05-27 catalog state-change** — rolling
9. **LACMTA Iran attribution investigation inv-2026-05-26-001** —
   ACTIVE through 2026-06-09 (T+13 carry-forward window)
10. **GlassWorm takedown roster #005 Russian-pattern attribution** —
    ACTIVE through 2026-05-28 16:00 EDT (~16h from this sweep)
11. **ShinyHunters Charter 40M-records vishing Salesforce Entra
    April 2026** — ACTIVE through 2026-05-28 08:00 EDT (~8h from this
    sweep). Unit 42 "Bling Libra" relay flagged as supplementary
    context for AM-28 grader.

## Carry-forward to AM-28 pre-brief

1. **Unit 42 "Out of the Crypt: The Evolving Cyber Extortion Economy"**
   (Matt Brady + Justin Moore, 18:00:46 EDT) — held for AM-28 grader
   absorption evaluation as supplementary context. Recommended
   framing: "Unit 42 strategic synthesis restates TeamPCP/Cl0p/
   ShinyHunters attribution under vendor-specific aliases (TGR-CRI-
   1135 / Hazy Scorpius / Bling Libra). Novel observations: (a) Cl0p
   Oracle EBS exploitation framing — potential TTP-novelty signal,
   requires independent corroboration before WEP elevation; (b)
   BlackFile → Redact rebrand for CL-CRI-1116 with swatting double-
   extortion tactic — candidate for actor-profiler /new-actor
   evaluation but NOT FLASH-tier; (c) Scattered LAPSUS$ Hunters
   alliance disbanded with Bling Libra distancing — corpus alignment
   with prior 2026-05-18-afternoon coverage."
2. **Mandiant endpoint canonicalization** — AM-28 collector should
   canonicalize `mandiant.com/resources/blog/rss.xml` as productive
   endpoint in `source-grades.yaml`. The `cloud.google.com/blog/topics/
   threat-intelligence/rss/` endpoint returned 404 on direct
   retrieval this sweep, confirming the path is no longer serving
   RSS (or has been relocated). Either retire the cloud.google.com
   entry or update the path. Five consecutive sentinel sweeps now
   show the mandiant.com path as the productive surface.
3. **Volexity retry-or-MCP-build decision** — SIXTH consecutive
   parse-error observation. Worth investigating whether the feed
   schema has changed or whether a custom MCP would be productive.
4. **ReliaQuest + Aikido** — NOT re-queried this evening cycle;
   retry eligibility check.
5. **BlackFile → Redact (CL-CRI-1116)** — candidate for
   actor-profiler `/new-actor` evaluation IF future A-grade sources
   name the same actor with the same swatting-as-extortion tactic.
   Not roster-eligible from a single Unit 42 trends-piece reference.

## Carry-forward KEV deadlines

- **CVE-2026-9082 Drupal SQLi**: **T+~5h PAST DEADLINE** for federal
  civilian estates (Wed 2026-05-27 EOB expired). Operationally past
  for many DIB/CMMC partner-flow estates whose business day closed.
  Anti-noise lock active continuous from 2026-05-22 FLASH lineage
  through morning brief absorption. AM-28 morning brief should track
  post-deadline exploitation activity OR compliance-status changes.
- **CVE-2026-42897 Exchange OWA XSS**: T-1 Fri 2026-05-29 (~40h
  from this sweep).
- **CVE-2026-48172 LiteSpeed cPanel**: T-1 Fri 2026-05-29 (~40h
  from this sweep). CVSS 10.0 anchor.
- **CVE-2026-45321 TanStack (Mini Shai-Hulud)**: T+14 Wed 2026-06-10.
- **CVE-2026-48027 Nx Console**: T+14 Wed 2026-06-10.

If 06:00 EDT Thursday dawn sweep surfaces post-deadline exploitation
activity on Drupal or compliance-status changes on Exchange /
LiteSpeed / TanStack / Nx Console, those would be AM-28 morning-brief
absorption material NOT fresh FLASH (anti-noise locks active rolling
brief-tier coverage).

## Quiet-hours posture

00:05 EDT is **OUTSIDE** active hours (09:00 to 21:00 EDT). FLASH
dispatch would have **QUEUED to `flash-queue.yaml`** (not posted
directly to `#flash-alerts`) if any trigger had fired. Zero triggers
fired = no queue entry needed.

Critical-override conditions (CVSS 10.0 + confirmed active
exploitation + tracked actor + A&D watchlist hit, all four
simultaneously) NOT met on any in-window item — zero in-window CVE
publications, no novel attribution publications, no A&D-watchlist-
prime named. CVE-2026-48172 LiteSpeed cPanel REMAINS the only
carry-forward CVSS 10.0 + active-exploitation surface, but no tracked
actor + no A&D-watchlist prime named, so fails 2 of 4 override prongs
(same posture as all sweeps today).

## Source health changes

- **mandiant** — `mandiant.com/resources/blog/rss.xml` returned 200
  OK with 20 items in feed (**SIXTH consecutive recovery**). The
  `cloud.google.com/blog/topics/threat-intelligence/rss/` endpoint
  returned **404 "not found"** on direct WebFetch retrieval this
  sweep — confirms the canonicalization recommendation. AM-28
  pre-brief collector should canonicalize `mandiant.com` as the
  productive Mandiant endpoint in `source-grades.yaml` and either
  retire or update the cloud.google.com path. NO runtime field
  change applied this sweep — operator-set `notes:` preservation
  rule honored; recommendation is for AM-28 pre-brief collector to
  enact.

- **volexity** — `volexity.com/blog/feed/` returned parse error
  `<unknown>:17:68: not well-formed (invalid token)`, **SIXTH
  consecutive observation** (PM-26 18:00 / 00:00 / noon FLASH /
  18:00 FLASH / this sweep + one earlier observation). Failure count
  NOT incremented because this is a known-pattern transient
  parse-error. Defer to AM-28 pre-brief collector for retry-or-MCP-
  build decision.

- **crowdstrike** — `crowdstrike.com/blog/feed/` returned 200 OK +
  10 items, ALL `published: null` per the established persistent-
  dateless-marketing pattern documented across 16+ consecutive prior
  sweeps in source-health.yaml. Pattern unchanged. ZERO threat-intel
  content this sweep.

- **unit42** — `feeds.feedburner.com/Unit42` returned 200 OK + 15
  items; last_modified 2026-05-27T22:56 UTC (= 18:56 EDT IN-window
  refresh). ONE in-window publication held below FLASH threshold
  (see carry-forward to AM-28 grader). Endpoint healthy.

- **reliaquest** — NOT re-queried this sweep (narrowed
  scheduled-FLASH scope). Defer to AM-28 pre-brief collector.

- **aikido** — NOT re-queried this sweep (narrowed scheduled-FLASH
  scope). Defer to AM-28 pre-brief collector.

## Hard Rules compliance

- **Rule 2**: Unit 42 introduces vendor-specific aliases (Bling Libra
  = ShinyHunters, Hazy Scorpius = Cl0p, TGR-CRI-1135 = TeamPCP).
  These are vendor-taxonomy restatements of already-tracked actor
  identities, NOT new attribution claims. No Archimedes-side
  crosswalk performed — aliases preserved verbatim as Unit 42
  published them. BlackFile → Redact rebrand for CL-CRI-1116
  preserved as Unit 42's claim; CL-CRI-1116 is NOT in `_roster.yaml`
  and Archimedes does NOT crosswalk or originate. Scattered LAPSUS$
  Hunters preserved as Unit 42's framing; Archimedes does NOT
  crosswalk to Scattered Spider (#013).
- **Rule 3**: no PoC code, no payloads, no exploit guides referenced
  or generated. Unit 42 trends piece references exploitation patterns
  (Oracle EBS targeting, supply-chain compromise via malicious code
  injection, vishing) at a strategic-landscape level — no attack-step
  detail.
- **Rule 4**: passive only; SpiderFoot not invoked;
  `authorized-targets.yaml` empty.
- **Rule 6**: no direct quotes used in this sentinel. Full article
  retrieval + quote-budgeted citation deferred to AM-28 grader if
  absorbed into finding.
- **Rule 7**: no credentials surfaced.
- **Rule 8**: defenseclaw_local 66th consecutive dormant non-self
  sweep; targeted 47-IOC sweep ZERO events (no Archimedes self-
  telemetry either).

## Disposition

- **No Discord post** — zero FLASH triggers fired (quiet-hours
  posture would have queued to `flash-queue.yaml` had any trigger
  fired, not posted directly).
- **No queue entry** — zero triggers fired.
- **Sentinel raw-signal written** for librarian commit + Splunk
  `flash_sweep_clean` event.
- **All eleven anti-noise locks honored** — zero in-window items
  absorbed under any active lock; Unit 42 trends piece held for
  AM-28 grader absorption-decision rather than FLASH-tier absorption.
- **AM-28 pre-brief collector carry-forwards**:
  - Unit 42 "Out of the Crypt" trends piece (supplementary context
    for VT-006 / Cl0p baseline / AM-27 finding-0007)
  - Mandiant endpoint canonicalization (mandiant.com path productive,
    cloud.google.com path 404 confirmed)
  - Volexity retry-or-MCP-build decision (6 consecutive parse-errors)
  - ReliaQuest + Aikido retry eligibility
  - BlackFile → Redact (CL-CRI-1116) actor-profiler /new-actor
    candidate IF future A-grade sources corroborate
- **Streak update**: Eighth consecutive clean sentinel sweep (Tuesday
  06:00 / 12:00 / 18:00 + Wednesday 00:00 / 06:00 / 12:00 / 18:00 +
  Thursday 00:00 = 8 sentinels, zero FLASH dispatches). 06:00 EDT
  Thursday dawn sweep is the next FLASH evaluation window before
  AM-28 pre-brief collection at 07:30 EDT.
- **TLP:CLEAR.**
