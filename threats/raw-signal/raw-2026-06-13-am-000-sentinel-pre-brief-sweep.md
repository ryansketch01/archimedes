---
raw_id: raw-2026-06-13-am-000
collected_at: 2026-06-13T07:34:00-04:00
run_id: pre-brief-20260613-073000
collection_mode: pre_brief_collection
sources:
  - source_yaml_id: collector_sentinel
    source_name: Archimedes Collector (sentinel sweep)
    source_url: null
    published_at: 2026-06-13T07:34:00-04:00
match_reason:
  watchlist: [sentinel_sweep_record]
  actors: []
  vulnerabilities: []
  keywords: [sentinel, pre_brief_collection, splunk_first_party_sweep, source_health_audit]
triage_tags: [sentinel_only, no_finding_promotion, audit_trail]
iocs_extracted: false
iocs_count: 0
text_word_count: 530
promoted: false
ttl_expires_at: 2026-09-11T07:34:00-04:00
flash_trigger_evaluation:
  flash_eligible: false
  notes: "Sentinel raw-signal documenting the 07:30 pre-brief sweep. Records sweep scope, source-health observations, Splunk sentinel result, and triage-tag inventory for the 4 substantive raw-signal files written this sweep."
---

# Pre-brief Collection Sweep — 2026-06-13 07:30 EDT

## Scope

- **Mode:** pre_brief_collection
- **Run ID:** pre-brief-20260613-073000
- **Window:** 2026-06-12T17:30:00-04:00 → 2026-06-13T07:30:00-04:00 (14 hours)
- **Trigger:** Scheduled 07:30 EDT pre-brief for 08:00 morning brief
- **Prior FLASH sweeps in window:** 18:00 (commit 7f5f407, clean), 00:00 (commit 1445988, clean), 06:00 (commit 6f45f5e, clean — Anthropic Fable 5 / Mythos 5 trigger-evaluated NEGATIVE and deferred to this pre-brief per audit-trail)

## Sweep summary

- **Sources queried:** 22 RSS / WebFetch endpoints (heavy-priority subset of the 55-healthy active source set; full health audit in source-health.yaml updates)
- **Splunk first-party sweep:** 1 query against archimedes + defenseclaw_local, -24h, against 50-token watchlist (3 actors + 22 IPs/domains + 18 CVE / actor / watchlist tokens)
- **Items fetched matching watchlists/roster/vulnerability index:** 4 (across 5 sources)
- **Raw-signal files written:** 4 substantive + 1 sentinel (this file)
- **Source-health changes:** 4 (volexity stale-persistent ++, mandiant stale-persistent ++, lumen parse-error second-failure → STALE FLIP, shadowserver 404 second-failure → STALE FLIP)
- **Sources hard-down:** 0 new beyond prior tracked state
- **FLASH-eligible items:** 0 (all carry-forward; anti-noise locks topics from yesterday's afternoon brief / prior FLASH sweeps)

## Substantive raw-signal files written

| File | Topic | Triage tags |
|---|---|---|
| raw-2026-06-13-am-001 | Anthropic Fable 5 / Mythos 5 USG export-control suspension (BleepingComputer + THN + SecurityWeek/AP) | usg_export_control_action, ai_tooling_supply_chain, three_publisher_convergence, carry_forward_anthropic_ai_export |
| raw-2026-06-13-am-002 | Mandiant + GTIG attributes Oracle PeopleSoft CVE-2026-35273 zero-day exploitation to UNC6240 (ShinyHunters); full IOC set; 100+ orgs notified; 68% higher-ed; University of Nottingham confirmed; 455k HIBP-indexed records | carry_forward_corroboration_NEW_MANDIANT_PRIMARY, new_attribution_unc6240_shinyhunters, ioc_set_NEW, candidate_for_finding_update |
| raw-2026-06-13-am-003 | Handala / Cal Water — SecurityAffairs second-publisher relay of Dataminr analysis; 2M-customer figure; explicit retaliation-for-US-actions-in-Iran motive; Stryker incident precedent | iran_cyber_us_targeting, tracked_actor_handala_014, second_publisher_corroboration |
| raw-2026-06-13-am-004 | NanoClaw + JFrog vetted-registry integration (vendor announcement) — extends developer/AI-tooling supply-chain cluster | vendor_announcement_not_incident, ai_tooling_supply_chain_cluster_extends, commentary_quality_thought_leadership |

## Splunk first-party sentinel (Hard Rule 8)

- **Query:** metadata sourcetypes inventory NOT sourcetype=archimedes:* over -24h → 0 non-archimedes-internal events across both indexes
- **Watchlist IOC sweep:** 5 hits across `azurenetfiles.net OR "176.120.22.24" OR meshagent OR ShinyHunters OR UNC6240 OR Handala OR "Cal Water" OR RTKBase OR NTRIP OR Velvet Ant OR UNC1549 OR Charming Kitten OR MuddyWater OR Salt Typhoon OR Volt Typhoon OR APT28 OR APT29 OR [13 watchlist companies] OR CVE-2026-35273 OR CVE-2026-10520 OR CVE-2026-10523 OR Fable OR Mythos OR Anthropic OR PeopleSoft OR LangGraph` over -24h. **All 5 hits are Archimedes' own pipeline emissions** (3x flash_sweep events from 18:00/00:00/06:00; 1x source_grades_updated for the 5 provisional adds from yesterday's PM cycle; 1x brief_published for 2026-06-12-afternoon).
- **Disposition:** Trigger 3 (first-party-ioc-hit) NEGATIVE. Defenseclaw_local 13th consecutive sweep with dormant non-archimedes-internal stream pattern.

## Source-health observations (full updates in source-health.yaml)

### Stale-persistent (no change to status; failure_count incremented)

- **volexity:** XML parse error line 17 col 68 (6th consecutive); failure_count 5 → 6 stale-persistent
- **mandiant:** RSS XML syntax error at line 2 col 0 (25th consecutive); failure_count 24 → 25 stale-persistent

### New stale flips this sweep

- **lumen:** XML parse error line 26 col 4 mismatched tag — SECOND consecutive failure (first was 2026-06-12 12:00 FLASH); failure_count 1 → 2 — STALE FLIP. last_error updated.
- **shadowserver:** shadowserver.org/feed/ returned 404 — SECOND consecutive failure (first was 2026-06-12 12:00 FLASH); failure_count 1 → 2 — STALE FLIP. last_error updated.

### Skipped per stale-under-24h rule or known degraded state

- **trellix:** 403 bot-shield known; not retried this sweep
- **blackberry:** XML mismatched tag (parse error single-shot, not tracked at top level)
- **cisco-talos:** 200 OK / RSS reachable but 0 items in window
- **sentinelone:** 200 OK / RSS reachable but 0 items in window
- **bitdefender:** 200 OK / RSS reachable but 0 items in window
- **rapid7:** 1 item in window (Metasploit weekly update, no security signal for finding promotion)
- **wired:** 1 item in window (security roundup mentioning ShinyHunters/Oracle PeopleSoft as sub-item — captured under raw-2026-06-13-am-002 cluster, no separate file)

### Successfully fetched this sweep

bleepingcomputer, thehackernews, securityweek, theregister, securityaffairs, cisa-advisories (all.xml path), unit42, crowdstrike (no in-window dated items), microsoft msrc (0 items, pre-existing stale state unchanged), proofpoint, rapid7, isc.sans.edu (0 items), darkreading (1 item, contest non-security), checkpoint, recorded-future, helpnetsecurity, wired, arstechnica, krebs (0 items), therecord (0 items), welivesecurity (0 items)

## Anti-noise / carry-forward inventory

- Oracle PeopleSoft CVE-2026-35273 KEV add — already covered yesterday afternoon (finding-2026-06-12-pm-001). NEW Mandiant + GTIG attribution + IOCs collected this sweep as UPDATE candidate.
- Ivanti EPMM CVE-2026-10520 honeypot-only — already covered (finding-2026-06-12-pm-002). No new reporting this sweep. CVE-2026-10523 companion auth bypass — STILL NOT ADDRESSED in any source this sweep. Flag for vuln-tracker follow-on if not surfaced by 16:00 afternoon pre-brief.
- Handala / Cal Water — second-publisher SecurityAffairs relay collected this sweep (raw-2026-06-13-am-003). Cal Water acknowledgment still absent.
- Sygnia / Velvet Ant — no new reporting this sweep. /new-actor handoff still pending Sygnia primary direct retrieval.
- AUR / Sonatype — no new reporting this sweep.
- Tenet Security Agentjacking — no Sentry policy update or Anthropic/Cursor advisory this sweep. Adjacent NanoClaw + JFrog vendor announcement collected (raw-2026-06-13-am-004) as defensive-architecture counterpoint.
- LangGraph 3-CVE chain — no new exploitation reports this sweep.
- Google v. Outsider Enterprise — no civil case progression this sweep.
- IBM/AT&T Barlow qui tam — no DOJ statement this sweep.
- Anthropic Fable 5 / Mythos 5 — collected this sweep (raw-2026-06-13-am-001) per FLASH 06:00 deferral.

## Hard rule compliance

- Hard Rule 1 (LEGAL-POLICY): all sweep activity was passive OSINT (RSS / WebFetch). No active scanning. authorized-targets.yaml empty.
- Hard Rule 2 (no novel attribution): UNC6240 attribution preserved verbatim from Mandiant per raw-2026-06-13-am-002. No attribution upgrades.
- Hard Rule 3 (no exploit content): shell command sequences from Mandiant's `.bash_history` reconstruction summarized at operational-metadata level only; no PoC content.
- Hard Rule 6 (15-word quote limit): flagged for briefer trim in raw-2026-06-13-am-001 (Anthropic Red Team quote at 24 words) and raw-2026-06-13-am-003 (Dataminr quotes at 30 words) and raw-2026-06-13-am-004 (Cohen quote at 50 words). Briefer to paraphrase.
- Hard Rule 7 (credentials radioactive): Handala dump credential exposure recorded as categories + counts only. Zero credential values stored.
- Hard Rule 8 (Splunk first-party priority): sweep executed; 0 non-archimedes-internal events; 0 IOC hits across watchlist.
