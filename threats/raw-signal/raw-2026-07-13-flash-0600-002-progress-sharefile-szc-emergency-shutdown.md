---
raw_id: raw-2026-07-13-flash-0600-002-progress-sharefile-szc-emergency-shutdown
collected_at: 2026-07-13T06:12:00-04:00
run_id: flash-sweep-20260713-060000
collection_mode: flash_sweep
test: false
source:
  source_yaml_id: securityweek
  source_name: SecurityWeek
  source_url: https://www.securityweek.com/progress-prompts-sharefile-storage-zone-controller-shutdown-amid-security-concerns/
  published_at: 2026-07-13T04:20:46-04:00
  originating_primary: Progress Software customer advisory (vendor self-disclosure)
  relay_grade: B
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: [CVE-2026-2699, CVE-2026-2701]
  keywords: [Progress, ShareFile, managed file transfer, pre-auth RCE, emergency shutdown]
triage_tags: [non_flash, developing, zero_day_watch, vuln_tracker_handoff, grader_queue_morning]
iocs_extracted: true
iocs_count: 2
promoted: false
ttl_expires_at: 2026-10-11T06:12:00-04:00
---

# Progress prompts ShareFile Storage Zone Controller shutdown amid security concerns

SecurityWeek (Ionut Arghire, in-window ~04:20 EDT): Progress Software
instructed ShareFile customers to manually shut down servers hosting their
Storage Zone Controllers "as soon as possible" while it assesses a credible
external security threat with cybersecurity experts. Progress states it found
no unauthorized access to any ShareFile accounts or customer data.

**Suspected vulnerabilities (per user speculation, NOT vendor-confirmed as
the vector):** CVE-2026-2699 (CVSS 9.8) and CVE-2026-2701 (CVSS 9.1),
disclosed/addressed in March, described as chainable for unauthenticated
config changes + malicious file upload → pre-auth RCE.

**Exploitation status:** Suspected, NOT confirmed. No zero-day confirmed.
No threat actor named. No IOCs. No A&D nexus stated.

---

## Why this is NON-FLASH (characterization only — grader adjudicates)

- **Trigger 1 (critical-CVE-exploited) FAILS:** CVE-2026-2699 is CVSS 9.8,
  but active exploitation is speculated by users, not confirmed; the vendor
  explicitly reports no unauthorized access. Active-exploitation condition
  not met.
- **Trigger 6 (zero-day-no-patch) FAILS on current evidence:** the named
  CVEs were patched in March (not unpatched); a new unpatched zero-day is
  plausible given the emergency "shut down your servers" posture but is not
  established. Exploitation unconfirmed.

## Why it still matters (watch rationale)

- Progress Software is the MOVEit vendor; ShareFile is a widely-deployed
  managed-file-transfer / content-collaboration product with plausible
  presence in enterprise and supply-chain environments (Progress/MFT is a
  historical Cl0p mass-exploitation target class).
- A vendor telling customers to power off production servers is an unusually
  strong precautionary signal — this is a **developing situation** that could
  escalate to a Trigger 1 or Trigger 6 FLASH if (a) exploitation is
  confirmed, (b) a new CVE is assigned, or (c) CISA KEV adds it.

**Recommend:** Route to 08:00 morning brief; hand to vuln-tracker as a watch
item (monitor for CVE assignment / confirmed exploitation / KEV add /
Progress follow-up advisory). Re-evaluate for FLASH on any confirmation.

## IOCs (FLASH-fast, inline)

- **CVE-2026-2699** — Progress ShareFile Storage Zone Controller; CVSS 9.8;
  pre-auth config change (chain component). Suspected-not-confirmed vector.
- **CVE-2026-2701** — Progress ShareFile Storage Zone Controller; CVSS 9.1;
  malicious file upload (chain component). Suspected-not-confirmed vector.
- No atomic network IOCs (IP / domain / hash) in the relay.
