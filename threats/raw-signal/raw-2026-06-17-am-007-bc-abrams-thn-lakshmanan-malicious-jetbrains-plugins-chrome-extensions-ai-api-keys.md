---
raw_id: raw-2026-06-17-am-007-bc-abrams-thn-lakshmanan-malicious-jetbrains-plugins-chrome-extensions-ai-api-keys
collected_at: 2026-06-17T07:46:00-04:00
run_id: pre-brief-20260617-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: bleepingcomputer
  source_name: BleepingComputer
  source_url: https://www.bleepingcomputer.com/news/security/malicious-jetbrains-marketplace-plugins-steal-ai-api-keys-from-developers/
  published_at: 2026-06-16T21:54:50+00:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [JetBrains, plugins, marketplace, AI API key theft, CodeGPT, DeepSeek, Chrome extensions, Smart Adblocker, Aikido Security, PromptSnatcher]
triage_tags: [carry_forward_06_00_sweep, possible_other_signal, ai_api_key_theft_cluster, ai_dev_supply_chain_pattern_twin, no_tracked_actor]
iocs_extracted: false
iocs_count: 0
text_word_count: 250
promoted: false
rejected_at: 2026-06-17T08:22:00-04:00
rejection_id: reject-2026-06-17-0003
ttl_expires_at: 2026-09-15T07:46:00-04:00
---

# Malicious JetBrains Marketplace plugins steal AI API keys from developers

**Primary capture (BleepingComputer):**
**Source:** BleepingComputer (https://www.bleepingcomputer.com/news/security/malicious-jetbrains-marketplace-plugins-steal-ai-api-keys-from-developers/)
**Author byline:** Lawrence Abrams
**Published:** 2026-06-16T21:54:50+00:00 (17:54:50 EDT)

**Co-publisher (The Hacker News):**
**Source:** The Hacker News (https://thehackernews.com/2026/06/malicious-jetbrains-plugins-steal-ai.html)
**Author byline:** Ravie Lakshmanan
**Published:** 2026-06-17T09:38:46+00:00 (05:38:46 EDT)

## RSS-summary captured (BC)

> At least 15 malicious plugins found on the JetBrains Marketplace were designed to steal AI API keys from developers.

## RSS-summary captured (THN)

> Cybersecurity researchers have flagged a "coordinated malware campaign" on the JetBrains Marketplace that has published no less than 15 malicious plugins capable of exfiltrating artificial intelligence (AI) provider keys.

## Extraction notes

- **Language:** en
- **Publisher byline:** Lawrence Abrams (BC) + Ravie Lakshmanan (THN)
- **Article type:** trade-press journalistic relay of Aikido Security IR research (Makari named researcher per 06:00 sweep notes)
- **Upstream primary:** Aikido Security (provisional C since 2026-05-12 per source-grades.yaml)
- **Scope per 06:00 sweep notes:** 15 JetBrains plugins (CodeGPT AI Assistant + DeepSeek AI Assist >25K downloads each among them) + 2 Chrome extensions (PromptSnatcher campaign; Smart Adblocker 90K users) — exfiltrate API keys from OpenAI, SiliconFlow, DeepSeek, Claude, Gemini, Copilot, Perplexity, Grok, Meta AI
- **Cross-walk:** Same trigger-topic carry-forward from 2026-06-17 06:00 sweep. Twin pattern with Mastra npm supply-chain (raw-2026-06-17-am-006) — AI-dev-supply-chain cluster.
- **A&D-relevance:** LOW (commodity AI-dev-supply-chain operational-template pattern). No A&D-prime named victim.
- **Hard Rule 6 preservation:** 15-word quote discipline preserved.
- **Hard Rule 2 preservation:** No tracked-actor attribution. "Coordinated malware campaign" researcher-coined working framing.
- **Raw IOC extraction invoked:** no (no specific IOCs in trade-press relay; specific plugin names + extension IDs at Aikido Security upstream primary)

## Substrate observation for grader

Carry-forward from 06:00 sweep. T1/T6 FAIL (no CVE). T2/T4 FAIL (no tracked-actor attribution). T5 FAIL (no A&D-prime named victim). Critical-override 0-of-4.

Possible 2026-06-17 morning brief Other Signal one-liner cluster with Mastra npm finding (raw-006). Twin AI-dev-supply-chain surface — operational-template inheritance pattern via A&D-prime AI-development teams. Developer-marketplace-supply-chain pattern recurrence.
