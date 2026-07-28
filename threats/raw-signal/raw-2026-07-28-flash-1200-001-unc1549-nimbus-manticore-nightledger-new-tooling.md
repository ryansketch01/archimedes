---
raw_id: raw-2026-07-28-flash-1200-001
collected_at: 2026-07-28T12:06:00-04:00
run_id: flash-sweep-20260728-120000
collection_mode: flash_sweep
source:
  source_yaml_id: the-hacker-news
  source_name: The Hacker News (relay of Kaspersky Securelist primary research — Omar Amin & Vasily Berdnikov)
  source_url: https://thehackernews.com/2026/07/nimbus-manticore-deploys-nightledger.html
  published_at: 2026-07-28T07:55:20-04:00
  originating_primary: "Kaspersky Securelist (2026-07-28) — pending direct retrieval for full IOC appendix"
match_reason:
  watchlist: [aerospace-defense-marginal]
  actors: [UNC1549]
  vulnerabilities: []
  keywords: [Nimbus Manticore, Smoke Sandstorm, NightLedger, BridgeHead, ArcBridge, "DLL search-order hijacking", aviation, "WebSocket tunneler"]
triage_tags: [flash_candidate, tracked-actor-ttp-change, ad-sector-campaign-marginal, unc1549, nimbus-manticore, iranian-apt, new-tooling]
iocs_extracted: true
iocs_count: 3
text_word_count: 320
promoted: true
promoted_to_finding: finding-2026-07-28-flash-1200-0001
promoted_at: 2026-07-28T12:14:00-04:00
ttl_expires_at: 2026-10-26T12:06:00-04:00
---

# Nimbus Manticore (UNC1549) deploys NightLedger backdoor + WebSocket tunnelers in fresh Middle East / Africa / South Asia campaign

New net-new FLASH candidate this window. The Hacker News (2026-07-28 07:55 EDT,
in-window) relays Kaspersky Securelist research (Omar Amin, Vasily Berdnikov)
attributing a fresh set of intrusions to the Iranian state-backed group tracked
as **Nimbus Manticore**, whose alias set includes **Smoke Sandstorm** and
**UNC1549** — roster actor #004 (IRGC, MEDIUM, espionage category HIGH composite
10 on documented A&D-prime targeting).

The campaign introduces a **previously undocumented tooling set**, the core of
this candidate:

- **NightLedger** — new Windows backdoor (recon, command execution, file ops,
  process discovery, screenshot capture). Masquerades as `SspiCli.dll` and is
  loaded via **DLL search-order hijacking** against a legitimate
  `AppVShNotify.exe` binary.
- **BridgeHead** — SOCKS5 tunnel proxy, delivered as `unbcl.dll`.
- **ArcBridge** — WebSocket-based tunneler for covert, operator-controlled
  network access ("turns victim systems into covert relays").

Prior/known UNC1549 tooling referenced for lineage: TWOSTROKE, MiniFast (aka
MiniUpdate / Retrograde), LIGHTRAIL, POLLBLEND.

## Key facts (collection only — not graded)

- Actor: Nimbus Manticore = GalaxyGato = Mirage Kitten = Smoke Sandstorm =
  Subtle Snail = TA455 = UNC1549. **Smoke Sandstorm and UNC1549 both match
  roster #004.** The other five labels (Nimbus Manticore, GalaxyGato, Mirage
  Kitten, Subtle Snail, TA455) are NOT currently in roster #004's alias list
  [Tortoiseshell, Smoke Sandstorm, Imperial Kitten, Crimson Sandstorm] —
  flagged for actor-profiler alias-set review.
- Targeting: government / SMB (Jordan, Tanzania), **aviation organizations
  (Pakistan)**, telecommunications (Ethiopia), financial services (Burkina
  Faso), plus Egypt. Regions: Middle East, Africa, South Asia. Multi-victim,
  multi-sector, characterized as a "fresh set of attacks" (active).
- A&D relevance (collection note, not assessed): aviation sector explicitly
  named as a victim vertical; one relay (TechNadu) headlines the toolkit as
  targeting "aerospace and defense." However, the named victims are regional
  aviation orgs abroad — **NO US A&D prime, DIB contractor, or watchlist entity
  named.** A&D relevance is sector-level / structural, not target-specific.
- Attribution status: **RESTATEMENT** of established UNC1549 tracking, not a new
  first-time attribution. The net-new element is the TOOLING, not the actor
  attribution.
- CVEs: none referenced in the reporting.
- Origin/grade estimate (collection note, NOT a grade): Kaspersky Securelist is
  the A-grade originating primary; THN is a relay. Estimate ~A2 at primary,
  ~B2 through the THN relay. Corroborating relays observed: Broadcom/Symantec
  protection bulletin (MiniFast), TechNadu, multiple aggregators. Grader to set
  the digraph.

## FLASH trigger evaluation

- **Trigger 4 (tracked-actor-ttp-change): MET (primary trigger).** New tooling
  documented (NightLedger backdoor + BridgeHead + ArcBridge WebSocket tunnelers)
  [MET]; A/B-grade source [MET — Kaspersky Securelist A-grade primary]; clearly
  attributable to a tracked actor [MET — UNC1549 / Smoke Sandstorm = roster #004].
  Net: strong Trigger-4 candidate — a new tooling class (WebSocket covert-relay
  tunnelers + DLL-search-order-hijack backdoor) for a tracked Iranian APT.
- **Trigger 5 (ad-sector-campaign): MARGINAL.** Active [MET]; multi-victim [MET];
  targets aerospace/defense/watchlist [MARGINAL-FAIL — aviation vertical named
  and one relay frames it as "aerospace and defense," but victims are regional
  aviation orgs abroad, no US A&D prime / DIB / watchlist entity named]. Grader
  to resolve whether the aviation-sector hit clears the A&D-sector bar.
- **Trigger 2 (tracked-actor-attribution): NOT MET.** Attribution to UNC1549 is
  a restatement of prior tracking, not new (FLASH-POLICY Trigger 2 requires the
  attribution itself be new).
- **Triggers 1 / 3 / 6: NOT MET.** No CVE (1, 6); Splunk first-party 24h sweep
  returned no tracked-IOC hit (3).

Anti-noise: NET-NEW this window. Distinct from the 08:00 morning brief topics
(CVE-2026-16812 Arista VeloCloud; CVE-2026-16723 Fastjson, absorbed). This item
published ~07:55 EDT — after the 07:30 pre-brief collection window — so it is
genuinely first-surfaced at this 12:00 sweep. No prior UNC1549 / Nimbus Manticore
FLASH in the last 24h. One FLASH per trigger-topic rule: first on this topic.

Quiet hours: 12:00 EDT is INSIDE active hours (09:00-21:00) — a resulting FLASH
would post immediately to #flash-alerts, not queue. Critical override NOT met
(no CVSS 10.0, no confirmed active exploitation of a specific CVE, no named A&D
watchlist victim).

---

## Extraction notes

- Language: en
- Publisher byline: The Hacker News (relay); originating research Kaspersky
  Securelist (Omar Amin, Vasily Berdnikov)
- Article type: news relay of vendor threat-research blog
- Raw IOC extraction invoked: yes — result: 3 atomic file-artifact indicators in
  the retrievable reporting (masquerade/abuse filenames). Full network IOC
  appendix (C2 domains/IPs, hashes) resides in the Kaspersky Securelist primary,
  NOT in the THN relay — recorded as pending_direct_retrieval for the grader.
  attribution_claims: UNC1549 (restatement, Kaspersky-originated). Hard Rule 2:
  attribution inherited from Kaspersky, not originated here.

## IOCs (from ioc-extraction skill)

```yaml
iocs:
  - type: filename
    value: "SspiCli.dll"
    context: "NightLedger backdoor masquerades under this legitimate DLL name"
    confidence: reported_not_verified
    note: "Common legitimate Windows DLL name — high false-positive risk; detection value is in the search-order-hijack pairing with AppVShNotify.exe, not the name alone."
  - type: filename
    value: "AppVShNotify.exe"
    context: "Legitimate binary abused as DLL-search-order-hijack host for NightLedger"
    confidence: reported_not_verified
  - type: filename
    value: "unbcl.dll"
    context: "BridgeHead SOCKS5 tunnel proxy delivered under this DLL name"
    confidence: reported_not_verified
tooling:
  new:
    - NightLedger        # Windows backdoor (DLL search-order hijack via AppVShNotify.exe)
    - BridgeHead         # SOCKS5 tunnel proxy (unbcl.dll)
    - ArcBridge          # WebSocket tunneler / covert relay
  prior_referenced:
    - TWOSTROKE
    - MiniFast           # aka MiniUpdate, Retrograde
    - LIGHTRAIL
    - POLLBLEND
cve_references: []
attribution_claims:
  - actor: UNC1549
    also_tracked_as: [Nimbus Manticore, GalaxyGato, Mirage Kitten, Smoke Sandstorm, Subtle Snail, TA455]
    roster_match: "004 (via Smoke Sandstorm + UNC1549)"
    originator: "Kaspersky Securelist"
    status: restatement_not_new
    hard_rule_2: "attribution inherited from Kaspersky; not originated by Archimedes"
network_iocs_pending_direct_retrieval: true
notes: "Full C2/hash IOC appendix is in the Kaspersky Securelist primary (not the THN relay). New aliases Nimbus Manticore / GalaxyGato / Mirage Kitten / Subtle Snail / TA455 are candidates for roster #004 alias-set extension — actor-profiler review."
```
