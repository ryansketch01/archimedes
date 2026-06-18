---
raw_id: raw-2026-06-18-am-003-sa-fortibleed-substrate-strengthening-75k-fortinet-firewalls
collected_at: 2026-06-18T07:37:00-04:00
run_id: pre-brief-20260618-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: securityaffairs
  source_name: Security Affairs (Pierluigi Paganini)
  source_url: https://securityaffairs.com/193817/hacking/fortibleed-exposes-admin-passwords-for-75000-fortinet-firewalls.html
  published_at: 2026-06-18T03:31:49-04:00
match_reason:
  watchlist: [aerospace-defense]
  actors: []
  vulnerabilities: []
  keywords: [FortiBleed, Fortinet, FortiGate, "VPN credentials", Siemens, "Turkish NATO defense contractor", Diachenko, Beaumont, "Hudson Rock", "Russian-speaking group", "credential stuffing"]
triage_tags: [substrate_pivot_update_carry_forward, ad_sector_named_victim, finding_2026_06_17_0002, substrate_strengthening_journalistic_relay, multi_ir_vendor_confirmation, ad_prime_named_siemens_explicit]
iocs_extracted: false
iocs_count: 0
text_word_count: 1100
promoted: true
promoted_to_finding: finding-2026-06-17-0002  # AM UPDATE — substrate-pivot UPDATE on existing FortiBleed finding via sixth-publisher SA-Paganini relay
promoted_at: 2026-06-18T08:14:00-04:00
ttl_expires_at: 2026-09-16T07:37:00-04:00
---

# FortiBleed Exposes Admin Passwords for 75,000 Fortinet Firewalls (SA-Paganini relay)

**Publisher:** Security Affairs (Pierluigi Paganini byline)
**Published:** 2026-06-18T03:31 EDT
**URL:** https://securityaffairs.com/193817/hacking/fortibleed-exposes-admin-passwords-for-75000-fortinet-firewalls.html

## Article body (SA-Paganini relay of SocRadar primary + Hudson Rock + Beaumont + Diachenko)

FortiBleed: Admin Passwords for 75,000 Fortinet Firewalls Are Out in the Wild. Half the Internet-Facing Fortinets on the Planet.

Security researcher Bob Diachenko found a server sitting open on the internet containing what appeared to be valid Fortinet VPN credentials, including usernames, email addresses, and plaintext passwords for tens of thousands of organizations. He posted about it on LinkedIn. Kevin Beaumont, one of the most trusted independent voices in network security, then obtained the dataset, worked through it with Hudson Rock, and confirmed what nobody wanted to hear.

Bob Diachenko on LinkedIn: "Massive Fortinet/FortiGate bruteforce/active exploitation campaign uncovered in action. Thousands of top vendors instances are listed in the files like this (see screenshot). This one alone has 21,634 domain names – from Chevron to Fortinet itself. All – with potentially working passwords to the FortiGate appliances obtained through various menas." Diachenko further: "Crooks use sophisticated hashcracking approach to get then plaintext passwords from the Fortigate configs and use them consequently in the internal network movement and takeover."

Kevin Beaumont: "The data is legit. It is around 75k devices. Almost all are still online, and Fortinet devices. It appears to be recent data." And on data source: "The data appears to have come from exports of config from the devices, as it includes things which are only visible from the device itself."

Beaumont verified credentials at multiple organizations in the dataset personally and found them working. The IP addresses in this collection are largely different from the 2025 Belsen Group leak, which covered 15,000 devices. That earlier dump was old data from a 2022 zero-day. This one isn't.

Based on Shodan polling, the FortiBleed dataset covers roughly 50% of all Fortinet firewall devices currently facing the internet.

"In a majority of cases, the Fortigate Management Interface is exposed to the internet on impacted devices."

According to Hudson Rock's analysis, the 73,932 unique firewall URLs span 194 countries and 21,632 unique domains. Names appearing in the dataset according to Hudson Rock include **Foxconn, Samsung, Comcast, Siemens, Lenovo, PwC, Accenture, Oracle**, and numerous government agencies and critical infrastructure operators. One entry in Diachenko's screenshots alone listed 21,634 domain names, including **Chevron and Fortinet itself**.

Diachenko's investigation went further after he found the attackers had accidentally left an open directory containing their own tooling, scripts, connection strings, logs, and analytics. What he found inside suggests a **Russian-speaking multi-operator threat group** conducted approximately 1.16 billion credential attempts against 320,777 FortiGate targets, plus 2.1 billion attempts against 163,650 Microsoft SQL Server systems.

The group reportedly intercepted SSL VPN authentication hashes and cracked them using a 45-GPU cluster managed through Hashtopolis. Multiple organizations across Japan, Taiwan, Vietnam, Iraq, and Turkey were described as fully compromised, including **a Turkish NATO defense contractor from which classified documents were allegedly stolen**.

The data appears to have come from exported device configurations rather than a simple credential scrape. That's a meaningful distinction: config exports contain information you can't get just by intercepting login traffic, which points toward actual device access at some point. How that access was obtained remains unknown: it may be one of the many documented Fortinet CVEs, or it may be something new.

One detail in the dataset that stands out is the business intelligence layer. Each entry includes the company's industry, revenue, employee count, and country, formatted in a way Beaumont describes as very common in criminal markets for selling initial access. This wasn't assembled for personal use. It was assembled for sale or coordinated deployment across a team.

Beaumont noted that Fortinet moved to PBKDF2 credential storage in early 2025 firmware updates, but only for devices where admins had actually logged in after applying the update. Many devices were still storing passwords as SHA-256 with salt, which is crackable via brute force from a stolen config file.

Hudson Rock published a free lookup tool at hudsonrock.com/fortinet where organizations can check if their domain appears in the dataset.

---

## Extraction notes

- Language: en
- Publisher byline: Pierluigi Paganini (SecurityAffairs Editor-in-Chief)
- Article type: trade-press journalistic relay
- Substrate role: SIXTH-publisher journalistic relay (SocRadar primary + SW + BC + DR + TR-Jones + Ars-Goodin + this SA-Paganini); FOURTH IR-vendor verification layer remains as previously enumerated (Hudson Rock + Beaumont + Diachenko/SecurityDiscovery.com + SocRadar). This SA-Paganini relay does NOT add a new independent IR-vendor verification but DOES add a sixth-publisher relay layer and consolidates direct quotes from Diachenko + Beaumont in one article.
- A&D-relevance: HIGH. Siemens (German industrial / defense conglomerate) and Turkish NATO defense contractor with classified-defense-document exfiltration claim are explicitly named. Chevron critical-infrastructure energy named. Foxconn / Samsung / PwC / Accenture / Oracle / Lenovo / Comcast / Fortinet-itself named in the broader compromised list.
- Carry-forward: This article fully matches the FortiBleed substrate-pivot UPDATE candidate flagged from 2026-06-17 18:00 sweep and reinforced through 2026-06-18 00:00 + 06:00 sweeps. Anti-noise Rule 1 applies (finding-2026-06-17-0002 published 2026-06-17 morning).
- Attribution discipline: SA-Paganini preserves Diachenko's "Russian-speaking multi-operator threat group" framing verbatim — Hard Rule 2 BINDING — Archimedes does NOT cross-walk to APT28 / Sandworm / Gamaredon / FIN6 / any roster-tracked Russia-nexus actor without an independent A-grade source making the actor-specific attribution.
- Quote-budget pre-budget for morning brief: Beaumont "the data is legit" 4-word at-cap option (best), Beaumont "around 75k devices. Almost all are still online" 8-word at-cap, Diachenko "Russian-speaking multi-operator threat group" 4-word at-cap framing. Fortinet vendor-denial framing carry-forward from prior sweeps — verbatim string 31-word OVER 15-word ceiling per Hard Rule 6 — EXCLUDED from quote citation, carried as paraphrase only.
- IOCs: no concrete network IOCs (domains / hashes / IPs / mailboxes) in this article. Hudson Rock lookup tool URL: hudsonrock.com/fortinet (informational, not an IOC).
- Anti-attribution carry-forward: ESET FishMonger cluster identity vetoed (finding-2026-06-16-0001), DragonForce/Scattered-Spider linkage Hard-Rule-2 BINDING (finding-2026-06-17-0005), UNC6508/INFINITERED 72h-FLASH-dedup window through 2026-06-18 12:00 EDT.
