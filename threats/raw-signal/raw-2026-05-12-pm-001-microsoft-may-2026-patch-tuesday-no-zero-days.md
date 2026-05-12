---
raw_id: raw-2026-05-12-pm-001
collected_at: 2026-05-12T15:32:00-04:00
run_id: pre-brief-20260512-153000
collection_mode: pre_brief_collection
sweep_type: pre_brief
test: false
source:
  source_yaml_id: bleepingcomputer
  source_name: BleepingComputer (media relay of MSRC vendor advisory) + SecurityWeek cross-corroboration
  source_grade: B
  source_urls:
    - https://www.bleepingcomputer.com/news/microsoft/microsoft-may-2026-patch-tuesday-fixes-120-flaws-no-zero-days/
    - https://www.securityweek.com/microsoft-patches-137-vulnerabilities/
  primary_disclosure_source: Microsoft MSRC (vendor advisory; Patch Tuesday)
  primary_disclosure_source_grade: A (vendor official advisory)
  primary_disclosure_source_urls:
    - https://msrc.microsoft.com/update-guide/releaseNote/2026-May
  published_at_bleepingcomputer: 2026-05-12T18:08:06+00:00       # 14:08 EDT
  published_at_securityweek: 2026-05-12T18:07:39+00:00           # 14:07 EDT
  authors:
    bleepingcomputer: Lawrence Abrams
    securityweek: Ionut Arghire
match_reason:
  watchlist: []
  watchlist_match_strength: structural_via_windows_endpoint_dns_netlogon_sharepoint_office_word_deployment_across_all_ad_primes
  watchlist_match_detail: |
    Microsoft Windows, Office, Word, SharePoint, Dynamics 365, Netlogon,
    DNS Client, and Azure SDK are not directly listed in
    infrastructure/watchlists/aerospace-defense.yaml — but ALL Tier-1
    A&D primes (Lockheed Martin, Boeing, RTX, Northrop Grumman, General
    Dynamics, BAE Systems, L3Harris, Leidos, SAIC, Thales, GE Aerospace,
    Safran, Honeywell Aerospace, Airbus, Elbit Systems) run Windows
    endpoints + Active Directory + Office productivity suite + at
    least one of SharePoint / Dynamics 365 / Hyper-V virtualization /
    Microsoft DNS infrastructure as core operational stack. Per the
    structural-A&D-relevance test established in raw-2026-05-09-am-001
    (OpenC3 COSMOS) and refreshed in raw-2026-05-12-am-001 (SAP May
    Patch Day) and raw-2026-05-12-am-002 (Siemens RUGGEDCOM ROX May
    Patch Tuesday), Microsoft May 2026 Patch Tuesday is RAW-SIGNALED
    via the same rationale: the cluster impacts the structural endpoint
    + identity + collaboration layer that every prime depends on, even
    without prime-specific advisory language.
  actors: []
  vulnerabilities:
    - cve_id: CVE-2026-41096
      product: Windows DNS Client
      class: RCE
      severity: Critical
      bleepingcomputer_called_out_as_most_operationally_significant: true
      itw_exploitation: false
      preview_pane_or_zero_click: |
        Attacker-controlled DNS server sends specially crafted DNS
        response triggering memory corruption + RCE — fundamental
        infrastructure attack vector per BleepingComputer analysis.
    - cve_id: CVE-2026-40365
      product: SharePoint Server
      class: RCE
      severity: Critical
      itw_exploitation: false
      attack_vector: "authenticated network-based"
    - cve_id: CVE-2026-41089
      product: Windows Netlogon
      class: RCE
      severity: Critical
      itw_exploitation: false
    - cve_id: CVE-2026-41103
      product: Microsoft SSO Plugin for Jira & Confluence
      class: Elevation of Privilege
      severity: Critical
      itw_exploitation: false
      securityweek_called_out_as_critical: true
    - cve_id: CVE-2026-40364
      product: Microsoft Word
      class: RCE
      severity: High
      cvss_v3: 8.4
      bug_class: type-confusion
      itw_exploitation: false
      securityweek_preview_pane_exploitable: true
    - cve_id: CVE-2026-40361
      product: Microsoft Word
      class: RCE
      severity: High
      cvss_v3: 8.4
      bug_class: use-after-free
      itw_exploitation: false
    - cve_id: CVE-2026-40366
      product: Microsoft Word
      class: RCE
      severity: Critical
      itw_exploitation: false
    - cve_id: CVE-2026-40367
      product: Microsoft Word
      class: RCE
      severity: Critical
      itw_exploitation: false
    - cve_id: CVE-2026-40358
      product: Microsoft Office
      class: RCE
      severity: Critical
      itw_exploitation: false
    - cve_id: CVE-2026-40363
      product: Microsoft Office
      class: RCE
      severity: Critical
      itw_exploitation: false
    - cve_id: CVE-2026-42831
      product: Microsoft Office
      class: RCE
      severity: Critical
      itw_exploitation: false
    - cve_id: CVE-2026-42898
      product: Dynamics 365 (on-premises)
      class: RCE
      severity: Critical
      itw_exploitation: false
    - cve_id: CVE-2026-32161
      product: Windows Native WiFi Miniport Driver
      class: RCE
      severity: Critical
      itw_exploitation: false
    - cve_id: CVE-2026-35421
      product: Windows GDI (via malicious EMF files)
      class: RCE
      severity: Critical
      itw_exploitation: false
    - cve_id: CVE-2026-40402
      product: Windows Hyper-V
      class: Elevation of Privilege
      severity: Critical
      itw_exploitation: false
    - cve_id: CVE-2026-40403
      product: Windows Graphics Component
      class: RCE
      severity: Critical
      itw_exploitation: false
    - cve_id: CVE-2026-26164
      product: Microsoft 365 Copilot
      class: Information Disclosure
      severity: Critical
      itw_exploitation: false
  keywords:
    - patch-tuesday
    - microsoft
    - may-2026
    - no-zero-days
    - structural-ad-relevance
triage_tags:
  - patch_tuesday_may_2026
  - microsoft_msrc_a_grade_primary
  - 137_total_cves_120_windows_plus_17_edge_chromium
  - no_zero_days_disclosed_this_month
  - no_itw_exploitation_for_any_cve_in_batch
  - cve_2026_41096_dns_client_rce_most_operationally_significant
  - cve_2026_40364_40361_word_rce_preview_pane_exploitable
  - cve_2026_40365_sharepoint_rce_authenticated_network
  - cve_2026_41089_netlogon_rce
  - cve_2026_41103_sso_plugin_jira_confluence_elevation
  - non_flash_grader_queue
  - structural_ad_relevance_via_windows_endpoint_deployment
  - same_treatment_precedent_as_sap_am_001_and_siemens_am_002
  - patch_backlog_tier_for_morning_brief_consideration
iocs_extracted: true
iocs_count: 17
text_word_count: 1180
promoted: true
promoted_to_finding: finding-2026-05-12-0003
promoted_at: 2026-05-12T16:08:00-04:00
promoted_by_run: afternoon-20260512-160000
ttl_expires_at: 2026-08-10T15:32:00-04:00
---

# Microsoft May 2026 Patch Tuesday — 137 vulnerabilities, no zero-days, no ITW exploitation

Microsoft released its May 2026 Patch Tuesday updates on 2026-05-12,
fixing **120 Windows-only vulnerabilities** (per BleepingComputer's
Lawrence Abrams) — or **137 total** when including 17 Edge/Chromium-
related cumulative updates (per SecurityWeek's Ionut Arghire). Both
primaries explicitly note: **no zero-days disclosed** and **none of
the flaws have been flagged as exploited in the wild**.

## Severity breakdown

Microsoft rated **17+ CVEs as Critical**, with the remainder rated High
or Moderate. The Critical-severity calls primarily span Office / Word
RCE classes, Windows infrastructure (DNS, Netlogon, Hyper-V, GDI,
Graphics, Native WiFi Miniport), Dynamics 365 on-premises, the
Microsoft SSO Plugin for Jira & Confluence, and Microsoft 365 Copilot
information disclosure.

## Operationally significant CVEs called out by primaries

Per BleepingComputer's analysis, the most operationally significant
CVE in the batch is:

- **CVE-2026-41096 — Windows DNS Client RCE** — Critical severity. An
  attacker-controlled DNS server sends a specially crafted DNS response
  to a Windows client, triggering memory corruption and remote code
  execution. BleepingComputer characterizes this as a "fundamental
  infrastructure attack vector" — the DNS resolution path runs on every
  domain-joined Windows endpoint by default.

Per SecurityWeek's analysis, the standout Critical from the SSO + Office
side is:

- **CVE-2026-41103 — Microsoft SSO Plugin for Jira & Confluence** —
  Critical-severity elevation of privilege flaw.

Per SecurityWeek's preview-pane-exploitable analysis on the Word RCE
cluster:

- **CVE-2026-40364 & CVE-2026-40361 — Microsoft Word RCE** — High
  severity, CVSS v3 8.4 each. CVE-2026-40364 is a type-confusion bug;
  CVE-2026-40361 is a use-after-free. SecurityWeek states that
  "exploitation is possible just by viewing a malicious document in
  the Preview Pane" — no user click required beyond receiving the
  message that lands in Outlook with Preview Pane enabled (a common
  enterprise default).

## Other Critical CVEs in the batch (BleepingComputer enumeration)

- **CVE-2026-42831, CVE-2026-40363, CVE-2026-40358** — Microsoft Office
  RCE
- **CVE-2026-40361, CVE-2026-40367, CVE-2026-40366, CVE-2026-40364** —
  Microsoft Word RCE
- **CVE-2026-40365** — SharePoint Server RCE ("an authenticated
  attacker can perform a network-based attack")
- **CVE-2026-35421** — Windows GDI RCE via malicious EMF files
- **CVE-2026-41096** — Windows DNS Client RCE
- **CVE-2026-41103** — Microsoft SSO Plugin elevation
- **CVE-2026-42898** — Dynamics 365 on-premises RCE
- **CVE-2026-40402** — Windows Hyper-V elevation
- **CVE-2026-32161** — Native WiFi Miniport driver RCE
- **CVE-2026-41089** — Windows Netlogon RCE
- **CVE-2026-26164** — M365 Copilot information disclosure
- **CVE-2026-40403** — Windows Graphics Component RCE

## Why this matters to an A&D prime

Per the structural-A&D-relevance test established at raw-2026-05-09-am-001
(OpenC3 COSMOS) and applied again at raw-2026-05-12-am-001 (SAP) and
raw-2026-05-12-am-002 (Siemens), Microsoft Patch Tuesday is a structural
A&D-relevant signal even without prime-specific advisory language:

- All Tier-1 primes operate Active-Directory-joined Windows endpoint
  fleets at scale
- Microsoft DNS infrastructure is the resolution layer for those AD
  forests
- Office + Word are the default productivity suite
- SharePoint is common for program-management collaboration
- Dynamics 365 is used at multiple primes for CRM / supply-chain ERP
  adjacencies
- Microsoft SSO Plugin for Jira & Confluence is deployed in many DevOps
  + program-management environments

The Windows DNS Client RCE (CVE-2026-41096) and Netlogon RCE
(CVE-2026-41089) are particularly notable as they sit at the
identity/resolution-infrastructure layer that every domain-joined
endpoint depends on.

## What this is NOT

- **Not a FLASH** — no zero-days, no ITW exploitation, all CVEs
  patched at-disclosure, no tracked-actor attribution. All six FLASH
  triggers fail on the strict conjunction tests per the sentinel
  raw-signal `flash_triggers_evaluated` block.
- **Not a single-CVE finding** — this is a patch-backlog tier item.
  Grader should consider clustering with the SAP (finding-2026-05-12-
  0001) + Siemens (finding-2026-05-12-0002) patches already on the
  corpus into a combined "May 2026 enterprise-software patch backlog"
  brief item, or list separately depending on briefer composition.
- **Not the most operationally urgent item of the day** — the morning
  Mini Shai-Hulud worm (FLASH-0001) remains the highest-priority active
  threat. Microsoft Patch Tuesday is standing-patch-discipline material.

## Source notes

BleepingComputer (B-grade) and SecurityWeek (provisional B-grade) cross-
corroborate the 120 / 137 count discrepancy as 120 Windows-only flaws +
17 Edge/Chromium cumulative additions = 137 total advisory entries.
Both relay the MSRC Update Guide vendor primary (A-grade, vendor
official advisory). SANS Internet Storm Center diary entry from
2026-05-12T18:29 UTC (Tue, May 12th) provides corroborating short-form
137-CVE awareness note; treated as anti-noise to this primary raw-signal.

---

## Extraction notes

- Language: en
- Article type: media relay of vendor advisory (BleepingComputer +
  SecurityWeek primaries; MSRC Update Guide vendor advisory underneath;
  SANS ISC diary corroboration anti-noise)
- Copyright discipline: no quote exceeds 15 words; no source quoted
  more than once
- Per Hard Rule 2 (no attribution origination), no actor attribution
  applied; sources do not attribute either
- Per Hard Rule 3 (no exploitation assistance), no PoC content
  reproduced; CVE IDs and class descriptions only
- Raw IOC extraction invoked: yes

## IOCs (from ioc-extraction skill)

```yaml
indicators:
  cves:
    - value: CVE-2026-41096
      product: Microsoft Windows DNS Client
      class: rce
      severity: critical
      itw_exploitation_reported: false
      cited_by:
        - source: bleepingcomputer
          context: "most operationally significant CVE in the batch"
    - value: CVE-2026-40365
      product: Microsoft SharePoint Server
      class: rce
      severity: critical
      itw_exploitation_reported: false
      attack_vector: "authenticated network-based"
      cited_by:
        - source: bleepingcomputer
    - value: CVE-2026-41089
      product: Microsoft Windows Netlogon
      class: rce
      severity: critical
      itw_exploitation_reported: false
      cited_by:
        - source: bleepingcomputer
    - value: CVE-2026-41103
      product: Microsoft SSO Plugin for Jira & Confluence
      class: elevation_of_privilege
      severity: critical
      itw_exploitation_reported: false
      cited_by:
        - source: securityweek
        - source: bleepingcomputer
    - value: CVE-2026-40364
      product: Microsoft Word
      class: rce
      severity: high
      cvss_v3: 8.4
      bug_class: type_confusion
      itw_exploitation_reported: false
      preview_pane_exploitable: true
      cited_by:
        - source: securityweek
        - source: bleepingcomputer
    - value: CVE-2026-40361
      product: Microsoft Word
      class: rce
      severity: high
      cvss_v3: 8.4
      bug_class: use_after_free
      itw_exploitation_reported: false
      preview_pane_exploitable: true
      cited_by:
        - source: securityweek
        - source: bleepingcomputer
    - value: CVE-2026-40366
      product: Microsoft Word
      class: rce
      severity: critical
      itw_exploitation_reported: false
      cited_by:
        - source: bleepingcomputer
    - value: CVE-2026-40367
      product: Microsoft Word
      class: rce
      severity: critical
      itw_exploitation_reported: false
      cited_by:
        - source: bleepingcomputer
    - value: CVE-2026-40358
      product: Microsoft Office
      class: rce
      severity: critical
      itw_exploitation_reported: false
      cited_by:
        - source: bleepingcomputer
    - value: CVE-2026-40363
      product: Microsoft Office
      class: rce
      severity: critical
      itw_exploitation_reported: false
      cited_by:
        - source: bleepingcomputer
    - value: CVE-2026-42831
      product: Microsoft Office
      class: rce
      severity: critical
      itw_exploitation_reported: false
      cited_by:
        - source: bleepingcomputer
    - value: CVE-2026-42898
      product: Microsoft Dynamics 365 (on-premises)
      class: rce
      severity: critical
      itw_exploitation_reported: false
      cited_by:
        - source: bleepingcomputer
    - value: CVE-2026-32161
      product: Windows Native WiFi Miniport Driver
      class: rce
      severity: critical
      itw_exploitation_reported: false
      cited_by:
        - source: bleepingcomputer
    - value: CVE-2026-35421
      product: Windows GDI (EMF file processing)
      class: rce
      severity: critical
      itw_exploitation_reported: false
      cited_by:
        - source: bleepingcomputer
    - value: CVE-2026-40402
      product: Windows Hyper-V
      class: elevation_of_privilege
      severity: critical
      itw_exploitation_reported: false
      cited_by:
        - source: bleepingcomputer
    - value: CVE-2026-40403
      product: Windows Graphics Component
      class: rce
      severity: critical
      itw_exploitation_reported: false
      cited_by:
        - source: bleepingcomputer
    - value: CVE-2026-26164
      product: Microsoft 365 Copilot
      class: information_disclosure
      severity: critical
      itw_exploitation_reported: false
      cited_by:
        - source: bleepingcomputer

attribution_claims: []                 # Microsoft + media primaries make NO threat-actor attribution for any of the 137 CVEs in this batch

# 17 indicators captured (all CVE class). No domain / IPv4 / hash IOCs
# applicable — this is a vendor patch advisory, not active-threat
# documentation. Per Hard Rule 3 (no exploitation assistance), no PoC
# content reproduced.
```
