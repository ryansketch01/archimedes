# Threat Box — Charming Kitten / Mint Sandstorm

**Actor ID:** 011
**Target profile:** ad-prime-v1 (mid-to-large US A&D contractor, ITAR-regulated)
**Status:** TEMPLATE — initial scoring deferred to first `/update-tracking` invocation.
**Scored:** Not yet scored.
**Approval:** N/A — pending scoring.
**Overall Threat Level:** Pending. (Roster carries `HIGH` from prior intake; this template does not yet support that.)
**Primary threat vector:** Pending.

---

## Summary

This is a **placeholder narrative**. The companion [`threat-box.yaml`](./threat-box.yaml) is a structural template with `null` values throughout. No category scores, modifiers, or composites have been computed.

**Why scoring is deferred:**

Charming Kitten / Mint Sandstorm is an active IRGC-IO Iranian APT with concurrent A1 attribution corroboration in [finding-2026-05-05-0002](../../findings/finding-2026-05-05-0002.md) (CrowdStrike + Microsoft MSTIC 2026-05-04 — same-day independent A-grade publication; corroboration test passes; WEP "very likely"). The Q2 2026 campaign introduces a new persistence path — OAuth application consent grants for `Mail.Read` + `Mail.ReadWrite` scopes via attacker-controlled apps — that is platform-portable to any Entra ID tenant. A first-pass scoring is highly likely to produce **HIGH overall**, driven by significant Capability (sustained persona-driven operations across 2014–2026 plus the new OAuth tradecraft) and Intent against the named ecosystem.

A HIGH overall threat level triggers **Hard Rule 5**: the scoring requires human sign-off via `/approve-scoring 011` posted to `#actor-review` before it can be committed. Per operator direction at this Mode-1 scaffold (2026-05-06), the threat-box-scoring skill was deliberately NOT invoked at dossier creation.

**Critical scoring discipline carried forward from the source finding:**

The red-team review on finding-2026-05-05-0002 issued a `qualify` outcome with required briefer caveats. The same discipline binds threat-box scoring construction:

- **Espionage Intent must be scored against the named victim ecosystem** (defense-policy think tanks, Iran-nuclear researchers, MENA security journalists). No defense primes are named as victims in the 2026-05-04 reporting.
- **The OAuth consent-grant tradecraft generalization to prime mailboxes is forward-looking, mechanism-based, NOT observed prime-direct activity.** This is mechanism-portability, not observed targeting. It informs Capability and Novelty modifiers, **not** Intent against `ad-prime-v1`.
- Lateral pretext from compromised think-tank persona into a prime mailbox (ACH H2 in the source finding) is plausible but unobserved; it does not raise Intent above sector-association.

These constraints exist precisely because Charming Kitten is the most **mechanism-portability-relevant** Iranian APT for the Archimedes profile, but **not** the most A&D-direct (UNC1549 holds that position). Conflating the two risks over-scoring Intent and producing a defensibility hole the source finding's red team explicitly flagged.

**Next action:** A subsequent `/update-tracking` invocation against this actor will run the threat-box-scoring skill with full evidence-set construction (carrying the qualify directive forward) and KAC review of load-bearing assumptions. If HIGH overall is computed, `reviewed_by` will remain `null` in `threat-box.yaml`, and the librarian will post the proposed scoring to `#actor-review` for human `/approve-scoring 011`.

The `next_review_due` is **2026-08-04** (90 days from dossier creation).

---

## What goes here once scoring runs

When the threat-box-scoring skill runs, this file will be regenerated with full per-category narratives. Per-category structural placeholder:

| Category | Composite | Level |
|---|---|---|
| Espionage (35%) | Pending | Pending |
| Supply Chain (20%) | Pending | Pending |
| Destructive (15%) | Pending | Pending |
| Disruptive (15%) | Pending | Pending |
| Cyber-Crime (15%) | Pending | Pending |

---

## Review policy

- **Interval:** 90 days
- **Last reviewed (template scaffold):** 2026-05-06
- **Next review due:** 2026-08-04
- **Early review triggers:**
  - New attribution from A-grade source
  - New tooling documented
  - CVE exploitation linked to actor
  - Major campaign disclosure
  - First-party IOC observation (a first-party Splunk hit on the OAuth consent-grant pattern would be especially consequential)

---

## Methodology note

Scoring will follow `doctrine/THREAT-BOX-METHODOLOGY.md` (Piazza SANS framework adapted for A&D). Target profile: `ad-prime-v1`.

**Authority gate per HIGH outcome:** if the weighted overall comes back as HIGH, `/approve-scoring 011` is required via `#actor-review` before commit.

**Red-team qualify directive carried into scoring:** the espionage-vs-mechanism-portability distinction is binding on Intent scoring, evidence narratives, and any forward-language. See `threat-box.yaml` `scoring_note` field on the `espionage` category for the load-bearing constraint text.

---

*This is a placeholder narrative. To replace it with the rendered scoring narrative, run the `threat-box-scoring` skill via `/update-tracking` (or directly) and regenerate this file from the resulting `threat-box.yaml`. See [profile.md](./profile.md) for full actor dossier.*
