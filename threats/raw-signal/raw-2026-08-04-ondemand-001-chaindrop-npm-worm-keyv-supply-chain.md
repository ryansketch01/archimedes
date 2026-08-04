---
raw_id: raw-2026-08-04-ondemand-001
collected_at: 2026-08-04T14:02:00-04:00
run_id: ondemand-investigate-20260804-140000
collection_mode: on_demand
sentinel: false
source:
  primary_sources:
    - source_yaml_id: semgrep
      source_name: "Semgrep (named the campaign 'ChainDrop')"
      source_url: "https://semgrep.dev/blog/2026/its-not-npm-ver-yet-npm-worm-chaindrop-hits-400-packages-including-jaredwray-servicetitan-ornikar-qlik-and-nebulajs/"
      published_at: 2026-08-04
      retrieval: search_summary_only        # direct WebFetch returned HTTP 403; retrieved via WebSearch summarizer
    - source_yaml_id: stepsecurity
      source_name: "StepSecurity — 'ChainDrop npm Worm: Bun-loaded CI/CD credential harvester with Ethereum dead-drop C2'"
      source_url: "https://www.stepsecurity.io/blog/chaindrop-npm-worm"
      published_at: 2026-08-04
      retrieval: search_summary_only        # HTTP 403 on direct fetch
    - source_yaml_id: wiz-research
      source_name: "Wiz Research — keyv/cacheable npm supply-chain attack (observed Bun/1.3.13 UA)"
      source_url: "https://www.wiz.io/blog/keyv-and-cacheable-npm-supply-chain-attack"
      published_at: 2026-08-04
      retrieval: search_summary_only        # HTTP 403 on direct fetch
    - source_yaml_id: socket
      source_name: "Socket — 'Massive npm Malware Campaign Leverages Ethereum Smart Contracts'"
      source_url: "https://socket.dev/blog/massive-npm-malware-campaign-leverages-ethereum-smart-contracts"
      published_at: 2026-08-04
      retrieval: search_summary_only
    - source_yaml_id: reversinglabs
      source_name: "ReversingLabs — 'Ethereum smart contracts used to push malicious code on npm'"
      source_url: "https://www.reversinglabs.com/blog/ethereum-contracts-malicious-code"
      published_at: 2026-08-04
      retrieval: search_summary_only        # not in source-grades.yaml; B-class vendor
    - source_yaml_id: safedep
      source_name: "SafeDep — expanded count (1,684 versions / 420 names / 9 orgs)"
      source_url: null
      published_at: 2026-08-04
      retrieval: search_summary_only
    - source_yaml_id: thehackernews
      source_name: "The Hacker News — 'Keyv-Linked npm Worm Poisons Hundreds of Packages, Plants Claude Code and VS Code Hooks'"
      source_url: "https://thehackernews.com/2026/08/keyv-linked-npm-worm-poisons-hundreds.html"
      published_at: 2026-08-04
      retrieval: search_summary_only        # HTTP 403 on direct fetch
match_reason:
  watchlist: [software_supply_chain, npm_ecosystem, ci_cd_pipeline]
  actors: []                                # no named attribution in any source (Hard Rule 2)
  vulnerabilities: []                        # no CVE; access via credential/token hijack, not a software flaw
  keywords: [chaindrop, npm, worm, supply-chain, keyv, preinstall, bun, ethereum-c2, credential-harvest]
triage_tags: [supply_chain, npm_worm, ci_cd_credential_theft, blockchain_c2, active, on_demand]
iocs_extracted: true
iocs_count: 6
text_word_count: 620
retrieval_caveat: >
  ALL primary-source direct fetches returned HTTP 403 this cycle (Semgrep, StepSecurity, Wiz, The Hacker News).
  Content captured via the WebSearch summarizer's paraphrase of those primaries — evidentiary quality is
  relay-equivalent, not direct-primary. First-party enrichment unavailable: splunk-query, virustotal, and
  urlscan MCP servers did not connect this session.
promoted: true
promoted_to: finding-2026-08-04-0001
ttl_expires_at: 2026-11-02T14:02:00-04:00
---

# On-demand collection: ChainDrop self-propagating npm worm (2026-08-04)

Operator query: "What can you find on ChainDrop." On-demand `/investigate`-class collection sweep, 2026-08-04 ~14:00 EDT.

## What was collected

A self-propagating npm worm that security vendors are calling **ChainDrop** (Semgrep's name) broke out the morning of **2026-08-04**. Multiple independent vendors (Semgrep, StepSecurity, Wiz, Socket, ReversingLabs, SafeDep) plus a Hacker News relay report the same campaign, corroborating on directly-observable artifacts (packages on the npm registry, a contract on the Ethereum mainnet).

- **Patient zero:** `keyv@6.0.0`, published 2026-08-04 09:35:00Z.
- **Scale:** Semgrep — 435 packages / 1,557 poisoned versions in a ~2h burst (09:40–11:44 UTC). SafeDep — 1,684 versions / 420 names / 9 orgs (higher, still-moving count).
- **Named affected scopes:** keyv, cacheable, jaredwray, servicetitan, ornikar, qlik, nebula.js.
- **Mechanism:** obfuscated loaders (`setup.mjs`, `math_init.js`) wired into the npm `preinstall` lifecycle hook → runs at install/dependency-resolution, not at import. Loader pulls the Bun runtime and executes an obfuscated second stage (Wiz observed user-agent `Bun/1.3.13`).
- **Propagation:** harvests npm tokens; each successful harvest supplies publish rights for the next wave (worm behavior).
- **Credential targets:** npm tokens, GitHub Actions secrets/tokens, cloud creds (AWS IMDS/ECS, HashiCorp Vault, Kubernetes), SSH private keys, CI secrets. Also reported planting Claude Code and VS Code hooks (persistence).
- **C2:** Ethereum-mainnet dead-drop smart contract; on-chain config initially returned 3 domains, later reduced to `npm-cache[.]com`.

## IOCs (extracted; see finding for schema)

- ETH contract (C2 dead-drop): `0xa1b40044EBc2794f207D45143Bd82a1B86156c6b`
- ETH wallet: `0x52221c293a21D8CA7AFD01Ac6bFAC7175D590A84`
- C2 domain: `npm-cache[.]com`
- Loader files: `setup.mjs`, `math_init.js`
- User-agent: `Bun/1.3.13`
- Malicious `preinstall` lifecycle hook

## Handoff

Promoted to `finding-2026-08-04-0001`. No attribution in any source (Hard Rule 2 — none originated). No CVE (VT/vuln-tracker not warranted). First-party sweep deferred: splunk-query MCP unavailable this session — flag `/ioc-hunt npm-cache[.]com` + Splunk search for `Bun/1.3.13` UA and `preinstall`-triggered execution when tooling reconnects.
