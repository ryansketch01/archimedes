---
raw_id: raw-2026-07-14-pm-006
collected_at: 2026-07-14T15:39:40-04:00
run_id: pre-brief-20260714-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: bleepingcomputer
  source_name: BleepingComputer (originating research ReliaQuest)
  source_url: https://www.bleepingcomputer.com/news/security/new-phishing-kits-target-microsoft-365-accounts-evade-mfa/
  published_at: 2026-07-14T08:49:00-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [Microsoft 365, phishing kit, MFA bypass, OAuth device code, Entra ID, SharePoint exfiltration]
triage_tags: [ttp_awareness, mfa_bypass, identity_layer, ad_structural, flash_1200_handoff]
iocs_extracted: true
iocs_count: 0
text_word_count: 210
promoted: true
promoted_to_finding: finding-2026-07-14-0009
promoted_at: 2026-07-14T16:03:00-04:00
ttl_expires_at: 2026-10-12T15:39:40-04:00
---

# New M365 phishing kits Jalisco and OmegaLord evade MFA — OAuth device-code abuse + phone-number capture (ReliaQuest)

ReliaQuest identified two phishing toolkits targeting Microsoft 365 accounts, both engineered to defeat MFA. (Carried forward from the 12:00 FLASH sweep non-FLASH grader queue; formalized to raw-signal this pre-brief.)

**Jalisco:**
- Abuses the OAuth 2.0 Device Authorization Grant flow.
- Generates fresh Microsoft OAuth device codes in real time to beat Microsoft's 15-minute code validity window.
- Includes an operator web portal to manage compromised accounts.
- Registers multiple rogue devices per account (up to 5), using benign names like "Microsoft" or "Windows."

**OmegaLord:**
- Uses fake PDF Reader login pages.
- Collects email addresses, passwords, and phone numbers; the phone-number capture is specifically engineered to bypass MFA.

**Post-compromise:** actors search SharePoint and SaaS services for valuable data and exfiltrate within minutes (as little as 6 minutes) before detection, then make extortion demands threatening leaks.

**Defenses noted:** reduce Entra ID device-registration limits (50 → 1-2), block device-code authentication via Conditional Access, restrict OAuth Device Authorization grants, audit unnecessary app registrations.

No specific domains, URLs, IPs, hashes, targeted sectors, or threat-actor attribution were provided.

---

## Extraction notes

- Language: en
- Publisher byline: Bill Toulas (BleepingComputer); originating research ReliaQuest (no prior Archimedes source grade — would be provisional on first citation)
- Article type: news
- Raw IOC extraction invoked: yes — no atomic IOCs published (kit names Jalisco / OmegaLord are researcher-coined tooling designations, not IOCs)
- A&D relevance: structural — M365 / Entra ID is the dominant identity and collaboration fabric across the DIB; OAuth device-code MFA-bypass plus rapid SharePoint exfiltration is a directly portable TTP against A&D-prime tenants. No named A&D victim; relevance is TTP-class.
- No actor attribution present; none originated (Hard Rule 2). No credentials handled (Hard Rule 7 — n/a, none present).

## IOCs (from ioc-extraction skill)

```yaml
extraction_metadata:
  source_brief_id: raw-2026-07-14-pm-006
  source_url: https://www.bleepingcomputer.com/news/security/new-phishing-kits-target-microsoft-365-accounts-evade-mfa/
  extracted_at: 2026-07-14T15:39:40-04:00
  extracted_by: collector
  target_actor_id: null
  text_word_count: 210

indicators: []

attribution_claims: []

benign_filtered: []

extraction_warnings:
  - type: no_atomic_iocs
    ioc_id: null
    detail: "Source published no domains/URLs/IPs/hashes. Tooling names Jalisco + OmegaLord recorded as campaign/tooling context, not IOCs. Grader may seek ReliaQuest primary for indicator appendix."
```
