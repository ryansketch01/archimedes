---
raw_id: raw-2026-05-20-flash-1800-000
collected_at: 2026-05-20T18:05:00-04:00
run_id: flash-sweep-20260520-180000-ad-hoc
collection_mode: flash_sweep
test: false
source:
  source_yaml_id: sentinel
  source_name: "Collector FLASH sweep sentinel (ad-hoc, operator-invoked)"
  source_url: null
  published_at: 2026-05-20T18:05:00-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: []
triage_tags:
  - flash_sweep_2026_05_20_1800_ad_hoc_sentinel
  - operator_invoked_ad_hoc_ahead_of_scheduled_1800
  - zero_triggers_fired
  - active_hours_post_capable
  - splunk_first_party_zero_hits_50th_consecutive_dormant_sweep
  - anti_noise_absorbed_mstic_antv_a_grade_corroboration_lock_teampcp_mini_shai_hulud
  - anti_noise_absorbed_unit42_npm_landscape_update_lock_teampcp_mini_shai_hulud
  - trigger_1_evaluated_failed_sonicwall_cve_2024_12802_reliaquest_itw_no_a_grade_attestation_of_exploitation
  - trigger_6_evaluated_failed_drupal_cve_2026_9082_patch_available_cvss_6_5
iocs_extracted: false
iocs_count: 0
text_word_count: null
promoted: false
ttl_expires_at: 2026-08-18T18:05:00-04:00
---

# FLASH sweep 2026-05-20 18:00 EDT (ad-hoc, operator-invoked) — zero triggers fired

This sentinel raw-signal records the ad-hoc FLASH sweep at 18:00 EDT on
2026-05-20, invoked by the operator ahead of the scheduled 18:00 sweep.

Window: items published since 2026-05-20T12:00:00-04:00 (6 hours since
the prior 12:00 EDT FLASH clean sweep, commit d0721ac).

Active-hours posture: inside 09:00-21:00 EDT — any fired FLASH would
have posted live to #flash-alerts, not queued.

Authorized-targets.yaml empty — passive-only across the board.

## Sources swept

- BleepingComputer RSS (2 in-window items, both substantive)
- The Hacker News RSS (0 in-window items)
- SecurityWeek RSS (0 in-window items)
- The Record RSS (0 in-window items)
- CrowdStrike blog (10 dateless marketing items — unchanged pattern,
  not in-window)
- Microsoft Security Blog RSS (2 in-window items)
- Unit 42 RSS (1 in-window item)
- Mandiant RSS (still feedburner-404 stale pattern; not in-window)
- NVD CVE detail (lookups on CVE-2024-12802 and CVE-2026-9082)
- Drupal Security Advisories (SA-CORE-2026-004 published in-window)
- CISA KEV catalog (WebFetch 403; alt-path search returned no new
  KEV adds since 2026-05-20 batch of 7 already covered in PM brief)
- Splunk archimedes + defenseclaw_local (-24h tracked-IOC superset)

## Six-trigger matrix outcome

Zero of six FLASH triggers fired on any in-window item after applying
anti-noise rule 1 (one FLASH per trigger topic per 24h) and the
A-grade-attestation requirement on Trigger 1.

### Trigger 1 — critical-cve-exploited

**Strongest evaluated candidate: SonicWall CVE-2024-12802 SSL-VPN MFA
bypass — ReliaQuest "first ITW" claim Feb-Mar 2026.**

- CVE: CVE-2024-12802 (2024-vintage, disclosed 2025-01-09 per NVD)
- CVSS v3.1: 9.1 (NVD via CISA-ADP). SonicWall vendor self-scored 6.5;
  the higher CVSS comes from CISA-ADP (CISA Authorized Data Publisher,
  A-grade adjacency). Hard Rule 8 framing: CISA-ADP scoring methodology
  is open-published, no first-party Splunk conflict to arbitrate.
- Active-exploitation evidence: ReliaQuest published research today
  2026-05-20 attributing "with medium confidence" the first ITW
  exploitation of CVE-2024-12802 to incidents observed February-March
  2026. Relayed by BleepingComputer (Bill Toulas, 2026-05-20T17:19 EDT
  in-window) and Cybersecurity Dive (2026-05-19 publish, B-grade
  outside-window relay). Suspected attribution to Akira ransomware
  group via Darktrace and Bitsight earlier-2026 SonicWall lineage
  reporting; ReliaQuest's framing is "initial access broker selling
  credentials to ransomware groups" — Akira name NOT directly attested
  in the ReliaQuest claim per BleepingComputer relay.
- A-grade source requirement: **BORDERLINE-FAIL**. ReliaQuest is the
  PRIMARY source for the ITW claim. ReliaQuest is NOT in
  `infrastructure/source-grades.yaml` — would be a provisional source
  on first surface (precedent: SOCRadar 2026-05-11 surfaced provisional;
  Trendyol / LayerX / Seqrite all surfaced C-grade provisional).
  BleepingComputer (B-grade) and Cybersecurity Dive (B-grade — not
  in source-grades.yaml either but B-tier-equivalent commercial
  security trade press) are RELAYS only. SonicWall PSIRT advisory
  SNWLID-2025-0001 IS A-grade vendor self-disclosure on the
  vulnerability + the incomplete-patching mitigation gap, but does
  NOT directly attest active exploitation — the ITW claim is solely
  ReliaQuest's.
- Trigger 1 strict-read: requires (CVSS >= 9.0) AND
  (article_claims_active_exploitation) AND (source_grade in A-grades).
  CVSS condition satisfied. Active-exploitation-claim condition
  satisfied (ReliaQuest "medium confidence first ITW"). A-grade-source
  condition NOT satisfied — the A-grade vendor self-disclosure
  attests the vuln + mitigation gap, not the exploitation; the
  exploitation claim is from a single provisionally-graded CTI vendor
  with own-published "medium confidence" language.
- **Disposition:** Trigger 1 FAILS strict read. Strong vuln-tracker
  handoff candidate. Surfaced as raw-2026-05-20-flash-1800-001 for
  morning-brief priority-vulnerability item consideration — the
  "incomplete patching" mechanic is operationally meaningful for any
  A&D-prime running SonicWall Gen6 SSL-VPN appliances, and the second
  A-grade attestation (e.g., CISA KEV addition, Mandiant / CrowdStrike
  second-vendor ITW corroboration) would re-trigger evaluation.

### Trigger 2 — tracked-actor-attribution (new)

- Akira ransomware (named by Cybersecurity Dive in SonicWall ITW
  context): NOT in `_roster.yaml`. T2 FAILS on attribution-to-tracked-
  actor predicate.
- Storm-2949 / Fox Tempest / Vanilla Tempest / Webworm carry-forward
  from prior sweeps: all evaluated and failed in 12:00 sweep; no new
  attribution-layer evidence in 6h window.
- Mini Shai-Hulud / TeamPCP: MSTIC publishes formal technical analysis
  in-window (17:48 UTC = 13:48 EDT). MSTIC frames the actor as
  "a threat actor [who] compromised an @antv maintainer account" with
  NO attribution to a named tracked actor; MSTIC uses the unnamed-actor
  framing. TeamPCP attribution chain is via the Breached forum self-
  claim relayed by three B-grade media (covered in 06:08 queued FLASH
  and finding-2026-05-20-FLASH-0001). MSTIC publication is
  CORROBORATION-UPLIFT of the campaign mechanic; NOT a new attribution
  to a tracked actor. Anti-noise lock
  `teampcp-github-internal-repos-breach-via-vscode-extension-2026-05-20`
  (valid to 2026-05-21T06:08:00-04:00) absorbs.

### Trigger 3 — first-party-ioc-hit

- Splunk archimedes + defenseclaw_local -24h sweep returned 2 events
  total, both `index=archimedes` `sourcetype=archimedes:operation`
  (23 events) and `sourcetype=archimedes:scheduler` (15 events).
  These are Archimedes-self-telemetry (collector / scheduler runs),
  NOT tracked-IOC hits.
- Zero hits on the tracked-IOC superset (TeamPCP / Mini Shai-Hulud
  C2 set + GlassWorm + UNC1549 + Charming Kitten + MuddyWater + APT28
  + Beagle / CL-STA-1132).
- **50th consecutive dormant non-self-telemetry sweep** (incrementing
  from 49th cited in 12:00 FLASH sentinel and afternoon brief
  finding-set). Hard Rule 8 framing: silence is not disconfirming,
  not confirming.

### Trigger 4 — tracked-actor TTP change

- No tracked-actor TTP signal in 6h window.
- MSTIC @antv analysis IS new technical detail (Bun-runtime payload
  install, PBKDF2 + SHA-256 string obfuscation, /proc PID-scanning
  for Runner.Worker memory scraping, 12+ Vault token paths, SLSA
  provenance forgery) — but the "actor" remains unattributed by
  MSTIC; not propagatable to a roster actor under Hard Rule 2.
  TTP-uplift is for the campaign cluster (VT-006 / Mini Shai-Hulud),
  not for TeamPCP-attributed (which is Breached-forum self-claim
  layer, not MSTIC-attested).
- Unit 42 npm-threat-landscape update IS a corpus-level summary —
  no new actor attribution. T4 FAILS.

### Trigger 5 — ad-sector-campaign (active, multi-victim, watchlist)

- SonicWall ITW: "multiple sectors" framing per ReliaQuest via
  BleepingComputer — no A&D-prime named, no watchlist entity named.
  Sector-shape only. T5 FAILS strict read on watchlist-specificity.
- Mini Shai-Hulud @antv: MSTIC names "downstream impact" via
  echarts-for-react (1M+ weekly downloads); CI/CD environments
  generically — no A&D-prime named. Anti-noise lock absorbs.
- Webworm carry-forward (12:00 sweep): aerospace sector named but
  no A&D-prime; already evaluated and discarded. T5 still FAILS.

### Trigger 6 — zero-day-no-patch

**Strongest evaluated candidate: Drupal SA-CORE-2026-004 / CVE-2026-9082
SQL injection — published in-window today.**

- CVE: CVE-2026-9082 (NEW, assigned today 2026-05-20)
- CVSS v3.1 (NVD): 6.5 (MEDIUM) — vector CVSS:3.1/AV:N/AC:L/PR:N/UI:N/
  S:U/C:L/I:L/A:N
- Drupal Security Team risk rating: 20/25 ("Highly critical" — Drupal's
  top-tier rating)
- Mechanism: SQL injection in Drupal database abstraction API, affects
  PostgreSQL-backed Drupal installations only, anonymous-user
  exploitable, can lead to information disclosure / privilege
  escalation / RCE
- Affected versions: 8.9.x, 10.4.x-10.6.x, 11.0.x-11.3.x
- Fixed versions: 11.3.10, 11.2.12, 11.1.10, 10.6.9, 10.5.10, 10.4.10
  (released today 2026-05-20 within the 17:00-21:00 UTC publication
  window per PSA-2026-05-18)
- Exploitation status (per Drupal advisory): "Theoretical or white-hat
  (no public exploit code or documentation on development exists)"
- Trigger 6 evaluation:
  - CVSS >= 8.0: FAILS (NVD score 6.5; Drupal's 20/25 "highly critical"
    is a vendor-internal rubric not directly CVSS-comparable)
  - exploitation_confirmed_or_imminent_per_A-grade: FAILS (Drupal A-grade
    self-disclosure explicitly labels status "theoretical")
  - no_patch: FAILS (patches shipped concurrent with disclosure)
- **All three Trigger 6 predicates FAIL.** Disposition: strong
  vuln-tracker handoff candidate — Drupal Highly Critical is rare
  (typically 1-3/year), and the PSA-2026-05-18 "exploits within hours
  of update disclosure" pre-warning means defenders watching this
  surface should prioritize patch deployment. Surfaced as
  raw-2026-05-20-flash-1800-002 for morning-brief / vuln-tracker
  consideration.

## Items evaluated, anti-noise absorbed

| Item | Lock |
|---|---|
| MSTIC — Mini Shai Hulud @antv npm packages enable CI/CD credential theft (17:48 UTC = 13:48 EDT in-window) | `teampcp-github-internal-repos-breach-via-vscode-extension-2026-05-20` (06:08 queued FLASH, valid to 2026-05-21T06:08) — A-grade corroboration uplift on the existing campaign cluster; not a new trigger fire; surfaced as raw-2026-05-20-flash-1800-003 for grader morning-brief CORROBORATION block on VT-006 / finding-2026-05-20-0001 lineage |
| Unit 42 — The npm Threat Landscape: Attack Surface and Mitigations (Updated May 20) (19:30 UTC = 15:30 EDT in-window) | Same lock — A-grade analyst-tier landscape update referencing post-Shai-Hulud npm wormable malware and CI/CD persistence; surfaced as raw-2026-05-20-flash-1800-004 for grader morning-brief CORROBORATION block on VT-006 lineage |

## Items evaluated, discarded (no trigger, no lock — recorded only)

| Item | Failing predicates |
|---|---|
| BleepingComputer — Ukraine identifies infostealer operator tied to 28,000 stolen accounts (21:36 UTC = 17:36 EDT) | T1 FAIL (no CVE); T2 FAIL (18-year-old individual cybercriminal, NOT in _roster.yaml); T3 FAIL (Splunk dormant); T4 FAIL (no actor); T5 FAIL (single California retail victim, no A&D, no campaign); T6 FAIL (no vuln). Single-LE-target IR cybercrime case. Discarded. |
| Microsoft Security Blog — Securing the gaming culture of cultures (16:00 UTC = 12:00 EDT, edge-of-window) | Deputy CISO commentary blog post on Xbox / gaming security; NOT incident or vulnerability content; ALL TRIGGERS FAIL. Discarded. |
| CrowdStrike blog top-10 (dateless marketing content carry-pattern) | All dateless / out-of-window per persistent pattern across 17+ consecutive sweeps; ALL TRIGGERS FAIL. Discarded. |

## Items raw-signaled as morning-brief grader handoff

These are non-FLASH but operationally important items written to disk
for the next pre-brief sweep (morning brief 2026-05-21 07:30) to
evaluate per Mode 1 procedure. They are NOT FLASH-trigger fires.

| Item | Raw-signal | Handoff to |
|---|---|---|
| SonicWall CVE-2024-12802 ITW (ReliaQuest, BleepingComputer relay) | raw-2026-05-20-flash-1800-001 | Vuln-tracker (priority); morning-brief active-threats consideration |
| Drupal CVE-2026-9082 SA-CORE-2026-004 (Highly Critical SQL injection) | raw-2026-05-20-flash-1800-002 | Vuln-tracker; morning-brief vulnerabilities consideration |
| MSTIC formal Mini Shai-Hulud @antv technical analysis | raw-2026-05-20-flash-1800-003 | Grader (uplift on VT-006 / finding-2026-05-20-0001 KAC A1 Test tripwire — 72h closes 2026-05-23 07:30 EDT) |
| Unit 42 npm threat landscape update (May 20) | raw-2026-05-20-flash-1800-004 | Grader (same VT-006 lineage corroboration) |

## Hard Rules compliance

- **Rule 2 (no first-time attribution):** Compliance verified. ReliaQuest's
  Akira-suspected framing preserved as Cybersecurity Dive relay; not
  cross-walked to any tracked actor. MSTIC's unattributed framing on the
  @antv compromise preserved verbatim; not propagated to TeamPCP except
  via the existing Breached-self-claim chain already locked. Webworm /
  Fox Tempest / Vanilla Tempest / Storm-2949 carry-forward attribution
  framing unchanged from 12:00 sweep.
- **Rule 3 (no PoC content):** Compliance verified. SonicWall ITW
  detection indicators (sess="CLI" parameter, Event IDs 238/1080)
  preserved as defensive-detection signal only; no attack walkthrough
  extracted. Drupal CVE-2026-9082 SQL injection mechanism preserved at
  class level (PostgreSQL-backed installations, anonymous user
  exploitable) without exploit primitives. MSTIC @antv payload internals
  preserved as defensive-observability content (Bun runtime, PBKDF2
  obfuscation, /proc PID scanning, Vault token paths) — these are
  defender-actionable indicators of compromise, not attack code.
- **Rule 4 (no active scans, authorized-targets.yaml empty):** Compliance
  verified. Only passive RSS / WebFetch on public news pages + NVD detail
  + Drupal advisory + Splunk first-party. No Shodan / Censys / VT
  lookups. No SpiderFoot / theHarvester / nmap. All targets passive-read-
  only.
- **Rule 6 (no quotes beyond 15 words):** Compliance verified. ReliaQuest
  "medium confidence" + "first in-the-wild exploitation" (under limit);
  Drupal advisory "Theoretical or white-hat" (under limit); MSTIC
  "deploy the Mini Shai-Hulud payload" (under limit). No verbatim quotes
  exceed 15 words.
- **Rule 7 (15-word quote, one per source):** Verified across all
  raw-signal output (this sentinel + the four handoff items).
- **Rule 8 (Splunk first-party priority):** First-party sweep result is
  dormant continuation — 50th consecutive sweep with zero hits on
  tracked-IOC superset (-24h). No conflict between Splunk telemetry and
  any external claim in this sweep. Self-telemetry events (collector /
  scheduler runs) properly excluded from tracked-IOC hit counting.

## Carry-forward observations from afternoon brief (do NOT re-grade)

The 2026-05-20-afternoon brief (commit e97afee) shipped at 16:00 EDT
covering 0 of 6 FLASH triggers across 4 afternoon findings. Carry-forward
status:

- **finding-2026-05-20-0006 (Cisco Secure Workload CVE-2026-20223 CVSS
  10.0, A2 / very-likely + likely):** No CISA KEV addition observed in
  this sweep. No second-vendor PoC publication observed. Carry-forward
  stable; no resurface threshold met in 2h since publication.
- **finding-2026-05-20-0005 (CISA KEV +7 batch including Defender pair
  CVE-2026-41091 + CVE-2026-45498, A2 / very-likely + likely):**
  Federal deadline 2026-06-03; no new in-window signal beyond afternoon
  baseline.
- **finding-2026-05-20-0004 (Webworm China-aligned, B3 / roughly-even):**
  Single-source veto holds; no Mandiant / CrowdStrike / Unit 42 / MSTIC
  corroboration of Webworm-specific claims this sweep.
- **finding-2026-05-20-0007 (Anthropic Claude Code sandbox bypass
  SOCKS5, B3 / roughly-even):** No new in-window signal; KAC A1 Test
  tripwire on finding-2026-05-20-0001 remains OPEN until 2026-05-23
  07:30 EDT. MSTIC + Unit 42 npm publications today (handoff items
  raw-2026-05-20-flash-1800-003 and -004) are corroboration on the
  Mini Shai-Hulud campaign cluster but do NOT directly resolve the
  KAC tripwire (which is on the SecurityWeek-asserted Claude-Code-
  backdoor-drop claim, not the npm @antv compromise mechanism).
- **finding-2026-05-20-FLASH-0001 (TeamPCP GitHub-corp self-claim,
  B2 / likely):** Anti-noise lock continues. MSTIC + Unit 42
  publications are corroboration uplift on the same campaign cluster.

## Source-health deltas

- bleepingcomputer: last_successful_fetch refresh 2026-05-20T18:01:31
  (2 in-window items, both substantive). Status healthy; failure_count
  0; runtime-fields-only update. Operator notes preserved verbatim.
- thehackernews: last_successful_fetch refresh 2026-05-20T18:01:33
  (0 in-window items; feed last_modified 21:41 UTC = 17:41 EDT inside
  window from feed-server activity). Status healthy; failure_count 0;
  runtime-fields-only update. Operator notes preserved verbatim.
- securityweek: last_successful_fetch refresh 2026-05-20T18:01:34
  (0 in-window items; feed last_modified 15:49 UTC pre-window).
  Status healthy; failure_count 0; runtime-fields-only update.
  Operator notes preserved verbatim.
- the-record: last_successful_fetch refresh 2026-05-20T18:01:35
  (0 in-window items via RSS). Status healthy; failure_count 0;
  runtime-fields-only update. Operator notes preserved verbatim.
- crowdstrike: last_successful_fetch refresh 2026-05-20T18:03:45
  (10 dateless marketing items, ~18th consecutive sweep of same
  pattern). Status healthy; failure_count 0; runtime-fields-only
  update. Operator notes preserved verbatim.
- unit42: last_successful_fetch refresh 2026-05-20T18:03:47 — PRODUCTIVE
  (1 in-window item, npm threat landscape update May 20). Status
  healthy; failure_count 0; runtime-fields-only update. Operator notes
  preserved verbatim. First productive Unit 42 fetch since the long
  quiet pattern noted in prior sweeps.
- mstic: last_successful_fetch refresh 2026-05-20T18:03:47 — PRODUCTIVE
  (2 in-window items, Mini Shai-Hulud @antv post + Gaming CISO Deputy
  blog). Status healthy; failure_count 0; runtime-fields-only update.
  Operator notes preserved verbatim. MSTIC publication of formal
  technical analysis on the @antv campaign is significant for the
  Archimedes A&D corpus given the campaign's locked status.
- nvd: WebFetch on CVE-2024-12802 and CVE-2026-9082 succeeded
  (single-CVE-detail queries, not the lastModStartDate window query).
  Status healthy; runtime-fields-only update. Operator notes preserved
  verbatim.
- mandiant: still feedburner-404 stale pattern; not invoked this sweep.
  Operator notes preserved verbatim.
- splunk-archimedes + splunk-defenseclaw: -24h query returned 2 events
  total (Archimedes self-telemetry only). 50th consecutive dormant
  non-self-telemetry sweep. Status healthy; query latency normal.

## LEGAL-POLICY refusals

None. No prohibited query patterns received. All evaluated content was
passive read of public news / vendor advisories / first-party Splunk.
SonicWall PSIRT direct fetch (psirt.global.sonicwall.com) returned 403
on the vendor advisory page — this is a passive-read failure on the
publisher side, NOT an Archimedes-side LEGAL-POLICY refusal. The
ReliaQuest blog index page also did not surface direct content via
WebFetch (returned a "loading" page). Both are infrastructure / scraping
limitations, not policy issues. The substantive claims attributed to
ReliaQuest in this sentinel come from BleepingComputer's quoted-summary
relay and the Cybersecurity Dive secondary relay, both passive RSS /
public-page reads.

## Orchestrator note (informational)

This is an ad-hoc operator-invoked sweep ~2 hours ahead of the scheduled
18:00 EDT FLASH sweep. The scheduled 18:00 sweep should still run on
its normal cadence; if so, it will see a substantially overlapping 6h
window and will (per anti-noise rule 1) absorb the items raw-signaled
this sweep without re-triggering. Per FLASH-POLICY anti-noise rule 1,
the topic-lock keys recorded here are authoritative for the next 24h.

## TLP marking

TLP:CLEAR — all source content from public news / vendor advisories /
CISA / Drupal / NVD / Microsoft Security Blog / Unit 42; no first-party
Splunk content reproduced (zero IOC hits to reproduce; self-telemetry
event counts only); no PII; no credentials.
