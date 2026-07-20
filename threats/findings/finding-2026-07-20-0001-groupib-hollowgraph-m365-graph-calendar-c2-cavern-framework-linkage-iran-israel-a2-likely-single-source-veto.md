---
finding_id: finding-2026-07-20-0001
created_at: 2026-07-20T16:05:00-04:00
graded_by: grader
grading_run_id: afternoon-20260720-160000
grading_mode: scheduled_brief

# Core grading (from admiralty-grading skill output)
digraph: A2
source_reliability:
  grade: A
  source_name: Group-IB (HollowGraph technical analysis) — relayed via BleepingComputer
  source_yaml_id: group-ib          # NOT YET in source-grades.yaml — provisional first-corpus-surface; librarian to add
  grade_rationale: >
    Group-IB is a Tier-1 DFIR / threat-intel vendor with a long-running, named-analyst
    APT-research practice. First Archimedes-corpus surface — no existing source-grades.yaml
    id. Provisional A assigned per the established Tier-1-vendor-research first-surface
    precedent (SentinelLabs 2026-05-08, Bitdefender / Symantec 2026-05-13, Darktrace
    2026-05-14, Check Point Research 2026-07-06). Reached the corpus THIS pass only as a
    BleepingComputer (B, Bill Toulas) relay; Group-IB primary NOT directly retrieved
    (awaiting_direct_retrieval). Operator may ratify at A or downgrade.
  provisional: true
  awaiting_ratification: true
  awaiting_direct_retrieval: true
credibility:
  grade: 2
  checklist_passed:
    - probably_true_ttp_consistent          # Iranian-nexus espionage vs Israel via a tracked C2 framework (Cavern/Cav3rn) is consistent with known campaign targeting; M365 Graph-API/calendar living-off-trusted-cloud C2 is an established, coherent real-world TTP
    - probably_true_no_contradicting_ab      # no A/B source contradicts
    - probably_true_claims_coherent          # HollowGraph mechanism (Graph API reads commands from / exfils via M365 calendar items), IOC (cloudlanecdn[.]com DNS tunneling), config file (logAzure.txt) all internally coherent
  grade_1_withheld_reason: >
    Grade 1 (Confirmed) withheld — single effective source. Group-IB is the sole primary;
    BleepingComputer is a pure relay/rewrite of the Group-IB report, NOT independent
    corroboration (doctrine: an aggregator summarizing a vendor is one source, not two).
    Check Point Research's earlier Cavern-framework work (finding-2026-07-06-0001) concerns
    the framework generally and does NOT independently corroborate the HollowGraph capability
    or the cloudlanecdn[.]com IOC. No independent second evidence basis on THIS malware. Err low.
  rationale: >
    Group-IB reports a new malware component, HollowGraph, that abuses the Microsoft Graph
    API and the calendar feature of compromised M365 mailboxes as a stealthy C2 channel, and
    assesses "with high confidence" that it is linked to the Cavern C2 framework previously
    associated with Iranian actors targeting Israeli entities. Espionage-focused; at least 12
    systems infected (3 actively communicating 2026-06-03 to 2026-07-09). Consistent with
    established Iranian-nexus tradecraft; technically coherent; no contradicting A/B source.
corroboration:
  independent_sources:
    - group-ib             # single effective primary
  independent: false
  independence_test_passed: >
    FAIL — single effective source. BleepingComputer is a relay of Group-IB (remove Group-IB
    and nothing stands). CPR's prior Cavern-framework finding (2026-07-06-0001) is framework-
    level context, not independent corroboration of the HollowGraph capability or its IOCs.
first_party_precedence:
  applied: false
  splunk_evidence: null
  splunk_note: >
    Collector swept archimedes + defenseclaw_local (-90d) on cloudlanecdn[.]com,
    hospitalinstallation[.]com (Cavern Manticore #026 C2), HollowGraph, logAzure — 0 hits.
    Visibility-bounded null (Frank is not an Israeli target); no corroboration bonus.
    Hard Rule 8: silent Splunk does not disconfirm. Trigger 3 did not fire.
single_source_veto_applied: true
single_source_veto_note: >
  Veto applied — single effective source (Group-IB). WEP capped at "likely" regardless of the
  provisional-A letter grade. Lifts on a genuinely independent second evidence basis on the
  HollowGraph capability specifically (a second vendor's telemetry, a first-party Splunk hit,
  or direct Group-IB primary retrieval PLUS an independent corroborator).
wep_ceiling: likely
wep_ceiling_rationale: >
  Capability existence (HollowGraph M365-Graph/calendar C2): LIKELY — coherent, Tier-1-vendor-
  reported, single-source (veto). Tooling-framework linkage to the Cavern C2 framework: per
  Group-IB "high confidence" — recorded as SOURCE-STATED, not hardened by Archimedes.
  Actor identity (Cavern Manticore #026 vs. a distinct Cavern-framework operator vs. Lyceum
  similarity): UNRESOLVED — open analytic question (Hard Rule 2). A&D nexus: STRUCTURAL /
  TTP-portability only — Israel-targeted, NO A&D prime or DIB victim named; the M365-Graph-
  calendar C2 technique is portable to any Microsoft-365 tenant incl. A&D primes (TTP-watch
  interest, NOT asserted targeting).

# Cluster metadata
cluster:
  topic: "HollowGraph — Microsoft Graph / M365-calendar C2 malware Group-IB links (high confidence) to the Cavern C2 framework; Iran-nexus, Israel-targeted espionage"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-07-20-pm-001
  attribution_claims:
    - claim: "HollowGraph linked to the Cavern C2 framework"
      claimed_actor: null                        # tooling-framework linkage, NOT an actor attribution
      claimed_by_sources: [group-ib]
      confidence_language: "with high confidence"
      scope: tooling_framework_linkage
      roster_match: false
      requires_analyst_review: true
    - claim: "technical similarities with the Iranian-nexus actor Lyceum"
      claimed_actor: null
      claimed_by_sources: [group-ib]
      confidence_language: "insufficient to attribute the activity to the threat actor with high confidence"
      scope: low_confidence_similarity
      roster_match: false                         # Lyceum = OilRig/APT34 #023 subgroup per CPR; NOT asserted here (Hard Rule 2)
      requires_analyst_review: true
    - claim: "Cavern framework previously associated with Iranian threat actors targeting Israeli entities"
      claimed_actor: null
      claimed_by_sources: [group-ib]
      confidence_language: "previously associated"
      scope: framework_provenance
      roster_relationship: "Cavern Manticore #026 (Iran-MOIS) operates the Cavern/Cav3rn framework per CPR / finding-2026-07-06-0001 — relationship recorded, NOT hardened to actor attribution"
      requires_analyst_review: true

# Inclusion eligibility (from admiralty-grading)
inclusion:
  eligible_for:
    - daily_brief_action
    - weekly_synthesis
    - actor_profile_update
  not_eligible_for:
    - flash                  # NON-flash (all six FLASH triggers failed per raw-2026-07-20-pm-001 disposition); scheduled afternoon brief captures it

# Source-grade notes
source_grade_notes: >
  group-ib has no dedicated source-grades.yaml id. Librarian: ADD as provisional A
  (Tier-1-vendor-research first-surface precedent), awaiting_ratification + awaiting_direct_
  retrieval, provenance finding-2026-07-20-0001. No grade revision proposed on any existing source.

# Downstream handoff flags
analyst_review_required: true
analyst_review_note: >
  Attribution is the analytic crux. Group-IB links HollowGraph to the Cavern C2 framework
  (high confidence, TOOLING-level) and offers a LOW-confidence Lyceum similarity — neither is
  a hardened roster-actor attribution. Open question for SAT-ACH: is this a Cavern Manticore
  #026 (Iran-MOIS) cluster DEVELOPMENT (new capability + new IOC on the tracked framework),
  a DISTINCT Cavern-framework operator, or Lyceum (OilRig/APT34 #023 subgroup)? This mirrors
  the standing SAT-ACH question on finding-2026-07-06-0001 (distinct cluster vs. MuddyWater/
  OilRig sub-cluster). Preserve all Group-IB confidence language verbatim (Hard Rule 2); do
  NOT propagate to Cavern Manticore #026 or Lyceum without an independent A-grade attribution
  layer. Also note the M365-Graph-calendar C2 TTP as portable-to-A&D-tenant watch interest.
red_team_review_required: false            # WEP "likely" < "very likely" — unchanged post-SAT
red_team_review: null

# Analyst review (SAT-ACH + SAT-KAC applied 2026-07-20)
analyst_review_complete: true
analyst_review_run_id: analyst-20260720-171500
sats_applied: [sat-ach, sat-kac]
wep_ceiling_adjusted: false                # capability WEP stays "likely"; SATs CONFIRM the grader's capability/identity split
wep_ceiling_adjustment_reason: >
  ACH confirms the grader's framing: capability-existence + Iran-nexus Israel-espionage framing hold at
  "likely" (the shared core across surviving hypotheses; null H5 rejected on 4 inconsistencies). Actor
  identity is UNRESOLVED — the matrix is non-diagnostic among the four Iran-nexus hypotheses; H1 (#026)
  and H2 (distinct Cavern-framework operator) are indistinguishable, and the only pro-#026 evidence (the
  shared framework) is non-diagnostic for identity. No downward WEP adjustment needed because the grader
  never asserted actor identity.
assessment_blocked_pending_test: false     # capability leg proceeds; identity leg already un-asserted (nothing to block)
actor_identity_test_tripwire: >
  KAC A3 (Test): Cavern-framework exclusivity to #026 is unestablished. A future promotion of the
  actor-identity leg is gated on (a) a vendor exclusivity statement, (b) cloudlanecdn[.]com <-> #026
  hospitalinstallation[.]com infra/victim overlap, or (c) evidence of a second distinct Cavern operator.
  Tracked as a tripwire, not a hard block on this finding.
actor_profiler_queue: true
actor_profiler_note: >
  Queue for actor-profiler review of Cavern Manticore #026 (Iran-MOIS). NEW roster-adjacent
  development: an independent vendor (Group-IB) attaches a new capability (HollowGraph, M365
  Graph/calendar C2) and a new IOC (cloudlanecdn[.]com) to the Cavern C2 framework that #026
  operates per CPR/finding-2026-07-06-0001. Actor-profiler to adjudicate whether this warrants
  a #026 dossier development note (tooling-linked, actor unconfirmed) WITHOUT hardening
  attribution (Hard Rule 2). Do NOT re-score threat-box off a single-source tooling linkage.

analysis_sections:
  sat_ach:
    ach_analysis:
      question: "Which actor operates HollowGraph (the M365-Graph/calendar C2 malware Group-IB links to the Cavern C2 framework)?"
      analyzed_at: 2026-07-20T17:20:00-04:00
      analyzed_by: analyst
      analyst_run_id: analyst-20260720-171500
      red_team_review: null
      hard_rule_2_note: >
        This ACH pressure-tests Group-IB's SOURCE-STATED tooling-framework linkage; it does NOT
        originate an actor attribution. Group-IB attributes HollowGraph to NO actor (it links the
        tooling to the Cavern framework at high confidence and hedges a Lyceum similarity as
        "insufficient to attribute"). The ranking-1 output below is "actor identity unresolved" —
        no cited source asserts an actor, so Archimedes asserts none (Hard Rule 2).
      hypotheses:
        - id: H1
          statement: "Cavern Manticore (#026, Iran-MOIS) operates HollowGraph — a new capability and new IOC developed on the framework it is tracked to (per CPR/finding-2026-07-06-0001)."
        - id: H2
          statement: "A distinct Cavern-framework operator (shared/available tooling; a different Iran-nexus actor) operates HollowGraph."
        - id: H3
          statement: "Lyceum / OilRig (#023 sub-cluster) operates HollowGraph — Group-IB's low-confidence technical similarity."
        - id: H4
          statement: "An unknown or otherwise-untracked Iran-nexus actor operates HollowGraph."
        - id: H5
          statement: "Null / non-Iran: the activity is not Iran-nexus targeted espionage; the Cavern-framework association is coincidental, misread, or false-flag mimicry (opportunistic/non-state)."
      evidence:
        - id: E1
          description: "Group-IB high-confidence linkage of HollowGraph to the Cavern C2 framework (framework tracked to #026 per CPR)"
          source: group-ib
          digraph: A2
          weight: 3
        - id: E2
          description: "Novel M365-Graph/calendar living-off-trusted-cloud C2 TTP — NOT the tradecraft documented for #026's prior Cavern activity (sideloaded DLLs + CVE exploitation + hospitalinstallation[.]com)"
          source: group-ib
          digraph: A2
          weight: 3
        - id: E3
          description: "Israel-primary targeting"
          source: group-ib
          digraph: A2
          weight: 3
        - id: E4
          description: "Victimology: small targeted espionage set (~12 infected, 3 active) 2026-06-03 to 2026-07-09"
          source: group-ib
          digraph: A2
          weight: 3
        - id: E5
          description: "New IOC cloudlanecdn[.]com (DNS tunneling) — NO overlap with #026's known C2 hospitalinstallation[.]com"
          source: group-ib
          digraph: A2
          weight: 3
        - id: E6
          description: "Group-IB's own low-confidence technical similarity to Lyceum, explicitly hedged as insufficient to attribute"
          source: group-ib
          digraph: A2
          weight: 3
        - id: E7
          description: "Absence: no independent second vendor (incl. CPR) attaches HollowGraph or cloudlanecdn[.]com specifically to #026 or the Cavern framework"
          source: absence-of-evidence
          digraph: null
          weight: 1
      matrix:
        E1: {H1: C, H2: C, H3: N, H4: C, H5: I}   # framework linkage — CONSISTENT with H1 AND H2; does NOT distinguish operator identity (weakly diagnostic per shared-tooling)
        E2: {H1: N, H2: N, H3: N, H4: N, H5: I}   # novel cloud-C2 TTP — non-diagnostic among Iran hypotheses; inconsistent with opportunistic/non-espionage null
        E3: {H1: C, H2: C, H3: C, H4: C, H5: I}   # Israel targeting — non-diagnostic among Iran hypotheses
        E4: {H1: C, H2: C, H3: C, H4: C, H5: I}   # targeted espionage scope — non-diagnostic among Iran hypotheses
        E5: {H1: N, H2: C, H3: N, H4: N, H5: N}   # new non-overlapping infra — WEAKLY favors distinct operator (H2); infra rotation makes it non-diagnostic against H1
        E6: {H1: N, H2: N, H3: C, H4: N, H5: I}   # Lyceum similarity — weakly favors H3 but Group-IB itself hedges; inconsistent with non-Iran null
        E7: {H1: N, H2: N, H3: N, H4: N, H5: N}   # absence — non-diagnostic; noted for sensitivity (nothing independently ties HollowGraph to #026)
      inconsistency_counts:
        H1: 0
        H2: 0
        H3: 0
        H4: 0
        H5: 4
      non_diagnostic_flag: true
      non_diagnostic_detail: >
        STEP-4 RED FLAG: the matrix is NON-DIAGNOSTIC for actor identity. Among the four Iran-nexus
        hypotheses (H1-H4) no evidence item distinguishes the operator — E1/E3/E4 are consistent with
        all of them, E2 is neutral, and the only weakly-diagnostic items (E5 → H2, E6 → H3) pull AWAY
        from H1 (#026), not toward it. Critically, the sole evidence that would favor #026 (E1, the
        shared Cavern framework) is non-diagnostic for identity because a framework is shared/available
        tooling. The matrix cleanly REJECTS only H5 (null). Per skill guidance this is handled by
        acknowledging underdetermination and widening WEP for the identity question — NOT by forcing a
        pick. This is the expected, honest outcome given Hard Rule 2.
      diagnostic_evidence:
        - E1: "Diagnostic that this is a CAVERN-FRAMEWORK operation and Iran-nexus (vs. null); NON-diagnostic for WHICH operator (H1 vs H2 both C) — the analytic crux."
        - E5: "Weakly diagnostic toward H2 (distinct operator, own infra); no positive infrastructure tie to #026."
        - E6: "Weakly diagnostic toward H3 (Lyceum), but Group-IB explicitly hedges as insufficient to attribute."
      ranking:
        - rank: 1
          hypothesis_id: "H1/H2 (indistinguishable)"
          rationale: >
            H1 (#026) and H2 (distinct Cavern-framework operator) both carry 0 inconsistencies and are
            NOT separable on available evidence. The only pro-#026 evidence (E1 shared framework) is
            non-diagnostic for identity; the one weakly-diagnostic infra item (E5) marginally favors H2.
            There is therefore NO basis to elevate #026 over a distinct-operator explanation. Identity
            unresolved.
          wep: roughly_even_chance
        - rank: 3
          hypothesis_id: H4
          rationale: "Residual untracked-Iran-actor hypothesis; 0 inconsistencies but purely non-diagnostic — cannot be excluded, adds no explanatory parsimony."
          wep: unlikely
        - rank: 4
          hypothesis_id: H3
          rationale: "0 hard inconsistencies but supported only by E6, which Group-IB itself grades low-confidence and insufficient to attribute; framework provenance (E1) does not point to Lyceum."
          wep: unlikely
        - rank: 5
          hypothesis_id: H5
          rationale: "Four inconsistencies (E1/E2/E3/E4, plus E6). Iran-nexus, Israel-targeted, espionage-scoped, framework-linked activity is inconsistent with an opportunistic/non-Iran null. Rejected."
          wep: very_unlikely
      shared_core_across_survivors: >
        What H1-H4 all share and H5 fails: "Iran-nexus, Israel-targeted espionage using a HollowGraph
        capability that Group-IB links (source-stated, high confidence) to the Cavern C2 framework."
        That shared core is well-supported and sits at WEP "likely" (single-source veto). The ACTOR
        IDENTITY layered on top of it is underdetermined.
      sensitivity_analysis:
        brittleness_actor_identity: high
        brittleness_capability_and_framing: medium
        load_bearing_evidence: [E1, "group-ib source reliability"]
        if_E1_reinterpreted: >
          If the Cavern-framework linkage were downgraded or reinterpreted, even the framework leg
          weakens and the finding collapses toward "an Iran-nexus M365 cloud-C2 espionage capability,
          unlinked" — actor identity becomes fully open.
        if_group_ib_downgraded: >
          Group-IB is provisional-A, primary NOT directly retrieved (BleepingComputer relay). If direct
          retrieval fails ratification or downgrades the source, the capability WEP drops below "likely."
        single_point_of_failure: >
          The entire finding rests on one effective source (Group-IB). No first-party Splunk (Frank not
          an Israeli target — visibility-bounded null). Single-source veto already caps at "likely."
      tripwires:
        - observation: "CPR or a second IR vendor independently attaches HollowGraph / cloudlanecdn[.]com to the Cavern framework or #026"
          effect: "Lifts single-source veto; strengthens H1; re-run ACH"
        - observation: "Infrastructure or victim overlap surfaces between cloudlanecdn[.]com and #026's hospitalinstallation[.]com"
          effect: "Diagnostic — strengthens H1 over H2; re-rank"
        - observation: "Evidence the Cavern framework is operated by >=2 distinct clusters"
          effect: "Confirms non-exclusivity; strengthens H2; hardens the shared-tooling framing"
        - observation: "Group-IB primary retrieval reveals actor-attribution language"
          effect: "Re-run ACH with the new source-stated attribution as evidence"
        - observation: "Resolution of the standing SAT-ACH on finding-2026-07-06-0001 (#026 distinct cluster vs. MuddyWater/OilRig sub-cluster)"
          effect: "Informs H3 and the coherence of #026 as an attribution target"
      conclusion:
        summary: >
          Actor identity is UNRESOLVED. The matrix rejects only the null (H5); among the four Iran-nexus
          hypotheses it is non-diagnostic. H1 (Cavern Manticore #026) and H2 (a distinct Cavern-framework
          operator) are indistinguishable, and the only evidence favoring #026 — the shared Cavern
          framework — is non-diagnostic for identity because frameworks are shared/available tooling. The
          shared-framework hypothesis (H2) is NOT excluded and is marginally favored on the one infra
          signal (E5). Archimedes therefore does not elevate #026. What IS well-supported is the shared
          core across all surviving hypotheses: an Iran-nexus, Israel-targeted espionage capability
          (HollowGraph) that Group-IB links source-stated to the Cavern framework — WEP "likely," single-
          source veto.
        wep_actor_identity: roughly_even_chance   # between H1 and H2; no single actor hypothesis reaches "likely"
        wep_capability_and_framing: likely
        confidence_caveats: >
          Single effective source (Group-IB, provisional-A, primary not directly retrieved). Assessment
          is HIGH-brittleness for any actor-identity claim and MEDIUM-brittleness for the capability/
          Iran-espionage framing. Hard Rule 2: no actor attribution originated; framework linkage and
          Lyceum similarity recorded strictly as Group-IB-stated.
  sat_kac:
    kac_analysis:
      assessment_under_review: >
        "HollowGraph is an Iran-nexus, Israel-targeted M365-Graph/calendar C2 espionage capability that
        Group-IB links (high confidence) to the Cavern C2 framework; actor identity is unresolved."
      analyzed_at: 2026-07-20T17:28:00-04:00
      analyzed_by: analyst
      analyst_run_id: analyst-20260720-171500
      invoking_context: "Post-ACH stress-test of the surviving analytic line before the afternoon brief; attribution is the crux."
      assumptions:
        - id: A1
          statement: "Framework linkage implies actor identity (HollowGraph on the Cavern framework => Cavern Manticore #026 operates it)"
          category: attribution_logic
          stated: false
          why_must_be_true: "Any temptation to harden HollowGraph onto #026 depends on tooling-use equating to operator identity"
          when_could_be_false: "Frameworks are shared, sold, leaked, or independently rebuilt; CPR itself describes Cavern as a mature, adaptable toolset — shareable by design"
          evidence_for: []
          evidence_against: [finding-2026-07-06-0001, group-ib]
          confidence: low
          centrality: critical
          classification: reject
          note: "REJECTED as a hardened inference. This is the assumption Hard Rule 2 exists to block. Its rejection is WHY #026 is not elevated (ACH H1/H2 indistinguishable)."
        - id: A2
          statement: "Group-IB's high-confidence HollowGraph<->Cavern tooling call is reliable at first-corpus-surface"
          category: source_reliability
          stated: true
          why_must_be_true: "The framework linkage — the spine of the finding — is a single Group-IB judgment"
          when_could_be_false: "Group-IB is provisional-A, reached the corpus only as a BleepingComputer relay; primary not directly retrieved; ratification pending"
          evidence_for: [group-ib]
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify
          note: "Record as SOURCE-STATED; carry the awaiting_direct_retrieval / awaiting_ratification caveat into the brief."
        - id: A3
          statement: "The Cavern framework is exclusive to #026 (vs. shared / available across multiple operators)"
          category: capability
          stated: false
          why_must_be_true: "H1 (#026 operates HollowGraph) only outranks H2 (distinct operator) if the framework is operator-exclusive"
          when_could_be_false: "No source establishes exclusivity; CPR's 'mature and adaptable toolset' framing and the absence of any infra overlap (E5) both cut toward shareability"
          evidence_for: []
          evidence_against: [finding-2026-07-06-0001]
          confidence: unknown
          centrality: critical
          classification: test
          proposed_test: >
            Watch for (a) a vendor statement that the Cavern framework is under exclusive #026 control,
            or (b) infrastructure/victim overlap tying cloudlanecdn[.]com to #026's hospitalinstallation[.]com,
            or (c) evidence of >=2 distinct Cavern operators. Until then, exclusivity cannot be assumed and
            #026 cannot be elevated. NOTE: this test gates only the (currently un-asserted) actor-identity leg;
            the capability finding proceeds without it.
        - id: A4
          statement: "Cavern Manticore #026 is itself a coherent, distinct actor (not a fuzzy sub-cluster of MuddyWater/OilRig)"
          category: attribution_coherence
          stated: false
          why_must_be_true: "Even a source-stated #026 link is unstable if #026 is not a well-bounded cluster"
          when_could_be_false: "The standing SAT-ACH on finding-2026-07-06-0001 (distinct cluster vs. MuddyWater #022 / OilRig #023 sub-cluster) is UNRESOLVED"
          evidence_for: [finding-2026-07-06-0001]
          evidence_against: []
          confidence: low
          centrality: material
          classification: qualify
          note: "Carry-forward dependency on the unresolved #026 coherence question; do not treat #026 as a settled attribution target."
        - id: A5
          statement: "Group-IB's Lyceum similarity is low-confidence and must not be propagated to OilRig/APT34 #023"
          category: attribution_logic
          stated: true
          why_must_be_true: "Preserving Group-IB's hedge is required by Hard Rule 2"
          when_could_be_false: "n/a — Group-IB explicitly states the similarity is insufficient to attribute"
          evidence_for: [group-ib]
          evidence_against: []
          confidence: high
          centrality: peripheral
          classification: sound
          note: "Keep as recorded low-confidence similarity; do NOT cross-walk to #023."
        - id: A6
          statement: "The Iran-nexus, Israel-targeted, espionage framing of the activity is correct"
          category: intent_context
          stated: true
          why_must_be_true: "The finding's core characterization (what H1-H4 share, what rejects H5) depends on it"
          when_could_be_false: "Single-source; if Group-IB mischaracterized victimology or nexus, the whole finding reframes"
          evidence_for: [group-ib]
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify
          note: "Coherent and Tier-1-reported but single-source — this is the leg that legitimately holds at 'likely.'"
        - id: A7
          statement: "The absence of infrastructure overlap (new domain cloudlanecdn[.]com) is uninformative for attribution"
          category: visibility
          stated: false
          why_must_be_true: "Not-seeing shared infra should not by itself argue for or against #026"
          when_could_be_false: "Infra rotation is normal, so absence is weak; but it also means nothing POSITIVELY ties HollowGraph to #026 beyond the shared framework"
          evidence_for: []
          evidence_against: []
          confidence: medium
          centrality: peripheral
          classification: sound
        - id: A8
          statement: "Frank's silent Splunk (0 hits -90d) does not disconfirm the activity"
          category: visibility
          stated: true
          why_must_be_true: "Absence of first-party telemetry must not be read as negative evidence"
          when_could_be_false: "n/a — Hard Rule 8; Frank is not an Israeli target (visibility-bounded null)"
          evidence_for: []
          evidence_against: []
          confidence: high
          centrality: peripheral
          classification: sound
      classifications_summary:
        sound: 3
        qualify: 3
        test: 1
        reject: 1
      remediation:
        status: proceed
        proceed_scope: >
          The CAPABILITY finding (HollowGraph exists; Iran-nexus, Israel-targeted espionage; framework
          linkage source-stated) proceeds to the briefer at WEP "likely" (single-source veto), carrying
          the qualifying caveats below.
        blocking_assumptions_for_actor_identity: [A1, A3]
        blocking_detail: >
          A1 (rejected) and A3 (test) block any hardening to #026. Because Archimedes is NOT asserting an
          actor identity, there is no assertion to halt — the safe state (identity unresolved) is already
          in force. The A3 test gates only a future promotion of the identity leg, tracked as a tripwire.
        qualifying_caveats:
          - "Framework linkage and Lyceum similarity are Group-IB-stated only; Archimedes originates no actor attribution (Hard Rule 2)."
          - "Cavern framework is NOT established as exclusive to #026 (A3, Test); a distinct Cavern-framework operator is not excluded and is marginally favored on infrastructure grounds."
          - "#026's own cluster coherence is unresolved (A4) pending the standing SAT-ACH on finding-2026-07-06-0001."
          - "Single effective source (Group-IB, provisional-A, primary not directly retrieved); capability leg holds at 'likely,' not higher."
      recommended_wep_after_test:
        capability_existence: likely
        framework_linkage: source_stated_high_confidence   # Group-IB's, not hardened by Archimedes
        actor_identity_if_A3_confirms_exclusive_and_infra_overlap: likely   # would elevate H1 (#026)
        actor_identity_if_A3_confirms_shared_or_no_overlap: "remains unresolved — do not assert; H2 stands co-equal"
        actor_identity_current: roughly_even_chance   # H1 vs H2; no single actor reaches "likely"

# Lifecycle
tlp: CLEAR
published_in_briefs: [2026-07-20-afternoon]
retracted: false
retraction_brief_id: null
---

# HollowGraph — Group-IB links a new Microsoft Graph / M365-calendar C2 malware to the Cavern C2 framework; Iran-nexus, Israel-targeted espionage

## Summary

Group-IB reports a new malware component, HollowGraph, that abuses the Microsoft Graph API
and the calendar feature of compromised Microsoft 365 mailboxes as a stealthy command-and-
control channel — reading attacker commands from and exfiltrating stolen data through calendar
items, blending with legitimate M365 traffic. Group-IB assesses "with high confidence" that
HollowGraph is linked to the Cavern C2 framework previously associated with Iranian actors
targeting Israeli entities, and separately notes a low-confidence technical similarity to the
Iranian-nexus actor Lyceum. The set is espionage-focused and Israel-targeted; at least 12
systems were infected, 3 actively communicating with operators between 2026-06-03 and
2026-07-09. No CVE is referenced and no aerospace or defense victim is named. Archimedes
records Group-IB's tooling-framework linkage and Lyceum similarity as source-stated only and
originates no actor attribution (Hard Rule 2).

## Sources

### Group-IB (group-ib, digraph: A provisional) — relayed via BleepingComputer (B)

- URL: https://www.bleepingcomputer.com/news/security/new-hollowgraph-malware-uses-microsoft-graph-for-stealthy-c2-comms/
- Originating research: Group-IB (HollowGraph technical report; primary NOT directly retrieved)
- Published (relay): 2026-07-20 13:43 EDT (Bill Toulas)
- Key claim: HollowGraph uses the M365 mailbox calendar via Microsoft Graph as a C2 channel;
  linked "with high confidence" to the Cavern C2 framework; Iran-nexus, Israel-targeted; ~12
  systems infected. Low-confidence similarity to Lyceum ("insufficient to attribute").

## Technical detail

- **HollowGraph** — malicious component that abuses the calendar feature of compromised M365
  mailboxes as a C2 channel via the Microsoft Graph API (living-off-trusted-cloud-service;
  blends with legitimate M365 traffic).
- **Framework linkage (source-stated, high confidence):** Group-IB links HollowGraph to the
  Cavern C2 framework ("Cavern"/"Cav3rn" modular .NET C2), described as previously associated
  with Iranian actors targeting Israeli entities. This is the same framework tracked to Cavern
  Manticore (Actor #026, Iran-MOIS) per Check Point Research / finding-2026-07-06-0001.
  Recorded as a TOOLING/framework linkage, NOT an actor attribution.
- **Similarity note (source-stated, low confidence):** Group-IB observed technical similarities
  to the Iranian-nexus actor Lyceum but states evidence is insufficient to attribute with high
  confidence. Lyceum is mapped to OilRig/APT34 (#023) subgroup per CPR — NOT asserted here.
- **Scope:** at least 12 systems infected; 3 actively communicating 2026-06-03 to 2026-07-09.
- **Targeting:** primarily Israel; espionage-focused, targeted intrusion set. No A&D victim named.
- **No CVE** referenced. No file hashes or IPs disclosed in the relay.

## IOCs surfaced

```yaml
domains:
  - value: cloudlanecdn.com
    defanged: "cloudlanecdn[.]com"
    role: c2_dns_tunneling
    context: "DNS tunneling for credential/token refresh (Group-IB via BleepingComputer)"
    actor_id: null            # tooling-linked (Cavern C2 framework); actor unconfirmed
    source: finding-2026-07-20-0001
file_paths:
  - value: logAzure.txt
    role: config_storage
    context: "HollowGraph configuration storage file"
    actor_id: null
    source: finding-2026-07-20-0001
tooling:
  - name: HollowGraph
    type: malware
    detail: "M365-mailbox-calendar C2 via Microsoft Graph API (living-off-trusted-cloud-service)"
  - name: "Cavern C2 framework"
    type: c2_framework
    detail: "Group-IB high-confidence linkage; = 'Cavern'/'Cav3rn' modular .NET C2 tracked to Cavern Manticore #026 per CPR/finding-2026-07-06-0001"
hashes: []
network_iocs_ip: []
credentials_observed: false     # article references credential/token refresh mechanism; NO credential values published or stored (Hard Rule 7)
```

## Relationship to existing findings

- **finding-2026-07-06-0001** (Check Point Research — Cavern / Cav3rn modular .NET C2 framework;
  CPR designates the operator Cavern Manticore, a new MOIS-affiliated cluster, Actor #026 in
  `_roster.yaml`; tracked C2 domain hospitalinstallation[.]com). This Group-IB report is a
  potential NEW development on the SAME Cavern-framework cluster — a fresh capability
  (HollowGraph M365-Graph/calendar C2) and fresh IOC (cloudlanecdn[.]com) attached to the
  framework by an INDEPENDENT vendor. Whether HollowGraph belongs to Cavern Manticore #026,
  a distinct Cavern-framework operator, or Lyceum is the open analytic question — mirroring the
  standing SAT-ACH question on finding-2026-07-06-0001.

## Analytic notes (from analyst review)

ACH and KAC both land in the same place: **attribution is unresolved, and that is the honest
answer.** The evidence rejects only the null hypothesis (opportunistic/non-Iran). Among the four
Iran-nexus hypotheses the matrix is non-diagnostic — nothing separates Cavern Manticore #026 (H1)
from a distinct Cavern-framework operator (H2). The single item that would favor #026, the shared
Cavern framework, is non-diagnostic for identity precisely because a framework is shared, adaptable
tooling. The one weakly diagnostic signal — a brand-new C2 domain with no overlap to #026's known
infrastructure — marginally favors a *distinct* operator, not #026. So the shared-framework
hypothesis is not excluded and arguably fits best.

The load-bearing KAC assumption is A1: "framework linkage implies actor identity." It is rejected —
that inference is exactly what Hard Rule 2 exists to block, and rejecting it is why #026 is not
elevated. Assumption A3 (is the Cavern framework exclusive to #026?) is a low-confidence, critical
Test: nothing establishes exclusivity, so #026 cannot be promoted over a distinct operator.

What **does** hold at "likely" is the shared core across surviving hypotheses: an Iran-nexus,
Israel-targeted M365-Graph/calendar espionage capability that Group-IB links (source-stated, high
confidence) to the Cavern framework. Single effective source; the whole finding is medium-brittle on
Group-IB and high-brittle on any identity claim.

**Briefer guidance:** report the capability and the M365-calendar living-off-trusted-cloud TTP as the
lede (portable to any M365 tenant incl. A&D primes — TTP-watch, not asserted targeting). Characterize
the Cavern-framework link as **Group-IB's** high-confidence *tooling* call, and state plainly that
**this does not identify the operator** — #026 is one candidate, a distinct framework-sharing operator
is equally consistent, and the Lyceum angle is Group-IB's own low-confidence, insufficient-to-attribute
note. Do not name #026 as the actor.

## Open questions for analyst

- **Attribution (crux):** Cavern Manticore #026 development vs. distinct Cavern-framework
  operator vs. Lyceum (OilRig/APT34 #023) similarity — unresolved. Group-IB hardens only the
  TOOLING linkage (high confidence) and hedges Lyceum (low confidence). Do not originate or
  propagate an actor attribution (Hard Rule 2).
- **TTP watch:** M365 Graph API / calendar living-off-trusted-cloud C2 is portable to any
  Microsoft-365 tenant, including A&D primes — record as defensive TTP-watch interest, NOT
  asserted A&D targeting.
- **Corroboration watch:** single effective source (Group-IB via relay). A second independent
  evidence basis on HollowGraph, or direct Group-IB primary retrieval, would lift the veto.
