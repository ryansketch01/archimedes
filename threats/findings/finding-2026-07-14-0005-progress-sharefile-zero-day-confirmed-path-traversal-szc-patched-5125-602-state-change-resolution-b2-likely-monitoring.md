---
finding_id: finding-2026-07-14-0005
created_at: 2026-07-14T15:59:00-04:00
graded_by: grader
grading_run_id: afternoon-20260714-160000
grading_mode: scheduled_brief

# Continuity marker — STATE CHANGE / RESOLUTION
continuation_of: finding-2026-07-13-0003          # which continues finding-2026-07-10-0002 (the original ShareFile SZC emergency-shutdown event)
continuation_of_raw_signal: raw-2026-07-14-pm-002
state_change: >
  RESOLUTION of the tracked ShareFile SZC emergency-shutdown thread. Progress CONFIRMED the
  cause was a high-severity path-traversal zero-day and shipped patches (SZC 5.12.5 / 6.0.2).
  This closes the open "what was the credible external security threat" question the parent
  findings carried, and RETIRES the user-speculated CVE-2026-2699/2701 vector from
  finding-2026-07-13-0003 (Progress attributes the emergency to a NEW path-traversal flaw
  with a reserved-unpublished CVE, NOT to the March-patched CVEs).

# Core grading (from admiralty-grading skill output)
digraph: B2
source_reliability:
  grade: B
  source_name: BleepingComputer (Lawrence Abrams) relaying Progress Software's confirmation + patch advisory
  source_yaml_id: bleepingcomputer
  grade_rationale: >
    Reached Archimedes via BleepingComputer (B). The originating evidence basis is Progress
    Software's own vendor advisory (self-disclosure on its own product) — procedurally
    A-class per the F5 / Cisco PSIRT / OpenAI precedent — but the Progress advisory primary
    was NOT directly retrieved (relay-only). Anchored at B, the honest floor of what
    Archimedes holds, the same anchor as parent findings 07-10-0002 and 07-13-0003.
  provisional: false
  provisional_reason: >
    Progress Software has no dedicated source-grades.yaml id — advisory relayed via
    BleepingComputer, not directly retrieved. Librarian may consider a
    progress-self-disclosure vendor-on-own-product id (provisional A) on direct retrieval.
credibility:
  grade: 2
  checklist_passed:
    - probably_true_claims_coherent          # vendor confirms cause (path traversal), ships named fixed versions (5.12.5/6.0.2), reports no unauthorized access — internally coherent and consistent with the parent thread
    - probably_true_no_contradicting_ab      # no A/B source contradicts
    - probably_true_ttp_consistent           # authenticated-admin path traversal on the storage tier is a coherent data-exposure primitive; consistent with the high-value MFT/secure-file-sharing target profile
  grade_1_withheld_reason: >
    Grade 1 withheld — single evidence basis (Progress's advisory via one B relay), no
    independent corroboration, CVE reserved-but-unpublished (no CVE artifact to cross-match),
    no confirmed exploitation (vendor reports no unauthorized access). Err low → 2.
  rationale: >
    Progress confirmed that a high-severity path-traversal zero-day was the cause of last
    week's emergency ShareFile Storage Zone Controller shutdown directive, and released
    fixes in SZC 5.12.5 and 6.0.2. Affected: SZC 5.x and 6.x. The vulnerability lets an
    authenticated administrator read arbitrary files, write attacker-controlled content to
    arbitrary directories, or enumerate the filesystem. No confirmed active exploitation
    (Progress: no indication of unauthorized access). CVE reserved, publication ~2 weeks out.
corroboration:
  independent_sources:
    - bleepingcomputer         # single B relay of the same Progress upstream
  independent: false
  independence_test_passed: >
    FAILS. One B relay of the Progress vendor upstream. One effective evidence basis
    (Progress). No independent second basis.
first_party_precedence:
  applied: false
  splunk_evidence: null
  splunk_note: >
    No atomic IOCs published (no IPs/domains/hashes; CVE reserved-unpublished) — nothing to
    hunt. First-party sentinel clean this sweep. Hard Rule 8: silent Splunk does not
    disconfirm.
single_source_veto_applied: true
single_source_veto_note: >
  Veto retained — one effective evidence basis (Progress via one B relay). WEP capped at
  "likely." Lifts on: CVE publication + independent exploitation telemetry, a tracked-actor
  attribution from an A/B source, a named A&D-prime victim, or first-party observation.
wep_ceiling: likely
wep_ceiling_rationale: >
  "Likely," capped by the single-source veto. The core claim STRENGTHENS relative to the
  parent (vendor has now CONFIRMED a cause and shipped a patch, resolving the "credible
  external threat" ambiguity) but the evidentiary architecture is unchanged (one Progress
  upstream, one B relay), so the ceiling holds at likely. Exploitation remains unconfirmed.

# Inclusion eligibility
inclusion:
  eligible_for:
    - daily_brief_monitoring     # state-change/resolution of an already-published thread — monitoring-tier: "the ShareFile emergency is now explained + patched"
    - weekly_synthesis
  not_eligible_for:
    - daily_brief_action         # anti-repetition: the core event was action-surfaced via the parent findings (07-10 afternoon, 07-11 morning, 07-13 morning). This is a resolution update, not a fresh action item. Briefer applies final anti-repetition judgment.
    - flash                      # no vendor-confirmed exploitation, no actor, no A&D-prime victim
    - actor_profile_update       # no actor attributed

# Cluster metadata
cluster:
  topic: "Progress ShareFile SZC emergency — RESOLVED: confirmed path-traversal zero-day, patched (SZC 5.12.5 / 6.0.2); CVE reserved-unpublished; no confirmed exploitation; no actor"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-07-14-pm-002
  deduplicated_against:
    - raw-2026-07-10-pm-001                 # original emergency (parent finding-2026-07-10-0002)
    - raw-2026-07-13-flash-0600-002         # day-3 continuation (finding-2026-07-13-0003)
  attribution_claims: []                    # none — MOVEit/Cl0p reference in the thread remains historical analogy only (Hard Rule 2)
  supersedes_speculation: >
    RETIRES the user-speculated CVE-2026-2699/2701 vector from finding-2026-07-13-0003.
    Progress now attributes the emergency to a NEW path-traversal flaw (reserved CVE),
    not the March-patched CVEs. Vuln-tracker should mark the speculated pair as
    superseded-by-vendor-confirmation.

# Source-grade notes
source_grade_notes: >
  No revision proposed. Progress Software has no dedicated source id; if the reserved CVE
  publishes (~2 weeks) and Archimedes retrieves the Progress bulletin directly, librarian
  may add a progress-self-disclosure vendor-on-own-product id (provisional A precedent).

# Downstream handoff flags
analyst_review_required: true
analyst_review_note: >
  WEP "likely" → flagged, LIGHT. The parent finding-2026-07-10-0002 already ran full ACH/KAC
  that substantially cover this thread. Incremental need: (1) the resolution retires the
  speculated CVE-2026-2699/2701 vector — brief must state the confirmed cause is a NEW
  reserved-CVE path-traversal flaw, not the March CVEs; (2) exploitation remains
  unconfirmed (vendor reports no unauthorized access). No new ACH/KAC required.
red_team_review_required: false            # WEP "likely" < "very likely"
red_team_review: null
analyst_review_complete: true
analyst_review_run_id: analyst-20260714-160500
wep_ceiling_adjusted: null                 # no adjustment — stays "likely"

analysis_sections:
  sat_ach: null
  sat_kac:
    kac_analysis:
      assessment_under_review: >
        "A high-severity path-traversal zero-day (new reserved CVE) was the confirmed cause
        of the ShareFile SZC emergency shutdown, now patched (5.12.5 / 6.0.2); exploitation
        unconfirmed."
      analyzed_at: 2026-07-14T16:05:00-04:00
      analyzed_by: analyst
      invoking_context: "Afternoon-brief light-touch review; resolution/state-change of an already-published thread (parent 07-10-0002 carries the full ACH/KAC)."
      assumptions:
        - id: A1
          statement: "No active exploitation occurred (Progress: no indication of unauthorized access)."
          category: visibility
          stated: true
          why_must_be_true: "Underpins the 'resolution, not active-incident' framing."
          when_could_be_false: "Vendor detection is incomplete; a low-and-slow authenticated-admin abuse could evade the vendor's own visibility. Absence-of-evidence, not evidence-of-absence."
          evidence_for: [bleepingcomputer]
          evidence_against: []
          confidence: low
          centrality: material
          classification: qualify
        - id: A2
          statement: "The new reserved-CVE path-traversal flaw fully supersedes the user-speculated CVE-2026-2699/2701 vector."
          category: technology
          stated: true
          why_must_be_true: "Finding retires the speculated March-patched CVEs as the cause."
          when_could_be_false: "Vendor characterization is partial, or both the March CVEs and the new flaw are in play."
          evidence_for: [bleepingcomputer]
          evidence_against: []
          confidence: medium
          centrality: material
          classification: sound
        - id: A3
          statement: "The authenticated-administrator precondition materially bounds exploitability."
          category: technology
          stated: true
          why_must_be_true: "Severity/urgency framing depends on the attacker needing admin auth first."
          when_could_be_false: "A chainable pre-auth flaw exists on the same appliance, or admin creds are trivially obtained on exposed SZCs."
          evidence_for: [bleepingcomputer]
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify
      classifications_summary:
        sound: 1
        qualify: 2
        test: 0
        reject: 0
      remediation:
        status: proceed
        qualifying_caveats:
          - "'No unauthorized access' is a vendor detection-limited statement (absence-of-evidence); the emergency-shutdown directive itself signalled the vendor treated the threat as credible."
          - "Exploit requires an authenticated administrator — a material precondition that bounds, but does not eliminate, exposure on internet-facing SZCs."
      recommended_wep_after_test:
        stays: likely

# Vuln-tracker handoff
vuln_tracker_handoff:
  proposed: true
  updates_prior: finding-2026-07-13-0003
  cves:
    - cve: "RESERVED-UNPUBLISHED (Progress: publication ~2 weeks)"
      product: "Progress ShareFile Storage Zone Controller (SZC) 5.x / 6.x"
      type: "Path traversal (high severity) — authenticated-admin arbitrary file read/write/enumeration"
      fixed_in: ["SZC 5.12.5", "SZC 6.0.2"]
      exploited: "unconfirmed — vendor reports no unauthorized access"
      status: "VENDOR-CONFIRMED as the cause of the ShareFile SZC emergency shutdown; supersedes the user-speculated CVE-2026-2699/2701 vector"
  note: >
    STATE CHANGE for the ShareFile SZC watch: emergency cause now vendor-confirmed as a NEW
    path-traversal zero-day, patched (5.12.5/6.0.2), CVE reserved-unpublished. Mark the
    prior user-speculated CVE-2026-2699/2701 pair as superseded-by-vendor-confirmation.
    Watch signals: CVE publication (~2 weeks) + potential CISA KEV addition; any confirmed
    exploitation or published IOCs; actor attribution from an A/B source; named A&D victim.

# Lifecycle
tlp: CLEAR
published_in_briefs: [2026-07-14-afternoon]
retracted: false
retraction_brief_id: null
---

# Progress confirms a path-traversal zero-day was behind the ShareFile Storage Zone Controller emergency shutdown — now patched (5.12.5 / 6.0.2)

## Summary

Progress Software confirmed that a high-severity path-traversal zero-day was the cause of
last week's emergency directive to shut down ShareFile Storage Zone Controllers, and it has
released fixes in SZC 5.12.5 and 6.0.2. This resolves the open question the tracked
ShareFile thread has carried since 2026-07-10 (finding-2026-07-10-0002 and its 07-13
continuation): the "credible external security threat" is now explained as a specific flaw
with a patch available. The vulnerability lets an authenticated administrator read, write,
or enumerate arbitrary files on the SZC host. Progress reports no indication of unauthorized
access — active exploitation is unconfirmed. The CVE is reserved but not yet published
(Progress: roughly two weeks out). This vendor confirmation retires the user-speculated
CVE-2026-2699/2701 vector from finding-2026-07-13-0003.

## Sources

### BleepingComputer (bleepingcomputer, digraph: B) — relay of Progress advisory

- URL: https://www.bleepingcomputer.com/news/security/progress-confirms-sharefile-zero-day-flaw-behind-storage-zone-shutdown/
- Published: 2026-07-14T12:08:47-04:00 (Lawrence Abrams)
- Key claim: Progress confirms a path-traversal zero-day caused the SZC shutdown; fixes
  shipped in 5.12.5 / 6.0.2; no indication of unauthorized access; CVE reserved-unpublished.

### Originating primary (not directly retrieved)

- Progress Software customer/security advisory (vendor self-disclosure). No dedicated
  source-grades.yaml id; relay-conveyed.

## Technical detail

- **Vulnerability:** Path traversal (high severity). An authenticated administrator could
  read arbitrary files accessible to the app service account, write attacker-controlled
  content to arbitrary directories, or enumerate the filesystem layout.
- **Affected:** ShareFile Storage Zone Controller 5.x and 6.x (all versions).
- **Fixed:** SZC 5.12.5 and 6.0.2.
- **CVE:** reserved, not yet published (~2 weeks per Progress).
- **Exploitation:** unconfirmed. Progress states no indication of unauthorized access to any
  ShareFile customer account or data (11-word quote per Hard Rule 6).
- **Actor:** none attributed. Warning came "from a credible source" (no actor named).

## IOCs surfaced

- No atomic network IOCs (CVE reserved-unpublished; no IPs/domains/hashes). One reserved CVE
  handed to vuln-tracker as the vendor-confirmed vector (supersedes prior speculation).

## Relationship to existing findings

- **Resolution of finding-2026-07-13-0003** (day-3 continuation) and its parent
  **finding-2026-07-10-0002** (original emergency shutdown). Those findings graded the
  severe-exposure core (B2/likely, single-source veto) and left the cause and the
  precautionary-vs-active question open. This surface CONFIRMS the cause (a new
  path-traversal flaw) and delivers a patch, but does not confirm exploitation.
- **Supersedes** the user-speculated CVE-2026-2699/2701 vector from finding-2026-07-13-0003:
  the vendor-confirmed cause is a distinct new reserved-CVE flaw, not the March-patched CVEs.

## Open questions for analyst

- The confirmed cause is a NEW path-traversal zero-day with a reserved CVE — do NOT restate
  the March-patched CVE-2026-2699/2701 pair as the vector. That speculation is now retired.
- Exploitation remains unconfirmed (vendor reports no unauthorized access). Patch
  availability resolves the remediation path; it does not confirm compromise occurred.
- Anti-repetition: the core event was published across three prior briefs — surface this as
  a resolution update at monitoring tier. Briefer applies final judgment.

## Analytic notes (from analyst review)

Light-touch KAC only; the parent finding-2026-07-10-0002 already carries the full ACH/KAC for this thread. Two assumptions load-bear on the "resolution" framing. First, "no unauthorized access" is a vendor detection-limited statement — absence-of-evidence, not evidence-of-absence. The vendor's own emergency-shutdown directive signalled it treated the threat as credible, so the brief should not upgrade "vendor reports no access" into "no compromise occurred." Second, the flaw requires an authenticated administrator, which materially bounds exploitability on internet-facing SZCs and is worth stating alongside the "high severity" label. The supersession claim (new reserved-CVE flaw retires the speculated CVE-2026-2699/2701 pair) rests on the vendor's own characterization and is sound. WEP stays "likely," correctly capped by the single-source veto (one Progress upstream via one B relay). No adjustment.
