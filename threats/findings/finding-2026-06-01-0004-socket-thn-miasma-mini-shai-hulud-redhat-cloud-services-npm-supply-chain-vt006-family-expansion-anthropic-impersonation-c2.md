---
finding_id: finding-2026-06-01-0004-socket-thn-miasma-mini-shai-hulud-redhat-cloud-services-npm-supply-chain-vt006-family-expansion-anthropic-impersonation-c2
created_at: 2026-06-01T16:08:00-04:00
graded_by: grader
grading_run_id: afternoon-20260601-160000
grading_mode: scheduled_brief
test: false

# Core grading (admiralty-grading skill output)
digraph: B2
digraph_layered:
  mini_shai_hulud_family_mechanism_class_identification_install_time_execution_credential_harvest_cicd_target_encrypted_exfil_self_propagate: A2  # Socket verbatim — A-grade-corpus-corroborated against VT-006 origination; mechanism class consistent with VT-006 family
  affected_ecosystem_npm_registry_redhat_cloud_services_namespace: B2                # Socket primary; THN relay confirms
  eight_named_redhat_cloud_services_packages_compromised: B2                          # Socket primary (only one version explicitly named per primary body); THN relay enumerates eight
  redhat_cloud_services_chrome_2_3_1_explicitly_versioned: B2                         # Socket primary directly retrieved
  c2_exfiltration_api_anthropic_com_impersonation_v1_api_port_443: B2                 # Socket primary; novel tradecraft layer; impersonation of legitimate Anthropic API
  fallback_exfiltration_github_repos_with_miasma_spreading_blight_description: B2     # THN relay attestation; not in directly-retrieved Socket body
  sha256_hashes_three_published_tarball_payload_decrypted_payload: B2                 # Socket primary publishes
  encryption_layer_aes_128_gcm_aes_256_gcm_rsa_oaep_wrapping: B2                      # Socket primary
  string_signature_ifyouinvalidatethistoken_internal_payload_string: B2               # Socket primary
  detection_timeline_2026_05_29_first_detection_2026_06_01_disclosure: B3             # THN-relay-only; not in directly-retrieved Socket body
  vt006_lineage_extension_third_documented_ecosystem_after_tanstack_and_nx_console: A1  # Internal corpus state verifiable against VT-006 + VT-009
  socket_explicitly_declines_miasma_attribution_to_teampcp_attribution_remains_unclear: A1   # Socket verbatim; Hard Rule 2 compliance positive
  teampcp_open_sourced_shai_hulud_tooling_lineage_only_NOT_miasma_attribution: A1     # Socket verbatim
  multi_firm_co_attribution_in_thn_relay_NOT_directly_retrieved_in_socket_primary: B3 # THN-relay-only — quality-of-evidence concern; Wiz/JFrog/MSTIC/OX/SafeDep/StepSecurity/Aikido named in THN but not visible in Socket primary body
  microsoft_mstic_no_blog_post_identified_at_sweep_time: A1                           # Verifiable absence
  red_hat_no_incident_response_statement_at_sweep_time: A1                            # Verifiable absence
  no_a_and_d_prime_named_victim_or_sector_specific_targeting: A1                      # Verifiable absence
  packages_unpublished_or_revoked_per_socket_downstream_impact_language: B2           # Socket-published; not vendor-independently-confirmed
  structural_ad_relevance_lower_than_vt006_redhat_cloud_services_no_aviation_specific_packages: B2  # Grader-side structural inference; consistent with vuln-tracker corpus posture
  no_new_cve_assigned_to_miasma_at_disclosure: A1                                     # Verifiable absence in NVD + Socket primary
  cluster_anchor: B2

digraph_anchor: >
  Cluster digraph B2 anchored on Socket Research Team originating
  research post (provisional B per source-grades.yaml, first cited
  2026-05-14) with The Hacker News (Ravie Lakshmanan, provisional B)
  relay disclosing the "Miasma" campaign — a Mini Shai-Hulud family
  supply-chain compromise of at least seven @redhat-cloud-services
  npm packages with credential-stealing, CI/CD-targeting, encrypted-
  exfiltrating, self-propagating worm payloads. Campaign disclosed
  2026-06-01; first detection per THN relay dates to 2026-05-29.
  Socket EXPLICITLY declines to attribute the Miasma campaign to
  any specific actor — TeamPCP is named only as the open-sourcer
  of the underlying tooling lineage, not as the Miasma operator.

  B2 (not A2) anchored because:
    - Source-reliability LETTER grade is B per source-grades.yaml on
      both Socket (provisional B since 2026-05-14) and THN (provisional
      B). This raw-signal IS a direct retrieval of Socket's primary
      URL on a substantive surface, which lifts the "awaiting direct
      retrieval" flag on the Socket provisional grade.
    - The co-attributor list in THN relay (Wiz provisional A, JFrog
      first-surface, MSTIC A ratified, OX Security provisional B,
      SafeDep provisional C, StepSecurity provisional B, Aikido
      Security provisional C) appears to be reporter-aggregated
      rather than vendor-co-published. The directly-retrieved Socket
      primary does NOT show co-attribution in its visible body. MSTIC
      did not publish an independent blog post at sweep time
      (verifiable absence). The multi-firm co-attribution layer
      therefore does NOT lift Socket from B to A on this cluster
      anchor — independence test on the supposed co-attributors fails
      pending direct-retrieval of each vendor's primary publication.
    - The mechanism-family identification layer (Mini Shai-Hulud
      family per Socket verbatim "This is effectively a mini
      Shai-Hulud campaign") cleanly corroborates against VT-006
      origination corpus state (2026-05-12 finding-FLASH-0001 with
      Wiz + Snyk + StepSecurity + Semgrep + Onapsis + Aikido +
      SafeDep multi-vendor co-attribution + MSTIC primary). This
      layer cleanly carries A2 because the family identification
      is independently verifiable against the existing VT-006
      corpus state — Miasma's payload behaviors (install-time
      execution, credential harvesting, CI/CD targeting, encrypted
      exfiltration, self-propagation) are the documented VT-006
      family signature.

  Single-source veto applied on multiple layers:
    - Miasma-specific operational details (the 8 affected packages,
      the api.anthropic[.]com C2 impersonation, the SHA-256 hashes,
      the AES-128/256-GCM + RSA-OAEP encryption scheme, the
      "IfYouInvalidateThisToken" internal string signature) carry
      single-source veto — Socket is sole primary on these claims.
      WEP ceiling on Miasma-specific operational layer is "likely,"
      not "very likely."
    - The 2026-05-29 first-detection date is THN-relay-only and not
      visible in directly-retrieved Socket primary — grades B3 on
      this specific timeline detail pending Socket-side confirmation.
    - The mechanism-family identification layer carries higher
      confidence (A2 sub-grade) because VT-006 corpus state provides
      independent corroboration on the family signature.

  Per Hard Rule 2 (never originate attribution): Socket EXPLICITLY
  declines Miasma-specific actor attribution. Socket's verbatim
  language: "Attribution remains unclear, as the publicly available
  tooling lowers the barrier to entry and enables a broad range of
  threat actors to conduct similar operations." TeamPCP is named
  only as the prior-campaign open-sourcer of the underlying tooling
  ("TeamPCP open-sourced the attack tools" linked to the Shai-Hulud
  worm lineage), NOT as the Miasma operator. Hard Rule 2 compliance
  preserved verbatim in the cluster.attribution_claims field below.

  Per Hard Rule 3 (no exploitation, ever): defender-facing detail
  is included (affected package names, C2 endpoint, SHA-256 hashes,
  GitHub repository-description signature, internal payload string
  signature) but NO PoC code, exploit walkthrough, attack-step
  guidance, or payload construction detail. Consumers needing full
  technical detail can read Socket's blog post directly.

  Per Hard Rule 4 (credentials radioactive): The campaign harvests
  credentials but Socket-published IOCs are payload-side artifacts,
  not credential values. No credential content is copied or stored.

  Per Hard Rule 6 quote discipline: Three verbatim Socket quotes
  preserved in raw-signal extraction notes (attribution-layer hedge,
  mechanism-family identification, downstream-impact guidance). For
  brief promotion, briefer must trim to one Socket quote per Hard
  Rule 6 doctrine. This finding prose paraphrases throughout.

  Per Hard Rule 8 (Splunk first-party precedence): Targeted -30d
  query across both defenseclaw_local and archimedes indices for
  api.anthropic / Miasma / @redhat-cloud-services / VT-006 hashes /
  CVE-2026-45321 returned 0 substantive hits. The corpus self-
  reference event in Splunk is the morning sweep summary itself
  (Archimedes operational record), not first-party external
  telemetry. First-party silent.

source_reliability:
  grade: B
  source_name: "Socket Research Team (originating) + The Hacker News (relay)"
  source_yaml_ids:
    - socket
    - thn                          # The Hacker News — not yet ratified entry; treated B per media-class precedent
  grade_rationale: >
    Socket carries provisional B per source-grades.yaml since
    2026-05-14 (first cited finding-2026-05-14-0009 node-ipc
    3 backdoored versions, UNATTRIBUTED — co-primary with
    StepSecurity). The direct-retrieval flag on Socket can be
    lifted following this sweep — this raw-signal IS a direct
    retrieval of Socket's primary URL on a substantive surface.
    The Hacker News (Ravie Lakshmanan byline) is provisional B
    per multi-cycle citation in the corpus and the
    media-class-relay precedent.

    The THN relay names additional co-attributors (Wiz provisional
    A, JFrog first-surface, Microsoft / MSTIC A ratified, OX
    Security provisional B, SafeDep provisional C, StepSecurity
    provisional B, Aikido Security provisional C). However, the
    directly-retrieved Socket primary does NOT show co-attribution
    in its visible body, and no independent MSTIC primary
    publication was identified at sweep time. The co-attributor
    list is treated as reporter-aggregated until each vendor's
    primary publication is directly retrieved.
  provisional: true
  provisional_since: 2026-05-14
  awaiting_ratification: true

credibility:
  grade: 2
  checklist_passed:
    - probably_true_ttp_consistent
    - probably_true_no_contradicting_ab
    - probably_true_claims_coherent
  checklist_failed:
    - confirmed_independent_corroboration         # Socket sole primary on Miasma-specific operational details
  rationale: >
    Probably True (2) per credibility checklist:
    (1) Consistent with established Mini Shai-Hulud family TTPs
        (VT-006 origination 2026-05-12) — install-time execution,
        credential harvesting, CI/CD targeting, encrypted exfiltration,
        self-propagation are the documented family signature.
    (2) No contradicting evidence from A/B-grade sources. The Red Hat
        IR-response gap is informationally absent rather than
        contradicting.
    (3) Technical claims internally coherent. C2 endpoint impersonation
        pattern is consistent with broader supply-chain compromise
        tradecraft; AES-GCM + RSA-OAEP encryption scheme is realistic;
        SHA-256 hashes are well-formed; GitHub repository-description
        and commit-message signature pattern matches the lineage's
        prior GitHub-storage-class behaviors.

    Cannot rise to (1) Confirmed because Socket is the sole effective
    primary on Miasma-specific operational details. The THN co-
    attributor list appears reporter-aggregated rather than vendor-co-
    published; pending direct-retrieval of each named vendor's primary
    publication, the cluster does not clear the independent-corroboration
    test for grade 1.

corroboration:
  independent_sources_on_family_layer:
    - socket                       # Miasma research
    - vt006_corpus_state           # VT-006 origination corpus state with Wiz + Snyk + StepSecurity + Semgrep + Onapsis + Aikido + SafeDep + MSTIC multi-vendor co-attribution
  independent_sources_on_miasma_specific_operational_layer:
    - socket                       # sole primary
  independent_sources_on_first_detection_2026_05_29_layer:
    - thn                          # relay-only; not in Socket primary directly retrieved
  independent_on_family_layer: true
  independent_on_miasma_specific_operational_layer: false
  independent_on_first_detection_layer: false
  test_passed_family_layer: "VT-006 corpus state provides independent corroboration on the Mini Shai-Hulud family signature; Miasma's payload behaviors match the documented VT-006 family TTPs"
  test_failed_miasma_specific_operational_layer: "Socket is sole primary on the 8 packages, api.anthropic impersonation C2, SHA-256 hashes, encryption scheme, internal string signature — co-attributor list in THN relay is reporter-aggregated pending direct vendor-primary retrieval"

first_party_precedence:
  applied: false
  splunk_evidence: >
    Splunk -30d query across defenseclaw_local + archimedes for
    api.anthropic / @redhat-cloud-services / Miasma / SHA-256 hashes /
    CVE-2026-45321 / "Spreading Blight" returned 0 substantive
    external-event hits. No first-party telemetry on the
    api.anthropic[.]com:443/v1/api impersonation C2; no first-party
    telemetry on @redhat-cloud-services package installations from
    npm. First-party silent.

    Recommended follow-up first-party query (defender action): if
    defenseclaw_local has SDLC / CI-CD telemetry, hunt for npm
    package installation events naming any of the eight enumerated
    @redhat-cloud-services packages.

single_source_veto_applied: true
single_source_veto_layer: miasma_specific_operational_details_and_first_detection_timeline
wep_ceiling: likely                # on Miasma-specific operational layer
wep_ceiling_family_layer: very_likely  # on the Mini Shai-Hulud family identification (VT-006 corpus corroborates)

inclusion:
  eligible_for:
    - daily_brief_action          # B2 clears the daily-brief-action threshold
    - daily_brief_monitoring
    - weekly_synthesis
    - actor_profile_update        # Tooling-lineage TeamPCP reference qualifies for actor-profiler review on the lineage layer; Hard Rule 2 preserved on Miasma-specific attribution
  not_eligible_for:
    - flash                        # FLASH already evaluated and no-fired (no new CVE; mechanism class is supply-chain compromise not unpatched zero-day; co-attributor primaries not directly retrieved)

# Cluster metadata
cluster:
  topic: "Miasma Mini Shai-Hulud campaign — @redhat-cloud-services npm supply-chain compromise (VT-006 family expansion)"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-06-01-pm-001-thn-socket-miasma-mini-shai-hulud-redhat-cloud-services-npm-supply-chain
  cluster_basis: >
    Single-item cluster anchored on Socket originating research +
    THN relay disclosure of the Miasma campaign as a third-documented
    Mini Shai-Hulud family ecosystem expansion (after VT-006 npm
    @tanstack origination 2026-05-12 and VT-009 Nx Console KEV-add
    2026-05-27). Operationally a new-ecosystem expansion event for
    the VT-006 family lineage — warrants new-finding promotion
    consideration, not anti-noise dedup against existing VT-006
    state.
  attribution_claims:
    - claimed_actor: "Mini Shai-Hulud family"
      claim_type: "mechanism_family_identification"
      claimed_by_sources: [socket]
      verbatim_language: "This is effectively a mini Shai-Hulud campaign"
      verbatim_word_count: 8
      requires_analyst_review: false       # Family identification is mechanism-class, not actor attribution
    - claimed_actor: "TeamPCP"
      claim_type: "prior_campaign_tooling_origin_lineage_only_NOT_miasma_attribution"
      claimed_by_sources: [socket]
      verbatim_language_excerpt: "TeamPCP open-sourced the attack tools" + "opening the door for other threat actors"
      requires_analyst_review: true         # Lineage-tooling reference; analyst SAT-class consideration of whether TeamPCP attribution remains operationally meaningful when tooling is open-sourced
    - claimed_actor: "unattributed_miasma_operator"
      claim_type: "miasma_specific_actor_attribution"
      claimed_by_sources: [socket]
      verbatim_language: "Attribution remains unclear, as the publicly available tooling lowers the barrier to entry and enables a broad range of threat actors to conduct similar operations."
      hard_rule_2_compliance: positive_socket_explicitly_declines_attribution
      requires_analyst_review: true         # Attribution void preserved; if A-grade vendor later attributes, analyst handoff

# Lifecycle
tlp: CLEAR
published_in_briefs: [2026-06-01-afternoon]
retracted: false
retraction_brief_id: null

# Downstream handoff flags
analyst_review_required: true   # WEP "likely" on Miasma-specific operational layer + tooling-lineage attribution claims requiring SAT-class consideration
analyst_review_complete: true
analyst_review_run_id: analyst-20260601-164000
analyst_verdict: stands_with_brief_caveat   # WEP unchanged; ACH ranks H2 (tooling-leaked-reused) first, H1 (TeamPCP-direct) LAST — reinforces Hard-Rule-2 attribution void; 5 KAC qualify + A3 defender-pre-condition test
red_team_review_required: false # WEP ceiling "likely" not "very likely"; single-source veto holds on Miasma-specific layer
red_team_review: null
analysis_sections:
  sat_ach:
    ach_analysis:
      question: "What is the most plausible operator-class explanation for the Miasma Mini Shai-Hulud campaign, given Socket's explicit attribution-decline and the open-sourced TeamPCP tooling lineage?"
      analyzed_at: 2026-06-01T16:40:00-04:00
      analyzed_by: analyst
      red_team_review: null
      hard_rule_2_compliance: >
        ACH framed at operator-CLASS level, not specific-actor-attribution
        level. Per Hard Rule 2, Archimedes does NOT originate Miasma-specific
        attribution. Socket explicitly declined attribution. This ACH
        evaluates the CATEGORY of operator-explanation most consistent with
        evidence; it does NOT name a specific actor. H1 references TeamPCP
        only as a RELAY of Socket's lineage-tooling claim (sourced), not as
        an Archimedes-originated attribution.

      hypotheses:
        - id: H1
          statement: "TeamPCP-direct operator continuity — same actor operating the original Shai-Hulud tooling and the Miasma campaign; tooling open-sourcing is misdirection or a co-existing public-tooling track."
        - id: H2
          statement: "TeamPCP-tooling-leaked-and-reused — TeamPCP open-sourced or had tooling leaked; unrelated downstream operator(s) adopted the tooling and conducted Miasma; operator identity is distinct from TeamPCP."
        - id: H3
          statement: "Copycat unrelated to TeamPCP tooling — operator independently developed Mini-Shai-Hulud-class tooling, with family-resemblance arising from convergent npm-ecosystem worm tradecraft rather than tooling lineage."
        - id: H4
          statement: "Null / opportunistic — multiple unrelated operators acting opportunistically with mixed tooling provenance; 'Miasma' is a name applied to what is actually a heterogeneous cluster of activity in @redhat-cloud-services."
        - id: H5
          statement: "Composite — TeamPCP-aligned operator collaborating with or selling tooling/services to a second-party downstream campaign operator (e.g., affiliate model); attribution-decline is appropriate but operator continuity is partial."

      evidence:
        - id: E1
          description: "Socket explicitly declines Miasma-specific attribution, citing 'publicly available tooling lowers the barrier to entry' (verbatim)"
          source: socket
          digraph: B2
          weight: 2
        - id: E2
          description: "Socket attests TeamPCP open-sourced the underlying Shai-Hulud tooling (verbatim relay; 'TeamPCP open-sourced the attack tools')"
          source: socket
          digraph: B2
          weight: 2
        - id: E3
          description: "Mechanism class identification — Miasma payload behaviors (install-time execution, credential harvesting, CI/CD targeting, encrypted exfiltration, self-propagation) match VT-006 family signature"
          source: socket-plus-vt006-corpus
          digraph: A2
          weight: 3
        - id: E4
          description: "Novel tradecraft layer — Miasma uses api.anthropic[.]com:443/v1/api C2 impersonation; prior VT-006 cohort used different exfiltration patterns"
          source: socket
          digraph: B2
          weight: 2
        - id: E5
          description: "Three ecosystem expansions in ~20 days (@tanstack 5/12 → Nx Console 5/27 → @redhat-cloud-services 6/01)"
          source: corpus-state
          digraph: A1
          weight: 3
        - id: E6
          description: "Internal payload string signature 'IfYouInvalidateThisToken...' suggests operator awareness of detection-research community"
          source: socket
          digraph: B2
          weight: 2
        - id: E7
          description: "Same encryption scheme class (AES-128/256-GCM + RSA-OAEP) across VT-006 family lineage and Miasma"
          source: socket
          digraph: B2
          weight: 2
        - id: E8
          description: "Different namespace (@redhat-cloud-services) compared to VT-006 (@tanstack aviation packages) and VT-009 (Nx Console developer tooling) — namespace targeting drift"
          source: corpus-state
          digraph: A1
          weight: 3
        - id: E9
          description: "Splunk -30d zero substantive hits on Miasma IOCs / api.anthropic C2 / @redhat-cloud-services package installations"
          source: splunk-negative-search
          digraph: A1
          weight: 3
        - id: E10
          description: "MSTIC + Wiz + JFrog + OX Security + SafeDep + StepSecurity + Aikido named in THN as co-attributors, but THN-relay-only — none directly retrieved as primaries at sweep time; MSTIC has not published independent blog post"
          source: thn-relay-quality-concern
          digraph: B3
          weight: 1
        - id: E11
          description: "No A-grade vendor IR-firm has committed to operator-class attribution for Miasma; coordinated-disclosure-style framing"
          source: corpus-state-verifiable-absence
          digraph: A1
          weight: 3

      matrix:
        E1: {H1: I, H2: C, H3: C, H4: C, H5: C}     # Socket attribution-decline weakly inconsistent with same-operator H1 (would expect attribution-confidence if same operator)
        E2: {H1: C, H2: C, H3: I, H4: N, H5: C}     # Open-sourced-tooling claim distinguishes lineage-via-tooling (H1/H2/H5) from independent-development (H3)
        E3: {H1: C, H2: C, H3: C, H4: C, H5: C}     # Family-mechanism identification is non-diagnostic on operator-class — Socket explicitly notes tooling lowers barrier
        E4: {H1: C, H2: C, H3: C, H4: C, H5: C}     # Novel tradecraft (Anthropic-API C2) is non-diagnostic — any of H1-H5 could innovate
        E5: {H1: C, H2: C, H3: N, H4: C, H5: C}     # 20-day expansion velocity is non-diagnostic against most hypotheses but mildly inconsistent with single-operator-development H3
        E6: {H1: C, H2: C, H3: C, H4: N, H5: C}     # Detection-aware string signature is non-diagnostic
        E7: {H1: C, H2: C, H3: I, H4: N, H5: C}     # Same encryption scheme weakly inconsistent with independent-development H3
        E8: {H1: N, H2: C, H3: C, H4: C, H5: C}     # Namespace drift mildly inconsistent with same-operator H1 (would expect target-class consistency)
        E9: {H1: N, H2: N, H3: N, H4: N, H5: N}     # Splunk silence non-diagnostic across all hypotheses
        E10: {H1: N, H2: N, H3: N, H4: N, H5: N}    # Co-attributor list quality concern non-diagnostic on operator-class
        E11: {H1: I, H2: N, H3: N, H4: C, H5: N}    # No A-grade attribution mildly inconsistent with same-operator-known H1; consistent with heterogeneous-cluster H4

      inconsistency_counts:
        H1: 3     # E1, E8, E11 — attribution decline, namespace drift, no A-grade attribution
        H2: 0
        H3: 2     # E2, E7 — open-sourced tooling reference and encryption-scheme reuse weakly inconsistent with independent development
        H4: 0
        H5: 0

      diagnostic_evidence:
        - E1: "Socket's attribution-decline distinguishes tooling-leaked-reused (H2/H5) and heterogeneous-cluster (H4) from same-operator-continuity (H1)"
        - E2: "Open-sourced-tooling attestation distinguishes tooling-lineage hypotheses (H1/H2/H5) from independent-development (H3)"
        - E7: "Same encryption scheme weakly distinguishes shared-tooling-lineage (H1/H2/H5) from independent-development (H3)"
        - E8: "Namespace targeting drift distinguishes single-operator-with-target-class-continuity (H1) from heterogeneous-operator hypotheses (H2/H4/H5)"

      ranking:
        - rank: 1
          hypothesis_id: H2
          rationale: "Zero inconsistencies. Tooling-leaked-and-reused is the parsimonious read of Socket's explicit attribution-decline + open-sourced-tooling reference + namespace drift. Operationally meaningful: defender prioritization is family-mechanism-class, NOT actor-specific."
          wep: likely
        - rank: 2
          hypothesis_id: H4
          rationale: "Zero inconsistencies. Heterogeneous-operator-cluster is also consistent with the evidence — the 'Miasma' label may aggregate multiple unrelated operators using public tooling. Cannot be distinguished from H2 with available evidence."
          wep: roughly_even_chance
        - rank: 3
          hypothesis_id: H5
          rationale: "Zero inconsistencies. Composite (TeamPCP-affiliated downstream operator) cannot be ruled out — Socket's hedge specifically permits this reading. Operationally indistinguishable from H2 from a defender standpoint."
          wep: unlikely
        - rank: 4
          hypothesis_id: H3
          rationale: "Two weak inconsistencies (E2, E7). Independent-development scenario requires ignoring Socket's open-sourced-tooling attestation and the encryption-scheme reuse; not parsimonious."
          wep: unlikely
        - rank: 5
          hypothesis_id: H1
          rationale: "Three inconsistencies (E1, E8, E11). TeamPCP-direct operator continuity requires arguing AGAINST Socket's explicit attribution-decline + the namespace drift + the A-grade attribution silence. Hard Rule 2 explicit: ACH ranks this last; finding does NOT attribute to TeamPCP-direct."
          wep: very_unlikely

      sensitivity_analysis:
        brittleness: high
        load_bearing_evidence: [E1, E2, E8, E10]
        if_E1_socket_reverses_attribution_decline: "If Socket or any A-grade vendor commits to TeamPCP-direct attribution post-disclosure, H1 rises significantly; rerun ACH; Hard Rule 2 attribution-relay rather than origination"
        if_E10_co_attributors_directly_retrieved_with_attribution_content: "If MSTIC / Wiz / JFrog primaries directly retrieved reveal operator-specific attribution, H1/H2/H5 re-rank; current sweep does not have this evidence"
        if_E2_open_sourced_tooling_claim_revised: "If TeamPCP-tooling-open-sourcing is later disputed (e.g., Socket revises post-publication; corpus-precedent on TeamPCP changes), H1 vs. H3 distinction shifts"
        if_namespace_drift_pattern_continues_4th_5th_expansion: "If Mini-Shai-Hulud family expansion continues into completely unrelated namespaces, H4 (heterogeneous cluster) gains support over H2 (single-leaked-tooling operator)"

      tripwires:
        - observation: "Socket or any A-grade vendor publishes Miasma-specific actor attribution"
          effect: "Hard Rule 2 boundary — relay attribution; re-rank ACH; potentially elevate to H1 if attribution is TeamPCP-direct"
        - observation: "MSTIC primary publication identified in next-cycle collection"
          effect: "Lift cluster source-reliability from B to A; potentially shift co-attribution layer credibility"
        - observation: "4th or 5th Mini-Shai-Hulud family ecosystem expansion within next 30 days"
          effect: "If continuing namespace drift, H4 (heterogeneous-cluster) rises over H2; if namespace stays @redhat-cloud-services-adjacent, H1/H5 rise"
        - observation: "TeamPCP roster actor profile update — any change in operational-status assessment, threat-box re-scoring, or capability inventory"
          effect: "If TeamPCP operational status changes (disrupted, active-but-pivoting, etc.), assumption A1 below revises"
        - observation: "Anthropic publishes public statement on api.anthropic[.]com:443/v1/api C2 impersonation"
          effect: "May surface DNS / cert-pinning forensics that distinguishes single-operator from heterogeneous-cluster operator(s)"

      conclusion:
        summary: |
          ACH ranks H2 (tooling-leaked-and-reused) first with zero
          inconsistencies, tied with H4 (heterogeneous cluster) and H5
          (composite). H1 (TeamPCP-direct operator continuity) is ranked
          last with three inconsistencies — ACH does NOT support attributing
          Miasma to TeamPCP-direct. The grader's preservation of
          Hard-Rule-2 attribution void is correct and is reinforced by ACH.

          The operationally meaningful insight: H2, H4, and H5 are all
          consistent with the evidence and operationally indistinguishable
          from a defender-action standpoint. The "operator continuity"
          question is academically interesting (relevant to TeamPCP actor
          profile maintenance) but does NOT change the briefer's
          defender-prioritization message. Defender action is family-
          mechanism-class, NOT actor-specific.

          TeamPCP tooling-lineage reference in the finding is sourced (Socket
          verbatim) and acceptable per Hard Rule 2; it must NOT be inflated
          to Miasma-operator attribution in brief prose.
        wep: likely
        confidence_caveats: |
          Assessment is HIGH-brittleness to co-attributor primary retrieval
          (E10) and to any Tier-1 vendor publishing Miasma-specific
          attribution. Three-way tie at rank 1 means ACH cannot
          distinguish operator-class; this is appropriate epistemic
          humility given Socket's explicit attribution-decline. Hard-Rule-2
          attribution void must be preserved by briefer.

  sat_kac:
    kac_analysis:
      assessment_under_review: >
        "Miasma is a Mini Shai-Hulud family supply-chain campaign affecting
        eight @redhat-cloud-services npm packages with novel api.anthropic
        C2 impersonation tradecraft; A&D-sector relevance is medium-low /
        indirect given the @redhat-cloud-services namespace lacks aviation/
        defense-specific package footprint."
      analyzed_at: 2026-06-01T16:45:00-04:00
      analyzed_by: analyst
      invoking_context: "Pre-publication review for afternoon brief; B2 WEP-ceiling likely on Miasma-specific operational layer; tooling-lineage TeamPCP reference requires SAT-class scrutiny"

      assumptions:
        - id: A1
          statement: "TeamPCP-as-tooling-origin reference implies operator-level continuity meaningful to threat-actor tracking"
          category: actor_continuity
          stated: true
          why_must_be_true: "If TeamPCP's open-sourced tooling does NOT carry operator continuity to downstream campaigns, the actor-profile-update inclusion eligibility on this finding is mis-targeted; the lineage-tooling layer becomes mechanism-class only, not actor-class"
          when_could_be_false: "Open-sourcing is precisely the act that BREAKS operator-tooling continuity — once tooling is in the public domain, any downstream operator can use it; Socket's own framing explicitly contemplates this ('publicly available tooling lowers the barrier to entry and enables a broad range of threat actors'); ACH ranks H1 (TeamPCP-direct) last"
          evidence_for: [socket-attestation-teampcp-open-sourced]
          evidence_against: [socket-attribution-decline, ach-h1-ranked-last]
          confidence: low
          centrality: material
          classification: qualify

        - id: A2
          statement: "api.anthropic[.]com:443/v1/api C2 impersonation generalizes as TTP signature across Miasma operations, vs. being campaign-specific tradecraft"
          category: ttp_patterns
          stated: false
          why_must_be_true: "If the Anthropic-API-impersonation C2 is durable across the Mini-Shai-Hulud-family lineage going forward, defenders can build long-term detection rules around DNS/cert-pinning verification; if it's one-campaign-only, defenders should not over-anchor detection on this artifact"
          when_could_be_false: "Operator may rotate C2 infrastructure post-disclosure; Anthropic may issue takedown or revoke cert-pinning, forcing C2 rotation; novel tradecraft layers in prior VT-006 cohort did NOT carry forward as durable signatures"
          evidence_for: [socket-attestation-anthropic-impersonation]
          evidence_against: [vt006-prior-cohort-c2-rotation-pattern]
          confidence: low
          centrality: material
          classification: qualify

        - id: A3
          statement: "@redhat-cloud-services namespace packages appear in defense-prime dependency trees at material-enough rate to warrant brief surfacing"
          category: targeting_logic
          stated: false
          why_must_be_true: "A&D-prime defender prioritization rests on this; if @redhat-cloud-services package family is NOT in defense-prime SDLC dependency trees, the finding's A&D Relevance is downgradeable from medium-low to negligible"
          when_could_be_false: "@redhat-cloud-services is Red Hat Console / Insights tooling, not core enterprise Red Hat product line; defense-prime estates running Red Hat Enterprise Linux / OpenShift may NOT have @redhat-cloud-services packages in dependency graphs — this is Red Hat Console UI / Insights customer-facing tooling, not RHEL/OpenShift core"
          evidence_for: []
          evidence_against: [redhat-cloud-services-namespace-scope-uncertainty]
          confidence: low
          centrality: critical
          classification: test
          proposed_test: "Defender action — A&D-prime SDLC asset-management teams should grep dependency graphs for any @redhat-cloud-services/* package across npm package.json / lockfiles. This is an inexpensive test (single-pass grep across SDLC dependency manifests). Recommend brief elevates this as defender pre-condition; if zero hits across A&D-prime estate, the entire finding's A&D Relevance is negligible and brief positioning should be revised."

        - id: A4
          statement: "Socket's provisional B grade is correctly applied; the lift from 'awaiting direct retrieval' to direct-retrieval-confirmed in this sweep is operationally meaningful but does not lift letter grade"
          category: source_reliability
          stated: true
          why_must_be_true: "Grader treated Socket as provisional B with direct-retrieval flag lifted on this sweep; cluster anchor B2 rests on this"
          when_could_be_false: "If Socket's track record post-ratification revises grade up or down, B2 anchor shifts"
          evidence_for: [source-grades-yaml-socket-provisional-b, direct-retrieval-sweep]
          evidence_against: []
          confidence: high
          centrality: material
          classification: sound

        - id: A5
          statement: "Co-attributor list in THN relay (Wiz/JFrog/MSTIC/OX/SafeDep/StepSecurity/Aikido) does NOT lift cluster reliability from B to A — reporter-aggregated rather than vendor-co-published"
          category: source_reliability
          stated: true
          why_must_be_true: "Grader's letter-B anchor explicitly rests on this; if co-attribution layer DID lift to A, the entire WEP ceiling shifts to very_likely"
          when_could_be_false: "Next-cycle collector direct-retrieval of MSTIC / Wiz / JFrog primary publications may confirm co-attribution; in which case the cluster lifts from B2 to A2 and red-team-analyst handoff triggers"
          evidence_for: [mstic-no-blog-post-at-sweep-time, vendor-primaries-not-directly-retrieved]
          evidence_against: []
          confidence: medium
          centrality: critical
          classification: qualify

        - id: A6
          statement: "Three ecosystem expansions in ~20 days indicates active family-expansion-phase rather than steady-state opportunistic activity"
          category: ttp_patterns
          stated: true
          why_must_be_true: "Finding's 'expansion velocity' framing depends on this; relevant to defender prioritization tempo"
          when_could_be_false: "Three observations may be coincidence — selection bias on what defenders are catching, not necessarily a tempo signal; family expansion may be more uniform but observed less consistently before the May-June 2026 detection window"
          evidence_for: [vt006-vt009-miasma-temporal-cluster]
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify

        - id: A7
          statement: "Red Hat IR-response silence is informationally absent rather than contradicting; absence does not weaken Socket's @redhat-cloud-services namespace claim"
          category: source_reliability
          stated: true
          why_must_be_true: "Cluster grading explicitly treats Red Hat silence as informational gap, not as contradiction"
          when_could_be_false: "If Red Hat eventually publishes a statement clarifying that @redhat-cloud-services packages are NOT official Red Hat-published packages (community-published, namespace-squatting, etc.), Socket's framing of 'Red Hat namespace compromise' may be revised; campaign target-class shifts"
          evidence_for: [red-hat-statement-pending]
          evidence_against: []
          confidence: low
          centrality: material
          classification: qualify

        - id: A8
          statement: "VT-006 family identification on the mechanism layer is robust (A2 sub-grade) and would survive even if Miasma-specific operational details are later revised"
          category: ttp_patterns
          stated: true
          why_must_be_true: "Family-layer carries A2 via VT-006 corpus corroboration; WEP-ceiling very_likely on family identification layer"
          when_could_be_false: "If multiple Miasma-specific operational details are revised post-publication, the family-identification confidence may erode by association"
          evidence_for: [vt006-corpus-state, socket-verbatim-family-identification]
          evidence_against: []
          confidence: high
          centrality: peripheral
          classification: sound

        - id: A9
          statement: "Hard Rule 2 attribution void will hold — no source will lift Socket's explicit attribution-decline within the brief-relevant window"
          category: source_reliability
          stated: true
          why_must_be_true: "Briefer's framing depends on continued attribution silence in the post-disclosure window"
          when_could_be_false: "Tier-1 IR firm publication (Mandiant / CrowdStrike / Unit 42 / MSTIC) within 24-72h post-Socket may commit to Miasma-specific attribution; analyst handoff per Hard Rule 2 boundary"
          evidence_for: [socket-explicit-decline]
          evidence_against: []
          confidence: medium
          centrality: peripheral
          classification: sound

      classifications_summary:
        sound: 3
        qualify: 5
        test: 1
        reject: 0

      remediation:
        status: proceed
        qualifying_caveats:
          - "A1 (TeamPCP-as-tooling-origin operator continuity): open-sourcing of tooling BREAKS operator-tooling continuity by definition; lineage-tooling reference is mechanism-class, NOT actor-class for downstream campaigns; briefer must preserve Hard-Rule-2 attribution void"
          - "A2 (Anthropic-API C2 generalization): novel tradecraft layer may NOT carry forward as durable signature; defenders should not over-anchor long-term detection on api.anthropic[.]com IOC"
          - "A5 (co-attributor list quality): THN-aggregated co-attribution may be reporter aggregation, not vendor-co-publication; if next-cycle direct-retrieval of MSTIC/Wiz/JFrog primaries confirms co-attribution, cluster lifts to A2 and red-team handoff triggers"
          - "A6 (expansion-velocity selection-bias): three-in-20-days may be observation cluster rather than tempo signal"
          - "A7 (Red Hat namespace ambiguity): if Red Hat clarifies @redhat-cloud-services is NOT official Red Hat package family, campaign framing shifts"
        blocking_test_assumption: A3
        blocking_test_detail: |
          A3 (@redhat-cloud-services namespace packages in defense-prime
          dependency trees at material rate) is the LOAD-BEARING premise on
          A&D-prime relevance. Without empirical evidence that the eight
          enumerated packages appear in A&D-prime SDLC manifests, the
          finding's medium-low-indirect framing is speculative. This is an
          inexpensive defender-side test (grep across npm dependency graphs).
          Recommend brief elevates A3 to defender pre-condition: "Grep
          A&D-prime npm dependency graphs for @redhat-cloud-services/*
          packages BEFORE treating this as defender-action priority. If
          zero hits, A&D Relevance is negligible."
        next_action: "Briefer surfaces A3 as defender pre-condition check; A1/A2/A5/A6/A7 as qualifying caveats; preserve Hard-Rule-2 attribution void verbatim per Socket"

      recommended_wep_after_test:
        if_a3_defender_grep_finds_zero_hits: "WEP on operational layer holds at likely (Socket attestation unchanged), but A&D Relevance downgraded from medium-low to negligible; recommend briefer reposition as awareness item not defender-action item"
        if_a3_defender_grep_finds_material_hits: "WEP holds at likely; A&D Relevance upgraded from medium-low to medium-direct; recommend grader re-look for promotion priority adjustment"
        if_co_attributor_primaries_directly_retrieved_with_co_attribution_content: "Cluster lifts B2 → A2; WEP rises to very_likely on Miasma-specific operational layer; red-team-analyst handoff triggers"

# Relationships
related_findings:
  - finding-2026-05-12-FLASH-0001   # VT-006 origination — Mini Shai-Hulud npm @tanstack cluster
  - finding-2026-05-27-0007         # VT-009 Nx Console KEV-add — prior Mini Shai-Hulud family expansion event
related_vulns:
  - VT-006                          # Mini Shai-Hulud family — Miasma is the third documented ecosystem expansion
related_actors:
  - "001"                           # TeamPCP — prior-campaign tooling-origin lineage only; Hard Rule 2 preserved on Miasma-specific attribution
related_vulns_corpus_index_action: >
  vuln-tracker handoff: evaluate whether Miasma warrants a NEW
  VT- entry (next slot VT-011 if Oracle WebLogic finding-2026-06-01-0005
  takes VT-012) or constitutes a documented expansion of VT-006
  family-scope. Recommended posture: extend VT-006 scope-of-coverage
  to enumerate the Miasma ecosystem expansion as a documented family
  variant, rather than scaffolding a separate VT- entry, because:
  (a) no new CVE assigned to Miasma, (b) mechanism class is identical
  to VT-006 per Socket verbatim, (c) the operational unit-of-tracking
  is the "Mini Shai-Hulud family" not the specific @redhat-cloud-services
  ecosystem. The VT-006 dossier (not yet scaffolded per _index.yaml
  state) should incorporate Miasma as a documented expansion when
  vuln-tracker creates the dossier on next pass.

# Watch signals
watch_signals:
  - "Red Hat public incident-response statement on @redhat-cloud-services namespace exposure"
  - "MSTIC primary publication confirming the Microsoft co-attribution referenced in THN relay (currently relay-only)"
  - "Snyk publication on Miasma — Snyk co-attributed VT-006 origination 2026-05-12; absence from THN's Miasma co-attributor list is notable"
  - "Additional ecosystem expansions — Mini Shai-Hulud family now touches npm @tanstack (VT-006), Nx Console (VT-009), npm @redhat-cloud-services (Miasma) in ~20 days; watch for further namespace expansions"
  - "Attribution refinement — does any A-grade vendor lift Socket's explicit 'attribution remains unclear' hedge and attribute Miasma to TeamPCP specifically? Per Hard Rule 2, Archimedes does NOT originate that attribution; relay if/when an A-grade vendor commits"
  - "CISA KEV expansion to include Miasma-named packages or create a new CVE — VT-006 CVE-2026-45321 is already KEV-listed (2026-05-27)"
  - "A&D-prime customer-impact statement naming @redhat-cloud-services dependency exposure in Tier-1 SDLC"
  - "Anthropic public statement on the api.anthropic[.]com:443/v1/api C2 impersonation"
---

# Miasma Mini Shai-Hulud Campaign — @redhat-cloud-services npm Supply-Chain Compromise, Third Documented VT-006 Family Ecosystem Expansion

## Summary

The Socket Research Team published originating research on 2026-06-01 disclosing **Miasma** — a Mini Shai-Hulud family supply-chain campaign that compromised at least eight `@redhat-cloud-services` npm packages with credential-stealing, CI/CD-targeting, encrypted-exfiltrating, self-propagating worm payloads. The Hacker News (Ravie Lakshmanan) relayed the disclosure the same day. First detection per THN relay dates to 2026-05-29; public disclosure 2026-06-01.

This is the **third documented Mini Shai-Hulud family ecosystem expansion** in the Archimedes corpus after the original npm `@tanstack` cluster (VT-006 origination, CVE-2026-45321, 2026-05-12) and the Nx Console developer-tooling pathway (VT-009, KEV-listed 2026-05-27) — three ecosystem expansions of the same self-propagating worm family within approximately 20 days.

**Socket explicitly declines actor attribution.** Per Socket verbatim, "Attribution remains unclear, as the publicly available tooling lowers the barrier to entry and enables a broad range of threat actors to conduct similar operations." TeamPCP (roster actor #001, HIGH threat level) is referenced only as the prior-campaign open-sourcer of the underlying Shai-Hulud tooling lineage, NOT as the Miasma operator. Hard Rule 2 compliance is preserved: this finding records what Socket asserts and does not originate Miasma-specific attribution.

The campaign's novel tradecraft layer is a **C2 endpoint impersonating Anthropic's legitimate API infrastructure**: `https://api.anthropic[.]com:443/v1/api` (defanged). The impersonation is a new tradecraft layer within the Mini Shai-Hulud family — prior VT-006 cohort used session-network exfiltration and direct attacker-controlled domains. This C2 endpoint requires DNS-and-cert-pinning verification against Anthropic-legitimate infrastructure before any blocking action to avoid breaking legitimate Anthropic API consumers in A&D-prime estates.

## Sources

### Socket Research Team (socket, provisional B since 2026-05-14)

- **URL:** https://socket.dev/blog/mini-shai-hulud-campaign-hits-red-hat-cloud-services-npm-packages
- **Published:** 2026-06-01
- **Byline:** Socket Research Team (originating)
- **Key claim:** Originating disclosure of the Miasma campaign as Mini Shai-Hulud family; eight `@redhat-cloud-services` packages compromised; novel `api.anthropic[.]com` C2 impersonation; explicit attribution decline.

### The Hacker News (thn, provisional B)

- **URL:** https://thehackernews.com/2026/06/miasma-supply-chain-attack-compromises.html
- **Published:** 2026-06-01T17:40:28 UTC (13:40 EDT)
- **Byline:** Ravie Lakshmanan (relay)
- **Key claim:** Relays Socket; supplies the 2026-05-29 first-detection date; names co-attributor vendors (Wiz / JFrog / Microsoft / OX Security / SafeDep / StepSecurity / Aikido Security) — co-attribution layer NOT directly retrieved from each vendor primary at sweep time.

### Internal corpus state (VT-006 family identification corroboration)

- **finding-2026-05-12-FLASH-0001:** VT-006 origination — Mini Shai-Hulud npm @tanstack cluster with Wiz + Snyk + StepSecurity + Semgrep + Onapsis + Aikido + SafeDep + MSTIC multi-vendor co-attribution
- **VT-006 in `_index.yaml`:** Mini Shai-Hulud family — npm + PyPI self-propagating worm (CVE-2026-45321), KEV-listed 2026-05-27, KEV due 2026-06-10

## Technical detail

**Campaign codename:** Miasma (originator unclear; "Miasma: The Spreading Blight" appears as a GitHub repository description and commit-message string)

**Family lineage:** Mini Shai-Hulud (per Socket verbatim: "This is effectively a mini Shai-Hulud campaign" — 8 words, Hard Rule 6 compliant)

**Affected ecosystem:** npm registry, `@redhat-cloud-services` organizational namespace

**Affected packages (per THN relay of Socket):**

1. `@redhat-cloud-services/chrome@2.3.1` (only package with explicitly named version in directly-retrieved Socket primary)
2. `@redhat-cloud-services/vulnerabilities-client`
3. `@redhat-cloud-services/tsc-transform-imports`
4. `@redhat-cloud-services/topological-inventory-client`
5. `@redhat-cloud-services/sources-client`
6. `@redhat-cloud-services/rule-components`
7. `@redhat-cloud-services/remediations-client`
8. `@redhat-cloud-services/rbac-client`

Socket primary references "affected `@redhat-cloud-services` package versions" plurally without enumerating versions for packages 2-8 in the directly-retrieved post content.

**Mechanism class (per Socket — family TTP signature):**
- Install-time execution (npm `postinstall` or equivalent install-script lifecycle)
- Credential harvesting (broadly: ambient developer / CI-CD credentials in environment)
- CI/CD targeting (build-environment-aware payload behavior)
- Encrypted exfiltration (AES-128-GCM and AES-256-GCM with RSA-OAEP wrapping)
- Self-propagation (worm publishes to additional packages, hence "Mini Shai-Hulud" family designation)

**Primary C2 (defanged):** `https://api.anthropic[.]com:443/v1/api`

This C2 endpoint impersonates Anthropic's legitimate API infrastructure. The legitimate Anthropic API is on `api.anthropic.com` without the trailing `:443/v1/api` path-stub; the difference is the campaign-controlled domain (or DNS-spoofed equivalent). **Defender note:** DNS-and-cert-pinning verification against Anthropic-legitimate infrastructure is required before any blocking action to avoid breaking legitimate Anthropic API consumers in A&D-prime estates that use Claude / Anthropic-API-based tooling.

**Fallback exfiltration:** GitHub API used for encrypted-result storage in public GitHub repositories with description string "Miasma: The Spreading Blight" (per THN relay).

**No PoC code, exploit walkthrough, or attack-step guidance is included per Hard Rule 3.** The mechanism class is identified for defensive purposes; consumers needing full technical detail can read Socket's blog post directly.

## IOCs surfaced

```yaml
indicators:
  - type: domain
    value: api.anthropic[.]com
    defanged: true
    role: c2_exfiltration_primary
    path: "/v1/api"
    port: 443
    notes: >
      Defanged. Impersonates legitimate Anthropic API endpoint
      (api.anthropic.com). Requires DNS-and-cert-pinning
      verification against Anthropic-legitimate infrastructure
      before blocking. Novel tradecraft layer within VT-006
      family lineage.

  - type: sha256
    value: 88896d478986d453f5da79b311de39d9b4b1bea95c21af1d8ef181b0f4e52fe9
    role: tarball_of_compromised_package
    artifact: "@redhat-cloud-services/chrome@2.3.1.tar.gz"

  - type: sha256
    value: 21b6409a7b84446310daca5409ad6112ac60a1e4bef97736e53fff5f63bfdef4
    role: malicious_payload_file
    artifact: package/index.js

  - type: sha256
    value: 0dc06ecdaa63fe24859cfd955053c23245c536e4733480239d14bebf12688e35
    role: decrypted_payload

  - type: encryption_scheme
    value: AES-128-GCM and AES-256-GCM with RSA-OAEP wrapping
    role: campaign_encryption_layer

  - type: string_identifier
    value: "IfYouInvalidateThisTokenItWillNukeTheComputerOfTheOwner"
    role: campaign_string_signature_internal_payload
    notes: >
      Useful for static-detection rule authoring. Operator-side
      string suggests awareness of detection research community.

  - type: github_string_identifier
    value: "Miasma: The Spreading Blight"
    role: github_repo_description_or_commit_string
    notes: >
      Used as GitHub repository description and commit-message
      string on encrypted-result-storage GitHub repos. Useful
      for GitHub-side detection / hunt rule authoring.

  - type: cve
    value: CVE-2026-45321
    role: family_lineage_origination
    notes: >
      Originating CVE on VT-006 Mini Shai-Hulud family. Miasma
      reuses the same family mechanism class per Socket verbatim.
      No new CVE assigned to Miasma at disclosure.

attribution_claims:
  - actor: "Mini Shai-Hulud family"
    claim_type: mechanism_family_identification
    source: socket
    verbatim_language: "This is effectively a mini Shai-Hulud campaign"

  - actor: "TeamPCP"
    claim_type: prior_campaign_tooling_origin_lineage_ONLY
    source: socket
    verbatim_language_excerpt: "TeamPCP open-sourced the attack tools"
    NOTE: explicit_lineage_only_NOT_miasma_attribution

  - actor: "unattributed"
    claim_type: miasma_specific_actor_attribution
    source: socket
    verbatim_language: "Attribution remains unclear, as the publicly available tooling lowers the barrier to entry and enables a broad range of threat actors to conduct similar operations."
    hard_rule_2_compliance: positive_socket_explicitly_declines
```

## A&D Sector Relevance

**Medium-low / indirect, lower than VT-006 origination.** Socket primary and THN relay both make no defense / aerospace / industrial / DIB references. The `@redhat-cloud-services` namespace exposure has generalized enterprise / cloud-platform deployment footprint, not A&D-specific.

The corpus-precedent VT-006 origination assessed A&D relevance as **medium-indirect via @squawk aviation ecosystem** (the original cluster compromised 19 aviation-data packages under `@squawk`). Miasma's affected namespace `@redhat-cloud-services` does NOT carry an analogous aviation / defense-specific package set; A&D relevance assessment for Miasma defaults lower than VT-006 unless A&D-prime customer-impact statements surface in the 24-72h post-disclosure window.

**A&D defender priority:**
- Check SDLC dependency trees for any of the eight enumerated `@redhat-cloud-services` packages. The `@redhat-cloud-services/chrome` (UI library), `*-client` packages (REST API clients), and `rbac-client` are common Red Hat product-tooling consumers — defense primes running OpenShift, Red Hat Insights, or other Red Hat-product-adjacent middleware should audit dependency graphs.
- DNS / proxy / EDR hunt for outbound connections to `api.anthropic.com:443/v1/api` — with the verification caveat above to avoid breaking legitimate Anthropic API consumers.
- GitHub-tenant hunt for repositories with description string "Miasma: The Spreading Blight" anywhere in the A&D-prime GitHub estate.
- npm install events naming any of the eight packages in CI/CD telemetry.

## Relationship to existing findings

- **finding-2026-05-12-FLASH-0001 (VT-006 origination):** Miasma is the third documented family ecosystem expansion of Mini Shai-Hulud. Mechanism class is identical per Socket verbatim. Family-identification layer is independently corroborated by VT-006 corpus state.
- **finding-2026-05-27-0007 (VT-006 + VT-009 KEV-add):** Miasma extends the family's ecosystem-expansion trajectory documented in this prior finding — npm @tanstack → Nx Console → @redhat-cloud-services in ~20 days.
- **VT-006 in `_index.yaml`:** This finding's grader handoff recommends extending VT-006 scope-of-coverage to enumerate Miasma as a documented family variant rather than scaffolding a separate VT- entry. Vuln-tracker handles the determination.

## Open questions for analyst

1. **Attribution-void preservation** — Socket EXPLICITLY declines Miasma-specific attribution. Per Hard Rule 2, Archimedes does NOT originate attribution. If a future A-grade vendor (Mandiant / CrowdStrike / Unit 42 / MSTIC) commits to a specific actor attribution for Miasma, analyst SAT-ACH handoff. Until then, the operator-meaningful claim is "Mini Shai-Hulud family mechanism, unattributed-operator."

2. **TeamPCP tooling-lineage operational meaningfulness** — Socket notes TeamPCP open-sourced the underlying tooling, "opening the door for other threat actors." Analyst SAT-class consideration: at what point does an actor's open-sourced tooling stop being a load-bearing attribution signal for downstream campaigns? Implications for VT-006 family lineage tracking and TeamPCP actor profile (roster #001, HIGH threat level).

3. **Co-attributor vendor primary retrieval** — THN relay names Wiz / JFrog / Microsoft / OX Security / SafeDep / StepSecurity / Aikido Security as co-attributors. None of these vendor primaries was directly retrieved at sweep time. Collector handoff: prioritize direct-retrieval of MSTIC + Wiz primary publications on next-cycle collection. If any MSTIC publication is identified, the cluster's effective source-reliability lifts from B to A.

4. **Red Hat IR-response gap** — Socket primary and THN relay both LACK Red Hat incident-response statement at sweep time. Red Hat's silence on whether the affected packages were officially Red Hat-published or community-published under the `@redhat-cloud-services` namespace is a quality-of-evidence concern. Watch signal active for Red Hat statement.

5. **Anthropic API C2 impersonation defensive operationalization** — DNS / cert-pinning verification path against Anthropic-legitimate infrastructure is required before blocking. A&D primes using Claude / Anthropic-API-based tooling must coordinate defender action with platform teams.

6. **VT-006 family ecosystem-expansion velocity** — three ecosystem expansions in ~20 days (2026-05-12, 2026-05-27, 2026-06-01). Analyst SAT-KAC class consideration: is the family in an active expansion phase, and what's the operational implication for defender prioritization?

---

## Analytic notes (from analyst review)

ACH on the operator-class question — explicitly framed at category level, not specific-actor-attribution level per Hard Rule 2 — ranks H2 (TeamPCP-tooling-leaked-and-reused) first with zero inconsistencies, tied with H4 (heterogeneous opportunistic cluster) and H5 (composite). H1 (TeamPCP-direct operator continuity) ranks LAST with three inconsistencies. Socket's explicit attribution-decline, the namespace targeting drift across the three family expansions, and the A-grade-vendor attribution silence all weakly contradict the same-operator reading. ACH reinforces, does not weaken, the grader's Hard-Rule-2 preservation. The brief must NOT inflate the TeamPCP tooling-lineage reference into Miasma-operator attribution; the reference is sourced (Socket verbatim) at the mechanism-class layer only.

KAC surfaces nine assumptions; A3 (@redhat-cloud-services packages in defense-prime dependency trees at material rate) is classified Test — the load-bearing premise on A&D-prime relevance with low-confidence and critical centrality. This is an inexpensive defender-side test (grep across npm dependency manifests); brief should elevate to defender pre-condition. Five additional Qualify caveats: A1 (open-sourced tooling breaks operator continuity), A2 (Anthropic-API C2 may not generalize as durable signature), A5 (co-attributor list may be reporter-aggregated), A6 (expansion-velocity may be observation cluster), A7 (Red Hat namespace ambiguity). The three Sound assumptions cover source-grading procedural questions.

Verdict: stands with brief caveat. Hard-Rule-2 attribution void is preserved and reinforced by ACH; A3 defender pre-condition check should be elevated.

---

## Extraction notes

- Cluster invoked admiralty-grading skill: yes
- Hard Rule 2 compliance: Socket EXPLICITLY declines Miasma-specific attribution; lineage-tooling reference to TeamPCP preserved verbatim; no novel attribution originated
- Hard Rule 3 compliance: no PoC code, exploit walkthrough, or attack-step guidance copied; mechanism class identified for defensive purposes only
- Hard Rule 4 compliance: no credential values stored or copied; campaign harvests credentials but published IOCs are payload-side artifacts
- Hard Rule 6 quote discipline: one Socket quote in finding prose (8 words on family identification); paraphrased throughout
- Hard Rule 8 first-party precedence: Splunk -30d zero substantive hits; first-party silent on Miasma-specific IOC set and api.anthropic[.]com C2 impersonation
- Single-source veto: applied on Miasma-specific operational layer and on 2026-05-29 first-detection date (THN-relay-only); WEP ceiling "likely" on these layers; family-identification layer carries A2 sub-grade via VT-006 corpus corroboration
