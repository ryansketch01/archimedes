---
raw_id: raw-2026-05-29-am-001-mstic-vpmdhaj-npm-typosquat-shaiworm-cloud-cicd-credential-theft-may-28-distinct-or-lineage-question
collected_at: 2026-05-29T07:42:00-04:00
run_id: pre-brief-20260529-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: mstic
  source_name: Microsoft MSTIC / Microsoft Security Blog
  source_url: https://www.microsoft.com/en-us/security/blog/2026/05/28/typosquatted-npm-packages-used-steal-cloud-ci-cd-secrets/
  source_grade: A
  published_at: 2026-05-28T23:04:52-04:00
  author: "Microsoft Defender Security Research Team"
match_reason:
  watchlist: []
  actors:
    - roster_001_TeamPCP_question    # vpmdhaj attribution is OPEN per MSTIC — Defender detection name "Trojan:JS/ShaiWorm" hints at Shai-Hulud family lineage (May 12 Mini Shai-Hulud was Wiz/Snyk/StepSecurity-attributed to TeamPCP), but MSTIC itself makes NO actor attribution. Source-fidelity question for grader: distinct cluster, or lineage extension?
  vulnerabilities:
    - CVE-2026-45321    # VT-006 Mini Shai-Hulud lineage — possibly extended by this campaign
  keywords:
    - "vpmdhaj"
    - "ShaiWorm"
    - "Mini Shai-Hulud"
    - "typosquat"
    - "preinstall hook"
    - "Bun runtime"
    - "AWS IMDSv2"
    - "HashiCorp Vault"
    - "npm publish token"
triage_tags:
  - npm_supply_chain
  - cloud_credential_theft
  - cicd_secret_theft
  - vt006_lineage_question
  - mstic_primary
  - distinct_cluster_or_extension
iocs_extracted: true
iocs_count: 18
text_word_count: 1850
promoted: true
promoted_to_finding: finding-2026-05-29-0001-mstic-vpmdhaj-npm-typosquat-shaiworm-cloud-cicd-credential-theft-bun-runtime-abuse-distinct-cluster-lineage-suggestion
promoted_at: 2026-05-29T08:08:00-04:00
promoted_run_id: morning-20260529-080000
ttl_expires_at: 2026-08-27T07:42:00-04:00
test: false
---

# Typosquatted npm packages used to steal cloud and CI/CD secrets (MSTIC, 2026-05-28)

Microsoft Defender Security Research Team writeup of an active supply-chain attack targeting the npm package ecosystem. On 2026-05-28, a single threat actor operating under the newly created maintainer alias **`vpmdhaj`** (`a39155771@gmail[.]com`) published 14 malicious packages within a four-hour window. The packages typosquat well-known OpenSearch, ElasticSearch, DevOps, and environment-configuration libraries, and several spoof the upstream OpenSearch project's repository URL in `package.json` to appear legitimate. Once installed, the packages harvest AWS credentials, HashiCorp Vault tokens, and CI/CD pipeline secrets from the host environment.

All packages in the cluster ship the same install-time stager and the same Bun-compiled second-stage payload — a ~195 KB credential harvester purpose-built for cloud and CI/CD environments. The payload runs silently during `npm install` and targets credentials across Amazon Web Services, HashiCorp Vault, GitHub Actions, and the npm registry itself, enabling both cloud lateral movement and downstream supply-chain pivoting through stolen npm publish tokens. Based on Microsoft's investigation and feedback to the npm team, these repos and users were taken down.

Key capabilities observed:
- Automatic execution via npm lifecycle hooks (`preinstall`, `install`, `postinstall`).
- Two distinct stager generations: Gen-1 HTTP-C2 variant and Gen-2 stealthier variant that abuses the legitimate Bun runtime distribution.
- AWS Instance Metadata Service (IMDSv2) and ECS task-role theft.
- AWS Secrets Manager enumeration across 16+ regions.
- HashiCorp Vault token harvesting.
- Theft of npm publish tokens for follow-on supply-chain attacks.

## Attack chain

The `vpmdhaj` cluster spans 14 scoped and unscoped packages that all mimic the `@opensearch` / `@elastic` ecosystem. The attack proceeds:

1. Publication of 14 typosquat packages under a single actor identity.
2. Automatic payload execution through a preinstall hook during `npm install`.
3. Gen-1 execution chain: `node` → `preinstall.js` → HTTP C2 → `payload.bin` (detached).
4. Gen-2 execution chain: `node` → `setup.mjs` → download legitimate Bun runtime → run bundled stage-2.
5. Cloud credential theft (AWS IMDS, ECS metadata, Vault, Secrets Manager) and npm publish-token theft for downstream supply-chain pivot.

## The lure: typosquats and spoofed metadata

Three social-engineering techniques designed to drive installs by mistake or trust transference:

- **Lookalike naming** — `opensearch-setup`, `opensearch-setup-tool`, `opensearch-config-utility`, `elastic-opensearch-helper`, `search-engine-setup`, `env-config-manager` mimic well-known cluster-management and configuration libraries.
- **Spoofed upstream metadata** — every unscoped package sets its `package.json` `homepage`, `repository`, and `bugs` fields to the legitimate `github.com/opensearch-project/opensearch-js` project.
- **Inflated version numbers** — releases jump straight to `1.0.7265`, `1.0.9108`, or `2.1.9201` to suggest a long, mature release history.

## Execution: npm lifecycle hook abuse

Every package in the cluster declares an automatic install-time hook in `package.json`. The malicious code executes the moment a victim runs `npm install` — no `require()` from victim code is needed. Two stager variants:

- **Gen-1** (versions ≤ 1.0.7265): `install`, `preinstall`, and `postinstall` hooks all invoke `preinstall.js` / `index.js`.
- **Gen-2** (versions ≥ 1.0.7266): a single `preinstall` hook invokes `setup.mjs` (newer, stealthier loader).

## Gen-1 stager — HTTP C2 beacon and payload drop

`preinstall.js` collects rich host context — hostname, platform, arch, Node version, `USER`/`USERNAME`, `cwd`, `INIT_CWD`, `npm_package_name`, `npm_package_version` — base64-encodes the JSON, and POSTs it to the actor's C2 with a campaign-unique header `X-Supply: 1`. The same C2 endpoint then serves a gunzip-compressed second-stage binary, which is written to `payload.bin` in the package install directory, `chmod 0755`'d, and spawned detached. The `__DAEMONIZED=1` environment variable lets the spawned process detect re-entry and exit cleanly.

## Gen-2 stager — Bun runtime abuse

The Gen-2 loader downloads the legitimate Bun runtime distribution from `github.com/oven-sh/bun/releases` (legitimate vendor URL — defensive blocking complicates), then executes the bundled stage-2 payload through Bun. This is a living-off-the-trusted-vendor pattern; the network traffic to GitHub's release CDN is harder to alert on than direct C2.

## Credential theft

The stage-2 payload (~195 KB Bun-compiled binary) targets:

- **AWS IMDSv2** — 169.254.169.254 metadata endpoint, harvests IAM instance-role credentials.
- **AWS ECS task metadata** — 169.254.170.2 endpoint, harvests ECS task-role credentials.
- **AWS Secrets Manager** — enumerates across 16+ regions to surface any cached secrets.
- **HashiCorp Vault** — token harvesting from `VAULT_TOKEN` environment variable + `~/.vault-token` file.
- **GitHub Actions** — environment-context collection (`GITHUB_TOKEN`, `GITHUB_REPOSITORY`, `RUNNER_*`).
- **npm registry** — publish-token theft from `~/.npmrc` for follow-on supply-chain attacks.

## Impact and blast radius

Microsoft frames the impact as dual-vector: (a) **cloud lateral movement** via AWS IAM / Vault credentials enabling downstream resource compromise within the victim's AWS environment, and (b) **supply-chain pivoting** via stolen npm publish tokens enabling the actor to push further malicious updates from compromised maintainer accounts. The CI/CD-secret-theft angle means a single developer install can compromise the entire downstream pipeline.

## How Microsoft Defender helps

Defender XDR detections that flag this campaign:
- `Trojan:JS/ShaiWorm`
- `Trojan:JS/ObfusNpmJs`
- `Backdoor:JS/SupplyChain`

**The `ShaiWorm` family-name in the detection signature is the strongest evidence of MSTIC's internal-classification view that vpmdhaj is in the Shai-Hulud lineage** — but the article body **does not attribute vpmdhaj to TeamPCP**, does not reference Wiz / Snyk / StepSecurity prior reporting, and does not name a tracked actor at any point. This is the central source-fidelity question for the grader: MSTIC's detection-rule naming signals lineage, but MSTIC's analytic prose declines to name an actor. The grader and analyst should preserve MSTIC's silence as-stated and not extend the attribution past what the article says.

## Hunting indicators (operator-actionable)

- npm lifecycle script execution with package names matching the typosquat set (`preinstall` / `postinstall` hooks on the listed package names).
- `payload.bin` in `node_modules` directories.
- Detached processes with `__DAEMONIZED=1` environment variable.
- Bun runtime downloads by Node.js processes from `github.com/oven-sh/bun/releases`.
- IMDS/ECS metadata access (`169.254.169.254`, `169.254.170.2`) from Node.js processes.

## Proxy / network defense

- Block `aab.sportsontheweb.net`.
- Alert on HTTP requests carrying header `X-Supply: 1`.

---

## Extraction notes

- Language: en
- Publisher byline: Microsoft Defender Security Research Team
- Article type: vendor blog / threat-intelligence primary
- Raw IOC extraction invoked: yes (inline below)
- A&D-prime relevance: structural / indirect — cloud and CI/CD credential theft applies to any DIB engineering pipeline using AWS + GitHub Actions + Vault. Not a victim-named A&D incident; structural exposure.

## IOCs (from ioc-extraction)

```yaml
domains:
  - value: aab.sportsontheweb.net
    role: c2
    confidence: high
    first_seen: 2026-05-28
    source: mstic

urls:
  - value: http://aab.sportsontheweb.net/x.php
    role: c2_endpoint_gen1
    confidence: high
    source: mstic

http_headers:
  - name: X-Supply
    value: "1"
    role: campaign_signature
    confidence: high
    detection_use: proxy_log_alert
    source: mstic

email_addresses:
  - value: a39155771@gmail.com
    role: registry_account
    platform: npmjs
    maintainer_alias: vpmdhaj
    confidence: high
    source: mstic

npm_packages_malicious:
  - "@vpmdhaj/elastic-helper"
  - "@vpmdhaj/devops-tools"
  - "@vpmdhaj/opensearch-setup"
  - "opensearch-setup"
  - "opensearch-setup-tool"
  - "opensearch-config-utility"
  - "elastic-opensearch-helper"
  - "search-engine-setup"
  - "env-config-manager"
  - "app-config-utility"
  # MSTIC names 11 specifically + the @vpmdhaj/* scoped set; total cluster = 14 packages. Full list deferred to vuln-tracker / VT-006 lineage dossier update.
  note: "MSTIC IOC section enumerates the full 14; this raw lists the high-signal subset. Full list pulled from source URL by vuln-tracker on dossier update."

file_hashes_sha256:
  - value: 638788AFC4F1B5860A328312CAF5895ABD5F5632D28A4F2A85B09076E270D15D
    file_role: preinstall_js_gen1_stager
    confidence: high
    source: mstic
  - value: 77D92EFE7AF3547F71FD41D4A884872D66B1BE9499EAA637E91EAC866911694D
    file_role: setup_mjs_gen2_stager
    confidence: high
    source: mstic
  - value: BFA149694EC6411C23936311A999163ADE54D6F38E2F4B0E3CFB8CB67BD7CFAA
    file_role: payload_gz_stage2_compressed
    confidence: high
    source: mstic

ip_addresses_referenced_not_c2:
  - value: 169.254.169.254
    role: aws_imdsv2_target_not_actor_controlled
    note: "Legitimate AWS metadata endpoint; included for hunting context only — NOT a C2 indicator."
  - value: 169.254.170.2
    role: aws_ecs_metadata_target_not_actor_controlled
    note: "Legitimate AWS ECS metadata endpoint; included for hunting context only — NOT a C2 indicator."

defender_detection_signatures:
  - "Trojan:JS/ShaiWorm"        # family-name signal of Shai-Hulud lineage per MSTIC internal classification
  - "Trojan:JS/ObfusNpmJs"
  - "Backdoor:JS/SupplyChain"

attribution_claims:
  - source: mstic
    actor: null                   # MSTIC names no tracked actor in the article body
    confidence_language: null
    direct_quote_under_15_words: |
      "newly created maintainer alias vpmdhaj"
    notes: |
      MSTIC's article prose makes NO actor attribution. The Defender detection
      family name "Trojan:JS/ShaiWorm" is a strong INTERNAL-CLASSIFICATION
      signal of family lineage with Shai-Hulud (which the May 12 Wiz/Snyk
      finding attributed to TeamPCP at high confidence), but MSTIC does not
      restate that attribution in this article. Hard Rule 2 governs: do not
      originate or upgrade attribution past source statements. Grader should
      treat this as DISTINCT campaign with FAMILY-LINEAGE SUGGESTION, not as
      a new TeamPCP-attributed finding.

mitre_attack_techniques_observed:
  - id: T1195.002
    name: "Supply Chain Compromise: Compromise Software Supply Chain"
    confidence: high
  - id: T1059.007
    name: "Command and Scripting Interpreter: JavaScript"
    confidence: high
  - id: T1552.005
    name: "Unsecured Credentials: Cloud Instance Metadata API"
    confidence: high
  - id: T1552.007
    name: "Unsecured Credentials: Container API"
    confidence: high
  - id: T1027
    name: "Obfuscated Files or Information (Bun-compiled payload)"
    confidence: high
  - id: T1071.001
    name: "Application Layer Protocol: Web Protocols (HTTP C2)"
    confidence: high
  - id: T1574
    name: "Hijack Execution Flow (npm lifecycle hooks)"
    confidence: high

a_and_d_relevance_assessment:
  level: structural_indirect
  rationale: |
    No A&D prime named as a victim. Structural exposure applies to any DIB
    organization with AWS + GitHub Actions + HashiCorp Vault CI/CD pipelines
    where a developer might install one of the typosquat packages. Most US
    primes' developer workstations are exposed to the npm registry. The npm
    publish-token theft creates downstream supply-chain risk for any DIB
    vendor that publishes private or public npm packages.

corroboration_required:
  - "Wiz Research follow-up linking vpmdhaj to TeamPCP / Shai-Hulud lineage explicitly (May 12 first surface)"
  - "Snyk / StepSecurity / Semgrep / Aikido secondary analyses (May 12 cluster vendors)"
  - "CISA KEV addition for any of the 14 packages (could trigger if Defender ShaiWorm signature lights up across .gov estate)"

grader_handoff_notes: |
  - Single MSTIC primary; A-grade vendor source. Strong technical content, full IOC
    set, named research team, named campaign / actor-alias (vpmdhaj).
  - Distinct campaign launch (May 28) vs. May 12 Mini Shai-Hulud (CVE-2026-45321) —
    same lineage by Defender family-name `ShaiWorm` but NOT explicit MSTIC
    attribution to TeamPCP. Grader should NOT upgrade past MSTIC's silence.
  - Likely WEP "very likely" on procedural facts (campaign exists, IOC valid,
    detection signature live), "likely" on family-lineage claim (Defender naming
    is a strong signal but not an attributive analytic statement).
  - VT-006 dossier (Mini Shai-Hulud) is a candidate for state-update note —
    add this as related-campaign-distinct-cluster on the lineage; do NOT
    fold vpmdhaj into VT-006 as same campaign without Wiz/Snyk explicit
    follow-up.
  - Possible new VT-tracker scaffold candidate for vpmdhaj as its own tracked
    cluster, separate from VT-006.
```
