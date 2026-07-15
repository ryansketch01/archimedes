# Threat Box — Pioneer Kitten

**Actor ID:** 029
**Target profile:** ad-prime-v1
**Scored:** 2026-07-14 by `actor-profiler`
**Approval:** auto-committed (MEDIUM overall — Hard Rule 5 gate did NOT fire)
**Overall Threat Level:** 🟡 MEDIUM (weighted 5.5/10)

See [profile.md](profile.md) for full actor context.

---

## Summary

Pioneer Kitten is assessed as an overall 🟡 **MEDIUM** threat to the Archimedes
target profile (`ad-prime-v1`), driven primarily by an **espionage category HIGH
(composite 8)** and amplified by an unusually broad non-floor profile across
disruptive, cyber-crime, and destructive. Its **VERSATILITY** — a dual-track
state-intelligence + commercial access-broker/ransomware-enabler model — not any
single ceiling score, is what lifts it to the top of the Iranian MEDIUM cluster.

### Per-category breakdown

| Category | Composite | Level |
|---|---|---|
| Espionage (35%) | 8/10 | 🔴 HIGH |
| Supply Chain (20%) | 3/10 | 🟢 LOW |
| Destructive (15%) | 4/10 | 🟢 LOW |
| Disruptive (15%) | 5/10 | 🟡 MEDIUM |
| Cyber-Crime (15%) | 5/10 | 🟡 MEDIUM |

**Calibration:** parity with Peach Sandstorm (#027, 5.5) reached by a different
path — Peach is Intent=5 Target-Specific espionage-dominant (composite 9) with
floors elsewhere; Pioneer Kitten is Intent=4 Ideology espionage (composite 8,
capped because no A&D prime is named) but broader. Above UNC1549 (5.4), APT34
(4.9), and the Iranian LOW cluster (Charming Kitten 4.45, CyberAv3ngers 4.2,
MuddyWater 4.15, Cavern Manticore 3.25). Pioneer Kitten is the **only roster
Iranian actor with a genuine cyber-crime/ransomware-enablement dimension.**

---

## Espionage

**Intent 4/5** (ideology-association) · **Capability 4/5** (significant) · **Composite: 8/10** · **🔴 HIGH**

### Why this Intent score

IRGC-aligned state actor whose state-intelligence track conducts high-volume
intrusions against US/allied targets "consistent with Iranian state intelligence
objectives" (AA24-241A) — ideologically/strategically-driven anti-Western state
targeting. Intent=4 minimum (1 A-grade source) met by AA24-241A, which names
"defense" among US victim sectors, corroborated by CrowdStrike (IRGC-aligned) and
MITRE (suspected nexus). **NOT elevated to 5 (Target-Specific):** no A-grade
source names a specific US A&D prime / DIB contractor — AA24-241A/MITRE name the
"defense" SECTOR and Dragos names the "aerospace" SECTOR generically. A&D
relevance is structural/sector-level. Parallels Handala (#014) and CyberAv3ngers
(#028), both held at Ideology=4.

**Sources:** AA24-241A, MITRE G0117, Dragos PARISITE

### Why this Capability score

Multi-year, multi-source-documented espionage with active use inside 24 months:
AA24-241A (sustained state-intelligence intrusions), FortiGuard IR (independent
~2-year CNI espionage campaign, May 2023→early 2025, novel custom backdoors),
Dragos (access/recon), MITRE (curation). Multiple A-grade sources + active use
within 24 months = Cap=5 (Significant); semi-custom novelty reduces final to 4.

**Sources:** AA24-241A, FortiGuard IR, Dragos PARISITE, MITRE G0117

### Modifiers

- **Willingness (-0):** no-constraints — Iran/IRGC, active sanctions + hostilities.
- **Novelty (-1):** semi-custom — blended: novel (now-identified) custom backdoors + public edge CVEs + commodity tunnelers.

### First-party Splunk

No first-party IOC hits at time of scoring. -90d sweep 0 hits, both indices live
(archimedes 1725, defenseclaw_local 6 events). Visibility-bounded null.

---

## Supply Chain

**Intent 2/5** (regional-association) · **Capability 1/5** (possible) · **Composite: 3/10** · **🟢 LOW**

### Why this Intent score

MO is DIRECT edge-device compromise then access monetization — not a classic
supply-chain pivot (no compromised vendor build, no documented supplier-pivot to
reach a downstream A&D victim). The access-broker "supply chain of access" is
scored under cyber-crime/disruptive. Intent held at 2 (Regional).

**Sources:** AA24-241A, MITRE G0117

### Why this Capability score

Broad edge-exploitation gives FEASIBILITY of compromising a supplier's perimeter
and brokering that access, but no A-grade source documents a completed
supply-chain compromise reaching a downstream A&D victim. Cap=2 → 1 after novelty.

**Sources:** AA24-241A

### Modifiers

- **Willingness (-0):** no-constraints — Iran/IRGC.
- **Novelty (-1):** semi-custom — identified edge-exploitation + commodity toolkit.

### First-party Splunk

No first-party IOC hits at time of scoring.

---

## Destructive

**Intent 3/5** (sector-association) · **Capability 1/5** (possible) · **Composite: 4/10** · **🟢 LOW**

### Why this Intent score

FortiGuard IR assesses the actor "may have been positioning themselves to carry
out a future destructive attack" against the Middle East CNI victim — a
documented but **HEDGED** destructive-prepositioning signal at the critical-infra
sector level (Intent=3). Per Hard Rule 2 the hedge is preserved (suspected/
assessed, not confirmed). The prepositioning was against ME CNI, not a US A&D
prime; scored Sector Association reflecting the pattern's structural extension to
the OT/critical-infra footprint an A&D prime runs.

**Sources:** FortiGuard IR

### Why this Capability score

**No CONFIRMED destructive/wiper event** in any A-grade source. FortiGuard reports
SUSPECTED prepositioning only; Dragos explicitly states PARISITE has no observed
ICS destructive capability; Pay2Key (2020) was extortion, not a wiper. Persistent
access provides feasibility, but demonstrated destructive capability is absent.
Cap=2 → 1 after novelty. This deliberately does NOT harden the FortiGuard hedge.

**Sources:** FortiGuard IR, Dragos PARISITE

### Modifiers

- **Willingness (-0):** no-constraints — Iran/IRGC.
- **Novelty (-1):** semi-custom — no confirmed wiper tooling to assess; rests on identified backdoors + access.

### First-party Splunk

No first-party IOC hits at time of scoring.

---

## Disruptive

**Intent 3/5** (sector-association) · **Capability 2/5** (limited) · **Composite: 5/10** · **🟡 MEDIUM**

### Why this Intent score

The ransomware-enabler track predictably produces availability denial — affiliates
(NoEscape/RansomHouse/ALPHV) encrypt victim environments (T1486); the actor
historically ran Pay2Key (2020). AA24-241A names "defense" among US sectors hit by
this enablement activity (Intent=3 minimum). Not elevated to 5 — availability
impact is a downstream consequence of opportunistic access monetization.

**Sources:** AA24-241A, MITRE G0117

### Why this Capability score

Availability impact is documented but the DIRECT encryption is executed by
affiliates with Pioneer Kitten as access enabler; the actor's own direct
disruptive campaign (Pay2Key) is dated. Cap=3 (Limited) → 2 after novelty.
Conservative to avoid double-counting the ransomware model's financial dimension
(scored under cyber-crime).

**Sources:** AA24-241A, MITRE G0117

### Modifiers

- **Willingness (-0):** no-constraints — Iran/IRGC.
- **Novelty (-1):** semi-custom — commodity affiliate RaaS + semi-custom access-generation; weighted toward the specialized access capability.

### First-party Splunk

No first-party IOC hits at time of scoring.

---

## Cyber-Crime

**Intent 3/5** (sector-association) · **Capability 2/5** (credible) · **Composite: 5/10** · **🟡 MEDIUM**

### Why this Intent score

Pioneer Kitten's DISTINCTIVE feature vs every other Iranian roster actor: a
commercial financially-motivated track selling access via Br0k3r/xplfinder and
collaborating with ransomware affiliates for a **share of ransom proceeds**
(AA24-241A). Per the ransomware disambiguation, extortion-for-profit scores here.
AA24-241A places this activity within the US "defense" sector (Intent=3 minimum).
Not elevated to 5 — opportunistic monetization, no A&D prime named.

**Sources:** AA24-241A, MITRE G0117

### Why this Capability score

Well-documented: Br0k3r marketplace operation, direct collaboration with three
named affiliate programs (NoEscape, RansomHouse, ALPHV/BlackCat), historical
Pay2Key. AA24-241A is a dedicated US-gov advisory documenting exactly this with
active use in 2024. Cap=4 (Credible — one extensively documented A-grade body +
MITRE corroboration; NOT Cap=5 as it rests substantially on the single AA24-241A
primary). **Commodity novelty (-2)** reduces final to 2 — affiliate RaaS + public
exploits are off-the-shelf with mature detection signatures.

**Sources:** AA24-241A, MITRE G0117

### Modifiers

- **Willingness (-0):** no-constraints — Iran/IRGC criminal-freelancing track.
- **Novelty (-2):** commodity — commodity RaaS affiliate programs + public edge exploits.

### First-party Splunk

No first-party IOC hits at time of scoring.

---

## Review policy

- **Interval:** 90 days
- **Last reviewed:** 2026-07-14
- **Next review due:** 2026-10-12
- **Early review triggers:**
  - New attribution from A-grade source
  - New tooling documented
  - CVE exploitation linked to actor
  - Major campaign disclosure
  - First-party IOC observation
  - **Named US A&D-prime / DIB victim** (would lift espionage Intent toward Target-Specific)
  - **Confirmed destructive / wiper event** (would lift Destructive Capability vs current suspected prepositioning)
  - **AA24-241A or FortiGuard IOC appendix retrieved** (loads pending network IOCs; re-run Splunk sweep)

---

## Methodology note

Scored per `doctrine/THREAT-BOX-METHODOLOGY.md` (Piazza SANS framework adapted for A&D).
Target profile: `ad-prime-v1` (mid-to-large US A&D contractor, ITAR-regulated, DoD contracts).

**Confidence A2** — single originating US-gov primary (AA24-241A) on the
ransomware-enablement + network IOC appendix (both pending direct retrieval);
identity attribution and espionage/edge-exploitation capability are corroborated
across multiple independent bodies (US-gov + MITRE + Dragos + FortiGuard). No
single-source veto on core facts; single-primary caveat applied to the
ransomware-affiliate detail and the pending IOC appendix.

---

*Generated from `threat-box.yaml`. To update, re-run `threat-box-scoring` skill and regenerate.*
