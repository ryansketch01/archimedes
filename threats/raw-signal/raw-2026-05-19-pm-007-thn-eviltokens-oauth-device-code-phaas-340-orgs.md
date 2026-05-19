---
raw_id: raw-2026-05-19-pm-007
collected_at: 2026-05-19T15:46:00-04:00
run_id: pre-brief-20260519-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: thehackernews
  source_name: "The Hacker News"
  source_url: https://thehackernews.com/2026/05/the-new-phishing-click-how-oauth.html
  published_at: 2026-05-19T07:30:00-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords:
    - EvilTokens
    - PhaaS
    - phishing-as-a-service
    - OAuth device-code phishing
    - Microsoft 365
    - M365 tenants
    - device-code flow
    - microsoft.com/devicelogin
    - MFA bypass
    - refresh tokens
    - Cloud Security Alliance
    - CSA Research Note
    - Tycoon2FA adjacent class
    - Storm-2949 adjacent class
triage_tags:
  - eviltokens_phaas_oauth_device_code
  - 340_plus_m365_tenants_compromised_five_weeks
  - platform_live_february_2026
  - tradecraft_class_overlap_tycoon2fa_finding_2026_05_17_0002
  - tradecraft_class_overlap_storm_2949_finding_morning_carry_forward
  - mfa_bypass_via_legitimate_device_code_flow
  - refresh_token_persistence_weeks_to_months
  - csa_research_note_2026_03_25
  - five_countries_unspecified_geographic_scope
  - no_specific_victim_sectors_in_source
  - no_a_and_d_prime_named
  - no_tracked_actor_attribution_per_source
  - no_iocs_per_source
  - cluster_corroboration_pattern_match_to_storm_2949_tradecraft
  - hard_rule_2_no_archimedes_originated_attribution_to_storm_2949
  - hard_rule_3_no_phishing_template_or_token_extraction_walkthrough
iocs_extracted: false
iocs_count: 0
text_word_count: 350
promoted: true
promoted_to_finding: finding-2026-05-19-0010
promoted_at: 2026-05-19T16:22:00-04:00
ttl_expires_at: 2026-08-17T15:46:00-04:00
---

# The New Phishing Click: How OAuth Consent Bypasses MFA

The Hacker News — Tuesday 2026-05-19, 07:30 EDT (11:30 UTC).

## Source primary content (extract — preserved for grader)

**Platform:** EvilTokens — a Phishing-as-a-Service (PhaaS) platform that went live in February 2026.

**Scale:** Within five weeks of launch, EvilTokens had compromised **more than 340 Microsoft 365 organizations** across **five countries** (countries unspecified in source).

**Tradecraft mechanism (conceptual):**
1. Target receives a message asking them to enter a short code at `microsoft.com/devicelogin`
2. Target completes their normal MFA challenge
3. Target walks away believing they have verified a normal sign-in
4. Behind the scenes, the device-code flow grants the operator long-lived **refresh tokens**
5. Per source: "The operator never needed a password, never tripped an MFA prompt, and never produced a sign-in event that looked like an intrusion."
6. Refresh tokens survive password resets and remain valid "for weeks or months, depending on the tenant configuration"
7. Closure requires explicit token revocation, not password rotation

**Research attribution:** Cloud Security Alliance (CSA) Research Note on OAuth device-code phishing, dated **2026-03-25**. THN article is the post-research relay.

**Sector/industry mentions:** No specific victim sectors identified. Finance and CRM contexts mentioned only as illustrative examples in toxic-combination discussion.

**IOCs and actor naming:** No indicators of compromise, no CVEs, no tracked threat-actor designations provided in the source.

**A&D mentions:** None.

## Extraction notes

- Language: en
- Publisher byline: The Hacker News (no individual byline; primary source CSA via THN relay)
- Article type: media-relay of CSA research
- Source grade context: The Hacker News = B2 media-relay tier per source-grades.yaml (provisional). CSA = first-citation as a research source in Archimedes corpus — likely provisional-B for the grader to evaluate (Cloud Security Alliance is an established multi-stakeholder cloud-security trade body with formal research-note publications; analogous to a tier between ENISA and vendor blogs).
- Hard Rule 2 compliance: THN does NOT attribute EvilTokens to any tracked actor. Archimedes does NOT propagate Storm-2949 (morning brief carry-forward) or Tycoon2FA (finding-2026-05-17-0002 carry-forward) attribution to EvilTokens despite tradecraft-class overlap. The OAuth device-code phishing tradecraft is a tradecraft class, not a single-operator attribution.
- Hard Rule 3 compliance: source describes the mechanism at conceptual flow-of-operations level only; no phishing-template HTML, no token-extraction script, no walkthrough material. Tradecraft framing only.
- Hard Rule 4 compliance: passive only.

## Tradecraft-class cluster (pattern-match awareness for grader)

EvilTokens shares operational mechanism class with three other tracked items in the Archimedes corpus:

1. **Tycoon2FA** (finding-2026-05-17-0002) — device-code PhaaS, similar OAuth abuse pattern, different vendor naming. Anti-noise rule 1 active.
2. **Storm-2949** (Microsoft MSTIC originating-research per morning-brief carry-forward) — identity-driven cloud-pivot tradecraft including device-code abuse class. NOT YET A&D-prime-attributed per Microsoft framing.
3. **CORDIAL SPIDER + SNARKY SPIDER** (CrowdStrike 2026-04-30 voice-phishing AiTM SaaS) — earlier in the year. Different specific tradecraft (vishing AiTM, not device-code phishing) but adjacent SaaS-impersonation class.

The pattern is an industry-wide PhaaS arms-race against M365 device-code and OAuth consent flows. Archimedes does not extrapolate from this class observation to a single tracked actor.

## A&D-prime relevance assessment

**Direct A&D-prime targeting:** NOT mentioned.

**Indirect / structural relevance:**
1. **M365 device-code flow is enabled by default** in most M365 tenants. A&D-prime tenants that have not explicitly disabled device-code flow via Conditional Access policy are exposed to this tradecraft class.
2. **A&D-prime exposure measurement** would require Splunk-based Sign-In log analysis for unexpected `deviceCode` grant types — Archimedes' first-party Splunk dormancy precludes proactive exposure assessment beyond awareness.
3. **Pattern-match to finding-2026-05-17-0002 (Tycoon2FA):** the grader should consider whether EvilTokens warrants finding-creation as a tradecraft-class refresh on the device-code phishing surface, or as a corroboration relay on the prior Tycoon2FA finding.

## IOCs (from ioc-extraction skill)

```yaml
iocs: []
attribution_claims: []
```
