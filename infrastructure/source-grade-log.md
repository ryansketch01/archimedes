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
