---
name: sat-kac
description: Use when applying Key Assumptions Check (KAC), the structured analytic technique from the CIA Tradecraft Primer, to interrogate assumptions embedded in an assessment. Invoke at the outset of a significant analytic project before writing the assessment, when reviewing an ACH output whose hypotheses contain unstated premises, when the analyst feels an assessment rests on "common knowledge" or "everyone knows" reasoning, when challenging a draft before a HIGH-confidence finding is published, when a source makes a claim and the analyst must decide whether to accept or interrogate the underlying assumptions. This skill produces a structured list of stated and unstated assumptions, scores each for confidence and centrality, flags assumptions whose failure would invalidate the assessment, and recommends whether each assumption should remain, be qualified, or be tested further before publication.
---

# Key Assumptions Check (KAC) Skill

## Purpose

This skill applies the Key Assumptions Check technique from the CIA Tradecraft Primer (2009) and Heuer & Pherson's Structured Analytic Techniques. KAC surfaces the assumptions — stated AND unstated — that an assessment depends on, then interrogates each one.

**KAC answers the question:** *"What would have to be true for this assessment to hold? And are those things actually true?"*

**KAC complements ACH:**
- ACH evaluates competing hypotheses against evidence
- KAC evaluates the assumptions within a single analytic line
- Run KAC at the start of analysis OR after ACH to check the surviving hypothesis

## When to invoke

Invoke KAC when:

- Beginning a significant analytic project (best practice: KAC first, then analyze)
- After ACH, to stress-test the leading hypothesis's assumptions
- An assessment rests on "common knowledge," "everyone agrees," or analyst intuition
- Before publishing any WEP "very likely" or higher assessment
- The red-team-analyst is challenging a draft and wants to surface hidden premises
- A source makes a claim that depends on unstated conditions
- An assessment hasn't been rerun in 90+ days (review cycle trigger)

Do NOT use KAC for:

- Pure factual lookups with no interpretation ("Is CVE-2024-1234 in KEV?")
- Single-source claims with A1 grading and independent corroboration (grading already did the work)
- Time-critical FLASH briefs where KAC's overhead exceeds its value (use it on the subsequent brief revisiting the incident)

## Prerequisites

Before invoking, gather:

1. **The assessment or analytic line** — the sentence or claim whose assumptions you want to interrogate. State it precisely.
2. **The surrounding context** — what question does this assessment answer? Who's the audience?
3. **Access to the evidence base** — you'll need to test assumptions against available evidence

If the assessment isn't articulated clearly, stop and clarify first. KAC on vague assessments produces vague results.

## The 5 steps

### Step 1 — Articulate all premises

List every premise — stated and unstated — that the assessment depends on. Aim for exhaustive. Include:

**Stated assumptions** — things the assessment explicitly claims or relies on.

**Unstated assumptions** — things the assessment takes for granted without saying so. These are usually the dangerous ones. Look for:

- Assumptions about the actor ("they wouldn't do X because Y")
- Assumptions about capability ("they can't do X without Z")
- Assumptions about intent ("they wouldn't bother with X-tier targets")
- Assumptions about context ("the geopolitical situation favors X")
- Assumptions about technology ("that CVE requires pre-auth")
- Assumptions about Archimedes visibility ("we'd see it in Splunk if it happened")
- Assumptions about sources ("Mandiant's attribution is reliable")
- Assumptions about TTPs ("this actor doesn't use commodity tooling")

**Technique for surfacing unstated assumptions:** For each stated claim, ask "why do I believe this?" Recursively, until you reach something that feels like foundational fact. Often that "foundational fact" is an assumption.

**Aim for 5-15 assumptions.** Fewer usually means you're missing hidden ones. More usually means you're listing restatements rather than distinct assumptions.

### Step 2 — For each assumption, ask the three questions

For every assumption:

1. **Why must this be true?** State the rationale. "Because Source X says so." "Because it's consistent with historical pattern Y." "Because I can't imagine otherwise."

2. **Under what conditions would this be false?** Specifically, what would have to change for the assumption to no longer hold?

3. **What evidence supports or contradicts this?** Cite specific `source_brief_id`s or Splunk observations. If the answer is "none," that's a red flag.

### Step 3 — Score each assumption

Two dimensions:

**Confidence** (how sure are we this assumption is correct?):
- **High** — multiple A-grade sources or first-party Splunk confirmation
- **Medium** — one A-grade source or multiple B-grade sources
- **Low** — one B-grade source, no corroboration, or inferred from pattern
- **Unknown** — no direct evidence; accepted as framing

**Centrality** (how much would the assessment change if this assumption were wrong?):
- **Critical** — assessment collapses if assumption is wrong
- **Material** — assessment's WEP would drop or shift meaningfully
- **Peripheral** — assessment holds even if assumption is wrong, with minor rewording

**The interesting box** in this 4×3 grid is **Low-confidence + Critical-centrality**. These are the assumptions that most deserve scrutiny.

### Step 4 — Classify each assumption

For each assumption, assign one of:

- **Sound** — high confidence, or medium/low confidence but peripheral. Keep as-is.
- **Qualify** — material centrality with less-than-high confidence. Assessment should include the assumption as an explicit caveat.
- **Test** — critical centrality with low confidence. Assessment is premature until this assumption is verified. Propose specific test or evidence gathering.
- **Reject** — evidence contradicts the assumption. Assessment must be revised.

### Step 5 — Produce the remediation

Based on Step 4 classifications:

- If all assumptions are **Sound** → assessment proceeds, KAC output logged as analysis trail
- If any **Qualify** → add explicit caveats to assessment. Example: *"This assessment rests on the assumption that UNC1549 retains its 2025 tradecraft profile, unchanged."*
- If any **Test** → halt the assessment. Specify the test. Rerun KAC after test completes.
- If any **Reject** → revise the assessment, rerun KAC on the revised version

## Output format

```yaml
kac_analysis:
  assessment_under_review: >
    "UNC1549 will very likely continue targeting U.S. defense contractors
    in Q2 2026, consistent with their established TTPs against CMMC-adjacent
    suppliers."
  analyzed_at: 2026-04-23T14:30:00Z
  analyzed_by: analyst
  invoking_context: "Pre-publication review for Friday Actor Summary"

  assumptions:
    - id: A1
      statement: "UNC1549's tradecraft profile in 2025 is representative of what they'll do in 2026"
      category: actor_continuity
      stated: false
      why_must_be_true: "Assessment's forward projection depends on pattern continuity"
      when_could_be_false: "Actor undergoes tooling shift, disruption, absorption into another group, or change in operational tempo"
      evidence_for: [mandiant-m-trends-2026, unit-42-2025-05]
      evidence_against: []
      confidence: high
      centrality: critical
      classification: sound

    - id: A2
      statement: "CMMC compliance creates a distinguishable target pattern for UNC1549"
      category: targeting_logic
      stated: true
      why_must_be_true: "Assessment names CMMC-adjacent suppliers as the specific target set"
      when_could_be_false: "UNC1549 targeting is actually driven by something else (victim size, geography, industry) and CMMC correlation is coincidental"
      evidence_for: [mandiant-m-trends-2026]
      evidence_against: []
      confidence: medium
      centrality: material
      classification: qualify

    - id: A3
      statement: "Q2 2026 geopolitical context remains Iran-hostile toward US defense industry"
      category: geopolitical_context
      stated: false
      why_must_be_true: "Actor willingness modifier depends on continued Iran-US tension"
      when_could_be_false: "Diplomatic détente, regional conflict shift, domestic Iranian political change"
      evidence_for: []
      evidence_against: []
      confidence: unknown
      centrality: material
      classification: qualify

    - id: A4
      statement: "UNC1549 has not been disrupted by law enforcement or counterintelligence action"
      category: actor_operational_status
      stated: false
      why_must_be_true: "Continued activity assumes continued operational capacity"
      when_could_be_false: "Undisclosed disruption operation, arrests, or infrastructure takedown"
      evidence_for: []
      evidence_against: []
      confidence: low
      centrality: critical
      classification: test

    - id: A5
      statement: "Archimedes's definition of 'CMMC-adjacent' matches what UNC1549 is actually targeting"
      category: semantic
      stated: false
      why_must_be_true: "If categorization differs, the assessment's targeting claim misaligns with reality"
      when_could_be_false: "Archimedes includes Tier-3 suppliers that UNC1549 doesn't care about, or vice versa"
      evidence_for: [archimedes-watchlist-2026]
      evidence_against: []
      confidence: medium
      centrality: peripheral
      classification: sound

  classifications_summary:
    sound: 2
    qualify: 2
    test: 1
    reject: 0

  remediation:
    status: halt_pending_test
    blocking_assumption: A4
    blocking_detail: |
      Assessment depends on UNC1549 being operationally active in Q2 2026, but
      we have no evidence confirming active-vs-disrupted status. Proposed test:
      query Mandiant/Unit 42 for any recent UNC1549 campaign reporting in last
      30 days; check for LE takedown announcements; query first-party Splunk
      for any UNC1549 infrastructure touchpoints.
    qualifying_caveats:
      - "UNC1549 targeting is correlated with CMMC-adjacent status; causation not established"
      - "Assessment assumes Iran-US geopolitical posture in Q2 2026 remains hostile"
    next_action: "Run operational-status test, then rerun KAC before publication"

  recommended_wep_after_test:
    if_A4_confirmed_active: likely
    if_A4_confirmed_disrupted: remove assessment entirely
    if_A4_unclear: reduce to "roughly even chance" with explicit caveat
```

All fields required. Nulls explicit.

## Failure modes

Return a halt signal when:

1. **Only stated assumptions listed** — the analyst hasn't dug for unstated ones. Halt and push for more.
2. **All assumptions classified as "sound"** — probably too easy. Check whether the analysis genuinely has low uncertainty, or whether the analyst is rationalizing.
3. **A "test" classification has no proposed test** — must specify concretely what would validate the assumption.
4. **Assessment is too vague to KAC** — halt and clarify the assessment first.

```yaml
status: halt
reason: insufficient_assumption_surface
detail: "Only 3 assumptions identified, all stated. An assessment of this complexity typically has 5-15 assumptions including unstated ones."
action_requested: "Review assessment for unstated premises using the taxonomy: actor continuity, capability, intent, context, technology, visibility, source reliability, TTP patterns."
```

## Worked examples

### Example 1 — DC Sniper case (canonical illustration)

**Assessment:** "The sniper is a male, white, military-trained lone operator driving a white van."

**KAC surfaces these assumptions:**

| ID | Assumption | Confidence | Centrality | Classification |
|---|---|---|---|---|
| A1 | Sniper is male | Low (base rate of similar incidents) | Critical | Qualify — single sniper possible but not certain |
| A2 | Sniper is white | Low (base rate) | Critical | **Test/Reject** — no evidence; base-rate reasoning insufficient |
| A3 | Sniper has military training | Medium (precision of shots) | Material | Qualify — marksmanship could come from other sources |
| A4 | Sniper is alone | Low (no contrary evidence) | Critical | **Test** — check for accomplice patterns |
| A5 | White van used | High (eyewitness reports) | Critical | Qualify — may be coincidence |

**Remediation:** Widen suspect pool by relaxing A1, A2, A4 assumptions. Test explicitly for team operators. In retrospect, the sniper was two Black males, neither with formal military training, driving a blue Chevrolet — every assumption except A5 was wrong. KAC at the outset would have surfaced these as low-confidence critical assumptions requiring test.

### Example 2 — Attribution assumption check

**Assessment:** "APT28 conducted the Q1 2026 A&D campaign based on infrastructure overlap with prior campaigns."

**Assumptions:**

- A1: Infrastructure reuse patterns are unique enough to identify APT28 (vs. coincidence or mimicry)
- A2: Trellix's infrastructure attribution methodology is reliable
- A3: APT28 is active and hasn't been disrupted
- A4: The observed infrastructure is actually in use, not seized/reused by a different actor
- A5: No other actor has gained access to APT28 tooling

A1 and A4 are usually low-confidence critical — worth explicit test. "Infrastructure overlap" has a famously bad history in attribution (e.g., Lazarus/APT38 case studies).

### Example 3 — KAC after ACH

**ACH output:** H1 (APT28) ranked first with zero inconsistencies.

**KAC on H1's implicit premises:**

- A1: APT28 is a coherent actor, not a cluster of related activities Mandiant has labeled APT28
- A2: APT28's TTPs in 2026 resemble their TTPs in prior reporting
- A3: The specific CVE exploitation is within APT28's observed capability

All three are reasonable but shouldn't be assumed. If A1 is wrong (APT28 is actually a fuzzy cluster), "APT28 did it" loses clarity. If A2 is wrong (TTPs drifted), attribution weakens. KAC forces these to surface rather than hide behind "APT28."

## Integration with other skills

- **`sat-ach`** — often run together. ACH reveals which hypothesis has fewest inconsistencies; KAC stress-tests the winning hypothesis's assumptions.
- **`admiralty-grading`** — evidence cited in KAC's "evidence_for" fields should already be graded.
- **`threat-box-scoring`** — KAC can reveal hidden assumptions in actor scorings (e.g., "this actor would only use custom tooling" embedded in novelty modifier reasoning).
- **`smart-brevity`** — when KAC identifies qualifying caveats, they get inserted in the brief with Smart Brevity rules.
- **`red-team-analyst`** — primary consumer alongside `analyst` subagent. Red team runs KAC to expose weaknesses in primary analyst's drafts.

## Assumption taxonomy

When generating assumptions, walk this taxonomy to avoid missing categories:

- **Actor continuity** — will the actor remain the same actor over the assessment horizon?
- **Actor operational status** — is the actor active and not disrupted?
- **Capability** — can the actor actually do what we claim they'd do?
- **Intent** — does the actor want to do what we claim they'd do?
- **Geopolitical context** — are the environmental factors driving behavior stable?
- **Technology** — do the technical preconditions hold? (e.g., "this CVE requires auth")
- **Visibility** — would Archimedes see it if it happened?
- **Source reliability** — is the source still reliable given recent performance?
- **TTP patterns** — do historical patterns predict future behavior?
- **Semantic** — do our categories match the actor's?

## References

- CIA Tradecraft Primer (April 2009), "Key Assumptions Check" section
- Heuer & Pherson, *Structured Analytic Techniques for Intelligence Analysis* (3rd ed., SAGE)
- `doctrine/INTEL-GRADING.md` — source-grading context
- The 2002 DC Sniper case — canonical KAC training example
