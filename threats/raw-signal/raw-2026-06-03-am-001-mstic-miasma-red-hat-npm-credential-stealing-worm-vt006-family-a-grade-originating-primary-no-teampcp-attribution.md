---
raw_id: raw-2026-06-03-am-001-mstic-miasma-red-hat-npm-credential-stealing-worm-vt006-family-a-grade-originating-primary-no-teampcp-attribution
collected_at: 2026-06-03T07:33:00-04:00
run_id: pre-brief-20260603-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: mstic
  source_name: Microsoft Security Blog / MSTIC (Microsoft Defender Security Research Team) — full technical write-up of the Red Hat npm "Miasma" credential-stealing supply-chain campaign
  source_url: https://www.microsoft.com/en-us/security/blog/2026/06/02/preinstall-persistence-inside-red-hat-npm-miasma-credential-stealing-campaign/
  published_at: 2026-06-03T00:45:06-04:00          # 04:45:06 UTC = 00:45 EDT; in-window (window 17:30 EDT 2026-06-02 → 07:30 EDT 2026-06-03)
source_grade: A (mstic ratified A per source-grades.yaml — Tier-1 vendor research practice; first-party Defender + Microsoft Threat Intelligence telemetry; named-research-team byline)
date: 2026-06-03
topic: mstic-miasma-red-hat-npm-credential-stealing-worm-32-packages-90-versions-a-grade-originating-primary-no-teampcp-attribution-shaiworm-signature-family-linkage
match_reason:
  watchlist: []                                    # No A&D-watchlist entity. Red Hat is not an A&D prime; @redhat-cloud-services is generic cloud/IT tooling.
  actors: []                                       # MSTIC EXPLICITLY does NOT attribute. No nation-state, no TeamPCP, no Mini-Shai-Hulud linkage in MSTIC text. Roster match is via the SHAIWORM signature naming, not via actor-roster id.
  vulnerabilities: [VT-006]                        # Linked to VT-006 (Mini Shai-Hulud family) via the Defender signature `Trojan:JS/ShaiWorm.DAW!MTB` — the SHAIWORM family naming is the corpus link. MSTIC does NOT link the campaigns themselves in body text.
  keywords:
    - Miasma
    - "Miasma: The Spreading Blight"
    - "@redhat-cloud-services"
    - Red Hat npm
    - Bun runtime
    - preinstall hook
    - SLSA provenance forgery
    - Sigstore
    - OIDC token exchange
    - GitHub Actions OIDC publishing workflow
    - RedHatInsights/javascript-clients
    - ShaiWorm.DAW!MTB
    - destructive tripwire
    - "rm -rf ~/"
    - Mini Shai-Hulud
    - TanStack
    - CVE-2026-45321
    - supply chain
    - CI/CD compromise
    - credential theft
    - GitHub Actions runner memory
    - api.anthropic.com C2 dormancy
triage_tags:
  - vt006_family_extension
  - a_grade_originating_primary
  - mstic_first_party_telemetry
  - attribution_explicitly_withheld
  - shaiworm_signature_family_linkage
  - destructive_capability_added
  - slsa_attestation_forgery_via_sigstore
  - oidc_token_exchange_worm_mechanic
  - dual_ecosystem_npm_only_this_variant
  - cross_platform_linux_macos_windows
  - ci_cd_primary_targeting
  - upstream_pipeline_compromise
  - dormant_anthropic_api_c2
  - operator_high_priority_morning_brief
candidate_triggers:
  - trigger_id: 2
    name: tracked-actor-attribution
    evaluation: FAIL (no tracked-actor attribution by MSTIC — attribution explicitly withheld; restatement-via-signature-tag does not satisfy "attribution_is_new_not_restatement")
    rationale: |
      MSTIC names no nation-state, no eCrime cluster, no prior alias.
      Defender signature `Trojan:JS/ShaiWorm.DAW!MTB` ties the malware
      family-taxonomically to the Shai-Hulud family but Microsoft's body
      text deliberately does NOT extend that into a TeamPCP attribution
      (vs. the prior Wiz / Snyk / StepSecurity attribution chain on
      VT-006). This is itself a material analytical signal — the
      A-grade originating primary on the Red Hat campaign declines to
      affirm the TeamPCP attribution that B-grade vendors (Aikido, Ox
      Security, ReversingLabs, Socket) propagated yesterday via
      SecurityWeek relay. Hard Rule 2 preserved: do NOT extend TeamPCP
      attribution into this campaign from prior-campaign similarity.
      Trigger 2 FAILS as a FLASH condition; but this is high-WEP-shaping
      material for the AM brief and grader cluster.
  - trigger_id: 4
    name: tracked-actor-ttp-change
    evaluation: FAIL (no tracked actor named by MSTIC — TTP-change condition requires `attributable_actor in _roster.yaml`)
    rationale: |
      The capability advances are substantial — SLSA provenance forgery
      via Sigstore (Fulcio + Rekor), OIDC token exchange for publish
      rights, dormant Anthropic API C2 (`api.anthropic.com:443/v1/api`
      with `noop: true`), 16 rotating attacker GitHub accounts per
      session, decoy-honeytoken-triggered `rm -rf ~/` destructive
      tripwire, and Bun runtime as second-stage execution environment.
      But Trigger 4 requires actor-attribution; MSTIC declines. Trigger
      4 FAILS as a FLASH condition. Capability lift IS the morning
      brief lead.
  - trigger_id: 5
    name: ad-sector-campaign
    evaluation: FAIL (no aerospace/defense/watchlist entity victim — Red Hat is not an A&D prime; @redhat-cloud-services is general cloud/IT)
    rationale: |
      The MSTIC report names Red Hat / @redhat-cloud-services as the
      compromised maintainer scope. No A&D prime is named as victim.
      However A&D-prime exposure is INDIRECT via dependency-graph
      reach: any A&D-prime CI/CD pipeline pulling
      @redhat-cloud-services packages (which include OpenShift
      management tooling, cloud-services integration components, and
      RBAC/inventory clients commonly used in enterprise DevOps stacks)
      inherits the credential-theft + worm-propagation exposure. This
      is the same indirect-pathway analysis applied to VT-006 @squawk
      / @tanstack on 2026-05-12. Trigger 5 FAILS on direct-named-victim
      condition. Indirect A&D relevance is a grader / analyst call,
      not a FLASH-eligibility call.
  - trigger_id: 6
    name: zero-day-no-patch
    evaluation: FAIL (no CVE; this is supply-chain campaign disclosure, not a software vulnerability)
    rationale: |
      MSTIC's report covers an active campaign and its remediation
      (npm removed affected repos; @redhat-cloud-services namespace
      hardened; tokens invalidated). No CVE assignment surfaced for
      the campaign itself. Distinguishes from VT-006 which DOES carry
      CVE-2026-45321. Trigger 6 N/A.
flash_evaluation_outcome: NO_FLASH — non-FLASH morning-brief LEAD material; grader should promote and cluster against VT-006 with explicit attribution-divergence note
iocs_extracted: true
iocs_count: 26                                     # 6 SHA-256 + 2 legitimate-infra-abuse IOC strings (api.anthropic.com noop endpoint, oven-sh/bun release paths) + 16 attacker GitHub account rotation pool (count only, not enumerated) + 32 package families + 2 Defender signatures + Bun runtime indicator + decoy honeytoken token-name + Miasma marker string + spoofed commit author + spoofed commit message
text_word_count: 2650
promoted: true
promoted_to_finding: finding-2026-06-03-0001-mstic-miasma-red-hat-npm-credential-stealing-worm-a-grade-originating-primary-second-tier1-attribution-declination-vt006-family-extension
promoted_at: 2026-06-03T08:18:00-04:00
ttl_expires_at: 2026-09-01T07:33:00-04:00
test: false
---

# Preinstall to persistence: Inside the Red Hat npm "Miasma" credential-stealing campaign

**Source:** Microsoft Security Blog — Microsoft Defender Security Research Team
**Publication:** 2026-06-02 (16:45 PDT) / 2026-06-03 00:45 EDT
**URL:** https://www.microsoft.com/en-us/security/blog/2026/06/02/preinstall-persistence-inside-red-hat-npm-miasma-credential-stealing-campaign/
**Source grade:** A (mstic ratified A per `source-grades.yaml` — Tier-1 vendor research with first-party Defender + MSTIC platform telemetry, named-research-team byline)

---

## Summary of MSTIC's Findings (analyst-paraphrased per Hard Rule 7 quote discipline)

Microsoft Threat Intelligence identified a large-scale npm supply-chain attack affecting **32 maliciously modified packages across more than 90 versions** under the `@redhat-cloud-services` npm scope. The compromise **originated from the upstream RedHatInsights/javascript-clients CI/CD pipeline**, allowing attackers to publish trojanized packages through the legitimate GitHub Actions OIDC publishing workflow. As a result, the malicious packages carried authentic provenance signatures while embedding the campaign marker **"Miasma: The Spreading Blight"**.

Once installed, the trojanized packages triggered an **npm preinstall hook** that executed a heavily obfuscated **4.29 MB dropper script**. Through multiple layers of obfuscation and encryption, the malware downloaded the **Bun JavaScript runtime** and launched a secondary payload designed to harvest credentials from GitHub, npm, AWS, Azure, GCP, HashiCorp Vault, Kubernetes, and developer systems. The malware also attempted to propagate by compromising additional maintainer packages and, in some scenarios, could destroy the maintainer's home directory.

The payload operates across **Linux, macOS, and Windows** by dynamically downloading the correct Bun runtime for each platform. **Linux CI/CD runners appeared to be the primary target.** On developer systems, the malware steals SSH keys, CLI credentials, browser and wallet data; in CI/CD environments it scrapes GitHub Actions runner memory for secrets, escalates privileges using passwordless sudo, and republishes poisoned packages with **forged SLSA provenance** to continue downstream propagation. Microsoft shared findings with the npm team, leading to removal of affected repositories and additional protections on the `@redhat-cloud-services` namespace.

## Attack Chain — 10 Phases

1. **Delivery and execution** — Malicious `preinstall` hook in `package.json` executes `node index.js` automatically during `npm install`, no user interaction required. The 4.29 MB `index.js` dropper replaces legitimate package code while leaving source-map metadata unchanged (indicating release-pipeline tampering, not source-tree commit).
2. **Staged unpacking** — Payload unpacks through multiple ROT-based obfuscation variants followed by AES-128-GCM decryption. Downloads Bun runtime, detonates final payload.
3. **Environment gating** — Terminates execution on systems configured with few regions in locale settings; can optionally restrict execution to CI/CD environments only.
4. **Defense evasion** — Attempts to neutralize security controls.
5. **Credential access** — Harvests secrets and authentication tokens from GitHub, npm, major cloud providers, HashiCorp Vault, Kubernetes; includes scraping sensitive data directly from CI runner process memory.
6. **Privilege escalation** — Installs passwordless sudo rule for elevated privileges and deeper system control.
7. **Persistence** — Continuously monitors stolen tokens; prepares secondary-stage payload deployment for long-term access.
8. **Exfiltration** — Stolen data transmitted via **three separate C2 channels**, including abuse of GitHub infrastructure as exfil mechanism.
9. **Self-propagation** — Republishes packages owned by the compromised maintainer using forged provenance metadata, spreading like a worm across trusted package ecosystems.
10. **Destructive tripwire** — If the malware detects interaction with a planted decoy token, it triggers a destructive fail-safe `rm -rf ~/` intended to wipe the victim's home directory.

## Three Self-Propagation Channels

- **Channel A (Victim-Owned Repo Drop):** Creates public GitHub repositories under the victim's account with description **"Miasma: The Spreading Blight"** and commits stolen credentials to `results/<timestamp>-<counter>.json` with randomized repo names like `adjective-creature-<0–99999>`.
- **Channel B (Code Injection via Git API):** Injects malicious `.github/setup.js` into non-protected branches using the Git Data API (blob → tree → commit → ref update). Skips protected/default branches and common bot branches. Uses spoofed commit author `github-actions@github.com` with message `chore: update dependencies [skip ci]`.
- **Channel C (Package Republishing):** Exchanges OIDC token for publish rights and republishes compromised maintainer packages with **forged SLSA provenance attestations through Sigstore (Fulcio or Rekor)** to appear legitimate, enabling downstream propagation across dependency trees.

## Destructive Tripwire Detail

The malware plants a decoy honeytoken labeled:
`IfYouInvalidateThisTokenItWillNukeTheComputerOfTheOwner`

Trigger condition: if the victim invalidates or revokes this planted token, the payload executes:
```
rm -rf ~/ && ~/Documents
```
This wiper command attempts to delete the entire home directory — a destructive fail-safe against defender remediation efforts. **This is a new capability layer vs. VT-006 Mini Shai-Hulud**, which had no destructive component.

## 32 Affected `@redhat-cloud-services` Packages (90+ versions)

`types`, `frontend-components-utilities`, `frontend-components`, `rbac-client`, `javascript-clients-shared`, `frontend-components-config-utilities`, `frontend-components-notifications`, `tsc-transform-imports`, `frontend-components-config`, `eslint-config-redhat-cloud-services`, `host-inventory-client`, `rule-components`, `frontend-components-remediations`, `frontend-components-translations`, `vulnerabilities-client`, `frontend-components-advisor-components`, `entitlements-client`, `chrome`, `notifications-client`, `compliance-client`, `sources-client`, `integrations-client`, `frontend-components-testing`, `remediations-client`, `insights-client`, `topological-inventory-client`, `config-manager-client`, `hcc-pf-mcp`, `quickstarts-client`, `patch-client`, `hcc-feo-mcp`, `hcc-kessel-mcp`.

(Three malicious versions per package on average — typically tagged at `x.x.1`, `x.x.2`, `x.x.4` patterns visible in MSTIC's published matrix.)

## Credential-Theft Targets

- **GitHub** — validates token/scopes, enumerates repos, reads Actions/org secrets; steals `ACTIONS_RUNTIME_TOKEN` + `ACTIONS_ID_TOKEN_REQUEST_TOKEN`.
- **npm** — validates via `/-/whoami`, exchanges OIDC tokens for publish rights.
- **AWS** — pulls IAM credentials via IMDS/ECS metadata and Secrets Manager.
- **Azure** — collects IMDS OAuth2 tokens for Management, Graph, and Key Vault.
- **GCP** — harvests `metadata.google.internal` service-account tokens, Secret Manager, Resource Manager access.
- **HashiCorp Vault** — probes `127.0.0.1:8200` across multiple token paths.
- **Kubernetes** — reads Service Account tokens and namespace secrets.
- **Other** — CircleCI tokens, SSH keys, CLI credentials, browser/wallet data, **Anthropic API keys**.

## IOC Set (extracted to dossier; full details in raw-signal IOCs section below)

- **6 SHA-256 hashes** (dropper + secondary payload variants)
- **Dormant HTTPS exfil endpoint:** `api.anthropic.com:443/v1/api` (marked `noop: true` in MSTIC code excerpt — exfil channel is staged but inactive at the campaign's observed phase, likely held in reserve)
- **Bun runtime fetch URLs:** `github.com/oven-sh/bun/releases` and `release-assets.githubusercontent.com`
- **GitHub abuse pool:** 16 attacker-controlled GitHub accounts rotating per session (count published; individual account list not in MSTIC body)
- **Campaign marker:** `"Miasma: The Spreading Blight"` (used as repo description, code comment, and decoy-token label substring)
- **Spoofed commit author:** `github-actions@github.com`
- **Spoofed commit message:** `chore: update dependencies [skip ci]`
- **Decoy honeytoken name:** `IfYouInvalidateThisTokenItWillNukeTheComputerOfTheOwner`
- **Defender signatures:** `Trojan:JS/ShaiWorm.DAW!MTB`, `Trojan:JS/ObfusNpmJs`

## Attribution Statement (MSTIC text)

**MSTIC does not attribute this campaign to any nation-state, cybercriminal cluster, or named actor.** The threat is identified solely by its embedded **"Miasma: The Spreading Blight"** marker. The MSTIC report does NOT link Miasma to TeamPCP, Mini Shai-Hulud, TanStack/CVE-2026-45321, or any prior Shai-Hulud-family campaign in body text. The Defender signature naming `Trojan:JS/ShaiWorm.DAW!MTB` ties the malware family-taxonomically to the broader Shai-Hulud family — but this is signature taxonomy, NOT actor attribution.

This is a **material divergence** from yesterday's B-grade relay chain (Aikido, Ox Security, ReversingLabs, Socket via SecurityWeek, per `raw-2026-06-02-am-003`), which carried the TeamPCP attribution forward from VT-006 / `finding-2026-05-12-FLASH-0001`. The A-grade originating primary on the Red Hat campaign **declines to affirm** the TeamPCP attribution. Per Hard Rule 2 (no novel attribution origination from Archimedes), the corpus must preserve this divergence:

- The Red Hat / Miasma campaign carries **NO TeamPCP attribution** in the A-grade source.
- The VT-006 / Mini Shai-Hulud campaign retains its **"likely" WEP TeamPCP attribution** per the prior A2 grading (Wiz + Snyk + StepSecurity).
- The family-taxonomic linkage via `ShaiWorm.DAW!MTB` signature is preserved (this is what allows VT-006 to be the closest corpus anchor) but signature naming is NOT actor attribution.

The grader should evaluate whether VT-006's "TeamPCP at likely" attribution should be downgraded on the basis of the A-grade source declining to extend it to the closely-related Red Hat campaign — or whether the two campaigns should be treated as distinct family-members under the Shai-Hulud umbrella with separate attribution treatment per-campaign. The red-team-analyst should challenge any AM-brief language that conflates the two.

## Connection to VT-006 / Mini Shai-Hulud (Corpus Linkage)

MSTIC's "Related posts" section references the May 2026 "Typosquatted npm packages used to steal cloud and CI/CD secrets" post (labeled "Mini Shai-Hulud campaign") and the May 29 "Malicious npm packages abuse dependency confusion to profile developer environments" post. These are surfaced as **related** material, not **linked** material. MSTIC's body text contains **zero mentions** of Mini Shai-Hulud, TanStack, or CVE-2026-45321.

For Archimedes corpus tracking:
- The campaign is anchor-linked to **VT-006** via the SHAIWORM family taxonomy.
- Miasma adds **novel capability layers** vs VT-006: destructive tripwire (`rm -rf ~/`); dormant Anthropic API C2 reserved channel; 16-account GitHub rotation pool; Sigstore-attestation forgery via Fulcio + Rekor (vs VT-006's documented SLSA-attestation breakage); explicit upstream pipeline compromise as initial vector (vs VT-006's maintainer-account compromise vector).
- Miasma is **npm-only** at this observation point (no PyPI variant surfaced) vs VT-006's dual-ecosystem (npm + PyPI) propagation.
- Both campaigns share: forged-provenance SDLC poisoning, GitHub-infra abuse, multi-platform support (Linux/macOS/Windows), CI/CD credential exfiltration focus.

Recommended grader / vuln-tracker action: treat Miasma as a **VT-006 family extension** with explicit attribution-divergence note, OR scaffold a separate VT-011 dossier for Miasma if the campaign-distinct features warrant separate tracking. The destructive tripwire alone is arguably enough to warrant separate VT-tracking given it is a new capability class for the family.

## Defender Coverage and Detection Guidance

Microsoft Defender Antivirus signatures:
- `Trojan:JS/ShaiWorm.DAW!MTB`
- `Trojan:JS/ObfusNpmJs`

Microsoft Defender for Endpoint alerts named in the report:
- "Suspicious Node.js process behavior"
- "Suspicious installation of Bun runtime"
- "Suspicious Bun execution from Node.js process"
- "Credential access attempt"
- "Kubernetes secrets enumeration indicative of credential access"

Advanced Hunting KQL queries published in the report (excluded from this raw-signal text per Hard Rule 3 — defensive detection guidance is publicly available at the source URL for any defender to apply):
- Bun execution from temp directories
- Bun download activity
- npm → Node → Bun process chain
- Cloud-metadata endpoint access from build processes (`169.254.169.254`, `169.254.170.2`)
- GitHub repository creation by service accounts
- Process memory access (`grep` with `isSecret":true`)
- npm token enumeration queries

## Remediation Status

- npm team removed affected repositories.
- Additional protections implemented on `@redhat-cloud-services` namespace to prevent unauthorized publishing.
- GitHub team invalidated all npm tokens with write access and 2FA bypass.

Microsoft published the analysis on **June 2, 2026** (post body date). Article URL date `/2026/06/02/` is published-date.

## MITRE ATT&CK Mapping (inferred from MSTIC detection-table coverage)

| Tactic | Technique |
|---|---|
| Initial Access / Execution | T1195.003 (Compromised Dependencies), T1059 (Command & Scripting Interpreter) |
| Execution / Defense Evasion | T1202 (Indirect Command Execution), T1140 (Deobfuscate/Decode Files), T1036.005 (Match Legitimate Name) |
| Credential Access | T1110.003 (Credential Stuffing), T1552.001 (Credentials in Files), T1552.007 (Container Environment Credentials), T1187 (Forced Authentication) |
| Privilege Escalation | T1548.003 (Sudo & Sudo Caching) |
| Persistence | T1098 (Account Manipulation), T1547.014 (Pre-Install Hooks) |
| Exfiltration | T1041 (Exfiltration Over C2), T1567.002 (Exfiltration Over Web Service) |
| Lateral Movement / Impact | T1570 (Lateral Tool Transfer), T1565.001 (Data Destruction) |

## A&D Relevance (analyst note for grader handoff)

- **Direct named victim:** none. Red Hat is not an A&D prime.
- **Indirect dependency-graph exposure:** moderate-to-high. `@redhat-cloud-services` includes OpenShift management tooling, RBAC clients, host-inventory clients, MCP (Multi-Cluster Platform) integrations, insights/compliance/remediations clients, and notifications components. Many A&D-prime CI/CD pipelines pulling OpenShift / RHCS integrations into Node-based developer-platform code (DevEx portals, monitoring dashboards, integration glue) would be in scope.
- **CI/CD primary-target framing** sharpens this: A&D primes with Node-based CI/CD runners on Linux (which is essentially all of them at this point) are within the documented target profile, NOT incidentally affected.
- **Hard Rule 2 discipline:** Archimedes does NOT extrapolate "A&D primes are exposed" from "this campaign targets Node CI/CD." We record the dependency-graph reach, name it as indirect, and let the grader call WEP.

---

## Extraction notes

- Language: en
- Publisher byline: Microsoft Defender Security Research Team
- Article type: vendor research blog (full technical write-up; Tier-1 originating primary)
- Raw IOC extraction invoked: yes

## IOCs (from ioc-extraction skill)

```yaml
iocs:
  - type: file_hash_sha256
    value: 396cac9e457ec54ff6d3f6311cb5cc1da8054d019ce3ffa1de5741506c7a4ea4
    context: Miasma dropper / payload sample (MSTIC IOC table)
    confidence: high
    source: MSTIC
  - type: file_hash_sha256
    value: d8d170af3de17bb9b217c52aaaffdf9395f35ef015a57ef676e406c121e5e223
    context: Miasma dropper / payload sample (MSTIC IOC table)
    confidence: high
    source: MSTIC
  - type: file_hash_sha256
    value: f0641e053e81f0d01fa46db35a83e0a34494886503086866d956d14e81fd3e1c
    context: Miasma dropper / payload sample (MSTIC IOC table)
    confidence: high
    source: MSTIC
  - type: file_hash_sha256
    value: d5a97614d5319ce9c8e01fa0b4eb06fb5b9e54fa13b23d718174a1546444123b
    context: Miasma dropper / payload sample (MSTIC IOC table)
    confidence: high
    source: MSTIC
  - type: file_hash_sha256
    value: f88258e21592084a2f93a572ade8f9b91c0cd0e242f5cf6121ed7bad0f7bdd1f
    context: Miasma dropper / payload sample (MSTIC IOC table)
    confidence: high
    source: MSTIC
  - type: file_hash_sha256
    value: 25e121e3b7d300c0d0075b33e5eca39a3e6a659fb9cfee52b70ef71686628f1b
    context: Miasma dropper / payload sample (MSTIC IOC table)
    confidence: high
    source: MSTIC
  - type: domain
    value: api.anthropic.com
    context: |
      DORMANT C2 / staged-exfil endpoint marked `noop: true` in MSTIC
      code excerpt; URL path /v1/api. NOT currently active — held in
      reserve. Defenders should NOT block api.anthropic.com generically
      (legitimate Anthropic API surface) but should monitor for
      unusual `/v1/api` traffic from CI runner contexts to that host.
    confidence: medium
    source: MSTIC
    notes: |
      Legitimate-infrastructure abuse caveat: api.anthropic.com is the
      official Anthropic API endpoint. The Miasma campaign stages exfil
      capability against this surface but the observed traffic at the
      time of MSTIC's writeup was marked dormant. Defenders should
      treat this as a TTP indicator (what the campaign CAN do) rather
      than as an active blocklist candidate.
  - type: url_pattern
    value: github.com/oven-sh/bun/releases
    context: Bun runtime download (legitimate Bun release infrastructure abused as second-stage runtime fetch)
    confidence: high
    source: MSTIC
    notes: Legitimate infra abuse — do not blocklist generically; monitor for unexpected Bun installs in CI/dev contexts.
  - type: url_pattern
    value: release-assets.githubusercontent.com
    context: Bun runtime download fallback (GitHub release assets)
    confidence: high
    source: MSTIC
    notes: Legitimate infra abuse — do not blocklist generically; monitor for unexpected Bun installs in CI/dev contexts.
  - type: campaign_marker_string
    value: "Miasma: The Spreading Blight"
    context: Campaign signature string — appears in attacker-created GitHub repo descriptions, code comments, decoy honeytoken substring
    confidence: high
    source: MSTIC
  - type: spoofed_commit_author
    value: github-actions@github.com
    context: Spoofed Git commit author used in Channel B code-injection self-propagation
    confidence: high
    source: MSTIC
  - type: spoofed_commit_message_pattern
    value: "chore: update dependencies [skip ci]"
    context: Spoofed commit message used to mask malicious .github/setup.js injection
    confidence: high
    source: MSTIC
  - type: decoy_honeytoken_name
    value: IfYouInvalidateThisTokenItWillNukeTheComputerOfTheOwner
    context: Decoy token planted by malware; invalidation triggers destructive `rm -rf ~/` payload
    confidence: high
    source: MSTIC
  - type: defender_signature
    value: Trojan:JS/ShaiWorm.DAW!MTB
    context: Microsoft Defender Antivirus signature for Miasma family
    confidence: high
    source: MSTIC
  - type: defender_signature
    value: Trojan:JS/ObfusNpmJs
    context: Microsoft Defender Antivirus signature for obfuscated npm JS payloads
    confidence: high
    source: MSTIC
  - type: package_namespace
    value: "@redhat-cloud-services"
    context: Compromised npm namespace — 32 packages across 90+ versions affected
    confidence: high
    source: MSTIC
  - type: upstream_repo
    value: github.com/RedHatInsights/javascript-clients
    context: Compromised upstream CI/CD pipeline — source of the publishing OIDC workflow that pushed trojanized packages
    confidence: high
    source: MSTIC

attribution_claims:
  - claim: |
      The Miasma campaign is identified by an embedded marker
      "Miasma: The Spreading Blight" but MSTIC does NOT attribute
      the campaign to any nation-state, eCrime cluster, or named actor.
    source_actor_named: null
    source_confidence_language: "no attribution offered"
    source: MSTIC
  - claim: |
      Defender signature `Trojan:JS/ShaiWorm.DAW!MTB` ties the malware
      family-taxonomically to the broader Shai-Hulud family.
    source_actor_named: null
    source_confidence_language: "family-taxonomic — signature naming, NOT actor attribution"
    source: MSTIC
    note: |
      Per Hard Rule 2, signature-family naming is NOT an attribution
      claim. The Miasma → Shai-Hulud-family taxonomic link does NOT
      extend the prior VT-006 / Mini Shai-Hulud "TeamPCP at likely"
      attribution to the Red Hat / Miasma campaign. The two campaigns
      are taxonomically related per Defender naming but attribution-
      independent per MSTIC's stated position.
```

## Grader handoff notes

- **Cluster against:** VT-006 (Mini Shai-Hulud family) — preserve the attribution divergence note. Do NOT extend TeamPCP attribution.
- **WEP-shaping implication for VT-006:** the A-grade originating primary on Miasma declines to affirm TeamPCP. This is mild downward pressure on the VT-006 attribution layer (currently "likely"), but does not by itself force a downgrade — VT-006's attribution rests on Wiz + Snyk + StepSecurity on the TanStack / CVE-2026-45321 surface, which Miasma does not directly contradict. Red-team-analyst should weigh whether the attribution-divergence pattern across two A-grade primaries (MSTIC silent on Miasma vs Wiz vocal on Mini Shai-Hulud) implies the two campaigns may belong to different actors under the same family, or whether Wiz's earlier attribution was thinner than initially assessed.
- **VT scaffolding decision:** recommend either (a) update VT-006 dossier with Miasma as documented family extension, or (b) scaffold a separate VT-011 for Miasma. Destructive tripwire alone is arguably enough capability lift to warrant separate VT-tracking. Vuln-tracker should call this.
- **A&D framing for AM brief:** indirect dependency-graph exposure via `@redhat-cloud-services` packages used in A&D-prime CI/CD pipelines; A&D prime exposure NOT confirmed by named-victim disclosure; defender-action framing should emphasize CI/CD runner audit + npm token rotation + cloud-metadata-endpoint monitoring.
- **Brief lead candidate:** strong. A-grade originating primary on a campaign known yesterday only via B-grade relay; explicit capability lift (destructive tripwire, SLSA-attestation forgery via Sigstore, dormant Anthropic API C2, 16-account rotation pool, upstream pipeline compromise vector); explicit attribution divergence vs prior corpus assumption. This is the highest-impact morning brief item available.
- **Hard Rule 3:** MSTIC publishes Advanced Hunting KQL queries in the source. Those queries are defensive detection content (legitimate use case) but they are NOT copied into this raw-signal file — the grader / briefer should cite the source URL for any defender wanting the full hunt-query set.
- **Hard Rule 7:** All direct quotes in the body above are <15 words and ≤1 per usage block.
