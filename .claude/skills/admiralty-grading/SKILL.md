---
name: admiralty-grading
description: Use when grading any source-claim pair for intelligence findings — assessing source reliability (A-F) and information credibility (1-6) per NATO AJP-2.1. Invoke before promoting raw signal to findings, before setting WEP ceilings, before assigning inclusion eligibility, when encountering an unfamiliar source, when first-party Splunk telemetry contradicts an external source, or any time a digraph rating is needed. Also invoke when recalibrating an existing finding after new corroboration arrives or when a source's track record changes.
---

# Admiralty Grading Skill

## Purpose

This skill encodes Archimedes's intelligence grading methodology per `doctrine/INTEL-GRADING.md`. It produces a two-character digraph (e.g., `B2`) plus structured rationale that can be embedded directly in a finding's frontmatter.

**You must invoke this skill BEFORE drafting a finding's grade, not after. A grade produced without this skill has not been graded — it has been guessed.**

## Prerequisites

Before invoking this skill, gather:

1. **The source** — publisher, URL, author if known
2. **The claim** — the specific piece of information being graded (a single factual or attributive statement, not an entire article)
3. **Other sources reporting the same claim**, if any — you need these to assess corroboration
4. **Relevant Archimedes Splunk telemetry**, if any — first-party observations may change the grade
5. **Read `infrastructure/source-grades.yaml`** — the authoritative source reliability lookup table

If you cannot gather these, halt and request them. Do not assign a grade on incomplete inputs.

## Procedure

Work the steps in order. Each step produces an output that feeds the next.

### Step 1 — Identify the source(s)

For each source reporting the claim, record:

- Publisher name (e.g., "Mandiant", "Krebs on Security", "anonymous Telegram channel")
- URL
- Publication date
- Whether this source cites another source as its origin

If the claim has one source, proceed. If multiple, keep all of them — they're needed in Step 4.

### Step 2 — Look up source reliability (letter grade)

Query `infrastructure/source-grades.yaml` for each source.

- **Source found in YAML** → use the grade recorded there
- **Source not in YAML** → consult `references/source-grades-cheatsheet.md` to find the closest category match, then assign a provisional grade:
  - Unknown researcher or outlet: **F** (Cannot Be Judged)
  - Anonymous leak or claim: **E** (Unreliable)
  - Previously-unseen aggregator: **C** (Fairly Reliable) provisional, pending review
- **Source is technical (Shodan, VT, Censys, etc.)** → apply dual-grade: **A/F** for facts/attribution split. See "Dual-grade rule" below.

Log the letter grade and record the reasoning in `grade_rationale` (one sentence).

**If you assigned a provisional grade (source not in YAML):** flag this in the output so the librarian subagent can add the source to `source-grades.yaml` and `source-grade-log.md`.

### Step 3 — Assess information credibility (number grade)

Walk the credibility checklist. Do not skip. Do not soft-pedal.

#### 1 — Confirmed — require ALL of:
- [ ] At least one independent source (see Step 4 corroboration rules)
- [ ] Neither source cites the other as its origin
- [ ] Technical artifacts (hashes, IPs, CVEs, domains) match across sources
- [ ] No contradicting higher-grade source exists

#### 2 — Probably True — require ALL of:
- [ ] Consistent with established TTPs for the named actor, OR consistent with known campaign timing/targeting
- [ ] No contradicting evidence from A/B-grade sources
- [ ] Technical claims internally coherent (claimed CVE exists in NVD, claimed infrastructure plausible)

#### 3 — Possibly True — ANY of:
- [ ] Single-source, uncorroborated, but source is B-grade or better
- [ ] Partially consistent with known TTPs but some elements novel
- [ ] Technical claims plausible but not independently verifiable

#### 4 — Doubtful — ANY of:
- [ ] Claim requires multiple unverified assumptions to hold
- [ ] Source is C/D-grade and claim is extraordinary
- [ ] Timing or targeting inconsistent with known actor behavior

#### 5 — Improbable — ANY of:
- [ ] Directly contradicts A-grade reporting
- [ ] Claimed TTPs inconsistent with actor's tradecraft maturity
- [ ] Technical claims violate known constraints (e.g., "exploits Windows 11 via SMBv1 in default config")

#### 6 — Cannot Be Judged
Default when none of 1-5 can be established.

**Rules for working the checklist:**
- Start at 1 and walk down. Assign the highest grade whose conditions are fully met.
- For grades 1 and 2, ALL conditions must be met. For grades 3, 4, 5, any ONE condition suffices (but record which).
- Never round up. Err toward the more cautious grade.
- Record every condition checked as `credibility.checklist_passed` in the output.

### Step 4 — Verify independent corroboration (if claiming grade 1 or ≥"very likely")

Two sources are INDEPENDENT if ALL are true:
- [ ] Different publishing organization
- [ ] Neither cites the other, or a common upstream, as primary origin
- [ ] Different evidence basis (different telemetry, different incident response, different leaked documents)

Two sources are NOT INDEPENDENT if any of:
- One is a rewrite/aggregation of the other (BleepingComputer summarizing Mandiant is not corroboration of Mandiant)
- Both trace to the same original leak/dump
- Both quote the same anonymous source
- Both rely on the same vendor's telemetry

**Test:** If you remove one source, does the other still stand on its own evidence? If no → not independent.

If corroboration fails, downgrade credibility to at most 3 and record `corroboration.independent: false`.

### Step 5 — Apply the single-source veto

A finding CANNOT carry a WEP of "very likely" or higher based on a single source, regardless of the source's letter grade.

**Exception:** First-party Splunk telemetry (index `defenseclaw_local` or `archimedes`) combined with any A/B-grade external source is sufficient for "very likely" on attribution-to-your-environment claims.

If the veto applies, record `single_source_veto_applied: true` and set `wep_ceiling: likely`.

### Step 6 — Check for first-party precedence

If the claim concerns your own environment AND Archimedes Splunk telemetry speaks to it:

- First-party telemetry that **confirms** the external claim → credibility bumps up one step (e.g., 3 → 2)
- First-party telemetry that **contradicts** the external claim → first-party wins; external source gets **downgraded one letter** for this claim type, logged to `source-grade-log.md`

This is Rule 8 from `CLAUDE.md` ("Splunk is first-party"). Non-negotiable.

### Step 7 — Compute WEP ceiling

Based on the final digraph:

| Digraph | Maximum WEP |
|---|---|
| A1, B1 | Almost certainly / Very likely |
| A2, B2 | Very likely (with corroboration) / Likely |
| A3, B3, C2 | Likely |
| C3, D2 | Roughly even chance |
| D3, E-anything | Unlikely or below |
| F, or anything at 6 | Do not make predictive claims |

Apply the single-source veto if it kicks in — cap at "likely" regardless of grade.

### Step 8 — Determine inclusion eligibility

Based on the final digraph and the output thresholds:

| Output | Minimum digraph |
|---|---|
| FLASH brief | B2 |
| Daily brief — action items | B2 |
| Daily brief — monitoring items | C3 |
| Weekly synthesis | C3 |
| Actor profile updates | B2 |
| Raw signal archive | F6 (all) |

Record `inclusion.eligible_for: [array]`.

### Step 9 — Produce the output YAML block

See "Output format" below.

---

## Dual-grade rule for technical sources

Technical enrichment sources (Shodan, Censys, VirusTotal, urlscan.io, WHOIS, HIBP, GitHub code search) are graded separately for **facts** vs **attribution**.

- "Port 445 is open on IP 1.2.3.4" from Shodan → **A1** (facts)
- "That IP belongs to APT29" from Shodan → **F6** (attribution — Shodan cannot assess this)

When grading a technical source, decide which type of claim it's making. If the claim mixes facts and attribution, grade each independently and record both. See `source-grades.yaml` for the full facts/attribution split.

**Exception:** ThreatFox and MalwareBazaar carry community-contributed attribution (**B/B**). Still corroborate before treating as confirmed.

---

## Output format

Return a YAML block the grader subagent pastes into the finding's frontmatter:

```yaml
digraph: B2
source_reliability:
  grade: B
  source_name: Krebs on Security
  source_yaml_id: krebs-on-security
  grade_rationale: >
    Pre-assigned B per source-grades.yaml. Strong track record, well-sourced reporting.
  provisional: false
credibility:
  grade: 2
  checklist_passed:
    - probably_true_ttp_consistent
    - probably_true_no_contradicting_ab
    - probably_true_claims_coherent
  rationale: >
    Consistent with UNC1549 established TTPs against CMMC-adjacent suppliers;
    no contradicting A/B source; CVE-2024-XXXX is verified in NVD.
corroboration:
  independent_sources:
    - krebs-on-security
    - mandiant-m-trends-2026
  independent: true
  test_passed: "Mandiant report stands on its own telemetry; Krebs has separate IR source"
first_party_precedence:
  applied: false
  splunk_evidence: null
single_source_veto_applied: false
wep_ceiling: very_likely
inclusion:
  eligible_for:
    - flash
    - daily_brief_action
    - weekly_synthesis
    - actor_profile_update
graded_at: 2026-04-23T14:30:00Z
graded_by: grader
```

**All fields are required.** Set nulls explicitly rather than omitting.

---

## Failure modes — when to halt instead of grading

Return a halt signal (not a grade) when:

1. **Source cannot be identified** — URL leads to a deleted page, Telegram channel with no name, etc. Flag to collector for re-fetch.
2. **Claim is not a single assertion** — the input bundles multiple claims (e.g., "APT28 is using CVE-X AND targeting aerospace AND operating from Russia"). Return the input to the grader subagent with: "break into separate claims and regrade each."
3. **Credibility checklist returns contradictory signals** — e.g., conditions 1 and 5 both seem to apply. This usually means the claim is actually multiple claims. Halt and ask for decomposition.
4. **Corroboration evaluation requires external fetching** you cannot perform. Halt and request the missing sources.
5. **Source in YAML but marked `deprecated: true`** — flag and request a current replacement source.

Halt format:

```yaml
status: halt
reason: source_not_identifiable
detail: "Twitter handle @cybersec_intel_247 deleted between collection and grading"
action_requested: "Re-collect from archive.org or downgrade source to F"
```

---

## Worked examples

### Example 1 — Clean A1

**Input:**
- Source: CISA Advisory AA24-XXXX
- Claim: "CVE-2024-1234 is being exploited in the wild against U.S. defense contractors"
- Corroboration: Mandiant M-Trends 2026 reports same CVE exploitation against A&D sector

**Process:**
- Step 2: CISA → **A** (per source-grades.yaml)
- Step 3: Walk credibility checklist:
  - Independent corroboration? Yes, Mandiant is independent of CISA.
  - Neither cites the other? Yes.
  - Technical artifacts match? Yes (CVE-2024-1234 consistent).
  - No contradicting A-grade? None.
  - → Grade **1 (Confirmed)**
- Step 4: Confirmed independent.
- Step 5: Two sources → veto does not apply.
- Step 6: No Splunk contradiction.
- Step 7: A1 → WEP ceiling "almost certainly" or "very likely"
- Step 8: A1 → eligible for FLASH, daily brief, weekly, actor profile

**Output:** `digraph: A1`, eligible for all outputs.

### Example 2 — Single-source veto in action

**Input:**
- Source: Mandiant blog post
- Claim: "UNC1549 has shifted TTPs to include supply chain compromise of A&D Tier 2 suppliers"
- Corroboration: none yet

**Process:**
- Step 2: Mandiant → **A**
- Step 3: Walk credibility checklist:
  - Grade 1 fails (no independent corroboration).
  - Grade 2: Consistent with UNC1549 known TTPs? Yes. No contradicting A/B? None. Technical claims coherent? Yes.
  - → Grade **2 (Probably True)**
- Step 4: Corroboration failed (single source).
- Step 5: Single-source veto kicks in. Even with A2, WEP cannot exceed "likely".
- Step 7: WEP ceiling = **likely** (not "very likely")
- Step 8: A2 → eligible for FLASH, daily brief, weekly, actor profile

**Output:** `digraph: A2`, `single_source_veto_applied: true`, `wep_ceiling: likely`.

### Example 3 — Miscalibration (what NOT to do)

**Bad reasoning:** "It's from Mandiant, so A1."

**Why this is wrong:**
- Mandiant's reliability is A, but that's only the letter.
- A1 requires independent corroboration. A single-source Mandiant claim is at most A2.
- Going straight from source grade to digraph skips the entire credibility checklist.

**Fix:** Always walk the credibility checklist. Letter grade is not the digraph.

### Example 4 — Dual-grade technical source

**Input:**
- Source: Shodan scan result
- Claim A: "IP 192.0.2.50 has port 8080 open with Apache 2.4.41"
- Claim B: "IP 192.0.2.50 is infrastructure used by APT29"

**Process:**
- Grade each claim separately.
- Claim A (facts): Shodan → **A1** (Shodan is authoritative for open ports observed at scan time)
- Claim B (attribution): Shodan → **F6** (Shodan cannot attribute infrastructure)
- For Claim B to be any usable grade, need a separate A/B source attributing that IP to APT29.

**Output:** Two separate digraphs for two separate claims. Do not merge.

---

## Grade revision logging

If grading a claim reveals that a source's track record should change (e.g., Krebs reported something that turned out to be wrong), propose a grade revision by returning:

```yaml
source_grade_revision_proposed:
  source_yaml_id: krebs-on-security
  current_grade: B
  proposed_grade: C
  reason: "Claim X from YYYY-MM-DD was contradicted by higher-grade source on YYYY-MM-DD; second miss in 90-day window"
  severity: downgrade_requires_review
  action: "Post to Discord #actor-review for human sign-off before committing"
```

Per doctrine: downgrades of B→D or worse require human review before commit. Upgrades of C→B require three corroborated hits in a rolling 90-day window. The librarian subagent handles the logging; this skill just surfaces the proposal.

---

## References

- `doctrine/INTEL-GRADING.md` — full doctrine (source of truth)
- `infrastructure/source-grades.yaml` — authoritative source reliability lookup
- `references/source-grades-cheatsheet.md` — human-readable explanation of source categories (load on demand)
- `CLAUDE.md` Hard Rules 6, 8 — quote limits and first-party precedence
