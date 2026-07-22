---
finding_id: finding-2026-07-22-0004
created_at: 2026-07-22T16:24:00-04:00
graded_by: grader
grading_run_id: afternoon-20260722-160000
grading_mode: scheduled_brief

# Core grading (from admiralty-grading skill output)
digraph: B2
source_reliability:
  grade: B
  source_name: "The Record (Recorded Future News) — relay of a CISA/FBI/EPA joint OT advisory"
  source_yaml_id: the-record
  underlying_primary:
    source_name: "CISA + FBI + EPA joint advisory (revision/broadening of the April 2026 Iran-OT advisory)"
    grade: A                              # government primary is A-grade, but NOT directly retrieved this sweep
    in_hand_this_cycle: false
    corpus_predecessor: "AA26-097A (April 2026 six-agency Iran-OT advisory, in-corpus)"
  grade_rationale: >
    Anchored B. The claim reaches the corpus as a trade-press relay by The Record (B, per
    source-grades.yaml) of an A-grade CISA/FBI/EPA joint OT advisory. The A-grade government primary
    was NOT directly retrieved this sweep (advisory ID + verbatim attribution string + any IOC
    appendix pending direct retrieval), so the effective load-bearing source is the B-grade relay,
    not the A-grade primary. Same primary-via-relay logic applied to finding-2026-07-22-0001.
  provisional: false
credibility:
  grade: 2
  checklist_passed:
    - probably_true_ttp_consistent          # HMI/SCADA display manipulation, malicious project-file interaction, and internet-facing PLC (Rockwell/Allen-Bradley, Schneider, Siemens) targeting are EXACTLY the documented TTPs of the April AA26-097A Iran-OT activity the corpus already tracks (CyberAv3ngers / Actor #028, IRGC-CEC)
    - probably_true_no_contradicting_ab      # no A/B-grade source contradicts; the advisory is presented as a broadening/restatement of a known, corpus-tracked campaign, not a novel or surprising claim
    - probably_true_claims_coherent          # internally coherent — a joint CISA/FBI/EPA advisory restating Iranian OT targeting of water/wastewater, power, and manufacturing PLCs is consistent with the well-established Iran-vs-US-critical-infrastructure pattern
  grade_1_withheld_reason: >
    Grade 1 (Confirmed) withheld: single effective evidence basis. One publisher (The Record) relays
    one government advisory. No independent second source, no separate telemetry, no first-party
    corroboration. Corroboration fails the independence test -> at most grade 2. (Direct retrieval of
    the CISA/FBI/EPA primary would strengthen the source LETTER toward A but would not by itself add
    an INDEPENDENT second basis for grade 1 — it is the same advisory.)
  rationale: >
    The Record (2026-07-22 ~15:18 EDT) relayed a revised joint advisory from CISA, FBI, and the EPA
    broadening an April 2026 alert on Iranian regime-affiliated cyber activity against
    operational-technology environments in US critical infrastructure. The advisory describes
    observed incidents including malicious project-file interactions and manipulation of data on HMI
    and SCADA displays, with operational disruption and financial loss, focused on internet-facing
    PLCs from Rockwell Automation/Allen-Bradley, Schneider Electric, and Siemens. Named sectors: power
    utilities, wastewater treatment, and manufacturing. No aerospace/defense/DIB entity is named. The
    advisory attributes generically to "Iranian regime-affiliated" actors and names no specific group.
    B-grade relay of an A-grade primary, TTP-consistent with corpus-tracked Iran-OT activity, no
    contradiction, single-source -> Probably True.
corroboration:
  independent_sources:
    - the-record
  independent: false
  test_result: >
    Single effective source (The Record relaying one CISA/FBI/EPA advisory). No independent evidence
    basis this cycle. Independence test fails for grade 1. Corpus continuity with the April AA26-097A
    activity is a THEMATIC/TTP correspondence, not an independent corroborating source for THIS
    advisory revision.
first_party_precedence:
  applied: false
  splunk_evidence: null
  splunk_note: >
    Rule 8 run (index=defenseclaw_local OR index=archimedes, NOT sourcetype=archimedes:*, -30d; terms
    included CVE-2021-22681 / HMI / SCADA / PLC). Zero non-Archimedes-internal events. No atomic IOC in
    the relay to pivot on (the advisory appendix, if any, was not directly retrieved). Silent by
    absence-of-artifact and visibility-bounded, NOT disconfirming (Hard Rule 8). Re-run against any IOC
    appendix once the government primary is directly retrieved.
single_source_veto_applied: true
single_source_veto_note: >
  Applies — single effective source (one relay of one advisory). WEP capped at "likely" regardless of
  the underlying A-grade primary. Veto lifts on an independent second source or on direct retrieval of
  the primary PLUS an independent corroborating basis.
wep_ceiling: likely

# Attribution — recorded, NOT originated (Hard Rule 2 — this is the critical care point of this finding)
attribution:
  advisory_attribution_verbatim: "Iranian regime-affiliated / Iranian-government-affiliated (generic — the advisory names NO specific threat group, per the relay)"
  attributed_by: "CISA + FBI + EPA joint advisory, relayed by The Record"
  confidence_language: "advisory names no specific group; The Record caveat: the regime 'sometimes uses ransomware gangs or other groups as cover'"
  archimedes_position: >
    Archimedes reports the advisory's GENERIC Iran attribution as stated and does NOT assert any
    specific group. The correspondence to CyberAv3ngers (Actor #028, IRGC-CEC) is recorded as an
    advisory-line + TTP correspondence to the same April AA26-097A activity the corpus already tracks
    — NOT an Archimedes-originated attribution and NOT an assertion that #028 conducted this specific
    revised-advisory activity. Hard Rule 2 preserved: no novel attribution originated.
  structural_actor_linkage:
    - claimed_actor: null                  # NO actor named by the source; this is a corpus TTP/advisory-line correspondence, not a source attribution
      corpus_correspondence: "CyberAv3ngers (#028) via April predecessor AA26-097A + documented HMI/SCADA/project-file/PLC TTPs"
      basis: "advisory-line continuity (explicit revision of the April advisory) + TTP correspondence"
      requires_analyst_review: true        # analyst/actor-profiler adjudicates whether the corpus linkage is strong enough to note in #028's dossier; grader does NOT assert it
      is_source_attribution: false

# Inclusion eligibility (from admiralty-grading)
inclusion:
  eligible_for:
    - daily_brief_action                   # a fresh CISA/FBI/EPA joint OT advisory revision is an actionable awareness item for the Iran Cyber Watch + OT/ICS sections; B2 clears the B2 floor
    - daily_brief_monitoring
    - weekly_synthesis
    - actor_profile_update                 # actor-profiler reviews the #028 advisory-line correspondence for the CyberAv3ngers dossier (adjudicating, NOT asserting, the linkage)
  flash_eligibility_note: >
    NOT a FLASH. The collector's pre-brief FLASH evaluation is confirmed: Trigger 5 (A&D-sector
    campaign) FAILS on no-named-A&D/DIB-victim; Triggers 2/4 (actor attribution / TTP change) do not
    fire because the advisory names no specific group (generic Iran) and describes no net-new TTP vs
    the April AA26-097A baseline — this is a broadening/restatement of known activity, not a first
    attribution or a TTP shift. Routed to the 16:00 afternoon brief as Iran Cyber Watch + OT/ICS
    sector material.

# A&D relevance (structural / indirect — no A&D victimology)
ad_relevance: medium
ad_relevance_rationale: >
  No aerospace/defense/DIB victim is named — the named sectors are power utilities, wastewater
  treatment, and manufacturing. Relevance is STRUCTURAL / INDIRECT: Rockwell Logix / Allen-Bradley,
  Siemens, and Schneider PLCs are pervasive in A&D manufacturing lines, test ranges, and facility OT,
  so the attack surface is shared with the ITAR-regulated target profile. Rated MEDIUM — a shared-OT-
  attack-surface exposure to a state-affiliated OT threat, not a targeted A&D campaign. Re-rate up on
  any named A&D/DIB victim or a tracked-actor attribution.

# Direct-retrieval / vuln handoffs
handoffs:
  direct_retrieval_todo:
    - "Directly retrieve the CISA/FBI/EPA joint advisory (advisory ID — likely an AA26-XXX revision of AA26-097A), the verbatim attribution string, and any IOC appendix. This would strengthen the source letter toward A and enable a Rule 8 IOC hunt."
  vuln_note: >
    CVE-2021-22681 (VT-027, Rockwell Automation Logix / Studio 5000 authentication bypass; KEV-listed
    2026-03-05; CyberAv3ngers' primary tracked CVE) is STRUCTURALLY implicated by the Rockwell/
    Allen-Bradley PLC targeting but is NOT named in the advisory per the relay. Recorded as structural
    linkage only; no VT-027 state change asserted.
  actor_profiler_note: >
    CyberAv3ngers (#028) dossier candidate-update: advisory-line correspondence (revision of AA26-097A)
    for actor-profiler to adjudicate. Grader does NOT assert #028 for this specific revision (Hard Rule 2).

# Cluster metadata
cluster:
  topic: "CISA/FBI/EPA broaden their April 2026 Iran-OT advisory — HMI/SCADA display manipulation, malicious project-file interaction, and internet-facing PLC (Rockwell/Schneider/Siemens) targeting of US critical infrastructure. Generic Iran attribution (no group named). No A&D victim."
  cluster_size: 1
  raw_signal_members:
    - raw-2026-07-22-pm-001
  attribution_claims:
    - claimed_actor: "Iranian regime-affiliated (generic — NO specific group named by the advisory)"
      claimed_by_sources: [the-record]     # relaying the CISA/FBI/EPA advisory
      requires_analyst_review: true        # the corpus #028/CyberAv3ngers correspondence is for analyst/actor-profiler adjudication, NOT grader assertion
      novel_attribution: false             # generic Iran attribution restates a known, corpus-tracked pattern; no novel first-time attribution (Hard Rule 2 preserved)

# Downstream handoff flags
analyst_review_required: true
analyst_review_note: >
  Flagged per the WEP-"likely" rule AND the attribution correspondence. Focus: (1) adjudicate whether
  the #028/CyberAv3ngers advisory-line + TTP correspondence is strong enough to note in the dossier —
  WITHOUT asserting #028 for this specific revision (Hard Rule 2); (2) confirm the A&D-relevance-MEDIUM
  structural framing holds; (3) note the direct-retrieval-of-primary todo. ACH: only invoke if a genuine
  competing-actor hypothesis space exists — the advisory's generic Iran attribution and the single
  corpus correspondence may not warrant a matrix (risk of manufacturing/originating attribution).
analyst_review_complete: true            # ACH (assessment-framed, NOT actor-framed) + KAC applied. Hard Rule 2 held — no actor hypothesis generated.
analyst_review_run_id: analyst-20260722-165500
analyst_review_outcome: >
  Assessment HOLDS at B2 / "likely" with MEDIUM structural A&D framing. An ASSESSMENT-framed ACH (on
  exposure elevation, NOT "which actor" — no actor hypothesis generated, Hard Rule 2 preserved) refutes
  both an elevation to an A&D-nexus (H1, 3 inconsistencies) and a dismissal to nil exposure (H4, 2
  inconsistencies); the convergent zero-inconsistency reading is restatement/broadening of AA26-097A
  (H2) with opportunistic internet-facing target selection (H3) — supporting the grader's MEDIUM. KAC
  surfaced 6 assumptions (3 sound, 3 qualify, 0 test). Key nuance (A2): A&D-OT exposure to an
  internet-facing-PLC campaign is real but likely MORE BOUNDED than the named water/power/manufacturing
  victims because DIB OT tends to be better segmented — brief the exposure as segmentation-bounded, not
  equated to the victim sectors. Guardrail (A3): the #028 correspondence stays advisory-line/TTP context
  for actor-profiler adjudication; NO attribution originated. Brittleness (A4): the restatement-not-
  escalation reading is brittle to the un-retrieved government primary — tripwire on direct retrieval.
  No WEP adjustment. Not blocked (direct-retrieval is enrichment, not a blocking test).
red_team_review_required: false          # WEP ceiling "likely" < "very likely"; single-source veto binds. Red-team not mandatory.
red_team_review: null
analysis_sections:
  sat_ach:
    ach_analysis:
      question: >
        "What is the best-supported characterization of this CISA/FBI/EPA advisory revision's
        significance for A&D-OT exposure? (An ASSESSMENT-framed ACH on scope/intent/exposure — NOT a
        'which actor' matrix. Hard Rule 2: no actor hypotheses are generated; the advisory names no
        group and the CyberAv3ngers/#028 correspondence is advisory-line/TTP context only, never an
        Archimedes attribution.)"
      analyzed_at: 2026-07-22T16:55:00-04:00
      analyzed_by: analyst
      red_team_review: null
      hard_rule_2_guard: >
        Hypotheses are deliberately framed on the ASSESSMENT axis (exposure elevation), NOT on actor
        identity. Constructing actor hypotheses here would manufacture/originate an attribution the
        advisory does not make (generic 'Iranian regime-affiliated', no group named) and would violate
        Hard Rule 2. The #028 linkage is NOT a hypothesis and is NOT ranked.
      hypotheses:
        - id: H1
          statement: "The advisory implies ELEVATED A&D-OT exposure — a nexus/targeting signal warranting an above-baseline (HIGH) rating."
        - id: H2
          statement: "The advisory is a RESTATEMENT/BROADENING of known Iran-OT activity (AA26-097A baseline); A&D-OT exposure is real but STRUCTURAL and unchanged (MEDIUM) — the grader's position."
        - id: H3
          statement: "Targeting is OPPORTUNISTIC/internet-exposure-driven; A&D-OT exposure is INCIDENTAL (present because A&D shares the internet-facing PLC attack surface), not Iran-A&D-directed."
        - id: H4
          statement: "The advisory OVER-READS for A&D — no meaningful A&D-OT exposure is implied (no A&D victim, no A&D-specific targeting); relevance should be LOW."
      evidence:
        - id: E1
          description: "Advisory is explicitly a revision/broadening of the April 2026 six-agency Iran-OT advisory (corpus AA26-097A)"
          source: the-record
          digraph: B2
          weight: 2
        - id: E2
          description: "Described TTPs (HMI/SCADA display manipulation, malicious project-file interaction, internet-facing PLC targeting) match the April baseline — no net-new TTP"
          source: the-record
          digraph: B2
          weight: 2
        - id: E3
          description: "Named victim sectors are power utilities, wastewater, and manufacturing — NO A&D/DIB entity named"
          source: the-record
          digraph: B2
          weight: 2
        - id: E4
          description: "Targeted PLC families (Rockwell/Allen-Bradley, Schneider, Siemens) are pervasive in A&D manufacturing lines, test ranges, and facility OT"
          source: corpus-inference
          digraph: C3
          weight: 1
        - id: E5
          description: "Advisory describes REAL observed incidents with operational disruption + financial loss (not theoretical)"
          source: the-record
          digraph: B2
          weight: 2
        - id: E6
          description: "Attribution is generic 'Iranian regime-affiliated'; regime 'sometimes uses ransomware gangs or other groups as cover'"
          source: the-record
          digraph: B2
          weight: 2
        - id: E7
          description: "Targeting is of INTERNET-FACING PLCs — consistent with exposure-driven (opportunistic) target selection rather than directed sector victimology"
          source: the-record
          digraph: B2
          weight: 2
        - id: E8
          description: "First-party Splunk silent (visibility-bounded null; no IOC appendix retrieved to hunt on)"
          source: splunk-negative-search
          digraph: A2
          weight: 1
      matrix:
        E1: {H1: N, H2: C, H3: N, H4: N}
        E2: {H1: I, H2: C, H3: C, H4: N}   # no net-new TTP contradicts an escalation/elevation reading
        E3: {H1: I, H2: C, H3: C, H4: C}   # no A&D victim contradicts an A&D-nexus reading
        E4: {H1: C, H2: C, H3: C, H4: I}   # genuine PLC ubiquity contradicts a nil-exposure reading
        E5: {H1: C, H2: C, H3: C, H4: I}   # real incidents contradict an over-read/administrative-only reading
        E6: {H1: N, H2: C, H3: C, H4: N}
        E7: {H1: I, H2: N, H3: C, H4: N}   # internet-facing/exposure-driven contradicts directed A&D targeting
        E8: {H1: N, H2: N, H3: N, H4: N}   # non-diagnostic
      inconsistency_counts:
        H1: 3     # E2, E3, E7
        H2: 0
        H3: 0
        H4: 2     # E4, E5
      diagnostic_evidence:
        - E2: "Distinguishes escalation/elevation (H1, inconsistent) from restatement (H2/H3, consistent)"
        - E3: "Distinguishes an A&D-nexus reading (H1, inconsistent) from structural/incidental exposure (H2/H3/H4)"
        - E7: "Distinguishes directed A&D targeting (H1, inconsistent) from opportunistic exposure-driven selection (H3)"
        - E4: "Distinguishes real shared-attack-surface exposure (H1/H2/H3) from a nil/over-read reading (H4, inconsistent)"
      ranking:
        - rank: 1
          hypothesis_id: H2
          rationale: "Zero inconsistencies. Advisory is an explicit revision/broadening of AA26-097A with baseline-matching TTPs; A&D-OT exposure is real-but-structural. Directly supports the grader's MEDIUM structural rating."
          wep: likely
        - rank: 1
          hypothesis_id: H3
          rationale: "Also zero inconsistencies and CONVERGENT with H2 on the decision-relevant output (MEDIUM structural, not elevated). H3 sharpens the intent framing: exposure is incidental to internet-facing target-of-opportunity selection, not Iran-A&D-directed. NOT a problematic tie triggering halt — H2 and H3 agree on the rating and differ only on the intent gloss; the diagnostic work is the refutation of the two extremes H1/H4."
          wep: likely
        - rank: 3
          hypothesis_id: H4
          rationale: "Two inconsistencies (E4, E5): genuine PLC ubiquity and real disruption/financial-loss incidents refute a nil/over-read reading. A&D exposure is not zero."
          wep: unlikely
        - rank: 4
          hypothesis_id: H1
          rationale: "Three inconsistencies (E2, E3, E7). No net-new TTP, no A&D victim, and exposure-driven internet-facing selection all refute an elevation/A&D-nexus reading. An above-baseline HIGH rating is not supported by the current evidence."
          wep: unlikely
      sensitivity_analysis:
        brittleness: low_to_medium
        load_bearing_evidence: [E2, E3]
        detail: >
          The 'restatement not escalation' conclusion (refutation of H1) rests on E2 (no net-new TTP)
          and E3 (no A&D victim), both from the B-grade Record relay of a government primary that was
          NOT directly retrieved this cycle. If direct retrieval of the CISA/FBI/EPA advisory reveals
          net-new TTPs, a named A&D/DIB victim, or A&D-specific targeting, H1 would rise and the A&D
          rating would elevate above MEDIUM. This is the key brittleness — flagged as a tripwire.
        if_primary_retrieved_shows_netnew_ttp_or_ad_victim: "H1 elevates; re-rate ad_relevance up and re-run this ACH."
      tripwires:
        - observation: "Direct retrieval of the CISA/FBI/EPA primary reveals net-new TTPs vs the AA26-097A baseline."
          effect: "Elevate H1 (escalation); re-run ACH, reconsider ad_relevance."
        - observation: "A source names an aerospace/defense/DIB OT victim of this activity."
          effect: "A&D exposure strengthens from structural to nexus; re-rate up."
        - observation: "A cited A/B source attributes this specific revised-advisory activity to a NAMED group."
          effect: "Attribution becomes reportable (still not originated); hand to grader/actor-profiler. Until then, generic-Iran only (Hard Rule 2)."
      conclusion:
        summary: >
          The best-supported reading is that this advisory revision is a RESTATEMENT/BROADENING of the
          known AA26-097A Iran-OT campaign (H2), with opportunistic internet-facing PLC target selection
          (H3) — the two convergent zero-inconsistency hypotheses. Both an elevation to an A&D-nexus
          (H1, 3 inconsistencies) and a dismissal to nil exposure (H4, 2 inconsistencies) are refuted.
          This supports the grader's MEDIUM structural A&D rating: real shared-PLC-attack-surface
          exposure, NOT a targeted A&D campaign and NOT negligible. No actor hypothesis was generated
          or ranked; the generic-Iran attribution stands exactly as the source states it (Hard Rule 2).
        wep: likely
        confidence_caveats: >
          Single-source (B-grade Record relay); the government primary was not directly retrieved — the
          restatement-vs-escalation reading is brittle to that retrieval (see sensitivity). WEP holds at
          'likely' with the single-source veto. This ACH characterizes SIGNIFICANCE, not attribution.
  sat_kac:
    kac_analysis:
      assessment_under_review: >
        "This CISA/FBI/EPA advisory revision (generic Iran attribution, no group named) on HMI/SCADA
        manipulation and internet-facing Rockwell/Schneider/Siemens PLC targeting implies MEDIUM,
        structural A&D-OT exposure — a shared-attack-surface exposure, not a targeted A&D campaign —
        graded B2 / WEP 'likely'."
      analyzed_at: 2026-07-22T16:55:00-04:00
      analyzed_by: analyst
      invoking_context: >
        Analyst pass flagged by the WEP-'likely' rule + the attribution correspondence. Tests the
        load-bearing exposure assumption and enforces the Hard Rule 2 guardrail on the #028
        correspondence. Grade/WEP grader-owned, unchanged. Run AFTER the assessment-framed ACH above.
      assumptions:
        - id: A1
          statement: "The named PLC families (Rockwell Logix/Allen-Bradley, Siemens, Schneider) are genuinely present in A&D manufacturing/test/facility OT, so the attack surface is shared with the ITAR-regulated target profile."
          category: technology
          stated: true
          why_must_be_true: >
            The MEDIUM structural rating rests on A&D sharing the exploited product attack surface.
          when_could_be_false: >
            Weak only if A&D OT used disjoint PLC vendors — implausible; these three dominate industrial OT.
          evidence_for: []
          evidence_against: []
          confidence: high
          centrality: material
          classification: sound
        - id: A2
          statement: "A&D-OT exposure to THIS campaign is BOUNDED by segmentation — internet-facing PLC exposure in ITAR/CMMC-regulated DIB OT is typically more segmented than in the named water/power/manufacturing victims."
          category: technology
          stated: false
          why_must_be_true: >
            The advisory's targeting is of INTERNET-FACING PLCs. A&D exposure therefore depends on A&D's
            own internet-facing OT posture, which ITAR/NIST 800-171/CMMC pressures tend to segment more
            than water/wastewater utilities (a notoriously exposed sector).
          when_could_be_false: >
            False if DIB suppliers (esp. lower-tier) run internet-exposed PLCs at rates comparable to
            utilities — plausible for smaller Tier-2/3 shops with weaker OT segmentation.
          evidence_for: []
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify
          note: >
            Important nuance: A&D-OT exposure to an INTERNET-FACING-PLC campaign is real but likely more
            bounded than the named victim sectors because DIB OT is typically better segmented. MEDIUM
            is defensible (arguably slightly generous); the briefer should frame exposure as bounded by
            segmentation posture, not equate A&D to the water/power victims.
        - id: A3
          statement: "The generic 'Iranian regime-affiliated' attribution must NOT be narrowed to CyberAv3ngers/#028 for this specific revision (Hard Rule 2)."
          category: source_reliability
          stated: true
          why_must_be_true: >
            The advisory names no group. Narrowing to #028 would originate an attribution no source makes
            for this specific activity.
          when_could_be_false: >
            Only if a cited A/B source explicitly attributes THIS activity to a named group — then it is
            reportable (still not originated). Not the case this cycle.
          evidence_for: [raw-2026-07-22-pm-001]
          evidence_against: []
          confidence: high
          centrality: critical
          classification: sound
          note: >
            GUARDRAIL. The #028 linkage is advisory-line continuity (revision of AA26-097A) + TTP
            correspondence ONLY, for actor-profiler dossier-context adjudication — NOT an Archimedes
            attribution. The assessment-framed ACH above generated NO actor hypothesis. Hard Rule 2 held.
        - id: A4
          statement: "This is a restatement/broadening of the AA26-097A baseline, NOT an escalation with net-new TTPs."
          category: ttp_patterns
          stated: true
          why_must_be_true: >
            The 'no elevation above baseline' exposure rating (MEDIUM, not HIGH) depends on the described
            activity matching the April baseline.
          when_could_be_false: >
            False if the government primary (not retrieved this cycle) documents net-new TTPs or scope.
          evidence_for: [raw-2026-07-22-pm-001]
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify
          proposed_enrichment: "Direct-retrieve the CISA/FBI/EPA primary (advisory ID, verbatim attribution, IOC appendix, TTP list). Confirms restatement-vs-escalation and enables a Rule 8 IOC hunt."
          note: "Brittleness point (see ACH sensitivity). If primary shows net-new TTP/scope, re-rate up."
        - id: A5
          statement: "No named A&D victim means the exposure is neither a nexus (HIGH) nor negligible (LOW) — MEDIUM correctly sits between."
          category: intent
          stated: true
          why_must_be_true: >
            The MEDIUM rating is the middle position between over-reading (nexus) and dismissing (nil).
          when_could_be_false: >
            Shifts up on a named DIB victim / A&D-specific targeting; down if the exploited estate proves
            overwhelmingly non-DIB.
          evidence_for: []
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify
        - id: A6
          statement: "First-party Splunk silence does not disconfirm the advisory (visibility-bounded; no IOC appendix retrieved to hunt on)."
          category: visibility
          stated: true
          why_must_be_true: >
            Per Hard Rule 8, silent first-party does not disprove an external claim absent atomic IOCs.
          when_could_be_false: >
            Only with a retrieved IOC appendix AND an adequately-scoped clean hunt.
          evidence_for: []
          evidence_against: []
          confidence: high
          centrality: peripheral
          classification: sound
      classifications_summary:
        sound: 3
        qualify: 3
        test: 0
        reject: 0
      load_bearing_assumptions:
        - A2   # segmentation-bounded exposure — the nuance that keeps MEDIUM honest
        - A3   # Hard Rule 2 guardrail on the #028 correspondence (critical centrality)
        - A4   # restatement-not-escalation — brittle to un-retrieved primary
      remediation:
        status: proceed
        blocking_assumption: null
        blocking_detail: >
          Direct-retrieval of the government primary (A4) is enrichment, NOT a blocking Test — the
          MEDIUM/'likely' assessment HOLDS without it. It would only re-rate the exposure UP (if net-new
          TTPs/A&D victim appear), which is a tripwire, not a precondition for publication.
        qualifying_caveats:
          - "Generic 'Iranian regime-affiliated' attribution ONLY; no group named. The CyberAv3ngers/#028 correspondence is advisory-line + TTP context for actor-profiler adjudication, NOT an Archimedes attribution (A3, Hard Rule 2)."
          - "A&D relevance is MEDIUM/structural — a SHARED internet-facing-PLC attack surface, not a targeted A&D campaign; exposure is bounded by DIB OT segmentation posture and is likely more contained than the named water/power/manufacturing victims (A2)."
          - "The 'restatement not escalation' reading rests on a B-grade relay; the government primary was not directly retrieved. Re-rate up on net-new TTPs or a named A&D victim (A4)."
          - "No named A&D/DIB victim — do not frame as an A&D nexus (A5)."
        next_action: >
          Proceed to brief (Iran Cyber Watch + OT/ICS sections) with the caveats above. Direct-retrieve
          the primary for source-letter strengthening + a Rule 8 IOC hunt. Actor-profiler adjudicates
          the #028 dossier-context correspondence WITHOUT asserting #028 for this revision.
      recommended_wep_after_review:
        note: "WEP grader-owned; advisory only."
        concurrence: likely

# Lifecycle
tlp: CLEAR
published_in_briefs: [2026-07-22-afternoon]                  # briefer appends brief_ids
retracted: false
retraction_brief_id: null
---

# CISA/FBI/EPA broaden their Iran-linked OT advisory — HMI/SCADA manipulation and PLC targeting of US critical infrastructure (generic Iran attribution, no A&D victim named)

## Summary

CISA, the FBI, and the EPA issued a revised joint advisory broadening an April 2026 alert on Iranian regime-affiliated cyber activity against operational-technology environments in US critical infrastructure, relayed by The Record on 2026-07-22. The advisory describes observed incidents including malicious project-file interactions and manipulation of data on HMI and SCADA displays, causing operational disruption and financial loss, with targeting focused on internet-facing PLCs from Rockwell Automation/Allen-Bradley, Schneider Electric, and Siemens. Named sectors are power utilities, wastewater treatment, and manufacturing — no aerospace, defense, or DIB entity is named.

Graded B2 / "likely" with the single-source veto applied: the claim reaches the corpus as a B-grade Record relay of an A-grade government advisory that was not directly retrieved this cycle, so the effective source is the relay. The advisory attributes generically to "Iranian regime-affiliated" actors and names no specific group. Archimedes reports that generic attribution as stated and does not assert any named group — the correspondence to CyberAv3ngers (Actor #028) is recorded as an advisory-line and TTP correspondence for analyst/actor-profiler adjudication, not an Archimedes-originated attribution (Hard Rule 2).

## Attribution handling (Hard Rule 2)

The advisory (per the relay) names NO specific threat group; attribution is generic "Iranian regime-affiliated," and The Record adds that the regime "sometimes uses ransomware gangs or other groups as cover." This advisory is presented as a revision/broadening of the April 2026 six-agency Iran-OT advisory, which the corpus tracks as AA26-097A and associates with CyberAv3ngers (#028, IRGC-CEC). The described TTPs — HMI/SCADA display manipulation, malicious project-file interaction, internet-facing PLC targeting, confirmed disruption plus financial loss — are exactly #028's documented tradecraft. That correspondence is recorded as advisory-line continuity plus TTP match, flagged for analyst/actor-profiler review. Archimedes does NOT assert that #028 conducted this specific revised-advisory activity. No novel attribution is originated.

## Technical detail

- **Activity class:** manipulation of data on HMI and SCADA displays; malicious project-file interactions; targeting of internet-facing programmable logic controllers. Observed impacts: operational disruption and financial loss. Recorded at class level per Hard Rule 3 — no exploitation detail.
- **Affected products (named in the advisory per the relay):** PLCs from Rockwell Automation/Allen-Bradley, Schneider Electric, and Siemens, and possibly other PLC manufacturers.
- **Sectors named:** power utilities, wastewater treatment, manufacturing plants. No A&D/DIB victim.
- **CVE:** none cited in the advisory per the relay. CVE-2021-22681 (VT-027, Rockwell Logix authentication bypass, KEV 2026-03-05, #028's primary tracked CVE) is STRUCTURALLY implicated by the Rockwell/Allen-Bradley targeting but is NOT named — recorded as structural linkage only.
- **Primary not in hand:** the CISA/FBI/EPA advisory itself (ID, verbatim attribution string, IOC appendix) was not directly retrieved this sweep — direct-retrieval todo.

## IOCs surfaced

None. No atomic IOCs (IPs, domains, hashes) in the relay. Any IOC appendix in the government primary was not retrieved this sweep; a Rule 8 first-party hunt should be re-run against it once retrieved. No PoC/exploit content (Hard Rule 3). No credentials in scope (Hard Rule 7).

## Relationship to existing findings

Continuation of the corpus's Iran-OT / critical-infrastructure thread. Explicitly a revision/broadening of the April 2026 six-agency advisory tracked as AA26-097A (CyberAv3ngers / #028). Adjacent to finding-2026-07-12-iran-ondemand-0001 (GigaWiper / Iran-nexus / CyberAv3ngers lineage) and the broader Iran Cyber Watch standing coverage. The generic-Iran attribution and structural PLC-targeting profile mirror the AA26-097A baseline rather than introducing net-new TTPs.

## Analytic notes (from analyst review)

The assessment holds at B2 / "likely" with MEDIUM structural A&D framing. I ran the ACH on the assessment's significance — scope and exposure — not on "which actor," because the advisory names no group and building an actor matrix would originate an attribution no source makes (Hard Rule 2). Framed that way, the matrix cleanly refutes both extremes: an elevation to an A&D nexus fails on three counts (no net-new TTP, no A&D victim, exposure-driven internet-facing target selection), and a dismissal to nil exposure fails on two (the targeted PLC families are genuinely ubiquitous, and the incidents were real). The surviving reading is a restatement/broadening of the April AA26-097A campaign with opportunistic targeting — exactly the grader's MEDIUM.

The load-bearing nuance from KAC: A&D-OT exposure to an internet-facing-PLC campaign is real but likely more bounded than the named water, power, and manufacturing victims, because DIB OT tends to be better segmented under ITAR/CMMC pressure. Brief the exposure as segmentation-bounded, not equated to the victim sectors.

Two caveats for the brief. Attribution stays generic Iran; the CyberAv3ngers/#028 link is advisory-line and TTP correspondence only, for actor-profiler adjudication, never an Archimedes attribution. And the restatement-not-escalation reading is brittle to the un-retrieved government primary — if direct retrieval surfaces net-new TTPs or a named A&D victim, the exposure rating re-rates up.

## Open questions for analyst

- **Direct-retrieve the government primary** (advisory ID, verbatim attribution language, IOC appendix) — this strengthens the source letter and enables a first-party IOC hunt.
- **Adjudicate the #028 correspondence** for the CyberAv3ngers dossier WITHOUT asserting #028 for this specific revision (Hard Rule 2). Is the advisory-line + TTP correspondence dossier-worthy as context?
- **A&D framing:** keep it structural (shared PLC attack surface), not a targeted A&D campaign, absent a named DIB victim.

## Sources

### The Record (Recorded Future News) (the-record, digraph letter: B) — 2026-07-22 ~15:18 EDT

- URL: https://therecord.media/federal-agencies-broaden-alert-on-iran-linked-ot-attacks
- Key claim: CISA/FBI/EPA broadened their April 2026 Iran-OT advisory; observed HMI/SCADA display manipulation and malicious project-file interaction against internet-facing Rockwell/Schneider/Siemens PLCs, causing disruption and financial loss; generic "Iranian regime-affiliated" attribution, no specific group named.

### Underlying government primary (not directly retrieved this cycle)

- CISA + FBI + EPA joint advisory (revision/broadening of the April 2026 Iran-OT advisory; corpus predecessor AA26-097A), A-grade. Relayed by The Record. Direct retrieval pending.
