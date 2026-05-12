---
brief_id: flash-2026-05-12-0600
brief_type: flash
published_at: 2026-05-12T06:18:00-04:00
authored_by: archimedes-briefer
grader_approval: archimedes-grader
analyst_review: archimedes-analyst (sat-ach + sat-kac complete, no WEP adjustment)
red_team_review: archimedes-red-team (qualify; no publication block; framing-fixes applied)
human_override: null
findings_referenced:
  - finding-2026-05-12-FLASH-0001
related_actors_referenced:
  - actor_id: "001"
    actor_name: TeamPCP
    treatment: attributed_by_wiz_and_stepsecurity_with_snyk_relaying_stepsecurity_no_archimedes_origination
related_vulns_referenced:
  - cve: CVE-2026-45321
    cvss: 9.6
    ghsa: GHSA-g7cv-rxg3-hmpx
related_findings_referenced:
  - finding-id: finding-2026-05-04-0003
    relationship: same_shai_hulud_family_lineage_per_mstic_family_attribution
    note: "MSTIC family-attribution only; finding-0003 did NOT name TeamPCP as actor."
digraph: A2
digraph_layered:
  procedural_facts: A1
  teampcp_attribution: A2
  novelty_slsa_breaking_claim: A2
wep: likely
wep_split:
  procedural_facts: very_likely
  worm_propagation_dual_ecosystem: very_likely
  teampcp_attribution: likely
  novelty_first_documented_slsa_breaking: likely
quiet_hours_at_compose: true
critical_override_applied: false
critical_override_evaluation:
  cvss_10_0: false
  cvss_value: 9.6
  active_exploitation: true
  tracked_actor_involved: true
  ad_watchlist_targeted: false
  conditions_met: 2_of_4
  result: override_does_not_apply
triggers_fired:
  - trigger_1_critical_cve_exploited
  - trigger_4_tracked_actor_ttp_change
triggers_failed:
  - trigger_2_new_attribution
  - trigger_3_first_party_ioc_hit
  - trigger_5_explicit_ad_sector_targeting
posting_path: queue_for_catchup
expected_post_window: "09:00 EDT catchup sweep — librarian must check for supersession by 08:00 morning brief before posting"
absorbs_flash: null
anti_noise_distinction_2026_05_11_checkmarx_jenkins: distinct_topic_per_8_dimension_test_at_finding_level
red_team_composition_constraints_applied: true
composition_constraints:
  - constraint_id: 1
    label: novelty_claim_framing
    applied: true
    treatment: "Sourced as 'Wiz and Snyk characterize this as the first publicly documented npm worm to produce validly-attested malicious packages within the Shai-Hulud family lineage' — scoped to family lineage, attributed to source. No standalone Archimedes assertion."
  - constraint_id: 2
    label: attribution_independence_narrative
    applied: true
    treatment: "Surfaces Wiz + StepSecurity as originating attribution chain; flags Snyk as relay of StepSecurity, not independent third. Reader sees the two-source-effective posture in body prose."
  - constraint_id: 3
    label: capability_progression_caveat
    applied: true
    treatment: "Analyst A1 qualifier carried: capability progression is consistent with either organic TeamPCP development or composite handoff from an emerging worm-tooling capability."
  - constraint_id: 4
    label: cross_reference_framing
    applied: true
    treatment: "Lineage to finding-2026-05-04-0003 described as 'same Shai-Hulud family lineage' NOT 'same actor lineage per MSTIC attribution baseline.' MSTIC has not named an actor for the Shai-Hulud family in public reporting visible to Archimedes."
  - constraint_id: 5
    label: squawk_aviation_incidental_framing
    applied: true
    treatment: "@squawk hit framed as incidental via worm dependency-graph enumeration, not intentional A&D-adjacent targeting."
hard_rule_2_framings_load_bearing:
  - "TeamPCP attribution: per Wiz + StepSecurity (Snyk relays StepSecurity, not independent third)"
  - "Novelty: per Wiz and Snyk; scoped to Shai-Hulud family lineage; Archimedes does not originate"
  - "Capability progression: organic OR composite-handoff readings both consistent with cited sources"
splunk_first_party:
  status: clean_at_compose
  query_window: -30d
  indexes_queried: [archimedes, defenseclaw_local]
  hits: 0
  hard_rule_8_framing: silence_is_not_disconfirming_iocs_new_master_index_sync_pending
word_count: 299
tlp: CLEAR
test: false
---

# FLASH: TeamPCP-attributed npm/PyPI worm ships validly-attested malicious packages — SLSA trust floor broken

*2026-05-12 06:18 EDT · A2 (procedural facts A1) · TLP:CLEAR*

**What.** [Wiz](https://www.wiz.io/blog/mini-shai-hulud-strikes-again-tanstack-more-npm-packages-compromised) and StepSecurity attribute a 48-hour npm + PyPI compromise — "Mini Shai-Hulud" — to [TeamPCP (#001, HIGH)](../threat-actors/_roster.yaml); [Snyk](https://snyk.io/blog/tanstack-npm-packages-compromised/) relays StepSecurity, not an independent third. 169–172 packages / 403 malicious versions across @tanstack, @uipath, @mistralai, @opensearch-project, @squawk, @tallyui, DraftLab plus PyPI guardrails-ai and mistralai. [CVE-2026-45321](../vulnerabilities/_index.yaml) CVSS 9.6 / GHSA-g7cv-rxg3-hmpx. Wiz and Snyk characterize this as the first publicly documented npm worm producing validly-attested malicious packages within the Shai-Hulud family lineage: it hijacks legitimate maintainer OIDC tokens mid-workflow to publish SLSA-signed payloads. Maintainer reversion landed same-day.

**Impact.** A&D defenders lose SLSA attestations as a self-evident supply-chain trust floor. Any A&D prime ingesting npm or PyPI through CI/CD carries structural exposure even with attestation-enforcement policy in place. CVE-2026-45321 is very likely to land on CISA KEV given CVSS 9.6 + active mass-exploitation. The 19 @squawk aviation-developer packages hit are incidental via worm maintainer-enumeration, not strategic A&D targeting. TeamPCP capability progression is consistent with either organic development OR composite handoff; both readings sit within cited attribution.

**Action.** Pin npm + PyPI dependencies to known-good versions; SBOM-scan against the package list in [finding-2026-05-12-FLASH-0001](../findings/finding-2026-05-12-FLASH-0001.md). Hunt the published IOCs (6 C2 domains, IP `83.142.209.194`, 3 SHA-256s, Session recipient ID, PBKDF2 salt — full set in the finding) across CI/CD egress and developer-workstation telemetry, 14-day window. Treat SLSA provenance as necessary-but-not-sufficient: pair attestation policy with SBOM-scan + version-pin + IOC watch. [MSTIC Shai-Hulud 2.0 guidance](https://www.microsoft.com/en-us/security/blog/2025/12/09/shai-hulud-2-0-guidance-for-detecting-investigating-and-defending-against-the-supply-chain-attack/) is the family-tier baseline.

**Sources.** [Wiz Research](https://www.wiz.io/blog/mini-shai-hulud-strikes-again-tanstack-more-npm-packages-compromised) · [Snyk](https://snyk.io/blog/tanstack-npm-packages-compromised/) · [Hacker News relay](https://thehackernews.com/2026/05/mini-shai-hulud-worm-compromises.html).

**Related.** [TeamPCP #001 HIGH](../threat-actors/_roster.yaml) — Snyk adds aliases DeadCatx3, PCPcat, ShellForce, CipherForce (operator decision pending). [CVE-2026-45321](../vulnerabilities/_index.yaml). Lineage: [finding-2026-05-04-0003](../findings/finding-2026-05-04-0003.md) — same Shai-Hulud family lineage per MSTIC family attribution. MSTIC has not named an actor for the family in public reporting visible to Archimedes. Distinct from the 2026-05-11 Checkmarx Jenkins AST plugin compromise.
