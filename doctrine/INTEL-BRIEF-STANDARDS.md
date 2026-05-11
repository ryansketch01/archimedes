# INTEL-BRIEF-STANDARDS.md — Brief Formatting & Delivery

> **Archimedes doctrine — briefing.**
> Governing rules for every brief: Morning, Afternoon, Weekly Synthesis, Threat Detection Weekly, Threat Actor Summary, and FLASH.

---

## Brief Types

| Brief | Cadence | Minimum grade | Length target |
|-------|---------|---------------|---------------|
| Morning | Daily 08:00 EDT | B2 action / C3 monitoring | 400–800 words |
| Afternoon | Daily 16:00 EDT | B2 action / C3 monitoring | 400–800 words |
| FLASH | Async, 9am–9pm EDT | B2 | 150–300 words |
| Weekly Synthesis | Sun 10:00 EDT | C3 | 1500–3000 words |
| Threat Detection Weekly | Wed 10:30 EDT | B2 | 800–1500 words |
| Threat Actor Summary | Fri 12:00 EDT | B2 | 1000–2000 words |

---

## Layered Format

Every brief has **two layers** that the briefer subagent produces, plus an optional third:

### Layer 1 — Canonical brief (the permanent record)

Markdown file in `threats/briefs/YYYY-MM-DD-{type}.md`. Full structure, all sections, all metadata, all doctrine citations, all WEP / digraph / Hard Rule framings. This is the analyst-grade record that gets committed to git and becomes the audit trail. Word count target per brief type (see table above).

### Layer 2 — Discord summary (the delivery format)

A short, mobile-readable summary embedded as `## 📣 Discord Summary` at the bottom of every scheduled brief. This is what the librarian extracts and posts to `#intel-briefs`. **Smart Brevity, natural-language dates, source-linked headlines, no themed character.** Target 150–300 words total regardless of full-brief length (well under Discord's 2000-char per-message limit). See the dedicated section below for the format spec.

### Layer 3 — Dashboard view (deferred — not built)

Originally planned: HTML rendering of the canonical brief on a Flask dashboard with hover cards on actor references and filter controls. Deferred indefinitely; the Discord listener (`/cve`, `/investigate`, `/ioc-hunt`, etc.) and the markdown-in-git corpus together cover the interactive-query and browse needs. Reserved dependencies remain in `pyproject.toml [dashboard]` for future build.

**One source of truth, two active renderings.** The briefer produces Layers 1 and 2 in the same markdown file; the librarian extracts Layer 2 at post time.

---

## Discord Summary Section (Layer 2 spec)

Every scheduled brief (morning, afternoon, weekly synthesis, threat detection weekly, threat actor summary) ends with a `## 📣 Discord Summary` section. FLASH briefs are already short enough to post as-is and do NOT carry a separate summary section.

### Format rules

1. **Open with a one-line greeting that anchors the time.** Example: `Good morning. Here's your 0800 brief — 2026-05-11.` No themed character voice (no "Rebel scum," no in-character bot personality). Just the time anchor and date.
2. **Section headers use the same emoji as Layer 1** (🚨 Active Threats, 🔓 Vulnerabilities, ✈️ Sector Focus, 🕵️ Actor Activity, 🇮🇷 Iran Cyber Watch, 📰 Other Signal). Skip any section that's empty for the Discord post — standing-section "no new activity" boilerplate stays in Layer 1 but does NOT appear in Layer 2.
3. **One bullet per finding.** Format:
   ```
   • **[Plain-English headline that summarizes the item](https://source.example.com/article)** — Natural-language summary body with concrete dates, actor names, CVE IDs, and the action a reader should take.
   ```
   The headline IS the hyperlink. Target the source article URL, not the finding-id (the finding-id citation belongs in Layer 1).
4. **Natural-language dates.** Convey freshness — readers should know at a glance how old the intel is.
   - ✅ "Checkmarx warned Friday May 9..."
   - ✅ "SailPoint disclosed an April 20 incident..."
   - ✅ "Patches arrive May 13 & 28..."
   - ❌ "Checkmarx warned 2026-05-09..."
   - ❌ "SailPoint disclosed at 2026-04-20T00:00:00-04:00..."
5. **Smart Brevity discipline** (same rules as Layer 1):
   - Lead with impact, not context
   - Active voice
   - One idea per bullet, one sentence per body (Discord-summary bodies may run to two sentences if the action call needs its own clause)
   - Cut filler phrases ("It's worth noting that," "Additionally," "In other news," etc.)
   - Numbers and specificity over adjectives and hedging
   - Bold the "what" so a scanning reader can catch it
6. **Italic emphasis** on urgent calls to action: `*apply vendor mitigations right now*` or `*patch by EOD*`.
7. **Length target 150–300 words AND ≤1900 characters (hard ceiling).** A 700-word Layer 1 should collapse to ~200 words in Layer 2. If Layer 2 runs longer than 300 words, you're keeping too much; the canonical brief in Layer 1 carries the depth. The 1900-char hard ceiling is a character backstop — Discord enforces a 2000-char per-message limit, and bullets with long SecurityWeek/vendor URLs can push a 290-word Layer 2 past 2000 even though the word count looks fine. The briefer must check both (word count in band, char count ≤1900) before claiming preflight pass. The librarian re-verifies char count before posting and halts if exceeded — see `.claude/agents/librarian.md` Mode 1 step 4 — so a draft over 1900 chars will round-trip a regen cycle. Author within the ceiling on the first pass.
8. **Hard Rule 2 framings** ("per X per prior reporting," "Archimedes does not endorse") are PRESERVED in Layer 2 when they're load-bearing — the Discord audience needs to know what's attribution vs. what's relay. Keep them, but tighten the phrasing.
9. **Digraph / WEP / finding-id citations** belong in Layer 1, NOT Layer 2. Discord readers don't need the Admiralty grade in the channel; the analyst-grade record carries it.
10. **No standing-section boilerplate.** If Iran Cyber Watch had no new activity, omit it from Discord. Layer 1 still carries the "silent day" entry per `infrastructure/watch-config.yaml`.

### Example — Discord Summary section

```markdown
## 📣 Discord Summary

Good morning. Here's your 0800 brief — 2026-05-11.

🚨 **Active Threats**

• **[Checkmarx Jenkins AST plugin compromised in supply-chain attack](https://www.securityweek.com/checkmarx-jenkins-ast-plugin-compromised-in-supply-chain-attack/)** — Checkmarx warned Friday May 9 of a malicious Jenkins AST plugin on the Jenkins Marketplace; weekend variants surfaced on GitHub. Remediation `2.0.13-848` is out. **DIB CI/CD owners:** pin Jenkins instances to the fix version and capture plugin hashes now for backfill when IOCs land.

• **[SailPoint discloses GitHub repository hack](https://www.securityweek.com/sailpoint-discloses-github-repository-hack/)** — SailPoint disclosed an April 20 incident in which a third-party-app vulnerability opened a subset of its GitHub repos. No production customer data accessed; some customer info was in the repos with extent undisclosed. SecurityWeek floats a possible TeamPCP link per prior reporting; *Archimedes does not endorse the linkage.*

🔓 **Vulnerabilities**

• **CVE-2026-6973 (Ivanti EPMM on-prem):** federal patch deadline expired last night. Unpatched on-prem fleet now carries federal non-compliance posture plus standing exploitation risk.
• **CVE-2026-42208 (BerriAI LiteLLM):** KEV deadline closes today (FCEB scope). Shops proxying LLM API traffic through LiteLLM should inventory and patch *by EOD*.
```

That's ~190 words covering two findings + two carry-over CVE deadlines from a 731-word Layer 1 brief. Mobile-readable, source-linked, natural-language dates, no themed voice.

### What the librarian does with it

The librarian's Mode 1 procedure (see `.claude/agents/librarian.md`) extracts the content under `## 📣 Discord Summary` from the canonical brief and posts that text to `#intel-briefs`. The full canonical brief stays in git as the analyst-grade record; the Discord post is the executive summary. If the Discord summary is missing, the librarian halts the post step and flags the briefer's output as non-compliant.

---

## Timeliness Rules

Only include items that meet these age requirements:

| Item Type | Maximum Age |
|---|---|
| Active exploits / zero-days | 72 hours |
| CVE disclosures / patches | 7 days |
| Threat actor activity / campaigns | 48 hours |
| Data breaches / incidents | 48 hours |
| Geopolitical / conflict cyber ops | 48 hours |
| Ransomware attacks | 48 hours |
| Vendor advisories / CISA alerts | 7 days |
| Arrests / indictments / law enforcement | 7 days |

**Exception:** Breaking developments on previously covered stories are eligible regardless of the original item's age, but must include an **UPDATE:** flag.

### Source Priority Order (freshness)

1. CISA alerts, FBI advisories (primary — most authoritative)
2. X/Twitter threat intel feeds via RSS bridges (fastest — breaking news)
3. Vendor blogs: Mandiant, CrowdStrike, Microsoft, Recorded Future
4. Security news: Krebs, Help Net Security, BleepingComputer, The Record
5. YouTube/long-form: for context on ongoing campaigns, not breaking news

---

## Anti-Repetition Rules

### Resurface if:

- **Material update** — new victims, new attribution, new CVE, patch released, arrests made, ransom paid/refused, escalation in scope
- **Confirmed correlation** to another tracked event or threat actor in the repo (call it out explicitly: *"Connects to Actor #018 Cl0p..."*)
- **Direct A&D relevance** that wasn't present in the original coverage
- **Escalated threat level** (e.g., PoC exploit now in active use)
- **More than 7 days** since last mention AND the situation is still evolving

### Do NOT resurface:

- Same CVE with no new patch, victim, or exploitation activity
- Same threat actor campaign with no new confirmed victims or TTPs
- Geopolitical context that hasn't changed since last brief
- "Still ongoing" items with zero new developments

### Coverage log (programmatic enforcement)

Every item covered in any brief is logged in `threats/briefs/_coverage-log.yaml`. The briefer subagent reads this file before every brief and enforces anti-repetition against the `resurface_if` conditions of each entry.

---

## Smart Brevity Rules

**Lead with impact, not context.**
- ❌ "In recent weeks, researchers at Mandiant have been tracking a campaign..."
- ✅ "UNC1549 is targeting U.S. aerospace suppliers with new spear-phishing infrastructure."

**One idea per bullet. Maximum one sentence per bullet.**

**Bold the "what"** — the thing a scanning reader needs to catch.

**Active voice always.**
- ❌ "A vulnerability was discovered..."
- ✅ "Microsoft disclosed..."

**Cut these phrases on sight:**
- "It's worth noting that"
- "Additionally"
- "In other news"
- "Researchers have found"
- "According to reports"
- "It has been revealed"
- "As many of you may know"
- "Interestingly"
- "Notably"

**Specificity over hedging.**
- ❌ "Several organizations were affected."
- ✅ "17 U.S. defense contractors were affected, including three Tier-1 primes."

**Numbers over adjectives.**
- ❌ "A significant increase in attacks."
- ✅ "A 340% increase in attacks (41 → 181 observed in March)."

**Quote discipline.**
- Maximum ONE direct quote per external source
- Quotes must be under 15 words
- Paraphrase by default. Quote only when exact wording carries meaning the paraphrase cannot.

---

## Canonical Brief Structure

```markdown
---
brief_id: 2026-04-18-morning
brief_type: morning
published_at: 2026-04-18T08:00:00-04:00
authored_by: archimedes-briefer
grader_approval: archimedes-grader
red_team_review: archimedes-red-team
human_override: null
word_count: 0
findings_referenced: []
tlp: CLEAR
---

# Morning Brief — 2026-04-18

**[One-sentence lead: the single most important thing happening right now.]**

**Why it matters:** [One sentence. Why does this affect an A&D contractor specifically?]

---

## 🚨 Active Threats

[Items meeting freshness thresholds. For each item:]

**[Bold headline — what happened]**
- What: [One sentence]
- Why it matters for A&D: [One sentence]
- Source: [Hyperlinked] · Digraph: [e.g., B2]
- Related: [Actor #XXX / Vuln-ID / Campaign-name if applicable]

## 🔓 Vulnerabilities

[Same per-item format. Flag zero-days prominently.]

## ✈️ Sector Focus: Aerospace & Defense

[Sector-specific items. Standing section per watch-config.yaml.]

## 🕵️ Actor Activity

[New campaigns, TTPs, infrastructure. Link to actor-id if tracked.]

## 🇮🇷 Iran Cyber Watch

[Standing section per watch-config.yaml. Always present, even if "no new activity".]

## 📰 Other Signal

[Anything relevant that doesn't fit above.]

---

*Sources hyperlinked inline. Admiralty digraph noted per item. TLP:CLEAR unless flagged.*

## 📣 Discord Summary

[Layer 2 — Smart Brevity summary for the Discord post. 150–300 words. See "Discord Summary Section (Layer 2 spec)" above. The librarian extracts this section content and posts to #intel-briefs; the rest of the brief stays in git as the analyst-grade record.]
```

**Section order is fixed.** Standing sections (Sector Focus, Iran Cyber Watch) always appear in Layer 1 even if empty — use the `silent_day_template` from `infrastructure/watch-config.yaml`. The `## 📣 Discord Summary` section is always the LAST section in the file so it's trivially extractable by the librarian (read from heading to EOF).

---

## FLASH Brief Format

Fires asynchronously when priority criteria are met. Much tighter than scheduled briefs.

See `doctrine/FLASH-POLICY.md` for trigger conditions and quiet-hours handling.

```markdown
---
brief_id: flash-2026-04-18-1430
brief_type: flash
published_at: 2026-04-18T14:30:00-04:00
digraph: A1
wep: very-likely
critical_override: false
quiet_hours_queued: false
findings_referenced: [finding-2026-04-18-0042]
tlp: CLEAR
---

# ⚡ FLASH: [One-line headline]

*[Timestamp EDT] · Digraph: [e.g., A1] · TLP:[level]*

**What:** [One sentence]
**Impact:** [One sentence, sector-specific]
**Action:** [What should the reader do in the next hour?]
**Sources:** [Linked, max 3]
**Related:** [Actor/vuln/campaign refs if any]
```

---

## Pre-Flight Checklist

**The briefer subagent must run this checklist before output. If any check fails, regenerate the offending section rather than ship bad output.**

- [ ] Every item references at least one source (URL)
- [ ] Every item has an Admiralty digraph
- [ ] No item repeats `_coverage-log.yaml` without a material-update flag
- [ ] Lead sentence states impact, not context
- [ ] No banned phrases from the cut list
- [ ] Standing sections present (even if "no new activity")
- [ ] Forward assessments use WEP vocabulary with probability bands
- [ ] Word count within target for brief type
- [ ] All actor/vuln references link to repo dossier files
- [ ] TLP noted where non-CLEAR
- [ ] Single-source veto respected (no "very likely" or higher from one source)
- [ ] Every quote under 15 words, max one quote per source
- [ ] `## 📣 Discord Summary` section present, last in file, 150–300 words, headlines link to source URLs, dates in natural language, no themed-character voice (scheduled briefs only — FLASH briefs post as-is)

---

## Correlation Callouts

When a new event connects to a previously tracked actor, CVE, or incident, explicitly call it out:

> 🔗 **Connects to:** Actor #018 Cl0p — this campaign uses the same LEMURLOOT web shell documented in their MOVEit playbook.

> 🔗 **Update on:** [Prior brief date] — BlueHammer (ZD-001) now has confirmed in-the-wild exploitation.

This is the ONLY reason to resurface a previously covered item without a material update.

---

## Standing Sections (Configurable)

Sections that always appear in scheduled briefs are defined in `infrastructure/watch-config.yaml`. The briefer reads this file and generates the appropriate sections — do not hardcode.

Default v1 standing sections:
- **Sector Focus: Aerospace & Defense** (always)
- **Iran Cyber Watch** (always)

Additional sector watches can be enabled by editing `watch-config.yaml`:
- Critical Infrastructure (ICS/OT)
- Supply Chain
- Ransomware Watch
- China Cyber Watch
- Russia Cyber Watch
- DPRK Financial Ops

---

## Retraction Policy

If a brief contains an item later determined to be incorrect, follow `doctrine/RETRACTION-POLICY.md`. Never silently delete. The record of being wrong is part of the record.

---

## What Gets Cut (Always)

- Filler phrases: "It's worth noting that...", "Additionally...", "In other news..."
- Restatements of context already given in a prior brief (unless UPDATE:)
- Items with no A&D relevance and no cross-sector significance
- Unconfirmed rumors without at least C3 Admiralty grade
- Vendor marketing dressed up as threat intel
- Tool demos or product announcements unless they respond to an active threat

---

*Last reviewed: Session 1 scaffold*
