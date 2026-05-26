---
finding_id: finding-2026-05-26-0001-unc1549-nimbus-manticore-minifast-minijunk-v2-seo-poisoning-getsqldeveloper
created_at: 2026-05-26T08:00:00-04:00
graded_by: grader
grading_run_id: morning-20260526-080000
grading_mode: scheduled_brief
test: false

# Core grading (admiralty-grading skill output)
digraph: B2
digraph_layered:
  thn_relay_of_ckr_and_unit42_primaries: B2
  minifast_backdoor_capability_description: A2  # CKR originating primary
  miniupdate_minijunk_v2_taxonomy_overlap: A2  # Unit 42 originating primary
  appdomain_hijacking_zip_archived_dlls_ttp: A2
  seo_poisoning_getsqldeveloper_com_fake_sql_developer_page: A2
  trojanized_zoom_installer_career_lure: A2
  bing_duckduckgo_search_engine_targeting: B2
  aviation_software_defense_telecom_oil_gas_sectoral_targeting: A2
  geographic_us_eu_me_saudi_australia_israel_uae_targeting: A2
  ai_assisted_malware_development_indicators: B3  # CKR analytical inference; single primary
  iran_irgc_attribution_corpus_baseline_restated: A1
  no_ad_prime_named_compromised: A1
  splunk_first_party_zero_hits_on_minifast_minijunk_getsqldeveloper_appdomain: A1
  cluster_anchor: B2

digraph_anchor: >
  Cluster digraph B2 anchored on The Hacker News (Ravie Lakshmanan-era
  editorial relay, 2026-05-26 03:13 EDT in-window) restatement of two
  independent A-grade vendor research primaries published 2026-05-22:
  Check Point Research "Fast and Furious — Nimbus Manticore Operations
  During the Iranian Conflict" and Palo Alto Networks Unit 42's
  concurrent MiniUpdate/MiniJunk V2/AppDomainManager tradecraft
  documentation. THN is graded B (media relay); the cluster carries a
  B2 anchor because THN itself is single-relay layer over two genuinely
  independent A-grade vendor primaries (CKR + Unit 42, different
  research orgs, different telemetry, concurrent publication of
  overlapping but taxonomically distinct cluster mappings). The
  primaries themselves would support A2 at the originating layer
  (single-source veto on each vendor's analysis pre-corroboration),
  but the CKR+Unit42 independent-research-pair corroboration on the
  joint UNC1549/Nimbus Manticore/Screening Serpens campaign elevates
  the credibility to 2 (Probably True) across vendor consensus.
  Single-source veto applies at the THN-relay layer (one relay, two
  primaries cited but not directly retrieved this sweep) — WEP ceiling
  capped at "likely" not "very likely". This is a tradecraft-evolution
  UPDATE on the corpus-tracked UNC1549 surface (#004), not a new
  attribution claim. Iran/IRGC attribution is corpus-baseline.

source_reliability:
  grade: B
  source_name: "The Hacker News (editorial relay)"
  source_yaml_id: thehackernews
  grade_rationale: >
    Pre-assigned B per source-grades.yaml (provisional B, multi-cross-
    corroboration cycle established). THN is a multi-relay vendor
    research aggregator; in this article relays Check Point Research
    + Palo Alto Networks Unit 42 concurrent 2026-05-22 publications on
    UNC1549/Nimbus Manticore. THN does not introduce novel analysis;
    relay-layer source.
  provisional: true
  underlying_primaries:
    - vendor_name: "Check Point Research"
      vendor_grade: provisional_A_pending_source_grade_log_entry
      publication: "Fast and Furious – Nimbus Manticore Operations During the Iranian Conflict"
      publication_date: 2026-05-22
    - vendor_name: "Palo Alto Networks Unit 42"
      vendor_yaml_id: unit42
      vendor_grade: A
      publication: "MiniUpdate / MiniJunk V2 / AppDomainManager tradecraft (concurrent publication)"
      publication_date: 2026-05-22

credibility:
  grade: 2
  checklist_passed:
    - probably_true_consistent_with_established_ttps_or_known_campaign_timing_targeting
    - probably_true_no_contradicting_evidence_from_ab_grade_sources
    - probably_true_technical_claims_internally_coherent
  rationale: >
    Consistent with established UNC1549 / Nimbus Manticore / Screening
    Serpens TTPs in corpus baseline — IRGC-linked Iran-nexus actor
    targeting aviation, defense, telecommunications, oil & gas across
    US/EU/Middle East. AppDomain hijacking, SEO poisoning, and
    career-themed phishing lures with trojanized Zoom installers are
    tradecraft-evolution updates that fit within the actor's known
    operating envelope (DLL sideloading variant family + initial-
    access social engineering). No contradicting evidence from A/B-
    grade sources. Technical claims internally coherent: AppDomain
    hijacking is a documented .NET DLL-loading abuse class
    (T1574.x family); SEO poisoning via fake software-download
    landing pages is a documented initial-access TTP class
    (T1583.008 / T1608); domain getsqldeveloper[.]com is a plausible
    typosquat target on Oracle's SQL Developer brand. Campaign timing
    (following the joint US-Israeli campaign against Iran in late
    February 2026, per CKR framing) is consistent with established
    Iran-nexus operational tempo post-geopolitical escalations.

corroboration:
  independent_sources:
    - thehackernews     # relay layer
    - checkpoint-research # primary 1 (provisional A, cited via relay)
    - unit42              # primary 2 (A, cited via relay)
  independent: true
  test_passed: >
    CKR and Unit 42 are genuinely independent vendor research
    organizations (different parent companies, different telemetry,
    different cluster-naming taxonomies — CKR uses "Nimbus Manticore",
    Unit 42 uses Screening Serpens / Smoke Sandstorm). Concurrent
    publication 2026-05-22 on the same campaign suggests coordinated
    or parallel investigative threads on overlapping victim sets. THN
    relay does NOT independently corroborate — it aggregates the two
    primaries. The cluster has two effective primary sources at the
    originating layer.
  caveat: >
    Originating primaries were not directly retrieved this sweep
    (CKR + Unit 42 2026-05-22 publications corpus-tracked since the
    2026-05-23 0600 FLASH lineage but the THN restatement is the
    in-window retrieval). Primary research direct-fetch on a later
    sweep would tighten the corroboration test.

first_party_precedence:
  applied: false
  splunk_evidence: null
  splunk_query_executed: >
    14h pre-brief sentinel sweep query included MiniFast, MiniJunk,
    Nimbus Manticore, Screening Serpens, UNC1549, getsqldeveloper,
    AppDomainManager, MiniUpdate keywords across defenseclaw_local
    and archimedes indices. Zero events returned. 61st consecutive
    dormant non-self sweep on defenseclaw_local. Per Hard Rule 8,
    silence is not disconfirming.

single_source_veto_applied: true
single_source_veto_rationale: >
  Single-source veto applies at the THN-relay layer (this sweep
  retrieved one relay covering both primaries; primaries not directly
  retrieved this sweep). WEP ceiling capped at "likely". If CKR and
  Unit 42 primaries are directly retrieved in a subsequent sweep and
  the independent-corroboration test holds at the primary layer,
  the cluster could elevate to "very likely" on the joint
  tradecraft-evolution claim.

wep_ceiling: likely
wep_layered:
  unc1549_iran_irgc_attribution_corpus_baseline: not_a_new_claim  # already-established
  minifast_minijunk_v2_active_2026_campaign: likely
  appdomain_hijacking_zip_archived_dll_ttp: likely
  getsqldeveloper_com_seo_poisoning_domain_ioc: likely
  aviation_software_defense_telecom_oil_gas_sectoral_targeting: likely
  ai_assisted_malware_development_indicators: roughly_even_chance  # CKR analytical inference, single primary

inclusion:
  eligible_for:
    - daily_brief_action
    - daily_brief_monitoring
    - weekly_synthesis
    - actor_profile_update
  not_eligible_for:
    - flash               # FLASH-POLICY anti-noise: tradecraft-evolution UPDATE on existing corpus surface; lock active per raw-signal sentinel
  inclusion_rationale: >
    B2 cluster anchor → eligible for daily brief action item per
    INTEL-GRADING.md thresholds. UNC1549 is corpus-tracked actor #004
    with last-reviewed 2026-05-09; this tradecraft-evolution update
    is actor-profile-update eligible. NOT FLASH-eligible per
    FLASH-POLICY anti-noise rule (this is restatement-with-update
    on a corpus surface that has been actively tracked since
    2026-05-23 0600 FLASH lineage; no novel attribution; tradecraft
    extensions warrant brief inclusion not async escalation).

# Cluster metadata
cluster:
  topic: "UNC1549 / Nimbus Manticore / Screening Serpens 2026 campaign tradecraft evolution — MiniFast/MiniUpdate + MiniJunk V2 backdoors + SEO poisoning via getsqldeveloper[.]com + AppDomain hijacking + trojanized Zoom installers + aviation/software/defense/telecom/oil&gas sectoral targeting across US/EU/ME/Saudi/Australia/Israel/UAE"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-05-26-am-001-thn-unc1549-nimbus-manticore-minifast-minijunk-v2-seo-poisoning-getsqldeveloper-restatement
  related_actors: ["004"]
  related_vulnerabilities: []
  related_campaigns:
    - unc1549-nimbus-manticore-2026-active-campaign
  attribution_claims:
    - claimed_actor: "UNC1549 / Nimbus Manticore / Screening Serpens / Smoke Sandstorm / Crimson Sandstorm / Imperial Kitten / Tortoiseshell"
      claimed_actor_roster_id: "004"
      claimed_by_sources: [thehackernews, checkpoint-research, unit42]
      attribution_specificity: >
        Iran-nexus, IRGC-affiliated. Aliases enumerated:
        Nimbus Manticore (CKR), Screening Serpens / Smoke Sandstorm /
        Crimson Sandstorm (Unit 42), UNC1549 (Mandiant originating
        cluster naming), Imperial Kitten, Tortoiseshell. Corpus-
        baseline per _roster.yaml actor #004.
      hard_rule_2_treatment: >
        Corpus-baseline attribution preserved. Cross-cluster alias
        merge is _roster.yaml-baseline. THN's relay restates the
        established attribution — does NOT originate new attribution.
        Archimedes does not promote beyond what CKR + Unit 42
        primaries state.
      requires_analyst_review: false

# IOCs surfaced
iocs_surfaced:
  - type: domain
    value: getsqldeveloper[.]com
    context: "Fake Oracle SQL Developer download landing page; SEO-poisoning delivery vector for MiniFast/MiniUpdate backdoor via Bing and DuckDuckGo search-engine ranking manipulation"
    confidence: medium  # relay-layer; CKR is originating primary
    source_attribution: "Check Point Research (relayed via The Hacker News 2026-05-26)"
    actor_id: "004"
    related_campaign: unc1549-nimbus-manticore-2026
    defanged: true
  # Additional supporting domains noted as "dozens" by CKR but not enumerated in THN relay; direct CKR fetch on subsequent sweep would surface specifics

ttp_keywords:
  - name: AppDomain hijacking
    framework_mapping: MITRE T1574 / Hijack Execution Flow
    context: "Malicious DLLs launched from benign executables in ZIP archives — Nimbus Manticore campaign chain"
  - name: SEO poisoning via fake software-download landing pages
    framework_mapping: MITRE T1583.008 / Acquire Infrastructure — Malvertising/SEO
    context: "Fake SQL Developer download pages ranked on Bing and DuckDuckGo"
  - name: Trojanized Zoom installer
    framework_mapping: MITRE T1204.002 / User Execution — Malicious File
    context: "Career-themed phishing lures impersonating aviation/software organizations with fake meeting invitations"

# Downstream handoff flags
analyst_review_required: false      # B2 corpus-baseline restatement; no novel attribution; tradecraft-evolution UPDATE
red_team_review_required: false     # WEP ceiling "likely" not "very likely"
red_team_review: null
analysis_sections:
  sat_ach: null
  sat_kac: null

# Lifecycle
tlp: CLEAR
published_in_briefs: []
retracted: false
retraction_brief_id: null
---

# UNC1549 / Nimbus Manticore Deploy MiniFast and MiniJunk V2 via SEO Poisoning of getsqldeveloper[.]com and Trojanized Zoom Installers Against Aviation, Defense, Telecom Targets

## Summary

The Hacker News (2026-05-26 03:13 EDT) restates concurrent 2026-05-22 publications from Check Point Research and Palo Alto Networks Unit 42 documenting a fresh UNC1549 (a.k.a. Nimbus Manticore, Screening Serpens, Smoke Sandstorm, Imperial Kitten, Tortoiseshell) campaign attributed to Iran's IRGC. The campaign targets aviation, software, defense, telecommunications, and oil-and-gas sectors across the U.S., Europe, Middle East, Saudi Arabia, Australia, Israel, and UAE following the joint U.S.-Israeli military campaign against Iran in late February 2026. CKR documents a new backdoor named **MiniFast** (Unit 42 calls the same/adjacent family **MiniUpdate**) alongside an updated **MiniJunk V2** variant, deployed via career-themed phishing with trojanized Zoom installers and via SEO-poisoning fake software-download pages — including a fake Oracle SQL Developer page hosted at `getsqldeveloper[.]com` ranking on Bing and DuckDuckGo. AppDomain hijacking from ZIP-archived DLLs launches the payload from benign-looking executables. CKR additionally flags AI-assisted malware development indicators in MiniFast's code structure. No A&D prime is named as compromised. Iran/IRGC attribution is corpus-baseline (actor #004) and is restated, not originated. This is a tradecraft-evolution update on a corpus surface continuously tracked since the 2026-05-23 0600 FLASH lineage.

## Sources

### The Hacker News (thehackernews, digraph: B)

- URL: https://thehackernews.com/2026/05/iranian-hackers-deploy-minifast-and.html
- Published: 2026-05-26 03:13 EDT
- Byline: The Hacker News editorial (info@thehackernews.com)
- Key claim: Relay of CKR + Unit 42 documenting active UNC1549 campaign using MiniFast/MiniUpdate, MiniJunk V2, AppDomain hijacking, SEO poisoning via getsqldeveloper[.]com, and trojanized Zoom installers against aviation, defense, telecom, oil & gas across U.S., Europe, Middle East. Iran/IRGC attribution restated.

### Check Point Research (checkpoint-research, digraph: provisional A — originating primary cited via THN relay)

- Publication: "Fast and Furious – Nimbus Manticore Operations During the Iranian Conflict"
- Publication date: 2026-05-22
- Key claim (relayed): MiniFast backdoor capabilities (file operations, directory listings, process enumeration, cmd.exe execution, DLL loading, ZIP archive creation, scheduled-task persistence, runas privilege escalation, jittered beacon intervals); AI-assisted development indicators (excessive error handling, repetitive function naming, modular code organization); aviation/software/defense sectoral targeting.

### Palo Alto Networks Unit 42 (unit42, digraph: A — concurrent originating primary cited via THN relay)

- Publication: MiniUpdate / MiniJunk V2 / AppDomainManager tradecraft documentation
- Publication date: 2026-05-22 (concurrent with CKR)
- Key claim (relayed): Naming overlap question — CKR's MiniFast and Unit 42's MiniUpdate appear to describe the same or adjacent family. Documents AppDomainManager hijacking technique and targeting documentation.

## Technical detail

### MiniFast / MiniUpdate backdoor (per CKR analysis relayed by THN)

Capability set: file operations, directory listings, process enumeration, command execution via `cmd.exe`, DLL loading, ZIP archive creation, persistence via scheduled tasks, privilege escalation using `runas`, and configurable beacon intervals with jitter randomization.

CKR notes "excessive error handling," "repetitive function naming," and "modular code organization" suggesting AI-assisted malware development — analytical inference at single-vendor confidence.

### MiniJunk V2

Updated version of a previously deployed UNC1549 variant. Specific differential capability detail not enumerated in the THN relay.

### Delivery vectors

1. **Phishing with career-themed lures** — fake meeting invitations and trojanized Zoom installers impersonating aviation/software organizations.
2. **SEO poisoning** — fake Oracle SQL Developer download pages ranked on Bing and DuckDuckGo at `getsqldeveloper[.]com`; CKR additionally cites "dozens of supporting domains registered for SEO reputation manipulation" (specific list not enumerated in THN relay).
3. **AppDomain hijacking** — malicious DLLs launched from benign executables in ZIP archives (MITRE T1574 family).

### Targeting profile

- **Sectors:** aviation, software, defense, telecommunications, oil and gas.
- **Geographic scope:** U.S., Europe, Middle East, Saudi Arabia, Australia, Israel, UAE.
- **Victimology granularity:** Named individual employees in Saudi Arabia and Australia (software and aviation sectors); no specific organizational victim named in THN relay.

## IOCs surfaced

```yaml
iocs:
  - type: domain
    value: getsqldeveloper[.]com
    context: "Fake Oracle SQL Developer download landing page; SEO-poisoning delivery vector for MiniFast/MiniUpdate backdoor"
    confidence: medium
    source_attribution: "Check Point Research (via THN relay)"
    first_observed: pre-2026-05-22
    related_campaign: unc1549-nimbus-manticore-2026
    actor_id: "004"
    defanged: true
```

Additional "dozens" of SEO-supporting domains referenced by CKR are not enumerated in the THN relay; direct CKR primary fetch in a subsequent sweep would surface the full set for `_master-index.yaml` consideration.

## Relationship to existing findings

This is a tradecraft-evolution update on the UNC1549 surface continuously tracked across the corpus. Cross-reference: the 2026-05-23 0600 FLASH lineage captured the originating CKR + Unit 42 2026-05-22 publications; this THN restatement at 2026-05-26 surfaces the consolidated narrative in a B-grade media relay. UNC1549 dossier last-reviewed 2026-05-09 (threat level MEDIUM weighted 5.4; Espionage category HIGH composite 10 per `/update-tracking 2026-05-09` per _roster.yaml).

## Open questions for analyst

- Naming taxonomy reconciliation: does CKR's MiniFast == Unit 42's MiniUpdate (same family) or are these adjacent but distinct families? Resolution requires direct retrieval of both primary publications.
- AI-assisted development inference: CKR's analytical claim ("excessive error handling, repetitive function naming, modular code organization") is a single-vendor confidence layer; if corroborated by Unit 42 or other A-grade vendor research, escalate to actor-dossier TTP. Cross-reference the broader CKR AI Threat Landscape Digest (finding-2026-05-26-0002) which frames the AI-assisted-development pattern at the offensive-operations landscape level.
- Update the UNC1549 actor dossier TTP catalog with: AppDomain hijacking from ZIP-archived DLLs; SEO-poisoning via fake software-download pages; trojanized Zoom installer initial-access vector; jittered-beacon configuration in MiniFast/MiniUpdate.
- No A&D prime is named compromised. The aviation/defense sectoral framing is targeting-class; specific watchlist primes (Lockheed Martin, Boeing, RTX, Northrop, GD, BAE, L3Harris, Leidos, SAIC, Thales, GE Aerospace, Safran, Honeywell Aerospace, Airbus, Elbit) are not enumerated as victims in the THN relay or in the primaries as relayed.
