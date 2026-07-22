---
raw_id: raw-2026-07-22-pm-000
collected_at: 2026-07-22T15:46:00-04:00
run_id: pre-brief-20260722-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: sweep-sentinel
  source_name: "Pre-brief sweep sentinel (15:30 EDT feed for 16:00 afternoon brief)"
  source_url: null
  published_at: 2026-07-22T15:46:00-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [sweep-record, filter-trail]
triage_tags: [sentinel, sweep_record, non_flash]
iocs_extracted: false
iocs_count: 0
text_word_count: 0
promoted: false
grader_disposition: not_gradeable_sentinel      # sweep/filter-trail record, not a claim; no finding, no rejection-log entry
grader_disposition_run_id: afternoon-20260722-160000
ttl_expires_at: 2026-10-20T15:46:00-04:00
---

# Pre-brief collection sweep sentinel — 2026-07-22 afternoon (window 2026-07-22T07:30 → 15:30 EDT, ~8h)

Sweep record + filter trail for the 15:30 pre-brief collection feeding the 16:00 afternoon
brief. **Three net-new material raw-signals written this sweep:**
- `raw-2026-07-22-pm-001` — CISA/FBI/EPA Iran-linked OT advisory revision (Iran Cyber Watch +
  CyberAv3ngers #028 / VT-027 TTP line).
- `raw-2026-07-22-pm-002` — SharePoint **CVE-2026-50522 KEV-listed** (VT-048 state change).
- `raw-2026-07-22-pm-003` — Check Point SmartConsole **CVE-2026-16232** net-new KEV add.

## Sources queried (healthy per source-health.yaml)

Productive: **The Record** (5 in-window items; 1 matched → pm-001), **CISA KEV** JSON
(catalog **v2026.07.22** released 2026-07-22T19:00:21Z — **2 net-new adds**, both matched →
pm-002 + pm-003). Quiet/reachable: **BleepingComputer** (5 in-window items, 0 net-new
material after anti-noise), **SecurityWeek** (6 in-window items, 0 material), **Splunk**
`archimedes` + `defenseclaw_local` (first-party sweep clean). All queried sources returned
200 / reachable.

Not separately re-pulled this sweep (pre-brief-fast cadence; no fresh in-window lead requiring
the pivot; all reachable at last check): CISA advisories all.xml, NVD lastMod window query
(handoff-flagged for the two new KEV CVEs, not blocking), Unit42, MSTIC, SANS ISC, Krebs,
CrowdStrike, Rapid7, SentinelOne, Bitdefender, Dragos.

## Skipped — stale per source-health (runtime state unchanged this sweep)

- **mandiant** — feedburner RSS 404 (persistent); direct-HTML cloud.google.com fallback (no
  Mandiant lead surfaced this window).
- **msrc** — feed parse error (4x); MSRC content reaches corpus via relays.
- **ars-security** — security-only feed 404; arstechnica.com/feed/ root is the workaround.
- **censys / urlscan / hibp / threatfox / malwarebazaar** — MCP-not-built / no-key
  (enrichment-only; not triggered — no surviving IOC to enrich).
- **x-cisagov / x-gossithedog** — nitter bridge fragility (stale).

**No source-health status flips this sweep.**

## Match / discard trail

**MATCHED → raw-signaled (3):**
- **Iran-linked OT attacks** — CISA/FBI/EPA advisory revision (The Record, 15:18 EDT) →
  `raw-2026-07-22-pm-001`. Iran Cyber Watch + AA26-097A advisory-line / CyberAv3ngers (#028)
  TTP correspondence (HMI/SCADA manipulation, PLC targeting, Rockwell/Schneider/Siemens) +
  VT-027 structural. No named A&D victim; generic Iran attribution (Hard Rule 2 preserved).
- **CISA KEV CVE-2026-50522 SharePoint** → `raw-2026-07-22-pm-002`. Tracked **VT-048** state
  change `kev_pending` → KEV-listed (due 07-25). Resolves the morning privilege-vector
  conflict against NVD/CISA unauth reading (Hard Rule 8).
- **CISA KEV CVE-2026-16232 Check Point SmartConsole** → `raw-2026-07-22-pm-003`. Net-new
  actively-exploited edge/identity-tier CVE (due 07-25); vuln-tracker scaffold candidate.

**ALREADY CAPTURED / anti-noise → no duplicate:**
- **Langflow CVE-2026-0770** ("CISA orders urgent action on actively exploited Langflow RCE,"
  BleepingComputer 11:43 EDT) — KEV-listed 2026-07-21, evaluated at yesterday's 12:00 sweep,
  routed to the 2026-07-21 afternoon brief. BleepingComputer follow-on relay; anti-noise, NOT
  re-written.
- **Oracle July 2026 CPU** — already `raw-2026-07-22-flash-0600-001` (promoted
  finding-2026-07-22-0002); not re-observed net-new this window.
- **OpenAI models / Hugging Face breach** (The Record + prior BC/SecurityWeek) — already
  discarded at am-000 (AI-safety story, no A&D/roster/CVE nexus). Anti-noise.

**DISCARDED — no watchlist / roster / vuln-index hit:**
- **Swiss rail giant Stadler rejects $12.3M ransom** (BleepingComputer) — Everest ransomware
  breached a supplier-shared data-exchange platform. Rail-vehicle manufacturing supply-chain
  incident; Everest NOT a roster actor; rail is transport, not A&D/DIB. Flagged for awareness
  (manufacturing supply-chain-via-supplier pattern, thematically adjacent to A&D third-party
  risk) but no tracked entity/actor/CVE → not raw-signaled.
- **New Kimsuky campaign compromised South Korean software vendors** (The Record) — North
  Korean APT supply-chain compromise of collaborative-work/groupware vendors. **Kimsuky is NOT
  a roster actor** (roster KP = Stardust Chollima #002, Lazarus #003, APT37 #024; none list
  Kimsuky/APT43/Velvet Chollima as an alias). Non-A&D victims, no tracked CVE. Nation-state
  supply-chain campaign — flagged as a possible **/new-actor candidate** for operator review;
  not raw-signaled (fails Mode-1 roster/watchlist/vuln filter).
- **Adobe Acrobat Chrome extension WhatsApp-data-theft flaw** (BleepingComputer + SecurityWeek,
  300M installs) — browser-extension vuln, no A&D nexus, not a tracked CVE.
- **Suno / Paidwork data breaches** (SecurityWeek, tens of millions of accounts) — consumer
  data breach; non-A&D; no roster actor. **Hard Rule 7 N/A** — leaked-credential exposure
  reported by the source but NO credential values present in the relay; none stored/observed.
- **Vibe-coded apps riddled with exploitable flaws** (SecurityWeek, 434 flaws) — AI-codegen
  security research; no A&D/roster/CVE hit.
- **Nichirei Japan food-logistics extortion recovery** (The Record) — non-A&D (food logistics);
  extortion gang unnamed/non-roster.
- **Palo Alto Networks to acquire Embrace** (SecurityWeek) — M&A/business, not threat intel.
- **StrongestLayer $4.1M funding** (SecurityWeek), **Eclypsium InfraTrust launch** +
  **Acronis GenAI-ransomware sponsored** (BleepingComputer) — vendor/funding/sponsored,
  filtered.
- **French Parliament under-15 social media ban** (The Record) — policy, not threat intel.

## CISA KEV — 2 net-new adds this window (catalog v2026.07.22)

Catalog **v2026.07.22** (released 2026-07-22T19:00:21Z) supersedes yesterday's v2026.07.21.
Two adds dated **2026-07-22**, both due **2026-07-25** (accelerated ~3-day), both
knownRansomwareCampaignUse **Unknown**:
1. **CVE-2026-50522** Microsoft SharePoint (deserialization RCE, unauth) → pm-002 (tracked
   VT-048 state change).
2. **CVE-2026-16232** Check Point SmartConsole (improper auth / login-token theft, unauth) →
   pm-003 (net-new).
No other 2026-07-22 adds. Yesterday's 07-21 adds (wp2shell CVE-2026-60137/63030, Langflow
CVE-2026-0770, DD-WRT CVE-2021-27137) unchanged — all previously evaluated + brief-routed.

## Splunk first-party — clean (Trigger 3 cannot fire; visibility-bounded null)

`mcp__splunk-query health`: Frank reachable, Splunk 10.2.2, license OK. Sweep over -8h:
`(index=archimedes OR index=defenseclaw_local) NOT sourcetype=archimedes:*` → **0 events**.
No external IOC observations against any tracked indicator this window. Dormant
non-archimedes-internal stream pattern persists across both indices.

## Open threads — status this window

Live escalations THIS window: SharePoint **CVE-2026-50522 now KEV-listed** (pm-002); Iran-OT
CISA/FBI/EPA advisory revision (pm-001); Check Point **CVE-2026-16232** net-new KEV (pm-003).
No net-new substance on: Oracle-EBS CVE-2026-46817 (VT-043) / Cl0p CVE-2025-61882 (Estée Lauder
covered; CPU context only); wp2shell CVE-2026-63030/60137 (KEV, in 07-21 PM brief); Langflow
CVE-2026-0770 (KEV, in 07-21 PM brief; BC follow-on relay this window = anti-noise); ServiceNow
CVE-2026-6875; SonicWall SMA1000 UTA0533; PAN-OS CVE-2026-0257 / Qilin; VT-042 LegacyHive;
HollowGraph M365-Graph C2; Trump defense-contractor supply-chain-mapping EO. Kimsuky S. Korean
software-vendor supply-chain campaign = new awareness thread (/new-actor candidate, non-roster).
