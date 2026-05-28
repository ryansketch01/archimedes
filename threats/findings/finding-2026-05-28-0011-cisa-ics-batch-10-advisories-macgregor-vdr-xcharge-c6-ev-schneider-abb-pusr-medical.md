---
finding_id: finding-2026-05-28-0011-cisa-ics-batch-10-advisories-macgregor-vdr-xcharge-c6-ev-schneider-abb-pusr-medical
created_at: 2026-05-28T16:21:00-04:00
graded_by: grader
grading_run_id: afternoon-20260528-160000
grading_mode: scheduled_brief
test: false

# Core grading
digraph: A2
source_reliability:
  grade: A
  source_name: "CISA — Cybersecurity and Infrastructure Security Agency (ICS Advisory batch)"
  source_yaml_id: cisa-advisories
  grade_rationale: >
    Pre-assigned A per source-grades.yaml. CISA ICS advisories are
    vendor-coordinated disclosures with procedural-fact A-grade
    authority (CVE existence, CVSS scoring, affected/fixed versions,
    sector classification, geographic deployment).
  provisional: false
credibility:
  grade: 2
  checklist_passed:
    - probably_true_ttp_consistent_with_corpus_baseline_ics_disclosure_pattern_vendor_coordinated_release_with_patches_available_at_disclosure
    - probably_true_no_contradicting_a_b_grade_source
    - probably_true_technical_claims_internally_coherent_cve_assignments_cvss_scoring_affected_versions_all_procedurally_verifiable_per_individual_advisory
  rationale: >
    CISA ICS advisories are vendor-coordinated disclosures. Each
    individual advisory in the batch carries vendor-confirmed patch /
    mitigation status. Single-source-on-disclosure-side (CISA-vendor
    pair) but the advisories' procedural facts are authoritatively
    A-graded by CISA's pre-publication verification process. Grade 2
    (Probably True) — not Confirmed because individual exploitation-
    status claims are CISA-vendor-paired only, but the disclosure facts
    themselves are A-grade-authoritative. No contradicting source.
corroboration:
  independent_sources:
    - cisa-advisories
    - vendor-coordinated-disclosure-per-advisory
  independent: false
  test_passed: >
    CISA + vendor pair per advisory is single-source on the disclosure
    layer. Procedural facts (CVE existence, CVSS, version-fix-matrices)
    are pre-publication-verified by CISA.
first_party_precedence:
  applied: false
  splunk_evidence: null
  rationale: >
    No tracked-actor IOCs; advisories are pre-active-exploitation
    procedural disclosures. Splunk hunt for affected-product
    deployment IS warranted at defenseclaw_local for the MacGregor
    VDR + XCharge C6 + PUSR + Schneider EcoStruxure footprint, but
    that hunt is vuln-tracker / analyst responsibility, not grader-
    side.
single_source_veto_applied: false   # vuln advisories on procedural facts are not WEP-claim subject to single-source veto
wep_ceiling: very_likely

# Cluster metadata
cluster:
  topic: "CISA ICS advisory batch — 9 ICS advisories + 1 medical-device advisory published 2026-05-28 08:00 EDT covering MacGregor VDR (maritime / DoD MSC adjacency), XCharge C6 EV charger (federal-fleet adjacency), Schneider Electric EcoStruxure, ABB EIBPORT KNX, PUSR USR-W610 (China-HQ vendor), KMW CCTV, ABB Busch-Welcome, CP Plus NVR, Fourth Frontier medical wearable"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-05-28-pm-007
  attribution_claims: []  # CISA ICS advisories are procedural — no attribution

# Inclusion eligibility
inclusion:
  eligible_for:
    - daily_brief_monitoring
    - weekly_synthesis
    - actor_profile_update

# Downstream handoff
analyst_review_required: false  # procedural ICS batch; analyst-review not required
red_team_review_required: false # procedural facts; no WEP claim subject to challenge
red_team_review: null
analysis_sections:
  sat_ach: null
  sat_kac: null

# Lifecycle
tlp: CLEAR
published_in_briefs: [2026-05-28-afternoon]
retracted: false
retraction_brief_id: null
---

# CISA ICS Advisory Batch — 10 Advisories Published 2026-05-28 — MacGregor VDR + XCharge C6 EV Top A&D Adjacency

## Summary

CISA on 2026-05-28 08:00 EDT published a routine ICS advisory batch of 9 ICS + 1 medical-device advisory. Two items carry the highest A&D adjacency: **ICSA-26-148-01 MacGregor Voyage Data Recorder G4e (Danelec, CVSS 8.3, Transportation/Maritime)** — VDRs are mandatory IMO equipment on commercial shipping including chartered DoD MSC sealift vessels, with multi-CVE cluster including default credentials (CVE-2026-42941), insufficient credential protection, weak password hashes, hardcoded credentials, and accessible-file exposure (pre-patch: < V5.250); and **ICSA-26-148-08 XCharge C6 EV Charging Controller (US-HQ, CVSS 9.8, Transportation Systems)** — firmware download integrity check failure (CVE-2026-9037) plus stack-buffer-overflow and insecure default initialization, enabling unauthorized persistent firmware install relevant to US government EV fleet electrification mandate. Medium A&D adjacency: PUSR USR-W610 (China-HQ vendor, CVSS 9.8, hardcoded admin credentials, manufacturing-floor bridging), Schneider Electric EcoStruxure (CVSS 5.5, cleartext storage, Modicon M171/M172 programming software), KMW CCTV (Romania, CVSS 9.1, unverified password change, government-facilities sector named). Lower A&D: ABB EIBPORT KNX backlog, ABB Busch-Welcome door opener, CP Plus NVR XSS, Fourth Frontier medical wearable BLE auth. No active exploitation claimed by CISA for any item. No tracked-actor attribution.

## Sources

### CISA ICS advisories (cisa-advisories, digraph: A)

- Batch URL: https://www.cisa.gov/news-events/cybersecurity-advisories
- Productive feed: https://www.cisa.gov/cybersecurity-advisories/all.xml
- Published: 2026-05-28T12:00:00Z (08:00 EDT)
- 10 advisories total — full per-advisory list with URLs in raw-signal pm-007

## Technical detail

### Highest A&D adjacency

**ICSA-26-148-01 — MacGregor VDR G4e** (Danelec, CVSS 8.3, Transportation/Maritime)
- Multi-CVE: CVE-2026-42941 (default credentials) + cluster of insufficient credential protection / weak password hashes / hardcoded credentials / accessible file/directory exposure
- Pre-patch versions: all < V5.250
- **DoD-MSC adjacency:** chartered logistics vessels supporting DoD strategic sealift may carry vulnerable VDRs. Supplier-chain visibility is the operator's call.
- URL: https://www.cisa.gov/news-events/ics-advisories/icsa-26-148-01

**ICSA-26-148-08 — XCharge C6 EV Charging Controller** (US-HQ, CVSS 9.8, Transportation Systems)
- CVE-2026-9037 (firmware integrity check failure + stack-based buffer overflow + insecure default initialization)
- **Federal-fleet adjacency:** US government EV electrification mandate raises federal-facility EV charging infrastructure security profile
- Worldwide deployment
- Firmware-update-authenticity bypass enables persistent unauthorized firmware install
- URL: https://www.cisa.gov/news-events/ics-advisories/icsa-26-148-08

### Medium A&D adjacency

**ICSA-26-148-02 — PUSR USR-W610 Wi-Fi/Ethernet Converter** (Jinan USR IOT, China-HQ, CVSS 9.8, Critical Manufacturing)
- CVE-2026-7786 (hardcoded administrative credentials in firmware image)
- Industrial-network bridging device; manufacturing-floor → office-IT crossover
- China-HQ vendor — DIB facilities running RS232/485-to-Ethernet bridging warrant PUSR inventory

**ICSA-26-148-07 — Schneider Electric EcoStruxure Machine Expert HVAC** (CVSS 5.5, Chemical / Critical Mfg / Energy / Water+Wastewater)
- SEVD-2026-132-01 (cleartext storage of sensitive information — source-code disclosure class)
- Programming software for Modicon M171/M172 logic controllers
- Schneider Electric estate is widespread in A&D-prime manufacturing-floor controls

**ICSA-26-148-06 — KMW CCTV Security Cameras** (Romania, CVSS 9.1, Government Services / Critical Mfg / Transportation / Financial / Commercial)
- CVE-2026-5386 (unverified password change — remote unauthenticated admin reset)
- Government facilities sector named — federal facility CCTV adjacency

### Lower A&D adjacency

- ICSA-26-148-03 — ABB EIBPORT KNX (CVSS 8.0, IT / Critical Mfg) — backlog 2021 disclosure (CVE-2021-22291 XSS)
- ICSA-26-148-04 — ABB Busch-Welcome Door Opener (CVSS 6.8, Commercial Facilities) — CVE-2025-7705 auth bypass
- ICSA-26-148-05 — CP Plus 8-Ch NVR (CVSS 8.4, Commercial Facilities) — XSS
- ICSMA-26-148-01 — Fourth Frontier Frontier X Mobile App + Frontier X2 (CVSS 8.8, Healthcare) — CVE-2026-5768 BLE missing authentication for critical function

## IOCs surfaced

```yaml
cves:
  - CVE-2026-42941    # MacGregor VDR default credentials
  - CVE-2026-7786     # PUSR USR-W610 hardcoded credentials
  - CVE-2026-5386     # KMW CCTV unverified password change
  - CVE-2026-9037     # XCharge C6 firmware integrity check failure
  - CVE-2026-5768     # Fourth Frontier BLE missing authentication
  - CVE-2021-22291    # ABB EIBPORT XSS (2021 backlog)
  - CVE-2025-7705     # ABB Busch-Welcome auth bypass
  - SEVD-2026-132-01  # Schneider EcoStruxure (vendor ID, no CVE)
ip_addresses: []
domains: []
hashes: []
attribution_claims: []
```

## Relationship to existing findings

- **Vulnerability-density signal.** Pairs with morning finding-2026-05-28-0004 (NVD critical CVE batch — Samba CVE-2026-4408, X.Org CVE-2026-34000/34002, Red Hat Quay CVE-2026-32590) as a same-day CVE-disclosure-density datapoint.
- **Standing carry-forward density.** Combined with LiteSpeed CVE-2026-48172 + Exchange OWA CVE-2026-42897 KEV deadlines tomorrow (2026-05-29) and Nx Console / TanStack KEV deadlines 2026-06-10, the federal-compliance-deadline density across PM-28 → AM-29 → PM-29 brief windows is high.
- **VT-tracker pivots recommended:** vuln-tracker should pivot to per-advisory VT-* scaffolds for MacGregor VDR + XCharge C6 (highest A&D adjacency) at minimum.

## Open questions for analyst

- **Vuln-tracker per-advisory pivot.** MacGregor VDR + XCharge C6 + PUSR + Schneider EcoStruxure all warrant VT-* scaffold consideration. Vuln-tracker decision.
- **DoD-MSC supplier-chain visibility.** MacGregor VDR is mandatory IMO equipment; chartered DoD sealift vessel inventory exposure is the open question. Operator-level visibility call.
- **Federal-fleet EV charging posture.** XCharge C6 firmware-integrity bypass is relevant to federal facility EV charging mandates. Compliance-track surfacing.
- **DIB Splunk hunt candidate.** Affected-product deployment hunt across defenseclaw_local for MacGregor / XCharge / PUSR / Schneider EcoStruxure footprint.

## Source notes

- All quotes ≤15 words per Hard Rule 6.
- CISA ICS advisory bodies not directly fetched (all.xml RSS feed is productive endpoint per source-health long-standing observation).
- Per-advisory direct URLs preserved in raw-signal pm-007.
- No tracked-actor attribution; procedural disclosures.
