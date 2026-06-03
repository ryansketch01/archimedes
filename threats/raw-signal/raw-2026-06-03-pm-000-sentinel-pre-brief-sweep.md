---
raw_id: raw-2026-06-03-pm-000-sentinel-pre-brief-sweep
collected_at: 2026-06-03T15:32:00-04:00
run_id: pre-brief-20260603-153000
collection_mode: pre_brief_collection
sweep_type: pm-pre-brief-sentinel
time_window_start: 2026-06-03T07:30:00-04:00      # since AM pre-brief
time_window_end: 2026-06-03T15:30:00-04:00
look_back_tolerance_hours: 14
sources_queried: 15
sources_skipped_stale: 5
items_fetched: ~35
items_matching_filters: 5                          # PM-001 through PM-005 (excluding Acer below-bar marginal)
items_held_below_threshold: 1                      # Acer Wave 7 — below FLASH/grader bar, carry to PM brief if grader wants
items_discarded: 24                                # Marketing, anti-noise relays, non-A&D, non-threat-intel
splunk_first_party_hits: 0
triage_tags: [sentinel, pm_pre_brief, scheduled_canonical_sweep]
ttl_expires_at: 2026-09-01T15:32:00-04:00
---

# PM pre-brief sentinel — 2026-06-03 15:30 EDT

**Canonical scheduled afternoon pre-brief collection sweep per `doctrine/INTEL-OPERATIONS.md` Mode 1.** Eight-hour window since AM pre-brief at 07:30 EDT, 14-hour look-back tolerance per doctrine. Five raw-signal files written (PM-001 through PM-005). One item held below threshold (Acer Wave 7 — not raw-signaled but flagged in this sentinel for grader awareness).

## Sources queried (15 healthy / 5 stale skipped)

**Healthy / queried:**
- `cisa-advisories` (all.xml — 1 item in window; KEV-add alert for CVE-2026-45247 Mirasvit)
- `cisa-kev` (KEV JSON catalog — full-catalog scan; CVE-2026-45247 confirmed as today's add)
- `bleepingcomputer` (RSS — 3 items in window)
- `the-hacker-news` (RSS — 1 item in window)
- `securityweek` (RSS — 5 items in window)
- `securityaffairs` (RSS — 2 items in window)
- `theregister` (security/headlines.atom — 1 item in window)
- `therecord` (RSS — 1 item in window)
- `mstic` / `microsoft.com/en-us/security/blog/feed` (RSS — 0 items in window; MSTIC published 06:00 EDT and would be the AM brief surface)
- `mandiant` (alt endpoint `mandiant.com/resources/blog/rss.xml` — 0 items in window; feedburner persistent failure pattern)
- `unit42` (feedburner — 0 items in window)
- `rapid7` (RSS — 1 item in window, marketing-only — discarded)
- `cisco-talos` (blog.talosintelligence.com/rss/ — 0 items in window)
- `sans-isc` (RSS — 1 item in window, diary swagger.json scanning — non-A&D commodity scan content, discarded)
- `krebs` (RSS — 0 items in window)
- `splunk-archimedes` + `splunk-defenseclaw` (targeted IOC + actor keyword sweep over last 24h — 0 first-party hits)

**Skipped stale (per under-24h rule or persistent stale):**
- `msrc` (stale since 2026-05-30 — feed parse error 4x consecutive)
- `ars-security` (stale since 2026-05-09 — endpoint 404, workaround pending)
- `x-cisagov` (stale since 2026-05-10 — nitter.net bridge fragility)
- `x-gossithedog` (stale since 2026-05-09 — account delisted on nitter.net)
- `sophos` (stale since 2026-05-17 — RSS path retired)

## Items raw-signaled (5)

| # | Source(s) | Topic | Raw-signal file |
|---|-----------|-------|-----------------|
| 1 | CISA KEV + cisa-advisories alert | CVE-2026-45247 KEV add — Mirasvit Full Page Cache Warmer (Magento 2) PHP deserialization RCE; CVSS 9.8; **3-day federal due date 2026-06-06**; patched 2026-05-25 (v1.11.12); originating researcher Sansec; active-exploitation telemetry by Imperva | raw-2026-06-03-pm-001 |
| 2 | SecurityWeek + SecurityAffairs (originating: Symantec Threat Hunter Team + Carbon Black) | Suspected state-linked espionage operation against major global stock exchange — 150 days of Outlook mailbox theft via Aspose-wrapper, Adobe/OneDrive-masquerading binaries, Dropbox/OneDrive Personal exfil, hardcoded Microsoft IPs to bypass DNS logging; **no actor attribution**, **no A&D-prime victim named**, **undisclosed exchange** | raw-2026-06-03-pm-002 |
| 3 | SecurityWeek (originating: Defiant / Wordfence) | CVE-2026-8206 Kirki WordPress plugin unauth privesc/account takeover, CVSS 9.8, **active exploitation** ("thousands of attacks over past 24 hours"); Burst Statistics co-disclosure (no CVE); patches available | raw-2026-06-03-pm-003 |
| 4 | BleepingComputer + (BC carries marginal new technical detail beyond SecurityWeek + THN published earlier) | HTTP/2 Bomb update — CVE-2026-49975 (Apache); **new technical detail** — per-server memory exhaustion timelines (Envoy 10s, Apache 18s, nginx/IIS 45s); amplification ratios; Calif/OpenAI Codex methodology more explicit. **No ITW**, no new affected products beyond AM brief matrix | raw-2026-06-03-pm-004 |
| 5 | The Register | Microsoft disclosure-policy arc cumulative meta-coverage — Askar VS Code zero-day already in AM brief; The Register adds **explicit Nightmare-Eclipse + StarLabs reference linking 7 disclosures in one narrative**, **plus Microsoft Digital Crimes Unit backdown framing** (new context vs AM brief). Watch_signal `microsoft_disclosure_policy_arc_5th_data_point` from AM brief is the receptacle; this is meta-arc consolidation, NOT a fifth data point | raw-2026-06-03-pm-005 |

## Items held below threshold (1)

| # | Source | Topic | Disposition rationale |
|---|--------|-------|------------------------|
| 1 | BleepingComputer (article URL moved/404 from 12:00 FLASH evaluation; recoverable via alt path `bleepingcomputer.com/news/security/acer-warns-of-max-severity-zero-days-affecting-wave-7-routers`) | CVE-2026-49200 / CVE-2026-49201 Acer Wave 7 router max-severity zero-days — broken access control plaintext credentials + hardcoded AES key persistent backdoor; researcher Gergo Pap; patches planned end-June 2026; **explicit "no in-the-wild" + no public PoC** per BleepingComputer | **Below grader bar.** Consumer mesh router (Acer Wave 7), not A&D-applicable critical-infrastructure or watchlist-prime equipment. No ITW, no PoC, no actor. Trigger 6 fails on "exploitation confirmed OR exploitation imminent per A-grade." Not raw-signaled; flagged here in sentinel for grader visibility in case the grader wants to track for vulnerability-watch list addition (Acer is not on existing vuln-watch). |

## Items discarded (24)

- **Anti-noise relays** (8 items): BleepingComputer "CISA warns of active attacks exploiting Android, Linux bugs" (KEV-add relay, identical to FLASH 12:00 item 1); SecurityAffairs FSB statement (already at FLASH 12:00 item 12 — no attribution, no IOCs, below B2 grade minimum on FLASH); SecurityWeek "Organizations Warned of Exploited Linux Kernel Vulnerability" (same KEV-add cycle); THN "One-Click GitHub Dev Attack" (Askar VS Code relay, already AM finding-0002); THN "Unpatched Windows Search URI" already AM finding-0004 — surfaced earlier as 12:00 FLASH but no new content this sweep; SecurityWeek "HTTP/2 Bomb" (already AM finding-0003); SecurityWeek "Security of 100 AI Agents" (risk-quadrant academic ranking, not threat-intel); SecurityWeek "IMA Diligence Services Data Breach" (525k consumer-data breach, no A&D nexus).
- **Marketing / non-threat-intel** (4 items): SecurityWeek "Coralogix Raises $200M" (funding); Rapid7 "A Day in the Life of an MDR Analyst" (marketing); BleepingComputer "What 345 Days of Untested Exposure Looks Like at a Bank" (sponsored Sprocket Security); SANS-ISC "Continuing Scans for swagger.json" (commodity scan-pattern observation, not A&D-applicable).
- **Government policy / non-IOC news** (1 item): The Record "DHS chief signals efforts to reshape CISA" (CISA staffing-policy, not threat-intel).
- **Unrelated criminal LE / non-threat-intel** (1 item from FLASH sweep window): BleepingComputer "Police dismantles 9 crime groups in illegal streaming crackdown" (already discarded at FLASH 12:00).

## Source health changes this sweep

None. All previously-healthy sources remain healthy on this sweep. All five stale sources remain stale per their respective entries; no retry due (all under 24h since previous attempt for `msrc` 6-day stale; `ars-security`, `x-cisagov`, `x-gossithedog`, `sophos` are persistent operator-pending).

## Items requiring grader attention (FLASH-adjacent, A&D-watchlist, tracked-actor, tracked-CVE)

- **PM-001 Mirasvit KEV add** is FLASH-adjacent (Trigger 1: critical CVE + active exploitation + A-grade CISA source). NOT raw-signaled as FLASH because the next FLASH sweep is 18:00 EDT (2.5h out) and the KEV add fired during active hours when the grader will see it before the next FLASH window. **3-day due date 2026-06-06** is unusually compressed (KEV norm is 14-21 days) and worth grader attention as a signal of urgency. **Magento-on-DIB-prime exposure question is open** — Magento powers many DIB-prime e-commerce / supplier portals but Mirasvit Cache Warmer adoption among A&D primes is unknown.
- **PM-002 Symantec stock-exchange piece** sat below the 12:00 FLASH bar (single-victim, no A&D entity, no attribution) but is **structurally Tier-1 vendor research worth grading**: Symantec is provisional-A per source-grades.yaml; the IOCs published on security.com are pivot-ready for Splunk hunts; the OneDrive-Personal + Dropbox + hardcoded-Microsoft-IP-bypass-DNS-logging TTPs would be reusable against A&D primes by a similarly state-linked actor. **Unattributed** — grader should preserve "most likely espionage" hedge verbatim per Hard Rule 2.
- **PM-003 Kirki / Burst Statistics WordPress** — CVSS 9.8 + active exploitation but **scope-limited to WordPress sites**; commodity mass-exploitation pattern; below A&D-prime operator-relevance bar in isolation. Grader may downprioritize unless WordPress-on-DIB-prime surface is significant.
- **PM-004 HTTP/2 Bomb update** is update-on AM finding-0003. New technical detail (per-server timing, amplification ratios) is meaningful for defender hardening but doesn't shift the patch-posture matrix from AM brief. Grader will likely roll this into the existing finding rather than promote standalone.
- **PM-005 Microsoft disclosure-policy meta-coverage** is update-on AM watch_signal. The Register's Nightmare-Eclipse + StarLabs explicit-linkage framing is itself NOT a fifth disclosure-policy data point per the AM watch_signal definition; grader should hold the watch_signal at 4 data points (Bitskrieg/Nightmare-Eclipse / Askar VS Code / Windows Search NTLM / StarLabs VS Code-XSS-ineligible). **Watch_signal 5th-data-point clock still running.**
- **No tracked-actor activity** in this window. No UNC1549 / Charming Kitten / Handala Hack / MuddyWater / APT28 / Sandworm / Volt Typhoon / Salt Typhoon / APT29 / APT41 / Lazarus surface. No Gamaredon update (Sekoia "FSB's matryoshka #2/3" / #3/3 still unpublished per AM brief tracking).
- **No A&D-watchlist company hit** in this window. No DIB-prime named victim, no aerospace/defense/CMMC/ITAR/EAR direct surface.
- **No tracked-vuln update on _index.yaml entries** in this window. CVE-2026-45321 KEV deadline 2026-06-10 remains T-7 days; no fresh activity. Other tracked CVEs (PAN-OS CVE-2026-0300, Ivanti CVE-2026-6973, etc.) unchanged.
- **vuln-watch keyword `gogs-argument-injection-2026-05-28` (Jonah Burges / git rebase argument injection)** — no in-window activity. CVE assignment window 2026-06-04_to_2026-06-11 begins tomorrow.

## Splunk first-party check

Targeted query across 18 tracked CVEs + 14 tracked actor names + 4 tracked malware families (TeamPCP, Mini Shai-Hulud, Miasma/ShaiWorm, PCJack) returned **ZERO non-archimedes-internal events over last 24h**. Twelfth-plus consecutive sweep with dormant non-archimedes-internal stream pattern, matches established source-health notes on splunk-archimedes and splunk-defenseclaw.

## Notes for the grader

- The 12:00 FLASH sweep already flagged PM-002 (Symantec stock-exchange) and PM-003 (Kirki WordPress) as "held to next pre-brief for raw-signal capture" — both are honored here.
- **PM-001 Mirasvit** is a fresh KEV add this sweep window (CISA alert published 2026-06-03T12:00 UTC = 08:00 EDT; bleepingcomputer/SecurityWeek/SecurityAffairs relays published 12:08, 13:00, 13:50 UTC).
- The TLP for PM-002 Symantec IOCs should be evaluated carefully — Symantec published the IOCs themselves publicly on security.com (vendor-public), but the framing "if you run endpoint detection for a financial institution, regulator, or anyone else sitting on market-sensitive information" suggests Symantec's intent was distribution-encouraged. TLP:CLEAR likely appropriate; grader's call.
- **The Acer Wave 7 hold** is documented here so the grader has full filter-trail visibility. If the grader wants the Acer dossier as a vuln-watch entry (no CVE-2026-49200/49201 dossier exists), the hold should surface in the analyst's review queue rather than be re-raw-signaled.
