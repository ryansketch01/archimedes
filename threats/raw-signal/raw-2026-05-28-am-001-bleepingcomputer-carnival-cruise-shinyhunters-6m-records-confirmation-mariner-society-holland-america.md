---
raw_id: raw-2026-05-28-am-001
collected_at: 2026-05-28T07:38:00-04:00
run_id: pre-brief-2026-05-28-am
collection_mode: pre_brief_collection
source:
  source_yaml_id: bleepingcomputer
  source_name: BleepingComputer (Sergiu Gatlan)
  source_url: https://www.bleepingcomputer.com/news/security/carnival-cruise-confirms-data-breach-affecting-nearly-6-million-people/
  published_at: 2026-05-28T10:49:27+00:00
  publication_date_evidence: "RSS feed item dated 2026-05-28T10:49:27 UTC = 06:49:27 EDT, ~48m before this raw-signal collection at 07:38 EDT. Single-byline single-source for the breach-confirmation layer. ShinyHunters self-claim layer dates back to April 2026 (per article body, claim cited but no link to original claim-post). Carnival Corp customer-notification disclosure is the procedural anchor — BleepingComputer's reporting cites the notification filing without quoting Carnival Corp 8-K SEC filing directly."
secondary_source: null    # No A-grade or B-grade independent corroboration of the 5,995,277-records confirmation figure at this sweep moment. SecurityWeek, The Hacker News, The Record, Krebs all silent on Carnival Cruise in the AM-28 window.

match_reason:
  watchlist: []
  actors:
    - "ShinyHunters (self-claim, criminal extortion gang) — NOT directly a tracked roster ID but FORMALLY aliased as Bling Libra (Unit 42 cluster mapping per finding-2026-05-27 / Out of the Crypt extortion-economy piece AM-003 today). ShinyHunters / Scattered LAPSUS$ Hunters cluster has historical operational overlap with roster #013 Scattered Spider (alias UNC3944 + 0ktapus + Muddled Libra per Unit 42 alias mapping)."
  vulnerabilities: []    # No CVE referenced in the article
  keywords:
    - Carnival Corporation
    - Carnival Cruise
    - Holland America Line
    - Mariner Society loyalty program
    - ShinyHunters
    - Salesforce
    - Salesforce Aura
    - Salesloft Drift
    - social engineering
    - employee account compromise
    - 5,995,277 customers

triage_tags:
  - b_grade_single_source_breach_confirmation
  - extortion_gang_self_claim_corroborated_by_victim_notification
  - shinyhunters_claim_april_2026_confirmed_today
  - shinyhunters_bling_libra_unit42_alias_via_am_003_today
  - salesforce_aura_data_theft_pattern_continues
  - salesloft_drift_campaign_lineage
  - social_engineering_employee_target_april_2026
  - cruise_industry_consumer_breach_no_ad_relevance_direct
  - hard_rule_2_attribution_language_preserved_carnival_did_not_confirm_shinyhunters

iocs_extracted: false
iocs_count: 0
text_word_count: 870
promoted: true
promoted_to_finding: finding-2026-05-28-0001-bleepingcomputer-carnival-cruise-shinyhunters-6m-records-confirmation-mariner-society-holland-america
promoted_at: 2026-05-28T07:55:00-04:00
promoted_in_run: morning-20260528-080000
ttl_expires_at: 2026-08-26T07:38:00-04:00
---

# Carnival Cruise confirms data breach affecting nearly 6 million people

## Primary source

**BleepingComputer**, Sergiu Gatlan, published 2026-05-28T10:49:27 UTC =
06:49:27 EDT. URL:
https://www.bleepingcomputer.com/news/security/carnival-cruise-confirms-data-breach-affecting-nearly-6-million-people/

Single-byline single-source for the breach-confirmation layer. The
ShinyHunters self-claim layer dates back to April 2026 (per article body,
no link to original criminal-forum claim-post in this BleepingComputer
relay).

Source-grade resolution: `bleepingcomputer` is provisional-B per
source-grades.yaml at last_updated 2026-05-20. Per Hard Rule 2,
attribution language preserved verbatim — "ShinyHunters extortion gang
claimed responsibility" / "Carnival spokesperson didn't reply when
BleepingComputer reached out to confirm ShinyHunters' claims." NO
Archimedes-originated attribution upgrade; ShinyHunters layer remains
self-claim-with-victim-confirmation-of-incident-only.

## Carnival Corporation breach summary

Per BleepingComputer relay of Carnival Corporation's customer-notification
filing:

**Victim:** Carnival Corporation, world's largest cruise line operator.
Holland America Line is the operating subsidiary impacted (Mariner Society
loyalty program references in the data set).

**Affected count:** 5,995,277 customers notified (rounded "nearly 6
million" in headline).

**Initial-access vector:** Social engineering targeting an employee
account. Per Carnival's notification (paraphrased): "an unauthorized
actor used social engineering to deceive an employee to gain access to a
limited portion of the Company's IT system." Carnival did NOT name
Salesforce in the notification (article does NOT confirm Salesforce
implication directly, but observes broader ShinyHunters / Salesforce
targeting pattern: "ShinyHunters has been targeting Salesforce customers
and has breached hundreds of companies worldwide" via Salesloft Drift
campaign and Salesforce Aura data-theft attacks).

**Incident timeline (per Carnival notification):**
- 2026-04-14: initial unauthorized activity detected
- 2026-04-22: data theft confirmed
- 2026-05-28: customer notification + public confirmation

**Data exposed:**
- Names
- Dates of birth
- Email addresses
- Genders
- Geographic locations
- Loyalty program details (Mariner Society / Holland America Line)

NO payment-card data, NO Social Security numbers, NO passport numbers
referenced in Carnival's notification per the BleepingComputer relay.

## ShinyHunters self-claim layer

Per BleepingComputer body (paraphrased + verbatim quote):

> "ShinyHunters extortion gang claimed responsibility in April 2026."

The gang alleged stealing "over 8.7 million records and terabytes of
corporate data." Carnival's confirmation today is 5,995,277 records —
materially below the ShinyHunters self-claim figure. The differential
(~2.7 million records or ~31% lower than the criminal claim) is consistent
with the historical ShinyHunters pattern of overstating breach impact in
extortion negotiations.

**Critical attribution-preservation note (Hard Rule 2):**
Carnival has NOT confirmed the ShinyHunters attribution. The BleepingComputer
article explicitly states: "Although a Carnival spokesperson didn't reply
when BleepingComputer reached out to confirm ShinyHunters' claims." Per
Hard Rule 2, the attribution layer reads:

- **Procedural fact (confirmed):** Carnival Corporation experienced a
  social-engineering-mediated breach affecting 5,995,277 customers,
  initial unauthorized activity 2026-04-14.
- **Attribution claim (self-claim, not confirmed by victim):** ShinyHunters
  extortion gang claimed responsibility in April 2026, alleging 8.7M+
  records and terabytes of corporate data.

Grader should NOT upgrade ShinyHunters attribution beyond "claimed
responsibility" / "extortion gang self-claim" — Carnival has NOT
publicly confirmed the attribution and BleepingComputer relays the
self-claim without independent corroboration.

## ShinyHunters operational context (per BleepingComputer body)

The article situates Carnival within the broader ShinyHunters / Salesforce-
targeting pattern:

> "Over the past year, ShinyHunters has been targeting Salesforce customers
> and has breached hundreds of companies worldwide."

Specific campaign lineages cited:
- **Salesloft Drift campaign** — Salesforce CRM data theft via Drift
  marketing-automation integration compromise. Historical context only;
  Carnival not confirmed as a Drift-campaign victim in this relay.
- **Salesforce Aura data-theft attacks** — exploitation of Salesforce
  Aura framework for unauthorized data export. Historical context only;
  Carnival not confirmed as an Aura-campaign victim.

Neither Salesloft Drift nor Salesforce Aura is named in Carnival's own
notification per the BleepingComputer relay. The Salesforce-implication
layer is BleepingComputer editorial framing connecting Carnival to the
broader ShinyHunters campaign pattern, NOT a Carnival-attested incident
detail.

## Cross-corpus mapping to Unit 42 AM-003 Out of the Crypt piece

Today's Unit 42 "Out of the Crypt" extortion-economy piece (raw-signal
AM-003 this sweep) FORMALLY codifies the alias mapping:

- **Bling Libra = ShinyHunters** (Unit 42 cluster ID)
- **Scattered LAPSUS$ Hunters** = data-extortion alliance Bling Libra +
  Scattered Spider + LAPSUS$ Group operate within
- **Bling Libra TTPs per Unit 42:** SaaS-focused vishing, DDoS, media
  leaks, phishing sites designed to intercept credentials and MFA codes,
  device registration for persistence, reuses same Tox ID across victims,
  Tor-based data leak site

The Carnival confirmation today (April-2026 incident, employee-account
social-engineering vector, Salesforce-customer-targeting pattern) maps
to the Bling Libra TTP profile per Unit 42 — but Archimedes does NOT
originate that explicit mapping for Carnival's specific incident per
Hard Rule 2. The Bling Libra = ShinyHunters formalization is Unit 42's;
the Carnival-as-Bling-Libra-victim extension would be a NOVEL attribution
that Archimedes must NOT originate.

## A&D-relevance assessment

**Sector:** Cruise / hospitality consumer breach. NO direct A&D /
aerospace / defense / government contractor exposure.

**Indirect A&D-relevance:** The ShinyHunters / Bling Libra / Scattered
LAPSUS$ Hunters TTP profile (SaaS-focused vishing, Salesforce-customer
targeting, employee-account social engineering with sub-hour escalation,
Tor-based extortion leak sites) is operationally portable to ANY
Salesforce-using enterprise — INCLUDING A&D primes. Boeing, Lockheed
Martin, RTX, Northrop Grumman, GD, BAE, L3Harris, Leidos, SAIC all use
Salesforce or Salesforce-class CRM platforms in some capacity. The TTP
template is portable; the Carnival incident is one data-point in the
broader ShinyHunters / Salesforce campaign.

This raw-signal is recorded for grader awareness as TTP-template
context. The breach itself is NOT A&D-sector — DISCARDED from
ad-sector standing section. The TTP relevance is captured under the
broader Unit 42 Out of the Crypt piece (AM-003) which the briefer
can use for the Threat Detection Weekly or Ransomware Watch standing
sections if those activate.

## Source-grade triage tags

- BleepingComputer — provisional-B per source-grades.yaml; consistent
  relay-quality on breach confirmations including ShinyHunters lineage
  pieces.
- ShinyHunters self-claim — extortion-group self-claim with named C2 /
  TTP profile per Unit 42 Bling Libra mapping; treated as B-grade for
  the procedural-fact layer (claim existence) and C-grade for the
  attribution layer (no independent corroboration that Carnival's
  breach was specifically ShinyHunters / Bling Libra operation vs.
  another opportunistic actor leveraging similar TTPs).
- Carnival Corp customer-notification disclosure — A-grade procedurally
  (victim-self-disclosure on own incident is procedurally A-grade per
  the established precedent class — F5 K000160932, kernel.org netdev,
  Cisco PSIRT, OpenAI security communications, GitHub blog self-
  disclosure, LiteSpeed advisory).

Single-source veto applies to the attribution layer (BleepingComputer
sole-relay; ShinyHunters self-claim layer un-corroborated by victim).
WEP ceiling for the attribution layer: "likely" (per single-source
veto + extortion-gang-self-claim class). WEP for the procedural breach-
confirmation layer: "very likely" (victim-self-disclosure A-grade
procedurally + BleepingComputer relay consistency).

## Quotes preserved verbatim (≤15 words each, per Hard Rule 7)

1. "An unauthorized actor used social engineering to deceive an employee
   to gain access" (Carnival notification, per BleepingComputer).
2. "Although a Carnival spokesperson didn't reply when BleepingComputer
   reached out" (BleepingComputer).
3. "Over the past year, ShinyHunters has been targeting Salesforce
   customers and has breached hundreds" (BleepingComputer).

## Cross-link awareness for grader

- **Carnival as Bling Libra victim?** Unit 42 Out of the Crypt piece
  (AM-003 this sweep) does NOT name Carnival. The Bling Libra =
  ShinyHunters formalization is operational TTP mapping, not an
  exhaustive victim-list.
- **Scattered Spider operational overlap?** Unit 42 names Scattered
  LAPSUS$ Hunters as the cluster Bling Libra operates within — and
  Scattered Spider = roster #013 (aliases UNC3944, Octo Tempest,
  0ktapus, Scatter Swine, Muddled Libra, Starfraud per _roster.yaml).
  Cross-roster relevance is OPERATIONAL CLUSTER ADJACENCY, not direct
  Scattered-Spider attribution for Carnival. Briefer / grader should
  NOT upgrade Scattered Spider involvement in the Carnival incident
  per Hard Rule 2.
- **Wider ShinyHunters campaign list reachable from open sources?**
  BleepingComputer notes "hundreds of companies worldwide" but does
  NOT enumerate the list. The Charter Communications confirmation
  from raw-2026-05-27-am-007 yesterday is part of the same broader
  campaign per BleepingComputer's editorial framing — but Carnival
  + Charter are distinct incidents (April 2026 vs ~April 2026
  Salesforce vishing per yesterday's coverage).

## Disposition for grader

- **Anti-noise lock check:** PM-27 had NO ShinyHunters / Carnival
  specific lock. AM-27 brief covered Charter Communications under
  the same broader campaign umbrella (finding-2026-05-27-0002 via
  raw-2026-05-27-am-007). Today's Carnival raw-signal is potentially
  CLUSTERED with the Charter finding for grader-side anti-noise
  evaluation — same actor cluster, distinct named victims, both
  Salesforce / SaaS-focused vishing pattern. Grader may either: (a)
  promote Carnival as standalone-finding with cross-link to Charter
  cluster + AM-003 Unit 42 Bling Libra mapping; (b) absorb under
  existing ShinyHunters-campaign anti-noise lock as cluster
  enrichment. Recommend option (a) given Carnival's 6M-records scale
  + cruise-industry first-named-victim-in-corpus.
- **WEP recommendation:** procedural-facts very_likely (Carnival self-
  disclosure A-grade procedurally); attribution-layer likely (single-
  source BleepingComputer + ShinyHunters self-claim un-corroborated by
  victim). Single-source veto applied.
- **A&D-relevance:** indirect (TTP-template portability) — NO direct
  A&D-sector targeting in this incident. Briefer should NOT place
  Carnival under the Aerospace & Defense standing section.
- **Cross-link to AM-003 Unit 42 Out of the Crypt:** YES — same
  Bling Libra alias-mapping context. The Carnival incident is the
  named-victim corroboration data-point for the AM-003 Unit 42
  TTP-cluster piece this same brief cycle.
