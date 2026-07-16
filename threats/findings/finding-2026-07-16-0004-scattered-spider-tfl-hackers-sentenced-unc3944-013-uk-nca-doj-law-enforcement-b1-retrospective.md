---
finding_id: finding-2026-07-16-0004
created_at: 2026-07-16T16:24:00-04:00
graded_by: grader
grading_run_id: afternoon-20260716-160000

# Core grading (from admiralty-grading skill output)
digraph: B1
source_reliability:
  grade: B
  source_name: "BleepingComputer (primary body) + SecurityWeek + The Record (three publisher-independent relays)"
  source_yaml_id: bleepingcomputer
  grade_rationale: >
    Body anchored on BleepingComputer (source-grades.yaml grade B, fast/accurate on
    ransomware and cybercrime), corroborated by SecurityWeek (B, provisional) and The
    Record (B). The underlying evidence basis is the public court sentencing plus
    on-record statements from UK National Crime Agency, City of London Police, and the
    U.S. Department of Justice — official law-enforcement authorities, not the three
    newsrooms.
  provisional: false
credibility:
  grade: 1
  checklist_passed:
    - confirmed_independent_source
    - confirmed_neither_cites_other
    - confirmed_artifacts_match
    - confirmed_no_contradicting_higher_grade
  rationale: >
    This is a CONFIRMED public-record legal event, not a predictive CTI assessment. Two
    named defendants (Jubair, Flowers) were sentenced in a UK court under the Computer
    Misuse Act following guilty pleas, with parallel U.S. DOJ charges. The primary
    evidence basis is multiple mutually-independent official authorities — UK NCA, City
    of London Police, and U.S. DOJ — each confirming the same procedural facts, relayed
    by three publisher-independent B-grade newsrooms whose procedural details (names,
    ages, sentence length, victim, dates, financial impact) match. No higher-grade source
    contradicts. Adjudicated fact via guilty plea clears grade 1.
  grade_1_basis_note: >
    Conservative alternative reading: treat the three newsrooms as relays of one press
    event (the sentencing) -> single evidence basis -> B2 (Probably True). Disposition is
    IDENTICAL under either grade: retrospective monitoring-tier / actor-profile item, no
    forward WEP, not FLASH, not an action item. Anchored at B1 because the confirmation
    rests on multiple independent OFFICIAL authorities (NCA/City of London Police/DOJ)
    plus an open-court guilty plea, which is the confirmation standard for an adjudicated
    public-record event.
corroboration:
  independent_sources:
    - uk-national-crime-agency
    - city-of-london-police
    - us-department-of-justice
  independent: true
  test_passed: >
    The three official authorities (UK NCA, City of London Police, U.S. DOJ) are
    mutually independent institutions confirming the same adjudicated outcome; three
    B-grade newsrooms independently relay it without citing each other. For a public
    court sentencing this constitutes confirmation of the EVENT.
first_party_precedence:
  applied: false
  splunk_evidence: null
  rationale: >
    No atomic IOCs in the item (iocs_count: 0) — retrospective law-enforcement /
    sentencing content, no domains/IPs/hashes to query against defenseclaw_local /
    archimedes. No first-party check performable. Absence of queryable indicators is not
    disconfirming.
single_source_veto_applied: false
single_source_veto_note: >
  N/A — the single-source veto governs FORWARD-looking WEP ceilings. This finding
  reports a confirmed past event (a sentencing that occurred), so no predictive WEP is
  asserted and the veto does not bind. Multiple independent official authorities confirm
  regardless.
wep_ceiling: n/a
wep_ceiling_note: "Retrospective confirmed event; no predictive/estimative claim made."

# Cluster metadata
cluster:
  topic: "Scattered Spider (#013 / UNC3944) — UK sentencing of two members for the Aug 2024 Transport for London attack; parallel US DOJ charges"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-07-16-pm-001
  attribution_claims:
    - claimed_actor: Scattered Spider
      roster_id: "013"
      aliases_in_source: ["Scattered Spider cybercrime collective"]
      claimed_by_sources: [uk-national-crime-agency, us-department-of-justice]
      confidence_language: "convicted — guilty plea under the Computer Misuse Act"
      novelty: adjudicated_of_record
      requires_analyst_review: false
      note: >
        Attribution is ADJUDICATED (guilty plea in open court), not a novel CTI
        attribution and not originated by Archimedes (Hard Rule 2 satisfied). No ACH/SAT
        assessment is warranted for an adjudicated conviction. Downstream owner is
        actor-profiler (dossier #013 update), not the analyst.

# Inclusion eligibility (from admiralty-grading)
inclusion:
  eligible_for:
    - daily_brief_monitoring
    - weekly_synthesis
    - actor_profile_update
  not_eligible_for:
    - flash
  eligibility_note: >
    Clears B2 action threshold on grade, but content is retrospective law-enforcement
    with no new TTP / IOC / targeting -> carried as MONITORING, not an action item. Not
    FLASH (no forward threat, no A&D nexus, retrospective). Primary downstream value is
    the actor dossier.

# Downstream handoff flags
analyst_review_required: false
analyst_review_rationale: >
  No forward WEP (retrospective event) and the sole attribution is adjudicated of-record
  -> no SAT/ACH work required. Deviation from a mechanical "attribution-present -> analyst"
  read is deliberate and documented: a guilty-plea conviction needs no analytic
  assessment.
red_team_review_required: false
red_team_review: null
actor_profiler_handoff: true
actor_profiler_note: >
  actor-profiler should log this as a law-enforcement disruption event on dossier #013
  (Scattered Spider): two members sentenced (Jubair 5.5y, Flowers 5.5y), guilty pleas,
  ~£29M TfL loss, DOJ charges spanning ~120 breaches, Flowers implicated in Sutter Health
  + SSM Health intrusions. No new TTP; update the operational-history / disruptions
  section.
analysis_sections:
  sat_ach: null
  sat_kac: null

# Lifecycle
tlp: CLEAR
published_in_briefs: [2026-07-16-afternoon]
retracted: false
retraction_brief_id: null
---

# Two Scattered Spider (#013 / UNC3944) members sentenced to 5.5 years each in the UK for the 2024 Transport for London attack

## Summary

A UK court sentenced two members of the Scattered Spider cybercrime collective — Thalha
Jubair (20) and Owen Flowers (18) — to five years and six months each for the August 2024
cyberattack on Transport for London (TfL), following guilty pleas under the Computer
Misuse Act. UK authorities (National Crime Agency, City of London Police) called it the
country's largest cyber crime case to date; the U.S. Department of Justice brought
parallel charges. This is a retrospective, adjudicated law-enforcement development on a
tracked actor (Archimedes roster #013) — no new tooling, targeting, or exploitation TTP
is disclosed.

## Sources

### BleepingComputer (bleepingcomputer, digraph: B)

- URL: https://www.bleepingcomputer.com/news/security/scattered-spider-members-behind-transport-for-london-hack-get-five-years-in-prison/
- Published: 2026-07-16T12:31:29+00:00
- Key claim: Two Scattered Spider members sentenced to 5.5 years for the TfL attack; guilty pleas under the Computer Misuse Act; parallel DOJ charges.

### SecurityWeek (securityweek, digraph: B — provisional)

- URL: https://www.securityweek.com/two-scattered-spider-hackers-sentenced-to-jail-in-uk/
- Published: 2026-07-16T13:21:12+00:00
- Key claim: Independent relay confirming the same sentencing, defendants, and sentence length.

### The Record (the-record, digraph: B)

- URL: https://therecord.media/scattered-spider-hackers-tfl-sentenced
- Published: 2026-07-16T12:00:00+00:00
- Key claim: Independent relay confirming the sentencing and NCA/DOJ law-enforcement framing.

## Technical detail

No technical exploitation content. The reporting is procedural / law-enforcement:

- Primary victim: Transport for London. The breach rendered 148 systems inoperable and
  disrupted Dial-a-Ride, concessionary travel cards, contactless/digital payments, and
  refund processing; ~27,000 employees were required to reset passwords in person. Stolen
  customer data included names, addresses, and contact details.
- Financial impact: ~£29M in TfL losses/recovery costs. UK authorities estimated a
  potential ~£56B economic loss had a full network shutdown succeeded. Jubair and
  accomplices reportedly extorted over $115M from victims worldwide (Aug 2024 – Jul 2025).
- Additional victims: Flowers implicated in intrusions against U.S. healthcare providers
  Sutter Health and SSM Health Care Corporation. Jubair charged by DOJ with involvement in
  ~120 network breaches affecting dozens of U.S. organizations, including critical
  infrastructure and courts.
- Timeline: breach Aug 2024; TfL disclosure 2 Sep 2024; arrests 16 Sep 2024; sentencing
  Jul 2026.

Scattered Spider's known tradecraft (help-desk / SIM-swap social engineering, Okta and
M365 identity abuse, MFA-fatigue) remains directly relevant to the A&D target profile's
identity and help-desk attack surface, even though this specific sentencing discloses no
new technique.

## IOCs surfaced

None. `iocs_count: 0` — no atomic network indicators, hashes, or CVEs in the reporting.
Named individuals (Jubair, Flowers) are recorded as adjudicated public-record convicts,
name + age only, per LEGAL-POLICY GDPR data-minimization (official law-enforcement
context). No credentials stored — the 27,000-password-reset detail is a procedural fact,
not credential values (Hard Rule 7).

## Relationship to existing findings

No prior Archimedes finding covers the TfL incident directly; this is a new development on
the standing roster entry #013 (Scattered Spider), tracked HIGH since 2026-04-09. Feeds the
dossier's operational-history / law-enforcement-disruption record.

## Open questions for analyst

None requiring SAT/ACH. The attribution is adjudicated (guilty plea), so no analytic
assessment is warranted. The one downstream action is an actor-profiler dossier update on
#013 (see `actor_profiler_note`). Optional watch item: whether the sentencing prompts any
observable near-term shift or fragmentation in Scattered Spider operational tempo — a
question for future collection, not this finding.
