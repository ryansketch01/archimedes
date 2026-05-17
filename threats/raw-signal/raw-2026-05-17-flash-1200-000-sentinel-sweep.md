---
raw_id: raw-2026-05-17-flash-1200-000
collected_at: 2026-05-17T12:03:00-04:00
run_id: flash-sweep-20260517-120000
collection_mode: flash_sweep
source:
  source_yaml_id: multi
  source_name: "Multi-source FLASH sweep (scheduled, 12:00 EDT window)"
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
  - dormant_splunk_sweep_36
  - scheduled_1200_window
iocs_extracted: false
iocs_count: 0
text_word_count: 0
promoted: false
ttl_expires_at: 2026-08-15T12:03:00-04:00
---

# FLASH sweep 2026-05-17 12:00 EDT (scheduled) — CLEAN

## Sweep summary

**Mode:** flash_sweep (scheduled 12:00 EDT window)
**Window:** 2026-05-17T06:00:00-04:00 → 2026-05-17T12:00:00-04:00 (~6h since 06:00 sweep 83cb46f, ~4h since 08:00 morning brief c8a140d)
**Trigger evaluation outcome:** 0 of 6 FLASH triggers fired.
**Disposition:** clean sweep — no candidates promoted to grader; no escalation; no Discord post (FLASH-POLICY: silent on clean sweep).
**Quiet-hours state:** ACTIVE-WINDOW (12:00 EDT inside 09:00–21:00 EDT active window per FLASH-POLICY.md — had any trigger fired, post to `#flash-alerts` would have been live, not queued). Critical-override conditions NOT met (no CVSS 10.0 + active exploitation + tracked actor + A&D watchlist entity coincidence).

## Sources queried (active A-grade priority set)

- CISA all.xml (`cisa-advisories`) — reachable (200), 0 in-window items.
- CISA KEV JSON (`cisa-kev`) — top entries unchanged from 06:00 sweep: CVE-2026-42897 (Exchange OWA XSS, due 2026-05-29 / T-12d), CVE-2026-20182 (Cisco SD-WAN, due 2026-05-17 / **T-0 federal deadline TODAY, ~12h remaining at sweep time**), CVE-2026-42208, CVE-2026-6973, CVE-2026-0300, CVE-2026-31431, CVE-2026-41940, CVE-2024-1708. **Zero KEV additions dated 2026-05-17.** All within carry-forward state.
- The Hacker News (`thehackernews`) — reachable (200), **1 in-window item** evaluated and DISCARDED (see below): NGINX CVE-2026-42945 honeypot-class exploitation framing at 07:57 EDT.
- BleepingComputer (`bleepingcomputer`) — reachable (200), **1 in-window item** evaluated and DISCARDED (see below): Tycoon2FA device-code phishing at 10:43 EDT.
- Krebs on Security (`krebs`) — reachable (200), 0 in-window items.
- The Record (`the-record`) — reachable (200), 0 in-window items.
- SecurityWeek (`securityweek`) — reachable (200), 0 in-window items (last-modified 2026-05-16).
- Unit 42 feedburner (`unit42`) — reachable (200), 0 in-window items.
- Microsoft Security Blog parent feed (`mstic`) — reachable (200), 0 in-window items (last-modified 2026-05-14 21:51 UTC; no Sunday cadence expected).
- WeLiveSecurity (`eset`) — reachable (200), 0 in-window items.
- SentinelLabs (`sentinelone`) — reachable (200), 0 in-window items (last-modified 2026-05-15; Fast16 carry-forward unchanged).
- SANS ISC (`sans-isc`) — reachable (200) this sweep, RSS path parse clean (recovery from 06:00 transient). Diary index surfaced no 2026-05-17 entries. Held healthy.
- Cisco Talos (`cisco-talos`) — RSS endpoint `blog.talosintelligence.com/rss/` reachable (200) this sweep, **recovered** from prior two consecutive 404s at 2026-05-16 17:30 sweep and 2026-05-17 06:00 sweep against the `/feeds/posts/default` path. Latest post 2026-05-14 (the SD-WAN UAT-8616 carry-forward); no 2026-05-17 posts. Held healthy. Path-correction observation noted for source-health.yaml — operator pass.
- Sophos (`sophos`) — RSS endpoint `news.sophos.com/en-us/feed/` 404 this sweep (third consecutive failure: 2026-05-16T07:30 + 2026-05-17T00:00 + 2026-05-17T06:00 + this sweep makes ≥3 consecutive observations after the 06:00 commit's failure_count increment to 3 + stale_since 2026-05-17). Now at stale-threshold per the ≥2-consecutive-failure rule confirmed in 06:00 commit. Held healthy on WebFetch alt-path (301 redirect to www.sophos.com/en-us/blog?taxonomy_blog_category=Threat+Research/) but source-health.yaml entry status remains `stale`. Operator pass still pending replacement-path identification.
- Mandiant feedburner (`mandiant`) — known broken (~20 consecutive 404s), skipped per source-health.
- Dragos (`dragos`) — known broken (`/blog/feed/` 404), skipped per source-health.
- Ars Technica security (`ars-security`) — known stale since 2026-05-09, skipped per source-health.
- X / RSSHub bridges (`x-cisagov`, `x-gossithedog`) — rsshub.app 404 again. Held in expected-broken state.

## Splunk self-telemetry sweep

`index=archimedes OR index=defenseclaw_local earliest=-6h` — **9 events total**, all in self-telemetry sourcetypes (`archimedes:operation` + `archimedes:scheduler`). **Zero non-self-telemetry events.** This is the **36th consecutive dormant non-self-telemetry Splunk sweep** (35 at 08:00 morning brief c8a140d; 34 at 06:00 sweep 83cb46f; cadence increments each sweep that returns zero non-self-telemetry). Per doctrine: silence is not disconfirming. No IOC hits against `threats/iocs/_master-index.yaml`.

## In-window items evaluated and discarded

### Item 1 — The Hacker News (2026-05-17T07:57 EDT): "NGINX CVE-2026-42945 Exploited in the Wild"

- Topic: VulnCheck honeypot telemetry shows scanner-class probes against NGINX CVE-2026-42945 (Rift). THN editorial framing characterizes this as "exploitation in the wild." VulnCheck's underlying claim per the source is "exploitation attempts observed against honeypots" — i.e., scanner-class activity, not confirmed compromise of production systems.
- Named attribution: none (unattributed scanner-class activity).
- Roster intersect: none.

**Trigger evaluation:**

- Trigger 1 (Critical CVE actively exploited, A-grade attestation): **FAIL** — CVE-2026-42945 is the morning-brief carry-forward (Rift PoC, patch available). VulnCheck is provisional-B in `source-grades.yaml`, NOT A-grade. THN editorial framing of "exploited in the wild" exceeds VulnCheck's own scoped claim ("honeypot exploitation attempts" = scanner-class probes against decoy infrastructure, not confirmed production-system compromise). Under Hard Rule 2 (no attribution origination) and INTEL-GRADING credibility-check protocol, Archimedes does not propagate THN's framing as A-grade active-exploitation. The scoped VulnCheck claim is a **material status change** vs the morning brief's "no new exploitation signal overnight" disposition on CVE-2026-42945, but the bar for Trigger 1 (A-grade attestation of confirmed active exploitation) is not met. Status update flagged for afternoon brief grader as carry-forward refinement, NOT a FLASH fire.
- Trigger 2 (New tracked actor attribution): **FAIL** — no actor attribution.
- Trigger 3 (First-party IOC hit): **FAIL** — Splunk dormant sweep #36; no first-party Splunk hit.
- Trigger 4 (Tracked actor TTP change): **FAIL** — no tracked-actor TTP change documented.
- Trigger 5 (A&D sector campaign): **FAIL** — no A&D-watchlist entity named; scanner-class probes against undifferentiated honeypot infrastructure.
- Trigger 6 (Zero-day no patch): **FAIL** — patch is available (NGINX 1.27.4 / Plus R34 P1 per morning brief carry-forward).
- **Disposition: DISCARDED** for FLASH purposes. Status-update carry-forward flagged for 16:00 afternoon brief grader as CVE-2026-42945 disposition refinement (active scanner-class probes documented = "exploitation attempts against honeypots" per VulnCheck, NOT confirmed production active exploitation — Hard Rule 2 paraphrase). Afternoon briefer to decide whether to upgrade CVE-2026-42945 carry-forward language from "PoC published, no exploitation signal" to "PoC published, VulnCheck honeypot probes observed [B-grade], no confirmed production exploitation."

### Item 2 — BleepingComputer (2026-05-17T10:43 EDT): "Tycoon2FA hijacks Microsoft 365 accounts via device-code phishing"

- Topic: Tycoon2FA Phishing-as-a-Service kit operators pivot to Microsoft 365 device-code authentication flow phishing (no CVE; abuses legitimate Microsoft OAuth device-code endpoint to bypass MFA).
- Named attribution: none (criminal PhaaS operators, no tracked actor named).
- Roster intersect: none.

**Trigger evaluation:**

- Trigger 1 (Critical CVE): **FAIL** — no CVE, abuse of legitimate authentication flow.
- Trigger 2 (New tracked actor attribution): **FAIL** — no tracked actor (criminal PhaaS).
- Trigger 3 (First-party IOC hit): **FAIL** — Splunk dormant sweep #36; no IOCs.
- Trigger 4 (Tracked actor TTP change): **FAIL** — no tracked actor.
- Trigger 5 (A&D sector campaign): **FAIL** — no A&D entity named; broad Microsoft 365 commodity-criminal targeting.
- Trigger 6 (Zero-day no patch): **FAIL** — no vulnerability disclosed.
- **Disposition: DISCARDED.** Device-code phishing as a TTP is operationally relevant to A&D M365 defenders but the source neither names an A&D entity nor a tracked actor. Afternoon brief grader/briefer may pick up as a sub-FLASH defensive-TTP note if scope permits; no FLASH fire.

## Carry-forwards preserved (NOT re-triggered, all unchanged from 06:00 sweep and 08:00 morning brief)

- **CVE-2026-20182** (Cisco Catalyst SD-WAN auth bypass, CVSS 10.0, KEV **T-0 federal deadline TODAY 2026-05-17, ~12h remaining at sweep time**) — finding-2026-05-14-0005 carry-forward chain; morning brief c8a140d covered as headline calendar-event.
- **CVE-2026-42897** (Microsoft Exchange OWA XSS, KEV T-12d due 2026-05-29) — carry-forward; morning brief's >48h single-source veto on exploitation-claim layer (Mandiant / Volexity / Unit 42 / MSTIC / CrowdStrike all silent) preserved.
- **CVE-2026-42945 NGINX Rift PoC** — carry-forward; status-update candidate flagged from Item 1 above (VulnCheck honeypot probes) for 16:00 afternoon briefer; Hard Rule 3 PoC repo URL not linked.
- **Symantec / Carbon Black + SentinelLABS April 2026 Fast16 framework** (A2 cluster anchor) — finding-2026-05-16-0003 carry-forward. Symantec provisional-A 72h ratification clock fired 2026-05-16T18:25 (now T+17h35m at sweep time); operator pass still pending per morning brief disposition.
- **Pwn2Own Berlin 2026 Day 2 Exchange RCE-to-SYSTEM chain** — embargoed through ZDI clock (~2026-08-13); morning brief carry-forward unchanged.
- **Turla / Kazuar / Secret Blizzard D+2 relay layer** — finding-2026-05-14-0006 / reject-2026-05-16-0001 anti-noise duplicate-lock active; no new relay surface this window.

## Source health observations (this sweep) — operator pass deferred, NOT applied to source-health.yaml

Per task scope (operator has pending edits to source-health.yaml per untracked-files state), these observations are recorded here and in the commit message ONLY; source-health.yaml is NOT modified by this librarian invocation.

- `sophos`: news.sophos.com/en-us/feed/ third consecutive 404 confirmed (compounding the failure_count 2→3 increment at the 06:00 commit 83cb46f, which had already moved the entry to `status: stale` with `stale_since: 2026-05-17`). At-or-past stale threshold per ≥2-consecutive-failure rule. WebFetch alt-path against the homepage continues to work; operator pass for replacement-path identification still pending.
- `cisco-talos`: **RECOVERY** — `blog.talosintelligence.com/rss/` returned 200 this sweep, recovering from prior 404s observed at the `/feeds/posts/default` path on 2026-05-16T17:30 and 2026-05-17T00:00 + 2026-05-17T06:00 (06:00 commit body noted a 3rd consecutive 404 on the old path). The working path appears to be `/rss/` not `/feeds/posts/default`. Operator pass: update canonical RSS path in source-health.yaml and/or watch-config.yaml when the gitignored runtime file is next edited.
- `sans-isc`: parse-error transient from 06:00 sweep recovered this sweep (consistent prior recovery pattern: 2026-05-12 transient also recovered next sweep). No action.
- `mandiant`, `dragos`, `ars-security`: carried in expected-broken / stale state per source-health.yaml; no action.
- All other queried sources: reachable, zero non-discarded in-window items.

## Disposition

**Clean sweep, 0 FLASH triggers fired, 36th consecutive dormant non-self-telemetry Splunk sweep, no escalation, no Discord post.** All carry-forwards preserved unchanged. The 16:00 EDT afternoon brief pipeline will handle: (1) CVE-2026-20182 KEV deadline post-mortem (deadline arrives ~T+4h after the afternoon brief publishes; federal-agency compliance state to be assessed), (2) CVE-2026-42945 status-update refinement candidate (VulnCheck honeypot probes per Item 1, B-grade scanner-class signal — afternoon briefer to decide framing), (3) Symantec provisional-A ratification clock now T+17h35m past elapsed deadline (operator pass pending), (4) standard carry-forward chain.
