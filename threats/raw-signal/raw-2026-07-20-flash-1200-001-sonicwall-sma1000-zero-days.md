---
raw_id: raw-2026-07-20-flash-1200-001
collected_at: 2026-07-20T12:12:00-04:00
run_id: flash-sweep-20260720-120000
collection_mode: flash_sweep
source:
  source_yaml_id: securityweek
  source_name: SecurityWeek (relay of Volexity technical analysis)
  source_url: https://www.securityweek.com/sonicwall-zero-days-exploited-to-deliver-custom-malware-for-weeks-before-patch/
  published_at: 2026-07-20T10:11:05-04:00
  originating_research: "Volexity (assisted SonicWall investigation; UTA0533 tracking designation)"
match_reason:
  watchlist: []
  actors: []            # UTA0533 is a Volexity temp designation, NOT in _roster.yaml — no tracked-actor match
  vulnerabilities: []   # CVE-2026-15409 / -15410 NOT currently in threats/vulnerabilities/_index.yaml (net-new to corpus)
  keywords: [SonicWall, SMA1000, zero-day, edge-appliance, secure-remote-access, KnuckleBall]
triage_tags: [flash_sweep, non_flash, grader_queue, vuln_tracker_candidate, edge_appliance, n_day_kev_listed]
iocs_extracted: true
iocs_count: 6
text_word_count: 210
promoted: true
promoted_to_finding: finding-2026-07-14-0007        # state-change #2 (update-2026-07-20-0001) — same CVE pair; NOT a new finding. Attempted lift A2->A1/very_likely BLOCKED by red-team-20260720-181500 (common-upstream); finding stays A2/likely. Factual additions (~06-22 onset, UTA0533, tooling) shipped at likely.
promoted_at: 2026-07-20T16:10:00-04:00
ttl_expires_at: 2026-10-18T12:12:00-04:00
---

# SonicWall SMA1000 zero-days CVE-2026-15409 / CVE-2026-15410 — actively exploited by UTA0533 (Volexity), custom malware KnuckleBall

Net-new to the Archimedes corpus this sweep (NOT previously in the vuln index),
surfaced 2026-07-20 10:11 EDT via SecurityWeek (Eduard Kovacs) relaying a
Volexity technical analysis. Raw-signaled as a **non-FLASH grader / vuln-tracker
queue item** — did NOT clear a FLASH trigger this sweep (see disposition below).
Not graded here (grader's job); attribution recorded verbatim per Hard Rule 2.

## Procedural facts (per SecurityWeek relay of Volexity)

- Two vulnerabilities in **SonicWall SMA1000** secure remote access appliances:
  **CVE-2026-15409** and **CVE-2026-15410**.
- **Patches available 2026-07-14** (SonicWall hotfix versions); public disclosure
  also 2026-07-14. So NOT a zero-day-without-patch as of this sweep (patch ~6 days old).
- **CISA KEV: both listed since 2026-07-14** (dateAdded 2026-07-14, dueDate
  2026-07-17 — already past; knownRansomwareCampaignUse Unknown). Directly
  confirmed against the KEV catalog this sweep.
- **Active exploitation confirmed** — Volexity observed in-the-wild exploitation
  beginning as early as **2026-06-22**, ~3 weeks before disclosure.
- Actor: **UTA0533** (Volexity tracking designation). Volexity assessed the
  activity "more consistent with state-sponsored APT activity rather than a
  profit-driven cybercrime operation" (hedge preserved verbatim). **UTA0533 is
  NOT a `_roster.yaml` tracked actor** and no roster cross-walk is asserted.
- Tooling named: **KnuckleBall** (custom malware), **OrangeTail** (Java webshell),
  **Suo5** (open-source proxy).
- CVSS scores NOT provided in the relay; NOT independently established this sweep.
- Victim sectors / count NOT specified. **No aerospace or defense target named.**

---

## Extraction notes

- Language: en
- Publisher byline: Eduard Kovacs (SecurityWeek, B-grade relay)
- Originating research: Volexity (first-corpus-surface if adopted — no existing
  source-grades.yaml id; would be a provisional-grade first-surface for the grader)
- Article type: blog / vendor-relay news
- Raw IOC extraction invoked: yes
- Copyright: no verbatim quote >15 words used; Volexity hedge paraphrased/short-quoted once
- SMA1000 is an edge secure-remote-access appliance — structurally A&D-relevant
  (same perimeter/identity tier as tracked Fortinet FortiSandbox/FortiAuthenticator
  edge CVEs), but NO named A&D-prime/DIB victim in the reporting. A&D relevance is
  structural/indirect only; recorded for grader/vuln-tracker consideration, NOT asserted.

## IOCs (ioc-extraction skill output)

```yaml
cves:
  - id: CVE-2026-15409
    product: "SonicWall SMA1000 secure remote access appliance"
    cvss: null              # not provided in relay; not independently verified this sweep
    patch_status: patched   # hotfix 2026-07-14
    kev: true
    kev_added: 2026-07-14
    kev_due_date: 2026-07-17
    known_ransomware_campaign_use: Unknown
    exploitation: in_the_wild_confirmed_pre_disclosure   # since ~2026-06-22 per Volexity
  - id: CVE-2026-15410
    product: "SonicWall SMA1000 secure remote access appliance"
    cvss: null
    patch_status: patched   # hotfix 2026-07-14
    kev: true
    kev_added: 2026-07-14
    kev_due_date: 2026-07-17
    known_ransomware_campaign_use: Unknown
    exploitation: in_the_wild_confirmed_pre_disclosure
malware_tooling:
  - name: KnuckleBall
    type: custom_malware
  - name: OrangeTail
    type: java_webshell
  - name: Suo5
    type: open_source_proxy
network_iocs: []            # no atomic domains/IPs/hashes present in the SecurityWeek relay
attribution_claims:
  - actor_label: UTA0533
    attributed_by: Volexity
    confidence_language: "more consistent with state-sponsored APT activity"
    roster_match: false     # NOT in _roster.yaml; no cross-walk asserted (Hard Rule 2)
credentials_observed: false
```

## FLASH trigger disposition (why NON-flash)

- **T1 critical-cve-exploited:** exploitation confirmed, but (a) CVSS NOT established
  ≥9.0 from available sourcing this sweep, and (b) NOT net-new — CVEs disclosed +
  KEV-listed 2026-07-14 (6 days old, patch available, due date already past). Today's
  item is a retrospective technical deep-dive, not a fresh critical-CVE-exploitation
  disclosure — absorbs into next scheduled brief per anti-noise, not a FLASH.
- **T2 tracked-actor-attribution:** UTA0533 not in `_roster.yaml`. FAIL.
- **T3 first-party-IOC-hit:** Splunk null this sweep. FAIL.
- **T4 tracked-actor-TTP-change:** UTA0533 not tracked. FAIL.
- **T5 A&D-sector-campaign:** no named A&D victim, no multi-victim A&D confirmation. FAIL.
- **T6 zero-day-no-patch:** patch available since 2026-07-14. FAIL.

Recommended downstream: grader to weigh for next scheduled brief; **vuln-tracker to
consider opening a VT-NNN dossier** for the SonicWall SMA1000 CVE pair (net-new,
actively-exploited, KEV-listed edge-appliance CVEs absent from the current index).
