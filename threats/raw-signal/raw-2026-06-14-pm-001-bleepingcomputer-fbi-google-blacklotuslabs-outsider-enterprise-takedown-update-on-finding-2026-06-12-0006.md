---
raw_id: raw-2026-06-14-pm-001
collected_at: 2026-06-14T15:40:00-04:00
run_id: pre-brief-20260614-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: bleepingcomputer
  source_name: "BleepingComputer"
  source_url: https://www.bleepingcomputer.com/news/security/fbi-disrupts-massive-ai-powered-phishing-service-using-a-million-urls/
  published_at: 2026-06-14T10:36:23-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [outsider_enterprise, phaas, fbi_takedown, google_civil_suit_update, black_lotus_labs, china_based_phishing, smishing]
triage_tags: [update_candidate, fbi_takedown, china_based_actor, phaas_cluster, ad_sector_not_targeted, anti_noise_carry_candidate]
iocs_extracted: true
iocs_count: 0
text_word_count: 580
promoted: true
promoted_to_finding: finding-2026-06-14-0001-bleepingcomputer-fbi-google-blacklotuslabs-outsider-enterprise-operational-takedown-update-on-finding-2026-06-12-0006
promoted_at: 2026-06-14T15:55:00-04:00
update_relationship_parent_finding: finding-2026-06-12-0006-thn-helpnetsecurity-google-civil-suit-outsider-enterprise-china-based-smishing-phaas-gemini-ai-weaponization-no-nation-state-attribution
ttl_expires_at: 2026-09-12T15:40:00-04:00
---

# FBI disrupts massive AI-powered phishing service using a million URLs (BleepingComputer, 2026-06-14)

## Source metadata

- Publisher: BleepingComputer
- Byline: Bill Toulas
- URL: https://www.bleepingcomputer.com/news/security/fbi-disrupts-massive-ai-powered-phishing-service-using-a-million-urls/
- Published: 2026-06-14T14:36:23 UTC = 10:36 EDT
- Source grade per `source-grades.yaml`: B (BleepingComputer baseline established)
- Article type: relay of FBI + Google + Black Lotus Labs joint announcement; operational-takedown coverage

## Article summary (article paraphrase per Hard Rule 7 quote discipline)

In a coordinated effort, the FBI — working with Google and Lumen's Black Lotus Labs — dismantled a Chinese phishing-as-a-service operation called Outsider Enterprise.

Reported scale: 9000 fake websites and more than a million fraudulent URLs at peak; administration-server seizures (quantity-only, no IOC detail in BleepingComputer article); Shopify e-commerce storefront leveraged in the kit distribution; Telegram bot used for buyer coordination.

Smishing channels at scale via AT&T, T-Mobile, and Verizon were impacted by the campaign (consumer mobile carrier infrastructure abuse, not A&D / DIB / aerospace / defense sector targeting).

Time-window reference in article: "two-week SMS campaign window" in May 2026; explicit disruption date NOT specified beyond the 2026-06-14 publication date.

## Attribution language preserved verbatim (per Hard Rule 2)

- Google: "based in China" (cluster geolocation)
- Google: "coordinating through Telegram" (operational comms layer)
- No FBI exploitation-detection-tag attribution beyond the joint-announcement framing
- No tracked-roster actor cross-walk in article (Outsider Enterprise NOT on `_roster.yaml`)
- No UNC / APT / Mandiant-cluster cross-reference in article

## A&D / DIB / aerospace / defense sector cross-walk: NEGATIVE

- No named A&D primes (watchlist clean: no Lockheed Martin, Boeing, RTX, Northrop Grumman, General Dynamics, BAE Systems, L3Harris, Leidos, SAIC, Thales, GE Aerospace, Safran, Honeywell, Airbus, Elbit)
- No DIB / CMMC supplier-network mention
- No DFARS / NIST 800-171 / ITAR context
- Consumer mobile carrier infrastructure (AT&T / T-Mobile / Verizon) is the named impacted layer — consumer credential-theft / payment-card theft, NOT A&D primes
- A&D-relevance: LOW (anti-noise carry candidate; UPDATE-on-prior-finding candidate; NOT a fresh A&D-direct surface)

## UPDATE-on-finding-2026-06-12-0006 substrate

Per orchestrator carry-forward binding, this article serves as the **operational-takedown layer** on top of finding-2026-06-12-0006 (Google civil-suit + Gemini AI weaponization substrate, published 2026-06-12 PM brief).

What is net-new vs. finding-2026-06-12-0006:
1. **FBI operational disruption** vs. prior Google civil-suit (civil vs. criminal-law-enforcement layer)
2. **Black Lotus Labs (Lumen) as third joint participant** — corroborates Lumen's prior independent visibility into the cluster
3. **Administration-server seizures** (operational-takedown class) — Google civil-suit substrate did NOT include seizure language; this is FBI-operational layer
4. **Cross-confirmation of "million URLs" scale claim** — the prior Google civil-suit substrate carried this scale figure; FBI takedown independently confirms it operationally

What is NOT net-new vs. finding-2026-06-12-0006:
1. The Gemini AI weaponization narrative is NOT restated in the 06-14 article — that layer remains the prior finding's substrate
2. No new IOCs / no new infrastructure detail / no new TTP-class observation
3. No new tracked-roster-actor attribution

## IOC extraction (from `ioc-extraction` skill, structured)

```yaml
iocs:
  domains: []
  ips: []
  urls: []
  hashes: []
  emails: []
  cves: []
  mitre_techniques: []
attribution_claims:
  - claim: "Outsider Enterprise — Chinese phishing-as-a-service operation"
    source: BleepingComputer (relaying Google + FBI + Black Lotus Labs joint announcement)
    confidence_language: "Based in China" (Google verbatim)
    confidence_level: assertive_factual_no_hedge
    tracked_actor_match: NONE (Outsider Enterprise NOT on `_roster.yaml`)
    extraction_notes: |
      Outsider Enterprise has corpus history as of finding-2026-06-12-0006
      (Google civil suit + Gemini AI weaponization layer, 12-Jun PM brief)
      and finding-2026-06-12-0006 already evaluated as NOT-on-roster
      cybercriminal cluster (operator-deferred /new-actor decision pending
      per operator binding). Today's article is operational-disruption
      layer on the same cluster, not fresh attribution; Hard Rule 2 binding
      preserved — no novel attribution, no roster cross-walk.
  - claim: "Black Lotus Labs corroboration (third joint participant)"
    source: BleepingComputer (relaying joint announcement)
    confidence_language: implied via joint-participation framing
    confidence_level: not_a_confidence_claim
    tracked_actor_match: NONE
    extraction_notes: |
      Lumen Black Lotus Labs joining the FBI / Google operational layer
      corroborates prior Lumen Volt Typhoon-adjacent / KV-takedown visibility
      pattern (finding-2026-06-10-0007 carry); does NOT cross-walk
      Outsider Enterprise to Volt Typhoon. Distinct cluster.
halts: []
```

## Disposition (grader handoff)

- **UPDATE-on-finding-2026-06-12-0006 candidate** for 16:00 EDT afternoon brief composition
- Trigger evaluation deferred to grader per orchestrator binding (COLLECTION ONLY)
- Anti-noise pre-evaluation: per morning brief substrate the operator binding said "no need to re-raise unless materially new" — operational-takedown layer (vs. civil-suit layer) MAY be materially new at grader discretion; if grader decides operational-disruption layer does NOT cross materiality threshold, then this raw-signal anti-noise-defers cleanly with no further surface in afternoon brief
- A&D-relevance: LOW (no DIB / DFARS / ITAR / watchlist-prime intersection)
- Net-new vs. prior corpus: limited to operational-disruption layer + Black Lotus Labs corroboration; no new attribution / no new IOC / no new TTP

## Extraction notes

- Language: en
- Article type: news relay of joint government / private-sector takedown announcement
- Raw IOC extraction invoked: yes; returned 0 IOCs (article contains quantity-only references to URLs / sites / sellers, no specific domains / IPs / hashes / URLs / emails)
- Hard Rule binding: Rule 1 (LEGAL-POLICY) — passive WebFetch on public-news article. Rule 2 (no attribution origination) — Google + FBI attribution language preserved verbatim, no novel attribution. Rule 3 (no exploitation assistance) — no PoC / exploit detail in article or extraction. Rule 4 (credentials radioactive) — no credential exposure in article. Rule 7 (15-word quote discipline) — quoted phrases all <=15 words ("Based in China" / "coordinating through Telegram" — 3 + 3 words). Rule 8 (Splunk first-party) — N/A this item; sentinel scan in `raw-2026-06-14-pm-000` covers Splunk-self-substrate.
- Operator-binding context: scheduled 15:30 EDT pre-brief collection for 16:00 EDT afternoon brief. COLLECTION ONLY — grader downstream determines anti-noise vs. UPDATE disposition.
