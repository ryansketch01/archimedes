---
raw_id: raw-2026-07-16-pm-001
collected_at: 2026-07-16T15:33:00-04:00
run_id: pre-brief-20260716-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: bleepingcomputer
  source_name: BleepingComputer (primary body) + SecurityWeek + The Record (corroborating relays)
  source_url: https://www.bleepingcomputer.com/news/security/scattered-spider-members-behind-transport-for-london-hack-get-five-years-in-prison/
  published_at: 2026-07-16T12:31:29+00:00
  corroborating_sources:
    - source_yaml_id: securityweek
      url: https://www.securityweek.com/two-scattered-spider-hackers-sentenced-to-jail-in-uk/
      published_at: 2026-07-16T13:21:12+00:00
    - source_yaml_id: the-record
      url: https://therecord.media/scattered-spider-hackers-tfl-sentenced
      published_at: 2026-07-16T12:00:00+00:00
match_reason:
  watchlist: []
  actors: [Scattered Spider, UNC3944]
  vulnerabilities: []
  keywords: [Transport for London, Computer Misuse Act, NCA, DOJ, sentencing]
triage_tags: [tracked_actor, roster_hit_013, law_enforcement_action, retrospective_no_new_ttp]
iocs_extracted: true
iocs_count: 0
text_word_count: 340
promoted: true
promoted_to_finding: finding-2026-07-16-0004
promoted_at: 2026-07-16T16:24:00-04:00
grading_run_id: afternoon-20260716-160000
ttl_expires_at: 2026-10-14T15:33:00-04:00
---

# Scattered Spider members behind Transport for London hack sentenced to 5.5 years in UK

Two members of the Scattered Spider cybercrime collective — **Thalha Jubair (20)** and **Owen Flowers (18)** — were each sentenced to five years and six months in UK prison for the August 2024 cyberattack against **Transport for London (TfL)**. Both pleaded guilty under the Computer Misuse Act. UK authorities (National Crime Agency, City of London Police) described it as the UK's largest cyber crime case to date; the U.S. Department of Justice brought parallel charges.

Scattered Spider is tracked in the Archimedes roster as actor **#013** (aliases: UNC3944, Octo Tempest, 0ktapus, Scatter Swine, Muddled Libra, Starfraud). This is a retrospective law-enforcement / attribution-of-record development on a tracked actor — no new tooling, targeting, or exploitation TTP is disclosed.

## Case facts (per relays)

- **Primary victim:** TfL. The breach rendered 148 systems inoperable; disrupted Dial-a-Ride, concessionary travel cards, contactless/digital payments, refund processing; forced all ~27,000 employees to reset passwords in person. Stolen customer data included names, addresses, contact details.
- **Financial impact:** TfL losses/recovery costs ~£29 million; UK authorities estimated potential ~£56 billion economic loss had a full network shutdown succeeded. Jubair and accomplices reportedly extorted over $115 million from victims worldwide (Aug 2024–Jul 2025).
- **Additional victims:** Flowers implicated in intrusions against U.S. healthcare providers Sutter Health and SSM Health Care Corporation. Jubair charged by DOJ with involvement in ~120 network breaches affecting dozens of U.S. organizations, including critical infrastructure and courts.
- **Timeline:** breach Aug 2024; TfL disclosure 2 Sep 2024; arrests 16 Sep 2024; sentencing Jul 2026.

---

## Extraction notes

- Language: en
- Publisher byline: Sergiu Gatlan (BleepingComputer); Eduard Kovacs (SecurityWeek); The Record staff
- Article type: news (law-enforcement / court sentencing)
- Raw IOC extraction invoked: yes
- Three publisher-independent relays converge on the same procedural facts; no vendor threat-intel attribution layer required (attribution is by NCA/DOJ court process, not a CTI vendor).
- GDPR: named convicted defendants (Jubair, Flowers) recorded name + age only, in official law-enforcement context. No PII beyond what the public court record carries. No credentials stored (the 27,000-password-reset detail is a procedural fact, not credential values — Hard Rule 7).

## IOCs (from ioc-extraction skill)

```yaml
iocs:
  ipv4: []
  ipv6: []
  domains: []
  urls: []
  hashes: []
  emails: []
  cves: []
credentials_observed: false
credential_count: 0
named_individuals:
  - name: "Thalha Jubair"
    age: 20
    role: "convicted Scattered Spider member; DOJ parallel charges (~120 breaches)"
    basis: "public court / law-enforcement record"
  - name: "Owen Flowers"
    age: 18
    role: "convicted Scattered Spider member; implicated in Sutter Health + SSM Health intrusions"
    basis: "public court / law-enforcement record"
victims_named:
  - "Transport for London (TfL)"
  - "Sutter Health (US healthcare)"
  - "SSM Health Care Corporation (US healthcare)"
attribution_claims:
  - actor: "Scattered Spider"
    roster_id: "013"
    aliases_in_source: ["Scattered Spider cybercrime collective"]
    claimed_by: "UK National Crime Agency + City of London Police + U.S. DOJ (law-enforcement / court process)"
    language: "members of the Scattered Spider cybercrime collective"
    confidence_language: "convicted (guilty plea under Computer Misuse Act)"
    note: "Attribution is of-record via prosecution, not a novel Archimedes claim (Hard Rule 2). No new TTP/IOC disclosed."
```
