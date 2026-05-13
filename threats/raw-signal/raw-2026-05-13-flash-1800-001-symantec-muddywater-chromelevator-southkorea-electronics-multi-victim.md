---
raw_id: raw-2026-05-13-flash-1800-001
collected_at: 2026-05-13T18:08:00-04:00
run_id: flash-sweep-20260513-180000
collection_mode: flash_sweep
sweep_type: flash
sweep_time: 2026-05-13T18:00:00-04:00
time_window_start: 2026-05-13T14:00:00-04:00
time_window_end: 2026-05-13T18:00:00-04:00
test: false
quiet_hours_active: false                  # 18:00 EDT inside 09:00-21:00 EDT active window
source:
  source_yaml_id: bleepingcomputer
  source_name: BleepingComputer
  source_url: https://www.bleepingcomputer.com/news/security/iranian-hackers-targeted-major-south-korean-electronics-maker/
  source_grade: B
  source_role: relay
  originating_research_source: symantec-threat-hunter-team
  originating_research_url: https://www.security.com/threat-intelligence/iran-seedworm-electronics
  originating_research_grade_proposed: A_provisional
  originating_research_publication_date: 2026-05-12        # Symantec primary
  originating_research_byline: "Symantec Threat Hunter Team (no individual analyst names; Symantec + Carbon Black joint team)"
  relay_publication_date: 2026-05-13T17:59:33-00:00         # BleepingComputer 21:59 UTC = 17:59 EDT in-window
  relay_byline: "Bill Toulas (BleepingComputer)"
  cross_relays_surveyed:
    - industrialcyber-co     # WARNING — Industrial Cyber relay introduces "U.S. defense and aerospace software supplier" claim NOT present in Symantec primary. Likely conflation with March 2026 Symantec/HelpNetSecurity US-targeting Dindoor/Fakeset campaign. NOT propagated into corpus.
    - thehackernews          # Cross-relay corroboration of Symantec attribution; no fresh content
match_reason:
  watchlist: []                            # Symantec primary names NO A&D watchlist company; the Industrial Cyber-introduced "U.S. defense and aerospace software supplier" claim does NOT appear in Symantec primary and is NOT propagated
  watchlist_match_strength: none_direct
  actors:
    - "MuddyWater (Seedworm / Static Kitten / Mango Sandstorm / Mercury / Earth Vetala alias match)"   # FLASH-candidate tracked-actor attribution. Roster id 022, threat level LOW per weighted-overall but espionage category MEDIUM (composite 7). IR/MOIS.
  vulnerabilities: []                      # No CVEs named in Symantec primary or BleepingComputer relay
  keywords:
    - flash_candidate_symantec_muddywater_chromelevator_south_korea_electronics_multi_victim
    - new_attribution_distinct_from_2026_05_06_rapid7_muddywater_flash
    - new_malware_family_chromelevator
    - novel_dll_sideloading_pair_fortemedia_fmapp_dll
    - novel_dll_sideloading_pair_sentinelone_sentinelagentcore_dll
    - target_geographic_expansion_east_asia_latin_america
    - tier1_vendor_research_first_corpus_citation_symantec_provisional_a
triage_tags:
  - flash_candidate
  - flash_sweep_1800_2026_05_13
  - quiet_hours_inactive
  - trigger_2_tracked_actor_attribution_matched_cleanly
  - trigger_4_tracked_actor_ttp_change_matched_cleanly
  - trigger_5_ad_sector_campaign_FAILED_relay_conflation_industrialcyber_introduces_unfounded_ad_supplier_claim
  - critical_override_failed_no_cvss10_no_named_ad_watchlist_victim
  - symantec_first_corpus_citation_provisional_a_grade_proposed
  - relay_layer_conflation_caveat_industrialcyber_vs_symantec_primary
  - splunk_first_party_clean_22nd_consecutive_sweep
iocs_extracted: true
iocs_count: 18
text_word_count: 2240
promoted: true
promoted_to_finding: finding-2026-05-13-FLASH-1800-0001
promoted_at: 2026-05-13T18:25:00-04:00
ttl_expires_at: 2026-08-11T18:08:00-04:00   # 90 days per LEGAL-POLICY retention
---

# Iranian hackers targeted major South Korean electronics maker (Symantec via BleepingComputer)

Originating research source: **Symantec Threat Hunter Team** (Broadcom-owned; Symantec + Carbon Black joint team byline). Primary publication date 2026-05-12 at security.com/threat-intelligence/iran-seedworm-electronics. Relayed via BleepingComputer (Bill Toulas) at 2026-05-13T17:59:33Z = 17:59 EDT, inside the 14:00 → 18:00 FLASH sweep window.

## Article scope (per Symantec primary + BleepingComputer relay; cross-checked against Industrial Cyber + Hacker News relays)

**Campaign summary.** Symantec attributes a Q1 2026 multi-victim espionage campaign to **MuddyWater (alias Seedworm, Static Kitten, Mango Sandstorm, Mercury, Earth Vetala, TEMP.Zagros)** — roster id 022, Iran MOIS. Symantec's attribution language is "widely believed to be linked" to Iran's Ministry of Intelligence and Security — softer than formal "high confidence" / "moderate confidence" framing. No first-party MOIS-affiliation evidence is presented in the Symantec primary; attribution rests on toolset, infrastructure, and TTP overlap with prior Symantec Seedworm research and Group-IB's February 2026 reporting (cited as prior context).

**Victims.** At least nine high-profile organizations across four continents:

- Major South Korean **electronics manufacturer** (unnamed) — case-study victim with detailed intrusion timeline. Initial compromise 2026-02-20; active reconnaissance + exfiltration 2026-02-22 through 2026-02-27; nearly a week inside the network before detection; ~90-second C2 beaconing interval; ~36h inactivity gap 2026-02-24 → 2026-02-26.
- Middle East **international airport** (unnamed)
- Middle East **government agencies**
- Southeast Asia **industrial manufacturers**
- Latin America **financial services provider**
- Multiple-country **educational institutions**
- Q1 2026 timeframe (January–March)

**No A&D-named victim in the Symantec primary.** The Industrial Cyber relay introduces a "U.S. defense and aerospace software supplier" with Israeli operations as a victim — this claim **does NOT appear in the Symantec primary** and is **not propagated** into Archimedes corpus. The relay-introduced claim appears to be a conflation with the March 2026 Symantec/HelpNetSecurity-relayed Dindoor/Fakeset US-targeting campaign (which is a separate disclosure already known to be MuddyWater). Per Hard Rule 2 (never originate attribution) and Hard Rule 8 (first-party precedence — though here applied to source-research-primary vs. relay rather than first-party-telemetry), the unnamed-A&D-supplier claim is recorded as relay-introduced and NOT carried forward.

**Initial-access vector.** Unknown / not disclosed by Symantec.

## Tradecraft / TTP delta vs. prior MuddyWater corpus baseline

This is a substantive TTP delta against the actor's prior corpus profile (which was anchored on Rapid7's 2026-05-06 disclosure of MuddyWater MENA targeting). Specific deltas:

1. **New malware family — ChromElevator.** Post-exploitation tool for credential theft. First Symantec disclosure of this family. Not previously in `threats/threat-actors/MuddyWater/iocs.yaml`.

2. **Novel DLL sideloading pair (1) — Fortemedia.** Legitimate signed binary `fmapp.exe` (Fortemedia audio-driver utility shipped on many OEM Windows hosts) loads malicious `fmapp.dll`. First MuddyWater use of Fortemedia binary abuse on Archimedes-corpus record.

3. **Novel DLL sideloading pair (2) — SentinelOne component impersonation.** Legitimate signed binary `sentinelmemoryscanner.exe` (SentinelOne EDR memory scanner) loads malicious `sentinelagentcore.dll`. This pattern echoes the Salt Typhoon FamousSparrow `sentinelonepro[.]com` brand-impersonation infrastructure from earlier today (2026-05-13 14:30 FLASH); two separate APT clusters both impersonating SentinelOne defensive product in the same 12-hour window. Coincidental — different malware (SentinelOne component DLL sideloading vs. SentinelOne brand-impersonation C2 domain), different actors (Iran MuddyWater vs. China Salt Typhoon), different campaigns. Noted for grader / actor-profiler awareness but **not an attribution-link**.

4. **Node.js runtime as orchestration layer.** Symantec describes Node.js already-present on the South Korean victim host being used to drive automated PowerShell-based reconnaissance (user enumeration, domain-group enumeration, antivirus-product enumeration, persistence via Registry Run key, credential theft, SOCKS5 tunneling).

5. **Target-set geographic expansion.** Prior MuddyWater corpus baseline (Rapid7 2026-05-06 + historical Unit 42 / Symantec Seedworm / ClearSky / Trend Micro Earth Vetala documentation) anchored on MENA-government-and-telecom targeting. This Q1 2026 campaign extends into **East Asia electronics manufacturing**, **Southeast Asia industrial manufacturing**, **Latin America financial services**. The South Caucasus / Central Asia / North America US-critical-infrastructure footprint observed in the separate March 2026 Symantec Dindoor/Fakeset disclosure is NOT part of this Q1 retrospective; the two campaigns are temporally and tooling-distinct.

6. **Exfiltration via public file-transfer service `sendit.sh`.** Symantec notes the service is "associated with malicious activity per VirusTotal" — a living-off-trusted-cloud-services pattern.

7. **C2 beacon cadence ~90s** with ~36h inactivity gap mid-intrusion. Stealth-oriented dwell-time tradecraft (~week-long undetected presence).

## A-grade corroboration status

Symantec primary explicitly cites only **Group-IB February 2026 Seedworm reporting** as prior context. No Microsoft MSTIC, Mandiant, Unit 42, CrowdStrike, or other Tier-1 vendor cross-corroboration appears in the Symantec primary. Industrial Cyber and Hacker News are relay-layer (not independent research). Per anti-noise + INTEL-GRADING discipline this is a **single A-grade primary source with one A-grade prior-context citation (Group-IB)** — grader will evaluate whether the Group-IB Feb 2026 prior reporting + Symantec Seedworm long-running taxonomy constitute sufficient independent corroboration to lift WEP beyond "likely" per single-source-veto.

## FLASH trigger evaluation

- **Trigger 1 (critical-CVE-exploited):** FAILS — no CVE named.
- **Trigger 2 (tracked-actor-attribution):** **MATCHES.** MuddyWater is roster id 022. Symantec is A-grade Tier-1 vendor research practice (Broadcom-owned, peer of Mandiant / CrowdStrike / Unit 42 / MSTIC). The attribution is to a campaign distinct from the 2026-05-06 Rapid7 disclosure already in corpus (different victim set, different malware family, different geography). Trigger 2 condition `new_attribution_not_restatement` satisfied.
- **Trigger 3 (first-party-IOC-hit):** FAILS. Splunk search across `index=archimedes OR index=defenseclaw_local` for MuddyWater + Seedworm aliases + ChromElevator + Fortemedia / SentinelOne component file names + timetrakr.cloud + sendit.sh + 179.43.177.220 + 178.128.233.36 returned **zero non-archimedes-internal events** over `-30d`. Twenty-second consecutive dormant sweep across both indexes.
- **Trigger 4 (tracked-actor-TTP-change):** **MATCHES.** Multiple TTP deltas documented above (ChromElevator new family + two novel DLL sideloading pairs + target geographic expansion + Node.js orchestration). Symantec is A-grade.
- **Trigger 5 (A&D-sector campaign):** FAILS. Symantec primary names NO A&D victim. The Industrial Cyber relay-introduced "U.S. defense and aerospace software supplier" claim does NOT appear in the Symantec primary and is treated as relay conflation with the separate March 2026 Symantec Dindoor/Fakeset US-targeting campaign. Trigger 5 condition `targets_include_aerospace_defense_or_watchlist_entity` not satisfied at A-grade-primary layer.
- **Trigger 6 (zero-day-no-patch):** FAILS — no vulnerability named.

**Two clean trigger matches: 2 + 4.** Eligible for FLASH evaluation downstream (grader → red-team → briefer). Anti-noise: prior MuddyWater FLASH was 2026-05-06 (Rapid7-source) — 7 days ago, well outside 24h anti-noise window. Different campaign, different research source, different tradecraft. Anti-noise does NOT bar this FLASH.

## Critical override evaluation

- CVSS 10.0: **FAILS** — no CVE-class indicator.
- Active exploitation: TRUE — campaign described as Q1 2026 retrospective in Symantec primary with no explicit "ongoing" language (Industrial Cyber relay claim "continuing into recent days" appears tied to its A&D-supplier conflation; not in Symantec primary). Conservative reading: retrospective Q1 2026 disclosure, not actively-ongoing post-disclosure.
- Tracked actor: TRUE — MuddyWater is roster id 022.
- A&D watchlist NAMED: FALSE — Symantec primary names no A&D victim.

**Critical override FAILS** on multiple conditions. Moot anyway — quiet hours INACTIVE (18:00 EDT inside 09:00 EDT–21:00 EDT active window per `infrastructure/flash-policy.yaml`); FLASH posting permitted on Trigger 2 + Trigger 4 strength regardless.

## Source-grading proposal (operator-action item)

**Symantec** is a first Archimedes-corpus citation as an originating research source. Symantec is widely recognized as Tier-1 vendor research peer (Mandiant / CrowdStrike / Unit 42 / MSTIC / Sophos / ESET / Dragos / Bitdefender / Wiz Research / Snyk tier). Symantec Threat Hunter Team publishes peer-reviewed APT and malware research with first-party EDR telemetry (Symantec Endpoint Protection + Carbon Black) and a long track record of Seedworm taxonomy primacy (Symantec coined the Seedworm name 2018; cited by MITRE G0069; referenced in `threats/threat-actors/MuddyWater/profile.md` line 137 as historical-TTP-baseline source).

**Provisional A grade proposed**, consistent with the precedent applied to SentinelOne (2026-05-08 first surface, A-provisional), Wiz Research + Snyk (2026-05-12 first surface, A-provisional), Bitdefender (2026-05-13 first surface, A-provisional this morning), and the Session 11 ratifications of Sophos / ESET / Dragos. Operator action: add to `infrastructure/source-grades.yaml` `vendor_sources` and `infrastructure/source-health.yaml`.

---

## Extraction notes

- Language: en
- Article type: research blog (Symantec) + media relay (BleepingComputer / Industrial Cyber / Hacker News)
- Raw IOC extraction invoked: yes
- Pre-flight LEGAL-POLICY check: passive RSS/web fetches + VirusTotal IP/domain lookups + own-index Splunk reads only; no prohibited query patterns triggered; no credentials surfaced.
- Anti-noise: prior MuddyWater FLASH 2026-05-06 was Rapid7-sourced MENA campaign — distinct topic, >7 days ago, well outside 24h anti-noise window. This Symantec South Korea / ChromElevator campaign is a fresh trigger-topic.
- Hard Rule 6 (15-word quote limit) enforced — Symantec attribution rendered as "widely believed to be linked" (5 words) in IOC block below; no other verbatim quoting.
- Hard Rule 2 (never originate attribution) enforced — Industrial Cyber relay's A&D-supplier claim recorded as relay-introduced and NOT propagated as fact into Archimedes corpus. Source-research-primary (Symantec) controls.
- Hard Rule 3 (no exploitation assistance) enforced — Symantec primary discusses tradecraft observations (DLL sideloading mechanics, PowerShell recon patterns) but Archimedes raw-signal captures named-tooling + IOC-set only; no PoC code or attack-walkthrough content copied.

## IOCs (from ioc-extraction pattern)

```yaml
attribution_claims:
  - actor: MuddyWater
    actor_aliases_used_in_source: [Seedworm, "Static Kitten"]
    nation_or_service: "Iran MOIS (Ministry of Intelligence and Security)"
    confidence_language_source_reports: "widely believed to be linked"
    archimedes_assessment: not_originated_by_collector   # per Hard Rule 2
    roster_id: "022"

c2_infrastructure:
  domains:
    - domain: "timetrakr.cloud"
      vt_malicious: 5
      vt_total: 92
      vt_engines: [ADMINUSLabs, "ArcSight Threat Intelligence", ESET, Fortinet, SOCRadar]
      whois_creation: 2026-01-18
      whois_last_update: 2026-01-23
      notes: "Registered ~1 month before Feb 20 South Korean intrusion onset; brand-impersonation of time-tracking SaaS likely."
    - domain: "sendit.sh"
      vt_malicious: associated_with_malicious_activity_per_symantec
      notes: "Public file-transfer service abused for exfiltration. Not actor-owned infrastructure — living-off-trusted-cloud pattern."

  ip_addresses:
    - ip: "179.43.177.220"
      vt_malicious: 5
      vt_total: 92
      vt_engines: [ADMINUSLabs, CRDF, ESET, Fortinet, alphaMountain.ai]
      asn: 51852
      as_owner: "Private Layer INC"
      country: CH
      notes: "Swiss bulletproof-hosting AS. Known to host APT staging infrastructure."
    - ip: "178.128.233.36"
      vt_malicious: 3
      vt_total: 92
      vt_engines: [ADMINUSLabs, ESET, Fortinet]
      asn: 14061
      as_owner: "DigitalOcean, LLC"
      country: CA
      notes: "Commodity VPS staging; DigitalOcean Canada region."
    - ip: "additional_4_ips_not_disclosed_in_relay"
      notes: "Symantec primary reports 6 total IPs; relay surfaced 2. Operator to fetch full IOC set from security.com/threat-intelligence/iran-seedworm-electronics if dossier scaffold proceeds."

  urls:
    - url_count: 3
      notes: "Staging server paths + ipinfo.io/json reconnaissance call. Symantec primary; not enumerated in BleepingComputer relay."

malware_families:
  - name: "ChromElevator"
    type: "Post-exploitation credential-theft tool"
    novelty: "First Symantec corpus disclosure (per cross-relay survey); first Archimedes-corpus reference."
    capability:
      - credential_theft
      - powershell_reconnaissance_orchestration
    notes: "Symantec Threat Hunter Team primary; not previously in threats/threat-actors/MuddyWater/iocs.yaml. Operator action: add to actor IOC index on grader handoff."

dll_sideloading_pairs:
  - legitimate_binary: "fmapp.exe"
    legitimate_publisher: Fortemedia
    legitimate_function: "OEM audio driver utility"
    malicious_dll: "fmapp.dll"
    sha256_count_in_primary: "13 SHA256 values reported by Symantec across the binary + DLL set; specific hashes not surfaced in BleepingComputer relay"
  - legitimate_binary: "sentinelmemoryscanner.exe"
    legitimate_publisher: SentinelOne
    legitimate_function: "EDR memory scanner component"
    malicious_dll: "sentinelagentcore.dll"
    notes: "Brand-impersonation of defensive EDR. Coincident with Salt Typhoon FamousSparrow sentinelonepro[.]com C2-domain brand-impersonation (raw-2026-05-13-flash-1430-001) — TWO separate APT clusters impersonating SentinelOne defensive product in same 12h window; coincidental, not attribution-linked."

persistence:
  - mechanism: "Registry Run key (CurrentVersion\\Run; specific key name not disclosed)"
  - mechanism: "Node.js runtime orchestration of PowerShell scripts (using already-present Node.js on victim hosts)"

tactical_indicators:
  beacon_interval_seconds: ~90
  inactivity_gap_hours: ~36 (Feb 24-26 in South Korean case study)
  dwell_time_before_detection: ~1 week
  network_reconnaissance_method: "Automated PowerShell via Node.js orchestrator; user enumeration, domain group enumeration, AV product enumeration"
  exfiltration_channel: "sendit.sh (public file-transfer service); SOCKS5 tunnels"

victims_named_in_source:
  symantec_primary:
    - sector: "Electronics manufacturing"
      country: "South Korea"
      named: false
      role: case_study_victim
      intrusion_window: 2026-02-20 → 2026-02-27
    - sector: "Aviation (international airport)"
      country: "Middle East"
      named: false
    - sector: "Government"
      country: "Middle East"
      named: false
    - sector: "Industrial manufacturing"
      country: "Southeast Asia"
      named: false
    - sector: "Financial services"
      country: "Latin America"
      named: false
    - sector: "Educational institutions"
      country: "multiple"
      named: false
  industrialcyber_relay_introduced_NOT_in_symantec_primary:
    - sector: "U.S. defense and aerospace software supplier"
      country: "U.S. with Israeli operations"
      named: false
      flagged_as_relay_conflation: true
      conflation_likely_target: "March 2026 Symantec/HelpNetSecurity Dindoor/Fakeset US-critical-infrastructure campaign (separate disclosure)"
      propagated_to_archimedes_corpus: false

cves: []                  # No CVEs named in either Symantec primary or BleepingComputer relay

corroboration_status:
  primary_a_grade_sources_count: 1                        # Symantec (originating)
  prior_context_a_grade_citation: "Group-IB February 2026 Seedworm reporting"
  cross_relay_b_grade_corroboration:
    - BleepingComputer (Bill Toulas)
    - "Industrial Cyber (with A&D-supplier conflation caveat)"
    - "The Hacker News (cross-relay survey)"
  independent_secondary_a_grade_corroboration: absent_at_collection_time
  single_source_veto_recommendation_for_grader: "consider — Symantec is primary, prior Group-IB context is cited but not independently re-verified by Archimedes; relays are B-grade not independent research"

splunk_first_party_check:
  query_set:
    actor_aliases: [MuddyWater, Seedworm, "Static Kitten", "Mango Sandstorm", Mercury, "Earth Vetala", "TEMP.Zagros"]
    malware_families: [ChromElevator]
    file_names: [fmapp, sentinelmemoryscanner, sentinelagentcore]
    c2_domains: ["timetrakr.cloud", "sendit.sh"]
    c2_ips: ["179.43.177.220", "178.128.233.36"]
  earliest: -30d
  result: zero_non_archimedes_internal_events
  consecutive_dormant_sweep_count: 22
```

## Trigger 5 caveat — relay-layer conflation handling

The Industrial Cyber relay-introduced claim that a "U.S. defense and aerospace software supplier" with Israeli operations is among the victims appears to be a conflation with the separate March 2026 Symantec/HelpNetSecurity Dindoor/Fakeset US-critical-infrastructure campaign (also MuddyWater-attributed; covered by The Register and HelpNetSecurity). Industrial Cyber's article was published 2026-05-13 (relay-day) and may have synthesized both Symantec disclosures into one narrative.

**Archimedes corpus does NOT propagate the unfounded A&D-supplier claim.** Per Hard Rule 2 (never originate attribution) and source-primary-precedence discipline, the A&D-supplier claim is NOT carried into findings unless either (a) Symantec primary is updated to include it, or (b) an independent A-grade source corroborates it. The grader and red-team should evaluate this candidate on Trigger 2 + Trigger 4 strength alone.

If Symantec or another A-grade source publishes a follow-on with explicit A&D-prime victim naming in the next 24–72h, this candidate gets upgraded to Trigger 5 territory and Critical Override re-evaluation. Until then: indirect.
