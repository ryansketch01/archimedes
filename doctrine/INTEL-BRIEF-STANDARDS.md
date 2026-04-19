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

Every brief has **three layers** that the briefer subagent produces:

### Layer 1 — Canonical brief (the permanent record)

Markdown file in `threats/briefs/YYYY-MM-DD-{type}.md`. Full structure, all sections, all metadata. This is what gets committed to git and becomes the audit record.

### Layer 2 — Discord embed (the delivery format)

A rendering of the canonical brief into Discord's embed format. Has character limits (4096/embed, 6000 total, 25 fields max). The Discord bot performs this conversion; the briefer does not produce Discord-specific output directly.

### Layer 3 — Dashboard view (optional human read)

Same canonical brief, rendered as HTML in the Flask dashboard with links, hover cards on actor references, and filter controls.

**One source of truth, three renderings.** The briefer produces Layer 1 only.

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
```

**Section order is fixed.** Standing sections (Sector Focus, Iran Cyber Watch) always appear even if empty — use the `silent_day_template` from `infrastructure/watch-config.yaml`.

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
