# Pre-Flight Checklist

> **Required before every brief publication.** Not optional. Not "ship with warnings."
> If any item fails, regenerate the offending section until all items pass.

---

## How to use this file

The `briefer` subagent loads this reference at the end of every brief draft. It walks each item in order. The result is a pass/fail report per item.

**Only "all pass" ships.** A single fail means:

1. Identify the specific section or item that failed
2. Regenerate that section using the relevant skill(s)
3. Re-run the full checklist — not just the failed item
4. Repeat until all pass

**Do not ship a brief with a warning or caveat about a checklist failure.** If the briefer cannot produce a passing draft, halt and surface the issue to the orchestrator for human review.

---

## The 13 Checks

### 1. Source URL present on every item

**What to check:** Every brief item references at least one source URL. Items derived from Splunk telemetry can cite a Splunk saved-search link in lieu of an external URL.

**Pass criteria:** `len(item.sources) >= 1` and every source has a resolvable URL.

**Fail action:** Add the missing source from the finding's frontmatter, or remove the item from the brief.

### 2. Admiralty digraph present on every item

**What to check:** Every brief item has an Admiralty digraph (e.g., `A1`, `B2`, `C3`).

**Pass criteria:** Digraph matches pattern `[A-F][1-6]` and was produced by the `admiralty-grading` skill, not invented.

**Fail action:** Return to `admiralty-grading` for the ungraded item. Do not guess the grade.

### 3. No unauthorized repeats from coverage log

**What to check:** For each item, cross-reference `threats/briefs/_coverage-log.yaml`. If the item was covered in a prior brief, it must either:
- Have an `UPDATE:` flag explaining the material update, OR
- Be a correlation callout (🔗) linking to previously covered material as the news

**Pass criteria:** Every repeated item meets one of the above conditions.

**Fail action:** Remove unauthorized repeats. If the item seems important but doesn't meet the update criteria, defer to the next brief where a material development exists.

### 4. Lead sentence leads with impact

**What to check:** The brief's first sentence names the most important thing (actor + action + target, or CVE + status + impact). Not the reporter. Not the timeframe. Not the context.

**Pass criteria:**
- Active voice
- Names specific actor or CVE
- Names specific target or affected system
- Action verb describes what happened
- No banned phrases in the first 30 words

**Fail action:** Rewrite the lead using `smart-brevity` Rule 1. Common fix: move the buried lede from paragraph 2 or 3 to position 1.

### 5. Zero banned phrases from the hot list

**What to check:** Scan full brief body for the hot-list phrases in `references/banned-phrases.md`.

Hot list (always fail):
- "It's worth noting that"
- "Additionally"
- "In other news"
- "Researchers have found"
- "According to reports"
- "It has been revealed"
- "Interestingly"
- "Notably"
- "Critically" (as filler)
- "Importantly" (as filler)

**Pass criteria:** Zero occurrences in the body.

**Fail action:** Remove each offender. Rewrite sentence without the filler. Re-check.

### 6. Standing sections present

**What to check:** Read `infrastructure/watch-config.yaml`. Every section marked `always_present: true` must appear in the brief.

For v1 scheduled briefs, standing sections are:
- Sector Focus: Aerospace & Defense
- Iran Cyber Watch

**Pass criteria:** All `always_present` sections render in the output, using `silent_day_template` content if no activity.

**Fail action:** Add the missing section. Use the silent-day template if the section has no activity to report.

### 7. WEP vocabulary on forward assessments

**What to check:** Any sentence making a forward-looking claim uses Words of Estimative Probability vocabulary:
- "Almost certainly" (>95%)
- "Very likely" (85-95%)
- "Likely" (55-85%)
- "Roughly even chance" (~50%)
- "Unlikely" (15-45%)
- "Very unlikely" (5-15%)
- "Remote" (<5%)

**Pass criteria:** Every forward claim uses one of these phrases. No bare hedges like "may," "might," "could," "possibly," "perhaps."

**Fail action:** Replace bare hedges with WEP vocabulary. If probability isn't knowable, rewrite the sentence as present-tense observation rather than prediction.

### 8. Word count within target

**What to check:** Total word count (excluding frontmatter and code blocks) is within the brief-type target.

| Brief type | Min | Max |
|---|---|---|
| Morning | 400 | 800 |
| Afternoon | 400 | 800 |
| FLASH | 150 | 300 |
| Weekly Synthesis | 1500 | 3000 |
| Threat Detection Weekly | 800 | 1500 |
| Threat Actor Summary | 1000 | 2000 |
| Retraction | 150 | 400 |

**Pass criteria:** Word count within `[min, max]` for the brief type.

**Fail action:**
- Under min: brief is likely too sparse — add content or defer until there's enough to cover
- Over max: cut. Apply `smart-brevity` more aggressively. Ruthless editing over graceful trimming.

**Hard cap:** At 150% of max, halt. Something is wrong with scope.

### 9. Actor/vuln references link to dossier

**What to check:** Every mention of a tracked actor (APT28, UNC1549, etc.) or a tracked vulnerability (CVE-XXXX-YYYY) links to the corresponding dossier file in the repo.

**Pass criteria:**
- Actor mention → link to `threats/threat-actors/<actor>/profile.md`
- CVE mention → link to `threats/vulnerabilities/<cve>/` or `threats/vulnerabilities/_index.yaml` entry
- If the actor/vuln isn't tracked in the repo, the mention should be flagged for addition to `_roster.yaml` or `_index.yaml` by the librarian

**Fail action:** Add the missing links. If the entity isn't in the repo, flag for addition.

### 10. TLP noted where non-CLEAR

**What to check:** If the brief contains any TLP:AMBER, TLP:GREEN, or TLP:RED items, those items have their TLP explicitly noted. Default TLP:CLEAR items don't require per-item marking (the brief-level frontmatter covers them).

**Pass criteria:**
- Brief frontmatter has `tlp: CLEAR` (or higher)
- Any item with higher restriction than the brief-level TLP is explicitly marked
- No item with lower TLP than the brief-level (would indicate a metadata error)

**Fail action:** Add explicit TLP markings. If the brief contains TLP:RED material, halt and escalate — TLP:RED shouldn't appear in Discord briefs by default.

### 11. Single-source veto respected

**What to check:** For any claim made at WEP "very likely" or higher, verify two independent sources exist per the finding's `corroboration` field.

**Pass criteria:**
- Every "very likely" or stronger claim has `corroboration.independent: true`
- No claim exceeds the WEP ceiling set by its digraph
- First-party Splunk + A/B-grade external combinations are explicitly documented as the exception when used

**Fail action:** Downgrade the WEP to "likely" OR find the second source. Do not ship bare "very likely" on a single source.

### 12. Quote discipline — ≤15 words, ≤1 per source

**What to check:** Full scan of the brief body for direct quotes (text in quotation marks, attributed to an external source).

**Pass criteria:**
- Every direct quote is under 15 words (count words inside quote marks)
- Each source is quoted at most once per brief
- Quotes are in quotation marks with attribution (not paraphrased as if quoted)

**Fail action:**
- If a quote exceeds 15 words: paraphrase, or trim to the essential phrase
- If a source is quoted more than once: keep the most impactful quote, paraphrase the rest
- If a paraphrase is presented as a quote: fix the quotation marks

This is a **Hard Rule per CLAUDE.md** — copyright compliance, not style preference.

### 13. Discord Summary section present and compliant (scheduled briefs only)

**What to check:** Every scheduled brief (morning, afternoon, weekly synthesis, threat detection weekly, threat actor summary) ends with a `## 📣 Discord Summary` section that meets the Layer 2 spec in `doctrine/INTEL-BRIEF-STANDARDS.md`. FLASH briefs and retractions are exempt (they're already short enough to post as-is).

**Pass criteria (scheduled briefs):**
- The `## 📣 Discord Summary` heading exists and is the LAST heading in the file (extractable by reading from heading to EOF)
- Opens with a time-anchored greeting (e.g., `Good morning. Here's your 0800 brief — 2026-05-11.`) with NO themed-character voice
- Every bullet uses `**[Headline text](source-url)**` format — the headline IS the hyperlink, target is the source article URL
- All dates rendered in natural language ("Friday May 9," "April 20," "patches May 13 & 28") — NO ISO format ("2026-05-09")
- Smart Brevity rules (Rules 1, 4, 5, 7 from this checklist) apply — banned phrases zero, active voice, lead with impact, bold the "what"
- No Admiralty digraph, no WEP vocabulary, no finding-id citations (those stay in Layer 1)
- No standing-section "no new activity" boilerplate (Layer 1 still carries those)
- Hard Rule 2 framings preserved where load-bearing ("per X per prior reporting," "Archimedes does not endorse")
- Total Layer 2 word count between 150 and 300 words
- Total Layer 2 character count ≤1900 (hard ceiling — leaves headroom for the librarian's preview/flag prefix on Discord's 2000-char per-message limit). If word count is in band but char count >1900, regenerate with tighter bullets — URLs eat characters fast and a 290-word draft with multiple SecurityWeek/vendor URLs can blow the ceiling

**Pass criteria (FLASH / retraction):** Section absent (exempt).

**Fail action:**
- Section missing on a scheduled brief → compose it from Layer 1 content per the spec
- Themed-character voice detected → strip and re-write straight professional
- ISO dates inside Layer 2 → convert to natural language
- Headline not hyperlinked or pointing at wrong target → fix link
- Word count out of band → compress (over) or expand from Layer 1 (under, but rare — Layer 1 always has more material to draw from)
- Standing-section boilerplate present → remove (Layer 1 keeps it)

This check is the doctrine enforcement boundary for the Discord post format. The librarian extracts and posts this section directly — non-compliance here means a non-compliant Discord post.

---

## Pass/Fail Output Format

After running the checklist, return:

```yaml
preflight_result: passed  # or 'failed'
checks:
  - id: 1
    name: source_url_present
    result: pass
    detail: null
  - id: 2
    name: admiralty_digraph_present
    result: pass
    detail: null
  - id: 3
    name: coverage_log_respected
    result: pass
    detail: null
  - id: 4
    name: lead_with_impact
    result: pass
    detail: null
  - id: 5
    name: banned_phrases_zero
    result: fail
    detail: "'It's worth noting that' appears at line 27"
    remediation: "Remove the phrase; rewrite the sentence using smart-brevity Rule 5"
  - id: 6
    name: standing_sections_present
    result: pass
    detail: null
  - id: 7
    name: wep_vocabulary
    result: pass
    detail: null
  - id: 8
    name: word_count_in_range
    result: pass
    detail: "634 words (target: 400-800)"
  - id: 9
    name: actor_vuln_links
    result: pass
    detail: null
  - id: 10
    name: tlp_marked
    result: pass
    detail: null
  - id: 11
    name: single_source_veto_respected
    result: pass
    detail: null
  - id: 12
    name: quote_discipline
    result: pass
    detail: "2 quotes, 2 sources, max 12 words per quote"
  - id: 13
    name: discord_summary_layer_2
    result: pass
    detail: "section present, 240 words, 1973 chars (≤1900 ceiling met), 5 bullets, all natural-language dates, all source-linked headlines"
summary:
  total_checks: 13
  passed: 12
  failed: 1
  blocking: true
  action_required: "Regenerate active-threats section to remove banned phrase at line 27"
```

---

## What happens when the check fails repeatedly

If three iterations of regenerate-and-recheck fail to produce a passing draft:

1. Halt brief publication
2. Post the failure details to Discord `#intel-briefs` as a `BRIEF GENERATION FAILED` message
3. Log to Splunk with severity=high
4. Wait for human intervention before attempting next scheduled brief

This prevents silent-degradation where the agent keeps re-rolling bad drafts without surfacing the problem.

---

*Last updated: Session 2 scaffold*
*Runs against: every Archimedes brief before publication*
