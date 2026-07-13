---
id: "027"
primary_name: "Peach Sandstorm"
aliases:
  - APT33            # FireEye / Mandiant
  - Refined Kitten   # CrowdStrike
  - HOLMIUM          # Microsoft (pre-Sandstorm element taxonomy)
  - Elfin            # Symantec
  - Curious Serpens  # Palo Alto Unit 42
  - MAGNALLIUM       # Dragos (ICS/OT threat-group taxonomy)
mitre_attack_id: G0064
mitre_attack_url: https://attack.mitre.org/groups/G0064/
type: "Nation-State APT"
attribution:
  nation: IR
  service: "IRGC (Peach Sandstorm assessed to work in support of the IRGC per Microsoft; FireEye/Mandiant assess APT33 works at the behest of the Iranian government)"
  unit: null          # No officially confirmed unit designation; FireEye noted possible ties to the Nasr Institute / a persona linked to Iranian government, not confirmed
active_since: 2013
status: active
status_note: "Highly active 2023-2024 against US/UAE defense, satellite, and energy sectors via password-spray + custom backdoors (Tickler, FalseFont)."
motivation:
  - espionage
  - strategic-collection
  - pre-positioning
threat_level: MEDIUM         # overall weighted 5.5 → MEDIUM; per-category espionage HIGH (composite 9). See threat-box.yaml.
admiralty_grade: A1
tlp: CLEAR
dossier_version: 2
last_updated: 2026-07-12
last_reviewed: 2026-07-12
next_review_due: 2026-10-10
profile_path: threats/threat-actors/Peach-Sandstorm/
iocs_path: threats/threat-actors/Peach-Sandstorm/iocs.md
threat_box_path: threats/threat-actors/Peach-Sandstorm/threat-box.yaml
related_actors:
  - "004"      # UNC1549 — parallel IRGC actor with direct A&D-prime targeting
  - "011"      # Charming Kitten — IRGC-IO peer, overlapping infrastructure per Microsoft
  - "023"      # APT34/OilRig — Iranian MOIS peer (different service; regional espionage overlap)
  - "022"      # MuddyWater — Iranian MOIS peer
notes_for_intake: |
  First-pass profile created 2026-07-12 via /new-actor Peach Sandstorm (operator
  Ryan). Roster ID #027 (next after Cavern Manticore #026). Seed reference:
  finding-2026-05-22-0002 (Unit 42 "Paved With Intent" — Curious Serpens = Peach
  Sandstorm = APT33 used ROADtools post-password-spray 2023). Dossier body built
  from established public A-grade reporting on APT33 (FireEye 2017, Microsoft
  2023-2024, Symantec 2019, CrowdStrike, Dragos, Kaspersky). All attribution
  inherits from cited sources per Hard Rule 2 — no Archimedes-originated
  attribution. Exploited/CVE material referenced by ID only per Hard Rule 3.
---

# Peach Sandstorm — Threat Actor Profile

**Actor #027**

---

## Overview

Peach Sandstorm (APT33) is the Iranian state-sponsored actor whose defining, publicly-documented characteristic is **sustained targeting of the aerospace, defense, and energy sectors** — making it the most directly A&D-relevant Iranian cluster Archimedes tracks. FireEye (now Mandiant) first named APT33 in 2017 in a report titled "Insights into Iranian Cyber Espionage: APT33 Targets Aerospace and Energy Sectors and has Ties to Destructive Malware," documenting intrusions at a US aerospace organization, a Saudi conglomerate with aviation holdings, and a South Korean petrochemical firm. Microsoft (which renamed HOLMIUM to Peach Sandstorm in its 2023 taxonomy) assesses the group works in support of Iran's Islamic Revolutionary Guard Corps (IRGC). CrowdStrike tracks the cluster as Refined Kitten, Symantec as Elfin, Palo Alto Unit 42 as Curious Serpens, and Dragos as MAGNALLIUM in the ICS/OT space.

For the Archimedes target profile (mid-to-large US A&D contractor), Peach Sandstorm's relevance is **direct and current**, not second-order. Multiple A-grade sources document targeting of exactly this profile: FireEye 2017 named a US aerospace victim; Microsoft's September 2023 password-spray campaign hit thousands of organizations globally with follow-on intrusions concentrated in the **defense, satellite, and pharmaceutical** sectors; Microsoft's December 2023 disclosure of the **FalseFont** backdoor documented targeting of the Defense Industrial Base (DIB); and the August 2024 Microsoft disclosure of the custom **Tickler** backdoor documented targeting of **defense, satellite, and oil-and-gas** organizations in the US and UAE. This is prime-direct, US-defense-sector targeting by A-grade sources — the basis for scoring espionage Intent at Target-Specific (5). *(Sourcing note: the Tickler campaign is Microsoft-originated — Microsoft Security Blog, 2024-08-28, A1. An earlier build draft co-credited Mandiant; the collector's 2026-07-12 direct-retrieval pass could not locate a standalone Mandiant Tickler advisory. Any Mandiant Tickler co-reporting is `pending_direct_retrieval` and is not asserted here per Hard Rule 2.)*

Peach Sandstorm is also the one Iranian actor in the roster with **documented ties to destructive malware**. FireEye linked the group to the SHAPESHIFT / DROPSHOT wiper (used in testing), and Kaspersky linked the StoneDrill wiper to APT33-adjacent activity (NewsBeef). While the group's mission is overwhelmingly espionage and strategic collection, the demonstrated wiper connection differentiates it from Iranian espionage-only peers (MuddyWater, APT34, Charming Kitten) and is reflected in a non-floor destructive category score.

Operationally, the group's current-generation tradecraft leans heavily on **large-scale password-spray** for initial access (a commodity, detectable technique), abuse of legitimate cloud infrastructure (Azure, ROADtools for Entra ID enumeration per Unit 42 2026), and deployment of now-signatured custom backdoors (Tickler, FalseFont, TURNEDUP, POWERTON). This mix — commodity access plus identified custom implants — places the group's novelty at semi-custom: capable and persistent, but with a defensible detection surface for a mature SOC.

---

## Primary Targets

- **Aerospace & Defense** — Military and commercial aviation, defense contractors, the US Defense Industrial Base; FireEye 2017 named a US aerospace victim; Microsoft 2023-2024 documented defense-sector targeting
- **Satellite / Space** — Microsoft documented satellite-sector targeting in the 2023 password-spray campaign and the 2024 Tickler campaign
- **Energy / Oil & Gas / Petrochemical** — Long-standing target set (Saudi, Gulf, South Korean petrochemical per FireEye 2017; oil-and-gas per Tickler 2024)
- **Pharmaceutical** — Named among follow-on-intrusion sectors in Microsoft's 2023 password-spray reporting
- **Government** — Regional and Western government entities

**Geographic Focus:** United States, Saudi Arabia and the GCC (esp. UAE), South Korea, and Western allies. Unlike Iranian MOIS espionage peers (APT34, MuddyWater) whose focus is predominantly regional, Peach Sandstorm has a **documented, recurring US-target pattern** in aerospace, defense, and satellite.

**A&D-prime relevance:** DIRECT. Multiple A-grade sources document targeting of US aerospace/defense/satellite organizations, including the Defense Industrial Base. This is the differentiator that lifts espionage Intent to Target-Specific (5) where the other tracked Iranian actors were bounded at Sector or Ideology association.

---

## Signature Campaigns

| Campaign | Year | Description |
|---|---|---|
| APT33 aerospace/energy espionage (FireEye disclosure) | 2017 | FireEye publicly names APT33; documents spear-phishing (aviation-themed job lures) against a US aerospace org, a Saudi aviation conglomerate, and a South Korean petrochemical firm; ties group to destructive malware |
| Elfin campaign (Symantec) | 2018–2019 | Symantec documents Elfin targeting 50+ organizations across Saudi Arabia and the US, including engineering, chemical, research, and aerospace-adjacent entities |
| Password-spray campaign against DIB (Microsoft) | 2023 | Microsoft documents a high-volume 2023 password-spray operation against thousands of orgs, with follow-on intrusions concentrated in the defense, satellite, and pharmaceutical sectors |
| FalseFont backdoor deployment | Dec 2023 | Microsoft discloses the custom FalseFont backdoor used against the Defense Industrial Base (first seen early Nov 2023). Corroborated independently by Unit 42 "Curious Serpens' FalseFont" (A1, 2024-03-25 — impersonates Maxar Technologies) and Nextron (A2, 2024-01-29). Ratified by collector direct-retrieval 2026-07-12 with hashes/C2 — see `iocs.md` |
| ROADtools / Entra ID post-password-spray (Unit 42) | 2023 (disclosed 2026) | Unit 42 "Paved With Intent" documents Curious Serpens (Peach Sandstorm) using the open-source ROADtools framework for Entra ID enumeration after password-spray access (seed finding-2026-05-22-0002) |
| Tickler backdoor campaign | 2024 | Microsoft discloses the custom Tickler backdoor and Azure-infrastructure abuse against defense, satellite, and oil-and-gas organizations in the US and UAE (Apr–Jul 2024 window; Microsoft Security Blog 2024-08-28, A1). Ratified by collector direct-retrieval 2026-07-12 with full IOC appendix — see `iocs.md` |

---

## TTPs (MITRE ATT&CK)

Exploited/CVE references are **by ID only** per Hard Rule 3 — no exploitation mechanism or PoC detail. Technique mapping compiles FireEye, Microsoft, Symantec, and Unit 42 reporting.

### Initial Access

| ID | Technique |
|---|---|
| T1110.003 | Brute Force: Password Spraying (primary current-generation access vector; high-volume 2023 campaign) |
| T1566.001 | Spearphishing Attachment (aviation-themed / job-lure documents, early campaigns) |
| T1566.002 | Spearphishing Link (fake job-recruitment and login pages) |
| T1078 | Valid Accounts (credentials obtained via password spray) |
| T1190 | Exploit Public-Facing Application (N-day exploitation for access; CVEs by ID only) |

### Execution

| ID | Technique |
|---|---|
| T1059.001 | PowerShell (POWERTON and PowerShell-based tooling) |
| T1059.003 | Windows Command Shell |
| T1204.002 | User Execution: Malicious File |
| T1106 | Native API (custom .NET/C++ backdoors — Tickler, FalseFont) |

### Persistence

| ID | Technique |
|---|---|
| T1098.005 | Account Manipulation: Device Registration (rogue device registration in Entra ID via ROADtools/roadtx) |
| T1547.001 | Registry Run Keys / Startup Folder |
| T1053.005 | Scheduled Task |
| T1136 | Create Account |

### Credential Access

| ID | Technique |
|---|---|
| T1110.003 | Password Spraying (also an access + credential-access technique) |
| T1550 | Use Alternate Authentication Material (stolen tokens / Primary Refresh Tokens via ROADtools) |
| T1003 | OS Credential Dumping |

### Discovery

| ID | Technique |
|---|---|
| T1087 | Account Discovery (Microsoft Graph API / Entra ID enumeration via roadrecon) |
| T1018 | Remote System Discovery |
| T1082 | System Information Discovery |

### Command and Control

| ID | Technique |
|---|---|
| T1071.001 | Application Layer Protocol: Web (HTTP/HTTPS C2) |
| T1102 | Web Service / abuse of legitimate cloud services (Azure infrastructure abuse — Tickler) |
| T1573 | Encrypted Channel |

### Impact (destructive — historical/associated)

| ID | Technique |
|---|---|
| T1485 | Data Destruction (SHAPESHIFT / DROPSHOT wiper association per FireEye; StoneDrill per Kaspersky) |
| T1561 | Disk Wipe (wiper tooling ties; regionally focused, not documented against US A&D primes) |

---

## Malware Arsenal

| Malware | Type | Notes |
|---|---|---|
| Tickler | Backdoor | Custom multi-stage backdoor; Microsoft Aug 2024; Azure (`*.azurewebsites.net`) C2 abuse + DLL sideloading; used against US/UAE defense, satellite, oil-and-gas. Hashes + 16 Azure C2 subdomains in `iocs.md` |
| FalseFont | Backdoor | Custom backdoor; Microsoft Dec 2023, Unit 42 Mar 2024; impersonates Maxar Technologies (`Maxar.dll`); targeted the Defense Industrial Base. Hashes + C2 in `iocs.md` |
| TURNEDUP | Backdoor | Custom backdoor documented by FireEye 2017; APT33 signature implant |
| POWERTON | PowerShell backdoor | Custom PowerShell backdoor documented in APT33 operations |
| DROPSHOT / SHAPESHIFT | Dropper / Wiper | FireEye 2017 tied APT33 to the DROPSHOT dropper and SHAPESHIFT wiper (used in testing) — the destructive-malware link |
| StoneDrill | Wiper | Kaspersky linked StoneDrill to APT33-adjacent (NewsBeef) activity; regionally focused (Saudi/Gulf) |
| NanoCore / commodity RATs | Commodity RAT | Early campaigns leveraged off-the-shelf RATs alongside custom tooling |
| ROADtools (roadrecon / roadtx) | Open-source offensive framework (abused) | Not APT33-authored; open-source Entra ID toolkit (Dirk-jan Mollema) abused post-password-spray per Unit 42 2026 (seed finding-2026-05-22-0002) |

**Arsenal note:** This arsenal compiles tooling attributed to APT33 / Peach Sandstorm across FireEye, Microsoft, Mandiant, Kaspersky, and Unit 42 reporting. The wiper entries (DROPSHOT/SHAPESHIFT, StoneDrill) reflect FireEye's "ties to destructive malware" framing and Kaspersky's StoneDrill linkage — attribution of the destructive *attacks* (Shamoon-adjacent) carries the softer confidence language of the cited sources and is preserved as such per Hard Rule 2.

---

## Infrastructure Patterns

- **Large-scale password-spray as the primary access engine** — high-volume authentication attempts against cloud identity surfaces (Entra ID / M365); a commodity technique that generates detectable authentication telemetry
- **Legitimate cloud-service abuse** — Azure infrastructure abused for C2 and staging (Tickler); ROADtools abuse of Microsoft Graph API / Entra ID as a living-off-trusted-services surface
- **Job-lure / recruitment-themed social engineering** — aviation and defense recruitment lures in earlier spear-phishing (consistent with the aerospace target focus)
- **Domain-masquerading** — registration of domains impersonating aviation and defense companies (FireEye 2017 documented domains mimicking Boeing/Alsalam, Northrop/Vinnell, and similar aviation entities)
- **Custom backdoors behind commodity access** — once inside, deployment of identified custom implants (Tickler, FalseFont, TURNEDUP)
- **Rotation cadence** — infrastructure rotates but the domain-masquerade and cloud-abuse patterns are recurring; treat network-tier IOCs as time-bounded and prioritize identity-plane + behavioral detection

---

## Known IOCs

See `iocs.md` and `iocs.yaml` for the structured set, organized by:

- Malware families (Tickler, FalseFont, TURNEDUP, POWERTON, DROPSHOT/SHAPESHIFT, StoneDrill)
- **Concrete atomic IOCs (ratified 2026-07-12):** FalseFont — 2 SHA256 (packed `Maxar.dll` + unpacked), C2 `digitalcodecrafters[.]com` → `64.52.80[.]30` TCP/8080, Defender detection `Backdoor:MSIL/FalseFont.A!dha`. Tickler — 9 SHA256 (2 samples incl. the Yahsat-lure `.pdf.exe`, 3 payloads, 4 sideloading-chain binaries) + 16 `*.azurewebsites.net` C2 subdomains + a LOW-fidelity `go-http-client` password-spray user agent
- Behavioral / TTP-level detection patterns (password-spray, ROADtools/Entra ID enumeration, Azure abuse, DLL/backdoor artifacts)
- Detection queries (hunt guidance) for the identity-plane and cloud C2 surfaces

**First-party Splunk sentinel (2026-07-12):** 0 hits over -90d across `defenseclaw_local` and `archimedes` on Peach Sandstorm / APT33 alias and tooling terms, **and 0 hits on the newly-ratified FalseFont/Tickler hashes, `digitalcodecrafters[.]com`, `64.52.80[.]30`, and the Azure C2 subdomains** (`defenseclaw_local` categorical zero confirmed). Per Hard Rule 8, silent Splunk does NOT disconfirm — Frank is a home/test environment, not a US A&D prime matching the victim profile; visibility-bounded null, no IOC corroboration bonus applied.

### Standing collection gaps (as of 2026-07-12)

- **Mandiant Tickler co-reporting — NOT FOUND.** The collector's direct-retrieval pass located no standalone A-grade Mandiant Tickler advisory. Mandiant has historically co-reported APT33 password-spray/Azure activity, but the Aug-2024 Tickler disclosure is Microsoft-originated. Flagged `pending_direct_retrieval`; not asserted as a source (Hard Rule 2).
- **2025–2026 A-grade primary reporting + fresh IOCs — GAP.** The pass surfaced only forecast/commercial-bulletin *secondary* material (an identity-centric M365 / Azure AD password-spray shift, and a mid-2025 OT-targeting uptick) with no retrievable A-grade *primary* reporting carrying new IOCs. The dossier's atomic-IOC set therefore currently ends at the 2024 campaigns. Standing collection request open for A-grade 2025–2026 primaries.

---

## Geopolitical Context

Peach Sandstorm operates within Iran's IRGC-aligned cyber ecosystem, alongside UNC1549 (#004, IRGC) and Charming Kitten (#011, IRGC-IO), and adjacent to the MOIS-aligned clusters APT34 (#023) and MuddyWater (#022). Microsoft assesses Peach Sandstorm works in support of the IRGC; FireEye assesses APT33 acts at the behest of the Iranian government. Both attributions are inherited from those A-grade sources per Hard Rule 2 — Archimedes originates no attribution.

The group's target selection tracks Iranian strategic priorities:

- **Aerospace and defense collection** aligns with Iran's interest in advancing domestic aviation, missile, and defense capabilities and informing military decision-making (FireEye's assessed motivation for the aviation targeting)
- **Satellite/space targeting** (Microsoft 2023-2024) reflects interest in space and ISR capabilities
- **Energy/petrochemical targeting** aligns with regional economic-competition and pre-positioning objectives
- **Destructive-malware ties** (SHAPESHIFT/DROPSHOT, StoneDrill) sit against the backdrop of Iran's Shamoon-era destructive operations against Gulf energy — a latent capability rather than a documented US-A&D-prime destructive campaign

For a US A&D prime, Peach Sandstorm is a **first-order espionage concern**: it is the Iranian actor with the clearest, most recent, multi-source record of targeting US defense, satellite, and aerospace organizations. The destructive dimension is real but regionally demonstrated (Gulf energy), and should be tracked as a latent escalation vector rather than an active US-A&D-prime threat.

---

## Connection Web

- ⛓️ **[Actor #004 UNC1549](../UNC1549/profile.md)** — Fellow IRGC-aligned actor with the closest A&D-prime playbook overlap; UNC1549 also directly targets aerospace and defense (Mandiant). Peach Sandstorm and UNC1549 are the two Iranian roster actors scoring espionage Intent=5 on direct A&D targeting. Distinct clusters per their respective sources — no attribution merge asserted.
- ⛓️ **[Actor #011 Charming Kitten](../Charming-Kitten/profile.md)** — IRGC-IO peer; Microsoft has documented overlapping infrastructure/tooling among IRGC-aligned clusters. Different operational tasking (Charming Kitten focuses on think tanks / journalists / researchers). Recorded as peer, not merge.
- ⛓️ **[Actor #023 APT34 (OilRig)](../APT34/profile.md)** — Iranian MOIS peer (different service). Regional espionage overlap; APT34's A&D relevance is supply-chain-mediated whereas Peach Sandstorm's is prime-direct.
- ⛓️ **[Actor #022 MuddyWater](../MuddyWater/profile.md)** — Iranian MOIS peer; regional-collection pattern. Peer, not merge.

*The `related_actors` frontmatter lists 004, 011, 023, 022 as Iranian-nexus peers for analytic context. These are peer relationships within Iran's cyber ecosystem, NOT Archimedes-originated attribution merges (Hard Rule 2).*

---

## Defense Recommendations

1. **Harden the identity plane against password spray** — Peach Sandstorm's primary current-generation access vector is high-volume password spray against Entra ID / M365. Enforce phishing-resistant MFA universally, disable legacy authentication, deploy smart lockout, and alert on distributed low-and-slow authentication-failure patterns across many accounts from few source ASNs. This is the single highest-value control against this actor.
2. **Hunt for rogue Entra ID device registrations** — Post-access, the group uses ROADtools (roadrecon/roadtx) for Entra ID enumeration and rogue device registration (T1098.005). Audit device-registration logs for anomalous registrations, default OS-version artifacts, and Microsoft Graph API enumeration from `roadtools` / `python-requests` user-agent strings (see seed finding-2026-05-22-0002 and `iocs.md`).
3. **Hunt for the custom backdoor set** — Deploy current YARA/EDR signatures for **Tickler** and **FalseFont** (Microsoft-published) across the Defense Industrial Base environment; both were used specifically against defense/satellite targets in 2023-2024.
4. **Monitor Azure infrastructure abuse** — Tickler abused legitimate Azure infrastructure for C2. Baseline expected Azure tenant/resource creation and alert on anomalous subscription/resource activity tied to service accounts.
5. **Scrutinize aviation/defense recruitment-lure phishing** — The group has a documented history of job-lure and recruitment-themed social engineering aligned to the aerospace/defense sector. Brief recruiting, HR, and engineering staff; deploy lookalike-domain detection for aviation/defense brand impersonation.
6. **Patch internet-facing assets against the exploited N-day set** — The group exploits public-facing applications for access (T1190). Prioritize timely patching of internet-facing systems (specific CVEs referenced by ID only in `iocs.md`; consult vendor advisories).
7. **Track the destructive-escalation tripwire** — Given the documented wiper ties (SHAPESHIFT/DROPSHOT, StoneDrill), treat any observation of destructive tooling staging as a high-severity escalation. Maintain offline, tested backups and segmentation for critical R&D and OT-adjacent systems.
8. **Standing early-review trigger** — Any first-party observation of Peach Sandstorm tooling, any new A-grade attribution naming a US A&D-prime victim, or any new custom-backdoor disclosure should trigger an early threat-box re-review (which could lift espionage Capability novelty and shift the assessment).

---

## References

- [MITRE ATT&CK G0064 — APT33](https://attack.mitre.org/groups/G0064/)
- [FireEye/Mandiant: Insights into Iranian Cyber Espionage — APT33 Targets Aerospace and Energy Sectors (2017)](https://www.mandiant.com/resources/blog/apt33-insights-into-iranian-cyber-espionage) — initial public attribution; A&D + energy targeting + destructive-malware ties
- [Microsoft: Peach Sandstorm password-spray campaigns enable intelligence collection at high-value targets (Sept 2023)](https://www.microsoft.com/en-us/security/blog/2023/09/14/peach-sandstorm-password-spray-campaigns-enable-intelligence-collection-at-high-value-targets/) — defense/satellite/pharma targeting
- [Microsoft: FalseFont backdoor used against the Defense Industrial Base (Dec 2023)](https://www.microsoft.com/en-us/security/blog/) — DIB targeting (MSTIC advisory; A1)
- [Palo Alto Unit 42: Curious Serpens' FalseFont Backdoor (Mar 2024)](https://unit42.paloaltonetworks.com/curious-serpens-falsefont-backdoor/) — full FalseFont technical analysis; Maxar impersonation; A1
- [Nextron Systems: Analysis of FalseFont Backdoor used by Peach Sandstorm (Jan 2024)](https://www.nextron-systems.com/2024/01/29/analysis-of-falsefont-backdoor-used-by-peach-sandstorm-threat-actor/) — independent analysis + YARA/Sigma; A2
- [Microsoft: Peach Sandstorm deploys new custom Tickler malware (Aug 2024)](https://www.microsoft.com/en-us/security/blog/2024/08/28/peach-sandstorm-deploys-new-custom-tickler-malware-in-long-running-intelligence-gathering-operations/) — US/UAE defense, satellite, oil-and-gas; Microsoft-originated (A1). No standalone Mandiant Tickler advisory located (2026-07-12); Mandiant co-reporting `pending_direct_retrieval`
- [Symantec: Elfin — Relentless Espionage Group Targets Multiple Organizations in Saudi Arabia and US (2019)](https://symantec-enterprise-blogs.security.com/threat-intelligence/elfin-apt33-espionage)
- [Kaspersky: From Shamoon to StoneDrill (2017)](https://securelist.com/from-shamoon-to-stonedrill/77725/) — StoneDrill wiper linkage to APT33-adjacent (NewsBeef)
- [Palo Alto Unit 42: Paved With Intent — ROADtools and Nation-State Tactics in the Cloud (2026)](https://unit42.paloaltonetworks.com/roadtools-cloud-attacks/) — Curious Serpens = Peach Sandstorm = APT33 (seed finding-2026-05-22-0002)
- CrowdStrike (Refined Kitten) and Dragos (MAGNALLIUM) — taxonomy cross-references for the same cluster
- Originating seed: `threats/findings/finding-2026-05-22-0002.md` (Unit 42 ROADtools; Curious Serpens /new-actor candidate flag)

---

*Profile authored 2026-07-12 via `/new-actor` (operator Ryan) by `actor-profiler`. **Fold-in 2026-07-12 (dossier v2):** collector direct-retrieval ratified the FalseFont and Tickler campaigns and their atomic IOCs; the Tickler campaign was corrected to cite Microsoft alone (Mandiant co-reporting `pending_direct_retrieval`). This was a sourcing correction — the threat-box score is unchanged (Intent=5 re-verified). All attribution claims inherit from cited public sources per Hard Rule 2 — no Archimedes-originated attribution. Exploited-CVE material referenced by ID only per Hard Rule 3. See `threat-box.md` for scoring detail.*
