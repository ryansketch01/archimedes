# threat-box.md Template

> **On-demand reference.** Loaded when generating the human-readable companion to `threat-box.yaml`.
> The YAML is the source of truth; this is the readable rendering.

---

## Template

```markdown
# Threat Box — {ACTOR_NAME}

**Actor ID:** {actor_id}
**Target profile:** {target_profile}
**Scored:** {scored_at} by `{scored_by}`
**Approval:** {reviewed_by or "pending /approve-scoring"}
**Overall Threat Level:** {🔴 HIGH / 🟡 MEDIUM / 🟢 LOW} (weighted {weighted_score}/10)

---

## Summary

{ACTOR_NAME} is assessed as an overall {THREAT_LEVEL} threat to the Archimedes target profile ({target_profile}), primarily driven by {top-scoring-category}.

### Per-category breakdown

| Category | Composite | Level |
|---|---|---|
| Espionage (35%) | {X}/10 | {🔴/🟡/🟢} |
| Supply Chain (20%) | {X}/10 | {🔴/🟡/🟢} |
| Destructive (15%) | {X}/10 | {🔴/🟡/🟢} |
| Disruptive (15%) | {X}/10 | {🔴/🟡/🟢} |
| Cyber-Crime (15%) | {X}/10 | {🔴/🟡/🟢} |

---

## Espionage

**Intent {final_intent}/5** ({label}) · **Capability {final_capability}/5** ({label}) · **Composite: {X}/10** · **{THREAT_LEVEL}**

### Why this Intent score

{intent.evidence}

**Sources:** {comma-separated source links}

### Why this Capability score

{capability.evidence}

**Sources:** {comma-separated source links}

### Modifiers

- **Willingness (-{willingness.modifier}):** {willingness.label} — {willingness.evidence}
- **Novelty (-{novelty.modifier}):** {novelty.label} — {novelty.evidence}

### First-party Splunk

{if observed}
🟢 **Observed** on {first_seen} via `{splunk_search}`.
{ioc_corroboration.note}
{else}
No first-party IOC hits at time of scoring.
{endif}

---

## Supply Chain

{Same structure as Espionage}

---

## Destructive

{Same structure}

---

## Disruptive

{Same structure}

---

## Cyber-Crime

{Same structure}

---

## Review policy

- **Interval:** 90 days
- **Last reviewed:** {last_reviewed}
- **Next review due:** {next_review_due}
- **Early review triggers:**
  - New attribution from A-grade source
  - New tooling documented
  - CVE exploitation linked to actor
  - Major campaign disclosure
  - First-party IOC observation

---

## Methodology note

Scored per `doctrine/THREAT-BOX-METHODOLOGY.md` (Piazza SANS framework adapted for A&D).
Target profile: `ad-prime-v1` (mid-to-large US A&D contractor, ITAR-regulated, DoD contracts).

{if HIGH}
**⚠️ Awaiting human sign-off** — per CLAUDE.md Hard Rule 5, HIGH threat levels require `/approve-scoring {actor_id}` before commit. Not yet merged to main branch.
{endif}

---

*Generated from `threat-box.yaml`. To update, re-run `threat-box-scoring` skill and regenerate.*
```

---

## Rendering rules

1. **Emoji threat levels consistent** — 🔴 HIGH, 🟡 MEDIUM, 🟢 LOW. No substitutes.
2. **Per-category sections use the same structure** — mechanical consistency helps scanning
3. **Source references hyperlink** to findings in the repo — `[source_brief_id](path/to/finding.md)`
4. **Evidence fields render as-is** from YAML — they're already narrative prose
5. **Modifiers shown with explicit sign** — `-1`, `-2`, not `1`, `2` (makes the subtraction visible)
6. **Status banner at top and bottom** if HIGH and awaiting approval

## Length

A fully-rendered `threat-box.md` should be 800-1500 words. Covers five categories with evidence narratives plus summary and review policy. If significantly longer, evidence fields are too verbose — trim them in the YAML.

## Relationship to profile.md

`threat-box.md` is a narrower view than `profile.md`:

| File | Focus |
|---|---|
| `profile.md` | Full actor dossier — history, aliases, TTPs, victim sectors, attribution chain |
| `threat-box.md` | Only the scoring narrative against the target profile |

They should reference each other:

- `profile.md` links to `threat-box.md` for scoring details
- `threat-box.md` links back to `profile.md` for actor context

---

*Last updated: Session 2 scaffold*
