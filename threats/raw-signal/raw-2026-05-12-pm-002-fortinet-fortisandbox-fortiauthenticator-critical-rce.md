---
raw_id: raw-2026-05-12-pm-002
collected_at: 2026-05-12T15:32:00-04:00
run_id: pre-brief-20260512-153000
collection_mode: pre_brief_collection
sweep_type: pre_brief
test: false
source:
  source_yaml_id: bleepingcomputer
  source_name: BleepingComputer (media relay of Fortinet PSIRT vendor advisory)
  source_grade: B
  source_url: https://www.bleepingcomputer.com/news/security/fortinet-warns-of-critical-rce-flaws-in-fortisandbox-and-fortiauthenticator/
  primary_disclosure_source: Fortinet PSIRT (vendor official advisory)
  primary_disclosure_source_grade_proposed: A (provisional; first Archimedes-corpus surface — see source-grade-log block below; analog to siemens-productcert first-surface treatment 2026-05-12 morning)
  primary_disclosure_source_urls:
    - https://fortiguard.fortinet.com/psirt/FG-IR-26-136     # FortiSandbox CVE-2026-26083
    - https://fortiguard.fortinet.com/psirt                  # Fortinet PSIRT advisory index (FG-IR-26-* batch)
  published_at: 2026-05-12T18:23:09+00:00       # 14:23 EDT BleepingComputer relay; Fortinet PSIRT publication earlier same day
  author: Sergiu Gatlan
  note_on_fortinet_psirt_direct_fetch: |
    Direct WebFetch on the Fortinet PSIRT FG-IR-26-136 detail page
    returned ECONNREFUSED this sweep (intermittent server-side issue).
    Index page (fortiguard.fortinet.com/psirt) reachable and lists the
    full 2026-05-12 batch including FG-IR-26-136 + FG-IR-26-123 +
    FG-IR-26-131 + FG-IR-26-133 at advisory/severity/product level,
    but CVSS scores not exposed via index-page summary. The CVE-2026-44277
    FortiAuthenticator entry's specific FG-IR identifier was not
    exposed via this index sweep — captured via BleepingComputer relay
    only. Not workflow-blocking; treated as transient.
match_reason:
  watchlist: []
  watchlist_match_strength: structural_via_fortinet_security_appliance_deployment_at_ad_prime_perimeters_and_mfa
  watchlist_match_detail: |
    FortiSandbox (network sandboxing / advanced threat protection) and
    FortiAuthenticator (multi-factor authentication appliance + RADIUS
    + SAML + certificate authority) are not directly listed in
    infrastructure/watchlists/aerospace-defense.yaml — but Fortinet's
    security-appliance product family is broadly deployed across
    enterprise + government + critical-infrastructure environments
    including aerospace and defense contractors. Specific structural
    relevance:
      - FortiSandbox is commonly deployed inline with FortiGate
        next-gen firewalls at corporate perimeters and in CMMC / DIB
        compliance architectures
      - FortiAuthenticator backs MFA and SSO for VPN remote-access,
        admin-console authentication, and CAC/PIV smartcard
        integration at many federal-contracting environments
      - Fortinet advisories are frequently exploited in ransomware
        and cyber-espionage attacks against enterprise targets per
        BleepingComputer's historical-pattern context
    Per the structural-A&D-relevance test established in
    raw-2026-05-09-am-001 (OpenC3 COSMOS) and refreshed in
    raw-2026-05-12-am-001 / 002 / pm-001 (SAP / Siemens / Microsoft
    Patch Tuesday), Fortinet PSIRT critical RCE pair is RAW-SIGNALED
    via the same rationale: the cluster impacts the structural
    perimeter + identity layer that A&D primes' security architectures
    depend on, even without prime-specific advisory language.
  actors: []
  vulnerabilities:
    - cve_id: CVE-2026-26083
      product: FortiSandbox / FortiSandbox Cloud / FortiSandbox PaaS
      class: missing_authorization
      severity: Critical
      vector: "unauthenticated GUI access"
      cvss_v3_per_psirt_index: "not_exposed_in_index_summary"     # detail-page direct fetch ECONNREFUSED this sweep
      affected_versions:
        - "FortiSandbox 5.0, 4.4 (per Fortinet PSIRT index)"
        - "FortiSandbox Cloud 24, 23, 5.0"
        - "FortiSandbox PaaS 23.4, 23.3, 23.1, 22.2, 22.1"
      patched_versions_per_bleepingcomputer: "patched_versions_not_listed_in_article"
      itw_exploitation: false
    - cve_id: CVE-2026-44277
      product: FortiAuthenticator
      class: improper_access_control
      severity: Critical
      vector: "unauthenticated; execute unauthorized code or commands via crafted requests"
      cvss_v3_per_bleepingcomputer: "not_provided_in_article"
      affected_versions: "not exhaustively listed; cloud variant not affected per BleepingComputer"
      patched_versions:
        - "FortiAuthenticator 6.5.7"
        - "FortiAuthenticator 6.6.9"
        - "FortiAuthenticator 8.0.3"
      itw_exploitation: false
  keywords:
    - fortinet
    - fortisandbox
    - fortiauthenticator
    - critical-rce
    - unauthenticated
    - psirt
    - perimeter-security-appliance
    - mfa-appliance
    - structural-ad-relevance
triage_tags:
  - fortinet_psirt_a_grade_primary
  - critical_unauthenticated_rce_pair
  - cve_2026_26083_fortisandbox_missing_authorization_gui
  - cve_2026_44277_fortiauthenticator_improper_access_control
  - no_itw_exploitation_reported_either_cve
  - patches_available_at_disclosure
  - structural_ad_relevance_via_perimeter_and_mfa_appliance_deployment
  - non_flash_grader_queue
  - fortinet_psirt_first_archimedes_corpus_surface_provisional_a_grade_candidate
  - sibling_to_microsoft_patch_tuesday_pm_001_and_cisa_ics_pm_004_structural_cluster
  - bleepingcomputer_historical_pattern_context_ransomware_and_cyber_espionage
flash_triggers_evaluated:
  trigger_1_critical_cve_exploited:
    matched: false
    notes: |
      CVE-2026-26083 + CVE-2026-44277 are BOTH Critical-severity per
      Fortinet PSIRT classification. The CVSS v3 scores are not exposed
      in either the PSIRT index summary or the BleepingComputer relay
      article, so the strict >=9.0 CVSS test cannot be evaluated
      directly. However, BleepingComputer explicitly states "While the
      company didn't tag these two security flaws as being exploited
      in the wild" — Trigger 1 FAIL on the active_exploitation field
      regardless of CVSS-score-equivalence assumption.
  trigger_2_tracked_actor_attribution:
    matched: false
    notes: |
      Fortinet PSIRT advisory + BleepingComputer relay carry NO
      threat-actor attribution. Trigger 2 FAIL on new_attribution +
      tracked_actor_involved.
  trigger_3_first_party_ioc_hit:
    matched: false
    notes: |
      Splunk first-party 0 events for non-archimedes-internal stream.
      No FortiSandbox / FortiAuthenticator product-string keyword
      matches over -24h.
  trigger_4_tracked_actor_ttp_change:
    matched: false
    notes: |
      No tracked-actor TTP change documented this advisory. Trigger 4
      FAIL.
  trigger_5_ad_sector_campaign:
    matched: false
    notes: |
      No active multi-victim A&D-sector campaign claimed. This is
      pre-emptive vendor patching — Fortinet shipped patches at-
      disclosure. Trigger 5 FAIL on campaign_active + multi_victim +
      ad_sector_targeted.
  trigger_6_zero_day_no_patch:
    matched: false
    notes: |
      Patches ARE available at-disclosure per Fortinet PSIRT.
      Trigger 6 FAIL on patch_available=false.
iocs_extracted: true
iocs_count: 2
text_word_count: 720
promoted: true
promoted_to_finding: finding-2026-05-12-0004
promoted_at: 2026-05-12T16:08:00-04:00
promoted_by_run: afternoon-20260512-160000
ttl_expires_at: 2026-08-10T15:32:00-04:00
---

# Fortinet warns of critical RCE flaws in FortiSandbox and FortiAuthenticator

Fortinet's PSIRT shipped security advisories on 2026-05-12 disclosing
two **Critical-severity** vulnerabilities — one in FortiSandbox (the
network-sandboxing appliance) and one in FortiAuthenticator (the
multi-factor authentication appliance). Neither flaw is currently
tagged by Fortinet as being exploited in the wild, per BleepingComputer's
Sergiu Gatlan reporting on the disclosure.

## CVE-2026-26083 — FortiSandbox missing authorization (GUI)

Per Fortinet PSIRT FG-IR-26-136, this is a **missing-authorization
vulnerability** in the FortiSandbox web GUI permitting **unauthenticated
access**. Affected versions per the Fortinet PSIRT index page:

- FortiSandbox **5.0, 4.4** (on-prem)
- FortiSandbox Cloud **24, 23, 5.0**
- FortiSandbox PaaS **23.4, 23.3, 23.1, 22.2, 22.1**

CVSS v3 score was not exposed in the PSIRT index summary at the time
of collection (direct FG-IR-26-136 detail page returned ECONNREFUSED
this sweep). BleepingComputer's relay similarly did not include the
CVSS score, but tagged the vulnerability as Critical.

## CVE-2026-44277 — FortiAuthenticator improper access control

Per BleepingComputer's reporting, CVE-2026-44277 is an **improper-
access-control vulnerability** in FortiAuthenticator that allows an
**unauthenticated attacker to execute unauthorized code or commands
via crafted requests**. Patched versions:

- FortiAuthenticator **6.5.7**
- FortiAuthenticator **6.6.9**
- FortiAuthenticator **8.0.3**

The cloud variant is not affected, per BleepingComputer's relay. The
specific Fortinet PSIRT FG-IR identifier for CVE-2026-44277 was not
exposed via this collection sweep's PSIRT index fetch.

## Why this matters to an A&D prime

FortiSandbox and FortiAuthenticator are widely deployed across A&D
contractor environments. FortiSandbox sits inline as an advanced
threat-protection sandbox behind FortiGate next-gen firewalls; many
DIB / CMMC compliance architectures use it as the malware-detonation
tier of layered perimeter defense. FortiAuthenticator is a common
back-end for VPN MFA, admin-console authentication, RADIUS / SAML /
SCEP / OCSP, and certificate authority work — including environments
that integrate CAC / PIV smartcards for federal-contracting access
control.

Per BleepingComputer's historical-pattern context: "Fortinet
vulnerabilities are frequently exploited in ransomware and cyber-
espionage attacks." That pattern observation is editorial context
from the article, not a current ITW claim against either of these
two specific CVEs. The current advisory text from Fortinet PSIRT
explicitly states no in-the-wild exploitation.

## What this is NOT

- **Not a FLASH** — patches are available at-disclosure, no ITW
  exploitation reported, no tracked-actor attribution. All six
  FLASH triggers fail on the strict conjunction tests per the
  sentinel raw-signal `flash_triggers_evaluated` block.
- **Not currently exploited** per Fortinet PSIRT primary + BleepingComputer
  relay. Historical-pattern context noted but not asserted as an
  ITW claim against these CVEs specifically.
- **Not the only A&D-relevant patch event today** — Microsoft Patch
  Tuesday (PM-001) and the CISA ICS batch (PM-004) are concurrent
  structural-relevance items; the grader may consider clustering or
  separating per briefer-composition choice.

## Source notes

BleepingComputer (B-grade) provides the operational-context relay.
The primary disclosure is Fortinet PSIRT (vendor official advisory;
proposed at provisional A-grade as first Archimedes-corpus surface
for direct vendor-portal fetch — analog to siemens-productcert
first-surface treatment 2026-05-12 morning).

Direct fetch on FG-IR-26-136 detail page returned ECONNREFUSED this
sweep; the PSIRT index page (fortiguard.fortinet.com/psirt) was
reachable and confirmed FG-IR-26-136 plus three additional 2026-05-12
batch entries (FG-IR-26-123 / CVE-2025-53844 FortiOS OOBW CAPWAP
daemon High authenticated; FG-IR-26-131 / CVE-2025-53680 FortiAP
command-injection Medium authenticated; FG-IR-26-133 / CVE-2025-53870
FortiAP OS command-injection Medium authenticated). The 2026-05-12
PSIRT batch has 4 entries total visible to this sweep, with the
unauthenticated Critical pair (CVE-2026-26083 + CVE-2026-44277) the
operationally significant subset.

Treatment as provisional A is conservative for a vendor-official-
advisory first surface — Fortinet PSIRT is a well-established
disclosure channel for a vendor whose advisories are technically
vetted before publication, analogous to the Siemens ProductCERT
precedent from this morning's raw-2026-05-12-am-002.

---

## Extraction notes

- Language: en
- Article type: media relay of vendor PSIRT advisory
- Copyright discipline: no quote exceeds 15 words; no source quoted
  more than once
- Per Hard Rule 2 (no attribution origination), no actor attribution
  applied; sources do not attribute
- Per Hard Rule 3 (no exploitation assistance), no PoC content
  reproduced
- Raw IOC extraction invoked: yes

## IOCs (from ioc-extraction skill)

```yaml
indicators:
  cves:
    - value: CVE-2026-26083
      vendor: Fortinet
      product: FortiSandbox / FortiSandbox Cloud / FortiSandbox PaaS
      class: missing_authorization
      severity: critical
      vector: unauthenticated_gui_access
      cvss_v3: not_exposed_in_index_summary
      itw_exploitation_reported: false
      affected_versions:
        - "FortiSandbox 5.0"
        - "FortiSandbox 4.4"
        - "FortiSandbox Cloud 24"
        - "FortiSandbox Cloud 23"
        - "FortiSandbox Cloud 5.0"
        - "FortiSandbox PaaS 23.4"
        - "FortiSandbox PaaS 23.3"
        - "FortiSandbox PaaS 23.1"
        - "FortiSandbox PaaS 22.2"
        - "FortiSandbox PaaS 22.1"
      patched_versions: not_listed_in_article
      psirt_id: FG-IR-26-136
      cited_by:
        - source: bleepingcomputer
          context: "critical RCE flaw in FortiSandbox unauthenticated"
        - source: fortinet-psirt
          context: "FG-IR-26-136 index page entry; detail page ECONNREFUSED this sweep"
    - value: CVE-2026-44277
      vendor: Fortinet
      product: FortiAuthenticator
      class: improper_access_control
      severity: critical
      vector: unauthenticated_crafted_requests_code_execution
      cvss_v3: not_provided_in_article
      itw_exploitation_reported: false
      affected_versions: not_exhaustively_listed
      patched_versions:
        - "FortiAuthenticator 6.5.7"
        - "FortiAuthenticator 6.6.9"
        - "FortiAuthenticator 8.0.3"
      cloud_variant_affected: false
      psirt_id: not_exposed_in_index_summary_this_sweep
      cited_by:
        - source: bleepingcomputer
          context: "critical RCE flaw in FortiAuthenticator unauthenticated"

attribution_claims: []                  # NEITHER Fortinet PSIRT NOR BleepingComputer attributes these CVEs to any threat actor; BleepingComputer notes general "Fortinet vulnerabilities are frequently exploited in ransomware and cyber-espionage attacks" historical-pattern context but NOT as an ITW claim against either of these specific CVEs
```
