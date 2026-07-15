---
id: "029"
primary_name: "Pioneer Kitten"
aliases: [Fox Kitten, UNC757, Parisite, RUBIDIUM, Lemon Sandstorm]
mitre_attack_id: G0117
mitre_attack_url: https://attack.mitre.org/groups/G0117/
type: "Nation-State APT (state-intelligence + access-broker / ransomware-enabler dual-track)"
attribution:
  nation: IR
  service: "IRGC-linked / Government of Iran (GOI)"
  unit: null
  front_company: "Danesh Novin Sahand (Iranian IT company, company ID 14007585836; assessed 'likely' a cover entity per AA24-241A)"
  attribution_note: >
    Confidence-language SPREAD preserved per Hard Rule 2: FBI/CISA/DC3 AA24-241A says
    "connected to the Government of Iran (GOI)" and "activity consistent with Iranian
    state-sponsorship" (does NOT say IRGC-directed). CrowdStrike/industry sharpen to
    IRGC-aligned. MITRE G0117 hedges to "suspected nexus to the Iranian government."
    Dragos (PARISITE) explicitly abstains from political/nation-state attribution and
    tracks by TTP only. Carry as IR / IRGC-linked — do NOT harden to "IRGC-directed"
    on the strength of any single source.
active_since: 2017
status: active
status_note: "Active dual-track: state-intelligence intrusions + commercial access-brokering (Br0k3r/xplfinder) enabling ransomware; 2-year Middle East CNI campaign ran into early 2025 (FortiGuard)."
motivation: [espionage, financial-gain, access-brokering, ransomware-enablement, prepositioning]
threat_level: MEDIUM
admiralty_grade: A2
tlp: CLEAR
dossier_version: 1
last_updated: 2026-07-14
last_reviewed: 2026-07-14
next_review_due: 2026-10-12
related_actors: ["004", "027", "011", "028", "022", "023"]
---

# Pioneer Kitten (Fox Kitten / UNC757 / Parisite / RUBIDIUM / Lemon Sandstorm)

## Overview

Pioneer Kitten is an Iran-linked (IRGC-aligned) state-nexus actor with a
**distinctive dual-track operating model** that separates it from every other
Iranian actor on the Archimedes roster: it runs high-volume state-intelligence
intrusions against US and allied targets **while simultaneously operating a
commercial access-brokering business** — selling network access to
cybercriminal marketplaces and collaborating directly with ransomware
affiliates (NoEscape, RansomHouse, ALPHV/BlackCat) for a share of ransom
proceeds. The FBI, CISA, and DoD Cyber Crime Center (DC3) documented this model
in joint advisory **AA24-241A** (2024-08-28), which is the load-bearing US-gov
attribution source for this dossier.

The **so-what for a US A&D prime:** Pioneer Kitten's core competency is
opportunistic mass-exploitation of internet-facing edge/VPN appliances (Citrix,
Fortinet, PAN-OS, Ivanti/Pulse, Check Point, F5) — exactly the perimeter
technology a large ITAR-regulated contractor and its Tier-1/2 supplier network
expose. Once inside, the same access can be tasked for state-intelligence
collection **or sold to a ransomware affiliate**, producing a compound threat
(espionage + extortion + availability loss) from a single intrusion. AA24-241A
explicitly names **"defense"** among the US victim sectors of this activity, and
Dragos names **"aerospace"** among PARISITE targets — but neither, in the
reporting reviewed for this build, names a specific US A&D prime or DIB
contractor. A&D relevance is therefore **structural/sector-level**, not
prime-directed.

A material recent escalation: FortiGuard's Incident Response Team documented a
**~2-year intrusion into a Middle East critical national infrastructure (CNI)
entity** (active May 2023 into early 2025, initial-access traces to 2021),
during which the actor deployed a **novel custom backdoor arsenal** (HanifNet,
HXLibrary, NeoExpressRAT) and — per FortiGuard's hedged assessment — **"may have
been positioning themselves to carry out a future destructive attack."** This is
a Volt-Typhoon-shaped prepositioning signal that pushes the actor beyond pure
espionage + access-brokering toward potential effects operations. It is
**suspected/assessed, not confirmed** — Dragos separately states PARISITE has no
observed ICS-specific destructive capability. The dossier records both and does
not harden the hedge (Hard Rule 2).

Threat-box scoring (2026-07-14) lands **weighted 5.5 → MEDIUM**, driven by an
espionage category HIGH (composite 8) and non-floor disruptive (5), cyber-crime
(5), and destructive (4) categories — the breadth of its dual-track model, not
any single ceiling score, is what elevates it. See
[threat-box.md](threat-box.md).

## Primary Targets

**Sectors (per cited sources, sector-level attribution):**
- **United States (AA24-241A):** education, finance, healthcare, and **defense**,
  plus local/municipal government entities.
- **Dragos (PARISITE) sector list:** Oil & Gas, **Aerospace**, Utilities
  (water/electric/gas), Government, NGOs.
- **MITRE G0117 sector list:** oil & gas, technology, government, **defense**,
  healthcare, manufacturing, engineering.

**Geography:** United States; Middle East (Israel, UAE, Azerbaijan named in
AA24-241A); North Africa, Europe, Australia, North America (MITRE/Dragos).

**A&D-scoring caveat:** "Defense" (AA24-241A, MITRE) and "Aerospace" (Dragos) are
**sector-level** attributions. No specific US A&D prime / DIB contractor is named
in the reporting reviewed for this build. This is the load-bearing fact that
holds espionage Intent at Ideology (4), not Target-Specific (5) — see
threat-box.md.

## Signature Campaigns

| Campaign | Year | Description |
|---|---|---|
| Pay2Key ransomware (Israel) | 2020 | Early actor-operated ransomware/hack-and-leak against Israeli firms — the actor's own direct extortion/disruption operation (per MITRE G0117). |
| Edge-device access operations | 2019–present | Long-running mass-exploitation of Citrix/Pulse/PAN-OS/Check Point/F5 appliances for initial access, feeding both state collection and the Br0k3r access-broker business (AA24-241A). |
| Br0k3r / xplfinder access-brokering | ~2020–2024 | Commercial sale of network access on underground marketplaces; direct collaboration with ransomware affiliates NoEscape, RansomHouse, ALPHV/BlackCat for a share of ransom proceeds (AA24-241A). |
| Lemon Sandstorm Middle East CNI intrusion | 2023–2025 | ~2-year intrusion into a Middle East CNI entity (initial-access traces to 2021), novel custom backdoors deployed, suspected destructive prepositioning (FortiGuard IR, May 2025). |

## TTPs

### Initial Access
| Technique | ID | Note |
|---|---|---|
| Exploit Public-Facing Application | [T1190](https://attack.mitre.org/techniques/T1190/) | Mass-exploitation of internet-facing edge/VPN appliances — the actor's signature access vector (see Known IOCs / CVE list). |
| External Remote Services | [T1133](https://attack.mitre.org/techniques/T1133/) | Abuse of VPN / remote-access appliances post-exploitation. |

### Execution & C2
| Technique | ID | Note |
|---|---|---|
| Web Shell | [T1505.003](https://attack.mitre.org/techniques/T1505/003/) | China Chopper and custom web shells on compromised edge devices. |
| Protocol Tunneling | [T1572](https://attack.mitre.org/techniques/T1572/) | ngrok, Ligolo, FRPC, Chisel, ReverseSocks5, Glider Proxy for tunneling. |
| Remote Access Software | [T1219](https://attack.mitre.org/techniques/T1219/) | AnyDesk, MeshCentral, TightVNC for hands-on access. |

### Persistence
| Technique | ID | Note |
|---|---|---|
| Scheduled Task/Job | [T1053.005](https://attack.mitre.org/techniques/T1053/005/) | Backdoors (HanifNet/HXLibrary/NeoExpressRAT) deployed via scheduled tasks disguised as legitimate system jobs (FortiGuard). |

### Impact / Effects
| Technique | ID | Note |
|---|---|---|
| Data Encrypted for Impact | [T1486](https://attack.mitre.org/techniques/T1486/) | Via ransomware-affiliate handoff (NoEscape/RansomHouse/ALPHV) and historical Pay2Key. |
| (Suspected) prepositioning for destructive effect | — | FortiGuard assesses the actor "may have been positioning" for a future destructive attack against CNI — **suspected/assessed, not confirmed**; Dragos observes no ICS-specific destructive capability. Recorded as a hedge, not a confirmed technique. |

## Malware Arsenal

| Malware / Tool | Type | Notes |
|---|---|---|
| HanifNet | Backdoor | Novel backdoor (command execution, file ops, system discovery) — Lemon Sandstorm CNI campaign (FortiGuard). |
| HXLibrary | Backdoor | Novel backdoor — same campaign (FortiGuard). |
| NeoExpressRAT | RAT | Novel RAT — same campaign (FortiGuard). |
| Havoc | C2 framework | Open-source / off-the-shelf C2 used in the CNI campaign. |
| Pay2Key | Ransomware | Actor-operated ransomware, 2020 Israel campaign (MITRE G0117). |
| China Chopper | Web shell | Post-exploitation web shell (MITRE G0117). |
| SystemBC | Proxy/backdoor | Associated tooling (MITRE G0117). |
| PsExec / ngrok / Ligolo / FRPC / Chisel / ReverseSocks5 / Glider Proxy / AnyDesk / MeshCentral / PuTTY-Plink / TightVNC | Living-off-the-land / commodity | Tunneling, remote access, lateral movement toolkit. |

**Note:** No atomic hashes for HanifNet/HXLibrary/NeoExpressRAT were retrieved for
this build (FortiGuard IOC appendix pending direct retrieval). Families recorded
as tooling, not as atomic IOCs.

## Infrastructure Patterns

- **Perimeter-first:** scans for and exploits internet-facing edge/VPN appliances
  at scale; initial foothold is almost always a vulnerable public-facing device.
- **Living-off-the-land tunneling:** heavy use of commodity tunnelers and remote-
  access utilities (ngrok, Ligolo, FRPC, Chisel, AnyDesk, MeshCentral) rather than
  bespoke C2 in the access-broker phase.
- **Custom backdoors for high-value persistence:** in the CNI campaign, novel
  backdoors were installed via scheduled tasks masquerading as legitimate system
  jobs — a materially more capable arsenal than the access-broker-era toolkit.
- **Access-broker monetization:** compromised access is packaged and sold via the
  **Br0k3r / xplfinder** persona on underground marketplaces (KeyBase / Twitter
  channels referenced per SOCRadar relay of AA24-241A).
- **Front company:** **Danesh Novin Sahand** assessed as a likely cover IT entity
  (AA24-241A).

## Known IOCs

Summary — full detail in [iocs.md](iocs.md) / [iocs.yaml](iocs.yaml):

- **10 exploited CVEs (by ID only, Hard Rule 3)** across Citrix, Pulse/Ivanti,
  PAN-OS, Check Point, F5, and Fortinet edge/VPN products — the actor's signature
  access surface. Several are `vuln-tracker` handoff candidates.
- **Access-broker persona handles:** `Br0k3r`, `xplfinder` (attribution/hunt
  context, not network IOCs).
- **Front-company attribution note:** Danesh Novin Sahand (distinct from ASA /
  Cotton Sandstorm — see Connection Web).
- **Network IOC appendix PENDING:** the AA24-241A network-indicator appendix
  (IPs/domains/hashes/email accounts) and the FortiGuard backdoor
  hashes/C2 are **held pending direct retrieval** — NOT fabricated. See iocs.md.
- **First-party Splunk:** 0 hits over -90d across `archimedes` + `defenseclaw_local`
  (both indices live). Visibility-bounded null — no corroboration, no bonus.

## Geopolitical Context

Pioneer Kitten operates within Iran's IRGC-aligned cyber ecosystem, where
state-intelligence tasking and financially-motivated freelancing coexist —
individuals and contractor entities conduct state-directed operations while
running parallel for-profit access-brokering and ransomware collaboration. The
US-Iran relationship is defined by an active sanctions regime and sustained
hostilities; there are **no diplomatic constraints** moderating Iranian cyber
operations against US and Western-aligned targets (willingness modifier 0 across
all categories). The 2020 Pay2Key campaign against Israeli firms and the
2023–2025 Middle East CNI intrusion both track the anti-Israel / anti-Western
axis of Iranian strategic targeting. The dual-track model — a state actor
monetizing intrusions via ransomware affiliates — is itself a geopolitical
signal: it lowers the cost of state operations and blurs the line between
espionage and cybercrime, a pattern US-gov reporting (AA24-241A) treats as a
deliberate feature, not an accident.

## Connection Web

Iranian-nexus peers tracked for analytic context — **NOT attribution merges**
(Hard Rule 2). Pioneer Kitten's identity cluster is Fox Kitten / UNC757 /
Parisite / RUBIDIUM / Lemon Sandstorm only (the vendors' mapping per MITRE
G0117), and the front company is Danesh Novin Sahand only.

- ⛓️ **[Actor #004 UNC1549](../UNC1549/profile.md)** — IRGC espionage peer; both
  target the defense sector via edge/cloud access, both scored espionage-dominant.
- ⛓️ **[Actor #027 Peach Sandstorm](../Peach-Sandstorm/profile.md)** — IRGC (APT33)
  peer; nearest calibration analog (both MEDIUM ~5.5) reached by different paths.
- ⛓️ **[Actor #011 Charming Kitten](../Charming-Kitten/profile.md)** — IRGC-IO
  peer; Iranian state-intelligence espionage.
- ⛓️ **[Actor #028 CyberAv3ngers](../CyberAv3ngers/profile.md)** — IRGC-CEC peer;
  edge/OT exploitation of US-exposed infrastructure.
- ⛓️ **[Actor #022 MuddyWater](../MuddyWater/profile.md)** — MOIS context peer.
- ⛓️ **[Actor #023 APT34](../APT34/profile.md)** — MOIS context peer.

**Explicit NON-merges (Hard Rule 2):**
- **Aria Sepehr Ayandehsazan (ASA)** — the mid-2024 rename of **Emennet Pasargad**,
  front for **Cotton Sandstorm** (aka Emennet Pasargad / Haywire Kitten), a
  SEPARATE IRGC-linked influence-operations actor. **ASA is NOT a Pioneer Kitten
  front** and is **NOT** folded into this dossier. Only **Danesh Novin Sahand** is
  the Pioneer Kitten front (AA24-241A).
- **Ransomware affiliates (NoEscape, RansomHouse, ALPHV/BlackCat)** are
  **collaborators/customers** of the Br0k3r persona per AA24-241A — recorded as
  affiliate relationships, NOT as Pioneer Kitten identities.

## Defense Recommendations

1. **Prioritize edge/VPN patch + exposure management** for the exact product set
   Pioneer Kitten exploits: Citrix ADC/Gateway (CVE-2019-19781, CVE-2023-3519),
   Pulse/Ivanti Connect Secure (CVE-2019-11510), PAN-OS GlobalProtect
   (CVE-2024-3400, CVE-2019-1579), Check Point Security Gateway (CVE-2024-24919),
   F5 BIG-IP (CVE-2020-5902, CVE-2022-1388), Fortinet FortiOS SSL VPN
   (CVE-2018-13379). Route all ten to `vuln-tracker`. Treat any unpatched
   internet-facing instance as a live Pioneer Kitten access candidate.
2. **Hunt for unauthorized remote-access / tunneling utilities** on and behind
   edge devices — AnyDesk, MeshCentral, TightVNC, ngrok, Ligolo, FRPC, Chisel,
   ReverseSocks5, Glider Proxy, PuTTY/Plink — especially any not sanctioned by IT.
   Alert on outbound ngrok/FRPC tunnels from DMZ segments.
3. **Baseline and alert on anomalous scheduled tasks** masquerading as legitimate
   system jobs (T1053.005) — the FortiGuard-documented persistence pattern for
   HanifNet/HXLibrary/NeoExpressRAT.
4. **Web-shell hunting on edge appliances** (China Chopper signatures, anomalous
   files in web-server directories on Citrix/PAN-OS/Ivanti devices).
5. **Assume compound-threat blast radius:** a single Pioneer Kitten foothold can
   be tasked for state collection OR sold to a ransomware affiliate. Model
   incident response for both espionage exfiltration AND downstream encryption
   (NoEscape/RansomHouse/ALPHV playbooks) from one intrusion.
6. **Extend edge-exposure scrutiny to the Tier-1/2 supplier network** — the same
   perimeter-first MO applies to suppliers, and brokered access to a supplier is a
   documented Pioneer Kitten monetization path.
7. **Deploy the pending IOCs on retrieval:** when the AA24-241A and FortiGuard
   IOC appendices are directly retrieved, load the IPs/domains/hashes into Splunk
   sentinel and re-run the -90d sweep (early-review trigger).

## References

- [FBI / CISA / DC3 Joint CSA AA24-241A — Iran-based Cyber Actors Enabling Ransomware Attacks on US Organizations (2024-08-28)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-241a) — load-bearing US-gov primary (page 403s on direct fetch; content reconstructed via clean relays this build; pending direct retrieval).
- [MITRE ATT&CK — Group G0117 (Fox Kitten)](https://attack.mitre.org/groups/G0117/) — curated alias-cluster + TTP reference.
- [Dragos — PARISITE threat page](https://www.dragos.com/threat/parisite/) — sector list (incl. Aerospace); deliberate non-attribution stance.
- [CrowdStrike — PIONEER KITTEN adversary profile](https://www.crowdstrike.com/en-us/adversaries/pioneer-kitten/) — IRGC-alignment framing (page pending direct retrieval; via WebSearch summary this build).
- [FortiGuard IR — Investigating Iranian Intrusion into Strategic Middle East CNI (Lemon Sandstorm, 2025-05)](https://www.fortinet.com/blog/threat-research/fortiguard-incident-response-team-detects-intrusion-into-middle-east-critical-national-infrastructure) — 2-year CNI campaign, novel backdoors, suspected destructive prepositioning (report PDF pending direct retrieval).

---

*Dossier v1 — first-pass /new-actor build 2026-07-14 (operator Ryan). Scoring: weighted 5.5 → MEDIUM (auto-commit; Hard Rule 5 gate did NOT fire). Load-bearing primary AA24-241A + FortiGuard report pending direct retrieval of their IOC appendices.*
