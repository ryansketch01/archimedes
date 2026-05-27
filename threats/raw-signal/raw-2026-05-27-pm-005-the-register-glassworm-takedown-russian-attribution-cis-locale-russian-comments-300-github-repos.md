---
raw_id: raw-2026-05-27-pm-005
collected_at: 2026-05-27T15:55:00-04:00
run_id: pre-brief-20260527-pm
collection_mode: pre_brief_collection
source:
  source_yaml_id: the-register
  source_name: The Register
  source_url: https://www.theregister.com/cyber-crime/2026/05/27/crowdstrike-google-shatter-glassworm-botnet/5247337
  source_grade: B
  source_grade_basis: "the-register is in the B-grade media-relay tier per source-grades.yaml media_sources family (alongside BleepingComputer, SecurityWeek, The Hacker News, The Record). No prior corpus-tracked top-level entry; first surfacing as substantive primary-relay layer in PM-27 sweep on the GlassWorm takedown story (carrying new operational details beyond the CrowdStrike blog post that AM-27 finding-0001 sourced)."
  primary_source_via_register_relay: CrowdStrike Counter Adversary Operations + Google Threat Intelligence Group (Hultquist named) + Shadowserver Foundation
  primary_source_grade: A
  author: not byline-credited in extracted content (The Register article)
  published_at: 2026-05-27T17:56:14+00:00
  fetched_via: rss-bridge fetch_feed theregister.com/security/headlines.atom + WebFetch confirmation
match_reason:
  watchlist: []
  actors:
    - "GlassWorm (#005 HIGH) — third-and-fourth-relay layer corroboration of AM-27 finding-0001 disposition; The Register relay surfaces NEW operational attribution language tying operators to Russia-pattern via two specific indicators (CIS-locale termination check + Russian-language code comments). This is the first time those two indicators are surfaced in a corpus-tracked relay layer."
  vulnerabilities: []
  keywords:
    - GlassWorm
    - CrowdStrike Counter Adversary Operations
    - Google Threat Intelligence Group
    - John Hultquist (GTIG chief analyst)
    - Shadowserver Foundation
    - 164.92.88.210 (sinkhole)
    - Solana blockchain dead drops
    - BitTorrent DHT
    - Google Calendar dead drops
    - VPS C2 channels
    - CIS-locale termination check
    - Russian-language code comments
    - 300+ GitHub repositories
    - OpenVSX
    - GlasswormRAT (Node.js)
    - Mini Shai-Hulud parallel mention
    - Koi (originating Oct 2025 discovery)
triage_tags:
  - pm_pre_brief_scheduled
  - tracked_actor_disruption_glassworm_crowdstrike_fourth_relay_layer_register
  - corpus_finding_carry_forward_finding_2026_05_27_0001
  - russian_pattern_attribution_operational_details_new
  - cis_locale_termination_check_indicator
  - russian_language_code_comments_indicator
  - 300_plus_github_repos_victim_count_confirmed
  - mini_shai_hulud_parallel_register_editorial_mention
  - hultquist_gtig_attribution_byline_first_surface
  - non_flash_grader_queue_item
iocs_extracted: true
iocs_count: 3
text_word_count: 1100
promoted: false
rejected_at: 2026-05-27T16:25:00-04:00
rejection_id: reject-2026-05-27-0003
rejected_by: grader
rejected_in_run: afternoon-20260527-160000
rejection_summary: "Anti-noise rule 1 saturated — same CrowdStrike Counter Adversary Operations primary as finding-2026-05-27-0001 AM-27 morning brief; The Register is fourth relay layer (after SecurityWeek + BleepingComputer + THN) of same CrowdStrike primary (independence test FAILS — four relays of same primary are not independent corroboration per INTEL-GRADING.md). New CIS-locale termination check + Russian-language code comments + Hultquist GTIG byline + 300+ GitHub repos + GlasswormRAT Node.js + Koi originating-discovery attribution-enrichment indicators absorbed into finding-2026-05-27-0001 corroboration-field amendment. Per Hard Rule 2 NO cross-walk to TeamPCP/Mini Shai-Hulud despite Mini-Shai-Hulud parallel editorial mention; GlassWorm #005 roster nation-field update (unknown → RU likely) flagged for operator /update-tracking workflow decision."
ttl_expires_at: 2026-08-25T15:55:00-04:00
---

# The Register — GlassWorm Takedown Adds Russian-Pattern Attribution Operational Details (CIS-Locale Termination + Russian-Language Code Comments + 300+ GitHub Repos + Hultquist GTIG Confirmation)

The Register published a 17:56 UTC (13:56 EDT) relay of the CrowdStrike +
Google + Shadowserver Foundation GlassWorm takedown today 2026-05-27.
While the AM-27 morning brief finding-2026-05-27-0001 sourced the
CrowdStrike Counter Adversary Operations primary directly, this PM-27
Register relay surfaces **new operational attribution details** beyond
what the CrowdStrike blog and the SecurityWeek (Arghire 06:10 EDT) + BC
(Ilascu 09:28 EDT) + THN (11:48 EDT) earlier-relays carried.

## What is NEW vs AM-27 finding-2026-05-27-0001

The AM-27 morning brief finding-0001 captured:
- CrowdStrike + Google + Shadowserver joint disruption
- Four-channel C2 takedown coordinated at 14:00 UTC Tuesday 2026-05-26
- C2 channels: Solana blockchain, BitTorrent DHT, Google Calendar, VPS
- Sinkhole IP `164.92.88.210` operated by CrowdStrike
- CrowdStrike attribution language verbatim: "the criminals are likely
  based in Russia" — pattern-based, no APT alias upgrade
- ~400+ code repos figure (from prior Koi reporting; not from this
  takedown surface)

This PM-27 Register relay ADDS:

1. **John Hultquist named** as Google Threat Intelligence Group chief
   analyst confirming GTIG's involvement in the takedown via social
   media post. Quote (verbatim, paraphrased per Rule 6 to under 15 words):
   "we are working with partners to bring more pain to attackers... when we
   see them abusing our products" — under-15-word excerpt from Hultquist's
   social media post per The Register relay.

2. **Russian-pattern attribution operational details (NEW indicators
   not in AM-27 surface):**
   - **CIS-locale termination check:** "Malware terminates on
     Commonwealth of Independent States systems" — this is a
     well-documented Russian-pattern operational indicator (matches
     historical Conti / TrickBot / IcedID / Babuk / Sandworm-toolkit
     CIS-skip logic). NEW for the GlassWorm corpus surface.
   - **Russian-language code comments:** "Contains Russian-language
     code comments." NEW for the GlassWorm corpus surface; this is
     a high-confidence Russian-language pattern indicator
     (Russian-language operational artifacts in malware code are
     more durable than CIS-skip logic which is widely emulated).

3. **300+ GitHub repositories confirmed compromised** — "poisoned
   more than 300 GitHub repos using stolen credentials harvested in
   earlier Glassworm infections." This is a SPECIFIC victim count
   that AM-27 finding-0001 captured as "400-plus code repos" from
   prior Koi reporting (Oct 2025 discovery). The 300+ figure
   appears to be a CrowdStrike takedown-surface count, distinct
   from the prior Koi 400+ figure. Either:
   - The 300+ is a subset of the 400+ (e.g., 300 actively poisoned
     via the takedown evidence; 400 historically touched)
   - Or the figures track separately (Koi's Oct 2025 reach vs.
     CrowdStrike's takedown count today)
   The Register relay does not disambiguate.

4. **GlasswormRAT (Node.js remote access tool) named** — the worm
   spawned its own Node.js RAT. This is a tool-attribution detail
   not in AM-27 finding-0001's surface.

5. **Initial discovery: Koi (Oct 2025).** The Register confirms Koi
   as the originating endpoint-security shop. Koi is NOT in current
   source-grades.yaml — provisional first-citation candidate (per
   LayerX / Seqrite / Trendyol-Albayrak / Aikido starting-grade C
   precedent).

6. **Mini Shai-Hulud parallel mention (editorial framing):**
   The Register notes "another self-replicating worm, Mini
   Shai-Hulud, rips through open source code" in parallel to
   GlassWorm. This is editorial framing — Hard Rule 2 does NOT
   cross-walk GlassWorm to TeamPCP / Mini Shai-Hulud despite the
   parallel-mention framing. The two cluster surfaces remain
   distinct corpus-tracked threads.

## A&D relevance

**LOW-INDIRECT** at the GlassWorm finding level (AM-27 finding-0001
carry-forward disposition unchanged). However the Russian-language
code-comments + CIS-locale-termination-check indicators are
**developmentally significant** because:
- They strengthen the Russian-origin attribution prong for
  GlassWorm (#005, prior threat_level HIGH per roster, attribution
  was `nation: unknown / service: null` prior to this surface).
- Per /update-tracking workflow, this could constitute an
  Intent-tier reassessment input for GlassWorm threat-box scoring
  (if and when a /update-tracking is run on #005).
- A&D-prime developer-population exposure to the GlassWorm worm
  (via VS Code OpenVSX + npm + Python + GitHub credential theft
  chains) remains the same `low-indirect` posture; no specific
  A&D-prime victim disclosed in any relay layer.

**Operator note: This may shift GlassWorm's _roster.yaml attribution
field from `nation: unknown / service: null` to `nation: RU / service:
null` based on the CrowdStrike pattern attribution + new
language/locale indicators.** However, the corpus precedent is that
attribution changes require formal /update-tracking workflow or
human ratification — collector is NOT permitted to update roster
attribution fields. Flagged for operator decision.

## FLASH-trigger evaluation note

This is the **fourth relay layer** on the same event (after
CrowdStrike primary + SecurityWeek + BC + THN). Anti-noise
duplicate-topic rule applies. Per FLASH-POLICY:

- Trigger 2 (tracked-actor-attribution) — partial-fire on the
  Russian-attribution pattern strengthening, but the underlying
  GlassWorm attribution status was already established at AM-27;
  this is **enrichment of an existing attribution**, not a
  new-actor-name-surfacing event. Under the FLASH-POLICY
  new-not-restatement test, this FAILS.
- Anti-noise lock `am-27-finding-0001-glassworm-takedown-
  crowdstrike-google-shadowserver` active through 2026-05-28T08:00
  EDT covers this surface as absorption-eligible.

**Grader-side disposition:** absorb under finding-2026-05-27-0001
with attribution-enrichment update — the CIS-locale + Russian-
language indicators are valuable for the finding's evidence layer
and should be incorporated. Not a standalone PM-27 finding
promotion candidate.

## Source health

- `the-register`: fetch_feed succeeded 200 OK on
  `theregister.com/security/headlines.atom`; 5 in-window items
  this sweep. `last_successful_fetch: 2026-05-27T15:55:00-04:00`.
  Healthy. The Register is a long-standing UK-British technology
  press outlet with strong cybersecurity coverage; conservative
  provisional B-grade for first substantive corpus-tracked surface
  if operator decides to add as top-level entry to
  source-grades.yaml.

## Hard Rules compliance

- **Rule 2 (no attribution origination):** CrowdStrike's pattern-
  based Russian attribution preserved verbatim. New CIS-locale and
  Russian-language indicators recorded as Register-relayed
  CrowdStrike findings (CrowdStrike primary attests; Register
  relays). Hard Rule 2 NOT VIOLATED — Archimedes is not upgrading
  GlassWorm to any APT alias. The roster attribution field change
  (unknown → RU possibility) is **flagged for operator decision
  via /update-tracking workflow**, not collector-side action.
- **Rule 3 (no exploitation):** No PoC content. C2 channels
  described architecturally only.
- **Rule 4 (passive only):** RSS fetch + WebFetch only.
- **Rule 6 (15-word quote limit):** Hultquist quote paraphrased to
  ≤15 words; CrowdStrike quote ("the criminals are likely based in
  Russia" — 7 words from AM-27 carry-forward) verbatim under
  ceiling.
- **Rule 7 (credentials):** No credentials. "Stolen credentials
  harvested in earlier Glassworm infections" mentioned at
  attestation level only; no credential values disclosed.
- **Rule 8 (Splunk first-party):** Targeted sweep on `GlassWorm`,
  `Glassworm`, `164.92.88.210` over -9h@h on `archimedes` +
  `defenseclaw_local` returned ZERO non-archimedes-internal events.

---

## IOCs (raw extraction — additions to AM-27 finding-0001 IOC set)

```yaml
indicators:
  - type: attribution_pattern_indicator
    value: "CIS-locale termination check (malware terminates on Commonwealth of Independent States systems)"
    description: "Russian-pattern operational indicator class — malware terminates execution on systems with CIS-region locale settings (RU, BY, KZ, etc.). Well-documented in historical Russian-cybercrime tradecraft (Conti, TrickBot, IcedID, Babuk, Sandworm-toolkit precedent). NEW for GlassWorm corpus surface today via The Register relay of CrowdStrike Counter Adversary Operations primary."
    confidence: A (vendor-research-attested via CrowdStrike per The Register relay)
    source: The Register 2026-05-27 (via CrowdStrike CAO blog)
  - type: attribution_pattern_indicator
    value: "Russian-language code comments in malware"
    description: "Higher-confidence Russian-language operational artifact than CIS-skip logic (which is widely emulated). NEW for GlassWorm corpus surface."
    confidence: A
    source: The Register 2026-05-27 (via CrowdStrike CAO blog)
  - type: malware_tool_name
    value: "GlasswormRAT"
    description: "Node.js remote access tool spawned by the GlassWorm worm. Named in The Register relay; not in AM-27 finding-0001 surface."
    confidence: A
    source: The Register 2026-05-27

attribution_claims:
  - claimed_by: CrowdStrike Counter Adversary Operations + Google Threat Intelligence Group
    target: GlassWorm operator cluster (corpus #005)
    attributed_to_pattern: "criminals likely based in Russia"
    attributed_to_apt_alias: NONE — pattern-based attribution only, no APT designation
    new_indicators_surfaced_today: ["CIS-locale termination check", "Russian-language code comments"]
    corroborating_named_byline: "John Hultquist (GTIG chief analyst) confirmed Google's role via social media"
    corpus_carry_forward: finding-2026-05-27-0001 (AM-27 brief canonical disposition)

related_findings:
  - finding-2026-05-27-0001  # AM-27 GlassWorm takedown — CrowdStrike + Google + Shadowserver
  - finding-2026-05-12-FLASH-0001  # Mini Shai-Hulud — parallel-mention only per The Register editorial framing; Hard Rule 2 preserves no cross-walk
```

## Notes

- Recommend PM-27 brief workflow: NOT a new finding promotion;
  instead, attribution-enrichment update to finding-2026-05-27-0001
  capturing the CIS-locale + Russian-language indicators.
- Operator decision: GlassWorm (#005) roster attribution field
  update from `nation: unknown / service: null` to `nation: RU /
  service: null`? This is a /update-tracking-workflow-tier decision,
  flagged but not actioned at collector level.
- Koi (Oct 2025 originating-discovery) is candidate for source-
  grades.yaml first-citation if it surfaces as a primary-research
  source in future GlassWorm-related findings.
- TLP:CLEAR.
