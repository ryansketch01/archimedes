---
raw_id: raw-2026-05-11-pm-002
collected_at: 2026-05-11T15:36:00-04:00
run_id: pre-brief-20260511-153000
collection_mode: pre_brief_collection
sweep_type: pre_brief
test: false
source:
  source_yaml_id: the-record
  source_name: The Record (Recorded Future News)
  source_url: https://therecord.media/uk-water-company-had-hackers-lurking-for-years
  primary_disclosure_source: UK Information Commissioner's Office (ICO) — regulatory action / fine announcement 2026-05-11; The Record reports per Alexander Martin (UK Editor)
  primary_disclosure_source_grade: A      # ICO is a UK government regulatory body — official-body grade
  published_at: 2026-05-11T12:51:00+00:00
  author: Alexander Martin
match_reason:
  watchlist: []
  watchlist_match_strength: no_match
  watchlist_match_detail: |
    Victim is South Staffordshire Water — UK water utility serving
    ~1.6 million people. NOT on aerospace-defense.yaml watchlist.
    Sector is water utility / critical infrastructure (UK
    regulatory tier), not A&D.

    NO A&D / aerospace / defense / DIB / satellite / ITAR / CMMC
    content in the article. The Cl0p actor's BROADER 2022 MOVEit
    / GoAnywhere campaign DID touch A&D primes (Lockheed, Boeing,
    and others were publicly disclosed as MOVEit victims in 2023
    follow-on reporting), but the South Staffordshire Water
    incident specifically is a UK-utility-sector breach — NOT an
    A&D-prime touch.
  actors:
    - Cl0p    # roster #018, HIGH threat-level — RESTATED attribution, not new
  actors_attribution_note: |
    The ICO regulatory action attributes the 2022 breach to Cl0p
    ransomware group. This is RESTATED attribution:

      - Cl0p claimed the breach on its leak site in August 2022
        at the time of data publication.
      - 2022-2023 third-party research (multiple vendors)
        corroborated the Cl0p attribution at the time.
      - The ICO accepts the Cl0p attribution without publishing
        new technical evidence; the regulatory framing is
        "an attack by the Cl0p ransomware group."

    Per FLASH-POLICY Trigger 2 strict reading + Hard Rule 2
    (Archimedes does not originate attribution), this is a
    RESTATEMENT of 2022 attribution rather than a fresh
    tracked-actor naming event. Trigger 2 fails.

    No other roster actors named in the article. Cl0p alias list
    per _roster.yaml #018: [TA505, FIN11, GOLD TAHOE]. None of
    these aliases appears in the article; The Record uses only
    the "Cl0p" canonical name.
  vulnerabilities:
    - ZeroLogon-CVE-2020-1472    # NOT in _index.yaml currently (2020 vulnerability, 5+ years aged at this point)
  vulnerabilities_attribution_note: |
    The Record's article identifies the technical attack vector
    as ZeroLogon (CVE-2020-1472), an unpatched critical
    Netlogon Remote Protocol elevation-of-privilege vulnerability
    published August 2020 with active exploitation observed in
    2020-2021. The vulnerability allowed Cl0p to compromise
    domain administrator account access at South Staffordshire
    Water in September 2020.

    ZeroLogon is NOT in Archimedes _index.yaml currently — the
    vulnerability index is currently scoped to active 2026
    threat-tracked CVEs (ZD-001/002/003 BlueHammer/RedSun/UnDefend;
    ZD-004 PAN-OS CVE-2026-0300; VT-005 OpenC3 COSMOS cluster).
    ZeroLogon as a 2020 vulnerability is HISTORICAL — patches
    have been available since August 2020 — but its appearance
    in this regulatory action serves as a contextual reminder
    that legacy unpatched vulnerabilities continue to drive
    long-dwell-time intrusions (in this case ~22 months from
    September 2020 initial access to July 2022 discovery).

    Trigger 1 / Trigger 6 do NOT apply (ZeroLogon is a 2020 CVE
    with patches available; not a new disclosure).
  keywords: [cl0p, south-staffordshire-water, uk-water-utility, ico-regulatory-fine, zerologon, cve-2020-1472, historical-2022-incident-regulatory-closure, long-dwell-time-22-months, leak-site-data-publication, regulatory-tier-not-threat-research, alexander-martin-byline, ad-relevance-zero]
triage_tags:
  - non_flash
  - flash_marginal_trigger_2_attribution_restatement_2022_historical
  - grader_queue_afternoon_brief_inventory_candidate
  - tracked_actor_roster_018_cl0p_restated_attribution_historical_incident
  - water_utility_sector_not_ad
  - regulatory_closure_2026_on_2022_breach
  - long_dwell_time_22_months_initial_access_to_discovery
  - zerologon_cve_2020_1472_historical_unpatched_attack_vector
  - ad_relevance_zero_direct_zero_capability_level_zero
iocs_extracted: true   # invoked; zero IOCs in The Record article body
iocs_count: 0
text_word_count: 950
promoted: true
promoted_to_finding: finding-2026-05-11-0004
promoted_at: 2026-05-11T16:10:00-04:00
ttl_expires_at: 2026-08-09T15:36:00-04:00
---

# UK Water Company Allowed Hackers to Lurk Undetected for Nearly Two Years, Regulator Finds (2026-05-11)

## Article body

**Title:** UK water company allowed hackers to lurk undetected for nearly
two years, regulator finds

**Published:** 2026-05-11T12:51:00+00:00 (08:51 EDT, in-window)

**Author:** Alexander Martin, UK Editor for Recorded Future News

**Lede:** The Information Commissioner's Office (ICO) fined South
Staffordshire Water £963,900 ($1.3 million) on Monday over an attack
by the Cl0p ransomware group that led to the personal data of 633,887
customers and employees being published in August 2022.

### Incident chronology

The ICO's regulatory action describes a long-dwell-time intrusion:

- **Initial access — September 2020.** Cl0p actors gained initial
  access to South Staffordshire Water via a malicious email
  attachment. This date sits within the 2020 ZeroLogon disclosure
  window (CVE-2020-1472, published August 2020) and is consistent
  with broader Cl0p exploitation patterns of the era.
- **Latent persistence — 20 months.** From September 2020 to May 2022,
  Cl0p operators maintained covert access to the South Staffordshire
  Water environment without triggering IR engagement.
- **Lateral movement begins — May 2022.** Cl0p escalates to
  compromised domain administrator account access via ZeroLogon
  exploitation of an unpatched Netlogon Remote Protocol weakness.
- **Discovery — July 2022.** The breach was discovered ~22 months
  after initial access, when IT performance issues triggered
  investigation.
- **Data publication — August 2022.** Cl0p published approximately
  4.1 terabytes of stolen data on its leak site, including:
  - Names
  - Addresses
  - Dates of birth
  - Bank account numbers and sort codes
  - National Insurance numbers
  - Disability information for Priority Services Register customers
  (a vulnerable-population subset of utility customers requiring
   special billing or service accommodations)
- **Regulatory action — 2026-05-11.** ICO publishes £963,900 fine
  for data protection failures related to the breach.

### Regulator framing

The ICO's framing focuses on **data protection failures** rather than
threat-actor TTP analysis. The £963,900 fine is for inadequate
security controls that allowed the long-dwell-time intrusion — not
for any specific exploitation pattern by Cl0p. The Cl0p attribution
is accepted from 2022 leak-site claims and contemporaneous
third-party vendor research, without new technical evidence
published as part of this 2026 regulatory action.

### Sector context

South Staffordshire Water serves approximately 1.6 million people
across South Staffordshire and Cambridge. The water utility is
classified as critical national infrastructure (CNI) under UK
Cabinet Office sector designations. The article notes broader water
sector vulnerabilities including operational technology (OT) threats,
but does not identify named A&D / aerospace / defense / DIB /
satellite / ITAR / CMMC contractors.

---

## Extraction notes

- **Language:** en
- **Publisher byline:** Alexander Martin, UK Editor for Recorded
  Future News
- **Article type:** news (regulatory-closure framing on historical
  incident)
- **Primary research source:** UK Information Commissioner's Office
  (ICO) — regulatory action / fine announcement
- **Raw IOC extraction invoked:** yes (zero IOCs extracted from The
  Record article body)

## IOCs (from ioc-extraction skill)

```yaml
extraction_run:
  source_id: pm-002
  invoked_at: 2026-05-11T15:36:00-04:00
  text_processed:
    - the-record_relay (Alexander Martin)
  total_iocs_extracted: 0
  iocs: []
  benign_filtered:
    - therecord.media (publisher's own domain)
    - recordedfuture.com (publisher's parent organization)
    - ico.org.uk (regulator's own domain referenced as primary
      source, NOT an IOC)
  attribution_claims:
    - claim: "The September 2020 → August 2022 intrusion at South
        Staffordshire Water was conducted by the Cl0p ransomware
        group"
      source: ICO regulatory action via The Record / Alexander Martin
      confidence_language: "an attack by the Cl0p ransomware group"
        (declarative, no hedging)
      coupling: RESTATEMENT — Cl0p claimed the breach on its leak
        site in August 2022; 2022-2023 third-party research
        corroborated; the ICO accepts the existing attribution
        without new technical evidence in 2026
      attributed_actor: Cl0p (roster #018 HIGH)
  flags:
    - tracked_actor_restated_not_new
    - historical_incident_2022_regulatory_closure_2026
    - sector_water_utility_not_ad
    - zerologon_cve_2020_1472_historical_attack_vector
    - no_iocs_in_article_body
```

## Cl0p tracking implications

Cl0p is roster actor #018, HIGH threat-level. The roster entry notes
attribution to "Russia" with "Cybercriminal (RaaS)" type. Aliases:
TA505, FIN11, GOLD TAHOE.

This regulatory closure adds no new tracked-actor TTP / tooling /
infrastructure observation. The ICO action is procedural — it
formalizes a 2022 attribution and assigns a £963.9K fine for data
protection failures. No new Cl0p activity is described.

Recommend actor-profiler / grader treat this as a contextual update
for the Cl0p dossier:

- Historical-victim list update: South Staffordshire Water (UK water
  utility, 1.6M customers served, 4.1TB data published 2022-08).
- Long-dwell-time tradecraft documentation: ~22 months from initial
  access to discovery. This pattern is consistent with prior Cl0p
  reporting on MOVEit / GoAnywhere campaigns where pre-positioning
  often preceded mass exploitation by months. The South Staffordshire
  Water timeline (Sept 2020 → July 2022) is an outlier-long dwell
  even by Cl0p standards.
- Initial access vector documentation: malicious email attachment
  → ZeroLogon (CVE-2020-1472) exploitation. This vector is well-
  established in Cl0p reporting; not a new observation.

The ICO fine itself (£963,900) is a regulatory-tier signal, not a
threat-research signal. Cl0p threat-level remains HIGH per existing
roster scoring; no rescore is implied by this article.

## A&D-relevance assessment

**ZERO.** This is a UK water utility incident. The Cl0p actor's
broader 2022 MOVEit / GoAnywhere campaigns DID touch A&D primes in
2022-2023 follow-on reporting, but the South Staffordshire Water
breach is sector-specific to utilities. No named A&D primes in
victim list. No capability-level relevance to the A&D-target
profile from CLAUDE.md.

Recommend grader queue this for awareness in the afternoon brief
ONLY if Cl0p tracking is a standing-section topic for this brief
cycle (per watch-config.yaml, no Cl0p standing section is currently
configured — water utility / ransomware / Russia-linked actors
have suggested-future-section status but `active: false`).

## FLASH trigger evaluation summary

| # | Trigger | Result | Driver |
|---|---|---|---|
| 1 | Critical CVE exploited | FAIL | ZeroLogon (CVE-2020-1472) is a 2020 historical vulnerability; patches available since August 2020; not a new exploitation event |
| 2 | Tracked-actor attribution | FAIL | Cl0p attribution is RESTATED from 2022 leak-site claim and contemporaneous third-party research; ICO regulatory action does not publish new technical evidence |
| 3 | First-party IOC hit | FAIL | No IOCs in article body; Splunk first-party check empty |
| 4 | Tracked-actor TTP change | FAIL | No new TTP / tooling / infrastructure / targeting observation; the article is regulatory-closure framing on a 2022 incident |
| 5 | A&D-sector campaign | FAIL | UK water utility, NOT A&D; no named A&D primes in victim list |
| 6 | Zero-day no patch | FAIL | ZeroLogon was patched August 2020; not a zero-day |

**FLASH disposition:** non-FLASH grader-queue item.
**Carry-forward to 16:00 afternoon brief:** OPTIONAL — tracked-actor
Cl0p (#018 HIGH) roster touch but the touch is regulatory-tier
(historical-incident closure), not threat-research-tier. Recommend
grader / briefer decide based on available brief space and
relevance ranking against other afternoon-brief candidates.
Actor-profiler should note the South Staffordshire Water entry in
Cl0p's historical-victim list and the long-dwell-time tradecraft
context.
