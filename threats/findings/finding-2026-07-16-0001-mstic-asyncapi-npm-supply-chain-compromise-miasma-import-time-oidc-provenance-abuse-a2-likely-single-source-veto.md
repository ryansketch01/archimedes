---
finding_id: finding-2026-07-16-0001
created_at: 2026-07-16T08:12:00-04:00
graded_by: grader
grading_run_id: morning-20260716-080000
grading_mode: scheduled_brief
raw_id_source: raw-2026-07-16-am-001

# Core grading (from admiralty-grading skill output)
# Single vendor, single evidence basis (MSTIC's own investigation). No layered split:
# procedural-compromise facts and the novelty/mechanism characterization all rest on one
# source, so the whole caps at credibility 2 and the single-source veto binds WEP at "likely."
digraph: A2
source_reliability:
  grade: A
  source_name: Microsoft Threat Intelligence (MSTIC) — Microsoft Security Blog
  source_yaml_id: mstic
  grade_rationale: >
    Pre-assigned A per source-grades.yaml (nation-state / supply-chain tracking, Defender
    telemetry-backed). This is a first-party MSTIC disclosure (not a relay) — Microsoft's own
    investigation of the @asyncapi npm compromise, published 2026-07-16 01:36 UTC with named
    research bylines. Authoritative on the procedural compromise facts (package versions,
    timeline, C2 endpoint, Defender detection names) and on the mechanism characterization.
  provisional: false
credibility:
  grade: 2
  checklist_passed:
    - probably_true_ttp_consistent          # pwn-request / pull_request_target PAT theft + import-time loader + OIDC-published-with-valid-provenance is a coherent, documented supply-chain-compromise mechanism class (sibling to tracked VT-006 Mini Shai-Hulud OIDC/SLSA abuse and VT-009 Nx Console)
    - probably_true_no_contradicting_ab      # no A/B-grade source contradicts any element of the MSTIC account
    - probably_true_claims_coherent          # concrete artifacts (5 versions across 4 package names, C2 85.137.53.71 on 8080/8081/8091, IPFS sync.js stage, Defender detections) are internally coherent; Miasma runtime already documented in the corpus (see relationship note) — not a novel-tooling extraordinary claim
  grade_1_withheld_reason: >
    Grade 1 (Confirmed) withheld — no INDEPENDENT evidence basis for the AsyncAPI compromise this
    window. MSTIC is the sole reporting source. The co-occurring Unit 42 npm-landscape refresh
    (raw-2026-07-16-am-003) concerns the Shai-Hulud lineage / VT-006, a DIFFERENT campaign, tooling,
    and C2 — it is NOT corroboration of the AsyncAPI/Miasma event (collector confirmed: "Mechanism
    differs from Mini Shai-Hulud; distinct C2; no attribution overlap asserted"). Prior corpus
    coverage of the Miasma family (a "Miasma A1 origin" finding shipped in the 2026-06-03 morning
    brief) is same-vendor MSTIC lineage — it reinforces mechanism-coherence but is not an independent
    second evidence basis for this specific compromise. Err low -> 2.
  rationale: >
    A-grade first-party MSTIC disclosure that the @asyncapi npm organization was compromised on
    2026-07-14 (five malicious versions across four package names, import-time "Miasma" loader,
    live C2, OIDC/provenance abuse origin). Coherent with documented supply-chain-compromise TTPs
    and with previously-corpus-documented Miasma tooling; no contradicting higher-grade source.
    Not lifted to Confirmed because a single source carries the campaign this window.
corroboration:
  independent_sources:
    - mstic
  independent: false
  test_passed: null
  test_failed: >
    Remove MSTIC and no source with an independent evidence basis remains for the AsyncAPI
    compromise. Unit 42's npm-landscape doc (am-003) is a different campaign lineage (Shai-Hulud /
    VT-006), not this event. The 2026-06-03 corpus Miasma-origin finding is same-vendor MSTIC
    lineage, not independent. Single effective source -> not independent.
first_party_precedence:
  applied: false
  queried_indices: [archimedes, defenseclaw_local]
  query_window: "-45d"
  splunk_evidence: >
    Queried (defenseclaw_local OR archimedes) for C2 IP 85.137.53.71, "asyncapi", "Miasma",
    "sync.js" over -45d. Seven events returned — ALL archimedes:operation audit/operational
    log-events (FLASH-sweep meta-events, git_committed, brief_published) that matched the keyword
    "Miasma" from prior corpus coverage (the 2026-06-03 Miasma-origin finding + a
    Megalodon/TrapDoor/Miasma watch-pattern hold). ZERO defenseclaw_local network-telemetry hits on
    the C2 IP or the compromised packages. That is operational-metadata provenance, not a network
    telemetry hit. Silent first-party telemetry does NOT disconfirm (Hard Rule 8; absence of
    evidence != evidence of absence). first_party_precedence therefore not applied.
single_source_veto_applied: true
single_source_veto_scope: "entire finding — MSTIC is the sole reporting source for the AsyncAPI compromise this window"
wep_ceiling: likely

# Cluster metadata
cluster:
  topic: "AsyncAPI npm organization supply-chain compromise (2026-07-14) — import-time Miasma loader delivered via OIDC/valid-provenance abuse of a GitHub Actions pwn-request; live C2"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-07-16-am-001
  environmental_context_not_merged:
    # am-003 co-occurs in the npm-supply-chain theme but is a DIFFERENT campaign lineage (Shai-Hulud /
    # VT-006). NOT merged (would be multi-claim) and NOT corroboration of this event. Referenced as
    # environmental backdrop only; rejected as a standalone finding (reject-2026-07-16-0001).
    - raw-2026-07-16-am-003
  attribution_claims: []          # Hard Rule 2 — MSTIC names NO threat actor. None originated. The npm-oidc-no-reply@github.com identity is a legitimate GitHub OIDC publish identity ABUSED, not an attacker identity.

# Inclusion eligibility (from admiralty-grading)
inclusion:
  eligible_for:
    - flash
    - daily_brief_action
    - weekly_synthesis
  not_eligible_for:
    - actor_profile_update        # no actor attributed (Hard Rule 2)
  flash_disposition:
    grade_floor_cleared: true     # A2 clears the FLASH B2 floor
    substantive_trigger_met: false
    rationale: >
      Grade-eligible for FLASH but no FLASH substantive trigger fires: no CVE (not KEV-eligible),
      no CVSS 10.0, no tracked A&D-nexus actor, no named A&D victim. The compromise is real and
      carries a LIVE C2 IOC, but the exposure window has passed (packages identified/being
      remediated) and there is no A&D-prime victimology. Action-item / defensive-hunt tier for the
      scheduled brief, not an "actually wake up" FLASH. Defer final inclusion call to briefer.

# Downstream handoff flags
analyst_review_required: true     # WEP == likely (meets >= likely threshold); live C2 IOC + supply-chain SDLC-exposure angle warrant analyst attention
analyst_review_complete: true
analyst_review_run_id: analyst-20260716-081500
red_team_review_required: false   # WEP == likely, below the very_likely trigger; single-source veto binds; ACH did not lift WEP
red_team_review: null
# Analyst SAT verdict: assessment SURVIVES. WEP unchanged (likely; single-source veto binds; ACH cannot lift).
# ACH pressure-tests MOTIVE/NATURE (NOT attribution — MSTIC names no actor, Hard Rule 2). Leading read:
# opportunistic / non-targeted supply-chain compromise. ACH REJECTS the targeted-A&D-espionage inflation
# (H2, 1 inconsistency, not ruled out but unsupported by victimology) and REFUTES benign researcher/PoC (H3, 3 inconsistencies).
wep_ceiling_adjusted: likely
wep_ceiling_adjustment_reason: "No change. Already veto-capped at likely. ACH confirms likely and cautions against reading targeted-A&D espionage into an ecosystem-wide, no-victimology compromise."
assessment_blocked_pending_test: false
analysis_sections:
  sat_ach:
    ach_analysis:
      question: >
        What is the NATURE/MOTIVE of the 2026-07-14 @asyncapi npm supply-chain compromise (import-time Miasma
        loader, OIDC/provenance abuse, live C2)? Hypotheses characterize activity-type only. Hard Rule 2 binds:
        MSTIC names no actor; NO named-actor attribution is originated or resolved here.
      analyzed_at: 2026-07-16T08:15:00-04:00
      analyzed_by: analyst
      red_team_review: null
      hard_rule_2_frame: >
        Hypotheses enumerate candidate motive/actor-TYPES (opportunistic crime, targeted espionage, researcher,
        false-flag, automated/non-directed). None names a roster actor. Ranking-1 is a nature characterization,
        not an attribution. No cited source is contradicted.
      hypotheses:
        - id: H1
          statement: "Opportunistic, financially-motivated criminal supply-chain compromise — broad ecosystem harvesting via a high-reach transitive dependency; no specific victim targeting."
        - id: H2
          statement: "Targeted supply-chain espionage — @asyncapi compromised as a delivery vector to reach specific high-value downstream (e.g., A&D/enterprise) SDLCs."
        - id: H3
          statement: "Security researcher / red-team / proof-of-concept — non-malicious demonstration of import-time execution + OIDC-provenance abuse."
        - id: H4
          statement: "False-flag / disruption — deployment designed to implicate the prior Miasma operator or discredit npm/OIDC provenance-trust controls."
        - id: H5
          statement: "Automated / self-propagating compromise with no coherent human targeting direction (null-adjacent — genuine compromise, no directed campaign)."
      evidence:
        - id: E1
          description: "Import-time (module-load) loader survives npm install --ignore-scripts — deliberate evasion of a common developer assumption"
          source: mstic
          digraph: A2
          weight: 3
        - id: E2
          description: "OIDC/valid-provenance abuse via pwn-request PAT theft; poisoned artifacts carry valid provenance signatures from unauthorized commits — advanced SDLC tradecraft"
          source: mstic
          digraph: A2
          weight: 3
        - id: E3
          description: "Modular runtime carries 6 capability modules (credential harvest, encrypted exfil, propagation, metamorphic gen, AI-tool poisoning, sandbox evasion) but they are DISABLED in this build"
          source: mstic
          digraph: A2
          weight: 3
        - id: E4
          description: "Resilient decentralized C2/fallback (Nostr, Ethereum, BitTorrent DHT, libp2p, IPFS) — sophisticated live operational infrastructure"
          source: mstic
          digraph: A2
          weight: 3
        - id: E5
          description: "Broad reach — @asyncapi/specs is a widely-used transitive dependency; compromise hit developer workstations, CI/CD, container builds, prod broadly"
          source: mstic
          digraph: A2
          weight: 3
        - id: E6
          description: "C2 (85.137.53.71) is LIVE/active at disclosure — a real operating malicious deployment, not dormant"
          source: mstic
          digraph: A2
          weight: 3
        - id: E7
          description: "MSTIC names NO actor and reports NO victim-specific targeting/victimology (absence of evidence, not evidence of absence)"
          source: mstic
          digraph: A2
          weight: 3
        - id: E8
          description: "Miasma is a previously-corpus-documented family (MSTIC 2026-06-03 origin); this is a fresh deployment — tooling/family reuse and continuity"
          source: mstic
          digraph: A2
          weight: 3
        - id: E9
          description: "Compromise is ecosystem-wide; NO sector targeting and NO A&D victim named"
          source: mstic
          digraph: A2
          weight: 3
        - id: E10
          description: "Module set present (credential harvest + crypto/Ethereum + AI-tool poisoning) is consistent with financial/broad-harvesting motive"
          source: mstic
          digraph: A2
          weight: 3
        - id: E11
          description: "First-party Splunk: ZERO defenseclaw_local network hits on C2/packages over -45d (only archimedes audit-metadata keyword hits from prior corpus) — visibility-bounded null"
          source: splunk-negative-search
          digraph: A1
          weight: 3
      matrix:
        E1: {H1: C, H2: C, H3: C, H4: C, H5: C}   # sophisticated evasion — non-diagnostic (fits all)
        E2: {H1: C, H2: C, H3: C, H4: C, H5: C}   # provenance abuse — non-diagnostic
        E3: {H1: N, H2: C, H3: C, H4: N, H5: N}   # disabled modules fit staged-targeted (H2) or PoC (H3)
        E4: {H1: C, H2: C, H3: I, H4: C, H5: C}   # live resilient C2 inconsistent with benign researcher
        E5: {H1: C, H2: N, H3: N, H4: C, H5: C}   # broad reach mildly favors opportunistic
        E6: {H1: C, H2: C, H3: I, H4: C, H5: C}   # live active C2 inconsistent with PoC
        E7: {H1: N, H2: N, H3: N, H4: N, H5: N}   # no actor/no targeting reported — non-diagnostic on motive
        E8: {H1: C, H2: C, H3: I, H4: C, H5: C}   # established malicious family reuse inconsistent with researcher
        E9: {H1: C, H2: I, H3: N, H4: N, H5: C}   # no victimology cuts against targeted espionage
        E10: {H1: C, H2: C, H3: N, H4: N, H5: C}  # financial/harvest modules — non-diagnostic H1/H2
        E11: {H1: N, H2: N, H3: N, H4: N, H5: N}  # visibility-bounded null (Hard Rule 8) — non-diagnostic
      inconsistency_counts:
        H1: 0
        H2: 1
        H3: 3
        H4: 0
        H5: 0
      diagnostic_evidence:
        - E9: "Distinguishes targeted espionage (H2) from opportunistic/non-directed (H1/H5) — no observed victimology"
        - E4: "Distinguishes live operational deployment from benign PoC (H3)"
        - E6: "Live active C2 refutes researcher/PoC (H3)"
        - E8: "Established malicious-family reuse refutes researcher (H3); mildly supports false-flag (H4)"
        - E3: "Disabled module set weakly favors staged/targeted (H2) or PoC (H3)"
      ranking:
        - rank: 1
          hypothesis_id: H1
          rationale: "Zero inconsistencies; most diagnostic support (E5, E9, E10 point to opportunistic/non-targeted financial harvesting). Converges with H5 (both = non-directed)."
          wep: likely
        - rank: 2
          hypothesis_id: H5
          rationale: "Zero inconsistencies but largely a mechanism-detail subset of H1 (non-directed). Not truly mutually exclusive with H1."
          wep: likely
        - rank: 3
          hypothesis_id: H2
          rationale: "One inconsistency (E9). NOT ruled out — 'no victimology' is an absence that could be visibility/reporting-limited. Would rise sharply if independent corroboration named A&D victims."
          wep: unlikely
        - rank: 4
          hypothesis_id: H4
          rationale: "Zero inconsistencies but requires multiple unverified assumptions (false-flag intent; a prior Miasma operator to frame — itself unnamed). Low prior per Occam."
          wep: very_unlikely
        - rank: 5
          hypothesis_id: H3
          rationale: "Three inconsistencies (E4, E6, E8). Refuted — live resilient C2 + established malicious-family reuse are not benign research."
          wep: remote
      sensitivity_analysis:
        brittleness: medium
        load_bearing_evidence: [E9, E4, E6, E8]
        single_point_of_failure: >
          Entire evidence base is MSTIC (single source, A2). Every row inherits that dependency. The leading
          motive read (opportunistic vs targeted) is robust WITHIN that source, but not independent of it.
        if_E9_reinterpreted: "If undisclosed victimology exists (MSTIC reporting breadth, not confirmed absence), H2 (targeted espionage) rises from unlikely toward roughly-even. This is the key watch item."
        if_mstic_downgraded: "All weights drop; H1/H5 vs H2 becomes indistinguishable. Single-source veto already caps WEP at likely regardless."
      tripwires:
        - observation: "Independent A/B-grade source (Unit 42 / Wiz / Snyk / Socket / GitHub self-disclosure) reports the SAME AsyncAPI/Miasma compromise with named victimology"
          effect: "Lift credibility toward Confirmed; if A&D/sector victims named, elevate H2 and rerun ACH; route to red-team if WEP reaches very_likely"
        - observation: "Miasma modules observed ENABLED/active in a later build"
          effect: "Re-rank — active credential/exfil modules strengthen H1 (financial) or, if paired with target selection, H2"
        - observation: "First-party Splunk observes C2 85.137.53.71 or a compromised package in defenseclaw_local"
          effect: "First-party telemetry (Hard Rule 8); rerun ACH with direct-exposure weighting"
      conclusion:
        summary: >
          The evidence is most consistent with an OPPORTUNISTIC, non-targeted supply-chain compromise (H1/H5):
          zero inconsistencies and diagnostic support from broad ecosystem reach, absent victimology, and a
          financial/harvesting module set. Targeted-A&D-espionage (H2) is NOT ruled out but is unsupported by any
          observed targeting and rests on an absence that could be reporting-limited. Benign researcher/PoC (H3)
          is refuted by live resilient C2 and established malicious-family reuse. No actor is named or implied —
          this is a nature/motive characterization, not an attribution (Hard Rule 2). The analytic value here is
          defensive: the briefer should present this as ecosystem-wide/opportunistic and NOT inflate it into a
          targeted A&D story, while keeping the independent-corroboration + victimology tripwire live.
        wep: likely
        confidence_caveats: >
          Single-source (MSTIC A2) dependence binds WEP at likely via the single-source veto; ACH cannot lift it.
          The opportunistic read is robust within the source but the whole base is one source. 'No A&D targeting'
          is an absence of evidence, NOT a confirmed negative.
  sat_kac:
    kac_analysis:
      assessment_under_review: >
        "The @asyncapi npm compromise is a real, ecosystem-wide supply-chain event (A2/likely, single-source veto);
        A&D relevance is structural/SDLC-exposure, not A&D-directed; no actor attributed."
      analyzed_at: 2026-07-16T08:18:00-04:00
      analyzed_by: analyst
      invoking_context: "Post-ACH stress-test of the surviving opportunistic/structural-relevance line before briefer use; morning brief 2026-07-16."
      assumptions:
        - id: A1
          statement: "MSTIC's compromise facts (5 versions/4 packages, C2, import-time mechanism, OIDC-provenance origin) are accurate"
          category: source_reliability
          stated: true
          why_must_be_true: "The entire finding rests on the MSTIC account"
          when_could_be_false: "MSTIC investigation error or later revision"
          evidence_for: [mstic]
          evidence_against: []
          confidence: high
          centrality: critical
          classification: sound
        - id: A2
          statement: "MSTIC is the SOLE reporting source this window (no independent evidence basis yet)"
          category: source_reliability
          stated: true
          why_must_be_true: "Drives the credibility-2 / single-source veto / likely cap"
          when_could_be_false: "Unit 42 / Wiz / Snyk / Socket / GitHub publish independent confirmation of THIS compromise"
          evidence_for: [mstic]
          evidence_against: []
          confidence: high
          centrality: material
          classification: sound
        - id: A3
          statement: "This event and the 2026-06-03 Miasma-origin finding are the same malware family (continuity)"
          category: ttp_patterns
          stated: true
          why_must_be_true: "Underpins the mechanism-coherence argument (credibility 2) and the 'new deployment not first sighting' framing"
          when_could_be_false: "Same-name / different-lineage; MSTIC family labeling drift"
          evidence_for: [mstic]
          evidence_against: []
          confidence: medium
          centrality: peripheral
          classification: sound
        - id: A4
          statement: "The activity is NOT A&D-directed (ecosystem-wide, no targeting)"
          category: intent
          stated: true
          why_must_be_true: "Supports the structural-relevance framing and the no-FLASH disposition"
          when_could_be_false: "Undisclosed victimology exists; MSTIC did not report victim selection; targeting could be present but unobserved"
          evidence_for: [mstic]
          evidence_against: []
          confidence: low
          centrality: material
          classification: qualify
        - id: A5
          statement: "The disabled capability modules are representative of the deployment's intent (not a staged pre-activation build)"
          category: capability
          stated: false
          why_must_be_true: "If modules are staged for later activation on target reach, the opportunistic read weakens"
          when_could_be_false: "Operator activates modules selectively after propagation reaches chosen environments"
          evidence_for: [mstic]
          evidence_against: []
          confidence: low
          centrality: material
          classification: qualify
        - id: A6
          statement: "The exposure window has passed / packages are being remediated (justifies action-tier, not FLASH)"
          category: technology
          stated: true
          why_must_be_true: "Supports the no-FLASH disposition"
          when_could_be_false: "Packages still resolvable in lockfiles/caches/mirrors; transitive pins keep the bad versions live downstream"
          evidence_for: [mstic]
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify
        - id: A7
          statement: "@asyncapi/* actually reaches A&D-prime/Tier-1 build graphs (SDLC-exposure relevance)"
          category: semantic
          stated: true
          why_must_be_true: "Any upgrade of A&D relevance above 'structural/unverified' depends on it"
          when_could_be_false: "A&D primes don't consume @asyncapi/* transitively (same open question as VT-006 @squawk)"
          evidence_for: []
          evidence_against: []
          confidence: unknown
          centrality: peripheral
          classification: qualify
        - id: A8
          statement: "No credential values were stored; asyncapi-bot PAT is compromised-context only (Hard Rule 7)"
          category: source_reliability
          stated: true
          why_must_be_true: "Policy compliance"
          when_could_be_false: "n/a — verified: value not present in source"
          evidence_for: [mstic]
          evidence_against: []
          confidence: high
          centrality: peripheral
          classification: sound
      classifications_summary:
        sound: 4
        qualify: 4
        test: 0
        reject: 0
      remediation:
        status: proceed
        blocking_assumption: null
        qualifying_caveats:
          - "'No A&D targeting' is an absence of observed victimology, NOT a confirmed negative (A4)."
          - "Observed build has capability modules DISABLED; a staged/later-activation posture cannot be excluded (A5)."
          - "Remediation-in-progress does not guarantee the bad versions are unreachable via lockfiles/caches/mirrors (A6)."
          - "Whether @asyncapi/* reaches A&D build graphs is unverified — same open question as VT-006 @squawk (A7)."
        next_action: >
          Proceed to briefer at action/defensive-hunt tier. No blocking test. SDLC-exposure verification (A7)
          is a relevance-UPGRADE tripwire, not a gate — already flagged in the finding's open questions.
      recommended_wep_after_test:
        if_independent_corroboration_with_ad_victimology: "re-rate credibility toward Confirmed; elevate ACH H2; route to red-team if very_likely"
        if_no_new_evidence: likely
        if_first_party_splunk_hit: "rerun ACH with direct-exposure weighting; likely FLASH re-rate"

# Handoff to vuln-tracker / actor-profiler (supply-chain surface; NO CVE)
vuln_tracker_handoff:
  cve: null
  in_index: false
  recommended_action: consider_supply_chain_surface_row
  detail: >
    No CVE assigned (maintainer-org compromise + malicious-package republish, not a product CVE),
    so KEV-ineligible — same structural class as VT-006 (Mini Shai-Hulud) and VT-009 (Nx Console).
    vuln-tracker may open a supply-chain surface note for the AsyncAPI/Miasma compromise linked to
    the VT-006 / VT-009 npm-CI/CD-compromise lineage. Miasma malware family already corpus-documented
    (2026-06-03 Miasma-origin finding) — this is a new deployment/campaign of that family.
  ioc_handoff: "Live C2 85.137.53.71 (8080/8081/8091) + compromised package versions -> master IOC index."

# Lifecycle
tlp: CLEAR
published_in_briefs: [2026-07-16-morning]
retracted: false
retraction_brief_id: null
---

# MSTIC discloses an AsyncAPI npm supply-chain compromise: import-time "Miasma" loader delivered via OIDC/valid-provenance abuse

## Summary

Microsoft Threat Intelligence disclosed on 2026-07-16 that the `@asyncapi` npm organization was compromised on 2026-07-14, with five malicious package versions across four package names (`@asyncapi/specs`, `@asyncapi/generator`, `@asyncapi/generator-components`, `@asyncapi/generator-helpers`) republished within ~90 minutes, each carrying the same injected loader. Because `@asyncapi/specs` is a widely used transitive dependency, the compromise reached developer workstations, CI/CD pipelines, container builds, and production services that imported the affected versions during the exposure window. Two mechanics are notable: the loader executes at module-load (import) time rather than via a postinstall hook — so `npm install --ignore-scripts` does not neutralize it — and the poisoned packages were auto-published through legitimate GitHub Actions OIDC release workflows, producing artifacts carrying valid provenance signatures built from unauthorized source commits. MSTIC names no threat actor.

## Grade rationale (why A2 / likely, not A1 / very likely)

- **Source reliability A:** first-party MSTIC investigation (not a relay), authoritative on the compromise facts.
- **Credibility 2:** no independent evidence basis this window. MSTIC is the sole reporting source; the co-occurring Unit 42 npm-landscape doc is a different campaign lineage (Shai-Hulud / VT-006), not corroboration; prior corpus Miasma coverage (2026-06-03) is same-vendor MSTIC lineage. Coherent with documented supply-chain TTPs and already-known Miasma tooling -> Probably True.
- **Single-source veto applied** -> WEP capped at **likely**. Matches house precedent for single-A-source campaign disclosures (e.g., the A2 / single-source-veto treatment of MSTIC-origin supply-chain findings).

## Sources

### Microsoft Threat Intelligence / MSTIC (mstic, digraph: A)

- URL: https://www.microsoft.com/en-us/security/blog/2026/07/15/unpacking-asyncapi-npm-supply-chain-compromise-import-time-payload-delivery/
- Published: 2026-07-16T01:36 UTC
- Key claim: The `@asyncapi` npm org was compromised 2026-07-14; five malicious versions across four packages carried an import-time "Miasma" loader with live C2, published via OIDC/valid-provenance abuse originating from a GitHub Actions pwn-request.

## Technical detail

Recorded at awareness/defensive level only — no PoC or attack-step reproduction (Hard Rule 3):

- **Delivery:** five versions across four package names republished 2026-07-14 (~07:10-08:49 UTC per MSTIC timeline), each carrying the same injected loader. `@asyncapi/specs@6.11.2` (stable) and `6.11.2-alpha.1` (prerelease) plus `@asyncapi/generator@3.3.1`, `@asyncapi/generator-components@0.7.1`, `@asyncapi/generator-helpers@1.1.1`.
- **Execution model:** import-time (module-load) execution, not the common postinstall-hook pattern. `--ignore-scripts` does not neutralize it.
- **Origin:** a "pwn request" against `asyncapi/generator` — a misconfigured `pull_request_target` GitHub Actions workflow executed attacker-controlled PR code, exposing the `asyncapi-bot` PAT and enabling unauthorized pushes. Legitimate OIDC release workflows then auto-published the poisoned packages under the automated identity `npm-oidc-no-reply@github.com`, yielding **artifacts with valid provenance signatures built from unauthorized source commits** — a provenance-trust-abuse pattern in the same family as tracked VT-006 (OIDC token hijack + SLSA/provenance breaking).
- **Second stage — "Miasma":** modular runtime with active C2, persistence, and decentralized fallback channels (Nostr, Ethereum, BitTorrent DHT, libp2p, IPFS). A child process fetches `sync.js` from IPFS into an OS-specific "NodeJS" masquerade directory. Six additional capability modules (credential harvest, encrypted exfil, supply-chain propagation, metamorphic generation, AI-tool poisoning, sandbox evasion) were present but disabled in this build.
- **Vendor mitigations (verbatim, MSTIC):** remove all five affected versions; purge npm and Yarn caches; hunt for `sync.js` under NodeJS masquerade directories; block outbound to `85.137.53.71` on 8080/8081/8091; rotate credentials reachable from any environment that imported the packages.

## IOCs surfaced

```yaml
iocs:
  - type: ipv4
    value: 85.137.53.71
    role: c2
    context: "Miasma second-stage C2 on ports 8080/8081/8091; MSTIC advises blocking outbound. LIVE."
    campaign: "AsyncAPI npm supply-chain compromise (2026-07-14)"
    related_malware: [Miasma]
    confidence: high
    source: mstic
  - type: file_path
    value: "sync.js (under OS-specific 'NodeJS' masquerade directory)"
    role: staging
    context: "IPFS-fetched second-stage; hunt hint (exact per-OS path not enumerated in source)."
    confidence: medium
    source: mstic
  - type: detection_signature
    value: "Trojan:JS/MiasmStealer.SC"
    role: defender_detection
    context: "Microsoft Defender AV detection name (recorded under yara_rule tag by collector for lack of a detection-signature schema type)."
    source: mstic
  - type: detection_signature
    value: "Trojan:Script/Supychain.A"
    role: defender_detection
    context: "Microsoft Defender AV detection name."
    source: mstic
  - type: npm_package_version
    value:
      - "@asyncapi/specs@6.11.2"
      - "@asyncapi/specs@6.11.2-alpha.1"
      - "@asyncapi/generator@3.3.1"
      - "@asyncapi/generator-components@0.7.1"
      - "@asyncapi/generator-helpers@1.1.1"
    role: compromised_artifact
    context: "Remediation targets — remove and purge npm/Yarn caches."
    source: mstic
do_not_blocklist:
  - type: email
    value: npm-oidc-no-reply@github.com
    reason: >
      Legitimate GitHub OIDC publish identity ABUSED via the release workflow, NOT attacker-owned.
      Provenance/context indicator only — do not naively blocklist.
network_iocs_for_master_index:
  - "85.137.53.71 (C2)"
credential_exposure_detected: false   # asyncapi-bot PAT referenced as compromised-artifact context only; value not present in source; none stored (Hard Rule 7)
```

## Relationship to existing findings

- **New deployment of a previously-documented malware family.** The "Miasma" modular runtime was already covered in the corpus — a "Miasma A1 origin" finding shipped in the 2026-06-03 morning brief (surfaced via the first-party archimedes audit index during the Hard Rule 8 check). The AsyncAPI compromise is a fresh 2026-07-14 deployment of that family, not a first sighting. This reinforces mechanism-coherence (credibility 2) but is same-vendor MSTIC lineage, so it is NOT independent corroboration of this specific compromise.
- **Sibling to the tracked npm/CI-CD supply-chain lineage.** Structurally adjacent to VT-006 (Mini Shai-Hulud / CVE-2026-45321 — OIDC token hijack + SLSA/provenance breaking) and VT-009 (Nx Console). Mechanism DIFFERS from Mini Shai-Hulud (import-time loader vs. self-propagating worm; Miasma vs. TeamPCP tooling; distinct C2). No attribution overlap — do not conflate; TeamPCP (#001) is NOT named here.
- **Co-occurring but distinct.** The Unit 42 npm-landscape refresh (raw-2026-07-16-am-003) is the same theme but a different campaign lineage (Shai-Hulud / VT-006); rejected as a standalone finding (reject-2026-07-16-0001), referenced here as environmental backdrop only.

## A&D relevance

Structural / SDLC-exposure. AsyncAPI tooling is event-driven-API specification and code-generation software; `@asyncapi/specs` as a transitive dependency can reach A&D-prime and supplier SDLCs, CI/CD pipelines, and container builds. No named A&D victim and no sector targeting — the compromise is ecosystem-wide, not A&D-directed. Relevance flows from the same dependency-graph-reach concern already logged for VT-006's `@squawk` aviation-namespace analysis: an import-time loader that survives `--ignore-scripts` and publishes with valid provenance defeats two common developer-side assumptions, which raises defensive priority for any org with Node/TypeScript build pipelines. Concrete defensive actions are enumerated in Technical detail.

## Open questions for analyst

- **Independence tripwire:** the finding is capped at A2 / likely because MSTIC is the sole source. Independent A/B-grade telemetry (Unit 42 / Wiz / Snyk / Socket / GitHub self-disclosure) on the AsyncAPI/Miasma compromise specifically would lift credibility toward Confirmed and WEP toward very likely, routing to red-team. Watch for it.
- **Hard Rule 2 discipline:** MSTIC names no actor. Do not let the Miasma-family lineage (2026-06-03 origin) or the VT-006/TeamPCP adjacency cause attribution-by-inference. Report only what MSTIC states.
- **Provenance-trust angle:** valid provenance signatures on packages built from unauthorized commits is the load-bearing novelty for defenders (SLSA/OIDC-trust assumptions). Worth an ACH/KAC pass on whether provenance attestation remains a usable defensive control for the target profile given this and the VT-006 precedent.
- **SDLC exposure test:** whether `@asyncapi/*` reaches A&D-prime build graphs is unverified (same open question as VT-006 `@squawk`). If an A&D-prime or Tier-1 supplier publishes a customer-impact statement, re-rate A&D relevance upward.

## Analytic notes (from analyst review)

The assessment survives SAT review; WEP stays **likely** (single-source veto binds — ACH cannot lift it). Because MSTIC names no actor, the ACH pressure-tested the *nature* of the activity, not attribution (Hard Rule 2). The evidence is most consistent with an **opportunistic, non-targeted** supply-chain compromise: broad ecosystem reach, no observed victimology, and a financial/harvesting module set all point that way (zero inconsistencies). The strongest counter-hypothesis is targeted supply-chain espionage — it is *not* ruled out, but it rests on a single inconsistency (absent victimology) that could be reporting-limited rather than confirming an actual absence of targeting. The benign researcher/PoC reading is refuted: a live, resilient decentralized C2 plus reuse of an established malicious family is not research.

For the briefer: present this as an **ecosystem-wide, opportunistic** compromise with real defensive urgency (import-time execution defeats `--ignore-scripts`; valid provenance on unauthorized commits defeats SLSA/OIDC trust) — but do **not** inflate it into a targeted-A&D narrative. A&D relevance is structural and unverified.

The load-bearing assumptions worth watching (KAC): "no A&D targeting" is an *absence*, not a confirmed negative; the observed build has capability modules disabled (staged activation cannot be excluded); and whether `@asyncapi/*` reaches A&D build graphs is unverified. None blocks publication. The live tripwire is independent corroboration with named victimology — if it names A&D/sector victims, elevate the espionage hypothesis and re-run.
