---
name: sat-ach
description: Use when applying Analysis of Competing Hypotheses (ACH), the structured analytic technique from Richards Heuer's Psychology of Intelligence Analysis. Invoke when the analyst subagent is drafting an assessment at WEP "likely" or higher, when the red-team-analyst is challenging a high-confidence finding, when attribution is uncertain and multiple actors could fit the observed TTPs, when an assessment has survived a first draft and needs rigor before publication, or when competing explanations exist for the same observed evidence. This skill produces an ACH matrix scoring each piece of evidence for consistency with each hypothesis, identifies diagnostic evidence, flags hypotheses with too much inconsistent evidence, and surfaces the hypothesis with the fewest inconsistencies — not the one with the most supporting evidence.
---

# Analysis of Competing Hypotheses (ACH) Skill

## Purpose

This skill applies Heuer's 8-step ACH methodology to Archimedes intelligence assessments. It shifts the analyst's focus from "which hypothesis does the evidence support?" to "which hypotheses are disproved by inconsistent evidence?" — the latter being a more rigorous epistemic standard.

**ACH is a tool against cognitive bias, not a tool to produce false precision.** The matrix scoring is a structured way to organize thinking; the final judgment still belongs to the analyst.

## When to invoke

Invoke ACH when any of:

- An assessment is being made at WEP "likely" or higher
- Attribution is claimed and could plausibly fit more than one actor
- Multiple explanations exist for the same observed activity
- The red-team-analyst is challenging a high-confidence finding
- A source is asserting something inconsistent with internally-held priors
- The analyst feels "too certain too fast" — overconfidence is itself an ACH trigger

Do NOT invoke ACH for:

- Routine factual findings graded A1-A2 with independent corroboration (the grading already did this work)
- IOC extraction (that's pattern-matching, not hypothesis evaluation)
- Questions with only one plausible answer (e.g., "is CVE-2024-1234 in the NVD?")

ACH is for genuine uncertainty with competing explanations. Using it routinely on everything cheapens its output.

## Prerequisites

Before invoking, gather:

1. **The question** — stated precisely. Not "did APT28 do this?" but "which threat actor is most likely responsible for the 2026-04 campaign against Tier-1 A&D primes using CVE-2026-21509?"
2. **Graded evidence** — each source-claim pair should have passed `admiralty-grading`. The ACH matrix will weight evidence by credibility.
3. **Initial candidate hypotheses** — 3-7 distinct, ideally mutually exclusive explanations. If you have only 2, you're probably missing options. More than 7, cluster.
4. **Context limits** — what facts are agreed-upon and not part of the ACH? Bound the question.

If the question isn't precise, stop and make it precise first. ACH on a vague question produces vague analysis.

## The 8 steps

### Step 1 — Identify hypotheses

Generate 3-7 candidate hypotheses. Ideally mutually exclusive (if one is true, the others must be false). In practice, some overlap is acceptable, but note it.

**Techniques for generating hypotheses:**

- Start with the obvious hypothesis (the one that first came to mind)
- Add the null hypothesis ("no specific actor; opportunistic activity")
- Add false-flag hypotheses (Actor X made it look like Actor Y)
- Add surprise hypotheses (an actor you haven't been tracking)
- Add composite hypotheses (two actors collaborating, or an actor + insider)

**Quality check:** if you can't think of at least one hypothesis you'd be embarrassed to propose, you're not stretching enough. Include low-probability hypotheses — they'll be rejected quickly if evidence is clear, but their absence creates blind spots.

**Hypothesis format:** One clear sentence per hypothesis, written in declarative form.

- H1: APT28 conducted the campaign, using CVE-2026-21509 as initial access.
- H2: UNC1549 conducted the campaign, masquerading as APT28 TTPs.
- H3: A ransomware affiliate group conducted the campaign; A&D targeting is coincidental.
- H4: A previously-untracked actor conducted the campaign, reusing public APT28 TTPs.
- H5: The campaign is a deliberate false flag by an unknown actor designed to implicate APT28.

### Step 2 — List evidence

For each hypothesis, list evidence and arguments for AND against. Include:

- Direct evidence (observed IOCs, TTPs, victim patterns)
- Absence of evidence (what we'd expect to see but don't)
- Assumptions and logical deductions (labeled as such)
- First-party Splunk telemetry (gets high weight per Hard Rule 8)

**Evidence quality check:**
- Every piece of evidence must cite a `source_brief_id` or Splunk search
- Evidence graded via `admiralty-grading` inherits that digraph
- Ungraded evidence can be used but must be flagged as such

**Heuer's diagnostic questions** (the most valuable part of Step 2):
- If this hypothesis were true, what would I expect to observe?
- If I'm not observing that evidence, why? Because the hypothesis is false? Because the evidence would not normally be observable? Because it's being concealed?
- What's the evidence of absence vs. absence of evidence?

### Step 3 — Build the matrix

Create a table: rows = evidence items, columns = hypotheses. In each cell, record consistency:

- **C** — Consistent (evidence supports this hypothesis)
- **I** — Inconsistent (evidence contradicts this hypothesis)
- **N** — Neutral (evidence neither supports nor contradicts)
- **N/A** — Not applicable (evidence doesn't relate to this hypothesis)

**Weighted variant:** multiply consistency by evidence credibility weight:

| Admiralty grade | Weight |
|---|---|
| A1, A2 | 3 |
| B1, B2 | 2 |
| A3-A5, B3-B5, C1-C3 | 1 |
| C4+, D, E, F | 0.5 (use only if no better evidence) |

Use weighted scoring only when the unweighted matrix is ambiguous. For most questions, unweighted C/I/N is sufficient.

### Step 4 — Refine the matrix — find diagnostic evidence

**Most important step.** Not all evidence is equal.

- **Diagnostic evidence** — distinguishes between hypotheses. If evidence item E is C for H1 but I for H2/H3/H4/H5, E has high diagnostic value.
- **Non-diagnostic evidence** — consistent with most or all hypotheses. Low value. "APT28 is known to be capable of this" is often non-diagnostic because multiple capable actors could fit.

Mark the diagnostic rows. These are what your assessment will rest on.

**Red flag:** if no evidence is diagnostic (all rows mostly-C across all hypotheses), you have a problem. Either:
- Hypotheses aren't distinct enough — regenerate
- Evidence isn't specific enough — need more specific observations
- The question is fundamentally underdetermined — acknowledge this and widen WEP range

### Step 5 — Draw tentative conclusions

**Focus on refuting, not confirming.**

For each hypothesis, count the I (inconsistent) entries:

- Hypotheses with many I entries = low probability
- Hypotheses with few I entries = higher probability

**Do NOT** focus on counting C entries — a hypothesis with many Cs and many Is is still weak. The Cs prove nothing; the Is are what matter.

Rank hypotheses by:
1. Fewest inconsistencies (weighted by evidence credibility)
2. Most diagnostic supporting evidence
3. Absence of fatal contradictions

### Step 6 — Analyze sensitivity

Identify the 2-3 most load-bearing pieces of evidence. Ask: if this evidence were wrong or reinterpreted, does the conclusion change?

**Specific questions:**

- If this evidence were a deception, which hypothesis would emerge?
- If this source were later downgraded, what would happen to the conclusion?
- Is there a single piece of evidence whose removal would flip the ranking?

If yes — the assessment is **brittle**. Flag this in the output. Consider reducing WEP.

### Step 7 — Report conclusions

State:

- The most probable hypothesis (fewest inconsistencies, most diagnostic support)
- The probability gap to the second-most-probable (is there a clear leader?)
- The load-bearing evidence
- The sensitivity analysis — what would change the conclusion
- WEP classification with confidence interval

**WEP discipline:** The ACH output must be translated to WEP vocabulary:

- One hypothesis with 0-1 inconsistencies, rivals with 3+ each → "very likely"
- Clear leader with meaningful gap → "likely"
- Narrow leader → "roughly even chance" between top 2
- No leader → "unlikely" that any single hypothesis is correct; widen scope

### Step 8 — Identify milestones for future observation

What evidence, if it later appeared, would:

- Confirm the leading hypothesis further?
- Flip the ranking?
- Prove a rejected hypothesis after all?

These become **tripwires** — the librarian should track them, and when they fire, rerun the ACH. This is how ACH assessments stay calibrated over time.

## Output format

```yaml
ach_analysis:
  question: "Which threat actor conducted the 2026-04 campaign against Tier-1 A&D primes using CVE-2026-21509?"
  analyzed_at: 2026-04-23T14:30:00Z
  analyzed_by: analyst
  red_team_review: null  # filled in after red-team pass

  hypotheses:
    - id: H1
      statement: "APT28 conducted the campaign, using CVE-2026-21509 as initial access."
    - id: H2
      statement: "UNC1549 conducted the campaign, masquerading as APT28 TTPs."
    - id: H3
      statement: "A ransomware affiliate group conducted the campaign; A&D targeting is coincidental."
    - id: H4
      statement: "A previously-untracked actor conducted the campaign, reusing public APT28 TTPs."
    - id: H5
      statement: "The campaign is a deliberate false flag designed to implicate APT28."

  evidence:
    - id: E1
      description: "Trellix attributes to APT28 based on infrastructure overlap with prior campaigns"
      source: trellix-2026-02
      digraph: A2
      weight: 3
    - id: E2
      description: "Victim list overlaps with prior APT28 targeting (NATO/A&D focus)"
      source: trellix-2026-02
      digraph: A2
      weight: 3
    - id: E3
      description: "CVE-2026-21509 exploitation tooling shows code similarities to X-Agent"
      source: trellix-2026-02
      digraph: A2
      weight: 3
    - id: E4
      description: "No first-party Splunk observation of campaign infrastructure in our environment"
      source: splunk-negative-search
      digraph: A1
      weight: 3
    - id: E5
      description: "Ransomware payload NOT deployed; data exfil only"
      source: trellix-2026-02
      digraph: A2
      weight: 3

  matrix:
    E1: {H1: C, H2: C, H3: I, H4: C, H5: C}  # infrastructure overlap fits APT28 or someone copying
    E2: {H1: C, H2: I, H3: I, H4: C, H5: C}  # NATO/A&D targeting doesn't fit ransomware affiliate
    E3: {H1: C, H2: I, H3: I, H4: C, H5: C}  # X-Agent similarities inconsistent with UNC1549
    E4: {H1: N, H2: N, H3: N, H4: N, H5: N}  # no information — non-diagnostic
    E5: {H1: C, H2: C, H3: I, H4: C, H5: C}  # no ransomware inconsistent with cyber-crime hypothesis

  inconsistency_counts:
    H1: 0
    H2: 2
    H3: 4
    H4: 0
    H5: 0

  diagnostic_evidence:
    - E2: "Distinguishes ransomware (H3) from targeted espionage (H1/H2/H4/H5)"
    - E3: "Distinguishes APT28-origin (H1/H4) from masquerade (H2)"

  ranking:
    - rank: 1
      hypothesis_id: H1
      rationale: "Zero inconsistencies; strongest diagnostic evidence (E2, E3); simplest explanation per Occam."
      wep: likely
    - rank: 2
      hypothesis_id: H4
      rationale: "Also zero inconsistencies, but H1 is simpler given established APT28 pattern. Cannot be ruled out without additional evidence."
      wep: unlikely
    - rank: 3
      hypothesis_id: H5
      rationale: "Zero inconsistencies but requires multiple unverified assumptions (false-flag actor, capability to replicate TTPs)."
      wep: unlikely
    - rank: 4
      hypothesis_id: H2
      rationale: "Two inconsistencies via E2, E3."
      wep: very_unlikely
    - rank: 5
      hypothesis_id: H3
      rationale: "Four inconsistencies; ruled out."
      wep: remote

  sensitivity_analysis:
    brittleness: medium
    load_bearing_evidence: [E2, E3]
    if_E3_wrong: "Ranking shifts — H4 becomes equally plausible with H1"
    if_trellix_downgraded: "Evidence weights all drop; H1/H4 ranking becomes indistinguishable"

  tripwires:
    - observation: "Previously-untracked actor claims credit for campaign"
      effect: "Elevate H4, re-rank"
    - observation: "Splunk observes campaign infrastructure in our environment"
      effect: "First-party telemetry; rerun entire ACH with +1 capability weighting"
    - observation: "Second independent source contradicts Trellix attribution"
      effect: "Reduce E1/E2/E3 weights; H4/H5 rise"

  conclusion:
    summary: |
      APT28 is likely responsible for the 2026-04 CVE-2026-21509 campaign against
      Tier-1 A&D primes. No inconsistencies in the evidence with H1, and strong
      diagnostic evidence (E2, E3) distinguishes APT28 from alternative actors.
      However, H4 (untracked actor reusing TTPs) cannot be ruled out, and the
      assessment is medium-brittleness to source downgrade.
    wep: likely
    confidence_caveats: |
      Single-source dependence on Trellix attribution is a material limitation.
      Pending second independent source, this assessment stops at "likely" per
      INTEL-GRADING single-source veto.
```

All fields required. Nulls explicit where needed.

## Failure modes

Return a halt signal when:

1. **Evidence rows are all non-diagnostic** — no evidence distinguishes hypotheses. Halt and regenerate hypotheses or gather more specific evidence.
2. **Question is too vague** — ACH cannot resolve "is this bad?" Halt and specify the question.
3. **Only one hypothesis survives** — either the analysis is right (great) or you didn't consider enough alternatives (bad). Halt and generate 2-3 more hypotheses to pressure-test.
4. **Top-ranked and second-ranked are tied** — the matrix didn't resolve the question. Halt and either gather more evidence or widen WEP to "roughly even chance."
5. **Conflicting evidence at C and I for the same hypothesis** — shouldn't happen; means evidence was mis-assessed. Halt and review.

```yaml
status: halt
reason: non_diagnostic_matrix
detail: "All 6 evidence items score C or N across all hypotheses. No hypothesis is differentially supported."
action_requested: "Generate additional hypotheses, or gather evidence that would distinguish them."
```

## Integration with other skills

- **`admiralty-grading`** — every evidence row's digraph comes from this skill; weights derive from it
- **`smart-brevity`** — the ACH conclusion narrative gets written per Smart Brevity rules when it appears in a brief
- **`sat-kac`** — ACH reveals assumptions embedded in hypotheses; those should run through KAC next
- **`red-team-analyst`** — invokes this skill to challenge analyst's draft by arguing for the rejected hypotheses

## Worked examples

### Example 1 — Attribution uncertainty (see full output format above)

The APT28/UNC1549 example is in the Output format section. Key takeaway: even with zero inconsistencies for APT28, the WEP stops at "likely" because of single-source dependence. ACH informs but doesn't override admiralty rules.

### Example 2 — When ACH reveals the question was wrong

**Initial question:** "Is this ransomware attack financially motivated?"

**Hypotheses:**
- H1: Financial extortion (standard ransomware)
- H2: Destructive wiper disguised as ransomware
- H3: Data theft with ransomware as cover
- H4: Disruption only, no financial goal

**Matrix reveals:** all hypotheses score C against most evidence. Non-diagnostic matrix.

**Insight:** The question is miscast. "Financially motivated?" isn't the interesting question because the evidence can't distinguish outcomes — the adversary hasn't completed their operation yet. The right question: "what is the adversary's primary objective, given observed pre-encryption activity?"

**Action:** Restart ACH with the reframed question.

### Example 3 — ACH with the red team

**Analyst draft:** "UNC1549 is likely responsible for the Q1 A&D phishing campaign."

**Red-team-analyst invokes ACH:**
- H1: UNC1549 did it (analyst's position)
- H2: APT28 did it (different Russia-linked actor)
- H3: APT34 did it (different Iran-linked actor, closer to UNC1549 in TTPs)
- H4: An emerging Iranian actor we haven't named yet
- H5: False flag by unrelated party

**Red-team focus:** Argue for H2/H3/H4/H5 against H1. Look for evidence that's C for H3 but I for H1.

**Output:** Even if the red team can't flip the ranking, it strengthens the assessment by making the case against H1 explicit. The published finding then cites the red team's analysis as part of the confidence narrative.

## References

- `references/ach-matrix-template.md` — blank matrix templates and worked walkthrough
- Heuer, Richards J. *Psychology of Intelligence Analysis*, CIA Center for the Study of Intelligence, 1999
- CIA Tradecraft Primer: Structured Analytic Techniques (2009)
- `doctrine/INTEL-GRADING.md` — WEP vocabulary and evidence grading
