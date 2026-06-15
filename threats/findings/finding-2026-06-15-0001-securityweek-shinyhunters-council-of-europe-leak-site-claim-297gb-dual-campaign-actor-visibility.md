---
id: finding-2026-06-15-0001
finding_id: finding-2026-06-15-0001-securityweek-shinyhunters-council-of-europe-leak-site-claim-297gb-dual-campaign-actor-visibility
title: "SecurityWeek single-publisher relay of ShinyHunters Tor leak-site self-claim against Council of Europe (~297 GB / 429K files / payroll + HR + medical data on 10K+ employees 2011-2026; threats release 2026-06-16 deadline); CoE has not publicly acknowledged; dual-campaign actor visibility — ShinyHunters concurrently runs Oracle PeopleSoft / UNC6240 financial-extortion (BOD 26-04 KEV deadline EOD TODAY 2026-06-15) AND Council of Europe data-theft cluster (this finding) plus DentaQuest 2.6M + French Tchap-adjacent activity; NO CoE breach attributed to PeopleSoft CVE per SW article — separate campaign; NO A&D / DIB / aerospace / defense intersection (intergovernmental human-rights body); NO IOCs disclosed; NO net-new attribution to tracked roster (UNC6240/ShinyHunters still off _roster.yaml pending operator /new-actor decision)"
date: 2026-06-15
created_at: 2026-06-15T08:08:00-04:00
graded_by: grader
grading_run_id: morning-20260615-080000
grading_mode: scheduled_brief
test: false
status: graded

# ============================================================================
# Core grading (admiralty-grading skill output)
# ============================================================================
digraph: C3
digraph_layered:
  shinyhunters_posted_council_of_europe_entry_on_tor_leak_site_2026_06_15: B2  # SW first-party relay of leak-site existence; verifiable via direct URL retrieval (not retrieved this sweep — SW is the only attestation in-window)
  threatened_release_deadline_2026_06_16: B2  # SW direct article body; verifiable per leak-site post
  claimed_volume_297gb_429k_files_payroll_hr_medical_data: C3  # ShinyHunters self-claim through single B-grade publisher; CoE has NOT acknowledged; single-source veto applies on quantified volume claim until CoE ACK or second-publisher independent verification
  claimed_data_scope_payroll_2011_2026_10k_employees_14k_cvs_medical_records: C3  # ShinyHunters self-claim layer; single-source via SW; standard leak-site scope-inflation pattern warrants conservative grading until CoE ACK
  council_of_europe_NOT_acknowledged_publicly_as_of_publication: B2  # SW direct attestation; verifiable absence layer
  dual_campaign_actor_visibility_shinyhunters_concurrently_active_peoplesoft_AND_council_of_europe: B2  # SW article explicitly references the separate PeopleSoft "zero-day vulnerability in Oracle PeopleSoft" campaign — actor-visibility framing is publisher-attested
  council_of_europe_breach_NOT_attributed_to_peoplesoft_cve_per_SW: A1  # Verifiable absence — SW article does not link the two campaigns at CVE-vector layer; they are framed as SEPARATE campaigns
  no_third_party_ir_firm_attribution_no_mandiant_unit42_crowdstrike_corroboration: A1  # Verifiable absence in-window
  no_ad_dib_aerospace_defense_intersection_council_of_europe_is_intergovernmental_human_rights_body: A1  # Verifiable structural absence — CoE is 46-state Strasbourg-based intergovernmental human-rights body, NOT in DIB / CMMC / DFARS supply chain, NOT on aerospace-defense.yaml
  no_iocs_disclosed_no_domains_no_ips_no_hashes_no_malware_family: A1  # Verifiable absence in source article
  no_cve_attribution_for_council_of_europe_vector: A1  # Verifiable absence — SW does not specify breach mechanism
  shinyhunters_unc6240_NOT_on_archimedes_roster_yaml_operator_deferred_new_actor_decision_strengthening: A1  # Verifiable absence per 24-actor roster check; /new-actor decision substrate continues building per pre-flash sentinel notes
  edqm_european_directorate_quality_medicines_healthcare_pharma_adjacent_NOT_ad: B2  # SW direct attestation of EDQM among affected departments; pharma-regulatory adjacency but NOT A&D-prime
  cluster_anchor: C3

digraph_anchor: >
  Cluster anchored at C3 (Possibly True / monitoring-tier) on
  SecurityWeek's single-publisher relay of ShinyHunters' self-claim
  via Tor leak-site post. SecurityWeek is B-grade (provisional, per
  source-grades.yaml awaiting ratification).

  WHY NOT B2: Three converging constraints warrant the step-down
  from the typical single-B-source B-letter floor:

    1. SUBSTANTIVE CLAIM IS ACTOR SELF-CLAIM. The 297 GB / 429K
       files / payroll-on-10k-employees scope is ShinyHunters'
       leak-site narrative, NOT independently verified. Council
       of Europe has NOT publicly acknowledged the incident as of
       SW publication time. Self-claim through single B-grade
       publisher relay sits at credibility 3 (Possibly True) per
       INTEL-GRADING credibility checklist:
         - "Single-source, uncorroborated, but source is B-grade
            or better" (the SW relay)
         - "Technical claims plausible but not independently
            verifiable" (the volume/scope claim)
       Single-source veto applies on the quantified-volume claim.

    2. NO A&D / DIB INTERSECTION. Council of Europe is a 46-state
       intergovernmental human-rights body (Strasbourg, France).
       NOT an aerospace-defense.yaml watchlist entity, NOT a DIB
       supplier, NOT in CMMC / ITAR / DFARS supply chain. EDQM
       (European Directorate for Quality of Medicines & HealthCare)
       is pharma-regulatory, NOT A&D-prime.

    3. NO NET-NEW ATTRIBUTION TO TRACKED ROSTER ACTOR. ShinyHunters
       and UNC6240 are already in active substrate across the
       finding-2026-06-13-0002 / 0006 PeopleSoft cluster +
       finding-2026-06-10-0012 (Oracle PeopleSoft ShinyHunters
       300 instances / 100 orgs gadget chain) + finding-2026-06-12
       PeopleSoft KEV. Neither is on _roster.yaml as of 2026-05-10
       last_updated. The Council of Europe attribution is a THIRD
       campaign in the visible ShinyHunters portfolio this week,
       reinforcing the operator-deferred /new-actor decision
       substrate without changing it materially.

  WHAT THE C3 ATTESTS:
    (a) ShinyHunters posted a Council of Europe entry on its Tor
        leak site on Sunday 2026-06-15 (SW first-party relay of
        leak-site existence; B2 procedural-fact layer).
    (b) Claimed scope is approximately 297 GB across 429,000+
        files (ShinyHunters self-claim through SW B-relay; C3
        substantive claim).
    (c) Threatened release deadline 2026-06-16 (B2 procedural).
    (d) Council of Europe has NOT publicly acknowledged the
        incident as of SW publication (B2 verifiable absence).
    (e) Affected departments per claim include HR, the Secretariat,
        the Parliamentary Assembly, and EDQM (C3 self-claim layer).
    (f) Dual-campaign actor visibility: SW explicitly frames the
        Council of Europe activity as SEPARATE from ShinyHunters'
        Oracle PeopleSoft campaign (UNC6240 cluster; CVE-2026-35273
        KEV deadline EOD Sunday 2026-06-15) — actor-visibility
        framing is publisher-attested (B2).

  WHAT THE C3 DOES NOT ATTEST:
    - That the breach occurred at the claimed scope (CoE ACK
      pending; standard leak-site inflation pattern warrants
      conservative grading).
    - That the Council of Europe breach was conducted via the
      Oracle PeopleSoft CVE-2026-35273 vector (SW explicitly
      frames the two campaigns as SEPARATE; no SW-attested
      cross-link).
    - Any nation-state attribution (no PLA / MSS / Iranian / North
      Korean / Russian intelligence-services language at any
      in-window source — Hard Rule 2 binding preserved).
    - That ShinyHunters and UNC6240 are the same operator-cluster
      (Mandiant binds UNC6240 to the PeopleSoft activity per
      finding-2026-06-13-0002 + 0006; SW uses the "ShinyHunters"
      leak-site brand consistently across DentaQuest + PeopleSoft +
      Council of Europe; brand-vs-cluster relationship is an open
      actor-profiler decision, NOT grader's call).
    - Any A&D / DIB intersection (verifiable structural absence).
    - Specific IOCs (no domains / IPs / hashes / malware family
      disclosed in SW article).
    - A breach mechanism / CVE attribution (SW does not specify
      how the CoE breach was achieved).

  HARD RULE 2 binding constraint: PRESERVED.
    - ShinyHunters self-claim preserved verbatim ("claims" framing
      throughout).
    - UNC6240 binding to PeopleSoft per Mandiant preserved
      unchanged from finding-2026-06-13-0002 + 0006.
    - ShinyHunters-vs-UNC6240 relationship NOT collapsed; brand
      vs Mandiant-cluster framing maintained.
    - No nation-state attribution introduced.

  HARD RULE 6 binding constraint: PRESERVED. Raw-signal source
  contains zero verbatim quotes over 15 words; this finding does
  not introduce any quotes; data-scope list and attribution
  language are paraphrased per Hard Rule 6.

  HARD RULE 8 binding constraint: First-party Splunk check N/A
  (no IOCs disclosed in source to hunt against). The 19-IOC
  PeopleSoft / UNC6240 sentinel set carried forward across
  flash sweeps remains active for the SEPARATE PeopleSoft
  cluster — that hunt set does NOT extend to this Council of
  Europe substrate because (a) no IOCs disclosed here and
  (b) SW explicitly frames the two campaigns as separate.

source_reliability:
  grade: B
  source_name: "SecurityWeek (Ionut Arghire byline)"
  source_yaml_id: securityweek
  grade_rationale: >
    SecurityWeek is provisional B per source-grades.yaml
    (provisional_since 2026-05-06, awaiting_ratification: true).
    Established track record across the corpus as accurate
    publisher-relay of vendor / actor / advisory primaries.
  provisional: true
  provisional_since: 2026-05-06

credibility:
  grade: 3
  checklist_passed:
    - possibly_true_single_source_uncorroborated_but_b_grade_or_better
    - possibly_true_technical_claims_plausible_but_not_independently_verifiable
  rationale: >
    Grade 3 (Possibly True): single B-grade publisher relay of
    actor self-claim with no Council of Europe acknowledgment,
    no third-party IR firm corroboration, no independent
    telemetry. The actor-cluster activity is consistent with
    ShinyHunters' active 2026 campaign portfolio (PeopleSoft
    extortion + DentaQuest + leak-site doxxing pattern is
    established), so credibility does NOT drop to 4 (Doubtful).
    Grade 2 (Probably True) NOT met because the volume / scope
    claim is uncorroborated and CoE has not acknowledged.

corroboration:
  independent_sources:
    - securityweek
  independent: false  # Single-publisher in-window; no BleepingComputer / THN / SA / Mandiant / Unit 42 corroboration of the CoE-specific claim
  test_passed: >
    Publisher-layer independence FAILS — SW is sole in-window
    publisher. Evidence-basis independence FAILS — ShinyHunters
    self-claim is the only evidence basis; no third-party
    telemetry, no CoE ACK, no IR-firm investigation.
  notes: >
    Council of Europe acknowledgment or second-publisher
    (BleepingComputer / THN / The Record / Reuters / AP /
    Le Monde) relay of the leak-site post would lift the
    procedural-fact layer from C3 to B2. Mandiant or other
    Tier-1 IR firm telemetry on the CoE-specific intrusion
    vector would lift the substantive-claim layer.

first_party_precedence:
  applied: false
  splunk_evidence: >
    No IOCs disclosed in SW article to hunt against. Council of
    Europe is not in Frank's defenseclaw_local environment scope
    (intergovernmental human-rights body in Strasbourg; visibility-
    limited absence by design). Silent Splunk does NOT
    disconfirm at this substrate.

single_source_veto_applied: true  # Applies on quantified-volume claim and substantive-scope claims
wep_ceiling: roughly_even_chance  # On substantive-scope claim (297 GB / 429K files / 10k+ employees); ShinyHunters self-claim through single B-grade publisher relay without CoE ACK
wep_layered:
  shinyhunters_posted_coe_entry_on_tor_leak_site_procedural_fact: likely  # B2 procedural — SW first-party relay of leak-site existence
  threatened_release_deadline_2026_06_16: likely  # B2 procedural
  claimed_volume_297gb_429k_files_substantive_claim: roughly_even_chance  # C3 actor self-claim; single-source veto applies
  claimed_data_scope_payroll_hr_medical: roughly_even_chance  # C3 actor self-claim
  council_of_europe_not_acknowledged_at_publication: likely  # B2 verifiable absence
  dual_campaign_actor_visibility_shinyhunters_concurrently_active: likely  # B2 publisher-attested framing
  council_of_europe_breach_distinct_from_peoplesoft_per_SW_framing: likely  # B2 verifiable absence at SW layer
  no_ad_dib_intersection: very_likely  # Verifiable structural absence
  no_iocs_disclosed: very_likely  # Verifiable absence
  no_cve_attribution_for_coe_vector: very_likely  # Verifiable absence
  no_nation_state_attribution: very_likely  # Verifiable absence
  shinyhunters_unc6240_not_on_roster_new_actor_decision_substrate_strengthening: very_likely  # Verifiable per roster check; substrate continuity

inclusion:
  eligible_for:
    - daily_brief_monitoring  # C3 → monitoring tier only; cluster-context substrate value for actor-visibility framing alongside PeopleSoft deadline coverage
    - weekly_synthesis  # ShinyHunters portfolio pattern + dual-campaign actor visibility candidate for Sunday synthesis
  not_eligible_for:
    - flash  # C3 fails B2 FLASH minimum
    - daily_brief_action  # C3 fails B2 action minimum; no operational urgency
    - actor_profile_update  # C3 fails B2 actor-profile minimum
  flash_eligible: false
  flash_threshold_met: false

graded_at: 2026-06-15T08:08:00-04:00

# ============================================================================
# Cluster metadata
# ============================================================================
cluster:
  topic: "ShinyHunters Tor leak-site self-claim against Council of Europe (~297 GB / 429K files / 10k+ employees payroll + HR + medical; threatened release 2026-06-16); SecurityWeek single-publisher relay; CoE has not acknowledged; dual-campaign actor visibility with separate Oracle PeopleSoft / UNC6240 campaign (BOD 26-04 KEV deadline EOD TODAY 2026-06-15)"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-06-15-am-001-securityweek-shinyhunters-council-of-europe-leak-site-claim-297gb-dual-campaign-actor-visibility
  attribution_claims:
    - claimed_attribution: "ShinyHunters (Tor leak-site self-claim against Council of Europe; ~297 GB / 429K files)"
      claimed_by_sources: [securityweek_relaying_actor_self_claim]
      requires_analyst_review: false
      note: "Actor self-claim preserved verbatim. NOT roster actor. NO Council of Europe acknowledgment. NO third-party IR-firm corroboration. NO nation-state attribution. ShinyHunters-vs-UNC6240 brand-vs-cluster relationship NOT collapsed."
    - claimed_attribution: "ShinyHunters separate Oracle PeopleSoft campaign (UNC6240 per Mandiant; CVE-2026-35273; BOD 26-04 KEV deadline EOD 2026-06-15)"
      claimed_by_sources: [securityweek_referencing_separate_campaign]
      requires_analyst_review: false
      note: "Reference to separate active campaign. Mandiant UNC6240 binding carried forward from finding-2026-06-13-0002 + 0006 unchanged. CoE attack vector NOT linked to PeopleSoft CVE per SW article."

# ============================================================================
# IOC hunt set — NONE DISCLOSED IN SOURCE
# ============================================================================
iocs:
  no_iocs_disclosed_in_source: true
  shinyhunters_tor_leak_site_infrastructure: "General actor-cluster infrastructure pattern; not enumerable as Archimedes-trackable IOC class without specific .onion address / Tor v3 hidden-service hash"
  council_of_europe_breach_mechanism: "Not disclosed by SW; no CVE attribution; no domain / IP / hash / malware family"

# ============================================================================
# Relationship to existing findings
# ============================================================================
relationships:
  related_findings:
    - finding_id: finding-2026-06-13-0002
      relationship: "Cluster-adjacent — ShinyHunters / UNC6240 Mandiant primary on Oracle PeopleSoft active campaign. Brand-vs-Mandiant-cluster relationship maintained. UNC6240 binding to PeopleSoft unchanged; CoE activity is a separate campaign in the same actor-brand portfolio."
    - finding_id: finding-2026-06-13-0006
      relationship: "Cluster-adjacent — Mandiant GTIG primary direct retrieval expanded IOC set for UNC6240 / PeopleSoft. Unchanged by this finding; the 19-IOC sentinel set carried forward across flash sweeps remains active for the PeopleSoft cluster, distinct from this CoE substrate."
    - finding_id: finding-2026-06-12-0001
      relationship: "Cluster-adjacent — CISA KEV CVE-2026-35273 Oracle PeopleSoft 3-day FCEB deadline (NOW EOD TODAY 2026-06-15). This brief is the FINAL pre-deadline coverage window — briefer can carry CoE substrate alongside PeopleSoft deadline retrospective as 'sustained-campaign-class actor active mid-deadline-cycle' context."
    - finding_id: finding-2026-06-10-0012
      relationship: "Cluster-adjacent — BleepingComputer Oracle PeopleSoft ShinyHunters self-attested 300 instances / 100 orgs (gadget chain failed FBI attempt) substrate. Brand consistency: ShinyHunters across PeopleSoft + DentaQuest + CoE."

# ============================================================================
# Open questions for analyst
# ============================================================================
open_questions_for_analyst:
  - "Does the dual-campaign visibility (PeopleSoft + CoE + DentaQuest + Tchap-adjacent) materially affect the operator-deferred /new-actor decision substrate for ShinyHunters / UNC6240? Substrate continues to strengthen but Hard Rule 2 binding on ShinyHunters-vs-UNC6240 brand-vs-cluster relationship pending Mandiant or Unit 42 unified attribution."
  - "Council of Europe ACK watch — second-publisher relay or CoE statement in next 24-48h would lift procedural-fact layer from C3 to B2 and the substantive-volume claim from roughly_even_chance to likely."
  - "Is the 2026-06-16 threatened release deadline a leak-site negotiating posture or a hard data-drop deadline? Pattern analysis across prior ShinyHunters operations (DentaQuest cadence) may calibrate expectation."

analyst_review_required: false  # C3 monitoring tier; no SAT-ACH / SAT-KAC trigger conditions; substrate cluster-context only
red_team_review_required: false  # WEP ceiling roughly_even_chance on substantive claim, likely on procedural facts — does not meet very_likely red-team invocation floor

# ============================================================================
# Lifecycle
# ============================================================================
tlp: CLEAR
published_in_briefs:
  - 2026-06-15-morning
retracted: false
retraction_brief_id: null
---

# ShinyHunters Tor Leak-Site Self-Claim Against Council of Europe — Single-Publisher Relay, No CoE ACK, Dual-Campaign Actor Visibility

## Summary

SecurityWeek (Ionut Arghire) relays ShinyHunters' Tor leak-site
self-claim against the Council of Europe (~297 GB / 429K files /
payroll + HR + medical data on 10,000+ employees 2011-2026;
threatened release deadline 2026-06-16). Council of Europe has
not publicly acknowledged the incident. The SW article frames
this as SEPARATE from ShinyHunters' Oracle PeopleSoft / UNC6240
campaign (CVE-2026-35273; BOD 26-04 KEV deadline EOD TODAY
2026-06-15) — dual-campaign actor visibility, not same-vector
activity. Cluster anchors C3 / WEP roughly_even_chance on the
substantive volume claim (actor self-claim through single
B-grade publisher relay; single-source veto applies); WEP likely
on procedural-fact layer (leak-site post exists, threatened
release deadline, CoE non-acknowledgment). No A&D / DIB
intersection. No IOCs disclosed. No nation-state attribution.
ShinyHunters and UNC6240 remain off the 24-actor `_roster.yaml`;
operator-deferred /new-actor decision substrate continues to
strengthen but is not changed materially by this surface.

## Sources

### SecurityWeek (securityweek, digraph B)

- URL: https://www.securityweek.com/shinyhunters-claims-council-of-europe-hack/
- Published: 2026-06-15T10:44:29+00:00 (06:44 EDT)
- Byline: Ionut Arghire
- Key claim: ShinyHunters posted a Council of Europe entry on its
  Tor-based leak site Sunday 2026-06-15, claiming approximately
  297 GB across 429,000+ files with threatened release by
  2026-06-16; Council of Europe has not publicly acknowledged;
  claim is separate from ShinyHunters' Oracle PeopleSoft campaign.

## Claimed scope (per ShinyHunters leak-site post, via SW relay)

- ~297 GB across 429,000+ files
- Payroll data for 10,000+ employees, spanning 2011 through 2026
- 14,000+ CVs
- Contract and purchase order records
- Absence and illness reports
- Bank account information
- Performance evaluations
- Employee names, IDs, addresses, phone numbers, dates of birth
- Tax and social security information
- Medical records

Affected departments per leak-site claim: HR, the Secretariat,
the Parliamentary Assembly, the European Directorate for the
Quality of Medicines & HealthCare (EDQM).

All scope data is actor self-claim through single B-grade
publisher relay. Council of Europe has not publicly acknowledged.

## Dual-campaign actor visibility

SW explicitly references ShinyHunters' SEPARATE Oracle PeopleSoft
zero-day campaign — i.e., the UNC6240 / CVE-2026-35273 cluster
currently in the CISA BOD 26-04 KEV catalog with FCEB deadline
EOD TODAY Sunday 2026-06-15. The Council of Europe activity is
framed as a distinct campaign per SW; no CVE-vector cross-link
is asserted.

Visible ShinyHunters portfolio across the past week (corpus
substrate):

- Oracle PeopleSoft / UNC6240 mass theft (finding-2026-06-13-0002 +
  0006, BOD 26-04 KEV deadline EOD 2026-06-15)
- DentaQuest 2.6M (2026-06-12 PM substrate; EE health-sector cluster)
- Council of Europe (this finding, 2026-06-15)

ShinyHunters and UNC6240 are not on the 24-actor `_roster.yaml`
as of 2026-05-10. Mandiant binds UNC6240 to the PeopleSoft
activity (finding-2026-06-13-0002); SW uses the ShinyHunters
leak-site brand consistently across all three campaigns. The
brand-vs-Mandiant-cluster relationship is an actor-profiler
decision pending operator review; this grader finding does NOT
collapse the two identities. Hard Rule 2 binding.

## Technical detail

- **Breach mechanism**: NOT disclosed in SW article. No CVE
  attribution. No domain, IP, hash, or malware family disclosed.
- **Leak-site infrastructure**: Tor-based hidden service; specific
  .onion address not relayed by SW. General actor-cluster
  infrastructure pattern, not enumerable as a discrete IOC.
- **Affected entity**: Council of Europe — 46-state intergovernmental
  human-rights body headquartered in Strasbourg, France. Not a US
  federal contractor, not in CMMC / ITAR / DFARS supply chain, not
  on `infrastructure/watchlists/aerospace-defense.yaml`. EDQM is
  pharma-regulatory under Council of Europe, not A&D-prime.

## IOCs surfaced

None disclosed in source article. The 19-IOC sentinel set
carried forward across recent flash sweeps remains active for
the SEPARATE PeopleSoft / UNC6240 cluster, distinct from this
Council of Europe substrate.

## Relationship to existing findings

- finding-2026-06-13-0002 (Mandiant UNC6240 / ShinyHunters
  Oracle PeopleSoft active campaign) — actor-brand-adjacent,
  cluster-distinct campaign.
- finding-2026-06-13-0006 (Mandiant GTIG expanded IOC set on
  same UNC6240 / PeopleSoft cluster) — sentinel set carried
  forward unchanged.
- finding-2026-06-12-0001 (CISA KEV CVE-2026-35273 3-day FCEB
  deadline, EOD TODAY 2026-06-15) — briefer can carry this
  finding's dual-campaign substrate alongside PeopleSoft
  deadline retrospective.
- finding-2026-06-10-0012 (BleepingComputer ShinyHunters
  PeopleSoft self-attested 300 instances / 100 orgs) — same
  actor-brand, distinct PeopleSoft campaign.

## Open questions for analyst / actor-profiler

1. Council of Europe ACK watch — second-publisher relay or CoE
   statement in next 24-48h would lift procedural-fact layer
   from C3 to B2 and substantive-volume claim from
   roughly_even_chance to likely.
2. Does the dual-campaign visibility (PeopleSoft + CoE +
   DentaQuest) materially affect the operator-deferred
   /new-actor decision substrate for ShinyHunters / UNC6240?
3. Is the 2026-06-16 threatened release deadline a negotiating
   posture or a hard data-drop deadline? Pattern analysis
   across prior ShinyHunters operations may calibrate the
   expectation.
