---
raw_id: raw-2026-06-12-pm-004
collected_at: 2026-06-12T15:50:00-04:00
run_id: pre-brief-20260612-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: thehackernews
  source_name: The Hacker News (relaying Sygnia primary)
  source_url: https://thehackernews.com/2026/06/china-linked-hackers-backdoored-linux.html
  published_at: 2026-06-12T18:17:55+00:00
  source_grade: B (provisional) — THN; Sygnia primary not directly retrieved
match_reason:
  watchlist: []
  actors: [Velvet Ant (China-nexus, NOT in Archimedes roster)]
  vulnerabilities: []
  keywords: [Velvet Ant, Sygnia, PAM, OpenSSH, Linux backdoor, China-nexus, air-gapped, ten-year dwell, login system]
triage_tags: [new_attribution_to_corpus, china_nexus, structural_ad, supply_chain_login_system, no_iocs, new_actor_candidate_flag]
iocs_extracted: false
iocs_count: 0
text_word_count: 480
promoted: true
promoted_to_finding: finding-2026-06-12-0004
promoted_at: 2026-06-12T16:40:00-04:00
ttl_expires_at: 2026-09-10T15:50:00-04:00
---

# Sygnia documents Velvet Ant backdoor of Linux PAM and OpenSSH login system; ~10-year dwell on air-gapped East Asia victim

## What The Hacker News reports (2026-06-12T14:17 EDT)

THN relays Sygnia research on a China-nexus group tracked as Velvet Ant that backdoored the PAM (Pluggable Authentication Modules) and OpenSSH components of a victim's Linux login system. THN attribution language verbatim per article: "China-nexus group" / "China-linked." (Hard Rule 2 — attribution origination: Sygnia is the primary; THN relay preserves Sygnia's framing without escalation.)

### Technical primitives (per THN summary of Sygnia)

- **PAM (Pluggable Authentication Modules):** the main PAM login module was replaced with backdoored copies. Sygnia documents **nine separate versions** of the backdoored module.
- **OpenSSH:** OpenSSH programs were modified to log credentials and every command typed; some variants accepted secret passwords; others quietly recorded real usernames and passwords during legitimate logins.
- **Hidden disable switch:** the credential/command logging functionality includes an operator-side switch to disable it on demand (operational discipline against forensic surface).
- **Persistence philosophy:** rather than hiding on endpoints/servers defenders watch most closely, the actor "hid inside the Linux login system itself."

### Dwell time

Per article, earliest traces date to **2016** — approximately a decade of unbroken access on the victim network.

### Victim profile

- The network "had no direct internet access" — air-gapped or isolated environment.
- Located in East Asia (per Sygnia's prior public research lineage on Velvet Ant; THN article does not name the specific country).
- **No sector named** (defense / aerospace / government / financial — none called out in THN summary).

### IOCs

- THN article does not enumerate file paths, hashes, or IP addresses.
- Sygnia's primary surface may have richer IOC content; not directly retrieved this sweep.

## Hard Rule 2 — attribution discipline

- Velvet Ant is **NOT** in the Archimedes roster (_roster.yaml).
- Sygnia's verbatim attribution: "China-nexus group" / "China-linked." NOT a specific PLA / MSS unit naming, NOT mapped to APT41 / Volt Typhoon / Salt Typhoon / APT40.
- Archimedes does NOT cross-walk Velvet Ant to existing roster actors. /new-actor candidacy flag for operator decision.

### Velvet Ant prior public lineage (per article reference + open-source corpus check)

THN article references Velvet Ant's prior public activity: 2024 F5 BIG-IP appliance exploitation and 2024 CVE-2024-20399 Cisco NX-OS zero-day. Sygnia has tracked Velvet Ant since at least 2024. The pattern: Velvet Ant migrates between targets (endpoints → legacy servers → network appliances → login subsystem) within the same victim environment over multi-year campaigns. **Pre-2026 reporting is from Sygnia primarily; East Asia victim location is consistent across surfaces.**

## A&D relevance

- **Direct:** none. No A&D-prime victim named.
- **Structural:** **HIGH.** Velvet Ant's "hide in the login system itself" trade is exactly the kind of long-dwell capability A&D-prime SOCs need to defend against. The 9-variant backdoored PAM + modified OpenSSH primitives are detection-engineering-rich material (file-integrity monitoring on PAM modules; OpenSSH binary attestation; behavioral anomaly on command logging patterns).
- **A&D-prime exposure inference:** Operationally, any A&D-prime Linux fleet runs PAM + OpenSSH; the supply chain is the same supply chain Velvet Ant targeted in East Asia. Hard Rule 2 binding — Archimedes does NOT extrapolate A&D-prime targeting from East Asia campaign.

## /new-actor candidacy

- **Flag for operator:** Velvet Ant — China-nexus, long-running, login-system tradecraft, Sygnia-tracked since 2024+. Operationally meaningful for A&D SOCs.
- Operator decision pending. Archimedes does NOT initiate /new-actor in this raw-signal file.
- Compare with prior /new-actor candidate flags in corpus: OceanLotus / APT32 (raw-2026-06-11-am-001), UNC1069 (carried in source-health notes from 2026-05-09), UNC6692 (same).

## Action / brief framing

- Other Signal section item (Sector Focus does not apply); explicitly mark "NOT in Archimedes roster" + "no A&D-prime victim named."
- Highlight detection-engineering surfaces (PAM module file-integrity monitoring; OpenSSH binary attestation; secret-password-acceptance behavioral pattern) for Threat Detection Weekly synthesis.
- Watch item: Sygnia primary direct retrieval at next collector pass (high-value, may carry IOCs not in THN relay).

## Watch items

- Sygnia primary URL direct retrieval (https://www.sygnia.co/blog/) — pending for next sweep.
- Second-IR-firm corroboration of Velvet Ant attribution or technical primitive.
- Any A&D-prime SOC reporting of PAM-module integrity anomalies in the next 60 days.
- /new-actor operator decision on Velvet Ant.

## Extraction notes

- Language: en
- Article type: security trade press relay of vendor research
- IOCs: none in THN article. Sygnia primary not directly retrieved.
- Direct retrieval: THN only; Sygnia blog https://www.sygnia.co/blog/ flagged for next pass.
