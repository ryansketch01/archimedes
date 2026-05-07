---
id: "004"
primary_name: "UNC1549"
aliases:
  - Tortoiseshell
  - Smoke Sandstorm
  - Imperial Kitten
  - Crimson Sandstorm
  - "Yellow Liderc"   # CrowdStrike-adjacent reporting (overlap, not full alias)
mitre_attack_id: null              # No MITRE ATT&CK Group ID assigned at first-pass; UNC-prefix reflects pre-attribution Mandiant tracking
mitre_attack_url: null
type: "Nation-State APT"
attribution:
  nation: IR
  service: IRGC
  unit: null                       # No unit-level public attribution
  attribution_source: "Mandiant — IRGC-aligned"
active_since: 2017                 # Earliest Tortoiseshell campaign (Symantec 2019; lineage placed earlier in retrospective Mandiant reporting)
status: active
status_note: "Highly active in Q1–Q2 2026 against US/UK/FR/IL aerospace and defense per Mandiant 2026-05-04."
motivation:
  - espionage
  - long-term-access
  - regional-strategic-collection
  - aerospace-and-defense-targeting
threat_level: HIGH                 # Carried from _roster.yaml entry; threat-box.yaml is TEMPLATE pending /update-tracking
admiralty_grade: A2                # Mandiant A; single-source veto applied per finding-2026-05-05-0001 (WEP capped at "likely")
tlp: CLEAR
dossier_version: 1
last_updated: 2026-05-06
last_reviewed: 2026-05-06
next_review_due: 2026-08-04
profile_path: threats/threat-actors/UNC1549/
iocs_path: threats/threat-actors/UNC1549/iocs.md
threat_box_path: threats/threat-actors/UNC1549/threat-box.yaml
related_actors:
  - "011"   # Charming Kitten — IRGC-IO sister cluster; persona-driven targeting overlap
  - "022"   # MuddyWater — fellow Iranian APT; MOIS rather than IRGC, distinct tasking
  - "023"   # APT34 — MOIS-aligned; overlapping Iranian ecosystem, distinct tradecraft
notes_first_pass: |
  First-pass dossier authored 2026-05-06 from finding-2026-05-05-0001 (Mandiant 2026-05-04
  publication, single-source veto applied, WEP "likely"). All attribution and TTP claims
  inherit from Mandiant per Hard Rule 2 — Archimedes does not originate attribution.
  Threat-box scoring is TEMPLATE pending deliberate /update-tracking pass with the human
  /approve-scoring gate intact.
---

# UNC1549 — Threat Actor Profile

**Actor #004**

---

## Overview

UNC1549 is an IRGC-aligned Iranian cyber-espionage cluster that — per Mandiant's 2024 baseline and the 2026-05-04 expansion report — operates a sustained recruiter-lure tradecraft against aerospace, defense, and aviation organizations. Mandiant attributes the cluster to Iran with high confidence and assesses it overlaps with publicly-tracked clusters Tortoiseshell, Smoke Sandstorm, Imperial Kitten, and Crimson Sandstorm. Microsoft tracks an overlapping cluster as Smoke Sandstorm. The UNC- prefix reflects Mandiant's pre-attribution naming convention and the absence (as of first-pass dossier creation) of a MITRE ATT&CK Group ID.

For the Archimedes target profile (`ad-prime-v1` — mid-to-large US A&D contractor), UNC1549 is the most operationally relevant Iranian APT in the 2026 corpus. The campaign documented in finding-2026-05-05-0001 explicitly extended UNC1549's recruiter-lure operations from historical Israeli A&D targeting into US, UK, French, and Israeli aerospace and defense primes between February and April 2026. Mandiant named target categories (without naming victims): "a major US space and defense contractor" and "a European missile systems integrator." This is a direct sectoral hit on the Archimedes profile, even where no specific prime is publicly identified as a confirmed victim.

UNC1549's tradecraft signature is the recruiter-lure pretext: LinkedIn outreach impersonating defense-industry recruiters, redirect to lookalike careers portals (e.g., `defense-careers-portal.com`, `aerospace-talent-hub.net`), and weaponized .lnk delivery via cloud-storage download. Post-access tooling is custom — MINIBIKE backdoor variants, MINIBUS loader, and an Outlook profile credential harvester. Mandiant's three attribution pillars for the 2026 expansion are (1) MINIBIKE C2 protocol reuse with prior UNC1549 campaigns, (2) Let's Encrypt TLS issuance pattern overlap with ~7-day cycling across UNC1549-linked domains, and (3) Iranian-working-hours operational tempo continuity from 2024–2025 baseline activity.

The 2026-05-04 Mandiant disclosure is currently single-source: The Record (B) and Kevin Beaumont (B) amplify but do not corroborate independently. Per `INTEL-GRADING.md`, the WEP ceiling on the attribution is "likely" pending an independent A/B-grade vendor (Unit 42, MSTIC, CrowdStrike) corroborating. Analyst SAT-ACH on the 2026-05-05 finding placed H1 (UNC1549 as Mandiant claims) at zero inconsistencies; alternative readings (false-flag using leaked MINIBIKE, IAB-composite, Iranian-cluster-confusion) accumulated 2, 0, and 4 inconsistencies respectively. The TLS-issuance pillar (E2) is the most replicable attribution signal and the most plausible vector for any future false-flag mimicry — flagged as a brittleness factor for ongoing review.

---

## Primary Targets

- **Aerospace and defense primes** — US, UK, French, Israeli; specifically named target categories per Mandiant 2026-05-04: "major US space and defense contractor," "European missile systems integrator." Roster ID 004 carries this lineage from the original 2024 Mandiant baseline.
- **Defense recruiting / HR functions** — LinkedIn personas targeting recruiters, hiring managers, and engineering staff with lookalike careers-portal lures.
- **Israeli aerospace and defense** — the historical core targeting set per pre-2026 Mandiant and Symantec (Tortoiseshell) reporting.
- **Aviation and travel-adjacent** — earlier Tortoiseshell campaigns reportedly compromised IT providers serving aviation customers (Symantec 2019 attribution).

**Geographic Focus:** Israel (primary, historical) → US, UK, France, Israel (current 2026 expansion per Mandiant). MENA aerospace and defense organizations also documented.

**A&D-prime relevance:** UNC1549 is the **most directly A&D-relevant Iranian APT** in the 2026 corpus. Direct prime targeting is documented at category level (per Mandiant 2026-05-04), even where specific victim names are withheld. Recruiter-lure tradecraft maps directly onto A&D HR, recruiting, and engineering staff — the surface most exposed to LinkedIn outreach.

---

## Signature Campaigns

| Campaign | Year | Description |
|---|---|---|
| Tortoiseshell — IT supplier compromise | 2018–2019 | Symantec attributes intrusions against IT providers (some serving aviation customers); supply-chain-mediated targeting of downstream customers (cluster precursor). |
| Imperial Kitten / Crimson Sandstorm — defense lure baseline | 2022–2023 | CrowdStrike (Imperial Kitten) and Microsoft (Crimson Sandstorm) document persona-driven lure campaigns against Israeli A&D. |
| Mandiant UNC1549 baseline disclosure | 2024-02 | Mandiant publishes initial UNC1549 cluster identification: recruiter-lure tradecraft, MINIBIKE backdoor, lookalike careers portals, IRGC attribution. |
| 2026 US/UK/FR A&D expansion | 2026-02 to 2026-04 | Mandiant 2026-05-04 — recruiter-lure expansion into US/UK/FR/IL aerospace and defense primes; named target categories include "major US space and defense contractor" and "European missile systems integrator." |

---

## TTPs (MITRE ATT&CK)

> **First-pass scaffold.** Techniques below reflect Mandiant 2024 baseline + 2026-05-04 expansion reporting. Full ATT&CK mapping deferred to a subsequent collector pass against the Mandiant 2024 disclosure and any forthcoming 2026 follow-on reporting.

### Initial Access

| ID | Technique |
|---|---|
| T1566.003 | Spearphishing via Service (LinkedIn outreach impersonating defense recruiters) |
| T1566.002 | Spearphishing Link (lookalike careers portal hosting weaponized .lnk) |
| T1204.001 | User Execution: Malicious Link |
| T1204.002 | User Execution: Malicious File (weaponized .lnk delivery via cloud storage) |

### Execution

| ID | Technique |
|---|---|
| T1059.001 | PowerShell (post-access scripting per Mandiant) |
| T1106 | Native API (custom MINIBIKE backdoor) |

### Persistence

| ID | Technique |
|---|---|
| T1547.001 | Registry Run Keys / Startup Folder (MINIBIKE persistence per prior reporting) |
| T1053.005 | Scheduled Task |

### Defense Evasion

| ID | Technique |
|---|---|
| T1027 | Obfuscated Files |
| T1036 | Masquerading (lookalike careers-portal domains; recruiter persona) |
| T1140 | Deobfuscate/Decode Files |

### Credential Access

| ID | Technique |
|---|---|
| T1003 | OS Credential Dumping (post-MINIBIKE) |
| T1555 | Credentials from Password Stores (custom Outlook profile credential harvester per Mandiant 2026-05) |

### Command and Control

| ID | Technique |
|---|---|
| T1071.001 | Application Layer Protocol: Web (HTTPS C2 to UNC1549 domains) |
| T1573 | Encrypted Channel (Let's Encrypt TLS, ~7-day cert cycling pattern) |
| T1568 | Dynamic Resolution (infrastructure rotation across staging/C2 roles) |

### Collection / Exfiltration

| ID | Technique |
|---|---|
| T1114.001 | Email Collection: Local Email Collection (Outlook profile harvester) |
| T1041 | Exfiltration Over C2 Channel |

---

## Malware Arsenal

| Malware | Type | Notes |
|---|---|---|
| MINIBIKE | Backdoor | UNC1549 signature backdoor; C2 protocol reuse is one of Mandiant's three 2026 attribution pillars; variants documented from 2024 baseline through 2026 campaign |
| MINIBUS | Loader | Pairs with MINIBIKE in 2026 campaign per Mandiant |
| Outlook profile credential harvester | Credential thief | Custom; targets Outlook profile credentials specifically — surfaced in Mandiant 2026-05-04 reporting |

> **Source-of-record arsenal note:** The MINIBIKE/MINIBUS toolchain is, per Mandiant 2026-05-04, not publicly observed in non-UNC1549 hands. ACH evidence E5 (finding-2026-05-05-0001) places this as a UNC1549-distinguishing attribution pillar. If a leak or repository surfaces — flagged as ACH tripwire — the cluster identity assumption requires re-examination.

---

## Infrastructure Patterns

- **Lookalike careers portals as initial-access surface** — domain naming follows defense-recruiter pretext (`defense-careers-portal.com`, `aerospace-talent-hub.net`); registered ahead of LinkedIn outreach campaign waves.
- **Let's Encrypt TLS with ~7-day cert cycling** — Mandiant cites this as one of three attribution pillars for the 2026 expansion. Behavioral pattern; not a static IOC. ACH sensitivity analysis flags this as the most replicable attribution signal (any adversary can mimic Let's Encrypt automation).
- **Domain role-rotation** — distinct domains for delivery (lookalike portals) versus C2 (e.g., `cdn-ml-static.com`, `secure-update-svc.net`); roles do not cross over within a single campaign window.
- **Cloud-storage staging for weaponized .lnk** — delivery URLs route through attacker-controlled portals to cloud-hosted .lnk payloads.
- **Iranian-working-hours operational tempo** — Mandiant cites as continuity signal from 2024–2025 baseline. Sensitivity-analysis flag: tempo can be mimicked via scheduling automation; not a strong stand-alone attribution pillar.

---

## Known IOCs

This profile is a first-pass scaffold built from the eleven IOCs published by Mandiant on 2026-05-04 (finding-2026-05-05-0001). See [`iocs.md`](./iocs.md) and [`iocs.yaml`](./iocs.yaml) for the structured indicator set, organized by:

- Malicious delivery domains (recruiter-lure portals)
- C2 domains and IP addresses
- File hashes (MINIBIKE, MINIBUS staging samples)
- Behavioral indicator: Let's Encrypt 7-day TLS cycling pattern
- Recruiter persona email (fabricated, no PII subject)

**No first-party Splunk observations of UNC1549 infrastructure as of 2026-05-06** — collector queried `defenseclaw_local` and `archimedes` indices for the eleven Mandiant IOCs over -30d window with zero hits. Silent telemetry, not disconfirming.

Mandiant's eleven published IOCs are likely a published subset rather than a complete indicator set (KAC assumption A3 in finding-2026-05-05-0001). Hunt should treat the published IOCs as the operationally-actionable seed and not as an exhaustive list.

---

## Geopolitical Context

UNC1549 is part of Iran's broader IRGC-aligned cyber-operations ecosystem. Per Mandiant's high-confidence attribution, the cluster operates in support of IRGC strategic intelligence collection requirements; the historical Israeli A&D focus reflects the longstanding Iran-Israel cyber-confrontation dynamic. The 2026 expansion into US, UK, French, and Israeli A&D primes maps onto Iranian strategic interest in adversary defense-industrial capability — particularly missile-systems and space-defense programs.

The 2026-05-04 Mandiant report is consistent with continuing IRGC investment in long-running, low-volume, persona-driven espionage operations. The recruiter-lure pretext is operationally cheap (LinkedIn personas + lookalike portals + cloud-staged .lnk) but generates high-value access when it lands on engineering or program-management staff. The tradecraft has not visibly migrated to ransomware or destructive operations within the UNC1549 cluster — those mission profiles sit in adjacent Iranian clusters (MOIS-aligned MuddyWater, MOIS-adjacent Handala Hack) per public reporting.

For a US A&D prime, UNC1549 risk maps to:

- **HR / recruiting / engineering staff exposure to LinkedIn defense-recruiter outreach** — direct primary surface
- **Lookalike careers-portal traffic from corporate browsers** — outbound DNS / proxy hunt surface
- **Outlook profile credential exposure** — endpoint hunt for Mandiant 2026-05 credential-harvester signature
- **Weaponized .lnk delivery via cloud-storage download** — email gateway / endpoint hunt for inbound .lnk from cloud storage with recruiter-pretext context

UNC1549 is the highest direct-targeting Iranian APT for the Archimedes profile in the 2026 corpus. APT34, MuddyWater, and Charming Kitten are second-order, supply-chain-mediated, or generalizable-tradecraft concerns by comparison.

---

## Connection Web

- ⛓️ **[Actor #011 Charming Kitten](../Charming-Kitten/profile.md)** — Sister IRGC cluster (IRGC-IO rather than IRGC). Persona-driven targeting overlap; different objective ecosystem (think-tank/academic vs. A&D recruiter-lure). Some shared infrastructure historical patterns per Microsoft tracking.
- ⛓️ **[Actor #022 MuddyWater](../MuddyWater/profile.md)** — Fellow Iranian APT but MOIS-aligned (different service tasking). UNC1549 ACH evidence E1/E5/E6 explicitly distinguishes UNC1549 tooling and tradecraft from MuddyWater commodity-tooling pattern.
- ⛓️ **[Actor #023 APT34](../APT34/profile.md)** — MOIS-aligned; overlapping Iranian-ecosystem context but no documented operational overlap with UNC1549 specifically. Analytical neighbor, not confirmed operational connection.
- ⛓️ **Tortoiseshell (Symantec taxonomy, 2019)** — Earlier Symantec cluster covering IT-provider compromise targeting aviation and Saudi entities; Mandiant retrospectively places lineage within UNC1549 cluster.
- ⛓️ **Smoke Sandstorm (Microsoft taxonomy)** — Microsoft-tracked overlapping cluster identity per roster aliases.

---

## Defense Recommendations

1. **HR / recruiting threat-awareness program** — UNC1549's primary initial-access surface is LinkedIn defense-recruiter impersonation. A&D primes should run a targeted awareness module for recruiters, hiring managers, engineering leads, and program managers covering recruiter-pretext red flags, lookalike domain spotting, and cloud-storage .lnk delivery patterns. Refresh quarterly.
2. **Block / alert on weaponized .lnk from cloud storage** — Email gateway and endpoint policy should treat `.lnk` files arriving via cloud-storage download links as high-risk, particularly when paired with recruiter or careers-portal pretext context.
3. **Hunt for the eleven published Mandiant IOCs across -90d window** — Run retrospective hunt against `defenseclaw_local` and `archimedes` for the four delivery/C2 domains, two IPv4s, two SHA256 hashes, and the recruiter-persona email. See `iocs.yaml` hunt queries.
4. **DNS / proxy egress monitoring for lookalike careers-portal patterns** — Build hunt query for outbound DNS to domains matching `defense-*-portal*`, `aerospace-*-hub*`, `*-careers-*` patterns from corporate browsers. Tune for known-good HR vendors.
5. **Outlook profile credential exposure hunt** — Endpoint EDR rules for unauthorized read access to Outlook profile credential storage (`HKCU\Software\Microsoft\Office\*\Outlook\Profiles\*`); Mandiant 2026-05 reports a custom Outlook profile credential harvester. Tune for legitimate Outlook tooling.
6. **TLS certificate transparency monitoring** — Subscribe corporate-domain CT-log monitoring for lookalike domains issued under Let's Encrypt; ~7-day cert cycling on domains mimicking the corporate brand is the MINIBIKE infrastructure pattern. Vendors offering CT-log monitoring (e.g., Censys, Crt.sh-based pipelines) are appropriate.
7. **MFA enforcement on privileged engineering and program-management accounts** — UNC1549's post-access objective is credential harvest into privileged identities; phishing-resistant MFA (FIDO2 / hardware tokens) is the highest-value preventive control.
8. **Coverage attestation for prime-tier laptop fleet and Outlook telemetry** — KAC A4 in finding-2026-05-05-0001 flags the assumption that prime-tier first-party telemetry would observe MINIBIKE staging if it occurred. Confirm: laptop-fleet EDR coverage, outbound-DNS visibility for the four UNC1549 domains, and Office365 audit-log retention spans the -90d window.

---

## References

- [Mandiant: UNC1549 expands defense-recruiter lure campaign (2026-05-04)](https://cloud.google.com/blog/topics/threat-intelligence/unc1549-defense-recruiter-lure-2026/) — Mandiant 2026 expansion disclosure; primary source for 2026 campaign frame and the eleven published IOCs (cited in finding-2026-05-05-0001).
- [Mandiant: UNC1549 baseline disclosure (Feb 2024)](https://cloud.google.com/blog/topics/threat-intelligence/) — Original UNC1549 cluster identification (baseline reference; specific URL via Mandiant blog index).
- [The Record: Iran UNC1549 defense recruiter campaign (2026-05-04)](https://therecord.media/iran-unc1549-defense-recruiter-campaign-2026) — B-grade relay; not independent of Mandiant.
- [CrowdStrike Imperial Kitten reporting](https://www.crowdstrike.com/blog/) — CrowdStrike taxonomy for overlapping cluster (Imperial Kitten alias); see CrowdStrike blog index.
- [Microsoft Smoke Sandstorm tracking](https://www.microsoft.com/en-us/security/blog/) — Microsoft taxonomy for overlapping cluster (Smoke Sandstorm alias).
- [Symantec: Tortoiseshell IT-supplier compromise (2019)](https://symantec-enterprise-blogs.security.com/) — Earlier Tortoiseshell cluster reporting, retrospectively associated with UNC1549 lineage.
- finding-2026-05-05-0001 — Archimedes graded finding (digraph A2, WEP "likely") with full ACH and KAC analysis; referenced for sensitivity-analysis tripwires and load-bearing assumption set.

---

*First-pass profile authored 2026-05-06 by `actor-profiler` from finding-2026-05-05-0001.
All attribution and TTP claims herein inherit from cited sources per Hard Rule 2 — Archimedes
does not originate attribution. Threat-box scoring is TEMPLATE pending /update-tracking pass
with /approve-scoring gate.*
