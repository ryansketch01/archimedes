---
raw_id: raw-2026-05-04-0003
collected_at: 2026-05-04T07:52:00-04:00
run_id: pre-brief-20260504-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: bleepingcomputer
  source_name: "BleepingComputer"
  source_url: https://www.bleepingcomputer.com/news/security/backdoored-pytorch-lightning-package-drops-credential-stealer/
  published_at: 2026-05-04T13:15:27-04:00
  corroborating_sources:
    - id: mstic
      note: "Microsoft Threat Intelligence detected; ShaiWorm name from Defender"
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [supply-chain, pypi, ml, ai, credential-stealer, ci-cd]
triage_tags: [non_flash, supply-chain, dev-toolchain, credential-theft, broad-deployment]
iocs_extracted: false
iocs_count: 0
text_word_count: 240
promoted: false
ttl_expires_at: 2026-08-02T07:52:00-04:00
test: false
---

# Backdoored PyTorch Lightning 2.6.3 on PyPI drops 'ShaiWorm' credential stealer

**Package:** pytorch-lightning
**Malicious version:** 2.6.3 (PyPI)
**Distribution method:** Compromise of build/release pipeline (NOT typosquat)
**Reverted to:** 2.6.1 by Lightning AI
**Detection name:** ShaiWorm (Microsoft Defender)

## What sources say

Per BleepingComputer (2026-05-04, citing Microsoft Threat Intelligence): The malicious 2.6.3 release activates on import; downloads JavaScript runtime Bun v1.3.13 from GitHub and executes "an 11.4 MB heavily obfuscated JavaScript payload (`router_runtime.js`)." Stealer scope: `.env` files, API keys, GitHub tokens, browser data (Chrome, Firefox, Brave), AWS / Azure / GCP cloud credentials, and arbitrary command execution.

Per Microsoft (paraphrased in source): detection prevented further infection; "small number of devices" affected per Microsoft telemetry.

No specific file hashes, C2 domains, or IPs disclosed in the BleepingComputer article. Investigation into compromise mechanism still ongoing.

## A&D relevance

Indirect but operationally meaningful:
- PyTorch Lightning is a widely-used ML training framework. A&D primes with ML/AI engineering programs (e.g., autonomy, computer vision, sensor fusion, predictive maintenance) likely have it in their dev-toolchain inventory.
- Stealer targets exactly the credentials that matter on an engineering workstation: `.env`, GitHub tokens, cloud creds. CMMC-scoped environments running ML on classified-adjacent data care about this.

## FLASH evaluation

No triggers match. Non-FLASH; routine supply-chain advisory raw-signal.

## Extraction notes

- Language: en
- Article type: news (BleepingComputer) citing Microsoft research
- Source grade per source-grades.yaml: B (BleepingComputer); A (MSTIC underlying)
- Raw IOC extraction invoked: no — no host indicators (hashes/C2/domains) provided in article
- Quote count from BleepingComputer: 1 (10 words)
