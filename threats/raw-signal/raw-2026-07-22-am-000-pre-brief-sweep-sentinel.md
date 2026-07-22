---
raw_id: raw-2026-07-22-am-000
collected_at: 2026-07-22T07:32:00-04:00
run_id: pre-brief-20260722-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: sweep-sentinel
  source_name: "Pre-brief sweep sentinel (00:00 EDT feed for 08:00 morning brief)"
  source_url: null
  published_at: 2026-07-22T07:32:00-04:00
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
ttl_expires_at: 2026-10-20T07:32:00-04:00
---

# Pre-brief collection sweep sentinel — 2026-07-22 morning (window 2026-07-21T17:30 → 2026-07-22T07:30 EDT, ~14h)

Sweep record + filter trail for the 07:30 pre-brief collection feeding the 08:00
morning brief. One net-new material raw-signal written this sweep
(`raw-2026-07-22-am-001`, SharePoint CVE-2026-50522 second-publisher corroboration).

## Sources queried (healthy per source-health.yaml)

Productive: **SecurityWeek** (5 in-window items), **BleepingComputer** (6 in-window
items). Quiet/reachable, 0 in-window: **The Record** (0 items after since-filter),
**CISA KEV** JSON (catalog v2026.07.21 — no net-new adds dated 2026-07-22), **Splunk**
`archimedes` + `defenseclaw_local` (first-party sweep clean).

Not separately re-pulled this sweep (FLASH-fast/quiet cadence, no fresh in-window lead
requiring the pivot; all reachable at last check): CISA advisories all.xml, NVD
lastMod window query (no fresh media CVE lead needing NVD verification beyond KEV),
Unit42, MSTIC, SANS ISC, Krebs, CrowdStrike, Rapid7, SentinelOne, Bitdefender.

## Skipped — stale per source-health (runtime state unchanged this sweep)

- **mandiant** — feedburner RSS 404 (persistent); direct-HTML cloud.google.com path is
  the working fallback when a Mandiant lead surfaces (none this window).
- **msrc** — feed parse error (4x); MSRC content reaches corpus via relays.
- **ars-security** — security-only feed 404; arstechnica.com/feed/ root is the workaround.
- **censys / urlscan / hibp / threatfox / malwarebazaar** — MCP-not-built / no-key
  (enrichment-only; not triggered — no surviving IOC to enrich).
- **x-cisagov / x-gossithedog** — nitter bridge fragility (stale).

No source-health status flips this sweep. All queried sources returned 200 / reachable.

## Match / discard trail

**MATCHED → raw-signaled (1):**
- **SharePoint CVE-2026-50522** ("Fourth SharePoint Vulnerability Exploited," SecurityWeek,
  Eduard Kovacs, 07:29 EDT) → `raw-2026-07-22-am-001`. Net-new second-publisher relay of
  the actively-exploited on-prem SharePoint machine-key-theft thread first raw-signaled at
  the 18:00 sweep yesterday (`raw-2026-07-21-flash-1800-001`, BleepingComputer). Matches the
  tracked SharePoint cluster (VT-037/038/041) + A&D-HIGH (structural, DIB-pervasive on-prem
  SharePoint). Carries a **privilege-requirement CONFLICT** vs the 18:00 raw-signal
  (SecurityWeek: "authenticated, Site Owner privileges" vs BleepingComputer+NVD: unauth PR:N
  CVSS 9.8) — surfaced for grader adjudication (Hard Rule 8, not adjudicated here).

**ALREADY CAPTURED this cycle → no duplicate (anti-noise):**
- **Oracle July 2026 Critical Patch Update** (SecurityWeek, same URL) — already raw-signaled
  at the 06:00 FLASH sweep as `raw-2026-07-22-flash-0600-001` (non_flash, Oracle-EBS thread
  vuln-tracker handoff). Re-observed in-window this sweep; NOT re-written. EBS received the
  most patches in the CPU (410 CVEs per the relay) — Oracle-EBS standing thread (Cl0p
  CVE-2025-61882; VT-043 CVE-2026-46817) patch-posture context stands with the 06:00 file.

**DISCARDED — no watchlist / roster / vuln-index hit:**
- Microsoft to end Exchange 2016/2019 ESU security updates in October (BleepingComputer).
  Touches on-prem Exchange (VT-008 thematic, DIB-relevant) but is an EOL/lifecycle reminder,
  NOT a CVE/actor/exploitation event — fails the Mode-1 filter (no tracked CVE, no actor, no
  watchlist entity). Flagged here for briefer awareness as possible A&D sector-planning
  context (DIB estates on on-prem Exchange lose ESU October 2026); not raw-signaled to keep
  pre-brief scope discipline.
- OpenAI AI models "hacked" Hugging Face during sandboxed testing (BleepingComputer +
  SecurityWeek, both publishers). AI-safety/red-team testing story; no A&D nexus, no roster
  actor, no tracked CVE.
- Chick-fil-A data breach via credential-stuffing (BleepingComputer). Non-A&D (fast food),
  no roster actor, no tracked CVE. (No credentials in scope — Hard Rule 7 N/A, none present.)
- FakeGit — 7,600 malicious GitHub repos pushing SmartLoader/StealC (BleepingComputer).
  Commodity malware supply-chain; no A&D/roster/vuln hit.
- Police dismantle Kratos phishing-as-a-service platform (BleepingComputer). LE takedown; no
  A&D/roster/vuln hit.
- Anubis ransomware threatens Coca-Cola Fairlife data leak (SecurityWeek). Non-A&D (dairy),
  Anubis not a roster actor — already discarded at prior sweeps; anti-noise.
- Glow endpoint-security $180M funding round (SecurityWeek). Business/funding; not threat intel.

## CISA KEV — no net-new since yesterday

Catalog **v2026.07.21** (released 2026-07-21T15:12 UTC), unchanged this window. The four
2026-07-21 adds — wp2shell **CVE-2026-60137** + **CVE-2026-63030** (WordPress Core, due
07-24/08-04), Langflow **CVE-2026-0770** (due 07-24), DD-WRT **CVE-2021-27137** (due 07-24)
— were all evaluated at yesterday's 12:00 + 18:00 sweeps (wp2shell + Langflow routed to the
2026-07-21 afternoon brief; DD-WRT discarded as commodity-router no-nexus). **No KEV entries
dated 2026-07-22.** SharePoint CVE-2026-50522 is NOT (yet) KEV-listed (rapid-KEV watch active).

## Splunk first-party — clean (Trigger 3 cannot fire; visibility-bounded null)

`mcp__splunk-query health`: Frank reachable, Splunk 10.2.2, license OK. Sweep over -14h:
`(index=archimedes OR index=defenseclaw_local) NOT sourcetype=archimedes:*` → **0 events**.
Targeted -24h keyword sweep (CVE-2026-50522 / SharePoint / machine key / CVE-2026-46817 /
Oracle EBS / CVE-2025-61882 / Langflow / wp2shell / CVE-2026-0257 / Qilin / Cl0p /
HollowGraph) → 2 hits, both `archimedes:operation` pipeline self-references (Archimedes' own
logging), **zero external IOC observations**. Dormant non-archimedes-internal stream pattern
persists across both indices.

## Open threads — status this window

No net-new substance on: PAN-OS CVE-2026-0257 / Qilin (07-21 morning-brief lead, quiet);
Cl0p / Oracle EBS CVE-2025-61882 (Estée Lauder restatement covered; Oracle CPU context only);
ServiceNow CVE-2026-6875; SonicWall SMA1000 UTA0533; wp2shell CVE-2026-63030/60137 (KEV, in
07-21 afternoon brief); Langflow CVE-2026-0770 (KEV, in 07-21 afternoon brief); VT-042
LegacyHive; HollowGraph M365-Graph C2; Trump defense-contractor supply-chain-mapping EO (in
07-21 afternoon brief). SharePoint CVE-2026-50522 is the one live escalation (see am-001).
