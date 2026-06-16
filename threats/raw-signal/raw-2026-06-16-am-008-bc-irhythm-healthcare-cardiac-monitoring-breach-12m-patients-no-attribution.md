---
raw_id: raw-2026-06-16-am-008
collected_at: 2026-06-16T07:56:00-04:00
run_id: pre-brief-20260616-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: bleepingcomputer
  source_name: BleepingComputer (iRhythm self-disclosure)
  source_url: https://www.bleepingcomputer.com/news/security/irhythm-discloses-data-breach-says-hackers-stole-patient-info/
  published_at: 2026-06-16T06:31:59+00:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [iRhythm, cardiac monitoring, healthcare breach, PHI, social engineering, third-party hosted business applications, material incident, ransomware extortion]
triage_tags: [self_disclosure, healthcare_breach, no_actor_attribution, no_ad_prime_victim, no_promotable_substrate, situational_awareness_only]
iocs_extracted: true
iocs_count: 0
text_word_count: 580
promoted: false
rejected_at: 2026-06-16T08:00:00-04:00
rejection_id: reject-2026-06-16-0003
ttl_expires_at: 2026-09-14T07:56:00-04:00
---

# iRhythm Holdings (Cardiac Monitoring) — Self-Disclosed Data Breach, 12M Patient Profile, No Attribution

**Source:** BleepingComputer, Sergiu Gatlan byline. Published 2026-06-16T06:31:59Z.
**URL:** https://www.bleepingcomputer.com/news/security/irhythm-discloses-data-breach-says-hackers-stole-patient-info/

## Article substance (paraphrased, no >15 word quotes)

**iRhythm Holdings**, a digital healthcare company providing cardiac monitoring services (Zio cardiac monitor patches) to **over 12 million patients**, has self-disclosed a data breach in which attackers accessed patient protected health information (PHI), proprietary data, and personal information stored on **third-party-hosted business applications**.

### Breach scope and impact

- **Affected data classes**: PHI, proprietary corporate data, personal information
- **Affected systems**: third-party-hosted business applications (NOT iRhythm's primary clinical monitoring devices, NOT financial reporting systems, NOT payment systems)
- **Clinical operations unaffected**: cardiac monitoring devices and patient safety operations not impacted
- **Financial systems unaffected**: no payment card or financial account information stored by iRhythm; financial reporting unaffected
- **Materiality assessment**: company determined incident is "material" due to volume of potentially affected data

### Self-disclosure attribution language (iRhythm direct)

iRhythm quote (paraphrased to under 15 words per Hard Rule 6): The Company determined that the incident is material in light of the volume of the potentially affected data.

### Attack vector and timeline

- **Attack vector**: social engineering
- **Extortion demand**: attackers demanded payment on 2026-06-09 to prevent public disclosure
- **Public disclosure**: iRhythm self-disclosed in BC publication 2026-06-16 (i.e., after declining or not paying the extortion demand)
- **No actor attribution** — BC does NOT name a ransomware operator, no Tor leak-site claim cited

## Attribution language (Hard Rule 2 preserved)

- No threat actor attribution from any source
- BC describes the actors as "hackers" without naming a group
- No Tor leak-site claim attribution cited
- iRhythm's SEC 8-K filing (material disclosure) may have additional attribution detail; BC does not reproduce it

## A&D relevance assessment

- **A&D-relevance: NONE**
- iRhythm is a consumer/B2B healthcare technology company; not A&D, not DIB, not ITAR-regulated, not a defense contractor
- No A&D-prime named victim
- No CVE, no actor, no IOC, no tradecraft pattern with broad A&D applicability
- **Promotable substrate: NO** — situational awareness only, healthcare-sector breach with no broader implications for A&D-prime corpus

## IOC extraction

**No IOCs** in BC article.

## Grader notes

- **Source grading path**: BC B-grade trade press; iRhythm self-disclosure A1-equivalent for the procedural-facts layer (iRhythm vouching for its own breach disclosure) but the breach context (actor identity, attack chain detail, IOCs) is unsourced and unconfirmed.
- **Promotability assessment**: NOT PROMOTABLE. Healthcare-sector consumer breach, no A&D relevance, no actor attribution, no tradecraft pattern.
- **Coverage decision**: This is captured as raw-signal for completeness audit trail, but the grader should DISCARD from morning brief consideration — situational awareness only. The brief composition lane this fits is none.
- **Why captured as raw-signal anyway**: Per collector discipline, any BC item that hits a healthcare-sector / breach-self-disclosure pattern is logged for completeness. The grader applies the promotability filter downstream; the collector does not pre-filter.
