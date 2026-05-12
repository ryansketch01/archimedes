---
raw_id: raw-2026-05-12-pm-004
collected_at: 2026-05-12T15:32:00-04:00
run_id: pre-brief-20260512-153000
collection_mode: pre_brief_collection
sweep_type: pre_brief
test: false
source:
  source_yaml_id: cisa-advisories
  source_name: CISA Cybersecurity & Infrastructure Security Agency (Industrial Control Systems advisories)
  source_grade: A
  source_urls:
    - https://www.cisa.gov/news-events/ics-advisories/icsa-26-132-05    # ABB AC500 V3 Stack Buffer Overflow CVE-2025-15467 CVSS 9.8
    - https://www.cisa.gov/news-events/ics-advisories/icsa-26-132-03    # ABB AC500 V3 Multiple Vulnerabilities CVSS 8.3
    - https://www.cisa.gov/news-events/ics-advisories/icsa-26-132-06    # ABB WebPro SNMP Card PowerValue CVSS 8.8
    - https://www.cisa.gov/news-events/ics-advisories/icsa-26-132-04    # ABB Automation Builder Gateway for Windows CVSS 5.3
    - https://www.cisa.gov/news-events/ics-advisories/icsa-26-132-02    # Subnet Solutions PowerSYSTEM Center CVSS 8.2
    - https://www.cisa.gov/news-events/ics-advisories/icsa-26-132-01    # Fuji Electric Tellus CVSS 7.8
  primary_disclosure_source: CISA + affected vendors (ABB, Subnet Solutions, Fuji Electric)
  primary_disclosure_source_grade: A (CISA government source — technically vetted before publication per source-grades.yaml rationale)
  published_at: 2026-05-12T12:00:00+00:00       # 08:00 EDT — all six advisories published simultaneously
  authors: CISA (vendor-coordinated advisories)
match_reason:
  watchlist: []
  watchlist_match_strength: structural_via_ics_critical_infrastructure_and_defense_manufacturing_deployment
  watchlist_match_detail: |
    The six CISA ICS advisories cover three vendors (ABB / Subnet
    Solutions / Fuji Electric) and four affected products (ABB AC500
    V3, ABB WebPro SNMP Card PowerValue, ABB Automation Builder
    Gateway, Subnet Solutions PowerSYSTEM Center, Fuji Electric
    Tellus). None of these vendors is listed in
    infrastructure/watchlists/aerospace-defense.yaml directly, but
    ICS / PLC / industrial-networking equipment in this product class
    is widely deployed across A&D primes' manufacturing facilities,
    test ranges, propulsion-test stands, and weapon-system integration
    labs.

    Specifically:
      - ABB AC500 V3 = PLC platform deployed in industrial automation
        including aerospace / defense manufacturing facilities for
        process control, machinery interlocks, and safety systems
      - ABB WebPro SNMP Card PowerValue = UPS monitoring card
        commonly deployed in data-center / industrial UPS
        infrastructure across A&D facilities
      - Subnet Solutions PowerSYSTEM Center = critical-manufacturing
        + energy SCADA platform
      - Fuji Electric Tellus = HMI / SCADA software for industrial
        automation

    Per the structural-A&D-relevance test established at
    raw-2026-05-09-am-001 (OpenC3 COSMOS), refreshed at
    raw-2026-05-12-am-001 (SAP) + am-002 (Siemens RUGGEDCOM ROX) +
    pm-001 (Microsoft Patch Tuesday) + pm-002 (Fortinet PSIRT), this
    CISA ICS batch is RAW-SIGNALED via the same rationale: the
    cluster impacts the structural OT / industrial-automation layer
    that A&D manufacturing and test-environment infrastructure
    depends on, even without prime-specific advisory language.

    Notable: This batch dropped at 12:00 UTC = 08:00 EDT, JUST AFTER
    the 07:30 EDT morning sweep boundary. The backstop-reach-to-
    morning-brief window on the 15:30 pre-brief sweep is what surfaced
    it — validates the doctrine for source-cadence resilience on
    asynchronous CISA publication times.
  actors: []                            # NO threat actor attribution for any advisory; ABB AC500 V3 Stack Buffer Overflow is "publicly reported" but no specific actor named; Subnet Solutions + Fuji Electric advisories are internal-discovery framings
  vulnerabilities:
    - cve_id: CVE-2025-15467
      product: ABB AC500 V3 PM5xxx 3.9.0, 3.9.0_HF1
      class: out_of_bounds_write_oobw
      severity: critical
      cvss_v3: 9.8
      advisory_id: ICSA-26-132-05
      mechanism: |
        When parsing CMS (Auth)EnvelopedData structures that use AEAD
        ciphers such as AES-GCM, the IV (Initialization Vector)
        encoded in the ASN.1 parameter could be processed in a way
        that triggers a stack buffer overflow leading to crash, DoS,
        or potentially remote code execution.
      itw_exploitation: false
      critical_infrastructure_sectors:
        - Chemical
        - Critical Manufacturing
        - Energy
        - Water and Wastewater
      countries_areas_deployed: Worldwide
      company_headquarters: Switzerland
    - cve_id: CVE-2025-2595
      product: ABB AC500 V3 < 3.9.0, 3.9.0
      class: direct_request_forced_browsing
      severity: high
      cvss_v3: 8.3
      advisory_id: ICSA-26-132-03
      mechanism: "Bypass user management to read visualization files"
      itw_exploitation: false
    - cve_id: CVE-2025-41659
      product: ABB AC500 V3 < 3.9.0, 3.9.0
      class: incorrect_permission_assignment_for_critical_resource
      severity: high
      cvss_v3: 8.3
      advisory_id: ICSA-26-132-03
      mechanism: "Read and write certificates and keys"
      itw_exploitation: false
    - cve_id: CVE-2025-41691
      product: ABB AC500 V3 < 3.9.0, 3.9.0
      class: null_pointer_dereference
      severity: high
      cvss_v3: 8.3
      advisory_id: ICSA-26-132-03
      mechanism: "Denial-of-service"
      itw_exploitation: false
    - cve_id: CVE-2026-26289
      product: Subnet Solutions PowerSYSTEM Center 2020 5.8.x-5.28.x / 2024 6.0.x-6.1.x / 2026 7.0.x
      class: incorrect_authorization
      severity: high
      cvss_v3: 8.2
      advisory_id: ICSA-26-132-02
      mechanism: "Authenticated attacker information disclosure"
      itw_exploitation: false
      critical_infrastructure_sectors:
        - Critical Manufacturing
        - Energy
      countries_areas_deployed: Worldwide
      company_headquarters: Canada
    - cve_id: CVE-2026-33570
      product: Subnet Solutions PowerSYSTEM Center 2020 5.11.x-5.28.x
      class: incorrect_authorization_or_crlf_injection
      severity: high
      cvss_v3: 8.2
      advisory_id: ICSA-26-132-02
      itw_exploitation: false
    - cve_id: CVE-2026-35504
      product: Subnet Solutions PowerSYSTEM Center 2020 <=5.28.x / 2024 / 2026
      class: incorrect_authorization_or_crlf_injection
      severity: high
      cvss_v3: 8.2
      advisory_id: ICSA-26-132-02
      itw_exploitation: false
    - cve_id: CVE-2026-35555
      product: Subnet Solutions PowerSYSTEM Center 2024 / 2026
      class: incorrect_authorization_or_crlf_injection
      severity: high
      cvss_v3: 8.2
      advisory_id: ICSA-26-132-02
      itw_exploitation: false
    - cve_id: CVE-2026-8108
      product: Fuji Electric Tellus 5.0.2
      class: exposed_dangerous_method_or_function
      severity: high
      cvss_v3: 7.8
      advisory_id: ICSA-26-132-01
      mechanism: |
        Installation adds a kernel driver granting all users read and
        write permissions, enabling privilege escalation from user to
        system; resulting capability includes DoS, file open, or file
        deletion.
      itw_exploitation: false
      critical_infrastructure_sectors:
        - Critical Manufacturing
      countries_areas_deployed: Worldwide
      company_headquarters: Japan
      vendor_recommendation: "Install Tellus only with administrator privileges"
    - cve_id: CVE-2024-41975
      product: ABB Automation Builder < 2.9.0, 2.9.0
      class: initialization_of_resource_with_insecure_default
      severity: medium
      cvss_v3: 5.3
      advisory_id: ICSA-26-132-04
      mechanism: |
        Gateway listens on all available network adapters by default,
        permitting unauthenticated remote search for PLCs (though
        PLC user-management prevents actual PLC access unless
        disabled).
      itw_exploitation: false
    - cve_ids_grouped:
        - CVE-not-published-by-cisa-summary  # ABB WebPro SNMP Card PowerValue multiple-vulnerabilities advisory ICSA-26-132-06 covers multiple CVEs but summary did not enumerate individual CVE IDs; product affected versions <=1.1.8.k, 1.1.8.p
      product: ABB WebPro SNMP Card PowerValue <=1.1.8.k, 1.1.8.p
      class:
        - improper_check_for_unusual_or_exceptional_conditions
        - incorrect_implementation_of_authentication_algorithm
        - insufficient_session_expiration
      severity: high
      cvss_v3: 8.8
      advisory_id: ICSA-26-132-06
      mechanism: |
        Local-network attacker can gain unauthorized access, cause
        insufficient session expiration leading to resource
        unavailability, and trigger uncontrolled resource consumption
        leading to DoS.
      itw_exploitation: false
  keywords:
    - cisa-ics-advisory
    - abb-ac500-plc
    - subnet-solutions-powersystem-center
    - fuji-electric-tellus
    - abb-webpro-snmp-card
    - abb-automation-builder-gateway
    - critical-manufacturing
    - structural-ad-relevance
triage_tags:
  - cisa_a_grade_primary
  - ics_batch_six_advisories_2026_05_12
  - abb_ac500_v3_critical_oobw_cvss_98_no_itw
  - cve_2025_15467_publicly_reported_vulnerability_no_actor_named
  - subnet_solutions_powersystem_center_cluster_cvss_82
  - fuji_electric_tellus_kernel_driver_privesc
  - abb_webpro_snmp_card_local_network_attack
  - abb_automation_builder_gateway_insecure_default_listening
  - no_threat_actor_attribution_any_advisory
  - patches_or_firmware_updates_available_all_six_advisories
  - non_flash_grader_queue
  - structural_ad_relevance_via_ot_industrial_automation_deployment
  - sibling_to_microsoft_patch_tuesday_pm_001_and_fortinet_pm_002
  - same_treatment_precedent_as_siemens_am_002_ruggedcom_ros_sharp
  - sbom_for_ai_guidance_policy_governance_discarded_separately
  - published_post_morning_sweep_boundary_backstop_reach_validated
flash_triggers_evaluated:
  trigger_1_critical_cve_exploited:
    matched: false
    notes: |
      CVE-2025-15467 (ABB AC500 V3 Stack Buffer Overflow) is rated
      CVSS 9.8 Critical — meets the CVSS≥9.0 threshold. However,
      the advisory text describes it as "publicly reported
      vulnerability" — not as "actively exploited in the wild."
      Public reporting ≠ active exploitation. CISA advisories
      explicitly distinguish these — the KEV catalog is the proper
      authority for ITW-exploitation claims (no KEV entries for
      any of the six CVE clusters in this batch). Trigger 1 FAIL on
      the active_exploitation field.
  trigger_2_tracked_actor_attribution:
    matched: false
    notes: |
      NO threat-actor attribution for any of the six advisories.
      Trigger 2 FAIL on new_attribution + tracked_actor_involved.
  trigger_3_first_party_ioc_hit:
    matched: false
    notes: |
      Splunk first-party 0 events for non-archimedes-internal stream.
      Targeted IOC keyword sweep across all 10+ ICS CVE IDs over -24h
      returned zero non-pipeline-self-reference hits. Trigger 3 FAIL.
  trigger_4_tracked_actor_ttp_change:
    matched: false
    notes: |
      No tracked-actor TTP change documented. Trigger 4 FAIL.
  trigger_5_ad_sector_campaign:
    matched: false
    notes: |
      No active multi-victim A&D-sector campaign claimed in any
      advisory. CISA advisories are vendor-coordinated vulnerability
      disclosures, not campaign attribution reports. Trigger 5 FAIL.
  trigger_6_zero_day_no_patch:
    matched: false
    notes: |
      Patches / firmware updates ARE available at-disclosure for all
      six advisories. ABB advises customers to "update the latest
      firmware of affected products." Subnet Solutions and Fuji
      Electric similarly include vendor-fix references. Trigger 6
      FAIL on patch_available=false.
iocs_extracted: true
iocs_count: 10
text_word_count: 1080
promoted: true
promoted_to_finding: finding-2026-05-12-0006
promoted_at: 2026-05-12T16:08:00-04:00
promoted_by_run: afternoon-20260512-160000
ttl_expires_at: 2026-08-10T15:32:00-04:00
---

# CISA ICS batch — 2026-05-12: ABB AC500 V3 critical RCE + Subnet Solutions + Fuji Electric + ABB ancillary

CISA published a six-advisory ICS batch on 2026-05-12 at 12:00 UTC
(08:00 EDT), JUST AFTER the 07:30 EDT morning collection sweep
boundary. The batch covers three vendors and four affected product
families:

- **ABB AC500 V3** (PLC platform — critical infrastructure):
  ICSA-26-132-05 + ICSA-26-132-03 (combined 4 CVEs)
- **ABB WebPro SNMP Card PowerValue** (UPS monitoring):
  ICSA-26-132-06
- **ABB Automation Builder Gateway for Windows** (PLC-development
  toolchain): ICSA-26-132-04
- **Subnet Solutions PowerSYSTEM Center** (SCADA platform):
  ICSA-26-132-02 (4 CVEs)
- **Fuji Electric Tellus** (HMI / SCADA software): ICSA-26-132-01

A seventh CISA publication in this batch — **"Software Bill of
Materials for AI - Minimum Elements"** — is policy/governance
guidance jointly with G7 partners (Germany, Canada, France, Italy,
Japan, UK, EU). This is NOT threat-intel and is DISCARDED separately
per Mode 1 procedure (no watchlist / roster / vuln-index hit).

## Headline finding — CVE-2025-15467 ABB AC500 V3 CVSS 9.8

**ICSA-26-132-05 — ABB AC500 V3 Stack Buffer Overflow in
Cryptographic Message Syntax** is the most operationally significant
advisory in this batch:

- **CVE-2025-15467** — Out-of-bounds write, CVSS v3 9.8 (Critical)
- Affected: AC500 V3 PM5xxx 3.9.0, 3.9.0_HF1
- Mechanism: when parsing CMS (Auth)EnvelopedData structures using
  AEAD ciphers such as AES-GCM, the IV encoded in the ASN.1 parameter
  is processed in a way that triggers stack buffer overflow leading
  to crash, denial-of-service, or potentially remote code execution
- CISA classification: "publicly reported vulnerability" — this is
  NOT the same as "actively exploited in the wild" (the KEV catalog
  is the authority for ITW claims, and no KEV entry exists for this
  CVE)
- Critical Infrastructure Sectors: Chemical, Critical Manufacturing,
  Energy, Water and Wastewater
- Countries/Areas Deployed: Worldwide
- ABB Headquarters: Switzerland

This is the second consecutive CISA ICS advisory window in 2026 with
a ruggedized-or-industrial-networking critical RCE landing — paired
with the Siemens RUGGEDCOM ROX SSA-081142 / CVE-2025-40949
(authenticated command injection, CVSS 9.1) from this morning's
raw-2026-05-12-am-002.

## Subnet Solutions PowerSYSTEM Center cluster

**ICSA-26-132-02** documents a 4-CVE cluster in Subnet Solutions
PowerSYSTEM Center (2020, 2024, and 2026 versions):

- **CVE-2026-26289** — Incorrect authorization (authenticated info
  disclosure)
- **CVE-2026-33570** — CRLF injection
- **CVE-2026-35504** — Incorrect authorization
- **CVE-2026-35555** — Additional vulnerability class

All rated CVSS v3 8.2 (High). Affected versions span PowerSYSTEM
Center 2020 5.8.x → 5.28.x, 2024 6.0.x → 6.1.x, and 2026 7.0.x.
Critical Infrastructure Sectors: Critical Manufacturing + Energy.
Subnet Solutions HQ: Canada.

## Fuji Electric Tellus — kernel driver privilege escalation

**ICSA-26-132-01 / CVE-2026-8108 — Fuji Electric Tellus exposed
dangerous method or function**:

- CVSS v3 7.8 (High)
- Affected: Tellus 5.0.2
- Mechanism: Tellus installation adds a kernel driver granting all
  users read and write permissions, enabling privilege escalation
  from user to SYSTEM (temporary DoS, file open, or file deletion
  capability)
- Vendor recommendation: "install Tellus only with administrator
  privileges"
- Critical Infrastructure Sectors: Critical Manufacturing
- Fuji Electric HQ: Japan

## ABB AC500 V3 Multiple Vulnerabilities — ICSA-26-132-03

A 3-CVE cluster in the ABB AC500 V3 product line (separate from
ICSA-26-132-05):

- **CVE-2025-2595** — Forced browsing (bypass user management to
  read visualization files)
- **CVE-2025-41659** — Incorrect permission assignment (read/write
  certificates and keys)
- **CVE-2025-41691** — Null pointer dereference (DoS)

All rated CVSS v3 8.3 (High) per the CISA advisory.

## ABB WebPro SNMP Card PowerValue — ICSA-26-132-06

UPS monitoring card with multiple vulnerabilities:

- CVSS v3 8.8 (High)
- Affected: WebPro SNMP Card <=1.1.8.k, 1.1.8.p
- Three vulnerability classes: improper check for unusual conditions,
  incorrect authentication algorithm implementation, insufficient
  session expiration
- Local-network attack vector

## ABB Automation Builder Gateway for Windows — ICSA-26-132-04

Lower severity, secondary to the AC500 V3 batch:

- **CVE-2024-41975** — Initialization of resource with insecure
  default, CVSS v3 5.3 (Medium)
- Affected: Automation Builder <2.9.0, 2.9.0
- Mechanism: gateway listens on all network adapters by default,
  enabling unauthenticated remote PLC search (though PLC user-
  management prevents actual PLC access unless disabled)

## Why this matters to an A&D prime

ICS / PLC / SCADA equipment in this product class is widely deployed
across A&D primes' manufacturing facilities, test ranges, propulsion-
test stands, and weapon-system integration labs. Specifically:

- ABB AC500 V3 PLCs are used in industrial automation including
  aerospace / defense manufacturing for process control, machinery
  interlocks, and safety systems
- ABB WebPro SNMP Card PowerValue is deployed for UPS monitoring in
  data-center and industrial-UPS infrastructure across many primes
- Subnet Solutions PowerSYSTEM Center is a SCADA platform in
  critical-manufacturing and energy verticals
- Fuji Electric Tellus is HMI / SCADA software in industrial
  automation environments

The ICS-advisory-class structural-relevance precedent is already
established in this corpus via the Siemens RUGGEDCOM ROX +
ROS# + SIMATIC cluster (raw-2026-05-12-am-002 same morning).

## Procedural note — backstop-reach window validation

This batch was published at 12:00 UTC = 08:00 EDT, **just after** the
07:30 EDT morning collection sweep boundary. The 07:30 morning sweep's
CISA all.xml fetch correctly returned 0 in-window items at that point.
The 15:30 pre-brief sweep's **backstop-reach to 07:30 EDT** is what
surfaced this batch — validates the source-cadence-resilience design
in the collector mode-1 procedure for asynchronous CISA publication
times.

## What this is NOT

- **Not a FLASH** — multiple Criticals at CVSS≥9.0 (one at 9.8, two
  others structural-critical) but NO ITW exploitation per any
  advisory's text. All six FLASH triggers fail on the strict
  conjunction tests per the sentinel raw-signal `flash_triggers_
  evaluated` block.
- **Not a single-CVE finding** — this is a 6-advisory / 10+-CVE
  cluster. Grader should consider clustering with the SAP
  (finding-2026-05-12-0001) + Siemens (finding-2026-05-12-0002) +
  Microsoft Patch Tuesday (PM-001) + Fortinet (PM-002) into a
  combined "May 2026 enterprise + ICS patch backlog" sector-focus
  brief item, or list separately per briefer-composition choice.
- **Not attributed to any actor** — CISA advisories are vendor-
  coordinated vulnerability disclosures, not campaign attribution
  reports. CVE-2025-15467 ABB AC500 V3 OOBW is described as
  "publicly reported vulnerability" — that phrasing references the
  prior public disclosure of the underlying flaw, not a threat-actor
  source.

## Source notes

CISA (A-grade per source-grades.yaml) publishes ICS advisories in
coordination with affected vendors and the ICS Cyber Emergency
Response Team (CERT-ICS). Technical details are vetted before
publication.

---

## Extraction notes

- Language: en
- Article type: government advisory cluster (CISA ICS advisories)
- Copyright discipline: no quote exceeds 15 words; no source quoted
  more than once
- Per Hard Rule 2 (no attribution origination), no actor attribution
  applied; CISA does not attribute either
- Per Hard Rule 3 (no exploitation assistance), no PoC content
  reproduced
- Raw IOC extraction invoked: yes
- Note on "publicly reported vulnerability" phrasing in CISA
  ICSA-26-132-05: this is CISA's standard language indicating prior
  third-party disclosure of the underlying flaw; it is NOT a claim
  of active in-the-wild exploitation, which would be reflected in
  the KEV catalog (no KEV entry exists for CVE-2025-15467 as of this
  sweep)

## IOCs (from ioc-extraction skill)

```yaml
indicators:
  cves:
    - value: CVE-2025-15467
      vendor: ABB
      product: "AC500 V3 PM5xxx 3.9.0, 3.9.0_HF1"
      class: out_of_bounds_write
      severity: critical
      cvss_v3: 9.8
      advisory_id: ICSA-26-132-05
      itw_exploitation_reported: false
      critical_infrastructure_sectors: ["Chemical", "Critical Manufacturing", "Energy", "Water and Wastewater"]
      cited_by:
        - source: cisa-advisories
    - value: CVE-2025-2595
      vendor: ABB
      product: "AC500 V3 < 3.9.0, 3.9.0"
      class: direct_request_forced_browsing
      severity: high
      cvss_v3: 8.3
      advisory_id: ICSA-26-132-03
      itw_exploitation_reported: false
      cited_by:
        - source: cisa-advisories
    - value: CVE-2025-41659
      vendor: ABB
      product: "AC500 V3 < 3.9.0, 3.9.0"
      class: incorrect_permission_assignment_for_critical_resource
      severity: high
      cvss_v3: 8.3
      advisory_id: ICSA-26-132-03
      itw_exploitation_reported: false
      cited_by:
        - source: cisa-advisories
    - value: CVE-2025-41691
      vendor: ABB
      product: "AC500 V3 < 3.9.0, 3.9.0"
      class: null_pointer_dereference
      severity: high
      cvss_v3: 8.3
      advisory_id: ICSA-26-132-03
      itw_exploitation_reported: false
      cited_by:
        - source: cisa-advisories
    - value: CVE-2026-26289
      vendor: Subnet Solutions Inc.
      product: "PowerSYSTEM Center 2020 5.8.x-5.28.x / 2024 6.0.x-6.1.x / 2026 7.0.x"
      class: incorrect_authorization
      severity: high
      cvss_v3: 8.2
      advisory_id: ICSA-26-132-02
      itw_exploitation_reported: false
      critical_infrastructure_sectors: ["Critical Manufacturing", "Energy"]
      cited_by:
        - source: cisa-advisories
    - value: CVE-2026-33570
      vendor: Subnet Solutions Inc.
      product: "PowerSYSTEM Center 2020 5.11.x-5.28.x"
      class: crlf_injection
      severity: high
      cvss_v3: 8.2
      advisory_id: ICSA-26-132-02
      itw_exploitation_reported: false
      cited_by:
        - source: cisa-advisories
    - value: CVE-2026-35504
      vendor: Subnet Solutions Inc.
      product: "PowerSYSTEM Center 2020/2024/2026"
      class: incorrect_authorization
      severity: high
      cvss_v3: 8.2
      advisory_id: ICSA-26-132-02
      itw_exploitation_reported: false
      cited_by:
        - source: cisa-advisories
    - value: CVE-2026-35555
      vendor: Subnet Solutions Inc.
      product: "PowerSYSTEM Center 2024/2026"
      class: incorrect_authorization
      severity: high
      cvss_v3: 8.2
      advisory_id: ICSA-26-132-02
      itw_exploitation_reported: false
      cited_by:
        - source: cisa-advisories
    - value: CVE-2026-8108
      vendor: Fuji Electric
      product: "Tellus 5.0.2"
      class: exposed_dangerous_method_or_function
      severity: high
      cvss_v3: 7.8
      advisory_id: ICSA-26-132-01
      itw_exploitation_reported: false
      critical_infrastructure_sectors: ["Critical Manufacturing"]
      cited_by:
        - source: cisa-advisories
    - value: CVE-2024-41975
      vendor: ABB
      product: "Automation Builder < 2.9.0, 2.9.0"
      class: initialization_of_resource_with_insecure_default
      severity: medium
      cvss_v3: 5.3
      advisory_id: ICSA-26-132-04
      itw_exploitation_reported: false
      cited_by:
        - source: cisa-advisories

  advisory_no_individual_cves_enumerated:
    - advisory_id: ICSA-26-132-06
      vendor: ABB
      product: "WebPro SNMP Card PowerValue <=1.1.8.k, 1.1.8.p"
      severity: high
      cvss_v3: 8.8
      classes:
        - improper_check_for_unusual_conditions
        - incorrect_authentication_algorithm
        - insufficient_session_expiration
      itw_exploitation_reported: false
      note: "CVE IDs not enumerated in CISA all.xml advisory summary"
      cited_by:
        - source: cisa-advisories

attribution_claims: []                # NONE of the six advisories attributes any vulnerability to a threat actor; ABB CVE-2025-15467 is described as "publicly reported vulnerability" but no actor source named
```
