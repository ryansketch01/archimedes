---
finding_id: finding-2026-05-28-0008-fbi-group-ib-ghost-stadium-chinese-criminal-2026-fifa-world-cup-4300-domains
created_at: 2026-05-28T16:15:00-04:00
graded_by: grader
grading_run_id: afternoon-20260528-160000
grading_mode: scheduled_brief
test: false

# Core grading
digraph: A2
source_reliability:
  grade: A
  source_name: "FBI PSA260527 (IC3 Public Service Announcement) — relayed by BleepingComputer; Group-IB originating attribution — relayed by The Record"
  source_yaml_id: fbi-flash
  grade_rationale: >
    FBI PSA pre-assigned A per source-grades.yaml (FBI Flash Alerts /
    IC3 PSAs are law-enforcement-vetted, operationally verified
    government source). Group-IB is established Tier-1/Tier-2
    cybersecurity vendor research with prior attribution track record;
    not currently in source-grades.yaml (would need source-grade-log
    addition — librarian flag). BleepingComputer (B) + The Record (B)
    serve as relay layer for two-effective-primary cluster (FBI
    government primary + Group-IB originating-research primary).
    Cluster anchor A on FBI/Group-IB pair; relay layer B does not
    weaken the underlying primaries.
  provisional: false
  embedded_primaries:
    - artifact: FBI PSA260527 IC3 Public Service Announcement
      grade: A
      role: "Government primary — operationally verified law-enforcement consumer-fraud alert"
    - artifact: Group-IB Ghost Stadium originating research investigation (March–May 2026)
      grade: A_provisional
      role: "Originating attribution primary; Group-IB Tier-1/Tier-2 vendor — source-grade-log addition pending"
  source_grade_revision_proposed:
    source_yaml_id: group-ib
    current_grade: not_in_yaml
    proposed_grade: B   # provisional until track-record review
    reason: "First Archimedes-corpus citation as originating research primary. Group-IB is established Tier-1/Tier-2 vendor with prior peer-reviewed APT research. Provisional B pending librarian / operator ratification."
    severity: new_source_addition
    action: "Librarian to add to source-grades.yaml and source-grade-log.md"
credibility:
  grade: 2
  checklist_passed:
    - probably_true_ttp_consistent_with_event_driven_fraud_economy_pattern_fifa_world_cup_attack_surface
    - probably_true_no_contradicting_a_b_grade_source
    - probably_true_technical_claims_internally_coherent_4300_domains_300_active_layui_2_7_6m_chinese_ui_library_chinese_language_code_comments_phishing_kit_lineage_evidence_is_procedurally_verifiable
  rationale: >
    FBI PSA + Group-IB originating research are two independent originator
    streams (different organizations, different evidence bases —
    Group-IB owns the infrastructure attribution via phishing-kit
    code analysis; FBI owns the consumer-warning + IC3-data perspective).
    BleepingComputer + The Record relay independently to different
    audiences. Group-IB's "Chinese-speaking fraudsters" attribution is
    grounded in concrete evidence (Layui 2.7.6m library + Chinese-
    language code comments in phishing kit source) — this is linguistic
    / origin-evidence attribution, NOT China-state attribution; ethnic-
    linguistic identifier only. Hard Rule 2: do not upgrade the
    attribution beyond the source language. Technical scope claims
    (~4,300 domains since August 2025, ~300 active, ~3,800 dormant) are
    Group-IB-counted procedural facts. No contradicting A/B source.
    Credibility 2 (Probably True) — cluster falls just short of grade 1
    (Confirmed) because the FBI + Group-IB pair, while independent in
    organizational sense, partially overlap in operational substrate
    (FBI advisory likely draws on Group-IB submission to IC3; explicit
    citation chain not retrievable this sweep). If FBI PSA's full
    body cites Group-IB as source, the streams collapse to single
    originating evidence; if FBI has independent IC3-reporting evidence,
    grade is 1. Defensible cap at 2 absent that confirmation.
corroboration:
  independent_sources:
    - fbi-flash
    - group-ib-originating-research
    - bleepingcomputer-relay
    - the-record-relay
  independent: true_partial
  test_passed: >
    Two-organization corroboration (FBI government + Group-IB vendor
    research) via two independent relays (BleepingComputer + The Record).
    Partial-independence caveat on whether FBI advisory draws on
    Group-IB submission as substrate.
first_party_precedence:
  applied: false
  splunk_evidence: null
  rationale: >
    Three exemplar domains published (fiffa[.]com, jobs-fifa[.]com,
    fifa-hiring[.]com) but the full ~4,300-domain Group-IB set is not
    in retrievable summary. Splunk hunt against the exemplars is
    candidate enrichment for next sweep. Pattern-match against TLD
    rotation (.org/.xyz/.live/.sale) could surface adjacent
    pre-positioned infrastructure.
single_source_veto_applied: false
wep_ceiling: very_likely

# Cluster metadata
cluster:
  topic: "FBI PSA260527 + Group-IB attribution — Chinese-speaking criminal 'Ghost Stadium' group running 2026 FIFA World Cup fraud cluster (~4,300 domains since August 2025, ~300 active); consumer-focused (premium ticket fraud + employment fraud + data harvesting)"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-05-28-pm-005
  attribution_claims:
    - claimed_actor: "Ghost Stadium (Group-IB-coined name)"
      claimed_by_sources: [group-ib]
      requires_analyst_review: true
      notes: >
        Group-IB attribution language: "Chinese-speaking fraudsters" —
        ethnic-linguistic identifier only, NOT China-state attribution,
        NOT MSS / MPS attributed. Confidence basis: phishing kit uses
        Chinese open-source UI library (Layui 2.7.6m) with Chinese-
        language code comments embedded throughout the source. Per Hard
        Rule 2, grader does NOT upgrade this attribution; analyst may
        surface SAT-ACH on Chinese-speaking-criminal vs. China-state
        distinction with appropriate WEP hedging.
    - claimed_actor: null
      claimed_by_sources: [fbi-flash]
      requires_analyst_review: false
      notes: >
        FBI PSA260527 does not name a specific actor; consumer-warning
        alert focuses on fraud schemes + indicators. No attribution
        beyond the Group-IB-relayed framing.

# Inclusion eligibility
inclusion:
  eligible_for:
    - daily_brief_action
    - weekly_synthesis
    - actor_profile_update

# Downstream handoff
analyst_review_required: true   # WEP very_likely + cluster-corroboration of morning brief 0002 World Cup theme
analyst_review_complete: true
analyst_review_run_id: analyst-20260528-1632
red_team_review_required: true  # WEP very_likely
red_team_review:
  reviewed_at: 2026-05-28T16:54:00-04:00
  reviewed_by: red-team-analyst
  run_id: red-team-20260528-165400
  mode: post_analyst

  strongest_counter_hypothesis:
    hypothesis: >
      H1 (Chinese-speaking criminal financial-fraud, per Group-IB) is the
      sourced and defensible reading and is correctly ranked first. The
      contrarian case is NOT to flip the ranking — Hard Rule 2 prevents
      originating a state attribution Group-IB did not make. The contrarian
      case is that the FOUR INCONSISTENCIES that rule H3 (China-state) out
      are LESS DIAGNOSTIC than the analyst credited, and the gap between H1
      and H2 (state-tolerance / opportunism) is structurally narrower than
      the ACH ranking presents. The four "inconsistencies" against H3 each
      have well-documented Chinese state-cyber counter-examples that erode
      their diagnostic value.
    evidence_for_counter:
      - "E5 (Facebook ads / WhatsApp distribution channels rule out state-CI): MSS-linked operations have used Facebook ads and consumer-app channels for influence + initial-access seeding since at least 2019 (Mandiant's reporting on Dragonbridge / Spamouflage Dragon influence ops; the 2024 Microsoft / OpenAI joint disclosure on Storm-1376 / Storm-2035 Chinese state IO using Facebook + WhatsApp + Telegram-adjacent platforms). The 'state-CI rarely uses Facebook ads' premise embedded in the matrix coding is empirically false for Chinese state actors operating in the IO / pre-positioning space — they use the same consumer channels precisely because attribution becomes harder."
      - "E7 (account-lockout tradecraft is financially motivated, not CI-yield-optimizing): state-tolerance H2 explicitly accommodates 'financially motivated front-end with state-aligned data flow downstream' — locking out the legitimate user does NOT cost a state actor the credential value if credentials + PII have already been exfiltrated and the credential-replay window is short. The analyst's coding implicitly assumes state actors would prioritize long-running account access over data extraction; this is true for some state operations (long-dwell espionage) but not for bulk-PII collection where account access is the EXTRACTION VECTOR, not the dwell vector."
      - "E8 (consumer-fan victim profile inconsistent with state-CI targeting): PRC state services have a documented history of bulk-PII collection against US consumer populations — OPM 2015, Anthem 2015, Equifax 2017, Marriott 2018 (all DOJ-attributed to PRC state services in subsequent indictments). Consumer-fan victim profile is NOT diagnostic against state-CI; it is diagnostic against TARGETED-EXTRACTION state espionage, but bulk-PII state collection has used consumer-platform aggregation as its primary vector at significant scale for a decade."
      - "E9 (no sourced state attribution): absence of evidence != evidence of absence. Group-IB's attribution language is 'Chinese-speaking fraudsters' — this is a DELIBERATE LINGUISTIC HEDGE common in Tier-1 CTI when sourced state attribution cannot be technically substantiated but where state-tolerance / state-direction is structurally consistent with the operational pattern. The Group-IB framing tells us what they could substantiate; it does NOT tell us what is structurally true. H2 (state-tolerance / opportunism) fits the same evidence equally well and Group-IB simply could not source it."
    evidence_against_counter:
      - "Group-IB is the originating-attribution Tier-1 vendor and explicitly chose 'Chinese-speaking fraudsters' framing; arguing H2 against this requires arguing the vendor under-attributed, which red-team can flag but cannot resolve"
      - "Premium-ticket fraud + $60-vs-thousands monetization is straightforwardly criminal-financial; state-direction would not normally bother with the small-dollar lure layer when the high-value extraction is the PII"
      - "Group-IB's procedural fact-set (4,300 domains, 300 active, 3,800 dormant, Layui 2.7.6m + Chinese comments) is consistent with criminal-financial operation at scale and there is no positive evidence of state coordination — H2 is structurally plausible but unsourced"
      - "Hard Rule 2 explicitly prevents red-team from originating the H2 attribution — the contrarian case is to surface that H2 is structurally adjacent to H1, NOT to claim H2 is the correct reading"

  weaknesses_in_primary_assessment:
    - "Four-inconsistency count against H3 is structurally over-confident. E5, E7, E8 each have well-documented Chinese state-cyber counter-examples (Dragonbridge / Spamouflage, OPM / Anthem / Equifax / Marriott bulk-PII pattern). These are reasonably scored 'C' in the bulk-PII state collection variant of H3 (call it H3', which the analyst did not articulate). The matrix's H3 column is coded against a NARROW reading of state-CI (targeted espionage) rather than the broader reading that includes bulk-PII state collection. Re-coding H3 against the broader reading: E5 becomes C (state actors use consumer channels for bulk-collection), E7 becomes N (bulk-extraction does not require account preservation), E8 becomes N (consumer-fan victim profile IS bulk-PII state collection's victim profile). H3' inconsistency count drops from 4 to potentially 1 — and H3' becomes structurally indistinguishable from H2."
    - "Operator-origin from linguistic forensics (Layui 2.7.6m + Chinese comments) carries less attribution weight than the analyst credited. Chinese-origin phishing kits are TRADED on Chinese-language criminal forums (TeleMessage / hackgary / Caoliu-adjacent) AND repurposed by non-Chinese-speaking buyers who do not strip comments. The analyst flagged this as KAC A3 'qualify' at medium confidence — the qualify classification is defensible but the ACH matrix's H4 (false-flag-by-toolchain) coding of E1 + E2 as 'I' is over-confident. A more honest coding: E1 = C for H1/H2/H3/H5, N for H4 (kit-inheritance possible). The H4 inconsistency count drops from 2 to 0."
    - "FBI-Group-IB independence question (KAC A1, qualify, low confidence) is the SINGLE LOAD-BEARING ASSUMPTION on the credibility-2 grade. Analyst correctly flagged that if FBI PSA draws on Group-IB submission to IC3, the streams collapse to single-effective-source and WEP drops one step. The analyst did not pressure-test this — FBI IC3 PSAs are reasonably likely to incorporate vendor-submitted research (Group-IB submission to IC3 is exactly the type of LE-vendor relationship that exists in practice). The analyst's recommended_wep_after_test correctly identified 'if_fbi_drew_on_group_ib_submission: likely' but did not act on it. The contrarian read: the 50/50 risk on A1 is structurally insufficient to support very_likely; conservative reading is 'likely' until citation chain confirmed."
    - "Group-IB first-corpus-citation source-grade-log addition at provisional B is a structural quiet-risk. Group-IB's track record is generally good but has had attribution disputes in the past (RYUK-Conti historical research had naming-collision issues; some FIN7 attribution sub-claims have been contested). Provisional B is reasonable but treating the provisional grade as carrying the same weight as established B-grade for the WEP ceiling is generous."
    - "ACH brittleness classified as 'low' — contrarian reading is medium-to-high. If E5, E7, E8 are re-coded against bulk-PII state collection (H3'), the H1/H3' gap closes substantially and the ACH's apparent strong-leader profile shifts to narrow-leader. The 'low brittleness' framing under-represents the dependence on the narrow-state-CI reading of H3."

  strongest_counter_wep: likely

  recommendation: qualify

  qualifying_language_suggested: >
    "Group-IB attributes the Ghost Stadium FIFA World Cup fraud cluster
    (~4,300 domains since August 2025; ~300 active, ~3,800 dormant) to a
    Chinese-speaking criminal group, based on phishing-kit Chinese-language
    code comments and Chinese open-source UI library (Layui 2.7.6m) embedded
    in the source. FBI PSA260527 names the consumer-fraud surface without
    attributing. Group-IB's framing is linguistic-evidence-only and
    explicitly NOT a China-state attribution — H1 (criminal financial fraud,
    per Group-IB) is the sourced reading. The bulk-PII collection victim
    profile does not by itself rule out a state-tolerance / state-tasking
    relationship structurally adjacent to the criminal-financial primary
    motivation; that adjacency is not in any cited source and remains an
    unverified contrarian read. FBI-Group-IB operational independence
    (whether the PSA draws on Group-IB submission as substrate) is unverified
    this sweep — if the streams collapse, WEP drops one step to likely."

  specific_tests_that_would_resolve:
    - "Retrieve Group-IB primary blog (not retrievable this sweep) — verify whether explicit state-tolerance language was excluded from the The Record summary, and verify the operator-origin vs. toolchain-inheritance argument is technically substantiated"
    - "Retrieve FBI PSA260527 primary text (not just BleepingComputer relay) — confirm whether FBI cites Group-IB as substrate; resolves KAC A1 directly"
    - "Splunk hunt of the three exemplar domains (fiffa[.]com, jobs-fifa[.]com, fifa-hiring[.]com) + the four TLD rotation patterns (.org, .xyz, .live, .sale) against defenseclaw_local. Specifically: if hunt returns DIB-employee click-through and the click-through includes credential capture, the consumer-fan victim profile diagnostic (E8) weakens further and H3' (bulk-PII state collection) gains structural weight"
    - "Track second Tier-1 vendor (CrowdStrike, Mandiant, Unit 42, Bitdefender follow-up) attribution — corroboration of Group-IB at A1 candidate vs. divergent attribution narrative"

  wep_adjustment_recommended: likely
  wep_adjustment_rationale: >
    Contrarian recommendation drops WEP one step from very_likely to likely.
    Two compounding reasons. (1) FBI-Group-IB independence (KAC A1) is
    unverified this sweep and explicitly drops WEP one step if it fails per
    analyst's own recommended_wep_after_test — the partial-independence
    grading already acknowledged this risk but the WEP ceiling stayed at
    very_likely. (2) H3 / H3' (bulk-PII state collection) diagnostic gap is
    narrower than the four-inconsistency count presents; rerunning E5/E7/E8
    coding against the bulk-PII state collection reading collapses the
    inconsistency count for H3' substantially and erodes the strong-leader
    profile. Hard Rule 2 still prevents claiming H2 / H3' affirmatively, but
    the WEP on the sourced H1 should reflect the structurally-narrower gap
    to the unsourced adjacent hypotheses. Likely (55-85%) is the honest
    reading given (1) the un-tested single-source-collapse risk and
    (2) the structural adjacency to unsourced bulk-PII-state hypothesis.

  contrarian_ach_result:
    re_ran_from_contrarian_position: true
    recoded_evidence:
      - E5_against_H3_broader: "C (was I) — state actors use Facebook ads / WhatsApp for bulk-collection IO and pre-positioning (Dragonbridge / Spamouflage, Storm-1376 / Storm-2035)"
      - E7_against_H3_broader: "N (was I) — bulk-PII extraction does not require account-access preservation; lockout is consistent with extract-and-discard pattern"
      - E8_against_H3_broader: "N (was I) — consumer-fan victim profile is the empirical target profile of OPM-class bulk-PII state collection (OPM 2015, Anthem 2015, Equifax 2017, Marriott 2018)"
      - E1_against_H4: "N (was I) — Chinese-origin kit inheritance via traded toolchain does NOT rule out non-Chinese-speaking operator"
      - E2_against_H4: "N (was I) — comments inherited from kit source are operator-independent"
    recoded_inconsistency_counts:
      H1: 0  # unchanged
      H2: 0  # unchanged
      H3_narrow_state_CI: 4  # unchanged (analyst's original H3 reading)
      H3_prime_bulk_PII_state: 1  # was 4 in narrow H3; bulk-PII variant is structurally adjacent to H2
      H4: 0  # was 2; toolchain-inheritance reading drops both inconsistencies
      H5: 0  # unchanged
    finding: >
      Contrarian ACH does NOT flip the ranking — H1 remains rank-1 because
      Group-IB sourced it and Hard Rule 2 prevents originating an alternative
      attribution. However, the H1 / H2 / H3' / H4 / H5 gap collapses to
      structurally indistinguishable under the recoded matrix. The original
      ACH's 'strong leader, low brittleness' profile is structurally accurate
      only against the narrow H3 reading; against the broader bulk-PII state
      collection variant (H3'), the leader gap is narrow. WEP should reflect
      narrow-leader rather than strong-leader profile.

  notes: >
    Not blocking, but recommending WEP drop very_likely → likely. The Chinese-
    speaking criminal financial-fraud reading remains the sourced and most
    defensible attribution. The contrarian pressure surfaces two distinct
    structural risks: (1) FBI-Group-IB single-source-collapse if PSA draws
    on Group-IB submission — explicit drop-one-step trigger the analyst
    already articulated but did not act on; (2) the four-inconsistency
    diagnostic against state-cyber is built on a narrow reading of state-CI
    (targeted espionage) and erodes substantially under the bulk-PII state
    collection variant. Briefer should preserve Group-IB's 'Chinese-speaking
    fraudsters' verbatim AND explicitly state the linguistic-evidence-only
    nature of the attribution AND avoid the "ruled out: China-state" framing
    that the ACH's narrow-H3 reading would otherwise support. The DIB-
    employee spillover hunt remains the highest-value first-party test and
    should run regardless of brief inclusion.
analysis_sections:
  sat_ach:
    ach_analysis:
      question: >
        Which actor-type best fits Group-IB's "Ghost Stadium" cluster
        (~4,300 fraudulent FIFA domains since August 2025, Layui 2.7.6m
        UI library, Chinese-language source-code comments, premium-ticket
        + employment + data-harvesting fraud)?
      analyzed_at: 2026-05-28T16:32:00-04:00
      analyzed_by: analyst
      red_team_review: null
      hypotheses:
        - id: H1
          statement: >
            Chinese-speaking criminal financial-fraud group (Group-IB's sourced
            characterization) — purely financially motivated, operates from
            mainland China or PRC-diaspora region, no state direction.
          attribution_provenance: sourced  # Group-IB explicitly says this
        - id: H2
          statement: >
            Chinese-speaking criminal group operating with state tolerance /
            tasking opportunism — financially primary, but data-harvesting
            yield is shared with or sold to PRC services (MSS / MPS) as
            opportunistic byproduct.
          attribution_provenance: not_sourced
        - id: H3
          statement: >
            China-state operation (MSS / MPS) using criminal-fraud cover for
            data-harvesting against Western consumer-fan populations (names,
            addresses, banking) to feed broader CI / influence dossiers.
          attribution_provenance: not_sourced
        - id: H4
          statement: >
            Non-Chinese-speaking criminal group using a Chinese-origin phishing
            kit (Layui + Chinese comments inherited from kit source); false-
            flag-by-toolchain rather than operator-origin.
          attribution_provenance: not_sourced
        - id: H5
          statement: >
            Multi-actor cluster — multiple Chinese-speaking criminal subgroups
            running shared infrastructure / phishing-kit lineage; Group-IB's
            'Ghost Stadium' label is an attribution-bucket rather than a
            single coherent actor.
          attribution_provenance: not_sourced
      evidence:
        - id: E1
          description: "Phishing kit uses Layui 2.7.6m (Chinese open-source UI library)"
          source: group-ib-originating-research
          digraph: A2
          weight: 3
        - id: E2
          description: "Chinese-language code comments embedded throughout source"
          source: group-ib-originating-research
          digraph: A2
          weight: 3
        - id: E3
          description: "Fraud categories: premium-ticket ($60 vs thousands officially), employment fraud, data harvesting (names/addresses/banking)"
          source: fbi-flash
          digraph: A2
          weight: 3
        - id: E4
          description: "Scale: ~4,300 domains since August 2025; ~300 active, ~3,800 dormant/pre-positioned"
          source: group-ib-originating-research
          digraph: A2
          weight: 3
        - id: E5
          description: "Distribution channels: Facebook ads, Google Search, Telegram, WhatsApp — consumer-fan-targeting"
          source: group-ib-originating-research
          digraph: A2
          weight: 3
        - id: E6
          description: "Geographic spread per Bitdefender: UK / Portugal / Spain / Algeria / US / Canada / Mexico / Brazil / Germany / Australia"
          source: bleepingcomputer-relay
          digraph: B2
          weight: 2
        - id: E7
          description: "Phishing kit post-credential-capture redirects victim to legitimate site, requests password reset to lock victims out"
          source: group-ib-originating-research
          digraph: A2
          weight: 3
        - id: E8
          description: "Victim profile is consumer fans, not government / military / corporate / DIB"
          source: fbi-flash + group-ib-originating-research
          digraph: A2
          weight: 3
        - id: E9
          description: "No MSS / MPS-attributed infrastructure overlap or sourced state attribution"
          source: absence_of_evidence
          digraph: B3
          weight: 2
      matrix:
        E1: {H1: C, H2: C, H3: C, H4: I, H5: C}
        E2: {H1: C, H2: C, H3: C, H4: I, H5: C}
        E3: {H1: C, H2: C, H3: C, H4: C, H5: C}
        E4: {H1: C, H2: C, H3: C, H4: N, H5: C}
        E5: {H1: C, H2: C, H3: I, H4: C, H5: C}  # state-CI rarely uses Facebook ads / WhatsApp for primary targeting
        E6: {H1: C, H2: C, H3: N, H4: C, H5: C}
        E7: {H1: C, H2: C, H3: I, H4: C, H5: C}  # account-lockout is financially motivated, not CI-yield-optimizing
        E8: {H1: C, H2: C, H3: I, H4: C, H5: C}  # consumer-fan victim profile inconsistent with state-CI targeting
        E9: {H1: C, H2: N, H3: I, H4: C, H5: C}  # no sourced state attribution
      inconsistency_counts:
        H1: 0
        H2: 0
        H3: 4
        H4: 2
        H5: 0
      diagnostic_evidence:
        - E5: "Facebook / WhatsApp distribution channels distinguish criminal-financial (H1/H2/H4/H5) from state-CI (H3)"
        - E7: "Account-lockout tradecraft is financially motivated; CI-yield collection would preserve account access for ongoing monitoring"
        - E8: "Consumer-fan victim profile diagnostic against state-CI targeting class"
        - E1+E2: "Chinese-origin toolchain evidence weakly diagnostic against H4 (false-flag-by-toolchain) absent further mimicry indicators"
      ranking:
        - rank: 1
          hypothesis_id: H1
          rationale: >
            Group-IB's sourced characterization. Zero inconsistencies.
            Diagnostic evidence (E5, E7, E8) all consistent with criminal-
            financial profile. Hard Rule 2 anchor: this is the attribution
            the source made.
          wep: very_likely
        - rank: 2
          hypothesis_id: H2
          rationale: >
            Zero inconsistencies but requires unverified premise (state
            tolerance / tasking opportunism). Cannot be elevated without
            sourced citation; remains structurally plausible but
            unconfirmed.
          wep: roughly_even_chance
        - rank: 3
          hypothesis_id: H5
          rationale: >
            Zero inconsistencies but requires unverified premise (multi-
            subgroup cluster). Plausible given scale (E4) and dormant-
            infrastructure pattern; not sourced.
          wep: roughly_even_chance
        - rank: 4
          hypothesis_id: H4
          rationale: >
            Two inconsistencies (E1, E2). False-flag-by-toolchain is
            possible but requires the actor to source a Chinese-origin
            kit AND maintain Chinese-comment authenticity AND not leave
            other operator-origin tells. Weakest fit.
          wep: unlikely
        - rank: 5
          hypothesis_id: H3
          rationale: >
            Four inconsistencies. State-CI hypothesis fails on victim
            profile (E8), distribution channels (E5), account-lockout
            tradecraft (E7), and absence of any sourced state attribution
            (E9). Ruled out.
          wep: very_unlikely
      sensitivity_analysis:
        brittleness: low
        load_bearing_evidence: [E5, E7, E8]
        if_group_ib_downgraded: "H1 / H2 ranking gap narrows; H5 cluster-of-actors hypothesis becomes equally plausible"
        if_state_attribution_emerges: "H2 lifts toward H1-equivalent; H3 cannot be elevated without explicit sourced state attribution"
        if_dib_employee_victim_emerges: "E8 contradicted; H3 inconsistencies drop one; rerun ACH"
        single_point_of_failure: >
          H1 / H2 / H5 are all consistent with the evidence; the ACH
          ranks H1 first because that is the sourced attribution. Hard
          Rule 2 prevents elevating H2 or H5 to a sourced claim without
          a citation. The ACH is structurally robust because the
          diagnostic against H3 (state-CI) is strong from victim profile
          and tradecraft alone, regardless of source.
      tripwires:
        - observation: "Second Tier-1 vendor (CrowdStrike / Mandiant / Unit 42 / Bitdefender follow-up) corroborates Group-IB attribution"
          effect: "Lift cluster to A1 candidate; H1 confirmed"
        - observation: "Any DIB-prime employee click-through observed in defenseclaw_local hunt"
          effect: "Spillover-vector validation; doesn't shift ACH ranking but lifts A&D-relevance"
        - observation: "MSS / MPS-attributed source documents infrastructure overlap"
          effect: "Lifts H2 / H3 candidacy; rerun ACH"
        - observation: "Group-IB blog full text retrieved, contains state-tasking evidence"
          effect: "May lift H2 to sourced; H3 only if state-CI tasking is explicit"
      conclusion:
        summary: >
          Ghost Stadium most likely is the Chinese-speaking criminal financial-
          fraud cluster Group-IB characterized — H1 ranks first with zero
          inconsistencies and strong diagnostic support from victim profile,
          distribution channels, and account-lockout tradecraft. H3 (China-
          state operation) is ruled out by four inconsistencies; H2 / H5
          remain plausible alternatives but not sourced. Hard Rule 2 caps
          analyst at H1 (Group-IB's sourced framing).
        wep: very_likely
        confidence_caveats: >
          Brittleness low. The Chinese-speaking-criminal vs. China-state
          distinction is the key analytic discipline — briefer must preserve
          Group-IB's linguistic-origin characterization verbatim and NOT
          upgrade to state attribution. H2 (state-tolerance / opportunism)
          remains structurally plausible but unsourced and cannot be
          asserted.
  sat_kac:
    kac_analysis:
      assessment_under_review: >
        "FBI PSA260527 + Group-IB attribute a Chinese-speaking criminal group
        named 'Ghost Stadium' to ~4,300 fraudulent FIFA World Cup domains
        registered since August 2025, with ~300 actively running malicious
        infrastructure and ~3,800 dormant / pre-positioned for campaign-stage
        deployment" (paraphrased FBI + Group-IB).
      analyzed_at: 2026-05-28T16:34:00-04:00
      analyzed_by: analyst
      invoking_context: "Analyst review on A2 / very_likely finding with linguistic-evidence-only attribution and partial-independence corroboration"
      assumptions:
        - id: A1
          statement: "FBI PSA260527 and Group-IB are operationally independent originator streams (not FBI relaying Group-IB submission)"
          category: source_reliability
          stated: true
          why_must_be_true: "Credibility 2 (vs. 1) hinges on this — grader flagged the dependency risk"
          when_could_be_false: "FBI PSA may draw on Group-IB submission to IC3 as substrate; explicit citation chain not retrievable this sweep"
          evidence_for: []
          evidence_against: []
          confidence: low
          centrality: material
          classification: qualify
        - id: A2
          statement: "Group-IB's 'Chinese-speaking' attribution is linguistic-evidence-only and does NOT imply China-state direction"
          category: source_reliability
          stated: true
          why_must_be_true: "Hard Rule 2 discipline rests on preserving the source's framing verbatim"
          when_could_be_false: "Group-IB primary blog (not retrieved) may contain additional state-attribution language; SecurityWeek / The Record summary may have stripped nuance"
          evidence_for: [group-ib-originating-research, the-record-relay]
          evidence_against: []
          confidence: high
          centrality: critical
          classification: sound
        - id: A3
          statement: "Layui 2.7.6m + Chinese-language code comments are operator-origin evidence, not toolchain-inheritance from a public phishing kit"
          category: TTP_patterns
          stated: false
          why_must_be_true: "Operator-origin attribution defensibility depends on this"
          when_could_be_false: "Chinese-origin phishing kits are publicly traded; non-Chinese-speaking criminal could repurpose with comments intact"
          evidence_for: [group-ib-originating-research]
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify
        - id: A4
          statement: "~4,300 domain count + ~300 active / ~3,800 dormant ratio is Group-IB-counted procedural fact, not extrapolation"
          category: source_reliability
          stated: true
          why_must_be_true: "Scale claim drives operational-tempo framing"
          when_could_be_false: "Domain-counting methodology may include speculative-cluster expansion or registration-pattern inference"
          evidence_for: [group-ib-originating-research]
          evidence_against: []
          confidence: medium
          centrality: peripheral
          classification: sound
        - id: A5
          statement: "Dormant 3,800-domain pool will be activated for campaign-stage deployment as World Cup approaches (June 11 – July 19, 2026)"
          category: TTP_patterns
          stated: true
          why_must_be_true: "Forward-projection / standing carry-forward justification depends on this"
          when_could_be_false: "Dormant domains may be takedown-defensive / sunk-cost / abandoned registrations"
          evidence_for: [group-ib-originating-research]
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify
        - id: A6
          statement: "DIB-employee click-through risk from consumer-fan vector is non-trivial and warrants Splunk hunt"
          category: visibility
          stated: true
          why_must_be_true: "A&D-relevance narrative depends on consumer-fan / DIB-employee vector spillover"
          when_could_be_false: "DIB primes may have aggressive web-filtering on sports-event / ticket / employment domains during operational tempo events"
          evidence_for: []
          evidence_against: []
          confidence: low
          centrality: peripheral
          classification: qualify
        - id: A7
          statement: "Group-IB's track record as Tier-1/Tier-2 vendor is reliable on attribution, despite not currently being in source-grades.yaml"
          category: source_reliability
          stated: true
          why_must_be_true: "Provisional B grade rests on track-record precedent"
          when_could_be_false: "Group-IB has had some prior attribution disputes; track-record is good but not perfect"
          evidence_for: [group-ib-originating-research]
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify
        - id: A8
          statement: "Three exemplar domains (fiffa[.]com, jobs-fifa[.]com, fifa-hiring[.]com) are representative of the broader 4,300-domain set"
          category: semantic
          stated: true
          why_must_be_true: "Splunk hunt productivity depends on exemplar representativeness"
          when_could_be_false: "Group-IB / FBI may have highlighted highest-traffic / most-distinctive domains; broader set may show different patterns"
          evidence_for: [fbi-flash, bleepingcomputer-relay]
          evidence_against: []
          confidence: medium
          centrality: peripheral
          classification: sound
      classifications_summary:
        sound: 3
        qualify: 5
        test: 0
        reject: 0
      remediation:
        status: proceed
        qualifying_caveats:
          - "FBI / Group-IB operational independence not fully verified (FBI PSA may draw on Group-IB submission as substrate)"
          - "Operator-origin attribution rests on Layui + Chinese-comment evidence; toolchain-inheritance alternative cannot be fully ruled out"
          - "Dormant 3,800-domain pool activation forecast is structural inference, not directly evidenced"
          - "DIB-employee spillover risk modeled but not directly evidenced; Splunk hunt would resolve"
          - "Group-IB track-record presumed reliable; first Archimedes-corpus citation"
        next_action: >
          Brief at very_likely on the Chinese-speaking criminal cluster
          characterization (H1 from ACH). Preserve Group-IB linguistic-origin
          language verbatim; do NOT upgrade to state attribution. Splunk
          hunt of three exemplar domains + four TLD rotation patterns
          against defenseclaw_local. Librarian to add Group-IB to
          source-grades.yaml at provisional B.
      recommended_wep_after_test:
        if_fbi_group_ib_independence_validated: very_likely  # current ceiling
        if_fbi_drew_on_group_ib_submission: likely  # single-source collapse drops one step
        if_splunk_hunt_returns_dib_hits: very_likely  # validates spillover; doesn't change ACH ranking

# Red-team downstream flags
red_team_review_complete: true
red_team_outcome: qualify
wep_ceiling_adjusted_by_red_team: true
wep_ceiling_adjustment_value: likely  # was very_likely
wep_ceiling_adjustment_reason_red_team: >
  Two compounding structural weaknesses justify one-step WEP drop. (1) FBI-
  Group-IB operational independence (KAC A1) is unverified this sweep and
  triggers analyst's own 'if_fbi_drew_on_group_ib_submission: likely' drop-
  one-step path — partial-independence grading already acknowledged the risk
  but ceiling stayed at very_likely. (2) Contrarian-recoded ACH (against
  bulk-PII state collection variant H3' rather than narrow targeted-espionage
  H3) collapses the H1 / H3' diagnostic gap from four inconsistencies to
  approximately one. Hard Rule 2 still prevents claiming H2 / H3'
  affirmatively, but the WEP on H1 should reflect narrow-leader rather than
  strong-leader profile. WEP ceiling adjusted from very_likely to likely.
publication_blocked: false

# Lifecycle
tlp: CLEAR
published_in_briefs: [2026-05-28-afternoon]
retracted: false
retraction_brief_id: null
---

# FBI PSA260527 / Group-IB Attribution — Chinese-Speaking "Ghost Stadium" Criminal Group Runs 2026 FIFA World Cup Fraud Cluster

## Summary

The FBI on 2026-05-28 published IC3 Public Service Announcement **PSA260527** warning consumers of fraudulent FIFA-themed websites operating in advance of the 2026 World Cup. Singapore-based research firm **Group-IB** (originating attribution) attributes the cluster to a **Chinese-speaking criminal group named "Ghost Stadium"** — active since November 2025, operating ~4,300 fraudulent domains registered since August 2025, with ~300 actively running malicious infrastructure and ~3,800 dormant/pre-positioned for campaign-stage deployment. Attribution is linguistic-evidence-based (phishing kit uses Chinese open-source UI library Layui 2.7.6m with Chinese-language comments throughout the source code) — **Chinese-speaking-criminal**, NOT China-state, NOT MSS / MPS-attributed. Fraud categories: premium-ticket fraud ($60 vs. thousands officially), employment fraud (jobs-fifa[.]com / fifa-hiring[.]com pattern), data harvesting (names, addresses, banking details). Distribution channels: Facebook ads, Google Search, Telegram, WhatsApp. Geographic spread per Bitdefender observation: UK, Portugal, Spain, Algeria, US, Canada, Mexico, Brazil, Germany, Australia.

## Sources

### FBI PSA260527 (fbi-flash, digraph: A) — relayed by BleepingComputer

- URL: https://www.bleepingcomputer.com/news/security/fbi-warns-of-fake-fifa-websites-running-world-cup-fraud-schemes/
- Published: 2026-05-28T19:08:10Z (15:08 EDT)
- Byline: Bill Toulas (BleepingComputer)
- Underlying: IC3 PSA260527
- Key claim: FBI consumer-warning advisory naming fraudulent FIFA-themed website cluster targeting World Cup attendees; ticket-fraud, employment-fraud, and data-harvesting categories named.

### Group-IB originating research — relayed by The Record

- URL: https://therecord.media/chinese-speaking-fraud-gang-fifa-world-cup-scam
- Published: 2026-05-28T13:20:00Z (09:20 EDT)
- Byline: Alexander Martin (UK Editor for Recorded Future News)
- Underlying: Group-IB investigation (March–May 2026); Ghost Stadium first observed November 2025
- Key claim: Group-IB attribution of the cluster to "Chinese-speaking fraudsters" (operator profile, linguistic evidence — Layui 2.7.6m library + Chinese-language source-code comments). Scope: ~4,300 domains, ~300 active.

## Technical detail

### Scale and methodology (Group-IB)
- **~4,300 fraudulent domains** registered since August 2025
- **~300 actively running** malicious infrastructure
- **~3,800 dormant / pre-positioned** (campaign-stage-ready)
- **Domain spoofing patterns:** minor spelling variations (e.g., fiffa[.]com), alternative TLDs (.org, .xyz, .live, .sale)
- **Phishing kit lineage:** clones FIFA login system; silently redirects users to legitimate site post-credential-capture; requests password-reset parameters to lock victims out of legitimate accounts
- **Premium-ticket fraud:** discounted tickets ($60 vs. thousands officially); Facebook ads primary distribution
- **Employment fraud:** jobs-fifa[.]com / fifa-hiring[.]com pattern
- **Data harvesting:** names, physical addresses, email addresses, phone numbers, banking / payment details
- **Distribution:** Google Search, Facebook ads, Telegram, WhatsApp

### Attribution evidence (Group-IB)
- Phishing kit uses **Layui 2.7.6m** (Chinese open-source UI library)
- **Chinese-language comments embedded throughout the source code**
- Attribution language preserved: "Chinese-speaking fraudsters" — operator linguistic-origin identifier, NOT China-state attribution

## IOCs surfaced

```yaml
domains:
  - "fiffa[.]com"            # exemplar typo-domain per FBI/BleepingComputer
  - "jobs-fifa[.]com"        # employment-fraud pattern
  - "fifa-hiring[.]com"      # employment-fraud pattern
  # Full ~300 active + ~3,800 dormant domain set NOT in retrievable summary
  # Group-IB primary blog likely contains the full domain set
tld_patterns_observed:
  - .org
  - .xyz
  - .live
  - .sale
phishing_kit_lineage:
  library: "Layui 2.7.6m (Chinese open-source UI library)"
  code_comments_language: Chinese
attribution_claims:
  - claim: "Chinese-speaking fraudster" group operating since November 2025
    claimed_by: Group-IB
    nation_attribution_strength: linguistic-evidence-only (NOT China-state, NOT MSS / MPS)
fbi_alert_reference: PSA260527
ip_addresses: []
hashes: []
cves: []
```

**Operator hunt recommendation:** the three exemplar domains + the four observed TLD rotation patterns are candidates for Splunk hunt against defenseclaw_local for any DIB-workforce employee click-through (consumer-fan vector spillover into DIB-employee inbound).

## Relationship to existing findings

**This finding pairs with morning brief finding-2026-05-28-0002 (Unit 42 2026 World Cup attack surface — Iran IRGC/MOIS fronts + Handala + Cyberav3ngers + Razing Ursa + NoName057).** Decision: **distinct clusters, not merged**. Rationale:
- **Different actor class.** Iran-state ideological / disruptive operators (Unit 42 morning) vs. Chinese-speaking criminal financial-fraud operators (this finding, PM). Different motivations (espionage / sabotage vs. financial fraud), different victim profiles (think tanks / journalists / civil society vs. consumer fans).
- **Same attack surface.** The 2026 FIFA World Cup event-driven attack surface is now corpus-tracked with **at least three concurrent threat layers**:
  1. Iran IRGC/MOIS front campaigns (Unit 42, morning finding 0002 — ideological / disruptive)
  2. Chinese-speaking criminal Ghost Stadium (this finding — financial fraud)
  3. Additional patterns Bitdefender observed in 10 countries (mentioned in BleepingComputer but not detailed this sweep)
- **A&D-direct relevance is indirect for this finding** (consumer-fan victim profile, no contractor / DIB / federal employee victim category named). DIB-employee spillover risk via personal-fan-engagement is real but not the direct surface.

This three-layer concurrence is the kind of **broad-spectrum opportunistic targeting** that DIB-prime IT teams should be modeling — World Cup season generates lure-content traversing both consumer-fan and DIB-employee inbound vectors. The pairing with morning finding 0002 elevates the World Cup attack-surface as a standing brief theme through July 19, 2026.

## Open questions for analyst

- **Source-grade-log addition.** Group-IB is new to source-grades.yaml. Librarian flag for addition; provisional B starting grade (consistent with established Tier-1/Tier-2 vendor precedent class). Operator may ratify.
- **Attribution discipline.** Group-IB's "Chinese-speaking fraudsters" is linguistic-evidence-only. Analyst should NOT escalate to China-state attribution; SAT-ACH on the Chinese-speaking-criminal vs. China-state distinction would surface the operator-profile argument cleanly.
- **World Cup attack-surface theme.** Brief carry-forward through July 19, 2026 (event conclusion). Briefer should establish standing section if PM-28 brief lands this.
- **DIB-employee spillover hunt.** Three exemplar domains + four TLD rotation patterns are candidates for defenseclaw_local hunt for DIB-workforce click-through risk.

## Source notes

- All quotes ≤15 words per Hard Rule 6.
- Hard Rule 2 preserved: linguistic-origin attribution preserved verbatim, NOT upgraded to state-attribution.
- Group-IB first Archimedes-corpus citation — librarian source-grades.yaml addition pending.

## Analytic notes (from analyst review)

ACH ranks H1 (Chinese-speaking criminal financial-fraud, per Group-IB's sourced characterization) first with zero inconsistencies, supported by three diagnostic evidence items: distribution channels via Facebook ads / WhatsApp (E5), account-lockout tradecraft after credential capture (E7), and consumer-fan victim profile (E8). All three are diagnostic against H3 (China-state operation), which collects four inconsistencies and is ruled out. H2 (state tolerance / opportunism) and H5 (multi-subgroup cluster) remain structurally plausible alternatives but unsourced — Hard Rule 2 prevents elevating either. The briefer must preserve Group-IB's "Chinese-speaking fraudsters" language verbatim and NOT upgrade to MSS / MPS attribution.

KAC surfaces eight assumptions with five qualifying caveats; the most load-bearing is A1 (FBI / Group-IB operational independence) which the grader already flagged as a credibility-2 vs. credibility-1 question. If the FBI PSA's full body cites Group-IB as source, the streams collapse to single-source and WEP would drop one step. Operator-origin attribution (A3) — Layui + Chinese comments as operator evidence vs. toolchain inheritance — is the second-most-important caveat. Sensitivity analysis is low brittleness on actor-type (H1 is well-supported diagnostically regardless of state-attribution speculation) but medium on the FBI-Group-IB independence question.
