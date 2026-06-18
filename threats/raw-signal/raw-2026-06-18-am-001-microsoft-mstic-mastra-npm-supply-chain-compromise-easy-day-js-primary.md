---
raw_id: raw-2026-06-18-am-001-microsoft-mstic-mastra-npm-supply-chain-compromise-easy-day-js-primary
collected_at: 2026-06-18T07:34:00-04:00
run_id: pre-brief-20260618-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: mstic
  source_name: Microsoft Threat Intelligence (MSTIC) / Microsoft Defender Security Research Team
  source_url: https://www.microsoft.com/en-us/security/blog/2026/06/17/postinstall-payload-inside-mastra-npm-supply-chain-compromise/
  published_at: 2026-06-17T23:43:04-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [mastra, npm, supply-chain, easy-day-js, postinstall, ehindero, typosquat, ci_cd, AI-developer-tooling, "Microsoft Threat Intelligence", MSTIC]
triage_tags: [supply_chain, ad_adjacent_via_developer_tooling, ir_vendor_corroboration_a_grade, substrate_pivot_candidate_on_carry_forward_reject, ioc_rich, anti_noise_check_against_reject_2026_06_17_0003]
iocs_extracted: true
iocs_count: 9
text_word_count: 1240
promoted: true
promoted_to_finding: finding-2026-06-18-0001
promoted_at: 2026-06-18T08:16:00-04:00
ttl_expires_at: 2026-09-16T07:34:00-04:00
---

# From package to postinstall payload: Inside the Mastra npm supply chain compromise

**Publisher:** Microsoft Threat Intelligence / Microsoft Defender Security Research Team
**Published:** 2026-06-17T23:43 EDT (per RSS feed timestamp)
**URL:** https://www.microsoft.com/en-us/security/blog/2026/06/17/postinstall-payload-inside-mastra-npm-supply-chain-compromise/

## Article body (Microsoft primary)

Microsoft Threat Intelligence identified a large-scale npm supply chain attack affecting "140+ packages across the mastra and @mastra scopes" on the npm registry. The compromise originated from the takeover of the **ehindero** npm maintainer account, which had publish rights across the Mastra ecosystem.

### Attack methodology

The attacker executed a coordinated multi-stage operation. They published **easy-day-js**, "a malicious typosquat of the popular dayjs library" (57M+ weekly downloads), using a coordinating anonymous email account (sergey2016@tutamail.com). The typosquat employed a staged delivery strategy:
- Version 1.11.21 (published 2026-06-16 07:05 UTC) — clean bait code
- Version 1.11.22 (published 2026-06-17 01:01 UTC) — weaponized postinstall hook

Using the compromised ehindero account, attackers then injected easy-day-js@^1.11.21 as a dependency into 140+ packages across the @mastra scope, all tagged as latest. The SemVer range `^1.11.21` ensures resolution to 1.11.22 — the weaponized version.

### Discovery indicators

Microsoft Threat Intelligence identified the compromise through anomalous publishing patterns on the mastra package. All previous versions (through v1.13.0) were published through GitHub Actions OpenID Connect — the legitimate CI/CD pipeline. Version 1.13.1 was manually published by ehindero using a Tutamail address (ehindero2016@tutamail.com), an anonymous email service. The only change between mastra@1.13.0 and mastra@1.13.1 was the addition of easy-day-js@^1.11.21 as a dependency. No corresponding code changes were present in the Mastra GitHub repository.

### Payload execution chain

The postinstall hook executed a 4,572-byte obfuscated dropper (setup.cjs) protected with "JavaScript obfuscation using rotated string arrays and a custom base64 decoder function." The payload followed a five-step sequence:

1. Disabled TLS certificate verification via `NODE_TLS_REJECT_UNAUTHORIZED`
2. Dropped filesystem markers in temporary directories
3. Fetched a ~41 KB second-stage payload from C2 infrastructure
4. Wrote the payload as a randomly named .js file and spawned it as a detached, window-hidden Node.js process
5. Self-deleted the dropper via `fs.rmSync`

The second-stage implant installed cross-platform persistence using "NVM/Node masquerade" naming conventions. On Windows: registry Run keys; on macOS: LaunchAgent files; on Linux: systemd user units. All variants used the misspelled artifact name **protocal.cjs**.

### Windows-specific capabilities

On Windows, the payload performed reflective .NET assembly injection. It enumerated installed applications across Start Menu entries, registry Uninstall keys, and UWP packages via PowerShell's `Get-StartApps` and `Get-AppxPackage` cmdlets. The malware then downloads a .NET DLL loaded directly into memory via reflection, completely bypassing disk-based detection before injecting into cmd.exe processes. The implant also collected cryptocurrency wallet data by matching 166 wallet browser-extension IDs (MetaMask, Phantom, Coinbase Wallet, Binance Wallet, TronLink, others) against Chrome, Edge, and Brave profiles, alongside browser history exfiltration.

### Risk assessment

Microsoft notes: "the payload executes during installation, any developer workstation or continuous integration and continuous delivery (CI/CD) pipeline that ran npm install or npm update after the compromised versions were published was potentially exposed, regardless of whether the package was imported in application code." Affected versions: mastra through 1.13.1 and @mastra packages published by ehindero. Version 1.13.0 and earlier remain unaffected.

### Microsoft attribution language

Microsoft framed this as "organized threat actor activity" rather than opportunistic compromise, based on the use of anonymous email services (Tutamail) for both the compromised publisher and typosquat creator, combined with the staged delivery pattern and professional-grade payload development. NO specific tracked-actor attribution made by Microsoft (no MSTIC weather-name; no UNC / APT alias). NO A&D-prime named victims in this primary.

### Vendor remediation

Microsoft notes the compromised packages have been removed from npm and the attacker's publish access to the @mastra scope has been revoked. Microsoft shared findings with the npm security team. Microsoft Defender Antivirus, Microsoft Defender for Endpoint, and Microsoft Defender XDR provide detections and hunting coverage for suspicious Node.js execution, malicious package behavior, reflective code loading, persistence activity, and command-and-control communication.

---

## Extraction notes

- Language: en
- Publisher byline: Microsoft Defender Security Research Team
- Article type: vendor IR research blog (primary)
- Raw IOC extraction invoked: yes
- Substrate-context: This MSTIC primary substantiates and substantially strengthens carry-forward `reject-2026-06-17-0003` (Mastra-npm AI-app-framework reject from 2026-06-17 morning brief). The earlier reject was on third-party Aikido-Security / BC-Toulas / THN-Lakshmanan single-IR-vendor surface; this MSTIC primary lifts that vetoed layer with A-grade vendor IR research and a rich IOC set.
- A&D-relevance: medium-indirect. The Mastra ecosystem is an AI agent-orchestration framework used in TypeScript / Node.js developer environments. A&D-prime developer-team named-victim layer remains unmet. Anyone running `npm install` on a CI/CD pipeline pulling @mastra after 2026-06-17 ~01:01 UTC is potentially exposed regardless of whether @mastra was imported in app code.
- Anti-noise check against reject-2026-06-17-0003: Hard Rule 1 carry-forward applies. This is substrate-strengthening (IR-vendor independence + IOC set + technical depth) on the same trigger-topic; grader should consider as substrate-pivot UPDATE candidate from reject → finding scaffold IF A&D-prime named-victim emerges OR IF a similarly A-grade vendor (Mandiant / CrowdStrike / Unit-42 / Wiz / Socket / Snyk / Sansec) publishes independent corroboration on the same campaign within 72h.
- Anti-attribution discipline: Microsoft did NOT cross-walk to TeamPCP / Shai-Hulud-family / Lazarus / DPRK / any roster actor. Hard Rule 2 BINDING — Archimedes does NOT originate cross-walk attribution.

## IOCs (from ioc-extraction skill)

```yaml
indicators:
  - type: domain
    value: "tutamail.com"
    role: "anonymous email service used by both compromised publisher (ehindero2016@tutamail.com) and typosquat publisher (sergey2016@tutamail.com)"
    confidence: high
    first_seen: 2026-06-16
    last_seen: 2026-06-17
  - type: ip
    value: "23.254.164.92"
    role: "primary C2"
    confidence: high
  - type: ip
    value: "23.254.164.123"
    role: "secondary C2"
    confidence: high
  - type: url
    value: "https://23.254.164.92:8000/update/49890878"
    role: "payload-fetch endpoint"
    confidence: high
  - type: sha256
    value: "B122A9873BEDF145AE2A7FD024B5F309007DBB025149F4DC4AC3F7E4F32A36A4"
    file: "setup.cjs"
    confidence: high
  - type: sha256
    value: "AE70DD4F6BC0D1C8C2848E4E6B51934626C4818DCB5AF99D080DDBD7DC337185"
    file: "easy-day-js-1.11.22.tgz"
    confidence: high
  - type: sha256
    value: "B73DE25C053C3225A077738A1FCBD9CA6966D7B3CD6F5494A30F0AA0EAE55C7E"
    file: "mastra-1.13.1.tgz"
    confidence: high
  - type: filename
    value: "protocal.cjs"
    role: "persistence artifact (misspelled spelling preserved verbatim)"
    confidence: high
  - type: account
    value: "ehindero (npm maintainer, compromised)"
    confidence: high
  - type: account
    value: "sergey2016 (easy-day-js publisher, anonymous tutamail)"
    confidence: high
attribution_claims:
  - actor: null
    asserted_by: Microsoft Threat Intelligence
    language: "organized threat actor activity"
    confidence: not_a_specific_actor_attribution
    notes: "Microsoft did NOT cross-walk to TeamPCP / Shai-Hulud / any roster actor."
```
