# MiniPlasma (CVE-2020-17103) — Windows cldflt.sys LPE: Patch-Ineffective Zero-Day

## Identity

| Field | Details |
|---|---|
| **CVE** | CVE-2020-17103 — original patch confirmed **ineffective / silently reversed** |
| **Codename** | **MiniPlasma** |
| **ZD ID** | ZD-040 |
| **Vendor Advisory** | [MSRC — CVE-2020-17103](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2020-17103) — Microsoft has not issued a new CVE or advisory acknowledging the regression |
| **Type** | Local Privilege Escalation (LPE) → SYSTEM shell |
| **Class** | CWE-362 — Race Condition / CWE-269 — Improper Privilege Management |
| **Affected Component** | `cldflt.sys` — Windows Cloud Files Mini Filter Driver; routine `HsmOsBlockPlaceholderAccess`; `CfAbortHydration` API |
| **Affected Platform** | Windows 10 · Windows 11 (all versions through May 2026 Patch Tuesday KB5089549; **fixed at June 2026 Patch Tuesday**) · Windows Server 2016/2019/2022/2025 |
| **Not Affected** | Windows 7 · 8 · 8.1 · Server 2008/2008R2/2012/2012R2 (`cldflt.sys` not present) · Windows 11 carrying the June 2026 Patch Tuesday update (fix shipped; Canary had it staged early) |
| **Patch Status** | ✅ **PATCHED** — CVE-2020-17103 (regression) fixed at **June 2026 Patch Tuesday (2026-06-09/10)**. Confirmed by BleepingComputer + The Hacker News. Was exploitable on fully patched May 2026 builds (KB5089549) until the June fix; Microsoft's 2026-05-18 "investigating" statement resolved with the June update. |
| **CVSS v3.1 (original NVD)** | **7.8 HIGH** (`CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H`) |
| **CVSS (regression)** | Fix shipped under the original CVE-2020-17103 at June 2026 PT; no separate new CVE assigned |
| **Exploit Maturity** | 🔴 **PUBLIC PoC** — Full weaponized exploit on GitHub (source + compiled binary); original Google Project Zero PoC works unchanged |
| **PoC** | [Nightmare-Eclipse/MiniPlasma](https://github.com/Nightmare-Eclipse/MiniPlasma) |
| **CISA KEV** | ❌ Not listed — no evidence of active exploitation reported; fixed at June 2026 PT |
| **Attack Requirements** | **Local** — requires existing code execution on target as standard user |
| **Disclosed** | May 14–17, 2026 |
| **Disclosed By** | Chaotic Eclipse (GitHub: Nightmare-Eclipse) — **6th tool** in protest campaign against Microsoft MSRC |
| **Original Discoverer** | James Forshaw (Google Project Zero) — first reported September 2020 |
| **Originally "Patched"** | December 9, 2020 (Patch Tuesday) — patch now confirmed ineffective |
| **Threat Level** | 🔴 HIGH (pre-June-PT) → reduced once June 2026 update applied; public full PoC; SYSTEM shell from standard user; was confirmed on fully patched May 2026 builds until the June fix |
| **Admiralty Grade** | A1 — Confirmed independently by BleepingComputer, Will Dormann (Tharros), The Hacker News; June 2026 PT fix confirmed by BleepingComputer + THN |
| **ATT&CK** | T1068 (Exploitation for Privilege Escalation) · T1106 (Native API) |

---

## Overview

MiniPlasma is the **sixth exploit tool** published by pseudonymous researcher **Chaotic Eclipse** (aka Nightmare-Eclipse) in their ongoing protest campaign against Microsoft's Security Response Center. Published May 14–17, 2026, it is a Windows local privilege escalation exploit targeting `cldflt.sys` (Cloud Files Mini Filter Driver) that achieves **SYSTEM** on fully patched Windows 11 via a race condition in `HsmOsBlockPlaceholderAccess`.

The key finding: a vulnerability in `cldflt.sys` originally reported by Google Project Zero's James Forshaw in September 2020, supposedly patched as CVE-2020-17103 in December 2020, **was never properly fixed — or its fix was silently reversed.** The original GPZ proof-of-concept code works without modification on a Windows 11 system running the latest May 2026 Patch Tuesday updates.

The researcher stated: *"After investigating, it turns out the exact same issue that was reported to Microsoft by Google Project Zero is actually still present, unpatched. I'm unsure if Microsoft just never patched the issue or the patch was silently rolled back at some point for unknown reasons. The original PoC by Google worked without any changes."*

**BleepingComputer independently confirmed** a SYSTEM shell on fully patched Windows 11 Pro (KB5089549). Will Dormann (Tharros) confirmed independently. The exploit did **not** work on Windows 11 Insider Preview Canary — Microsoft was staging a fix. Microsoft issued a statement via SecurityWeek on May 18: *"Microsoft is investigating this report and will take appropriate action."* **Resolution: Microsoft fixed MiniPlasma at June 2026 Patch Tuesday (2026-06-09/10) under the original CVE-2020-17103**, confirmed by BleepingComputer and The Hacker News — the regression that had reopened the 2020 bug is now closed.

**Notable context:** In December 2025, Microsoft patched a related `cldflt.sys` privilege escalation (CVE-2025-62221, CVSS 7.8) that was being actively exploited by unknown threat actors — suggesting this driver has been a persistent target.

---

## Technical Analysis

### Root Cause

`cldflt.sys` is the Windows Cloud Files Mini Filter Driver, responsible for OneDrive-style cloud file transparency (placeholder files, hydration/dehydration). The vulnerable routine is `HsmOsBlockPlaceholderAccess`.

The flaw allows **arbitrary registry key creation in the `.DEFAULT` user hive without proper access checks**, exploitable via the undocumented `CfAbortHydration` API. Because the Cloud Filter driver runs in kernel mode, successfully abusing this primitive escalates privileges to SYSTEM.

### Attack Chain

```
Standard user account
    ↓
Create cloud placeholder file + trigger Cloud Filter activity
    ↓
Call undocumented CfAbortHydration API
    ↓
Race condition window in cldflt!HsmOsBlockPlaceholderAccess
    ↓
Arbitrary registry key write to HKU\.DEFAULT (no access check)
    ↓
Keys enable attacker-controlled code execution in privileged context
    ↓
cmd.exe / arbitrary code as NT AUTHORITY\SYSTEM
```

**Reliability:** Race condition — success rate varies by system load, but described as "works reliably" in researcher testing and confirmed as reliable by Will Dormann on Windows 11.

**No patch applies:** Works on systems running KB5089549 (May 12, 2026 cumulative update, OS build 26100.8457 / 26200.8457).

### Affected Scope

Any Windows system with `cldflt.sys` present is potentially vulnerable:
- All Windows 10 versions (1803 through 20H2 and later)
- All Windows 11 versions (through May 2026)
- Windows Server 2016, 2019, 2022, 2025

Not affected: Windows 7, 8, 8.1, Server 2008–2012R2 (`cldflt.sys` introduced later). Driver is installed by default — no OneDrive configuration required.

---

## Context: Chaotic Eclipse Disclosure Series

| # | Tool | Disclosed | CVE | Patch Status |
|---|---|---|---|---|
| 1 | BlueHammer | Apr 3, 2026 | CVE-2026-33825 | ✅ Patched — Apr 14, 2026 |
| 2 | RedSun | Apr 16, 2026 | CVE-2026-41091 | ✅ Patched — May 20/21, 2026 |
| 3 | UnDefend | Apr 16, 2026 | CVE-2026-45498 | ✅ Patched — May 20/21, 2026 |
| 4 | YellowKey | May 12, 2026 | CVE-2026-45585 | ✅ Patched — June PT |
| 5 | GreenPlasma | May 12, 2026 | CVE-2026-45586 | ✅ Patched — June PT |
| **6** | **MiniPlasma** | **May 14–17, 2026** | **CVE-2020-17103 (regression)** | **✅ Patched — June PT (2026-06-09/10)** |
| 7 | RoguePlanet | Jun 9–10, 2026 | None | 🔴 Unpatched — no CVE (see [RoguePlanet](../RoguePlanet/profile.md)) |

The researcher's **"big surprise"** for June Patch Tuesday materialized as **RoguePlanet** (7th tool, dropped hours after the June fixes shipped) — see the RoguePlanet dossier.

---

## Downstream Risk

While local-only, LPE to SYSTEM is the standard post-exploitation step in nearly every Windows intrusion chain. Prior Nightmare-Eclipse tools were weaponized by third-party actors (geolocated to Russia by Lyrie.ai) within 24–48 hours of release. MiniPlasma will follow the same trajectory.

**Confirmed kill chain using predecessor tools:**
1. Initial access (e.g., compromised SSLVPN/FortiGate credentials)
2. UnDefend deployed — blocks Defender updates, falsifies telemetry
3. RedSun / MiniPlasma → SYSTEM
4. Credential dump, lateral movement

MiniPlasma is a drop-in substitute for RedSun at step 3, via a completely different code path.

---

## Detection

### Behavioral / EDR Indicators

Elastic Defend has confirmed detection coverage against MiniPlasma exploit primitives.

Key signals to monitor:
- Low-privileged process calling undocumented `CfAbortHydration` or unusual Cloud Filter APIs
- Anomalous registry write events in `HKU\.DEFAULT` from non-SYSTEM / non-OneDrive processes (Sysmon Event 13)
- `Event 4688`: SYSTEM-token process spawned from Medium/Low integrity parent with no corresponding auth event
- Rapid repeated Cloud Filter API calls from a single process (race condition artifact)
- `cldflt.sys` kernel callbacks from non-Microsoft processes

### MITRE ATT&CK Mapping

| Tactic | Technique | Notes |
|---|---|---|
| Privilege Escalation | T1068 — Exploitation for Privilege Escalation | `cldflt.sys` race condition → SYSTEM |
| Execution | T1106 — Native API | Abuse of undocumented `CfAbortHydration` API |
| Defense Evasion | T1036 — Masquerading | SYSTEM cmd.exe spawned; appears as legitimate process |

---

## Mitigations

✅ **Patched at June 2026 Patch Tuesday (CVE-2020-17103).** Apply the June 2026 Windows updates to remediate. Compensating controls below remain useful as defence-in-depth and for any endpoints not yet on the June update:

1. **Apply the June 2026 Patch Tuesday update** — primary remediation; closes the CVE-2020-17103 regression
2. **EDR behavioral detection** — Elastic Defend confirmed; other major EDRs likely developing signatures
3. **Disable Cloud Files Mini Filter Driver** on systems that do not require OneDrive Files On-Demand (reduces functionality; verify impact before broad rollout — per Startup Defense guidance re: RedSun mitigation)
4. **Restrict local access** — exploit requires a local standard user account; reduce interactive login exposure for service accounts

---

## Disclosure Timeline

| Date | Event |
|---|---|
| Sep 2020 | James Forshaw (Google Project Zero) reports `cldflt.sys` LPE to Microsoft |
| Dec 9, 2020 | Microsoft patches as CVE-2020-17103 (KB5001649); fix later confirmed ineffective |
| Dec 2025 | Microsoft patches CVE-2025-62221 (related `cldflt.sys` EoP; actively exploited by unknown actors) |
| May 14–16, 2026 | Chaotic Eclipse publishes MiniPlasma PoC on GitHub; researcher confirms original GPZ PoC works unchanged |
| May 17, 2026 | BleepingComputer confirms SYSTEM shell on Windows 11 Pro (KB5089549); Will Dormann confirms independently; THN reports |
| May 18, 2026 | Microsoft issues statement via SecurityWeek: *"investigating...will take appropriate action to protect customers as soon as possible"*; ThreatLocker publishes registry key detection guidance; Profile created (ZD-040) |
| May 20, 2026 | Still unpatched; no new CVE assigned; Profile updated (ZD-040) |
| **Jun 9–10, 2026** | **PATCHED at June 2026 Patch Tuesday under CVE-2020-17103.** Confirmed by BleepingComputer + The Hacker News (alongside YellowKey CVE-2026-45585 and GreenPlasma CVE-2026-45586). No active exploitation reported prior to patch. |

---

## References

- [BleepingComputer — New Windows 'MiniPlasma' Zero-Day Gives SYSTEM Access, PoC Released](https://www.bleepingcomputer.com/news/microsoft/new-windows-miniplasma-zero-day-exploit-gives-system-access-poc-released/)
- [SecurityWeek — Researcher Drops MiniPlasma Windows Exploit for Unpatched 2020 CVE](https://www.securityweek.com/researcher-drops-miniplasma-windows-exploit-for-unpatched-2020-cve/) *(includes Microsoft official statement)*
- [The Hacker News — MiniPlasma Windows 0-Day Enables SYSTEM Privilege Escalation](https://thehackernews.com/2026/05/miniplasma-windows-0-day-enables-system.html)
- [WindowsForum — MiniPlasma PoC Questions KB5089549 Fix for CVE-2020-17103](https://windowsforum.com/threads/miniplasma-poc-questions-kb5089549-fix-for-cve-2020-17103-on-win11.418703/)
- [GitHub — Nightmare-Eclipse/MiniPlasma](https://github.com/Nightmare-Eclipse/MiniPlasma)
- [MSRC — CVE-2020-17103 Advisory](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2020-17103)
- [NVD — CVE-2020-17103](https://nvd.nist.gov/vuln/detail/CVE-2020-17103)
- [Born City (DE) — Nightmare Eclipse veröffentlicht MiniPlasma-Schwachstelle CVE-2020-17103](https://borncity.com/blog/2026/05/16/nightmare-eclipse-veroeffentlicht-miniplasma-schwachstelle/)

---

*Profile created: 2026-05-18 | Updated: 2026-06-10 | Author: C3PO / Archimedes (vuln-tracker) | Admiralty Grade: A1 | TLP: WHITE*

---

## Intelligence Update — 2026-06-10

> **Status: PATCHED.** Microsoft fixed MiniPlasma at June 2026 Patch Tuesday (2026-06-09/10) under the original **CVE-2020-17103** — the regression that reopened the 2020 Cloud Files bug is closed. Status flipped UNPATCHED → PATCHED.

June 2026 Patch Tuesday addressed three Nightmare Eclipse tools simultaneously: MiniPlasma (CVE-2020-17103 regression), YellowKey (**CVE-2026-45585**, BitLocker/WinRE bypass), and GreenPlasma (**CVE-2026-45586**, CTFMON LPE). No new CVE was assigned to MiniPlasma — Microsoft re-fixed under the original 2020 identifier. No active in-the-wild exploitation of MiniPlasma was reported prior to the patch (it was never CISA-KEV-listed). Apply the June 2026 Windows updates; verify on any endpoints that defer updates.

The 7th tool in the series, **RoguePlanet** (Defender race-condition LPE, no CVE), was dropped hours after the June fixes shipped and remains unpatched — see the [RoguePlanet](../RoguePlanet/profile.md) dossier. With the June fixes, MiniPlasma joins BlueHammer, RedSun, UnDefend, YellowKey, and GreenPlasma as patched; only RoguePlanet remains open in the Nightmare Eclipse series.

*Updated: 2026-06-10 | Author: Archimedes (vuln-tracker) | TLP: WHITE*
