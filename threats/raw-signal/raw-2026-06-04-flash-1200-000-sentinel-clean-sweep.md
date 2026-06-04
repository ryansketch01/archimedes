---
raw_id: raw-2026-06-04-flash-1200-000
collected_at: 2026-06-04T12:05:00-04:00
run_id: flash-sweep-20260604-120000
collection_mode: flash_sweep
sentinel: true
source:
  source_yaml_id: sentinel
  source_name: "FLASH sweep sentinel (clean)"
  source_url: null
  published_at: 2026-06-04T12:00:00-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: []
triage_tags: [flash_clean_sweep, non_flash, active_hours]
iocs_extracted: false
iocs_count: 0
text_word_count: 0
promoted: false
ttl_expires_at: 2026-09-02T12:05:00-04:00
---

# FLASH sweep 2026-06-04 12:00 EDT — clean sweep (0 of 6 triggers fired)

Window: 06:00 EDT 2026-06-04 to 12:00 EDT 2026-06-04 (6h since prior 0600 clean sweep, commit `b7e2e64`). Active-hours window per FLASH-POLICY (09:00-21:00 EDT) — any candidate would post immediately to `#flash-alerts`, no queue. Morning brief 2026-06-04 (commit `7fa731f`) carried Linux cgroups KEV T-1, Mirasvit KEV T-2, Miasma KEV T-6, Bitskrieg June-window watch.

## Triggers evaluated

1. **Critical CVE (CVSS ≥9.0) + active exploitation (A-grade):** none firing. CISA KEV catalog unchanged in window (no new adds; most recent remains CVE-2026-45247 Mirasvit added 2026-06-03 — already carried in AM-04 brief). Cisco Unified CM CVE-2026-20230 disclosed today is critical-SIR with public PoC but **patched at disclosure** and **no active exploitation confirmed**; PoC ≠ ITW per trigger letter. NVD lastModified window-query surfaced no in-window ≥9.0-with-confirmed-ITW entries.
2. **New attribution for tracked actor:** none. JFrog explicitly *declines* attribution on the IronWorm npm worm — "appears to be a custom, carefully built implant from an operation with its own infrastructure" — and notes the operation is distinct from prior Shai-Hulud / TeamPCP lineage. Five Eyes joint alert (item below) names "China's military intelligence services" generically; no specific tracked actor (no APT40/41/Volt/Salt naming). No other actor surfaces in window.
3. **First-party Splunk IOC hit (last 24h):** none. `archimedes` + `defenseclaw_local` indexes carry only Archimedes self-telemetry (`archimedes:operation` 8 events, `archimedes:scheduler` 12 events in last 24h). Zero network/auth telemetry with IOC-matchable content. No tracked-IOC matches possible.
4. **Tracked-actor TTP change (A/B-grade):** none. Mandiant / Unit 42 / CrowdStrike / SentinelLabs / MSTIC / ESET WeLiveSecurity / Sekoia / Securelist all returned zero in-window items. Cisco Talos in-window items are product-marketing class (Threat Hunting launch posts), not threat research with new tracked-actor TTP. No new tooling / targeting / infrastructure attributable to any of the 22 roster actors.
5. **Active A&D-sector nation-state campaign:** none firing under strict trigger letter. Five Eyes "Safeguarding Our Secrets" (item below) is the borderline candidate — A1 multi-victim, China-attributed, active — but is HUMINT-led counterintelligence (not cyber-TTP) and A&D-sector targeting is implicit ("anyone with access to classified or privileged information") not explicit. Defers to PM-04 brief as a counterintelligence-adjacent standing-section note, not a FLASH.
6. **Zero-day without patch (CVSS ≥8.0 or widely deployed) with exploitation confirmed/imminent:** none. Cisco Unified CM CVE-2026-20230 patched at disclosure (not a zero-day). No other in-window disclosures match criteria.

## Notable-but-non-triggering (carry to PM-04 brief queue)

### IronWorm npm self-propagating worm — 36 packages compromised (BleepingComputer / JFrog, 2026-06-04T15:25 UTC = 11:25 EDT)

- **Source:** [BleepingComputer](https://www.bleepingcomputer.com/news/security/new-ironworm-malware-hits-36-packages-in-npm-supply-chain-attack/) (B3 relay) on [JFrog research](https://jfrog.com/blog/) primary (A2 vendor). Secondary verification: Ox Security, Endor Labs, StepSecurity.
- **Mechanism:** Self-propagating npm worm with stolen-credential-driven publishing. Initial compromise via `asteroiddao` account. Shai-Hulud-class by behavior (worm-propagation + npm-ecosystem).
- **Attribution layer:** JFrog *declines* TeamPCP attribution. Quote (per Hard Rule 7): "a custom, carefully built implant from an operation with its own infrastructure" (14 words). Explicit *not-Shai-Hulud-operator* finding — distinct infrastructure.
- **A&D nexus:** Not surfaced. Developers / CI/CD broadly targeted; no industry specificity per JFrog.
- **CVE / KEV:** None assigned. Not on KEV.
- **Why this is NOT a FLASH:** Trigger 4 requires tracked-actor attribution — JFrog declines it. Trigger 5 requires A&D-sector naming — none. The Shai-Hulud-*family* pattern is already tracked (VT-006); a new *operator* in the same class is a corpus signal, not an actionable FLASH-tier change.
- **Handoff to grader:** Promote as a standalone finding for PM-04 brief. Tracks as Shai-Hulud-family fourth instance (after Mini Shai-Hulud / Miasma / Nx Console adjacency). Watch signals: TeamPCP-attribution shift if a second A-grade vendor names them; CVE assignment; KEV listing; A&D-prime customer impact statement on @asteroiddao or downstream packages.

### Five Eyes joint alert "Safeguarding Our Secrets" — Chinese MSS HUMINT recruitment via LinkedIn (FBI/MI5/ASIO/CSIS/NZSIS, 2026-06-04)

- **Source:** [The Record](https://therecord.media/five-eyes-warns-chinese-spies-are-using-job-sites-to-recruit-insiders) (B3 relay) on Five Eyes joint advisory (A1 — five Tier-1 government intelligence services, MI5 named as lead).
- **Mechanism:** Chinese intelligence officers posing as recruiters / consultants on online job platforms (LinkedIn explicitly named) and through front companies described as "private consultancies, think tanks or human resources firms." Virtual interviews, payment for reports. HUMINT-led, not cyber-TTP.
- **Targeting:** "Government and military personnel" and "anyone with access to classified or privileged information." A&D-direct naming is *implicit* — DIB cleared personnel are squarely in scope but A&D contractors, aerospace, defense industrial base are not in the named-target list.
- **Attribution layer:** Five Eyes attributes to "China's military intelligence services" — PLA-attributed but no specific tracked actor in our roster named (Volt Typhoon is PLA-attributed, but the Five Eyes alert does not specify which group). MSS-vs-PLA framing in the alert leans PLA (military intelligence).
- **Why this is NOT a FLASH:** (a) Trigger 5 requires explicit A&D-sector campaign naming and a cyber-TTP component; this is HUMINT-led counterintelligence with implicit A&D-personnel scope. (b) Trigger 2 requires NEW attribution to a *specific tracked actor*; "China's military intelligence services" is sector-generic, not roster-mapped. (c) Trigger 4 requires named tracked-actor + new TTP; same gap.
- **Handoff to grader:** Promote as a counterintelligence-adjacent finding for PM-04 brief. The A1 grade and DIB-cleared-personnel-scope read makes this material for the A&D-target-profile audience even though it is technically out-of-cyber-domain (HUMINT). Suggested digraph A1 procedural / B2 operational read. Action language: cleared-personnel security awareness reminder on unsolicited LinkedIn / virtual-interview / consulting-engagement contacts; A&D corporate security CI partnership reminder. Watch signals: any cyber-TTP overlap (e.g., subsequent malware delivery against recruited insiders); APT40 / APT41 / Volt Typhoon attribution layered on by a Tier-1 IR firm; A&D-prime explicit naming in any follow-on Five Eyes or NCSC release.

### Other in-window items dispositioned non-trigger

- **Cisco Unified CM CVE-2026-20230 critical-SIR + PoC (BleepingComputer, 11:09 EDT).** Patched at disclosure. PoC public but no confirmed ITW. Not Trigger 1 (no ITW), not Trigger 6 (not a zero-day). Watch signals: KEV listing; first-IR-firm-telemetry of exploitation. Carry to PM-04 brief as defensive-prioritization note for Cisco-Unified-CM-deploying estates.
- **The Hacker News — TA4922 China-linked phishing expansion (Proofpoint relay, 12:22 EDT).** TA4922 is a Proofpoint cluster name, NOT in `_roster.yaml`. Cybercrime-class (per Proofpoint framing), not espionage. Targets enterprises in UK/Germany/Italy/South Africa — no A&D-sector specificity. Potential `/new-actor` candidate for operator review; not a FLASH today.
- **The Hacker News — FlutterShell macOS malvertising (Unit 42 relay, 11:19 EDT).** Activity cluster names JSCoreRunner / FileRipple — neither in roster. macOS-targeted commodity backdoor via Google/YouTube ads. No A&D-sector specificity. Not a FLASH.
- **The Hacker News — Claude Code GitHub Action flaw (15:15 EDT).** Published just outside 12:00 EDT window endpoint. Defer to PM-04 sweep. Anthropic-supplier security-research class (Ryotaka @ GMO) — not a roster-actor TTP, not a tracked CVE today. Watch for CVE assignment.
- **CISA ICS-CERT batch (08:00 EDT, 5 advisories).** NAVTOR NavBox 6.3, Hitachi Energy MACH HiDraw 5.5, Hitachi Energy ITT600 Explorer 7.5, B&R PPT30 7.5, Hitachi Energy RTU500 (multi-CVE cluster). NONE meet FLASH threshold (no CVSS ≥9.0, no ITW exploitation, no A&D-watchlist-domain match, no tracked actor). Standard ICS-cadence reporting; not trigger-worthy. RTU500 cluster may merit afternoon-brief energy-sector note if power-utility findings are a standing section.

## Source health

All queried A-grade and B-grade sources responded 200; no health-state changes proposed. Mandiant primary feedburner remains stale-but-held-healthy per operator decision (32nd consecutive 404 on feedburner path; alt-endpoint `mandiant.com/resources/blog/rss.xml` continues validating at 200 with 0 in-window items today — same pattern as prior 31 sweeps). Volexity RSS continues parse-failing (not well-formed at line 17 col 68) — known longstanding issue, not a new degradation. ThreatFox browse interface gated behind CAPTCHA on WebFetch path; abuse.ch MCP not yet built (operator action item per prior source-health notes).

Stale-source skips (per source-health.yaml, preserved verbatim): `msrc` (parse failure since 2026-05-30), `dragos` (404 since 2026-05-13 — pending operator RSS-path identification), and the standing no-MCP/no-key set (`censys`, `urlscan`, `hibp`, abuse.ch family).

Sources queried (16, in-window evaluations): CISA all.xml RSS (5 in-window ICS items, all sub-threshold), CISA KEV JSON (0 in-window adds), Microsoft Security Blog RSS (0 in-window), Unit 42 feedburner (0 in-window), Mandiant alt-endpoint (0 in-window), Cisco Talos RSS (2 in-window items, product-marketing class, non-threat-intel), SentinelLabs RSS (0 in-window), ESET WeLiveSecurity RSS (0 in-window), Volexity RSS (parse-fail, no items), Sekoia blog RSS (0 in-window), Securelist RSS (0 in-window), BleepingComputer RSS (5 in-window, 2 evaluated above), The Hacker News feedburner (4 in-window, 3 evaluated above + 1 deferred), The Record RSS (4 in-window, 1 evaluated above + 3 informational), Splunk archimedes + defenseclaw_local indexes (0 IOC-matching events in last 24h), CISA cybersecurity-advisories landing page (403 — known WAF behavior; all.xml RSS is productive endpoint, already queried).

## Disposition

Clean sweep. 0 of 6 triggers fired. No FLASH posting. Two notable-but-non-triggering items (IronWorm npm worm + Five Eyes Chinese HUMINT recruitment alert) handed off to grader for PM-04 brief consideration via standard non-FLASH promotion path. Orchestrator: log `flash_sweep_clean`, exit silently per FLASH-POLICY anti-noise rules.
