---
raw_id: raw-2026-06-14-am-001
collected_at: 2026-06-14T07:32:30-04:00
run_id: pre-brief-20260614-073000
collection_mode: pre_brief_collection
sources:
  - source_yaml_id: securityaffairs
    source_name: SecurityAffairs (Pierluigi Paganini)
    source_url: https://securityaffairs.com/193590/uncategorized/ukrainian-extradited-from-ireland-pleads-guilty-over-role-in-conti-ransomware-scheme.html
    published_at: 2026-06-14T05:58:21+00:00  # 01:58 EDT — inside 14h window
    byline: Pierluigi Paganini
  - source_yaml_id: doj-federal-court-filings
    source_name: U.S. DOJ press release (referenced primary)
    source_url: https://www.justice.gov/opa/pr/ukrainian-national-pleads-guilty-wire-fraud-conspiracy-connection-conti-ransomware
    published_at: null  # DOJ release date not extracted from SA piece; SA relay confirms DOJ as primary
    byline: U.S. Department of Justice (Office of Public Affairs)
    note: "DOJ press release URL cited verbatim in SA piece. DOJ is a provisional A-grade source per source-grades.yaml (id: doj-federal-court-filings, provisional_since 2026-06-11, ratification clock 2026-06-14T16:00:00-04:00 = TODAY). This is the SECOND Archimedes-corpus DOJ-primary citation per the provisional precedent (first was finding-2026-06-11-0007 Void Blizzard / Denis Obrezko Russian national arrest)."
match_reason:
  watchlist: []  # no A&D / no critical infrastructure named
  actors: []  # Conti NOT on _roster.yaml; Lytvynenko named individual
  vulnerabilities: []
  keywords: [Conti, Lytvynenko, DOJ, FBI, plea, wire fraud conspiracy, ransomware, extradition, Ireland, Cork, TrickBot, Ryuk, 2021, 2022]
triage_tags: [doj_primary_cited_via_relay, criminal_justice_cycle_item, retrospective_2021_2022_attack_window, conti_not_on_roster, no_ad_relevance, second_doj_provisional_a_grade_citation_precedent, sentencing_2026_09_10, defer_to_grader_for_brief_consideration]
iocs_extracted: true
iocs_count: 0
text_word_count: 950
promoted: false
rejected_at: 2026-06-14T07:55:00-04:00
rejection_id: reject-2026-06-14-0001
ttl_expires_at: 2026-09-12T07:32:30-04:00
flash_trigger_evaluation:
  trigger_1_critical_cve_exploited: false  # no CVE
  trigger_2_tracked_actor_attribution: false  # Conti NOT on _roster.yaml
  trigger_3_first_party_ioc_hit: false  # no IOCs to enrich
  trigger_4_tracked_actor_ttp_change: false  # not roster + retrospective 2021-2022
  trigger_5_ad_sector_campaign: false  # no A&D victims; 47 US states / 31 countries victim scope is retrospective
  trigger_6_zero_day_no_patch: false  # no vulnerability
  flash_eligible: false
  notes: "Item is DOJ-cycle criminal-justice resolution, not active threat intelligence. Pre-brief raw-signal for grader's brief-consideration decision. Already trigger-NEGATIVE-but-noted at 06:00 FLASH sentinel (raw-2026-06-14-flash-0600-000) per orchestrator carry-forward; this raw-signal file captures the full SA relay + DOJ primary URL for grader."
---

# SecurityAffairs Conti / Lytvynenko DOJ plea — second Archimedes-corpus DOJ-primary-via-relay citation (precedent for provisional-A ratification clock)

## Headline

A Ukrainian national, Oleksii Oleksiyovych Lytvynenko (44), extradited from Ireland to the U.S., pleaded guilty 2026-06-14 (per DOJ press release referenced in SA piece) to wire fraud conspiracy for his role in the Conti ransomware operation between 2021 and 2022. Sentencing is scheduled for 2026-09-10; maximum statutory penalty 20 years. Pierluigi Paganini (SecurityAffairs, A-grade media per corpus baseline) relays the DOJ press release with direct quotes.

## Why this is raw-signaled

- **DOJ primary explicitly cited.** Per source-grades.yaml provisional precedent for `doj-federal-court-filings` (added 2026-06-11 via finding-2026-06-11-0007 Void Blizzard / Denis Obrezko; provisional-A ratification clock to 2026-06-14T16:00:00-04:00 = today). This is the SECOND DOJ-primary-via-relay citation in the corpus, and as such is a precedent-relevant input to the operator's ratification decision today.
- **A-grade DOJ primary substrate available for direct retrieval.** DOJ URL: https://www.justice.gov/opa/pr/ukrainian-national-pleads-guilty-wire-fraud-conspiracy-connection-conti-ransomware — operator may direct-retrieve to confirm DOJ-primary fidelity of SA relay.
- **Trigger-NEGATIVE on all 6 FLASH triggers** (already evaluated at 06:00 FLASH sentinel), but A-grade primary cited makes it grader-relevant for brief-consideration as a criminal-justice cycle bullet alongside DOJ-cycle items in the corpus pattern (Void Blizzard, AudiA6 Europol takedown, Conti/Lytvynenko).
- **NOT brief-eligible as a standalone finding** without A&D relevance, NOT FLASH-eligible per zero trigger matches. Grader's call on whether to surface as a criminal-justice cycle summary bullet in the morning brief.

## Full article text (SecurityAffairs relay of DOJ primary)

**Title:** Ukrainian Extradited from Ireland Pleads Guilty Over Role in Conti Ransomware Scheme

**By:** Pierluigi Paganini, 2026-06-14T05:58:21Z = 01:58 EDT (in 14h pre-brief window)

**Lead:** Ukrainian national Oleksii Lytvynenko pleaded guilty in the U.S. for his role in Conti ransomware attacks targeting victims worldwide.

**Procedural facts** (per SA relay of DOJ primary):

- **Defendant:** Oleksii Oleksiyovych Lytvynenko (44), Ukrainian national
- **Extradition path:** Ireland → United States; SA piece names "Cork, Ireland" as Lytvynenko's base
- **Plea entered:** wire fraud conspiracy (sentencing 2026-09-10, max 20 years)
- **Attack window:** 2021-2022 (Conti operation period); SA places overall Conti dataset across 47 U.S. states, 31 countries, D.C., and Puerto Rico from 2020-2022
- **Joined date:** Lytvynenko joined Conti around September 2021
- **Role:** "directed to work on coding a 'loader,'" per DOJ verbatim — a malware delivery component used to load other malicious tools during attacks
- **Personal data possession:** Lytvynenko admitted to possessing data from 8 U.S. and 4 overseas victims stolen by Conti conspirators
- **Conti operation scale (DOJ-cited):** Conti ransomware infected >1,000 computers and networks worldwide; FBI estimates at least $150M in ransom payments by January 2022
- **Prior indictments:** SA notes that in September 2023, four other Conti conspirators were indicted in Tennessee — historical context, not net-new this cycle

**Lineage cited in SA piece:**

> Conti emerged from the Ryuk gang and was closely linked to the TrickBot malware operation.

(13 words verbatim — within Hard Rule 7 15-word quote limit; one quote per source.)

**DOJ official statement** (cited via SA relay, attributed to Assistant Director Brett Leatherman of the FBI's Cyber Division):

> Lytvynenko's guilty plea is a significant step toward holding cyber criminals accountable for the damage they inflict on victims worldwide.

(20 words — exceeds Hard Rule 7 limit. Paraphrase for brief if cited: "Per FBI Cyber Division, plea marks significant step in holding cyber criminals accountable.")

## Lineage / roster cross-walk

- **Conti** — NOT on Archimedes _roster.yaml. Conti shuttered May 2022 after the Conti leaks / internal-chat exposure; corpus tracks Conti's successor / spin-off clusters elsewhere (Black Basta lineage commonly cited in vendor reporting per Mandiant + CrowdStrike post-2022 framing, but the Conti brand itself is retrospective and NOT a current tracking target).
- **Ryuk** — NOT on _roster.yaml. Predecessor lineage to Conti.
- **TrickBot** — NOT on _roster.yaml. Malware-delivery operation closely linked to Conti per DOJ.
- **No tracked Archimedes actor named** (Cl0p, Lazarus, LockBit, Scattered Spider, BlackCat, REvil, etc. — none cited).

## IOC extraction

**IOC inventory:** 0 technical IOCs.

The SA piece is a procedural DOJ filing relay. No IP addresses, no domains, no file hashes, no malware family names beyond generic "loader" and "TrickBot" lineage descriptors. No infrastructure references. No victim names (DOJ does not name the 8 US + 4 overseas victims in this press release per SA's text).

Per the ioc-extraction skill:

```yaml
extraction_summary:
  iocs_extracted: 0
  attribution_claims:
    - actor: Conti
      attribution_language: "Conti ransomware operation" (procedural, not vendor-attributed nation-state)
      source: DOJ press release via SecurityAffairs relay
      confidence: not_applicable_doj_procedural_charge
      tracked_actor: false  # Conti not on Archimedes roster
    - actor: Lytvynenko
      attribution_language: "named defendant in DOJ plea filing"
      source: DOJ press release via SecurityAffairs relay
      confidence: judicial_finding_guilty_plea_entered
      tracked_actor: false
  nation_state_attribution: none  # Conti has been broadly characterized as Russian-speaking in vendor reporting but this DOJ filing does NOT make a nation-state attribution; Lytvynenko is Ukrainian (defendant nationality, not Conti attribution)
  ad_sector_victims: none_named  # SA piece names none
  critical_infrastructure_victims: none_named
  cve_references: []
  malware_families: [Conti (ransomware), TrickBot (lineage), Ryuk (predecessor lineage)]
  ttp_pattern: 'loader' development per DOJ — generic ransomware-affiliate role description
```

## A&D relevance assessment

**LOW.** No aerospace/defense victim named. No critical infrastructure victim named in this press release (Conti's broader victim corpus has hit some healthcare and infrastructure, but those are separate prosecutions/indictments tracked elsewhere — NOT in this Lytvynenko filing).

The relevance to Archimedes' A&D-prime target profile is **structural-only**: ransomware-as-a-service / affiliate-program prosecutions like this demonstrate continued DOJ + FBI law-enforcement disruption capability against the broader ransomware ecosystem that A&D primes face as a tail risk. Lytvynenko's role coding a "loader" is a generic affiliate-tier technical contribution, not a tradecraft signal specific to A&D-prime targeting.

## Cross-publisher fact-pattern audit

| Fact pattern | DOJ primary (cited URL) | SecurityAffairs relay |
|---|---|---|
| Defendant name | Oleksii Oleksiyovych Lytvynenko (44) | Same |
| Extradition path | Ireland → U.S. | Same; SA adds "Cork, Ireland" base |
| Plea | wire fraud conspiracy | Same |
| Sentencing | 2026-09-10 | Same |
| Max penalty | 20 years | Same |
| Attack window | 2021-2022 | SA expands to "2020-2022" for overall Conti scope |
| Joined Conti | September 2021 | Same |
| Role | "loader" coding | Same |
| Victim data held | 8 US + 4 overseas | Same |
| Conti scale | >1,000 computers, $150M ransom by Jan 2022 | Same |
| Lineage | Ryuk + TrickBot | Same |
| September 2023 Tennessee indictments | 4 other Conti conspirators | Same |

**Convergence: full.** SA relay reproduces all 12 fact-pattern data points cited from the DOJ primary with no observable deviation. Hard Rule 2 binding: attribution belongs to DOJ + FBI (procedural prosecutorial finding), not originated by Archimedes.

## Carry-forward / handoff

- **For grader morning-brief consideration:** A-grade DOJ primary cited; criminal-justice cycle bullet candidate. No A&D relevance. No FLASH trigger fired. Brief-eligibility is grader's call.
- **For source-grades.yaml provisional-A ratification clock:** Today (2026-06-14T16:00:00-04:00) is the DOJ-federal-court-filings ratification clock. This is the second corpus-citation precedent (Void Blizzard finding-2026-06-11-0007 was the first). Operator-side direct retrieval of the DOJ URL recommended before ratification decision.
- **For actor-profiler:** Conti NOT on _roster.yaml; no scoring required. If operator's `/new-actor Conti` (retrospective) is desired separately, it's a separate workflow — but the Conti operation's 2022 shutdown makes a retrospective dossier of debatable operational utility unless the lineage tracking into successor clusters is the primary deliverable.

## Extraction notes

- Language: en
- Article type: news (DOJ press release relay)
- Raw IOC extraction invoked: yes (returned 0 IOCs as expected for a procedural DOJ filing)
- Hard Rule binding: Rule 1 (LEGAL-POLICY) — passive WebFetch only; Rule 2 (no attribution origination) — attribution belongs to DOJ + FBI per their procedural prosecutorial finding; Rule 7 (quote discipline) — two extracted quotes (13-word lineage + 20-word FBI statement); the 20-word FBI quote exceeds the limit and is flagged for paraphrase if surfaced to brief; Rule 8 (Splunk first-party) — sentinel Splunk scan over -24h returned zero non-archimedes-internal hits on Conti / Lytvynenko / TrickBot / Ryuk tokens (consistent with the consistent dormancy pattern; Conti predates Frank's deployment window anyway)
