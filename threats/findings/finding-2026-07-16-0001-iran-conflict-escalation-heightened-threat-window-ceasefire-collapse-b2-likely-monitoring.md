---
finding_id: finding-2026-07-16-0001
created_at: 2026-07-16T14:30:00-04:00
graded_by: orchestrator   # on-demand sweep; grader-equivalent inline grading per admiralty-grading skill
grading_run_id: on-demand-iran-sweep-20260716
grading_mode: on_demand

# Core grading (from admiralty-grading skill logic)
digraph: B2
source_reliability:
  grade: B
  source_name: "Conflict cyber-monitor cluster (FDD analysis + Cybersecurity Dive + Flare + SOCRadar + CSIS + SafeBreach)"
  source_yaml_id: null   # multi-source cluster; no single source-grades.yaml id
  grade_rationale: >
    Reliability B (reliable) as an aggregate: the geopolitical facts (Strait of
    Hormuz strikes, CENTCOM response, ceasefire declared over, oil-waiver
    revocation) are corroborated across multiple independent outlets. FDD is a
    think-tank primary (unlisted in source-grades.yaml, would grade low in
    isolation) but the strategic escalation it reports is independently
    reproduced by security-press and vendor conflict monitors. No single vendor
    A-grade cyber report anchors the in-window item.
credibility:
  grade: 2
  checklist_passed:
    - probably_true_no_contradicting_ab   # no A/B source contradicts the escalation facts or the elevated-threat framing
    - probably_true_claims_coherent       # coherent: kinetic escalation historically precedes Iranian hacktivist/IO surges
    - multi_source_geopolitical_corroboration
  grade_1_withheld_reason: >
    Grade 1 withheld: the operative claim is a FORECAST (renewed cyber surge),
    not an observed in-window incident. Primaries only partially retrieved this
    sweep (FDD via search-summary; Flare/CPR/Unit42 pages 403'd or stale —
    Unit 42 brief stamped "Updated April 17"). Probably True, not Confirmed.
corroboration:
  independent_sources:
    - fdd
    - cybersecurity-dive
    - flare
    - socradar
    - csis
    - safebreach
  independent: true
  independence_test_result: >
    The heightened-threat ASSESSMENT is independently made by multiple monitors.
    However, several of those monitors draw on the same historical
    pattern-of-life (Iranian cyber ops timed to kinetic events), so the forecast
    is convergent-assessment, not observation of distinct new incidents.
first_party_precedence:
  applied: false
  splunk_evidence: null
  splunk_note: >
    No Splunk enrichment run — strategic conflict-context item with zero atomic
    IOCs to correlate against defenseclaw_local / archimedes indices. Hard Rule 8
    not applicable (no first-party-observable claim).
single_source_veto_applied: false
single_source_veto_note: >
  Not triggered on the geopolitical facts (multi-source). The forecast is
  capped by its nature as a prediction, not by single-source veto — WEP held at
  "likely" for the renewed-surge assessment; specific A&D-prime targeting held
  at "possible/even chance."
wep_ceiling: likely

# Weighted Estimative Probability (forward assessments)
assessments:
  - claim: "A renewed wave of Iran-nexus hacktivist DDoS, defacement, hack-and-leak, and MOIS-directed influence operations against US and Gulf targets is coming in the near term (days-to-weeks) following the ceasefire collapse."
    wep: likely            # 55-70%
    basis: "Iranian conflict-cyber ops have been reliably timed to kinetic escalation across 2026; ceasefire declared over + public revenge framing resets the retaliation clock."
  - claim: "That renewed surge will include hack-and-leak claims naming US/allied defense contractors (reprising the March-June APT IRAN/Handala pattern)."
    wep: possible           # ~40-50%, even chance
    basis: "Prior phases produced defense-contractor leak claims (APT IRAN/Lockheed Martin data-for-sale; Handala PSK Wind, US Marines dox). Pattern-portable but not observed in-window."

# Inclusion eligibility
inclusion:
  eligible_for:
    - daily_brief_monitoring        # Iran Cyber Watch standing-section situational-awareness material
  not_eligible_for:
    - flash                         # no FLASH trigger met (no in-window discrete incident, no new attribution, no atomic IOC, no critical-CVE-exploited tie)
  ad_relevance: indirect            # defense named among likely target classes; NO A&D prime named in-window

# Attribution (Hard Rule 2)
attribution:
  originated_by_archimedes: false
  note: >
    No new attribution originated or relayed in-window. Prior-phase actor
    references (UNC1549/#004, MuddyWater/#022, Handala/#014, CyberAv3ngers/#028,
    APT IRAN) are restatements of existing corpus attribution for context, not
    new claims.

# Timeliness
timeliness:
  window: "last 24-48h (geopolitical/conflict cyber ops threshold: 48h)"
  in_window_item: "strategic escalation / heightened-threat window (FDD 2026-07-14)"
  out_of_window_context:
    - "UNC1549/Nimbus Manticore defense/aerospace/aviation campaigns — Feb-May 2026 (CPR, SecurityWeek)"
    - "MuddyWater Operation Olalampo / Dindoor — Jan-Feb 2026 (Group-IB, Rescana)"
    - "Handala US Marines dox (~Apr-May) + PSK Wind air-defense C2 breach (Apr 2)"
    - "APT IRAN/CyberAv3ngers Lockheed Martin F-35 data-for-sale claim (~May-Jun); Rockwell/Allen-Bradley PLC campaign (CISA AA26-097A, Apr)"
    - "Iranian AI-assisted space/satellite targeting reporting — National Defense Magazine, Jun 23"

sources:
  - url: https://www.fdd.org/analysis/2026/07/14/ceasefire-collapse-restores-u-s-leverage-as-sanctions-strikes-weaken-irans-hand/
    publisher: FDD
    published: 2026-07-14
    role: primary_in_window
  - url: https://www.cybersecuritydive.com/news/iran-actors-claims-cyber-threat-us-allies/816228/
    publisher: Cybersecurity Dive
    published: 2026-mid   # APT IRAN Lockheed data-for-sale claim; out-of-window incident, in-window heightened-threat framing
    role: corroborating
  - url: https://flare.io/learn/resources/blog/cyberattacks-us-israel-iran-military-conflict
    publisher: Flare
    role: corroborating   # 403 on direct fetch — pending_direct_retrieval
  - url: https://socradar.io/iran-israel-cyber-conflict-dashboard/
    publisher: SOCRadar
    role: corroborating

raw_signal_refs:
  - raw-2026-07-16-iran-001

tlp: CLEAR
---

# Finding — Iran conflict-escalation heightened-threat window (ceasefire collapse resets the cyber retaliation clock)

**BLUF:** The 24-48h window carries **no discrete, attributed Iranian cyber operation against aerospace & defense.** The one genuinely in-window development is strategic: the July 7-9 ceasefire collapse and July 14 escalation analysis **reset the Iranian cyber-retaliation clock**, placing defenders in a heightened-threat window for a renewed hacktivist/hack-and-leak/IO surge. Graded **B2**; renewed surge assessed **likely (WEP)**; A&D-prime targeting within that surge assessed **possible**. **No FLASH trigger met** — this is a watch condition, not an event.

## What is in-window (July 14-16, 2026)

- **Ceasefire collapse (July 7-9):** Iran struck three commercial vessels in the Strait of Hormuz (~July 7); US CENTCOM responded with strikes on 80+ Iranian targets. The ceasefire was declared "over" July 8; the US revoked the Iranian oil-sales waiver.
- **FDD analysis (July 14):** frames the current phase as renewed escalation with restored US leverage.
- **Convergent monitor assessment (Flare, SOCRadar, CSIS, SafeBreach, Cybersecurity Dive):** Iranian cyber ops track kinetic events; this escalation is the most probable trigger for renewed DDoS, defacement, hack-and-leak, and MOIS-directed influence operations against US and Gulf targets, historically spiking within hours of escalation.

## Why it matters for A&D (indirect)

Prior conflict phases produced defense-contractor leak claims (APT IRAN / Lockheed Martin F-35 data-for-sale; Handala air-defense-contractor and US-Marines dox). A renewed surge would likely reprise this pattern. Standing OT/ICS exposure (CyberAv3ngers PLC campaign, CISA AA26-097A) remains the most concrete disruption vector; A&D relevance is structural via shared OT classes.

## Grading note

Multi-source corroboration on the geopolitical facts (B2). The operative cyber claim is a forecast, not an observation — WEP held at "likely," and primaries were only partially retrieved (FDD via search summary; Flare/Unit 42 pages 403'd or stale). Retrieve vendor primaries before any escalation of confidence.
