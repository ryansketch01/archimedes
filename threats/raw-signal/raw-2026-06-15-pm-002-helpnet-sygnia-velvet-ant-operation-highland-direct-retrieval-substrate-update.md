---
raw_id: raw-2026-06-15-pm-002
collected_at: 2026-06-15T15:38:00-04:00
run_id: pre-brief-20260615-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: helpnetsecurity
  source_name: Help Net Security (Zeljka Zorz byline)
  source_url: https://www.helpnetsecurity.com/2026/06/15/velvet-ant-backdoored-authentication-persistence/
  published_at: 2026-06-15T15:27:11+00:00
related_primary:
  - source_yaml_id: sygnia-research
    source_name: Sygnia (Operation Highland blog post)
    source_url: https://www.sygnia.co/blog/
    primary_post_title: "Velvet Ant's Operation Highland: How a China-Nexus Actor Infiltrated an Internal Network Undetected"
    primary_post_date: 2026-06-08
    primary_post_reading_time: "21 minutes"
match_reason:
  watchlist: []
  actors: []   # Velvet Ant NOT on Archimedes 24-actor roster — Hard Rule 2 preserved, NO cross-walk
  vulnerabilities: []
  keywords: [Velvet Ant, China-nexus, China-linked, decade-long-dwell, PAM module backdoor, OpenSSH credential capture, SOCKS5 proxy, GS-Netcat reverse shell, ssspl, Sygnia primary]
triage_tags: [primary_direct_retrieval, substrate_update_on_prior_finding, china-nexus, multi-year-dwell, authentication-stack-backdoor, NOT-ad-prime-named, anti-noise-hold-update]
iocs_extracted: true
iocs_count: 0
text_word_count: 580
promoted: true
promoted_to_finding: finding-2026-06-15-0007-helpnetsecurity-sygnia-velvet-ant-operation-highland-direct-retrieval-9-pam-variants-ssspl-socks5-gs-netcat-update-on-finding-2026-06-12-0004
promoted_at: 2026-06-15T16:14:00-04:00
ttl_expires_at: 2026-09-13T15:38:00-04:00
---

# China-linked spies backdoored authentication stack to stay hidden for years

**HelpNet Security (Zeljka Zorz)** — 2026-06-15 15:27 UTC

A China-linked cyber espionage group known as Velvet Ant spent nearly a decade inside the
internal network of an unnamed organization without being detected, according to the results
of a forensic investigation published by cybersecurity firm Sygnia.

The group's defining characteristic is the ability to maintain stealthy years-long persistence
in target environments. In this particular case, booting them out also took considerable effort,
as they managed to gain control of the full authentication stack by modifying PAM modules and
OpenSSH binaries.

## Sygnia primary direct retrieval

Sygnia primary blog post **directly retrieved this sweep**:
- **Title**: "Velvet Ant's Operation Highland: How a China-Nexus Actor Infiltrated an Internal Network Undetected"
- **Published**: 2026-06-08
- **Reading time**: 21 minutes
- **Categories**: Attack Techniques, Cyber Crime, Detection, Ransomware (Sygnia tag set)
- **URL**: https://www.sygnia.co/blog/ (post-level URL not visible from index)

This resolves the previously-flagged `awaiting_direct_retrieval: true` on the
`sygnia-research` source ID (provisional B since 2026-06-12 via finding-2026-06-12-0004).

## Velvet Ant attribution language (per Sygnia / HelpNet verbatim)

- **Sygnia**: "China-Nexus Actor" (per post title); "China-linked cyber espionage group"
  (per HelpNet relay)
- **Hard Rule 2 preserved**: Sygnia attribution string is "China-nexus" / "China-linked";
  collector does NOT originate cross-walk to APT41 / Volt Typhoon / Salt Typhoon / APT40 /
  UNC6508 or any roster-tracked actor.

## Victim profile

- **Organization**: UNNAMED in both Sygnia primary post title and HelpNet relay
- **Sector**: NOT disclosed
- **Country**: NOT disclosed
- **Dwell time**: Nearly a decade (~9-10 years) undetected

## TTP chain (per HelpNet relay of Sygnia primary)

1. Initial access method NOT disclosed in the relay
2. Deployed modified **GS-Netcat** utility for reverse shell to C2
3. Leveraged modified **Nginx** configurations and custom SSH-triggering binary
4. Established SOCKS5 proxy tunneling using **custom `ssspl` implementation**
5. Compromised authentication layer through PAM and OpenSSH modifications

## Authentication-stack backdoor detail

- **Nine distinct `_pam_unix.so_` variants** identified, each built in a separate compile
  environment
- Functions: hardcoded password bypass + silent credential logging
- Modified SSH binaries: captured both incoming and outgoing credentials, logged commands,
  encrypted storage with filesystem obfuscation
- Appended unauthorized keys to `authorized_keys` files for persistence

## IOCs published

**HelpNet relay does NOT publish hashes, IPs, domains, or file paths.** The Sygnia primary
21-minute post likely carries IOCs; direct fetch of the post-level URL (not the blog index)
recommended for grader / actor-profiler if Velvet Ant is added to the roster.

## CVE / KEV references

No CVE references mentioned by HelpNet or Sygnia in the retrievable substrate.

## A&D relevance

**No military, defense, or critical infrastructure sector identified** in the HelpNet relay
of the Sygnia primary. Victim sector is undisclosed. A&D relevance is at the **tradecraft-class
level only** (China-nexus full-authentication-stack backdoor pattern is materially relevant
to A&D-prime / DIB Linux estates running OpenSSH + PAM stacks, which is universal at
Tier-1/2 contractors).

## Remediation challenges (per Sygnia primary)

Complexity involved testing across multiple Linux distributions before production deployment,
with rollback contingencies required.

---

## Extraction notes

- Language: en
- Publisher byline: Zeljka Zorz (HelpNet Security)
- Primary research: Sygnia (Operation Highland, 2026-06-08, 21-minute deep dive)
- Article type: vendor-research relay + analyst-byline coverage
- Raw IOC extraction invoked: yes (zero IOCs in retrievable substrate)

## IOCs (from ioc-extraction skill)

```yaml
iocs:
  hashes: []
  ips: []
  domains: []
  urls: []
  file_paths: []
  cves: []

attribution_claims:
  - source: Sygnia (Operation Highland primary, 2026-06-08)
    actor: "Velvet Ant"
    actor_description: "China-Nexus Actor" (post title verbatim) / "China-linked cyber espionage group" (HelpNet relay verbatim)
    confidence: HIGH (Sygnia primary, vendor-attested; Sygnia provisional B per source-grades.yaml since 2026-06-12 via finding-2026-06-12-0004; provisional A candidacy on second-surface direct retrieval)
    note: |
      Hard Rule 2 preserved — Sygnia attribution string is "China-Nexus" / "China-linked";
      collector does NOT originate cross-walk to APT41 / Volt Typhoon / Salt Typhoon / APT40 /
      UNC6508 or any roster-tracked actor. Velvet Ant is NOT on Archimedes 24-actor _roster.yaml.
      Operator-deferred /new-actor candidacy substrate-strengthening per Hard Rule 5 (collector
      does NOT originate roster addition; if operator invokes /new-actor Velvet Ant the
      actor-profiler subagent scaffolds dossier with Sygnia primary substrate).

ttp_details:
  initial_access: undisclosed_in_relay
  reverse_shell_tool: GS-Netcat (modified)
  pivot_tooling:
    - "Nginx configurations (modified)"
    - "custom SSH-triggering binary"
    - "custom ssspl SOCKS5 proxy implementation"
  authentication_backdoor:
    - "9 distinct _pam_unix.so_ variants (per-environment-compiled)"
    - "Modified OpenSSH server binaries (credential capture + command logging + encrypted storage + filesystem obfuscation)"
    - "Persistence via authorized_keys append"
  dwell_time: "~9-10 years (nearly a decade)"

anti_noise_disposition: SUBSTRATE_UPDATE
anti_noise_reasoning: |
  Carry-forward anti-noise hold from previous-day pipeline: "Velvet Ant Operation Highland
  Sygnia primary pending" (per FLASH 12:00 commit c48f6fc carry-forward + morning brief
  finding-2026-06-12-0004 substrate). This sweep provides:
    1. Sygnia primary now directly retrievable (was relay-only via THN at 2026-06-12);
    2. Direct-retrieval substrate enables Sygnia source-ID `awaiting_direct_retrieval` flag
       removal (operator-deferred);
    3. HelpNet adds independent B-grade publisher-side relay (Zorz byline);
    4. New TTP detail surfaced: 9-variant PAM modules, custom ssspl SOCKS5, GS-Netcat
       reverse shell — all NET-NEW vs the THN 2026-06-12 relay substrate.
  Substrate-update is grader-decision territory; collector marks NET-NEW + pending hold lift.

direct_retrieval_recommendation: |
  HIGH PRIORITY for grader/actor-profiler — retrieve Sygnia post-level URL (sygnia.co/blog/
  individual permalink, not index) to obtain:
    - Full IOC enumeration (hashes, IPs, domains, file paths)
    - Victim sector/country if disclosed
    - Initial access vector
    - Detection/eviction timeline detail
    - C2 infrastructure detail beyond GS-Netcat tooling note
  This is the substrate that would feed an actor-profiler scaffold if operator invokes
  /new-actor Velvet Ant.

flash_trigger_evaluation_notes_for_grader:
  trigger_2_tracked_actor_attribution: FAIL — Velvet Ant NOT on _roster.yaml (operator-
    deferred /new-actor candidacy only).
  trigger_4_tracked_actor_ttp_change: FAIL — same as Trigger 2; tracked-actor gate not met.
  trigger_5_ad_sector_campaign: MARGINAL FAIL — victim sector/country undisclosed; cannot
    establish multi_victim_confirmed or aerospace_defense_watchlist_entity match without
    Sygnia primary post-level retrieval.
```
