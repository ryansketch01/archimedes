# Cl0p — Threat Box Scoring

**Actor #018 · Target profile: `ad-prime-v1` · Scored 2026-08-12 · Version 1**
**Overall: MEDIUM (weighted 4.6) · Primary vector: SUPPLY CHAIN (category HIGH, composite 8)**
**Authority: actor-profiler-autonomous-with-notification · Hard Rule 5 gate did NOT fire**

---

## Headline

Cl0p scores **MEDIUM overall**, but the number that matters for an A&D prime is the **supply-chain category: HIGH (composite 8)**. Cl0p's entire model is compromising the ubiquitous enterprise platforms — managed file transfer (MOVEit, GoAnywhere, Cleo), ERP (Oracle E-Business Suite), and PLM (PTC Windchill/FlexPLM) — that the defense industrial base runs on, reaching hundreds of downstream victims per campaign. **MEDIUM overall is a weighting artifact**, not a low-risk verdict: the methodology weights espionage at 35%, which structurally understates a pure criminal-extortion actor whose espionage/destructive/disruptive categories are near-floor. This is the same pattern seen with other roster actors whose category-HIGH sits beneath a MEDIUM/LOW weighted overall (UNC1549 espionage-HIGH/overall-MEDIUM; CyberAv3ngers disruptive-HIGH/overall-LOW).

---

## Category scores

| Category | Intent | Willing | Cap | Novelty | Final I | Final C | Composite | Level |
|---|---|---|---|---|---|---|---|---|
| Espionage | 1 | 0 | 2 | 0 | 1 | 2 | **3** | LOW |
| **Supply Chain** | 3 | 0 | 5 | 0 | 3 | 5 | **8** | **HIGH** |
| Destructive | 1 | 0 | 2 | 1 | 1 | 1 | **2** | LOW |
| Disruptive | 2 | 0 | 3 | 1 | 2 | 2 | **4** | LOW |
| Cyber-Crime | 2 | 0 | 5 | 0 | 2 | 5 | **7** | MEDIUM |

**Weighted overall** = (3×0.35) + (8×0.20) + (2×0.15) + (4×0.15) + (7×0.15) = 1.05 + 1.60 + 0.30 + 0.60 + 1.05 = **4.60 → rounds to 5 → MEDIUM**.

---

## Rationale by category

### Supply Chain — HIGH (composite 8) · PRIMARY VECTOR
- **Intent 3 (Sector Association).** Target selection is platform-driven, not sector-selective — but the platforms Cl0p serially targets are the DIB's core software stack: Windchill/FlexPLM (aerospace/defense PLM engineering data), MFT platforms (controlled-data movement), Oracle EBS (ERP). Multiple A-grade sources document manufacturing/engineering/logistics victims (CISA AA23-158A, GTIG, Recorded Future); MOVEit 2023 touched US government/defense-adjacent orgs. Held at 3, not 5 — no A-grade source names an A&D *prime* victim; the 2026 aerospace naming is customer-base-level and the Cl0p tie on that campaign is B3/suspected.
- **Capability 5 (Significant), Novelty 0.** World-leading serial zero-day mass exploitation, multiple confirmed campaigns in 24 months (Cleo 182+, Oracle EBS 29+), custom per-platform tooling (LEMURLOOT, GOLDVEIN, SAGE*). Fresh implant per platform defeats prior signatures → Novelty 0 (defensively hard).

### Cyber-Crime — MEDIUM (composite 7)
- **Intent 2 (Regional).** Financially-motivated extortion of US/Western enterprises broadly; opportunistic-by-platform, not A&D-selective (the sector argument lives in supply_chain to avoid double-counting).
- **Capability 5 (Significant), Novelty 0.** The most prolific enterprise-mass-extortion operation of the 2020s; custom exfil tooling + Tor leak site with torrent distribution. Unlike a commodity Cobalt-Strike RaaS crew, Cl0p's custom tooling earns Novelty 0.

### Disruptive — LOW (composite 4)
- **Intent 2, Capability 3, Novelty 1.** Historical network-encryption ransomware capability, but deprecated in favor of data-theft-only extortion — active disruptive use in the 24-month window is limited.

### Espionage — LOW (composite 3)
- **Intent 1, Capability 2.** Extortion actor, not an intelligence collector. Bulk data theft ≠ espionage tradecraft. Long dwell (South Staffordshire Water ~22 months) noted but not intelligence-purposed.

### Destructive — LOW (composite 2)
- **Intent 1, Capability 2, Novelty 1.** The Clop encryptor (S0611) is destructive-capable historically, but no wiper and encryption is now routinely skipped.

---

## Modifiers

- **Willingness = 0 everywhere.** Russian-speaking criminal group; no diplomatic/sanctions/LE constraint has deterred it (June 2021 Ukraine arrests of six members did not end operations; the biggest campaigns followed).
- **Novelty = 0** on the two load-bearing categories (supply_chain, cyber_crime): custom per-platform webshells/loaders + zero-day acquisition, not commodity tooling. This is the key differentiator from a generic ransomware crew and is why capability is not discounted.

## IOC corroboration

**None applied.** First-party Splunk `defenseclaw_local` returned **0 hits** over -90d across all queryable Cl0p indicators (extortion emails, Oracle EBS C2/source IPs, webshell filenames, CVEs). The 19 hits observed were in the `archimedes` index (`archimedes:operation`) — self-referential operational telemetry, excluded. Per Hard Rule 8, silence does not disconfirm: Frank is not a MOVEit/Cleo/Oracle-EBS/Windchill tenant. Visibility-bounded null.

## Confidence

**A1** on the established campaign record (CISA AA23-158A, Google Threat Intelligence Group, Mandiant, Microsoft — multiple independent A-grade primaries). The 2026 Windchill campaign's Cl0p attribution is **B3/suspected** and was deliberately **not** relied upon for this scoring (Hard Rule 2). Attribution to a monolithic "Cl0p" is itself qualified — GTIG assesses the CL0P brand is used by ≥1 actor with different TTPs.

## Review

- **Interval:** 90 days · **Next due:** 2026-11-10
- **Actor-specific trigger:** if an independent A/B source *firmly* attributes CVE-2026-12569 (Windchill/FlexPLM) to Cl0p, rescore supply_chain and cyber_crime intent — a named A&D-prime victim would be the strongest lift toward Intent 5 and a HIGH overall (Hard Rule 5 gate).

---

*Scored 2026-08-12 via threat-box-scoring skill (compute-threat-box.py, exit 0). First-pass scoring for the pre-existing roster stub; replaces the never-scored placeholder HIGH. Auto-committed with notification; Hard Rule 5 gate did NOT fire.*
