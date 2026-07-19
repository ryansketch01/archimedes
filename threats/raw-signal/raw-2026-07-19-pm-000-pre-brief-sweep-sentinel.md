---
raw_id: raw-2026-07-19-pm-000
collected_at: 2026-07-19T15:32:00-04:00
run_id: pre-brief-20260719-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: multiple
  source_name: "Pre-brief collection coverage sentinel (15:30 EDT, afternoon brief)"
  source_url: null
  published_at: null
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: []
triage_tags: [pre_brief, coverage_record, non_flash, clean_sweep]
iocs_extracted: false
iocs_count: 0
text_word_count: 545
promoted: false
ttl_expires_at: 2026-10-17T15:32:00-04:00
---

# Pre-brief collection coverage record — 2026-07-19 15:30 EDT (afternoon brief)

CLEAN sweep. 0 substantive raw-signal items written. No watchlist / roster /
vuln-index matches in the window. This sentinel is the coverage record for the
2026-07-19 afternoon brief pre-brief collection.

Window: ~2026-07-19T07:30 → 15:30 EDT (8h primary). The 06:00 → 12:00 slice was
already swept clean by the 2026-07-19 12:00 FLASH sweep
(raw-2026-07-19-flash-1200-000 — 0 candidates, 0 triggers). Net-new uncovered
slice this pre-brief was ~12:00 → 15:30 EDT plus a broader re-sweep of all
healthy surfaces. Sunday afternoon — low news cadence expected and fully
observed (fourth consecutive clean coverage record of 2026-07-19 after AM
pre-brief + 00:00/06:00/12:00 FLASH sweeps).

## Sources swept (healthy)

RSS/media via rss-bridge fetch_feed (all HTTP 200):
- bleepingcomputer — 1 item in window (15 in feed; last_modified
  2026-07-19T19:29 GMT). Item is the same "Hackers abuse ViPNet software to
  target Russian govt agencies" (Bill Toulas, 2026-07-19T14:23 UTC = 10:23 EDT)
  already assessed and discarded in the 12:00 FLASH sweep — anti-noise applies,
  not re-signaled. See disposition note below.
- securityweek — 0 items in window (10 in feed; last_modified 2026-07-18T09:45
  GMT — no new SecurityWeek content since Saturday morning).
- the-record — 0 items in window (5 in feed).

Authoritative CVE surface:
- cisa-kev (JSON, direct WebFetch) — catalog version 2026.07.16 (released
  2026-07-16T17:00Z), 1,647 total. UNCHANGED from the AM pre-brief + 00:00 /
  06:00 / 12:00 FLASH sweeps. NO entries dated 2026-07-17, 2026-07-18, or
  2026-07-19. No new KEV additions this window. A passing KEV deadline is not a
  brief-signal trigger.

First-party (Splunk, Frank; reachable, v10.2.2, license OK):
- Trigger-3 / first-party-IOC sweep (index=archimedes OR index=defenseclaw_local,
  -8h): in-window events are exclusively Archimedes' own operational/scheduler
  telemetry (archimedes:operation 3, archimedes:scheduler 6 = 9 self-audit
  events). defenseclaw_local returned ZERO events in-window. No tracked-IOC hits.
  Visibility-bounded null, no bonus.

Not queried this pre-brief (stale, carry prior state; entrenched failure
patterns pending operator action, consistent with the 2026-07-19 AM pre-brief
and recent sweeps): mandiant (stale since 2026-06-13, feedburner RSS 404 —
direct-HTML path is the working workaround, canonical-swap decision still
pending), msrc (stale since 2026-05-30, feed parse error — content still reaches
corpus via relays), ars-security (stale since 2026-05-09, security-only path
retired — root feed workaround in use). No stale-source retry attempted this
sweep.

### In-window item assessed and discarded (anti-noise) — ViPNet / "HelloNet"

Carried forward from the 12:00 FLASH disposition. BleepingComputer (Bill Toulas):
campaign "HelloNet" abusing the ViPNet private-networking update mechanism,
active since ~May 2026. DISCARDED — no watchlist/roster/vuln-index hit and no
FLASH trigger: targeting is Russian organizations (govt/energy/transport/
education/logistics — inverse of the US A&D-prime profile); attribution is an
UNIDENTIFIED Chinese-speaking APT held at LOW confidence (possible false-flag
noted), NOT a _roster.yaml actor; no CVE / no CVSS; not an A&D-sector campaign.
Named IOCs out-of-scope, not extracted. Logged for trail completeness only.

## Standing watch items — no state change this window

- SharePoint CVE-2026-58644 (VT-041, KEV due today 07-19;
  knownRansomwareCampaignUse Unknown): deadline passing quietly, no net-new
  escalation. Quiet.
- Oracle EBS CVE-2026-46817 (VT-043, KEV due 07-18, now past-due; Unknown): no
  new attribution, no named A&D/DIB victim, no A-grade direct exploitation
  confirmation net-new, no ransomware-campaign-use flip. Quiet.
- FortiSandbox CVE-2026-25089 / CVE-2026-39808 (VT-045/046, KEV due today 07-19;
  Unknown): no net-new escalation. Quiet.
- WordPress Core CVE-2026-63030 (wp2shell, VW-001): no new escalation this window
  — no in-window RSS item mentions it (bleepingcomputer/securityweek/the-record
  clean), no mass-exploitation telemetry beyond the ITW-onset already covered in
  the 2026-07-18 briefs. Quiet.

## FLASH / match evaluation

No item in-window matched any watchlist (aerospace-defense), _roster.yaml actor
alias, or _index.yaml tracked vulnerability. Nothing rose to a raw-signal-worthy
finding candidate. Grader has a clean queue for the 2026-07-19 afternoon brief;
standing sections (A&D Sector Focus, Iran Cyber Watch) carry silent-day templates.

## Source health

All queried sources returned HTTP 200 and remain `healthy`; no status flips, no
new failures, no recoveries. mandiant/msrc/ars-security carry prior stale state
(not retried this sweep). No runtime-field changes warranted; no edit to
source-health.yaml this sweep.
