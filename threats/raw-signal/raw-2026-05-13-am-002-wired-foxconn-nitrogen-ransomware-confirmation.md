---
raw_id: raw-2026-05-13-am-002
collected_at: 2026-05-13T07:32:00-04:00
run_id: pre-brief-20260513-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: wired-security
  source_name: Wired (security desk; grade B per source-grades.yaml)
  source_url: https://www.wired.com/story/foxconn-ransomware-attack-shows-nothing-is-safe-forever/
  source_byline: Lily Hay Newman
  published_at: 2026-05-12T21:52:05+00:00     # 17:52 EDT 2026-05-12, just inside 14h pre-brief window
  fetched_via: wired_rss_feed_metadata_plus_websearch_cross_corroboration  # Wired.com body fetch blocked by Claude Code; corroboration via WebSearch + other publications
  fetched_at: 2026-05-13T07:32:00-04:00
secondary_sources_via_websearch_cross_corroboration:
  - source_id: the-record
    source_url: https://therecord.media/foxconn-confirms-cyberattack-north-american-factories
    source_grade: B
    role: foxconn_first_party_confirmation_corroborating_source
  - source_id: the_register
    source_url: https://www.theregister.com/cyber-crime/2026/05/12/foxconn-confirms-cyberattack-after-nitrogen-claims-apple-nvidia-data-theft/5239144
    source_grade: B_uk_tech_press_named_byline_track_record
    role: nitrogen_claim_detail_corroboration
    note: "First Archimedes-corpus surface for The Register. Provisional B on first surface per UK-tech-press-track-record precedent (no prior corpus citations; The Register has a strong long-running track record on UK cybercrime / ransomware coverage with named-staff bylines). Operator may ratify upon source-grade-log review."
  - source_id: 9to5mac
    source_url: https://9to5mac.com/2026/05/12/apple-supplier-foxconn-confirms-ransomware-attack-affected-north-american-factories/
    source_grade: B_apple_focused_tech_press_named_byline
    role: foxconn_apple_supplier_context_corroboration
    note: "First Archimedes-corpus surface for 9to5Mac. Provisional B on first surface — Apple-focused tech publication with named-staff bylines. Operator may ratify upon source-grade-log review."
  - source_id: focus_taiwan
    source_url: https://focustaiwan.tw/business/202605130008
    source_grade: B_taiwan_government_news_service_official_publication
    role: foxconn_taiwan_jurisdiction_first_party_context
    note: "First Archimedes-corpus surface for Focus Taiwan. Provisional B on first surface — Taiwan's official-government-news-service-equivalent publication; Foxconn is Taiwan-headquartered so Focus Taiwan carries jurisdiction-proximate coverage value. Operator may ratify upon source-grade-log review."
  - source_id: cybernews
    source_url: https://cybernews.com/security/foxconn-data-breach-apple-nvidia-partner/
    source_grade: C_provisional_first_surface_unknown_cybersec_news_aggregator
    role: 11m_files_8tb_data_volume_claim_corroboration
    note: "First Archimedes-corpus surface for Cybernews. Provisional C on first surface per LayerX / Seqrite / Trendyol precedent (conservative starting grade for unknown cybersecurity-news aggregators). Operator may ratify upon source-grade-log review."
  - source_id: ransomware_live
    source_url: https://www.ransomware.live/id/Rk9YQ09OTkBuaXRyb2dlbg
    source_grade: C_provisional_first_surface_ransomware_tracker_aggregator
    role: nitrogen_leak_site_victim_listing_aggregator
    note: "Ransomware.live is a passive ransomware leak-site aggregator. C provisional on first surface — useful for claim corroboration but not original-research source. Operator may ratify upon source-grade-log review."
  - source_id: redpacket_security
    source_url: https://www.redpacketsecurity.com/nitrogen-ransomware-victim-foxconn/
    source_grade: C_provisional_first_surface
    role: nitrogen_leak_site_relay
match_reason:
  watchlist: []
  watchlist_match_strength: structural_adjacency_via_manufacturing_sector_supply_chain_proximity
  watchlist_match_detail: |
    Foxconn (Hon Hai Precision Industry Co. Ltd.; Taiwan-headquartered)
    is NOT on aerospace-defense.yaml watchlist. Foxconn is the world's
    largest electronics manufacturing services (EMS) provider; primary
    business is consumer-electronics contract manufacturing (Apple
    iPhone assembly being the most visible) and server/networking/data-
    center hardware. Foxconn Industrial Internet (FII) operates
    industrial-IoT and intelligent-manufacturing platforms but does
    NOT have a publicly-disclosed defense-contracting line of business
    comparable to a Tier-1 A&D prime.

    Nitrogen leak claims name commercial-tech customers in the stolen
    data: Intel, Apple, Google, Dell, Nvidia. NO A&D primes (no
    Lockheed, Boeing, RTX, Northrop, GD, BAE, L3Harris, Leidos, SAIC,
    Thales, GE Aerospace, Safran, Honeywell, Airbus, Elbit).

    Structural adjacency exists at the manufacturing-sector level —
    Foxconn manufactures server / networking / computing hardware that
    touches the broader US tech supply chain (Apple silicon, Nvidia
    GPU board manufacturing, Dell server assembly). A&D primes' SDLC
    and procurement teams source from this same manufacturing
    ecosystem at the hardware-component level. The Mount Pleasant
    Wisconsin facility outage 2026-05-01 is electronics manufacturing,
    not defense manufacturing.

    RAW-SIGNALED per the same structural-adjacency-by-disclosure test
    that surfaced 2026-05-11 SecurityWeek HookedWing (raw-2026-05-11-
    flash-0000-001) as a non-FLASH grader-queue item — not because
    it's a FLASH but so the grader has the supply-chain / manufacturing-
    sector signal in the queue for cluster evaluation.
  actors: []
  actors_attribution_note: |
    Nitrogen ransomware (NOT in _roster.yaml). Per cross-corroborated
    WebSearch:
      - Active since 2023
      - Conti-2-builder code lineage (one of multiple ransomware
        offshoots derived from the leaked Conti 2 builder)
      - Possible BlackCat / ALPHV affiliation per code-sharing analysis
      - Double-extortion model (encrypt + steal + leak-site publication)
      - Historical Foxconn-target context: NOT first Foxconn ransomware
        attack — December 2020 DoppelPaymer hit Foxconn Mexico (1,804
        BTC ransom demand), May 2022 LockBit hit a different Foxconn
        Mexico facility, 2024 LockBit hit subsidiary Foxsemicon
        Integrated Technology. Nitrogen 2026-05-11 is the FOURTH
        ransomware attack against Foxconn since 2020.

    Nitrogen flagged as potential /new-actor candidate for operator
    review. The Conti-2-builder code lineage + possible BlackCat/ALPHV
    affiliation + multi-year track record since 2023 + Foxconn-target
    escalation pattern is enough to warrant a profile if the operator
    chooses to track.

    SecurityWeek + Wired + The Record + The Register + 9to5Mac all
    name Nitrogen as the claimed actor; criminal-source claim grade
    per LEGAL-POLICY is F for the actor self-claim, but the cross-
    corroboration by multiple B-grade media outlets relaying the
    leak-site listing makes the procedural fact (Nitrogen claimed
    Foxconn) A1. Foxconn's own confirmation of the cyberattack
    (without confirming the Nitrogen claim specifically) is A1
    first-party.
  vulnerabilities: []        # No CVE attached to the Nitrogen attack chain in public reporting at this disclosure point; initial-access vector not yet specified
  keywords:
    - foxconn_hon_hai_precision_industry
    - nitrogen_ransomware_2023_active
    - conti_2_builder_code_lineage
    - blackcat_alphv_possible_affiliation
    - double_extortion_raas_class
    - mount_pleasant_wisconsin_facility_outage
    - 8tb_data_theft_11m_files
    - apple_intel_google_dell_nvidia_data_claim
    - electronics_manufacturing_sector
    - foxconn_industrial_internet_fii
    - foxsemicon_2024_lockbit_historical_context
    - foxconn_mexico_2020_doppelpaymer_2022_lockbit_historical_context
    - potential_new_actor_candidate_nitrogen
    - structural_ad_adjacency_manufacturing_supply_chain
triage_tags:
  - manufacturing_sector_adjacent_supply_chain
  - foxconn_not_on_ad_watchlist
  - nitrogen_not_in_roster_potential_new_actor_candidate
  - electronics_manufacturing_not_defense_manufacturing
  - multi_source_cross_corroboration_strong
  - non_flash_grader_discretion_for_morning_brief
  - no_named_ad_prime_customer_in_leak_claims
  - conti_2_builder_lineage_blackcat_alphv_possible_affiliation
flash_trigger_evaluation:
  trigger_1_critical_cve_exploited:
    matched: false
    rationale: |
      No CVE attached to the Nitrogen attack chain in public reporting
      at this disclosure point. Ransomware-class initial-access vector
      not specified (Foxconn confirmed cyberattack but has not disclosed
      vector; Nitrogen leak-site claims do not specify CVE exploitation
      as the entry path).
  trigger_2_tracked_actor_attribution:
    matched: false
    rationale: |
      Nitrogen is NOT in _roster.yaml. Potential /new-actor candidate
      flagged for operator review, but Trigger 2 evidence-minimum
      requires attribution to a tracked actor.
  trigger_3_first_party_ioc_hit:
    matched: false
    rationale: |
      Splunk archimedes + defenseclaw_local indices searched for
      "Foxconn" + "Nitrogen" tokens over 24h — zero matches. Twenty-
      first consecutive dormant non-archimedes-internal stream sweep.
      Trigger 3 cannot fire on dormant stream.
  trigger_4_tracked_actor_ttp_change:
    matched: false
    rationale: |
      Nitrogen is NOT a tracked actor. TTPs reported (double-extortion
      RaaS with Conti-2-builder lineage) are not new to the Nitrogen
      threat-actor class itself; the Foxconn-target represents
      escalation in target-size NOT capability-evolution.
  trigger_5_ad_sector_campaign:
    matched: false
    rationale: |
      Foxconn is NOT on aerospace-defense.yaml watchlist. Named-
      customer leak data is commercial-tech (Intel, Apple, Google,
      Dell, Nvidia), NOT A&D primes. Multi-victim claim is Foxconn-
      internal only at this disclosure point; the customer-data
      claims are derivative (data ALLEGEDLY pertaining to Intel/
      Apple/Google/Dell/Nvidia, not separate-victim breach claims
      against those companies). Trigger 5 evidence-minimum (multi-
      victim confirmed + A&D-prime-or-watchlist-entity targeted)
      FAILS on both criteria.
  trigger_6_zero_day_no_patch:
    matched: false
    rationale: |
      Not a vulnerability disclosure. Ransomware-class extortion event.
  net: NON-FLASH. Grader-queue item for 2026-05-13 08:00 morning brief
       at grader discretion.

grader_disposition_recommendation: |
  NON-FLASH. Grader discretion on inclusion in 08:00 morning brief.

  Two viable dispositions:

  (A) SKIP from morning brief — Foxconn is not on watchlist, Nitrogen
      is not in roster, no CVE nexus, no A&D-prime customer-impact
      claim from Nitrogen. The structural adjacency (manufacturing-
      sector supply chain) is weak signal for an A&D-prime-focused
      brief.

  (B) INCLUDE as sidebar / supply-chain-watch observation. Frame as
      "Foxconn confirmed cyberattack 2026-05-12; Nitrogen claimed 8TB
      / 11M files including commercial-tech customer data; FOURTH
      Foxconn ransomware attack since 2020 (DoppelPaymer 2020,
      LockBit 2022, LockBit 2024, Nitrogen 2026); no A&D-prime
      customer naming in Nitrogen claims; A&D primes' EMS-procurement
      and SDLC teams may want to monitor for follow-on data-leak
      content if and when Nitrogen publishes the full 8TB to a leak
      site."

  RECOMMEND (B) — include as a tight sidebar. The Foxconn name carries
  enough operational significance (Tier-1 EMS provider serving the
  global tech manufacturing ecosystem) that A&D primes' supply-chain
  and procurement security teams may want to be aware. The historical-
  context (four Foxconn ransomware attacks since 2020) carries pattern-
  recognition value for the manufacturing-sector-as-soft-target
  observation.

  Operator awareness flag — Nitrogen is a potential /new-actor
  candidate. The 2023-active timeline + Conti-2-builder code lineage +
  possible BlackCat/ALPHV affiliation + Foxconn-target escalation makes
  the actor worth profiling if the operator chooses. Per /new-actor
  workflow standard, this would warrant a 7-day first-pass profile and
  14-day threat-box scoring window.

ad_relevance_assessment: |
  STRUCTURAL LOW-MEDIUM via manufacturing-sector adjacency.

  Foxconn is NOT a tracked A&D prime. The named-customer leak data is
  commercial-tech (Intel, Apple, Google, Dell, Nvidia). A&D primes do
  NOT appear in the public Nitrogen claim.

  However, the broader manufacturing-sector / EMS / supply-chain
  context is operationally relevant:
    - Foxconn manufactures server / networking / computing hardware
      that touches the US tech supply chain at the component-assembly
      level
    - A&D primes' SDLC teams source compute / network hardware from
      the same EMS ecosystem (Dell servers, Nvidia GPUs in compute
      clusters, etc.)
    - The historical-context pattern (four Foxconn ransomware attacks
      since 2020) suggests EMS providers are repeated soft-targets
      for double-extortion RaaS groups

  This is "watch the supply chain" intelligence, not a direct A&D-
  threat signal. Forward-looking awareness for the orchestrator: if
  Nitrogen publishes the full 8TB leak content and that content
  surfaces evidence of A&D-prime-component-procurement details, the
  ad_relevance shifts upward to MEDIUM.

historical_context_foxconn_prior_ransomware_attacks:
  - december_2020:
      actor: DoppelPaymer
      facility: Foxconn Mexico
      ransom_demand: 1804_btc
      outcome: not_publicly_disclosed
  - may_2022:
      actor: LockBit
      facility: Foxconn Mexico (different facility from 2020)
      outcome: not_publicly_disclosed
  - 2024:
      actor: LockBit
      facility: Foxsemicon Integrated Technology (Foxconn subsidiary)
      attack_type: defacement_plus_data_breach_claim
      outcome: not_publicly_disclosed
  - 2026_05_11:
      actor: Nitrogen
      facility_outage: Mount_Pleasant_Wisconsin (surfaced 2026-05-01)
      ransom_demand: not_publicly_disclosed
      data_claimed_stolen: 8_TB_11_million_files
      customer_data_claimed: Intel_Apple_Google_Dell_Nvidia
      foxconn_confirmation_date: 2026-05-12
      foxconn_confirmation_scope: cyberattack_confirmed_no_explicit_nitrogen_acknowledgment

promoted: true
promoted_to_finding: finding-2026-05-13-0002
promoted_at: 2026-05-13T08:18:00-04:00
promoted_grading_run_id: morning-20260513-080000
promoted_disposition: manufacturing_sector_ems_supply_chain_adjacency_monitoring_sidebar
---

# Foxconn Cyberattack Confirmation 2026-05-12 + Nitrogen Ransomware Claim

**Wired primary publication:** 2026-05-12T21:52:05+00:00 (17:52 EDT)
**Wired byline:** Lily Hay Newman
**Wired URL:** https://www.wired.com/story/foxconn-ransomware-attack-shows-nothing-is-safe-forever/
**Wired body fetch:** BLOCKED by Claude Code WebFetch tool (Wired.com fetches
  return 403 / blocked status per prior 2026-05-09 source-health note;
  corroboration this sweep via WebSearch + RSS feed metadata + multiple
  cross-corroborating publication URLs)

**Cross-corroborating publications (WebSearch results):**

- The Record (Recorded Future News, B-grade media): "Foxconn confirms
  cyberattack impacting North American factories" — corroborates Foxconn
  first-party confirmation
- The Register (UK tech press, provisional B on first surface): "Foxconn
  confirms cyberattack after ransomware crew claims it stole confidential
  Apple, Nvidia files" — relays Nitrogen claim detail
- 9to5Mac (Apple-focused tech press, provisional B on first surface):
  "Apple supplier Foxconn confirms ransomware attack affected North
  American factories"
- AppleInsider: "Hackers attack Foxconn again, Apple doesn't appear to be
  at risk" — Apple-customer-data-risk-assessment framing
- Focus Taiwan (Taiwan's official-government-news-service-equivalent,
  provisional B): "Foxconn confirms cyberattack on North American
  facilities" — Taiwan-jurisdiction first-party context
- Cybernews (provisional C on first surface): "Major Apple partner
  Foxconn allegedly breached with 11M files stolen"
- ThreatAft (security blog): "Nitrogen Ransomware Hits Foxconn Wisconsin:
  8TB Data Breach – Full Analysis"
- Ransomware.live (passive ransomware-tracker aggregator): victim
  listing entry for Foxconn under Nitrogen leak site
- RedPacket Security: Nitrogen Ransomware Victim Foxconn aggregation

## Cross-Corroborated Facts

**Attack timeline:**
- 2026-05-01 (Friday) — Workers at Mount Pleasant Wisconsin facility
  reported a "full network collapse"
- 2026-05-11 (Monday) — Nitrogen ransomware group claimed Foxconn on
  its leak site, claiming 8 TB / 11 million files stolen
- 2026-05-12 (Tuesday) — Foxconn officially confirmed cyberattack
  impacting North American factories (Foxconn did not specifically
  confirm the Nitrogen claim or the 8 TB / 11M files figure)
- 2026-05-12T21:52 UTC — Wired published Lily Hay Newman editorial
  framing the attack as "nothing is safe forever"

**Nitrogen ransomware group details (cross-corroborated):**
- Active since 2023
- Conti-2-builder code lineage (one of several ransomware offshoots
  derived from the leaked Conti 2 builder)
- Possible BlackCat / ALPHV affiliation per code-sharing analysis (not
  definitive)
- Double-extortion model (encrypt + steal + leak-site publication)

**Claimed stolen data scope:**
- 8 TB volume
- 11 million files
- Customer-data subjects named: Intel, Apple, Google, Dell, Nvidia
- Content categories claimed: "confidential instructions, internal
  project documentation, and technical drawings related to projects"

**Historical context — Foxconn prior ransomware attacks:**
- December 2020: DoppelPaymer hit Foxconn Mexico (1,804 BTC ransom)
- May 2022: LockBit hit a different Foxconn Mexico facility
- 2024: LockBit hit Foxsemicon Integrated Technology (Foxconn subsidiary)
- 2026-05-11: Nitrogen Foxconn Wisconsin (this event)

## Important Negative Findings

- **NO named A&D prime customer in Nitrogen's claims.** No Lockheed,
  Boeing, RTX, Northrop, GD, BAE, L3Harris, Leidos, SAIC, Thales, GE
  Aerospace, Safran, Honeywell, Airbus, Elbit appears in the claimed
  stolen-data customer naming. Named customers are all commercial-tech.

- **Foxconn is NOT on aerospace-defense.yaml watchlist.** Foxconn is
  the world's largest EMS provider but its primary business is
  consumer-electronics contract manufacturing (Apple iPhone assembly).
  Foxconn Industrial Internet (FII) operates industrial-IoT platforms
  but does not have a publicly-disclosed defense-contracting line.

- **Nitrogen is NOT in _roster.yaml.** Potential /new-actor candidate
  flagged for operator review.

- **No CVE attached to the attack chain in public reporting.**
  Ransomware-class initial-access vector not specified at this
  disclosure point.

## Why Raw-Signaled Despite Not-on-Watchlist + Not-in-Roster

Per the same structural-adjacency-by-disclosure test that surfaced
2026-05-11 SecurityWeek HookedWing 500+ org phishing campaign (raw-2026-
05-11-flash-0000-001) as a non-FLASH grader-queue item, this Foxconn /
Nitrogen confirmation gets raw-signaled NOT because it's a FLASH or a
high-priority A&D-direct threat but because:

1. **Manufacturing-sector supply-chain adjacency** to A&D primes via
   EMS procurement (Dell servers, Nvidia GPUs, Intel CPUs, Apple silicon
   all touch A&D-prime SDLC at the hardware-component level)
2. **Historical pattern recognition** — four Foxconn ransomware attacks
   since 2020 with consistent escalation in target-facility-size and
   data-volume claims
3. **Nitrogen as potential /new-actor candidate** with Conti-2-builder
   code lineage + possible BlackCat/ALPHV affiliation
4. **Forward-looking watch signal** — if Nitrogen publishes the full 8TB
   leak content and that content surfaces evidence of A&D-prime-
   component-procurement detail, the ad_relevance shifts upward

The grader at 08:00 has discretion to either SKIP from morning brief or
INCLUDE as a tight sidebar / supply-chain-watch observation. The
recommended disposition is INCLUDE as sidebar.

---

## Extraction Notes

- **Language:** en
- **Publisher byline:** Lily Hay Newman (Wired senior writer; named-byline
  with prior tech-security track record on Wired)
- **Article type:** editorial / feature commentary on ransomware-target
  ecosystem with Foxconn-specific historical pattern framing
- **Raw IOC extraction invoked:** yes (per ioc-extraction skill SKILL.md)
- **Wired body fetch blocked:** Yes — Claude Code WebFetch tool cannot
  retrieve www.wired.com content; this raw-signal relies on RSS feed
  metadata (Wired's RSS feed returned the title + URL + publication
  date + summary) + multi-source WebSearch cross-corroboration.

## IOCs (from ioc-extraction skill)

```yaml
cves: []   # No CVE attached to the Nitrogen attack chain in public reporting at this disclosure point

domains:
  - foxconn.com                                # Foxconn primary corporate domain (victim, not IOC)
  - foxsemicon.com.tw                          # Foxsemicon subsidiary (referenced historical 2024 LockBit context)

ips: []
hashes: []
emails: []
yara: []

actor_claims:
  - actor_name: "Nitrogen"
    in_roster: false
    aliases_observed:
      - "Nitrogen ransomware"
      - "Nitrogen ransomware crew"
    claim_source: "Nitrogen leak site (criminal-source F-grade per LEGAL-POLICY for actor claim itself)"
    claim_corroboration: "B-grade media cross-corroboration from The Record + The Register + 9to5Mac + Wired + Focus Taiwan = A1 procedural fact (Nitrogen claimed Foxconn)"
    actor_classification: "Cybercriminal (RaaS) — Conti-2-builder lineage, possible BlackCat/ALPHV affiliation"
    actor_active_since: "2023"
    new_actor_candidate_flag: true
    proposed_threat_level_if_added_to_roster: "MEDIUM — placeholder pending /new-actor profile + threat-box scoring; would benchmark against LockBit / BlackCat / Cl0p RaaS-class comparators"

victim_claims:
  - victim_name: "Foxconn (Hon Hai Precision Industry Co. Ltd.)"
    confirmed_by_victim: true
    confirmation_date: 2026-05-12
    confirmation_scope: "cyberattack_confirmed_no_explicit_nitrogen_acknowledgment_no_explicit_data_volume_acknowledgment"
    facility_affected: "Mount Pleasant Wisconsin (primary; possible other North American facilities per Foxconn statement)"
    sector: "Electronics manufacturing services (EMS) / Contract electronics manufacturing"
    on_watchlist: false
  - victim_data_subjects_claimed_by_nitrogen:
      - "Intel"
      - "Apple"
      - "Google"
      - "Dell"
      - "Nvidia"
    note: "These are CUSTOMER data subjects whose data is allegedly within the 8TB leak, NOT separate-victim breach claims. None on aerospace-defense.yaml watchlist. None confirmed the data-theft claim."

attribution_claims:
  - claim: "Nitrogen has been around since 2023 and is believed to be one of the various ransomware offshoots that borrowed code from the leaked Conti 2 builder"
    source_grade: B_cross_corroborated_websearch_relay_from_security_research_analyses
    claim_type: actor_lineage_assertion
  - claim: "the group seems to have ties to the BlackHat/ALPHV ransomware"
    source_grade: C_speculative_per_seems_to_have_ties_hedge_language
    claim_type: actor_affiliation_assertion_speculative
  - claim: "8 TB of data comprising more than 11 million files"
    source_grade: F_nitrogen_leak_site_self_claim_criminal_source
    claim_type: data_volume_self_claim
    independent_verification: pending
  - claim: "leaks include confidential instructions, internal project documentation, and technical drawings related to projects at Intel, Apple, Google, Dell, and Nvidia"
    source_grade: F_nitrogen_leak_site_self_claim_criminal_source
    claim_type: customer_data_self_claim
    independent_verification: pending_no_named_customer_has_confirmed
  - claim: "Foxconn confirmed cyberattack impacting North American factories"
    source_grade: A1_foxconn_first_party_confirmation_cross_corroborated_by_b_grade_media
    claim_type: cyberattack_procedural_fact
    independent_verification: confirmed_multi_source

historical_context_actor_attribution:
  - 2020_12_doppelpaymer_foxconn_mexico:
      grade: A_foxconn_mexico_acknowledged_event_doppelpaymer_named_in_contemporaneous_reporting
  - 2022_05_lockbit_foxconn_mexico:
      grade: A_lockbit_named_contemporaneous_reporting
  - 2024_lockbit_foxsemicon:
      grade: B_lockbit_subsidiary_defacement_breach_claim_event

mitre_attack_techniques_referenced: []
mitre_attack_inferred_from_class:
  - T1486_Data_Encrypted_for_Impact            # ransomware class
  - T1567_Exfiltration_Over_Web_Service         # double-extortion data-theft class
  - T1657_Financial_Theft                        # ransom-demand class
  # initial-access TTP unspecified at this disclosure point

a_d_prime_named_as_victim_or_target: false
multi_victim_signal_within_ad_sector: false
splunk_first_party_archimedes_index_hits: 0
splunk_first_party_defenseclaw_local_index_hits: 0
splunk_query_window: -24h
splunk_dormant_consecutive_sweeps: 21
```

## Grader Notes

This raw-signal is positioned as a manufacturing-sector adjacent supply-
chain observation for the 08:00 morning brief grader queue. Grader
discretion on inclusion. Recommended disposition: INCLUDE as tight
sidebar / supply-chain-watch observation. See grader_disposition_
recommendation in frontmatter.

Operator awareness flag: **Nitrogen** is a potential /new-actor candidate.
The 2023-active timeline + Conti-2-builder code lineage + possible
BlackCat/ALPHV affiliation + Foxconn-target escalation makes the actor
worth profiling if the operator chooses to track. Per /new-actor workflow
standard, profile creation would warrant a 7-day first-pass + 14-day
threat-box scoring window.

Cross-corroboration is strong: Wired + The Record + The Register +
9to5Mac + Focus Taiwan + Cybernews + AppleInsider all cover the same
core facts (Foxconn confirmed cyberattack 2026-05-12; Nitrogen leak-
site claim 2026-05-11; 8 TB / 11M files; Intel + Apple + Google + Dell
+ Nvidia customer-data scope). Procedural-fact grading is A1 for the
cyberattack confirmation and for the Nitrogen-claimed-Foxconn fact;
the data-volume and customer-data claims themselves are F per LEGAL-
POLICY (criminal-source self-claims) pending independent verification.

The Wired body fetch was blocked by Claude Code's WebFetch tool (the
2026-05-09 source-health note documents this limitation for www.wired.
com fetches). This raw-signal therefore relies on RSS feed metadata +
multi-source WebSearch cross-corroboration for the full content
reconstruction. If the operator wants the full Wired body, manual
browser retrieval may be needed.
