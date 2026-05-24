---
raw_id: raw-2026-05-24-pm-001-socket-trapdoor-crypto-stealer-multi-ecosystem-npm-pypi-crates-34-packages-384-versions
collected_at: 2026-05-24T15:35:00-04:00
run_id: pre-brief-20260524-153000
collection_mode: pre_brief_collection
test: false
source:
  source_yaml_id: socket
  source_name: "Socket (npm/supply-chain security vendor; provisional B per source-grades.yaml 2026-05-14)"
  source_url: https://socket.dev/blog/trapdoor-crypto-stealer-npm-pypi-crates
  published_at: 2026-05-24T13:32:20+00:00          # 09:32 EDT, IN WINDOW
  byline: "Socket Research Team (no individual byline disclosed)"
corroborating_primaries:
  - source_yaml_id: x-vxunderground
    source_name: "vx-underground (grade C per source-grades.yaml)"
    notes: |
      vx-underground tweet at 2026-05-24 15:45 UTC (11:45 EDT, in window) relayed
      the Socket disclosure with a 34-package + 384-versions count and the named
      Socket detection-timing (median 5m27s, fastest 58s). vx-underground is a
      pure relay layer — adds no independent corroborating telemetry.
    primary_url_not_retrieved_this_sweep: false
    relay_only: true
  - source_yaml_id: socket-twitter
    source_name: "@SocketSecurity X account (Socket vendor-owned)"
    notes: |
      Socket's own X announcement at 2026-05-24 19:05 UTC (15:05 EDT, in window).
      Follow-up at 2026-05-24 21:29 UTC (17:29 EDT, post-window) added more
      GitHub-activity findings: the attacker maintained payload infrastructure,
      published AI/security-themed decoy repositories, and attempted to inject
      malicious configurations (.cursorrules, CLAUDE.md files) into projects
      INCLUDING modelcontextprotocol and gemini-cli upstream repos. Socket
      reported the attacker account to GitHub. Post-window update — flag for
      next sweep corroboration check.
    primary_url_not_retrieved_this_sweep: false
    relay_only: false  # Socket's own account so functionally an extension of the primary disclosure
match_reason:
  watchlist: []                       # NO A&D-prime named victim — target sectors are crypto/DeFi/AI/security developers
  actors: []                          # UNATTRIBUTED per Socket originating research; explicitly NOT TeamPCP/Shai-Hulud/Mini Shai-Hulud
  vulnerabilities: []                 # NO CVE assigned to this supply-chain compromise
  keywords:
    - trapdoor_crypto_stealer_supply_chain_attack
    - multi_ecosystem_npm_pypi_crates_first_documented_three_ecosystem_simultaneous_publication
    - 34_packages_socket_tracker_36_blog_header_384_versions_artifacts
    - 21_npm_packages_7_pypi_packages_6_crates_io_packages
    - crypto_defi_solana_sui_aptos_move_lang_ai_security_developer_targeting
    - github_pages_dead_drop_ddjidd564_github_io_defi_security_best_practices
    - npm_account_asdxzxc_github_account_ddjidd564
    - trap_core_js_payload_48485_bytes_xor_obfuscation_cargo_build_helper_2026
    - p_2024_001_campaign_marker_universal_ai_agent_extraction_framework_self_described
    - cursorrules_claude_md_persistence_into_modelcontextprotocol_gemini_cli_decoy_repos
    - persistence_vectors_git_hooks_shell_hooks_systemd_cron_ssh
    - credential_exfil_wallets_ssh_aws_github_browser_env_vars_api_keys
    - unattributed_per_socket_explicit_decline
triage_tags:
  - non_flash
  - new_multi_ecosystem_supply_chain_campaign_npm_pypi_crates
  - first_documented_three_ecosystem_simultaneous_publication_pattern
  - cursorrules_claude_md_ai_agent_persistence_novel_vector
  - decoy_repos_modelcontextprotocol_gemini_cli_targeting
  - github_pages_dead_drop_infrastructure
  - crypto_defi_solana_sui_aptos_developer_targeting
  - actor_unattributed_socket_explicit_decline
  - originating_research_socket_provisional_b
  - supply_chain_watch_finding_candidate
  - cross_ecosystem_first_time_corpus_tier_expansion_crates_io
  - temporally_close_to_packagist_8_pkg_laravel_lang_node_ipc_supply_chain_cluster
flash_trigger_evaluation:
  trigger_1_critical_cve_exploited: FAIL    # No CVE assigned; supply-chain compromise without a vulnerability disclosure
  trigger_2_tracked_actor_attribution: FAIL # Explicitly UNATTRIBUTED per Socket; NO tracked actor named (Socket explicitly notes "no existing threat actor group attributed"); Hard Rule 2 prevents Archimedes from originating attribution; specifically NOT TeamPCP / Shai-Hulud / Mini Shai-Hulud per Socket
  trigger_3_first_party_ioc_hit: FAIL       # Splunk defenseclaw_local dormant 52nd consecutive sweep; structural zero-opportunity
  trigger_4_tracked_actor_ttp_change: FAIL  # No tracked actor
  trigger_5_ad_sector_campaign: FAIL        # Target sectors are crypto/DeFi/AI/security developers (Solana/Sui/Aptos/Move-lang ecosystems); NO A&D-direct victim named
  trigger_6_zero_day_no_patch: FAIL         # Not a vulnerability disclosure; packages reported to ecosystem registries; GitHub account reported
  overall_flash_qualifies: false
  flash_evaluation_rationale: |
    A new UNATTRIBUTED multi-ecosystem supply-chain campaign — first documented
    three-ecosystem simultaneous-publication pattern in the Archimedes corpus
    (npm + PyPI + Crates.io with one attacker identity across all three).
    Crypto-developer-targeted credential stealer, decoy AI/security repos,
    `.cursorrules` + `CLAUDE.md` AI-agent-persistence vector NOVEL relative to
    prior supply-chain campaigns (Mini Shai-Hulud, node-ipc, Laravel-Lang,
    Packagist 8-pkg). NO A&D-direct victim. Fails all 6 FLASH triggers.
    Supply Chain Watch narrative candidate for afternoon brief if grader judges
    eligible — second-grade Tier-2 vendor originating-research (provisional B),
    no second-source confirmation in window, single-source veto applies on
    novelty claims (first three-ecosystem simultaneous-publication pattern).
    Notably distinct from recent supply-chain cluster (Mini Shai-Hulud worm /
    Laravel-Lang Composer / Packagist 8-pkg / node-ipc) on ecosystem (adds
    Crates.io for first time in corpus), targeting (crypto-developer vs. broad
    npm), and self-described framing ("Universal AI Agent Extraction Framework"
    is the malware author's own self-description embedded in `trap-core.js`).
promoted: true
promoted_to_finding: finding-2026-05-24-0001
promoted_at: 2026-05-24T16:18:00-04:00
ttl_expires_at: 2026-08-22T15:35:00-04:00
---

# TrapDoor Crypto Stealer Supply Chain Attack Hits 34 Packages and Hundreds of Versions Across npm, PyPI, and Crates.io

**Source:** Socket (Socket Research Team byline; provisional B per `source-grades.yaml`)
**Source URL:** <https://socket.dev/blog/trapdoor-crypto-stealer-npm-pypi-crates>
**Published:** 2026-05-24T13:32:20+00:00 (09:32 EDT — IN WINDOW for 2026-05-24 PM pre-brief sweep)
**Byline:** Socket Research Team (no individual analyst byline disclosed)

## Campaign overview

Socket disclosed an UNATTRIBUTED supply-chain campaign — internally codenamed
"TrapDoor" by the attacker per a `P-2024-001` campaign marker embedded in the
malware — comprising 34 malicious packages (the blog header says 36; the
tracker shows 34) across three ecosystems published over a roughly 50-hour
window. Earliest observed package: `eth-security-auditor@0.1.0` (PyPI) at
2026-05-22T20:20:18Z. Latest pre-disclosure activity continued through the
disclosure-window itself per Socket's tracker. Total compromised: **384+
versions and artifacts** across npm + PyPI + Crates.io.

**Ecosystem breakdown:**
- **npm:** 21 packages
- **PyPI:** 7 packages
- **Crates.io:** 6 packages

This is the **first documented three-ecosystem simultaneous-publication
pattern** in the Archimedes corpus. Prior corpus-tracked supply-chain
campaigns: Mini Shai-Hulud (VT-006) — npm + PyPI, dual-ecosystem; node-ipc
(2026-05-14-0009) — npm only; Laravel-Lang (2026-05-23-am-001 / pm-003) —
Composer/Packagist only; Packagist 8-pkg (2026-05-23-pm-002) — Composer only
with `package.json` cross-ecosystem injection vector. TrapDoor expands the
operational tier by adding **Crates.io** to the simultaneously-published
ecosystem set with one attacker identity across all three.

## Attribution

**UNATTRIBUTED per Socket.** Socket explicitly notes the campaign is not
attributable to a known threat actor group. The malware's self-description as
a "Universal AI Agent Extraction Framework" is the attacker's own framing
embedded in `trap-core.js`; it is not a Socket attribution.

Specifically NOT attributed to:
- TeamPCP (roster ID 001)
- Shai-Hulud / Mini Shai-Hulud (VT-006 / CVE-2026-45321)

**Hard Rule 2 (no Archimedes-originated attribution):** Per Socket's explicit
decline-to-attribute, Archimedes does NOT propose cluster-walk to any tracked
actor in `_roster.yaml`. The campaign carries operational adjacency to Mini
Shai-Hulud (ecosystem-supply-chain class) but mechanism (decoy-repo +
GitHub-Pages dead drop + persistence-via-AI-agent-config) and targeting
(crypto-developer-narrow vs. Mini Shai-Hulud's broad maintainer-enumeration
worming) differ.

## Attacker identity

- **GitHub account:** `ddjidd564` (Socket reports to GitHub; status at
  disclosure unspecified)
- **npm account:** `asdxzxc`
- **Decoy repos published:** AI/security-themed (specific names noted by
  Socket on X follow-up at 17:29 EDT — post-window; flag for next sweep)
- **Attempted-injection targets:** `modelcontextprotocol` and `gemini-cli`
  upstream repositories per Socket's post-window X update (17:29 EDT)

## Named packages

### npm (21)
- `async-pipeline-builder`
- `build-scripts-utils`
- `chain-key-validator`
- `crypto-credential-scanner`
- `defi-env-auditor`
- `defi-threat-scanner`
- `deployment-key-auditor`
- `dev-env-bootstrapper`
- `eth-wallet-sentinel`
- `llm-context-compressor`
- `mnemonic-safety-check`
- `model-switch-router`
- `node-setup-helpers`
- `project-init-tools`
- `prompt-engineering-toolkit`
- `solidity-deploy-guard`
- `token-usage-tracker`
- `wallet-backup-verifier`
- `wallet-security-checker`
- `web3-secrets-detector`
- `workspace-config-loader`

### PyPI (7)
- `cryptowallet-safety`
- `data-pipeline-check`
- `defi-risk-scanner`
- `env-loader-cli`
- `eth-security-auditor`
- `git-config-sync`
- `solidity-build-guard`

### Crates.io (6)
- `move-analyzer-build`
- `move-compiler-tools`
- `move-project-builder`
- `sui-framework-helpers`
- `sui-move-build-helper`
- `sui-sdk-build-utils`

## Infrastructure (dead-drop and C2)

- **GitHub Pages dead-drop:** `ddjidd564.github.io`
- **Payload-hosting path:** `ddjidd564.github.io/defi-security-best-practices/`
- **No additional IPs or non-GitHub URLs disclosed by Socket** beyond the
  GitHub Pages dead-drop infrastructure.

## Payload

- **File:** `trap-core.js` (48,485 bytes)
- **Obfuscation:** XOR encryption with key `cargo-build-helper-2026`
- **Self-description embedded in payload:** "Universal AI Agent Extraction
  Framework" (attacker's own framing per Socket; not a vendor designation)
- **Campaign marker:** `P-2024-001`
- **Hashes:** Socket did NOT publish SHA-256 hashes for `trap-core.js` in this
  disclosure. Hash absence flagged for grader's IOC-count tally.

## Persistence vectors

Novel persistence-mechanism mix per Socket:
- `.cursorrules` injection (Cursor AI-IDE config — agentic-development-tool
  rules file)
- `CLAUDE.md` injection (Claude Code project-instructions file)
- Git hooks
- Shell hooks
- `systemd` units
- `cron` entries
- SSH (specific mechanism not elaborated by Socket)

The `.cursorrules` + `CLAUDE.md` AI-agent-persistence pattern is **novel
relative to prior corpus-tracked supply-chain campaigns**. Targeting agentic
coding-assistant configuration files as a persistence surface is operationally
new in the Archimedes corpus. Socket characterizes this as part of the
"Universal AI Agent Extraction Framework" self-description; Archimedes
preserves Socket's framing verbatim per Hard Rule 2.

## Credential exfiltration scope

Per Socket, the stealer targets:
- SSH keys
- Crypto-wallet data — specifically Sui, Solana, and Aptos chains
- AWS credentials
- GitHub tokens and credentials
- Browser profile data (general)
- Browser login databases
- Crypto-wallet browser-extension data
- Environment variables
- API keys
- Local development configuration files

## Target sectors

- Cryptocurrency developers (broad)
- DeFi developers
- Solana ecosystem developers
- Sui ecosystem developers (Move language toolchain — distinctive Crates.io
  targeting)
- Aptos ecosystem developers (Move language toolchain)
- AI ecosystem developers (decoy-repo + .cursorrules + CLAUDE.md vectors)
- Security developers (defi-threat-scanner, web3-secrets-detector,
  crypto-credential-scanner type-squat surface)

**No aerospace / defense / DIB / CMMC-aligned victim or downstream named.**

## Detection timeline (per Socket)

- Earliest package observation: `eth-security-auditor@0.1.0` (PyPI)
  2026-05-22T20:20:18Z
- Average Socket detection time: 5 minutes 56 seconds post-publication
- Fastest Socket detection: 58 seconds post-publication

Socket attributes detection speed to their published-package-monitoring
pipeline; framing preserved verbatim per Hard Rule 2.

## Reporting actions taken by Socket

- Packages reported to npm, PyPI, and Crates.io registries
- GitHub account `ddjidd564` reported to GitHub
- Disclosure published to Socket blog at 2026-05-24T13:32:20Z (09:32 EDT)
- Public-channel disclosure via @SocketSecurity X at 19:05 UTC (15:05 EDT)
- Follow-up disclosure at 21:29 UTC (17:29 EDT, post-window) with
  additional GitHub-activity findings

## Single-source veto note

Socket is the **sole originating primary** on this disclosure. The
in-window vx-underground tweet at 15:45 UTC is a pure relay with no
independent corroborating telemetry. Socket's own X account at 15:05 UTC is
an extension of the vendor's own disclosure, not an independent source.

No second-source independent corroboration in window. **Single-source veto
applies** for the grader's WEP cap on:

1. The 34-package + 384-version scope claim
2. The first-documented three-ecosystem simultaneous-publication framing
3. The novelty of `.cursorrules` + `CLAUDE.md` AI-agent persistence
4. The cross-attempted-injection into `modelcontextprotocol` and
   `gemini-cli` upstream repositories (the riskiest content-injection claim
   — post-window addendum carries highest-risk hyperbole potential and
   Hard Rule 2 sensitivity)

Cross-vendor corroboration to watch: Snyk, StepSecurity, Aikido, Wiz
Research, Unit 42 (npm threat landscape series), SafeDep — none in-window.

## Hard Rules compliance

- **Rule 2 (no Archimedes-originated attribution):** UNATTRIBUTED per Socket
  explicit decline. Archimedes does NOT cross-walk to TeamPCP / Mini
  Shai-Hulud / Shai-Hulud / any roster actor. The "Universal AI Agent
  Extraction Framework" self-description is the attacker's own framing
  embedded in `trap-core.js`; preserved verbatim as Socket-reported.
- **Rule 3 (no exploitation content):** No PoC code, no exploit walkthrough,
  no payload reconstruction. References to `trap-core.js` are descriptive.
  XOR key value disclosed only because Socket published it as an IOC; not
  reproduced as part of an exploitation guide.
- **Rule 4 (passive only):** No active scans invoked. Socket blog WebFetch
  + vx-underground RSS + Socket X RSS only — all passive OSINT against
  third-party publishers.
- **Rule 6 (15-word quote limit):** No quotes used in this raw-signal beyond
  the attacker's own self-description ("Universal AI Agent Extraction
  Framework" — 6 words, used once, preserved verbatim as Socket-reported).
- **Rule 7 (credentials radioactive):** No credentials surfaced in source;
  Socket disclosure focuses on the stealer's scope without naming any
  victim credentials.

## Extraction notes

- Language: en
- Article type: vendor research blog
- Source grade (provisional): B (Socket per source-grades.yaml 2026-05-14)
- Raw IOC extraction invoked: YES (see IOCs section below)

## IOCs (from ioc-extraction skill)

```yaml
extraction_metadata:
  source_brief_id: raw-2026-05-24-pm-001-socket-trapdoor-crypto-stealer-multi-ecosystem-npm-pypi-crates-34-packages-384-versions
  source_url: https://socket.dev/blog/trapdoor-crypto-stealer-npm-pypi-crates
  extracted_at: 2026-05-24T15:35:00-04:00
  extractor: collector subagent (manual extraction per skill template)
  context: "Multi-ecosystem supply-chain campaign UNATTRIBUTED; IOCs extracted for grader review and master-index regeneration on promotion"
  actor_id: null
  attribution_claims: []
  attribution_claims_note: "Socket explicitly declines attribution. No tracked roster actor named."

iocs:
  # Network infrastructure (GitHub Pages dead-drop)
  - type: domain
    value: ddjidd564.github.io
    context: "TrapDoor C2 / payload-hosting dead-drop hosted on GitHub Pages — attacker-controlled GitHub account ddjidd564"
    role: c2_payload_host
    first_seen: 2026-05-22T20:20:18Z   # earliest TrapDoor package observation
    last_seen: 2026-05-24T13:32:20Z    # Socket disclosure
    confidence: high                    # vendor first-party disclosure on observed payload-pull infrastructure
    source: socket

  - type: url
    value: https://ddjidd564.github.io/defi-security-best-practices/
    context: "TrapDoor full payload-hosting path on GitHub Pages dead-drop; thematic AI/security/DeFi decoy framing"
    role: c2_payload_host
    first_seen: 2026-05-22T20:20:18Z
    last_seen: 2026-05-24T13:32:20Z
    confidence: high
    source: socket

  # Attacker identities
  - type: other
    type_detail: github_account
    value: ddjidd564
    context: "TrapDoor attacker GitHub account; hosts C2 dead-drop ddjidd564.github.io; reported to GitHub by Socket"
    role: attacker_identity
    first_seen: 2026-05-22T20:20:18Z
    last_seen: 2026-05-24T13:32:20Z
    confidence: high
    source: socket

  - type: other
    type_detail: npm_account
    value: asdxzxc
    context: "TrapDoor attacker npm account; published 21 malicious npm packages"
    role: attacker_identity
    first_seen: 2026-05-22T20:20:18Z
    last_seen: 2026-05-24T13:32:20Z
    confidence: high
    source: socket

  # Payload artifact
  - type: file_path
    value: trap-core.js
    context: "TrapDoor stealer payload file (48,485 bytes); XOR-obfuscated with key 'cargo-build-helper-2026'; embedded P-2024-001 campaign marker; self-described 'Universal AI Agent Extraction Framework'"
    role: payload_file
    confidence: high
    source: socket
    note: "SHA-256 hash NOT published by Socket; cannot record hash IOC. Filename + byte-size + XOR-key form composite IOC; hash unavailable in this disclosure."

  # Campaign markers (other-type)
  - type: other
    type_detail: campaign_marker
    value: P-2024-001
    context: "TrapDoor internal campaign marker embedded in trap-core.js payload"
    role: campaign_id
    confidence: high
    source: socket

  - type: other
    type_detail: xor_key
    value: cargo-build-helper-2026
    context: "TrapDoor XOR-obfuscation key for trap-core.js payload deobfuscation"
    role: deobfuscation_key
    confidence: high
    source: socket

  # Malicious package identities — npm (21 packages, all attributed to attacker npm account asdxzxc)
  - type: other
    type_detail: malicious_package_npm
    value: async-pipeline-builder
    context: "TrapDoor malicious npm package"
    role: malicious_package
    confidence: high
    source: socket
  - type: other
    type_detail: malicious_package_npm
    value: build-scripts-utils
    role: malicious_package
    confidence: high
    source: socket
  - type: other
    type_detail: malicious_package_npm
    value: chain-key-validator
    role: malicious_package
    confidence: high
    source: socket
  - type: other
    type_detail: malicious_package_npm
    value: crypto-credential-scanner
    role: malicious_package
    confidence: high
    source: socket
  - type: other
    type_detail: malicious_package_npm
    value: defi-env-auditor
    role: malicious_package
    confidence: high
    source: socket
  - type: other
    type_detail: malicious_package_npm
    value: defi-threat-scanner
    role: malicious_package
    confidence: high
    source: socket
  - type: other
    type_detail: malicious_package_npm
    value: deployment-key-auditor
    role: malicious_package
    confidence: high
    source: socket
  - type: other
    type_detail: malicious_package_npm
    value: dev-env-bootstrapper
    role: malicious_package
    confidence: high
    source: socket
  - type: other
    type_detail: malicious_package_npm
    value: eth-wallet-sentinel
    role: malicious_package
    confidence: high
    source: socket
  - type: other
    type_detail: malicious_package_npm
    value: llm-context-compressor
    role: malicious_package
    confidence: high
    source: socket
  - type: other
    type_detail: malicious_package_npm
    value: mnemonic-safety-check
    role: malicious_package
    confidence: high
    source: socket
  - type: other
    type_detail: malicious_package_npm
    value: model-switch-router
    role: malicious_package
    confidence: high
    source: socket
  - type: other
    type_detail: malicious_package_npm
    value: node-setup-helpers
    role: malicious_package
    confidence: high
    source: socket
  - type: other
    type_detail: malicious_package_npm
    value: project-init-tools
    role: malicious_package
    confidence: high
    source: socket
  - type: other
    type_detail: malicious_package_npm
    value: prompt-engineering-toolkit
    role: malicious_package
    confidence: high
    source: socket
  - type: other
    type_detail: malicious_package_npm
    value: solidity-deploy-guard
    role: malicious_package
    confidence: high
    source: socket
  - type: other
    type_detail: malicious_package_npm
    value: token-usage-tracker
    role: malicious_package
    confidence: high
    source: socket
  - type: other
    type_detail: malicious_package_npm
    value: wallet-backup-verifier
    role: malicious_package
    confidence: high
    source: socket
  - type: other
    type_detail: malicious_package_npm
    value: wallet-security-checker
    role: malicious_package
    confidence: high
    source: socket
  - type: other
    type_detail: malicious_package_npm
    value: web3-secrets-detector
    role: malicious_package
    confidence: high
    source: socket
  - type: other
    type_detail: malicious_package_npm
    value: workspace-config-loader
    role: malicious_package
    confidence: high
    source: socket

  # Malicious package identities — PyPI (7 packages)
  - type: other
    type_detail: malicious_package_pypi
    value: cryptowallet-safety
    role: malicious_package
    confidence: high
    source: socket
  - type: other
    type_detail: malicious_package_pypi
    value: data-pipeline-check
    role: malicious_package
    confidence: high
    source: socket
  - type: other
    type_detail: malicious_package_pypi
    value: defi-risk-scanner
    role: malicious_package
    confidence: high
    source: socket
  - type: other
    type_detail: malicious_package_pypi
    value: env-loader-cli
    role: malicious_package
    confidence: high
    source: socket
  - type: other
    type_detail: malicious_package_pypi
    value: eth-security-auditor
    context: "Earliest observed TrapDoor package — eth-security-auditor@0.1.0 PyPI 2026-05-22T20:20:18Z"
    role: malicious_package
    confidence: high
    source: socket
  - type: other
    type_detail: malicious_package_pypi
    value: git-config-sync
    role: malicious_package
    confidence: high
    source: socket
  - type: other
    type_detail: malicious_package_pypi
    value: solidity-build-guard
    role: malicious_package
    confidence: high
    source: socket

  # Malicious package identities — Crates.io (6 packages — first ecosystem-tier expansion to Crates.io in corpus)
  - type: other
    type_detail: malicious_package_crates_io
    value: move-analyzer-build
    role: malicious_package
    confidence: high
    source: socket
  - type: other
    type_detail: malicious_package_crates_io
    value: move-compiler-tools
    role: malicious_package
    confidence: high
    source: socket
  - type: other
    type_detail: malicious_package_crates_io
    value: move-project-builder
    role: malicious_package
    confidence: high
    source: socket
  - type: other
    type_detail: malicious_package_crates_io
    value: sui-framework-helpers
    role: malicious_package
    confidence: high
    source: socket
  - type: other
    type_detail: malicious_package_crates_io
    value: sui-move-build-helper
    role: malicious_package
    confidence: high
    source: socket
  - type: other
    type_detail: malicious_package_crates_io
    value: sui-sdk-build-utils
    role: malicious_package
    confidence: high
    source: socket

ioc_counts:
  total: 38      # 1 domain + 1 url + 2 attacker_identity + 1 file_path + 1 campaign_marker + 1 xor_key + 21 npm + 7 pypi + 6 crates_io
  by_type:
    domain: 1
    url: 1
    other_github_account: 1
    other_npm_account: 1
    file_path: 1
    other_campaign_marker: 1
    other_xor_key: 1
    other_malicious_package_npm: 21
    other_malicious_package_pypi: 7
    other_malicious_package_crates_io: 6
  hashes_unavailable_in_source: true
  hashes_unavailable_note: "Socket did NOT publish SHA-256 hashes for trap-core.js in this disclosure. Composite IOC built from filename + byte-size + XOR-key only."

attribution_claims: []
attribution_claims_note: |
  Socket explicitly declines attribution. The malware's "Universal AI Agent
  Extraction Framework" self-description is the attacker's own framing
  embedded in trap-core.js — preserved verbatim as Socket-reported. No
  tracked roster actor named. Specifically NOT TeamPCP / Shai-Hulud / Mini
  Shai-Hulud per Socket's explicit decline. Archimedes does NOT originate
  attribution per Hard Rule 2.
```
