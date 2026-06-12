---
id: finding-2026-06-12-0003
finding_id: finding-2026-06-12-0003-securityweek-handala-cal-water-iran-mois-5gb-leak-rtkbase-ntrip-credentials-restatement-attribution-iran-cyber-watch
title: "Handala Hack (#014, Iran/MOIS) claims California Water Service compromise — 5GB customer-PII leak + RTKBase administrative credentials + NTRIP source passwords; Dataminr cites RTKBase platform as initial access vector + lateral move to billing; Cal Water no public acknowledgment; water utility NOT A&D; Iran Cyber Watch primary content"
date: 2026-06-12
created_at: 2026-06-12T16:35:00-04:00
graded_by: grader
grading_run_id: afternoon-20260612-160000
grading_mode: scheduled_brief
test: false
status: graded

# ============================================================================
# Core grading (admiralty-grading skill output) — LAYERED
# ============================================================================
digraph: B3
admiralty_grade: B3
digraph_layered:
  # ---- ACTOR-CLAIM LAYER (self-publication via Handala blog through media relay) ----
  handala_blog_self_publication_claims_cal_water_compromise: B3  # Actor self-claim through SW relay; Handala's blog itself not directly retrieved (passive-only policy per LEGAL-POLICY)
  cal_water_chico_district_named_in_leak_per_handala_self_publication: B3  # Self-claim layer
  leak_volume_5gb_per_handala_self_publication: B3  # Self-claim layer
  customer_pii_categories_per_handala_self_publication: B3  # Self-claim layer
  rtkbase_administrative_credentials_in_leak_per_dataminr_analysis: B3  # Dataminr third-party analysis; Dataminr not in source-grades.yaml; provisional B-tier per cheatsheet "named third-party analytic firm with structured public report"
  ntrip_mountpoint_passwords_in_leak_per_dataminr_analysis: B3  # Dataminr third-party analysis; same provisional B-tier as above
  # ---- ATTRIBUTION LAYER (restatement of prior public attribution per article) ----
  handala_iran_mois_attribution_RESTATEMENT_of_prior_public: A2  # SW article restates US-government prior public attribution of Handala to Iran MOIS; restatement framing (NOT new attribution) — A grade for the restatement claim itself; verifiable per the article's framing "US previously linked Handala to Iran's MOIS"
  handala_in_archimedes_roster_actor_014_HIGH: A1  # Verifiable presence — _roster.yaml entry #014 with aliases Void Manticore / Storm-0842 / DEV-0842, attribution nation: IR, service: MOIS, threat_level: HIGH
  new_aliases_banished_kitten_dune_red_sandstorm_to_fold_into_dossier: B3  # SW article aliases; not currently in roster #014; flag for actor-profiler
  # ---- TECHNICAL TRADECRAFT LAYER (Dataminr analysis) ----
  rtkbase_platform_likely_initial_access_vector_per_dataminr: B3  # Dataminr analytic framing; "likely" hedge in source language
  actor_lateral_movement_to_billing_system_per_dataminr: B3  # Dataminr analytic framing
  rtkbase_operational_for_783_continuous_hours_at_access_time: B3  # Dataminr-specific telemetry detail
  gps_correction_data_seven_district_mountpoints: B3  # Dataminr-specific telemetry detail
  handala_toolkit_historically_includes_wipers_mbr_overwrite: B2  # Article restates prior known TTPs; consistent with roster #014 + prior public reporting; conservative B2 anchor on the historical-TTP characterization
  destructive_escalation_within_single_campaign_cycle_historical_pattern: B2  # Article-cited historical pattern; conservative anchor
  # ---- VICTIM LAYER ----
  cal_water_no_public_acknowledgment_at_sw_publication: A1  # Verifiable absence at the SW publication layer
  cal_water_water_utility_not_ad_prime: A1  # Verifiable absence from aerospace-defense.yaml
  cal_water_investor_owned_california_2m_customer_class: B2  # Background fact relayed by SW; consistent with public record
  # ---- FLASH-TRIGGER EVALUATION (carry-forward from pm-003 + 12:00 sentinel) ----
  trigger_2_tracked_actor_attribution_RESTATEMENT_not_new: A1  # FLASH-POLICY Trigger 2 requires "new (not re-reporting prior attribution)"; restatement does NOT qualify
  trigger_4_ttp_change_not_triggered_consistent_with_handala_playbook: A1  # 5GB blog dump pattern + wiper-capable toolkit consistent with prior Handala TTPs
  trigger_5_ad_sector_campaign_not_triggered: A1  # Water utility NOT A&D
  # ---- A&D / DIB RELEVANCE LAYER ----
  ad_direct_relevance: A1  # NONE — verifiable absence
  ad_structural_relevance_iran_continued_capability_against_us_civilian_infrastructure: B3  # Structural inference; Iran Cyber Watch standing-section anchor
  iranian_retaliation_extrapolation_to_ad_prime_targeting_BLOCKED: A1  # Hard Rule 2 binding — Archimedes does NOT extrapolate
  # ---- CREDENTIAL DISCIPLINE LAYER (HARD RULE 7) ----
  rtkbase_credentials_named_in_leak_per_article_no_values_stored: A1  # Hard Rule 7 binding; counts at article level only
  ntrip_mountpoint_passwords_named_in_leak_per_article_no_values_stored: A1  # Hard Rule 7 binding
  customer_pii_named_in_leak_per_article_no_values_stored: A1  # GDPR data minimization applies
  cluster_anchor: B3

digraph_anchor: >
  Cluster anchored at B3 (Possibly True) on the actor-claim
  layer: Handala Hack self-publication via Handala blog claiming
  Cal Water compromise, reaching the corpus through a single
  SecurityWeek (provisional B) media relay AND through Dataminr
  third-party analysis (not in source-grades.yaml; provisional
  B-tier per cheatsheet "named third-party analytic firm with
  structured public report"). The Handala blog itself was NOT
  directly retrieved this sweep per LEGAL-POLICY passive-only
  stance on actor publication channels — operator decision
  pending on whether to enable direct retrieval of Handala's
  publication channel.

  Single-source veto APPLIES at the strict "actor self-claim
  independently corroborated by second IR firm" framing — only
  Dataminr provides third-party analysis at this sweep; no
  CrowdStrike / Mandiant / Unit 42 / Volexity / MSTIC cross-
  vendor corroboration. WEP ceiling on the cluster anchor caps
  at "possibly" per veto + B-tier source layer + ACTOR-SELF-
  CLAIM-ORIGIN evidence basis.

  WHAT THE B3 ATTESTS:
    (a) Handala has self-published a claim against Cal Water —
        at single B-grade media relay + Dataminr analytic layer.
    (b) The leak content categories (5GB volume, customer PII,
        RTKBase credentials, NTRIP passwords) are claimed by
        Handala and analyzed by Dataminr — both source layers
        below A.
    (c) RTKBase-as-initial-access-vector is Dataminr's analytic
        framing ("likely served as initial access vector") with
        explicit hedge in source language.

  WHAT THE B3 DOES NOT ATTEST:
    - That Cal Water actually suffered the breach as claimed
      (no Cal Water public acknowledgment at SW publication
      layer; single-source veto on victim acknowledgment layer
      per pm-003 collector analysis).
    - The destructive-escalation potential extrapolated to
      future Cal Water cycle (article frames historical pattern
      only; Hard Rule 2 binding on extrapolation).
    - Any A&D-prime targeting implication from this campaign
      cycle (Hard Rule 2 binding — Iranian retaliation framing
      does NOT extrapolate to A&D from single water-utility
      campaign).

  HARD RULE 2 binding constraint: PRESERVED.
    - Handala IS in Archimedes _roster.yaml at actor #014 with
      pre-existing Iran/MOIS attribution. The SW article
      RESTATES prior US-government public attribution; this is
      restatement-of-prior-attribution, NOT origination of new
      attribution by Archimedes. The roster's pre-existing
      attribution is the citation basis.
    - The NEW aliases in the SW article (Banished Kitten /
      Dune / Red Sandstorm) are flagged for actor-profiler to
      fold into the #014 dossier if corroborated; this finding
      does NOT cross-walk those aliases to other roster actors
      and does NOT confirm the alias mapping as Archimedes
      attribution.
    - Iranian retaliation framing is NOT extrapolated to A&D-
      prime targeting from this single campaign cycle.

  HARD RULE 6 binding constraint: PRESERVED. No verbatim quote
  above ≤15 words propagated into the finding. SW restatement
  attribution: "US previously linked Handala to Iran's MOIS"
  (8 words) is at the cap and preserved as restatement
  framing.

  HARD RULE 7 binding constraint: PRESERVED. Credentials and
  PII enumerated in the leak per SW + Dataminr analysis are
  counted at article level only. No credential values stored
  in raw-signal pm-003 or in this finding. Categories named:
  RTKBase administrative credentials + NTRIP mountpoint
  passwords + customer PII (names, addresses, phone numbers,
  account numbers, payment histories). GDPR data minimization
  applies.

  HARD RULE 8 binding constraint: Per pm-000 sentinel + grader-
  side first-party Splunk query (-7d window across
  index=archimedes OR index=defenseclaw_local on Handala +
  Cal Water + RTKBase + NTRIP + Void Manticore keywords): 12
  events at most-recent query, all Archimedes self-
  instrumentation. Zero substantive first-party matches.
  defenseclaw_local does not observably run Cal Water
  infrastructure (Frank lab is not a California water utility);
  silence expected. Per Hard Rule 8: silence is not
  disconfirming. First-party precedence does NOT apply.

source_reliability:
  grade: B
  source_name: "SecurityWeek (provisional B) relaying Handala self-publication + Dataminr third-party analysis (Dataminr provisional B-tier per cheatsheet, not in source-grades.yaml)"
  source_yaml_id: securityweek
  grade_rationale: >
    SecurityWeek is provisional B per source-grades.yaml. The
    underlying actor channel (Handala blog) is treated as actor-
    self-claim layer (NOT a graded source-grades.yaml entry;
    actor publication channels are dossier-content layer, not
    intelligence-source layer). Dataminr is not in
    source-grades.yaml — provisional B-tier per cheatsheet
    "named third-party analytic firm with structured public
    report" lineage. Operator may want to evaluate Dataminr for
    formal source-grades.yaml entry given its appearance pattern
    across multiple findings.
  provisional: true
  provisional_since: 2026-05-06
  source_grade_revision_proposed: null
  flag_for_librarian: >
    Add Dataminr to source-grades.yaml at provisional B-tier per
    cheatsheet "named third-party analytic firm with structured
    public report" lineage.

credibility:
  grade: 3
  checklist_passed:
    - possibly_true_single_source_uncorroborated_b_grade_or_better  # SW single in-window publisher; Dataminr analytic relay; meets "single-source, uncorroborated, but source is B-grade or better"
    - possibly_true_partially_consistent_with_known_ttps_but_some_elements_novel  # RTKBase-as-IAV is a novel TTP angle for Handala; the destructive-leak playbook itself is consistent with #014 dossier
  rationale: >
    Cluster anchor at Grade 3 (Possibly True): single B-grade
    publisher in window; Dataminr provides third-party analytic
    framing but Dataminr itself is B-tier provisional and is
    NOT publisher-independent from SW at the in-window evidence
    basis (SW article is the relay surface for Dataminr's
    analysis). No second IR firm at sweep (CrowdStrike /
    Mandiant / Unit 42 / Volexity / MSTIC silent on Cal Water).
    The leak content categories are claimed by Handala self-
    publication + analyzed by Dataminr — the chain is single
    actor-claim primary + single analytic primary + single
    media relay. RTKBase-as-initial-access-vector is a novel
    TTP angle within Handala's playbook (the destructive-leak
    pattern itself is consistent with prior Handala campaigns
    per roster #014); the novel element pulls credibility down
    from Grade 2 to Grade 3 per checklist condition
    "Partially consistent with known TTPs but some elements
    novel." Grade 2 (Probably True) is NOT met because the
    independent-publisher corroboration requirement fails;
    Grade 4 (Doubtful) is NOT met because no multiple
    unverified assumptions are required and Handala's
    track record + roster #014 HIGH classification establish
    the actor-credibility baseline.

corroboration:
  independent_sources:
    - securityweek
  independent: false  # Single SW publisher in window; Dataminr analytic relay through SW; no second IR firm corroboration
  test_passed: >
    Corroboration test FAILS at this sweep. SW single in-window
    publisher; Dataminr third-party analytic surface reaches
    cluster only via the SW relay. Independence requires either
    (a) Cal Water public acknowledgment, (b) second IR firm
    (CrowdStrike / Mandiant / Unit 42 / Volexity / MSTIC)
    independent analysis, or (c) Handala's blog direct retrieval
    (passive-only operator decision pending). All three are
    next-sweep watch items.

first_party_precedence:
  applied: false
  splunk_evidence: >
    Per pm-000 sentinel + grader-side query (-7d window across
    index=archimedes OR index=defenseclaw_local on Handala +
    Cal Water + RTKBase + NTRIP + Void Manticore + Storm-0842
    keywords): 12 events at most-recent query, all Archimedes
    self-instrumentation. Zero substantive first-party matches.
    defenseclaw_local does not observably run Cal Water
    infrastructure. Silence expected; per Hard Rule 8: silence
    is not disconfirming. First-party precedence does NOT
    apply.

single_source_veto_applied: true  # Single SW publisher + Dataminr through SW relay
wep_ceiling: possibly  # Per single-source veto + B3 cluster anchor
wep_layered:
  handala_self_claim_layer: possibly  # Per veto + B3
  cal_water_actually_breached_layer: possibly  # No Cal Water public acknowledgment at sweep
  rtkbase_as_initial_access_vector_layer: possibly  # Dataminr "likely" hedge in source + analytic layer
  handala_iran_mois_attribution_restatement_layer: very_likely  # Restatement of pre-existing US-government public attribution + roster #014 anchor
  handala_destructive_escalation_extrapolation_to_cal_water_BLOCKED: not_assessed_per_hard_rule_2  # Hard Rule 2 binding on extrapolation
  iranian_retaliation_extrapolation_to_ad_prime_BLOCKED: not_assessed_per_hard_rule_2  # Hard Rule 2 binding
  ad_direct_relevance: very_unlikely  # Verifiable absence — water utility NOT A&D

inclusion:
  eligible_for:
    - daily_brief_monitoring  # B3 meets C3 monitoring threshold; primary content for Iran Cyber Watch standing section
    - weekly_synthesis
    - actor_profile_update  # Roster #014 dossier extension — Banished Kitten / Dune / Red Sandstorm aliases + RTKBase TTP angle
  flash_eligible: false  # Per pm-003 FLASH-trigger evaluation and 12:00 sentinel — Trigger 2 fails (restatement not new), Trigger 4 fails (consistent TTPs), Trigger 5 fails (not A&D)
  flash_threshold_met: false  # B3 below FLASH B2 threshold

graded_at: 2026-06-12T16:35:00-04:00

# ============================================================================
# Cluster metadata
# ============================================================================
cluster:
  topic: "Handala Hack (#014, Iran/MOIS) self-claim of Cal Water compromise — 5GB leak + RTKBase administrative credentials + NTRIP source passwords; Dataminr analytic framing of RTKBase-as-IAV; Cal Water no acknowledgment; water utility NOT A&D"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-06-12-pm-003
  attribution_claims:
    - claimed_actor: Handala Hack (roster #014)
      claimed_by_sources: [securityweek_restatement_of_prior_us_government_public_attribution_via_dataminr_analytic_framing]
      requires_analyst_review: false
      note: "Handala IS in roster #014 with pre-existing Iran/MOIS attribution. SW restates prior US-government public attribution. Restatement-of-prior, NOT origination of new. Roster anchor is the citation basis."
    - claimed_alias_extensions:
        - Banished Kitten
        - Dune
        - Red Sandstorm
      claimed_by_sources: [securityweek_pm_003]
      requires_actor_profiler_review: true
      note: "NEW aliases for #014 (currently in roster: Void Manticore, Storm-0842, DEV-0842). actor-profiler to evaluate and fold into dossier if corroborated."

# ============================================================================
# Downstream handoff flags
# ============================================================================
analyst_review_required: false  # B3 / possibly + restatement-of-prior-attribution + roster anchor present — no SAT-ACH structural ambiguity at cluster level
red_team_review_required: false  # WEP "possibly" — below very_likely red-team trigger threshold per doctrine
red_team_review: null

actor_profile_handoff:
  roster_id: "014"
  proposed_dossier_updates:
    - new_aliases: [Banished Kitten, Dune, Red Sandstorm]
    - new_ttp_angle: "RTKBase platform as initial access vector with lateral move to billing system; NTRIP mountpoint password exposure cross-organizational"
    - new_campaign: "Cal Water Service / Chico District — 5GB customer-PII + RTKBase/NTRIP credential leak (single-source veto; Cal Water no acknowledgment)"
    - threat_level_review_trigger: false  # No new evidence of #014 escalation to A&D-prime targeting; current HIGH classification preserved

vuln_tracker_handoff: null  # No tracked CVE in this finding

analysis_sections:
  sat_ach: null
  sat_kac: null

tlp: CLEAR
published_in_briefs: [2026-06-12-afternoon]
retracted: false
retraction_brief_id: null
---

# Handala Hack (#014, Iran/MOIS) claims California Water Service compromise — 5GB customer-PII + RTKBase credentials + NTRIP passwords; Dataminr cites RTKBase-as-initial-access-vector; Cal Water no acknowledgment; water utility NOT A&D

## Summary

Handala Hack (Archimedes roster actor #014, Iran/MOIS, threat_level HIGH) has self-published a claim against California Water Service (Cal Water), per a SecurityWeek relay on 2026-06-12. The article cites a 5 GB leak comprising customer PII, RTKBase administrative credentials, and NTRIP mountpoint passwords across seven district mountpoints; Dataminr analytic framing identifies the RTKBase platform as the likely initial access vector with lateral movement to the billing system. The Iran/MOIS attribution is a restatement of prior US-government public attribution, not new attribution per the source. Cal Water has not publicly acknowledged the breach. This is the primary content for the Iran Cyber Watch standing section in the afternoon brief; Cal Water is NOT in aerospace-defense.yaml and A&D-prime structural extrapolation is blocked by Hard Rule 2.

## Sources

### SecurityWeek (securityweek, digraph: B provisional)

- URL: `https://www.securityweek.com/iranian-cyber-group-handala-claims-cal-water-hack/`
- Published: 2026-06-12T07:30 EDT
- Key claim: Handala self-publishes Cal Water compromise; 5 GB leak with customer PII, RTKBase administrative credentials, NTRIP source passwords; Dataminr analytic framing of RTKBase-as-IAV; Cal Water has not publicly acknowledged.

## Technical detail

- **Victim claimed:** California Water Service (Cal Water), Chico District named in the leak. Investor-owned California water utility (~2 million customers; not federal, not A&D).
- **Attacker:** Handala — roster #014 with attribution nation: IR, service: MOIS, threat_level: HIGH. SW article lists aliases: Handala Hack, Banished Kitten, Dune, Red Sandstorm, Storm-0842, Void Manticore. Of these, Void Manticore + Storm-0842 + DEV-0842 are in the existing roster #014 dossier; Banished Kitten + Dune + Red Sandstorm are NEW aliases flagged for actor-profiler review.
- **Attribution framing:** restatement of prior US-government public attribution per SW article ("US previously linked Handala to Iran's MOIS" — 8 words, preserved verbatim under Hard Rule 6 cap). This is restatement, NOT new attribution.
- **Leak volume / content:** 5 GB; customer PII (names, addresses, phone numbers, account numbers, payment histories); RTKBase administrative credentials; NTRIP source passwords across seven district mountpoints. Hard Rule 7 binding: no credential values are stored at any layer of the corpus; only category counts at the article level.
- **Initial access vector per Dataminr:** RTKBase platform identified as "likely served as initial access vector"; actor lateral movement to billing system documented. RTKBase platform operational ~783 continuous hours at access time; GPS correction data covered seven district mountpoints.
- **Destructive potential framing:** Handala's historical toolkit includes custom wipers and MBR-overwriting capabilities; the group has previously escalated from data theft to destructive operations within a single campaign cycle. This is article-cited historical pattern, NOT a prediction for Cal Water; Hard Rule 2 binding on extrapolation.
- **Cal Water response:** no public acknowledgment at SW publication time.

## Hard Rule 2 — attribution discipline (BINDING)

- Handala IS in roster #014 with pre-existing Iran/MOIS attribution. SW article RESTATES prior US-government public attribution; this is restatement-of-prior-attribution, NOT Archimedes origination of new attribution.
- NEW aliases (Banished Kitten, Dune, Red Sandstorm) are flagged for actor-profiler to evaluate and fold into the #014 dossier if corroborated against independent sources; this finding does NOT confirm the alias mapping as Archimedes attribution.
- Iranian retaliation framing is NOT extrapolated to A&D-prime targeting from this single water-utility campaign cycle. Hard Rule 2 binding.

## Hard Rule 7 — credential / PII discipline (BINDING)

Credentials enumerated in the leak per SW + Dataminr analysis are counted at article level only. No credential values stored at any layer of the raw-signal pm-003 or this finding. Categories named:

- RTKBase administrative credentials
- NTRIP mountpoint passwords (seven mountpoints implied)
- Customer PII (names, addresses, phone numbers, account numbers, payment histories) — GDPR data minimization applies

## FLASH trigger evaluation (carry-forward from pm-003 + 12:00 sentinel)

- **Trigger 2 (tracked-actor attribution):** NOT triggered. Attribution is restatement, NOT new per FLASH-POLICY definition.
- **Trigger 4 (TTP change):** NOT triggered. 5 GB blog dump pattern + wiper-capable toolkit consistent with prior Handala TTPs. (RTKBase-as-IAV is novel WITHIN Handala's playbook but does NOT meet Trigger 4 "TTP change" threshold for a roster-actor at this scale.)
- **Trigger 5 (A&D-sector campaign):** NOT triggered. Cal Water is a water utility, NOT A&D.

## IOCs surfaced

None enumerated by SW or Dataminr. Handala's blog itself was NOT directly retrieved this sweep (LEGAL-POLICY passive-only stance on actor publication channels; operator decision pending on Handala channel direct retrieval).

## Relationship to existing findings

- **Actor dossier extension** on roster #014 (Handala Hack). No supersession of prior findings. Folds RTKBase-as-IAV TTP angle and new alias candidates into the dossier-update queue.
- **Iran Cyber Watch standing section** primary content for this afternoon brief.

## Open questions for analyst

- Watch: Cal Water public acknowledgment (would firm the breach beyond actor self-claim).
- Watch: second IR-firm corroboration beyond Dataminr (CrowdStrike Falcon, Mandiant, Volexity, Unit 42 silent on Cal Water at this sweep).
- Watch: wiper / MBR-overwrite escalation against Cal Water within the campaign cycle.
- Watch: US Treasury / OFAC sanctions response trajectory (Handala has prior US-government attention).
- Watch: actor-profiler dossier fold-in for Banished Kitten / Dune / Red Sandstorm aliases.
- RTKBase / NTRIP cross-organizational exposure pattern is worth surfacing in Threat Detection Weekly synthesis: GPS-precision client organizations downstream of Cal Water's NTRIP mountpoints could be subverted via compromised mountpoint credentials.
