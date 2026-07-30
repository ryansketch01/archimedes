---
finding_id: finding-2026-07-30-0006
created_at: 2026-07-30T16:18:00-04:00
graded_by: grader
grading_run_id: afternoon-20260730-160000
grading_mode: scheduled_brief
finding_type: net_new                 # first Archimedes finding for the Operation Double Barrel Lazarus<->Gunra cluster

# Core grading (from admiralty-grading skill output)
digraph: B2
source_reliability:
  grade: B
  source_name: "The Record (Recorded Future News) — relaying an AhnLab + four-South-Korean-agency joint advisory"
  source_yaml_id: the-record
  underlying_primary:
    source_name: "AhnLab + four South Korean security & intelligence agencies (joint advisory, 'Operation Double Barrel')"
    grade: A                          # national-CERT-class joint advisory + reputable AV vendor would grade A-class
    in_hand_this_cycle: false         # advisory / AhnLab primary NOT directly retrieved this sweep
    yaml_status: not_in_source_grades  # flag for librarian: AhnLab + the SK-agency advisory are not in source-grades.yaml
  grade_rationale: >
    Anchored B on the single retrieved relay (The Record, B per source-grades.yaml). The originating primary
    is a national-CERT-class joint advisory (four SK agencies) + AhnLab — A-class in reliability — but it was
    NOT directly retrieved this cycle and neither AhnLab nor the advisory is in source-grades.yaml. Anchoring
    on the retrieved source is consistent with the corpus method (cf. finding-2026-07-30-0002).
  provisional: false
credibility:
  grade: 2
  checklist_passed:
    - probably_true_ttp_consistent            # DPRK<->ransomware entanglement is well-documented for Lazarus (prior Play/Qilin/Medusa links 2024-2025; Lazarus backdoor deployment at scale); Gunra Conti-v2 lineage is coherent
    - probably_true_no_contradicting_ab        # no A/B-grade source contradicts; AhnLab itself is the most authoritative voice on the claim and it HEDGES (see note)
    - probably_true_claims_coherent            # the technical-overlap indicators (identical filenames/args, shared priv-esc tools, shared C2, shared SSH key fingerprint, identical rename-to-random-4-char file-deletion) are internally coherent linkage evidence
  grade_1_withheld_reason: >
    Grade 1 (Confirmed) withheld on two independent grounds. (1) Single retrieved relay (The Record) of a
    single originating advisory -> no independent second evidence basis. (2) More important: AhnLab itself
    EXPLICITLY hedges — it "stopped short of definitively attributing both campaigns to the same actor,"
    classifying the finding as "a high likelihood of technical linkage" requiring continued investigation.
    Archimedes cannot grade the linkage higher than its most authoritative source states it (Hard Rule 2 /
    no-attribution-beyond-source-confidence). The graded claim is therefore the TECHNICAL-LINKAGE assertion
    as AhnLab frames it, not a merged-actor identity.
  rationale: >
    Graded claim: AhnLab + four SK agencies report overlapping technical indicators between Lazarus Group
    (#003) and the Gunra ransomware operation ("Operation Double Barrel"), assessed by AhnLab as "a high
    likelihood of technical linkage" (hedged, not definitive attribution). The overlap indicators are
    coherent and consistent with the documented DPRK-ransomware nexus; single evidence basis and source-level
    hedge -> Probably True.
corroboration:
  independent_sources:
    - the-record
  independent: false
  test_result: >
    FAILS independence. One retrieved relay (The Record) of one originating joint advisory. No second
    independent evidence basis in hand. The four-agency + AhnLab co-authorship strengthens the PRIMARY's
    authority but is a single advisory, not multiple independent bases.
first_party_precedence:
  applied: false
  queried_indices: [archimedes, defenseclaw_local]
  query_window: "-24h (grader confirmatory) + collector 15:30 pre-brief IOC/entity sweep"
  splunk_evidence: >
    Rule 8 run by grader this cycle: (index=archimedes OR index=defenseclaw_local) NOT sourcetype=archimedes:*
    over "Gunra" / "Operation Double Barrel" / Lazarus -> 0 events, both indices. Collector's 15:30 pre-brief
    sweep also 0 defender-telemetry hits. Atomic overlap indicators (C2 IPs/domains, SSH key fingerprint
    VALUE, malware hashes/filenames) were NOT provided as values in the relay layer, so no atomic hunt was
    possible. Visibility-bounded null — neither corroboration nor disconfirmation (Hard Rule 8). Re-run on
    direct retrieval of the AhnLab / SK-agency IOC appendix.
single_source_veto_applied: true
single_source_veto_note: >
  Applies — single retrieved relay of a single advisory. WEP capped at "likely." Independently reinforced by
  AhnLab's own hedge ("high likelihood of technical linkage," not definitive attribution): even a second
  independent source would not upgrade the actor-identity claim beyond what AhnLab asserts. Veto lifts on a
  second independent A/B source corroborating the overlap and on direct retrieval of the advisory.
wep_ceiling: likely

# Cluster metadata
cluster:
  topic: "AhnLab + four South Korean agencies ('Operation Double Barrel') report overlapping technical indicators between DPRK Lazarus Group and the Gunra ransomware operation: identical malware filenames + execution arguments, shared privilege-escalation tools, shared C2 servers, a shared SSH key fingerprint, and an identical file-deletion method (rename to random 4-character strings). All exploited vulnerabilities in Korean financial-security software. AhnLab assesses 'a high likelihood of technical linkage' but stops short of definitive same-actor attribution. Gunra: Conti-v2-lineage ransomware, emerged Apr 2025, >=32 victims by Mar 2026; prior DPRK ransomware links noted with Play/Qilin/Medusa (2024-2025); advisory reports Lazarus backdoored >=72 organizations in 2026."
  cluster_size: 1
  raw_signal_members:
    - raw-2026-07-30-pm-002
  attribution_claims:
    - claimed_actor: "Lazarus Group"
      nation: "North Korea (DPRK) / Reconnaissance General Bureau"
      claimed_by_sources: ["AhnLab + four South Korean security & intelligence agencies (via The Record relay)"]
      source_confidence_language: "'stopped short of definitively attributing both campaigns to the same actor'; 'a high likelihood of technical linkage'"
      roster_match: "#003 Lazarus Group"
      requires_analyst_review: true
      hard_rule_2_note: >
        The Lazarus<->Gunra linkage is EXPLICITLY HEDGED by AhnLab and MUST NOT be upgraded to a definitive
        same-actor attribution. Recorded as AhnLab's assessment, at AhnLab's stated confidence.
    - claimed_actor: "Gunra ransomware operators"
      nation: "unattributed (ransomware ecosystem; DPRK-linkage under investigation)"
      prior_dprk_ransomware_links: [Play, Qilin, Medusa]
      claimed_by_sources: ["AhnLab / SK agencies (via The Record relay)"]
      roster_match: none
      note: "Gunra is not a roster actor; recorded as ransomware-nexus context only."

# FLASH-adjacency adjudication (grader)
flash_adjacency:
  independently_warrants_flash: false
  rationale: >
    Tracked actor (#003) and an A&D-adjacent spearphishing lure, but NO active exploitation of a tracked CVE,
    NO US A&D prime named (single named defense target is a non-US Korean company), NO first-party hit, and
    the core linkage claim is source-hedged. Correctly held below-FLASH by the collector and the 12:00 sweep
    for the afternoon board.

# Inclusion eligibility (from admiralty-grading)
inclusion:
  eligible_for:
    - flash
    - daily_brief_action
    - weekly_synthesis
    - actor_profile_update

# Downstream handoff flags
analyst_review_required: true            # attribution claim present + tracked actor (#003) + source-hedged linkage worth SAT treatment; WEP likely
analyst_review_complete: true
analyst_review_run_id: analyst-20260730-164000
red_team_review_required: false          # WEP ceiling 'likely' (< very_likely); analyst reinforces cap, no upward pressure
red_team_review: null
wep_ceiling_adjusted: likely             # unchanged — ACH confirms a linkage read but brittleness + AhnLab hedge keep it at 'likely'
wep_ceiling_adjustment_reason: >
  ACH leader is H2 (technical/operational linkage between DPRK-nexus groups), which is AhnLab's own hedged
  position — NOT same-actor (H1). Sensitivity is high: the linkage rests entirely on two indicators (shared C2,
  shared SSH key fingerprint) whose atomic values were NOT retrieved. WEP stays capped at 'likely' (already the
  single-source-veto ceiling); no downgrade below, but the same-actor question is explicitly unresolved.
analysis_sections:
  sat_ach:
    ach_analysis:
      question: "What is the nature of the AhnLab/SK-agency-reported technical overlap between Lazarus Group (#003) and the Gunra ransomware operation ('Operation Double Barrel') — same actor, inter-group linkage, or coincidental reuse?"
      analyzed_at: 2026-07-30T16:40:00-04:00
      analyzed_by: analyst
      red_team_review: null
      hypotheses:
        - id: H1
          statement: "A single actor (Lazarus, #003) operates both the Lazarus intrusions and the Gunra ransomware campaign — same-actor identity."
        - id: H2
          statement: "Distinct DPRK-nexus groups are linked via deliberate tool/infrastructure hand-off or operational collaboration (Lazarus tooling/infra used by the Gunra operation) — genuine linkage, not merged identity. [AhnLab's hedged position]"
        - id: H3
          statement: "Gunra operators independently reused commodity tooling / a shared supplier that Lazarus also uses; no operational linkage. [null hypothesis]"
        - id: H4
          statement: "A non-DPRK actor deliberately mimicked Lazarus tooling to misattribute Gunra activity to DPRK — false flag."
      evidence:
        - id: E1
          description: "Identical malware filenames + execution arguments across both campaigns"
          source: raw-2026-07-30-pm-002
          digraph: B2
          weight: 2
        - id: E2
          description: "Shared privilege-escalation tools"
          source: raw-2026-07-30-pm-002
          digraph: B2
          weight: 2
        - id: E3
          description: "Shared C2 servers (atomic values NOT retrieved this cycle)"
          source: raw-2026-07-30-pm-002
          digraph: B2
          weight: 2
        - id: E4
          description: "Shared SSH key fingerprint (value NOT retrieved; Hard Rule 7 — no value stored)"
          source: raw-2026-07-30-pm-002
          digraph: B2
          weight: 2
        - id: E5
          description: "Identical anti-forensics file-deletion method (rename to random 4-char strings)"
          source: raw-2026-07-30-pm-002
          digraph: B2
          weight: 2
        - id: E6
          description: "Both campaigns hit Korean financial-security software (shared victimology)"
          source: raw-2026-07-30-pm-002
          digraph: B2
          weight: 2
        - id: E7
          description: "Gunra is Conti-v2-lineage ransomware built on LEAKED public source code (payload not unique to any actor)"
          source: raw-2026-07-30-pm-002
          digraph: B2
          weight: 2
        - id: E8
          description: "AhnLab (most authoritative voice) EXPLICITLY declines same-actor attribution; classifies as 'high likelihood of technical linkage'"
          source: raw-2026-07-30-pm-002
          digraph: B2
          weight: 2
        - id: E9
          description: "Documented prior DPRK ransomware-nexus tool/access relationships (Play/Qilin/Medusa, 2024-2025)"
          source: raw-2026-07-30-pm-002
          digraph: B2
          weight: 2
        - id: E10
          description: "First-party Splunk null over Gunra / Operation Double Barrel / Lazarus, both indices (visibility-bounded, Hard Rule 8)"
          source: splunk-negative-search
          digraph: A1
          weight: 3
      matrix:
        E1: {H1: C, H2: C, H3: N, H4: C}   # filenames/args copyable; leans shared-op but not decisive
        E2: {H1: C, H2: C, H3: C, H4: C}   # non-diagnostic — priv-esc tools often commodity
        E3: {H1: C, H2: C, H3: I, H4: I}   # DIAGNOSTIC — shared live C2 implies operator linkage; hard for pure-reuse or non-DPRK mimic
        E4: {H1: C, H2: C, H3: I, H4: I}   # DIAGNOSTIC (linchpin) — shared SSH key fingerprint implies shared operator control
        E5: {H1: C, H2: C, H3: N, H4: C}   # distinctive but copyable anti-forensics routine
        E6: {H1: C, H2: C, H3: N, H4: N}   # shared targeting; weakly supports linkage
        E7: {H1: N, H2: N, H3: C, H4: N}   # keeps H3 alive for the PAYLOAD strand — commodity leaked code
        E8: {H1: I, H2: C, H3: N, H4: N}   # source declines same-actor -> inconsistent with confident H1; consistent with H2
        E9: {H1: N, H2: C, H3: N, H4: I}   # DPRK hand-off pattern supports H2; cuts against non-DPRK false flag
        E10: {H1: N, H2: N, H3: N, H4: N}  # non-diagnostic visibility-bounded null
      inconsistency_counts:
        H1: 1     # E8 — the source's own refusal to affirm same-actor
        H2: 0
        H3: 2     # E3, E4 — shared C2 + shared SSH key hard to reconcile with 'no operational linkage'
        H4: 3     # E3, E4, E9 + requires multiple unverified assumptions (non-DPRK access to genuine Lazarus infra)
      diagnostic_evidence:
        - E3: "Shared C2 distinguishes operational linkage (H1/H2) from independent reuse (H3) and false flag (H4)"
        - E4: "Shared SSH key fingerprint is the linchpin — implies shared operator key control; strongest anti-H3/anti-H4 item"
        - E8: "AhnLab's hedge distinguishes confirmed same-actor (H1) from hedged linkage (H2) — bounds the conclusion"
        - E7: "Conti-v2 leaked-code lineage is the one item keeping H3 alive for the ransomware payload strand"
      ranking:
        - rank: 1
          hypothesis_id: H2
          rationale: "Zero inconsistencies; consistent with the diagnostic linkage evidence (E3, E4) AND with AhnLab's explicit hedge (E8) and the documented DPRK hand-off pattern (E9). This is the source's stated position — a genuine technical/operational linkage short of merged identity."
          wep: likely
        - rank: 2
          hypothesis_id: H1
          rationale: "Only 1 inconsistency (E8) and NOT diagnostically separable from H2 on current evidence — shared C2/SSH could be same-actor OR hand-off. Ranked below H2 solely because the most authoritative source declines same-actor; Hard Rule 2 forbids Archimedes hardening past AhnLab. Same-actor remains an open, unresolved possibility."
          wep: roughly_even_chance   # vs H2, for the FORM of linkage — not separable
        - rank: 3
          hypothesis_id: H3
          rationale: "Two inconsistencies (E3, E4). Survives only for the ransomware-payload strand (E7 commodity leaked code), NOT for the shared operational infrastructure. Would revive if E3/E4 turn out to be shared commodity hosting rather than operator-controlled infra (see sensitivity)."
          wep: unlikely
        - rank: 4
          hypothesis_id: H4
          rationale: "Three inconsistencies plus multiple unverified assumptions (a non-DPRK actor with access to genuine Lazarus C2 and SSH keys). Not supported."
          wep: very_unlikely
      sensitivity_analysis:
        brittleness: high
        load_bearing_evidence: [E3, E4]
        if_E3_E4_reinterpreted: >
          The entire linkage read rests on E3 (shared C2) and E4 (shared SSH key fingerprint). Their atomic
          values were NOT retrieved. If direct retrieval shows the 'shared C2' is shared bulletproof/commodity
          hosting (same VPS provider, different tenants) rather than an operator-controlled server, E3 weakens
          to N and H3 (independent reuse) revives to near-parity. Likewise if the 'shared SSH key fingerprint'
          is a hosting-provider host key or a widely-reused default rather than an operator authentication key,
          E4 collapses. The assessment is BRITTLE to the interpretation of these two indicators and cannot be
          verified without the IOC appendix.
        if_source_downgraded: >
          Single relay (The Record, B) of a single un-retrieved advisory. If The Record's relay proves to have
          overstated the advisory's linkage language, the whole cluster weakens. Single-source veto already
          caps at 'likely.'
      tripwires:
        - observation: "Direct retrieval of the AhnLab / SK-agency IOC appendix confirms operator-controlled shared C2 + shared operator SSH key"
          effect: "Firms E3/E4; lifts linkage read; rerun ACH — could narrow H1-vs-H2 gap"
        - observation: "IOC appendix shows the 'shared C2' is commodity hosting / the SSH key is a provider host-key"
          effect: "Weakens E3/E4; H3 revives; reduce linkage confidence"
        - observation: "A second independent A/B source corroborates the Lazarus<->Gunra overlap"
          effect: "Lifts single-source veto; rerun; could move linkage above 'likely' (but NOT same-actor past AhnLab's hedge)"
        - observation: "AhnLab or SK agencies later upgrade to definitive same-actor attribution"
          effect: "H1 becomes the sourced position; re-rank"
      conclusion:
        summary: >
          A genuine technical/operational linkage (H2) between Lazarus (#003) and the Gunra operation is the
          leading read: the diagnostic indicators (shared C2, shared SSH key fingerprint) are hard to reconcile
          with independent commodity reuse (H3) or a non-DPRK false flag (H4). Crucially, ACH does NOT resolve
          the FORM of linkage — same-actor (H1) vs deliberate hand-off/collaboration (H2) are not diagnostically
          separable on current evidence, and AhnLab itself declines same-actor. Per Hard Rule 2, Archimedes
          reports AhnLab's hedged linkage assessment, not a merged identity.
        wep: likely
        confidence_caveats: >
          High brittleness: the linkage rests on two un-retrieved indicators (E3, E4). Single-source veto +
          AhnLab's hedge cap this at 'likely.' The same-actor question is explicitly OPEN. Do not harden into a
          Lazarus-IS-Gunra claim (Hard Rule 2).
  sat_kac:
    kac_analysis:
      assessment_under_review: >
        "The AhnLab/SK-agency-reported technical overlap (shared filenames/args, priv-esc tools, C2, SSH key
        fingerprint, file-deletion routine) indicates a genuine operational linkage between Lazarus (#003) and
        the Gunra ransomware operation ('Operation Double Barrel')."
      analyzed_at: 2026-07-30T16:52:00-04:00
      analyzed_by: analyst
      invoking_context: "Post-ACH stress-test of the leading hypothesis (H2, technical/operational linkage) before afternoon-brief publication"
      assumptions:
        - id: A1
          statement: "The 'shared C2 servers' reflect the same operator-controlled infrastructure, not shared commodity/bulletproof hosting"
          category: technology
          stated: false
          why_must_be_true: "Shared C2 is a load-bearing diagnostic indicator (ACH E3) distinguishing linkage from independent reuse"
          when_could_be_false: "The 'shared C2' is the same VPS provider under different tenant accounts, or a shared open-proxy — no operator linkage"
          evidence_for: [raw-2026-07-30-pm-002]
          evidence_against: []
          confidence: low          # atomic values NOT retrieved
          centrality: critical
          classification: test
        - id: A2
          statement: "The 'shared SSH key fingerprint' is an operator authentication key, not a hosting-provider host key or a widely-reused default"
          category: technology
          stated: false
          why_must_be_true: "The SSH-key overlap (ACH E4) is the linkage linchpin; its meaning depends entirely on which kind of key it is"
          when_could_be_false: "The fingerprint is a provider host-key shared by co-tenants, or a default/leaked key with no operator significance"
          evidence_for: [raw-2026-07-30-pm-002]
          evidence_against: []
          confidence: low          # value NOT retrieved (Hard Rule 7 — not stored regardless)
          centrality: critical
          classification: test
        - id: A3
          statement: "Technical/tradecraft overlap implies OPERATIONAL linkage rather than independent adoption of the same tooling"
          category: TTP_patterns
          stated: true
          why_must_be_true: "This is the core inference AhnLab draws and the assessment restates"
          when_could_be_false: "Overlap is explained by commodity tooling, a shared third-party supplier, or leaked code (cf. Gunra's Conti-v2 lineage) without any operational tie"
          evidence_for: [raw-2026-07-30-pm-002]
          evidence_against: []
          confidence: medium       # supported IF A1/A2 hold — partly circular with them
          centrality: critical
          classification: qualify
        - id: A4
          statement: "Gunra's Conti-v2 leaked-code lineage does not by itself establish linkage — the payload is commodity; linkage (if any) rests on the non-payload indicators"
          category: technology
          stated: false
          why_must_be_true: "Guards against over-reading the ransomware payload as an attribution signal"
          when_could_be_false: "n/a — this is a bounding caveat that constrains, not extends, the claim"
          evidence_for: [raw-2026-07-30-pm-002]
          evidence_against: []
          confidence: high
          centrality: material
          classification: sound
        - id: A5
          statement: "The Lazarus side of the overlap is correctly attributed to Lazarus (#003) by AhnLab + four SK agencies"
          category: source_reliability
          stated: true
          why_must_be_true: "If the 'Lazarus' campaign isn't Lazarus, the linkage question is moot"
          when_could_be_false: "The SK-agency Lazarus attribution is itself mistaken — low probability given national-CERT-class + AhnLab co-authorship"
          evidence_for: [raw-2026-07-30-pm-002]
          evidence_against: []
          confidence: high
          centrality: critical
          classification: sound
        - id: A6
          statement: "The overlap is not the product of one actor mimicking the other (false flag)"
          category: actor_intent
          stated: false
          why_must_be_true: "A false flag would invert the linkage's meaning"
          when_could_be_false: "A capable actor planted Lazarus indicators — but the shared SSH key + live C2 argue strongly against this (ACH H4 = 3 inconsistencies)"
          evidence_for: [raw-2026-07-30-pm-002]
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify
        - id: A7
          statement: "AhnLab's hedge ('high likelihood of technical linkage,' not same-actor) is a genuine analytic reservation that must be preserved, not collapsed"
          category: source_reliability
          stated: true
          why_must_be_true: "Hard Rule 2 binds Archimedes to the source's stated confidence"
          when_could_be_false: "n/a — this is a discipline constraint, not an empirical claim"
          evidence_for: [raw-2026-07-30-pm-002]
          evidence_against: []
          confidence: high
          centrality: material
          classification: sound
        - id: A8
          statement: "DPRK actors continue the documented pattern of ransomware-nexus tool/access relationships (context supporting the hand-off model H2)"
          category: geopolitical_context
          stated: true
          why_must_be_true: "Underpins H2's plausibility over a pure-coincidence read"
          when_could_be_false: "The prior Play/Qilin/Medusa DPRK links were themselves overstated"
          evidence_for: [raw-2026-07-30-pm-002]
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify
      classifications_summary:
        sound: 3
        qualify: 3
        test: 2
        reject: 0
      remediation:
        status: proceed
        qualifying_caveats:
          - "The FORM of linkage is unresolved — a genuine technical/operational linkage is supported, but same-actor (Lazarus IS Gunra) is NOT established and AhnLab explicitly declines it (preserve the hedge; Hard Rule 2)."
          - "The two load-bearing indicators (shared C2, shared SSH key fingerprint) are TEST-class: their meaning depends on atomic values not retrieved this cycle. Direct retrieval of the AhnLab/SK-agency IOC appendix is the resolving test; publish at awareness level, do not harden pending it."
          - "The ransomware payload (Conti-v2 leaked code) is commodity and carries no attribution weight on its own."
        blocking_assumption: null   # Test-class assumptions flag a retrieval action but do NOT block awareness-level publication at WEP 'likely'
        blocking_detail: >
          A1/A2 are Test-class, but the finding is an awareness-level 'likely' item, not a HIGH-confidence
          attribution. Publication proceeds with the hedge preserved; the test (IOC-appendix retrieval) is a
          tripwire, not a publication gate. It WOULD be a gate if this were promoted toward 'very likely' or a
          same-actor claim.
      recommended_wep_after_test:
        if_C2_and_SSH_confirmed_operator_controlled: likely   # linkage firm; same-actor still not past AhnLab's hedge
        if_C2_SSH_prove_commodity_hosting: roughly_even_chance # linkage vs independent-reuse re-opens; reduce
        if_second_independent_source_corroborates: likely      # veto lifts but same-actor cap holds

# actor-profiler handoff
actor_profiler_handoff:
  roster_actor: "003"                    # Lazarus Group
  recommended_action: consider_dossier_update
  note: >
    'Operation Double Barrel' Lazarus<->Gunra technical-linkage + the >=72-org 2026 backdoor figure are
    candidate additions to the Lazarus (#003) dossier IF the analyst confirms handling. Preserve AhnLab's
    hedge — do NOT harden the Gunra linkage into a merged identity (Hard Rule 2).

# Lifecycle
tlp: CLEAR
published_in_briefs: [2026-07-30-afternoon]
retracted: false
retraction_brief_id: null
---

# South Korean agencies + AhnLab: Lazarus Group and Gunra ransomware share tooling and infrastructure ("Operation Double Barrel") — linkage assessed "high likelihood," not confirmed

## Summary

A joint advisory from AhnLab and four South Korean security and intelligence agencies reports overlapping technical indicators between North Korea's Lazarus Group (#003) and the Gunra ransomware operation, under the name "Operation Double Barrel." The reported overlaps — identical malware filenames and execution arguments, shared privilege-escalation tools, shared command-and-control servers, a shared SSH key fingerprint, and an identical file-deletion method (renaming files to random four-character strings) — all appear in intrusions against Korean financial-security software. AhnLab explicitly stopped short of definitive same-actor attribution, classifying the finding as "a high likelihood of technical linkage" pending further investigation. Graded B2 (single retrieved relay of one un-retrieved joint advisory); single-source veto caps the assessment at "likely," reinforced by AhnLab's own hedge. A single A&D-adjacent datum stands out: one campaign spearphished a Korean defense company using gallium-nitride (GaN) semiconductor survey lures.

## Grade rationale

- **Source B** — The Record (B) is the retrieved relay; the AhnLab + four-SK-agency joint advisory (A-class) was not directly retrieved and is not in source-grades.yaml (flagged for librarian).
- **Credibility 2** — coherent overlap indicators, consistent with the documented DPRK-ransomware nexus; but single evidence basis, and the most authoritative source (AhnLab) hedges the linkage -> cannot reach 1.
- **Single-source veto applied** — one retrieved relay of one advisory -> WEP held at "likely."

## Sources

### The Record — Recorded Future News (the-record, digraph: B)

- URL: https://therecord.media/north-korea-hackers-ransomware
- Published: 2026-07-30T10:00 EDT
- Key claim: AhnLab + four SK agencies report shared Lazarus/Gunra tooling and infrastructure ("Operation Double Barrel"), assessed as a high likelihood of technical linkage.

## Technical detail

The linkage rests on tradecraft-overlap indicators rather than a single dispositive artifact: identical malware filenames and execution arguments, the same privilege-escalation utilities, shared C2 servers, a shared SSH key fingerprint, and an identical anti-forensics file-deletion routine (rename to random four-character strings). Gunra is Conti-v2-lineage ransomware (leaked source code), emerged April 2025, and claimed at least 32 victims by March 2026; the advisory also states Lazarus installed backdoors in at least 72 organizations in 2026 across South Korean government, cryptocurrency-exchange, IT-service, healthcare, and manufacturing sectors. Atomic values (C2 IPs/domains, the SSH key fingerprint value, malware hashes/filenames) were referenced qualitatively but not provided in the relay layer — pending direct retrieval of the AhnLab / SK-agency primary. No credential values present (Hard Rule 7). Recorded at awareness level (Hard Rule 3).

## IOCs surfaced

```yaml
atomic_iocs: []                          # C2 IPs/domains, SSH key fingerprint value, hashes/filenames referenced but NOT provided in the relay layer
context_iocs:
  - type: campaign_name
    value: "Operation Double Barrel"
    context: "AhnLab / SK-agency designation for the Lazarus<->Gunra overlap campaign"
    confidence: reported
  - type: malware_family
    value: "Gunra ransomware"
    context: "Conti-v2 source-code lineage; emerged Apr 2025; >=32 victims by Mar 2026; technical overlap with Lazarus tooling"
    confidence: reported
  - type: ttp
    value: "file-deletion via rename to random 4-character strings"
    context: "shared anti-forensics method cited as a Lazarus<->Gunra technical-linkage indicator"
    confidence: reported
credential_exposure_detected: false      # 'shared SSH key fingerprint' referenced qualitatively, no value stored (Hard Rule 7)
```

## Relationship to existing findings

DPRK double-header with finding-2026-07-30-0005 (Stardust Chollima #002 / npm supply-chain) on this same board — DISTINCT findings (different actor, campaign, and originating primary); NOT merged. Extends the corpus's DPRK-ransomware-nexus tracking (prior Play/Qilin/Medusa DPRK-linkage reporting). Related as a class to Lazarus (#003) dossier tracking, pending analyst confirmation.

## A&D relevance

Sector-adjacent, non-US. The sharpest A&D datum is a single spearphishing campaign against a Korean defense company using GaN (gallium-nitride) semiconductor survey lures — GaN being a defense RF/radar-relevant material class. This is one named non-US defense-sector target within a broader Korean-financial-security-software campaign; no US A&D prime is named. The GaN-lure thread is the A&D-adjacent tripwire worth watching, not a named-prime compromise.

## Analytic notes (from analyst review)

ACH + KAC applied (run analyst-20260730-164000). The leading hypothesis is a genuine technical/operational linkage between Lazarus (#003) and Gunra (H2, zero inconsistencies) — which is exactly AhnLab's hedged position. The diagnostic evidence is narrow but pointed: shared C2 servers and a shared SSH key fingerprint are hard to reconcile with independent commodity reuse (H3, two inconsistencies) or a non-DPRK false flag (H4, three inconsistencies). The Conti-v2 leaked-code lineage is commodity and carries no attribution weight on its own.

The important negative result: ACH does not resolve the FORM of the linkage. Same-actor (H1) and deliberate hand-off/collaboration (H2) are not diagnostically separable on current evidence, and AhnLab itself declines same-actor. Per Hard Rule 2, this is reported as AhnLab's linkage assessment, not a merged Lazarus-IS-Gunra identity.

The assessment is brittle. The two load-bearing indicators (shared C2, shared SSH key fingerprint) had no atomic values in the relay layer; KAC scores both as Test-class (low confidence, critical centrality). If direct retrieval of the SK-agency IOC appendix shows the "shared C2" is commodity hosting or the SSH fingerprint is a provider host-key, the linkage read weakens materially. Single-source veto already caps this at "likely"; no change to the grade. Briefer: preserve the hedge, present linkage-not-identity, and flag IOC-appendix retrieval as the resolving test.

## Open questions for analyst

- **Linkage nature (candidate ACH).** Shared tooling/infra/SSH-key can indicate same-actor, deliberate tool hand-off/collaboration, or commodity-tool reuse. AhnLab's hedge ("high likelihood of technical linkage") should be preserved; an ACH would keep the competing explanations explicit.
- **GaN-lure significance.** Does the Korean-defense GaN-semiconductor spearphishing lure indicate A&D-directed intent, or is it one target within a finance-software-centric campaign? Bears on any future Intent scoring for #003.
- **Direct retrieval.** AhnLab / SK-agency advisory + IOC appendix not retrieved — retrieval would firm the atomic overlap indicators and could establish an independent documentary basis.
