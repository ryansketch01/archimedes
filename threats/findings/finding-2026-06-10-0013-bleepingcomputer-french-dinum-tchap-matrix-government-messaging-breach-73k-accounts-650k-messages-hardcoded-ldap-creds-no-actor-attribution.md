---
finding_id: finding-2026-06-10-0013-bleepingcomputer-french-dinum-tchap-matrix-government-messaging-breach-73k-accounts-650k-messages-hardcoded-ldap-creds-no-actor-attribution
created_at: 2026-06-10T16:20:00-04:00
graded_by: grader
grading_run_id: afternoon-20260610-160000
grading_mode: scheduled_brief
test: false
status: graded

# Core grading (admiralty-grading skill output)
digraph: C3
digraph_layered:
  french_dinum_disclosed_tchap_education_shard_breach_2026_06_09: B2                    # BC primary; DINUM vendor self-disclosure procedurally A-equivalent but not directly retrieved
  affected_service_tchap_matrix_protocol_government_messaging_education_shard_hostname: B2 # BC primary
  scope_73000_accounts_650000_messages_13_5gb_exfil_account_device_metadata: B2          # BC primary; DINUM-disclosed via BC
  attack_method_social_engineering_account_hijacking_legitimate_user_compromise: B2       # BC primary; DINUM-disclosed via BC
  hardcoded_ldap_credentials_in_powershell_script_french_tax_authority_regional_director: B3  # BC editorial framing on credential-pivot vector; "allegedly" qualifier
  attribution_unknown_dinum_no_attribution_claimant_unidentified: B1                       # Verifiable absence
  response_dinum_account_blocked_cnil_alerted: B2                                          # BC primary; standard French govt incident-response cadence
  no_formal_iocs_released_at_this_hour: B1                                                 # Verifiable absence
  no_a_d_prime_named_victim_french_public_sector_only: B1                                  # Verifiable absence
  defensive_tradecraft_relevance_credential_handling_in_scripts_matrix_protocol_enterprise_messaging: C2  # Grader-side structural inference; cautionary-tale framing
  cluster_anchor: C3

digraph_anchor: >
  Cluster anchored on ONE B-grade media primary (BleepingComputer
  2026-06-09) of DINUM (French interministerial digital agency)
  incident disclosure. Direct URL returned 404 on collector
  retrieval; content reconstructed via BC homepage rotation +
  WebFetch summary. DINUM primary not directly retrieved this
  sweep.

  C3 (NOT B2) anchored because — by exception to the typical
  single-primary B2 floor — this cluster has several quality
  constraints that warrant a step-down:

    - SOURCE LETTER GRADE: One B-grade media primary with
      collector retrieval caveat (404 on direct URL; partial
      reconstruction via homepage rotation). DINUM primary
      not directly retrieved. Cluster letter would otherwise
      hold at B but the retrieval-quality caveat warrants C.

    - INDEPENDENCE TEST: Single-source cluster.

    - SUBSTANTIVE CONSTRAINTS:
      * No formal IOCs released by DINUM — defender-
        actionable signal is constrained to defensive
        tradecraft cautionary tale.
      * No threat actor attribution — claimant unidentified
        per DINUM; Hard Rule 2 strict.
      * No A&D-prime victim — French public sector incident
        with no direct A&D-prime relevance.
      * A&D-relevance is indirect/defensive-tradecraft only
        (credential-handling-in-scripts cautionary tale +
        Matrix protocol architectural model relevance).

    - INCLUSION threshold: C3 → monitoring inclusion only.
      NOT eligible for action-item brief inclusion or actor
      profile updates.

  Single-source veto APPLIED at cluster level on all
  predictive claim layers (no WEP claims >= "likely").

  Promotion rationale at C3 (vs. rejection): defensive
  tradecraft cautionary tale value — credential-handling
  failure (PowerShell scripts with hardcoded LDAP creds shared
  internally) + social-engineering account hijack maps directly
  to common A&D-prime attack vectors. Brief inclusion via Other
  Signal lane only, light handling.

source_reliability:
  cluster_anchor_grade: B
  cluster_anchor_grade_with_retrieval_caveat: C
  sources:
    - source_yaml_id: bleepingcomputer
      grade: B
      provisional: false
      role: "Sole-primary of DINUM Tchap breach disclosure (with retrieval caveat — 404 on direct URL, partial reconstruction via BC homepage rotation + WebFetch summary)"
    - source_yaml_id: dinum
      grade: B
      provisional: true
      provisional_proposed_addition: false
      role: "Originating French interministerial digital agency announcement (not yet in source-grades.yaml; first surface; conservative provisional B per allied-government-CERT-class precedent — ABW 2026-05-08, CCB 2026-06-01 baseline); primary not directly retrieved this sweep"
  grade_rationale: >
    Cluster letter grade steps down from B to C at the
    cluster anchor due to retrieval-quality caveat (BC URL
    404 on direct fetch; partial reconstruction). DINUM
    primary not directly retrieved. Conservative
    provisional posture pending direct DINUM primary
    retrieval next collector pass.
  provisional: true

credibility:
  grade: 3
  checklist_passed:
    - possibly_true_single_source_uncorroborated_but_source_is_b_grade
    - possibly_true_technical_claims_plausible_but_not_independently_verifiable
  rationale: >
    BC single-source with retrieval caveat. DINUM-disclosed
    procedural facts (scope, affected service, response) are
    plausible and consistent with established government-
    incident-disclosure cadence (CNIL DPA notification per
    standard French public-sector incident-response
    protocol). Hardcoded-LDAP-credentials-via-PowerShell-
    script editorial framing carries "allegedly" qualifier
    — credibility-3 cap on the credential-pivot mechanism
    layer specifically.

corroboration:
  independent_sources:
    - bleepingcomputer
  independent: false
  test_passed: >
    Single-source cluster. No independent media or vendor
    cross-corroboration available in-window. Watch signals:
    DINUM direct primary advisory; CNIL public statement;
    second tier-2 security media outlet (Le Monde, ANSSI
    coverage, The Record, BleepingComputer follow-up); any
    technical IR-firm telemetry attribution.

first_party_precedence:
  applied: false
  splunk_evidence: >
    No published IOCs (matrix.agent.education.tchap.gouv.fr
    is the VICTIM host, not attacker infrastructure). No
    first-party hunt actionable.

single_source_veto_applied: true
single_source_veto_layers:
  - cluster_anchor_single_b_grade_primary_with_retrieval_caveat
wep_ceiling: roughly_even_chance

inclusion:
  eligible_for:
    - daily_brief_monitoring
    - weekly_synthesis
    - other_signal_defensive_tradecraft_cautionary_tale

# Cluster metadata
cluster:
  topic: "French government Tchap encrypted messaging service (Matrix-protocol-based; DINUM-operated; education shard matrix.agent.education.tchap.gouv.fr) breached via social-engineering account hijack of legitimate user account; ~73K accounts exposed; ~650K messages scraped; 13.5GB documents/media exfil + account/device metadata; allegedly enabled by hardcoded LDAP credentials leaked in PowerShell script from French tax authority regional director; claimant unidentified per DINUM; CNIL alerted"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-06-10-pm-007
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

# French DINUM Tchap (Matrix-Protocol Government Messaging) Breached — ~73K Accounts / 650K Messages / 13.5GB Exfil via Social-Engineering Account Hijack + Hardcoded LDAP Creds in PowerShell Script (Claimant Unidentified)

## Summary

DINUM (French interministerial digital agency) announced on 2026-06-09 a breach of the education shard of Tchap, the French government Matrix-protocol-based encrypted messaging platform, per BleepingComputer. Scope per DINUM: approximately 73,000 accounts had information exposed, 650,000 messages were scraped, and 13.5GB of documents and media files were exfiltrated. The compromise method was social-engineering account hijacking of a legitimate user account on the education shard; supporting credential-pivot infrastructure was allegedly enabled by hardcoded LDAP credentials leaked in a PowerShell script shared internally by a French tax authority regional director. No threat actor was named; claimant remains unidentified per DINUM. CNIL (French DPA) was alerted per protocol. No formal IOCs at this hour. A&D-prime relevance is indirect — defensive tradecraft cautionary tale on credential-handling-in-scripts + Matrix-protocol enterprise-messaging architectural model.

## Sources

### BleepingComputer (bleepingcomputer, B — sole primary; URL retrieval caveat)

- URL: https://www.bleepingcomputer.com/news/security/french-govt-messaging-service-breached-in-account-hijacking-attack/
- Published: 2026-06-09 (in-window per BC homepage rotation)
- Retrieval caveat: Direct URL returned 404 on collector retrieval; content reconstructed via BC homepage rotation + WebFetch summary. Direct DINUM / Tchap primary retrieval recommended next collector pass.
- Key claim: DINUM disclosure framing + scope + attack method + credential pivot + response.

### DINUM (Direction Interministérielle du Numérique, B provisional — NOT directly retrieved this sweep)

- Originating French interministerial digital agency announcement
- First Archimedes-corpus surface; provisional B per allied-government-CERT-class precedent (ABW 2026-05-08, CCB 2026-06-01 baseline)

## Technical detail

### Affected service

- **Tchap** — French government encrypted messaging platform based on the Matrix protocol
- Civil-service equivalent of Signal/WhatsApp for inter-agency communication
- Self-hosted internally by DINUM
- Affected shard: `matrix.agent.education.tchap.gouv.fr` (education shard)

### Attack method

- Social engineering → account hijacking of a legitimate user account on the education shard
- Allegedly leveraged "hardcoded LDAP credentials leaked via a PowerShell script shared by a French tax authority regional director" (verbatim per BC) — credential-pivot vector

### Scope (per DINUM via BC)

- ~73,000 accounts had information exposed (email addresses, organizational details)
- ~650,000 messages scraped
- 13.5GB of documents and media files exfiltrated
- Account and device metadata exfiltrated

### Affected sectors

- French civil service
- French education sector
- French tax authority (credential origination point)
- **No A&D / aerospace / defense / military victim named**

### Attribution

- **No threat actor attribution.** Claimant remains unidentified per DINUM.

### Response

- DINUM: "the account originating the malicious requests has been identified" and "immediately blocked" (verbatim per BC)
- CNIL alerted per protocol
- Breach detected Sunday; DINUM announcement Monday 2026-06-09

## IOCs surfaced

No formal IOCs released by DINUM. Affected host hostname (`matrix.agent.education.tchap.gouv.fr`) is the VICTIM host, not attacker infrastructure.

## Relationship to existing findings

- **No direct prior finding tie-in** — first French DINUM surface in Archimedes corpus
- **Cross-corpus tracked-actor cross-walk (Hard Rule 2 strict — no extrapolation):**
  - APT28 (Fancy Bear / Forest Blizzard / GRU Unit 26165) — historically targets French government but DINUM did NOT attribute and no TTP-pattern match
  - APT29 (Cozy Bear / Midnight Blizzard / SVR) — similar concern but no signal-matching
  - Sandworm (APT44 / GRU Unit 74455) — destructive operations against French infrastructure not a fit (this is data-exfil class)

## Open questions for analyst

- **Defensive tradecraft cautionary tale:** the attack pattern (social-engineering account hijack + hardcoded credentials in scripts + LDAP credential reuse) maps directly to common A&D-prime attack vectors. PowerShell scripts shared internally with hardcoded credentials is a recurring vulnerability across enterprise environments. SAT-KAC consideration on assumption that A&D-prime defender posture on internal-script credential hygiene is meaningfully different from French civil-service posture.
- **Matrix protocol class relevance:** Some enterprises (including some A&D supplier networks) deploy Matrix-protocol-based internal messaging (Element, Synapse). The education-shard compromise is single-account-pivot rather than protocol-level, but the architectural model is portable. Watch signals on any Matrix-Synapse-related security advisory in next 30 days.
- **No-attribution-by-DINUM pattern:** SAT-ACH consideration on whether French government's no-attribution posture reflects (a) genuine attribution uncertainty, (b) deliberate operational discretion pending LE / DGSI investigation, or (c) attribution withheld for diplomatic-sensitivity reasons. Hard Rule 2 prevents Archimedes from filling the gap.
