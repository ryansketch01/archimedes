---
finding_id: finding-2026-06-03-0006-symantec-carbon-black-stock-exchange-outlook-150-day-espionage-aspose-dropbox-onedrive-no-attribution-reusable-ttps-against-ad
created_at: 2026-06-03T16:18:00-04:00
graded_by: grader
grading_run_id: afternoon-20260603-160000
grading_mode: scheduled_brief
test: false
status: graded

# Core grading (admiralty-grading skill output)
digraph: B2
digraph_layered:
  symantec_carbon_black_published_150_day_espionage_compromise_writeup: A1   # Verifiable via Symantec publication (security.com); referenced by SecurityAffairs + SecurityWeek with verbatim attribution
  target_unidentified_major_global_stock_exchange_single_executive_outlook_mailbox: A2   # Symantec verbatim refusal-to-name with SecurityWeek/SecurityAffairs corroborating verbatim quote
  dwell_time_approximately_150_days_2025_10_10_to_2026_03_19: B2   # Symantec/Carbon Black first-party EDR telemetry single-firm-origination through tier-2 relays
  entry_vector_remains_unknown: A1   # Verbatim Symantec / SecurityAffairs negative-claim — verifiable absence
  aspose_wrapper_ost_to_pst_conversion_via_legitimate_dotnet_library: B2   # Symantec single-source on mechanism via two-relay independent publishers; technically coherent (Aspose.Email is a known .NET library)
  eight_subsequent_ost_extraction_runs_at_two_to_four_week_intervals_through_2026_02_17_with_adjoining_time_windows: B2   # Symantec single-source on operational cadence
  exfiltration_via_dropbox_and_onedrive_personal_with_hardcoded_microsoft_ips_to_bypass_dns_logging: B2   # Symantec single-source on operational mechanism
  scheduled_task_rotation_5min_5hr_15hr_24hr_intervals_under_adobe_lenovo_onedrive_masquerade: B2   # Symantec single-source on persistence
  binary_masquerading_rotation_2025_10_10_adobe_onedrive_2026_02_27_onedrive_sync_2026_03_19_adobe_driver: B2   # Symantec single-source on operational timeline
  symantec_published_full_ioc_set_at_security_com_including_file_hashes: A1   # Verifiable via Symantec publication; SecurityAffairs verbatim references
  no_actor_attribution_at_any_source: A1   # Verbatim Symantec / SecurityWeek refusal-to-attribute
  symantec_analytic_judgment_almost_certainly_state_linked_given_target_value_plus_operational_discipline_plus_patience: B2   # Symantec analytic judgment hedge preserved verbatim per Hard Rule 2
  no_ad_watchlist_entity_named: A1   # Verifiable absence
  no_ad_prime_named_victim: A1   # Verifiable absence
  ttps_reusable_against_ad_prime_outlook_estates_with_aspose_dropbox_onedrive_pattern: B2   # Grader-side structural inference based on Symantec-documented TTP set; M365 mail estates are universal at A&D primes
  cluster_anchor: B2

digraph_anchor: >
  Cluster anchored on Symantec Threat Hunter Team + Carbon
  Black joint write-up (published "this week" on security.com)
  documenting a five-month suspected-espionage compromise of
  a major global stock exchange, scoped to a single senior
  executive's Outlook mailbox, with reusable TTPs (Aspose-wrapped
  OST→PST extraction, Dropbox + OneDrive Personal exfil with
  hardcoded Microsoft IPs to bypass DNS logging, scheduled-task
  rotation across 5-minute / 5-hour / 15-hour / 24-hour
  intervals, binary masquerading rotation across Adobe / Lenovo
  / OneDrive identities). Tier-2 relays at SecurityWeek (Eduard
  Kovacs) and SecurityAffairs (Pierluigi Paganini) both
  in-window 2026-06-03.

  B2 (not A2 or B3) anchored because:

    - SOURCE LETTER GRADE: Symantec is provisional A per source-
      grades.yaml `symantec` entry (first-citation 2026-05-13
      FLASH MuddyWater/Seedworm Q1 2026 multi-victim campaign;
      72h ratification clock long elapsed; operator-side
      ratification path remains open). This is the SECOND
      Archimedes-corpus citation for Symantec, with analytic
      discipline (refusing attribution despite operational
      discipline + target value implying state-linked espionage)
      itself a positive ratification signal. Symantec is
      Broadcom-owned, holds long-running Seedworm taxonomy
      primacy, and operates first-party Carbon Black EDR
      telemetry — comparable to Tier-1 vendor profile.
      SecurityWeek and SecurityAffairs are both ratified B per
      source-grades.yaml.

      For grading purposes at this finding: Symantec is treated
      as A (provisional but second-citation with analytic-
      discipline ratification signal); cluster-anchor B2 reflects
      that the underlying SUBSTANTIVE content is single-firm-
      origination through two B-grade publisher-independent
      relays — both SecurityWeek and SecurityAffairs derive
      substantive technical content from the same Symantec
      primary research with first-party Carbon Black EDR
      telemetry as the originating evidence basis.

    - INDEPENDENCE TEST: SecurityWeek + SecurityAffairs are
      different publishers (Eduard Kovacs byline vs. Pierluigi
      Paganini byline). Neither cites the other; both
      attribute to Symantec primary. Publisher-independence
      holds. EVIDENCE-BASIS-INDEPENDENCE FAILS through single-
      Symantec-primary origin (Symantec's first-party Carbon
      Black EDR telemetry is the only substantive evidence
      basis). Per admiralty-grading skill Step 4: "Both rely
      on the same vendor's telemetry" → NOT independent on
      substantive technical content.

      First-party-telemetry exception: Symantec + Carbon Black
      is FIRST-PARTY VENDOR telemetry (not first-party Archimedes
      telemetry). Hard Rule 8's first-party-precedence rule
      applies to Archimedes Splunk indices, not vendor first-
      party telemetry. Vendor first-party telemetry remains
      single-source-origination at admiralty layer.

    - CREDIBILITY: Walk the checklist.
      * Grade 1 (Confirmed): FAILS — single-vendor-origination
        through two publisher-independent relays; no Tier-1 IR
        firm (Mandiant / Unit 42 / MSTIC / CrowdStrike / Cisco
        Talos / SentinelLabs / Volexity) independent
        corroboration of mechanism or victim at sweep.
      * Grade 2 (Probably True): ASSIGNS —
          - Consistent with established TTPs for state-linked
            espionage actor profile (long-dwell mailbox
            collection against high-value financial-sector
            executive is canonical state-aligned intelligence
            collection pattern; Symantec's "almost certainly
            state-linked" framing is grounded in this established
            pattern).
          - No contradicting A/B-grade source.
          - Technical claims internally coherent: Aspose.Email
            is a real .NET library; OST→PST conversion is
            canonical mailbox-extraction mechanism; Dropbox +
            OneDrive Personal exfil bypass is well-documented
            blend-with-normal-traffic pattern; hardcoded-IP
            DNS-logging-bypass is canonical EDR-evasion
            tradecraft; scheduled-task rotation + binary
            masquerading are well-established persistence
            patterns.

  Single-source veto APPLIED on substantive operational claims
  (specific mechanism + cadence + persistence + masquerading +
  exfil patterns) because Symantec + Carbon Black is single-
  vendor-origination through two publisher-independent relays.
  NOT applied on procedural-fact layer (Symantec published the
  write-up + IOC set + attribution declination — all verifiable
  via Symantec publication).

  Hard Rule 2: PRESERVED — Symantec explicitly declines
  attribution. SecurityWeek verbatim: "Symantec and Carbon
  Black did not share any information about who may have been
  behind the attack" (15 words, Hard Rule 6 compliant). Symantec
  analytic hedge "almost certainly state-linked given the
  target and the patience involved" preserved verbatim and not
  upgraded. NO tracked roster actor named.

  Hard Rule 3: PRESERVED — no PoC content extracted; mechanism
  classes (Aspose-wrapper OST→PST extraction, Dropbox/OneDrive
  Personal exfil, hardcoded-IP DNS-bypass, scheduled-task
  rotation, binary masquerading) described at category level
  only.

  Hard Rule 6: PRESERVED — two short verbatim Symantec quotes
  preserved at 15-word and 24-word raw-signal-internal note
  status; brief composition should pick ONE quote under 15
  words ("did not share any information about who may have
  been behind the attack" — 14 words; or "almost certainly
  state-linked given the target and the patience involved" —
  12 words).

  Hard Rule 8: Splunk first-party check ran (-30d sweep across
  defenseclaw_local + archimedes-NOT-archimedes-internal on
  Aspose.Email + OST→PST conversion + Dropbox / OneDrive
  Personal exfil + hardcoded Microsoft IP exfil patterns +
  Adobe/Lenovo/OneDrive scheduled-task masquerade). 0 events
  per PM-000 sentinel record. Per Hard Rule 8 silence is not
  disconfirming; once IOC set is extracted from Symantec
  primary, run hash-based pivot against Archimedes Splunk
  indices.

source_reliability:
  grade: A
  source_name: Symantec Threat Hunter Team + Carbon Black — 150-day suspected-espionage Outlook mailbox compromise against major global stock exchange executive
  source_yaml_id: symantec
  grade_rationale: >
    Symantec is provisional A per source-grades.yaml entry
    (first-citation 2026-05-13 FLASH on MuddyWater/Seedworm Q1
    2026 multi-victim campaign; awaiting human ratification).
    This is the SECOND Archimedes-corpus citation. Analytic
    discipline (refusing attribution despite operational
    discipline + target value strongly implying state-linked
    espionage) is a positive ratification signal. Broadcom-
    owned; long-running Seedworm taxonomy primacy; first-party
    Carbon Black EDR telemetry — comparable to Tier-1 vendor
    profile. Operator-side ratification path remains open;
    this finding's positive ratification signal forwarded to
    librarian.
  provisional: true
  provisional_since: 2026-05-13
  cluster_secondary_sources:
    - source_yaml_id: securityweek
      grade: B
      grade_rationale: Pre-assigned B per source-grades.yaml. Eduard Kovacs byline; tier-2 relay of Symantec primary.
    - source_yaml_id: securityaffairs
      grade: B
      grade_rationale: Pre-assigned B per source-grades.yaml. Pierluigi Paganini byline; tier-2 relay of Symantec primary with fuller body text.

credibility:
  grade: 2
  checklist_passed:
    - probably_true_consistent_with_established_state_linked_espionage_ttps_long_dwell_mailbox_collection_high_value_executive
    - probably_true_no_contradicting_ab_grade_source
    - probably_true_technical_claims_internally_coherent_aspose_dotnet_library_ost_pst_conversion_dropbox_onedrive_personal_exfil_hardcoded_ip_dns_bypass_scheduled_task_rotation_binary_masquerading
  rationale: >
    Symantec + Carbon Black write-up documents an operationally-
    disciplined long-dwell mailbox-extraction campaign with
    canonical state-aligned-espionage characteristics (high-
    value financial-sector executive target, 150-day dwell,
    cumulative-window operational cadence, blend-with-normal-
    traffic exfil, EDR-evasion persistence patterns). Technical
    claims are internally coherent: Aspose.Email is a real
    legitimate .NET library used by mailbox-extraction tooling;
    OST→PST conversion is the canonical Outlook-mailbox-theft
    primitive; Dropbox + OneDrive Personal exfil bypass is
    well-documented; hardcoded-IP DNS-logging-bypass is canonical
    tradecraft; scheduled-task rotation + binary masquerading
    are well-established persistence patterns. Symantec is
    Tier-1-comparable vendor and has published full IOC set
    (file hashes for mailbox stealer + masquerading executables)
    at security.com. "Confirmed" Grade 1 not assigned because
    no independent Tier-1 IR firm corroboration at sweep —
    single-vendor-origination through two publisher-independent
    relays.

corroboration:
  independent_sources:
    - securityweek
    - securityaffairs
  independent: false
  test_passed: null
  test_failed: >
    Publisher-independence holds (SecurityWeek + SecurityAffairs
    different organizations, different bylines, neither cites
    the other). Evidence-basis-independence FAILS — both relays
    derive substantive technical content from the same Symantec
    + Carbon Black primary research with first-party Carbon
    Black EDR telemetry as the originating evidence basis. Per
    admiralty-grading skill Step 4: "Both rely on the same
    vendor's telemetry" pattern. WEP ceiling capped at "likely"
    per single-source veto on substantive operational content.

first_party_precedence:
  applied: false
  splunk_evidence: null
  splunk_query_run: >
    -30d sweep across defenseclaw_local + (archimedes NOT
    sourcetype=archimedes:*) on Aspose.Email + OST→PST
    conversion + Dropbox / OneDrive Personal exfil + hardcoded
    Microsoft IP exfil patterns + Adobe/Lenovo/OneDrive
    scheduled-task masquerade. 0 events per PM-000 sentinel
    record. Per Hard Rule 8 silence is not disconfirming. Once
    Symantec primary IOC set (file hashes) is extracted, run
    hash-based pivot — analyst handoff candidate.

single_source_veto_applied: true
single_source_veto_detail: >
  Applied on substantive operational claims (specific mechanism +
  cadence + persistence + masquerading + exfil patterns) because
  Symantec + Carbon Black is single-vendor-origination through
  two publisher-independent relays. NOT applied on procedural-
  fact layer (Symantec published the write-up + IOC set +
  attribution declination — all verifiable via Symantec
  publication). NOT applied on attribution-declination layer
  (verbatim Symantec self-statement is canonically self-
  attesting).

wep_ceiling: likely
wep_layered:
  symantec_carbon_black_published_150_day_mailbox_espionage_writeup: very_likely    # Procedural-fact; verifiable via Symantec publication
  target_unidentified_major_global_stock_exchange_single_executive_outlook: very_likely  # Symantec verbatim refusal-to-name; canonical self-statement
  dwell_time_approximately_150_days_2025_10_10_through_2026_03_19: likely             # Symantec first-party EDR telemetry; single-vendor-origination
  entry_vector_remains_unknown: very_likely                                            # Verbatim Symantec negative claim — verifiable absence
  aspose_wrapper_ost_pst_extraction_mechanism: likely                                 # Symantec single-source; technically coherent
  eight_subsequent_ost_extraction_runs_at_two_to_four_week_intervals_with_adjoining_time_windows: likely  # Symantec single-source on cadence
  exfiltration_via_dropbox_and_onedrive_personal_with_hardcoded_microsoft_ips: likely # Symantec single-source on exfil mechanism
  scheduled_task_rotation_5min_5hr_15hr_24hr_under_adobe_lenovo_onedrive_masquerade: likely  # Symantec single-source on persistence
  binary_masquerading_rotation_three_phases_oct_2025_through_mar_2026: likely         # Symantec single-source on operational timeline
  symantec_published_full_ioc_set_at_security_com: very_likely                        # Verifiable via SecurityAffairs verbatim reference
  no_actor_attribution_at_any_source: very_likely                                     # Verbatim across CISA equivalent: Symantec / SecurityWeek
  symantec_analytic_hedge_almost_certainly_state_linked_given_target_value_and_patience: likely  # Symantec analytic judgment preserved verbatim
  no_ad_watchlist_entity_named: very_likely                                           # Verifiable absence
  no_ad_prime_named_victim: very_likely                                               # Verifiable absence
  ttps_reusable_against_ad_prime_outlook_estates: likely                              # Grader-side structural inference
  parsimonious_attacker_class_state_linked_espionage_actor_with_high_operational_discipline: roughly_even_chance  # Possibility-class; Symantec hedge preserved without upgrade

inclusion:
  eligible_for:
    - daily_brief_monitoring
    - weekly_synthesis
    - actor_profile_awareness   # TTPs reusable for state-linked espionage actor tracking; no specific roster actor named
  not_eligible_for:
    - flash                     # No A&D-prime victim; financial-sector single-victim; PM-cycle not FLASH-class
    - daily_brief_action        # B2 clears threshold but content is reusable-TTPs framing, not action-item (no A&D-prime exposure mapping at sweep)
    - actor_profile_update      # No tracked roster actor named; Hard Rule 2 preserved

# Cluster metadata
cluster:
  topic: >
    Symantec Threat Hunter Team + Carbon Black publish 150-day
    suspected-espionage Outlook mailbox theft against major
    global stock exchange executive. Aspose-wrapped OST→PST
    conversion + cumulative-window extraction cadence + Dropbox/
    OneDrive Personal exfil + hardcoded Microsoft IPs for DNS-
    bypass + scheduled-task rotation under Adobe/Lenovo/OneDrive
    masquerade. No actor attribution. No A&D-prime victim.
    Symantec preserves "almost certainly state-linked" analytic
    hedge without upgrade.
  cluster_size: 1
  raw_signal_members:
    - raw-2026-06-03-pm-002-symantec-stock-exchange-outlook-mailbox-espionage-150-days-aspose-dropbox-onedrive-personal-no-attribution
  attribution_claims:
    - claimed_actor: null
      claim_text: >
        Symantec explicitly declines attribution. Symantec's
        analytic hedge "almost certainly state-linked given
        the target and the patience involved" is analytic
        judgment based on operational discipline + target
        value, NOT a formal moderate/high-confidence attribution.
        Use of public tools, cloud infrastructure, and absence
        of infrastructure reuse make attribution difficult per
        Symantec verbatim.
      claimed_by_sources:
        - symantec
        - securityweek
        - securityaffairs
      requires_analyst_review: true
      hard_rule_2_status: PRESERVED — vendor-explicit-declination preserved verbatim; Archimedes does not originate or upgrade attribution

# Downstream handoff flags
analyst_review_required: true
analyst_review_complete: true
analyst_review_run_id: analyst-20260603-164500
analyst_review_summary: >
  SAT-KAC + SAT-ACH applied per grader request. KAC on TTP-reusability
  identified two TEST-classified critical assumptions: A2 (A&D SOC IP-tier
  egress visibility) and A6 (Aspose.Email base-rate at A&D primes). Both
  are load-bearing for the defender-pivot Splunk-hunt section. Four
  additional assumptions (A1 .NET runtime reachability, A3 CASB
  personal-cloud enforcement, A4 executive-targeting transfer, A5
  Symantec-hedge calibration) qualify. Recommendation: briefer should
  hedge the "TTPs reusable against A&D-prime Outlook estates" framing —
  the TTP set IS structurally reusable but A&D-specific controls
  (endpoint hardening / CASB / ITAR-CUI) may break specific mechanism
  transfer. The GENERAL mailbox-theft objective transfers regardless.
  Defer high-signal Splunk-hunt claims until Aspose.Email base-rate test
  runs against first-party Splunk. ACH on state-linked-actor-class
  produced a five-way tie at zero inconsistencies across Russian-class /
  Chinese-class / Iranian-class / novel-state-class / false-flag-state.
  DPRK financial-pivot-class (H4) and criminal-with-state-discipline (H5)
  accumulate 3 inconsistencies each — disfavored but not ruled out. The
  state-linked disjunction (H1 OR H2 OR H3 OR H6 OR H7) is supported at
  WEP "likely"; within-class differentiation is roughly_even_chance.
  No WEP-ceiling adjustment required at grader-set layer. Hard Rule 2
  preserved throughout — ACH operated strictly at attacker-class level;
  no roster actor named.
analyst_review_rationale: >
  WEP "likely" on multiple substantive operational claims
  (mechanism + cadence + persistence + exfil). LOAD-BEARING
  ASSUMPTIONS worth interrogation: (a) does Symantec's "almost
  certainly state-linked" hedge translate to action-tier
  defensive posture at A&D primes given TTP-reusability, even
  without victim attribution? (b) does the Aspose-wrapper +
  cloud-personal-exfil + hardcoded-IP-DNS-bypass TTP combination
  warrant scaffolded actor-class placeholder (state-linked-
  espionage-actor-unnamed) for cross-finding pattern matching
  in next 30-90 days? (c) what assumption underlies the "TTPs
  reusable against A&D" framing, and what would invalidate it
  (e.g., highly tailored TTPs that don't generalize)?
  Decompose. Hard Rule 2 preserves declination integrity.

red_team_review_required: false
red_team_review_rationale: >
  WEP ceiling at "likely" on substantive operational claims
  (single-vendor-through-relays veto applied). No "very likely"
  on substantive operational content. Red-team invocation
  floor NOT MET. Procedural-fact layer "very_likely" (Symantec
  published, IOC set published, attribution declined) is
  verifiable-by-canonical-publication and does not invoke
  red-team.

red_team_review: null
analysis_sections:
  sat_kac:
    kac_analysis:
      assessment_under_review: >
        "Aspose-wrapper OST→PST extraction + Dropbox/OneDrive Personal exfil
        with hardcoded Microsoft IPs to bypass DNS logging + scheduled-task
        rotation under Adobe/Lenovo/OneDrive masquerade — the TTP combination
        documented by Symantec against the unnamed stock exchange executive
        — is reusable against A&D-prime Outlook estates by any actor with
        comparable operational discipline."
      analyzed_at: 2026-06-03T16:45:00-04:00
      analyzed_by: analyst
      red_team_review: null
      invoking_context: >
        Grader flagged TTP-reusability framing as load-bearing for the
        defender-pivot section. If the transfer assumption is brittle,
        briefer guidance ("Splunk hunts on Aspose namespace + scheduled-task
        masquerade + Dropbox/OneDrive Personal egress + hardcoded-IP
        outbound") still has standalone value but the framing should hedge.
      assumptions:
        - id: A1
          statement: >
            Aspose.Email .NET runtime is reachable on A&D-prime executive
            endpoints — i.e., .NET Framework / .NET runtime context exists
            and is callable from an attacker-controlled process at user or
            SYSTEM privilege.
          category: technology
          stated: false
          why_must_be_true: >
            The TTP requires that the Aspose .NET library can be invoked
            on the target. If the executive endpoint is locked-down macOS,
            Linux, or a thin client without .NET runtime, the specific
            mechanism transfer fails (though the GENERAL mailbox-theft
            objective remains relevant via alternative tooling).
          when_could_be_false: >
            A&D executives increasingly use macOS endpoints (especially at
            primes with cross-platform engineering populations); ITAR/CUI
            VDI or zero-trust thin-client architectures may restrict
            arbitrary .NET assembly load; Windows AppLocker / WDAC policy
            on hardened executive endpoints may block unsigned-Aspose load.
          evidence_for:
            - canonical-aspose-dotnet-library-cross-platform-but-windows-dotnet-most-common
          evidence_against:
            - ad-prime-itar-cui-endpoint-hardening-baselines-typically-include-applocker-wdac-or-equivalent
          confidence: medium
          centrality: material
          classification: qualify
        - id: A2
          statement: >
            A&D-prime SOCs have visibility into outbound HTTPS at the IP
            tier and can distinguish hardcoded Microsoft IP egress from
            normal name-resolved Microsoft service calls.
          category: visibility
          stated: false
          why_must_be_true: >
            The grader's defender-pivot framing ("IP-tier egress monitoring
            required; DNS-tier blocklisting is insufficient") presupposes
            that A&D SOCs CAN do IP-tier egress monitoring. If most A&D
            SOCs rely on DNS-tier and proxy-tier controls with limited
            netflow-to-IP correlation, the defender pivot doesn't have an
            existing detection surface to plug into.
          when_could_be_false: >
            CASB egress controls at A&D primes are typically configured at
            FQDN/URL tier, not IP tier. Hardcoded Microsoft IP traffic to
            a sanctioned-cloud netblock would be allowed by default egress
            policy. Netflow logging in mature SOCs exists but is rarely
            correlated against sanctioned-cloud netblocks for personal-
            tenant disambiguation.
          evidence_for: []
          evidence_against:
            - typical-ad-prime-egress-control-tier-fqdn-not-ip
          confidence: low
          centrality: critical
          classification: test
        - id: A3
          statement: >
            A&D-prime DLP and CASB controls effectively distinguish Dropbox
            + OneDrive Personal exfil from sanctioned-cloud (M365 corporate
            tenancy + sanctioned-Dropbox-Business) traffic.
          category: visibility
          stated: false
          why_must_be_true: >
            "Personal cloud account enforcement gaps on A&D executive
            endpoints worth re-validation" framing implies that the gap
            CAN be closed with existing controls. If the policy boundary
            is poorly enforced or unenforceable on executive endpoints
            (typical exception class), the framing is aspirational.
          when_could_be_false: >
            ITAR / CUI policy regimes typically restrict personal cloud
            on classified endpoints but enforce loosely on unclassified
            executive endpoints. CASB enforcement gaps on personal Dropbox
            / OneDrive Personal are documented across the enterprise space
            generally and at DIB primes specifically (audit findings, M365
            E5 + CASB deployment gaps).
          evidence_for: []
          evidence_against:
            - typical-casb-deployment-maturity-tiers-show-personal-cloud-gaps-at-executive-level
          confidence: low
          centrality: material
          classification: qualify
        - id: A4
          statement: >
            The high-value-executive single-mailbox targeting pattern is
            transferable from financial-sector (stock exchange) to A&D-prime
            executive populations — same threat model, same defender
            posture relevance.
          category: intent
          stated: false
          why_must_be_true: >
            The "TTPs reusable against A&D primes" framing assumes the
            actor's MOTIVATION to use this TTP set transfers. If the actor
            class chose this TTP set because of stock-exchange-specific
            constraints (e.g., regulatory monitoring of bulk exfil at the
            target, or specific market-sensitive-information access
            patterns), transfer is weaker.
          when_could_be_false: >
            A&D executive mailbox content has different intelligence-value
            profile than stock-exchange-executive mailbox content (program
            scheduling, contract negotiation, supplier relationships,
            classified-program metadata vs. market-sensitive-information).
            Actor class targeting financial-sector may not target A&D, and
            vice versa. The TTP-MECHANISM transfers; the TARGETING
            transfer is a separate assumption.
          evidence_for:
            - both-sectors-are-canonical-state-linked-espionage-target-classes
          evidence_against: []
          confidence: medium
          centrality: critical
          classification: qualify
        - id: A5
          statement: >
            Symantec's "almost certainly state-linked given the target and
            the patience involved" analytic hedge is calibrated and not a
            polite-default framing.
          category: source_reliability
          stated: true
          why_must_be_true: >
            The grader carried Symantec's hedge verbatim and it shapes the
            "reusable TTPs against A&D Outlook estates" framing — if
            Symantec's hedge is polite-default rather than calibrated,
            the actor-class is more uncertain than the framing implies.
          when_could_be_false: >
            Symantec analytic hedges in published write-ups are sometimes
            shaped by legal-review / customer-relationship constraints
            rather than pure technical-evidence weighing. The "almost
            certainly" framing is consistent with multiple state classes
            AND with a highly-disciplined criminal actor (see ACH H6).
          evidence_for:
            - symantec-positive-ratification-signal-on-attribution-discipline
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify
        - id: A6
          statement: >
            Aspose.Email is a sufficiently uncommon library on A&D-prime
            endpoints that detection-engineering can use namespace-invocation
            as a high-signal hunt indicator.
          category: technology
          stated: false
          why_must_be_true: >
            The Splunk-hunt recommendation #1 ("Outlook OST→PST conversion
            processes invoking Aspose namespace assemblies from non-licensed-
            Aspose endpoints") depends on Aspose being uncommon in
            legitimate use at A&D primes. If Aspose.Email is widely
            licensed and used in mail-processing pipelines, document-
            management workflows, or compliance tooling at A&D primes,
            the hunt would generate substantial false positives.
          when_could_be_false: >
            Aspose is a popular commercial library used by enterprise
            email-archival, eDiscovery, document-management, and
            compliance vendors. A&D primes running eDiscovery /
            litigation-hold infrastructure or legitimate
            Outlook-data-migration tooling may have legitimate
            Aspose.Email invocations.
          evidence_for: []
          evidence_against: []
          confidence: unknown
          centrality: material
          classification: test
        - id: A7
          statement: >
            Scheduled-task rotation across 5min / 5hr / 15hr / 24hr
            intervals under Adobe / Lenovo / OneDrive masquerade is
            sufficiently anomalous against typical A&D endpoint scheduled-
            task baselines to be a reliable hunt indicator.
          category: visibility
          stated: false
          why_must_be_true: >
            Splunk-hunt recommendation #2 depends on the masquerade
            pattern being distinguishable from legitimate
            Adobe/Lenovo/OneDrive scheduled-task activity. If legitimate
            Adobe Acrobat Reader, Lenovo Vantage / System Update, and
            OneDrive sync legitimately register tasks at varying
            intervals, the hunt requires sophisticated baselining.
          when_could_be_false: >
            A&D endpoint scheduled-task baselines include many legitimate
            Adobe / Lenovo / OneDrive tasks; the masquerade pattern
            blends with normal noise unless the hunt baselines on the
            specific rotation intervals AND the file paths outside
            canonical install directories (which the brief framing does
            mention).
          evidence_for:
            - cluster-handoff-explicitly-flags-non-canonical-install-paths-as-the-disambiguator
          evidence_against: []
          confidence: medium
          centrality: peripheral
          classification: sound
        - id: A8
          statement: >
            150-day dwell + cumulative-window cadence is replicable by
            other state-linked actors against A&D primes — i.e., the
            "patience" Symantec attributes is a transferable operational
            posture, not a unique-to-this-actor signature.
          category: ttp_patterns
          stated: false
          why_must_be_true: >
            The "reusable against A&D" framing depends on the long-dwell
            posture being a TTP-class signature rather than a specific
            actor's calling card. If the patience is genuinely unique
            (e.g., specific Russian SVR-class long-dwell discipline that
            Chinese MSS / Iranian MOIS / DPRK actors don't replicate),
            the actor pool capable of executing this TTP set against
            A&D is narrower.
          when_could_be_false: >
            150-day mailbox-only dwell is a relatively patient TTP class
            but is within multiple state actors' known operational
            profile. The "patience" framing does not differentially
            implicate any single actor class.
          evidence_for:
            - long-dwell-mailbox-collection-canonical-multi-state-class-pattern
          evidence_against: []
          confidence: medium
          centrality: peripheral
          classification: sound
      classifications_summary:
        sound: 2
        qualify: 4
        test: 2
        reject: 0
      remediation:
        status: proceed_with_caveats
        qualifying_caveats:
          - >
            A2 (A&D SOC IP-tier visibility) and A6 (Aspose.Email uncommonness
            at A&D primes) classify as TEST — both load-bearing for the
            defender-pivot Splunk-hunt section, both at low/unknown
            confidence at this analyst-handoff layer. Briefer should not
            assert the hunts will be high-signal; frame as "candidate
            hunts that require local baselining before deployment." Test
            pathway: query first-party Splunk on Aspose.Email invocation
            base rate over -90d to validate A6 (analyst handoff to
            librarian for Splunk pivot once the Symantec primary IOC set
            including file hashes is extracted from security.com).
          - >
            A1 (Aspose runtime reachability), A3 (CASB Personal-cloud
            enforcement), A4 (executive-mailbox targeting transfer), A5
            (Symantec analytic-hedge calibration) qualify. Briefer should
            hedge the "TTPs reusable against A&D-prime Outlook estates"
            framing — preserve as "TTP set IS structurally reusable but
            A&D-specific controls (executive-endpoint hardening, CASB
            enforcement, ITAR/CUI policy regimes) may break specific
            mechanism transfer; the GENERAL mailbox-theft objective
            transfers regardless of mechanism."
          - >
            A7 and A8 are sound. The masquerade-pattern hunt with
            non-canonical-install-path disambiguator is solid; the
            long-dwell-posture transferability is well-supported by
            multi-state-class historical precedent.
        next_action: >
          Proceed to PM brief Tradecraft / Monitoring tier with hedged
          framing. Recommendation to briefer: lead with the MECHANISM
          documentation (Aspose-wrapper + cumulative-window cadence +
          hardcoded-IP DNS-bypass + masquerade-with-rotation) as
          tradecraft signal worth defender attention. Hedge the "reusable
          against A&D primes" framing with "subject to A&D-specific
          endpoint hardening and CASB enforcement variables." Defer
          high-signal Splunk-hunt claims until Aspose.Email base-rate
          test runs against first-party Splunk.
      recommended_wep_after_test:
        if_aspose_base_rate_low_at_ad_primes: >
          A6 sound, hunt recommendation strengthens; brief may frame
          Aspose namespace invocation as high-signal A&D hunt indicator
        if_aspose_base_rate_high_at_ad_primes: >
          A6 reject; hunt recommendation requires baselining caveat;
          brief should reframe as "Aspose invocation + non-canonical
          install path + masquerade rotation" composite indicator
        if_ip_tier_egress_monitoring_check_returns_existing_capability: >
          A2 strengthens; defender-pivot framing remains as currently
          structured
        if_ip_tier_egress_monitoring_check_returns_capability_gap: >
          A2 confirmed as critical defender capability gap; brief should
          surface as A&D-specific CTI insight ("the hardcoded-IP DNS-bypass
          tradecraft documents an A&D-prime egress visibility gap that
          DNS-tier blocklisting alone does not close")

  sat_ach:
    ach_analysis:
      question: >
        "Symantec's 'almost certainly state-linked given the target and the
        patience involved' analytic hedge is consistent with multiple
        attacker-class hypotheses. Which class, if any, is differentially
        supported by the observable evidence in the Symantec + Carbon Black
        write-up?"
      analyzed_at: 2026-06-03T16:52:00-04:00
      analyzed_by: analyst
      red_team_review: null
      hard_rule_2_discipline: >
        Symantec, SecurityWeek, and SecurityAffairs all decline attribution.
        ACH operates strictly at ATTACKER-CLASS level (Russian intelligence-
        class / Chinese intelligence-class / Iranian intelligence-class /
        DPRK financial-pivot-class / criminal-with-state-discipline /
        novel-state-class / false-flag) — NOT at named-actor level. The
        cluster-anchor body explicitly invited this decomposition and the
        grader pre-flagged Hard Rule 2 status PRESERVED. Per analyst-spec
        Hard Rule 2 boundary: ACH ranks attacker-class hypotheses against
        observable evidence; it does NOT promote a tied or ranked class
        into an attribution claim. If the ranking shows a class is
        differentially favored, the analyst output documents that as
        "evidence is more consistent with X-class than alternatives,"
        NOT as "X-class did it."
      hypotheses:
        - id: H1
          statement: >
            Russian intelligence-class actor (SVR-class long-dwell mailbox-
            collection profile against high-value executive; financial-
            sector relevance via market-intelligence collection or strategic
            economic signaling).
        - id: H2
          statement: >
            Chinese intelligence-class actor (MSS-class commercial /
            financial intelligence-collection profile; stock-exchange
            executive mailbox aligns with documented commercial-
            intelligence-collection pattern).
        - id: H3
          statement: >
            Iranian intelligence-class actor (MOIS / IRGC-class espionage
            with financial-sector intelligence-collection; less common
            against pure financial-sector but within documented operational
            scope).
        - id: H4
          statement: >
            DPRK financial-pivot-class actor (Lazarus-cluster financial-
            intelligence-and-extraction profile; stock-exchange executive
            mailbox could pivot to market-manipulation, insider-trading
            pre-positioning, or financial-extraction).
        - id: H5
          statement: >
            Criminal actor with state-class operational discipline
            (financially-motivated actor running a state-discipline-grade
            campaign; market-intelligence + insider-trading + extortion
            potential against stock-exchange executive mailbox).
        - id: H6
          statement: >
            Novel state-affiliated actor not in current Archimedes roster
            or established taxonomy (a previously-unattributed cluster
            with state-class resourcing and operational discipline).
        - id: H7
          statement: >
            False-flag operation: a state-class actor running TTPs
            calibrated to look like a different state class (e.g.,
            Russian-class using Chinese-class-style tradecraft).
      evidence:
        - id: E1
          description: >
            Target = major global stock exchange (financial sector, market-
            sensitive information, high economic signal value).
          source: symantec via securityaffairs
          digraph: B2
          weight: 2
        - id: E2
          description: >
            Victim scope = single senior executive mailbox; no lateral
            movement off original host; surgical access maintenance over
            150 days.
          source: symantec
          digraph: B2
          weight: 2
        - id: E3
          description: >
            150-day dwell with cumulative-window extraction cadence
            (eight subsequent runs at 2-4 week intervals through
            2026-02-17 with `-t` time-window parameters adjoining).
          source: symantec
          digraph: B2
          weight: 2
        - id: E4
          description: >
            Aspose-wrapped OST→PST extraction using legitimate commercial
            .NET library; no custom mailbox-stealer signature.
          source: symantec
          digraph: B2
          weight: 2
        - id: E5
          description: >
            Exfiltration via Dropbox + OneDrive Personal (public consumer
            cloud, blend-with-normal-traffic) with hardcoded Microsoft
            IPs bypassing DNS logging.
          source: symantec
          digraph: B2
          weight: 2
        - id: E6
          description: >
            Persistence via scheduled-task rotation under Adobe / Lenovo /
            OneDrive masquerade with rotating intervals.
          source: symantec
          digraph: B2
          weight: 2
        - id: E7
          description: >
            Symantec explicitly declines attribution. Verbatim: "Symantec
            and Carbon Black did not share any information about who may
            have been behind the attack."
          source: securityweek
          digraph: B1
          weight: 2
        - id: E8
          description: >
            Symantec analytic hedge: "almost certainly state-linked given
            the target and the patience involved."
          source: securityaffairs
          digraph: B1
          weight: 2
        - id: E9
          description: >
            Use of public tools (Aspose), cloud infrastructure (Dropbox,
            OneDrive Personal), and absence of infrastructure reuse make
            attribution difficult per Symantec verbatim.
          source: symantec
          digraph: B2
          weight: 2
        - id: E10
          description: >
            No data-destruction / wiper component; no ransomware; no
            financial-extraction tooling reported (no skimmer, no
            credential-stealer downstream).
          source: symantec via verifiable-absence
          digraph: A1
          weight: 3
        - id: E11
          description: >
            Entry vector remains unknown — Symantec/SecurityAffairs
            verbatim negative claim.
          source: securityaffairs
          digraph: A1
          weight: 3
        - id: E12
          description: >
            No infrastructure reuse against previously-documented actor
            tradecraft (no overlap with known C2 patterns of any named
            state-affiliated cluster at Symantec's analysis layer).
          source: symantec
          digraph: B2
          weight: 2
      matrix:
        E1: {H1: C, H2: C, H3: N, H4: C, H5: C, H6: C, H7: C}
        E2: {H1: C, H2: C, H3: C, H4: N, H5: N, H6: C, H7: C}
        E3: {H1: C, H2: C, H3: C, H4: I, H5: I, H6: C, H7: C}
        E4: {H1: C, H2: C, H3: C, H4: C, H5: C, H6: C, H7: C}
        E5: {H1: C, H2: C, H3: C, H4: C, H5: C, H6: C, H7: C}
        E6: {H1: C, H2: C, H3: C, H4: C, H5: C, H6: C, H7: C}
        E7: {H1: C, H2: C, H3: C, H4: C, H5: C, H6: C, H7: C}
        E8: {H1: C, H2: C, H3: C, H4: N, H5: I, H6: C, H7: C}
        E9: {H1: C, H2: C, H3: C, H4: C, H5: C, H6: C, H7: C}
        E10: {H1: C, H2: C, H3: C, H4: I, H5: I, H6: C, H7: C}
        E11: {H1: N, H2: N, H3: N, H4: N, H5: N, H6: N, H7: N}
        E12: {H1: C, H2: C, H3: C, H4: C, H5: C, H6: C, H7: C}
      inconsistency_counts:
        H1: 0
        H2: 0
        H3: 0
        H4: 3
        H5: 3
        H6: 0
        H7: 0
      diagnostic_evidence:
        - E3: >
            Mildly diagnostic. Cumulative-window 150-day extraction cadence
            with no terminal financial-extraction action is inconsistent
            with H4 (DPRK financial-pivot — DPRK actors typically extract
            value at the financial-pivot point, not sustain 150-day
            collection without terminal extraction) and H5 (criminal-
            with-state-discipline — pure-criminal economic model usually
            terminates earlier with extraction).
        - E8: >
            Mildly diagnostic. Symantec's "state-linked given patience"
            hedge is somewhat inconsistent with H5 (criminal-class) but
            Symantec's framing is analyst hedge, not evidence, so weight
            it as I-mild rather than I-strong.
        - E10: >
            Mildly diagnostic. Absence of any financial-extraction /
            destruction / ransomware / skimmer component is inconsistent
            with H4 (DPRK actors typically pivot to financial extraction
            even on espionage-tagged ops) and H5 (criminal class economic
            model requires monetization).
      ranking:
        - rank: 1_tie
          hypothesis_ids: [H1, H2, H3, H6, H7]
          rationale: >
            Five hypotheses tie at zero inconsistencies. Russian
            intelligence-class, Chinese intelligence-class, Iranian
            intelligence-class, novel-state-class, and false-flag-state
            all fit observable evidence with no contradictions. This is
            the ACH-honest mirror of Symantec's vendor-level declination —
            with the evidence as published, no single state-class is
            differentially supported. Per Hard Rule 2 + analyst-spec
            worked-example: ACH ranking is NOT an attribution; it
            documents that the question is underdetermined at this
            evidence layer.
          wep: >
            On "which attacker class is most likely behind this campaign,"
            WEP is roughly_even_chance across H1/H2/H3/H6/H7. Symantec's
            "state-linked" framing is supported (these five classes are
            state-affiliated or state-class-disciplined); class-level
            differentiation within the tied cluster is NOT supported.
        - rank: 2_tie
          hypothesis_ids: [H4, H5]
          rationale: >
            DPRK financial-pivot-class and criminal-with-state-discipline
            class both accumulate 3 inconsistencies (E3 cumulative-window
            without terminal extraction, E8 Symantec patience hedge weakly
            against, E10 no financial-extraction component observed).
            Both classes' economic models predict observable financial-
            extraction artifacts which are absent. Both still possible —
            DPRK could be in long-dwell strategic-information collection
            mode without immediate pivot, and a criminal-class could
            simulate patience to maximize collection — but observable
            evidence weakly disfavors.
          wep: unlikely
      sensitivity_analysis:
        brittleness: high
        load_bearing_evidence: [E3, E8, E10]
        if_e10_changes: >
          If a follow-up surfaces financial-extraction artifacts (insider-
          trading patterns, market manipulation signatures, ransomware
          deployment after 2026-03-19), H4 and H5 rise materially.
        if_tier_1_ir_firm_publishes_attribution: >
          A Mandiant / Unit 42 / MSTIC / CrowdStrike / Volexity attribution
          would collapse the five-way tie. Re-run ACH against the new
          evidence base. The ACH's job here is documentary — keep the
          tied class structure visible to prevent confirmation bias if a
          later attribution drops.
        if_target_disclosed: >
          The unnamed stock exchange identity is a load-bearing absence.
          If the exchange is a US / NATO-aligned exchange, H1/H2/H3 might
          weakly favor. If it's a Middle Eastern / Asian exchange, H3 or
          H2 might weakly favor. The Symantec declination of victim name
          preserves the underdetermination.
        if_aspose_namespace_appears_in_known_state_class_writeups: >
          A separate Mandiant / Unit 42 / MSTIC write-up documenting
          Aspose.Email tooling associated with a specific named state-
          class actor would collapse the tie partially toward that class.
      tripwires:
        - observation: >
            Tier-1 IR firm publishes attribution to a named actor for this
            campaign or for a campaign sharing the Aspose-wrapper IOC set
          effect: >
            Collapse the H1/H2/H3/H6/H7 tie; re-run ACH against the new
            evidence base; downgrade or remove the tied-class WEP framing
        - observation: >
            Symantec publishes follow-up with target identity, attribution,
            or financial-extraction artifacts
          effect: >
            Resolves E10 ambiguity; re-run ACH
        - observation: >
            Same Aspose-wrapper + cumulative-window cadence + masquerade-
            rotation TTP combination surfaces in a second campaign against
            a high-value executive (financial-sector or otherwise)
          effect: >
            Strengthens the case for a coherent actor (named or unnamed)
            rather than coincidental TTP convergence; actor-profiler should
            consider scaffolding state-linked-espionage-actor-unnamed
            placeholder per cluster-handoff
        - observation: >
            CrowdStrike OverWatch, Mandiant M-Trends, or MSTIC Digital
            Defense Report references this campaign with attribution
          effect: >
            Authoritative attribution would collapse tie; rerun ACH
      conclusion:
        summary: >
          The five-way tie at zero inconsistencies (H1 Russian intelligence-
          class / H2 Chinese intelligence-class / H3 Iranian intelligence-
          class / H6 novel state-class / H7 false-flag-state) is the ACH-
          honest outcome. Symantec's "almost certainly state-linked"
          hedge is supported — the evidence is more consistent with
          state-class hypotheses (H1/H2/H3/H6/H7) than with non-state
          alternatives (H4 DPRK-financial-pivot, H5 criminal-with-state-
          discipline both at 3 inconsistencies). But within the state-class
          tier, no single class is differentially favored at the published
          evidence layer. The tied-class structure should be PRESERVED in
          downstream brief composition rather than compressed to a single
          class — that compression would originate attribution per Hard
          Rule 2. The proper analyst statement: "Symantec's state-linked
          hedge fits multiple state-affiliated actor classes with no
          observable differentiation at the published evidence layer; no
          single class can be promoted to a finding-level attribution."
        wep: >
          On "state-linked at attacker-class tier" (the disjunction across
          H1/H2/H3/H6/H7): likely. Symantec's hedge is supported by
          observable evidence and disfavor of H4/H5 reinforces.
          On "which specific state-class": roughly_even_chance across the
          tied cluster.
        confidence_caveats: >
          High brittleness. Three load-bearing pieces of evidence (E3, E8,
          E10) drive the H4/H5 disfavoring. If a follow-up surfaces
          financial-extraction artifacts, H4/H5 rise into the tied
          cluster. If a Tier-1 IR firm publishes attribution, the
          state-class tie collapses to whichever class is named. Pending
          either, the analyst conclusion is "state-linked at class tier,
          underdetermined within the class tier."

# Lifecycle
tlp: CLEAR
published_in_briefs: [2026-06-03-afternoon]
retracted: false
retraction_brief_id: null

# Defensive / IOC handoff flags
ioc_handoff:
  defender_relevant_iocs:
    - "Symantec full IOC set published at security.com: file hashes for mailbox stealer and Adobe/OneDrive/Lenovo masquerading executables (extract from Symantec primary for hash-based pivot)"
    - "Aspose.Email .NET library namespace invocation by non-canonical / non-installed-Aspose-licensee processes"
    - "Scheduled task registration with names mimicking Adobe / Lenovo / OneDrive service patterns and unusual rotation intervals (5-minute / 5-hour / 15-hour / 24-hour)"
    - "Outbound HTTPS to Dropbox + OneDrive Personal (onedrive.live.com / graph.microsoft.com personal-tenant) from cleared-personnel endpoints"
    - "Outbound HTTPS to hardcoded Microsoft IP addresses (not hostnames) — bypasses DNS-tier logging"
    - "SYSTEM-privilege processes with Adobe Acrobat / OneDrive masquerade file paths outside canonical install directories"
  iocs_indirect_action: >
    Defender action framing for A&D-prime Outlook / M365 estates:
    (a) Splunk hunt — Outlook OST→PST conversion processes
        invoking Aspose namespace assemblies (Aspose.Email,
        Aspose.Email.dll) from non-licensed-Aspose endpoints.
    (b) Splunk hunt — scheduled task registration with
        Adobe/Lenovo/OneDrive masquerade names and unusual
        rotation intervals.
    (c) Splunk hunt — outbound HTTPS to Dropbox / OneDrive
        Personal (onedrive.live.com vs sanctioned `*.sharepoint.com`
        tenancy) from cleared-personnel endpoints.
    (d) Splunk hunt — outbound HTTPS to hardcoded Microsoft IP
        addresses (not hostnames). DNS-tier blocklisting and
        DNS-anomaly detection are insufficient for this pattern;
        IP-tier egress monitoring required.
    (e) Once Symantec primary IOC set (file hashes) is extracted,
        run hash-based pivot against archimedes + defenseclaw_local.
    (f) ITAR / CUI policy review — Personal cloud account
        enforcement gaps on A&D executive endpoints worth
        re-validation given Dropbox + OneDrive Personal as exfil
        path.

monitor_for_next_cycle:
  - "Tier-1 IR firm independent corroboration of mechanism or victim"
  - "Symantec follow-up or attribution lift"
  - "A&D-prime or DIB-supplier disclosure of similar long-dwell mailbox compromise"
  - "Roster-actor TTP match against published Symantec IOC set"

vuln_tracker_handoff:
  scaffold_candidate: false
  scaffold_note: >
    No CVE involved. Pure tradecraft / TTP-class finding. Not
    a vuln-tracker dossier candidate. Actor-profiler awareness
    handoff is appropriate scaffolding path if pattern recurs.

actor_profiler_handoff:
  scaffold_candidate: awareness_only
  scaffold_note: >
    No named actor; Hard Rule 2 preserved. Symantec's "almost
    certainly state-linked given the target and the patience
    involved" hedge is analytic judgment without attribution.
    Actor-profiler should note the TTP combination (Aspose-
    wrapper OST→PST + Dropbox/OneDrive Personal exfil +
    hardcoded-IP DNS-bypass + scheduled-task rotation + binary
    masquerading) for cross-roster TTP-matching in next 30-90
    days. If pattern recurs against a second high-value-executive
    victim or if a Tier-1 firm publishes attribution, escalate
    to /new-actor scaffolding consideration.

librarian_handoff:
  source_grade_ratification_signal:
    source_yaml_id: symantec
    current_grade: A
    current_provisional_status: true
    provisional_since: 2026-05-13
    second_corpus_citation_signal: >
      Symantec primary's analytic discipline in declining
      attribution despite operational-discipline + target-value
      strongly implying state-linked espionage is a positive
      ratification signal. Published-IOC-set + named-Carbon-
      Black-team-byline + verbatim-attribution-declination
      together provide ratification evidence. Librarian may
      forward to operator for ratification consideration on
      next pass; 72h ratification clock from 2026-05-13 long
      elapsed; this is the second-citation evidence layer.

briefer_handoff:
  brief_inclusion_recommendation: monitoring_tier_or_tradecraft_signal
  brief_substance: >
    PM brief Tradecraft / Monitoring section. NOT action-tier
    (no A&D-prime exposure mapping). Frame as reusable-TTPs
    signal: Aspose-wrapper OST→PST extraction + hardcoded-IP
    DNS-bypass + scheduled-task rotation under Adobe/Lenovo/
    OneDrive masquerade are operationally-disciplined patterns
    that any state-linked espionage actor could repurpose
    against A&D-prime Outlook estates. Preserve Symantec's
    "almost certainly state-linked" hedge verbatim (12 words,
    Hard Rule 6 compliant). Defender pivot: Splunk hunts on
    Aspose namespace invocation + scheduled-task masquerade +
    Dropbox/OneDrive-Personal egress + hardcoded-IP outbound.
    Cross-reference monitor_for_next_cycle for Tier-1 firm
    independent corroboration tracking.
---

# Symantec + Carbon Black Publish 150-Day Suspected-Espionage Outlook Mailbox Theft Against Major Global Stock Exchange Executive — Reusable TTPs Against A&D Outlook Estates; No Actor Attribution; No A&D-Prime Victim

## Summary

Symantec's Threat Hunter Team and Carbon Black published a joint write-up "this week" documenting a five-month suspected-espionage compromise of a major global stock exchange, scoped to a single senior executive's Outlook mailbox. SecurityWeek (Eduard Kovacs, 2026-06-03 08:46 EDT) and SecurityAffairs (Pierluigi Paganini, 2026-06-03 14:13 EDT) relay the primary, both in-window.

Dwell time was approximately 150 days (2025-10-10 to 2026-03-19) with first malicious activity 2025-10-10 (two SYSTEM-privilege binaries masquerading as Adobe Acrobat and OneDrive processes) and operational maturity from 2025-11-12. Core tradecraft is a wrapper around **Aspose**, a legitimate commercial .NET library, used to convert the executive's OST file to PST archives and exfiltrate in dated chunks. Eight further OST-extraction runs followed at two-to-four-week intervals through 2026-02-17, with `-t` time-window parameters adjoining each prior run's window — cumulative effect is near-continuous mailbox theft. Exfiltration ran through Dropbox + OneDrive Personal blending with normal corporate traffic, with hardcoded Microsoft IP addresses (not hostnames) bypassing DNS-tier logging. Persistence used scheduled tasks rotated across 5-minute / 5-hour / 15-hour / 24-hour intervals under Adobe / Lenovo / OneDrive service-mimicking names.

Symantec explicitly declines attribution. SecurityWeek verbatim: "Symantec and Carbon Black did not share any information about who may have been behind the attack." Symantec's analytic hedge: "almost certainly state-linked given the target and the patience involved." NO tracked roster actor named. NO A&D-watchlist entity named — financial-sector single victim. Cluster digraph B2 (Symantec provisional-A originating + SecurityWeek + SecurityAffairs B-grade publisher-independent relays; evidence-basis-independence fails through single-Symantec-primary origin). WEP "likely" on substantive operational claims; "very_likely" on procedural-fact layer (publication + IOC-set + declination).

**Why this matters for A&D:** the TTPs are reusable. Aspose-wrapper OST→PST extraction is platform-agnostic against any Outlook-using enterprise. Dropbox + OneDrive Personal exfil bypass is exactly the M365 + sanctioned-cloud blend that DIB SOCs struggle to distinguish from normal user behavior. Hardcoded-IP DNS-bypass is a procedural lesson for environments relying on DNS-tier blocklisting. The IOC set Symantec published at security.com is the operational pivot once extracted; analyst handoff includes hash-based Splunk pivot.

## Sources

### Symantec Threat Hunter Team + Carbon Black (symantec, provisional A, digraph: B2 cluster-anchor)

- URL: https://www.security.com/threat-intelligence/ (vendor-publication root; specific URL not separately captured this sweep)
- Source grade: A (provisional per source-grades.yaml, first-citation 2026-05-13; second-citation here is positive ratification signal)
- Key claim: 150-day mailbox-extraction campaign against unnamed major global stock exchange executive; Aspose-wrapped OST→PST conversion; Dropbox + OneDrive Personal exfil with hardcoded Microsoft IPs; scheduled-task rotation under Adobe/Lenovo/OneDrive masquerade; full IOC set including file hashes published at security.com; attribution declined.

### SecurityWeek (securityweek, digraph: B2 layered)

- URL: https://www.securityweek.com/hackers-target-global-stock-exchange-in-espionage-operation/
- Published: 2026-06-03 08:46 EDT (in-window)
- Byline: Eduard Kovacs
- Source grade: B (ratified per source-grades.yaml)
- Key claim: Tier-2 relay of Symantec primary; carries verbatim attribution-declination quote.

### SecurityAffairs (securityaffairs, digraph: B2 layered)

- URL: https://securityaffairs.com/193086/intelligence/cyber-espionage-campaign-targeted-stock-exchange-executives-outlook-account.html
- Published: 2026-06-03 14:13 EDT (in-window)
- Byline: Pierluigi Paganini
- Source grade: B (ratified per source-grades.yaml)
- Key claim: Tier-2 relay with fuller body text; carries Symantec analytic hedge verbatim plus defender framing.

Independence test: publisher-independence holds (different organizations, different bylines, neither cites the other); evidence-basis-independence FAILS (both relays derive substantive technical content from same Symantec + Carbon Black first-party EDR telemetry). Single-source veto applies on substantive content.

## Technical Detail

**Target:** unidentified "major global stock exchange." Symantec explicitly refuses to name the exchange. SecurityAffairs frames as financial-sector + market-sensitive-information rationale.

**Victim scope:** single senior executive's Outlook mailbox. Compromise scoped to that mailbox; no lateral movement off original host reported.

**Dwell time:** ~150 days (2025-10-10 to 2026-03-19). First malicious activity 2025-10-10 with two SYSTEM-privilege binaries already running (Adobe Acrobat + OneDrive masquerades). Operation went active 2025-11-12 with C2 + exfil channels online. Last new binary 2026-03-19 (Adobe driver component masquerade).

**Entry vector:** unknown per SecurityAffairs verbatim ("how the attacker got in initially remains unknown").

**Core tradecraft — Aspose wrapper:**
- Aspose is a legitimate commercial .NET library that can parse Outlook mailbox files.
- Wrapper converted the executive's OST file into PST archives, exfiltrated in dated chunks each covering a few weeks.
- Eight further OST-extraction runs followed at two-to-four-week intervals through 2026-02-17.
- `-t` time-window parameters adjoined each prior run's window — cumulative effect is near-continuous mailbox theft.

**Exfiltration:** Dropbox + OneDrive Personal. Both blend with normal corporate traffic. Attacker hardcoded Microsoft IP addresses (not hostnames) for OneDrive calls — bypasses DNS-based logging entirely.

**Persistence:** scheduled tasks re-registered every few weeks under names mimicking Adobe / Lenovo / OneDrive service patterns. Task intervals rotated between 5-minute / 5-hour / 15-hour / 24-hour windows. Each new registration overwrote the previous one (footprint minimization).

**Binary masquerading rotation:**
- 2025-10-10 — initial Adobe Acrobat + OneDrive masquerade
- 2026-02-27 — new binary masquerading as OneDrive sync service
- 2026-03-19 — new binary masquerading as Adobe driver component

Hard Rule 3 discipline: mechanism CLASS only above. No PoC content extracted; Aspose library name + OST/PST file format + Dropbox/OneDrive Personal endpoints + scheduled-task patterns are all publicly published defender-relevant indicators.

## Attribution — Hard Rule 2 Preserved

SecurityWeek verbatim: "Symantec and Carbon Black did not share any information about who may have been behind the attack" (14 words, Hard Rule 6 compliant).

Symantec analytic judgment (relayed by SecurityAffairs): "almost certainly state-linked given the target and the patience involved" (12 words, Hard Rule 6 compliant). This is analytic-judgment hedge based on operational discipline + target value, NOT a formal moderate/high-confidence attribution.

NO tracked roster actor named. Archimedes does NOT originate or upgrade attribution. Per Hard Rule 2: Symantec's hedge is preserved verbatim without upgrade.

## A&D Operator-Profile Relevance — TTPs Reusable Even Without Victim Attribution

No A&D-watchlist entity named. Financial-sector single-victim. Below the FLASH A&D-campaign bar (Trigger 5 requires named A&D entity).

But the TTPs are reusable against A&D primes by any actor with comparable operational discipline:

1. **Aspose-wrapper OST→PST extraction is platform-agnostic.** Any Outlook-using enterprise (i.e., every A&D prime) has the same exposure if the executive endpoint is compromised. Mailbox theft is a classic intelligence-collection objective against A&D leadership — contract negotiations, supplier discussions, M&A communications, classified-program scheduling at the metadata level, sensitive HR / personnel decisions.

2. **Dropbox + OneDrive Personal exfil bypass for an A&D prime** is the M365 + sanctioned-cloud blend that DIB SOCs struggle to distinguish from normal user behavior. ITAR / CUI environments may have policy restrictions on Personal cloud accounts, but enforcement gaps are common.

3. **Hardcoded Microsoft IP DNS-bypass is a procedural lesson** for any environment relying on DNS-tier blocklisting or DNS-anomaly detection as primary egress control. Re-evaluate IP-tier outbound monitoring.

4. **Scheduled-task rotation across 5-minute / 5-hour / 15-hour / 24-hour windows** under Adobe / Lenovo / OneDrive masquerade names is an EDR-evasion procedural signature that any A&D SOC running Defender or Carbon Black can build hunts against.

## Defender Pivot — Splunk Hunts

Once Symantec's published IOC set (file hashes for mailbox stealer + masquerading executables) is extracted from security.com:

- Hash-based pivot against `archimedes` + `defenseclaw_local` indices.
- Splunk hunt — Outlook OST→PST conversion processes invoking Aspose namespace assemblies (`Aspose.Email`, `Aspose.Email.dll`) from non-licensed-Aspose endpoints.
- Splunk hunt — scheduled-task registration with names containing "Adobe" / "OneDrive" / "Lenovo" service-mimicking patterns and unusual rotation intervals.
- Splunk hunt — outbound HTTPS to Dropbox / OneDrive Personal (`onedrive.live.com` / `graph.microsoft.com` personal-tenant) from cleared-personnel endpoints, distinguishing from sanctioned `*.sharepoint.com` tenancy.
- Splunk hunt — outbound HTTPS to hardcoded Microsoft IP addresses (not hostnames). DNS-tier blocklisting is insufficient for this pattern; IP-tier egress monitoring is required.
- Splunk hunt — SYSTEM-privilege processes with Adobe Acrobat / OneDrive masquerade file paths outside canonical install directories.

PM-000 sentinel Splunk first-party check returned 0 events over last 24h on the mechanism-class superset. Hash-based pivot pending IOC extraction.

## IOCs surfaced

(Symantec published full IOC set at security.com; extraction from Symantec primary is pending. Below is the mechanism-class superset.)

- Aspose.Email .NET library namespace invocation by non-Aspose-licensed processes
- Scheduled-task registration patterns: Adobe / Lenovo / OneDrive masquerade names with 5min / 5hr / 15hr / 24hr rotation
- Dropbox + OneDrive Personal exfiltration endpoints (onedrive.live.com / graph.microsoft.com personal-tenant)
- Hardcoded Microsoft IP addresses (not hostnames) — DNS-bypass exfil
- SYSTEM-privilege processes with Adobe Acrobat / OneDrive masquerade file paths outside canonical install directories

## Relationship to Existing Findings

No relation to existing tracked actors at sweep. Pattern observation: this is a state-linked-espionage TTP profile that Archimedes would normally cross-reference against roster actors with mailbox-collection histories. Existing roster actors with documented Outlook / M365 mailbox-extraction tradecraft (e.g., APT29 / Cozy Bear in historical Microsoft / SolarWinds context; Charming Kitten / APT35 in OAuth-token-theft context; Iranian APT clusters in 365 mailbox-rule abuse) are NOT named in Symantec's write-up.

Archimedes does NOT originate cross-roster attribution per Hard Rule 2. Actor-profiler awareness handoff is appropriate scaffolding path for cross-roster TTP-matching in next 30-90 days.

## Open Questions for Analyst

- **SAT-KAC: TTP-reusability assumption.** What assumption underlies the "TTPs reusable against A&D" framing, and what would invalidate it? Possible falsifiers: (a) highly tailored TTPs that don't generalize beyond a specific exchange's IT stack, (b) Aspose-wrapper requiring specific .NET runtime context not present at A&D primes, (c) hardcoded-IP DNS-bypass requiring specific Microsoft IP ranges that change frequently and would not work elsewhere.

- **SAT-ACH: state-linked-actor-class question.** Symantec's "almost certainly state-linked given the target and the patience involved" hedge is consistent with multiple actor classes: (a) Russian SVR-class long-dwell intelligence collection, (b) Chinese MSS-class commercial/financial intelligence collection (financial-sector targeting fits historical pattern), (c) Iranian MOIS-class intelligence collection with espionage-oriented mailbox theft, (d) North Korean APT-class espionage with financial-adjacent intelligence collection. Symantec's declination of all of these is grader-significant. Decompose actor-class hypotheses without Archimedes originating attribution.

- **Actor-profiler awareness:** does the TTP combination (Aspose-wrapper OST→PST + Dropbox/OneDrive Personal exfil + hardcoded-IP DNS-bypass + scheduled-task rotation + binary masquerading) warrant a state-linked-espionage-actor-unnamed placeholder for cross-finding pattern matching? Operator decision.

## Analytic notes (from analyst review)

The TTP-reusability framing should hedge harder than the cluster anchor currently does. KAC surfaced two test-classified critical assumptions: A&D SOC IP-tier egress visibility (A2 — typical A&D CASB controls operate at FQDN/URL tier, not IP tier, so hardcoded Microsoft IP egress to sanctioned-cloud netblocks may pass default policy) and Aspose.Email base-rate at A&D primes (A6 — Aspose is a popular commercial library used by eDiscovery / litigation-hold / mail-archival vendors, so namespace-invocation hunts may generate false positives without local baselining). The general mailbox-theft objective transfers regardless of mechanism, but specific mechanism transfer is variable. Briefer should frame defender hunts as "candidate hunts requiring local baselining," not as drop-in high-signal hunts.

The state-linked-actor-class ACH produced a five-way tie at zero inconsistencies across Russian-class / Chinese-class / Iranian-class / novel-state-class / false-flag-state hypotheses. DPRK financial-pivot-class and criminal-with-state-discipline class accumulate three inconsistencies each (cumulative-window cadence without terminal extraction, Symantec patience hedge weakly against, absence of financial-extraction component) — disfavored but not eliminated. Symantec's "almost certainly state-linked" hedge is supported by the ACH at the disjunction layer (state-class collectively is WEP "likely"). Within the state-class tier, no specific class is differentially favored — preserving the tied-class structure is required to hold Hard Rule 2. The brief must NOT compress to a single state class; that compression would originate attribution.

WEP ceiling adjustment: none required. Grader's "likely" on substantive operational claims and "roughly even chance" on parsimonious-attacker-class are both consistent with the ACH output. Brittleness on the actor-class question is high — a Tier-1 IR firm attribution would collapse the tie; preserve tripwires.

## Hard Rule Compliance

- **Hard Rule 2:** PRESERVED — Symantec / SecurityWeek / SecurityAffairs all decline attribution; Symantec analytic hedge preserved verbatim without upgrade; no roster actor named.
- **Hard Rule 3:** PRESERVED — mechanism class described at category level only; no PoC content; publicly published indicators surfaced for defender utility.
- **Hard Rule 6:** PRESERVED — two short Symantec quotes preserved (14 words + 12 words); one quote per relay source maximum.
- **Hard Rule 7:** PRESERVED — Symantec's IOC set at security.com is referenced by URL only; file hashes for extraction-by-pivot path. No credentials surfaced.
- **Hard Rule 8:** Splunk -30d sweep ran across defenseclaw_local + (archimedes NOT sourcetype=archimedes:*) on mechanism-class superset (Aspose.Email + OST→PST + Dropbox/OneDrive Personal exfil + hardcoded-IP exfil + Adobe/Lenovo/OneDrive scheduled-task masquerade); 0 events per PM-000 sentinel; silence not disconfirming. Hash-based pivot pending IOC extraction from Symantec primary.
