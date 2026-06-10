---
finding_id: finding-2026-06-10-0015-bleepingcomputer-servicenow-incident-material-extension-am006-endpoint-api-now-related-list-edit-create-australia-platform-scope-bounding-ipv4-51-159-98-241
created_at: 2026-06-10T16:24:00-04:00
graded_by: grader
grading_run_id: afternoon-20260610-160000
grading_mode: scheduled_brief
test: false
status: graded

relates_to:
  - finding-2026-06-10-0006-bleepingcomputer-thn-securityweek-servicenow-api-exploitation-pending-cve-unauthenticated-rest-api-customer-instance-tables-internal-since-april-7
relation_type: material_extension_to_am006_specific_endpoint_scope_bounding_ioc_publication_patch_date

# Core grading (admiralty-grading skill output)
digraph: B2
digraph_layered:
  vulnerable_endpoint_api_now_related_list_edit_create_with_requires_authentication_false_misconfiguration: B2  # BC primary (Lawrence Abrams); extends AM-006 three-source consensus with new specific endpoint identification
  scope_bounding_australia_platform_release_or_certain_config_changes: B2                                       # BC primary; extends AM-006 scope-bounding language
  security_patch_applied_2026_06_05_not_today_patch_tuesday: B2                                                 # BC primary; verifiable timeline data
  detection_method_anomalous_activity: B2                                                                       # BC primary
  ipv4_ioc_51_159_98_241_published_per_bc: B2                                                                   # BC primary published IOC; first-party Splunk silent over -90d (silent not disconfirming)
  cve_status_pending_servicenow_evaluating_carry_forward_from_am006: B1                                          # Verifiable absence carry-forward from AM-006
  no_actor_attribution_carry_forward_from_am006: B1                                                              # Verifiable absence
  no_named_victims_carry_forward_from_am006: B1                                                                  # Verifiable absence
  disclosure_mechanism_customer_support_bulletin_behind_login_portal_no_public_cve_style_no_cisa_notification: B2  # BC editorial framing on disclosure-discipline layer
  material_extension_class_not_re_coverage_anti_repetition_preserved: B1                                          # Self-evident scope-of-update
  cluster_anchor: B2

digraph_anchor: >
  Cluster anchored on ONE B-grade media primary (BleepingComputer
  2026-06-09T21:34:00 UTC). This is a MATERIAL EXTENSION of
  finding-2026-06-10-0006 (AM brief ServiceNow finding) — NOT a
  fresh standalone surface. AM-006 was anchored on three
  publisher-independent B-grade primaries (BC + THN + SW) with
  cluster anchor B2. Today's pm-009 raw signal adds specific
  endpoint path, scope-bounding, IPv4 IOC, patch date, detection
  method — all new material since AM-006 coverage.

  B2 (not B1, not B3) anchored because:

    - SOURCE LETTER GRADE: One B-grade media primary on the
      extension layer. AM-006 cluster anchor already
      established at B2 via three-source consensus on the
      broader framing. The pm-009 signal extends that
      established cluster with single-source net-new
      specifics. Cluster letter holds at B.

    - INDEPENDENCE TEST: AM-006 three-source consensus
      provides the load-bearing independence test on the
      broader framing (vulnerability existence, internal
      awareness date, ServiceNow disclosure event). The
      extension layer (specific endpoint + scope-bounding +
      IOC) is BC sole-source this sweep — independence
      fails at the extension layer.

    - CREDIBILITY: Walk the checklist.
      * Grade 1 (Confirmed): FAILS at extension layer
        (BC single-source on new specifics).
      * Grade 2 (Probably True) PASSES: extension layer
        is consistent with AM-006 three-source consensus
        framing; technical claims internally coherent
        (specific endpoint path matches ServiceNow REST
        API URL pattern; scope-bounding to Australia
        platform release is consistent with ServiceNow's
        multi-region SaaS deployment model; IPv4 IOC is
        a single specific indicator); no contradicting
        source.

    - SUBSTANTIVE CLAIM LAYERS:
      * Specific endpoint identification + scope bounding
        + patch date + IPv4 IOC: B2 — BC sole-primary on
        new specifics; consistent with AM-006 broader
        framing.
      * Carry-forward CVE-pending status + no actor
        attribution + no named victims: B1 — verifiable
        absence layers unchanged from AM-006 consensus.
      * Disclosure-discipline editorial framing (customer
        support bulletin behind login portal, no CISA
        notification): B2 — BC editorial framing on
        disclosure-pattern observation.

  Single-source veto APPLIED on:
    - Single IPv4 IOC (51.159.98.241) layer — BC sole-
      source; per AM-006 layered grading precedent which
      already had this IOC at B2 layered. Splunk first-
      party silent over -90d (silent not disconfirming).
    - Specific endpoint path identification — BC sole-
      source on net-new specific endpoint; consistent
      with broader cluster framing.

  Single-source veto NOT applied on:
    - Cluster existence (carry-forward AM-006 three-
      source consensus on ServiceNow incident).
    - CVE-pending status (verifiable absence consensus).
    - Anti-repetition discipline: this is material
      extension class, not re-coverage.

source_reliability:
  cluster_anchor_grade: B
  sources:
    - source_yaml_id: bleepingcomputer
      grade: B
      provisional: false
      role: "Primary on extension layer (specific endpoint, scope-bounding, IPv4 IOC, patch date, detection method)"
  grade_rationale: >
    Cluster letter grade holds at B (single B-grade media
    primary on the extension layer). AM-006 three-source
    consensus provides the broader framing's independence
    test. This finding cross-references AM-006 for the
    load-bearing cluster anchor and adds net-new specifics
    only.
  provisional: false

credibility:
  grade: 2
  checklist_passed:
    - probably_true_consistent_with_am006_three_source_consensus_broader_framing
    - probably_true_no_contradicting_a_b_source
    - probably_true_technical_claims_internally_coherent_specific_endpoint_scope_bounding_patch_date_ipv4_ioc
  rationale: >
    Specific endpoint path (/api/now/related_list_edit/create)
    matches ServiceNow REST API URL pattern conventions. Scope-
    bounding to Australia platform release is consistent with
    ServiceNow's multi-region SaaS deployment model. Single
    IPv4 IOC (51.159.98.241) is operator-actionable for
    first-party hunt. Patch date 2026-06-05 (not today's Patch
    Tuesday) clarifies the disclosure-to-patch timeline beyond
    AM-006 framing. Detection method "anomalous activity"
    indicates ServiceNow's internal-discovery mechanism. All
    consistent with AM-006 three-source consensus broader
    framing.

corroboration:
  independent_sources:
    - bleepingcomputer
  independent: false
  test_passed: >
    Extension layer single-source. AM-006 cross-reference
    provides broader-framing independence test (THN + SW
    + BC three-source consensus on cluster existence,
    internal awareness date, ServiceNow self-disclosure
    event, no-CVE-pending status, no-actor-attribution,
    no-named-victims). The pm-009 net-new specifics are
    consistent with that broader consensus but not
    independently corroborated this sweep.

first_party_precedence:
  applied: true
  splunk_evidence: >
    Splunk first-party hunt executed against published
    IPv4 IOC (51.159.98.241) over -90d window (covers
    the April 7 → June 5 internal exposure period).
    RESULT: zero hits. Per Hard Rule 8 / INTEL-GRADING.md
    / sat-ach discipline: absence-of-evidence is NOT
    evidence-of-absence. Silent Splunk is NOT disconfirming
    of external claim; consistent with no known internal
    exposure to date. First-party precedence applied as
    "no contradiction."
  splunk_query_executed: "index=archimedes OR index=defenseclaw_local src_ip=\"51.159.98.241\""
  splunk_window: "-90d"
  splunk_result: "zero events"
  splunk_interpretation: "no_internal_exposure_to_published_ipv4_ioc_silent_not_disconfirming"

single_source_veto_applied: true
single_source_veto_layers:
  - single_ipv4_ioc_51_159_98_241_bc_sole_primary
  - specific_endpoint_path_identification_extension_layer
wep_ceiling: likely

inclusion:
  eligible_for:
    - daily_brief_action
    - weekly_synthesis
    - coverage_log_update_to_am006

# Cluster metadata
cluster:
  topic: "Material extension of finding-2026-06-10-0006 (ServiceNow API exploitation, pending CVE, internal since April 7). Net-new specifics per BleepingComputer 2026-06-09T21:34: vulnerable endpoint /api/now/related_list_edit/create with requires_authentication=false misconfiguration; scope bounded to customers on Australia platform release OR customers with certain configuration changes; security patch applied 2026-06-05 (not today's Patch Tuesday); detection method 'anomalous activity'; IPv4 IOC 51.159.98.241 published; disclosure mechanism customer support bulletin behind login portal (NOT public CVE-style, no CISA notification mentioned)"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-06-10-pm-009
  attribution_claims: []

# Downstream handoff flags
analyst_review_required: false
red_team_review_required: false
red_team_review: null
analysis_sections:
  sat_ach: null
  sat_kac: null

# Lifecycle
tlp: CLEAR
published_in_briefs: [2026-06-10-afternoon]
retracted: false
retraction_brief_id: null
---

# ServiceNow Material Extension — Specific Endpoint `/api/now/related_list_edit/create`, Australia-Platform Scope Bounding, IPv4 IOC 51.159.98.241, Patch 2026-06-05 (Extends finding-2026-06-10-0006)

## Summary

BleepingComputer published 2026-06-09T21:34 material extension to the ServiceNow security incident first reported in finding-2026-06-10-0006 (AM brief). Net-new specifics: vulnerable endpoint identified as `/api/now/related_list_edit/create` configured with `requires_authentication=false` before patching; scope bounded to "customers on the Australia platform release" or customers with "certain configuration changes"; security patch applied 2026-06-05 (NOT today's Patch Tuesday); detection method "anomalous activity"; published IPv4 IOC 51.159.98.241. Disclosure mechanism is customer support bulletin behind login portal — no public CVE-style disclosure, no CISA notification mentioned. Archimedes Splunk first-party hunt across `archimedes` + `defenseclaw_local` over -90d returned zero hits on the published IPv4 IOC (silent not disconfirming). CVE assignment still pending per ServiceNow. No actor attribution.

## Sources

### BleepingComputer (bleepingcomputer, B — sole primary on extension layer)

- URL: https://www.bleepingcomputer.com/news/security/servicenow-discloses-security-incident-exposing-customer-data/
- Published: 2026-06-09T21:34:00 UTC
- Key claim: Material extension to AM-006 with specific endpoint, scope bounding, IOC, patch date, detection method, disclosure mechanism.

### AM-006 cross-reference

Cluster anchor independence test is carried by finding-2026-06-10-0006 (BC + THN + SW three-source consensus on broader framing). This finding adds net-new specifics only.

## Technical detail

### Vulnerability identification (new)

- **Vulnerable endpoint:** `/api/now/related_list_edit/create`
- **Misconfiguration:** "allegedly configured with `requires_authentication=false` before being patched" (verbatim per BC)
- **Class:** Unauthenticated API access flaw allowing attackers to "query data from customer instances" (verbatim per BC)

### Scope bounding (new)

- Affected scope per BC: "primarily 'customers on the Australia platform release or made certain configuration changes'" (verbatim)
- Implication: configuration-dependent issue, not universal; defender lens is auditable (check Australia platform release tenancy + certain-configuration-change indicator)

### Timeline (new)

- **Security patch applied:** 2026-06-05 (NOT today's Patch Tuesday)
- **Detection method:** "anomalous activity"
- **Article publication:** 2026-06-09

### CVE status (carry-forward)

- "ServiceNow says it is still evaluating whether it will publish a CVE for the issue" (verbatim per BC)
- No CVE assigned as of this hour

### Named victims (carry-forward)

- None specifically identified in BC article (consistent with AM-006)

### Actor attribution (carry-forward)

- No threat actor attribution; BC references "attackers" without specific group naming. Hard Rule 2 preserved.

### Disclosure mechanism (new editorial framing)

- ServiceNow issued customer support bulletin behind login portal
- No public CVE-style disclosure
- No CISA notification mentioned
- More cautious disclosure pattern than typical vendor-on-own-product PSIRT class

## IOCs surfaced

### IPv4 address (new, BC-published)

- **51.159.98.241**

### Splunk first-party hunt result

Per Hard Rule 8 first-party precedence: Splunk queried across `archimedes` + `defenseclaw_local` for src_ip=51.159.98.241 over -90d (covers April 7 → June 5 internal exposure period). **Result: zero hits.**

Interpretation per sat-ach discipline: silent Splunk is NOT disconfirming; consistent with no known internal exposure to date. First-party precedence applied as "no contradiction."

## Relationship to existing findings

- **finding-2026-06-10-0006** — material extension; cluster anchor independence test carries over from AM-006 three-source consensus.

## Open questions for analyst

- **Brief composition guidance:** This finding can either be (a) coverage-log update line under AM-006 ServiceNow finding in PM brief (preferred — preserves anti-repetition discipline), or (b) presented as material-extension call-out in the PM brief with separate disclosure-of-the-day framing.
- **A&D-prime defender actionability:** ServiceNow is widely deployed across A&D primes for ITSM / SecOps workflow / vendor management. Operator-actionable items:
  - Splunk hunt extension: incoming connections to ServiceNow instances from IPv4 51.159.98.241 over April 7 → June 5 window
  - Configuration audit: check ServiceNow Australia-platform-release tenancy + `requires_authentication=false` configuration on `/api/now/related_list_edit/create`
- **Disclosure discipline observation:** No CISA notification + customer-support-bulletin-only is atypical for a customer-data-exposure incident at vendor scale. SAT-ACH consideration on whether this reflects (a) ServiceNow's bounded-scope assessment justifying limited disclosure, (b) operational discretion pending fuller incident analysis, or (c) disclosure-policy gap that warrants tracking if pattern continues.
