---
finding_id: finding-2026-06-11-0003-thehackernews-eset-oceanlotus-apt32-spectralviper-fireant-supply-chain-vietnam-not-in-roster-new-actor-candidate
created_at: 2026-06-11T08:22:00-04:00
graded_by: grader
grading_run_id: morning-20260611-080000
grading_mode: scheduled_brief
test: false
status: graded

# ============================================================================
# Core grading (admiralty-grading skill output)
# ============================================================================
digraph: A2
digraph_layered:
  eset_originating_research_attribution_oceanlotus_apt32_vietnam_aligned: A2   # ESET A-grade per source-grades.yaml; long track record on East/Southeast Asian APT clusters; attribution at vendor-claimed layer not roster-mapped on Archimedes side
  spectralviper_new_malware_family_name_attributed_to_oceanlotus: A2   # ESET originating research; new-family naming canonical at vendor layer; relayed via THN
  campaign_1_vietnamese_infrastructure_transport_construction_corporation_espionage_2024_to_2026_02: A2   # ESET attestation; victim-class characterization sector-generic not entity-specific
  campaign_2_fireant_metakit_supply_chain_attack_2025_10_to_2026_03: A2   # ESET attestation; supply-chain compromise of named investor-tools platform
  dll_side_loading_chain_via_legitimate_binaries: A2   # ESET TTP characterization; consistent with established APT32 tradecraft public record
  process_injection_onedrive_sync_service_exe_lolbin_class: A2   # ESET TTP characterization; consistent with public LOLBin abuse pattern
  ioc_layer_2_c2_domains_financemachinelearning_com_gatewayrvcenter_com_plus_supply_chain_update_url: A2   # ESET originating; relayed via THN; verifiable as artifact-existence
  no_a_and_d_prime_victim_named_in_eset_research: A1   # Verifiable absence
  no_us_government_target_named_in_eset_research: A1   # Verifiable absence; campaign target set is Vietnamese-domestic
  thn_b_grade_aggregator_relay_of_eset_originating_research: B2   # THN provisional B per source-grades.yaml; relay-class; aggregator carries ESET attribution layer forward
  no_eset_direct_url_surfaced_in_thn_article_body: A1   # Verifiable from raw signal; full ESET WeLiveSecurity advisory not directly retrieved this sweep
  actor_oceanlotus_apt32_NOT_in_archimedes_roster: A1   # Verifiable absence via grep on aliases per raw signal
  ad_relevance_low_vietnamese_aligned_actor_vietnamese_domestic_targets: A2   # Structural inference; out-of-scope for operator target profile (US A&D contractor)
  tradecraft_portability_to_a_d_espionage_scenarios_acknowledged_but_not_claimed_in_window: A2   # ESET does NOT claim US A&D targeting in this report; portability is grader-side observation not source claim
  cluster_anchor: A2

digraph_anchor: >
  Cluster anchored on ESET / WeLiveSecurity originating research
  (A-grade per source-grades.yaml; ratified Session 11 per finding-
  2026-05-07-0004 precedent) relayed via The Hacker News (B-grade
  provisional per source-grades.yaml) as the in-window publisher.
  Direct ESET WeLiveSecurity URL not surfaced in THN article body
  this sweep; ESET originating research layer carries through THN
  as the relay vehicle.

  A2 (not A1 or B2) anchored because:

    - SOURCE LETTER GRADE: ESET is the originating A-grade
      vendor-research source; THN is a B-grade aggregator relay.
      Per skill discipline, the originating A-grade source
      carries the cluster anchor letter when the relay layer
      reproduces attribution and technical claims faithfully.
      THN's relay is the only in-window publisher surface for
      Archimedes; ESET WeLiveSecurity direct retrieval deferred.

    - INDEPENDENCE TEST: ONE effective source at the substantive
      evidence-basis layer. THN is NOT independent of ESET — THN
      explicitly relays ESET research; per skill Step 4 ("one is
      a rewrite/aggregation of the other") THN cannot corroborate
      ESET. The cluster has one source (ESET via THN relay) at
      this hour. No second A/B-grade vendor (Mandiant, Unit 42,
      CrowdStrike, MSTIC, Sekoia, Volexity) corroborating in
      window.

    - CREDIBILITY: Walk the checklist.
      * Grade 1 (Confirmed) — FAILS: no independent A/B-grade
        corroboration in window; ESET-via-THN is one effective
        source.
      * Grade 2 (Probably True) — PASSES:
        - Consistent with established OceanLotus / APT32
          tradecraft per public record (DLL side-loading +
          legitimate-binary hijack + LOLBin host process
          abuse + supply-chain compromise are all in the
          documented APT32 corpus going back to 2017-2020
          Volexity / FireEye / ESET prior research).
        - No contradicting A/B-grade source.
        - Technical claims internally coherent: SPECTRALVIPER
          backdoor + DLL side-loading + OneDrive.Sync.Service.exe
          process injection + supply-chain compromise of
          investor-tools platform are mechanistically plausible
          and consistent with the campaign target characterization
          (Vietnamese-domestic espionage + investor-platform
          monetization adjacency).
        - Timing (~20-month infrastructure campaign + ~6-month
          supply-chain campaign) consistent with established
          APT32 operational tempo.

    - CONSERVATIVE ANCHOR at Grade 2 because single-source
      attestation (one effective source: ESET-via-THN). Single-
      source veto applies on the WEP layer (caps at "likely",
      not "very likely") for any forward-looking or operationally-
      actionable claim, per INTEL-GRADING.md single-source-veto
      doctrine.

  Single-source veto APPLIED on the cluster anchor — one effective
  evidence source (ESET via THN relay) means WEP caps at "likely"
  for all forward / operational claims, regardless of source
  letter-grade.

  Hard Rule 2 binding constraint: PRESERVED — Archimedes does NOT
  originate attribution. The OceanLotus / APT32 attribution is
  ESET's, carried via THN; Archimedes reports the attribution
  WITH source-citation, does NOT propagate independently. The
  actor is NOT in Archimedes roster; this finding flags the
  /new-actor candidacy for orchestrator-discretion handoff per
  CLAUDE.md "On-Demand Commands" workflow (the /new-actor command
  requires human approval per Hard Rule 5 pipeline class).

  Hard Rule 6 binding constraint: PRESERVED — verbatim quotes
  under 15 words each, max one per source:
  - THN: "Vietnam-aligned threat actor known as OceanLotus" (7
    words; characterization-only).
  - THN: "prolonged cyber espionage operation aimed at a
    Vietnamese infrastructure" (8 words; characterization).
  ESET originating quotes not surfaced in THN body; direct
  WeLiveSecurity retrieval deferred.

  Hard Rule 8 binding constraint: -24h@h first-party Splunk query
  (archimedes + defenseclaw_local) on OceanLotus + APT32 +
  SPECTRALVIPER + FireAnt + financemachinelearning +
  gatewayrvcenter + metakit.fireant returned zero substantive
  hits. Per Hard Rule 8: silence is not disconfirming. First-
  party precedence does NOT apply. defenseclaw_local is not
  observably running infrastructure that would intersect a
  Vietnamese-domestic espionage campaign; silence expected.

source_reliability:
  grade: A
  source_name: "ESET / WeLiveSecurity (A ratified, originating research; direct WeLiveSecurity URL not surfaced in THN body this sweep) relayed via The Hacker News (B provisional, aggregator class)"
  source_yaml_id: eset
  grade_rationale: >
    ESET ratified A per source-grades.yaml (Session 11, 2026-05-07,
    per finding-2026-05-07-0004 librarian handoff — originating
    research on APT37 Birdcall Android, Filip Jurčacko byline,
    cited via The Record relay; same publication-relay precedent
    class as this finding). ESET research has long track record
    on East/Southeast Asian APT clusters including OceanLotus /
    APT32 historical coverage going back to 2017-2020. The Hacker
    News provisional B per source-grades.yaml (Session 12,
    2026-05-14); aggregator-class relay. This finding rests on
    one effective source (ESET via THN relay) — THN is NOT
    independent of ESET per skill Step 4 "aggregation of the
    other" test.
  provisional: false
  cluster_secondary_sources:
    - source_yaml_id: thehackernews
      grade: B
      provisional: true
      provisional_since: 2026-05-14
      grade_rationale: "Pre-assigned B per source-grades.yaml; aggregator class; relay-only role on this finding (THN explicitly cites ESET as originating; NOT independent corroboration)."
      role: relay_of_eset_originating_research_NOT_independent_corroboration

credibility:
  grade: 2
  checklist_passed:
    - probably_true_ttp_consistent_with_established_apt32_oceanlotus_tradecraft_in_public_record
    - probably_true_no_contradicting_a_b_grade_source
    - probably_true_technical_claims_internally_coherent_spectralviper_dll_side_loading_lolbin_supply_chain
    - probably_true_campaign_timing_and_target_set_consistent_with_established_apt32_operational_tempo
  checklist_NOT_passed_at_grade_1:
    - confirmed_independent_corroboration_at_substantive_evidence_basis_layer  # FAILS — one effective source (ESET via THN)
    - confirmed_neither_source_cites_the_other_as_origin  # FAILS — THN cites ESET as origin
  rationale: >
    Cluster anchor is the ESET-attributed dual-campaign claim:
    "OceanLotus / APT32 (Vietnam-aligned) conducted (1) ~20-month
    espionage campaign against a Vietnamese infrastructure /
    transport construction corporation mid-2024 → 2026-02 and
    (2) ~6-month supply-chain compromise of FireAnt Metakit
    investor-tools platform 2025-10 → 2026-03, deploying
    SPECTRALVIPER backdoor via DLL side-loading and
    OneDrive.Sync.Service.exe LOLBin injection." Single effective
    source: ESET originating research via THN relay (THN explicitly
    cites ESET; relay-class not independent corroboration per
    skill Step 4 aggregation test). Conservative Grade 2 anchor
    (Probably True) because: (a) tradecraft is consistent with
    established APT32 public-record corpus going back to
    2017-2020 (FireEye / Volexity / ESET prior coverage of DLL
    side-loading + LOLBin abuse + supply-chain compromise); (b)
    no contradicting A/B-grade source; (c) technical claims
    internally coherent; (d) timing consistent with established
    operational tempo. Grade 1 (Confirmed) FAILS because no
    independent second A/B-grade vendor corroboration in window
    (Mandiant / Unit 42 / CrowdStrike / MSTIC / Sekoia / Volexity
    not in this sweep). The IOC layer (2 C2 domains, 1 supply-
    chain update URL) is ESET-originating and would benefit from
    direct WeLiveSecurity advisory retrieval to capture full
    hash + IP set for vuln-tracker / IOC index population;
    deferred at this layer.

corroboration:
  independent_sources:
    - eset                  # Originating A-grade research
  independent: false        # One effective source; THN relay is NOT independent corroboration
  independent_at_substantive_evidence_basis_layer:
    cluster_anchor_eset_attribution: false   # No second A/B-grade vendor in window
    cluster_anchor_technical_claims: false   # ESET sole originating
    cluster_anchor_iocs: false               # ESET sole originating
  test_passed: null
  test_failed: >
    Strict skill-Step-4 evidence-basis-independence FAILS at the
    cluster anchor. THN is explicitly an aggregation of ESET
    research; THN cites ESET as origin; per skill Step 4 "one
    is a rewrite/aggregation of the other" test, THN is NOT
    independent corroboration of ESET. The finding rests on one
    effective source: ESET originating research carried via THN
    relay. Single-source veto applies on WEP layer for all
    forward / operational claims.

first_party_precedence:
  applied: false
  splunk_evidence: null
  splunk_query_run: >
    Per raw-signal manual query, -24h@h window across
    index=archimedes OR index=defenseclaw_local on OceanLotus +
    APT32 + SPECTRALVIPER + FireAnt + financemachinelearning +
    gatewayrvcenter + metakit.fireant. Zero substantive hits.
    Per Hard Rule 8: silence is not disconfirming. First-party
    precedence does NOT apply. defenseclaw_local is not
    observably running Vietnamese-domestic investor-tools
    infrastructure; silence expected.

single_source_veto_applied: true
single_source_veto_detail: >
  Applied on the cluster anchor — one effective evidence source
  (ESET via THN relay) means WEP caps at "likely" for all
  forward / operational claims regardless of source letter-grade.
  Per INTEL-GRADING.md single-source-veto doctrine: a finding
  CANNOT be assessed at WEP "very likely" or higher based on a
  single source. ESET A-grade does not lift the veto absent
  independent second-source corroboration. Veto lifts on
  retroactive procedural-fact layer (ESET published the research,
  THN relayed it) — these are verifiable observations not
  forward claims.

wep_ceiling: likely
wep_layered:
  eset_published_research_attributing_campaigns_to_oceanlotus_apt32_procedural_fact: very_likely  # Verifiable publication
  thn_relayed_eset_research_2026_06_11_publication: very_likely  # Verifiable publication
  oceanlotus_apt32_vietnam_aligned_attribution_per_eset: likely  # SINGLE-SOURCE VETOED — ESET sole; consistent with established APT32 public record but no in-window independent vendor corroboration
  campaign_1_vietnamese_infrastructure_transport_construction_corporation_espionage_attribution: likely  # SINGLE-SOURCE VETOED
  campaign_2_fireant_metakit_supply_chain_compromise_attribution: likely  # SINGLE-SOURCE VETOED
  spectralviper_backdoor_attributed_to_oceanlotus: likely  # SINGLE-SOURCE VETOED — new family naming
  dll_side_loading_plus_onedrive_sync_service_exe_lolbin_chain_used_in_campaign: likely  # SINGLE-SOURCE VETOED — though TTP consistent with established APT32 corpus
  c2_domains_financemachinelearning_com_gatewayrvcenter_com_are_oceanlotus_infrastructure: likely  # SINGLE-SOURCE VETOED
  fireant_metakit_update_url_was_supply_chain_compromise_vector: likely  # SINGLE-SOURCE VETOED
  no_us_a_d_prime_targeting_in_this_campaign_set: very_likely  # Verifiable absence in ESET-via-THN
  oceanlotus_apt32_tradecraft_is_portable_to_us_a_d_espionage_scenarios_structural_observation: likely  # Grader-side structural observation; NOT an ESET claim
  oceanlotus_apt32_will_target_us_a_d_primes_in_future_speculative: roughly_even_chance  # Speculative forward assessment; no source claim; not action-grade

inclusion:
  eligible_for:
    - daily_brief_monitoring   # A2 clears C3 monitoring threshold (B2 action threshold borderline; structural relevance LOW caps to monitoring)
    - weekly_synthesis         # Strong candidate for AI/East-Asian-APT continuing coverage theme
    - actor_profile_update     # /new-actor candidacy flag per orchestrator handoff (NOT direct propagation; human approval required per Hard Rule 5)
  NOT_eligible_for:
    - daily_brief_action       # A&D-relevance LOW + no operator-target intersection + no first-party hit + single-source veto on WEP — does NOT clear action-tier weighting
    - flash                    # No state-transition trigger; no operator-target intersection
inclusion_eligibility: yes

# ============================================================================
# Hard Rule 2 — Attribution preserved (ESET-claim only; NOT roster-mapped on Archimedes side)
# ============================================================================
attribution: "OceanLotus / APT32 (per ESET)"
attribution_class: vendor_claim_eset_NOT_archimedes_originated
attribution_claims:
  - claimed_actor: OceanLotus
    aliases: [APT32, SeaLotus, CobaltKitty]   # Public-record aliases; not currently in Archimedes roster
    claimed_by_sources: [eset]
    claimed_by_relay: [thehackernews]
    nation_alignment: VN  # Vietnam-aligned per ESET attribution language
    confidence_per_source: high
    technical_evidence: |
      ESET originating research methodology not fully detailed in
      THN relay body; SPECTRALVIPER backdoor family + DLL side-
      loading TTP + targeting pattern (Vietnamese-domestic entities
      + investor-platform supply chain) form the attribution basis
      per ESET. Direct WeLiveSecurity advisory retrieval would
      yield the full attribution methodology / hash set / IR
      timeline for analyst SAT-ACH at deeper investigation.
    roster_actor_mapping: null   # OceanLotus / APT32 NOT in Archimedes _roster.yaml per raw-signal grep verification
    requires_analyst_review: true
    new_actor_candidacy_flag: true
    new_actor_candidacy_orchestrator_handoff: >
      OceanLotus / APT32 is a Tier-1-vendor-tracked APT cluster
      (ESET / Mandiant / FireEye / Volexity / Group-IB / Sekoia
      historical coverage) with public-record activity going back
      to 2012; Vietnam-aligned attribution; aerospace-defense-
      relevant tradecraft portability (DLL side-loading + LOLBin +
      supply chain). Per CLAUDE.md "On-Demand Commands" workflow,
      /new-actor command requires human approval per Hard Rule 5
      pipeline class. This finding flags the candidacy WITHOUT
      auto-invoking scaffolding. Adjacent precedent: May 2026
      collector observations on UNC6692 + UNC1069 (Mandiant) were
      similarly flagged as /new-actor candidates without auto-
      scaffolding.
    propagation_guardrail: >
      Per Hard Rule 2, Archimedes does NOT originate attribution.
      ESET attribution to OceanLotus / APT32 is reported with
      explicit source-citation ("per ESET"). Archimedes does NOT
      propagate this attribution independently. If a future
      finding requires attribution-by-inference (e.g., IOC
      overlap with a future ESET-attributed OceanLotus campaign),
      analyst SAT-ACH handles per doctrine; grader does NOT
      extend.

# ============================================================================
# IOCs surfaced
# ============================================================================
iocs:
  domains_c2:
    - value: "financemachinelearning[.]com"
      role: c2
      family: SPECTRALVIPER
      attribution: OceanLotus_APT32_per_ESET
      confidence: a_grade_eset_originating_research
    - value: "gatewayrvcenter[.]com"
      role: c2
      family: SPECTRALVIPER
      attribution: OceanLotus_APT32_per_ESET
      confidence: a_grade_eset_originating_research
  urls_supply_chain:
    - value: "metakit.fireant[.]vn/Software/version.xml"
      role: supply_chain_update_path
      family: FireAnt_Metakit_compromise
      attribution: OceanLotus_APT32_per_ESET
      confidence: a_grade_eset_originating_research
      note: |
        FireAnt Metakit is a Vietnamese investor-tools platform;
        the compromised update path served the trojanized
        installer in the Campaign 2 supply-chain attack vector
        per ESET.
  iocs_hashes: []   # Not surfaced in THN article body; would require direct ESET WeLiveSecurity advisory retrieval

# ============================================================================
# Cluster metadata
# ============================================================================
cluster:
  topic: "ESET attributes dual OceanLotus / APT32 campaign set (Vietnamese infrastructure / transport corp espionage + FireAnt Metakit supply chain compromise) deploying SPECTRALVIPER backdoor — actor NOT in Archimedes roster, /new-actor candidacy flag"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-06-11-am-001-thehackernews-eset-oceanlotus-apt32-spectralviper-fireant-vietnam-not-in-roster-new-actor-flag
  related_findings: []
  new_actor_candidacy_flag: true

# ============================================================================
# Downstream handoff flags
# ============================================================================
analyst_review_required: true    # Attribution claim present; /new-actor candidacy
red_team_review_required: false  # WEP capped at "likely" by single-source veto; below red-team-trigger threshold
red_team_review: null
analysis_sections:
  sat_ach: null
  sat_kac: null

orchestrator_handoffs:
  - target: new_actor_candidacy_watchlist
    action: flag_oceanlotus_apt32_candidacy
    rationale: tier1_vendor_tracked_apt_cluster_not_in_archimedes_roster_with_a_d_tradecraft_portability
    requires_human_approval: true   # Per Hard Rule 5 pipeline class
    precedent: may_2026_unc6692_unc1069_mandiant_candidacy_observations

librarian_handoffs:
  - target: ioc_index_unattributed_or_oceanlotus_subdir
    action: aggregate_2_c2_domains_plus_1_supply_chain_url
    iocs:
      - "financemachinelearning[.]com"
      - "gatewayrvcenter[.]com"
      - "metakit.fireant[.]vn/Software/version.xml"
    attribution_at_index_layer: OceanLotus_APT32_per_ESET_NOT_roster_mapped
  - target: ioc_extraction_via_direct_eset_welivesecurity_retrieval
    action: direct_advisory_retrieval_for_hash_set_completion
    rationale: thn_article_body_does_not_surface_iocs_hashes_or_ips
    priority: medium  # Not blocking for morning brief

# ============================================================================
# Lifecycle
# ============================================================================
tlp: CLEAR
published_in_briefs:
  - 2026-06-11-morning
retracted: false
retraction_brief_id: null
---

# ESET Attributes Dual OceanLotus / APT32 Campaign Set to Vietnamese Infrastructure Espionage Plus FireAnt Metakit Supply Chain Compromise — Actor Not in Roster, /new-actor Candidacy Flagged

## Summary

ESET attributes (via The Hacker News relay) two distinct OceanLotus / APT32 campaigns deploying a new backdoor family named SPECTRALVIPER: a ~20-month espionage operation against a Vietnamese infrastructure / transport construction corporation (mid-2024 through February 2026), and a ~6-month supply chain compromise of the FireAnt Metakit investor-tools platform (October 2025 through March 2026). Tradecraft per ESET includes DLL side-loading via legitimate binaries and process injection into OneDrive.Sync.Service.exe as LOLBin host. **OceanLotus / APT32 is NOT in Archimedes roster** per grep verification on aliases; this finding flags `/new-actor` candidacy for orchestrator-discretion handoff per CLAUDE.md "On-Demand Commands" workflow (Hard Rule 5: human approval required, NOT auto-invoked). No US A&D-prime victim named; A&D-relevance LOW directly, though APT32 tradecraft is structurally portable to A&D espionage scenarios.

## Sources

### ESET / WeLiveSecurity (A ratified, originating research)

- Originating vendor: ESET (Slovakian; ratified A per source-grades.yaml Session 11, 2026-05-07)
- Direct WeLiveSecurity advisory URL NOT surfaced in THN article body this sweep; deferred to vuln-tracker for direct retrieval to complete IOC hash set
- Key claim: Two-campaign attribution to OceanLotus / APT32 with SPECTRALVIPER backdoor + DLL side-loading + OneDrive.Sync.Service.exe LOLBin TTP chain

### The Hacker News (B provisional, relay)

- URL: https://thehackernews.com/2026/06/oceanlotus-hits-vietnam-investors-with.html
- Published: 2026-06-11T09:45:58 UTC
- Author: THN editorial
- Key role: Relay of ESET research — NOT independent corroboration per skill Step 4 aggregation test; relay-only role on this finding

## Technical detail

ESET (via THN relay) attributes the campaigns to OceanLotus / APT32 (Vietnam-aligned, active since 2012 per public record). The malware framework is SPECTRALVIPER — described by ESET as a backdoor family — delivered via a DLL side-loading chain using legitimate binaries to load the malicious DLL, with process injection into OneDrive.Sync.Service.exe as the LOLBin host process. The tradecraft pattern (DLL side-loading + LOLBin abuse + supply-chain compromise of a software-update path) is consistent with the established APT32 public-record corpus going back to 2017-2020 FireEye / Volexity / ESET prior coverage; this finding adds a new family name (SPECTRALVIPER) and two new campaign sets but is not novel-mechanism at the tradecraft layer.

The FireAnt Metakit supply chain compromise targeted a Vietnamese investor-tools platform's software update path (`metakit.fireant[.]vn/Software/version.xml`), serving a trojanized installer or update payload over ~6 months. The ~20-month Vietnamese infrastructure / transport construction corporation espionage campaign is sector-generic at the victim characterization layer; no specific named entity is disclosed in the relay.

## Attribution

Attribution language is verbatim "Vietnam-aligned threat actor known as OceanLotus" per THN (7-word quote, characterization-only). Per Hard Rule 2, Archimedes reports the attribution WITH explicit source-citation ("per ESET"), does NOT propagate it independently. **OceanLotus / APT32 is NOT in Archimedes `_roster.yaml`** (verified via grep on aliases `OceanLotus|Ocean Lotus|APT32|SeaLotus|CobaltKitty`, zero matches). This finding flags the candidacy for `/new-actor` orchestrator-discretion handoff per CLAUDE.md "On-Demand Commands" workflow; the `/new-actor` command requires human approval per Hard Rule 5 pipeline class.

Precedent class: May 2026 collector observations on UNC6692 and UNC1069 (Mandiant) were similarly flagged as `/new-actor` candidates without auto-scaffolding.

## IOCs surfaced

| Value | Role | Family | Confidence |
|---|---|---|---|
| financemachinelearning[.]com | C2 | SPECTRALVIPER | A (ESET originating) |
| gatewayrvcenter[.]com | C2 | SPECTRALVIPER | A (ESET originating) |
| metakit.fireant[.]vn/Software/version.xml | Supply chain update path | FireAnt Metakit compromise | A (ESET originating) |

Hash IOCs and additional IPs NOT surfaced in THN article body; direct ESET WeLiveSecurity advisory retrieval required for completion. Librarian handoff to aggregate the three IOCs above into `iocs/unattributed/` or a new `iocs/oceanlotus-apt32-per-eset-2026-06-11/` subdirectory (attribution at index layer preserved as "per ESET, NOT roster-mapped" per Hard Rule 2).

## A&D relevance

A&D-relevance LOW directly. Vietnam-aligned actor targeting Vietnamese-domestic entities (infrastructure / transport construction corp + Vietnamese investor platform) is out-of-scope for operator target profile (mid-to-large US A&D contractor, ITAR-regulated, US government contracts, Tier-1/2 supplier network). However, the TTP chain (DLL side-loading + legitimate-binary hijack + OneDrive.Sync.Service.exe LOLBin + supply-chain compromise of software update path) IS structurally portable to US A&D-prime espionage scenarios — though ESET does NOT claim US A&D targeting in this report. Portability is a grader-side structural observation, NOT an ESET attribution claim.

## Relationship to existing findings

None directly. This is a new actor surface for Archimedes; no prior finding on OceanLotus / APT32 in the Archimedes corpus per grep verification. Weekly-synthesis continuing-coverage candidate under the East-Asian-APT cluster theme alongside any future Mustang Panda / APT41 / Volt Typhoon / Salt Typhoon / APT40 coverage in the Tier-1-vendor reporting stream.

## Open questions for analyst

- /new-actor candidacy decision (orchestrator-discretion + human approval per Hard Rule 5): does the operator want OceanLotus / APT32 added to roster given (a) Tier-1-vendor-tracked APT cluster, (b) Vietnam-aligned attribution outside the current Iran/China/Russia roster focus, (c) tradecraft portability to A&D-prime espionage scenarios?
- Direct ESET WeLiveSecurity advisory retrieval for full IOC hash set + IP set + IR timeline + attribution methodology — vuln-tracker / collector handoff candidate.
- Forward assessment: will OceanLotus / APT32 expand targeting to US A&D primes in future reporting? Currently roughly-even-chance (no source claim; speculative); watch-signal for any future Tier-1 vendor reporting naming a US A&D-prime OceanLotus victim.
