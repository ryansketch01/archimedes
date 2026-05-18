---
raw_id: raw-2026-05-18-pm-006
collected_at: 2026-05-18T15:48:00-04:00
run_id: pre-brief-20260518-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: thehackernews
  source_name: The Hacker News
  source_url: https://thehackernews.com/2026/05/interpol-operation-ramz-disrupts-mena.html
  published_at: 2026-05-18T13:21:18-04:00
  author: The Hacker News
match_reason:
  watchlist: []
  actors: []  # No tracked APT named; MuddyWater / APT34 / Charming Kitten / OilRig / Handala / IRGC clusters NOT cited
  vulnerabilities: []
  keywords: [INTERPOL, Operation Ramz, MENA, PhaaS, phishing-as-a-service, cybercrime, Group-IB, Team-Cymru]
triage_tags: [le_disruption_class, mena_geography_adjacent_to_iran_roster_but_no_apt_named, sector_context_completeness, net_new_in_window]
iocs_extracted: false
iocs_count: 0
text_word_count: 320
promoted: false
rejected_at: 2026-05-18T16:18:00-04:00
rejection_id: reject-2026-05-18-0003
ttl_expires_at: 2026-08-16T15:48:00-04:00
---

# INTERPOL Operation Ramz Disrupts MENA Cybercrime Networks with 201 Arrests

The Hacker News, 2026-05-18 13:21 EDT.

INTERPOL has coordinated a first-of-its-kind cybercrime crackdown across the Middle East and North Africa (MENA) that led to 201 arrests and the identification of an additional 382 suspects. The initiative involved 13 countries from the region between October 2025 and February 2026, aiming to investigate and neutralize malicious infrastructure, arrest perpetrators behind these schemes, and identify victims.

Geographic scope (13 MENA countries): Algeria, Bahrain, Egypt, Iraq, Jordan, Lebanon, Libya, Morocco, Oman, Palestine, Qatar, Tunisia, U.A.E.

Operation results:
- 201 arrests made
- 382 additional suspects identified
- 3,867 victims identified
- 53 servers seized

Disrupted operations cited:
- Phishing-as-a-Service (PhaaS) scheme disrupted by Algerian authorities — one suspect arrested
- Financial fraud operation in Jordan — 15 individuals involved in investment scams; two orchestrators arrested

Cybercrime types targeted (per source): phishing and PhaaS, malware distribution, cyber scams, banking data theft, financial fraud / investment scams, compromise of legitimate servers via critical vulnerabilities.

Named APT roster overlap: NONE. No specific named APT groups or tracked threat clusters attributed in this article (no MuddyWater / APT34 / Charming Kitten / OilRig / Handala / IRGC-CEC / etc.).

Timeline: October 2025 → February 2026 (operation duration); 2026-05-18 publication.

Named law enforcement / partners cited: INTERPOL (coordinating agency); Group-IB (provided actionable intelligence on 5,000+ compromised accounts); Team Cymru (infrastructure disruption support); national law enforcement from participating MENA countries.

Attribution discipline: factual regarding infrastructure seizures and arrests without broader geopolitical attribution.

---

## Extraction notes

- Language: en
- Publisher byline: The Hacker News (no specific author byline)
- Article type: news (LE disruption operation summary)
- Raw IOC extraction invoked: not applicable (no IOCs in source body)
- Net-new vs. carry-forward set: YES — Operation Ramz is a NET-NEW LE-disruption surface in the corpus. Not previously evaluated.
- Hard Rule 2 preservation: factual / non-attribution language preserved. Geographic adjacency to Iran-tracked-actor cluster (MuddyWater #022 / Charming Kitten #011 / UNC1549 #004 / APT34 #023 / Handala Hack #014) NOT a basis for any attribution propagation — none of those actors named in source.
- A&D / defense / Tier-1 prime relevance: NONE.
- Status-update candidacy: Mention-class only for sector-context completeness on cybercrime ecosystem disruption. NOT a finding-promotion candidate (commodity-cybercrime LE-disruption, no tracked actor, no A&D entity, no IOCs published).
- Flagged for grader 16:00 afternoon brief as Other Signal mention or discard with rationale.
- Group-IB + Team Cymru are vendor-research partners cited; both could be candidates for source-grades.yaml addition if they recur as primary citation in future findings (currently neither in source-grades.yaml).

## IOCs

```yaml
iocs: []  # No file-level / network-level IOCs published. No CVE / no domain / no IP / no hash.

attribution_claims: []  # No specific named APT or threat cluster attributed; LE-disruption-class commodity cybercrime only.

le_disruption_procedural:
  operation_name: Operation Ramz
  coordinating_agency: INTERPOL
  scope: MENA (13 countries)
  duration: 2025-10 → 2026-02
  arrests: 201
  suspects_identified: 382
  victims_identified: 3867
  servers_seized: 53
  named_partners: [Group-IB, Team Cymru]

sector_relevance:
  a_and_d_watchlist: false
  iran_roster_geographic_adjacency: true_but_no_apt_named
  archimedes_position: "Geographic adjacency to Iran-tracked-actor cluster NOT a basis for attribution propagation per Hard Rule 2."
```
