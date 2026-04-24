---
id: "006"
primary_name: "APT28"
aliases:
  - Fancy Bear
  - Forest Blizzard
  - Sofacy
  - Sednit
  - Pawn Storm
  - STRONTIUM
  - FROZENLAKE
  - BlueDelta
  - Fighting Ursa
  - Iron Twilight
  - GruesomeLarch
  - UAC-0001
  - TG-4127
  - Tsar Team
  - Group 74
mitre_attack_id: G0007
mitre_attack_url: https://attack.mitre.org/groups/G0007/
type: "Nation-State APT"
attribution:
  nation: RU
  service: GRU
  unit: "Unit 26165 (85th GTsSS)"
active_since: 2004
status: active
status_note: "Highly active — Ukraine war operations and NATO defense targeting"
motivation:
  - espionage
  - hack-and-leak
  - influence-operations
  - nato-collection
  - ukraine-war-intelligence
threat_level: MEDIUM
admiralty_grade: A1
tlp: CLEAR
dossier_version: 2
last_updated: 2026-04-24
last_reviewed: 2026-04-18
next_review_due: 2026-07-17
profile_path: threats/threat-actors/APT28/
iocs_path: threats/threat-actors/APT28/iocs.md
threat_box_path: threats/threat-actors/APT28/threat-box.yaml
related_actors:
  - "007"      # Sandworm — sister GRU unit
  - "004"      # UNC1549 — parallel A&D targeting playbook
  - "003"      # Lazarus — parallel dream-job spearphishing
migrated_from: "intel-repository/threats/threat-actors/APT28"
---

## Dossier notes

**2026-04-24 — methodology migration.** `threat_level` changed from HIGH to
MEDIUM to match the weighted-overall of 6.60 in `threat-box.yaml`. This
reflects the Session 2A decision that weighted-overall determines authority
level rather than per-category maxima. APT28's espionage composite remains
10 (per-category HIGH) — see `primary_threat_level: HIGH` in
`threat-box.yaml`. Scoring values themselves were not changed; only the
headline threat_level field was brought into sync with doctrine.

# APT28 — Threat Actor Profile

**Actor #006**

---

## Overview

APT28 is one of the most prolific and well-documented state-sponsored threat actors on the planet. Operated by the GRU's Unit 26165, it has been active for two decades and is responsible for some of the most consequential cyberattacks in history — from the 2016 US election interference to sustained targeting of NATO defense infrastructure.

Unlike GRU Unit 74455 (Sandworm), which specializes in destructive operations, APT28's primary mission is **intelligence collection and hack-and-leak influence operations**. They steal data that matters strategically: military plans, diplomatic cables, election infrastructure, and defense logistics. Then — when it suits Moscow — they leak it.

The group has dramatically shifted tradecraft in recent years. Where they once relied heavily on custom malware, APT28 now prioritizes **cloud identity compromise** — password spraying, OAuth token theft, and mailbox delegation abuse — making detection significantly harder. They're living off the land inside Microsoft 365, and most orgs can't see them.

---

## Primary Targets

- **Defense & Military** — defense ministries, military logistics, NATO allies, weapons suppliers
- **Government** — foreign ministries, diplomatic entities, intelligence agencies
- **Transportation & Logistics** — Ukraine aid supply chains, border crossing monitoring (cameras)
- **Media & Think Tanks** — election-adjacent organizations, political campaigns, NGOs
- **Critical Infrastructure** — energy, telecom, finance adjacent to conflict zones
- **Sports & International Organizations** — WADA, OPCW, 2016 Olympics

**Geographic Focus:** Ukraine (primary post-2022), NATO member states (US, UK, Germany, France, Poland, Estonia, Romania, Czech Republic, Turkey), global when politically motivated.

---

## Signature Campaigns

| Campaign | Year | Description |
|---|---|---|
| 2016 US Election | 2016 | DNC, DCCC, Clinton campaign hacks; data leaked via Guccifer 2.0/DCLeaks |
| Olympic Doping Operations | 2016–2018 | WADA, USADA, CAS hacks; leaked anti-doping records |
| Nearest Neighbor Campaign | 2022–2024 | Wi-Fi lateral movement attack; compromised org networks via nearby Wi-Fi |
| Operation RoundPress | 2023–2025 | XSS webmail exploitation (Roundcube, Horde, MDaemon, Zimbra) for mailbox data theft |
| Ukraine Aid Logistics Campaign | 2025 | Targeting Western logistics companies supporting Ukraine |
| CVE-2026-21509 Maritime/Defense Wave | Jan 2026 | 72-hour phishing blitz against defense ministries and transport operators in 9 Eastern European nations; cloud C2 via filen.io |
| UKR.net Credential Campaign | 2024–2025 | Automated 2FA bypass on Ukrainian webmail using compromised Ubiquiti routers |

---

## TTPs (MITRE ATT&CK)

### Initial Access

| ID | Technique |
|---|---|
| T1566.001 | Spearphishing Attachment (weaponized RTF/DOC/PDF) |
| T1566.002 | Spearphishing Link (credential harvest via fake login pages) |
| T1110.003 | Password Spraying (large-scale, Tor/VPN-routed) |
| T1190 | Exploit Public-Facing Application (Exchange, Roundcube, Cisco SNMP) |
| T1199 | Trusted Relationship (compromised government accounts used as relay) |
| T1557.004 | Adversary-in-the-Middle: Evil Twin (Wi-Fi Pineapple for credential capture) |

### Execution & Persistence

| ID | Technique |
|---|---|
| T1059.001 | PowerShell |
| T1203 | Exploitation for Client Execution (CVE-2026-21509, CVE-2023-23397) |
| T1546.015 | COM Hijacking (AUTHENTIC ANTICS, CLSID {D9144DCD-E998-4ECA-AB6A-DCD83CCBA16D}) |
| T1053.005 | Scheduled Tasks (e.g., "OneDriveHealth" task for COM hijack trigger) |
| T1098.002 | Additional Email Delegate Permissions (mailbox persistence) |

### Defense Evasion

| ID | Technique |
|---|---|
| T1027 | Obfuscated Files (XOR, RC4, base64 layering) |
| T1562.004 | Disable Firewall / Modify Rules |
| T1070.001 | Clear Windows Event Logs |
| T1036 | Masquerading (fake filenames, fake gov doc aesthetics) |

### Credential Access

| ID | Technique |
|---|---|
| T1187 | Forced Authentication (AUTHENTIC ANTICS OAuth intercept) |
| T1003.003 | OS Credential Dumping: NTDS |
| T1040 | Network Sniffing / Responder (NetBIOS Name Service poisoning) |
| T1557 | Adversary-in-the-Middle (OAuth token theft) |

### Lateral Movement & Collection

| ID | Technique |
|---|---|
| T1021.001 | Remote Desktop Protocol |
| T1021.002 | SMB/Windows Admin Shares |
| T1550.002 | Pass the Hash |
| T1092 | Air-Gap Jump via USB (Jaguar Tooth adjacent) |
| T1114.002 | Remote Email Collection (mailbox exfil via Outlook API) |

### Exfiltration

| ID | Technique |
|---|---|
| T1567.002 | Exfiltration to Cloud Storage (filen.io, Koofr, Icedrive, OneDrive) |
| T1048.003 | Exfiltration via SMTP (NotDoor Outlook backdoor) |

---

## Malware Arsenal

| Malware | Type | Notes |
|---|---|---|
| X-Agent / Sofacy | Modular RAT | Long-standing flagship implant; keylogger, file stealer |
| X-Tunnel | Encrypted tunneler | C2 traffic obfuscation |
| CHOPSTICK | Backdoor | HTTP/HTTPS/IMAP C2; used in DNC/DCCC ops |
| GooseEgg | Privilege escalation tool | Exploits CVE-2022-38028 (Windows Print Spooler); drops SYSTEM shells |
| AUTHENTIC ANTICS | Credential/token stealer | COM hijacking; steals Outlook OAuth tokens; exfils via Outlook API |
| HEADLACE | Backdoor | Diplomat-themed lure delivery; public service staging |
| NotDoor | Outlook VBA backdoor | 2026 active; SMTP exfiltration |
| SimpleLoader | Loader | XOR-encrypted multi-stage loader; CVE-2026-21509 delivery |
| CovenantGrunt | .NET backdoor | Modified Covenant framework; AES-256 C2 via cloud storage |
| BeardShell | Backdoor | Signal Messenger lure delivery; CERT-UA attributed |
| Jaguar Tooth | Cisco router malware | SNMP-deployed; exfil over TFTP; unauthenticated backdoor |

---

## Infrastructure Patterns

- **Cloud-as-C2** — Heavy abuse of legitimate cloud storage (filen.io, Koofr, Icedrive) for C2; traffic looks like normal HTTPS
- **Compromised infrastructure** — Uses hacked routers (Ubiquiti EdgeOS), government email accounts, legitimate webmail providers as relay/staging
- **Fast-flux domains** — Registers new domains same-day for delivery; rapid rotation after takedowns
- **Tor/VPN routing** — All password spraying routed through Tor and commercial VPNs to obscure origin
- **Webmail provider targeting** — Exploits XSS in Roundcube, Horde, MDaemon, Zimbra to steal mailbox sessions

---

## Known IOCs

See `iocs.md` for the full human-readable indicator list and `iocs.yaml` for the agent-queryable sidecar.

**Key CVEs actively exploited:**
- CVE-2026-21509 — Microsoft Office OLE/WebDAV bypass (2026 active, KEV-listed)
- CVE-2024-11182 — MDaemon XSS zero-day (Operation RoundPress; CISA KEV)
- CVE-2023-23397 — Microsoft Outlook NTLM credential theft (CVSS 9.8)
- CVE-2023-43770 — Roundcube XSS (Operation RoundPress)
- CVE-2023-38831 — WinRAR code execution
- CVE-2022-38028 — Windows Print Spooler privesc (GooseEgg)
- CVE-2017-6742 — Cisco SNMP RCE (Jaguar Tooth)

---

## Geopolitical Context

APT28's operations are directly tied to GRU strategic priorities. Since Russia's 2022 full-scale invasion of Ukraine, the group has focused heavily on:

1. **Ukraine war intelligence** — targeting defense ministries, military logistics, weapons suppliers, border monitoring infrastructure
2. **NATO alliance fragmentation** — hack-and-leak operations designed to embarrass governments and create distrust
3. **Election interference** — sustained targeting of democratic processes (US 2016, France 2017, Germany 2021, potential ongoing)
4. **Sanctions evasion intel** — monitoring anti-Russia NGOs, OPCW, and international oversight bodies

APT28's "hack-and-leak" model — steal it, then weaponize it in media — makes them particularly dangerous beyond the intrusion itself. The data becomes a weapon.

---

## Connection Web

- ⛓️ **[Actor #007 Sandworm](../Sandworm/profile.md)** — Sister GRU unit (Unit 74455); destructive operations (NotPetya, Ukraine power grid attacks). APT28 and Sandworm share infrastructure and sometimes operate in coordination. Sandworm destroys; APT28 steals.
- ⛓️ **[Actor #004 UNC1549](../UNC1549/profile.md)** — Iranian IRGC equivalent playbook: both use fake job lures against A&D targets; geopolitically aligned on anti-NATO objectives despite being separate nation-state actors.
- ⛓️ **[Actor #003 Lazarus Group](../Lazarus-Group/profile.md)** — DPRK counterpart; all three (APT28, Lazarus, UNC1549) now run variants of the "dream job" spearphishing playbook against defense sector.

---

## Defense Recommendations

1. **Patch CVE-2023-23397 immediately** — CVSS 9.8, Outlook fires on receipt, no user click needed
2. **Apply emergency Office patch for CVE-2026-21509** — used in active 2026 campaign within 24 hours of disclosure
3. **Enforce phishing-resistant MFA** — APT28's primary vector is credential theft; hardware tokens stop password spraying cold
4. **Audit mailbox delegation and OAuth consents** — hunt for suspicious delegate permissions and unexpected app consents in M365
5. **Disable legacy authentication** — NTLM relay and IMAP/POP3 attacks rely on it
6. **Monitor cloud storage traffic from endpoints** — filen.io / Koofr / Icedrive connections from non-user processes = red flag
7. **Patch webmail stacks** — Roundcube, MDaemon, Zimbra, Horde have all been exploited; if self-hosted, treat as high priority
8. **Threat hunt for COM hijacking** — specifically CLSID `{D9144DCD-E998-4ECA-AB6A-DCD83CCBA16D}` and "OneDriveHealth" scheduled tasks
9. **Block Tor exit nodes at perimeter** — password spray attempts route through Tor; block known exit node ranges
10. **Air-gap sensitive systems** — APT28 has demonstrated USB-based air-gap jumping capability

---

## References

- [MITRE ATT&CK: APT28 (G0007)](https://attack.mitre.org/groups/G0007/)
- [Trellix: CVE-2026-21509 Multi-Stage Campaign (Feb 2026)](https://www.trellix.com/blogs/research/apt28-stealthy-campaign-leveraging-cve-2026-21509-cloud-c2/)
- [Microsoft: GooseEgg — Forest Blizzard CVE-2022-38028](https://www.microsoft.com/en-us/security/blog/2024/04/22/analyzing-forest-blizzards-custom-tool-for-exploiting-cve-2022-38028-to-obtain-credentials/)
- [ESET: Operation RoundPress (webmail XSS)](https://www.welivesecurity.com/en/eset-research/operation-roundpress/)
- [NSA/CISA May 2025 Advisory: GRU Unit 26165 Targeting Western Logistics](https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/4193749/)
- [Unit 42: APT28 "Fighting Ursa" CVE-2023-23397 Exploitation](https://unit42.paloaltonetworks.com/cve-2023-23397-fighting-ursa/)
- [UK NCSC: AUTHENTIC ANTICS Malware Analysis](https://www.ncsc.gov.uk/files/Advisory-APT28-exploits-known-vulnerability.pdf)
- [DOJ 2018 Indictment: GRU Unit 26165 Officers](https://www.justice.gov/file/1080281/dl)

---

*Last Updated: 2026-04-03 · Migrated to Archimedes: Session 1*
