---
name: threat-box-scoring
description: Use when scoring a threat actor against the Archimedes target profile (ad-prime-v1) per Andy Piazza's Threat Box methodology. Invoke when the actor-profiler creates a new actor dossier, when a tracked actor's 90-day review cycle comes due, when a review trigger fires (new attribution, new tooling, CVE exploitation linked, major campaign disclosure, first-party IOC observation), or when ad-hoc rescoring is requested. This skill produces a full threat-box.yaml — scoring all five attack categories (espionage, supply chain, destructive, disruptive, cyber-crime), applying willingness and novelty modifiers, applying IOC corroboration bonuses from Splunk observations, computing weighted overall score, assigning threat level, and determining authority level. HIGH overall scores halt auto-commit and require /approve-scoring via Discord.
---

# Threat Box Scoring Skill

## Purpose

This skill scores threat actors against Archimedes's target profile using the Threat Box methodology from `doctrine/THREAT-BOX-METHODOLOGY.md`. The output is a complete `threat-box.yaml` file ready to land in `threats/threat-actors/<actor>/`.

**Judgment + arithmetic = scoring.** The agent provides judgment (evidence adequacy, source grading, novelty assessment). The bundled `compute-threat-box.py` script provides arithmetic (final scores, composites, weighted overall, threat level, authority). This separation prevents math errors and keeps the skill focused on what humans are bad at verifying: did you actually see enough evidence to justify Intent=5?

## Prerequisites

Before invoking, gather:

1. **Actor identity** — `actor_id` from `threats/threat-actors/_roster.yaml` and `actor_name`
2. **Target profile** — always `ad-prime-v1` for Archimedes v1
3. **Graded evidence per category** — each Intent and Capability claim must cite Admiralty-graded sources. If the `admiralty-grading` skill hasn't graded them yet, do that first.
4. **First-party Splunk status** — has the actor's infrastructure been observed in `defenseclaw_local` or `archimedes` index? If unsure, ask the orchestrator to query Splunk before scoring.
5. **Geopolitical posture** — what's the willingness modifier baseline? Russia/China/Iran/DPRK = 0. Moderate-ties country = -1. Close US ally = -2.
6. **Tooling signature** — is the actor using custom, semi-custom, or commodity tooling? This drives the novelty modifier.

**Do not score on incomplete inputs.** If evidence is thin in a category, assign the lower score — never inflate.

## Procedure

### Step 1 — Score each of five categories

For each of `espionage`, `supply_chain`, `destructive`, `disruptive`, `cyber_crime`:

#### Score Intent (1-5)

Answer: *Why would this actor target THIS organization with THIS attack type?*

| Score | When to assign |
|---|---|
| **5 — Target-Specific** | Actor has demonstrated objective achievable ONLY within A&D primes (e.g., classified R&D theft, ITAR-controlled data). Requires at least 1 A-grade source. |
| **4 — Ideology Association** | Actor targets based on ideology (anti-NATO, anti-Western, pro-nation-state). Requires 2 B-grade or 1 A-grade source. |
| **3 — Sector Association** | Actor targets the broader A&D / defense / manufacturing sector without specific aim at A&D primes. Requires 2 B-grade or 1 A-grade source. |
| **2 — Regional Association** | Actor targets US or Western entities generally. |
| **1 — Target of Opportunity** | Actor is opportunistic; hits whoever is exposed. |

**Red flag:** If you're tempted to score Intent=5 but your evidence is "this actor hits government entities and A&D is government-adjacent," downgrade to Intent=3. Target-Specific requires direct, documented targeting of our profile.

#### Score Willingness Modifier (0, 1, or 2 — subtracted from Intent)

| Modifier | When to assign |
|---|---|
| **0 — No Constraints** | Strained diplomatic relations, active hostilities, sanctions regime. Russia, China, Iran, DPRK, most criminal groups. |
| **1 — Moderate Constraints** | Moderate US diplomatic/economic ties (e.g., some Middle Eastern states, certain post-Soviet states) |
| **2 — Strong Constraints** | Close US ally with strong security cooperation (EU NATO members, Five Eyes, Japan, South Korea, Israel). Very rare this applies to threat actors. |

#### Score Capability (1-5)

Answer: *What evidence exists that this actor is capable of this attack type?*

| Score | When to assign | Minimum evidence |
|---|---|---|
| **5 — Significant** | Multiple confirmed campaigns in last 24 months | Multiple A-grade sources AND documented active use within 24 months |
| **4 — Credible** | Multiple campaigns or one extensively documented | 1 A-grade source OR 2 B-grade sources |
| **3 — Limited** | Some evidence across a few incidents | Any documented source, grade noted |
| **2 — Possible** | Feasibility confirmed but limited evidence | Any documented source |
| **1 — Not Capable** | No evidence this actor has performed this attack type | N/A |

**Red flag:** If your evidence is "this actor is nation-state and nation-states can do X," that's not evidence of capability X. Score Capability=1 if there's genuinely no evidence, not 3 as a hedge.

#### Score Novelty Modifier (0, 1, or 2 — subtracted from Capability)

| Modifier | When to assign |
|---|---|
| **0 — Custom/Advanced** | Custom toolset per campaign, living-off-the-land, cloud-native C2, novel evasion |
| **1 — Semi-Custom** | Limited-availability or high-cost toolset across multiple campaigns (e.g., nation-state tooling that has been identified) |
| **2 — Commodity** | Generally available: Cobalt Strike, Metasploit, off-the-shelf stealers, public PoCs |

**Important:** Novelty measures *defensive difficulty*, not actor prestige. A nation-state using commodity tools scores -2 because defenders have signatures for commodity tools. This reduces the actor's *effective* capability against well-defended targets.

#### IOC Corroboration Check

For each category, determine: has this actor's infrastructure been observed in our Splunk?

If yes:
- `observed: true`
- `splunk_search: "index=defenseclaw_local <specific query>"`
- `first_seen: <timestamp>`
- `bonus_category: <the specific category where the IOC applies>` — the +1 bonus only applies to the category the observation relates to, not globally

If no: `observed: false, bonus_category: null`

### Step 2 — Assemble the raw input YAML

Format the scores into the input schema for `compute-threat-box.py`:

```yaml
actor_id: "006"
actor_name: "APT28"
target_profile: "ad-prime-v1"
scored_at: "2026-04-23"
scored_by: "actor-profiler"
scoring_version: 1
scores:
  espionage:
    intent:
      score: 5
      willingness_modifier: 0
    capability:
      score: 5
      novelty_modifier: 0
    ioc_corroboration:
      observed: false
      bonus_category: null
  supply_chain: { ... }
  destructive: { ... }
  disruptive: { ... }
  cyber_crime: { ... }
```

All five categories required. Missing category = validation error.

### Step 3 — Run the compute script

Execute:

```bash
python scripts/compute-threat-box.py --input /tmp/raw-scores.yaml > /tmp/computed.yaml
```

Or via stdin:

```bash
cat /tmp/raw-scores.yaml | python scripts/compute-threat-box.py --stdin > /tmp/computed.yaml
```

**Script exit codes:**
- `0` — scored successfully (LOW or MEDIUM overall), can auto-commit
- `1` — input validation error, script writes errors to stdout
- `2` — HIGH overall threat level detected, `reviewed_by: null`, requires `/approve-scoring`

### Step 4 — Attach evidence and narrative

The script output has the numeric scoring complete. Now enrich with the judgment fields that don't compute from inputs:

For each category, add:
- `intent.evidence` — multi-line narrative citing specific sources
- `intent.sources` — array of `source_brief_id` references
- `intent.label` — human-readable label (e.g., "target-specific")
- `willingness.evidence` — one-sentence justification
- `willingness.label` — human-readable label (e.g., "no-constraints")
- `capability.evidence` — multi-line narrative citing specific sources
- `capability.sources` — array of `source_brief_id` references
- `capability.label` — human-readable label (e.g., "significant")
- `novelty.evidence` — one-sentence justification
- `novelty.label` — human-readable label (e.g., "custom-advanced")
- `ioc_corroboration.note` — human-readable description of the Splunk observation, or "No first-party IOC hits at time of scoring"

See `references/evidence-examples.md` for fully-written examples from the APT28 exemplar.

### Step 5 — Handle authority per threat level

Based on `overall.threat_level`:

**LOW (weighted 2-4):**
- `reviewed_by: auto-committed`
- Write file, commit to main, update `_roster.yaml` status
- Librarian logs to Splunk

**MEDIUM (weighted 5-7):**
- `reviewed_by: auto-committed`
- Write file, commit to main
- Post summary to Discord `#actor-review` as FYI (not blocking)
- Librarian logs to Splunk

**HIGH (weighted 8-10):**
- `reviewed_by: null` (script sets this automatically)
- Write file with status `scored_pending_approval`
- **Do NOT commit to main yet**
- Post scoring summary to Discord `#actor-review`
- Wait for `/approve-scoring <actor-id>` in Discord
- On approval, update `reviewed_by` with approver's handle and commit

This is **Hard Rule 5 from CLAUDE.md** — human sign-off for HIGH threat levels is non-negotiable.

### Step 6 — Review policy setup

The script sets `next_review_due` 90 days from `scored_at`. Review triggers are pre-populated from doctrine. The `actor-profiler`'s weekly task picks the actor with the nearest `next_review_due`.

## Output format

The final `threat-box.yaml` structure:

```yaml
actor_id: "006"
actor_name: "APT28"
target_profile: "ad-prime-v1"
scored_at: "2026-04-23"
scored_by: "actor-profiler"
reviewed_by: null                     # awaiting /approve-scoring if HIGH, else auto-committed
scoring_version: 1

scores:
  espionage:
    intent:
      score: 5
      label: target-specific
      willingness_modifier: 0
      evidence: |
        <multi-line justification citing specific sources>
      sources: [source-1, source-2]
    willingness:
      modifier: 0
      label: no-constraints
      evidence: "<one-sentence justification>"
    capability:
      score: 5
      label: significant
      novelty_modifier: 0
      evidence: |
        <multi-line justification>
      sources: [source-3, source-4]
    novelty:
      modifier: 0
      label: custom-advanced
      evidence: "<one-sentence justification>"
    ioc_corroboration:
      observed: false
      bonus_category: null
      note: "No first-party IOC hits at time of initial scoring."
    final_intent: 5
    final_capability: 5
    composite: 10
    threat_level: HIGH
    ioc_bonus_applied: 0
  supply_chain: { ... }
  destructive: { ... }
  disruptive: { ... }
  cyber_crime: { ... }

overall:
  weighted_score: 7.35
  weights_used:
    espionage: 0.35
    supply_chain: 0.20
    destructive: 0.15
    disruptive: 0.15
    cyber_crime: 0.15
  threat_level: MEDIUM
  authority_level: actor-profiler-autonomous-with-notification

review_policy:
  interval_days: 90
  last_reviewed: "2026-04-23"
  next_review_due: "2026-07-22"
  review_triggers:
    - new_attribution_from_a_source
    - new_tooling_documented
    - cve_exploitation_linked_to_actor
    - major_campaign_disclosure
    - first_party_ioc_observation

status: scored                        # or 'scored_pending_approval' for HIGH
```

Every field required. Nulls must be explicit.

## Corresponding human-readable file

In addition to `threat-box.yaml`, generate `threat-box.md` — a markdown rendering of the same content for human review. The md file follows the actor's `profile.md` conventions. See `references/threat-box-md-template.md`.

## Failure modes

Return a halt signal (not a score) when:

1. **Evidence minimum not met** — e.g., scoring Intent=5 but only have C-grade sources. Downgrade or halt for better evidence.
2. **Actor not in `_roster.yaml`** — halt, request `/new-actor` command first.
3. **`admiralty-grading` has not been run** on the cited sources — halt, run grading first.
4. **Script validation error** (invalid input YAML) — halt, fix inputs, rerun.
5. **IOC corroboration claimed but no Splunk evidence file** — halt, require `splunk_search` field before applying bonus.

Halt format:

```yaml
status: halt
reason: evidence_minimum_not_met
detail: "Scored Intent=5 for supply_chain but only C-grade sources cited; requires 1 A-grade or 2 B-grade."
action_requested: "Downgrade to Intent=3 or locate A/B-grade source before rescoring"
```

## Worked examples

### Example 1 — Nation-state actor (APT28)

**Inputs:**
- Espionage: Intent=5 (DoJ indictment, NSA/CISA advisory = A-grade target-specific targeting), Cap=5 (MSTIC, Unit 42, NCSC, ESET, Trellix), Novelty=0 (custom tooling per campaign)
- Supply Chain: Intent=4 (sector targeting via NATO logistics, B-grade+ evidence), Cap=4 (M-grade capability)
- Destructive: Intent=2 (rare for APT28), Cap=3 (limited evidence)
- Disruptive: Intent=3 (occasional), Cap=4 (credible)
- Cyber-Crime: Intent=1 (not their MO), Cap=2 (feasibility)
- Willingness: 0 everywhere (Russia, active hostilities)
- Novelty: 0 everywhere (custom tooling)

**Script output:**
- Espionage composite: 10 → HIGH (category level)
- Overall weighted: 7.35 → MEDIUM (authority level)
- Authority: `actor-profiler-autonomous-with-notification`
- Auto-commit with Discord notification

**Note:** The HIGH designation on espionage is preserved in the YAML — the `overall` level just determines the approval gate.

### Example 2 — IOC corroboration changes the picture

**Same actor as Example 1, but** first-party Splunk observes APT28 infrastructure:

```yaml
ioc_corroboration:
  observed: true
  splunk_search: "index=defenseclaw_local src_ip=70.34.253.247"
  first_seen: "2026-04-15T08:22:00Z"
  bonus_category: espionage
```

**Effect:**
- Espionage Capability was already 5 → stays 5 (ceiling)
- But this is a significant change in the assessment narrative
- The `ioc_corroboration.observed: true` should trigger a review immediately

Since the actor is ALREADY at their ceiling Capability, the +1 bonus has no numeric effect — but the observation itself is a material event that bumps `next_review_due` to today and fires a FLASH sweep for that category.

### Example 3 — Criminal ransomware group

**Inputs:**
- Cyber-Crime: Intent=2 (regional; targets US firms broadly, not A&D specifically), Cap=5 (well-documented ransomware ops)
- Destructive: Intent=1 (wipers aren't their MO), Cap=2 (feasibility only)
- Disruptive: Intent=2, Cap=4 (encryption-disruption well-documented)
- Espionage: Intent=1, Cap=2 (some data theft alongside encryption)
- Supply Chain: Intent=2, Cap=3 (SolarWinds-era concern but historical)
- Willingness: 0 (criminal group, no constraints)
- Novelty: 2 (Cobalt Strike + commodity RaaS tooling)

**Script output:**
- Cyber-Crime: final_cap = 5 - 2 = 3; composite = 2 + 3 = 5 → MEDIUM
- Destructive: composite = 1 + (2-2=1, floor=1) = 2 → LOW
- Disruptive: composite = 2 + (4-2=2) = 4 → LOW
- Espionage: composite = 1 + (2-2=1, floor=1) = 2 → LOW
- Supply Chain: composite = 2 + (3-2=1, floor=1) = 3 → LOW
- Overall weighted: `2×0.35 + 3×0.20 + 2×0.15 + 4×0.15 + 5×0.15 = 0.7+0.6+0.3+0.6+0.75 = 2.95` → LOW
- Authority: `actor-profiler-autonomous`
- Auto-commit, no Discord notification

### Example 4 — Evidence minimum not met (halt)

**Input attempt:** Score a new actor with Intent=5 on Espionage, but the only cited source is a D-grade Telegram post claiming the actor targets A&D contractors.

**Result:**
```yaml
status: halt
reason: evidence_minimum_not_met
detail: "Intent=5 (Target-Specific) requires 1 A-grade source documenting targeting of ad-prime-v1 profile. Cited source is D-grade (unverified Telegram channel)."
action_requested: "Downgrade Intent to 1 (Target of Opportunity) until A-grade evidence is available, OR find corroborating A/B-grade source."
```

Do not proceed with scoring until evidence meets minimum.

## Migration note for Session 1 APT28

The Session 1 `threat-box.yaml` for APT28 uses a slightly different structure and has `reviewed_by: null` awaiting `/approve-scoring 006`. When this skill runs next against APT28:

- Weighted score will compute to ~7.35 (MEDIUM overall)
- New authority rule auto-commits MEDIUM
- Recommend: manually run `/approve-scoring 006` first to close the Session 1 gate, then let future scoring runs update under the new rule

This migration decision is the orchestrator's to make, not the skill's.

## References

- `references/evidence-examples.md` — fully-written evidence narratives from APT28 exemplar
- `references/threat-box-md-template.md` — human-readable threat-box.md template
- `scripts/compute-threat-box.py` — deterministic scoring arithmetic
- `doctrine/THREAT-BOX-METHODOLOGY.md` — full doctrine (source of truth)
- `threats/threat-actors/APT28/threat-box.yaml` — canonical schema example
- `CLAUDE.md` Hard Rule 5 — human sign-off for HIGH threat levels

## Interaction with other skills

- `admiralty-grading` grades the sources that feed this skill's evidence fields. Run that first; this skill consumes the graded output.
- `ioc-extraction` surfaces attribution claims and IOCs; when IOCs are confirmed in first-party Splunk, this skill applies the +1 bonus.
- The `actor-profiler` subagent is the primary consumer of this skill.
