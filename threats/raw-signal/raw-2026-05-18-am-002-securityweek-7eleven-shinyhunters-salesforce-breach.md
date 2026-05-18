---
raw_id: raw-2026-05-18-am-002
collected_at: 2026-05-18T07:36:00-04:00
run_id: pre-brief-20260518-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: securityweek
  source_name: "SecurityWeek (Eduard Kovacs)"
  source_url: https://www.securityweek.com/7-eleven-data-breach-confirmed-after-shinyhunters-ransom-demand/
  published_at: 2026-05-18T07:25:54-04:00
match_reason:
  watchlist: []
  actors:
    - shinyhunters_cluster_NOT_in_roster
    - scattered_spider_potentially_per_securityweek_relay_chain_HARD_RULE_2_DO_NOT_PROPAGATE
  vulnerabilities: []
  keywords:
    - 7_eleven
    - shinyhunters
    - salesforce_records
    - data_breach
    - franchisee_documents
    - ransom_demand
    - leak_site_listing
    - mid_2025_salesforce_targeting_campaign
    - coinbase_cartel_cluster_adjacent
    - grafana_same_morning_named_victim_cluster
triage_tags:
  - status_update_candidate
  - named_enterprise_victim_self_disclosure
  - shinyhunters_cluster_second_named_victim_same_morning
  - shinyhunters_NOT_in_roster
  - scattered_spider_roster_013_HIGH_relay_chain_NOT_propagated_HARD_RULE_2
  - no_a_grade_vendor_attestation
  - no_a_and_d_entity
  - mid_2025_salesforce_campaign_extension
  - five_historical_victims_named
  - non_flash
  - source_securityweek_provisional_b
iocs_extracted: true
iocs_count: 0
text_word_count: 1100
promoted: true
promoted_to_finding: finding-2026-05-18-0002
promoted_at: 2026-05-18T08:14:00-04:00
promoted_in_grading_run: morning-20260518-080000
ttl_expires_at: 2026-08-16T07:36:00-04:00
---

# SecurityWeek — 7-Eleven Data Breach Confirmed After ShinyHunters Ransom Demand

**Source URL:** https://www.securityweek.com/7-eleven-data-breach-confirmed-after-shinyhunters-ransom-demand/
**Author:** Eduard Kovacs
**Published:** 2026-05-18T11:25:54 UTC (07:25 EDT) — ~5 minutes before this pre-brief collection window-close
**Source grade per source-grades.yaml:** securityweek = B (provisional)
**Collection mode:** pre-brief, scheduled 07:30 EDT Monday sweep
**Relation to carry-forwards:** New named-enterprise-victim disclosure on ShinyHunters Salesforce-customer campaign; ShinyHunters cluster is cited by same SecurityWeek outlet earlier this morning (Grafana / Coinbase Cartel article 04:34 EDT, 06:00 FLASH a8121bc Item 3) as one of three threat-actor names in an unnamed-cybersecurity-companies multi-step attribution chain "Coinbase Cartel linked to ShinyHunters, Scattered Spider, and Lapsus$." 7-Eleven is therefore the SECOND named-enterprise-victim disclosure same morning attributed to the ShinyHunters cluster activity per SecurityWeek framing.

---

## Article summary (per WebFetch direct retrieval)

### Named victim self-disclosure

- **Victim:** 7-Eleven (US convenience-store franchise chain; subsidiary of Seven & i Holdings, Japan)
- **Intrusion detection date:** 2026-04-08 (5 weeks ago at time of confirmation)
- **Compromised systems:** systems storing **franchisee documents** at 7-Eleven (franchise application records)
- **Self-disclosed scope:** "unspecified personal information has been compromised" through franchise applications
- **Regulator notification:** reported only **two Maine residents impacted** per state-regulator filing
- **NOT named as A&D / aerospace / defense / ITAR-regulated company.** 7-Eleven is a convenience-store retailer. Off-watchlist per `infrastructure/watchlists/aerospace-defense.yaml`.

### Attacker claims (ShinyHunters)

- **Threat-actor named:** ShinyHunters
- **Leak site listing:** 2026-04-17 (9 days after 7-Eleven's intrusion detection)
- **Claimed stolen records:** >600,000 Salesforce records (personal information + corporate data)
- **Ransom demand timing:** by 2026-04-21
- **Subsequent sale offer:** $250,000 (after ransom deadline expired)
- **Note:** 7-Eleven's self-disclosed "two Maine residents impacted" framing and ShinyHunters' "600,000 Salesforce records" claim are NOT reconcilable as identical scope; SecurityWeek does not editorially reconcile the discrepancy. The conservative reading: 7-Eleven's regulator filing is narrowly scoped to Maine-residents-with-PII (Maine has aggressive data-breach-disclosure statutes); ShinyHunters' claim covers the full corporate Salesforce dataset including non-PII corporate records.

### Broader campaign context per SecurityWeek

- SecurityWeek frames as part of the ongoing **ShinyHunters Salesforce-customer targeting campaign since mid-2025**
- Mechanism per SecurityWeek: "exploiting **phishing, abuse of third-party integrations, or misconfigurations** rather than Salesforce vulnerabilities" — i.e., the Salesforce platform itself is not the vulnerability; victim-side misconfigurations and phishing-derived credential theft are the access vector
- Historically named victims in the same campaign per SecurityWeek: **Instructure, Vimeo, Wynn Resorts, Vercel, Medtronic**
  - **None on `infrastructure/watchlists/aerospace-defense.yaml`.**
  - Medtronic = medical device manufacturer (DoD healthcare procurement adjacency but not an A&D prime)
  - Vercel = SaaS frontend hosting platform (developer-tools surface)
  - Wynn Resorts = hospitality
  - Vimeo = video platform (consumer + enterprise SaaS)
  - Instructure = education LMS (Canvas; previously surfaced 2026-05-08 PM as separate breach event covered by BleepingComputer)

### Attribution language preservation (Hard Rule 2)

SecurityWeek's exact attribution language preserved verbatim:

> "ShinyHunters has been targeting the Salesforce instances of major organizations since mid-2025."

This morning's earlier Grafana article from same outlet (06:00 FLASH a8121bc Item 3) relayed an unnamed-cybersecurity-companies multi-step attribution chain framing Coinbase Cartel as "linked to ShinyHunters, Scattered Spider, and Lapsus$." That earlier framing is NOT re-cited in the 7-Eleven article — Eduard Kovacs's 7-Eleven coverage keeps ShinyHunters as a standalone cluster, not chained to Coinbase Cartel / Scattered Spider / Lapsus$ here.

**Hard Rule 2 / LEGAL-POLICY no-attribution-laundering compliance:** Archimedes does NOT propagate the Grafana-article multi-step relay attribution chain to the 7-Eleven case. The 7-Eleven attribution stands at "ShinyHunters per SecurityWeek per ShinyHunters leak-site self-claim." ShinyHunters is NOT in `_roster.yaml`. Scattered Spider (#013 HIGH) IS in roster but has NO direct attribution to 7-Eleven from any source cited by SecurityWeek today.

### No A-grade vendor corroboration

- **No Mandiant, CrowdStrike, Unit 42, MSTIC, Volexity, Talos, or Symantec citation** in the SecurityWeek 7-Eleven article
- **No IOCs published** (no IPs, no domains, no hashes, no malware family)
- **No CVE** (the campaign mechanism per SecurityWeek is phishing / third-party integration abuse / misconfiguration, not a CVE-vulnerability)
- **No A&D entity named** as victim or downstream target

---

## What's NEW vs. prior corpus coverage

The Grafana article from earlier this same morning (06:00 FLASH a8121bc Item 3, raw-2026-05-18-flash-0600-000 inline evaluation) was the FIRST same-morning surface naming ShinyHunters as part of a cluster activity pattern. The 7-Eleven article is the SECOND surface this morning, making it a 2-victim same-morning-news-cycle disclosure pattern from the same SecurityWeek outlet on the same actor cluster.

Material differences between the two surfaces:

| Detail | Grafana (Eduard Kovacs 04:34 EDT) | 7-Eleven (Eduard Kovacs 07:25 EDT) — THIS SURFACE |
|---|---|---|
| Named actor | Coinbase Cartel, linked to ShinyHunters + Scattered Spider + Lapsus$ per unnamed cybersecurity companies | ShinyHunters standalone per ShinyHunters leak-site self-claim |
| Mechanism | Codebase theft from Grafana (no customer data per Grafana statement) | Salesforce-records theft (600,000 records claimed by attacker) |
| Attribution chain | Multi-step relay through unnamed third-parties | Direct attacker self-claim on leak site |
| Hard Rule 2 risk | High (multi-step relay through unnamed third-parties = attribution laundering risk) | Low (single-step attacker self-claim on leak site, factual record) |
| Same-morning author | Eduard Kovacs | Eduard Kovacs |
| A-grade vendor attribution | NONE (unnamed "cybersecurity companies" only) | NONE |

The 7-Eleven surface is the cleaner Hard Rule 2 surface — direct ShinyHunters self-claim on leak site, scoped to the Salesforce-records mechanism, no laundered roster-actor attribution chain.

---

## FLASH-trigger evaluation (per FLASH-POLICY.md)

- **Trigger 1 (Critical CVE actively exploited, CVSS ≥ 9.0, A-grade attestation):** FAIL. No CVE involved (campaign mechanism is phishing / third-party integration abuse / misconfiguration, not CVE-vulnerability).
- **Trigger 2 (New tracked actor attribution to actor in `_roster.yaml`):** FAIL. ShinyHunters NOT in `_roster.yaml`. Scattered Spider (#013 HIGH) IS in roster but has NO direct attribution to 7-Eleven from any source — only the Grafana-article-companion relay chain, which Hard Rule 2 prevents Archimedes from propagating as an originated attribution.
- **Trigger 3 (First-party Splunk IOC hit):** FAIL. 42nd consecutive dormant non-self-telemetry Splunk sweep. No IOCs from source to query against in any case.
- **Trigger 4 (Tracked actor TTP change, A/B-grade source, attributable):** FAIL. No tracked actor; TTP not attributable.
- **Trigger 5 (Active A&D-sector campaign, multi-victim):** FAIL on A&D-sector leg. Although the campaign IS multi-victim (7 named victims including today's 7-Eleven addition), NONE of the named victims is an A&D prime or watchlist entity. The campaign is convenience-store + hospitality + SaaS + LMS + medical-device + video-platform — broadly enterprise but not A&D-targeted.
- **Trigger 6 (Zero-day no-patch):** FAIL. No CVE, no patch dimension.

**Disposition: NOT a FLASH-trigger fire.** Status-update CANDIDATE for 08:00 morning brief grader.

---

## Grader decision space (for 08:00 morning brief evaluation)

The grader should evaluate whether to:

1. **Promote 7-Eleven + Grafana as a single cluster finding** on ShinyHunters Salesforce-targeting campaign activity, with Hard Rule 2 hedging on the roster-actor attribution chain. The cluster would carry the procedural-facts layer at B/likely (both victim self-disclosures are A-procedural on own incident, but the actor attribution rests at B-relay-only) and the cluster-mapping layer at the C/possibly-true level (no A-grade vendor research on ShinyHunters cluster as a discrete trackable entity). Anti-noise rule on roster-actor attribution: do NOT collapse to Scattered Spider tracked-actor attribution.
2. **Promote as two discrete findings** (one Grafana, one 7-Eleven) with cross-reference, treating each as standalone named-victim disclosure. Less efficient but cleaner Hard Rule 2 posture.
3. **Hold as status-update candidates** without promotion pending A-grade vendor research (Mandiant / CrowdStrike / Unit 42 / MSTIC) on the ShinyHunters cluster. ShinyHunters has been visible in B-grade media reporting for years as a Salesforce-targeting commodity criminal actor; the absence of A-grade vendor research is methodologically notable. Conservative case under INTEL-GRADING.md: do not promote, hold as carry-forward.
4. **Discard as commodity criminal cluster activity outside A&D scope.** Defensible position given (a) no A&D entity in 7-victim list, (b) no A-grade vendor research, (c) actor cluster not on `_roster.yaml`. Counter-case: the ShinyHunters cluster is methodologically interesting as a recurring SaaS-customer-targeting pattern and may eventually reach A&D primes via the Salesforce ecosystem (most large A&D primes run Salesforce CRM for sales / FAR / DFARS compliance management). Forward-inference for `_roster.yaml` addition is grader's call, not collector's.

Hard Rule 2 reminder for the grader: under no circumstances propagate the SecurityWeek "Coinbase Cartel linked to ShinyHunters / Scattered Spider / Lapsus$" multi-step relay chain (per unnamed cybersecurity companies) as an Archimedes-originated Scattered-Spider attribution to either Grafana or 7-Eleven. LEGAL-POLICY no-attribution-laundering rule is dispositive on this.

Hard Rule 7 reminder: when quoting SecurityWeek in the morning brief, ≤15 words per source, one quote per source. The verbatim attribution language above ("ShinyHunters has been targeting the Salesforce instances of major organizations since mid-2025" = 13 words) is the strongest quote candidate; the regulator-filing scope ("two Maine residents impacted") is a strong second.

---

## Extraction notes

- Language: en
- Publisher byline: Eduard Kovacs (SecurityWeek)
- Article type: data-breach disclosure relay with attacker self-claim incorporation
- Raw IOC extraction invoked: yes (zero IOCs in source; only victim/actor/campaign-scope metadata)
- Source-grade reference: securityweek = B (provisional, awaiting ratification)

## IOCs (from ioc-extraction skill)

```yaml
cves: []
domains: []
ips: []
hashes: []
session_ids: []
named_victims_in_window:
  - name: "7-Eleven"
    sector: convenience_store_retail
    parent: "Seven & i Holdings (JP)"
    ad_watchlist: false
    disclosure_date: 2026-04-08
    confirmation_date: 2026-05-18
    scope_self_disclosed: "unspecified personal information through franchise applications; 2 Maine residents impacted per state regulator filing"
    scope_attacker_claimed: ">600,000 Salesforce records (PI + corporate data)"
    ransom_demand_date: 2026-04-21
    sale_offer_amount_usd: 250000
named_victims_referenced_as_prior_in_campaign:
  - name: Instructure
    sector: education_lms_canvas
    ad_watchlist: false
  - name: Vimeo
    sector: video_platform_saas
    ad_watchlist: false
  - name: Wynn Resorts
    sector: hospitality
    ad_watchlist: false
  - name: Vercel
    sector: saas_frontend_hosting_dev_tools
    ad_watchlist: false
  - name: Medtronic
    sector: medical_devices
    ad_watchlist: false
    note: "DoD healthcare procurement adjacency but not A&D prime"
attribution_claims:
  primary_attribution: "ShinyHunters (per their own leak-site self-claim 2026-04-17 + SecurityWeek attribution to ShinyHunters)"
  source_attribution_language_verbatim: "ShinyHunters has been targeting the Salesforce instances of major organizations since mid-2025"
  cluster_chain_relay_in_companion_article_grafana_only_NOT_propagated_HARD_RULE_2: "Coinbase Cartel linked to ShinyHunters, Scattered Spider, and Lapsus$ per unnamed cybersecurity companies — Archimedes does NOT propagate this chain to 7-Eleven attribution"
  shinyhunters_in_roster: false
  scattered_spider_in_roster_but_NOT_directly_attributed_to_7_eleven_by_any_source: true
  archimedes_originated_attribution: NEVER (Hard Rule 2)
mechanism:
  primary_vector: "phishing, abuse of third-party integrations, or misconfigurations (per SecurityWeek framing)"
  not_a_salesforce_platform_vulnerability: "Salesforce platform itself is not the vulnerability per SecurityWeek; victim-side misconfigurations and credential theft are the access vector"
  cve_involved: false
```
