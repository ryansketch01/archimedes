# Threat Box — MuddyWater

**Actor ID:** 022
**Target profile:** ad-prime-v1 (mid-to-large US A&D contractor, ITAR-regulated)
**Status:** TEMPLATE — initial scoring deferred to first `/update-tracking` invocation **after the 72-hour auto-downgrade clock on the source finding resolves (~2026-05-09 12:00 EDT)**.
**Scored:** Not yet scored.
**Approval:** N/A — pending scoring.
**Overall Threat Level:** Pending. (Roster carries `HIGH` from prior intake; this template does not yet support that.)
**Primary threat vector:** Pending.

---

## Summary

This is a **placeholder narrative**. The companion [`threat-box.yaml`](./threat-box.yaml) is a structural template with `null` values throughout. No category scores, modifiers, or composites have been computed.

**Why scoring is deferred:**

MuddyWater is an active Iranian APT (MOIS) with a US-pivot 2026 campaign attribution per Rapid7 2026-05-06 ([finding-2026-05-06-FLASH-0002](../../findings/finding-2026-05-06-FLASH-0002.md)). The campaign carries **two stacked confidence constraints**:

1. **Single-source veto** — Rapid7 alone is the originating source; SecurityWeek and BleepingComputer are pure relays.
2. **Vendor-self-rated moderate confidence** — Rapid7's own attribution ceiling.

A **72-hour auto-downgrade clock** is registered on the source finding (~2026-05-09 12:00 EDT). If by that time:

- No second A/B-grade vendor (Mandiant, Unit 42, MSTIC, CrowdStrike, Recorded Future, Volexity) corroborates,
- No first-party Splunk hit lands on any of the 19 IOCs once `_master-index.yaml` ingestion completes,
- No CISA / FBI advisory picks up,

then finding-2026-05-06-FLASH-0002 auto-downgrades to C3 "possibly true" per RETRACTION-POLICY.

A first-pass scoring is therefore **more sensitive to the resolution of the 72h clock** than the other two actors in this 2026-05-06 batch (UNC1549, Charming Kitten). Scoring before the clock resolves would either anchor on a finding that may be downgraded shortly after, or anchor on confidence levels that may shift up if independent corroboration arrives. Per operator direction at this Mode-1 scaffold (2026-05-06), the threat-box-scoring skill was deliberately NOT invoked at dossier creation.

A HIGH overall threat level — the most likely outcome if the source finding survives the 72h test — would trigger **Hard Rule 5**: the scoring requires human sign-off via `/approve-scoring 022` posted to `#actor-review` before commit.

**Critical scoring discipline carried forward (from the source finding's red-team specific revisions):**

- **Espionage Intent must be scored against Rapid7's NAMED victim ecosystem** — US construction, manufacturing, business services. **NO defense primes named. NO A&D watchlist entity named.** The brief / dossier / scoring must NOT extrapolate construction / manufacturing / business services into A&D-direct targeting. This is Rule-2-adjacent origination of campaign-targeting claims.
- **Destructive scoring must remain LOW** despite the Chaos ransomware artifacts firing T1486 — the false-flag-without-encryption pattern is theater, not destructive intent per Rapid7's assessment. Do not inflate destructive on the basis of the false-flag artifacts.
- **Cyber-crime scoring must remain LOW** — the Chaos-shaped cover does not make MuddyWater a criminal actor. Mission profile remains intelligence collection per Rapid7.
- **The contrarian ACH places H2 (different MOIS-linked Iranian cluster) and H6 (mixed-composition) at zero inconsistencies alongside H1 (MuddyWater specifically) at one inconsistency.** Per Hard Rule 2, H2 and H6 cannot be promoted as alternative actor attributions; they surface as cluster-imprecision in Rapid7's moderate-confidence framing. Scoring construction must respect this — confidence in scoring narrative will be capped by confidence in the source finding at scoring time.

**Next action:**

1. **At ~2026-05-09 12:00 EDT** — orchestrator / librarian evaluates the 72-hour auto-downgrade clock against the registered confirming-evidence and falsifying-evidence triggers in finding-2026-05-06-FLASH-0002.
2. **After clock resolution** — invoke `/update-tracking` against actor #022. Threat-box-scoring skill runs at that time.
3. **If HIGH overall computed** — `reviewed_by` stays `null` in `threat-box.yaml`; librarian posts proposed scoring to `#actor-review` for human `/approve-scoring 022`.
4. **If source finding auto-downgrades** — scoring narratives reflect that downgrade. Confidence drops accordingly. Per-category scores will likely move down across the board.

The `next_review_due` is **2026-08-04** (90 days from dossier creation), but an earlier `/update-tracking` immediately after the 72h clock resolution is the appropriate sequence.

---

## What goes here once scoring runs

When the threat-box-scoring skill runs (post-72h-clock-resolution), this file will be regenerated with full per-category narratives. Per-category structural placeholder:

| Category | Composite | Level |
|---|---|---|
| Espionage (35%) | Pending | Pending |
| Supply Chain (20%) | Pending | Pending |
| Destructive (15%) | Pending (must remain LOW) | Pending |
| Disruptive (15%) | Pending | Pending |
| Cyber-Crime (15%) | Pending (must remain LOW) | Pending |

---

## Review policy

- **Interval:** 90 days
- **Last reviewed (template scaffold):** 2026-05-06
- **Next review due:** 2026-08-04
- **Early review triggers:**
  - New attribution from A-grade source (a second A/B-grade vendor corroborating the Rapid7 attribution would lift the single-source veto and is the highest-priority trigger for this actor)
  - New tooling documented
  - CVE exploitation linked to actor
  - Major campaign disclosure
  - First-party IOC observation
  - **Retraction-policy trigger** — 72-hour auto-downgrade per finding-2026-05-06-FLASH-0002

---

## Methodology note

Scoring will follow `doctrine/THREAT-BOX-METHODOLOGY.md` (Piazza SANS framework adapted for A&D). Target profile: `ad-prime-v1`.

**Authority gate per HIGH outcome:** if the weighted overall comes back as HIGH, `/approve-scoring 022` is required via `#actor-review` before commit.

**Source-finding confidence binding:** scoring confidence will be capped by source-finding confidence at scoring time. If the source finding auto-downgrades by /update-tracking time, scoring narratives must reflect that downgrade.

---

*This is a placeholder narrative. To replace it with the rendered scoring narrative, run the `threat-box-scoring` skill via `/update-tracking` after the 72-hour auto-downgrade clock on finding-2026-05-06-FLASH-0002 resolves (~2026-05-09 12:00 EDT). See [profile.md](./profile.md) for full actor dossier and Attribution Notes section preserving all caveats.*
