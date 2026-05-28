---
finding_id: finding-2026-05-28-0001-bleepingcomputer-carnival-cruise-shinyhunters-6m-records-confirmation-mariner-society-holland-america
created_at: 2026-05-28T07:55:00-04:00
graded_by: grader
grading_run_id: morning-20260528-080000
grading_mode: scheduled_brief
test: false

# Core grading (admiralty-grading skill output)
digraph: B2
digraph_layered:
  bleepingcomputer_relay_of_carnival_self_disclosure: B2
  carnival_corporation_self_disclosure_of_breach: A2   # vendor self-disclosure of own incident — procedurally A for facts of the disclosure itself
  shinyhunters_self_claim_of_8_7m_records: C3           # actor self-claim, not independently verified
  carnival_confirmed_5_995_277_records: A2              # victim count — Carnival is authoritative on its own data
  social_engineering_employee_vector: A2                # Carnival self-disclosed mechanism
  salesforce_aura_or_salesloft_drift_implication: C3    # BleepingComputer editorial framing, NOT Carnival-confirmed
  apr_14_initial_access_apr_22_data_theft_confirmed: A2 # Carnival self-disclosed timeline
  data_categories_names_dob_email_gender_location_loyalty: A2  # Carnival self-disclosed
  no_payment_card_no_ssn_no_passport: A2                # Carnival self-disclosed negative
  bling_libra_alias_for_shinyhunters_per_unit42: A2     # via finding-0003 this same cycle (Unit 42 canonical)
  no_ad_prime_named: A1
  no_cve_identity_layer: A1
  hard_rule_2_no_scattered_spider_cross_walk: A1
  cluster_anchor: B2

digraph_anchor: >
  Cluster digraph B2 anchored on BleepingComputer (Sergiu Gatlan,
  2026-05-28 06:49 EDT today, in-window for AM-28 14h pre-brief) relay
  of Carnival Corporation's customer-notification disclosure following
  ShinyHunters extortion claim from April 2026. BleepingComputer is
  B-grade per source-grades.yaml. Carnival's own customer-notification
  filing is A-grade for the procedural facts of the disclosure itself
  (vendor self-statement is authoritative for what the vendor is
  saying). ShinyHunters' April 2026 self-claim of 8.7M records is C3
  (actor self-claim, threat-actor source, not independently verified —
  and Carnival's 5,995,277-confirmed-records figure is ~31% below the
  ShinyHunters self-claim, consistent with the well-documented actor
  pattern of scope-inflation for extortion leverage). The cluster
  anchor B2 reflects:
    (a) BleepingComputer (B) as the in-corpus proximate source
    (b) Carnival (A on its own disclosure facts) as the victim self-
        confirmation — independent corroboration of "an incident
        occurred" alongside the older ShinyHunters claim
    (c) Two independent sources on "an incident occurred + scope
        approximately 6M customers" — clearing single-source veto
        for the procedural-fact-of-disclosure layer
    (d) Direct corpus parallel to finding-2026-05-27-0006 (Charter
        Communications / ShinyHunters / 40M) — same actor cluster,
        distinct victim, both Salesforce-pattern editorial framing
        from BC
  ShinyHunters attribution layer is editorial — Carnival has NOT
  publicly confirmed the ShinyHunters attribution. The BleepingComputer
  body explicitly notes Carnival did not reply to confirm ShinyHunters'
  claims. Per Hard Rule 2 the attribution layer reads as "claimed
  responsibility" / "self-claim" only.

source_reliability:
  grade: B
  source_name: "BleepingComputer (Sergiu Gatlan)"
  source_yaml_id: bleepingcomputer
  grade_rationale: >
    BleepingComputer pre-assigned B per source-grades.yaml. In-window
    report 2026-05-28 06:49 EDT (today morning, within AM-28 14h
    pre-brief window). BleepingComputer reports Carnival's own
    customer-notification disclosure with the 5,995,277-customer
    figure plus the ShinyHunters self-claim layer. Single-byline,
    single-source for the breach-confirmation layer; SecurityWeek /
    THN / The Record / Krebs silent on Carnival Cruise in the AM-28
    window.
  provisional: false
  victim_self_disclosure:
    organization: Carnival Corporation (Holland America Line operating subsidiary; Mariner Society loyalty program)
    self_disclosure_grade: A   # for procedural facts of what Carnival is saying about itself
    self_disclosure_contribution: >
      Carnival's customer-notification filing confirms (1) the incident
      occurred, (2) initial unauthorized activity detected 2026-04-14,
      (3) data theft confirmed 2026-04-22, (4) social engineering of
      an employee account as the initial-access vector, (5) 5,995,277
      affected customers, (6) data categories limited to names / DOBs
      / emails / genders / geographic locations / Mariner Society
      loyalty details, and (7) explicitly NO payment-card / SSN /
      passport data. Carnival did NOT name Salesforce, Salesloft Drift,
      Salesforce Aura, or ShinyHunters in its own notification per the
      BleepingComputer relay.
  threat_actor_self_claim:
    actor: ShinyHunters
    self_claim_grade: C
    self_claim_contribution: >
      ShinyHunters April 2026 self-claim of "over 8.7 million records
      and terabytes of corporate data." Carnival's confirmed figure is
      5,995,277 records — materially below the self-claim (~31% lower).
      Pattern-consistent with corpus-anchored ShinyHunters extortion
      tradecraft (scope inflation for leverage).
  editorial_framing:
    pattern: "Salesforce-customer-targeting via Salesforce Aura data-theft and Salesloft Drift campaign lineage"
    framing_grade: C  # BC editorial framing, NOT Carnival-confirmed
    framing_caveat: >
      BleepingComputer situates Carnival within the broader ShinyHunters
      / Salesforce-targeting pattern ("ShinyHunters has been targeting
      Salesforce customers"). Carnival's own notification does NOT
      confirm Salesforce implication. The Salesforce framing is BC
      editorial, not victim-attested.

credibility:
  grade: 2
  checklist_passed:
    - probably_true_ttp_consistent_with_2026_shinyhunters_pattern
    - probably_true_no_contradicting_ab_grade_source
    - probably_true_technical_claims_internally_coherent_victim_count_below_actor_claim
  rationale: >
    Probably True (2) on the breach-occurred layer: Carnival's own
    notification + ShinyHunters' April 2026 self-claim are independent
    sources on "an incident occurred" (the actor named the victim
    publicly two months before victim disclosure; victim has now
    confirmed the incident with its own scope figure). Cluster grade
    B2 = BleepingComputer B-grade relay anchor + Carnival A-grade
    self-disclosure + ShinyHunters C-grade self-claim. ShinyHunters
    operational pattern of Salesforce-customer-targeting in 2026 is
    corpus-anchored via finding-2026-05-27-0006 (Charter Communications
    / 40M / Salesforce-Entra-vishing) and prior reported victims —
    Carnival fits the same operational pattern though Carnival's own
    notification does not confirm Salesforce implication. No
    contradicting A/B-grade source. Single-byline single-relay for the
    breach-confirmation layer — second independent A/B-grade source
    would lift cluster to B1/A2.

corroboration:
  independent_sources:
    - bleepingcomputer
    - carnival-self-disclosure
  independent: true
  independent_test_passed: >
    BleepingComputer (B media relay) and Carnival Corporation's
    customer-notification filing (A vendor self-disclosure on own
    incident) are independent of each other on the "an incident
    occurred + scope approximately 6M customers" layer. BleepingComputer
    relays the notification rather than co-authoring it. ShinyHunters'
    April 2026 self-claim is a third source on "an incident occurred
    with ShinyHunters responsible" but it is NOT independent corpus-
    grade evidence on scope (actor self-claim has incentive to inflate).
  awaiting_corroboration:
    - "Second A/B-grade media relay (SecurityWeek / THN / The Record /
      Krebs / Reuters / Bloomberg) on Carnival's notification —
      AM-28-window silence is collection-window limitation, not
      meaningful negative signal yet"
    - "A/B-grade IR firm independent attribution or telemetry
      (Mandiant / MSTIC / CrowdStrike / Unit 42 / Recorded Future /
      Volexity) — none has published parallel attribution on the
      Carnival incident specifically"
    - "Carnival Corporation 8-K SEC filing (would establish A-grade
      regulatory anchor on materiality + scope + remediation status)"
    - "Class-action filings / state AG breach-notifications providing
      regulatory cross-confirmation of scope and data-category claims"

first_party_precedence:
  applied: false
  splunk_evidence: null
  splunk_query_executed: >
    Splunk query against defenseclaw_local + archimedes over -24h@h
    covering "Carnival", "ShinyHunters", "Holland America", "Mariner
    Society", "Salesforce export". Zero IOC events. Hard Rule 8:
    silence is not disconfirming. Carnival Corporation is cruise /
    hospitality consumer-brand, not A&D-prime — no expected
    defenseclaw_local visibility on Carnival-specific infrastructure
    or Salesforce tenants. 67th consecutive dormant non-self sweep on
    defenseclaw_local per pre-brief sentinel raw-2026-05-28-am-000.

single_source_veto_applied: false
single_source_veto_rationale: >
  Veto does not apply on the breach-occurred layer (BleepingComputer
  relay + Carnival self-disclosure are two independent sources).
  Veto WOULD apply on the ShinyHunters-as-perpetrator-attribution
  layer if treated in isolation (actor self-claim is single-source +
  not victim-confirmed) but the cluster anchor follows the
  procedurally-corroborated breach-occurred layer at B2. Scope
  comparison (5,995,277 confirmed vs 8.7M+ claimed) is itself a
  cross-check that the actor's claim is inflated, which is corpus-
  consistent.

wep_ceiling: very_likely
wep_layered:
  breach_at_carnival_corporation_occurred: very_likely    # Carnival self-disclosure + ShinyHunters claim
  scope_approximately_6m_records_5_995_277_confirmed: very_likely  # Carnival's own figure
  social_engineering_of_employee_account_initial_vector: very_likely  # Carnival self-disclosed
  incident_dates_apr_14_initial_apr_22_exfil_confirmed: very_likely  # Carnival self-disclosed
  shinyhunters_responsible_per_self_claim_only: likely    # actor self-claim, victim has NOT publicly confirmed attribution
  salesforce_implication_per_bc_editorial_framing: roughly_even_chance  # BC editorial, NOT Carnival-confirmed
  bling_libra_unit42_alias_mapping_to_shinyhunters: very_likely  # Unit 42 canonical naming (per finding-0003 this cycle)
  shinyhunters_8_7m_records_scope_claim_actual: roughly_even_chance  # exceeds confirmed Carnival figure by 31%
  shinyhunters_operational_continuation_april_2026_through_today: very_likely  # corpus-anchored across multiple 2026 victims
  ad_prime_indirect_exposure_via_same_tradecraft_class: roughly_even_chance  # structural inference

inclusion:
  eligible_for:
    - daily_brief_action            # B2 + extortion-watch standing section relevance + corpus-paired with finding-0003 same cycle
    - daily_brief_monitoring
    - weekly_synthesis              # multi-victim 2026 ShinyHunters extortion-pattern signal cumulation
    - ioc_master_index_propagation  # tradecraft-pattern entry rather than IOC-specific (no IPs/hashes/domains)
  not_eligible_for:
    - flash             # ShinyHunters not in roster (Trigger 2 fails); no CVE (Trigger 1 fails); no first-party hit (Trigger 3 fails); no A&D-prime campaign (Trigger 5 fails — cruise/hospitality consumer)
    - actor_profile_update  # ShinyHunters not in _roster.yaml; /new-actor scaffolding remains operator-decision pending from prior cycle
  inclusion_rationale: >
    B2 cluster on Carnival's self-disclosure of breach following
    ShinyHunters April 2026 extortion claim. Eligible for AM-28 brief
    action tier on the basis that: (a) the ShinyHunters 2026 multi-
    victim extortion pattern is now corpus-confirmed across Carnival
    (6M) + Charter Communications (40M, finding-2026-05-27-0006) +
    BC-cited "hundreds of companies worldwide" — substantially raising
    defender actionability for A&D-prime estates running Salesforce or
    Salesforce-class CRM; (b) the Bling Libra = ShinyHunters alias
    mapping is formally codified by Unit 42 in today's AM-003 Out of
    the Crypt piece (finding-2026-05-28-0003 this cycle), making
    Carnival the named-victim corroboration data-point for the Unit 42
    cluster-mapping piece; (c) the social-engineering-employee initial-
    access vector is the corpus-anchored ShinyHunters TTP. NOT FLASH-
    eligible per FLASH-POLICY triggers all failing. /new-actor
    scaffolding for ShinyHunters remains an operator-pending decision
    from finding-2026-05-27-0006.

# Cluster metadata
cluster:
  topic: "Carnival Corporation (Holland America Line subsidiary, Mariner Society loyalty program) confirms breach affecting 5,995,277 customers via customer-notification filing — initial unauthorized activity 2026-04-14, data theft confirmed 2026-04-22 — social engineering of employee account as initial-access vector — data categories limited to names/DOBs/emails/genders/geographic-locations/loyalty-details; NO payment card / SSN / passport — ShinyHunters extortion gang self-claimed responsibility in April 2026 alleging 8.7M+ records (~31% above confirmed figure) — Carnival has NOT publicly confirmed ShinyHunters attribution — BleepingComputer editorial framing situates incident within broader ShinyHunters/Salesforce-customer-targeting pattern (Salesloft Drift, Salesforce Aura) but Carnival's own notification does NOT confirm Salesforce implication — Bling Libra = ShinyHunters alias formally codified by Unit 42 today (finding-2026-05-28-0003 this cycle) — operationally adjacent to Scattered LAPSUS$ Hunters cluster which includes roster #013 Scattered Spider — per Hard Rule 2 NO cross-walk to Scattered Spider for the Carnival incident specifically — no A&D-prime named — cruise/hospitality consumer-sector breach with indirect A&D-relevance via TTP-template portability to any Salesforce-using enterprise"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-05-28-am-001-bleepingcomputer-carnival-cruise-shinyhunters-6m-records-confirmation-mariner-society-holland-america
  related_actors: []  # ShinyHunters not in _roster.yaml
  related_actors_hard_rule_2_caveat:
    - actor_id: "013"
      actor_name: "Scattered Spider"
      tradecraft_overlap: "Scattered LAPSUS$ Hunters cluster (per Unit 42 finding-2026-05-28-0003) includes Bling Libra (ShinyHunters) + Scattered Spider (#013) + LAPSUS$ Group — operationally adjacent but Unit 42 distinguishes Bling Libra from Scattered Spider as distinct cluster members"
      cross_walk_status: "PROHIBITED per Hard Rule 2 — BleepingComputer does NOT name Scattered Spider in the Carnival relay; the Unit 42 cluster-adjacency framing names Bling Libra and Scattered Spider as separate cluster members, not as the same actor; Archimedes does NOT attribute Carnival to Scattered Spider"
    - new_actor_candidate:
        proposed_name: ShinyHunters (alias Bling Libra per Unit 42)
        proposed_threat_level: TBD
        rationale: "Operator decision flag preserved from finding-2026-05-27-0006 (Charter / 40M). Carnival adds a second confirmed 2026 victim under the same operational pattern. Multi-victim 2026 Salesforce-targeting-pattern is now strengthened; Bling Libra = ShinyHunters alias is now formally Unit 42-codified (finding-2026-05-28-0003 this cycle). /new-actor scaffolding remains operator-pending."
  related_vulnerabilities: []
  attribution_claims:
    - claim: "ShinyHunters responsible for Carnival Corporation breach"
      claimed_by: ShinyHunters self-claim April 2026 (un-corroborated by victim)
      claim_confidence_language: '"ShinyHunters extortion gang claimed responsibility" per BleepingComputer; Carnival did not reply to BC requests to confirm or deny ShinyHunters claims'
      novelty_to_corpus: false   # ShinyHunters is corpus-tracked via prior coverage (Charter, 7-Eleven, others)
      requires_analyst_review: true   # /new-actor scaffolding candidate flag carry-forward
      hard_rule_2_status: "preserved as cited; ShinyHunters self-claim is preserved as self-claim, NOT upgraded to victim-confirmed attribution"
    - claim: "Bling Libra = ShinyHunters (Unit 42 cluster-naming alias)"
      claimed_by: Unit 42 (Matt Brady + Justin Moore, 2026-05-27 18:00 EDT — see finding-2026-05-28-0003 this cycle)
      claim_confidence_language: "Unit 42 cluster-naming canonical (Palo Alto naming convention for cybercriminal clusters in the 'Libra' family); Unit 42 IS the originating source for this naming"
      novelty_to_corpus: true   # first corpus formalization of the Bling Libra alias for ShinyHunters
      requires_analyst_review: false   # Unit 42 canonical naming, single-A-grade-source, no controversial attribution claim
      hard_rule_2_status: "preserved as Unit 42 cluster-naming; Archimedes uses both names with cluster-mapping context"

# IOCs surfaced
iocs_surfaced:
  - type: tradecraft_pattern
    value: "Social engineering of employee account → access to limited portion of corporate IT system → exfiltration of customer-records data over ~8-day dwell window"
    context: "Carnival self-disclosed mechanism (verbatim: an unauthorized actor used social engineering to deceive an employee to gain access). Dwell window 2026-04-14 initial access → 2026-04-22 data theft confirmed = 8 days. Consistent with ShinyHunters 2026 operational pattern (corpus-anchored via Charter 40M finding-2026-05-27-0006)."
    confidence: high
    source_attribution: "Carnival Corporation customer-notification filing via BleepingComputer 2026-05-28"
    defanged: false
  - type: victim_organization
    value: Carnival Corporation (Holland America Line subsidiary, Mariner Society loyalty program)
    context: "World's largest cruise line operator. Confirmed 5,995,277 affected customers via customer-notification filing. Holland America Line is the named operating subsidiary; Mariner Society loyalty program references appear in the affected data set."
    confidence: high
    source_attribution: "Carnival Corporation customer-notification + BleepingComputer 2026-05-28"
    defanged: false
  - type: actor_self_claim
    value: "ShinyHunters April 2026 self-claim: 8.7M+ records and terabytes of corporate data"
    context: "Actor self-claim from April 2026, two months prior to victim confirmation. Scope claim ~31% higher than Carnival's confirmed 5,995,277-record figure. Consistent with corpus-anchored ShinyHunters / threat-actor-extortion pattern of scope inflation for leverage."
    confidence: medium
    source_attribution: "ShinyHunters via BleepingComputer relay of Carnival's notification context 2026-05-28"
    defanged: false
  - type: data_categories_affected
    value: "Names, dates of birth, email addresses, genders, geographic locations, Mariner Society loyalty program details"
    context: "Carnival-confirmed affected data categories. Explicitly excluded: payment card data, Social Security numbers, passport numbers."
    confidence: high
    source_attribution: "Carnival Corporation customer-notification filing via BleepingComputer 2026-05-28"
    defanged: false
  - type: editorial_framing_pattern_NOT_carnival_confirmed
    value: "Salesforce-customer-targeting via Salesforce Aura data-theft + Salesloft Drift campaign lineage"
    context: "BleepingComputer editorial framing situating Carnival within the broader ShinyHunters / Salesforce-targeting pattern. Carnival's own notification does NOT name Salesforce, Salesloft Drift, or Salesforce Aura. This framing is BC editorial, NOT victim-attested."
    confidence: low
    source_attribution: "BleepingComputer editorial framing 2026-05-28 (NOT Carnival)"
    defanged: false

ttp_keywords:
  - name: Social engineering of employee account for initial access
    framework_mapping: MITRE T1566 Phishing / T1078 Valid Accounts
    context: "Carnival-confirmed vector. Consistent with ShinyHunters 2026 operational pattern (vishing-Entra-SSO per Charter finding-2026-05-27-0006; Carnival notification does not specify the social-engineering channel)."
  - name: Multi-day dwell with delayed exfiltration confirmation
    framework_mapping: MITRE T1005 Data from Local System / T1530 Data from Cloud Storage
    context: "8-day window between initial-access detection (2026-04-14) and data-theft confirmation (2026-04-22) per Carnival timeline. Suggests Carnival's detection-and-response operated post-exfil rather than pre-exfil."
  - name: Loyalty-program data as collateral exfil target
    framework_mapping: MITRE T1213 Data from Information Repositories
    context: "Mariner Society loyalty program details in the exfiltrated data set. Loyalty-program data carries lower regulatory weight than payment cards / SSN / passport but high actor-resale value for downstream account-takeover / credential-stuffing campaigns."

# Downstream handoff flags
analyst_review_required: true
analyst_review_topics:
  - "/new-actor scaffolding decision for ShinyHunters: Carnival is a second confirmed 2026 victim under the same operational pattern (post-Charter / 40M from finding-2026-05-27-0006). Multi-victim corpus pattern now: Carnival 6M + Charter 40M + 'hundreds of companies worldwide' per BC framing. Bling Libra alias formally Unit 42-codified today (finding-2026-05-28-0003). Operator decision flag carries forward from prior cycle — Carnival strengthens the case for /new-actor scaffolding."
  - "Hard Rule 2 attribution-preservation framing for the brief: BleepingComputer's editorial Salesforce-pattern framing (Salesforce Aura, Salesloft Drift) is NOT Carnival-attested. The brief should report the breach + ShinyHunters self-claim as separable layers (procedural fact: breach occurred per Carnival; attribution claim: ShinyHunters claimed responsibility per their own April 2026 announcement; editorial pattern context: BC links to broader ShinyHunters/Salesforce-pattern but Carnival did not confirm Salesforce implication)."
  - "SAT-ACH candidate on the 8.7M-vs-5.995M scope dispute: H1 Carnival's confirmed figure is accurate and ShinyHunters inflated for extortion leverage (corpus-consistent pattern); H2 Carnival's figure is the notification-eligible subset and the actor's 8.7M includes records not legally requiring notification under applicable breach laws; H3 Carnival's figure is materially under-counted (legal-counsel-shaped scope minimization); H4 Surprise hypothesis — the actor's claim conflates multiple breach victims into a single tally. Load-bearing evidence: SEC 8-K materiality disclosure, state AG breach notifications, A/B-grade IR firm independent telemetry."

analysis_sections:
  sat_ach:
    ach_analysis:
      question: "What is the best-supported reading of the 8.7M-vs-5,995,277 scope discrepancy and the ShinyHunters attribution claim, given that Carnival self-discloses the lower figure and has not confirmed ShinyHunters' authorship?"
      analyzed_at: 2026-05-28T08:20:00-04:00
      analyzed_by: analyst
      analyst_run_id: analyst-20260528-082000
      red_team_review_note: >
        Grader explicitly waived red-team on this finding on the basis
        that the same claim-class was red-teamed yesterday on finding-
        2026-05-27-0006 (Charter / 40M). The analyst proceeds with both
        ACH layers (scope-dispute AND attribution) but mirrors the red-
        team posture from the Charter run — i.e., treats the actor-
        cluster-tradecraft framing with the same skepticism the red-
        team applied to "Salesforce-Entra-vishing tradecraft class" on
        Charter. The two findings should be read as a pair.

      hypotheses:
        - id: H1
          statement: "Carnival's 5,995,277 figure is the authoritative count; ShinyHunters' 8.7M self-claim is scope-inflation for extortion leverage (corpus-anchored actor pattern). ShinyHunters is the responsible actor per their own self-claim — un-corroborated by Carnival but unchallenged by any A/B-grade counter-attribution."
        - id: H2
          statement: "Carnival's 5,995,277 figure is the notification-eligible subset under applicable state breach-notification laws; the actor's 8.7M includes records not legally requiring notification (e.g., older / inactive customers; records held by non-US subsidiaries). Both figures are accurate at the populations they each describe. ShinyHunters is the responsible actor."
        - id: H3
          statement: "Carnival's 5,995,277 figure is materially under-counted — legal-counsel-shaped scope minimization to limit class-action exposure and SEC 8-K materiality framing. The actor's ~8.7M is closer to ground truth. ShinyHunters is the responsible actor."
        - id: H4
          statement: "Surprise / composite: ShinyHunters' April 2026 claim conflates multiple breach victims into a single tally (e.g., Carnival + an unnamed second victim). The 8.7M is real but distributed across more than one organization; Carnival's 5,995,277 is the true Carnival-only figure. ShinyHunters retains authorship of the Carnival incident specifically."
        - id: H5
          statement: "Null / false-claim hypothesis: ShinyHunters opportunistically claimed credit for a Carnival incident they did not in fact execute; a different actor (or insider) was responsible. Carnival's silence on attribution is consistent with this reading. The 8.7M figure is fabricated to lend the claim weight."
        - id: H6
          statement: "Composite-actor: ShinyHunters claim is accurate on authorship but the operation involved a partner (e.g., LAPSUS$ Group EaaS infrastructure for the leak site, or an initial-access broker for the social-engineering vector); the 8.7M and 5,995,277 may differ because the actor counts include partner-staged data Carnival never knew was taken."

      evidence:
        - id: E1
          description: "Carnival self-discloses 5,995,277 affected customers in its own customer-notification filing (vendor self-statement is authoritative on procedural facts of own disclosure)"
          source: carnival-self-disclosure-via-bleepingcomputer
          digraph: A2
          weight: 3
        - id: E2
          description: "ShinyHunters April 2026 self-claim of 8.7M+ records and terabytes of corporate data (actor self-claim, threat-actor source)"
          source: shinyhunters-self-claim-via-bleepingcomputer
          digraph: C3
          weight: 1
        - id: E3
          description: "Carnival did NOT publicly confirm ShinyHunters attribution; BleepingComputer explicitly notes Carnival did not reply to confirm or deny ShinyHunters' claims"
          source: bleepingcomputer-2026-05-28
          digraph: A2
          weight: 3
        - id: E4
          description: "Two-month gap between ShinyHunters' April 2026 claim and Carnival's May 28 confirmation — actor named the victim publicly before victim disclosed"
          source: bleepingcomputer-2026-05-28
          digraph: B2
          weight: 2
        - id: E5
          description: "Carnival-confirmed initial-access vector is social-engineering of an employee account; 8-day dwell (2026-04-14 initial → 2026-04-22 exfil confirmed)"
          source: carnival-self-disclosure-via-bleepingcomputer
          digraph: A2
          weight: 3
        - id: E6
          description: "ShinyHunters 2026 operational pattern: corpus-anchored multi-victim Salesforce-customer-targeting (Charter 40M finding-2026-05-27-0006; BC-cited 'hundreds of companies worldwide'); Bling Libra TTP profile per Unit 42 (SaaS vishing + MFA-intercept + device registration) is operationally consistent with Carnival pattern"
          source: corpus-prior-findings-pattern
          digraph: A2
          weight: 3
        - id: E7
          description: "Threat-actor self-claims for extortion leverage have well-documented pattern of scope-inflation (corpus precedents: Charter 40M ShinyHunters claim; prior LockBit / ALPHV / Cl0p MOVEit cases)"
          source: corpus-prior-findings-pattern
          digraph: B2
          weight: 2
        - id: E8
          description: "Carnival's 5,995,277 figure is ~31% below the actor self-claim (8.7M) — a magnitude consistent with the inflation pattern in E7, not an order-of-magnitude divergence"
          source: arithmetic-derived
          digraph: A1
          weight: 3
        - id: E9
          description: "Carnival's notification specifies data categories (names / DOB / email / gender / location / loyalty) and explicitly EXCLUDES payment card / SSN / passport — narrow data scope is consistent with a single-application/system compromise rather than full enterprise exfil"
          source: carnival-self-disclosure-via-bleepingcomputer
          digraph: A2
          weight: 3
        - id: E10
          description: "Holland America Line / Mariner Society loyalty program is named — the affected data set indicates a loyalty-program-scoped repository compromise rather than enterprise-wide CRM"
          source: carnival-self-disclosure-via-bleepingcomputer
          digraph: A2
          weight: 3
        - id: E11
          description: "No A/B-grade IR firm has published independent attribution or telemetry on the Carnival incident specifically (Mandiant / MSTIC / CrowdStrike / Unit 42 / Recorded Future / Volexity silent in AM-28 window)"
          source: corpus-silence-2026-05-28
          digraph: A1
          weight: 3
        - id: E12
          description: "No SEC 8-K filing visible in AM-28 window; no class-action filings or state AG breach-notifications cross-referenced yet"
          source: corpus-silence-2026-05-28
          digraph: A1
          weight: 3
        - id: E13
          description: "Bling Libra (per Unit 42 finding-2026-05-28-0003 this cycle) reuses same Tox ID across victims and operates a Tor-based leak site — operationally consistent with a single actor claiming multiple victims rather than multi-actor confusion"
          source: unit42-2026-05-27
          digraph: A2
          weight: 3
        - id: E14
          description: "Per red-team carry-over from Charter (finding-2026-05-27-0006): the 'Salesforce-customer-targeting' tradecraft-class framing is BC editorial, NOT Carnival-confirmed; Carnival's own notification does NOT name Salesforce, Salesloft Drift, or Salesforce Aura"
          source: red-team-corpus-check-finding-2026-05-27-0006
          digraph: A2
          weight: 3

      matrix:
        E1:  {H1: C, H2: C, H3: I, H4: C, H5: C, H6: C}
        E2:  {H1: C, H2: C, H3: C, H4: C, H5: C, H6: C}
        E3:  {H1: N, H2: N, H3: N, H4: N, H5: C, H6: N}
        E4:  {H1: C, H2: C, H3: C, H4: C, H5: C, H6: C}
        E5:  {H1: C, H2: C, H3: C, H4: C, H5: N, H6: C}
        E6:  {H1: C, H2: C, H3: C, H4: C, H5: I, H6: C}
        E7:  {H1: C, H2: N, H3: I, H4: N, H5: C, H6: N}
        E8:  {H1: C, H2: N, H3: I, H4: C, H5: N, H6: N}
        E9:  {H1: C, H2: C, H3: I, H4: C, H5: N, H6: C}
        E10: {H1: C, H2: C, H3: I, H4: C, H5: N, H6: C}
        E11: {H1: N, H2: N, H3: N, H4: N, H5: N, H6: N}
        E12: {H1: N, H2: N, H3: N, H4: N, H5: N, H6: N}
        E13: {H1: C, H2: C, H3: C, H4: I, H5: I, H6: N}
        E14: {H1: C, H2: C, H3: C, H4: C, H5: C, H6: C}

      inconsistency_counts:
        H1: 0
        H2: 0
        H3: 5
        H4: 1
        H5: 3
        H6: 0

      diagnostic_evidence:
        - E1: "Strongly diagnostic against H3 — Carnival's own A-grade self-disclosure of 5,995,277 is the strongest evidence that the lower figure is the real Carnival count; under-counting hypothesis requires accusing Carnival of materially false regulatory disclosure"
        - E6: "Diagnostic against H5 (null/false-claim) — the corpus-anchored 2026 ShinyHunters multi-victim pattern (Charter, BC-cited 'hundreds of companies') makes opportunistic-false-claim less plausible; this actor has a documented operational footprint that fits Carnival"
        - E7: "Diagnostic for H1 against H3 — the corpus-anchored actor pattern of scope-inflation explains the ~31% gap as inflation; H3 (Carnival under-counts) is the harder claim to sustain absent specific evidence"
        - E8: "Diagnostic for H1 against H3 — ~31% delta is in the inflation-pattern range, not the magnitude that would indicate Carnival systematically under-counting"
        - E9: "Diagnostic against H3 — narrow data-category scope (no payment card / SSN / passport) is consistent with a bounded compromise; under-counting hypothesis would more typically accompany broader data-category exposure"
        - E10: "Diagnostic against H3 — loyalty-program scoping further bounds the compromise to a specific data repository, weakening the systematic-under-counting reading"
        - E13: "Diagnostic against H4 (multi-victim conflation) and H5 (false claim) — Bling Libra's same-Tox-ID-across-victims operational discipline argues against conflation/false-claim modes"

      ranking:
        - rank: 1
          hypothesis_id: H1
          rationale: "Zero inconsistencies. The strongest diagnostic evidence (E1, E7, E8, E9, E10) all align: Carnival's authoritative self-disclosure of the lower count is internally coherent with a bounded loyalty-program-scoped compromise; the ~31% delta to the actor claim is in the documented inflation-pattern range; and the corpus-anchored ShinyHunters 2026 operational tempo (E6) supports the authorship layer. This is the analyst's preferred reading."
          wep: very_likely
        - rank: 2
          hypothesis_id: H6
          rationale: "Zero inconsistencies but introduces a partner actor for which there is no direct evidence in the Carnival material. The Unit 42 Bling-Libra-+-LAPSUS$-EaaS framing in finding-0003 makes this hypothesis structurally available but no Carnival-specific evidence elevates it above H1. Cannot be ruled out; should be treated as a 'cannot eliminate' rather than 'most probable.'"
          wep: roughly_even_chance
        - rank: 3
          hypothesis_id: H2
          rationale: "Zero inconsistencies but the notification-eligible-subset reading is an unverified legal hypothesis without specific evidence (Carnival has not stated 8.7M total of which 5.995M notified; the notification language reads as a total-affected count, not a subset). Plausible but speculative."
          wep: unlikely
        - rank: 4
          hypothesis_id: H4
          rationale: "One inconsistency (E13 — Bling Libra operational discipline argues against conflation). Multi-victim-conflation is structurally available but ShinyHunters explicitly named Carnival in April 2026; the actor identified the victim, not just claimed a generic record-count."
          wep: unlikely
        - rank: 5
          hypothesis_id: H5
          rationale: "Three inconsistencies (E6, E13, plus general low support). Opportunistic false-claim is hardest to sustain because (a) corpus-anchored ShinyHunters 2026 operational footprint fits the Carnival pattern; (b) Bling Libra's same-Tox-ID discipline argues against false-claim mode; (c) two months elapsed between claim and confirmation without ShinyHunters retracting or another actor disputing."
          wep: very_unlikely
        - rank: 6
          hypothesis_id: H3
          rationale: "Five inconsistencies (E1, E7, E8, E9, E10). Systematic-under-counting requires accusing Carnival of materially false regulatory disclosure with no positive evidence to support it; ruled out absent specific contradiction from SEC 8-K, class-action discovery, or state AG investigation."
          wep: very_unlikely

      sensitivity_analysis:
        brittleness: medium
        load_bearing_evidence: [E1, E6, E11, E13]
        if_E1_carnival_disclosure_later_amended_upward: "H3 becomes viable; H1 ranking weakens; rerun ACH after amended notification"
        if_E6_corpus_pattern_challenged_by_red_team_carry_over: "If the Bling-Libra-as-coherent-actor-cluster framing collapses (per Charter red-team analogue), H1 weakens on the attribution layer and H5 strengthens; the scope reading (lower-figure-correct) survives independently"
        if_E11_ir_firm_publishes_attribution_to_different_actor: "H5 strengthens directly; H1 ranking can flip; immediate rerun required"
        if_E13_bling_libra_tox_id_discipline_proves_misattributed: "H4 strengthens (conflation viable); H1 weakens marginally"
        single_point_of_failure: "E1 (Carnival's self-disclosure) is the single most load-bearing piece for the scope-dispute layer. If Carnival's filing turns out to be amended upward in a later state-AG breach-notification or SEC 8-K, the entire H1 ranking on scope must be re-examined. The attribution layer has two single-points-of-failure: E6 (corpus pattern coherence) and E13 (Bling Libra operational discipline) — if either erodes, H5 viability increases."

      tripwires:
        - observation: "Carnival files SEC 8-K with materially higher affected-customer count than 5,995,277"
          effect: "H1 weakens on scope; H3 strengthens; rerun ACH with revised E1"
        - observation: "State AG breach-notification specifies different scope or data categories than Carnival's customer-notification"
          effect: "H2 (notification-eligible-subset) becomes testable; rerun ACH"
        - observation: "A different actor (not ShinyHunters) claims credit for Carnival incident; OR an A/B-grade IR firm publishes attribution to a different actor"
          effect: "H5 strengthens; H1 ranking can flip; immediate rerun"
        - observation: "ShinyHunters publishes Carnival data sample on Tor leak site with provable Carnival-source data and a record count ≥6M"
          effect: "H1 confirms; H3/H4 weaken"
        - observation: "Class-action filing surfaces discovery indicating systematic under-counting"
          effect: "H3 becomes plausible; H1 weakens"
        - observation: "Second 2026 ShinyHunters victim disclosed where actor-claim and victim-figure align closely (not the 31% gap pattern)"
          effect: "H3 becomes more plausible for Carnival specifically; pattern of inflation is less reliable"

      conclusion:
        summary: |
          On the scope dispute, the best-supported reading is H1: Carnival's
          5,995,277 figure is authoritative for the Carnival-scoped compromise;
          the ShinyHunters 8.7M+ self-claim is scope-inflation in the
          documented actor pattern (~31% delta is consistent with inflation,
          not order-of-magnitude divergence). The narrow data-category scope
          (no payment card / SSN / passport; loyalty-program-bounded) further
          supports a bounded compromise reading. On attribution, ShinyHunters
          self-claim stands as the sole sourced attribution; corpus-anchored
          2026 operational pattern (Charter parallel + Bling Libra TTP
          profile) makes H1 the most defensible reading, but H5 (opportunistic
          false-claim) cannot be definitively ruled out absent independent
          IR-firm attribution. The attribution layer therefore caps at
          "likely" — not "very likely" — even though the scope-dispute layer
          reaches "very likely."
        wep: likely
        wep_layered:
          scope_dispute_carnival_figure_authoritative: very_likely
          attribution_to_shinyhunters_per_self_claim_only: likely
          shinyhunters_as_coherent_operational_actor_cluster: likely
        confidence_caveats: |
          Hard Rule 2: Archimedes preserves the attribution layer as
          ShinyHunters self-claim only; we do NOT upgrade to victim-
          confirmed attribution. The brief should keep three layers
          separable: (1) breach occurred at Carnival per Carnival (very
          likely); (2) ShinyHunters claimed responsibility per their own
          April 2026 announcement (likely as actual authorship; very likely
          as the claim-of-responsibility procedural fact); (3) editorial
          Salesforce-pattern framing per BleepingComputer is NOT Carnival-
          confirmed and should not be collapsed into the prior two layers.
          Carry-forward from red-team review of finding-2026-05-27-0006:
          the tradecraft-class synthesis framing was downgraded yesterday
          for over-confidence; the same caution applies to Carnival.

  sat_kac:
    kac_analysis:
      assessment_under_review: >
        "The Carnival Corporation breach affected 5,995,277 customers per
        Carnival's own notification; ShinyHunters claimed responsibility in
        April 2026 with an inflated 8.7M figure; the actor cluster is the
        same as the Charter Communications 2026-05-27 incident (Bling Libra
        per Unit 42 alias)."
      analyzed_at: 2026-05-28T08:32:00-04:00
      analyzed_by: analyst
      invoking_context: >
        Pre-publication review for AM-28 morning brief. Grader explicitly
        flagged the "named victim" claim as the load-bearing assumption
        — Carnival is named by both BleepingComputer (as victim) and
        ShinyHunters (as victim of their April 2026 claim), but Carnival's
        own notification does NOT confirm ShinyHunters as the perpetrator.
        KAC interrogates the chain of inference from "Carnival is named"
        to "the breach is the actor-claimed breach."

      assumptions:
        - id: A1
          statement: "Carnival's customer-notification filing as relayed by BleepingComputer refers to the SAME incident ShinyHunters publicly claimed in April 2026 (and not a separate, unrelated Carnival incident)"
          category: semantic
          stated: false
          why_must_be_true: >
            The whole pairing of the actor self-claim with the victim self-
            disclosure depends on both parties describing the same event;
            if they describe different events, the 31%-gap scope dispute
            evaporates because the figures don't refer to the same population
          when_could_be_false: >
            Large enterprises sometimes have multiple security incidents in
            overlapping timeframes; ShinyHunters' April claim could
            theoretically reference a different (smaller, earlier, or
            partial) Carnival incident than what Carnival's notification
            describes
          evidence_for: [carnival-incident-timing-april-2026-matches-shinyhunters-april-2026-claim, bleepingcomputer-frames-as-same-incident, carnival-april-14-initial-access-april-22-exfil-aligns-with-shinyhunters-april-claim-window]
          evidence_against: []
          confidence: high
          centrality: critical
          classification: sound

        - id: A2
          statement: "Carnival's silence on attribution (neither confirming nor denying ShinyHunters) is best read as 'attribution is under investigation / legally sensitive' rather than as 'Carnival has evidence of a different perpetrator'"
          category: source_reliability
          stated: false
          why_must_be_true: >
            The attribution reading rests on treating Carnival's non-denial as
            non-disconfirming; if Carnival's silence actually masks a
            counter-attribution they're not yet ready to make, the analysis
            of ShinyHunters as responsible is premature
          when_could_be_false: >
            Carnival's notification may be holding back attribution because
            their own IR firm has attributed differently, or because an
            insider-threat reading is under investigation, or because law
            enforcement requested non-attribution during active operation
          evidence_for: [vendor-self-disclosure-conventional-practice-is-non-attribution-during-investigation, no-contradicting-attribution-from-ir-firm]
          evidence_against: [no-direct-evidence-on-what-carnival-internally-believes]
          confidence: medium
          centrality: material
          classification: qualify

        - id: A3
          statement: "The Bling Libra = ShinyHunters alias mapping (per Unit 42 finding-2026-05-28-0003 this cycle) is operationally reliable enough to treat Carnival as a 'Bling Libra cluster' victim for brief-framing and roster purposes"
          category: source_reliability
          stated: true
          why_must_be_true: >
            The cluster-mapping is what allows the brief to pair Carnival
            with Charter (finding-2026-05-27-0006) and with the broader
            Unit 42 trend-analysis (finding-0003 this cycle) as a coherent
            multi-victim signal rather than three independent incidents
          when_could_be_false: >
            Unit 42's cluster-naming taxonomy is canonical for Palo Alto's
            internal framework but second-vendor cross-verification on
            Bling Libra = ShinyHunters specifically is not yet in corpus;
            if a future Mandiant / MSTIC / CrowdStrike piece distinguishes
            Bling Libra from ShinyHunters as separate clusters, the cluster-
            mapping would need to be qualified
          evidence_for: [unit42-canonical-palo-alto-naming-finding-0003, corpus-internal-charter-corroboration-finding-2026-05-27-0006]
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify

        - id: A4
          statement: "The 'named victim' framing applies symmetrically — i.e., a victim that ShinyHunters publicly named in April 2026 AND that has now self-confirmed an incident in the same window can be treated as a confirmed Bling Libra victim for analytic purposes, even without Carnival affirming the attribution"
          category: TTP_patterns
          stated: false
          why_must_be_true: >
            The bridge from 'actor claims X; victim confirms incident' to
            'victim is a confirmed actor-cluster victim' relies on this
            symmetric reading; otherwise, only actor-confirmed-by-victim
            attributions would count, and the corpus would lose a large
            class of corroboration patterns
          when_could_be_false: >
            Some actor self-claims target victims the actor did not actually
            breach (opportunistic false-claim mode, especially when victims
            announce incidents publicly that an actor can then claim
            retrospectively); the symmetric reading collapses if actor
            self-claim is unreliable
          evidence_for: [corpus-anchored-shinyhunters-pattern-charter-charter-bling-libra-tox-id-discipline, two-month-gap-with-no-retraction-or-counter-claim]
          evidence_against: [hard-rule-2-preserves-attribution-as-actor-self-claim-only-not-victim-confirmed]
          confidence: medium
          centrality: critical
          classification: qualify

        - id: A5
          statement: "The 8-day dwell window (2026-04-14 → 2026-04-22) and the social-engineering-of-employee initial vector are corpus-consistent enough with Bling Libra's documented TTP (vishing + MFA-intercept + device-registration) to support the 'same actor cluster as Charter' framing"
          category: TTP_patterns
          stated: false
          why_must_be_true: >
            The pattern-matching from Carnival's disclosed vector to Bling
            Libra's TTP profile is what carries the actor-cluster framing
            beyond the bare self-claim layer
          when_could_be_false: >
            Carnival's notification says only 'social engineering of an
            employee' — it does NOT specify vishing vs phishing vs in-person
            social engineering; the underspecification opens space for the
            vector to be a non-Bling-Libra mechanism; the 8-day dwell is
            also generic and not Bling-Libra-distinctive
          evidence_for: [carnival-self-disclosed-social-engineering-vector-aligned-with-bling-libra-saas-vishing-profile-per-unit42]
          evidence_against: [carnival-notification-does-not-specify-channel-vishing-vs-phishing-vs-other, bling-libra-tox-id-and-device-registration-not-confirmed-in-carnival-disclosure]
          confidence: low
          centrality: material
          classification: qualify

        - id: A6
          statement: "Per Hard Rule 2, Archimedes does NOT originate the 'Carnival is a Bling Libra victim' claim — the claim is sourced to ShinyHunters' own April 2026 self-claim, with Bling Libra being the Unit 42 canonical alias for ShinyHunters"
          category: source_reliability
          stated: true
          why_must_be_true: >
            The whole publication framing depends on this — Archimedes can
            report 'ShinyHunters claimed Carnival; ShinyHunters = Bling
            Libra per Unit 42' without violating Rule 2 because the
            attribution chain is sourced at every step
          when_could_be_false: >
            If Archimedes drifts to language like 'Bling Libra breached
            Carnival' (rather than 'Bling Libra is the Unit 42 alias for
            ShinyHunters, who claimed responsibility for the Carnival
            incident'), the framing crosses from preserved-attribution to
            originated-attribution
          evidence_for: [hard-rule-2-explicit-in-charter, finding-0003-codifies-the-alias-mapping]
          evidence_against: []
          confidence: high
          centrality: critical
          classification: sound

        - id: A7
          statement: "The BleepingComputer editorial Salesforce-customer-targeting framing (Salesforce Aura, Salesloft Drift) is reportable as 'BC editorial framing' but does NOT constitute Carnival-attested evidence and therefore does not load-bear the actor-cluster assessment"
          category: source_reliability
          stated: true
          why_must_be_true: >
            The grader explicitly separated the BC editorial layer from
            the Carnival-attested layer; the analyst-level framing must
            preserve this separation or the published brief will conflate
            BC editorial with victim attestation
          when_could_be_false: >
            Could only be false if Carnival later confirms Salesforce
            implication — which would lift the BC framing from editorial
            to confirmed; until then, the separation holds
          evidence_for: [carnival-notification-omits-salesforce-explicitly-per-bc-relay, grader-explicit-separation-of-bc-editorial-vs-carnival-attested]
          evidence_against: []
          confidence: high
          centrality: material
          classification: sound

        - id: A8
          statement: "Carnival's customer-notification filing language as relayed by BleepingComputer is substantively accurate — BC has not materially mis-relayed or mis-quoted the Carnival statement"
          category: source_reliability
          stated: false
          why_must_be_true: >
            Archimedes does not have the Carnival filing directly; the
            entire chain rests on BC's accurate relay; if BC has trimmed
            or paraphrased critical context the analysis may be off
          when_could_be_false: >
            BleepingComputer is B-grade per source-grades.yaml; B-grade
            sources sometimes editorialize / trim / re-frame; a direct
            read of Carnival's notification could surface attribution
            language BC omitted
          evidence_for: [bleepingcomputer-track-record-on-relay-accuracy-corpus-baseline, byline-sergiu-gatlan-known-relay-accuracy]
          evidence_against: [no-direct-archimedes-retrieval-of-carnival-filing]
          confidence: medium
          centrality: material
          classification: qualify

      classifications_summary:
        sound: 3
        qualify: 5
        test: 0
        reject: 0

      remediation:
        status: proceed
        qualifying_caveats:
          - "A2 — Brief should note 'Carnival has not publicly affirmed or denied ShinyHunters attribution' rather than implying Carnival silence = Carnival confirmation"
          - "A3 — Brief should attribute Bling Libra cluster-mapping to Unit 42 specifically; if a second-vendor analysis distinguishes Bling Libra from ShinyHunters, the cluster mapping needs revisiting"
          - "A4 — Brief language must preserve the actor-self-claim layer separately from the victim-confirmation layer (Hard Rule 2 alignment); 'ShinyHunters claimed responsibility for Carnival in April 2026; Carnival now confirms a breach but has not affirmed the attribution'"
          - "A5 — Brief should not over-fit the social-engineering vector to Bling Libra's specific vishing-+-MFA-intercept TTP; Carnival's notification underspecifies the channel"
          - "A8 — Brief should note source provenance: 'per BleepingComputer relay of Carnival's notification' rather than 'per Carnival' directly, until Archimedes can retrieve the filing"
        recommended_brief_language: >
          "Carnival Corporation confirmed a breach affecting 5,995,277 customers in
          a customer-notification filing relayed by BleepingComputer on 2026-05-28.
          Initial unauthorized activity was detected 2026-04-14 with data theft
          confirmed 2026-04-22 (an 8-day dwell), through social engineering of an
          employee account. The ShinyHunters extortion gang claimed responsibility
          in April 2026 alleging 8.7M+ records — approximately 31% above Carnival's
          confirmed figure, consistent with documented actor-side scope-inflation
          patterns. Carnival has NOT publicly affirmed or denied the ShinyHunters
          attribution. Unit 42 (yesterday) codified Bling Libra as the Palo Alto
          canonical alias for ShinyHunters; the actor cluster is operationally
          consistent with the Charter Communications confirmation 24h earlier.
          BleepingComputer's editorial framing situates the incident within the
          broader Salesforce-customer-targeting pattern, but Carnival's own
          notification does not name Salesforce or any third-party SaaS — that
          framing is BC editorial, not victim-attested."

      recommended_wep_after_kac:
        breach_occurred_at_carnival_per_carnival: very_likely
        scope_5_995_277_per_carnival: very_likely
        shinyhunters_claimed_responsibility_per_actor: very_likely
        shinyhunters_actually_responsible: likely
        bling_libra_as_unified_actor_cluster_per_unit42: likely
        salesforce_implication_per_bc_editorial: roughly_even_chance
        carnival_is_charter_class_same_tradecraft_incident: roughly_even_chance

red_team_review_required: false
red_team_review_rationale: >
  WEP ceiling on the breach-occurred layer is "very_likely" but this is
  the SAME claim-class as finding-2026-05-27-0006 (Charter / 40M /
  ShinyHunters) which DID undergo red-team review yesterday. The
  red-team's challenges to the Charter cluster — tradecraft-class
  framing on Salesforce-Entra-vishing, scope-claim dispute — apply
  in principle to Carnival as well, and the analyst-side SAT-ACH
  topics above pre-load those questions for the analyst phase. Re-
  running red-team on Carnival specifically would yield the same
  contrarian set (scope-inflation challenge, attribution-by-self-claim-
  only challenge, editorial-framing challenge). The grader judges
  these are sufficiently anchored by the Charter precedent that a
  separate red-team pass on Carnival is not required. If the
  ShinyHunters 2026 campaign expands beyond multi-victim consumer
  breach to include an A&D-prime named victim, red_team_review
  should be triggered at that point.
red_team_review: null

# Lifecycle
tlp: CLEAR
published_in_briefs:
  - 2026-05-28-morning
retracted: false
retraction_brief_id: null
---

# Carnival Corporation confirms 5,995,277-customer breach following ShinyHunters April 2026 extortion claim — Holland America Line / Mariner Society loyalty program — social-engineering-of-employee initial vector — 8-day dwell — no payment card / SSN / passport in scope — Carnival does NOT confirm ShinyHunters attribution

## Summary

Carnival Corporation's customer-notification filing confirms 5,995,277
customers affected by a breach traced to social-engineering compromise
of an employee account, with initial unauthorized activity 2026-04-14
and data exfiltration confirmed 2026-04-22 — an 8-day dwell window.
Affected data categories are limited to names, dates of birth, emails,
genders, geographic locations, and Mariner Society loyalty program
details (Holland America Line subsidiary); payment cards, SSNs, and
passports are explicitly out of scope. The ShinyHunters extortion gang
self-claimed responsibility in April 2026 alleging 8.7M+ records — a
figure ~31% above the confirmed count, consistent with corpus-anchored
actor-side scope-inflation patterns. Carnival has NOT publicly
confirmed the ShinyHunters attribution. BleepingComputer's editorial
framing situates the incident within the broader ShinyHunters /
Salesforce-customer-targeting pattern (Salesforce Aura, Salesloft
Drift), but Carnival's own notification does NOT confirm Salesforce
implication — that framing is BC editorial, not victim-attested. Per
Hard Rule 2, the attribution layer is preserved as actor self-claim
only.

## Sources

### BleepingComputer (bleepingcomputer, digraph: B)

- URL: https://www.bleepingcomputer.com/news/security/carnival-cruise-confirms-data-breach-affecting-nearly-6-million-people/
- Published: 2026-05-28T10:49:27+00:00 (06:49 EDT — in-window)
- Author: Sergiu Gatlan
- Key claim: Carnival Corporation's customer-notification filing
  confirms 5,995,277 affected customers from a social-engineering-
  initiated breach traced to April 2026; ShinyHunters self-claimed
  responsibility in April 2026 with an inflated 8.7M+ self-claim;
  Carnival has not publicly confirmed the ShinyHunters attribution.

### Carnival Corporation customer-notification filing (vendor self-disclosure, digraph: A on own facts)

- Notification published / filed: 2026-05-28 (timing per BleepingComputer relay)
- Direct text NOT directly retrieved by Archimedes; relayed via
  BleepingComputer.
- Key claim: Carnival self-confirms (1) incident occurred, (2) initial
  unauthorized activity 2026-04-14, (3) data theft confirmed
  2026-04-22, (4) social engineering of employee account as initial-
  access vector, (5) 5,995,277 affected customers, (6) data categories
  limited to names/DOBs/emails/genders/locations/loyalty-details, (7)
  explicitly NO payment card / SSN / passport.

### ShinyHunters April 2026 self-claim (threat-actor self-claim, digraph: C — actor self-claim)

- Original criminal-forum post NOT directly retrieved by Archimedes;
  context relayed via BleepingComputer body.
- Self-claim contribution: Alleged 8.7M+ records and terabytes of
  corporate data exfiltrated. Scope ~31% above Carnival's confirmed
  figure — consistent with actor-side scope-inflation pattern.

## Technical detail

### Confirmed incident parameters (per Carnival self-disclosure via BleepingComputer)

- **Victim:** Carnival Corporation, world's largest cruise line
  operator. Holland America Line is the named operating subsidiary
  impacted; Mariner Society loyalty program references appear in the
  affected data set.
- **Affected count:** 5,995,277 customers (rounded "nearly 6 million"
  in BC headline). Confirmed by victim's own customer-notification
  filing.
- **Initial-access vector:** Social engineering of employee account.
  Verbatim per Carnival notification (under 15 words): "an unauthorized
  actor used social engineering to deceive an employee to gain access."
- **Incident timeline:** 2026-04-14 initial unauthorized activity
  detected; 2026-04-22 data theft confirmed; 2026-05-28 customer
  notification + public confirmation.
- **Affected data categories:** names, dates of birth, email
  addresses, genders, geographic locations, Mariner Society / Holland
  America Line loyalty program details.
- **Explicitly excluded data:** No payment-card data, no Social
  Security numbers, no passport numbers per Carnival's notification.

### Attribution layer (preserved per Hard Rule 2)

- **Procedural fact (confirmed):** A breach occurred at Carnival
  Corporation affecting 5,995,277 customers. (Source: Carnival self-
  disclosure.)
- **Attribution claim (self-claim, NOT victim-confirmed):**
  ShinyHunters extortion gang claimed responsibility in April 2026.
  (Source: ShinyHunters self-claim via BleepingComputer relay.)
- **BleepingComputer editorial framing (NOT victim-attested):**
  Carnival situated within the broader ShinyHunters / Salesforce-
  customer-targeting pattern via Salesforce Aura and Salesloft Drift
  campaign lineage. Carnival's own notification does NOT name
  Salesforce or any third-party SaaS in the disclosure.

### Cluster context: Bling Libra = ShinyHunters (Unit 42 canonical)

Today's Unit 42 "Out of the Crypt" piece (finding-2026-05-28-0003
this same cycle) formally codifies the **Bling Libra = ShinyHunters**
alias mapping in Archimedes corpus for the first time. The Bling Libra
TTP profile per Unit 42 (SaaS-focused vishing, phishing sites
designed to intercept credentials and MFA codes, device registration
for persistence, reuses same Tox ID across victims, Tor-based data
leak site) is operationally consistent with the Carnival incident
pattern (social engineering of employee account, multi-day dwell,
broad customer-data exfil). Per Hard Rule 2, Archimedes does NOT
originate the "Carnival is a Bling Libra victim" mapping — the
mapping is corpus-grade for Bling Libra = ShinyHunters as a name,
and ShinyHunters has self-claimed Carnival; the actor-cluster name
substitution follows the actor's own claim, not new Archimedes
attribution.

### Cross-corpus parallel: Charter Communications 40M (finding-2026-05-27-0006)

The Carnival confirmation today is the **second 2026 ShinyHunters
confirmed victim** in Archimedes corpus, following finding-2026-05-27-
0006 (Charter Communications / Spectrum confirmation of breach
following ShinyHunters extortion claim, 40M records). Pattern signal
strengthens: multi-victim 2026 ShinyHunters extortion campaign across
consumer-sector enterprises (telecom + cruise/hospitality) with
broader "hundreds of companies worldwide" framing per BC. The Bling
Libra cluster mapping (Unit 42 today) provides the analytic anchor
for treating these as a single actor-cluster operational pattern
rather than independent incidents.

## IOCs surfaced

| Type | Value | Confidence | Source |
|------|-------|-----------|--------|
| Tradecraft pattern | Social engineering of employee account → IT-system access → 8-day dwell → customer-records exfil | High | Carnival self-disclosure via BC |
| Victim org | Carnival Corporation (Holland America Line / Mariner Society) | High | Carnival self-disclosure |
| Actor self-claim | ShinyHunters: 8.7M+ records and terabytes of corporate data (April 2026) | Medium | ShinyHunters via BC relay |
| Data categories | Names, DOBs, emails, genders, locations, loyalty details | High | Carnival self-disclosure |
| Excluded categories | No payment card / SSN / passport per Carnival | High | Carnival self-disclosure |
| Editorial framing (NOT victim-confirmed) | Salesforce Aura + Salesloft Drift campaign lineage | Low | BC editorial framing |

No domains, IPs, hashes, or file artifacts surfaced in this relay.
Pattern-level IOC family (Salesforce-customer-targeting + social-
engineering-employee-vector) is corpus-anchored across multiple 2026
ShinyHunters victims.

## Relationship to existing findings

- **finding-2026-05-27-0006-bleepingcomputer-charter-shinyhunters-40m-records-salesforce-entra-vishing-victim-confirmation** — DIRECT corpus parallel. Same actor cluster (ShinyHunters / Bling Libra), distinct victim (Carnival 6M vs Charter 40M), both consumer-sector breaches confirmed within 24h of each other, both BC editorial framing tied to broader Salesforce-targeting pattern. Pattern signal: multi-victim 2026 ShinyHunters extortion campaign.
- **finding-2026-05-28-0003-unit42-out-of-the-crypt-extortion-economy-tgr-cri-1135-teampcp-bling-libra-hazy-scorpius-cl-cri-1116-blackfile-redact** (this cycle) — Unit 42 formally codifies Bling Libra = ShinyHunters alias mapping. Carnival is the named-victim corroboration data-point for the Unit 42 cluster-mapping framework.

## Open questions for analyst

1. **/new-actor scaffolding decision for ShinyHunters (alias Bling Libra per Unit 42).** Carnival is the second confirmed 2026 victim under the same operational pattern. Multi-victim corpus signal is strengthening. Operator decision flag carries forward from finding-2026-05-27-0006.
2. **SAT-ACH on the 8.7M-vs-5.995M scope dispute** — competing hypotheses on whether the actor inflated, the victim under-counted, the figures reference different population subsets, or the actor's claim conflated multiple victims.
3. **Hard Rule 2 attribution-preservation framing for the morning brief** — keep the procedural fact (breach occurred per Carnival), the attribution claim (ShinyHunters self-claim), and the editorial pattern context (BC's Salesforce framing) as separable layers; do not collapse them into a single "ShinyHunters used Salesforce vishing to breach Carnival" statement that exceeds what is confirmed.
4. **Cross-link to AM-003 Unit 42 Out of the Crypt** — Carnival is the corpus-internal corroboration data-point for the Bling Libra cluster-mapping framework Unit 42 publishes today; the AM-28 brief should pair the two findings (Carnival as victim case + Unit 42 trend-analysis as cluster framework).

## Analytic notes (from analyst review)

ACH (6 hypotheses, 14 evidence items) ranks H1 first: Carnival's 5,995,277
figure is authoritative; ShinyHunters' 8.7M+ is scope-inflation in the
documented actor pattern (~31% delta sits in the inflation band, not the
order-of-magnitude divergence that would point to systematic under-counting).
Narrow data scope (no payment card / SSN / passport; loyalty-program
bounded) and Carnival's authoritative self-disclosure together produce five
inconsistencies against the under-counting hypothesis (H3). The
opportunistic-false-claim hypothesis (H5) cannot be definitively ruled out
absent independent IR-firm attribution, but Bling Libra's same-Tox-ID-across-
victims operational discipline (per Unit 42 finding-0003 this cycle) argues
against it.

KAC surfaces eight load-bearing assumptions; five are qualify-class, three
sound. The riskiest are A4 (treating actor-claim + victim-confirmation as
symmetric corroboration) and A5 (pattern-matching Carnival's underspecified
"social engineering of an employee" to Bling Libra's specific vishing+MFA-
intercept TTP). Neither rises to test-class — but both demand explicit
qualifying language in the brief.

Recommendation: the brief should split into three separable layers — breach
occurred at Carnival (very likely), ShinyHunters claimed responsibility
(very likely as a procedural fact of the claim; likely on actual authorship),
and BleepingComputer's Salesforce-pattern editorial framing (NOT Carnival-
attested). The scope-dispute layer reaches "very likely" on H1; the
attribution layer caps at "likely" per single-source-veto on actor-self-
claim. Pair with finding-0003 (Unit 42 Out of the Crypt) for cluster
context; preserve Hard Rule 2 by sourcing the alias mapping to Unit 42 and
the authorship claim to ShinyHunters.
