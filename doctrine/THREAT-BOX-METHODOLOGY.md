# THREAT-BOX-METHODOLOGY.md — Actor Scoring

> Based on Andy Piazza's Threat Box framework (SANS Whitepaper #39585)
> Adapted for Aerospace & Defense targeting
> Reference: https://klrgrz.medium.com/quantifying-threat-actors-with-threat-box-e6b641109b11

---

## Purpose

Threat Box answers the question executives ask: **"Which threat actor should I care about, and why?"**

Standard risk models quantify organizational vulnerabilities. Threat Box quantifies the **human element** — specific actor intentions and capabilities against a defined target organization.

---

## Target Organization Profile

All scores are assessed against this anchor:

> **A mid-to-large US aerospace and defense contractor** — ITAR-regulated, holding US government contracts, engaged in aircraft, spacecraft, missile, or defense system development, with a Tier-1/2 supplier network and classified/sensitive R&D programs.

Every Intent score answers: *"Why would this actor target THIS organization?"*

Target profile identifier: `ad-prime-v1` (referenced in every `threat-box.yaml`).

---

## Attack Categories

Each actor is scored across five dimensions (four standard + one A&D-specific):

| Category | CIA Triad | Question |
|---|---|---|
| **Espionage** | Confidentiality | Can/will they steal our IP, data, or personnel information? |
| **Destructive** | Integrity | Can/will they corrupt, wipe, or damage our systems? |
| **Disruptive** | Availability | Can/will they take our systems offline? |
| **Cyber-Crime** | Financial | Can/will they extort us for near-term financial gain? |
| **Supply Chain** | All three | Can/will they compromise our suppliers, contractors, or shared software to reach us? |

**Ransomware disambiguation:**
- Legitimate extortion → Cyber-Crime
- Wiper disguised as ransomware → Destructive

**IP theft disambiguation:**
- No immediate monetization → Espionage
- Immediate sale → Cyber-Crime

---

## Scoring Dimensions

### Intent (1–5)

*Why would this actor target this organization with this attack type?*

| Score | Label | Definition |
|---|---|---|
| **5** | Target-Specific | Actor targets based on an objective achievable ONLY within our network |
| **4** | Ideology Association | Actor targets based on association with a specific ideology |
| **3** | Sector Association | Actor targets based on sector (aerospace, defense, manufacturing, technology) |
| **2** | Regional Association | Actor targets based on geographic area of operations |
| **1** | Target of Opportunity | Actor targets because we are exposed and exploitable |

### Willingness Modifier (subtract from Intent)

| Modifier | Label | Definition |
|---|---|---|
| **-0** | No Constraints | Strained diplomatic relations, hostilities, or significant economic disruption. Applies to Russia, China, Iran, DPRK, and most criminal groups. |
| **-1** | Moderate Constraints | Moderate diplomatic/economic ties with the US |
| **-2** | Strong Constraints | Strong diplomatic, economic, and security ties with the US |

### Capability (1–5)

*What evidence exists that this actor is capable of this attack type?*

| Score | Label | Definition |
|---|---|---|
| **5** | Significant | Significant evidence of prior activity, confirmed by multiple trusted sources |
| **4** | Credible | Credible evidence, moderately confirmed |
| **3** | Limited | Some evidence, limited sources |
| **2** | Possible | Very limited evidence, feasibility confirmed |
| **1** | Not Capable | No evidence of capability |

### Novelty Modifier (subtract from Capability)

| Modifier | Label | Definition |
|---|---|---|
| **-0** | Custom/Advanced | Custom toolset per campaign with demonstrated living-off-the-land capability. Hardest to detect/defend. |
| **-1** | Semi-Custom | Limited-availability or high-cost toolset across multiple campaigns |
| **-2** | Commodity | Generally available toolset (Cobalt Strike, off-the-shelf malware, public exploits) |

**Key insight:** Novelty measures *defensive difficulty*, not attacker sophistication. A nation-state using commodity tools scores -2 even if technically elite — the point is: common tools = defenders have better detection signatures.

---

## Minimum Evidence Requirements

**Scores must be grounded in Admiralty-graded evidence. The `actor-profiler` subagent cannot assign scores without citing supporting sources in the `evidence` field.**

| Score | Requirement |
|---|---|
| **Intent = 5 (Target-Specific)** | At least one A-grade source documenting targeting of our specific profile |
| **Intent = 4 (Ideology)** | Two B-grade sources OR one A-grade source |
| **Intent = 3 (Sector)** | Two B-grade sources OR one A-grade source |
| **Capability = 5 (Significant)** | Multiple A-grade sources AND documented active use within last 24 months |
| **Capability = 4 (Credible)** | One A-grade source OR two B-grade sources |
| **Capability ≤ 3** | Any documented source, grade noted |

If evidence requirements are not met, score must be lower. The `actor-profiler` cannot "estimate" a higher score.

---

## IOC Corroboration Bonus

**If an actor's IOCs appear in your first-party Splunk telemetry (`defenseclaw_local` or `archimedes` index), their Capability score for attacks against *your environment* gets +1 (capped at 5).**

This reflects the reality that a generic A-grade capability assessment from external reporting is one thing; evidence the actor has actually reached your perimeter is another. First-party observation materially changes the defensive calculus.

The bonus is applied to the specific attack category where the IOC was observed, not globally. Logged in the `threat-box.yaml` under `ioc_corroboration`:

```yaml
ioc_corroboration:
  observed: true
  splunk_search: "index=defenseclaw_local 70.34.253.247"
  first_seen: 2026-04-15T08:22:00Z
  capability_bonus_applied_to: [espionage]
  bonus_value: +1
```

---

## Calculating Final Scores

```
Final Intent     = Intent Score - Willingness Modifier value
Final Capability = Capability Score - Novelty Modifier value + IOC Corroboration Bonus

Floor = 1. Ceiling = 5. Scores cannot go below 1 or above 5.
```

**Composite Score** (per category) = Final Intent + Final Capability
- Minimum: 2 · Maximum: 10

**Overall A&D Priority Score** = Weighted average across categories:
- Espionage: 35% weight
- Supply Chain: 20% weight
- Destructive: 15% weight
- Disruptive: 15% weight
- Cyber-Crime: 15% weight

---

## Threat Level Thresholds

| Composite Score | Threat Level |
|---|---|
| 8–10 | 🔴 HIGH |
| 5–7 | 🟡 MEDIUM |
| 2–4 | 🟢 LOW |

---

## Scoring Authority

| Threat Level | Authority |
|---|---|
| LOW (2–4) | `actor-profiler` autonomous — commit directly |
| MEDIUM (5–7) | `actor-profiler` autonomous, human notified in `#actor-review` |
| **HIGH (8–10)** | **`actor-profiler` proposes, human confirms before commit** |

For HIGH-level proposals:
1. `actor-profiler` writes `threat-box.yaml` with `reviewed_by: null`
2. Posts scoring summary to Discord `#actor-review`
3. Waits for `/approve-scoring <actor-id>` in Discord
4. On approval, `reviewed_by` is populated and file is committed

---

## Review Policy

Every `threat-box.yaml` carries:

```yaml
review_policy:
  interval_days: 90
  last_reviewed: 2026-04-18
  next_review_due: 2026-07-17
  review_triggers:          # events that force early review
    - new_attribution_from_a_source
    - new_tooling_documented
    - cve_exploitation_linked_to_actor
    - major_campaign_disclosure
    - first_party_ioc_observation
```

The `actor-profiler` runs a weekly task: pick the actor whose `next_review_due` is nearest, re-score, update.

---

## Rules of Engagement

1. **Evidence-based only.** No "what-if monster" — don't score theoretical capability.
2. **Target-focused.** Scores are relative to `ad-prime-v1`, not generic.
3. **Admiralty grade applies.** Scoring inherits the reliability of underlying intel. Log confidence.
4. **Disrupted actors.** Scores reflect historical capability. Active threat level is noted separately in `status`.
5. **No score inflation.** If a source says "suspected," you do not upgrade to "confirmed" in your scoring evidence.

---

## Output Files

Per actor:
- `threats/threat-actors/{ACTOR}/threat-box.yaml` — structured scoring (agent-queryable)
- `threats/threat-actors/{ACTOR}/threat-box.md` — human-readable rationale (generated from yaml)

Repo-wide:
- `threats/threat-actors/threat-matrix.md` — cross-actor ranked view (regenerated on any score change)

Tool reference: https://github.com/OllieJC/tbat (YAML export compatible)

---

*Methodology by Andy Piazza (SANS) · A&D adaptation and Archimedes implementation by Ryan*
*Last reviewed: Session 1 scaffold*
