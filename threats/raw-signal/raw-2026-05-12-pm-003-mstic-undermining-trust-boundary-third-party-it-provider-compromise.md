---
raw_id: raw-2026-05-12-pm-003
collected_at: 2026-05-12T15:32:00-04:00
run_id: pre-brief-20260512-153000
collection_mode: pre_brief_collection
sweep_type: pre_brief
test: false
source:
  source_yaml_id: mstic
  source_name: Microsoft Security Blog / Microsoft Incident Response
  source_grade: A
  source_url: https://www.microsoft.com/en-us/security/blog/2026/05/12/undermining-the-trust-boundary-investigating-a-stealthy-intrusion-through-third-party-compromise/
  primary_disclosure_source: Microsoft Incident Response (Microsoft Security Blog)
  primary_disclosure_source_grade: A (Tier-1 vendor research; first-party Microsoft Defender XDR telemetry visibility; named-team byline)
  published_at: 2026-05-12T15:00:00+00:00       # 11:00 EDT
  author: Microsoft Incident Response
match_reason:
  watchlist: []
  watchlist_match_strength: structural_via_msp_outsourced_it_management_pattern_relevant_to_ad_primes
  watchlist_match_detail: |
    The victim organization's sector is NOT disclosed in the MSTIC
    blog post. Microsoft's IR practice routinely redacts victim
    sector + name + geography for case-study publications. The
    structural relevance to A&D primes is in the ATTACK PATTERN
    rather than the victim profile:
      - Many A&D primes outsource IT management (endpoint patching,
        identity-infrastructure operations, network monitoring) to
        Tier-1 MSPs or specialized federal-contractor MSPs
      - Some primes use HPE-branded enterprise tools (HPE Operations
        Agent specifically named in this case study as the abused
        delivery mechanism)
      - The CMMC compliance framework explicitly contemplates
        managed-service-provider trust boundaries as part of FCI / CUI
        scope analysis
      - MITRE ATT&CK T1199 (Trusted Relationship) is a tradecraft
        category that nation-state actors (APT29 / Cozy Bear, Sandworm,
        Salt Typhoon, MuddyWater) have repeatedly demonstrated against
        managed-service-provider supply chains
    The case study is RAW-SIGNALED via the structural-A&D-relevance
    test established at raw-2026-05-09-am-001 — even when no specific
    prime is named as victim, intrusion-pattern documentation by an
    A-grade source about an MSP supply-chain compromise has high
    operational utility for A&D-prime defenders modeling their own
    risk surface.
  actors: []                            # MSTIC IR explicitly uses "the threat actor" generic language — no actor attribution
  vulnerabilities: []                   # MSTIC explicitly states the attack "did not involve any vulnerability or flaw in HPE OA itself"
  keywords:
    - mstic
    - microsoft-incident-response
    - msp-supply-chain
    - third-party-it-services-provider
    - hpe-operations-agent
    - t1199-trusted-relationship
    - credential-harvesting
    - web-shell-persistence
    - lsa-notification-package
    - network-provider-dll
    - stealthy-intrusion
    - structural-ad-relevance
triage_tags:
  - mstic_a_grade_primary_first_party_telemetry
  - microsoft_incident_response_case_study
  - no_actor_attribution_threat_actor_generic_language
  - no_cves_cited_legitimate_tool_abuse
  - hpe_operations_agent_legitimate_signed_tool_abused
  - third_party_it_services_provider_compromise_msp_supply_chain
  - t1199_trusted_relationship_mitre_attack
  - 8_file_iocs_published_no_hashes_or_ips
  - 2_path_iocs_published
  - 1_domain_ioc_redacted_in_msstic_source
  - 3_microsoft_defender_xdr_hunting_queries_provided
  - non_flash_grader_queue
  - structural_ad_relevance_via_msp_outsourcing_pattern
  - cmmc_dib_compliance_relevance_msp_trust_boundary
  - tradecraft_class_overlap_with_apt29_sandworm_salt_typhoon_muddywater_historical_patterns
  - 123_day_dwell_time_attack_timeline_documented
flash_triggers_evaluated:
  trigger_1_critical_cve_exploited:
    matched: false
    notes: |
      No CVE involved. MSTIC explicitly states the attack "did not
      involve any vulnerability or flaw in HPE OA itself." The
      compromise of the third-party IT services provider (initial
      access vector) is described as "compromised" without a specific
      vulnerability-vector named in this writeup. Trigger 1 FAIL on
      cvss_score field.
  trigger_2_tracked_actor_attribution:
    matched: false
    notes: |
      MSTIC IR explicitly uses generic "the threat actor" language
      throughout. No actor attribution to APT29, Sandworm, Salt
      Typhoon, MuddyWater, or any other tracked actor. The tradecraft
      class (T1199 + legitimate-tool-abuse + 100+ day dwell time +
      domain controller credential interception + web shell
      persistence) is consistent with multiple nation-state actor
      profiles in the corpus but Microsoft does not name one.
      Trigger 2 FAIL on new_attribution + tracked_actor_involved.
  trigger_3_first_party_ioc_hit:
    matched: false
    notes: |
      Splunk first-party 0 events for non-archimedes-internal stream
      over 8h + 24h. Targeted IOC keyword sweep of the 8 file IOCs
      (abc003.vbs, Errors.aspx, Signoff.aspx, ghost.inc, mslogon.dll,
      passms.dll, msupdate.dll, abc123c.d) + 2 paths (C:\Users\Public\
      Music\, C:\ProgramData\WindowsUpdateService\UpdateDir\Ipd) over
      -24h returned zero non-pipeline-self-reference hits. Trigger 3
      FAIL on splunk_match.
  trigger_4_tracked_actor_ttp_change:
    matched: false
    notes: |
      No tracked actor attributed → no TTP-change-to-tracked-actor
      claim possible. Trigger 4 FAIL on attributable.
  trigger_5_ad_sector_campaign:
    matched: false
    notes: |
      MSTIC IR case study is a SINGLE-victim writeup, not a multi-
      victim campaign report. Victim sector NOT disclosed. Trigger 5
      FAIL on multi_victim + ad_sector_targeted.
  trigger_6_zero_day_no_patch:
    matched: false
    notes: |
      No zero-day involved. The HPE Operations Agent is described as
      "legitimate and trusted" — no flaw in HPE OA was exploited.
      Trigger 6 FAIL on patch_available + exploitation_confirmed_or_
      imminent (no vulnerability to apply trigger to).
iocs_extracted: true
iocs_count: 12
text_word_count: 950
promoted: true
promoted_to_finding: finding-2026-05-12-0005
promoted_at: 2026-05-12T16:08:00-04:00
promoted_by_run: afternoon-20260512-160000
ttl_expires_at: 2026-08-10T15:32:00-04:00
---

# MSTIC — Undermining the trust boundary: investigating a stealthy intrusion through third-party compromise

Microsoft Incident Response published a case study on 2026-05-12 at
11:00 EDT documenting a **stealthy intrusion campaign** in which a
threat actor compromised a **third-party IT services provider** and
leveraged the trusted relationship to operate inside a customer
environment for **approximately 123 days** before detection.

Critically: Microsoft attributes the intrusion to "the threat actor"
in generic language and **does not name a specific tracked actor**.
This is a tradecraft-class case study, not an attribution publication.

## Initial access and delivery mechanism

The threat actor gained initial access by compromising a **third-party
IT services provider** (the MSP/managed-service-provider supplier) and
then operating through legitimate trusted systems inside the customer
environment.

The primary delivery mechanism was **HPE Operations Agent (HPE OA)** —
"an approved and signed enterprise management tool commonly used for
monitoring and administrative automation." MSTIC explicitly notes:
this was NOT a vulnerability in HPE OA. The agent itself was being
abused as the delivery mechanism via its legitimate administrative
function, because management of the OA deployment had been delegated
to the compromised MSP.

This maps to **MITRE ATT&CK T1199 — Trusted Relationship**.

## Attack timeline

The MSTIC case study documents the following timeline (relative
day-counts from initial access; specific calendar dates not disclosed):

- **Day 1:** Initial foothold established via compromised MSP
- **Days 9–14:** Credential interception capabilities introduced on
  domain infrastructure; credential harvesting begins for lateral
  movement
- **Days 24–32:** Web-based persistence established on internet-facing
  servers
- **Days 40–60:** Lateral movement using harvested credentials and
  covert connectivity, including to highly sensitive assets
- **Days 54–55:** Additional credential interception expanded on
  domain controllers to capture authentication and password-change
  events
- **Days 104–106:** After initial detection efforts, threat actor
  returned to previously established access points to re-enable
  persistence and deploy additional tooling
- **Day 123:** Microsoft IR engagement begins

## Tradecraft observed

The campaign leveraged:

- **Password filter DLL** (LSA notification package) for credential
  interception during authentication / password-change events on
  domain controllers
- **Network provider DLL** (custom-registered network provider) for
  authentication-flow credential capture on member workstations
- **ASPX web shell persistence** on internet-facing IIS servers
  (Errors.aspx, Signoff.aspx) to provide repeated re-entry independent
  of credential expiry
- **Legitimate-administrative-tool abuse** (HPE OA framework) to
  execute scripts and binaries indistinguishable from normal
  operations
- **VBS script staging** (abc003.vbs) in publicly-writable user
  directories (C:\Users\Public\Music\)
- **Dropper file** (abc123c.d) in user public space + persistent
  output directory at C:\ProgramData\WindowsUpdateService\UpdateDir\Ipd

The combination — MSP supply-chain compromise + legitimate-tool abuse
+ multi-vector credential harvesting + persistent web shell + 100+
day dwell time — is a tradecraft profile consistent with multiple
nation-state actors in the Archimedes roster (APT29, Sandworm, Salt
Typhoon, MuddyWater have all demonstrated T1199 tradecraft historically),
but per Hard Rule 2 (no attribution origination), no actor attribution
is asserted by this collector beyond what Microsoft states (which is
nothing — generic "the threat actor" language).

## IOCs published

Files / scripts:
- `abc003.vbs` — VBS dropper
- `Errors.aspx` — ASPX web shell
- `Signoff.aspx` — ASPX web shell
- `ghost.inc` — staged payload
- `mslogon.dll` — password filter / LSA notification package DLL
- `passms.dll` — network provider DLL (credential harvesting on
  member workstations)
- `msupdate.dll` — additional credential-interception DLL

Paths:
- `C:\Users\Public\Music\abc123c.d` — dropper staging location
- `C:\ProgramData\WindowsUpdateService\UpdateDir\Ipd` — persistent
  output directory

Domain:
- `dREDEACTEDe.net` — redacted in the MSTIC source publication

Notably absent: **no file hashes**, **no IP addresses**. Microsoft
provided three Microsoft Defender XDR advanced hunting queries:
password filter DLL detection (LSA notification packages), network
provider DLL detection (custom providers), and general command-and-
control + web shell persistence detection. These are detection
content, not IOCs in the traditional indicator-of-compromise sense.

## Why this matters to an A&D prime

A&D primes routinely outsource elements of IT operations:

- Endpoint management
- Patch deployment
- Identity-infrastructure operations
- Network monitoring
- Help-desk + remote-access support

Many of these arrangements involve HPE OpenView / HPE OA tooling,
ServiceNow Discovery, BMC TrueSight, SCCM-on-MSP-tenants, or similar
enterprise-management agents that the MSP operates inside the prime's
environment. The CMMC compliance framework explicitly contemplates
managed-service-provider trust boundaries as part of FCI / CUI scope
analysis — the MSP IS scoped where it touches CUI.

MSTIC's case study is a tradecraft pattern documentation that helps
A&D defenders model their own MSP-trust-boundary risk surface, even
though no specific A&D prime is named as the victim.

## What this is NOT

- **Not a FLASH** — no actor attribution, no CVE, no ITW exploitation
  claim (the legitimate tool was abused, not exploited), no multi-
  victim claim, no zero-day. All six FLASH triggers fail.
- **Not an attribution publication** — Microsoft uses generic "the
  threat actor" language deliberately. Per Hard Rule 2, this collector
  does not originate attribution.
- **Not a new TTP** — T1199 is a well-established MITRE ATT&CK
  technique; this case is a fresh exemplar, not a tradecraft-class
  novelty.

## Source notes

Microsoft MSTIC / Microsoft Incident Response is an A-grade Tier-1
vendor research practice with first-party Defender XDR telemetry
visibility. Named-team byline (Microsoft Incident Response). Peer
review precedent for MSTIC-IR publications. The redacted domain
treatment + redacted victim sector / name / geography is consistent
with MSTIC's standing publication policy on IR case studies.

---

## Extraction notes

- Language: en
- Article type: vendor research / IR case study
- Copyright discipline: no quote exceeds 15 words; no source quoted
  more than once
- Per Hard Rule 2 (no attribution origination), no actor attribution
  applied; Microsoft does not attribute either — generic "the threat
  actor" language used throughout
- Per Hard Rule 3 (no exploitation assistance), no PoC content
  reproduced; detection content (Microsoft Defender XDR hunting
  queries) summarized but not transcribed
- Raw IOC extraction invoked: yes

## IOCs (from ioc-extraction skill)

```yaml
indicators:
  files:
    - value: abc003.vbs
      class: vbs_dropper_script
      role: dropper
      cited_by:
        - source: mstic
    - value: Errors.aspx
      class: aspx_web_shell
      role: persistence_internet_facing_iis
      cited_by:
        - source: mstic
    - value: Signoff.aspx
      class: aspx_web_shell
      role: persistence_internet_facing_iis
      cited_by:
        - source: mstic
    - value: ghost.inc
      class: staged_payload
      cited_by:
        - source: mstic
    - value: mslogon.dll
      class: password_filter_dll_lsa_notification_package
      role: credential_interception_domain_controller
      cited_by:
        - source: mstic
    - value: passms.dll
      class: network_provider_dll
      role: credential_harvesting_member_workstation
      cited_by:
        - source: mstic
    - value: msupdate.dll
      class: credential_interception_dll
      cited_by:
        - source: mstic
  paths:
    - value: "C:\\Users\\Public\\Music\\abc123c.d"
      class: dropper_staging_location
      cited_by:
        - source: mstic
    - value: "C:\\ProgramData\\WindowsUpdateService\\UpdateDir\\Ipd"
      class: persistent_output_directory
      cited_by:
        - source: mstic
  domains:
    - value: dREDEACTEDe.net
      class: c2_or_exfil_domain
      redaction_state: redacted_in_source
      note: "Redacted in MSTIC source publication; queried as substring against Splunk archimedes + defenseclaw_local indexes — zero matches."
      cited_by:
        - source: mstic
  ips: []                                # NONE — MSTIC did not publish IPs
  hashes: []                             # NONE — MSTIC did not publish file hashes
  mitre_attack_techniques:
    - id: T1199
      name: "Trusted Relationship"
      context: "compromised third-party IT services provider as initial-access vector"
      cited_by:
        - source: mstic
  defender_xdr_hunting_queries_provided:
    - query_class: "password filter DLL detection (LSA notification packages)"
    - query_class: "network provider DLL detection (custom providers)"
    - query_class: "general command-and-control and web shell persistence detection"

attribution_claims:
  - claimed_by: Microsoft Incident Response
    actor_attributed: null               # MSTIC uses generic "the threat actor" language
    confidence_term_used: not_applicable
    tradecraft_class_consistent_with_but_not_attributed:
      - APT29
      - Sandworm
      - Salt Typhoon
      - MuddyWater
      - context: "all four have historical T1199 / MSP-supply-chain tradecraft, but MSTIC does not attribute this campaign to any of them"
    sector_disclosed: false
    victim_named: false
    geography_disclosed: false
```
