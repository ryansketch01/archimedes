# Banned Phrases — The Cut List

> **On-demand reference.** Loaded when the briefer is auditing a draft or when a human editor is reviewing output.
> These phrases are cut on sight. If the draft reads worse without them, rewrite the sentence — don't restore the phrase.

---

## The Hot List — always cut

These appear most often and add zero meaning. Remove them every time.

| Phrase | Why it's banned |
|---|---|
| "It's worth noting that" | Everything in a brief is worth noting. Cut the announcement. |
| "Additionally" | If two things matter, start a new bullet. If they're related, use a dash or semicolon. |
| "In other news" | News transitions are for newsreaders reading from teleprompters. You're writing a scannable brief. |
| "Researchers have found" | Name the researchers or skip the qualifier. Never "researchers" generic. |
| "According to reports" | Which reports? Name them, cite them, or don't mention them. |
| "It has been revealed" | Passive voice + vague agent = double violation. Use active voice with named source. |
| "As many of you may know" | Don't assume or condescend. If it's relevant, state it. If not, cut it. |
| "Interestingly" | Show the interesting thing. Don't announce it. |
| "Notably" | Same — "notably X" should just be "X." If it's in the brief, it's notable. |
| "Critically" | Same. If it's critical, treat it critically; don't label it. |
| "Importantly" | Same. |

---

## The Hedges — cut or replace with WEP

Vague hedges with no probability anchor. Replace with Words of Estimative Probability or specificity.

| Hedge | Replace with |
|---|---|
| "Seems to be" | "Very likely," "likely," or name the specific evidence |
| "Appears to be" | Same as above |
| "May have" | WEP vocabulary: "very likely," "likely," "unlikely" |
| "Could potentially" | Either "could" (50%) or specific WEP — pick one, not both |
| "Some sources suggest" | Name the sources, grade them, then state their claim |
| "It is believed" | Who believes it? Name them. Passive voice of belief hides the source. |
| "There are indications that" | What indications? Cite them. |

---

## The Filler — drop entirely

These phrases can be removed without changing meaning. Cut them and move on.

| Filler | Action |
|---|---|
| "In recent weeks" | Replace with actual timeframe ("since 2026-04-01") or cut |
| "In recent months" | Same |
| "Over the past few years" | Replace with date range or cut |
| "It should be noted" | Always cut |
| "It is important to note" | Always cut |
| "It goes without saying" | If it goes without saying, don't say it |
| "Needless to say" | Same |
| "Of course" | Cut — either the reader knows it (then don't say it) or they don't (and "of course" is condescending) |
| "Obviously" | Cut — same reasoning |
| "In essence" | Cut — just state the essence |
| "Basically" | Cut — if something needs "basically," it's probably oversimplified |
| "At the end of the day" | Cut |
| "When all is said and done" | Cut |

---

## The Marketing Language — cut ruthlessly

CTI is not marketing copy. These words belong in vendor blog posts, not Archimedes briefs.

| Marketing word | Why it's banned |
|---|---|
| "Sophisticated" | Almost every attack is called sophisticated. Use specific TTPs instead. |
| "Advanced" | Same — describe what's actually advanced about it. |
| "Nation-state-grade" | Describe the actual observations. Attribution is separate. |
| "Unprecedented" | Almost nothing is truly unprecedented in CTI. Describe the specifics. |
| "Game-changing" | Never appropriate in CTI. |
| "Revolutionary" | Never appropriate in CTI. |
| "Cutting-edge" | Describe what it actually does. |
| "World-class" | Never appropriate. |
| "Best-in-breed" | Never appropriate. |
| "Threat landscape" (as fluff) | Acceptable as a specific technical reference; unacceptable as filler. |
| "Bad actors" | Say "threat actors" at worst. Prefer "attackers" or the specific actor name. |

---

## The Soft Verbs — use hard verbs instead

Soft verbs dilute impact. Trade them for specific, active verbs.

| Soft | Hard |
|---|---|
| "Targeted" (when actual attack occurred) | "Attacked," "breached," "compromised," "phished" |
| "Leveraged" | "Used," "exploited" |
| "Utilized" | "Used" (always — "utilized" is bureaucratic "used") |
| "Conducted operations against" | "Attacked," "breached" |
| "Engaged with" | "Hit," "targeted," or name the specific action |
| "Interfaced with" | Name what was actually happening |
| "Touched" (as in "touched systems") | "Accessed," "compromised," "executed on" |

---

## The Scale Words — replace with numbers

Adjectival scale terms hide the actual scale. Replace with numbers.

| Vague | Specific |
|---|---|
| "Massive" | "X records," "X victims," "$X" |
| "Significant" | "X% increase," "X organizations" |
| "Widespread" | "X countries," "X entities," "X% of sector" |
| "Large-scale" | Numbers |
| "Many" | Exact count or estimate range |
| "Several" | Exact count |
| "A number of" | Exact count |
| "A handful" | Exact count |
| "Numerous" | Exact count |

**If you don't have the number,** either find it or rewrite the sentence to not need it. Never claim scale you can't quantify.

---

## The Meta-commentary — cut

Commentary about the brief itself or about how we're writing the brief.

| Meta-phrase | Why it's banned |
|---|---|
| "In this brief, we will cover..." | The brief's structure shows the reader what you're covering. |
| "Let's dive into..." | Don't narrate; just do it. |
| "Moving on to..." | Use section headers, not transitional prose. |
| "This brief aims to..." | The brief doesn't need to announce its aims; it just serves them. |
| "As always," | Cut — this is recurrence announcement, not content. |
| "This just in" | You're not reading a news bulletin. |
| "Breaking:" (in morning/afternoon briefs) | Reserve for FLASH only. |

---

## Exceptions — when "banned" phrases are actually fine

A few gray areas. These are banned in 99% of cases, but context occasionally justifies them.

**"It's worth noting that..."** — Fine when immediately followed by a meta-observation about the analysis itself, not about the content. E.g., "It's worth noting that this assessment relies on a single primary source; we're currently seeking corroboration." That's methodology transparency, not filler.

**"Additionally"** — Fine ONLY when connecting two tightly related claims that genuinely build on each other AND splitting would lose the logical connection. In practice, this is very rare.

**"Sophisticated"** — Acceptable when used as an industry term with a specific referent ("sophisticated persistent threat" in quotes, or referring to a named APT category). Not acceptable as a descriptor of a specific attack without supporting specifics.

When using an "exception," you should be able to explain why the word earned its place. If you can't, cut it.

---

## Usage in the skill

The `smart-brevity` skill's Rule 5 ("Cut banned phrases on sight") enforces this list. The pre-flight checklist runs a banned-phrase scan and flags any hits.

If a new filler phrase becomes common, add it here with rationale. The list is extensible — not a fixed artifact from Session 1.

---

## Extension protocol

When proposing to add a phrase to this list:

1. Show 3+ examples of the phrase in recent Archimedes drafts or in external CTI writing
2. Write a one-sentence rationale for why it's banned
3. Provide one rewrite example showing what to use instead
4. Commit via standard doctrine-revision process (not a silent edit)

---

*Last updated: Session 2 scaffold*
