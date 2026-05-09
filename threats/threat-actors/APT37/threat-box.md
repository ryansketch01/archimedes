# Threat Box — APT37

**Actor ID:** 024
**Target profile:** ad-prime-v1 (mid-to-large US A&D contractor, ITAR-regulated)
**Status:** TEMPLATE — initial scoring deferred to deliberate `/update-tracking` invocation.
**Scored:** Not yet scored.
**Approval:** N/A — pending scoring.
**Overall Threat Level:** Pending. (Roster carries `HIGH` from intake; this template does not yet support that.)
**Primary threat vector:** Pending.

---

## Summary

This is a **placeholder narrative**. The companion [`threat-box.yaml`](./threat-box.yaml) is a structural template with `null` values throughout. No category scores, modifiers, or composites have been computed.

**Why scoring is deferred:**

APT37 is an active DPRK-attributed APT with an extensive 2012+ multi-vendor track record (FireEye/Mandiant 2018, Kaspersky 2016–2018, Cisco Talos 2017–ongoing, Volexity 2021, ESET 2024–2026). The most recent disclosed campaign — Sqgame Android APK supply-chain compromise delivering BirdCall to ethnic Koreans in Yanbian Korean Autonomous Prefecture, China — is per ESET via The Record ([finding-2026-05-07-0004](../../findings/finding-2026-05-07-0004.md), 2026-05-07).

The likely scoring outcome is **HIGH overall** driven by sustained operational tempo, multi-decade history, mobile capability, supply-chain initial-access pattern, and cross-platform tooling. A HIGH overall would trigger **Hard Rule 5**: scoring requires human sign-off via `/approve-scoring 024` posted to `#actor-review` before commit. Per operator direction at this Mode-1 scaffold (2026-05-09), the threat-box-scoring skill was deliberately NOT invoked at dossier creation. The scoring decision is deferred to a deliberate `/update-tracking` pass with the human gate intact.

**Critical scoring discipline carried forward (must apply at /update-tracking time):**

- **Score Espionage Intent against the A&D target profile, NOT against APT37's dominant target profile.** APT37 has HIGH espionage capability against its dominant target population (civil society, defectors, Korean-language journalists, defense-policy think-tanks). The Archimedes threat-box question is espionage capability + INTENT against the A&D prime, which is lower. **A&D-prime targeting is undocumented in public reporting.** Civil-society + defector + occasional defense-think-tank targeting is A&D-adjacent, not A&D-direct. This is the methodologically honest constraint and must NOT be inflated by extrapolation.

- **Single-source veto applies to the Sqgame / BirdCall specific campaign** per finding-2026-05-07-0004 (ESET via The Record alone). Historical APT37 attribution and capability assessment is multi-vendor (FireEye, Kaspersky, Cisco Talos, Volexity, ESET) — that broader capability assessment is NOT single-sourced. Scoring construction must distinguish:
  - Recent-campaign-specific inferences (single-source-capped at "likely")
  - Historical multi-vendor capability (high confidence)

- **MSS attribution distinction.** APT37 attribution to MSS specifically is per ESET via The Record's 2026 framing. Earlier reporting (FireEye 2018, Kaspersky 2018, Cisco Talos 2017) attributed broadly to "North Korean state interests" without specifying MSS vs. RGB. Scoring should distinguish:
  - "DPRK state-aligned" — high confidence, multi-vendor, decade-plus
  - "MSS specifically" — lower confidence, recent single-source framing
  Per Hard Rule 2, Archimedes does not originate either attribution; both are reported as cited sources' claims.

- **Supply-chain scoring tension.** APT37 has DEMONSTRATED supply-chain compromise capability (Sqgame Android APK supply-chain, 14+ month operator-side persistence per ESET). Capability is HIGH on absolute terms. However, the demonstrated supply-chain operation targets **consumer Android distribution** (gaming platform), NOT enterprise SaaS, software vendor, or A&D supplier ecosystem. Intent against A&D supply chain is undocumented. Score Capability HIGH, Intent against A&D lower (not target-specific). The Sqgame demonstration is *method-portability* evidence, not *target-specific-intent* evidence.

- **Destructive scoring caveats.** FireEye 2018 documents RUHAPPY (suspected wiper / MBR-overwrite capability). **NO public reporting documents APT37 actually deploying RUHAPPY or any destructive operation against any victim.** Score destructive Capability LOW-MEDIUM (capability-existence per FireEye 2018, but no operational deployment), Intent LOW. Distinct from Lazarus / Sandworm / Stardust Chollima destructive track record. Do NOT inflate destructive on the basis of capability-existence alone.

- **Cyber-crime LOW.** APT37 is state-aligned MSS espionage actor — NOT financially motivated. Distinct from RGB-attributed Lazarus and Stardust Chollima which have financial-revenue-generation tasking. Mission profile is intelligence collection.

**Next action:**

1. Invoke `/update-tracking` against actor #024 at deliberate scoring time. Threat-box-scoring skill runs at that time.
2. **If HIGH overall computed (likely)** — `reviewed_by` stays `null` in `threat-box.yaml`; librarian posts proposed scoring to `#actor-review` for human `/approve-scoring 024`.
3. **If A&D-direct targeting disclosed in subsequent A/B-grade reporting** — early review trigger fires; rerun scoring at that point.
4. **If second A/B-grade vendor corroborates Sqgame attribution** — single-source veto on the Sqgame-specific campaign lifts; capability inferences from that campaign upgrade.

The `next_review_due` is **2026-08-07** (90 days from dossier creation), but an earlier `/update-tracking` invoked deliberately for scoring is appropriate at any time.

---

## What goes here once scoring runs

When the threat-box-scoring skill runs (at deliberate /update-tracking time), this file will be regenerated with full per-category narratives. Per-category structural placeholder:

| Category | Composite | Level |
|---|---|---|
| Espionage (35%) | Pending — score against A&D target profile, NOT dominant civil-society profile | Pending |
| Supply Chain (20%) | Pending — Capability HIGH on absolute terms; Intent against A&D supply chain LOW (consumer Android demonstrated) | Pending |
| Destructive (15%) | Pending — capability-existence per RUHAPPY 2018; no operational deployment | Pending |
| Disruptive (15%) | Pending — no documented disruptive operations | Pending |
| Cyber-Crime (15%) | Pending — state-aligned MSS espionage, not financially motivated; LOW expected | Pending |

---

## Review policy

- **Interval:** 90 days
- **Last reviewed (template scaffold):** 2026-05-09
- **Next review due:** 2026-08-07
- **Early review triggers:**
  - **New attribution from A-grade source** — second A/B-grade vendor corroborating ESET's Sqgame attribution would lift the single-source veto on that campaign-specific finding
  - New tooling documented
  - CVE exploitation linked to actor
  - Major campaign disclosure
  - First-party IOC observation (any first-party Splunk hit on APT37 indicators)
  - **A&D-direct targeting disclosure** — would materially shift Espionage Intent against the A&D target profile

---

## Methodology note

Scoring will follow `doctrine/THREAT-BOX-METHODOLOGY.md` (Piazza SANS framework adapted for A&D). Target profile: `ad-prime-v1`.

**Authority gate per HIGH outcome:** if the weighted overall comes back as HIGH, `/approve-scoring 024` is required via `#actor-review` before commit.

**Source-finding confidence binding:** scoring confidence on the Sqgame-specific campaign is capped by single-source-veto on finding-2026-05-07-0004. Historical multi-vendor capability assessment is not single-source-bound and can score on its own evidence basis.

**A&D-relevance binding:** the methodologically honest move is to score Espionage Intent against the A&D target profile based on documented A&D-direct targeting (currently: NONE per public reporting), not against APT37's dominant target profile. Method-portability and structural-risk arguments inform secondary scoring elements (Capability, Novelty modifiers) but do NOT inflate Intent.

---

*This is a placeholder narrative. To replace it with the rendered scoring narrative, run the `threat-box-scoring` skill via `/update-tracking` against actor #024 with deliberate scoring intent. See [profile.md](./profile.md) for full actor dossier; see [iocs.md](./iocs.md) and [iocs.yaml](./iocs.yaml) for indicator set.*
