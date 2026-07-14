---
finding_id: finding-2026-07-14-0001
created_at: 2026-07-14T08:12:00-04:00
graded_by: grader
grading_run_id: morning-20260714-080000
grading_mode: scheduled_brief

# Core grading (from admiralty-grading skill output)
digraph: A2
source_reliability:
  grade: A
  source_name: Microsoft Threat Intelligence (MSTIC) / Microsoft Security Blog
  source_yaml_id: mstic
  grade_rationale: >
    Pre-assigned A per source-grades.yaml (ratified, active). Nation-state and
    financially-motivated actor tracking backed by first-party Defender/Entra
    telemetry. Author byline: Microsoft Security Research + Microsoft Defender
    Security Research Team.
  provisional: false
credibility:
  grade: 2
  checklist_passed:
    - probably_true_ttp_consistent          # consistent with the known, real Salesloft Drift (Aug 2025) + Gainsight (Nov 2025) OAuth supply-chain compromises and vishing-driven consent abuse; the Klue June-2026 compromise is itself corpus-corroborated (Huntress via finding-2026-06-19-0003)
    - probably_true_no_contradicting_ab      # no A/B-grade source contradicts MSTIC's characterization
    - probably_true_claims_coherent          # OAuth-trust-abuse mechanism (consented malicious connected app / compromised integration secret -> API-level bulk exfil without sign-in anomaly) is internally coherent; MSTIC explicitly states this is not a Salesforce product vulnerability
  grade_1_withheld_reason: >
    Grade 1 withheld. The single primary is MSTIC. The Klue-June-2026 incident
    occurrence is independently corroborated in-corpus (Huntress-attributed via
    finding-2026-06-19-0003, roster actor Icarus #025), but that corroborates the
    INCIDENT, not MSTIC's actor labeling (Storm-3138) or its clustering of the
    broader mid-2025->mid-2026 campaign under ShinyHunters-associated tradecraft.
    Those framings rest on the MSTIC primary alone. Headline credibility = 2.
  rationale: >
    MSTIC publishes defensive guidance characterizing a mid-2025->mid-2026 set of
    campaigns abusing trusted OAuth relationships against SaaS applications
    (primarily Salesforce) for unauthorized access, data exfiltration, and
    persistence, which it attributes to "overlapping tradecraft commonly
    associated with ShinyHunters" (hedge preserved verbatim). MSTIC names
    Storm-3138 as the actor that in June 2026 gained access to the market-
    intelligence platform Klue and used credentials to query and exfiltrate data
    from Salesforce customer instances. Three intrusion paths: vishing-driven
    OAuth consent abuse (fake "Salesforce Data Loader" connected app), SaaS
    supply-chain compromise of trusted integrations (Salesloft Drift Aug 2025,
    Gainsight Nov 2025), and guest-access misconfiguration. Named victim
    industries: retail, education, manufacturing (no A&D prime). Coherent,
    consistent, no A/B contradiction -> Probably True.
corroboration:
  independent_sources:
    - mstic
  independent: false
  independence_test_result: >
    Single primary (MSTIC) for the campaign characterization and both actor
    labels. The Klue-June-2026 incident occurrence is separately corroborated by
    Huntress (relayed via finding-2026-06-19-0003), but Huntress and MSTIC apply
    DIFFERENT labels (Icarus vs Storm-3138) to the same incident and MSTIC's
    broader campaign clustering / Storm-3138 attribution stand on MSTIC alone.
    Corroboration of the incident is not corroboration of the attribution.
first_party_precedence:
  applied: false
  splunk_evidence: null
  splunk_note: >
    Splunk queried (index=archimedes OR index=defenseclaw_local, -30d) for
    Storm-3138 / Klue / Salesloft / Gainsight / ShinyHunters. Returns ONLY
    Archimedes' own operational telemetry (flash_evaluation / git_committed /
    finding_promoted meta-events that mention these terms as content, incl. the
    2026-06-19 Klue/Icarus promotion). ZERO defenseclaw_local target detections.
    Hard Rule 8: silent first-party on a visibility-bounded single-user dev host
    does not disconfirm; no first-party contradiction.
single_source_veto_applied: true
single_source_veto_note: >
  Veto applies to the campaign-clustering and Storm-3138 attribution claims
  (MSTIC single primary). WEP capped at "likely" regardless of A letter grade.
  Veto would lift on independent second-vendor corroboration of the Storm-3138
  label / campaign clustering (not merely of the underlying incidents).
wep_ceiling: likely

# Inclusion eligibility (from admiralty-grading)
inclusion:
  eligible_for:
    - daily_brief_monitoring        # A-grade defensive guidance + attribution development on a tracked incident (Icarus #025); no A&D prime named -> monitoring tier
    - weekly_synthesis
    - actor_profile_update          # directly bears on Icarus #025 SAT-KAC A1 + SAT-ACH H1/H3 (route to actor-profiler)
  not_eligible_for:
    - flash                         # not a FLASH trigger: no exploited critical CVE, no zero-day, no tracked-actor-attribution FLASH threshold event (this is defensive guidance on an ongoing-but-known campaign set), no A&D-prime victim. Correctly non-FLASH.
    - daily_brief_action            # A2 grade-eligible, but substance is monitoring: defensive guidance, no named A&D victim, A&D relevance structural/indirect

# Cluster metadata
cluster:
  topic: "MSTIC ShinyHunters-tradecraft SaaS OAuth-abuse campaign set (mid-2025 -> mid-2026, primarily Salesforce); MSTIC names Storm-3138 for the June-2026 Klue compromise -> Salesforce customer-instance exfil. Same underlying incident Archimedes tracks as Icarus (#025) via Huntress. Vishing-consent-abuse + Salesloft Drift (Aug 2025) / Gainsight (Nov 2025) integration compromise + guest-access misconfig. Not a Salesforce product vuln (MSTIC explicit). No atomic IOCs."
  cluster_size: 1
  raw_signal_members:
    - raw-2026-07-14-am-001
  attribution_claims:
    - claimed_actor: "Storm-3138 (Microsoft label)"
      claimed_by_sources: [mstic]
      source_confidence: "Named directly as the actor that accessed Klue (June 2026) and used credentials against Salesforce customer instances. No explicit confidence qualifier attached by MSTIC to the Storm-3138 label."
      requires_analyst_review: true
      hard_rule_2_note: >
        Grader originates NO merge. Recorded strictly as what MSTIC says. Same
        underlying Klue-June-2026 incident that Huntress attributed to Icarus
        (roster #025). Storm-3138 (Microsoft) and Icarus (Huntress) are two vendor
        labels on one incident; the actor-profiler adjudicates the relationship.
        MSTIC's Storm-3138 label does NOT by itself resolve the Icarus dossier's
        open question of whether Icarus is a distinct actor. ShinyHunters and
        UNC6395 cross-walk explicitly NOT originated here.
    - claimed_actor: "ShinyHunters (tradecraft-overlap cluster)"
      claimed_by_sources: [mstic]
      source_confidence: "Hedged: 'overlapping tradecraft commonly associated with ShinyHunters' — tradecraft overlap, not definitive actor identity. Hedge preserved verbatim."
      requires_analyst_review: true
      hard_rule_2_note: >
        ShinyHunters is NOT a roster actor. No roster entry originated from this
        relay. Recorded as MSTIC's hedged clustering language only.

# Downstream handoff flags
analyst_review_required: true
analyst_review_note: >
  Flagged for two reasons: (1) WEP "likely"; (2) two vendor attribution labels
  (Storm-3138, ShinyHunters-tradecraft) present that bear directly on roster
  actor Icarus #025. Analyst focus: whether MSTIC's Storm-3138 naming moves the
  Icarus SAT-KAC assumption A1 ("Icarus is a distinct actor" vs "Huntress
  tracking unattributed activity under a label") or the SAT-ACH H1/H3 hypotheses
  (incl. the UNC6395-affiliate/splinter hypothesis). Do NOT originate a merge or
  a novel attribution — assess and record what the sources claim. Also route to
  actor-profiler for an Icarus dossier data-point update (not a re-score).
red_team_review_required: false        # headline WEP "likely" < "very likely" — red-team not mandatory
red_team_review: null

# Analyst review (analyst subagent)
analyst_review_complete: true
analyst_review_run_id: analyst-20260714-081500
analysis_sections:
  sat_ach:
    ach_analysis:
      question: >
        What is the identity relationship among the vendor labels applied to the
        June-2026 Klue -> Salesforce OAuth-token-abuse activity: MSTIC's Storm-3138,
        Huntress's Icarus (roster #025), and MSTIC's hedged "ShinyHunters-associated
        tradecraft" cluster? This ACH pressure-tests whether the sources' labels can
        be distinguished — it does NOT originate an attribution (Hard Rule 2).
      analyzed_at: 2026-07-14T08:15:00-04:00
      analyzed_by: analyst
      red_team_review: null
      hard_rule_2_boundary: >
        This ACH ranks the RELATIONSHIP hypotheses among labels that CITED SOURCES
        already applied. It does not attribute the incident to any actor. MSTIC
        attributes the Klue access to Storm-3138; Huntress attributes the same
        incident to Icarus; MSTIC clusters the broader campaign under hedged
        ShinyHunters-tradecraft language. No cited source asserts Storm-3138 == Icarus
        or Storm-3138 == ShinyHunters as an identity. Whatever this matrix surfaces,
        the merge cannot be originated by Archimedes and is reported as source-labels
        only. This is a "false-flag hypothesis is not operative" case: the uncertainty
        is cross-vendor labeling, not adversary deception, so no false-flag hypothesis
        is included (it would not be diagnostic here).
      hypotheses:
        - id: H1
          statement: >
            Storm-3138 is a distinct actor cluster that Microsoft tracks under its own
            (developing "Storm-####") label — neither confirmed identical to Icarus nor
            confirmed within the ShinyHunters/UNC6395 lineage. A third vendor label on
            overlapping-tradecraft activity.
        - id: H2
          statement: >
            Storm-3138 is within the ShinyHunters/UNC6395 lineage as a matter of ACTOR
            IDENTITY (reading MSTIC's tradecraft-clustering language as an identity claim).
        - id: H3
          statement: >
            Storm-3138 and Icarus (Huntress) are the same actor/activity — two vendor
            labels on the one June-2026 Klue compromise (the "merge" hypothesis).
        - id: H4
          statement: >
            Null — the labels reflect independent vendor tracking of overlapping-but-
            distinct OAuth-abuse operators in a shared crimeware ecosystem; there is no
            single unifying actor behind the mid-2025 -> mid-2026 campaign set.
        - id: H5
          statement: >
            Composite — Storm-3138 is a ShinyHunters-ecosystem affiliate/splinter that
            conducted the Klue operation (thus approximately == Icarus for that incident)
            AND sits within the ShinyHunters tradecraft lineage.
      evidence:
        - id: E1
          description: "MSTIC (A) names Storm-3138 as the actor that accessed Klue (June 2026) and used credentials against Salesforce customer instances"
          source: mstic
          digraph: A2
          weight: 3
        - id: E2
          description: "MSTIC clusters the broad mid-2025->mid-2026 campaign under 'overlapping tradecraft commonly associated with ShinyHunters' — HEDGED, tradecraft-level, explicitly not a definitive identity claim (hedge preserved verbatim)"
          source: mstic
          digraph: A2
          weight: 3
        - id: E3
          description: "Huntress (via finding-2026-06-19-0003) attributes the SAME Klue June-2026 incident to Icarus ('Mr Brean' persona), single-IR-vendor"
          source: finding-2026-06-19-0003
          digraph: B2
          weight: 2
        - id: E4
          description: "MSTIC asserts NO identity merge — it names Storm-3138 AND references ShinyHunters-tradecraft but does not state Storm-3138 == ShinyHunters/UNC6395/Icarus despite the opportunity (evidence of absence within an A-grade report)"
          source: mstic
          digraph: A2
          weight: 3
        - id: E5
          description: "Microsoft 'Storm-####' designation denotes a distinct cluster-in-development, not a graduated/named actor or a confirmed sub-identity of one — analyst taxonomy inference, ungraded"
          source: analyst-inference-microsoft-taxonomy
          digraph: null
          weight: 0.5
        - id: E6
          description: "Same incident particulars: both Storm-3138 (MSTIC) and Icarus (Huntress) describe the identical Klue June-2026 compromise -> OAuth-token abuse -> downstream Salesforce customer-instance exfil"
          source: mstic + finding-2026-06-19-0003
          digraph: A2
          weight: 3
        - id: E7
          description: "Temporal scope: MSTIC attributes Storm-3138 specifically to the June-2026 Klue slice (not the whole campaign); Icarus per Huntress emerged 2026-04-28 with a single Klue campaign — the two labels' scopes coincide (June-2026 Klue), while the broader Salesloft-Aug-2025 / Gainsight-Nov-2025 activity is clustered separately under ShinyHunters-tradecraft"
          source: mstic + finding-2026-06-19-0003
          digraph: A2
          weight: 3
        - id: E8
          description: "No first-party Splunk detection of Storm-3138 / Klue / Salesforce activity in the target environment (visibility-bounded null; Hard Rule 8 — does not disconfirm)"
          source: splunk-negative-search
          digraph: null
          weight: 0.5
      matrix:
        E1: {H1: C, H2: C, H3: C, H4: C, H5: C}   # naming an actor for Klue is consistent with every relationship hypothesis — non-diagnostic
        E2: {H1: C, H2: I, H3: N, H4: C, H5: C}   # the HEDGE ('commonly associated with') contradicts a DEFINITIVE ShinyHunters-identity reading (H2)
        E3: {H1: C, H2: N, H3: C, H4: C, H5: C}   # Huntress calling the same incident Icarus — weakly consistent with both distinct-label and merge readings
        E4: {H1: C, H2: I, H3: N, H4: C, H5: N}   # MSTIC's non-merge / hedge is inconsistent with a confirmed lineage identity (H2)
        E5: {H1: C, H2: I, H3: N, H4: C, H5: C}   # a 'Storm-####' developing designation weakly argues against a settled ShinyHunters-lineage identity (H2); ungraded inference
        E6: {H1: N, H2: N, H3: C, H4: I, H5: C}   # SAME incident -> single operator; contradicts the null 'no unifying actor' (H4); supports merge/composite (H3/H5)
        E7: {H1: C, H2: N, H3: C, H4: N, H5: C}   # coincident June-2026 scope of both labels — weakly supports H1/H3/H5, non-diagnostic against H2
        E8: {H1: N, H2: N, H3: N, H4: N, H5: N}   # first-party null — non-diagnostic
      inconsistency_counts:
        H1: 0
        H2: 3
        H3: 0
        H4: 1
        H5: 0
      diagnostic_evidence:
        - E2: "The verbatim hedge distinguishes a tradecraft-overlap reading (H1/H4/H5) from a DEFINITIVE ShinyHunters-identity claim (H2). Most load-bearing row."
        - E4: "MSTIC's absence of a merge claim, within an A-grade report that had the opportunity to make one, weakens the definitive-lineage hypothesis (H2)."
        - E6: "Same-incident particulars distinguish a single-operator reading (H3/H5) from the null 'independent unrelated operators' (H4)."
      ranking:
        - rank: 1
          hypothesis_id: H1
          rationale: >
            Zero inconsistencies. Microsoft tracks Storm-3138 under its own developing
            designation; the ShinyHunters reference is hedged tradecraft, not identity.
            Distinct-cluster is the reading most faithful to what MSTIC actually SAYS.
          wep: likely
          tied_with: [H3, H5]
        - rank: 1
          hypothesis_id: H3
          rationale: >
            Zero inconsistencies. Same-incident particulars (E6) and coincident June-2026
            scope (E7) are fully consistent with Storm-3138 and Icarus being one actor
            under two vendor labels. CANNOT be distinguished from H1 on current evidence —
            and, decisively, NO cited source asserts this merge. Consistent-with is not
            established, and is not sourced.
          wep: likely
          tied_with: [H1, H5]
        - rank: 1
          hypothesis_id: H5
          rationale: >
            Zero inconsistencies. A ShinyHunters-ecosystem affiliate that ran the Klue op
            fits both the tradecraft-overlap and same-incident evidence. Also not
            distinguishable from H1/H3, and also unsourced as an identity claim.
          wep: likely
          tied_with: [H1, H3]
        - rank: 4
          hypothesis_id: H4
          rationale: >
            One inconsistency (E6): both vendors describe the identical Klue incident, which
            contradicts a 'no single unifying actor' reading for THAT incident. (The broader
            campaign set may still be multi-actor — the null survives for the wider cluster,
            not the Klue slice.)
          wep: unlikely
        - rank: 5
          hypothesis_id: H2
          rationale: >
            Three inconsistencies (E2, E4, E5). MSTIC's language is explicitly hedged to
            tradecraft overlap; a DEFINITIVE ShinyHunters actor-IDENTITY claim is NOT what the
            source says. Tradecraft overlap is real and sourced; identity is not.
          wep: very_unlikely
      sensitivity_analysis:
        brittleness: high_among_top_three_by_design
        load_bearing_evidence: [E2, E4, E6]
        note_on_brittleness: >
          The tie among H1/H3/H5 is not a defect to be resolved by forcing a winner — it
          is the analytically correct output and the exact reason Hard Rule 2 binds here.
          The evidence is CONSISTENT with a merge (H3) or an affiliate composite (H5) but
          does not ESTABLISH either, and no cited source asserts either. Declining to
          originate the merge is the robust move; it removes the brittleness by refusing to
          convert an undetermined tie into an attribution.
        if_E2_reinterpreted: >
          If MSTIC's ShinyHunters language were actually a definitive identity claim (not a
          hedge), H2 would rise from last to contention and Archimedes would then hold a
          SOURCED lineage attribution. But the hedge is preserved verbatim in the finding —
          E2 is well-grounded. Guard the briefer against paraphrasing the hedge away.
        if_E6_wrong_two_klue_events: >
          If there were two separate Klue compromises (there is only one documented), the
          parallel-label framing collapses. Very low probability — Salesforce disabled the
          single Klue Battlecards integration; one event.
      tripwires:
        - observation: "A second IR vendor independently corroborates the Storm-3138 label OR MSTIC/Huntress primary explicitly asserts Storm-3138 == Icarus"
          effect: "Lifts the single-source veto and could collapse the H1/H3 tie into a SOURCED merge — rerun ACH; route to actor-profiler for an Icarus dossier resolution (not a rescore off one relay)."
        - observation: "MSTIC graduates Storm-3138 to a named-actor designation or explicitly maps it into the ShinyHunters/UNC6395 taxonomy"
          effect: "Resolves H1 vs H2 — rerun ACH with the graduated designation."
        - observation: "Huntress primary publication is retrieved and states whether 'Icarus' is a distinct-actor attribution vs an unattributed-activity label"
          effect: "Resolves the standing Icarus dossier KAC-A1 test; may distinguish H1 from H3."
      conclusion:
        summary: >
          MSTIC's Storm-3138 label is most faithfully read as a distinct Microsoft-tracked
          cluster (H1) whose tradecraft OVERLAPS the ShinyHunters pattern (hedged) — a
          definitive ShinyHunters actor-IDENTITY reading (H2) is the least supported, with
          three inconsistencies, because MSTIC explicitly hedged. Critically, the merge
          hypotheses H3 (Storm-3138 == Icarus) and H5 (ShinyHunters-affiliate composite) sit
          TIED with H1 at zero inconsistencies: the evidence is fully consistent with them but
          the matrix cannot distinguish them, and — decisively — NO cited source asserts the
          Storm-3138 <-> Icarus <-> ShinyHunters identity. Per Hard Rule 2, Archimedes
          originates no merge. The correct record is two vendor labels on one incident:
          Storm-3138 (MSTIC) and Icarus (Huntress), with MSTIC's ShinyHunters reference held
          as hedged tradecraft overlap, not identity. This does NOT resolve the standing
          Icarus #025 distinctness question; a second vendor applying its own label is not
          resolution.
        wep: likely
        wep_change_from_grader: none
        confidence_caveats: >
          Attribution is single-source-veto-capped at 'likely' on the Storm-3138 label and the
          campaign clustering (MSTIC sole primary). The H1/H3/H5 tie means the briefer must NOT
          imply Storm-3138 and Icarus are confirmed the same actor. Present as parallel vendor
          labels; present the ShinyHunters link as hedged tradecraft, not identity.
  sat_kac:
    kac_analysis:
      assessment_under_review: >
        "MSTIC's naming of Storm-3138 for the June-2026 Klue compromise is a cross-vendor
        labeling data point that Archimedes records as a SECOND vendor label on the incident
        it tracks as Icarus (#025) — it does not resolve the Icarus distinctness question and
        Archimedes originates no Storm-3138 <-> Icarus <-> ShinyHunters merge."
      analyzed_at: 2026-07-14T08:20:00-04:00
      analyzed_by: analyst
      invoking_context: >
        Grader_handoff. WEP 'likely'; two vendor attribution labels present bearing on roster
        actor Icarus #025. KAC stress-tests the leading ACH reading (H1 distinct-cluster / the
        no-merge posture) and guards the briefer and actor-profiler against over-reading.
      assumptions:
        - id: A1
          statement: "MSTIC's Storm-3138 and Huntress's Icarus refer to the same underlying June-2026 Klue activity"
          category: semantic
          stated: true
          why_must_be_true: "The 'two labels on one incident' framing depends on both describing the same event"
          when_could_be_false: "If MSTIC's Storm-3138 activity is a different Salesforce-instance intrusion that merely resembles the Klue op"
          evidence_for: [mstic, finding-2026-06-19-0003]
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify
        - id: A2
          statement: "MSTIC's 'overlapping tradecraft commonly associated with ShinyHunters' is a tradecraft-level clustering, NOT a definitive actor-identity claim"
          category: source_reliability
          stated: true
          why_must_be_true: "The no-merge posture and the H2-disfavored ACH result both rest on reading the hedge as tradecraft, not identity"
          when_could_be_false: "If MSTIC intended the phrase as a firm lineage attribution (the hedge would then be an identity claim)"
          evidence_for: [mstic]
          evidence_against: []
          confidence: high
          centrality: critical
          classification: sound
        - id: A3
          statement: "A second A-grade vendor applying its own label (Storm-3138) does not by itself resolve the Icarus #025 distinctness question"
          category: source_reliability
          stated: true
          why_must_be_true: "The finding declines to treat MSTIC's label as resolution of the dossier's standing KAC-A1 open question"
          when_could_be_false: "If MSTIC's label were accompanied by an explicit cross-vendor reconciliation (it is not)"
          evidence_for: [mstic]
          evidence_against: []
          confidence: high
          centrality: material
          classification: sound
        - id: A4
          statement: "Microsoft's 'Storm-####' designation denotes a distinct developing cluster, not a confirmed sub-identity of a named actor"
          category: semantic
          stated: false
          why_must_be_true: "Supports the ACH H1 (distinct-cluster) reading and the H2-disfavored result"
          when_could_be_false: "If Microsoft uses Storm-#### transitionally for activity it already privately maps to ShinyHunters/UNC6395"
          evidence_for: [analyst-inference-microsoft-taxonomy]
          evidence_against: []
          confidence: low
          centrality: material
          classification: qualify
        - id: A5
          statement: "There is ONE Klue June-2026 compromise, not two — Salesforce disabled the single Klue Battlecards integration"
          category: technology
          stated: false
          why_must_be_true: "The parallel-label framing collapses if MSTIC and Huntress describe different Klue events"
          when_could_be_false: "If a second, distinct Klue-integration intrusion occurred and the two vendors are describing different incidents"
          evidence_for: [finding-2026-06-19-0003, mstic]
          evidence_against: []
          confidence: high
          centrality: critical
          classification: sound
        - id: A6
          statement: "No retrieved/relayed source asserts the Storm-3138 <-> Icarus identity — because none does, not because the assertion was missed"
          category: source_reliability
          stated: false
          why_must_be_true: "Hard Rule 2 compliance depends on there being no sourced merge to report"
          when_could_be_false: "Huntress's primary publication (NOT retrieved) could contain reconciling language; MSTIC blog is held but Huntress primary is not"
          evidence_for: [mstic]
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify
        - id: A7
          statement: "A&D relevance is structural/indirect — no A&D prime is named among MSTIC's victim industries (retail, education, manufacturing)"
          category: intent
          stated: true
          why_must_be_true: "Guards the monitoring-tier framing; prevents briefing this as A&D-specific targeting"
          when_could_be_false: "If a later MSTIC/second-vendor report names an A&D/DIB victim in the campaign set"
          evidence_for: [mstic]
          evidence_against: []
          confidence: high
          centrality: material
          classification: qualify
      classifications_summary:
        sound: 3
        qualify: 4
        test: 0
        reject: 0
      remediation:
        status: proceed
        blocking_assumption: null
        blocking_detail: null
        qualifying_caveats:
          - "Present Storm-3138 (MSTIC) and Icarus (Huntress) as TWO vendor labels on the one Klue June-2026 incident. Do NOT state or imply they are confirmed the same actor (ACH H1/H3/H5 tie; no source asserts the merge). (A1, A6)"
          - "MSTIC's ShinyHunters reference is HEDGED tradecraft overlap ('commonly associated with'), not an identity claim. Do not paraphrase the hedge into a lineage attribution. (A2)"
          - "A second A-grade vendor label does NOT resolve the Icarus #025 distinctness question. The dossier's standing KAC-A1 (is 'Icarus' a distinct-actor attribution or an unattributed-activity label?) remains open pending the Huntress primary. (A3, A6)"
          - "Attribution content is single-source-veto-capped at 'likely' (MSTIC sole primary for the Storm-3138 label and the campaign clustering). (grading)"
          - "A&D relevance is structural/indirect only — no A&D prime named. Brief as the portable OAuth-consent-abuse + trusted-integration-compromise exposure any large Salesforce-ecosystem ITAR enterprise shares. (A7)"
        next_action: >
          Proceed to brief at monitoring tier. Route to actor-profiler for an Icarus #025
          dossier DATA-POINT update (external-labeling / cross-vendor tracking section: add
          'Microsoft labels the same incident Storm-3138') — NOT a rescore and NOT a merge.
          The one genuinely-unresolved item (Huntress primary language, A6) is the dossier's
          standing tripwire, not a blocker for this monitoring-tier inclusion.
      recommended_wep_after_test:
        storm_3138_label: likely
        campaign_clustering: likely
        note: >
          No WEP change from KAC. The interrogation constrains how the finding is FRAMED
          (two parallel labels, hedged tradecraft, structural A&D relevance) and does not
          alter the graded confidence. No blocking Test — inclusion is legitimate at
          monitoring tier.

# Actor-profiler handoff
actor_profiler_handoff:
  proposed: true
  actor_id: "025"
  actor_name: Icarus
  reason: >
    A-grade (MSTIC) same-incident attribution/label development on the Klue
    June-2026 compromise (Icarus #025's originating event). New data point for
    the standing SAT-KAC A1 and SAT-ACH H1/H3 open questions. Update the dossier's
    external-labeling / cross-vendor tracking section; do NOT re-score off a single
    new relay, and do NOT cross-walk Storm-3138 <-> Icarus <-> ShinyHunters.

# Lifecycle
tlp: CLEAR
published_in_briefs: [2026-07-14-morning]
retracted: false
retraction_brief_id: null
---

# MSTIC attributes a mid-2025->mid-2026 Salesforce OAuth-abuse campaign to ShinyHunters-associated tradecraft and names Storm-3138 for the June-2026 Klue compromise — the same incident Archimedes tracks as Icarus (#025)

## Summary

Microsoft Threat Intelligence published defensive guidance characterizing a set
of campaigns, spanning mid-2025 through mid-2026, that abuse trusted OAuth
relationships against SaaS applications — primarily Salesforce — for
unauthorized access, bulk data exfiltration, and persistence. MSTIC attributes
the activity to "overlapping tradecraft commonly associated with ShinyHunters"
(a hedged, tradecraft-level clustering, not a definitive identity) and names
Storm-3138 as the actor that in June 2026 compromised the market-intelligence
platform Klue and used credentials to query and exfiltrate data from Salesforce
customer instances. That Klue June-2026 incident is the originating event
Archimedes already tracks as roster actor Icarus (#025), attributed by Huntress.
Storm-3138 (Microsoft) and Icarus (Huntress) are two vendor labels on one
incident; Archimedes originates no merge. Named victim industries are retail,
education, and manufacturing — no aerospace-defense prime — so A&D relevance is
structural/indirect (any large ITAR enterprise running Salesforce plus
OAuth-connected third-party integrations shares the exposure surface).

## Sources

### Microsoft Threat Intelligence / MSTIC (mstic, digraph A) — sole primary

- URL: https://www.microsoft.com/en-us/security/blog/2026/07/13/defending-saas-based-applications-against-shinyhunters-oauth-abuse/
- Published: 2026-07-13T18:02:41-04:00
- Key claim: OAuth-trust-abuse campaign set against Salesforce SaaS (mid-2025 ->
  mid-2026), clustered under ShinyHunters-associated tradecraft; Storm-3138 named
  for the June-2026 Klue compromise and subsequent Salesforce customer-instance
  exfiltration. MSTIC states explicitly this is NOT a Salesforce product
  vulnerability.

### Corroborating context (incident occurrence only, not MSTIC's attribution)

- finding-2026-06-19-0003 — Huntress-attributed Klue/Salesforce supply-chain
  compromise, promoted B2, established roster actor Icarus (#025). Corroborates
  that the Klue June-2026 compromise occurred; does NOT corroborate the
  Storm-3138 label or MSTIC's broader campaign clustering.

## Technical detail

Three intrusion paths, all OAuth-trust abuse (per MSTIC):

1. **Vishing-driven OAuth consent abuse (from mid-2025):** actors impersonate IT
   support and socially engineer employees into authorizing an attacker-
   controlled connected app disguised as a legitimate "Salesforce Data Loader"
   tool; the consented app then performs API calls (enumeration, persistent CRM
   access, possible lateral movement via discovered credentials).
2. **SaaS supply-chain compromise of trusted integrations:** Aug 2025 compromised
   Salesloft Drift credentials yielded downstream OAuth connection secrets usable
   across multiple customer Salesforce instances; Nov 2025 activity targeted
   Gainsight-published Salesforce-integrated apps for persistent API access.
   Activity is often indistinguishable from legitimate integration behavior
   (bulk queries + mass exfil of account/contact/case data without sign-in
   anomalies).
3. **Guest-access misconfiguration used for exfiltration.**

Mitigation framing (per MSTIC): monitor OAuth-connected apps, validate
third-party integrations, review guest access, enable Salesforce event
monitoring. Microsoft states it worked with Salesforce to add near-real-time
Defender for Cloud Apps detection with connected-application attribution.

## IOCs surfaced

None. The published body is defensive-guidance shaped, not an indicator drop —
no IP / domain / hash / URL indicators. Storm-3138, ShinyHunters, Salesloft
Drift, Gainsight, and Klue are actor and vendor/product names, not IOCs.

## Relationship to existing findings

Directly related to **finding-2026-06-19-0003** (Huntress Klue/Salesforce
supply-chain compromise; roster actor Icarus #025). This finding is a
same-incident attribution/label development: MSTIC labels the Klue June-2026
activity Storm-3138 and clusters the broader campaign under ShinyHunters-
associated tradecraft, where Huntress labeled the same incident Icarus. Not a
continuation of a new campaign — a cross-vendor labeling data point on a tracked
incident.

## Open questions for analyst

- **Does MSTIC's Storm-3138 naming move the Icarus SAT-KAC A1 assumption?** The
  Icarus dossier's standing open question — "Icarus is a distinct actor" vs.
  "Huntress tracking unattributed activity under a label" — is now touched by a
  second A-grade vendor applying its own label (Storm-3138) to the same incident.
  A second vendor label does not by itself resolve distinctness. Assess; do not
  originate a merge.
- **UNC6395 / ShinyHunters cross-walk remains NOT originated.** The Icarus roster
  note explicitly declined a ShinyHunters/UNC6395 cross-walk; MSTIC's hedged
  ShinyHunters-tradecraft clustering does not resolve it. Hard Rule 2 binding.
- **A&D exposure is structural, not victim-anchored.** No A&D prime named; do not
  brief as A&D-specific targeting. The portable risk is the Salesloft/Gainsight-
  class integration-compromise and OAuth-consent-abuse surface any large ITAR
  enterprise running Salesforce shares.

## Analytic notes (from analyst review)

ACH and KAC both run. The ACH ranks a distinct Microsoft-tracked cluster (H1) at
zero inconsistencies — but so are H3 (Storm-3138 == Icarus) and H5 (ShinyHunters-
affiliate composite). That three-way tie is not a failure to resolve; it is the
answer. The evidence is fully consistent with a merge yet cannot establish one, and
no cited source asserts the Storm-3138 <-> Icarus <-> ShinyHunters identity. Hard
Rule 2 binds: Archimedes records two vendor labels on one Klue incident and
originates nothing.

The strongest counter-move is against the reading most likely to leak into a brief —
that MSTIC "linked" Storm-3138 to ShinyHunters. It did not. The language is hedged
tradecraft overlap ("commonly associated with"), and a definitive-identity reading
(H2) is the *least* supported hypothesis, with three inconsistencies. The load-bearing
assumption is A2 (MSTIC's hedge is tradecraft, not identity) — high confidence because
the hedge is preserved verbatim; if a briefer paraphrases it away, the finding would
falsely appear to carry a sourced lineage attribution.

No WEP change: single-source veto holds it at "likely." Briefer must present
Storm-3138 and Icarus as parallel labels, not a confirmed same actor, and hold the
ShinyHunters tie as hedged tradecraft. This does not resolve the Icarus #025
distinctness question — a second vendor label is not resolution. Route to
actor-profiler as a dossier data-point (add "Microsoft labels this Storm-3138"), not
a rescore and not a merge.
