---
raw_id: raw-2026-07-22-flash-0600-001
collected_at: 2026-07-22T06:14:00-04:00
run_id: flash-sweep-20260722-060000
collection_mode: flash_sweep
source:
  source_yaml_id: securityweek
  source_name: "SecurityWeek"
  source_url: https://www.securityweek.com/oracle-patches-over-1400-vulnerabilities-with-quarterly-security-updates/
  published_at: 2026-07-22T05:33:12-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: [CVE-2025-61882, CVE-2026-46817]
  keywords: [Oracle, "Critical Patch Update", "Oracle E-Business Suite", "quarterly patch"]
triage_tags: [non_flash, patch_release, oracle_cpu, vuln_tracker_handoff, oracle_ebs_thread, no_ad_nexus, no_actor_attribution]
iocs_extracted: true
iocs_count: 0
text_word_count: 210
promoted: false
ttl_expires_at: 2026-10-20T06:14:00-04:00
---

# Oracle July 2026 Critical Patch Update — 1,400+ vulnerabilities patched (routine quarterly; Oracle-EBS thread relevance)

**State this window (00:00→06:00 EDT):** SecurityWeek relayed Oracle's **July 2026
Critical Patch Update (CPU)**, its regular quarterly release, patching **1,400+
vulnerabilities** across the Oracle product portfolio. Per the article, many of the
fixed flaws were "likely discovered by AI."

## Why raw-signaled (non-FLASH, vuln-tracker handoff)

Oracle E-Business Suite is a **standing tracked thread** in the corpus (Cl0p /
Oracle EBS CVE-2025-61882 mass-exploitation; VT-043 CVE-2026-46817). Oracle's
quarterly CPU is the mechanism by which EBS security fixes ship, so this bundle is
structurally relevant to the vuln-tracker's Oracle-EBS dossier maintenance and to
the grader for any morning-brief UPDATE. Surfacing it so the EBS thread's patch
posture stays current.

**Not a FLASH — no trigger met:**
- Routine n-day **patch release**, not a zero-day (T6 fails).
- **No active-exploitation claim** attached to any specific CVE in this bundle at
  the relay level; the CPU is a preventive quarterly (T1 fails — no CVSS≥9.0 + ITW
  + A-grade on a named CVE).
- **No tracked-actor attribution** (Hard Rule 2; T2/T4 fail).
- **No A&D / DIB / watchlist entity** named (T5 fails).

Disposition: absorb into a scheduled brief as UPDATE material at the grader's
discretion; hand to vuln-tracker for the Oracle-EBS dossier. Per-CVE triage against
the EBS thread requires fetching the Oracle CPU advisory matrix — deferred to the
grader/vuln-tracker (out of FLASH-fast scope). No FLASH warranted.

## Extraction notes

- Language: en
- Article type: trade-press relay (SecurityWeek) of a vendor patch bundle
- Raw IOC extraction invoked: yes — no atomic IOCs present in a CPU announcement
- Vuln-tracker handoff candidate: yes (Oracle-EBS standing thread patch-posture)

## IOCs (from ioc-extraction skill)

```yaml
atomic_iocs: []          # no C2 / hashes / domains — vendor patch announcement
cve_references:
  - id: "Oracle July 2026 CPU (bundle)"
    product: "Oracle product portfolio (1,400+ CVEs; incl. E-Business Suite)"
    type: "Quarterly Critical Patch Update — mixed severities"
    exploitation_status: "no active-exploitation claim on a named CVE at relay level; preventive quarterly"
    note: "Structurally touches tracked Oracle-EBS thread (CVE-2025-61882 Cl0p; CVE-2026-46817 VT-043); per-CVE mapping deferred to vuln-tracker"
    flash_trigger: "none — n-day patch bundle, no ITW/actor/A&D nexus"
attribution_claims: []   # none
notes: "No PoC/exploit content (Hard Rule 3). Per-CVE matrix not fetched (FLASH-fast scope)."
```
