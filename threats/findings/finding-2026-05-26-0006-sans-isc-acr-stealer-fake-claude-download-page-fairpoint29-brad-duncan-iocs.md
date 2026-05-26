---
finding_id: finding-2026-05-26-0006-sans-isc-acr-stealer-fake-claude-download-page-fairpoint29-brad-duncan-iocs
created_at: 2026-05-26T08:00:00-04:00
graded_by: grader
grading_run_id: morning-20260526-080000
grading_mode: scheduled_brief
test: false

# Core grading (admiralty-grading skill output)
digraph: B3
digraph_layered:
  sans_isc_brad_duncan_diary_publication: B3   # Single B-grade defender diary, named handler
  acr_stealer_windows_infostealer_family_malpedia_class: B2   # Family-class consistent with Malpedia canonical record
  fairpoint29_com_fake_claude_download_landing_page: B3   # IOC published with high diary-author confidence; single-source
  primemetricsa_com_download_domain: B3
  6ryuefl_creativecommunityinfo_art_host_specific_download_domain: B3
  i_ibb_co_legitimate_service_abused_for_payload_staging: B3
  yw_enhanceblabber_cc_c2_domain: B3
  3_sha256_hashes_zip_powershell_image_file: B3
  malvertising_via_google_ads_delivery_vector: B3
  url_concealment_via_sites_google_com_initial_redirect: B3
  ai_brand_impersonation_anthropic_claude_lure_pattern: B3
  no_actor_attribution_per_brad_duncan: A1
  no_ad_prime_named: A1
  splunk_first_party_zero_hits_on_fairpoint29_primemetricsa_enhanceblabber_creativecommunityinfo_acr_stealer_hashes: A1
  cluster_anchor: B3

digraph_anchor: >
  Cluster digraph B3 anchored on SANS Internet Storm Center diary
  33018 (Brad Duncan named-handler byline, 2026-05-26 00:02 EDT
  in-window) — defender-tier IOC publication on an ACR Stealer
  Windows infostealer delivery chain via fake Claude (Anthropic)
  download landing pages. SANS ISC is graded B per source-grades.yaml
  ("Quality research but community-contributed"); Brad Duncan is a
  long-standing malware-analysis handler byline with a multi-year
  diary track record. Single-source publication; six IOCs published
  (one fake-page domain, three download/staging domains, one C2
  domain, three SHA-256 hashes — defanged enumeration below). No
  threat actor attribution — ACR Stealer is commodity infostealer
  deployed by multiple criminal operators. Credibility 3 (Possibly
  True / single-source uncorroborated, B-grade source) — the IOCs
  are immediately actionable for defender blocklist deployment but
  the cluster lacks independent corroboration of the specific
  delivery-chain narrative. Single-source veto applies — WEP ceiling
  capped at "likely". Defender-utility-of-IOCs is independent of
  attribution-layer corroboration: the six IOCs warrant promotion
  to `_master-index.yaml` for blocklist deployment regardless of
  the cluster's attribution-layer grade.

source_reliability:
  grade: B
  source_name: "SANS Internet Storm Center diary (Brad Duncan handler byline)"
  source_yaml_id: sans-isc
  grade_rationale: >
    Pre-assigned B per source-grades.yaml ("Quality research but
    community-contributed"). Brad Duncan is a long-standing malware-
    analysis handler byline with a multi-year diary track record on
    commodity-malware infrastructure analysis (notably the regularly
    published "Wireshark Quizes" and traffic-analysis diaries). The
    diary format is defender-tier IOC publication — IOCs published
    are typically obtained via the handler's own sandbox-execution +
    pcap-analysis workflow, not from external attribution claims.
  provisional: false

credibility:
  grade: 3
  checklist_passed:
    - possibly_true_single_source_uncorroborated_b_grade_or_better
    - possibly_true_partially_consistent_with_known_ttps_some_elements_novel
    - possibly_true_technical_claims_plausible_but_not_independently_verifiable
  rationale: >
    Single-source uncorroborated, B-grade source. ACR Stealer family
    is documented on Malpedia canonical record (Windows infostealer
    class). Malvertising via Google Ads + URL concealment via
    sites.google.com + fake software-download landing pages on
    attacker-controlled domains is a well-documented commodity-
    delivery pattern across many infostealer campaigns. AI brand
    impersonation (Anthropic / Claude) as lure vector is a NEW
    surface in the corpus — first ACR Stealer + fake-Claude-page
    combination documented. Technical claims internally coherent.
    Defender-tier diary is typically a single-handler observation
    with sandbox-execution / pcap analysis; independent corroboration
    of THIS specific campaign chain would require a second sandbox
    operator (e.g., ANY.RUN, Hatching Triage, Joe Sandbox) or vendor
    (Palo Alto, CrowdStrike, Sophos, Microsoft) publishing the same
    IOCs or chain.

corroboration:
  independent_sources:
    - sans-isc
  independent: false
  test_passed: >
    Single-source. Brad Duncan diary is the only in-window
    publication on this specific ACR Stealer + fake-Claude-page
    chain. ACR Stealer family Malpedia record is canonical reference
    (not corroboration of this specific campaign). No other vendor
    or sandbox-operator publication of the same IOCs in window.
    Corroboration test FAILS on independence. Single-source veto
    applies on the campaign-narrative layer.

first_party_precedence:
  applied: false
  splunk_evidence: null
  splunk_query_executed: >
    14h pre-brief sentinel sweep included fairpoint29, primemetricsa,
    enhanceblabber, creativecommunityinfo, ACR Stealer, and the
    three SHA-256 hashes across defenseclaw_local and archimedes
    indices. Zero events returned. 24h grader-run Splunk corroboration
    query likewise zero. Per Hard Rule 8, silence is not
    disconfirming. The defender-utility of the IOCs is independent
    of first-party-IOC hit status — operator may deploy the
    blocklist preemptively given the diary publication date is
    today and the campaign may not yet have reached the operator
    estate at observation depth.

single_source_veto_applied: true
single_source_veto_rationale: >
  Single-source SANS ISC diary on the campaign-narrative layer.
  WEP ceiling capped at "likely". Independent corroboration paths:
  ANY.RUN / Hatching Triage / Joe Sandbox public sandbox submissions
  on the same hashes; Palo Alto Unit 42 / CrowdStrike / Sophos /
  Microsoft Defender / Google TAG publishing parallel campaign
  observations on the AI-brand-impersonation lure vector; abuse.ch
  URLhaus / ThreatFox tagging of the published domains.

wep_ceiling: likely
wep_layered:
  acr_stealer_family_class_malpedia_canonical: very_likely  # family-class reference
  fairpoint29_com_fake_claude_landing_page_observed: likely
  primemetricsa_com_download_domain_observed: likely
  6ryuefl_creativecommunityinfo_art_host_specific_download_observed: likely
  i_ibb_co_legitimate_service_abused_for_payload_staging_observed: likely
  yw_enhanceblabber_cc_c2_domain_observed: likely
  3_sha256_hashes_in_acr_stealer_chain_observed: likely
  malvertising_google_ads_url_concealment_sites_google_com_delivery_pattern: likely
  ai_brand_impersonation_anthropic_claude_as_lure_vector: likely
  no_named_threat_actor: not_a_predictive_claim

inclusion:
  eligible_for:
    - daily_brief_monitoring
    - weekly_synthesis
    - ioc_master_index           # Defender-utility of the 6 IOCs justifies _master-index.yaml promotion regardless of attribution layer
  not_eligible_for:
    - flash                       # FLASH-POLICY: commodity infostealer, no named actor, no A&D-prime named, no CVE — no FLASH trigger fires
    - daily_brief_action          # Defender-tier IOC publication, monitoring-tier rather than action-tier given commodity-infostealer class
    - actor_profile_update        # No actor attribution; no roster actor to update
  inclusion_rationale: >
    B3 cluster anchor → eligible for daily brief monitoring section
    per INTEL-GRADING.md thresholds. The 6 IOCs are immediately
    actionable for defender blocklist deployment; recommend
    librarian regenerate _master-index.yaml after this run to
    include the new IOCs.

# Cluster metadata
cluster:
  topic: "SANS ISC diary 33018 (Brad Duncan): ACR Stealer Windows infostealer delivered via fake Claude (Anthropic) download landing page on fairpoint29[.]com + Google Ads malvertising + sites.google.com URL concealment; 6 IOCs (5 domains incl. legitimate-service-abuse alert + 3 SHA-256 hashes) published for defender blocklist deployment"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-05-26-am-006-sans-isc-acr-stealer-fake-claude-download-page-brad-duncan-iocs-fairpoint29
  related_actors: []
  related_vulnerabilities: []
  related_campaigns:
    - acr-stealer-fake-claude-anthropic-download-page-2026-05-26
  attribution_claims: []   # No actor attribution per Brad Duncan; Hard Rule 2 keeps empty

# IOCs surfaced
iocs_surfaced:
  - type: domain
    value: fairpoint29[.]com
    context: "Fake Claude (Anthropic) download landing page; hosts OS-aware lure displaying platform-specific malware download instructions"
    confidence: high
    source_attribution: "SANS ISC diary 33018 (Brad Duncan, 2026-05-26 00:02 EDT)"
    first_observed: 2026-05-26
    related_malware: ACR Stealer
    actor_id: null
    defanged: true
  - type: domain
    value: primemetricsa[.]com
    context: "Download domain in ACR Stealer delivery chain via fake Claude landing page on fairpoint29.com"
    confidence: high
    source_attribution: "SANS ISC diary 33018 (Brad Duncan, 2026-05-26 00:02 EDT)"
    first_observed: 2026-05-26
    related_malware: ACR Stealer
    actor_id: null
    defanged: true
  - type: domain
    value: 6ryuefl.creativecommunityinfo[.]art
    context: "Host-specific download domain in ACR Stealer delivery chain; subdomain pattern suggests randomized per-campaign host generation; parent zone creativecommunityinfo.art likely operator-controlled"
    confidence: high
    source_attribution: "SANS ISC diary 33018 (Brad Duncan, 2026-05-26 00:02 EDT)"
    first_observed: 2026-05-26
    related_malware: ACR Stealer
    actor_id: null
    defanged: true
  - type: domain
    value: i.ibb[.]co
    context: "Legitimate image-hosting service (imgbb.com infrastructure) abused for payload staging in ACR Stealer delivery chain. DEFENDER ALERT NOTE: do NOT blocklist parent ibb.co — false-positive risk against legitimate usage. Alert on download + execute-from-i.ibb.co patterns specifically."
    confidence: medium   # legitimate-service-abuse, not operator-controlled domain
    source_attribution: "SANS ISC diary 33018 (Brad Duncan, 2026-05-26 00:02 EDT)"
    first_observed: 2026-05-26
    related_malware: ACR Stealer
    actor_id: null
    defanged: true
    defender_handling: "alert_only_do_not_blocklist_parent_zone"
  - type: domain
    value: yw.enhanceblabber[.]cc
    context: "C2 domain in ACR Stealer chain; subdomain pattern suggests randomized per-campaign host generation; parent zone enhanceblabber.cc likely operator-controlled"
    confidence: high
    source_attribution: "SANS ISC diary 33018 (Brad Duncan, 2026-05-26 00:02 EDT)"
    first_observed: 2026-05-26
    related_malware: ACR Stealer
    actor_id: null
    defanged: true
  - type: hash_sha256
    value: 70b5ecc110e074dbca92932c0e840ea3492ea0a43c3f215b71392c12b02213b2
    context: "ZIP archive — initial-stage delivery file in ACR Stealer chain"
    confidence: high
    source_attribution: "SANS ISC diary 33018 (Brad Duncan, 2026-05-26 00:02 EDT)"
    first_observed: 2026-05-26
    related_malware: ACR Stealer
    actor_id: null
  - type: hash_sha256
    value: a14c3ecf5eb3d2543358482e43dc765dbf9ee7a4bec7571f5ecb8829ca719692
    context: "PowerShell — execution-stage script in ACR Stealer chain"
    confidence: high
    source_attribution: "SANS ISC diary 33018 (Brad Duncan, 2026-05-26 00:02 EDT)"
    first_observed: 2026-05-26
    related_malware: ACR Stealer
    actor_id: null
  - type: hash_sha256
    value: 47fa746422f1bf6b7712dc6803378e6a995488007193a7441d790f70d204728f
    context: "Image file — masquerading-as-image payload-staging file in ACR Stealer chain"
    confidence: high
    source_attribution: "SANS ISC diary 33018 (Brad Duncan, 2026-05-26 00:02 EDT)"
    first_observed: 2026-05-26
    related_malware: ACR Stealer
    actor_id: null

ttp_keywords:
  - name: Malvertising via Google Ads
    framework_mapping: MITRE T1583.008 / Acquire Infrastructure — Malvertising
    context: "Fake Claude download pages surfaced via Google Ads malicious advertising delivery"
  - name: URL concealment via sites.google.com
    framework_mapping: MITRE T1566.002 / Phishing — Spearphishing Link (loose analog)
    context: "Initial redirect chain concealed in URLs for sites.google.com → fake Claude page on fairpoint29.com"
  - name: AI brand impersonation lure (Anthropic / Claude)
    framework_mapping: MITRE T1036 / Masquerading (loose analog at brand-impersonation layer)
    context: "Fake Claude (Anthropic) download landing page as initial-access lure mechanism"

librarian_handoff:
  master_index_regeneration_required: true
  master_index_regeneration_reason: >
    Six new domain + hash IOCs surfaced from this finding warrant
    _master-index.yaml regeneration. Note the special handling on
    i.ibb.co (alert-only, do NOT blocklist parent zone).

# Downstream handoff flags
analyst_review_required: false      # B3 single-source defender-tier IOC publication; no novel attribution; commodity infostealer
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

# SANS ISC: ACR Stealer Delivered via Fake Claude (Anthropic) Download Page on fairpoint29[.]com — Google Ads Malvertising, sites.google.com URL Concealment, 6 Actionable IOCs Published

## Summary

SANS Internet Storm Center diary 33018 (Brad Duncan handler byline, 2026-05-26 00:02 EDT) documents an ACR Stealer Windows infostealer delivery chain that abuses Anthropic's Claude brand as the initial-access lure. The chain: Google Ads malvertising → URL concealment via `sites.google.com` redirects → a fake Claude download landing page on `fairpoint29[.]com` that displays OS-aware lures with platform-specific malware download instructions → ACR Stealer execution. The diary publishes six immediately-actionable IOCs (the fake-page domain, three download/staging domains including one legitimate-service-abuse alert on `i.ibb.co`, one C2 domain, and three SHA-256 hashes for ZIP / PowerShell / image-file stages). No threat actor attribution — ACR Stealer is commodity infostealer deployed by multiple criminal operators. Single-source defender-tier publication; the IOC defender-utility is independent of the attribution-layer corroboration question. Recommend `_master-index.yaml` regeneration after this run with the special-handling note on `i.ibb.co` (alert-only, do NOT blocklist parent zone). This is the fourth corpus surface of Anthropic-product / Claude-brand abuse across the last three weeks (ClaudeBleed Chrome extension via `finding-2026-05-08-0004`; MacSync claude.ai/share URL abuse via `finding-2026-05-10-0001`; GTG-1002 Claude Code CLAUDE.md persistent jailbreak via `finding-2026-05-26-0002`; and now this).

## Sources

### SANS Internet Storm Center (sans-isc, digraph: B)

- URL: https://isc.sans.edu/diary/rss/33018
- Published: 2026-05-26 00:02 EDT
- Handler: Brad Duncan
- Key claim: ACR Stealer delivered via fake Claude download landing page on `fairpoint29[.]com`; Google Ads malvertising + `sites.google.com` URL concealment delivery pattern; six IOCs published.

## Technical detail

### ACR Stealer

- **Family:** Windows malware classified on Malpedia.
- **Capability class:** Information-stealing (infostealer).
- **Specific technical details:** Not elaborated in this diary; refer to Malpedia's ACR Stealer canonical record for capability detail.

### Delivery chain

1. **Malvertising / Google Ads** — fake Claude download pages surfaced via Google Ads malicious advertising delivery.
2. **URL concealment** — initial redirect chain concealed in URLs for `sites.google[.]com` per Brad Duncan diary.
3. **Fake landing page** — hosted on `fairpoint29[.]com`.
4. **OS-aware lure** — the fake page displays platform-specific malware download instructions based on the victim's operating system.

### Defender handling notes

The diary explicitly flags `i.ibb[.]co` as a legitimate image-hosting service (imgbb.com infrastructure) abused for payload staging. Do NOT blocklist the parent zone `ibb.co` — false-positive risk against legitimate usage. Alert on download + execute-from-`i.ibb.co` patterns specifically.

## IOCs surfaced

```yaml
iocs:
  - type: domain
    value: fairpoint29[.]com
    context: "Fake Claude (Anthropic) download landing page — OS-aware lure"
    confidence: high
    related_malware: ACR Stealer
  - type: domain
    value: primemetricsa[.]com
    context: "Download domain in ACR Stealer delivery chain"
    confidence: high
    related_malware: ACR Stealer
  - type: domain
    value: 6ryuefl.creativecommunityinfo[.]art
    context: "Host-specific download domain; parent zone likely operator-controlled"
    confidence: high
    related_malware: ACR Stealer
  - type: domain
    value: i.ibb[.]co
    context: "Legitimate image-hosting service abused for payload staging; ALERT-ONLY, do NOT blocklist parent zone ibb.co"
    confidence: medium
    related_malware: ACR Stealer
    defender_handling: "alert_only_do_not_blocklist_parent_zone"
  - type: domain
    value: yw.enhanceblabber[.]cc
    context: "C2 domain in ACR Stealer chain; parent zone likely operator-controlled"
    confidence: high
    related_malware: ACR Stealer
  - type: hash_sha256
    value: 70b5ecc110e074dbca92932c0e840ea3492ea0a43c3f215b71392c12b02213b2
    context: "ZIP archive — initial-stage delivery file"
    related_malware: ACR Stealer
  - type: hash_sha256
    value: a14c3ecf5eb3d2543358482e43dc765dbf9ee7a4bec7571f5ecb8829ca719692
    context: "PowerShell — execution-stage script"
    related_malware: ACR Stealer
  - type: hash_sha256
    value: 47fa746422f1bf6b7712dc6803378e6a995488007193a7441d790f70d204728f
    context: "Image file — masquerading-as-image payload-staging file"
    related_malware: ACR Stealer
```

## Relationship to existing findings

- **finding-2026-05-08-0004** (LayerX ClaudeBleed Chrome extension) — first corpus surface of Anthropic-product/Claude-brand abuse.
- **finding-2026-05-10-0001** (TeamPCP MacSync claude.ai/share URL abuse) — second corpus surface; share-URL trust-boundary abuse.
- **finding-2026-05-26-0002** (CKR AI Threat Landscape Digest, GTG-1002 Claude Code CLAUDE.md jailbreak) — third corpus surface; agentic-config-file persistence abuse.
- **This finding** — fourth corpus surface; AI-brand-impersonation-as-lure-vector. ACR Stealer is commodity-stealer; the Anthropic brand abuse is the lure mechanism, not AI-platform-credential-targeting (which is the CKR digest's structurally distinct surface).

The cumulative four-surface Anthropic-product-abuse pattern over three weeks is a meta-cluster candidate — surfaced as an analyst question for SAT-ACH consideration in the next analyst cycle (cross-referenced in `finding-2026-05-26-0002` analyst handoff).

## Open questions for analyst

- Meta-cluster question (cross-referenced from finding-2026-05-26-0002): does the four-surface Anthropic-product-abuse pattern (ClaudeBleed Chrome extension + MacSync claude.ai/share + GTG-1002 Claude Code CLAUDE.md + ACR Stealer fake Claude page) warrant a discrete corpus meta-cluster tag?
- Librarian: regenerate `_master-index.yaml` to include the 6 new IOCs. Preserve the `i.ibb.co` defender-handling note (alert-only, do NOT blocklist parent zone).
- Independent corroboration paths if/when they arrive: ANY.RUN / Hatching Triage / Joe Sandbox public sandbox submissions on the same hashes; Palo Alto Unit 42 / CrowdStrike / Sophos / Microsoft Defender / Google TAG publishing parallel campaign observations on the AI-brand-impersonation lure vector; abuse.ch URLhaus / ThreatFox tagging of the published domains.
