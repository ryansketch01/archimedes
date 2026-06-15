---
id: finding-2026-06-15-0003
finding_id: finding-2026-06-15-0003-thn-sa-sansec-awesome-motive-wordpress-cdn-supply-chain-polyfill-pattern-net-new-ioc-yandex-cloud-ip-consumer-plugin-not-ad
title: "Awesome Motive WordPress CDN supply-chain compromise (Sansec primary disclosure 2026-06-13; SA + THN multi-publisher independent relays 2026-06-15) — OptinMonster, TrustPulse, PushEngage consumer marketing plugins served compromised JS via clientcdn.pushengage.com (PushEngage hot ~36h until 2026-06-14, OptinMonster + TrustPulse hot ~25 min on 2026-06-12 22:17-22:42 UTC); C2 typosquat tidio.cc (registered 2026-04-28, ~45d warm-up); NET-NEW IOC `84.201.6.54` attacker server IP (Yandex Cloud ASN per public DNS, NOT Archimedes-resolved this sweep, NOT state-actor attribution); hidden backdoor plugins 'content-delivery-helper' v2.7.1 + 'database-optimizer' v2.9.4 with 'WPM File Manager & Shell' web-shell; admin account patterns 'developer_api1' + 'dev_xxxxxx' randomized; ~1.2M sites collective reach; Sansec method-pattern framing: 'Polyfill-pattern attackers' (NOT actor-cluster name); PushEngage UpdraftPlus initial-entry theory DISPUTED by Sansec (breached system still unknown); NO A&D-prime production deployment context (consumer marketing / lead-generation / push-notification plugins NOT used in A&D-prime production stack); NO US A&D / DIB victim named; NO CVE assigned; NO tracked-roster actor attribution; NO nation-state attribution"
date: 2026-06-15
created_at: 2026-06-15T08:20:00-04:00
graded_by: grader
grading_run_id: morning-20260615-080000
grading_mode: scheduled_brief
test: false
status: graded

# ============================================================================
# Core grading
# ============================================================================
digraph: B2
digraph_layered:
  sansec_primary_disclosure_2026_06_13_of_awesome_motive_cdn_supply_chain_compromise: A1  # Sansec is A-grade research firm with Polyfill 2024 incident attribution lineage; multi-publisher independent corroboration achieved (SA + THN both relay independently from Sansec primary)
  pushengage_clientcdn_compromised_serving_malicious_script_2026_06_12_22_17_until_2026_06_14: B2  # Sansec primary + 2 independent publisher relays; technical timeline corroborated
  optinmonster_and_trustpulse_hot_25_min_window_22_17_22_42_utc_2026_06_12: B2  # Sansec primary + 2 publisher relays
  c2_typosquat_tidio_cc_registered_2026_04_28_first_active_2026_06_12_22_17_utc: B2  # Sansec primary + 2 publisher relays; domain registration verifiable via public WHOIS (not retrieved this sweep)
  net_new_ioc_84_201_6_54_attacker_server_yandex_cloud_asn: B2  # THN net-new vs SA; Yandex Cloud ASN attribution is method-pattern not state-actor binding
  hidden_backdoor_plugins_content_delivery_helper_v2_7_1_and_database_optimizer_v2_9_4: B2  # Sansec + 2 publisher relays
  wpm_file_manager_shell_webshell_brand_disclosed_by_thn: B2  # THN net-new vs SA
  admin_account_patterns_developer_api1_fixed_and_dev_xxxxxx_randomized: B2  # Sansec + 2 publisher relays
  approximately_1_2m_sites_collective_reach: B2  # THN-refined number vs SA's 'thousands'; reach claim is publisher-level not Archimedes-verified
  pushengage_updraft_plus_initial_entry_theory_DISPUTED_by_sansec: B2  # Sansec actively disputes the PushEngage attribution claim; verifiable disputation
  sansec_polyfill_pattern_attackers_framing_method_pattern_not_actor_cluster_name: A1  # Verifiable framing — Sansec compares to its own 2024 Polyfill discovery as method-pattern, NOT actor-cluster identity carryover
  no_tracked_actor_attribution_no_actor_cluster_name_no_nation_state_attribution: A1  # Verifiable absence — Hard Rule 2 binding preserved
  no_ad_prime_production_deployment_context_consumer_marketing_plugins: A1  # Verifiable structural absence — OptinMonster / TrustPulse / PushEngage are consumer marketing / lead-gen / push-notification plugins, NOT used in A&D-prime production stack
  no_us_ad_dib_victim_named_no_cve_assigned: A1  # Verifiable absence
  cluster_anchor: B2

digraph_anchor: >
  Cluster anchored at B2 (Probably True / monitoring-tier).
  Multi-publisher independence achieved with three independent
  surfaces:
    - Sansec (research-firm primary, 2026-06-13 disclosure)
    - Security Affairs (B-grade publisher, 2026-06-15 04:34 EDT)
    - The Hacker News (B-grade publisher, 2026-06-15 05:59 EDT)

  Independence test PASSES: different publishing organizations,
  no upstream-citation circularity (SA and THN both cite Sansec
  primary but operate as independent publishers with distinct
  editorial / technical-detail layers — THN added the
  84.201.6.54 attacker IP + WPM File Manager & Shell web-shell
  brand detail beyond SA's coverage; SA added the
  customer1usx@gmail.com associated-email pattern; both
  converge on the OptinMonster / TrustPulse / PushEngage core
  facts).

  WHY B2 NOT B1: Single-source-veto exception NOT applicable
  here — Sansec is the primary discoverer but two independent
  publisher relays exist, lifting cluster above single-source-
  veto floor. B1 (Confirmed) requires independent corroboration
  of the substantive claim from non-Sansec evidence basis;
  current substrate has SA + THN both relaying Sansec's
  technical-investigation evidence basis. No independent
  IR-firm or vendor-IR-team has published parallel findings
  on the Awesome Motive compromise this sweep. Conservative
  B2 anchor pending independent-basis confirmation (e.g.,
  Cloudflare / Akamai / Sucuri / Wordfence publishing their
  own telemetry on the malicious JS distribution).

  WHY MONITORING-TIER INCLUSION NOT ACTION-TIER:
    1. NO A&D-PRIME PRODUCTION DEPLOYMENT CONTEXT. OptinMonster
       (lead-gen / opt-in forms), TrustPulse (social-proof
       notifications), PushEngage (push notifications) are
       consumer marketing plugins. NOT typically used in
       A&D-prime production environments. Frank's A&D-prime
       target stack does not deploy these plugins as part of
       core production architecture.
    2. NO US A&D / DIB VICTIM NAMED. Reach claim of ~1.2M
       sites is publisher-level rollup, not enumerated to
       any specific A&D-prime victim.
    3. NO CVE ASSIGNED. UpdraftPlus initial-entry theory
       (PushEngage's claim) is DISPUTED by Sansec ("the
       breached system is still unknown"); no canonical
       CVE-class vector exists for FCEB-class urgency.
    4. NO TRACKED-ROSTER ACTOR ATTRIBUTION. Sansec frames as
       "Polyfill-pattern attackers" — method-pattern comparison
       to Sansec's own 2024 Polyfill discovery, NOT actor-
       cluster identity carryover. Hard Rule 2 binding.
    5. SUPPLY-CHAIN-PATTERN-AWARENESS VALUE: Polyfill 2024
       lineage method-pattern (third-party JS CDN compromise
       silently replacing clean payload with malicious code)
       has supply-chain awareness substrate value for A&D-prime
       operational stack hardening — but the specific plugin
       set is out-of-scope for A&D-prime production deployment.

  WHAT THE B2 ATTESTS:
    (a) Awesome Motive WordPress plugin family (OptinMonster,
        TrustPulse, PushEngage) served compromised JavaScript
        via clientcdn.pushengage.com over the affected windows.
    (b) C2 typosquat tidio.cc (registered 2026-04-28) acted
        as the exfiltration / second-stage host.
    (c) Attacker server IP 84.201.6.54 (Yandex Cloud ASN per
        public DNS) is part of the campaign infrastructure.
    (d) Hidden backdoor plugins 'content-delivery-helper'
        v2.7.1 and 'database-optimizer' v2.9.4 + 'WPM File
        Manager & Shell' web-shell deployed.
    (e) Admin account patterns 'developer_api1' (fixed) and
        'dev_xxxxxx' (randomized variants) created.
    (f) PushEngage's UpdraftPlus initial-entry theory is
        DISPUTED by Sansec.
    (g) Sansec frames as "Polyfill-pattern" method comparison.

  WHAT THE B2 DOES NOT ATTEST:
    - That Yandex Cloud hosting = Russian state-actor attribution
      (Sansec does NOT make this claim; cloud-provider
      attribution is method-pattern not nation-state binding).
    - That this campaign is operator-overlap with the 2024
      Polyfill cluster (Sansec uses method-pattern framing,
      NOT actor-cluster identity carryover).
    - Specific CVE-class initial-access vector (Sansec: still
      unknown; PushEngage's UpdraftPlus theory disputed).
    - Any A&D-prime victim count (no enumeration to A&D-prime
      production deployments).
    - Long-term attacker control persistence beyond the
      observed campaign windows.

  HARD RULE 2 binding constraint: PRESERVED.
    - "Polyfill-pattern attackers" preserved as Sansec method-
      framing, NOT actor-cluster identity carryover.
    - Yandex Cloud ASN attribution preserved as cloud-provider
      method-pattern, NOT Russian-state attribution.
    - No nation-state attribution introduced.

  HARD RULE 6 binding constraint: PRESERVED. Raw-signal
  contains zero verbatim quotes over 15 words; this finding
  does not introduce any quotes.

  HARD RULE 8 binding constraint: First-party Splunk hunt
  recommended for net-new IOC `84.201.6.54` + C2 typosquat
  `tidio.cc` against defenseclaw_local + archimedes indices.
  Hunt expectation: NEGATIVE — Frank's A&D-prime production
  stack does not deploy OptinMonster / TrustPulse / PushEngage,
  so visibility-limited absence by stack composition is
  expected. Silent Splunk does NOT disconfirm. NOT promoting
  these IOCs to the standing 19-IOC PeopleSoft / UNC6240
  sentinel set because (a) different cluster, (b) consumer-
  WordPress out-of-A&D-prime scope.

source_reliability:
  grade: B
  source_name: "The Hacker News + Security Affairs + Sansec primary"
  source_yaml_id: thehackernews
  grade_rationale: >
    Cluster anchor source for grading purposes is THN (B-grade,
    provisional, awaiting_ratification per source-grades.yaml
    provisional_since 2026-05-14). SA (B-grade, provisional
    2026-05-29) provides parallel publisher relay. Sansec is
    the research-firm primary (A-tier security-research firm
    with Polyfill 2024 incident attribution lineage; not
    individually graded in source-grades.yaml but Mandiant /
    CrowdStrike / Unit-42-class research-firm tier).
  provisional: true
  provisional_since: 2026-05-14

credibility:
  grade: 2
  checklist_passed:
    - probably_true_consistent_with_established_ttps_polyfill_2024_method_pattern_lineage
    - probably_true_no_contradicting_evidence_from_a_or_b_grade_sources
    - probably_true_technical_claims_internally_coherent_typosquat_warmup_cdn_compromise_pattern_well_documented
  rationale: >
    Grade 2 (Probably True): Sansec primary disclosure relayed
    by two independent B-grade publishers (SA + THN); no
    contradicting A/B-grade source; technical claims (typosquat
    warmup, CDN compromise, hidden plugin backdoor pattern,
    admin account creation) are internally coherent and
    consistent with established Polyfill-pattern supply-chain-
    compromise TTPs. PushEngage's UpdraftPlus initial-entry
    theory contradicts Sansec's "still unknown" assessment;
    Sansec's disputation is the higher-credibility reading
    (research-firm-primary vs affected-vendor self-explanation).

corroboration:
  independent_sources:
    - sansec_primary
    - securityaffairs
    - thehackernews
  independent: true  # Three independent surfaces; SA and THN relay Sansec primary but operate as independent publishers with distinct net-new technical detail layers
  test_passed: >
    Multi-publisher independence PASSES. Different publishing
    organizations (Sansec research firm, Security Affairs
    publisher, The Hacker News publisher), no upstream-citation
    circularity beyond shared Sansec primary, distinct
    editorial / technical-detail layers (THN added 84.201.6.54
    + WPM File Manager & Shell web-shell brand; SA added
    customer1usx@gmail.com associated-email pattern).
    Evidence-basis independence: PARTIAL — both publishers
    relay Sansec's investigation evidence; independent IR-firm
    or vendor-IR-team telemetry on the malicious JS distribution
    (e.g., Cloudflare / Akamai / Sucuri / Wordfence) would
    lift to evidence-basis-independence-PASS and B1 anchor.
  notes: >
    Independent IR-firm telemetry on the malicious JS
    distribution OR Cloudflare / Sucuri / Wordfence parallel
    findings on the OptinMonster / TrustPulse / PushEngage
    compromise would lift cluster from B2 to B1.

first_party_precedence:
  applied: false
  splunk_evidence: >
    Hunt recommended for `84.201.6.54` + `tidio.cc` against
    defenseclaw_local + archimedes indices but not executed
    this sweep (cluster is monitoring-tier; not blocking
    promotion). Frank's A&D-prime production stack does not
    deploy OptinMonster / TrustPulse / PushEngage; visibility-
    limited absence by stack composition expected. Silent
    Splunk does NOT disconfirm.

single_source_veto_applied: false  # Multi-publisher independence achieved; veto does not apply at cluster-anchor
wep_ceiling: likely  # Multi-publisher independence + research-firm primary; absent independent evidence-basis corroboration cluster does not reach very_likely
wep_layered:
  sansec_primary_disclosure_substrate: very_likely  # A-tier research firm + 2 independent publisher relays
  pushengage_cdn_compromise_2026_06_12_22_17_to_2026_06_14: likely  # B2 multi-publisher
  optinmonster_trustpulse_25_min_window: likely  # B2 multi-publisher
  c2_typosquat_tidio_cc_with_45d_warmup: likely  # B2 multi-publisher
  attacker_server_84_201_6_54_yandex_cloud_asn: likely  # B2 multi-publisher; ASN attribution is method-pattern
  hidden_backdoor_plugins_with_webshell: likely  # B2 multi-publisher
  admin_account_patterns_developer_api1_dev_xxxxxx: likely  # B2 multi-publisher
  approximately_1_2m_sites_collective_reach: roughly_even_chance  # Reach claim is publisher rollup; reasonable but not Archimedes-verified
  pushengage_updraftplus_theory_disputed_by_sansec: likely  # Sansec's disputation is the higher-credibility reading
  polyfill_pattern_method_framing_not_actor_cluster_identity: very_likely  # Verifiable Sansec framing
  no_nation_state_or_actor_cluster_attribution: very_likely  # Verifiable absence + Hard Rule 2 binding
  no_ad_prime_production_deployment_context: very_likely  # Verifiable structural absence
  no_us_ad_dib_victim_named_or_cve_assigned: very_likely  # Verifiable absence

inclusion:
  eligible_for:
    - daily_brief_monitoring  # B2 → monitoring tier; supply-chain-pattern-awareness substrate value; Polyfill method-pattern lineage worth A&D-operational-stack hardening context
    - weekly_synthesis  # Multi-victim consumer-marketing-plugin compromise + Polyfill-method-pattern lineage candidate for Sunday synthesis as supply-chain-awareness substrate
  not_eligible_for:
    - flash  # All 6 FLASH triggers NEGATIVE per collector evaluation (no tracked actor, no A&D-prime victim, no CVE, no zero-day)
    - daily_brief_action  # No A&D-prime production deployment context; no operational urgency to US A&D
    - actor_profile_update  # "Polyfill-pattern" is method-framing not actor-cluster; no roster actor to update
  flash_eligible: false
  flash_threshold_met: false

graded_at: 2026-06-15T08:20:00-04:00

# ============================================================================
# Cluster metadata
# ============================================================================
cluster:
  topic: "Awesome Motive WordPress CDN supply-chain compromise — OptinMonster + TrustPulse + PushEngage served malicious JS via clientcdn.pushengage.com (PushEngage hot ~36h; OM + TP hot ~25 min on 2026-06-12); C2 tidio.cc typosquat (45d warmup); attacker IP 84.201.6.54 Yandex Cloud ASN; hidden backdoor plugins + web-shell; ~1.2M sites collective reach; Polyfill-pattern method-framing per Sansec; NOT actor-cluster identity carryover; NO A&D-prime production deployment context"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-06-15-am-004-thn-sa-sansec-awesome-motive-wordpress-cdn-supply-chain-second-publisher-relay-net-new-ioc
  attribution_claims:
    - claimed_attribution: "Sansec method-framing: 'Polyfill-pattern attackers'"
      claimed_by_sources: [sansec_primary, thehackernews_relay, securityaffairs_relay]
      requires_analyst_review: false
      note: "METHOD-PATTERN framing only — Sansec compares to its own 2024 Polyfill discovery as TTP-pattern, NOT actor-cluster identity carryover. Hard Rule 2 binding: NO actor-cluster name fabricated; NO operator-overlap claim between 2024 Polyfill cluster and this campaign."
    - claimed_attribution: "Cloud-provider attribution: Yandex Cloud ASN per public DNS"
      claimed_by_sources: [thehackernews_relay]
      requires_analyst_review: false
      note: "CLOUD-PROVIDER method-pattern only — Sansec does NOT attribute to Russian state actor. ASN-level cloud-provider context is infrastructure-rental fact, NOT nation-state binding. Hard Rule 2 preserved."

# ============================================================================
# IOC hunt set — NET-NEW VS PRIOR CORPUS
# ============================================================================
iocs:
  domains:
    - value: tidio.cc
      type: c2_domain
      first_seen: 2026-04-28  # domain registration
      first_active: 2026-06-12T22:17:00Z
      tld_typosquat_of: tidio.com
      sources: [sansec, thehackernews, securityaffairs]
    - value: clientcdn.pushengage.com
      type: legitimate_compromised_cdn
      affected_files: ["pushengage-web-sdk.js", "pushengage-subscription.js"]
      sources: [sansec, thehackernews]
  ipv4:
    - value: 84.201.6.54
      type: attacker_server
      asn_owner: "Yandex Cloud (per public DNS; method-pattern not state-actor binding)"
      sources: [sansec, thehackernews]
      net_new_in_thn_relay: true
  malicious_admin_account_patterns:
    - value: "developer_api1"
      type: fixed_username
      sources: [sansec, thehackernews, securityaffairs]
    - value: "customer1usx@gmail.com"
      type: associated_email
      sources: [sansec, securityaffairs]
    - value: "dev_xxxxxx"
      type: randomized_username_pattern
      sources: [sansec, thehackernews, securityaffairs]
  plugin_disguises:
    - value: "content-delivery-helper"
      version: "v2.7.1"
      type: hidden_backdoor_plugin
      sources: [sansec, thehackernews, securityaffairs]
    - value: "database-optimizer"
      version: "v2.9.4"
      type: hidden_backdoor_plugin
      sources: [sansec, thehackernews, securityaffairs]
  webshell_brand:
    - value: "WPM File Manager & Shell"
      type: webshell_brand_string
      capability: "arbitrary system commands + file uploads + eval-class PHP via unauthenticated entry"
      sources: [sansec, thehackernews]
      net_new_in_thn_relay: true
  splunk_hunt_recommended_but_not_executed_this_sweep:
    targets: ["84.201.6.54", "tidio.cc"]
    expected_result: "NEGATIVE — Frank's A&D-prime production stack does not deploy OptinMonster / TrustPulse / PushEngage; visibility-limited absence by stack composition"

# ============================================================================
# Relationship to existing findings
# ============================================================================
relationships:
  related_findings_by_method_pattern_not_operator_overlap:
    - finding_id_pattern: "Polyfill 2024 lineage (Sansec primary discovery)"
      relationship: "METHOD-PATTERN substrate lineage only — Sansec's framing compares this 2026 Awesome Motive campaign to its own 2024 Polyfill third-party-JS-CDN-compromise discovery as TTP-pattern (CDN silently replacing clean payload with malicious code). NOT operator-overlap claim. Hard Rule 2 binding: Archimedes does not collapse the 2024 and 2026 campaigns into a single actor-cluster identity."
  related_findings:
    - finding_id: finding-2026-06-12-0005
      relationship: "Cluster-adjacent supply-chain awareness substrate — Sonatype / Atomic Arch 400+ AUR Rust credential-stealer + eBPF rootkit developer-tier supply-chain compromise. DIFFERENT cluster (AUR / Rust dev tooling vs WordPress CDN), DIFFERENT actor unknown, SAME meta-category (supply-chain compromise). Co-relationship: developer-tier and consumer-marketing-CDN-tier supply-chain compromises co-occurring in current substrate window."

# ============================================================================
# Open questions for analyst
# ============================================================================
open_questions_for_analyst:
  - "Independent IR-firm telemetry watch — Cloudflare / Akamai / Sucuri / Wordfence parallel findings on the OptinMonster / TrustPulse / PushEngage malicious JS distribution would lift cluster from B2 to B1 (evidence-basis-independence)."
  - "Yandex Cloud ASN attribution: confirm method-pattern framing preserved across downstream coverage; Hard Rule 2 binding requires NO escalation to Russian-state attribution absent explicit Sansec / IR-firm attribution language. Watch for downstream publisher drift."
  - "PushEngage's UpdraftPlus initial-entry theory is DISPUTED by Sansec. Independent vulnerability-management vendor (Patchstack / WPScan) telemetry on the dispute would clarify the load-bearing initial-access vector. Currently 'still unknown' per Sansec."
  - "A&D-prime operational stack hardening: although OptinMonster / TrustPulse / PushEngage are out-of-A&D-production-scope, the broader Polyfill-method-pattern (third-party JS CDN silent payload swap) is a supply-chain class threat worth A&D-prime CIS hardening review. Sector-context substrate for weekly synthesis."

analyst_review_required: false  # B2 monitoring tier with multi-publisher independence; no SAT-ACH / SAT-KAC trigger; consumer-WordPress out-of-A&D-scope dampens load-bearing-assumption analysis value
red_team_review_required: false  # WEP ceiling likely — does not meet very_likely red-team invocation floor

# ============================================================================
# Lifecycle
# ============================================================================
tlp: CLEAR
published_in_briefs:
  - 2026-06-15-morning
retracted: false
retraction_brief_id: null
---

# Awesome Motive WordPress CDN Supply-Chain — Polyfill-Pattern Method, Multi-Publisher Independent Corroboration, Consumer-Plugin Scope (Not A&D-Prime)

## Summary

Sansec disclosed 2026-06-13 that Awesome Motive's WordPress
plugin family — OptinMonster, TrustPulse, and PushEngage —
served compromised JavaScript through the legitimate
clientcdn.pushengage.com CDN. Security Affairs (2026-06-15
04:34 EDT) and The Hacker News (2026-06-15 05:59 EDT) are
two independent publisher relays, providing multi-publisher
corroboration. PushEngage's CDN served compromised script
from 2026-06-12 22:17 UTC until 2026-06-14 (~36h); OptinMonster
and TrustPulse were hot for a tighter ~25-minute window
(22:17-22:42 UTC 2026-06-12). C2 traffic egressed to a tidio.cc
typosquat (registered 2026-04-28 — ~45d warm-up before first
malicious activity). THN adds a net-new attacker server IP
`84.201.6.54` (Yandex Cloud ASN per public DNS — method-
pattern not state-actor binding) and the 'WPM File Manager &
Shell' web-shell brand string. Hidden backdoor plugins
'content-delivery-helper' v2.7.1 and 'database-optimizer'
v2.9.4 were deployed; admin account patterns 'developer_api1'
(fixed) and 'dev_xxxxxx' (randomized) created.

Sansec frames the campaign as "Polyfill-pattern attackers"
— a method-pattern comparison to Sansec's own 2024 Polyfill
discovery, NOT an actor-cluster identity carryover. PushEngage's
UpdraftPlus initial-entry theory is DISPUTED by Sansec ("the
breached system is still unknown"). Cluster anchors B2 / WEP
likely — multi-publisher independence achieved at publisher
layer; evidence-basis independence pending independent IR-firm
parallel telemetry. NO A&D-prime production deployment context
(consumer marketing / lead-generation / push-notification
plugins not in A&D-prime production stack); NO US A&D / DIB
victim named; NO CVE assigned; NO tracked-roster actor; NO
nation-state attribution.

## Sources

### Sansec (research-firm primary, A-tier)

- Primary disclosure 2026-06-13.
- Polyfill 2024 incident attribution lineage gives Sansec
  established credibility on third-party-JS-CDN-compromise
  pattern.

### The Hacker News (thehackernews, digraph B)

- URL: https://thehackernews.com/2026/06/popular-wordpress-plugin-scripts.html
- Published: 2026-06-15T09:59:38Z (05:59 EDT)
- Net-new vs SA: `84.201.6.54` attacker server IP; 'WPM
  File Manager & Shell' web-shell brand string; ~1.2M
  collective-reach refinement; PushEngage UpdraftPlus
  theory disputed by Sansec framing.

### Security Affairs (securityaffairs, digraph B)

- URL: https://securityaffairs.com/193616/malware/supply-chain-attack-hits-popular-wordpress-plugins-through-awesome-motive-cdn.html
- Published: 2026-06-15T08:34:02Z (04:34 EDT)
- First publisher-relay; covered core facts including admin
  account patterns + plugin disguises + customer1usx@gmail.com
  associated email.

## Technical detail

- **Compromise vector**: Awesome Motive corporate CDN
  (clientcdn.pushengage.com) served two malicious JavaScript
  files (pushengage-web-sdk.js + pushengage-subscription.js)
  during the affected windows. Initial-access vector to the
  Awesome Motive CDN is "still unknown" per Sansec
  (PushEngage's UpdraftPlus theory is disputed).
- **C2 infrastructure**: tidio.cc (typosquat of legitimate
  tidio.com), registered 2026-04-28 — plan-ahead pattern with
  ~45d warm-up before first malicious activity 2026-06-12.
- **Attacker server**: 84.201.6.54 (Yandex Cloud ASN per
  public DNS; method-pattern not state-actor binding).
- **Persistence**: hidden backdoor WordPress plugins
  'content-delivery-helper' (v2.7.1) and 'database-optimizer'
  (v2.9.4); 'WPM File Manager & Shell' web-shell allowing
  arbitrary system commands, file uploads, and eval-class
  PHP execution via unauthenticated entry points.
- **Admin account patterns**: 'developer_api1' (fixed
  username) and 'dev_xxxxxx' (randomized variants); some
  associated with email customer1usx@gmail.com.
- **Reach**: ~1.2M sites collectively across the three
  plugin families (publisher rollup; not Archimedes-verified).

## Attribution language (preserved per Hard Rule 2)

- Sansec method-framing: "Polyfill-pattern attackers" — a
  TTP-pattern comparison to Sansec's 2024 Polyfill discovery,
  NOT an actor-cluster identity carryover.
- Yandex Cloud ASN attribution is cloud-provider hosting
  fact, NOT Russian-state-actor attribution.
- NO tracked threat actor named; NO nation-state attribution
  by any source.

## A&D-prime / watchlist match

- **NONE direct.** OptinMonster, TrustPulse, PushEngage are
  consumer marketing / lead-generation / push-notification
  plugins. NOT used in A&D-prime production environments per
  known sector stack. Consumer WordPress ecosystem.
- **NO A&D-prime victim named** in any source.
- **Supply-chain-pattern-awareness value**: The Polyfill-method-
  pattern (third-party JS CDN silent payload swap) is a
  supply-chain class threat worth A&D-prime CIS hardening
  review for sector context, but the specific plugin set is
  out-of-scope for A&D-prime production deployment.

## IOCs surfaced

See `iocs` frontmatter block. Net-new vs prior corpus:
`84.201.6.54` attacker server IP (THN net-new vs SA);
'WPM File Manager & Shell' web-shell brand string (THN
net-new vs SA). Splunk hunt for `84.201.6.54` + `tidio.cc`
recommended for completeness but expected NEGATIVE due to
Frank's A&D-prime production stack composition (no
OptinMonster / TrustPulse / PushEngage deployment).

## Relationship to existing findings

- **Polyfill 2024 lineage** (Sansec primary discovery): METHOD-
  PATTERN substrate lineage only. Sansec compares this 2026
  campaign to the 2024 Polyfill discovery as TTP-pattern
  framing. NOT operator-overlap claim. Hard Rule 2 binding
  preserved.
- **finding-2026-06-12-0005** (Sonatype Atomic Arch 400+ AUR
  Rust credential-stealer + eBPF rootkit developer-tier
  supply-chain): cluster-adjacent in meta-category (supply-
  chain compromise) but different tier (developer tools vs
  consumer marketing CDN); different actor (unknown vs
  unknown but distinct campaigns).

## Open questions for analyst

1. Independent IR-firm parallel telemetry (Cloudflare /
   Akamai / Sucuri / Wordfence) on the malicious JS
   distribution would lift cluster B2 → B1.
2. Yandex Cloud method-pattern framing must be preserved
   across downstream coverage; watch for publisher drift to
   Russian-state attribution absent Sansec / IR-firm
   language.
3. PushEngage UpdraftPlus theory dispute resolution — load-
   bearing initial-access vector is "still unknown" per
   Sansec; vulnerability-management vendor (Patchstack /
   WPScan) telemetry would clarify.
4. A&D-prime sector-context substrate: Polyfill-method-
   pattern hardening review for third-party JS CDN
   dependencies in A&D-prime production stack — weekly
   synthesis candidate.
