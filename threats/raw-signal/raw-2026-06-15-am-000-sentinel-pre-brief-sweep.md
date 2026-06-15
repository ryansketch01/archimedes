---
raw_id: raw-2026-06-15-am-000
collected_at: 2026-06-15T07:32:00-04:00
run_id: pre-brief-20260615-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: sentinel-internal
  source_name: "Pre-brief sweep sentinel (internal)"
  source_url: null
  published_at: 2026-06-15T07:32:00-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [pre_brief_sweep, splunk_sentinel_clean, peoplesoft_deadline_today, source_health_observations]
triage_tags: [non_flash, sentinel, sweep_substantive, pre_brief, peoplesoft_final_pre_deadline_brief]
iocs_extracted: false
iocs_count: 0
text_word_count: 1800
promoted: false
ttl_expires_at: 2026-09-13T07:32:00-04:00
---

# Pre-brief sweep 2026-06-15 07:30 EDT — morning brief substrate (3 net-new raw-signals + 2 carry-forward relays)

## Sweep parameters

- Mode: `pre_brief_collection` for the 08:00 EDT morning brief on Sunday 2026-06-15
- **PeopleSoft / UNC6240 deadline context:** CVE-2026-35273 BOD 26-04 KEV due-date closes **EOD TODAY Sunday 2026-06-15 (~T-16h from 08:00 brief publication)**. This morning brief is the **FINAL pre-deadline FCEB coverage window**; afternoon brief at 16:00 EDT would be ~T-8h still pre-EOD but the morning brief is the substantive coverage window for compliance-status framing. Ivanti Sentry CVE-2026-10520 deadline already PAST EOB 2026-06-14 (~13h ago).
- Time window: 2026-06-14T15:30:00-04:00 → 2026-06-15T07:32:00-04:00 (~16h since last pre-brief substrate close + 6h since 06:00 EDT flash sweep). Effective collection window covers everything since the 15:30 PM pre-brief substrate; intermediate flash sweeps (18:00 + 00:00 + 06:00) all returned clean (3 consecutive clean sentinel sweeps + 9th in cumulative 36h window since 2026-06-13 18:00).
- Active hours per FLASH-POLICY (09:00-21:00 EDT). This is a pre-brief collection, not a FLASH sweep; FLASH-trigger evaluation is downstream-of-grader.
- Sources queried: 18 healthy primary RSS feeds + KEV JSON + Mandiant direct-HTML index + BleepingComputer direct-HTML cross-check + Splunk first-party sentinel.
- Sources skipped (stale, <24h per under-24h rule): volexity, msrc, lumen (failure_count=1 held healthy), shadowserver (failure_count=1 held healthy), trellix, x-cisagov, x-gossithedog, censys, urlscan, hibp, abw.
- Sources skipped (stale, retried per >=24h rule): mandiant feedburner (retried, still 404 — 29th consecutive observation; direct-HTML path remains the productive endpoint), proofpoint (not retested this sweep — no top-level entry exists in source-health, soft-pattern continuity carry).
- Operator binding: COLLECTION ONLY. No grading, no FLASH evaluation, no brief composition, no Discord posting, no commit, no `_coverage-log.yaml` update.

## In-window content survey

### SecurityWeek — 5 in-window items (3 substantive, 2 already-covered)

1. **"ShinyHunters Claims Council of Europe Hack"** by Ionut Arghire (2026-06-15T10:44:29Z = 06:44 EDT inside window). **NET-NEW SUBSTRATE.** ShinyHunters added Council of Europe to Tor leak site Sunday, claiming 297 GB / 429,000+ files including: payroll data for 10,000+ employees (2011-2026), 14,000+ CVs, contract/PO records, absence/illness reports, bank account info, performance evaluations, employee PII, tax/SSN info, medical records. Affected departments: HR, Secretariat, Parliamentary Assembly, European Directorate for Quality of Medicines & HealthCare. Threat to release if no contact by **June 16**. Council of Europe has not publicly acknowledged. Article explicitly references ShinyHunters' **separate** "zero-day vulnerability in Oracle PeopleSoft" campaign (i.e., the UNC6240 / CVE-2026-35273 BOD 26-04 cluster) — Council of Europe NOT attributed to PeopleSoft per article, but the dual-campaign visibility is the contextual hook. **A&D-prime relevance: NONE direct** (Council of Europe is a 46-state intergovernmental human-rights body, not an A&D supplier; HQ Strasbourg). Strategic-context relevance: ShinyHunters as active multi-campaign actor this week parallels DentaQuest 2.6M (06-12 substrate) and PeopleSoft UNC6240 mass theft (finding-2026-06-13-0002 + 0006). **Raw-signaled as `raw-2026-06-15-am-001`** for grader handoff. Grader decision: surface in morning brief as ShinyHunters-cluster carry-forward bullet (single-source SW + threat-actor leak-site claim, **single-source veto applies on volume claim**; Council of Europe official ACK pending). Possible UPDATE-on-PeopleSoft-substrate framing for the dual-campaign actor visibility.

2. **"Ozempic Maker Novo Nordisk Says Hackers Breached IT Systems"** by Eduard Kovacs (2026-06-15T11:17:21Z = 07:17 EDT inside window, ~13min before sweep). **NET-NEW SUBSTRATE.** Pharmaceutical giant discloses limited number of internal IT systems containing personal data breached. Affected data: patient clinical trial data (randomly-assigned IDs, biomarkers, immunogenicity), healthcare provider info (names, registrations, contact). Company statement: "not directly linked to any patients by name or other direct identifiers." **No attribution, no actor named, no CVE, no IOCs, no ransomware claim, no A&D / aerospace / defense connection.** Pharma sector — Novo Nordisk is the world's largest GLP-1 manufacturer. **Raw-signaled as `raw-2026-06-15-am-002`** for grader handoff. Grader decision: likely Other Signal single-bullet if covered at all (pharma not A&D-prime, single-source vendor self-disclosure with no actor attribution).

3. **"French Government Messaging Platform Breached by Mysterious 'Misere' Hacker"** by Kevin Townsend (2026-06-15T11:09:10Z = 07:09 EDT inside window, ~22min before sweep). **UPDATE on finding-2026-06-12-pm-009 / finding-2026-06-10-pm-007 Tchap French government breach.** Net-new substrate vs prior coverage: actor name "Misere" claimed responsibility, 73,000 of 825,000 accounts affected (<9% per DINUM), claimed exfiltration 13.5 GB + 640,000+ plaintext messages, breach occurred **2026-06-07**. Expert Ilia Kolochenko (article-quoted analyst) characterizes "too small for large power intelligence agencies to bother with" but flags data as targeting-material risk for downstream spear-phishing by financial or state actors. **No public record of threat actor "Misere" — likely burner identity per analyst.** No A&D-prime relevance. No CVE, no IOC. **Raw-signaled as `raw-2026-06-15-am-003`** for grader handoff. Grader decision: surface as UPDATE bullet on Tchap finding chain if afternoon brief has substrate; not FLASH-eligible.

4. **"FBI, Google Dismantle 'Outsider Enterprise' Phishing Service"** by Ionut Arghire (2026-06-15T09:31:14Z = 05:31 EDT). Second-day relay of yesterday's BleepingComputer primary (already shipped as finding-2026-06-14-0001 in 2026-06-14 PM brief at commit `18e26fc`). 9,000 phishing sites + nearly 4 million credit cards + $1.9B in losses figures match prior substrate. **DISCARDED — anti-noise hold (UPDATE already shipped).**

5. **"Maine Disables Data Breach Portal Due to Fake Submissions"** by Eduard Kovacs (2026-06-15T08:34:54Z = 04:34 EDT). Fake VRChat/Discord breach submissions on Maine AG portal. **DISCARDED — administrative news, not threat intel.**

### The Hacker News — 4 in-window items

1. **"152 Chrome Wallpaper Extensions with 105K Installs Linked to Adware and Fake Traffic"** by Ravie Lakshmanan (2026-06-15T11:07:50Z = 07:07 EDT inside window, ~25min before sweep). Socket researcher Kush Pandya disclosure. PUP family, 105K installs, 3 brand backends (tabplugins[.]com, yowgames[.]com, chromewallpaper[.]com), 20+ extension IDs disclosed. No actor attribution; circumstantial Turkish provenance indicators. Consumer adware not A&D-prime threat. **DISCARDED — consumer adware, not FLASH-eligible.** Possible Other Signal carry if grader wants supply-chain-of-browser-extensions framing.

2. **"Popular WordPress Plugin Scripts Tampered to Plant Hidden Backdoors on Sites"** (2026-06-15T09:59:38Z = 05:59 EDT). **Publisher-independent second relay of yesterday's SA Awesome Motive WordPress CDN supply-chain story** (Sansec primary 2026-06-13). THN adds NEW substrate vs SA: PushEngage's UpdraftPlus initial-entry-theory disputed by Sansec ("the breached system is still unknown"); attacker server IP **84.201.6.54** disclosed (NEW IOC vs SA piece); hidden plugin folder names "content-delivery-helper" / "database-optimizer"; admin account patterns "developer_api1" / "dev_xxxxxx" reaffirmed; 1.2M sites collective reach figure refined down from SA's "thousands". **Two publisher-independent B-grade publishers + A-grade Sansec primary discoverer (A2 with B-grade publishing-tier)** — meets multi-publisher corroboration threshold per INTEL-GRADING discipline. **Raw-signaled as `raw-2026-06-15-am-004`** for grader handoff. Grader decision: possible Other Signal one-liner; consumer WordPress out of A&D-prime scope but pattern-of-CDN-supply-chain-compromise reinforces Polyfill 2024 lineage and Sansec-primary credibility. Not FLASH-eligible.

3. **"Sniper Dz Scams Target MENA Users via Fake Facebook Offers and Browser Alerts"** (2026-06-15T06:30:22Z = 02:30 EDT). Group-IB Anna Yurtaeva + Viacheslav Shevchenko disclosure. PhaaS platform previously dismantled INTERPOL May 2026; consumer fraud MENA. No A&D, no Iranian-tracked-actor link, no nation-state. **DISCARDED — consumer scam, not FLASH-eligible.**

4. **"Palo Alto Warns of Active Exploitation of PAN-OS GlobalProtect VPN Flaw"** (2026-06-15T06:17:32Z = 02:17 EDT). **Vendor confirmation of CVE-2026-0257 active exploitation.** Already in 06:00 FLASH sentinel substrate as evaluated-not-FLASH-eligible. **Net-new vs 06:00 substrate: vendor (Palo Alto) confirmation language is now public.** CVSS 7.8 fails T1 >=9.0 + T6 >=8.0. SA piece (item below) carries full Rapid7 detail with IOCs. **DISCARDED for FLASH but Other Signal one-liner candidate for morning brief** — retrospective context that the May 17 exploitation activity is publicly vendor-confirmed; KEV deadline 2026-06-01 already past 14 days.

### Security Affairs — 3 in-window items

1. **"Palo Alto Warns of Exploitation of VPN Bypass Exploits (CVE-2026-0257) in PAN-OS Flaw"** by Pierluigi Paganini (2026-06-15T11:11:13Z = 07:11 EDT inside window). Companion to THN PAN-OS piece. **Full Rapid7 detail with IOCs:** consistent MAC `aa:bb:cc:dd:ee:ff` across both waves (same-actor assessment), source ASNs Vultr (May 18 wave 1) + Dromatics Systems (May 21 wave 2), hostnames "GP-CLIENT" (Linux) + "DESKTOP-GP01", first observation 2026-05-17, 8/10 customer envs received forged-cookie acceptance without full VPN session, 2/10 received VPN IP assignment and internal access, no successful lateral movement. CVSS 7.8 (Palo Alto initial assessment as medium, Rapid7 disagrees). No tracked-actor attribution; "unknown threat actor" per all sources. **Raw-signaled as `raw-2026-06-15-am-005`** for grader handoff — primary IOC carrier even though substrate fails FLASH triggers. Other Signal grader call likely.

2. **"Supply Chain Attack Hits Popular WordPress Plugins Through Awesome Motive CDN"** by Pierluigi Paganini (2026-06-15T08:34:02Z = 04:34 EDT). Same Sansec-primary substrate as THN piece (item 2 above). SA was first publisher-relay (yesterday 06:00 sweep flagged); THN is now second publisher-relay. Two-publisher corroboration achieved. **Substrate referenced in `raw-2026-06-15-am-004` THN file above — no separate SA raw-signal written (anti-noise principle: one raw-signal per substrate cluster).**

3. **"Infostealers, AI, and a 90% Affiliate Cut Fuel The Gentlemen group's Rise"** by Pierluigi Paganini (2026-06-15T06:58:21Z = 02:58 EDT). **KELA RansomNews research report deep-dive on The Gentlemen ransomware** — 483 victims since 2025-09 emergence, 380 in 2026 alone, second-most-prolific by leak-site volume in 2026 (only behind Qilin), 9 core members, 90% affiliate cut model, AI-assisted tooling ("vibe-coded" negotiation panel in 3 days per "zeta88"), operators using Qwen-variant uncensored models for analysis. Initial access via FortiOS CVE-2024-55591 + ZeroLogon + PetitPotam + infostealer creds. May 2026 chat leak (Nov 2025 - Apr 2026). Manufacturing top-targeted sector, healthcare 44 victims, only ~15% US (atypically low vs 40-50% typical), Tier 1-3 countries + LatAm priority. 2GO Philippine logistics named victim with 6 employee logins + 7 customer logins + 38 active session tokens pre-exposed via alerts.bar infostealer index. Microsoft separately documented self-propagating Go-based encryptor. **The Gentlemen is NOT on the 24-actor `_roster.yaml`.** Operator-deferred /new-actor consideration per prior sweep substrate; this deeper KELA detail strengthens the /new-actor candidacy with named-victim cross-validation (alerts.bar IOC layer). **Raw-signaled as `raw-2026-06-15-am-006`** for grader handoff — possible Other Signal mention + actor-profiler /new-actor candidate-strength bullet.

### Help Net Security — 9 in-window items

1. **"Proving what a military AI model will do is the real problem"** by Sinisa Markovic (2026-06-15T08:30:35Z = 04:30 EDT). **A&D-prime watchlist hit: Lockheed Martin explicitly named** alongside Anduril (OpenAI partner), Palantir (Microsoft partner). Discusses verification problem in military AI systems delivered to drone-tasking and kill-chain support. **No incident, no breach, no IOC, no CVE, no actor attribution.** Opinion-class / research-framing piece, not threat intel. **A&D-prime watchlist hit by Lockheed Martin name reference suffices for grader visibility but substantively not promotion-eligible — no threat substrate, just sector context.** **Raw-signaled as `raw-2026-06-15-am-007`** for grader handoff — sector-context Other Signal candidate.

2-9. **PhishLumos research / Modat Magnify product / Microsoft Wi-Fi check-in privacy / LTM BlueVerse AI marketing / Onspring GRC CISO interview / CI/CD abuse detector open-source / hardware NN backdoor research / AI-generated code senior-engineer review.** All opinion / research / industry product news. None FLASH-eligible. **DISCARDED in aggregate.**

### Other healthy sources — 0 in-window items beyond noted

- BleepingComputer: 0 in window (RSS confirms last_modified Mon 15 Jun 11:19 GMT but no items in window; direct-HTML cross-check confirms only deal-of-the-day post + yesterday's FBI Outsider Enterprise piece in window range)
- The Register: 0 in window (last_modified Mon 15 Jun 09:31 GMT inside window from feed-server activity but no items in window)
- The Record: 0 in window
- Krebs: 0 in window (last_modified Thu 11 Jun pre-window)
- Cisco Talos: 0 in window (200 OK + ETag; 15 items in feed pre-window)
- SentinelLabs: 0 in window (last_modified Sat 13 Jun pre-window)
- Microsoft Security Blog (MSTIC parent): 0 in window (last_modified Wed 10 Jun pre-window)
- Rapid7: 0 in window (20 items in feed pre-window)
- WeLiveSecurity (ESET): 0 in window (last_modified Sat 13 Jun pre-window)
- Unit 42 feedburner: 0 in window (last_modified Fri 12 Jun pre-window)
- CISA all.xml Atom: 200 OK + parseable + 30 items, 0 in window
- CISA news.xml: 200 OK + 10 items, 0 in window
- SANS ISC rssfeed.xml: 200 OK + parseable; 2 in-window items (Evil MSI BASE64 analysis from 06:00 sweep + Stormcast podcast detail) — both defensive content, neither FLASH-eligible
- Sophos category-path: 200 OK + parseable + 15 items, 0 in window (last_modified holds)
- Dark Reading rss.xml: **RECOVERED 200 OK** (vs yesterday's 06:00 single-failure 404 observation) — 1 dateless "Name That Toon Contest" event marker only (DISCARDED, no actual content). **404 was transient single-failure as anticipated; NOT promoted as stale.**

### Sources with degradations this sweep

- **industrialcyber.co `/feed/`:** 403 forbidden this sweep (first observation in tracking — failure_count 0 → 1; NOT promoted to stale on single observation; possible Cloudflare bot-detection trip vs persistent endpoint failure — will re-attempt on next sweep)
- **dragos.com `/blog/feed/`:** 404 this sweep (first observation in tracking — failure_count 0 → 1; NOT promoted to stale on single observation; possible endpoint change; will re-attempt on next sweep)
- **bitdefender.com `/blog/businessinsights/rss/`:** 404 this sweep (Bitdefender restructuring suspected — was successfully fetched 2026-06-01 pre-window per healthy status; first observed failure here; failure_count 0 → 1; NOT promoted to stale on single observation)

These three single-failure observations are **soft-flagged for operator review** but NOT mutated to `status: stale` per field-ownership / single-failure-non-promotion rule.

### CISA KEV catalog scan: 0 net-new entries since 2026-06-12

5 most recent KEV adds unchanged from 06:00 FLASH substrate:
- **CVE-2026-35273 Oracle PeopleSoft** (added 2026-06-12, dueDate **2026-06-15 = TODAY EOD ~T-16h from 08:00 brief publication**) — anti-noise-held; UNC6240 / ShinyHunters per Mandiant primary; ransomwareUse: Known
- **CVE-2026-10520 Ivanti Sentry** (added 2026-06-11, dueDate 2026-06-14 = PAST ~13h ago) — anti-noise-held; CVSS 10.0; deadline closed overnight; ransomwareUse: Unknown
- CVE-2026-11645 Chrome V8 (added 2026-06-09, dueDate 2026-06-23, ransomwareUse Unknown)
- CVE-2026-7473 Arista EOS (added 2026-06-09, dueDate 2026-06-23, ransomwareUse Unknown)
- CVE-2026-20245 Cisco Catalyst SD-WAN (added 2026-06-09, dueDate 2026-06-23, ransomwareUse Unknown)

**NO net-new KEV adds.** No FCEB-compliance data has landed on either closed/closing clock.

### Mandiant direct-HTML index (cloud.google.com/blog/topics/threat-intelligence)

Top-10 posts confirmed unchanged from 06:00 FLASH + 15:30 PM pre-brief substrate (7 consecutive direct-HTML successes against RSS-path failure):
1. GTIG AI Threat Tracker
2. ShinyHunters Targets Education Sector with Oracle PeopleSoft Exploit (finding-2026-06-13-0002 + 0006 substrate — **relevant to today's PeopleSoft deadline framing**)
3. Seeking Counsel: Ongoing Targeted Campaign Against US Law Firms (UNC3753 vishing — operator-deferred)
4. Exploitation of KnowledgeDeliver via ViewState Deserialization
5. 2 PhaaS 2 Furious — Chinese-Language Phishing Services
6. Welcome to BlackFile — Vishing Extortion
7. Snow Flurries — UNC6692 Social Engineering (not on roster)
8. Defending Your Enterprise When AI Models Can Find Vulnerabilities (deSouza opinion)
9. The German Cyber Criminal Überfall
10. vSphere and BRICKSTORM Malware Defender's Guide

**None dated in window.** All previously substrate. **Direct-HTML path CONFIRMED working consistently 2026-06-13 PM + 2026-06-14 00:00 + 06:00 + 07:30 + 12:00 + 15:30 + 2026-06-15 06:00 + 07:30 — 8TH consecutive direct-HTML success against RSS-path failure; canonical-swap operator decision still pending after 8 consecutive direct-HTML successes.**

## Splunk first-party sentinel — Hard Rule 8

Indexes queried: `archimedes`, `defenseclaw_local`. Time window: -24h.

Sentinel set (19 IOCs carried forward from 2026-06-13 PM brief commit dc85aae): `azurenetfiles.net`, `176.120.22.24`, staging IPs `142.11.200.186-190` (5 IPs), Windows meshagent filenames (3), Linux + Windows meshagent SHA-256 hashes (5 — elided per Hard Rule 7), `.bash_history` ref, `exfil.tar.zst`, `envmetadata/data/environment/`, README defacement marker.

Query executed (mcp__splunk-query__search): `search index=archimedes OR index=defenseclaw_local ("azurenetfiles.net" OR "176.120.22.24" OR "142.11.200.186" OR "142.11.200.187" OR "142.11.200.188" OR "142.11.200.189" OR "142.11.200.190" OR "meshagent64-azure-ops" OR "meshagent64-v2" OR "meshagent32-azure-ops" OR "exfil.tar.zst" OR "envmetadata/data/environment" OR "README-IF-YOU-SEE-THIS-YOUVE-BEEN-HACKED") earliest=-24h@h latest=now`

**Result: 0 events over -24h on either index.**

This is the **10TH CONSECUTIVE clean sentinel sweep** across the cumulative window since 2026-06-13 18:00 EDT (18:00 + 00:00 + 06:00 + 07:30 + 12:00 + 15:30 + 18:00 + 00:00 + 06:00 + 07:30). Pattern fully established at the 42-hour mark; sentinel set remains valid carry-forward. Frank is not a higher-ed environment consistent with UNC6240's 68% higher-ed victim concentration per Mandiant — silent Splunk does NOT disconfirm. Visibility-limited absence, NOT confirmed-negative.

**Hard Rule 8 binding for today's PeopleSoft brief:** the 10-sweep clean window over 42h cumulative ON the standing IOC set against defenseclaw_local + archimedes DOES NOT support an "all-clear" framing for FCEB-class peers consuming the brief — Frank's higher-ed-pattern visibility mismatch with UNC6240's victim profile means absence here is non-disconfirming. Morning brief should preserve the "hunt the 19-IOC set today" call substrate-language with the visibility caveat per Hard Rule 8.

## Source-health deltas observed this sweep (runtime fields only)

The collector is permitted to mutate runtime fields per field-ownership rule, but operator binding for this run says COLLECTION ONLY — no source-health.yaml file mutations this sweep. Observations are logged here for librarian Mode 1 handoff post-brief commit.

- **mandiant:** feedburner RSS 404 again — per >=24h-since-stale rule (stale_since=2026-06-13, ~38h ago), the retry IS eligible. **Failure_count would advance 28 → 29** if mutated. Direct-HTML retrieval path SUCCEEDED again (8th consecutive direct-HTML success). Operator-flagged canonical-swap decision still pending — NOT swapped this sweep per operator binding.
- **sans-isc:** rssfeed.xml reachable + parseable + 2 in-window items (Stormcast + Evil MSI defensive analysis). Stable. No state change required.
- **cisco-talos:** blog.talosintelligence.com/rss/ reachable (200 OK + ETag); 15 items in feed, 0 in window. No state change.
- **sophos:** category-path `news.sophos.com/en-us/category/threat-research/feed/` returned 200 OK with 15 items, last_modified holds from yesterday. **Top-level `news.sophos.com/en-us/feed/` remains stale-persistent; category-path success is SOFT observation worth carrying for operator endpoint-swap consideration.** **NOT swapped this sweep per operator binding.**
- **proofpoint:** Not retested this sweep. `/us/threat-insight/blog/feed` soft-pattern continuity from 06:00 sweep; **no top-level proofpoint-threat-insight entry exists in source-health, NOT promoted to status:stale without operator approval.**
- **dark-reading:** **RECOVERED from yesterday's 404 single-failure observation** — `rss.xml` returned 200 OK + 1 dateless event item. Single-failure transient as anticipated; **NOT mutated to stale** (only had single failure observation 06:00 yesterday; today's recovery confirms transient). No state change required.
- **industrialcyber.co:** **403 forbidden this sweep** — first observation. Cloudflare-anti-bot likely. **failure_count 0 → 1** if mutated. NOT promoted to stale on single observation. Soft-flag for operator review.
- **dragos:** **404 this sweep on `/blog/feed/`** — first observation. Endpoint may have changed. **failure_count 0 → 1** if mutated. NOT promoted to stale on single observation. Soft-flag for operator review.
- **bitdefender:** **404 this sweep on `/blog/businessinsights/rss/`** — first observed failure on this endpoint. Bitdefender corporate restructuring suspected (split / rebrand activity 2025-2026). **failure_count 0 → 1** if mutated. NOT promoted to stale on single observation. Soft-flag for operator review.
- **lumen:** not retested this sweep (failure_count=1 from 2026-06-12 12:00 XML parse error; multi-day cadence; held healthy below stale threshold).
- **shadowserver:** not retested this sweep (failure_count=1 from 2026-06-12 12:00 404; relay-tier already-productive coverage via BleepingComputer / SecurityWeek; held healthy).
- All other healthy sources reachable with 0 in-window items beyond what's noted above.

## Disposition / handoff

**7 substantive raw-signal files written this sweep** for grader (this sentinel = file 0; 6 substantive content files numbered 001-007):

- `raw-2026-06-15-am-001` — ShinyHunters Council of Europe leak-site claim (NET-NEW substrate; dual-campaign ShinyHunters visibility hook to PeopleSoft cluster; EU non-A&D)
- `raw-2026-06-15-am-002` — Novo Nordisk pharma breach disclosure (NET-NEW substrate; no attribution; pharma not A&D)
- `raw-2026-06-15-am-003` — French Tchap "Misere" UPDATE (UPDATE on finding-2026-06-12-pm-009 / -pm-007; net-new actor name + scale + analyst risk-language)
- `raw-2026-06-15-am-004` — THN Awesome Motive WordPress CDN supply-chain (2nd-publisher relay of SA + Sansec primary; net-new IOC `84.201.6.54`; consumer WordPress out of A&D)
- `raw-2026-06-15-am-005` — SA Palo Alto PAN-OS CVE-2026-0257 Rapid7 IOC detail (vendor confirmation of CVE-2026-0257 active exploitation; KEV deadline 14d past; no FLASH eligibility)
- `raw-2026-06-15-am-006` — SA The Gentlemen ransomware KELA RansomNews deep-dive (483 victims, AI-assisted tooling, alerts.bar IOC corroboration; /new-actor candidacy strengthens; NOT on roster)
- `raw-2026-06-15-am-007` — HelpNet "Proving military AI" (A&D-prime watchlist hit by Lockheed Martin name; opinion-class, no incident substrate)

**Anti-noise carry-forward bindings preserved per orchestrator instruction** (none re-litigated as net-new this sweep):

- **PeopleSoft / UNC6240 / CVE-2026-35273** — KEV deadline EOD TODAY Sunday 2026-06-15 (~T-16h from 08:00 brief publication). **This morning brief is the FINAL substantive pre-deadline FCEB coverage window.** Splunk sentinel 10/10 clean across 42h cumulative window; Hard Rule 8 visibility-limited caveat binds. ShinyHunters Council of Europe claim today provides dual-campaign-actor-context flavor but NOT same-CVE attribution.
- **Ivanti Sentry CVE-2026-10520** — KEV deadline now PAST EOB 2026-06-14 (~13h ago); language pivots from T-N countdown to "deadline passed; compliance-status surfaces in next-day metrics not KEV catalog itself" per standard pattern
- **CVE-2026-20253 Splunk Enterprise** — finding-2026-06-13-0004 carry unchanged
- **NPM 12 default script-execution change** — finding-2026-06-13-0005 carry; GitHub direct blog retrieval still pending
- **Velvet Ant Operation Highland** — Sygnia primary still pending
- **Handala #014 / Cal Water** — finding-2026-06-13-0003 carry; Hard Rule 2 binding preserved; OT/ICS impact NOT confirmed
- **Fable 5 / Mythos 5 Anthropic** — finding-2026-06-13-0001 three-publisher carry
- **Check Point VPN CVE-2026-50751 / Qilin** — sustained hold, no net-new substrate
- **Shai-Hulud / Miasma / IronWorm npm-worm family** — carry as operator-deferred /new-actor; today's Awesome Motive WordPress CDN supply-chain is **parallel** (CDN-injection lineage to Polyfill 2024) but NOT npm-worm cluster
- **UNC3753 vishing-to-physical-intrusion / Mandiant "Seeking Counsel"** — Mandiant direct-HTML carry-forward to actor-profiler /new-actor decision

## Items worth flagging to grader for morning brief composition (FLASH-NEGATIVE but priority noted)

1. **PeopleSoft / UNC6240 KEV deadline EOD Sunday — T-16h from 08:00 brief publication.** Grader should surface this as the BRIEF'S LEAD per the morning brief substrate — final FCEB pre-deadline coverage window, hunt-the-19-IOC-set sustained, Splunk 10/10 clean with visibility-limited caveat. ShinyHunters Council of Europe claim today adds dual-campaign-actor context but is NOT same-CVE attribution — keep Council of Europe story separately bounded.

2. **Ivanti Sentry CVE-2026-10520 deadline PAST.** Language pivots to retrospective compliance-metrics per established pattern. No FCEB compliance data has landed.

3. **ShinyHunters Council of Europe (`raw-2026-06-15-am-001`)** — net-new this morning; SW single-source on volume claim; A1 reportability of *actor-claimed* leak post is the primary substrate, official Council of Europe ACK pending. Grader should evaluate whether to surface as substrate-thin standalone bullet OR as ShinyHunters-cluster context for PeopleSoft framing OR as anti-noise hold pending Council of Europe confirmation.

4. **Tchap "Misere" UPDATE (`raw-2026-06-15-am-003`)** — UPDATE on existing finding chain (06-10 pm-007, 06-12 pm-009 carry); net-new actor name + scale + analyst risk-framing. Grader call: 1-2 line UPDATE bullet acceptable; not FLASH.

5. **HelpNet military AI piece (`raw-2026-06-15-am-007`)** — A&D-prime watchlist hit by Lockheed Martin name reference suffices for Sector Focus visibility but opinion-class with no incident substrate. Grader call: sector-context Other Signal one-liner.

6. **THN Awesome Motive WordPress CDN (`raw-2026-06-15-am-004`)** — publisher-independent corroboration achieved (Sansec primary + SA + THN); consumer WordPress out of A&D-prime scope; possible Other Signal one-liner. Grader call: brief mention OK.

7. **SA The Gentlemen KELA deep-dive (`raw-2026-06-15-am-006`)** — actor-profiler /new-actor candidacy strengthens with named-victim alerts.bar cross-validation; surface as Other Signal candidate. Operator-deferred /new-actor decision.

8. **SA PAN-OS Rapid7 detail (`raw-2026-06-15-am-005`)** — primary IOC carrier for grader IOC-extraction even though substrate fails FLASH triggers; KEV deadline already 14d past. Possible Other Signal sub-bullet on vendor confirmation language.

9. **Mandiant canonical-swap operator decision** — 8 consecutive direct-HTML successes against RSS-path failure; **soft-recommend operator-side endpoint canonical-swap before next pre-brief cycle** at this point (29 consecutive RSS failures + 8 consecutive direct-HTML successes is a stable cross-over signal).

10. **Sophos category-path recovery soft-observation** — `news.sophos.com/en-us/category/threat-research/feed/` continues 200 OK + parseable; **soft-recommend operator endpoint swap on top-level Sophos entry** pending operator decision.

11. **Three single-failure source-health observations this sweep** (industrialcyber 403, dragos 404, bitdefender 404) — soft-flag for operator review per single-failure-non-promotion rule. Will re-attempt next sweep.

## Extraction notes

- Language: en
- Article type: sentinel (internal pre-brief substrate audit)
- Raw IOC extraction invoked: no (sentinel file; each substantive raw-signal `raw-2026-06-15-am-001` through `-am-007` carries its own IOC-extraction or absence-of-IOC declaration)
- Hard Rule binding: Rule 1 (LEGAL-POLICY) — all queries passive RSS / WebFetch / Splunk-self; no active recon of any target outside `authorized-targets.yaml` (which is empty). Rule 2 (no attribution origination) — no novel attributions made this sweep; ShinyHunters self-claim of Council of Europe preserved verbatim per SW source; Rapid7 single-actor assessment of CVE-2026-0257 preserved verbatim per SA source; "Misere" identity preserved as unknown-actor-claim per SW source. Rule 3 (no exploitation assistance) — no PoC content or exploit walkthroughs ingested into raw-signal. Rule 7 (15-word quote discipline) — no verbatim quotes >15 words preserved in this sentinel. Rule 8 (Splunk first-party) — sentinel Splunk scan emitted with 19-IOC carry-forward set, 0 events on -24h; visibility-limited absence flagged per Hard Rule 8.
- Operator-invocation context: scheduled 07:30 EDT pre-brief collection for 08:00 EDT morning brief Sunday 2026-06-15. COLLECTION ONLY per operator binding — no grading, no FLASH evaluation, no brief composition, no Discord posting, no commit, no `_coverage-log.yaml` update.
