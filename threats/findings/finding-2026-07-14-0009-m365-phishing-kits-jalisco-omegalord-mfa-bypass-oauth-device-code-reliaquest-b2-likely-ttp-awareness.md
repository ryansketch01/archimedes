---
finding_id: finding-2026-07-14-0009
created_at: 2026-07-14T16:03:00-04:00
graded_by: grader
grading_run_id: afternoon-20260714-160000
grading_mode: scheduled_brief

# Core grading (from admiralty-grading skill output)
digraph: B2
source_reliability:
  grade: B
  source_name: BleepingComputer (Bill Toulas) relaying ReliaQuest research on Jalisco + OmegaLord M365 phishing kits
  source_yaml_id: bleepingcomputer
  grade_rationale: >
    Reached Archimedes via BleepingComputer (B). Originating research is ReliaQuest — a
    reputable MDR / threat-research vendor, but no prior Archimedes-corpus source grade
    (provisional on first citation). Anchored at B (the relay Archimedes holds); ReliaQuest
    flagged to librarian for a provisional grade addition.
  provisional: false
credibility:
  grade: 2
  checklist_passed:
    - probably_true_ttp_consistent          # OAuth 2.0 Device Authorization Grant abuse + fake-login credential + phone-number capture for MFA bypass are established, well-documented M365/Entra phishing TTPs; rapid SharePoint exfil-then-extort is a known pattern
    - probably_true_no_contradicting_ab      # no A/B source contradicts
    - probably_true_claims_coherent          # mechanisms internally coherent (real-time device-code generation to beat the 15-min validity window; up to 5 rogue devices with benign names; phone-number capture engineered for MFA bypass)
  grade_1_withheld_reason: >
    Grade 1 withheld — single evidence basis (ReliaQuest via one B relay), no independent
    corroboration, and no atomic IOCs to cross-match (source published none — kit names
    Jalisco/OmegaLord are researcher-coined tooling designations, not IOCs). Err low → 2.
  rationale: >
    ReliaQuest identified two M365-targeting phishing toolkits engineered to defeat MFA.
    Jalisco abuses the OAuth 2.0 Device Authorization Grant flow, generating fresh device
    codes in real time to beat Microsoft's 15-minute validity window, registers up to five
    rogue devices per account under benign names, and ships an operator portal. OmegaLord
    uses fake PDF-Reader login pages and captures email/password/phone, with the
    phone-number capture engineered to bypass MFA. Post-compromise, operators search
    SharePoint/SaaS and exfiltrate within minutes (as little as 6) before extortion.
corroboration:
  independent_sources:
    - bleepingcomputer         # single B relay of ReliaQuest research
  independent: false
  independence_test_passed: "FAILS — one B relay of a single originating researcher (ReliaQuest). One effective evidence basis."
first_party_precedence:
  applied: false
  splunk_evidence: null
  splunk_note: >
    No atomic IOCs published (no domains/URLs/IPs/hashes) — nothing to hunt. First-party
    sentinel clean this sweep. Hard Rule 8: silent Splunk does not disconfirm.
single_source_veto_applied: true
single_source_veto_note: "Veto applied — one effective evidence basis (ReliaQuest via one B relay). WEP capped at likely."
wep_ceiling: likely
wep_ceiling_rationale: >
  "Likely," capped by the single-source veto. This is a TTP-awareness item describing
  observed tooling, consistent with established M365/Entra device-code phishing tradecraft.
  A&D nexus STRUCTURAL — M365/Entra ID is the dominant identity + collaboration fabric across
  the DIB; OAuth device-code MFA-bypass + rapid SharePoint exfiltration is a directly
  portable TTP against A&D-prime tenants. No named A&D victim, no actor (Hard Rule 2).

# Inclusion eligibility
inclusion:
  eligible_for:
    - daily_brief_monitoring     # TTP-awareness / defensive-hardening item (Entra device-registration limits, block device-code auth via Conditional Access); high structural A&D relevance
    - weekly_synthesis
  not_eligible_for:
    - flash                      # no atomic IOCs, no active-exploitation CVE, no tracked actor, no named A&D victim
    - actor_profile_update       # no actor attributed

# Cluster metadata
cluster:
  topic: "M365 phishing kits Jalisco + OmegaLord defeat MFA via OAuth device-code abuse + phone-number capture; rapid SharePoint exfiltration then extortion (ReliaQuest)"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-07-14-pm-006
  attribution_claims: []       # kit names are researcher-coined tooling designations, not threat-actor attribution

# Source-grade notes (librarian awareness)
source_grade_additions_proposed:
  - source_yaml_id: reliaquest
    proposed_name: "ReliaQuest (GreyMatter / threat research)"
    proposed_grade: B
    provisional: true
    awaiting_direct_retrieval: true
    dual_grade: null
    grade_note: >
      First Archimedes-corpus citation via finding-2026-07-14-0009 (Jalisco + OmegaLord M365
      phishing kits). ReliaQuest is an established MDR / threat-research vendor with named
      published research. Provisional B is the conservative starting grade for a first-surface
      reputable vendor reaching via a B media relay (cf. Sysdig 2026-05-14, Socket 2026-05-14).
      Operator may upgrade to A on subsequent surfaces showing consistent first-party-telemetry
      rigor, or hold at B if relay-only citation persists. ReliaQuest primary NOT directly
      retrieved this sweep.
    first_cited: finding-2026-07-14-0009

# Downstream handoff flags
analyst_review_required: true
analyst_review_note: >
  WEP "likely" → flagged, LIGHT. No attribution. Ensure the brief: (1) presents this as
  ReliaQuest single-source TTP awareness (no independent corroboration, no IOCs); (2) surfaces
  the defensive levers (reduce Entra device-registration limits 50→1-2, block device-code auth
  via Conditional Access, restrict OAuth Device Authorization grants, audit app registrations)
  — directly actionable for A&D M365 tenants; (3) frames A&D nexus as structural TTP-class. No
  ACH/KAC needed.
red_team_review_required: false
red_team_review: null
analyst_review_complete: true
analyst_review_run_id: analyst-20260714-160500
wep_ceiling_adjusted: null                 # no adjustment — stays "likely"

analysis_sections:
  sat_ach: null
  sat_kac:
    kac_analysis:
      assessment_under_review: >
        "The Jalisco + OmegaLord M365 phishing kits are a TTP-awareness item with structural
        A&D relevance (M365/Entra ubiquity across the DIB), not a campaign targeting A&D
        primes; defensive levers are directly actionable."
      analyzed_at: 2026-07-14T16:05:00-04:00
      analyzed_by: analyst
      invoking_context: "Afternoon-brief KAC on the TTP-awareness framing and its A&D-relevance inference; single-source, no IOCs."
      assumptions:
        - id: A1
          statement: "This is generalized tooling / TTP awareness, NOT a campaign targeting A&D primes."
          category: intent
          stated: true
          why_must_be_true: "Determines whether the item is a defensive-hardening awareness note vs. a targeted-threat finding."
          when_could_be_false: "Later reporting reveals A&D-sector victimology; but the source names no sectors, victims, or targeting selectivity, so the awareness framing is well-supported."
          evidence_for: [bleepingcomputer]
          evidence_against: []
          confidence: medium
          centrality: material
          classification: sound
        - id: A2
          statement: "A&D relevance derives from M365/Entra being the dominant DIB identity fabric, making the TTP directly portable to A&D tenants."
          category: semantic
          stated: true
          why_must_be_true: "Justifies inclusion; the nexus is structural (ubiquity), not victim-named."
          when_could_be_false: "A&D tenants have already hardened device-code auth / device-registration limits, blunting portability; or the kits target consumer/SMB tenants with different configs."
          evidence_for: [bleepingcomputer]
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify
        - id: A3
          statement: "The kits exist and function as ReliaQuest describes (device-code abuse; phone-capture MFA bypass; sub-6-minute SharePoint exfil)."
          category: source_reliability
          stated: true
          why_must_be_true: "The defensive recommendations are calibrated to these specific mechanisms."
          when_could_be_false: "Single-source (ReliaQuest via one B relay), no atomic IOCs to corroborate; mechanisms are consistent with established M365/Entra device-code tradecraft, which raises prior plausibility."
          evidence_for: [bleepingcomputer]
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify
        - id: A4
          statement: "The item is actionable for A&D defenders."
          category: technology
          stated: false
          why_must_be_true: "Value of a TTP-awareness note depends on a defender being able to act on it."
          when_could_be_false: "No atomic IOCs published — defenders cannot hunt/block indicators; actionability is limited to posture-hardening (Conditional Access, device-registration limits, OAuth grant restriction), not detection."
          evidence_for: [bleepingcomputer]
          evidence_against: []
          confidence: high
          centrality: material
          classification: qualify
      classifications_summary:
        sound: 1
        qualify: 3
        test: 0
        reject: 0
      remediation:
        status: proceed
        qualifying_caveats:
          - "Present as ReliaQuest single-source TTP awareness — no independent corroboration, no atomic IOCs."
          - "Absence of IOCs limits actionability to posture-hardening (block device-code auth via Conditional Access, reduce Entra device-registration limits, restrict OAuth Device Authorization grants, audit app registrations) — defenders cannot hunt indicators."
          - "A&D relevance is structural (M365/Entra ubiquity), an inference from portability — not evidence of A&D-sector targeting."
      recommended_wep_after_test:
        stays: likely

# Vuln-tracker handoff
vuln_tracker_handoff:
  proposed: false
  note: "No CVE — TTP/tooling item, not a tracked vulnerability. No vuln-tracker action."

# Lifecycle
tlp: CLEAR
published_in_briefs: [2026-07-14-afternoon]
retracted: false
retraction_brief_id: null
---

# New M365 phishing kits Jalisco and OmegaLord defeat MFA via OAuth device-code abuse and phone-number capture, with SharePoint exfiltration in minutes

## Summary

ReliaQuest identified two phishing toolkits targeting Microsoft 365 accounts, both
engineered to defeat MFA. Jalisco abuses the OAuth 2.0 Device Authorization Grant flow,
generating fresh Microsoft device codes in real time to beat the 15-minute code-validity
window, registering up to five rogue devices per account under benign names like "Microsoft"
or "Windows," and shipping an operator portal to manage compromised accounts. OmegaLord uses
fake PDF-Reader login pages and captures email, password, and phone number — the phone
capture specifically engineered to bypass MFA. Post-compromise, operators search SharePoint
and SaaS for valuable data and exfiltrate within minutes (as little as six) before making
extortion demands. No domains, IPs, hashes, targeted sectors, or threat-actor attribution
were provided. M365/Entra ID is the dominant identity fabric across the defense industrial
base, making this a directly portable TTP against A&D-prime tenants.

## Sources

### BleepingComputer (bleepingcomputer, digraph: B) — relay of ReliaQuest research

- URL: https://www.bleepingcomputer.com/news/security/new-phishing-kits-target-microsoft-365-accounts-evade-mfa/
- Published: 2026-07-14T08:49:00-04:00 (Bill Toulas)
- Key claim: two MFA-bypass M365 phishing kits (Jalisco device-code abuse; OmegaLord
  fake-login + phone capture) with rapid SharePoint exfiltration then extortion.

### ReliaQuest (originating research; provisional B, not directly retrieved)

- Originating threat research. No prior Archimedes-corpus grade — flagged to librarian for a
  provisional-B source addition.

## Technical detail

- **Jalisco:** abuses the OAuth 2.0 Device Authorization Grant; generates fresh device codes
  in real time to beat the 15-minute validity window; registers up to five rogue devices per
  account under benign names; includes an operator web portal.
- **OmegaLord:** fake PDF-Reader login pages; collects email, password, and phone number
  (phone capture engineered for MFA bypass).
- **Post-compromise:** SharePoint / SaaS search + exfiltration within minutes (as little as
  6), then extortion demands threatening leaks.
- **Defensive levers noted:** reduce Entra ID device-registration limits (50 → 1-2); block
  device-code authentication via Conditional Access; restrict OAuth Device Authorization
  grants; audit unnecessary app registrations.
- No atomic IOCs published.

## IOCs surfaced

- None. Kit names Jalisco / OmegaLord are researcher-coined tooling designations, not
  indicators. No domains/URLs/IPs/hashes in source.

## Relationship to existing findings

- No direct prior-finding lineage. Adds to the corpus's ongoing M365/Entra identity-layer
  threat coverage (cf. finding-2026-07-14-0001 ShinyHunters OAuth Salesforce supply-chain,
  morning — related identity-layer theme, distinct campaign/tooling).

## Open questions for analyst

- Single-source (ReliaQuest via one B relay), no IOCs — present as TTP awareness, not a
  triangulated campaign finding.
- The defensive levers are directly actionable for A&D M365 tenants — worth surfacing.
- A&D nexus is STRUCTURAL TTP-class (portable against A&D-prime tenants); no named victim, no
  actor.

## Analytic notes (from analyst review)

KAC on the framing. The core assumption — that this is generalized tooling awareness, not an A&D-targeted campaign — is sound: the source names no sectors, victims, or targeting selectivity, so treating it as a defensive-hardening note is correct. The A&D relevance is an inference from M365/Entra ubiquity across the DIB (portability), not evidence of A&D-sector targeting; the brief should frame it that way. The load-bearing limitation is actionability: ReliaQuest published no atomic IOCs, so defenders cannot hunt or block indicators — value is confined to posture-hardening (block device-code auth via Conditional Access, cut Entra device-registration limits, restrict OAuth Device Authorization grants, audit app registrations). Those levers are directly usable and worth surfacing. Single-source (ReliaQuest via one B relay); the described device-code and phone-capture mechanisms are consistent with established Entra tradecraft, raising prior plausibility. WEP stays "likely." No adjustment; no ACH needed (no attribution).
