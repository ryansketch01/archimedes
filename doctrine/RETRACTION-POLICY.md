# RETRACTION-POLICY.md — Retraction & Correction

> **Archimedes doctrine — correcting mistakes.**
> What happens when a brief ships with bad intel. Never silently delete. The record of being wrong is part of the record.

---

## When to Retract

A retraction is required when an item in a published brief is determined to be:

- **Factually wrong** — a claim that did not happen, a CVE that doesn't exist, attribution that was inverted
- **Materially misleading** — technically true but presented in a way that creates false understanding
- **Violating doctrine** — attribution that Archimedes originated, a quote exceeding 15 words, a single-source "very likely" assessment

A correction (not retraction) is sufficient for:

- Typos or formatting errors
- Wrong link to a correct source
- Minor wording adjustments that don't change meaning

---

## Retraction Procedure

### Step 1 — Freeze the finding

The finding's frontmatter is updated:

```yaml
retracted: true
retracted_at: 2026-04-19T10:30:00-04:00
retracted_by: ryan                     # or archimedes-librarian if auto-detected
retraction_reason: "Attribution was wrong — the source we cited later withdrew the claim. Mandiant statement 2026-04-19."
retraction_source: https://...          # what prompted the retraction
supersedes: null                        # if a new finding replaces this one
superseded_by: finding-2026-04-19-0088  # populated if there's a replacement
```

### Step 2 — Update the coverage log

In `threats/briefs/_coverage-log.yaml`, the relevant entry gets:

```yaml
retraction:
  at: 2026-04-19T10:30:00-04:00
  reason: "<one-line summary>"
  replacement_brief: 2026-04-19-afternoon  # where the correction was published
```

### Step 3 — Post retraction to Discord

A follow-up note in `#intel-briefs`:

> **🔁 Retraction — [Brief date] [brief type]**
>
> Item "[headline]" is retracted.
> Reason: [one sentence].
> Correct position: [one sentence] OR "Under review."
> Source of correction: [link].
>
> Original brief remains in the record with retraction notice.

### Step 4 — Source grade review

If the retraction was caused by an external source's error:

1. Log to `infrastructure/source-grade-log.md`
2. If 3+ retractions trace to the same source in 90 days, `actor-profiler` proposes a grade downgrade (requires human approval per `INTEL-GRADING.md`)

### Step 5 — Pattern check

After every retraction, ask:
- Was the grading process followed?
- Did the red-team review catch anything?
- What would have prevented this?

If a pattern emerges (e.g., multiple retractions from the same trigger type), update doctrine.

---

## Never Delete

The original brief file is never deleted, never edited to remove the retracted content. Retractions are additive:

- Original finding stays in `threats/findings/` with `retracted: true` flag
- Original brief stays in `threats/briefs/` unmodified
- A new markdown block is appended to the brief noting the retraction:

```markdown
---

## 🔁 Retraction (added 2026-04-19)

The item "[headline]" in the [section] section above has been retracted.

**Reason:** [explanation]
**Correction:** [what's actually true, if known]
**Source:** [link]

See `threats/findings/finding-YYYY-MM-DD-NNNN.md` for full retraction metadata.
```

Git history preserves the append operation. No force-pushes, no history rewrites.

---

## Correction Procedure (no retraction needed)

For minor errors that don't warrant retraction:

1. Fix the underlying finding/brief file with a normal edit
2. Commit with message starting `Correction:` for discoverability
3. No Discord notification required unless the correction changes meaning substantively

---

## Automatic Retraction Triggers

The agent may propose a retraction (but never commit one autonomously) when:

- A cited source publishes a correction or withdrawal
- A later A/B-grade source directly contradicts a finding
- A finding's underlying IOCs turn out to be benign (e.g., VT later shows 0/72)

When the agent detects one of these conditions, it:

1. Writes a retraction proposal to `threats/findings/_retraction-proposals.yaml`
2. Posts to Discord `#actor-review` with the proposed retraction
3. Waits for human decision before any user-facing action

The agent never autonomously ships a retraction message — retractions damage trust if issued in error, so the bar is human approval.

---

## Retraction Metrics

Tracked in Splunk for visibility:

| Metric | Target |
|---|---|
| Retractions per 100 briefs | < 2 |
| Days from publication to retraction | < 7 (most errors caught quickly) |
| Retractions causing source grade downgrade | Tracked for source quality |

Retraction rate that climbs suggests the grading pipeline is leaking bad intel. Persistent low rate suggests grading is too conservative.

---

## Examples

### Example 1 — Clean retraction

Original brief (2026-04-18 morning): "APT28 targeted Lockheed Martin this week."
Source: Single BleepingComputer article, no other corroboration.
Singled-source veto rule was violated — finding should have capped at "likely."

On 2026-04-19, Mandiant publishes analysis showing the activity was actually from a different actor.

Retraction action:
1. Finding frontmatter updated with `retracted: true`
2. Coverage log updated
3. Discord retraction post
4. New finding published with Mandiant attribution
5. Self-review: grading pipeline missed single-source veto — update grader subagent prompt

### Example 2 — Correction without retraction

Typo: "CVE-2026-21509" written as "CVE-2026-21590" in one bullet.

Correction action:
1. Fix the typo in the brief file
2. Commit with `Correction: typo on CVE number in 2026-04-18 morning brief`
3. No Discord post needed — link was correct, just the text was wrong

---

*Effective: Session 1 scaffold*
*Last reviewed: Session 1 scaffold*
