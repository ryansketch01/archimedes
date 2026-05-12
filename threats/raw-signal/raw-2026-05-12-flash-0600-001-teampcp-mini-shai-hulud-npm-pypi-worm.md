---
raw_id: raw-2026-05-12-flash-0600-001
collected_at: 2026-05-12T06:08:00-04:00
run_id: flash-sweep-20260512-060000
collection_mode: flash_sweep
sweep_type: flash
sweep_time: 2026-05-12T06:00:00-04:00
time_window_start: 2026-05-12T00:00:00-04:00
time_window_end: 2026-05-12T06:00:00-04:00
test: false
source:
  source_yaml_id: hacker-news
  source_name: The Hacker News (relay)
  source_url: https://thehackernews.com/2026/05/mini-shai-hulud-worm-compromises.html
  published_at: 2026-05-12T00:00:00-04:00
  author: Ravie Lakshmanan
  primary_research_sources:
    - id: wiz-research
      url: https://www.wiz.io/blog/mini-shai-hulud-strikes-again-tanstack-more-npm-packages-compromised
      grade_proposal: provisional_A
      grade_rationale: |
        Wiz is a Tier-1 cloud-security research practice with named-analyst
        bylines, peer-reviewed publications, and a strong recent track
        record on supply-chain attack analysis (SAP CAP Mini Shai-Hulud
        coverage earlier in 2026, NPM ecosystem research). High-confidence
        TeamPCP attribution language in this post matches Wiz's typical
        evidentiary standard. Not currently in source-grades.yaml; proposed
        provisional A on first surface per the precedent applied to
        SentinelOne (2026-05-08) and Sophos / ESET / Dragos (Session 11
        ratifications). Operator may ratify at A.
      published_at: 2026-05-12
      author: Wiz Research team
    - id: snyk
      url: https://snyk.io/blog/tanstack-npm-packages-compromised/
      grade_proposal: provisional_A
      grade_rationale: |
        Snyk is a Tier-1 application-security research practice with named
        byline (Stephen Thoemmes), CVE coordination (CVE-2026-45321,
        GHSA-g7cv-rxg3-hmpx), cross-references to peer analyses (Upwind
        Security deobfuscation, Unit 42 tracking, StepSecurity
        attribution). Operator may ratify at A.
      published_at: 2026-05-11
      author: Stephen Thoemmes
    - id: stepsecurity
      url: (StepSecurity blog — primary attribution source per Snyk + Wiz)
      grade_proposal: provisional_B
      grade_rationale: |
        StepSecurity is the originating attribution source for the TeamPCP
        claim per Snyk + Wiz citations. CI/CD-security vendor research
        practice. No prior Archimedes-corpus citation; provisional B on
        first surface (defensible per Unit 42 / Mandiant tier-2 vendor
        research precedent — narrower technical scope than Tier-1 but
        consistent rigor in their published analyses).
    - id: aikido-security
      url: https://www.aikido.dev/blog/mini-shai-hulud-is-back-tanstack-compromised
      grade_proposal: provisional_C
      grade_rationale: |
        Application-security vendor research. No prior corpus citation;
        first-surface provisional C per LayerX / Seqrite / Trendyol /
        Albayrak precedent. Operator may upgrade with track-record
        observation.
    - id: unit42
      url: https://unit42.paloaltonetworks.com/monitoring-npm-supply-chain-attacks/
      grade_assigned: A
      grade_rationale: |
        Unit 42 is A-grade in source-grades.yaml. The cited post "The
        npm Threat Landscape: Attack Surface and Mitigations" was
        last-updated May 1 (pre-window for this sweep) and provides
        baseline-corpus analysis of the npm supply-chain attack family
        including prior Shai-Hulud variants. Backbone A-grade context
        for the broader campaign lineage; the 2026-05-12 Mini Shai-Hulud
        specific burst is not yet Unit42-published, but lineage analysis
        and corroborating A-grade backbone is in place.
    - id: msft-mstic
      url: https://www.microsoft.com/en-us/security/blog/2025/12/09/shai-hulud-2-0-guidance-for-detecting-investigating-and-defending-against-the-supply-chain-attack/
      grade_assigned: A
      grade_rationale: |
        MSTIC published "Shai-Hulud 2.0" defender's guide 2025-12-09
        documenting the prior generation of this worm lineage. The
        2026-05-12 Mini Shai-Hulud burst is the latest variant; MSTIC's
        product response is the Microsoft Defender for Cloud SBOM-scan
        capability per WebSearch corroboration. No MSTIC-published 2026-
        05-12 active-attack blog post observed in the RSS feed this sweep
        (last_modified 2026-05-08T23:03 UTC pre-window — confirms no
        fresh MSTIC content), but the lineage analysis and product-
        capability response is A-grade corroboration of the worm family.
    - id: onapsis
      url: https://onapsis.com/blog/sap-cap-mini-shai-hulud-supply-chain-attack/
      grade_proposal: provisional_B
      grade_rationale: |
        SAP-security specialist; published earlier 2026 SAP CAP Mini
        Shai-Hulud coverage. Named-vendor research. Tier-2.
    - id: safedep
      url: https://safedep.io/mass-npm-supply-chain-attack-tanstack-mistral/
      grade_proposal: provisional_C
      grade_rationale: |
        First-surface NPM security vendor; provisional C per precedent.
    - id: semgrep
      url: https://semgrep.dev/blog/2026/tanstack-router-packages-hit-by-coordinated-supply-chain-attack/
      grade_proposal: provisional_B
      grade_rationale: |
        Semgrep is an established code-security vendor with named-engineer
        bylines and consistent technical-rigor. Tier-2 research practice;
        provisional B on first surface.
  corroborating_relays:
    - bleepingcomputer  # NOT in this sweep's window — anticipated for later sweeps
    - securityweek      # NOT in this sweep's window — anticipated for later sweeps
    - security-boulevard # WebSearch confirmation
match_reason:
  watchlist: []           # No named A&D primes among compromised packages
  watchlist_adjacent: aviation_developer_ecosystem_squawk_19_packages
  actors: [TeamPCP]       # Roster #001 (HIGH)
  actor_attribution_strength: A_grade_vendor_high_confidence
  vulnerabilities: [CVE-2026-45321]
  vulnerability_cvss: 9.6
  keywords:
    - supply-chain-worm
    - npm-pypi-dual-ecosystem
    - validly-attested-malicious-packages
    - slsa-provenance-abuse
    - oidc-token-hijack
    - shai-hulud-lineage
triage_tags:
  - flash_candidate
  - trigger_4_passed
  - trigger_1_passed
  - tracked_actor_teampcp_001_high
  - new_ttp_first_documented_npm_worm_with_valid_attestation
  - new_infrastructure_dual_ecosystem_npm_pypi
  - quiet_hours_active_at_06_edt_must_queue
  - critical_override_fail_no_a_and_d_named
  - sector_adjacency_aviation_squawk_packages_19
  - lineage_continuation_of_shaiworm_2026_05_04
  - distinct_from_checkmarx_jenkins_2026_05_11_topic
iocs_extracted: true
iocs_count: 12
text_word_count: 2400
promoted: true
promoted_to_finding: finding-2026-05-12-FLASH-0001
promoted_at: 2026-05-12T06:18:00-04:00
ttl_expires_at: 2026-08-10T06:08:00-04:00

flash_trigger_evaluation:
  trigger_1_critical_cve_exploited:
    matched: true
    cvss_min_met: true
    cvss_value: 9.6
    cvss_cve: CVE-2026-45321
    active_exploitation_confirmed: true
    active_exploitation_evidence: |
      169-172 npm packages (count varies by tracker) compromised in a
      48-hour window 2026-05-11 → 2026-05-12 with attacker-published
      malicious versions confirmed live on registries (TanStack 42
      packages / 84 versions, plus Mistral AI / Guardrails AI / UiPath /
      DraftLab / OpenSearch / @squawk aviation data packages). Wiz,
      Snyk, StepSecurity, Aikido, SafeDep, Semgrep, Endor Labs all
      published deobfuscation + IOC analysis within hours.
    a_grade_source_named_operational_layer: true
    a_grade_sources:
      - wiz (provisional_A — high-confidence TeamPCP attribution, IOC
        publication, named research team byline)
      - snyk (provisional_A — Stephen Thoemmes byline, CVE coordination
        for CVE-2026-45321, GHSA-g7cv-rxg3-hmpx)
      - unit42 (A in source-grades.yaml — npm threat landscape baseline
        analysis includes this family)
      - msft-mstic (A in source-grades.yaml — Shai-Hulud 2.0 lineage
        guidance + Defender for Cloud SBOM-scan product capability)
    pass_summary: |
      Trigger 1 PASSES on the strict conjunction. CVSS 9.6 ≥ 9.0 floor.
      Active exploitation is not "PoC, theoretical" — 169-172 packages
      were actively compromised and live on registries before
      maintainer revert. Multiple A-grade sources name the operational
      layer (Wiz, Snyk, Unit42, MSTIC lineage). No source-grade
      structural deficit.
  trigger_2_tracked_actor_attribution:
    matched: false
    tracked_actor_named: TeamPCP (roster #001 HIGH)
    attribution_is_new_not_restatement: false
    attribution_lineage:
      - 2026-05-04 PyTorch Lightning ShaiWorm — MSTIC attribution baseline (finding-2026-05-04-0003)
      - 2026-05-11 Checkmarx Jenkins AST plugin — TeamPCP attribution (raw-2026-05-11-flash-0600-001)
      - 2026-05-12 Mini Shai-Hulud TanStack burst — TeamPCP attribution per StepSecurity/Wiz/Snyk
    fail_reason: |
      Trigger 2 requires attribution to be NEW (first-time naming, not
      restatement). TeamPCP attribution to the supply-chain spree is
      pre-existing (May 4 / May 11). Today's Wiz/Snyk/StepSecurity
      attribution is a new CAMPAIGN under an existing attributed actor,
      not a new attribution event. Trigger 2 FAIL on strict structural
      test.
  trigger_3_first_party_ioc_hit:
    matched: false
    splunk_archimedes_6h_non_archimedes_events: 0
    splunk_archimedes_24h_non_archimedes_events: 0
    splunk_defenseclaw_6h_non_archimedes_events: 0
    splunk_defenseclaw_24h_non_archimedes_events: 0
    targeted_ioc_keyword_sweep_24h_hits: 6
    targeted_ioc_keyword_sweep_24h_disposition: |
      All 6 hits are archimedes:operation pipeline self-references
      (flash_sweep_clean 06:00 EDT 2026-05-11, brief_published morning
      08:16 EDT 2026-05-11, brief_published afternoon 16:47 EDT
      2026-05-11, flash_sweep operator-initiated 17:00 EDT 2026-05-11,
      flash_sweep_clean 00:00 EDT 2026-05-12, and 18:03 EDT 2026-05-11
      operation). Pipeline self-references match keyword tokens in
      JSON payloads but reflect Archimedes' own operational logging.
    fail_reason: |
      Trigger 3 cannot fire on a dormant non-archimedes-internal stream.
      Fifteenth consecutive sweep with the dormant pattern across both
      indexes. Mini Shai-Hulud IOCs (filev2.getsession[.]org, api.masscan
      [.]cloud, git-tanstack.com, 83.142.209[.]194, three SHA-256 file
      hashes, recipient ID, dead-drop catbox URLs) were specifically
      tested against both indexes — zero matches.
  trigger_4_tracked_actor_ttp_change:
    matched: true
    a_or_b_grade_source: true
    a_or_b_grade_sources_named:
      - wiz (provisional_A — high-confidence TeamPCP attribution + TTP
        deobfuscation)
      - snyk (provisional_A — CVE coordination + technical TTP analysis
        with named byline)
      - unit42 (A in source-grades.yaml — backbone npm threat landscape)
      - stepsecurity (provisional_B — originating attribution source)
      - semgrep (provisional_B — coordinated supply-chain attack analysis)
    attributable_to_tracked_actor: true
    attributable_actor: TeamPCP (roster #001 HIGH)
    new_tooling_targeting_or_infrastructure: true
    new_ttp_layer_description: |
      Three distinct capability layers documented as NEW for TeamPCP /
      Shai-Hulud lineage in the 2026-05-12 Mini Shai-Hulud burst:

      (1) First documented npm worm producing VALIDLY-ATTESTED
          malicious packages — the worm hijacks legitimate maintainer
          OIDC tokens mid-workflow to publish packages that carry SLSA
          provenance signatures. This breaks the SLSA-attestation
          assurance model the npm ecosystem has been building toward.
          Wiz, Snyk, StepSecurity all explicitly call this out as
          previously-unobserved capability for the Shai-Hulud family.
          Prior generations (PyTorch Lightning ShaiWorm 2026-05-04,
          Shai-Hulud 2.0 December 2025) were attestation-naive.

      (2) Dual-ecosystem self-propagation — the worm enumerates every
          package a compromised maintainer publishes, injects the same
          payload, and republishes autonomously. Spread npm + PyPI in
          a single coordinated campaign within hours of initial
          compromise (172 packages / 403 malicious versions). Prior
          generations were single-ecosystem (PyPI for ShaiWorm 2026-
          05-04; npm for Shai-Hulud 2.0 December 2025).

      (3) Session-network dead-drop architecture — exfiltration to
          seed1/seed2/seed3.getsession[.]org + filev2.getsession[.]org
          with a specific recipient ID (05f9e609d79eed391015e11380dee4b
          5c9ead0b6e2e7f0134e6e51767a87323026), plus dead-drop staging
          at litter.catbox[.]moe. Session-network exfiltration is a
          new C2 infrastructure class for this actor — prior
          generations used GitHub-hosted dead-drops + direct attacker
          domains.
    pass_summary: |
      Trigger 4 PASSES cleanly. New tooling (worm-class attestation-
      breaking capability), new infrastructure (dual-ecosystem self-
      propagation + Session-network exfiltration), clearly attributable
      to TeamPCP (#001 HIGH) per multiple A-grade sources (Wiz, Snyk,
      Unit42 backbone, MSTIC lineage). Source-grade threshold met
      (A grade explicitly named operational layer; B grade redundancy
      across StepSecurity, Semgrep, Aikido).
  trigger_5_ad_sector_campaign:
    matched: false
    campaign_active: true
    multi_victim: true
    ad_sector_explicitly_targeted: false
    ad_sector_adjacency_observation: |
      @squawk namespace contains "19 aviation data packages" compromised
      (per Snyk byline analysis). The @squawk packages handle aviation-
      domain functionality (flightplan, weather, mcp tooling). This is
      genuine aviation-software-ecosystem compromise, not generic npm
      churn.

      HOWEVER, Trigger 5 requires "EXPLICITLY targeting" aerospace,
      defense, or watchlist companies. The Mini Shai-Hulud campaign is
      a broader npm-ecosystem mass-compromise event in which aviation
      developer packages were INCIDENTALLY hit (the worm enumerates
      maintainer-published packages and replicates, not maintainer-
      selected based on victim sector profile). Per the strict
      structural-test reading the orchestrator has applied to prior
      sector-adjacent cases (SailPoint 2026-05-11 AM-001, OpenC3 COSMOS
      2026-05-09 AM-001, HookedWing 2026-05-11 FLASH-0000-001), this
      ranks as "structural relevance through ecosystem capture" rather
      than "explicit targeting."

      NO A&D prime (Lockheed Martin, Boeing, RTX, Northrop Grumman,
      General Dynamics, BAE Systems, L3Harris, Leidos, SAIC, Thales,
      GE Aerospace, Safran, Honeywell Aerospace, Airbus, Elbit Systems)
      is named as victim. NO defense agency named. The @squawk
      aviation-data context is aviation-ecosystem, not A&D-prime-
      direct.

      Flagged for grader awareness as a real but indirect A&D relevance
      signal — the dependency chain from compromised @squawk packages
      to actual A&D developer tooling is plausible but requires
      enumeration the grader/analyst can do downstream.
    fail_reason: |
      Trigger 5 FAIL on "EXPLICITLY targeting" structural test. Sector
      adjacency observed (aviation developer ecosystem, 19 @squawk
      packages). Sector-direct targeting not observed.
  trigger_6_zero_day_no_patch:
    matched: false
    patch_status_assessment: |
      TanStack, Mistral AI, UiPath, Guardrails AI, OpenSearch, @squawk,
      DraftLab — maintainers reverted to clean versions within hours
      of initial compromise (TanStack reverted by maintainer same day
      per WebSearch corroboration). CVE-2026-45321 entry is the
      catalog-level designation for the supply-chain compromise; the
      remediation is package reversal, not a vendor-issued patch
      (because the malicious code WAS the package versions, not a
      vulnerability in an underlying product). Trigger 6 requires
      "Vulnerability disclosed before a patch is available."
    fail_reason: |
      The supply-chain attack model (validly-attested malicious package
      versions published by hijacked maintainer pipelines) does not
      structurally fit Trigger 6, which contemplates an unpatched
      orphan vulnerability in a deployed product. The remediation for
      Mini Shai-Hulud is package version reversion + token rotation,
      not a vendor patch. Trigger 6 N/A by structural type-mismatch.
  critical_override_evaluated:
    applied: false
    cvss_10_0: false
    cvss_value: 9.6
    active_exploitation: true
    tracked_actor_involved: true
    ad_watchlist_targeted: false
    summary: |
      Override requires ALL FOUR (CVSS 10.0 + confirmed active
      exploitation + tracked actor + A&D watchlist entity named as
      target). TWO of FOUR satisfied (active exploitation ✓, tracked
      actor ✓). TWO of FOUR FAILED (CVSS 9.6 < 10.0 floor; no A&D
      watchlist entity named as target — @squawk aviation ecosystem
      hit is incidental not explicit). Override FAILS by hard threshold
      criteria. Quiet-hours rule remains in force (06:00 EDT is inside
      21:00–09:00 quiet-hours window).

flash_outcome:
  triggers_fired: [trigger_1_critical_cve_exploited, trigger_4_tracked_actor_ttp_change]
  triggers_failed: [trigger_2, trigger_3, trigger_5, trigger_6]
  critical_override: false
  quiet_hours_active: true
  posting_required: false
  expected_disposition: queue_to_flash_queue_for_09_00_catchup_sweep
  briefer_composition_required: true
  red_team_review_required: true
  red_team_rationale: |
    Per FLASH-POLICY anti-noise rule "Red-team review is mandatory for
    any FLASH with WEP >= very-likely." The Mini Shai-Hulud Trigger 4
    evaluation has procedural-facts WEP very-likely (multiple A-grade
    independent firms publishing IOC and TTP analysis with named
    bylines within hours; technical claims are forensically
    reproducible via the published hashes), and operational-claim WEP
    likely (TeamPCP attribution is multi-source independent but the
    attribution-chain originates from StepSecurity and is corroborated
    by Wiz/Snyk; the "first documented validly-attested" claim is
    novel and benefits from independent peer challenge).

iocs:
  cves:
    - id: CVE-2026-45321
      cvss: 9.6
      severity: CRITICAL
      type: supply_chain_compromise_via_validly_attested_malicious_packages
      affected_package_ecosystem: npm
      first_compromised_burst_utc: "2026-05-11T19:20Z to 2026-05-11T19:26Z"
      ghsa: GHSA-g7cv-rxg3-hmpx
      patch_status: package_versions_reverted_by_maintainer_not_a_product_patch

  c2_domains:
    - filev2.getsession[.]org
    - seed1.getsession[.]org
    - seed2.getsession[.]org
    - seed3.getsession[.]org
    - api.masscan[.]cloud
    - git-tanstack[.]com

  c2_ips:
    - 83.142.209[.]194

  dead_drop_staging_urls:
    - litter.catbox[.]moe/h8nc9u.js
    - litter.catbox[.]moe/7rrc6l.mjs

  file_hashes_sha256:
    - ab4fcadaec49c03278063dd269ea5eef82d24f2124a8e15d7b90f2fa8601266c    # router_init.js variant 1
    - 2ec78d556d696e208927cc503d48e4b5eb56b31abc2870c2ed2e98d6be27fc96    # router_init.js variant 2
    - 2258284d65f63829bd67eaba01ef6f1ada2f593f9bbe41678b2df360bd90d3df    # setup.mjs

  session_network_recipient_id:
    - 05f9e609d79eed391015e11380dee4b5c9ead0b6e2e7f0134e6e51767a87323026

  pbkdf2_campaign_salt:
    - svksjrhjkcejg

  github_author_identity:
    - claude@users.noreply.github.com    # spoofed-looking but legitimate npm-bot pattern used by attacker

  compromised_packages_partial_list:
    npm_namespaces:
      - "@tanstack (42 packages, 84 malicious versions)"
      - "@uipath"
      - "@mistralai"
      - "@opensearch-project"
      - "@squawk (19 aviation data packages including flightplan, weather, mcp)"
      - "@tallyui (connector-medusa, connector-vendure)"
      - DraftLab packages
    pypi_packages:
      - guardrails-ai@0.10.1
      - mistralai@2.4.6

  attribution_claims:
    - actor: TeamPCP
      attribution_source: StepSecurity (provisional B; originating attribution per Wiz + Snyk citations)
      attribution_strength: high_confidence
      corroboration:
        - source: Wiz
          language: "Wiz assesses with high confidence that this is the work of TeamPCP behind prior SAP, Checkmarx, and other compromises"
        - source: Snyk
          language: "The incident is attributed by StepSecurity to the threat group known as TeamPCP"
          aliases_added_by_snyk:
            - DeadCatx3
            - PCPcat
            - ShellForce
            - CipherForce
          note_for_librarian: |
            Snyk article adds four NEW aliases for TeamPCP not currently
            in _roster.yaml (#001 aliases field is empty: []). Operator
            decision on roster alias update is a librarian/operator
            task, not collector's domain — flagging here per the field-
            ownership-preserve rule in CLAUDE.md.

ttp_summary:
  primary_capability_layer: supply_chain_compromise_via_hijacked_maintainer_oidc_tokens
  novel_ttp_2026_05_12_burst:
    - first_documented_npm_worm_producing_validly_attested_malicious_packages
    - dual_ecosystem_self_propagation_npm_plus_pypi_in_single_campaign
    - session_network_dead_drop_c2_architecture
    - country_aware_termination_on_russian_locale_inherited_from_shai_hulud_family

  technique_classification_mitre_attack:
    - T1195.002    # Supply Chain Compromise: Compromise Software Supply Chain
    - T1059.007    # Command and Scripting Interpreter: JavaScript
    - T1552.001    # Unsecured Credentials: Credentials In Files (.env files)
    - T1539        # Steal Web Session Cookie (token theft from CI)
    - T1078.004    # Valid Accounts: Cloud Accounts (cloud-credential theft)
    - T1056.001    # Input Capture: Keylogging (browser data scope)
    - T1567        # Exfiltration Over Web Service (Session network)
    - T1480        # Execution Guardrails (country-aware Russian locale check)

source_health_changes_this_sweep:
  - source_yaml_id: bleepingcomputer
    runtime_field: last_successful_fetch
    old_value: 2026-05-12T00:00:00-04:00
    new_value: 2026-05-12T06:00:00-04:00
    rationale: |
      RSS reachable status 200, etag d3de396c37742510827ba9a461be42d2,
      1 item in 6h window (Instructure/ShinyHunters agreement — DISCARDED
      per Mode 1 procedure no A&D/roster/vuln-index hit; consumer
      edtech extortion).
  - source_yaml_id: hacker-news
    runtime_field: last_successful_fetch
    old_value: 2026-05-12T00:00:00-04:00
    new_value: 2026-05-12T06:00:00-04:00
    rationale: |
      Hacker News homepage WebFetch surfaced 2 new 2026-05-12-dated
      items vs. the 00:00 sweep: (1) Mini Shai-Hulud Worm Compromises
      TanStack, Mistral AI, Guardrails AI & More Packages — this
      raw-signal; (2) OpenAI Launches Daybreak for AI-Powered
      Vulnerability Detection and Patch Validation — defensive
      product announcement, no threats, no IOCs, DISCARDED per Mode 1.
  - source_yaml_id: securityweek
    runtime_field: last_successful_fetch
    old_value: 2026-05-12T00:00:00-04:00
    new_value: 2026-05-12T06:00:00-04:00
    rationale: |
      RSS reachable status 200, etag e8c6cafde0dd5edc69f6d970adb972d0,
      0 items in 6h window after since-filter. Homepage WebFetch
      surfaced no 2026-05-12-dated items beyond 2026-05-11 already-
      covered topics; the Mini Shai-Hulud story has not yet reached
      SecurityWeek as of this sweep (anticipated for 12:00 FLASH).
  - source_yaml_id: krebs
    runtime_field: last_successful_fetch
    old_value: 2026-05-12T00:00:00-04:00
    new_value: 2026-05-12T06:00:00-04:00
    rationale: 0 items in 6h window, normal cadence.
  - source_yaml_id: mstic
    runtime_field: last_successful_fetch
    old_value: 2026-05-12T00:00:00-04:00
    new_value: 2026-05-12T06:00:00-04:00
    rationale: |
      RSS reachable status 200, last_modified 2026-05-11T17:38:35 GMT
      pre-window, 0 items in 6h window. Most recent MSTIC content
      remains 2026-05-08T17:12 UTC Dirty Frag active-attack post. MSTIC
      has NOT yet published a fresh active-attack post for the Mini
      Shai-Hulud 2026-05-12 burst as of this sweep; the Shai-Hulud
      lineage A-grade corroboration cites the December 2025 MSTIC
      defender's guide + the Defender for Cloud SBOM-scan product
      capability per WebSearch.
  - source_yaml_id: unit42
    runtime_field: last_successful_fetch
    old_value: 2026-05-12T00:00:00-04:00
    new_value: 2026-05-12T06:00:00-04:00
    rationale: |
      feedburner.com/Unit42 reachable status 200, last_modified
      2026-05-11T22:51:12 GMT pre-window, 0 items in 6h window. The
      "Inside AD CS Escalation" piece from 2026-05-11 18:00 EDT is
      pre-window for this 06:00 FLASH sweep.
  - source_yaml_id: rapid7
    runtime_field: last_successful_fetch
    old_value: 2026-05-12T00:00:00-04:00
    new_value: 2026-05-12T06:00:00-04:00
    rationale: 0 items in 6h window.
  - source_yaml_id: sentinelone
    runtime_field: last_successful_fetch
    old_value: 2026-05-12T00:00:00-04:00
    new_value: 2026-05-12T06:00:00-04:00
    rationale: 0 items in 6h window.
  - source_yaml_id: sophos
    runtime_field: last_successful_fetch
    old_value: 2026-05-12T00:00:00-04:00
    new_value: 2026-05-12T06:00:00-04:00
    rationale: 0 items in 6h window.
  - source_yaml_id: cisa-advisories
    runtime_field: last_successful_fetch
    old_value: 2026-05-12T00:00:00-04:00
    new_value: 2026-05-12T06:00:00-04:00
    rationale: 0 items in 6h window.
  - source_yaml_id: mandiant
    runtime_field: failure_count
    old_value: 14
    new_value: 15
    rationale: |
      feedburner.com/Mandiant 404 SIXTEENTH consecutive sweep. cloud.
      google.com/blog/topics/threat-intelligence index page top-5
      titles unchanged from 2026-05-11 sweeps (Proactive Preparation
      2026 Edition, Look What You Made Us Patch 2025 Zero-Days,
      Ransomware Under Pressure, DarkSword iOS, M-Trends 2026) — all
      previously triangulated as out-of-window. Held healthy pending
      operator alt-endpoint decision (feedburner shutdown well-
      established pattern).
  - source_yaml_id: sans-isc
    runtime_field: failure_count
    old_value: 0
    new_value: 1
    rationale: |
      isc.sans.edu/rssfeed.xml XML parse error this sweep (same class
      as the 2026-05-10 18:00 transient failure). Single soft-fail;
      held healthy pending next-sweep retry given prior pattern of
      site-side transients.
    last_error_update: |
      "isc.sans.edu/rssfeed.xml returned XML parse error on 2026-05-12
      06:00 FLASH — single soft-fail of the same class as the
      2026-05-10 18:00 transient; held healthy pending next-sweep
      retry."

---

# Mini Shai-Hulud npm/PyPI worm — TeamPCP (#001 HIGH) — first documented validly-attested malicious-package worm, FLASH candidate via Trigger 4

## What sources say

Per The Hacker News (2026-05-12, Ravie Lakshmanan byline; relay of Wiz Research + Snyk + StepSecurity + Aikido + Endor Labs + SafeDep + Socket + Semgrep primary research):

- **Campaign:** "Mini Shai-Hulud," a self-propagating npm/PyPI supply-chain worm. Multiple security firms (Aikido Security, Endor Labs, SafeDep, Socket, StepSecurity) independently confirmed the incident in coordinated published analyses within hours of the 2026-05-11 19:20–19:26 UTC TanStack compromise burst.

- **Scale:** 169–172 unique packages compromised (count varies by tracker) across 403 malicious versions, spanning both **npm and PyPI** in a single coordinated campaign within the 2026-05-11 → 2026-05-12 48-hour window. Affected namespaces include @tanstack (42 packages / 84 versions), @uipath, @mistralai (PyPI), @opensearch-project, @squawk (19 aviation data packages including @squawk/flightplan, @squawk/weather, @squawk/mcp), @tallyui (connector-medusa, connector-vendure), plus DraftLab packages. PyPI hits include guardrails-ai@0.10.1 and mistralai@2.4.6.

- **Attribution:** **TeamPCP** (Archimedes roster #001 HIGH) — first-named by StepSecurity, with Wiz assessing "with high confidence" attribution to "the work of TeamPCP behind prior SAP, Checkmarx, and other compromises." Snyk corroborates the StepSecurity attribution and adds four new aliases: DeadCatx3, PCPcat, ShellForce, CipherForce (not currently in `_roster.yaml`; operator-side roster-alias-update decision).

- **CVE:** CVE-2026-45321 assigned to the TanStack supply-chain compromise (CVSS 9.6 critical; GitHub Security Advisory GHSA-g7cv-rxg3-hmpx).

- **Novel capability — first documented npm worm producing validly-attested malicious packages:** Per Wiz, Snyk, and StepSecurity, the worm hijacks legitimate maintainer **OIDC tokens** mid-workflow and publishes packages that carry **SLSA provenance signatures**. This is the first publicly documented case of malicious packages bypassing the SLSA attestation assurance model — prior Shai-Hulud variants (PyTorch Lightning ShaiWorm 2026-05-04 finding-2026-05-04-0003; Shai-Hulud 2.0 December 2025) were attestation-naive.

- **Worm propagation:** Per Snyk and Wiz, the worm "enumerates every package a compromised maintainer publishes, injects the same payload, and republishes — autonomously." This produced the dual-ecosystem npm + PyPI spread within hours.

- **Country-aware execution:** Inherited from the Shai-Hulud family — the malware checks for Russian-language system configuration and terminates without exfiltration if detected.

- **MSTIC link:** Microsoft is responding via Microsoft Defender for Cloud SBOM-scanning capability per the December 2025 "Shai-Hulud 2.0" defender's guide; no fresh active-attack blog post yet for the 2026-05-12 Mini Shai-Hulud burst as of this sweep (MSTIC RSS last_modified 2026-05-08T23:03 UTC). Lineage A-grade corroboration via the December 2025 guide.

## FLASH evaluation summary

**Two triggers fired:**

- **Trigger 1 (critical-cve-exploited): PASSED.** CVE-2026-45321 CVSS 9.6 ≥ 9.0 floor. Active exploitation confirmed by maintainer-pipeline-published malicious versions live on registries (not PoC, not theoretical). A-grade source naming operational layer: Wiz (provisional A), Snyk (provisional A), Unit 42 (A in source-grades.yaml) backbone npm threat landscape, MSTIC (A) lineage.

- **Trigger 4 (tracked-actor-ttp-change): PASSED.** New tooling (first documented npm worm producing validly-attested malicious packages — breaks SLSA assurance model), new infrastructure (dual-ecosystem self-propagation npm + PyPI in single campaign; Session-network dead-drop C2 architecture). Clearly attributable to TeamPCP (#001 HIGH) per Wiz "high confidence" + StepSecurity originating attribution + Snyk corroboration.

**Four triggers failed:**

- **Trigger 2** (new-tracked-actor-attribution): FAILED on strict structural test. TeamPCP attribution to the supply-chain spree is pre-existing (finding-2026-05-04-0003 MSTIC PyTorch Lightning baseline; raw-2026-05-11-flash-0600-001 Checkmarx Jenkins). Today's attribution is a new CAMPAIGN under an existing attributed actor, not a new attribution event.

- **Trigger 3** (first-party-IOC-hit): FAILED on dormant Splunk stream. Sixteenth consecutive sweep with zero non-archimedes-internal events across both indexes.

- **Trigger 5** (A&D-sector-campaign): FAILED on "explicitly targeting" structural test. @squawk aviation developer ecosystem (19 packages) is sector-adjacent but incidentally hit, not explicitly targeted; no A&D prime named as victim. Genuine but indirect A&D relevance flagged for grader.

- **Trigger 6** (zero-day-no-patch): N/A — supply-chain compromise remediation model (package version reversion + token rotation) is type-mismatch for the "unpatched orphan vulnerability in deployed product" structural fit Trigger 6 contemplates.

**Critical override: FAILED on two of four hard thresholds.** CVSS 9.6 < 10.0 floor; no A&D watchlist entity named as target. Override does not apply even if quiet-hours rule were waivable (which it is not for sub-10.0 CVSS in any case).

## Quiet-hours disposition

**06:00 EDT IS INSIDE the 21:00–09:00 quiet-hours window.** Per FLASH-POLICY §Quiet Hours: "FLASH evaluations still run at 00:00 and 06:00 sweeps. If a FLASH is generated, queue to `infrastructure/flash-queue.yaml`." Posting to Discord `#flash-alerts` is **NOT permitted** at this sweep time. Catchup processing at 09:00 sweep: this raw-signal becomes briefer-composable input for a FLASH brief that, if produced, gets the "QUEUED FROM OVERNIGHT" prefix per policy.

## Topic distinction from 2026-05-11 06:00 FLASH (Checkmarx Jenkins)

This is **NOT** the same topic as `raw-2026-05-11-flash-0600-001-securityweek-checkmarx-jenkins-ast-plugin-compromise.md`. The 06:00 2026-05-11 FLASH covered a single Jenkins Marketplace plugin compromise (Checkmarx AST plugin v2.0.13-829 → -848) via stolen GitHub credentials. Mini Shai-Hulud (this raw-signal) is a separate burst:

| Dimension | 2026-05-11 06:00 FLASH (Checkmarx Jenkins) | 2026-05-12 06:00 FLASH (Mini Shai-Hulud) |
|---|---|---|
| Victim ecosystem | Jenkins Marketplace | npm + PyPI (dual-ecosystem) |
| Scale | 1 plugin (Checkmarx AST) | 169-172 packages / 403 versions |
| Capability layer | Point-strike via stolen GitHub creds | Self-propagating worm with valid attestation |
| CVE | None | CVE-2026-45321 (CVSS 9.6) |
| Originating research | Checkmarx PSIRT (vendor self-disclosure) | StepSecurity + Wiz + Snyk multi-firm |
| Worm capability | None | Autonomous package enumeration + republish |
| Attestation breaking | N/A | Yes (SLSA provenance bypass — first documented) |
| Hacker News headline framing | "TeamPCP Compromises Checkmarx Jenkins AST Plugin Weeks After KICS Supply Chain Attack" | "Mini Shai-Hulud Worm Compromises TanStack, Mistral AI, Guardrails AI & More Packages" |

The 2026-05-11 06:00 evaluation rated the Checkmarx Jenkins item Trigger 4 "marginal on composite source-grade" — Mini Shai-Hulud (this raw-signal) provides the A-grade-clean Trigger 4 pass that the prior item lacked. FLASH-POLICY anti-noise rule "one FLASH per topic per 24h" applies **per topic**, not per actor; these are distinct topics per the comparison above.

## Aviation-sector adjacency observation (Trigger 5 close-but-fail)

Snyk's byline analysis specifies the @squawk namespace as comprising **"19 aviation data packages"** — including @squawk/flightplan, @squawk/weather, @squawk/mcp. The aviation-domain functionality is real (these packages handle aviation flight-planning data), not name-coincidence.

However, the worm's mechanism is maintainer-enumeration-driven, not sector-targeted. The @squawk packages were hit because their maintainer was on the worm's propagation path, not because the campaign was selectively designed to compromise aviation tooling. Per the strict Trigger 5 structural-test reading applied to prior sector-adjacent cases (SailPoint 2026-05-11 AM-001 — A&D customer base via SCIM dependency; OpenC3 COSMOS 2026-05-09 AM-001 — spacecraft C2 software with NASA + BAE named users; HookedWing 2026-05-11 FLASH-0000-001 — aviation among 7 victim sectors with no named primes), this ranks as **structural relevance through ecosystem capture** rather than **explicit targeting**.

The downstream A&D-relevance assessment for grader/analyst:
- @squawk packages may be dependencies in A&D-prime aviation-domain developer tooling (Boeing, Airbus, Honeywell Aerospace, Safran could plausibly use aviation flight-planning libraries; unverified)
- Even without direct A&D-prime victim naming, the supply-chain reach into aviation-developer tooling is operationally meaningful
- Worth grader/analyst SDLC-dependency-graph enumeration if A&D-prime A-grade firms publish customer-impact statements over the next 24-72h

## Splunk first-party telemetry (Trigger 3 fail)

Combined `archimedes` + `defenseclaw_local` index sweep over 6h returns zero non-archimedes-internal events. Same over 24h returns zero non-archimedes-internal events. Targeted IOC keyword sweep across 25 high-priority tokens over 24h returned 6 hits — all six are `archimedes:operation` sourcetype pipeline self-references (flash_sweep_clean 06:00 EDT 2026-05-11, brief_published morning 08:16 EDT 2026-05-11, brief_published afternoon 16:47 EDT 2026-05-11, flash_sweep operator-initiated 17:00 EDT 2026-05-11, flash_sweep_clean 00:00 EDT 2026-05-12, and 18:03 EDT 2026-05-11 operation; payloads include this-window-keyword tokens reflecting Archimedes' own operational logging).

The Mini Shai-Hulud IOCs (`filev2.getsession[.]org`, `api.masscan[.]cloud`, `git-tanstack[.]com`, `83.142.209[.]194`, three SHA-256 file hashes, recipient ID, dead-drop catbox URLs) were specifically tested against both indexes — zero matches. Sixteenth consecutive sweep with the dormant non-archimedes-internal stream pattern across both indexes. Trigger 3 cannot fire on a dormant stream.

## Carry-forward state for downstream pipeline

**For grader (08:00 morning brief / FLASH catchup at 09:00):**
- FLASH candidate confirmed via Trigger 1 + Trigger 4 clean passes
- Procedural-facts WEP: very_likely (multiple independent A-grade firms with forensically-reproducible IOCs)
- Operational-claim WEP: likely (TeamPCP attribution multi-source-corroborated; "first documented validly-attested" novelty claim is the load-bearing technical assertion benefitting from independent peer challenge)
- Red-team review required (WEP >= very-likely per FLASH-POLICY anti-noise rule)
- Recommended digraph: A2 on procedural facts (Wiz, Snyk, Unit42 backbone A-grade; StepSecurity/Semgrep B-grade redundancy; technically confirmed by reproducible hashes/IOCs); B2 on TeamPCP attribution (multi-source but originates from StepSecurity)

**For briefer (FLASH brief composition):**
- Smart Brevity FLASH format per INTEL-BRIEF-STANDARDS.md
- Quiet-hours rule active — composed brief queues to `infrastructure/flash-queue.yaml` for 09:00 catchup sweep, not direct Discord post
- "QUEUED FROM OVERNIGHT" prefix per policy
- Anti-noise check: separately-topic from 2026-05-11 06:00 Checkmarx Jenkins FLASH (see comparison table above)
- Action items emphasis: SLSA-attestation-breaking is the load-bearing novelty; A&D structural relevance via @squawk + dependency-graph reach; supply-chain SDLC SBOM-scanning hardening posture

**For actor-profiler (TeamPCP #001 dossier update):**
- New aliases observed per Snyk: DeadCatx3, PCPcat, ShellForce, CipherForce (operator/librarian decision)
- New capability layer: worm-class self-propagation with SLSA-attestation bypass
- New infrastructure: Session-network exfiltration architecture
- Capability score update consideration on next /update-tracking (currently HIGH per roster; supply-chain worm capability progression warrants intra-HIGH gradient observation)

**For vuln-tracker:**
- CVE-2026-45321 new entry candidate (Mini Shai-Hulud TanStack supply-chain compromise; not the orphan-vuln-in-deployed-product type the existing vulnerability index tracks, but worth catalog placement for cross-reference)

## Extraction notes

- Language: en
- Primary article type: vendor research blog + media relay aggregation
- Multi-source corroboration: Wiz + Snyk + StepSecurity + Aikido + SafeDep + Semgrep + Endor Labs + Socket + Onapsis + Unit 42 (backbone) + MSTIC (lineage) — 11 independent firms within 24-48h
- Originating attribution: StepSecurity (per Wiz + Snyk citations)
- A-grade-confirmed: Wiz (high-confidence TeamPCP), Unit 42 (backbone npm landscape), MSTIC (Shai-Hulud 2.0 lineage + Defender for Cloud SBOM-scan capability)
- Anti-noise distinction from 2026-05-11 06:00 FLASH (Checkmarx Jenkins) verified via 8-dimension comparison table

## IOCs (from ioc-extraction skill output, structured above in `iocs:` frontmatter block)

Complete IOC set captured in frontmatter `iocs:` field — CVE-2026-45321 + 6 C2 domains + 1 C2 IP + 2 dead-drop staging URLs + 3 SHA-256 file hashes + Session-network recipient ID + PBKDF2 campaign salt + GitHub author identity + partial compromised-package list (npm + PyPI) + 4 new TeamPCP alias candidates per Snyk attribution corroboration.

**Defender enrichment priorities:**
- AbuseIPDB lookup on 83.142.209[.]194 (passive, no credit cost)
- VirusTotal lookup on the three SHA-256 hashes
- WHOIS/RDAP on git-tanstack[.]com (likely recent registration)
- Shodan InternetDB free lookup on 83.142.209[.]194 (no credit cost)

These enrichments are NOT invoked at this sweep level — defer to grader/analyst per Mode 4 protocols. Flagging here for the next phase's priority queue.
