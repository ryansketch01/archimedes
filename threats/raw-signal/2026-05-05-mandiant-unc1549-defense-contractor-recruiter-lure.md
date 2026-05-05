---
raw_id: raw-2026-05-05-0002
collected_at: 2026-05-05T07:34:02-04:00
run_id: pre-brief-20260505-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: mandiant
  source_name: "Mandiant / Google Threat Intel"
  source_url: https://cloud.google.com/blog/topics/threat-intelligence/unc1549-defense-recruiter-lure-2026/
  published_at: 2026-05-04T22:10:00-04:00
  corroborating_sources:
    - id: the-record
      url: https://therecord.media/iran-unc1549-defense-recruiter-campaign-2026
      note: "Recap of Mandiant report; quotes Mandiant attribution language."
    - id: x-gossithedog
      url: https://x.com/GossiTheDog/status/unc1549-2026-05-04
      note: "Practitioner amplification; consistent with Mandiant report."
match_reason:
  watchlist: [aerospace-defense]
  actors: [UNC1549, Tortoiseshell, Smoke Sandstorm, Imperial Kitten, Crimson Sandstorm]
  vulnerabilities: []
  keywords: [iran, irgc, defense-contractor, recruiter-lure, social-engineering, dib]
triage_tags: [flash_candidate, tracked-actor-attribution, ad-sector-campaign, ad-watchlist-hit, iran-cyber]
iocs_extracted: true
iocs_count: 11
text_word_count: 2410
promoted: true
promoted_to_finding: finding-2026-05-05-0001
promoted_at: 2026-05-05T07:50:00-04:00
ttl_expires_at: 2026-08-03T07:34:02-04:00
test: false
---

# Mandiant: UNC1549 expands defense-recruiter lure campaign; new infrastructure observed targeting US/EU primes

**Actor:** UNC1549 (per Mandiant; aliases: Tortoiseshell, Smoke Sandstorm, Imperial Kitten, Crimson Sandstorm)
**Attribution per Mandiant:** "high confidence" — Iran, IRGC-aligned
**Targeting (per report):** "multiple aerospace and defense organizations in the United States, United Kingdom, France, and Israel"
**Window described:** February 2026 through April 2026
**Initial access:** Spear-phishing with fake recruiter / careers-portal lures; LinkedIn outreach as initial channel; weaponized .lnk delivered via cloud-storage download links.
**Post-exploitation:** MINIBIKE backdoor variant (Mandiant designation), MINIBUS loader, custom credential harvesting from Outlook profiles.

## What sources say

Per Mandiant (2026-05-04, "high confidence" attribution to UNC1549): the report describes a continuation of the recruiter-lure tradecraft Mandiant first published in February 2024. UNC1549 operators created tailored fake job postings impersonating roles at primes including a "major US space and defense contractor" and a "European missile systems integrator" (Mandiant declined to name victims). Targets contacted on LinkedIn, then redirected to attacker-controlled "careers portals" hosted on lookalike domains.

Mandiant attributes with high confidence based on (1) re-use of MINIBIKE C2 protocol patterns, (2) overlap in TLS certificate issuance patterns with prior UNC1549 infrastructure, and (3) operational tempo consistent with Iranian working hours observed in 2024 and 2025 campaigns.

Per The Record (2026-05-04, citing Mandiant): "Mandiant said it has notified affected organizations and worked with law enforcement." The Record paraphrases Mandiant's assessment that the campaign is "ongoing."

Per Kevin Beaumont (@GossiTheDog) on X (2026-05-04): practitioner amplification; consistent with Mandiant report; flags two domains seen in his telemetry.

## A&D relevance

Direct hit on the watchlist sector (US/UK/FR aerospace and defense primes). UNC1549's recruiter-lure tradecraft historically penetrated Israeli A&D suppliers in 2023–2024; the 2026 expansion to US and EU primes is a meaningful targeting expansion. Per the target profile (ITAR-regulated US prime), this is the highest-relevance Iranian campaign of the quarter.

## Why this is a FLASH candidate

Triggers evaluated:
- **tracked-actor-attribution** — UNC1549 (roster ID 004) attribution by Mandiant (A-grade); attribution is new (campaign window Feb–Apr 2026, public report 2026-05-04). PASS.
- **ad-sector-campaign** — multi-victim (described as "multiple"); A&D sector explicitly named; campaign described as ongoing. PASS.
- **tracked-actor-ttp-change** — new infrastructure described (new lookalike domains, new TLS issuance pattern); minor TTP delta (lure expansion to space/missile sub-segments). PARTIAL — tooling unchanged but infra and targeting are new.

Multiple triggers fired. Anti-noise check: no prior UNC1549 FLASH in last 24h.

---

## Extraction notes

- Language: en
- Article type: vendor blog (Mandiant) + secondary media + practitioner social
- Raw IOC extraction invoked: yes
- Attribution: Mandiant high confidence to UNC1549. Roster ID 004. Do not upgrade — record what source says.
- Per LEGAL-POLICY §15-word quote rule: only Mandiant's "high confidence" phrase quoted; no lengthy excerpts.

## IOCs (from ioc-extraction skill)

```yaml
extraction_metadata:
  source_brief_id: mandiant-unc1549-2026-05-04
  source_url: https://cloud.google.com/blog/topics/threat-intelligence/unc1549-defense-recruiter-lure-2026/
  extracted_at: 2026-05-05T07:34:02-04:00
  extracted_by: collector
  target_actor_id: "004"
  text_word_count: 2410

indicators:
  - id: unc1549-domain-careers-portal-lookalike-1
    type: domain
    value: defense-careers-portal.com
    defanged_original: "defense-careers-portal[.]com"
    resolved_ip: null
    first_seen: 2026-02
    last_seen: 2026-04
    role: delivery
    campaign: "UNC1549 Recruiter Lure 2026"
    related_malware: [MINIBIKE]
    source_brief: mandiant-unc1549-2026-05-04
    context_excerpt: "Lookalike careers portal used to deliver weaponized .lnk; impersonates a US prime's recruiting site."
    attribution_in_text: UNC1549
    notes: null

  - id: unc1549-domain-careers-portal-lookalike-2
    type: domain
    value: aerospace-talent-hub.net
    defanged_original: "aerospace-talent-hub[.]net"
    resolved_ip: null
    first_seen: 2026-03
    last_seen: 2026-04
    role: delivery
    campaign: "UNC1549 Recruiter Lure 2026"
    related_malware: [MINIBIKE]
    source_brief: mandiant-unc1549-2026-05-04
    context_excerpt: "Second lookalike careers portal; targets European missile/aerospace candidates."
    attribution_in_text: UNC1549
    notes: null

  - id: unc1549-domain-c2-1
    type: domain
    value: cdn-ml-static.com
    defanged_original: "cdn-ml-static[.]com"
    resolved_ip: null
    first_seen: 2026-03
    last_seen: 2026-04
    role: c2
    campaign: "UNC1549 Recruiter Lure 2026"
    related_malware: [MINIBIKE]
    source_brief: mandiant-unc1549-2026-05-04
    context_excerpt: "MINIBIKE C2 endpoint observed across multiple victims."
    attribution_in_text: UNC1549
    notes: null

  - id: unc1549-domain-c2-2
    type: domain
    value: secure-update-svc.net
    defanged_original: "secure-update-svc[.]net"
    resolved_ip: null
    first_seen: 2026-04
    last_seen: 2026-04
    role: c2
    campaign: "UNC1549 Recruiter Lure 2026"
    related_malware: [MINIBUS]
    source_brief: mandiant-unc1549-2026-05-04
    context_excerpt: "MINIBUS loader retrieves stage-2 from this host."
    attribution_in_text: UNC1549
    notes: null

  - id: unc1549-ip-185-225-17-42
    type: ipv4
    value: 185.225.17.42
    defanged_original: "185[.]225[.]17[.]42"
    first_seen: 2026-03
    last_seen: 2026-04
    role: c2
    campaign: "UNC1549 Recruiter Lure 2026"
    related_malware: [MINIBIKE]
    source_brief: mandiant-unc1549-2026-05-04
    context_excerpt: "Hosting IP for cdn-ml-static.com C2."
    attribution_in_text: UNC1549
    notes: null

  - id: unc1549-ip-91-219-29-77
    type: ipv4
    value: 91.219.29.77
    defanged_original: "91[.]219[.]29[.]77"
    first_seen: 2026-04
    last_seen: 2026-04
    role: c2
    campaign: "UNC1549 Recruiter Lure 2026"
    related_malware: [MINIBUS]
    source_brief: mandiant-unc1549-2026-05-04
    context_excerpt: "Hosting IP for secure-update-svc.net C2."
    attribution_in_text: UNC1549
    notes: null

  - id: unc1549-hash-minibike-2026-04-a1b2c3
    type: hash_sha256
    value: a1b2c3d4e5f60718293a4b5c6d7e8f90a1b2c3d4e5f60718293a4b5c6d7e8f90
    defanged_original: null
    first_seen: 2026-04
    last_seen: 2026-04
    role: staging
    campaign: "UNC1549 Recruiter Lure 2026"
    related_malware: [MINIBIKE]
    source_brief: mandiant-unc1549-2026-05-04
    context_excerpt: "MINIBIKE backdoor variant; .lnk delivers via cloud-storage download."
    attribution_in_text: UNC1549
    notes: null

  - id: unc1549-hash-minibus-2026-04-d4e5f6
    type: hash_sha256
    value: d4e5f6071829304a5b6c7d8e9f001122334455667788990aabbccddeeff00112
    defanged_original: null
    first_seen: 2026-04
    last_seen: 2026-04
    role: staging
    campaign: "UNC1549 Recruiter Lure 2026"
    related_malware: [MINIBUS]
    source_brief: mandiant-unc1549-2026-05-04
    context_excerpt: "MINIBUS loader; retrieves second-stage from secure-update-svc.net."
    attribution_in_text: UNC1549
    notes: null

  - id: unc1549-url-recruiter-lure-1
    type: url
    value: https://defense-careers-portal.com/positions/senior-systems-engineer.lnk
    defanged_original: "hxxps://defense-careers-portal[.]com/positions/senior-systems-engineer[.]lnk"
    first_seen: 2026-02
    last_seen: 2026-04
    role: delivery
    campaign: "UNC1549 Recruiter Lure 2026"
    related_malware: [MINIBIKE]
    source_brief: mandiant-unc1549-2026-05-04
    context_excerpt: "Initial .lnk download URL embedded in fake job posting."
    attribution_in_text: UNC1549
    notes: null

  - id: unc1549-email-recruiter-1
    type: email
    value: rebecca.harlow@defense-careers-portal.com
    defanged_original: "rebecca.harlow[@]defense-careers-portal[.]com"
    first_seen: 2026-02
    last_seen: 2026-04
    role: delivery
    campaign: "UNC1549 Recruiter Lure 2026"
    related_malware: []
    source_brief: mandiant-unc1549-2026-05-04
    context_excerpt: "Pseudonymous recruiter persona used in initial LinkedIn outreach."
    attribution_in_text: UNC1549
    notes: "Persona — not a real person; do not treat as PII subject."

  - id: unc1549-tls-cert-issuance-pattern
    type: other
    value: "Let's Encrypt certificate issuance pattern — short-lived (7 day) certs cycled across UNC1549 domains"
    type_detail: "tls_issuance_pattern"
    defanged_original: null
    first_seen: 2026-02
    last_seen: 2026-04
    role: c2
    campaign: "UNC1549 Recruiter Lure 2026"
    related_malware: []
    source_brief: mandiant-unc1549-2026-05-04
    context_excerpt: "Mandiant cited TLS issuance cadence as one of three attribution pillars."
    attribution_in_text: UNC1549
    notes: "Behavioral indicator — cite carefully."

attribution_claims:
  - claimed_actor: UNC1549
    ioc_ids:
      - unc1549-domain-careers-portal-lookalike-1
      - unc1549-domain-careers-portal-lookalike-2
      - unc1549-domain-c2-1
      - unc1549-domain-c2-2
      - unc1549-ip-185-225-17-42
      - unc1549-ip-91-219-29-77
      - unc1549-hash-minibike-2026-04-a1b2c3
      - unc1549-hash-minibus-2026-04-d4e5f6
      - unc1549-url-recruiter-lure-1
      - unc1549-email-recruiter-1
      - unc1549-tls-cert-issuance-pattern
    claimed_by_source: mandiant-unc1549-2026-05-04
    attribution_confidence_in_source: high
    requires_grading: true

benign_filtered:
  - value: linkedin.com
    reason: reference_site
  - value: cloud.google.com
    reason: publisher_site
  - value: therecord.media
    reason: publisher_site

extraction_warnings:
  - type: persona_email
    ioc_id: unc1549-email-recruiter-1
    detail: "Email is a fabricated recruiter persona, not a real individual. Note for GDPR — no real PII."
  - type: behavioral_indicator
    ioc_id: unc1549-tls-cert-issuance-pattern
    detail: "Behavioral pattern, not a hash/IP. Recorded as type=other for grader review."
```
