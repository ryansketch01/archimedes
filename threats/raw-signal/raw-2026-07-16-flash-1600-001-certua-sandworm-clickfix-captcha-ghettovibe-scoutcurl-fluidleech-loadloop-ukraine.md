---
raw_id: raw-2026-07-16-flash-1600-001
collected_at: 2026-07-16T16:05:00-04:00
run_id: flash-2026-07-16-1600
collection_mode: flash_sweep
sweep_window_start: 2026-07-16T06:00:00-04:00
sweep_window_end: 2026-07-16T16:00:00-04:00
source:
  source_yaml_id: the-record
  source_name: "The Record from Recorded Future News (relay of CERT-UA advisory)"
  source_url: https://therecord.media/ukraine-sandworm-hacks-captcha-powershell
  published_at: 2026-07-16T13:50:00+00:00
  originating_source: "CERT-UA (Ukraine national CERT) — advisory published 2026-07-16"
match_reason:
  watchlist: []
  actors: [Sandworm]
  vulnerabilities: []
  keywords: [ClickFix, CAPTCHA, PowerShell, GRU, CERT-UA]
triage_tags: [flash_candidate, tracked-actor-ttp-change, sandworm, russia-gru, marginal_trigger4]
iocs_extracted: true
iocs_count: 0
promoted: true
promoted_to_finding: finding-2026-07-16-0003
promoted_at: 2026-07-16T16:22:00-04:00
flash_posted: false
flash_disposition: held_routed_to_next_scheduled_brief_russia_watch
ttl_expires_at: 2026-10-14T16:05:00-04:00
---

# CERT-UA: Sandworm shifts to ClickFix (fake-CAPTCHA -> PowerShell paste) delivering new malware set vs Ukrainian targets

Async FLASH sweep hit, window 2026-07-16T06:00 -> 16:00 EDT. Roster-actor match on
**Sandworm (_roster.yaml #007; APT44 / Seashell Blizzard, RU GRU Unit 74455)**.

## What the source says (attribution language preserved verbatim — Hard Rule 2)

Per **CERT-UA** (originating; relayed by **The Record**, Recorded Future News), Sandworm —
described by the source as "**Kremlin-backed**" and linked to "**Russia's military intelligence
agency, the GRU**," active "since at least 2013" — has shifted this spring/summer to a
**ClickFix** social-engineering delivery: victims meet a fake CAPTCHA on a compromised site and
are instructed to copy/paste a PowerShell command into Windows, which deploys malware for
persistent access.

Named malware set (CERT-UA codenames):
- **GhettoVibe** — initial malware
- **ScoutCurl** — reconnaissance (system details, software inventory, browser data)
- **FluidLeech** — loader disguised as antivirus-removal software
- **LoadLoop** — malware loader

CERT-UA frames this as "a shift this spring and summer" toward ClickFix — an **evolved delivery
tactic**, not entirely new tooling (source's own characterization).

## FLASH trigger evaluation

- **Trigger 4 (tracked-actor TTP change) — MET (marginal).** New named tooling
  (GhettoVibe/ScoutCurl/FluidLeech/LoadLoop) + documented delivery-method shift to ClickFix,
  attributed to a roster-tracked actor (Sandworm #007) by an A-grade national CERT (CERT-UA;
  B-grade relay via The Record). Genuinely NEW to the Archimedes corpus (distinct from the
  2026-07-13 EU/UK Sandworm-DynoWiper sanctions topic and the FSB Center16 advisory).
- Triggers 1/2/3/5/6 — NOT met.

## Mitigating factors for the grader / red-team (do NOT pre-empt — recorded for downstream)

- **No A&D / DIB / government / critical-infrastructure target named.** Targeting is
  "primarily Ukrainian." A&D nexus is absent, not merely indirect.
- **ClickFix is a commodity technique** widely used across many actors; the reported change is
  Sandworm *adopting* a common delivery method in its baseline Ukraine theater, not a novel
  capability class.
- Attribution to Sandworm is **not new** (long-standing GRU attribution) — the NEW element is
  the tooling/delivery, which is why this reads as Trigger 4 (TTP change), not Trigger 2 (new
  attribution).
- **No atomic IOCs** in the retrieved relay (CERT-UA advisory primary not directly retrieved
  this sweep — domains/hashes/PowerShell command detail not in The Record piece).
- Likely disposition: a **Russia-watch / next-scheduled-brief** item rather than a posted FLASH,
  pending grader weighting of the Ukraine-focus + commodity-base factors. Surfaced as a candidate
  per collector discipline (surface, don't suppress); grader/red-team make the post/hold call.

## Extraction notes

- Language: en. Article type: news relay of a national-CERT advisory.
- Byline: The Record (Recorded Future News); originating author CERT-UA.
- Raw IOC extraction invoked: yes.

## IOCs (from ioc-extraction skill)

```yaml
atomic_iocs: []            # none present in the retrieved relay
tooling_references:        # malware family NAMES only (not atomic indicators)
  - name: GhettoVibe
    role: initial_malware
  - name: ScoutCurl
    role: reconnaissance
  - name: FluidLeech
    role: loader_disguised_as_av_removal
  - name: LoadLoop
    role: loader
techniques:
  - "ClickFix (fake-CAPTCHA social engineering -> user-pasted PowerShell)"
attribution_claims:
  - actor: Sandworm
    aliases_in_source: []
    nation: RU
    service: GRU
    source: CERT-UA (relayed by The Record)
    language: "Kremlin-backed / linked to Russia's military intelligence agency, the GRU"
    novelty: "attribution not new; tooling + ClickFix delivery shift is the new element"
notes:
  - "Hard Rule 2: attribution recorded as stated by CERT-UA; not originated/upgraded."
  - "Hard Rule 3: no PoC / no exploit / no PowerShell command body copied."
  - "No credentials observed."
  - "CERT-UA advisory primary pending_direct_retrieval for atomic IOCs (domains/hashes)."
```
