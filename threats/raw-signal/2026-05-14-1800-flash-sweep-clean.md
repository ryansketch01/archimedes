---
raw_id: raw-2026-05-14-1800-flash-sweep-clean
collected_at: 2026-05-14T18:08:00-04:00
run_id: flash-sweep-20260514-180000
collection_mode: flash_sweep
source:
  source_yaml_id: meta-sweep-tombstone
  source_name: "FLASH sweep tombstone (no candidates)"
  source_url: null
  published_at: 2026-05-14T18:00:00-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: []
triage_tags: [flash_sweep_clean, audit_trail, non_flash]
iocs_extracted: false
iocs_count: 0
text_word_count: 0
promoted: false
ttl_expires_at: 2026-08-12T18:08:00-04:00
test: false

sweep_summary:
  sweep_window_start: 2026-05-14T16:00:00-04:00
  sweep_window_end: 2026-05-14T18:00:00-04:00
  sweep_window_hours: 2
  scope_rationale: "Narrow FLASH-fast scope per orchestrator instruction. 16:00 afternoon brief just shipped (Cisco SD-WAN CVE-2026-20182 UAT-8616 KEV 3-day deadline; MSTIC Kazuar / Secret Blizzard architectural; Salt Typhoon Azerbaijan carry-forward + Twill Typhoon FDMTP; OpenAI TanStack confirmation; node-ipc UNATTRIBUTED). Last clean FLASH was 06:00 today (0 triggers / 14 sources)."
  sources_queried: 15
  sources_skipped_stale: 4               # ars-security, censys, urlscan, hibp
  sources_blocked_this_sweep: 2          # cisa.gov direct (403), threatfox-browse (CAPTCHA)
  items_fetched_in_window: 6
  items_already_covered_anti_noise: 4    # Cisco SD-WAN re-relays, ESET/UNC1151 re-relay, OpenAI/TanStack re-relay, FamousSparrow re-relay
  items_evaluated_against_flash_triggers: 4
  flash_candidates: 0
  brief_update_candidates_for_morning: 2
  source_health_changes: []              # no status flips this sweep
---

# FLASH sweep 2026-05-14 18:00 EDT — clean (0 triggers)

**0 triggers fired. 0 candidates queued. Window: 2026-05-14 16:00 EDT → 2026-05-14 18:00 EDT (2 hours, post-afternoon-brief).**

Quiet hours: 18:00 EDT is OUTSIDE the quiet window (active hours 09:00–21:00 EDT). Had any trigger fired, the FLASH would have been eligible for immediate Discord post. No critical-override conditions met (no CVSS 10.0 + active exploitation + tracked actor + A&D-watchlist named target simultaneously in any in-window item — the Cisco SD-WAN CVE-2026-20182 finding IS CVSS 10.0 with active exploitation, but it was already absorbed in the 16:00 afternoon brief).

## Sweep window

2026-05-14T16:00:00-04:00 → 2026-05-14T18:00:00-04:00 (2h, post-afternoon-brief)

## Sources queried (15)

Priority A-grade primary research / vendor PSIRTs / CISA / first-party Splunk:

- **CISA KEV catalog** (cisa.gov direct fetch returned 403 WAF — typical pattern; KEV state confirmed via this morning's brief frontmatter and afternoon brief deadlines; most recent KEV addition is CVE-2026-20182 Cisco Catalyst SD-WAN dateAdded 2026-05-14, dueDate 2026-05-17 — already absorbed in 16:00 afternoon brief).
- **CISA advisories all.xml** (direct page fetch returned 403 — same WAF pattern as cisa.gov direct; productive endpoint pattern via fetch_feed remains unchanged but the FLASH-fast scope used WebFetch direct, blocked).
- **Cisco Talos blog** — 0 in-window items. Most recent posts visible: "Ongoing exploitation of Cisco Catalyst SD-WAN vulnerabilities" (12:02 EDT — already in 16:00 brief) and "The time of much patching is coming" (14:00 EDT — already in 16:00 brief).
- **Palo Alto Networks PSIRT** (security.paloaltonetworks.com/CVE-2026-0300) — advisory last-updated 2026-05-14, but the only change in the May 14 update was "Updated the Fix release timeline for 10.2.16-h7" (patch ETA adjustment, NOT a new exploitation claim or attribution). CVE-2026-0300 itself is from 2026-05-05 and was FLASHed twice on 2026-05-06 (morning + 18:00 KEV-add update). Anti-noise applies; no resurface trigger.
- **Palo Alto Unit 42** — 0 in-window items. Most recent visible item is the 2026-05-11 AD CS Escalation analysis (pre-window).
- **Microsoft MSTIC** (security/blog/feed/) — 1 in-window item: "Defense in depth for autonomous AI agents" (2026-05-14T16:00 UTC — best-fit timestamp shows 12:00 EDT; AI-security thought-leadership content, no APT attribution, no fresh CVE, no in-window threat-research). Kazuar / Secret Blizzard architectural post is from 11:00 EDT (15:00 UTC) — already absorbed in 16:00 brief. Configuration-vulnerability-AI-apps post is from 10:20 EDT (14:20 UTC) — out of window.
- **Mandiant Google Threat Intel index** (cloud.google.com/blog/topics/threat-intelligence) — same top-8 visible titles as 06:00 sweep, all triangulated out-of-window per prior triangulations. Feedburner remains 404 (twentieth-plus consecutive failure pattern). No fresh post-16:00 publication identifiable.
- **CrowdStrike blog** — 1 in-window item: "Now Live: The CrowdStrike 2026 Financial Services Threat Landscape Report" (timestamped 00:00 EDT, technically not post-16:00; financial-sector annual report, no APT attributions matching our roster for the 16:00→18:00 window).
- **SentinelOne Labs** — 0 in-window items (most recent post 13:00 UTC = 09:00 EDT — before cutoff).
- **Sophos News** (Threat Research feed) — endpoint shows posts back to Dec 2025, no fresh May 2026 entries in the threat-research feed (consistent with Sophos's multi-week cadence).
- **Volexity blog** — 0 in-window items, no May 2026 publication on RSS.
- **BleepingComputer RSS** — 2 in-window items:
  - "Cisco warns of new critical SD-WAN flaw exploited in zero-day attacks" (16:09 EDT) — re-relay of the Cisco SD-WAN CVE-2026-20182 story already in the 16:00 afternoon brief; anti-noise applies.
  - "Hackers exploit auth bypass flaw in Burst Statistics WordPress plugin" (17:07 EDT) — net-new but evaluated against FLASH triggers, see below.
- **SecurityWeek RSS** — 0 in-window items past 14:00 UTC (10:00 EDT) cutoff. YellowKey/GreenPlasma BitLocker piece referenced in feed was from earlier today (already in 2026-05-13 afternoon brief carry-forward).
- **The Hacker News RSS (feedburner)** — 4 in-window items:
  - Cisco Catalyst SD-WAN CVE-2026-20182 (THN re-relay of the already-absorbed Cisco SD-WAN story; anti-noise).
  - node-ipc Stealer Backdoor — THN re-relay of the already-absorbed node-ipc UNATTRIBUTED story from the 16:00 afternoon brief; anti-noise.
  - ThreatsDay Bulletin (PAN-OS RCE / Mythos cURL / AI Tokenizer / Operation GriefLure / Operation SilentCanvas / Langflow / ClickFix / ModeloRAT) — weekly aggregation, see Item 4 below.
  - Ghostwriter Targets Ukrainian Government (THN re-relay of ESET FrostyNeighbor / UNC1151 story already in the 2026-05-14 morning brief; anti-noise — see Item 3 below).
- **The Record RSS** — 2 in-window items:
  - "OpenAI asks macOS users to update after TanStack npm supply chain attack" (16:26 EDT) — re-relay of OpenAI / TeamPCP / VT-006 confirmation already in the 16:00 afternoon brief; anti-noise.
  - "ODNI taps officials to coordinate response to foreign election threats" (14:21 EDT — pre-window) — policy/governance, not a FLASH trigger candidate.
- **Krebs on Security** — 0 in-window items. Most recent post is 2026-05-13 Patch Tuesday roundup (already pre-window).

Free passive enrichment / threat-feeds (touch-only):

- **abuse.ch ThreatFox browse** — CAPTCHA / browser-verification challenge blocked WebFetch direct (no fresh IOC scan this sweep).
- **abuse.ch URLhaus API root** — documentation page only (auth-key required for actual recent-feed data).
- **abuse.ch ThreatFox API endpoint** — 401 without POST body / auth (skipped, no Auth-Key configured in WebFetch).

First-party telemetry:

- **Splunk `archimedes` + `defenseclaw_local`** — last-24h sweep returned 37 events, all archimedes-internal sourcetypes (`archimedes:operation` × 23, `archimedes:scheduler` × 14). Zero security-event sourcetypes; zero tracked-IOC matches against the corpus IOC set (PAN-OS / MuddyWater / Ivanti EPMM / FamousSparrow / TeamPCP / node-ipc). 24th consecutive dormant sweep with the non-archimedes-internal stream. Per Hard Rule 8: silence is absence of evidence, not evidence of absence.

## Items evaluated against FLASH triggers

### Item 1 — Burst Statistics WordPress plugin CVE-2026-8181 active exploitation (BleepingComputer, 2026-05-14T17:07 EDT)

- CVE-2026-8181 affecting Burst Statistics 3.4.0–3.4.1 (patched 3.4.2 released 2026-05-12).
- Approximately 200K installed sites; ~115K remain exposed per Wordfence telemetry.
- Wordfence reported discovery 2026-05-08; Wordfence blocked 7,400+ exploit attempts in a 24h window confirmed by 2026-05-14 BC piece.
- CVSS not stated in the article (NVD entry not surfaced in window).
- No threat-actor attribution. No A&D sector framing. Patch available.
- Primary research: Wordfence (WP-niche vendor; not in source-grades.yaml at A-grade; closest precedent is Sucuri / Patchstack provisional B for WP-niche).

**Trigger evaluation:**

- **Trigger 1 (critical CVE + active exploitation + A-grade primary) — FAILS on two predicates.** (a) CVSS score not stated; not confirmed ≥9.0. (b) Wordfence is not A-grade primary per source-grades (WP-niche provisional B at best); BleepingComputer is B-grade media relay layer. Active exploitation predicate is MET (7,400 attempts in 24h is real activity, not PoC).
- **Trigger 6 (zero-day no patch) — FAILS.** Patch available (3.4.2 since 2026-05-12 — 2 days ago).
- **Trigger 5 (active A&D-sector campaign) — FAILS.** Targeting is WordPress sites at large; no aerospace/defense / no watchlist company / no Tier-1/2 supplier framing.

**Disposition: BRIEF-UPDATE candidate for 2026-05-15 morning brief.** WordPress-plugin active-exploitation with 7,400 attempts/24h is non-trivial telemetry but the A&D-relevance is structural / dependency-graph only (WordPress is not typical A&D-prime web stack). Useful for completeness; not FLASH-eligible.

### Item 2 — Cisco SD-WAN CVE-2026-20182 (BleepingComputer 16:09 EDT, THN later)

- Re-relay of the story already in the 16:00 afternoon brief (finding-2026-05-14-0005).
- CISA KEV (dateAdded 2026-05-14, dueDate 2026-05-17, 3-day federal deadline).
- Talos attributes to UAT-8616 with "high confidence" (single-source, WEP capped at likely; red-team C1-C6 caveats propagated in the 16:00 brief).

**Trigger evaluation:** **Anti-noise rule applies** (one FLASH per trigger topic per 24h). Already absorbed in 16:00 afternoon brief; resurface as continuing-coverage in tomorrow's morning brief.

### Item 3 — Ghostwriter / UNC1151 / FrostyNeighbor (THN re-relay of ESET, 2026-05-14T~10:00 EDT prior + 19:30 IST re-relay)

- THN re-relay of the ESET Damien Schaeffer FrostyNeighbor analysis already in the 2026-05-14 morning brief (finding-2026-05-14-0001).
- Same Ukrainian-government + Polish/Lithuanian-industrial sector framing.
- Belarus-aligned UNC1151 / Ghostwriter is **NOT in `_roster.yaml`** (already flagged as /new-actor candidate in morning brief).

**Trigger evaluation:**

- **Trigger 2 (new attribution for tracked actor) — FAILS.** UNC1151 / Ghostwriter is not in roster. The 24 tracked actors checked (TeamPCP, Stardust Chollima, Lazarus, UNC1549, GlassWorm, APT28, Sandworm, Volt Typhoon, APT29, Salt Typhoon, Charming Kitten, Miyako, Scattered Spider, Handala Hack, LockBit, REvil, APT40, Cl0p, APT41, BlackCat, Payouts King, MuddyWater, APT34, APT37) include no alias overlap.
- **Trigger 5 (active A&D-sector campaign) — FAILS.** No A&D-watchlist company named.

**Disposition: Anti-noise** (already absorbed in morning brief). Continuing /new-actor candidacy status (analyst flagged Intent=3 or Intent=4 expected cap; HIGH unlikely per "threat-box methodology is conservatively bounded" operational note).

### Item 4 — THN ThreatsDay Bulletin: PAN-OS CVE-2026-0300 + Mythos cURL + AI Tokenizer / Hugging Face + Operation GriefLure + Operation SilentCanvas + Langflow CVE-2026-33017 + ModeloRAT (2026-05-14T~12:00 EDT)

- Aggregation of multiple stories, several with deep prior coverage in the Archimedes corpus:
  - **PAN-OS CVE-2026-0300** — primary research at Palo Alto PSIRT 2026-05-05, FLASHed twice 2026-05-06 (06:00 morning + 18:00 KEV-add update). The May 14 PSIRT update was a patch ETA tweak for 10.2.16-h7 only — no fresh exploitation claim, no fresh attribution, no new IOC publication. Anti-noise (already deeply covered).
  - **Mythos cURL bug** — Daniel Stenberg blog disclosure, "not going to make anyone grasp for breath" per Stenberg himself; low severity; no active exploitation; planned to publish with next curl 8.21.0 release. Not a FLASH candidate (low severity + no exploitation).
  - **AI Tokenizer / Hugging Face** — HiddenLayer research on tokenizer.json modification enabling output control / sensitive data exfiltration. No threat-actor attribution. No active exploitation in window. Research-class disclosure.
  - **Operation GriefLure** — Vietnam telecom + PH healthcare phishing+RAT. Unknown / state-sponsored APT, no roster overlap. No A&D framing.
  - **Operation SilentCanvas** — Multi-target PowerShell/ScreenConnect. Unknown attribution. No A&D framing.
  - **ModeloRAT** — Already absorbed in 2026-05-13 afternoon brief (Rapid7 KongTuke / fake Microsoft Teams IT-support, B3 grade).
  - **Langflow CVE-2026-33017** — Aggregator-only NATS C2 reference; no active-exploitation primary cited in window. Not raw-signal-worthy at this layer.
  - **TeamPCP $1,000 Monero contest** — Aggregator framing of TeamPCP-corpus-already-covered worm; anti-noise.

**Trigger evaluation:**

- **Trigger 1 (critical CVE + active exploitation + A-grade primary):**
  - PAN-OS CVE-2026-0300: CVSS 9.3 ≥9.0 ✓; active exploitation per Palo Alto PSIRT ✓ ("Limited exploitation has been observed"); Palo Alto PSIRT A-grade primary ✓. **BUT anti-noise rule fires** — already FLASHed 2026-05-06 (twice). No fresh exploitation claim, no fresh IOC publication, no fresh attribution in this aggregator surface. **FAILS on anti-noise**.
  - Mythos cURL: low severity per the discoverer; **FAILS** on CVSS predicate.
  - AI Tokenizer: research-class; **FAILS** on active-exploitation predicate.
  - Langflow CVE-2026-33017: aggregator-only; no primary cited in window; **FAILS** on A-grade-primary predicate.

- **Trigger 4 (tracked actor TTP change, A/B grade) — FAILS.** No tracked actor in the bulletin contents that we are not already tracking.

- **Trigger 5 (active A&D-sector campaign, multi-victim, A&D sector) — FAILS.** None of the campaigns name A&D primes or watchlist entities. Operation GriefLure is Vietnam telecom + Philippines healthcare. Operation SilentCanvas is multi-target without A&D framing.

- **Trigger 6 (zero-day no patch) — FAILS.** No zero-day-without-patch entries in the bulletin.

**Disposition:** Anti-noise on PAN-OS / TeamPCP / ModeloRAT (already covered); BRIEF-UPDATE candidate for the cURL / AI-tokenizer / Operation GriefLure / Operation SilentCanvas items in tomorrow's morning brief if the underlying research surfaces independently in window.

## Items pre-window but worth noting for tomorrow's morning brief

These items surfaced in this sweep but timestamp pre-16:00 EDT today; they are **carry-forward candidates for tomorrow's morning brief**, not FLASH-eligible for this 16:00→18:00 window:

- **Sandworm OT/ICS retrospective via Nozomi Networks** (industrialcyber.co 2026-05-14 07:37 EDT — pre-window, not previously surfaced in the corpus). Nozomi analyzed 5.5M alerts → 29 confirmed Sandworm-related events July 2025–Jan 2026 across 7 countries (US/Mexico/UK/Germany/Belgium/Colombia/Thailand) in manufacturing/transportation/pharmaceuticals/food/motor vehicles. Sandworm IS in roster (#007). **Trigger 5 fails on TWO predicates: (a) retrospective historical analysis, not active campaign; (b) no aerospace/defense / no watchlist company named.** Trigger 4 fails on no novel TTPs (EternalBlue / WannaCry / Cobalt Strike all well-documented Sandworm tradecraft). Trigger 2 fails on attribution being restated, not new. Best handled as morning-brief content with Sandworm-roster-entry context.

- **Bitdefender FamousSparrow / Azerbaijan O&G** (industrialcyber.co 2026-05-14 07:32 EDT — pre-window) — already FLASHed 2026-05-13 14:30 (Salt Typhoon #010 alias attribution). Industrialcyber piece is a B-grade relay of the Bitdefender primary; anti-noise applies. Carry-forward.

- **West Pharmaceutical + Foxconn ransomware** (industrialcyber.co 2026-05-14 09:29 EDT — pre-window) — original disclosure dates 2026-05-04 (West) and 2026-05-07 (Foxconn). Nitrogen ransomware = NOT in tracked roster. Foxconn alleged-stolen data includes Apple/NVIDIA/Intel/Google/Dell but no explicit A&D-prime named. No FLASH trigger fires.

## Hard Rule 8 — First-party Splunk

Clean across `archimedes` and `defenseclaw_local` over -24h. 37 events returned, all archimedes-internal audit-trail sourcetypes. Zero tracked-IOC matches. 24th consecutive dormant sweep with the non-archimedes-internal stream. Per doctrine: silence is absence of evidence, not evidence of absence.

## Quiet-hours and critical-override audit

- Quiet hours: 18:00 EDT is INSIDE 09:00–21:00 EDT active window. Had a FLASH fired, it would have been eligible for immediate Discord post (no queue).
- Critical-override conditions (all 4 required): the Cisco SD-WAN CVE-2026-20182 finding is CVSS 10.0 ✓ with confirmed active exploitation ✓ and UAT-8616 attribution (per Talos high-confidence) but UAT-8616 is **NOT in roster** ✗ and no A&D-watchlist entity is named as a specific UAT-8616 target ✗ — 2 of 4 conditions, override does not apply. (The CVE was already FLASH-equivalent absorbed in the 16:00 afternoon brief regardless.)

## Anti-noise / 24h-lockouts in effect

- Cisco SD-WAN CVE-2026-20182 — absorbed in 16:00 afternoon brief; 24h FLASH lockout until 2026-05-15 16:00 EDT.
- OpenAI / TanStack / TeamPCP — absorbed in 16:00 afternoon brief; 24h lockout.
- node-ipc UNATTRIBUTED stealer — absorbed in 16:00 afternoon brief; 24h lockout.
- MSTIC Kazuar / Secret Blizzard — absorbed in 16:00 afternoon brief; 24h lockout.
- Salt Typhoon / FamousSparrow Azerbaijan O&G — FLASHed 2026-05-13 14:30, carry-forwarded in 16:00 afternoon brief; 24h lockout (relative to FLASH) expired but reinforced via brief carry-forward (effective lockout until 2026-05-14 16:00 EDT just passed; any genuinely new content would now be eligible — but no new content this sweep, only re-relay).
- Twill Typhoon / Mustang Panda FDMTP — absorbed in 16:00 afternoon brief; 24h lockout.
- ESET FrostyNeighbor / UNC1151 — absorbed in 08:00 morning brief + 16:00 afternoon brief mention; 24h lockout.
- PAN-OS CVE-2026-0300 — FLASHed twice 2026-05-06; deep coverage; only fresh material would resurface.

## Source-health changes this sweep

None. No status flips. Failure counters unchanged for endpoints that returned WAF blocks today (cisa.gov direct, threatfox-browse CAPTCHA) — those are persistent-known WAF / CAPTCHA patterns, not source-health degradation. All A-grade vendor feeds queried (Talos / Mandiant / CrowdStrike / MSTIC / Unit42 / SentinelOne / Volexity / Sophos) remain healthy with normal cadence.

## Disposition

**Return: 0 candidates — clean sweep.** Pass nothing forward to grader / red-team / briefer. Continuing-coverage items (Cisco SD-WAN deadline T-3, OpenAI / TanStack 30-day window, FamousSparrow Azerbaijan, Sandworm Nozomi retrospective, Burst Statistics WordPress) are pre-brief candidates for the 2026-05-15 07:30 collection cycle / 08:00 morning brief, not FLASH-eligible.
