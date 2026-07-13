---
id: "014"
primary_name: "Handala Hack"
aliases: [Void Manticore, Storm-0842, DEV-0842, Red Sandstorm, Banished Kitten]
mitre_attack_id: G1055
mitre_attack_url: https://attack.mitre.org/groups/G1055/
type: "Nation-State / Hacktivist (MOIS faketivist front)"
attribution:
  nation: IR
  service: MOIS
  unit: "MOIS Internal Security Deputy, Counter-Terrorism (CT) Division — per Check Point Research; reportedly under Seyed Yahya Hosseini Panjaki (CPR: reportedly killed in Israeli strikes, early March 2026)"
active_since: 2022
status: active
status_note: "Highly active 2024–2026. Anti-Israel hack-and-leak + destructive wiper ops (Handala persona); expanded to US enterprises in 2026 (Stryker Intune mass-wipe, ~2026-03-11)."
motivation: [destructive, hack-and-leak, influence-operations, espionage]
threat_level: MEDIUM                    # overall weighted 5.45 → MEDIUM; Destructive category = HIGH (composite 9). See threat-box.yaml.
admiralty_grade: A2
tlp: CLEAR
dossier_version: 1
last_updated: 2026-07-12
last_reviewed: 2026-07-12
next_review_due: 2026-10-10
related_actors: ["022", "023", "026"]   # Iranian-MOIS PEERS for analytic context — NOT attribution merges (Hard Rule 2). Scarred Manticore (Storm-0861) is a documented collaborator but is not rostered — see Connection Web.
profile_path: threats/threat-actors/Handala-Hack/
iocs_path: threats/threat-actors/Handala-Hack/iocs.md
threat_box_path: threats/threat-actors/Handala-Hack/threat-box.yaml
notes_for_intake: |
  First-pass profile + initial scoring created 2026-07-12 via /new-actor-style
  targeted dossier-seed build for the pre-existing roster #014 stub ("profile
  pending"). Built from two collector raw-signal files (raw-2026-07-12-handala-
  newactor-001, -002). SINGLE ORIGINATING PRIMARY: Check Point Research (CPR) is
  the sole A-grade originator of the Void Manticore = MOIS attribution ("Bad
  Karma, No Justice," 2024) and the Handala-persona-operated-by-Void-Manticore
  linkage ("Handala Hack — Unveiling Group's Modus Operandi," 2026). The Hacker
  News is a pure relay (not independent corroboration). MITRE ATT&CK G1055 is a
  structured second statement of the MOIS attribution, but its independence-vs-
  CPR-derivation is unadjudicated (recorded, not resolved). Microsoft's own
  Storm-0842/DEV-0842 primary is pending_direct_retrieval. All attribution and the
  cluster designation inherit from cited sources per Hard Rule 2 — no
  Archimedes-originated attribution. Void Manticore <-> Scarred Manticore
  (Storm-0861) is recorded as a CPR-stated target HAND-OFF / collaboration, NOT a
  merge. Wiper hash VALUES held pending_direct_retrieval (garbled on WebFetch
  retrieval; VT spot-checks returned found:false) — malware FAMILIES recorded as
  tooling, hash strings NOT folded. CVEs by ID only (Hard Rule 3); no credentials
  stored (Hard Rule 7). Threat-box weighted 5.45 → MEDIUM → auto-committed; Hard
  Rule 5 gate did NOT fire. The roster's prior placeholder threat_level HIGH was
  never a scored value — this computed MEDIUM governs. Splunk first-party 0 hits
  over -90d across all 9 IPs (visibility-bounded null, no bonus).
---

# Handala Hack — Threat Actor Profile

**Actor #014**

---

## Overview

Handala Hack is an online persona **operated by Void Manticore** — an Iranian threat actor that Check Point Research (CPR) attributes to the Ministry of Intelligence and Security (MOIS). Unlike the espionage-dominant Iranian actors elsewhere on the roster, Handala/Void Manticore is fundamentally a **destructive and hack-and-leak** operator: a MOIS-directed "faketivist" front (named for the Palestinian cartoon figure Handala) that pairs custom disk wipers with ideologically-framed leak operations. Its per-category **Destructive** score is HIGH (composite 9) — the operative number for a defender — even though the doctrine-weighted overall lands MEDIUM (5.45).

The reason to care is the actor's **demonstrated mass-destruction capability at enterprise scale**. On or around **2026-03-11**, Handala abused medical-technology maker **Stryker's own Microsoft Intune MDM platform** to issue legitimate remote-wipe commands to **200,000+ enrolled devices across 79 countries** — its first documented US-enterprise expansion. This is a living-off-the-land destructive technique that turns a victim's own management plane against it, needs no attacker-controlled infrastructure for the wipe itself, and is directly **portable to any large ITAR-regulated enterprise** with a comparable MDM footprint. The custom wiper arsenal (BiBi for Windows and Linux, Cl Wiper via the ElRawDisk driver, a partition-wiper family, and the MBR-based Handala Wiper) is layered onto manual, hands-on tradecraft: RDP lateral movement, Group Policy distribution of wipers, and off-the-shelf tunnelers (reGeorge, NetBird).

**This dossier rests on a single originating IR vendor.** CPR is the sole A-grade originator of both the MOIS attribution and the Handala-persona-operated-by-Void-Manticore linkage; The Hacker News relayed CPR without independent corroboration; MITRE ATT&CK G1055 provides a structured second statement of the MOIS attribution whose independence from CPR is unadjudicated; and Microsoft's own Storm-0842/DEV-0842 primary was not directly retrieved. The destructive *capability* facts (that these wipers exist and were used at scale) are more broadly corroborated — BiBi is widely documented, MITRE G1055 lists the destructive cluster tooling, and the Stryker incident drew Krebs on Security plus multiple relays — but the specific persona attribution should be read as CPR-originated pending independent second-vendor confirmation or direct retrieval of the Microsoft primary.

**A&D-prime relevance is INDIRECT and STRUCTURAL, not direct.** No aerospace/defense prime is named as a victim in any retrieved source. The concern maps to (a) the Intune/MDM mass-wipe TTP's portability to any large ITAR enterprise, (b) a hack-and-leak posture that would apply the same way to a defense supplier as to Stryker, and (c) Iran's standing anti-Western destructive intent. Per the evidence-minimum table, portability and extrapolation do **not** lift Intent to Target-Specific — no A-grade source documents A&D-prime-direct targeting, so Intent is held at Ideology Association across the scored categories.

---

## Primary Targets

- **Israel (primary)** — government and 40+ claimed victim organizations across sectors; the core anti-Israel destructive + hack-and-leak theatre post-October 2023 (Karma / Handala personas)
- **Albania** — destructive wiper + hack-and-leak campaigns under the "Homeland Justice" persona (2022–2024), the earlier well-documented Void Manticore theatre (anti-MEK/dissident framing)
- **US enterprises (emerging, 2026)** — Stryker Corporation (medical technology), the first documented US-enterprise expansion; the Stryker Intune wipe propagated to devices in 79 countries

**Geographic focus:** Israel (primary) and Albania historically; expanding to US and global reach in 2026 (the Stryker mass-wipe crossed 79 countries).

**Named victims:** Stryker Corporation (US, medical technology; ~2026-03-11 Intune mass-wipe). Israeli victims are claimed in volume (40+) but specific names are largely withheld in the public reporting.

**A&D-prime relevance:** INDIRECT / STRUCTURAL only. No A&D prime is named. Risk maps to (a) MDM/management-plane mass-wipe portability to large ITAR enterprises, (b) hack-and-leak posture applicable to defense suppliers, and (c) Iran-nexus destructive intent against Western industry — not to documented A&D-prime-direct targeting, which does not exist in any retrieved source.

---

## Signature Campaigns

| Campaign | Year | Description |
|---|---|---|
| Homeland Justice (Albania) | 2022–2024 | Destructive wiper + hack-and-leak against Albanian government targets; MITRE folds ROADSWEEP (encryptor-as-destruction) and ZeroCleare (disk wiper) into the G1055 cluster for this theatre |
| Karma / BiBi wiper (Israel) | 2023–2024 | Post-October-2023 anti-Israel destructive operations under the "Karma" persona; THN ties the BiBi wiper (Windows + Linux) specifically to this persona |
| Handala hack-and-leak (Israel) | 2024–2026 | The "Handala" leak persona (Telegram + leak site); intrusions and hack-and-leak against 40+ claimed Israeli organizations |
| Stryker Intune mass-wipe (US) | 2026 | ~2026-03-11 abuse of Stryker's own Microsoft Intune MDM to issue legitimate remote-wipe commands to 200,000+ devices across 79 countries; first documented US-enterprise expansion (CPR cross-references Krebs on Security; corroborated across Deepwatch / CSA Labs / Push Security / 7AI relays — treat as reported-consistent, common upstream possible) |

*Void Manticore <-> Scarred Manticore (Storm-0861) is a documented target hand-off / collaboration, not a discrete Handala campaign — see Connection Web.*

---

## TTPs (MITRE ATT&CK)

Technique mapping derives from CPR's described tradecraft (2024 + 2026) and MITRE G1055; it is originating-single-source and coarse-grained. CVEs (where relevant) are referenced **by ID only** per Hard Rule 3 — no mechanism, no PoC.

### Initial Access

| ID | Technique |
|---|---|
| T1078 | Valid Accounts — abuse of legitimate admin access to a compromised management plane (the Intune/MDM tenant vector at Stryker) |
| T1199 | Trusted Relationship — access obtained via the documented hand-off from collaborating actor Scarred Manticore (Storm-0861), who performs initial access + stealthy exfiltration |
| T1190 | Exploit Public-Facing Application — external-facing exploitation for access (as described in CPR reporting) |

### Execution

| ID | Technique |
|---|---|
| T1059.001 | Command and Scripting Interpreter: PowerShell — PowerShell-based wiper for file deletion (CPR notes AI-assisted code — CPR's characterization) |
| T1106 | Native API — custom wiper binaries (BiBi, Cl Wiper, Handala Wiper) |

### Persistence / Defense Evasion

| ID | Technique |
|---|---|
| T1505.003 | Server Software Component: Web Shell — Karma Shell, a custom persona-branded web shell |
| T1036 | Masquerading — abuse of legitimate/dual-use tools (VeraCrypt, NetBird) and legitimate MDM tooling to blend destructive actions into normal operations |

### Lateral Movement

| ID | Technique |
|---|---|
| T1021.001 | Remote Services: RDP — manual, hands-on RDP lateral movement |

### Command and Control

| ID | Technique |
|---|---|
| T1090 | Proxy / tunneling — reGeorge (off-the-shelf HTTP tunneler) and NetBird (off-the-shelf overlay network) for access and pivot |
| T1105 | Ingress Tool Transfer — delivery of wipers and tooling to compromised hosts |

### Impact (the actor's defining tactic)

| ID | Technique |
|---|---|
| T1561.001 | Disk Wipe: Disk Content Wipe — Cl Wiper (via the commercial ElRawDisk driver for raw disk writes); BiBi wiper |
| T1561.002 | Disk Wipe: Disk Structure Wipe — partition-wiper family (LowEraser/"No-Justice", Pinky, JustMBR) and the MBR-based Handala Wiper (partition-table / MBR destruction) |
| T1485 | Data Destruction — file-deletion PowerShell wiper; **abuse of legitimate MDM remote-wipe (Intune) to destroy data across enrolled devices at scale** (the Stryker vector — LOTL, uses the victim's own management plane) |
| T1486 | Data Encrypted for Impact — VeraCrypt repurposed for destructive lock-out; ROADSWEEP encryptor used destructively (per doctrine, wiper-disguised-as-ransomware = Destructive, not Cyber-Crime) |
| T1484.001 | Domain Policy Modification: Group Policy Modification — Group Policy used to distribute wipers fleet-wide |

*Technique precision is provisional pending direct retrieval of the CPR primaries and the Microsoft Storm-0842 report.*

---

## Malware Arsenal

| Malware | Type | Notes |
|---|---|---|
| BiBi Wiper | Wiper (Windows + Linux) | Custom. THN ties BiBi to the Karma persona operating against Israel post-October 2023 |
| Cl Wiper | Wiper | Custom. Uses the commercial **ElRawDisk** driver for raw disk writes |
| Partition Wipers | Wiper (partition/MBR) | Custom family — variants named LowEraser / "No-Justice", Pinky, JustMBR (partition-table / MBR destruction) |
| Handala Wiper | Wiper (MBR-based) | Custom, persona-branded MBR wiper |
| PowerShell wiper | Wiper (script) | CPR notes AI-assisted file-deletion code (recorded as CPR's characterization) |
| Karma Shell | Web shell | Custom, persona-branded |
| VeraCrypt | Legitimate FDE tool (dual-use) | Repurposed for destructive lock-out impact |
| NetBird | Legitimate overlay/tunneling (dual-use) | Off-the-shelf network overlay used for access |
| reGeorge | HTTP tunneler (off-the-shelf) | Publicly available; used for tunneling/pivot — NOT a wiper |

**MITRE G1055 cluster mapping (recorded as MITRE's mapping, not a CPR claim):** CHIMNEYSWEEP (S1149), ROADSWEEP (S1150, ransomware/encryptor), ZeroCleare (S1151, disk wiper), RawDisk (S0364). ROADSWEEP + ZeroCleare are historically the Homeland Justice / Albania toolset.

**Hash discipline:** CPR's reports list SHA-256 (2024) and MD5 (2026) wiper hashes, but the values surfaced via WebFetch summarization were **garbled** (VT spot-checks returned `found:false`). Hash **values are held pending_direct_retrieval** of the CPR IOC appendix — malware **families** are recorded above; hash strings are **not** folded into `iocs.yaml`. See `iocs.md` §4.

---

## Infrastructure Patterns

- **Abuse of the victim's own management plane** — the marquee pattern: legitimate MDM (Microsoft Intune) remote-wipe issued from a compromised tenant, propagating destruction to enrolled devices with no attacker-controlled infrastructure required for the wipe (Stryker: 200k+ devices, 79 countries)
- **Operator IPs on commercial/bulletproof hosting** — Vultr / The Constant Company (AS20473; a `64.176.160.0/19` cluster, 2024 set), Zenlayer (`82.25.35.0/24`, 2026), and frequently-abused hosting ranges (e.g., `107.189.0.0/16`)
- **Commercial-VPN / Starlink egress for operator obfuscation** — shared-egress ranges surfaced (low standalone value; context only)
- **Manual, hands-on operations** — RDP lateral movement, Group Policy distribution of wipers, manual deletion; consistent with CPR's characterization of Void Manticore as a manual operator
- **Off-the-shelf tunnelers layered with custom impact tooling** — reGeorge and NetBird for access/pivot, custom wipers and Karma Shell for effect
- **Persona-branded leak infrastructure** — the Handala leak persona operates a Telegram channel and leak site for hack-and-leak publication

---

## Known IOCs

First-pass IOC set from the two seed raw-signal files. See `iocs.md` and `iocs.yaml` for the structured set (9 IP indicators):

- **2 higher-confidence, VirusTotal-confirmed operator IPs:** `64.176.169.22` (VT 10 engines malicious; Vultr AS20473; 2024 set) and `82.25.35.25` (VT 9 engines malicious; Zenlayer AS21859; last-seen 2026-07-09; 2026 set)
- **7 lower-confidence, reported-but-not-individually-VT-checked IPs:** `64.176.172.235`, `64.176.172.165`, `64.176.173.77`, `64.176.172.101` (2024 Vultr /19 cluster); `31.57.35.223`, `107.189.19.52`, `146.185.219.235` (2026 set)
- **Wiper hashes:** held `pending_direct_retrieval` (garbled on retrieval — see Malware Arsenal and `iocs.md` §4). Not folded.

**First-party Splunk sentinel (2026-07-12):** 0 hits over -90d across `defenseclaw_local` and `archimedes` on all 9 IPs. Per Hard Rule 8, silent Splunk does NOT disconfirm — Frank is not an Israeli/Albanian/US-medical-tech victim matching the target profile; visibility-bounded null, not negative evidence. No IOC corroboration bonus applied.

---

## Geopolitical Context

CPR situates Void Manticore within Iran's MOIS-aligned cyber ecosystem — specifically tying the operator to the MOIS Internal Security Deputy's Counter-Terrorism (CT) Division, reportedly under Seyed Yahya Hosseini Panjaki (whom CPR states was reportedly killed in Israeli strikes in early March 2026). Recorded as CPR's assessment.

The actor's defining posture is **destructive influence operations under a hacktivist veneer**. The Handala persona (anti-Israel, named for the Palestinian cartoon figure) and the earlier Homeland Justice persona (anti-MEK, against Albania for hosting Iranian dissidents) are MOIS-directed "faketivist" fronts: the ideological framing is cover for state destructive tasking. Activity intensified after October 2023 as part of Iran's broader cyber pressure on Israel and its partners.

The **2026 expansion to US enterprises** (Stryker) is the strategically significant shift. It demonstrates both willingness to strike US-based targets and a mass-propagation technique (management-plane abuse) whose blast radius (200k+ devices, 79 countries) is disproportionate to the effort. For a US A&D prime, this maps to a second-order but real exposure: any ITAR-regulated enterprise operating a large MDM/management footprint, or tied to Israel/Western-defense interests, sits within the ideological and technical envelope this actor has now shown it will use — even though no A&D prime has been named a victim.

Because the persona attribution rests on a single, not-directly-retrieved originating vendor (CPR), the geopolitical framing here is CPR's and should firm up (or be revised) on independent second-vendor confirmation or retrieval of Microsoft's Storm-0842 primary.

---

## Connection Web

- ⛓️ **Scarred Manticore (Microsoft: Storm-0861)** — **CPR-documented target HAND-OFF / collaboration, NOT a merge (not rostered).** CPR reports "clear overlaps between the targets of Void Manticore and Scarred Manticore, with indications of systematic hand off of targets" — Scarred Manticore performs initial access + stealthy exfiltration, then hands the access to Void Manticore for the destructive phase ("a different set of IPs began accessing the network, suggesting the involvement of another actor"). CPR frames the two as **separate but collaborating** actors and does NOT merge them; Archimedes records the collaboration exactly as CPR stated it and originates no equivalence (Hard Rule 2).
- ⛓️ **[Actor #023 APT34 (OilRig)](../APT34/profile.md)** — Iranian MOIS peer (analytic context only; NO attribution merge asserted — Hard Rule 2). Shares the MOIS milieu.
- ⛓️ **[Actor #022 MuddyWater](../MuddyWater/profile.md)** — Iranian MOIS peer (analytic context only; NO attribution merge — Hard Rule 2).
- ⛓️ **[Actor #026 Cavern Manticore](../Cavern-Manticore/profile.md)** — Iranian MOIS peer, also CPR-documented (analytic context only; NO attribution merge — Hard Rule 2).

*The `related_actors` frontmatter lists "022", "023", "026" as Iranian-MOIS analytic PEERS — not attribution merges. Scarred Manticore, the most operationally significant connection, is a documented collaborator but is not a rostered actor, so it appears here in prose rather than in `related_actors`.*

---

## Defense Recommendations

1. **Harden the MDM / Intune control plane — the marquee TTP.** Enforce phishing-resistant MFA and Conditional Access on all Intune/MDM administrator accounts; require multi-admin approval (dual authorization) for bulk device actions; alert on high-volume `Wipe` / `Retire` / `Fresh Start` commands in Intune audit logs; scope admin roles to least privilege. The Stryker attack propagated through a legitimate management plane — treat mass-wipe as an insider-grade control problem.
2. **Build wiper resilience, not just exfil prevention.** Maintain offline / immutable, segmented backups with tested restore; the primary threat here is integrity/availability destruction, not quiet data theft. Assume a mass-wipe scenario and rehearse recovery.
3. **Block and hunt the operator IPs.** Prioritize the two VT-confirmed IPs (`64.176.169.22`, `82.25.35.25`); hunt the full 9-IP set (see `iocs.md`) in DNS/proxy/firewall/netflow. Network-infrastructure TTL is 90 days — re-validate before long-term reliance.
4. **Detect web shells and off-the-shelf tunnelers.** Hunt for Karma Shell artifacts on internet-facing servers and for anomalous outbound tunneling/overlay traffic consistent with reGeorge and NetBird (T1090); baseline expected remote-access tooling and alert on NetBird where it is not sanctioned.
5. **Monitor Group Policy integrity.** Alert on GPO changes that distribute executables or scripts fleet-wide (T1484.001) — the actor uses GPO to push wipers.
6. **Monitor internal RDP lateral movement.** The actor is manual and hands-on; watch for anomalous internal RDP chains and privileged-account RDP from unusual hosts (T1021.001).
7. **Scrutinize dual-use tooling.** Treat unexpected VeraCrypt deployment (full-disk encryption used as destructive lock-out) and unsanctioned NetBird installs as high-severity — both are legitimate tools the actor repurposes.
8. **Standing corroboration tripwire.** The Handala-persona attribution is CPR-single-origin. Treat any independent second-IR-vendor confirmation (Mandiant / CrowdStrike / Unit 42 / MSTIC) or direct retrieval of Microsoft's Storm-0842/DEV-0842 primary as a trigger to re-review and re-score. Direct retrieval of the CPR IOC appendix (to recover verified wiper hashes) is a standing collection task.

---

## References

- [Check Point Research — "Bad Karma, No Justice: Void Manticore Destructive Activities in Israel" (2024-05)](https://research.checkpoint.com/2024/bad-karma-no-justice-void-manticore-destructive-activities-in-israel/) — originating primary for the MOIS attribution, wiper toolset, and Scarred Manticore hand-off. Retrieved via WebFetch summarization; IOC appendix not cleanly retrieved.
- Check Point Research — "'Handala Hack' — Unveiling Group's Modus Operandi" (2026) — originating primary for the Handala-persona-operated-by-Void-Manticore linkage, 2024–2026 operations, and the Stryker/Intune vector. `https://research.checkpoint.com/2026/handala-hack-unveiling-groups-modus-operandi/` — **primary not directly retrieved; exact publication date pending**.
- [MITRE ATT&CK — Group G1055 (Void Manticore)](https://attack.mitre.org/groups/G1055/) — structured second statement of the MOIS attribution and the destructive cluster tooling; independence-vs-CPR-derivation unadjudicated.
- [The Hacker News (2024-05-20, Ravie Lakshmanan) — Iranian MOIS-linked hackers behind destructive attacks](https://thehackernews.com/2024/05/iranian-mois-linked-hackers-behind.html) — RELAY of CPR; not independent corroboration.
- Krebs on Security — Stryker incident (cross-referenced by CPR 2026; not directly retrieved).
- Microsoft — Storm-0842 (formerly DEV-0842) tracking designation — **primary pending_direct_retrieval**.
- Originating raw-signal: `raw-2026-07-12-handala-newactor-001` (attribution foundation) and `raw-2026-07-12-handala-newactor-002` (persona / MO / 2026 IOCs). No promoted finding at build time — dossier built directly from the collector seed pass.

---

*Profile authored 2026-07-12 (first-pass build for pre-existing roster #014 stub) by `actor-profiler`. Single originating primary (Check Point Research); CPR primaries retrieved via WebFetch summarization, IOC appendices and Microsoft Storm-0842 primary not directly retrieved. All attribution and the cluster designation inherit from cited sources per Hard Rule 2 — no Archimedes-originated attribution; Void<->Scarred Manticore recorded as a hand-off/collaboration, not a merge. See `threat-box.md` for scoring detail.*
