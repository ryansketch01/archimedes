# Threat Box — Charming Kitten / Mint Sandstorm

**Actor ID:** 011
**Target profile:** ad-prime-v1 (mid-to-large US A&D contractor, ITAR-regulated)
**Scored:** 2026-05-09 by `actor-profiler` (run via `/update-tracking` Mode 2)
**Approval:** auto-committed (LOW overall — no `/approve-scoring` gate engaged)
**Overall Threat Level:** 🟢 **LOW** (weighted 4.45/10)
**Primary threat vector:** Espionage (composite 9 — category-level 🔴 HIGH)

---

## Summary

Charming Kitten / Mint Sandstorm is assessed as an overall **LOW** threat to the Archimedes target profile (`ad-prime-v1`), driven entirely by the Espionage category which scores 🔴 HIGH at composite 9. The four non-espionage categories all sit at floor (LOW, composite 2), and the doctrine weighting (Espionage 35%, Supply Chain 20%, Destructive/Disruptive/Cyber-Crime 15% each) yields a weighted overall of 4.45 — which rounds to 4 and falls in the LOW band (2-4).

**The operator-anticipated outcome was HIGH; the disciplined computation lands LOW.** This is the red-team `qualify` directive on [finding-2026-05-05-0002](../../findings/finding-2026-05-05-0002.md) doing precisely what it was meant to do: preventing over-scoring on Espionage Intent by binding the score against the named victim ecosystem (US/UK/Israeli defense-policy think tanks, Iran-nuclear researchers, MENA security journalists) rather than extrapolating to ad-prime-v1 targeting that no A-grade source has documented.

Intent=4 (Ideology Association) is the binding scoring outcome — NOT Intent=5 (Target-Specific). Per the methodology evidence-minimum table, Intent=5 requires "at least 1 A-grade source documenting targeting of our specific profile." That source does not exist for Charming Kitten in the current corpus. The 2026-05-04 vendor reporting names think-tank, academic, and journalist victims; no defense primes. The platform-portable OAuth consent-grant tradecraft is a Capability/Novelty consideration, not Intent against ad-prime-v1.

### Per-category breakdown

| Category | Composite | Level |
|---|---|---|
| Espionage (35%) | 9/10 | 🔴 HIGH |
| Supply Chain (20%) | 2/10 | 🟢 LOW |
| Destructive (15%) | 2/10 | 🟢 LOW |
| Disruptive (15%) | 2/10 | 🟢 LOW |
| Cyber-Crime (15%) | 2/10 | 🟢 LOW |

**Weighted computation:**
```
espionage:    9 × 0.35 = 3.15
supply_chain: 2 × 0.20 = 0.40
destructive:  2 × 0.15 = 0.30
disruptive:   2 × 0.15 = 0.30
cyber_crime:  2 × 0.15 = 0.30
                       ------
weighted_score:          4.45 → rounds to 4 → LOW (band 2-4)
```

---

## Espionage

**Intent 4/5** (ideology-association) · **Capability 5/5** (significant) · **Composite: 9/10** · **🔴 HIGH**

### Why this Intent score

Intent=4 (Ideology Association) is the binding-with-red-team-qualify scoring outcome, NOT Intent=5 (Target-Specific). The Q2 2026 vendor reporting (CrowdStrike + MSTIC 2026-05-04, both A-grade) explicitly names victims as US/UK/Israeli defense-policy think tanks (Brookings, RUSI, Atlantic Council), Iran-nuclear-program researchers, and MENA-security journalists. NO defense primes are named as victims.

Per the methodology evidence-minimum table, Intent=5 requires "at least 1 A-grade source documenting targeting of ad-prime-v1 specifically" — that source does not exist for Charming Kitten in the current corpus. Extrapolating from the named think-tank victim list to ad-prime-v1 targeting is exactly what the red-team `qualify` directive on finding-2026-05-05-0002 prohibits ("brief must NOT characterize prime-direct OAuth-consent activity as observed or attributed; treat it strictly as a generalizable mechanism-level risk").

Intent=4 (Ideology Association) is well-supported by 2 A-grade sources (CrowdStrike + MSTIC concurrent 2026-05-04 attribution) documenting sustained 2014-2026 IRGC-IO ideology-driven targeting of the Iran-policy ecosystem (think tanks, researchers, journalists, dissidents). The motivation chain is unambiguous: Iran-policy formation in the West → policy advisors and researchers who shape it → IRGC-IO collection priority. This is ideology-association targeting (anti-Iran-policy-formation, anti-Western), not sector-association (Charming Kitten does NOT target the broader defense/manufacturing sector indiscriminately) and not target-specific (no documented prime-direct targeting).

A&D-prime relevance is second-order and mechanism-portability-driven — the OAuth consent-grant tradecraft is platform-generic and would apply to any Entra ID tenant — but mechanism portability is a Capability/Novelty consideration, NOT an Intent consideration against ad-prime-v1. Per the source finding's red-team review: "tradecraft portability is plausible-but-not-evidenced" against primes specifically.

**Sources:** [finding-2026-05-05-0002](../../findings/finding-2026-05-05-0002.md), CrowdStrike 2026-05-04, MSTIC 2026-05-04

### Why this Capability score

Capability=5 minimum requires "Multiple A-grade sources AND documented active use within last 24 months." Both met decisively:

**(1) Multi-source A-grade lineage spanning 2014-2026** — CrowdStrike (2026-05-04 concurrent attribution + prior Charming Kitten tracking), Microsoft MSTIC (2026-05-04 + sustained Phosphorus/Mint Sandstorm tracking), Mandiant (HYPERSCRAPE original 2022 disclosure + APT35/G0059 baseline), Google TAG (Iran-cyber quarterly reporting), CERTFA (long-running Iranian-dissident-targeting documentation), and US government / DOJ reporting (2017 Mesri indictment context).

**(2) Active use within 24 months** — the Q2 2026 campaign (Feb–Apr 2026) is by definition active within the window. Evidence covers full kill-chain: initial access (LinkedIn / fake-conference / fake-research-collaboration personas + OAuth phishing landings on Microsoft-lookalike domains), execution (updated PowerShell loader per CrowdStrike), persistence (T1528 OAuth application access tokens via attacker-controlled "Policy Review Tool" app — survives password resets), credential access (HYPERSCRAPE 2026 variant — first publicly-documented update since 2022), defense evasion (lookalike domains, deceptive OAuth app display names), collection / exfil (HYPERSCRAPE mailbox download via captured tokens; T1567 cloud-hosted credential exfiltration C2).

The HYPERSCRAPE 2022 → 2026 update arc and the OAuth consent-grant tradecraft pivot together demonstrate sustained capability evolution — not a one-off campaign, but a maturing operational program.

**Sources:** [finding-2026-05-05-0002](../../findings/finding-2026-05-05-0002.md), CrowdStrike 2026-05-04, MSTIC 2026-05-04, Mandiant HYPERSCRAPE 2022, MITRE G0059

### Modifiers

- **Willingness (-0):** no-constraints — Iran (IRGC-IO cluster) — strained US relations, active sanctions, no diplomatic constraints on cyber-espionage operations. Doctrine willingness floor for Russia/China/Iran/DPRK clusters.
- **Novelty (-0):** custom-advanced — HYPERSCRAPE is an operator-controlled custom credential-and-mailbox-exfiltration tool not publicly observed in non-Charming-Kitten hands. The 2026 variant is custom-evolved tooling, not commodity. The OAuth consent-grant tradecraft (T1528) is a platform-leveraging persistence path requiring custom attacker-app registration with deceptive display names and tailored social-engineering pretext — defenders cannot rely on commodity AV signatures because the persistence artifact is an Entra ID application registration, not a malware binary. The novelty-as-defensive-difficulty framing per doctrine fits.

### First-party Splunk

🟡 **Silent across both indices.** First-party Splunk negative: queried `archimedes` + `defenseclaw_local` for all 6 published IOCs (login-microsoft365-secure.com, m365-policy-review.org, hyperscrape-update.net, 194.87.44.99, HYPERSCRAPE 2026 SHA256, "Policy Review Tool" OAuth app pattern) over -30d on 2026-05-09. Zero hits across both indices. Also queried OAuth consent-grant audit-log signals (Mail.ReadWrite, Consent to application) — zero hits. Per Hard Rule 8 doctrine: silent telemetry is not contradicting evidence; first-party precedence not invoked; no Capability bonus applied.

This is the most defensively consequential indicator class in the dossier — a future first-party hit on the OAuth consent-grant pattern would be especially actionable and would trigger immediate review-cycle re-engagement.

---

## Supply Chain

**Intent 1/5** (target-of-opportunity) · **Capability 1/5** (not-capable) · **Composite: 2/10** · **🟢 LOW**

### Why this Intent score

Intent floor (=1). The Supply Chain category per doctrine asks "Can/will they compromise our suppliers, contractors, or shared software to reach us?" — i.e., classic supply-chain compromise. The OAuth consent-grant tradecraft is NOT a supply-chain mechanism; it is a direct user-consent attack against the target tenant's own users (or those of a peer/partner organization). It does not compromise a supplier or shared-software dependency to reach the target. The think-tank → prime lateral-pretext hypothesis (ACH H2 in finding-2026-05-05-0002) is also NOT classic supply chain — it is social engineering via a compromised peer in the same ecosystem, not a supplier compromise.

No documented Charming Kitten supply-chain operations against A&D primes or their suppliers exist in the public reporting corpus. Charming Kitten's mission profile is persona-driven credential-phishing for direct intelligence collection — not supply-chain access brokering or shared-software compromise. Floor scoring is correct and disciplined.

**Methodology surfacing note:** the operator request flagged "around Supply-chain since OAuth consent doesn't fit the classic supply-chain-compromise definition" — confirmed. Supply Chain category does NOT capture the OAuth consent-grant risk, which is Espionage-mechanism-portability and lives in the Espionage scoring narrative. Avoiding the temptation to inflate Supply Chain Intent to capture mechanism-portability is correct doctrine application.

### Why this Capability score

Capability=1 floor — no documented Charming Kitten supply-chain capability in the public reporting corpus. The doctrine red-flag check applies: the temptation to score Capability=3 "because nation-states can do supply-chain ops" is explicitly disqualified by methodology — that is not evidence of capability X. HYPERSCRAPE and the OAuth-consent tradecraft are direct-target tools, not supply-chain compromise tools.

### Modifiers

- **Willingness (-0):** no-constraints — Iran/IRGC-IO — willingness floor irrespective of category; no diplomatic brake on supply-chain operations if cluster pivoted, but no current intent.
- **Novelty (-0):** custom-advanced — N/A; no supply-chain capability scored.

### First-party Splunk

No first-party Splunk hits; no supply-chain-specific IOCs in the published indicator set.

---

## Destructive

**Intent 1/5** (target-of-opportunity) · **Capability 1/5** (not-capable) · **Composite: 2/10** · **🟢 LOW**

### Why this Intent score

Intent floor (=1). No documented destructive operations attributed to Charming Kitten across CrowdStrike, MSTIC, Mandiant, Google TAG, or CERTFA reporting from 2014 through 2026. The IRGC-IO mission profile is intelligence collection — persona-driven credential harvest and mailbox content extraction. Iranian destructive operations sit in MOIS-aligned clusters (MuddyWater, roster ID 022) and MOIS-adjacent hacktivist clusters (Handala Hack, roster ID 014) — distinct service tasking, distinct mission profiles. Charming Kitten's profile.md captures this distinction explicitly.

### Why this Capability score

Capability=1 floor. No evidence of Charming Kitten destructive capability (wipers, integrity-corruption tooling) in the public reporting corpus. Doctrine red-flag check applies — capability is not estimated upward without evidence.

### Modifiers

- **Willingness (-0):** no-constraints — Iran/IRGC-IO — willingness floor.
- **Novelty (-0):** custom-advanced — N/A; no destructive capability scored.

### First-party Splunk

No first-party Splunk hits; no destructive-mode IOCs.

---

## Disruptive

**Intent 1/5** (target-of-opportunity) · **Capability 1/5** (not-capable) · **Composite: 2/10** · **🟢 LOW**

### Why this Intent score

Intent floor (=1). No documented disruptive operations (DDoS, availability-denial, ICS/OT-targeting) attributed to Charming Kitten in the public reporting corpus. The cluster's documented operational mode is sustained low-volume credential-phishing for intelligence collection — not availability denial. Charming Kitten does not appear in IRGC operational repertoires that include disruptive ops; that profile sits with Sandworm-class actors (Russia) and is distinct from IRGC-IO mission tasking.

### Why this Capability score

Capability=1 floor. No documented evidence of Charming Kitten disruptive capability against A&D-relevant infrastructure. Doctrine red-flag check: nation-state status does not count as evidence of capability X.

### Modifiers

- **Willingness (-0):** no-constraints — Iran/IRGC-IO — willingness floor.
- **Novelty (-0):** custom-advanced — N/A; no disruptive capability scored.

### First-party Splunk

No first-party Splunk hits; no disruptive-mode IOCs.

---

## Cyber-Crime

**Intent 1/5** (target-of-opportunity) · **Capability 1/5** (not-capable) · **Composite: 2/10** · **🟢 LOW**

### Why this Intent score

Intent floor (=1). Charming Kitten is an IRGC-IO state-intelligence cluster — espionage and intelligence collection motivation. No documented financially-motivated operations (ransomware, extortion, BEC, IP-resale) attributed to the cluster in the public reporting corpus. Iranian financially-motivated cyber sits in distinct ecosystem clusters (criminal-affiliated, MOIS-adjacent monetization operations), not within the IRGC-IO mission profile. Floor scoring is correct.

### Why this Capability score

Capability=1 floor. No documented evidence of Charming Kitten cyber-crime capability.

### Modifiers

- **Willingness (-0):** no-constraints — Iran/IRGC-IO — willingness floor.
- **Novelty (-0):** custom-advanced — N/A; no cyber-crime capability scored.

### First-party Splunk

No first-party Splunk hits; no cyber-crime IOCs.

---

## Confidence

**Admiralty:** A1 — inherits from [finding-2026-05-05-0002](../../findings/finding-2026-05-05-0002.md) (concurrent A-grade independent corroboration: CrowdStrike + Microsoft MSTIC publish 2026-05-04 with separate evidence bases; neither cites the other; corroboration test passes).

**Caveats:**
- Red-team `qualify` directive on the source finding is binding — Espionage Intent must NOT extrapolate think-tank victims into prime-direct targeting. This binding is preserved in the Intent=4 scoring.
- First-party Splunk silent across all 6 IOCs and OAuth consent-grant audit-log patterns over -30d. Silent telemetry is not contradicting; no IOC bonus.
- The ACH H3 leader (tradecraft-portability) on the source finding is at WEP "likely" — sufficient for forward-defensive language on Capability/Novelty but NOT for Intent escalation.
- KAC A1 (prime-tier Entra audit-log coverage) classified `test` on the source finding; remains a coverage attestation question not blocking. A future Splunk hit on OAuth consent-grant audit events would invoke first-party precedence and trigger immediate review-cycle re-engagement.

---

## Review policy

- **Interval:** 90 days
- **Last reviewed:** 2026-05-09
- **Next review due:** 2026-08-07
- **Early review triggers:**
  - New attribution from A-grade source (especially independent third-party corroboration of OAuth consent-grant tradecraft beyond MSTIC)
  - New tooling documented (HYPERSCRAPE 2026+ further variants; new persistence paths)
  - CVE exploitation linked to actor
  - Major campaign disclosure (especially any vendor follow-up disclosing prime-tier OAuth consent-grant events — would invoke ACH tripwire from source finding)
  - **First-party IOC observation** (would invoke Hard Rule 8 first-party precedence; especially consequential for OAuth consent-grant audit-log patterns)

---

## Methodology note

Scored per `doctrine/THREAT-BOX-METHODOLOGY.md` (Piazza SANS framework adapted for A&D). Target profile: `ad-prime-v1` (mid-to-large US A&D contractor, ITAR-regulated, DoD contracts).

**Authority:** auto-committed (LOW overall — `actor-profiler-autonomous`). The Hard Rule 5 `/approve-scoring` gate is keyed on weighted overall, not on per-category HIGH. Espionage composite 9 (HIGH) is preserved in the per-category table for analytical use but does NOT trigger the gate.

**Methodology surfacing note carried into this scoring:**

1. **Espionage Intent calibration (4 vs 5):** the disciplined Intent=4 (Ideology) reflects the red-team `qualify` directive's binding constraint. Intent=5 (Target-Specific) would have required at least one A-grade source documenting targeting of ad-prime-v1 specifically; vendors named only think-tank/academic/journalist victims. This is the primary judgment call that produces LOW overall vs the operator-anticipated HIGH.

2. **Supply Chain category fit:** OAuth consent-grant tradecraft does NOT fit the classic supply-chain-compromise definition (compromise of a supplier or shared-software dependency to reach a target). It is direct user-consent attack and lives in the Espionage scoring narrative as Capability/Novelty. Floor scoring on Supply Chain is correct doctrine application; resisting the temptation to inflate Supply Chain Intent to capture mechanism-portability is part of the discipline.

3. **First-party silence is not contradiction:** zero hits across 6 IOCs and OAuth consent-grant audit-log patterns over -30d does not invoke Hard Rule 8 first-party precedence; it is silent telemetry. Future hits would change the picture materially.

---

*Generated from `threat-box.yaml`. To update, re-run `threat-box-scoring` skill via `/update-tracking` and regenerate. See [profile.md](./profile.md) for full actor dossier.*
