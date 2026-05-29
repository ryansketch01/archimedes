---
finding_id: finding-2026-05-29-0001-mstic-vpmdhaj-npm-typosquat-shaiworm-cloud-cicd-credential-theft-bun-runtime-abuse-distinct-cluster-lineage-suggestion
created_at: 2026-05-29T08:08:00-04:00
graded_by: grader
grading_run_id: morning-20260529-080000
grading_mode: scheduled_brief
test: false

# Core grading (admiralty-grading skill output)
digraph: A2
digraph_layered:
  mstic_primary_research_publication_existence: A1                    # MSTIC byline, Microsoft Defender Security Research Team, vendor-authority on own product detection telemetry
  vpmdhaj_maintainer_alias_registered_npm_e_a39155771_at_gmail: A2    # Vendor self-statement of detection telemetry; not independently corroborated in window
  fourteen_typosquat_packages_published_within_4h_window_2026_05_28: A2  # MSTIC observation; not yet relayed by Snyk/Wiz/StepSecurity
  payload_capability_aws_imdsv2_ecs_vault_secrets_npm_publish_tokens: A2  # MSTIC technical claim; internally coherent with known credential-stealer TTPs
  gen1_http_c2_aab_sportsontheweb_net_x_php: A2                        # MSTIC IOC publication on own-product telemetry
  gen2_bun_runtime_abuse_downloads_from_oven_sh_bun_releases: A2       # MSTIC describes novel-but-plausible execution chain
  npm_lifecycle_hook_abuse_preinstall_install_postinstall: A1          # Established npm supply-chain TTP, internally coherent
  defender_signature_trojan_js_shaiworm_published: A1                   # MSTIC procedural fact on own-product signature publication
  defender_signature_trojan_js_obfusnpmjs_backdoor_js_supplychain: A1   # Same
  shaiworm_family_name_signals_internal_lineage_view: B3                # Internal-classification signal, NOT analytic statement; family-name in signature is suggestive but MSTIC declines to state TeamPCP attribution in article body; grader respects MSTIC silence per Hard Rule 2
  teampcp_attribution_for_vpmdhaj_claim: NOT_PROMOTED_HARD_RULE_2     # MSTIC does not name TeamPCP for this campaign — Archimedes does NOT extend the attribution; lineage suggestion is recorded as analyst question only
  vt006_mini_shai_hulud_same_actor_continuation_claim: NOT_PROMOTED_HARD_RULE_2  # Requires Wiz / Snyk / StepSecurity follow-up explicitly binding vpmdhaj to TeamPCP campaign tree
  packages_taken_down_npm_remediation: A2                              # MSTIC vendor statement; remediation status time-perishable
  proxy_defense_block_aab_sportsontheweb_net_alert_x_supply_header: A2  # MSTIC operator-actionable defensive guidance
  dib_structural_exposure_aws_vault_github_actions_npm_pipeline: A2    # Sector-shape framing — applies to any DIB org with cloud + CI/CD; no DIB prime named as victim
  cluster_anchor: A2

digraph_anchor: >
  Cluster digraph A2 anchored on Microsoft MSTIC / Microsoft Security
  Blog primary (Microsoft Defender Security Research Team, 2026-05-28
  23:04 EDT) — vendor-authority publication on own-product detection
  telemetry. MSTIC names the campaign actor-alias `vpmdhaj` (npm
  maintainer account, registry email a39155771@gmail.com), enumerates
  14 typosquat packages published in a 4-hour window targeting the
  OpenSearch / ElasticSearch / DevOps configuration ecosystem, and
  describes a two-generation stager architecture (Gen-1 HTTP C2
  beacon to aab.sportsontheweb.net; Gen-2 living-off-Bun-runtime
  loader) culminating in a Bun-compiled ~195KB stage-2 payload that
  harvests AWS instance/ECS task credentials, HashiCorp Vault tokens,
  GitHub Actions secrets, AWS Secrets Manager entries across 16+
  regions, and npm publish tokens. Three Defender detection
  signatures published: `Trojan:JS/ShaiWorm`, `Trojan:JS/ObfusNpmJs`,
  `Backdoor:JS/SupplyChain`.

  A2 (not A1) holds on the cluster anchor because:
    - MSTIC is single-source in window. Snyk, Wiz Research,
      StepSecurity, Semgrep, and Aikido — the cohort of vendors who
      attributed the May 12 Mini Shai-Hulud cluster (VT-006) to
      TeamPCP — have not yet published independent vpmdhaj coverage
      relating this campaign to that lineage. Single-source veto
      applies on operational claims that exceed "likely" WEP.
    - The procedural facts (campaign exists, IOCs valid, signature
      families live, packages were taken down) are at A1 individually
      but cluster-anchor at A2 pending independent corroboration of
      the campaign envelope.
    - The `ShaiWorm` Defender family-name in the signature is the
      strongest evidence of MSTIC's internal-classification view
      that vpmdhaj is in the Shai-Hulud / Mini Shai-Hulud (VT-006)
      lineage, BUT MSTIC's article prose makes NO actor attribution
      and does NOT reference Wiz/Snyk/StepSecurity prior reporting.
      Hard Rule 2 governs: do not originate or upgrade attribution
      past source statements. This finding records the lineage
      SUGGESTION as an analyst question, NOT as a TeamPCP-attributed
      campaign.

  Per Hard Rule 3 (no exploitation, ever), defender-facing detail
  is included in the technical-detail section, but NO PoC
  reproduction steps, payload construction, or exploitation
  guidance.

source_reliability:
  grade: A
  source_name: "Microsoft MSTIC / Microsoft Security Blog (Microsoft Defender Security Research Team)"
  source_yaml_id: mstic
  grade_rationale: >
    MSTIC pre-assigned A per source-grades.yaml. Microsoft Defender
    Security Research Team byline; vendor-authority publication on
    own-product detection telemetry; Microsoft Defender XDR detection
    signatures cited as live; remediation coordinated with npm team
    (packages taken down). Microsoft is the canonical primary source
    on its own product's detection signature family-naming
    (`Trojan:JS/ShaiWorm`) which carries the strongest internal-
    classification signal of lineage. Article is a vendor blog
    threat-intelligence primary, not a relay.
  provisional: false

credibility:
  grade: 2
  checklist_passed:
    - probably_true_no_contradicting_ab_grade_source_in_window
    - probably_true_technical_claims_internally_coherent_npm_lifecycle_hooks_imdsv2_bun_runtime_all_real_and_plausible_in_combination
    - probably_true_ttp_consistent_with_known_credential_stealer_supply_chain_class_npm_publish_token_theft_t1195_002
  rationale: >
    Probably True (2) on the campaign-envelope claim. MSTIC technical
    detail (npm lifecycle hooks, IMDSv2 169.254.169.254 + ECS
    169.254.170.2 metadata-endpoint targeting, HashiCorp Vault token
    harvesting, AWS Secrets Manager enumeration, Bun runtime
    distribution abuse, npm publish-token theft for downstream
    supply-chain pivot) is internally coherent and consistent with
    established npm-supply-chain credential-stealer TTPs (T1195.002,
    T1059.007, T1552.005, T1552.007, T1027, T1071.001, T1574).
    Cannot be promoted to "Confirmed" (1) without at least one
    independent source from the Wiz / Snyk / StepSecurity / Semgrep /
    Aikido cohort relaying or expanding on this campaign. The
    Defender `ShaiWorm` family-name signal is internal-classification
    evidence but does not constitute independent corroboration of
    the campaign existence — it IS MSTIC's own observation. No
    contradicting A/B-grade source.

corroboration:
  independent_sources:
    - mstic
  independent: false
  independent_test_failed: >
    Single MSTIC primary in window. The Wiz Research, Snyk,
    StepSecurity, Semgrep, and Aikido Security cohort — vendors who
    independently confirmed and analyzed the May 12 Mini Shai-Hulud
    (VT-006) campaign attributed by Wiz/StepSecurity to TeamPCP —
    have NOT yet published on vpmdhaj at AM sweep time 2026-05-29
    07:42 EDT. The CISA KEV catalog does not yet list any vpmdhaj
    package. The Defender ShaiWorm signature family-name is MSTIC's
    own internal-classification observation, not independent
    corroboration of the underlying campaign claim.
  single_source_veto_applied: true
  single_source_veto_layer: campaign_envelope_and_any_actor_attribution_claim
  wep_ceiling_with_veto: likely

first_party_precedence:
  applied: false
  splunk_query_executed: true
  splunk_query: 'index=defenseclaw_local OR index=archimedes (src_ip=169.254.169.254 OR dest_ip=169.254.169.254 OR domain="aab.sportsontheweb.net" OR url="*X-Supply*" OR file_name="payload.bin") earliest=-30d'
  splunk_event_count: 0
  splunk_silent_not_contradictory: true
  hard_rule_8_notes: >
    Splunk silent on aab.sportsontheweb.net C2 domain, X-Supply
    header, payload.bin filename, and AWS metadata-endpoint
    169.254.169.254 / ECS 169.254.170.2 references over -30d window
    against both defenseclaw_local and archimedes indices. Absence
    of evidence is not evidence of absence per INTEL-GRADING.md
    Hard Rule 8 doctrine. First-party precedence not applied — no
    Splunk attestation to bump or contradict.

wep_ceiling: likely
wep_layered:
  campaign_exists_per_mstic: very_likely    # MSTIC primary, vendor self-attestation on own telemetry, detection signatures live
  iocs_valid_aab_sportsontheweb_net_payload_hashes: very_likely    # MSTIC IOC publication, internally coherent
  fourteen_packages_taken_down: very_likely  # MSTIC vendor coordination claim
  family_lineage_vpmdhaj_in_shaiworm_family: likely  # Defender signature naming is internal-classification signal, not analytic; respect MSTIC silence on attribution
  same_actor_as_may_12_mini_shai_hulud_vt006_teampcp: NOT_ARCHIMEDES_ORIGINATED  # Hard Rule 2 binding; requires Wiz/Snyk/StepSecurity explicit follow-up
  dib_developer_workstation_exposure_via_typosquat_install_path: likely  # Sector-shape WEP framing on structural exposure, not victim-confirmed
  dib_npm_publish_token_theft_downstream_supply_chain_pivot_risk: likely  # Structural-exposure WEP

# Cluster metadata
cluster:
  topic: >
    Microsoft MSTIC discloses npm typosquat campaign by maintainer
    alias `vpmdhaj` distributing 14 packages mimicking OpenSearch /
    ElasticSearch / DevOps configuration libraries; payload steals
    AWS IMDSv2 / ECS task credentials, HashiCorp Vault tokens, AWS
    Secrets Manager entries across 16+ regions, GitHub Actions
    secrets, and npm publish tokens; two-stager architecture (Gen-1
    HTTP C2 to aab.sportsontheweb.net, Gen-2 living-off-Bun-runtime
    loader); Defender signatures Trojan:JS/ShaiWorm + ObfusNpmJs +
    SupplyChain published; family-name signals internal Shai-Hulud
    lineage classification but MSTIC declines actor attribution in
    article prose. Cluster anchored on MSTIC single primary.
  cluster_size: 1
  raw_signal_members:
    - raw-2026-05-29-am-001-mstic-vpmdhaj-npm-typosquat-shaiworm-cloud-cicd-credential-theft-may-28-distinct-or-lineage-question
  attribution_claims:
    - claimed_actor: null
      claimed_by_sources: [mstic]
      claim_language: "newly created maintainer alias vpmdhaj"
      requires_analyst_review: true
      notes: >
        MSTIC names NO tracked threat actor in article body. The
        Defender detection family-name `Trojan:JS/ShaiWorm` is the
        strongest INTERNAL-CLASSIFICATION signal of family lineage
        with the Shai-Hulud / Mini Shai-Hulud (VT-006) cluster which
        Wiz / Snyk / StepSecurity attributed in May 12 reporting to
        TeamPCP (roster id 001) at high confidence. MSTIC does NOT
        restate that attribution for vpmdhaj. Per Hard Rule 2,
        Archimedes does NOT extend the attribution. Analyst should
        treat this as DISTINCT campaign with FAMILY-LINEAGE
        SUGGESTION pending Wiz / Snyk / StepSecurity follow-up.

# Inclusion eligibility
inclusion:
  eligible_for:
    - daily_brief_action
    - weekly_synthesis
    - actor_profile_update    # TeamPCP dossier — append cross-ref note ONLY (lineage suggestion), do NOT bind vpmdhaj as confirmed TeamPCP campaign
    - vuln_tracker_handoff    # VT-006 Mini Shai-Hulud dossier — append "related-distinct-campaign" cross-ref; possible NEW VT-tracker scaffold for vpmdhaj as own cluster pending corroboration
    - ioc_index_update
  ineligible_for:
    - flash    # Not net-new alert-class material in 2-min window — already past the 1200/1800 FLASH; promote to morning brief instead
  rationale: >
    Cluster meets B2-minimum inclusion threshold for action-item brief
    inclusion (A2 anchor). Eligible for actor-profile cross-reference
    (TeamPCP roster 001 dossier — append lineage-suggestion note
    ONLY, do NOT bind vpmdhaj). Eligible for vuln-tracker handoff
    (VT-006 cross-reference + candidate new VT scaffold for vpmdhaj).
    IOC index update warranted (aab.sportsontheweb.net C2, 14
    package names, 3 SHA256 hashes, 1 registry-email,
    1 HTTP-header campaign signature).

# Downstream handoff flags
analyst_review_required: true
analyst_review_reason: >
  Two questions require analyst structured-analysis judgment:
    (1) Family-lineage claim — should the VT-006 Mini Shai-Hulud
        dossier be updated to reflect vpmdhaj as a related-distinct
        campaign in the Shai-Hulud lineage, OR should vpmdhaj be
        scaffolded as its own VT-tracker entry pending Wiz/Snyk/
        StepSecurity corroboration? Recommend SAT-ACH on the
        lineage hypothesis.
    (2) Hard Rule 2 boundary call — the Defender `ShaiWorm`
        signature family-name is unusually strong internal-
        classification evidence of MSTIC's analytic view. The
        analyst should explicitly affirm or revise the grader's
        conservative posture of NOT extending the attribution to
        TeamPCP. Recommend SAT-KAC on the assumption "signature
        family naming = analytic attribution."

red_team_review_required: false
red_team_review_required_reason: >
  WEP ceiling caps at "likely" (not "very likely" or higher) due to
  single-source veto on campaign envelope and all attribution-
  adjacent claims. Red-team review not required per doctrine
  threshold. Analyst may escalate to red-team if Wiz/Snyk/
  StepSecurity follow-up arrives and bumps WEP above "likely."

red_team_review: null
analysis_sections:
  sat_ach:
    ach_analysis:
      question: >
        What is the most defensible characterization of the relationship
        between the vpmdhaj npm typosquat campaign (MSTIC, 2026-05-28) and
        the Shai-Hulud / Mini Shai-Hulud (VT-006) campaign tree previously
        attributed by Wiz / Snyk / StepSecurity to TeamPCP (roster 001)?
      analyzed_at: 2026-05-29T08:42:00-04:00
      analyzed_by: analyst
      analyst_run_id: analyst-20260529-084200
      red_team_review: null
      bound_question_notes: >
        ACH evaluates the LINEAGE/CHARACTERIZATION question. ACH does NOT
        attempt to originate a TeamPCP attribution — per Hard Rule 2, only
        the cited sources can do that, and MSTIC explicitly declines to do
        so for vpmdhaj. The ranking output below characterizes which
        framing is best supported by the in-window evidence; it cannot
        promote MSTIC's silence into a Wiz/Snyk-style attribution claim.

      hypotheses:
        - id: H1
          statement: >
            vpmdhaj is a TeamPCP-operated continuation of the Shai-Hulud /
            Mini Shai-Hulud campaign tree (the Defender `ShaiWorm`
            family-name reflects MSTIC's internal-classification view that
            this is the same actor cluster).
        - id: H2
          statement: >
            vpmdhaj is a distinct actor reusing or copying public Shai-Hulud
            TTPs (npm lifecycle-hook credential-stealer pattern, AWS/Vault
            harvest targets, npm-publish-token pivot) which have been
            documented by Wiz/Snyk/StepSecurity since May 12.
        - id: H3
          statement: >
            vpmdhaj is a TeamPCP-adjacent actor (affiliate, splinter, or
            shared-tooling collaborator) — analogous to Unit 42's
            TGR-CRI-1135 / BlackFile extended-naming pattern seen with the
            broader TeamPCP cluster on 2026-05-28.
        - id: H4
          statement: >
            vpmdhaj is opportunistic / uncoordinated — a single actor or
            small team riding the npm credential-stealer pattern without
            any meaningful tie to Shai-Hulud beyond a vendor
            classification family-name that aggregates broadly similar
            behavior (the null/no-specific-attribution hypothesis).
        - id: H5
          statement: >
            vpmdhaj is an actor deliberately mimicking Shai-Hulud surface
            features (lifecycle hooks, cloud-credential targets, Bun-runtime
            stager) to be classified into the ShaiWorm family by vendor
            detection, masking origin (false-flag / misdirection
            hypothesis).

      evidence:
        - id: E1
          description: >
            MSTIC published Defender signature `Trojan:JS/ShaiWorm` for the
            vpmdhaj campaign — vendor-internal classification places it
            within the ShaiWorm family.
          source: mstic
          digraph: A1
          weight: 3
        - id: E2
          description: >
            MSTIC article prose makes NO actor attribution and does NOT
            cite Wiz / Snyk / StepSecurity prior reporting on TeamPCP, and
            does NOT use the name "TeamPCP" or "Shai-Hulud" in article
            body — only the signature carries the family signal.
          source: mstic
          digraph: A1
          weight: 3
        - id: E3
          description: >
            Cloud-credential target set (AWS IMDSv2, ECS task metadata,
            HashiCorp Vault tokens, AWS Secrets Manager 16+ regions,
            GitHub Actions secrets, npm publish tokens) matches the
            Shai-Hulud / Mini Shai-Hulud (VT-006) target set documented
            by Wiz/Snyk/StepSecurity in May 12 reporting.
          source: mstic
          digraph: A2
          weight: 3
        - id: E4
          description: >
            npm lifecycle-hook abuse pattern (preinstall/install/postinstall
            triple-hook in Gen-1; single preinstall in Gen-2) matches the
            general Shai-Hulud TTP class but is also a widely-used
            commodity supply-chain credential-stealer pattern (T1195.002
            + T1574) — many non-Shai-Hulud actors use the same execution
            chain.
          source: mstic
          digraph: A2
          weight: 3
        - id: E5
          description: >
            Bun-runtime abuse (Gen-2 stager downloads legitimate Bun
            distribution from oven-sh/bun/releases and executes payload
            through Bun) is novel — NOT documented in Wiz/Snyk/StepSecurity
            May 12 Mini Shai-Hulud (VT-006) reporting; appears for the
            first time in this campaign.
          source: mstic
          digraph: A2
          weight: 3
        - id: E6
          description: >
            Distinct C2 infrastructure — `aab.sportsontheweb.net` with
            campaign-unique header `X-Supply: 1` is not previously
            documented in any Shai-Hulud or Mini Shai-Hulud campaign per
            corpus search.
          source: mstic
          digraph: A2
          weight: 3
        - id: E7
          description: >
            Distinct maintainer identity — newly created npm account
            `vpmdhaj` with registry email `a39155771@gmail.com` is not
            documented in prior Shai-Hulud TeamPCP-attributed reporting;
            14 packages published in a 4-hour window on 2026-05-28.
          source: mstic
          digraph: A2
          weight: 3
        - id: E8
          description: >
            The May 12 Mini Shai-Hulud (VT-006) → Wiz/StepSecurity TeamPCP
            attribution arrived within 24-72 hours of MSTIC-class primary
            disclosure. Same cadence here would arrive by 2026-05-30 or
            2026-05-31; at AM-29 sweep time the Wiz/Snyk/StepSecurity
            cohort is silent on vpmdhaj.
          source: mstic_corpus_pattern
          digraph: B3
          weight: 1
        - id: E9
          description: >
            Public availability of Shai-Hulud TTPs since May 12 lowers
            the imitation cost — any actor with npm publishing capability
            could reproduce the lifecycle-hook + cloud-credential-harvest
            chain. Established base-rate consideration for supply-chain
            ecosystems with prior published research.
          source: analyst_inference
          digraph: F6
          weight: 0.5
        - id: E10
          description: >
            Splunk first-party silent on aab.sportsontheweb.net C2,
            X-Supply header, payload.bin filename, and IMDS/ECS metadata
            access from Node processes over -30d window across
            defenseclaw_local + archimedes indices.
          source: splunk_negative_search
          digraph: A1
          weight: 3

      matrix:
        E1: {H1: C, H2: N, H3: C, H4: I, H5: C}
        E2: {H1: I, H2: C, H3: C, H4: C, H5: C}
        E3: {H1: C, H2: C, H3: C, H4: N, H5: C}
        E4: {H1: C, H2: C, H3: C, H4: C, H5: C}
        E5: {H1: N, H2: C, H3: C, H4: C, H5: N}
        E6: {H1: N, H2: C, H3: C, H4: C, H5: N}
        E7: {H1: N, H2: C, H3: C, H4: C, H5: N}
        E8: {H1: I, H2: N, H3: N, H4: N, H5: N}
        E9: {H1: N, H2: C, H3: N, H4: C, H5: C}
        E10: {H1: N, H2: N, H3: N, H4: N, H5: N}

      inconsistency_counts:
        H1: 2    # E2 (MSTIC declines attribution), E8 (Wiz/Snyk silence at expected cadence point)
        H2: 0
        H3: 0
        H4: 1    # E1 (Defender family-name does some classification work that "no-specific-actor" doesn't account for)
        H5: 0

      diagnostic_evidence:
        E2: >
          Most diagnostic single piece. MSTIC's article body explicitly
          declines attribution despite their own Defender signature
          carrying the ShaiWorm family-name. If H1 were MSTIC's view,
          we would expect prose attribution OR a cross-reference to
          Wiz/Snyk/StepSecurity prior reporting — neither appears.
          This INCONSISTENT cell on H1 is the load-bearing evidence
          for the grader's conservative posture.
        E5_E6_E7: >
          Distinct novel surface (Bun-runtime, aab.sportsontheweb.net
          C2, X-Supply header, new vpmdhaj registry identity) reads as
          NEUTRAL for H1 (could be TeamPCP tooling evolution) but as
          CONSISTENT for H2 / H3 / H4 / H5 (any of which would expect
          distinct surface). The novelty does not refute H1 — actors
          evolve — but it also does not support H1 over the
          alternatives.
        E8: >
          Tripwire-class. At AM-29 sweep time, Wiz/Snyk/StepSecurity
          have NOT relayed vpmdhaj. The May 12 Mini Shai-Hulud
          attribution arrived in 24-72 hours. Their silence at the
          ~24-30h mark is mildly INCONSISTENT with H1 (we would
          expect them to be commenting if this were obviously the
          same actor). This is fragile — could flip in 24-48h.

      ranking:
        - rank: 1
          hypothesis_id: H3
          rationale: >
            Zero inconsistencies. H3 (TeamPCP-adjacent affiliate or
            successor cluster) accommodates BOTH the ShaiWorm family-name
            signal AND MSTIC's explicit prose silence on attribution.
            The Unit 42 TGR-CRI-1135 / BlackFile extended-naming
            pattern on the broader TeamPCP cluster (per finding-2026-
            05-28-0003 corpus context) shows that the TeamPCP-family
            actor space has heterogeneity already documented by named
            IR firms. Distinct surface (E5/E6/E7) and base-rate of
            imitation (E9) are CONSISTENT. H3 fits best because it
            does not require either over-attribution OR rejection of
            the Defender family signal.
          wep: roughly_even_chance
          wep_caveat_explicit: >
            H3 is the leading characterization — NOT a leading
            attribution. WEP "roughly even chance" reflects that H3 is
            an analyst framing, not a sourced attribution. Hard Rule 2
            prohibits promoting this to a TeamPCP-affiliate claim
            unless a source makes it.
        - rank: 2
          hypothesis_id: H2
          rationale: >
            Zero inconsistencies. H2 (distinct actor reusing public
            TTPs) is also fully consistent with the evidence. Base-rate
            (E9) supports it; distinct surface (E5/E6/E7) supports it.
            What separates H2 from H3 is the Defender signature
            family-name (E1) — H3 explains it; H2 treats it as a
            vendor classification convenience that aggregates similar
            behavior.
          wep: roughly_even_chance
        - rank: 3
          hypothesis_id: H4
          rationale: >
            One inconsistency (E1). H4 (null hypothesis — opportunistic
            actor with no Shai-Hulud tie) is partially refuted by the
            Defender family-name signal. A purely opportunistic actor
            with no shared tooling lineage to Shai-Hulud would not
            typically inherit the ShaiWorm family-name classification.
            Cannot be ruled out — Defender family-names occasionally
            aggregate broadly — but ranked below H2/H3.
          wep: unlikely
        - rank: 4
          hypothesis_id: H1
          rationale: >
            Two inconsistencies (E2 MSTIC prose silence; E8 cohort
            silence at expected cadence point). H1 (TeamPCP campaign
            continuation, with Defender signature = MSTIC's analytic
            view) is the hypothesis the family-name MOST DIRECTLY
            suggests — but the inconsistency pattern is structural,
            not artifact. MSTIC has the editorial capacity to make
            attribution and chose not to. If they viewed this as
            TeamPCP, they would say so OR cross-reference
            Wiz/Snyk/StepSecurity. The signature is internal
            classification; the prose is editorial position. These
            are not the same thing.
          wep: unlikely
          wep_caveat_explicit: >
            H1 cannot be promoted by Archimedes regardless of ACH
            ranking — only a cited source can make this attribution.
            Even if H1 were rank-1 here, Hard Rule 2 would prohibit
            origination. ACH's role on H1 is to pressure-test whether
            the grader's CONSERVATIVE posture was correct: it is.
        - rank: 5
          hypothesis_id: H5
          rationale: >
            Zero inconsistencies but requires multiple unverified
            assumptions (actor with capability to deliberately
            engineer Defender-classification outcomes; motivation to
            misdirect attribution; familiarity with Microsoft's
            signature-family taxonomy). Cannot be ruled out but
            requires substantially more evidence than H2/H3.
          wep: very_unlikely

      sensitivity_analysis:
        brittleness: medium
        load_bearing_evidence: [E1, E2, E8]
        if_E1_reinterpreted: >
          If the Defender ShaiWorm family-name were later clarified
          by MSTIC as broad-aggregation (multiple distinct actor
          clusters in one family), H1's distinguishing claim
          collapses; H2/H4 rise. The grader's conservative posture
          is robust to this reinterpretation.
        if_E2_reinterpreted: >
          If MSTIC publishes a follow-up explicitly attributing
          vpmdhaj to TeamPCP, the analysis flips immediately: that
          becomes a sourced attribution (no longer Hard Rule 2
          blocked), H1 rises to rank-1, WEP at "likely" pending
          single-source veto.
        if_E8_flips: >
          If Wiz / Snyk / StepSecurity publish in the next 24-72h
          explicitly binding vpmdhaj to TeamPCP, H1 / H3 both rise
          (Wiz/Snyk usage of "TeamPCP campaign" would support H1
          directly; "TeamPCP-affiliate" or "TeamPCP-adjacent"
          language would support H3). This is the most probable
          near-term observation.

      tripwires:
        - observation: >
            MSTIC publishes a follow-up article or Defender Security
            Intelligence advisory naming TeamPCP, Shai-Hulud actor
            cluster, or cross-referencing Wiz/Snyk/StepSecurity prior
            reporting.
          effect: >
            E2 flips from I to C for H1; H1 rises to rank-1 with
            possible WEP elevation to "likely". The lineage SUGGESTION
            in this finding becomes a sourced lineage CLAIM. Vuln-
            tracker should fold vpmdhaj into VT-006 dossier; TeamPCP
            roster entry gets a confirmed campaign cross-reference.
        - observation: >
            Wiz Research, Snyk, StepSecurity, Semgrep, or Aikido
            publish vpmdhaj coverage in the next 24-72h. Either:
            (a) explicit TeamPCP binding → H1 ranked-1; or
            (b) "TeamPCP-affiliate" / "splinter" / "successor cluster"
            language → H3 ranked-1 with sourced support; or
            (c) explicit distinct-actor framing → H2 ranked-1.
          effect: >
            Rerun ACH with the new evidence; revise vuln-tracker
            disposition; possibly trigger new actor-profile work or
            VT-tracker scaffold.
        - observation: >
            CISA KEV addition for any vpmdhaj package.
          effect: >
            Government attestation on exploitation; raises priority
            but does NOT alter the actor-lineage ACH directly.
        - observation: >
            First-party Splunk hit on aab.sportsontheweb.net,
            X-Supply: 1 header, or 169.254.169.254 access from Node
            processes in DIB environment.
          effect: >
            First-party precedence per Hard Rule 8 — would elevate
            visibility weight and trigger immediate operator alert.
            Does not directly alter actor-lineage ACH unless
            telemetry includes attribution-relevant artifacts.

      conclusion:
        summary: >
          The grader's conservative posture is well-supported by ACH.
          H3 (TeamPCP-adjacent affiliate or successor cluster) and H2
          (distinct actor reusing public TTPs) are tied at zero
          inconsistencies and best fit the evidence. H1 (direct TeamPCP
          continuation) carries two inconsistencies — MSTIC's explicit
          prose silence on attribution, and the Wiz/Snyk/StepSecurity
          cohort's absence at the expected cadence point. The Defender
          `ShaiWorm` family-name signal is real evidence of MSTIC's
          internal-classification view, but it does NOT rise to
          analytic attribution and Hard Rule 2 prohibits Archimedes
          from promoting it past MSTIC's editorial silence. The
          analysis is medium-brittle to imminent Wiz/Snyk/StepSecurity
          follow-up (high-probability near-term tripwire).
        wep: >
          Lineage characterization: "roughly even chance" between H2
          (distinct copycat) and H3 (TeamPCP-adjacent affiliate /
          successor). Direct TeamPCP attribution (H1): "unlikely" per
          ACH ranking AND blocked by Hard Rule 2 regardless. Grader's
          `wep_layered.family_lineage_vpmdhaj_in_shaiworm_family:
          likely` is consistent with this — "in the ShaiWorm family"
          (vendor classification) is supportable; "is TeamPCP"
          (analytic attribution) is not.
        confidence_caveats: >
          Single-source MSTIC primary. High probability of corpus
          shift in next 24-72h as Wiz/Snyk/StepSecurity respond.
          ACH should be rerun on any such relay. The H2/H3 tie at
          rank-1 reflects genuine evidentiary ambiguity — the matrix
          cannot resolve "imitation vs. affiliate" with currently
          available evidence; only cohort follow-up can.

  sat_kac:
    kac_analysis:
      assessment_under_review: >
        "The Microsoft Defender signature family-name `Trojan:JS/ShaiWorm`
        is internal-classification signal, not analytic attribution. The
        grader has taken the conservative posture of NOT extending the
        attribution to TeamPCP based on the signature family-name alone."
      analyzed_at: 2026-05-29T08:48:00-04:00
      analyzed_by: analyst
      analyst_run_id: analyst-20260529-084200
      invoking_context: >
        Grader requested KAC on the load-bearing assumption that
        a vendor detection family-name does not constitute analytic
        attribution. This assumption shapes the WEP ceiling for the
        family-lineage claim and the entire actor-profile-update
        disposition.

      assumptions:
        - id: A1
          statement: >
            Microsoft Defender detection signature family-names are
            generated by an internal classification process that
            aggregates technical similarity (code patterns, behavior
            chains, IOC overlap), not by an analytic attribution
            process that names a specific threat actor cluster.
          category: source_methodology
          stated: true
          why_must_be_true: >
            The grader's entire posture rests on this distinction. If
            Defender signature naming WERE analytic attribution
            (signature name = MSTIC's named-actor view), then the
            grader's refusal to extend attribution would be over-
            conservative — a Defender signature naming would be the
            same epistemic act as a Mandiant report naming an actor.
          when_could_be_false: >
            If Microsoft documented (in MSTIC playbooks, Defender
            documentation, or response to industry questions) that
            signature family-names ARE intended as actor attribution,
            this assumption inverts. There is also a weaker case: if
            MSTIC has a track record of using family-names that
            functionally serve as actor attribution (e.g., signatures
            that map 1:1 to named actors like APT28 or Lazarus).
          evidence_for:
            - mstic_article_body_silence_on_actor_attribution_e2
            - defender_signatures_routinely_aggregate_multiple_actor_clusters_per_industry_practice_general_knowledge
            - mstic_published_actor_attribution_when_intended_via_separate_named_actor_blog_format_distinct_from_signature_publication
          evidence_against: []
          confidence: medium
          centrality: critical
          classification: qualify
          qualifying_caveat: >
            Assessment is "Defender signature family-name = internal
            classification signal only, NOT analytic attribution per
            MSTIC's editorial standard." Caveated rather than tested
            because MSTIC's distinct treatment of family-name signatures
            (technical) vs. named-actor publications (analytic) is
            well-established industry practice. However, the assumption
            should be explicitly stated rather than implicit.
        - id: A2
          statement: >
            MSTIC's silence on actor attribution in the article body
            is editorial intent (they chose not to attribute), not
            editorial oversight (they forgot or didn't notice the
            family-lineage signal in their own signature).
          category: source_intent
          stated: false
          why_must_be_true: >
            If MSTIC's silence is oversight rather than intent, the
            ACH inconsistency cell at E2-H1 weakens — it's not
            MSTIC's editorial position, it's an editorial gap.
          when_could_be_false: >
            MSTIC publication tempo on a same-day campaign disclosure
            sometimes prioritizes IOC/detection content over actor
            framing. The article could be a fast-publication that
            elides actor framing intended for a follow-up.
          evidence_for:
            - mstic_byline_microsoft_defender_security_research_team
            - same_team_publishes_attribution_when_intended_evidenced_by_corpus
            - article_includes_explicit_naming_of_vpmdhaj_alias_e_a39155771_at_gmail_demonstrating_attention_to_actor_layer
          evidence_against:
            - mstic_did_not_cross_reference_wiz_snyk_stepsecurity_may_12_reporting_a_reasonable_gap_in_a_fast_publication
          confidence: medium
          centrality: material
          classification: qualify
          qualifying_caveat: >
            If MSTIC publishes a follow-up adding actor attribution
            within 7 days, the silence-as-intent interpretation
            weakens. Rerun KAC + ACH on the follow-up.
        - id: A3
          statement: >
            The Wiz / Snyk / StepSecurity / Semgrep / Aikido cohort
            has the operational capacity and editorial inclination to
            publish vpmdhaj coverage within 24-72 hours if they assess
            it as TeamPCP-related (same cadence as their May 12 Mini
            Shai-Hulud → TeamPCP response).
          category: source_capacity
          stated: true
          why_must_be_true: >
            The tripwire structure of the ACH (E8) treats cohort
            silence at AM-29 as mild evidence against H1. If the
            cohort doesn't actually have that response cadence on
            non-headline npm campaigns, the inference weakens.
          when_could_be_false: >
            The cohort may prioritize larger or more visible
            campaigns; May 12 Mini Shai-Hulud had broader
            ecosystem impact and may have warranted a tier of
            response that this 14-package campaign doesn't.
          evidence_for:
            - corpus_pattern_may_12_to_may_14_attribution_cycle_documented_in_vt006_lineage
            - wiz_step_security_published_quickly_on_prior_npm_supply_chain_campaigns
          evidence_against:
            - vpmdhaj_smaller_surface_14_packages_4h_window_may_warrant_lower_priority
          confidence: medium
          centrality: material
          classification: qualify
          qualifying_caveat: >
            Cohort silence at AM-29 is weak evidence; window should
            extend to at least 72h before treating silence as
            informative. If at 2026-06-01 the cohort is still silent,
            the inference strengthens.
        - id: A4
          statement: >
            "TeamPCP" is a coherent, stable actor cluster — not a
            fuzzy aggregation of related-but-distinct activities that
            different vendors group differently.
          category: actor_definition
          stated: false
          why_must_be_true: >
            H1 (TeamPCP campaign continuation) only has clean meaning
            if TeamPCP is a defined actor. If TeamPCP is itself a
            cluster-of-clusters (like the Unit 42 TGR-CRI-1135 /
            BlackFile extended-naming pattern documented in
            finding-2026-05-28-0003 suggests), then "TeamPCP
            continuation" vs. "TeamPCP-adjacent" is a less clear
            distinction.
          when_could_be_false: >
            Existing corpus already shows TeamPCP-family naming
            heterogeneity. Roster id 001 is "TeamPCP" but the
            Unit 42 cross-naming (TGR-CRI-1135 + BlackFile) suggests
            the underlying actor space has at least three coexisting
            labels that may not refer to identical operator sets.
          evidence_for:
            - wiz_step_security_may_12_attribution_treated_TeamPCP_as_single_actor
          evidence_against:
            - unit_42_TGR_CRI_1135_BlackFile_naming_in_finding_2026_05_28_0003
            - general_industry_pattern_of_actor_label_fragmentation_in_supply_chain_credential_steals
          confidence: low
          centrality: material
          classification: qualify
          qualifying_caveat: >
            ACH H1 and H3 should be read as a CONTINUUM rather than
            discrete states. "TeamPCP campaign continuation" (H1)
            and "TeamPCP-adjacent affiliate / successor" (H3) may
            represent gradient positions on a single actor-cluster
            spectrum. Vuln-tracker dossier should note this when
            handling VT-006 cross-reference.
        - id: A5
          statement: >
            Hard Rule 2 (no novel attribution) means Archimedes
            CANNOT promote vpmdhaj to TeamPCP attribution regardless
            of how strongly the Defender signature family-name
            suggests it.
          category: doctrine
          stated: true
          why_must_be_true: >
            This is the doctrinal anchor. Even if ACH ranked H1 at
            rank-1 with zero inconsistencies (it did not), Archimedes
            cannot originate the attribution. The cited source
            (MSTIC) declined to make it; Archimedes preserves that
            silence.
          when_could_be_false: >
            Cannot be false within current doctrine. Hard Rule 2 is
            non-negotiable. If MSTIC, Wiz, Snyk, StepSecurity,
            Semgrep, Aikido, or another A/B-grade source makes the
            attribution, Archimedes can then relay it citing them.
          evidence_for: [doctrine_LEGAL_POLICY_attribution_standards, CLAUDE_md_hard_rules]
          evidence_against: []
          confidence: high
          centrality: critical
          classification: sound
        - id: A6
          statement: >
            The grader's conservative posture (NOT extending to
            TeamPCP attribution) results in the correct downstream
            treatment of this finding — appending lineage-suggestion
            cross-references to TeamPCP roster 001 and VT-006
            dossier, rather than binding vpmdhaj as a confirmed
            TeamPCP campaign.
          category: workflow
          stated: true
          why_must_be_true: >
            The actor-profiler and vuln-tracker handoffs operate
            on this binding. If the assumption is wrong, downstream
            dossiers may either over-claim (if the grader was too
            cautious) or under-claim (if the grader was too eager).
          when_could_be_false: >
            The downstream treatment is the right action given the
            assumption — but the wider question is whether the
            assumption should bind WEP at "likely" vs. "very likely"
            on the family-lineage claim. ACH supports "likely" for
            ShaiWorm-family membership and "roughly even chance"
            for any specific lineage characterization.
          evidence_for:
            - ach_h2_h3_tie_at_rank_1
            - grader_wep_layered_family_lineage_likely
          evidence_against: []
          confidence: high
          centrality: peripheral
          classification: sound

      classifications_summary:
        sound: 2
        qualify: 4
        test: 0
        reject: 0

      remediation:
        status: proceed_with_qualifying_caveats
        blocking_assumption: null
        blocking_detail: null
        qualifying_caveats:
          - >
            "Defender signature family-name `Trojan:JS/ShaiWorm` is
            internal-classification signal of family-lineage by
            MSTIC technical convention, NOT analytic attribution."
            (This should appear in the brief's prose AND in the
            VT-006 lineage cross-reference note.)
          - >
            "MSTIC's silence on actor attribution is taken as
            editorial intent. If MSTIC publishes a follow-up
            extending attribution, this finding's posture should
            be revised."
          - >
            "Wiz / Snyk / StepSecurity / Semgrep / Aikido cohort
            silence at AM-29 is weak evidence; window extends to
            72h before silence becomes informative."
          - >
            "TeamPCP as an actor cluster has documented naming
            heterogeneity (Unit 42 TGR-CRI-1135 / BlackFile).
            Lineage suggestions should be read as gradient rather
            than discrete attribution."
        next_action: >
          Proceed with grader's WEP ceiling at "likely" for the
          family-lineage claim. Add qualifying caveats to the brief
          prose AND to vuln-tracker VT-006 cross-reference. Watch
          for Wiz/Snyk/StepSecurity follow-up over the next 72h
          per ACH tripwire E8.

      recommended_wep_after_test:
        if_mstic_publishes_attribution_followup:
          family_lineage_in_shaiworm_family: very_likely
          teampcp_attribution_for_vpmdhaj: likely (newly sourced, single-source veto applies)
        if_wiz_snyk_stepsecurity_explicitly_bind_to_teampcp:
          family_lineage_in_shaiworm_family: very_likely
          teampcp_attribution_for_vpmdhaj: very_likely (multi-source if MSTIC + cohort align)
        if_72h_passes_with_no_cohort_response:
          family_lineage_in_shaiworm_family: likely (unchanged)
          distinct_or_adjacent_cluster_h2_h3: likely (currently roughly_even_chance — silence elevates these)

# Analyst recommendation for briefer (downstream handoff, advisory only)
analyst_recommendation:
  wep_adjustment: none
  wep_adjustment_rationale: >
    Grader's WEP ceiling at "likely" and `wep_layered.family_lineage_
    vpmdhaj_in_shaiworm_family: likely` are well-supported by ACH and
    KAC. No adjustment recommended.
  briefer_caveat_inserts:
    - >
      Brief prose MUST include the qualifying caveat that "Defender
      signature family-name is internal-classification signal of
      family-lineage by MSTIC technical convention, NOT analytic
      attribution to TeamPCP."
    - >
      Brief should explicitly frame the lineage relationship as
      UNRESOLVED between H2 (distinct copycat reusing public TTPs)
      and H3 (TeamPCP-adjacent affiliate / successor) — these are
      tied at rank-1 in ACH and the matrix cannot distinguish them
      with current evidence.
    - >
      Brief should flag the 72h tripwire for Wiz/Snyk/StepSecurity
      response as the most probable near-term corpus shift.
  vuln_tracker_handoff_note: >
    Recommend NEW VT-tracker scaffold for vpmdhaj as own cluster
    (not folded into VT-006) PLUS cross-reference note on VT-006
    dossier indicating lineage suggestion. Rationale: ACH H2/H3
    tie at rank-1 means the corpus should preserve the distinction
    until a source resolves it.
  actor_profiler_handoff_note: >
    Append lineage-suggestion cross-reference to TeamPCP roster 001
    dossier ONLY (no TeamPCP dossier exists at AM-29; if scaffolded,
    the cross-reference goes in the dossier; otherwise on the
    roster entry). Do NOT bind vpmdhaj as confirmed TeamPCP
    campaign. Hard Rule 2 controls.
  red_team_escalation_needed: false
  red_team_escalation_rationale: >
    WEP ceiling at "likely" — below red-team threshold of "very
    likely". If Wiz/Snyk/StepSecurity follow-up bumps WEP above
    "likely", escalate.

# Analyst review complete
analyst_review_complete: true
analyst_review_run_id: analyst-20260529-084200

# Lifecycle
tlp: CLEAR
published_in_briefs: [2026-05-29-morning]
retracted: false
retraction_brief_id: null

# Grader-only handoff notes
grader_handoff_notes: >
  Single MSTIC primary; A-grade vendor source; strong technical
  content; full IOC set; named research team; named campaign /
  actor-alias (vpmdhaj). Distinct campaign launch (May 28) vs.
  May 12 Mini Shai-Hulud (VT-006). Defender ShaiWorm signature
  family naming is suggestive of lineage but NOT MSTIC analytic
  attribution to TeamPCP. Grader respects MSTIC silence. Vuln-
  tracker handoff: append cross-ref to VT-006 + consider new VT
  scaffold for vpmdhaj. Actor-profiler handoff: append lineage-
  suggestion cross-ref to TeamPCP (roster 001) dossier ONLY, do
  NOT bind as confirmed TeamPCP campaign. Splunk first-party
  silent over -30d.

source_health_concerns: []    # No source-health issues surfaced
---

# MSTIC discloses `vpmdhaj` npm typosquat campaign — 14 packages, AWS + Vault + npm-token theft, Bun-runtime abuse, Shai-Hulud family lineage signaled (not attributed)

## Summary

Microsoft MSTIC published a primary-research disclosure on 2026-05-28 23:04 EDT covering an active npm supply-chain campaign by a single threat actor operating under the maintainer alias `vpmdhaj` (registry email `a39155771@gmail.com`). The actor published 14 typosquat packages in a four-hour window on 2026-05-28, mimicking well-known OpenSearch / ElasticSearch / DevOps configuration libraries. The payload — delivered via npm lifecycle hooks (`preinstall` / `install` / `postinstall`) without any victim `require()` — harvests AWS IMDSv2 + ECS task-role credentials, HashiCorp Vault tokens, GitHub Actions secrets, AWS Secrets Manager entries across 16+ regions, and npm publish tokens. Microsoft Defender published three detection signatures: `Trojan:JS/ShaiWorm`, `Trojan:JS/ObfusNpmJs`, `Backdoor:JS/SupplyChain`. The `ShaiWorm` family-name in the signature is the strongest evidence of MSTIC's internal-classification view that vpmdhaj is in the Shai-Hulud lineage previously attributed by Wiz / Snyk / StepSecurity to TeamPCP (Archimedes roster 001) — but MSTIC's article prose makes no actor attribution. Per Hard Rule 2, Archimedes does not extend the attribution.

## Sources

### Microsoft MSTIC / Microsoft Security Blog (mstic, digraph A — grade A per source-grades.yaml)

- URL: https://www.microsoft.com/en-us/security/blog/2026/05/28/typosquatted-npm-packages-used-steal-cloud-ci-cd-secrets/
- Published: 2026-05-28T23:04:52-04:00
- Byline: Microsoft Defender Security Research Team
- Key claim: A single threat actor under maintainer alias `vpmdhaj` published 14 typosquat npm packages targeting OpenSearch / ElasticSearch / DevOps configuration ecosystem on 2026-05-28; two-stager architecture (Gen-1 HTTP C2, Gen-2 Bun-runtime abuse) culminates in a Bun-compiled ~195KB stage-2 payload that harvests AWS / Vault / npm credentials; Defender detection signatures `Trojan:JS/ShaiWorm`, `Trojan:JS/ObfusNpmJs`, and `Backdoor:JS/SupplyChain` are published. Packages were taken down following coordination with the npm team.
- Direct quote (≤15 words, Hard Rule 6): "newly created maintainer alias vpmdhaj"

## Technical detail

**Campaign envelope.** Fourteen packages published in a four-hour window on 2026-05-28 under a single registry maintainer (`vpmdhaj`, email `a39155771@gmail.com`). High-signal package names enumerated by MSTIC include `@vpmdhaj/elastic-helper`, `@vpmdhaj/devops-tools`, `@vpmdhaj/opensearch-setup`, plus unscoped `opensearch-setup`, `opensearch-setup-tool`, `opensearch-config-utility`, `elastic-opensearch-helper`, `search-engine-setup`, `env-config-manager`, `app-config-utility`. Full 14-package enumeration in MSTIC source; vuln-tracker pulls on dossier update.

**Social engineering layer.** Lookalike naming targets common cluster-management and configuration libraries. Every unscoped package spoofs the legitimate `github.com/opensearch-project/opensearch-js` project in `package.json` `homepage` / `repository` / `bugs` fields. Inflated version numbers (`1.0.7265`, `1.0.9108`, `2.1.9201`) suggest a long mature release history.

**Execution chain — two stager generations.**

*Gen-1 (versions ≤ 1.0.7265):* Triple-hook (`preinstall` + `install` + `postinstall`) invokes `preinstall.js` / `index.js`. The stager collects host context (hostname, platform, arch, Node version, `USER` / `USERNAME`, `cwd`, `INIT_CWD`, `npm_package_*`), base64-encodes it, and POSTs to the C2 with a campaign-unique header `X-Supply: 1`. The same C2 endpoint serves a gunzip-compressed second-stage binary written to `payload.bin` in the package install directory, chmod'd 0755, and spawned detached. `__DAEMONIZED=1` environment variable lets re-entry detect and exit cleanly.

*Gen-2 (versions ≥ 1.0.7266):* Single `preinstall` hook invokes `setup.mjs`, which downloads the legitimate Bun runtime distribution from `github.com/oven-sh/bun/releases` and executes the bundled stage-2 payload through Bun. This is a living-off-the-trusted-vendor pattern — defensive blocking is complicated because the network traffic to GitHub's release CDN is harder to alert on than direct C2.

**Credential theft targets.**

- AWS IMDSv2 (`169.254.169.254`) — IAM instance-role credential harvest.
- AWS ECS task metadata (`169.254.170.2`) — task-role credential harvest.
- AWS Secrets Manager — enumeration across 16+ regions.
- HashiCorp Vault — `VAULT_TOKEN` environment variable + `~/.vault-token` file.
- GitHub Actions — environment context (`GITHUB_TOKEN`, `GITHUB_REPOSITORY`, `RUNNER_*`).
- npm registry — publish-token theft from `~/.npmrc` for follow-on supply-chain pivot.

**MITRE ATT&CK mapping.** T1195.002 (Supply Chain Compromise: Software), T1059.007 (JavaScript), T1552.005 (Unsecured Credentials: Cloud Instance Metadata API), T1552.007 (Container API), T1027 (Obfuscated Files: Bun-compiled), T1071.001 (HTTP C2), T1574 (Hijack Execution: npm lifecycle hooks).

**Defender detections.** `Trojan:JS/ShaiWorm`, `Trojan:JS/ObfusNpmJs`, `Backdoor:JS/SupplyChain`. The `ShaiWorm` family-name in the first signature is the strongest evidence of MSTIC's internal-classification view of this campaign's lineage. Hard Rule 2: family-name in a vendor detection signature is *internal-classification signal*, not *analytic attribution*; the article body does not state an actor attribution, and Archimedes preserves MSTIC's silence.

**Defender hunting indicators.** npm lifecycle script execution against the typosquat package names; `payload.bin` in `node_modules` directories; detached processes with `__DAEMONIZED=1`; Bun runtime downloads by Node.js processes from `github.com/oven-sh/bun/releases`; IMDS/ECS metadata access (`169.254.169.254`, `169.254.170.2`) from Node.js processes.

**Network defense.** Block `aab.sportsontheweb.net`. Alert on HTTP requests carrying header `X-Supply: 1`.

## IOCs surfaced

```yaml
domains:
  - value: aab.sportsontheweb.net
    role: c2
    confidence: high
    first_seen: 2026-05-28
    source: mstic

urls:
  - value: http://aab.sportsontheweb.net/x.php
    role: c2_endpoint_gen1
    confidence: high
    source: mstic

http_headers:
  - name: X-Supply
    value: "1"
    role: campaign_signature
    confidence: high
    detection_use: proxy_log_alert
    source: mstic

email_addresses:
  - value: a39155771@gmail.com
    role: registry_account
    platform: npmjs
    maintainer_alias: vpmdhaj
    confidence: high
    source: mstic

npm_packages_malicious:
  - "@vpmdhaj/elastic-helper"
  - "@vpmdhaj/devops-tools"
  - "@vpmdhaj/opensearch-setup"
  - "opensearch-setup"
  - "opensearch-setup-tool"
  - "opensearch-config-utility"
  - "elastic-opensearch-helper"
  - "search-engine-setup"
  - "env-config-manager"
  - "app-config-utility"
  note: "MSTIC IOC section enumerates the full 14; this finding lists the high-signal subset. Full list deferred to vuln-tracker dossier update."

file_hashes_sha256:
  - value: 638788AFC4F1B5860A328312CAF5895ABD5F5632D28A4F2A85B09076E270D15D
    file_role: preinstall_js_gen1_stager
    confidence: high
    source: mstic
  - value: 77D92EFE7AF3547F71FD41D4A884872D66B1BE9499EAA637E91EAC866911694D
    file_role: setup_mjs_gen2_stager
    confidence: high
    source: mstic
  - value: BFA149694EC6411C23936311A999163ADE54D6F38E2F4B0E3CFB8CB67BD7CFAA
    file_role: payload_gz_stage2_compressed
    confidence: high
    source: mstic

ip_addresses_referenced_not_c2:
  - value: 169.254.169.254
    role: aws_imdsv2_target_NOT_ACTOR_CONTROLLED
    note: "Legitimate AWS metadata endpoint; hunting context only — NOT a C2 indicator."
  - value: 169.254.170.2
    role: aws_ecs_metadata_target_NOT_ACTOR_CONTROLLED
    note: "Legitimate AWS ECS metadata endpoint; hunting context only — NOT a C2 indicator."

defender_detection_signatures:
  - "Trojan:JS/ShaiWorm"
  - "Trojan:JS/ObfusNpmJs"
  - "Backdoor:JS/SupplyChain"

attribution_claims:
  - source: mstic
    actor: null
    notes: >
      MSTIC's article prose makes NO actor attribution. The Defender
      detection family name `Trojan:JS/ShaiWorm` is a strong
      INTERNAL-CLASSIFICATION signal of family lineage with the
      Shai-Hulud / Mini Shai-Hulud (VT-006) cluster which Wiz /
      Snyk / StepSecurity attributed in May 12 reporting to TeamPCP
      (roster 001) at high confidence. MSTIC does NOT restate that
      attribution for vpmdhaj. Per Hard Rule 2, Archimedes does NOT
      extend the attribution. Family-name in vendor signature ≠
      analytic attribution.
```

## A&D relevance

Sector-shape: structural / indirect. No A&D prime named as a victim. Structural exposure applies to any DIB organization with AWS + GitHub Actions + HashiCorp Vault CI/CD pipelines where a developer might install one of the typosquat packages. Most US prime contractors' developer workstations are exposed to the public npm registry. The npm publish-token theft creates downstream supply-chain risk for any DIB vendor that publishes private or public npm packages.

## Relationship to existing findings / corpus

- **VT-006 Mini Shai-Hulud (TanStack ecosystem credential-theft worm, CVE-2026-45321):** Defender `ShaiWorm` family-name in vpmdhaj signature signals MSTIC's internal-classification view of lineage with VT-006. VT-006 is Wiz/StepSecurity-attributed to TeamPCP (Archimedes roster 001) at high confidence. **Lineage SUGGESTION only — not Archimedes-promoted attribution for vpmdhaj.**
- **finding-2026-05-27-0007 (CISA KEV three-add for CVE-2026-45321 + nx Console + DAEMON Tools):** VT-006 state-transitioned to KEV-listed 2026-05-27 — same week as vpmdhaj launch. Pattern relevance only.
- **finding-2026-05-04-0003 (PyTorch Lightning ShaiWorm — Shai-Hulud family-lineage predecessor):** Earlier family-lineage anchor. Procedural-fact relevance for the lineage claim.
- **finding-2026-05-14-0008 / 0009 (May 14 Mini Shai-Hulud follow-up):** Corpus continuation of VT-006 cluster.
- **finding-2026-05-28-0003 (Unit 42 "Out of the Crypt" — TGR-CRI-1135 = TeamPCP cross-ref + Bling Libra / Hazy Scorpius / CL-CRI-1116 BlackFile):** Direct prior coverage of TeamPCP / Unit 42's extended naming of the actor. Lineage-suggestion cross-reference only — Unit 42 in that finding does NOT extend TeamPCP attribution to vpmdhaj.

## Open questions for analyst

1. **Lineage hypothesis (SAT-ACH recommended).** Is vpmdhaj a TeamPCP-operated continuation of the Shai-Hulud / Mini Shai-Hulud campaign tree (per Defender signature family-name signal), or is it a distinct actor reusing or copying the Shai-Hulud TTPs (which are public per Wiz/Snyk/StepSecurity prior reporting)? Competing hypotheses:
   - H1: TeamPCP campaign continuation (Defender signature naming reflects MSTIC's analytic view).
   - H2: Distinct actor copying public Shai-Hulud TTPs (low cost of imitation once TTPs are public).
   - H3: Closely related TeamPCP-adjacent actor (e.g., a TeamPCP affiliate or splinter, similar to Unit 42's TGR-CRI-1135 extended-naming pattern).
2. **Signature-naming-as-attribution assumption (SAT-KAC recommended).** The grader has taken the conservative posture that Defender family-name in a detection signature is *internal-classification signal* and NOT *analytic attribution*. This assumption shapes the entire WEP ceiling. Should the analyst affirm or revise it?
3. **Operational tempo — anticipate Wiz / Snyk / StepSecurity follow-up.** May 12 Mini Shai-Hulud (VT-006) was followed by the Wiz/StepSecurity TeamPCP attribution within 24-72 hours. Same cadence here would arrive by AM/PM 2026-05-30 or 2026-05-31. The morning brief should flag a watch window.
4. **VT-tracker scaffold question for vpmdhaj.** Should this campaign be scaffolded as its own VT-tracker entry (e.g., VT-011-vpmdhaj-npm-cloud-cicd-theft) pending corroboration, OR folded as a state-update note on the VT-006 dossier? Recommend new scaffold; reconcile after Wiz/Snyk follow-up.

## Analytic notes (from analyst review)

ACH on the lineage question ranks H3 (TeamPCP-adjacent affiliate or successor) and H2 (distinct actor reusing public Shai-Hulud TTPs) tied at zero inconsistencies; H1 (direct TeamPCP continuation) carries two inconsistencies — MSTIC's explicit prose silence on attribution and the Wiz/Snyk/StepSecurity cohort's absence at the expected 24-72h cadence. The grader's conservative posture is correct and is supported by the matrix, not weakened by it.

KAC surfaces six load-bearing assumptions; four classify as Qualify (signature methodology, source intent, cohort capacity, TeamPCP cluster coherence), two as Sound (Hard Rule 2 binding, downstream workflow). None are Test-blocking. The interesting find is A4: TeamPCP itself has documented naming heterogeneity (Unit 42's TGR-CRI-1135 / BlackFile labels in finding-2026-05-28-0003), so the H1/H3 distinction is more gradient than discrete — vpmdhaj likely sits somewhere on a single actor-cluster spectrum, and the matrix cannot resolve where without cohort follow-up.

Net: no WEP adjustment; grader's "likely" ceiling on family-lineage holds. Brief should carry the qualifying caveat that the Defender `ShaiWorm` signature family-name is internal-classification signal, not analytic attribution, and should flag the 72h Wiz/Snyk/StepSecurity tripwire as the most probable near-term corpus shift. Recommend new VT-tracker scaffold for vpmdhaj rather than folding into VT-006 — the H2/H3 tie means the corpus should preserve the distinction until a source resolves it.
