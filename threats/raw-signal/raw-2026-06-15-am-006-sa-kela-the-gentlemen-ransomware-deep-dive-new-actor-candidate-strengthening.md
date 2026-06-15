---
raw_id: raw-2026-06-15-am-006
collected_at: 2026-06-15T07:45:00-04:00
run_id: pre-brief-20260615-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: securityaffairs
  source_name: Security Affairs
  source_url: https://securityaffairs.com/193622/uncategorized/infostealers-ai-and-a-90-affiliate-cut-fuel-the-gentlemen-groups-rise.html
  published_at: 2026-06-15T06:58:21+00:00
match_reason:
  watchlist: []
  actors: ["The Gentlemen", "zeta88"]
  vulnerabilities: [CVE-2024-55591]
  keywords: [The Gentlemen, KELA, ransomware, 483 victims, infostealers, vibe-coded, Qwen, AI-assisted, Black Basta study, alerts.bar, 2GO Philippine logistics, FortiOS]
triage_tags: [new_actor_candidate_strengthening, kela_primary, ai_assisted_ransomware, non_roster, non_ad_direct]
iocs_extracted: true
iocs_count: 4
text_word_count: 720
promoted: true
finding_id: finding-2026-06-15-0005
promoted_at: 2026-06-15T08:32:00-04:00
ttl_expires_at: 2026-09-13T07:45:00-04:00
---

# SA / KELA RansomNews — The Gentlemen Ransomware Deep-Dive — /new-actor Candidacy Strengthens

**Source:** Security Affairs (Pierluigi Paganini), published 2026-06-15T06:58:21Z (02:58 EDT).
**URL:** https://securityaffairs.com/193622/uncategorized/infostealers-ai-and-a-90-affiliate-cut-fuel-the-gentlemen-groups-rise.html

**Primary source:** KELA RansomNews research report, published 2026-06-13 (per article).

## Substrate context

The Gentlemen ransomware brand was **second-flagged in 06:00 EDT FLASH sentinel today** as possible /new-actor candidate but NOT raw-signaled at that sweep (FLASH-NEGATIVE evaluation). This deeper KELA detail published by SA at 02:58 EDT and surfaced in 07:30 pre-brief sweep provides substantively more research-quality substrate worth grader / actor-profiler review.

**The Gentlemen is NOT on the 24-actor `_roster.yaml`.** Operator-deferred /new-actor consideration carried from 06:00 sweep.

## Article substance — substrate worth grader / actor-profiler attention

**Scale and trajectory:**
- Surfaced as ransomware operation 2025-09
- 483 victims listed on Tor leak site by 2026-06-13 (KELA observation date)
- **380 of 483 victims in 2026 alone** — accelerating 2026 trajectory
- **2nd-most-prolific 2026 ransomware brand by leak-site count, behind only Qilin**

**Structure (per leaked chats):**
- 9 core members
- Affiliate-based: external operators handle intrusion, keep 90% of ransom (generous-by-current-standards split)
- Core team builds + maintains ransomware + negotiation panel
- Chat-log leak May 2026, spans 2025-11-07 through 2026-04-30
- One named administrator: handle `zeta88` (operational-handle attribution only, no real-identity surface)

**Geographic / sector distribution (atypical):**
- ~15% US victims (vs typical 40-50% across other ransomware leak sites — atypically low)
- Top victim countries: Thailand, Brazil, UK, France, India, Germany, Italy, Japan, Taiwan, Spain
- Sectoral leaders: Manufacturing (top), then Technology, Business Services, Healthcare (44 victims)
- Targeting doctrine (per leaked chats): "Tier 1 to 3 countries and Latin America" priority; "operational pain over raw revenue" — reasoning that a $20M utility can pay faster than a $200M manufacturer if the lock genuinely halts the business

**Initial-access TTP set:**
- **FortiOS authentication-bypass CVE-2024-55591** (well-known older vuln)
- ZeroLogon
- PetitPotam
- **Valid credentials from compromised Outlook Web Access mailboxes** (used both to find VPN logins AND to send phishing from trusted internal accounts)
- **Infostealer credentials sourced from commodity stealer markets** — primary access vector

**Cross-validation against named victim:**
- KELA cross-referenced sample of named Gentlemen victims against `alerts.bar` infostealer index
- **2GO Philippine logistics firm** (NOT A&D-prime) example: 6 employee logins + 7 customer logins + **38 active session tokens** already exposed in stealer data BEFORE 2GO appeared on Gentlemen leak site

**AI-assisted operations (substantive net-new substrate):**
- Operators discussed "uncensored" / "abliterated" open-weight models
- Specifically named: **stripped-down Qwen variant** for coding and analysis of "hundreds of gigabytes of stolen data"
- `zeta88` admin reportedly "vibe-coded" the negotiation panel "in three days" (paraphrased to ≤15 words)

**Tradecraft inheritance:**
- Crew "studied the February 2025 Black Basta chat leak" as a training manual
- Copied phishing + mailbox-abuse workflows directly from Black Basta playbook
- Did NOT build novel TTP from scratch — derivative tradecraft pattern

**Extortion approach:**
- Willing to "get personal" — KELA observed operator pressure via sensitive medical content sent from compromised personal mailbox (single observation)
- Microsoft separately documented a "self-propagating Go-based encryptor" attributed to The Gentlemen (Microsoft attribution noted — not Archimedes-originated)

## Attribution language (preserved per Hard Rule 2)

- **No nation-state attribution.** KELA does not attribute to RU/CN/IR/KP cluster.
- **Microsoft attribution** (per article reference): Microsoft separately documents Go-based encryptor as The Gentlemen — this is Microsoft's binding, not Archimedes-originated.
- **Black Basta lineage:** training-manual relationship, NOT actor-cluster overlap. Hard Rule 2 binding preserved: The Gentlemen and Black Basta are framed by KELA as derivative-tradecraft pattern, not overlapping operator-clusters.
- **`zeta88`** is operational handle from leaked chats; not a real-identity surface.

## IOC extraction

```yaml
iocs:
  cve_references:
    - value: CVE-2024-55591
      type: initial_access_vector
      product: FortiOS
      class: authentication_bypass
      note: "Re-used 2024-disclosed vuln; not in active KEV cycle today; widely deployed legacy exposure"
      sources: [KELA, Microsoft (via article reference)]
  named_victim_with_session_token_exposure:
    - value: "2GO Philippine logistics"
      type: named_ransomware_victim
      pre_exposure_observation:
        employee_logins: 6
        customer_logins: 7
        active_session_tokens: 38
        infostealer_index_source: "alerts.bar"
      ad_prime_relevance: NO
      sources: [KELA]
  ai_tooling_pattern:
    - value: "Qwen variant (stripped-down / uncensored / abliterated)"
      type: open_weight_model_pattern
      use_case: "coding + analysis of hundreds of GB stolen data"
      sources: [KELA]
  operational_handles:
    - value: "zeta88"
      type: leak_chat_handle
      role: administrator
      sources: [KELA]
attribution_claims:
  - text: "The Gentlemen self-propagating Go-based encryptor"
    source: Microsoft (per article reference; not direct retrieval)
    grade: A (Microsoft IR primary tier)
    nation_state_attribution: null
```

## A&D-prime / watchlist match

- **NONE direct.** Manufacturing top-sector and Healthcare 44 victims, but no A&D-prime specifically named. 2GO Philippine logistics is a logistics firm, not A&D-prime.
- **Indirect / supplier-ecosystem concern:** Manufacturing top sector + Tier 1-3 country prioritization MAY include defense-supplier-ecosystem entities at Tier-2/3 levels (smaller machining shops, electronics manufacturers servicing A&D primes). Not specifically named per KELA / SA coverage.

## /new-actor candidacy — substrate evaluation

The Gentlemen /new-actor candidacy substrate (cumulative across surfaces in current window):

- **06:00 EDT 2026-06-15 FLASH sentinel:** flagged as /new-actor candidate based on KELA scale framing (2nd-most-prolific 2026); operator-deferred
- **07:30 EDT this raw-signal:** SA deep-dive with KELA primary detail; 9-core-member structure; AI-assisted tooling; alerts.bar IOC cross-validation; Black Basta tradecraft inheritance; **substrate is now sufficient for /new-actor scaffolding evaluation**

**Recommend actor-profiler review window:** post-PeopleSoft-deadline-cycle (EOD Sunday 2026-06-15 + Monday morning brief 2026-06-16) for /new-actor candidacy scaffolding. Substrate is research-firm-grade (KELA RansomNews), multi-vector confirmed (FortiOS + ZeroLogon + PetitPotam + infostealer + OWA), distinctively named ("The Gentlemen"), with quantified victim scale.

**Per actor-profiler scoring framework:** estimated initial categories (NOT scoring this sweep, just substrate-flag for profiler):
- Cyber-crime: HIGH (483 victims, manufacturing focus, financially motivated, AI-assisted)
- Destructive: HIGH (encryptor confirmed by Microsoft)
- Disruptive: MEDIUM (extortion-with-personal-content suggests willingness to amplify pressure beyond data-locking)
- Espionage: LOW (financially motivated, not state-cluster)
- Supply-chain: MEDIUM (infostealer-credential-sourcing is supply-chain-adjacent attack pattern)
- Intent: Sector Association (manufacturing, not target-specific A&D)
- Capability: Inheritor (Black Basta-derived tradecraft; AI-assisted operational uplift)

## Grader handoff considerations

1. **Not FLASH-eligible.** T2 NEGATIVE (actor not on roster), T5 NEGATIVE (manufacturing-broad not A&D-specific), T4 NEGATIVE (no roster-actor TTP change).

2. **Other Signal candidate** for morning brief with actor-profiler /new-actor pointer — 1-2 line note about scale + AI-assisted-tooling-pattern + recommend post-deadline /new-actor scaffolding.

3. **Substrate is research-firm-grade** (KELA RansomNews primary, SA B-grade publisher relay) — meets multi-tier-source quality bar for Other Signal inclusion.

4. **CVE-2024-55591 FortiOS** is in CISA KEV but with deadline well-past; mention as "still-in-active-use" context not net-new FCEB-class urgency.

## Extraction notes

- Language: en
- Publisher byline: Pierluigi Paganini (SA)
- Primary source: KELA RansomNews 2026-06-13 (research-firm-grade)
- Article type: deep-dive research-report relay
- Publisher independence: 2 surfaces (KELA primary + SA relay); awaiting THN / BleepingComputer corroboration
- IOC extraction: 4 IOCs (1 CVE, 1 victim cross-validation pattern, 1 AI-tooling pattern, 1 operational handle)
- Attribution: KELA primary research; Microsoft separately attributes Go-based encryptor
- A&D match: NO direct
- Roster match: NO ("The Gentlemen" not on roster; /new-actor candidacy substrate strengthening)
- Vulnerability match: SOFT (CVE-2024-55591 referenced as initial-access vector but not net-new vuln)
- FLASH evaluation: all 6 triggers NEGATIVE
- Hard Rule 7: 0 verbatim quotes over 15 words
- Hard Rule 2: KELA + Microsoft language preserved verbatim; Black Basta-lineage framed as tradecraft inheritance NOT cluster overlap
- Hard Rule 3: ransomware operation described at substrate granularity; no encryptor PoC or exploit walkthrough content extracted
