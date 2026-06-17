---
raw_id: raw-2026-06-17-pm-015
collected_at: 2026-06-17T15:54:00-04:00
run_id: pre-brief-20260617-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: eset
  source_name: ESET / WeLiveSecurity
  source_url: https://www.welivesecurity.com/en/eset-research/fishmongers-arsenal-upgraded-sprysocks-windows/
  published_at: 2026-06-16T04:54:04-04:00
match_reason:
  watchlist: []
  actors: [FishMonger]
  vulnerabilities: []
  keywords: [FishMonger, SprySOCKS, Windows, kernel driver, ESET research, backdoor, stealthiness]
triage_tags: [eset_primary_direct_url_substantiation, watch_item, substrate_strengthening_indirect, fishmonger_cluster_carry_forward]
iocs_extracted: true
iocs_count: 0
text_word_count: 100
promoted: false
rejection_id: reject-2026-06-17-0018
rejected_at: 2026-06-17T16:00:00-04:00
ttl_expires_at: 2026-09-15T15:54:00-04:00
---

# FishMonger's arsenal upgraded: SprySOCKS for Windows

ESET / WeLiveSecurity, 2026-06-16 08:54 UTC.

ESET researchers have discovered SprySOCKS for Windows, FishMonger's backdoor weaponizing a kernel driver for advanced stealthiness.

(RSS summary only — direct ESET primary URL now in feed. Full body retrieval already absorbed via SA-Paganini quintuple-publisher relay in AM brief 56cf187 / finding-2026-06-17-0004.)

---

## Extraction notes

- Language: en
- Publisher byline: ESET research team
- Article type: ESET WeLiveSecurity primary publication
- Substrate context: This is the ESET PRIMARY URL surface direct in feed. Already absorbed via finding-2026-06-17-0004 substrate-strengthening UPDATE in 2026-06-17 AM brief 56cf187 (SA-Paganini full-body retrieval lifted publisher cardinality to quintuple BC+THN+DR+SA+ESET-primary publisher-independence). 
- This RSS item-in-feed surface adds NO net-new substrate — confirms feed delivery of ESET primary URL.
- Single-vendor-on-cluster-identity veto persists: Mandiant / CrowdStrike / Unit 42 / MSTIC corroboration of FishMonger = i-Soon-contractor cluster identity remains the substrate-that-would-lift-veto.
- Raw IOC extraction invoked: no (already extracted via finding-2026-06-17-0004 substrate via prior cycle SA-Paganini retrieval; no net-new IOCs in this RSS item summary)

## IOCs (from ioc-extraction skill)

```yaml
extracted_iocs:
  ipv4: []
  ipv6: []
  domains: []
  urls: []
  hashes: []
  email_addresses: []
  attribution_claims:
    - actor: FishMonger
      cluster_identity_layer: "single-vendor-on-cluster-identity veto persists per finding-2026-06-17-0004"
      source: ESET research direct primary
```
