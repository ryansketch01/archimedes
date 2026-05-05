---
raw_id: raw-2026-05-05-0007
collected_at: 2026-05-05T15:34:00-04:00
run_id: pre-brief-afternoon-20260505-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: mstic
  source_name: "Microsoft MSTIC / Defender Security Research"
  source_url: https://www.microsoft.com/en-us/security/blog/2026/05/04/breaking-the-code-multi-stage-code-of-conduct-phishing-campaign-leads-to-aitm-token-compromise/
  published_at: 2026-05-04T12:00:00-04:00
  corroborating_sources:
    - id: securityweek
      url: https://www.securityweek.com/microsoft-warns-of-sophisticated-phishing-campaign-targeting-us-organizations/
      note: "SecurityWeek 2026-05-05 10:45 EDT relay of Microsoft post (Eduard Kovacs); not independent — adds no new technical observation."
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [aitm, oauth, token-theft, mfa-bypass, phishing, conditional-access, entra, microsoft, defender]
triage_tags: [non_flash, aitm-tradecraft, oauth-token-theft, multi-victim-campaign, us-targeting-92pct, mechanism-relevant-to-ad]
iocs_extracted: true
iocs_count: 13
text_word_count: 1850
promoted: true
promoted_to_finding: finding-2026-05-05-0007
promoted_at: 2026-05-05T15:48:00-04:00
ttl_expires_at: 2026-08-03T15:34:00-04:00
test: false
---

# Microsoft: multi-stage "code of conduct" AitM phishing campaign — 35K users, 13K orgs, 92% US

**Source:** Microsoft Security Blog, joint authorship Microsoft Defender Security Research Team and Microsoft Threat Intelligence (MSTIC).
**Published:** 2026-05-04 (post-dates the morning brief data window — first relayed by SecurityWeek 2026-05-05 10:45 EDT, Eduard Kovacs).
**Attribution:** Unattributed. No Storm-NNNN designation. No nation-state language.
**Campaign window:** 2026-04-14 through 2026-04-16 (three-day burst).
**Scope:** 35,000+ recipients across 13,000+ organizations in 26 countries; 92% of targets US-based.
**Sectors named:** healthcare & life sciences (19%), financial services (18%), professional services (11%), technology & software (11%). **Defense, aerospace, and government are NOT named in the Microsoft post.**

## What the source says

Microsoft describes a multi-stage phishing chain that culminated in adversary-in-the-middle (AitM) session token theft, bypassing non-phishing-resistant MFA. The chain:

1. Inbound email impersonating internal compliance / regulatory teams (display names: "Internal Regulatory COC," "Workforce Communications," "Team Conduct Report"); subject lines reference conduct-policy violations.
2. PDF attachment titled e.g. "Awareness Case Log File — [date].pdf" or "Disciplinary Action — Employee Device Handling Case.pdf"; PDF contains a "Review Case Materials" link.
3. Cloudflare CAPTCHA-gated landing page (used to evade automated URL detonation).
4. Intermediate staging page claiming an "encryption requirement."
5. Email-address collection form.
6. Second CAPTCHA (image-selection style).
7. Platform-specific redirect (mobile vs desktop).
8. Final sign-in prompt branded "Sign in with Microsoft."
9. AitM proxy intercepts the authenticated session and exfiltrates the token — bypassing MFA via session-token rather than credential capture.

Microsoft frames the operator infrastructure as "likely originating from a cloud-hosted Windows virtual machine" and describes the staging domains as "likely attacker-controlled." Microsoft does not present a confidence digraph; the language "likely" appears in qualified positions throughout.

## A&D relevance assessment (mechanism, not observation)

**Direct sectoral targeting:** Microsoft does not name defense or aerospace recipients. The 92% US concentration is real but is distributed across the four sectors listed; A&D primes are not in that list.

**Mechanism overlap:** The AitM token-theft pattern is the same class of attack the morning brief covered for Charming Kitten / Mint Sandstorm (OAuth consent-grant phishing against defense-policy think tanks). The two campaigns are separate, with separate operators and pretexts, but they exploit the same Entra ID gap: non-phishing-resistant MFA can be bypassed once a session token is obtained via proxy. A prime's Entra tenant is exposed to this class regardless of whether this specific campaign hit it.

**Lookalike pretext risk:** "Code of conduct" / "compliance review" pretexts route well to legal, HR, and ethics-office staff at primes. ITAR-regulated organizations have heavier compliance traffic than the average enterprise, which raises the conversion rate for that pretext shape. This is mechanism-based forecasting, not observed prime-direct activity — note carefully if briefer escalates.

## Cross-source independence

SecurityWeek's article is a relay, not an independent observation. Eduard Kovacs cites the Microsoft post and links to it for "additional IOCs and threat-hunting queries." No A-grade source has published an independent corroborating observation as of collection time. Single-source veto applies if grader promotes — primary source is Microsoft.

## Comparison to morning brief items

- **Distinct from finding-2026-05-05-0002 (Charming Kitten OAuth):** different operator, different pretext (think-tank "comment on draft" vs corporate "code of conduct"), different sector emphasis (think tanks/MENA journalists vs. healthcare/financial/professional services). Same Entra-token weakness class.
- **Adds new IOC set** — five attacker domains, three SHA-256 hashes, five sender addresses.
- **Does not** intersect with FortiManager, IIS HTTP.sys, Cisco ASA, UNC1549, or Siemens SIMATIC findings.

---

## Extraction notes

- Language: en
- Article type: vendor blog (Microsoft) + media relay (SecurityWeek)
- Microsoft is the sole primary source; SecurityWeek does not independently observe.
- Raw IOC extraction invoked: yes

## IOCs (from ioc-extraction skill)

```yaml
extraction_metadata:
  source_brief_id: mstic-aitm-code-of-conduct-2026-05
  source_url: https://www.microsoft.com/en-us/security/blog/2026/05/04/breaking-the-code-multi-stage-code-of-conduct-phishing-campaign-leads-to-aitm-token-compromise/
  extracted_at: 2026-05-05T15:34:00-04:00
  extracted_by: collector
  target_actor_id: null
  text_word_count: 1850

indicators:
  - id: raw-domain-compliance-protectionoutlook-de
    type: domain
    value: compliance-protectionoutlook.de
    defanged_original: "compliance-protectionoutlook[.]de"
    resolved_ip: null
    first_seen: 2026-04
    last_seen: 2026-04
    role: delivery
    campaign: "Code of Conduct AitM 2026-Q2"
    related_malware: []
    source_brief: mstic-aitm-code-of-conduct-2026-05
    context_excerpt: "Phishing landing/staging domain in MSTIC writeup"
    attribution_in_text: null
    notes: null

  - id: raw-domain-acceptable-use-policy-calendly-de
    type: domain
    value: acceptable-use-policy-calendly.de
    defanged_original: "acceptable-use-policy-calendly[.]de"
    resolved_ip: null
    first_seen: 2026-04
    last_seen: 2026-04
    role: delivery
    campaign: "Code of Conduct AitM 2026-Q2"
    related_malware: []
    source_brief: mstic-aitm-code-of-conduct-2026-05
    context_excerpt: "Lookalike Calendly-themed phishing host"
    attribution_in_text: null
    notes: null

  - id: raw-domain-cocinternal-com
    type: domain
    value: cocinternal.com
    defanged_original: "cocinternal[.]com"
    resolved_ip: null
    first_seen: 2026-04
    last_seen: 2026-04
    role: delivery
    campaign: "Code of Conduct AitM 2026-Q2"
    related_malware: []
    source_brief: mstic-aitm-code-of-conduct-2026-05
    context_excerpt: "Sender-tied domain for cocpostmaster@ and m365premiumcommunications@"
    attribution_in_text: null
    notes: null

  - id: raw-domain-gadellinet-com
    type: domain
    value: gadellinet.com
    defanged_original: "gadellinet[.]com"
    resolved_ip: null
    first_seen: 2026-04
    last_seen: 2026-04
    role: delivery
    campaign: "Code of Conduct AitM 2026-Q2"
    related_malware: []
    source_brief: mstic-aitm-code-of-conduct-2026-05
    context_excerpt: "Sender-tied domain for nationaladmin@"
    attribution_in_text: null
    notes: null

  - id: raw-domain-harteprn-com
    type: domain
    value: harteprn.com
    defanged_original: "harteprn[.]com"
    resolved_ip: null
    first_seen: 2026-04
    last_seen: 2026-04
    role: delivery
    campaign: "Code of Conduct AitM 2026-Q2"
    related_malware: []
    source_brief: mstic-aitm-code-of-conduct-2026-05
    context_excerpt: "Sender-tied domain for nationalintegrity@"
    attribution_in_text: null
    notes: null

  - id: raw-email-cocpostmaster-cocinternal
    type: email
    value: cocpostmaster@cocinternal.com
    defanged_original: null
    role: delivery
    campaign: "Code of Conduct AitM 2026-Q2"
    related_malware: []
    source_brief: mstic-aitm-code-of-conduct-2026-05
    context_excerpt: "Sender address used in compliance-themed lures"
    attribution_in_text: null
    notes: null

  - id: raw-email-nationaladmin-gadellinet
    type: email
    value: nationaladmin@gadellinet.com
    defanged_original: null
    role: delivery
    campaign: "Code of Conduct AitM 2026-Q2"
    related_malware: []
    source_brief: mstic-aitm-code-of-conduct-2026-05
    context_excerpt: "Sender address used in compliance-themed lures"
    attribution_in_text: null
    notes: null

  - id: raw-email-nationalintegrity-harteprn
    type: email
    value: nationalintegrity@harteprn.com
    defanged_original: null
    role: delivery
    campaign: "Code of Conduct AitM 2026-Q2"
    related_malware: []
    source_brief: mstic-aitm-code-of-conduct-2026-05
    context_excerpt: "Sender address used in compliance-themed lures"
    attribution_in_text: null
    notes: null

  - id: raw-email-m365premium-cocinternal
    type: email
    value: m365premiumcommunications@cocinternal.com
    defanged_original: null
    role: delivery
    campaign: "Code of Conduct AitM 2026-Q2"
    related_malware: []
    source_brief: mstic-aitm-code-of-conduct-2026-05
    context_excerpt: "Sender address mimicking M365 service traffic"
    attribution_in_text: null
    notes: null

  - id: raw-email-documentviewer-businesshellosign-de
    type: email
    value: documentviewer@na.businesshellosign.de
    defanged_original: null
    role: delivery
    campaign: "Code of Conduct AitM 2026-Q2"
    related_malware: []
    source_brief: mstic-aitm-code-of-conduct-2026-05
    context_excerpt: "Sender lookalike for HelloSign-style document delivery"
    attribution_in_text: null
    notes: null

  - id: raw-hash-5db1ecbbb2c9
    type: hash_sha256
    value: 5DB1ECBBB2C90C51D81BDA138D4300B90EA5EB2885CCE1BD921D692214AECBC6
    defanged_original: null
    role: delivery
    campaign: "Code of Conduct AitM 2026-Q2"
    related_malware: []
    source_brief: mstic-aitm-code-of-conduct-2026-05
    context_excerpt: "PDF attachment hash from MSTIC IOC list"
    attribution_in_text: null
    notes: null

  - id: raw-hash-b5a3346082ac
    type: hash_sha256
    value: B5A3346082AC566B4494E6175F1CD9873B64ABE6C902DB49BD4E8088876C9EAD
    defanged_original: null
    role: delivery
    campaign: "Code of Conduct AitM 2026-Q2"
    related_malware: []
    source_brief: mstic-aitm-code-of-conduct-2026-05
    context_excerpt: "PDF attachment hash from MSTIC IOC list"
    attribution_in_text: null
    notes: null

  - id: raw-hash-11420d6d693b
    type: hash_sha256
    value: 11420D6D693BF8B19195E6B98FEDD03B9BCBC770B6988BC64CB788BFABE1A49D
    defanged_original: null
    role: delivery
    campaign: "Code of Conduct AitM 2026-Q2"
    related_malware: []
    source_brief: mstic-aitm-code-of-conduct-2026-05
    context_excerpt: "PDF attachment hash from MSTIC IOC list"
    attribution_in_text: null
    notes: null

attribution_claims: []

benign_filtered:
  - value: microsoft.com
    reason: publisher_own_domain
  - value: securityweek.com
    reason: publisher_own_domain
  - value: cloudflare.com
    reason: legitimate_infrastructure_referenced

extraction_warnings:
  - type: ambiguous_role
    ioc_id: raw-domain-cocinternal-com
    detail: "Domain hosts both staging redirect chain and sender infrastructure; recorded as delivery, grader may split."
```
