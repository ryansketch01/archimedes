---
raw_id: raw-2026-05-08-1200-sweep
collected_at: 2026-05-08T12:01:30-04:00
run_id: flash-sweep-20260508-120000
collection_mode: flash_sweep
sweep_outcome: clean
triggers_fired: 0
candidates: 0
window_start: 2026-05-08T08:00:00-04:00
window_end: 2026-05-08T12:00:00-04:00
window_hours: 4
ttl_expires_at: 2026-08-06T12:01:30-04:00
---

# 2026-05-08 12:00 EDT FLASH sweep — clean

**0 triggers fired. 0 candidates queued. Window: 08:00 → 12:00 EDT (4 hours since morning brief).**

## Sources checked

A-grade primary research and government feeds (in-window):

- CISA KEV catalog (JSON feed) — most recent entry CVE-2026-6973 Ivanti EPMM, dateAdded 2026-05-07 (already covered in 2026-05-08 morning brief). No new KEV additions since 08:00.
- CISA Advisories RSS — 0 items in 4h window
- NVD — no in-window critical-CVE-with-exploitation surfaced via downstream relay
- Mandiant (cloud.google.com/blog/topics/threat-intelligence) — feed reachable, 0 items in 4h window
- Microsoft MSTIC / Security Blog RSS — 0 items in 4h window
- Palo Alto Unit 42 RSS — 0 items in 4h window (last activity 2026-05-07T21:26 UTC)
- CrowdStrike blog RSS — 10 items returned but all undated / marketing-tier (Gartner MQ, Falcon launches, ROI studies); one item "Defending Against CORDIAL SPIDER and SNARKY SPIDER" — neither alias in `_roster.yaml`
- Rapid7 blog RSS — 1 in-window item ("Zero Chaos: Scaling Detection Engineering" — detection engineering thought leadership, no threat content)
- SecurityWeek RSS — 1 in-window item ("In Other News" digest, see below)
- The Record RSS — 2 in-window items (Canvas/universities; BO Team & Head Mare hacktivist coordination)
- BleepingComputer RSS — 3 in-window items (SOC alert sponsored content; Trellix RansomHouse claim; Ivanti EPMM CISA-deadline restatement)
- SANS ISC RSS — 1 in-window item ("Dirty Frag" Linux LPE diary — see below)
- Splunk first-party (`archimedes` + `defenseclaw_local`, last 24h) — 3 sourcetypes returned, all Archimedes operational telemetry (`archimedes:brief`, `archimedes:operation`, `archimedes:scheduler`); 0 security-event sourcetypes; 0 tracked-IOC hits

## Trigger evaluation

### Trigger 1 — Critical CVE with active exploitation (CVSS≥9.0, A-grade)

- **CISA KEV catalog**: most recent entry is Ivanti EPMM CVE-2026-6973 (2026-05-07), already published in 08:00 morning brief — anti-noise rule 1 (one FLASH per topic per 24h) holds. PAN-OS CVE-2026-0300 (2026-05-06) similarly already-tracked.
- No new CVSS≥9.0 + active-exploitation entry since 08:00.
- **Not fired.**

### Trigger 2 — New attribution for tracked actor

- BO Team / Head Mare (Kaspersky via The Record) — neither in `_roster.yaml`; pro-Ukraine hacktivist groups, not aligned with the 23 tracked actors.
- ScarCruft / ArcaneDoor / "darkworm" (PamDOORa) named in SecurityWeek "In Other News" — none in `_roster.yaml`. ScarCruft is a known DPRK actor but not currently tracked; would require a `/new-actor` workflow if escalated.
- CORDIAL SPIDER / SNARKY SPIDER (CrowdStrike marketing post) — not in `_roster.yaml`.
- RansomHouse (Trellix breach claim, BleepingComputer) — not in `_roster.yaml`.
- **Not fired.**

### Trigger 3 — First-party IOC hit (Splunk, last 24h)

- `archimedes` + `defenseclaw_local` queried for last 24h. Returned only Archimedes' own operational sourcetypes (`archimedes:brief`, `archimedes:operation`, `archimedes:scheduler`). Zero security-event telemetry; zero tracked-IOC matches. Consistent with prior 24h state (per `source-health.yaml` note: `defenseclaw_local` not currently receiving live security stream).
- **Not fired.**

### Trigger 4 — Tracked actor TTP change (A/B-grade)

- No in-window content from A/B-grade source documenting new tooling, targeting, or infrastructure for any of the 23 tracked actors.
- **Not fired.**

### Trigger 5 — Active nation-state campaign vs A&D sector

- SecurityWeek "Operation Silent Rotor" mention (drone industry, Eurasian, Russian Aeronautical Information Center spear-phishing): adjacent sector but **no A&D watchlist company named**, **no attribution to tracked actor**, and surfaced as one-line digest item rather than primary multi-victim campaign reporting from A-grade primary. Below FLASH threshold; better suited for non-FLASH raw-signal pickup at next pre-brief if Mandiant/Unit42/Talos publish a primary writeup.
- No watchlist company (Lockheed, Boeing, RTX/Raytheon/Collins/P&W, Northrop, GD, BAE, L3Harris, Leidos, SAIC, Thales, GE Aerospace, Safran, Honeywell Aerospace, Airbus, Elbit) referenced in any in-window item.
- **Not fired.**

### Trigger 6 — Zero-day without patch (CVSS≥8.0 or wide-deployed, exploitation confirmed/imminent)

- "Dirty Frag" Linux LPE (SANS ISC, 2026-05-08T14:57Z): no CVE assigned in surfaced summary, characterized as research-disclosure (Hyunwoo Kim discovery), no active-exploitation claim. Local privilege escalation in Linux kernel — wide-deployed product class, but no exploitation-confirmed-or-imminent A-grade claim. SANS ISC is B-grade. Below FLASH threshold; vuln-tracker may pick up for `_index.yaml` candidacy if patch lag emerges.
- PamDOORa (SecurityWeek) — Linux PAM backdoor sold on cybercrime forum; not a vulnerability disclosure, not a zero-day with-patch-pending issue.
- **Not fired.**

## Anti-noise observations

- Ivanti EPMM CVE-2026-6973 surfaced again (BleepingComputer relay of CISA 4-day patch deadline). Already covered in 2026-05-08 morning brief. Standard anti-noise behavior: subsequent surface absorbs into next scheduled brief as UPDATE if material change emerges, not a fresh FLASH.

## Source-health observations (no changes proposed)

All sources queried this sweep returned status consistent with current `source-health.yaml`. No status transitions warranted:

- `cisa-kev`: healthy (KEV JSON returned cleanly)
- `mandiant`: still healthy with prior `failure_count: 1`; this sweep used cloud.google.com/blog endpoint indirectly (no fresh items), no new failure event
- `unit42`, `mstic`, `crowdstrike`, `securityweek`, `bleepingcomputer`, `the-record`, `rapid7`, `sans-isc`: healthy, all responded with valid feeds
- `splunk-archimedes`, `splunk-defenseclaw`: healthy (search returned events from archimedes index)

`source-health.yaml` not modified by this sweep.

## Notes

- 4h window is short by design for the 12:00 sweep (08:00 morning brief was the prior anchor). Lower-volume sweep is expected.
- Mandiant feedburner endpoint warning from 07:30 sweep persists — not retried this run because alternate endpoint not yet identified; defer to next pre-brief.
- The drone-industry / Operation Silent Rotor item (SecurityWeek) is the closest-to-relevant signal and warrants pre-brief pickup at 15:30 if a Mandiant / Unit42 / Talos primary surfaces.

---

*Sweep mode: flash_sweep. Outcome: clean. No raw-signal-flash files written. No queue entries. No source-health changes.*
