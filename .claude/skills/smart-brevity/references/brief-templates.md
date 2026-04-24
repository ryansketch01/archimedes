# Brief Templates — Canonical Formats

> **On-demand reference.** Loaded when the briefer needs the canonical template for a specific brief type.
> These are Layer 1 outputs — permanent markdown records that get committed to `threats/briefs/`.
> Layer 2 (Discord embed) and Layer 3 (dashboard HTML) are derived from Layer 1 by the Discord bot and Flask app respectively.

---

## Morning Brief

**File:** `threats/briefs/YYYY-MM-DD-morning.md`
**Cadence:** Daily 08:00 EDT
**Length target:** 400-800 words
**Minimum grade:** B2 action / C3 monitoring

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

**[Bold headline — what happened]**
- What: [One sentence]
- Why it matters for A&D: [One sentence]
- Source: [Hyperlinked] · Digraph: [e.g., B2]
- Related: [Actor #XXX / Vuln-ID / Campaign-name if applicable]

## 🔓 Vulnerabilities

[Per-item format same as above. Flag zero-days prominently.]

## ✈️ Sector Focus: Aerospace & Defense

[Standing section per watch-config.yaml. Always present.]

## 🕵️ Actor Activity

[New campaigns, TTPs, infrastructure. Link to actor-id if tracked.]

## 🇮🇷 Iran Cyber Watch

[Standing section per watch-config.yaml. Always present, even if "no new activity".]

## 📰 Other Signal

[Anything relevant that doesn't fit above.]

---

*Sources hyperlinked inline. Admiralty digraph noted per item. TLP:CLEAR unless flagged.*
```

---

## Afternoon Brief

**File:** `threats/briefs/YYYY-MM-DD-afternoon.md`
**Cadence:** Daily 16:00 EDT
**Length target:** 400-800 words
**Minimum grade:** B2 action / C3 monitoring

Structure identical to Morning Brief. Differences:

- `brief_type: afternoon`
- Lead sentence emphasizes what has developed since 08:00
- "UPDATE:" flagging is more common (intra-day developments on morning items)
- Anti-repetition check considers the morning brief's coverage log entries

```markdown
---
brief_id: 2026-04-18-afternoon
brief_type: afternoon
published_at: 2026-04-18T16:00:00-04:00
...
---

# Afternoon Brief — 2026-04-18

**[Lead: what's changed since this morning, or what's new entirely.]**

[Same section structure as morning.]
```

---

## FLASH Brief

**File:** `threats/briefs/flash-YYYY-MM-DD-HHMM.md` (timestamp to the minute)
**Cadence:** Async, 9am-9pm EDT (with critical override per FLASH-POLICY.md)
**Length target:** 150-300 words
**Minimum grade:** B2

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

**Critical override flag:** Set `critical_override: true` only when ALL of: CVSS 10.0 + confirmed active exploitation + tracked actor + A&D watchlist hit. See `doctrine/FLASH-POLICY.md`.

---

## Weekly Synthesis

**File:** `threats/briefs/YYYY-MM-DD-weekly-synthesis.md`
**Cadence:** Sun 10:00 EDT
**Length target:** 1500-3000 words
**Minimum grade:** C3

The synthesis is about patterns, not incidents. It's the only scheduled brief where C3 items can carry narrative weight — because a pattern of lower-confidence signal is itself a higher-confidence observation.

```markdown
---
brief_id: 2026-04-20-weekly-synthesis
brief_type: weekly_synthesis
published_at: 2026-04-20T10:00:00-04:00
authored_by: archimedes-briefer
grader_approval: archimedes-grader
red_team_review: archimedes-red-team
coverage_window:
  start: 2026-04-13
  end: 2026-04-19
findings_referenced: []
word_count: 0
tlp: CLEAR
---

# Weekly Synthesis — 2026-04-13 to 2026-04-19

**[Lead: the dominant pattern of the week in one sentence.]**

**Executive summary:** [3-5 bullet points covering the week's most significant developments.]

---

## 📈 Patterns & Trends

[What emerged this week that wasn't visible in any single daily brief?]

- **Pattern 1:** [One-sentence description]
  - Evidence: [Links to specific findings from the week]
  - Assessment: [WEP statement about what this likely means]

- **Pattern 2:** [Same format]

## 🎯 Sector Spotlight: Aerospace & Defense

[Standing section. This week's A&D-specific developments consolidated.]

## 🔓 Vulnerability Landscape

[New CVEs disclosed this week, patches released, exploitation status changes. Emphasis on CVEs relevant to A&D tech stack.]

## 🕵️ Actor Activity Rollup

[Per-actor summary of tracked groups active this week. Link to actor dossier for each.]

- **APT28** — [One-sentence summary] · [Link to dossier]
- **UNC1549** — [Same]
- [Continue for all actors with activity this week]

## 🇮🇷 Iran Cyber Watch — Weekly

[Standing section. Week-over-week aggregation.]

## 🔄 Updates on Prior Coverage

[Material updates to items covered in prior briefs. Use UPDATE: flag.]

## 📊 By the Numbers

[Quantitative roundup:]
- FLASH alerts this week: N
- Findings graded B2 or higher: N
- CISA KEV additions: N
- New actors or campaigns added to repo: N

## 🔮 Forward Look

[What to watch next week. Use WEP vocabulary strictly — these are forward assessments.]

---

*Cumulative view of the week. Individual items link back to daily briefs for deeper detail.*
```

---

## Threat Detection Weekly

**File:** `threats/briefs/YYYY-MM-DD-threat-detection.md`
**Cadence:** Wed 10:30 EDT
**Length target:** 800-1500 words
**Minimum grade:** B2

Focused on detection engineering opportunities — what new IOCs, behaviors, or TTPs have emerged that could be translated into Splunk detections.

```markdown
---
brief_id: 2026-04-22-threat-detection
brief_type: threat_detection_weekly
published_at: 2026-04-22T10:30:00-04:00
coverage_window:
  start: 2026-04-15
  end: 2026-04-21
findings_referenced: []
proposed_detections: []
word_count: 0
tlp: CLEAR
---

# Threat Detection Weekly — 2026-04-22

**[Lead: the most operationally relevant development for detection engineers.]**

---

## 🎯 New Detection Opportunities

For each opportunity:

**Title**
- Observable: [The specific thing to detect — behavior, IOC, pattern]
- Source finding: [Link to finding in repo]
- Recommended detection source: [Splunk index, Sysmon event IDs, etc.]
- MITRE ATT&CK mapping: [T-number if applicable]
- Splunk search sketch: [One-line SPL or pseudocode — not production-ready]
- False positive considerations: [What legitimate activity looks similar?]
- Digraph: [e.g., B2]

## 🔍 IOC Expansions

[New indicators added to the repo this week, organized by actor/campaign. Point to `threats/iocs/_master-index.yaml` for the full list.]

## 🔁 TTP Updates

[Existing actor profiles where TTPs shifted this week.]

## 📐 Detection Coverage Gaps

[Observations about what Archimedes's own Splunk is NOT currently catching, based on this week's external reporting.]

## 🧰 Tooling & Sigma Rules

[Community Sigma rules, YARA rules, or detection tooling released this week relevant to tracked threats.]

---

*Designed for detection engineering consumption. All detections are recommendations, not production-approved.*
```

---

## Threat Actor Summary

**File:** `threats/briefs/YYYY-MM-DD-actor-summary.md`
**Cadence:** Fri 12:00 EDT
**Length target:** 1000-2000 words
**Minimum grade:** B2

Rotating deep-dive on one or more tracked actors. Every actor in the roster gets covered on a ~quarterly rotation.

```markdown
---
brief_id: 2026-04-24-actor-summary
brief_type: threat_actor_summary
published_at: 2026-04-24T12:00:00-04:00
actors_covered: [APT28, UNC1549]
findings_referenced: []
word_count: 0
tlp: CLEAR
---

# Threat Actor Summary — 2026-04-24

**[Lead: one-sentence thesis spanning the actors covered this week.]**

---

## 🎯 Primary Focus: APT28 (Fancy Bear / Forest Blizzard)

**Quick reference:**
- Attribution: GRU Unit 26165
- Region: Russia
- Threat box: [HIGH/MEDIUM/LOW] (score: X)
- Last updated: [date]
- Full dossier: [link to `threats/threat-actors/APT28/`]

### Activity in the last 90 days

[Material campaigns, TTP shifts, new infrastructure, new targeting patterns.]

### A&D relevance

[Specific observations about how this actor affects A&D contractors, if any.]

### What changed this quarter

[Changes to the actor's dossier: new IOCs, updated TTPs, scoring changes, attribution updates.]

### Detection recommendations

[Specific observables from this actor's recent activity suitable for Splunk detection.]

### Forward assessment

[WEP-worded assessment of likely next-quarter behavior.]

---

## 🎯 Secondary Focus: UNC1549

[Same structure, abbreviated.]

---

## 📋 Roster Maintenance Notes

[Admin log: which actors got `last_reviewed` bumped this week, any scoring changes proposed, any new actors added to the roster.]

---

*Covers {N} actors this week. Next summary: {next Friday date} — covering {next actors}.*
```

---

## Retraction Brief

**File:** `threats/briefs/retraction-YYYY-MM-DD-HHMM.md`
**Cadence:** As required per `doctrine/RETRACTION-POLICY.md`
**Length target:** 150-400 words
**Minimum grade:** N/A (retractions aren't graded the same way)

```markdown
---
brief_id: retraction-2026-04-25-1000
brief_type: retraction
published_at: 2026-04-25T10:00:00-04:00
retracts: [2026-04-23-morning-item-3]
retraction_reason: [attribution_error | ioc_false_positive | source_downgrade | factual_error]
superseding_grade: [new digraph if applicable]
tlp: CLEAR
---

# 🔄 Retraction — 2026-04-25

**The 2026-04-23 morning brief's [item] was incorrect.**

### What we said

[Brief restatement of the original claim, with link back to the original brief.]

### What we got wrong

[The specific error, stated directly. No hedging.]

### What we now assess

[The corrected assessment, with new digraph if applicable.]

### What changed in our process

[If the retraction implies a process failure — source miscategorized, checklist skipped, attribution rushed — state it. If it was an honest-mistake given the information at the time, say that too.]

### Impact to prior briefs

[List all prior briefs that referenced this item; each gets a correction note appended per RETRACTION-POLICY.md.]

---

*Per RETRACTION-POLICY.md, the original brief is preserved unchanged. A correction note is added inline pointing to this retraction.*
```

---

## Section emoji reference

Consistent emoji improve scanability. Use these, not substitutes:

| Emoji | Section |
|---|---|
| 🚨 | Active Threats |
| 🔓 | Vulnerabilities |
| ✈️ | Sector Focus: Aerospace & Defense |
| 🕵️ | Actor Activity |
| 🇮🇷 | Iran Cyber Watch |
| 🇨🇳 | China Cyber Watch (if enabled) |
| 🇷🇺 | Russia Cyber Watch (if enabled) |
| 📰 | Other Signal |
| 📈 | Patterns & Trends |
| 🎯 | Primary Focus / Actor Spotlight |
| 📊 | By the Numbers |
| 🔮 | Forward Look |
| 🔗 | Correlation callouts |
| 🔄 | Retractions / Updates |
| ⚡ | FLASH prefix |
| 📐 | Detection Coverage Gaps |
| 🔍 | IOC Expansions |
| 🔁 | TTP Updates |
| 🧰 | Tooling |
| 📋 | Roster / Admin |

Do not invent new emoji for sections without updating this reference.

---

*Last updated: Session 2 scaffold*
*Source of truth: `doctrine/INTEL-BRIEF-STANDARDS.md`*
