---
raw_id: raw-2026-05-28-pm-005
collected_at: 2026-05-28T16:00:00-04:00
run_id: pre-brief-20260528-pm
collection_mode: pre_brief_collection
source:
  source_yaml_id: bleepingcomputer
  source_name: BleepingComputer
  source_url: https://www.bleepingcomputer.com/news/security/fbi-warns-of-fake-fifa-websites-running-world-cup-fraud-schemes/
  source_grade: B
  source_yaml_id_corroborating_1: the-record
  source_url_corroborating_1: https://therecord.media/chinese-speaking-fraud-gang-fifa-world-cup-scam
  source_yaml_id_corroborating_2: fbi-flash
  source_url_corroborating_2: https://www.ic3.gov/PSA/2026/PSA260527   # PSA260527 reference per BleepingComputer
  originating_research_firm: Group-IB
  fbi_alert_reference: PSA260527
  authored_by_bleeping: Bill Toulas
  authored_by_record: Alexander Martin (UK Editor for Recorded Future News)
  published_at_bleeping: 2026-05-28T19:08:10Z   # 15:08 EDT
  published_at_record: 2026-05-28T13:26:00Z     # 09:26 EDT
match_reason:
  watchlist: []   # consumer-focused; no A&D direct
  actors: []      # Ghost Stadium NOT in _roster.yaml
  vulnerabilities: []
  keywords:
    - FBI PSA260527
    - World Cup 2026 fraud
    - FIFA impersonation
    - Ghost Stadium criminal group
    - Group-IB attribution
    - Chinese-speaking fraudsters
    - Layui 2.7.6m UI library
    - 4300 fraudulent domains since August 2025
    - premium ticket fraud
    - fake employment fraud
    - Facebook advertising
    - $60 vs thousands fake tickets
triage_tags:
  - non_flash
  - new_to_corpus_actor_candidate_low_priority
  - government_source_fbi_psa
  - consumer_focused_no_ad_direct
  - world_cup_attack_surface_carry_forward
  - corroborates_morning_brief_world_cup_theme
iocs_extracted: true
iocs_count: 0
text_word_count: 600
promoted: true
promoted_to_finding: finding-2026-05-28-0008-fbi-group-ib-ghost-stadium-chinese-criminal-2026-fifa-world-cup-4300-domains
promoted_at: 2026-05-28T16:15:00-04:00
promoted_run_id: afternoon-20260528-160000
ttl_expires_at: 2026-08-26T16:00:00-04:00
---

# FBI PSA260527 / Group-IB Ghost Stadium — Chinese-Speaking Fraudsters Run 2026 FIFA World Cup Scam Cluster — 2026-05-28

## Sources

### Primary 1 — BleepingComputer (FBI advisory relay)

**Title:** "FBI warns of fake FIFA websites running World Cup fraud schemes"

**Author:** Bill Toulas

**Published:** 2026-05-28T19:08:10Z (15:08 EDT)

**FBI advisory reference:** PSA260527 (IC3 Public Service Announcement)

**URL:** https://www.bleepingcomputer.com/news/security/fbi-warns-of-fake-fifa-websites-running-world-cup-fraud-schemes/

### Primary 2 — The Record (Group-IB research relay)

**Title:** "Chinese-speaking fraud gang could be stealing millions from 2026 World Cup fans"

**Author:** Alexander Martin (UK Editor for Recorded Future News)

**Published:** 2026-05-28T13:26:00Z (09:26 EDT)

**URL:** https://therecord.media/chinese-speaking-fraud-gang-fifa-world-cup-scam

### Originating research

**Group-IB** (Singapore-based cybersecurity firm) — originating attribution of the **Ghost Stadium** criminal group. Group-IB investigation ran March–May 2026; Ghost Stadium first observed November 2025.

---

## Actor framing (Group-IB attribution per The Record + BleepingComputer)

- **Group-IB-coined name:** Ghost Stadium
- **Attribution language (per Group-IB via The Record):**
  - "Chinese-speaking fraudsters"
  - Confidence basis: phishing kit uses Chinese open-source UI library **Layui 2.7.6m**, with **Chinese-language comments embedded throughout the source code**
- **Type:** Cybercriminal (financially motivated; consumer-focused)
- **Activity timeline:** Active since November 2025; Group-IB investigation March–May 2026
- **Targeting:** Consumer fans purchasing tickets / hospitality / employment-fraud victims; global geographic scope per Bitdefender observation

---

## Scale and methodology

### Scale (Group-IB)

- **~4,300 fraudulent domains** registered since August 2025
- **~300 actively running malicious infrastructure**
- **~3,800 dormant or pre-positioned** (campaign-stage-ready)

### Methodology (Group-IB / FBI)

- **Domain spoofing:** minor spelling variations (e.g., "fiffa[.]com") and alternative TLDs (.org, .xyz, .live, .sale)
- **Phishing kit:** clones FIFA's login system; silently redirects users to legitimate site; requests password-reset parameters to lock victims out of legitimate accounts
- **Premium-ticket fraud:** discounted tickets advertised ($60 vs thousands officially) — Facebook advertising primary distribution channel
- **Fake employment portals:** "jobs-fifa[.]com", "fifa-hiring[.]com" pattern
- **Data harvesting:** names, physical and email addresses, phone numbers, banking/payment details
- **Malvertising channels:** Google Search, Facebook ads, Telegram, WhatsApp

### Geographic spread (Bitdefender observation cited)

UK, Portugal, Spain, Algeria, US, Canada, Mexico, Brazil, Germany, Australia.

---

## IOCs

```yaml
iocs:
  ip_addresses: []
  domains:
    - "fiffa[.]com"           # exemplar typo-domain per FBI/BleepingComputer
    - "jobs-fifa[.]com"        # employment-fraud pattern
    - "fifa-hiring[.]com"      # employment-fraud pattern
    # Full ~300 active + ~3,800 dormant domain set NOT published in retrievable summary
    # Per Group-IB attribution — full list likely in Group-IB blog primary (not directly retrieved this sweep)
  hashes: []
  cves: []
  tld_patterns_observed:
    - .org
    - .xyz
    - .live
    - .sale
  phishing_kit_lineage:
    library: "Layui 2.7.6m (Chinese open-source UI library)"
    code_comments_language: Chinese
attribution_claims:
  - claim: Ghost Stadium is a "Chinese-speaking fraudster" group operating since November 2025
    claimed_by: Group-IB
    confidence_language: confident attribution on Chinese-speaking-operator profile via phishing-kit linguistic evidence (Layui library + Chinese-language code comments)
    nation_attribution_strength: Chinese-speaking operator profile (NOT China-state attribution; NOT MSS / MPS attributed); ethnic-linguistic identifier only
  - claim: "more than 300 phishing sites" operated for premium-ticket fraud
    claimed_by: Group-IB / FBI PSA260527
    confidence_language: procedural (Group-IB-counted active infrastructure)
named_entities:
  events_targeted:
    - 2026 FIFA World Cup (June 11–July 19, 2026; US / Canada / Mexico hosts)
  fraud_categories:
    - premium ticket fraud
    - employment fraud
    - data harvesting (PII + banking)
  geographic_victim_categories:
    - global consumers — no enterprise / contractor / government victims named
  ai_or_state_actor_involvement: none named
  fbi_alert_reference: PSA260527
collection_notes: |
  Pure consumer-focused criminal-fraud surface. NO A&D / NO defense /
  NO government / NO contractor victim category named in either FBI
  PSA or Group-IB attribution. Pairs with morning brief finding 0002
  (Unit 42 2026 World Cup attack surface — Iran IRGC/MOIS fronts +
  Handala + Cyberav3ngers + Razing Ursa + NoName057) as a separate
  threat-layer on the same Word Cup attack-surface theme: Iran-state
  fronts (Unit 42 morning brief) targeting different victim profile
  (think tanks / journalists / civil society) than Chinese-criminal
  Ghost Stadium (consumer fans). The fact that both Iran-state and
  Chinese-criminal operators are concurrently exploiting the World
  Cup attack surface is a sector-corroborating data point on attack-
  surface convergence, not a tracked-actor link.
```

---

## Extraction notes

- Language: en
- Article types: media relay (BleepingComputer = FBI PSA relay; The Record = Group-IB research relay)
- Body retrieval: both BleepingComputer and The Record bodies fetched successfully
- Source grades: BleepingComputer B, The Record B; FBI A; Group-IB unknown (not in source-grades.yaml — would need source-grade-log addition if Ghost Stadium surfaces in future corpus content; Group-IB is established Tier-1/Tier-2 vendor research practice)
- Two-effective-primary corroboration: FBI government source + Group-IB originating research, both relayed by independent B-grade media outlets (BleepingComputer + The Record).

## A&D / DIB relevance — collector framing for grader

- **NO A&D direct relevance** — pure consumer-focused fraud surface (premium-ticket fraud, employment fraud, data harvesting for banking). No contractor / DIB / federal employee victim category named.
- **World Cup attack-surface sector-corroboration:** the corpus is now tracking THREE distinct threat-layers on the 2026 FIFA World Cup attack surface concurrently:
  1. Iran IRGC / MOIS front campaign (Unit 42, morning brief finding 0002 — Handala / Cyberav3ngers / Razing Ursa / NoName057, ideological / disruptive)
  2. China-speaking criminal Ghost Stadium (this raw-signal — pure financial fraud, Group-IB-attributed)
  3. Unspecified additional patterns Bitdefender observed in 10 countries (mentioned in BleepingComputer but not detailed)
  This three-layer concurrence on a single event-driven attack surface is the kind of broad-spectrum opportunistic targeting A&D-prime IT teams should be modeling — World Cup season generates lure-content that traverses both consumer-fan and DIB-employee inbound vectors. DIB employee social-media activity (fan-engagement) is the spillover threat surface for primes.
- **NEW TO CORPUS (low priority):** Ghost Stadium NOT in _roster.yaml. Pure consumer-criminal targeting profile means likely no /new-actor scaffold warranted; collector flags for orchestrator awareness but recommends NO actor-roster scaffolding at this surface.

## Flash trigger evaluation

- **Trigger 1–6**: NONE MATCHED. Pure consumer-fraud campaign; no CVE, no IOC for Splunk-check, no A&D-prime victim, no tracked actor, no zero-day.

No FLASH escalation. Candidate for PM-28 16:00 brief as secondary content under the standing World Cup attack-surface theme (carry-forward from morning brief finding 0002), with the framing that FBI + Group-IB attribution rounds out the morning brief's Unit 42 Iran-only framing into a multi-actor multi-targeting picture.
