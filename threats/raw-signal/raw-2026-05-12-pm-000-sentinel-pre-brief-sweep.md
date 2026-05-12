---
raw_id: raw-2026-05-12-pm-000
collected_at: 2026-05-12T15:32:00-04:00
run_id: pre-brief-20260512-153000
collection_mode: pre_brief_collection
sweep_type: pre_brief
sweep_time: 2026-05-12T15:30:00-04:00
time_window_start: 2026-05-12T07:30:00-04:00      # backstop reach to morning-brief boundary for source-cadence resilience; primary candidate window 12:00 → 15:30 EDT (3.5h since 12:00 FLASH clean)
time_window_end: 2026-05-12T15:30:00-04:00
test: false
sources_queried:
  - cisa-advisories        # all.xml RSS via fetch_feed — status 200, 30 items in feed total, 7 items in 8h backstop window (all dated 2026-05-12T12:00 UTC = 08:00 EDT). PRODUCTIVE — fresh CISA ICS batch dropped just after this morning's 07:30 sweep boundary (ABB AC500 V3 Stack Buffer Overflow CVSS 9.8 OOBW = CVE-2025-15467; ABB AC500 V3 Multiple Vulnerabilities CVSS 8.3 = CVE-2025-2595 + CVE-2025-41659 + CVE-2025-41691; ABB WebPro SNMP Card PowerValue CVSS 8.8; ABB Automation Builder Gateway for Windows CVSS 5.3 = CVE-2024-41975; Subnet Solutions PowerSYSTEM Center CVSS 8.2 = CVE-2026-26289 + CVE-2026-33570 + CVE-2026-35504 + CVE-2026-35555; Fuji Electric Tellus CVSS 7.8 = CVE-2026-8108; SBOM for AI Minimum Elements policy guidance NOT threat-intel — last item DISCARDED). RAW-SIGNALED as PM-004 (ICS cluster via structural critical-infrastructure / defense-manufacturing relevance precedent same as Siemens RUGGEDCOM ROX cluster in raw-2026-05-12-am-002).
  - cisa-kev               # JSON catalog via WebFetch — top 10 most recent entries returned. ZERO entries dateAdded >= 2026-05-11 (full-catalog scan corroborates 00:00 + 06:00 + 07:30 sweeps across the day). Most recent KEV addition remains CVE-2026-42208 (BerriAI LiteLLM, dateAdded 2026-05-08). Three deadlines = TODAY EOB (CVE-2024-1708 ConnectWise ScreenConnect dueDate 2026-05-12 EOB; CVE-2026-32202 Microsoft Windows dueDate 2026-05-12 EOB); CVE-2026-31431 Linux Kernel dueDate 2026-05-15 = T+3d. KEV catalog does not publish compliance-status changes against passed deadlines.
  - nvd                    # WebFetch on services.nvd.nist.gov lastModStartDate 2026-05-12T07:30:00-04:00 → 15:30:00-04:00. cvssV3Severity=CRITICAL → 40 results: 11 are fresh disclosures (CVE-2026-27446 Apache Artemis 9.8 auth bypass; CVE-2026-31789 OpenSSL OCTET STRING 32-bit 9.8 — patched 2026-04-07; CVE-2026-5963/5964 Digiwin EasyFlow .NET SQLi 9.3/9.8; CVE-2026-0300 PAN-OS already in KEV; CVE-2026-41509 CROSS post-quantum signature 9.8; CVE-2025-14179 PHP PDO Firebird NUL-byte SQLi 9.8; CVE-2026-6722/7261 PHP SOAP UAF 9.8 dual; CVE-2026-6104 PHP encoding-names NUL OOB-read 9.1; CVE-2021-47923 OpenCart session-fixation 9.3 deferred); remaining 29 are older-CVE NVD metadata refreshes (CVE-2024-37371 MIT Kerberos, CVE-2024-3596 FreeRADIUS RADIUS/UDP forgery, CVE-2024-45491/45492 libexpat 32-bit integer overflow, CVE-2024-47685 Linux kernel netfilter, plus 24 others 2019-2024 vintage). cvssV3Severity=HIGH → returned CVE-2023-4911 GLIBC ld.so GLIBC_TUNABLES + CVE-2023-44487 HTTP/2 Rapid Reset (analyzed-status NOT modified-status; not metadata refreshes — older analyzed entries surfacing in lastModStartDate via catalog-wide re-touch). NONE of the fresh Criticals match A&D / tracked-actor / tracked-vuln filter set (PHP runtime / Apache Artemis JMS / PAN-OS already covered / OpenSSL 32-bit patched April / Digiwin EasyFlow / OpenCart / CROSS post-quantum reference impl) — ALL DISCARDED per Mode 1 procedure (no watchlist / roster / vuln-index hit). Microsoft May Patch Tuesday CVEs (120 Windows-only + 17 Edge/Chromium = 137 total per SecurityWeek) NOT yet visible in NVD lastModStartDate window — typical 24-48h NVD lag from MSRC publication; will surface in tomorrow's morning-sweep NVD window. NVD endpoint remains healthy and responsive.
  - bleepingcomputer       # RSS via fetch_feed — status 200, etag 293bfce8e22a318fc7589450b80fc9b3, last_modified 2026-05-12T19:30:09 GMT (15:30 EDT in-window from feed-server activity), 6 items in 8h backstop window. (1) "Microsoft releases Windows 10 KB5087544 extended security update" (Lawrence Abrams, 18:58 UTC = 14:58 EDT in-window) — Windows 10 ESU patch announcement, RELATED to MS May Patch Tuesday but secondary detail, NOT independently raw-signaled (covered structurally via PM-001). (2) "Fortinet warns of critical RCE flaws in FortiSandbox and FortiAuthenticator" (Sergiu Gatlan, 18:23 UTC = 14:23 EDT in-window) — Critical CVE-2026-26083 FortiSandbox missing authorization unauthenticated GUI + critical CVE-2026-44277 FortiAuthenticator improper access control unauthenticated code execution; no ITW exploitation reported; A&D-relevant via Fortinet security-appliance deployment at prime perimeters + MFA infrastructure. RAW-SIGNALED as PM-002. (3) "Windows 11 KB5089549 & KB5087420 cumulative updates released" (Mayank Parmar, 18:09 UTC) — detail patch announcement, covered structurally via PM-001. (4) "Microsoft May 2026 Patch Tuesday fixes 120 flaws, no zero-days" (Lawrence Abrams, 18:08 UTC = 14:08 EDT in-window) — Windows-only count; RAW-SIGNALED as PM-001 (covers full MS Patch Tuesday picture cross-referenced with SecurityWeek 137-CVE total count). (5) "Škoda warns of customer data breach after online shop hack" (Sergiu Gatlan, 17:07 UTC) — Volkswagen Group automotive subsidiary breach; NO threat actor, NO A&D content, NO IOCs. DISCARDED per Mode 1 procedure (no watchlist / roster / vuln-index hit). (6) "Android 17 to expand banking scam call and privacy protections" (Bill Toulas, 17:00 UTC) — consumer Android feature announcement; DISCARDED per Mode 1.
  - securityweek           # RSS via fetch_feed — status 200, etag W/9e663313c186e59c7d502aec990a4b61, last_modified 2026-05-12T18:07:44 GMT (14:07 EDT in-window from feed-server activity), 10 items in 8h backstop window. (1) "Microsoft Patches 137 Vulnerabilities" (Ionut Arghire, 18:07 UTC) — 137-CVE total count (120 Windows + 17 Edge/Chromium cumulative); cross-references PM-001 (no zero-days, no ITW). (2) "Exaforce Raises $125 Million for Agentic SOC Platform" (17:23 UTC) — venture-funding editorial, DISCARDED per Mode 1. (3) "Adobe Patches 52 Vulnerabilities in 10 Products" (Ionut Arghire, 16:47 UTC) — Adobe Tuesday patch batch; "none of the flaws have been exploited in the wild"; DISCARDED per Mode 1 (no exploitation, no A&D, no tracked actor — structural-relevance threshold not met for the watchlist test). (4) "White Circle Raises $11 Million for AI Control Platform" (15:40 UTC) — venture-funding, DISCARDED. (5) "BWH Hotels Says Hackers Had Access to Reservation Data for 6 Months" (14:30 UTC) — hospitality breach, no A&D, DISCARDED. (6) "Free OnlyFans Lure Used to Spread Cross-Platform CRPx0 Malware" (Kevin Townsend, 13:46 UTC) — consumer-targeted social-engineering malware; no A&D, no tracked-actor; DISCARDED per Mode 1. (7) "Deal Reached With Hackers to Delete Data Stolen From the Canvas Educational Platform" (AP, 13:26 UTC) — Instructure ransom settlement; edtech; DISCARDED per Mode 1 (ANTI-NOISE — Instructure already covered in 06:00 FLASH sentinel sweep). (8) "West Pharmaceutical Services Hit by Disruptive Ransomware Attack" (Ionut Arghire, 12:59 UTC) — pharma ransomware; no A&D; DISCARDED per Mode 1. (9) "Apple Patches Dozens of Vulnerabilities in macOS, iOS" (Eduard Kovacs, 12:37 UTC) — Apple May patches; no ITW zero-days called out; DISCARDED per Mode 1 (no tracked-actor, no A&D specifically, ANTI-NOISE with iOS 26.5 already discarded at 06:00 FLASH). (10) "SAP Patches Critical S/4HANA, Commerce Vulnerabilities" (Ionut Arghire, 12:13 UTC) — ANTI-NOISE applies (SAP May 2026 Patch Day already raw-signaled at AM-001 + finding-2026-05-12-0001 + 08:00 morning brief coverage).
  - mstic                  # RSS via fetch_feed (microsoft.com/en-us/security/blog/feed/) — status 200, etag "0e8349dba8a786a9e848a821ce2864be-gzip", last_modified 2026-05-12T17:51:55 GMT (13:51 EDT in-window from feed-server activity), 2 items in 8h backstop window. (1) "Defending consumer web properties against modern DDoS attacks" (Kumar Srinivasamurthy, 2026-05-12T16:00 UTC = 12:00 EDT in-window) — defensive editorial on DDoS-defense-in-depth architecture; no fresh threat-actor naming, no IOCs, no fresh CVEs, no A&D specifically (consumer-web-property framing); DISCARDED per Mode 1 procedure (no watchlist / roster / vuln-index hit beyond generic "DDoS uptick across Bing"). (2) "Undermining the trust boundary: Investigating a stealthy intrusion through third-party compromise" (Microsoft Incident Response, 2026-05-12T15:00 UTC = 11:00 EDT in-window) — MSTIC A-grade source; FRESH Microsoft IR case study; HPE Operations Agent legitimate enterprise tool abused via compromised third-party IT services provider; IOCs published (8 files, 2 paths, 1 redacted domain); 1 MITRE technique cited (T1199 Trusted Relationship); no actor attribution; victim sector NOT disclosed. RAW-SIGNALED as PM-003 (supply-chain / managed-service-provider intrusion pattern structurally relevant to A&D primes who outsource IT management).
  - unit42                 # RSS (feedburner) via fetch_feed — status 200, last_modified 2026-05-11T22:51:12 GMT pre-window unchanged, 0 items in 8h window. The 2026-05-11 18:00 EDT AD CS Escalation piece (Fighting Ursa = APT28 alias) remains the most recent post; covered + discarded at 00:00 FLASH sentinel.
  - sans-isc               # RSS via fetch_feed (rssfeed.xml) — status 200, etag W/1e43-651a3e04b9b0e, last_modified 2026-05-12T19:29:04 GMT (15:29 EDT in-window from feed-server activity), 1 item in 8h window — "Microsoft May 2026 Patch Tuesday, (Tue, May 12th)" (no author, 18:29 UTC = 14:29 EDT in-window). 137-CVE diary note. ANTI-NOISE — same MS Patch Tuesday topic raw-signaled at PM-001 via BleepingComputer + SecurityWeek primaries; SANS ISC diary is short-form awareness restatement.
  - rapid7                 # RSS via fetch_feed (rapid7.com/blog/rss/) — status 200, last_modified 2026-05-12T19:16:38 GMT (15:16 EDT in-window from feed-server activity), 1 item in 8h window — "How Rapid7 is bringing Cyber GRC closer to security operations" (Sabeen Malik, 13:17 UTC = 09:17 EDT in-window). Vendor-product editorial (GRC + SecOps integration); no threats, no actors, no CVEs, no IOCs. DISCARDED per Mode 1 procedure.
  - crowdstrike            # RSS via fetch_feed — status 200, 10 items returned ALL with null published_at (EIGHTEENTH consecutive sweep with dateless marketing pattern across 10+ days). Same pile (Automated Leads AI threat detection, Gartner MQ leader, Falcon OverWatch for Defender, Technical Risk Assessments, AI Vuln Discovery podcast, CORDIAL/SNARKY SPIDER product-marketing, ChatGPT Enterprise audit logging, Frost & Sullivan CNAPP, Google Cloud detection expansion, Falcon Cloud Security ROI). Pattern fully entrenched.
  - sentinelone-labs       # RSS via fetch_feed (sentinelone.com/labs/feed/) — status 200, etag W/490b65c5d9486ce4cef110346cf0932b, last_modified 2026-05-12T19:29:38 GMT (15:29 EDT in-window from feed-server activity but no fresh body), 0 items in 8h window.
  - sophos                 # RSS via fetch_feed (news.sophos.com/feed/) — status 200, last_modified 2026-05-12T17:59:45 GMT (13:59 EDT in-window from feed-server activity but no fresh body), 9 items total in feed, 0 items in 8h window.
  - eset-welivesecurity    # RSS via fetch_feed — status 200, 100 items total in feed, 0 items in 8h window.
  - krebs                  # RSS via fetch_feed — status 200, last_modified 2026-05-12T02:20:41 GMT pre-window unchanged across the day, 0 items in 8h window. Normal Krebs cadence.
  - the-record             # RSS via fetch_feed — status 200, 5 items total in feed, 3 items in 8h backstop window. (1) "West Pharmaceutical warns of ransomware attack impacting business operations" (2026-05-12T19:00 UTC = 15:00 EDT in-window) — ANTI-NOISE (SecurityWeek primary already DISCARDED above; pharma not A&D). (2) "European countries are exporting surveillance tech to countries with poor human rights records, report says" (16:49 UTC = 12:49 EDT in-window) — HRW policy/advocacy report on EU surveillance-tech export controls; policy/governance content; no threats, no actors, no IOCs, no A&D specific. DISCARDED per Mode 1 procedure. (3) "Instructure pays ransom after Canvas incident as Congress announces investigation" (13:01 UTC = 09:01 EDT in-window) — Instructure ransom + congressional-investigation announcement; ANTI-NOISE (already covered at 06:00 FLASH sentinel sweep and 07:30 morning-brief filter trail).
  - hacker-news            # WebFetch on thehackernews.com/ index — 12 most recent articles listed. Two 2026-05-12-dated items NEW vs. 07:30 sweep: (a) "New Exim BDAT Vulnerability Exposes GnuTLS Builds to Potential Code Execution" — CVE-2026-45185 ("Dead.Letter") use-after-free in BDAT command handling on USE_GNUTLS=yes builds only (versions 4.97-4.99.2); patched 4.99.3; disclosed 2026-05-01; researcher Federico Kirschbaum / XBOW Security Lab; NO active exploitation reported; NO threat-actor attribution; NO A&D specific; narrow deployment scope (USE_GNUTLS-only builds, not OpenSSL builds). DISCARDED per Mode 1 procedure (no watchlist / roster / vuln-index hit; FLASH Trigger 1 fails on no-ITW + no-A-grade-exploitation-claim; FLASH Trigger 6 fails on patched-at-disclosure 12 days ago). (b) "RubyGems Suspends New Signups After Hundreds of Malicious Packages Are Uploaded" — Mend.io surfaced "hundreds" of malicious RubyGems packages; RubyGems team disabled new signups; "It's currently not known who is behind the attack" per article; NO IOCs published yet (Mend.io will release more details once contained); NO confirmed connection to TeamPCP / Mini Shai-Hulud worm covered today (separate ecosystem RubyGems vs npm+PyPI); NO A&D-prime targeting cited. Supply-chain attack PATTERN-ADJACENT but operationally distinct. DISCARDED per Mode 1 procedure (no IOCs, no actor, no A&D specific — Mode 1 requires watchlist / roster / vuln-index hit). Flagged for orchestrator awareness as potential 2026-05-13 morning-brief candidate once Mend.io publishes IOC layer. (c) "New TrickMo Variant Uses TON C2 and SOCKS5 to Create Android Network Pivots" — ThreatFabric analysis; Android banking trojan with TON-blockchain proxy C2 + .adnl resolution; targeting France/Italy/Austria banking + crypto wallets; package-name + dropper-hash IOCs published; NO tracked-actor attribution; NO A&D specific; consumer-banking targeting scope. DISCARDED per Mode 1 procedure (no watchlist / roster / vuln-index hit; consumer-financial targeting outside A&D-prime scope). Remaining 9 items pre-window or anti-noise-applies (Mini Shai-Hulud relay, Instructure ransom relay, OpenAI Daybreak product, iOS 26.5 consumer, Salesforce Aura sponsored pen-test, Agentic AI Blind Spot editorial, OAuth Review Checklist sponsored, SOC Alerts webinar, Checkmarx Jenkins anti-noise to 2026-05-11 raw-signal).
  - cloud-google-blog-mandiant  # WebFetch on cloud.google.com/blog/topics/threat-intelligence top page — top-8 visible titles unchanged from 2026-05-11 + 2026-05-12 morning sweeps (GTIG AI Threat Tracker, UNC6692 Snow Flurries, deSouza AI vuln post, German Cyber Überfall, BRICKSTORM Defender's Guide, UNC1069 Axios NPM, M-Trends 2026, DarkSword iOS). NO fresh GTIG content this 8h window. Mandiant feedburner endpoint /Mandiant continues 404 (EIGHTEENTH consecutive); failure_count 16 → 17. UNC6692 + UNC1069 remain NOT in _roster.yaml — operator /new-actor candidates pending.
  - fortinet-psirt         # WebFetch on fortiguard.fortinet.com/psirt index — confirmed 2026-05-12 PSIRT publication of FG-IR-26-136 (CVE-2026-26083 FortiSandbox Critical missing-authorization unauthenticated GUI access; affects FortiSandbox 5.0/4.4, Cloud 24/23/5.0, PaaS 23.4/23.3/23.1/22.2/22.1) plus FG-IR-26-123 (CVE-2025-53844 FortiOS High OOB-write in CAPWAP daemon authenticated; FortiOS 7.6/7.4/7.2), FG-IR-26-131 (CVE-2025-53680 FortiAP Medium command-injection authenticated), FG-IR-26-133 (CVE-2025-53870 FortiAP Medium OS command-injection authenticated). Direct fetch on FG-IR-26-136 detail page returned ECONNREFUSED — index-page summary captured at appliance/version level only; CVSS scores not exposed via index-page summary (BleepingComputer relay PM-002 captured CVE-2026-44277 FortiAuthenticator improper-access-control unauthenticated code-execution patched in 6.5.7 / 6.6.9 / 8.0.3 cross-corroboration but specific PSIRT-FG-IR identifier for FortiAuthenticator not exposed in this index sweep). Fortinet PSIRT advisory page is FIRST Archimedes-corpus surface for direct vendor fetch; source-grade-log candidate at provisional A (vendor official advisory; analog to siemens-productcert raw-2026-05-12-am-002 first-surface treatment).
  - splunk-archimedes      # search NOT sourcetype=archimedes:* over 8h returned zero events; same over 24h zero events. Targeted IOC keyword sweep across 25+ high-priority tokens (15 tracked actor aliases including ShinyHunters via Canvas, Mini Shai-Hulud, plus this-sweep CVE-2026-26083 / CVE-2026-44277 / CVE-2026-41096 / CVE-2026-40365 / CVE-2026-45185 / CVE-2026-45321 / CVE-2025-15467 ABB AC500 / FortiSandbox / FortiAuthenticator) over 24h returned 8 hits — ALL eight are archimedes:operation pipeline self-references from today's 06:00 FLASH + 08:00 morning brief commit cycles (raw_signal_written for FLASH-0600-001, finding_promoted for FLASH-0001, brief_composed for flash-2026-05-12-0600, flash_queued, brief_published for morning at 08:19 EDT, flash_queue_superseded by morning at 08:19 EDT, git_committed for flash-0600 commit hash 7af358c, git_committed for morning brief commit hash 733b5ee). Pipeline self-references match keyword tokens in JSON payloads (related_vulns includes CVE-2026-45321/34263/34260/41551/2025-40949/22924/25786/25787 in morning brief_published payload; related_actor 001 TeamPCP) but reflect Archimedes' own operational logging, NOT external observations. The Mini Shai-Hulud IOCs (filev2.getsession[.]org, api.masscan[.]cloud, git-tanstack.com, 83.142.209[.]194, three SHA-256 file hashes) and the today-new MSTIC PM-003 IOCs (abc003.vbs, Errors.aspx, Signoff.aspx, ghost.inc, mslogon.dll, passms.dll, msupdate.dll) and the Fortinet PM-002 affected-version strings all specifically tested — zero matches. Splunk first-party remains structurally dormant for non-archimedes-internal events.
  - splunk-defenseclaw     # NOT sourcetype=archimedes:* over 8h returns zero events; over 24h also zero. EIGHTEENTH consecutive sweep with dormant non-archimedes-internal stream pattern across both indexes.
sources_skipped_stale:
  - censys                 # MCP not built (deferred to Session 11+)
  - urlscan                # MCP not built (deferred to Session 11+)
  - hibp                   # No API key configured (HIBP_API_KEY missing from .env)
  - x-cisagov              # STALE since 2026-05-10 12:00 FLASH — three consecutive WinError 10060 nitter.net timeouts. ~51h since stale-flip = eligible-to-retry per 24h rule; not invoked this sweep — pre-brief scope priority kept on RSS / vendor / NVD / CISA / Microsoft / Fortinet / Hacker News. Operator nitter-pool / direct-X-API decision still pending.
  - x-gossithedog          # STALE since 2026-05-09 — nitter.net account permanently delisted. ~3+ days since stale flip; treating as effectively stale until operator nitter-pool decision.
  - ars-security           # STALE since 2026-05-09 — feeds.arstechnica.com/arstechnica/security 404. Workaround in use (arstechnica.com/feed/ root path); root path not invoked this sweep — pre-brief scope priority kept on higher-signal feeds.
sources_skipped_softfail_this_sweep:
  - threatfox              # CAPTCHA wall via WebFetch (auth-injection limitation); awaiting MCP build priority
  - malwarebazaar          # awaiting MCP build priority
  - github-advisories      # 406 Not Acceptable on global advisories.atom; per-repo GHSA fallback path remains productive workaround when triggered (not triggered this sweep)
  - proofpoint             # /us/threat-insight/blog/feed endpoint 404 since 2026-05-10 12:00 FLASH; alt /us/rss.xml corporate-news endpoint multi-day cadence; not invoked this sweep
  - iran-monitor           # iranmonitor.org 403 WAF/UA workaround pending
sources_health_changed_this_sweep:
  - mandiant               # feedburner.com/Mandiant continues 404 (EIGHTEENTH consecutive); failure_count 16→17. cloud.google.com index page WebFetch surfaced same top-8 visible titles as 2026-05-11 + 2026-05-12 morning sweeps (all out-of-window per prior triangulations). Held healthy pending operator alt-endpoint decision.
  - bleepingcomputer       # last_successful_fetch 2026-05-12T07:30 → 15:30; 6 in-window items, 2 raw-signaled (MS Patch Tuesday = PM-001 + Fortinet RCEs = PM-002), 4 discarded (Win 10 ESU detail patch announcement / Win 11 KB detail patch announcement covered structurally via PM-001; Škoda automotive consumer breach; Android 17 consumer feature) — one of the most productive single-feed sweeps of the day.
  - securityweek           # last_successful_fetch 2026-05-12T07:30 → 15:30; 10 in-window items, 0 raw-signaled (1 anti-noise to PM-001 cross-corroboration MS PT 137-CVE total; 9 discarded incl. anti-noise SAP relay to AM-001; pharma West Pharma; edtech Instructure anti-noise; hospitality BWH; consumer CRPx0; consumer Adobe-no-ITW; venture-funding Exaforce + White Circle; consumer Apple anti-noise).
  - krebs                  # last_successful_fetch 2026-05-12T07:30 → 15:30; 0 in-window items, normal cadence.
  - mstic                  # last_successful_fetch 2026-05-12T07:30 → 15:30; 2 in-window items, 1 raw-signaled (Undermining the Trust Boundary = PM-003; the DDoS-defense editorial discarded as defensive-content non-threat-intel). Productive afternoon — MSTIC IR case studies are A-grade primary research with first-party Microsoft Defender telemetry visibility.
  - unit42                 # last_successful_fetch 2026-05-12T07:30 → 15:30; 0 in-window items.
  - rapid7                 # last_successful_fetch 2026-05-12T07:30 → 15:30; 1 in-window item (Cyber GRC editorial) — DISCARDED (vendor-product editorial, no threats).
  - hacker-news            # last_successful_fetch 2026-05-12T07:30 → 15:30; 3 new in-window items, 0 raw-signaled (1 Exim CVE-2026-45185 BDAT/GnuTLS — discarded narrow USE_GNUTLS-only deployment scope + no ITW + patched 2026-05-01; 1 RubyGems suspends signups — discarded NO IOCs yet, NO actor, NO A&D, flagged for 2026-05-13 morning-brief candidate once Mend.io publishes; 1 TrickMo TON C2 Android — discarded consumer-banking targeting outside A&D scope).
  - sentinelone            # last_successful_fetch 2026-05-12T07:30 → 15:30; 0 in-window items.
  - sophos                 # last_successful_fetch 2026-05-12T07:30 → 15:30; 0 in-window items.
  - cisa-advisories        # last_successful_fetch 2026-05-12T07:30 → 15:30; 7 in-window items (ICS batch dropped at 12:00 UTC = 08:00 EDT just after morning-sweep boundary), 1 raw-signaled (ICS cluster = PM-004 covering 6 advisories minus the SBOM-for-AI policy guidance which is non-threat-intel).
  - cisa-kev               # last_successful_fetch 2026-05-12T07:30 → 15:30; zero entries dateAdded >= 2026-05-11 (corroborates the full day's KEV-quiet pattern).
  - nvd                    # last_successful_fetch 2026-05-12T07:30 → 15:30; NVD lastModStartDate window-query surfaced 11 fresh Criticals + 29 metadata refreshes + 2 HIGH older-analyzed entries. ALL DISCARDED per Mode 1 (no A&D / no tracked-actor / no tracked-vuln match). Microsoft May Patch Tuesday CVEs typical 24-48h lag NOT yet in NVD lastModStartDate; will surface 2026-05-13 morning sweep.
  - the-record             # last_successful_fetch 2026-05-12T07:30 → 15:30; 3 in-window items (West Pharma anti-noise; HRW EU surveillance export advocacy report; Instructure anti-noise) — 0 raw-signaled.
  - sans-isc               # last_successful_fetch 2026-05-12T07:30 → 15:30; 1 in-window item (MS Patch Tuesday short diary) — anti-noise to PM-001.
  - fortinet-psirt         # FIRST Archimedes-corpus surface for direct vendor fetch — added to source-health.yaml as healthy with provisional A source-grade-log candidate (analog to siemens-productcert first-surface 2026-05-12 morning treatment). Index page returned summary listing of FG-IR-26-* advisories for 2026-05-12 batch including the FortiSandbox + FortiOS + FortiAP cluster; direct fetch on FG-IR-26-136 detail page returned ECONNREFUSED (intermittent server-side issue; not a workflow-blocking failure since BleepingComputer relay PM-002 captured the FortiAuthenticator + FortiSandbox CVE pair end-to-end). Held healthy pending re-test on next sweep.
match_reason:
  watchlist: []                          # PM-001 + PM-002 + PM-003 + PM-004 are structural A&D-relevance signals, not direct-prime-watchlist hits
  watchlist_match_strength: structural_via_ms_windows_+_fortinet_+_msp_supply_chain_+_abb_ics_deployment_across_ad_primes
  actors: []                             # PM-001 + PM-002 + PM-003 + PM-004 are NO-actor-attribution material; flagged here for grader-queue clarity
  vulnerabilities:
    - CVE-2026-26083                     # FortiSandbox missing-authorization unauthenticated GUI access (Critical, no ITW)
    - CVE-2026-44277                     # FortiAuthenticator improper-access-control unauthenticated code-execution (Critical, no ITW)
    - CVE-2026-41096                     # Windows DNS Client RCE (Critical, no ITW; most operationally significant per BleepingComputer analysis)
    - CVE-2026-40364                     # Microsoft Word RCE type-confusion CVSS 8.4 (High, no ITW, preview-pane-exploitable per SecurityWeek)
    - CVE-2026-40361                     # Microsoft Word RCE use-after-free CVSS 8.4 (High, no ITW)
    - CVE-2026-40365                     # SharePoint Server RCE (Critical, no ITW; authenticated)
    - CVE-2026-41089                     # Windows Netlogon RCE (Critical, no ITW)
    - CVE-2026-41103                     # Microsoft SSO Plugin for Jira & Confluence elevation (Critical, no ITW)
    - CVE-2025-15467                     # ABB AC500 V3 Stack Buffer Overflow OOB-write CVSS 9.8 (Critical, no ITW; critical-infrastructure deployment)
    - CVE-2025-2595                      # ABB AC500 V3 forced-browsing
    - CVE-2025-41659                     # ABB AC500 V3 incorrect-permission
    - CVE-2025-41691                     # ABB AC500 V3 null-pointer-deref DoS
    - CVE-2026-26289                     # Subnet Solutions PowerSYSTEM Center
    - CVE-2026-33570                     # Subnet Solutions PowerSYSTEM Center
    - CVE-2026-35504                     # Subnet Solutions PowerSYSTEM Center
    - CVE-2026-35555                     # Subnet Solutions PowerSYSTEM Center
    - CVE-2026-8108                      # Fuji Electric Tellus exposed-dangerous-method
  keywords:
    - patch-tuesday-may-2026-no-zero-days
    - fortinet-criticals-no-itw
    - msp-third-party-compromise-t1199
    - cisa-ics-batch-2026-05-12
    - structural-ad-relevance
triage_tags:
  - sentinel
  - pre_brief_pm_2026_05_12
  - active_hours
  - microsoft_patch_tuesday_may_2026_no_zero_days_no_itw
  - fortinet_fortisandbox_fortiauthenticator_criticals_no_itw_structural_ad
  - mstic_undermining_trust_boundary_msp_supply_chain_t1199_no_attribution
  - cisa_ics_batch_seven_advisories_abb_subnet_fuji_published_post_morning_sweep
  - mandiant_feedburner_18th_consecutive_404
  - splunk_dormant_18th_consecutive
  - fortinet_psirt_first_corpus_surface_provisional_a_grade_candidate
  - rubygems_signups_suspended_no_iocs_flagged_for_tomorrow_morning_brief
  - exim_cve_2026_45185_narrow_use_gnutls_scope_no_itw_discarded
  - trickmo_ton_c2_android_consumer_banking_eu_discarded
  - apple_may_patches_anti_noise_to_06_00_flash
  - adobe_52_vulns_no_itw_discarded
  - west_pharma_ransomware_pharma_discarded
  - instructure_ransom_canvas_anti_noise
  - skoda_automotive_breach_consumer_discarded
  - bwh_hotels_hospitality_discarded
  - crpx0_onlyfans_lure_consumer_discarded
  - sap_patch_day_anti_noise_to_am_001
  - siemens_patch_tuesday_anti_noise_to_am_002
  - mini_shai_hulud_anti_noise_to_flash_0001
flash_triggers_evaluated:
  trigger_1_critical_cve_exploited:
    matched: false
    notes: |
      Microsoft Patch Tuesday May 2026 has CRITICAL CVEs (CVE-2026-41096
      DNS Client RCE, CVE-2026-40365 SharePoint RCE, CVE-2026-41089
      Netlogon RCE, CVE-2026-41103 SSO Plugin elevation, plus seven
      additional Office/Word Criticals) but NO reported ITW exploitation
      per both BleepingComputer Lawrence Abrams and SecurityWeek Ionut
      Arghire primaries — "no zero-days disclosed this month" + "none
      of which have been flagged as exploited in the wild" — Trigger 1
      FAIL on the strict conjunction (CVSS≥9.0 ✓ for several;
      active_exploitation ✗; source_grade A ✓). Same conclusion for
      Fortinet CVE-2026-26083 + CVE-2026-44277 (Critical, no ITW per
      BleepingComputer relay). Same conclusion for ABB AC500 V3
      CVE-2025-15467 CVSS 9.8 (Critical, no ITW per CISA advisory text
      — "publicly reported vulnerability" doesn't equate to ITW
      exploitation). All three afternoon Critical clusters fail
      Trigger 1 on active_exploitation field.
  trigger_2_tracked_actor_attribution:
    matched: false
    notes: |
      PM-001 + PM-002 + PM-003 + PM-004 all have NO tracked-actor
      attribution. MSTIC's "Undermining the Trust Boundary" IR case
      study explicitly uses "the threat actor" generic language — no
      Volt/Salt Typhoon, no UNC1549, no APT28, no actor named.
      Trigger 2 FAIL on new_attribution + tracked_actor_involved.
  trigger_3_first_party_ioc_hit:
    matched: false
    notes: |
      Splunk first-party 0 events for non-archimedes-internal stream
      over 8h + 24h. Targeted IOC keyword sweep including MSTIC PM-003
      IOCs (abc003.vbs, Errors.aspx, Signoff.aspx, ghost.inc,
      mslogon.dll, passms.dll, msupdate.dll, paths C:\Users\Public\
      Music\abc123c.d, C:\ProgramData\WindowsUpdateService\UpdateDir\
      Ipd) returned zero non-pipeline-self-reference hits. Trigger 3
      FAIL on splunk_match + ioc_tracked.
  trigger_4_tracked_actor_ttp_change:
    matched: false
    notes: |
      No tracked-actor TTP change documented this afternoon window.
      PM-003 MSTIC trust-boundary investigation describes T1199
      MITRE technique (Trusted Relationship) but no actor attributed.
      Trigger 4 FAIL on attributable + ttp_delta (no actor to attribute
      TTP delta to).
  trigger_5_ad_sector_campaign:
    matched: false
    notes: |
      No active multi-victim A&D-sector campaign disclosed this window.
      MSTIC PM-003 victim sector NOT disclosed (single-IR-case-study
      framing). Fortinet PM-002 affects security-appliance ecosystem
      broadly across many sectors, not A&D-specific. ABB AC500 cluster
      affects critical-infrastructure broadly across Chemical /
      Critical Manufacturing / Energy / Water, no A&D-specific
      multi-victim campaign claim. Trigger 5 FAIL on multi_victim +
      ad_sector_targeted.
  trigger_6_zero_day_no_patch:
    matched: false
    notes: |
      All afternoon Critical CVEs ARE PATCHED at disclosure. Microsoft
      shipped patches today via May Patch Tuesday. Fortinet shipped
      patches today via PSIRT advisories. ABB shipped firmware updates
      per CISA advisories. CVE-2026-45185 Exim BDAT/GnuTLS was patched
      2026-05-01 (11 days before this window). Trigger 6 FAIL on
      patch_available=false (all patched at-disclosure).
critical_override_evaluated:
  cvss_10: false                          # multiple Criticals but none CVSS 10.0 specifically
  active_exploitation: false              # none ITW
  tracked_actor: false                    # no actor attribution
  ad_watchlist_hit: false                 # structural A&D relevance only, no direct-prime named
  conditions_met: 0_of_4
  bypass_quiet_hours: false
  outcome: not_applicable                  # active hours anyway (15:30 EDT inside 09:00-21:00)
iocs_extracted: false                      # this is the sentinel sweep file; IOC extraction lives on per-item raw-signal files PM-001 through PM-004
iocs_count: 0
text_word_count: 0                         # sentinel sweep frontmatter-only
promoted: false
sentinel_disposition: audit_trail_only_no_promotable_claim
sentinel_processed_at: 2026-05-12T16:08:00-04:00
sentinel_processed_by_run: afternoon-20260512-160000
sentinel_processed_note: >
  Sentinel sweep file carries the sweep audit trail and pre-flight
  evaluation context for the afternoon brief grading run. Not a
  promotable claim cluster — the per-item raw-signals PM-001 through
  PM-004 are the gradable units. PM-001 → finding-2026-05-12-0003.
  PM-002 → finding-2026-05-12-0004. PM-003 → finding-2026-05-12-0005.
  PM-004 → finding-2026-05-12-0006.
ttl_expires_at: 2026-08-10T15:32:00-04:00  # 90 days per LEGAL-POLICY retention
---

# Sentinel — 2026-05-12 15:30 EDT pre-brief sweep

Pre-brief collection sweep for the 16:00 EDT afternoon brief. Window
12:00 → 15:30 EDT primary (3.5h since the 12:00 FLASH clean sweep);
backstop reach to 07:30 EDT for source-cadence resilience.

## Productive surface this sweep

Four content raw-signal files written (PM-001 through PM-004):

- **PM-001** — Microsoft May 2026 Patch Tuesday (120 Windows-only +
  17 Edge/Chromium = 137 total CVEs; no zero-days, no ITW). Standing
  patch-backlog tier; structurally A&D-relevant via Windows endpoint +
  AD/DNS infrastructure deployment across all primes.

- **PM-002** — Fortinet FortiSandbox CVE-2026-26083 + FortiAuthenticator
  CVE-2026-44277 critical unauthenticated RCE pair (no ITW). Structurally
  A&D-relevant via Fortinet security-appliance deployment at prime
  perimeters + MFA infrastructure.

- **PM-003** — MSTIC "Undermining the trust boundary" Microsoft IR case
  study (HPE Operations Agent abuse via compromised third-party IT
  services provider; T1199 Trusted Relationship; no actor named).
  Structurally relevant to A&D primes who outsource IT management.

- **PM-004** — CISA ICS batch (7 advisories incl. ABB AC500 V3 Stack
  Buffer Overflow CVE-2025-15467 CVSS 9.8 RCE + Subnet Solutions
  PowerSYSTEM Center CVSS 8.2 cluster + Fuji Electric Tellus CVSS 7.8 +
  ABB AC500 V3 Multiple Vulnerabilities CVSS 8.3 + ABB WebPro SNMP Card
  PowerValue CVSS 8.8 + ABB Automation Builder Gateway CVSS 5.3 + SBOM
  for AI Minimum Elements policy guidance non-threat-intel discarded).
  Critical-infrastructure / defense-manufacturing structural relevance.

## FLASH-trigger evaluation

Zero FLASH-trigger fires this sweep. All four PM raw-signals are
non-FLASH grader-queue material — see `flash_triggers_evaluated` in
frontmatter for per-trigger reasoning. Critical-override evaluation
2-of-4 fail (CVSS_10 absent + no ITW + no actor + no A&D watchlist
direct hit). Active-hours window anyway (15:30 EDT inside 09:00-21:00
EDT) so quiet-hours bypass moot.

## Anti-noise applied

Anti-noise / already-covered items discarded:

- SAP May Patch Day SecurityWeek/BleepingComputer relays — already
  covered AM-001 + finding-2026-05-12-0001 + 08:00 morning brief
- Apple May patches SecurityWeek relay — already covered at 06:00 FLASH
- Instructure ransom The Record + SecurityWeek relays — already covered
  at 06:00 FLASH sentinel
- Mini Shai-Hulud worm references — already covered FLASH-0600-001 +
  finding-2026-05-12-FLASH-0001 + 08:00 morning brief

## Discarded per Mode 1 (no watchlist / roster / vuln-index hit)

Items reviewed and discarded as out-of-scope for A&D-prime tracking:

- TrickMo TON C2 Android variant (ThreatFabric; France/Italy/Austria
  consumer banking)
- Exim CVE-2026-45185 "Dead.Letter" BDAT/GnuTLS (narrow USE_GNUTLS-only
  build deployment; patched 2026-05-01; no ITW)
- RubyGems hundreds-of-malicious-packages signup-suspension (Mend.io;
  no IOCs published yet, no actor, no A&D specific — flagged for
  2026-05-13 morning-brief candidate once Mend.io publishes IOC layer)
- Adobe 52 vulns batch (no ITW)
- West Pharmaceutical ransomware (pharma)
- BWH Hotels reservation-data breach (hospitality)
- CRPx0 OnlyFans-lure cross-platform malware (consumer)
- Škoda Auto online-shop breach (Volkswagen Group automotive consumer)
- Android 17 banking-scam protections (consumer feature announcement)
- Exaforce / White Circle / Rapid7 GRC vendor-product editorials
- HRW EU surveillance-tech export advocacy report (policy/governance)
- SBOM for AI Minimum Elements CISA + G7 guidance (policy/governance,
  non-threat-intel)

## Source-health updates this sweep

See `sources_health_changed_this_sweep` block in frontmatter. Notable:

- `bleepingcomputer` — one of the most productive single-feed sweeps of
  the day with 2 raw-signaled items + 4 in-scope-but-discarded
- `mstic` — productive afternoon (PM-003 fresh IR case-study post)
- `mandiant` — feedburner 404 18th consecutive sweep; failure_count
  16 → 17 (held healthy pending operator alt-endpoint decision)
- `cisa-advisories` — 7-item ICS batch published 12:00 UTC = 08:00 EDT
  just AFTER 07:30 morning sweep boundary (productive backstop-reach
  rationale validated)
- `fortinet-psirt` — FIRST Archimedes-corpus surface for direct
  vendor-portal fetch; index-page reachable but FG-IR detail-page
  ECONNREFUSED intermittent server-side issue; held healthy pending
  re-test next sweep; provisional A source-grade-log candidate analog
  to siemens-productcert (raw-2026-05-12-am-002 first-surface
  treatment)

## Flagged for orchestrator awareness (next-day candidates)

- **RubyGems supply-chain** — pattern-adjacent to today's Mini Shai-Hulud
  npm+PyPI worm but separate ecosystem and no IOCs published yet.
  Mend.io stated "more details once contained." High-probability
  follow-on raw-signal material for tomorrow morning's brief when the
  IOC layer surfaces.
- **UNC6692 + UNC1069** remain Mandiant-blog top-of-list visible titles
  but NOT in `_roster.yaml` — operator `/new-actor` candidates pending
  decision.

## What did NOT change this sweep

- Splunk first-party non-archimedes-internal stream: 0 events 8h + 24h
  (eighteenth consecutive dormant sweep across both indexes)
- KEV catalog: 0 entries dateAdded ≥ 2026-05-11 (full-catalog scan
  corroborates the day's KEV-quiet pattern)
- CrowdStrike blog feed: same dateless marketing pattern (eighteenth
  consecutive sweep)
- Mandiant feedburner: 18th consecutive 404
- x-cisagov + x-gossithedog + ars-security: stale-held per prior
  source-health entries

---

## Extraction notes

- Sentinel file — per Mode 1 procedure, this raw-signal carries the
  full sweep audit trail; per-item raw-signal files (PM-001 → PM-004)
  carry their own full frontmatter + body content + `iocs_extracted`
  blocks per the ioc-extraction skill output.
- Pre-flight LEGAL-POLICY check: passive RSS/web fetches + own-index
  Splunk reads only; `authorized_for_active_recon` remains empty; no
  prohibited query patterns triggered; no credentials surfaced this
  sweep.
- Anti-noise enforced per FLASH-POLICY §one-flash-per-topic-per-24h
  and per Mode 1 procedure.
- No raw-signal items marked `test: true` filtered from sweep (none
  observed in current `threats/raw-signal/` directory).

## IOCs (sentinel level)

This sentinel file carries no body-level IOC extraction — see PM-001
through PM-004 for per-item IOC blocks. The Splunk first-party sweep
queried but did not match any of the following indicator set:

```yaml
splunk_queried_iocs_no_match:
  ms_patch_tuesday_cves:
    - CVE-2026-41096
    - CVE-2026-40364
    - CVE-2026-40361
    - CVE-2026-40365
    - CVE-2026-41089
    - CVE-2026-41103
  fortinet_cves:
    - CVE-2026-26083
    - CVE-2026-44277
  mstic_pm_003_iocs:
    files:
      - abc003.vbs
      - Errors.aspx
      - Signoff.aspx
      - ghost.inc
      - mslogon.dll
      - passms.dll
      - msupdate.dll
    paths:
      - "C:\\Users\\Public\\Music\\abc123c.d"
      - "C:\\ProgramData\\WindowsUpdateService\\UpdateDir\\Ipd"
    domain: dREDEACTEDe.net    # MSTIC redacted in source; queried as substring
  cisa_ics_cves:
    - CVE-2025-15467
    - CVE-2025-2595
    - CVE-2025-41659
    - CVE-2025-41691
    - CVE-2026-26289
    - CVE-2026-33570
    - CVE-2026-35504
    - CVE-2026-35555
    - CVE-2026-8108
  exim_cve:
    - CVE-2026-45185
```

Zero non-pipeline-self-reference matches across all of these against
`archimedes` and `defenseclaw_local` indexes over `-24h@h` window.
