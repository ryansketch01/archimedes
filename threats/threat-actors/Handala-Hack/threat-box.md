# Threat Box — Handala Hack

**Actor ID:** 014
**Target profile:** ad-prime-v1
**Scored:** 2026-07-12 by `actor-profiler`
**Approval:** auto-committed (MEDIUM — Hard Rule 5 gate did not fire; #actor-review notification per authority table)
**Overall Threat Level:** 🟡 MEDIUM (weighted 5.45/10)
**Primary threat vector:** Destructive (category 🔴 HIGH, composite 9)

---

## Summary

Handala Hack (a persona operated by Void Manticore; Iran / MOIS) is assessed as an overall 🟡 **MEDIUM** threat to the Archimedes target profile (ad-prime-v1) — but its risk is **concentrated in Destruction, where it scores a per-category 🔴 HIGH (composite 9)**. This is a genuinely top-tier destructive actor: a custom wiper arsenal (BiBi for Windows and Linux, Cl Wiper via the ElRawDisk driver, a partition-wiper family, the MBR-based Handala Wiper, a PowerShell wiper) plus a **demonstrated enterprise-scale mass-wipe** — the ~2026-03-11 abuse of Stryker's own Microsoft Intune MDM to remote-wipe 200,000+ devices across 79 countries.

The overall dilutes to MEDIUM because the four non-destructive categories are lower (Espionage MEDIUM, Disruptive MEDIUM, Supply Chain LOW, Cyber-Crime LOW) and the doctrine weighting caps Destructive at 15%. **This is the same pattern seen with UNC1549** (espionage composite 10 / overall MEDIUM): a maximal per-category score can sit inside a MEDIUM weighted overall. **Do not read MEDIUM as "not dangerous"** — the Destructive composite 9 is the operative number for defensive prioritization.

**Single-origin caveat (the big one):** Check Point Research is the sole originating A-grade primary for the persona attribution and MOIS affiliation. The Hacker News is a pure relay; MITRE G1055 is a structured second MOIS statement whose independence-vs-CPR-derivation is unadjudicated; Microsoft's own Storm-0842/DEV-0842 primary is pending direct retrieval. The destructive *capability* facts are more broadly corroborated (BiBi is widely documented, MITRE lists the cluster tooling, and the Stryker incident drew Krebs plus multiple relays) — so the single-origin caveat weighs most on the *attribution*, less on the destructive *capability*.

### Per-category breakdown

| Category | Intent | Capability | Composite | Level |
|---|---|---|---|---|
| Espionage (35%) | 4 (ideology) | 3 | 7/10 | 🟡 MEDIUM |
| Supply Chain (20%) | 2 (regional) | 1 | 3/10 | 🟢 LOW |
| **Destructive (15%)** | **4 (ideology)** | **5 (significant)** | **9/10** | **🔴 HIGH** |
| Disruptive (15%) | 3 (sector) | 2 | 5/10 | 🟡 MEDIUM |
| Cyber-Crime (15%) | 1 (opportunity) | 1 | 2/10 | 🟢 LOW |

**A&D-nexus / Intent discipline:** No A&D prime is named a victim in any retrieved source. A&D relevance is INDIRECT/STRUCTURAL — the Intune/MDM mass-wipe TTP is portable to any large ITAR enterprise, and the hack-and-leak posture would apply to a defense supplier. Per the evidence-minimum table and the explicit build directive, **portability and extrapolation do NOT lift Intent to Target-Specific (5)**. Intent is therefore held at **Ideology Association (4)** on the actor's two defining vectors (Destructive, Espionage) — supported by CPR's documentation of the anti-Israel/anti-Western ideological posture — and lower on the secondary vectors.

---

## Destructive — the primary vector

**Intent 4/5** (ideology-association) · **Capability 5/5** (significant) · **Novelty -0** (custom/advanced) · **Composite: 9/10** · **🔴 HIGH**

### Why this Intent score

Destruction is the actor's defining behavior and is explicitly ideologically driven — anti-Israel destructive wiper campaigns post-October 2023 (Karma/BiBi) and anti-MEK destruction against Albania (Homeland Justice, 2022–2024). The 2026 Stryker Intune mass-wipe proves willingness to destroy at scale against a US enterprise. Intent=5 (Target-Specific) is barred (no A&D prime named); Intent=4 (Ideology Association) is strongly supported by CPR (A-grade), with the Stryker case demonstrating the ideology extends to Western industry.

### Why this Capability score

The best-corroborated dimension. Custom wipers spanning Windows+Linux (BiBi), raw-disk (Cl Wiper/ElRawDisk), and partition/MBR (partition family, Handala Wiper), plus a **demonstrated** enterprise-scale mass-wipe (Stryker: 200k+ devices, 79 countries). Multiple trusted sources and active use within 24 months: BiBi is widely documented, MITRE G1055 independently lists the destructive cluster tooling (ROADSWEEP S1150, ZeroCleare S1151, RawDisk S0364), and the Stryker incident drew Krebs plus multiple relays. Cap=5 (Significant). The CPR single-origin caveat applies to the persona *attribution*, not to the destructive *capability*.

### Novelty

**-0 (Custom/Advanced).** Custom per-campaign wipers combined with genuine living-off-the-land destruction — the Intune legitimate-remote-wipe abuse turns the victim's own management plane into the weapon, needs no attacker infrastructure for the wipe, and looks like sanctioned administration. This is the hardest-to-defend tier.

**Sources:** CPR "Bad Karma, No Justice" (2024); CPR "Handala Hack — Unveiling Group's Modus Operandi" (2026); MITRE ATT&CK G1055.

---

## Espionage

**Intent 4/5** (ideology-association) · **Capability 4/5** (credible) · **Novelty -1** (semi-custom) · **Composite: 7/10** · **🟡 MEDIUM**

Hack-and-leak involves real data theft (confidentiality compromise) — 40+ claimed Israeli victims (2024–2026) and the Handala leak persona — driven by anti-Israel/anti-Western ideology (Intent=4, one A-grade source; parallels the Charming Kitten precedent). Capability is Credible (4), not Significant (5): the actor's own collection tradecraft is largely off-the-shelf/manual (reGeorge, NetBird, RDP), much of the stealthy exfiltration is performed by the collaborating actor Scarred Manticore (hand-off, not merge), and multiple-A corroboration is shaky (CPR sole originator; MITRE independence unadjudicated). Semi-custom novelty (-1) reduces final Capability to 3.

---

## Disruptive

**Intent 3/5** (sector-association) · **Capability 3/5** (limited) · **Novelty -1** (semi-custom) · **Composite: 5/10** · **🟡 MEDIUM**

Operational/reputational disruption is an aim of the hack-and-leak posture, and the Stryker wipe caused a massive multi-country outage. Intent held at 3 (not 4) to avoid inflating a vector that is largely a byproduct of the destruction. Per doctrine, a wiper-induced outage is scored under Destructive to avoid double-counting, so the standalone disruptive capability (DDoS/defacement without destruction) is thinner — Cap=3 (Limited), reduced to 2 by semi-custom novelty.

---

## Supply Chain

**Intent 2/5** (regional-association) · **Capability 2/5** (possible) · **Novelty -1** (semi-custom) · **Composite: 3/10** · **🟢 LOW**

The Stryker attack compromised Stryker's OWN Intune tenant (direct-tenant compromise); the propagation to 200k+ devices is scored as the destructive blast radius, not as a supplier-compromise-to-reach-target chain. No A&D-supplier-directed supply-chain campaign is documented. Per the directive, the MDM-abuse TTP's portability must NOT inflate Intent — held at Regional Association (2). The management-plane mass-propagation shows feasibility (Cap=2 Possible), reduced to 1 by semi-custom novelty.

---

## Cyber-Crime

**Intent 1/5** (target-of-opportunity) · **Capability 1/5** (not-capable) · **Composite: 2/10** · **🟢 LOW**

No financially-motivated intent. MOIS-directed state destruction under a hacktivist veneer. Where an encryptor appears (ROADSWEEP), it is destructive cover, not profit extortion — per doctrine, wiper-disguised-as-ransomware = Destructive, not Cyber-Crime. Floor.

---

## First-party Splunk

No first-party IOC hits at time of scoring. Sentinel run 2026-07-12: **0 hits over -90d on all 9 operator IPs** across `defenseclaw_local` and `archimedes`. Per Hard Rule 8, silent Splunk does not disconfirm — Frank is not an Israeli/Albanian/US-medical-tech victim matching the target profile. Visibility-bounded null; **no IOC corroboration bonus applied** to any category.

---

## Calibration

- Weighted overall **5.45 → MEDIUM**, just above **UNC1549** (5.4, MEDIUM) and in the neighborhood of **Peach Sandstorm** (5.5, MEDIUM).
- **Unique among the roster's Iran-MOIS actors** in carrying a per-category 🔴 HIGH **Destructive** score (composite 9) — the espionage-dominant peers (UNC1549, APT34, Charming Kitten, MuddyWater, Cavern Manticore) all floor or near-floor destruction. Peach Sandstorm is the only other Iranian actor with a non-floor destructive category, and at composite 4 it is well below Handala's 9.
- The MEDIUM overall is a weighting artifact, **not** a statement that the actor is low-risk. For a defender, the Destructive composite 9 governs.

---

## Review policy

- **Interval:** 90 days
- **Last reviewed:** 2026-07-12
- **Next review due:** 2026-10-10
- **Early review triggers:**
  - New attribution from an A-grade source
  - New tooling documented
  - CVE exploitation linked to actor
  - Major campaign disclosure
  - First-party IOC observation
  - **Independent second-IR-vendor corroboration** (Mandiant / CrowdStrike / Unit 42 / MSTIC) — would resolve the single-origin caveat
  - **Retrieval of Microsoft's Storm-0842/DEV-0842 primary**
  - **Direct retrieval of the CPR IOC appendix** — would recover verified wiper hashes
  - **A&D-prime-direct targeting disclosure** — would lift Intent above Ideology and could move overall to HIGH

---

## Methodology note

Scored per `doctrine/THREAT-BOX-METHODOLOGY.md` (Piazza SANS framework adapted for A&D).
Target profile: `ad-prime-v1` (mid-to-large US A&D contractor, ITAR-regulated, DoD contracts).

Single ORIGINATING primary (Check Point Research); persona attribution CPR-originated, destructive capability broadly corroborated. Hard Rule 2 preserved throughout — no Archimedes-originated attribution; Void Manticore <-> Scarred Manticore is a hand-off/collaboration, NOT a merge; related_actors are Iranian-MOIS analytic peers, not merges. Hard Rule 5 gate did NOT fire (MEDIUM). See [profile.md](./profile.md) for full actor context.

---

*Generated from `threat-box.yaml`. To update, re-run the `threat-box-scoring` skill and regenerate.*
