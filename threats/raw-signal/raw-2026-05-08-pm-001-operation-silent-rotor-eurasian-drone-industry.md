---
raw_id: raw-2026-05-08-pm-001
collected_at: 2026-05-08T15:35:00-04:00
run_id: pre-brief-20260508-153000
collection_mode: pre_brief_collection
test: false
sources:
  - source_yaml_id: securityweek
    source_name: "SecurityWeek (In Other News column)"
    source_url: https://www.securityweek.com/in-other-news-train-hacker-arrested-pamdoora-linux-backdoor-new-cisa-director-frontrunner/
    source_grade_estimated: B
    role: pointer
    published_at: 2026-05-08T14:30:00+00:00
    note: |
      SecurityWeek "In Other News" column referenced "spy operation
      targets Eurasian drone industry" — pointer to original Seqrite
      Labs research. SecurityWeek itself a one-line relay; depth
      comes from the primary.
  - source_yaml_id: seqrite-labs
    source_name: "Seqrite Labs (primary)"
    source_url: https://www.seqrite.com/blog/operation-silent-rotor-rust-malware-unmanned-aviation-sector/
    source_grade_estimated: not_in_grades_yaml_pending_assessment
    role: primary
    published_at: 2026-05-08T00:00:00+00:00
    note: |
      Seqrite Labs is NOT currently listed in source-grades.yaml. This
      is the primary research piece carrying the technical depth (Rust
      malware analysis, IOCs, MITRE mapping, C2 infrastructure). Grader
      should treat as new-source-pending-grade — likely C until track
      record observed (vendor-of-AV/EDR-origin, India-based, no prior
      Archimedes-corpus citation). Russian-language Hacker News and
      multiple international relays cover the same campaign.
publish_window: { start: 2026-05-08T07:30:00-04:00, end: 2026-05-08T15:30:00-04:00 }
match_reason:
  watchlist:
    - aerospace-defense
  watchlist_match_detail: |
    "Eurasian unmanned aviation sector" — direct match to A&D
    target profile. Targeting includes Russia, Tajikistan, Central
    Asia, Middle East, and Europe. Lure documents reference Boeing
    737 navigation databases and NOTAM datasets — Boeing aliasing is
    a Tier-1 prime watchlist hit (though as lure subject matter, not
    confirmed Boeing-target).
  actors: []
  vulnerabilities: []
  keywords:
    - operation-silent-rotor
    - eurasian-drone-industry
    - unmanned-aviation
    - rust-malware
    - russian-aeronautical-information-center
    - cai
    - boeing-737
    - notam
    - spear-phishing
    - moscow-forum-2026
triage_tags:
  - ad_sector
  - active_campaign
  - watchlist_hit
  - new_source_pending_grade
  - boeing_lure_subject
  - no_attribution_yet
  - rust_malware_emerging_pattern
flash_trigger_evaluation:
  trigger_1_critical_cve_exploited:
    decision: not_triggered
    rationale: "No CVE involved; this is custom malware via spear-phishing."
  trigger_2_tracked_actor_attribution:
    decision: not_triggered
    rationale: |
      Seqrite explicitly: "we are not attributing this campaign to any
      known threat actor." No tracked actor named.
  trigger_3_first_party_ioc_hit:
    decision: not_triggered
    rationale: "Splunk archimedes/defenseclaw_local clean for the IOCs in this report (verified 8h window)."
  trigger_4_tracked_actor_ttp_change:
    decision: not_triggered
    rationale: "No tracked actor."
  trigger_5_ad_sector_campaign:
    evaluation: |
      Matches conditions partially:
      - campaign_active: TRUE (Seqrite reports ongoing infrastructure;
        domain registered 9 days before analysis; multiple decoy lures).
      - multi_victim_confirmed: AMBIGUOUS — Seqrite reports a "campaign
        affecting professionals in the Eurasian unmanned aviation
        sector" but does not enumerate specific victim count. Targeting
        the Unmanned Aviation 2026 Moscow forum attendees implies
        breadth, not just one victim.
      - ad_sector_targeted: TRUE (unmanned aviation sector — direct
        A&D watchlist hit).
      Multi-victim is the weak leg. Source grade also a question
      (Seqrite is not in current grades.yaml; cautious provisional).
    decision: candidate_borderline_grader_decides
    rationale: |
      Bordeline FLASH-5 candidate. Multi-victim confirmed in spirit
      (forum-attendee targeting) but not enumerated. Recommend grader
      cluster with morning brief A&D-watchlist coverage; if grader
      decides this rises to FLASH, briefer composes per FLASH-POLICY.
      Otherwise rolls into 16:00 afternoon brief A&D section.
  trigger_6_zero_day_no_patch:
    decision: not_triggered
    rationale: "Custom malware, not a vulnerability."
iocs_extracted: true
iocs_count: 11
text_word_count: 950
publication_window_match: in_window
promoted: true
promoted_to_finding: finding-2026-05-08-0010
promoted_at: 2026-05-08T16:38:00-04:00
ttl_expires_at: 2026-08-06T15:35:00-04:00
---

# Operation Silent Rotor — Rust-based malware targets Eurasian unmanned aviation sector ahead of Moscow drone forum

## Source summary

Seqrite Labs published primary research naming "Operation Silent Rotor" — a spear-phishing campaign delivering a Rust-based 64-bit Windows executable disguised as order confirmation documents from the Russian Aeronautical Information Center (Центр аэронавигационной информации / ЦАИ / CAI). Targets are professionals in the Eurasian unmanned aviation systems sector. The campaign is timed to the XIII Eurasian International Forum "Unmanned Aviation 2026" held April 23, 2026, in Moscow. SecurityWeek's "In Other News" column for 2026-05-08 included a one-line pointer crediting the original research to Seqrite.

## Targeting (per Seqrite)

- **Industries:** Unmanned Aviation Systems (UAS/UAV), aeronautical information services
- **Geographies:** Russia, Tajikistan, Central Asia, Middle East, Europe
- **Lure documents (decoys in the malicious archive):**
  - Translation certificate from a Tajikistan-based company
  - Aviation product order confirmation
  - Excel spreadsheets listing **Boeing 737 navigation databases and NOTAM datasets** (NOTAM = Notice to Airmen, FAA-standard aviation alerts)

The Boeing 737 navigation database lure is subject-matter — the malware's social engineering centers on Boeing aircraft navigation data, not a confirmed Boeing intrusion. Still flagged as a Boeing-aliased watchlist surface.

## Malware (per Seqrite)

**Stage 1 — Initial execution:**
- 64-bit Rust executable
- System fingerprinting: hostname + C: drive volume serial number XOR'd
- Collects environment variables (username, domain, profile path) + network adapter info
- JSON exfiltration via XOR encryption over HTTPS to C2

**Stage 2 — Payload delivery:**
- Receives encrypted response, decrypts via AES-256 in blocks
- Writes randomly-named .exe to `%USERPROFILE%\Documents\` or `C:\Users\Public\Documents\`
- Executes second-stage payload

## Infrastructure (per Seqrite)

- **C2 domain:** cdn[.]kleymarket[.]ru (registered 9 days before Seqrite analysis)
- **Primary C2 IP:** 45[.]142[.]36[.]76 (AS48347 MTW-AS, Moscow)
- **Historical IPs:** 92[.]62[.]113[.]232, 89[.]108[.]110[.]154

## Attribution (per Seqrite)

> "At the time of writing, we are not attributing this campaign to any known threat actor."

No attribution made by Seqrite. Russian-language lures and regional targeting (Eurasian, with Russian government-themed decoys) suggest Russian-language operator but origin/sponsor unspecified. Targeting of the *Russian* aeronautical industry (with Russian-language lures masquerading as a Russian government entity) is interesting — suggests either a Russian internal/factional operation, an actor pretending to be Russian to attract Russian-aviation attendees (false flag), or a pro-Ukraine / hostile-to-Russia actor harvesting Russian-aviation sector intelligence. **No assessment from collector — Seqrite did not name an actor; downstream subagents handle.**

## Why this matters for A&D target profile

- Direct watchlist match: "Eurasian unmanned aviation sector" is A&D-relevant.
- Boeing 737 navigation database lures = subject-matter aliasing of a Tier-1 prime watchlist entity.
- NOTAM datasets in lures suggest the operator understands aviation-industry document conventions; targets are likely real aviation professionals.
- Moscow forum timing implies audience-specific operation, not opportunistic.

## Anti-noise note

Seqrite primary research is fresh (within window). SecurityWeek "In Other News" column relays the same. No prior Archimedes raw-signal exists for "Operation Silent Rotor" — first surface in corpus.

## Extraction notes

- Language: en (Seqrite primary in English; SecurityWeek relay in English)
- Article type: vendor research blog (primary) + media digest column (relay)
- Publisher byline: Seqrite Labs (primary); SecurityWeek News (relay)
- Raw IOC extraction invoked: yes

## IOCs

```yaml
iocs:
  - type: domain
    value: "cdn.kleymarket.ru"
    role: c2
    notes: "Registered ~9 days before Seqrite analysis. Russian TLD. C2 for Stage-1 Rust executable."
    sources: [seqrite]

  - type: ipv4
    value: "45.142.36.76"
    role: c2
    notes: "AS48347 MTW-AS, Moscow. Resolves to cdn.kleymarket.ru per Seqrite."
    sources: [seqrite]

  - type: ipv4
    value: "92.62.113.232"
    role: c2_historical
    notes: "Historical association per Seqrite; current relevance not stated."
    sources: [seqrite]

  - type: ipv4
    value: "89.108.110.154"
    role: c2_historical
    notes: "Historical association per Seqrite; current relevance not stated."
    sources: [seqrite]

  - type: sha256
    value: "5936f42ffd7fa7896eeae725b60a5d26bbf3e584712671ef5da0138ee5d58f60"
    role: malware_stage1
    filename: "Подтверждение заказа продукции ЦАИ.exe"
    detection: "Trojan.Win64"
    sources: [seqrite]

  - type: sha256
    value: "fdef9e489f773319f55f92f712d1b7b5447d59a632b8f4173d1b161d3759ad92"
    role: malware_archive
    filename: "cai partner (1).zip"
    sources: [seqrite]

  - type: sha256
    value: "57e26f6e3b311a1064c946b69159ee05abedf9228b2f95c65536429e7ac7fb24"
    role: malware_archive
    filename: "cai partner.zip"
    sources: [seqrite]

  - type: sha256
    value: "a7bd8869293212e1671df90d2d41b96d4933eb9408b1111bd830e111a91bb202"
    role: malware_lure
    filename: "Certificate of translation.PDF"
    sources: [seqrite]

  - type: sha256
    value: "2064ef387ac9e51ba72b32004d99e8a0b291dbab24ed8db30f437abf1b40cb49"
    role: malware_lure
    filename: "Confirmation document (DOCX)"
    sources: [seqrite]

  - type: sha256
    value: "89f8e42c825d09a0a50e99bbf7304d7037be33ea362a57d34f87fa7981f80126"
    role: malware_lure
    filename: "summary_order_cai_final.xlsx"
    sources: [seqrite]
    note: "Excel file containing Boeing 737 navigation database / NOTAM data references — Tier-1 watchlist alias surface."

  - type: mitre_attack_mapping
    value: |
      Initial Access: T1566.001 (Spearphishing Attachment)
      Execution: T1204.002, T1059.003, T1106
      Defense Evasion: T1036.004, T1027, T1140
      Discovery: T1082, T1016, T1033, T1083
      Command & Control: T1071.001, T1090.001
      Exfiltration: T1041
      Impact: T1105
    sources: [seqrite]

attribution_claims:
  - claim_text: "we are not attributing this campaign to any known threat actor"
    claim_source: seqrite
    claim_confidence: explicit_non_attribution
    claim_date: 2026-05-08
    notes: |
      Seqrite explicit non-attribution. Russian-language lures + Russian-government-themed
      decoys + Moscow timing suggest Russian-language operator but Seqrite makes no
      sponsor/origin claim. Downstream actor-profiler review NOT triggered (no actor
      named).
```
