---
raw_id: raw-2026-06-17-am-016-sa-paganini-fulcrumsec-novo-nordisk-clinical-ai-research-data-leak
collected_at: 2026-06-17T07:59:00-04:00
run_id: pre-brief-20260617-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: securityaffairs
  source_name: Security Affairs
  source_url: https://securityaffairs.com/193763/security/fulcrumsec-targets-novo-nordisk-leaks-clinical-and-research-data.html
  published_at: 2026-06-17T08:45:05+00:00
match_reason:
  watchlist: []
  actors: [FulcrumSec]
  vulnerabilities: []
  keywords: [Novo Nordisk, FulcrumSec, Ozempic, Wegovy, clinical trial data, AI model checkpoint, NovoPert, multimodal, biological data, drug discovery]
triage_tags: [out_of_ad_scope_pharma, possible_substrate_pharma_ai_research_pattern, fulcrumsec_carry_forward_anti_noise_dedup_06_00_sweep]
iocs_extracted: false
iocs_count: 0
text_word_count: 320
promoted: false
rejected_at: 2026-06-17T08:26:00-04:00
rejection_id: reject-2026-06-17-0007
ttl_expires_at: 2026-09-15T07:59:00-04:00
---

# FulcrumSec Targets Novo Nordisk, Leaks Clinical and Research Data

**Source:** Security Affairs (https://securityaffairs.com/193763/security/fulcrumsec-targets-novo-nordisk-leaks-clinical-and-research-data.html)
**Author byline:** Pierluigi Paganini
**Published:** 2026-06-17T08:45:05+00:00 (04:45:05 EDT)

## RSS-summary captured

> FulcrumSec leaked data stolen from Novo Nordisk, claiming to have exfiltrated 1.3TB, including clinical records and AI research assets.

## Extraction notes

- **Language:** en
- **Publisher byline:** Pierluigi Paganini (Security Affairs)
- **Article type:** trade-press extortion-disclosure narrative citing Ransomnews + Ransomtracker third-party records
- **Upstream primaries:** FulcrumSec leak-site postings + Novo Nordisk victim notice + Ransomnews analysis + Ransomtracker historical record
- **Carry-forward:** Same FulcrumSec/Novo Nordisk trigger-topic already discarded as out-of-A&D-scope in 2026-06-17 06:00 sweep (per 06:00 sweep notes "Cybercrime Group FulcrumSec Claims Novo Nordisk Hack 1.3TB pharma data exfil SW-Arghire T2-GATE-FAIL FulcrumSec NOT on _roster.yaml T5 FAIL Novo Nordisk pharma sector NOT A&D/DIB/CMMC/ITAR — discarded out-of-scope"). Anti-noise rule 1 in effect.
- **Net-new substrate via SA full-body:** Inventory detail — 16.7 GB multimodal model checkpoint (text + image + transcriptomic); 407 MB proprietary biological/chemical training datasets; 50 MB source code for internal tool "NovoPert"; logs from 113 training runs; HPC infrastructure maps; Slurm scheduler configs; SSH settings; 53 GB internal container images; developer identities; private GitHub URLs. **Pharma AI research substrate** — distinct from clinical-trial data leak.
- **Cross-walk:** FulcrumSec NOT on `_roster.yaml`. Novo Nordisk pharma NOT A&D/DIB/CMMC/ITAR.
- **Possible parallel substrate:** Mandiant direct page #2 "Public and Private Medical Community Targeted by China-Nexus Threat Actor Pursuing AI, Cyber, Medical, and National Defense Research" — UNC6508/INFINITERED targets pharma AI research as adjacent victim profile per finding-2026-06-13 substrate carry-forward. FulcrumSec is cybercriminal extortion (not nation-state); cluster separation preserved per Hard Rule 2.
- **Hard Rule 6 preservation:** 15-word quote discipline preserved.
- **Hard Rule 2 preservation:** FulcrumSec attribution recorded per FulcrumSec self-claim + SA + Ransomnews. NOT cross-walked to UNC6508 despite topical overlap (pharma AI research) — different actor type, different TTPs, different attribution chain.
- **Raw IOC extraction invoked:** no (leak-site URL `fulcrumsec.net` + Tor mirror referenced; specific filenames in inventory list paraphrased not IOC-extracted)

## Substrate observation for grader

T2 FAIL FulcrumSec NOT on roster. T5 FAIL pharma NOT A&D. T1/T3/T4/T6 FAIL no CVE. Critical-override 0-of-4. Non-FLASH-eligible.

Out-of-A&D-scope but pharma AI research theft pattern is operationally analogous to A&D-prime IP exfiltration risk — operational-template inheritance pattern worth tracking. Possible 2026-06-17 morning brief Other Signal one-liner as AI-research-theft cluster signal alongside FulcrumSec EdTech raw-015 + Mandiant UNC6508 medical/military health carry-forward.
