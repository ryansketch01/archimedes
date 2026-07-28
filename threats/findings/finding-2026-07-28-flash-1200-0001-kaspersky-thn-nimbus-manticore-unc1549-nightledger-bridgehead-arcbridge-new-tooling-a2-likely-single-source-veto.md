---
finding_id: finding-2026-07-28-flash-1200-0001
created_at: 2026-07-28T12:14:00-04:00
graded_by: grader
grading_run_id: flash-grade-20260728-120500

# Core grading (from admiralty-grading skill output)
digraph: A2
source_reliability:
  grade: A
  source_name: Kaspersky Securelist (Omar Amin & Vasily Berdnikov), relayed by The Hacker News
  source_yaml_id: securelist            # NO dedicated source-grades.yaml id yet — see source_grade_addition_proposed
  grade_rationale: >
    Grade attaches to the originating primary. Kaspersky Securelist is corpus
    A-grade Tier-1 vendor research (referenced as "Kaspersky GReAT (corpus A)"
    in source-grades.yaml). The research is unambiguously attributed with named
    analyst bylines (Omar Amin, Vasily Berdnikov). The claim reached Archimedes
    via The Hacker News (provisional B) relay this sweep; the Kaspersky primary
    was NOT directly retrieved — relay-only / pending_direct_retrieval caveat
    applies (mirrors the Symantec/MuddyWater-via-THN precedent,
    finding-2026-05-13-FLASH-1800-0001). Conservative alternative FLOOR is B
    (relay-in-hand); the promote/reject outcome is identical either way (both
    clear the FLASH B2 minimum).
  provisional: true
  provisional_reason: >
    No dedicated `securelist` / `kaspersky-securelist` id exists in
    source-grades.yaml; grade anchored on established corpus Kaspersky-A
    precedent. Flagged for librarian to open a provisional-A source entry
    (Tier-1 vendor-research first-dedicated-surface).
credibility:
  grade: 2
  checklist_passed:
    - probably_true_ttp_consistent          # DLL search-order hijack + custom backdoor + SOCKS5/WebSocket tunnelers consistent with UNC1549 established espionage tradecraft (prior toolset TWOSTROKE/MiniFast/LIGHTRAIL/POLLBLEND); targeting (aviation/telecom/gov across ME/Africa/S.Asia) consistent with UNC1549 regional profile
    - probably_true_no_contradicting_ab      # no contradicting A/B-grade source
    - probably_true_claims_coherent          # technique internally coherent; no CVE claim to verify; no implausible technical assertion
  rationale: >
    Grade 1 (Confirmed) fails: no INDEPENDENT corroboration of the specific
    new-tooling claim. The Hacker News and TechNadu are relays of the same
    Kaspersky research (remove Kaspersky and neither stands). The
    Broadcom/Symantec protection bulletin covers MiniFast — PRIOR/known UNC1549
    tooling referenced for lineage — NOT the net-new NightLedger/BridgeHead/
    ArcBridge set that is the core claim; its independent evidence basis for
    the new-tooling claim is unestablished (likely derivative detection
    additions triggered by Kaspersky's published IOCs). Effective single
    source (Kaspersky) on the primary claim. Grade 2 (Probably True) — all
    three conditions met: TTP-consistent for tracked actor UNC1549 (roster #004),
    no contradicting A/B source, technically coherent.
corroboration:
  independent_sources: []
  independent: false
  test_passed: >
    FAILS independence test. THN + TechNadu are relays of the Kaspersky primary
    (not independent publishers with separate evidence bases). Symantec/Broadcom
    bulletin addresses MiniFast (prior tooling), not the new-tooling claim, and
    its independence-of-evidence-basis for the new claim is unestablished. Single
    effective source (Kaspersky) on the graded claim.
first_party_precedence:
  applied: false
  splunk_evidence: >
    Hard Rule 8 check performed. Query across defenseclaw_local + archimedes
    (-30d) on distinctive artifacts (AppVShNotify.exe, unbcl.dll, NightLedger,
    Nimbus Manticore, UNC1549) returned ONE hit — an Archimedes operational log
    event (flash_queue_archived record containing "UNC1549" in an archived
    brief-id string), NOT a first-party telemetry detection. defenseclaw_local
    silent. Collector's -24h FLASH sweep (Trigger 3) also returned no tracked-IOC
    hit. Silent first-party is NOT disconfirming. Atomic network IOCs (C2/hashes)
    reside in the Kaspersky primary, pending_direct_retrieval.
single_source_veto_applied: true
wep_ceiling: likely

# Source-grade housekeeping (librarian action)
source_grade_addition_proposed:
  source_yaml_id: securelist
  proposed_grade: A
  proposed_provisional: true
  reason: >
    Kaspersky Securelist is the originating primary on this finding. Corpus
    treats Kaspersky research as A-grade Tier-1 vendor research but has no
    dedicated source-grades.yaml id. Open a provisional-A entry per Tier-1
    vendor-research first-dedicated-surface precedent (SentinelOne 2026-05-08,
    Bitdefender/Symantec 2026-05-13, etc.). Note relay-only surface this sweep;
    awaiting_direct_retrieval of securelist.com primary.
  action: "librarian to add provisional-A entry + source-grade-log.md; human ratification pending"

# Cluster metadata
cluster:
  topic: "UNC1549 / Nimbus Manticore new tooling — NightLedger backdoor + BridgeHead + ArcBridge tunnelers"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-07-28-flash-1200-001
  attribution_claims:
    - claimed_actor: UNC1549
      roster_id: "004"
      also_tracked_as_per_source: [Nimbus Manticore, GalaxyGato, Mirage Kitten, Smoke Sandstorm, Subtle Snail, TA455]
      claimed_by_sources: [securelist]
      status: restatement_not_new           # Hard Rule 2 — attribution inherited from Kaspersky, not originated by Archimedes
      requires_analyst_review: true
      note: >
        Roster #004 alias list [Tortoiseshell, Smoke Sandstorm, Imperial Kitten,
        Crimson Sandstorm] matches on Smoke Sandstorm + UNC1549. The other five
        Kaspersky-cluster labels (Nimbus Manticore, GalaxyGato, Mirage Kitten,
        Subtle Snail, TA455) are NOT in roster #004 — flagged for actor-profiler
        alias-set review. Archimedes records Kaspersky's alias mapping as
        Kaspersky's claim; does not originate the merge.

# Inclusion eligibility (from admiralty-grading)
inclusion:
  eligible_for:
    - flash
    - daily_brief_action
    - weekly_synthesis
    - actor_profile_update

# FLASH context
flash:
  trigger_primary: "Trigger 4 — tracked-actor TTP change (new tooling; A-grade primary; attributable to roster #004). MET."
  trigger_secondary: "Trigger 5 — A&D-sector campaign. MARGINAL-FAIL: aviation vertical named (regional aviation orgs abroad, Pakistan) but NO US A&D prime / DIB / watchlist entity named. A&D relevance sector-level/structural, not target-specific."
  quiet_hours: "12:00 EDT inside active hours (09:00-21:00) — a resulting FLASH posts immediately to #flash-alerts, not queued."
  critical_override_met: false           # no CVSS 10.0, no confirmed active CVE exploitation, no named A&D watchlist victim

# Downstream handoff flags
analyst_review_required: true            # WEP >= likely AND attribution/alias-extension claim present
red_team_review_required: false          # WEP ceiling is "likely" (single-source veto), NOT "very likely" — red-team not mandatory per anti-noise rule 3
red_team_review: null
analysis_sections:
  sat_ach: null
  sat_kac: null

# Lifecycle
tlp: CLEAR
published_in_briefs: [flash-2026-07-28-1200]   # briefer appends brief_ids
retracted: false
retraction_brief_id: null
---

# Kaspersky attributes a fresh multi-region espionage campaign to UNC1549 (Nimbus Manticore), introducing three previously undocumented tools

## Summary

Kaspersky Securelist reports that the Iranian state-backed group it tracks as
Nimbus Manticore — alias set including Smoke Sandstorm and UNC1549, matching
roster actor #004 (IRGC) — has deployed a previously undocumented tooling set in
a fresh set of intrusions across the Middle East, Africa, and South Asia. The
net-new element is the tooling, not the actor attribution, which restates
Kaspersky's established tracking. Three new tools anchor the campaign: NightLedger,
a Windows backdoor loaded via DLL search-order hijacking against a legitimate
AppVShNotify.exe binary; BridgeHead, a SOCKS5 tunnel proxy; and ArcBridge, a
WebSocket-based tunneler that turns victim hosts into covert relays. Archimedes
grades this A2 with the single-source veto applied — Kaspersky is the sole
effective source; The Hacker News and TechNadu are relays, and the Broadcom/
Symantec bulletin covers prior tooling (MiniFast), not the new set. WEP ceiling
is "likely."

## Sources

### Kaspersky Securelist — originating primary (securelist, digraph anchor: A)

- Authors: Omar Amin, Vasily Berdnikov
- Published: 2026-07-28 (relayed same day)
- Not directly retrieved this sweep — surfaced via The Hacker News relay; primary
  and its full network-IOC appendix are pending_direct_retrieval.
- Key claim: A fresh UNC1549/Nimbus Manticore campaign deploys new tooling
  (NightLedger, BridgeHead, ArcBridge) against aviation, telecom, government, and
  financial-services targets across the Middle East, Africa, and South Asia.

### The Hacker News (thehackernews, digraph: B) — relay

- URL: https://thehackernews.com/2026/07/nimbus-manticore-deploys-nightledger.html
- Published: 2026-07-28T07:55:20-04:00
- Key claim: Faithful relay of the Kaspersky research; not an independent evidence
  basis.

### Broadcom/Symantec + TechNadu — NOT independent corroboration of the new-tooling claim

- Symantec/Broadcom protection bulletin addresses MiniFast (prior/known UNC1549
  tooling referenced for lineage), not NightLedger/BridgeHead/ArcBridge; likely
  derivative of Kaspersky's published IOCs.
- TechNadu is a media relay (headlines the toolkit as "aerospace and defense"
  targeting); not a separate primary.

## Technical detail

- **NightLedger** — new Windows backdoor. Capabilities per Kaspersky: recon,
  command execution, file operations, process discovery, screenshot capture.
  Masquerades as `SspiCli.dll`; loaded via DLL search-order hijacking against a
  legitimate `AppVShNotify.exe` host binary.
- **BridgeHead** — SOCKS5 tunnel proxy, delivered as `unbcl.dll`.
- **ArcBridge** — WebSocket-based tunneler for covert, operator-controlled network
  access ("turns victim systems into covert relays").
- Prior UNC1549 tooling cited for lineage: TWOSTROKE, MiniFast (aka MiniUpdate /
  Retrograde), LIGHTRAIL, POLLBLEND.
- No CVE referenced; no exploitation-of-a-specific-vulnerability claim. This is a
  tooling/targeting story. The tradecraft (DLL search-order hijack + custom
  backdoor + SOCKS5/WebSocket covert tunneling) is consistent with UNC1549's
  established espionage tradecraft, supporting the credibility-2 assessment.
- Reference: MITRE ATT&CK T1574.001 (DLL Search Order Hijacking).

## IOCs surfaced

Atomic file-artifact indicators from the relay (masquerade/abuse filenames).
Detection value is in the search-order-hijack PAIRING, not the individual
legitimate-DLL names, which carry high false-positive risk:

```yaml
iocs:
  - type: filename
    value: "SspiCli.dll"
    context: "NightLedger backdoor masquerades under this legitimate Windows DLL name"
    confidence: reported_not_verified
    note: "Common legitimate DLL name — detection value is the AppVShNotify.exe search-order-hijack pairing, not the name alone."
  - type: filename
    value: "AppVShNotify.exe"
    context: "Legitimate binary abused as DLL-search-order-hijack host for NightLedger"
    confidence: reported_not_verified
  - type: filename
    value: "unbcl.dll"
    context: "BridgeHead SOCKS5 tunnel proxy delivered under this DLL name"
    confidence: reported_not_verified
network_iocs_pending_direct_retrieval: true   # C2 domains/IPs + hashes reside in the Kaspersky primary, not the THN relay
tooling_new: [NightLedger, BridgeHead, ArcBridge]
tooling_prior_referenced: [TWOSTROKE, MiniFast, LIGHTRAIL, POLLBLEND]
cve_references: []
```

## Relationship to existing findings

- UNC1549 is roster actor #004 (last threat-box scoring 2026-05-09, weighted 5.4 →
  MEDIUM; espionage category HIGH composite 10). This finding is a net-new tooling
  update to that actor's tradecraft baseline — an actor_profile_update candidate.
- No prior UNC1549 / Nimbus Manticore FLASH in the last 24h. Net-new this window;
  distinct from the 08:00 morning-brief topics (CVE-2026-16812 Arista VeloCloud;
  CVE-2026-16723 Fastjson).

## Open questions for analyst

- **Alias-set extension (actor-profiler):** Kaspersky's alias cluster names five
  labels not in roster #004 (Nimbus Manticore, GalaxyGato, Mirage Kitten, Subtle
  Snail, TA455). Assess whether to extend #004's alias list. Record as Kaspersky's
  mapping; do not originate the merge (Hard Rule 2).
- **A&D relevance:** aviation vertical is named but victims are regional aviation
  orgs abroad — no US A&D prime / DIB / watchlist entity. A&D relevance is
  sector-level/structural. Analyst to assess portability of the new tunneling
  tooling (WebSocket covert relay) to an ITAR-enterprise M365/edge environment
  without extrapolating a prime victim (Hard Rule 2).
- **Corroboration tripwire:** single effective source (Kaspersky). Direct
  retrieval of the Securelist primary (network-IOC appendix) OR a genuinely
  independent second A/B primary with its own telemetry would lift credibility
  toward 1 and WEP toward "very likely" — at which point red-team review becomes
  mandatory.
