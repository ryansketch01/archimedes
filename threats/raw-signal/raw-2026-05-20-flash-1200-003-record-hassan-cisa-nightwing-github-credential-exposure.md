---
raw_id: raw-2026-05-20-flash-1200-003
collected_at: 2026-05-20T12:12:00-04:00
run_id: flash-sweep-20260520-120000
collection_mode: flash_sweep
test: false
source:
  source_yaml_id: the-record
  source_name: "The Record from Recorded Future News — relay of Brian Krebs original reporting"
  source_url: https://therecord.media/hassan-presses-cisa-github-leak
  published_at: 2026-05-20T08:11:00-04:00
match_reason:
  watchlist: []        # Hard Rule 2: Nightwing's RTX-spin-off lineage not vendor-attested in this article
  actors: []
  vulnerabilities: []
  keywords:
    - Nightwing
    - government contractor
    - Senator Maggie Hassan D-NH
    - CISA acting director letter
    - Brian Krebs reporting
    - GitHub public repository
    - AWS credentials exposure
    - cloud keys plaintext passwords logs
    - two-day window keys remained valid
triage_tags:
  - in_window
  - the_record_b_grade_relay
  - krebs_b_grade_originating_reporter_via_relay
  - cisa_a_grade_official_response_no_compromise_indication
  - nightwing_ad_lineage_per_public_osint_NOT_vendor_attested_in_article
  - hard_rule_2_no_ad_lineage_origination_via_relay
  - exposure_not_intrusion_no_active_campaign
  - no_actor_named
  - flash_trigger_5_fail_no_active_campaign_clause
  - non_flash_grader_review_candidate_ad_adjacency
  - splunk_first_party_zero_hits_49th_consecutive_dormant_sweep
  - github_repository_credential_exposure_class
  - federal_contractor_credential_hygiene_signal
iocs_extracted: false
iocs_count: 0
text_word_count: 280
promoted: false
ttl_expires_at: 2026-08-18T12:12:00-04:00
---

# Senator presses CISA for answers about alleged GitHub repository leak

## Article body summary (extracted)

The Record relays that Senator Maggie Hassan (D-NH) sent a letter on
Tuesday 2026-05-19 to the acting director of CISA demanding answers about
an alleged breach uncovered by cybersecurity reporter Brian Krebs involving
government contractor Nightwing.

**Article-attested facts:**

- Public GitHub repository containing exposed credentials of Nightwing
- Data alleged: AWS credentials and tokens, cloud keys, plaintext passwords,
  logs
- AWS keys "remained valid for two more days" after discovery before being
  removed
- CISA acknowledgement: "Currently, there is no indication that any
  sensitive data was compromised as a result of this incident"
- Senator Hassan's letter seeks CISA response on the incident posture

**Article-NOT-attested:**

- Nightwing's corporate lineage (publicly known as 2024 spin-off of
  Raytheon Intelligence & Space / RTX subsidiary, but NOT stated in The
  Record article — Hard Rule 2 prevents Archimedes-side origination of
  the RTX-watchlist link via this relay)
- Threat actor name or attribution (no actor identified)
- Active exploitation OR claim of stolen data being weaponized (CISA
  posture is "no indication of compromise")
- CVE
- IOCs

## Roster + watchlist + vuln evaluation

- _roster.yaml: no actor named in article; no roster match
- aerospace-defense.yaml watchlist: **Nightwing is NOT directly listed
  in aerospace-defense.yaml** (the watchlist enumerates RTX Corporation
  with subsidiaries Raytheon, Collins Aerospace, Pratt & Whitney — NOT
  Nightwing). Nightwing's RTX-spin-off lineage is public OSINT but the
  watchlist's current state does NOT enumerate it as a subsidiary. The
  watchlist was last_updated 2026-04-18 per file metadata — pre-dating
  the operator's potential awareness of Nightwing as a separate
  watchlist-worthy entity. Per Hard Rule 2 + collector doctrine the
  collector does NOT edit watchlist files; surface only.
- _index.yaml: no tracked CVE
- _master-index.yaml: no IOC

## FLASH trigger evaluation

- **T1 (critical-cve-exploited):** FAIL — no CVE
- **T2 (tracked-actor-attribution new):** FAIL — no actor named
- **T3 (first-party IOC hit):** FAIL — no IOCs to query; broader -24h
  Splunk sweep returned zero events on tracked superset
- **T4 (tracked-actor TTP change):** FAIL — no actor; credential exposure
  via public repo is not actor-tradecraft
- **T5 (ad-sector-campaign):** FAIL on multiple conditions:
  - article_describes_active_campaign: FAIL — passive credential exposure
    incident with CISA investigating; "no indication of compromise" posture
  - multi_victim_confirmed: FAIL — single contractor exposure, not
    multi-victim
  - targets_include_aerospace_defense_or_watchlist_entity: PARTIAL —
    Nightwing's RTX-spin-off lineage per public OSINT places it in the
    A&D ecosystem, but (a) NOT vendor-attested in this article and (b) NOT
    enumerated in current aerospace-defense.yaml watchlist. Strict-read
    of FLASH-POLICY trigger condition fails because Archimedes cannot
    originate the A&D-watchlist linkage from this relay.
- **T6 (zero-day no patch):** FAIL — no vulnerability

## Why surface as raw-signal anyway

Three reasons:

1. **A&D-adjacency signal per public OSINT.** Nightwing's RTX-spin-off
   status is well-known in defense industry trade press (Defense News,
   Breaking Defense, etc.). Even though this Record relay does NOT
   vendor-attest the lineage and Archimedes does not originate the
   linkage per Hard Rule 2, the grader / briefer may want to cite the
   public OSINT separately when composing the morning brief's A&D
   Sector Focus section. Surfacing the raw-signal preserves the
   collection option without violating Hard Rule 2.
2. **Federal-contractor credential-hygiene signal.** The two-day-valid
   AWS keys window is operationally diagnostic: it indicates Nightwing's
   credential-rotation cadence on discovery-to-revoke is multi-day, NOT
   minutes. This pattern is a recurring soft signal in A&D-prime supply
   chains; carrying the data point forward enables longitudinal pattern
   tracking across multiple exposure incidents.
3. **CISA response posture.** "No indication of compromise" is the
   strongest CISA disposition language short of full all-clear; carry
   forward for grader's discretion on whether to UPDATE the brief if
   subsequent reporting strengthens or weakens that posture.

## Recommendation flag (for librarian / operator review, NOT collector
## action)

The aerospace-defense.yaml watchlist may benefit from a human-edit pass
to enumerate notable post-2024 A&D-prime spin-offs (Nightwing from RTX;
others as relevant). The collector cannot edit the watchlist. The flag is
informational; operator decides if a `/update-tracking` or watchlist
human-edit pass is warranted.

## Hard Rules compliance

- Rule 2: Nightwing RTX-spin-off lineage NOT propagated as Archimedes
  origination; the public-OSINT linkage is separately citable by the
  grader / briefer but the collector preserves the article-attested-only
  framing in this raw-signal
- Rule 3: no PoC content
- Rule 4: passive-only — no scan of Nightwing infrastructure;
  authorized-targets.yaml empty; only RSS retrieval of public news
- Rule 6: no >15-word quotes (the CISA "no indication of compromise"
  string is 9 words)
- Rule 7: copyright discipline preserved
- Rule 8: Splunk first-party silence continues on tracked-IOC superset
  (no Nightwing-specific IOCs to query; broader sweep zero hits)

## TLP marking

TLP:CLEAR — public news source (The Record); CISA official acknowledgement
language; no first-party telemetry content; no PII (Senator Hassan is a
named public figure acting in official capacity, freely reportable per
GDPR Operational Rules in LEGAL-POLICY).
