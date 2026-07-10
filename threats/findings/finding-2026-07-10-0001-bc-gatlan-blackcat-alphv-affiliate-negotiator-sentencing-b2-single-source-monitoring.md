---
finding_id: finding-2026-07-10-0001
created_at: 2026-07-10T08:14:00-04:00
graded_by: grader
grading_run_id: morning-20260710-080000

# Core grading (from admiralty-grading skill output)
digraph: B2
source_reliability:
  grade: B
  source_name: BleepingComputer (Sergiu Gatlan) — relaying U.S. federal court sentencing (DOJ-class primary)
  source_yaml_id: bleepingcomputer
  grade_rationale: >
    Pre-assigned B per source-grades.yaml ("Fast and accurate on CVEs/ransomware, sometimes light on
    context"). The underlying event is a public U.S. federal court sentencing — a DOJ-class primary of
    record — but the DOJ press release / court docket was NOT retrieved this sweep. The effective
    in-window source is the single B-grade BleepingComputer relay.
  provisional: false
credibility:
  grade: 2
  checklist_passed:
    - probably_true_consistent_known_actor_landscape_and_le_timeline
    - probably_true_no_contradicting_ab
    - probably_true_claims_internally_coherent
  rationale: >
    Grade 1 fails — no independent in-window corroboration retrieved (single BleepingComputer relay;
    DOJ/docket primary not pulled this sweep). Grade 2 met: the reported facts are consistent with the
    well-documented BlackCat/ALPHV public record (RaaS affiliate model, ~20% revenue split,
    $300M+ from 1,000+ victims through Sept 2023) and with a coherent LE timeline (Oct 2025 indictment,
    March 2026 name unseal, July 2026 sentencing); no contradicting A/B-grade source exists; ransom
    figures, roles, and dates are internally coherent. Retrospective law-enforcement outcome, not a
    contested or extraordinary claim. Graded 2 (Probably True), erring low per doctrine (not 1 — single
    effective source, primary not retrieved).
corroboration:
  independent_sources:
    - bleepingcomputer
  independent: false
  test_passed: >
    FAILS independence test — one effective in-window source (BleepingComputer relaying the federal
    sentencing). The DOJ press release and court docket are corroboratable upstream primaries, but no
    SECOND independent evidence basis was retrieved this window. Single-source veto applies.
first_party_precedence:
  applied: false
  splunk_evidence: null
  note: >
    No network/file IOCs published (no domains, IPs, hashes, wallets, or CVEs in source). Nothing to hunt.
    Collector confirmed first-party Splunk clean this sweep (0 external hits, pre-brief-20260710-073000).
    Absence of a hunt is not disconfirmation (Rule 8 satisfied — no matchable indicator exists).
single_source_veto_applied: true
wep_ceiling: likely

# Cluster metadata
cluster:
  topic: "BlackCat/ALPHV affiliate-negotiator sentencing — former DigitalMint IR-firm insiders sentenced (Martino 70 months; two co-conspirators 4 years each) for 2023–2025 extortion"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-07-10-am-001
  attribution_claims:
    - claimed_actor: "BlackCat / ALPHV"
      roster_id: "020"
      claimed_by_sources: [bleepingcomputer]
      claim_type: court_procedural_characterization
      requires_analyst_review: true
      note: >
        Source (relaying U.S. federal proceedings) characterizes the three sentenced individuals as
        "BlackCat (ALPHV) affiliates" on a 20% revenue split with BlackCat administrators. This is
        adjudicated/procedural legal language, NOT a novel technical campaign attribution and NOT
        Archimedes-originated (Hard Rule 2 preserved). No SAT/ACH decomposition needed; analyst review
        is light-touch (confirm no origination; route dossier note). Actor-profiler is the more natural
        downstream — see actor_profiler_handoff.

# Inclusion eligibility (from admiralty-grading)
inclusion:
  eligible_for:
    - daily_brief_monitoring
    - weekly_synthesis
    - actor_profile_update
    - daily_brief_action     # clears the B2 grade floor
  not_eligible_for:
    - flash                  # grade clears B2 but NO FLASH trigger fires: LE outcome, no active exploitation, no tracked CVE, no new attribution-to-tracked-actor, no A&D watchlist hit
  disposition_note: >
    Grade clears B2, but operationally this is a MONITORING-tier / actor-landscape awareness item, not
    an action item: retrospective law-enforcement sentencing of rogue-insider affiliates, no IOCs, no
    A&D-sector victim named, no new campaign activity. Primary value is as a BlackCat (#020) dossier
    note (insider-threat / affiliate-economics / LE-pressure angle) and ransomware-landscape context.

# Downstream handoff flags
analyst_review_required: true    # attribution claim present (procedural court characterization) — light-touch review only; WEP ceiling "likely" (< very likely)
red_team_review_required: false  # WEP ceiling "likely" (< very likely)
red_team_review: null
analyst_review_complete: true
analyst_review_run_id: analyst-20260710-081500
wep_ceiling_adjusted: null          # no change — light-touch review confirms grader's "likely" is correct
assessment_blocked_pending_test: false
analysis_sections:
  sat_ach: null                     # NOT applied — settled/adjudicated fact, not a contested attribution; no competing-hypothesis space to decompose (would be retrofitting)
  sat_kac:
    kac_analysis:
      assessment_under_review: >
        Three former DigitalMint IR-firm insiders were sentenced in U.S. federal court for operating as
        BlackCat/ALPHV affiliate negotiators (Martino 70 months; two co-conspirators 4 years each),
        April 2023–April 2025, on a ~20% revenue split — carried B2 / WEP "likely" at monitoring tier.
      analyzed_at: 2026-07-10T08:16:30-04:00
      analyzed_by: analyst
      invoking_context: >
        grader_handoff — analyst_review_required set ONLY because cluster.attribution_claims carries a
        court_procedural_characterization ("BlackCat affiliates"). Light-touch: this is adjudicated legal
        fact relayed with citation, not an Archimedes analytic attribution. No full ACH/KAC decomposition
        warranted for a settled LE outcome.
      assumptions:
        - id: A1
          statement: >
            The "BlackCat/ALPHV affiliate" label attaches to these individuals as a court/DOJ-established
            characterization, not as an Archimedes inference.
          confidence: high
          centrality: critical
          classification: sound
          rationale: >
            Directly stated by the cited source relaying the federal proceeding. Hard Rule 2 test passed:
            the rank-relevant attribution originates with the court/DOJ and BleepingComputer, not with
            Archimedes. The finding relays and cites; it does not originate. No test needed.
        - id: A2
          statement: >
            The single B-grade relay accurately reports the sentences, dates, roles, and revenue split.
          confidence: medium
          centrality: material
          classification: qualify
          rationale: >
            Single effective in-window source; DOJ press release / court docket not retrieved this sweep.
            Already correctly handled — single-source veto caps WEP at "likely" and the grade is B2. The
            qualifier is structural, not load-bearing on the assessment's tier. Optional enrichment (pull
            DOJ primary) would lift corroboration if carried into weekly synthesis; not blocking.
        - id: A3
          statement: >
            This item implies no new/ongoing BlackCat campaign activity and no A&D-sector nexus.
          confidence: high
          centrality: material
          classification: sound
          rationale: >
            Retrospective sentencing; named victims are financial-services, nonprofit, school districts,
            medical, and law firms — no A&D victim. Finding correctly scopes ad_relevance: low and does not
            overstate. The one transferable point (insider-threat at a retained IR/negotiation vendor) is a
            generic third-party/supply-chain trust consideration, proportionately flagged, not inflated.
      classifications_summary:
        sound: 2
        qualify: 1
        test: 0
        unsupported: 0
      remediation:
        status: proceed
        qualifying_caveats:
          - "Single-source (A2): already reflected in B2 grade + 'likely' cap. Optional DOJ-primary enrichment for weekly synthesis, non-blocking."
          - "Scope discipline (A3): keep as monitoring-tier BlackCat #020 landscape note; do not read as new campaign activity or A&D targeting."
      recommended_wep_after_test:
        wep: likely
        changed: false
        note: "No test required (0 Test classifications). Grader's 'likely' stands unchanged."

# A&D relevance (structural)
ad_relevance: low
ad_relevance_rationale: >
  LOW. No aerospace/defense-sector victim is named or described (named/described victims are
  financial-services, a nonprofit, school districts, medical facilities, and law firms). The one
  transferable structural lesson is the INSIDER-THREAT vector: the sentenced individuals were employees
  of a cybersecurity incident-response firm (DigitalMint / Sygnia-linked in the reporting) who
  moonlighted as ransomware affiliates and, per prosecutors, leaked victims' insurance-limit and
  negotiation-position data. That trusted-insider-at-a-security-vendor pattern is a generic
  supply-chain/third-party-risk consideration relevant to any org (including A&D primes) that retains
  external IR/negotiation firms — but there is NO A&D nexus, no sector targeting, and no actor campaign
  activity in this item. Do not overstate.

# Actor-profiler handoff (BlackCat #020 — profile pending)
actor_profiler_handoff:
  roster_id: "020"
  actor: "BlackCat / ALPHV"
  dossier: threats/threat-actors/BlackCat/
  dossier_status: profile_pending
  recommended_action: add_landscape_note
  note: >
    Feed to the (pending) BlackCat #020 dossier as a landscape/LE-pressure data point: former DigitalMint
    IR-firm insiders operated as BlackCat affiliates (Apr 2023–Apr 2025, 20% revenue split), sentenced
    July 2026. Reinforces the documented BlackCat affiliate economics ($300M+ / 1,000+ victims through
    Sept 2023). Not a threat-box scoring trigger and not a new attribution — context only. No
    /approve-scoring gate engaged.

# Lifecycle
tlp: CLEAR
published_in_briefs: [2026-07-10-morning]
retracted: false
retraction_brief_id: null
---

# BlackCat/ALPHV affiliate negotiator sentenced to 70 months; two co-conspirators get 4 years each (U.S. federal LE outcome, no A&D victim, no IOCs)

## Summary

BleepingComputer reports that a U.S. federal court sentenced Angelo Martino, a former employee of
incident-response firm DigitalMint, to 70 months in prison for acting as a BlackCat (ALPHV) affiliate
negotiator; two co-conspirators (both linked to Sygnia/DigitalMint in the reporting) received four-year
sentences in May 2026. Per the source, the three ran extortion attacks between April 2023 and April 2025
on a 20% revenue split with BlackCat administrators, and prosecutors allege Martino leaked victims'
insurance-limit and negotiation-position data from his negotiator role. No aerospace/defense victim is
named and no technical IOCs are provided. Graded B2 on a single B-grade relay (the DOJ/docket primary was
not retrieved this sweep); single-source veto caps the assessment at "likely." Carried at the monitoring
tier as a BlackCat (#020) dossier landscape note.

## Sources

### BleepingComputer (bleepingcomputer, digraph letter: B) — relaying U.S. federal sentencing

- URL: https://www.bleepingcomputer.com/news/security/us-ransomware-negotiator-gets-4-years-in-prison-for-blackcat-attacks/
- Byline: Sergiu Gatlan (BleepingComputer), published 2026-07-10
- Underlying primary: U.S. federal court sentencing (DOJ-class) — press release / docket NOT directly retrieved this sweep
- Key claim: A former DigitalMint IR-firm employee was sentenced to 70 months as a BlackCat (ALPHV)
  affiliate negotiator; two co-conspirators received four-year terms; the group ran extortion attacks
  April 2023–April 2025 on a 20% split with BlackCat administrators.

Note on corroboration: one effective in-window source. The DOJ release and court docket are
corroboratable upstream primaries, but no independent second evidence basis was retrieved. Single-source
veto applied (WEP capped at "likely").

## Technical detail

No technical content. This is a law-enforcement sentencing report, not campaign or vulnerability
reporting.

- **No IOCs:** no domains, IPs, hashes, ransom wallets, or CVEs are present in the source (ioc_count=0 by
  content, not by extraction failure).
- **Affiliate economics (reported):** the three operated as BlackCat affiliates on a ~20% revenue split
  with BlackCat administrators. The source frames the broader BlackCat gang as having collected at least
  $300 million from over 1,000 victims through September 2023 — consistent with prior public reporting on
  BlackCat/ALPHV.
- **Insider vector (reported):** the sentenced individuals were employees of a cybersecurity
  incident-response firm; prosecutors allege the negotiator leaked victims' insurance-policy limits and
  negotiation positions. This is the item's one transferable structural lesson (third-party/insider risk
  at retained security vendors) — see A&D relevance in frontmatter.

## Attribution handling (Hard Rule 2)

Archimedes originates nothing here. The "BlackCat (ALPHV) affiliate" characterization is the
source's/court's adjudicated procedural language, reported and cited — not an Archimedes first-time
attribution and not a novel technical campaign attribution. Recorded in `cluster.attribution_claims` as a
`court_procedural_characterization` mapped to roster #020 for actor-profiler awareness. Do not read this
finding as asserting any new campaign activity by BlackCat.

## Analytic notes (from analyst review)

Light-touch KAC only; no ACH. This is an adjudicated law-enforcement outcome, not a contested attribution,
so there is no competing-hypothesis space to decompose — a matrix would be retrofitting. Hard Rule 2 test
passes cleanly: the "BlackCat/ALPHV affiliate" label originates with the court/DOJ and is relayed with
citation by BleepingComputer. Archimedes originates nothing. The rank-relevant attribution was made by a
cited source, so the analysis pressure-tested a sourced claim rather than creating one.

Three assumptions checked: two sound (A1 attribution is court-established, not inferred; A3 no new campaign
activity and no A&D nexus), one qualify (A2 single-source accuracy — already handled by the single-source
veto capping WEP at "likely" and the B2 grade). Zero Test classifications, so nothing blocks. WEP stays at
"likely"; grade unchanged.

The one transferable point for the A&D profile is the insider-threat vector: trusted employees at a
retained IR / ransomware-negotiation vendor moonlighting as affiliates and leaking victims' insurance-limit
and negotiation-position data. That is a generic third-party/supply-chain trust risk relevant to any prime
retaining external IR firms — proportionately flagged, monitoring-tier, no IOCs. Primary downstream is
actor-profiler (BlackCat #020 landscape note), not further analysis.

## IOCs surfaced

None. No network or file indicators, no CVE, no wallet addresses in the source.

## Relationship to existing findings

- No direct prior finding. This is the first BlackCat/ALPHV item in the recent corpus and the first
  content promoted for 2026-07-10.
- Not merged with any 2026-07-09 finding: the GhostLock (finding-2026-07-09-0001), RoguePlanet
  (finding-2026-07-09-0002), and PAN-OS (finding-2026-07-09-0003) findings are all vulnerability/CVE
  items with no shared actor, campaign, or IOC. Distinct clusters.

## Open questions for analyst

Light-touch only — no SAT/ACH required:
- Confirm the attribution note is handled as reported court-procedural language (no Archimedes
  origination). No inference analysis is warranted for an adjudicated LE outcome.
- Primary downstream is actor-profiler, not analyst: route the insider-affiliate / LE-pressure data point
  to the pending BlackCat #020 dossier (see actor_profiler_handoff). No threat-box re-scoring is triggered.
- Optional enrichment (not blocking): pull the DOJ press release / court docket to convert this from a
  single-source B2 to an independently corroborated grade if the item is carried forward in weekly
  synthesis.
