# Threat Box — UNC1549

**Actor ID:** 004
**Target profile:** ad-prime-v1 (mid-to-large US A&D contractor, ITAR-regulated)
**Scored:** 2026-05-09 by `actor-profiler`
**Approval:** auto-committed (weighted overall MEDIUM — Hard Rule 5 gate not engaged)
**Overall Threat Level:** 🟡 MEDIUM (weighted 5.4/10)
**Primary threat vector:** Espionage (category-level 🔴 HIGH, composite 10)

---

## Summary

UNC1549 is assessed as an overall **🟡 MEDIUM** threat to the Archimedes target profile (`ad-prime-v1`), driven entirely by **espionage** — which scores at the category ceiling (composite 10, 🔴 HIGH) on direct A&D-prime targeting and significant custom-tooling capability. The weighted overall lands at MEDIUM because UNC1549's non-espionage attack categories sit at floor (Destructive, Disruptive, Cyber-Crime all 🟢 LOW; Supply Chain 🟡 MEDIUM on dated Tortoiseshell precedent), and the doctrine weighting (espionage 35%, supply-chain 20%, destructive/disruptive/cyber-crime 15% each) dilutes the dominant espionage composite.

Per `doctrine/THREAT-BOX-METHODOLOGY.md` and the threat-box-scoring skill, the Hard Rule 5 `/approve-scoring` gate is keyed on the **weighted overall** only, not on any category-level HIGH. UNC1549's espionage composite of 10 is preserved in the per-category breakdown for situational awareness — defensive prioritization should treat UNC1549 as a top-tier espionage threat against A&D primes regardless of the overall MEDIUM label.

### Per-category breakdown

| Category | Composite | Level |
|---|---|---|
| Espionage (35%) | 10/10 | 🔴 HIGH |
| Supply Chain (20%) | 5/10 | 🟡 MEDIUM |
| Destructive (15%) | 2/10 | 🟢 LOW |
| Disruptive (15%) | 2/10 | 🟢 LOW |
| Cyber-Crime (15%) | 2/10 | 🟢 LOW |

**Weighted overall computation:** `10×0.35 + 5×0.20 + 2×0.15 + 2×0.15 + 2×0.15 = 3.50 + 1.00 + 0.30 + 0.30 + 0.30 = 5.40` → MEDIUM (5-7 band, rounded = 5).

---

## Espionage

**Intent 5/5** (target-specific) · **Capability 5/5** (significant) · **Composite: 10/10** · **🔴 HIGH**

### Why this Intent score

Mandiant 2026-05-04 (A-grade) explicitly documents UNC1549's Feb-Apr 2026 recruiter-lure campaign targeting categories that map directly onto the `ad-prime-v1` profile: "a major US space and defense contractor" and "a European missile systems integrator." This is targeting based on objectives achievable ONLY within A&D primes (classified/sensitive R&D, ITAR-controlled programs, missile-systems IP). Per methodology evidence-minimum table, Intent=5 requires "at least 1 A-grade source documenting targeting of our specific profile" — the single-A-grade-source threshold is met by Mandiant.

The WEP cap of "likely" applied via single-source veto in [finding-2026-05-05-0001](../../findings/finding-2026-05-05-0001.md) caps Archimedes confidence in the attribution itself; it does **not** modify the underlying targeting-evidence grade for purposes of the threat-box minimum. Backstopped by the Mandiant 2024 baseline, Symantec 2019 (Tortoiseshell IT-supplier compromise with aviation-customer downstream), and analyst SAT-ACH on the 2026-05 finding (H1 = UNC1549-as-claimed scored zero inconsistencies across eight evidence rows).

**Sources:** [finding-2026-05-05-0001](../../findings/finding-2026-05-05-0001.md), Mandiant 2026-05-04, Mandiant 2024 baseline, Symantec Tortoiseshell 2019.

### Why this Capability score

Capability=5 minimum requires multiple A-grade sources AND documented active use within last 24 months. Both conditions are met:

1. **Multi-source A-grade lineage** — Mandiant (2024 baseline + 2026-05-04 expansion), Microsoft (Smoke Sandstorm tracking), CrowdStrike (Imperial Kitten tracking), and Symantec (Tortoiseshell 2019 attribution).
2. **Active use within 24 months** — the Feb-Apr 2026 campaign is, by definition, active within the window. MINIBIKE C2 protocol reuse from 2024-2025 ops is one of Mandiant's three attribution pillars for the 2026 expansion.

Capability evidence covers the full kill-chain: initial access (LinkedIn recruiter persona + lookalike careers portals + weaponized .lnk via cloud storage), execution (PowerShell + custom MINIBIKE), persistence (registry Run keys, scheduled tasks), credential access (custom Outlook profile credential harvester documented in Mandiant 2026-05), C2 (HTTPS to UNC1549 domains with Let's Encrypt 7-day cycling), collection/exfil (Outlook email harvest + C2 channel exfil).

**Sources:** [finding-2026-05-05-0001](../../findings/finding-2026-05-05-0001.md), Mandiant 2026-05-04, Mandiant 2024 baseline, Microsoft Smoke Sandstorm, CrowdStrike Imperial Kitten, Symantec Tortoiseshell 2019.

### Modifiers

- **Willingness (-0):** no-constraints — Iran (IRGC-aligned) — strained US relations, active sanctions, no diplomatic constraints on cyber-espionage operations against US defense industrial base.
- **Novelty (-0):** custom-advanced — Custom MINIBIKE backdoor + MINIBUS loader + Outlook profile credential harvester. Per Mandiant 2026-05-04 and ACH evidence E5 in [finding-2026-05-05-0001](../../findings/finding-2026-05-05-0001.md), the toolchain is not publicly observed in non-UNC1549 hands. Detection signatures are limited to vendor/community sharing rather than commodity AV coverage.

### First-party Splunk

No first-party IOC hits at time of scoring. Queried `archimedes` and `defenseclaw_local` indices for all 11 IOCs (4 domains, 2 IPv4, 2 SHA256, 1 URL, 1 persona email, MINIBIKE/MINIBUS strings) over -30d on 2026-05-09. Zero hits across both indices. Per Hard Rule 8 doctrine, silent telemetry is not contradicting evidence; first-party precedence is not invoked; no Capability bonus applied.

---

## Supply Chain

**Intent 2/5** (regional-association) · **Capability 3/5** (limited) · **Composite: 5/10** · **🟡 MEDIUM**

### Why this Intent score

UNC1549's 2026 campaign is direct recruiter-lure against A&D primes, not supply-chain-mediated. Historical Tortoiseshell precedent (Symantec 2019) documented IT-supplier compromise with aviation customers downstream — a sector-association supply-chain pattern — but this is dated and has not visibly persisted into the 2024-2026 UNC1549 tradecraft signature. Mandiant 2026-05-04 reporting frames the cluster's current operational mode as direct-prime targeting, not supplier-pivot.

Intent scored at Regional Association rather than Sector Association because current evidence does not show UNC1549 actively pursuing A&D supply-chain compromise — the 2019 precedent is too old and tradecraft has demonstrably shifted to direct-prime recruiter-lure. Doctrine red-flag: scoring Intent=3 on the basis that "UNC1549 once did supply-chain in 2019 so they might again" would be inflation against the evidence-minimum.

**Sources:** Symantec Tortoiseshell 2019, [finding-2026-05-05-0001](../../findings/finding-2026-05-05-0001.md).

### Why this Capability score

Capability=3 (Limited) reflects the historical Symantec 2019 attribution of Tortoiseshell IT-supplier compromise — feasibility confirmed via documented prior activity, but limited to one documented campaign era and now ~6 years stale. The custom MINIBIKE/MINIBUS toolchain is reusable across operational modes if UNC1549 chose to pivot back to supplier compromise, but no current evidence of supply-chain capability deployment in 2024-2026 reporting.

**Sources:** Symantec Tortoiseshell 2019.

### Modifiers

- **Willingness (-0):** no-constraints — same posture as espionage; no diplomatic constraints if supply-chain operations resumed.
- **Novelty (-0):** custom-advanced — if supply-chain mode were resumed, the custom MINIBIKE/MINIBUS toolchain would carry forward.

### First-party Splunk

No first-party IOC hits. No supply-chain-specific IOCs in the published 11-indicator set; the IOCs cover delivery, C2, and persona infrastructure for the direct-prime campaign.

---

## Destructive

**Intent 1/5** (target-of-opportunity) · **Capability 1/5** (not-capable) · **Composite: 2/10** · **🟢 LOW**

### Why this Intent score

No documented destructive operations attributed to UNC1549 in Mandiant 2024 baseline, Mandiant 2026-05-04 expansion, Microsoft Smoke Sandstorm tracking, CrowdStrike Imperial Kitten tracking, or Symantec Tortoiseshell historical reporting. Profile.md notes destructive operations sit in adjacent Iranian clusters (MOIS-aligned MuddyWater roster ID 022, MOIS-adjacent Handala Hack roster ID 014), not within the UNC1549 (IRGC-aligned) cluster's documented mission profile.

Intent=1 (Target-of-Opportunity) is the doctrine floor; no evidence of targeted destructive intent against `ad-prime-v1`.

**Sources:** none — absence of destructive evidence in the corpus.

### Why this Capability score

No evidence of UNC1549 destructive capability in the public reporting corpus. Capability=1 is the doctrine floor when no documented capability exists. Doctrine red-flag check: the temptation to score Capability=3 "because nation-states can do destructive ops" is explicitly disqualified by the methodology — that's not evidence of capability X.

**Sources:** none.

### Modifiers

- **Willingness (-0):** no-constraints — Iran/IRGC willingness floor irrespective of category.
- **Novelty (-0):** custom-advanced — N/A; no destructive capability scored.

### First-party Splunk

No first-party IOC hits; no destructive-mode IOCs in the published indicator set.

---

## Disruptive

**Intent 1/5** (target-of-opportunity) · **Capability 1/5** (not-capable) · **Composite: 2/10** · **🟢 LOW**

### Why this Intent score

No documented disruptive operations (DDoS, network-availability attacks, ICS/OT disruption) attributed to UNC1549 across the public reporting corpus. UNC1549's documented operational mode is sustained low-volume espionage, not availability denial.

Intent=1 (Target-of-Opportunity) reflects the absence of disruptive intent evidence.

**Sources:** none.

### Why this Capability score

No documented evidence of UNC1549 disruptive capability against A&D-relevant infrastructure. Capability=1 floor per doctrine — no evidence is not estimated upward.

**Sources:** none.

### Modifiers

- **Willingness (-0):** no-constraints — Iran/IRGC willingness floor.
- **Novelty (-0):** custom-advanced — N/A; no disruptive capability scored.

### First-party Splunk

No first-party IOC hits; no disruptive-mode IOCs.

---

## Cyber-Crime

**Intent 1/5** (target-of-opportunity) · **Capability 1/5** (not-capable) · **Composite: 2/10** · **🟢 LOW**

### Why this Intent score

UNC1549 is an IRGC-aligned nation-state cluster with espionage and long-term-access motivation per Mandiant. No documented financially-motivated operations (ransomware, extortion, BEC, IP-resale). Iranian financially-motivated cyber sits in MOIS-adjacent and criminal ecosystem clusters, not within UNC1549's mission profile.

Intent=1 floor — no evidence of cyber-crime intent against `ad-prime-v1`.

**Sources:** none.

### Why this Capability score

No documented evidence of UNC1549 cyber-crime capability. Capability=1 floor per doctrine.

**Sources:** none.

### Modifiers

- **Willingness (-0):** no-constraints — Iran/IRGC willingness floor.
- **Novelty (-0):** custom-advanced — N/A; no cyber-crime capability scored.

### First-party Splunk

No first-party IOC hits; no cyber-crime IOCs.

---

## Confidence

- **Admiralty grade:** A2 (inherited from [finding-2026-05-05-0001](../../findings/finding-2026-05-05-0001.md): Mandiant A-grade source with single-source veto applied; WEP capped at "likely")
- **ACH outcome:** H1 (UNC1549-as-Mandiant-claims) scored zero inconsistencies across eight evidence rows; nearest competing hypothesis (H4 false-flag) accumulated two inconsistencies
- **KAC outcome:** seven assumptions surfaced — three sound, three to qualify, one to test (A4 coverage attestation, async; not blocking this scoring run)
- **Brittleness flags:** TLS-issuance attribution pillar (Let's Encrypt 7-day cycling) is the most replicable adversary-mimicry vector; MINIBIKE source-code leak (currently no evidence) would force re-examination of all UNC1549-attributed activity per ACH tripwire

---

## Review policy

- **Interval:** 90 days
- **Last reviewed:** 2026-05-09
- **Next review due:** 2026-08-07
- **Early review triggers:**
  - New attribution from A-grade source (e.g., Unit 42, MSTIC, CrowdStrike independently corroborate Mandiant 2026-05-04 — would lift single-source veto, WEP could move to "very likely")
  - New tooling documented
  - CVE exploitation linked to actor
  - Major campaign disclosure (e.g., follow-on Mandiant or peer reporting on the 2026 expansion)
  - First-party IOC observation (any of the 11 IOCs in `defenseclaw_local` or `archimedes` would invoke first-party precedence and trigger immediate rescoring + FLASH consideration)

---

## Methodology note

Scored per `doctrine/THREAT-BOX-METHODOLOGY.md` (Piazza SANS framework adapted for A&D). Target profile: `ad-prime-v1` (mid-to-large US A&D contractor, ITAR-regulated, DoD contracts).

**Authority gate:** weighted overall MEDIUM (5.4) lands in the `actor-profiler-autonomous-with-notification` band — auto-commit with Discord `#actor-review` FYI per doctrine. Espionage category-level HIGH (composite 10) does NOT trigger the Hard Rule 5 `/approve-scoring` gate; only the weighted overall does.

---

*Generated from `threat-box.yaml`. To update, re-run `threat-box-scoring` skill and regenerate. See [profile.md](./profile.md) for full actor dossier.*
