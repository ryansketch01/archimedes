---
raw_id: raw-2026-06-03-pm-002-symantec-stock-exchange-outlook-mailbox-espionage-150-days-aspose-dropbox-onedrive-personal-no-attribution
collected_at: 2026-06-03T15:34:00-04:00
run_id: pre-brief-20260603-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: symantec                            # Provisional A per source-grades.yaml entry symantec (first-citation 2026-05-13 FLASH MuddyWater/Seedworm Q1 2026 multi-victim campaign; awaiting human ratification). Source-grade not yet ratified.
  source_name: Symantec Threat Hunter Team + Carbon Black — five-month suspected-espionage Outlook mailbox theft against major global stock exchange executive
  source_url: https://www.security.com/threat-intelligence/                 # Vendor-published primary; specific URL not captured this sweep — known to be referenced as "security.com" in SecurityWeek + SecurityAffairs relays
  published_at: 2026-06-03T00:00:00-04:00              # "this week" per SecurityAffairs; relays appeared 12:46 UTC (SecurityWeek) and 18:13 UTC (SecurityAffairs) — in-window
source_grade: A (provisional per source-grades.yaml — Symantec Threat Hunter Team + Carbon Black; first-party EDR telemetry; Broadcom-owned; long-running Seedworm taxonomy primacy)
additional_sources:
  - source_yaml_id: securityweek
    source_url: https://www.securityweek.com/hackers-target-global-stock-exchange-in-espionage-operation/
    source_grade: B
    role: "Tier-2 relay — Eduard Kovacs byline; surfaced 2026-06-03 12:46 UTC = 08:46 EDT"
  - source_yaml_id: securityaffairs
    source_url: https://securityaffairs.com/193086/intelligence/cyber-espionage-campaign-targeted-stock-exchange-executives-outlook-account.html
    source_grade: B
    role: "Tier-2 relay — Pierluigi Paganini byline; surfaced 2026-06-03 18:13 UTC = 14:13 EDT; carries fuller body text and additional defender framing"
date: 2026-06-03
topic: symantec-carbon-black-suspected-state-linked-espionage-stock-exchange-executive-outlook-150-day-aspose-wrapper-dropbox-onedrive-personal-hardcoded-microsoft-ips-no-actor-attribution
match_reason:
  watchlist: []                                       # No A&D-watchlist entity. "Major global stock exchange" is financial-sector, not A&D-sector. Symantec explicitly does not name the exchange.
  actors: []                                          # NO attribution to any tracked roster actor. Symantec verbatim per SecurityWeek: "did not share any information about who may have been behind the attack". Most-likely-espionage hedge preserved verbatim per Hard Rule 2.
  vulnerabilities: []                                 # No CVE / no vulnerability exploited per the available reporting; the entry vector "remains unknown" per SecurityAffairs body text.
  keywords:
    - Symantec Threat Hunter Team
    - Carbon Black
    - Broadcom
    - "stock exchange"
    - Outlook mailbox theft
    - OST to PST extraction
    - Aspose
    - "Aspose-wrapper"
    - .NET library
    - "150-day dwell time"
    - Dropbox exfiltration
    - "OneDrive Personal exfiltration"
    - "hardcoded Microsoft IP addresses"
    - "DNS logging bypass"
    - "Adobe Acrobat masquerading"
    - "OneDrive process masquerading"
    - "Lenovo masquerading"
    - SYSTEM-privilege binary
    - "scheduled task persistence rotation"
    - "5-minute / 5-hour / 15-hour / 24-hour scheduled task rotation"
    - "state-linked"                                  # Symantec's hedged framing; preserved verbatim
    - "most likely espionage"                         # Verbatim hedge from Symantec primary as relayed
triage_tags: [pm_pre_brief, tier1_vendor_research, espionage_campaign, no_actor_attribution, hedge_preserved, single_victim, no_a_d_watchlist_hit, reusable_ttps_against_a_d, ioc_set_published_at_primary, splunk_pivot_ready]
iocs_extracted: false                                 # Symantec primary not directly fetched this sweep; SecurityAffairs notes "Symantec and Carbon Black have published the full list of indicators of compromise, including file hashes for the mailbox stealer and the various masquerading executables, at security.com." Grader / actor-profiler can invoke ioc-extraction on Symantec primary directly if dossier work is undertaken.
iocs_count: 0
text_word_count: ~900
promoted: true
promoted_to_finding: finding-2026-06-03-0006-symantec-carbon-black-stock-exchange-outlook-150-day-espionage-aspose-dropbox-onedrive-no-attribution-reusable-ttps-against-ad
promoted_at: 2026-06-03T16:18:00-04:00
promoted_grading_run_id: afternoon-20260603-160000
ttl_expires_at: 2026-09-01T15:34:00-04:00
---

# Symantec + Carbon Black publish 150-day suspected-espionage Outlook mailbox theft against major global stock exchange executive — no actor attribution, no A&D-prime victim named; reusable TTPs (Aspose-wrapped OST→PST conversion, Dropbox/OneDrive Personal exfil, hardcoded Microsoft IPs to bypass DNS logging)

## What the source says (Symantec Threat Hunter Team + Carbon Black, via SecurityAffairs + SecurityWeek relays)

Symantec's Threat Hunter Team and Carbon Black threat-hunting team have published a joint write-up on a five-month suspected-espionage compromise of a major global stock exchange. SecurityAffairs (Pierluigi Paganini, 2026-06-03T18:13 UTC = 14:13 EDT, in-window) and SecurityWeek (Eduard Kovacs, 2026-06-03T12:46 UTC = 08:46 EDT, in-window) carry the relay.

Key facts from the source as relayed:

- **Target:** unidentified "major global stock exchange." Symantec explicitly does not name the exchange. SecurityAffairs frames this as financial-sector + market-sensitive-information rationale.
- **Victim profile:** a single senior executive's Outlook mailbox. The compromise is described as scoped to that mailbox; no lateral movement off the original host is reported.
- **Dwell time:** approximately 150 days, from 2025-10-10 to 2026-03-19. First malicious activity 2025-10-10 with two SYSTEM-privilege binaries already running disguised as Adobe Acrobat and OneDrive processes. Operation went active 2025-11-12 with C2 and exfil channels online. Last new binary 2026-03-19 (Adobe driver component masquerade).
- **Entry vector:** unknown ("how the attacker got in initially remains unknown" per SecurityAffairs).
- **Core tradecraft:** wrapper around **Aspose** — a legitimate commercial .NET library that can parse Outlook mailbox files. The wrapper converted the executive's OST file into a PST archive and pushed it out in dated chunks, each covering a window of a few weeks. **Eight further OST-extraction runs followed at roughly two-to-four-week intervals through 2026-02-17**, with `-t` time-window parameters that adjoined the previous run's window (cumulative effect: complete near-continuous theft).
- **Exfiltration:** Dropbox and OneDrive Personal. Both blend with normal corporate traffic. The attacker hardcoded Microsoft IP addresses (not hostnames) for OneDrive calls — bypasses DNS-based logging entirely.
- **Persistence:** scheduled tasks re-registered every few weeks under names mimicking Adobe, Lenovo, and OneDrive services. Task intervals rotated between 5-minute, 5-hour, 15-hour, and 24-hour windows. Each new registration overwrote the previous one (footprint minimization).
- **Binary masquerading rotation:** 2025-10-10 initial Adobe Acrobat + OneDrive masquerade. 2026-02-27 new binary masquerading as OneDrive sync service. 2026-03-19 new binary masquerading as Adobe driver component.

## Attribution language — preserved verbatim per Hard Rule 2

SecurityWeek verbatim:

> "Symantec and Carbon Black did not share any information about who may have been behind the attack or which stock exchange was targeted."

SecurityAffairs verbatim, paraphrasing Symantec's reading:

> "the operation was tightly scoped, technically disciplined, and almost certainly state-linked given the target and the patience involved."

> "The use of public tools, cloud infrastructure for both C2 and exfiltration, and no reuse of infrastructure tied to known groups all make attribution very difficult."

**No tracked roster actor is named.** No nation-state attribution is claimed. The "state-linked" framing is Symantec's analytic judgment based on operational discipline + target value, NOT a formal moderate/high-confidence attribution. Grader should preserve "suspected espionage" / "almost certainly state-linked" hedges verbatim and not upgrade.

## A&D relevance analysis

**No A&D-watchlist entity named.** Financial-sector single-victim. Below the 12:00 FLASH Trigger 5 bar (A&D campaign requires named A&D entity).

**But the TTPs are reusable against A&D primes by a similar actor.** Worth grader attention because:

1. **Aspose-wrapper OST→PST extraction is platform-agnostic.** Any Outlook-using enterprise (which is every A&D prime) has the same exposure if the executive endpoint is compromised. Mailbox theft is a classic intelligence-collection objective against A&D leadership (contract negotiations, supplier discussions, M&A communications, classified-program scheduling at the metadata level, sensitive HR / personnel decisions).
2. **Dropbox + OneDrive Personal exfil bypass for an A&D prime** is exactly the M365 + sanctioned-cloud-services blend that DIB SOCs struggle to distinguish from normal user behavior. ITAR / CUI environments may have policy restrictions on Personal cloud accounts but enforcement gaps are common.
3. **Hardcoded Microsoft IP DNS-bypass is a procedural lesson** for any environment relying on DNS-tier blocklisting or DNS-anomaly detection as primary egress control. Re-evaluate IP-tier outbound monitoring.
4. **Scheduled task rotation + 5-minute / 5-hour / 15-hour / 24-hour windowing** is an EDR-evasion procedural signature that any A&D SOC running Defender or Carbon Black can build hunts against. The published IOCs at security.com include the binary hashes that would surface this pattern.

## Defender pivot (for the grader's brief composition consideration)

- **Symantec published IOCs at security.com** (per SecurityAffairs verbatim: "Symantec and Carbon Black have published the full list of indicators of compromise, including file hashes for the mailbox stealer and the various masquerading executables, at security.com").
- **Splunk first-party pivot** — once IOC set is extracted, the hashes can be queried against `archimedes` and `defenseclaw_local` indexes. No first-party hits in this sweep window (Splunk first-party check returned zero non-archimedes-internal events over last 24h per PM-000 sentinel).
- **Splunk hunt suggestions** even without IOCs:
  - Outlook `OST → PST` conversion processes invoking Aspose namespace assemblies (`Aspose.Email`, `Aspose.Email.dll`)
  - Scheduled task registration with names containing "Adobe", "OneDrive", "Lenovo" service-mimicking patterns and unusual rotation intervals
  - Outbound HTTPS connections to Dropbox / OneDrive Personal (graph.microsoft.com or onedrive.live.com vs sanctioned `*.sharepoint.com` tenancy) from cleared-personnel endpoints
  - SYSTEM-level processes with Adobe Acrobat or OneDrive masquerade file paths outside the canonical install directories

## Coverage hierarchy

- **Primary:** Symantec Threat Hunter Team + Carbon Black joint write-up on security.com (vendor-public; published "this week")
- **Tier-2 relays:** SecurityWeek + SecurityAffairs (both in-window today)
- **Note on Symantec source-grade:** provisional A per source-grades.yaml `symantec` entry (first-citation 2026-05-13 FLASH MuddyWater/Seedworm Q1 2026 multi-victim campaign). Awaiting human ratification. This is the SECOND Archimedes-corpus citation for Symantec — the 72h ratification clock from 2026-05-13T18:25 has long elapsed; the operator-side ratification path remains open. The Symantec primary's analytic discipline (refusing attribution despite operational discipline + target value pointing at state-linked espionage) is itself a positive ratification signal.

## Sources

- SecurityWeek relay (primary in-window): https://www.securityweek.com/hackers-target-global-stock-exchange-in-espionage-operation/
- SecurityAffairs relay (primary in-window, fuller body text): https://securityaffairs.com/193086/intelligence/cyber-espionage-campaign-targeted-stock-exchange-executives-outlook-account.html
- Symantec primary (vendor-publication root, specific URL not yet captured): https://www.security.com/threat-intelligence/

## Extraction notes

- Language: en
- Article type: vendor threat-research relay + originating-vendor blog (Symantec primary not directly fetched this sweep)
- Raw IOC extraction invoked: no — Symantec primary not fetched; SecurityAffairs notes IOC set is published at security.com. Grader / actor-profiler can invoke ioc-extraction on Symantec primary directly.
- No PoC code reproduced per Hard Rule 3.
- No credentials surfaced.
- Symantec verbatim attribution hedges preserved per Hard Rule 2.
- Cross-reference for source-grade-log: Symantec second-corpus-citation 2026-06-03 PM via this raw-signal. If operator wishes to ratify the 2026-05-13 provisional A on this surface, the second-citation analytic discipline + named-byline + published-IOC-set provide ratification evidence.
