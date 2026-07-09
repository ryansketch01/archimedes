# RoguePlanet — Windows Defender Zero-Day Local Privilege Escalation

## Identity

| Field | Details |
|---|---|
| **Vulnerability Name** | RoguePlanet |
| **CVE** | **CVE-2026-50656** — assigned by Microsoft (MSRC); NVD-published 2026-06-16 |
| **CVSS** | **7.0 HIGH** (NVD primary, `CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H`) · 7.8 HIGH (Microsoft secondary, `AC:L`). CWE-59 (Link Following) |
| **Type** | Local Privilege Escalation (LPE) — Elevation of Privilege in the Microsoft Malware Protection Engine |
| **Class** | TOCTOU Race Condition + Defender Remediation Path Redirection (NTFS junction / link-following, CWE-59) — originally a Remote Code Execution primitive, released as LPE |
| **Affected Platforms** | Windows 10 and Windows 11 (fully patched, incl. June 2026 Patch Tuesday / KB5094126; Win11 stable + Canary). Fixed in Malware Protection Engine ≥ 1.1.26060.3008 |
| **Patch Status** | ✅ **PATCHED** — Microsoft shipped an out-of-band Defender Malware Protection Engine update (**1.1.26060.3008**) and assigned **CVE-2026-50656** (reported 2026-07-09; NVD record published 2026-06-16). Engine update auto-deploys (same channel as the BlueHammer precedent). Engine builds do not carry a Windows KB number. This closes the last open tool in the Nightmare Eclipse series — the series is now fully closed |
| **PoC Status** | 🔴 **PUBLIC** — released hours after Patch Tuesday; GitHub/GitLab repos removed by Microsoft, researcher self-hosting on `projectnightcrawler.dev` (and "MSNightmare" GitHub account per THN) |
| **Discovered By** | Nightmare Eclipse / Chaotic Eclipse / Dead Eclipse / MSNightmare / deadeclipse666 (pseudonymous researcher) |
| **Public Disclosure** | June 9–10, 2026 (uncoordinated — dropped hours after Microsoft's June Patch Tuesday) |
| **Confirmed Working** | ThreatLocker (independently reproduced on patched Windows 11) |
| **Exploited in Wild** | ⚪ Not confirmed for RoguePlanet specifically as of 2026-06-10. Earlier tools in the series (BlueHammer / RedSun / UnDefend) confirmed in-the-wild by Huntress |
| **Reliability** | Race condition — researcher reports ~100% on some machines, unreliable on others |
| **Series Position** | 7th drop in the Nightmare Eclipse series — fulfilled the YellowKey "big surprise" threat for June Patch Tuesday; now the series-closing patch |
| **KEV Status** | ⚪ Not listed (CISA KEV catalog 2026.07.07). CVE assignment restores KEV-*eligibility* (previously ineligible for lack of a CVE); KEV-eligible-but-not-yet-listed — watch signal active |
| **Admiralty Grade** | State-change (patch) fact: **A2** — Microsoft vendor self-disclosure of a fix on its own product, relay-conveyed via BleepingComputer + SecurityWeek (single-source veto: two bylines relay one Microsoft action). Prior pre-patch disclosure profile: B2 |

---

## Overview

RoguePlanet is the seventh public disclosure in the Nightmare Eclipse series and the "big surprise" the researcher promised for June 2026 Patch Tuesday. It was dropped publicly on June 9–10, 2026, hours after Microsoft shipped its June Patch Tuesday fixes — which addressed two earlier tools in the series (GreenPlasma and YellowKey) but left RoguePlanet untouched.

RoguePlanet is a **race-condition Local Privilege Escalation** in Microsoft Defender. A standard, low-privileged local user can win a timing window against a Defender file operation that runs as SYSTEM, redirect that operation via an NTFS junction, and obtain a command prompt running as **NT AUTHORITY\SYSTEM** on a **fully patched Windows 10 or Windows 11** machine — including systems carrying the June 2026 Patch Tuesday updates. Because it is a race, reliability varies: the researcher reports near-100% success on some hardware and inconsistent results on others.

Notably, RoguePlanet did not start as an LPE. The researcher describes the underlying bug as originally a **Remote Code Execution** primitive that abused Defender's handling of files staged on remote SMB shares (a victim coerced into opening a malicious `.vhd(x)` on an attacker-controlled SMB server, after which Defender would overwrite its own files). Per the researcher, Microsoft *silently* hardened the relevant Defender internals (reported as `mpengine!SysIO*` handling) in mid-May 2026, blocking the junction-based remote vector — so the bug was reworked and released as a local privilege escalation instead.

For an A&D contractor, the operational shape is familiar and dangerous: Windows Defender is the default endpoint protection across essentially the entire defense industrial base, and a standard-user-to-SYSTEM escalation on fully patched endpoints is a textbook ransomware / lateral-movement pre-cursor primitive.

> **STATE CHANGE — 2026-07-09 (patched; CVE assigned).** Microsoft shipped an **out-of-band Malware Protection Engine update (1.1.26060.3008)** and assigned **CVE-2026-50656** (NVD-published 2026-06-16; the OOB engine push and CVE surfaced in reporting 2026-07-09). The engine update auto-deploys through the same Defender channel used for the BlueHammer fix, so estates on current Defender definitions receive it without administrator action. NVD scores it **7.0 HIGH** (primary; `AV:L/AC:H/PR:L`, the `AC:H` reflecting the timing race) with a **7.8 HIGH** Microsoft secondary score, CWE-59 (Link Following — consistent with the NTFS-junction redirect mechanism). **With RoguePlanet patched, the Nightmare Eclipse / Chaotic Eclipse series is fully closed** — every one of the seven tools now carries a CVE and a fix. The CVE assignment also restores CISA-KEV *eligibility* (RoguePlanet was previously ineligible only for lack of a CVE); as of KEV catalog 2026.07.07 it is **not yet listed** — a live watch signal. This finding is a defensive-positive de-escalation, graded A2 on the procedural vendor-patch fact.

---

## Technical Analysis

> **Defensive framing only.** This section describes the vulnerability class, the subsystems involved, and the telemetry a defender can watch for. It contains no exploit code, no payloads, and no step-by-step exploitation instructions (Hard Rule 3).

### Vulnerability Class

RoguePlanet is a **Time-of-Check to Time-of-Use (TOCTOU) race condition** in Microsoft Defender's file-path validation during its remediation / file-handling workflow. Defender's relevant file operations execute in the SYSTEM security context. The vulnerability arises because Defender validates a path and later acts on it without re-verifying that the path has not been swapped underneath it.

### Mechanism (conceptual)

- **The race target** is a Defender file operation performed as SYSTEM. The exploit competes against Defender's own timing to interpose between Defender's path check and its file action.
- **The redirection primitive** is an **NTFS junction point** (mount-point reparse). Standard users can create junctions without elevation. By swapping a directory for a junction at the right moment, a write or file operation Defender believes is targeting one location is silently redirected by the kernel to an attacker-chosen location — Defender has no awareness of the redirection.
- **The outcome** is execution in SYSTEM context — the PoC spawns a command prompt as `NT AUTHORITY\SYSTEM`.

This is the same conceptual family as the researcher's earlier Defender LPEs (RedSun's unvalidated reparse/junction write-back path; BlueHammer's TOCTOU + path confusion) — legitimate Windows components interacting in a sequence Defender does not defend against, rather than memory corruption or a kernel bug. The researcher has separately claimed to hold "a batch of memory corruption vulnerabilities in Defender as well" — unverified, noted for tracking.

### Origin: RCE → LPE

The bug began as a **remote** primitive: Defender's handling of files on remote SMB shares could be abused so that, when a victim was coerced into opening a malicious `.vhd(x)` hosted on an attacker SMB server, Defender would be steered into overwriting its own files — a path to remote code execution. Per the researcher, Microsoft silently hardened Defender's internal file I/O handling in mid-May 2026, closing the remote junction vector. RoguePlanet is the reworked **local** form of that bug. RCE feasibility on current builds is described as unclear.

### Why Standard Hardening Does Not Stop It

Because RoguePlanet abuses legitimate Defender behavior and a standard-user NTFS feature rather than corrupting memory, kernel-level exploit mitigations (CFG, hardware stack protection, Exploit Guard) provide no protection. The defensive levers are behavioral detection of the junction/redirect pattern, application allowlisting, and reducing the standing population of accounts that can run the trigger.

---

## Affected Systems

| Platform | Status | Notes |
|---|---|---|
| Windows 10 (fully patched, incl. June 2026 PT) | ✅ Vulnerable | Confirmed; tested against KB5094126-patched systems |
| Windows 11 (stable + Canary, fully patched incl. June 2026 PT) | ✅ Vulnerable | Confirmed; ThreatLocker reproduced on patched Win11 |
| Windows Server (all) | ⚠️ Believed vulnerable, PoC non-functional | Underlying bug believed present; current PoC does not run because standard users cannot mount ISO/`.vhd(x)` images on Server |

**Requires:** Local user account + Microsoft Defender active. No admin rights, no kernel exploit, no memory corruption required for the LPE.

**Fix boundary:** Microsoft Malware Protection Engine **≥ 1.1.26060.3008** (per NVD affected-configuration: engine versions *prior to* 1.1.26060.3008 are vulnerable). The engine update auto-deploys with Defender definition updates; no Windows KB / OS-level patch is involved.

---

## Public PoC Status

| Location | Status | Notes |
|---|---|---|
| Original GitHub / GitLab repos | Removed | Taken down by Microsoft |
| `projectnightcrawler.dev` (researcher self-hosted) | Public | Researcher relocated PoC after takedowns (per BleepingComputer) |
| "MSNightmare" GitHub account | Public | Reported by The Hacker News / SecurityAffairs |

> Per Hard Rule 3, the PoC code is **not** mirrored or summarized at an actionable level in this dossier. Only the existence, hosting, and reliability characteristics are tracked.

---

## IOCs & Detection

No file hashes or network IOCs have been published for RoguePlanet as of 2026-06-10. Detection is behavioral. The observables below are inferred from the documented mechanism and the closely-related RedSun behavioral profile; treat as hunt hypotheses pending validation against a controlled sample.

### Behavioral Indicators

| Behavior | Telemetry | Confidence |
|---|---|---|
| NTFS junction / reparse point created by a non-system, medium/low-integrity process, then targeted by a Defender file operation | File-system minifilter / EDR reparse-point creation events correlated with `MsMpEng.exe` activity | 🟡 MEDIUM |
| `MsMpEng.exe` (Defender) performing a file operation that resolves through a user-created junction into an unexpected target path | EDR process/file telemetry on Defender file write/move targets | 🟡 MEDIUM |
| Interactive SYSTEM shell (`cmd.exe` / `conhost.exe`) spawned in a standard user's session immediately following Defender remediation activity | Process-creation telemetry: SYSTEM-integrity child in a user desktop session | 🔴 HIGH |
| Anomalous privilege elevation (medium/low → SYSTEM) not attributable to a known service or scheduled task | EDR privilege-transition signals | 🔴 HIGH |
| `.vhd(x)` / ISO mounted from a user context immediately before Defender scan activity | Disk image mount events (VDS / `vhdmp`) from non-admin process | 🟡 MEDIUM |

### MITRE ATT&CK Mapping

| Technique | ID |
|---|---|
| Exploitation for Privilege Escalation | T1068 |
| Abuse Elevation Control Mechanism | T1548 |
| Hide Artifacts: NTFS File Attributes (junction/reparse manipulation) | T1564.004 |

---

## Mitigations

> ✅ **PATCHED (2026-07-09).** The primary control is now the vendor fix: ensure Microsoft Defender is running **Malware Protection Engine ≥ 1.1.26060.3008** — this auto-deploys with definition updates but should be *verified* on managed/air-gapped estates where definition delivery may lag. The compensating controls below remain valuable defense-in-depth for the series' behavioral class and for any estate that cannot immediately confirm engine currency.

| Control | Priority | Notes |
|---|---|---|
| **Application allowlisting (e.g., AppLocker / WDAC / ThreatLocker)** | 🔴 IMMEDIATE | ThreatLocker states allowlisting prevents the exploit binary from executing — the highest-value single control reported for RoguePlanet. |
| **Restrict execution from user-writable directories** | 🔴 HIGH | Block unsigned `.exe` from `%TEMP%`, Downloads, Pictures — interrupts staging used by this researcher's tooling. |
| **Restrict / monitor disk-image mounting by standard users** | 🔴 HIGH | The PoC depends on standard-user ISO/`.vhd(x)` mounting (which is why it fails on Server). Group Policy can restrict mounting; removable-storage / disk-image mount events make a useful tripwire. |
| **Supplement Defender with independent EDR / network visibility** | 🔴 HIGH | This series specifically targets Defender. A second detection layer and network-layer telemetry maintain coverage when the endpoint AV is the thing under attack. |
| **Least-privilege enforcement** | 🟡 HIGH | RoguePlanet starts from a standard-user context; reducing standing local accounts reduces blast radius. |
| **Verify Defender engine ≥ 1.1.26060.3008** | 🔴 IMMEDIATE | The fix ships as a Defender Malware Protection Engine update (CVE-2026-50656). Confirm engine currency across managed/air-gapped estates rather than assuming auto-deploy landed. |
| **Monitor CISA KEV** | 🟠 WATCH | CVE now assigned → KEV-eligible; not listed as of catalog 2026.07.07. A future KEV addition would impose a BOD 22-01 federal deadline. |

---

## Threat Context

**A&D target-profile relevance: HIGH (defensive).** Microsoft Defender is the default, ubiquitous endpoint protection across the aerospace & defense industrial base — primes, Tier-1/2 suppliers, and program enclaves alike. A standard-user-to-SYSTEM escalation that works on **fully patched** Windows 10/11 is a **ransomware and lateral-movement pre-cursor primitive**: it bridges "attacker has a low-privileged foothold (phishing, stolen VPN credential)" to "attacker has SYSTEM," which is the on-ramp to credential harvesting, lateral movement, and domain compromise. This is the same framing applied to BlueHammer and RedSun, and it holds here.

The previously-aggravating **no-CVE / no-patch** posture is now **resolved.** As of 2026-07-09 Microsoft has assigned **CVE-2026-50656** and shipped the fix out-of-band via Defender engine update 1.1.26060.3008. The structural gap noted at disclosure (KEV-ineligibility for lack of a CVE, hence no BOD 22-01 mandate) is closed on the eligibility axis: RoguePlanet is now KEV-*eligible*, though CISA had not listed it as of catalog 2026.07.07. Because the fix rides Defender's auto-deploying engine channel rather than a Windows KB, most estates converge automatically — but managed/air-gapped enclaves where definition delivery is throttled should verify engine currency explicitly.

In-the-wild exploitation of RoguePlanet **specifically** is not confirmed as of 2026-06-10. However, the same researcher's earlier tools (BlueHammer, RedSun, UnDefend) were confirmed exploited in live attack chains by Huntress, with Russian-geolocated infrastructure observed using the Defender zero-days. The series' historical pattern — public PoC, followed by threat-actor pickup within days — makes RoguePlanet a credible near-term escalation primitive for the A&D defender to plan against now, not after exploitation is confirmed.

> First-party note: no Archimedes first-party telemetry (`defenseclaw_local` / `archimedes`) currently corroborates or contradicts the external exploitation reporting for this series. The "not confirmed ITW for RoguePlanet" status reflects open-source reporting only.

---

## Related Vulnerabilities — Nightmare Eclipse Series

RoguePlanet is the 7th drop in the Nightmare Eclipse / Chaotic Eclipse series. Sibling dossiers:

| Tool | Disclosed | Type | CVE | Patch | Dossier |
|---|---|---|---|---|---|
| BlueHammer | Apr 3, 2026 | LPE → SYSTEM (file read) | CVE-2026-33825 | ✅ Patched (Apr 14) | [BLUEHAMMER](../BLUEHAMMER/profile.md) |
| RedSun | Apr 16, 2026 | LPE → SYSTEM (file write) | CVE-2026-41091 | ✅ Patched (May 20/21) | [REDSUN](../REDSUN/profile.md) |
| UnDefend | Apr 16, 2026 | Defender DoS / update block | CVE-2026-45498 | ✅ Patched (May 20/21) | [UNDEFEND](../UNDEFEND/profile.md) |
| YellowKey | May 12, 2026 | BitLocker bypass | CVE-2026-45585 | ✅ Patched (June PT) | [YELLOWKEY](../YELLOWKEY/profile.md) |
| GreenPlasma | May 12, 2026 | EoP (CTFMON section) | CVE-2026-45586 | ✅ Patched (June PT) | [GREENPLASMA](../GREENPLASMA/profile.md) |
| MiniPlasma | May 14, 2026 | LPE → SYSTEM (`cldflt.sys`, CVE-2020-17103 regression) | CVE-2020-17103 | ✅ Patched (June PT) | [MiniPlasma](../MiniPlasma/profile.md) |
| **RoguePlanet** | **Jun 9–10, 2026** | **LPE → SYSTEM (Defender TOCTOU / junction; ex-RCE)** | **CVE-2026-50656** | **✅ Patched (OOB engine 1.1.26060.3008, 2026-07-09)** | *(this dossier)* |

> **Series-closed confirmation (2026-07-09):** With RoguePlanet patched out-of-band (CVE-2026-50656, Defender engine 1.1.26060.3008), **the Nightmare Eclipse / Chaotic Eclipse series is fully closed** — all seven tools now carry a CVE and a fix. Prior state (2026-06-10): June 2026 Patch Tuesday had fixed GreenPlasma (CVE-2026-45586), YellowKey (CVE-2026-45585), and MiniPlasma (CVE-2020-17103 regression); RedSun (CVE-2026-41091) and UnDefend (CVE-2026-45498) were patched 2026-05-20/21. RoguePlanet was the last open tool; it is now closed.

The researcher's published threat at YellowKey/GreenPlasma disclosure — *"Next patch tuesday will have a big surprise for you Microsoft"* — is fulfilled by RoguePlanet, dropped hours after the June fixes shipped.

---

## Disclosure Timeline

| Date | Event | Source |
|---|---|---|
| Early Apr 2026 | Series begins (BlueHammer); ongoing Nightmare Eclipse vs MSRC / bug-bounty dispute | (series history) |
| Mid-May 2026 | Microsoft silently hardens Defender internal file I/O (reported `mpengine!SysIO*`), blocking RoguePlanet's original remote/junction RCE vector | BleepingComputer (researcher claim) |
| ~Late May 2026 | Researcher restores prototype after Microsoft updates initially broke it; reworked as LPE | SecurityAffairs (researcher claim) |
| Jun 9–10, 2026 | **Microsoft June Patch Tuesday** — fixes GreenPlasma (CVE-2026-45586), YellowKey (CVE-2026-45585), and MiniPlasma (CVE-2020-17103 regression); **does NOT fix RoguePlanet** | The Hacker News / BleepingComputer |
| Jun 9–10, 2026 | **RoguePlanet PoC released publicly**, hours after Patch Tuesday ("big surprise"). GitHub/GitLab repos removed by Microsoft; researcher self-hosts on `projectnightcrawler.dev` | BleepingComputer / THN |
| Jun 9–10, 2026 | ThreatLocker independently reproduces, confirms viability on patched Windows 11; notes application allowlisting blocks execution | BleepingComputer |
| Jun 2026 | Microsoft public posture: condemns uncoordinated disclosures as putting customers at risk, but states it will **not** pursue researchers conducting/publishing security research; reserves action for malicious harm (earlier DCU threat walked back) | THN / SecurityAffairs |
| Jun 10, 2026 | Profile created. UNPATCHED. No CVE. PoC public. ITW not confirmed for RoguePlanet specifically | — |
| Jun 16, 2026 | **CVE-2026-50656 record published in NVD** (MSRC-assigned); CVSS 7.0 HIGH primary / 7.8 secondary, CWE-59 | [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-50656) / [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-50656) |
| **Jul 9, 2026** | **PATCHED out-of-band.** Microsoft ships Defender Malware Protection Engine update **1.1.26060.3008** and the CVE-2026-50656 assignment surfaces in reporting. **Nightmare Eclipse series fully closed.** KEV-eligible (CVE now exists) but not listed (CISA KEV 2026.07.07) | BleepingComputer (Sergiu Gatlan) / SecurityWeek (Eduard Kovacs) — relaying Microsoft |

---

## References

- [NVD — CVE-2026-50656](https://nvd.nist.gov/vuln/detail/CVE-2026-50656) — canonical record; CVSS 7.0 HIGH (primary) / 7.8 HIGH (Microsoft secondary), CWE-59, engine fix ≥ 1.1.26060.3008
- [MSRC — CVE-2026-50656 (Microsoft Malware Protection Engine EoP "RoguePlanet")](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-50656)
- [BleepingComputer — Microsoft patches RoguePlanet Defender zero-day (CVE-2026-50656)](https://www.bleepingcomputer.com/news/microsoft/microsoft-patches-rogueplanet-defender-zero-day-vulnerability/) — Sergiu Gatlan, 2026-07-09 (state-change relay)
- [BleepingComputer — Microsoft Defender "RoguePlanet" zero-day grants SYSTEM privileges](https://www.bleepingcomputer.com/news/microsoft/microsoft-defender-rogueplanet-zero-day-grants-system-privileges/)
- [The Hacker News — Microsoft Defender RoguePlanet zero-day](https://thehackernews.com/2026/06/microsoft-defender-rogueplanet-zero-day.html)
- [SecurityAffairs — Chaotic Eclipse unveils RoguePlanet exploit targeting fully patched Windows](https://securityaffairs.com/193436/security/chaotic-eclipse-unveils-rogueplanet-exploit-targeting-fully-patched-windows.html)
- [CybersecurityNews — Windows Defender 0-day exploit "RoguePlanet"](https://cybersecuritynews.com/windows-defender-0-day-exploit-rogueplanet/)

> The NVD record for CVE-2026-50656 references a public PoC repository. Per Hard Rule 3 that link is intentionally **not** reproduced here; PoC existence is tracked in the *Public PoC Status* section, not mirrored.

---

*Profile created: 2026-06-10 | Updated: 2026-07-09 (state change — CVE-2026-50656 assigned, patched OOB via Defender engine 1.1.26060.3008, series closed) | TLP: CLEAR | Tracking: factual curation only — no threat-box scoring (vuln-tracker scope).*
