---
finding_id: finding-2026-07-06-0001
created_at: 2026-07-06T16:56:00-04:00
graded_by: grader
grading_run_id: flash-sweep-20260706-162900
grading_mode: flash_fast_path

# Core grading (from admiralty-grading skill output)
digraph: A2
source_reliability:
  grade: A
  source_name: Check Point Research (via The Hacker News)
  source_yaml_id: checkpoint-research
  grade_rationale: >
    Check Point Research is a Tier-1 vendor research practice (dedicated threat
    research team, first-party telemetry, named-analyst bylines, long APT/C2
    tracking track record). NOT yet in source-grades.yaml — assigned provisional
    A per the established first-surface Tier-1-vendor-research precedent
    (Bitdefender / Symantec / Darktrace / Cisco Talos / SentinelOne). The Hacker
    News (provisional B) is a PURE RELAY here — CPR is the sole originating
    primary; CPR primary NOT directly retrieved this sweep.
  provisional: true
  awaiting_direct_retrieval: true
credibility:
  grade: 2
  checklist_passed:
    - probably_true_ttp_consistent          # new MOIS-affiliated .NET modular C2 framework consistent with Iranian MOIS ecosystem (MuddyWater / OilRig tradecraft space)
    - probably_true_no_contradicting_ab     # no contradicting A/B source
    - probably_true_claims_coherent         # tooling description (mature modular .NET C2), targeting (Israel primary, Egypt/UAE), and exploited-CVE set internally coherent
  grade_1_withheld_reason: >
    Grade 1 requires independent corroboration. CPR is the sole originating
    primary; The Hacker News is a rewrite of CPR, not independent corroboration
    (per INTEL-GRADING: a media outlet summarizing a Tier-1 firm is not a second
    source). Single-source → credibility capped at 2.
  rationale: >
    CPR documents a previously-undocumented modular .NET C2 framework (Cavern /
    Cav3rn) used against Israeli IT-providers and government, and designates a
    NEW cluster "Cavern Manticore" it assesses as MOIS-affiliated with tactical
    overlaps to MuddyWater and Lyceum (OilRig subgroup). Claim is consistent with
    established Iranian MOIS tradecraft and internally coherent.
corroboration:
  independent_sources:
    - checkpoint-research         # sole originating primary
  independent: false
  test_passed: >
    FAILS independence test. The Hacker News is a rewrite/relay of Check Point
    Research — remove CPR and THN does not stand on its own evidence. One
    effective source.
first_party_precedence:
  applied: false
  splunk_evidence: null
  splunk_note: >
    13 IOCs extracted (1 C2 domain hospitalinstallation[.]com + 7 DLL filenames
    + 5 exploited CVEs). First-party sentinel query recommended at librarian/next
    sweep; not run in this fast-path. Silent Splunk would not disconfirm
    (Hard Rule 8). Frank is not an Israeli/Egyptian/UAE IT-provider or government
    org matching the victim profile — visibility-bounded, not negative evidence.
single_source_veto_applied: true
single_source_veto_note: >
  CPR sole primary (THN is relay). Single-source veto caps WEP at "likely"
  regardless of CPR's A letter grade.
wep_ceiling: likely
wep_ceiling_rationale: >
  A2 with single-source veto → WEP capped at "likely." Lifts on independent
  second-IR-vendor corroboration of the Cavern framework and/or the Cavern
  Manticore cluster designation (Mandiant / CrowdStrike / Unit 42 / MSTIC /
  Microsoft), or direct retrieval of the CPR primary.

# FLASH adjudication — does NOT ship as a FLASH
flash:
  clears_flash_bar: false
  b2_minimum_met: true                     # A2 exceeds B2 grade floor...
  ships_as_flash: false                    # ...but NO FLASH TRIGGER is genuinely met
  trigger_fired: null
  trigger_evaluation:
    trigger_2_new_attribution_tracked_actor:
      met: false
      reason: >
        Cavern Manticore is a NET-NEW cluster, NOT in _roster.yaml. CPR's noted
        tactical overlaps with MuddyWater (#022) and Lyceum/OilRig (#023) are
        CPR's assessment of overlap — NOT an attribution to a tracked roster
        actor. Hard Rule 2 BINDING: Archimedes does NOT cross-walk a distinct
        CPR-designated cluster onto a roster actor. No tracked-actor attribution
        exists → Trigger 2 does not fire.
    trigger_4_tracked_actor_ttp_change:
      met: false
      reason: >
        The Cavern .NET modular C2 framework is genuinely new tooling from an
        A-class source, but Trigger 4 requires the new TTP be "clearly
        attributable to a tracked actor." Cavern Manticore is not a tracked
        actor; attributing the tooling to MuddyWater/OilRig would require
        accepting CPR's overlap as roster-attribution, which Hard Rule 2 forbids.
        Recorded as a TTP-change WATCH, not a fired trigger.
    trigger_5_ad_sector_campaign:
      met: false
      reason: >
        Aviation is named among targeted sectors, but no A&D-prime watchlist
        entity is named; victims are Israeli/Egyptian/UAE IT-provider and
        government orgs — not A&D-prime direct targeting and not A&D-sector-
        anchored. Marginal fail.
  disposition: >
    Promoted to the corpus as a standard graded finding (A2, well above the C3
    monitoring floor) — Iran Cyber Watch HIGH, strong actor-profiler substrate —
    but ships as NO FLASH because no FLASH trigger is met. Feeds the next
    scheduled brief and the /new-actor Cavern Manticore operator-deferred queue.

# Inclusion eligibility (from admiralty-grading)
inclusion:
  eligible_for:
    - daily_brief_action
    - weekly_synthesis
    - actor_profile_update                 # as a /new-actor candidate, operator-deferred
  not_eligible_for:
    - flash                                # no trigger met (grade floor met, trigger not)

# Cluster metadata
cluster:
  topic: "Cavern (Cav3rn) modular .NET C2 framework — CPR-designated new cluster 'Cavern Manticore' (MOIS-affiliated) vs. Israeli/Egyptian/UAE orgs"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-07-06-flash-1629-002
  attribution_claims:
    - claimed_actor: "Cavern Manticore (NEW cluster — NOT in _roster.yaml)"
      claimed_by_sources: [checkpoint-research]
      attribution_language: >
        "affiliated with Iran's Ministry of Intelligence and Security (MOIS);
        tactical overlaps with MuddyWater and Lyceum (Lyceum assessed by CPR as
        an OilRig subgroup)" — preserved verbatim as CPR's assessment.
      is_new_cluster: true
      roster_match: false
      hard_rule_2_binding: true
      hard_rule_2_note: >
        CPR designates Cavern Manticore a DISTINCT new cluster. Archimedes does
        NOT originate a cross-walk to MuddyWater (#022) or APT34/OilRig (#023)
        despite CPR's noted overlaps. The overlap claim is recorded as CPR's
        language; Archimedes asserts no roster attribution. Analyst to assess
        attribution-by-inference; grader does not.
      requires_analyst_review: true

# New-actor candidacy
new_actor_candidate:
  name: "Cavern Manticore"
  status: operator_deferred
  hard_rule_2_binding: true
  note: >
    Strong /new-actor Cavern Manticore candidacy (MOIS-affiliated Iranian
    cluster, new .NET modular C2 framework, aviation among targets — Iran Cyber
    Watch HIGH). Operator-deferred per /new-actor requiring human approval.
    Do NOT cross-walk to #022 / #023.

# Source-grade additions proposed (librarian to add to source-grades.yaml)
source_grade_additions_proposed:
  - source_yaml_id: checkpoint-research
    proposed_name: "Check Point Research (CPR)"
    proposed_grade: A
    provisional: true
    awaiting_direct_retrieval: true
    grade_note: >
      First Archimedes-corpus dedicated source ID. Tier-1 vendor research
      practice — provisional A per the first-surface precedent applied to
      Bitdefender / Symantec / Darktrace / Cisco Talos / SentinelOne. This
      surface: relayed via The Hacker News; CPR primary NOT directly retrieved.
      72h ratification clock; pending direct retrieval AND human ratification.
    first_cited: finding-2026-07-06-0001

# Downstream handoff flags
analyst_review_required: true              # attribution claim present (Cavern Manticore new-cluster + MOIS + MuddyWater/OilRig overlap)
red_team_review_required: false           # WEP "likely" < "very likely"
red_team_review: null
analysis_sections:
  sat_ach: null
  sat_kac: null

# Lifecycle
tlp: CLEAR
published_in_briefs: []
retracted: false
retraction_brief_id: null
---

# Check Point Research documents a new modular .NET C2 framework ("Cavern") and attributes it to a new MOIS-affiliated cluster it names "Cavern Manticore"

## Summary

Check Point Research (relayed by The Hacker News) documents a previously
undocumented modular command-and-control framework, Cavern (aka Cav3rn), built
on a shared .NET foundation and used against Israeli organizations — primarily
IT providers and government. CPR attributes the activity to a NEW cluster it
designates Cavern Manticore, which it assesses as affiliated with Iran's
Ministry of Intelligence and Security (MOIS) and as sharing tactical overlaps
with MuddyWater and Lyceum (an OilRig subgroup per CPR). CPR nonetheless
designates Cavern Manticore as a distinct new cluster. Archimedes records CPR's
attribution and overlap language verbatim and does NOT cross-walk the cluster to
any tracked roster actor (Hard Rule 2).

## Sources

### Check Point Research (checkpoint-research, provisional digraph: A) — PRIMARY (relay-conveyed)

- URL (relay): https://thehackernews.com/2026/07/iran-linked-hackers-use-new-cavern-c2.html
- Published (relay): 2026-07-06T14:34:26-04:00
- Key claim: New Cavern .NET modular C2 framework; new MOIS-affiliated cluster
  "Cavern Manticore" with tactical overlaps to MuddyWater and Lyceum/OilRig.

### The Hacker News (thehackernews, digraph: B) — RELAY (not independent corroboration)

- Rewrite of the CPR research; does not stand on independent evidence.

## Technical detail

- **Cavern (Cav3rn):** newly documented modular C2 framework — CPR describes it
  as "a mature and adaptable toolset built around a shared .NET foundation"
  (paraphrased; <15 words if quoted).
- **Targeted sectors:** IT providers, government, aviation, energy, public sector.
- **Targeted countries:** Israel (primary), Egypt, United Arab Emirates.
- **Named victims:** none identified.
- **Exploited CVEs (per CPR, by ID only — Hard Rule 3):** CVE-2025-52691,
  CVE-2025-68613, CVE-2025-9316, CVE-2025-34291, CVE-2025-54068.

## IOCs surfaced

- Domain (C2): hospitalinstallation[.]com
- Filenames (sideloaded/malicious DLLs): uxtheme.dll, n-HTCommp.dll, mhm.dll,
  db.dll, ode.dll, n-ten.dll, n-sws.dll
- CVEs exploited by actor: CVE-2025-52691, CVE-2025-68613, CVE-2025-9316,
  CVE-2025-34291, CVE-2025-54068
- (13 IOCs total; recommend first-party sentinel query at librarian/next sweep.)

## Relationship to existing findings

- Iranian MOIS cluster space overlaps thematically with MuddyWater (#022) and
  APT34/OilRig (#023) tracking, but CPR designates Cavern Manticore a DISTINCT
  new cluster — no roster cross-walk originated (Hard Rule 2). Analyst to assess
  whether the CPR overlap supports attribution-by-inference.

## Open questions for analyst

- **Attribution (SAT-ACH candidate):** CPR asserts a new MOIS-affiliated cluster
  with MuddyWater/OilRig overlaps. Is Cavern Manticore a genuinely distinct
  cluster, a MuddyWater/OilRig sub-cluster, or a re-labeling? Grader does not
  resolve — analyst assesses. Hard Rule 2 binds: no origination of roster
  cross-walk.
- **/new-actor Cavern Manticore** — operator-deferred candidacy; Iran Cyber Watch
  HIGH. Awaits human approval.
- **Corroboration tripwire:** independent second-IR-vendor confirmation
  (Mandiant / CrowdStrike / Unit 42 / MSTIC / Microsoft) of the Cavern framework
  or the Cavern Manticore designation lifts WEP from "likely" and would resolve
  the single-source veto.
- **Direct retrieval:** CPR primary not retrieved this sweep — flag for collector.
