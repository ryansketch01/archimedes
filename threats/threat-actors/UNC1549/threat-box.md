# Threat Box — UNC1549

**Actor ID:** 004
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

UNC1549 is the most A&D-direct Iranian APT in the 2026 Archimedes corpus per [finding-2026-05-05-0001](../../findings/finding-2026-05-05-0001.md) (Mandiant 2026-05-04 disclosure: recruiter-lure expansion into US/UK/FR/IL aerospace and defense primes, with named target categories "major US space and defense contractor" and "European missile systems integrator"). A first-pass scoring is highly likely to produce **HIGH overall** — the espionage category alone is on track for a top-band Intent (target-specific A&D primes named) paired with significant Capability (custom MINIBIKE/MINIBUS toolchain, sustained operational tempo, Outlook credential harvester documented in Mandiant 2026-05).

A HIGH overall threat level triggers **Hard Rule 5**: the scoring requires human sign-off via `/approve-scoring 004` posted to `#actor-review` before it can be committed. Per operator direction at this Mode-1 scaffold (2026-05-06), the threat-box-scoring skill was deliberately NOT invoked at dossier creation — auto-scoring at scaffold time would either (a) bypass the human gate if scoring auto-committed at LOW/MEDIUM (unlikely), or (b) immediately enter the gate without a deliberate review-cycle context.

**Next action:** A subsequent `/update-tracking` invocation against this actor will run the threat-box-scoring skill with full evidence-set construction and KAC review of load-bearing assumptions (per the actor-profiler Mode 2 procedure). If HIGH overall is computed, `reviewed_by` will remain `null` in `threat-box.yaml`, and the librarian will post the proposed scoring to `#actor-review` for human `/approve-scoring 004`.

The `next_review_due` is **2026-08-04** (90 days from dossier creation), but an earlier `/update-tracking` is appropriate given the active 2026 campaign.

---

## What goes here once scoring runs

When the threat-box-scoring skill runs, this file will be regenerated (per the threat-box-md template at `.claude/skills/threat-box-scoring/references/threat-box-md-template.md`) with:

### Per-category breakdown (placeholder)

| Category | Composite | Level |
|---|---|---|
| Espionage (35%) | Pending | Pending |
| Supply Chain (20%) | Pending | Pending |
| Destructive (15%) | Pending | Pending |
| Disruptive (15%) | Pending | Pending |
| Cyber-Crime (15%) | Pending | Pending |

Each category will populate with full Intent / Willingness / Capability / Novelty narratives sourced from the 2026 Mandiant disclosure, the 2024 Mandiant baseline, and any additional first-party Splunk corroboration available at scoring time.

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
  - First-party IOC observation (first-party Splunk hit on any of the eleven Mandiant 2026-05-04 IOCs would trigger this)

---

## Methodology note

Scoring will follow `doctrine/THREAT-BOX-METHODOLOGY.md` (Piazza SANS framework adapted for A&D). Target profile: `ad-prime-v1` (mid-to-large US A&D contractor, ITAR-regulated, DoD contracts).

**Authority gate per HIGH outcome:** if the weighted overall comes back as HIGH, `/approve-scoring 004` is required via `#actor-review` before commit. Per-category HIGH on espionage alone does not trigger the gate (per Session 2A methodology decision); only the weighted overall does.

---

*This is a placeholder narrative. To replace it with the rendered scoring narrative, run the `threat-box-scoring` skill via `/update-tracking` (or directly) and regenerate this file from the resulting `threat-box.yaml`. See [profile.md](./profile.md) for full actor dossier.*
