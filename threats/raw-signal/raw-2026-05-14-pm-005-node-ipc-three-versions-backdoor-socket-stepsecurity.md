---
raw_id: raw-2026-05-14-pm-005
collected_at: 2026-05-14T15:54:00-04:00
run_id: pre-brief-20260514-153000
collection_mode: pre_brief_collection
test: false
source:
  source_yaml_id: thehackernews
  source_name: "The Hacker News (relay of Socket + StepSecurity)"
  source_url: https://thehackernews.com/2026/05/stealer-backdoor-found-in-3-node-ipc.html
  published_at: 2026-05-14T13:22:43-04:00
corroborating_sources:
  - source_yaml_id: null
    source_name: "Socket (originating research vendor — NOT IN source-grades.yaml, first-citation flag)"
    source_url: null
    role: originating_primary_malicious_version_detection_and_stealer_behavior_analysis
  - source_yaml_id: stepsecurity
    source_name: "StepSecurity (originating research vendor — provisional B in source-grades.yaml)"
    source_url: null
    role: co_primary_exfiltration_mechanism_analysis
match_reason:
  watchlist: []
  actors: []                                   # UNATTRIBUTED — no Shai-Hulud / TeamPCP / other-roster-actor claim
  vulnerabilities: []                          # No CVE issued at evaluation time
  keywords: [node-ipc, npm, supply-chain, atiertant, sh.azurestaticprovider, dns-txt-exfil, stealer, backdoor, credential-theft]
triage_tags:
  - non_flash
  - brief_update
  - unattributed
  - supply_chain
  - npm
  - account_compromise_or_maintainer_addition
  - ad_sector_indirect_dependency_graph_unknown
  - ioc_rich
  - dual_dns_exfil_pattern
  - 90_credential_categories_exfil
iocs_extracted: true
iocs_count: 5    # 1 domain + 2 DNS resolvers + 1 maintainer-account + 3 versions = ~7 distinct artifacts
text_word_count: 700
promoted: true
promoted_to_finding: finding-2026-05-14-0009
promoted_at: 2026-05-14T16:04:00-04:00
ttl_expires_at: 2026-08-12T15:54:00-04:00
---

# Socket + StepSecurity identify 3 backdoored node-ipc npm versions; ~90 credential categories exfil via DNS-TXT + HTTPS-POST; unattributed

## Cover

Cybersecurity researchers at **Socket** and **StepSecurity** have identified three malicious versions of the **node-ipc** npm package published by an account named **"atiertant"** with no prior publish history. The Hacker News relayed the disclosure on **2026-05-14T13:22 EDT**.

**Malicious versions** (verbatim per Socket + StepSecurity per The Hacker News):
- node-ipc@9.1.6
- node-ipc@9.2.3
- node-ipc@12.0.1

The last legitimate node-ipc publish was August 2024. The package is a popular Node.js inter-process-communication library with deep dependency-graph reach into developer tooling — its compromise is significant by ecosystem scope alone, even at the surface of "3 backdoored versions, unattributed."

**Stealer/backdoor behavior**:
- Exfiltrates **approximately 90 categories** of developer credentials and cloud secrets to attacker C2
- C2 domain: **sh.azurestaticprovider[.]net**
- Exfil channels: **HTTPS POST + DNS TXT record encoding** (dual-channel)
- DNS resolvers used: **1.1.1.1 (primary)** and **8.8.8.8 (fallback)** — bypasses environments that block one resolver
- Persistence: package-installation-time activation; activates on `npm install` of any affected version

**Attribution**: **UNATTRIBUTED**. Socket + StepSecurity do NOT claim a Shai-Hulud / Mini Shai-Hulud / TeamPCP lineage at this disclosure surface, despite operational-pattern adjacency (developer-credential targeting, supply-chain via npm). The Hacker News framing notes "no specific threat actor family identified."

**Compromise vector**: account compromise OR unauthorized maintainer addition. Atiertant account exhibits the no-prior-publish-history pattern consistent with credential-takeover OR malicious maintainer insertion. Researchers do not yet have evidence to distinguish.

---

## Article primary content (The Hacker News relay of Socket + StepSecurity, Hard Rule 7 quote-limited)

### Three confirmed malicious versions

| Version | Confirmation | Source |
|---|---|---|
| node-ipc@9.1.6 | "confirmed as malicious" | Socket + StepSecurity |
| node-ipc@9.2.3 | "confirmed as malicious" | Socket + StepSecurity |
| node-ipc@12.0.1 | "confirmed as malicious" | Socket + StepSecurity |

### IOCs (cluster-scope)

- **C2 domain**: `sh.azurestaticprovider[.]net`
- **DNS resolvers (dual-fallback)**: 1.1.1.1 (primary), 8.8.8.8 (fallback)
- **Exfil method**: HTTPS POST + DNS TXT record encoding (dual-channel)
- **Maintainer account**: `atiertant` — no prior publish history with this package
- **Targeted credentials**: approximately 90 categories spanning developer-credential + cloud-secret categories (per Socket + StepSecurity analysis)

### Attribution language

The Hacker News explicitly notes: **"No specific threat actor family identified in reporting."** Socket + StepSecurity do not claim TeamPCP, Shai-Hulud-family, or any other tracked-cluster attribution at this disclosure surface. Hard Rule 2 — Archimedes does NOT originate attribution; this raw-signal records "unattributed at disclosure" verbatim.

## Compromise vector hypothesis

Per The Hacker News framing of Socket research:
- **Atiertant** account exhibited "no prior publish history" with the package — consistent with either:
  - **Credential takeover** of an existing maintainer account that then transferred ownership / added atiertant as collaborator
  - **Unauthorized maintainer addition** to the package's publish-permission list (npm's `npm owner add` command)
  - **Account compromise** of atiertant separately followed by malicious-publish

Distinguishing requires npm registry audit-log access that Socket / StepSecurity have not yet published.

## Context: similar to but DISTINCT from Mini Shai-Hulud

Important context for grader's clustering decision:

- **Mini Shai-Hulud** (VT-006, finding-2026-05-12-FLASH-0001): npm + PyPI **self-propagating worm** with SLSA-attestation breaking and OIDC token hijack. TeamPCP-attributed (high confidence per Wiz + StepSecurity).
- **node-ipc 3-version backdoor** (THIS raw-signal): npm-only, 3 specific malicious-version publish events. No worm propagation logic claimed at this disclosure. No SLSA-attestation breaking claim. Unattributed.

The two are **OPERATIONALLY ADJACENT** (developer-credential targeting via npm) but **DISTINCT** in mechanism (worm-propagation vs targeted-publish-event). The grader may consider this for clustering: keep as separate "npm supply-chain credential-theft cluster" (the broader pattern) but DO NOT propagate Mini Shai-Hulud / TeamPCP attribution to this surface absent independent corroboration.

## Anti-noise lockout state

- Mini Shai-Hulud broader-pattern lockout: not active in this evaluation context (this is a different package family with different attribution status)
- Operator may consider treating node-ipc as a parallel-cluster watch surface for future-finding aggregation

## A&D / DIB relevance

**Indirect — dependency-graph reach unknown**:
- node-ipc is a widely-used Node.js IPC library with substantial dependency-graph reach
- Whether @squawk / @uipath / @mistralai / other A&D-prime-relevant packages depend on node-ipc directly or transitively is **unverified at this evaluation time**
- A&D-prime build-pipelines using Node.js IPC tooling may have transitive exposure
- Recommendation for briefer: surface in Supply Chain Watch sector context if active in this brief cycle

## Splunk first-party check

Splunk indexes (archimedes + defenseclaw_local) returned 0 events on a -12h sweep. No first-party telemetry hit on:
- `sh.azurestaticprovider.net` (C2 domain — no DNS resolution logged)
- node-ipc package install events (defenseclaw_local has no live security telemetry currently per source-health.yaml notes)

## Extraction notes

- Language: en
- Article type: media relay of vendor-research-vendor primary
- Raw IOC extraction invoked: yes
- Hard Rule 2 compliance: UNATTRIBUTED preserved verbatim. No first-time attribution origination. Operational adjacency to Mini Shai-Hulud explicitly noted as DISTINCT cluster.
- Hard Rule 3 compliance: no exploit content.
- Hard Rule 4 compliance: no credential values stored; ~90 categories framing recorded, no specific values.
- Hard Rule 7 compliance: 15-word quote limits enforced.

## IOCs (from ioc-extraction skill)

```yaml
attribution_claims:
  - claim_text: "No specific threat actor family identified in reporting"
    claimed_actor: null   # UNATTRIBUTED
    nation_state: unknown
    confidence_term: "unattributed"
    claimant_primary: socket
    claimant_co_primary: stepsecurity
    claimant_relay: thehackernews

malware:
  - family: node-ipc-stealer-backdoor   # researcher-coined / no canonical family name at disclosure
    distribution_method: npm_malicious_publish
    propagation: targeted_version_publish_not_worm
    affected_versions:
      - "9.1.6"
      - "9.2.3"
      - "12.0.1"
    legitimate_last_version_at_disclosure: "<= published before 2024-08"
    exfil_channels: [https_post, dns_txt_record_encoding]
    targeted_credentials_categories_count: 90

domains:
  - sh.azurestaticprovider.net    # C2 — categorize as enrichment target for Shodan / VirusTotal lookup

dns_resolvers_used_for_exfil:
  - 1.1.1.1     # primary (Cloudflare)
  - 8.8.8.8     # fallback (Google)
  # Note: these are infrastructure-resolver-IPs the malware USES, not C2; do not enrich as C2

npm_accounts:
  - account: atiertant
    publish_history: "no prior publish history with node-ipc"
    role: malicious_publisher_attribution_status_undetermined  # credential-takeover vs maintainer-addition vs sock-puppet

packages_affected:
  - registry: npm
    name: node-ipc
    malicious_versions: ["9.1.6", "9.2.3", "12.0.1"]
    legitimate_status_pre_compromise: widely_used_node_ipc_library

source_first_citation_flag:
  vendor: Socket
  vendor_role: originating_primary_research_npm_malicious_version_detection
  in_source_grades_yaml: false
  recommended_provisional_grade: B   # npm-security specialist research vendor; second mention this sweep (also surfaced in PM-004 via researcher-tracking-of-OpenAI-TanStack-fallout)
  rationale: "Tier-2 npm-supply-chain-research specialist with consistent peer-reviewed publication track record; same tier as StepSecurity / SafeDep / Aikido"

related_archimedes_corpus:
  related_findings: [finding-2026-05-12-FLASH-0001]   # Mini Shai-Hulud — operationally adjacent but DISTINCT cluster
  related_vts: [VT-006]
  cluster_disposition: parallel_npm_credential_theft_pattern_DO_NOT_PROPAGATE_TEAMPCP_ATTRIBUTION
```

---

**Source:**
- The Hacker News: https://thehackernews.com/2026/05/stealer-backdoor-found-in-3-node-ipc.html
- Socket research (primary): not directly URL-surfaced in THN summary
- StepSecurity research (co-primary): not directly URL-surfaced in THN summary
