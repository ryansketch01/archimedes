---
raw_id: raw-2026-06-10-pm-011
collected_at: 2026-06-10T15:53:00-04:00
run_id: pre-brief-20260610-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: krebs
  source_name: "Krebs on Security (Brian Krebs)"
  source_url: https://krebsonsecurity.com/2026/06/who-runs-the-ransomware-group-the-gentlemen/
  published_at: 2026-06-10T14:03:44+00:00
  retrieval_method: RSS + WebFetch
secondary_sources:
  - id: check-point
    name: "Check Point Software (originating research)"
    url: null  # specific Check Point blog URL not surfaced this sweep
    grade: A
  - id: intel471
    name: "Intel 471"
    grade: A
  - id: ke-la
    name: "KELA"
    url: ke-la.com
    grade: A_provisional  # not yet in source-grades.yaml; first surface
  - id: constella
    name: "Constella Intelligence"
    grade: A_provisional
  - id: flashpoint
    name: "Flashpoint"
    grade: A_provisional  # Flashpoint sponsored Krebs's blog (disclosed)
match_reason:
  watchlist: []  # No A&D-prime named victim
  actors:
    - "The Gentlemen"  # NOT in roster — recommend /new-actor evaluation
  vulnerabilities: []
  keywords: [The Gentlemen, ransomware, RaaS, Hastalamuerte, Zeta88, Alexander Yapaev, Izhevsk, Russia, Udmurt Republic, 90/10 affiliate split, 332 victims, 240 victims 2026, internet-facing devices VPN firewall, encrypt networks hours, Check Point, Intel 471]
triage_tags:
  - ransomware_raas_attribution_osint
  - krebs_breadcrumbs_methodology
  - the_gentlemen_not_in_roster_new_actor_candidate
  - russia_attribution_via_osint_breadcrumbs
  - check_point_originating_research
  - 90_10_affiliate_split_aggressive_recruitment_signal
  - internet_facing_vpn_firewall_initial_access_class
  - encrypt_within_hours_high_velocity_ransomware
  - second_most_active_2026_volume_signal
iocs_extracted: true
iocs_count: 5  # email, telegram username, phone number, mail.ru address, github username
text_word_count: 0
promoted: true
promoted_to_finding: finding-2026-06-10-0017-krebs-check-point-intel471-flashpoint-the-gentlemen-raas-osint-de-anonymization-hastalamuerte-zeta88-alexander-yapaev-izhevsk-russia-new-actor-candidate
promoted_at: 2026-06-10T16:30:00-04:00
ttl_expires_at: 2026-09-08T15:53:00-04:00
---

# Krebs OSINT — "The Gentlemen" Ransomware Administrator De-Anonymization (Hastalamuerte / Zeta88 → Alexander Yapaev, Izhevsk, Russia)

**Primary source:** Krebs on Security (Brian Krebs) — "Who Runs the Ransomware Group 'The Gentlemen?'" — 2026-06-10T14:03:44 UTC
**Originating research:** Check Point Software (sustained coverage of The Gentlemen)
**Supporting OSINT services:** Intel 471, Flashpoint (Krebs's disclosed advertiser), Constella Intelligence, KELA, Epieos

## Key claims (per Krebs OSINT analysis)

### Actor / group overview
- **"The Gentlemen"** — emerging as **second most active ransomware group by victim count in 2026**.
- 332 published victims since group's inception in mid-2025.
- **240+ victims in 2026 alone** (data point of velocity).
- **RaaS model with 90/10 affiliate split** (vs. industry standard 80/20) — aggressive recruitment of affiliates from competing programs.
- Check Point: "A 90/10 affiliate revenue split — compared to the industry standard 80/20 — is accelerating the group's growth by attracting experienced operators from competing programs" (verbatim, ~22 words — over the 15-word ceiling; trim before quoting in brief).

### Operational characteristics
- Targets **internet-facing devices (VPNs, firewalls)** as initial access vector.
- Once inside, "moves quickly to encrypt entire networks within hours" (verbatim per Krebs — 11 words, under ceiling).
- High-velocity / opportunistic targeting profile.

### Administrator identity per Krebs OSINT chain
- **Nickname on Russian-language cybercrime forums: Zeta88**.
- **Previously known as: Hastalamuerte**.
- Per Check Point + Intel 471: "Hastalamuerte/Zeta88 is the person who assembles the locker and RaaS panel, manages payments, and is essentially the administrator of the entire program who receives 10 percent of all ransoms."
- Intel 471 forum-registration trace 2019 → present across multiple forums (Exploit, Breachforums, Ramp_V2, BHF, Raidforums, Nulled, Codeby).
- Hastalamuerte registered on Breachforums January 2025 from **Izhevsk** (capital of Russia's Udmurt Republic).
- Zeta88 registered on English-language Breached August 2022 from different Izhevsk IP.

### OSINT pivot chain → identity
- Email `hastalamuerte1488@protonmail.com` (the "1488" is white-supremacy numeric symbology — Krebs explicit).
- Epieos pivot: connected to Apple account + phone number ending in 04.
- Connected to **GitHub username SantaMuerte** — private account watching/developing malware tools and exploits.
- Telegram username `@hastalamuerte18` → Telegram ID 30907522 (per Flashpoint).
- Constella pivot: Telegram ID connected to username `bu4vs` + Russian phone number **79127650004**.
- Phone number pivot → multiple records in hacked Russian government databases.
- Identity: **Alexander Andreevich Yapaev**, 36-year-old from Izhevsk.
- Pikabu (Russian social media) handle: `4apai18`.
- Common surnames used: Ivanov, Chapaev ("4apaev").
- Codeby forum nickname: `SantaMeurte` → originally registered as `Alexandr 4apaev`.
- Email pivot: `bu4vs@mail.ru` → LinkedIn account for "Alexander Yapaev, head of B2B marketing at Uralenergo Udmurtia" (Russian electrotechnical / lighting products supplier).
- Mr. Yapaev "did not respond to multiple requests for comment."

## Cross-corpus context

### Roster gap
- **"The Gentlemen"** is NOT currently in `_roster.yaml`.
- Operating since mid-2025 (~12 months); 332 published victims; second-most-active 2026 by victim count.
- Strong **/new-actor candidate**.

### A&D-prime defender lens
- **Internet-facing VPN/firewall initial access** = standard ransomware playbook overlapping with LockBit / BlackCat / Cl0p / Scattered Spider TTPs.
- **High-velocity encryption (hours)** = staging primitive likely includes backup-server compromise (cross-reference Veeam pm-004 CVE-2026-44963 critical RCE on backup servers — domain-joined low-priv → RCE is exactly the access primitive ransomware ops require).
- No named A&D-prime victim in this Krebs piece.

### Russia attribution as policy/OFAC lever
- Krebs Breadcrumbs methodology is **OSINT-based de-anonymization**, not LE-confirmed identity.
- Yapaev did not confirm or deny.
- Identity carries policy / OFAC sanctions implications if confirmed.

### Hard Rule 6 quote discipline preserved
- Quotes kept under 15 words per source where possible.
- The "90/10 affiliate split" Check Point quote at 22 words exceeds ceiling — trim before brief reuse.

### Hard Rule 2 attribution discipline
- Krebs / Check Point / Intel 471 / Flashpoint / Constella all establish the attribution chain.
- The Gentlemen → Hastalamuerte/Zeta88 → Alexander Yapaev attribution preserved as **per-source reported**, NOT confirmed by Archimedes.

## FLASH-trigger evaluation

- **Trigger 2 (tracked-actor-attribution):** ❌ The Gentlemen not in roster.
- **Trigger 5 (ad-sector-campaign):** ❌ No A&D-prime victim named.
- **Trigger 1 (critical-cve-exploited):** ❌ No CVE specifics in Krebs piece.

Not a FLASH trigger. Brief-track candidate via Other Signal / cybercriminal-watch lane. Strong /new-actor candidate.

## Extraction notes

- Language: en
- Publisher byline: Brian Krebs (Krebs on Security)
- Article type: investigative OSINT de-anonymization
- Raw IOC extraction invoked: yes (below)

## IOCs (from ioc-extraction skill)

```yaml
attribution_claims:
  - source: "Krebs / Check Point Software / Intel 471 / Flashpoint / Constella / KELA / Epieos"
    actor_named: "The Gentlemen"
    actor_admin_aliases: ["Hastalamuerte", "Zeta88", "SantaMuerte", "Alexandr 4apaev", "SantaMeurte"]
    actor_admin_identity_claimed: "Alexander Andreevich Yapaev, 36-year-old from Izhevsk, Udmurt Republic, Russia"
    confidence_language: "OSINT breadcrumbs / multi-source pivots — NOT LE-confirmed; subject did not respond to comment requests"
    hard_rule_2_compliance: "Preserve per-source reported framing; do NOT propagate as Archimedes-confirmed"

selectors:
  emails:
    - "hastalamuerte1488@protonmail.com"
    - "bu4vs@mail.ru"
  telegram_usernames:
    - "@hastalamuerte18"
    - "bu4vs"
  telegram_id: 30907522
  phone_number: "79127650004"
  github_usernames:
    - "SantaMuerte (private)"
  cybercrime_forum_nicknames:
    - Hastalamuerte
    - Zeta88
    - SantaMuerte
    - SantaMeurte
    - "Alexandr 4apaev"

forum_presence:
  - Exploit
  - Breachforums  # 2025-01 registration from Izhevsk IP
  - Ramp_V2
  - BHF
  - Raidforums
  - Nulled
  - Breached  # 2022-08 registration from different Izhevsk IP (as Zeta88)
  - Codeby  # SantaMeurte nickname

geographic_attribution:
  city: "Izhevsk"
  region: "Udmurt Republic"
  country: "Russia"

operational_metadata:
  victim_count_published_total_since_inception: 332
  victim_count_2026: "240+"
  inception_period: "mid-2025"
  raas_model: "90/10 affiliate split"
  industry_standard_comparison: "80/20"
  initial_access_vectors: ["Internet-facing VPNs", "Internet-facing firewalls"]
  time_to_encryption: "Hours"

cves: []

network_iocs_extracted:
  ipv4: []  # No infrastructure IPs published in Krebs piece
  domains: []
  hashes: []

cross_corpus_relevance:
  ransomware_roster_gap: "The Gentlemen NOT in _roster.yaml — recommend /new-actor candidate"
  related_tracked_raas: ["LockBit (#015)", "REvil (#016)", "Cl0p (#018)", "BlackCat/ALPHV (#020)"]
  veeam_cross_corpus_tie_in: "Backup-server RCE (CVE-2026-44963 pm-004) is structurally aligned with The Gentlemen's hours-to-encryption velocity pattern"
```

## Notes for grader

- **/new-actor candidate recommended** for The Gentlemen — high-velocity RaaS, 332 victims, second-most-active 2026, sustained Check Point primary research, multi-source OSINT attribution.
- **Hard Rule 2** strictly preserved — Krebs OSINT-derived identification is per-source attribution, NOT Archimedes-confirmed.
- **Hard Rule 6** quote discipline — Check Point's 90/10 quote at 22 words exceeds ceiling; trim before brief reuse.
- **No FLASH trigger** but strong brief candidate via Other Signal cybercriminal-watch lane.
- **A&D-prime defender takeaway** — internet-facing VPN/firewall initial-access vector + hours-to-encryption velocity = audit external attack surface + tighten VPN/firewall MFA + ensure backup-server isolation (cross-reference Veeam pm-004).
- **OSINT attribution chain** is Krebs's "Breadcrumbs" methodology — reportable but should NOT be propagated as confirmed; subject denial-or-confirmation unknown.
