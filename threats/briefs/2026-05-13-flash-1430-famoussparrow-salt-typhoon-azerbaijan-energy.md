---
brief_id: flash-2026-05-13-1430
brief_type: flash
published_at: 2026-05-13T14:30:00-04:00
authored_by: archimedes-briefer
grader_approval: archimedes-grader
analyst_review: not_yet_required (WEP ceiling "likely" — analyst handoff queued but not blocking FLASH publication)
red_team_review: not_required (WEP "likely" — below "very likely" threshold per FLASH-POLICY Anti-Noise Rule 3)
human_override: null
findings_referenced:
  - finding-2026-05-13-FLASH-0001
related_actors_referenced:
  - actor_id: "010"
    actor_name: Salt Typhoon
    alias_cited_in_source: FamousSparrow
    treatment: attributed_by_bitdefender_moderate_to_high_confidence_archimedes_does_not_originate
    dossier_status: roster_entry_exists_no_dossier_files_on_disk_scaffold_pending
related_vulns_referenced:
  - cve: CVE-2021-34473
    cvss: 9.8
    role: proxyshell_initial_access
    patch_status: patched_2021
  - cve: CVE-2021-34523
    cvss: 9.8
    role: proxyshell_initial_access
    patch_status: patched_2021
  - cve: CVE-2021-31207
    cvss: 7.2
    role: proxyshell_initial_access
    patch_status: patched_2021
  - cve: CVE-2022-41040
    cvss: 8.8
    role: proxynotshell_initial_access
    patch_status: patched_2022
  - cve: CVE-2022-41082
    cvss: 8.8
    role: proxynotshell_initial_access
    patch_status: patched_2022
digraph: A2
digraph_layered:
  bitdefender_attribution: A2
  bitdefender_ttp_delta: A2
  cve_chain_facts: A1
  c2_domain_vt_facts: B1
wep: likely
wep_rationale: "Single-source veto applied. Bitdefender originates attribution + TTP-delta; Hacker News and Dark Reading are pure relays and fail the independence test. WEP capped at 'likely' until a second independent IR-grade source (Mandiant / CrowdStrike / Unit 42 / MSTIC / ESET / Talos) publishes matching IOCs + cluster cross-walk with own telemetry."
critical_override_applied: false
critical_override_evaluation:
  cvss_10_0: false
  cvss_max_in_chain: 9.8
  active_exploitation: true
  tracked_actor_involved: true
  ad_watchlist_targeted: false   # Azerbaijani oil & gas is energy sector, not A&D
  conditions_met: 2_of_4
  result: override_does_not_apply
quiet_hours_at_compose: false
quiet_hours_window: "09:00-21:00 EDT (inactive at 14:30 EDT compose)"
triggers_fired:
  - trigger_2_tracked_actor_attribution
  - trigger_4_tracked_actor_ttp_change
triggers_failed:
  - trigger_1_critical_cve_exploited     # CVE chain is 2021/2022 n-day, not fresh
  - trigger_3_first_party_ioc_hit        # Splunk 30d clean
  - trigger_5_ad_sector_campaign         # energy, not A&D; single-victim disclosure
  - trigger_6_zero_day_no_patch          # CVEs long-patched
posting_path: immediate_post_quiet_hours_inactive
hard_rule_2_framings_load_bearing:
  - "Bitdefender attributes campaign to FamousSparrow at moderate-to-high confidence — Archimedes does not originate the campaign attribution"
  - "FamousSparrow → Salt Typhoon alias link is pre-existing in _roster.yaml line 160, not originated by Archimedes here"
  - "Hacker News and Dark Reading cite Bitdefender as origin and add no independent evidence basis — attribution is single-effective-source"
splunk_first_party:
  status: clean_at_compose
  query_window: -30d
  indexes_queried: [archimedes, defenseclaw_local]
  hits: 0
  ioc_set_queried: "actor aliases + malware families (Deed RAT / Snappybee / TernDoor / Mofu Loader) + C2 domains + ProxyShell/ProxyNotShell CVE chain"
  hard_rule_8_framing: silence_is_not_disconfirming
provisional_source_grade_block:
  - source_yaml_id: bitdefender
    proposed_grade: A
    rationale: "Tier-1 vendor research practice — named-analyst bylines (Vrabie + Zugec), first-party EDR telemetry, IntelliZone IOC distribution, prior FamousSparrow attribution track record with ESET + Microsoft. Consistent with SentinelOne / Wiz / Snyk / Sophos / ESET / Dragos provisional-then-ratified precedent. Pending operator ratification."
actor_profiler_handoff_queued: true
actor_profiler_handoff_reason: "First Archimedes-corpus citation of any Salt Typhoon / FamousSparrow / Earth Estries / GhostEmperor / UNC2286 activity. Roster entry exists at id 010 (HIGH, China MSS) but no dossier files on disk. This finding is sufficient first-pass content."
word_count: 280
tlp: CLEAR
test: false
---

# ⚡ FLASH: Bitdefender attributes Azerbaijani oil & gas multi-wave Exchange intrusion to FamousSparrow (Salt Typhoon alias)

*2026-05-13 14:30 EDT · A2 · WEP: likely · TLP:CLEAR*

**What.** [Bitdefender Labs](https://businessinsights.bitdefender.com/famoussparrow-apt-targets-azerbaijani-oil-gas-industry) attributes a three-wave Exchange intrusion against an Azerbaijani oil and gas company (Dec 2025 — Feb 2026) to **FamousSparrow** at moderate-to-high confidence — a listed alias for [Salt Typhoon (#010, HIGH, China MSS)](../threat-actors/_roster.yaml). Initial access via n-day [ProxyShell + ProxyNotShell chain](../vulnerabilities/_index.yaml) (CVE-2021-34473 / -34523 / -31207, CVE-2022-41040 / -41082; all patched 2021/2022). Seven new tradecraft observations documented: Deed RAT variant with magic value `0xFF66ABCD` and Deflate compression, Mofu Loader → TernDoor combination, evolved LogMeIn Hamachi DLL sideloading via exported-function override, three-wave persistence through one entry point, and TernDoor target-set expansion from South American telecom to South Caucasus energy. Two VT-confirmed C2 domains: `sentinelonepro[.]com` (registered same day as Wave 3) and `virusblocker[.]it[.]com`.

**Impact.** The victim is not A&D, but the **TTP delta is portable to any on-prem Exchange surface** — and many A&D suppliers still run on-prem Exchange. The three-wave pattern is a **victim-hygiene story**: same actor returned through the same entry point across two months, consistent with remediation without full eviction. Single-source veto applies — Hacker News and Dark Reading are pure Bitdefender relays — so WEP caps at "likely". Splunk first-party clean across both indexes on the full IOC set over 30d.

**Action.** Verify ProxyShell + ProxyNotShell patch state across every Exchange surface — unpatched in 2026 is a hygiene failure. Hunt mail-surface telemetry for `virusblocker[.]it[.]com`, `sentinelonepro[.]com`, Deed RAT magic `0xFF66ABCD`, and `LMIGuardianSvc.exe` + `LMIGuardianDll.dll` in unexpected locations. Full IOC, hash, and web-shell-filename set in [finding-2026-05-13-FLASH-0001](../findings/finding-2026-05-13-FLASH-0001.md). Treat post-compromise remediation as not-done until credentials are rotated and return paths are closed.

**Sources.** [Bitdefender](https://businessinsights.bitdefender.com/famoussparrow-apt-targets-azerbaijani-oil-gas-industry) (A, provisional) · [Hacker News](https://thehackernews.com/2026/05/azerbaijani-energy-firm-hit-by-repeated.html) (B, relay) · [Dark Reading](https://www.darkreading.com/cyberattacks-data-breaches/china-famoussparrow-apt-south-caucasus-energy-firm) (B, relay).

**Related.** [Salt Typhoon #010 HIGH](../threat-actors/_roster.yaml) — first Archimedes-corpus citation; dossier scaffolding queued. Recalibration watch through 2026-05-16 14:30 EDT: a second IR-grade source (Mandiant / CrowdStrike / Unit 42 / MSTIC / ESET / Talos) publishing matching IOCs with own telemetry lifts the finding to A1 and WEP to "very likely" pending red-team review.
