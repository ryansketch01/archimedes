---
name: smart-brevity
description: Use when writing or editing any Archimedes brief — morning brief, afternoon brief, FLASH alert, weekly synthesis, threat detection weekly, threat actor summary, or retraction notice. Invoke when drafting brief content from findings, when rewriting a weak lead sentence, when checking banned phrases, when applying quote discipline (max 15 words, one quote per source), when running the pre-flight checklist before publication, when enforcing anti-repetition against the coverage log, or when formatting correlation callouts. Also invoke when a briefer subagent produces content that feels verbose, hedged, or marketing-ish — this skill enforces the cut list and calibrates to Axios-style impact-first writing.
---

# Smart Brevity Skill

## Purpose

This skill encodes Archimedes's brief-writing doctrine per `doctrine/INTEL-BRIEF-STANDARDS.md`. It teaches agents to write in Axios-style Smart Brevity: lead with impact, cut filler, specify over hedge, and pass the pre-flight checklist before shipping.

**Invoke BEFORE drafting, not after.** Retrofitting brevity onto finished prose is harder than writing brief from the start.

## What this skill covers

1. The 9 style rules — how each sentence should read
2. The banned phrase list — words and openers to cut on sight
3. Section structure — the canonical format per brief type
4. Quote discipline — Hard Rule 6 enforcement
5. Anti-repetition — checking `_coverage-log.yaml` before including an item
6. Correlation callouts — how to surface connections between items
7. Pre-flight checklist — the QC gate that fires before publication

## Prerequisites

Before invoking, gather:

1. **Brief type** — morning, afternoon, flash, weekly_synthesis, threat_detection_weekly, threat_actor_summary, retraction
2. **Graded findings to include** — each with its digraph from `admiralty-grading`
3. **Current coverage log** — `threats/briefs/_coverage-log.yaml`
4. **Watch config** — `infrastructure/watch-config.yaml` for standing sections
5. **Target word count** — from the brief-type table below

If drafting a retraction, also load `doctrine/RETRACTION-POLICY.md`.

## Brief types and targets

| Brief | Cadence | Min grade | Target length |
|---|---|---|---|
| Morning | 08:00 EDT daily | B2 action / C3 monitoring | 400-800 words |
| Afternoon | 16:00 EDT daily | B2 action / C3 monitoring | 400-800 words |
| FLASH | Async 9am-9pm EDT | B2 | 150-300 words |
| Weekly Synthesis | Sun 10:00 EDT | C3 | 1500-3000 words |
| Threat Detection Weekly | Wed 10:30 EDT | B2 | 800-1500 words |
| Threat Actor Summary | Fri 12:00 EDT | B2 | 1000-2000 words |

Load `references/brief-templates.md` for the canonical template per brief type.

## The 9 Style Rules

### Rule 1 — Lead with impact, not context

The lead sentence must state the thing that matters most. Not the setup. Not "in recent weeks." Not who's reporting. The thing.

| ❌ Bad | ✅ Good |
|---|---|
| "In recent weeks, researchers at Mandiant have been tracking a campaign targeting U.S. aerospace suppliers." | "UNC1549 is targeting U.S. aerospace suppliers with new spear-phishing infrastructure." |
| "A new vulnerability has been discovered in Microsoft Outlook." | "Microsoft disclosed CVE-2026-XXXXX — unauthenticated RCE in Outlook, exploited in the wild against defense contractors." |

The reader should know what matters from sentence one.

### Rule 2 — One idea per bullet, one sentence per bullet

Bullets are not paragraphs. If a bullet runs two sentences, split it into two bullets or cut to one.

| ❌ Bad | ✅ Good |
|---|---|
| "The group has been active since 2004 and typically targets government and military organizations, with a focus on Eastern European and NATO countries, though recent campaigns have expanded to include aerospace contractors." | Split into: "Active since 2004." / "Historical focus: government, military, Eastern European and NATO targets." / "Recent expansion: aerospace contractors." |

### Rule 3 — Bold the "what"

Bold the specific thing a scanning reader needs to catch — usually a CVE, actor name, product, victim, or number.

✅ "**Microsoft disclosed CVE-2026-XXXXX** — unauthenticated RCE in Outlook..."
✅ "**17 U.S. defense contractors affected** — including three Tier-1 primes."

Do not bold entire sentences. Do not bold for decoration.

### Rule 4 — Active voice always

Active voice names the actor. Passive voice hides them.

| ❌ Bad (passive) | ✅ Good (active) |
|---|---|
| "A vulnerability was discovered in Cisco ASA." | "Cisco disclosed a vulnerability in ASA." |
| "The payload was deployed via a spear-phishing email." | "APT28 deployed the payload via spear-phishing." |
| "The organization was breached in March." | "Scattered Spider breached the organization in March." |

**Exception:** When the actor is genuinely unknown and matters less than the effect, passive is acceptable. ("Seventeen contractors were breached; attribution pending.")

### Rule 5 — Cut banned phrases on sight

Load `references/banned-phrases.md` for the full list. The hot-list to always cut:

- "It's worth noting that"
- "Additionally"
- "In other news"
- "Researchers have found"
- "According to reports"
- "It has been revealed"
- "As many of you may know"
- "Interestingly"
- "Notably"
- "Critically"
- "Importantly"

These add words without adding meaning. If something is "notable," show why — don't announce it.

### Rule 6 — Specificity over hedging

Replace vague qualifiers with numbers. If you don't have the number, either find it or cut the sentence.

| ❌ Bad | ✅ Good |
|---|---|
| "Several organizations were affected." | "17 U.S. defense contractors were affected, including three Tier-1 primes." |
| "A significant increase in attacks." | "A 340% increase in attacks (41 → 181 observed in March)." |
| "Many victims have been identified." | "87 named victims across six countries." |

**If specificity isn't available,** use WEP (Words of Estimative Probability) vocabulary rather than vague words like "many" or "significant":

- "Very likely" (85-95%)
- "Likely" (55-85%)
- "Roughly even chance" (~50%)

### Rule 7 — Quote discipline (Hard Rule 6)

**This is a HARD RULE, not a style preference.** Violations count as copyright non-compliance per `CLAUDE.md`.

- Maximum ONE direct quote per external source
- Direct quotes must be under 15 words
- Quotes must be in quotation marks with attribution
- Paraphrase by default — quote only when exact wording carries meaning paraphrase cannot

**Good quote usage:**

> Mandiant's M-Trends 2026 notes that "UNC1549 has abandoned commodity loaders for custom tooling." The shift coincides with a 3× expansion of their target set.

The rest of the Mandiant coverage in this brief must paraphrase. One quote, one source, done.

**Counting rule:** string of quoted phrases from the same source = still one quote limit. "X said 'alpha' and later 'beta' and also 'gamma'" = three quotes, violates the rule.

### Rule 8 — Numbers over adjectives

Adjectives are opinions. Numbers are facts.

| ❌ Bad | ✅ Good |
|---|---|
| "A massive breach" | "2.3M records exposed" |
| "Rapid patch adoption" | "63% patched within 48 hours" |
| "Widespread exploitation" | "Exploitation observed against 41 known entities in 12 countries" |

### Rule 9 — Action-oriented endings

Every item in a brief should implicitly or explicitly answer: "what does the reader do with this?"

For action items (B2 grade, in brief "Active Threats" section): include an explicit action line.
For monitoring items (C3 grade, in "Other Signal"): implicit — the item's inclusion signals "keep watching."

FLASH briefs are the strictest — every FLASH has an explicit Action line. See the FLASH template in `references/brief-templates.md`.

## Anti-repetition

Before including any item in a brief, check `threats/briefs/_coverage-log.yaml`.

Resurface an item ONLY if one of these conditions is met:

1. **Material update** — new victim, new attribution, new CVE, patch released, arrest made, ransom outcome, scope change
2. **Confirmed correlation** — this item connects to another tracked actor/CVE/campaign that was NOT previously connected to it
3. **Direct A&D relevance** appeared where none existed in original coverage
4. **Escalated threat level** — PoC → active exploitation, for example
5. **>7 days** since last mention AND situation still evolving

If no condition is met, DO NOT resurface. The coverage log is the authoritative record of what's already been said.

When resurfacing, explicitly flag as an UPDATE:

```markdown
**UPDATE: CVE-2026-21509 exploitation confirmed** — Mandiant reports...
```

## Correlation callouts

When a new finding connects to something tracked, call it out explicitly:

```markdown
🔗 **Connects to:** Actor #018 Cl0p — this campaign uses the same LEMURLOOT web shell documented in their MOVEit playbook.

🔗 **Update on:** [Prior brief date] — BlueHammer (ZD-001) now has confirmed in-the-wild exploitation.
```

**Format rules:**

- Use the 🔗 emoji prefix consistently (scannable visual anchor)
- Reference by actor number, CVE ID, or ZD-ID — not by descriptive name alone
- Briefly state the connection in the same sentence
- Do not use correlation callouts to sneak in resurfaced content — the connection must be the news

This is the ONE exception to anti-repetition: a new item that explicitly connects to previously covered material.

## Standing sections

Scheduled briefs (morning, afternoon, weekly synthesis, threat detection weekly, threat actor summary) always include configured standing sections from `infrastructure/watch-config.yaml`.

Default v1:
- **Sector Focus: Aerospace & Defense** (always present)
- **Iran Cyber Watch** (always present)

If no new activity, use the `silent_day_template` from `watch-config.yaml`. Do NOT silently omit the section — silence is a signal too.

Example silent-day content:

```markdown
## 🇮🇷 Iran Cyber Watch

No significant Iran-attributed activity in the last 24 hours. Background monitoring continues on APT33, APT34, APT35, APT39, MuddyWater, and CharmingKitten.
```

## Pre-flight checklist

Before any brief ships, run the 12-item checklist from `references/preflight-checklist.md`.

**If any check fails, regenerate the offending section. Do NOT ship bad output with a warning.**

Summary of what the checklist enforces:

- Source URL present on every item
- Admiralty digraph present on every item
- No repeats of coverage log without UPDATE flag
- Lead sentence leads with impact
- Zero banned phrases
- Standing sections present
- WEP vocabulary on forward assessments
- Word count within brief-type target
- Actor/vuln references link to dossier files
- TLP noted where non-CLEAR
- Single-source veto respected (no "very likely"+ from single source)
- Quote discipline: ≤15 words, ≤1 per source

## Output

This skill does not produce a single YAML block — it's an editing/rewriting skill, not a grading skill. Its outputs are:

1. **Rewritten prose** — the actual brief text, conforming to all rules
2. **A pre-flight checklist result** — which items passed/failed, with specifics per failure
3. **A banned-phrase audit** — any banned phrase caught and replaced, logged

Optional YAML output when the briefer wants a structured audit:

```yaml
smart_brevity_audit:
  brief_id: 2026-04-23-morning
  rules_applied:
    - rule_1_lead_with_impact
    - rule_4_active_voice
    - rule_5_banned_phrases_removed
    - rule_7_quote_discipline
  banned_phrases_cut:
    - phrase: "It's worth noting that"
      location: "active-threats section, item 2"
      replacement: "[removed; rewrote sentence]"
    - phrase: "Additionally"
      location: "vulnerabilities section, item 1"
      replacement: "[removed]"
  quote_audit:
    total_quotes: 2
    sources_quoted: [mandiant-m-trends-2026, cisa-aa26-113a]
    max_words_per_quote: 12
    violations: []
  preflight_result: passed
  word_count: 634
  target_range: [400, 800]
```

## Failure modes

Return a halt signal when:

1. **Pre-flight check fails** — never ship. Return the specific failure(s) with the regenerate-this-section instruction.
2. **Banned phrase appears more than 3 times in a draft** — indicates the briefer is writing in the wrong mode. Halt and suggest the briefer re-read this skill.
3. **Quote discipline violated** — halt and force rewrite. This is a Hard Rule, not a warning.
4. **Missing required section** (standing sections, metadata frontmatter) — halt, surface what's missing.
5. **Word count wildly off target** (<50% or >200% of target range) — halt and ask whether the wrong brief type is being drafted.

Halt format:

```yaml
status: halt
reason: quote_discipline_violation
detail: "Mandiant quoted 3 times in one brief (lines 14, 27, 45); limit is 1 per source"
action_requested: "Retain one quote; paraphrase the others"
```

## Worked examples

### Example 1 — Lead rewrite

**Bad draft:**
> "In the past several weeks, researchers at Mandiant have been observing an interesting pattern of attacks, and they have found that a group identified as UNC1549 has been targeting several U.S. aerospace suppliers, including some that are part of the A&D supply chain. It's worth noting that this represents a shift from their previous activity."

**Applied rules:** 1 (lead), 5 (banned phrases: "In the past several weeks", "interesting", "It's worth noting"), 4 (active voice), 6 (specificity).

**Good rewrite:**
> "**UNC1549 is targeting U.S. aerospace suppliers with new spear-phishing infrastructure** — a shift from their 2024-2025 focus on NATO government entities. 11 Tier-2 and Tier-3 suppliers affected in March 2026 per Mandiant telemetry."

Word count: 34. Rules applied: all 4.

### Example 2 — Quote discipline

**Bad draft (violates Rule 7):**
> Mandiant noted that "UNC1549 has abandoned commodity loaders" and added that the group is "now operating custom tooling with evasion capabilities previously unseen" and that this "represents a step-function increase in tradecraft maturity."

**What's wrong:** Three separate quotes from one source = Rule 7 violation. Also likely exceeds the 15-word quote limit on fragments 2 and 3.

**Good rewrite:**
> Mandiant notes that "UNC1549 has abandoned commodity loaders for custom tooling." The group now fields evasion capabilities Mandiant describes as a step-function increase in tradecraft maturity — paraphrasing from the same M-Trends 2026 section.

**Rules applied:** one quote, under 15 words, remainder paraphrased. Still attributes Mandiant clearly.

### Example 3 — Anti-repetition with UPDATE flag

**Coverage log entry exists:**
```yaml
- brief_id: 2026-04-18-morning
  item: "CVE-2026-21509 — patch released, no known exploitation"
  date: 2026-04-18
  digraph: A2
  resurface_if:
    - active_exploitation_confirmed
    - new_victim_disclosed
    - patch_adoption_data_available
```

**New signal:** Mandiant reports CVE-2026-21509 now exploited in the wild against A&D targets.

**Good resurface:**
> **UPDATE: CVE-2026-21509 exploitation confirmed** — Mandiant reports active in-the-wild exploitation against at least 4 U.S. defense contractors since 2026-04-20, including one Tier-1 prime. Digraph: A1.
> 🔗 **Update on:** 2026-04-18 morning brief — status moved from "patched, no exploitation" to "active exploitation."

**Rules applied:** UPDATE flag present, correlation callout used correctly, lead states the new development, specific numbers.

### Example 4 — Pre-flight catches a missing section

**Draft pre-flight result:**
```yaml
preflight_result: failed
failures:
  - check: standing_section_iran_cyber_watch_present
    detail: "Section missing entirely; watch-config.yaml requires always-present"
    remediation: "Add section using silent_day_template if no activity"
```

**Action:** Briefer regenerates the brief with the Iran Cyber Watch section included using the silent-day template. Re-runs pre-flight until pass.

## References

- `references/brief-templates.md` — canonical template per brief type
- `references/banned-phrases.md` — full cut list with rationale
- `references/preflight-checklist.md` — 12-item QC gate
- `doctrine/INTEL-BRIEF-STANDARDS.md` — full doctrine (source of truth)
- `doctrine/RETRACTION-POLICY.md` — for retraction briefs
- `infrastructure/watch-config.yaml` — standing sections config
- `threats/briefs/_coverage-log.yaml` — anti-repetition source of truth
- `CLAUDE.md` Hard Rule 6 — quote discipline
