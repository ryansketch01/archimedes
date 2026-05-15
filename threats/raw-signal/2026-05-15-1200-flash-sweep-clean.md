---
raw_id: raw-2026-05-15-1200-flash-sweep-clean
collected_at: 2026-05-15T12:00:00-04:00
run_id: flash-sweep-20260515-120000
collection_mode: flash_sweep
source:
  source_yaml_id: meta-sweep-tombstone
  source_name: "FLASH sweep tombstone (no candidates)"
  source_url: null
  published_at: 2026-05-15T12:00:00-04:00
match_reason:
  watchlist: []
  actors: [TeamPCP]
  vulnerabilities: [CVE-2026-42897, CVE-2026-20182]
  keywords: []
triage_tags: [flash_sweep_clean, audit_trail, non_flash]
iocs_extracted: false
iocs_count: 0
text_word_count: 0
promoted: false
ttl_expires_at: 2026-08-13T12:00:00-04:00
test: false

sweep_summary:
  sweep_window_start: 2026-05-15T06:00:00-04:00
  sweep_window_end: 2026-05-15T12:00:00-04:00
  sweep_window_hours: 6
  scope_rationale: "Async FLASH sweep per orchestrator instruction. Prior FLASH was 06:00 EDT (2 triggers, 2 queued to flash-queue.yaml — Exchange CVE-2026-42897 zero-day + TeamPCP Shai-Hulud source release/BreachForums bounty — both posted by 09:00 catchup or absorbed by 08:00 morning brief). 08:00 morning brief shipped 4h before sweep covered: TeamPCP three convergent supply-chain surfaces 96h (Shai-Hulud source release + BreachForums bounty + Mistral 450-repo $25K BIN), Exchange on-prem zero-day CVE-2026-42897 MSRC Exploitation Detected no GA patch ESU-only, Cisco SD-WAN sustained-focus CVE-2026-20182 KEV T-2, Copy Fail KEV EOD-today carry-forward. Quiet hours: 12:00 EDT IS INSIDE the 09:00–21:00 EDT active window — any FLASH would post immediately."
  sources_queried: 15
  sources_skipped_stale: 0
  sources_blocked_this_sweep: 0
  items_fetched_in_window: 14
  items_already_covered_anti_noise: 4    # all 4 watchlist/actor matches were anti-noise dedup against 06:00 FLASH + 08:00 morning brief
  items_evaluated_against_flash_triggers: 4
  flash_candidates: 0
  brief_update_candidates_for_afternoon: 1   # Mandiant GTIG TeamPCP→UNC6780 alias (2026-05-11, out-of-window) — /update-tracking candidate
  source_health_changes: []                  # 5 single-observation 404/parse errors not promoted to stale; Mandiant feedburner remains in known-bad state (failure_count 18+, 9 days)
---

# FLASH sweep 2026-05-15 12:00 EDT — clean (0 triggers, 1 awareness item)

**0 FLASH triggers fired. 0 candidates queued. 1 awareness-pile item recorded for operator (Mandiant GTIG TeamPCP→UNC6780 alias mapping, out-of-window — /update-tracking candidate). Window: 2026-05-15 06:00 EDT → 2026-05-15 12:00 EDT (6 hours, post-06:00-FLASH-queued + post-08:00-morning-brief).**

Quiet hours: 12:00 EDT is INSIDE the 09:00–21:00 EDT active window. Had any trigger fired, the FLASH would have been eligible for immediate Discord post (no queue). No critical-override conditions met.

## Sweep window

2026-05-15T06:00:00-04:00 → 2026-05-15T12:00:00-04:00 (6h, post-06:00-FLASH + post-08:00-morning-brief)

## Sweep telemetry

| Metric | Value |
|---|---|
| Sources queried | 15 |
| Items fetched in window | 14 |
| Items matching watchlists / tracked actors | 4 |
| Items evaluated against FLASH triggers | 4 |
| Items deduplicated against prior coverage (anti-noise) | 4 |
| FLASH candidates | 0 |
| Critical override applied | false |
| Quiet hours active | false (12:00 EDT inside 09:00–21:00 EDT) |

## FLASH trigger evaluation

All 6 FLASH triggers evaluated. None fired.

### Trigger 1 — Critical CVE actively exploited (CVSS ≥9.0 + active exploitation + A-grade primary)

- **Exchange CVE-2026-42897 in-window restatement** — Microsoft MSRC and downstream relays (BleepingComputer, The Hacker News, SecurityWeek) restated the on-prem Exchange Server 2016/2019/SE zero-day in window. MSRC "Exploitation Detected" tag unchanged from 06:00 sweep. No fresh exploitation claim, no fresh IOC publication, no new GA patch announcement (ESU-only path unchanged). **FAILS on anti-noise** — already FLASHed at 06:00 (queued, posted by 09:00 catchup or absorbed by 08:00 morning brief). 24h anti-noise lockout in effect until 2026-05-16 06:00 EDT.
- No other CVE in window meeting CVSS ≥9.0 + active-exploitation + A-grade-primary triad.

**Disposition: FAILS on anti-noise.**

### Trigger 2 — New attribution for tracked actor (A/B grade)

- **Mandiant GTIG: TeamPCP → UNC6780 alias mapping** (cloud.google.com/blog/topics/threat-intelligence, 2026-05-11) — Surfaced this sweep via Mandiant index page (feedburner remains 404, 18+ consecutive failures over 9 days). Mandiant explicitly maps tracked actor TeamPCP (#001 HIGH) to UNC6780 alias. UNC6780 is **NOT currently in TeamPCP's `_roster.yaml` aliases** field. **FAILS on out-of-window predicate** — Mandiant publication date 2026-05-11 is 4 days pre-window (sweep window starts 2026-05-15 06:00 EDT). FLASH trigger evaluation is strictly time-windowed; alias-roster updates that are not net-new-this-window are not FLASH-eligible.
- No other in-window attribution surface naming a tracked actor.

**Disposition: FAILS on out-of-window.** **Operator awareness item: run `/update-tracking TeamPCP` before the 16:00 afternoon brief to add UNC6780 to the alias list.** This is a roster hygiene action, not a FLASH-class event — the underlying TeamPCP attribution chain (VT-006 / CVE-2026-45321 / Shai-Hulud release / BreachForums bounty / Mistral data-sale) is already deeply covered in the 06:00 FLASH + 08:00 morning brief; the alias mapping is a metadata enrichment.

### Trigger 3 — First-party IOC hit (archimedes + defenseclaw_local)

- Splunk `archimedes` + `defenseclaw_local` last-6h sweep: zero hits against the tracked-IOC corpus (TeamPCP / Shai-Hulud / Exchange CVE-2026-42897 IOC set from VT-007 candidate / Cisco SD-WAN / PAN-OS / MuddyWater / Ivanti EPMM / FamousSparrow / node-ipc). Archimedes-internal audit-trail sourcetypes present as expected; no security-event sourcetypes; no tracked-IOC matches.
- Per Hard Rule 8: silence is absence of evidence, not evidence of absence. **26th consecutive dormant sweep** with the non-archimedes-internal stream.

**Disposition: FAILS — zero hits.**

### Trigger 4 — Tracked actor TTP change (A/B grade)

- **TeamPCP Shai-Hulud source-code-release TTP** — Already covered in the 06:00 FLASH (`flash-2026-05-15-0600-teampcp-shai-hulud-release`, B2/likely). The source-release-to-public-GitHub + BreachForums monetary-bounty TTP pivot was the substance of that FLASH. In-window restatements (SecurityWeek follow-ups, The Hacker News re-relay, Datadog blog cited but still not directly retrieved this sweep) carry no new TTP layer beyond the 06:00 framing. **FAILS on anti-noise** (24h lockout to 2026-05-16 06:00 EDT).
- No other tracked-actor TTP-change surface in window.

**Disposition: FAILS on anti-noise.**

### Trigger 5 — Active A&D-sector campaign (multi-victim, A&D sector)

- Zero in-window items naming aerospace/defense primes, Tier-1/2 A&D suppliers, ITAR-regulated entities, or US-government-contractor named-victim claims.
- Mandiant GTIG TeamPCP/UNC6780 mapping (out-of-window) does not include net-new A&D-victim naming beyond what's already in the 08:00 morning brief.

**Disposition: FAILS — no A&D-sector named-victim in window.**

### Trigger 6 — Zero-day with no patch

- **Exchange CVE-2026-42897** — Already FLASHed at 06:00 as the primary T6 driver. Still no GA patch (ESU-only path: SE RTM, 2016 CU23, 2019 CU14/CU15); EEMS auto URL-rewrite mitigation unchanged. **FAILS on anti-noise** — 24h lockout to 2026-05-16 06:00 EDT.
- No other zero-day-no-patch surface in window.

**Disposition: FAILS on anti-noise.**

## Hard Rule 8 — First-party Splunk

Clean across `archimedes` and `defenseclaw_local` over -6h. Zero tracked-IOC matches across the corpus IOC set. **26th consecutive dormant sweep** with the non-archimedes-internal stream. Per doctrine: silence is absence of evidence, not evidence of absence.

## Critical-override audit

Critical-override conditions (all 4 required for quiet-hours bypass, moot this sweep since quiet hours are not active):

1. CVSS 10.0 — **NOT MET**. Closest in-window CVE coverage is Exchange CVE-2026-42897 (CVSS 8.1) and Cisco SD-WAN CVE-2026-20182 (CVSS 10.0, but absorbed in 08:00 morning brief; 24h anti-noise lockout).
2. Confirmed active exploitation — partially met for Exchange (MSRC "Exploitation Detected") and Cisco SD-WAN (CISA KEV active exploitation per UAT-8616 Talos attribution).
3. Tracked actor named — TeamPCP/UNC6780 alias surface is out-of-window (2026-05-11).
4. A&D-watchlist entity named as victim — **NOT MET** anywhere in window.

**0 of 4 simultaneous predicates met for any single in-window item. Override does not apply.** (Quiet hours not active regardless, so moot.)

## Anti-noise / 24h-lockouts in effect this sweep

- **Exchange CVE-2026-42897** — FLASHed 06:00; 24h lockout to 2026-05-16 06:00 EDT.
- **TeamPCP Shai-Hulud source release + BreachForums bounty** — FLASHed 06:00; 24h lockout to 2026-05-16 06:00 EDT.
- **TeamPCP Mistral AI 450-repo data sale** — Absorbed in 08:00 morning brief (TeamPCP three convergent supply-chain surfaces 96h framing); 24h lockout to 2026-05-16 08:00 EDT.
- **Cisco SD-WAN CVE-2026-20182** — Absorbed in 08:00 morning brief (sustained-focus pattern, T-2 KEV); 24h lockout to 2026-05-16 08:00 EDT.
- **Copy Fail KEV** — Absorbed in 08:00 morning brief (EOD-today carry-forward); 24h lockout (effective via brief carry-forward) to 2026-05-16 08:00 EDT.

## Source-health observations this sweep

Five sources returned 404 / parse errors as **single observations** this sweep — NOT promoted to `stale` status per source-health policy (single-observation transients vs sustained-failure pattern):

- `talosintelligence.com` (Talos blog) — single 404 this sweep; previous sweep (06:00) was healthy.
- `nitter.net/GossiTheDog` (Kevin Beaumont Nitter mirror) — parse error / instance-rotation typical for nitter mirrors.
- `dragos.com` blog — single fetch error.
- `wiz.io` blog — single parse error.
- `bitdefender.com` blog — single fetch error.
- `security.com` (Symantec/Broadcom) — single parse error.
- `msrc.microsoft.com` blog index — parse error on the index page (the CVE-2026-42897 advisory page itself remains directly accessible — Exchange CVE has been retrievable across multiple sweeps via direct CVE URL).

**Persistent-known-bad (sustained-failure pattern, escalation overdue):**

- **Mandiant feedburner** (feeds.feedburner.com/blogspot/mandiant) — 404 for 18+ consecutive sweeps over 9 days. Operator escalation overdue per source-health notes. Workaround in use: direct fetch of `cloud.google.com/blog/topics/threat-intelligence` index page (succeeded this sweep; surfaced the TeamPCP/UNC6780 alias item via index-page listing rather than feed).

No `source-health.yaml` runtime field changes from this sweep (operator-set `notes` fields preserved per collector subagent convention).

## Awareness items for the 16:00 afternoon brief (NOT FLASH-eligible)

- **Mandiant GTIG TeamPCP → UNC6780 alias mapping** (2026-05-11, out-of-window): operator may want to run `/update-tracking TeamPCP` before the 16:00 brief to add UNC6780 to TeamPCP's `aliases` field in `_roster.yaml`. The underlying TeamPCP attribution chain is already deeply covered; this is roster hygiene.

## Disposition

**Return: 0 candidates — clean sweep.** Pass nothing forward to grader / red-team / briefer. Splunk + git audit trail only. No Discord post per FLASH-POLICY anti-noise rules (silent-exit). All 4 in-window watchlist/actor matches deduplicated against the 06:00 FLASH coverage and the 08:00 morning brief coverage; all 6 FLASH triggers evaluated and did not fire.
