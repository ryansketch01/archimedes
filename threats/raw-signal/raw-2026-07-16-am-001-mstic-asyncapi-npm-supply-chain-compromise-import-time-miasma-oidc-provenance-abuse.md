---
raw_id: raw-2026-07-16-am-001
collected_at: 2026-07-16T07:33:00-04:00
run_id: pre-brief-20260716-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: mstic
  source_name: Microsoft Security Blog / Microsoft Threat Intelligence (MSTIC)
  source_url: https://www.microsoft.com/en-us/security/blog/2026/07/15/unpacking-asyncapi-npm-supply-chain-compromise-import-time-payload-delivery/
  published_at: 2026-07-16T01:36:21+00:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [npm, supply-chain, CI/CD, OIDC, provenance, GitHub Actions, import-time, Miasma]
  thematic_link: "npm/CI-CD supply-chain compromise class — sibling to tracked VT-006 (Mini Shai-Hulud, OIDC token hijack + SLSA/provenance abuse) and VT-009 (Nx Console). Structural A&D SDLC-exposure concern per VT-006 @squawk analysis."
triage_tags: [supply_chain, npm, ci_cd_compromise, a_grade_vendor, live_c2, unattributed, non_flash]
iocs_extracted: true
iocs_count: 9
text_word_count: 780
promoted: true
promoted_to_finding: finding-2026-07-16-0001
promoted_at: 2026-07-16T08:12:00-04:00
grading_run_id: morning-20260716-080000
digraph: A2
wep_ceiling: likely
ttl_expires_at: 2026-10-14T07:33:00-04:00
---

# Unpacking the AsyncAPI npm supply chain compromise and import-time payload delivery

**Source:** Microsoft Threat Intelligence (MSTIC) — Microsoft Security Blog, published 2026-07-16T01:36 UTC.
Authors: Microsoft Security Research, Ravikant Tiwari, Sagar Patil, Suriyaraj Natarajan, Arvind Gowda.

On July 14, 2026, Microsoft Threat Intelligence identified a coordinated supply-chain
compromise of the `@asyncapi` npm organization (packages for the AsyncAPI specification
and code generation). Five package versions across four package names were republished
within ~90 minutes, each carrying the same maliciously injected loader:

- `@asyncapi/specs` — `6.11.2-alpha.1` (prerelease) and `6.11.2` (stable)
- `@asyncapi/generator@3.3.1`
- `@asyncapi/generator-components@0.7.1`
- `@asyncapi/generator-helpers@1.1.1`

Because `@asyncapi/specs` is a transitive dependency of numerous AsyncAPI tooling
packages, the compromise reached developer workstations, CI/CD pipelines, container
builds, and production services that resolved and imported the affected versions during
the exposure window.

**Key novel/notable mechanics (recorded verbatim from source; not Archimedes-assessed):**

- **Import-time (module-load) execution**, NOT the common postinstall-hook pattern. The
  injected block runs on `require()`/`import`, so `npm install --ignore-scripts` does NOT
  neutralize it.
- **OIDC + valid provenance abuse:** origin was a "pwn request" against
  `asyncapi/generator` — a misconfigured GitHub Actions workflow (`pull_request_target`)
  executed attacker-controlled PR code, exposed the `asyncapi-bot` personal access token
  (PAT), and enabled unauthorized pushes to auto-publish branches. Legitimate GitHub
  Actions OIDC release workflows then published the poisoned packages under the automated
  identity `npm-oidc-no-reply@github.com`, producing artifacts **with valid provenance
  signatures built from unauthorized source commits.**
- **Second stage — "Miasma" modular runtime:** decrypts/evaluates with active C2,
  persistence, and decentralized fallback channels (Nostr, Ethereum, BitTorrent DHT,
  libp2p, IPFS). Six additional capability modules (credential harvest, encrypted exfil,
  supply-chain propagation, metamorphic generation, AI-tool poisoning, sandbox evasion)
  were implemented but **disabled** in this build.
- **IPFS second-stage fetch:** child process downloads `sync.js` from IPFS and writes it
  to an OS-specific "NodeJS" masquerade directory.

**Microsoft-published detections / mitigations (verbatim):** Defender AV detects as
`Trojan:JS/MiasmStealer.SC` and `Trojan:Script/Supychain.A`. Guidance: remove all five
affected versions, purge npm and Yarn caches, hunt for `sync.js` under NodeJS masquerade
directories, block outbound to `85.137.53[.]71` on ports 8080/8081/8091, rotate all
credentials accessible from any environment that imported the compromised packages.

**Timeline (UTC, per source):** ~07:10 generator trio republished; 08:06:20
`@asyncapi/specs@6.11.2-alpha.1`; 08:30:09 `@asyncapi/specs@6.11.2` stable (byte-identical
payload); 08:49:22 first observed downstream fetch of the stable tarball into a Yarn cache.

**Attribution:** None. Source does not name a threat actor. (Hard Rule 2 — no origination.)

---

## Extraction notes

- Language: en
- Publisher byline: Microsoft Security Research et al. (MSTIC)
- Article type: vendor threat-intel blog (A-grade source: mstic, grade A)
- Raw IOC extraction invoked: yes
- Collector note: No credentials stored. The `asyncapi-bot` PAT and any harvested
  credentials are referenced as compromised-artifact *context* only (Hard Rule 7 — value
  not present in source excerpt, none stored). No PoC/exploit content copied (Hard Rule 3).
- Thematic clustering hint for grader: this is the third distinct npm/CI-CD supply-chain
  surface in the corpus lineage (VT-006 Mini Shai-Hulud / TeamPCP; VT-009 Nx Console) and
  co-occurs this window with a Unit 42 npm threat-landscape update (raw-2026-07-16-am-003).
  Mechanism differs from Mini Shai-Hulud (import-time vs worm self-propagation; Miasma vs
  TeamPCP tooling; distinct C2). No attribution overlap asserted.

## IOCs (from ioc-extraction skill)

```yaml
extraction_metadata:
  source_brief_id: raw-2026-07-16-am-001
  source_url: https://www.microsoft.com/en-us/security/blog/2026/07/15/unpacking-asyncapi-npm-supply-chain-compromise-import-time-payload-delivery/
  extracted_at: 2026-07-16T11:33:00Z
  extracted_by: collector
  target_actor_id: null
  text_word_count: 780

indicators:
  - id: raw-ipv4-85-137-53-71
    type: ipv4
    value: 85.137.53.71
    defanged_original: "85.137.53[.]71"
    first_seen: 2026-07
    last_seen: 2026-07
    role: c2
    campaign: "AsyncAPI npm supply-chain compromise (2026-07-14)"
    related_malware: [Miasma]
    source_brief: raw-2026-07-16-am-001
    context_excerpt: >
      "block outbound connections to 85.137.53[.]71 on ports 8080, 8081, and 8091" —
      named C2 endpoint of the Miasma second-stage runtime.
    attribution_in_text: null
    notes: "C2 on ports 8080/8081/8091."
  - id: raw-file_path-sync-js-nodejs-masquerade
    type: file_path
    value: "sync.js (under OS-specific 'NodeJS' masquerade directory)"
    defanged_original: null
    first_seen: 2026-07
    last_seen: 2026-07
    role: staging
    campaign: "AsyncAPI npm supply-chain compromise (2026-07-14)"
    related_malware: [Miasma]
    source_brief: raw-2026-07-16-am-001
    context_excerpt: "child downloaded sync.js from IPFS and wrote it to an OS-specific 'NodeJS' masquerade directory."
    attribution_in_text: null
    notes: "Exact per-OS path not enumerated in source excerpt; hunt hint."
  - id: raw-email-npm-oidc-no-reply-github
    type: email
    value: npm-oidc-no-reply@github.com
    defanged_original: "npm-oidc-no-reply@github[.]com"
    first_seen: 2026-07
    last_seen: 2026-07
    role: ambiguous
    campaign: "AsyncAPI npm supply-chain compromise (2026-07-14)"
    related_malware: []
    source_brief: raw-2026-07-16-am-001
    context_excerpt: >
      "published the poisoned packages under the automated identity npm-oidc-no-reply@github[.]com,
      producing artifacts with valid provenance signatures" — legitimate GitHub OIDC publish
      identity ABUSED, not attacker-owned. Not a blocklist indicator; provenance-context only.
    attribution_in_text: null
    notes: "Legitimate identity abused via OIDC release workflow; do not naively blocklist."
  - id: raw-yara-trojan-js-miasmstealer-sc
    type: yara_rule
    value: "Trojan:JS/MiasmStealer.SC"
    defanged_original: null
    first_seen: 2026-07
    last_seen: 2026-07
    role: ambiguous
    campaign: "AsyncAPI npm supply-chain compromise (2026-07-14)"
    related_malware: [Miasma]
    source_brief: raw-2026-07-16-am-001
    context_excerpt: "Microsoft Defender Antivirus detects and blocks malicious artifacts as Trojan:JS/MiasmStealer.SC"
    attribution_in_text: null
    notes: "Vendor (Defender) detection name, not a YARA rule per se; recorded as detection signature."
  - id: raw-yara-trojan-script-supychain-a
    type: yara_rule
    value: "Trojan:Script/Supychain.A"
    defanged_original: null
    first_seen: 2026-07
    last_seen: 2026-07
    role: ambiguous
    campaign: "AsyncAPI npm supply-chain compromise (2026-07-14)"
    related_malware: [Miasma]
    source_brief: raw-2026-07-16-am-001
    context_excerpt: "detects and blocks malicious artifacts as ... Trojan:Script/Supychain.A"
    attribution_in_text: null
    notes: "Vendor (Defender) detection name."
  - id: raw-other-pkg-asyncapi-specs-6-11-2
    type: other
    type_detail: npm_package_version
    value: "@asyncapi/specs@6.11.2 (and 6.11.2-alpha.1)"
    defanged_original: null
    first_seen: 2026-07
    last_seen: 2026-07
    role: delivery
    campaign: "AsyncAPI npm supply-chain compromise (2026-07-14)"
    related_malware: [Miasma]
    source_brief: raw-2026-07-16-am-001
    context_excerpt: "Five package versions across four package names were republished ... each carrying the same maliciously injected loader."
    attribution_in_text: null
    notes: "Compromised package version — remediation target."
  - id: raw-other-pkg-asyncapi-generator-3-3-1
    type: other
    type_detail: npm_package_version
    value: "@asyncapi/generator@3.3.1"
    defanged_original: null
    first_seen: 2026-07
    last_seen: 2026-07
    role: delivery
    campaign: "AsyncAPI npm supply-chain compromise (2026-07-14)"
    related_malware: [Miasma]
    source_brief: raw-2026-07-16-am-001
    context_excerpt: "@asyncapi/generator@3.3.1 ... republished with the injected loader."
    attribution_in_text: null
    notes: "Compromised package version."
  - id: raw-other-pkg-asyncapi-generator-components-0-7-1
    type: other
    type_detail: npm_package_version
    value: "@asyncapi/generator-components@0.7.1"
    defanged_original: null
    first_seen: 2026-07
    last_seen: 2026-07
    role: delivery
    campaign: "AsyncAPI npm supply-chain compromise (2026-07-14)"
    related_malware: [Miasma]
    source_brief: raw-2026-07-16-am-001
    context_excerpt: "@asyncapi/generator-components@0.7.1 ... republished with the injected loader."
    attribution_in_text: null
    notes: "Compromised package version."
  - id: raw-other-pkg-asyncapi-generator-helpers-1-1-1
    type: other
    type_detail: npm_package_version
    value: "@asyncapi/generator-helpers@1.1.1"
    defanged_original: null
    first_seen: 2026-07
    last_seen: 2026-07
    role: delivery
    campaign: "AsyncAPI npm supply-chain compromise (2026-07-14)"
    related_malware: [Miasma]
    source_brief: raw-2026-07-16-am-001
    context_excerpt: "@asyncapi/generator-helpers@1.1.1 ... republished with the injected loader."
    attribution_in_text: null
    notes: "Compromised package version."

attribution_claims: []

benign_filtered:
  - value: microsoft.com
    reason: reference_site_publisher
  - value: github.com
    reason: reference_site
  - value: "IPFS / Nostr / Ethereum / BitTorrent DHT / libp2p"
    reason: decentralized_transport_infrastructure_named_generically_not_atomic_indicator

extraction_warnings:
  - type: ambiguous_role
    ioc_id: raw-email-npm-oidc-no-reply-github
    detail: "Legitimate GitHub OIDC publish identity abused, not attacker-owned — do not blocklist; provenance/context indicator only."
  - type: detection_name_not_yara
    ioc_id: raw-yara-trojan-js-miasmstealer-sc
    detail: "Defender detection names recorded under yara_rule tag for lack of a detection-signature schema type; grader/actor-profiler should reclassify if a dedicated type exists."
```
