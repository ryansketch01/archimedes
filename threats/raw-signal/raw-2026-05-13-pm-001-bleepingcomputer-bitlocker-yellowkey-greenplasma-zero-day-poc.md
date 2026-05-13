---
raw_id: raw-2026-05-13-pm-001
collected_at: 2026-05-13T15:35:00-04:00
run_id: pre-brief-20260513-153000
collection_mode: pre_brief_collection
sweep_type: pre_brief
sweep_time: 2026-05-13T15:30:00-04:00
time_window_start: 2026-05-13T07:30:00-04:00
time_window_end: 2026-05-13T15:30:00-04:00
test: false
source:
  source_yaml_id: bleepingcomputer
  source_name: BleepingComputer
  source_url: https://www.bleepingcomputer.com/news/security/windows-bitlocker-zero-day-gives-access-to-protected-drives-poc-released/
  source_byline: Bill Toulas
  published_at: 2026-05-13T16:37:49+00:00     # 12:37 EDT, inside afternoon-pre-brief window
  fetched_via: fetch_feed + WebFetch
  fetched_at: 2026-05-13T15:34:00-04:00
secondary_sources_via_websearch_or_extraction_notes:
  - source_id: chaotic_eclipse_nightmare_eclipse_github
    source_grade: F_unknown_researcher_pseudonym
    source_url_class: github.com/Nightmare-Eclipse/YellowKey + github.com/Nightmare-Eclipse/GreenPlasma
    role: originating_disclosure_via_self_published_poc_github_repos
    note: |
      Pseudonymous researcher self-describing as disgruntled with
      Microsoft's vulnerability handling. NOT in source-grades.yaml.
      First Archimedes-corpus surface. Pseudonym + self-described
      grievance posture = F grade until track record establishes.
      Grader should NOT upgrade based on PoC functionality alone —
      working PoC is fact-layer, attribution-of-credibility-to-claims
      remains separate from technical demonstration.
  - source_id: microsoft_response_via_bleepingcomputer_quote
    source_grade: A_official_vendor
    role: vendor_response_relayed_by_secondary
    fetch_status: not_directly_fetched_msrc_advisory_does_not_yet_exist_per_no_cve_assigned
    quoted_text: "Microsoft is committed to investigating reported security issues and will update impacted devices as soon as possible."
  - source_id: bluehammer_redsun_lineage_precedent
    role: prior_class_member_exploited_in_wild_after_public_disclosure
    note: |
      Article notes BlueHammer (CVE-2026-33825) and RedSun (no
      identifier) "began to be exploited in the wild shortly after
      being publicly disclosed." This is researcher / BleepingComputer
      editorial framing — not first-party telemetry. Pattern-of-class
      data point for grader.
match_reason:
  watchlist: []
  watchlist_match_strength: structural_via_bitlocker_universal_enterprise_deployment_across_all_15_primes_dib_required
  actors: []
  vulnerabilities:
    - bitlocker_yellowkey_no_cve_yet            # NTFS-transaction WinRE shell elevation → BitLocker drive decryption on original device
    - bitlocker_greenplasma_no_cve_yet          # CTFMON arbitrary memory-section creation in SYSTEM-writable directories → LPE-to-SYSTEM
  related_prior_class_cves:
    - cve_2026_33825_bluehammer                # prior leaked-then-itw exploit per BleepingComputer framing
    - redsun_no_identifier                      # same lineage, no CVE assigned
  keywords:
    - bitlocker_bypass_zero_day_poc_published
    - yellowkey_winre_ntfs_transaction_fstx_files
    - greenplasma_ctfmon_arbitrary_section_creation_lpe
    - chaotic_eclipse_nightmare_eclipse_github_disclosure
    - tpm_only_protection_bypass_tpm_pin_still_vulnerable
    - bitlocker_pin_plus_bios_password_only_published_mitigation
    - microsoft_no_patch_yet_committed_to_investigating
    - itw_class_precedent_bluehammer_redsun_post_disclosure
    - dib_full_disk_encryption_mandate_class_target
    - windows_11_server_2022_server_2025_affected
triage_tags:
  - zero_day_disclosed_without_patch_class
  - poc_published_publicly_on_github
  - no_cve_assigned_yet_microsoft_aware
  - bitlocker_full_disk_encryption_bypass_class
  - tpm_only_configurations_affected
  - tpm_pin_configuration_still_exploitable_per_researcher
  - flash_trigger_6_marginal_fail_no_imminent_a_grade_attestation
  - non_flash_grader_queue_item_pm_afternoon_brief_eligible
  - structural_ad_relevance_dib_bitlocker_full_disk_encryption_mandate
  - lineage_class_bluehammer_redsun_itw_after_public_disclosure_pattern
flash_trigger_evaluation:
  trigger_1_critical_cve_exploited:
    matched: false
    rationale: |
      No CVE assigned yet; CVSS not published. Article explicitly states
      "researchers have not confirmed any in-the-wild exploitation of
      YellowKey or GreenPlasma" — only the prior lineage members
      (BlueHammer / RedSun) were ITW. Active-exploitation FALSE on
      YellowKey + GreenPlasma blocks Trigger 1.
  trigger_2_tracked_actor_attribution:
    matched: false
    rationale: |
      No actor attribution. Pseudonymous researcher discovery
      (Chaotic Eclipse / Nightmare-Eclipse). Not in _roster.yaml.
  trigger_3_first_party_ioc_hit:
    matched: false
    rationale: |
      Splunk archimedes + defenseclaw_local indices searched over -24h
      for any non-archimedes-internal events — ZERO. Twentieth
      consecutive dormant sweep. No first-party telemetry IOCs to
      pivot on (BitLocker bypass artifacts would be host-local: FsTx
      files in EFI partition, WinRE NTFS-transaction journal entries,
      registry changes for the boot-time shell — none of which would
      surface in network-telemetry first-party indexes).
  trigger_4_tracked_actor_ttp_change:
    matched: false
    rationale: |
      No tracked actor. The TTPs described (boot-environment NTFS
      transaction manipulation, EFI partition write, CTRL-key shell
      trigger during boot) are physical-access / supply-chain attack
      class — useful TTP context for grader downstream actor scoring
      if/when a tracked actor weaponizes the class.
  trigger_5_ad_sector_campaign:
    matched: false
    rationale: |
      No A&D prime named. No campaign described. Structural relevance
      is universal-deployment-shaped (BitLocker is mandated under CMMC
      Level 2 / NIST 800-171 3.13.16 for protecting controlled
      unclassified information at rest, deployed across all 15 primes
      on aerospace-defense.yaml watchlist), but evidence-minimum for
      Trigger 5 requires multi-victim confirmed + A&D-prime-or-
      watchlist-entity targeted. Both FAIL on this disclosure.
  trigger_6_zero_day_no_patch:
    matched: marginal_fail
    rationale: |
      patch_available=false: CONFIRMED — no patch released; Microsoft
      response is "committed to investigating" with no timeline.
      cvss_score>=8.0: UNDETERMINED — no CVSS published yet (no CVE).
      wide_deployment: TRUE — Windows 11, Windows Server 2022, Windows
      Server 2025 are mass-deployed across enterprise environments
      including the DIB.
      exploitation_confirmed_or_imminent: MARGINAL FAIL. Article cites
      BlueHammer / RedSun lineage precedent of leaked exploits being
      ITW shortly after disclosure, but does NOT make an imminent-
      exploitation claim FOR YellowKey or GreenPlasma. BleepingComputer
      is B-grade, not A-grade. Trigger 6 evidence-minimum specifies
      "(exploitation_confirmed OR exploitation_imminent per A-grade)"
      — BleepingComputer's lineage-pattern observation is B-grade and
      does not meet the imminent threshold.
      NET: FLASH Trigger 6 evaluates FALSE at this sweep on the
      A-grade-attestation clause. Reclassify if MSRC / CISA / Microsoft
      vendor blog publishes A-grade imminent / ITW attestation in
      next 24h.
  net: NON-FLASH. Grader-queue item for 2026-05-13 16:00 afternoon brief.
grader_disposition_recommendation: |
  Promote to a fresh standalone finding for the 2026-05-13 afternoon
  brief, citing BleepingComputer (B grade) as primary with explicit
  A-grade absence caveat (no MSRC advisory, no CISA addition, no CVE
  yet). Single-source veto rules apply: BleepingComputer is the only
  named-byline source on this story this sweep — propose WEP "possible"
  at most, with the A-grade absence + B-source single-effective-origin
  explicitly flagged in finding frontmatter.

  Forward weaponization risk framing: the class (boot-environment +
  BitLocker bypass) has precedent of public-PoC → ITW translation
  within the BlueHammer / RedSun lineage (article's own claim, not
  Archimedes-originated). Frame as "patch is unavailable AND public
  PoC exists AND historical class members went ITW post-disclosure" —
  the operator-actionable signal for DIB Exchange / endpoint owners
  is to prioritize BitLocker hardening (transition TPM-only to TPM+PIN
  if not already; verify BIOS passwords; queue tripwires for Microsoft
  out-of-band patch + KEV addition + CVE assignment over 7-14d).

  Forward watch:
    - MSRC advisory + CVE assignment (Microsoft acknowledgment)
    - CISA KEV addition (would shift to Trigger 1 active-exploitation
      class via CISA's "known to be exploited" attestation)
    - Independent corroboration from a Tier-1 vendor (Mandiant,
      CrowdStrike, MSTIC, Sophos X-Ops, ESET) — first n-day analysis
      or ITW first-party telemetry observation
    - PoC weaponization (working full-chain exploit beyond the
      published partial PoC) — researcher hint that TPM+PIN is "still
      exploitable regardless" suggests fuller PoC may surface
copyright_compliance:
  - quote_count: 2_quotes_from_bleepingcomputer
  - quote_word_count: 13_words_each_under_15_word_cap
  - paraphrase_majority: true
iocs_extracted: false
iocs_count: 0
iocs_note: |
  No IOCs extracted — disclosure is vulnerability-class technical
  detail, no infrastructure / hashes / actor-controlled artifacts.
  PoC GitHub repos (github.com/Nightmare-Eclipse/YellowKey,
  github.com/Nightmare-Eclipse/GreenPlasma) are researcher-published
  research artifacts, NOT IOCs. Recording in keywords for grader
  awareness but not adding to _master-index.yaml as IOCs (which would
  imply attacker infrastructure).
text_word_count_full_capture: 312       # synthesized from BleepingComputer body via WebFetch
promoted: true
promoted_to_finding: finding-2026-05-13-0003
promoted_at: 2026-05-13T16:08:00-04:00
promoted_by_run_id: afternoon-20260513-160000
promoted_disposition: monitoring_tier_b3_single_source_uncorroborated_bleepingcomputer_b_grade_with_originating_researcher_pseudonym_f_grade_single_source_veto_wep_likely_no_action_item
ttl_expires_at: 2026-08-11T15:35:00-04:00     # 90 days per LEGAL-POLICY retention
---

# Windows BitLocker Zero-Day Gives Access to Protected Drives — YellowKey + GreenPlasma PoCs Released (BleepingComputer 2026-05-13 12:37 EDT)

## Source

- **Outlet:** BleepingComputer (B-grade media per source-grades.yaml)
- **URL:** https://www.bleepingcomputer.com/news/security/windows-bitlocker-zero-day-gives-access-to-protected-drives-poc-released/
- **Byline:** Bill Toulas
- **Published:** 2026-05-13T16:37:49Z (12:37 EDT, inside 8h afternoon pre-brief window 2026-05-13T07:30 → 15:30 EDT)
- **Originating researcher:** Chaotic Eclipse / Nightmare-Eclipse (GitHub handle; pseudonym; F-grade attribution per source-grades.yaml convention for unknown researchers)

## Synthesized body (extraction notes — not verbatim BleepingComputer copy)

A pseudonymous researcher operating as "Chaotic Eclipse" (GitHub handle Nightmare-Eclipse) published proof-of-concept exploits for two previously undisclosed Windows vulnerabilities on 2026-05-13:

- **YellowKey** — BitLocker bypass exploiting NTFS transactions in Windows Recovery Environment (WinRE). The technique requires specially crafted `FsTx` files placed on a USB drive or copied to the EFI partition on the target's drive; pressing CTRL during boot triggers a shell within the recovery environment. The bypass succeeds against TPM-only BitLocker configurations on the **original device** (the article notes it does NOT work against stolen drives — the TPM key release still requires the original platform). YellowKey is documented to affect Windows 11, Windows Server 2022, and Windows Server 2025.
- **GreenPlasma** — Local privilege escalation ("Windows CTFMON Arbitrary Section Creation Elevation of Privileges"). Allows unprivileged users to create arbitrary memory-section objects in SYSTEM-writable directories. The leaked PoC is described as incomplete, but the researcher claims full SYSTEM-shell exploitation is achievable.

**Patch status:** No patches released. Microsoft's response to BleepingComputer (relayed in the article body): "Microsoft is committed to investigating reported security issues and will update impacted devices as soon as possible." No timeline, no out-of-band cycle commitment, no CVE assignment yet.

**Mitigations published:** The article cites combining a **BitLocker PIN with a BIOS password** as a mitigation for the released YellowKey PoC against TPM-only configurations. The researcher publicly states TPM+PIN is "still exploitable regardless" — meaning a more complete PoC against TPM+PIN BitLocker exists in research but was not published.

**Lineage precedent (BleepingComputer editorial framing):** The article relates YellowKey and GreenPlasma to prior leaked Windows exploits **BlueHammer (CVE-2026-33825)** and **RedSun (no identifier assigned)**, which the article states "began to be exploited in the wild shortly after being publicly disclosed." This is B-grade editorial pattern observation, not Microsoft-attested ITW.

**Researcher motivation:** The article relays Chaotic Eclipse expressing frustration with Microsoft's vulnerability handling cadence — characterized as "disgruntled." The 13-word researcher quote captured in the article: "I just never managed to understand why this vulnerability is sooo well hidden."

**Direct researcher / vendor quotes used (each <=15 words, one per source per LEGAL-POLICY §Copyright):**
- *Microsoft (via BleepingComputer):* "committed to investigating reported security issues and will update impacted devices as soon as possible" (12 words).
- *Chaotic Eclipse:* "I just never managed to understand why this vulnerability is sooo well hidden" (13 words).

## Extraction notes — A&D / DIB structural relevance

BitLocker is the standard Windows full-disk-encryption deployment that satisfies multiple regulatory mandates relevant to the Archimedes target profile (US A&D prime, ITAR-regulated, CMMC Level 2+ for CUI):

- **CMMC Level 2** (DoD 32 CFR Part 170): NIST SP 800-171 control 3.13.16 — "Protect the confidentiality of CUI at rest." BitLocker is the canonical implementation across the DIB.
- **NIST 800-53 SC-28** — equivalent control for the cleared-environment baseline.
- **HSPD-12 / FIPS 140-2/3 cryptographic-module requirements** — BitLocker on Windows 11 / Server 2022 / Server 2025 meets the FIPS module validation when configured per FIPS-mode guidance.

A BitLocker bypass affecting Windows 11 and the current Windows Server generations is therefore relevant to **every prime on aerospace-defense.yaml**, but the threat-model is narrower than the OS deployment population suggests:

- **Physical-access requirement:** YellowKey requires either a USB drive or write access to the EFI partition on the target's drive. This is a **physical-access OR insider-access OR supply-chain attack class**, not a remote attack vector.
- **Original-device requirement:** YellowKey explicitly does not unlock stolen drives — the TPM-bound key release still requires the original platform. The threat model is then "attacker recovers or accesses the original hardware, then boots into WinRE and gains shell" — closer to evil-maid / supply-chain / facility-physical-access than to remote compromise.

This narrows the operator-actionable surface: A&D primes with **classified-handling SCIFs, classified-laptop programs, traveler-laptop policies, supply-chain-shipped pre-loaded devices, and any program that depends on BitLocker for at-rest protection of CUI on systems leaving controlled spaces** are the at-risk surface. Pure remote-network threat models are not implicated by these PoCs as published.

GreenPlasma's LPE class is more universally applicable — any local user account on an affected Windows host can theoretically escalate to SYSTEM, but the PoC was described as incomplete.

## Extraction notes — FLASH trigger evaluation summary

This raw-signal sits at **Trigger 6 marginal-fail** per the rationale in the frontmatter. Patch unavailable + wide deployment + public PoC ALL satisfied; "exploitation_confirmed_or_imminent per A-grade" FAILS because BleepingComputer is B-grade and the BlueHammer / RedSun lineage-pattern observation is B-grade editorial framing rather than A-grade attestation.

Recommend grader frame this as a **standalone afternoon-brief Vulnerabilities-section item at WEP "possible"** with explicit caveats:
1. Single B-grade origin (BleepingComputer); no A-grade corroboration yet (MSRC advisory not published, CISA KEV not added, no Tier-1 vendor analysis).
2. Patch unavailable as of disclosure.
3. Public PoC repos exist on GitHub (research artifacts, not actor infrastructure).
4. Class lineage shows post-disclosure ITW pattern (BleepingComputer's own framing; flag as pattern claim, not first-party-attested).
5. Physical-access / supply-chain / evil-maid attack class — not remote.

Forward weaponization triggers to monitor over next 24-72h:
- MSRC advisory publication → CVE assignment → CVSS score
- CISA KEV addition (would shift to Trigger 1)
- Tier-1 vendor analysis (Mandiant, CrowdStrike, MSTIC, Sophos X-Ops, ESET)
- Independent ITW telemetry from EDR / IR firm

## Extraction notes — Splunk first-party check

`(index=archimedes OR index=defenseclaw_local) earliest=-24h NOT sourcetype=archimedes:* | stats count by sourcetype` returned **0 events** at the time of this raw-signal collection — twentieth consecutive dormant non-archimedes-internal stream sweep. No first-party telemetry to bump external claims in either direction.

## Extraction notes — Hard Rules compliance

- **Hard Rule 2 (no attribution origination):** N/A — no actor attribution claimed in the source.
- **Hard Rule 3 (no exploitation, ever):** Compliant. Raw-signal records the public existence of PoCs and the class of technique; does NOT reproduce or summarize working exploit code beyond what the BleepingComputer article already publicly describes at vulnerability-class level. GitHub PoC repo URLs are recorded for grader / vuln-tracker pivot, not for reproduction.
- **Hard Rule 4 (never scan third parties):** Compliant — no scanning conducted.
- **Hard Rule 6 (15-word quote limit, one per source):** Compliant — two quotes captured, both ≤15 words, one per source (Microsoft + Chaotic Eclipse).
- **Hard Rule 7 (credentials are radioactive):** N/A — no credentials in this surface.
- **Hard Rule 8 (Splunk first-party priority):** Splunk dormant; no first-party signal to contradict or confirm BleepingComputer's claims.

## IOCs (from ioc-extraction skill — not invoked this raw-signal)

No IOC extraction performed. Disclosure does not contain attacker infrastructure (no C2 IPs, no malicious domains, no malicious hashes). The two GitHub PoC repository URLs (`github.com/Nightmare-Eclipse/YellowKey`, `github.com/Nightmare-Eclipse/GreenPlasma`) are research artifacts, not attacker-controlled infrastructure, and are NOT added to `threats/iocs/_master-index.yaml` to avoid muddying the IOC corpus with research repos. They are captured here as keywords for grader pivot.
