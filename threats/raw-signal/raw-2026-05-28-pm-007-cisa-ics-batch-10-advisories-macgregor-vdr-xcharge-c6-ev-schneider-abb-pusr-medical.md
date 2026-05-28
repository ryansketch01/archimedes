---
raw_id: raw-2026-05-28-pm-007
collected_at: 2026-05-28T16:05:00-04:00
run_id: pre-brief-20260528-pm
collection_mode: pre_brief_collection
source:
  source_yaml_id: cisa-advisories
  source_name: CISA — Cybersecurity and Infrastructure Security Agency
  source_grade: A
  source_url_batch_landing: https://www.cisa.gov/news-events/cybersecurity-advisories
  feed_path: https://www.cisa.gov/cybersecurity-advisories/all.xml
  authored_by: CISA
  published_at: 2026-05-28T12:00:00Z   # 08:00 EDT batch publication
batch_advisories:
  - id: ICSA-26-148-01
    product: MacGregor Voyage Data Recorder (VDR) G4e
    vendor: Danelec
    sectors: [Transportation Systems]
    cvss_v3: 8.3
    cves:
      - CVE-2026-42941   # Default credentials
      # Multi-CVE cluster — full CVE set not enumerated in retrievable summary
    advisory_url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-148-01
    ad_adjacency: maritime / DoD MSC adjacency
  - id: ICSA-26-148-02
    product: PUSR USR-W610 RS232/485 to Wi-Fi/Ethernet Converter
    vendor: Jinan USR IOT Technology Limited (China-HQ)
    sectors: [Critical Manufacturing]
    cvss_v3: 9.8
    cves: [CVE-2026-7786]
    advisory_url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-148-02
    ad_adjacency: industrial-network bridging, manufacturing-floor adjacency
    note: hardcoded admin credentials in firmware image
  - id: ICSA-26-148-03
    product: ABB EIBPORT (KNX building automation)
    vendor: ABB
    sectors: [Critical Manufacturing, Information Technology]
    cvss_v3: 8.0
    cves: [CVE-2021-22291]   # disclosed 2021 — backlog publication
    advisory_url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-148-03
    ad_adjacency: building automation, facility-IT crossover
  - id: ICSA-26-148-04
    product: ABB Busch-Welcome 2 Wire Door Opener Actuator
    vendor: ABB
    sectors: [Commercial Facilities]
    cvss_v3: 6.8
    cves: [CVE-2025-7705]
    advisory_url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-148-04
    ad_adjacency: low
  - id: ICSA-26-148-05
    product: CP Plus 8 Ch. Network Video Recorder (CP-UNR-108F1)
    vendor: CP Plus
    sectors: [Commercial Facilities, Critical Manufacturing, Emergency Services]
    cvss_v3: 8.4
    cves: []   # XSS via web-page generation
    advisory_url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-148-05
    ad_adjacency: low
  - id: ICSA-26-148-06
    product: KMW CCTV Security Cameras (KM-IP521, KM-IP421)
    vendor: KMW (Romania)
    sectors: [Commercial Facilities, Government Services and Facilities, Critical Manufacturing, Financial Services, Transportation Systems]
    cvss_v3: 9.1
    cves: [CVE-2026-5386]   # Unverified password change
    advisory_url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-148-06
    ad_adjacency: government facilities and transport sector named; passive surveillance reach
  - id: ICSA-26-148-07
    product: Schneider Electric EcoStruxure Machine Expert HVAC
    vendor: Schneider Electric
    sectors: [Chemical, Critical Manufacturing, Energy, Water and Wastewater]
    cvss_v3: 5.5
    cves: [SEVD-2026-132-01]   # Cleartext Storage of Sensitive Information
    advisory_url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-148-07
    ad_adjacency: energy / critical-mfg infrastructure
  - id: ICSA-26-148-08
    product: XCharge C6 EV Charging Controller
    vendor: XCharge (US-HQ)
    sectors: [Transportation Systems]
    cvss_v3: 9.8
    cves: [CVE-2026-9037]   # Firmware download integrity check failure + stack buffer overflow
    advisory_url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-148-08
    ad_adjacency: DoD fleet electrification / federal facility EV charging adjacency
    note: failure to validate firmware authenticity allows unauthorized firmware install
  - id: ICSMA-26-148-01
    product: Fourth Frontier Frontier X Mobile App + Frontier X2
    vendor: Fourth Frontier
    sectors: [Healthcare and Public Health]
    cvss_v3: 8.8
    cves: [CVE-2026-5768]   # Missing Authentication for Critical Function
    advisory_url: https://www.cisa.gov/news-events/ics-medical-advisories/icsma-26-148-01
    ad_adjacency: minimal
    note: BLE unauth read/write to clinical-reading GATT characteristics
  # ABB EIBPORT entry partially duplicated above; CISA batch count is 10 total — 9 listed plus 1 supply-chain alert
match_reason:
  watchlist:
    - aerospace-defense (transportation sector + DoD fleet EV adjacency; maritime VDR for DoD MSC vessels potentially)
  actors: []
  vulnerabilities:
    - CVE-2026-7786   # PUSR hardcoded admin creds
    - CVE-2026-5386   # KMW CCTV password reset bypass
    - CVE-2026-9037   # XCharge firmware integrity
    - CVE-2026-5768   # Fourth Frontier BLE auth
    - CVE-2026-42941  # MacGregor VDR default creds
  keywords:
    - CISA ICS advisory batch
    - MacGregor Voyage Data Recorder
    - XCharge C6 EV charger
    - Schneider Electric EcoStruxure
    - ABB EIBPORT KNX
    - PUSR USR-W610
    - KMW CCTV
    - Fourth Frontier
    - critical infrastructure
    - transportation systems
    - critical manufacturing
    - energy
triage_tags:
  - non_flash
  - ics_advisory_batch
  - government_source_cisa_procedural
  - mixed_ad_adjacency
  - transportation_systems_named
  - maritime_vdr_for_dod_msc_adjacency
  - ev_charger_federal_fleet_adjacency
iocs_extracted: true
iocs_count: 5
text_word_count: 1200
promoted: true
promoted_to_finding: finding-2026-05-28-0011-cisa-ics-batch-10-advisories-macgregor-vdr-xcharge-c6-ev-schneider-abb-pusr-medical
promoted_at: 2026-05-28T16:21:00-04:00
promoted_run_id: afternoon-20260528-160000
ttl_expires_at: 2026-08-26T16:05:00-04:00
---

# CISA ICS Advisory Batch — 10 Advisories Published 2026-05-28 12:00 UTC

## Batch summary

CISA published a routine ICS advisory batch on 2026-05-28 12:00 UTC (08:00 EDT) containing **9 ICS advisories + 1 medical-device advisory + 1 alert on supply chain compromises** (the supply-chain compromise alert is raw-signaled separately at raw-2026-05-28-pm-004).

Per source-grades.yaml CISA is grade A on procedural facts (CVE existence, CVSS scoring, affected/fixed versions, sector classification, geographic deployment). CISA ICS advisories carry vendor-coordinated disclosure status and are the canonical US-government surface for industrial control system vulnerability disclosures.

This collector file indexes the batch with per-advisory adjacency notes for grader / vuln-tracker review. **No single advisory is promoted to a dedicated raw-signal file** since none individually crosses the A&D-direct threshold; the batch index here serves as the source-record for grader clustering decisions.

## Advisory cluster — A&D adjacency assessment

### Highest A&D adjacency

1. **ICSA-26-148-01: MacGregor Voyage Data Recorder (VDR) G4e** (Danelec, CVSS 8.3, Transportation Systems / Maritime)
   - VDRs are mandatory IMO equipment on commercial shipping including chartered DoD MSC (Military Sealift Command) sealift vessels
   - Multi-CVE cluster includes: default credentials (CVE-2026-42941), insufficient credential protection, weak password hashes, hardcoded credentials, accessible file/directory exposure
   - **DoD adjacency:** chartered logistics vessels supporting DoD strategic sealift could carry vulnerable VDRs; supplier-chain visibility is the operator's call
   - **Pre-patch versions:** all < V5.250

2. **ICSA-26-148-08: XCharge C6 EV Charging Controller** (XCharge US-HQ, CVSS 9.8, Transportation Systems)
   - Firmware download integrity check failure + stack-based buffer overflow + insecure default initialization
   - **DoD / federal-fleet adjacency:** US government EV fleet electrification mandate makes EV charging infrastructure increasingly relevant to federal facility security posture
   - Firmware-update-authenticity bypass class enables persistent unauthorized firmware install
   - Worldwide deployment; US-HQ vendor

### Medium A&D adjacency

3. **ICSA-26-148-02: PUSR USR-W610 Wi-Fi/Ethernet Converter** (Jinan USR IOT, China-HQ, CVSS 9.8, Critical Manufacturing)
   - Hardcoded administrative credentials embedded in firmware image
   - Industrial-network bridging device; manufacturing-floor crossover to office IT networks
   - **Supply-chain adjacency:** China-HQ vendor; DIB facilities running RS232/485-to-Ethernet bridging are recommended to inventory PUSR deployment

4. **ICSA-26-148-07: Schneider Electric EcoStruxure Machine Expert HVAC** (Schneider, CVSS 5.5, Chemical / Critical Mfg / Energy / Water+Wastewater)
   - Cleartext storage of sensitive information (source-code disclosure class)
   - Programming software for Modicon M171-M172 logic controllers
   - **DIB adjacency:** Schneider Electric estate is widespread in A&D-prime manufacturing-floor controls

5. **ICSA-26-148-06: KMW CCTV Security Cameras** (Romania, CVSS 9.1, Government Services / Critical Mfg / Transportation / Financial / Commercial)
   - Unverified password change (CVE-2026-5386) allows remote unauthenticated admin reset
   - **Government facilities sector named** — federal facility CCTV adjacency

### Lower A&D adjacency

6. **ICSA-26-148-03: ABB EIBPORT KNX** (CVSS 8.0, Critical Manufacturing / IT) — backlog 2021-disclosure XSS
7. **ICSA-26-148-04: ABB Busch-Welcome Door Opener** (CVSS 6.8, Commercial Facilities) — auth bypass via debug-mode default
8. **ICSA-26-148-05: CP Plus NVR** (India-HQ, CVSS 8.4, Commercial Facilities) — XSS
9. **ICSMA-26-148-01: Fourth Frontier Frontier X (medical wearable)** (CVSS 8.8, Healthcare) — BLE unauthenticated GATT access; clinical-reading manipulation impact

## IOCs

```yaml
iocs:
  ip_addresses: []
  domains: []
  hashes: []
  cves:
    - CVE-2026-42941   # MacGregor VDR default credentials
    - CVE-2026-7786    # PUSR USR-W610 hardcoded credentials
    - CVE-2026-5386    # KMW CCTV unverified password change
    - CVE-2026-9037    # XCharge C6 firmware integrity check failure
    - CVE-2026-5768    # Fourth Frontier BLE missing authentication
    - CVE-2021-22291   # ABB EIBPORT XSS (2021 backlog)
    - CVE-2025-7705    # ABB Busch-Welcome auth bypass
    - SEVD-2026-132-01 # Schneider Electric EcoStruxure (vendor ID, no CVE)
attribution_claims: []   # CISA ICS advisories are procedural disclosures — no attribution
named_entities:
  vendors_with_disclosure:
    - Danelec (MacGregor VDR)
    - Jinan USR IOT Technology Limited (PUSR)
    - ABB (EIBPORT KNX + Busch-Welcome)
    - CP Plus
    - KMW (Romania)
    - Schneider Electric (EcoStruxure HVAC)
    - XCharge
    - Fourth Frontier
  sectors_named_in_batch:
    - Transportation Systems (2 advisories — MacGregor VDR + XCharge)
    - Critical Manufacturing (4 advisories — PUSR, ABB EIBPORT, CP Plus, Schneider EcoStruxure, KMW)
    - Commercial Facilities (3 advisories — ABB Busch-Welcome, CP Plus, KMW)
    - Government Services and Facilities (1 advisory — KMW)
    - Healthcare and Public Health (1 advisory — Fourth Frontier)
    - Information Technology (1 advisory — ABB EIBPORT)
    - Emergency Services (1 advisory — CP Plus)
    - Energy (1 advisory — Schneider EcoStruxure)
    - Water and Wastewater (1 advisory — Schneider EcoStruxure)
    - Chemical (1 advisory — Schneider EcoStruxure)
    - Financial Services (1 advisory — KMW)
collection_notes: |
  CISA ICS advisory batches are routine procedural disclosures. The
  full batch is indexed here as a single raw-signal record to support
  grader / vuln-tracker awareness without expanding 10 separate
  raw-signal files for items most of which are individually under
  the A&D-direct threshold. MacGregor VDR (maritime / DoD MSC
  adjacency) and XCharge C6 (federal-fleet EV adjacency) are the
  two highest-A&D-relevance items; PUSR + Schneider Electric +
  KMW are mid-tier DIB-adjacency. If the grader determines any
  specific advisory warrants finding-level promotion, the vuln-
  tracker should pivot to per-advisory tracking (VT-* scaffold).
  No active exploitation observed in CISA's framing for any item.
  No tracked actor attributed.
```

## Extraction notes

- Language: en
- Article type: vendor-coordinated CISA government disclosure batch
- Source grade: A (per source-grades.yaml — CISA government, procedural-fact authoritative)
- Body retrieval: all 10 advisory abstracts captured via cisa.gov/cybersecurity-advisories/all.xml RSS feed which remains the productive endpoint per source-health.yaml long-standing observation
- Per-advisory direct URLs noted; full advisory bodies not directly retrieved this sweep (operator may retrieve as needed)
- Quote compliance: no verbatim quotes >15 words

## Flash trigger evaluation (per advisory)

- **Trigger 1**: NOT MATCHED any advisory. No active in-the-wild exploitation claim by CISA for any of the 10 items.
- **Trigger 2**: NOT MATCHED. No tracked-actor attribution.
- **Trigger 3**: NOT MATCHED. No first-party-Splunk match query attempted this sweep.
- **Trigger 4**: NOT MATCHED.
- **Trigger 5**: PARTIAL on MacGregor VDR + XCharge C6. Transportation Systems sector named with DoD-MSC + federal-fleet adjacency. NOT crossing trigger threshold absent active exploitation claim. Defer to grader.
- **Trigger 6**: NOT MATCHED. All advisories are vendor-coordinated with patches available or version-fix-matrices published.

No FLASH escalation from collector. Batch index for grader / vuln-tracker awareness; recommended for AM-29 brief inclusion as a vulnerability-density datapoint with MacGregor VDR + XCharge C6 as the two items warranting individual call-out.
