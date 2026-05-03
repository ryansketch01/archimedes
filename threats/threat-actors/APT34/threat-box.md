# Threat Box — APT34

**Actor ID:** 023
**Target profile:** ad-prime-v1 (mid-to-large US A&D contractor, ITAR-regulated)
**Scored:** 2026-05-01 by `actor-profiler`
**Approval:** auto-committed (overall weighted = MEDIUM; authority = actor-profiler-autonomous-with-notification)
**Overall Threat Level:** 🟡 MEDIUM (weighted 4.9/10)
**Primary threat vector:** Espionage — per-category composite **8/10 = 🔴 HIGH**

---

## Summary

APT34 is assessed as an **overall MEDIUM threat** to the Archimedes target profile (`ad-prime-v1`), driven entirely by its **espionage capability**. Public reporting (Mandiant, Unit 42, Trend Micro, Symantec, Cisco Talos) documents a decade of continuous, high-skill Iran-aligned espionage operations against Middle East government, telecom, energy, and finance. For a US A&D prime, direct targeting is not documented — APT34 risk is **second-order via supply-chain and regional partner compromise**, particularly through GCC defense ministries, MENA-region subsidiaries, and shared regional infrastructure.

The per-category **espionage composite of 8 (HIGH)** is the operationally relevant number for defenders. The weighted 4.9 reflects that APT34 has no documented destructive, disruptive, or cyber-crime activity — those four categories average down what is, in espionage terms, a top-tier actor.

### Per-category breakdown

| Category | Composite | Level |
|---|---|---|
| Espionage (35%) | 8/10 | 🔴 HIGH |
| Supply Chain (20%) | 6/10 | 🟡 MEDIUM |
| Destructive (15%) | 2/10 | 🟢 LOW |
| Disruptive (15%) | 2/10 | 🟢 LOW |
| Cyber-Crime (15%) | 2/10 | 🟢 LOW |

---

## Espionage

**Intent 3/5** (sector-association) · **Capability 5/5** (significant) · **Composite: 8/10** · **🔴 HIGH**

### Why this Intent score

APT34 is documented by Mandiant, Palo Alto Unit 42, Trend Micro, and Symantec as a sustained Iranian state-aligned espionage actor focused on Middle East government, telecommunications, energy, and finance, with documented A&D-adjacent targeting of regional defense ministries and aerospace research entities (notably Israeli targets per Mandiant Crambus 2023 reporting). Targeting of US A&D primes specifically is NOT documented in public reporting; A&D-prime exposure is sectoral and supply-chain-mediated rather than direct. Scored Intent=3 (sector-association) rather than 5 (target-specific) — the latter would require A-grade evidence of direct ad-prime-v1 targeting, which is absent.

**Sources:** mandiant-2017-apt34, unit-42-oilrig-2018, symantec-crambus-2023, trendmicro-menorah-2023

### Why this Capability score

Multiple A-grade sources document active espionage tradecraft within the last 24 months: Trend Micro and Unit 42 disclosed MENORAH C# backdoor against Saudi government targets in 2023-2024; Symantec documented an eight-month dwell-time intrusion (PowerExchange, compromised Exchange transport agent C2) in a Middle East government network in 2023. A decade of continuous tooling evolution (Helminth, ISMAgent, OopsIE, BONDUPDATER, RGDoor, DNSpionage/Karkoff, Saitama, SideTwist, MARLIN, MENORAH, PowerExchange). Capability against ad-prime-v1's technology stack (Windows, Exchange, IIS, Office) is significant in the abstract — what's lower is targeting interest, not capability.

**Sources:** trendmicro-menorah-2023, symantec-crambus-2023, unit-42-saitama-2022, cisco-talos-dnspionage-2019, mandiant-2017-apt34

### Modifiers

- **Willingness (-0):** no-constraints — Iran, sustained sanctions regime, no diplomatic constraints, active regional cyber confrontation through 2024-2025.
- **Novelty (-0):** custom-advanced — Custom-developed tooling per campaign (MENORAH, MARLIN, PowerExchange, SideTwist). DNS-tunneling C2 across multiple toolkits raises detection difficulty above commodity baseline. PowerExchange's use of compromised Exchange transport agents as covert C2 is novel living-off-the-land tradecraft against M365/Exchange-heavy environments.

### First-party Splunk

No first-party APT34 infrastructure observations in `defenseclaw_local` at time of initial scoring 2026-05-01.

---

## Supply Chain

**Intent 3/5** (sector-association) · **Capability 3/5** (credible, with -1 novelty) · **Composite: 6/10** · **🟡 MEDIUM**

### Why this Intent score

APT34 has documented use of compromised regional ministries and telecommunications providers as relays into partner networks (T1199 Trusted Relationship). For ad-prime-v1 specifically, this manifests as a credible supply-chain risk via: (1) joint ventures with GCC defense ministries, (2) MENA-region subsidiaries, (3) shared regional telecom or cloud infrastructure. The intent is not ad-prime-v1-specific (Intent=5 unsupported), but it does map to the broader A&D / defense-adjacent sector via partner compromise.

**Sources:** mandiant-2017-apt34, symantec-crambus-2023, unit-42-oilrig-2018

### Why this Capability score

Documented capability to compromise regional infrastructure and use it as relay (T1199). Multiple Mandiant and Unit 42 reports document intrusion sets pivoting through compromised regional partners. Capability is credible but not at the level of operators known for running large-scale supplier-chain compromise (e.g., APT41 hardware supply chain). Scored 4 (credible) rather than 5 (significant) because the supply-chain-into-ad-prime-v1 chain has not been documented end-to-end in public reporting. After -1 novelty modifier, final capability is 3.

**Sources:** mandiant-2017-apt34, symantec-crambus-2023

### Modifiers

- **Willingness (-0):** no-constraints — Iran, no constraints.
- **Novelty (-1):** semi-custom — Compromised-infrastructure-as-relay is moderate-skill tradecraft; not commodity, but not novel either.

### First-party Splunk

No first-party APT34 supply-chain-related observations as of 2026-05-01.

---

## Destructive

**Intent 1/5** (target-of-opportunity) · **Capability 1/5** (possible, with -1 novelty floored at 1) · **Composite: 2/10** · **🟢 LOW**

### Why this Intent score

APT34's mission profile is intelligence collection, not destructive operations. No documented APT34 deployment of wipers or destructive attacks against any target sector in public Mandiant, Unit 42, Symantec, or Trend Micro reporting. Destructive activity against ad-prime-v1 would be off-mission for this actor cluster; if destructive intent emerges from Iran, sister clusters (e.g., MOIS or IRGC operators with documented wiper history) are the more likely vector.

**Sources:** mandiant-2017-apt34, mitre-attack-g0049

### Why this Capability score

Feasibility-only assessment. APT34's existing access tradecraft (long dwell, privileged credential acquisition) could support a pivot to destructive action if tasked, but the group has no documented destructive tradecraft, no wiper malware in public reporting, and no indication this is in their toolkit.

### Modifiers

- **Willingness (-0):** no-constraints
- **Novelty (-1):** semi-custom — Hypothetical destructive action would likely use existing access rather than novel destructive tooling.

### First-party Splunk

No first-party APT34 observations.

---

## Disruptive

**Intent 1/5** (target-of-opportunity) · **Capability 1/5** (possible, with -1 novelty floored at 1) · **Composite: 2/10** · **🟢 LOW**

### Why this Intent score

APT34 has no documented availability-attack history. The group's operational signature is long-dwell intelligence collection, which is the opposite of disruption — operators preserve target uptime and detection blindness rather than disrupt it. No documented DDoS, ransomware, or service-disruption operations attributable to APT34 in public reporting.

**Sources:** mandiant-2017-apt34, mitre-attack-g0049

### Why this Capability score

Feasibility-only. Existing access could enable disruptive action, but the group has no documented disruption tradecraft.

### Modifiers

- **Willingness (-0):** no-constraints
- **Novelty (-1):** semi-custom — Hypothetical disruption would use existing access, not novel disruptive tooling.

### First-party Splunk

No first-party APT34 observations.

---

## Cyber-Crime

**Intent 1/5** (target-of-opportunity) · **Capability 1/5** (not-capable, with -2 novelty floored at 1) · **Composite: 2/10** · **🟢 LOW**

### Why this Intent score

APT34 is a state-aligned espionage actor with no documented financial motivation. No documented ransomware, extortion, or monetization operations attributable to APT34 in public reporting. Iran-aligned criminal ransomware is a separate ecosystem from APT34's mission profile.

**Sources:** mandiant-2017-apt34, mitre-attack-g0049

### Why this Capability score

No documented criminal tradecraft, ransomware deployment, or monetization infrastructure.

### Modifiers

- **Willingness (-0):** no-constraints
- **Novelty (-2):** commodity — Hypothetical criminal pivot would presumably use commodity tooling (no evidence of even this).

### First-party Splunk

No first-party APT34 observations.

---

## Review policy

- **Interval:** 90 days
- **Last reviewed:** 2026-05-01
- **Next review due:** 2026-07-30
- **Early review triggers:**
  - New attribution from A-grade source
  - New tooling documented
  - CVE exploitation linked to actor
  - Major campaign disclosure
  - First-party IOC observation

---

## Methodology note

Scored per `doctrine/THREAT-BOX-METHODOLOGY.md` (Piazza SANS framework adapted for A&D).
Target profile: `ad-prime-v1` (mid-to-large US A&D contractor, ITAR-regulated, DoD contracts).

**Confidence: A2.** Attribution and tooling are well-documented across multiple A-grade sources. Targeting-of-ad-prime-v1-specifically evidence is sparse, which is why Intent on espionage is 3 rather than 5. Confidence in the scoring calibration against ad-prime-v1 is one notch below A1.

**Authority gate:** overall weighted 4.9 rounds to 5 → MEDIUM threat level → `actor-profiler-autonomous-with-notification`. No `/approve-scoring` required. Per-category HIGH on espionage is preserved in the structured scoring but does not trigger the Hard Rule 5 gate.

---

*Generated from `threat-box.yaml`. To update, re-run `threat-box-scoring` skill and regenerate. See [profile.md](./profile.md) for full actor dossier.*
