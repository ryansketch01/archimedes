---
raw_id: raw-2026-06-11-am-001
collected_at: 2026-06-11T07:35:00-04:00
run_id: pre-brief-20260611-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: thehackernews
  source_name: "The Hacker News (B-grade aggregator carrying ESET A-grade originating research)"
  source_url: https://thehackernews.com/2026/06/oceanlotus-hits-vietnam-investors-with.html
  source_url_originating_research: "ESET (Slovakian vendor — research findings shared with The Hacker News; direct ESET WeLiveSecurity URL not surfaced in THN article)"
  published_at: 2026-06-11T09:45:58+00:00   # 05:45 EDT in window
match_reason:
  watchlist: []
  actors: [OceanLotus, APT32]
  vulnerabilities: []
  keywords: [oceanlotus, apt32, spectralviper, fireant, vietnam, supply_chain, dll_side_loading, onedrive_sync_service, espionage]
triage_tags: [actor_not_in_roster, new_actor_candidate_orchestrator_flag, vietnam_aligned, ad_relevance_low, supply_chain_attack, espionage_campaign, eset_originating_a_grade_research, thn_b_grade_relay, weekly_synthesis_candidate, no_ad_watchlist_victim, no_first_party_splunk_hits]
iocs_extracted: true
iocs_count: 3
text_word_count: 850
promoted: true
promoted_to_finding: finding-2026-06-11-0003-thehackernews-eset-oceanlotus-apt32-spectralviper-fireant-supply-chain-vietnam-not-in-roster-new-actor-candidate
promoted_at: 2026-06-11T08:22:00-04:00
ttl_expires_at: 2026-09-09T07:35:00-04:00
---

# OceanLotus Hits Vietnam Investors With SPECTRALVIPER in FireAnt Attack

**Source:** The Hacker News (B-grade aggregator)
**Originating research:** ESET (Slovakian vendor; tier-1 APT research peer)
**Published:** 2026-06-11T09:45:58 UTC = 05:45:58 EDT (in window)
**URL:** https://thehackernews.com/2026/06/oceanlotus-hits-vietnam-investors-with.html

## Attribution language (verbatim per Hard Rule 6, < 15 words)

- "Vietnam-aligned threat actor known as OceanLotus" (THN, 7 words)

ESET (originating research) attribution layer carries through THN: OceanLotus / APT32, "previously linked to CyberOne Group (2020 Meta disclosure)", active since 2012.

## Roster intersection

**OceanLotus / APT32 is NOT in `_roster.yaml`** — confirmed via grep on aliases `OceanLotus|Ocean Lotus|APT32|SeaLotus|CobaltKitty`, zero matches.

This is a `/new-actor` candidate observation per CLAUDE.md "On-Demand Commands" workflow. Same pattern observed in May 2026 collector observations for UNC6692 and UNC1069 in Mandiant feedburner notes — actors surfaced by Tier-1 vendor research without prior roster coverage.

Operator-discretion path: flagging here for orchestrator visibility rather than directly invoking `/new-actor` scaffolding (the command requires human approval per CLAUDE.md Pipeline rules).

## Article content summary (Hard Rule 7 rights-respecting paraphrase)

OceanLotus (APT32, Vietnam-aligned) attributed to two distinct campaigns:

**Campaign 1 — Vietnamese infrastructure/transport construction corporation espionage:**
- Period: Mid-2024 through February 2026 (~20 months)
- Victim type: Vietnamese infrastructure and transport construction corporation
- Espionage objective (cyber espionage operation framing per ESET / THN)

**Campaign 2 — FireAnt Metakit supply chain attack:**
- Period: October 2025 through March 2026 (~6 months)
- Victim type: Stock investors (via FireAnt Metakit platform — Vietnamese investor-tools platform)
- Mechanism: Supply chain attack on FireAnt Metakit; trojanized installer or update path

**Malware:**
- SPECTRALVIPER backdoor (new family name per ESET / THN)
- DLL side-loading chain via legitimate binaries
- Process injection into `OneDrive.Sync.Service.exe` (LOLBin-style host process abuse)

**Verbatim quote (Hard Rule 6, < 15 words):**
- THN: "prolonged cyber espionage operation aimed at a Vietnamese infrastructure" (8 words; characterization-only, not technical claim)

## IOCs (extraction-skill style structured)

```yaml
domains_c2:
  - value: "financemachinelearning[.]com"
    role: C2
    family: SPECTRALVIPER
    confidence: a_grade_eset_originating
  - value: "gatewayrvcenter[.]com"
    role: C2
    family: SPECTRALVIPER
    confidence: a_grade_eset_originating

urls_supply_chain:
  - value: "metakit.fireant[.]vn/Software/version.xml"
    role: supply_chain_update_path
    family: FireAnt_Metakit_compromise
    confidence: a_grade_eset_originating
    note: |
      FireAnt Metakit is a Vietnamese investor-tools platform; the
      compromised update path served the trojanized installer in the
      Campaign 2 supply-chain attack vector.

iocs_hashes: []  # not surfaced in THN article body; would require direct ESET WeLiveSecurity retrieval

attribution_claims:
  - actor: OceanLotus
    aliases: [APT32, SeaLotus_implied_not_explicit]
    nation_alignment: VN  # Vietnam-aligned per ESET / THN
    confidence_per_source: high_eset_originating
    technical_evidence: |
      SPECTRALVIPER backdoor family + DLL side-loading TTP + targeting
      pattern (Vietnamese domestic entities + diaspora-adjacent
      investor platforms). ESET methodology not detailed in THN relay
      (would require WeLiveSecurity direct retrieval for full
      grading-actionable detail).
    operator_target_match: false  # no A&D-prime intersection
```

## Sector and A&D relevance

- **NO US A&D-watchlist victim named.** Campaigns target Vietnamese domestic entities (infrastructure/transport construction corporation) and Vietnamese investor platforms (stock investors via FireAnt).
- **A&D-relevance: LOW.** Vietnam-aligned actor targeting Vietnamese-domestic entities is out-of-scope for operator target profile (mid-to-large US A&D contractor, ITAR-regulated, US gov contracts, Tier-1/2 supplier network).
- Tradecraft (DLL side-loading, OneDrive.Sync.Service.exe LOLBin injection, supply-chain via update-path compromise) IS portable to A&D-prime espionage scenarios, but ESET research does NOT claim such targeting in this report.

## First-party Splunk corroboration

- `archimedes` + `defenseclaw_local` -24h@h queries on `OceanLotus`, `APT32`, `SPECTRALVIPER`, `FireAnt`, `financemachinelearning`, `gatewayrvcenter`, `metakit.fireant` — **zero substantive hits.**
- Hard Rule 8: silence is not disconfirming, not confirming.

## Disposition

Grader to evaluate:

1. **Promotion to finding** — possibly, given Tier-1 origination (ESET) + APT-tier actor + technical IOCs (2 C2 domains + 1 supply-chain URL). A&D-relevance LOW caps weighted priority.
2. **Morning brief inclusion** — likely NOT (A&D-relevance LOW + no operator-target intersection + no first-party hit). Possibly a brief context bullet under Iran/China-adjacent geopolitical framing IF the briefer ranks Vietnam-aligned tradecraft drift toward US A&D targets in coming reporting (no evidence today).
3. **Weekly synthesis** — candidate. The /new-actor evaluation pathway is more naturally weekly-synthesis or operator-discretion than urgent-AM-brief.
4. **`/new-actor` candidate flag for orchestrator** — yes. Add APT32 to a watchlist of /new-actor candidates alongside the May 2026 UNC6692 + UNC1069 observations.

## Extraction notes

- Language: en
- Publisher byline: The Hacker News editorial
- Article type: blog (B-grade aggregator carrying A-grade ESET research)
- Raw IOC extraction invoked: yes (structured above)
- Quote discipline: Hard Rule 6 satisfied (two quotes, each < 15 words, from THN; ESET originating-quote not surfaced in THN body)
- Hard Rule 3 (no exploitation assistance): SPECTRALVIPER DLL-side-loading technique referenced at functional level only; no PoC code or weaponization aid extracted
