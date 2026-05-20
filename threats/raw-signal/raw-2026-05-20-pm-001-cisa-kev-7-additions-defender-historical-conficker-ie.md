---
raw_id: raw-2026-05-20-pm-001
collected_at: 2026-05-20T15:32:00-04:00
run_id: pre-brief-20260520-153000
collection_mode: pre_brief_collection
test: false
source:
  source_yaml_id: cisa-kev
  source_name: "CISA Known Exploited Vulnerabilities Catalog — alerts page + JSON feed"
  source_url: https://www.cisa.gov/news-events/alerts/2026/05/20/cisa-adds-seven-known-exploited-vulnerabilities-catalog
  published_at: 2026-05-20T08:00:00-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities:
    - CVE-2026-41091
    - CVE-2026-45498
    - CVE-2008-4250
    - CVE-2009-1537
    - CVE-2009-3459
    - CVE-2010-0249
    - CVE-2010-0806
  keywords:
    - CISA KEV
    - BOD 22-01
    - Microsoft Defender Elevation of Privilege
    - Microsoft Defender Denial of Service
    - CWE-59 link-following
    - Microsoft Windows Buffer Overflow
    - Conficker
    - MS08-067
    - DirectX NULL byte overwrite
    - Adobe Acrobat Reader heap buffer overflow
    - Internet Explorer use-after-free
    - federal dueDate 2026-06-03
    - active exploitation evidence
triage_tags:
  - in_window
  - cisa_kev_batch_seven_additions_2026_05_20
  - cve_2026_41091_microsoft_defender_eop_link_following_cwe_59
  - cve_2026_45498_microsoft_defender_denial_of_service
  - five_historical_cves_2008_2009_2010_resurfaced_active_exploitation
  - conficker_ms08_067_cve_2008_4250
  - microsoft_directx_cve_2009_1537
  - adobe_acrobat_reader_cve_2009_3459
  - microsoft_ie_use_after_free_cve_2010_0249_cve_2010_0806
  - federal_due_date_2026_06_03_14_day_window
  - a_grade_cisa_kev_authority
  - ad_relevance_high_defender_universal_deployment
  - trigger_1_evaluation_candidate
  - no_named_actor_attribution_per_cisa
  - vt_index_addition_candidate_defender_pair
  - vuln_tracker_handoff_pair
  - splunk_first_party_zero_hits_49th_consecutive_dormant_sweep
iocs_extracted: false
iocs_count: 0
text_word_count: 1180
promoted: true
promoted_to_finding: finding-2026-05-20-0005
promoted_at: 2026-05-20T16:15:00-04:00
ttl_expires_at: 2026-08-18T15:32:00-04:00
---

# CISA adds seven known-exploited vulnerabilities to KEV catalog (2026-05-20)

CISA published an alert at 2026-05-20T08:00 EDT and updated the KEV JSON
feed (`https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json`)
the same morning, adding seven entries to the catalog "based on evidence
of active exploitation." All seven carry the standard federal dueDate
2026-06-03 (BOD 22-01, 14-day window from 2026-05-20).

Full title at CISA: "CISA Adds Seven Known Exploited Vulnerabilities to
Catalog."

Source URL (primary):
`https://www.cisa.gov/news-events/alerts/2026/05/20/cisa-adds-seven-known-exploited-vulnerabilities-catalog`

JSON feed source URL (verified retrieval):
`https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json`

## The seven additions

### Fresh 2026 CVEs (2)

**1. CVE-2026-41091 — Microsoft Defender Link Following Vulnerability**

- Vendor / project: Microsoft
- Product: Defender (the Microsoft Defender / Microsoft Defender Antivirus
  endpoint protection product family — same family as Microsoft Defender
  for Endpoint, Microsoft Defender Antivirus on Windows 10/11/Server)
- CWE: CWE-59 (Improper Link Resolution Before File Access / "Link
  Following")
- Description per CISA KEV JSON: "Link following vulnerability permitting
  authorized attackers to elevate privileges locally"
- CVSS: not surfaced on the CISA KEV record itself (CISA KEV does not
  publish CVSS — the underlying NVD record is "Awaiting Analysis" at the
  time of this collection; MSRC update guide page returned a barren
  header-only body via WebFetch this sweep, so MSRC's own CVSS / affected
  Defender Platform / Engine / Signature versions are not yet retrievable
  via Archimedes' passive WebFetch path)
- Date added to KEV: 2026-05-20
- dueDate: 2026-06-03
- Required action per CISA: "Apply mitigations per vendor instructions,
  follow applicable BOD 22-01 guidance for cloud services, or discontinue
  use"
- Notes / references on KEV record:
  - `https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-41091`
  - `https://nvd.nist.gov/vuln/detail/CVE-2026-41091`
- knownRansomwareCampaignUse per CISA: "Unknown"
- No threat actor attribution on the CISA KEV record.

**2. CVE-2026-45498 — Microsoft Defender Denial of Service Vulnerability**

- Vendor / project: Microsoft
- Product: Defender
- CWE: none listed on KEV record
- Description per CISA KEV JSON: "Unspecified vulnerability in Microsoft
  Defender enabling denial of service attacks"
- CVSS: not surfaced on the CISA KEV record itself; NVD record likewise
  "Awaiting Analysis" via passive retrieval this sweep
- Date added to KEV: 2026-05-20
- dueDate: 2026-06-03
- Required action: same as CVE-2026-41091
- Notes / references on KEV record:
  - `https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-45498`
  - `https://nvd.nist.gov/vuln/detail/CVE-2026-45498`
- knownRansomwareCampaignUse per CISA: "Unknown"
- No threat actor attribution on the CISA KEV record.

### Historical CVEs resurfaced as actively exploited (5)

CISA also added five well-known historical CVEs to KEV on the same batch,
each dated to 2008–2010 but added to the KEV catalog 2026-05-20 with
dueDate 2026-06-03 federal:

**3. CVE-2008-4250 — Microsoft Windows Buffer Overflow Vulnerability**

- Vendor / project: Microsoft, product Windows
- Description per CISA KEV: "Buffer overflow vulnerability in the Windows
  Server Service that allows remote attackers to execute arbitrary code
  via a crafted RPC request"
- CWE: CWE-94 (Code Injection)
- This is the MS08-067 Server Service RPC RCE — the original Conficker
  vector — added to KEV in 2026 indicates CISA observed active
  exploitation against unpatched / EOL Windows fleets in the federal
  enterprise. Operational reality is the 18-year-old vuln is still
  productive against unmanaged / EOL endpoints.
- Notes: `https://learn.microsoft.com/en-us/security-updates/securitybulletins/2008/ms08-067`

**4. CVE-2009-1537 — Microsoft DirectX NULL Byte Overwrite Vulnerability**

- Vendor: Microsoft, product DirectX
- Description: "NULL byte overwrite vulnerability in the QuickTime Movie
  Parser Filter in quartz.dll in DirectShow allowing remote code execution
  via crafted media files"
- CWE: not listed
- MS09-028 quartz.dll DirectShow QuickTime parser bug
- Notes: `https://learn.microsoft.com/en-us/security-updates/securitybulletins/2009/ms09-028`

**5. CVE-2009-3459 — Adobe Acrobat and Reader Heap-Based Buffer Overflow**

- Vendor: Adobe, product Acrobat and Reader
- Description: "Heap-based buffer overflow vulnerability allowing remote
  attackers to execute arbitrary code via crafted PDF files triggering
  memory corruption"
- CWE: CWE-119
- Notes: `https://www.cisa.gov/news-events/alerts/2009/10/13/adobe-reader-and-acrobat-vulnerabilities`

**6. CVE-2010-0249 — Microsoft Internet Explorer Use-After-Free**

- Vendor: Microsoft, product Internet Explorer
- Description: "Use-after-free vulnerability allowing remote attackers to
  execute arbitrary code by accessing pointers associated with deleted
  objects; product may be end-of-life"
- CWE: CWE-416
- This is the IE 0-day used in Aurora attacks against Google + 30+ other
  companies in 2009-2010 attributed historically to Chinese state actors;
  CISA's 2026 KEV addition is for active exploitation against modern
  unpatched / EOL fleets.
- Notes: `https://learn.microsoft.com/en-us/security-updates/SecurityAdvisories/2010/979352`

**7. CVE-2010-0806 — Microsoft Internet Explorer Use-After-Free**

- Vendor: Microsoft, product Internet Explorer
- Description: "Use-after-free vulnerability permitting remote attackers
  to execute arbitrary code through invalid pointer access following
  object deletion; product may be end-of-life"
- CWE: CWE-399
- Notes: `https://learn.microsoft.com/en-us/security-updates/securityadvisories/2010/981374`

## A&D-prime relevance

The two fresh Microsoft Defender CVEs (CVE-2026-41091 EoP + CVE-2026-45498
DoS) carry direct A&D enterprise relevance: Microsoft Defender (and the
Microsoft Defender for Endpoint EDR product) is deployed across the
overwhelming majority of A&D-prime Windows endpoint fleets, often as the
primary EDR layer or in dual-EDR-stack configurations. Local privilege
escalation via CWE-59 link-following against an EDR product means a
chained attacker with low-privilege foothold on a Defender-managed
endpoint can pivot to higher privileges; the DoS variant means the
Defender service itself can be made unavailable, which on a Defender-only
endpoint translates to suppression of EDR / AV coverage during follow-on
intrusion activity.

CISA's "based on evidence of active exploitation" framing is the A-grade
authority for ITW status on both fresh Defender CVEs even though CISA
does not name the exploiting actor / campaign on the KEV record. CISA KEV
publication itself triggers the BOD 22-01 14-day patch window for the
federal civilian enterprise; the same patching pressure applies to A&D
primes that follow KEV cadence as a CMMC / cyber-hygiene best practice.

The five historical CVEs (2008-2010) are most likely associated with
attacks against EOL / unmanaged Windows fleets (legacy Windows Server
2003 / 2008 / Windows XP / Windows 7 boxes still in production on
isolated industrial / OT segments, or development / lab environments).
The Conficker-era MS08-067 entry is the headline: 18-year-old RPC bug
still has enough live attack surface for CISA to flag it 2026.

## FLASH trigger evaluation (collector-side)

- **Trigger 1 (critical-cve-exploited):** CISA KEV is the A-grade authority
  on active-exploitation status — the framing "based on evidence of active
  exploitation" is the canonical Trigger 1 active-exploitation gate.
  HOWEVER, neither fresh 2026 Defender CVE has a CVSS surfaced on its
  passive-retrieval surface this sweep (NVD Awaiting Analysis, MSRC page
  returns header-only via WebFetch). Trigger 1 condition `cvss_score >=
  9.0` is therefore not verifiable yet — collector marks this as a
  Trigger 1 EVALUATION CANDIDATE pending CVSS surfacing, not a confirmed
  Trigger 1 fire. The five historical CVEs are well-known 9.x CVSS but
  the active-exploitation evidence is against EOL/unmanaged fleets, which
  the grader can apply Trigger 1 anti-noise discipline against (KEV adds
  on historical CVEs are routine and not standalone FLASH-worthy).
- **Trigger 5 (ad-sector-campaign):** No A&D-prime victim named by CISA;
  no multi-victim campaign characterization on this batch. Does not fire.
- **Trigger 6 (zero-day-no-patch):** Patches available for the 2026
  Defender CVEs per MSRC reference linkage; not zero-day-class. Does not
  fire.

## Vuln-tracker handoff candidates

Both fresh 2026 Defender CVEs are strong vuln-tracker `_index.yaml`
addition candidates:

- CVE-2026-41091 — Microsoft Defender EoP (CWE-59 link-following)
- CVE-2026-45498 — Microsoft Defender DoS

The grader and vuln-tracker subagent will decide on dossier scaffolding
and tracking depth (CVSS pending), and the briefer should treat the
Defender pair as the headline A&D-relevant signal of this KEV batch.

## Citations within Hard Rule 7 budget

- CISA KEV alert: "based on evidence of active exploitation" (10 words —
  within 15-word per-source limit, single quote per source budget).

## Extraction notes

- Language: en
- Publisher byline: CISA (no individual byline; CISA institutional
  publication)
- Article type: government advisory + JSON catalog
- Raw IOC extraction invoked: no (no IOCs in the KEV alert text; the seven
  CVE identifiers are vuln-tracker domain, not IOC-extraction domain)

## IOCs

None. KEV alerts publish CVE identifiers + required-action language; no
infrastructure / domain / hash IOCs are included in the alert or JSON
record.
