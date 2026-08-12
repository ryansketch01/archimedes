---
id: "018"
primary_name: "Cl0p"
aliases:
  - CL0P
  - Clop
  - TA505              # Proofpoint (parent financial-crime cluster)
  - FIN11             # Mandiant / Google Threat Intelligence Group
  - GRACEFUL SPIDER   # CrowdStrike
  - GOLD TAHOE        # Secureworks (Cl0p); GOLD EVERGREEN tracks the wider TA505 parent
  - Lace Tempest      # Microsoft (current taxonomy)
  - DEV-0950          # Microsoft (former)
  - Spandex Tempest   # Microsoft (Cl0p ransomware element)
  - UNC4857           # Mandiant (MOVEit exploitation cluster; merged into FIN11)
mitre_attack_id: null            # No dedicated "Cl0p group" G-number. Clop malware = Software S0611; closest associated group = TA505 (G0092). See TTPs note.
mitre_attack_url: https://attack.mitre.org/software/S0611/
type: "Cybercriminal (RaaS / data-theft extortion)"
attribution:
  nation: RU                     # Russian-speaking / CIS-based per multiple A-grade vendors; NOT a state actor
  service: null                  # criminal, not state-directed
  unit: null
  note: >
    Attribution is to a Russian-speaking, financially-motivated criminal cluster, NOT a
    government service. CRITICAL Hard Rule 2 nuance: "Cl0p" is as much an extortion BRAND
    (leak site + encryptor) as a single crew. Google Threat Intelligence Group assesses the
    CL0P DLS/brand is used by AT LEAST ONE actor with different TTPs, and did NOT formally
    attribute the 2025 Oracle EBS campaign to a single tracked group. Treat "Cl0p did X" as
    "activity carrying the Cl0p brand," graded per-campaign.
active_since: 2019               # Cl0p ransomware first observed ~Feb 2019; TA505 parent active since ~2014
status: active
status_note: >
  Highly active. Pivoted from network-encryption ransomware to serial zero-day mass-exploitation
  data-theft extortion. Confirmed A-grade campaigns through 2025 (Oracle E-Business Suite);
  a 2026 PTC Windchill/FlexPLM campaign is attributed to Cl0p by trade sources only, UNCONFIRMED.
motivation:
  - extortion
  - financial-gain
  - data-theft
threat_level: MEDIUM             # weighted overall 4.6 -> MEDIUM (first-pass scoring 2026-08-12). Supply-chain category HIGH (composite 8) is the primary_threat_vector; MEDIUM overall is a weighting artifact of the espionage-heavy methodology, NOT low risk. Replaces the never-scored placeholder HIGH.
admiralty_grade: A1              # ESTABLISHED campaign history (Accellion/GoAnywhere/MOVEit/Cleo/Oracle EBS) is A1 (CISA, Mandiant/GTIG, Microsoft). The 2026 Windchill tie is B3/suspected — fenced in-body.
tlp: CLEAR
dossier_version: 1
last_updated: 2026-08-12
last_reviewed: 2026-08-12
next_review_due: 2026-11-10       # +90 days
profile_path: threats/threat-actors/Cl0p/
iocs_path: threats/threat-actors/Cl0p/iocs.md
threat_box_path: threats/threat-actors/Cl0p/threat-box.yaml
related_actors: ["015", "016", "013", "025"]   # LockBit, REvil (RaaS peers); Scattered Spider, Icarus (data-theft-extortion pattern peers) — analytic peers, NOT attribution merges (Hard Rule 2)
tracked_since: 2026-04-14
source_findings:
  - finding-2026-07-24-flash-0600-0001    # Windchill/FlexPLM CVE-2026-12569 (exploitation A1; Cl0p tie B3/suspected)
  - finding-2026-07-27-0001               # Windchill campaign enrichment (B2; Cl0p tie B3/suspected)
  - raw-2026-07-21-flash-0000-001         # Oracle EBS Estée Lauder victim disclosure (actor-profiler awareness)
  - finding-2026-05-11-0004               # South Staffordshire Water ICO fine (historical, ZeroLogon)
---

# Cl0p — Threat Actor Profile

**Actor #018**

---

## Overview

Cl0p is the most prolific enterprise-software mass-exploitation extortion operation of the 2020s. It is not a nation-state actor and not a conventional ransomware crew: over five years it has industrialized a repeatable playbook — acquire or develop a zero-day in a widely-deployed enterprise data-movement or engineering platform (Accellion FTA, Fortra GoAnywhere, Progress MOVEit, Cleo, Oracle E-Business Suite), exploit it en masse in a tight window before patches land, steal data via a custom webshell, and extort hundreds of downstream customer organizations at once. Encryption is now frequently skipped — the stolen data alone is the leverage. For an A&D defender the "so what" is direct: Cl0p reaches victims through the ubiquitous platforms the defense industrial base runs on, so exposure is a function of *which enterprise software you expose to the internet*, not whether Cl0p has singled you out.

The operation sits inside the **TA505 / FIN11** financial-crime nexus. The name "Cl0p" denotes both a criminal crew and an extortion **brand** — a leak site and an encryptor family used across a cluster of operators. This distinction is load-bearing for attribution: Google Threat Intelligence Group (GTIG) has publicly assessed that the CL0P data-leak site and brand are used by **at least one actor with different TTPs**, and declined to formally attribute the 2025 Oracle E-Business Suite campaign to a single tracked group even while noting historical FIN11 overlap. Archimedes therefore treats "Cl0p did X" as "activity carrying the Cl0p brand," graded campaign by campaign, and never originates a firm attribution beyond what a cited source states (Hard Rule 2).

Cl0p's **established** campaign record is A-grade and beyond reasonable dispute: CISA/FBI advisory AA23-158A (MOVEit), Mandiant/GTIG reporting (FIN11, GoAnywhere, Oracle EBS), and Microsoft (Lace Tempest) all attribute the major campaigns. What is **not** settled is the group's most A&D-relevant recent surface: a **2026 campaign against PTC Windchill / FlexPLM (CVE-2026-12569)** that trade sources (ReliaQuest, SecurityWeek) attribute to Cl0p **only with an explicit "unconfirmed / tradecraft-similarity" hedge**. Archimedes grades that tie **B3 / possibly** and fences it throughout this dossier: the *exploitation* of Windchill is confirmed (CISA KEV), the *Cl0p attribution* is suspected-only. Because Windchill is the dominant PLM platform across the ITAR-regulated DIB, this is the surface to watch — but it is not, today, a confirmed Cl0p prime compromise.

The disciplined bottom line: Cl0p is a **MEDIUM**-overall threat to an A&D prime whose **supply-chain / platform-mass-exploitation category scores HIGH** (composite 8). The MEDIUM overall is a weighting artifact of an espionage-weighted methodology applied to a pure criminal-extortion actor — it is emphatically **not** a statement that Cl0p is low risk to the platforms the DIB depends on. See `threat-box.md`.

---

## Primary Targets

- **Internet-exposed enterprise data-movement and engineering platforms** — Cl0p selects the *platform*, not the sector: managed file-transfer (Accellion FTA, GoAnywhere MFT, MOVEit Transfer, Cleo Harmony/VLTrader/LexiCom), ERP (Oracle E-Business Suite), and — per suspected 2026 reporting — PLM/PDM (PTC Windchill/FlexPLM). Whoever runs the vulnerable software and exposes it is a target.
- **Large US and Western enterprises** — the victim ledgers skew heavily to US/Western organizations across finance, healthcare, higher education, retail, logistics, manufacturing, technology, and government.
- **Manufacturing / engineering / logistics (sector-relevant to A&D)** — the platforms Cl0p serially targets are core DIB infrastructure. MOVEit-era victim disclosures (2023) included US government and defense-adjacent organizations as part of the mass compromise; the suspected 2026 Windchill campaign names **aerospace among targeted sectors** (though at customer-base level, not a named prime).

**Geographic Focus:** US-and-Western-enterprise-dominant. No geographic *selection* — targeting is driven by platform exposure, not geography — but the realized victim base is overwhelmingly North American and European.

**A&D-prime targeting:** No confirmed, named A&D-prime victim in Archimedes-graded reporting. A&D exposure is **structural**: (a) the DIB runs the exact platforms Cl0p mass-exploits (Windchill PLM holds ITAR/EAR-controlled engineering data; MFT platforms move controlled data); (b) MOVEit's 2023 mass compromise touched defense-adjacent and government organizations; (c) the 2026 Windchill campaign names aerospace as a sector — but the Cl0p attribution on that campaign is **suspected-only (B3)**. Do not read structural relevance as a documented prime compromise.

---

## Signature Campaigns

| Campaign | Year | Description |
|---|---|---|
| **Accellion FTA** | 2020–2021 | Exploited four zero-days (CVE-2021-27101/-27102/-27103/-27104) in the legacy Accellion File Transfer Appliance; deployed the custom **DEWMODE** PHP webshell to exfiltrate data from 300+ tenants, then extorted via the Cl0p leak site. Mandiant tracked exploitation as UNC2546 and extortion as UNC2582 (both later folded into the FIN11 story). First large-scale demonstration of the "steal-and-extort, skip encryption" model. |
| **GoAnywhere MFT** | 2023 (Jan–Feb) | Zero-day exploitation of **CVE-2023-0669** (deserialization RCE) in Fortra GoAnywhere MFT; the group claimed ~130 victims compromised over roughly 10 days. |
| **PaperCut** | 2023 (Apr) | Microsoft attributed exploitation of PaperCut print-management servers (**CVE-2023-27350**) to Cl0p (Lace Tempest) alongside LockBit — a data-theft, not file-transfer, surface. |
| **MOVEit Transfer** | 2023 (May–Jun) | The defining campaign. Zero-day SQL-injection **CVE-2023-34362** in Progress MOVEit Transfer, exploited en masse from ~27 May 2023; deployed the **LEMURLOOT** C# webshell (dropped as `human2.aspx` and variants). Eventually ~2,700+ organizations and tens of millions of individuals affected across every sector, including US government and defense-adjacent orgs. Subject of CISA/FBI advisory **AA23-158A**; US State Dept Rewards for Justice offered up to $10M for information. |
| **Cleo MFT** | 2024 (Dec) | Mass exploitation of **CVE-2024-50623** and the related **CVE-2024-55956** in Cleo Harmony/VLTrader/LexiCom; Cl0p claimed the campaign on its leak site 24 Dec 2024 and named 182+ organizations by Feb 2025 (Hertz, WK Kellogg, Western Alliance Bank, Blue Yonder, Chicago Public Schools, and others). Notably re-hit organizations that believed they had already patched. |
| **Oracle E-Business Suite** | 2025 | Zero-day exploitation (**CVE-2025-61882**, with related **CVE-2025-61884**) of Oracle EBS beginning ~9 Aug 2025, weeks before patches (4/11 Oct 2025); extortion-email wave from ~29 Sep 2025 (`support@pubstorm.com` / `.net`). Custom tooling: **GOLDVEIN.JAVA** downloader and the **SAGEGIFT → SAGELEAF → SAGEWAVE** WebLogic loader/dropper/servlet-filter chain (per GTIG/Mandiant). 29+ alleged victims named on the leak site (Harvard, Envoy Air [American Airlines subsidiary], The Washington Post, Logitech, Cox Enterprises, Schneider Electric, Emerson, Estée Lauder, and others). GTIG noted FIN11 overlap but did **not** formally attribute to a single group. |
| **PTC Windchill / FlexPLM** *(SUSPECTED — attribution unconfirmed)* | 2026 | **CVE-2026-12569** (unsafe-deserialization unauth RCE, CVSS 9.3) confirmed actively exploited (CISA KEV 2026-06-25; PTC vendor advisory), JSP webshells deployed, active data-theft extortion campaign since ~20 Jul 2026, extortion from `support@cryptohox.com`, **aerospace among named sectors**. ReliaQuest (via BleepingComputer) and SecurityWeek attribute to Cl0p **only with an explicit "unconfirmed / tradecraft-similarity" hedge** — Archimedes grades the exploitation A1 but the Cl0p tie **B3 / possibly**, recorded strictly as reported (Hard Rule 2). See fenced note below. |
| **South Staffordshire Water** *(historical, regulatory closure)* | 2020–2022 | ~22-month intrusion of a UK water utility (initial access Sep 2020 via malicious email attachment; domain-admin compromise via **ZeroLogon / CVE-2020-1472**); 4.1 TB published on the Cl0p leak site Aug 2022. UK ICO fined the utility £963,900 in 2026. Attribution restated from the 2022 leak-site claim + contemporaneous research; not new. Documents Cl0p's outlier-long dwell-time tolerance. |

> **Discipline note:** Campaigns are discrete named operations, not tool rollouts. Rows above are the operations; the webshells/loaders (DEWMODE, LEMURLOOT, GOLDVEIN, SAGE*) are in **Malware Arsenal**.

---

## ⚠️ Attribution fence — the 2026 PTC Windchill / FlexPLM campaign

This is the single most A&D-relevant surface and the one most likely to be over-read. Hold the line:

- **CONFIRMED (A1):** CVE-2026-12569 is a real, CISA-KEV-listed (2026-06-25), actively-exploited unauth-RCE in PTC Windchill/FlexPLM; attackers deploy JSP webshells and exfiltrate data; an active extortion campaign has run since ~20 Jul 2026; aerospace is named among targeted sectors. (Established across finding-2026-07-24-flash-0600-0001 and finding-2026-07-27-0001.)
- **SUSPECTED-ONLY (B3 / possibly):** that **Cl0p** is the actor. The only bases are ReliaQuest's and SecurityWeek's near-identical "unconfirmed / tradecraft-similarity" language plus a reused extortion address (`support@cryptohox.com`) characterized by ReliaQuest — *not independently verified in the corpus* — as "a known Clop address." Archimedes' own ACH on the two-source pattern ranked genuine-independent-corroboration as the **least**-supported explanation; a Cl0p-copycat hypothesis ties Cl0p at zero inconsistencies. **The second source did not lift the attribution.**
- **Therefore:** the Windchill campaign is **not** counted as confirmed Cl0p activity in this dossier's scoring or IOC-of-record set. `support@cryptohox.com` and CVE-2026-12569 are carried as **suspected/as-reported** indicators, flagged as such. Do not propagate the Cl0p–Windchill tie as confirmed in any brief, and do not let it firm the scoring.

---

## TTPs (MITRE ATT&CK)

> **ATT&CK mapping note.** MITRE tracks the **Clop** malware as Software **[S0611](https://attack.mitre.org/software/S0611/)** and the parent financial-crime group as **TA505 ([G0092](https://attack.mitre.org/groups/G0092/))**; there is no dedicated "Cl0p group" G-number. Techniques below are drawn from CISA AA23-158A (MOVEit), GTIG (Oracle EBS), and vendor reporting on the named campaigns.

### Initial Access

| ID | Technique |
|---|---|
| [T1190](https://attack.mitre.org/techniques/T1190/) | Exploit Public-Facing Application — the signature vector: zero-day/n-day exploitation of internet-exposed MFT/ERP/PLM platforms (Accellion, GoAnywhere, MOVEit, Cleo, Oracle EBS, Windchill-suspected) |
| [T1566.001](https://attack.mitre.org/techniques/T1566/001/) | Phishing: Spearphishing Attachment — TA505-lineage malicious-attachment access (e.g., South Staffordshire Water 2020 initial access) |
| [T1195.002](https://attack.mitre.org/techniques/T1195/002/) | Supply Chain Compromise: Compromise Software Supply Chain — platform-level compromise reaching many downstream customer organizations at once |

### Execution / Persistence

| ID | Technique |
|---|---|
| [T1505.003](https://attack.mitre.org/techniques/T1505/003/) | Server Software Component: Web Shell — DEWMODE (Accellion), LEMURLOOT/`human2.aspx` (MOVEit), JSP webshells (Windchill-suspected), SAGEWAVE servlet filter (Oracle EBS) |
| [T1059](https://attack.mitre.org/techniques/T1059/) | Command and Scripting Interpreter — webshell command execution; Java reflective loading (SAGEGIFT) |
| [T1547](https://attack.mitre.org/techniques/T1547/) | Boot or Logon Autostart Execution — Cleo Autorun-directory abuse (CVE-2024-55956) |

### Privilege Escalation / Credential Access

| ID | Technique |
|---|---|
| [T1068](https://attack.mitre.org/techniques/T1068/) | Exploitation for Privilege Escalation — ZeroLogon (CVE-2020-1472) to domain admin (South Staffordshire Water) |
| [T1003](https://attack.mitre.org/techniques/T1003/) | OS Credential Dumping — TA505-lineage credential theft for lateral movement |

### Collection / Exfiltration

| ID | Technique |
|---|---|
| [T1213](https://attack.mitre.org/techniques/T1213/) | Data from Information Repositories — bulk theft of files/records from compromised MFT/ERP/PLM data stores (incl. Oracle EBS `XDO_TEMPLATES_B` / `XDO_LOBS` template abuse) |
| [T1005](https://attack.mitre.org/techniques/T1005/) | Data from Local System — filesystem enumeration and staging on compromised servers |
| [T1567](https://attack.mitre.org/techniques/T1567/) | Exfiltration Over Web Service — data staged and exfiltrated via the webshell/C2; large dumps distributed via torrent for leak-site publication |

### Command & Control

| ID | Technique |
|---|---|
| [T1071.001](https://attack.mitre.org/techniques/T1071/001/) | Application Layer Protocol: Web — GOLDVEIN.JAVA beacons to attacker C2 disguised as a "TLSv3.1" handshake (Oracle EBS) |
| [T1572](https://attack.mitre.org/techniques/T1572/) | Protocol Tunneling — Cobalt Strike / bespoke tunneling in post-exploitation |

### Impact

| ID | Technique |
|---|---|
| [T1657](https://attack.mitre.org/techniques/T1657/) | Financial Theft — data-theft extortion; named-and-shamed on the Tor leak site if unpaid |
| [T1486](https://attack.mitre.org/techniques/T1486/) | Data Encrypted for Impact — the Clop encryptor (S0611), CryptoMix-derived, `.Clop`/`.CIop` extensions — used historically; frequently **skipped** in recent data-theft-only campaigns |

---

## Malware Arsenal

| Malware | Type | Notes |
|---|---|---|
| **Clop** (S0611) | Ransomware / Encryptor | CryptoMix-derived; appends `.Clop`/`.CIop`; drops `README` extortion notes; signed with stolen certs historically. Recent campaigns often skip encryption entirely. |
| **DEWMODE** | Web shell (PHP) | Custom Accellion FTA webshell for silent data exfiltration (2020–2021). |
| **LEMURLOOT** | Web shell (C#/ASP.NET) | Custom MOVEit Transfer webshell (2023); deployed as `human2.aspx` and variants; authenticates HTTP requests with a hard-coded password; can download files, extract Azure Blob storage settings/keys, and create/delete MOVEit users. |
| **GOLDVEIN / GOLDVEIN.JAVA** | Downloader | Java variant used against Oracle EBS (2025); beacons to C2 disguised as a "TLSv3.1" handshake to retrieve a second-stage payload. |
| **SAGEGIFT / SAGELEAF / SAGEWAVE** | Loader / Dropper / Servlet filter | Oracle EBS WebLogic infection chain (2025): SAGEGIFT (custom Java reflective class loader) → SAGELEAF (in-memory dropper, public WebLogic filter-injection lineage) → SAGEWAVE (malicious Java servlet filter enabling AES-encrypted ZIP payload deployment). |
| **TrueBot** | Downloader/Loader | Associated post-exploitation loader in Cl0p/TA505-linked intrusions. |
| **FlawedAmmyy / FlawedGrace (GraceWire)** | RAT | TA505-lineage remote-access tooling. |
| **Get2 / SDBot** | Loader / Downloader | TA505-lineage loaders historically used to stage follow-on payloads. |
| **Cobalt Strike** | Post-exploitation framework | Commodity C2/lateral-movement in hands-on-keyboard phases. |

> The through-line: Cl0p develops **custom, per-platform webshells and loaders** (DEWMODE, LEMURLOOT, GOLDVEIN, SAGE*) rather than relying on commodity tooling — which is why its supply-chain/mass-exploitation capability scores at high novelty (defensively hard) despite the criminal nature of the group.

---

## Infrastructure Patterns

- **Serial zero-day acquisition/development** against internet-exposed enterprise platforms — a new platform roughly every campaign cycle, exploited before patches are broadly deployed.
- **Custom webshell per platform** — reused tradecraft *class* (drop a webshell, enumerate, stage, exfiltrate) with a *fresh implant* per platform, defeating prior signatures.
- **Tor-hosted data-leak site** ("CL0P^_- LEAKS" / "Clop Leaks") for named-and-shamed victim listing and staged data publication; large dumps distributed via **torrent** to withstand takedown.
- **Per-campaign extortion email addresses** rather than a single static contact — e.g., `support@pubstorm.com` / `.net` (Oracle EBS, GTIG-documented); `support@cryptohox.com` (Windchill-suspected, ReliaQuest-reported). Address reuse is sometimes cited as an attribution signal but is imitable and not dispositive.
- **Bulletproof/rented hosting** for exploitation-source and C2 IPs (e.g., the Oracle EBS C2 set); infrastructure rotates per campaign.
- **Long dwell tolerance when needed** — mass-exploitation windows are short, but Cl0p has also maintained covert access for extended periods (South Staffordshire Water: ~22 months from initial access to discovery).

---

## Known IOCs

Indicators span the confirmed A-grade campaigns (MOVEit `human2.aspx`/LEMURLOOT; Oracle EBS C2 IPs and `pubstorm` extortion addresses; per-campaign CVEs) plus **suspected/as-reported** 2026 Windchill indicators (`support@cryptohox.com`, CVE-2026-12569) that are explicitly flagged pending firmer attribution. No credentials are stored (Hard Rule 7). First-party Splunk (`defenseclaw_local`) returned **0 hits** across all queryable Cl0p indicators over the scoring window — a visibility-bounded null (Frank is not a MOVEit/Cleo/Oracle-EBS/Windchill tenant), neither corroboration nor disconfirmation.

See [`iocs.md`](iocs.md) for the human-readable reference and hunt guidance, and [`iocs.yaml`](iocs.yaml) for the agent-queryable sidecar.

---

## Geopolitical Context

Cl0p is a financially-motivated criminal enterprise, not a state instrument. Multiple A-grade vendors assess it as Russian-speaking and based in a Commonwealth of Independent States country; there is no evidence of state tasking, though Russian-based criminal groups operate with de-facto impunity so long as they avoid CIS-country victims. In **June 2021** Ukrainian law enforcement, with US and South Korean cooperation, arrested six individuals linked to the group and disrupted infrastructure — a genuine disruption that nonetheless did **not** end operations; the brand resumed within months and went on to run its largest campaigns (MOVEit, Cleo, Oracle EBS) afterward. The **willingness modifier is 0** across all categories: no diplomatic, sanctions, or law-enforcement constraint has meaningfully deterred the operation.

The criminal-brand structure has geopolitical analytic consequences: because the CL0P leak site and encryptor are used by more than one operator (GTIG), "Cl0p" is best read as a shared extortion franchise. This is why Archimedes refuses to collapse every "Cl0p" campaign into one monolithic actor and grades attribution per campaign.

---

## Connection Web

The following are analytic peers and pattern-adjacent comparisons. Per Hard Rule 2, Archimedes asserts **no attribution merge** beyond what cited sources state; the TA505/FIN11 relationships below are the vendor-documented lineage, not Archimedes-originated.

- 🧬 **TA505 (G0092) / FIN11** — the parent financial-crime cluster and the Mandiant/GTIG designation under which the major Cl0p campaigns are tracked (UNC4857 MOVEit exploitation merged into FIN11). This is **documented lineage**, cited to Mandiant/GTIG — not an Archimedes origination.
- ⛓️ **[Actor #015 LockBit](../LockBit/profile.md)** *(roster; dossier pending)* — RaaS peer; co-attributed with Cl0p by Microsoft in the 2023 PaperCut (CVE-2023-27350) exploitation. Peer, not merge.
- ⛓️ **[Actor #016 REvil](../REvil/profile.md)** *(roster; dossier pending)* — Russian-speaking RaaS peer; historical extortion-ecosystem comparator. Peer, not merge.
- ⛓️ **[Actor #013 Scattered Spider](../Scattered-Spider/profile.md)** *(roster; dossier pending)* — data-theft-extortion pattern peer (different access tradecraft). Peer, not merge.
- ⛓️ **[Actor #025 Icarus](../Icarus/profile.md)** — data-theft-extortion + supply-chain-pivot pattern peer (OAuth/SaaS vector vs. Cl0p's platform-zero-day vector). Pattern-adjacent only; NO attribution link.

The `related_actors` frontmatter array `["015","016","013","025"]` encodes these as analytic peers, not confirmed relationships.

---

## Defense Recommendations

1. **Inventory and internet-exposure-audit every managed file-transfer, ERP, and PLM platform** — MOVEit, GoAnywhere, Cleo, Accellion/Kiteworks, Oracle E-Business Suite, and **PTC Windchill/FlexPLM**. Cl0p's entire model is exploiting these at the perimeter. Anything internet-facing that doesn't need to be should be behind VPN/allow-listing. This is the single highest-leverage control against Cl0p.
2. **Prioritize emergency patching of MFT/ERP/PLM zero-days and KEV entries within hours, not the maintenance window** — Cl0p exploits in a short window before broad patch deployment. Specifically for the DIB: patch **CVE-2026-12569 (Windchill/FlexPLM)** immediately (CISA KEV 2026-06-25; PTC patches from 2026-06-17) regardless of the unresolved actor attribution — the exploitation is confirmed.
3. **Hunt for webshells on the platforms above** — MOVEit: `human2.aspx` and any unexpected `.aspx` under the MOVEit web root (LEMURLOOT); Windchill: unexpected `.jsp` webshells and suspicious requests to `/servlet/WindchillGW/`, `/servlet/WindchillAuthGW/`; Oracle EBS: malicious templates in `XDO_TEMPLATES_B` / `XDO_LOBS` and requests to `/OA_HTML/SyncServlet` and `/OA_HTML/configurator/UiServlet`. See `iocs.md` for queries.
4. **Alert on the documented Oracle EBS C2 and extortion infrastructure** — network alerts for `162.55.17.215`, `104.194.11.200` (GOLDVEIN.JAVA C2), `200.107.207.26`, `161.97.99.49` (exploitation source), and mail-gateway detections for extortion senders `support@pubstorm.com` / `.net`. Add `support@cryptohox.com` as a **suspected** Windchill-campaign indicator.
5. **Baseline and alert on anomalous outbound data volume from MFT/ERP/PLM servers** — Cl0p's impact is bulk exfiltration, often without encryption, so there may be no ransomware "boom." A spike in outbound bytes from a file-transfer or PLM host, or a webshell serving large downloads, is the detection opportunity.
6. **Treat any "we exploited your MFT/ERP/PLM and stole your data" extortion email as a live incident** — Cl0p's extortion often arrives by email before leak-site listing. Preserve headers, do not engage, and immediately triage the named platform for webshells and exfiltration evidence.
7. **Monitor the Cl0p leak site for your organization and your Tier-1/2 suppliers** — Cl0p's mass campaigns routinely catch third parties; a supplier listed on the DLS is a supply-chain exposure to your controlled data. Extend monitoring to the vendor tier.
8. **Patch ZeroLogon (CVE-2020-1472) and audit domain-controller Netlogon exposure** — a legacy but still-abused Cl0p privilege-escalation path to domain admin (South Staffordshire Water). Confirm all DCs are patched and enforcing secure RPC.

---

## References

**Confirmed campaigns (A-grade):**
- [CISA/FBI AA23-158A — #StopRansomware: CL0P Ransomware Gang Exploits CVE-2023-34362 MOVEit Vulnerability](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-158a) (primary; LEMURLOOT/`human2.aspx`, TTPs, IOCs)
- [Google Threat Intelligence Group — Oracle E-Business Suite Zero-Day Exploitation](https://cloud.google.com/blog/topics/threat-intelligence/oracle-ebusiness-suite-zero-day-exploitation) (CVE-2025-61882/-61884, GOLDVEIN/SAGE*, FIN11 overlap, non-attribution caveat)
- [Mandiant/Google — Zero-Day MOVEit Data Theft (FIN11 / UNC4857)](https://cloud.google.com/blog/topics/threat-intelligence/zero-day-moveit-data-theft) (FIN11 attribution of MOVEit)
- [Recorded Future / Insikt — Cleo MFT CVE-2024-50623 Vulnerability Analysis](https://www.recordedfuture.com/blog/cleo-mft-cve-2024-50623-vulnerability-analysis) (Cleo campaign)
- Microsoft Threat Intelligence — Lace Tempest (DEV-0950) attribution of MOVEit and PaperCut (CVE-2023-27350) exploitation

**MITRE / catalog:**
- [MITRE ATT&CK — Clop (Software S0611)](https://attack.mitre.org/software/S0611/)
- [MITRE ATT&CK — TA505 (Group G0092)](https://attack.mitre.org/groups/G0092/)
- [CISA KEV Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) (CVE-2023-34362, CVE-2024-50623, CVE-2025-61882, CVE-2026-12569, etc.)

**Suspected 2026 Windchill campaign (attribution UNCONFIRMED — B3):**
- [finding-2026-07-24-flash-0600-0001](../../findings/finding-2026-07-24-flash-0600-0001-clop-hedged-ptc-windchill-flexplm-cve-2026-12569-active-exploitation-webshell-a1-exploit-b3-attribution.md) (Archimedes; exploitation A1, Cl0p tie B3/possibly)
- [finding-2026-07-27-0001](../../findings/finding-2026-07-27-0001-securityweek-clop-hedged-ptc-windchill-flexplm-cve-2026-12569-active-extortion-campaign-aerospace-b2-likely-update-to-0724.md) (Archimedes; campaign enrichment B2, Cl0p tie B3/possibly)
- BleepingComputer — "Clop ransomware targets Windchill, FlexPLM in data theft attacks" (relay of ReliaQuest research; attribution self-labeled unconfirmed)

**Historical / context:**
- [finding-2026-05-11-0004 / raw-2026-05-11-pm-002 — South Staffordshire Water ICO fine](../../findings/finding-2026-05-11-0004.md) (ZeroLogon, ~22-month dwell)
- [The Record — Estée Lauder / Oracle EBS victim disclosure](https://www.bleepingcomputer.com/news/security/est-e-lauder-discloses-data-breach-via-oracle-e-business-flaw/) (via raw-2026-07-21-flash-0000-001; Cl0p victim-ledger data point)

> **Ukraine 2021 arrests:** In June 2021 Ukrainian police, with US/ROK cooperation, arrested six individuals linked to Cl0p and disrupted infrastructure; operations resumed within months. No DOJ indictment names the current core operators; the US Rewards for Justice program has offered up to $10M for information on the MOVEit-campaign actors.

---

*Created 2026-08-12 — first-pass dossier build for the pre-existing roster stub (#018, tracked since 2026-04-14; prior placeholder threat_level HIGH was never scored). Established campaign history graded A1 (CISA, Mandiant/GTIG, Microsoft); the 2026 PTC Windchill/FlexPLM Cl0p tie is graded B3/suspected and fenced throughout (Hard Rule 2). Threat-box scored 2026-08-12: weighted 4.6 → MEDIUM (auto-commit with notification); supply-chain category HIGH (composite 8) is the primary threat vector; Hard Rule 5 gate did NOT fire. First-party Splunk 0 hits in defenseclaw_local — visibility-bounded null, no IOC-corroboration bonus.*
