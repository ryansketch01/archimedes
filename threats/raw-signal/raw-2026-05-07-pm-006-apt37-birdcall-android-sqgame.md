---
raw_id: raw-2026-05-07-pm-006
collected_at: 2026-05-07T15:44:00-04:00
run_id: pre-brief-20260507-153000
collection_mode: pre_brief_collection
test: false
sources:
  - source_yaml_id: the-record
    source_name: "The Record (Jonathan Greig)"
    source_url: https://therecord.media/north-korean-hackers-target-ethnic-koreans-in-china
    source_grade_estimated: B
    role: originating
    published_at: 2026-05-07T00:12:00-04:00
    note: |
      ESET research relayed by The Record. APT37 (a.k.a. Scarcruft,
      DPRK / MSS-attributed per source) compromised the Sqgame card-game
      platform in a supply-chain attack since at least November 2024.
      BirdCall malware (Android and Windows variants) delivered to
      ethnic Koreans in Yanbian region of China — likely targeting
      defectors and refugees. APT37 is NOT in the Archimedes _roster.yaml
      (closest entries: 003 Lazarus Group, 002 Stardust Chollima — both
      DPRK but distinct APT lineages). NOT an A&D-targeting campaign.
match_reason:
  watchlist: []
  actors: []   # APT37 not currently in _roster.yaml
  vulnerabilities: []
  keywords: [apt37, scarcruft, north-korea, dprk, mss, sqgame, birdcall, android-malware, supply-chain, ethnic-korean-targeting, yanbian, eset]
triage_tags: [dprk_actor_not_tracked, supply_chain_compromise, mobile_malware, civil_society_targeting, candidate_for_roster_review, no_ad_relevance]
iocs_extracted: true
iocs_count: 4
text_word_count: 290
promoted: true
promoted_to_finding: finding-2026-05-07-0004
promoted_at: 2026-05-07T16:15:00-04:00
promoted_by: grader
promoted_grading_run_id: afternoon-20260507-160000
ttl_expires_at: 2026-08-05T15:44:00-04:00
---

# DPRK-attributed APT37 (Scarcruft) compromised Sqgame Android platform in supply-chain attack — ethnic-Korean targeting in China since Nov 2024

## Source summary

The Record (Jonathan Greig, "North Korean hackers targeted ethnic Koreans in China with Android 'BirdCall' malware," 2026-05-07 00:12 EDT) reports ESET research on a long-running APT37 supply-chain compromise. Sqgame, a card-game platform, was compromised since at least November 2024; victims downloaded compromised game APKs from web browsers (not the Google Play store) and installed the BirdCall backdoor.

ESET attribution: explicit, "attributed the campaign to APT37." Source confidence language: "Researchers at cybersecurity firm ESET attributed the campaign to APT37."

Quote (under 15-word limit, attributed to ESET / Filip Jurčacko): "We were unable to determine when the website was first compromised."

## What this signal represents

1. **DPRK-attributed actor not currently in Archimedes roster.** APT37 (a.k.a. Scarcruft, sometimes mapped to ScarCruft, RedEyes, Reaper, or Group123 in other vendor reporting) is NOT in `_roster.yaml`. The Archimedes roster's DPRK actors are:
   - **003 Lazarus Group** (RGB-attributed)
   - **002 Stardust Chollima / BlueNoroff / APT38** (RGB / financial)
   APT37 is operationally distinct from both per public reporting. Recommend grader / actor-profiler evaluate APT37 as a `/new-actor` candidate. The campaign volume and targeting profile (civil society, refugees, defectors) is significant though not currently A&D-relevant.

2. **Targeting profile.** Yanbian Korean Autonomous Prefecture (China) — ethnic Koreans, "likely North Korean refugees or defectors" per ESET. This is **civil society / human rights targeting**, not A&D / DIB. No defense contractor or A&D entity named.

3. **Attack chain.** Sqgame website → compromised game APKs (Android) → BirdCall backdoor. Windows variant of BirdCall also exists per article. ESET notified Sqgame December 2025; supply-chain compromise window: November 2024 – at least early 2026 (article does not state remediation date).

4. **Not A&D-relevant — but worth surfacing.** The pattern (gaming platform supply-chain compromise → mobile malware → diaspora/refugee targeting) matches DPRK's broader civil-society / coercion playbook. Outside Archimedes' primary scope but methodologically interesting for A&D-adjacent civil-rights / NGO partner organizations.

## Why this is NOT a FLASH

Trigger evaluation:
- **Trigger-1 (critical-cve-exploited):** No CVE involved. Fails.
- **Trigger-2 (tracked-actor-attribution):** APT37 not in roster. Fails.
- **Trigger-5 (ad-sector-campaign):** No A&D targeting. Fails.
- All other triggers: not applicable.

This is scheduled-brief background material at most. Recommend the `iran-cyber` / DPRK-tracking standing-section briefer treatment as a context item, NOT a featured finding.

## Recommendation for actor-profiler

`/new-actor APT37` is supportable. Justification:
- Multi-vendor track record (ESET, Mandiant, Kaspersky, Cisco Talos historically)
- DPRK MSS attribution (distinct from RGB-attributed Lazarus / Stardust Chollima)
- Mobile capability (Android-targeting differentiator from existing roster)
- Civil-society targeting + occasional defense-think-tank targeting (per historical reporting)

Decision deferred to operator approval. This raw-signal alone does not justify roster addition — but it is the third+ vendor-reported APT37 campaign in Archimedes' window, suggesting tracking pressure is reasonable.

---

## Extraction notes

- Language: en
- Article type: secondary news reporting (B-grade), citing ESET research (A-grade vendor)
- Raw IOC extraction invoked: yes
- Quote-discipline: one quote, 11 words, under 15-word limit honored

## IOCs (from ioc-extraction skill)

```yaml
iocs:
  - type: malware_family
    value: BirdCall
    confidence: high
    role: backdoor
    platforms: [Android, Windows]
    source_attribution: ["ESET", "The Record"]
    actor_attribution: "APT37 (per ESET)"
    first_seen: "November 2024 (supply-chain window opens)"

  - type: domain
    value: sqgame
    confidence: high
    role: compromised_distribution_platform
    source_attribution: ["ESET", "The Record"]
    notes: |
      Article identifies "Sqgame" as the compromised gaming platform but
      does not provide the exact domain in the source text. Domain
      enrichment recommended via VirusTotal / passive DNS at grader stage.

  - type: targeting_pattern
    value: "Ethnic Koreans in Yanbian Korean Autonomous Prefecture, China"
    confidence: high
    role: victim_demographic
    source_attribution: ["ESET", "The Record"]
    notes: "Likely targeting North Korean refugees and defectors per ESET."

  - type: distribution_pattern
    value: "Compromised APKs delivered via web browser download (not Google Play)"
    confidence: high
    role: initial_access_vector
    source_attribution: ["ESET", "The Record"]

attribution_claims:
  - actor_named: APT37
    aliases: ["Scarcruft"]
    actor_class: "DPRK-nexus state-aligned APT"
    nation_state_named: true
    nation: KP
    service: "Ministry of State Security (MSS) — per The Record's framing"
    confidence_language: "attributed the campaign to APT37"
    cross_walk_to_roster: null
    archimedes_action: |
      APT37 not in _roster.yaml. Hard Rule 2 holds — do not originate
      cross-walk to Lazarus or Stardust Chollima. Recommend actor-profiler
      evaluate /new-actor candidacy at next refresh window.
```

- Authorized-targets check: not applicable
- LEGAL-POLICY check: passed
