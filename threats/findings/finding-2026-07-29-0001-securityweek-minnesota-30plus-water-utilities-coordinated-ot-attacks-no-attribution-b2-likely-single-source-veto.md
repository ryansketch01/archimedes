---
finding_id: finding-2026-07-29-0001
created_at: 2026-07-29T08:14:00-04:00
graded_by: grader
grading_run_id: morning-20260729-080000
grading_mode: scheduled_brief
finding_type: new                         # net-new incident (distinct from the 0722/0723 advisory-revision thread)

# Core grading (from admiralty-grading skill output)
digraph: B2
source_reliability:
  grade: B
  source_name: "SecurityWeek (Eduard Kovacs)"
  source_yaml_id: securityweek
  underlying_primary:
    source_name: "Minnesota IT Services (MNIT) + affected municipalities (Maple Plain, Braham, South St. Paul, Plymouth)"
    grade: null                           # official-state-agency + victim statements relayed; not a directly-retrieved graded primary
    in_hand_this_cycle: false
  grade_rationale: >
    Anchored B per source-grades.yaml (SecurityWeek, provisional B, ratifiable). Named-byline
    trade-press incident report (Eduard Kovacs) citing Minnesota IT Services (MNIT) and named
    affected municipalities. Single effective source this cycle — no independent second publisher
    with a separate evidence basis was in hand.
  provisional: false
credibility:
  grade: 2
  checklist_passed:
    - probably_true_ttp_consistent          # coordinated OT-disruption targeting of US water/wastewater utilities is squarely consistent with the well-established threat pattern against that sector (the corpus already tracks this sector-targeting via the AA26-097A / finding-0722-0004 / 0723-0002 Iran-OT advisory thread) — used to assess EVENT plausibility only, NOT to attribute
    - probably_true_no_contradicting_ab      # no A/B-grade source contradicts; a multi-utility OT incident with brief service disruption and safe-water assurances is not surprising against the known sector-threat backdrop
    - probably_true_claims_coherent          # internally coherent — 30+ community water systems, named municipalities, automated-control disruption with manual/contingency fallback, drinking water reported safe, state+federal response — a self-consistent incident report
  grade_1_withheld_reason: >
    Grade 1 (Confirmed) withheld: single effective evidence basis. One publisher (SecurityWeek)
    relaying MNIT + municipality statements. No independent second source, no separate telemetry, no
    first-party corroboration. Corroboration fails the independence test -> at most grade 2.
  rationale: >
    SecurityWeek (Eduard Kovacs, published 2026-07-29 03:53 EDT, in the 00:00-06:00 sweep window)
    reported that more than 30 Minnesota community water systems were targeted in coordinated attacks
    on operational-technology systems on 2026-07-26 to 2026-07-27, disrupting automated control
    functions and briefly taking some systems offline; drinking water was reported safe and services
    remained operational in most cases via contingency/manual procedures. B-grade named-byline relay
    of an official-agency + victim account, sector-threat-consistent, no contradiction, single
    effective source -> Probably True.
corroboration:
  independent_sources:
    - securityweek
  independent: false
  test_result: >
    Single effective source (SecurityWeek relaying MNIT + municipality statements). No independent
    evidence basis this cycle. Independence test fails for grade 1. The corpus Iran-OT thread
    (0722-0004 / 0723-0002) is a THEMATIC/sector-TTP correspondence, NOT an independent corroborating
    source for THIS specific incident.
first_party_precedence:
  applied: false
  splunk_evidence: null
  splunk_note: >
    No atomic IOCs in the report to pivot on (no IPs / domains / hashes / CVEs published). No queryable
    atom -> no Rule 8 hunt possible this cycle. Frank telemetry has no Minnesota-water-utility nexus
    regardless. Silent by absence-of-artifact, NOT disconfirming (Hard Rule 8).
single_source_veto_applied: true
single_source_veto_note: >
  Applies — single effective source (one publisher relaying official-agency + victim statements). WEP
  capped at "likely". Veto lifts on an independent second source with a separate evidence basis.
wep_ceiling: likely

# Attribution — NONE made; grade the EVENT, not the speculation (Hard Rule 2 — the critical care point)
attribution:
  attribution_made: false
  advisory_attribution_verbatim: "formal attribution has not been made"   # <15 words, Hard Rule 6; source explicitly states attribution not established
  attributed_by: null
  archimedes_position: >
    The source EXPLICITLY states no attribution has been made and that it is unclear who is behind the
    attack. SecurityWeek mentions Iranian groups (CyberAv3ngers, Handala) only as SPECULATIVE potential
    profiles, NOT as a confirmed attribution of this incident. Archimedes originates NO attribution and
    inherits NONE. The roster overlap is recorded as sector-TTP-class awareness for analyst/actor-profiler
    ONLY — it is not an assertion that any tracked actor conducted this activity. Hard Rule 2 preserved
    rigorously: the event is graded; the speculation is not.
  structural_actor_linkage:
    - claimed_actor: null                 # NO actor named as the operator; sector-TTP-class correspondence only
      corpus_correspondence: "CyberAv3ngers (#028, IRGC-CEC — documented US water-utility OT targeting, Unitronics 2023-24) and Handala (#014, Iran-MOIS) named by the source ONLY as speculative profiles; the OT-disruption-vs-US-water pattern is consistent with #028's documented TTP class"
      basis: "sector + TTP-class correspondence to the corpus Iran-OT thread (0722-0004 / 0723-0002 advisory revisions warning of exactly this sector-targeting)"
      requires_analyst_review: true       # analyst/actor-profiler adjudicates whether this incident is dossier-worthy CONTEXT for #028 — WITHOUT asserting #028 conducted it (Hard Rule 2)
      is_source_attribution: false
      novel_attribution: false            # nothing originated

# Inclusion eligibility (from admiralty-grading)
inclusion:
  eligible_for:
    - daily_brief_monitoring              # Iran Cyber Watch / OT-ICS continuity monitoring datum; B2 clears both the B2 action floor and the C3 monitoring floor, but framed MONITORING given no attribution, no A&D victim, no CVE, 0 IOCs
    - weekly_synthesis
    - actor_profile_update                # actor-profiler reviews the sector-TTP-class correspondence for the #028 dossier as CONTEXT only (adjudicating, NOT asserting)
  flash_eligibility_note: >
    NOT a FLASH — confirmed below-bar by the collector. Trigger 2 (new attribution): FAIL (no
    attribution). Trigger 5 (nation-state A&D campaign): FAIL on sector (water/critical-infra, not
    A&D/watchlist). Trigger 4 (tracked-actor TTP change): FAIL (no tracked actor attributed). Routed
    to the 2026-07-29 morning brief as Iran Cyber Watch + OT/ICS sector-monitoring material.

# A&D relevance (structural / indirect — NOT an A&D victim)
ad_relevance: low_to_medium
ad_relevance_rationale: >
  Sector is water/wastewater critical infrastructure — NOT aerospace/defense, not a watchlist entity,
  no PLC vendors named, no CVE, 0 IOCs. Relevance is INDIRECT: (1) it is a fresh, real-world OT-
  disruption incident against the exact US-water-utility sector the corpus Iran-OT advisory thread
  (0722-0004 / 0723-0002) warned about days earlier, so it is a live monitoring datum for that thread;
  (2) the OT-disruption TTP class shares an attack-surface concept with A&D facility/manufacturing OT.
  Rated LOW-to-MEDIUM — a sector-adjacent monitoring signal, NOT a targeted A&D campaign and NOT a
  named-A&D exposure. Re-rate up ONLY on a named A&D/DIB victim or a cited A/B-source attribution.

# Cluster metadata
cluster:
  topic: "30+ Minnesota community water systems hit by coordinated OT attacks (2026-07-26/27); automated control disrupted, water reported safe; NO attribution made (Iranian personas named only speculatively). Water/wastewater sector, no A&D victim, no CVE, 0 IOCs."
  cluster_size: 1
  raw_signal_members:
    - raw-2026-07-29-flash-0600-001
  attribution_claims:
    - claimed_actor: null                 # NO actor attributed; Iranian-persona mentions are explicitly speculative
      claimed_by_sources: []
      requires_analyst_review: true       # sector-TTP-class correspondence for actor-profiler adjudication, NOT grader assertion
      novel_attribution: false

# Downstream handoff flags
analyst_review_required: true
analyst_review_note: >
  Flagged per the WEP-"likely" rule AND the sector-TTP-class correspondence to the corpus Iran-OT
  thread. Focus: (1) adjudicate whether this incident is dossier-worthy CONTEXT for CyberAv3ngers
  (#028) as a monitoring datum — WITHOUT asserting #028 or any Iranian actor conducted it, because NO
  source attributes it (Hard Rule 2 is the hard constraint here); (2) confirm the LOW-to-MEDIUM
  structural A&D framing; (3) note the direct-retrieval enrichment todo (an MNIT primary / any CISA
  ICS advisory that may follow). Caution: do NOT construct an actor-identity ACH matrix — the source
  makes no attribution and building one would manufacture/originate attribution.
analyst_review_complete: true
analyst_review_run_id: analyst-20260729-0830
red_team_review_required: false           # WEP ceiling "likely" < "very likely"; single-source veto binds. Red-team not mandatory.
red_team_review: null
wep_ceiling_after_analysis: likely        # UNCHANGED — SATs do not override the single-source veto grading floor
wep_ceiling_adjusted: false
wep_ceiling_adjustment_reason: >
  KAC surfaced no Reject and no Test classification. Load-bearing assumptions are Qualify-class
  (framing caveats), not evidence collapse. WEP remains "likely" per the single-source veto; SATs
  qualify HOW the event is framed for monitoring, not the grade.
assessment_blocked_pending_test: false
analysis_sections:
  sat_ach: null                           # NOT run by design — an actor-identity ACH would originate attribution the source declines to make (Hard Rule 2, per grader instruction). Mechanism-class ACH not warranted: the finding makes no mechanism claim beyond "coordinated OT disruption," and the diagnostic question here is about framing-assumptions (KAC's job), not competing explanations of graded evidence.
  sat_kac:
    kac_analysis:
      assessment_under_review: >
        "The 30+ Minnesota water-utility OT incident (2026-07-26/27) is a valid, sector-TTP-consistent
        MONITORING datum for the corpus Iran-OT / US-water-utility thread and carries low-to-medium
        indirect A&D-transfer relevance." (Assessment is about the EVENT and its analytic relevance to
        the target profile — NOT about who conducted it. No attribution is assessed; Hard Rule 2 binds.)
      analyzed_at: 2026-07-29T08:32:00-04:00
      analyzed_by: analyst
      invoking_context: >
        Grader handoff, WEP-"likely" rule + explicit instruction to KAC the source's FRAMING assumptions
        (coordination, intentionality, sector-transfer value) rather than build an actor-identity ACH.
      assumptions:
        - id: A1
          statement: "'Coordinated attacks' implies a single coordinating actor / unified campaign rather than clustered independent, commodity, or opportunistic incidents."
          category: semantic
          stated: true
          why_must_be_true: "The source's 'coordinated' characterization is what elevates this from routine multi-site IT trouble to a campaign-shaped signal."
          when_could_be_false: "The 30+ systems share a common MSP, SCADA vendor, remote-access tool, or regional ISP, and a single commodity intrusion (or misconfiguration/ransomware spillover) produced simultaneous effects with no coordinating adversary."
          evidence_for: [securityweek]
          evidence_against: []
          confidence: low
          centrality: material
          classification: qualify
        - id: A2
          statement: "The OT disruption was intentional adversary targeting of operational technology, not a commodity/opportunistic event (ransomware, IT-side outage) reported as 'OT attacks.'"
          category: intent
          stated: false
          why_must_be_true: "The monitoring value as an Iran-OT-thread continuation depends on this being deliberate OT-directed activity, not generic IT compromise mislabeled."
          when_could_be_false: "Root cause turns out to be commodity ransomware/IT outage that degraded OT-adjacent control indirectly; 'OT attack' is early-reporting shorthand."
          evidence_for: [securityweek]
          evidence_against: []
          confidence: low
          centrality: material
          classification: qualify
        - id: A3
          statement: "The incident actually reached OT/automated-control functions (as reported), not only the IT/business network."
          category: technology
          stated: true
          why_must_be_true: "Automated-control disruption is the specific technical claim that makes this OT-relevant."
          when_could_be_false: "Follow-on reporting reveals the disruption was IT-side (billing, telemetry, HMI availability) with automated control degraded only by loss of visibility."
          evidence_for: [securityweek]
          evidence_against: []
          confidence: low
          centrality: material
          classification: qualify
        - id: A4
          statement: "A water/wastewater OT incident carries non-zero monitoring/transfer value to the A&D target profile (shared OT attack-surface concepts)."
          category: semantic
          stated: true
          why_must_be_true: "This is why an incident with no A&D victim, no CVE, and zero IOCs is included at all — the OT-attack-surface concept and the Iran-OT-thread continuity are the transfer bridge."
          when_could_be_false: "Water-SCADA specifics (Unitronics-class PLCs, municipal remote-access patterns) are sufficiently distinct from A&D-manufacturing OT that operational lessons do not transfer."
          evidence_for: [securityweek]
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify
        - id: A5
          statement: "The reported scope ('more than 30 community water systems') is materially accurate."
          category: source_reliability
          stated: true
          why_must_be_true: "Scope is part of what makes this a notable sector signal vs a single-site outage."
          when_could_be_false: "Early official/victim counts revise down, or 'affected' conflates probed/scanned with disrupted."
          evidence_for: [securityweek]
          evidence_against: []
          confidence: medium
          centrality: peripheral
          classification: sound
        - id: A6
          statement: "This is a net-new real-world INCIDENT distinct from the 0722/0723 Iran-OT ADVISORY-revision thread, not a re-report of it."
          category: semantic
          stated: true
          why_must_be_true: "Filing as a new finding with monitoring value (vs an UPDATE) depends on temporal/factual distinctness from the advisory campaign."
          when_could_be_false: "The Minnesota incident is later shown to be a downstream instance of the same advisory-warned campaign — which would still be monitoring-relevant, just re-scoped as continuity."
          evidence_for: [securityweek]
          evidence_against: []
          confidence: medium
          centrality: peripheral
          classification: sound
        - id: A7
          statement: "Sector-TTP-class correspondence to the corpus Iran-OT thread has monitoring value even with NO attribution made."
          category: TTP_patterns
          stated: false
          why_must_be_true: "The finding's inclusion rests on pattern-continuity monitoring, not on any actor claim; the correspondence must be analytically useful absent attribution."
          when_could_be_false: "If sector-TTP correspondence with zero attribution is treated as a nudge toward the Iranian personas, it silently manufactures attribution (Hard Rule 2 breach) — the assumption is only valid if held STRICTLY as unattributed pattern awareness."
          evidence_for: [securityweek]
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify
      classifications_summary:
        sound: 2
        qualify: 5
        test: 0
        reject: 0
      remediation:
        status: proceed
        blocking_assumption: null
        qualifying_caveats:
          - "Brief must present 'coordinated' as the SOURCE's characterization, not an established single-actor campaign (A1)."
          - "Intentional-OT-targeting vs commodity/IT-spillover root cause is UNCONFIRMED; frame as reported, not established (A2/A3)."
          - "A&D relevance is indirect OT-attack-surface transfer + Iran-OT-thread continuity — hold at low-to-medium; do not imply a targeted A&D nexus (A4)."
          - "Sector-TTP correspondence is UNATTRIBUTED pattern awareness ONLY; it must never read as a hint toward CyberAv3ngers/Handala (A7, Hard Rule 2)."
        next_action: >
          Proceed to brief as a caveated MONITORING datum. Re-run KAC if a CISA/EPA/MNIT primary or ICS
          advisory publishes root-cause, revised scope, IOCs, or a cited attribution.
      tripwires:
        - observation: "Follow-on primary establishes commodity ransomware / IT-side root cause"
          effect: "A2/A3 shift toward Reject; downgrade OT-targeting framing, keep as sector-outage datum"
        - observation: "CISA/EPA/MNIT publishes a cited attribution"
          effect: "Re-scope: attribution becomes INHERITED (sourced), reassess relevance; still no Archimedes origination"
        - observation: "Independent second publisher with a separate evidence basis appears"
          effect: "Single-source veto lifts; grader re-grades toward grade 1 / higher WEP ceiling"
      recommended_wep_after_test:
        current: likely
        if_root_cause_commodity: likely (relevance framing narrows to generic OT-outage datum)
        if_attribution_published: likely (veto still binds until independent corroboration; attribution then inherited not originated)

# Handoffs
handoffs:
  direct_retrieval_todo:
    - "Watch for a follow-on CISA / EPA / MNIT primary or ICS advisory on the Minnesota water-utility incident (would add an independent evidence basis, possible IOC appendix, and possibly a cited attribution — until then, no attribution and single-source veto binds)."
  actor_profiler_note: >
    CyberAv3ngers (#028) dossier candidate-CONTEXT: a fresh US-water-utility OT-disruption incident
    consistent with #028's documented TTP class, occurring days after the 0722/0723 Iran-OT advisory
    revisions. For actor-profiler to adjudicate as monitoring context ONLY. Grader asserts NO
    attribution (Hard Rule 2). Handala (#014) named only in the same speculative framing.

# Lifecycle
tlp: CLEAR
published_in_briefs: [2026-07-29-morning, 2026-07-31-morning]   # briefer appends brief_ids
retracted: false
retraction_brief_id: null
last_updated: 2026-07-31T08:16:00-04:00
updates:
  - update_id: upd-2026-07-31-0001
    updated_at: 2026-07-31T08:16:00-04:00
    updated_by: grader
    grading_run_id: morning-20260731-080000
    raw_signal_members:
      - raw-2026-07-31-am-001
    update_type: authoritative_advisory_followon
    grade_change: none                    # remains B2 / likely; single-source veto still binds (same relay publisher, CISA advisory not directly retrieved)
    summary: >
      CISA has published an authoritative mitigation advisory following the Minnesota water-utility OT
      incident, relayed by SecurityWeek (Mike Lennon, 2026-07-30). CISA's three immediate actions:
      (1) disconnect PLCs from the internet / route remote access via VPN/gateway; (2) enable password
      protection and change default credentials; (3) allowlist IP addresses to known devices. CISA also
      recommends clean PLC backups and points to advisory AA26-097A for indicators of compromise. Named
      PLC target families surfaced: Rockwell CompactLogix and Micro850, Schneider Electric Modicon M340,
      Siemens S7-1200. Attack technique detail added: attackers modified passwords to lock out operators
      and disconnected PLCs by changing IP addresses; vulnerable cellular modems called out as often-
      undocumented entry points. Incident scope reaffirmed (30+ community water systems, 2026-07-26/27;
      named municipalities Maple Plain, Braham, South St. Paul, Plymouth).
    grade_rationale_note: >
      Grade unchanged at B2 / likely. The advisory ELEVATES the originating authority from trade-press
      relay of MNIT+municipality statements to a federal CISA advisory (A-grade authority) — but the
      effective source IN HAND is still SecurityWeek (B), the SAME relay publisher as the original
      finding, and neither the CISA advisory nor AA26-097A was directly retrieved this cycle. Per this
      finding's own tripwire, the single-source veto lifts only on an INDEPENDENT SECOND PUBLISHER with a
      separate evidence basis; a different authority (CISA) reaching us through the same publisher does
      not satisfy that. Credibility stays 2; digraph stays B2; WEP stays "likely." Direct retrieval of the
      CISA advisory + AA26-097A is the firming milestone (would establish an independent documentary basis
      and possibly an IOC appendix).
    attribution_note: >
      Hard Rule 2 preserved. STILL no attribution. The source states no formal attribution has been made;
      CyberAv3ngers (#028) and Handala (#014) remain named only as profile-fit, NOT as an attribution of
      this campaign. Critically: CISA's own cross-reference to AA26-097A (the CyberAv3ngers six-agency
      advisory) is a PROCEDURAL IOC-reference, not an attribution of this Minnesota campaign — that
      distinction must be preserved downstream. Archimedes originates and inherits NO attribution.
    named_plc_targets:
      - "Rockwell Automation CompactLogix"
      - "Rockwell Automation Micro850"
      - "Schneider Electric Modicon M340"
      - "Siemens S7-1200"
    ioc_reference_advisory: AA26-097A       # CISA-referenced IOC set; NOT directly retrieved this cycle (direct-retrieval todo)
    first_party_precedence:
      applied: false
      splunk_note: "Grader Rule 8 re-run 2026-07-31 over the named PLC families (CompactLogix / Micro850 / Modicon / S7-1200) across archimedes + defenseclaw_local -> 0 events. No atomic IOCs in the relay to pivot on; AA26-097A IOC set not retrieved. Visibility-bounded null (Hard Rule 8)."
    handoff_note: >
      Direct-retrieval todo elevated: pull the CISA advisory + AA26-097A for (a) an independent documentary
      basis (could lift credibility toward 1 / lift the veto) and (b) the atomic IOC set for the master
      index + first-party hunt. actor-profiler: the named PLC families + technique detail (password lockout,
      IP-change PLC disconnection, cellular-modem entry) are sector-TTP-class CONTEXT for the #028 dossier
      to adjudicate WITHOUT asserting #028 conducted this (Hard Rule 2). vuln-tracker: no CVE named.
    briefer_note: "Present as an authoritative-advisory UPDATE to the 2026-07-29 Minnesota OT item — CISA now has published mitigation guidance and named PLC targets. Carry the named PLC families + CISA's three immediate actions as the actionable OT-hardening so-what. Keep attribution absent; Iranian personas only as the source's profile-fit, never Archimedes' lean."
---

# 30+ Minnesota water utilities hit by coordinated OT attacks — automated control disrupted, water reported safe (NO attribution made)

## Summary

SecurityWeek (Eduard Kovacs, 2026-07-29) reported that more than 30 Minnesota community water systems were targeted in coordinated attacks on operational-technology systems on 2026-07-26 to 2026-07-27, citing Minnesota IT Services (MNIT) and named affected municipalities (Maple Plain, Braham, South St. Paul, Plymouth). Automated control functions were disrupted and some systems were briefly taken offline; drinking water was reported safe and services remained operational in most cases via contingency and manual procedures. State and federal agencies are responding.

Graded B2 / "likely" with the single-source veto applied: a single B-grade trade-press relay of official-agency and victim statements, sector-threat-consistent and internally coherent, but not independently corroborated this cycle. The water/wastewater sector is not aerospace/defense — this is an INDIRECT monitoring datum, valuable primarily as a live continuation of the corpus Iran-OT / US-water-utility advisory thread.

## Attribution handling (Hard Rule 2 — the critical care point)

The source EXPLICITLY states that formal attribution has not been made and that it is unclear who is behind the attack. SecurityWeek names Iranian groups (CyberAv3ngers, Handala) only as SPECULATIVE potential profiles, not as a confirmed attribution of this incident. Archimedes originates NO attribution and inherits NONE. The event is graded; the speculation is not. The corpus overlap — CyberAv3ngers (#028, IRGC-CEC, documented US water-utility OT targeting) and Handala (#014, Iran-MOIS) — is recorded ONLY as sector-TTP-class awareness for analyst/actor-profiler adjudication, never as an assertion that any tracked actor conducted this activity.

## Technical detail

- **Activity class:** coordinated attacks on OT systems of community water utilities; disruption of automated control functions; some systems briefly offline; manual/contingency procedures maintained service in most cases. Recorded at class level per Hard Rule 3 — no exploitation detail.
- **Impact:** drinking water reported safe; no reported public-health impact per the source.
- **Scope:** more than 30 community water systems; named municipalities — Maple Plain, Braham, South St. Paul, Plymouth.
- **CVE:** none named. **IOCs:** none published (no IPs, domains, or hashes in the source).
- **Response:** MNIT plus state and federal agencies responding/investigating.

## IOCs surfaced

None. Zero atomic IOCs (no IPs, domains, hashes, or CVEs) in the source. No PoC/exploit content (Hard Rule 3). No credentials in scope (Hard Rule 7).

## Relationship to existing findings

Sector-thread continuity with the corpus Iran-OT / US-critical-infrastructure line — finding-2026-07-22-0004 (The Record relay of the CISA/FBI/EPA Iran-OT advisory revision) and finding-2026-07-23-0002 (SecurityWeek relay of the same advisory, adding named victims California Water Service + Stryker and specific PLC models/ports). Those were ADVISORY-REVISION findings warning of Iranian OT targeting of US water utilities; this is a distinct, NET-NEW real-world INCIDENT against 30+ Minnesota water systems occurring days later. The sector and TTP class correspond, but NO source connects this incident to that advisory campaign or to any actor — so it is filed as a new finding with a relationship note, not an UPDATE, and carries no inherited attribution (Hard Rule 2).

## Analytic notes (from analyst review)

KAC only — an actor-identity ACH was correctly declined, since building one would manufacture the attribution the source explicitly withholds (Hard Rule 2). Seven assumptions surfaced; none Reject, none Test, so the assessment proceeds and the "likely" WEP ceiling stands (the single-source veto is a grading floor SATs cannot lift).

Five assumptions are load-bearing-but-fragile (Qualify). The most fragile: "coordinated" implies a single actor (A1) and the disruption was intentional OT targeting rather than commodity/IT-spillover mislabeled as an "OT attack" (A2/A3) — both rest on one B-grade relay of early official/victim statements. The finding's value survives even if these soften: a multi-site water-utility OT-adjacent disruption remains a real Iran-OT-thread continuity datum. The most important discipline point is A7 — the sector-TTP correspondence to the corpus Iran-OT thread is useful ONLY as strictly unattributed pattern awareness; if it ever reads as a nudge toward CyberAv3ngers or Handala, it silently originates attribution.

Monitoring assessment holds at low-to-medium indirect A&D relevance. Briefer must carry: present "coordinated" and "OT attack" as the source's characterization (not established fact), keep relevance framed as OT-attack-surface transfer plus thread continuity, and name the Iranian personas — if at all — only as the source's own speculation, never as Archimedes' lean.

## Open questions for analyst

- Adjudicate whether this incident is dossier-worthy monitoring CONTEXT for CyberAv3ngers (#028) — WITHOUT asserting #028 or any Iranian actor conducted it (no source attributes it; Hard Rule 2).
- Do NOT construct an actor-identity ACH here — building one would originate an attribution the source declines to make.
- Watch for a follow-on CISA/EPA/MNIT primary or ICS advisory that could add an independent evidence basis (and possibly a cited attribution or IOC appendix).

## Sources

### SecurityWeek (securityweek, digraph letter: B) — 2026-07-29 03:53 EDT

- URL: https://www.securityweek.com/dozens-of-minnesota-water-utilities-targeted-in-coordinated-ot-attacks/
- Author: Eduard Kovacs
- Key claim: 30+ Minnesota community water systems targeted in coordinated OT attacks on 2026-07-26/27; automated control disrupted, some systems briefly offline; drinking water safe; formal attribution not made (Iranian personas named only speculatively); MNIT + state/federal response.

### SecurityWeek (securityweek, digraph letter: B) — 2026-07-30 18:18 EDT — CISA advisory relay (added in 2026-07-31 update)

- URL: https://www.securityweek.com/cisa-urges-water-sector-to-protect-ot-after-coordinated-attacks-on-plcs/
- Author: Mike Lennon (relaying a CISA alert dated 2026-07-30; CISA references advisory AA26-097A for IOCs)
- Key claim: CISA urges the water sector to protect OT after the coordinated PLC attacks; three immediate actions (disconnect PLCs from the internet / VPN-gate remote access, enable password protection + change defaults, allowlist IPs) plus clean PLC backups and review of AA26-097A for IOCs; names targeted PLC families (Rockwell CompactLogix/Micro850, Schneider Modicon M340, Siemens S7-1200); attackers locked out operators by changing passwords and disconnected PLCs by changing IPs; vulnerable cellular modems flagged as entry points. Still NO attribution (CyberAv3ngers/Handala profile-fit only).

## Update — 2026-07-31 morning (CISA advisory follow-on; grade unchanged B2 / likely; NO attribution)

**Authoritative follow-on, grade unchanged.** CISA has published mitigation guidance following the Minnesota water-utility OT incident, relayed by SecurityWeek (Mike Lennon, 2026-07-30). This advances the tracked campaign from a trade-press incident report to an authoritative federal advisory. New material this cycle:

- **CISA's three immediate actions:** (1) disconnect PLCs from the internet — route remote access through VPN/gateway; (2) enable password protection and change default credentials; (3) allowlist IP addresses to known devices only. Plus: maintain clean PLC backups; review advisory **AA26-097A** for indicators of compromise.
- **Named targeted PLC families:** Rockwell Automation CompactLogix and Micro850, Schneider Electric Modicon M340, Siemens S7-1200.
- **Technique detail:** attackers modified passwords to lock out operators and disconnected PLCs by changing IP addresses; vulnerable, often-undocumented cellular modems flagged as entry points.
- **Scope reaffirmed:** 30+ community water systems, 2026-07-26/27; named municipalities (Maple Plain, Braham, South St. Paul, Plymouth).

**Why the grade does not move.** The advisory elevates the ORIGINATING authority to CISA (A-grade federal), but the effective source in hand is still SecurityWeek (B) — the SAME relay publisher as the original finding — and neither the CISA advisory nor AA26-097A was directly retrieved this cycle. Per this finding's own tripwire, the single-source veto lifts only on an INDEPENDENT SECOND PUBLISHER with a separate evidence basis; a different authority (CISA) reaching us through the same publisher does not satisfy that. Credibility stays 2, digraph stays **B2**, WEP stays **"likely."** Grader Rule 8 re-run over the named PLC families across `archimedes` + `defenseclaw_local` returned 0 events (visibility-bounded null; AA26-097A IOC set not retrieved).

**Hard Rule 2 — still no attribution.** The source states no formal attribution has been made. CyberAv3ngers (#028) and Handala (#014) remain profile-fit mentions only. Critically, CISA's own cross-reference to AA26-097A (the CyberAv3ngers six-agency advisory) is a **procedural IOC-reference, not an attribution** of this Minnesota campaign — preserve that distinction downstream. Archimedes originates and inherits no attribution.

**So-what (now actionable OT hardening).** Carry the named PLC families and CISA's three immediate actions as the actionable defensive guidance for OT-owning readers (including A&D-facility/manufacturing OT by attack-surface analogy). Direct-retrieval todo elevated: pull the CISA advisory + AA26-097A for an independent documentary basis (could lift credibility toward 1 / lift the veto) and the atomic IOC set for the master index and a first-party hunt.

*Update source: raw-2026-07-31-am-001. Grader run morning-20260731-080000.*
