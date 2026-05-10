# Threat Box — APT37

**Actor ID:** 024
**Target profile:** ad-prime-v1 (mid-to-large US A&D contractor, ITAR-regulated)
**Scored:** 2026-05-10 by `actor-profiler`
**Approval:** `auto-committed` (MEDIUM weighted overall — no Hard Rule 5 gate)
**Overall Threat Level:** 🟡 MEDIUM (weighted 4.9/10)
**Primary threat vector:** Espionage (category-tier 🔴 HIGH composite 8/10)

---

## Summary

APT37 is assessed as an overall 🟡 MEDIUM threat to the Archimedes target profile (`ad-prime-v1`), driven entirely by espionage. The espionage category alone scores composite 8 (🔴 HIGH at the per-category tier); four other categories at floor or near-floor dilute via doctrine weighting to overall MEDIUM.

The operator-anticipated outcome at dossier scaffold time was HIGH overall, with the Hard Rule 5 gate flagged. **Actual computation lands MEDIUM** for the same disciplinary reason that brought MuddyWater in at LOW one day earlier: the evidence-minimum table caps Espionage Intent at 3 (Sector Association), not 5 (Target-Specific). NO public reporting documents APT37 targeting a US A&D prime, an ITAR-regulated defense contractor, a defense-system developer, or a Tier-1/2 defense supplier. The dominant documented targeting is civil-society, defectors, Korean-language journalists, DPRK-policy researchers, and regional industrial sectors. FireEye 2018's listing of "aerospace" among South Korean industrial-sector targeting supports Intent=3 (Sector Association); it does not support Intent=5. The roster intake note framed the relevance honestly as "INDIRECT/STRUCTURAL — A&D-direct targeting is undocumented in public reporting." Scoring upholds that framing.

### Per-category breakdown

| Category | Composite | Level |
|---|---|---|
| Espionage (35%) | 8/10 | 🔴 HIGH |
| Supply Chain (20%) | 6/10 | 🟡 MEDIUM |
| Destructive (15%) | 2/10 | 🟢 LOW |
| Disruptive (15%) | 2/10 | 🟢 LOW |
| Cyber-Crime (15%) | 2/10 | 🟢 LOW |

**Weighted:** 8(0.35) + 6(0.20) + 2(0.15) + 2(0.15) + 2(0.15) = 2.80 + 1.20 + 0.30 + 0.30 + 0.30 = **4.9 → MEDIUM**

---

## Espionage

**Intent 3/5** (sector-association) · **Capability 5/5** (significant) · **Composite: 8/10** · **🔴 HIGH** (category-tier)

### Why this Intent score

Intent=3 (Sector Association) is the highest score the evidence-minimum table supports. Intent=5 (Target-Specific) requires at least one A-grade source documenting targeting of the `ad-prime-v1` profile (US A&D prime, ITAR-regulated, defense-system developer, Tier-1/2 defense supplier with classified R&D). **NO such source exists in public reporting on APT37.**

APT37's dominant documented targeting across 2012–2026:

- **North Korean defectors and refugees** (multi-vendor: Mandiant 2018, Kaspersky 2016–2018, Cisco Talos 2017, Volexity 2021, ESET 2026)
- **South Korean civil society** — NGOs, journalists, human-rights organizations engaged with refugee populations
- **DPRK-policy researchers** and academic specialists studying DPRK military/political programs (think-tank-tier)
- **Defense-policy think-tanks** (regional, occasionally US) — A&D-adjacent at most
- **South Korean industrial sectors** per FireEye 2018, including the phrase "aerospace" among broader sector listings (chemicals, electronics, manufacturing). This is sector-shaped historical South-Korea-domestic targeting, not US-A&D-prime targeting.
- **Diaspora civil society** — ESET 2026 Sqgame compromise targeting ethnic Koreans in Yanbian Korean Autonomous Prefecture, China, with assessed inclusion of North Korean refugees and defectors

The FireEye 2018 mention of "aerospace" in South Korean industrial-sector targeting is the closest the public record comes to A&D relevance. It supports Intent=3 (Sector Association) on a documented A-grade source basis: the actor has historically targeted sector-broad industrial categories that include aerospace among others. It does NOT support Intent=5: targeting was sector-shaped (not target-specific) and directed at South Korean (not US) industrial entities. Per the methodology's red-flag note, "if your evidence is 'this actor hits government entities and A&D is government-adjacent,' downgrade to Intent=3." The same logic applies — sector-broad industrial targeting that lists aerospace alongside chemicals and manufacturing is sector-shaped, not target-specific.

Intent=4 (Ideology Association) was considered and rejected. The Ideology slot fits actors driven by ideological opposition to a target population (e.g., Charming Kitten's anti-dissident anti-Israel-policy anti-US-Iran-policy tasking). APT37 is mission-shaped — the targeting traces to specific DPRK regime objectives (defector tracking, civil-society coercion, regional intelligence collection) rather than to anti-Western-ideology orientation. Intent=3 is the honest read.

**Sources:** [fireeye-apt37-reaper-2018](../../findings/finding-2026-05-07-0004.md), [cisco-talos-rokrat-2017](../../findings/finding-2026-05-07-0004.md), [kaspersky-operation-daybreak-2016](../../findings/finding-2026-05-07-0004.md), [volexity-inkysquid-2021](../../findings/finding-2026-05-07-0004.md), [eset-via-the-record-2026-05-07](../../findings/finding-2026-05-07-0004.md)

### Why this Capability score

Capability=5 (Significant) lands cleanly on the evidence-minimum threshold: **multiple A-grade sources document active espionage capability with confirmed use within the last 24 months.**

A-grade sources (multiple, independent):

- FireEye/Mandiant Feb 2018 — "APT37 (REAPER): The Overlooked North Korean Actor"
- Cisco Talos 2017 — "ROKRAT Reloaded"
- Kaspersky 2016 — "Operation Daybreak" (CVE-2016-4117 Flash zero-day)
- Kaspersky 2018 — "ScarCruft continues to evolve"
- Cisco Talos 2018 — CVE-2018-4878 Flash zero-day weaponization
- Volexity 2021 — "InkySquid: The Missing Arsenal" (BLUELIGHT, strategic web compromise)
- ESET 2026 (relayed The Record 2026-05-07) — Sqgame supply-chain compromise / BirdCall (14+ month operator-side persistence)

Active-use-within-24-months threshold: comfortably met. ESET 2026 documents continuous operational tempo from November 2024 through 2026. Capability spans Windows custom RAT (RokRAT, BLUELIGHT), Android backdoor (BirdCall, prior RokRAT mobile, Konni-cluster overlap), supply-chain compromise (Sqgame 2026), strategic website compromise (Volexity 2021), zero-day exploitation (CVE-2016-4117, CVE-2018-4878), and cloud-platform C2 abuse (pCloud, Yandex Disk, Dropbox, Google Drive). Cross-platform reach and supply-chain initial-access pattern distinguish APT37 from many regional-tier APTs.

Single-source veto on the Sqgame-specific 2026 campaign (per finding-2026-05-07-0004 — ESET via The Record alone) does NOT constrain the broader Capability=5 assessment, which rests on the multi-vendor pre-2026 record.

**Sources:** fireeye-apt37-reaper-2018, cisco-talos-rokrat-2017, cisco-talos-group123-2018, cisco-talos-rokrat-2018, kaspersky-operation-daybreak-2016, kaspersky-scarcruft-evolves-2018, volexity-inkysquid-2021, eset-via-the-record-2026-05-07, multi-vendor-apt37-tracking

### Modifiers

- **Willingness (-0):** no-constraints — DPRK; comprehensive sanctions regime, no diplomatic ties, active hostilities posture
- **Novelty (-0):** custom-advanced — RokRAT/BLUELIGHT/BirdCall are custom APT37-attributed implants; cloud-platform C2 blends into legitimate HTTPS noise; supply-chain initial access against compromised legitimate platforms; zero-day exploitation history. No commodity-tooling signature dominates.

### First-party Splunk

🟢 No first-party IOC hits at time of scoring. Splunk check executed 2026-05-10: zero hits across primary IOC search set (APT37 / ScarCruft / Reaper / InkySquid / RedEyes / BirdCall / RokRAT / BLUELIGHT / Sqgame / pcloud.com / cloud-api.yandex.net) over -30d window across `defenseclaw_local` and `archimedes` indices. Mobile-malware (BirdCall) primary distribution to consumer Android in Yanbian, China is unlikely to surface in DefenseClaw enterprise telemetry given consumer-Android targeting profile.

---

## Supply Chain

**Intent 2/5** (regional-association) · **Capability 4/5** (credible) · **Composite: 6/10** · **🟡 MEDIUM**

### Why this Intent score

Intent=2 (Regional Association). The Sqgame Android APK supply-chain compromise per ESET 2026 demonstrates supply-chain INTENT, but targeting was a Korean-language consumer Android gaming platform distributing to ethnic Koreans in Yanbian, China — diaspora civil-society regional targeting, NOT US A&D supplier ecosystem, NOT enterprise SaaS, NOT software vendor build-pipeline compromise of the SolarWinds / 3CX / MOVEit pattern. Intent against US A&D supply chain is undocumented. Intent=3 (Sector Association) would require evidence of supply-chain targeting against an A&D-relevant sector, which does not exist. Intent=2 captures the demonstrated supply-chain capability against a regional consumer-Android distribution channel without sector-broad A&D relevance.

**Sources:** eset-via-the-record-2026-05-07

### Why this Capability score

Capability=4 (Credible) — one A-grade source (ESET via The Record 2026-05-07) documents an active 14+ month supply-chain compromise operation. Per the evidence-minimum table, Cap=4 requires "1 A-grade source OR 2 B-grade sources" — threshold met by ESET alone. Operator-side persistence from at least November 2024 through ESET December 2025 disclosure indicates operational supply-chain tradecraft. Cap=5 (Significant) is NOT supported because Cap=5 requires "multiple A-grade sources" — supply-chain capability assessment rests on Sqgame alone. Historical APT37 supply-chain operations prior to Sqgame are not directly documented in the cited record.

**Sources:** eset-via-the-record-2026-05-07

### Modifiers

- **Willingness (-0):** no-constraints — DPRK baseline
- **Novelty (-0):** custom-advanced — compromise of legitimate platform with web-browser-download distribution channel that bypasses Google Play vetting; sideload-warning is the sole friction. Defensive difficulty high.

### First-party Splunk

🟢 No first-party IOC hits at time of scoring (2026-05-10).

---

## Destructive

**Intent 1/5** (target-of-opportunity) · **Capability 1/5** (not-capable, post-novelty) · **Composite: 2/10** · **🟢 LOW**

### Why this Intent score

Intent=1 (Target of Opportunity / floor). NO public reporting documents APT37 conducting destructive operations against any victim, in any sector, at any time. The mission profile is intelligence collection / civil-society coercion / defector tracking — confidentiality-tier objectives, not integrity-tier. Intent=1 is the floor and the honest read.

**Sources:** fireeye-apt37-reaper-2018

### Why this Capability score

Capability=2 (Possible) base — FireEye 2018 documents RUHAPPY as suspected wiper / MBR-overwrite capability in the APT37 arsenal. This is capability-EXISTENCE evidence at A-grade source tier. NO public reporting documents APT37 deploying RUHAPPY operationally. Capability=2 captures "feasibility confirmed, very limited evidence." Final Capability lands at 1 after Novelty=-1.

**Sources:** fireeye-apt37-reaper-2018

### Modifiers

- **Willingness (-0):** no-constraints — DPRK baseline
- **Novelty (-1):** semi-custom — RUHAPPY is APT37-attributed legacy tooling per FireEye 2018; semi-custom rather than custom-advanced given the tool's age and lack of subsequent reported iteration or deployment.

### First-party Splunk

🟢 No first-party IOC hits at time of scoring (2026-05-10).

---

## Disruptive

**Intent 1/5** (target-of-opportunity) · **Capability 1/5** (not-capable) · **Composite: 2/10** · **🟢 LOW**

### Why this Intent score

Intent=1 (floor). No documented disruptive operations against any target. Mission profile is collection / coercion — neither category drives availability-tier disruption.

### Why this Capability score

Capability=1 (Not Capable). No evidence APT37 conducts disruptive operations (DDoS, ransom-style availability denial, ICS-disruption, telecom-disruption). Arsenal does not include disruption-purposed tooling.

### Modifiers

- **Willingness (-0):** no-constraints — DPRK baseline
- **Novelty (-2):** commodity placeholder — if disruptive activity were to occur it would likely use commodity tooling not present in current documented arsenal.

### First-party Splunk

🟢 No first-party IOC hits at time of scoring (2026-05-10).

---

## Cyber-Crime

**Intent 1/5** (target-of-opportunity) · **Capability 1/5** (not-capable) · **Composite: 2/10** · **🟢 LOW**

### Why this Intent score

Intent=1 (floor). APT37 is state-aligned MSS espionage (per ESET 2026 framing) — NOT financially-motivated. Distinct from RGB-attributed Lazarus and Stardust Chollima, which DO carry DPRK financial-revenue-generation tasking (cryptocurrency theft, SWIFT-targeting, fraudulent IT-worker schemes). No public reporting documents APT37 conducting financial-revenue operations.

**Sources:** eset-via-the-record-2026-05-07, fireeye-apt37-reaper-2018

### Why this Capability score

Capability=1 (Not Capable). No public reporting documents APT37 conducting financially-motivated operations of any kind — no ransomware, no cryptocurrency theft, no payment-card theft, no fraud. Arsenal does not include financially-monetizable tooling. Capability=1 is the structural floor for state-aligned MSS espionage actors.

### Modifiers

- **Willingness (-0):** no-constraints — DPRK baseline
- **Novelty (-2):** commodity placeholder — no documented cyber-crime tooling.

### First-party Splunk

🟢 No first-party IOC hits at time of scoring (2026-05-10).

---

## Review policy

- **Interval:** 90 days
- **Last reviewed:** 2026-05-10
- **Next review due:** 2026-08-08
- **Early review triggers:**
  - **New attribution from A-grade source** — second A/B-grade vendor corroborating ESET's Sqgame attribution would lift the single-source veto on that campaign-specific finding
  - New tooling documented
  - CVE exploitation linked to actor
  - Major campaign disclosure
  - First-party IOC observation (any first-party Splunk hit on APT37 indicators)
  - **A&D-direct targeting disclosure** — would materially shift Espionage Intent from 3 toward 5 against the A&D target profile

---

## Methodology note

Scored per `doctrine/THREAT-BOX-METHODOLOGY.md` (Piazza SANS framework adapted for A&D). Target profile: `ad-prime-v1` (mid-to-large US A&D contractor, ITAR-regulated, DoD contracts).

**Authority gate:** weighted overall MEDIUM (4.9) → `actor-profiler-autonomous-with-notification`. Hard Rule 5 (HIGH gate) did NOT fire. Auto-committed.

**Source-finding confidence binding:** scoring confidence on the Sqgame-specific 2026 campaign is capped by single-source-veto on finding-2026-05-07-0004. Historical multi-vendor capability assessment is not single-source-bound and supports Capability=5 on its own evidence basis.

**A&D-relevance binding:** the methodologically honest move is to score Espionage Intent against the A&D target profile based on documented A&D-direct targeting (currently: NONE per public reporting), not against APT37's dominant target profile (civil society / defectors / Korean-language journalists / DPRK-policy researchers). Method-portability and structural-risk arguments inform secondary scoring elements (Capability, Novelty modifiers) but do NOT inflate Intent. Per Hard Rule 2: scoring grounds in cited sources, not Archimedes-originated extrapolation.

**Workflow validation note:** This is the FIFTH consecutive non-HIGH outcome in the recent /update-tracking series — UNC1549 5.4 MEDIUM, Charming Kitten 4.45 LOW, MuddyWater 4.15 LOW, APT34 4.9 MEDIUM, APT37 4.9 MEDIUM. Empirical pattern: actors whose documented targeting is regional / sector-broad / civil-society / dissident-diaspora cap at Intent=3-4, producing espionage composites 7-8 (MEDIUM to HIGH at category tier), and the four other categories at floor for state-aligned espionage actors dilute via doctrine weighting to overall MEDIUM or LOW. The HIGH overall threshold (band 8-10 rounded) effectively requires either (a) Intent=5 in espionage on documented A&D-direct targeting AND high marks in another category, or (b) HIGH-tier composites in two or more weighted-significant categories. The methodology refuses to invent A&D-direct targeting where evidence does not support it.

---

*Generated from `threat-box.yaml`. To update, re-run `threat-box-scoring` skill via `/update-tracking 024` and regenerate. See [profile.md](./profile.md) for full actor dossier; see [iocs.md](./iocs.md) and [iocs.yaml](./iocs.yaml) for indicator set.*
