# Threat Box — Peach Sandstorm

**Actor ID:** 027
**Target profile:** ad-prime-v1 (mid-to-large US A&D contractor, ITAR-regulated)
**Scored:** 2026-07-12 by `actor-profiler` · **Corrected (sourcing only):** 2026-07-12 (see Change Log)
**Approval:** auto-committed (overall weighted = MEDIUM; authority = actor-profiler-autonomous-with-notification). Hard Rule 5 `/approve-scoring` gate did NOT fire.
**Overall Threat Level:** 🟡 MEDIUM (weighted 5.5/10)
**Primary threat vector:** Espionage — per-category composite **9/10 = 🔴 HIGH**

---

## Summary

Peach Sandstorm (APT33) is assessed as an **overall MEDIUM threat** to the Archimedes target profile (`ad-prime-v1`), driven by a **HIGH espionage capability** against the exact profile — US aerospace, defense, and satellite organizations. It is the **most A&D-directly-relevant Iranian actor** Archimedes tracks. Multiple independent A-grade sources (FireEye/Mandiant 2017, Microsoft 2023-2024, Symantec 2019, Kaspersky, Unit 42 2026) document prime-direct, US-defense-sector targeting — the basis for scoring espionage Intent at Target-Specific (5), in parity with UNC1549 (#004).

Peach Sandstorm is also the **only Iranian roster actor with a documented destructive dimension** (SHAPESHIFT/DROPSHOT and StoneDrill wiper ties per FireEye and Kaspersky) — reflected in a non-floor destructive category. The destructive activity is regionally demonstrated (Gulf/Saudi energy), not directed at US A&D primes, so it is scored as a latent (Regional) rather than active-prime threat.

The per-category **espionage composite of 9 (HIGH)** is the operationally relevant number for defenders. The weighted 5.5 reflects that disruptive and cyber-crime are low, diluting a top-tier espionage actor when averaged across all five categories. Peach Sandstorm calibrates **above** its Iranian peers (UNC1549 5.4, APT34 4.9, Charming Kitten 4.45, MuddyWater 4.15, Cavern Manticore 3.25).

### Per-category breakdown

| Category | Composite | Level |
|---|---|---|
| Espionage (35%) | 9/10 | 🔴 HIGH |
| Supply Chain (20%) | 5/10 | 🟡 MEDIUM |
| Destructive (15%) | 4/10 | 🟢 LOW |
| Disruptive (15%) | 3/10 | 🟢 LOW |
| Cyber-Crime (15%) | 2/10 | 🟢 LOW |

---

## Espionage

**Intent 5/5** (target-specific) · **Capability 4/5** (significant, with -1 novelty) · **Composite: 9/10** · **🔴 HIGH**

### Why this Intent score

Peach Sandstorm (APT33) is the Iranian actor with the clearest, most recent, multi-A-grade-source record of targeting the exact ad-prime-v1 profile — US aerospace, defense, and satellite organizations. The evidence-minimum table requires at least one A-grade source documenting targeting of our specific profile for Intent=5; here there are several: FireEye/Mandiant 2017 titled its disclosure "APT33 Targets Aerospace and Energy Sectors" and named a US aerospace victim; Microsoft Sept 2023 documented password-spray follow-on intrusions concentrated in the defense, satellite, and pharmaceutical sectors; Microsoft Dec 2023 documented the FalseFont backdoor against the US Defense Industrial Base (corroborated by Unit 42 Mar 2024 and Nextron Jan 2024); Microsoft Aug 2024 documented the custom Tickler backdoor against US/UAE defense, satellite, and oil-and-gas orgs (Microsoft-originated — no standalone Mandiant Tickler advisory located 2026-07-12, co-reporting `pending_direct_retrieval`). This is prime-DIRECT, US-defense-sector targeting — materially different from the sector-shaped Iranian peers (MuddyWater, Charming Kitten, APT37, Cavern Manticore) where no A-grade source named A&D primes and Intent was correctly bounded. Scored in parity with UNC1549 (#004).

**Sources:** fireeye-apt33-2017, microsoft-peach-sandstorm-2023, microsoft-falsefont-2023, microsoft-mstic-tickler-2024

### Why this Capability score

Multiple A-grade sources document active espionage tradecraft within the last 24 months (Tickler Aug 2024, FalseFont Dec 2023, password-spray Sept 2023). A decade of continuous custom-tooling development (TURNEDUP, POWERTON, FalseFont, Tickler) plus documented cloud-identity tradecraft (ROADtools/Entra ID enumeration per Unit 42 2026). Capability=5 (Significant) is well-supported. Reduced by -1 novelty to final capability 4.

**Sources:** microsoft-mstic-tickler-2024, microsoft-falsefont-2023, microsoft-peach-sandstorm-2023, fireeye-apt33-2017, unit42-curious-serpens-2026

### Modifiers

- **Willingness (-0):** no-constraints — Iran / IRGC, sanctions regime, active cyber confrontation with the US, Gulf, and Israel.
- **Novelty (-1):** semi-custom — The access engine is high-volume password spray (commodity, well-detectable, rich identity-plane telemetry) plus abuse of open-source (ROADtools) and legitimate cloud (Azure) tooling. Custom backdoors (Tickler, FalseFont, TURNEDUP) are genuine nation-state implants but now publicly signatured. Not fully-novel/unsignatured LotL (-0), not pure commodity (-2). Identified nation-state tooling across multiple campaigns = -1.

### First-party Splunk

First-party sentinel 2026-07-12 (re-run at fold-in against the ratified atomic IOCs): 0 hits over -90d across `defenseclaw_local` + `archimedes` — on alias/tooling terms AND on the FalseFont/Tickler SHA256 set, `digitalcodecrafters[.]com`, `64.52.80[.]30`, and the Tickler `azurewebsites.net` C2 (`defenseclaw_local` categorical zero). Per Hard Rule 8, silent Splunk does not disconfirm — Frank is a home/test environment, not a US A&D prime. Visibility-bounded null; no bonus.

---

## Supply Chain

**Intent 3/5** (sector-association) · **Capability 2/5** (limited, with -1 novelty) · **Composite: 5/10** · **🟡 MEDIUM**

### Why this Intent score

Peach Sandstorm targets the defense sector broadly (the DIB is the supply chain of A&D primes), and its 2023 password-spray hit thousands of orgs with selective follow-on. But no A-grade source documents an end-to-end supply-chain compromise pivoting INTO a downstream A&D prime, and no specific supplier-to-prime relay is named. Intent=3 (Sector Association) — Intent=5 unsupported.

**Sources:** microsoft-peach-sandstorm-2023, microsoft-mstic-tickler-2024

### Why this Capability score

Broad password-spray + cloud-identity abuse gives feasible relay/pivot capability, and DIB targeting implies proximity to prime supply chains, but the single-hop supply-chain compromise into a downstream A&D victim is not documented end-to-end. Cap=3 (Limited), reduced by -1 novelty to final capability 2.

**Sources:** microsoft-peach-sandstorm-2023

### Modifiers

- **Willingness (-0):** no-constraints — Iran / IRGC.
- **Novelty (-1):** semi-custom — same identified tooling ecosystem (custom backdoors + commodity password spray + open-source ROADtools).

### First-party Splunk

No first-party IOC hits at time of scoring.

---

## Destructive

**Intent 2/5** (regional-association) · **Capability 2/5** (limited, with -1 novelty) · **Composite: 4/10** · **🟢 LOW**

### Why this Intent score

Peach Sandstorm is the one Iranian roster actor with documented ties to destructive malware — FireEye 2017 linked APT33 to the SHAPESHIFT/DROPSHOT wiper (used in testing), and Kaspersky linked StoneDrill to APT33-adjacent (NewsBeef) activity. But the demonstrated destructive operations were regionally focused (Gulf/Saudi energy, Shamoon-adjacent), NOT directed at US A&D primes. Destructive intent against ad-prime-v1 is Regional Association (2): latent capability, no A-grade source documents destructive tasking against a US A&D prime.

**Sources:** fireeye-apt33-2017, kaspersky-stonedrill-2017

### Why this Capability score

Real, differentiated destructive capability relative to Iranian espionage-only peers: FireEye (A1) tied APT33 to SHAPESHIFT/DROPSHOT; Kaspersky (A2) linked StoneDrill. Cap=3 (Limited): destructive tooling is documented, but attribution of the destructive attacks themselves carries the cited sources' softer "ties to" / "potential" language (preserved per Hard Rule 2, no upgrade). Reduced by -1 novelty to final capability 2.

**Sources:** fireeye-apt33-2017, kaspersky-stonedrill-2017

### Modifiers

- **Willingness (-0):** no-constraints — Shamoon-era destructive precedent against Gulf targets.
- **Novelty (-1):** semi-custom — wiper families are custom but now well-characterized/signatured.

### First-party Splunk

No first-party IOC hits at time of scoring.

---

## Disruptive

**Intent 2/5** (regional-association) · **Capability 1/5** (possible, with -1 novelty floored at 1) · **Composite: 3/10** · **🟢 LOW**

### Why this Intent score

Availability-disruption (DDoS, service disruption) is not a documented Peach Sandstorm hallmark. Wiper activity has a disruptive side-effect but is categorized as Destructive (integrity). For ad-prime-v1, disruptive intent is Regional Association (2): latent capability via existing access / destructive tooling, no documented availability-attack tasking against US A&D primes.

**Sources:** fireeye-apt33-2017

### Why this Capability score

Feasibility-only. Existing access + wiper tooling could enable disruptive action, but no documented dedicated availability-disruption tradecraft. Cap=2 (Possible), reduced by -1 novelty to final capability 1.

### Modifiers

- **Willingness (-0):** no-constraints.
- **Novelty (-1):** semi-custom — hypothetical disruption would piggyback on existing access / destructive tooling.

### First-party Splunk

No first-party IOC hits at time of scoring.

---

## Cyber-Crime

**Intent 1/5** (target-of-opportunity) · **Capability 1/5** (not-capable, with -2 novelty floored at 1) · **Composite: 2/10** · **🟢 LOW**

### Why this Intent score

Peach Sandstorm is a state-sponsored espionage/strategic-collection actor with no documented financial motivation. No ransomware, extortion, or monetization operations attributable to the group in public reporting. Intent=1 (Target of Opportunity).

**Sources:** fireeye-apt33-2017, mitre-attack-g0064

### Why this Capability score

No documented criminal tradecraft, ransomware deployment, or monetization infrastructure.

### Modifiers

- **Willingness (-0):** no-constraints (immaterial at Intent=1).
- **Novelty (-2):** commodity — hypothetical criminal pivot would presumably use commodity tooling (no evidence of even this).

### First-party Splunk

No first-party IOC hits at time of scoring.

---

## Review policy

- **Interval:** 90 days
- **Last reviewed:** 2026-07-12
- **Next review due:** 2026-10-10
- **Early review triggers:**
  - New attribution from A-grade source
  - New tooling documented
  - CVE exploitation linked to actor
  - Major campaign disclosure
  - First-party IOC observation
  - New A-grade source naming a US A&D-prime victim (would firm/raise the espionage Intent basis)
  - Destructive-tooling staging observed (escalation tripwire per destructive category)

---

## Methodology note

Scored per `doctrine/THREAT-BOX-METHODOLOGY.md` (Piazza SANS framework adapted for A&D).
Target profile: `ad-prime-v1` (mid-to-large US A&D contractor, ITAR-regulated, DoD contracts).

**Confidence: A1.** Attribution and tooling are documented across multiple independent A-grade sources (FireEye/Mandiant, Microsoft, Symantec, CrowdStrike, Kaspersky, Dragos, Unit 42) over 2017-2024 — no single-source dependence, no single-source veto. The load-bearing Intent=5 call rests on multiple A-grade sources documenting US defense/satellite/aerospace targeting, clearing the evidence-minimum bar for Target-Specific — the deliberate difference from sector-bounded Iranian peers. Robustness: even at Intent=4 the espionage composite would be 8 (still HIGH category) and the weighted overall would round to 5 (still MEDIUM).

**Authority gate:** overall weighted 5.5 → MEDIUM threat level → `actor-profiler-autonomous-with-notification`. No `/approve-scoring` required; Hard Rule 5 gate did NOT fire. Per-category HIGH on espionage is preserved in the structured scoring but does not trigger the gate.

---

## Change Log

- **2026-07-12 — Sourcing correction (no rescore).** Collector direct-retrieval fold-in. The Tickler campaign was corrected to cite **Microsoft alone** (MSTIC, 2024-08-28, A1); the earlier build draft co-credited Mandiant, but no standalone Mandiant Tickler advisory was retrievable. Source id `microsoft-mandiant-tickler-2024` renamed to `microsoft-mstic-tickler-2024`; Mandiant Tickler co-reporting flagged `pending_direct_retrieval`. **Intent=5 re-verified and HOLDS** on the corrected source set (FalseFont vs DIB [Microsoft A1 + Unit 42 A1 + Nextron A2] + Tickler vs defense/satellite/oil-and-gas [Microsoft A1] + FireEye 2017 US aerospace victim). All category scores and the weighted **5.5 MEDIUM are UNCHANGED**. Atomic FalseFont/Tickler IOCs (32 indicators) ratified into `iocs.yaml`/`iocs.md`. Splunk sentinel re-run against the new hashes/domains: 0 hits -90d, visibility-bounded null.
- **2026-07-12 — Initial scoring** at dossier creation via `/new-actor`. Weighted 5.5 MEDIUM; espionage composite 9 HIGH. Auto-committed.

---

*Generated from `threat-box.yaml`. To update, re-run `threat-box-scoring` skill and regenerate. See [profile.md](./profile.md) for full actor dossier.*
