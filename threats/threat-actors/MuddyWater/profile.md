---
id: "022"
primary_name: "MuddyWater"
aliases:
  - Mango Sandstorm
  - Static Kitten
  - Mercury
  - MERCURY
  - Seedworm
  - Earth Vetala
  - TEMP.Zagros
  - Boggy Serpens
mitre_attack_id: G0069
mitre_attack_url: https://attack.mitre.org/groups/G0069/
type: "Nation-State APT"
attribution:
  nation: IR
  service: MOIS
  unit: null
  attribution_source: "Long-running US Government background attribution to MOIS, reproduced by Rapid7 2026-05-06 via citation chain. Hard Rule 2: Archimedes does not originate the MOIS attribution."
active_since: 2017
status: active
status_note: |
  Active 2026 per Rapid7 2026-05-06 (US construction / manufacturing /
  business services targeting; Game.exe RAT; Donald Gay code-signing
  cluster). Single-source veto applied — Rapid7 is sole originating
  source; SecurityWeek and BleepingComputer are pure relays. WEP capped
  at "likely" pending independent A/B-grade vendor corroboration.
motivation:
  - espionage
  - credential-harvest
  - data-theft
  - mois-tasking
  - dual-use-with-criminal-cover
threat_level: HIGH                 # Carried from _roster.yaml; threat-box.yaml is TEMPLATE
admiralty_grade: A2                # Per finding-2026-05-06-FLASH-0002 — Rapid7 (provisional A) + single-source veto applied
tlp: CLEAR
dossier_version: 1
last_updated: 2026-05-06
last_reviewed: 2026-05-06
next_review_due: 2026-08-04
profile_path: threats/threat-actors/MuddyWater/
iocs_path: threats/threat-actors/MuddyWater/iocs.md
threat_box_path: threats/threat-actors/MuddyWater/threat-box.yaml
related_actors:
  - "023"   # APT34 — fellow MOIS-aligned cluster; periodic operational adjacency per Mandiant / Unit 42
  - "011"   # Charming Kitten — Iranian APT, IRGC-IO not MOIS, distinct service tasking
  - "004"   # UNC1549 — Iranian APT, IRGC not MOIS, distinct mission profile (A&D recruiter-lure)
  - "014"   # Handala Hack — MOIS-adjacent hacktivist-with-IRGC-backing pattern; visual-surface overlap with Chaos false-flag tradecraft
notes_first_pass: |
  First-pass dossier authored 2026-05-06 from finding-2026-05-06-FLASH-0002
  (Rapid7 incident-response report, single-source veto applied, WEP "likely",
  red-team review qualify with required briefer caveats and 72h auto-downgrade
  clock). All attribution and TTP claims inherit from cited sources per Hard
  Rule 2; the MOIS service affiliation is reproduced from Rapid7's citation
  chain (which itself cites US Government background attribution). Threat-box
  scoring is TEMPLATE pending /update-tracking pass with /approve-scoring gate.
  Attribution Notes section preserves the contrarian-ACH cluster-imprecision
  caveat and the false-flag-via-Chaos-ransomware concern explicitly.
---

# MuddyWater — Threat Actor Profile

**Actor #022**

---

## Overview

MuddyWater is an Iranian advanced persistent threat cluster, attributed by long-running US Government background reporting to the Iranian Ministry of Intelligence and Security (MOIS), and reproduced as such by Microsoft (tracking the cluster as Mango Sandstorm), Mandiant, Unit 42, ClearSky, Trend Micro, and others. The cluster has been documented operating since at least 2017, with a long-standing focus on Middle East government, telecommunications, and oil-and-gas targets, evolving across the years into broader business-services and infrastructure-adjacent operations. MITRE tracks the cluster as G0069. Aliases include Mango Sandstorm (Microsoft), Static Kitten / Mercury, Seedworm (Symantec), Earth Vetala (Trend Micro), TEMP.Zagros, and Boggy Serpens.

For the Archimedes target profile (`ad-prime-v1` — mid-to-large US A&D contractor), MuddyWater's operational relevance is **second-order, mechanism-driven, and currently unresolved**. Rapid7's 2026-05-06 incident-response report (finding-2026-05-06-FLASH-0002) attributes a 2026 intrusion against US construction, manufacturing, and business-services victims to MuddyWater **at moderate confidence**, naming a custom 12-command RAT (Game.exe / Darkcomp, masquerading as Microsoft WebView2), Microsoft Teams interactive screen-share with "IT Support" persona, MFA device-add manipulation, a Donald Gay code-signing cluster (revoked shortly post-deployment), and — operationally striking — a Chaos ransomware false flag deployed **without actual file encryption**, plus a fake DLS onion address as extortion theater. No aerospace, defense, or A&D watchlist entity is named as a victim. The Microsoft Teams + MFA-device-add + Quick Assist tradecraft is platform-generic across M365 estates; defenders should not over-anchor on MuddyWater specifically.

The 2026-05-06 attribution is currently single-source. SecurityWeek and BleepingComputer are pure relays of Rapid7's reporting; neither contributes independent telemetry. Per `INTEL-GRADING.md`, the WEP ceiling is "likely." The red-team contrarian ACH on the source finding placed two alternative readings — H2 (a different MOIS-linked / MOIS-adjacent Iranian cluster sharing tooling and code-signing lineage) and H6 (mixed-composition engagement with both state-tradecraft and criminal Chaos-affiliate components present) — at zero inconsistencies alongside H1 (MuddyWater specifically) at one inconsistency. Two confidence constraints stack on this finding: Rapid7's own self-rated "moderate confidence" plus single-source veto. A 72-hour auto-downgrade clock is registered: if no second A/B-grade vendor (Mandiant, Unit 42, MSTIC, CrowdStrike, Recorded Future, Volexity) corroborates by 2026-05-09 ~12:00 EDT, no first-party Splunk hit lands on the 19 IOCs once ingested, and no CISA / FBI advisory picks up, the finding auto-downgrades to C3 "possibly true" per the precedent set in finding-2026-05-06-FLASH-0001.

This profile is therefore a **first-pass scaffold under attribution caveat**. All campaign-2026 specifics cite Rapid7 explicitly. None of the 2026 surfaces (Game.exe / Darkcomp, Donald Gay cert cluster, moonzonet[.]com / uploadfiler[.]com / adm-pulse[.]com infrastructure, Chaos false-flag tradecraft) are promoted as MuddyWater-canonical — they are explicitly carried as "Rapid7 attributes ... at moderate confidence" until independent corroboration arrives.

---

## Primary Targets

### Historical (pre-2026, per multiple A-grade sources)

- **Middle East government** — ministries (foreign affairs, defense, interior); long-running pattern across Iraq, Saudi Arabia, Jordan, UAE, Pakistan, Turkey, Israel
- **Telecommunications providers** — regional and Middle Eastern telcos
- **Oil and gas** — GCC oil ministries and energy companies
- **Defense industries (regional)** — Israeli defense and aerospace per Operation Olalampo and follow-on reporting
- **Universities and NGOs** — particularly those supporting Iran-policy research
- **IT service providers** — used as supply-chain pivots into customer environments

### 2026 (per Rapid7 2026-05-06, single-source, attribution-caveated)

- **US construction** — sector named by Rapid7
- **US manufacturing** — sector named by Rapid7; **NOT specified as defense manufacturing** by the source
- **US business services** — sector named by Rapid7

**Geographic Focus:** Historical — Middle East primary (Iraq, Saudi Arabia, Israel, Jordan, UAE, Pakistan, Turkey). 2026 — predominantly United States per Rapid7 (caveated).

**A&D-prime relevance:** **None named.** Rapid7 does not name any aerospace, defense, or A&D watchlist entity as a victim. Manufacturing is sector-adjacent to the defense industrial base but is not the same set; Rapid7 does not specify defense manufacturing. The brief / dossier consumer must not extrapolate construction / manufacturing / business services into A&D-direct targeting — that is the explicit must-fix language from the source finding's red-team review.

The operationally consequential A&D-relevance bridge is **tradecraft portability**, not actor-or-sector specificity. Microsoft Teams interactive screen-share with "IT Support" persona, MFA device-add manipulation via attacker-controlled device addition, and Quick Assist initiation from external accounts are platform-generic TTPs that have appeared in 2025–2026 reporting across multiple actors (Scattered Spider patterns, Storm-1811 patterns, generic IAB tradecraft). A&D defenders should evaluate M365 / Teams configuration and detection posture for those mechanisms regardless of which actor is currently using them.

---

## Signature Campaigns

| Campaign | Year | Description |
|---|---|---|
| Initial MuddyWater disclosures | 2017–2018 | Unit 42, MorphiSec, Trend Micro document early MuddyWater operations against Middle East government with PowerShell-based POWERSTATS backdoor and document-borne macros. |
| Iraq / Saudi / regional government targeting | 2018–2020 | Sustained Unit 42, ClearSky, Symantec reporting of MuddyWater operations against Iraqi government, Saudi entities, GCC ministries. |
| ZeroLogon / Exchange exploitation period | 2020–2022 | MuddyWater documented exploiting then-prevalent CVEs (ZeroLogon CVE-2020-1472, Exchange ProxyLogon / ProxyShell) per multiple vendor reports. |
| Operation Olalampo and successor branding | 2022–2024 | MuddyWater MENA-focused branded operations referenced in multiple vendor disclosures; Donald Gay / Amy Cherne code-signing cert lineage emerges in this period. |
| Microsoft Teams / "IT Support" persona patterns | 2024–2025 | Multiple vendors document MuddyWater pivot toward live social-engineering via Teams with "IT Support" personas, alongside continued legitimate-tool abuse (DWAgent, AnyDesk, Quick Assist). |
| Q2 2026 Chaos-false-flag US campaign (per Rapid7, moderate confidence — caveated) | 2026 | Rapid7 2026-05-06 attributes a US construction / manufacturing / business-services intrusion to MuddyWater at moderate confidence; Game.exe / Darkcomp custom 12-command RAT; Chaos ransomware false flag without actual encryption; fake DLS onion address as extortion theater; Donald Gay code-signing cert; pythonw.exe code injection into suspended processes; Microsoft Teams interactive screen-share with "IT Support" persona. **Single-source; auto-downgrade clock at 72h post-disclosure.** |

---

## TTPs (MITRE ATT&CK)

> **First-pass scaffold.** Historical TTPs reflect long-running MuddyWater reporting (Unit 42, ClearSky, Symantec, Trend Micro, MITRE G0069). 2026 additions (per Rapid7) are explicitly cited as Rapid7-source and carry the moderate-confidence + single-source caveat.

### Initial Access

| ID | Technique | Notes |
|---|---|---|
| T1566.001 | Spearphishing Attachment | Document-borne macros (POWERSTATS era and continuing) |
| T1566.002 | Spearphishing Link | Fake Microsoft / OneDrive landings |
| T1566.003 | Spearphishing via Service | Microsoft Teams "IT Support" persona engagement (2024–2026 per multiple sources) |
| T1190 | Exploit Public-Facing Application | Historical CVE exploitation (ZeroLogon, ProxyLogon / ProxyShell window) |
| T1199 | Trusted Relationship | Compromised IT service providers used to relay into customers |
| T1078 | Valid Accounts | Credential reuse across regional victims |

### Execution

| ID | Technique |
|---|---|
| T1059.001 | PowerShell (POWERSTATS / continuing through 2024+) |
| T1059.005 | Visual Basic (VBA macros) |
| T1059.006 | Python — pythonw.exe code injection (per Rapid7 2026 reporting; consistent with prior MuddyWater pattern) |
| T1106 | Native API |
| T1204.002 | User Execution: Malicious File |
| T1218 | System Binary Proxy Execution |

### Persistence

| ID | Technique |
|---|---|
| T1547.001 | Registry Run Keys / Startup Folder |
| T1053.005 | Scheduled Task |
| T1505.003 | Server Software Component: Web Shell (historical) |
| T1136 | Create Account |

### Defense Evasion

| ID | Technique |
|---|---|
| T1027 | Obfuscated Files |
| T1140 | Deobfuscate/Decode Files or Information |
| T1036.005 | Masquerading: Match Legitimate Name (Game.exe masquerades as Microsoft WebView2 per Rapid7 2026) |
| T1553.002 | **Code Signing — Donald Gay / Amy Cherne lineage on Microsoft ID Verified CS AOC CA 02 certs (per Rapid7 2026 + prior reporting). Time-invalid / revoked shortly post-deployment.** |
| T1055 | Process Injection — into suspended processes (pythonw.exe per Rapid7 2026; consistent with prior MuddyWater pattern) |
| T1562.001 | Disable / Modify Tools |

### Credential Access

| ID | Technique |
|---|---|
| T1056 | Input Capture (Microsoft Teams interactive screen-share for live credential harvest per Rapid7 2026) |
| T1003.001 | OS Credential Dumping: LSASS |
| T1110 | Brute Force / Password Spray (historical pattern) |
| T1556.006 | Modify Authentication Process: Multi-Factor Authentication (**MFA device-add manipulation via attacker-controlled device addition per Rapid7 2026**) |

### Discovery

| ID | Technique |
|---|---|
| T1087 | Account Discovery |
| T1018 | Remote System Discovery |
| T1057 | Process Discovery |

### Lateral Movement / Remote Access

| ID | Technique |
|---|---|
| T1219 | Remote Access Software — DWAgent, AnyDesk, Microsoft Quick Assist (per Rapid7 2026 + multiple historical sources) |

### Command and Control

| ID | Technique |
|---|---|
| T1071.001 | Application Layer Protocol: Web (HTTPS C2) |
| T1573 | Encrypted Channel |
| T1090 | Proxy (commodity infrastructure rotation) |

### Impact (false-flag tradecraft per Rapid7 2026, attribution-caveated)

| ID | Technique |
|---|---|
| T1486 | Data Encrypted for Impact — **deployed WITHOUT actual encryption per Rapid7 2026 (extortion theater)** |
| T1657 | Financial Theft — **fake leak-site (DLS) onion address used as extortion facade per Rapid7 2026; no actual victim leak** |

> The Chaos-ransomware-without-encryption + fake-DLS pattern is the most operationally striking 2026 delta. Rapid7 assesses these artifacts were deployed to obscure cyber-espionage intent. The red-team contrarian ACH explicitly notes that the **espionage-shaped reading is partially independent of the MuddyWater attribution**: items 1–4 of the false-flag observation (no encryption, DLS facade, custom RAT investment alongside ransomware, credential harvest + MFA manipulation + persistence) are observable from the engagement forensics regardless of which specific actor is involved.

---

## Malware Arsenal

| Malware | Type | Notes |
|---|---|---|
| POWERSTATS | PowerShell backdoor | Original MuddyWater backdoor — Unit 42 / Trend Micro 2017–2018 |
| Mori / SHARPSTATS / DELPHSTATS | Loaders / backdoors | Mid-generation MuddyWater tooling (multiple vendors) |
| PhonyC2 | C2 framework | Documented in MuddyWater leak-derived reporting |
| **Game.exe / Darkcomp** | **Custom 12-command RAT** | **Per Rapid7 2026; masquerades as Microsoft WebView2; SHA256 `1319d474d19eb386841732c728acf0c5fe64aa135101c6ceee1bd0369ecf97b6`. Carry attribution caveat — not yet promoted as MuddyWater-canonical pending second A/B-grade source.** |
| **ms_upd.exe** | **Loader** | **Per Rapid7 2026; SHA256 `24857fe82f454719cd18bcbe19b0cfa5387bee1022008b7f5f3a8be9f05e4d14`. Same caveat.** |
| **Stagecomp** | **Staging component** | **Per Rapid7 2026; specific hashes referenced in Rapid7 reporting. Same caveat.** |
| Chaos ransomware (false-flag deployment) | Commodity ransomware family used as cover | Per Rapid7 2026 — deployed without actual encryption as extortion theater. Chaos itself is a low-tier commodity ransomware family used by multiple criminal affiliates; the operational fact here is its FALSE-FLAG use, not the family itself. |
| Legitimate-tool abuse: DWAgent | Remote access tool | Multiple historical sources + Rapid7 2026 |
| Legitimate-tool abuse: AnyDesk | Remote access tool | Multiple historical sources + Rapid7 2026 |
| Legitimate-tool abuse: Microsoft Quick Assist | Remote access tool (legitimate) | Per Rapid7 2026 — phishing-initiated Quick Assist sessions paired with the "IT Support" Teams persona |

> **Source-of-record arsenal note:** The 2026-tooling rows (Game.exe / Darkcomp, ms_upd.exe, Stagecomp) are **explicitly NOT promoted as MuddyWater-canonical** until a second A/B-grade vendor (Mandiant, Unit 42, MSTIC, CrowdStrike, Recorded Future, Volexity) independently confirms. They are carried as "Rapid7 attributes ... at moderate confidence." This is the core Hard Rule 2 binding for the dossier per the source finding's red-team specific revisions.

---

## Infrastructure Patterns

> All 2026-specific infrastructure entries below carry the Rapid7 + moderate-confidence + single-source-veto caveat. Historical patterns are sourced from multiple A-grade vendors.

### Historical patterns (multiple A-grade sources, 2017–2025)

- **Compromised regional infrastructure as C2** — heavy historical reuse of compromised regional web servers in MENA (similar to APT34 pattern); reduces fresh-registration noise
- **Commodity hosting providers** — operational infrastructure includes commodity cloud and hosting providers; rotation is moderate
- **Microsoft Teams social-engineering tradecraft** — "IT Support" persona pattern documented across 2024–2025 reporting; 2026 escalation includes interactive screen-share for live credential harvest
- **Donald Gay / Amy Cherne code-signing cluster** — long-running code-signing identity reuse pattern; certs typically time-invalid or revoked shortly post-deployment

### 2026 (per Rapid7, attribution-caveated)

- `moonzonet[.]com` — ms_upd.exe loader C2
- `uploadfiler[.]com` — Game.exe / Darkcomp RAT C2 on port 443
- `adm-pulse[.]com` — Quick Assist phishing infrastructure
- IPv4 sources for Microsoft Teams interactive screen-share: `77.110.107.235`, `93.123.39.127`
- IPv4 hosting / contact: `172.86.126.208` (ms_upd.exe hosting), `116.203.208.186` (pythonw.exe outbound contact)
- Onion address (Chaos DLS facade): `hptqq2o2qjva7lcaaq67w36jihzivkaitkexorauw7b2yul2z6zozpqd[.]onion`

---

## Known IOCs

This profile is a first-pass scaffold built from the 19 IOCs published by Rapid7 on 2026-05-06 (finding-2026-05-06-FLASH-0002). See [`iocs.md`](./iocs.md) and [`iocs.yaml`](./iocs.yaml) for the structured indicator set, organized by:

- 9 SHA256 hashes (Game.exe / Darkcomp; ms_upd.exe; WebView2.exe legitimate binary repurposed; WebView2Loader.dll; visualwincomp.txt; dwagent.exe; dwagsvc.exe; dwaglnc.exe; AnyDesk.exe)
- 3 domains (moonzonet[.]com, uploadfiler[.]com, adm-pulse[.]com)
- 4 IPv4 (77.110.107.235; 93.123.39.127; 172.86.126.208; 116.203.208.186)
- 1 onion address (Chaos DLS facade)
- 1 code-signing certificate (Donald Gay / Microsoft ID Verified CS AOC CA 02; thumbprint `B674578D4BDB24CD58BF2DC884EAA658B7AA250C`)

**No first-party Splunk observations of these IOCs as of 2026-05-06** — collector queried `defenseclaw_local` and `archimedes` indices for the 4 IPv4 and 3 domain IOCs over -30d window with zero hits. The 9 SHA256 hashes were not directly queryable against current sourcetypes (no malware-detection telemetry in scope) and are skipped pending `_master-index.yaml` ingestion. Silent telemetry, not disconfirming.

The behavioral / mechanism-level indicators (Microsoft Teams interactive screen-share with "IT Support" persona; MFA device-add manipulation; OAuth-app-style Quick Assist initiation from external accounts) are **platform-generic**. They are documented in 2025–2026 reporting across multiple actors and should be hunted as mechanism-level surfaces, not as MuddyWater-diagnostic patterns.

---

## Geopolitical Context

MuddyWater operates as part of Iran's broader cyber-operations ecosystem alongside APT34 (also MOIS-aligned), Charming Kitten (IRGC-IO), and other clusters. Per US Government background reporting reproduced by multiple A-grade vendors, MuddyWater supports MOIS strategic intelligence collection requirements.

The cluster's historical operational signature is intelligence-collection-driven against Middle East government, telecommunications, and oil-and-gas entities. The 2026 Rapid7 disclosure — if borne out by independent corroboration — would mark a US-pivot in active campaigning and an operationally significant tradecraft delta in the form of the Chaos-ransomware-false-flag-without-encryption pattern. Rapid7 assesses the false flag is intended to obscure cyber-espionage intent, which would be consistent with broader 2025–2026 MOIS / IRGC-adjacent moves toward dual-use operations (espionage with criminal cover) — the structural parallel is to Handala Hack's hack-and-leak-as-MOIS-influence pattern, although Handala's mission profile is influence rather than espionage.

For a US A&D prime, MuddyWater 2026 risk maps to:

- **Mechanism-level M365 / Teams exposure** — the Microsoft Teams interactive screen-share + "IT Support" persona + MFA device-add tradecraft is platform-generic and is the operationally consequential A&D-relevance bridge. Defenders should evaluate Teams external-access policy, Quick Assist initiation policy, and MFA device-add monitoring **regardless of whether MuddyWater specifically targets the tenant**.
- **DIB tier-2/3 exposure via manufacturing-sector targeting (HYPOTHETICAL)** — Rapid7 names manufacturing as a victim sector but does NOT specify defense manufacturing. The brief / dossier consumer must not extrapolate this into A&D-direct targeting. Defenders should treat MuddyWater 2026 as an Iran/MOIS tasking-shift signal worth monitoring, not as evidence of A&D primary targeting.
- **Code-signing certificate hygiene** — the Donald Gay / Amy Cherne lineage continues to be the operational signing cluster pattern. Endpoint EDR rules for binaries signed by recently-issued, recently-revoked Microsoft ID Verified CS AOC CA 02 certs are appropriate.

MuddyWater is **NOT** the most A&D-direct Iranian APT — UNC1549 holds that position. MuddyWater is **NOT** the most mechanism-portability-relevant Iranian APT for OAuth tradecraft — Charming Kitten holds that position. MuddyWater 2026 is a **mechanism-portability / tasking-shift / attribution-caveated signal** that warrants tracking but does not yet warrant A&D-specific operational alarm.

---

## Connection Web

- ⛓️ **[Actor #023 APT34](../APT34/profile.md)** — Fellow MOIS-aligned cluster. Multiple Mandiant and Unit 42 reports document overlapping tooling and infrastructure between APT34 and MuddyWater in some campaign windows. Treat as separate clusters with periodic operational adjacency, not as a single actor.
- ⛓️ **[Actor #011 Charming Kitten](../Charming-Kitten/profile.md)** — IRGC-IO sister cluster (different service tasking — IRGC-IO not MOIS). Distinct mission profile. Iranian-ecosystem context warrants the link; no documented operational overlap.
- ⛓️ **[Actor #004 UNC1549](../UNC1549/profile.md)** — IRGC-aligned cluster (different service tasking — IRGC not MOIS). UNC1549 ACH evidence in finding-2026-05-05-0001 explicitly distinguishes UNC1549 tooling and tradecraft (MINIBIKE/MINIBUS recruiter-lure) from MuddyWater commodity-tooling pattern. Iranian-ecosystem neighbor, not operational sibling.
- ⛓️ **[Actor #014 Handala Hack](../Handala-Hack/profile.md)** — MOIS-adjacent hacktivist-with-IRGC-backing pattern. Visual-surface overlap with the 2026 Chaos-false-flag-without-encryption tradecraft (extortion theater + DLS facade resemble Handala's hack-and-leak presentation), but mission profile is structurally distinct (Handala is influence-driven; MuddyWater 2026 is espionage-with-cover per Rapid7). Surfaced in red-team contrarian ACH H3 as ranked-4 alternative reading.

---

## Attribution Notes

This section is **load-bearing** per the source finding's red-team specific revisions. It exists to preserve the attribution caveats and false-flag concerns explicitly so future briefs and dossier consumers do not inherit a stronger-than-supported impression.

### Attribution chain

Per Hard Rule 2, all attribution claims trace to cited public sources. The 2026-05-06 disclosure rests on a single originating source: **Rapid7's incident-response report**, which itself attributes the intrusion to MuddyWater at **moderate confidence** (verbatim source language: "moderate confidence in attributing the incident to MuddyWater" — 9 words, one quote per Hard Rule 6). Rapid7's MOIS service affiliation comes via a citation chain: Rapid7 → US Government background attribution. Archimedes does NOT originate or strengthen either attribution.

SecurityWeek and BleepingComputer relay Rapid7's report; neither contributes independent telemetry. Removing Rapid7 collapses both. Single-source veto applies.

### Two stacked confidence constraints

The "likely" WEP cap on the source finding is doing **double duty** for two separate confidence pressures, which a casual read might compress into one:

1. **Single-source veto** (Rapid7 alone is the originating source — `INTEL-GRADING.md` rule)
2. **Vendor-self-rated moderate confidence** (Rapid7's own ceiling on the attribution; vendor-IR convention treats "moderate" as one band below their own ceiling, signaling unresolved alternatives)

The brief and dossier consumer should not silently treat "likely" as comfortable. Both constraints argue for the same WEP cap; the cap absorbs both.

### Contrarian ACH summary (H2 + H6 zero inconsistencies; H1 one inconsistency)

The red-team contrarian ACH on finding-2026-05-06-FLASH-0002 placed two alternative readings at zero inconsistencies alongside H1 (MuddyWater specifically) at one inconsistency:

- **H2:** A different MOIS-linked / MOIS-adjacent Iranian cluster (or an MOIS-adjacent contractor) sharing tooling and code-signing lineage with MuddyWater. Espionage objective preserved; specific actor wrong.
- **H6:** Mixed-composition engagement where state-tradecraft components (custom RAT, "IT Support" Teams persona, Donald Gay code-signing) and criminal Chaos-affiliate components (the ransomware deployment itself) are concurrently present.

Per Hard Rule 2 binding, **H2 cannot be promoted as a specific alternative actor claim** because no cited source has attributed the activity to Charming Kitten, APT34, or a named MOIS contractor. H2 surfaces as **"Rapid7's attribution may be cluster-imprecise"** — NOT as "Archimedes attributes to a different actor." Same binding for H6 as a mixed-composition reading.

### Espionage-shaped reading is partially independent of the actor attribution

The observable evidence for the false-flag reading — (1) ransomware deployed without actual encryption, (2) DLS facade with no real victim leak, (3) custom RAT investment alongside the ransomware, (4) credential harvest + MFA manipulation + persistence artifacts inconsistent with smash-and-grab criminal extortion — is observable from the engagement forensics regardless of which specific actor is involved. The reading is "espionage activity wrapped in ransomware theater," **NOT** "MuddyWater activity wrapped in ransomware theater." These are two different sub-claims with different defensibility profiles.

### Chaos as false-flag explanation — operator concern preserved

The operator's note at dossier creation (2026-05-06): the Chaos-ransomware-without-encryption tradecraft has visual-surface overlap with multiple alternative explanations, including:

- **Implementation failure or EDR-blocked encryption** by a genuine commodity Chaos affiliate (H5 in contrarian ACH; placed at three inconsistencies — least likely but not eliminated).
- **Deliberate-leak-only campaign by criminal Chaos affiliate** — Chaos is a low-tier commodity ransomware family with multiple criminal affiliates in 2025–2026; failed encryption appears in commodity-affiliate intrusions for various reasons.
- **Hacktivist-shaped MOIS-backed cluster** (H3 in contrarian ACH; e.g., Handala Hack visual surface overlap).
- **Non-Iranian sophisticated actor mimicking MuddyWater tradecraft as misdirection** (H4 in contrarian ACH).

This dossier preserves these alternatives explicitly. Defenders should treat the espionage-shaped reading as the more defensible sub-claim and the actor-specific cluster identification as the moderate-confidence claim. The two are not the same.

### 72-hour auto-downgrade clock

A 72-hour auto-downgrade clock is registered on the source finding. If, by approximately 2026-05-09 12:00 EDT:

- No second A/B-grade vendor (Mandiant, Unit 42, MSTIC, CrowdStrike, Recorded Future, Volexity) corroborates the MuddyWater attribution, AND
- No first-party Splunk hit lands on any of the 19 IOCs once `_master-index.yaml` ingestion completes, AND
- No CISA / FBI advisory picks up MuddyWater + this campaign,

then finding-2026-05-06-FLASH-0002 auto-downgrades to C3 "possibly true" and a supersession-brief is produced per RETRACTION-POLICY. This dossier holds at first-pass status pending that resolution; campaign-2026 surfaces are NOT promoted as MuddyWater-canonical until a second A/B-grade source independently confirms.

### Confirming-evidence triggers (re-grade up to A1)

- Independent A/B-grade vendor publishes corroborating attribution → lifts single-source veto, WEP can move to "very likely"
- First-party Splunk hit on any of the 19 IOCs once ingested → first-party precedence kicks in on attribution-to-environment sub-claim
- CISA / FBI advisory naming MuddyWater + this campaign → independent A-grade corroboration
- Rapid7 publishes follow-on with high-confidence attribution upgrade

---

## Defense Recommendations

> All 2026-specific recommendations are framed at mechanism level so they apply regardless of whether MuddyWater is the actor currently using the tradecraft. Per the source finding's red-team specific revisions, the brief and dossier must NOT extrapolate construction / manufacturing / business services to A&D primes as direct targets.

1. **Microsoft Teams external-access posture audit** — Restrict external Teams access to known partner tenants only; block Teams meetings initiated by external accounts where business need is absent. The "IT Support" Teams persona pattern is the operationally consequential 2025–2026 A&D risk surface.
2. **Microsoft Quick Assist initiation policy** — Block / alert on Quick Assist initiation from external accounts. Adm-pulse[.]com infrastructure is the 2026 Rapid7 indicator, but the mechanism is platform-generic.
3. **MFA device-add monitoring** — Alert on unauthorized MFA device-add events in Entra ID audit logs, particularly when paired with recent password reset, recent credential exposure, or unusual sign-in geography. The MFA device-add manipulation tradecraft is mechanism-level and applies regardless of actor.
4. **Code-signing certificate hygiene endpoint hunt** — Endpoint EDR rules for binaries signed by recently-issued, recently-revoked Microsoft ID Verified CS AOC CA 02 certs (or any cert with a similarly short valid window between issuance and revocation). Donald Gay / Amy Cherne lineage is the persistent MuddyWater pattern.
5. **Hunt for the 19 published Rapid7 IOCs across -90d window** — Once `_master-index.yaml` ingestion completes, run retroactive sweep against `defenseclaw_local` and `archimedes` for the 9 SHA256, 3 domains, 4 IPv4, 1 onion, and 1 code-signing thumbprint. See `iocs.yaml` hunt queries.
6. **pythonw.exe code injection into suspended processes** — Endpoint EDR detection for pythonw.exe (or other Python interpreters) creating suspended child processes and writing to their memory. This is a long-running MuddyWater pattern continued in 2026 reporting.
7. **Game.exe / Microsoft WebView2 masquerade hunt** — Endpoint hunt for `Game.exe` (or other unusual executable names) loading WebView2 components from non-standard paths, with outbound HTTPS to non-Microsoft destinations. The masquerade-as-WebView2 pattern is the 2026 Rapid7 indicator.
8. **Chaos ransomware artifact triage discipline** — If a Chaos-branded ransom note appears in environment without corresponding actual file encryption, treat as **espionage-with-cover** until proven otherwise. The "no encryption" outcome is not by itself diagnostic of false-flag-for-espionage — it can also be implementation failure or EDR-blocked encryption — but the combination with other state-tradecraft surfaces (custom RAT, persistence, credential harvest) supports the espionage reading.

---

## References

- [Rapid7: MuddyWater operation — Iranian APT intrusion masquerading as Chaos ransomware (2026-05-06)](https://www.rapid7.com/blog/) — A (provisional, pending source-grades.yaml ratification per finding-2026-05-06-FLASH-0002 librarian handoff); originating source for 2026 campaign frame
- [SecurityWeek: Iranian APT Intrusion Masquerades as Chaos Ransomware Attack (2026-05-06)](https://www.securityweek.com/iranian-apt-intrusion-masquerades-as-chaos-ransomware-attack/) — B (relay; not independent of Rapid7)
- [BleepingComputer: MuddyWater hackers use Chaos ransomware as a decoy (2026-05-06)](https://www.bleepingcomputer.com/news/security/muddywater-hackers-use-chaos-ransomware-as-a-decoy-in-attacks/) — B (relay; not independent of Rapid7)
- [MITRE ATT&CK G0069 — MuddyWater](https://attack.mitre.org/groups/G0069/) — A1
- [Palo Alto Unit 42: MuddyWater research index](https://unit42.paloaltonetworks.com/) — A1 (search MuddyWater tag for sustained reporting)
- [ClearSky: MuddyWater research](https://www.clearskysec.com/) — A2 / A1 — long-running MuddyWater attribution and TTP reporting
- [Symantec: Seedworm research](https://symantec-enterprise-blogs.security.com/) — A1 (Seedworm taxonomy maps to MuddyWater)
- [Trend Micro: Earth Vetala research](https://www.trendmicro.com/) — A1 (Earth Vetala taxonomy maps to MuddyWater)
- [Microsoft: Mango Sandstorm](https://www.microsoft.com/en-us/security/blog/) — A1 (Microsoft taxonomy)
- finding-2026-05-06-FLASH-0002 — Archimedes graded finding (digraph A2, WEP "likely", red-team `qualify` with required briefer caveats and 72h auto-downgrade clock); source-of-truth for the 2026 campaign-specific surfaces with full red-team contrarian ACH

---

*First-pass profile authored 2026-05-06 by `actor-profiler` from finding-2026-05-06-FLASH-0002.
All attribution and TTP claims herein inherit from cited sources per Hard Rule 2 — Archimedes
does not originate attribution. The MOIS service affiliation reproduces Rapid7's citation chain
(which itself cites US Government background attribution). 2026 campaign-specific surfaces
(Game.exe / Darkcomp, Donald Gay cert, moonzonet[.]com / uploadfiler[.]com / adm-pulse[.]com,
Chaos false-flag tradecraft) are NOT promoted as MuddyWater-canonical pending second A/B-grade
source confirmation. Threat-box scoring is TEMPLATE pending /update-tracking pass with
/approve-scoring gate. Auto-downgrade clock at 72h post-disclosure (~2026-05-09 12:00 EDT)
held forward.*
