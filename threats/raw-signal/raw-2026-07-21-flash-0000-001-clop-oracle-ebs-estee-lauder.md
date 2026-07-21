---
raw_id: raw-2026-07-21-flash-0000-001
collected_at: 2026-07-21T00:08:00-04:00
run_id: flash-sweep-20260721-000000
collection_mode: flash_sweep
source:
  source_yaml_id: bleepingcomputer
  source_name: BleepingComputer (Bill Toulas)
  source_url: https://www.bleepingcomputer.com/news/security/est-e-lauder-discloses-data-breach-via-oracle-e-business-flaw/
  published_at: 2026-07-20T18:39:30-04:00
  originating_research: "Estée Lauder breach-notification disclosure; Cl0p attribution per CrowdStrike (prior 2025 reporting, re-stated)"
match_reason:
  watchlist: []          # Estée Lauder is cosmetics — NOT on aerospace-defense.yaml
  actors: [Cl0p]         # roster #018 (aliases TA505, FIN11, GOLD TAHOE) — attribution re-stated, NOT new
  vulnerabilities: []    # CVE-2025-61882 NOT in threats/vulnerabilities/_index.yaml; distinct from tracked VT-043 CVE-2026-46817
  keywords: [Oracle E-Business Suite, Cl0p, Clop, data breach, ransomware, extortion]
triage_tags: [flash_sweep, non_flash, grader_queue, actor_profiler_awareness, tracked_actor_new_victim, anti_noise_no_new_attribution]
iocs_extracted: true
iocs_count: 0
text_word_count: 300
promoted: false
ttl_expires_at: 2026-10-19T00:08:00-04:00
---

# Estée Lauder discloses Oracle E-Business Suite breach — Cl0p (tracked #018) extortion campaign, new named victim

Non-FLASH grader-queue / actor-profiler-awareness item. Cl0p is a tracked roster
actor (#018), so this new named victim is worth surfacing — but it did NOT clear
a FLASH trigger (attribution is re-stated, not new; victim is non-A&D). Not
graded here; attribution recorded verbatim per Hard Rule 2.

## Procedural facts (per BleepingComputer relay)

- **Victim:** Estée Lauder Companies (cosmetics / beauty sector — NOT A&D).
  Notifying customers of a data breach affecting HR-system data (names,
  addresses, email, DOB, SSNs, passport numbers, bank-account info, health
  records, employment data).
- **Vulnerability:** a flaw in **Oracle E-Business Suite** used for HR
  operations. The relay ties this to the **Cl0p Oracle EBS mass-exploitation
  campaign; CVE-2025-61882** (the 2025 Oracle EBS zero-day). **NOTE — this is
  DISTINCT from the Archimedes-tracked open thread VT-043 CVE-2026-46817**; do
  not conflate. CVE-2025-61882 is not currently in the vuln index.
- **Attribution (verbatim):** "CrowdStrike confirmed that Clop had been
  exploiting the flaw since early August, 2025." This is the ESTABLISHED 2025
  campaign attribution, re-stated — not a new attribution event.
- **Other victims named in the article** (all previously-known 2025 Cl0p Oracle
  EBS victims, re-reported, NOT net-new here): Harvard University, University of
  Pennsylvania, Dartmouth College, University of Phoenix, The Washington Post,
  Logitech, GlobalLogic, Cox Enterprises, **Envoy Air** (American Airlines
  subsidiary — aviation, but not an A&D watchlist entity).
- No aerospace or defense entity named.

## Why non-FLASH

- **T2 (new attribution):** FAILS — Cl0p↔Oracle-EBS is the established 2025
  attribution; a new victim disclosure is not new attribution.
- **T5 (A&D-sector campaign):** FAILS — victim is cosmetics; no A&D prime named.
- **T1 / T6:** FAIL — CVE-2025-61882 long disclosed and patched; exploitation
  established since Aug 2025, not net-new.

Grader / actor-profiler value: adds a data point to the Cl0p (#018) victim
ledger and the ongoing Oracle EBS extortion arc. Candidate for a low-priority
UPDATE line in a scheduled brief, at the grader's discretion.

---

## Extraction notes

- Language: en
- Publisher byline: Bill Toulas (BleepingComputer, B-grade relay)
- Article type: blog / news
- Raw IOC extraction invoked: yes — NO atomic IOCs in the relay (no hashes /
  domains / IPs published). CVE-2025-61882 recorded by ID only (Hard Rule 3).

## IOCs (from ioc-extraction skill)

```yaml
iocs: []          # no atomic indicators in source
cve_references:
  - id: CVE-2025-61882
    context: "Oracle E-Business Suite flaw; Cl0p 2025 mass-exploitation campaign. By ID only."
    note: "DISTINCT from tracked VT-043 CVE-2026-46817. Not in vuln index."
attribution_claims:
  - actor: "Clop (Cl0p)"
    roster_id: "018"
    claim: "Exploiting the Oracle EBS flaw since early August 2025"
    attributing_source: "CrowdStrike (per BleepingComputer relay)"
    language: "confirmed"
    novelty: "re-statement of established 2025 attribution — NOT new"
```
