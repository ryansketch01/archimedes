---
finding_id: finding-2026-07-30-0007
created_at: 2026-07-30T16:24:00-04:00
graded_by: grader
grading_run_id: afternoon-20260730-160000
grading_mode: scheduled_brief
finding_type: net_new                 # first Archimedes finding for the Analog Devices SEC-filed breach

# Core grading (from admiralty-grading skill output)
digraph: B2
source_reliability:
  grade: B
  source_name: "BleepingComputer (Bill Toulas), corroborated at outlet level by SecurityWeek (Eduard Kovacs) and The Record — all reporting Analog Devices' SEC filing"
  source_yaml_id: bleepingcomputer
  secondary_source_yaml_ids: [securityweek, the-record]
  underlying_primary:
    source_name: "Analog Devices (ADI) SEC filing (company self-disclosure of the breach)"
    grade: A                          # a company's own regulatory (SEC) breach disclosure is authoritative for the FACT-of-disclosure
    in_hand_this_cycle: false         # SEC filing not directly retrieved; reaches corpus via three relays
  grade_rationale: >
    Anchored B on BleepingComputer (B) with two additional B-grade relays (SecurityWeek — provisional B,
    awaiting_ratification; The Record — B). All three restate the same ADI SEC filing (A-class company
    self-disclosure), which was not directly retrieved this cycle. Three publisher-independent outlets +
    a legally-accountable SEC filing is a strong basis for the FACT of the breach, but a single upstream
    evidence basis for its substance.
  provisional: false
credibility:
  grade: 2
  checklist_passed:
    - probably_true_claims_coherent            # SEC-filed breach disclosure with a detection date (2026-06-23), 'operations unaffected' framing, external-IR + law-enforcement notification — internally coherent and consistent with standard 8-K breach-disclosure practice
    - probably_true_no_contradicting_ab        # no A/B source contradicts; three independent outlets + the SEC filing agree on the core facts
  grade_1_withheld_reason: >
    Grade 1 (Confirmed) withheld. The three outlets are publisher-independent but all relay the SAME ADI SEC
    filing — single upstream evidence basis (INTEL-GRADING: outlets relaying one document are not independent
    corroboration). The FACT that ADI disclosed a breach is near-certain (SEC filings are legally
    accountable), but the SUBSTANCE (scope, data types, actor) is explicitly undetailed / under
    investigation, and the ExfilSquad connection is UNCONFIRMED. Single evidence basis for the substance ->
    at most grade 2.
  rationale: >
    Graded claim: Analog Devices disclosed in an SEC filing that an unauthorized party accessed some systems
    and exfiltrated certain files (breach detected 2026-06-23), states business operations were unaffected and
    no material financial impact is anticipated, and engaged external IR + notified law enforcement. Coherent,
    multi-outlet, consistent with routine SEC breach-disclosure practice, no contradiction -> Probably True.
    The type of data compromised is NOT yet detailed, and the ExfilSquad-vs-SEC-breach linkage is UNCONFIRMED.
corroboration:
  independent_sources:
    - bleepingcomputer
    - securityweek
    - the-record
  independent: false
  test_result: >
    FAILS independence for the substance. SecurityWeek (07:16 EDT), BleepingComputer (11:12 EDT), and The
    Record (15:10 EDT) are three publisher-independent outlets but all relay the same ADI SEC filing — single
    shared evidence basis. Outlet count strengthens confidence in the fact-of-disclosure (-> "likely") without
    providing a second independent basis for scope/actor. The ExfilSquad leak-site listing is a separate
    basis but its connection to the SEC-filed breach is explicitly UNCONFIRMED and it is a low-grade
    self-claim.
first_party_precedence:
  applied: false
  queried_indices: [archimedes, defenseclaw_local]
  query_window: "-24h (grader confirmatory) + collector 15:30 pre-brief entity sweep"
  splunk_evidence: >
    Rule 8 run by grader this cycle: (index=archimedes OR index=defenseclaw_local) NOT sourcetype=archimedes:*
    over "Analog Devices" / "ExfilSquad" -> 0 events, both indices. Collector's 15:30 pre-brief sweep also 0
    defender-telemetry hits. No atomic IOCs were published in any relay, so no indicator hunt was possible.
    Visibility-bounded null — neither corroboration nor disconfirmation (Hard Rule 8).
single_source_veto_applied: true
single_source_veto_note: >
  Applies — single effective evidence basis (the ADI SEC filing, relayed by three outlets) for the breach
  substance. WEP capped at "likely." Veto lifts on direct retrieval of the SEC filing / a confirmed
  independent second basis on scope or actor, or first-party telemetry.
wep_ceiling: likely

# Cluster metadata
cluster:
  topic: "Analog Devices (ADI), a major American semiconductor firm, disclosed in an SEC filing that an unauthorized party accessed some systems and exfiltrated certain files (breach detected 2026-06-23). ADI states operations were unaffected, does not anticipate material financial impact, engaged external cybersecurity experts, and notified law enforcement. Type of data compromised: not yet detailed (under investigation). Data-theft/extortion group ExfilSquad (no file-encryption) initially claimed ADI on its leak site — earlier reporting cited a 570,000-record claim — then delisted the company; the connection between the ExfilSquad intrusion and the SEC-filed breach is UNCONFIRMED. ADI separately noted an unrelated cybersecurity matter reported publicly ~2026-07-26. No defense/aerospace customer, product, actor-roster match, CVE, or atomic IOCs."
  cluster_size: 1
  raw_signal_members:
    - raw-2026-07-30-pm-004
  attribution_claims:
    - claimed_actor: "ExfilSquad"
      type: "data-theft / extortion group (no file-encryption)"
      nation: unknown
      claimed_by_sources: ["ExfilSquad self-claim (leak-site listing, since delisted)"]
      linkage_to_sec_breach: "UNCONFIRMED — relays note it is unclear whether the ExfilSquad intrusion is connected to the SEC-filed breach"
      roster_match: none
      requires_analyst_review: true
      hard_rule_2_note: >
        ExfilSquad self-claim recorded verbatim, NOT asserted by Archimedes. The connection to the SEC-filed
        breach is explicitly UNCONFIRMED and must not be hardened. ExfilSquad is not a roster actor.

# FLASH-adjacency adjudication (grader)
flash_adjacency:
  independently_warrants_flash: false
  rationale: >
    NO tracked actor (ExfilSquad non-roster + unconfirmed linkage), NO CVE, NO atomic IOC, NO named A&D
    victim/product, NO first-party hit. Operations reported unaffected. Correctly held below-FLASH at the
    12:00 sweep and surfaced for the afternoon board on the strength of multi-outlet + SEC-filing state change.

# Inclusion eligibility (from admiralty-grading)
inclusion:
  eligible_for:
    - daily_brief_monitoring
    - weekly_synthesis
  eligibility_note: >
    B2 clears the action-item GRADE bar, but the CONTENT is awareness/monitoring — no atomic IOCs, no CVE,
    unconfirmed actor linkage, no named A&D victim. Recommended for the monitoring/awareness surface and
    weekly synthesis, not an action item.

# Downstream handoff flags
analyst_review_required: true            # attribution claim present (ExfilSquad self-claim, unconfirmed linkage); WEP likely
analyst_review_complete: true
analyst_review_run_id: analyst-20260730-164000
red_team_review_required: false          # WEP ceiling 'likely' (< very_likely)
red_team_review: null
analysis_sections:
  sat_ach:
    status: not_applied
    reason: no_multi_actor_competition
    detail: >
      ACH not warranted. The only actor claim is a single non-roster self-claim (ExfilSquad) whose connection
      to the SEC-filed breach is explicitly UNCONFIRMED. There is no sourced second actor to compete against,
      and generating rival-actor hypotheses for an unattributed breach would originate attribution (Hard Rule
      2). The load-bearing question is a single assumption — the ExfilSquad<->SEC-breach linkage — which is a
      KAC problem, not an ACH one.
  sat_kac:
    kac_analysis:
      assessment_under_review: >
        "Analog Devices disclosed an SEC-filed breach (unauthorized access + file exfiltration, detected
        2026-06-23, operations reportedly unaffected); the data-theft/extortion group ExfilSquad's leak-site
        claim (since delisted; ~570,000 records) may relate to it."
      analyzed_at: 2026-07-30T17:04:00-04:00
      analyzed_by: analyst
      invoking_context: "Pre-publication review — isolating the confirmed core from the unconfirmed actor linkage"
      assumptions:
        - id: A1
          statement: "Analog Devices did disclose a breach in an SEC filing (the fact-of-disclosure)"
          category: source_reliability
          stated: true
          why_must_be_true: "The entire finding exists on this fact"
          when_could_be_false: "All three outlets misread the filing — near-impossible given a legally-accountable SEC filing + three publisher-independent relays"
          evidence_for: [bleepingcomputer, securityweek, the-record]
          evidence_against: []
          confidence: high
          centrality: critical
          classification: sound
        - id: A2
          statement: "The ExfilSquad leak-site claim is connected to the SEC-filed breach"
          category: source_reliability
          stated: true
          why_must_be_true: "Required for any actor/scope narrative around the breach"
          when_could_be_false: "ExfilSquad claimed ADI opportunistically/falsely; the SEC breach is a different or unrelated incident (note ADI's separately-mentioned unrelated cybersecurity matter ~2026-07-26)"
          evidence_for: []                    # only an ExfilSquad self-claim (low-grade); no independent tie
          evidence_against: [the-record]      # relays explicitly state the connection is unclear/unconfirmed
          confidence: low
          centrality: material                # if false, actor/scope collapses BUT the breach-fact (A1) survives -> material, not critical to the finding
          classification: test
        - id: A3
          statement: "The '~570,000 records' figure is ExfilSquad's unverified self-claim, not a confirmed scope"
          category: source_reliability
          stated: true
          why_must_be_true: "Prevents over-stating breach scope"
          when_could_be_false: "ADI later confirms a scope figure"
          evidence_for: []
          evidence_against: []
          confidence: low
          centrality: peripheral
          classification: qualify
        - id: A4
          statement: "The delist-after-claim pattern indicates ransom negotiation"
          category: actor_intent
          stated: false
          why_must_be_true: "Only if used to infer motive/outcome"
          when_could_be_false: "Delisting reflects a false/retracted claim, a takedown, or unrelated housekeeping"
          evidence_for: []
          evidence_against: []
          confidence: low
          centrality: peripheral
          classification: qualify
        - id: A5
          statement: "ADI's separately-noted 'unrelated cybersecurity matter' (~2026-07-26) is genuinely distinct from the SEC-filed breach"
          category: semantic
          stated: true
          why_must_be_true: "Determines whether these are one or two incidents"
          when_could_be_false: "The two are actually the same event, or related — only ADI's characterization separates them"
          evidence_for: [the-record]
          evidence_against: []
          confidence: low
          centrality: peripheral
          classification: qualify
        - id: A6
          statement: "A confirmed ADI breach is A&D-relevant because ADI is a semiconductor supplier into aerospace/defense systems"
          category: capability
          stated: true
          why_must_be_true: "The A&D-relevance framing"
          when_could_be_false: "No DIB customer/product/controlled data implicated; operations reportedly unaffected -> relevance stays structural"
          evidence_for: [bleepingcomputer]
          evidence_against: []
          confidence: medium       # structural
          centrality: material
          classification: qualify
        - id: A7
          statement: "The compromised data types are undetailed / under investigation; a follow-up disclosure could materially change relevance"
          category: technology
          stated: true
          why_must_be_true: "Bounds current confidence in impact"
          when_could_be_false: "n/a — this is a bounding caveat"
          evidence_for: [bleepingcomputer]
          evidence_against: []
          confidence: unknown
          centrality: material
          classification: qualify
      classifications_summary:
        sound: 1
        qualify: 5
        test: 1
        reject: 0
      remediation:
        status: proceed
        qualifying_caveats:
          - "Confirmed core: ADI disclosed a breach (file exfiltration, detected 2026-06-23, operations reportedly unaffected). Publishable as a monitoring item."
          - "Actor/scope is NOT confirmed. The ExfilSquad<->SEC-breach linkage is a low-grade self-claim, explicitly unconfirmed in all relays, and must NOT be hardened (Hard Rule 2). Present the breach as the confirmed core and ExfilSquad as an unverified, since-delisted claim of uncertain connection."
          - "The '~570,000 records' is an unverified scope claim; the delist pattern is suggestive, not dispositive."
          - "A&D relevance is structural (semiconductor-into-A&D); no DIB customer, product, or controlled data named. Track the pending data-type disclosure as a relevance tripwire."
        blocking_assumption: A2   # Test-class, but NON-blocking for awareness-level publication (see detail)
        blocking_detail: >
          A2 (ExfilSquad<->breach linkage) is Test-class but MATERIAL, not critical, to the finding: the breach
          fact (A1) is Sound and stands on its own, so A2 does not block awareness-level publication. It WOULD
          block any assessment that names an actor or asserts scope. Resolving test: direct retrieval of the ADI
          SEC filing + monitoring for a credible source (or ADI) tying ExfilSquad to the disclosed breach.
        test_required: "Retrieve the ADI SEC filing; watch for scope/data-type disclosure and any credible ExfilSquad<->breach linkage before any actor or scope claim is made."
      recommended_wep_after_test:
        breach_fact: likely                       # unchanged; SEC-filing + 3 outlets, single-source-veto capped
        if_exfilsquad_linkage_confirmed: likely   # actor claim becomes sourced; still capped by veto until independent scope basis
        if_exfilsquad_linkage_refuted: "drop the ExfilSquad thread; breach-fact finding stands alone"

# Orchestrator / watchlist flag
watchlist_consideration:
  raised_by: collector
  question: "Does the semiconductor-supply-chain angle (ADI is a major supplier into aerospace/defense systems) warrant a watchlist entry?"
  grader_note: "Surfaced for orchestrator decision. This finding does NOT add a watchlist entry (grader has no write scope for watch-config); it records the question."

# Lifecycle
tlp: CLEAR
published_in_briefs: [2026-07-30-afternoon]
retracted: false
retraction_brief_id: null
---

# Analog Devices discloses SEC-filed data breach — files exfiltrated, operations reportedly unaffected; ExfilSquad leak-site claim unconfirmed

## Summary

Analog Devices (ADI), a major U.S. semiconductor firm, disclosed in an SEC filing that an unauthorized party accessed some systems and exfiltrated certain files, with the breach detected on 2026-06-23. ADI states business operations were not affected, does not anticipate material financial impact, engaged external cybersecurity experts, and notified law enforcement; the type of data compromised is not yet detailed. The disclosure was reported by three publisher-independent outlets in-window (SecurityWeek 07:16 EDT, BleepingComputer 11:12 EDT, The Record 15:10 EDT). The data-theft/extortion group ExfilSquad initially claimed ADI on its leak site — earlier reporting cited a 570,000-record claim — then delisted the company, but the connection between that claim and the SEC-filed breach is unconfirmed. Graded B2 (three B-grade outlets relaying one un-retrieved SEC filing — single effective evidence basis); single-source veto caps the assessment at "likely." Awareness/monitoring item: DIB-supply-chain-adjacent, but no defense/aerospace customer or product is named, and there is no tracked actor, CVE, or atomic IOC.

## Grade rationale

- **Source B** — BleepingComputer (B) anchor, with SecurityWeek (provisional B) and The Record (B) as additional outlets; the underlying ADI SEC filing (A-class self-disclosure) was not directly retrieved.
- **Credibility 2** — the fact-of-disclosure is near-certain (legally-accountable SEC filing) and coherent, but three outlets share one document basis and the substance/actor is undetailed/unconfirmed -> cannot reach 1.
- **Single-source veto applied** — one effective evidence basis -> WEP held at "likely."

## Sources

### BleepingComputer — Bill Toulas (bleepingcomputer, digraph: B)

- URL: https://www.bleepingcomputer.com/news/security/analog-devices-discloses-data-breach-says-operations-unaffected/
- Published: 2026-07-30T11:12 EDT
- Key claim: ADI disclosed a data breach in an SEC filing; unauthorized access + file exfiltration; operations unaffected.

### SecurityWeek — Eduard Kovacs (securityweek, digraph: B provisional)

- URL: https://www.securityweek.com/
- Published: 2026-07-30T07:16 EDT
- Key claim: Semiconductor firm Analog Devices disclosed a breach (earliest in-window outlet).

### The Record — Recorded Future News (the-record, digraph: B)

- URL: https://therecord.media/analog-devices-semiconductor-company-data-breach
- Published: 2026-07-30T15:10 EDT
- Key claim: ADI breach disclosure; notes the ExfilSquad claim and that its connection to the SEC-filed breach is unclear.

## Technical detail

No technical indicators were published: the relays carry no domains, IPs, hashes, malware names, or CVE. The intrusion is characterized only as unauthorized system access + file exfiltration, detected 2026-06-23, with scope still under investigation. ExfilSquad is described as a data-theft/extortion group that does not deploy file-encryption; its leak-site listing (earlier cited at 570,000 records) was subsequently delisted, a pattern often consistent with ransom negotiation — but the linkage to the SEC-filed breach is unconfirmed. The "570,000 records" figure is a breach-scope claim, not credential values; no credentials stored (Hard Rule 7).

## IOCs surfaced

```yaml
atomic_iocs: []                          # no domains, IPs, hashes, or malware names in any relay
breach_scope_claim:
  records_claimed: 570000                # ExfilSquad leak-site claim (since delisted); UNCONFIRMED; scope-claim only, not credential values
  claim_status: unconfirmed
credential_exposure_detected: false      # Hard Rule 7 — scope claim only, no credential values present
```

## Relationship to existing findings

Net-new. No overlap with the other 2026-07-30 findings (Cisco FMC 0001, VMware 0002, TeamCity 0003, China-nexus AI mass-exploitation 0004, DPRK 0005/0006). First Archimedes finding on Analog Devices; first ExfilSquad reference in the corpus (non-roster). Thematically related to the broader semiconductor-/DIB-supply-chain awareness thread (cf. the ADI watchlist question raised for the orchestrator).

## A&D relevance

DIB-supply-chain-adjacent. ADI is a major semiconductor supplier whose components are used in aerospace/defense systems, so a confirmed breach at ADI is worth awareness on supply-chain-exposure grounds. However, no defense/aerospace customer or product is named, no controlled technical data is implicated in the public reporting, and there is no tracked actor, CVE, or atomic IOC. Relevance is structural (semiconductor-into-A&D), not a named-prime or named-program compromise. The orchestrator flag on whether semiconductor-supply-chain warrants a watchlist entry is recorded above.

## Analytic notes (from analyst review)

KAC applied; ACH declined (run analyst-20260730-164000). The finding splits cleanly into a confirmed core and an unconfirmed graft. The core — ADI disclosed a breach (file exfiltration, detected 2026-06-23, operations reportedly unaffected) — is Sound: a legally-accountable SEC filing relayed by three publisher-independent outlets. That is publishable as a monitoring item.

The graft is the ExfilSquad connection. KAC scores the ExfilSquad-to-SEC-breach linkage as the one Test-class assumption (low confidence, explicitly unconfirmed in every relay, contradicted by the relays' own "connection unclear" language). Critically it is Material, not Critical, to the finding: the breach fact stands without it, so it does not block awareness-level publication — but it fully blocks any actor or scope claim. The briefer must present the breach as confirmed and ExfilSquad as an unverified, since-delisted self-claim of uncertain connection (Hard Rule 2). The "~570,000 records" figure and the delist-as-negotiation read are both unverified. A&D relevance is structural (semiconductor-into-A&D); no DIB customer, product, or controlled data is named. Resolving test: retrieve the SEC filing and watch for a data-type/scope disclosure. Grade unchanged at "likely"; recommend monitoring-surface placement, not an action item.

## Open questions for analyst

- **ExfilSquad linkage (Hard Rule 2).** Is the ExfilSquad leak-site claim connected to the SEC-filed breach? Explicitly unconfirmed in all relays — do not harden. The delist-after-claim pattern is suggestive of negotiation but not dispositive.
- **Scope/data type.** ADI has not detailed the compromised data types; a follow-up disclosure could materially change relevance (e.g., if design/product/DIB-customer data is implicated).
- **Unrelated cybersecurity matter.** ADI separately noted an unrelated cybersecurity matter (~2026-07-26) — track whether the two are actually distinct.
- **Direct retrieval.** ADI SEC filing not retrieved — retrieval would firm the disclosure specifics and could establish an independent documentary basis.
