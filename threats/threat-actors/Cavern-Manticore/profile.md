---
id: "026"
primary_name: "Cavern Manticore"
aliases: []
mitre_attack_id: null
mitre_attack_url: null
type: "Nation-State APT"
attribution:
  nation: IR
  service: "MOIS (Ministry of Intelligence and Security) — per Check Point Research"
  unit: null
active_since: 2026                     # first documented by CPR 2026-07-06; no earlier date established
status: active
status_note: "First documented 2026-07-06 by Check Point Research against Israeli IT-provider and government orgs. Single-source; CPR primary not directly retrieved."
motivation:
  - espionage
threat_level: LOW                      # overall weighted 3.25 → LOW; per-category espionage = MEDIUM (composite 5). See threat-box.yaml.
admiralty_grade: A2
tlp: CLEAR
dossier_version: 1
last_updated: 2026-07-07
last_reviewed: 2026-07-07
next_review_due: 2026-10-05
profile_path: threats/threat-actors/Cavern-Manticore/
iocs_path: threats/threat-actors/Cavern-Manticore/iocs.md
threat_box_path: threats/threat-actors/Cavern-Manticore/threat-box.yaml
related_actors:
  - "022"      # MuddyWater — CPR-noted tactical overlap (NOT an Archimedes attribution merge)
  - "023"      # APT34/OilRig — CPR-noted tactical overlap via Lyceum subgroup (NOT an Archimedes attribution merge)
notes_for_intake: |
  First-pass profile created 2026-07-07 via /new-actor Cavern Manticore (operator
  Ryan) from finding-2026-07-06-0001 (Check Point Research relayed by The Hacker
  News). SINGLE-SOURCE: CPR is the sole originating primary; The Hacker News is a
  pure relay, not independent corroboration. CPR primary NOT directly retrieved.
  Admiralty A2, WEP "likely," single-source veto applied. All attribution and the
  entire cluster designation inherit from CPR per Hard Rule 2 — no
  Archimedes-originated attribution. CPR-noted tactical overlaps with MuddyWater
  (#022) and Lyceum/OilRig (#023) are recorded as CPR's assessment ONLY; NO roster
  cross-walk asserted. finding-2026-07-06-0001 carries analyst_review_required=true
  for a SAT-ACH on whether Cavern Manticore is a genuinely distinct cluster vs. a
  MuddyWater/OilRig sub-cluster — that ACH is the analyst's job and remains a
  standing open question.
---

# Cavern Manticore — Threat Actor Profile

**Actor #026**

---

## Overview

Cavern Manticore is a newly designated Iran-nexus cluster documented by Check Point Research (CPR) on 2026-07-06 and assessed by CPR as affiliated with Iran's Ministry of Intelligence and Security (MOIS). CPR ties the cluster to a previously-undocumented modular command-and-control framework it calls **Cavern** (aka **Cav3rn**) — a toolset built on a shared .NET foundation — used against Israeli organizations, primarily IT providers and government. Note that "Cavern"/"Cav3rn" are the *toolset/framework* names, not aliases of the actor.

**This entire dossier rests on one IR vendor.** CPR is the sole originating primary; The Hacker News, which relayed the research, is a pure rewrite and does NOT constitute independent corroboration. The CPR primary was not directly retrieved at intake. Per the Admiralty grading (A2, WEP "likely," single-source veto applied), every claim below — the MOIS affiliation, the Cavern framework, the target set, and the very existence of "Cavern Manticore" as a distinct cluster — inherits from CPR and should be read as a single-source assessment pending independent second-IR-vendor confirmation (Mandiant / CrowdStrike / Unit 42 / MSTIC / Microsoft) or direct retrieval of the CPR primary.

**Standing attribution caveat.** CPR designates Cavern Manticore a DISTINCT new cluster while noting *tactical overlaps* with MuddyWater and Lyceum (which CPR assesses as an OilRig subgroup). Archimedes records CPR's overlap language verbatim and originates NO cross-walk merging Cavern Manticore into MuddyWater (#022) or APT34/OilRig (#023) — that would violate Hard Rule 2. Whether Cavern Manticore is a genuinely distinct cluster, a MuddyWater/OilRig sub-cluster, or a re-labeling is an open question flagged for a SAT-ACH by the analyst; it is not resolved here.

For the Archimedes target profile (mid-to-large US A&D contractor), Cavern Manticore's relevance is **indirect and structural**, not direct. Aviation appears among CPR's named target sectors, but no A&D-prime victim is identified and targeting is geographically anchored to Israel (primary), Egypt, and the UAE. The A&D concern is second-order: (1) aviation sits among the sectors CPR names; (2) the actor's IT-provider targeting is a supply-chain exposure pattern relevant to any org sharing regional IT service providers; and (3) it fits the broader Iran-MOIS regional-collection pattern already tracked via MuddyWater and APT34. No A-grade source documents A&D-prime-direct targeting — so per the evidence-minimum table, Intent is capped at Sector Association.

---

## Primary Targets

- **IT providers** — CPR's primary named victim sector; a supply-chain pivot surface into downstream customers
- **Government / public sector** — Israeli government among primary named targets
- **Aviation** — named among targeted sectors (basis for indirect/structural A&D relevance; no A&D-prime victim identified)
- **Energy** — named among targeted sectors

**Geographic Focus:** Israel (primary), Egypt, United Arab Emirates.

**Named victims:** None identified in CPR reporting.

**A&D-prime relevance:** INDIRECT / STRUCTURAL only. Aviation is among the named sectors and IT-provider compromise creates supply-chain exposure, but there is no documented A&D-prime-direct targeting. Risk to a US A&D prime maps to regional IT-service-provider supply chains and Israeli/GCC partner exposure, consistent with the broader Iran-MOIS regional-collection pattern — not to direct US-soil targeting.

---

## Signature Campaigns

| Campaign | Year | Description |
|---|---|---|
| Cavern (Cav3rn) framework disclosure | 2026 | Check Point Research documents a previously-undocumented modular .NET C2 framework used against Israeli IT-provider and government orgs; CPR designates the operating cluster "Cavern Manticore" and assesses it as MOIS-affiliated |

*No other discrete named campaigns are documented at this time. The Cavern framework disclosure is a tooling/cluster designation, not a multi-campaign body of work — the evidence base is a single CPR report.*

---

## TTPs (MITRE ATT&CK)

CPR's public reporting (as relayed) describes a modular .NET C2 framework, DLL sideloading, and exploitation of a set of CVEs. Technique mapping below is derived from CPR's described tradecraft; it is single-source and coarse-grained. Exploited CVEs are referenced **by ID only** per Hard Rule 3 — no mechanism or PoC detail.

### Initial Access

| ID | Technique |
|---|---|
| T1190 | Exploit Public-Facing Application — actor exploits CVE-2025-52691, CVE-2025-68613, CVE-2025-9316, CVE-2025-34291, CVE-2025-54068 (by ID only per Hard Rule 3; no exploitation detail) |

### Execution

| ID | Technique |
|---|---|
| T1106 | Native API — custom modular .NET (Cavern/Cav3rn) tooling |

### Persistence / Defense Evasion

| ID | Technique |
|---|---|
| T1574.002 | Hijack Execution Flow: DLL Side-Loading — sideloaded/malicious DLLs (uxtheme.dll, n-HTCommp.dll, mhm.dll, db.dll, ode.dll, n-ten.dll, n-sws.dll) |
| T1036.005 | Masquerading: Match Legitimate Name — DLL names mimic legitimate Windows / application components (e.g., uxtheme.dll) |

### Command and Control

| ID | Technique |
|---|---|
| T1071.001 | Application Layer Protocol: Web — Cavern modular .NET C2 (C2 domain hospitalinstallation[.]com) |
| T1105 | Ingress Tool Transfer — modular framework component delivery |

*Technique set is a first-pass mapping from a single CPR report. Treat T-number precision as provisional pending direct retrieval of the CPR primary.*

---

## Malware Arsenal

| Malware | Type | Notes |
|---|---|---|
| Cavern (Cav3rn) | Modular C2 framework | Newly documented by CPR (2026); built on a shared .NET foundation; described by CPR as a mature, adaptable toolset. This is the actor's C2 framework — the "Cavern"/"Cav3rn" names refer to the tooling, NOT to the actor |

*Individual modules/payloads beyond the framework and its sideloaded DLL components are not enumerated in the single available report.*

---

## Infrastructure Patterns

- **DLL side-loading** — delivery/persistence via sideloaded or malicious DLLs bearing legitimate-looking names (uxtheme.dll and six others); hunt on unexpected DLL load paths and name/location mismatches for these artifacts
- **Web-based C2 on registered domains** — C2 observed at hospitalinstallation[.]com; single domain documented, rotation pattern not yet characterized on one report
- **Public-facing-application exploitation for access** — actor leverages a set of 2025-vintage CVEs (by ID only) for initial access
- **Modular .NET tradecraft** — shared .NET foundation across the Cavern framework, consistent with the Iranian MOIS tooling ecosystem CPR situates it in

*Infrastructure characterization is thin — one C2 domain and a DLL name set from a single report. Rotation cadence, staging patterns, and registrar preferences are undocumented.*

---

## Known IOCs

This profile is a first-pass scaffold with 13 IOCs from the originating finding. See `iocs.md` and `iocs.yaml` for the structured set:

- 1 C2 domain (hospitalinstallation[.]com)
- 7 sideloaded/malicious DLL filenames (uxtheme.dll, n-HTCommp.dll, mhm.dll, db.dll, ode.dll, n-ten.dll, n-sws.dll)
- 5 exploited CVEs, by ID only (CVE-2025-52691, CVE-2025-68613, CVE-2025-9316, CVE-2025-34291, CVE-2025-54068)

**First-party Splunk sentinel (2026-07-07):** 0 hits over -90d across `defenseclaw_local` and `archimedes` on the C2 domain and distinctive DLL filenames. Per Hard Rule 8, silent Splunk does NOT disconfirm — Frank is not an Israeli/Egyptian/UAE IT-provider or government org matching the victim profile; visibility-bounded null, not negative evidence.

---

## Geopolitical Context

CPR situates Cavern Manticore within Iran's MOIS-aligned cyber-espionage ecosystem, the same space Archimedes already tracks via MuddyWater (#022, MOIS) and APT34/OilRig (#023, MOIS). CPR's noted tactical overlaps with MuddyWater and Lyceum (an OilRig subgroup per CPR) are consistent with a shared Iranian tooling/tradecraft milieu — but CPR nonetheless calls Cavern Manticore a distinct cluster, and Archimedes asserts no attribution merge.

The target set — Israel primary, plus Egypt and the UAE — tracks Iranian strategic-collection interest in regional adversaries and neighbors, mirroring the regional focus of APT34 and MuddyWater. For a US A&D prime, this maps to the same second-order exposure pattern as its Iranian MOIS peers: regional IT-service-provider supply chains, Israeli/GCC technology partners, and shared regional infrastructure — rather than direct US-soil targeting, which is not documented.

Because the assessment rests on a single, not-directly-retrieved CPR report, the geopolitical framing here is CPR's and should firm up (or be revised) once a second IR vendor weighs in or the primary is retrieved.

---

## Connection Web

- ⛓️ **[Actor #022 MuddyWater](../MuddyWater/profile.md)** — **CPR-noted tactical overlap; NO attribution merge asserted.** CPR reports Cavern Manticore shares tactical overlaps with MuddyWater. Archimedes records this as CPR's assessment only and originates no cross-walk (Hard Rule 2). Both are MOIS-attributed per their respective sources.
- ⛓️ **[Actor #023 APT34 (OilRig)](../APT34/profile.md)** — **CPR-noted tactical overlap via Lyceum; NO attribution merge asserted.** CPR reports overlap with Lyceum, which CPR assesses as an OilRig (APT34) subgroup. Recorded as CPR's language only; no roster cross-walk originated (Hard Rule 2).

*The `related_actors` frontmatter lists "022" and "023" because CPR asserts a documented tactical-overlap relationship — but this reflects CPR-noted overlap, NOT an Archimedes attribution merge. A SAT-ACH by the analyst (whether Cavern Manticore is distinct vs. a MuddyWater/OilRig sub-cluster) remains an open question.*

---

## Defense Recommendations

1. **Hunt for the DLL side-load artifact set** — Alert on loads of `uxtheme.dll`, `n-HTCommp.dll`, `mhm.dll`, `db.dll`, `ode.dll`, `n-ten.dll`, `n-sws.dll` from non-standard paths or by processes that would not normally load them (esp. `uxtheme.dll` loaded from an application directory rather than System32). See `iocs.md` for the hunt query.
2. **Block / alert on the C2 domain** — Add `hospitalinstallation[.]com` to DNS sinkhole / proxy blocklists and hunt historical resolver logs for it (network-infrastructure TTL 90 days — re-validate before long-term reliance).
3. **Patch the exploited CVE set** — Ensure CVE-2025-52691, CVE-2025-68613, CVE-2025-9316, CVE-2025-34291, and CVE-2025-54068 are remediated on internet-facing assets (referenced by ID only; consult vendor advisories for affected products and fixes).
4. **Scrutinize regional IT-service-provider supply chains** — Given the IT-provider targeting pattern, review access held by Israeli/GCC-region IT service providers and managed-service partners; enforce least privilege and phishing-resistant MFA on partner accounts.
5. **Baseline DLL search-order integrity on Windows fleet** — DLL side-loading exploits search-order and signing gaps; enforce DLL search-order hardening and alert on unsigned DLLs loaded from application directories.
6. **Standing corroboration tripwire** — Because this rests on a single not-directly-retrieved CPR report, treat any independent second-IR-vendor confirmation (Mandiant / CrowdStrike / Unit 42 / MSTIC / Microsoft) or direct CPR retrieval as a trigger to re-review and re-score.

---

## References

- [The Hacker News: Iran-linked hackers use new Cavern C2 framework to target Israeli organizations (2026-07-06)](https://thehackernews.com/2026/07/iran-linked-hackers-use-new-cavern-c2.html) — RELAY of Check Point Research; not independent corroboration
- Check Point Research (CPR) — originating primary; **not directly retrieved at intake**. Flagged for collector direct retrieval. CPR is provisional-A per the first-surface Tier-1-vendor-research precedent (72h ratification clock; pending direct retrieval and human ratification).
- Originating finding: `threats/findings/finding-2026-07-06-0001-checkpoint-thn-cavern-manticore-mois-cavern-net-c2-framework-new-cluster-not-in-roster-new-actor-candidate.md`

*No MITRE ATT&CK group page exists for this cluster at time of writing.*

---

*Profile authored 2026-07-07 via `/new-actor` (operator Ryan) by `actor-profiler`. Single-source (Check Point Research); CPR primary not directly retrieved. All attribution and the cluster designation inherit from CPR per Hard Rule 2 — no Archimedes-originated attribution, no roster cross-walk to MuddyWater (#022) or APT34/OilRig (#023). See `threat-box.md` for scoring detail.*
