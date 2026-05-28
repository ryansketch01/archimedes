---
finding_id: finding-2026-05-28-0009-the-record-gchq-keast-butler-russia-daily-hybrid-uk-seabed-to-cyberspace-subsea-cables
created_at: 2026-05-28T16:17:00-04:00
graded_by: grader
grading_run_id: afternoon-20260528-160000
grading_mode: scheduled_brief
test: false

# Core grading
digraph: B2
source_reliability:
  grade: B
  source_name: "The Record (Recorded Future News) — Alexander Martin relaying GCHQ Director Anne Keast-Butler official briefing"
  source_yaml_id: the-record
  grade_rationale: >
    The Record pre-assigned B per source-grades.yaml (established
    quality journalism, well-sourced). Underlying speaker is Anne
    Keast-Butler, Director of GCHQ — UK government official-position
    A-grade-equivalent on her own agency's threat assessments.
    Single relay this sweep; UK outlets (BBC / FT / Reuters / Sky)
    likely also covered the briefing but were not pivoted to.
    Effective single-B-grade-relay of an A-grade-equivalent underlying
    speaker.
  provisional: false
credibility:
  grade: 2
  checklist_passed:
    - probably_true_ttp_consistent_with_corpus_baseline_russia_hybrid_pattern_subsea_cable_targeting_recurring_sandworm_canonical_targeting
    - probably_true_no_contradicting_a_b_grade_source
    - probably_true_technical_claims_internally_coherent_subsea_cable_energy_pipeline_supply_chain_corporate_network_targeting_categories_well_documented
  rationale: >
    Keast-Butler's framing is at the UK-government-position level and
    consistent with corpus-baseline Russia-hybrid-targeting patterns
    that Western intelligence agencies have publicly tracked for years.
    Subsea cable + energy pipeline targeting is a recurring corpus-
    tracked pattern (Sandworm canonical per roster #007; APT28 / APT29
    adjacent at roster #006 / #009). Keast-Butler does NOT attribute
    to specific GRU / SVR / FSB units — frames at state-level "Kremlin"
    shorthand. Per Hard Rule 2, grader does NOT upgrade to unit-level
    attribution. Technical claim coherence is procedurally satisfied.
    No contradicting source. Single-B-grade-relay of an A-grade-
    equivalent speaker yields credibility 2 (Probably True); cannot
    advance to 1 (Confirmed) absent independent second-relay this
    sweep window.
corroboration:
  independent_sources:
    - the-record
    - gchq-official-speaker-anne-keast-butler
  independent: false
  test_passed: >
    The Record is sole relay this sweep. Underlying speaker is a single
    primary (GCHQ Director). UK outlets likely covered the briefing
    but not pivoted to in this sweep window. Independence test fails
    on relay-layer count.
first_party_precedence:
  applied: false
  splunk_evidence: null
  rationale: "No IOCs published; state-level briefing has no technical artifacts to query."
single_source_veto_applied: true
wep_ceiling: likely

# Cluster metadata
cluster:
  topic: "GCHQ Director Anne Keast-Butler official briefing — Russia conducting daily hybrid attacks on UK 'from seabed to cyberspace,' targeting critical infrastructure, democratic processes, supply chains, public trust; Russian submarine operations near critical seabed infrastructure"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-05-28-pm-006
  attribution_claims:
    - claimed_actor: "Russia (Kremlin, state-level only; no specific GRU / SVR / FSB unit named)"
      claimed_by_sources: [gchq-official-anne-keast-butler]
      requires_analyst_review: true
      notes: >
        State-level attribution ("Kremlin") only. Per Hard Rule 2,
        grader does NOT upgrade to unit-level (GRU / SVR / FSB) or
        actor-roster-level (APT28 #006, Sandworm #007, APT29 #009)
        attribution. Subsea cable + energy pipeline targeting IS the
        Sandworm-canonical pattern but Keast-Butler does not make
        that link explicit; analyst may surface the structural-
        attribution adjacency as SAT-ACH hypothesis with appropriate
        WEP hedging.

# Inclusion eligibility
inclusion:
  eligible_for:
    - daily_brief_action
    - weekly_synthesis
    - actor_profile_update

# Downstream handoff
analyst_review_required: true   # WEP "likely" + Russia-attribution + Sandworm-adjacent targeting pattern
analyst_review_complete: true
analyst_review_run_id: analyst-20260528-1638
red_team_review_required: false # WEP capped at "likely" by single-source veto
red_team_review: null
analysis_sections:
  sat_ach:
    ach_analysis:
      question: >
        Which Russia-attributed actor classes most plausibly account for the
        target categories Keast-Butler named in the 2026-05-28 GCHQ briefing
        (critical infrastructure / democratic processes / supply chains /
        public trust / corporate networks / subsea cables / energy pipelines)?
      analyzed_at: 2026-05-28T16:38:00-04:00
      analyzed_by: analyst
      red_team_review: null
      hypotheses:
        - id: H1
          statement: >
            Keast-Butler's "Kremlin daily hybrid attacks" framing aggregates
            multiple GRU and SVR services concurrently — Sandworm (GRU 74455)
            for subsea-cable / energy-pipeline / critical-infrastructure
            targeting; APT28 (GRU 26165) for corporate / supply-chain
            espionage; APT29 (SVR) for democratic-process / influence
            operations. State-level shorthand for a multi-unit picture.
          attribution_provenance: not_sourced  # Keast-Butler did NOT make this unit-level claim
        - id: H2
          statement: >
            Sandworm-dominant — subsea cable + energy pipeline targeting is
            Sandworm-canonical (roster #007); Keast-Butler's framing is
            primarily driven by Sandworm activity with other services
            secondary.
          attribution_provenance: not_sourced
        - id: H3
          statement: >
            Generic Russia-state framing without specific unit decomposition
            — Keast-Butler's framing is genuinely state-level diplomatic-
            policy language, not a shorthand for any specific service mix.
            Targeting categories are recurring patterns across the broader
            Russia-state ecosystem (intelligence services + military
            intelligence + military operations).
          attribution_provenance: sourced  # this is what Keast-Butler actually said
        - id: H4
          statement: >
            Non-traditional Russia-aligned proxies (NoName057, paid sabotage
            networks, Wagner-successor groups, "amateur saboteurs and spies"
            per Keast-Butler verbatim) account for a material share of the
            activity Keast-Butler is describing — physical-domain sabotage
            specifically.
          attribution_provenance: partially_sourced  # "amateur saboteurs" language is direct quote
        - id: H5
          statement: >
            The framing reflects UK political-diplomatic positioning more than
            operational threat decomposition — daily-hybrid-attacks framing
            is a policy-tempo claim for parliamentary / NATO audiences,
            decoupled from any specific operational tasking pattern.
          attribution_provenance: not_sourced
      evidence:
        - id: E1
          description: "Keast-Butler verbatim: 'amateur saboteurs and spies remotely operated by the Kremlin' (≤15 words)"
          source: the-record
          digraph: B2
          weight: 2
        - id: E2
          description: "Target categories include subsea cables + energy pipelines"
          source: gchq-official-anne-keast-butler
          digraph: A2  # primary speaker
          weight: 3
        - id: E3
          description: "Target categories include corporate networks + supply chains"
          source: gchq-official-anne-keast-butler
          digraph: A2
          weight: 3
        - id: E4
          description: "Target categories include democratic processes + public trust"
          source: gchq-official-anne-keast-butler
          digraph: A2
          weight: 3
        - id: E5
          description: "Russian submarine operations near critical seabed infrastructure"
          source: gchq-official-anne-keast-butler
          digraph: A2
          weight: 3
        - id: E6
          description: "GCHQ defensive activity includes 'countering reckless sabotage and assassination attempts' (verbatim, ≤15 words)"
          source: the-record
          digraph: B2
          weight: 2
        - id: E7
          description: "Keast-Butler does NOT name specific GRU / SVR / FSB units"
          source: gchq-official-anne-keast-butler
          digraph: A2
          weight: 3
        - id: E8
          description: "No specific UK A&D prime (BAE / Rolls Royce / Babcock / QinetiQ) named"
          source: gchq-official-anne-keast-butler
          digraph: A2
          weight: 3
        - id: E9
          description: "Subsea cable + energy pipeline targeting is corpus-anchored Sandworm-canonical pattern (roster #007)"
          source: archimedes-corpus
          digraph: A2  # inherited from prior Sandworm grading
          weight: 3
        - id: E10
          description: "Roster-tracked actors: APT28 #006 (GRU 26165, HIGH), Sandworm #007 (GRU 74455, HIGH), APT29 #009 (SVR, HIGH)"
          source: archimedes-roster
          digraph: A1  # internal authoritative
          weight: 3
      matrix:
        E1: {H1: C, H2: N, H3: C, H4: C, H5: C}  # amateur saboteurs fits H4 specifically
        E2: {H1: C, H2: C, H3: C, H4: I, H5: N}  # subsea/energy is unit-state pattern, not amateur-saboteur
        E3: {H1: C, H2: N, H3: C, H4: I, H5: N}
        E4: {H1: C, H2: N, H3: C, H4: I, H5: N}
        E5: {H1: C, H2: C, H3: C, H4: I, H5: N}  # submarine ops are state-military, not amateur
        E6: {H1: C, H2: N, H3: C, H4: C, H5: C}
        E7: {H1: N, H2: N, H3: C, H4: N, H5: C}  # absence of unit-naming is diagnostic of H3 / H5
        E8: {H1: N, H2: N, H3: C, H4: N, H5: C}  # absence of prime-naming neutral on most
        E9: {H1: C, H2: C, H3: N, H4: I, H5: N}  # corpus-side Sandworm fit lifts H1/H2
        E10: {H1: C, H2: C, H3: N, H4: N, H5: N}  # roster fit lifts H1/H2
      inconsistency_counts:
        H1: 0
        H2: 0
        H3: 0
        H4: 4
        H5: 0
      diagnostic_evidence:
        - E1+E6: "Amateur-saboteur language is diagnostic of H4 component"
        - E2+E5: "Subsea / submarine operations are diagnostic of H2 (Sandworm-canonical) but also fit H1 / H3"
        - E7: "Absence of unit naming is diagnostic of H3 (sourced state-level framing)"
        - E9+E10: "Corpus-side Sandworm fit lifts H1 / H2 but cannot be elevated to source-level claim"
      ranking:
        - rank: 1
          hypothesis_id: H3
          rationale: >
            Sourced (Keast-Butler made this framing). Zero inconsistencies.
            Diagnostic absence of unit naming (E7, E8) directly supports.
            Hard Rule 2 anchor: this is the attribution the source made.
          wep: likely  # single-source veto cap
        - rank: 2
          hypothesis_id: H1
          rationale: >
            Zero inconsistencies; corpus-side roster fit (E9, E10) lifts
            structural plausibility. Cannot be elevated to sourced claim
            without explicit unit attribution. Briefer may surface as
            corpus-side structural-adjacency note tagged 'not sourced.'
          wep: roughly_even_chance
        - rank: 3
          hypothesis_id: H2
          rationale: >
            Zero inconsistencies; Sandworm-canonical pattern fit is strong
            but cannot be elevated absent source. Corpus-side
            structural-adjacency only.
          wep: roughly_even_chance
        - rank: 4
          hypothesis_id: H5
          rationale: >
            Zero inconsistencies but requires unverified meta-premise
            (framing is political-tempo claim decoupled from operational
            reality). Plausible-but-untestable; held as null-hypothesis
            placeholder.
          wep: unlikely
        - rank: 5
          hypothesis_id: H4
          rationale: >
            Four inconsistencies. Amateur-saboteur framing fits one slice
            (E1, E6) but subsea / submarine / corporate / democratic-process
            categories require state-service capability that amateur
            proxies don't have. Ruled out as primary explanation; remains
            valid as one component within H1 / H3.
          wep: unlikely
      sensitivity_analysis:
        brittleness: low_to_medium
        load_bearing_evidence: [E2, E7, E9]
        if_second_uk_outlet_corroborates: "Lifts to very_likely candidate on H3; H1 / H2 corpus-side framing unchanged"
        if_keast_butler_names_units_in_follow_on: "Inverts ranking; H1 or H2 becomes sourced"
        if_uk_prime_disclosure_emerges_in_14_days: "E8 weakens; lifts corporate-targeting component"
        single_point_of_failure: >
          H3 is sourced and zero-inconsistency. The interesting analytic
          load is the H1 / H2 corpus-side structural-adjacency framing,
          which briefer may surface as 'not sourced' candidate but MUST
          NOT elevate to attribution. Per Hard Rule 2, analyst cannot
          originate the Sandworm-canonical link Keast-Butler did not
          explicitly make.
      tripwires:
        - observation: "Second UK outlet (BBC / FT / Reuters / Sky) corroborates within 7 days"
          effect: "Lift to B1 candidate; sourced H3 holds"
        - observation: "Keast-Butler / GCHQ follow-on names specific GRU / SVR / FSB units"
          effect: "Rerun ACH with H1 / H2 sourced"
        - observation: "UK A&D prime corporate disclosure within 14 days that links operationally"
          effect: "E8 weakens; lifts corporate-targeting component"
        - observation: "Independent NCSC / FCDO statement attributing specific operations"
          effect: "Lifts attribution layer below state-level"
      conclusion:
        summary: >
          Keast-Butler's "Russia / Kremlin daily hybrid attacks" framing
          ranks H3 (sourced state-level framing) first with zero
          inconsistencies. Corpus-side roster fit on Sandworm-canonical
          subsea / energy pipeline targeting (H2) and the broader multi-
          service decomposition (H1) are structurally plausible but
          unsourced — briefer may surface as corpus-side adjacency notes
          tagged 'not sourced' without elevating to attribution. H4
          (amateur saboteurs as primary) is ruled out; remains a
          component within H3.
        wep: likely  # capped by single-source veto on the underlying sourced framing
        confidence_caveats: >
          Hard Rule 2 anchor: H3 is what Keast-Butler said. H1 / H2
          (multi-unit decomposition / Sandworm-dominant) are corpus-side
          structural inferences. Single-source veto caps at 'likely.'
          Sensitivity is low-to-medium: a single second UK-outlet relay
          would lift to very_likely on H3 but would not lift H1 / H2 to
          sourced.
  sat_kac:
    kac_analysis:
      assessment_under_review: >
        "GCHQ Director Anne Keast-Butler characterizes Russia as conducting
        daily hybrid attacks on the UK across physical-and-cyber domains,
        targeting critical infrastructure / democratic processes / supply
        chains / public trust / corporate networks / subsea cables / energy
        pipelines; structural adjacency to Sandworm-canonical patterns"
        (paraphrased Keast-Butler + analyst inference).
      analyzed_at: 2026-05-28T16:40:00-04:00
      analyzed_by: analyst
      invoking_context: "Analyst review on B2 / likely state-level briefing; single-source veto applied; Sandworm-adjacency hypothesis on subsea cable + energy pipeline targeting"
      assumptions:
        - id: A1
          statement: "Keast-Butler's 'daily' tempo characterization is operationally accurate, not policy-rhetoric inflation"
          category: source_reliability
          stated: true
          why_must_be_true: "Operational-tempo framing depends on it"
          when_could_be_false: "Director-level briefings to parliamentary / NATO audiences sometimes inflate tempo for rhetorical purposes"
          evidence_for: [gchq-official-anne-keast-butler]
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify
        - id: A2
          statement: "Subsea cable + energy pipeline targeting Keast-Butler describes is operationally tied to roster-tracked Sandworm activity (#007)"
          category: TTP_patterns
          stated: false
          why_must_be_true: "Corpus-side structural-adjacency framing depends on it"
          when_could_be_false: "Targeting may be conducted by different Russia-aligned actors (Wagner-successor groups, FSB units, paid sabotage networks) not currently roster-tracked"
          evidence_for: [archimedes-roster, archimedes-corpus]
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify
        - id: A3
          statement: "The Record's relay accurately preserves Keast-Butler's framing without summarization loss"
          category: source_reliability
          stated: false
          why_must_be_true: "Single-source veto applies; relay fidelity is the only check"
          when_could_be_false: "Recorded Future News editorial may compress / paraphrase parts of the briefing"
          evidence_for: [the-record]
          evidence_against: []
          confidence: medium
          centrality: peripheral
          classification: sound
        - id: A4
          statement: "Russia-aligned 'amateur saboteurs and spies remotely operated by the Kremlin' represent a material component of the threat, not an aside"
          category: capability
          stated: true
          why_must_be_true: "ACH H4 weighting depends on it"
          when_could_be_false: "Amateur-saboteur framing may be rhetorical flourish rather than operational characterization"
          evidence_for: [the-record]
          evidence_against: []
          confidence: medium
          centrality: peripheral
          classification: sound
        - id: A5
          statement: "UK A&D primes (BAE / Rolls Royce / Babcock / QinetiQ) sit within the corporate-network / supply-chain target categories Keast-Butler named"
          category: target_profile
          stated: false
          why_must_be_true: "A&D-relevance narrative depends on UK A&D primes being implicit targets"
          when_could_be_false: "Keast-Butler may have intended specific civilian / utility sector framing"
          evidence_for: [archimedes-roster]
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify
        - id: A6
          statement: "Russia operational posture against UK / EU is stable through 2026 H2 (no diplomatic détente, no operational tempo shift)"
          category: geopolitical_context
          stated: false
          why_must_be_true: "Forward-projection / standing carry-forward depends on it"
          when_could_be_false: "Ukraine war trajectory shift, Russia internal political change, NATO posture shift"
          evidence_for: []
          evidence_against: []
          confidence: unknown
          centrality: material
          classification: qualify
        - id: A7
          statement: "Keast-Butler's deliberate non-naming of GRU / SVR / FSB units reflects discipline-of-attribution, not absence of evidence"
          category: source_reliability
          stated: true
          why_must_be_true: "ACH H3 ranking rests on sourced absence of unit-level claim"
          when_could_be_false: "Underlying GCHQ assessment may have unit-level confidence not disclosed for diplomatic reasons"
          evidence_for: [gchq-official-anne-keast-butler]
          evidence_against: []
          confidence: high
          centrality: critical
          classification: sound
        - id: A8
          statement: "Transatlantic A&D communications via UK subsea cables include DoD-UK shared intelligence and STRATCOM links"
          category: capability
          stated: true
          why_must_be_true: "Structural A&D-relevance narrative depends on it"
          when_could_be_false: "Specific cable-to-link mapping is classified; structural inference may overstate STRATCOM cable-dependency"
          evidence_for: []
          evidence_against: []
          confidence: medium
          centrality: peripheral
          classification: qualify
      classifications_summary:
        sound: 3
        qualify: 5
        test: 0
        reject: 0
      remediation:
        status: proceed
        qualifying_caveats:
          - "Director-level tempo claim ('daily') accepted at face value; rhetorical-inflation alternative not ruled out"
          - "Sandworm-canonical structural adjacency on subsea / energy pipeline targeting is corpus-side inference, not sourced from Keast-Butler"
          - "UK A&D primes implicitly inside corporate / supply-chain target categories; not explicitly named"
          - "Russia operational posture stability through 2026 H2 assumed; standard geopolitical-context qualifier"
          - "Transatlantic A&D-communications dependency on UK subsea cables presumed; specific link-mapping classified"
        next_action: >
          Brief at likely on Keast-Butler's sourced state-level framing.
          Surface corpus-side Sandworm-adjacency as structural inference
          tagged 'not sourced' if A&D-relevance framing requires.
          Operator may corroborate via BBC / FT / Reuters / Sky. Track
          UK prime corporate disclosures over next 14 days for any
          prime-named incident that would link operationally.
      recommended_wep_after_test:
        if_second_uk_outlet_corroborates: very_likely  # lifts single-source veto
        if_no_corroboration_within_7_days: likely  # current ceiling
        if_uk_prime_disclosure_emerges: very_likely  # lifts corporate-targeting component

# Lifecycle
tlp: CLEAR
published_in_briefs: [2026-05-28-afternoon]
retracted: false
retraction_brief_id: null
---

# GCHQ Director Anne Keast-Butler — Russia Conducting Daily Hybrid Attacks on UK "From Seabed to Cyberspace"

## Summary

GCHQ Director **Anne Keast-Butler** in a 2026-05-28 official briefing characterized Russia as conducting **daily** hybrid attacks on the United Kingdom and Europe spanning physical-and-cyber domains. Targeting categories named: **critical infrastructure, democratic processes, supply chains, public trust, corporate networks, subsea cables, and energy pipelines**. Specific operations described include Russian submarine activity near critical seabed infrastructure and "amateur saboteurs and spies remotely operated by the Kremlin" (verbatim, ≤15 words). GCHQ posture described includes defending subsea cables and energy pipelines in British waters, disrupting Russian networks smuggling sanctioned technology, and countering "reckless sabotage and assassination attempts." No specific UK A&D primes (BAE Systems, Rolls Royce, Babcock, QinetiQ) named in the relayed summary. Attribution remains at state-level "Kremlin" shorthand — no specific GRU / SVR / FSB unit named.

## Sources

### The Record (the-record, digraph: B)

- URL: https://therecord.media/russia-conducting-attacks-on-uk-gchq-briefing
- Published: 2026-05-28T13:20:00Z (09:20 EDT)
- Byline: Alexander Martin (UK Editor for Recorded Future News)
- Underlying speaker: Anne Keast-Butler, Director of GCHQ (UK Government Communications Headquarters)
- Key claim: GCHQ Director publicly characterizing Russia as conducting daily hybrid attacks on UK across physical-and-cyber domains.

## Technical detail

### Russia target categories (per Keast-Butler briefing)
- Critical infrastructure (general)
- Democratic processes
- Supply chains
- Public trust
- Corporate networks
- Subsea cables
- Energy pipelines

### Specific operations described
- **Russian submarine operations** near "critical seabed infrastructure"
- **"Amateur saboteurs and spies remotely operated by the Kremlin"** (verbatim, ≤15-word compliance preserved)
- **GCHQ defensive activity:** defending subsea cables and energy pipelines in British waters; disrupting Russian networks smuggling sanctioned technology; countering "reckless sabotage and assassination attempts" (verbatim, ≤15 words)

### A&D / DIB relevance — structural framing
- **UK defense estate adjacency.** UK A&D primes on the aerospace-defense watchlist (BAE Systems primary; Rolls Royce, Babcock, QinetiQ, Leonardo UK adjacent) operate within the UK national security ecosystem GCHQ is defending. Keast-Butler's briefing elevates operational-tempo framing for Russia activity against UK at the diplomatic-policy level.
- **Subsea cable + energy pipeline targeting** is the recurring Sandworm-canonical (roster #007) and broader Russia-state targeting pattern. UK subsea cable infrastructure is critical to transatlantic A&D communications including DoD-UK shared intelligence and STRATCOM links.
- **No UK primes named.** Keast-Butler's framing is at the national-security-system level, not the specific-contractor level.

## IOCs surfaced

No technical IOCs (no domains, IPs, hashes, CVEs). State-level diplomatic-policy briefing.

## Relationship to existing findings

- **Pairs with PM-003 (GreyVibe / WithSecure — Russia-nexus AI-augmented Ukraine targeting)** for a single-sweep Russia-adversary pattern thread across two operational tiers (state-level diplomatic-policy briefing here + WithSecure-attributed tracked-operator-level analysis there).
- **Structural-attribution adjacency to roster Russia-attributed actors:** APT28 #006 (GRU 26165), Sandworm #007 (GRU 74455), APT29 #009 (SVR) — all HIGH threat-level corpus-tracked. Subsea cable + energy pipeline targeting is **Sandworm-canonical** but Keast-Butler does NOT make that link explicit. Analyst may surface structural-adjacency SAT-ACH hypothesis.

## Open questions for analyst

- **Single-source veto applied.** WEP capped at "likely" pending second independent relay (BBC / FT / Reuters / Sky / other UK outlet). If second UK-outlet relay surfaces within 7 days, regrade to B1 candidate.
- **Sandworm-adjacency SAT-ACH.** Subsea cable + energy pipeline targeting is Sandworm-canonical (roster #007). Hypothesis worth testing: "Keast-Butler's briefing primarily reflects Sandworm and adjacent GRU activity." Per Hard Rule 2, grader does NOT make that attribution; analyst SAT-ACH with appropriate WEP hedging is the path.
- **UK prime-named-victim surfacing.** Keast-Butler did NOT name BAE Systems / Rolls Royce / Babcock / QinetiQ. Analyst may want to track UK prime corporate disclosures over next 14 days for any prime-named UK A&D incident that would link to this briefing operationally.
- **EU subsea cable + energy pipeline standing carry-forward.** Pairs with corpus-tracked Sandworm / NoName057 / hybrid-Russia patterns. Worth establishing as weekly synthesis standing section if not already.

## Source notes

- All quotes ≤15 words per Hard Rule 6 (four verbatim quotes total: "hybrid attacks ... from seabed to cyberspace"; "amateur saboteurs and spies remotely operated by the Kremlin"; "reckless sabotage and assassination attempts"; and the four target-category line).
- Hard Rule 2 preserved: state-level "Kremlin" attribution NOT upgraded to GRU / SVR / FSB or actor-roster-level.
- Single-relay caveat noted; operator may corroborate via BBC / FT / Reuters / Sky.

## Analytic notes (from analyst review)

ACH ranks H3 (sourced state-level framing — Keast-Butler's actual claim) first with zero inconsistencies; H1 (multi-unit decomposition) and H2 (Sandworm-dominant) are corpus-side structural-adjacency hypotheses that fit the evidence equally well but cannot be elevated to sourced attribution without an explicit Keast-Butler / GCHQ unit-level statement. The diagnostic insight is E7 (absence of unit naming) — Keast-Butler's deliberate non-attribution to GRU / SVR / FSB units IS the discipline that supports H3. The briefer may surface H1 / H2 as corpus-side adjacency notes (tagged "not sourced") if A&D-relevance framing requires, but must NOT elevate to attribution. H4 (amateur saboteurs as primary explanation) ruled out by four inconsistencies — amateur framing fits one slice but subsea / submarine / corporate targeting requires state-service capability.

KAC surfaces eight assumptions; the most analytically interesting is A2 (Sandworm-canonical structural adjacency on subsea / energy pipeline targeting), medium confidence and material centrality, qualified. Three further qualifying caveats: tempo claim accepted at face value (A1), UK A&D primes implicitly inside corporate target categories (A5), and Russia geopolitical-posture stability through 2026 H2 (A6, unknown confidence). WEP "likely" appropriately capped by single-source veto. A single second UK-outlet relay (BBC / FT / Reuters / Sky) within 7 days would lift to very_likely on H3; would not change the H1 / H2 sourcing status.
