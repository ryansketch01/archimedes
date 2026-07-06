# Threat Box — Icarus

**Actor ID:** 025
**Target profile:** ad-prime-v1
**Scored:** 2026-07-06 by `actor-profiler`
**Approval:** auto-committed (LOW — Hard Rule 5 did not fire)
**Overall Threat Level:** 🟢 LOW (weighted 2.2/10)

See [`profile.md`](profile.md) for full actor context.

---

## Summary

Icarus is assessed as an overall 🟢 **LOW** threat to the Archimedes target profile (`ad-prime-v1`), primarily driven by its **Supply Chain** vector (OAuth-integration abuse against downstream Salesforce tenants) — which, at composite 3, is the highest-scoring category but is still LOW.

Every category is capped by three factors: commodity novelty (−2 everywhere; defenders have signatures for legacy-credential and OAuth-token abuse), the absence of any A&D-*directed* targeting (no A-grade source documents targeting of our profile — both named victims are cybersecurity firms), and a thin capability base (single documented campaign, ~2 victims, ~7-week track record, single-IR-vendor B2 attribution). A LOW outcome is the methodology working as designed for a newly-emerged, financially-motivated, commodity-tradecraft extortion actor with no A&D nexus.

> **Read the per-category breakdown alongside the weighted overall.** The Supply Chain category and the structural OAuth-integration exposure pattern are what an A&D defender should watch — not the headline LOW in isolation.

### Per-category breakdown

| Category | Composite | Level |
|---|---|---|
| Espionage (35%) | 2/10 | 🟢 |
| Supply Chain (20%) | 3/10 | 🟢 |
| Destructive (15%) | 2/10 | 🟢 |
| Disruptive (15%) | 2/10 | 🟢 |
| Cyber-Crime (15%) | 2/10 | 🟢 |

---

## Espionage

**Intent 1/5** (target-of-opportunity) · **Capability 1/5** (possible, after −2 novelty) · **Composite: 2/10** · **🟢 LOW**

### Why this Intent score

Icarus is a financially-motivated extortion actor, not an intelligence collector. Data stolen (CRM records, business contacts, price quotes, sales messaging, client names) was harvested to enable extortion. Per the IP-theft disambiguation in the methodology, immediate-monetization theft is Cyber-Crime, not Espionage. No source documents A&D-prime-directed collection; both named victims are cybersecurity firms. Intent=1 (Target of Opportunity).

**Sources:** [finding-2026-06-19-0003](../../findings/finding-2026-06-19-0003-klue-salesforce-supply-chain-compromise-icarus-extortion-group-huntress-recorded-future-named-victims-oauth-token-abuse-net-new-actor-candidate.md)

### Why this Capability score

Feasibility of data theft is demonstrated, but there is no evidence of espionage-grade collection (no long-dwell operations, no targeted IP/R&D theft, no custom collection tooling). Single campaign, ~2 victims. Capability=2 (Possible), reduced to effective 1 by commodity novelty.

**Sources:** finding-2026-06-19-0003

### Modifiers

- **Willingness (−0):** no-constraints — criminal group, no state nexus.
- **Novelty (−2):** commodity — legacy-credential abuse, OAuth-token harvesting, Salesforce REST API via Python-urllib; defenders have signatures for this class.

### First-party Splunk

No first-party IOC hits at time of scoring — Splunk −90d returned a categorical zero (Frank is not a Salesforce-Klue tenant). No bonus applied.

---

## Supply Chain

**Intent 2/5** (regional-association) · **Capability 1/5** (limited, after −2 novelty) · **Composite: 3/10** · **🟢 LOW**

### Why this Intent score

The Icarus campaign IS a supply-chain compromise — it reached victims by compromising a trusted third-party SaaS integration (Klue) and abusing OAuth tokens for downstream Salesforce tenants. But targeting is opportunistic/regional, not A&D-directed: entry was via whichever organizations used the compromised Klue integration, and named victims are cybersecurity firms. Intent=2 (Regional Association) — the highest-substance category, which is why Intent sits at 2 rather than 1.

**Sources:** finding-2026-06-19-0003

### Why this Capability score

Real, documented substance: Icarus compromised a SaaS vendor via a legacy integration credential, harvested OAuth tokens, and used them against downstream customer Salesforce instances. But it is a SINGLE campaign against ONE integration vendor with ~2 disclosed victims — no evidence of repeatable multi-vendor supply-chain operations or of implanting into shared software as a nation-state supply-chain actor would. Capability=3 (Limited), reduced to effective 1 by commodity novelty.

**Sources:** finding-2026-06-19-0003

### Modifiers

- **Willingness (−0):** no-constraints — criminal group.
- **Novelty (−2):** commodity — legacy-credential + OAuth-token abuse against a SaaS integration is a well-documented pattern; defensible via connected-app auditing and OAuth-scope governance.

### First-party Splunk

No first-party IOC hits at time of scoring (categorical Splunk null).

---

## Destructive

**Intent 1/5** (target-of-opportunity) · **Capability 1/5** (not-capable) · **Composite: 2/10** · **🟢 LOW**

### Why this Intent score

No evidence of intent to corrupt, wipe, or damage systems. The campaign was data-theft-plus-extortion with no destructive component. Intent=1.

**Sources:** finding-2026-06-19-0003

### Why this Capability score

No evidence Icarus has performed any destructive attack. Per methodology red-flag guidance, scored 1 (Not Capable) rather than hedged upward.

**Sources:** finding-2026-06-19-0003

### Modifiers

- **Willingness (−0):** no-constraints.
- **Novelty (−2):** commodity default — no destructive tooling documented.

### First-party Splunk

No first-party IOC hits at time of scoring.

---

## Disruptive

**Intent 1/5** (target-of-opportunity) · **Capability 1/5** (not-capable) · **Composite: 2/10** · **🟢 LOW**

### Why this Intent score

No evidence of intent to take systems offline or degrade availability. Covert data theft for extortion, not a disruption operation. Intent=1.

**Sources:** finding-2026-06-19-0003

### Why this Capability score

No evidence of availability attacks (no DDoS, no encryption-for-disruption, no service takedown). Capability=1 (Not Capable).

**Sources:** finding-2026-06-19-0003

### Modifiers

- **Willingness (−0):** no-constraints.
- **Novelty (−2):** commodity default — no disruptive tooling documented.

### First-party Splunk

No first-party IOC hits at time of scoring.

---

## Cyber-Crime

**Intent 1/5** (target-of-opportunity) · **Capability 1/5** (limited, after −2 novelty) · **Composite: 2/10** · **🟢 LOW**

### Why this Intent score

Extortion is Icarus's PRIMARY vector — the category that defines the actor. But intent against the A&D-prime profile specifically is Target-of-Opportunity: Icarus extorted whoever was reachable through the compromised Klue integration; the two named victims are cybersecurity firms. No source documents A&D-prime-directed extortion, so per the evidence-minimum table Intent cannot rise above 1 here. The LOW score reflects lack of A&D-DIRECTED targeting, not absence of extortion capability (captured under Capability).

**Sources:** finding-2026-06-19-0003

### Why this Capability score

Extortion capability is demonstrated ("Mr Brean" persona reached victim employees following data theft), but the track record is thin — ~2 victims, ~7-week emergence horizon, single-IR-vendor (Huntress, B2) attribution, no evidence of a repeatable large-scale operation. Capability=3 (Limited), reduced to effective 1 by commodity novelty.

**Sources:** finding-2026-06-19-0003

### Modifiers

- **Willingness (−0):** no-constraints — criminal extortion group.
- **Novelty (−2):** commodity — steal-then-extort via SaaS OAuth abuse; no custom tooling.

### First-party Splunk

No first-party IOC hits at time of scoring (categorical Splunk null).

---

## Attribution confidence caveat

This scoring rests on **single-IR-vendor (Huntress) B2** attribution with WEP **likely** on the actor-identity layer. Per the finding's SAT-KAC, assumption A1 is unresolved — whether Huntress's actual language asserts "Icarus is distinct" versus "Huntress is tracking unattributed activity under the Icarus label" (Huntress primary was not retrieved). Per the finding's SAT-ACH, hypotheses H1 (genuinely-distinct actor) and H3 (UNC6395 affiliate/splinter) are **not operationally distinguishable** on current evidence. The scores above reflect *observed behavior*, which is the same under either hypothesis — but the identity itself is provisional. Per Hard Rule 2, no attribution link to ShinyHunters, UNC6395, or Scattered Spider is asserted.

---

## Review policy

- **Interval:** 90 days
- **Last reviewed:** 2026-07-06
- **Next review due:** 2026-10-04
- **Early review triggers:**
  - New attribution from A-grade source
  - New tooling documented
  - CVE exploitation linked to actor
  - Major campaign disclosure
  - First-party IOC observation
- **Standing tripwires:** second IR vendor publishes independent Icarus assessment (lifts single-source veto); Huntress primary retrieved (resolves KAC A1); IR vendor cross-walks Icarus to an established cluster (Hard Rule 2 re-evaluation); additional or A&D-prime victim emerges (re-score).

---

## Methodology note

Scored per `doctrine/THREAT-BOX-METHODOLOGY.md` (Piazza SANS framework adapted for A&D). Target profile: `ad-prime-v1` (mid-to-large US A&D contractor, ITAR-regulated, DoD contracts).

---

*Generated from `threat-box.yaml`. To update, re-run the `threat-box-scoring` skill and regenerate.*
