# Threat Box — MuddyWater

**Actor ID:** 022
**Target profile:** ad-prime-v1 (mid-to-large US A&D contractor, ITAR-regulated)
**Scored:** 2026-05-09 by `actor-profiler`
**Approval:** auto-committed (LOW overall — doctrine authority table)
**Overall Threat Level:** 🟢 **LOW** (weighted 4.15/10)
**Primary threat vector:** Espionage (category-level 🟡 MEDIUM, composite 7)

---

## Summary

MuddyWater is assessed as an overall 🟢 **LOW** threat to the Archimedes target profile (`ad-prime-v1`), primarily driven by espionage capability. The category-level espionage composite is 🟡 **MEDIUM** (7/10); four floor categories dilute via doctrine weighting to overall LOW.

**This was the operator-anticipated HIGH that did NOT materialize.** Two stacked disciplinary outcomes drove the result down:

1. **Espionage Intent capped at 3 (Sector Association), not 5 (Target-Specific).** Per the source-finding red-team specific revisions carried into the dossier, Rapid7 names US construction, manufacturing, and business services as victim sectors. **NO defense primes. NO A&D watchlist entity.** Per the methodology evidence-minimum table, Intent=5 requires "at least 1 A-grade source documenting targeting of ad-prime-v1 profile" — that source does not exist for MuddyWater.

2. **72-hour auto-downgrade clock fired with no independent corroboration.** The clock on [finding-2026-05-06-FLASH-0002](../../findings/finding-2026-05-06-FLASH-0002.md) resolved at ~2026-05-09 12:00 EDT. No second A/B-grade vendor (Mandiant, Unit 42, MSTIC, CrowdStrike, Recorded Future, Volexity) corroborated. The Record + BleepingComputer + SecurityWeek coverage is pure relay (independence test failed in raw-2026-05-07-pm-002 grading). First-party Splunk re-queried 2026-05-09 PM sweep: zero hits across all 7 directly-queryable IOCs over -30d.

This is the **third workflow validation pass** after UNC1549 (5.4 MEDIUM) and Charming Kitten (4.45 LOW). Same pattern recurring: red-team `qualify` directives bind Intent below ceiling, four floor categories dilute, weighted overall lands LOW or MEDIUM, Hard Rule 5 gate does not fire.

### Per-category breakdown

| Category | Composite | Level |
|---|---|---|
| Espionage (35%) | 7/10 | 🟡 MEDIUM |
| Supply Chain (20%) | 4/10 | 🟢 LOW |
| Destructive (15%) | 2/10 | 🟢 LOW (floor preserved) |
| Disruptive (15%) | 2/10 | 🟢 LOW (floor) |
| Cyber-Crime (15%) | 2/10 | 🟢 LOW (floor preserved) |

**Weighted overall:** 7×0.35 + 4×0.20 + 2×0.15 + 2×0.15 + 2×0.15 = 2.45 + 0.80 + 0.30 + 0.30 + 0.30 = **4.15 → LOW**

---

## Espionage

**Intent 3/5** (sector-association) · **Capability 4/5** (significant, semi-custom) · **Composite: 7/10** · 🟡 **MEDIUM**

### Why this Intent score

Intent=3 (Sector Association) is the binding-with-red-team-qualify scoring outcome — NOT Intent=5 (Target-Specific) and NOT Intent=4 (Ideology Association).

**Intent=5 is NOT met.** Per the methodology evidence-minimum table, Intent=5 requires "at least 1 A-grade source documenting targeting of ad-prime-v1 profile" — i.e., direct documented targeting of a US aerospace and defense prime. That source does not exist for MuddyWater. Rapid7 2026-05-06 (the only 2026 US-pivot source) names US construction, manufacturing, and business services as victim sectors. Rapid7 explicitly does NOT specify defense manufacturing. The scoring MUST NOT extrapolate construction / manufacturing / business services into A&D-direct targeting (red-team specific revision carried from source finding).

**Intent=4 is also a poor fit.** Ideology Association applies when the actor targets based on anti-NATO / anti-Western / pro-nation-state ideology demonstrated through targeting Western defense-policy think tanks, journalists, dissidents (cf. Charming Kitten Q2 2026 pattern). Historical MuddyWater pattern is regional MENA government / telco / oil-and-gas, not ideology-driven against US/Western targets. The 2026 Rapid7-attributed US-pivot, even if confirmed, is sector-shaped, not ideology-shaped.

**Intent=3 is the honest binding read.** Multiple A-grade sources document sustained MuddyWater sector-association targeting of MENA government, telecommunications, and oil-and-gas across 2017–2025. The 2026 Rapid7-attributed US-pivot is also sector-association in the US.

Carry forward: H2 contrarian ACH (different MOIS-linked Iranian cluster sharing tooling) and H6 (mixed-composition state + criminal Chaos affiliate) remain at zero inconsistencies vs H1 (MuddyWater specifically) at one. Per Hard Rule 2 these surface as cluster-imprecision in Rapid7's moderate-confidence framing, not as alternative actor attributions. Scoring respects this binding by anchoring Intent in HISTORICAL MuddyWater documentation (multi-source A-grade) which is robust regardless of the 2026 attribution dispute.

**Sources:** MITRE G0069, Microsoft Mango Sandstorm, Unit 42, Symantec Seedworm, ClearSky, Trend Micro Earth Vetala, finding-2026-05-06-FLASH-0002.

### Why this Capability score

Capability=5 (Significant) is well-met. The methodology requires "Multiple A-grade sources AND documented active use within last 24 months." MuddyWater satisfies both.

Capability scoring anchors on the **long-running pre-2026 capability documentation**, which is robust regardless of the 2026 attribution dispute: POWERSTATS, Mori / SHARPSTATS / DELPHSTATS, PhonyC2, Donald Gay / Amy Cherne code-signing certificate lineage, pythonw.exe code injection, Microsoft Teams "IT Support" persona social engineering (multiple vendors, 2024-2025 reporting before Rapid7 2026), legitimate-tool abuse (DWAgent, AnyDesk, Quick Assist), historical CVE exploitation (ZeroLogon, ProxyLogon / ProxyShell era).

2026-specific tooling additions (Game.exe / Darkcomp, ms_upd.exe loader, Stagecomp) carry the Rapid7 single-source attribution caveat per Hard Rule 2 and are NOT promoted as MuddyWater-canonical pending second A/B-grade vendor confirmation. Capability=5 is justified WITHOUT relying on the attribution-caveated 2026 surfaces — the pre-2026 capability is already at ceiling.

Per the source finding red-team specific revisions: "the espionage-shaped TTP-and-objective observation is more defensible than the actor-specific cluster identification." Capability=5 lives at the more-defensible end of that distinction.

**Sources:** MITRE G0069, Microsoft Mango Sandstorm, Unit 42, Symantec Seedworm, ClearSky, Trend Micro Earth Vetala, finding-2026-05-06-FLASH-0002.

### Modifiers

- **Willingness (-0):** no-constraints — Iran/MOIS, strained US diplomatic relations, sanctions regime, active hostilities backdrop.
- **Novelty (-1):** semi-custom — meaningful custom RAT investment (POWERSTATS, Mori, SHARPSTATS / DELPHSTATS, PhonyC2, 2026 Game.exe per attribution-caveated reporting) sits alongside heavy reliance on legitimate-tool abuse (DWAgent, AnyDesk, Quick Assist), commodity Microsoft Teams social engineering tradecraft (mechanism-portable across multiple actors per 2025-2026 reporting), and commodity Chaos ransomware. Custom-RAT investment argues against -2; legitimate-tool / mechanism-portable / Chaos-commodity mix argues against -0. Semi-Custom is the honest middle position.

### First-party Splunk

🔴 **No hits.** Re-queried 2026-05-09 PM sweep against the 7 directly-queryable IOCs (4 IPv4 + 3 domains) over -30d. Zero hits in `defenseclaw_local` and `archimedes` indices. The 9 SHA256 hashes are still not directly queryable against current sourcetypes pending `_master-index.yaml` ingestion. The `defenseclaw_local` index has shown zero non-archimedes-internal events for eight consecutive sweeps — index appears dormant for live security telemetry. Silent Splunk is not disconfirming. No IOC corroboration bonus applied.

---

## Supply Chain

**Intent 2/5** (regional-association) · **Capability 2/5** (limited, semi-custom) · **Composite: 4/10** · 🟢 **LOW**

### Why this Intent score

Intent=2 (Regional Association). Historical MuddyWater pattern includes IT-service-provider compromise as relay into customer environments (T1199 Trusted Relationship), documented across multiple A-grade sources including Symantec Seedworm and Unit 42 reporting. Consistent with broader Iranian-ecosystem T1199 usage. However, supply-chain compromise is NOT MuddyWater's primary MO — it surfaces opportunistically alongside spearphishing and exploit-public-facing as initial-access vectors. The 2026 Rapid7 report does NOT make any supply-chain compromise claim. Intent=3 (Sector Association) would require supply-chain-specific sector targeting beyond opportunistic IT-service-provider relay.

**Sources:** MITRE G0069, Symantec Seedworm, Unit 42.

### Why this Capability score

Capability=3 (Limited) — some evidence across a few incidents but no extensive, sustained, multi-target supply-chain prosecution comparable to APT29 SolarWinds or APT41 software supply-chain operations.

**Sources:** MITRE G0069, Symantec Seedworm.

### Modifiers

- **Willingness (-0):** no-constraints
- **Novelty (-1):** semi-custom — same toolchain mix as espionage.

### First-party Splunk

No first-party supply-chain-specific observations.

---

## Destructive

**Intent 1/5** (target-of-opportunity) · **Capability 1/5** (possible, commodity) · **Composite: 2/10** · 🟢 **LOW (floor preserved per scoring discipline)**

### Why this Intent score

Intent=1 — destructive operations are NOT MuddyWater's MO. Mission profile is intelligence collection per sustained A-grade source consensus and per Rapid7 2026-05-06 explicit assessment. The Chaos-ransomware-without-encryption pattern is FALSE-FLAG THEATER deployed for espionage cover, NOT genuine destructive intent. Per the source-finding red-team specific revisions and the TEMPLATE scoring discipline note carried forward verbatim: **"Do NOT inflate destructive scoring on the basis of the false-flag artifacts."** Floor preserved.

**Sources:** finding-2026-05-06-FLASH-0002, Microsoft Mango Sandstorm, Unit 42.

### Why this Capability score

Capability=2 (Possible) — feasibility confirmed (Chaos artifact deployment in 2026 Rapid7 reporting demonstrates the operator can drop ransomware payloads, even as theater) but no genuine destructive outcomes documented.

### Modifiers

- **Willingness (-0):** no-constraints
- **Novelty (-2):** commodity — Chaos ransomware family is low-tier commodity ransomware with multiple criminal affiliates 2025-2026.

### First-party Splunk

No first-party destructive-related observations.

---

## Disruptive

**Intent 1/5** (target-of-opportunity) · **Capability 1/5** (possible, semi-custom) · **Composite: 2/10** · 🟢 **LOW (floor)**

### Why this Intent score

Intent=1 — disruptive operations are NOT MuddyWater's MO. Some sparse historical regional patterns may exist in Iraqi-government-targeting context but availability disruption is not documented as a primary objective.

**Sources:** MITRE G0069, Unit 42.

### Why this Capability score

Capability=2 (Possible) — feasibility based on remote-access tooling and code execution capability documented elsewhere. No actual disruptive outcomes documented against US targets.

### Modifiers

- **Willingness (-0):** no-constraints
- **Novelty (-1):** semi-custom

### First-party Splunk

No first-party disruptive-related observations.

---

## Cyber-Crime

**Intent 1/5** (target-of-opportunity) · **Capability 1/5** (possible, commodity) · **Composite: 2/10** · 🟢 **LOW (floor preserved per scoring discipline)**

### Why this Intent score

Intent=1 — MuddyWater is state-aligned MOIS espionage actor, NOT financially-motivated criminal cluster. Per Rapid7 2026-05-06 explicit assessment, the Chaos-ransomware-without-encryption pattern is FALSE-FLAG THEATER for espionage cover, NOT genuine extortion. The fake DLS onion address was deployed without actual victim leak.

Per the TEMPLATE scoring_note carried forward verbatim: **"MuddyWater is state-aligned MOIS espionage actor — not a financially-motivated criminal cluster. Score cyber-crime LOW. The Chaos-ransomware-without-encryption tradecraft does NOT make MuddyWater a criminal actor; it makes it an espionage actor using criminal-shaped cover."** Floor preserved.

**Sources:** finding-2026-05-06-FLASH-0002.

### Why this Capability score

Capability=2 (Possible) — Chaos ransomware deployment feasibility demonstrated (even as theater). No actual criminal extortion outcomes documented — fake DLS facade with no victim leak per Rapid7.

### Modifiers

- **Willingness (-0):** no-constraints
- **Novelty (-2):** commodity — Chaos ransomware

### First-party Splunk

No first-party cyber-crime-related observations.

---

## Confidence

**Admiralty:** A2 (inherits source-finding constraints in force at scoring time)

Scoring confidence inherits source-finding constraints:

- **Single-source veto on Rapid7 attribution PERSISTS at scoring time.** 72-hour auto-downgrade clock fired ~2026-05-09 12:00 EDT with no independent A/B-grade vendor corroborating. The Record + BleepingComputer + SecurityWeek post-disclosure coverage is pure relay.
- **Rapid7 self-rated moderate confidence on the cluster identification STACKS with single-source veto.**
- **First-party Splunk: zero hits over -30d on 2026-05-09 PM sweep across all 7 directly-queryable IOCs.**

Per RETRACTION-POLICY, [finding-2026-05-06-FLASH-0002](../../findings/finding-2026-05-06-FLASH-0002.md) should auto-downgrade to C3 "possibly true" (librarian handoff pending). However, the **scoring is robust against this auto-downgrade** because Capability anchors on long-running pre-2026 MuddyWater capability (multiple A-grade sources, robust regardless of 2026 attribution dispute), and Intent=3 (Sector Association) is supported by historical MENA pattern alone (multi-A-grade) and does NOT depend on the 2026-attribution-caveated US-pivot. If the source finding auto-downgrades, the 2026-specific tooling loses its MuddyWater-canonical claim, but the scoring construction remains sound.

---

## Review policy

- **Interval:** 90 days
- **Last reviewed:** 2026-05-09
- **Next review due:** 2026-08-07
- **Early review triggers:**
  - New attribution from A-grade source (a second A/B-grade vendor corroborating the Rapid7 2026 attribution would lift the single-source veto and trigger immediate rescoring — could move Intent toward 4 if framing is ideology-shaped, or sustain Intent=3 if sector-shaped)
  - New tooling documented
  - CVE exploitation linked to actor
  - Major campaign disclosure (especially A&D-prime targeting — would move Intent toward 5)
  - First-party IOC observation (Splunk hit on any of the 19 IOCs once `_master-index.yaml` ingested triggers immediate rescoring + IOC bonus)
  - Retraction-policy trigger (auto-downgrade of source finding triggers re-evaluation of attribution-caveated surfaces)

---

## Methodology note

Scored per `doctrine/THREAT-BOX-METHODOLOGY.md` (Piazza SANS framework adapted for A&D). Target profile: `ad-prime-v1` (mid-to-large US A&D contractor, ITAR-regulated, DoD contracts).

**Authority gate:** weighted overall LOW → `actor-profiler-autonomous` → auto-commit. Hard Rule 5 (HIGH human sign-off) did NOT fire.

**Source-finding confidence binding:** scoring confidence is capped by source-finding confidence. The 72-hour auto-downgrade clock fired with no independent corroboration; single-source veto persists. The scoring construction is engineered to be robust against this — Capability anchors on multi-A-grade pre-2026 documentation, Intent=3 is supported by historical MENA pattern alone.

---

*Generated from `threat-box.yaml` (`reviewed_by: auto-committed`). To update, re-run `threat-box-scoring` skill and regenerate.*
