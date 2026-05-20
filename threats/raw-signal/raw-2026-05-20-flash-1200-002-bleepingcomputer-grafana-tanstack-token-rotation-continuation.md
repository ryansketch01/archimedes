---
raw_id: raw-2026-05-20-flash-1200-002
collected_at: 2026-05-20T12:10:00-04:00
run_id: flash-sweep-20260520-120000
collection_mode: flash_sweep
test: false
source:
  source_yaml_id: bleepingcomputer
  source_name: "BleepingComputer (Bill Toulas) — relay of Grafana Labs security update blog"
  source_url: https://www.bleepingcomputer.com/news/security/grafana-breach-caused-by-missed-token-rotation-after-tanstack-attack/
  published_at: 2026-05-20T11:46:37-04:00
match_reason:
  watchlist: []
  actors: [TeamPCP]
  vulnerabilities: [VT-006]
  keywords:
    - Grafana breach
    - TanStack supply chain
    - missed GitHub workflow token rotation
    - Shai-Hulud malware campaign
    - TeamPCP attribution
    - credential stealer
    - Grafana official security update blog
triage_tags:
  - in_window
  - bleepingcomputer_b_grade_relay
  - grafana_a_grade_self_disclosure_official_security_blog
  - tracked_actor_teampcp_001_high
  - tracked_vulnerability_vt_006_cve_2026_45321
  - anti_noise_absorbed_teampcp_github_corp_breach_lock_2026_05_20_06_08
  - anti_noise_absorbed_same_campaign_cluster_vt_006_mini_shai_hulud_lineage
  - grafana_named_victim_downstream_continuation_not_new_attribution
  - non_flash_morning_brief_vt_006_update_block_candidate
  - splunk_first_party_zero_hits_49th_consecutive_dormant_sweep
iocs_extracted: false
iocs_count: 0
text_word_count: 320
promoted: false
rejected_at: 2026-05-20T16:18:00-04:00
rejection_id: reject-2026-05-20-0001
ttl_expires_at: 2026-08-18T12:10:00-04:00
---

# Grafana breach caused by missed token rotation after TanStack attack

## Article body summary (extracted)

BleepingComputer Bill Toulas byline relays Grafana Labs' official security
update blog (grafana.com/blog/grafana-labs-security-update-latest-on-tanstack-
npm-supply-chain-ransomware-incident/) confirming that the Grafana breach
covered in prior news cycle was caused by a single GitHub workflow token
that escaped the post-incident credential rotation following the
2026-05-12 TanStack npm supply-chain attack (Mini Shai-Hulud parent
surface, VT-006 / CVE-2026-45321 lineage).

**Source-of-disclosure:** Grafana Labs official — vendor self-disclosure on
own incident.

**Attribution language:** "Shai-Hulud malware campaign attributed to TeamPCP
hackers" / "dozens of TanStack packages" with credential-stealing code.

**Incident framing:** *past* exploitation (token rotation cycle 2026-05-12 →
~2026-05-16 window); not ongoing active exploitation against Grafana at
publication.

**New IOCs:** none provided in BleepingComputer relay.

**Named victims beyond Grafana:** none in this article.

**A&D / aerospace / defense references:** none.

**CVE:** none assigned to the Grafana-side incident specifically; VT-006 /
CVE-2026-45321 remains the parent surface CVE.

## Anti-noise lock evaluation

Active anti-noise locks at 12:00 sweep:

1. `teampcp-github-internal-repos-breach-via-vscode-extension-2026-05-20`
   (06:08 queued FLASH; valid to 2026-05-21T06:08:00-04:00) — TeamPCP
   campaign cluster, GitHub-corp specifically as victim
2. VT-006 / CVE-2026-45321 parent surface — Mini Shai-Hulud worm,
   attribution to TeamPCP via Wiz + Snyk + StepSecurity per
   finding-2026-05-12-FLASH-0001
3. AM raw-signal raw-2026-05-20-am-001 — @antv namespace continuation,
   already in finding-2026-05-20-0001

Grafana / TanStack token-rotation continuation is the same TeamPCP campaign
cluster, downstream-victim continuation. The lock at (1) explicitly covers
TeamPCP campaign-chain extensions (the 06:08 brief's anti-noise distinction
block enumerates Mistral, Trivy, Checkmarx, Bitwarden CLI, TanStack, OpenAI,
Grafana, GitHub-corp as parallel commercialization / supply-chain branches).
Grafana is named in that block. Per FLASH-POLICY anti-noise rule 1, this
item ABSORBS into the existing lock.

## FLASH trigger evaluation

- T1: FAIL — no new CVE
- T2: FAIL by anti-noise lock — TeamPCP attribution NOT new in 24h window
  (already attributed in 06:08 queued FLASH and 2026-05-12 originating
  surface)
- T3: FAIL — Splunk -24h zero hits on tracked-IOC superset
- T4: FAIL by anti-noise lock — token-rotation hygiene failure is not a
  tradecraft pivot; same VT-006 worm post-exploitation mechanism
- T5: FAIL — Grafana not on A&D watchlist; no A&D-sector specifics
- T6: FAIL — no zero-day

## Why surface as raw-signal anyway

This is a grader-morning-brief-UPDATE-block candidate on VT-006 / TeamPCP
lineage. The Grafana official disclosure adds a named-A-grade-self-
disclosure layer to the campaign cluster (vendor authority on own incident,
same procedural-A class as F5 / OpenAI / kernel.org netdev / Nx Team Nrwl
precedent). The morning brief that the briefer composes from
finding-2026-05-20-0001 (Mini Shai-Hulud @antv continuation) may want
to fold Grafana into an UPDATE block as the latest named-enterprise victim
on the VT-006 campaign chain.

Surfacing as raw-signal (not FLASH-candidate) is the correct disposition:
- Anti-noise lock prevents duplicate FLASH
- Operational tempo of the TeamPCP campaign now spans:
  - 2026-05-12: Mini Shai-Hulud npm + PyPI worm deployment (originating
    FLASH)
  - 2026-05-14: Mistral AI 450 repos sale (raw-2026-05-14-flash-2200-001)
  - 2026-05-15: Source-code release + BreachForums bounty
    (flash-2026-05-15-0600-teampcp-shai-hulud-release)
  - 2026-05-19: actions-cool/issues-helper + @antv preview surfaces
    (finding-2026-05-19-0001 with t.m-kosche.com cross-corpus C2 repeat)
  - 2026-05-20: GitHub-corp self-disclosure (06:08 queued FLASH;
    flash-2026-05-20-0608-teampcp-github-internal-repos)
  - 2026-05-20: @antv namespace continuation (finding-2026-05-20-0001;
    SecurityWeek 11:06 EDT in-window confirms)
  - **2026-05-20: Grafana token-rotation-miss disclosure (this item)**
- Grafana surface offers concrete operational lesson for A&D defenders:
  token-rotation-cycle completeness audit is the actionable signal — a
  single GitHub-workflow-token miss propagated from the TanStack
  exposure to the Grafana codebase breach.

## Provisional source addition flag for librarian

`grafana-self-disclosure` is a candidate for provisional A first-citation
on the same vendor-authority-on-own-incident class as f5 / openai-self-
disclosure / kernel-org-netdev / nx-team-nrwl / github-blog-self-disclosure
precedent. Vendor disclosure on own incident is procedurally A-grade.
Librarian source-grade-log to ingest at next pass; awaiting direct-
retrieval verification of grafana.com/blog primary URL (this sweep only
retrieved BleepingComputer relay).

## Hard Rules compliance

- Rule 2: TeamPCP attribution preserved as Grafana-via-BleepingComputer
  attribution chain; not Archimedes-originated; carry-forward from
  finding-2026-05-12-FLASH-0001
- Rule 3: no PoC / payload extraction
- Rule 6: no >15-word quotes
- Rule 7: copyright discipline preserved
- Rule 8: Splunk first-party silence on TeamPCP IOC superset continues

## TLP marking

TLP:CLEAR — public news source (BleepingComputer) relaying public vendor
disclosure (Grafana Labs); no first-party telemetry content; no PII; no
credentials.
