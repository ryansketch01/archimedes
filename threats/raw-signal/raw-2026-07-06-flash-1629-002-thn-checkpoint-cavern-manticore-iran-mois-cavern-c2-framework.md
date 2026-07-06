---
raw_id: raw-2026-07-06-flash-1629-002
collected_at: 2026-07-06T16:44:00-04:00
run_id: flash-sweep-20260706-162900
collection_mode: flash_sweep
source:
  source_yaml_id: thehackernews
  source_name: The Hacker News
  source_url: https://thehackernews.com/2026/07/iran-linked-hackers-use-new-cavern-c2.html
  published_at: 2026-07-06T14:34:26-04:00
match_reason:
  watchlist: [aerospace-defense]        # aviation sector named among targets (not a watchlist-prime)
  actors: []                            # Cavern Manticore NOT in _roster.yaml; overlap-only to #022 MuddyWater / #023 OilRig
  vulnerabilities: [CVE-2025-52691, CVE-2025-68613, CVE-2025-9316, CVE-2025-34291, CVE-2025-54068]
  keywords: [Iran, MOIS, Cavern, Cav3rn, MuddyWater, Lyceum, OilRig, aviation, Israel]
triage_tags: [iran_cyber_watch, new_tooling, new_actor_candidate, ttp_change_watch, attribution_overlap_hard_rule_2]
iocs_extracted: true
iocs_count: 13
text_word_count: 240
promoted: true
promoted_to_finding: finding-2026-07-06-0001
promoted_at: 2026-07-06T16:56:00-04:00
ttl_expires_at: 2026-10-04T16:44:00-04:00
---

# Iran-Linked Hackers Use New Cavern C2 Framework to Target Israeli Organizations

The Hacker News (2026-07-06), relaying Check Point Research, reports a
previously undocumented modular command-and-control framework named
**Cavern (aka Cav3rn)** used against Israeli organizations, primarily IT
providers and government.

Attribution and tooling (as stated by Check Point Research — preserved
verbatim, not originated by Archimedes):

- **Cluster designation:** Check Point Research attributes the activity to
  a NEW cluster it calls **Cavern Manticore**, described as affiliated with
  Iran's Ministry of Intelligence and Security (MOIS).
- **Overlap claims (CPR's assessment, not an Archimedes cross-walk):**
  shares tactical overlaps with **MuddyWater** and **Lyceum** (Lyceum
  assessed by CPR as a subgroup of **OilRig**). CPR nonetheless designates
  Cavern Manticore as a distinct new cluster.
- **New tooling:** Cavern is a newly documented modular C2 framework —
  "a mature and adaptable toolset built around a shared .NET foundation."
- **Targeted sectors:** IT providers, government, aviation, energy, public
  sector.
- **Targeted countries:** Israel (primary), Egypt, United Arab Emirates.
- **Named victims:** none identified.

---

## Extraction notes

- Language: en
- Publisher byline: The Hacker News (relaying Check Point Research primary)
- Article type: news / vendor-research relay
- Raw IOC extraction invoked: yes
- FLASH trigger mapping — GRADER TO ADJUDICATE (collector does not
  originate attribution per Hard Rule 2):
  - **Trigger 2 (new-attribution-tracked-actor): NOT cleanly met.** Cavern
    Manticore is a NET-NEW cluster, NOT in `_roster.yaml`. CPR's noted
    overlaps with MuddyWater (#022) and OilRig (#023) are CPR's assessment;
    Hard Rule 2 BINDING — Archimedes does NOT cross-walk a distinct
    CPR-designated cluster onto a roster actor. This is a `/new-actor`
    candidate (Cavern Manticore), operator-deferred.
  - **Trigger 4 (tracked-actor-ttp-change): marginal / grader call.** New
    modular .NET C2 framework (Cavern) is genuinely new tooling from an
    A-grade-tier source (Check Point Research). It is attributable to a
    tracked actor ONLY if the grader accepts CPR's MuddyWater/OilRig
    overlap as attribution — which Hard Rule 2 discipline argues against.
    Recorded as TTP-change WATCH, not an originated trigger.
  - **Trigger 5 (ad-sector-campaign): marginal fail.** Aviation is named
    among targeted sectors, but no A&D-prime watchlist entity is named and
    victims are Israeli/Egyptian/UAE IT-provider/government orgs — not
    A&D-prime direct targeting. Multi-victim/multi-country but not
    A&D-sector-anchored.
- Iran Cyber Watch relevance: HIGH. MOIS-affiliated, new C2 framework,
  aviation among targets. Strong substrate for actor-profiler review and
  a `/new-actor` Cavern Manticore candidacy.
- Hard Rule 2 preserved: MuddyWater / Lyceum / OilRig overlaps recorded as
  CPR's language; NO roster cross-walk originated. Hard Rule 3: exploited
  CVEs referenced by ID only, no exploit content.

## IOCs (from ioc-extraction skill)

iocs:
  - type: domain
    value: hospitalinstallation[.]com
    role: c2
    first_seen: 2026-07-06
  - type: filename
    value: uxtheme.dll
    role: sideloaded_or_malicious_dll
  - type: filename
    value: n-HTCommp.dll
  - type: filename
    value: mhm.dll
  - type: filename
    value: db.dll
  - type: filename
    value: ode.dll
  - type: filename
    value: n-ten.dll
  - type: filename
    value: n-sws.dll
  - type: cve
    value: CVE-2025-52691
    role: exploited_by_actor
  - type: cve
    value: CVE-2025-68613
    role: exploited_by_actor
  - type: cve
    value: CVE-2025-9316
    role: exploited_by_actor
  - type: cve
    value: CVE-2025-34291
    role: exploited_by_actor
  - type: cve
    value: CVE-2025-54068
    role: exploited_by_actor
attribution_claims:
  - actor_as_named_by_source: "Cavern Manticore (NEW cluster)"
    attributing_source: "Check Point Research (via The Hacker News)"
    attribution_language: "affiliated with Iran's MOIS; tactical overlaps with MuddyWater and Lyceum (OilRig subgroup)"
    is_new: true
    roster_match: false           # NOT in _roster.yaml; Hard Rule 2 blocks origination of a cross-walk
    note: "Overlap-to-tracked-actor is CPR's assessment; recorded verbatim, not originated."
