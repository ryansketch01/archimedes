---
raw_id: raw-2026-06-16-pm-002-cisa-rockwell-ics-five-advisory-cluster-critical-manufacturing
collected_at: 2026-06-16T15:35:00-04:00
run_id: pre-brief-20260616-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: cisa-advisories
  source_name: CISA Cybersecurity & Infrastructure Security Agency (ICS Advisories)
  source_url: https://www.cisa.gov/cybersecurity-advisories/all.xml
  published_at: 2026-06-16T12:00:00+00:00
match_reason:
  watchlist: [aerospace-defense]
  actors: []
  vulnerabilities: [CVE-2026-11317, CVE-2020-13573, CVE-2026-0646, CVE-2026-0647, CVE-2025-14272, CVE-2025-11694]
  keywords: [Rockwell Automation, CompactLogix, ControlLogix, GuardLogix, RSLinx, FLEX I/O, EtherNet/IP, FactoryTalk Analytics, PavilionX, CIP protocol, Critical Manufacturing]
triage_tags: [a_d_ics_relevant, critical_manufacturing_sector, vendor_psirt_substrate_via_cisa, cluster_advisory, possible_other_signal_pm_brief, possible_net_new_finding_grader_discretion]
iocs_extracted: false
iocs_count: 0
text_word_count: 720
promoted: true
promoted_at: 2026-06-16T16:00:00-04:00
promoted_to_finding: finding-2026-06-16-0005
promotion_type: net_new_finding
ttl_expires_at: 2026-09-14T15:35:00-04:00
---

# CISA ICS Advisory Cluster — Rockwell Automation (5 advisories, 2026-06-16)

**Source:** CISA All Cybersecurity Advisories Atom feed (https://www.cisa.gov/cybersecurity-advisories/all.xml)
**Publisher:** CISA (U.S. government primary, A1 per `source-grades.yaml` doctrine baseline)
**Published:** 2026-06-16T12:00:00+00:00 (08:00 EDT — inside the 07:30→15:30 EDT pre-brief window)
**Advisory IDs (CISA ICS-CERT):** ICSA-26-167-01 / 02 / 03 / 04 / 05

## Advisory 1 — Rockwell Automation FactoryTalk Analytics PavilionX (ICSA-26-167-01)

- **CVE:** CVE-2025-14272
- **CVSS v3:** 7.0
- **CWE:** Missing Authorization
- **Affected:** FactoryTalk Analytics PavilionX < 7.01
- **Critical infrastructure sectors:** Critical Manufacturing
- **Countries deployed:** Worldwide
- **Impact:** "improper authorization enforcement in API endpoints. This vulnerability can allow an unauthorized actor to execute privileged operations, including user/role management and other administrative actions."

## Advisory 2 — Rockwell Automation RSLinx Classic (ICSA-26-167-02)

- **CVE:** CVE-2020-13573 (third-party vulnerability, vintage)
- **CVSS v3:** 7.5
- **CWE:** Out-of-bounds Read (stack-based buffer overflow per CISA summary)
- **Affected:** RSLinx Classic ≤ 4.50.00
- **Critical infrastructure sectors:** Critical Manufacturing, Energy, Food and Agriculture, Water and Wastewater
- **Countries deployed:** Worldwide
- **Impact:** stack-based buffer overflow allowing remote arbitrary code execution; denial-of-service unresponsive state without self-recovery.

## Advisory 3 — Rockwell Automation Logix 5370 & 5570 Controllers (ICSA-26-167-03)

- **CVE:** CVE-2026-11317
- **CVSS v3:** 7.5
- **CWE:** Improper Resource Shutdown or Release
- **Affected:** CompactLogix 5370 ≤ 34.016, Compact GuardLogix 5370 ≤ 35.015, ControlLogix 5570 ≤ 35.015, GuardLogix 5570 36.012
- **Critical infrastructure sectors:** Critical Manufacturing
- **Countries deployed:** Worldwide
- **Impact:** denial-of-service condition that may result in a major nonrecoverable fault (MNRF).

## Advisory 4 — Rockwell Automation CompactLogix 5370 L1/L2/L3 (ICSA-26-167-04)

- **CVE:** CVE-2025-11694
- **CVSS v3:** 7.5
- **CWE:** Improper Validation of Integrity Check Value + Exposure of Sensitive System Information to an Unauthorized Control Sphere
- **Affected:** CompactLogix 5370 L1, L2, L3
- **Critical infrastructure sectors:** Critical Manufacturing
- **Countries deployed:** Worldwide
- **Impact:** denial-of-service via missing validation of sequence numbers and source IP addresses in the CIP protocol; abuse of exposed Connection IDs visible on web interface.

## Advisory 5 — Rockwell Automation FLEX I/O EtherNet/IP Adapters (ICSA-26-167-05) — **highest CVSS in cluster**

- **CVEs:** CVE-2026-0646 + CVE-2026-0647
- **CVSS v3:** **9.4**
- **CWEs:** Missing Release of Memory after Effective Lifetime + Missing Authentication for Critical Function
- **Affected:** 1794-AENTR V2.012, 1794-AENTRXT V2.012
- **Critical infrastructure sectors:** Critical Manufacturing
- **Countries deployed:** Worldwide
- **Impact:** unauthorized access, account takeover, loss of availability. CVE-2026-0646 = improper memory handling of CIP protocol requests causing adapter fault + loss of connection to associated I/O. CVE-2026-0647 = paired missing-authentication critical-function vulnerability.

## Extraction notes

- **Language:** en
- **Publisher byline:** CISA (no individual byline; institutional advisory)
- **Article type:** Vendor-PSIRT-derived CISA ICS-CERT advisory cluster (Rockwell Automation PSIRT advisories cross-walked into CISA ICS-CERT channel per standard CISA ICS pattern).
- **Raw IOC extraction invoked:** no (no IOCs — these are vulnerability advisories, not active campaign reports; no IPs / domains / hashes / samples surface in CISA advisory text)
- **Active exploitation cited:** **NO.** No CISA KEV listing for any of the 6 CVEs as of this sweep (5 most-recent KEV unchanged from FLASH-1200 baseline). All five advisories are vendor-discovered vulnerabilities with patches available; no campaign attribution; no ITW exploitation language.
- **Hard Rule 2 preservation:** no actor attribution claims to preserve — these are vulnerability advisories, not campaign reports.
- **Hard Rule 6 preservation:** quotes from CISA advisory text are short technical descriptions under 15-word cap.

## Substrate observation for grader

**A&D relevance — moderate-to-high on operational template inheritance:**

Rockwell Automation industrial control products are deeply embedded in A&D manufacturing-floor and supplier-network industrial bases:

- **CompactLogix / ControlLogix / GuardLogix programmable automation controllers** — widely deployed in A&D-prime manufacturing floors, factory automation, supplier networks (Tier-1/2 industrial subcontractors), build-line MES integration.
- **RSLinx Classic** — communications driver historically bundled with Rockwell PAC deployments; legacy installations persist in industrial estates.
- **FactoryTalk Analytics PavilionX** — analytics platform commonly inherited in A&D manufacturing OT/IT-converged estates.
- **FLEX I/O EtherNet/IP Adapters (1794-AENTR / 1794-AENTRXT)** — distributed I/O on EtherNet/IP fieldbus, common in DIB Tier-1/2 supplier manufacturing.

**No A&D-prime named victim**, but **operational-template inheritance applies broadly across the DIB manufacturing supplier network**. The CVE-2026-0646 + CVE-2026-0647 FLEX I/O cluster at **CVSS 9.4 unauthenticated** is the highest-severity entry and the most operationally-relevant for A&D Tier-1/2 supplier defenders to track now.

## Grader / briefer cues

- **Possible PM brief Other Signal one-liner** — A&D ICS cluster surface notification for DIB Tier-1/2 supplier defenders; FLEX I/O 9.4 unauthenticated entry is the headline.
- **Possible net-new finding candidacy** at grader discretion — would be a cluster-anchor digraph A1 finding (CISA vendor-PSIRT-derived A&D ICS substrate). No active exploitation cited; no actor attribution; substrate is vendor-confirmed-pre-publication vulnerability cluster only.
- **Vuln-tracker handoffs operator-deferred** — six distinct CVE dossier scaffolds (CVE-2026-11317, CVE-2020-13573, CVE-2026-0646, CVE-2026-0647, CVE-2025-14272, CVE-2025-11694) OR cluster-dossier-decision operator-deferred per Hard Rule 5 binding.
- **No FLASH-eligibility** — no Trigger-1 (no active exploitation), no Trigger-2 (no actor attribution), no Trigger-3 (no first-party Splunk hit), no Trigger-4 (no actor TTP delta), no Trigger-5 (no multi-victim campaign), no Trigger-6 (patches available). Pre-brief pre-brief substrate only.
- **CISA KEV pathway:** none of the 6 CVEs are KEV-listed; standing vendor PSIRT advisories cross-walked into CISA ICS-CERT channel only.
