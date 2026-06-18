---
raw_id: raw-2026-06-18-pm-009-krebs-popa-botnet-netnut-alarum-vo1d-badbox-residential-proxy
collected_at: 2026-06-18T15:52:00-04:00
run_id: pre-brief-20260618-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: krebs
  source_name: Krebs on Security
  source_url: https://krebsonsecurity.com/2026/06/popa-botnet-linked-to-publicly-traded-israeli-firm/
  published_at: 2026-06-18T17:37:58+00:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [Popa botnet, Vo1d, BadBox 2.0, NetNut, Alarum Technologies, residential proxy, Ninjatech, HUMAN Security, Qurium, XLAB]
triage_tags: [non_a_d_consumer_iot, residential_proxy_research, supply_chain_pattern_watch, krebs_investigative_journalism, multi_vendor_corroboration]
iocs_extracted: true
iocs_count: 4
test: false
promoted: false
rejected_at: 2026-06-18T16:19:00-04:00
rejection_id: reject-2026-06-18-0015
ttl_expires_at: 2026-09-16T15:52:00-04:00
---

# 'Popa' Botnet Linked to Publicly-Traded Israeli Firm

## Source metadata

- **Publisher:** Krebs on Security
- **Author:** Brian Krebs
- **Publication timestamp:** 2026-06-18T17:37:58+00:00 (13:37 EDT, inside the post-12:00-FLASH-sweep window)
- **URL:** https://krebsonsecurity.com/2026/06/popa-botnet-linked-to-publicly-traded-israeli-firm/
- **Source grade:** A (Krebs baseline per source-grades.yaml)

## Summary

Krebs investigative reporting on the Popa botnet — sprawling Android-based residential proxy network forcing millions of consumer TV boxes to relay traffic for advertising fraud, account takeovers, and mass data-scraping. Multiple security vendors converge on attribution: Popa is linked to NetNut (residential proxy provider) operated by publicly-traded Israeli firm Alarum Technologies Ltd [NASDAQ: ALAR]. Popa is described as a plugin component of the Vo1d botnet (large-scale malware campaign on unofficial Android TV boxes).

## Multi-vendor corroboration (verbatim attribution surface)

> "researchers from multiple security firms concluded that the Popa botnet is linked to NetNut, a 'residential proxy' provider operated by the publicly-traded Israeli firm Alarum Technologies Ltd [NASDAQ: ALAR]"

Named research vendors corroborating:
- **XLAB** (Chinese security company) — 2025 report flagging at least nine domain names registered to control Popa
- **Qurium** (this 2026-06-18 publication) — 1.4M IP-distributed scraping event observation + several dozen domains traced (gmslb[.]net, safernetwork[.]io, tera-home[.]com, ninjatech[.]io)
- **HUMAN Security** — Badbox 2.0 disruption coordination (Google + Trend Micro joint)
- **Trend Micro** — Badbox 2.0 disruption participation
- **Lumen Technologies / Black Lotus Labs** — referenced in category tags
- **Spur** — referenced in category tags
- **Synthient** — referenced in category tags
- **Include Security** — referenced in category tags

## Attribution

NetNut (residential proxy provider) → Alarum Technologies Ltd [NASDAQ: ALAR] (publicly-traded Israeli firm). Ninjatech (founded by Moishi Kramer, VP R&D at NetNut). Kramer's emailed response denies operation of current Popa infrastructure.

**Not on `_roster.yaml`** — Popa botnet operators / NetNut / Alarum NOT tracked as APT or cybercriminal cluster on Archimedes roster. Vo1d / BadBox 2.0 background also NOT roster-tracked.

## IOCs (incremental, from Krebs reporting via Qurium)

```yaml
iocs:
  domains:
    - value: "gmslb.net"
      context: "Popa control domain, used across pirated/modded streaming apps (CRICFy, DooFlix, Sprozfy, RTS Tv, Flixoid, CyberFlix, Rapid Streamz, TvMob, HD/OceanStreams)"
      defanged: "gmslb[.]net"
    - value: "safernetwork.io"
      context: "Popa control domain"
      defanged: "safernetwork[.]io"
    - value: "tera-home.com"
      context: "Popa control domain"
      defanged: "tera-home[.]com"
    - value: "ninjatech.io"
      context: "Popa control domain (referenced post-Badbox-2.0-July-2025-disruption); founded by Moishi Kramer (NetNut VP R&D); Kramer denies operating current infrastructure"
      defanged: "ninjatech[.]io"

attribution_claims:
  - actor: "Popa botnet operators (linked to NetNut / Alarum Technologies Ltd [NASDAQ: ALAR] per multi-vendor research)"
    actor_status: not_on_roster
    confidence_phrase: "researchers from multiple security firms concluded"
    asserted_by: Brian Krebs (KrebsOnSecurity) consolidating Qurium + XLAB + HUMAN Security + Trend Micro
    cross_walk_to_roster: NONE — Hard Rule 2 BINDING; Popa/Vo1d/BadBox 2.0 are commodity residential-proxy / consumer-IoT supply-chain pattern, not tracked APT or cybercriminal cluster
  
  - vendor_response: "Moishi Kramer denies Ninjatech operates current Popa infrastructure; states code was sold/licensed 5 years ago"
    quote_verbatim: "That code was sold and licensed to third parties including resellers years ago"
    asserted_by: Moishi Kramer (Ninjatech founder, NetNut VP R&D) via email to Krebs
```

## A&D relevance

**Out-of-scope.** Consumer Android TV boxes = consumer IoT supply-chain compromise; victims are device-owners not enterprise networks. Residential-proxy abuse is ad-fraud + account-takeover + data-scraping — not A&D-prime intrusion vector.

**However, two structural observations are watch-pattern relevant:**

1. **Consumer-IoT supply-chain compromise pattern** — devices arriving pre-compromised at scale, bundled malware in distribution channels. Parallel to BRICKSTORM vSphere-targeting + Mandiant supply-chain compromise patterns that ARE A&D-relevant. Pattern observation only; no A&D-direct substrate.
2. **Residential-proxy infrastructure** as obfuscation layer for APT operations — consistent with UNC6508 OBF-network tradecraft (compromised routers + residential proxies + VPS per Mandiant primary). Popa/Vo1d-class residential-proxy infrastructure is the kind of OBF-network commodity infrastructure that APT actors lease for operational anonymity. This is methodologically interesting but does NOT directly tie Popa to any tracked-actor operations — no Archimedes-originated cross-walk attempted.

## FLASH-trigger evaluation

- T1/T6 FAIL: no CVE
- T2/T4 FAIL: no tracked-roster-actor
- T5 FAIL: no A&D-prime named victim; consumer-IoT target class
- Critical-override 0-of-4

**Discarded as non-FLASH-eligible.** Substrate-strengthening watch-pattern observation only on consumer-IoT supply-chain compromise + residential-proxy obfuscation infrastructure.

## WEP framing for grader

- Popa botnet existence and scale → **very likely** (Krebs investigative reporting + multi-vendor corroboration: XLAB + Qurium + HUMAN + Trend Micro)
- NetNut/Alarum link to Popa → **likely** (multi-vendor research conclusion + Krebs reporting; Alarum/NetNut denial counter-balanced)
- A&D-DIB direct targeting → **very unlikely** (consumer IoT TV box target class)
- Residential-proxy-as-OBF-infrastructure pattern observation → **likely** structurally

## Quote budget reservation (Hard Rule 6, 15-word cap)

Candidate at-cap quotes from Krebs:

- "researchers from multiple security firms concluded that the Popa botnet is linked to NetNut" (14 words AT CEILING) — attribution framing
- Kramer denial: "That code was sold and licensed to third parties including resellers years ago" (13 words AT CEILING) — vendor-denial framing
- Krebs framing: "implementing a persistent communications layer capable of registering a device, maintaining" (11 words) — technical framing

## Extraction notes

- Language: en
- Publisher byline: Brian Krebs
- Article type: investigative journalism with multi-vendor source consolidation
- Raw IOC extraction invoked: yes (4 domains; attribution claims with verbatim quotes preserved)
