# ACH Matrix Templates

> **On-demand reference.** Loaded when the analyst needs a starting structure for a new ACH analysis or is unsure about matrix mechanics.

---

## Blank matrix template (markdown)

Use this for human-readable workspace during draft. The formal output is YAML (see SKILL.md).

```markdown
## ACH Matrix — [Question]

**Question:** [Precisely stated]
**Date:** YYYY-MM-DD
**Analyst:** [agent_id]

### Hypotheses

- **H1:** [One-sentence declarative]
- **H2:** [One-sentence declarative]
- **H3:** [One-sentence declarative]
- **H4:** [One-sentence declarative]
- **H5:** [One-sentence declarative]

### Evidence matrix

| ID | Evidence | Source | Digraph | H1 | H2 | H3 | H4 | H5 |
|---|---|---|---|---|---|---|---|---|
| E1 | [evidence description] | [source_brief_id] | B2 | C | I | C | N | C |
| E2 | [evidence description] | [source_brief_id] | A1 | C | I | I | C | N |
| E3 | [evidence description] | [source_brief_id] | B2 | I | C | N | N | C |

**Legend:** C = Consistent · I = Inconsistent · N = Neutral · N/A = Not applicable

### Inconsistency counts

- H1: [N] inconsistencies
- H2: [N] inconsistencies
- H3: [N] inconsistencies
- H4: [N] inconsistencies
- H5: [N] inconsistencies

### Diagnostic evidence

- **E[N]:** Why it's diagnostic — what it distinguishes

### Ranking

1. **H[X]** — Rationale · WEP: [likely/very_likely/etc.]
2. **H[X]** — Rationale · WEP
...

### Sensitivity analysis

- Load-bearing evidence: E[N], E[N]
- What would flip the ranking: [specific conditions]
- Brittleness: low / medium / high

### Conclusion

[Smart-brevity paragraph stating the assessment, WEP, and caveats]

### Tripwires

- [Observation that would change the ranking] → [effect]
```

---

## Quick-reference: how to score a cell

For each (evidence, hypothesis) cell:

**C — Consistent** — If this hypothesis were true, this evidence is what you'd expect to see (or at least, not surprising).

**I — Inconsistent** — If this hypothesis were true, this evidence contradicts what you'd expect. Something doesn't fit.

**N — Neutral** — This evidence is consistent with the hypothesis being true AND consistent with it being false. Non-diagnostic.

**N/A — Not applicable** — This evidence doesn't pertain to whether this hypothesis is true (e.g., evidence about infrastructure when the hypothesis is about motive).

**Key principle:** C doesn't mean "this proves the hypothesis." It means "doesn't refute it." Many hypotheses will have Cs for the same evidence. That's normal.

**Important:** I is rarer than analysts think. Most evidence in real-world ACH is C or N. When I appears, it's valuable — it's the reason to reject a hypothesis.

---

## Common mistakes

### Mistake 1 — Counting Cs to find the winner

**Wrong:** "H1 has 8 C's, H2 has 5 C's, so H1 wins."

**Right:** "H1 has 0 I's, H2 has 3 I's, so H2 is weaker than H1." The hypothesis with the fewest inconsistencies is strongest, not the one with the most consistencies.

**Why:** A hypothesis can be consistent with a huge amount of evidence and still be wrong if it's also contradicted by even one piece. Rejection is the operation.

### Mistake 2 — Treating "absence of evidence" as "evidence of absence"

**Wrong:** "We haven't seen APT28 activity against this sector, so H1 is inconsistent."

**Right:** Ask — would we normally see this evidence if H1 were true? If yes, and we don't see it, that's evidence. If the evidence would not normally be observable, absence tells us nothing.

### Mistake 3 — Evidence that's consistent with everything

**Wrong:** Including "the attacker used spear-phishing" as an evidence row when most APTs use spear-phishing.

**Right:** Filter for diagnostic evidence. Spear-phishing is C for most hypotheses — non-diagnostic. It belongs in the finding's narrative but not in the ACH matrix.

**Exception:** If "did NOT use spear-phishing" is observed when spear-phishing was expected, that absence IS diagnostic.

### Mistake 4 — Confirmation bias in hypothesis generation

**Wrong:** Generating 3 hypotheses where 2 of them are variants of the analyst's favored conclusion.

**Right:** Include genuinely alternative framings:
- The null hypothesis (no specific actor)
- A surprise hypothesis (an unmonitored actor)
- The inverted hypothesis (someone deliberately implicating your suspected actor)
- The simplest hypothesis (Occam's razor — what's the least complex explanation?)

### Mistake 5 — Stopping when you have "enough" evidence

**Wrong:** "H1 has 5 C's and 0 I's. Conclusion: H1."

**Right:** Apply sensitivity analysis. If one of those 5 C's were wrong, does H1 still lead? If the whole conclusion rests on one piece of evidence, the assessment is brittle — reduce WEP.

---

## Weighted scoring (advanced)

For most questions, unweighted C/I/N is sufficient. Use weighted scoring when:

- Evidence varies widely in credibility (A1 alongside C3 sources)
- The matrix is ambiguous and you need more resolution
- Multiple hypotheses tie on inconsistency counts

### Weight assignment

| Admiralty grade | Weight |
|---|---|
| A1, A2 | 3 |
| B1, B2 | 2 |
| A3-A5, B3-B5, C1-C3 | 1 |
| C4+, D, E, F | 0.5 (use only when no better evidence) |

### Weighted inconsistency score per hypothesis

```
Inconsistency Score = sum(weight × 1 for each I entry)
Consistency Score   = sum(weight × 1 for each C entry)
```

Rank hypotheses by lowest inconsistency score. Consistency score is a tie-breaker.

**Example:**

| E | Weight | H1 | H2 |
|---|---|---|---|
| E1 (A1) | 3 | C | I |
| E2 (B2) | 2 | I | C |
| E3 (C3) | 1 | C | C |

H1 inconsistency: 2 (from E2)
H2 inconsistency: 3 (from E1 — heavier weight)

Even though H1 and H2 both have 1 I each, H2 is weaker because its inconsistency is against higher-weighted evidence.

---

## When ACH isn't the right tool

Use `sat-kac` (Key Assumptions Check) instead when:

- There's only one hypothesis, but it depends on assumptions
- The question is "what would have to be true for this to be wrong?"
- You're validating an existing assessment, not comparing alternatives

Use `admiralty-grading` alone when:

- Single source-claim pair
- No genuine alternatives, just grading

Use structured brainstorming when:

- You can't even generate hypotheses yet
- The question is too open-ended for hypothesis structure

ACH's overhead is justified when there are real, competing explanations. Don't use it as a ritual when the answer is clear from grading alone.

---

*Last updated: Session 2 scaffold*
*Based on: Heuer, Psychology of Intelligence Analysis (1999), Chapter 8*
