---
id: "024"
primary_name: "APT37"
aliases:
  - ScarCruft
  - Scarcruft
  - Reaper
  - Group123
  - InkySquid
  - RedEyes
  - Ricochet Chollima
  - ATK4
  - StarCruft
  - Operation Daybreak
mitre_attack_id: G0067
mitre_attack_url: https://attack.mitre.org/groups/G0067/
type: "Nation-State APT"
attribution:
  nation: KP
  service: "Ministry of State Security (MSS) — per The Record's framing of ESET reporting; historically attributed by FireEye/Mandiant 2018 to North Korean state interests, with subsequent reporting (Kaspersky, Cisco Talos, ESET, Volexity) sustaining DPRK attribution"
  unit: null
active_since: 2012
status: active
status_note: "Active 2024–2026 with sustained Android and Windows operations. Most recent disclosed campaign (ESET, 2026-05-07): Sqgame card-game platform supply-chain compromise delivering BirdCall Android + Windows backdoor to ethnic-Korean populations in Yanbian, China since November 2024."
motivation:
  - espionage
  - civil-society-coercion
  - defector-tracking
  - regional-strategic-collection
threat_level: MEDIUM                # weighted overall 4.9 (MEDIUM) per /update-tracking 2026-05-10; espionage category HIGH (composite 8). Intent=3 Sector Association bound by evidence-minimum table — no A-grade source documents A&D-prime-direct targeting required for Intent=5; FireEye 2018 "aerospace" mention in South Korean industrial sector targeting is sector-shaped, not target-specific.
admiralty_grade: A2
tlp: CLEAR
dossier_version: 2
last_updated: 2026-05-10
last_reviewed: 2026-05-10
next_review_due: 2026-08-08
profile_path: threats/threat-actors/APT37/
iocs_path: threats/threat-actors/APT37/iocs.md
threat_box_path: threats/threat-actors/APT37/threat-box.yaml
related_actors:
  - "003"      # Lazarus Group — DPRK counterpart (RGB-attributed; operationally distinct from APT37/MSS)
  - "002"      # Stardust Chollima — DPRK financial sub-cluster (RGB; distinct from APT37)
notes_for_session_10: |
  First-pass dossier created 2026-05-09 from finding-2026-05-07-0004 (ESET via
  The Record; BirdCall / Sqgame supply-chain campaign). All attribution
  inherits from cited sources per Hard Rule 2 — no Archimedes-originated
  attribution. ESET attribution to APT37 is explicit high confidence per
  The Record's framing; historical DPRK lineage attribution predates Archimedes
  (FireEye/Mandiant 2018, Kaspersky 2016–2018, Cisco Talos 2017, Volexity 2021).

  Threat-box scoring completed 2026-05-10 via /update-tracking (Mode 2):
  weighted overall 4.9 → MEDIUM → auto-commit per doctrine authority table.
  Hard Rule 5 gate did NOT fire. Espionage category-tier composite 8 (HIGH)
  preserved per-category but does not trigger the gate; only weighted overall
  does. Operator-anticipated HIGH did NOT materialize for the same disciplinary
  reason that brought MuddyWater in at LOW one day earlier: per the methodology
  evidence-minimum table, Intent=5 (Target-Specific) requires "at least 1
  A-grade source documenting targeting of ad-prime-v1 profile" and no such
  source exists for APT37. A&D-direct targeting is undocumented in public
  reporting. FireEye 2018's listing of "aerospace" among South Korean industrial
  sector targeting supports Intent=3 (Sector Association), not Intent=5.
  Capability=5 lands cleanly on multi-A-grade sustained record. Splunk first-
  party zero hits over -30d at scoring time across the primary search set.
---

# APT37 — Threat Actor Profile

**Actor #024**

---

## Overview

APT37 is a North Korean state-aligned cyber espionage group operating since at least 2012, with FireEye (now Mandiant) publishing the most consequential public attribution profile in February 2018 ("APT37 (REAPER): The Overlooked North Korean Actor"). The group is also tracked as ScarCruft (Kaspersky), Reaper (FireEye/Mandiant), Group123 (Cisco Talos), InkySquid (Volexity), and RedEyes — a dense alias map reflecting independent observation by multiple Tier-1 vendors over more than a decade. Recent ESET reporting (relayed via The Record on 2026-05-07) attributes the group to the DPRK Ministry of State Security (MSS), distinguishing APT37 from the Reconnaissance General Bureau (RGB)-attributed Lazarus and Stardust Chollima clusters tracked elsewhere in the Archimedes roster.

For the Archimedes target profile (mid-to-large US A&D contractor), APT37's relevance is **indirect and structural**, not primary. The group's dominant targeting pattern is **civil-society coercion**: North Korean defectors, journalists covering DPRK affairs, NGOs and human-rights organizations engaged with refugee populations, South Korean policy researchers, and (since 2017) regional industrial sectors aligned with DPRK strategic intelligence requirements. Direct A&D-prime targeting has not been documented in public reporting. However, three structural factors keep the actor on the tracking list:

1. **Defense-think-tank and policy-research targeting** — historical APT37 reporting (Mandiant 2018, Kaspersky 2018, Cisco Talos 2017) documents occasional targeting of South Korean and US-based defense policy organizations and think tanks studying DPRK military programs. This is A&D-adjacent rather than A&D-direct, but partner-NGO compromise is a credible lateral-pivot vector for prime CTI teams that share intelligence with civil-society partners.
2. **Mobile-malware capability** — APT37 has documented Android tooling (RokRAT mobile variants, Konni Android, BirdCall Android variant per ESET 2026) that distinguishes it from the Archimedes roster's existing DPRK actors, both of which are Windows/macOS/cross-platform-but-not-mobile-primary. Mobile compromise of executive or policy-staff devices is a structural risk vector regardless of which specific cluster operates the tooling.
3. **Roster gap closure** — Archimedes' DPRK coverage prior to this scaffold consisted only of RGB-attributed actors (Lazarus, Stardust Chollima). APT37 (MSS-attributed per recent reporting) closes a structural gap in the corpus.

The most recent disclosed campaign — the **Sqgame supply-chain compromise** detailed by ESET via The Record on 2026-05-07 — reflects the group's continued operational tempo. APT37 compromised the Sqgame card-game platform at least as far back as November 2024 and used compromised Android APKs (delivered via web-browser download, bypassing Google Play's vetting) to install the **BirdCall** backdoor on victim devices. ESET researchers state that Windows variants of BirdCall also exist. Targeting concentrated on ethnic Koreans in the Yanbian Korean Autonomous Prefecture, China — a population ESET assesses to include North Korean refugees and defectors. ESET notified Sqgame in December 2025; remediation status is not stated in the source. **No A&D entity, defense contractor, or DIB victim is named in the Sqgame disclosure.**

APT37's tradecraft has matured visibly across the last decade. Early operations (2012–2017) leaned on Korean-language spearphishing with HWP (Hancom Office) document-borne exploits and CVE-2018-4878 Flash zero-day exploitation. Mid-generation tooling (2017–2021) introduced **RokRAT** (Cisco Talos 2017; one of the most-tracked APT37 implants), **DOGCALL**, **KARAE**, **CORALDECK**, and **POORAIM**. Volexity's 2021 disclosure of "InkySquid" tied APT37 to strategic-website-compromise activity targeting a South Korean newspaper readership using BlueLight and RokRAT. The 2026 BirdCall / Sqgame disclosure is the latest in a continuous public reporting cadence and demonstrates that the group continues to invest in Android tooling and supply-chain initial-access vectors.

---

## Primary Targets

- **North Korean defectors and refugees** — primary historical and 2026 focus; tracking, coercion, and intelligence collection on refugee populations in South Korea, China (especially Yanbian Korean Autonomous Prefecture), and globally
- **South Korean civil society and policy researchers** — NGOs focused on DPRK human-rights, journalists covering DPRK affairs, academics studying DPRK politics and military programs
- **Defense think-tanks (regional and occasionally US)** — A&D-adjacent: research organizations studying DPRK military capabilities, RoK/US alliance policy, and Northeast Asia security
- **Industrial sectors (since 2017)** — South Korean industrial-sector targeting documented by FireEye 2018 and subsequent reporting; sectors include chemicals, electronics, manufacturing, and aerospace (per FireEye's 2018 profile language)
- **Government and military (regional)** — South Korean government entities and military targets per multi-vendor reporting
- **Diaspora-targeted civil-society** — extending the DPRK regime's reach into diaspora populations via consumer-grade software supply-chain (Sqgame 2026 case)

**Geographic Focus:** Republic of Korea (South Korea), China (especially Yanbian Korean Autonomous Prefecture), Japan, Vietnam, the Middle East (occasional, per Mandiant 2018), and globally where DPRK-defector populations reside. Some reporting has documented APT37 activity in Russia, India, Romania, Kuwait, and Nepal in connection with DPRK-related diplomatic interests.

**A&D-prime relevance:** APT37 is **unlikely to target a US A&D prime as primary objective** based on the public reporting record. Risk is **second-order via civil-society / NGO partner compromise** (intelligence-sharing partner orgs that engage with refugee or human-rights communities) and **mobile-device exposure** (executives and policy-staff personal devices accessing corporate resources). Direct A&D risk is structural and low-likelihood but worth tracking given the actor's mobile capability and the Archimedes corpus's prior DPRK coverage gap.

---

## Signature Campaigns

| Campaign | Year | Description |
|---|---|---|
| Operation Daybreak | 2016 | Kaspersky documents APT37 (then "ScarCruft") using Adobe Flash zero-day CVE-2016-4117 in spearphishing against South Korean targets |
| Evil New Year | 2017 | Cisco Talos (as "Group123") documents Korean-language spearphishing with HWP document-borne exploits delivering ROKRAT |
| FreeMilk | 2017 | Cisco Talos documents APT37 spearphishing of non-Korean diplomatic targets — earliest documented expansion outside Korean-peninsula focus |
| RokRAT continuity | 2017–ongoing | RokRAT Windows backdoor remains a signature APT37 implant across multiple campaigns and variants |
| FireEye / Mandiant disclosure | Feb 2018 | FireEye publishes "APT37 (REAPER): The Overlooked North Korean Actor" — most consequential public attribution and capability profile |
| CVE-2018-4878 exploitation | Jan–Feb 2018 | APT37 weaponizes Adobe Flash zero-day CVE-2018-4878 against South Korean targets; Adobe issues out-of-band patch |
| InkySquid / BLUELIGHT | 2021 | Volexity documents strategic-website-compromise of South Korean newspaper readership delivering BLUELIGHT and RokRAT |
| Konni-cluster overlap | 2021–2024 | Konni Android malware activity documented across multiple vendors with APT37-overlap attribution; cluster boundaries with Kimsuky remain debated in public reporting |
| Sqgame / BirdCall supply-chain | Nov 2024 – 2026 | ESET (via The Record, 2026-05-07): APT37 compromises Sqgame Android card-game platform; BirdCall Android + Windows backdoor delivered to ethnic Koreans in Yanbian Korean Autonomous Prefecture, China — civil-society / defector targeting |

---

## TTPs (MITRE ATT&CK)

### Initial Access

| ID | Technique |
|---|---|
| T1566.001 | Spearphishing Attachment (HWP / Hancom Office documents, Word, Excel — historically Korean-language) |
| T1566.002 | Spearphishing Link (credential-harvest pages, malicious download links) |
| T1189 | Drive-by Compromise (Adobe Flash zero-day CVE-2016-4117, CVE-2018-4878; strategic website compromise per Volexity InkySquid 2021) |
| T1195.002 | Supply Chain Compromise: Compromise Software Supply Chain (Sqgame Android APK supply-chain per ESET 2026) |
| T1195.001 | Supply Chain Compromise: Compromise Software Dependencies (historically observed in Korean software ecosystem) |
| T1199 | Trusted Relationship (use of compromised regional infrastructure as initial-access pivot) |

### Execution

| ID | Technique |
|---|---|
| T1059.001 | PowerShell |
| T1059.005 | Visual Basic (VBA macros in Office documents) |
| T1059.006 | Python (some intermediate stages) |
| T1204.002 | User Execution: Malicious File |
| T1203 | Exploitation for Client Execution (Flash and Office vulnerabilities) |

### Persistence

| ID | Technique |
|---|---|
| T1547.001 | Registry Run Keys / Startup Folder |
| T1053.005 | Scheduled Task |
| T1547.009 | Shortcut Modification |
| T1136.001 | Create Account: Local Account (occasional) |

### Defense Evasion

| ID | Technique |
|---|---|
| T1027 | Obfuscated Files (XOR, RC4, custom encoding across RokRAT and BLUELIGHT) |
| T1140 | Deobfuscate/Decode Files or Information |
| T1070.004 | File Deletion (post-collection cleanup) |
| T1036 | Masquerading |
| T1497 | Virtualization / Sandbox Evasion (RokRAT and BirdCall both ship anti-analysis routines per public reporting) |

### Credential Access

| ID | Technique |
|---|---|
| T1003 | OS Credential Dumping (multiple variants) |
| T1555 | Credentials from Password Stores (browsers, email clients) |
| T1056.001 | Input Capture: Keylogging |

### Discovery

| ID | Technique |
|---|---|
| T1057 | Process Discovery |
| T1082 | System Information Discovery |
| T1083 | File and Directory Discovery |
| T1518 | Software Discovery |
| T1124 | System Time Discovery |

### Collection

| ID | Technique |
|---|---|
| T1005 | Data from Local System |
| T1113 | Screen Capture |
| T1119 | Automated Collection |
| T1056.001 | Keylogging (overlap with Credential Access) |
| T1430 | Location Tracking (Android — BirdCall and prior mobile variants) |
| T1409 | Stored Application Data (Android — message and contact harvesting on mobile victims) |

### Command and Control

| ID | Technique |
|---|---|
| T1071.001 | Application Layer Protocol: Web (HTTP/HTTPS C2) |
| T1102.002 | Web Service: Bidirectional Communication (Cloud-platform abuse — pCloud, Yandex Disk, Dropbox, Google Drive across multiple campaigns) |
| T1573.001 | Encrypted Channel: Symmetric Cryptography |
| T1573.002 | Encrypted Channel: Asymmetric Cryptography |
| T1090 | Proxy (compromised infrastructure) |

### Exfiltration

| ID | Technique |
|---|---|
| T1041 | Exfiltration Over C2 Channel |
| T1567.002 | Exfiltration to Cloud Storage (heavy use of pCloud, Yandex Disk per RokRAT and BLUELIGHT reporting) |

### Mobile (per BirdCall and prior Android variants)

| ID | Technique |
|---|---|
| T1644 | Out of Band Data (mobile-tier C2 channels) |
| T1409 | Stored Application Data |
| T1417.001 | Input Capture: Keylogging (mobile) |
| T1430 | Location Tracking |
| T1474.003 | Supply Chain Compromise: Compromise Software Supply Chain (mobile — Sqgame APK supply-chain per ESET 2026) |

---

## Malware Arsenal

| Malware | Type | Notes |
|---|---|---|
| RokRAT | RAT (Windows) | Signature APT37 implant since 2017 (Cisco Talos); modular, cloud-platform C2 (pCloud, Yandex Disk, Dropbox), multiple variants and packers across 2017–2024 |
| BirdCall | Backdoor (Android + Windows) | ESET 2026; Android variant primary in Sqgame supply-chain campaign; Windows variant also documented per ESET via The Record |
| BLUELIGHT | Backdoor (Windows) | Volexity 2021 (InkySquid disclosure); cloud-platform C2; deployed via strategic website compromise |
| KARAE | Backdoor | FireEye 2018 disclosure; first-stage downloader |
| DOGCALL | Backdoor | FireEye 2018 disclosure; secondary backdoor |
| CORALDECK | Exfiltration tool | FireEye 2018 disclosure; archives victim files for upload |
| POORAIM | Backdoor | FireEye 2018 disclosure; AOL Instant Messenger-based C2 (historical) |
| RUHAPPY | Wiper / disruptive (suspected) | FireEye 2018 disclosure; possible MBR-overwrite capability — disruptive intent observed historically but not in primary current-generation operations |
| SLOWDRIFT | Downloader | FireEye 2018; cloud-platform C2 |
| HAPPYWORK | Downloader | FireEye 2018 |
| MILKDROP | Loader | FireEye 2018 |
| Konni (overlap) | RAT (Windows + Android) | Konni cluster has documented overlap with APT37 in some reporting; cluster boundaries with Kimsuky remain debated — counted here as overlap rather than APT37-exclusive |
| ROKRAT-mobile (historical) | Mobile RAT (Android) | Earlier Android tooling pre-dating BirdCall; Korean-language-targeted |

**Source-of-record arsenal note:** This arsenal compiles tools attributed to APT37 across FireEye/Mandiant 2018, Kaspersky 2018, Cisco Talos 2017–ongoing, Volexity 2021, ESET 2024–2026, and other public reporting. Where reporting attributes overlapping tooling to other DPRK clusters (e.g., Kimsuky, Lazarus sub-clusters), this is noted as overlap rather than APT37-exclusive capability. Hard Rule 2: no Archimedes-originated attribution; arsenal entries trace to cited sources.

---

## Infrastructure Patterns

- **Cloud-platform C2 abuse** — pCloud, Yandex Disk, Dropbox, Google Drive used as bidirectional C2 channels across multiple implants (RokRAT, BLUELIGHT). This blends C2 traffic into legitimate cloud-storage HTTPS traffic, complicating perimeter detection
- **Strategic website compromise** — Volexity 2021 documented APT37 compromising South Korean newspaper websites to deliver BLUELIGHT to readership; consistent with civil-society / journalist targeting profile
- **Software supply-chain compromise (mobile)** — ESET 2026 Sqgame case documents APK supply-chain compromise delivered via web-browser download (bypassing Google Play vetting); long dwell (Nov 2024 → 2026 minimum)
- **Korean-language lure infrastructure** — historical pattern of Korean-language spearphishing with HWP / Word / Excel documents weaponized for the South Korean and Korean-diaspora target populations
- **Compromised regional infrastructure** — use of compromised regional web servers and cloud accounts as C2 relays
- **Long dwell time on supply-chain access** — Sqgame compromise window opens at least November 2024 per ESET; 14+ month operator-side persistence before public disclosure
- **Tooling rotation post-disclosure** — visible across the 2018 Mandiant disclosure and 2021 Volexity disclosure cycles; like many state APTs, APT37 treats disclosure as a tooling-change trigger rather than an operational pause

---

## Known IOCs

This profile is a first-pass scaffold; current IOCs are limited and concentrated on the BirdCall / Sqgame campaign per finding-2026-05-07-0004 (ESET via The Record). See `iocs.md` and `iocs.yaml` for the current indicator set, organized by:

- Malware family records (BirdCall, RokRAT, BLUELIGHT, etc. as TTP-tier indicators)
- Compromised supply-chain platform (Sqgame — exact domain not surfaced in source text; passive DNS / VirusTotal enrichment recommended)
- Targeting / distribution patterns (web-browser APK sideload, Yanbian ethnic-Korean victim demographic)
- CVEs historically exploited (CVE-2018-4878 Flash zero-day; CVE-2016-4117 Flash zero-day)
- Cloud-platform C2 abuse patterns

**No first-party Splunk observations of APT37 infrastructure as of 2026-05-09.** Mobile-malware (BirdCall) is unlikely to surface in DefenseClaw enterprise Splunk telemetry given consumer-Android targeting.

---

## Geopolitical Context

APT37 operates in support of DPRK regime priorities, principally **defector and refugee tracking, civil-society coercion, and regional intelligence collection**. The MSS attribution per recent reporting (ESET via The Record 2026-05-07) places APT37 in a different bureaucratic lane than the RGB-attributed Lazarus and Stardust Chollima clusters tracked elsewhere in the Archimedes roster — RGB activity emphasizes financial revenue generation and military-strategic intelligence; MSS-aligned APT37 emphasizes regime-security and population-control objectives.

**Operational tempo** has been continuous since 2012 with no documented operational pause. Public-disclosure cycles (2018 FireEye/Mandiant, 2021 Volexity, 2026 ESET) prompt tooling rotation but not operational cessation. The group's investment in Android tooling (BirdCall, prior RokRAT mobile variants, Konni-cluster Android variants) reflects a deliberate adaptation to the consumer-device dominance among the actor's primary target populations (defectors, civil-society, journalists).

The **Yanbian Korean Autonomous Prefecture** targeting in the 2026 Sqgame campaign is geopolitically significant: Yanbian is a Chinese-administered region with the largest concentration of ethnic Koreans in the People's Republic of China and a long-running transit and resettlement zone for North Korean refugees. APT37 targeting of this population reflects DPRK regime interest in tracking, coercing, and gathering intelligence on defectors before they transit further to South Korea or third countries. **No A&D entity is named in the Yanbian campaign.**

**For a US A&D prime, APT37 risk maps to:**

- **Civil-society partner compromise** — A&D prime CTI teams that share threat intelligence with NGO partners (human-rights orgs, defector-resettlement charities, policy-research think-tanks) face a non-trivial second-order exposure if those partners are compromised by APT37 and share data laterally
- **Executive / policy-staff mobile device exposure** — APT37's Android capability is structural; executives traveling in East Asia or accessing personal devices that interface with corporate resources represent a low-likelihood but non-zero exposure
- **Defense-think-tank intelligence-sharing** — A&D primes that consume threat intelligence from defense-policy think-tanks (FDD, CSIS, Atlantic Council DPRK programs, RAND, etc.) may receive products derived from environments APT37 has historically targeted

The actor is not a primary US-soil threat to a US A&D prime, but the structural risk is worth tracking given the actor's mobile capability, supply-chain initial-access pattern, and the prior DPRK coverage gap in the Archimedes roster.

---

## Connection Web

- ⛓️ **[Actor #003 Lazarus Group](../Lazarus-Group/profile.md)** — DPRK counterpart attributed to the Reconnaissance General Bureau (RGB); operationally distinct from APT37 (MSS) per public reporting. Lazarus emphasizes financial revenue generation and broader military-strategic targeting; APT37 emphasizes civil-society coercion and defector tracking. **No documented operational tooling overlap.**
- ⛓️ **[Actor #002 Stardust Chollima](../Stardust-Chollima/profile.md)** — DPRK financial sub-cluster (CrowdStrike taxonomy; also tracked as BlueNoroff / APT38 / Sapphire Sleet). RGB-attributed and operationally distinct from APT37. No documented operational tooling overlap.
- ⛓️ **Kimsuky (Velvet Chollima / Black Banshee / Thallium)** — NOT currently in the Archimedes roster. Documented overlap with APT37 in some Konni-cluster reporting; cluster boundaries between Kimsuky and APT37 remain debated in public reporting. Treat as overlapping cluster with periodic tradecraft adjacency.
- ⛓️ **APT38 / BlueNoroff** — same alias-tree as Stardust Chollima above; RGB-financial; distinct from APT37.

---

## Defense Recommendations

1. **Mobile device security for executives traveling in East Asia** — Personal Android devices used by executives or policy staff to access corporate resources should be on managed-device policy with sideload restrictions enforced; review MDM posture for users with East Asia travel patterns. APT37's Android supply-chain delivery (Sqgame case) bypasses Google Play vetting via web-browser sideload — Play Protect alone is insufficient.
2. **Cloud-platform C2 hunt** — Audit outbound HTTPS to pCloud, Yandex Disk, Dropbox, and Google Drive from endpoints. APT37's RokRAT, BLUELIGHT, and adjacent implants use these as bidirectional C2 channels. Hunt for anomalous upload volume to cloud-storage APIs from non-developer endpoints; tune by allowlisting known-good user upload patterns.
3. **HWP (Hancom Office) document hygiene for Korea-touching business units** — Subsidiaries or business units transacting with South Korean partners should treat HWP attachments as elevated risk. APT37's historical lure infrastructure leans heavily on weaponized HWP. Block HWP execution outside an explicit allowlist of business processes that require it.
4. **Strategic-website compromise hunt** — Audit Korean-language news, NGO, and policy-research website visits from corporate endpoints to identify potential strategic-website-compromise exposure. APT37 (Volexity InkySquid 2021 case) has compromised reader-targeting websites to deliver implants.
5. **Civil-society partner threat-intel sharing protocols** — Establish notification protocols with NGO and policy-research partners. A partner-side detection of APT37 activity is often the earliest signal for downstream sharing-partner exposure.
6. **YARA deployment for current-generation APT37 tooling** — Pull current YARA rules from ESET (BirdCall), Volexity (BLUELIGHT), and Cisco Talos (RokRAT) publications; deploy to EDR. Cross-reference indicators with the actor's mobile capability — Android-capable EMM/MTD signal sources should ingest BirdCall indicators where feasible.
7. **Anti-sideload posture review** — Sideload-warning behavior is the only friction between an APT37-compromised APK and victim infection in the Sqgame case. Review enterprise Android posture for sideload allowance and Google Play Protect signal ingestion. Consumer-grade-equivalent posture is insufficient for executive devices.
8. **Defense-policy think-tank intelligence consumption hygiene** — When consuming threat intelligence products from DPRK-focused defense think-tanks (FDD, CSIS, RAND, Atlantic Council, etc.), apply same source-handling discipline as for any external feed; APT37 has historically targeted these environments.
9. **Korean-language spearphishing detection tuning** — Korea-touching personnel should have email security tuned for Korean-language spearphishing patterns; APT37 lure infrastructure has historically been Korean-language-primary even when targeting non-Korean victims.

---

## References

- [MITRE ATT&CK G0067 — APT37](https://attack.mitre.org/groups/G0067/)
- [FireEye / Mandiant: APT37 (REAPER) — The Overlooked North Korean Actor (Feb 2018)](https://www.mandiant.com/resources/reports/apt37-overlooked-north-korean-actor) — most consequential public attribution and capability profile
- [Cisco Talos: Korea In The Crosshairs (Group123, 2018)](https://blog.talosintelligence.com/korea-in-crosshairs/)
- [Cisco Talos: ROKRAT Reloaded (2017)](https://blog.talosintelligence.com/rokrat-reloaded/)
- [Kaspersky: Operation Daybreak — ScarCruft and the CVE-2016-4117 Flash zero-day (2016)](https://securelist.com/operation-daybreak/75100/)
- [Kaspersky Securelist: ScarCruft continues to evolve — Konni and other tooling (2018)](https://securelist.com/scarcruft-continues-to-evolve-introduces-bluetooth-harvester/90729/)
- [Volexity: InkySquid — The Missing Arsenal (2021)](https://www.volexity.com/blog/2021/08/17/north-korean-apt-inkysquid-infects-victims-using-browser-exploits/) — strategic website compromise + BLUELIGHT
- [ESET: APT37 / Sqgame supply-chain campaign — relayed via The Record (Jonathan Greig, 2026-05-07)](https://therecord.media/north-korean-hackers-target-ethnic-koreans-in-china) — BirdCall Android + Windows backdoor; ethnic-Korean targeting in Yanbian
- finding-2026-05-07-0004 — ingested ESET-via-The-Record finding feeding this dossier; ESET ratified A-grade in source-grades.yaml per commit `a49c576`
- Adobe Security Bulletin APSB18-03 — out-of-band patch for CVE-2018-4878 (Flash) following APT37 zero-day exploitation

---

*Profile authored 2026-05-09 by `actor-profiler` (Mode 1 — new-actor scaffold) from finding-2026-05-07-0004 (ESET via The Record). All attribution claims herein are inherited from cited sources per Hard Rule 2. Dossier_version 1; threat-box.yaml is TEMPLATE pending /update-tracking pass with /approve-scoring gate (HIGH likely).*
