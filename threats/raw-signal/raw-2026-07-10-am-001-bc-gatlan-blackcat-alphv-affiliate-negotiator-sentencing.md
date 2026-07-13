---
raw_id: raw-2026-07-10-am-001
collected_at: 2026-07-10T07:33:00-04:00
run_id: pre-brief-20260710-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: bleepingcomputer
  source_name: BleepingComputer
  source_url: https://www.bleepingcomputer.com/news/security/us-ransomware-negotiator-gets-4-years-in-prison-for-blackcat-attacks/
  published_at: 2026-07-10T04:17:52-04:00
match_reason:
  watchlist: []
  actors: ["020"]          # BlackCat / ALPHV (roster alias match)
  vulnerabilities: []
  keywords: [blackcat, alphv, ransomware-affiliate, insider-threat, ir-firm-insider]
triage_tags: [non_flash, actor_adjacent, roster_match_blackcat, le_sentencing, no_iocs, low_ad_relevance]
iocs_extracted: true
iocs_count: 0
text_word_count: 300
promoted: true
promoted_to_finding: finding-2026-07-10-0001
promoted_at: 2026-07-10T08:14:00-04:00
ttl_expires_at: 2026-10-08T07:33:00-04:00
test: false
---

# Former ransomware negotiator gets 4 years for BlackCat attacks

BleepingComputer (Sergiu Gatlan, 2026-07-10) reports the U.S. federal
sentencing of **Angelo Martino, 41**, a former employee of cybersecurity
incident-response firm **DigitalMint**, to **70 months** in prison for
participating in **BlackCat (ALPHV)** ransomware extortion attacks against
U.S. companies. Two co-conspirators — **Kevin Tyler Martin, 28** and **Ryan
Clifford Goldberg, 33** (both linked to Sygnia / DigitalMint in the reporting)
— each received four-year sentences in May 2026.

Per the article, between **April 2023 and April 2025** the three operated as
**BlackCat affiliates**, running extortion attacks and sharing a 20% revenue
split with BlackCat administrators. Prosecutors allege Martino, in his
negotiator role, shared confidential information about victims' insurance
policy limits and negotiation positions. Named/described victims include a
financial-services firm (~$25.66M ransom), a nonprofit (~$26.79M ransom), plus
school districts, medical facilities, law firms, and additional
financial-services companies. The reporting frames the broader BlackCat gang as
having collected **at least $300 million** from **over 1,000 victims** through
September 2023.

Timeline per source: initial indictment October 2025; Martino's name unsealed
March 2026; sentencing announced 2026-07-10. **No aerospace/defense sector
victim is identified**, and **no technical IOCs** (domains, IPs, hashes,
wallets, CVEs) are provided in the article.

**Collector note (not an assessment):** captured on a **roster-alias match** —
BlackCat / ALPHV is tracked as actor **#020** (threat_level HIGH, profile
pending) in `_roster.yaml`. This is a **law-enforcement sentencing** of
rogue-insider affiliates (IR-firm employees who moonlighted as BlackCat
affiliates), not new campaign activity or a new attribution to a tracked
actor. Attribution language ("BlackCat affiliates," "BlackCat (ALPHV)") is the
source's / court's procedural characterization, preserved verbatim per Hard
Rule 2 — Archimedes originates nothing here. No FLASH trigger fires: no active
exploitation, no tracked-CVE, no new-attribution-to-tracked-actor in the FLASH
sense, no A&D watchlist hit. Grader / actor-profiler to decide whether it
warrants a note in the BlackCat (#020) dossier (insider-threat / affiliate
economics angle) or the ransomware landscape.

---

## Extraction notes

- Language: en
- Publisher byline: Sergiu Gatlan (BleepingComputer)
- Article type: news / law-enforcement sentencing
- Raw IOC extraction invoked: yes (result: zero technical indicators in source)
- Copyright discipline: no verbatim quote >15 words used; facts paraphrased.
- Corroboration status at collection: single-source (BleepingComputer) in-window.
  Underlying event is a public U.S. federal court sentencing (DOJ-class
  primary); direct DOJ press release / court docket NOT retrieved this sweep
  (relay-only). Named-individual PII limited to names + ages already public in
  court proceedings, per LEGAL-POLICY GDPR data-minimization (public figures in
  adjudicated criminal proceedings).

## IOCs (from ioc-extraction skill)

```yaml
extraction_metadata:
  source_brief_id: raw-2026-07-10-am-001
  source_url: https://www.bleepingcomputer.com/news/security/us-ransomware-negotiator-gets-4-years-in-prison-for-blackcat-attacks/
  extracted_at: 2026-07-10T11:33:00Z
  extracted_by: collector
  target_actor_id: "020"    # BlackCat / ALPHV — claim-in-text only; grader/actor-profiler resolve
  text_word_count: 300

indicators: []               # No technical IOCs (domains/IPs/hashes/wallets/CVEs) present in source

attribution_claims:
  - claimed_actor: "BlackCat / ALPHV"
    ioc_ids: []              # attribution is to the named individuals as affiliates, not to any IOC
    claimed_by_source: raw-2026-07-10-am-001
    attribution_confidence_in_source: procedural_court_characterization
    requires_grading: true
    notes: >
      Source/court characterizes the three sentenced individuals as "BlackCat
      (ALPHV) affiliates" operating on a 20% revenue split with BlackCat
      administrators. This is procedural (indictment/sentencing) language, not
      a novel technical attribution. Preserved per Hard Rule 2; grader applies
      admiralty grading if promoted.

benign_filtered:
  - value: bleepingcomputer.com
    reason: reference_site_publisher

extraction_warnings:
  - type: no_indicators_present
    ioc_id: null
    detail: "Article is a sentencing report with no technical indicators; iocs_count=0 by content, not by extraction failure."
```
