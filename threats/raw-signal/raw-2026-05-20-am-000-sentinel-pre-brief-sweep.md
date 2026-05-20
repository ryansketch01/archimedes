---
raw_id: raw-2026-05-20-am-000
collected_at: 2026-05-20T07:30:00-04:00
run_id: pre-brief-20260520-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: multi
  source_name: "Multi-source pre-brief sweep (07:30 EDT Wednesday)"
  source_url: null
  published_at: null
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: []
triage_tags:
  - sentinel
  - pre_brief_sweep_summary
  - scheduled_0730_window
  - non_promotable
  - 3_items_raw_signaled_am_001_am_002_am_003
  - flash_0600_carry_forward_teampcp_github_corp_breach
  - splunk_first_party_zero_hits_48th_consecutive_dormant_sweep
  - kev_zero_new_entries_since_2026_05_15
  - cisa_advisories_all_xml_zero_in_window
  - mandiant_feedburner_404_carry_forward_known_failure
  - dragos_feed_404_carry_forward
  - msrc_blog_feed_parse_failure_carry_forward
  - google_ti_rss_parse_failure_carry_forward
  - the_record_zero_in_window
  - recordedfuture_blog_zero_in_window
  - mstic_zero_in_window
  - sentinelone_zero_in_window
  - sophos_zero_in_window
  - eset_welivesecurity_zero_in_window
  - krebs_zero_in_window
  - crowdstrike_10_items_no_published_timestamps_marketing_filtered
  - unit42_tampered_chef_no_ad_no_roster_actor_discarded
  - bleepingcomputer_pintheft_arch_linux_poc_non_ad_discarded
  - nvd_3_criticals_seppmail_anti_noise_rclone_glib_non_ad_discarded
iocs_extracted: false
iocs_count: 0
text_word_count: 750
promoted: false
ttl_expires_at: 2026-08-18T07:30:00-04:00
test: false
---

# Pre-brief collection sweep — 2026-05-20 07:30 EDT (Wednesday)

Wednesday morning pre-brief collection. Time window: 2026-05-19T15:30 EDT to 2026-05-20T07:30 EDT (14 hours).

## Sweep outcome

**3 raw-signal files written** plus carry-forward from 2026-05-20 06:00 FLASH (TeamPCP/GitHub-corp breach, raw-2026-05-20-flash-0600-001, already promoted to finding-2026-05-20-FLASH-0001).

### Raw-signaled this sweep (3)

1. **raw-2026-05-20-am-001** — SecurityWeek Mini Shai-Hulud 320+ npm @antv namespace expansion; TeamPCP "suggesting" attribution at moderate-hedge confidence; Python-downloader + Claude Code backdoor TTP additions. Tracked actor (TeamPCP #001 HIGH). Tracked vuln (VT-006 / CVE-2026-45321). **Topic-distinct from 06:00 FLASH GitHub-corp breach** but campaign-chain-adjacent. No A&D-prime named.

2. **raw-2026-05-20-am-002** — BleepingComputer (Bill Toulas) relay of Microsoft Security Blog 2026-05-18: Storm-2949 SSPR/MFA-manipulation/Graph-enum/OneDrive-SharePoint-exfil/Key-Vault/Defender-disablement TTP chain against M365 + Azure production environments. Storm-2949 NOT in `_roster.yaml`. No A&D prime named. Awareness flag for orchestrator: candidate /new-actor evaluation if cross-corroborated or re-classified.

3. **raw-2026-05-20-am-003** — Microsoft mitigation publication for YellowKey BitLocker bypass (CVE-2026-45585, CVSS 6.8). PoC public, no in-the-wild claim. Nightmare Eclipse researcher lineage (BlueHammer ZD-001 + RedSun ZD-002 + UnDefend ZD-003 + GreenPlasma + YellowKey — 5-zero-day cluster). Actionable mitigation: TPM+PIN reconfiguration via Intune/GPO. Vuln-tracker handoff candidate.

### In-window items DISCARDED per Mode 1 procedure (no watchlist / roster / vuln-index hit)

- **Unit 42 — Tracking TamperedChef Clusters via Certificate and Code Reuse** (Joseph Ganter, 2026-05-20T10:00 UTC). Trojanized PDF/converter productivity apps, CL-CRI-1089 + CL-UNK-1090 + CL-UNK-1110 clusters. No roster actor (Microsoft Storm-class would not apply here either). No A&D sector targeting. VT-confirmed malicious IOCs (onezipapp.com 7/91, crystalpdf.com 13/91) — but the actor is not tracked and there's no A&D-prime named. DISCARDED.

- **BleepingComputer — Exploit released for new PinTheft Arch Linux root escalation flaw** (Sergiu Gatlan, 2026-05-20T10:52 UTC). Linux LPE PoC, Arch-specific. No A&D-prime targeting. No tracked actor. Patched class. DISCARDED.

- **NVD lastModified Critical window query 2026-05-19T19:30Z → 2026-05-20T11:30Z (CVSS Critical):**
  - **CVE-2025-14087** (GNOME GLib GVariant parser buffer-underflow, CVSS 9.8) — Linux desktop library, no A&D-specific exposure path. DISCARDED.
  - **CVE-2026-2743** (SeppMail file transfer path traversal RCE, CVSS 9.8) — SeppMail-secure-email-gateway 7-CVE cluster already raw-signaled at raw-2026-05-19-am-004 (anti-noise locked, same parent advisory). DISCARDED (anti-noise).
  - **CVE-2026-41179** (Rclone REST API unauthenticated RCE, CVSS 9.8) — patched in 1.73.5 (2026-04-19), NVD modification is metadata refresh on already-patched CVE. No active exploitation claim. DISCARDED.

- **SecurityWeek — Verizon DBIR 2026: Vulnerability Exploitation Overtakes Credential Theft** (Ionut Arghire, 2026-05-20T00:04 UTC). Sector report. A&D not specifically named at headline level. Aggregate-tier reporting, not finding-class signal. DISCARDED (potential brief-context use by briefer).

- **BleepingComputer — Discord rolls out end-to-end encryption** (2026-05-19T20:37). Vendor product announcement. DISCARDED.

- **BleepingComputer — FBI: Americans lost over $388 million to scams using crypto ATMs in 2025** (2026-05-19T19:45). Consumer fraud reporting. DISCARDED.

- **SecurityWeek — Caught Off Guard: Securing AI After It Hits Production** (Joshua Goldfarb, 2026-05-20T11:00). Opinion piece. DISCARDED.

- **SecurityWeek — Real-World ICS Security Tales From the Trenches** (Eduard Kovacs, 2026-05-20T10:15). Aggregated interview piece, no fresh finding. DISCARDED.

- **SecurityWeek — Virtual Event Today: Threat Detection & Incident Response Summit** (2026-05-20T10:00). Marketing post. DISCARDED.

- **The Hacker News — Typosquatting Is No Longer a User Problem. It's a Supply Chain Problem** (2026-05-20T10:30). Opinion-essay format, no fresh finding. DISCARDED.

- **The Hacker News — Grafana GitHub Breach Exposes Source Code via TanStack npm Attack** (2026-05-20T05:12). Investigation update on Grafana 2026-05-16 breach, part of TeamPCP campaign chain — already addressed as campaign-chain context in raw-2026-05-20-flash-0600-001 § Secondary in-window items. DISCARDED (anti-noise / campaign-chain absorbed).

- **CrowdStrike feed** — 10 items returned, all `published: null` (no in-window timestamps available in feed). Top titles are product/marketing posts (Falcon AIDR, Falcon Shield/CORDIAL+SNARKY SPIDER, Magic Quadrant CTI Leader, ChatGPT Enterprise integration, May 2026 Patch Tuesday recap). 15th consecutive sweep with this pattern; no threat-intel content surfaced. DISCARDED.

- **Recorded Future blog feed** — 0 items in 14h window. No fresh content.

- **Sophos News Threat Research feed** — 0 items in 14h window. No fresh content.

- **WeLiveSecurity (ESET)** — 0 items in 14h window. No fresh content.

- **SentinelOne blog feed** — 0 items in 14h window. No fresh content.

- **SANS ISC** — 1 item (StormCast podcast detail 2026-05-20T02:00 UTC — awareness-only podcast detail, no body content). DISCARDED.

- **MSTIC (Microsoft Security Blog parent feed)** — 0 items in 14h window. No fresh content (the Storm-2949 / SSPR Microsoft Security Blog post 2026-05-18 was relayed by BleepingComputer in-window — captured at raw-2026-05-20-am-002 — but the MSTIC parent feed itself did not surface a new post in the 14h window).

- **The Record (Recorded Future News)** — 0 items in 14h window. No fresh content.

- **Krebs on Security** — 0 items in 14h window. No fresh content.

- **CISA Advisories all.xml** — 0 items in 14h window after since-filter. No fresh advisories.

- **CISA KEV JSON** — 0 new entries since 2026-05-15 (CVE-2026-42897 Exchange Server OWA XSS most recent). 5d carry-forward.

### Source-health observations

**Sources with NEW failures this sweep:** None.

**Sources with PERSISTENT carry-forward failures (no source-health change required this sweep):**
- Mandiant `feeds.feedburner.com/Mandiant` — 404 (~21st consecutive failure; operator alt-endpoint decision still pending).
- Dragos `dragos.com/blog/feed/` — carry-forward (failure_count=1; below ≥2 stale threshold).
- MSRC blog feed — XML parse failure carry-forward.
- Google Cloud Threat Intelligence RSS — XML parse failure carry-forward.
- Volexity feed — XML parse failure carry-forward.

**Sources with successful in-window fetches:**
- BleepingComputer (9 items in window)
- The Hacker News (4 items in window)
- SecurityWeek (6 items in window)
- Unit 42 (1 item)
- SANS ISC (1 item)
- MSTIC parent feed (0 items, reachable)
- The Record (0 items, reachable)
- Krebs (0 items, reachable)
- CISA Advisories all.xml (0 items, reachable)
- CISA KEV JSON (0 new entries, reachable)
- Sophos Threat Research (0 items, reachable)
- WeLiveSecurity (0 items, reachable)
- SentinelOne (0 items, reachable)
- Recorded Future blog (0 items, reachable)
- CrowdStrike (10 items but no timestamps, reachable)

## Splunk first-party check (Hard Rule 8)

Targeted IOC keyword sweep across `archimedes` + `defenseclaw_local` indexes over -24h: zero non-Archimedes-internal events. tstats inventory: archimedes:operation (22), archimedes:scheduler (15), archimedes:brief (1) — all Archimedes-internal pipeline events. **48th consecutive sweep with dormant non-self-telemetry stream pattern.**

## FLASH-trigger evaluation across all in-window items

- **Trigger 1 (critical CVE + active exploitation + A-grade):** No new in-window CVE met all three conditions. KEV no new entries. NVD lastModified Criticals (SeppMail / Rclone / GLib) all fail active-exploitation gate.
- **Trigger 2 (new attribution for tracked actor):** FLASH 0600 already fired on TeamPCP GitHub-corp breach (T2 PRIMARY). SecurityWeek Mini Shai-Hulud @antv expansion is a RESTATEMENT of existing TeamPCP attribution, not a new attribution — does not fire.
- **Trigger 3 (first-party Splunk IOC hit):** Dormant. Does not fire.
- **Trigger 4 (tracked actor TTP change):** FLASH 0600 already fired on TeamPCP GitHub-corp breach (T4 SECONDARY). SecurityWeek Mini Shai-Hulud @antv Python-downloader + Claude Code backdoor claim is a CANDIDATE TTP delta, but single-source originating (no Wiz/Snyk/Socket cross-corroboration in window) — grader assessment whether single-source veto applies. Conservatively does not fire as standalone FLASH; will absorb into morning brief.
- **Trigger 5 (A&D-sector multi-victim active campaign):** No A&D-prime victim named in any in-window surface. Does not fire.
- **Trigger 6 (zero-day no patch + CVSS≥8.0 + exploitation confirmed/imminent):** YellowKey CVE-2026-45585 is CVSS 6.8 (below 8.0 floor); PoC public but no in-the-wild claim. Does not fire.

**Pre-brief disposition: no fresh FLASH from this sweep. The 06:00 FLASH on TeamPCP/GitHub-corp breach remains the active FLASH; quiet hours queue catchup at 09:00 — likely superseded by the 08:00 morning brief.**

## Disposition

Sentinel file written for audit-trail completeness. 3 raw-signal items handed off to grader. Source-health.yaml runtime fields will be updated to reflect last_successful_fetch on the productive sources. No new failures introduced this sweep.
