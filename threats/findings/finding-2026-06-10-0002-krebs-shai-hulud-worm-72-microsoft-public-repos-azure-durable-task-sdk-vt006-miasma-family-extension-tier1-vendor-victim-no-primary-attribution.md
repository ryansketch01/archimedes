---
finding_id: finding-2026-06-10-0002-krebs-shai-hulud-worm-72-microsoft-public-repos-azure-durable-task-sdk-vt006-miasma-family-extension-tier1-vendor-victim-no-primary-attribution
created_at: 2026-06-10T08:14:00-04:00
graded_by: grader
grading_run_id: morning-20260610-080000
grading_mode: scheduled_brief
test: false
status: graded

relates_to:
  - finding-2026-06-03-0001-mstic-miasma-red-hat-npm-credential-stealing-worm-a-grade-originating-primary-second-tier1-attribution-declination-vt006-family-extension
relation_type: vt006_family_extension_to_tier1_vendor_victim_microsoft_with_single_source_relay_at_this_hour_pending_primary_attribution_retrieval

# Core grading (admiralty-grading skill output)
digraph: B3
digraph_layered:
  krebs_published_patch_tuesday_roundup_with_shai_hulud_paragraph_on_microsoft_72_repos: B1   # Vendor-on-own-product-class for Krebs editorial layer is canonical for "Krebs reported X"; verifiable via direct URL retrieval
  at_least_72_microsoft_public_repositories_infected_with_shai_hulud_worm_variant: B3      # Krebs single-source on this specific claim; no primary attribution chain retrieved; pending grader/vuln-tracker primary research vendor retrieval
  affected_packages_connected_to_microsoft_official_azure_durable_task_sdk: B3            # Krebs single-source on the Azure Durable Task SDK named-component framing
  second_touch_infection_on_same_sdk_may_2026_plus_june_2026: B3                          # Krebs single-source on the recurrence framing
  no_primary_attribution_to_teampcp_or_any_named_actor_in_krebs_body: B1                  # Verifiable absence in Krebs text; Hard Rule 2 binding constraint
  shai_hulud_worm_family_taxonomic_designation: B2                                         # Cross-corpus VT-006 family lineage; Krebs body uses the family-name as a relay; family-name designation is malware-family-taxonomy-class NOT actor-attribution-class
  microsoft_battling_internal_zero_day_emergencies_editorial_framing: B3                  # Krebs editorial-layer interpretation; not vendor-attested
  ai_coding_agents_supply_chain_framing: C3                                                # Krebs editorial inference; broad and not load-bearing
  cross_corpus_vt_006_miasma_family_chain_extension_to_tier_1_cloud_platform_vendor: B2   # Internal corpus state lineage; multiple prior corpus findings (finding-2026-05-12-FLASH-0001 origin; finding-2026-06-01-0004; finding-2026-06-02-0003; finding-2026-06-02-0008; finding-2026-06-03-0001) confirm family lineage at high consensus
  archimedes_does_not_originate_teampcp_attribution_per_hard_rule_2_on_microsoft_incident: B1  # Verifiable internal discipline; Tier-1 declination chain (Unit 42 + MSTIC) binds the attribution layer on Miasma extensions
  a_d_relevance_structural_via_azure_durable_task_sdk_dependency_graph_at_a_d_prime_estates: C2  # Grader-side structural inference; no A&D-prime named victim
  microsoft_corp_named_as_victim_tier_1_cloud_platform_vendor: B1                          # Verifiable directly in Krebs body; Microsoft is the named-victim entity
  cluster_anchor: B3

digraph_anchor: >
  Cluster anchored on Krebs on Security (Brian Krebs) "A
  Record-Breaking Patch Tuesday for June 2026" (2026-06-09T22:07
  UTC). Krebs is pre-assigned B per source-grades.yaml; ratified.
  This raw-signal extracts the Shai-Hulud / Microsoft-repos
  paragraph specifically from the Krebs Patch Tuesday article
  (the Patch Tuesday body of the same Krebs article is captured
  separately in finding-2026-06-10-0001).

  B3 (not B2, not B1) anchored because:

    - SOURCE LETTER GRADE: Krebs B (ratified). The sweep did
      NOT retrieve the underlying primary research surface that
      Krebs's "Researchers found..." phrasing relays. The pre-
      brief sentinel called out this gap and queued grader-stage
      retrieval. Without that primary retrieval, the cluster
      anchor is single-source B-grade media relay on a non-
      vendor-self-disclosure claim. (Krebs is NOT Microsoft;
      Krebs is reporting on Microsoft.)

    - INDEPENDENCE TEST: FAILS at the cluster-anchor layer.
      Only one source on the Microsoft 72-repo Azure Durable
      Task SDK Shai-Hulud claim retrieved in window. The
      pre-brief sentinel flagged the following primary surfaces
      as pending grader retrieval:
        (a) MSRC advisory (if Microsoft published one) —
            not retrieved this sweep
        (b) GitHub Security Advisories for the 72 affected
            repositories — not retrieved this sweep
        (c) Tier-1 supply-chain security vendor primary (Wiz /
            Snyk / Socket / StepSecurity / Aikido / Ox Security) —
            not retrieved this sweep
        (d) Microsoft GitHub-org public statement — not
            retrieved this sweep
      Per grader-stage retrieval discipline: the grader should
      not synthesize a primary retrieval inside the 08:00
      morning-brief window that the collector did not perform.
      Promoting at single-source-veto-applied B3 with explicit
      single-source-status preserves the surface for downstream
      vuln-tracker / actor-profiler primary-retrieval work
      without overstating evidence at this hour.

    - CREDIBILITY: Walk the checklist.
      * Grade 1 (Confirmed) — FAILS (no independent
        corroboration).
      * Grade 2 (Probably True) — partially: consistent with
        VT-006 / Miasma family established TTPs against
        ecosystem-packaging targets (npm, PyPI, container
        images, GitHub repositories); consistent with the
        family's known progression toward Tier-1 vendor victims
        across the May–June 2026 corpus chain; no contradicting
        A/B-grade source. However, technical claims at the
        specific 72-repo-count-on-Azure-Durable-Task-SDK layer
        are NOT independently verifiable at this hour
        (claim is plausible but requires primary research
        vendor or vendor-self-disclosure to confirm).
      * Grade 3 (Possibly True) — PASSES: single-source,
        uncorroborated, but source is B-grade (Krebs).
        Partially consistent with VT-006 family established
        TTPs but some elements at the specific-claim layer
        (72 repos, Azure Durable Task SDK named victim,
        May+June second-touch framing) are novel and not
        independently verifiable at this hour. Technical
        claims plausible but not independently verifiable.

    - PROCEDURAL FACTS at the meta-layer ("Krebs published
      this claim in the Patch Tuesday roundup") are B1 canonical
      (Krebs vendor-on-own-product class for Krebs's own
      editorial). SUBSTANTIVE CLAIM layer (the 72-repo
      Azure Durable Task SDK Shai-Hulud infection actually
      happened as Krebs describes) is B3 single-source pending
      primary retrieval.

  Single-source veto APPLIED on the substantive claim layer.
  WEP ceiling capped at "likely" on the substantive claim;
  WEP "very_likely" on the meta-layer "Krebs published the
  claim."

  Hard Rule 2 binding constraint: PRESERVED — Krebs's body
  text does NOT name TeamPCP, Miasma, or any threat-actor for
  the Microsoft Azure Durable Task SDK infection. The TeamPCP
  attribution lineage on the broader Shai-Hulud / Mini Shai-
  Hulud family rests on the originating Wiz + Snyk + StepSecurity
  attribution at the VT-006 anchor + subsequent Tier-1 vendor
  attribution-declination chain (Unit 42 hedge per finding-
  2026-06-02-0008 + MSTIC silence per finding-2026-06-03-0001).
  TWO Tier-1 A-grade vendors decline TeamPCP attribution on
  Miasma extensions; ZERO Tier-1 A-grade affirmations on Miasma
  extensions. Archimedes does NOT propagate TeamPCP attribution
  onto the Microsoft Azure Durable Task SDK incident from Krebs
  alone — Hard Rule 2 binds. The Shai-Hulud family-name
  designation Krebs uses is malware-family-taxonomy-class
  (similar to MSTIC's `Trojan:JS/ShaiWorm.DAW!MTB` Defender
  signature naming), NOT threat-actor attribution.

  Hard Rule 3 binding constraint: PRESERVED — no PoC content,
  no exploit chain detail. Krebs's framing ("infected with a
  variant of the Shai-Hulud worm") is malware-family-class
  description.

  Hard Rule 6: PRESERVED — Krebs paraphrased ≤15 words per
  Hard Rule 7 in raw-signal; finding text preserves <15-word
  quotes only.

  Hard Rule 8 binding constraint: Splunk first-party check ran
  (-30d sweep against Shai-Hulud + Azure Durable Task SDK +
  Miasma + TeamPCP + @redhat-cloud-services + Microsoft GitHub
  + npm-related keywords on index=archimedes OR index=
  defenseclaw_local). 0 substantive events (25 events all
  sourcetype `archimedes:operation` self-instrumentation). Per
  Hard Rule 8: silence is not disconfirming.

source_reliability:
  grade: B
  source_name: "Krebs on Security (Brian Krebs) — 'A Record-Breaking Patch Tuesday for June 2026' (Shai-Hulud / Microsoft 72-repo / Azure Durable Task SDK paragraph specifically)"
  source_yaml_id: krebs
  grade_rationale: >
    Pre-assigned B per source-grades.yaml — ratified B. Strong
    track record, well-sourced reporting. This raw-signal
    sources from the Shai-Hulud paragraph in the Krebs Patch
    Tuesday roundup; the broader Patch Tuesday body is captured
    in finding-2026-06-10-0001.
  provisional: false

credibility:
  grade: 3
  checklist_passed:
    - possibly_true_single_source_uncorroborated_but_source_is_b_grade_krebs
    - possibly_true_partially_consistent_with_vt006_miasma_family_established_ttps_but_some_elements_at_specific_claim_layer_novel
    - possibly_true_technical_claims_plausible_but_not_independently_verifiable_at_this_hour
  rationale: >
    Single B-grade media-relay source on the Microsoft 72-repo
    Azure Durable Task SDK Shai-Hulud infection. Pre-brief
    sentinel flagged the need for primary attribution / primary
    research vendor / vendor-self-disclosure retrieval; that
    primary retrieval was not performed inside the 08:00 morning-
    brief grading window. Per skill Step 4 corroboration
    discipline: corroboration evaluation requires external
    fetching the grader cannot perform inside this window
    without invoking collector tooling that is outside grader
    scope. Grader promotes at C3 monitoring tier with explicit
    single-source-veto disposition and pending-primary-retrieval
    flag for downstream vuln-tracker / actor-profiler / next-
    sweep collector hand-off. The claim is plausible (consistent
    with VT-006 family established progression toward Tier-1
    vendor victims; Krebs is a B-grade source with strong track
    record on accurate technical relay) but not independently
    verifiable at this hour. Promoting at B3 (Possibly True)
    preserves the surface for corpus continuity while
    explicitly recording the evidence weakness.

corroboration:
  independent_sources:
    - krebs
  independent: false
  test_passed: null
  test_failed: >
    Independence test FAILS at the cluster-anchor layer. Only
    one source on the Microsoft 72-repo Azure Durable Task SDK
    Shai-Hulud claim retrieved this sweep. Pre-brief sentinel
    flagged pending primary retrieval: (a) MSRC advisory,
    (b) GitHub Security Advisories on the 72 affected
    repositories, (c) Tier-1 supply-chain security vendor
    primary (Wiz / Snyk / Socket / StepSecurity / Aikido / Ox),
    (d) Microsoft GitHub-org public statement. None of these
    retrieved this sweep; grader does not synthesize primary
    retrieval inside the morning-brief grading window. Single-
    source veto applies on substantive claim layer.

first_party_precedence:
  applied: false
  splunk_evidence: null
  splunk_query_run: >
    -30d sweep across index=archimedes OR index=defenseclaw_local
    on Shai-Hulud + Azure Durable Task + Miasma + TeamPCP +
    Microsoft GitHub repos + npm + @redhat-cloud-services
    superset. 25 events returned, all sourcetype
    `archimedes:operation` self-instrumentation. 0 substantive
    first-party telemetry hits. Per Hard Rule 8: silence is
    not disconfirming.

single_source_veto_applied: true
single_source_veto_detail: >
  Applied on the substantive claim layer (72 Microsoft public
  repositories infected with Shai-Hulud worm variant; affected
  packages connected to Microsoft official Azure Durable Task
  SDK; second-touch infection on same SDK May+June 2026). Krebs
  is the sole source retrieved this sweep on the specific
  Microsoft-incident claim; underlying primary research vendor
  or vendor-self-disclosure was not retrieved. WEP capped at
  "likely" on substantive claim. WEP "very_likely" on meta-
  layer (Krebs published the claim in the Patch Tuesday
  roundup — canonical via direct URL retrieval).

wep_ceiling: likely
wep_layered:
  krebs_published_the_claim_in_patch_tuesday_roundup: very_likely  # Meta-layer canonical via direct URL retrieval
  at_least_72_microsoft_public_repositories_infected_with_shai_hulud_worm_variant: likely  # SINGLE-SOURCE VETOED on substantive claim
  affected_packages_connected_to_microsoft_official_azure_durable_task_sdk: likely  # SINGLE-SOURCE VETOED on substantive claim
  second_touch_infection_on_same_sdk_may_2026_plus_june_2026: likely  # SINGLE-SOURCE VETOED on substantive claim
  vt_006_family_lineage_continuity_to_tier_1_vendor_victim_class: likely  # Cross-corpus inference, single-source on Microsoft surface specifically
  archimedes_does_not_originate_teampcp_attribution_per_hard_rule_2_on_microsoft_incident: almost_certainly  # Internal discipline binding
  no_named_a_d_prime_victim_no_a_d_direct_relevance: almost_certainly  # Verifiable absence in Krebs body
  a_d_structural_relevance_via_azure_durable_task_sdk_dependency_at_a_d_prime_estates: roughly_even_chance  # Grader-side structural inference; depends on A&D-prime Azure GovCloud / Azure for Government adoption patterns
  ai_coding_agents_framing: roughly_even_chance  # Krebs editorial framing; not load-bearing

inclusion:
  eligible_for:
    - daily_brief_monitoring   # B3 meets C3 monitoring floor; tracked-corpus-chain extension warrants visibility
    - weekly_synthesis         # Pattern-emerging signal from VT-006 family progression
  not_eligible_for:
    - flash                    # Below FLASH B2 floor; substantive claim single-source-vetoed
    - daily_brief_action       # Below B2 action floor; single-source-vetoed substantive claim
    - actor_profile_update     # No primary attribution at this surface; Hard Rule 2 binds

# Cluster metadata
cluster:
  topic: >
    Krebs on Security paragraph in the June 2026 Patch Tuesday
    roundup reports that at least 72 of Microsoft's public code
    repositories were infected with a variant of the Shai-Hulud
    worm; affected packages were connected to Microsoft's
    official Azure Durable Task SDK, which Krebs notes was hit
    by the same worm in May 2026. Single B-grade media-relay
    source; underlying primary research vendor or vendor-self-
    disclosure (MSRC advisory, GitHub Security Advisories,
    Tier-1 supply-chain security vendor primary, Microsoft
    GitHub-org statement) not retrieved this sweep. Cross-
    corpus VT-006 / Miasma family extension to Tier-1 cloud
    platform vendor (Microsoft as named victim). No primary
    attribution in Krebs body; per Hard Rule 2, Archimedes
    does NOT originate TeamPCP attribution on the Microsoft
    incident from Krebs alone — TWO Tier-1 A-grade vendors
    (Unit 42 + MSTIC) have explicitly declined TeamPCP
    attribution on Miasma extensions per the prior corpus
    chain. A&D relevance is structural-indirect via Azure
    Durable Task SDK dependency-graph reach at A&D-prime
    Azure GovCloud / Azure for Government estates; no A&D-
    prime named victim.
  cluster_size: 1
  raw_signal_members:
    - raw-2026-06-10-am-002-krebs-shai-hulud-microsoft-72-public-repos-azure-durable-task-sdk-vt-006-miasma-teampcp-family-tier1-vendor
  attribution_claims:
    - claimed_actor: null
      claim_text: >
        Krebs body identifies the malware family as "Shai-Hulud
        worm" (variant) but does NOT name any threat actor
        attribution (no TeamPCP, no Miasma actor label, no
        nation-state, no eCrime cluster). Shai-Hulud worm
        family-name designation is malware-family-taxonomy-
        class NOT actor-attribution-class. The TeamPCP
        attribution lineage on the broader Shai-Hulud / Mini
        Shai-Hulud family rests on the originating Wiz + Snyk
        + StepSecurity attribution at the VT-006 anchor + has
        been EXPLICITLY DECLINED by TWO Tier-1 A-grade vendors
        (Unit 42 hedge per finding-2026-06-02-0008; MSTIC
        silence per finding-2026-06-03-0001) on Miasma
        extensions. Per Hard Rule 2, Archimedes does NOT
        originate TeamPCP attribution on the Microsoft Azure
        Durable Task SDK incident from Krebs alone.
      claimed_by_sources:
        - krebs
      requires_analyst_review: false
      hard_rule_2_status: PRESERVED — malware-family-taxonomy designation only; no threat-actor attribution at Krebs source layer; Tier-1 declination chain on Miasma extensions preserved as corpus stance

related_vulnerabilities: []
related_actors:
  - "TeamPCP (#001 HIGH per _roster.yaml — carry-context only; NOT primary-attributed at this surface; Hard Rule 2 binding)"
related_campaigns:
  - "VT-006 / Mini Shai-Hulud / Miasma family extension to Tier-1 cloud platform vendor (Microsoft Azure Durable Task SDK)"

update_on:
  - finding-2026-06-03-0001-mstic-miasma-red-hat-npm-credential-stealing-worm-a-grade-originating-primary-second-tier1-attribution-declination-vt006-family-extension

# Downstream handoff flags
analyst_review_required: false
analyst_review_rationale: >
  WEP ceiling at "likely" on substantive claim layer; single-
  source-vetoed at this hour pending primary retrieval. No
  primary attribution. No A&D-prime named victim. Pre-flagged
  Tier-1 declination chain on Miasma extensions binds the
  attribution layer. SAT-ACH / SAT-KAC trigger conditions not
  met. Downstream queue priority is vuln-tracker (Shai-Hulud
  family extension tracking) and actor-profiler (TeamPCP
  threat-box re-score consideration deferred to next /update-
  tracking cycle pending primary-attribution corroboration on
  the Microsoft incident).

red_team_review_required: false
red_team_review_rationale: >
  WEP ceiling "likely" does not meet red-team invocation floor
  ("very likely" or higher) on substantive predictive or
  attributive claims. Substantive-claim layer single-source-
  vetoed at this hour. Red-team invocation deferred until
  primary attribution surfaces.

red_team_review: null
analysis_sections:
  sat_ach: null
  sat_kac: null

# Lifecycle
tlp: CLEAR
published_in_briefs: [2026-06-10-morning]
retracted: false
retraction_brief_id: null

# Defensive / IOC handoff flags
ioc_handoff:
  defender_relevant_iocs:
    - "Microsoft Azure Durable Task SDK ecosystem — named-component victim per Krebs (.NET / Python / Java / JavaScript framework for durable-function orchestration)"
    - "At least 72 Microsoft public repositories — affected scope per Krebs (specific repo list not in Krebs body)"
    - "Second-touch infection (May 2026 prior + June 2026 current) per Krebs framing"
    - "VT-006 / Mini Shai-Hulud parent CVE-2026-45321 — references the underlying ecosystem-specific RCE class (not the worm-as-malware itself)"
  iocs_indirect_action: >
    Defender action framing for A&D-DIB estates running Azure
    services / Azure GovCloud / Azure for Government workloads:
    (a) Inventory dependencies on Microsoft Azure Durable Task
    SDK packages across A&D-prime build pipelines and runtime
    environments (NuGet for .NET, npm for JavaScript, PyPI
    for Python, Maven for Java);
    (b) Pin Azure Durable Task SDK package versions to pre-
    incident known-good versions pending Microsoft / GitHub
    Security Advisories landing (advisories not retrieved this
    sweep);
    (c) Monitor CI/CD pipeline outbound traffic for VT-006
    family C2 patterns (anomalous npm / NuGet / PyPI requests
    from build runners; outbound HTTPS to attacker-controlled
    infrastructure observed in prior VT-006 surfaces per
    finding-2026-06-01-0004 and finding-2026-06-03-0001);
    (d) Microsoft GitHub-org statement watch — Microsoft
    typically publishes blog updates when employee-org repos
    are involved;
    (e) MSRC advisory watch — does Microsoft have a
    corresponding security advisory on the Azure Durable Task
    SDK infection? Pending grader / vuln-tracker direct
    retrieval.

monitor_for_next_cycle:
  - MSRC advisory on Azure Durable Task SDK Shai-Hulud infection (pending retrieval)
  - GitHub Security Advisories on the 72 affected Microsoft public repositories (pending retrieval)
  - Tier-1 supply-chain security vendor primary research surface (Wiz / Snyk / Socket / StepSecurity / Aikido / Ox Security) that Krebs's "Researchers found..." phrasing relays — primary research vendor not named in Krebs body
  - Microsoft GitHub-org public statement
  - Any primary attribution to TeamPCP or other actor — if surfaces, would change the attribution-layer disposition; Hard Rule 2 currently binds against propagation
  - Tier-1 A-grade IR firm or vendor-research telemetry on the specific Microsoft incident — would lift cluster from B3 to B2 or B1 layered depending on independence
  - Repo-specific IOCs (package names, file hashes, attacker-controlled GitHub/npm accounts) — none surfaced at this hour

vuln_tracker_handoff:
  scaffold_candidate: true
  scaffold_note: >
    Extend VT-006 family dossier to record the Microsoft
    Azure Durable Task SDK extension claim with Krebs single-
    source-citation status and pending-primary-retrieval flag.
    Do NOT propagate TeamPCP attribution onto the Microsoft
    incident per Hard Rule 2 + the Tier-1 declination chain
    on Miasma extensions. If primary research vendor surface
    is identified in next sweep, re-grade the cluster up.
    The Microsoft Azure Durable Task SDK named-victim
    designation is a notable extension of the family's
    Tier-1-vendor-victim progression (TanStack May origin →
    GitHub-corp internal repos May → Red Hat npm @redhat-
    cloud-services May–June → Microsoft Azure Durable Task
    SDK May+June) and warrants vuln-tracker rollup-entry
    framing.

actor_profiler_handoff:
  scaffold_candidate: false
  threat_box_rescore_consideration: deferred_pending_primary_attribution_corroboration_on_microsoft_incident
  note: >
    TeamPCP (#001 HIGH per _roster.yaml) threat-box re-score
    consideration remains in pending-status per finding-2026-
    05-15-FLASH-0002 briefer flag (commoditization /
    distribution pivot expanding attack-class blast radius).
    This Microsoft 72-repo extension would add weight IF
    primary attribution to TeamPCP is corroborated. Without
    that primary corroboration (and given Tier-1 A-grade
    declination chain on Miasma extensions: Unit 42 hedge +
    MSTIC silence), the re-score does not advance this cycle.
    Per Hard Rule 5, HIGH-tier composite re-scoring requires
    `/approve-scoring` sign-off; not invoked at this hour.

librarian_handoff:
  source_grade_revision_proposed: null

briefer_handoff:
  brief_inclusion_recommendation: monitoring_tier
  brief_substance: >
    Morning brief monitoring section. Headline framing:
    "Krebs reports at least 72 Microsoft public repositories
    infected with Shai-Hulud worm variant tied to Azure Durable
    Task SDK (second-touch May+June); single-source at this
    hour pending primary research vendor / MSRC / GitHub
    Security Advisories retrieval; Hard Rule 2 binds against
    TeamPCP attribution from Krebs alone — TWO Tier-1 vendors
    decline that attribution on Miasma extensions." Keep
    concise (3-4 sentences max in monitoring tier). A&D
    structural relevance via Azure Durable Task SDK dependency-
    graph reach at A&D-prime Azure GovCloud estates is the
    practical defender pivot. Cross-reference VT-006 /
    Mini Shai-Hulud / Miasma family chain (finding-2026-06-03-
    0001 MSTIC originating primary on Red Hat extension;
    finding-2026-06-01-0004 Socket Mini Shai-Hulud).
---

# Krebs Reports at Least 72 Microsoft Public Repositories Infected with Shai-Hulud Worm Variant Tied to Azure Durable Task SDK (Second-Touch May+June 2026) — Single-Source Relay, Primary Attribution Pending

## Summary

Krebs on Security's "A Record-Breaking Patch Tuesday for June 2026" (2026-06-09T22:07 UTC) reports — in a paragraph adjacent to but distinct from the Patch Tuesday body — that **at least 72 of Microsoft's public code repositories were infected with a variant of the Shai-Hulud worm**, and that all affected packages were connected to **Microsoft's official Azure Durable Task SDK**. Krebs notes the SDK was hit by the same worm in May 2026 — a **second-touch infection** on the same component.

This is a single-source B-grade media-relay surface at this hour. The pre-brief sentinel called out four primary surfaces pending grader-stage retrieval: (1) MSRC advisory, (2) GitHub Security Advisories on the 72 affected repositories, (3) Tier-1 supply-chain security vendor primary (the "Researchers found..." that Krebs's framing relays — vendor not named in Krebs body), and (4) Microsoft GitHub-org public statement. None of these were retrieved this sweep. Per skill Step 4 corroboration discipline, the grader does not synthesize primary retrieval inside the 08:00 morning-brief window; the surface is promoted at C3 monitoring tier with explicit single-source-veto disposition.

**Krebs does NOT name TeamPCP or any threat actor for the Microsoft Azure Durable Task SDK infection.** The Shai-Hulud family-name designation Krebs uses is malware-family-taxonomy-class, not threat-actor attribution. Per Hard Rule 2, Archimedes does NOT originate or propagate TeamPCP attribution onto the Microsoft incident from Krebs alone. The prior corpus chain has TWO Tier-1 A-grade vendors explicitly declining TeamPCP attribution on Miasma extensions: Unit 42 hedge per finding-2026-06-02-0008 ("Attribution remains uncertain... the public release of the Mini Shai-Hulud source code means any competent actor can replicate the same attack") and MSTIC silence on TeamPCP per finding-2026-06-03-0001 (full technical writeup with zero mentions of TeamPCP, Mini Shai-Hulud campaign-attribution, or any nation-state / eCrime cluster). The VT-006 / Mini Shai-Hulud TanStack/CVE-2026-45321 base campaign retains TeamPCP attribution at "likely" per Wiz + Snyk + StepSecurity originating layer; the Red Hat / Miasma extension and now the Microsoft Azure Durable Task SDK extension remain UNATTRIBUTED per the Tier-1 declination chain.

A&D relevance is structural-indirect: Microsoft Azure Durable Task SDK is broadly used across enterprise cloud workloads including potential A&D-prime estates running Azure GovCloud / Azure for Government. No A&D-prime named as direct victim.

This finding represents an **UPDATE** to the broader VT-006 / Miasma family chain anchored in finding-2026-06-03-0001 (MSTIC Red Hat npm Miasma originating primary). Grader recommends vuln-tracker extend the VT-006 family dossier to record the Microsoft Azure Durable Task SDK extension claim with single-source-citation status; actor-profiler TeamPCP threat-box re-score consideration remains deferred pending primary-attribution corroboration on the Microsoft incident.

## Sources

### Krebs on Security (krebs, digraph: B3 single-source relay)

- URL: https://krebsonsecurity.com/2026/06/a-record-breaking-patch-tuesday-for-june-2026/
- Published: 2026-06-09T22:07:28 UTC
- Source grade: B (ratified)
- Key claim: At least 72 Microsoft public repositories were infected with a variant of the Shai-Hulud worm; all affected packages were connected to Microsoft's official Azure Durable Task SDK, which was hit by the same worm in May 2026 — a second-touch infection on the same component.
- Verbatim quote (≤15 words, Hard Rule 6 preserved): *"Microsoft battled its own internal zero-day emergencies last week"* (9 words, framing-class) — *"infected with a variant of the Shai-Hulud worm"* (8 words, family-name relay).
- Single-source posture: Krebs's "Researchers found..." phrasing relays an unnamed primary research vendor surface; that primary surface was not retrieved this sweep. No MSRC advisory, no GitHub Security Advisory, no Tier-1 supply-chain security vendor primary, and no Microsoft GitHub-org statement retrieved.

Independence test: FAILS at the substantive claim layer. Single source on the specific Microsoft-incident claim. Single-source veto applies on the substantive claim. The meta-layer ("Krebs published the claim in the Patch Tuesday roundup") is canonical via direct URL retrieval.

## Technical detail

### Substantive claim layer (single-source-vetoed)

| Claim | Source | Status |
|---|---|---|
| At least 72 Microsoft public repositories infected | Krebs | Single-source; pending primary retrieval |
| Affected packages connected to Microsoft official Azure Durable Task SDK | Krebs | Single-source; pending primary retrieval |
| Second-touch infection (May 2026 + June 2026) | Krebs | Single-source; pending primary retrieval (May 2026 prior incident scope: not retrieved) |
| Shai-Hulud worm family-name designation | Krebs | Malware-family-taxonomy-class; cross-corpus consistent with VT-006 family lineage |

### What Krebs's text does NOT include

- **No primary attribution.** Krebs does NOT name TeamPCP, Miasma actor label, or any threat-actor for the Microsoft incident.
- **No CVE.** Mini Shai-Hulud's parent CVE-2026-45321 references the underlying ecosystem-specific RCE class; the worm-as-malware has no standalone CVE.
- **No technical IOCs** (no domains, IPs, package names, file hashes).
- **No data exfiltration scope statement** (whether maintainer credentials from Microsoft developer accounts reached attacker-controlled infrastructure).
- **No MSRC advisory citation** in the Krebs body.
- **No specific named primary research vendor** — "Researchers found..." is unattributed in the retrieved Krebs paragraph.

### Cross-corpus VT-006 / Mini Shai-Hulud / Miasma family chain

| Date | Finding | Surface |
|---|---|---|
| 2026-05-12 | finding-2026-05-12-FLASH-0001 | VT-006 origin — Mini Shai-Hulud npm + PyPI worm; Wiz + Snyk + StepSecurity TeamPCP attribution (high confidence) |
| 2026-05-13+ | finding-2026-05-13 (multiple) | Family extension surfaces |
| 2026-05-20 | finding-2026-05-20-FLASH-0001 | TeamPCP self-claim of GitHub-corp breach via poisoned VS Code marketplace extension (~3,800 internal repos) |
| 2026-05-23 | finding-2026-05-23 | LiteSpeed cPanel sibling tracking; TeamPCP not directly attributed |
| 2026-06-01 | finding-2026-06-01-0004 | Socket Mini Shai-Hulud Red Hat cloud-services npm; api.anthropic[.]com endpoint observation |
| 2026-06-02 | finding-2026-06-02-0003 | SecurityWeek Red Hat npm 32-packages Miasma / Mini Shai-Hulud VT-006 family extension |
| 2026-06-02 | finding-2026-06-02-0008 | Unit 42 npm threat landscape — Miasma / TeamPCP attribution HEDGE |
| 2026-06-03 | finding-2026-06-03-0001 | MSTIC Miasma originating-primary, NO TeamPCP attribution |
| 2026-06-10 | **this finding** | **Microsoft Azure Durable Task SDK 72 public repos infection — single-source relay, primary attribution pending** |

**Attribution trend across this chain:** the originating Wiz + Snyk + StepSecurity TeamPCP attribution at high confidence (May 2026) on the base TanStack/CVE-2026-45321 campaign retains "likely" WEP per the VT-006 dossier state. On Miasma extensions, TWO Tier-1 A-grade vendors (Unit 42 + MSTIC) have explicitly declined TeamPCP attribution, with ZERO Tier-1 A-grade affirmations on Miasma extensions. The Microsoft Azure Durable Task SDK extension inherits the Miasma-extension attribution stance: UNATTRIBUTED pending primary corroboration.

### A&D relevance — structural-indirect

- Microsoft Azure Durable Task SDK is broadly used across enterprise cloud workloads including potential A&D-prime estates running Azure GovCloud / Azure for Government workloads.
- The chain of Tier-1 vendor compromises (Microsoft May+June; OpenAI TanStack May; GitHub-corp internal repos May; Red Hat npm @redhat-cloud-services May–June; multi-victim trail across the family) extends the supply-chain blast radius to Tier-1 cloud-platform infrastructure A&D primes depend upon.
- **No A&D-prime entity named as direct victim.**

## IOCs

```yaml
iocs:
  cves: []   # Shai-Hulud worm has no standalone CVE; VT-006 parent CVE-2026-45321 references the underlying RCE class
  hashes: []
  domains: []
  ipv4: []
  urls: []
  named_victims:
    - entity: Microsoft Corporation
      product_or_org_component: "Azure Durable Task SDK (Microsoft-official .NET/Python/Java/JavaScript framework for durable-function orchestration)"
      victim_class: tier_1_cloud_platform_vendor
      ad_watchlist_member: false
      ad_relevance: structural_indirect
      incident_scope_per_source: "at least 72 public code repositories" (Krebs)
      incident_recurrence: "second touch (May 2026 + June 2026)" per Krebs
      victim_self_disclosure_retrieved: pending_grader_or_collector
  attribution_claims:
    - claim_text: "Variant of the Shai-Hulud worm"
      target: 72 Microsoft public repositories / Azure Durable Task SDK ecosystem
      source: krebs (B-grade media roundup; no upstream researcher named in Krebs body)
      attribution_type: malware_family_label_NOT_threat_actor_attribution
      hard_rule_2_compliant: true
      cross_corpus_lineage: VT-006 Mini Shai-Hulud worm (TeamPCP attribution at originating Wiz/Snyk/StepSecurity layer on TanStack base campaign; Tier-1 A-grade declination chain on Miasma extensions: Unit 42 hedge + MSTIC silence)
      grader_primary_retrieval_required: true
```

## Relationship to existing findings

- **finding-2026-06-03-0001** (MSTIC Miasma Red Hat npm credential-stealing worm — A-grade originating primary; second Tier-1 attribution declination on TeamPCP-on-Miasma) — this Microsoft Azure Durable Task SDK surface is a further extension of the VT-006 / Miasma family chain to a second Tier-1 cloud-platform vendor victim. Attribution-stance inheritance: Tier-1 declination chain binds against TeamPCP attribution on the Microsoft incident.
- **finding-2026-06-02-0008** (Unit 42 npm threat landscape — Miasma / TeamPCP attribution HEDGE) — Unit 42's explicit hedge ("Attribution remains uncertain... any competent actor can replicate the same attack") applies by extension to the Microsoft incident.
- **finding-2026-06-01-0004** (Socket Mini Shai-Hulud Red Hat cloud-services npm; api.anthropic[.]com endpoint observation) — earliest Tier-1 vendor surface on the Red Hat extension.
- **finding-2026-05-12-FLASH-0001** (VT-006 origin) — Wiz + Snyk + StepSecurity TeamPCP attribution at high confidence on the TanStack/CVE-2026-45321 BASE campaign; this attribution remains in force per the VT-006 dossier and is UNAFFECTED by Miasma extension declination per logical-scope discipline.
- **finding-2026-05-15-FLASH-0002** (TeamPCP source-code release of Shai-Hulud) — briefer flagged TeamPCP for potential threat-box re-score; this Microsoft 72-repo extension adds weight to that consideration but does not advance the re-score this cycle pending primary-attribution corroboration.
- **finding-2026-05-20-FLASH-0001** (TeamPCP self-claim of GitHub-corp breach via poisoned VS Code marketplace extension) — separate self-claim chain; Microsoft is a different entity (Microsoft Corp vs. GitHub Inc., though Microsoft owns GitHub).

## Open questions for analyst

- Pending primary retrieval: MSRC advisory + GitHub Security Advisories + Tier-1 supply-chain security vendor primary (the "Researchers found..." that Krebs relays) + Microsoft GitHub-org public statement. Any one of these landing in the next sweep cycle would lift this cluster from B3 to B2 layered (single-source veto lifts on corroboration). The collector should prioritize these retrievals in the next pre-brief sweep.
- If primary attribution to TeamPCP surfaces for the Microsoft incident, the actor-profiler should reconsider the TeamPCP threat-box re-score consideration that has been pending since finding-2026-05-15-FLASH-0002. Until then, Hard Rule 2 binds against propagation.
- The Tier-1 declination chain on Miasma extensions (Unit 42 + MSTIC) is the dominant attribution stance for Miasma-class extensions including the Microsoft incident. Analyst should preserve this stance in any subsequent SAT analysis on the broader VT-006 family chain.
- Is the May 2026 prior Microsoft Azure Durable Task SDK incident captured anywhere in the prior corpus? Krebs's framing implies it should be; if no prior corpus surface, the May incident is a corpus-gap that warrants retroactive collection.
