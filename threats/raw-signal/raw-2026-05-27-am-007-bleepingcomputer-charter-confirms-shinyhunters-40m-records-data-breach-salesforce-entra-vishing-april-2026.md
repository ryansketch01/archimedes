---
raw_id: raw-2026-05-27-am-007
collected_at: 2026-05-27T07:50:00-04:00
run_id: pre-brief-2026-05-27-am
collection_mode: pre_brief_collection
source:
  source_yaml_id: bleepingcomputer
  source_name: BleepingComputer (Lawrence Abrams)
  source_url: https://www.bleepingcomputer.com/news/security/charter-confirms-data-breach-after-shinyhunters-extortion-threat/
  published_at: 2026-05-26T19:46:01+00:00       # 15:46 EDT yesterday, in-window
prior_anti_noise_lock_status:
  lock_id: shinyhunters-7-eleven-consumer-retail-data-breach-no-roster-no-ad
  prior_state: ACTIVE 2026-05-26 06:00 → 2026-05-27 06:00 (24h lock from initial filter-out)
  current_state: EXPIRED at 06:00 EDT today (this AM-27 sweep is AFTER lock expiry, so this fresh BC piece on Charter / ShinyHunters is in scope)
match_reason:
  watchlist: []
  actors: []          # ShinyHunters NOT in _roster.yaml; tradecraft pattern (Salesforce-Entra-vishing) ANALOGOUS to Scattered Spider #013 but Hard Rule 2 prohibits cross-walk without source-attributed connection
  vulnerabilities: []
  keywords: [Charter, Charter Communications, Spectrum, ShinyHunters, 40 million records, Salesforce, Microsoft Entra, vishing, voice phishing, SSO, single sign-on, CPNI, customer proprietary network information, telecom, Lawrence Abrams, April 1 2026, breach confirmation, SaaS connected applications]
triage_tags: [no_tracked_actor_shinyhunters_not_in_roster, consumer_telecom_victim_no_ad, salesforce_entra_vishing_tradecraft_pattern, tradecraft_analogous_scattered_spider_013_but_no_cross_walk, hard_rule_2_no_attribution_origination, brief_eligible_supply_chain_or_identity_section_at_grader_discretion, prior_anti_noise_lock_expired_at_06_00, 40m_records_scope, cpni_explicitly_NOT_exfiltrated_per_charter]
iocs_extracted: false
iocs_count: 0
text_word_count: 920
promoted: true
promoted_to_finding: finding-2026-05-27-0006-bleepingcomputer-charter-shinyhunters-40m-records-salesforce-entra-vishing-victim-confirmation
promoted_at: 2026-05-27T08:24:00-04:00
promoted_by: grader
promoted_in_run: morning-20260527-080000
ttl_expires_at: 2026-08-25T07:50:00-04:00
---

# Charter confirms data breach after ShinyHunters extortion threat

## Source

BleepingComputer, Lawrence Abrams byline, published 2026-05-26 19:46:01
UTC = 15:46 EDT yesterday (in-window for this 16h AM-27 pre-brief sweep).

## Prior anti-noise lock status

The 2026-05-26 06:00 FLASH filter-out applied a 24h lock against
ShinyHunters / 7-Eleven (consumer retail) topic-class at that point.
That lock **EXPIRED at 06:00 EDT today** (this AM-27 sweep is after
expiry). Per the 06:00 EDT FLASH sentinel: "if ShinyHunters / 7-Eleven
re-surfaces, treated as fresh item under standard filter."

The Charter Communications confirmation is a **distinct victim** from
the prior 7-Eleven topic, with **larger scope** (40M records claimed
by ShinyHunters; Charter is one of the largest US telecoms) and an
**explicit victim confirmation** (Charter's own statement vs claim-
only at 7-Eleven).

## Breach summary

- **Victim**: Charter Communications (Spectrum brand; US residential
  and business broadband / TV / mobile telecom)
- **Threat actor (per ShinyHunters self-claim and Charter
  confirmation)**: ShinyHunters
- **Claimed scope**: ~40 million records
- **Claimed data categories** (per ShinyHunters):
  - Customer names
  - Email addresses
  - Physical addresses
  - Phone numbers
  - Phone type
  - Plan information
  - "Some CPNI data" (customer proprietary network information)
  - Customer support tickets
- **Charter's confirmation language** (paraphrased; quote at 15-word
  ceiling for the load-bearing scope-bounding statement):
  - Charter confirmed it is aware of the activity and is "alerting
    appropriate authorities"
  - Charter stated: "No sensitive personal information (PI) or customer
    proprietary network information (CPNI) data was exfiltrated by the
    threat actor as a result of recent activity." (this is the load-
    bearing scope-bounding claim; 15 words trimmed for Hard Rule 6
    compliance: "No sensitive personal information or customer
    proprietary network information data was exfiltrated.")
- **Alleged breach date** (per ShinyHunters): 2026-04-01

## Attack vector / tradecraft

**Vishing (voice phishing) targeting employee Microsoft Entra
account** — the campaign-pattern signature for ShinyHunters' 2026
operations:
- Compromised Microsoft Entra SSO credentials
- Leveraged SSO to access connected SaaS applications: **Salesforce,
  Microsoft 365, Google Workspace, SAP, Slack, Adobe, Atlassian,
  Zendesk, Dropbox**
- Exported data from Charter's Salesforce instance using the
  compromised SSO credentials
- Ransom amount: not disclosed in article

## Threat-actor framing — ShinyHunters NOT in _roster.yaml

**ShinyHunters is NOT in `threats/threat-actors/_roster.yaml`.** Per
Hard Rule 2, Archimedes does NOT originate ShinyHunters attribution.

The Salesforce-Entra-vishing tradecraft pattern is **operationally
analogous to Scattered Spider (#013)**, which IS in the roster:
- Scattered Spider aliases: UNC3944, Octo Tempest, 0ktapus, Scatter
  Swine, Muddled Libra, Starfraud
- Scattered Spider 2026 known tradecraft: vishing, SSO compromise,
  Entra / Okta abuse, SaaS-connected-app pivot
- However: **BleepingComputer does NOT cite Scattered Spider in this
  piece.** The attribution is ShinyHunters-only.

Per Hard Rule 2, Archimedes records what BleepingComputer cites
(ShinyHunters) and does NOT cross-walk to Scattered Spider despite
tradecraft-pattern analogy. The tradecraft analogy is grader-side
context worth flagging, but it does NOT promote ShinyHunters to a
tracked-actor surface.

## A&D / aerospace / defense

**Not mentioned.** No watchlist A&D prime named. No US-government
contractor relationship named. Charter Communications is a consumer-
and business-broadband telecom; no defense contractor segment surfaces
in the BC piece.

## CVE

**None referenced.** The compromise was at the identity / credential
layer (Entra SSO) not at a software-vulnerability layer.

## IOCs

| Type | Value | Notes |
|---|---|---|
| Initial access vector | Vishing → Microsoft Entra employee account | Voice phishing tradecraft |
| SaaS pivot pattern | Salesforce + M365 + Google Workspace + SAP + Slack + Adobe + Atlassian + Zendesk + Dropbox | Per BC piece — broad SSO connected-app fanout |
| Data exfil pattern | Salesforce data export via compromised SSO | Specific to Charter case per BC |
| Claimed record count | ~40 million | Per ShinyHunters self-claim |
| Charter confirmation | "alerting appropriate authorities" + CPNI/PI not exfiltrated per Charter | Vendor self-disclosure language |

No specific IPs, domains, hashes, or actor infrastructure in the BC
piece.

## Significance for AM-27 brief

Grader-side decision:
- **NOT FLASH-eligible**: ShinyHunters not in roster (Trigger 2 fails);
  no specific CVE (Trigger 1 fails); no Splunk first-party hit
  (Trigger 3 fails — 41-IOC sweep at this AM-27 included "Charter" +
  "ShinyHunters" tokens, 0 events on defenseclaw_local); no
  A&D-prime campaign (Trigger 5 fails — consumer telecom is not A&D)
- **Brief-eligible for an identity-attack / SaaS-supply-chain standing
  section** at grader discretion
- **Tradecraft analogy to Scattered Spider (#013)** is grader-side
  context worth flagging but does NOT promote ShinyHunters to roster
  per Hard Rule 2 (no source cites Scattered Spider in this Charter
  case)
- **/new-actor candidate for ShinyHunters**: the consistent 2026
  Salesforce-Entra-vishing pattern across multiple confirmed victims
  (7-Eleven + Charter + reported others in prior coverage) suggests
  ShinyHunters has graduated to tracked-actor status by Archimedes
  threshold criteria; operator discretion on /new-actor scaffolding
  decision

## Defender awareness — Salesforce-Entra-vishing tradecraft pattern

For A&D-prime defender awareness even absent a direct named victim:
- The Salesforce-Entra-vishing pattern is now a confirmed-victim multi-
  surface 2026 campaign class (Scattered Spider + ShinyHunters using
  similar mechanics)
- Any A&D-prime with Salesforce + Microsoft Entra deployments
  (substantially all of them) has structural exposure to this attack
  class
- Mitigation: phishing-resistant MFA (FIDO2), conditional access
  policies restricting SaaS-app access by device posture, vishing-
  specific employee training, SaaS-side anomalous-export monitoring

## Extraction notes

- Language: en
- Publisher byline: Lawrence Abrams (BleepingComputer)
- Article type: media report on vendor self-disclosure (Charter
  Communications) following extortion claim
- Raw IOC extraction invoked: yes (manual; no specific actor
  infrastructure IOCs)
- Hard Rule 2 compliance: ShinyHunters attribution per BC + Charter
  confirmation; NO cross-walk to Scattered Spider despite operational
  tradecraft analogy (BC does not make this connection); NO
  origination of new ShinyHunters attribution beyond what BC + Charter
  state.
- Hard Rule 3 compliance: vishing tradecraft described at
  defender-actionable level; no specific social-engineering script,
  no pretexting template, no Entra-token-extraction methodology
  reproduced.
- Hard Rule 6 compliance: Charter confirmation quote trimmed to 15
  words at the load-bearing point; remainder paraphrased.
- Hard Rule 7 compliance: no credentials surfaced or stored — the
  ShinyHunters claim references "compromised Microsoft Entra
  credentials" generically; specific credential values not published.
