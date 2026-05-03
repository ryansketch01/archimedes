---
id: "023"
primary_name: "APT34"
aliases:
  - OilRig
  - Helix Kitten
  - Cobalt Gypsy
  - Crambus
  - Hazel Sandstorm
  - EUROPIUM
  - IRN2
  - ITG13
  - Greenbug
mitre_attack_id: G0049
mitre_attack_url: https://attack.mitre.org/groups/G0049/
type: "Nation-State APT"
attribution:
  nation: IR
  service: MOIS
  unit: "ITSecTeam (per third-party reporting; not officially confirmed)"
active_since: 2014
status: active
status_note: "Active in 2024–2025 against Middle East government, telecom, and energy; documented A&D-adjacent targeting via supply chain and ministry compromise."
motivation:
  - espionage
  - long-term-access
  - regional-strategic-collection
threat_level: MEDIUM                 # overall weighted 4.9 → MEDIUM; per-category espionage = HIGH (composite 8). See threat-box.yaml.
admiralty_grade: A2
tlp: CLEAR
dossier_version: 1
last_updated: 2026-05-01
last_reviewed: 2026-05-01
next_review_due: 2026-07-30
profile_path: threats/threat-actors/APT34/
iocs_path: threats/threat-actors/APT34/iocs.md
threat_box_path: threats/threat-actors/APT34/threat-box.yaml
related_actors:
  - "004"      # UNC1549 — parallel Iranian A&D-targeted playbook
  - "011"      # Charming Kitten — IRGC-IO equivalent, overlapping infrastructure
  - "022"      # MuddyWater — fellow MOIS actor
notes_for_session_9: |
  Initial dossier created Session 9 pre-work (2026-05-01). Profile is first-pass
  from public reporting through 2024-2025. All attribution inherits from cited
  sources per Hard Rule 2 — no Archimedes-originated attribution.
---

# APT34 — Threat Actor Profile

**Actor #023**

---

## Overview

APT34 is an Iran-aligned cyber espionage group that has operated continuously since at least 2014, with FireEye/Mandiant publicly first naming the group in 2017 after a sustained campaign against Middle Eastern financial, government, and energy organizations. Mandiant has assessed the group acts on behalf of the Iranian government, with reporting tying activity to the Iranian Ministry of Intelligence and Security (MOIS); Microsoft tracks overlapping activity as Hazel Sandstorm and previously as EUROPIUM. The group is most commonly known as **OilRig** in Palo Alto Unit 42 reporting and as **Helix Kitten** in CrowdStrike's taxonomy.

For the Archimedes target profile (mid-to-large US A&D contractor), APT34's relevance is **second-order but real**. The group's primary geographic focus is the Middle East — Saudi Arabia, the UAE, Israel, Iraq, Jordan, and the GCC more broadly — and its primary sectors are government, telecommunications, energy/oil-and-gas, and financial services. However, three patterns make it a tracked threat for an A&D prime: (1) documented supply-chain pivoting via compromised ministries and telecoms used as a relay into Western partners; (2) sustained interest in defense ministries and aerospace research organizations across the region, including Israeli targets per Mandiant 2023 reporting on the "Crambus" intrusion; and (3) operational tempo continuity across years of public exposure, including a 2023 eight-month dwell-time intrusion in a Middle Eastern government network that Symantec attributed to Crambus.

APT34's tradecraft has matured visibly across the last decade. Early operations leaned heavily on commodity-adjacent loaders (Helminth, ISMAgent, ISMDoor) and document-borne macros. Current-generation tooling — MENORAH, MARLIN, SideTwist, PowerExchange — reflects custom development tailored to specific intrusions, increased use of compromised Exchange servers as covert C2, and DNS-tunneling C2 patterns that are harder to detect at perimeter. The 2024 MENORAH disclosures by Trend Micro and Unit 42 demonstrate the group continues to ship new C# tooling against Saudi government targets.

The April 2019 "Lab Dookhtegan" leaks of OilRig source code, victim lists, and operator chat logs on Telegram represent the most consequential operational disclosure in APT34's history. The leak validated Mandiant/Unit 42 attribution and exposed several years of victim relationships, but did not visibly slow the group's operational tempo — APT34 simply rotated tooling and continued.

---

## Primary Targets

- **Government** — Middle East ministries (foreign affairs, defense, interior); per Mandiant/Unit 42, sustained focus on Saudi Arabia, UAE, Iraq, Jordan, Israel
- **Telecommunications** — Regional telecom providers used both as targets and as supply-chain pivots into government and corporate customers
- **Energy / Oil & Gas** — Saudi Aramco-adjacent, GCC oil ministries, regional oilfield services
- **Financial Services** — Middle Eastern banks (per Mandiant 2017 initial reporting)
- **Aerospace & Defense (regional)** — Defense ministries and aerospace research entities, particularly Israeli targets per Mandiant 2023 Crambus reporting
- **Universities & Research** — Regional universities supporting defense and energy research

**Geographic Focus:** Saudi Arabia, UAE, Israel, Iraq, Jordan, Lebanon, Kuwait, Qatar, Turkey. Western targeting is typically opportunistic via supply-chain compromise of regional partners rather than direct.

**A&D-prime relevance:** APT34 is unlikely to target a US A&D prime as primary objective. Risk is **supplier and partner compromise** — joint ventures with regional defense ministries, GCC subsidiary networks, or shared regional infrastructure may be reached via APT34 access to a regional partner.

---

## Signature Campaigns

| Campaign | Year | Description |
|---|---|---|
| Initial Mandiant disclosure | 2017 | Mandiant publicly names APT34; documents financial / government / energy targeting in the Middle East via weaponized Excel and PowerShell loaders |
| OopsIE / RGDoor activity | 2018 | Unit 42 documents OopsIE trojan and RGDoor IIS backdoor used against Middle East government targets |
| Lab Dookhtegan leak | Apr 2019 | Anonymous Telegram channel publishes OilRig source code, victim list, and operator chat logs; Mandiant and Unit 42 confirm authenticity |
| Karkoff / DNSpionage continuity | 2019 | Cisco Talos documents DNSpionage and Karkoff backdoors with overlapping infrastructure to OilRig |
| Out to Sea (Saitama backdoor) | 2022 | Unit 42 documents a phishing campaign against a Jordanian government official deploying the Saitama .NET backdoor |
| PowerExchange / Crambus intrusion | 2023 | Symantec documents an eight-month intrusion in a Middle East government network using the PowerExchange backdoor pivoting via compromised Exchange |
| MENORAH deployment | 2023–2024 | Trend Micro and Unit 42 disclose MENORAH C# backdoor against Saudi government, delivered via macro-laden Word documents |
| MARLIN and SideTwist updates | 2023–2024 | Updated SideTwist variant and MARLIN backdoor documented in continued GCC government targeting |

---

## TTPs (MITRE ATT&CK)

### Initial Access

| ID | Technique |
|---|---|
| T1566.001 | Spearphishing Attachment (weaponized Word/Excel with macros) |
| T1566.002 | Spearphishing Link (credential harvest pages, fake Microsoft login) |
| T1190 | Exploit Public-Facing Application (Exchange, IIS — installs RGDoor / PowerExchange) |
| T1199 | Trusted Relationship (compromised regional ministries used to relay into partners) |
| T1078 | Valid Accounts (credential reuse from prior intrusions) |

### Execution

| ID | Technique |
|---|---|
| T1059.001 | PowerShell (heavy use across multiple toolkits) |
| T1059.003 | Windows Command Shell |
| T1059.005 | Visual Basic (VBA macros in Office documents) |
| T1204.002 | User Execution: Malicious File |
| T1106 | Native API (custom C# tooling — MENORAH, SideTwist) |

### Persistence

| ID | Technique |
|---|---|
| T1505.003 | Server Software Component: Web Shell (RGDoor on IIS) |
| T1505.003 | Server Software Component: Exchange transport agent (PowerExchange covert C2) |
| T1053.005 | Scheduled Task |
| T1547.001 | Registry Run Keys / Startup Folder |
| T1546.003 | WMI Event Subscription |

### Defense Evasion

| ID | Technique |
|---|---|
| T1027 | Obfuscated Files (XOR, base64, custom encoding in MENORAH/MARLIN) |
| T1140 | Deobfuscate/Decode Files or Information |
| T1070.004 | File Deletion (post-collection cleanup) |
| T1036.005 | Masquerading: Match Legitimate Name (e.g., backdoor named after legitimate services) |

### Credential Access

| ID | Technique |
|---|---|
| T1003.001 | OS Credential Dumping: LSASS Memory |
| T1003.003 | OS Credential Dumping: NTDS |
| T1555 | Credentials from Password Stores |
| T1110 | Brute Force (credential stuffing where harvested creds available) |

### Discovery

| ID | Technique |
|---|---|
| T1087 | Account Discovery |
| T1018 | Remote System Discovery |
| T1057 | Process Discovery |
| T1082 | System Information Discovery |

### Command and Control

| ID | Technique |
|---|---|
| T1071.004 | Application Layer Protocol: DNS (DNSpionage / Karkoff DNS tunneling) |
| T1071.001 | Application Layer Protocol: Web (HTTP/HTTPS C2) |
| T1071.003 | Application Layer Protocol: Mail Protocols (PowerExchange uses Exchange Web Services as C2 channel) |
| T1573.002 | Encrypted Channel: Asymmetric Cryptography |
| T1090 | Proxy (use of compromised infrastructure as C2 relay) |

### Collection / Exfiltration

| ID | Technique |
|---|---|
| T1005 | Data from Local System |
| T1213 | Data from Information Repositories |
| T1041 | Exfiltration Over C2 Channel |
| T1567.002 | Exfiltration to Cloud Storage (occasional) |

---

## Malware Arsenal

| Malware | Type | Notes |
|---|---|---|
| Helminth | Backdoor | Original OilRig backdoor disclosed by Unit 42 in 2016; PowerShell + VBScript variants |
| ISMAgent / ISMDoor | Backdoor | Mid-generation tooling; documented by Unit 42 |
| OopsIE | Trojan | Unit 42 (2018); HTTP-based C2 |
| QUADAGENT | PowerShell backdoor | Unit 42 (2018) |
| RGDoor | IIS backdoor | Custom IIS module providing covert C2 via HTTP cookies |
| BONDUPDATER | Backdoor | DNS-tunneled C2; Unit 42 |
| DNSpionage / Karkoff | Backdoor | Cisco Talos (2019); DNS tunneling, used in DNS hijacking campaigns |
| Saitama | .NET backdoor | Unit 42 "Out to Sea" (2022); DNS-based C2, anti-analysis-heavy |
| PowerExchange | Backdoor | Symantec (2023); C2 via compromised Exchange transport agent — covert email-based C2 |
| MENORAH | C# backdoor | Trend Micro / Unit 42 (2023–2024); modular, anti-sandbox checks, used against Saudi government |
| MARLIN | Backdoor | Recent custom C# tooling against GCC government targets |
| SideTwist | Backdoor | C-language backdoor with multiple variants since 2021 |
| Drovorub-adjacent rootkit | (disputed) | Some early reporting linked OilRig to rootkit activity; later attribution clarification associates Drovorub primarily with APT28/GRU per NSA/FBI 2020 advisory — kept here for historical clarity, NOT counted toward APT34 capability |

**Source-of-record arsenal note:** This arsenal compiles tools attributed to APT34 across Unit 42, Mandiant, Trend Micro, Symantec, and Cisco Talos reporting. Where reporting attributes overlapping tooling to other Iranian clusters (e.g., shared infrastructure with Charming Kitten or MuddyWater), this is noted in the Connection Web rather than counted as APT34-exclusive capability.

---

## Infrastructure Patterns

- **Compromised regional infrastructure as C2** — heavy use of compromised regional web servers and Exchange instances rather than fresh registrations; reduces attribution noise and complicates geographic blocking
- **DNS tunneling tradition** — Helminth, BONDUPDATER, DNSpionage, Karkoff, and Saitama all use DNS as a C2 channel — defenders should treat anomalous DNS volume to atypical TLDs as a high-fidelity hunt
- **Exchange as covert channel** — PowerExchange (2023) uses compromised Exchange transport agents as C2, sending operator commands via internal email
- **Long dwell time** — Symantec's 2023 Crambus reporting documented an eight-month dwell in a Middle East government network; APT34 patiently expands access rather than burning it
- **Credential reuse across regional victims** — credentials harvested from one regional target are tested against partners and adjacent organizations
- **Rapid tooling rotation post-disclosure** — after the 2019 Lab Dookhtegan leak, tooling rotated within months; the group treats public disclosure as a tooling change trigger, not an operational pause
- **Web shells and backdoored IIS modules** — RGDoor and similar custom IIS components persist on perimeter web servers

---

## Known IOCs

This profile is a first-pass scaffold; current IOCs are limited. See `iocs.md` and `iocs.yaml` for the current indicator set, organized by:

- CVEs historically exploited
- Backdoor file hashes (per public reporting)
- DNS-tunneling C2 patterns
- Compromised Exchange / IIS indicators

The IOC sidecar starts sparse and grows as collector / grader feed APT34-attributed findings into the dossier.

**No first-party Splunk observations of APT34 infrastructure as of 2026-05-01.**

---

## Geopolitical Context

APT34 operates as part of Iran's broader cyber espionage ecosystem alongside MuddyWater (also MOIS-aligned), Charming Kitten (IRGC-IO), and other clusters. Mandiant's assessment is that APT34 supports MOIS strategic intelligence collection requirements; Unit 42 and CrowdStrike concur on Iranian state-aligned attribution.

The group's tempo and target selection track regional tensions:

- **Sustained focus on Saudi Arabia and UAE** reflects Iranian strategic interest in GCC adversaries
- **Israeli targeting** has intensified per Mandiant's 2023 Crambus reporting; aligns with Iran-Israel cyber escalation through 2024-2025
- **No documented operational pause** following major disclosures (2019 Lab Dookhtegan, 2023 Symantec) — the group continues to operate with adjusted tooling

For a US A&D prime, APT34 risk maps to:
- **Joint ventures with GCC defense ministries** — APT34 access to a partner ministry could pivot to shared programs
- **Subsidiaries operating in MENA region** — direct targeting risk
- **Shared regional infrastructure** — telecom or cloud providers serving both APT34 victims and the prime's regional ops
- **Israeli technology partners** — defense and aerospace tech partners targeted by APT34's 2023+ campaigns

The group is not a primary US-soil threat, but it is a credible second-order concern via the supply chain.

---

## Connection Web

- ⛓️ **[Actor #022 MuddyWater](../MuddyWater/profile.md)** — Fellow MOIS-aligned cluster; documented overlapping tooling and infrastructure in some Mandiant and Unit 42 reporting. Treat as separate group with periodic operational adjacency.
- ⛓️ **[Actor #011 Charming Kitten](../Charming-Kitten/profile.md)** — IRGC-IO counterpart with different operational tasking but occasional shared infrastructure or tooling per Microsoft Threat Intelligence reporting.
- ⛓️ **[Actor #004 UNC1549](../UNC1549/profile.md)** — Iranian-aligned (IRGC) actor with the most direct A&D playbook overlap; UNC1549 directly targets aerospace and defense, while APT34's A&D relevance is supply-chain-mediated.
- ⛓️ **Greenbug (Symantec taxonomy)** — Earlier Symantec reporting clustered some APT34 activity under "Greenbug"; treated as overlapping cluster rather than distinct actor.

---

## Defense Recommendations

1. **Hunt for DNS-tunneled C2** — Treat anomalous outbound DNS volume to atypical TLDs (.icu, .top, .tk) as high-fidelity hunt signal. Build detection on per-host DNS query volume baselines and entropy of subdomain labels (DNSpionage, BONDUPDATER, Saitama, Karkoff all use DNS C2).
2. **Audit Exchange transport agents** — PowerExchange (2023) installs as a custom transport agent on compromised Exchange. Inventory installed transport agents quarterly; alert on new or unsigned agents.
3. **IIS module integrity monitoring** — RGDoor persists as a custom IIS module. Hash-baseline IIS module inventory on perimeter web servers; alert on new or modified modules.
4. **Macro execution constraints in MENA-touching business units** — APT34 spearphishing payloads remain macro-heavy; enforce Office macro blocking for users in subsidiaries / business units transacting with GCC partners.
5. **Credential hygiene for regional partner accounts** — Treat credentials shared with Middle East joint-venture partners as elevated risk; enforce phishing-resistant MFA and review account access quarterly.
6. **Egress monitoring for compromised Exchange C2 patterns** — Email-based C2 (PowerExchange) blends into legitimate Exchange traffic; monitor for unusual internal-to-external email volume from privileged service accounts.
7. **Partner compromise notifications** — Establish notification protocols with regional partner SOCs; APT34 dwell time means a partner-side detection is often the earliest signal for a downstream prime.
8. **Hunt for SideTwist / MENORAH / MARLIN file artifacts** — Pull current YARA rules from Trend Micro and Unit 42 publications; deploy to EDR.

---

## References

- [MITRE ATT&CK G0049 — OilRig](https://attack.mitre.org/groups/G0049/)
- [Mandiant: APT34 — A previously unidentified Iranian threat actor (2017)](https://www.mandiant.com/resources/blog/apt34-new-targeted-attack-middle-east) — initial public attribution
- [Palo Alto Unit 42: OilRig research index](https://unit42.paloaltonetworks.com/tag/oilrig/) — sustained tooling and campaign reporting
- [Cisco Talos: DNSpionage Brings Out the Karkoff (2019)](https://blog.talosintelligence.com/dnspionage-brings-out-the-karkoff/)
- [Symantec: Crambus — New campaign in Middle East (2023)](https://symantec-enterprise-blogs.security.com/threat-intelligence/crambus-middle-east-government) — eight-month intrusion, PowerExchange disclosure
- [Trend Micro: APT34 deploys new MENORAH malware (2023)](https://www.trendmicro.com/en_us/research/23/i/apt34-deploys-phishing-attack-with-new-malware.html)
- [Palo Alto Unit 42: Out to Sea — Saitama Backdoor (2022)](https://unit42.paloaltonetworks.com/saitama-backdoor/)
- [Microsoft Threat Intelligence: Hazel Sandstorm (formerly EUROPIUM) profile](https://www.microsoft.com/en-us/security/blog/) — Microsoft's tracking of overlapping cluster
- Lab Dookhtegan Telegram leak (April 2019) — referenced via Mandiant/Unit 42 confirmation reporting; original leak channel not linked here per LEGAL-POLICY guidance on directly hosting / linking leaked operational material

---

*Profile authored 2026-05-01 (Session 9 pre-work) by `actor-profiler`. All attribution claims herein are inherited from cited sources per Hard Rule 2.*
