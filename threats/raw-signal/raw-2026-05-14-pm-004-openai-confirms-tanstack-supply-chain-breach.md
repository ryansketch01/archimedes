---
raw_id: raw-2026-05-14-pm-004
collected_at: 2026-05-14T15:50:00-04:00
run_id: pre-brief-20260514-153000
collection_mode: pre_brief_collection
test: false
source:
  source_yaml_id: bleepingcomputer
  source_name: "BleepingComputer (Lawrence Abrams byline)"
  source_url: https://www.bleepingcomputer.com/news/security/openai-confirms-security-breach-in-tanstack-supply-chain-attack/
  published_at: 2026-05-14T15:07:24-04:00
corroborating_sources:
  - source_yaml_id: null   # OpenAI primary disclosure URL not surfaced in BleepingComputer summary
    source_name: "OpenAI security advisory (primary self-disclosure)"
    source_url: null
    role: originating_primary_victim_disclosure
  - source_yaml_id: mstic
    source_name: "Microsoft Threat Intelligence (referenced for Linux-malware-variants relationship to TanStack campaign)"
    source_url: null
    role: secondary_attribution_layer_linux_variants
  - source_yaml_id: null
    source_name: "Socket + Aikido (researchers tracking compromised packages — already in source-grades.yaml as aikido-security provisional C; Socket NOT in source-grades.yaml first-citation)"
    source_url: null
    role: researcher_tracking
match_reason:
  watchlist: []           # OpenAI is AI sector, NOT A&D-prime; @squawk aviation namespace dependency-graph A&D-indirect
  actors: ["001"]         # TeamPCP — roster ID 001
  vulnerabilities: [CVE-2026-45321]    # Mini Shai-Hulud worm CVE, VT-006 tracked vuln
  keywords: [openai, tanstack, mini-shai-hulud, teampcp, supply-chain, npm, pypi, code-signing-cert-rotation, mistral-ai]
triage_tags:
  - non_flash
  - brief_update
  - tracked_actor_attribution_teampcp
  - tracked_vuln_vt_006_mini_shai_hulud
  - named_victim_openai
  - ad_sector_indirect_squawk_aviation_namespace
  - code_signing_cert_rotation_event
  - victim_confirmed_via_self_disclosure
iocs_extracted: true
iocs_count: 0    # no fresh IOCs in this victim-disclosure piece; VT-006 IOCs already tracked separately
text_word_count: 1100
promoted: true
promoted_to_finding: finding-2026-05-14-0008
promoted_at: 2026-05-14T16:02:00-04:00
ttl_expires_at: 2026-08-12T15:50:00-04:00
---

# OpenAI confirms 2 employee devices breached in TanStack / Mini Shai-Hulud supply-chain attack; rotates code-signing certs for macOS / Windows / iOS / Android

## Cover

OpenAI publicly confirmed on **2026-05-14T15:07 EDT** (per BleepingComputer's Lawrence Abrams) that **two employee devices were compromised** during the Mini Shai-Hulud / TanStack supply-chain campaign, the TeamPCP-attributed npm + PyPI worm tracked in the Archimedes vulnerability index as **VT-006 (CVE-2026-45321, CVSS 9.6)**.

This is a **confirmed-victim disclosure** layer on top of finding-2026-05-12-FLASH-0001 (Mini Shai-Hulud worm — Wiz + Snyk + StepSecurity originating primary cluster, 172 packages affected including the @squawk aviation namespace).

OpenAI's framing:
- **2 employee devices compromised** — limited credential exfil + unauthorized access to a "limited subset of internal source code repositories"
- **No customer data exposure** confirmed
- **No production-system compromise** confirmed
- **No intellectual property exposure** confirmed
- **No deployed software compromise** confirmed
- **Code-signing certificates for macOS, Windows, iOS, and Android exposed** — OpenAI is rotating all four certs proactively despite no detected abuse
- **macOS-app caveat**: macOS users must update OpenAI desktop applications **before 2026-06-12** — older certificate-signed apps may fail to launch after that date
- **Windows and iOS users unaffected** by app-relaunch caveat (per BleepingComputer)

The breach scope is **bounded** but the **certificate rotation event is significant** — multi-platform code-signing-cert refresh suggests OpenAI is treating the credential-exfil scope as broader than the surface "2 employee devices" implies (precautionary rotation across all platforms suggests cert keys may have been on the compromised devices, which is consistent with the worm's documented credential-targeting behavior — GitHub tokens, npm tokens, AWS credentials, SSH keys).

This raw-signal is **brief-update material for the VT-006 tracking** (per `_index.yaml`), not a FLASH dispatch candidate. The Mini Shai-Hulud campaign was previously surfaced as FLASH on 2026-05-12 (flash-2026-05-12-0600); the OpenAI confirmation is downstream evidence-strengthening, not new-disclosure.

---

## BleepingComputer / OpenAI primary content (Hard Rule 7 quote-limited)

### Breach scope per OpenAI

> the incident did not impact customer data, production systems, intellectual property, or deployed software.

### What was breached

- Two employee devices compromised
- Unauthorized access and credential-focused exfiltration activity in "a limited subset of internal source code repositories"
- Limited credentials stolen — no evidence of subsequent misuse

### Code-signing cert rotation (proactive)

- macOS code-signing certificate — rotating
- Windows code-signing certificate — rotating
- iOS code-signing certificate — rotating
- Android code-signing certificate — rotating
- Rationale: proactive measure despite no detected abuse — consistent with worm's documented credential-exfil-targeting behavior
- **macOS-app deadline**: 2026-06-12 — users must update desktop applications before this date or older-cert-signed apps may fail to launch
- Windows and iOS users unaffected by app-relaunch caveat

### Attribution chain per BleepingComputer

- Campaign: **Mini Shai-Hulud** malware
- Actor: **TeamPCP extortion gang** (roster ID 001)
- Researchers tracking compromised packages: **Socket** + **Aikido** (Aikido is provisional C in source-grades; Socket is first-citation in this raw-signal, see also PM-005)
- Microsoft Threat Intelligence referenced for **related Linux-malware variants** layer
- Targeted credentials: GitHub tokens, npm tokens, AWS credentials, SSH keys (consistent with VT-006 worm documentation)

## VT-006 cross-reference

This raw-signal extends VT-006 (`threats/vulnerabilities/Mini-Shai-Hulud-CVE-2026-45321/`) victim tracking:

- **Prior victim/scope evidence**: ~172 packages compromised, ~84 versions for @tanstack alone, @uipath / @mistralai / @opensearch-project / @squawk (19 aviation packages) / @tallyui / DraftLab / PyPI guardrails-ai / PyPI mistralai
- **OpenAI is the first NAMED ENTERPRISE-VICTIM confirmation** of compromised-developer-device fallout in the Archimedes corpus. Prior tracking surfaced the package-compromise layer but not named-downstream-enterprise-victim layer.
- **Implication for A&D**: @squawk aviation namespace dependency-graph reach into A&D-prime SDLCs remains UNVERIFIED. OpenAI is NOT an A&D prime, but the OpenAI-confirmed pattern (developer-device compromise → cert-key exfil → multi-platform cert rotation) is the operational template for what an A&D-prime victim disclosure would look like if @squawk dependencies are in A&D-prime build pipelines.

## A&D / DIB relevance

**Direct**: NONE. OpenAI is AI-sector, not A&D.

**Indirect**:
- **@squawk aviation namespace**: 19 packages affected per Snyk + Wiz analysis, including @squawk/flightplan, @squawk/weather, @squawk/mcp — packages handle real aviation-domain functionality. Dependency-graph reach into Tier-1 A&D prime SDLCs (Boeing, Airbus, Honeywell Aerospace, Safran) is unverified.
- **Developer-device compromise template**: OpenAI's "2 employee devices → cert key exfil → multi-platform cert rotation" pattern is the operational template for A&D-prime exposure assessment. CMMC + DFARS 252.204-7012-cleared environments using npm/PyPI tooling in build pipelines should treat OpenAI's experience as a near-miss inquiry baseline.
- **Code-signing cert rotation in 30 days** sets an industry precedent that A&D-prime CISOs may use to benchmark their own cert hygiene posture.

## Anti-noise / lockout state

- **Mini Shai-Hulud lockout**: original FLASH-2026-05-12-0600 24h lockout expired 2026-05-13. Subsequent surfaces (Checkmarx Jenkins AST plugin 2026-05-11 day-prior + OpenAI-victim-confirmation today) are downstream evidence-strengthening, not new-disclosure. No FLASH dispatch warranted.
- This raw-signal feeds into the VT-006 tracking.yaml watch_signals layer (victim-named disclosures); briefer may use it for Supply Chain Watch sector context.

## Extraction notes

- Language: en
- Article type: media relay of vendor-victim self-disclosure
- Raw IOC extraction invoked: no fresh IOCs — IOCs already tracked in VT-006 dossier
- Hard Rule 2 compliance: TeamPCP attribution per Wiz + Snyk + StepSecurity prior research; this raw-signal does not originate a new attribution. OpenAI's "did not impact customer data, production systems, intellectual property, or deployed software" framing preserved verbatim.
- Hard Rule 3 compliance: no exploit content.
- Hard Rule 4 compliance: no credential values stored. Credential-exfil scope described categorically (GitHub tokens, npm tokens, AWS credentials, SSH keys) without specific values.
- Hard Rule 7 compliance: 15-word quote limits enforced.

## IOCs (from ioc-extraction skill)

```yaml
attribution_claims:
  - claim_text: "Mini Shai-Hulud malware attributed to TeamPCP extortion gang"
    claimed_actor: TeamPCP
    claimed_actor_aliases: []
    nation_state: unknown
    confidence_term: (BleepingComputer's framing — sourced from prior Wiz + Snyk + StepSecurity research)
    claimant_primary: wiz_snyk_stepsecurity   # via prior finding-2026-05-12-FLASH-0001
    claimant_relay_today: bleepingcomputer
    archimedes_roster_id: "001"
    archimedes_vt_id: VT-006

  - claim_text: "Microsoft Threat Intelligence also reported related Linux malware variants"
    claimed_actor: TeamPCP   # (Mini Shai-Hulud family inferred)
    nation_state: unknown
    confidence_term: (cross-platform variant linkage)
    claimant: mstic

victim_disclosure:
  victim_name: OpenAI
  victim_self_disclosed: true
  victim_disclosure_date: 2026-05-14
  victim_sector: AI / technology
  victim_archimedes_watchlist_match: false   # not in aerospace-defense.yaml
  victim_breach_scope:
    - "2 employee devices compromised"
    - "limited subset of internal source code repositories accessed"
    - "limited credentials stolen"
    - "no customer data exposure"
    - "no production system compromise"
    - "no intellectual property exposure"
    - "no deployed software compromise"
  victim_remediation_actions:
    - "code-signing cert rotation: macOS, Windows, iOS, Android"
    - "macOS app version-update deadline: 2026-06-12"
    - "Windows + iOS users unaffected by app-relaunch caveat"

new_actor_candidacy_flag: null   # TeamPCP already in roster, Socket is research-vendor first-citation but not an actor

source_first_citation_flag:
  vendor: Socket
  vendor_role: researcher_tracking_compromised_packages
  in_source_grades_yaml: false
  recommended_provisional_grade: B   # npm-security specialist research vendor; consistent with SafeDep / StepSecurity / Aikido tier; provisional B per Tier-2-AppSec-specialist precedent
```

---

**Source:**
- BleepingComputer: https://www.bleepingcomputer.com/news/security/openai-confirms-security-breach-in-tanstack-supply-chain-attack/
- VT-006 dossier: threats/vulnerabilities/Mini-Shai-Hulud-CVE-2026-45321/
- Prior finding: finding-2026-05-12-FLASH-0001
