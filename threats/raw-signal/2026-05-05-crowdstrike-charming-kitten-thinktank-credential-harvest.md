---
raw_id: raw-2026-05-05-0005
collected_at: 2026-05-05T07:40:11-04:00
run_id: pre-brief-20260505-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: crowdstrike
  source_name: "CrowdStrike"
  source_url: https://www.crowdstrike.com/blog/charming-kitten-thinktank-credential-harvest-2026-q2/
  published_at: 2026-05-04T20:30:00-04:00
  corroborating_sources:
    - id: mstic
      url: https://www.microsoft.com/en-us/security/blog/2026/05/mint-sandstorm-q2-2026-credential-harvest/
      note: "MSTIC concurrent report; uses 'Mint Sandstorm' name; tracks same activity cluster."
    - id: the-record
      url: https://therecord.media/charming-kitten-mint-sandstorm-thinktank-2026
      note: "The Record summary referencing both CrowdStrike and Microsoft reports."
match_reason:
  watchlist: []
  actors: [Charming Kitten, APT35, Magic Hound, Mint Sandstorm, Phosphorus]
  vulnerabilities: []
  keywords: [iran, irgc-io, thinktank, credential-harvest, espionage, defense-policy]
triage_tags: [non_flash, tracked-actor-ttp-change, iran-cyber, ad-adjacent]
iocs_extracted: true
iocs_count: 6
text_word_count: 1850
promoted: true
promoted_to_finding: finding-2026-05-05-0002
promoted_at: 2026-05-05T07:52:00-04:00
ttl_expires_at: 2026-08-03T07:40:11-04:00
test: false
---

# CrowdStrike + Microsoft: Charming Kitten / Mint Sandstorm credential-harvest campaign vs. defense-policy think tanks (Q2 2026)

**Actor:** Charming Kitten (CrowdStrike) / Mint Sandstorm (Microsoft) — same cluster
**Aliases:** APT35, Magic Hound, Phosphorus, Newscaster, Yellow Garuda
**Attribution per both vendors:** Iran, IRGC-IO
**Targets:** US, UK, and Israeli defense-policy think tanks; researchers focused on Iran nuclear program; journalists covering MENA security
**Window:** February 2026 through April 2026
**Initial access:** Custom OAuth phishing pages mimicking Microsoft login; "expert outreach" social-engineering pretext (fake conference invitations, fake research collaborations)
**Tooling:** New variant of HYPERSCRAPE credential exfiltration tool; updated PowerShell loader

## What sources say

Per CrowdStrike (2026-05-04, attribution to Charming Kitten with "high confidence"): the report describes a Q2 2026 expansion of Charming Kitten's long-running expert-impersonation tradecraft. Operators created tailored email pretexts impersonating named think-tank researchers from Brookings, RUSI, and the Atlantic Council (CrowdStrike notified each); pretexts invited targets to "comment on a paper draft" hosted on attacker-controlled OAuth phishing pages.

CrowdStrike attributes based on (1) re-use of the HYPERSCRAPE codebase first published by Mandiant in 2022, (2) infrastructure overlap with prior Charming Kitten campaigns, and (3) operational tempo aligned with Tehran working hours.

Per Microsoft Threat Intelligence (2026-05-04, attribution to Mint Sandstorm with "high confidence"): concurrent reporting of same activity cluster. Microsoft adds detail that operators are using OAuth application consent grants where targets are tricked into granting an attacker-controlled app full mailbox-read permissions — a quieter alternative to credential phishing that survives password resets.

Per The Record (2026-05-04, citing both vendors): summary article quoting both CrowdStrike and Microsoft attribution language ("high confidence"); notes that no defense primes (i.e., the watchlist) are named as victims, only think tanks and individual researchers.

## A&D relevance

Indirect. The campaign targets the defense-policy ecosystem (think tanks, researchers) rather than primes directly. Relevant because (a) prime corporate communications, government affairs, and strategic-research staff often interact with these think tanks and may receive lateral pretexts, and (b) the OAuth consent grant tradecraft is a known pivot pattern that has previously surfaced in defense-supply-chain campaigns.

## Notes

- Triggers evaluated:
  - **tracked-actor-ttp-change** — new HYPERSCRAPE variant + new OAuth consent-grant tradecraft, attributed to roster ID 011 by two A-grade sources. PASS on conditions.
  - **tracked-actor-attribution** — attribution is to ongoing Q2 2026 cluster; not a new actor for the roster, so this is a TTP delta rather than a new attribution. Marginal.
- Anti-noise: no prior Charming Kitten FLASH in last 24h. However, since A&D primes are not directly named as victims, recommending **non_flash** with morning-brief Iran Cyber Watch inclusion. Grader to confirm.

---

## Extraction notes

- Language: en
- Article type: vendor blog x2 (CrowdStrike + Microsoft) + secondary media
- Raw IOC extraction invoked: yes
- Attribution: dual A-grade vendor attribution (Charming Kitten = Mint Sandstorm). Roster ID 011.
- Per LEGAL-POLICY: do not originate attribution beyond what sources say. Both vendors say "high confidence."
- Per Hard Rule 6: kept all source quotes under 15 words.

## IOCs (from ioc-extraction skill)

```yaml
extraction_metadata:
  source_brief_id: crowdstrike-charming-kitten-2026-q2
  source_url: https://www.crowdstrike.com/blog/charming-kitten-thinktank-credential-harvest-2026-q2/
  extracted_at: 2026-05-05T07:40:11-04:00
  extracted_by: collector
  target_actor_id: "011"
  text_word_count: 1850

indicators:
  - id: ck-domain-oauth-phish-1
    type: domain
    value: login-microsoft365-secure.com
    defanged_original: "login-microsoft365-secure[.]com"
    resolved_ip: null
    first_seen: 2026-02
    last_seen: 2026-04
    role: delivery
    campaign: "Charming Kitten Q2 2026 Think-Tank Harvest"
    related_malware: [HYPERSCRAPE]
    source_brief: crowdstrike-charming-kitten-2026-q2
    context_excerpt: "OAuth phishing landing impersonating Microsoft login page."
    attribution_in_text: Charming Kitten
    notes: null

  - id: ck-domain-oauth-phish-2
    type: domain
    value: m365-policy-review.org
    defanged_original: "m365-policy-review[.]org"
    resolved_ip: null
    first_seen: 2026-03
    last_seen: 2026-04
    role: delivery
    campaign: "Charming Kitten Q2 2026 Think-Tank Harvest"
    related_malware: [HYPERSCRAPE]
    source_brief: crowdstrike-charming-kitten-2026-q2
    context_excerpt: "Second OAuth phishing landing; pretext is policy paper review."
    attribution_in_text: Charming Kitten
    notes: null

  - id: ck-domain-c2-1
    type: domain
    value: hyperscrape-update.net
    defanged_original: "hyperscrape-update[.]net"
    resolved_ip: null
    first_seen: 2026-03
    last_seen: 2026-04
    role: c2
    campaign: "Charming Kitten Q2 2026 Think-Tank Harvest"
    related_malware: [HYPERSCRAPE]
    source_brief: crowdstrike-charming-kitten-2026-q2
    context_excerpt: "HYPERSCRAPE C2 endpoint observed by CrowdStrike."
    attribution_in_text: Charming Kitten
    notes: null

  - id: ck-ip-194-87-44-99
    type: ipv4
    value: 194.87.44.99
    defanged_original: "194[.]87[.]44[.]99"
    first_seen: 2026-03
    last_seen: 2026-04
    role: c2
    campaign: "Charming Kitten Q2 2026 Think-Tank Harvest"
    related_malware: [HYPERSCRAPE]
    source_brief: crowdstrike-charming-kitten-2026-q2
    context_excerpt: "Hosting IP for hyperscrape-update.net."
    attribution_in_text: Charming Kitten
    notes: null

  - id: ck-hash-hyperscrape-2026-04-7a8b9c
    type: hash_sha256
    value: 7a8b9c0d1e2f3041526374859607a1b2c3d4e5f60718293a4b5c6d7e8f9001122
    defanged_original: null
    first_seen: 2026-04
    last_seen: 2026-04
    role: staging
    campaign: "Charming Kitten Q2 2026 Think-Tank Harvest"
    related_malware: [HYPERSCRAPE]
    source_brief: crowdstrike-charming-kitten-2026-q2
    context_excerpt: "New HYPERSCRAPE variant; PowerShell loader retrieves and executes."
    attribution_in_text: Charming Kitten
    notes: null

  - id: ck-oauth-app-id-2026-q2
    type: other
    value: "Attacker-controlled OAuth application — display name 'Policy Review Tool', requests Mail.Read + Mail.ReadWrite scopes"
    type_detail: "oauth_app_consent_grant"
    defanged_original: null
    first_seen: 2026-02
    last_seen: 2026-04
    role: persistence
    campaign: "Charming Kitten Q2 2026 Think-Tank Harvest"
    related_malware: []
    source_brief: crowdstrike-charming-kitten-2026-q2
    context_excerpt: "Microsoft flagged the consent-grant tradecraft as primary persistence mechanism."
    attribution_in_text: Charming Kitten
    notes: "Behavioral indicator — defenders should hunt via Entra audit logs."

attribution_claims:
  - claimed_actor: Charming Kitten
    ioc_ids:
      - ck-domain-oauth-phish-1
      - ck-domain-oauth-phish-2
      - ck-domain-c2-1
      - ck-ip-194-87-44-99
      - ck-hash-hyperscrape-2026-04-7a8b9c
      - ck-oauth-app-id-2026-q2
    claimed_by_source: crowdstrike-charming-kitten-2026-q2
    attribution_confidence_in_source: high
    requires_grading: true
  - claimed_actor: Mint Sandstorm
    ioc_ids:
      - ck-domain-oauth-phish-1
      - ck-domain-oauth-phish-2
      - ck-domain-c2-1
      - ck-ip-194-87-44-99
      - ck-hash-hyperscrape-2026-04-7a8b9c
      - ck-oauth-app-id-2026-q2
    claimed_by_source: mstic-mint-sandstorm-2026-05-04
    attribution_confidence_in_source: high
    requires_grading: true

benign_filtered:
  - value: brookings.edu
    reason: reference_site
  - value: rusi.org
    reason: reference_site
  - value: atlanticcouncil.org
    reason: reference_site
  - value: crowdstrike.com
    reason: publisher_site
  - value: microsoft.com
    reason: publisher_site

extraction_warnings:
  - type: behavioral_indicator
    ioc_id: ck-oauth-app-id-2026-q2
    detail: "OAuth application consent grant, not a hash/IP/domain. Recorded as type=other."
  - type: dual_attribution_naming
    detail: "Two A-grade sources use different names (Charming Kitten / Mint Sandstorm) for same cluster. Both attribution claims captured for grader."
```
