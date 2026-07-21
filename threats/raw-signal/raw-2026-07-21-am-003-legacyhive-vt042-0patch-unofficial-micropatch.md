---
raw_id: raw-2026-07-21-am-003
collected_at: 2026-07-21T07:36:00-04:00
run_id: pre-brief-20260721-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: bleepingcomputer
  source_name: "BleepingComputer"
  source_url: https://www.bleepingcomputer.com/news/security/windows-legacyhive-zero-day-flaw-gets-free-unofficial-patches/
  published_at: 2026-07-21T04:06:26-04:00
  originating_research: "ACROS Security / 0Patch (micropatch); Nightmare Eclipse (persona, original disclosure)"
match_reason:
  watchlist: []
  actors: []                       # Nightmare Eclipse = tracked persona/series, NOT a _roster.yaml actor
  vulnerabilities: [VT-042]        # LegacyHive; no CVE assigned
  keywords: [LegacyHive, Nightmare Eclipse, User Profile Service, profsvc, 0patch, ACROS Security, arbitrary hive load]
triage_tags: [tracked_vuln, patch_status_state_change, update_material, non_flash, grader_vuln_tracker_handoff]
iocs_extracted: true
iocs_count: 0                        # no CVE, no atomic IOCs
text_word_count: 340
promoted: false
disposition: update_material_vuln_tracker_and_existing_finding
related_finding: finding-2026-07-15-0002    # LegacyHive (VT-042) — existing finding this updates
vuln_tracker_target: VT-042
graded_at: 2026-07-21T08:22:00-04:00
grading_run_id: morning-20260721-080000
grader_note: >
  NOT a net-new finding and NOT a rejection. Factual PATCH-STATUS STATE CHANGE for VT-042
  (LegacyHive Windows profsvc LPE): an unofficial ACROS/0Patch micropatch is now available for
  Win10 2004+ / Server 2022+. UPDATE material for vuln-tracker (VT-042 patch_status ->
  unofficial-patch-available; update monitor_for set) and the existing finding-2026-07-15-0002.
  Still NO CVE (KEV-ineligible), NO official MSRC patch (Microsoft "actively investigating"),
  NO reported ITW. No grading action needed — state change only; no new claim to grade.
ttl_expires_at: 2026-10-19T07:36:00-04:00
---

# Windows LegacyHive zero-day flaw gets free, unofficial patches

**Source:** BleepingComputer (Sergiu Gatlan), 2026-07-21 ~04:06 EDT.

Free unofficial micropatches are now available for the recently disclosed Windows
"LegacyHive" User Profile Service (profsvc) privilege-escalation zero-day
(tracked as **VT-042**, Nightmare Eclipse 8th public drop; NO CVE, MSRC-silent as
of last tracking).

Key facts (per the relay):
- **Unofficial patch provider:** ACROS Security, via its 0Patch platform, released
  free micropatches. The fix works by having the vulnerable path load a temporary
  user-profile hive instead of the targeted admin user's hive.
- **Coverage:** Windows 10 2004 or later, and Windows Server 2022 or later.
  Systems older than Windows 10 2004 / Windows Server 2019 are NOT affected.
- **Official status:** Microsoft has NOT assigned a CVE-ID or released an official
  patch. A Microsoft spokesperson said it is "actively investigating the validity
  and potential applicability of these claims."
- **Mechanism (class level):** a non-admin user can mount another user's registry
  hive in full-access mode to read secrets or modify registry values affecting
  subsequent logins (standard-user → elevated context).
- **In-the-wild:** no active exploitation campaigns reported. Kevin Beaumont
  confirmed the exploit works after the PoC was released.

---

## Extraction notes

- Language: en
- Publisher byline: Sergiu Gatlan (BleepingComputer)
- Article type: security news
- Raw IOC extraction invoked: yes (no atomic IOCs present)
- Hard Rule 3: no PoC/exploit steps retrieved or copied; mechanism at class level
  only, consistent with prior VT-042 handling (PoC deliberately stripped upstream).
- Hard Rule 2: "Nightmare Eclipse" is a self-claimed persona/series, NOT a
  _roster.yaml actor; no attribution originated.
- Copyright (Hard Rule 7): one <15-word quote below, single use.

Verbatim vendor language (Microsoft, <15 words):
> "actively investigating the validity and potential applicability of these claims"

## Grader / vuln-tracker flags

- **PATCH-STATUS STATE CHANGE** on VT-042 (LegacyHive): previously UNPATCHED /
  MSRC-silent; now an unofficial 0Patch/ACROS micropatch is available for Win10
  2004+ / Server 2022+. Directly maps to a VT-042 `patch_status` update
  (candidate: unofficial-patch-available) and the dossier's monitor_for set.
  Vuln-tracker handoff. This item was noted in the 2026-07-21 06:00 FLASH commit
  message but no raw-signal file was written for it then — captured here for the
  morning-brief grader queue.
- Still NO CVE assignment (KEV-ineligible), NO official MSRC patch, NO reported
  ITW — the substantive change is the third-party micropatch availability only.
- A&D relevance: HIGH structural (ubiquitous Windows-endpoint LPE = ransomware /
  lateral-movement precursor); no named A&D victim.

## IOCs (from ioc-extraction skill)

```yaml
iocs:
  cve: []                            # no CVE assigned
  network_iocs: []
  file_iocs: []
attribution_claims: []               # persona self-claim only; no actor attribution (Hard Rule 2)
credential_exposure_detected: false
notes: "Unofficial 0Patch/ACROS micropatch = patch-status state change; no atomic indicators."
```
