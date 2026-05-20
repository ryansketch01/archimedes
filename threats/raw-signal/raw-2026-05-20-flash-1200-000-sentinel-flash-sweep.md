---
raw_id: raw-2026-05-20-flash-1200-000
collected_at: 2026-05-20T12:05:00-04:00
run_id: flash-sweep-20260520-120000
collection_mode: flash_sweep
test: false
source:
  source_yaml_id: sentinel
  source_name: "Collector FLASH sweep sentinel"
  source_url: null
  published_at: 2026-05-20T12:00:00-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: []
triage_tags:
  - flash_sweep_2026_05_20_1200_sentinel
  - zero_triggers_fired
  - active_hours_post_capable
  - splunk_first_party_zero_hits_49th_consecutive_dormant_sweep
  - anti_noise_absorbed_teampcp_github_corp_breach_continuation_grafana_tanstack
  - anti_noise_absorbed_mini_shai_hulud_antv_continuation
  - anti_noise_absorbed_yellowkey_mitigation
  - anti_noise_absorbed_storm_2949_sspr
iocs_extracted: false
iocs_count: 0
text_word_count: null
promoted: false
ttl_expires_at: 2026-08-18T12:05:00-04:00
---

# FLASH sweep 2026-05-20 12:00 EDT — zero triggers fired

This sentinel raw-signal records the 12:00 EDT FLASH sweep on 2026-05-20.
Window: items published since 2026-05-20T06:00:00-04:00 (6 hours).
Active-hours posture: inside 09:00-21:00 EDT — any fired FLASH would have
posted live to #flash-alerts, not queued. Authorized-targets.yaml empty —
passive-only across the board.

## Sources swept (FLASH-narrow)

- BleepingComputer RSS (4 in-window items)
- SecurityWeek RSS (9 in-window items, 5 substantive after promo filter)
- The Hacker News RSS (5 in-window items, 3 substantive after promo filter)
- The Record RSS (3 in-window items, 2 substantive after non-cyber filter)
- CISA all.xml RSS (0 in-window items)
- CISA KEV catalog (full-catalog scan for dateAdded>=2026-05-19 — 0 entries)
- Splunk archimedes + defenseclaw_local (-24h tracked-IOC superset)

## Six-trigger matrix outcome

Zero of six FLASH triggers fired on any in-window item after applying
anti-noise rule 1 (one FLASH per trigger topic per 24h).

### Trigger 1 — critical-cve-exploited
- CISA KEV: zero entries dated 2026-05-19 or 2026-05-20. Most recent
  addition remains CVE-2026-42897 Exchange Server XSS (dateAdded
  2026-05-15, dueDate 2026-05-29).
- No new CVE in the 6h sweep window meets CVSS >= 9.0 with confirmed
  active exploitation per A-grade source.

### Trigger 2 — tracked-actor-attribution (new)
- Fox Tempest (THN — Microsoft takedown of malware-signing service):
  NOT in _roster.yaml; Hard Rule 2 prevents Archimedes-side cross-walk
  to TeamPCP / Vanilla Tempest / other Microsoft "Storm" or "Tempest"
  designations. Microsoft article attributes activity to Fox Tempest +
  Vanilla Tempest distribution channel; neither alias maps to any of
  the 24 tracked actors in _roster.yaml. Discarded.
- Webworm (THN — ESET via Symantec lineage): NOT in _roster.yaml.
  Aliases extracted from article — FishMonger, Aquatic Panda,
  SixLittleMonkeys, Space Pirates, APT17 — none match _roster.yaml
  primary names or alias lists. Hard Rule 2 prevents alias origination.
  Discarded as FLASH candidate; surfaced to morning-brief grader as
  raw-2026-05-20-flash-1200-001 for A&D Sector Focus standing-section
  consideration only.
- Storm-2949 (BleepingComputer am-002 carry-forward, no new in-window
  surface this sweep): "Storm-####" is a Microsoft temporary
  designation, NOT in _roster.yaml. Already absorbed into AM
  pre-brief raw-signal stream. No new attribution in 12:00 window.

### Trigger 3 — first-party IOC hit
- Splunk archimedes + defenseclaw_local query against the standard
  tracked-IOC superset (TeamPCP / Mini Shai-Hulud C2 set + GlassWorm
  carry-forward + UNC1549 + Charming Kitten + MuddyWater + APT28
  spray IPs + Beagle / CL-STA-1132 unattributed clusters) over -24h
  window returned zero events.
- 49th consecutive dormant non-self-telemetry sweep (incrementing from
  47th cited in 06:08 queued FLASH and 48th cited in am-002
  finding-2026-05-20-0002). Hard Rule 8 framing: silence is not
  disconfirming, not confirming.

### Trigger 4 — tracked-actor TTP change
- TeamPCP (#001 HIGH): Grafana/TanStack token-rotation-miss
  continuation (BleepingComputer Bill Toulas 11:46 EDT) is a
  downstream branch of the VT-006 / Mini Shai-Hulud campaign cluster.
  Per FLASH-POLICY anti-noise rule 1 and the explicit
  anti_noise_lock=teampcp-github-internal-repos-breach-via-vscode-
  extension-2026-05-20 carried by the 06:08 queued FLASH (valid to
  2026-05-21T06:08:00-04:00), the Grafana continuation absorbs into
  the existing lock. Source-of-disclosure is Grafana official update
  blog. No new actor TTP layer beyond continued token-rotation hygiene
  failure; not a tradecraft pivot. Discarded as FLASH candidate;
  raw-2026-05-20-flash-1200-002 surfaces it for grader morning-brief
  UPDATE block on VT-006 lineage.
- Webworm: actor not in _roster.yaml; T4 fails on attributability.
- No other tracked-actor surface in 6h window.

### Trigger 5 — A&D-sector campaign (active, multi-victim, watchlist named)
- Webworm (THN — China-aligned actor, EchoCreep + GraphWorm backdoors):
  article names "aerospace" as a target sector and 9 countries
  (Russia, Georgia, Mongolia, Belgium, Italy, Serbia, Poland, Spain,
  South Africa). Multi-victim YES, active YES, sector includes
  aerospace YES. However, FLASH-POLICY Trigger 5 condition reads
  "targets_include_aerospace_defense_or_watchlist_entity" — strict
  read requires a watchlist company OR explicit A&D-prime victim
  naming. Article names no specific A&D-watchlist prime (Lockheed
  Martin, Boeing, RTX, Northrop Grumman, General Dynamics, BAE,
  L3Harris, Leidos, SAIC, Thales, GE Aerospace, Safran, Honeywell
  Aerospace, Airbus, Elbit). Per Hard Rule 2 Archimedes does not
  upgrade sector-shape to entity-specific framing. T5 FAILS on
  watchlist-specificity clause. Surfaced as
  raw-2026-05-20-flash-1200-001 for morning brief A&D Sector Focus
  consideration, NOT as FLASH candidate.
- Senator Hassan / CISA / Nightwing (The Record): Nightwing's RTX
  spin-off corporate lineage is public OSINT but NOT vendor-attested
  in this Record relay (article calls it only "government contractor
  Nightwing"). Mechanism = AWS credential exposure on public GitHub
  repo per Brian Krebs original (CISA acknowledged). Incident is a
  passive credential exposure investigated by CISA, not an active
  multi-victim campaign. T5 condition article_describes_active_campaign
  FAILS. Surfaced as raw-2026-05-20-flash-1200-003 for grader review
  of A&D-watchlist-adjacency framing — Archimedes does NOT originate
  the RTX-lineage attribution per Hard Rule 2; the grader may cite
  public OSINT separately or wait for the Krebs primary.
- TeamPCP / Mini Shai-Hulud lineage: anti-noise lock active to
  2026-05-21T06:08:00-04:00.

### Trigger 6 — zero-day no patch
- Anthropic Claude Code sandbox bypass (CVE-2025-66479 + uncatalogued
  SOCKS5 null-byte injection): Anthropic silently patched in commit
  March 27 / shipped in Claude Code 2.1.88 on March 31; no CVSS
  disclosed by vendor; PoC-only by researcher Guan via HackerOne;
  marked as duplicate by Anthropic. NOT a zero-day at disclosure
  (already patched 50+ days prior). T6 FAILS.
- PinTheft Arch Linux LPE (CVE TBA): kernel patch released ~2026-05-05;
  PoC released today by V12 research team; PoC-only, no in-the-wild
  exploitation. Already patched. T6 FAILS — vulnerability is not
  disclosed before a patch is available.
- Drupal core security release (CVE TBA): patches shipping today
  17:00-21:00 UTC; advisory warns of high exploitation risk
  post-disclosure; no current active exploitation; not yet zero-day
  status. T6 condition exploitation_confirmed_or_imminent_per_A-grade
  FAILS at this sweep (would need re-evaluation if Drupal advisory
  confirms exploitation post-patch-release).

## Items evaluated, anti-noise absorbed

| Item | Lock |
|---|---|
| BleepingComputer / Bill Toulas — Grafana breach via TanStack token rotation miss (11:46 EDT) | teampcp-github-internal-repos-breach-via-vscode-extension-2026-05-20 (06:08 queued FLASH) — same TeamPCP / Mini Shai-Hulud campaign cluster, downstream Grafana victim continuation |
| SecurityWeek / Ionut Arghire — Over 320 NPM @antv Mini Shai-Hulud (11:06 EDT) | Same VT-006 anti-noise lock + already in AM pre-brief as raw-2026-05-20-am-001 / finding-2026-05-20-0001 |
| THN — GitHub Breached / TeamPCP 3,800+ repos (11:38 EDT) | 06:08 queued FLASH directly — anti_noise_lock_expires 2026-05-21T06:08 |
| The Record — GitHub confirms TeamPCP hack (12:21 EDT, edge-of-window) | 06:08 queued FLASH same |
| SecurityWeek — Microsoft mitigations for YellowKey BitLocker bypass (11:39 EDT) | Already in AM pre-brief as raw-2026-05-20-am-003 / finding-2026-05-20-0003 |

## Items evaluated, discarded (no trigger, no anti-noise lock — recorded only)

| Item | Failing predicates |
|---|---|
| THN — Microsoft takes down Fox Tempest malware-signing service (10:36 EDT) | T1 FAIL (no CVE); T2 FAIL (Fox Tempest + Vanilla Tempest NOT in _roster.yaml, Hard Rule 2); T3 FAIL (Splunk dormant); T4 FAIL (actor not tracked); T5 FAIL (no A&D sector — healthcare/edu/gov/finance); T6 FAIL (no vuln) |
| THN — Webworm EchoCreep + GraphWorm Discord + MS Graph API backdoors (08:51 EDT) | T1 FAIL (no CVE); T2 FAIL (Webworm + aliases FishMonger / Aquatic Panda / SixLittleMonkeys / Space Pirates / APT17 NOT in _roster.yaml, Hard Rule 2); T3 FAIL (Splunk dormant); T4 FAIL (actor not tracked); **T5 BORDERLINE-FAIL** (aerospace sector named but no A&D-watchlist prime named; strict-read of trigger condition fails); T6 FAIL (no vuln). Surfaced as raw-2026-05-20-flash-1200-001 for morning-brief A&D Sector Focus consideration, NOT as FLASH candidate. |
| The Record — Senator Hassan presses CISA on Nightwing GitHub repo leak (08:11 EDT) | T1 FAIL (no CVE); T2 FAIL (no actor); T3 FAIL (Splunk dormant); T4 FAIL (no actor); T5 FAIL (passive credential exposure, not active campaign; no actor; Nightwing's RTX-spin-off lineage not vendor-attested in this relay — Hard Rule 2 prevents Archimedes origination); T6 FAIL (no vuln). Surfaced as raw-2026-05-20-flash-1200-003 for grader review. |
| SW — Anthropic silently patches Claude Code sandbox bypass (09:00 EDT) | T1 FAIL (no active exploitation; PoC-only; patched 2026-03-31 50+ days ago); T2 FAIL (no actor); T6 FAIL (already patched, not zero-day at disclosure); all others FAIL |
| BleepingComputer — Drupal critical update high exploitation risk (08:52 EDT) | T1 FAIL (no active exploitation, patch shipping today); T6 FAIL (patches scheduled today, not zero-day); CVE TBA; all others FAIL |
| BleepingComputer — PinTheft Arch Linux LPE PoC released (06:52 EDT) | T1 FAIL (no CVE, PoC-only no in-the-wild); T6 FAIL (kernel patch already shipped ~2026-05-05); narrow Arch-Linux scope (RDS + io_uring + x86_64); no A&D; all others FAIL |
| SW — AI-Powered App Attacks (Digital.ai analyst report, 10:37 EDT) | Not incident-class; sector-wide framing not A&D-targeted; T1-T6 all FAIL |

## Hard Rules compliance

- **Rule 2 (no first-time attribution):** Compliance verified verbatim. Webworm China-alignment + aliases preserved as ESET / Symantec-attested only; Fox Tempest + Vanilla Tempest not cross-walked to roster; Nightwing's RTX-spin-off lineage NOT propagated through this sweep (not vendor-attested in the Record relay); Storm-2949 carry-forward retains Microsoft temporary-designation framing; Grafana / TanStack continuation keeps Grafana official disclosure attribution; TeamPCP attribution on the 06:08 queued FLASH preserved as self-claim relayed by three B-grade media, NOT Archimedes-originated.
- **Rule 3 (no PoC content):** Compliance verified. PinTheft PoC content NOT extracted (article reference only); Anthropic Claude Code sandbox bypass technical primitive NOT extracted; Drupal upcoming patch contents NOT speculated. CVE numbers + product names + patch boundaries only.
- **Rule 4 (no active scans, authorized-targets.yaml empty):** Compliance verified. Only passive RSS / WebFetch on public news pages + CISA KEV JSON. No Shodan / Censys / VT lookups invoked this sweep beyond what was already cached in the AM run. No SpiderFoot / theHarvester / nmap. All targets passive-read-only.
- **Rule 6 (no quotes beyond 15 words):** Compliance verified. Extraction summaries include attribution-language strings under the limit (Webworm "China-aligned threat actor" 4 words; Microsoft "seized signspace[.]cloud" verb-clause); no >15-word verbatim quotes.
- **Rule 8 (Splunk first-party priority):** First-party sweep result is dormant continuation — 49th consecutive sweep with zero hits across the standard tracked-IOC superset (-24h). No conflict between Splunk telemetry and any external claim in this sweep (zero hits = absence of contradicting signal, not affirmation of external claim). Hard Rule 8 framing preserved: silence is not disconfirming, not confirming.

## Carry-forward observations from morning-brief findings (do NOT re-grade)

These are observations only; grader / briefer own all promotion decisions
on these surfaces. The 2026-05-20-morning brief file does NOT exist on
disk at sweep time — orchestrator anomaly flagged separately for
librarian (08:00 morning brief was not posted; 09:00 catchup sweep on
06:08 queued FLASH did not run). Findings-0001/-0002/-0003 remain
unposted-but-on-disk.

- finding-2026-05-20-0001 (Mini Shai-Hulud @antv continuation, B2 / likely):
  TeamPCP attribution layer continues to track. SecurityWeek 11:06 EDT
  in-window surface reaffirms; no new attribution-layer evidence; no
  new ecosystem (still npm + PyPI, no third-ecosystem expansion);
  Composer mention in keywords likely refers to the brief's coverage
  of Snyk's potential Composer reach analysis, not actual Composer
  packages compromised this sweep.
- finding-2026-05-20-0002 (Storm-2949 MSTIC SSPR / Azure cluster, B2 /
  likely): no new in-window MSTIC publication; no roster-actor
  reclassification; A&D-relevance remains structural-indirect via
  Microsoft 365 / Azure ubiquity in Tier-1 A&D environments. No new
  signal in 12:00 window beyond AM pre-brief baseline.
- finding-2026-05-20-0003 (YellowKey CVE-2026-45585 BitLocker bypass
  Microsoft mitigation, B2 / likely on PoC layer): SecurityWeek
  11:39 EDT Ionut Arghire surface is a B-grade relay of the same
  Microsoft mitigation publication already covered in AM pre-brief.
  No KEV addition observed (CISA KEV catalog has CVE-2026-42897
  Exchange as most recent at 2026-05-15). No new exploitation claim
  beyond the existing PoC-public-no-ITW posture.

## Orchestrator anomaly note (informational — librarian owns disposition)

The 06:08 FLASH for TeamPCP / GitHub-corp breach queued per
flash-queue.yaml shows `superseded: false` at this 12:00 sweep. The
2026-05-20-morning brief file does NOT exist on disk. The 09:00 catchup
sweep that should have processed the queue did not run, or ran without
posting / marking the queue entry. Three findings (-0001 / -0002 /
-0003) exist on disk as new files (per git status `??`). This appears
to be an orchestrator-side scheduler anomaly affecting the morning
phases, NOT a collector-side issue. Per collector doctrine, the
collector does not act on this — flagging for librarian + operator
visibility only.

## Source-health deltas

- bleepingcomputer: last_successful_fetch refresh 2026-05-20T12:02:38 (4
  in-window items). Status healthy; failure_count 0; runtime-fields-only
  update. Operator notes preserved verbatim.
- securityweek: last_successful_fetch refresh 2026-05-20T12:02:40 (9
  in-window items). Status healthy; failure_count 0; runtime-fields-only
  update. Operator notes preserved verbatim.
- thehackernews: last_successful_fetch refresh 2026-05-20T12:02:41 (5
  in-window items). Status healthy; failure_count 0; runtime-fields-only
  update. Operator notes preserved verbatim.
- the-record: last_successful_fetch refresh 2026-05-20T12:02:44 (3
  in-window items). Status healthy; failure_count 0; runtime-fields-only
  update. Operator notes preserved verbatim.
- cisa-advisories: last_successful_fetch refresh 2026-05-20T12:02:48 (0
  in-window items via all.xml — pattern continues). Status healthy;
  failure_count 0; runtime-fields-only update. Operator notes preserved
  verbatim.
- cisa-kev: catalog full-scan via WebFetch 2026-05-20T12:00 EDT — 0
  entries dated 2026-05-19 or 2026-05-20. Status healthy. Runtime fields
  only; operator notes preserved verbatim.
- splunk-archimedes + splunk-defenseclaw: -24h tracked-IOC superset query
  returned 0 events. 49th consecutive dormant sweep. Status healthy;
  query latency normal.

## TLP marking

TLP:CLEAR — all source content sourced from public news / CISA / vendor
publications; no first-party Splunk content reproduced (zero hits to
reproduce); no PII; no credentials.
