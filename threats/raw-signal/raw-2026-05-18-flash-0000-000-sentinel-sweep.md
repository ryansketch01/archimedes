---
raw_id: raw-2026-05-18-flash-0000-000
collected_at: 2026-05-18T00:05:00-04:00
run_id: flash-sweep-20260518-000000
collection_mode: flash_sweep
source:
  source_yaml_id: multi
  source_name: "Multi-source FLASH sweep (scheduled, 00:00 EDT Sunday→Monday transition)"
  source_url: null
  published_at: null
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: []
triage_tags:
  - sentinel
  - flash_sweep_clean
  - dormant_splunk_sweep_40
  - scheduled_0000_window
  - quiet_hours_active
  - non_promotable
iocs_extracted: false
iocs_count: 0
text_word_count: 0
promoted: false
promoted_note: "Sentinel tombstone — non-promotable per established precedent (see raw-2026-05-17-flash-0000-000, raw-2026-05-17-flash-0600-000, raw-2026-05-17-flash-1200-000, raw-2026-05-17-flash-1800-000 pattern). One in-window MiniPlasma item evaluated and DISCARDED (PoC-only, no A-grade exploitation attestation, no tracked actor, no A&D entity, no IOC) — flagged as status-update CANDIDATE for 08:00 morning brief grader as new tracked-vuln carry-forward consideration only; no separate raw-signal file written. Two DarkReading items (AI-essay forward-dated 2026-05-18 13:00 UTC and South Korea deepfake regulation 01:00 UTC) discarded per same precedent as 2026-05-17 18:00 FLASH AI-essay discard."
ttl_expires_at: 2026-08-16T00:05:00-04:00
---

# FLASH sweep 2026-05-18 00:00 EDT (scheduled, Sunday→Monday transition) — CLEAN

## Sweep summary

**Mode:** flash_sweep (scheduled 00:00 EDT window, Sunday→Monday transition)
**Window:** 2026-05-17T18:00:00-04:00 → 2026-05-18T00:00:00-04:00 (~6h since 18:00 FLASH 33d3f9a, ~8h since 16:00 afternoon brief 005596f)
**Trigger evaluation outcome:** 0 of 6 FLASH triggers fired.
**Disposition:** clean sweep — no candidates promoted to grader; no escalation; no Discord post (FLASH-POLICY: silent on clean sweep + quiet-hours active regardless).
**Quiet-hours state:** ACTIVE-QUIET (00:00 EDT inside 21:00–09:00 EDT quiet-hours per FLASH-POLICY.md — had any trigger fired, post to `#flash-alerts` would have QUEUED to `infrastructure/flash-queue.yaml` for 09:00 catchup sweep, NOT posted live). Critical-override conditions NOT met (no CVSS 10.0 + active exploitation + tracked actor + A&D watchlist entity coincidence — see MiniPlasma evaluation below for why this is correct).

## Sources queried (active A-grade / B-grade priority set)

- **BleepingComputer** (`bleepingcomputer`) — reachable (200, last-modified 2026-05-18T03:50 UTC = 23:50 EDT inside window from feed-server activity, etag fe21599a61b6dc694d236876683ce473), **1 in-window item** after since-filter: MiniPlasma Windows zero-day PoC by Lawrence Abrams 2026-05-17T22:30 UTC = 18:30 EDT (see Item 1 evaluation below).
- **The Hacker News** (`thehackernews`) — reachable (200, last-modified 2026-05-18T03:31 UTC = 23:31 EDT inside window from feed-server activity, 50 items in feed total), 0 in-window items after since-filter.
- **CISA all.xml** (`cisa-advisories`) — reachable (200, 30 items in feed), 0 in-window items after since-filter.
- **The Record** (`the-record`) — reachable (200), 0 in-window items (5 items total in feed, most recent pre-window).
- **Krebs on Security** (`krebs`) — reachable (200, last-modified 2026-05-13T10:43 UTC pre-window), 0 in-window items.
- **SecurityWeek** (`securityweek`) — reachable (200, last-modified 2026-05-16T12:45 UTC pre-window, etag W/"6c84e363e15c44c9fae953b857d4f0a3"), 0 in-window items.
- **Unit 42 feedburner** (`unit42`) — reachable (200, last-modified 2026-05-15T19:46 UTC pre-window), 0 in-window items.
- **Microsoft Security Blog parent feed** (`mstic`) — reachable (200, last-modified 2026-05-14T21:51 UTC pre-window), 0 in-window items.
- **WeLiveSecurity / ESET** (`eset`) — reachable (200, 100 items in feed total, last-modified 2026-05-16T06:58 UTC pre-window), 0 in-window items after since-filter.
- **CrowdStrike** (`crowdstrike`) — reachable (200, last-modified 2026-05-17T07:02 UTC pre-window, etag "1564-651fe075c4ba9-gzip"), 10 dateless marketing/MQ items returned (persistent pattern across 15+ consecutive sweeps documented in source-health note; no threat-intel content). All filtered as marketing/non-priority per established source-health pattern.
- **DarkReading** (`darkreading`) — reachable (200, last-modified 2026-05-18T04:01 UTC inside window from feed-server activity), 2 items after since-filter both DISCARDED (see Items 2 + 3 below): (a) "The Boring Stuff is Dangerous Now" (Shlomie Liberow, forward-dated 2026-05-18T13:00 UTC AI-essay class — same item discarded in 2026-05-17 18:00 FLASH sweep, anti-noise applies); (b) "Can Laws Stop Deepfakes? South Korea Aims to Find Out" (Alexander Culafi, 2026-05-18T01:00 UTC, regulatory analysis on South Korean deepfake law).
- **Recorded Future** (`recorded-future`) — reachable (200, last-modified 2026-05-15T14:00 UTC pre-window), 0 in-window items.
- **Mandiant feedburner** (`mandiant`) — known broken (~20+ consecutive 404s, feedburner endpoint persistently retired); skipped per source-health.
- **CrowdStrike RSS** path validated above; behavior unchanged.
- **Cisco Talos feeds/posts/default** path returned 404 this sweep — same as established broken-path pattern; canonical `blog.talosintelligence.com/rss/` workaround path (recovered in 2026-05-17 12:00 sweep per source-health) was not re-tested this FLASH sweep per FLASH-fast scope. Holding pending operator pass on source-health.yaml canonical path.
- **SANS ISC** (`sans-isc`) — `rssfeed.xml` returned XML parse error this sweep (same parse-error class observed in 2026-05-17 06:00 FLASH sweep, recovered next sweep). Held healthy per transient-class history and operator directive (failure_count not incremented on this FLASH-fast invocation).
- **Sophos** (`news.sophos.com/en-us/feed/`) — 404 again this sweep, consistent with stale-state per source-health.
- **GitHub Advisories Atom** (`github-advisories`) — known persistent 406; not re-tested this sweep (FLASH-fast scope).
- **CISA KEV JSON** (`cisa-kev`) — not WebFetched directly this FLASH-fast sweep; relies on `cisa-advisories` all.xml master feed which surfaced 0 in-window items. Five most-recent KEV entries unchanged from 2026-05-17 18:00 FLASH sweep state (CVE-2026-42897 due 2026-05-29 / CVE-2026-20182 federal deadline LAPSED end-of-day 2026-05-17 / CVE-2026-42208 due 2026-05-11 / CVE-2026-6973 / CVE-2026-0300 — all carry-forwards).

## Splunk first-party non-self-telemetry sweep

- `index=defenseclaw_local OR index=archimedes earliest=-24h@h | stats count by index, sourcetype`:
  - `archimedes` / `archimedes:operation` — 15 events (self-telemetry, run lifecycle).
  - `archimedes` / `archimedes:scheduler` — 17 events (self-telemetry, scheduled-task firing).
  - **0 events** outside self-telemetry sourcetypes.
- `index=defenseclaw_local OR index=archimedes NOT sourcetype=archimedes:scheduler NOT sourcetype=archimedes:operation earliest=-24h@h | head 20` — **0 events.**

This is the **40th consecutive dormant non-self-telemetry Splunk sweep** (39 at 2026-05-17 18:00 FLASH 33d3f9a; 38 at 16:00 afternoon brief 005596f; 37 at 15:30 pre-brief; 36 at 12:00 FLASH c17bf91; 35 at 08:00 morning brief c8a140d). Per doctrine: silence is not disconfirming. No IOC hits against `threats/iocs/_master-index.yaml`. **No Trigger 3 fire.**

## In-window items evaluated

### Item 1 — BleepingComputer (2026-05-17T22:30 UTC = 18:30 EDT, inside window): "New Windows 'MiniPlasma' zero-day exploit gives SYSTEM access, PoC released"

**Source:** BleepingComputer (Lawrence Abrams byline). Source grade: B (provisional, awaiting ratification).

**Headline content (per WebFetch direct retrieval, Hard Rule 3 no PoC code reproduced):**

- **Vulnerability class:** Local Privilege Escalation (LPE) to SYSTEM on Windows 11 Pro and Windows 11 generally; researcher demonstrates the technique on "fully patched" Windows systems.
- **CVE identifier:** CVE-2020-17103 — i.e., a **2020 CVE rediscovery**, not a net-new 2026 CVE assignment. Originally reported to Microsoft by Google Project Zero researcher James Forshaw September 2020; reported fix issued December 2020 Patch Tuesday; researcher (Chaotic Eclipse aka Nightmare Eclipse) now claims the fix was incomplete and the vulnerability remains exploitable on current Windows 11 builds.
- **CVSS score:** **NOT PUBLISHED** in source (no NVD or vendor-attested CVSS available at sweep time for the rediscovery claim; original 2020 CVE-2020-17103 NVD CVSS not surfaced by source).
- **Patch status:** Researcher-asserted unpatched; Microsoft has NOT been cited as confirming the regression at sweep time. The article notes the technique does NOT work in "Windows 11 Insider Preview Canary build" — implying a fix may already be present in unreleased builds.
- **Exploitation status:** **PoC-only.** A proof-of-concept exploit was published by the researcher. **No A-grade source (Microsoft MSRC, CISA, Mandiant, MSTIC, CrowdStrike, Volexity, Unit 42, Talos, Symantec, ESET) is cited as attesting active exploitation of MiniPlasma itself in the wild.** The article references that "all three vulnerabilities were spotted being exploited in attacks" applying to MiniPlasma + BlueHammer (CVE-2026-33825) + RedSun (silently patched, no CVE) — but per Hard Rule 2 evaluation (WebFetch direct re-query): **this is editorial framing by BleepingComputer, not vendor-attestation.** No specific A-grade source is cited for the exploitation claim. No named tracked actor. No specific victim. No IOC.
- **Originating researcher:** Chaotic Eclipse (alias Nightmare Eclipse). Independent researcher; not in `source-grades.yaml`; first surface in Archimedes corpus.
- **A&D-sector relevance:** None named in source. Indirect / structural only — LPE-to-SYSTEM on Windows endpoints applies broadly to any A&D prime running Windows 11 fleet; defensive-relevance is high but per Hard Rule 2 is forward-inference NOT source-attested.
- **IOCs:** None published.

**FLASH-trigger evaluation:**

- **Trigger 1 (Critical CVE actively exploited, CVSS ≥ 9.0, A-grade attestation):** **FAIL.**
  - No published CVSS score for the rediscovery claim (the original 2020 CVE-2020-17103 NVD CVSS is not surfaced by the source; researcher does not state CVSS).
  - Active exploitation of MiniPlasma is **not** attested by an A-grade source; the "spotted being exploited" claim in the article is editorial framing applying to a 3-vulnerability cluster (MiniPlasma + BlueHammer + RedSun) WITHOUT specifying which vendor confirmed which exploitation observation.
  - Single-source surface (BleepingComputer relay alone; no Microsoft MSRC, no MSTIC, no CISA confirmation in window — same single-source-veto precedent as CVE-2026-42897 carry-forward and CVE-2026-42945 NGINX Rift carry-forward applies).
- **Trigger 2 (New tracked actor attribution):** **FAIL.** No `_roster.yaml` actor named in source. Researcher Chaotic Eclipse / Nightmare Eclipse is not a roster member.
- **Trigger 3 (First-party Splunk IOC hit, within 24h):** **FAIL.** 40th consecutive dormant non-self-telemetry Splunk sweep; no IOCs from source to query against in any case (none published).
- **Trigger 4 (Tracked actor TTP change, A/B-grade source, attributable):** **FAIL.** No tracked actor; TTP not attributable.
- **Trigger 5 (Active A&D-sector campaign, multi-victim):** **FAIL.** No A&D entity named; no campaign described; no victim count.
- **Trigger 6 (Zero-day no-patch, CVSS ≥ 8.0 or widely-deployed, exploitation confirmed/imminent):**
  - Wide-deployment criterion: **MET** — Windows 11 is broadly deployed. Patch-absence criterion: **partially MET** — researcher asserts unpatched, Microsoft has not yet confirmed or refuted.
  - CVSS ≥ 8.0 criterion: **UNKNOWN** — no CVSS published in source for the rediscovery; original 2020 CVE-2020-17103 NVD record not consulted this sweep (FLASH-fast scope). LPE-to-SYSTEM class typically scores ~7.0-7.8 (CVSS v3 base for local-vector / low-privileges-required / high-impact-CIA) — likely below 8.0 floor.
  - "Exploitation confirmed or imminent per A-grade source": **FAIL.** No A-grade source attests confirmed exploitation of MiniPlasma; "imminent" cannot be inferred per Hard Rule 2 (no A-grade attestation of imminence).
  - **DISPOSITION: FAIL on Trigger 6** because the exploitation-confirmed-or-imminent leg of the conjunction is not met from an A-grade source. The BleepingComputer editorial "spotted being exploited" framing fails to satisfy the A-grade-attestation requirement (single-source B-grade media relay, no vendor-attested exploitation claim, same evidentiary bar that capped CVE-2026-42945 NGINX Rift VulnCheck honeypot scanner-class probes at "defensive telemetry" rather than "confirmed production exploitation").

**Disposition for MiniPlasma:** **DISCARDED for FLASH purposes.** Single-source B-grade relay with PoC-only exploitation status and editorial-framing-only "exploited in attacks" claim. Flagged as **status-update CANDIDATE for 08:00 morning brief grader** for evaluation as either: (a) new tracked-vuln addition to `threats/vulnerabilities/_index.yaml` if subsequent A-grade corroboration surfaces (Microsoft MSRC confirmation / MSTIC active-exploitation telemetry / CISA KEV addition), or (b) discarded as commodity-researcher PoC release with insufficient corroboration to warrant tracking. Defensive note: if A&D-prime SOCs see external surface scanning matching researcher-published PoC technique signatures, that would warrant a Trigger 3 fire — but no such signal in window from Splunk dormant state.

### Item 2 — DarkReading (2026-05-18T13:00 UTC = 09:00 EDT 2026-05-18 forward-dated): "The Boring Stuff is Dangerous Now"

- Same item as discarded in 2026-05-17 18:00 FLASH sweep 33d3f9a (Shlomie Liberow opinion essay on AI-agent vulnerability discovery and AI-generated code volume). Anti-noise applies (one FLASH per trigger-topic per 24h — but moot since not a trigger-topic to begin with). Opinion essay; no tracked actor; no CVE; no A&D entity; no IOC; all 6 triggers fail.
- **Disposition: DISCARDED.** Already covered in prior sweep decision-trail.

### Item 3 — DarkReading (2026-05-18T01:00 UTC = 21:00 EDT 2026-05-17 inside window): "Can Laws Stop Deepfakes? South Korea Aims to Find Out"

- Topic: Regulatory analysis by Alexander Culafi on South Korean local-election deepfake regulation as policy test bed.
- Named attribution: none (no actor attribution; no specific incident; no campaign).
- Roster intersect: none.
- CVE / vulnerability: none cited.
- A&D entity: none named.
- Sector / campaign claim: none — policy / regulatory commentary.
- **Trigger evaluation:** All 6 triggers FAIL — no CVE, no actor, no first-party IOC, no TTP change, no A&D campaign, no zero-day. Regulatory-policy commentary class content, not a status-update candidate for any brief.
- **Disposition: DISCARDED.**

## Carry-forwards preserved (NOT re-triggered, all unchanged from 18:00 FLASH and prior)

- **CVE-2026-20182** (Cisco Catalyst SD-WAN auth bypass, CVSS 10.0, KEV federal deadline LAPSED end-of-day 2026-05-17 Sunday) — finding-2026-05-14-0005 carry-forward chain. **Deadline post-mortem now active state for 08:00 morning brief grader.** No fresh A-grade attestation in 18:00–00:00 window (Mandiant feedburner broken, MSTIC pre-window, Unit 42 pre-window, Talos broken-path, Volexity pre-window, CrowdStrike marketing-only, no new BleepingComputer/Hacker News in-window items). Federal-agency-compliance reporting expected to surface in next-day CISA / OMB reporting per established pattern, not in the KEV catalog itself.
- **CVE-2026-42897** (Microsoft Exchange OWA XSS, KEV T-11d due 2026-05-29 Friday) — finding-2026-05-15-0003 carry-forward. >48h single-source veto on exploitation-claim layer (Mandiant / Volexity / Unit 42 / MSTIC / CrowdStrike all silent through 2026-05-17 18:00 confirmed; this sweep extends silence to full 24h+ since afternoon brief). Microsoft MSRC originating attester; no independent A-grade corroboration in window.
- **CVE-2026-42945 NGINX Rift PoC** (depthfirst) — finding-2026-05-16-0001 carry-forward. VulnCheck honeypot scanner-class probe refinement (B-grade defensive telemetry, NOT A-grade attestation of production exploitation) absorbed into finding. **Hard Rule 3 reminder: PoC repo URL not linked.** No new A-grade attestation in window.
- **Symantec / Carbon Black + SentinelLABS April 2026 Fast16 framework** (A2 cluster anchor) — finding-2026-05-16-0003 carry-forward. Symantec provisional-A 72h ratification clock fired 2026-05-16T18:25; now T+29h35m past elapsed deadline awaiting operator pass per established precedent. Not actionable in this sweep per task scope.
- **Pwn2Own Berlin 2026 Day 2 Exchange RCE-to-SYSTEM chain** (Orange Tsai / DEVCORE) — embargoed through ZDI vendor-coordinated-disclosure clock (~2026-08-13). finding-2026-05-16-0002 carry-forward unchanged.
- **Turla / Kazuar / Secret Blizzard D+2 relay layer** — finding-2026-05-14-0006 / reject-2026-05-16-0001 anti-noise duplicate-lock active; no new relay surface this window.
- **Tycoon2FA device-code phishing PhaaS** — absorbed into finding-2026-05-17-0002 per afternoon brief 005596f. Commodity criminal PhaaS, no tracked actor, anti-noise rule 1 active.
- **eSentire provisional-B source-grades.yaml addition candidate** — flagged for librarian pickup per afternoon brief; no librarian action expected pre-00:00 sweep. Carried forward to 08:00 morning brief librarian pickup window.

## Source health observations (this sweep) — operator pass deferred, NOT applied to source-health.yaml

Per task scope (operator has pending edits to source-health.yaml per untracked-files state including `.pm-update.py`, `.afternoon-edits.txt`, `.diff-summary*` files), these observations are recorded here ONLY; source-health.yaml is NOT modified by this collector invocation.

- `bleepingcomputer`: 200 with productive in-window content (MiniPlasma item); healthy continues.
- `thehackernews`: 200 last-modified inside window from feed-server activity; healthy continues with 0 in-window items.
- `cisa-advisories`: all.xml 200, healthy continues.
- `darkreading`: 200 with 2 in-window items both discarded; healthy continues.
- `sans-isc`: `rssfeed.xml` returned XML parse error this sweep (same transient-class as 2026-05-17 06:00 sweep which recovered next sweep). NOT incrementing failure_count on this FLASH-fast invocation per transient-class history; next sweep (06:00) will validate. Operator may consider tightening transient-class handling if pattern recurs.
- `cisco-talos`: `feeds/posts/default` returned 404 this sweep (this is the original broken-path; the canonical workaround path `blog.talosintelligence.com/rss/` from 2026-05-17 12:00 sweep recovery was not re-tested this FLASH-fast invocation per scope discipline). Holding pending operator pass on source-health.yaml canonical path.
- `mandiant`, `dragos`, `sophos`, `ars-security`, `github-advisories`: carried in expected-broken / stale state per source-health.yaml; no action.
- `crowdstrike`: 15th-or-16th consecutive sweep returning 10 dateless marketing/MQ items; pattern fully entrenched per source-health note. No state change.
- All other queried sources: reachable, zero non-discarded in-window items.

## Carry-forward to 06:00 FLASH sweep / 08:00 morning brief grader

The 06:00 FLASH (~6h from this sweep, still inside quiet-hours so any trigger would QUEUE not post) and 08:00 morning brief Monday will inherit the following operational state:

1. **CVE-2026-20182 federal KEV deadline post-mortem** — deadline LAPSED end-of-day Sunday 2026-05-17. The 08:00 morning brief grader should evaluate whether overnight reporting surfaces (a) federal-agency-compliance reporting, (b) post-deadline exploitation surge reporting tied to UAT-8616 expansion, (c) Talos UAT-8616 second-corpus widening, or (d) silence (the parsimonious expectation per the >48h second-corpus silence pattern through 2026-05-17 18:00). Federal compliance metric typically surfaces in next-day CISA / OMB reporting rather than the KEV catalog itself.
2. **CVE-2026-42897 Exchange OWA XSS** carry-forward unchanged with extended single-source-veto state. T-11d federal deadline Friday 2026-05-29.
3. **CVE-2026-42945 NGINX Rift PoC** carry-forward unchanged. Hard Rule 3 PoC URL not linked.
4. **MiniPlasma (CVE-2020-17103 rediscovery)** — new entrant to potential tracked-vuln consideration. **Status-update CANDIDATE for 08:00 morning brief grader.** Per single-source veto + Hard Rule 2 + PoC-only-not-exploitation evaluation, NOT a FLASH-trigger fire this sweep. Grader to evaluate whether: (a) tracking this vulnerability formally requires A-grade corroboration (MSRC confirmation / MSTIC active-exploitation telemetry / CISA KEV addition), (b) commodity-PoC-researcher publication class does not warrant tracking absent vendor-attested production exploitation. Defensive-relevance to A&D-prime Windows 11 fleets is structural-indirect not source-attested.
5. **Symantec/SentinelLABS Fast16 provisional-A ratification clock** now T+29h35m past elapsed deadline; operator pass remains pending per afternoon brief disposition. Awaiting next operator session.
6. **Pwn2Own Berlin Day 2 Exchange RCE chain** ZDI embargo unchanged through ~2026-08-13.
7. **Turla/Kazuar D+2 relay layer** duplicate-lock unchanged.
8. **Tycoon2FA device-code phishing** absorbed into finding-2026-05-17-0002; no FLASH carry-forward state.
9. **40th consecutive dormant non-self-telemetry Splunk sweep** state — silence is not disconfirming, but the cadence should continue tracking. Self-telemetry events (15 archimedes:operation + 17 archimedes:scheduler in last 24h) confirm the pipeline is running normally; no external IOC hits.

## Disposition

**Clean sweep, 0 FLASH triggers fired, 40th consecutive dormant non-self-telemetry Splunk sweep, no escalation, no Discord post.**

All carry-forwards preserved unchanged. Sentinel tombstone non-promotable per established precedent. The 06:00 FLASH sweep (~6h from this sweep, inside quiet-hours) and the 08:00 morning brief pipeline will handle: (1) MiniPlasma status-update consideration as new candidate for tracked-vuln list pending A-grade corroboration; (2) CVE-2026-20182 deadline post-mortem reporting if any surfaces overnight; (3) standard carry-forward chain refresh; (4) any net-new actor-attribution or campaign reporting that surfaces in the 00:00–08:00 EDT window.

**Hard Rule 2 compliance verified** — BleepingComputer's "spotted being exploited" framing for MiniPlasma is preserved verbatim as editorial-not-A-grade-attested and does NOT propagate as Archimedes-originated active-exploitation claim. **Hard Rule 3 compliance verified** — no PoC repository URL linked, no exploit code reproduced. **LEGAL-POLICY prohibited-query-patterns** not triggered (no active recon, no exploitation assistance, no credential storage). **SpiderFoot** not invoked (authorized-targets.yaml empty).
