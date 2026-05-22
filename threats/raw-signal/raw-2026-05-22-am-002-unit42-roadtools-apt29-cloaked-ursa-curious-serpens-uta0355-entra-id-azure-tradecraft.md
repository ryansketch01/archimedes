---
raw_id: raw-2026-05-22-am-002-unit42-roadtools-apt29-cloaked-ursa-curious-serpens
collected_at: 2026-05-22T07:42:00-04:00
run_id: pre-brief-20260522-073000
collection_mode: pre_brief_collection
test: false
source:
  source_yaml_id: unit42
  source_name: "Unit 42 / Palo Alto Networks (Bill Batchelor + Eyal Rafian)"
  source_url: https://unit42.paloaltonetworks.com/roadtools-cloud-attacks/
  published_at: 2026-05-22T10:00:24+00:00
match_reason:
  watchlist: []
  actors:
    - APT29                      # roster #009 (Cozy Bear / The Dukes / NOBELIUM / Midnight Blizzard / Cloaked Ursa / UNC2452)
  vulnerabilities: []
  keywords:
    - roadtools
    - roadrecon
    - roadtx
    - entra_id
    - azure_ad
    - microsoft_graph_api
    - primary_refresh_token_prt_hijack
    - conditional_access_policy_bypass
    - mfa_circumvention
    - device_registration_persistence
    - t1098_005_device_registration
    - t1550_alternate_authentication_material
    - t1087_account_discovery
    - cloaked_ursa
    - midnight_blizzard
    - apt29
    - cozy_bear
    - svr
    - curious_serpens
    - peach_sandstorm
    - apt33
    - uta0355
    - volexity_2025
    - void_blizzard
    - desktop_random_8_digit_device_naming
    - os_version_10_0_19041_928
    - python_requests_ua
triage_tags:
  - tracked_actor_apt29_ttp_class_research
  - a_grade_vendor_unit42_primary_publication
  - microsoft_graph_api_living_off_trusted_services
  - entra_id_attack_surface_relevance_to_a_and_d_m365_tenancy
  - prt_hijack_class_for_a_and_d_sso_environments
  - multi_actor_roadtools_misuse_documented
  - apt33_curious_serpens_not_in_roster_potential_new_actor_candidate
  - uta0355_volexity_2025_named_not_in_roster
  - hard_rule_2_attribution_language_conservative_preserved
  - trigger_4_evaluation_candidate_for_grader
  - retrospective_documentation_of_2021_onward_tradecraft
  - no_a_and_d_prime_victim_named
iocs_extracted: true
iocs_count: 3   # UA-strings (2) + device-registration default OS (1); device-naming pattern is detection-side not strictly an IOC
text_word_count: 540
promoted: true
promoted_to_finding: finding-2026-05-22-0002
promoted_at: 2026-05-22T08:18:00-04:00
ttl_expires_at: 2026-08-20T07:42:00-04:00
---

# Unit 42 publishes "Paved With Intent: ROADtools and Nation-State Tactics in the Cloud" — formal A-grade vendor research on ROADtools misuse by Cloaked Ursa (APT29 = roster #009), Curious Serpens (APT33, not in roster), UTA0355 (not in roster), plus Void Blizzard (tag-only)

## Source

Unit 42 / Palo Alto Networks (Bill Batchelor + Eyal Rafian byline),
published 2026-05-22T10:00:24+00:00 (06:00 EDT). Vendor primary research,
A-grade per source-grades.yaml. Article URL:
https://unit42.paloaltonetworks.com/roadtools-cloud-attacks/

## What's new

Formal Unit 42 publication on the misuse of the open-source **ROADtools**
framework (Python-written, "for offensive and defensive security purposes,"
targeting "identity and authentication layers of Azure") by four named
nation-state actors. The ROADtools framework consists of two principal
modules:

- **roadrecon** — Enumerates Entra ID users, groups, roles, devices,
  service principals, applications, and configurations.
- **roadtx** — Facilitates token acquisition/exchange, device
  registration, and OAuth 2.0 / OpenID Connect flow support.

The framework "operates through legitimate Microsoft APIs" and can
"mimic typical traffic," enabling detection evasion through customized
user-agent strings — i.e., abuse of Microsoft Graph API as a living-off-
trusted-services attack surface.

## Named actors

### 1. Cloaked Ursa = Midnight Blizzard = APT29 (roster #009)

- **Roster entry:** id #009, threat_level HIGH, attribution Russia / SVR
- **Aliases per _roster.yaml:** Cozy Bear, The Dukes, NOBELIUM,
  Midnight Blizzard, UNC2452, Iron Hemlock, Cloaked Ursa, BlueBravo
- **Documented activity:** Began with "highly targeted spear phishing" in
  **late 2021**; uses ROADtools for "discovery and enumerate victims'
  Azure AD" environments after initial compromise.

### 2. Curious Serpens = Peach Sandstorm = APT33 (NOT in roster)

- **Roster entry:** None — APT33 is not currently in the 24-actor
  _roster.yaml. Iranian nation-state actor cluster.
- **Documented activity:** Used ROADtools after **password spray attacks
  in 2023**. Unit 42 names "Curious Serpens" as the Palo-Alto-internal
  alias for the Peach Sandstorm / APT33 cluster.

### 3. UTA0355 (NOT in roster; Russian-aligned per Volexity 2025)

- **Documented activity:** "State-affiliated Russian threat actor"
  conducting "targeted phishing campaign" in early 2025; Unit 42 cites
  Volexity 2025 as the originating attribution layer; "capabilities
  matching roadtx module's token management" per Unit 42 framing.

### 4. Void Blizzard

- **Documented activity:** Listed in article tags but **not discussed in
  article body** per the WebFetch extraction. Operational detail not
  surfaced this sweep.

## Documented TTPs (MITRE ATT&CK alignment)

| MITRE Tech | Name | Operational shape |
|------------|------|-------------------|
| T1098.005 | Account Manipulation: Device Registration | Rogue device registration in Entra ID as "durable means of persistence" |
| T1550 | Use Alternate Authentication Material | Stolen Primary Refresh Tokens (PRTs) for "persistent, programmatic access across the tenant" |
| T1087 | Account Discovery | Account enumeration via Microsoft Graph API endpoints |

**Additional cloud-specific behaviors:**

- Token lifecycle manipulation
- Conditional Access Policy (CAP) bypass via device-bound tokens
- MFA circumvention through device-bound tokens
- Rogue device registration with default parameters (OS Version
  10.0.19041.928 — flagged by Unit 42 as "different than the OS version
  for the other hosts" in target tenancies)

## IOCs surfaced by Unit 42

**User-Agent string indicators (network detection):**

- `roadtools` — direct identifier when attackers don't customize
- `python-requests/<version>` — default UA when roadtx is invoked
  without custom UA override

**Device-registration default indicator:**

- OS Version `10.0.19041.928` — appears as default when attackers
  register rogue devices via roadtools without specifying alternate OS
  version; Unit 42 frames as detection-side anomaly versus the OS
  versions present on legitimate tenancy hosts

**Device-naming pattern (detection-side, not strict IOC):**

- `DESKTOP-<RANDOM 8 DIGITS>` — default Windows host-naming pattern when
  attackers don't customize device name during registration

## Activity timeline

| Date | Event |
|------|-------|
| Late 2021 | Cloaked Ursa (APT29) operationalizes ROADtools post-spear-phishing |
| 2023 | Curious Serpens (APT33) uses ROADtools after password spray attacks |
| Early 2025 | UTA0355 phishing campaign with roadtx-token-management capability match (Volexity attribution) |
| April 2025 | Last update to msgraph branch in official ROADtools repository (project still active) |
| 2026-05-22 | Unit 42 publication date |

## Attribution language preserved verbatim per Hard Rule 2

Unit 42 does **NOT** use explicit "high confidence" or "moderate confidence"
attribution language for any of the four actors. Instead the framing is:

- "Early observation" + "came in late 2021" for Cloaked Ursa
  (established reporting carry-forward)
- "Volexity reported in 2025" for UTA0355 (third-party attribution
  layer cited; Unit 42 itself does NOT attribute UTA0355)
- No first-party confidence-level statements ("high confidence" /
  "moderate confidence" / "with high confidence we assess") are present
  in the body per WebFetch extraction

Conservative attribution discipline preserved verbatim. Archimedes
does NOT upgrade attribution per Hard Rule 2.

## A&D relevance

**M365 / Entra ID tenancy attack-surface applicability is direct.**

A&D primes in scope (Lockheed Martin, Boeing, RTX, Northrop Grumman,
General Dynamics, BAE Systems, L3Harris, Leidos, SAIC, Thales, GE
Aerospace, Safran, Honeywell Aerospace, Airbus, Elbit Systems per
watchlists/aerospace-defense.yaml) operate substantial Entra ID
tenancies, federated SSO with Microsoft Graph API surfaces, and
Conditional Access Policy enforcement. The ROADtools-misuse TTP cluster
documented here — particularly PRT hijack + CAP bypass + Microsoft Graph
API enumeration + rogue device registration for persistence — is
operationally directly applicable to A&D-prime M365 environments.

**Specific A&D-prime defensive priorities (for grader / analyst):**

- Audit Entra ID device-registration logs for anomalous OS versions
  (the 10.0.19041.928 default) and DESKTOP-<8 digit> naming patterns
- Monitor Microsoft Graph API calls for `roadtools` or
  `python-requests/<version>` UA strings (detection-side)
- Review Conditional Access Policy enforcement against device-bound
  token paths to identify CAP-bypass exposure
- Audit PRT issuance logs for anomalous device-PRT-issuance patterns
- Per MITRE T1098.005 / T1550 / T1087 detection-engineering coverage

**No A&D-prime victim is named in this Unit 42 publication.** Article
frames target population as "high-value targets" generically.

## Trigger evaluation context (for grader, not collector)

- **Trigger 1 (critical-CVE-exploited):** N/A — no CVE referenced.
- **Trigger 2 (tracked-actor-attribution):** PARTIAL — APT29 is in roster.
  But the attribution is NOT new (APT29 / Cloaked Ursa ROADtools use has
  been publicly documented since at least 2022 via Mandiant, Microsoft,
  and Volexity). Unit 42's publication consolidates and re-attests
  rather than originates. The grader should evaluate whether
  consolidation-publication-by-A-grade-vendor qualifies as Trigger 2
  "attribution is new not restatement" — a defensible reading either
  way.
- **Trigger 3 (first-party-IOC-hit):** N/A — Splunk first-party 0 events
  this sweep (54th consecutive dormant sweep). Trigger evaluation FAIL.
- **Trigger 4 (tracked-actor-TTP-change):** **CANDIDATE** — APT29 in
  roster; "new tooling or targeting or infrastructure class" is the
  evaluation question. ROADtools-misuse is documented from "late 2021"
  onward — multi-year-aged tradecraft. The grader's judgment call: is
  A-grade vendor formal publication of a multi-year-aged TTP cluster
  itself "new" for Trigger 4 purposes? Conservative framing: A-grade
  vendor formal publication of detailed TTP cluster IS new in this
  corpus, even when underlying activity is multi-year-aged. Less-
  conservative framing: "ROADtools-misuse is established tradecraft;
  this is documentation-not-evolution." Both defensible.
- **Trigger 5 (A&D-sector campaign):** FAIL — no A&D-prime victim named;
  no specific A&D-sector campaign described.
- **Trigger 6 (zero-day-no-patch):** N/A — no CVE.

## Hard Rule 3 status

ROADtools is open-source defensive-AND-offensive Python tooling on
GitHub. Unit 42's article describes detection-engineering and
attribution surface — NOT exploitation walkthrough or PoC. Hard Rule 3
preserved: Archimedes does not copy attack tooling content; collector
captures the detection-side IOCs (UA strings + OS version + device-
naming pattern) for defensive purposes only.

## Hard Rule 7 status (copyright discipline)

The 15-word direct quote rule applies. This raw-signal includes one
≤15-word direct quote — "highly targeted spear phishing" (Unit 42 on
APT29 / Cloaked Ursa 2021 initial access). Other content is paraphrased
or framed as Unit 42's findings. Quote count = 1 per source; under limit.

## Extraction notes

- Language: en
- Publisher byline: Bill Batchelor and Eyal Rafian (Unit 42 / Palo Alto Networks)
- Article type: vendor primary research / threat-intel blog
- Raw IOC extraction invoked: yes — yielded 3 explicit IOCs (UA strings
  + OS version) plus 1 detection-side pattern (device-naming pattern)
  not strictly an IOC
- Source grade per source-grades.yaml: unit42 ratified A
- MITRE ATT&CK technique alignment: T1098.005 + T1550 + T1087
- Categories per feedburner tag set: Cloud Cybersecurity Research,
  Threat Research, Curious Serpens, Entra ID, Microsoft Azure,
  Microsoft graph API, Midnight Blizzard, MITRE, ROADtools, UTA0355,
  Void Blizzard

## IOCs (from ioc-extraction skill)

```yaml
iocs:
  - type: ua_string
    value: "roadtools"
    description: "Default User-Agent string emitted by ROADtools roadrecon and roadtx modules when attackers don't customize UA"
    detection_surface: network
    confidence_in_attribution: F   # UA string alone is not actor-attributable; only ROADtools-use-attributable
    source: unit42-2026-05-22
  - type: ua_string
    value: "python-requests/<version>"
    description: "Default Python-requests library UA emitted by roadtx when invoked without custom UA override; <version> varies by Python environment"
    detection_surface: network
    confidence_in_attribution: F   # generic Python-requests UA also appears in legitimate traffic; only roadtools-context-anomalous
    source: unit42-2026-05-22
  - type: device_registration_os_version
    value: "10.0.19041.928"
    description: "Default OS version reported by ROADtools when registering rogue devices via roadtx without specifying alternate OS version; Unit 42 frames as anomalous-versus-legitimate-tenancy-host-OS-versions"
    detection_surface: entra_id_device_registration_logs
    confidence_in_attribution: F   # OS version alone is detection-side anomaly, not actor-attributable
    source: unit42-2026-05-22
  - type: device_naming_pattern
    value: "DESKTOP-{RANDOM_8_DIGITS}"
    description: "Default Windows device-naming pattern when attackers don't customize device name during roadtools-registration"
    detection_surface: entra_id_device_inventory
    confidence_in_attribution: F   # generic Windows default pattern; only roadtools-context-anomalous
    source: unit42-2026-05-22
attribution_claims:
  - source: Unit 42 (Bill Batchelor + Eyal Rafian)
    actor: Cloaked Ursa (= Midnight Blizzard = APT29 = roster #009)
    claim: "ROADtools misuse since late 2021 for Azure AD enumeration after spear-phishing initial access"
    attribution_language: "early observation came in late 2021" — established-reporting-carry-forward framing, NO explicit confidence level
    confidence_per_source: implicit-high (multi-year-corroborated)
    novelty: ROADtools-misuse TTP class has been publicly documented since 2022 by Mandiant, MSTIC, Volexity; Unit 42 2026-05-22 consolidates rather than originates
  - source: Unit 42 (Bill Batchelor + Eyal Rafian)
    actor: Curious Serpens (= Peach Sandstorm = APT33; NOT in _roster.yaml)
    claim: "Used ROADtools after password-spray attacks in 2023"
    attribution_language: implicit-historical-carry-forward, NO explicit confidence level
    confidence_per_source: implicit
    novelty: documented retrospectively; APT33 not in roster — potential /new-actor candidate for actor-profiler review
  - source: Unit 42 (citing Volexity 2025)
    actor: UTA0355 (NOT in _roster.yaml; Russian-aligned per Volexity 2025)
    claim: "Targeted phishing campaign in early 2025 with roadtx-token-management capability match"
    attribution_language: third-party-relay-of-Volexity-attribution, Unit 42 does NOT first-party attribute
    confidence_per_source: relay-level
    novelty: documented retrospectively
  - source: Unit 42 (categorical tag only)
    actor: Void Blizzard
    claim: Not discussed in article body per WebFetch extraction
    attribution_language: tag-only
    novelty: insufficient surface to evaluate
ad_relevance: medium_to_high_indirect_via_m365_entra_id_attack_surface
ad_relevance_rationale: |
  No A&D-prime victim named in publication. TTP cluster is operationally
  directly applicable to A&D-prime M365 / Entra tenancies (PRT hijack +
  CAP bypass + Microsoft Graph API enumeration + rogue device registration
  for persistence). Defensive prioritization: audit Entra ID device-
  registration logs, monitor Microsoft Graph API call patterns, review
  CAP enforcement against device-bound token paths.
trigger_4_grader_evaluation_candidate: true
trigger_4_grader_question: |
  Does A-grade vendor formal publication of multi-year-aged ROADtools-
  misuse TTP cluster against a roster actor (APT29 #009) qualify as
  "new tooling or targeting or infrastructure class" per FLASH-POLICY
  Trigger 4? Conservative reading: yes (A-grade vendor consolidation IS
  new in this corpus). Less-conservative reading: no (tradecraft
  documented since 2022; Unit 42 retrospectives the cluster). Grader's
  judgment.
```
