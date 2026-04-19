# FLASH-POLICY.md — FLASH Alert Policy

> **Archimedes doctrine — async alerting.**
> When FLASH briefs fire, what triggers them, and when they're allowed to wake someone up.

---

## What is a FLASH Brief?

An asynchronous, out-of-cadence intelligence brief fired when something priority-worthy is detected between scheduled brief windows. FLASH briefs are short, single-topic, and action-oriented.

Format specification is in `doctrine/INTEL-BRIEF-STANDARDS.md`.

---

## Trigger Conditions

**Any one of the following triggers a FLASH evaluation.** Evaluation runs the full pipeline (grader → red-team → briefer), so not every trigger produces a posted FLASH — some get rejected during grading.

### Trigger 1 — Critical CVE with active exploitation
- CVE disclosed with CVSS ≥ 9.0
- AND confirmed active exploitation (not PoC, not theoretical)
- AND from an A-grade source

### Trigger 2 — New attribution for a tracked actor
- Finding attributes activity to one of the 22 actors in `_roster.yaml`
- AND the attribution is new (not re-reporting prior attribution)

### Trigger 3 — First-party IOC hit
- Splunk query during alert sweep returns a match on any tracked IOC
- AND match is within the last 24 hours of telemetry
- AND IOC is associated with an actor/campaign we track

### Trigger 4 — Tracked actor TTP change
- New tooling, new targeting, or new infrastructure class documented
- AND from an A/B-grade source
- AND clearly attributable to a tracked actor

### Trigger 5 — Active nation-state campaign vs. A&D sector
- Campaign explicitly targeting aerospace, defense, or watchlist companies
- AND active (not retrospective)
- AND multi-victim (not single-incident)

### Trigger 6 — Zero-day without patch
- Vulnerability disclosed before a patch is available
- AND CVSS ≥ 8.0 OR affects widely-deployed product
- AND exploitation confirmed or imminent per A-grade source

---

## Quiet Hours

**FLASH posting to Discord is restricted to 09:00–21:00 EDT.**

Rationale: Quiet hours don't mean "ignore threats" — they mean "don't interrupt a human at 3am for something still true at 9am."

### Outside Quiet Hours (21:00–09:00 EDT)

FLASH evaluations still run at 00:00 and 06:00 sweeps. If a FLASH is generated:

1. **Queue to `infrastructure/flash-queue.yaml`:**
   ```yaml
   queued_at: 2026-04-18T04:15:00-04:00
   brief_id: flash-2026-04-18-0415
   trigger: trigger-1-cve
   expires_at: 2026-04-18T16:15:00-04:00      # original + 12 hours
   superseded: false
   ```

2. **At 09:00 sweep, the scheduler processes the queue:**
   - If superseded by the 08:00 morning brief → mark `superseded: true`, archive
   - If stale (> 12h from queue time) → log and archive
   - Otherwise → post as catchup FLASH with "QUEUED FROM OVERNIGHT" prefix

### Critical Override — "Actually Wake Up"

**All four conditions must be true simultaneously:**
- CVSS 10.0
- Confirmed active exploitation
- Attributed to a tracked actor
- A&D watchlist entity is named as a target

When all four are met, the FLASH bypasses quiet hours and posts immediately to `#flash-alerts`. This is the once-a-year condition — genuine "wake up the analyst" scenario.

**The agent cannot expand the override conditions.** Human must edit this policy file + `flash-policy.yaml` to change the override rules.

---

## Policy File

Machine-readable version of this policy in `infrastructure/flash-policy.yaml`. The `briefer` and scheduler subagents read the YAML; this markdown is the authoritative specification.

```yaml
# infrastructure/flash-policy.yaml
flash_policy:
  active_hours:
    start: "09:00"
    end: "21:00"
    timezone: "America/New_York"
  
  outside_active_hours:
    behavior: queue
    queue_file: infrastructure/flash-queue.yaml
    catchup_sweep: "09:00"
    staleness_hours: 12
  
  critical_override:
    enabled: true
    conditions_all_of:
      - cvss_score: ">=10.0"
      - active_exploitation: true
      - tracked_actor_involved: true
      - watchlist_sector_targeted: true
  
  triggers:
    - id: critical-cve-exploited
      cvss_min: 9.0
      requires: [active_exploitation, a_grade_source]
    - id: tracked-actor-attribution
      requires: [new_attribution, tracked_actor]
    - id: first-party-ioc-hit
      requires: [splunk_match, ioc_tracked, within_24h]
    - id: tracked-actor-ttp-change
      requires: [a_or_b_grade, attributable, new_ttp]
    - id: ad-sector-campaign
      requires: [active, multi_victim, ad_sector]
    - id: zero-day-no-patch
      cvss_min: 8.0
      requires: [no_patch, exploitation_confirmed_or_imminent]
```

---

## Anti-Noise Rules

FLASH fatigue is a real operational hazard. The following rules prevent it:

1. **One FLASH per trigger topic per 24 hours.** If the same CVE or campaign triggers multiple sweeps, only the first FLASH ships. Subsequent triggers get absorbed into the next scheduled brief with an UPDATE flag.

2. **B2 minimum grade applies to FLASH.** No "unconfirmed but interesting" alerts.

3. **Red-team review is mandatory** for any FLASH with WEP ≥ "very likely." If red-team flags a weakness, FLASH is downgraded or held.

4. **Weekly FLASH count targets:** If Archimedes generates more than 10 FLASH alerts in a 7-day window without any critical overrides, trigger a self-review of FLASH thresholds. Too much noise means the thresholds are too loose.

---

## Queue Expiry Log

FLASH items that queue but never ship are logged to `infrastructure/flash-queue-archive.yaml` for pattern analysis:

```yaml
- queued_at: 2026-04-18T04:15:00-04:00
  brief_id: flash-2026-04-18-0415
  disposition: superseded_by_morning_brief
  supersession_brief: 2026-04-18-morning
```

Patterns of frequent supersession suggest the quiet-hours window might be too conservative. Patterns of frequent staleness suggest triggers are firing on slow-moving events.

---

*Effective: Session 1 scaffold*
*Last reviewed: Session 1 scaffold*
