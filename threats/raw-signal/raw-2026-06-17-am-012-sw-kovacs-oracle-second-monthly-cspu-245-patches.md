---
raw_id: raw-2026-06-17-am-012-sw-kovacs-oracle-second-monthly-cspu-245-patches
collected_at: 2026-06-17T07:55:00-04:00
run_id: pre-brief-20260617-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: securityweek
  source_name: SecurityWeek
  source_url: https://www.securityweek.com/oracles-second-monthly-security-updates-deliver-245-patches/
  published_at: 2026-06-17T09:04:43+00:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [Oracle, CSPU, Critical Security Patch Update, June 2026, Communications, EBS, Enterprise Manager, monthly schedule]
triage_tags: [routine_patch_cycle, oracle_cspu_cadence_change, possible_other_signal_one_liner, no_specific_cve_singled_out]
iocs_extracted: false
iocs_count: 0
text_word_count: 145
promoted: false
rejected_at: 2026-06-17T08:24:00-04:00
rejection_id: reject-2026-06-17-0005
ttl_expires_at: 2026-09-15T07:55:00-04:00
---

# Oracle's Second Monthly Security Updates Deliver 245 Patches

**Source:** SecurityWeek (https://www.securityweek.com/oracles-second-monthly-security-updates-deliver-245-patches/)
**Author byline:** Eduard Kovacs
**Published:** 2026-06-17T09:04:43+00:00 (05:04:43 EDT)

## RSS-summary captured

> Oracle has released its June 2026 Critical Security Patch Update to fix vulnerabilities in Communications, EBS, Enterprise Manager and other products.

## Extraction notes

- **Language:** en
- **Publisher byline:** Eduard Kovacs (SecurityWeek)
- **Article type:** trade-press relay of Oracle vendor advisory (Oracle June 2026 CSPU schedule restructuring)
- **Upstream primary:** Oracle (vendor-self-disclosure)
- **Carry-forward:** Mentioned in 06:00 sweep notes as routine-patch-cycle coverage. Oracle moved to monthly CSPU schedule. 245 patches this month — Communications + EBS + Enterprise Manager + others.
- **Cross-walk:** No specific CVE singled out for active exploitation in window. Possible CVE-2026-35273 PeopleSoft Enterprise PeopleTools (KEV-listed-2026-06-12 retrospective-compliance-metrics phase) overlap given Oracle vendor-of-record but PeopleSoft was a prior month's CSPU. Article does not single out any CVE for active exploitation.
- **Hard Rule 6 preservation:** 15-word quote discipline preserved.
- **Hard Rule 2 preservation:** No tracked-actor attribution.
- **Raw IOC extraction invoked:** no

## Substrate observation for grader

T1/T6 FAIL (no specific CVE singled out for active exploitation). T2/T4/T5 FAIL (no tracked-actor or A&D-prime surface). Critical-override 0-of-4. Non-FLASH-eligible.

Possible 2026-06-17 morning brief Other Signal one-liner — Oracle CSPU cadence restructuring (monthly vs quarterly) is operationally noteworthy for A&D-prime patch management programs running Oracle Communications / EBS / Enterprise Manager footprint. Operator-deferred review.
