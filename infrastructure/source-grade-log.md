# Source Grade Change Log

Ledger of all source reliability grade changes. Every grade change gets an entry here before `infrastructure/source-grades.yaml` is modified.

**Rules per `doctrine/INTEL-GRADING.md`:**
- Downgrades of B→D or worse require human review
- Upgrades of C→B or better require three corroborated hits in a rolling 90-day window
- Automated proposals post to Discord `#actor-review` for sign-off
- Grades reviewed quarterly even when no change is proposed

---

## 2026-04-18 — Initial grades established

**Type:** Initial
**Source:** Session 1 scaffold
**Summary:** Initial grades assigned per `doctrine/INTEL-GRADING.md` v1.0.0. All 42 sources seeded from the C3PO grading doctrine with minor refinements for the enrichment source dual-grade model (facts vs. attribution).
**Reviewer:** Ryan
**Next review:** 2026-07-18

---

## 2026-05-06 — Rapid7 — (none) → A (provisional, awaiting ratification)

**Type:** New source — provisional
**Source ID:** `rapid7`
**Reason:** First Archimedes-corpus citation as the originating source on `finding-2026-05-06-FLASH-0002` (MuddyWater attribution at moderate confidence; Chaos ransomware false-flag tradecraft). Rapid7 Labs / IR practice is widely treated as Tier-1 in industry; peer-reviewed publications, named analyst bylines, IR-engagement-grounded reporting. Proposed grade A by the grader on the assumption it sits with Mandiant / CrowdStrike / Unit 42 / MSTIC peers.
**Supporting findings:** [finding-2026-05-06-FLASH-0002]
**Posted to:** Discord `#actor-review` (message id pending — see librarian Splunk telemetry)
**Reviewer:** Awaiting Ryan ratification via `/approve-source-grade rapid7 A` (or operator downgrade)
**Provisional flag set:** `provisional: true`, `awaiting_ratification: true` in `infrastructure/source-grades.yaml`
**Effect on referencing finding:** Provisional A is treated as A for grading the finding (finding is digraph A2 / WEP likely with single-source-veto already capping); a subsequent operator downgrade to B would not change the FLASH disposition (still single-source-veto load-bearing) but would propagate to the auto-downgrade clock evaluation at 2026-05-09 12:18 EDT.
**Next review:** ratification target 2026-05-13 (7 days; before MuddyWater profile first-pass deadline)

---

## 2026-05-06 — SecurityWeek — (none) → B (provisional, awaiting ratification)

**Type:** New source — provisional
**Source ID:** `securityweek`
**Reason:** First Archimedes-corpus citation as a relay on `finding-2026-05-06-FLASH-0002` (MuddyWater attribution; SecurityWeek added no original reporting, relayed Rapid7). Proposed grade B by the grader as a fast-and-accurate security trade outlet on a par with BleepingComputer. Operator may ratify at B or downgrade to C if context-thin relay-only profile is observed across more findings.
**Supporting findings:** [finding-2026-05-06-FLASH-0002]
**Posted to:** Discord `#actor-review` (combined with Rapid7 ratification request — single message id)
**Reviewer:** Awaiting Ryan ratification via `/approve-source-grade securityweek B` or `/approve-source-grade securityweek C`
**Provisional flag set:** `provisional: true`, `awaiting_ratification: true` in `infrastructure/source-grades.yaml`
**Effect on referencing finding:** SecurityWeek role on this finding is `relay` only; its grade does not load-bear on the WEP cap (single-source veto already pins to "likely" via Rapid7 originating role). Outcome: cosmetic, no FLASH disposition impact.
**Next review:** ratification target 2026-05-13 (7 days; bundled with Rapid7)

**Precedent note:** This is the first time the librarian has surfaced new-source ratification requests via this log. Future grader runs that introduce a not-yet-listed source should follow the same pattern: add provisional entry to `source-grades.yaml`, log here, post `#actor-review`. Doctrine `INTEL-GRADING.md` does not yet describe this flow explicitly — surface in the next doctrine review.

---

## Entry template

*Copy the format below when logging a grade change.*

```
## YYYY-MM-DD — Source-Name — OLD → NEW

**Type:** Downgrade | Upgrade | New source | Deactivation | Reactivation
**Source ID:** <source-id from source-grades.yaml>
**Reason:** <specific miss/hit, or rationale, with links to evidence>
**Supporting findings:** [finding-IDs that support the change]
**Reviewer:** <human or agent>
**Next review:** YYYY-MM-DD
```
