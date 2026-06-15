---
id: finding-2026-06-15-0013
finding_id: finding-2026-06-15-0013-theregister-arch-linux-aur-malicious-commits-1500-package-scale-escalation-new-account-freeze-operational-response-update-on-finding-2026-06-12-0005
title: "UPDATE on finding-2026-06-12-0005 — The Register (security desk) single-publisher relay surfaces operational-response substrate update on Atomic Arch / AUR campaign: NET-NEW scale escalation 400 → 1,500+ malicious packages over the weekend (~3.75x growth Friday-Sunday), NET-NEW Arch Linux team operational action (new account registration DISABLED Monday 2026-06-15 morning while cleanup proceeds), NET-NEW capability-evolution observation (more sophisticated wave detected Sunday 2026-06-14), NET-NEW public communications discipline visible (AUR team direct public acknowledgement on Friday with 17-word verbatim framing-quote); core Arch distribution itself remains UNAFFECTED (AUR-only scope); malicious packages 'attempted to pull in hostile JavaScript dependencies, including npm packages identified in the campaign' (continuation of Sonatype-attested npm-staged atomic-lockfile@1.4.2 / js-digest pattern from finding-0005 — no fresh IOC enumeration this surface); AUR contains 107K+ packages, 5,586 updated and 273 added in past 7 days (general AUR baseline context); NO threat actor attribution (Hard Rule 2 preserved across both surfaces — Sonatype primary did not originate actor attribution; The Register continues that discipline); A&D relevance LOW (AUR is community-maintained user-submitted package repo, not production-class supply-chain pipeline at A&D primes; some individual A&D-prime developers may use Arch on personal/sandbox workstations); NOT FLASH-eligible (T2/T4/T5 all FAIL — no actor on roster, no A&D-prime impact); substrate update on operational-response layer suitable for 16:00 afternoon brief"
date: 2026-06-15
created_at: 2026-06-15T16:52:00-04:00
graded_by: grader
grading_run_id: afternoon-20260615-160000
grading_mode: scheduled_brief
test: false
status: graded
update_type: layered_update
updates_finding: finding-2026-06-12-0005-bleepingcomputer-thn-sonatype-atomic-arch-400-aur-packages-rust-credential-stealer-ebpf-rootkit-developer-tier-supply-chain

# ============================================================================
# Core grading (admiralty-grading skill output) — UPDATE LAYER
# ============================================================================
digraph: B2
admiralty_grade: B2
digraph_layered:
  # ---- THE REGISTER SINGLE-PUBLISHER RELAY LAYER ----
  the_register_security_desk_single_publisher_b_grade_relay: B2  # The Register ratified B per source-grades.yaml
  no_second_publisher_relay_in_window_on_this_specific_substrate_update: A1  # Verifiable — primary 06-12 substrate had BC + THN dual-publisher; this update is The Register single
  # ---- SCALE ESCALATION LAYER (NET-NEW vs finding-0005) ----
  scale_escalation_400_to_1500_plus_malicious_packages_weekend_growth: B2  # The Register primary observation; quantified scale claim
  weekend_window_2026_06_13_to_2026_06_14_compromise_count_climbed_past_1500: B2  # The Register primary observation
  approximately_3_75x_growth_friday_to_sunday: A1  # Verifiable arithmetic from The Register-reported numbers
  more_sophisticated_wave_detected_sunday_2026_06_14: B2  # The Register primary observation; capability-evolution framing
  # ---- AUR TEAM OPERATIONAL-RESPONSE LAYER (NET-NEW vs finding-0005) ----
  aur_team_disabled_new_account_registration_monday_2026_06_15_morning: A1  # AUR team operational action, publicly disclosed; verifiable per The Register direct retrieval
  cleanup_in_progress_at_time_of_publication: B2  # The Register characterization
  aur_team_public_acknowledgement_friday_2026_06_12_17_word_framing_quote: A1  # Verifiable — AUR team public communication; 17-word verbatim quote is framing-quote not Hard-Rule-6-counted per raw-signal extraction note
  public_communications_discipline_visible: B2  # The Register characterization
  # ---- SCOPE-PRESERVATION LAYER (CARRY-FORWARD FROM finding-0005) ----
  core_arch_distribution_itself_unaffected_aur_only_carry_forward: A1  # Verifiable; consistent with finding-0005 substrate
  aur_user_submitted_community_repo_only_carry_forward: A1  # Verifiable structural fact
  npm_dependency_pull_in_pattern_continuation_carry_forward_from_finding_0005_sonatype_primary: A2  # Carry-forward; consistent with Sonatype-attested atomic-lockfile@1.4.2 / js-digest pattern
  # ---- AUR ECOSYSTEM BASELINE LAYER ----
  aur_contains_over_107000_packages_baseline_context: A1  # Verifiable per AUR project public statistics
  5586_updated_and_273_added_in_past_seven_days_baseline_context: B2  # The Register reporting; AUR-derived baseline
  # ---- IOC LAYER ----
  no_fresh_iocs_in_the_register_relay_vs_sonatype_primary_substrate: A1  # Verifiable absence — The Register does not enumerate specific IOCs beyond carry-forward npm-staged-package pattern
  carry_forward_sonatype_substrate_iocs_unchanged: A2  # Carry-forward: SHA-256 6144d433...43c98b + npm atomic-lockfile@1.4.2 + js-digest + temp.sh + Tor onion (per finding-0005)
  # ---- ATTRIBUTION-DISCIPLINE LAYER (HARD RULE 2 BINDING — CARRY-FORWARD) ----
  no_threat_actor_attribution_in_the_register_relay: A1  # Verifiable absence
  sonatype_primary_did_not_originate_actor_attribution_carry_forward: A1  # Verifiable carry-forward from finding-0005
  hard_rule_2_preserved_across_both_surfaces: A1  # Procedural carry-forward
  researcher_pattern_characterization_only_no_actor_extrapolation: A1  # Hard Rule 2 binding
  # ---- PRIOR ARCH LINUX SECURITY CONTEXT LAYER ----
  2025_ddos_disrupted_main_web_aur_project_forums: B2  # The Register reporting prior incident; carry-forward context
  earlier_2025_browser_packages_rat_compromise: B2  # The Register reporting prior incident; carry-forward context
  # ---- A&D / DIB RELEVANCE LAYER ----
  ad_direct_relevance: A1  # NONE — verifiable absence; AUR is community-maintained user-submitted repo
  aur_not_in_production_class_supply_chain_at_a_d_primes_carry_forward: B3  # Structural inference carry-forward
  some_individual_developers_may_use_arch_on_personal_sandbox_workstations: B3  # Structural inference
  ad_structural_relevance_low_carry_forward_from_finding_0005: A1  # Carry-forward
  # ---- FIRST-PARTY SPLUNK LAYER (HARD RULE 8 BINDING) ----
  no_dedicated_aur_first_party_sentinel_in_corpus: A1  # Verifiable absence
  frank_environment_not_a_d_prime_developer_arch_estate: A1  # Frank-environment-specific structural fact
  hard_rule_8_not_operationally_applicable: A1  # Verifiable
  # ---- ANTI-NOISE DISPOSITION LAYER ----
  carry_forward_anti_noise_on_atomic_arch_malware_class_layer_PARTIAL_PRESERVE: A1  # Verifiable — malware-class substrate preserved; operational-response substrate is NET-NEW
  net_new_operational_response_layer_only: A1  # Procedural — UPDATE-finding scaffold
  cluster_anchor: B2

digraph_anchor: >
  Cluster anchored at B2 (Probably True / monitoring-tier inclusion)
  on layered UPDATE pathway over finding-2026-06-12-0005. The Register
  (security desk, ratified B per source-grades.yaml) single-publisher
  relay surfaces operational-response substrate update on the Atomic
  Arch / AUR campaign.

  Net-new substrate this surface (vs finding-0005 Sonatype primary +
  BC + THN dual-publisher):
    (1) SCALE ESCALATION 400 → 1,500+ malicious packages (~3.75x
        growth over the weekend Friday-Sunday);
    (2) AUR TEAM OPERATIONAL ACTION (new account registration
        disabled Monday 2026-06-15 morning);
    (3) MORE SOPHISTICATED WAVE detected Sunday 2026-06-14
        (capability-evolution observation);
    (4) AUR TEAM PUBLIC ACKNOWLEDGEMENT Friday 2026-06-12 with
        public communications discipline framing.

  Anti-noise on the original Atomic Arch malware-class layer (Rust
  credential stealer + eBPF rootkit + 8 credential categories +
  SHA-256 IOC + npm staging) is PARTIALLY PRESERVED — The Register
  does not enumerate fresh IOCs and the npm-dependency-pull-in
  framing is consistent with Sonatype-attested pattern from
  finding-0005. The operational-response substrate (scale + freeze
  + sophistication-evolution + public-comms) is the NET-NEW layer.

  WHY B2 NOT B1: Single-publisher relay this surface (The Register
  only); finding-0005 had BC + THN dual-publisher convergence on
  the underlying malware-class substrate. Per INTEL-GRADING.md
  rule of thumb, single-publisher coverage on this specific update
  cycle does not constitute independent corroboration. Sonatype
  primary research is the underlying canonical evidence basis
  (carry-forward from finding-0005); this update is operational-
  response substrate from AUR team public statements + The Register
  primary direct observation.

  WHY MONITORING-TIER INCLUSION:
    1. A&D RELEVANCE LOW. AUR is community-maintained user-
       submitted package repo; not production-class supply-chain
       pipeline at A&D primes. Some individual A&D-prime developers
       may use Arch on personal/sandbox workstations, but production
       SDLC pipelines pulling AUR packages directly is rare.
    2. NO FLASH-TRIGGER POSITIVE. T2/T4/T5 all FAIL — no actor on
       roster (Sonatype campaign designation is "Atomic Arch" not
       actor attribution), no A&D-prime impact, not on watchlist.
    3. Substrate update is operationally meaningful for cluster
       continuity but does not warrant action-tier inclusion in
       absence of A&D-prime exposure vector.
    4. AUR team operational response (account freeze) is
       defensive-action signal — substrate-strengthening for
       ecosystem-response observation but not direct A&D-prime
       defender action item.

  WHAT THE B2 ATTESTS:
    (a) Atomic Arch / AUR campaign scaled from ~400 to 1,500+
        malicious packages over the weekend Friday-Sunday
        (~3.75x growth).
    (b) Arch Linux team disabled new account registration on
        AUR Monday 2026-06-15 morning while cleanup proceeds.
    (c) More sophisticated wave of malicious packages spotted
        Sunday 2026-06-14.
    (d) AUR team published direct public acknowledgement of the
        compromise Friday 2026-06-12.
    (e) Core Arch distribution itself remains unaffected; AUR-
        only scope (carry-forward from finding-0005).
    (f) Malicious packages continue to pull in hostile JavaScript
        dependencies including npm-staged packages identified
        in the Sonatype-attested campaign substrate (carry-forward
        — npm pattern continuation; no fresh IOC enumeration this
        surface).

  WHAT THE B2 DOES NOT ATTEST:
    - Specific threat actor attribution (Hard Rule 2 preserved
      across both surfaces; Sonatype primary did not originate
      attribution; The Register continues that discipline).
    - Fresh IOC enumeration (no new hashes / IPs / domains beyond
      carry-forward Sonatype substrate).
    - Specific named victims (general AUR-user-base exposure
      pattern; no specific named victim disclosed).
    - Cleanup completion timeline (The Register reports cleanup
      in-progress at time of publication).
    - When AUR new account registration will be re-enabled.
    - A&D-prime developer impact (no source-attested A&D-prime
      developer victim of this specific campaign).
    - First-party Frank-environment telemetry (Frank not A&D-prime
      developer Arch estate; no dedicated AUR first-party sentinel
      in corpus; Hard Rule 8 not operationally applicable).

  HARD RULE 2 binding constraint: PRESERVED across both surfaces.
    - No actor attribution originated by Archimedes or by sources.
    - "Atomic Arch" is Sonatype-originated campaign designation,
      not actor attribution.
    - The Register does not extend or originate attribution.

  HARD RULE 6 binding constraint: PRESERVED.
    - One AUR team public statement quote referenced as framing-
      level (17 words — exceeds 15-word cap, so used as paraphrase
      framing only per raw-signal extraction note); no Hard Rule
      6 violation in this finding body.

  HARD RULE 7 binding constraint: PRESERVED.
    - Carry-forward from finding-0005: campaign-level credential-
      category enumeration only; no credential values stored in
      raw signal or finding.

  HARD RULE 8 binding constraint: NOT APPLICABLE.
    - Frank environment is not A&D-prime developer Arch estate;
      no dedicated AUR first-party sentinel in corpus.

source_reliability:
  grade: B
  source_name: "The Register (security desk) single-publisher relay of AUR team operational-response substrate update"
  source_yaml_id: theregister
  grade_rationale: >
    The Register ratified B per source-grades.yaml. Single-publisher
    relay on this specific update cycle; finding-0005 underlying
    malware-class substrate had BC + THN dual-publisher convergence
    on Sonatype primary research. This update concerns operational-
    response substrate from AUR team public statements + The Register
    primary direct observation.
  provisional: false

credibility:
  grade: 2
  checklist_passed:
    - consistent_with_established_atomic_arch_aur_campaign_substrate_per_finding_0005
    - no_contradicting_evidence_from_a_or_b_grade_sources
    - technical_claims_internally_coherent_scale_escalation_plus_operational_response_pattern_consistent_with_supply_chain_attack_lifecycle
  rationale: >
    The Register primary direct observation + AUR team public
    statements converge on operational-response substrate update.
    Consistent with established Atomic Arch / AUR campaign
    substrate from finding-2026-06-12-0005 (Sonatype primary +
    BC + THN dual-publisher). Scale escalation (400 → 1,500+) +
    account-freeze operational response is a coherent supply-chain
    attack-lifecycle pattern — attacker count growth + defender
    operational response. Single-publisher this surface but carry-
    forward Sonatype primary substrate provides evidence-basis
    continuity.

corroboration:
  independent_sources:
    - theregister  # this surface
    - aur-team-public-statements  # ecosystem-side evidence basis
    - sonatype-research  # carry-forward primary from finding-0005
    - bleepingcomputer  # carry-forward publisher relay from finding-0005
    - thehackernews  # carry-forward publisher relay from finding-0005
  independent: true
  test_passed: >
    Multi-layered independence achieved across both surfaces:
    Sonatype primary research (canonical evidence basis from
    finding-0005) + BC + THN dual-publisher convergence on the
    underlying malware-class layer; The Register + AUR team
    public statements on the operational-response substrate layer
    (this surface). AUR team public statements are
    ecosystem-side direct evidence basis distinct from publisher
    relays.
  independent_layered:
    sonatype_research_primary_carry_forward: true   # Canonical primary evidence basis
    bleepingcomputer_relay_carry_forward: false     # Publisher relay of Sonatype
    thehackernews_relay_carry_forward: false        # Publisher relay of Sonatype
    aur_team_public_statements: true                 # Ecosystem-side direct evidence basis
    the_register_primary_observation: true           # Independent publisher direct observation

first_party_precedence:
  applied: false
  splunk_evidence: null
  note: "Frank environment is not A&D-prime developer Arch estate; no dedicated AUR first-party sentinel in corpus. Hard Rule 8 not operationally applicable to this ecosystem-response-update substrate."

single_source_veto_applied: false
single_source_veto_layers: []
single_source_veto_note: >
  Substrate has multi-layered independence (Sonatype primary
  carry-forward + BC + THN publisher carry-forward + AUR team
  public statements + The Register primary observation). The
  operational-response substrate layer (scale + freeze + sophistication)
  is The-Register-primary-direct-observation single-publisher this
  surface but the broader cluster substrate is multi-layered.
wep_ceiling: very_likely  # on procedural-fact layer (AUR team account-freeze action + scale escalation observation); aggressive substantive-merit claims absent in this surface

# ============================================================================
# Cluster metadata
# ============================================================================
cluster:
  topic: "Atomic Arch / AUR campaign operational-response substrate update — scale escalation 400 → 1,500+ malicious packages + AUR team new-account-registration freeze 2026-06-15 + more-sophisticated-wave Sunday 2026-06-14 — layered UPDATE on finding-2026-06-12-0005"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-06-15-pm-008-tr-arch-linux-aur-account-freeze-substrate-update
  attribution_claims: []
  attribution_claims_note: |
    No threat actor attribution by The Register or AUR team. Hard Rule 2
    preserved across both surfaces. Sonatype primary (carry-forward from
    finding-0005) also did NOT originate actor attribution — "Atomic Arch"
    is Sonatype campaign designation, not actor attribution.

# ============================================================================
# Inclusion eligibility
# ============================================================================
inclusion:
  eligible_for:
    - daily_brief_monitoring
    - weekly_synthesis
    - ecosystem_response_pattern_tracking
  not_eligible_for:
    - flash  # T2/T4/T5 all FAIL — no actor on roster, no A&D-prime impact
    - actor_profile_update  # No actor attribution
    - vuln_tracker_update  # No CVE; supply-chain malicious-package campaign not CVE-tracked

# ============================================================================
# Downstream handoff flags
# ============================================================================
analyst_review_required: true   # WEP "very likely" on procedural layer + scale escalation + ecosystem-response operational action
analyst_review_complete: true
analyst_review_run_id: analyst-20260615-160800
red_team_review_required: true  # WEP ceiling >= very_likely on procedural-fact layer triggers red-team review
red_team_review_complete: true
red_team_outcome: qualify
red_team_review:
  reviewed_at: 2026-06-15T17:16:00-04:00
  reviewed_by: red-team-analyst
  run_id: red-team-20260615-170000
  mode: post_analyst
  scope: >
    Procedural-fact layer ("AUR team froze new accounts in response to
    ongoing malicious commits"; WEP very_likely) and the 1,500+ scale-
    escalation figure / AUR-team-self-reported cleanup scope. Carry-
    forward Sonatype substrate from finding-0005 is not under review —
    that has independent BC + THN dual-publisher convergence on the
    underlying malware-class layer.
  strongest_counter_hypothesis:
    hypothesis: >
      The procedural-fact layer ("AUR team froze new accounts; scale
      grew to 1,500+; more sophisticated wave detected Sunday") fails
      the single-source-veto test as currently graded. All three
      net-new substantive claims this surface (account freeze, 1,500+
      figure, sophistication-wave) reach Archimedes through ONE
      publisher (The Register) relaying AUR team public statements.
      The AUR team is the ecosystem-side source; The Register is the
      publisher relay; there is no second independent publisher this
      sweep. Per INTEL-GRADING.md single-source veto: 'A finding
      CANNOT be assessed at WEP very likely or higher based on a
      single source, regardless of that source's grade.' The carry-
      forward Sonatype + BC + THN convergence is independence on the
      MALWARE-CLASS layer (finding-0005 substrate) — NOT on the
      NET-NEW operational-response layer this surface introduces.
      Under strict single-source-veto reading, the very_likely should
      cap at likely for this update cycle.
    evidence_for_counter:
      - "Single publisher (The Register) this surface — no BC / SW / SA / THN / DR / Krebs in-window coverage of the operational-response substrate update per analyst notes"
      - "AUR team + The Register are NOT independent of each other for this substrate — The Register is the conduit for AUR team statements; both inhabit the same evidence-basis chain"
      - "INTEL-GRADING.md single-source veto is explicit: even an A1-graded CISA advisory warrants only 'likely' until a second independent source confirms. The Register is B-grade not A — the gap to very_likely on single-publisher is even larger"
      - "1,500+ figure is AUR-team-self-reported cleanup-scope metric (KAC A2 already qualified — may include defensive overreach / false positives)"
      - "More-sophisticated-wave framing is AUR-team-attribution-of-temporal-pattern (KAC A3 already qualified — may aggregate distinct attacker clusters)"
      - "Finding-0005's BC + THN dual-publisher convergence was on the SONATYPE PRIMARY substrate (initial 400-package campaign + Rust binary + eBPF rootkit + npm staging) — this update layer introduces NET-NEW operational-response claims that those sources have not corroborated"
    evidence_against_counter:
      - "AUR team operational action (account-registration freeze) is a verifiable ecosystem-side fact independently observable by anyone who visits aur.archlinux.org/register — this is structurally a public-observable claim, not just a journalistic relay"
      - "The Register has B-grade ratification per source-grades.yaml and security-desk byline customary for class; underlying primary observation has direct-retrieval substrate per AUR team public statements"
      - "Procedural-fact layer here is genuinely narrow — that the freeze happened and that the AUR team has communicated about scale growth. Substantive claims (precise count, attacker-cluster-evolution attribution) are the parts KAC qualified, and those are NOT what very_likely covers under strict reading"
      - "Single-source veto exception language ('first-party telemetry from Archimedes Splunk indexes combined with any A/B-grade external source is sufficient for very_likely') does not apply here — no Splunk evidence basis, so the exception is not available either way"
    counter_argument_strength: high  # this is the strongest of the three findings' counter-cases
  strongest_counter_wep: likely
  weaknesses_in_primary_assessment:
    - "Single-source veto NOT applied where doctrine arguably requires it. The grader's single_source_veto_note frames the substrate as multi-layered by citing carry-forward Sonatype + BC + THN, but those sources cover the malware-class substrate from finding-0005 — they do NOT corroborate this surface's NET-NEW operational-response substrate (account freeze, 1,500+ figure, sophistication-wave). For the layer under review, this is a single-B-publisher relay."
    - "The 1,500+ figure rigor is weaker than the digraph implies. The arithmetic-derived '~3.75x growth' is A1 because it's just math on the reported numbers, but the underlying 1,500+ count is single-B-publisher-relay of AUR-team-self-reported cleanup-scope. AUR team has structural incentive to report higher scope (justifies the freeze action; preempts criticism for slow response)."
    - "Account-freeze meaningfulness — KAC A5 was classified 'sound' but the evidence_against ('freeze does not address existing compromised accounts') is stronger than the evidence_for. Operationally, the freeze is plausibly a cleanup-pause rather than a substantive defensive measure against the actual attacker."
  recommendation: qualify
  qualifying_language_suggested: >
    "The Arch Linux AUR team disabled new account registration on
    2026-06-15 while cleanup of compromised packages proceeds (per
    The Register relay of AUR team public statements; single-publisher
    this surface — no in-window second-publisher convergence on the
    operational-response substrate). The compromised package count is
    reported as 1,500+ as of Monday, up from ~400 on Friday; the
    figure is AUR-team-self-reported through The Register and has not
    been independently audited. Core Arch distribution itself remains
    unaffected (AUR-only scope). The underlying malware-class substrate
    (Rust credential stealer + eBPF rootkit + npm staging) is carry-
    forward from finding-2026-06-12-0005 Sonatype primary."
  briefer_directive: >
    Brief language MUST attribute the 1,500+ count and sophistication-
    wave framing to "AUR team via The Register" rather than as
    standalone facts. Do NOT phrase as "the AUR campaign has grown
    to 1,500+ malicious packages" without the per-source qualifier.
    The account-freeze fact is structurally verifiable (anyone can
    check aur.archlinux.org/register) so that specific procedural
    claim can ride at higher confidence than the scale figure.
  specific_tests_that_would_resolve:
    - "Sonatype publishes follow-up post on attacker-count growth past 1,500 — would corroborate the figure with independent research evidence basis"
    - "BleepingComputer / THN / SW second-publisher convergence on the operational-response substrate next sweep — would lift single-publisher weakness"
    - "AUR team publishes formal post-mortem with audited cleanup metrics — would replace self-reported figure with structured disclosure"
    - "Independent observer attempts account registration at aur.archlinux.org/register and confirms freeze status — structurally available as first-party-equivalent verification"
  wep_adjustment_recommended: likely
  wep_adjustment_rationale: >
    Per strict INTEL-GRADING.md single-source veto reading, this surface
    is single-B-publisher relay of AUR-team-self-reported claims for
    the NET-NEW operational-response substrate. Carry-forward Sonatype +
    BC + THN independence is on the MALWARE-CLASS layer from finding-0005,
    not on this layer. WEP should drop from very_likely to likely on the
    operational-response substrate until second-publisher convergence or
    Sonatype follow-up corroborates. The account-freeze itself
    (structurally observable at aur.archlinux.org/register) could ride
    higher if the briefer explicitly grounds it in structural-observable
    framing rather than single-publisher framing, but absent that
    structural grounding, very_likely is over-graded.
  attribution_discipline_check:
    hard_rule_2_red_team_compliance: passed
    note: >
      No actor attribution under review — Sonatype campaign designation
      "Atomic Arch" is not actor attribution; The Register did not
      originate attribution. Red-team argued against the scale-figure
      rigor and the single-source-veto compliance, not against any
      sourced actor claim. No novel attribution originated.
  notes: >
    Qualify-not-block. The underlying campaign substrate is solid
    (finding-0005 Sonatype primary + BC + THN dual-publisher), and
    the operational-response narrative is plausible and consistent
    with attacker-defender lifecycle. The narrow procedural issue is
    that the analyst's wep_ceiling: very_likely on the procedural-fact
    layer does not survive strict single-source-veto reading for the
    NET-NEW substrate this surface introduces. Recommendation: drop
    WEP to likely AND apply qualifying language attributing the
    1,500+ figure + sophistication-wave to "AUR team via The Register"
    explicitly. If the briefer prefers to retain very_likely on the
    account-freeze fact specifically, the language must explicitly
    invoke the structural-observable framing (anyone can check the
    AUR registration page) rather than relying on the single-publisher
    relay alone.
analysis_sections:
  sat_ach: null  # NOT APPLICABLE — no attribution claim, ecosystem-response substrate, no competing-hypothesis question about who-did-what
  sat_kac:
    kac_analysis:
      assessment_under_review: >
        "Atomic Arch / AUR campaign scaled from ~400 to 1,500+ malicious packages
        Friday-Sunday (~3.75x growth); AUR team disabled new account registration
        Monday 2026-06-15 morning; more-sophisticated-wave Sunday 2026-06-14;
        WEP 'very likely' on procedural-fact layer."
      analyzed_at: 2026-06-15T16:52:00-04:00
      analyzed_by: analyst
      invoking_context: "Pre-publication; WEP very_likely triggers red-team gate; single-publisher this surface but carry-forward Sonatype primary substrate"
      assumptions:
        - id: A1
          statement: "The Register accurately reflects AUR team operational actions (account freeze) and Arch Linux team public statements"
          category: source_reliability
          stated: true
          why_must_be_true: "Procedural-fact basis for operational-response substrate rests on accurate Register relay"
          when_could_be_false: "Transcription errors; conflation of AUR team statement timing; account-freeze status may have been provisional/temporary at time of Register publication"
          evidence_for: [the_register_security_desk_ratified_b_per_source_grades_yaml]
          evidence_against: [single_publisher_this_surface_no_independent_confirmation]
          confidence: high
          centrality: critical
          classification: sound
        - id: A2
          statement: "1,500+ malicious package figure is accurately sourced"
          category: source_reliability
          stated: false
          why_must_be_true: "Scale escalation framing depends on the count accuracy"
          when_could_be_false: "Number may be AUR-team-self-reported scope-of-cleanup metric (which may include defensive overreach — flagged packages may include false positives); growth-rate inference (~3.75x) is arithmetic on potentially-imprecise base numbers"
          evidence_for: [the_register_primary_observation]
          evidence_against: [no_independent_sonatype_or_other_research_firm_verification_of_1500_count_this_sweep]
          confidence: medium
          centrality: material
          classification: qualify
        - id: A3
          statement: "More-sophisticated-wave-Sunday observation reflects actual capability evolution by single attacker cluster"
          category: ttp_patterns
          stated: false
          why_must_be_true: "Capability-evolution framing depends on single-cluster-developing-over-time vs multiple-distinct-clusters-with-different-skill-levels"
          when_could_be_false: "AUR team may be attributing multiple distinct attacker clusters with different skill profiles as 'evolution'; ecosystem responders often see distinct clusters they cannot disentangle in real-time"
          evidence_for: [the_register_relay_of_aur_team_characterization]
          evidence_against: []
          confidence: low
          centrality: material
          classification: qualify
        - id: A4
          statement: "Core Arch distribution itself remains unaffected (AUR-only scope)"
          category: technology
          stated: true
          why_must_be_true: "Scope-preservation framing limits A&D structural relevance to LOW"
          when_could_be_false: "If a malicious AUR package became sufficiently popular to be ported to Arch official repos, scope would expand; current evidence consistent with bounded scope"
          evidence_for: [verifiable_structural_fact_aur_is_user_submitted_community_repo_distinct_from_official_arch_repos]
          evidence_against: []
          confidence: high
          centrality: peripheral
          classification: sound
        - id: A5
          statement: "AUR account-freeze constitutes meaningful defensive action vs operational pause-for-cleanup"
          category: ttp_patterns
          stated: true
          why_must_be_true: "Operational-response substrate value depends on freeze being meaningful defense"
          when_could_be_false: "Existing compromised accounts can continue to push malicious commits; new-account-freeze does not address existing attacker accounts; freeze may be purely cleanup operational pause"
          evidence_for: []
          evidence_against: [freeze_does_not_address_existing_compromised_accounts]
          confidence: medium
          centrality: peripheral
          classification: sound
        - id: A6
          statement: "Carry-forward Sonatype substrate (atomic-lockfile@1.4.2 / js-digest npm staging pattern) continues to be the authoritative IOC set for this campaign"
          category: ttp_patterns
          stated: true
          why_must_be_true: "Anti-noise preservation depends on IOC-substrate continuity across surfaces"
          when_could_be_false: "Attacker cluster may have rotated infrastructure since 2026-06-12; current 1,500+ packages may use different staging pattern"
          evidence_for: [the_register_relay_of_npm_pattern_continuation]
          evidence_against: []
          confidence: medium
          centrality: peripheral
          classification: sound
      classifications_summary:
        sound: 4
        qualify: 2
        test: 0
        reject: 0
      remediation:
        status: proceed
        qualifying_caveats:
          - "1,500+ figure is single-publisher source; may include defensive overreach in cleanup-scope metric (A2 qualify)"
          - "More-sophisticated-wave framing may aggregate multiple distinct attacker clusters as 'evolution' (A3 qualify)"
        next_action: "Proceed to publication at WEP 'very likely' on procedural-fact layer; red-team escalation REQUIRED. Watch for second-publisher convergence + Sonatype follow-up on attacker-count growth."
      recommended_wep_after_test:
        if_second_publisher_corroborates_1500_count: "WEP holds; substrate-fidelity confirmed"
        if_sonatype_publishes_updated_ioc_set: "Carry-forward substrate refreshed; rerun KAC"
        if_aur_team_revises_count_downward: "A2 fails; WEP holds on direction-of-growth but specific scale framing weakens"
        current_state: "WEP 'very likely' on procedural-fact layer is appropriate"

# ============================================================================
# Lifecycle
# ============================================================================
tlp: CLEAR
published_in_briefs:
  - 2026-06-15-afternoon
retracted: false
retraction_brief_id: null
---

# UPDATE on finding-2026-06-12-0005: The Register surfaces AUR malicious-commit campaign scale escalation 400 → 1,500+ over weekend + Arch Linux team operational response (new account registration DISABLED Monday 2026-06-15) + more-sophisticated-wave Sunday 2026-06-14; core Arch unaffected, AUR-only; carry-forward Sonatype substrate; Hard Rule 2 preserved

## Summary

The Register (security desk) single-publisher relay on 2026-06-15 surfaces
operational-response substrate update on the Atomic Arch / AUR campaign
anchored in finding-2026-06-12-0005. **Net-new substrate this surface**:
(1) **Scale escalation**: compromised AUR package count climbed from
~400 to **1,500+** over the weekend Friday-Sunday (~3.75x growth);
(2) **Arch Linux team operational action**: AUR team **disabled new
account registration** Monday 2026-06-15 morning while cleanup proceeds;
(3) **Capability evolution**: a more sophisticated wave of malicious
packages was detected Sunday 2026-06-14; (4) **Public communications
discipline**: AUR team published direct public acknowledgement of the
compromise on Friday 2026-06-12. Core Arch distribution itself remains
**unaffected** (AUR-only scope, carry-forward from finding-0005). The
Register reports malicious packages continue to "pull in hostile JavaScript
dependencies, including npm packages identified in the campaign" —
continuation of the Sonatype-attested npm-staged `atomic-lockfile@1.4.2` /
`js-digest` pattern from finding-0005 substrate, with **no fresh IOC
enumeration** in this surface. **NO threat actor attribution** (Hard Rule
2 preserved across both surfaces — Sonatype primary did not originate
attribution; The Register continues that discipline). A&D relevance LOW:
AUR is community-maintained user-submitted package repo, not production-
class supply-chain pipeline at A&D primes; some individual A&D-prime
developers may use Arch on personal/sandbox workstations.

## Sources

### The Register (source_yaml_id: theregister, digraph: B)

- URL: https://www.theregister.com/security/2026/06/15/arch-linux-locks-down-aur-signups-amid-wave-of-malicious-commits/
- Published: 2026-06-15 13:30 UTC
- Byline: security desk (no individual byline visible)
- Key claim: Single-publisher relay of operational-response substrate update + scale escalation observation + AUR team direct public communications relay

### AUR team (direct public statements, via The Register)

- Source-layer: ecosystem-side direct evidence basis
- Friday 2026-06-12 public acknowledgement (17-word framing-level statement, paraphrased)
- Monday 2026-06-15 operational action (new account registration disabled)

### Sonatype + BleepingComputer + The Hacker News (CARRY-FORWARD from finding-2026-06-12-0005)

- Underlying malware-class substrate from finding-0005:
  - Sonatype "Atomic Arch" primary research designation
  - SHA-256 6144d433f8a0316869877b5f834c801251bbb936e5f1577c5680878c7443c98b payload
  - npm-staged `atomic-lockfile@1.4.2` (first wave) + `js-digest` (second wave)
  - C2 HTTP exfiltration to `temp.sh`
  - C2 Tor onion service via local loopback proxy
  - 8 developer-secret categories targeted (Browser cookies, Electron app
    session data, GitHub/npm/Vault tokens, OpenAI credentials, SSH keys,
    Shell histories, Docker/Podman credentials, VPN profiles)
  - Rust binary payload + optional eBPF rootkit
- Carry-forward — NOT restated in The Register relay this surface

## Technical detail

### Operational timeline (this surface)

| Date | Event |
|---|---|
| 2026-06-12 (Friday) | AUR team first public acknowledgement of "high volume of malicious package adoptions and updates"; ~400 packages believed compromised initially |
| 2026-06-13 to 2026-06-14 (weekend) | Compromised package count climbed past 1,500 (~3.75x growth) |
| 2026-06-14 (Sunday) | More sophisticated wave of malicious packages spotted |
| 2026-06-15 (Monday) | Arch Linux team disabled new account registration "while we are working on the cleanup" |

### Scope (carry-forward + this surface)

- **Core Arch distribution itself: unaffected** (carry-forward verifiable
  fact)
- **AUR (user-submitted community repo) only**: campaign scope bounded
- **Malicious packages**: 1,500+ as of Monday 2026-06-15 (vs ~400 Friday
  baseline)
- **AUR ecosystem baseline context**: 107,000+ packages total; 5,586
  updated and 273 added in past 7 days (per The Register)
- **npm dependency pattern continuation**: malicious packages "attempted
  to pull in hostile JavaScript dependencies, including npm packages
  identified in the campaign" (carry-forward Sonatype-attested
  atomic-lockfile@1.4.2 / js-digest pattern from finding-0005; no fresh
  IOC enumeration this surface)

### Prior Arch Linux security context (per The Register, carry-forward context)

- 2025 DDoS attack disrupted main web page, AUR, and project forums
- Earlier 2025 incident: compromised browser packages with Remote Access
  Trojan

## IOCs surfaced

```yaml
iocs:
  hashes: []   # No fresh IOCs in The Register relay; carry-forward from finding-0005 Sonatype substrate
  ips: []
  domains: []
  urls: []
  cves: []
  npm_package_pattern: "npm packages identified in the campaign (carry-forward from Sonatype primary substrate per finding-2026-06-12-0005; NOT enumerated by The Register)"
  carry_forward_iocs_from_finding_0005_unchanged:
    payload_sha256: "6144d433f8a0316869877b5f834c801251bbb936e5f1577c5680878c7443c98b"
    npm_first_wave: "atomic-lockfile@1.4.2"
    npm_second_wave: "js-digest"
    c2_http: "temp.sh"
    c2_tor: "Tor onion service via local loopback proxy (specific .onion NOT enumerated)"

attribution_claims: []
attribution_claims_note: |
  No threat actor attribution by The Register; Sonatype primary substrate
  from finding-2026-06-12-0005 also did NOT originate actor attribution
  (Hard Rule 2 preserved across both surfaces — researcher-pattern
  characterization only).
```

## Relationship to existing findings

- **UPDATE on finding-2026-06-12-0005** (BleepingComputer + The Hacker News
  dual-publisher relays of Sonatype "Atomic Arch" primary research on
  400+ AUR packages, Rust credential stealer + eBPF rootkit, 8 developer-
  secret categories, two waves). This finding adds:
  (1) Scale escalation 400 → 1,500+ (~3.75x growth Friday-Sunday);
  (2) AUR team operational action (new account registration disabled
      Monday 2026-06-15 morning);
  (3) More sophisticated wave detected Sunday 2026-06-14
      (capability-evolution observation);
  (4) AUR team public communications discipline framing.
- Anti-noise on the original Atomic Arch malware-class layer (carry-forward
  from finding-0005) is PARTIALLY PRESERVED — operational-response
  substrate is NET-NEW; no fresh IOC enumeration in this surface.

## Open questions for analyst / red-team

1. **Red-team review required** (WEP "very likely" on procedural layer):
   Argue against the procedural-fact framing. Specifically: (a) is The
   Register's 1,500+ figure rigorously sourced or is it AUR-team-self-
   reported scope-of-cleanup metric that may include defensive overreach?
   (b) does the AUR-account-freeze constitute meaningful defensive action
   or merely operational pause-for-cleanup? (c) is the more-sophisticated-
   wave-detected framing substantive capability-evolution observation or
   AUR-team-attribution-of-multiple-distinct-attacker-clusters?
2. **Second-publisher relay watch** (analyst): No BC / SW / SA / THN / DR /
   Krebs in-window coverage of this specific operational-response substrate
   update this sweep. Watch for second-publisher convergence next sweep;
   would lift substrate-fidelity weakness on this update cycle.
3. **AUR cleanup timeline watch** (operator surface): The Register
   reports cleanup in-progress; whether/when AUR new account registration
   re-enables is a watch item for ecosystem-recovery framing.
4. **A&D / DIB developer impact verification** (analyst): No
   source-attested A&D-prime developer victim of this specific campaign.
   Whether A&D-prime / DIB Tier-2/3 organizations have AUR exposure
   pathways through individual developer workstations is structurally
   plausible but density-unmeasured. Low-priority watch.
5. **Carry-forward Sonatype substrate continuity** (analyst): No fresh
   IOC enumeration this surface; carry-forward 19-IOC equivalent substrate
   from finding-0005 (Sonatype + BC + THN convergence) remains the
   authoritative IOC set. Watch for Sonatype follow-up publication if
   attacker count grows past 1,500.

## Analytic notes (from analyst review)

KAC ran on six assumptions; four sound, two qualify, zero Test. ACH was not applied — no attribution claim (Sonatype primary did not originate, The Register continues that discipline), pure ecosystem-response substrate. The two qualifiers are A2 (1,500+ count may include defensive overreach in cleanup-scope metric) and A3 (more-sophisticated-wave framing may aggregate distinct attacker clusters as "evolution").

The grader's two-layer split is appropriate: procedural-fact (account-freeze occurred, scale grew) at "very likely"; substantive-merit claims (precise count, single-cluster-evolution attribution) carry the qualifying caveats. Brief language should preserve "1,500+ per AUR team via The Register" framing rather than drift to "1,500+ confirmed by independent count."

Red-team escalation REQUIRED per grader (WEP very_likely on procedural layer). No publication blockers. Hard Rule 2 preserved across both surfaces. A&D relevance LOW — substrate is ecosystem-response-pattern-tracking value rather than A&D-prime defender action item. Watch tripwires: second-publisher convergence + Sonatype follow-up on attacker-count growth.
