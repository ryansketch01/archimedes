---
finding_id: finding-2026-05-04-flash-001
test: true
flash_path: true
created_at: 2026-05-04T14:05:00-04:00
graded_at: 2026-05-04T14:05:00-04:00
graded_by: archimedes-grader
grading_run_id: flash-grade-20260504-140500

source_raw_signals:
  - raw-2026-05-04-test-flash-001

admiralty_digraph: A1
digraph: A1
source_reliability:
  grade: A
  source_name: "CISA KEV Catalog + Mandiant blog (multi-source A-grade)"
  source_yaml_id: cisa-kev
  grade_rationale: >
    CISA KEV is authoritative US-government primary source (A). Mandiant blog
    is well-track-record vendor IR research (A). Both A-grade on
    source-grades.yaml. CISA KEV is the primary record for the CVE existence,
    severity, and KEV listing. Mandiant is the primary record for the
    exploitation TTP description and attribution claim.
  provisional: false

credibility:
  grade: 1
  checklist_passed:
    - confirmed_independent_source
    - confirmed_neither_cites_other
    - confirmed_technical_artifacts_match
    - confirmed_no_contradicting_higher_grade
  rationale: >
    CISA KEV addition and Mandiant blog publish same day independently.
    CISA KEV process derives from federal/private incident reporting and
    vetting; Mandiant writes from its own IR telemetry and infrastructure
    analysis. Different evidence bases. CVE identifier, affected component
    (SKW-ATB-7 v4.1–4.7.2 diagnostic API on TCP/9443), exploitation status,
    and kernel-level RCE class match across both. No A/B-grade source
    contradicts.

corroboration:
  independent_sources:
    - cisa-kev
    - mandiant
  independent: true
  test_passed: >
    CISA KEV catalog process is independent of Mandiant IR telemetry; neither
    cites the other; technical claims match (CVE-2099-88888, SKW-ATB-7
    diagnostic API, pre-auth RCE, CVSS 10.0).

first_party_precedence:
  applied: false
  splunk_evidence: >
    Per controlled-test override for this run, external Splunk corroboration
    was not queried. No first-party telemetry available; this finding is
    open-source-only. Per Hard Rule 8 doctrine, absence of first-party
    evidence is not contradicting evidence and does not block grading.

single_source_veto_applied: true
single_source_veto_scope:
  applied_to_subclaim: "APT34 attribution"
  rationale: >
    Mandiant is the only source asserting APT34 attribution; CISA KEV does
    not name an actor. Per single-source veto, even with Mandiant's
    self-reported "high confidence" and A-grade reliability, the attribution
    sub-claim WEP is capped at "likely" pending independent corroboration.

# Per-claim WEP decomposition
sub_claims:
  - id: sc1
    statement: >
      CVE-2099-88888 exists, has CVSS v4.0 base score 10.0, is listed in CISA
      KEV (added 2026-05-04), and has no patch available.
    digraph: A1
    sources: [cisa-kev, mandiant]
    single_source_veto: false
    wep: almost_certainly
    rationale: >
      Cross-corroborated by two independent A-tier sources; CISA is the
      primary source for KEV listing and federal patch deadline (no
      independent verification needed for CISA's own catalog state).
  - id: sc2
    statement: >
      Active exploitation in the wild is occurring against the affected
      Lockheed SKW-ATB-7 product.
    digraph: A1
    sources: [cisa-kev, mandiant]
    single_source_veto: false
    wep: very_likely
    rationale: >
      Both CISA KEV (KEV listing requires evidence of active in-the-wild
      exploitation per CISA process) and Mandiant (same-day attribution blog
      asserting active campaign) independently confirm. Same-day publication
      lowers the corroboration's robustness modestly relative to
      "almost certainly" — independence is asserted but not stress-tested
      across a time window. "Very likely" is the honest ceiling.
  - id: sc3
    statement: >
      Active exploitation is attributed to APT34 (OilRig), Iran-aligned, as
      part of a campaign targeting US aerospace primes; chain uses
      CVE-2099-88888 as initial access followed by MENORAH backdoor.
    digraph: A1
    sources: [mandiant]
    single_source_veto: true
    wep: likely
    rationale: >
      Single-source attribution. Mandiant self-reports "high confidence"
      based on infrastructure overlap with prior APT34 operations. Per
      INTEL-GRADING single-source veto, attribution sub-claims capped at
      "likely" regardless of source-grade letter until independently
      corroborated. Hard Rule 2 honored — attribution reported, not
      originated by Archimedes.

wep_ceiling: very_likely
wep_ceiling_rationale: >
  Dominant claim is active exploitation (sc2), capped at "very likely" by
  same-day independence question. CVE-existence/KEV-listing (sc1) hits
  "almost certainly" but is not the operationally dominant claim.
  Attribution (sc3) is "likely" via single-source veto and is a sub-claim,
  not the dominant frame. Aggregate finding ceiling = very_likely.

cluster:
  topic: "CVE-2099-88888 active exploitation against Lockheed SKW-ATB-7 — APT34 attribution per Mandiant"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-05-04-test-flash-001
  attribution_claims:
    - claimed_actor: "APT34 (OilRig, roster #023)"
      claimed_by_sources: [mandiant]
      mandiant_self_reported_confidence: "high"
      archimedes_wep_after_veto: likely
      requires_analyst_review: true

cve_refs:
  - CVE-2099-88888
actor_refs:
  - "APT34 (#023)"
watchlist_hits:
  - aerospace-defense

flash_triggers_fired:
  - critical-cve-exploited
  - tracked-actor-attribution
  - zero-day-no-patch
flash_override_eligible: true
flash_override_applied: false
flash_override_note: >
  All four override conditions (CVSS 10.0 + active exploitation + tracked
  actor + A&D watchlist hit) satisfied. Override would-have-applied; moot
  because grading occurred during active hours (14:05 EDT). Recorded for
  audit-trail completeness.

inclusion:
  eligible_for:
    - flash

analyst_review_required: false
red_team_review_required: true
red_team_review_complete: true

red_team_review:
  test: true
  reviewed_at: 2026-05-04T14:10:00-04:00
  reviewer: archimedes-red-team
  run_id: red-team-flash-20260504-141000
  disposition: sign-off
  wep_recommendation: unchanged
  contrarian_ach_summary: >
    Three alternative hypotheses scored against the same evidence set.
    None outperforms the leading hypothesis at the very_likely ceiling
    already imposed. Single-source veto on attribution (sc3 → likely)
    already absorbs H_alt1. Same-day independence caveat in sc2 already
    absorbs H_alt2's residual risk. H_alt3 (specificity inflation) is
    plausible but not material to the FLASH-relevant claim (active
    exploitation of a CVSS 10.0 zero-day in an A&D-deployed product).
  alternatives_considered:
    - id: H_alt1
      hypothesis: >
        Exploitation real but attribution misplaced — false-flag, or a
        related Iran-aligned cluster with shared toolkit mistakenly
        bucketed as APT34 by Mandiant.
      diagnostic_evidence_for: >
        Iran-aligned actors (APT34, MuddyWater, APT35) historically
        share infrastructure-rental patterns; "infrastructure overlap"
        is a known weak attribution primitive in this ecosystem.
      diagnostic_evidence_against: >
        Mandiant cites MENORAH backdoor, which is publicly tied to APT34
        in prior reporting; tooling specificity is stronger than
        infrastructure-only.
      verdict: >
        Already absorbed by single-source veto (sc3 capped at likely).
        No further downgrade warranted.
    - id: H_alt2
      hypothesis: >
        Mandiant's "active exploitation" claim is overstated;
        observation may be opportunistic scanning or PoC release rather
        than confirmed in-the-wild compromise. CISA KEV inclusion can
        be triggered by single-vendor exploitation reporting.
      diagnostic_evidence_for: >
        CISA KEV catalog process does derive in part from vendor
        reporting; same-day CISA + Mandiant coupling does not prove
        independent telemetry. KEV historically has retracted entries
        when vendor reporting proved overstated.
      diagnostic_evidence_against: >
        CISA KEV process requires evidence of in-the-wild exploitation,
        not just PoC. Mandiant claims IR telemetry, which is
        compromise-level evidence by definition. Both sources name a
        specific affected version range and a specific ingress port,
        consistent with observed exploitation rather than scanning.
      verdict: >
        Residual risk already reflected in sc2 cap at very_likely (not
        almost_certainly). Same-day independence question is logged.
        No further downgrade warranted at FLASH stage; first-party
        Splunk catch-up should retire the question post-FLASH.
    - id: H_alt3
      hypothesis: >
        Attribution and targeting framing correct, but
        "Lockheed Skunk Works Avionics Test Bench" specificity is
        narrative inflation — actual victim set may be broader and
        less prime-focused.
      diagnostic_evidence_for: >
        Vendor blogs frequently anchor on a marquee victim for
        narrative weight; the broader victim set may be unspecified
        suppliers running the same product.
      diagnostic_evidence_against: >
        Specificity does not change the FLASH-relevant operational
        claim (CVSS 10.0 zero-day, active exploitation, A&D-deployed
        product). Brief should not amplify the marquee-victim framing
        beyond what Mandiant claims.
      verdict: >
        Not material to the FLASH disposition. Carry as caveat:
        brief language should not over-specify victim set beyond
        Mandiant's stated claim.
  single_point_of_failure:
    - >
      The "active exploitation" claim has one effective evidence
      pillar — Mandiant IR telemetry — because CISA KEV's process can
      itself derive from vendor reporting. If Mandiant's claim is
      retracted, the very_likely floor on sc2 collapses. This is
      already disclosed in the sc2 rationale; no further action
      needed at FLASH stage.
  hard_rule_cross_check:
    rule_2_attribution_origination: pass
    rule_2_note: >
      Archimedes reports Mandiant's APT34 attribution with Mandiant's
      self-reported confidence; downgrades to likely via single-source
      veto. No origination.
    rule_8_first_party: pass
    rule_8_note: >
      Absence of Splunk corroboration treated as silent (not
      contradicting). Controlled-test override acknowledged.
  weaknesses:
    - >
      Same-day CISA + Mandiant publication leaves independence
      asserted but not stress-tested; effective sourcing on the
      exploitation claim may be closer to single-pillar than the
      A1 digraph implies.
    - >
      Attribution rests on infrastructure overlap plus MENORAH
      tooling tie; infrastructure-overlap is a known weak primitive
      in the Iran-aligned ecosystem.
    - >
      "Lockheed SKW-ATB-7" marquee framing risks over-specifying the
      victim set in downstream brief language.
  sign_off_caveats:
    - >
      Brief must preserve "per Mandiant" framing on attribution and
      cite the WEP "likely" cap on the actor sub-claim.
    - >
      Brief must not assert exploitation independence beyond what
      same-day publication can support; carry the very_likely
      ceiling and the same-day independence caveat into the brief.
    - >
      Brief should not extrapolate the victim set beyond Mandiant's
      stated claim; avoid implying all A&D primes are confirmed
      victims when only the marquee product is named.

tlp: CLEAR
published_in_briefs: []
retracted: false
retraction_brief_id: null
---

# [TEST FLASH] CVE-2099-88888: Pre-auth RCE in Lockheed SKW-ATB-7 in active exploitation, Mandiant attributes to APT34

> **THIS FINDING IS GRADED FROM SYNTHETIC TEST DATA.** Source raw signal
> `raw-2026-05-04-test-flash-001` is a Session 9 Stage 2 controlled-test
> seed. CVE-2099-88888 is a deliberately impossible CVE ID. The "Lockheed
> Skunk Works Avionics Test Bench (SKW-ATB-7)" affected product is
> fictitious. The APT34 attribution is a controlled test scenario. This
> finding exists for FLASH-pipeline grading-shape validation; do NOT
> propagate to production channels, do NOT publish to `#flash-alerts` or
> `#intel-briefs`, do NOT update actor dossiers from this finding.

## Summary

Two A-grade sources (CISA KEV, Mandiant) independently confirm active
in-the-wild exploitation of a critical pre-authentication RCE
(CVE-2099-88888, CVSS 10.0) in the Lockheed Martin SKW-ATB-7 avionics test
bench, deployed at multiple ITAR-regulated aircraft programs. CISA added
the CVE to KEV on 2026-05-04 with a 2026-05-25 federal patch deadline; no
vendor patch is currently available. Mandiant attributes the exploitation
to APT34 (OilRig, roster #023) with self-reported high confidence based on
infrastructure overlap with prior operations.

## What is corroborated, what is single-source

- **Corroborated (A1):** CVE existence, CVSS 10.0, KEV listing, no patch
  available, active exploitation in the wild, affected product/version
  range. CISA + Mandiant agree on the technical and severity facts.
- **Single-source (A1, veto applied):** APT34 attribution and the MENORAH
  post-exploitation chain rest on Mandiant alone. CISA KEV does not name
  an actor.

## WEP per claim

| Sub-claim | Sources | WEP | Notes |
|---|---|---|---|
| CVE exists, CVSS 10.0, KEV-listed, no patch | CISA + Mandiant | almost certainly | CISA is the primary record for its own catalog state. |
| Active exploitation in the wild | CISA + Mandiant | very likely | Same-day independent A-tier confirmation; "very likely" rather than "almost certainly" reflects that same-day independence is asserted but not stress-tested. |
| Attributed to APT34 (OilRig) | Mandiant only | likely | Single-source veto applied; cap at "likely" regardless of Mandiant's self-reported "high confidence" until independent corroboration. |

Dominant finding-level WEP ceiling: **very likely** — the operationally
relevant claim is active exploitation, not the CVE catalog state and not
the attribution.

## Why not "almost certainly" on the dominant claim

CISA KEV and Mandiant both publish 2026-05-04 (same day). Independence is
plausible (different evidence bases — CISA vetting process vs. Mandiant
IR telemetry) but not stress-testable on a 0-hour window. INTEL-GRADING
WEP table puts "almost certainly" at >95%. Without a time-separated
second confirmation and without first-party Splunk corroboration (per the
controlled-test override for this run), the 95% floor is hard to defend.
"Very likely" (85–95%) absorbs the residual independence question without
losing urgency.

## First-party telemetry status

No first-party Splunk corroboration available; this finding is
open-source-only. Per the controlled-test override, external Splunk was
not queried for this run. Hard Rule 8 honored — silent first-party is not
treated as contradicting evidence.

## Hard Rule compliance

- **Rule 2 (no originating attribution):** Compliant. Attribution to
  APT34 is reported as Mandiant's claim with Mandiant's self-reported
  confidence and is downgraded by Archimedes to WEP "likely" via
  single-source veto. Archimedes does not originate the attribution.
- **Rule 8 (first-party precedence):** Honored. Absence of first-party
  Splunk telemetry recorded as a grading consideration; not treated as
  contradicting evidence.

## FLASH triggers fired

- `critical-cve-exploited` — CVSS 10.0 ≥ 9.0, active exploitation, source A-grade
- `tracked-actor-attribution` — APT34 is roster #023 (MEDIUM threat_level)
- `zero-day-no-patch` — no vendor patch available at finding creation

Override conditions (CVSS 10.0 + active exploitation + tracked actor +
A&D watchlist hit) all met. Override would-have-applied; moot in active
hours. Recorded `flash_override_eligible: true` for audit completeness.

## Red-Team Review

**Disposition: sign-off. WEP recommendation: unchanged (very_likely).**

Contrarian ACH ran three alternatives against the same evidence set:

- **H_alt1 — attribution misplaced (false-flag or wrong Iran cluster):** Iran-aligned ecosystem shares infrastructure rental; infrastructure-overlap is a weak primitive. Counter: Mandiant cites MENORAH tooling, which is APT34-specific in prior reporting. Already absorbed by single-source veto on sc3 (cap at likely).
- **H_alt2 — exploitation claim overstated (scanning/PoC, not compromise):** CISA KEV can be triggered by single-vendor reporting; same-day publication does not prove independent telemetry. Counter: KEV requires in-the-wild evidence; Mandiant claims IR telemetry; specific affected versions and TCP/9443 ingress consistent with compromise rather than scanning. Residual risk already reflected in sc2's very_likely (not almost_certainly) cap.
- **H_alt3 — marquee-victim narrative inflation:** Vendor blogs anchor on prominent victims; actual victim set may be broader/less prime-focused. Not material to the FLASH-relevant claim; carry as caveat in brief language.

**Single point of failure:** The active-exploitation claim has one effective evidence pillar (Mandiant IR telemetry); CISA KEV can derive from vendor reporting. Already disclosed in sc2 rationale.

**Hard Rule status:** Rule 2 PASS (attribution reported, not originated; veto applied). Rule 8 PASS (absent first-party telemetry treated as silent, not contradicting).

**Caveats to preserve in brief:** (1) "per Mandiant" framing on attribution with WEP likely cap; (2) same-day independence caveat on the exploitation claim — do not promote to almost_certainly; (3) do not extrapolate victim set beyond Mandiant's marquee product.

## Open items for downstream agents

- **Red-team review required** (WEP very likely): challenge the same-day
  independence assumption and the single-source attribution downgrade
  scope; confirm "very likely" rather than "almost certainly" survives.
- **Analyst review deferred** per FLASH fast-path doctrine; full SAT
  catch-up only if this finding persists into the next-day brief cycle.
- **Actor-profiler:** do NOT update APT34 dossier from this finding —
  test data flag forbids dossier propagation.
