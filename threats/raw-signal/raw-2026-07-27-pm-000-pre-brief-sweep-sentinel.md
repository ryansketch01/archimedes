---
raw_id: raw-2026-07-27-pm-000
collected_at: 2026-07-27T15:33:00-04:00
run_id: pre-brief-20260727-153000
collection_mode: pre_brief_collection
test: false
source:
  source_yaml_id: multiple
  source_name: "Pre-brief collection coverage sentinel (15:30 EDT)"
  source_url: null
  published_at: null
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [pre_brief, coverage_record]
triage_tags: [pre_brief, coverage_record, non_flash]
iocs_extracted: false
iocs_count: 0
text_word_count: 610
promoted: false
ttl_expires_at: 2026-10-25T15:33:00-04:00
---

# Pre-brief collection coverage record — 2026-07-27 15:30 EDT (feeds 16:00 afternoon brief)

Window: ~2026-07-27T07:30 → 15:30 EDT (8h afternoon lookback; the gap since this morning's
07:30 pre-brief collection). Prior sweeps of record: 2026-07-27 07:30 morning pre-brief
(raw-2026-07-27-am-000, clean) → 08:00 morning brief (quiet operational-week open, board
unchanged); 2026-07-27 00:00 + 06:00 FLASH (both clean). This afternoon pre-brief produced
**3 net-new substantive raw-signal files** (pm-001 through pm-003) plus this sentinel.

## Substantive raw-signal written this window

- **pm-001** — PTC Windchill CVE-2026-12569 (VT-tracked) Cl0p ransomware campaign, SecurityWeek
  fresh dated primary; continuing-coverage enrichment on the one live A&D-relevant thread
  (aerospace named among targeted sectors). NON-FLASH (already in-corpus / KEV-listed since
  ~06-25; new detail is attack-chain mechanism + active-campaign-since-07-20 + extortion scope).
- **pm-002** — CISA KEV net-new addition (dateAdded 2026-07-27): Fortinet FortiOS
  CVE-2025-68686 (SSL-VPN), dueDate 2026-08-10, ransomware Unknown.
- **pm-003** — CISA KEV net-new addition (dateAdded 2026-07-27): Arista VeloCloud Orchestrator
  CVE-2026-16812, dueDate 2026-07-30 (accelerated ~3-day), ransomware Unknown.

## In-window items evaluated — DISCARDED

**securityweek** — 4 items in window (last_modified 2026-07-27T16:33 GMT):
- "PTC Windchill Vulnerability Exploited in Ransomware Campaign" (Ionut Arghire, 13:19 UTC) —
  RAW-SIGNALED as pm-001 (tracked CVE-2026-12569 + Cl0p + aerospace).
- "New GitHub, PyPI Policies Boost Supply Chain Security" — supply-chain policy. DISCARDED.
- "MedusaHVNC Malware Uses Hidden Windows Desktops to Evade Detection" — MaaS HVNC; no roster
  actor / no A&D / no tracked CVE. DISCARDED.
- "Nvidia and Tech Giants Launch AI Security Alliance" — AI-security coalition. DISCARDED.

**bleepingcomputer** — 4 items in window (last_modified 2026-07-27T19:26 GMT):
- "Ernst & Young data breach claimed by ShinyHunters extortion gang" — ShinyHunters is NOT a
  roster actor (explicitly non-cross-walked per Icarus #025 dossier); E&Y is a consulting firm,
  not A&D; supply-chain vector mentioned but no tracked CVE / no IOC. DISCARDED; flagged for
  grader awareness (ShinyHunters extortion cadence).
- "Coca-Cola confirms data theft in Fairlife ransomware attack" — Anubis group, carried in the
  morning sentinel; anti-noise. DISCARDED.
- "Apple sued over fake App Store crypto wallet app" — consumer fraud litigation. DISCARDED.
- "Shadow AI agents are multiplying" — sponsored vendor content. DISCARDED.

**the-record** — 4 items in window:
- "Hackers used autonomous AI agent to spy on Thailand's finance ministry" — AI-agent espionage
  TTP; target is Thai MoF (not A&D); no roster actor named in the item. DISCARDED; flagged for
  grader TTP-awareness (autonomous-AI-agent tradecraft, recurring theme).
- "Telegram phishing campaign targeted exiled Belarusian activist, Russians, Kazakhstanis" —
  personalized account-takeover phishing; no A&D / no roster attribution. DISCARDED.
- "UK court rejects Bahrain immunity claim in spyware case" — spyware litigation. DISCARDED.
- "Health system in South Carolina, Georgia closes offices after malware" (AnMed) — healthcare
  disruption. DISCARDED.

**mstic** (parent feed) — 2 items in window: "Rethinking security for the age of AI" (Project
Perception) and "Enhancing AI security through global AI red teaming" (EXTRA). Both Microsoft
AI-security product/program announcements; no threat-intel claim, no A&D / roster / vuln.
DISCARDED.

**sans-isc** 0 · **unit42** 0 · **rapid7** 0 · **krebs** 0 · **cisa-advisories** (all.xml) 0
in window.

## Authoritative CVE / KEV surface

- **cisa-kev** (JSON directly fetched): **KEV DELTA this window** — TWO net-new entries dated
  2026-07-27: CVE-2025-68686 (Fortinet FortiOS) and CVE-2026-16812 (Arista VeloCloud
  Orchestrator). Both raw-signaled (pm-002, pm-003). The 2026-07-22 pair (CVE-2026-16232 Check
  Point, CVE-2026-50522 SharePoint) remains in-corpus; no change.

## Tracked-topic state-change check

- **Windchill CVE-2026-12569** (Cl0p, aerospace sector): fresh SecurityWeek primary this window
  → pm-001 (enrichment, not a state change vs KEV-listed status).
- **Oracle EBS CVE-2026-46817 (VT-043)**, **LegacyHive/Nightmare Eclipse (VT-042)**, **SharePoint
  CVE-2026-50522 (VT-048)**, **Check Point SmartConsole CVE-2026-16232**, **Zimbra
  CVE-2025-66376** (Laundry Bear/Void Blizzard) — NO in-window development. Steady-state.

## First-party (Splunk, Frank)

Sentinel sweep `(index=archimedes OR index=defenseclaw_local) NOT sourcetype=archimedes:*` over
-8h → **0 events**, both indexes. Dormant-external-stream pattern holds; Trigger 3
(first-party-ioc-hit) cannot fire. No in-window candidate carried atomic IOCs requiring
Shodan/VT/AbuseIPDB enrichment (KEV entries + the SecurityWeek Windchill item published no
atomic network IOCs).

## Not queried (stale / no MCP)

mandiant (stale, feedburner dead / direct-HTML pending operator swap), msrc (stale since
2026-05-30, relays carry content), ars-security (stale, root-feed workaround), x-cisagov /
x-gossithedog (nitter fragility), censys / urlscan / hibp / threatfox / malwarebazaar (MCP not
built / no key). None eligible-and-productive this fast window.

## Source health

All queried RSS/media/KEV/Splunk sources returned HTTP 200 (or 0-event clean) and remain
`healthy`. No status flips this sweep. Per file convention, per-source runtime timestamps are
refreshed only on a status/failure_count change (none this sweep); source-health.yaml header
`last_updated` advanced to this sweep. Operator-set `notes` preserved verbatim.

## Extraction notes

- Language: en
- Article type: coverage sentinel (no external article ingested in this file)
- Raw IOC extraction invoked: per-item in pm-001..pm-003

## FLASH assessment

Two net-new KEV additions (pm-002 Fortinet, pm-003 Arista) carry active-exploitation
confirmation legs. Routed to the **16:00 afternoon brief** (~25 min out) as net-new items rather
than a re-FLASH, consistent with the SharePoint / Oracle-EBS 3-day-KEV precedent (KEV state
changes absorbed into the imminent scheduled brief). CVSS not confirmed ≥9.0 for either from the
KEV entry alone; grader to adjudicate FLASH-adjacency. No tracked-actor attribution originated
(Hard Rule 2). Windchill pm-001 is continuing coverage, non-FLASH.
