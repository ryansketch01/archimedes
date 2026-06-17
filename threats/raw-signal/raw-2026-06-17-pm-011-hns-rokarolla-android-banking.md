---
raw_id: raw-2026-06-17-pm-011
collected_at: 2026-06-17T15:50:00-04:00
run_id: pre-brief-20260617-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: helpnetsecurity
  source_name: Help Net Security (Sinisa Markovic)
  source_url: https://www.helpnetsecurity.com/2026/06/17/rokarolla-android-banking-trojan-device-takeover/
  published_at: 2026-06-17T09:23:46-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [Rokarolla, Android banking trojan, Zimperium, 217 apps, 137 commands, TikTok impersonation, Google Chrome impersonation]
triage_tags: [non_flash, out_of_a&d_scope, consumer_android_mobile_banking]
iocs_extracted: true
iocs_count: 0
text_word_count: 200
promoted: false
rejection_id: reject-2026-06-17-0014
rejected_at: 2026-06-17T16:00:00-04:00
ttl_expires_at: 2026-09-15T15:50:00-04:00
---

# Rokarolla Android trojan targets banking and crypto users, enables device takeover

Help Net Security, Sinisa Markovic, 2026-06-17 13:23 UTC.

A newly discovered Android banking trojan, dubbed Rokarolla, targets 217 banking and cryptocurrency applications and can execute 137 commands on infected devices, according to researchers at Zimperium. Named after its command-and-control (C2) infrastructure, Rokarolla is primarily distributed through malicious websites that impersonate popular applications such as TikTok and Google Chrome.

---

## Extraction notes

- Language: en
- Publisher byline: Sinisa Markovic (HNS), B-grade
- Article type: HNS relay of Zimperium zLabs research primary
- T-gates: T5 FAIL — consumer Android banking trojan NOT A&D/DIB/CMMC/ITAR. T1/T6 FAIL no CVE. T2/T4 FAIL no tracked-actor. T3 FAIL no first-party IOC anticipated.
- Out-of-scope consumer-mobile
- Anti-noise context: same general consumer-Android-banking pattern previously evaluated multiple sweeps. Anti-noise dedup applies.
- Raw IOC extraction invoked: yes

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
    - actor: "unattributed (operator-coined Rokarolla)"
      source: Zimperium via HNS
```
