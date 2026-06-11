---
id: finding-2026-06-11-0011
finding_id: finding-2026-06-11-0011-bleepingcomputer-europol-audia6-crypto-laundering-takedown-380m-tkachuk-ledenev-georgia-dark2web-forum
title: "AudiA6 crypto-laundering service dismantled in Europol-coordinated 11-country operation — >$380M laundered 2022-2025; 15+ international ransomware investigations linked; 2 administrators charged Ruslan Igorevich Tkachuk (37, Ukrainian) + Alexander Vladimirovich Ledenev (25, Russian) detained in Georgia + admin of 'Dark2Web' forum; 25 domains + €86,000 crypto seized + €692,000 frozen + 80 vehicles/properties + Telegram blocked; up to 20 years each; ransomware-economy disruption indirect A&D relevance"
date: 2026-06-11
created_at: 2026-06-11T17:25:00-04:00
graded_by: grader
grading_run_id: afternoon-20260611-160000
grading_mode: scheduled_brief
test: false
status: graded

# ============================================================================
# Core grading (admiralty-grading skill output) — LAYERED
# ============================================================================
digraph: B2
admiralty_grade: B2
digraph_layered:
  audia6_dismantled_by_europol_coordinated_11_country_operation: B2  # BleepingComputer (B ratified) sole in-window publisher; underlying Europol announcement is canonical at originator A but not directly retrieved
  audia6_laundered_more_than_380m_2022_2025: B2  # BleepingComputer relay of Europol
  audia6_linked_to_15_plus_international_ransomware_investigations: B2  # BC relay; no specific ransomware groups named per source
  audia6_posed_as_cryptocurrency_mixing_service_3_to_10_percent_commission_1_hour_turnaround: B2  # BC relay of Europol operational description
  audia6_two_administrators_charged_ruslan_igorevich_tkachuk_37_ukrainian_alexander_vladimirovich_ledenev_25_russian: B2  # BC relay of charging document
  audia6_administrators_detained_in_georgia: B2  # BC relay
  audia6_administrators_face_up_to_20_years: B2  # BC relay
  audia6_administrators_also_charged_with_administering_dark2web_forum: B2  # BC relay
  audia6_prior_arrest_2025_09_polish_authorities_separate_ukrainian_linked_to_audia6: B3  # BC historical reference
  audia6_seizures_25_domains_86k_eur_crypto_seized_692k_eur_frozen_80_vehicles_properties_telegram_blocked: B2  # BC relay
  no_ransomware_groups_named_explicitly_in_audia6_link: A1  # Verifiable absence in source
  no_ad_prime_named_as_victim: A1  # Verifiable absence
  ad_relevance_indirect_ransomware_economy_disruption_signal: B3  # Structural inference
  cluster_anchor: B2

digraph_anchor: >
  Cluster anchored at B2. BleepingComputer (B ratified) is the
  SOLE in-window publisher relaying Europol-coordinated takedown
  announcement. Underlying Europol announcement IS canonical at
  originator layer (Europol = peer-class to FBI / DOJ / NCA for
  law-enforcement actions; provisional A at originator layer)
  but NOT directly retrieved this sweep — substantive content
  is BC-relay-derived. Single-source through single-publisher
  relay; single-source veto applies on substantive operational
  claims.

  Hard Rule 2 binding constraint: NOT TRIGGERED — Tkachuk +
  Ledenev are publicly named in Europol charging document
  per LEGAL-POLICY data-handling table (corporate officers
  publicly named in incidents with source citation). No actor
  attribution to roster-tracked actor.

  Hard Rule 7 binding constraint: PRESERVED — named persons are
  charged subjects in unsealed law-enforcement action; LEGAL-
  POLICY GDPR data-handling permits with source citation.

  Hard Rule 8 binding constraint: -7d@d first-party Splunk
  query on AudiA6 + Tkachuk + Ledenev + Dark2Web: zero
  substantive first-party matches. Per Hard Rule 8: silence
  is not disconfirming. First-party precedence does NOT apply.

source_reliability:
  grade: B
  source_name: "BleepingComputer (B ratified) — sole in-window publisher relaying Europol-coordinated takedown announcement"
  source_yaml_id: bleepingcomputer
  grade_rationale: "Pre-assigned B ratified per source-grades.yaml; sole in-window publisher; underlying Europol announcement canonical at originator A but NOT directly retrieved."
  provisional: false

credibility:
  grade: 2
  checklist_passed:
    - probably_true_consistent_with_european_law_enforcement_pattern_for_2024_2026_cryptocurrency_laundering_takedown_class
    - probably_true_no_contradicting_a_b_grade_source
    - probably_true_technical_claims_internally_coherent_3_to_10_percent_commission_1_hour_turnaround_consistent_with_mixing_service_class_operationally_plausible_for_named_dollar_volume

corroboration:
  independent_sources:
    - bleepingcomputer  # SOLE in-window publisher
    - europol-coordinated-announcement   # primary, NOT directly retrieved
  independent: false
  test_failed: "Single in-window publisher; primary Europol announcement not directly retrieved"

first_party_precedence:
  applied: false
  splunk_evidence: null

single_source_veto_applied: true
single_source_veto_detail: "APPLIES on all substantive operational claims (laundered amount, victim count, scope, charging detail, seizure detail). WEP caps at 'likely'."

wep_ceiling: likely
wep_layered:
  audia6_dismantled_by_europol_coordinated_11_country_operation: likely
  audia6_laundered_more_than_380m_2022_2025: likely
  audia6_linked_to_15_plus_ransomware_investigations: likely
  tkachuk_ledenev_charged_detained_georgia_administered_dark2web: likely
  audia6_seizures_25_domains_86k_seized_692k_frozen_80_vehicles_properties: likely
  no_ad_prime_named: very_likely  # A1 verifiable absence
  no_specific_ransomware_groups_named: very_likely  # A1 verifiable absence
  ad_relevance_indirect_ransomware_economy_disruption_signal: roughly_even_chance  # Structural

inclusion:
  eligible_for:
    - daily_brief_monitoring   # B2 clears B2 minimum; monitoring tier
    - weekly_synthesis         # Counter-cybercrime tempo data point
inclusion_eligibility: yes
inclusion_rationale: "B2 + WEP 'likely'. NOT eligible for action-tier — no A&D-prime victim, no actor attribution to roster, no actionable defender step. Counter-cybercrime tempo signal value for monitoring + weekly."

attribution: null
attribution_claims:
  - claimed_subjects:
      - Ruslan_Igorevich_Tkachuk_37_Ukrainian
      - Alexander_Vladimirovich_Ledenev_25_Russian
    claim_type: europol_charging_document_administered_audia6_crypto_laundering_service_and_dark2web_forum
    detained_location: Georgia
    max_sentence: 20_years_each
    claimed_by_sources:
      - bleepingcomputer
      - europol-coordinated-announcement
    independent_corroboration: false
    archimedes_attribution_origination_check: pass_per_legal_policy_data_handling_corporate_officers_publicly_named_in_incidents_with_source_citation

cves: []
affected_products: []
affected_vendors: []

iocs:
  individuals_named:
    - name: Ruslan Igorevich Tkachuk
      age: 37
      nationality: Ukrainian
      status: detained_Georgia
      role: audia6_administrator_and_dark2web_forum_administrator
    - name: Alexander Vladimirovich Ledenev
      age: 25
      nationality: Russian
      status: detained_Georgia
      role: audia6_administrator_and_dark2web_forum_administrator
  takedown_scope:
    operation_type: europol_coordinated_11_country
    dollar_volume_laundered: more_than_380M_USD_2022_2025
    ransomware_investigations_linked: 15+_international
    seizures:
      domains: 25
      crypto_seized: 86000_EUR
      crypto_frozen: 692000_EUR
      vehicles_properties: 80
      telegram_accounts: blocked
ioc_count: 2  # Two named individuals

cluster:
  topic: "AudiA6 crypto-laundering service takedown (Europol-coordinated 11-country operation) — ransomware-economy disruption signal"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-06-11-pm-005   # subset (1 of 4 cybercrime cluster components)

analyst_review_required: false
red_team_review_required: false
red_team_review: null
analysis_sections:
  sat_ach: null
  sat_kac: null

tlp: CLEAR
published_in_briefs: [2026-06-11-afternoon]
retracted: false

source_grade_revision_proposed:
  - source_yaml_id: europol-coordinated-announcement
    proposed_action: add_new_provisional_source_entry_if_missing
    proposed_grade: A
    rationale: "Europol coordinated announcements are canonical at originator A per peer-class to FBI / DOJ / NCA for law-enforcement actions. If not in source-grades.yaml, librarian handoff to add as provisional A."
---

# AudiA6 crypto-laundering service dismantled in Europol-coordinated 11-country operation

## Summary

BleepingComputer (B sole in-window publisher) relays Europol-coordinated 11-country takedown of AudiA6, a cryptocurrency-laundering service that posed as a mixing service with 3-10% commission and ~1-hour turnaround. The service laundered >$380M between 2022 and 2025 and is linked to 15+ international ransomware investigations (no specific groups named per source). Two administrators charged: Ruslan Igorevich Tkachuk (37, Ukrainian) and Alexander Vladimirovich Ledenev (25, Russian), detained in Georgia, facing up to 20 years each; also charged with administering the "Dark2Web" forum. Seizures: 25 domains, €86,000 in crypto seized, €692,000 in crypto frozen, 80 vehicles/properties, Telegram accounts blocked. Polish authorities arrested a separate Ukrainian national linked to AudiA6 in September 2025. No A&D-prime named; no specific ransomware groups named. Ransomware-economy disruption signal warrants monitoring-tier inclusion as a counter-cybercrime tempo data point.

## Sources

### BleepingComputer (bleepingcomputer, B)

- URL: https://www.bleepingcomputer.com/news/legal/authorities-dismantle-audia6-ransomware-crypto-laundering-service/
- Published: 2026-06-11 15:55 EDT
- Key claim: Europol-coordinated 11-country dismantling; >$380M laundered 2022-2025; 15+ international ransomware investigations linked; 2 administrators charged + detained Georgia; seizures detail.

### Europol coordinated announcement (NOT directly retrieved)

- Role: primary law-enforcement source on takedown
- Librarian handoff if not in source-grades.yaml: add as provisional A

## A&D / DIB relevance

- **No A&D-prime named:** verifiable absence.
- **No specific ransomware groups named:** verifiable absence.
- **Indirect (B3):** ransomware-economy disruption reduces general operational tempo against any victim including DIB.

## IOCs surfaced

- **Individuals named in charging document:** Ruslan Igorevich Tkachuk (37, Ukrainian) + Alexander Vladimirovich Ledenev (25, Russian), detained Georgia.
- **Takedown scope:** >$380M USD laundered 2022-2025; 25 domains seized; €86k crypto seized + €692k frozen; 80 vehicles/properties; Telegram accounts blocked.

## Open questions for analyst

None at this confidence tier. Counter-cybercrime tempo signal for monitoring + weekly synthesis.
