---
raw_id: raw-2026-05-29-pm-002-securityweek-in-other-news-roundup-trump-mobile-russia-apt-treasury-vscode-176npm-fifa-megalodon-enrichment
collected_at: 2026-05-29T15:45:00-04:00
run_id: pre-brief-20260529-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: securityweek
  source_name: SecurityWeek "In Other News" weekly roundup (Eduard Kovacs et al)
  source_url: https://www.securityweek.com/in-other-news-trump-mobile-data-breach-fifa-world-cup-phishing-cisa-responds-to-supply-chain-attacks/
  published_at: 2026-05-29T16:20:49+00:00
match_reason:
  watchlist: []                 # No A&D-prime named in any roundup item
  actors:
    - roster_009_APT29_historical    # SecurityWeek references "Russian state-sponsored APT" from SolarWinds 2019-2020 campaign with deep US Treasury email access — APT29-cluster historical activity per public attribution. This is a 2026 FOIA document release on a 2019 incident, NOT new attribution. Anti-noise to existing APT29 dossier; no fresh signal beyond standing-knowledge baseline
    - roster_010_Salt_Typhoon_outside_window  # NOT in this roundup (named earlier this week but not in 2026-05-29 SecurityWeek roundup)
    - cluster_ghost_stadium_chinese_fifa     # carry-forward — already absorbed PM-28-005 (FBI/Group-IB Ghost Stadium 4,300 domains) → finding-2026-05-28-FLASH-1800-0001. Anti-noise lock applies; SecurityWeek mention is bounded restatement
    - cluster_megalodon_npm_supply_chain     # carry-forward — Megalodon attackers + Nx Console enrichment to VT-009 carries from PM-28-004 → finding cluster. 176 malicious npm packages with postinstall credential-stealing is operational expansion of VT-006 / VT-009 cluster but unattributed; SecurityWeek does NOT attribute to TeamPCP, Shai-Hulud, Mini Shai-Hulud, or any roster actor
  vulnerabilities:
    - VT-006                    # Mini Shai-Hulud / TanStack / CVE-2026-45321 cluster — already KEV-listed 2026-05-27; SecurityWeek In Other News bounded restatement
    - VT-009                    # Nx Console / CVE-2026-48027 cluster — already KEV-listed 2026-05-27; bounded restatement
    - cve_chain_no_new_tracked  # 176 npm packages with version 99.99.99 + postinstall credential-stealing → no individual CVE assignment per SecurityWeek piece; ecosystem-level pattern signal for vuln-tracker / VT-006 / VT-009 cluster awareness, NOT a fresh tracking candidate
    - vs_code_remote_ssh_rce    # researcher Suman Kumar Chakraborty disclosure of Remote-SSH extension RCE via bootstrap-script-in-Temp pathway. No CVE assigned per SecurityWeek summary. NOT in _index.yaml. No ITW. Coordinated-disclosure class. Vuln-tracker monitoring-only candidate
    - veeam_backup_two_high     # two high-severity Veeam Backup & Replication patches (privesc + arbitrary file writes). Vendor-coordinated. No ITW. Not in _index.yaml — vendor-patch monitoring-only
    - notepad_plus_plus_v8961   # three Notepad++ patches including two arbitrary code execution flaws v8.9.6.1. Vendor-coordinated. No ITW. Not in _index.yaml
    - roundcube_patches_2024_05_24   # eight Roundcube flaws including unauth SQL injection + arbitrary file delete (v1.6.16, 1.7.1 released 2026-05-24). Vendor-coordinated. No ITW. Not in _index.yaml
  keywords:
    - "Trump Mobile data breach"
    - "Russian state-sponsored APT"
    - "Treasury email access"
    - "SolarWinds 2019-2020 incident"
    - "FOIA lawsuit 2026"
    - "VS Code Remote-SSH RCE"
    - "Suman Kumar Chakraborty"
    - "UK Visa Portal AWS S3 bucket"
    - "100,000 documents passports selfies"
    - "LinkedIn phishing Adobe Target"
    - "Ghost Stadium FIFA"
    - "4,300 fraudulent FIFA domains"
    - "Veeam Backup Replication"
    - "Notepad++ v8.9.6.1"
    - "Roundcube v1.6.16 v1.7.1"
    - "CISA supply chain KEV additions"
    - "Megalodon attackers"
    - "5,500 GitHub repositories"
    - "176 malicious NPM packages"
    - "version 99.99.99"
    - "postinstall credential stealing"
    - "Maxwell Schultz contractor 24 months"
triage_tags:
  - in_other_news_roundup
  - structural_context_no_a2_promotion_candidate
  - russia_apt_treasury_historical_2019_anti_noise_to_apt29_baseline
  - npm_supply_chain_cluster_enrichment_unattributed
  - 176_packages_post_install_credential_steal_vt006_vt009_adjacent
  - megalodon_5500_repos_enrichment
  - ghost_stadium_carry_forward_pm28_lock_active
  - vs_code_remote_ssh_research_disclosure_no_itw
  - vendor_patch_layer_no_itw_no_tracking
  - civil_litigation_22andme_separate_item
iocs_extracted: false
iocs_count: 0                   # SecurityWeek "In Other News" is summary-format; no specific IOCs published in the piece for any of the listed items
text_word_count: 1750
promoted: false
rejected_at: 2026-05-29T16:14:00-04:00
rejection_id: reject-2026-05-29-0001
grading_run_id: afternoon-20260529-160000
ttl_expires_at: 2026-08-27T15:45:00-04:00
test: false
---

# SecurityWeek "In Other News" — Trump Mobile, Russia APT Treasury, VS Code RCE, FIFA, CISA supply-chain, 2026-05-29

Source: SecurityWeek "In Other News" weekly roundup published 2026-05-29T16:20:49 UTC by SecurityWeek News (institutional byline). URL: https://www.securityweek.com/in-other-news-trump-mobile-data-breach-fifa-world-cup-phishing-cisa-responds-to-supply-chain-attacks/

**Disposition for grader:** structural-context item. Most discrete entries are vendor-patch summaries, civil-litigation updates, or already-absorbed-in-prior-windows campaigns. Three items merit individual call-out: (1) Russian APT Treasury 2019 FOIA-release reference (historical, anti-noise to APT29 baseline), (2) **176 malicious npm packages + Megalodon enrichment** (operational cluster-expansion signal for VT-006 / VT-009, but **unattributed** — no Shai-Hulud / Mini Shai-Hulud / TeamPCP designation by SecurityWeek), (3) VS Code Remote-SSH RCE researcher disclosure (no CVE / no ITW / no roster). The rest are roundup-format noise.

## Discrete items (categorized)

### Item 1 — Trump Mobile data breach

**What:** Trump Mobile customer data exposed via third-party platform provider. Names, addresses, emails, phone numbers, "and other data" affected. **Disposition:** consumer-telecom breach, not A&D, not roster, not tracked vuln. DISCARDED for finding-grader consideration. Background context for briefer at most.

### Item 2 — Russian state-sponsored APT Treasury email access (FOIA release)

**What:** SecurityWeek surfaces FOIA-released 2026 documents on the 2019-2020 SolarWinds-linked Russian state-sponsored APT campaign with deep access to U.S. Treasury Department emails. Per the documents, eight email accounts linked to ~300 others were focal. **Disposition:** **historical 2019 incident** (APT29-cluster public-attribution baseline; not new attribution and not a fresh state transition). Anti-noise to existing APT29 dossier; no actor-tracking action required. The FOIA-release timing is noteworthy as a public-attention surfacing of long-known activity but does NOT cross a Trigger-2 (tracked-actor-attribution) threshold per FLASH-POLICY (would need NEW attribution).

**Grader note:** Hard Rule 2 — the public attribution baseline already names APT29-cluster for SolarWinds; SecurityWeek's framing as "Russian state-sponsored APT" is appropriately conservative. Do NOT use this surface to attempt actor-attribution upgrade or to re-baseline the APT29 dossier (already at HIGH per roster).

### Item 3 — VS Code Remote-SSH RCE researcher disclosure

**What:** Suman Kumar Chakraborty discloses Remote-SSH extension RCE vulnerability allowing pivot attacks via bootstrap-script-in-Temp pathway. SecurityWeek summary describes the mechanism without naming a CVE. **Disposition:** coordinated-disclosure class, no ITW exploitation language, no roster actor attribution. Vuln-tracker monitoring-only candidate; would convert to active tracking if CVE assigned + ITW signal surfaces. NOT in _index.yaml.

**Researcher**: Suman Kumar Chakraborty (independent / not yet in source-grades.yaml). First Archimedes-corpus citation; would be provisional C/F starting grade per LayerX / Seqrite / Trendyol-Albayrak / depthfirst precedent depending on technical-output observable surface. Source-grade-log review candidate.

### Item 4 — UK Visa Portal AWS S3 exposure

**What:** Over 100,000 documents exposed including passports and selfies in unsecured AWS S3 bucket; private (non-government-affiliated) UK Visa Portal vendor; secured earlier in the week. **Disposition:** PII exposure, not A&D, not roster, not tracked vuln, not threat-intel-class incident. DISCARDED.

### Item 5 — LinkedIn phishing via Adobe Target

**What:** Phishers abused Adobe Target platform to track victims and steal credentials; HTML files masquerading as PDFs redirect to fake LinkedIn login. **Disposition:** commodity phishing campaign exploitation pattern; no roster actor, no A&D, no tracked vuln. Defensive-awareness-only.

### Item 6 — Ghost Stadium FIFA World Cup phishing (CARRY-FORWARD)

**What:** "Over 4,300 fraudulent domains impersonating FIFA" with "pixel-perfect clone" by Chinese-speaking Ghost Stadium group; potential "hundreds of millions of dollars in losses" pre-World-Cup-kickoff. **Disposition:** **ANTI-NOISE LOCK ACTIVE** — Ghost Stadium 4,300-domain cluster already raw-signaled PM-28-005 (FBI/Group-IB primary) → finding-2026-05-28-FLASH-1800-0001 cluster. SecurityWeek mention is bounded restatement (no new actor / no new TTP / no new victim disclosure / no new IOC). Block from afternoon brief consideration.

### Item 7 — Veeam Backup & Replication two high-severity patches

**What:** Privilege escalation + arbitrary file writes patched in Veeam. **Disposition:** vendor-coordinated disclosure layer, no ITW per SecurityWeek summary, no CVE detail provided in the roundup. Patch-Tuesday-class entry; vendor announcement context-only. NOT in _index.yaml.

### Item 8 — Notepad++ v8.9.6.1 patches

**What:** Three security issues including two arbitrary code execution flaws patched in v8.9.6.1. **Disposition:** vendor-coordinated disclosure, no ITW, no CVE detail provided. NOT in _index.yaml.

### Item 9 — Roundcube v1.6.16 / 1.7.1 patches

**What:** Eight Roundcube flaws fixed (versions 1.6.16, 1.7.1 released 2026-05-24) including unauthenticated SQL injection and arbitrary file delete. **Disposition:** vendor-coordinated disclosure, no ITW, no CVE detail provided in roundup. Roundcube IS used at some federal/government webmail deployments — possible vuln-tracker monitoring candidate if CVE assignment + ITW signal surface later. NOT in _index.yaml.

### Item 10 — CISA supply chain KEV additions (CARRY-FORWARD)

**What:** CISA added CVE-2026-8398 (Daemon Tools Lite) + CVE-2026-45321 (TanStack) + CVE-2026-48027 (Nx Console) to KEV catalog on 2026-05-27. **Disposition:** **ANTI-NOISE LOCK ACTIVE** — already absorbed PM-27 brief; restated here without new operational state. Block from afternoon brief consideration.

### Item 11 — Megalodon attackers / Nx Console alert (CARRY-FORWARD WITH ENRICHMENT)

**What:** CISA issued 2026-05-28 alert on Megalodon and Nx Console attacks; npm invalidated granular access tokens; "5,500+ GitHub repositories infected per separate reporting." **Disposition:** carry-forward with enrichment. The "5,500+ GitHub repositories infected" framing extends the operational scope beyond GitHub's previously published 3,800-internal-repo figure (finding-2026-05-20-FLASH-0001 baseline). SecurityWeek attributes the 5,500+ number to "separate reporting" without naming the source — secondary-relay-of-relay framing; not standalone-citable as fact.

**Grader note:** Hard Rule 2 — the 5,500 number is unattributed in the SecurityWeek summary and may be conflating the Megalodon-attacker campaign with the separate Nx Console / VS Code marketplace extension compromise. Do NOT treat the 5,500-repo figure as corroborated for the Megalodon campaign specifically without identifying the underlying primary.

### Item 12 — 176 malicious npm packages (NEW operational signal)

**What:** "Supply chain attack using 176 NPM packages with postinstall scripts stealing credentials and secrets" — packages using "version 99.99.99" pattern; "malware harvests CI/CD secrets, environment variables, tokens." **Disposition:** operational cluster-expansion signal **adjacent to but not attributed to** the active VT-006 (Mini Shai-Hulud / CVE-2026-45321 / TeamPCP) and VT-009 (Nx Console / CVE-2026-48027) clusters. SecurityWeek does NOT attribute these 176 packages to TeamPCP, Shai-Hulud, Mini Shai-Hulud, or any roster actor.

**Mechanism comparison:**
- VT-006 Mini Shai-Hulud: TanStack credential theft via malicious package versions, TeamPCP-attributed by Wiz / Snyk / StepSecurity
- VT-009 Nx Console: VS Code marketplace extension credential-harvest via compromised employee device, GitHub self-disclosed
- 176-package campaign: postinstall scripts harvest CI/CD secrets / env vars / tokens via version 99.99.99 pattern, **UNATTRIBUTED** per SecurityWeek

The "version 99.99.99" pattern is a distinct tradecraft signature (semver-string abuse to force resolution priority) that is NOT documented in the Wiz / Snyk / StepSecurity Mini Shai-Hulud research and NOT documented in the GitHub Nx Console self-disclosure. This is **probably a separate campaign** with overlapping victim sector (npm/CI/CD ecosystem) but different mechanism and possibly different actor.

**Grader note:** Hard Rule 2 — do NOT propagate a Shai-Hulud-lineage framing onto the 176-package campaign without an A/B-grade source making that attribution. The cluster-adjacency signal is valuable for trend-analysis context but does not warrant attribution upgrade. Vuln-tracker should consider whether VT-006 / VT-009 dossier expansion to include "176-package version-99.99.99 adjacent unattributed wave" is warranted given the operational pattern.

**No specific IOCs published in SecurityWeek piece.** Would require fetching the underlying primary (likely a vendor-research-firm blog) to obtain package names, hashes, C2 destinations. Flag for grader review; if vuln-tracker / VT-006 / VT-009 cluster expansion is decided, identify the underlying primary on the next collection pass.

### Item 13 — Contractor sentenced (Maxwell Schultz, Columbus OH)

**What:** Maxwell Schultz, 36, sentenced to 24 months for hacking former employer network post-termination; reset ~2,500 passwords; $862K+ losses; pleaded guilty Nov 2025; offense May 2021. **Disposition:** insider-threat criminal case, completed legal proceeding. Not A&D, not roster, not threat-intel cadence. DISCARDED.

### Item 14 — California AG sues 23andMe (also in separate BleepingComputer + Register items today)

**What:** California AG Rob Bonta sues Chrome Holding Co. (formerly 23andMe) over 2023 genetic-data breach. **Disposition:** civil litigation on already-known breach; not threat-intel cadence. DISCARDED.

## Anti-noise locks honored

Multiple items in this roundup are bounded carry-forward restatements of already-absorbed material:
- Ghost Stadium (PM-28-005 lock active until 2026-05-29T18:00)
- CISA KEV additions Daemon Tools / TanStack / Nx Console (PM-27 absorption)
- Megalodon / Nx Console (PM-28-004 absorption baseline)
- GitHub VS Code marketplace extension 3,800-repo baseline (finding-2026-05-20-FLASH-0001)

The 176-malicious-npm-packages item is the **only** NEW operational signal in this roundup. Worth grader review as cluster-context, not as a standalone finding.

## Extraction notes

- Language: en
- Article type: weekly news roundup (SecurityWeek "In Other News" format — bounded summary entries, no deep-research analysis)
- Raw IOC extraction invoked: no (roundup format does not publish IOCs in-piece; individual items would require primary-source retrieval)
- Quote discipline: Trump Mobile breach + Russian APT Treasury access wording preserved at summary-level; no >15-word quotes propagated
- Hard Rule 2: no actor-attribution upgrade. Russian APT Treasury reference is 2019 SolarWinds-cluster historical; 176-package campaign explicitly unattributed per SecurityWeek. The 5,500-repo Megalodon figure is unattributed in SecurityWeek and is NOT corroborated for the Megalodon campaign specifically without primary-source identification
- Hard Rule 6: no quoted passages used in this raw-signal; all extraction is summary-paraphrase. Quote discipline preserved for downstream brief composition
- Single-source veto evaluation: NOT applicable. This is a summary-format relay; the items it covers each have their own underlying primaries. Single-source analysis applies item-by-item at the underlying-primary level if grader promotes any to finding
- 72h auto-downgrade clock: NOT applicable
