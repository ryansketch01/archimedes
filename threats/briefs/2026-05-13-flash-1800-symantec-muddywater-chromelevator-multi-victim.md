---
brief_id: flash-2026-05-13-1800
brief_type: flash
published_at: 2026-05-13T18:10:00-04:00
authored_by: archimedes-briefer
grader_approval: archimedes-grader
analyst_review: not_yet_required (WEP ceiling "likely" — analyst handoff queued but not blocking FLASH publication)
red_team_review: not_required (WEP ceiling "likely" — below "very likely" threshold per FLASH-POLICY Anti-Noise Rule 3)
human_override: null
findings_referenced:
  - finding-2026-05-13-FLASH-1800-0001
related_actors_referenced:
  - actor_id: "022"
    actor_name: MuddyWater
    aliases_cited_in_source: [Seedworm, "Static Kitten"]
    treatment: attributed_by_symantec_widely_believed_to_be_linked_to_iran_mois_archimedes_does_not_originate
    dossier_status: roster_entry_exists_profile_on_disk_actor_profiler_handoff_queued
related_vulns_referenced: []
digraph: A2
digraph_layered:
  symantec_attribution: A2
  symantec_ttp_delta: A2
  symantec_campaign_scope: A2
  intrusion_timeline_facts: A1
  c2_infrastructure_vt_facts: B1
wep: likely
wep_layered:
  procedural_intrusion_timeline_facts: very_likely
  c2_infrastructure_vt_facts: very_likely
  symantec_originated_campaign_disclosure: very_likely
  attribution_muddywater_seedworm_iran_mois: likely
  ttp_delta_chromelevator_dll_sideloading_nodejs: likely
  operational_claim_campaign_scope_geographic_expansion: likely
wep_rationale: "Single-source veto applied — Symantec originates attribution + TTP-delta + campaign-scope; BleepingComputer (Toulas, 17:59 EDT in-window), Industrial Cyber, and The Hacker News are pure relays and fail the independence test. Symantec's own attribution hedge is preserved verbatim ('widely believed to be linked' — softer than formal moderate/high confidence). WEP capped at 'likely' on attribution + TTP-delta + campaign-scope until a second independent IR-grade source publishes matching IOCs + cluster cross-walk with own telemetry."
critical_override_applied: false
critical_override_evaluation:
  cvss_10_0: false
  cvss_named_in_disclosure: none
  active_exploitation: partial_retrospective_q1_2026_per_symantec
  tracked_actor_involved: true
  ad_watchlist_targeted: false
  conditions_met: 1_of_4
  result: override_does_not_apply
  industrial_cyber_relay_introduced_ad_supplier_claim: NOT_propagated_per_hard_rule_2
quiet_hours_at_compose: false
quiet_hours_window: "09:00-21:00 EDT (inactive at 18:10 EDT compose)"
triggers_fired:
  - trigger_2_tracked_actor_attribution
  - trigger_4_tracked_actor_ttp_change
triggers_failed:
  - trigger_1_critical_cve_exploited     # no CVE named in primary or relays
  - trigger_3_first_party_ioc_hit        # Splunk 30d clean across both indexes
  - trigger_5_ad_sector_campaign         # Symantec primary names NO A&D victim; Industrial Cyber relay claim NOT propagated
  - trigger_6_zero_day_no_patch          # no vulnerability named
posting_path: immediate_post_quiet_hours_inactive
hard_rule_2_framings_load_bearing:
  - "Symantec attribution language preserved verbatim: 'widely believed to be linked' to Iran MOIS — softer than formal moderate/high confidence. Do not collapse to 'Symantec confirms' or 'Archimedes assesses Iran MOIS'."
  - "MuddyWater / Seedworm / Static Kitten alias relationships are pre-existing in _roster.yaml id 022 — not originated by Archimedes here."
  - "Industrial Cyber relay-introduced 'U.S. defense and aerospace software supplier' victim claim is NOT in the Symantec primary and is NOT propagated into this FLASH. Treated as cross-campaign conflation with separate March 2026 Symantec Dindoor/Fakeset campaign."
  - "Coincident SentinelOne brand-impersonation pattern with Salt Typhoon FamousSparrow (flash-2026-05-13-1430) is a cross-cluster observation, NOT an attribution link."
  - "BleepingComputer (Toulas, in-window 17:59 EDT), Industrial Cyber, and The Hacker News explicitly cite Symantec as origin and add no separate evidence basis — single-effective-source."
splunk_first_party:
  status: clean_at_compose
  query_window: -30d
  indexes_queried: [archimedes, defenseclaw_local]
  hits: 0
  ioc_set_queried: "actor aliases (MuddyWater / Seedworm / Static Kitten / Mango Sandstorm / Mercury / Earth Vetala / TEMP.Zagros) + ChromElevator + fmapp / sentinelmemoryscanner / sentinelagentcore filename tokens + timetrakr.cloud + sendit.sh + 179.43.177.220 + 178.128.233.36"
  consecutive_dormant_sweep_count: 22
  hard_rule_8_framing: silence_is_not_disconfirming
provisional_source_grade_block:
  - source_yaml_id: symantec
    proposed_grade: A
    rationale: "Tier-1 vendor research practice — Symantec Threat Hunter Team + Carbon Black joint byline, Broadcom-owned, first-party EDR telemetry (SEP + Carbon Black), long-running Seedworm taxonomy primacy since 2018 (MITRE G0069 attribution cite). Consistent with SentinelOne / Wiz / Snyk / Bitdefender / Sophos / ESET / Dragos provisional-then-ratified precedent. Second provisional-A first-citation on 2026-05-13 (Bitdefender at 14:30 was the first). Pending operator ratification."
relay_layer_conflation_handled: true
relay_layer_conflation_summary: "Industrial Cyber introduced a 'U.S. defense and aerospace software supplier with Israeli operations' victim claim NOT in the Symantec primary; treated as cross-campaign conflation with separate March 2026 Symantec Dindoor/Fakeset US-critical-infrastructure campaign (different malware family, different victim set). NOT propagated into this FLASH per Hard Rule 2. Recorded in finding frontmatter relay_layer_conflation block for audit. Re-evaluates only if Symantec primary updates to name an A&D-supplier victim, or if an independent A/B-grade source corroborates the claim with explicit A&D-prime naming within the 24-72h post-disclosure window (deadline 2026-05-16 18:00 EDT)."
actor_profiler_handoff_queued: true
actor_profiler_handoff_reason: "MuddyWater (#022) profile.md exists; last_reviewed 2026-05-09; next_review_due 2026-08-07. This disclosure adds ChromElevator malware family + two novel DLL sideloading pairs + Node.js orchestration + target-set geographic expansion + sendit.sh exfil pattern ahead of the next-review-due date. Ingestion handoff queued for iocs.yaml + profile.md TTP block + victimology + potential Intent score re-evaluation (currently Intent=3 Sector Association)."
recalibration_watch:
  watch_for: "Within 24-72h post-disclosure: cross-corroboration of attribution + campaign scope by Mandiant / Google Threat Intel / CrowdStrike / MSTIC / Unit 42 / ESET / Sophos / Cisco Talos / Recorded Future / SentinelLabs / Group-IB follow-up. Matching IOCs + campaign cross-walk with own telemetry lifts finding to A1 and WEP to 'very likely' pending red-team review."
  deadline: 2026-05-16T18:00:00-04:00
cross_cluster_observation:
  observation: "Coincident SentinelOne brand-impersonation pattern with Salt Typhoon FamousSparrow campaign (finding-2026-05-13-FLASH-0001, posted 14:30 EDT same day)"
  muddywater_mechanism: "DLL sideloading via legitimate SentinelOne component sentinelmemoryscanner.exe loading malicious sentinelagentcore.dll"
  salt_typhoon_mechanism: "C2 domain brand-impersonation via sentinelonepro[.]com"
  treatment: "Cross-cluster observation, NOT attribution link. Different actors (Iran MOIS vs China MSS), different mechanism, different campaigns. Recording for grader / actor-profiler / detection awareness."
word_count: 292
tlp: CLEAR
test: false
---

# FLASH: Symantec attributes Q1 2026 multi-victim espionage campaign to MuddyWater (Seedworm) with new ChromElevator malware and SentinelOne-component DLL sideloading

*2026-05-13 18:10 EDT · A2 · WEP: likely · TLP:CLEAR*

**What.** [Symantec](https://www.security.com/threat-intelligence/iran-seedworm-electronics) attributes a Q1 2026 nine-victim espionage campaign to **MuddyWater** ([id 022](../threat-actors/MuddyWater/profile.md); aliases Seedworm, Static Kitten) — "widely believed to be linked" to Iran MOIS (Symantec's hedge, preserved). Case study: a South Korean electronics maker, breached Feb 20 and detected Feb 27 after a ~36-hour mid-intrusion silence and ~90-second beacons. Eight further victims span Middle East government and aviation, Southeast Asia industrial manufacturing, Latin America financial services, and global education. Three tradecraft deltas: new credential-theft family **ChromElevator**; two novel DLL sideloading pairs — Fortemedia `fmapp.exe → fmapp.dll` and SentinelOne `sentinelmemoryscanner.exe → sentinelagentcore.dll` (defensive-EDR brand impersonation); Node.js orchestrating PowerShell. Exfil via `sendit[.]sh`.

**Impact.** Symantec names **no A&D victim**. Industrial Cyber's relay-introduced "U.S. defense and aerospace software supplier" claim is absent from the primary and **not propagated** — treated as conflation with the separate March 2026 Dindoor/Fakeset campaign. Relevance is structural: MuddyWater's footprint now extends beyond the MENA government/telecom anchor into supplier-tier electronics and industrial manufacturing, narrowing the distance to A&D sub-tier suppliers. Both DLL sideloading pairs are portable to any Windows fleet running Fortemedia OEM drivers or SentinelOne EDR. Single-source veto caps WEP at "likely". Splunk clean across both indexes over 30 days (22nd consecutive dormant sweep).

**Action.** Sweep mail, proxy, and DNS for `timetrakr[.]cloud`, `sendit[.]sh`, `179.43.177.220` (AS51852 Private Layer CH), `178.128.233.36` (AS14061 DigitalOcean CA). Hunt `fmapp.exe → fmapp.dll` from non-OEM paths and `sentinelmemoryscanner.exe → sentinelagentcore.dll` from non-SentinelOne paths. Review Node.js parents of PowerShell on non-developer endpoints (ATT&CK T1059.001 + T1059.007). Full IOCs in [finding-2026-05-13-FLASH-1800-0001](../findings/finding-2026-05-13-FLASH-1800-0001.md).

**Sources.** [Symantec](https://www.security.com/threat-intelligence/iran-seedworm-electronics) (A, provisional) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/iranian-hackers-targeted-major-south-korean-electronics-maker/) (B, relay) · Industrial Cyber (B, relay — A&D-supplier addition NOT propagated) · The Hacker News (B, relay).

**Related.** Actor-profiler handoff queued for ChromElevator + DLL pairs + Node.js + geographic-expansion ingestion. Cross-cluster note: today's [14:30 FamousSparrow FLASH](../briefs/2026-05-13-flash-1430-famoussparrow-salt-typhoon-azerbaijan-energy.md) used `sentinelonepro[.]com` C2 — two APT clusters impersonating SentinelOne in the same ~12-hour window. **Coincidental, not attribution-linked.** Recalibration watch through 2026-05-16 18:00 EDT.
