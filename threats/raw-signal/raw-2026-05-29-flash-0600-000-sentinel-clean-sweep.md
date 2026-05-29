---
raw_id: raw-2026-05-29-flash-0600-000-sentinel-clean-sweep
collected_at: 2026-05-29T06:05:00-04:00
run_id: flash-sweep-20260529-060000
collection_mode: flash_sweep
source:
  source_yaml_id: sentinel
  source_name: FLASH 0600 sentinel clean sweep
  source_url: null
  published_at: 2026-05-29T06:05:00-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [sentinel, clean-sweep, flash-0600]
triage_tags: [sentinel, clean_sweep, non_flash]
iocs_extracted: false
iocs_count: 0
text_word_count: 720
promoted: false
ttl_expires_at: 2026-08-27T06:05:00-04:00
---

# FLASH 0600 Sentinel — Clean Sweep, 2026-05-29

Window: 2026-05-29T00:05:00-04:00 (last scheduled FLASH, commit ff2a290 — 0 of 6 triggers) → 2026-05-29T06:05:00-04:00. Quiet hours ACTIVE (06:05 EDT is inside the 21:00–09:00 queue-only window).

## Sources swept (in-window items)

- BleepingComputer RSS — 1 in-window item.
  - "Charter Communications data breach affects 4.9 million accounts" (2026-05-29T04:29 EDT, Sergiu Gatlan). ShinyHunters extortion gang stole 4.9M Charter account records in early-April 2026 hack; surfaced via HaveIBeenPwned. US telecom (residential cable/broadband), NOT A&D sector. ShinyHunters NOT in _roster.yaml. No CVE, no zero-day, no nation-state attribution. Trigger 5 evaluation: single-victim breach disclosure, not a multi-victim active campaign. DISCARDED.
- The Hacker News RSS — 1 in-window item.
  - "Kimsuky Deploys HTTPSpy, Expands Arsenal with HelloDoor and VS Code Tunnels" (2026-05-29T01:57 EDT). DPRK actor Kimsuky (aka Velvet Chollima) campaign March-April 2026 against South Korean military and corporate entities; HTTPSpy variant disguised as nProtect/AhnLab installers, JSONPing infection-verification technique, Rust-based HelloDoor PebbleDash variant (Aug 2025), HttpMalice (Dec 2025), VS Code Remote Tunnel abuse, Cloudflare Quick Tunnels, DWAgent. Primary sources: ENKI (HTTPSpy/JSONPing), Kaspersky (VS Code tunneling + HelloDoor + broader). **Kimsuky NOT in _roster.yaml** — the only DPRK actors tracked are Stardust Chollima (#002, BlueNoroff), Lazarus (#003), APT37 (#024 ScarCruft). Velvet Chollima is Kimsuky, not Charming Kitten (#011 — Iran IRGC-IO). Trigger 2 (new attribution to tracked actor) NO FIRE — Kimsuky not tracked. Trigger 4 (tracked-actor TTP change) NO FIRE — Kimsuky not tracked. Trigger 5 (A&D-sector campaign) evaluation: generic "South Korean military" + 2024 historic "German defense manufacturer" — no A&D prime named, target is not US A&D estate; structural relevance is foreign-state regional military, not directly applicable to operator's ad-prime-v1 profile. NO FIRE. Roster-gap candidate — consider /new-actor proposal for Kimsuky in a future session given recurring activity volume, but does not warrant FLASH this sweep. DISCARDED for FLASH; flag for operator roster review.
- The Record RSS — 0 in-window items.
- SecurityWeek RSS — 0 in-window items (last_modified Thu, 28 May 2026 19:01 GMT = 15:01 EDT, before window).
- Unit 42 (feedburner) — 0 in-window items.
- Mandiant feedburner — 404 (twenty-first consecutive failure, source-health held healthy per operator policy; no alt endpoint).
- MSTIC (Microsoft Security Blog) — 0 in-window items (last_modified 03:06 GMT = pre-window).
- CrowdStrike blog — 10 items returned but ALL with `published: null` (parser-incompatible date schema on this fetch; same as 0000 sweep). Verified the queue is the same set already absorbed: "Disrupting GlassWorm" (finding-2026-05-27-0001 + prior briefs), "May 2026 Patch Tuesday: 30 Critical Among 130 CVEs" (Patch Tuesday absorption complete), CrowdStrike 2026 Financial Services Threat Landscape Report (operator-domain, NOT A&D — financial sector), Gartner MQ Cyberthreat Intel marketing, Falcon AIDR Kubernetes detection, Claude integration. No in-window net-new. DISCARDED.
- Volexity blog — feed parse error continues from 0000 sweep (not well-formed XML at line 17 col 68; second consecutive parse failure). Re-test next sweep; not yet a stale flip. DEFERRED.
- Rapid7 blog — 0 in-window items.
- Krebs on Security — 0 in-window items (last_modified May 25 — well before window).
- SANS ISC — 0 in-window items.
- Cisco Talos blog — 0 in-window items (last_modified Thu 28 May 20:28 GMT = pre-window).
- Security Affairs — 1 in-window item.
  - "BTMOB RAT Gives Criminals a Point-and-Click Kit to Take Over Your Android Phone" (2026-05-29T04:22 EDT, Pierluigi Paganini). ESET researcher Daniel Cunha Barbosa research; commercial Android RAT-as-a-service, $5k lifetime + monthly support, APK builder GUI, abuses Android Accessibility Services, primary distribution Telegram + X/Instagram, observed campaigns in Argentina (AFIP impersonation), Latin America focus. No actor attribution, no nation-state, no A&D sector relevance, no CVE. Commodity criminal tooling. DISCARDED.
- ESET WeLiveSecurity — 0 in-window items.
- SentinelLabs — 0 in-window items (last_modified 07:40 GMT = pre-window).
- Check Point Research — 0 in-window items (last_modified Tue 26 May = pre-window).
- Wiz Research — not re-attempted (404 pattern; pending alt endpoint).
- Socket — not re-attempted (404 pattern; pending alt endpoint).
- GitHub Security Blog — 0 in-window items.
- Sucuri — 0 in-window items.
- Patchstack — not re-attempted (404 pattern).
- Proofpoint — not re-attempted (404 pattern).
- Industrial Cyber — not re-attempted (403 bot-block pattern).
- Dark Reading — 404 on /rss.xml; DEFERRED (consistent pattern from 0000 sweep).

## CISA KEV catalog check

KEV catalog `dateReleased: 2026-05-28T16:27:12.9227Z` (unchanged from 0000 sweep — no republish since). Three KEV entries from dateAdded 2026-05-27 still listed (CVE-2026-48027 Nx Console, CVE-2026-45321 TanStack, CVE-2026-8398 Daemon Tools Lite). All three already absorbed by finding-2026-05-27-0007 + 2026-05-27-afternoon brief. **Zero new dateAdded entries for 2026-05-28 or 2026-05-29.**

KEV due-date watch:
- VT-008 Exchange CVE-2026-42897 federal due 2026-05-29 (T+0, TODAY). MSRC "Exploitation Detected" tag remains single-source — no Mandiant / Volexity / Unit 42 / CrowdStrike corroboration in window. Single-source veto persists; vuln-tracker tracking entry already documents the state.
- VT-006 Mini Shai-Hulud CVE-2026-45321, VT-009 Nx Console CVE-2026-48027 federal due 2026-06-10 (T-12). No state changes in window.
- CVE-2026-8398 Daemon Tools Lite federal due 2026-05-30 (T-1). No state changes in window.

## NVD critical-CVE check

`pubStartDate=2026-05-29T00:00Z pubEndDate=2026-05-29T06:00Z cvssV3Severity=CRITICAL` — 2 results.

- **CVE-2026-8732** — WP Maps Pro plugin for WordPress (≤ 6.1.0). CVSS 9.8 (`AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`). Unauthenticated admin-account creation via unprotected AJAX action with ineffective nonce validation. Reported by Wordfence (security@wordfence.com).
- **CVE-2026-3655** — OTP Login With Phone Number / OTP Verification plugin for WordPress (1.8.50–1.8.60). CVSS 9.8 (`AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`). Authentication bypass — Firebase phone verification fails to validate phone-number-to-target-user binding, enables impersonation of any user including administrators. Reported by Wordfence.

**Trigger 1 evaluation (both):** CVSS ≥ 9.0 PASS. A-grade source (NVD + Wordfence) PASS. **Active exploitation:** NEITHER NVD record carries exploitation language. Both are vendor/security-research coordinated-disclosure class (Wordfence-only, no honeypot/attack-attempt observation). No Sucuri / Patchstack / CISA KEV / IR-firm corroboration. Single-source veto on ITW layer for both. **Trigger 1 does NOT fire for either.** Defer to next scheduled brief for vuln-tracker tracking-list consideration.

**A&D structural exposure:** WordPress plugin = sub-tier-supplier corporate-web-presence layer, not direct A&D-prime ITAR / classified-R&D estate. Same structural posture class as the 0000 sweep's CVE-2026-8809 ACF Extended and the 2026-05-23 LiteSpeed cPanel CVE-2026-48172 — corporate-web layer, structurally-indirect.

## abuse.ch ThreatFox check

ThreatFox recent IOCs (2026-05-28 → 2026-05-29) — botnet_cc / payload_delivery / malware_download filtered for any roster-actor or roster-malware family (SmokeLoader, RedLine, BlackCat, ALPHV, LockBit, Cl0p, AppleSeed, BabyShark, Kimsuky, APT28, Fancy Bear, APT29, APT41, Sandworm, Volt Typhoon, MuddyWater, Charming Kitten, Mint Sandstorm, APT37, ScarCruft, RokRat, BirdCall, Lazarus, BlueNoroff, Tortoiseshell, Imperial Kitten, UNC1549, GlassWorm, Scattered Spider). **Zero matches.** In-window families observed: ClearFake, XMRIG, Cobalt Strike, Nanocore, DanaBot, Remcos, DCRat, Evilginx, AsyncRAT, Mirai, BianLian, ACR Stealer, Vidar, Quasar RAT, VShell, Latrodectus, Joker, Stealc, SnappyClient, Meterpreter. Commodity / generic-criminal mix; nothing tied to tracked actors.

## Splunk first-party

`index=defenseclaw_local OR index=archimedes earliest=-24h@h | stats count by index sourcetype` — 3 sourcetypes:
- archimedes:scheduler — 17 events
- archimedes:operation — 11 events
- archimedes:flash — 2 events

All Archimedes operational telemetry; **zero defenseclaw_local events; zero IOC hits.** Trigger 3 cannot fire. Hard Rule 8: silence is not disconfirming, just absent.

## Anti-noise locks honored

Currently active (would block re-trigger if new content surfaced in window):
- FortiClient EMS CVE-2026-35616 (raw-2026-05-28-flash-1200-001 → finding-2026-05-28-FLASH-1200-0001 B2) — within 24h, lock active. Nothing in window.
- Gogs zero-day RCE (raw-2026-05-28-flash-1200-002 → finding-2026-05-28-FLASH-1200-0002 A2) — within 24h, lock active. Nothing in window.
- MSRC Chaotic Eclipse Defender/BitLocker zero-day pushback (raw-2026-05-28-flash-1200-003) — within 24h, lock active. Nothing in window.
- VT-008 Exchange CVE-2026-42897 — 5-day quiet carry-forward continues; nothing in window.
- VT-006 Mini Shai-Hulud (TanStack) + VT-009 Nx Console — KEV-listed 2026-05-27 absorbed into PM brief; nothing new in window.
- GreyVibe / WithSecure / finding-2026-05-28-0010 — absorbed (BleepingComputer relay already discarded prior sweep).
- All 7 PM 2026-05-28 brief findings + 4 morning findings + 3 FLASH-1200 findings — implicit absorption.

Cleared since 0000 sweep — none (window too short for new lock expirations).

## Trigger evaluation

| Trigger | Condition | Result |
|---|---|---|
| 1 — critical CVE + ITW | CVE-2026-8732 WP Maps Pro (CVSS 9.8) + CVE-2026-3655 OTP Login (CVSS 9.8) both Wordfence-only coordinated-disclosure; no A-grade ITW confirmation | **NO FIRE** |
| 2 — tracked-actor attribution | Kimsuky surfaced in window but Kimsuky NOT in _roster.yaml (DPRK roster = Stardust Chollima, Lazarus, APT37); ShinyHunters surfaced but NOT in roster | **NO FIRE** |
| 3 — first-party IOC hit | Splunk archimedes + defenseclaw_local clean; zero IOC hits in -24h; zero defenseclaw_local events | **NO FIRE** |
| 4 — tracked-actor TTP change | Kimsuky HTTPSpy / HelloDoor / VS Code tunnel evolution would be TTP-change material IF Kimsuky were on roster — it is not | **NO FIRE** |
| 5 — A&D-sector campaign | Kimsuky targets generic South Korean military (not US A&D primes); Charter is US telecom not A&D; no new multi-victim A&D campaign disclosed in window | **NO FIRE** |
| 6 — zero-day no-patch | Gogs (FLASH-1200-002) and FortiClient EMS (FLASH-1200-001) and MSRC Chaotic Eclipse (FLASH-1200-003) already absorbed; no new zero-day disclosures in window | **NO FIRE** |

**Disposition: NO TRIGGERS. Sentinel-only.** Zero FLASH candidates; per FLASH-POLICY anti-noise rules, log clean-sweep and exit silently. Quiet hours active anyway — even if a trigger had fired, post would queue not ship.

## Operator flag — roster gap

Kimsuky surfaced again in this sweep (third or fourth time in recent weeks per memory of feed patterns). The DPRK roster currently covers RGB-attributed (Lazarus, Stardust Chollima) and the post-2026 MSS-attributed APT37 — but Kimsuky is a high-volume, high-tempo DPRK actor (RGB-attributed in most reporting) with recurring South Korean military + Western defense-manufacturer activity. Not a FLASH-this-sweep concern, but the operator may want to consider a `/new-actor Kimsuky` proposal in a future session to close the gap. Flagged for the briefer's coverage log / operator review queue, not handled here.

## Source-health proposed changes

None this sweep.
- Volexity feed parse error — second consecutive (0000 + 0600). If a third consecutive occurs at the 1200 sweep, flip to stale per the 2-failure threshold. For now, monitoring.
- Cisco Talos feedburner — alt endpoint working again this sweep (200, but 0 in-window items). No state change.
- Mandiant feedburner 404 — twenty-first consecutive failure, held healthy per operator policy.
- Wiz / Socket / Patchstack / Proofpoint / Dark Reading 404s — likely require alt endpoints; flag for operator review on next source-health pass.

## Extraction notes

- Language: en
- Article type: sentinel (no in-window flash candidates)
- Raw IOC extraction invoked: no (no in-window items promoted)
