---
raw_id: raw-2026-05-27-am-001
collected_at: 2026-05-27T07:38:00-04:00
run_id: pre-brief-2026-05-27-am
collection_mode: pre_brief_collection
source:
  source_yaml_id: crowdstrike
  source_name: CrowdStrike Counter Adversary Operations
  source_url: https://www.crowdstrike.com/en-us/blog/inside-crowdstrike-takedown-of-a-developer-targeting-botnet/
  published_at: 2026-05-26T14:00:00+00:00
  publication_date_evidence: "Body of CrowdStrike post states disruption coordinated 2026-05-26 14:00 UTC; SecurityWeek (Arghire) dated relay 2026-05-27T10:10:00 UTC = 06:10 EDT corroborates same-day publication. CrowdStrike RSS feed item has published: null per persistent-dateless-marketing pattern but publication day is unambiguously 2026-05-26 per body content + cross-relay corroboration."
secondary_source:
  source_yaml_id: securityweek
  source_name: SecurityWeek (Ionut Arghire)
  source_url: https://www.securityweek.com/glassworm-botnet-disrupted/
  published_at: 2026-05-27T10:10:00+00:00
match_reason:
  watchlist: []
  actors: ["GlassWorm (roster #005, HIGH threat-level)"]
  vulnerabilities: []
  keywords: [GlassWorm, GlasswormRAT, GlasswormDownloader, CrowdStrike, Shadowserver, Solana blockchain, BitTorrent DHT, Google Calendar, VSCode, OpenVSX, npm, PyPI, supply chain, Russian, CIS, sinkhole, 164.92.88.210]
triage_tags: [tracked_actor_state_change, tracked_actor_005_disruption, supply_chain_developer_targeting, a_grade_vendor_primary, crowdstrike_counter_adversary_operations, multi_partner_takedown, novel_c2_channels_blockchain_dht_calendar, russian_origin_per_source]
iocs_extracted: false
iocs_count: 0
text_word_count: 1180
promoted: true
promoted_to_finding: finding-2026-05-27-0001-crowdstrike-glassworm-takedown-roster-005-counter-adversary-operations-google-shadowserver
promoted_at: 2026-05-27T08:14:00-04:00
promoted_by: grader
promoted_in_run: morning-20260527-080000
ttl_expires_at: 2026-08-25T07:38:00-04:00
---

# Disrupting GlassWorm: Inside CrowdStrike's takedown of a developer-targeting botnet

## Primary source

CrowdStrike Counter Adversary Operations (cited byline; no individual
analyst named on this post), published 2026-05-26 ~14:00 UTC. URL:
https://www.crowdstrike.com/en-us/blog/inside-crowdstrike-takedown-of-a-developer-targeting-botnet/

CrowdStrike's RSS feed item lists this post but with `published: null`
per the long-standing CrowdStrike persistent-dateless-marketing pattern.
The publication date is anchored via (a) the SecurityWeek relay
(2026-05-27T10:10:00 UTC = 06:10 EDT today, Ionut Arghire) which dates
the takedown to "yesterday" relative to the relay; (b) CrowdStrike's
own body text describing the disruption as "coordinated 2026-05-26
14:00 UTC."

## Tracked actor: GlassWorm (roster #005, HIGH)

Per `threats/threat-actors/_roster.yaml`, GlassWorm is actor ID #005,
threat level HIGH, type Cybercriminal, attribution: nation unknown
service null, tracked since 2026-04-02. This CrowdStrike post is the
first A-grade vendor takedown report on GlassWorm in the Archimedes
corpus.

## What was disrupted

A multi-partner takedown of GlassWorm's four parallel command-and-control
channels:

1. **Solana blockchain dead-drop**: C2 addresses encoded in the memo
   fields of Solana blockchain transactions. CrowdStrike characterizes
   this as an "immutable, publicly accessible dead-drop mechanism."
2. **BitTorrent DHT**: GlasswormRAT queried the BitTorrent peer-to-peer
   network for configuration data stored against hardcoded public keys.
   CrowdStrike notes the decentralized network architecture as a
   resilience mechanism.
3. **Google Calendar**: Event titles used as dead-drop locations for
   Base64-encoded C2 paths.
4. **Commercial VPS providers**: Traditional direct C2 servers hosting
   final-stage payload delivery.

CrowdStrike coordinated the takedown with Google (Calendar C2 channel
shutdown) and the Shadowserver Foundation (sinkhole and infrastructure
takeover). All four channels were disrupted simultaneously per the
SecurityWeek relay; infected machines redirected to CrowdStrike's
benign sinkhole at 164.92.88[.]210.

## Targeting and scope

- **Target population**: Software developers with access to source-code
  repositories, CI/CD pipelines, and cloud platforms
- **Geographic spread**: Global (per article); no specific countries
  named
- **Sectors**: Not specifically scoped — the campaign targeted developer
  ecosystem broadly; aerospace, defense, ITAR, CMMC, DIB **not
  mentioned**
- **Campaign duration**: "At least early 2025" through 2026-05-26
  disruption
- **Attack vectors**:
  - Trojanized VSCode extensions distributed via OpenVSX marketplace
  - Compromised npm and Python packages (PyPI)
  - Over 300 poisoned GitHub repositories using stolen credentials
  - Platforms targeted: VSCode, Cursor, Positron, Windsurf, VSCodium

## Attribution

CrowdStrike's attribution language per Hard Rule 2 preservation:
**"The criminals are likely based in Russia."** No APT alias or UNC
designation. Pattern-based assessment, no formal confidence-level
language.

Russian-origin indicators cited:
- Runtime locale and timezone checks; malware "quietly exits" if the
  victim system is in a CIS country
- "Russian-language comments appear throughout the source code"
- CrowdStrike's own caveat preserved verbatim per Hard Rule 2: "No
  single indicator is proof on its own" (with the further note that
  code comments may reflect AI tooling rather than human authorship)

GlassWorm's `_roster.yaml` entry has `attribution: nation unknown,
service null` — this post is the first A-grade attribution toward
Russian origin in the Archimedes corpus. **Per Hard Rule 2,
Archimedes records CrowdStrike's "likely based in Russia" framing
verbatim and does NOT upgrade to confirmed RU attribution.**

## Malware families

- **GlasswormRAT** — described as a "full-featured Node.js remote
  access tool"
- **GlasswormDownloader** — a smaller (<10KB) downloader component,
  detected by the YARA rule `CrowdStrike_GlasswormDownloader_01`
  (patterns: zlib, decompress, lambda, exec)
- **GlasswormRAT** detection signature: `CrowdStrike_GlasswormRat_01`
  (patterns: DownloadManager, start_socks, nodejs.org, bootstrap strings)

CrowdStrike's post explicitly publishes both YARA rules.

## IOCs

| Type | Value | Notes |
|---|---|---|
| IPv4 (sinkhole, benign) | 164.92.88[.]210 | CrowdStrike-operated sinkhole; infected machines redirected here post-disruption. NOT a malicious indicator; defender awareness only. |
| YARA rule | CrowdStrike_GlasswormRat_01 | Detects GlasswormRAT |
| YARA rule | CrowdStrike_GlasswormDownloader_01 | Detects GlasswormDownloader (<10KB filesize) |

Note: CrowdStrike's post mentions Solana addresses, BitTorrent hashes,
and Google Calendar event titles as part of the C2 architecture but
does NOT publish a list of specific identifiers in the body. Operator
follow-up via direct CrowdStrike intel-platform access would be
required for that IOC layer.

## A&D / aerospace / defense

**Not mentioned.** No watchlist A&D prime named (Lockheed Martin,
Boeing, RTX, Northrop Grumman, General Dynamics, BAE Systems, L3Harris,
Leidos, SAIC, Thales, GE Aerospace, Safran, Honeywell, Airbus, Elbit
Systems all silent). The targeted developer-ecosystem framing is
structural-supply-chain-warning class for A&D-SDLC indirect exposure
(any A&D prime using VSCode + OpenVSX + npm + PyPI + GitHub had
contemporaneous exposure surface) but NO A&D-prime victim disclosure
in this report.

## MITRE ATT&CK

CrowdStrike's post does NOT include a MITRE ATT&CK technique mapping.

## CrowdStrike's framing

CrowdStrike emphasizes two operational themes per the body:
- "Detection alone is virtually impossible" against supply-chain threats
- "Proactive disruption" and "cross-sector collaboration" as the
  response model — implicit endorsement of the multi-partner takedown
  model used here

## Relay coverage

SecurityWeek published an in-window relay 2026-05-27T10:10:00 UTC =
06:10 EDT today (Ionut Arghire byline). The SecurityWeek piece is a
B-grade media relay that:
- Confirms the takedown date and partner set
- Confirms the four-channel C2 architecture
- Confirms the "likely Russia" framing
- Adds no independent corroborating telemetry or IOC layer

The relay layer establishes peer-publishing-tier coverage of the
CrowdStrike primary but does NOT constitute independent A-grade
corroboration (it is a relay of the CrowdStrike post, not parallel
research).

## Significance for AM-27 brief

Grader-side decision:
- This is a **tracked-actor STATE CHANGE** (operational neutralization)
  not a fresh attribution or fresh TTP discovery. Per FLASH-POLICY,
  Trigger 4 (TTP change) is not a canonical fit because the change is
  destructive-of-actor-infrastructure rather than additive-to-TTP-set.
- AM-27 morning brief is well-positioned to surface this as the
  headline item in a tracked-actor section: tracked actor #005
  (HIGH) disrupted by A-grade vendor in coordinated multi-partner
  operation.
- The "novel four-channel C2 architecture" (blockchain + DHT + calendar
  + VPS) is itself a structural intelligence signal worth surfacing
  for defender awareness — even after disruption, the architectural
  pattern is reusable by other actors.

## Extraction notes

- Language: en
- Publisher byline: Counter Adversary Operations (team byline, no
  individual analyst)
- Article type: vendor research blog (CrowdStrike) / news relay
  (SecurityWeek)
- Raw IOC extraction invoked: yes (manual; structured into the IOCs
  table above)
- CVSS / CVE: N/A (this is an actor-disruption report, not a CVE
  publication)
- Hard Rule 2 compliance: attribution language preserved verbatim ("the
  criminals are likely based in Russia"); no upgrade to confirmed RU
  attribution; roster `_roster.yaml` entry for GlassWorm retains
  `nation: unknown` pending grader-side decision on whether to update.
- Hard Rule 3 compliance: no PoC, no exploit primitive, no working
  attack chain reproduced.
- Hard Rule 6 compliance: CrowdStrike attribution quote ("the
  criminals are likely based in Russia") is 7 words, under 15-word
  ceiling.
