---
raw_id: raw-2026-05-18-am-000
collected_at: 2026-05-18T07:32:00-04:00
run_id: pre-brief-20260518-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: archimedes-self
  source_name: "Archimedes collector — pre-brief sweep sentinel"
  source_url: null
  published_at: 2026-05-18T07:32:00-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [sentinel, pre_brief, dedup_audit, monday_morning]
triage_tags:
  - sentinel
  - non_flash
  - dedup_audit
  - splunk_self_telemetry_only
  - dormant_splunk_sweep_42
  - monday_morning_pattern
  - cve_2026_20182_kev_t_post_lapsed_t_plus_10h
  - cve_2026_42897_kev_t_minus_11d
  - symantec_provisional_a_clock_fired_t_plus_37h
  - shinyhunters_cluster_named_victim_disclosure_observed
  - miniplasma_dual_relay_refinement_observed
iocs_extracted: false
iocs_count: 0
text_word_count: 1800
promoted: false
ttl_expires_at: 2026-08-16T07:32:00-04:00
---

# Pre-brief sweep sentinel — 2026-05-18 07:30 EDT (Monday morning)

**Window:** 2026-05-17 17:30 EDT → 2026-05-18 07:32 EDT (~14h)
**Prior sweeps in this window:**
- 2026-05-17 18:00 EDT scheduled FLASH (clean sweep, 0 triggers, 39th consecutive dormant Splunk sweep; raw-2026-05-17-flash-1800-000; commit 33d3f9a)
- 2026-05-18 00:00 EDT scheduled FLASH (clean sweep, 0 triggers, 40th consecutive dormant Splunk sweep; raw-2026-05-18-flash-0000-000; commit 9c61bdb)
- 2026-05-18 06:00 EDT scheduled FLASH (clean sweep, 0 triggers, 41st consecutive dormant Splunk sweep; raw-2026-05-18-flash-0600-000; commit a8121bc)

**Quiet hours:** ending 09:00 EDT today; morning brief publishes 08:00 EDT (inside the 21:00–09:00 quiet window for the FLASH-policy quiet-hours layer, but morning brief publication is a scheduled cadence brief NOT a FLASH and is exempt per FLASH-POLICY — INTEL-BRIEF-STANDARDS scheduled cadence governs).
**Catchup-window load this pre-brief:** the 18:00 / 00:00 / 06:00 FLASH sweeps already cleared the bulk of the 14h window; this pre-brief is effectively the gap-fill 06:00 → 07:30 (~1.5h fresh window) plus a full re-pass of the priority sources for any items that drifted in.

---

## Sources queried (this pre-brief sweep)

| Source | Status | Items in 14h window | Notes |
|---|---|---|---|
| CISA Advisories (`cisa-advisories`, RSS all.xml) | OK 200 | 0 | 30 items in feed total, all pre-window |
| CISA KEV (`cisa-kev`, JSON via WebFetch) | OK | 0 new entries | catalogVersion 2026.05.15 unchanged. Top 5 entries: CVE-2026-42897 Exchange OWA XSS (dateAdded 2026-05-15, due 2026-05-29 / **T-11d**), CVE-2026-20182 Cisco Catalyst SD-WAN auth bypass (dateAdded 2026-05-14, due 2026-05-17 / **T-0 deadline LAPSED end-of-day Sunday 2026-05-17, now T+10h+ post-deadline**), CVE-2026-42208 LiteLLM (2026-05-08), CVE-2026-6973 Ivanti EPMM (2026-05-07), CVE-2026-0300 PAN-OS (2026-05-06). |
| The Hacker News (`thehackernews`, RSS) | OK 200 | 3 (MiniPlasma, Shai-Hulud worm clones / Phantom Bot, Fast16 nuclear-simulations relay — all evaluated at 06:00 FLASH a8121bc, anti-noise here) | last_modified 10:17 UTC = 06:17 EDT |
| BleepingComputer (`bleepingcomputer`, RSS) | OK 200 | 5 (MiniPlasma, Pwn2Own Berlin final wrap, DirtyDecrypt Linux LPE, Windows 11 KB5089549 install issue, Windows 11 taskbar feature — last two technical-operations not threat-intel, all 5 evaluated at 06:00 FLASH a8121bc anti-noise here) | last_modified 11:23 UTC = 07:23 EDT |
| SecurityWeek (`securityweek`, RSS) | OK 200 | 6 (NGINX exploitation, Shai-Hulud worm clones, Grafana/Coinbase Cartel, Pwn2Own — all evaluated at 06:00 FLASH a8121bc, anti-noise; **TWO NET-NEW post-06:00 items: MiniPlasma SecurityWeek refinement 06:38 EDT + 7-Eleven/ShinyHunters breach 07:25 EDT — both raw-signaled as separate files this pre-brief**) | last_modified 11:25 UTC = 07:25 EDT |
| Krebs on Security (`krebs`, RSS) | OK 200 | 0 | last_modified 11:25 UTC = 07:25 EDT, 10 items in feed all pre-window. Multi-day Krebs cadence normal. |
| The Record (`the-record`, RSS) | OK 200 | 0 | 5 items in feed total, all pre-window |
| Unit 42 (`unit42`, RSS feedburner) | OK 200 | 0 | last_modified 08:35 UTC = 04:35 EDT (feed-server activity), 15 items in feed all pre-window |
| Microsoft Security Blog parent feed (`mstic`, RSS) | OK 200 | 0 | last_modified 2026-05-14 21:51 UTC, pre-window |
| Dark Reading (`darkreading`, RSS via mcp__rss-bridge__fetch_feed) | OK 200 | 2 (Shlomie Liberow AI-essay forward-dated 13:00 UTC + Alexander Culafi South Korea deepfakes 01:00 UTC — both already evaluated and discarded in 18:00 / 00:00 / 06:00 FLASH chain, anti-noise here) | last_modified 11:31 UTC = 07:31 EDT |
| MITRE/CrowdStrike (`crowdstrike`, RSS) | OK 200 | 10 items but all dateless marketing/MQ content | 16th-consecutive-sweep dateless-marketing pattern entrenched, no threat-intel content |
| ESET WeLiveSecurity (`eset`, RSS) | not re-fetched this sweep | n/a | Multi-day cadence; will re-fetch on 15:30 pre-brief or next FLASH |
| SentinelLabs (`sentinelone`, RSS) | not re-fetched this sweep | n/a | Multi-day cadence; will re-fetch on next sweep |
| Rapid7 (`rapid7`, RSS) | not re-fetched this sweep | n/a | Multi-day cadence |
| SANS ISC (`sans-isc`, RSS rssfeed.xml) | recovered intermittently per source-health | n/a | 2026-05-17 06:00 FLASH had transient parse-error; not re-tested this sweep |
| Cisco Talos (`cisco-talos`, RSS) | known intermittent 404 on `/feeds/posts/default` | n/a | Blog index WebFetch reachable as alt-path; no new posts since 2026-05-14 12:02 (CVE-2026-20182 UAT-8616 ongoing exploitation post, already in finding chain). KEV federal deadline lapsed end-of-day Sunday 2026-05-17 — no Talos follow-up post in window. |
| Sophos (`sophos`, RSS) | stale (`news.sophos.com/en-us/feed/` 404 since 2026-05-15) | n/a | Skipped per stale rule |
| Mandiant feedburner (`mandiant`) | 404 (~21st consecutive) | n/a | Carried in expected-broken state per source-health |
| Dragos (`dragos`) | known broken | n/a | `/blog/feed/` 404; carried in expected-broken state |
| Bitdefender Labs (`bitdefender`) | businessinsights.bitdefender.com/rss 404 (path-discovery pending) | n/a | Same path-discovery issue as 2026-05-16/17 |
| Symantec security.com (`symantec`) | symantec-enterprise-blogs feed 404 (path-discovery pending) | n/a | Same path-discovery issue. Provisional-A 72h ratification clock T+37h past elapsed deadline 2026-05-16T18:25; operator pass pending |
| Wiz Research (`wiz-research`) | feed.xml 404 (path-discovery pending) | n/a | Same path-discovery issue |
| Socket (`socket`) | blog/rss.xml 404 (path-discovery pending) | n/a | Same path-discovery issue |
| Industrial Cyber (`industrialcyber-co`) | 403 (Akamai WAF/bot-block) | n/a | Consistent prior pattern |
| ZDI Pwn2Own blog (`zdi-blog`, RSS) | not re-fetched this sweep | n/a | Pwn2Own Berlin already wrapped 2026-05-16 morning (raw-2026-05-16-am-001); SecurityWeek + BleepingComputer Pwn2Own-final-wrap items this window are pure secondary relays of ZDI primary, already evaluated at 06:00 FLASH |
| Splunk first-party (`splunk-archimedes`, `splunk-defenseclaw`) | OK | 0 non-self-telemetry events | **42nd consecutive dormant non-self-telemetry sweep** — see Splunk section below |
| x-cisagov | stale (nitter bridge fragility) | skipped per source-health | |
| x-gossithedog | stale (nitter delisted) | skipped per source-health | |
| ars-security | stale (feed retired) | skipped per source-health | Workaround: arstechnica.com/feed root works but security-only is retired |

---

## Splunk self-telemetry sweep

`index=archimedes OR index=defenseclaw_local earliest=-24h | stats count by sourcetype` returned:

- `archimedes:operation` = 1 event in last 6h (pipeline operations / FLASH-evaluation), expanded to 15+ events in last 24h
- `archimedes:scheduler` = 3 events in last 6h, expanded to 17+ events in last 24h (scheduled task launches every ~90min)
- **Zero non-self-telemetry sourcetypes in last 24h.** `index=defenseclaw_local earliest=-24h | head 10` returned 0 events.

This is the **42nd consecutive dormant non-self-telemetry Splunk sweep** (41 at 2026-05-18 06:00 FLASH a8121bc; 40 at 00:00 FLASH 9c61bdb; 39 at 2026-05-17 18:00 FLASH 33d3f9a; 38 at 16:00 afternoon brief 005596f; 37 at 15:30 pre-brief; 36 at 12:00 FLASH c17bf91; 35 at 08:00 morning brief c8a140d). Pattern fully entrenched. Per doctrine: silence is not disconfirming. No IOC hits against `threats/iocs/_master-index.yaml`. Trigger 3 (first-party-ioc-hit) cannot fire on a dormant non-archimedes-event stream.

---

## In-window items evaluated

### Items already evaluated at 06:00 FLASH a8121bc — anti-noise applies (NOT re-raw-signaled here)

The 06:00 FLASH sweep evaluated 8 in-window items at the SecurityWeek + BleepingComputer + The Hacker News + DarkReading layer. All 8 received Trigger 1–6 evaluations there; all 8 FAILED all 6 triggers; 3 were promoted to status-update candidate disposition for this morning's grader pass. Per anti-noise rule 1, this pre-brief sentinel does NOT re-evaluate; the 06:00 FLASH evaluations carry forward verbatim. Brief recap (commit a8121bc holds full detail):

1. **CVE-2026-42945 NGINX Rift VulnCheck Canaries dual-relay** (SecurityWeek Ionut Arghire 03:27 EDT + The Hacker News, same VulnCheck primary as 2026-05-17 12:00 FLASH c17bf91) — defensive-telemetry surface expansion, NOT A-grade-attested production exploitation. Status-update CANDIDATE for grader as CVE-2026-42945 carry-forward refinement / finding-2026-05-16-0001 carry-forward.
2. **Shai-Hulud worm clones — 4 npm packages** (SecurityWeek Ionut Arghire 05:45 EDT, primary: Ox Security) — UNATTRIBUTED actor explicitly distinct from TeamPCP. Materializes the predicted derivative-attacks-30-days WEP from flash-2026-05-15-0600-teampcp-shai-hulud-release / VT-006 carry-forward at T+3d post-source-code-release. Status-update CANDIDATE for grader as VT-006 / Mini Shai-Hulud lineage carry-forward refinement.
3. **Grafana / Coinbase Cartel breach** (SecurityWeek Eduard Kovacs 04:34 EDT) — Grafana victim self-disclosure; SecurityWeek single-source-relay attribution of "Coinbase Cartel linked to ShinyHunters, Scattered Spider, and Lapsus$" per unnamed cybersecurity companies. Status-update CANDIDATE for grader as Scattered-Spider cluster-adjacent surface pending A-grade vendor corroboration. Hard Rule 2 — do NOT propagate cluster-collapse attribution as Archimedes-originated.
4. **Pwn2Own Berlin 2026 final wrap** ($1.298M / 47 zero-days / DEVCORE Master of Pwn) — anti-noise rule 1 on finding-2026-05-16-0002. No re-fire.
5. **DirtyDecrypt CVE-2026-31635 Linux kernel rxgk LPE PoC** (V12 security team) — narrow distro footprint, patched 2026-04-25, no A-grade attestation, no CVSS published. Status-update CANDIDATE for grader for tracked-vuln list addition pending A-grade corroboration.
6. **Fast16 Symantec/Carbon Black nuclear-simulations sabotage-intent confirmation** (The Hacker News relay) — second-corpus surface on finding-2026-05-16-0003. Pre-Stuxnet 2005-2010 historical activity. Strengthens Symantec provisional-A ratification case.
7. **MiniPlasma BleepingComputer Lawrence Abrams original 2026-05-17 18:30 EDT** — duplicate-locked against 18:00 FLASH 33d3f9a. The Hacker News relay (08:57 UTC = 04:57 EDT this window) is a SECOND relay, anti-noise rule 1 active.
8. **DarkReading Shlomie Liberow AI-essay + Alexander Culafi South Korea deepfakes** — opinion-essay class, no triggers, anti-noise applies (same disposition as 18:00 FLASH 33d3f9a + 00:00 FLASH 9c61bdb).

### Net-new items surfaced post-06:00 FLASH (raw-signaled as separate files this pre-brief)

**Item A: SecurityWeek MiniPlasma refinement** (Ionut Arghire 2026-05-18T10:38 UTC = 06:38 EDT)
- Title: "Researcher Drops MiniPlasma Windows Exploit for Unpatched 2020 CVE"
- Underlying CVE explicitly named: **CVE-2020-17103** (CVSS 7.0, Windows Cloud Filter driver LPE-to-SYSTEM)
- New material vs. BleepingComputer / The Hacker News prior coverage: (a) SecurityWeek explicit CVE-2020-17103 mapping (BleepingComputer + THN did not name CVE; researcher claimed it as patched-flaw rediscovery), (b) Affected platform refined: Windows 11 with May 2026 security updates confirmed working, does NOT work on Windows 11 Insider Preview Canary builds (suggests unreleased fix may already be present upstream), (c) MSRC explicitly emailed for statement — no response yet, (d) Researcher quote elevated: "After investigating, it turns out the exact same issue that was reported to Microsoft by Google Project Zero is actually still present, unpatched" — implies either Microsoft never patched or patch was silently rolled back.
- Hard Rule 2 / 3 evaluation: SecurityWeek framing carefully avoids "exploitation begins" editorial framing on this item (unlike its NGINX article); the headline says "Drops" not "Exploits Begin." But the article DOES link the GitHub PoC repo `github.com/Nightmare-Eclipse/MiniPlasma` — Hard Rule 3 prevents Archimedes from linking the PoC repo URL in our own publications, but observing that the source linked it is fact of source coverage.
- Raw-signaled: `raw-2026-05-18-am-001-securityweek-miniplasma-cve-2020-17103-refinement.md`
- Status-update CANDIDATE for grader for VT-tracked-vuln evaluation; tied to carry-forward #11.

**Item B: 7-Eleven / ShinyHunters breach** (SecurityWeek Eduard Kovacs 2026-05-18T11:25 UTC = 07:25 EDT, ~5 minutes before this pre-brief)
- Title: "7-Eleven Data Breach Confirmed After ShinyHunters Ransom Demand"
- Named-victim self-disclosure: 7-Eleven confirmed an intrusion detected 2026-04-08 into systems storing franchisee documents; "unspecified personal information has been compromised" through franchise applications; reported only two Maine residents impacted per regulator filing.
- Attacker claim: ShinyHunters listed 7-Eleven on their leak site 2026-04-17, claimed >600,000 Salesforce records (personal information + corporate data) stolen, demanded ransom by 2026-04-21, later offered to sell for $250,000.
- Broader campaign context: SecurityWeek frames as part of the ShinyHunters Salesforce-customer targeting since mid-2025 ("exploiting phishing, abuse of third-party integrations, or misconfigurations rather than Salesforce vulnerabilities").
- Other named victims cited by SecurityWeek as part of same campaign: **Instructure, Vimeo, Wynn Resorts, Vercel, Medtronic** (none A&D primes; Medtronic = medical device manufacturer, Vercel = SaaS frontend hosting, Wynn = hospitality, Vimeo = video platform, Instructure = education LMS / Canvas).
- ShinyHunters NOT in `_roster.yaml`. Scattered Spider (#013 HIGH) is in roster; the Grafana article published earlier this morning at 04:34 EDT (FLASH 06:00 evaluated) relayed an unnamed-cybersecurity-companies multi-step attribution chain "Coinbase Cartel linked to ShinyHunters, Scattered Spider, and Lapsus$" — but Hard Rule 2 + LEGAL-POLICY no-attribution-laundering rule prevents Archimedes from propagating that chain to Scattered Spider direct attribution.
- No A&D entity named in 7-Eleven coverage. No A-grade vendor (Mandiant / CrowdStrike / Unit 42 / MSTIC) cited. No IOCs / CVEs.
- Material new context vs. Grafana article: 7-Eleven is the SECOND named-enterprise-victim disclosure in the same morning's news cycle on the ShinyHunters cluster activity. Grafana = code-stealing supply-chain-adjacent; 7-Eleven = Salesforce-records customer-data theft. Different mechanism but same actor cluster per SecurityWeek framing.
- Raw-signaled: `raw-2026-05-18-am-002-securityweek-7eleven-shinyhunters-salesforce-breach.md`
- Status-update CANDIDATE for grader; the ShinyHunters cluster activity is now a 2-victim same-morning disclosure pattern (Grafana + 7-Eleven) plus 5 historically-named victims in the same source-relayed campaign chain. Grader to evaluate as either: (a) discrete ShinyHunters Salesforce-campaign finding with the ShinyHunters cluster preserved verbatim and NOT propagated to Scattered Spider per Hard Rule 2, or (b) discarded as commodity-criminal-cluster activity outside A&D scope.

---

## Carry-forwards preserved (NOT re-collected this sweep)

Per orchestrator scope this morning — watch for new developments but do NOT re-collect existing topics:

1. **CVE-2026-20182 Cisco Catalyst SD-WAN auth bypass (CVSS 10.0, CISA KEV).** Federal patch deadline LAPSED end-of-day Sunday 2026-05-17 (T+10h+ past elapsed at this sweep). Watched this sweep for next-day CISA/OMB federal-agency-compliance reporting + A-grade vendor exploitation attestation (Mandiant / Volexity / Unit 42 / MSTIC / CrowdStrike / Talos / Symantec / Cisco PSIRT follow-up): **zero new items in window.** Cisco Talos blog index has no new post since 2026-05-14 12:02. Federal-agency-compliance reporting expected to surface in next-day CISA / OMB metric reporting per established pattern, not in the KEV catalog itself. finding-2026-05-14-0005 carry-forward chain.
2. **CVE-2026-42897 Microsoft Exchange OWA XSS (CISA KEV, due 2026-05-29).** T-11d to federal patch deadline. >48h single-source-veto on exploitation-claim layer holds: zero A-grade vendor (Mandiant / Volexity / Unit 42 / MSTIC / CrowdStrike) corroboration on the originating MSRC exploitation-detected claim. MSRC remains sole originating attester. finding-2026-05-15-0003 carry-forward.
3. **CVE-2026-42945 NGINX Rift PoC (depthfirst)** — VulnCheck Canaries dual-relay (SecurityWeek + The Hacker News + Ionut Arghire byline) refinement folded into 06:00 FLASH a8121bc evaluation as Item 1. Hard Rule 3 — PoC repo URL not linked. finding-2026-05-16-0001 carry-forward.
4. **Symantec/SentinelLABS Fast16 framework** — provisional-A 72h ratification clock now T+37h past elapsed 2026-05-16T18:25 deadline awaiting operator pass. New nuclear-weapons-simulations sabotage-intent confirmation per Symantec/Carbon Black + The Hacker News relay (06:00 FLASH a8121bc Item 6) strengthens ratification case via second-corpus surface. finding-2026-05-16-0003 carry-forward.
5. **Pwn2Own Berlin 2026 final wrap** — DEVCORE Orange Tsai Exchange RCE-to-SYSTEM chain under standard 90-day ZDI vendor-coordinated-disclosure embargo through ~2026-08-13. Final event totals confirmed $1.298M / 47 zero-days / DEVCORE Master of Pwn 50.5 points / $505K rewards (06:00 FLASH a8121bc Item 4). finding-2026-05-16-0002 carry-forward refinement.
6. **Turla/Kazuar/Secret Blizzard** — D+2 relay layer duplicate-locked against finding-2026-05-14-0006 / reject-2026-05-16-0001. No new relay surface this window.
7. **Tycoon2FA device-code PhaaS** — absorbed into finding-2026-05-17-0002 per afternoon brief 005596f. Commodity criminal PhaaS, no tracked actor, anti-noise rule 1 active, no re-fire.
8. **Shai-Hulud worm clones** (4 npm packages, UNATTRIBUTED per Ox Security) — VT-006 / Mini Shai-Hulud lineage carry-forward refinement, 06:00 FLASH a8121bc Item 2 evaluation governs.
9. **CVE-2026-31635 DirtyDecrypt Linux kernel rxgk LPE** — V12 security team PoC, narrow distro footprint, patched upstream 2026-04-25, status-update candidate pending A-grade corroboration. 06:00 FLASH a8121bc Item 5 evaluation governs.
10. **Grafana / Coinbase Cartel breach** — Scattered-Spider cluster-adjacent surface pending A-grade vendor corroboration. 06:00 FLASH a8121bc Item 3 evaluation governs. Today's 7-Eleven breach (Item B above) is the SECOND named-enterprise-victim disclosure in the same morning's news cycle on the ShinyHunters cluster — grader's call whether to fold or treat discretely. Hard Rule 2 — do NOT propagate SecurityWeek multi-step relay attribution chain to roster actors.
11. **MiniPlasma Windows CVE-2020-17103 rediscovery** (Chaotic Eclipse / Nightmare Eclipse) — SecurityWeek refinement post-06:00 (Item A above) elevates carry-forward from "POC published" to "POC published with explicit CVE-2020-17103 mapping + MSRC unresponsive + Insider Preview Canary already fixed" status. Status-update CANDIDATE pending Microsoft MSRC confirmation / MSTIC active-exploitation telemetry / CISA KEV addition.

---

## Source health observations (this sweep)

Runtime state changes proposed for `infrastructure/source-health.yaml` (operator-set `notes` preserved verbatim per Hard Rule field-ownership doctrine):

- **`bleepingcomputer`**: healthy. Fetch successful; 5 in-window items, all evaluated and dispositioned via 06:00 FLASH or filtered as technical-operations. `last_successful_fetch` → 2026-05-18T07:32:00-04:00.
- **`thehackernews`**: healthy. Fetch successful; 3 in-window items, all carry-forward refinements of 06:00 FLASH evaluations. `last_successful_fetch` → 2026-05-18T07:32:00-04:00.
- **`securityweek`**: healthy. Fetch successful; 6 in-window items, 4 evaluated at 06:00 FLASH a8121bc, 2 NET-NEW post-06:00 raw-signaled separately. `last_successful_fetch` → 2026-05-18T07:32:00-04:00.
- **`cisa-advisories`**: healthy. Fetch successful; 0 in-window items. `last_successful_fetch` → 2026-05-18T07:32:00-04:00.
- **`cisa-kev`**: healthy. JSON catalog unchanged from 06:00 FLASH state. `last_successful_fetch` → 2026-05-18T07:32:00-04:00.
- **`krebs`**: healthy. Fetch successful; 0 in-window items. `last_successful_fetch` → 2026-05-18T07:32:00-04:00.
- **`the-record`**: healthy. Fetch successful; 0 in-window items. `last_successful_fetch` → 2026-05-18T07:32:00-04:00.
- **`unit42`**: healthy. Fetch successful; 0 in-window items. `last_successful_fetch` → 2026-05-18T07:32:00-04:00.
- **`mstic`**: healthy. Fetch successful; 0 in-window items. `last_successful_fetch` → 2026-05-18T07:32:00-04:00.
- **`splunk-archimedes`**, **`splunk-defenseclaw`**: both healthy; 42nd consecutive dormant non-self-telemetry sweep. `last_successful_fetch` → 2026-05-18T07:32:00-04:00.
- All other queried sources: reachable or in known expected-broken/stale state per source-health.yaml; no changes proposed.

---

## Disposition

**Two net-new raw-signal files written this pre-brief:**
1. `raw-2026-05-18-am-001-securityweek-miniplasma-cve-2020-17103-refinement.md` — SecurityWeek refinement of MiniPlasma carry-forward #11 with explicit CVE-2020-17103 mapping + MSRC unresponsive + Insider Preview Canary already fixed (Ionut Arghire byline)
2. `raw-2026-05-18-am-002-securityweek-7eleven-shinyhunters-salesforce-breach.md` — net-new named-enterprise-victim disclosure on ShinyHunters Salesforce-customer campaign; SECOND named-victim same morning (Grafana being the first); Eduard Kovacs byline; relevant to carry-forward #10 (Grafana / Coinbase Cartel) re-evaluation by grader

**42nd consecutive dormant non-self-telemetry Splunk sweep.** Pattern fully entrenched. Per doctrine: silence is not disconfirming. No IOC hits against `threats/iocs/_master-index.yaml`. Trigger 3 cannot fire.

**No FLASH-eligible items spotted this pre-brief** (06:00 FLASH a8121bc already evaluated and cleared the 8 carry-forward-relevant items; the 2 net-new SecurityWeek items are status-update candidates / refinements, not FLASH-trigger fires).

**Source-health runtime updates queued for `infrastructure/source-health.yaml`:** `last_successful_fetch` refresh across all healthy fetched sources (bleepingcomputer, thehackernews, securityweek, cisa-advisories, cisa-kev, krebs, the-record, unit42, mstic, splunk-archimedes, splunk-defenseclaw). Operator-set `notes:` fields preserved verbatim per Hard Rule field-ownership doctrine. No status flips this sweep.

**Zero LEGAL-POLICY refusals this sweep.** authorized-targets.yaml empty; SpiderFoot not invoked; theHarvester not invoked; no active scanning; no exploitation assistance; no credential storage; no impersonation; no circumvention. TLP:CLEAR.

## Extraction notes

- Language: en
- Article type: sentinel / pre-brief sweep aggregator
- Raw IOC extraction invoked: no (sentinel; no novel content)

## IOCs (from ioc-extraction skill)

No IOCs in this sentinel. Two net-new raw-signal files (am-001 + am-002) each contain ioc-extraction skill output for their primary surfaces.
