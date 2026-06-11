---
id: finding-2026-06-11-0010
finding_id: finding-2026-06-11-0010-securityweek-securityaffairs-blackfog-onyxc2-maas-credential-stealer-250-monthly-210-targets-zero-vt-detections
title: "OnyxC2 MaaS credential-stealer — BlackFog research; $250/month standard / $500/month HVNC premium / $6,000 source-code purchase; 210+ application targets including 95+ Chromium and 14+ Gecko extensions with dedicated 2FA + password manager modules; AES-256 encrypted payloads + DLL sideloading (NVIDIA-library masquerade) + in-memory execution + legitimate-signature wrapper; zero VirusTotal detections across 71 engines on initial upload (per BlackFog 2026-05-30); no A&D direct tie; MaaS commoditization watchlist signal"
date: 2026-06-11
created_at: 2026-06-11T17:15:00-04:00
graded_by: grader
grading_run_id: afternoon-20260611-160000
grading_mode: scheduled_brief
test: false
status: graded

# ============================================================================
# Core grading (admiralty-grading skill output) — LAYERED
# ============================================================================
digraph: B2
admiralty_grade: B2
digraph_layered:
  blackfog_originating_research_provenance: B2  # SecurityWeek + Security Affairs two B-grade publisher-independent relays of same BlackFog vendor research; BlackFog provisional B (first dedicated-id surface)
  onyxc2_maas_pricing_250_monthly_500_premium_hvnc_6000_source: B2  # Two B-grade publisher-independent relays of BlackFog
  onyxc2_target_list_210_plus_applications_37_chromium_8_gecko_browsers_95_chromium_14_gecko_extensions_17_crypto_wallets: B2  # Two B-publisher relays of BlackFog
  onyxc2_dedicated_2fa_module_6_extensions_plus_password_manager_module_5_extensions: B2  # Two B-publisher relays
  onyxc2_evasion_aes_256_encrypted_payloads_dll_sideloading_nvidia_library_masquerade_in_memory_execution_legitimate_signature_wrapper: B2  # Two B-publisher relays of BlackFog
  onyxc2_zero_vt_detections_71_engines_2026_05_30_initial_upload: B2  # BlackFog vendor attestation through two B-publisher relays
  onyxc2_lure_installers_fineprint_systemsettings_fake_windows_updates_fling_standalone_gaming: B2  # Two B-publisher relays
  onyxc2_persistence_for_prolonged_foothold_credential_theft_class: B2  # BlackFog vendor characterization
  no_actor_named_at_any_in_window_source: A1  # Verifiable absence (MaaS class — actor pool is heterogeneous customer base; only vendor-author identification is the OnyxC2 development team)
  no_ad_prime_named_as_victim: A1  # Verifiable absence
  maas_commoditization_threat_signal_for_dib_workforce_credential_theft_indirect: B3  # Structural inference
  cluster_anchor: B2

digraph_anchor: >
  Cluster anchored at B2. SecurityWeek (B ratified) + Security
  Affairs (B provisional) are TWO publisher-independent B-grade
  media relays of the SAME BlackFog vendor research. Independence
  test PASSES at PUBLISHER layer (different publishers, neither
  cites the other per raw-signal pm-005 verification). Independence
  test FAILS at substantive evidence-basis layer per skill Step 4
  "both rely on the same vendor's telemetry" rule — BlackFog
  vendor research is the sole originating evidence basis. The two
  B-grade relays combined count as ONE effective source at the
  substantive evidence-basis layer. BlackFog is provisional B
  first dedicated-id surface; librarian handoff candidate.

  CREDIBILITY CHECKLIST:
    - Grade 1 (Confirmed) FAILS — single-vendor through dual-
      publisher relay; no second-vendor independent attestation of
      OnyxC2 technical detail or pricing this sweep.
    - Grade 2 (Probably True) PASSES: consistent with established
      MaaS commoditization TTP pattern (Lumma stealer / RedLine /
      Vidar / Raccoon precedent class on credential-stealer-as-a-
      service); no contradicting A/B-grade source; technical
      claims internally coherent (AES-256 + DLL sideloading +
      in-memory execution + legitimate-signature wrapper are
      standard evasion patterns for modern credential-stealer
      class).

  Hard Rule 2 binding constraint: NOT TRIGGERED — no actor
  attribution at any in-window source. MaaS class: actor pool is
  heterogeneous customer base; only the OnyxC2 development team
  is vendor-author-identifiable.

  Hard Rule 3 binding constraint: PRESERVED — mechanism class
  preserved at architectural-identifier level (DLL sideloading
  via NVIDIA-library masquerade, in-memory execution class,
  legitimate-signature wrapper application class). NO PoC code,
  NO payload bytes, NO step-by-step compromise guidance copied.
  Defender-utility-class information for endpoint detection
  rule writing (DLL load anomaly, signed-binary masquerade
  audit, browser-extension manifest monitoring).

  Hard Rule 8 binding constraint: -7d@d first-party Splunk query
  on OnyxC2 + MaaS + credential-stealer adjacent keywords: zero
  substantive first-party matches. Per Hard Rule 8: silence is
  not disconfirming. First-party precedence does NOT apply.

source_reliability:
  grade: B
  source_name: "SecurityWeek (B ratified) + Security Affairs (B provisional) two publisher-independent relays of BlackFog (provisional B) vendor research"
  source_yaml_id: securityweek
  grade_rationale: >
    SecurityWeek ratified B per source-grades.yaml. Security
    Affairs provisional B (2026-05-29 first dedicated-id surface).
    BlackFog provisional B starting grade per vendor-research-
    class precedent (anti-data-exfiltration vendor with sustained
    threat-intelligence-research publication track record). First
    Archimedes-corpus dedicated source ID for BlackFog via this
    finding. Librarian handoff for source-grades.yaml addition.
  provisional: false
  cluster_secondary_sources:
    - source_yaml_id: securityaffairs
      grade: B
      provisional: true
      provisional_since: 2026-05-29
      role: independent_publisher_relay_of_blackfog_vendor_research
    - source_yaml_id: blackfog-research
      grade: B
      provisional: true
      provisional_since: 2026-06-11
      provisional_72h_clock_expires: 2026-06-14T17:15:00-04:00
      grade_rationale: "BlackFog is established anti-data-exfiltration vendor with sustained threat-intelligence-research track record. First Archimedes-corpus dedicated source ID via this finding. Conservative provisional B starting grade per Tier-2 vendor-research class. Librarian handoff. 72h ratification clock to 2026-06-14T17:15:00-04:00."
      role: originating_vendor_research_on_onyxc2_maas_not_directly_retrieved

credibility:
  grade: 2
  checklist_passed:
    - probably_true_consistent_with_maas_commoditization_ttp_pattern_lumma_redline_vidar_raccoon_precedent_class
    - probably_true_no_contradicting_a_b_grade_source
    - probably_true_technical_claims_internally_coherent_aes256_dll_sideloading_in_memory_execution_legitimate_signature_wrapper_standard_evasion_class
  rationale: >
    Two B-grade publisher-independent relays of BlackFog vendor
    research. Independence at substantive evidence-basis layer
    fails per skill Step 4 (both rely on same vendor telemetry).
    Conservative B2 anchor.

corroboration:
  independent_sources:
    - securityweek
    - securityaffairs
    - blackfog-research
  independent: partial
  independent_at_publisher_layer: true
  independent_at_substantive_evidence_basis_layer: false
  test_partial: "Publisher-independent yes; evidence-basis-independent no per skill Step 4 vendor-telemetry shared-origin test"

first_party_precedence:
  applied: false
  splunk_evidence: null
  splunk_query_run: "Combined -7d@d Splunk query on PM-cycle IOC superset; zero substantive first-party matches; Hard Rule 8 silence-is-not-disconfirming."

single_source_veto_applied: true
single_source_veto_detail: >
  APPLIES on substantive operational claims (pricing tiers,
  target list, evasion techniques, zero-VT-detections claim,
  lure-installers list). All trace to BlackFog vendor research
  through dual-publisher relay; single-vendor evidence basis.
  WEP caps at "likely" on substantive operational claims.

wep_ceiling: likely
wep_layered:
  blackfog_origin_provenance_of_onyxc2_research: very_likely  # Two B-publisher independence at publisher layer
  onyxc2_maas_pricing_250_monthly_500_premium_hvnc_6000_source: likely
  onyxc2_target_list_210_plus_applications: likely
  onyxc2_zero_vt_detections_71_engines_initial_upload: likely
  onyxc2_evasion_aes256_dll_sideloading_nvidia_masquerade_in_memory_legitimate_signature_wrapper: likely
  no_actor_named: very_likely  # A1 verifiable absence
  no_ad_prime_named_victim: very_likely  # A1 verifiable absence
  maas_commoditization_indirect_dib_workforce_credential_theft_signal: likely  # Structural

inclusion:
  eligible_for:
    - daily_brief_monitoring   # B2 clears B2 minimum; monitoring-tier given MaaS commoditization signal
    - weekly_synthesis         # Pattern across credential-stealer MaaS commoditization
inclusion_eligibility: yes
inclusion_rationale: >
  B2 anchor + WEP "likely" on substantive operational claims.
  NOT eligible for daily_brief_action — no A&D-prime victim,
  no actor attribution, no actionable defender step beyond
  generic credential-stealer detection class. Monitoring-tier
  + weekly-synthesis appropriate.

# ============================================================================
# Hard Rule 2 — Attribution preserved (NULL)
# ============================================================================
attribution: null
attribution_claims:
  - claimed_vendor: BlackFog (anti-data-exfiltration vendor research)
    claim_type: vendor_research_origination_on_maas_class
    claim: "OnyxC2 enterprise-grade MaaS credential-stealer sold $250/month standard, $500/month HVNC premium, $6,000 source-code purchase; 210+ application targets including 95 Chromium + 14 Gecko extensions (6 dedicated 2FA + 5 password manager); zero VirusTotal detections across 71 engines on initial upload 2026-05-30"
    claimed_by_sources:
      - blackfog-research  # primary, not directly retrieved
      - securityweek      # publisher relay
      - securityaffairs   # publisher relay
    independent_corroboration: false  # Single-vendor through dual-publisher relay
    archimedes_attribution_origination_check: pass_per_hard_rule_2_vendor_research_preserved_with_citation
attribution_rationale: >
  No actor attribution at any in-window source. MaaS class:
  actor pool is heterogeneous customer base of OnyxC2; only the
  OnyxC2 development team is vendor-author-identifiable per
  BlackFog research, NOT named in B-grade relay tier.

# ============================================================================
# Vulnerability + product identifiers
# ============================================================================
cves: []
affected_products:
  - 37_Chromium_8_Gecko_browsers
  - 95_Chromium_14_Gecko_extensions_including_6_dedicated_2FA_5_password_managers
  - 17_crypto_wallets
  - 11_FTP_clients
  - 5_email_clients
  - VPN_RDP_messaging_gaming_clients
affected_vendors: []

# ============================================================================
# IOCs surfaced
# ============================================================================
iocs:
  malware:
    - name: OnyxC2
      class: maas_credential_stealer
      pricing:
        standard: $250/month
        hvnc_premium: $500/month
        source_code_purchase: $6000
      target_count: 210+ applications
      target_classes:
        - 37_Chromium_8_Gecko_browsers
        - 95_Chromium_extensions_14_Gecko_extensions
        - 6_dedicated_2FA_extensions
        - 5_password_manager_extensions
        - 17_crypto_wallets
        - 11_FTP_clients
        - 5_email_clients
        - VPN_RDP_messaging_gaming_clients
      evasion:
        - AES_256_encrypted_payloads
        - DLL_sideloading_NVIDIA_library_masquerade
        - in_memory_execution
        - legitimate_signature_wrapper_application
      vt_posture_per_blackfog: zero_detections_71_engines_2026_05_30_initial_upload
      lure_installers:
        - FinePrint
        - SystemSettings
        - fake_Windows_updates
        - Fling_Standalone_gaming
      persistence: designed_for_prolonged_foothold_credential_theft
      defender_pivot_classes:
        - dll_load_anomaly_audit_on_nvidia_library_path_masquerade
        - signed_binary_masquerade_audit_for_legitimate_wrapper_class
        - browser_extension_manifest_monitoring_on_high_risk_browsers
        - in_memory_execution_detection_via_memory_scanner_or_amsi
ioc_count: 1  # OnyxC2 family identification
iocs_summary: >
  No hash, domain, or IP IOCs in B-grade relay tier. BlackFog
  primary research likely carries hash + infrastructure IOCs
  but was NOT directly retrieved this sweep.

# ============================================================================
# Cluster metadata
# ============================================================================
cluster:
  topic: "OnyxC2 MaaS credential-stealer (BlackFog vendor research) — MaaS commoditization watchlist signal; no A&D direct"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-06-11-pm-005   # subset (1 of 4 cybercrime cluster components)
  related_findings: []

# ============================================================================
# Inclusion + handoffs
# ============================================================================
analyst_review_required: false
analyst_review_rationale: "WEP ceiling 'likely' on substantive operational claims (single-source veto). No SAT-class invocation trigger conditions."

red_team_review_required: false
red_team_review_rationale: "WEP ceiling 'likely' does not meet red-team invocation floor."

red_team_review: null
analysis_sections:
  sat_ach: null
  sat_kac: null

tlp: CLEAR
published_in_briefs: [2026-06-11-afternoon]
retracted: false

source_grade_revision_proposed:
  - source_yaml_id: blackfog-research
    proposed_action: add_new_provisional_source_entry
    proposed_grade: B
    proposed_provisional_until: 2026-06-14T17:15:00-04:00
    rationale: "BlackFog is established anti-data-exfiltration vendor with sustained threat-intelligence-research publication track record. First Archimedes-corpus dedicated source ID via this finding. Conservative provisional B starting grade per Tier-2 vendor-research class. Librarian handoff. 72h ratification clock."
---

# OnyxC2 MaaS credential-stealer — BlackFog vendor research; commoditization watchlist signal

## Summary

BlackFog (provisional B vendor research, first Archimedes-corpus dedicated source ID) reports a new MaaS credential-stealer dubbed OnyxC2, relayed independently by SecurityWeek (B) and Security Affairs (B provisional). Pricing tiers: $250/month standard, $500/month HVNC premium, $6,000 source-code purchase. Target footprint: 210+ applications including 37 Chromium + 8 Gecko browsers; 95 Chromium + 14 Gecko extensions (including 6 dedicated 2FA modules + 5 password manager modules); 17 crypto wallets; 11 FTP clients; 5 email clients; plus VPN / RDP / messaging / gaming clients. Evasion: AES-256 encrypted payloads + DLL sideloading via NVIDIA-library masquerade + in-memory execution + legitimate-signature wrapper application. Zero VirusTotal detections across 71 engines on initial upload (BlackFog attestation 2026-05-30). Bundled lure installers include FinePrint, SystemSettings, fake Windows updates, Fling-Standalone gaming installers. Designed for prolonged foothold; converts one workstation into ongoing visibility into browsers + password managers + 2FA tokens + email + FTP + VPN credentials + crypto wallets. No actor attribution; no A&D-prime named victim. MaaS commoditization watchlist signal only.

## Sources

### SecurityWeek (securityweek, B)

- URL: https://www.securityweek.com/onyxc2-stealer-offers-cybercriminals-enterprise-grade-theft-for-250-a-month/
- Published: 2026-06-11 13:00 EDT
- Key claim: BlackFog research origination; $250 standard pricing; 210+ app target list; evasion details; persistence framing.

### Security Affairs (securityaffairs, B provisional)

- URL: https://securityaffairs.com/193523/malware/onyxc2-malware-as-a-service-offers-enterprise-grade-data-theft.html
- Published: 2026-06-11 14:22 EDT
- Key claim: Same BlackFog research origination; identical pricing; evasion details; persistence framing (publisher-independent at publisher layer; same evidence basis at substantive layer).

### BlackFog (blackfog-research, B provisional, NOT directly retrieved)

- Status: primary not directly retrieved this sweep
- Role: originating vendor research on OnyxC2 MaaS class

## A&D / DIB relevance

- **No A&D-prime named:** verifiable absence.
- **MaaS commoditization signal (B3, indirect):** lower barrier for credential-theft against any enterprise including DIB workforce; standard credential-stealer-class defender posture (signed-binary masquerade audit, DLL-load anomaly detection, browser-extension manifest monitoring, in-memory execution detection) applies.

## Defender pivots

- DLL load anomaly audit on NVIDIA-library-path masquerade
- Signed-binary masquerade audit for legitimate-wrapper class
- Browser-extension manifest monitoring (especially 2FA + password manager extension categories)
- In-memory execution detection via memory scanner / AMSI
- Lure installer file-name pattern matching (FinePrint, SystemSettings, fake Windows updates, Fling-Standalone)

## IOCs surfaced

- **OnyxC2** family identification (MaaS credential-stealer class)
- **No hash, domain, or IP IOCs** in B-grade relay tier. BlackFog primary likely carries hash + infrastructure IOCs but was NOT directly retrieved this sweep.

## Open questions for analyst

None at this confidence tier. Watch signal for monitoring-tier and weekly-synthesis credential-stealer commoditization pattern.
