---
raw_id: raw-2026-06-15-pm-007
collected_at: 2026-06-15T15:52:00-04:00
run_id: pre-brief-20260615-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: thehackernews
  source_name: The Hacker News
  source_url: https://thehackernews.com/2026/06/litellm-vulnerability-chain-lets-low.html
  published_at: 2026-06-15T16:39:01+00:00
related_primary:
  - source_yaml_id: null   # Obsidian Security — not yet a corpus source ID
    source_name: Obsidian Security (LiteLLM vuln chain research)
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []   # CVE(s) NOT enumerated in THN snippet; awaiting Obsidian primary direct retrieval
  keywords: [LiteLLM, AI gateway, OpenAI-compatible interface, model provider keys, three-vulnerability chain, low-priv to admin to RCE, Obsidian Security]
triage_tags: [net_new_disclosure, ai_gateway_attack_class, multi-provider-key-blast-radius, NOT_flash_no_active_exploitation_disclosed, secondary-corpus-substrate]
iocs_extracted: true
iocs_count: 0
text_word_count: 220
promoted: true
promoted_to_finding: finding-2026-06-15-0012-thn-obsidian-security-litellm-3-vuln-chain-low-priv-to-admin-to-rce-ai-gateway-substrate-pending-primary-direct-retrieval
promoted_at: 2026-06-15T16:46:00-04:00
ttl_expires_at: 2026-09-13T15:52:00-04:00
---

# LiteLLM Vulnerability Chain Lets Low-Privilege Users Take Over AI Gateway Servers

**The Hacker News** — 2026-06-15 16:39 UTC

A default low-privilege account on a LiteLLM proxy can climb to full admin and run code on
the server by chaining three vulnerabilities, researchers at **Obsidian Security** disclosed.

## Vulnerability overview

- **Product**: LiteLLM (widely deployed open-source AI gateway brokering calls to more than
  100 model providers behind one OpenAI-compatible interface)
- **Chain**: Three vulnerabilities (specific CVE IDs NOT enumerated in THN snippet)
- **Privilege progression**: Low-priv default account → full admin → arbitrary code execution
  on server
- **Blast radius**: A server takeover exposes every provider key it holds (the secrets that)
  govern access to LLM-provider API endpoints downstream

## Research disclosure

- **Researcher**: Obsidian Security (provisional vendor — no prior Archimedes-corpus source ID;
  first-surface candidate for source-grades.yaml provisional B)
- **Article-snippet substrate**: short THN excerpt (220 words estimated visible); full Obsidian
  research write-up NOT directly retrieved this sweep — flag for grader / vuln-tracker on next
  pass

## Patch / vendor coordination status

- NOT disclosed in the THN snippet retrievable to collector this sweep
- Recommend direct retrieval of Obsidian primary research URL for grader/vuln-tracker:
  - CVE IDs (if assigned)
  - CVSS scores
  - LiteLLM affected version range
  - Fixed version (if available)
  - Active exploitation attestation (if any)
  - LiteLLM maintainer coordination + patch availability

---

## Extraction notes

- Language: en
- Publisher byline: The Hacker News (no individual byline visible)
- Primary source: Obsidian Security research
- Article type: vendor-research disclosure
- Raw IOC extraction invoked: yes (no IOCs in retrievable snippet)

## IOCs (from ioc-extraction skill)

```yaml
iocs:
  cves: []   # CVE IDs NOT enumerated in THN snippet — pending Obsidian primary retrieval
  hashes: []
  ips: []
  domains: []
  urls: []

attribution_claims: []
attribution_claims_note: |
  No threat actor attribution; pre-disclosure research class.

source_id_recommendation_for_grader:
  obsidian_security:
    proposed_provisional_grade: B (Tier-2 vendor research first surface per StepSecurity /
      Socket / Sysdig precedent)
    note: |
      First Archimedes-corpus citation via raw-2026-06-15-pm-007. Obsidian Security is an
      identity/SaaS security vendor with prior threat research output. Conservative
      provisional B starting grade per same precedent class as the existing vendor-research
      Tier-2 provisional grades.

ad_relevance_notes_for_grader:
  ad_relevance: medium
  ad_relevance_rationale: |
    LiteLLM is widely deployed as an OSS AI gateway in OSS / enterprise / DIB SDLC pipelines
    that mediate calls to commercial LLM providers (OpenAI / Anthropic / Google / etc).
    Server takeover = exfil of all provider API keys held by the gateway = downstream
    secondary-victim cascade pattern (similar to the OnyxC2 MaaS class in finding-2026-06-11-0010
    or the API-key-aggregator class). A&D-prime defenders running internal LiteLLM gateways
    for AI tooling adoption (notably in CMMC-flow tenants that air-gap commercial LLM access
    behind an internal proxy) should evaluate exposure; standard config-defaults position is
    the binding gate.

anti_noise_disposition: NET_NEW_LOW_PRIORITY
anti_noise_reasoning: |
  Net-new disclosure; not in scope of any existing anti-noise hold. Substrate is THN snippet
  only — pending direct retrieval of Obsidian Security primary research. Suitable for 16:00
  afternoon brief as Other Signal one-liner or AI-attack-class section per briefer discretion;
  upgrade to dedicated finding only on Obsidian primary direct retrieval providing CVE(s) +
  active exploitation attestation + affected/fixed version range.

flash_trigger_evaluation_notes_for_grader:
  trigger_1_critical_cve_exploited: PENDING — no CVE / no ITW attestation visible in THN
    snippet. Awaiting Obsidian primary direct retrieval.
  trigger_6_zero_day_no_patch: PENDING — patch status NOT disclosed in THN snippet.
  flash_disposition: NOT FLASH at this substrate level; revisit if Obsidian primary
    discloses CVE ≥9.0 + active exploitation.
```
