---
raw_id: raw-2026-06-15-am-001
collected_at: 2026-06-15T07:35:00-04:00
run_id: pre-brief-20260615-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: securityweek
  source_name: SecurityWeek
  source_url: https://www.securityweek.com/shinyhunters-claims-council-of-europe-hack/
  published_at: 2026-06-15T10:44:29+00:00
match_reason:
  watchlist: []
  actors: [ShinyHunters, UNC6240]
  vulnerabilities: [CVE-2026-35273]
  keywords: [ShinyHunters, Council of Europe, Tor leak site, 297 GB, payroll, PeopleSoft, BOD 26-04, dual-campaign visibility]
triage_tags: [new_attribution, active_campaign, non_ad_sector, single_source_volume_claim, peoplesoft_deadline_context]
iocs_extracted: true
iocs_count: 0
text_word_count: 580
promoted: true
finding_id: finding-2026-06-15-0001
promoted_at: 2026-06-15T08:08:00-04:00
ttl_expires_at: 2026-09-13T07:35:00-04:00
---

# ShinyHunters Claims Council of Europe Hack — 297 GB / 429K Files, Threats Release by 2026-06-16

**Source:** SecurityWeek, Ionut Arghire byline. Published 2026-06-15T10:44:29Z (06:44 EDT).
**URL:** https://www.securityweek.com/shinyhunters-claims-council-of-europe-hack/

## Article substance (paraphrased, no >15 word quotes)

ShinyHunters posted a Council of Europe entry on its Tor-based leak site on Sunday 2026-06-15, claiming to have stolen approximately 297 GB across over 429,000 files. The group has set a contact-by-June-16 deadline before threatened release. The Council of Europe has not publicly acknowledged the incident as of article publication time.

The claimed data scope per the leak-site post:

- Payroll data for 10,000+ employees, spanning 2011 through 2026
- 14,000+ CVs
- Contract and purchase order records
- Absence and illness reports
- Bank account information
- Performance evaluations
- Employee names, IDs, addresses, phone numbers, dates of birth
- Tax and social security information
- Medical records

Departments allegedly impacted include HR, the Secretariat, the Parliamentary Assembly, and the European Directorate for the Quality of Medicines & HealthCare (EDQM).

## Attribution language (preserved per Hard Rule 2)

- Per the article: ShinyHunters **claims** responsibility via the Tor leak-site post. No corroboration from Council of Europe, no third-party IR-firm attribution, no Mandiant or Unit 42 cross-binding. Pure self-claim layer.
- SecurityWeek explicitly references ShinyHunters' **separate** "zero-day vulnerability in Oracle PeopleSoft" campaign — i.e., the UNC6240 / CVE-2026-35273 cluster currently in the BOD 26-04 KEV catalog with deadline **EOD TODAY Sunday 2026-06-15**. Council of Europe breach is **NOT attributed to PeopleSoft per SW article** — the dual-campaign visibility is contextual, not same-CVE.
- "Misere" / Tchap, ShinyHunters / Council of Europe, ShinyHunters / PeopleSoft (UNC6240 / education sector) — these are three independent campaigns currently in Archimedes corpus or substrate window.

## IOC extraction

- **No IOCs disclosed** in SecurityWeek article (no domain, IP, hash, certificate, malware family, exploitation TTP)
- **No CVE attribution** for Council of Europe vector — SW article does not specify how the breach was achieved
- ShinyHunters Tor leak-site presence is general infrastructure pattern, not Archimedes-trackable IOC class

## A&D-prime / watchlist match

- **NONE.** Council of Europe is a 46-state intergovernmental human-rights body headquartered in Strasbourg, France. NOT an A&D supplier, NOT a US federal contractor, NOT on the aerospace-defense watchlist, NOT in CMMC/ITAR/DFARS supply chain. Cross-Atlantic political institution.
- EDQM (European Directorate for Quality of Medicines & HealthCare) is the pharma-quality directorate under Council of Europe — relevant to EU pharma regulatory context but NOT A&D-prime per Archimedes scoping.

## Grader / actor-profiler handoff considerations

1. **Single-source veto on volume claim** — SW is sole publisher relay; ShinyHunters self-claim is unverified by Council of Europe acknowledgment, Mandiant, or other A-grade primary. Volume claim "297 GB / 429K files" carries single-source-veto qualifier per INTEL-GRADING discipline.

2. **A1 reportability of *actor-claimed* leak-site post is the primary substrate** — the fact that ShinyHunters posted this claim today is itself a verifiable observation (SW screenshot / direct URL retrievable). Whether the underlying breach occurred at stated scope is the second-order claim that pends Council of Europe ACK.

3. **Dual-campaign actor visibility:** ShinyHunters is now visibly active across:
   - DentaQuest 2.6M (2026-06-12 PM substrate, EE health-sector cluster continuation)
   - Oracle PeopleSoft / UNC6240 mass theft (finding-2026-06-13-0002 + 0006, BOD 26-04 KEV deadline TODAY EOD Sunday 2026-06-15)
   - Council of Europe (this raw-signal, 2026-06-15)
   - And SW references *implied* additional cluster activity ("separate" zero-day campaign language)
   
   **However:** UNC6240 is the Mandiant-binding for the PeopleSoft cluster per finding-2026-06-13-0002. SW uses the "ShinyHunters" leak-site brand consistently across all three. ShinyHunters and UNC6240 relate as **brand vs. Mandiant-cluster** — actor-profiler decision whether to treat as unified roster entry or maintain separate dossiers TBD.

4. **PeopleSoft deadline-context framing:** This raw-signal is collected at the morning brief's final pre-deadline window (~T-16h to EOD Sunday 2026-06-15). ShinyHunters' Council of Europe activity TODAY provides contextual flavor that the actor cluster is active mid-deadline-cycle — does NOT add net-new PeopleSoft-CVE substrate but does reinforce sustained-campaign-class actor signal.

5. **No FLASH eligibility (T2 fails on net-newness of attribution to existing-tracked actor):** ShinyHunters / UNC6240 are already in Archimedes substrate as active cluster; this is the third visible campaign attribution within a week. T2 attribution-FLASH requires NEW attribution of NEW campaign or actor to a tracked roster entry. UNC6240 / ShinyHunters connection is not net-new in this raw-signal.

6. **Not on `_roster.yaml`:** Neither "ShinyHunters" nor "UNC6240" appears in the 24-actor roster as of 2026-05-10 last_updated. /new-actor decision substrate has been building across:
   - finding-2026-06-10-pm-006 (Oracle PeopleSoft mass data theft, BleepingComputer)
   - finding-2026-06-11-pm-002 (Oracle PeopleSoft 100 orgs / 40GB Mandiant Carmakal)
   - finding-2026-06-12-pm-001 (CISA KEV CVE-2026-35273 PeopleSoft 3-day deadline ransomware-use tagged)
   - finding-2026-06-13-0002 (UNC6240 / ShinyHunters Mandiant primary, education-sector 68% concentration)
   - finding-2026-06-13-0006 (Mandiant GTIG primary direct retrieval expanded IOC set)
   - This raw-signal — Council of Europe dual-campaign visibility
   
   **Operator-deferred /new-actor decision substrate continues to strengthen.** Recommend actor-profiler review window after PeopleSoft deadline cycle closes EOD Sunday.

## Extraction notes

- Language: en
- Publisher byline: Ionut Arghire
- Article type: news / blog
- Publisher independence: single publisher relay (SW only at this surface time); BleepingComputer / THN / SA had not posted by 07:30 EDT sweep close
- IOC extraction: 0 IOCs (no domains, IPs, hashes, malware families disclosed in source)
- Attribution: ShinyHunters self-claim via Tor leak site, NO third-party IR-firm or Council of Europe ACK
- A&D match: NO
- Roster match: SOFT (ShinyHunters / UNC6240 substrate-active but not on roster; /new-actor decision pending)
- Vulnerability match: SOFT (article references separate PeopleSoft / CVE-2026-35273 campaign but Council of Europe attribution NOT tied to PeopleSoft per SW)
- FLASH evaluation: T1 NEGATIVE (no CVE in article), T2 NEGATIVE (no net-new attribution to tracked actor — ShinyHunters/UNC6240 already in substrate), T3 NEGATIVE (Splunk sentinel 10/10 clean), T4 NEGATIVE (no net-new TTP documented), T5 weak-NEGATIVE (multi-victim but non-A&D), T6 NEGATIVE (no CVE in article)
- Hard Rule 7: 0 verbatim quotes over 15 words; data-scope list paraphrased
- Hard Rule 2: ShinyHunters self-claim preserved verbatim; no Archimedes-originated attribution added
