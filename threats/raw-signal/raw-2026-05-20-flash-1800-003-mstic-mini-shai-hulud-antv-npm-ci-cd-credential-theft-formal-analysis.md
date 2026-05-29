---
raw_id: raw-2026-05-20-flash-1800-003
collected_at: 2026-05-20T18:11:00-04:00
run_id: flash-sweep-20260520-180000-ad-hoc
collection_mode: flash_sweep
test: false
source:
  source_yaml_id: mstic
  source_name: "Microsoft Security Blog (Microsoft Defender Security Research Team) — A-grade vendor self-publication, MSTIC adjacent"
  source_url: https://www.microsoft.com/en-us/security/blog/2026/05/20/mini-shai-hulud-compromised-antv-npm-packages-enable-ci-cd-credential-theft/
  published_at: 2026-05-20T13:48:44-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords:
    - Mini Shai-Hulud
    - antv npm supply chain
    - echarts-for-react
    - G2 G6 charting libraries
    - GitHub Actions Runner credential theft
    - AWS Secrets Manager enumeration
    - HashiCorp Vault token paths
    - npm token validation OIDC publish
    - Kubernetes service account tokens
    - 1Password CLI 2FA bypass
    - Bun runtime payload
    - PBKDF2 SHA-256 string obfuscation
    - SLSA provenance forgery
    - GitHub Actions Runner.Worker memory scraping
    - /proc PID scanning Linux
    - Linux gated payload execution
    - preinstall hook
triage_tags:
  - in_window
  - mstic_a_grade_microsoft_defender_security_research_team_self_publication
  - mini_shai_hulud_campaign_lineage_vt_006
  - teampcp_attribution_layer_outside_mstic_publication_scope
  - mstic_uses_unattributed_actor_framing_per_hard_rule_2
  - corroboration_uplift_on_finding_2026_05_20_0001_kac_a1_test_tripwire
  - anti_noise_lock_teampcp_github_internal_repos_breach_via_vscode_extension_2026_05_20
  - flash_trigger_1_fail_no_cve_in_publication
  - flash_trigger_2_fail_actor_unattributed_by_mstic
  - flash_trigger_3_fail_splunk_first_party_dormant
  - flash_trigger_4_pass_corpus_level_ttp_uplift_but_anti_noise_absorbs
  - flash_trigger_5_marginal_fail_no_a_and_d_prime_named_anti_noise_absorbs
  - flash_trigger_6_fail_no_vuln
  - grader_handoff_for_corroboration_block_morning_brief
  - ttp_uplift_bun_runtime_pbkdf2_proc_scanning_slsa_provenance_forgery
  - kac_a1_test_tripwire_finding_2026_05_20_0001_open_until_2026_05_23_07_30_edt
  - splunk_first_party_zero_hits_50th_consecutive_dormant_sweep
  - ad_relevance_high_ci_cd_credential_theft_universal_in_a_and_d_devops_estate
iocs_extracted: true
iocs_count: 4
text_word_count: 1100
promoted: true
promoted_to_finding: finding-2026-05-21-0007
promoted_at: 2026-05-21T08:35:00-04:00
ttl_expires_at: 2026-08-18T18:11:00-04:00
---

# MSTIC formal analysis — Mini Shai-Hulud: Compromised @antv npm packages enable CI/CD credential theft

Microsoft Security Blog (Microsoft Defender Security Research Team
byline) published a deep technical analysis of the Mini Shai-Hulud
@antv npm supply-chain compromise today 2026-05-20T17:48 UTC (13:48
EDT inside this sweep's 6h window). This is the A-grade Microsoft-side
formal technical attestation of the campaign cluster the Archimedes
corpus has been tracking since 2026-05-19 (VT-006 / finding-2026-05-20-0001 /
the Mini Shai-Hulud morning-brief KAC A1 Test tripwire).

Source URL: `https://www.microsoft.com/en-us/security/blog/2026/05/20/mini-shai-hulud-compromised-antv-npm-packages-enable-ci-cd-credential-theft/`

## Significance — corroboration uplift, not a new FLASH trigger

This MSTIC publication is the second A-grade vendor publication on
the Mini Shai-Hulud / @antv lineage in 6 hours (Unit 42 published a
landscape update at 15:30 EDT, raw-2026-05-20-flash-1800-004). The
campaign cluster is locked under anti-noise
`teampcp-github-internal-repos-breach-via-vscode-extension-2026-05-20`
(valid to 2026-05-21T06:08:00-04:00 per the 06:08 queued FLASH).

Per FLASH-POLICY anti-noise rule 1, this is CORROBORATION-UPLIFT, NOT
a new trigger fire. The grader's morning-brief handoff should treat
this as evidence for upgrading the WEP confidence on the existing
campaign-cluster findings (finding-2026-05-20-0001, finding-2026-05-20-
FLASH-0001) and as a potential closer for the KAC A1 Test tripwire on
the Claude-Code-backdoor-drop claim (NOTE: tripwire may NOT close
because MSTIC does not specifically validate the Claude-Code-backdoor-
drop claim from SecurityWeek; tripwire close requires direct A-grade
attestation OF THAT specific claim, not of the parent campaign).

## MSTIC's attribution framing (Hard Rule 2 — verbatim preservation)

MSTIC frames the actor as: **"A threat actor compromised an @antv
maintainer account and published malicious versions of widely used
data-visualization packages, resulting in cascading downstream
impact."** (24 words — context-only; not cited as quote in this
extraction summary)

Key attribution-language facts:
- MSTIC does NOT name a tracked actor
- MSTIC does NOT use the Mini Shai-Hulud name as actor attribution;
  it uses it as CAMPAIGN/MALWARE designation
- MSTIC does NOT propagate to TeamPCP attribution (the Breached-forum
  self-claim chain is OUTSIDE MSTIC's publication scope)
- The "@antv maintainer account" was the initial-compromise vector;
  MSTIC does NOT describe how the maintainer account was compromised
  (whether via VS Code extension supply chain per the TeamPCP self-
  claim, or via another vector)

**Hard Rule 2 binding:** Archimedes does NOT cross-walk MSTIC's
unattributed framing to TeamPCP. The TeamPCP attribution remains
single-chain (Breached forum self-claim relayed by three B-grade
media — finding-2026-05-20-FLASH-0001). MSTIC's publication corroborates
the CAMPAIGN MECHANIC but does NOT add to the actor attribution layer.

## Confirmed by @antv maintainers

Per MSTIC: "The authors of the antv account have also since confirmed
in a ticket on the repo that the situation is now resolved." (15 words —
at Hard Rule 7 quote budget for this source).

This is direct first-party confirmation by the compromised maintainer
chain — strong evidence the campaign mechanic is real and that
remediation has occurred at the @antv account level.

## Attack chain (technical detail, defender-actionable)

Per MSTIC's chain summary:

1. Maintainer account compromise (vector unspecified by MSTIC)
2. Publication of malicious @antv package versions
3. Downstream dependency amplification — MSTIC names
   `echarts-for-react` (over 1 million weekly downloads),
   `size-sensor`, "and others"
4. Automatic payload execution via `preinstall` hook during `npm install`
5. Execution chain: node → shell → bun → payload (Bun runtime
   installed if absent)

## Payload technical detail (TTP uplift over prior coverage)

These are defender-actionable indicators of compromise; NO attack code
extracted (Hard Rule 3 compliance):

**Obfuscation:**
- Layer 1: 1,732 Base64-encoded strings in a rotated array, decoded
  via lookup function with shuffle key `0xa31de`
- Layer 2: PBKDF2 + SHA-256 cipher with cipher salt
  `a8269c01069452afb8a54de904e6419578d155fdbdb9e566bab8576a4266b61e`
  and IV `7f44e4ba6f6a71bd0f789e7f83bd3104` — encrypts critical strings
  including C2 domain and env var names, decrypted at runtime

**Execution gating:**
- Payload exits immediately if NOT running on GitHub Actions on Linux
  (detected via `GITHUB_ACTIONS` and `RUNNER_OS` env vars; env var
  names themselves are PBKDF2-encrypted)
- Branch avoidance: skips main, master, dependabot/, renovate/, and
  gh-pages branches when using Git API exfiltration

**Credential theft surface (per MSTIC) — six platforms:**

1. **GitHub:**
   - Extracts `GITHUB_TOKEN`
   - Scans for Personal Access Tokens (pattern `gh[op]_`) and
     installation tokens (pattern `ghs_`)
   - Validates tokens via `/user` API
   - Enumerates repo and org secrets via
     `/actions/secrets?per_page=100` and
     `/actions/organization-secrets?per_page=100`
2. **AWS:**
   - Queries Instance Metadata Service at `169.254.169.254`
   - Queries Elastic Container Service metadata at `169.254.170.2`
   - Reads `~/.aws/` files
   - Harvests environment variables
   - Calls `SecretsManager:ListSecrets` and `GetSecretValue` across
     all regions
3. **HashiCorp Vault:**
   - Searches 12+ token paths including
     `/var/run/secrets/vault/token`, `~/.vault-token`,
     `/home/runner/.vault-token`, `/root/.vault-token`,
     `/etc/vault/token`
   - Connects to local Vault at `127.0.0.1:8200`
4. **npm:**
   - Validates tokens via `/-/whoami`
   - Exchanges OpenID Connect (OIDC) tokens for publish access
   - Enumerates packages
5. **Kubernetes:**
   - Reads service account tokens
   - Enumerates namespace secrets
6. **1Password:**
   - Interacts with CLI
   - Attempts master password extraction with two-factor authentication
     (2FA) bypass

**Runner memory scraping (most concerning capability):**
- Locates GitHub Actions Runner.Worker PID via `/proc` scanning
  (function name `findRunnerWorkerPIDLinux`)
- Scans `/proc/<pid>/cmdline` for "Runner.Worker"
- Extracts secrets from process memory via pattern matching for
  `"[name]":{"value":"[value]","isSecret":true}` JSON structures
- **Bypasses GitHub Actions normal secret masking** by reading secrets
  directly from process memory before mask redaction

**SLSA provenance forgery:**
- MSTIC notes the payload forges SLSA (Supply chain Levels for Software
  Artifacts) provenance metadata to evade analysis
- This is a sophistication signal — SLSA provenance forgery requires
  understanding of the SLSA attestation format

**Dual-channel exfiltration:**
- MSTIC notes "dual-channel data exfiltration" without specifying
  channels in the published summary; direct article retrieval would
  resolve

## A&D relevance — HIGH

CI/CD credential theft is a universal exposure surface in A&D devops
estates:
- Defense primes and Tier-1/Tier-2 contractors run GitHub Enterprise,
  GitHub Actions CI/CD pipelines, AWS / Azure cloud deployments,
  HashiCorp Vault for secrets management, Kubernetes for container
  orchestration, 1Password for password management
- echarts-for-react with 1M+ weekly downloads is plausibly in the
  dependency graph of many A&D-prime internal data-visualization
  applications
- GitHub Actions Runner memory scraping is a particularly concerning
  capability because it defeats secret-masking — a control most teams
  rely on as a primary defense

## FLASH trigger evaluation (collector-side)

- **Trigger 1 (critical-cve-exploited):** FAIL. No CVE in publication
  (this is a campaign-mechanic analysis, not a vulnerability).
- **Trigger 2 (tracked-actor-attribution-new):** FAIL. MSTIC uses
  unattributed-actor framing; TeamPCP attribution is outside MSTIC
  publication scope.
- **Trigger 3 (first-party-ioc-hit):** FAIL. Splunk dormant continues
  (50th sweep).
- **Trigger 4 (tracked-actor-ttp-change):** TECHNICALLY PASSES on
  TTP-uplift dimension (Bun runtime, PBKDF2/SHA-256 obfuscation, /proc
  PID scanning, SLSA provenance forgery, Runner.Worker memory scraping
  bypassing secret masking are all NEW technical detail relative to
  prior corpus coverage of Mini Shai-Hulud) — BUT MSTIC does NOT
  attribute to a roster actor, so the trigger's attributability
  predicate FAILS. Trigger 4 strict-read does NOT fire.
- **Trigger 5 (ad-sector-campaign):** FAIL on watchlist-specificity
  (no A&D-prime named); anti-noise lock absorbs in any case.
- **Trigger 6 (zero-day-no-patch):** FAIL (not a vulnerability).

This is NOT a FLASH candidate. It IS a high-value grader handoff for
the next morning brief CORROBORATION block on the existing campaign-
cluster findings.

## Grader handoff (morning brief 2026-05-21)

The grader should evaluate:
- Upgrade WEP on finding-2026-05-20-0001 (Mini Shai-Hulud / @antv)
  from B2 / likely to A1 / very-likely or A2 / very-likely — MSTIC
  publication is direct A-grade vendor attestation of the campaign
  mechanic
- Resolution status of the KAC A1 Test tripwire (72h closes
  2026-05-23 07:30 EDT) — MSTIC publication does NOT directly
  validate or refute the SecurityWeek-asserted "Mini Shai-Hulud drops
  backdoors into Claude Code" claim from finding-2026-05-20-0001. The
  KAC A1 Test was specifically on Claude Code as a backdoor-drop
  venue; MSTIC's publication focuses on CI/CD credential theft via
  GitHub Actions Runner. **The tripwire should remain OPEN** pending
  direct corroboration of the Claude Code backdoor-drop claim
  specifically.
- Whether to merge or differentiate the Unit 42 npm landscape update
  (raw-2026-05-20-flash-1800-004) into the same uplift package

## Citations within Hard Rule 7 budget

- MSTIC: "the authors of the antv account have also since confirmed
  in a ticket on the repo that the situation is now resolved"
  (15 words, at budget — direct first-party-confirmation quote)

## Extraction notes

- Language: en
- Publisher byline: Microsoft Defender Security Research Team
  (institutional, no individual byline)
- Article type: vendor threat-intelligence technical analysis
- Raw IOC extraction invoked: yes (network IOCs + payload artifacts)

## IOCs (defender-actionable)

- AWS metadata IP (legitimate, but called by malicious payload):
  `169.254.169.254`
- ECS metadata IP (same): `169.254.170.2`
- Vault default local IP/port (legitimate): `127.0.0.1:8200`
- PBKDF2 cipher salt (payload fingerprint):
  `a8269c01069452afb8a54de904e6419578d155fdbdb9e566bab8576a4266b61e`
- PBKDF2 IV (payload fingerprint):
  `7f44e4ba6f6a71bd0f789e7f83bd3104`
- Obfuscation array shuffle key (payload fingerprint): `0xa31de`

NOTE: The first three (AWS, ECS, Vault local IPs) are LEGITIMATE
infrastructure addresses that the payload CALLS; they are NOT
attacker-controlled and should not be added to deny-lists.

The PBKDF2 salt + IV + shuffle key ARE payload fingerprints that can
be used as YARA-rule anchors or static-analysis signatures by detection
engineering teams.

NO C2 domains or attacker-controlled IPs extracted from MSTIC summary
in this sweep (encrypted via PBKDF2 at runtime; full article retrieval
would surface the decrypted C2 domain set).

## Anti-noise compliance

Absorbed under existing lock
`teampcp-github-internal-repos-breach-via-vscode-extension-2026-05-20`.
No new lock proposed.
