---
raw_id: raw-2026-06-12-pm-000
collected_at: 2026-06-12T15:32:00-04:00
run_id: pre-brief-20260612-153000
collection_mode: pre_brief_collection
sentinel: pre_brief_sweep
window_start: 2026-06-12T07:30:00-04:00
window_end: 2026-06-12T15:32:00-04:00
sources_queried: 17
sources_with_in_window_items: 8
sources_with_parse_errors: 4
items_fetched: ~38
items_matching_watchlists: 13
raw_signal_files_written: 9
splunk_first_party_hits: 0
triage_tags: [sentinel, pre_brief_sweep, productive]
ttl_expires_at: 2026-09-10T15:32:00-04:00
---

# Pre-brief sweep 15:30 EDT 2026-06-12 — productive (9 raw-signal files)

## Window

This sweep covers the ~8h window from the 07:30 EDT morning pre-brief (which covered 17:30 EDT 06-11 → 07:30 EDT 06-12) through 15:32 EDT 06-12. The 12:00 FLASH sentinel (~18h overnight catchup) ran cleanly with 0 candidates and is fully captured in raw-2026-06-12-flash-1200-000.

Effective new-content window for this pre-brief: 12:04 EDT 06-12 → 15:32 EDT 06-12 (~3.5h since the 12:00 FLASH closed), plus any in-window items the 12:00 sentinel deferred to this pre-brief (Cal Water / Handala; AI-tooling cluster; Tchap 73k; Ivanti honeypot UPDATE; etc.).

## Sources canvassed and disposition

**Healthy with productive content:**
- BleepingComputer — 7 in-window items since 12:04 EDT
- The Hacker News — 5+ in-window items since 12:04 EDT
- SecurityWeek — 6+ in-window items today including Cal Water (07:30 EDT) + Ivanti honeypot UPDATE (05:44 EDT) + In Other News column (16:17 UTC = 12:17 EDT) + Chrome 149 (05:27 EDT)
- The Record — 3 in-window items since 12:00 (23andMe settlement, FISA 702 lapse, Coupang fine)
- Help Net Security — 2 in-window items (Google Gemini lawsuit, watchTowr Check Point PoC)
- Tenable Blog — BOD 26-04 FAQ (carry-forward from 12:00 sweep)
- watchTowr Labs — CVE-2026-50751 deep-dive (carry-forward from 12:00 sweep)
- SANS ISC — Stormcast podcast detail only

**Healthy, 0 items in window:**
- Krebs on Security
- Unit 42 (feedburner reachable, last post 2026-06-11 pre-window)
- MSTIC parent feed
- Mandiant alt-path (mandiant.com/resources/blog/rss.xml)
- Cisco Talos
- ESET WeLiveSecurity
- CISA Advisories all.xml

**Source-health degraded this sweep (no flips):**
- Volexity blog RSS — XML parse error (recurrent, already stale since 06-11)
- Lumen blog RSS — XML parse error (failure_count=1, held healthy from 12:00 sweep)
- Shadowserver /feed/ — 404 (failure_count=1, held healthy from 12:00 sweep)
- Trellix newsroom RSS — 403 bot-shield (known pattern, no new degradation)

CISA KEV: **1 NEW addition today (2026-06-12)** — CVE-2026-35273 Oracle PeopleSoft PeopleTools added with dueDate 2026-06-15 (3-day BOD-26-04 clock), `knownRansomwareCampaignUse: Known`. State transition for ShinyHunters/PeopleSoft case from yesterday's mitigations-only.

## In-window items raw-signaled (9 files including this sentinel)

| File | Topic | A&D? | Notes |
|---|---|---|---|
| pm-001 | CISA KEV addition: Oracle PeopleSoft CVE-2026-35273 + ransomware-use tag + 3-day clock | indirect | UPDATE on FLASH 06-11-1200 + 06-11-afternoon |
| pm-002 | Ivanti Sentry CVE-2026-10520 — vendor clarifies honeypot-only exploitation triggered KEV | indirect | UPDATE softens "mass" hedge — validates morning's caution |
| pm-003 | Handala claims Cal Water hack — 5GB customer PII + RTKBase credentials | Iran Cyber Watch | Roster actor #014; water utility NOT A&D |
| pm-004 | Sygnia Velvet Ant — PAM/OpenSSH backdoor, ~10y dwell, East Asia victim | structural | China-nexus; air-gapped network; not a roster actor |
| pm-005 | 400+ Arch Linux AUR packages compromised — Sonatype "Atomic Arch" | structural | Developer-tier supply chain, dev environment exposure |
| pm-006 | Google v. Outsider Enterprise — Chinese smishing PhaaS + Gemini AI weaponization | structural | AI-tooling weaponization cluster |
| pm-007 | AI-tooling cluster — LangGraph CVEs + Agentjacking + Tenet research | indirect | First confirmed agent-execution-flow attack on Claude Code / Cursor |
| pm-008 | Bloomberg-broken IBM/AT&T whistleblower lawsuit (W. Barlow) — alleges federal-contract hack cover-ups | A&D-direct | Federal-contractor disclosure violation; 2020 sealed, unsealed 06-04 |
| pm-009 | Tchap victim count firmed at 73,000 French gov employees | structural | UPDATE on raw-2026-06-10-pm-007 |

## In-window items NOT raw-signaled (filtered before raw-signal)

- BleepingComputer "phpBB forum fixes auth bypass bug lurking for a decade" (2026-06-12T18:19 UTC) — open-source forum software, no A&D / roster / tracked vuln; not a CVE assignment in our index; DISCARDED.
- BleepingComputer "Ukrainian national pleads guilty to role in Conti ransomware operation" (2026-06-12T17:54 UTC) — Conti was disbanded 2022; LE follow-on with no A&D-prime victim named, no tracked-actor lift; awareness only; DISCARDED.
- The Record "Bankruptcy admin approves settlement fund of $47 million for 23andMe data breach victims" (2026-06-12T17:12 UTC) — historic breach class-action settlement; DISCARDED.
- The Record "Major US surveillance program poised to lapse after legislative deadlock" (2026-06-12T17:08 UTC) — FISA Section 702 — important policy but NOT a CTI finding; flagged for orchestrator awareness, NOT raw-signaled.
- The Record "South Korea hits Coupang with record $409 million fine over data breach" (2026-06-12T15:56 UTC) — regulatory fine on Korean e-commerce, NOT A&D-prime; DISCARDED.
- SecurityWeek "In Other News" column also covered: Bitsight ICS exposure flat at 170,000 monthly exposures (ICS structural awareness, no specific CVE / actor / victim — DISCARDED at raw-signal layer but feeds Threat Detection Weekly synthesis); Microsoft incident response playbook for AI (defensive vendor doc — DISCARDED).
- Help Net Security CVE-2026-50751 PoC release (watchTowr) — anti-noise locked, covered in 12:00 FLASH sentinel and prior corpus; the watchTowr deep-dive may feed Threat Detection Weekly but NOT a fresh raw-signal trigger.

## Splunk first-party sentinel (-8h, defenseclaw_local + archimedes)

Both indexes queried for non-archimedes-internal events: **0 events** over the 8h window. Targeted CVE/actor keyword sweep (CVE-2026-10520, CVE-2026-35273, CVE-2026-5027, CVE-2026-50751, CVE-2026-11645, CVE-2026-7473, CVE-2026-20245, Handala, ShinyHunters, "Velvet Ant", "Cal Water", Tchap, RTKBase) returned 2 hits over 24h — both archimedes:operation / archimedes:brief pipeline self-references (flash_sweep_clean event from 06-11 18:00 + brief_published event for 06-11 afternoon).

Trigger 3 (first-party Splunk IOC hit) — NOT triggered.

## Source-health changes to persist (for librarian)

- All healthy productive sources (bleepingcomputer, the-record, securityweek, thehackernews, helpnetsecurity, sans-isc, krebs, unit42, mstic, mandiant alt-path, cisco-talos, cisa-advisories, cisa-kev, nvd) — advance `last_successful_fetch` to 2026-06-12T15:32:00-04:00.
- volexity — STALE (failure_count already 3 from 12:00 sweep, recurrent parse error this sweep — failure_count++ to 4; status unchanged).
- lumen — failure_count holds at 1 (held healthy; no new parse attempt this sweep; carries from 12:00 sweep).
- shadowserver — failure_count holds at 1 (held healthy; alt-endpoint investigation pending).
- trellix — 403 (known bot-shield; no top-level entry to update).

No status flips this sweep.

## Priority handoffs for 16:00 afternoon brief composition

1. **CVE-2026-35273 CISA KEV addition + ransomware-campaign-use tag (pm-001)** — material state transition from yesterday's afternoon brief; lifts the "limited" framing from ZDI Childs into federal procedural attestation; ShinyHunters self-claim now anchored by `knownRansomwareCampaignUse: Known` federal disposition. Hard Rule 2 binding: CISA does NOT name ShinyHunters as the ransomware-use actor explicitly; the campaign-use tag is procedural per KEV taxonomy.
2. **Ivanti Sentry honeypot-only UPDATE (pm-002)** — Ivanti now clarifies the KEV listing was triggered by honeypot exploitation, NOT production systems. Material softening of yesterday's afternoon "mass" framing; validates the red-team carry-forward hedge.
3. **Cal Water / Handala (pm-003)** — Iran Cyber Watch standing section primary content for the afternoon brief.
4. **Sygnia Velvet Ant (pm-004)** — China-attributed, deeply structural; flag for Sector Focus or Other Signal — NO roster cross-walk to APT41 / Volt Typhoon / Salt Typhoon per Hard Rule 2.
5. **AI-tooling cluster (pm-007)** — Tenet Security's Agentjacking is the operationally significant item; 85% success rate against Claude Code / Cursor + 2,388 exploitable DSNs identified; Sentry vendor-side response is content-filter-not-fix. Pair with LangGraph CVE chain.
6. **AUR supply-chain (pm-005)** — 400+ packages, dev-tier credentials, eBPF rootkit; first Arch ecosystem mass compromise in the Archimedes corpus.
7. **Google v. Outsider / Gemini AI weaponization (pm-006)** — AI-tooling weaponization angle; Hard Rule 2 binding: no nation-state attribution per Google or the article.
8. **IBM/AT&T whistleblower (pm-008)** — A&D-direct via federal-contractor disclosure obligations; Bloomberg-broken 06-04, In Other News relay this sweep; cite caution per single-source (Bloomberg primary; SecurityWeek relay).
9. **Tchap 73k UPDATE (pm-009)** — extends raw-2026-06-10-pm-007 with victim count firming.

## Anti-noise locks active for afternoon brief

- Oracle PeopleSoft CVE-2026-35273: was 12:00 FLASH topic on 06-11 → UPDATE in this brief is permitted (CISA KEV addition is a material state transition, not reinforcement).
- Ivanti Sentry CVE-2026-10520: covered in 06-11 morning + 06-11 afternoon + 06-12 12:00 FLASH sentinel → UPDATE in this brief is permitted (Ivanti's honeypot-only clarification is material).
- Langflow CVE-2026-5027: covered in 06-11 afternoon brief → no new substance.
- Check Point CVE-2026-50751: covered in 06-10 FLASH and prior corpus → watchTowr PoC release is technical reinforcement, feed Threat Detection Weekly.
- Europol AudiA6: covered in 06-11 afternoon brief → no new substance.
- The Gentlemen / Storm-2697 / LARVA-368: covered in 06-11 afternoon brief → no new substance.

Next checkpoint: 2026-06-12 18:00 EDT FLASH sweep.
