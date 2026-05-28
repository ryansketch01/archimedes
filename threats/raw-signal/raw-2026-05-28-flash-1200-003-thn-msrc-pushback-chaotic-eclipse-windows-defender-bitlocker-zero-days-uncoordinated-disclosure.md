---
raw_id: raw-2026-05-28-flash-1200-003
collected_at: 2026-05-28T12:20:00-04:00
run_id: flash-sweep-20260528-120000
collection_mode: flash_sweep
source:
  source_yaml_id: thehackernews
  source_name: The Hacker News
  source_url: https://thehackernews.com/2026/05/microsoft-slams-public-zero-day.html
  origin_disclosure_handles: ["Chaotic Eclipse", "Nightmare-Eclipse"]
  published_at: 2026-05-28T~AM-EDT
match_reason:
  watchlist: []
  actors: []
  vulnerabilities:
    - CVE-2026-33825   # BlueHammer (Microsoft Defender)
    - CVE-2026-41091   # RedSun (Microsoft Defender)
    - CVE-2026-45498   # UnDefend (Microsoft Defender)
    - CVE-2026-45585   # YellowKey (BitLocker)
    - GreenPlasma      # BitLocker (no CVE shown in THN excerpt)
    - MiniPlasma       # Windows SYSTEM escalation (no CVE shown)
  keywords: [Microsoft Defender, BitLocker, uncoordinated disclosure, GitHub account removal, GitLab block, public zero-day disclosure]
triage_tags:
  - flash_candidate
  - trigger-6-zero-day-no-patch
  - single_source_veto_candidate
  - microsoft_disputed
  - uncoordinated_disclosure
  - widely_deployed_product
iocs_extracted: true
iocs_count: 6
text_word_count: 400
promoted: false
rejected_at: 2026-05-28T12:45:00-04:00
rejection_id: reject-2026-05-28-0001
rejection_run_id: flash-grade-20260528-120000
rejection_summary: "Sixth surface in Archimedes corpus on the same Chaotic Eclipse Windows zero-day disclosure cluster (prior coverage finding-2026-05-13-0003 + finding-2026-05-18-0001 + finding-2026-05-20-0003 + finding-2026-05-21-0001 + _index.yaml ZD-001 BlueHammer already patched). Anti-noise rule 1 continuation; single-source veto on ITW exploitation claim (disclosing party with motive to inflate; Microsoft authoritative silence); Hard Rule 8 + Hard Rule 2 binding; net-new Microsoft pushback narrative falls below FLASH B2 threshold as single-source THN B-grade relay with no independent A/B corroboration. Belongs in scheduled-brief Industry-News UPDATE block on the Chaotic Eclipse disclosure lineage, NOT standalone FLASH promotion."
ttl_expires_at: 2026-08-26T12:20:00-04:00
flash_trigger_evaluation:
  trigger_6_zero_day_no_patch:
    matched: borderline_single_source
    no_patch: true_per_thn
    cvss_or_wide_deployment: wide_deployment_microsoft_defender_bitlocker_windows_native_components
    exploitation_confirmed_or_imminent: claimed_in_wild_per_disclosing_party_only_microsoft_did_not_confirm
    a_grade_source: thehackernews_B_microsoft_msrc_A_but_msrc_disputes_disclosure_not_confirms_exploitation
    notes: |
      THN cites three of the six (BlueHammer / RedSun / UnDefend, all Defender)
      as "active in the wild." Source of that claim is the disclosing party
      "Chaotic Eclipse" / "Nightmare-Eclipse" — same party with motive to inflate
      severity claims. Microsoft's response disputes the DISCLOSURE PROCESS
      ("uncoordinated") but does NOT confirm or deny in-wild exploitation.
      GitHub removed researcher's account; GitLab subsequently blocked a new
      account hosting exploit code.

      HARD RULE 2 / HARD RULE 8: single-source claim — Chaotic Eclipse is the
      ONLY origin attesting active in-wild exploitation. Microsoft (the
      authoritative source for confirming exploitation of its own products)
      has not corroborated. THN relays the claim without independent verification.
      Grader is expected to apply single-source veto on the "active in the wild"
      attribution; the disclosure itself is fact (the CVEs are real) but the
      WEP claim around exploitation should not exceed "possible."

      Trigger 6 evaluation: no-patch is confirmed; widely-deployed is confirmed
      (Defender + BitLocker ship in every Windows install); exploitation
      "confirmed or imminent per A-grade source" — Microsoft is A-grade and
      Microsoft has NOT confirmed exploitation. Grader's call on whether THN's
      relay of Chaotic Eclipse's claim qualifies. Defensible disposition:
      raw-signal for record but NOT promoted to FLASH given the single-source
      veto on the exploitation claim.

      HARD RULE 3: NO exploit content / PoC code extracted — refer to upstream
      THN article only.
---

# Microsoft Slams Public Zero-Day Disclosures Amid GitHub Researcher Account Removal

**Source:** The Hacker News (relaying disclosure by "Chaotic Eclipse" / "Nightmare-Eclipse")
**Published:** 2026-05-28

## Body

A security researcher operating under the handles **"Chaotic Eclipse"** and **"Nightmare-Eclipse"** publicly disclosed six previously-unknown Windows vulnerabilities without prior notification to Microsoft. The researcher justified the public release by citing "a breakdown in vulnerability disclosure process." GitHub subsequently removed the researcher's account; GitLab blocked a newly-created account hosting exploit code.

**Six disclosed vulnerabilities (per THN summary):**

| Disclosed name | CVE | Component | Status per disclosing party |
|---|---|---|---|
| BlueHammer | CVE-2026-33825 | Microsoft Defender | "Active in the wild" |
| RedSun | CVE-2026-41091 | Microsoft Defender | "Active in the wild" |
| UnDefend | CVE-2026-45498 | Microsoft Defender | "Active in the wild" |
| YellowKey | CVE-2026-45585 | BitLocker | "Disclosed" |
| GreenPlasma | not stated | BitLocker | "Disclosed" |
| MiniPlasma | not stated | Windows (SYSTEM-tier escalation) | "Disclosed" |

**Patch status:** None of the six are patched at disclosure time. CVSS scores not provided in THN excerpt.

**Microsoft's response (paraphrased):** Microsoft characterized the disclosure as uncoordinated and risk-elevating for customers; the company advocates Coordinated Vulnerability Disclosure (CVD). Microsoft did NOT confirm in-wild exploitation of any of the six.

**Platform actions:** GitHub removed the researcher's account; GitLab blocked the followup account hosting exploit content.

**A&D relevance (collector observation):** Microsoft Defender + BitLocker are baseline Windows enterprise endpoint controls. Defender bypass + BitLocker key extraction + SYSTEM escalation, all in one disclosure batch, against unpatched vulnerabilities, against an audience that runs Windows enterprise — relevant to DIB / aerospace endpoint estate IF the in-wild exploitation claims hold up. They are currently single-source-attested.

**Hard Rule 2 / Hard Rule 8 single-source veto candidate:** The ONLY origin for "active in the wild" is the disclosing party. Microsoft has not corroborated. THN relayed the claim without independent verification.

## Extraction notes

- Language: en
- Article type: vulnerability-disclosure / vendor-response
- Raw IOC extraction invoked: yes (CVE list only — no exploit content)
- Hard Rule 3: no PoC or technical exploitation walkthrough captured.

## IOCs (from ioc-extraction skill)

```yaml
iocs:
  - indicator: CVE-2026-33825
    type: cve
    nickname: BlueHammer
    component: Microsoft Defender
    patch_available: false
    cvss: not_stated
    exploitation_claim: active_in_wild_per_disclosing_party_only

  - indicator: CVE-2026-41091
    type: cve
    nickname: RedSun
    component: Microsoft Defender
    patch_available: false
    cvss: not_stated
    exploitation_claim: active_in_wild_per_disclosing_party_only

  - indicator: CVE-2026-45498
    type: cve
    nickname: UnDefend
    component: Microsoft Defender
    patch_available: false
    cvss: not_stated
    exploitation_claim: active_in_wild_per_disclosing_party_only

  - indicator: CVE-2026-45585
    type: cve
    nickname: YellowKey
    component: BitLocker
    patch_available: false
    cvss: not_stated
    exploitation_claim: disclosed_not_in_wild

  - indicator: GreenPlasma
    type: cve_pending
    component: BitLocker
    patch_available: false
    exploitation_claim: disclosed_not_in_wild

  - indicator: MiniPlasma
    type: cve_pending
    component: Windows (SYSTEM-tier escalation)
    patch_available: false
    exploitation_claim: disclosed_not_in_wild

attribution_claims:
  - source: "Chaotic Eclipse" / "Nightmare-Eclipse" (security researcher; disclosing party)
    language: "active in the wild" (for three Defender CVEs)
    actor_named: null
    nation_state_named: null
    confidence: disclosing-party-self-attestation
    notes: "Single-source claim. Microsoft (the A-grade authoritative source for confirming exploitation of its own products) has not corroborated."

  - source: Microsoft (MSRC)
    language: "details were not shared with Microsoft prior to release ... disclosures put our customers at unnecessary risk"
    actor_named: null
    nation_state_named: null
    confidence: disputes_disclosure_process_not_exploitation_status
    notes: "Microsoft contests the disclosure process but does not confirm or deny in-wild exploitation."
```
