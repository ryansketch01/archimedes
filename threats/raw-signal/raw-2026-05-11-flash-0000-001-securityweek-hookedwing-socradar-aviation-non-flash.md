---
raw_id: raw-2026-05-11-flash-0000-001
collected_at: 2026-05-11T00:08:00-04:00
run_id: flash-sweep-20260511-000000
collection_mode: flash_sweep
sweep_type: flash
test: false
source:
  source_yaml_id: securityweek
  source_name: SecurityWeek (provisional B)
  source_url: https://www.securityweek.com/over-500-organizations-hit-in-years-long-phishing-campaign/
  primary_research_source: SOCRadar
  primary_research_source_grade: provisional_unknown_no_prior_archimedes_citation
  primary_research_url_not_yet_retrieved: true
  published_at: 2026-05-11T03:49:18+00:00
  author: Ionut Arghire
match_reason:
  watchlist: [aerospace-defense-aviation-sector-token]
  watchlist_match_strength: structural_not_direct
  watchlist_match_detail: |
    "Aviation" is one of 7 victim sectors listed but no named A&D
    prime (Lockheed, Boeing, RTX/Raytheon, Northrop Grumman, GD,
    BAE Systems, L3Harris, Leidos, SAIC, Thales, GE Aerospace,
    Safran, Honeywell Aerospace, Airbus, Elbit) appears in the
    SecurityWeek article. Aviation sector token is broad and
    includes commercial travel / airlines / airport authorities;
    structurally adjacent to the A&D-prime watchlist but not a
    direct watchlist-entity hit.
  actors: []
  vulnerabilities: []
  keywords: [phishing-campaign, multi-victim, aviation, github-hosted-infrastructure, microsoft-outlook-themed-lures, 4-year-active, socradar-primary]
triage_tags:
  - non_flash
  - flash_marginal_trigger_5_discarded
  - grader_queue_morning_brief_inventory_candidate
  - socradar_new_provisional_source_grade_log_candidate
  - hookedwing_brand_new_campaign_name_no_prior_corpus_coverage
  - ioc_extraction_deferred_pending_primary_socradar_publication_retrieval
iocs_extracted: false   # Specific IOCs (24 C&C servers, 100+ GitHub domains, dozen+ distribution domains) NOT in the SecurityWeek piece; would require WebFetch on SOCRadar primary publication for extraction
iocs_count: 0
text_word_count: 1100
promoted: true
promoted_to_finding: finding-2026-05-11-0002
promoted_at: 2026-05-11T08:10:00-04:00
ttl_expires_at: 2026-08-09T00:08:00-04:00
---

# Over 500 Organizations Hit in Years-Long Phishing Campaign

**SecurityWeek**, by **Ionut Arghire** — 2026-05-10T23:49 EDT
(2026-05-11T03:49:18 UTC)

URL: https://www.securityweek.com/over-500-organizations-hit-in-years-long-phishing-campaign/

> Victims span across the aviation, critical infrastructure,
> energy, logistics, public administration, and technology
> sectors.

(SecurityWeek lede / categorization snippet, 14 words — within the
15-word quote ceiling per LEGAL-POLICY §Copyright Discipline)

---

## Article content summary (extracted via WebFetch, paraphrased)

**Originating research:** SOCRadar — a cyber-threat-intelligence
vendor that documented and analyzed the campaign. SOCRadar
appears to be the primary source; SecurityWeek is the relay.

**Campaign name:** "Operation HookedWing" — researcher-coined
working name. No threat-actor group attribution and no nation /
state-service attribution claimed. SOCRadar describes the
"targeting pattern" as "not random" and notes "high geopolitical
relevance" but does not name a perpetrator.

**Duration:** 2022 → present (4+ years). Status described as
"ongoing" with "sustained activity through 2025" and an
"expanding infrastructure and lures" trajectory.

**Victim scope:** 500+ organizations across 7 sectors:
- Aviation and travel
- Critical infrastructure
- Energy
- Financial
- Government / Public administration
- Logistics
- Technology

No named victim organizations / no named A&D primes in the
SecurityWeek piece.

**Tactics, Techniques, Procedures (TTPs):**
- Initial access: phishing emails impersonating HR, colleagues,
  or notifications
- Lure themes 2022-2024: Microsoft Outlook themed pages
- Lure themes 2024-2025: expanded with French-language content
  and additional themes
- Pre-loader: full-screen overlay with organization-name
  personalization (suggests sector-specific or org-specific
  targeting curation, not commodity spray)
- Background script: performs email/URL validation and collects
  geolocation data (filters out sandboxes / off-target traffic)

**Infrastructure (aggregate counts only — specific IOCs not in
SecurityWeek piece):**
- Two dozen (~24) command-and-control servers
- 100+ GitHub-hosted domains / repositories
- Dozen+ distribution domains on other platforms

**CVEs exploited:** none mentioned.

**Named A&D primes / aviation primes:** none. "Aviation" is
listed at sector level only.

---

## FLASH trigger evaluation (recorded in primary sweep sentinel)

This item was the one in-window in-scope candidate for FLASH
evaluation in the 2026-05-10 18:00 → 2026-05-11 00:00 EDT window.
Full evaluation in the sister file
`raw-2026-05-11-flash-0000-000-sentinel-clean-sweep.md`. Summary:

- **Trigger 1 (CVE):** N/A — no CVE
- **Trigger 2 (tracked actor):** FAIL — no attribution claimed
- **Trigger 3 (first-party IOC hit):** FAIL — no IOCs available
  to Splunk-query, and Splunk dormant on external observations
- **Trigger 4 (TTP change):** FAIL — no tracked actor anchor
- **Trigger 5 (A&D-sector campaign):** MARGINAL → FAIL
  - "multi-victim": PASSED (500+ orgs)
  - "active": PASSED (ongoing through 2025)
  - "explicitly targeting A&D / watchlist": FAILED — aviation
    listed at sector level only, no named A&D primes
  - Anti-noise rule "B2 minimum grade": FAILED — SOCRadar
    has no prior Archimedes source-grade (provisional-C on
    first surface per LayerX / Seqrite / Trendyol precedent);
    SecurityWeek is provisional-B relay; composite source-grade
    is below the B2-minimum FLASH bar
- **Trigger 6 (zero-day no patch):** N/A — no vuln

**Disposition: NOT FLASH-worthy.** Raw-signaled here as a
non-FLASH grader-queue item for the next scheduled brief
(2026-05-11 morning brief at 08:00 EDT).

---

## Grader notes (for downstream subagent inheritance)

The grader inheriting this raw-signal should consider:

1. **Brand-new to the corpus** — grep on the threats/ tree confirms
   "HookedWing" and "SOCRadar" have ZERO prior occurrences in
   raw-signal, findings, briefs, or actor dossiers. No anti-noise
   precondition applies; this is the first surfacing.

2. **Watchlist-edge admission** — same pattern the briefer applied
   to the 2026-05-10 MacSync raw-signal (finding-2026-05-10-0001):
   structural / sector-adjacent rather than direct watchlist hit.
   Grader's call whether to:
   - Promote to a finding with explicit "aviation sector token,
     no named primes, monitoring tier" framing (LOW WEP /
     speculative likelihood, B/C grade) — useful corpus entry
     for trend-tracking but not actionable today
   - Reject promotion with logged reason (sector token alone
     does not clear watchlist threshold)
   - Hold for the morning brief's inventory / awareness section
     without finding promotion

3. **SOCRadar source-grade-log expansion candidate** —
   SOCRadar (https://socradar.io/) is a legitimate XTI vendor
   based in Turkey (similar founder profile to Trendyol Group /
   Berk Albayrak with regional research roots). Has been
   producing public threat-research reports since 2020. Initial-
   surface assessment per the LayerX / Seqrite / Trendyol
   precedent: provisional C with opportunity for upgrade as
   track record accumulates. Operator decision required for
   ratification; collector does not propose grades.

4. **IOC extraction deferred** — the SecurityWeek piece gives
   aggregate infrastructure counts (24 C&C, 100+ GitHub domains,
   dozen+ distribution domains) but no specific indicators.
   To populate first-party hunt opportunities (i.e., to Splunk-
   sweep for "any HookedWing GitHub-hosted domain ever surfaced
   in defenseclaw_local telemetry?"), the operator or grader
   would need to retrieve the underlying SOCRadar primary
   publication and extract domain / IP / hash IOCs. Recorded
   here as a deferred work item; not blocking the FLASH sweep.

5. **A&D-prime relevance** — INDIRECT / STRUCTURAL. The
   "aviation" sector overlap is shallow without named primes;
   the watchlist target profile (Tier-1 A&D primes engaged in
   military / spacecraft / missile / defense-systems work)
   typically operates in DEFENSE aviation, not the commercial-
   travel + airport-authority + flight-operator profile that
   "aviation" as a broad sector token tends to denote in
   threat-intel reporting. The grader should be careful not to
   over-promote on the sector-token coincidence.

6. **Possible "/new-source" trigger** — operator may want to
   add SOCRadar to source-grade-log.md as a new provisional
   source (C, awaiting ratification, similar profile to
   LayerX / Seqrite Labs / Trendyol-Group-Albayrak). This is a
   librarian-handoff item, not a grader one — flagging for
   visibility.

---

## Extraction notes

- **Language:** en
- **Publisher byline:** Ionut Arghire (SecurityWeek staff writer)
- **Article type:** vendor-research relay (news writeup)
- **Raw IOC extraction invoked:** NO — no specific IOCs in
  SecurityWeek piece; SOCRadar primary publication not yet
  retrieved (deferred for grader / operator decision)
- **Primary research source:** SOCRadar (provisional-unknown
  Archimedes source-grade; NO prior corpus citation; would be
  a new source-grade-log entry per the LayerX / Seqrite /
  Trendyol-Group-Albayrak precedent if/when ratified)
- **Hard-Rule 2 attribution discipline:** Article does NOT
  attribute the campaign to a named threat-actor group. This
  raw-signal does NOT originate an attribution claim. The
  campaign-name "Operation HookedWing" is a SOCRadar-coined
  working name with no nation / service / alias assignment.
- **Hard-Rule 7 copyright discipline:** One direct quote from
  the SecurityWeek piece (14 words, within the 15-word ceiling);
  no second quote.

## IOCs (from ioc-extraction skill)

ioc-extraction skill not invoked this raw-signal — no specific
indicators present in the SecurityWeek piece beyond aggregate
counts. Skill should be re-invoked if/when the SOCRadar primary
publication is retrieved and parsed in a follow-on collection.

```yaml
iocs_extracted: false
iocs_count: 0
attribution_claims: []
```
