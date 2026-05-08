---
raw_id: raw-2026-05-08-pm-006
collected_at: 2026-05-08T15:40:00-04:00
run_id: pre-brief-20260508-153000
collection_mode: pre_brief_collection
test: false
sources:
  - source_yaml_id: securityweek
    source_name: "SecurityWeek (Eduard Kovacs)"
    source_url: https://www.securityweek.com/polish-security-agency-reports-ics-breaches-at-five-water-treatment-plants/
    source_grade_estimated: B
    role: relay_of_polish_government_advisory
    published_at: 2026-05-08T11:46:06+00:00
    note: |
      SecurityWeek relay of Polish Internal Security Agency (ABW)
      report. Primary source is the Polish ABW; SecurityWeek is the
      English-language relay.
publish_window: { start: 2026-05-08T07:30:00-04:00, end: 2026-05-08T15:30:00-04:00 }
match_reason:
  watchlist: []
  actors:
    - APT28        # in roster
    - APT29        # in roster
    - UNC1151      # NOT in roster (Belarusian-linked Ghostwriter operator)
  vulnerabilities: []
  keywords:
    - poland
    - abw
    - ics-breach
    - water-treatment
    - critical-infrastructure
    - hacktivist-persona
    - russian-intelligence
    - apt28
    - apt29
    - unc1151
    - ghostwriter
    - belarus
triage_tags:
  - tracked_actor_named
  - critical_infrastructure
  - non_us_critical_infra
  - foreign_government_advisory_relay
  - apt28_apt29_co_attribution
  - unc1151_actor_not_in_roster
  - non_ad_specific_geographic_pivot_relevant
flash_trigger_evaluation:
  trigger_1_critical_cve_exploited:
    decision: not_triggered
    rationale: |
      No CVE — ABW attributes the intrusions to "weak password policies
      and systems exposed directly to the internet." Operational
      hygiene failures, not a vulnerability.
  trigger_2_tracked_actor_attribution:
    evaluation: |
      Conditions:
      - article_attributes_activity_to_actor: PARTIAL — ABW says
        "hacktivist groups, though these are often personas used by
        foreign governments, particularly Russian intelligence services"
        and explicitly names "APT28, APT29, and Belarusian-linked
        UNC1151."
      - attributed_actor in _roster.yaml: TRUE for APT28 and APT29.
      - attribution_is_new_not_restatement: PARTIAL — APT28 and APT29
        operating against critical infrastructure is well-established.
        Polish ABW NAMING THEM specifically for these five 2025-26
        water-plant incidents IS new context. Question: does naming
        APT28/APT29 in a NEW victim set count as new attribution, or
        restatement of long-known TTP?
      Borderline judgment call. Defensible answer: yes, FLASH-2
      candidate — Polish ABW is a credible foreign-government
      attribution body, and APT28/APT29 explicitly named for
      operational technology / water-utility intrusions in Poland
      is a meaningful incremental signal.
    decision: candidate_borderline_grader_decides
    rationale: |
      Defensible FLASH-2 candidate. Tempering arguments:
      - Geographic pivot — Polish water utilities, not US/A&D-target
        profile. Briefer's A&D-relevance test will weight low.
      - "Hacktivist personas used by foreign governments" framing is
        common ABW language; not necessarily a fresh investigative
        finding.
      - APT28/APT29 already tracked HIGH; this does not change
        threat-box scoring.
      Recommend grader treat as FLASH-2 candidate but with strong
      preference for folding into 16:00 afternoon brief geo-pivot
      block (APT28/APT29 ICS targeting in NATO eastern flank). FLASH
      bar should reflect A&D-target relevance — Poland water is
      below that bar.
  trigger_3_first_party_ioc_hit:
    decision: not_triggered
    rationale: "Splunk archimedes/defenseclaw_local clean for these markers in 8h window; ABW report does not include IOCs in SecurityWeek relay."
  trigger_4_tracked_actor_ttp_change:
    evaluation: |
      Conditions:
      - source_grade A or B: SecurityWeek = B (provisional). Polish
        ABW primary = government source, treated as A-equivalent.
      - attributable: TRUE — APT28/APT29 named.
      - ttp_delta: AMBIGUOUS — APT28/APT29 ICS targeting not novel
        but the SCALE (5 water plants compromised) and specifics
        (modify operational parameters of equipment, "creating direct
        risk to public water supply") elevate impact framing.
    decision: candidate_borderline_grader_decides
    rationale: |
      Borderline FLASH-4. The TTP delta is "scale of ICS-modify
      capability achieved across 5 utilities" rather than a
      net-new tooling/targeting innovation. Grader judgment.
  trigger_5_ad_sector_campaign:
    decision: not_triggered
    rationale: "Water utilities, not A&D sector."
  trigger_6_zero_day_no_patch:
    decision: not_triggered
iocs_extracted: true
iocs_count: 6
text_word_count: 720
publication_window_match: in_window
promoted: true
promoted_to_finding: finding-2026-05-08-0009
promoted_at: 2026-05-08T16:32:00-04:00
ttl_expires_at: 2026-08-06T15:40:00-04:00
---

# Polish ABW reports five water-treatment ICS breaches; attributes to APT28, APT29, UNC1151

## Source summary

SecurityWeek published "Polish Security Agency Reports ICS Breaches at Five Water Treatment Plants" at 2026-05-08T11:46 UTC. SecurityWeek relays Poland's Internal Security Agency (ABW) report documenting ICS intrusions at five water treatment facilities during 2025. The ABW report attributes primary responsibility to "hacktivist groups, though these are often personas used by foreign governments, particularly Russian intelligence services" and explicitly names APT28, APT29, and Belarusian-linked UNC1151.

## Targets (per ABW via SecurityWeek)

Five water treatment stations in 2025:
1. Jabłonna Lacka
2. Szczytno
3. Małdyty
4. Tolkmicko
5. Sierakowo

Plus broader pattern of "increase in attacks targeting supply chains, critical infrastructure, and ICS at other types of municipal utilities, including wastewater treatment plants and waste incineration facilities."

## Attribution and tradecraft (per ABW via SecurityWeek)

> "attributed primary responsibility to hacktivist groups, though these are often personas used by foreign governments, particularly Russian intelligence services. Specific threat actors named include APT28, APT29, and Belarusian-linked UNC1151."

ABW identified two primary attack vectors:
1. **Weak password policies**
2. **Systems exposed directly to the internet**

Operational impact: "in some cases the attackers gained access to ICS and obtained the ability to modify the operational parameters of equipment, creating a direct risk to operational continuity and the public water supply."

## Tracked actor activity

- **APT28** (id 006 in _roster.yaml, GRU Unit 26165): Russian state APT, ICS history includes Ukrainian power grid (BlackEnergy via Sandworm sister-unit) — ICS targeting for APT28 itself is less well-documented than Sandworm, so naming APT28 specifically for ICS-modify in Polish water utilities is incrementally notable.
- **APT29** (id 009 in _roster.yaml, SVR): Cozy Bear / Midnight Blizzard. Espionage-focused historically; ICS targeting attribution is less common — also incrementally notable.
- **UNC1151** (Belarusian-linked, also known as Ghostwriter operator): NOT in current _roster.yaml. Strong candidate for actor intake.

## A&D target profile relevance

**Direct relevance: low.** Polish water utilities are not A&D primes; geography (Poland) is also outside US-target frame.

**Indirect relevance: meaningful.**
- APT28 and APT29 are tracked HIGH per _roster.yaml; their TTP and tooling apply globally including against US A&D primes.
- "Hacktivist persona used by foreign government" framing is the same operating model that has repeatedly surfaced in US-targeting (e.g., Iran's MOIS using Handala Hack persona, GRU using various hacktivist fronts).
- Critical-infrastructure ICS-modify capability achieved via "weak password policies and systems exposed directly to the internet" — the same hygiene failure modes apply to A&D-prime SCADA/OT environments. Briefer's analyst should pull this for the geo-pivot block as a posture/hygiene reminder for A&D OT teams.

## Anti-noise observation

First Polish-water-utility coverage in Archimedes corpus this cycle. Geographic pivot piece — clusters with morning brief's APT28/APT29 watch but is itself fresh signal.

## Extraction notes

- Language: en (relay of Polish-language ABW publication)
- Article type: media (SecurityWeek relay of foreign-government advisory)
- Publisher byline: Eduard Kovacs
- Raw IOC extraction invoked: yes

## IOCs

```yaml
iocs:
  - type: actor_alias
    value: "APT28"
    canonical_id: "006"
    role: tracked_actor_named
    notes: "Roster id 006 (GRU Unit 26165). Named by ABW as one of the actors behind 2025 Polish water-utility ICS intrusions."
    sources: [securityweek-relay, abw-primary]

  - type: actor_alias
    value: "APT29"
    canonical_id: "009"
    role: tracked_actor_named
    notes: "Roster id 009 (SVR). Named by ABW alongside APT28."
    sources: [securityweek-relay, abw-primary]

  - type: actor_alias_candidate
    value: "UNC1151"
    role: untracked_actor_named
    aliases_known: ["Ghostwriter (operator)", "TA445"]
    attribution: "Belarusian-linked per ABW; Mandiant has historically attributed UNC1151 to Belarusian KGB"
    notes: |
      Not in current _roster.yaml. Candidate for /new-actor intake.
      Ghostwriter information operations + UNC1151 cyber operations
      have a long history against NATO eastern flank.
    sources: [securityweek-relay, abw-primary]

  - type: target_geography
    value: "Poland — water treatment utilities (5 facilities); 2025"
    role: incident_targets
    facilities: ["Jabłonna Lacka", "Szczytno", "Małdyty", "Tolkmicko", "Sierakowo"]
    sources: [securityweek-relay, abw-primary]

  - type: ttp_pattern
    value: "Hacktivist persona used as front for state-sponsored intrusion; weak password policies + internet-exposed ICS"
    role: ttp
    notes: "ABW characterization. Pattern is well-known but ICS-modify outcome elevates impact."
    sources: [abw-primary]

  - type: ttp_outcome_signal
    value: "Modify operational parameters of ICS equipment — risk to public water supply"
    role: impact
    notes: "ABW direct claim. ICS-modify, not just data theft."
    sources: [abw-primary]

attribution_claims:
  - claim_text: "primary responsibility to hacktivist groups, though these are often personas used by foreign governments, particularly Russian intelligence services. Specific threat actors named include APT28, APT29, and Belarusian-linked UNC1151"
    claim_source: abw_via_securityweek
    claim_confidence: foreign_government_advisory_attribution
    claim_date: 2026-05-08
    notes: |
      ABW = Poland's Internal Security Agency. Foreign-government
      attribution body, treated as A-equivalent for Polish-domestic
      incidents. Cross-cites APT28, APT29, UNC1151 by canonical name.
      Strong attribution language despite hedge ("often personas").
```
