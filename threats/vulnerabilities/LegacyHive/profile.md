# LegacyHive — Windows User Profile Service Arbitrary-Hive-Load LPE Zero-Day

## Identity

| Field | Details |
|---|---|
| **Vulnerability Name** | LegacyHive |
| **CVE** | ⚪ **NONE assigned** as of 2026-07-15 (MSRC silent — no CVE, no CVSS, no advisory). KEV-ineligible for lack of a CVE (see *Threat Context*) |
| **CVSS** | ⚪ **None published** by any source |
| **CWE** | ⚪ None published. Class is consistent with a TOCTOU / time-of-check-to-time-of-use race (CWE-367 family) — noted for context only, not vendor-assigned |
| **Type** | Local Privilege Escalation (LPE) — standard user to another user's / an administrator's security context (→ SYSTEM/admin-adjacent) |
| **Class** | Arbitrary registry hive load via timed path-switching (TOCTOU-style race) against the Windows User Profile Service (`profsvc` / ProfSvc) |
| **Component** | Windows User Profile Service (`profsvc`) + the registry user-hive load path (`usrclass.dat` in the public PoC) |
| **Affected Platforms** | *Claimed* to affect all currently-supported Windows desktop and server, **including systems patched through July 2026 Patch Tuesday (2026-07-14)** — **CLAIMED / UNVERIFIED**; MSRC silent, no independent confirmation of the affected matrix |
| **Patch Status** | 🔴 **UNPATCHED zero-day** — no MSRC advisory, no CVE, no fix at dossier creation |
| **PoC Status** | 🔴 **PUBLIC but deliberately stripped-down** — the public version reportedly requires an additional standard-user credential plus a third username (which can be an admin account) and works only with `usrclass.dat`; the researcher claims the unpublished original needed no extra credentials. **Existence tracked only — NOT mirrored (Hard Rule 3)** |
| **Exploited in Wild** | ⚪ **None reported.** Analysts caution capable actors could reverse-engineer the withheld components |
| **Discovered By** | Nightmare Eclipse / Chaotic Eclipse / Dead Eclipse / MSNightmare / deadeclipse666 (pseudonymous researcher) — *self-attributed / press-asserted persona continuity* (Hard Rule 2; see *Attribution*) |
| **Public Disclosure** | ~2026-07-14 (uncoordinated — hours after July 2026 Patch Tuesday) |
| **Independent Assessment** | Matei Badanoiu — assessed as a genuine post-compromise primitive while disputing the "full system compromise" framing |
| **Series Position** | 8th public drop in the Nightmare Eclipse series — **REOPENS** the series (logged "fully closed" 2026-07-09 at RoguePlanet's patch) |
| **Admiralty Grade** | **B2** headline (operational / mechanism-plausibility layer). Layered: disclosure EVENT **B1** (independently observable public fact); mechanism-genuine **B2** (single-source veto → WEP "likely"); strong severity claims **B3** (single-claimant, disputed). See *Grading* |

---

## Overview

LegacyHive is the eighth public disclosure attributed to the pseudonymous Nightmare Eclipse persona, released on or about **2026-07-14 — hours after Microsoft's July Patch Tuesday**. It is a **local privilege escalation** claim against the Windows **User Profile Service** (`profsvc`): per reporting, the service can be induced via a carefully timed path-switch (a TOCTOU-style race) to mount **another user's registry hive — including an administrator's — into the attacker's own classes root**, yielding access to a higher-privileged user's context from a standard-user starting point.

Everything substantive here is **reported / claimed**, not confirmed. Eight-plus outlets covered the drop (The Register and The Hacker News as primary relays; Cybernews, SecurityOnline, CybersecurityNews, Cyderes, Cryptika, and OffSeq behind them), but every one traces back to a **single originating evidence basis** — the researcher's own stripped-down PoC and self-hosted blog. **Microsoft/MSRC was contacted and stayed silent: no CVE, no CVSS, no advisory, no patch.** Publisher-level breadth is not independent technical validation, so the operational claims carry a single-source veto (graded B2, WEP "likely").

The drop **fell short of the researcher's own hype**. A placeholder repository containing only a license and README reportedly appeared first, and the release did not match the "bone-shattering" mass drop the persona had promised for July 14. Independent researcher **Matei Badanoiu** assessed LegacyHive as a genuine post-compromise primitive but **disputed the full-system-compromise framing**; The Register characterized it as **"not the haymaker promised."** The strongest claims — that it works on fully July-2026-patched systems and that the unpublished original required no credentials — are single-claimant and actively disputed (graded B3).

For an A&D contractor the operational shape is familiar and dangerous regardless of the hype dispute: a **standard-user-to-elevated-context LPE on the ubiquitous Windows endpoint estate** is a ransomware and lateral-movement pre-cursor primitive — the bridge from a low-privileged foothold (phishing, a stolen VPN credential) to a privileged context. The posture is **aggravated by the absence of a CVE and a patch**: with no CVE, LegacyHive is CISA-KEV-ineligible, so there is no BOD 22-01 federal notification mechanism — the same structural gap previously flagged for RedSun, UnDefend, and RoguePlanet before their CVEs were assigned.

---

## Attribution

> **Hard Rule 2 — Archimedes does not originate attribution.** The Nightmare Eclipse identity and the continuity of LegacyHive to the prior series are the **researcher's own self-claim**, press-asserted by the relaying outlets and reported here strictly as such. Persona continuity to the prior drops is consistent with the established pattern but remains self-attributed, not Archimedes-originated. **No `_roster.yaml` actor is attributed** — Nightmare Eclipse is a tracked persona/series, not a formal roster actor. `related_actors: []`.

---

## Technical Analysis

> **Defensive framing only.** This section describes the vulnerability class, the subsystem involved, and the telemetry a defender can watch for. It contains **no exploit code, no PoC, no payloads, and no step-by-step exploitation instructions** (Hard Rule 3). The public PoC exists but is **not** fetched, mirrored, or reproduced.

### Vulnerability Class (as reported)

LegacyHive is described as an **arbitrary registry hive-load** privilege escalation driven by a **timed path-switch** — a time-of-check-to-time-of-use (TOCTOU) race — against the **User Profile Service**. The service is the Windows component responsible for loading and unloading user registry hives (e.g., the per-user `usrclass.dat` classes hive) during profile operations. The reported flaw is that the path the service resolves when it goes to load a hive can be swapped underneath it, so the service is induced to **mount a different user's hive** — potentially an administrator's — into a location the attacker controls (their own classes root).

This is a coherent, historically-precedented Windows `profsvc` bug class (arbitrary-hive-load / profile-service race conditions have produced real Windows LPEs before), and it is consistent with the persona's prior drops, which repeatedly abused **legitimate Windows components interacting in a sequence Windows does not defend against** rather than memory corruption. That coherence is what lifts the mechanism layer to grade 2 (plausible); it is **not** independent proof the primitive works as claimed.

### Why Standard Memory-Safety Mitigations Do Not Apply

Because the reported mechanism abuses a **legitimate service's file/registry-path handling and a race window** rather than corrupting memory, kernel-level exploit mitigations (CFG, hardware-enforced stack protection, Exploit Guard) offer no protection against this class. The defensive levers are **behavioral detection** of anomalous hive-load / path-switch activity, application allowlisting, and reducing the standing population of accounts that can run the trigger.

### Severity Claims — Held at Arm's Length (B3)

The following are **single-claimant and disputed**, and no strong predictive claim is made on them:

- Works on **all currently-supported Windows desktop/server including fully July-2026-patched systems** — *claimed, MSRC-unconfirmed*.
- Yields **full system compromise** — *disputed by Badanoiu, who framed it as a post-compromise primitive, not full compromise*.
- The **unpublished original required no extra credentials** and handled multiple hive types — *unverifiable; the public PoC is deliberately degraded (needs an extra standard-user credential + a third username, `usrclass.dat` only)*.

---

## Affected Systems

| Platform | Status | Notes |
|---|---|---|
| Windows 10 / 11 (desktop, all currently-supported) | ⚠️ **Claimed vulnerable** | Per reporting, incl. systems patched through July 2026 Patch Tuesday (2026-07-14). CLAIMED / UNVERIFIED — MSRC silent |
| Windows Server (all currently-supported) | ⚠️ **Claimed vulnerable** | Same claim; no independent confirmation of the affected matrix |

**Reported prerequisites (public PoC):** a standard-user starting context, an **additional standard-user credential**, and a **third username** (which can be an administrator account); the public PoC works only with `usrclass.dat`. The researcher claims the unpublished original needed **no** extra credentials — unverifiable.

> The entire affected-versions matrix is a **single-claimant assertion**. Microsoft has published no advisory, CVE, CVSS, or affected-build list. Treat "works on fully-patched July-2026 systems" as a claim to watch, not an established fact.

---

## Public PoC Status

| Location | Status | Notes |
|---|---|---|
| Placeholder repo (license + README only) | Appeared first | Reportedly published on the drop date ahead of the PoC itself |
| Self-hosted PoC repo (researcher infrastructure) | Public — deliberately stripped | 9th public repo in the series (some repos are placeholders); requires an extra standard-user credential + a third username; `usrclass.dat` only |
| Self-hosted blog (researcher infrastructure) | Public | Disclosure announcement / write-up |

> Per Hard Rule 3, the PoC is **not** mirrored, summarized at an actionable level, or fetched. Only its **existence, hosting posture, and the degraded-vs-original distinction** are tracked. Researcher-controlled publishing/identity infrastructure is recorded under *IOCs & Detection* as **identity indicators, not block-list IOCs**.

---

## IOCs & Detection

No malicious atomic IOCs exist for LegacyHive — it is a **PoC disclosure, not an intrusion campaign**. There is no CVE, no CVSS, no file hash, no attacker C2, and no victim infrastructure. Detection is **behavioral / hunt-hypothesis** only. First-party Splunk sweep (`defenseclaw_local` / `archimedes`, -30d, for the researcher publishing domains + "LegacyHive") returned **0 events** — silent, not disconfirming.

### Persona / Identity Indicators (NOT for blocking — attribution tracking only)

```yaml
persona_identity_indicators:
  - type: domain
    value: projectnightcrawler.dev        # researcher self-hosted blog; NOT C2
  - type: domain
    value: git.projectnightcrawler.dev     # self-hosted PoC repo host; EXISTENCE ONLY, not fetched (Hard Rule 3)
  - type: domain
    value: deadeclipse666.blogspot.com     # legacy persona publishing channel
  - type: account_handle
    value: github.com/MSNightmare          # historical persona account handle (repeatedly removed)
network_iocs: []
file_iocs: []
first_party_hits: none                     # Splunk -30d sweep of the above + "LegacyHive" = 0 events
```

### Behavioral Indicators (hunt hypotheses — inferred from the reported mechanism, pending validation against a controlled sample)

| Behavior | Telemetry | Confidence |
|---|---|---|
| Registry hive load (`RegLoadKey` / `NtLoadKey`) mounting **another user's** hive into a standard user's classes root, not attributable to a known service | Registry-load audit / EDR registry telemetry | 🟡 MEDIUM |
| Anomalous **User Profile Service (`ProfSvc`)** hive-load activity where the resolved target path was swapped mid-operation (junction / reparse on a profile directory path) | File-system minifilter / EDR reparse-point creation correlated with `ProfSvc`/`svchost` profile activity | 🟡 MEDIUM |
| Access to a **`usrclass.dat`** belonging to a different user from a standard-user process | File/registry access telemetry on `...\AppData\Local\Microsoft\Windows\UsrClass.dat` | 🟡 MEDIUM |
| Standard/low-integrity process obtaining a token or resource in **another user's / an administrator's context** shortly after profile-service activity | EDR privilege-transition / token telemetry | 🟡 MEDIUM |
| Junction / reparse point created by a non-system, medium/low-integrity process on a user-profile path, then targeted by a service operation | Reparse-point creation events (minifilter) | 🟡 MEDIUM |

### MITRE ATT&CK Mapping

| Technique | ID |
|---|---|
| Exploitation for Privilege Escalation | T1068 |
| Abuse Elevation Control Mechanism | T1548 |
| Modify Registry | T1112 |
| Hide Artifacts: NTFS File Attributes (junction / reparse manipulation) | T1564.004 |

---

## Mitigations

> 🔴 **UNPATCHED.** There is no vendor fix, CVE, or advisory to apply. The controls below are **compensating / defense-in-depth** for the reported class and for the broader Nightmare Eclipse LPE pattern. Re-evaluate the moment an MSRC advisory, CVE, or Patch Tuesday fix lands.

| Control | Priority | Notes |
|---|---|---|
| **Application allowlisting (AppLocker / WDAC / ThreatLocker)** | 🔴 IMMEDIATE | Highest-value single control across this researcher's series — prevents an unsigned exploit binary from executing. Reported to block prior siblings (RoguePlanet). |
| **Least-privilege enforcement / reduce standing local accounts** | 🔴 HIGH | LegacyHive starts from a standard-user context and (public PoC) needs additional local credentials — shrinking the standing account population reduces both blast radius and trigger availability. |
| **Behavioral EDR (TTP-based), not signature-only** | 🔴 HIGH | No hashes/signatures exist. Detection must key on the behavioral hive-load / path-switch pattern above, not a static indicator. |
| **Restrict execution from user-writable directories** | 🟠 HIGH | Block unsigned `.exe` from `%TEMP%`, Downloads, etc. — interrupts staging common to this researcher's tooling. |
| **Monitor anomalous registry hive-load + profile-service activity** | 🟠 HIGH | Instrument `RegLoadKey`/`NtLoadKey` and `ProfSvc` hive mounts as a tripwire (see *Behavioral Indicators*). |
| **Watch for a CVE / MSRC advisory and patch on release** | 🟠 WATCH | No CVE → KEV-ineligible → no BOD 22-01 mandate. Patch prioritization must be driven manually until a CVE exists. |

---

## Threat Context

**A&D target-profile relevance: HIGH (structural).** The Windows endpoint estate is ubiquitous across the aerospace & defense industrial base — primes, Tier-1/2 suppliers, and program enclaves alike. A **standard-user-to-elevated-context LPE** is a **ransomware and lateral-movement pre-cursor primitive**: it bridges "attacker has a low-privileged foothold" to "attacker holds a privileged context," which is the on-ramp to credential harvesting, lateral movement, and domain compromise. This is the same framing applied to BlueHammer, RedSun, and RoguePlanet, and it holds here.

The rating is HIGH on the same structural basis as those siblings — **but qualified**: LegacyHive's severity is **single-claimant and disputed**, its public PoC is **deliberately degraded** (requires an extra standard-user credential), and there is **no in-the-wild exploitation**. There is **no named A&D victim** and no A&D-specific victimology; relevance is structural, not campaign-driven. If a CVE is assigned, in-the-wild exploitation emerges, or an independent weaponized / no-credentials PoC surfaces, the rating and priority escalate.

The posture is **aggravated by the no-CVE / no-patch state**: without a CVE, LegacyHive is **CISA-KEV-ineligible**, so there is no BOD 22-01 federal deadline and no ecosystem notification mechanism — the same structural gap flagged for RedSun, UnDefend, and RoguePlanet before their CVEs were assigned. Patch prioritization must be driven manually.

> **First-party note:** No Archimedes first-party telemetry (`defenseclaw_local` / `archimedes`) corroborates or contradicts the reporting. A -30d sweep for the researcher publishing domains and "LegacyHive" returned 0 events (silent, not disconfirming). No malicious atomic IOC exists to hunt.

---

## Grading

| Layer | Claim | Digraph | WEP |
|---|---|---|---|
| **1 — Disclosure event** | A new `profsvc` LPE PoC ("LegacyHive") was publicly disclosed ~2026-07-14 by Nightmare Eclipse; repo + blog exist; 8+ outlets report it; MSRC contacted-and-silent | **B1** | very_likely |
| **2 — Genuine primitive** | LegacyHive is a genuine, functioning LPE primitive (profsvc induced to mount another user's hive) | **B2** | likely |
| **3 — Severity** | Reliably achieves full system compromise on ALL supported Windows incl. fully July-2026-patched; original needed no creds | **B3** | roughly_even_chance |

**Headline B2** (operational / mechanism-plausibility layer). **Single-source veto applied** to the operational and severity layers: remove the researcher's own PoC/blog and no outlet has an independent evidence basis. Badanoiu supplies a **partial** second basis on mechanism-plausibility only (not on severity). Relaying outlets (The Register, The Hacker News) are B-grade; all additional relays are publisher-independent but **not** evidence-basis-independent.

---

## Related Vulnerabilities — Nightmare Eclipse Series

LegacyHive is the **8th public drop** in the Nightmare Eclipse / Chaotic Eclipse series and **reopens** a series that was logged **"fully closed" on 2026-07-09** when RoguePlanet was patched. The prior seven all resolved into real, vendor-patched Windows LPE CVEs — a 7-of-7 track record that underpins the mechanism-plausibility (grade-2) assessment.

| Tool | Disclosed | Type | CVE | Patch | Dossier |
|---|---|---|---|---|---|
| BlueHammer | Apr 3, 2026 | LPE → SYSTEM | CVE-2026-33825 | ✅ Patched (Apr 14) | [BLUEHAMMER](../BLUEHAMMER/profile.md) |
| RedSun | Apr 16, 2026 | LPE → SYSTEM (file write) | CVE-2026-41091 | ✅ Patched (May 20/21) | [REDSUN](../REDSUN/profile.md) |
| UnDefend | Apr 16, 2026 | Defender DoS / update block | CVE-2026-45498 | ✅ Patched (May 20/21) | [UNDEFEND](../UNDEFEND/profile.md) |
| YellowKey | May 12, 2026 | BitLocker bypass | CVE-2026-45585 | ✅ Patched (June PT) | [YELLOWKEY](../YELLOWKEY/profile.md) |
| GreenPlasma | May 12, 2026 | EoP (CTFMON section) | CVE-2026-45586 | ✅ Patched (June PT) | [GREENPLASMA](../GREENPLASMA/profile.md) |
| MiniPlasma | May 14, 2026 | LPE → SYSTEM (`cldflt.sys`) | CVE-2020-17103 | ✅ Patched (June PT) | [MiniPlasma](../MiniPlasma/profile.md) |
| RoguePlanet | Jun 9–10, 2026 | LPE → SYSTEM (Defender TOCTOU / junction) | CVE-2026-50656 | ✅ Patched (OOB engine, Jul 9) | [RoguePlanet](../RoguePlanet/profile.md) |
| **LegacyHive** | **~Jul 14, 2026** | **LPE — profsvc arbitrary hive load (TOCTOU path-switch)** | ⚪ **NONE** | 🔴 **UNPATCHED** | *(this dossier)* |

> **Series reopened (2026-07-15).** The prior seven-tool CVE series was logged fully closed at RoguePlanet's 2026-07-09 patch. LegacyHive is a **new, post-closure drop** — do NOT re-report it as one of the closed set. It is **not** the previously-watched 8th-drop candidate (a promised **Defender memory-corruption batch**), which remains unreleased, and it is **not** BitSkrieg (Secure Boot / BitLocker, co-claimed with JonasLyk) — both of those remain **open standing watch signals**. GreatXML (June BitLocker/WinRE bypass) is a separate prior drop.

---

## Disclosure Timeline

| Date | Event | Source |
|---|---|---|
| 2026-07-09 | RoguePlanet patched (CVE-2026-50656, OOB Defender engine 1.1.26060.3008); Nightmare Eclipse 7-drop CVE series logged **fully closed** | (series history) |
| ~2026-07-14 | **July 2026 Patch Tuesday** ships | Microsoft |
| ~2026-07-14 | Placeholder repo (license + README only) reportedly appears first, ahead of the PoC | [The Register](https://www.theregister.com/security/2026/07/15/microsofts-serial-tormentor-drops-legacyhive-0-day/5271723) |
| ~2026-07-14 | **LegacyHive PoC dropped publicly** — unpatched `profsvc` arbitrary-hive-load LPE; deliberately stripped-down; falls short of the promised "bone-shattering" drop | The Register / [The Hacker News](https://thehackernews.com/2026/07/researcher-drops-new-windows-zero-day.html) |
| ~2026-07-15 | Microsoft/MSRC **contacted, silent** — no CVE, no CVSS, no advisory, no patch | The Register / The Hacker News |
| ~2026-07-15 | Matei Badanoiu assesses it as a genuine **post-compromise primitive** while disputing the full-compromise framing; The Register: **"not the haymaker promised"** | The Register |
| 2026-07-15 | Dossier created (VT-042). UNPATCHED. No CVE. PoC public (stripped). No ITW. Series reopened | — |

---

## References

- [The Register — Microsoft's serial tormentor drops LegacyHive 0-day](https://www.theregister.com/security/2026/07/15/microsofts-serial-tormentor-drops-legacyhive-0-day/5271723) — primary relay (B); disclosure event, MSRC-silent, "not the haymaker promised"
- [The Hacker News — Researcher drops new Windows zero-day](https://thehackernews.com/2026/07/researcher-drops-new-windows-zero-day.html) — corroborating relay (B); independently contacted Microsoft (no response); notes the public PoC is deliberately stripped
- Additional relays (publisher-independent, **not** evidence-basis-independent): Cybernews, SecurityOnline, CybersecurityNews, Cyderes (Howler Cell), Cryptika, OffSeq Threat Radar — all trace to the same originating claimant
- Source finding: [finding-2026-07-15-0002](../../findings/finding-2026-07-15-0002-nightmare-eclipse-legacyhive-windows-profsvc-lpe-zero-day-no-cve-vendor-silent-b2-single-source-veto-monitoring.md)

> No CVE/NVD record exists for LegacyHive as of 2026-07-15. Researcher self-hosted channels (blog.projectnightcrawler.dev, git.projectnightcrawler.dev, deadeclipse666.blogspot.com, github.com/MSNightmare) are recorded for **existence only** — not fetched, not linked as live PoC sources (Hard Rule 3).

---

*Profile created: 2026-07-15 | VT-042 | Series: Nightmare Eclipse / Chaotic Eclipse (8th drop — series reopened) | TLP: CLEAR | Tracking: factual curation only — no threat-box scoring (vuln-tracker scope). All substance is REPORTED / CLAIMED under single-source veto; attribution is researcher self-claim relayed by outlets (Hard Rule 2); no exploit detail (Hard Rule 3).*
