# Threat Box — Cavern Manticore

**Actor ID:** 026
**Target profile:** ad-prime-v1
**Scored:** 2026-07-07 by `actor-profiler`
**Approval:** auto-committed (LOW — Hard Rule 5 gate did not fire)
**Overall Threat Level:** 🟢 LOW (weighted 3.25/10)

---

## Summary

Cavern Manticore is assessed as an overall 🟢 **LOW** threat to the Archimedes target profile (ad-prime-v1), with its risk concentrated in **espionage** (category MEDIUM). The assessment is deliberately conservative: the actor shows genuine tooling substance — a mature modular .NET C2 framework (Cavern/Cav3rn), DLL side-loading, and exploitation of five 2025-vintage CVEs — but the entire evidence base is a **single report from a single IR vendor** (Check Point Research), relayed by The Hacker News (a pure relay, not corroboration), with the CPR primary **not directly retrieved**. Admiralty A2, WEP capped at "likely" by single-source veto.

The espionage category scores MEDIUM (composite 5) and is the primary threat vector; the overall dilutes to LOW because destructive, disruptive, and cyber-crime categories are at the floor and supply-chain is LOW. This calibrates below Iran-MOIS peers UNC1549 (5.4, MEDIUM) and APT34 (4.9, MEDIUM), and near MuddyWater (4.15, LOW) and Charming Kitten (4.45, LOW) — slightly lower given the thinner one-report base.

**Do not read LOW overall as "not dangerous."** The espionage per-category composite (5, MEDIUM) is the operative number for defensive prioritization; the LOW overall reflects a narrow, espionage-only threat surface plus a single-source evidence cap, not benign intent.

### Per-category breakdown

| Category | Composite | Level |
|---|---|---|
| Espionage (35%) | 5/10 | 🟡 |
| Supply Chain (20%) | 3/10 | 🟢 |
| Destructive (15%) | 2/10 | 🟢 |
| Disruptive (15%) | 2/10 | 🟢 |
| Cyber-Crime (15%) | 2/10 | 🟢 |

**Standing attribution caveat:** CPR designates Cavern Manticore a distinct cluster while noting tactical overlaps with MuddyWater and Lyceum/OilRig. Archimedes originates no cross-walk (Hard Rule 2). Whether this is a genuinely distinct cluster vs. a MuddyWater/OilRig sub-cluster is an open SAT-ACH for the analyst — unresolved.

---

## Espionage

**Intent 3/5** (sector-association) · **Capability 2/5** (limited) · **Composite: 5/10** · **MEDIUM**

### Why this Intent score

CPR names aviation, energy, IT providers, government, and public sector among Cavern Manticore's targets, geographically anchored to Israel (primary), Egypt, and the UAE. This is broad-sector Iranian MOIS collection, NOT documented targeting of A&D primes. Per the evidence-minimum table, Intent=5 (Target-Specific) requires at least one A-grade source documenting targeting of the ad-prime-v1 profile — no such source exists (no A&D-prime victim named; aviation appears only as one sector among several). Intent capped at 3 (Sector Association): aviation sits within the named sector set but targeting is not A&D-prime-directed. Single-source even for this sector claim.

**Sources:** [finding-2026-07-06-0001](../../findings/finding-2026-07-06-0001-checkpoint-thn-cavern-manticore-mois-cavern-net-c2-framework-new-cluster-not-in-roster-new-actor-candidate.md)

### Why this Capability score

CPR documents genuine tooling substance — a mature, modular .NET C2 framework, DLL side-loading, and exploitation of five 2025-vintage CVEs. But the evidence base is a SINGLE report from a SINGLE IR vendor, relayed (not corroborated) by The Hacker News, and the CPR primary was NOT directly retrieved. One documented cluster designation, no multi-campaign body of work, no independent second-vendor corroboration → Cap=3 (Limited), not Cap=4 or 5. The single-source veto and non-retrieval hold capability down despite real tooling substance. Semi-custom novelty (-1) then reduces final Capability to 2.

**Sources:** [finding-2026-07-06-0001](../../findings/finding-2026-07-06-0001-checkpoint-thn-cavern-manticore-mois-cavern-net-c2-framework-new-cluster-not-in-roster-new-actor-candidate.md)

### Modifiers

- **Willingness (-0):** no-constraints — Iran / MOIS; sanctions regime, no diplomatic constraints on cyber ops against Western-aligned targets.
- **Novelty (-1):** semi-custom — newly-documented custom modular .NET C2 (Cavern) now identified/named by CPR; identified nation-state tooling scores -1, not fully novel (-0) nor commodity (-2).

### First-party Splunk

No first-party IOC hits at time of scoring. Sentinel run 2026-07-07: 0 hits over -90d on C2 domain + distinctive DLL filenames across `defenseclaw_local` and `archimedes`. Per Hard Rule 8, silent Splunk does not disconfirm — Frank is not an Israeli/Egyptian/UAE IT-provider or government org matching the victim profile. Visibility-bounded null.

---

## Supply Chain

**Intent 2/5** (regional-association) · **Capability 1/5** (possible) · **Composite: 3/10** · **LOW**

### Why this Intent score

IT-provider targeting is a supply-chain-relevant pattern, but CPR documents no A&D-prime-directed supply-chain campaign and names no downstream A&D victim reached via IT-provider compromise. Intent=2 (Regional Association): the actor targets Western-aligned regional entities generally, with supply-chain exposure implied but not A&D-prime-anchored.

**Sources:** [finding-2026-07-06-0001](../../findings/finding-2026-07-06-0001-checkpoint-thn-cavern-manticore-mois-cavern-net-c2-framework-new-cluster-not-in-roster-new-actor-candidate.md)

### Why this Capability score

IT-provider compromise implies a pivot/relay capability, but the single CPR report does not document a completed supply-chain pivot into a downstream victim. Feasibility is indicated; demonstrated supply-chain capability is not. Cap=2 (Possible), reduced to 1 by semi-custom novelty.

**Sources:** [finding-2026-07-06-0001](../../findings/finding-2026-07-06-0001-checkpoint-thn-cavern-manticore-mois-cavern-net-c2-framework-new-cluster-not-in-roster-new-actor-candidate.md)

### Modifiers

- **Willingness (-0):** no-constraints — Iran / MOIS.
- **Novelty (-1):** semi-custom — same identified modular .NET tooling ecosystem.

### First-party Splunk

No first-party IOC hits at time of scoring.

---

## Destructive

**Intent 1/5** (target-of-opportunity) · **Capability 1/5** (not-capable) · **Composite: 2/10** · **LOW**

### Why this Intent score

No destructive intent documented. CPR characterizes Cavern Manticore as an espionage cluster; no wiper, no destructive tasking reported.

**Sources:** [finding-2026-07-06-0001](../../findings/finding-2026-07-06-0001-checkpoint-thn-cavern-manticore-mois-cavern-net-c2-framework-new-cluster-not-in-roster-new-actor-candidate.md)

### Why this Capability score

No evidence of destructive capability in the single available report.

**Sources:** [finding-2026-07-06-0001](../../findings/finding-2026-07-06-0001-checkpoint-thn-cavern-manticore-mois-cavern-net-c2-framework-new-cluster-not-in-roster-new-actor-candidate.md)

### Modifiers

- **Willingness (-0):** no-constraints (immaterial at Intent=1).
- **Novelty (-0):** not-applicable — no destructive tooling documented.

### First-party Splunk

No first-party IOC hits at time of scoring.

---

## Disruptive

**Intent 1/5** (target-of-opportunity) · **Capability 1/5** (not-capable) · **Composite: 2/10** · **LOW**

### Why this Intent score

No disruptive intent documented. No DDoS, defacement, or service-disruption tasking reported by CPR.

**Sources:** [finding-2026-07-06-0001](../../findings/finding-2026-07-06-0001-checkpoint-thn-cavern-manticore-mois-cavern-net-c2-framework-new-cluster-not-in-roster-new-actor-candidate.md)

### Why this Capability score

No evidence of disruptive capability in the single available report.

**Sources:** [finding-2026-07-06-0001](../../findings/finding-2026-07-06-0001-checkpoint-thn-cavern-manticore-mois-cavern-net-c2-framework-new-cluster-not-in-roster-new-actor-candidate.md)

### Modifiers

- **Willingness (-0):** no-constraints (immaterial at Intent=1).
- **Novelty (-0):** not-applicable — no disruptive tooling documented.

### First-party Splunk

No first-party IOC hits at time of scoring.

---

## Cyber-Crime

**Intent 1/5** (target-of-opportunity) · **Capability 1/5** (not-capable) · **Composite: 2/10** · **LOW**

### Why this Intent score

No financially-motivated / criminal intent documented. CPR characterizes Cavern Manticore as MOIS-affiliated state espionage, not criminal.

**Sources:** [finding-2026-07-06-0001](../../findings/finding-2026-07-06-0001-checkpoint-thn-cavern-manticore-mois-cavern-net-c2-framework-new-cluster-not-in-roster-new-actor-candidate.md)

### Why this Capability score

No evidence of cyber-crime capability (ransomware, extortion, financial theft) in the single available report.

**Sources:** [finding-2026-07-06-0001](../../findings/finding-2026-07-06-0001-checkpoint-thn-cavern-manticore-mois-cavern-net-c2-framework-new-cluster-not-in-roster-new-actor-candidate.md)

### Modifiers

- **Willingness (-0):** no-constraints (immaterial at Intent=1).
- **Novelty (-0):** not-applicable — no criminal tooling documented.

### First-party Splunk

No first-party IOC hits at time of scoring.

---

## Review policy

- **Interval:** 90 days
- **Last reviewed:** 2026-07-07
- **Next review due:** 2026-10-05
- **Early review triggers:**
  - New attribution from A-grade source
  - New tooling documented
  - CVE exploitation linked to actor
  - Major campaign disclosure
  - First-party IOC observation
  - **Independent second-IR-vendor corroboration** (Mandiant / CrowdStrike / Unit 42 / MSTIC / Microsoft) — would resolve the single-source veto and lift WEP
  - **Direct retrieval of the CPR primary**

---

## Methodology note

Scored per `doctrine/THREAT-BOX-METHODOLOGY.md` (Piazza SANS framework adapted for A&D).
Target profile: `ad-prime-v1` (mid-to-large US A&D contractor, ITAR-regulated, DoD contracts).

Single-source assessment (Check Point Research; CPR primary not directly retrieved). Scoring capped conservatively on a one-report evidence base; lift path is independent corroboration or direct retrieval. Hard Rule 2 preserved throughout — no Archimedes-originated attribution, no cross-walk to MuddyWater (#022) or APT34/OilRig (#023) despite CPR-noted tactical overlaps. See [profile.md](./profile.md) for full actor context.

---

*Generated from `threat-box.yaml`. To update, re-run `threat-box-scoring` skill and regenerate.*
