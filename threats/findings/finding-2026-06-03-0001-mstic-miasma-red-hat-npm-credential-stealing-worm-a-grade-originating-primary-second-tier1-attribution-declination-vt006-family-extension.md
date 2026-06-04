---
finding_id: finding-2026-06-03-0001-mstic-miasma-red-hat-npm-credential-stealing-worm-a-grade-originating-primary-second-tier1-attribution-declination-vt006-family-extension
created_at: 2026-06-03T08:18:00-04:00
graded_by: grader
grading_run_id: morning-20260603-080000
grading_mode: scheduled_brief
test: false
status: graded

relates_to:
  - finding-2026-06-02-0008-unit42-npm-threat-landscape-june-2-update-miasma-teampcp-attribution-hedge-tier1-corroboration-am-finding-0003-procedural-recheck
  - finding-2026-06-02-0003-securityweek-reversinglabs-aikido-ox-socket-miasma-red-hat-npm-32-package-vt006-extension-multi-firm-corroboration-oidc-cicd-vector
  - finding-2026-06-01-0004-socket-thn-miasma-mini-shai-hulud-redhat-cloud-services-npm-supply-chain-vt006-family-expansion-anthropic-impersonation-c2
relation_type: tier1_a_grade_originating_primary_with_second_attribution_declination_and_substantive_capability_lift

# Core grading (admiralty-grading skill output)
digraph: B1
digraph_layered:
  mstic_published_full_technical_writeup_of_red_hat_npm_miasma_campaign_with_first_party_defender_telemetry: A1   # MSTIC Tier-1 vendor research with named research team byline and first-party Defender + Microsoft Threat Intelligence telemetry; verifiable via direct URL retrieval
  affected_namespace_at_redhat_cloud_services_32_packages_compromised: A1                                          # SIX-vendor consensus now (MSTIC + Unit 42 + Socket + Ox Security + Aikido + ReversingLabs from 06-01 and 06-02 findings); procedural-facts independence test PASSES cleanly
  miasma_the_spreading_blight_campaign_marker_string: A1                                                            # MSTIC + Unit 42 + AM-finding-0003 four-vendor consensus on payload-embedded marker string; verifiable artifact
  variant_lineage_within_shai_hulud_family_vt006: A1                                                                # Internal corpus state via VT-006 anchor + Defender signature Trojan:JS/ShaiWorm.DAW!MTB family-taxonomic naming + Unit 42 Mini-Shai-Hulud-derivative framing; mechanism family signature consistent
  upstream_redhatinsights_javascript_clients_cicd_pipeline_compromise_as_initial_vector: A2                         # MSTIC sole originator on this specific upstream-pipeline-compromise framing; substantively-new vs. AM finding 0003 maintainer-account-compromise framing from Aikido; single-firm origination on the SPECIFIC vector
  preinstall_hook_4_29mb_dropper_script_with_aes_128_gcm_decryption: A2                                              # MSTIC sole originator on this specific dropper-mechanics detail; substantively-new vs. AM finding 0003 + Unit 42 mechanism-class framing
  bun_javascript_runtime_as_second_stage_execution_environment: A2                                                    # MSTIC sole originator on Bun-runtime mechanic; substantively-new
  destructive_tripwire_rm_rf_home_directory_on_decoy_token_invalidation: A2                                          # MSTIC sole originator on destructive-tripwire capability; NEW CAPABILITY CLASS not present in VT-006 / Mini Shai-Hulud per prior corpus state; single-firm origination
  sigstore_provenance_forgery_via_fulcio_and_rekor_oidc_token_exchange_for_publish_rights: A2                        # MSTIC sole originator on this specific Sigstore-forgery mechanism (vs. AM finding 0003 "SLSA-attestation breaking" framing — MSTIC adds the specific Sigstore Fulcio/Rekor mechanic + OIDC-token-exchange-for-publish-rights detail)
  dormant_anthropic_api_c2_endpoint_api_anthropic_com_v1_api_marked_noop_true: A2                                    # MSTIC corroborates Socket's prior api.anthropic[.]com observation from finding-2026-06-01-0004 (FIRST independent corroboration on this specific TTP — lifts from B2 single-source to B1 layered); MSTIC adds NEW DETAIL that the endpoint is currently DORMANT marked noop:true (held in reserve, not active exfil at MSTIC observation phase)
  sixteen_attacker_controlled_github_accounts_rotating_per_session: A2                                                # MSTIC sole originator on rotation-pool detail; substantively-new
  destructive_tripwire_decoy_honeytoken_string_ifyouinvalidatethistoken_substring: A1                                # MSTIC + Socket (finding-2026-06-01-0004 recorded "ifyouinvalidatethistoken" internal payload string) cross-corroborate on the honeytoken-string artifact at the substring level; verifiable artifact
  attribution_explicitly_withheld_by_mstic_no_nation_state_no_ecrime_cluster_no_named_actor_no_teampcp_extension: A1   # Verifiable absence in MSTIC body text; MSTIC named-research-team byline declines all attribution
  defender_signature_naming_trojan_js_shaiworm_daw_mtb_ties_malware_family_taxonomically_to_shai_hulud_family_but_signature_naming_is_not_actor_attribution: A1   # Verifiable in MSTIC text; explicit grader-side preservation that signature taxonomy is NOT actor attribution
  second_tier1_a_grade_vendor_explicitly_declines_teampcp_attribution_on_miasma_after_unit42_hedge_in_finding_0008: A1   # Verifiable internal corpus state across MSTIC + Unit 42; TWO Tier-1 A-grade vendors now decline TeamPCP attribution on Miasma vs. ZERO Tier-1 A-grade affirmations
  multi_platform_linux_macos_windows_with_linux_cicd_runners_as_primary_target: A1                                    # MSTIC + Unit 42 + AM-finding-0003 four-vendor consensus on multi-platform support; Linux-CI/CD-primary-target framing is MSTIC-strengthened consensus
  credential_theft_targets_github_npm_aws_azure_gcp_vault_kubernetes_circleci_anthropic_api_keys_ssh_browser_wallet: A1   # MSTIC + Socket (finding-2026-06-01-0004) + AM-finding-0003 consensus on credential-target scope at the category level; specific Anthropic API keys harvested = MSTIC new detail
  three_self_propagation_channels_victim_repo_drop_git_api_code_injection_oidc_package_republish_with_forged_provenance: A2   # MSTIC consolidates the three-channel framing; partial corroboration with AM finding 0003 OIDC vector + Channel A repo-drop with "Miasma" description observed by Wiz/Snyk on prior Shai-Hulud family campaigns; MSTIC structures as three discrete channels for first time
  npm_remediation_complete_redhat_cloud_services_namespace_hardened_github_invalidated_npm_tokens_with_write_2fa_bypass: A1   # MSTIC + AM finding 0003 + finding-2026-06-01-0004 consensus on remediation status; verifiable artifact (npm namespace state)
  ad_sector_indirect_relevance_via_redhat_cloud_services_dependency_graph_reach_at_ad_prime_cicd_pipelines: C2          # Grader-side structural inference; consistent with AM finding 0003 and Unit 42 framing; no A&D-prime named victim
  no_corpus_resident_mstic_surface_on_miasma_prior_to_this_raw_signal: A1                                              # Verifiable internal corpus state — MSTIC not previously surfaced on Miasma campaign in Archimedes corpus
  cluster_anchor: B1

digraph_anchor: >
  Cluster anchored on Microsoft Security Blog / MSTIC (Microsoft
  Defender Security Research Team named byline) full technical
  write-up "Preinstall to persistence: Inside the Red Hat npm
  'Miasma' credential-stealing campaign" (2026-06-02 16:45 PDT /
  2026-06-03 00:45 EDT, in-window). MSTIC is RATIFIED A per
  source-grades.yaml — this is the FIRST A-grade ORIGINATING
  PRIMARY on the Red Hat / Miasma campaign in Archimedes corpus
  with first-party Defender + Microsoft Threat Intelligence
  telemetry (Unit 42 in finding-2026-06-02-0008 was an A-grade
  monitor-post UPDATE; MSTIC is a full first-party technical
  write-up).

  B1 (not A1, not A2, not B2) anchored because:

    - SOURCE LETTER GRADE on the strongest corroborating primary
      is now A (MSTIC ratified A) joining the FIVE-vendor cluster
      from finding-2026-06-02-0008 (Unit 42 A + Socket B + Ox
      Security B + Aikido C + ReversingLabs C). The SIX-vendor
      consolidation lifts the cluster-anchor letter to B1 on
      procedural facts — addition of MSTIC A as SECOND Tier-1
      vendor (after Unit 42) reinforces the procedural-facts
      independence test, but the cluster contains C-grade members
      (Aikido, ReversingLabs from AM finding 0003) so cluster-
      anchor letter holds at B (not A) under conservative
      lowest-common-grade aggregation. Layered grading shows
      procedural-facts layer at A1 (six vendors, two A-grade
      Tier-1 with first-party telemetry).

    - The PROCEDURAL-FACTS layer (Miasma campaign existed;
      affected @redhat-cloud-services namespace; 32 packages
      compromised; Mini Shai-Hulud lineage; Miasma payload-
      embedded marker string) now CLEANLY carries 1 (Confirmed)
      because six independent vendors with different evidence
      bases corroborate (MSTIC first-party Defender + MS Threat
      Intelligence telemetry; Unit 42 monitor-post + variant-
      lineage analysis; Socket runtime; Ox Security downstream-
      repo enumeration; Aikido OIDC exploitation; ReversingLabs
      CI/CD compromise + publication-window forensics). Independence
      test PASSES on procedural facts.

    - The NOVEL CAPABILITY LAYERS first-published by MSTIC are
      SINGLE-FIRM-ORIGINATION at this hour:
        * destructive tripwire `rm -rf ~/` on decoy-token
          invalidation — NEW CAPABILITY CLASS not present in
          VT-006 / Mini Shai-Hulud per prior corpus state
        * Sigstore (Fulcio + Rekor) provenance forgery via
          OIDC token exchange — substantively-new vs. AM
          finding 0003 "SLSA-attestation breaking" framing
        * 16 attacker-controlled GitHub accounts rotating
          per session
        * Upstream RedHatInsights/javascript-clients CI/CD
          pipeline compromise as initial vector (vs. AM
          finding 0003 maintainer-account-compromise framing
          from Aikido)
        * Bun JavaScript runtime as second-stage execution
          environment
        * api.anthropic[.]com :443/v1/api endpoint marked
          DORMANT (noop:true) — held in reserve at MSTIC
          observation phase (MSTIC corroborates Socket's
          earlier finding-2026-06-01-0004 api.anthropic[.]com
          observation at substring level — FIRST independent
          corroboration on this specific TTP, lifts that
          layer from B2 single-source to B1 layered;
          dormancy-state detail is MSTIC sole-originator)
      These layers each carry single-firm origination at A
      (MSTIC sole originator) → A2 (Probably True, MSTIC-
      consistent with VT-006 family tradecraft, technical
      claims internally coherent, no contradicting A/B source).

    - The destructive-tripwire decoy-honeytoken string
      ("IfYouInvalidateThisTokenItWillNukeTheComputerOfTheOwner")
      cross-corroborates Socket's finding-2026-06-01-0004
      observation of "ifyouinvalidatethistoken" internal payload
      string at substring level — INDEPENDENT CORROBORATION on
      that specific artifact, lifts to A1.

    - The api.anthropic[.]com endpoint corroboration (MSTIC ↔
      Socket): both vendors observed the same Anthropic-API-
      surface impersonation/abuse endpoint. MSTIC adds the
      dormancy state (noop:true) which Socket did not report.
      This is the FIRST independent corroboration on Socket's
      finding-2026-06-01-0004 unique TTP detail, lifting that
      layer from B2 (Socket single-source) to B1 (MSTIC + Socket
      cross-corroborated, both Tier-1 / B-grade, different
      evidence bases). Note: api.anthropic.com is legitimate
      Anthropic API infrastructure — defender treatment is
      monitor-for-unusual-/v1/api-traffic-from-CI-runner-
      contexts, NOT generic blocklist.

    - The ATTRIBUTION LAYER carries SECOND A-grade Tier-1
      DECLINATION on TeamPCP-on-Miasma extension. After Unit 42's
      explicit hedge in finding-2026-06-02-0008 ("Attribution
      remains uncertain. The TTPs are consistent with TeamPCP,
      but the public release of the Mini Shai-Hulud source code
      means any competent actor can replicate the same attack."),
      MSTIC's body text contains ZERO mentions of TeamPCP, Mini
      Shai-Hulud campaign-attribution, TanStack/CVE-2026-45321
      campaign-attribution, or any nation-state / eCrime-cluster
      named-actor. The Defender signature naming `Trojan:JS/
      ShaiWorm.DAW!MTB` ties the malware family-taxonomically to
      the broader Shai-Hulud family — but signature taxonomy is
      NOT actor attribution per Hard Rule 2 discipline.

      TWO Tier-1 A-grade vendors (Unit 42 + MSTIC) now decline
      TeamPCP-on-Miasma. ZERO Tier-1 A-grade affirmations. The
      lower-grade affirmation chain that propagated through
      Aikido / Ox Security / ReversingLabs / Socket via
      SecurityWeek aggregation per AM finding 0003 is now
      bracketed by TWO A-grade Tier-1 declinations.

      For the VT-006 / Mini Shai-Hulud TanStack/CVE-2026-45321
      base campaign (NOT the Red Hat / Miasma extension), the
      Wiz + Snyk + StepSecurity affirmative TeamPCP attribution
      at "likely" WEP REMAINS in force per the VT-006 dossier
      state — those vendors published affirmative TeamPCP
      attribution on the BASE campaign; MSTIC's silence on
      Miasma extension does NOT unsay that. The grader / analyst
      / actor-profiler should preserve the distinction:
        * VT-006 / Mini Shai-Hulud TanStack base campaign:
          TeamPCP at "likely" (Wiz + Snyk + StepSecurity
          affirmative; no Tier-1 declination)
        * Red Hat / Miasma extension: TeamPCP UNATTRIBUTED
          (Unit 42 + MSTIC explicit Tier-1 declinations;
          Aikido / Ox / ReversingLabs / Socket affirmative
          chain bracketed but not refuted)

      Per Hard Rule 2: Archimedes does NOT originate TeamPCP
      attribution on Miasma. The Tier-1 declination chain is
      RATIFIED across the corpus as the dominant attribution
      stance on the Miasma extension; the lower-grade
      affirmation chain is preserved with citation but no
      longer carries forward as Archimedes' corpus-resident
      attribution stance.

  Single-source veto NOT applied on procedural-facts layer (six
  independent vendors, two Tier-1 A-grade with first-party
  telemetry). Single-source veto APPLIED on novel-capability
  layers (destructive tripwire, Sigstore forgery, 16-account
  rotation, upstream pipeline compromise, Bun runtime, dormant
  Anthropic C2 dormancy-state detail) — each is MSTIC sole-
  originator; WEP ceiling capped at "likely" on those specific
  TTPs per single-source veto. Single-source veto NOT applied
  on api.anthropic[.]com endpoint observation at endpoint-level
  (MSTIC + Socket cross-corroborated) — WEP ceiling lifted to
  "very_likely" on the endpoint-existence claim.

  Per Hard Rule 2: TWO Tier-1 A-grade declinations now bracket
  the Miasma attribution layer. Archimedes does NOT originate
  attribution; preserves the declination chain as the dominant
  corpus stance on Miasma extension. The VT-006 base-campaign
  TeamPCP attribution at "likely" is UNAFFECTED by Miasma
  extension declination per logical-scope discipline.

  Per Hard Rule 3: MSTIC publishes Advanced Hunting KQL queries
  for defensive detection. Defensive content URL is cited; full
  KQL not extracted into raw-signal beyond category-level
  references. Defender mitigation paths (CI/CD runner audit, npm
  token rotation, cloud-metadata-endpoint monitoring, outbound
  Bun-download monitoring) are described at category level.

  Per Hard Rule 6: MSTIC body text quoted ZERO times at >15
  words in finding text. Defender-signature names + decoy-token
  full substring + MSTIC named-team byline are all <15 words.

  Per Hard Rule 8: Splunk first-party check ran (-30d sweep
  across defenseclaw_local + archimedes-NOT-archimedes-internal
  on api.anthropic.com + Miasma + @redhat-cloud-services +
  ShaiWorm + polyapp + multiple Miasma IOC keywords). 0 events.
  First-party silence preserved as data point per the 20+-day
  non-archimedes-internal silent stream pattern, not
  disconfirming. Per Rule 8: absence of evidence is not
  evidence of absence.

source_reliability:
  grade: A
  source_name: Microsoft Security Blog / MSTIC (Microsoft Defender Security Research Team) — full technical write-up of the Red Hat npm "Miasma" credential-stealing supply-chain campaign
  source_yaml_id: mstic
  grade_rationale: >
    Pre-assigned A per source-grades.yaml — Microsoft MSTIC / MSRC,
    Tier-1 vendor, nation-state tracking, Defender telemetry-backed.
    This finding's MSTIC source is the named Microsoft Defender
    Security Research Team byline with first-party Defender + MS
    Threat Intelligence telemetry; full technical write-up class
    matches the A-grade evidentiary standard.
  provisional: false

credibility:
  grade: 1
  checklist_passed:
    - confirmed_independent_corroboration_six_vendors_on_procedural_facts
    - confirmed_neither_source_cites_other_as_origin_on_procedural_facts
    - confirmed_technical_artifacts_match_across_sources_namespace_marker_string_lineage
    - confirmed_no_contradicting_higher_grade_source_on_procedural_facts
    - probably_true_ttp_consistent_on_novel_capability_layers_via_vt006_family_tradecraft_anchor
    - probably_true_no_contradicting_ab_on_novel_capability_layers
    - probably_true_technical_claims_internally_coherent_throughout
  rationale: >
    Procedural-facts layer (Miasma campaign existed; affected
    @redhat-cloud-services namespace; 32 packages compromised; Mini
    Shai-Hulud lineage; "Miasma: The Spreading Blight" payload-
    embedded marker string) cleanly meets ALL grade-1 conditions
    across six independent vendors (MSTIC + Unit 42 + Socket + Ox
    Security + Aikido + ReversingLabs) with different evidence bases
    and no source citing another as origin. The api.anthropic[.]com
    endpoint observation is INDEPENDENTLY CORROBORATED for the
    first time (MSTIC + Socket). The destructive-tripwire decoy-
    honeytoken string cross-corroborates between MSTIC and Socket
    at substring level. Novel-capability layers (destructive
    tripwire, Sigstore forgery, 16-account rotation, upstream
    pipeline compromise, Bun runtime, dormant Anthropic C2
    dormancy-state) are MSTIC sole-originator and carry grade 2
    (Probably True) at LAYER level — TTP-consistent with VT-006
    family tradecraft, no contradicting A/B source, technical
    claims internally coherent. Cluster-anchor credibility holds
    at 1 on the procedural-facts layer; layered grading preserves
    distinct credibility on each novel-capability sub-claim per
    admiralty-grading skill Step 4 corroboration discipline.

corroboration:
  independent_sources:
    - mstic
    - unit42
    - socket-research-team
    - ox-security
    - aikido-security
    - reversinglabs
  independent: true
  test_passed: >
    On PROCEDURAL FACTS (namespace, package count, mechanism
    family, marker string, Mini-Shai-Hulud-lineage, multi-platform
    support, credential-target category set): six vendors are
    independent publishers; none cites another as origin; different
    evidence bases (MSTIC first-party Defender telemetry; Unit 42
    monitor-post lineage analysis; Socket runtime; Ox Security
    downstream-repo enumeration; Aikido OIDC exploitation; ReversingLabs
    CI/CD compromise forensics). Removing any one vendor: the others
    still stand independently on procedural facts. INDEPENDENCE TEST
    PASSES on procedural facts. On API.ANTHROPIC[.]COM endpoint
    observation: MSTIC + Socket cross-corroborate (different evidence
    bases — MSTIC first-party Defender; Socket runtime); INDEPENDENCE
    PASSES on this specific IOC. On NOVEL CAPABILITY LAYERS (destructive
    tripwire, Sigstore forgery via Fulcio/Rekor, 16-account rotation,
    upstream pipeline compromise, Bun runtime second-stage, dormancy-
    state detail): MSTIC sole originator; INDEPENDENCE NOT PASSED at
    layer level — single-source veto applies at WEP ceiling.
  test_failed: null

first_party_precedence:
  applied: false
  splunk_evidence: null
  splunk_query_run: >
    -30d sweep across defenseclaw_local + (archimedes NOT
    sourcetype=archimedes:*) on superset (api.anthropic.com,
    Miasma, @redhat-cloud-services, ShaiWorm, polyapp, multiple
    Miasma IOC keywords). 0 events. Per Hard Rule 8 silence is
    not disconfirming; first-party silence preserved as data
    point per the 20+-day non-archimedes-internal silent stream
    pattern.

single_source_veto_applied: true
single_source_veto_detail: >
  Applied at LAYER level on the novel-capability layers (destructive
  tripwire `rm -rf ~/`, Sigstore provenance forgery via Fulcio/Rekor,
  16 attacker-controlled GitHub accounts rotating per session,
  upstream RedHatInsights/javascript-clients CI/CD pipeline compromise
  as initial vector, Bun JavaScript runtime as second-stage execution
  environment, api.anthropic[.]com endpoint dormancy-state noop:true
  detail). Each is MSTIC sole-originator at this hour; WEP ceiling
  capped at "likely" per single-source veto. NOT applied at cluster-
  anchor level (six-vendor procedural-facts consensus + MSTIC/Socket
  cross-corroboration on api.anthropic[.]com endpoint existence).

wep_ceiling: very_likely
wep_layered:
  procedural_facts_layer_namespace_packages_marker_lineage_multiplatform_credential_categories: very_likely     # Six-vendor consensus; two Tier-1 A-grade with first-party telemetry; independence test passes
  api_anthropic_endpoint_existence_claim: very_likely                                                          # MSTIC + Socket cross-corroborated; endpoint-level corroboration
  destructive_tripwire_new_capability_class: likely                                                            # MSTIC sole-originator; single-source veto capped
  sigstore_provenance_forgery_via_fulcio_rekor_oidc_publish_rights: likely                                      # MSTIC sole-originator; single-source veto capped
  sixteen_account_rotation_pool: likely                                                                          # MSTIC sole-originator
  upstream_pipeline_compromise_vector: likely                                                                    # MSTIC sole-originator; conflicts with Aikido maintainer-account-compromise framing — different vector hypotheses; analyst should adjudicate
  bun_runtime_second_stage: likely                                                                              # MSTIC sole-originator
  api_anthropic_dormancy_state_noop_true_detail: likely                                                          # MSTIC sole-originator on dormancy-state detail
  attribution_layer_teampcp_on_miasma: unlikely                                                                  # TWO Tier-1 A-grade vendors decline TeamPCP-on-Miasma vs ZERO Tier-1 affirmations; corpus stance shifts toward "unlikely" on Miasma-specific TeamPCP attribution (NOT on VT-006 base campaign which retains Wiz+Snyk+StepSecurity affirmative at likely)
  defender_signature_family_taxonomic_link_shai_hulud: very_likely                                              # Verifiable in MSTIC text; signature naming consistent with corpus state; NOT actor attribution

inclusion:
  eligible_for:
    - flash
    - daily_brief_action
    - daily_brief_monitoring
    - weekly_synthesis
    - actor_profile_update
    - vuln_tracker_dossier_update

# Cluster metadata
cluster:
  topic: >
    MSTIC publishes A-grade originating primary technical write-up
    on the Red Hat npm "Miasma" credential-stealing supply-chain
    campaign with substantial capability lift (destructive tripwire,
    Sigstore forgery via Fulcio/Rekor, 16-account rotation, upstream
    pipeline compromise vector, Bun runtime, dormant Anthropic C2)
    AND explicitly declines TeamPCP attribution — SECOND Tier-1
    A-grade declination after Unit 42 in finding-2026-06-02-0008.
  cluster_size: 1
  raw_signal_members:
    - raw-2026-06-03-am-001-mstic-miasma-red-hat-npm-credential-stealing-worm-vt006-family-a-grade-originating-primary-no-teampcp-attribution
  attribution_claims:
    - claimed_actor: null
      claim_text: >
        MSTIC does not attribute the Miasma campaign to any
        nation-state, eCrime cluster, or named actor. Threat is
        identified solely by embedded marker "Miasma: The Spreading
        Blight." MSTIC's body text contains zero mentions of
        TeamPCP, Mini Shai-Hulud, TanStack, or CVE-2026-45321 as
        actor-attribution links.
      claimed_by_sources:
        - mstic
      requires_analyst_review: true
      hard_rule_2_status: PRESERVED — verifiable absence of attribution; MSTIC named-research-team byline explicitly declines
    - claimed_actor: shai-hulud-family
      claim_text: >
        Defender signature naming `Trojan:JS/ShaiWorm.DAW!MTB` ties
        the malware FAMILY-TAXONOMICALLY to the broader Shai-Hulud
        family. This is signature taxonomy, NOT actor attribution.
        Family-taxonomic linkage does NOT extend prior VT-006 /
        Mini Shai-Hulud TeamPCP-at-likely attribution to the Red
        Hat / Miasma campaign.
      claimed_by_sources:
        - mstic
      requires_analyst_review: true
      hard_rule_2_status: PRESERVED — signature naming is family taxonomy at malware-class level; Archimedes does NOT extend prior-campaign attribution to current campaign via signature-family linkage
    - claimed_actor: null
      claim_text: >
        TWO Tier-1 A-grade vendors (Unit 42 in finding-2026-06-02-0008
        + MSTIC in this finding) now explicitly decline TeamPCP
        attribution on Red Hat / Miasma extension. ZERO Tier-1
        A-grade affirmations. Lower-grade affirmation chain
        (Aikido C + Ox Security B + ReversingLabs C + Socket B via
        SecurityWeek aggregation per AM finding 0003) is BRACKETED
        by Tier-1 declinations.
      claimed_by_sources:
        - mstic
        - unit42
      requires_analyst_review: true
      hard_rule_2_status: PRESERVED — Archimedes does NOT originate TeamPCP attribution on Miasma; preserves Tier-1 declination as dominant corpus stance on Miasma extension; VT-006 base-campaign TeamPCP attribution at "likely" UNAFFECTED by Miasma extension declination

# Downstream handoff flags
analyst_review_required: true
analyst_review_rationale: >
  (a) ATTRIBUTION-DIVERGENCE event: SECOND Tier-1 A-grade vendor
  declines TeamPCP-on-Miasma. Analyst SAT-ACH warranted on the
  competing hypotheses — "Miasma is TeamPCP" (lower-grade chain) vs.
  "Miasma is a separate-actor Shai-Hulud-family extension" (Tier-1
  declination chain implication) vs. "Miasma is post-public-source-
  code-release competent-actor replication" (Unit 42 explicit
  hedge). SAT-KAC warranted on the assumption that Tier-1 silence-
  with-Defender-signature-tag is equivalent to Tier-1 attribution-
  declination (vs. alternative reading that Tier-1 vendors simply
  haven't completed attribution analysis yet — which would imply
  the Tier-1 "declination" is incomplete-assessment rather than
  affirmative-declination).

  (b) WEP LIFT EVENT on the procedural-facts layer for the entire
  Miasma cluster from B1 (five-vendor) to A1 (six-vendor with two
  Tier-1 A-grade including first-party MSTIC Defender telemetry).
  Analyst should formally recheck finding-2026-06-02-0008 +
  finding-2026-06-02-0003 procedural-facts WEP lift through this
  finding's six-vendor consolidation.

  (c) NOVEL CAPABILITY layers (destructive tripwire, Sigstore
  forgery, upstream pipeline compromise vs maintainer-account
  compromise, dormant Anthropic C2 dormancy-state) warrant SAT-
  class consideration — particularly the upstream-pipeline-
  compromise framing from MSTIC vs the maintainer-account-
  compromise framing from Aikido (these are DIFFERENT initial
  vectors and analyst should adjudicate which framing is correct
  or whether both are present in different sub-clusters).

  (d) DESTRUCTIVE TRIPWIRE is a new capability class for the
  Shai-Hulud family — analyst should consider whether VT-006
  dossier capability tracking warrants explicit "destructive
  capability" axis addition and whether the destructive-tripwire
  presence shifts the family's risk classification.

red_team_review_required: true
red_team_review_rationale: >
  WEP ceiling at "very_likely" on procedural-facts layer (six-
  vendor consolidation including two Tier-1 A-grade with first-
  party telemetry) meets red-team invocation floor. Red-team
  should:

  (a) Argue against the procedural-facts layer "very_likely" WEP
  lift — does MSTIC's first-party Defender telemetry + Unit 42
  monitor-post + four B/C vendor cluster genuinely lift to "very
  likely" given that ALL six vendors are tracing the same Red
  Hat / npm public-record event surface? Independence test on
  evidence bases could be argued as theatrical-independence-
  with-substantive-shared-origin (the @redhat-cloud-services
  npm namespace state is observable to all six vendors;
  independence is on analysis evidence, not on observation
  evidence).

  (b) Argue against the "Tier-1 declination = corpus attribution
  shift" framing — does MSTIC's silence-with-signature-tag on
  TeamPCP attribution constitute affirmative declination or
  merely incomplete-assessment? Unit 42's explicit verbatim hedge
  IS affirmative declination; MSTIC's silence with family-
  taxonomic signature tag is ambiguous. Red-team should adjudicate
  whether the "TWO Tier-1 declinations" framing overweights
  MSTIC's silence.

  (c) Argue against the destructive-tripwire capability lift on
  the VT-006 family risk classification — does ONE MSTIC sole-
  originator observation of a destructive tripwire on ONE Miasma-
  family extension justify family-level risk reclassification?
  Or should the destructive tripwire be treated as Miasma-extension-
  specific until corroborated on other Shai-Hulud family campaigns?

  (d) Argue against the api.anthropic[.]com cross-corroboration
  (MSTIC + Socket) — both vendors observed the endpoint, but
  MSTIC observed it as DORMANT (noop:true) and Socket observed
  it as ACTIVE (per finding-2026-06-01-0004). Is this:
  (i) campaign state-transition (was active, now dormant);
  (ii) different observation windows (Socket caught active phase,
  MSTIC caught dormant phase); (iii) the SAME observation with
  different interpretations; (iv) actually DIFFERENT endpoints
  on the same host with different operational states. Red-team
  should adjudicate.

red_team_review:
  reviewed_at: 2026-06-03T09:02:00-04:00
  reviewed_by: red-team-analyst
  run_id: red-team-20260603-090200
  recommendation: sign_off
  outcome: sign_off_with_qualifications

  strongest_counter_hypothesis:
    hypothesis: >
      Contrarian H1 reinstatement: TeamPCP authored AND operates the
      Miasma extension; both Tier-1 vendors are simply early in their
      attribution pipelines and the lower-grade chain (post-SecurityWeek-
      aggregation) has the substantive read right.
    evidence_for_counter:
      - >
        Unit 42's verbatim language is "TTPs consistent with TeamPCP" +
        "any competent actor can replicate" — this is an UNCERTAINTY
        statement, not an exclusion. Reframing E2 from I→N for H1 under
        a strict reading drops H1 weighted inconsistency from 12 to 9.
      - >
        MSTIC's Defender signature naming uses the Shai-Hulud family
        taxonomy explicitly. While signature taxonomy ≠ actor attribution
        per Hard Rule 2, MSTIC chose this naming over a Miasma-specific
        family — consistent with a vendor that sees family continuity.
      - >
        MSTIC body-text silence is empirically ambiguous; KAC A1's
        alternative reading (editorial scope / customer-feed deferral /
        in-progress) is a real failure mode for the I-assignment on E1.
        Reframing E1 from I→N drops H1 weighted inconsistency by 3 more.
    evidence_against_counter:
      - >
        Even under aggressive reinterpretation of E1+E2 (both flipped
        I→N), H1 still carries 5 weighted inconsistencies (E3 weight 2
        + E5 weight 3), versus H4 at 0 and H2/H5 at 1. Ranking unchanged.
      - >
        E3 (Socket primary declination) is DIRECTLY RETRIEVED text, not
        an inference about silence. Socket's own primary says
        "attribution remains unclear, as the publicly available tooling
        lowers the barrier to entry." This is verbatim — H1 cannot
        recover E3 absent a Socket walk-back.
      - >
        The lower-grade chain's "TeamPCP-affirmative" reading rests on
        SecurityWeek's framing of Aikido / Ox / ReversingLabs — and the
        underlying primaries are NOT directly retrieved. The single
        directly-retrieved primary in that chain (Socket) contradicts
        SecurityWeek's framing of itself.

  contrarian_ach_run:
    same_matrix_h1_ranking: rank_5_unchanged
    h1_weighted_inconsistencies_under_aggressive_reinterpretation: 5
    h1_weighted_inconsistencies_per_analyst: 12
    delta_under_contrarian_assumptions: -7
    delta_sufficient_to_flip_ranking: false
    load_bearing_evidence_for_h1_block: >
      E3 (Socket primary declination, directly retrieved, B2, weight 2)
      and E5 (MSTIC novel-capabilities documentation, A2, weight 3) are
      the two anchors that hold H1 in last place under any single-source
      reinterpretation. E3 is the more decisive of the two because it is
      not subject to silence-interpretation ambiguity — Socket affirmatively
      wrote "attribution remains unclear." A Socket walk-back is the
      tripwire that would flip the ranking; absent that, H1 stays last.

  weaknesses_in_primary_assessment:
    - >
      The "TWO Tier-1 affirmative declinations" framing as originally
      drafted by the grader overweights Unit 42 by approximately half a
      notch. Unit 42's verbatim is an UNCERTAINTY statement
      ("attribution remains uncertain") not an EXCLUSION
      ("not TeamPCP"). The honest framing is ONE Tier-1 explicit
      uncertainty (Unit 42) + ONE Tier-1 silence-with-family-signature-
      tag (MSTIC). Analyst's KAC A1 partially captures this by
      downgrading MSTIC silence to "secondary-strength"; red-team
      further notes Unit 42's hedge itself is uncertainty-strength, not
      exclusion-strength. Brief language should say "two Tier-1 vendors
      decline to affirm TeamPCP" or "two Tier-1 vendors leave
      attribution open" — NOT "two Tier-1 declinations" which implies
      affirmative rejection neither vendor wrote.
    - >
      "Six independent vendors" overstates the corroboration topology.
      Only THREE primaries are directly retrieved (MSTIC, Unit 42,
      Socket). Three (Aikido C + Ox B + ReversingLabs C) enter the
      corpus through ONE SecurityWeek B-grade relay aggregation per
      finding-2026-06-02-0003, whose own grader explicitly noted "Ox
      primary not directly retrieved." This is correlation through a
      common relay, not six-way independence. The procedural-facts WEP
      lift to "very_likely" survives ONLY because the three
      directly-retrieved primaries (MSTIC A first-party Defender + Unit
      42 A monitor-post + Socket B runtime, three genuinely independent
      evidence bases) ALREADY satisfy "very_likely" without the
      SecurityWeek-aggregated three. The aggregated three are
      corroborative-but-not-independent-of-each-other. Briefer should
      not lean on the "six-vendor consensus" phrasing — should anchor
      on the three directly-retrieved primaries.
    - >
      KAC A3 correctly identifies that Socket did NOT empirically
      state-flag api.anthropic[.]com as ACTIVE in finding-2026-06-01-0004.
      Socket described the endpoint as "primary C2" with
      "role: c2_exfiltration_primary" — these are STRUCTURAL
      designations (this is what the malware tries to use) NOT runtime
      state flags (this is what we saw it doing at observation time).
      The "Socket active vs. MSTIC dormant" framing the grader
      surfaced in red-team prompt (d) is reading runtime state into
      Socket's role labels. The state-transition narrative should NOT
      appear in the brief; analyst's KAC A3 remediation is correct.
    - >
      KAC A4 correctly identifies that the destructive tripwire is
      conditional (fires on decoy-token interaction) — tradecraft
      protection, not operational destructive capability. Red-team
      affirms: family-level risk-classification lift on VT-006 from
      ONE MSTIC observation on ONE family extension is structurally
      unsound. The single-source veto already caps this capability at
      "likely" at extension-level; family-level propagation requires
      cross-campaign corroboration. Analyst's remediation is correct.

  strongest_counter_wep: roughly_even_chance   # what H1's WEP would be IF the contrarian reinterpretation of E1+E2 held — still doesn't lead

  qualifying_language_required:
    - >
      Brief MUST avoid the phrase "two Tier-1 declinations" — it
      implies affirmative rejection. Use "two Tier-1 vendors decline
      to affirm TeamPCP attribution on Miasma" or "two Tier-1 vendors
      leave the Miasma operator open" (Unit 42 explicit uncertainty +
      MSTIC silence-with-family-signature-tag).
    - >
      Brief MUST avoid the "six-vendor consensus" phrasing as the
      lead. Anchor instead on "three directly-retrieved primaries
      (MSTIC first-party Defender telemetry + Unit 42 monitor-post +
      Socket runtime) with three additional vendor primaries (Aikido,
      Ox, ReversingLabs) entering via SecurityWeek aggregation." The
      WEP lift survives on the three retrieved primaries' independence
      alone.
    - >
      Brief MUST NOT advance the "api.anthropic[.]com state-transition
      (active → dormant)" narrative. Defensible single line is: "MSTIC
      documents api.anthropic[.]com:443/v1/api in the Miasma payload
      configured noop:true (held in reserve); defender action is
      MONITOR-for-unusual-/v1/api-traffic-from-CI-runner contexts; DO
      NOT generic-blocklist (legitimate Anthropic API infrastructure)."
      Treat as latent-live, not confirmed-dead. Do NOT compare to
      Socket's prior observation as a state change.
    - >
      Brief MUST frame destructive tripwire as MIASMA-EXTENSION-LEVEL
      capability only, NOT family-level lift to VT-006. Capability
      framing should be "destructive tradecraft protection" (fires on
      decoy-token interaction), NOT "destructive operational
      objective." VT-006 family risk axis change requires corroboration
      on at least one non-Miasma Shai-Hulud campaign.

  specific_tests_that_would_resolve:
    - >
      Direct retrieval of Aikido, Ox Security, ReversingLabs primary
      publications. If their primaries do NOT in fact affirm TeamPCP
      on Miasma (i.e., SecurityWeek aggregation is misframing them),
      H1's only support (E7) collapses, and the contrarian case for
      H1 fails decisively rather than just narrowly. Briefer should
      flag this as a follow-up retrieval task.
    - >
      A second Tier-1 vendor independently documents a destructive
      tripwire on a NON-Miasma Shai-Hulud family campaign. Lifts E5
      from MSTIC-sole-originator; warrants family-level VT-006
      capability axis addition.
    - >
      MSTIC or Unit 42 publishes an affirmative-attribution follow-up
      (either TeamPCP-on-Miasma confirmed or named-actor declination
      explicit). Resolves the silence-vs-declination ambiguity in
      KAC A1.
    - >
      Socket publishes a runtime-state follow-up on
      api.anthropic[.]com — specifically whether their observation
      window captured payload-configured-active or
      payload-configured-noop-true. Resolves KAC A3.

  wep_adjustment_recommended: null   # cluster-level WEP unchanged
  wep_adjustment_rationale: >
    Procedural-facts very_likely SURVIVES contrarian pressure. The lift
    is defensible on the three directly-retrieved primaries (MSTIC A
    first-party Defender telemetry + Unit 42 A monitor-post + Socket B
    runtime — three distinct evidence bases, no source citing another)
    independent of the SecurityWeek-aggregated three. Attribution-layer
    "Miasma unattributed" at very_likely SURVIVES with the qualifying
    language above. H1 (TeamPCP-on-Miasma affirmative) stays at
    "unlikely" — even under aggressive contrarian reinterpretation of
    MSTIC silence + Unit 42 hedge, H1 still carries 5 weighted
    inconsistencies via E3 (Socket primary directly-retrieved
    declination) + E5 (MSTIC novel capabilities); ranking unchanged.

  hard_rule_2_check:
    contrarian_did_not_originate_attribution: true
    h1_contrarian_case_argues_against_decline_framing: true
    h1_contrarian_case_does_not_advance_h4_or_h3: true
    affirmation: >
      Red-team's contrarian case argued for the lower-grade chain's
      reading of TeamPCP attribution — which IS a cited-source claim
      (Aikido/Ox/ReversingLabs via SecurityWeek). Red-team did NOT
      originate H4 (TeamPCP-adjacent cluster) or H3 (null hypothesis)
      as positive corpus stances. Red-team pressure-tested the
      analyst's ranking; the analyst's framing held.

  notes: >
    SIGN-OFF. Contrarian ACH ran from H1's position; matrix arithmetic
    holds — H1 ranking unchanged at rank 5 / last even under aggressive
    single-source reinterpretation. The two surviving red-team
    contributions: (1) the framing "TWO Tier-1 declinations" overstates
    by half a notch — Unit 42 wrote uncertainty, not exclusion;
    briefer must use "decline to affirm" language; (2) "six-vendor
    consensus" phrasing is structurally misleading because three of
    the six enter via one SecurityWeek aggregation; briefer must
    anchor on the three directly-retrieved primaries. Neither is
    block-worthy; both are qualify-in-brief-language. Analyst's KAC
    A1 / A3 / A4 / A5 remediations are all correct. Defensive single
    line on api.anthropic[.]com (analyst KAC A3 framing) is the right
    call — temporary host-level block would break legitimate Anthropic
    API consumption with material collateral damage; defender treatment
    is hunt-on-pattern (path + CI-runner context), not block-on-host.
    Procedural-facts WEP at very_likely holds.

# Analyst review outcome (analyst subagent)
analyst_review_complete: true
analyst_review_run_id: analyst-20260603-084200
sats_applied: [sat-ach, sat-kac]
wep_ceiling_adjusted: very_likely   # unchanged at cluster level; per-layer adjustments tracked in wep_layered_post_analyst below
wep_ceiling_adjustment_reason: >
  Procedural-facts WEP at "very_likely" survives sensitivity testing
  (six-vendor consolidation; matrix robust under single-source
  reinterpretation). Attribution-divergence framing should ship at
  "very_likely on corpus stance Miasma-unattributed" with KAC A1
  qualifying caveat replacing "SECOND Tier-1 affirmative declination"
  with "SECOND Tier-1 silence-with-family-signature-tag interpretable
  as declination in context of Unit 42 adjacent hedge." H1 (TeamPCP-
  on-Miasma affirmative) carries 12 weighted inconsistencies and
  ranks last; "unlikely" on H1 is structurally supported. Per Hard
  Rule 2 the matrix rank-1 hypothesis (H4 TeamPCP-adjacent cluster)
  is NOT advanced as Archimedes corpus stance — no cited source
  advances it. Per-layer adjustments applied to four KAC-qualify
  layers (initial vector composite framing; api.anthropic state
  reframed as latent-live; destructive tripwire extension-level
  only; base TeamPCP attribution unaffected).
wep_layered_post_analyst:
  procedural_facts_layer: very_likely
  api_anthropic_endpoint_existence: very_likely
  attribution_layer_miasma_unattributed_corpus_stance: very_likely
  attribution_layer_teampcp_on_miasma_affirmation: unlikely
  destructive_tripwire_miasma_extension_level: likely
  destructive_tripwire_family_level_propagation_to_vt006: not_advanced_per_kac_a4
  upstream_pipeline_compromise_as_sole_initial_vector: likely_but_qualified_per_kac_a2  # treat as composite with OIDC path
  api_anthropic_state_transition_active_to_dormant_narrative: not_advanced_per_kac_a3   # Socket did not state-flag
  vt006_base_teampcp_attribution: likely_unchanged_per_kac_a6
assessment_blocked_pending_test: false
red_team_review_still_required: false
red_team_review_complete: true
red_team_outcome: sign_off
red_team_wep_adjustment: null
red_team_publication_blocked: false
red_team_review_supplemental_prompts:
  - >
    Red-team should explicitly adjudicate KAC A1 (whether MSTIC silence
    is affirmative declination vs. incomplete-assessment vs. editorial-
    scope) before publication. The grader's red-team prompt (b)
    already covers this — analyst confirms the question is load-
    bearing.
  - >
    Red-team should explicitly adjudicate KAC A3 (api.anthropic state-
    transition narrative). Analyst flags that the "Socket active vs.
    MSTIC dormant" framing in the grader's red-team prompt (d) rests
    on inference about Socket's prior observation that Socket itself
    did not state-flag in finding-2026-06-01-0004. Red-team should
    not treat the state-transition narrative as established before
    adjudication.
  - >
    Red-team should consider whether KAC A4 (destructive tripwire as
    "tradecraft protection" not "operational destructive objective")
    is the correct framing. The current evidence is one MSTIC-
    documented conditional tripwire fired by decoy-token interaction;
    not unconditional destructive operation. Vuln-tracker handoff
    should distinguish these axes when updating VT-006 or scaffolding
    VT-011.
  - >
    Per Hard Rule 2: the ACH matrix's rank-1 hypothesis (H4 TeamPCP-
    adjacent cluster) is NOT advanced by any cited source. Red-team
    should confirm that no analyst- or red-team-side framing in the
    final brief inadvertently advances H4 as a positive corpus
    stance. Matrix arithmetic does not create attribution.

analysis_sections:
  sat_ach:
    ach_analysis:
      question: >
        Given two Tier-1 A-grade vendor declinations (MSTIC silence with
        family-taxonomic signature tag + Unit 42 explicit hedge) on the
        Red Hat / Miasma extension and a lower-grade affirmative chain
        (Aikido C + Ox B + ReversingLabs C + Socket B) via SecurityWeek
        aggregation, what is the most defensible corpus stance on
        TeamPCP attribution to the Miasma extension (distinct from the
        VT-006 base campaign)?
      analyzed_at: 2026-06-03T08:42:00-04:00
      analyzed_by: analyst
      analyst_run_id: analyst-20260603-084200
      red_team_review: null

      hypotheses:
        - id: H1
          statement: >
            TeamPCP authored AND operates the Miasma extension; the
            lower-grade affirmative chain is correct and the two Tier-1
            declinations reflect analytic conservatism / pre-publication
            holdback rather than substantive disagreement.
          source_basis: >
            Aikido / Ox / ReversingLabs / Socket affirmative chain per
            SecurityWeek aggregation in finding-2026-06-02-0003. (Note:
            Socket's directly-retrieved primary in finding-2026-06-01-0004
            EXPLICITLY declines Miasma attribution to TeamPCP; "Socket
            affirmative" via SecurityWeek aggregation may be reporter
            misframing — see KAC A2.)
        - id: H2
          statement: >
            TeamPCP authored only the VT-006 base TanStack / Mini Shai-
            Hulud campaign; a SEPARATE operator extended the toolchain
            into the Red Hat / Miasma campaign after public release of
            the Mini Shai-Hulud source code lowered the replication
            barrier.
          source_basis: >
            Unit 42 explicit verbatim hedge in finding-2026-06-02-0008
            ("public release of the Mini Shai-Hulud source code means
            any competent actor can replicate the same attack"). MSTIC
            silence is consistent with but does not affirmatively state
            this hypothesis.
        - id: H3
          statement: >
            Both VT-006 base campaign and Miasma extension are co-
            operated by an unattributed actor (or actor cluster); the
            TeamPCP-on-base attribution from Wiz + Snyk + StepSecurity is
            itself a misattribution thread propagated forward, and the
            Miasma extension Tier-1 declination is the leading edge of a
            broader attribution correction.
          source_basis: >
            No cited source advances this. Included as null hypothesis
            against confirmation bias. Per Hard Rule 2, Archimedes does
            NOT advance this hypothesis as a corpus stance; it exists
            in the matrix only to test the robustness of H2.
        - id: H4
          statement: >
            The Miasma extension is operated by a TeamPCP-adjacent
            cluster (e.g., affiliate or splinter) whose tradecraft
            overlaps with TeamPCP enough to register on the lower-grade
            family-signature-driven chain but not enough for MSTIC /
            Unit 42 to extend formal attribution.
          source_basis: >
            No cited source advances this. Included as composite
            hypothesis; sits between H1 and H2. Per Hard Rule 2, NOT
            advanced as corpus stance; exists in matrix to absorb the
            "tradecraft consistent but not affirmable" middle ground
            Unit 42's hedge gestures at.
        - id: H5
          statement: >
            The Miasma extension is operated by an opportunistic actor
            that downloaded the public Mini Shai-Hulud source after
            release, modified it (Sigstore forgery, Bun runtime,
            destructive tripwire, 16-account rotation are extension-
            specific additions), and ran it against @redhat-cloud-
            services as a target of opportunity rather than as a
            TeamPCP-directed operation.
          source_basis: >
            Unit 42 explicit hedge framing (replication-by-competent-
            actor). MSTIC's documentation of substantive novel
            capabilities not present in VT-006 base is consistent with
            but does not affirmatively state this hypothesis.

      evidence:
        - id: E1
          description: >
            MSTIC body text contains ZERO mentions of TeamPCP, Mini
            Shai-Hulud campaign-attribution, TanStack / CVE-2026-45321
            campaign-attribution, or any nation-state / eCrime-cluster
            named-actor on Miasma.
          source: mstic (this finding)
          digraph: A1
          weight: 3
        - id: E2
          description: >
            Unit 42 verbatim hedge: attribution remains uncertain;
            TTPs consistent with TeamPCP; public source code release
            means any competent actor can replicate.
          source: unit42 (finding-2026-06-02-0008)
          digraph: A1
          weight: 3
        - id: E3
          description: >
            Socket's directly-retrieved primary (finding-2026-06-01-0004)
            EXPLICITLY declines Miasma-specific attribution to TeamPCP
            ("Attribution remains unclear, as the publicly available
            tooling lowers the barrier to entry"). TeamPCP named only
            as prior-campaign open-sourcer of underlying tooling.
          source: socket (finding-2026-06-01-0004)
          digraph: B2
          weight: 2
        - id: E4
          description: >
            Defender signature naming `Trojan:JS/ShaiWorm.DAW!MTB` ties
            Miasma malware family-taxonomically to broader Shai-Hulud
            family.
          source: mstic (this finding)
          digraph: A1
          weight: 3
        - id: E5
          description: >
            Substantive novel capability layers not present in VT-006
            base per prior corpus state — destructive tripwire
            (`rm -rf ~/`), Sigstore Fulcio/Rekor provenance forgery via
            OIDC token exchange, 16 GitHub accounts rotating per
            session, Bun JavaScript runtime second-stage, upstream
            RedHatInsights/javascript-clients pipeline compromise vs.
            maintainer-account-compromise vector.
          source: mstic (this finding)
          digraph: A2
          weight: 3
        - id: E6
          description: >
            "Miasma: The Spreading Blight" payload-embedded marker
            string consistent across MSTIC + Unit 42 + Socket; campaign
            marker is internally coherent across vendors.
          source: mstic + unit42 + socket
          digraph: A1
          weight: 3
        - id: E7
          description: >
            SecurityWeek-aggregated lower-grade chain (Aikido C + Ox B +
            ReversingLabs C + Socket B via SecurityWeek) — the
            "affirmative TeamPCP-on-Miasma" reading. NOTE: Socket
            primary itself declines attribution per E3; SecurityWeek
            aggregation may overstate Socket's stance. ReversingLabs +
            Aikido + Ox primaries not directly retrieved.
          source: securityweek aggregation (finding-2026-06-02-0003)
          digraph: C3
          weight: 1
        - id: E8
          description: >
            Wiz + Snyk + StepSecurity affirmative TeamPCP attribution on
            VT-006 BASE campaign (TanStack / CVE-2026-45321 / Mini Shai-
            Hulud) at "likely" WEP per VT-006 corpus state. Distinct
            campaign from Miasma extension.
          source: wiz + snyk + stepsecurity (VT-006 dossier corpus state)
          digraph: A2
          weight: 3
        - id: E9
          description: >
            Mini Shai-Hulud source code is publicly released per Unit 42
            verbatim attestation — replication-by-competent-actor is
            technically feasible. (Underlying premise behind H2 / H4 /
            H5.)
          source: unit42 (finding-2026-06-02-0008)
          digraph: A1
          weight: 3
        - id: E10
          description: >
            No first-party Splunk telemetry on Miasma campaign IOCs in
            -30d sweep across defenseclaw_local + archimedes-NOT-
            archimedes-internal. Absence of first-party data.
          source: archimedes splunk (this finding)
          digraph: A1
          weight: 1   # absence of data is weight-1 — informative but not strong evidence either direction

      matrix:
        E1: {H1: I, H2: C, H3: C, H4: C, H5: C}   # MSTIC silence inconsistent with H1 (would expect attribution if straightforward TeamPCP)
        E2: {H1: I, H2: C, H3: N, H4: C, H5: C}   # Unit 42 hedge inconsistent with confident H1
        E3: {H1: I, H2: C, H3: N, H4: C, H5: C}   # Socket primary inconsistent with H1
        E4: {H1: C, H2: C, H3: N, H4: C, H5: C}   # family-taxonomic signature is consistent with all family-derivative hypotheses; NON-DIAGNOSTIC across H1/H2/H4/H5
        E5: {H1: I, H2: C, H3: N, H4: C, H5: C}   # substantive novel capabilities argue for forked development OR separate operator
        E6: {H1: C, H2: C, H3: N, H4: C, H5: C}   # marker string consistent with all family-derivative hypotheses; NON-DIAGNOSTIC
        E7: {H1: C, H2: I, H3: I, H4: N, H5: I}   # lower-grade affirmative chain only consistent with H1; but E7's own grade is C3
        E8: {H1: C, H2: C, H3: I, H4: C, H5: C}   # base-campaign TeamPCP affirmative; rules out H3
        E9: {H1: N, H2: C, H3: C, H4: C, H5: C}   # public source release enables H2/H4/H5; non-diagnostic against H1
        E10: {H1: N, H2: N, H3: N, H4: N, H5: N}  # NON-DIAGNOSTIC — Hard Rule 8 absence of evidence

      inconsistency_counts:
        H1: 4   # E1, E2, E3, E5 — all Tier-1 / primary direct retrieval evidence argues against
        H2: 1   # E7 — bracketed lower-grade chain; weight 1
        H3: 1   # E8 — base-campaign attribution; weight 3
        H4: 0
        H5: 1   # E7

      weighted_inconsistency_scores:
        H1: 12   # E1(3) + E2(3) + E3(2) + E5(3) — heavy weighted contradiction
        H2: 1    # E7 weight 1
        H3: 3    # E8 weight 3 — strong weighted contradiction via base-campaign attribution
        H4: 0
        H5: 1    # E7 weight 1

      diagnostic_evidence:
        - E1: >
            HIGHEST diagnostic value. MSTIC silence is consistent with
            H2/H4/H5 (separate operator or replicator) but inconsistent
            with H1 (straightforward TeamPCP). E1 is the load-bearing
            piece for the Tier-1 declination chain framing — and per
            KAC A1 the interpretation of E1 is itself an assumption.
        - E5: >
            HIGH diagnostic value. Substantive novel capabilities
            (destructive tripwire, Sigstore forgery, Bun runtime, 16-
            account rotation, upstream pipeline vector) argue for
            either forked TeamPCP development (still H1) or separate
            operator extension (H2/H4/H5). Less diagnostic between H1
            and H2/H4/H5 than E1.
        - E2: >
            HIGH diagnostic value. Unit 42 explicit hedge is direct
            verbatim evidence; not subject to interpretation ambiguity
            like E1.
        - E8: >
            HIGH diagnostic value. Rules out H3 (the "no actor"
            hypothesis) at weight 3.
        - E4 + E6: >
            NON-DIAGNOSTIC. Family-taxonomic signature naming and
            marker string consistency are consistent with all
            family-derivative hypotheses (H1/H2/H4/H5). These do NOT
            distinguish operator hypotheses; they distinguish
            family-membership from non-family-membership (which is not
            in dispute).
        - E10: >
            NON-DIAGNOSTIC per Hard Rule 8. Absence of first-party
            telemetry preserved as data point, not evidence either
            direction.

      ranking:
        - rank: 1
          hypothesis_id: H4
          rationale: >
            Zero inconsistencies (composite "TeamPCP-adjacent cluster"
            absorbs the middle ground between H1 and H2 — tradecraft
            consistent but not affirmable). However, per Hard Rule 2
            this hypothesis is NOT advanced by any cited source;
            included as matrix construct, NOT promoted as Archimedes
            corpus stance. Rank-1-by-matrix-arithmetic does NOT create
            attribution.
          wep: not_applicable_per_hard_rule_2
          hard_rule_2_status: HALT — Archimedes will NOT promote H4 as a corpus attribution stance because no cited source advances it
        - rank: 2
          hypothesis_id: H2
          rationale: >
            One weighted inconsistency (E7, weight 1, lower-grade
            chain). Best matches Unit 42 verbatim hedge framing and
            MSTIC silence interpretation. Cited by at least one Tier-1
            source (Unit 42 explicit replication-by-competent-actor
            language). Per Hard Rule 2: H2 is consistent with cited
            source framings; Archimedes preserves but does NOT
            originate this as a positive attribution.
          wep: roughly_even_chance
          hard_rule_2_status: PRESERVED — H2 is the framing Unit 42 advances; Archimedes restates Unit 42's hedge as the corpus stance, NOT a novel claim
        - rank: 3
          hypothesis_id: H5
          rationale: >
            One weighted inconsistency (E7, weight 1). Strongest
            specific framing of Unit 42's hedge — "any competent actor
            can replicate." H5 is a more specific instantiation of H2.
            Treat H2 and H5 as a hypothesis-pair.
          wep: roughly_even_chance
          hard_rule_2_status: PRESERVED — same as H2; H5 is Unit 42's verbatim language operationalized
        - rank: 4
          hypothesis_id: H3
          rationale: >
            Three weighted inconsistencies via E8 — VT-006 base
            attribution is too well-established to overturn. Included
            as null hypothesis; functionally rejected.
          wep: very_unlikely
          hard_rule_2_status: REJECT — base-campaign TeamPCP attribution is too well-corroborated to advance the null
        - rank: 5
          hypothesis_id: H1
          rationale: >
            Twelve weighted inconsistencies via E1/E2/E3/E5. The
            "TeamPCP-on-Miasma straightforward affirmative" hypothesis
            is the WEAKEST under matrix analysis. Both Tier-1 A-grade
            vendors plus the directly-retrieved Socket primary
            (B-grade) all align against this hypothesis. The lower-
            grade SecurityWeek-aggregation chain (E7, weight 1) is the
            only evidence supporting H1 and Socket's direct primary
            contradicts SecurityWeek's framing of Socket as
            affirmative.
          wep: unlikely
          hard_rule_2_status: PRESERVED — Archimedes does NOT advance H1 affirmatively; corpus stance remains "Miasma extension UNATTRIBUTED"

      sensitivity_analysis:
        brittleness: medium
        load_bearing_evidence: [E1, E2]
        if_E1_reinterpreted_as_incomplete_assessment: >
          KAC A1 stress-tests this directly. If MSTIC silence is
          incomplete-assessment rather than affirmative-declination,
          H1's inconsistency count drops by 3 (E1 weight). H1 still
          carries 9 weighted inconsistencies via E2/E3/E5; ranking
          unchanged. ROBUST to E1 reinterpretation.
        if_E2_unit42_walked_back: >
          If Unit 42 published a follow-up affirmatively attributing
          to TeamPCP, H1's weighted inconsistency drops further. H1
          would then carry 6 weighted inconsistencies (E3 + E5); still
          ranks below H2/H4/H5. ROBUST to Unit 42 walk-back IF the
          MSTIC declination interpretation holds.
        if_E5_novel_capabilities_reinterpreted_as_teampcp_evolution: >
          If MSTIC's novel capability documentation is treated as
          TeamPCP toolchain evolution rather than separate-operator
          fork, E5 flips C/I assignment. H1's inconsistency drops by
          3. H1 carries 9 weighted inconsistencies — still ranks last.
          ROBUST.
        if_socket_primary_e3_misread: >
          If Socket primary is re-read as attributing to TeamPCP (i.e.,
          SecurityWeek aggregation is correct that Socket is in the
          affirmative chain), E3 flips. H1 carries 9 weighted
          inconsistencies via E1 + E2 + E5 — still ranks last. ROBUST
          to Socket reinterpretation.
        single_point_of_failure: >
          No single piece of evidence's removal flips the ranking. The
          Tier-1 declination chain framing rests on TWO independent
          pieces of evidence (E1 MSTIC silence + E2 Unit 42 explicit
          hedge), not one. Even if E1 is fully discounted per KAC A1,
          E2 alone holds the framing.
        overall_assessment: >
          Matrix is robust under sensitivity testing on the
          ATTRIBUTION-DIVERGENCE framing — H1 stays last under any
          single-source reinterpretation. Procedural-facts layer is
          NOT under sensitivity stress (six-vendor consolidation is
          structurally independent of the attribution layer).

      tripwires:
        - observation: >
            MSTIC or Unit 42 publishes a follow-up affirmatively
            attributing Miasma extension to TeamPCP.
          effect: >
            Rerun ACH with E1/E2 flipped C↔I; ranking would shift but
            H1 would still need to overcome E5 (novel capabilities) +
            corrected-Socket primary stance.
        - observation: >
            A second Tier-1 vendor independently documents the
            destructive tripwire on a NON-Miasma Shai-Hulud family
            campaign.
          effect: >
            Lifts E5 from MSTIC-sole-originator to layered; family-
            level capability lift to VT-006 dossier warranted; matrix
            unchanged but vuln-tracker action.
        - observation: >
            Lower-grade chain (Aikido / Ox / ReversingLabs primaries)
            is directly retrieved and the Tier-1 declination chain
            framing is found to contradict directly-retrieved primary
            text (e.g., Aikido does NOT in fact affirm TeamPCP-on-
            Miasma in its primary).
          effect: >
            E7 weight collapses; H1 loses its only support; H2/H5
            framing further consolidated.
        - observation: >
            TeamPCP-controlled infrastructure (per actor dossier) is
            observed in connection with Miasma extension campaign.
          effect: >
            E1/E2 framing weakens; H1 inconsistency drops materially;
            rerun ACH.
        - observation: >
            Public release of Mini Shai-Hulud source code is
            disputed / found to be limited / found to be controlled
            release (E9 weakens).
          effect: >
            H2/H4/H5 lose their underlying premise; H1 by default
            becomes more probable; rerun ACH.

      conclusion:
        summary: >
          The matrix supports the grader's framing that the Miasma
          extension is UNATTRIBUTED in Archimedes corpus, with the
          Tier-1 declination chain (MSTIC silence + Unit 42 explicit
          hedge) as the dominant corpus stance. The "Miasma is
          TeamPCP" hypothesis (H1) is the WEAKEST under weighted
          matrix analysis (12 weighted inconsistencies) — the lower-
          grade SecurityWeek-aggregation chain is its only support and
          is contradicted by Socket's directly-retrieved primary.
          The "competent-actor replication post-public-source-release"
          framing (H2/H5, advanced by Unit 42 verbatim) carries fewest
          inconsistencies among hypotheses that any cited source
          advances. Per Hard Rule 2: Archimedes does NOT originate
          attribution to a TeamPCP-adjacent cluster (H4) despite its
          rank-1 matrix position; H4 is a matrix construct not
          advanced by any cited source. Per Hard Rule 2: Archimedes
          does NOT promote H2/H5 to positive attribution; preserves
          Unit 42's hedge framing as restated cited stance, NOT a
          novel claim.
        wep: unlikely_on_h1_teampcp_miasma_attribution     # i.e., affirming TeamPCP on Miasma is UNLIKELY
        wep_on_corpus_stance_miasma_unattributed: very_likely  # i.e., the procedural stance "Miasma is currently unattributed in corpus" is very likely correct
        confidence_caveats: >
          (a) The Tier-1 declination framing rests on the interpretation
          of MSTIC silence as affirmative declination (KAC A1); under
          alternative reading, the framing weakens but does not flip.
          (b) The lower-grade chain has not been directly retrieved at
          the primary level (Aikido / Ox / ReversingLabs); SecurityWeek
          aggregation may be misframing Socket as affirmative when
          Socket's primary declines. Direct retrieval of those primaries
          is a tripwire. (c) Archimedes does NOT extend H4's matrix
          rank-1 position into positive attribution per Hard Rule 2.

  sat_kac:
    kac_analysis:
      assessment_under_review: >
        "MSTIC's silence on TeamPCP attribution is the SECOND Tier-1
        A-grade affirmative declination of TeamPCP attribution on the
        Red Hat / Miasma extension, bracketing the lower-grade
        affirmative chain (Aikido C + Ox B + ReversingLabs C + Socket B
        via SecurityWeek aggregation)." Plus: (b) MSTIC's upstream
        RedHatInsights/javascript-clients CI/CD pipeline compromise
        vector is the correct initial-vector framing for the Miasma
        campaign; (c) api.anthropic[.]com endpoint is currently
        DORMANT per MSTIC observation; (d) MSTIC's documentation of a
        destructive tripwire constitutes a NEW capability class for
        the Shai-Hulud family and should propagate to family-level
        risk classification.
      analyzed_at: 2026-06-03T08:48:00-04:00
      analyzed_by: analyst
      analyst_run_id: analyst-20260603-084800
      invoking_context: >
        Pre-publication review for morning brief lead candidate.
        Grader flagged four specific KAC sub-questions (A1 attribution
        interpretation, A2 initial vector, A3 endpoint state, A4
        destructive capability axis). KAC applied to all four plus
        derivative.

      assumptions:
        - id: A1
          statement: >
            MSTIC's silence on TeamPCP attribution constitutes
            AFFIRMATIVE DECLINATION (i.e., MSTIC has analyzed the
            attribution question and decided not to extend TeamPCP),
            equivalent in corpus weight to Unit 42's explicit verbatim
            hedge.
          category: source_reliability + semantic
          stated: true
          why_must_be_true: >
            The "TWO Tier-1 declinations bracket ZERO affirmations"
            framing depends on MSTIC's silence being interpretable as
            affirmative declination. If MSTIC simply hasn't completed
            attribution analysis yet (analytic-conservatism / scope-
            decision / pre-publication-holdback), the framing
            overweights MSTIC silence.
          when_could_be_false: >
            (a) MSTIC's publication scope is intentionally limited to
            defender-facing detection content and excludes attribution
            by editorial policy; (b) MSTIC's attribution work on
            Miasma is in progress and silence reflects timing rather
            than declination; (c) MSTIC chose to use the family-
            taxonomic signature name (`Trojan:JS/ShaiWorm.DAW!MTB`) as
            its implicit family-level attribution stance, with named-
            actor attribution deferred to MS Threat Intelligence
            customer reports not visible in public blog.
          evidence_for:
            - Unit 42 verbatim hedge in finding-2026-06-02-0008 sets a
              precedent that Tier-1 vendors are actively declining
              attribution on this specific campaign — making MSTIC's
              silence in the same context more interpretable as
              alignment with that declination.
            - MSTIC named-research-team byline (Microsoft Defender
              Security Research Team) is consistent with a vendor that
              would publish attribution if it had it; the absence in a
              full technical write-up class publication is more
              informative than absence in a brief alert.
            - Defender signature naming ties at family-taxonomic level
              only; if MSTIC had operator attribution, they could have
              extended via prose without breaking signature-naming
              discipline.
          evidence_against:
            - MSTIC publications often defer named-actor attribution to
              MS Threat Intelligence customer feeds not visible in
              public blog content; public blogs sometimes lag
              attribution by weeks-to-months. (No specific source
              cited; this is general analyst priors on MSTIC editorial
              policy — flag as ASSUMPTION-ABOUT-ASSUMPTION, low
              confidence.)
            - MSTIC's family-taxonomic signature naming COULD be read
              as implicit attribution at family-level (i.e., "this is
              a Shai-Hulud family malware" implicitly invokes the
              family operator). KAC: this reading would CONFLICT with
              Hard Rule 2 discipline distinguishing family signature
              from actor attribution.
          confidence: medium
          centrality: critical
          classification: qualify
          remediation_action: >
            QUALIFY the framing in finding prose: replace "SECOND
            Tier-1 A-grade declination" with "SECOND Tier-1 A-grade
            silence-with-family-signature-tag, interpretable as
            declination in the context of Unit 42's adjacent explicit
            hedge." Preserve Unit 42's explicit hedge as the
            primary-strength-evidence of the declination chain;
            MSTIC's silence as secondary-strength-evidence.

        - id: A2
          statement: >
            MSTIC's upstream RedHatInsights/javascript-clients CI/CD
            pipeline compromise framing is the CORRECT initial-vector
            framing — i.e., the actual intrusion path was upstream
            pipeline compromise, not maintainer-account-takeover via
            OIDC token theft as Aikido reports.
          category: technology + source_reliability
          stated: true
          why_must_be_true: >
            Defensive recommendation prioritizes CI/CD pipeline audit
            vs. maintainer-account-credential rotation. These have
            different remediation cost profiles for A&D primes.
          when_could_be_false: >
            (a) BOTH vectors are operative — MSTIC and Aikido are
            observing different phases of the same intrusion chain
            (upstream pipeline compromise → harvested OIDC tokens →
            republish via legitimate maintainer-OIDC path); (b) MSTIC's
            first-party Defender telemetry reflects an OBSERVATION
            BIAS — Defender sees what Defender instruments, which is
            primarily endpoint/CI-runner activity; Aikido's OIDC
            exploitation analysis is from a different observation
            point (token-replay forensics) and might be capturing a
            different mechanism in the same chain; (c) Aikido's framing
            could be wrong (provisional C source-grade) — the lower-
            grade chain may have misidentified mechanism.
          evidence_for:
            - MSTIC first-party Defender telemetry (A1) — strongest
              available source-class on upstream-pipeline framing.
            - MSTIC structures the attack chain explicitly with the
              pipeline-compromise as initial-vector phase.
          evidence_against:
            - Aikido (provisional C) explicitly describes maintainer-
              account-compromise via OIDC vector in finding-2026-06-02-
              0003. Source-grade C is lower but the mechanism description
              is specific (GitHub Actions OIDC exploitation).
            - Both vectors are technically compatible — a CI/CD
              pipeline compromise CAN harvest OIDC tokens that then
              enable subsequent republish; the two framings may
              describe sequential phases rather than competing vectors.
          confidence: medium
          centrality: material
          classification: qualify
          remediation_action: >
            QUALIFY in brief: defender-action framing must cover BOTH
            CI/CD pipeline audit (MSTIC) AND maintainer-account /
            OIDC-token rotation (Aikido). Treat as a composite vector
            until either MSTIC affirmatively excludes the OIDC path
            or Aikido is directly retrieved and reframed. Both
            remediation paths are independently valuable for A&D
            defenders.

        - id: A3
          statement: >
            api.anthropic[.]com :443/v1/api endpoint state at MSTIC
            observation phase is DORMANT (noop:true), and Socket's
            earlier observation of the endpoint as active C2 reflects
            a state-transition between observation windows. Defender
            single-line recommendation: monitor-for-traffic, do NOT
            generic-blocklist.
          category: visibility + technology + actor_operational_status
          stated: true
          why_must_be_true: >
            Briefer needs a defensible single line on whether this
            endpoint is currently a live IOC. Affects defensive posture
            (active block vs. monitor-only).
          when_could_be_false: >
            (a) Socket and MSTIC observed DIFFERENT campaign
            sub-variants — the endpoint configuration (active vs.
            dormant) is per-variant rather than per-time; (b)
            DEFENDER takedown / Anthropic-side mitigation between
            Socket's observation (~2026-05-29 to 2026-06-01) and
            MSTIC's observation (between 06-01 and 06-02 publication)
            invalidated active C2 (this is a benign-cause
            explanation); (c) operator-controlled kill-switch flipped
            noop:true to hold the channel in reserve; (d) one of the
            two observations is methodologically wrong (Socket
            misidentified dormant traffic as active C2, or MSTIC
            misread an active endpoint as dormant); (e) the endpoints
            are LITERALLY DIFFERENT routes on the same host — Socket
            observed traffic on a specific /v1/api endpoint variant
            and MSTIC observed a different endpoint variant labeled
            noop:true in the payload config.
          evidence_for:
            - MSTIC explicitly documents the `noop:true` configuration
              flag — this is specific config-level detail, not
              general observation.
            - The temporal sequence (Socket earlier; MSTIC later)
              makes state-transition the most parsimonious explanation
              for the active→dormant difference if both observations
              are individually correct.
          evidence_against:
            - No vendor has affirmatively documented a kill-switch
              mechanism in the Miasma payload; (a) and (c) framings
              are speculative.
            - Socket did not document active vs. dormant explicitly;
              "Socket observed active" is an analyst-side interpretation
              of Socket's C2-exfil-channel framing. The Socket primary
              describes api.anthropic[.]com as the exfiltration
              endpoint without state-flag language. This means the
              "Socket active vs. MSTIC dormant" framing in the
              grader's red-team prompt is ITSELF an inference, not a
              directly-supported observation pair.
          confidence: low
          centrality: material
          classification: qualify
          remediation_action: >
            QUALIFY in brief: "api.anthropic[.]com :443/v1/api is
            documented by MSTIC as configured noop:true (held in
            reserve) at MSTIC observation; defender action is
            MONITOR-FOR-TRAFFIC from CI runner contexts (NOT generic-
            blocklist; legitimate Anthropic API infrastructure).
            Endpoint should be treated as latent-live, not confirmed-
            dead." Do NOT advance the state-transition narrative
            without further corroboration — the Socket-active-vs-MSTIC-
            dormant framing rests on inference about Socket's prior
            observation that Socket itself did not state-flag. Red-
            team should adjudicate before publication.

        - id: A4
          statement: >
            MSTIC's documentation of a destructive tripwire (`rm -rf
            ~/` on decoy honeytoken invalidation) constitutes a NEW
            capability class for the Shai-Hulud family and should
            propagate to family-level risk classification on the VT-006
            dossier.
          category: capability + TTP_patterns
          stated: true
          why_must_be_true: >
            VT-006 family risk classification drives vuln-tracker
            handoff (single-dossier-update vs. separate-dossier-scaffold
            decisions) and downstream defender priority weighting.
          when_could_be_false: >
            (a) Destructive tripwire is Miasma-EXTENSION-specific
            tradecraft, not present in VT-006 base or other Shai-Hulud
            family extensions — propagating to family-level
            overgeneralizes from one observation; (b) the tripwire is
            a defensive-targeting mechanism (anti-analyst booby trap),
            not a general destructive capability — it fires only on
            decoy-token interaction, not as an operational-objective
            destruction; (c) MSTIC is the SOLE source for this
            observation; single-source veto already caps it at
            "likely" — family-level lift requires layered corroboration
            on the destructive-capability axis.
          evidence_for:
            - MSTIC first-party Defender telemetry (A1) on the specific
              tripwire mechanism.
            - The honeytoken-substring artifact cross-corroborates with
              Socket's prior "ifyouinvalidatethistoken" observation in
              finding-2026-06-01-0004 — the TRIGGER is corroborated
              even if the TRIGGER-EFFECT is MSTIC-sole-originator.
          evidence_against:
            - VT-006 base campaign per prior corpus state did NOT
              document destructive capability — Wiz + Snyk + StepSecurity
              + Semgrep + Onapsis + Aikido + SafeDep + MSTIC primary
              on VT-006 base did not surface destructive tradecraft.
              Family-level lift from one extension observation is
              speculative absent base-campaign-or-other-extension
              corroboration.
            - The tripwire is conditional (triggers only on decoy
              honeytoken invalidation) — operationally, it is a
              tradecraft-protection mechanism, not a general operational-
              destructive capability. Risk classification axis lift
              should distinguish between "destructive tradecraft
              protection" and "destructive operational objective."
          confidence: low
          centrality: material
          classification: qualify
          remediation_action: >
            QUALIFY in brief and in vuln-tracker handoff: the
            destructive tripwire is MIASMA-EXTENSION-SPECIFIC at
            current evidence (MSTIC sole originator). Do NOT propagate
            to family-level risk classification on VT-006 dossier
            without corroboration on at least one other Shai-Hulud
            family campaign. Vuln-tracker should record the destructive
            capability as an EXTENSION-LEVEL axis on the Miasma sub-
            dossier (or VT-011 placeholder), NOT a family-level axis
            lift. Tripwire framing should be "destructive tradecraft
            protection" not "destructive operational objective" until
            evidence of unconditional destructive operation emerges.

        - id: A5
          statement: >
            The six independent vendors (MSTIC + Unit 42 + Socket + Ox
            + Aikido + ReversingLabs) are GENUINELY INDEPENDENT on the
            procedural-facts layer — i.e., the procedural-facts WEP
            lift to "very_likely" is structurally sound.
          category: source_reliability + visibility
          stated: false
          why_must_be_true: >
            Procedural-facts WEP at "very_likely" depends on independence
            of the six vendors. If they are all tracing the same
            public-record event surface (the @redhat-cloud-services
            npm namespace state), their analytical independence may
            be theatrical-with-shared-observation-substrate.
          when_could_be_false: >
            (a) All six vendors observe the same npm namespace state
            and the differences in evidence bases (runtime, monitor-
            post, downstream-repo enumeration, OIDC analysis, CI/CD
            forensics, Defender telemetry) are differences in ANALYSIS
            METHODOLOGY but not differences in OBSERVATION SUBSTRATE;
            (b) the procedural-facts independence test passes on
            methodological independence but the underlying observation
            substrate is shared, making the corroboration weaker than
            "very_likely" implies.
          evidence_for:
            - Different evidence bases per finding: MSTIC first-party
              Defender telemetry; Unit 42 monitor-post + variant-
              lineage; Socket runtime; Ox downstream-repo enumeration;
              Aikido OIDC analysis; ReversingLabs CI/CD + publication-
              window forensics. These are genuinely different
              methodological frames.
            - The procedural facts (namespace, package count, marker
              string, lineage) are independently verifiable artifacts,
              not interpretive claims.
          evidence_against:
            - The npm namespace state IS shared observable substrate.
              All six vendors look at @redhat-cloud-services; finding
              "32 packages compromised" reduces to counting the same
              packages.
            - This is the standard ratchet-effect concern in
              consolidation findings — does six-vendor consensus on
              the same public-record event surface count as six
              independent observations or one observation analyzed
              six ways?
          confidence: medium
          centrality: material
          classification: qualify
          remediation_action: >
            QUALIFY: procedural-facts WEP at "very_likely" is sound
            on independence-of-analysis-methodology but should be
            understood as resting partly on a shared observation
            substrate (the public npm namespace state). The "very
            likely" WEP is defensible because procedural facts are
            verifiable artifacts not interpretive claims; the lift is
            not on attribution or interpretation, but on facts-of-
            record. Red-team to argue this point per grader's red-team
            prompt (a).

        - id: A6
          statement: >
            The VT-006 BASE-campaign TeamPCP attribution at "likely"
            (Wiz + Snyk + StepSecurity affirmative chain) is
            UNAFFECTED by the Miasma extension declination. The base
            attribution stands.
          category: actor_continuity + semantic
          stated: true
          why_must_be_true: >
            Corpus stance distinction (base = TeamPCP at likely;
            extension = unattributed) depends on logical-scope
            separation. If the extension's Tier-1 declination
            propagates upward to challenge the base attribution, the
            VT-006 dossier corpus state changes materially.
          when_could_be_false: >
            (a) MSTIC's family-taxonomic signature naming implicitly
            challenges the base-campaign attribution — if the
            FAMILY is Shai-Hulud but the family operator is uncertain
            across extensions, the same uncertainty could
            retrospectively challenge the base; (b) Unit 42's
            "public source code release" framing is operator-claim-
            agnostic about the SOURCE-RELEASER — if the source release
            is itself unattributed at the operator level, the
            base-campaign attribution to TeamPCP-as-operator is
            challengeable; (c) actor-profiler may decide on review
            that scope-of-confidence narrowing on the TeamPCP dossier
            (per actor_profiler_handoff field) effectively challenges
            the base attribution.
          evidence_for:
            - VT-006 base attribution rests on a DIFFERENT vendor
              chain (Wiz + Snyk + StepSecurity affirmative) than the
              Miasma extension chain. The two attribution layers are
              source-base-disjoint.
            - Per Hard Rule 2 logical-scope discipline: declining
              attribution on extension X does NOT unsay affirmative
              attribution on base Y when the affirmative attribution
              has its own independent vendor base.
          evidence_against:
            - Family-level operator-uncertainty propagation is a real
              analyst concern — same family, increasingly uncertain
              operator across extensions, suggests the FAMILY-OPERATOR
              relationship is what's uncertain, not just the EXTENSION-
              OPERATOR.
          confidence: medium
          centrality: material
          classification: qualify
          remediation_action: >
            QUALIFY: preserve VT-006 base-campaign TeamPCP attribution
            at "likely" UNCHANGED. Flag for actor-profiler review per
            existing handoff field that the scope-of-confidence on
            TeamPCP attribution may need narrowing across the
            Shai-Hulud family extensions. Do NOT propagate Miasma
            extension declination upward to challenge the base
            attribution without affirmative evidence of base-campaign
            attribution challenge.

      classifications_summary:
        sound: 0
        qualify: 6
        test: 0
        reject: 0

      remediation:
        status: proceed_with_qualifying_caveats
        qualifying_caveats:
          - >
            A1 (MSTIC silence interpretation) — replace "SECOND
            Tier-1 A-grade affirmative declination" with "SECOND
            Tier-1 A-grade silence-with-family-signature-tag,
            interpretable as declination in context of Unit 42's
            adjacent explicit hedge." Unit 42 hedge is primary-
            strength; MSTIC silence is secondary-strength.
          - >
            A2 (initial vector) — defender-action framing must cover
            BOTH MSTIC upstream-pipeline AND Aikido maintainer-OIDC
            paths. Treat as composite or sequential vectors until
            either path is affirmatively excluded.
          - >
            A3 (api.anthropic state) — "configured noop:true at MSTIC
            observation; monitor-for-traffic from CI runners; do NOT
            generic-blocklist; treat as latent-live." Do NOT advance
            state-transition narrative — Socket-active-vs-MSTIC-dormant
            framing is itself an inference Socket did not state-flag.
          - >
            A4 (destructive capability axis) — record at Miasma-
            extension level (or VT-011 placeholder), NOT family-level
            VT-006 propagation. Tripwire is "destructive tradecraft
            protection" not "destructive operational objective" at
            current evidence.
          - >
            A5 (six-vendor independence) — procedural-facts "very
            likely" is defensible on independence-of-methodology;
            disclose shared observation substrate (npm namespace) as
            a caveat. Red-team to argue per existing prompt (a).
          - >
            A6 (base attribution unaffected) — preserve VT-006 base
            TeamPCP at "likely" unchanged; flag actor-profiler for
            scope-of-confidence narrowing review across family
            extensions; do NOT propagate Miasma declination upward.
        next_action: >
          Proceed with publication. All six assumptions are QUALIFY
          (none TEST, none REJECT). Brief should incorporate the
          qualifying caveats verbatim. Red-team gets the existing
          red-team prompts (a)-(d) plus A1 interpretation explicitly.

      recommended_wep_after_test:
        procedural_facts_layer: very_likely     # CONFIRMED; six-vendor consolidation passes sensitivity
        api_anthropic_endpoint_existence_claim: very_likely  # CONFIRMED via MSTIC+Socket cross-corroboration on endpoint
        attribution_layer_corpus_stance_miasma_unattributed: very_likely  # CONFIRMED with A1 qualifying caveat
        attribution_layer_teampcp_on_miasma_affirmation: unlikely  # CONFIRMED — H1 ranks last in ACH
        destructive_tripwire_extension_level: likely    # MSTIC sole-originator; single-source veto holds
        destructive_tripwire_family_level_propagation: not_advanced  # Per A4 qualify; do NOT propagate
        upstream_pipeline_vector_as_sole_initial_vector: likely_but_qualified  # Per A2; not exclusive of OIDC vector
        api_anthropic_state_transition_narrative: not_advanced  # Per A3; do NOT advance without Socket-side state-flag corroboration
        vt006_base_teampcp_attribution_unchanged: likely  # Per A6; UNAFFECTED by Miasma extension declination

# Lifecycle
tlp: CLEAR
published_in_briefs: [2026-06-03-morning, 2026-06-04-morning]
retracted: false
retraction_brief_id: null

# Defensive / IOC handoff flags
ioc_handoff:
  defender_relevant_iocs:
    - "api.anthropic[.]com :443/v1/api — dormant exfil endpoint at MSTIC observation phase; monitor for unusual /v1/api traffic from CI runner contexts; DO NOT generic-blocklist (legitimate Anthropic API infrastructure)"
    - "6 SHA-256 dropper payload hashes (see raw-signal IOC block)"
    - "github.com/oven-sh/bun/releases + release-assets.githubusercontent.com — Bun runtime download paths (legitimate infra; monitor for unexpected Bun installs in CI/dev contexts)"
    - "Spoofed Git commit author github-actions@github.com + commit message 'chore: update dependencies [skip ci]' — Channel B self-propagation signature"
    - "Decoy honeytoken name 'IfYouInvalidateThisTokenItWillNukeTheComputerOfTheOwner' — destructive-tripwire trigger artifact"
    - "Defender signatures: Trojan:JS/ShaiWorm.DAW!MTB, Trojan:JS/ObfusNpmJs"
    - "@redhat-cloud-services namespace — 32 affected packages across 90+ versions; package list in raw-signal"
    - "github.com/RedHatInsights/javascript-clients — upstream CI/CD pipeline compromised (initial vector per MSTIC)"
  iocs_indirect_action: >
    Defender action framing for A&D-prime CI/CD pipeline audit:
    (a) Audit @redhat-cloud-services package consumption across
        Node-based CI/CD runners on Linux (primary target per MSTIC);
    (b) Rotate npm tokens with write access on all CI/CD runners
        touching @redhat-cloud-services packages in last 30 days;
    (c) Rotate cloud-provider tokens (GitHub, AWS, Azure, GCP,
        HashiCorp Vault, Kubernetes Service Account) for any
        runner identified in (a);
    (d) Monitor cloud-metadata endpoints (169.254.169.254,
        169.254.170.2) for unusual access from build processes;
    (e) Monitor for unexpected Bun runtime installs (legitimate
        Bun infra abused as second-stage execution environment);
    (f) Watch for Channel B Git Data API code injection via
        spoofed github-actions@github.com author + 'chore: update
        dependencies [skip ci]' pattern in commit history;
    (g) Block destructive-tripwire by NOT triggering decoy token
        invalidation if the honeytoken substring matches the MSTIC-
        published name pattern.

vuln_tracker_handoff:
  vt006_dossier_update_candidate: true
  vt006_update_substance: >
    VT-006 dossier should incorporate Miasma extension state:
    (a) MSTIC FIRST A-grade originating primary; (b) destructive
    tripwire NEW capability class for family; (c) Sigstore-Fulcio-
    Rekor provenance forgery mechanism; (d) upstream-pipeline-
    compromise vector (vs maintainer-account-compromise vector);
    (e) dormant Anthropic C2 endpoint dormancy-state; (f) 16-
    account GitHub rotation pool; (g) TeamPCP-on-Miasma-extension
    attribution DECLINED by two Tier-1 A-grade vendors (Unit 42
    + MSTIC) — preserve VT-006 base-campaign TeamPCP-at-likely
    attribution UNAFFECTED.
  separate_vt_dossier_candidate: true
  separate_vt_substance: >
    Vuln-tracker may alternatively scaffold a separate VT-011
    Miasma dossier given (a) destructive tripwire as new capability
    class for the Shai-Hulud family, (b) Tier-1 attribution-
    divergence from VT-006 base campaign, (c) campaign-distinct
    features (Bun runtime, Sigstore-specific forgery, dormant
    Anthropic C2). Vuln-tracker decides. Grader recommendation:
    UPDATE VT-006 dossier with Miasma extension state AND scaffold
    VT-011 placeholder for tracking; both are coherent.

actor_profiler_handoff:
  teampcp_dossier_recheck_candidate: true
  teampcp_recheck_substance: >
    Actor-profiler TeamPCP dossier recheck warranted given TWO
    Tier-1 A-grade vendors (Unit 42 + MSTIC) now explicitly
    decline TeamPCP-on-Miasma extension AND Unit 42 + MSTIC
    framing both reference "public source code release lowering
    replication barrier" implying current Miasma operator may NOT
    be the original Shai-Hulud / TeamPCP author. Actor-profiler
    should consider whether:
    (a) TeamPCP scope-of-confidence should be NARROWED to VT-006
        / Mini Shai-Hulud / TanStack / CVE-2026-45321 base campaign
        (Wiz + Snyk + StepSecurity affirmative chain) and EXPLICITLY
        EXCLUDE the Miasma extension;
    (b) A separate "Miasma-operator-unattributed" placeholder
        should be added to the actor roster as a tracking entity;
    (c) The Shai-Hulud family-taxonomic anchor should be promoted
        to a separate tracking entity (vs. actor TeamPCP) reflecting
        that the malware FAMILY is the durable corpus anchor and
        the OPERATOR(s) are increasingly uncertain across family
        extensions.

briefer_handoff:
  brief_lead_candidate_for_morning_brief: true
  brief_lead_substance: >
    MSTIC publishes A-grade originating primary on Red Hat / Miasma
    campaign with substantive capability lift AND second Tier-1
    declination of TeamPCP attribution. This is the highest-impact
    AM brief lead candidate today. Briefer should treat as primary
    lead with: (1) procedural-facts WEP lift to "very_likely" via
    six-vendor consolidation; (2) novel-capability layer summary
    (destructive tripwire as new family capability class; Sigstore
    forgery via Fulcio/Rekor; upstream pipeline compromise vector;
    dormant Anthropic C2); (3) attribution-divergence framing
    (TWO Tier-1 declinations vs. ZERO Tier-1 affirmations;
    bracketed lower-grade affirmation chain); (4) defender-action
    framing centered on CI/CD runner audit + npm token rotation
    + cloud-metadata-endpoint monitoring + Bun-install monitoring;
    (5) preserve distinction between VT-006 BASE-campaign TeamPCP
    attribution (UNAFFECTED at "likely") and Miasma EXTENSION
    attribution (now UNATTRIBUTED with Tier-1 declination chain).
  smart_brevity_quote_discipline: >
    Briefer MUST keep MSTIC quotes <15 words per Hard Rule 6.
    No more than one quote per source. Default to paraphrase
    throughout.

source_grade_revision_proposed: null
---

# MSTIC Publishes A-grade Originating Primary on Red Hat npm "Miasma" Campaign with Second Tier-1 TeamPCP Attribution Declination and Destructive-Tripwire Capability Lift

## Summary

Microsoft MSTIC (Microsoft Defender Security Research Team named byline) published a full technical write-up of the Red Hat npm "Miasma" credential-stealing supply-chain campaign on 2026-06-02 (16:45 PDT) / 2026-06-03 (00:45 EDT, in-window). This is the FIRST A-grade originating primary on the Red Hat / Miasma campaign in Archimedes corpus with first-party Defender + Microsoft Threat Intelligence telemetry. The campaign affects 32 npm packages across 90+ versions in the @redhat-cloud-services namespace, originating from an upstream RedHatInsights/javascript-clients CI/CD pipeline compromise.

MSTIC's write-up surfaces substantive NOVEL capability layers vs. prior corpus state: (a) a DESTRUCTIVE TRIPWIRE that executes `rm -rf ~/` if a planted decoy honeytoken is invalidated — a NEW capability class for the Shai-Hulud family; (b) Sigstore provenance forgery via Fulcio + Rekor with OIDC token exchange for npm publish rights; (c) 16 attacker-controlled GitHub accounts rotating per session; (d) Bun JavaScript runtime as second-stage execution environment; (e) dormant Anthropic API C2 endpoint `api.anthropic[.]com :443/v1/api` marked `noop: true` (held in reserve); and (f) upstream RedHatInsights/javascript-clients CI/CD pipeline compromise as initial vector (distinct from earlier maintainer-account-compromise framing).

CRITICAL ATTRIBUTION SIGNAL: MSTIC's body text contains ZERO mentions of TeamPCP, Mini Shai-Hulud campaign-attribution, TanStack / CVE-2026-45321 campaign-attribution, or any nation-state / eCrime named-actor. This makes MSTIC the SECOND Tier-1 A-grade vendor (after Unit 42 in finding-2026-06-02-0008) to explicitly DECLINE TeamPCP attribution on the Red Hat / Miasma extension. TWO Tier-1 A-grade declinations now bracket ZERO Tier-1 A-grade affirmations. The lower-grade affirmation chain (Aikido C + Ox Security B + ReversingLabs C + Socket B via SecurityWeek aggregation per AM finding-2026-06-02-0003) is bracketed but not affirmatively refuted.

Per Hard Rule 2, the VT-006 BASE campaign TeamPCP attribution (Mini Shai-Hulud TanStack / CVE-2026-45321; Wiz + Snyk + StepSecurity affirmative chain at "likely" WEP) REMAINS in force — MSTIC's silence on Miasma extension does NOT unsay Wiz/Snyk/StepSecurity's affirmative attribution on the BASE campaign. The grader-recommended corpus stance: VT-006 BASE = TeamPCP at "likely"; Miasma EXTENSION = UNATTRIBUTED with two Tier-1 declinations.

The Defender signature `Trojan:JS/ShaiWorm.DAW!MTB` ties the Miasma malware FAMILY-TAXONOMICALLY to the broader Shai-Hulud family; signature taxonomy is NOT actor attribution per Hard Rule 2.

## Sources

### Microsoft MSTIC / Microsoft Security Blog (mstic, digraph: A1 layered)

- URL: https://www.microsoft.com/en-us/security/blog/2026/06/02/preinstall-persistence-inside-red-hat-npm-miasma-credential-stealing-campaign/
- Published: 2026-06-02 16:45 PDT / 2026-06-03 00:45 EDT
- Byline: Microsoft Defender Security Research Team (named research team byline)
- Source grade: A (ratified per source-grades.yaml — Tier-1 vendor research, nation-state tracking, Defender telemetry-backed)
- Key claim: Full technical write-up of Red Hat npm Miasma campaign with first-party Defender + Microsoft Threat Intelligence telemetry; explicitly declines TeamPCP attribution; introduces destructive tripwire as new capability class; documents Sigstore-Fulcio-Rekor provenance forgery + 16-account rotation + upstream CI/CD pipeline compromise + Bun runtime + dormant Anthropic C2 dormancy-state.

### Cross-Corpus Corroborating Sources (from prior findings)

- **Palo Alto Unit 42 (unit42, A)** — finding-2026-06-02-0008. Tier-1 monitor-post update with explicit TeamPCP attribution hedge. Independent evidence basis: long-running npm threat landscape monitoring + variant-lineage analysis.
- **Socket Research Team (socket-research-team, provisional B)** — finding-2026-06-01-0004. Originating runtime + IOC analysis with api.anthropic[.]com C2 observation, "ifyouinvalidatethistoken" payload string observation (now cross-corroborated by MSTIC at substring level). Different evidence basis: runtime / binary analysis.
- **Ox Security (ox-security, provisional B)** — finding-2026-06-02-0003. 210 downstream-infected-repo enumeration. Different evidence basis: downstream-repo enumeration.
- **Aikido Security (aikido-security, provisional C)** — finding-2026-06-02-0003. GitHub Actions OIDC exploitation assessment. Different evidence basis: OIDC vector analysis.
- **ReversingLabs (reversinglabs, provisional C)** — finding-2026-06-02-0003. 72-second publication window forensics. Different evidence basis: CI/CD compromise + publication-window forensics.

Independence test PASSES on procedural facts (six vendors, different publishing organizations, none cite another as origin, different evidence bases). Independence test PASSES at endpoint level on api.anthropic[.]com (MSTIC + Socket cross-corroborate at different evidence bases). Independence test FAILS on MSTIC-sole-originator novel capability layers — single-source veto applied at layer level.

## Technical detail

**Attack chain (10 phases per MSTIC):** Delivery and execution via npm preinstall hook → 4.29 MB obfuscated dropper → ROT-based + AES-128-GCM decryption → environment gating (terminates on few-region locales; optional CI/CD-only restriction) → defense evasion → credential access (GitHub + npm + AWS + Azure + GCP + HashiCorp Vault + Kubernetes + CircleCI + SSH + browser/wallet + Anthropic API keys; includes scraping CI runner process memory) → privilege escalation via passwordless sudo rule → persistence via token monitoring + secondary-stage staging → exfiltration via three C2 channels + GitHub-infra abuse → self-propagation (Channel A: victim-owned-repo drop with "Miasma" marker; Channel B: Git Data API code injection with spoofed `github-actions@github.com` author + `chore: update dependencies [skip ci]` message; Channel C: OIDC token exchange for npm publish rights with FORGED SLSA provenance via Sigstore Fulcio/Rekor) → destructive tripwire (`rm -rf ~/` on decoy honeytoken invalidation).

**Defender coverage:** Microsoft Defender Antivirus signatures `Trojan:JS/ShaiWorm.DAW!MTB` and `Trojan:JS/ObfusNpmJs`. Microsoft Defender for Endpoint alerts include "Suspicious Node.js process behavior", "Suspicious installation of Bun runtime", "Suspicious Bun execution from Node.js process", "Credential access attempt", "Kubernetes secrets enumeration indicative of credential access". MSTIC publishes Advanced Hunting KQL queries for defender hunt activity — defender content is at the source URL (per Hard Rule 3 referencing only).

**MITRE ATT&CK (per MSTIC detection-table coverage):** T1195.003 (Compromised Dependencies), T1059 (Command and Scripting Interpreter), T1202 (Indirect Command Execution), T1140 (Deobfuscate/Decode Files), T1036.005 (Match Legitimate Name), T1110.003 (Credential Stuffing), T1552.001 (Credentials in Files), T1552.007 (Container Environment Credentials), T1187 (Forced Authentication), T1548.003 (Sudo and Sudo Caching), T1098 (Account Manipulation), T1547.014 (Pre-Install Hooks), T1041 (Exfiltration Over C2), T1567.002 (Exfiltration Over Web Service), T1570 (Lateral Tool Transfer), T1565.001 (Data Destruction).

**Remediation status (npm side):** affected repositories removed; @redhat-cloud-services namespace hardened with additional publishing protections; GitHub invalidated all npm tokens with write access and 2FA bypass.

## IOCs surfaced

(From collector's ioc-extraction in raw-signal; aggregated and consolidated.)

- **6 SHA-256 file hashes** of Miasma dropper / payload variants (per MSTIC IOC table)
- **`api.anthropic[.]com :443/v1/api`** — dormant exfil endpoint marked `noop: true` at MSTIC observation phase; legitimate-infra abuse caveat applies (do NOT generic-blocklist Anthropic API; monitor for unusual `/v1/api` traffic from CI runner contexts)
- **`github.com/oven-sh/bun/releases`** + **`release-assets.githubusercontent.com`** — Bun runtime download paths (legitimate infra; monitor for unexpected Bun installs in CI/dev contexts)
- **Campaign marker string:** `"Miasma: The Spreading Blight"` (used in attacker-created GitHub repo descriptions, code comments, decoy-token-name substring)
- **Spoofed Git commit author:** `github-actions@github.com`
- **Spoofed Git commit message pattern:** `chore: update dependencies [skip ci]`
- **Decoy honeytoken name:** `IfYouInvalidateThisTokenItWillNukeTheComputerOfTheOwner` (cross-corroborates Socket's prior "ifyouinvalidatethistoken" substring observation from finding-2026-06-01-0004)
- **Defender signatures:** `Trojan:JS/ShaiWorm.DAW!MTB`, `Trojan:JS/ObfusNpmJs`
- **Compromised npm namespace:** `@redhat-cloud-services` (32 packages across 90+ versions; full package list in raw-signal)
- **Compromised upstream repo:** `github.com/RedHatInsights/javascript-clients` (CI/CD pipeline initial vector per MSTIC)

Full IOC structure and per-IOC notes preserved in raw-signal `raw-2026-06-03-am-001-...`.

## Relationship to existing findings

- **finding-2026-06-02-0008** — Unit 42 monitor-post update with TeamPCP attribution hedge. RELATION: this finding is the SECOND Tier-1 A-grade declination of TeamPCP-on-Miasma; both together bracket the lower-grade affirmation chain. WEP procedural-facts lift event documented.
- **finding-2026-06-02-0003** — four-vendor (Ox + Aikido + ReversingLabs + Socket via SecurityWeek aggregation) initial multi-firm cluster. RELATION: this finding adds MSTIC as SIXTH vendor and SECOND Tier-1 A-grade; procedural-facts layer lifts from B1 to A1 layered.
- **finding-2026-06-01-0004** — Socket + THN originating coverage with api.anthropic[.]com C2 observation. RELATION: MSTIC INDEPENDENTLY CORROBORATES the api.anthropic[.]com endpoint (different evidence bases — MSTIC first-party Defender vs Socket runtime); endpoint-level claim lifts from B2 single-source to B1 cross-corroborated. MSTIC observes endpoint as DORMANT (noop:true) at MSTIC observation phase; Socket observed it as ACTIVE — red-team should adjudicate state-transition vs window-different vs interpretation-different vs different-endpoint hypotheses.
- **VT-006 base-campaign Mini Shai-Hulud TanStack / CVE-2026-45321** — UNAFFECTED by Miasma extension attribution declination. Wiz + Snyk + StepSecurity affirmative TeamPCP-on-VT-006-base attribution at "likely" WEP REMAINS in force.

## Open questions for analyst

1. **Attribution-divergence SAT-ACH candidate.** Competing hypotheses: (a) Miasma is TeamPCP (lower-grade chain); (b) Miasma is a separate-actor Shai-Hulud-family extension (Tier-1 declination chain implication); (c) Miasma is post-public-source-code-release competent-actor replication (Unit 42 explicit hedge framing); (d) Miasma is TeamPCP but the Tier-1 vendors have not completed attribution analysis (alternative reading of MSTIC silence). Analyst should structure ACH explicitly.
2. **SAT-KAC on "Tier-1 silence = affirmative declination" assumption.** MSTIC's silence with family-taxonomic signature tag is ambiguous. Unit 42's explicit hedge IS affirmative declination. Are these equivalent corpus stances?
3. **Initial-vector adjudication.** MSTIC: upstream RedHatInsights/javascript-clients CI/CD pipeline compromise. Aikido (per AM finding 0003): maintainer-account-compromise framing via OIDC vector. Are these the same vector described differently, or different vectors, or both present in different sub-clusters?
4. **VT-006 family destructive-capability axis.** Does ONE MSTIC observation of destructive tripwire on ONE family extension warrant family-level risk reclassification, or treat as Miasma-extension-specific until corroborated on other Shai-Hulud campaigns?
5. **api.anthropic[.]com state-transition.** Socket observed active; MSTIC observed dormant. Campaign state-transition vs. observation-window vs. interpretation-difference vs. different-endpoint hypotheses — red-team should adjudicate as a precondition for analyst attribution-divergence work.

## Analytic notes (from analyst review)

SAT-ACH and SAT-KAC applied. The attribution-divergence framing survives matrix pressure-testing: the "TeamPCP-on-Miasma affirmative" hypothesis (H1) carries 12 weighted inconsistencies via MSTIC silence + Unit 42 explicit hedge + Socket primary's directly-retrieved declination + MSTIC's documented novel capabilities — and ranks last among five hypotheses. The lower-grade SecurityWeek-aggregation chain (E7, weight 1) is H1's only support, and Socket's own primary contradicts SecurityWeek's framing of Socket as affirmative. Per Hard Rule 2 the matrix rank-1 hypothesis (H4 TeamPCP-adjacent cluster) is NOT advanced as corpus stance — no cited source advances it; matrix arithmetic does not create attribution. Unit 42's verbatim "competent-actor replication post-public-source-release" framing (H2/H5) is the strongest hypothesis any cited source affirmatively advances; Archimedes restates that framing, not as positive attribution but as Unit 42-restated corpus stance.

KAC surfaced six load-bearing assumptions, all QUALIFY (none TEST, none REJECT). Three deserve red-team scrutiny: (A1) MSTIC silence interpretation — replace "SECOND Tier-1 affirmative declination" with "SECOND Tier-1 silence-with-family-signature-tag, interpretable as declination in context of Unit 42's adjacent explicit hedge." Unit 42 hedge is primary-strength evidence; MSTIC silence is secondary-strength. (A3) api.anthropic[.]com state — the "Socket active vs. MSTIC dormant" framing is itself an inference; Socket did not state-flag the endpoint in finding-2026-06-01-0004. Brief should describe the endpoint as "configured noop:true at MSTIC observation, latent-live, monitor-for-traffic from CI runners, do NOT generic-blocklist" — and NOT advance the state-transition narrative as established. (A4) destructive tripwire — Miasma-extension-level capability only at current evidence; do NOT propagate to VT-006 family-level risk classification without corroboration on another Shai-Hulud campaign; frame as "destructive tradecraft protection" not "destructive operational objective."

Recommendation: SHIP at procedural-facts WEP "very_likely" with the KAC qualifying caveats woven into brief prose. The attribution-divergence framing is defensible but should be downgraded one notch in language strength — from "TWO Tier-1 affirmative declinations" to "TWO Tier-1 declination signals (Unit 42 explicit hedge primary-strength; MSTIC silence-with-family-signature-tag secondary-strength)." Defender-action framing should cover both initial-vector hypotheses (CI/CD pipeline + maintainer-OIDC) as composite rather than picking MSTIC's framing over Aikido's. All other procedural and IOC content ships as graded.

## Hard Rule Compliance

- **Hard Rule 2 (no novel attribution):** PRESERVED. Archimedes does NOT originate TeamPCP attribution on Miasma. Tier-1 declination chain preserved as dominant corpus stance on Miasma extension. VT-006 base-campaign TeamPCP attribution UNAFFECTED by Miasma extension declination.
- **Hard Rule 3 (no exploit code / PoC):** PRESERVED. MSTIC publishes Advanced Hunting KQL queries for defensive detection — defensive content cited via URL only; full KQL not extracted into corpus.
- **Hard Rule 6 (<15-word quotes, max 1 per source):** PRESERVED. No source quote in this finding exceeds 15 words; defender-signature names + decoy-token name + MSTIC named-team byline are all <15 words.
- **Hard Rule 8 (Splunk first-party precedence):** Splunk -30d sweep ran on superset; 0 events; first-party silence preserved as data point per the 20+-day non-archimedes-internal silent stream pattern, not disconfirming.
