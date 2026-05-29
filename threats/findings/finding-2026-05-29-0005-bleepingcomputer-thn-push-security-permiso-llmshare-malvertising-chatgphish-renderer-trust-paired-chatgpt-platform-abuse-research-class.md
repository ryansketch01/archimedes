---
finding_id: finding-2026-05-29-0005-bleepingcomputer-thn-push-security-permiso-llmshare-malvertising-chatgphish-renderer-trust-paired-chatgpt-platform-abuse-research-class
created_at: 2026-05-29T16:18:00-04:00
graded_by: grader
grading_run_id: afternoon-20260529-160000
grading_mode: scheduled_brief
test: false

# Core grading (admiralty-grading skill output)
digraph: B3
digraph_layered:
  push_security_llmshare_malvertising_campaign_disclosure_existence: B2     # Push Security primary; BleepingComputer faithful relay; first-citation provisional B vendor research class
  llmshare_chatgpt_share_link_abuse_for_fake_outage_page_delivery: B3       # Push Security single primary; BleepingComputer is pure relay = not independent corroboration
  llmshare_macos_and_windows_payload_via_google_ads_initial_access: B3      # Same posture
  llmshare_vm_detection_behavior_in_windows_sample: B3                       # Push Security observation; not independently verified
  llmshare_iocs_openew_app_domain_and_two_sha256_hashes: B2                  # IOC publication; verifiable via VT lookup if elected
  permiso_chatgphish_vulnerability_disclosure_existence: B2                  # Permiso primary; THN faithful relay; first-citation provisional B vendor research class
  chatgphish_chatgpt_renderer_trust_in_third_party_markdown_links_and_images: B3   # Permiso single primary; THN pure relay = not independent
  chatgphish_image_auto_fetch_exposes_user_ip_user_agent_referer: B3        # Permiso observation; not independently verified
  chatgphish_markdown_link_render_as_clickable_in_response: B3              # Same
  chatgphish_no_cve_assigned_no_openai_response_detail_in_thn_summary: B2  # Procedural absence; verifiable in window
  llmshare_and_chatgphish_distinct_mechanism_classes: A2                    # Plain reading of the two disclosures; structural observation
  paired_timing_14_minute_window_probably_coincidence_neither_vendor_cites_the_other: B3   # Grader-side framing on timing
  cross_cluster_ai_platform_abuse_pattern_of_interest_signal: B3            # Grader-side pattern interpretation; research-class structural framing
  no_actor_attribution_either_disclosure: A1                                 # Verifiable absence in publications
  no_roster_actor_attribution: A1                                            # Verifiable absence
  no_a_and_d_prime_named_target_either_disclosure: A1                       # Verifiable absence
  no_tracked_cve_either_disclosure: A1                                       # Verifiable absence in _index.yaml
  research_class_disclosure_no_itw_named_campaign_on_chatgphish: A1         # Vulnerability-class disclosure, not campaign attribution
  research_class_disclosure_active_malvertising_observed_on_llmshare: A2    # Active commodity-malvertising observed per Push Security; not a roster-tracked campaign
  push_security_first_citation_provisional_b_candidate: B2                   # Per peer class precedent on starting grade
  permiso_security_first_citation_provisional_b_candidate: B2                # Same
  llm_platform_abuse_emerging_attack_surface_pattern: B3                    # Pattern-of-interest structural framing; not analytic claim about specific campaign
  cluster_anchor: B3

digraph_anchor: >
  Cluster digraph B3 anchored on two paired media-tier B-grade
  relays (BleepingComputer Lawrence Abrams byline 2026-05-29
  18:21:36 UTC; The Hacker News institutional byline 2026-05-29
  18:07:12 UTC — 14 minutes apart) of independent vendor-research
  primaries (Push Security on LLMShare malvertising campaign;
  Permiso Security with Andi Ahmeti byline on ChatGPhish renderer-
  trust vulnerability class). Both primaries are NEW first-citation
  candidates for source-grades.yaml as provisional B per the
  established peer class precedent (StepSecurity 2026-05-12, Socket
  2026-05-14, Sysdig 2026-05-14, Zellic 2026-05-14, Aikido Security
  2026-05-12, Ox Security 2026-05-15, Upwind 2026-05-15, Arctic Wolf
  2026-05-28).

  B3 (not B2) holds on the cluster anchor because:
    - Push Security is single-primary on LLMShare. BleepingComputer
      is a faithful relay but is NOT independent corroboration —
      different publisher and different evidence basis tests pass,
      but the "neither cites the other as origin" test fails because
      BleepingComputer explicitly relays Push Security as its origin.
      Single-source veto applies on the LLMShare side.
    - Permiso Security is single-primary on ChatGPhish. THN is a
      faithful relay but is NOT independent corroboration — same
      structural posture. Single-source veto applies on the
      ChatGPhish side.
    - Push Security and Permiso are independent of each other —
      they cover distinct mechanism classes (share-link malvertising
      vs. renderer-trust prompt-injection) and neither references
      the other. They do NOT corroborate each other on a single
      claim, however, because they are reporting on different
      vulnerability/abuse classes. The "two paired vendor-research
      surfacings" framing is a cluster-context pattern, not an
      independent-corroboration of any individual claim.
    - Both Push Security and Permiso are NEW first-citation candidates
      with NO prior Archimedes-corpus track record. Provisional B is
      the conservative starting grade per peer class precedent.
      First-surface methodological positives (Push Security explicit
      payload-identity hedge; Permiso clearly researcher-coined
      ChatGPhish working name per Hard Rule 2 framing) reinforce the
      provisional-B floor but do not lift the starting grade.

  B3 cluster anchor is a monitoring-class grade — meets C3 minimum
  for daily-brief monitoring and weekly synthesis inclusion, but
  does NOT meet B2 minimum for daily-brief action-item or FLASH.
  Disposition: research-pattern context only. NOT a brief-action
  candidate. Eligible for monitoring inclusion if the briefer elects
  to surface the structural-pattern signal under a standing or
  monitoring section.

  Per Hard Rule 2: NO actor attribution is originated. Both vendors
  publish unattributed; both media-tier relays preserve unattributed
  framing. LLMShare and ChatGPhish names are explicit researcher-
  coined working designations, not attributed campaigns. Archimedes
  does NOT extend these to any specific threat actor.

  Per Hard Rule 3 (no exploitation, ever): defender-facing detail is
  included at the level of "share-link rendering for fake-outage
  display" and "Markdown link/image trust + prompt injection"
  without copying any PoC injection payload or payload-delivery
  technique. Anyone needing full technical detail can read the Push
  Security or Permiso primaries directly via URLs in the Sources
  section.

  Per Hard Rule 6 (15-word quote limit): Permiso verbatim quote
  surfaced in raw-signal at 25 words is NOT propagated into this
  finding past the 15-word ceiling. Briefer downstream must apply
  the same discipline.

  Per Hard Rule 8 (Splunk first-party precedence): no targeted
  Splunk query on the LLMShare IOC set (openew[.]app + 2 hashes) per
  PM-001 budget exhaustion and PM-003 collector reasoning. Splunk
  index is dormant for non-archimedes-internal events across all
  prior sweeps (48th consecutive). Trigger 3 cannot fire even if
  hits did exist; IOC set is preserved in the raw-signal for
  downstream vuln-tracker / analyst consumption if a future
  corroborating surface lands.

source_reliability:
  grade: B
  source_name: "BleepingComputer (Push Security LLMShare relay) + The Hacker News (Permiso Security ChatGPhish relay) — paired media-tier relays of independent vendor-research firms"
  source_yaml_id: bleepingcomputer-and-thehackernews-paired
  grade_rationale: >
    Cluster anchor is B (B-grade media-tier relay layer). Both
    BleepingComputer (B per source-grades.yaml) and The Hacker News
    (provisional B since 2026-05-14) are media-tier B-grade sources
    relaying NEW first-citation provisional-B vendor-research
    primaries (Push Security on LLMShare; Permiso Security on
    ChatGPhish). The B-grade cluster anchor is dominated by both the
    media-tier relay layer AND the provisional-B vendor-research-
    primary layer.
  provisional: false   # The B-grade media relays are NOT provisional (BleepingComputer full B; THN provisional B awaiting ratification). The vendor-research primaries underneath ARE first-citation provisional B candidates flagged separately.
  push_security_first_citation_provisional_b_proposal:
    proposed_id: push-security
    proposed_name: "Push Security (browser-security and SaaS-attack-surface research)"
    proposed_grade: B
    proposed_provisional: true
    proposed_provisional_since: 2026-05-29
    proposed_provisional_reason: "First Archimedes-corpus citation via this finding (LLMShare malvertising campaign research — ChatGPT shared-link rendering abused to host fake OpenAI outage notice, redirect to malware disguised as ChatGPT desktop app via Google ads; macOS + Windows samples with VM-detection behavior on Windows side; IOCs published: openew[.]app domain + 2 SHA-256 hashes). Vendor research firm with structured campaign research and named-byline pattern (Push Security institutional byline this surface). Conservative provisional B starting grade per StepSecurity (2026-05-12), Socket (2026-05-14), Sysdig (2026-05-14), Zellic (2026-05-14), Aikido Security (2026-05-12), Ox Security (2026-05-15), Upwind (2026-05-15), Arctic Wolf (2026-05-28) precedent. Methodological positive on first surface: explicit hedge on payload identity ('unclear what payloads are ultimately deployed') and explicit IOC publication. Pending human ratification."
    librarian_action: "Add to source-grades.yaml at provisional B; post source-grade-log.md entry; flag for #actor-review ratification per provisional-B workflow."
  permiso_security_first_citation_provisional_b_proposal:
    proposed_id: permiso-security
    proposed_name: "Permiso Security (cloud-identity-security and AI-platform-abuse research)"
    proposed_grade: B
    proposed_provisional: true
    proposed_provisional_since: 2026-05-29
    proposed_provisional_reason: "First Archimedes-corpus citation via this finding (ChatGPhish vulnerability disclosure — OpenAI ChatGPT response renderer trusts third-party Markdown links and images from summarized web pages, enabling prompt-injection-and-phishing surface via attacker-controlled web pages users ask ChatGPT to summarize; image auto-fetch exposes user IP / User-Agent / Referer; clickable malicious Markdown links and fake system-style security alerts in trusted AI interface; researcher-coined working name ChatGPhish per Hard Rule 2 framing). Vendor research firm with named-analyst byline (Andi Ahmeti). Conservative provisional B starting grade per same peer class precedent as Push Security above. Methodological positive on first surface: ChatGPhish working-name designation clearly researcher-coined (not attributed campaign). Flag: direct retrieval of Permiso primary write-up needed on next collector pass — specific Permiso URL not captured in THN coverage. Pending human ratification."
    librarian_action: "Add to source-grades.yaml at provisional B; post source-grade-log.md entry; flag for #actor-review ratification per provisional-B workflow."

credibility:
  grade: 3
  checklist_passed:
    - possibly_true_single_source_uncorroborated_but_source_is_b_grade_or_better_applies_per_arm_independently_for_push_security_and_for_permiso_security
    - possibly_true_partially_consistent_with_known_ttps_some_elements_novel_chatgpt_share_link_abuse_consistent_with_prior_ai_platform_abuse_patterns_e_g_claude_ai_share_in_finding_2026_05_10_0001
    - possibly_true_technical_claims_plausible_but_not_independently_verifiable_in_window_neither_push_security_nor_permiso_is_corroborated_by_a_second_independent_vendor_research_firm_in_window
  rationale: >
    Possibly True (3) on each individual disclosure (LLMShare and
    ChatGPhish). Each is single-source-from-a-B-grade-source-or-
    better (Push Security and Permiso provisionally B; BleepingComputer
    and THN B-grade relays). Each is partially consistent with prior
    AI-platform-abuse research class (claude.ai/share/ MacSync via
    Trendyol-Albayrak finding-2026-05-10-0001 prior; ChatGPT product
    surface touched in OpenAI TanStack-breach self-disclosure
    finding-2026-05-14-0008 — but those are unrelated product-feature
    surfaces, not direct corroboration). Each is technically plausible
    on its face (Markdown-trust rendering is a known browser-trust-
    boundary pattern; share-link feature abuse for fake-outage-page
    delivery is consistent with prior commodity-malvertising tradecraft)
    but not independently verifiable in window. Cluster anchor at
    credibility 3 (Possibly True) reflects the single-source posture
    for each individual claim.

corroboration:
  independent_sources:
    - push-security-first-citation
    - bleepingcomputer
    - permiso-security-first-citation
    - thehackernews
  independent: false
  independent_test_failed: >
    On LLMShare: Push Security is single-primary; BleepingComputer
    is faithful relay. BleepingComputer cites Push Security as its
    origin. Independence test fails on the "neither cites the other
    as primary origin" criterion. Effective single-source on LLMShare.

    On ChatGPhish: Permiso Security is single-primary; THN is
    faithful relay. THN cites Permiso as its origin. Independence
    test fails on the same criterion. Effective single-source on
    ChatGPhish.

    Push Security and Permiso are independent of each other but cover
    DIFFERENT mechanism classes (share-link malvertising vs. renderer-
    trust prompt-injection). They do NOT corroborate each other on a
    single claim. The "two paired vendor-research surfacings within
    14 minutes" framing is a cluster-context pattern observation, not
    independent corroboration of any individual claim.
  single_source_veto_applied: true
  single_source_veto_layer: llmshare_arm_push_security_only_and_chatgphish_arm_permiso_only
  wep_ceiling_with_veto: likely
  veto_resolution_path: >
    Independent corroboration would arrive from: (a) a second
    independent vendor-research firm publishing on LLMShare or
    ChatGPhish without citing Push Security or Permiso respectively;
    (b) OpenAI publishing a coordinated-disclosure response statement
    on ChatGPhish (would bump Permiso side); (c) Google publishing
    on the malicious Google Ads buyer for the LLMShare surface (would
    bump Push Security side); (d) Mandiant / Volexity / Unit 42 /
    MSTIC / CrowdStrike telemetry on either surface; (e) a CVE
    assignment for ChatGPhish (would procedurally elevate the
    vulnerability-class layer).

first_party_precedence:
  applied: false
  splunk_query_executed: false   # PM-001 PAN-OS sweep exhausted -30d targeted IOC budget for this pre-brief; PM-003 collector reasoning: commodity-malvertising context with no roster/A&D fingerprint, and Splunk dormant for non-archimedes-internal events across 48 consecutive sweeps
  splunk_event_count: null
  splunk_silent_not_contradictory: true
  hard_rule_8_notes: >
    No targeted Splunk query executed for ChatGPT IOC set
    (openew[.]app domain + 2 SHA-256 hashes) per PM-001 budget
    exhaustion and PM-003 collector reasoning. Splunk index dormant
    for non-archimedes-internal events across all prior sweeps.
    Trigger 3 cannot fire even if hits did exist. IOC set preserved
    in raw-signal and below in IOCs Surfaced section for any
    downstream vuln-tracker / analyst consumption if a future
    corroborating surface lands.

single_source_veto_applied: true   # Per arm (LLMShare and ChatGPhish each)
single_source_veto_evaluation: >
  Per-arm single-source veto applies. LLMShare arm: Push Security
  single-primary; BleepingComputer relay = effective single source.
  ChatGPhish arm: Permiso single-primary; THN relay = effective
  single source. WEP ceiling on each arm individually capped at
  "likely." Cluster anchor B3 already reflects the single-source-
  veto outcome.

wep_ceiling: likely
wep_layered:
  push_security_published_llmshare_research_with_iocs_on_2026_05_29: very_likely   # Procedural fact verifiable
  permiso_security_published_chatgphish_research_via_thn_relay_on_2026_05_29: very_likely  # Procedural fact verifiable
  llmshare_campaign_is_actively_distributing_macos_and_windows_malware_via_chatgpt_share_link_abuse_at_some_volume: likely  # Single-source veto applies; capped at likely
  chatgphish_vulnerability_class_exists_in_chatgpt_response_renderer: likely        # Single-source veto applies; capped at likely
  openai_will_address_chatgphish_within_30_days: roughly_even_chance  # Pattern-based; no disclosure timeline detail in THN summary
  google_will_address_malicious_ads_buyer_for_llmshare_within_30_days: roughly_even_chance  # Pattern-based
  third_independent_vendor_research_firm_surface_on_llm_platform_abuse_within_14_days: roughly_even_chance  # Pattern-based; if surfaces, standing-section addition heuristic triggers
  a_and_d_prime_employee_exposure_via_corporate_chatgpt_summarization_or_share_link_consumption_vector_within_30_days: roughly_even_chance  # Structural exposure exists; specific A&D-prime exposure observation requires future surface
  campaign_actor_attribution_within_60_days_for_llmshare: unlikely   # Commodity-malvertising; researchers explicitly unattributed; pattern-based historical low rate of attribution for malvertising-class campaigns
  chatgphish_cve_assignment_within_60_days: roughly_even_chance      # Pattern-based; depends on OpenAI coordination posture

# Cluster metadata
cluster:
  topic: >
    Paired ChatGPT platform-abuse research surfacings, 2026-05-29.
    Two distinct vulnerability / abuse classes affecting OpenAI
    ChatGPT surfaced within 14 minutes of each other via independent
    vendor-research firms with media-tier B-grade relay coverage.
    Item A — Push Security LLMShare malvertising campaign: ChatGPT
    shared-link feature (chatgpt.com/s/) abused to display fake
    OpenAI outage notice on the legitimate chatgpt.com domain;
    victims redirected to malware disguised as ChatGPT desktop app
    via initial Google ads access; macOS and Windows samples; Windows
    sample exhibits VM-detection behavior; Push Security explicit hedge
    on payload identity. Item B — Permiso Security ChatGPhish
    vulnerability: ChatGPT response renderer implicitly trusts
    Markdown links and images from summarized third-party web pages,
    enabling prompt-injection-and-phishing surface via attacker-
    controlled web pages users ask ChatGPT to summarize; auto-image-
    fetch exposes user IP / User-Agent / Referer; live Markdown links
    rendered as clickable in response; potential for fake system-
    style security alerts within trusted AI interface. No actor
    attribution either disclosure. No A&D-prime named target either
    disclosure. No tracked CVE either disclosure. LLMShare and
    ChatGPhish are explicit researcher-coined working names per Hard
    Rule 2 framing — neither is an attributed campaign. Cluster
    anchor B3 is monitoring-class; does not meet B2 brief-action
    threshold.
  cluster_size: 2
  raw_signal_members:
    - raw-2026-05-29-pm-003-chatgpt-platform-abuse-cluster-push-security-llmshare-permiso-chatgphish-research-disclosures
  cluster_arms:
    - arm_id: llmshare
      primary: push-security-first-citation
      relay: bleepingcomputer
      relay_byline: "Lawrence Abrams"
      primary_class: vendor_research_first_citation_provisional_b
      mechanism_class: chatgpt_share_link_feature_abuse_for_fake_outage_page_delivery_with_malvertising_payload_initial_access_via_google_ads
      iocs_count: 4   # 1 domain + 2 file hashes + 1 legitimate-abused-surface marker (chatgpt.com/s/)
      single_source_veto_applied: true
      wep_ceiling_arm: likely
    - arm_id: chatgphish
      primary: permiso-security-first-citation
      relay: thehackernews
      primary_byline: "Andi Ahmeti (Permiso)"
      primary_class: vendor_research_first_citation_provisional_b
      mechanism_class: chatgpt_response_renderer_trust_in_third_party_markdown_links_and_images_from_summarized_web_pages_enabling_prompt_injection_and_phishing
      iocs_count: 0   # Vulnerability-class disclosure, not campaign attribution
      single_source_veto_applied: true
      wep_ceiling_arm: likely
      open_question: "Specific Permiso primary write-up URL not captured in THN coverage; flag for next collector pass to identify and direct-retrieve. OpenAI response detail not in THN summary — coordinated-disclosure timeline unknown."
  attribution_claims: []   # Both vendors publish unattributed; both relays preserve unattributed framing
  pre_brief_sentinel_reference: raw-2026-05-29-pm-000-pre-brief-sweep
  cluster_pattern_observations:
    - observation: paired_timing_14_minute_window_probably_coincidence
      detail: "BleepingComputer 18:21:36 UTC; THN 18:07:12 UTC. 14-minute window. Neither vendor references the other; neither media-tier relay references the other. Probably coincidence on the pairing itself."
      grade: B3
    - observation: cross_cluster_ai_platform_abuse_pattern_of_interest_signal
      detail: "LLM-platform feature surfaces (share links, summarization, prompt rendering) increasingly drawing security-research attention. Both classes have analogues in browser-trust-boundary research 2010-2015 (browser extension stores, autofill abuse, content-script injection) — operationally familiar attack-surface class, new substrate."
      grade: B3
      analyst_sat_kac_optional_candidate: true
    - observation: a_and_d_prime_relevance_indirect_via_employee_use_of_chatgpt_for_summarization_or_share_link_consumption
      grade: B3
      analyst_sat_kac_optional_candidate: true
    - observation: standing_section_consideration_three_surfaces_in_14_days_inflection_point_heuristic
      detail: "If a third surface lands in next 14 days of comparable research class (LLM-platform abuse / prompt injection / AI-platform feature exploitation), briefer / orchestrator may wish to consider adding standing 'AI Platform Security' section to watch-config.yaml per same pattern as existing ad-sector and iran-cyber standing sections. Two surfaces today + prior claude.ai/share/ MacSync 2026-05-10 = three-in-19-days approaching the standing-section heuristic boundary."
      grade: B3
      briefer_orchestrator_handoff: true

# Inclusion eligibility
inclusion:
  eligible_for:
    - daily_brief_monitoring   # B3 meets C3 monitoring minimum
    - weekly_synthesis          # B3 meets C3 weekly synthesis minimum
  ineligible_for:
    - flash                     # B3 below B2 FLASH threshold
    - daily_brief_action        # B3 below B2 action-item threshold
    - actor_profile_update      # No actor named
    - vuln_tracker_handoff      # No CVE assigned either disclosure; commodity-research class; vulnerability-class disclosure for ChatGPhish with no CVE and no vendor-coordinated disclosure timeline in window
  rationale: >
    Cluster meets C3 monitoring inclusion minimum (B3 cluster anchor
    on paired media-tier B-grade relays of provisional-B vendor-
    research first-citations). Does NOT meet B2 action-item or FLASH
    threshold due to per-arm single-source veto on each individual
    claim layer. Disposition is research-pattern-of-interest /
    monitoring class. Briefer may surface under a standing or
    monitoring section if elected; otherwise the finding records the
    structural cluster signal for the corpus and reserves the
    standing-section addition heuristic for a possible third
    comparable surface in the next 14 days.

# Downstream handoff flags
analyst_review_required: false
analyst_review_required_reason: >
  Cluster is research-class disclosure on two distinct vulnerability/
  abuse classes with no actor attribution, no A&D-prime named target,
  no tracked CVE either side. WEP ceiling capped at "likely" per per-
  arm single-source veto. Standard SAT topics not load-bearing here.

  Optional SAT-KAC on cross-cluster AI-platform-abuse pattern-of-
  interest signal (specifically: A&D-prime employee exposure via
  corporate ChatGPT usage for summarization or share-link consumption
  vector) if analyst wants to frame the pattern for briefer's
  monitoring section. Optional SAT-KAC on whether the 14-minute
  pairing is genuinely coincidence or signal of coordinated researcher
  attention to AI-platform surfaces (lower-stakes; useful for trend
  framing).

red_team_review_required: false
red_team_review_required_reason: >
  WEP ceiling caps at "likely" per per-arm single-source veto. Red-
  team review not required per doctrine threshold (>= very_likely).

red_team_review: null
analysis_sections:
  sat_ach: null
  sat_kac: null   # Optional — see analyst_review_required_reason

# Lifecycle
tlp: CLEAR
published_in_briefs: [2026-05-29-afternoon]
retracted: false
retraction_brief_id: null

# Grader-only handoff notes
grader_handoff_notes: >
  Cluster digraph B3 on paired media-tier B-grade relays of
  provisional-B vendor-research first-citations. Monitoring-class
  finding only — NOT brief-action candidate. Two librarian source-
  grade handoffs: add `push-security` and `permiso-security` to
  source-grades.yaml at provisional B with the proposal blocks above;
  post source-grade-log.md entries; flag both for #actor-review
  ratification per provisional-B workflow.

  Briefer-orchestrator handoff: standing-section addition heuristic
  approaching boundary. Two paired surfaces today + prior claude.ai/
  share/ MacSync (finding-2026-05-10-0001) = three-in-19-days. If a
  third comparable surface lands in the next 14 days (LLM-platform
  feature abuse / prompt-injection / AI-platform-rendering trust),
  consider proposing watch-config.yaml standing "AI Platform
  Security" section. Today the briefer may elect to surface this
  cluster under an existing monitoring framing or hold for future
  consolidation.

  Collector handoff for next pass: direct-retrieve the Permiso
  primary write-up URL on ChatGPhish (not captured in THN coverage).
  This would (a) close the source-grade-log review with the primary
  reference, (b) verify the coordinated-disclosure timeline and
  OpenAI response (or lack thereof), and (c) elaborate any IOC or
  PoC-scenario detail that THN's summary omitted.

  IOC summary for librarian iocs.yaml / iocs.md cross-references
  (LLMShare arm only — ChatGPhish has no IOCs):
    - openew[.]app (domain; fake ChatGPT desktop app download portal, Push Security)
    - chatgpt.com/s/ (legitimate-abused-surface marker; flagging for context but NOT a malicious domain — do not propagate as an IOC to block; flagged for awareness only)
    - 7e5b708f6659b1fad3aae7b589a706434fbf21708aeec5af5910189b96e25fef (sha256; macOS sample masquerading as ChatGPT desktop app, Push Security via VirusTotal)
    - 641526a22667a527290aac8c2c0358265d85c83318a7caca7cff28cecc2dbc16 (sha256; Windows sample masquerading as ChatGPT desktop app with VM-detection behavior, Push Security via VirusTotal)
  Provenance for IOCs: push_security_llmshare_research_2026_05_29_via_bleepingcomputer
  Confidence: push_security_research_observed (via VirusTotal verification path on hashes)

source_health_concerns:
  - push_security_new_first_citation_source_health_yaml_entry_recommended_at_failure_count_0_pending_librarian_add_to_source_grades_yaml
  - permiso_security_new_first_citation_source_health_yaml_entry_recommended_at_failure_count_0_pending_librarian_add_to_source_grades_yaml
---

# Paired ChatGPT platform-abuse research surfacings — LLMShare malvertising (Push Security via BleepingComputer) and ChatGPhish renderer-trust vulnerability (Permiso Security via The Hacker News): monitoring-class research pattern

## Summary

Two distinct vulnerability / abuse classes affecting OpenAI ChatGPT surfaced within a 14-minute window on the afternoon of 2026-05-29 via independent vendor-research firms with media-tier B-grade relay coverage. Push Security disclosed an LLMShare malvertising campaign abusing ChatGPT's shared-link feature (chatgpt.com/s/) to display a fake OpenAI outage notice from the legitimate chatgpt.com domain; victims clicking the link see a faked service-status page on a real-OpenAI URL, then are redirected via initial Google ads access to download malware disguised as the ChatGPT desktop application; macOS and Windows samples observed with VM-detection behavior on the Windows side. Permiso Security disclosed a ChatGPhish vulnerability in the ChatGPT response renderer's implicit trust of Markdown links and images from summarized third-party web pages, enabling prompt-injection-and-phishing via attacker-controlled web pages that users ask ChatGPT to summarize; auto-image-fetch exposes user IP / User-Agent / Referer; live Markdown links rendered as clickable elements in the response; potential for fake system-style security alerts in the trusted AI interface. Neither vendor attributes either disclosure to a threat actor; both media-tier relays preserve the unattributed framing. No A&D-prime named target. No tracked CVE on either side. LLMShare and ChatGPhish are explicit researcher-coined working names per Hard Rule 2 framing. Cluster anchor B3 is monitoring-class — meets C3 minimum for daily-brief monitoring and weekly synthesis inclusion, but does NOT meet B2 action-item or FLASH threshold per per-arm single-source veto on each individual claim. Two librarian source-grade handoffs (`push-security` and `permiso-security` at provisional B). Standing-section addition heuristic at three-in-19-days boundary if a third comparable LLM-platform-abuse surface lands in the next 14 days.

## Sources

### BleepingComputer (Push Security LLMShare relay) (bleepingcomputer, digraph B — full B per source-grades.yaml)

- URL: https://www.bleepingcomputer.com/news/security/chatgpt-share-links-abused-to-host-fake-outage-pages-to-deliver-malware/
- Published: 2026-05-29T18:21:36 UTC
- Byline: Lawrence Abrams
- Underlying primary: Push Security (pushsecurity.com/blog/llmshare-malvertising-campaign — NEW first-citation provisional B)
- Key claim: Push Security identifies the LLMShare campaign using the ChatGPT shared-link feature to display a fake OpenAI outage notice on the legitimate chatgpt.com domain; victims redirected to malware disguised as ChatGPT desktop app; macOS + Windows samples; Windows sample exhibits VM-detection behavior. Researchers note: "While it is unclear what payloads are ultimately deployed, earlier campaigns abusing AI platform sharing features have distributed infostealers" — explicit hedge preserved verbatim by BleepingComputer.

### The Hacker News (Permiso Security ChatGPhish relay) (thehackernews, digraph B — provisional B per source-grades.yaml since 2026-05-14)

- URL: https://thehackernews.com/2026/05/chatgphish-vulnerability-turns-chatgpt.html
- Published: 2026-05-29T18:07:12 UTC
- Byline: The Hacker News (institutional)
- Underlying primary: Permiso Security (Andi Ahmeti byline; specific URL not captured in THN piece — flagged for collector next-pass direct retrieval)
- Key claim: Permiso Security identifies the ChatGPhish vulnerability where the ChatGPT response renderer implicitly trusts Markdown links and image URLs from summarized third-party web pages. Attackers can append malicious Markdown to web pages users ask ChatGPT to summarize, triggering auto-image-fetch that exposes user IP / User-Agent / Referer, rendering live clickable Markdown links, and delivering fake system-style security alerts or QR codes within the trusted AI interface. ChatGPhish is a researcher-coined working name (Permiso) for the vulnerability class.

## Technical detail

### Item A — LLMShare malvertising campaign (Push Security)

**Mechanism (per Push Security via BleepingComputer):** Threat actors abuse ChatGPT's content-sharing feature (`chatgpt.com/s/` shared-link URLs that render custom HTML/CSS content) to display a fake OpenAI outage notice from the legitimate `chatgpt.com` domain. Victims click the link → see a faked OpenAI service-status page on a real-OpenAI URL → are redirected to download malware disguised as the ChatGPT desktop application. Initial victim access is via Google ads.

**Malware behavior (per BleepingComputer summary of Push Security):** The Windows sample "attempted to detect virtual machines through command execution." Final payload not explicitly characterized — Push Security hedge preserved by BleepingComputer.

**No actor attribution.** Push Security publishes IOCs and mechanism analysis without attributing to a named threat actor. BleepingComputer relay preserves the unattributed framing.

**No A&D / aerospace / defense / DIB sector targeting** named by Push Security or BleepingComputer. Mass-malvertising distribution targets general internet users via Google ads.

**Defensive recommendations (per Push Security via BleepingComputer):**
- Verify ChatGPT downloads only from official OpenAI sources
- Exercise caution with Google sponsored ads
- Implement application allowlisting
- Monitor for suspicious outage claims from legitimate domains

### Item B — ChatGPhish vulnerability (Permiso Security)

**Mechanism (per Permiso Security via THN):** Vulnerability in OpenAI ChatGPT that exploits the platform's implicit trust in Markdown links and images from summarized web pages. The chatgpt.com response renderer trusts Markdown links and Markdown image URLs that originated from a third-party page the assistant has just summarized. Attackers can:

- Append malicious Markdown payloads to web pages users ask ChatGPT to summarize
- Trigger ChatGPT to auto-fetch attacker-hosted images, exposing user IP / User-Agent / Referer details
- Render malicious Markdown links as live, clickable elements in the response
- Deliver fake system-style security alerts or QR codes within the trusted AI interface

**Permiso codename:** ChatGPhish (Permiso-coined working name for the vulnerability class).

**No actor attribution.** Permiso publishes the vulnerability without attributing to a named threat actor. THN does not extend attribution.

**No A&D / aerospace / defense / DIB sector targeting** named. The vulnerability is general-purpose against any ChatGPT user.

**OpenAI response:** not detailed in the THN piece. Permiso disclosure-coordination timeline not specified. Flagged for collector next-pass direct retrieval of Permiso primary write-up to resolve.

**No IOCs published.** ChatGPhish is a vulnerability-class disclosure (mechanism + research scenario), not a campaign attribution.

### Cross-cluster analysis

**Paired-timing observation:** Two independent vendor-research firms surfaced ChatGPT-platform-abuse research in the same 14-minute window. Probably coincidence — neither references the other; the mechanisms are distinct (share-link malvertising vs. renderer-trust prompt-injection); neither vendor names the other in coordination. But the cluster-timing is a structural signal worth noting.

**LLM-platform abuse pattern of interest:** LLM-platform feature surfaces (share links, summarization, prompt rendering) are increasingly drawing security-research attention. Both classes have analogues in browser-trust-boundary research from 2010-2015 (browser extension stores, autofill abuse, content-script injection) — operationally familiar attack-surface class, new substrate.

**A&D-prime relevance is INDIRECT:** corporate employees using ChatGPT for summarization or share-link consumption could surface either class as an attack vector, but neither has named A&D-prime targeting.

**Standing-section addition heuristic at boundary.** If a third surface lands in the next 14 days of comparable research class (LLM-platform abuse / prompt injection / AI-platform feature exploitation), the briefer / orchestrator may wish to consider adding a standing "AI Platform Security" section to `watch-config.yaml` per the same pattern as the existing `ad-sector` and `iran-cyber` standing sections. Two surfaces today + prior `claude.ai/share/` MacSync (finding-2026-05-10-0001) = three-in-19-days approaching the standing-section heuristic boundary.

## IOCs surfaced

**LLMShare arm only (ChatGPhish has no IOCs — vulnerability-class disclosure).**

Provenance: Push Security LLMShare research 2026-05-29 via BleepingComputer relay. Confidence: push_security_research_observed (via VirusTotal verification path on hashes).

- `openew[.]app` (domain) — fake download portal masquerading as OpenAI ChatGPT desktop-app download page
- `chatgpt.com/s/` (legitimate-abused-surface marker; not a malicious domain — flagged for awareness only, do NOT propagate as an IOC to block)
- `7e5b708f6659b1fad3aae7b589a706434fbf21708aeec5af5910189b96e25fef` (sha256) — macOS sample masquerading as ChatGPT desktop app
- `641526a22667a527290aac8c2c0358265d85c83318a7caca7cff28cecc2dbc16` (sha256) — Windows sample masquerading as ChatGPT desktop app; observed VM-detection behavior

**Splunk first-party check:** No targeted Splunk query executed for this IOC set per PM-001 budget exhaustion and PM-003 collector reasoning (commodity-malvertising context with no roster/A&D fingerprint; Splunk index dormant for non-archimedes-internal events across 48 consecutive sweeps).

## Relationship to existing findings

**No prior surface of LLMShare or ChatGPhish in the Archimedes corpus.** This is the first finding promotion on either disclosure.

- **Cross-reference: prior AI-platform-share-link research class.** `finding-2026-05-10-0001` (claude.ai/share/ MacSync via Trendyol-Albayrak) is the corpus baseline on AI-platform-share-link feature abuse, on a different vendor product (Anthropic Claude) and a different malware family (MacSync). The mechanism class (share-link feature abuse) is corpus-recurrent.
- **Cross-reference: ChatGPT product surface touched in prior finding.** `finding-2026-05-14-0008` is OpenAI TanStack-breach self-disclosure — unrelated product-feature surface, NOT direct corroboration on either LLMShare or ChatGPhish. No conflation.
- **Standing-section addition heuristic:** Three-in-19-days approaching boundary. Briefer-orchestrator handoff flagged in grader_handoff_notes.

## Open questions for analyst

1. **Optional SAT-KAC on cross-cluster AI-platform-abuse pattern-of-interest signal.** Specifically: A&D-prime employee exposure via corporate ChatGPT usage for summarization or share-link consumption vector. Useful for framing the briefer's monitoring-section disposition.

2. **Optional SAT-KAC on paired-timing coincidence vs. coordinated-attention signal.** Whether the 14-minute pairing is genuinely coincidence or signal of coordinated researcher attention to AI-platform surfaces. Lower-stakes; useful for trend framing.

3. **Collector next-pass direct-retrieval of Permiso primary write-up URL on ChatGPhish.** Would (a) close source-grade-log review with primary reference, (b) verify coordinated-disclosure timeline and OpenAI response (or lack thereof), and (c) elaborate any IOC or PoC-scenario detail THN's summary omitted.

4. **Hard Rule 2 attribution void preservation.** Both vendors publish unattributed; both media-tier relays preserve unattributed framing. LLMShare and ChatGPhish are researcher-coined working names. Analyst should not extend these to any specific threat actor without an A/B-grade source making the bind.
