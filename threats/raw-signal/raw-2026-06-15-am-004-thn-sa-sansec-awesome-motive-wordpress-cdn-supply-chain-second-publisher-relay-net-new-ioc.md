---
raw_id: raw-2026-06-15-am-004
collected_at: 2026-06-15T07:41:00-04:00
run_id: pre-brief-20260615-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: thehackernews
  source_name: The Hacker News
  source_url: https://thehackernews.com/2026/06/popular-wordpress-plugin-scripts.html
  published_at: 2026-06-15T09:59:38+00:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [Awesome Motive, OptinMonster, TrustPulse, PushEngage, CDN supply chain, Sansec, Polyfill, tidio.cc, JavaScript backdoor]
triage_tags: [supply_chain_compromise, multi_publisher_corroboration_achieved, net_new_ioc, consumer_wordpress_non_ad, polyfill_lineage]
iocs_extracted: true
iocs_count: 8
text_word_count: 480
promoted: true
finding_id: finding-2026-06-15-0003
promoted_at: 2026-06-15T08:20:00-04:00
ttl_expires_at: 2026-09-13T07:41:00-04:00
---

# THN Awesome Motive WordPress CDN Supply-Chain — 2nd Publisher Relay, Net-New IOC `84.201.6.54`

**Source:** The Hacker News. Published 2026-06-15T09:59:38Z (05:59 EDT).
**URL:** https://thehackernews.com/2026/06/popular-wordpress-plugin-scripts.html

**Companion source:** Security Affairs (Pierluigi Paganini), https://securityaffairs.com/193616/malware/supply-chain-attack-hits-popular-wordpress-plugins-through-awesome-motive-cdn.html, published 2026-06-15T08:34:02Z (04:34 EDT) — SA was first publisher-relay; THN is second.

**Primary source:** Sansec disclosure 2026-06-13.

## Multi-publisher corroboration status

- **Primary discoverer:** Sansec (A2-tier security research firm, Polyfill 2024 incident attribution lineage)
- **First publisher-relay:** Security Affairs (B-grade publisher, 2026-06-15 04:34 EDT)
- **Second publisher-relay:** The Hacker News (B-grade publisher, 2026-06-15 05:59 EDT)
- **Three independent surfaces** (Sansec primary + SA + THN) — meets multi-publisher-independence threshold per INTEL-GRADING discipline; substrate is corroborated, not single-source.

## Article substance (net-new vs SA piece)

THN adds the following substrate beyond SA's coverage:

1. **Attacker server IP `84.201.6.54` disclosed** — NEW IOC vs SA, which only listed C2 domain `tidio.cc`. IP `84.201.6.54` is owned by Yandex Cloud per public ASN data (Russian cloud provider — not Archimedes-resolved this sweep, mentioned only in context of provider attribution).
2. **PushEngage UpdraftPlus initial-entry theory disputed by Sansec** — PushEngage claims attacker exploited a known UpdraftPlus WordPress backup plugin vuln on a server hosting its marketing website, exposing CDN API key. Sansec characterizes this as unverified ("the breached system is still unknown").
3. **Hidden plugin folder names refined:** "content-delivery-helper" and "database-optimizer" — same naming as SA but THN adds version refinements (v2.7.1 vs v2.9.4 — though SA already had these specific versions).
4. **Admin account patterns reaffirmed:** "developer_api1" (fixed) and "dev_xxxxxx" (randomized variants).
5. **PushEngage timeline more granular:** OptinMonster + TrustPulse hot for ~25 min UTC 22:17-22:42 on 2026-06-12; PushEngage hot from 2026-06-12 22:17 UTC until 2026-06-14 (CDN servers continued serving compromised script for ~36h on PushEngage despite remediation announcement).
6. **Total reach refined:** 1.2M sites collective vs SA's "thousands."
7. **Web-shell capability of hidden plugin:** "WPM File Manager & Shell" disclosed as the web-shell brand string; runs arbitrary system commands, accepts file uploads, exposes `eval`-class PHP execution via unauthenticated entry points.

## Attribution language (preserved per Hard Rule 2)

- **No tracked threat actor attribution.** Sansec's framing per both SA and THN coverage: "Polyfill-pattern attackers." That is a pattern-of-method comparison to the Polyfill 2024 supply-chain compromise (where supply-chain.dev domain operators silently replaced clean polyfill.js with malicious code). NOT an actor-cluster name.
- C2 domain `tidio.cc` registered 2026-04-28 — typosquat of `tidio.com` (legitimate live-chat platform). Plan-ahead pattern (45+ days domain warm-up before first malicious activity 2026-06-12).
- Attacker server IP `84.201.6.54` — Yandex Cloud ASN per public DNS. Sansec does NOT attribute to Russian state actor; cloud-provider attribution is method-pattern not actor-attribution.

## IOC extraction (Hard Rule 7 / 8 compliant)

```yaml
iocs:
  domains:
    - value: tidio.cc
      type: c2_domain
      first_seen: 2026-04-28  # domain registration
      first_active: 2026-06-12T22:17:00Z
      tld_typosquat_of: tidio.com
      sources: [Sansec, THN, SA]
    - value: clientcdn.pushengage.com
      type: legitimate_compromised_cdn
      affected_files: ["pushengage-web-sdk.js", "pushengage-subscription.js"]
      sources: [Sansec, THN]
  ipv4:
    - value: 84.201.6.54
      type: attacker_server
      asn_owner: "Yandex Cloud (per public DNS, not Archimedes-resolved)"
      sources: [Sansec, THN]
  malicious_admin_account_patterns:
    - value: "developer_api1"
      type: fixed_username
      sources: [Sansec, THN, SA]
    - value: "customer1usx@gmail.com"
      type: associated_email
      sources: [Sansec, SA]
    - value: "dev_xxxxxx"
      type: randomized_username_pattern
      sources: [Sansec, THN, SA]
  plugin_disguises:
    - value: "content-delivery-helper"
      version: "v2.7.1"
      type: hidden_backdoor_plugin
      sources: [Sansec, THN, SA]
    - value: "database-optimizer"
      version: "v2.9.4"
      type: hidden_backdoor_plugin
      sources: [Sansec, THN, SA]
attribution_claims:
  - text: "Polyfill-pattern attackers"
    grade: B
    publisher_independent_corroboration: yes
    sources: [Sansec, THN, SA]
    actor_cluster_name: null
    nation_state_attribution: null
```

## A&D-prime / watchlist match

- **NONE.** OptinMonster, TrustPulse, PushEngage are consumer marketing / lead-generation / push-notification plugins. NOT used in A&D-prime production environments per known sector stack. Consumer WordPress ecosystem.
- **No A&D-prime victim named** in either THN or SA piece.

## Grader handoff considerations

1. **Possible Other Signal one-liner** for morning brief — pattern-of-CDN-supply-chain-compromise reinforces Polyfill 2024 lineage; consumer WordPress out of A&D-prime scope, low operational urgency for FCEB-class peers.

2. **Not FLASH-eligible.** T2 NEGATIVE (no tracked actor), T5 NEGATIVE (consumer plugins not A&D sector), T3 worth Splunk-sentinel-extension query for `84.201.6.54` + `tidio.cc` (1-call free InternetDB lookup) if grader chooses — but probability of hit on Frank's index is negligible given consumer-WordPress-class compromise.

3. **Multi-publisher independence achieved** (Sansec primary + SA + THN) — substrate is corroborated, grader could grade B2 if promoted.

4. **Polyfill 2024 lineage flag** — Sansec compared this to their own 2024 Polyfill discovery. **However, Hard Rule 2 binding: do NOT originate attribution beyond what Sansec / THN / SA say.** Sansec uses "Polyfill-pattern" as method comparison, NOT as actor-cluster carryover. Actor-cluster identity remains unknown.

## Extraction notes

- Language: en
- Publisher byline: THN editorial (no individual author byline)
- Article type: news / supply-chain compromise relay
- Publisher independence: 3 independent surfaces (Sansec primary + SA + THN second-relay)
- IOC extraction: 8 IOCs (1 C2 domain, 1 compromised CDN domain, 1 IPv4, 3 account/email patterns, 2 plugin disguises)
- Attribution: "Polyfill-pattern attackers" (Sansec method-pattern framing, NOT actor-cluster name)
- A&D match: NO
- Roster match: NO
- Vulnerability match: NO direct CVE; UpdraftPlus initial-entry theory mentioned but no CVE assigned and Sansec characterizes as unverified
- FLASH evaluation: all 6 triggers NEGATIVE
- Hard Rule 7: 0 verbatim quotes over 15 words
- Hard Rule 2: "Polyfill-pattern" preserved verbatim as Sansec method-framing; no actor-cluster name fabricated
