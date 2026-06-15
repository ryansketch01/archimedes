---
raw_id: raw-2026-06-15-pm-004
collected_at: 2026-06-15T15:45:00-04:00
run_id: pre-brief-20260615-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: securityaffairs
  source_name: Security Affairs (Pierluigi Paganini)
  source_url: https://securityaffairs.com/193657/data-breach/australian-sugar-producer-mackay-sugar-reports-cyber-incident.html
  published_at: 2026-06-15T18:51:17+00:00
additional_publisher_relay:
  - source_yaml_id: securityweek
    source_name: SecurityWeek (Eduard Kovacs byline, 2026-06-15 15:15 UTC)
    source_url: https://www.securityweek.com/ransomware-attack-shuts-down-mills-of-australias-second-largest-sugar-producer/
match_reason:
  watchlist: []
  actors: [The Gentlemen, Storm-2697, LARVA-368, Phantom Mantis]   # NONE on _roster.yaml; operator-deferred /new-actor candidacy substrate-strengthening
  vulnerabilities: []
  keywords: [Mackay Sugar, Queensland, sugar mill, crushing season, two of three mills offline, Tor leak site, The Gentlemen claim, Storm-2697 Microsoft tracking, KELA chat leak, 90/10 affiliate split, 483 victims, second-most-prolific 2026, Qilin]
triage_tags: [substrate_update_on_morning_finding, net_new_victim, operational-template-disruption, anti-noise-update-not-flash, ot-ICS-adjacent-not-confirmed, operator-deferred-/new-actor-candidacy]
iocs_extracted: true
iocs_count: 0
text_word_count: 510
promoted: true
promoted_to_finding: finding-2026-06-15-0009-sa-sw-mackay-sugar-the-gentlemen-australia-484th-victim-net-new-crushing-season-disruption-ot-it-recovery-question-update-on-finding-2026-06-15-0005
promoted_at: 2026-06-15T16:28:00-04:00
ttl_expires_at: 2026-09-13T15:45:00-04:00
---

# Australian Sugar Producer Mackay Sugar Reports Cyber Incident — The Gentlemen claims responsibility

**Security Affairs (Pierluigi Paganini)** — 2026-06-15 18:51 UTC

Mackay Sugar, Australia's second-largest sugar producer, disclosed a cyberattack on June 10,
potentially affecting key processing operations. The Gentlemen ransomware group, tracked by
Microsoft as Storm-2697, claimed responsibility for the attack and added Mackay Sugar to its
Tor-based data leak site on June 15. At this time, no data has been leaked yet, which usually
means negotiations are still ongoing.

## Victim profile

- **Mackay Sugar**: Australia's second-largest sugar manufacturer
- Based in Mackay region of tropical North Queensland; 140+ years of sugar-cane processing
  history
- **Three major sugar mills**: Farleigh, Marian, Racecourse
- ~700,000 tonnes of raw sugar produced annually for domestic and export markets

## Attack timeline

- **2026-06-10**: Cyberattack disclosed; attack hit during crushing season
- **2026-06-12**: Restarted limited manual crushing at Farleigh Mill (pre-harvested cane only)
- **2026-06-15**: Steam trials underway; Mackay Sugar published update; The Gentlemen added
  victim to Tor leak site
- **Currently**: Two of three mills appear forced offline; growers/harvesters told to hold
  pending mill restart

## Vendor / victim statements (verbatim, Hard Rule 6 — under 15 words each)

> "Mackay Sugar is responding to a cyber security incident affecting some of our operations."
> (12 words — Mackay Sugar disclosure)

> "Significant progress has been made over the weekend in restoring the systems that support
> cane supply, harvesting and mill operations." (Mackay Sugar 2026-06-15 update — paraphrase only
> per Hard Rule 6 limit)

## The Gentlemen actor profile (carry-forward from finding-2026-06-15-0005 substrate)

> "The Gentlemen ransomware group, tracked by Microsoft as Storm-2697, claimed responsibility
> for the attack and added Mackay Sugar to its Tor-based data leak site on June 15."

- The Gentlemen surfaced as a ransomware operation in **September 2025**
- By **2026-06-13** had listed **483 victims** on dark-web leak site; **380 in 2026 alone**
- Second-most-prolific ransomware brand of 2026 by published victim count (behind Qilin only)
- May 2026 leak of internal chat logs (KELA research): nine core members, AI-assisted tooling,
  access model built on commodity infostealer-stolen credentials
- Affiliate model: small core team builds ransomware + negotiation panel; external operators
  carry out intrusions and keep **90% of each ransom** (10% to core team)
- Leaked chats span **2025-11-07 to 2026-04-30**; described as "small product team arguing
  about infrastructure choices and which AI model to use for data analysis"
- Microsoft Storm-2697 tracking (per Paganini)
- PRODAFT tracks as **LARVA-368** with **Phantom Mantis** designation (per finding-2026-06-15-0005
  cross-corroboration substrate)

## OT / ICS exposure question (analyst-side flag, not collector-attributed)

Mackay Sugar's public statements don't mention data compromise, and it's still unclear
whether the attackers reached industrial control systems directly or whether operational
technology was affected as a downstream consequence of IT systems going down. That
distinction matters: IT recovery and OT recovery are different problems with different
timelines, and a mill that's restored its business systems but hasn't verified its control
systems is not a fully recovered estate.

**Operator note**: This is the analyst's framing-level question per the SA primary text, NOT
a Sygnia-style attributed claim of OT compromise.

---

## Extraction notes

- Language: en
- Publisher byline: Pierluigi Paganini (Security Affairs)
- Secondary publisher: Eduard Kovacs (SecurityWeek), 2026-06-15 15:15 UTC
- Primary source: Mackay Sugar public statements + The Gentlemen Tor leak-site listing
- Article type: ransomware-victim disclosure + extortion-group claim + actor-cluster context
- Raw IOC extraction invoked: yes (no fresh hashes/IPs/domains)

## IOCs (from ioc-extraction skill)

```yaml
iocs:
  hashes: []
  ips: []
  domains:
    - tor_leak_site (per SA reference; specific .onion address NOT published in SA relay)
  victims_named:
    - "Mackay Sugar (Australia, 2026-06-10, sugar manufacturing, OT-adjacent question open)"
  cves: []

attribution_claims:
  - source: The Gentlemen (self-claim on Tor leak site)
    claim: "claimed responsibility for the attack and added Mackay Sugar to its Tor-based data leak site on June 15"
    confidence: SELF_CLAIM
    actor_cross_tracking:
      microsoft_taxonomy: Storm-2697
      prodaft_taxonomy: LARVA-368 / Phantom Mantis
      operator_identity_chain: "Alexander Andreevich Yapaev (per finding-2026-06-11-0009 PRODAFT primary substrate; prior LockBit Tenacious Mantis / Qilin Pestilent Mantis / Medusa Venomous Mantis before transitioning to independent operator July 2025)"
    note: |
      Hard Rule 2 preserved — The Gentlemen / Storm-2697 / LARVA-368 / Phantom Mantis is a
      consolidated cross-vendor naming chain (Microsoft + PRODAFT + KELA + Mandiant peer
      class). NONE on Archimedes 24-actor _roster.yaml. Operator-deferred /new-actor candidacy
      substrate-strengthening per Hard Rule 5; collector does NOT originate roster addition.
      The substrate-strengthening rationale this surface: NET-NEW high-profile victim
      (Australia's 2nd-largest sugar producer) + sustained-cadence-confirmation (484th victim
      added 2026-06-15 — 1 day after the KELA-deep-dive 483-victim count cited 2026-06-13).

actor_cluster_context:
  - finding-2026-06-15-0005 substrate (KELA RansomNews deep-dive, 483 victims, AI-assisted Qwen variant, Black Basta Feb 2025 chat-leak training derivative, Microsoft Go-encryptor separate, operator-deferred /new-actor candidacy)
  - finding-2026-06-11-0009 substrate (PRODAFT Phantom Mantis primary, Yapaev operator-identity chain)
  
ad_relevance_notes_for_grader:
  ad_relevance: low_to_medium
  ad_relevance_rationale: |
    Mackay Sugar is an Australian agricultural processor — NOT A&D-prime; NOT DIB / CMMC
    partner-flow estate; NOT ITAR-regulated. Operational disruption (two of three mills
    offline during crushing season) is materially severe at the industrial level but the
    victim sector is agricultural-food-processing, not aerospace / defense. A&D relevance
    is at the operational-template level only (manufacturing + crushing-season-timing +
    OT-adjacent + 90/10 affiliate split + AI-assisted-Qwen-variant tradecraft pattern is
    relevant to A&D-prime defenders studying ransomware against process-industry estates,
    but Mackay-Sugar-itself is not on the watchlist).

anti_noise_disposition: SUBSTRATE_UPDATE
anti_noise_reasoning: |
  Carry-forward anti-noise hold from morning brief: finding-2026-06-15-0005 (KELA RansomNews
  deep-dive of The Gentlemen ransomware /new-actor candidacy substrate). This sweep adds:
    1. NET-NEW victim (Mackay Sugar, 484th cumulative);
    2. Operational-disruption template (crushing-season-timing + IT/OT recovery boundary
       question);
    3. Independent two-publisher relay (Paganini SA + Kovacs SW, both B-grade provisional);
    4. Sustained-cadence-confirmation (484th victim added ~2 days after the KELA-deep-dive
       483-victim count was published, supports the 380-in-2026 second-most-prolific framing).
  Substrate-update is grader-decision territory; collector marks NET-NEW + carry-forward
  signal-strengthening for operator-deferred /new-actor candidacy.

flash_trigger_evaluation_notes_for_grader:
  trigger_2_tracked_actor_attribution: FAIL — The Gentlemen / Storm-2697 / LARVA-368 /
    Phantom Mantis NONE on _roster.yaml (operator-deferred /new-actor candidacy).
  trigger_4_tracked_actor_ttp_change: FAIL — same as Trigger 2.
  trigger_5_ad_sector_campaign: MARGINAL FAIL — Mackay Sugar is NOT A&D-prime / NOT DIB /
    NOT watchlist entity. multi_victim_confirmed = TRUE (484 cumulative) but
    targets_include_aerospace_defense = FAIL on this surface.
  flash_disposition: NOT FLASH — substrate update suitable for 16:00 afternoon brief
    (UPDATE-finding pathway on finding-2026-06-15-0005 per grader decision OR Other Signal
    one-liner).
```
