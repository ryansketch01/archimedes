---
finding_id: finding-2026-06-10-0017-krebs-check-point-intel471-flashpoint-the-gentlemen-raas-osint-de-anonymization-hastalamuerte-zeta88-alexander-yapaev-izhevsk-russia-new-actor-candidate
created_at: 2026-06-10T16:28:00-04:00
graded_by: grader
grading_run_id: afternoon-20260610-160000
grading_mode: scheduled_brief
test: false
status: graded

# Core grading (admiralty-grading skill output)
digraph: B2
digraph_layered:
  the_gentlemen_ransomware_group_exists_as_second_most_active_2026_by_victim_count: B2    # Krebs primary; Check Point sustained-coverage corroboration
  the_gentlemen_332_victims_published_since_inception_240_plus_in_2026: B2                # Check Point primary via Krebs relay
  the_gentlemen_raas_model_90_10_affiliate_split: B2                                       # Check Point primary via Krebs
  the_gentlemen_aggressive_affiliate_recruitment_from_competing_programs: B2                # Check Point editorial framing via Krebs
  initial_access_vector_internet_facing_devices_vpns_firewalls: B2                          # Check Point primary via Krebs
  operational_velocity_encrypt_entire_networks_within_hours: B2                              # Krebs verbatim attribution
  hastalamuerte_zeta88_administrator_role_assembles_locker_raas_panel_payments_10_percent: B2  # Check Point + Intel 471 corroboration via Krebs
  intel471_forum_registration_trace_hastalamuerte_2019_to_present: B2                          # Intel 471 primary via Krebs
  hastalamuerte_breachforums_january_2025_izhevsk_ip: B2                                       # Intel 471 primary via Krebs
  zeta88_breached_august_2022_different_izhevsk_ip: B2                                          # Intel 471 primary via Krebs
  osint_pivot_chain_email_telegram_github_phone_apple_account: B3                              # Krebs OSINT breadcrumbs methodology; multiple intermediate pivots; not LE-confirmed
  identity_claim_alexander_andreevich_yapaev_36_year_old_izhevsk_udmurt_republic: B3            # Krebs OSINT breadcrumbs final-pivot identification; subject did not respond to comment requests
  yapaev_linkedin_uralenergo_udmurtia_b2b_marketing_head: B3                                    # Krebs OSINT layer; per-source-reported only
  hard_rule_2_preserve_per_source_attribution_framing_not_archimedes_confirmed: B1               # Self-evident procedural compliance
  the_gentlemen_not_in_archimedes_roster_new_actor_candidate: B1                                 # Verifiable absence
  no_a_d_prime_named_victim_in_krebs_piece: B1                                                   # Verifiable absence
  ad_prime_structural_relevance_via_internet_facing_vpn_firewall_initial_access_and_hours_to_encryption_velocity: C2  # Grader-side structural inference per A&D defender lens
  cluster_anchor: B2

digraph_anchor: >
  Cluster anchored on ONE B-grade media primary (Krebs on
  Security 2026-06-10T14:03:44 UTC) integrating A-grade vendor
  research from Check Point Software (sustained coverage of
  The Gentlemen) + Intel 471 (forum-registration trace) +
  Flashpoint (Krebs's disclosed advertiser) + Constella
  Intelligence (pivot chain) + KELA (additional surface) +
  Epieos (email-pivot tool). Multi-source OSINT chain
  characteristic of Krebs's "Breadcrumbs" methodology —
  reportable but expressly NOT LE-confirmed.

  B2 (not B1, not A2) anchored because:

    - SOURCE LETTER GRADE: One B-grade media primary (Krebs)
      integrating multiple A-grade vendor inputs. Vendor
      primaries (Check Point, Intel 471, Flashpoint,
      Constella, KELA) not directly retrieved this sweep —
      Krebs is the synthesizing surface. Cluster letter
      holds at B under conservative single-primary
      aggregation when the vendor-research primaries are
      surfaced via the Krebs integrating layer.

    - INDEPENDENCE TEST: Krebs's piece integrates multiple
      independent vendor inputs (Check Point + Intel 471
      + Flashpoint + Constella + KELA + Epieos), each with
      separate evidence basis (Check Point sustained
      research, Intel 471 forum-registration trace,
      Flashpoint Telegram ID, Constella pivot tooling).
      Independence holds robustly at the vendor-input
      tier; Krebs is the integrating surface.

    - CREDIBILITY: Walk the checklist.
      * Grade 1 (Confirmed): Procedural facts (group
        existence, 332 victim count, 90/10 RaaS model,
        forum-registration timeline) approach Confirmed
        via Check Point + Intel 471 independent
        corroboration. However the OSINT identity-chain
        layer (Hastalamuerte/Zeta88 → Alexander Yapaev)
        is Krebs's "Breadcrumbs" methodology — not LE-
        confirmed; subject did not respond to comment
        requests. Cluster anchor holds at B2.
      * Grade 2 (Probably True) PASSES: consistent with
        established RaaS ecosystem patterns; technical
        claims internally coherent (internet-facing
        VPN/firewall initial access + hours-to-encryption
        velocity is canonical RaaS playbook); no
        contradicting source.

    - SUBSTANTIVE CLAIM LAYERS:
      * Group existence + RaaS model + victim count +
        operational velocity + initial-access vector:
        B2 — Krebs + Check Point + Intel 471 multi-source.
      * Administrator role of Hastalamuerte/Zeta88
        (assembles locker, RaaS panel, payments, 10%
        share): B2 — Check Point + Intel 471 corroboration.
      * Forum-registration trace 2019 → present (Exploit,
        Breachforums, Ramp_V2, BHF, Raidforums, Nulled,
        Codeby): B2 — Intel 471 primary via Krebs.
      * OSINT identity-pivot chain → Alexander Yapaev,
        36-year-old, Izhevsk: B3 — Krebs Breadcrumbs
        methodology; multiple pivots (email, Telegram,
        GitHub, Apple-account-via-Epieos, phone,
        Constella pivots); per-source-reported only; NOT
        Archimedes-confirmed.
      * Yapaev LinkedIn → "head of B2B marketing at
        Uralenergo Udmurtia": B3 — single-source OSINT
        layer; Hard Rule 2 preserve per-source-reported
        framing strict.
      * No A&D-prime named victim: B1 — verifiable
        absence.
      * A&D-prime structural relevance via internet-facing
        VPN/firewall + hours-to-encryption velocity: C2 —
        grader-side structural inference.

  Single-source veto APPLIED on:
    - OSINT identity-chain final identification (Yapaev /
      Izhevsk / Uralenergo). Krebs Breadcrumbs methodology;
      not LE-confirmed; subject denial-or-confirmation
      unknown; WEP capped at "likely" on identity layer
      and "report per Krebs" framing strict.

  Single-source veto NOT applied on:
    - Group-existence + RaaS-model + victim-count
      operational facts (Check Point + Intel 471
      independent corroboration).
    - Administrator-role assignment of Hastalamuerte/Zeta88
      (Check Point + Intel 471 corroboration on the
      role-claim layer specifically).

source_reliability:
  cluster_anchor_grade: B
  sources:
    - source_yaml_id: krebs
      grade: B
      provisional: false
      role: "Primary integrating layer (Brian Krebs byline) of multi-source OSINT de-anonymization analysis on The Gentlemen RaaS"
    - source_yaml_id: check-point
      grade: A
      provisional: true
      provisional_proposed_addition: true
      role: "Originating research (sustained coverage of The Gentlemen); first Archimedes-corpus dedicated-id surface; A-provisional under Tier-1 vendor-research precedent"
    - source_yaml_id: intel471
      grade: A
      provisional: true
      provisional_proposed_addition: true
      role: "Cybercrime-forum monitoring research (forum-registration trace 2019 → present); first Archimedes-corpus dedicated-id surface; A-provisional under Tier-1 vendor-research precedent"
    - source_yaml_id: flashpoint
      grade: A
      provisional: true
      provisional_proposed_addition: true
      role: "Telegram-ID pivot research (Krebs's disclosed advertiser; disclosure noted in Krebs piece); first Archimedes-corpus dedicated-id surface"
    - source_yaml_id: constella
      grade: A
      provisional: true
      provisional_proposed_addition: true
      role: "OSINT pivot tooling research (Telegram-ID-to-phone pivots); first Archimedes-corpus dedicated-id surface"
    - source_yaml_id: ke-la
      grade: A
      provisional: true
      provisional_proposed_addition: true
      role: "Additional OSINT surface; first Archimedes-corpus dedicated-id surface"
    - source_yaml_id: epieos
      grade: B
      provisional: true
      provisional_proposed_addition: true
      role: "Email-pivot OSINT tool (used in Krebs's identity chain); first Archimedes-corpus dedicated-id surface; provisional B per Tier-2 OSINT-tool precedent"
  grade_rationale: >
    Cluster letter grade holds at B under Krebs as integrating
    primary. Vendor-research primaries (Check Point, Intel 471,
    Flashpoint, Constella, KELA, Epieos) not directly retrieved
    this sweep. Multiple source-grades.yaml additions
    recommended at A provisional (Check Point, Intel 471,
    Flashpoint, Constella, KELA) and B provisional (Epieos).
  provisional: false

credibility:
  grade: 2
  checklist_passed:
    - probably_true_consistent_with_established_raas_ecosystem_patterns_lockbit_blackcat_scattered_spider_press_relations_cadence
    - probably_true_no_contradicting_a_b_source
    - probably_true_technical_claims_internally_coherent_internet_facing_vpn_firewall_initial_access_hours_to_encryption_canonical_raas_playbook
  rationale: >
    Group existence + RaaS model + operational velocity claims
    are consistent with established LockBit / BlackCat /
    Scattered Spider / Cl0p press-relations and operational
    cadence (canonical RaaS playbook). Forum-registration
    trace methodology is consistent with Intel 471's
    established cybercrime-forum monitoring practice. No
    contradicting source. OSINT identity-chain layer is
    Krebs Breadcrumbs methodology — reportable as per-source
    per Hard Rule 2 framing.

corroboration:
  independent_sources:
    - krebs
    - check-point
    - intel471
    - flashpoint
    - constella
    - ke-la
    - epieos
  independent: true
  test_passed: >
    Multiple independent vendor inputs each with separate
    evidence basis. Check Point has sustained primary
    research on The Gentlemen (separate research program).
    Intel 471 has cybercrime-forum monitoring telemetry
    (separate evidence basis). Flashpoint has Telegram-ID
    pivot data (separate). Constella has OSINT-pivot
    tooling (separate). KELA has additional surface.
    Epieos is email-pivot tool. Independence holds
    robustly at vendor-input tier; Krebs is integrating
    surface.

first_party_precedence:
  applied: false
  splunk_evidence: >
    No infrastructure IPs published in Krebs piece (no
    IPv4, no domains, no hashes). Identity-related
    selectors (emails, Telegram usernames, phone) are
    actor-administrator identifiers, not infrastructure
    IOCs queryable against archimedes / defenseclaw_local
    indices. No first-party hunt actionable at this sweep.

single_source_veto_applied: true
single_source_veto_layers:
  - osint_identity_chain_final_identification_yapaev_izhevsk_uralenergo_krebs_breadcrumbs_methodology_not_le_confirmed
  - yapaev_linkedin_uralenergo_udmurtia_b2b_marketing_head_single_source_osint_layer
wep_ceiling: likely

inclusion:
  eligible_for:
    - daily_brief_action
    - weekly_synthesis
    - other_signal_cybercriminal_watch
    - new_actor_candidate_referral

# Cluster metadata
cluster:
  topic: "Krebs OSINT de-anonymization of The Gentlemen RaaS administrator — Hastalamuerte / Zeta88 → Alexander Andreevich Yapaev (36, Izhevsk, Udmurt Republic, Russia) per Krebs Breadcrumbs methodology integrating Check Point + Intel 471 + Flashpoint + Constella + KELA + Epieos. The Gentlemen is second most active ransomware group in 2026 by victim count (332 victims total since mid-2025 inception, 240+ in 2026), runs aggressive 90/10 affiliate split RaaS model, targets internet-facing VPN/firewall devices for initial access, encrypts entire networks within hours. NOT in Archimedes roster — /new-actor candidate. Yapaev did not respond to comment requests; subject denial-or-confirmation unknown."
  cluster_size: 1
  raw_signal_members:
    - raw-2026-06-10-pm-011
  attribution_claims:
    - claimed_actor: "The Gentlemen RaaS administrator Hastalamuerte/Zeta88 identified as Alexander Andreevich Yapaev (36, Izhevsk, Udmurt Republic, Russia)"
      claimed_by_sources: [krebs, check-point, intel471, flashpoint, constella, ke-la, epieos]
      requires_analyst_review: true
      hard_rule_2_compliance: "Per-source attribution framing preserved verbatim — Krebs Breadcrumbs methodology OSINT chain; NOT LE-confirmed; subject did not respond to comment requests. Do NOT propagate as Archimedes-confirmed."

# Downstream handoff flags
analyst_review_required: true
analyst_review_complete: true
analyst_review_run_id: analyst-20260610-165500
red_team_review_required: false
red_team_review: null

# Analyst-driven WEP-layer adjustments (per SAT-ACH refutation discipline)
wep_layer_adjustments:
  - layer: group_existence_raas_model_victim_count_operational_velocity_initial_access_vector
    before: likely
    after: likely
    reason: "Holds; Check Point + Intel 471 independent corroboration on the operational layer. Per KAC A4 victim counts framed as leak-site-published, standard CTI practice."
  - layer: administrator_role_attribution_to_hastalamuerte_zeta88_persona
    before: likely
    after: likely
    reason: "Holds; Check Point + Intel 471 corroboration robust at vendor-research methodology level (KAC A3). Persona-to-role mapping is vendor-research-based, not LE-confirmed; brief must preserve per-source framing."
  - layer: osint_identity_chain_persona_to_yapaev_krebs_breadcrumbs
    before: likely
    after: likely
    reason: "ACH H1 (Yapaev IS the administrator) leads at zero inconsistencies with strong diagnostic evidence (E7 Codeby literal-name 2019 registration; E15 7-year persona history; E4/E5 Telegram-ID + phone pivots). H2 (unrelated person) ruled out at 6 inconsistencies. KAC A1 brittleness via Breadcrumbs chained-error-rate flagged as qualify. Brief must preserve 'per Krebs / per the cited sources, not LE-confirmed' verbatim. Hard Rule 2 strict: Archimedes does NOT originate the attribution — pressure-tests the sourced claim."
  - layer: yapaev_linkedin_uralenergo_udmurtia_b2b_marketing_head_single_source_layer
    before: likely
    after: roughly_even_chance
    reason: "Single-source OSINT layer with no independent corroboration on the employer-role-attribution specifically. Identity-layer is robust; employer-role-attribution at LinkedIn is the weakest sub-layer."

# Briefer Hard-Rule-2-discipline alert
briefer_framing_requirements:
  - requirement: "Preserve 'per Krebs / per the cited sources, not LE-confirmed' verbatim on the identity-chain layer"
    rationale: "Hard Rule 2 — Archimedes does NOT originate identity attribution. ACH validates the sourced claim but does NOT upgrade it to Archimedes-confirmed."
  - requirement: "Do NOT use passive-voice de-attribution ('has been identified as ...' / 'has been linked to ...') without preserving the per-source citation"
    rationale: "KAC A9 — Hard Rule 2 compliance is briefer-drafting-discipline-dependent. The passive-voice pattern silently violates."
  - requirement: "Frame TTP-pattern A&D-prime defender takeaways as 'reinforces canonical defender priorities' rather than 'requires new defender actions specific to The Gentlemen'"
    rationale: "KAC A10 — defender takeaways are valuable but apply broadly across the RaaS ecosystem; The Gentlemen attribution does not add unique defender actions beyond what the canonical RaaS playbook already implies."
  - requirement: "Preserve Krebs's Flashpoint advertiser disclosure if quoting/paraphrasing Flashpoint-derived content"
    rationale: "KAC A8 — standard analyst-paid-advertising-disclosure protocol."
  - requirement: "Report subject silence verbatim ('did not respond to multiple requests for comment') WITHOUT inferring either confirmation or denial"
    rationale: "KAC A7 — subject silence is non-diagnostic; do not propagate either inference direction."
  - requirement: "OFAC sanctions consideration is explicitly OUT OF SCOPE — the OSINT chain is reportable but does NOT constitute the evidentiary threshold for sanctions designation"
    rationale: "ACH conclusion caveat (4) — that's an LE / Treasury process, not an Archimedes process."
analysis_sections:
  sat_ach:
    ach_analysis:
      question: "Is the OSINT identity chain Hastalamuerte/Zeta88 → Alexander Andreevich Yapaev (36, Izhevsk, Udmurt Republic) — as published by Krebs per Breadcrumbs methodology integrating Check Point + Intel 471 + Flashpoint + Constella + KELA + Epieos — most likely (a) correct attribution of the administrator to Yapaev, (b) genuine identity-chain hits driven by infrastructure overlap with an unrelated person who happens to share selectors, (c) deliberate identity-seeding by the administrator (or a third party) intended to misdirect investigators toward Yapaev, or (d) coincidental selector-collisions across multiple OSINT layers?"
      analyzed_at: 2026-06-10T16:55:00-04:00
      analyzed_by: analyst
      red_team_review: null

      hypotheses:
        - id: H1
          statement: "Correct attribution: Yapaev IS the administrator Hastalamuerte/Zeta88. The OSINT chain (email → Telegram → GitHub → Apple → phone → LinkedIn → forum registrations) converges because each pivot reflects a real selector reused by the same individual across personas."
        - id: H2
          statement: "Infrastructure overlap with unrelated person: Yapaev is a real Izhevsk resident whose selectors overlap with the administrator's via shared infrastructure (recycled phone number from prior subscriber, shared household IP, sold/reassigned email domain). The administrator is a DIFFERENT person."
        - id: H3
          statement: "Deliberate identity-seeding by the administrator: The administrator selected Yapaev's identifiers (or constructed personas designed to point at Yapaev) as a deliberate honey-trail — knowing investigators would eventually arrive at this identity. Yapaev is either (a) an unwitting decoy or (b) a knowing-but-non-administrator participant."
        - id: H4
          statement: "Deliberate identity-seeding by a THIRD party: A rival actor, LE-adjacent informant, or hostile foreign service constructed/seeded the trail to surface Yapaev as the administrator. Yapaev may or may not be involved in cybercrime at all."
        - id: H5
          statement: "Coincidental selector-collisions across multiple OSINT layers — the chain has at least one pivot that's a false-positive (e.g., a shared username across two unrelated services), and the Krebs methodology has chained false-positives into apparent convergence."
        - id: H6
          statement: "Correct attribution at the role-level but wrong at the identity-level: Yapaev is a real participant in The Gentlemen RaaS at some role (affiliate, locker developer, payment operator) but is NOT the administrator role described by Check Point + Intel 471. Krebs has correctly identified a participant but mis-mapped them to the administrator chair."

      evidence:
        - id: E1
          description: "Intel 471 traces Hastalamuerte forum registration across Exploit, Breachforums (Jan 2025, Izhevsk IP), BHF, Raidforums, Nulled, Codeby (as SantaMeurte, originally 'Alexandr 4apaev'), Ramp_V2, 2019 → present."
          source: intel471-via-krebs
          digraph: B2
          weight: 2
        - id: E2
          description: "Intel 471 reports Breached forum registration August 2022 with a DIFFERENT Izhevsk IP as Zeta88."
          source: intel471-via-krebs
          digraph: B2
          weight: 2
        - id: E3
          description: "Email hastalamuerte1488@protonmail.com (1488 numeric symbology — Krebs explicit on the white-supremacist coded numeric)."
          source: krebs-osint-via-breadcrumbs
          digraph: B2
          weight: 2
        - id: E4
          description: "Telegram @hastalamuerte18 → Telegram ID 30907522 (per Flashpoint)."
          source: flashpoint-via-krebs
          digraph: B2
          weight: 2
        - id: E5
          description: "Telegram username bu4vs (per Constella pivot); phone 79127650004 (per Constella pivot)."
          source: constella-via-krebs
          digraph: B2
          weight: 2
        - id: E6
          description: "GitHub username SantaMuerte (private account watching/developing malware tools)."
          source: krebs-osint
          digraph: B2
          weight: 2
        - id: E7
          description: "Codeby forum registration as SantaMeurte, originally registered as 'Alexandr 4apaev' — direct Cyrillic/4apaev-spelling literal-name surface on a cybercrime forum."
          source: intel471-via-krebs
          digraph: B2
          weight: 2
        - id: E8
          description: "Russian social media Pikabu username 4apai18."
          source: krebs-osint
          digraph: B3
          weight: 1
        - id: E9
          description: "LinkedIn → 'Alexander Yapaev, head of B2B marketing at Uralenergo Udmurtia'."
          source: krebs-osint
          digraph: B3
          weight: 1
        - id: E10
          description: "Check Point + Intel 471 independently corroborate the administrator role assignment to Hastalamuerte/Zeta88 (assembles locker, RaaS panel, manages payments, 10% share)."
          source: check-point-plus-intel471-via-krebs
          digraph: B2
          weight: 2
        - id: E11
          description: "Yapaev did NOT respond to multiple Krebs requests for comment — neither confirming nor denying."
          source: krebs-disclosed
          digraph: B1
          weight: 1
        - id: E12
          description: "Flashpoint is Krebs's disclosed advertiser per the piece — disclosure noted in Krebs piece."
          source: krebs-disclosed
          digraph: B1
          weight: 1
        - id: E13
          description: "1488 symbology (white-supremacist coded numeric) appears in actor's email selector; combined with Hastalamuerte ('until death' Spanish) suggests deliberate ideological signaling in the operational persona — not a value-neutral handle choice."
          source: krebs-osint-analyst-observation
          digraph: B3
          weight: 1
        - id: E14
          description: "Yapaev is reported as a 36-year-old in Izhevsk, Udmurt Republic, with a public LinkedIn profile naming a B2B marketing role at a regional energy company (Uralenergo). This is NOT the classic 'opsec-perfect' cybercriminal profile — the subject has a public identity easily linkable."
          source: krebs-osint
          digraph: B3
          weight: 1
        - id: E15
          description: "Hastalamuerte personas span 2019 → present (7 years); Zeta88 Breached registration is 2022; the Codeby surface preserves the original 'Alexandr 4apaev' literal-name registration."
          source: intel471-via-krebs
          digraph: B2
          weight: 2

      matrix:
        E1: {H1: C, H2: N, H3: C, H4: C, H5: N, H6: C}  # Multi-forum trace is consistent with real persona use OR seeded persona use; non-diagnostic between H1/H3/H4/H6
        E2: {H1: C, H2: N, H3: C, H4: N, H5: N, H6: C}  # 2nd Izhevsk IP weakly favors real-person-in-Izhevsk hypotheses (H1/H6); neutral for seeded
        E3: {H1: C, H2: N, H3: C, H4: C, H5: N, H6: C}  # Email selector is consistent with multiple hypotheses
        E4: {H1: C, H2: I, H3: C, H4: C, H5: N, H6: C}  # Telegram ID is a stable selector; if attribution to Yapaev's Telegram is established, H2 (different person) becomes harder
        E5: {H1: C, H2: I, H3: C, H4: C, H5: N, H6: C}  # Phone number pivot via Constella to Yapaev specifically: hard to reconcile with H2
        E6: {H1: C, H2: N, H3: C, H4: C, H5: N, H6: C}  # GitHub adds technical-tooling layer; consistent with multiple hypotheses
        E7: {H1: C, H2: I, H3: I, H4: C, H5: N, H6: C}  # 'Alexandr 4apaev' literal-name registration on a CYBERCRIME forum (Codeby) is hard to reconcile with H2 (unrelated person — too specific) and H3 (deliberate seeding by the administrator — why would the administrator seed their REAL name?); consistent with H1 (real-person opsec failure 2019) and H4 (third-party seeding) and H6
        E8: {H1: C, H2: N, H3: C, H4: C, H5: C, H6: C}  # Single Pikabu surface is low-weight; consistent with multiple hypotheses
        E9: {H1: C, H2: I, H3: C, H4: I, H5: N, H6: C}  # LinkedIn surface is consistent with real-person hypotheses (H1/H6); harder to reconcile with H4 (third-party seeding of an unrelated person would benefit from NOT having an obvious public LinkedIn surface)
        E10: {H1: N, H2: N, H3: N, H4: N, H5: N, H6: N}  # Role-level attribution to Hastalamuerte/Zeta88 from Check Point + Intel 471 is independent corroboration on the PERSONA level — but doesn't distinguish between the identity-mapping hypotheses
        E11: {H1: N, H2: C, H3: C, H4: C, H5: C, H6: N}  # Subject silence is non-diagnostic but mildly consistent with hypotheses where Yapaev is NOT the administrator (he can't deny without surface acknowledgment) and with H1 (a real cybercriminal wouldn't comment)
        E12: {H1: N, H2: N, H3: N, H4: N, H5: N, H6: N}  # Advertiser disclosure is procedural; non-diagnostic
        E13: {H1: C, H2: I, H3: C, H4: I, H5: N, H6: C}  # 1488 symbology + Hastalamuerte ideological signaling is hard to reconcile with H2 (random unrelated person's selectors happen to be ideologically loaded?) and H4 (third party seeding would not necessarily choose ideologically loaded handles)
        E14: {H1: C, H2: N, H3: I, H4: C, H5: N, H6: C}  # Imperfect-opsec real-person profile is INCONSISTENT with H3 (an administrator who chose Yapaev as a honey-trail decoy would want Yapaev to be a clean attributable surface — which Yapaev IS, but the more attributable the surface, the more it looks like a real failed-opsec actor rather than a deliberate decoy)
        E15: {H1: C, H2: I, H3: I, H4: C, H5: N, H6: C}  # 7-year persona span with the original 'Alexandr 4apaev' literal-name registration in 2019 (and Krebs explicitly identifies this as a historical-opsec-failure surface) is hard to reconcile with H2 (unrelated person doesn't have 7-year persona history) AND with H3 (administrator wouldn't seed their own literal name as the trail-start)

      inconsistency_counts:
        H1: 0
        H2: 6
        H3: 3
        H4: 2
        H5: 0
        H6: 0

      diagnostic_evidence:
        - E7: "Distinguishes real-person attribution (H1/H6) from third-party-seeding (H4) and from unrelated-person (H2) — the Codeby 'Alexandr 4apaev' historical literal-name registration is too specific for H2 and is OFF-strategy for H3 (an administrator deliberately seeding a decoy would not seed their own real name)"
        - E14: "Distinguishes deliberate-seeding-as-decoy (H3) from real-person-opsec-failure (H1) — Yapaev's public LinkedIn surface is so attributable that it reads more like opsec failure than deliberate construction"
        - E15: "7-year persona history with historical literal-name surface is hard to reconcile with both H2 (unrelated person) and H3 (administrator-seeded — too long a runway and too risky a real-name preservation)"
        - E13: "Ideologically loaded persona naming (Hastalamuerte + 1488 symbology) is hard to reconcile with H2 (random selector coincidence on TWO ideologically-loaded markers) and H4 (third party seeding generally chooses ideologically neutral decoys to maximize plausibility)"
        - E4, E5: "Telegram-ID and phone-number pivots via Flashpoint and Constella are stable selectors directly attaching to Yapaev's identity surface — hard to reconcile with H2"

      ranking:
        - rank: 1
          hypothesis_id: H5
          rationale: "Zero inconsistencies. However H5 is the 'one of the pivots is a false-positive' hypothesis — it's not WRONG, it's IMMUNE to the matrix because each individual pivot is presented as supportive evidence (every pivot collision is C with H5's framing that 'at least one pivot is coincidental'). H5 is methodologically inseparable from H1 at this evidence level; it tracks H1's probability minus a confidence-discount on the methodology. NOT actually the leading hypothesis on rank-1 reading; flagged as methodology-honest hypothesis but functionally co-located with H1."
          wep: roughly_even_chance
          methodology_note: "H5 is a structural-skepticism hypothesis rather than a substantive alternative — its zero inconsistencies are a feature of how it's framed, not evidence of its leading status. Treated as the irreducible-uncertainty layer of H1."
        - rank: 1
          hypothesis_id: H1
          rationale: "Zero inconsistencies. Multiple independent OSINT pivots (Intel 471 forum-registration trace, Flashpoint Telegram-ID, Constella phone pivot, Krebs email/GitHub/Pikabu surfaces, the literal-name Codeby registration in 2019) converge on the same identity. The 7-year persona history (E15) and the literal-name Codeby registration (E7) are particularly hard to construct as fabrications. Ideologically loaded persona naming (E13) is consistent with a real ideologically-motivated actor; the imperfect-opsec public LinkedIn surface (E14) is consistent with a real-person opsec failure (which is the BASE-RATE OUTCOME of long-running cybercrime personas)."
          wep: likely
        - rank: 3
          hypothesis_id: H6
          rationale: "Zero inconsistencies. Yapaev IS a real participant in The Gentlemen but at a different role (affiliate, locker developer, payment operator) rather than the administrator chair. Cannot be ruled out from the OSINT chain alone — the chain attaches identity to persona; Check Point + Intel 471 attach persona to role. The role-mapping layer is the under-tested layer. If the administrator role mapping is wrong but the identity mapping is right, the brief framing 'identified as the administrator' overstates the role-confidence."
          wep: unlikely
        - rank: 4
          hypothesis_id: H4
          rationale: "Two inconsistencies (E9 LinkedIn surface and E13 ideological signaling) — third-party seeding would not normally choose an obviously-attributable real-person target with ideologically loaded markers. H4 cannot be ruled out (counter-intelligence operations sometimes intentionally do this) but is substantially less likely than H1/H6."
          wep: unlikely
        - rank: 5
          hypothesis_id: H3
          rationale: "Three inconsistencies (E7 literal-name surface, E14 attributable public profile, E15 7-year persona span). Administrator-deliberate-seeding requires the administrator to have constructed a 7-year persona history culminating in their own legal name being surfaceable — strategically unsound. Unlikely."
          wep: very_unlikely
        - rank: 6
          hypothesis_id: H2
          rationale: "Six inconsistencies (E4, E5, E7, E9, E13, E15). Unrelated-person hypothesis requires Yapaev's selectors to coincidentally overlap with the administrator's across Telegram-ID, phone, GitHub, email, ideological signaling, AND a 7-year persona history with the actor's literal name on a cybercrime forum. Base-rate impossible. Ruled out."
          wep: remote

      sensitivity_analysis:
        brittleness: medium
        load_bearing_evidence: [E7, E15, E4, E5]
        if_E7_overturned: "If the Codeby 'Alexandr 4apaev' literal-name registration is shown to be a different person (different individual named Alexandr Yapaev, common Russian name combination), the chain weakens substantially — but the Telegram-ID and phone pivots (E4, E5) still attach the persona to Yapaev. H1 demoted to 'unlikely'; H6 elevates."
        if_E4_or_E5_overturned: "Flashpoint Telegram-ID or Constella phone pivot revealed as wrong-pivot or shared-infrastructure artifact — chain weakens at the stable-selector layer. H2 partially rehabilitated."
        if_yapaev_publicly_denies_with_specificity: "Subject denial with specific refutation (e.g., 'I can show I was elsewhere on date X' or 'my Telegram ID is actually Y') would directly contradict pivots; H1 demoted."
        if_yapaev_publicly_confirms: "Confirms H1; H2/H3/H4 ruled out."
        if_le_takedown_announces_different_administrator_identity: "Russian or international LE announces administrator identity ≠ Yapaev: H1 demoted to 'remote'; H4 or H3 elevated."
        if_check_point_or_intel471_publishes_separate_attribution_supporting_yapaev: "Confirms H1 at higher WEP; trigger red-team review for HIGH-WEP threshold."

      tripwires:
        - observation: "Yapaev publicly responds (confirm or deny) to Krebs / Check Point / Intel 471"
          effect: "Material change to H1-vs-alternatives ranking"
        - observation: "Russian or international LE announces an administrator identity for The Gentlemen — matching or not matching Yapaev"
          effect: "Direct external validation or refutation"
        - observation: "Check Point or Intel 471 publishes a follow-on attribution piece independently mapping the administrator to Yapaev with separate evidence basis"
          effect: "Lift WEP ceiling on identity layer; consider triggering red-team review"
        - observation: "OFAC or US Treasury sanctions list addition naming Yapaev"
          effect: "External-LE-confirmation tripwire; lifts attribution layer to 'very likely' per multi-source-confirmation precedent"
        - observation: "The Gentlemen group dissolves / rebrands following the Krebs publication"
          effect: "Behavioral evidence consistent with H1 (real subject sees attribution and burns the persona); rerun ACH"
        - observation: "Second person named in subsequent OSINT publication as joint administrator or actual primary administrator"
          effect: "Elevate H6 (correct identity, wrong role); demote H1"

      conclusion:
        summary: |
          H1 (Yapaev IS the administrator) is the leading hypothesis at zero
          inconsistencies — supported by multiple independent stable-selector
          pivots (Intel 471 forum-registration trace, Flashpoint Telegram-ID,
          Constella phone pivot, the 2019 Codeby literal-name 'Alexandr 4apaev'
          registration). The 7-year persona history with a historical literal-
          name surface (E15) is particularly hard to construct as either
          unrelated coincidence (H2: 6 inconsistencies — ruled out) or as
          deliberate seeding (H3: 3 inconsistencies, strategically unsound).
          H4 (third-party seeding) and H6 (correct identity, wrong role) are
          residual alternatives worth flagging but are clearly outranked. The
          irreducible-uncertainty layer (H5 — at least one pivot is a false-
          positive) is structurally inseparable from H1 and represents the
          methodology-honest skepticism Krebs himself acknowledges by NOT
          claiming LE-confirmation.

          Critical Hard Rule 2 framing: the ATTRIBUTION CLAIM here is made by
          Krebs/Check Point/Intel 471/Flashpoint/Constella/KELA — NOT by
          Archimedes. ACH pressure-tests their sourced claim; it does NOT
          originate a new attribution. The leading-hypothesis ranking
          informs how confidently the brief reports their claim (preserved
          verbatim, hedged 'per Krebs Breadcrumbs methodology, not LE-
          confirmed') rather than constituting a new Archimedes-confirmation.
        wep: likely
        wep_layer_specific:
          group_existence_raas_model_victim_count_operational_velocity_initial_access_vector: likely
          administrator_role_attribution_to_hastalamuerte_zeta88_persona_check_point_plus_intel471: likely
          forum_registration_trace_2019_to_present_intel471: likely
          osint_identity_chain_persona_to_yapaev_krebs_breadcrumbs: likely
          yapaev_linkedin_uralenergo_udmurtia_b2b_marketing_head_single_source_layer: roughly_even_chance
        confidence_caveats: |
          (1) Krebs Breadcrumbs methodology is OSINT, NOT LE-confirmed. Subject
          did not respond to comment requests. Brief framing must preserve
          'per Krebs / per the cited sources' verbatim; Archimedes does NOT
          originate the identity attribution.
          (2) H6 (correct identity, wrong role mapping) is the residual
          alternative worth explicit caveat — the OSINT chain attaches
          identity to persona; persona-to-administrator-role mapping is the
          Check Point + Intel 471 layer (independent but still vendor-research-
          based, not LE-confirmed).
          (3) H5 (one pivot is a false-positive) is the irreducible-
          uncertainty layer — Krebs himself acknowledges by NOT claiming
          LE-confirmation; brief framing should mirror this discipline.
          (4) OFAC sanctions consideration is OUT OF SCOPE for Archimedes —
          the OSINT chain is reportable but does NOT constitute the
          evidentiary threshold typically applied for sanctions designation.
          That's an LE / Treasury process, not an Archimedes process.
          (5) Subject denial-or-confirmation tripwire is active; rerun if
          Yapaev publicly responds.

  sat_kac:
    kac_analysis:
      assessment_under_review: |
        (a) The Gentlemen administrator (Hastalamuerte/Zeta88) has been
        identified as Alexander Andreevich Yapaev, 36, Izhevsk, Udmurt
        Republic, Russia, per Krebs Breadcrumbs methodology integrating
        Check Point + Intel 471 + Flashpoint + Constella + KELA + Epieos.
        (b) Krebs's Breadcrumbs methodology reaches a sufficient
        evidentiary threshold for CTI per-source-reportable framing
        without LE confirmation.
        (c) The Gentlemen RaaS warrants /new-actor candidate evaluation
        based on the 332-victim scale, second-most-active-2026 ranking,
        and structural A&D-prime relevance via VPN/firewall initial
        access and hours-to-encryption operational velocity.
      analyzed_at: 2026-06-10T17:00:00-04:00
      analyzed_by: analyst
      invoking_context: "Pre-publication analyst review for 2026-06-10 PM brief — finding-2026-06-10-0017; grader-flagged sat_ach + sat_kac per single-source veto on OSINT identity-chain layer; /new-actor candidate referral; Hard Rule 2 attribution-discipline focus"

      assumptions:
        - id: A1
          statement: "Each individual pivot in Krebs's OSINT chain (email-to-Telegram, Telegram-to-phone, phone-to-LinkedIn, forum-handle-to-literal-name) is methodologically valid and independent — i.e. the chain's apparent convergence reflects real selector overlap, not chained methodology error."
          category: source_reliability
          stated: false
          why_must_be_true: "The identity chain's evidentiary force depends on each pivot being a real-world selector match rather than a methodology artifact."
          when_could_be_false: "Krebs's Breadcrumbs methodology has a documented failure mode in long chains — each pivot has individual error rate, and chained pivots have compound error rate. A 7-step chain with 5% per-step error rate has ~30% total chain error rate (1 - 0.95^7). The methodology is reportable but NOT high-confidence; Krebs himself acknowledges by NOT claiming LE-confirmation."
          evidence_for: [krebs-breadcrumbs-historical-track-record-on-similar-attributions, intel471-forum-registration-tradecraft-pedigree, flashpoint-telegram-id-pivot-pedigree, constella-osint-pivot-tooling-pedigree]
          evidence_against: [no-le-confirmation, subject-did-not-respond]
          confidence: medium
          centrality: critical
          classification: qualify
          note: "Brief framing must preserve 'per Krebs Breadcrumbs methodology, not LE-confirmed' verbatim. Archimedes is NOT originating the attribution — pressure-testing it. The qualify status is the appropriate analyst posture."
        - id: A2
          statement: "Hastalamuerte/Zeta88 (administrator persona) and the Yapaev identity layer are causally tied: the persona's selectors trace to Yapaev because Yapaev IS the persona's operator."
          category: capability
          stated: true
          why_must_be_true: "Brief's identity-attribution claim depends on this causal chain."
          when_could_be_false: "ACH H4 (third-party seeding) or H6 (correct identity, wrong role) — both have nonzero residual probability. The chain attaches identity to PERSONA; the persona-to-administrator-role mapping is the Check Point + Intel 471 layer."
          evidence_for: [ach-h1-zero-inconsistencies]
          evidence_against: [ach-h6-zero-inconsistencies-residual]
          confidence: medium
          centrality: critical
          classification: qualify
          note: "Brief should preserve 'identified as the administrator per Krebs / Check Point / Intel 471' — NOT collapse to 'is the administrator' which would skip the per-source framing required by Hard Rule 2."
        - id: A3
          statement: "Check Point's sustained coverage of The Gentlemen and Intel 471's forum-registration tracking are methodologically separable evidence bases — i.e. they constitute independent corroboration on the administrator-persona role rather than two read-throughs of the same underlying intelligence."
          category: source_reliability
          stated: true
          why_must_be_true: "The role-mapping layer's confidence depends on Check Point and Intel 471 being independent inputs."
          when_could_be_false: "Check Point and Intel 471 may share underlying intelligence sources (informants, paid-access to cybercrime forums, mutual sharing in vendor cooperatives) such that their corroboration is partially-circular."
          evidence_for: [check-point-tier1-vendor-research-pedigree, intel471-cybercrime-forum-monitoring-tradecraft-pedigree, both-have-separate-business-models]
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify
        - id: A4
          statement: "The Gentlemen's 332-victim count + second-most-active-2026 ranking + 90/10 affiliate split are accurately reported per Check Point's sustained coverage."
          category: source_reliability
          stated: true
          why_must_be_true: "The /new-actor candidate referral's velocity / scale rationale depends on these operational facts."
          when_could_be_false: "Check Point's victim count may be a self-reported actor-leak-site enumeration (which has known issues — duplicate listings, retracted listings, false-positive victim claims) rather than independently-confirmed victim list."
          evidence_for: [check-point-sustained-coverage]
          evidence_against: [ransomware-leak-site-victim-counts-have-documented-inflation-pattern-across-vendors]
          confidence: medium
          centrality: material
          classification: qualify
          note: "Brief should report victim counts as 'leak-site-published-victim-count' framing — standard CTI practice — rather than confirmed-victim-list."
        - id: A5
          statement: "The Gentlemen's operational velocity ('encrypt entire networks within hours') and initial-access vector (internet-facing VPN/firewall devices) match the canonical RaaS playbook and are operationally predictive."
          category: ttp_patterns
          stated: true
          why_must_be_true: "Brief's A&D-prime defender takeaway (VPN/firewall hardening, MFA enforcement, backup-server isolation, high-velocity encryption monitoring) depends on these TTPs being operationally predictive of next-victim behavior."
          when_could_be_false: "The Gentlemen's published TTPs may be aspirational / marketing-grade rather than reflective of typical campaign mechanics. RaaS groups often present idealized TTPs to recruit affiliates; actual campaign mechanics vary widely across affiliate skill levels."
          evidence_for: [canonical-raas-playbook-precedent-lockbit-blackcat-cl0p]
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify
        - id: A6
          statement: "Russia's operating environment for cybercriminals (the 'don't hack Russia' tacit-permission norm, low likelihood of LE action against Russia-resident cybercriminals targeting Western victims) means the identity disclosure does NOT itself produce meaningful operational disruption to The Gentlemen."
          category: geopolitical_context
          stated: false
          why_must_be_true: "The brief's downstream framing about 'OFAC implications' and operational impact depends on understanding the Russia-resident enforcement environment."
          when_could_be_false: "(a) Russia's operating environment may be changing in 2026 — recent unpublicized arrests, shifting LE-criminal relationship dynamics; (b) Yapaev's specific situation (e.g., disliked by local Udmurtia LE, conflict with regional FSB, family ties to Ukrainian sphere) may differ from the general pattern."
          evidence_for: [cti-doctrinal-knowledge-russia-resident-cybercriminal-enforcement-pattern]
          evidence_against: []
          confidence: medium
          centrality: peripheral
          classification: sound
        - id: A7
          statement: "Subject silence (no response to multiple Krebs comment requests) is non-diagnostic — neither confirming nor denying."
          category: source_reliability
          stated: true
          why_must_be_true: "Brief reports 'did not respond to multiple requests for comment' — implicitly treating silence as not-informative."
          when_could_be_false: "Subject silence MAY be diagnostic in either direction: (a) a wrongly-identified innocent subject would typically issue a denial via counsel for reputation protection; (b) a correctly-identified subject would typically also remain silent (no upside to commenting). Base rate favors interpretation (b) but the methodology is open."
          evidence_for: []
          evidence_against: []
          confidence: low
          centrality: peripheral
          classification: qualify
          note: "Brief should report subject silence verbatim per Krebs without interpretation. Do not propagate either direction of inference."
        - id: A8
          statement: "Krebs's Flashpoint advertiser disclosure does NOT impair the grading of Flashpoint as an evidence source within this finding (analyst-paid-advertising-disclosure protocol)."
          category: source_reliability
          stated: true
          why_must_be_true: "Grader applied this assumption when keeping Flashpoint at A_provisional."
          when_could_be_false: "Advertiser relationships create commercial incentive for over-prominent positioning of advertiser-derived intelligence; the disclosure does not eliminate the bias, only surfaces it."
          evidence_for: [krebs-disclosure-pattern-historical-track-record, flashpoint-standalone-research-pedigree]
          evidence_against: []
          confidence: medium
          centrality: peripheral
          classification: sound
          note: "Standard analyst-paid-advertising disclosure practice; Flashpoint's grading should remain unchanged. Briefer should preserve the Krebs disclosure note in any quoted/paraphrased framing."
        - id: A9
          statement: "Archimedes' Hard Rule 2 obligation is met by preserving 'per Krebs / per the cited sources' verbatim framing — i.e. it is appropriate for Archimedes to report this attribution without originating it."
          category: source_reliability
          stated: true
          why_must_be_true: "The /new-actor candidate referral and brief publication depend on this being a compliant reporting pattern."
          when_could_be_false: "Edge case: if the brief framing collapses 'per Krebs et al.' into 'is identified as' or 'has been linked to' without preserving the per-source citation, Hard Rule 2 is silently violated. The drafting-discipline requirement is on the briefer."
          evidence_for: [hard-rule-2-explicitly-permits-reporting-sourced-attribution]
          evidence_against: []
          confidence: high
          centrality: critical
          classification: sound
          note: "Sound IF the briefer maintains per-source framing. The brief should NOT say 'The Gentlemen administrator is Alexander Yapaev' — it should say 'Krebs identifies The Gentlemen administrator as Alexander Yapaev per the Breadcrumbs methodology integrating Check Point / Intel 471 / Flashpoint / Constella / KELA / Epieos; not LE-confirmed; subject did not respond to comment requests.'"
        - id: A10
          statement: "A&D-prime structural relevance via internet-facing VPN/firewall initial-access and hours-to-encryption velocity is a defender-actionable framing — i.e. A&D primes can and should act on the TTP-pattern observation independent of victim attribution."
          category: capability
          stated: true
          why_must_be_true: "Brief's defender-takeaway depends on this being actionable framing."
          when_could_be_false: "The defender takeaways (audit external attack surface, tighten VPN/firewall MFA, isolate backup servers, monitor for high-velocity encryption indicators) are GENERIC ransomware-hygiene recommendations that apply regardless of The Gentlemen specifically. The 'A&D-prime structural relevance' framing may be reading more specificity into the finding than the TTP pattern supports."
          evidence_for: [veeam-finding-2026-06-10-0010-backup-server-rce-cross-corpus-tie]
          evidence_against: []
          confidence: medium
          centrality: peripheral
          classification: sound
          note: "The takeaways are valuable as general defender hygiene; the attribution to The Gentlemen specifically doesn't add unique defender actions. Brief should frame as 'The Gentlemen's TTP pattern reinforces canonical defender priorities' rather than 'The Gentlemen specifically requires new defender actions.'"

      classifications_summary:
        sound: 4
        qualify: 6
        test: 0
        reject: 0

      remediation:
        status: proceed_with_qualifications
        qualifying_caveats:
          - "Krebs Breadcrumbs methodology has a documented compound error rate on long chains (~30% on a 7-step chain at 5% per-step error rate). Brief must preserve 'per Krebs / per the cited sources, not LE-confirmed' verbatim (A1)."
          - "Persona-to-administrator-role mapping (Check Point + Intel 471) is independent corroboration on the role but is still vendor-research-based, not LE-confirmed. ACH H6 (correct identity, wrong role) is a nonzero residual. Brief framing must NOT collapse to 'is the administrator' (A2, A9)."
          - "Check Point and Intel 471 are methodologically separable but may share some underlying intelligence sources (informants, paid-access cooperatives) — independence is robust at the methodology level but qualified at the source-input level (A3)."
          - "Victim counts (332 published / 240+ in 2026) are leak-site-published counts; standard CTI inflation issues apply. Brief should preserve 'leak-site-published-victim-count' framing (A4)."
          - "TTP pattern (hours-to-encryption, VPN/firewall initial-access) is canonical RaaS playbook precedent — defender takeaways are valuable but apply broadly across RaaS ecosystem, not uniquely to The Gentlemen (A5, A10)."
          - "Subject silence is reported verbatim WITHOUT interpretation in either direction (A7)."
          - "Flashpoint advertiser disclosure noted per Krebs's own disclosure; analyst-paid-advertising-disclosure protocol holds (A8)."
          - "Hard Rule 2 compliance is BRIEFER-DRAFTING-DISCIPLINE-DEPENDENT: brief must preserve per-source framing. The phrasing 'Krebs identifies ... per Breadcrumbs methodology integrating ...' is the correct pattern; the phrasing 'has been identified as ...' (passive-voice de-attribution) silently violates (A9)."
        tests_required: []
        next_action: "Publish in PM brief WITH the qualifying caveats above. Strict briefer drafting discipline required on per-source framing (Hard Rule 2). /new-actor candidate referral proceeds — TTP-pattern actionability is independent of identity-layer attribution confidence."

      recommended_wep_after_test:
        no_tests_required: "Assessment proceeds with qualifications. WEP held at 'likely' on group-level and persona-level layers; 'roughly even chance' framing on Yapaev LinkedIn single-source layer per ACH; identity chain 'likely' but explicit per-Krebs caveat preserved."

# New-actor candidate referral
new_actor_candidate:
  actor_name: The Gentlemen
  candidacy_rationale: >
    High-velocity RaaS active since mid-2025 (~12 months);
    332 published victims; second most active 2026 by victim
    count; sustained Check Point primary research; multi-
    source OSINT attribution chain via Krebs; aggressive
    90/10 affiliate split signals recruitment from
    competing programs; internet-facing VPN/firewall
    initial-access vector + hours-to-encryption velocity
    maps to canonical APT / ransomware playbook
    overlapping LockBit / BlackCat / Cl0p / Scattered
    Spider tradecraft; structural A&D-prime defender
    relevance via VPN/firewall initial-access and backup-
    server compromise primitives (cross-reference Veeam
    CVE-2026-44963 finding-2026-06-10-0010).
  referral_action: "Operator /new-actor evaluation recommended"

# Source-grade revision proposals
source_grade_revision_proposed:
  - source_yaml_id: check-point
    current_grade: null
    proposed_grade: A_provisional
    reason: >
      First Archimedes-corpus dedicated-id surface for Check
      Point Software vendor research. Tier-1 vendor-research
      precedent class (Wiz Research / SentinelOne / Bitdefender
      / Cisco Talos first-citation precedent). Sustained
      coverage of The Gentlemen RaaS; established global
      cybersecurity vendor research practice.
    severity: addition_requires_ratification
    action: "Post to #actor-review for operator ratification"
  - source_yaml_id: intel471
    current_grade: null
    proposed_grade: A_provisional
    reason: >
      First Archimedes-corpus dedicated-id surface for Intel
      471. Cybercrime-forum monitoring research practice;
      Tier-1 vendor-research precedent class.
    severity: addition_requires_ratification
    action: "Post to #actor-review for operator ratification"
  - source_yaml_id: flashpoint
    current_grade: null
    proposed_grade: A_provisional
    reason: >
      First Archimedes-corpus dedicated-id surface for
      Flashpoint. Cybercrime / threat-actor intelligence
      research practice; Tier-1 vendor-research precedent.
      Note: Flashpoint is Krebs's disclosed advertiser per
      the piece — disclosure noted but does not impair
      grading per analyst-paid-advertising-disclosure
      protocol.
    severity: addition_requires_ratification
    action: "Post to #actor-review for operator ratification"
  - source_yaml_id: constella
    current_grade: null
    proposed_grade: A_provisional
    reason: >
      First Archimedes-corpus dedicated-id surface for
      Constella Intelligence. OSINT pivot-tooling practice;
      Tier-1 vendor-research precedent.
    severity: addition_requires_ratification
    action: "Post to #actor-review for operator ratification"
  - source_yaml_id: ke-la
    current_grade: null
    proposed_grade: A_provisional
    reason: >
      First Archimedes-corpus dedicated-id surface for
      KELA. Cybercrime threat-intelligence practice;
      Tier-1 vendor-research precedent.
    severity: addition_requires_ratification
    action: "Post to #actor-review for operator ratification"
  - source_yaml_id: epieos
    current_grade: null
    proposed_grade: B_provisional
    reason: >
      First Archimedes-corpus dedicated-id surface for
      Epieos. Email-pivot OSINT tool; Tier-2 OSINT-tool
      precedent class.
    severity: addition_requires_ratification
    action: "Post to #actor-review for operator ratification"

# Lifecycle
tlp: CLEAR
published_in_briefs: [2026-06-10-afternoon]
retracted: false
retraction_brief_id: null
---

# Krebs OSINT De-Anonymization — "The Gentlemen" RaaS Administrator Identified Per Breadcrumbs Methodology as Alexander Yapaev (Izhevsk, Russia); Second Most Active Ransomware Group 2026 by Victim Count

## Summary

Krebs on Security published a multi-source OSINT investigation identifying the administrator of The Gentlemen ransomware-as-a-service group per a Breadcrumbs methodology chain integrating Check Point Software, Intel 471, Flashpoint, Constella Intelligence, KELA, and Epieos. The group is reportedly the second-most-active ransomware group in 2026 by victim count, with 332 published victims since its mid-2025 inception and 240+ in 2026 alone. It runs an aggressive 90/10 affiliate revenue split (vs. industry standard 80/20), targets internet-facing VPN and firewall devices for initial access, and encrypts entire networks within hours. The administrator (forum nicknames Hastalamuerte and Zeta88) is identified via OSINT pivots as Alexander Andreevich Yapaev, a 36-year-old from Izhevsk in Russia's Udmurt Republic. Yapaev did not respond to comment requests. The Gentlemen is NOT currently in the Archimedes roster — strong /new-actor candidate. Per Hard Rule 2, the identity chain is preserved as per-source attribution and is NOT Archimedes-confirmed.

## Sources

### Krebs on Security (krebs, B — integrating primary)

- URL: https://krebsonsecurity.com/2026/06/who-runs-the-ransomware-group-the-gentlemen/
- Published: 2026-06-10T14:03:44 UTC
- Author: Brian Krebs
- Key claim: Multi-source OSINT de-anonymization integration.

### Check Point Software (check-point, A provisional — sustained originating research)

- Specific blog URL not surfaced this sweep
- Key claim: Sustained coverage of The Gentlemen RaaS; group profile + RaaS model + administrator role attribution.

### Intel 471 (intel471, A provisional — forum-registration trace)

- Key claim: Hastalamuerte / Zeta88 forum-registration timeline across Exploit, Breachforums, Ramp_V2, BHF, Raidforums, Nulled, Codeby (2019 → present).

### Flashpoint (flashpoint, A provisional — Krebs's disclosed advertiser; Telegram-ID pivot)

### Constella Intelligence (constella, A provisional — OSINT pivot tooling)

### KELA (ke-la, A provisional)

### Epieos (epieos, B provisional — email-pivot OSINT tool)

## Technical detail

### Group profile

- **Name:** The Gentlemen
- **Type:** RaaS (Ransomware-as-a-Service)
- **Active since:** Mid-2025 (~12 months)
- **Victim count:** 332 published since inception; 240+ in 2026
- **Ranking:** Second most active ransomware group in 2026 by victim count
- **RaaS model:** 90/10 affiliate split (vs. industry standard 80/20)
- **Recruitment posture:** Aggressive — accelerating growth by attracting experienced operators from competing programs

### Operational characteristics

- **Initial access vector:** Internet-facing devices — VPNs, firewalls
- **Operational velocity:** "moves quickly to encrypt entire networks within hours" (verbatim per Krebs, 11 words)
- **Profile:** High-velocity / opportunistic targeting

### Administrator role attribution (Check Point + Intel 471 corroboration)

- **Forum nicknames:** Hastalamuerte (primary), Zeta88 (English-language Breached, August 2022)
- **Role per Check Point + Intel 471:** "assembles the locker and RaaS panel, manages payments, and is essentially the administrator of the entire program who receives 10 percent of all ransoms"
- **Forum-registration trace (Intel 471):** 2019 → present across Exploit, Breachforums (Jan 2025, Izhevsk IP), BHF, Raidforums, Nulled, Codeby (as SantaMeurte, originally Alexandr 4apaev), Breached (Aug 2022, different Izhevsk IP as Zeta88), Ramp_V2

### OSINT pivot chain → identity (per Krebs Breadcrumbs methodology; single-source veto applied)

- Email `hastalamuerte1488@protonmail.com` (1488 numeric symbology — Krebs explicit)
- Email `bu4vs@mail.ru`
- Telegram `@hastalamuerte18` → Telegram ID 30907522 (per Flashpoint)
- Telegram username `bu4vs` (per Constella pivot)
- Phone number 79127650004 (per Constella pivot)
- GitHub username `SantaMuerte` (private account watching/developing malware tools)
- Pikabu (Russian social media) `4apai18`
- Codeby `SantaMeurte` → originally registered as `Alexandr 4apaev`
- LinkedIn → "Alexander Yapaev, head of B2B marketing at Uralenergo Udmurtia"
- **Identity claimed:** Alexander Andreevich Yapaev, 36-year-old from Izhevsk, Udmurt Republic, Russia
- **Subject response:** "did not respond to multiple requests for comment"

## IOCs surfaced

### Actor-administrator selectors (not infrastructure IOCs)

- Emails: `hastalamuerte1488@protonmail.com`, `bu4vs@mail.ru`
- Telegram usernames: `@hastalamuerte18`, `bu4vs`
- Telegram ID: 30907522
- Phone number: 79127650004
- GitHub username: SantaMuerte (private)
- Cybercrime forum nicknames: Hastalamuerte, Zeta88, SantaMuerte, SantaMeurte, Alexandr 4apaev

### No infrastructure IOCs

No IPv4, no domains, no hashes published in Krebs piece. First-party Splunk hunt not applicable at this sweep.

## Relationship to existing findings

- **No direct prior finding tie-in** — first The Gentlemen surface in Archimedes corpus
- **Cross-corpus structural context:**
  - Veeam CVE-2026-44963 (finding-2026-06-10-0010) — backup-server-RCE primitive aligned with The Gentlemen's hours-to-encryption velocity pattern
  - ShinyHunters Oracle PeopleSoft campaign (finding-2026-06-10-0012) — parallel cybercriminal-watch lane, also a /new-actor candidate today

## Analytic notes (from analyst review)

The Krebs identity-chain attribution (Hastalamuerte/Zeta88 → Yapaev) survives ACH refutation discipline at the leading-hypothesis tier (zero inconsistencies). The diagnostic evidence is structural: the 2019 Codeby forum registration as the literal-name 'Alexandr 4apaev' is too specific to coincidentally match an unrelated person (rules out H2 at 6 inconsistencies) and is OFF-strategy for deliberate seeding by the administrator (rules out H3 — administrators do not seed their own real names as the trail-start). The 7-year persona history, the Telegram-ID pivot via Flashpoint, and the phone-number pivot via Constella are stable selectors that attach the identity layer firmly to Yapaev. The imperfect-opsec public LinkedIn surface fits the base-rate outcome of long-running cybercrime personas — opsec failure, not deliberate construction. H4 (third-party seeding) and H6 (correct identity but wrong role mapping — Yapaev IS in The Gentlemen but at affiliate / locker-developer rather than administrator chair) are residual alternatives worth flagging but clearly outranked.

Hard Rule 2 is strictly briefer-drafting-discipline-dependent here. The ATTRIBUTION CLAIM is made by Krebs / Check Point / Intel 471 / Flashpoint / Constella / KELA — NOT by Archimedes. ACH pressure-tests their sourced claim; it does NOT originate one. The brief must preserve 'per Krebs / per the cited sources, not LE-confirmed' verbatim. Passive-voice de-attribution patterns ('has been identified as ...') silently violate Hard Rule 2 and must be avoided. The Krebs Breadcrumbs methodology has a documented compound error rate on long chains (~30% on a 7-step chain at 5% per-step error rate) — this is why Krebs himself does not claim LE confirmation, and Archimedes must mirror that discipline. OFAC sanctions consideration is OUT OF SCOPE for Archimedes — the OSINT chain is reportable but does not constitute the evidentiary threshold for sanctions designation; that's an LE / Treasury process. /new-actor candidate referral for The Gentlemen proceeds independently of identity-layer confidence — the TTP-pattern actionability (VPN/firewall hardening, backup-server isolation, high-velocity encryption monitoring) is canonical RaaS-defender hygiene that the attribution simply reinforces.

## Open questions for analyst

- **/new-actor evaluation:** The Gentlemen warrants /new-actor candidate review given (a) sustained 12-month track record, (b) 332-victim scale, (c) second-most-active-2026 ranking, (d) multi-source OSINT attribution chain, (e) aggressive RaaS recruitment posture, (f) A&D-prime structural relevance via VPN/firewall initial-access and hours-to-encryption velocity.
- **Russia attribution policy/OFAC implications:** SAT-ACH on whether Krebs Breadcrumbs OSINT-chain identification (a) constitutes sufficient pre-LE-confirmation basis for any OFAC sanctions consideration, (b) reaches the evidentiary threshold typically applied in CTI for "named individual" attribution, or (c) remains in per-source-reportable framing pending LE confirmation. Hard Rule 2 preserves per-source framing.
- **A&D-prime defender takeaway:**
  - Audit external attack surface for VPN / firewall exposure
  - Tighten VPN / firewall MFA enforcement
  - Ensure backup-server isolation from primary domain (cross-reference Veeam pm-004 finding-2026-06-10-0010)
  - Monitor for high-velocity encryption indicators (rapid GPO / scheduled task / WMI propagation)
- **Hard Rule 6 quote discipline note:** Check Point's "90/10 affiliate revenue split..." quote at 22 words exceeds 15-word ceiling. Briefer should trim or paraphrase if quoting in PM brief.
