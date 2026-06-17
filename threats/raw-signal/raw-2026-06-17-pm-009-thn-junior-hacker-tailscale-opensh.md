---
raw_id: raw-2026-06-17-pm-009
collected_at: 2026-06-17T15:49:00-04:00
run_id: pre-brief-20260617-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: thehackernews
  source_name: The Hacker News (uncredited byline)
  source_url: https://thehackernews.com/2026/06/junior-hacker-used-tailscale-and.html
  published_at: 2026-06-17T12:00:56-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [Tailscale, OpenSSH, Havoc, C2, keylogger, French, automotive, junior hacker, persistence]
triage_tags: [non_flash, out_of_a&d_scope, low_skill_tradecraft_observation, persistence_pattern_note]
iocs_extracted: true
iocs_count: 0
text_word_count: 250
promoted: false
rejection_id: reject-2026-06-17-0012
rejected_at: 2026-06-17T16:00:00-04:00
ttl_expires_at: 2026-09-15T15:49:00-04:00
---

# Junior Hacker Used Tailscale and OpenSSH to Keep Access After His C2 Went Offline

The Hacker News, 2026-06-17 16:00 UTC.

A French-speaking attacker broke into a small French automotive business, planted a keylogger, and stole banking and email credentials.

Ordinary stuff, until one move near the end.

Before his command-and-control server went dark, he installed OpenSSH and Tailscale on a victim's machine, building a way back in that did not run through the C2 at all. When the Havoc server went offline the next... (article continues — full body not retrieved).

---

## Extraction notes

- Language: en
- Publisher byline: THN uncredited editorial
- Article type: THN summary of (originating researcher not yet identified)
- T-gate evaluation:
  - T1 FAIL no CVE
  - T2 FAIL no roster-tracked actor (junior/uncategorized French-speaking attacker)
  - T3 FAIL no first-party IOC hit anticipated
  - T4 FAIL not a tracked-actor TTP change
  - T5 FAIL no A&D-prime named victim (small French automotive business)
  - T6 FAIL no CVE
- Critical override 0-of-4
- Out-of-scope SMB commodity intrusion
- Operational template observation worth carrying forward: Tailscale + OpenSSH as low-skill persistence pattern (when C2 dies, attacker keeps remote access via legitimate tunneling). Possible future relevance to A&D defenders monitoring for unauthorized Tailscale enrollment. Non-FLASH-eligible this window.
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
    - actor: "French-speaking junior attacker (uncategorized)"
      source: THN
  ttp_observations:
    - "Havoc C2 framework"
    - "OpenSSH + Tailscale post-C2-death persistence pattern"
    - "Keylogger for credential capture"
```
