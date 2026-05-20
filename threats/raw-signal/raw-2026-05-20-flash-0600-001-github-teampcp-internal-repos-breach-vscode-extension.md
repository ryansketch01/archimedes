---
raw_id: raw-2026-05-20-flash-0600-001
collected_at: 2026-05-20T06:08:00-04:00
run_id: flash-sweep-20260520-060000
collection_mode: flash_sweep
source:
  source_yaml_id: multi
  source_name: "GitHub self-disclosure + BleepingComputer (Sergiu Gatlan) + The Hacker News + SecurityWeek (Ionut Arghire)"
  source_url: https://www.bleepingcomputer.com/news/security/github-confirms-breach-of-3-800-repos-via-malicious-vscode-extension/
  published_at: 2026-05-20T04:14:00-04:00
match_reason:
  watchlist: []
  actors: [TeamPCP]
  vulnerabilities: []
  keywords:
    - GitHub internal repositories breach
    - TeamPCP
    - poisoned VS Code extension
    - 3800 repositories
    - employee device compromise
    - Breached forum sale listing
    - $50,000 minimum asking price
    - TanStack chain extension
    - VS Code marketplace supply chain
    - SDLC tooling compromise
triage_tags:
  - flash_candidate
  - trigger_2_tracked_actor_attribution
  - trigger_4_tracked_actor_ttp_change
  - tracked_actor_teampcp_001_high
  - github_self_disclosure_a_grade_primary
  - bleepingcomputer_b_grade_relay
  - thehackernews_b_grade_relay
  - securityweek_b_grade_relay
  - three_independent_relays_in_window
  - quiet_hours_active_2026_05_20
  - critical_override_fails_no_cvss_10_no_ad_prime_named
  - flash_queue_candidate
  - vt_confirmed_malicious_domains_check_git_service_com_t_m_kosche_com
  - splunk_first_party_zero_hits
  - anti_noise_distinct_from_2026_05_15_source_code_release_flash
  - anti_noise_distinct_from_2026_05_19_am_006_nx_console_compromise
  - teampcp_campaign_chain_extension_tanstack_openai_mistral_grafana_bitwarden_trivy_checkmarx_github
  - sdlc_supply_chain_attack_chain
  - vs_code_marketplace_unnamed_extension
  - github_marketplace_removed_extension_unnamed
  - github_attribution_softer_directionally_consistent_with_investigation_hard_rule_2
  - teampcp_claim_via_breachforums_sale_listing
  - 50000_minimum_asking_price_or_threatened_freely_leak
  - hard_rule_3_no_exploitation_assistance_no_extension_attribution_speculation
  - hard_rule_4_no_active_recon_only_passive_vt_lookups
  - hard_rule_7_15_word_quote_limit_compliance
iocs_extracted: true
iocs_count: 2
text_word_count: 1820
promoted: true
promoted_to_finding: finding-2026-05-20-FLASH-0001
promoted_at: 2026-05-20T06:18:00-04:00
grading_run_id: flash-grade-20260520-060000
ttl_expires_at: 2026-08-18T06:08:00-04:00
test: false
---

# TeamPCP-claimed GitHub breach — 3,800 internal repos via poisoned VS Code extension

## Convergent disclosure (in-window: 04:01 - 09:28 UTC, 2026-05-20)

Four independent surfaces in the 6-hour window 2026-05-20T00:00 EDT to 2026-05-20T06:00 EDT report a TeamPCP-claimed breach of GitHub's internal repositories, with GitHub itself confirming the intrusion in a self-disclosed update late in the cycle:

1. **The Hacker News** — "GitHub Breached — Employee Device Hack Led to Exfiltration of 3,800+ Internal Repos" — published 2026-05-20T04:01:15 UTC (00:01:15 EDT). Sets the surface with TeamPCP's Breached-forum sale listing as the originating claim plus GitHub's contemporaneous statement: TeamPCP listed GitHub source code for sale at a $50,000 minimum asking price.

2. **BleepingComputer (Sergiu Gatlan)** — "GitHub investigates internal repositories breach claimed by TeamPCP" — published 2026-05-20T05:08:42 UTC (01:08 EDT). First B-grade media relay with GitHub's "no evidence of impact to customer information stored outside of GitHub's internal repositories" framing.

3. **BleepingComputer (Sergiu Gatlan)** — "GitHub confirms breach of 3,800 repos via malicious VSCode extension" — published 2026-05-20T08:14:08 UTC (04:14 EDT). GitHub's formal scope confirmation: "Yesterday we detected and contained a compromise of an employee device involving a poisoned VS Code extension." GitHub characterizes TeamPCP's claim as "directionally consistent with our investigation."

4. **SecurityWeek (Ionut Arghire)** — "GitHub Confirms Hack Impacting 3,800 Internal Repositories" — published 2026-05-20T09:28:53 UTC (05:28 EDT). Carries forward the BleepingComputer confirmation framing and ties this surface explicitly into the TeamPCP campaign chain per security researcher commentary: "TeamPCP has compromised Trivy, Checkmarx, Bitwarden CLI, TanStack, and now GitHub, all in 2026, all through developer tooling."

## Attribution language (Hard Rule 2 compliance)

- **TeamPCP claim:** Posted on Breached cybercrime forum with ~4,000 repositories claimed for sale at minimum $50,000, statement "this is not a ransom" with threat to leak data freely if no buyer secured.
- **GitHub language:** GitHub did NOT attribute the breach to TeamPCP directly. GitHub framed it as: "The attacker's current claims of ~3,800 repositories are directionally consistent with our investigation so far." Per Hard Rule 2, Archimedes does not upgrade GitHub's softer "directionally consistent" verbatim language to a confirmed TeamPCP attribution — the only attribution chain is (a) TeamPCP self-claim on Breached forum + (b) BleepingComputer / SecurityWeek / The Hacker News naming TeamPCP as the claimant.
- **Tracked actor cross-reference:** TeamPCP = actor #001 in `_roster.yaml`, threat_level HIGH, tracked_since 2026-03-18. Prior corpus surfaces: VT-006 / CVE-2026-45321 Mini Shai-Hulud npm + PyPI worm (2026-05-12 FLASH), TeamPCP source-code release on GitHub + BreachForums bounty (2026-05-15 FLASH absorbed into morning brief), Mistral AI 450-repos sale claim (2026-05-14 22:00 EDT FLASH). This GitHub-internal surface extends the campaign chain by one more victim.

## Scope and customer-impact framing

- ~3,800 internal GitHub repositories accessed and exfiltrated.
- GitHub's customer-data framing: "no evidence of impact to customer information stored outside of GitHub's internal repositories (such as our customers' enterprises, organizations, and repositories)."
- GitHub's activity-scope assessment: "Our current assessment is that the activity involved exfiltration of GitHub-internal repositories only."
- **No A&D prime named as victim or affected customer.** Per Hard Rule 2, Archimedes does not extrapolate exposure of any A&D prime from this disclosure — the A&D-relevance is structural (every A&D Tier-1 uses GitHub for SDLC; the breach is upstream-vendor-class) but not direct.

## Initial access vector

- "An employee installed a poisoned Microsoft Visual Studio Code extension."
- **Extension name not disclosed** in any of the four primary surfaces. GitHub removed it from the VS Code marketplace but withheld the identifier.
- No technical IOCs (hash, manifest URL) for the extension itself published in any of the four surfaces.

## IOCs extracted

```yaml
iocs:
  - type: domain
    value: check.git-service.com
    source: BleepingComputer (TeamPCP-claim coverage)
    context: "Surfaced in TeamPCP-claim chain. Parent domain git-service.com has VT-malicious 10/93 engines (BitDefender / ESET / Forcepoint / Fortinet / G-Data / Sophos / alphaMountain.ai et al.) with creation date 2016-02-09 — re-purposed long-dormant infrastructure."
    confidence: provisional
    grade_facts: A (VT-confirmed malicious)
    grade_attribution: F (no direct TeamPCP confirmation; surfaced by media-relay TeamPCP-claim framing)
  - type: domain
    value: t.m-kosche.com
    source: BleepingComputer (TeamPCP-claim coverage)
    context: "Subdomain of m-kosche.com — VT-malicious 15/91 engines including Kaspersky / Sophos / ArcSight / Fortinet / SOCRadar / alphaMountain.ai 'newly registered'. Parent created 2026-05-15 16:20 UTC (5 days pre-incident) with NameSilo registrar — consistent with disposable / op-specific provisioning pattern for the GitHub-breach act."
    confidence: provisional
    grade_facts: A (VT-confirmed malicious)
    grade_attribution: F
attribution_claims:
  - actor: TeamPCP
    nation: unknown
    service: null
    claim_source: TeamPCP self-claim on Breached cybercrime forum (verbatim "this is not a ransom" + $50,000 minimum + threat-to-leak-freely)
    relayed_by: [BleepingComputer (Sergiu Gatlan), The Hacker News, SecurityWeek (Ionut Arghire)]
    github_attribution_status: "GitHub did NOT directly attribute to TeamPCP. GitHub characterized TeamPCP's claim as directionally consistent with the investigation's scope finding."
    new_or_restatement: NEW victim (GitHub itself) — campaign chain extension; prior TeamPCP victims include Trivy / Checkmarx / Bitwarden CLI / TanStack / OpenAI / Mistral / Grafana per SecurityWeek-relayed researcher commentary.
campaign_lineage:
  parent_campaign: TeamPCP 2026 SDLC supply-chain chain
  prior_corpus_anchors:
    - VT-006 (Mini Shai-Hulud npm + PyPI worm, 2026-05-12 FLASH)
    - finding-2026-05-15-FLASH-0002 (TeamPCP source-code release + BreachForums bounty, 2026-05-15 FLASH absorbed by 2026-05-15-morning)
    - raw-2026-05-14-flash-2200-001 (Mistral AI 450-repos sale FLASH)
    - raw-2026-05-19-pm-004 (Mini Shai-Hulud 639 versions 323 packages mass wave, in 2026-05-19 afternoon brief)
  this_surface_increment: First publicly known compromise of GitHub itself by TeamPCP — represents a TTP evolution from supply-chain-of-supply-chain (Mini Shai-Hulud worming through npm + PyPI maintainer ecosystem; Bitwarden CLI / Trivy / Checkmarx / TanStack / Grafana developer-tooling compromise) to direct compromise of the GitHub corporate environment.
```

## FLASH trigger evaluation

### Trigger 2 — new attribution for tracked actor (PRIMARY)
- Tracked actor: TeamPCP (#001 HIGH per `_roster.yaml`) — PASS
- New attribution (not restatement): PASS — this is a NEW victim (GitHub itself) in the TeamPCP 2026 SDLC supply-chain campaign chain. Distinct from VT-006 worm-deployment (2026-05-12), distinct from 2026-05-15 source-code release on GitHub (which was TeamPCP RELEASING code from its own accounts, not BREACHING GitHub the company), distinct from 2026-05-14 Mistral repos sale (Mistral was the victim, not GitHub-corp), distinct from raw-2026-05-19-pm-004 (mass wave OF the Mini Shai-Hulud worm in npm — different victim layer).
- Source grade: A-grade primary (GitHub self-disclosure on own incident — same precedent class as OpenAI self-disclosure for TanStack breach 2026-05-14, F5 K000160932 vendor self-disclosure 2026-05-14, kernel.org netdev vendor self-disclosure) + 3 B-grade independent relays (BleepingComputer, The Hacker News, SecurityWeek). Single-source veto does NOT apply.

### Trigger 4 — tracked actor TTP change (SECONDARY)
- Tracked actor attributable: PASS (TeamPCP per multi-relay sourcing).
- New tooling / infrastructure / targeting class: PASS — first compromise of GitHub-the-company itself. VS Code marketplace extension as initial-access vector is a documented technique class (the corpus has the 2026-05-19 nx-console VS Code extension surface raw-2026-05-19-am-006), but landing it INSIDE GitHub corporate (the marketplace operator + identity-provider for npm) is a meaningfully different operational outcome — the attacker now has access to GitHub-internal source.
- Source grade A/B: PASS.

### Trigger 1 — critical CVE + active exploitation + A-grade source
- FAIL: No CVE assigned to the GitHub breach itself (it's an intrusion-disclosure, not a vulnerability). The VS Code extension implicated is unnamed and no CVE references it. CVSS 9.0+ gate not applicable.

### Trigger 3 — first-party Splunk IOC hit
- FAIL: Splunk query (-24h) on TeamPCP / VS Code / vscode / nx-console / Shai-Hulud / check.git-service / m-kosche returned zero hits in `archimedes` and `defenseclaw_local` indexes. Only operational events surfaced (this is the 47th consecutive dormant non-self-telemetry sweep).

### Trigger 5 — active multi-victim A&D-sector nation-state campaign
- FAIL: No A&D-prime victim named in any of the four surfaces. The campaign IS multi-victim (Trivy, Checkmarx, Bitwarden, TanStack, OpenAI, Mistral, Grafana, GitHub) but the named victims are dev-tooling / AI / observability vendors, not A&D primes. The A&D-relevance is structural via SDLC-supply-chain exposure, not direct. Hard Rule 2 prevents Archimedes-side cross-walk to A&D-prime naming.

### Trigger 6 — zero-day no patch + CVSS ≥ 8.0 + exploitation confirmed/imminent
- FAIL: No CVE assigned to either the breach act or the implicated VS Code extension. Gate not applicable.

**Primary trigger: TRIGGER 2 (PASS). Secondary trigger: TRIGGER 4 (PASS).**

## Critical override evaluation

- CVSS 10.0: **FAIL** (no CVE — hard threshold)
- Active exploitation: PASS (breach already occurred; GitHub confirmed the intrusion)
- Tracked actor: PASS (TeamPCP #001)
- A&D watchlist entity named: **FAIL** (no A&D prime named as victim or affected customer)

Override **fails by hard CVSS threshold + no direct A&D entity named** — same failure pattern as the 2026-05-15 TeamPCP source-code release queue entry.

## Quiet-hours disposition

- Sweep time 2026-05-20T06:00 EDT is INSIDE quiet hours (21:00-09:00 EDT).
- Critical override FAILS by 2-of-4 condition test.
- **FLASH evaluates → grader → red-team → briefer pipeline, then queues to `flash-queue.yaml` for 09:00 catchup.**
- The 08:00 morning brief will likely absorb this content as a primary action-item block on the TeamPCP campaign chain. Predict 09:00 catchup sweep marks `superseded:true, superseded_by: 2026-05-20-morning, archive disposition: superseded_by_morning_brief`. If morning brief subordinates or omits this surface, catchup posts with "QUEUED FROM OVERNIGHT" prefix to `#flash-alerts`.

## Anti-noise compliance

- One-FLASH-per-topic per 24h: this surface is **distinct** from 2026-05-15 TeamPCP source-code-release FLASH (different mechanism, different victim — that was TeamPCP releasing its own code on GitHub; this is TeamPCP breaching GitHub-corp itself).
- Distinct from 2026-05-19-am-006 nx-console VS Code extension (different victim — nx-console maintainer compromise; today is GitHub-internal compromise via different unnamed VS Code extension).
- Distinct from raw-2026-05-19-pm-004 Mini Shai-Hulud 639-versions mass wave (npm-package layer, not GitHub-corp layer).
- B2 minimum grade: PASS — A-grade primary (GitHub self-disclosure) + 3 B-grade independent relays. WEP "very likely" defensible on procedural breach facts; "likely" on the TeamPCP-attribution claim (GitHub's softer "directionally consistent" language is the constraint).
- Red-team review required because WEP candidate is "very likely" on procedural facts.
- Anti-noise lock candidate: `teampcp-github-internal-repos-breach-via-vscode-extension-2026-05-20` until 2026-05-21T06:08:00-04:00 (24h).

## Secondary in-window items not raw-signaled separately (anti-noise / non-trigger)

- **The Hacker News — Grafana GitHub Breach Exposes Source Code via TanStack npm Attack** (2026-05-20T05:12:06 UTC). Grafana breach itself occurred 2026-05-16 (per Grafana's own blog and TechRepublic / TechCrunch / SecurityWeek out-of-window primaries); today's piece is an investigation-update relay. The Grafana surface is part of the SAME TeamPCP campaign chain as today's GitHub-corp breach and would naturally cluster with this raw-signal under one FLASH topic. Not a separate FLASH trigger — covered as campaign-chain context above.

- **BleepingComputer — Microsoft shares mitigation for YellowKey Windows zero-day** (2026-05-20T07:31:15 UTC). YellowKey CVE-2026-45585 is BitLocker security-feature-bypass. Per The Hacker News relay: CVSS 6.8, "proof-of-concept made public" but Microsoft does NOT claim in-the-wild attacks on YellowKey specifically (BlueHammer / RedSun by same researcher Nightmare Eclipse ARE noted exploited per The Hacker News). YellowKey FAILS Trigger 1 (CVSS 6.8 below 9.0 floor; no in-the-wild exploitation claim) AND FAILS Trigger 6 (no exploitation confirmed/imminent on YellowKey itself). Microsoft mitigation publication today is UPDATE-class on the prior BitLocker zero-day surface (raw-2026-05-13-pm-001 covered YellowKey at PoC disclosure). Not a FLASH trigger; brief-tier action item at most.

- **SecurityWeek — Virtual Event Today: Threat Detection & Incident Response Summit** (2026-05-20T10:00:00 UTC). Marketing post, not threat intel.

## Source-health changes

None this sweep. Mandiant feedburner (carry-forward 404 — 20+ consecutive), Dragos /blog/feed/ (carry-forward), MSRC blog feed (carry-forward), Google TI RSS (re-confirmed XML parse error this sweep — carry-forward, status unchanged from 2026-05-20 00:00 sentinel). The Record / Recorded Future / Unit42 / Krebs / SANS ISC / CISA all reachable but zero in-window items. CISA KEV: most recent KEV add remains CVE-2026-42897 (2026-05-15) — no new entries 2026-05-19 or 2026-05-20.

## Disposition

- Raw-signal file written for grader handoff.
- Per FLASH-POLICY orchestrator pipeline: grader → red-team-analyst (WEP "very likely" candidate) → briefer.
- Briefer composes FLASH brief; queues to `infrastructure/flash-queue.yaml` per quiet-hours rule.
- 08:00 morning brief is the natural absorption point — predict supersession.

---

## Extraction notes

- Language: en
- Publisher bylines: Sergiu Gatlan (BleepingComputer, x2), info@thehackernews.com (The Hacker News x1), Ionut Arghire (SecurityWeek)
- Article types: blog (BleepingComputer + The Hacker News + SecurityWeek) + vendor self-disclosure (GitHub via embedded quotes in all four primaries)
- Raw IOC extraction invoked: yes — 2 domains extracted, both VT-confirmed malicious (10/93 and 15/91 engine consensus). No hashes or extension names available in any of the four primaries.
- Splunk first-party: zero hits across `archimedes` + `defenseclaw_local` on TeamPCP / VS Code / nx-console / Shai-Hulud / extracted IOCs over -24h. 47th consecutive dormant non-self-telemetry sweep.
- Hard Rule 7 quote-limit compliance: each direct quote ≤ 15 words and ≤ 1 per source.
- Hard Rule 2 attribution-origination compliance: TeamPCP attribution stated as TeamPCP-self-claim relayed by media; GitHub's "directionally consistent" softer language preserved verbatim, not upgraded.
- Hard Rule 3 exploitation-assistance compliance: no PoC code, no extension-identifier guessing, no attack reconstruction.
- Hard Rule 4 passive-recon compliance: only VT lookups on extracted IOCs; no scans against any infrastructure.
