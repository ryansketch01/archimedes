---
raw_id: raw-2026-05-07-pm-007
collected_at: 2026-05-07T15:46:00-04:00
run_id: pre-brief-20260507-153000
collection_mode: pre_brief_collection
test: false
sources:
  - source_yaml_id: the-record
    source_name: "The Record (Alexander Martin)"
    source_url: https://therecord.media/polish-intelligence-warns-hackers-attacked-water-treatment
    source_grade_estimated: B
    role: originating
    published_at: 2026-05-07T12:38:00-04:00
    note: |
      Polish Internal Security Agency (ABW) public report on cyberattacks
      against water-treatment industrial control systems in five Polish
      towns: Jabłonna Lacka, Szczytno, Małdyty, Tolkmicko, Sierakowo.
      Plus prior attacks against Polish national railway, air traffic
      control, state news agency PAP, and energy infrastructure.
      ABW attributes "with particular emphasis on the special services
      of the Russian Federation" but does NOT publicly cross-walk to
      specific tracked actors. PM Donald Tusk warned of "ruthless"
      action against Russian-aiding entities. CyberDefence24 (relayed
      by The Record) links to a "pro-Russian hacktivist group" not named.
      No specific tracked-actor naming (Sandworm, APT28, APT29). No
      A&D entity named. Critical-infrastructure context for Poland as
      Western military-aid logistics hub.
match_reason:
  watchlist: []
  actors: []   # ABW does not name tracked actors; Hard Rule 2 forbids origination
  vulnerabilities: []
  keywords: [poland, abw, internal-security-agency, water-treatment, ics, ot, russian-state-services, sandworm-context, critical-infrastructure, military-aid-hub, donald-tusk]
triage_tags: [critical_infrastructure_attack, ot_ics_compromise, russian_attribution_general, no_specific_actor_named, ad_relevance_inferential, tracked_actor_candidate_unconfirmed]
iocs_extracted: true
iocs_count: 0
text_word_count: 360
promoted: true
promoted_to_finding: finding-2026-05-07-0005
promoted_at: 2026-05-07T16:17:00-04:00
promoted_by: grader
promoted_grading_run_id: afternoon-20260507-160000
ttl_expires_at: 2026-08-05T15:46:00-04:00
---

# Polish ABW publicly reports Russian-attributed cyberattacks on water-treatment ICS in five Polish towns — no tracked-actor name, no IOCs

## Source summary

The Record (Alexander Martin, "Polish intelligence warns hackers attacked water treatment control systems," 2026-05-07 12:38 EDT) reports that Poland's Internal Security Agency (ABW) has publicly disclosed cyberattacks on water-treatment industrial control systems across five Polish municipalities. Per ABW: "Attackers, gaining access in some cases to industrial control systems, had the ability to alter technical parameters of devices" — describing a "direct risk" to water-supply continuity.

Quote (under 15-word limit): "with particular emphasis on the special services of the Russian Federation."

## What this signal represents

**Targets named (water treatment):** Jabłonna Lacka, Szczytno, Małdyty, Tolkmicko, Sierakowo

**Targets named (broader 2024-2025 campaign per ABW):**
- Polish national railway
- Polish air traffic control system
- Polish state news agency (PAP)
- Polish energy infrastructure

**Attribution language (ABW):**
- "Intensified hostile cyber activity in 2024 and 2025"
- "with particular emphasis on the special services of the Russian Federation"

**Attribution language (Prime Minister Donald Tusk):**
- Will act "ruthlessly" toward those "directly or indirectly aiding Russian services"

**Attribution language (CyberDefence24, relayed by The Record):**
- Links to a "pro-Russian hacktivist group" (specific group not named in The Record's article)

## What this source does NOT add

- **No tracked-actor name.** ABW does NOT publicly attribute to Sandworm (007), APT28 (006), or APT29 (009) — the three Russian state-services tracked actors in `_roster.yaml`. Archimedes does NOT originate the cross-walk. Hard Rule 2 holds even where the inference may seem strong (Sandworm-class TTPs against Polish OT match historical Sandworm playbook precisely, but ABW does not say so publicly).
- **No IOCs.** No IPs, no domains, no hashes, no malware family names disclosed in The Record's reporting.
- **No CVE referenced.** No specific vulnerability disclosure.
- **No A&D entity.** Polish military-aid logistics is mentioned as context (Poland as logistics hub for Western military aid to Ukraine), but no specific defense contractor, A&D prime, or watchlist entity named.

## Why this matters for the afternoon brief — A&D adjacency

Inferential A&D-relevance:
1. Poland is the principal land-route hub for US/EU military aid to Ukraine. A&D primes (Lockheed Martin Javelin and HIMARS deliveries, RTX Patriot deliveries) transit Polish logistics infrastructure routinely.
2. Russian targeting of Polish OT (water, rail, air traffic, energy) maps to a sustained interdiction-of-aid campaign — same operational logic that historically drives Sandworm targeting of Ukrainian critical infrastructure.
3. Tier-1/2 A&D suppliers operating in or transiting Poland may face downstream OT-disruption risk. Not source-stated; recorded for the briefer to consider whether to surface in the standing A&D section as adjacent context.

## Why this is a scheduled-brief item, NOT a FLASH

Trigger evaluation:
- **Trigger-1 (critical-cve-exploited):** No CVE involved. Fails.
- **Trigger-2 (tracked-actor-attribution):** ABW does not name a tracked actor. Fails.
- **Trigger-3 (first-party-ioc-hit):** No IOCs to query. Fails.
- **Trigger-4 (tracked-actor-ttp-change):** Inferential Sandworm-class TTPs but no source attribution. Fails.
- **Trigger-5 (ad-sector-campaign):** No A&D entity targeted (per source). Fails.
- **Trigger-6 (zero-day-no-patch):** No CVE involved. Fails.

This is a context-rich scheduled-brief item, valuable in the standing A&D section as adjacent infrastructure-targeting signal, but not a FLASH.

## Recommendation for actor-profiler

The ABW attribution to "Russian special services" is consistent with all three Russian roster actors' historical TTPs but is too general to support cross-walking. The next-actor refresh on Sandworm (007), APT28 (006), or APT29 (009) — whichever is reviewed earliest — should note this Polish OT campaign as **possible-but-unconfirmed-attribution** context.

If a second source (e.g., Mandiant, CrowdStrike, ESET, Microsoft MSTIC) emerges with specific tracked-actor attribution, this raw-signal becomes a corroboration anchor.

---

## Extraction notes

- Language: en
- Article type: secondary news reporting (B-grade), citing ABW public statement (A-grade government source — but second-hand via The Record; primary ABW report not directly fetched)
- Raw IOC extraction invoked: yes (zero IOCs available)
- Quote-discipline: two quotes total across two distinct attributors (ABW, ABW), under 15w each — acceptable per quote-discipline rule (the second ABW quote is the attribution language, distinct from the first)

## IOCs (from ioc-extraction skill)

```yaml
iocs:
  - type: targeting_pattern
    value: "Water-treatment ICS in Polish municipalities"
    confidence: high
    role: victim_sector
    locations:
      - "Jabłonna Lacka, Poland"
      - "Szczytno, Poland"
      - "Małdyty, Poland"
      - "Tolkmicko, Poland"
      - "Sierakowo, Poland"
    source_attribution: ["Polish ABW", "The Record"]

  - type: targeting_pattern
    value: "Polish critical infrastructure (rail, ATC, news agency, energy)"
    confidence: high
    role: broader_campaign_context
    timeframe: "2024-2025 (per ABW)"
    source_attribution: ["Polish ABW", "The Record"]

attribution_claims:
  - actor_named: "[unspecified — Russian special services]"
    actor_class: "Russian state services (general)"
    nation_state_named: true
    nation: RU
    confidence_language: "with particular emphasis on the special services of the Russian Federation"
    cross_walk_to_roster: null
    archimedes_action: |
      Hard Rule 2 — do not originate cross-walk to Sandworm (007),
      APT28 (006), or APT29 (009) on the basis of inferential TTP
      match. ABW publicly attributes only at the "Russian state
      services" general level. Recorded as adjacent-attribution context
      for next refresh of Russian-actor profiles.

  - actor_named: "[unspecified — pro-Russian hacktivist group]"
    actor_class: "Pro-Russian hacktivist (per CyberDefence24, relayed)"
    nation_state_named: false
    confidence_language: "linked to" (not direct attribution)
    cross_walk_to_roster: null
    archimedes_action: |
      Group not named in available source text. No tracking-candidate
      action recommended without group identification.
```

- Authorized-targets check: not applicable
- LEGAL-POLICY check: passed
