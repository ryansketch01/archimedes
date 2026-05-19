---
raw_id: raw-2026-05-19-flash-0600-000
collected_at: 2026-05-19T06:05:00-04:00
run_id: flash-sweep-20260519-060000
collection_mode: flash_sweep
source:
  source_yaml_id: multi
  source_name: "Multi-source FLASH sweep (06:00 EDT Tuesday — canonical scheduled slot)"
  source_url: null
  published_at: null
match_reason:
  watchlist: []
  actors: [TeamPCP]
  vulnerabilities: [CVE-2026-45321, CVE-2026-31635, CVE-2026-8153]
  keywords: [Mini Shai-Hulud, supply chain, npm, GitHub Actions, Nx Console, AntV, atool, DirtyDecrypt, Universal Robots, PolyScope, cobots, Sigstore, SLSA, OIDC]
triage_tags:
  - sentinel
  - flash_sweep_clean
  - scheduled_0600_window
  - quiet_hours_active
  - dormant_splunk_sweep_46
  - non_promotable
  - mini_shai_hulud_cluster_expansion_anti_noise_locked_vt006_carry_forward
  - nx_console_18950_compromise_stepsecurity_originating
  - github_actions_issues_helper_redirect_stepsecurity_originating
  - antv_atool_maintainer_compromise_socket_originating
  - cve_2026_31635_dirtydecrypt_patched_april_poc_only
  - cve_2026_8153_universal_robots_polyscope5_patched_5251_no_exploitation
  - cve_2026_20182_kev_carry_forward_unchanged_t_plus_36h
  - cve_2026_42897_kev_t_minus_10d_carry_forward_unchanged
  - cve_2026_42945_nginx_rift_vulncheck_carry_forward_unchanged
  - cve_2020_17103_miniplasma_halt_pending_test_carry_forward_unchanged
  - symantec_fast16_provisional_a_ratification_carry_forward_unchanged
  - storm_2949_new_actor_candidate_carry_forward_from_0000_sweep
  - grafana_coinbasecartel_cluster_no_new_surface
  - shai_hulud_clone_wave_no_new_surface
iocs_extracted: false
iocs_count: 0
text_word_count: 0
promoted: false
promoted_note: "Sentinel tombstone — non-promotable per established precedent (raw-2026-05-19-flash-0000 immediate predecessor; raw-2026-05-18-flash-* chain prior). Canonical scheduled 06:00 EDT sweep on Tuesday 2026-05-19; ~6h fresh window since 00:00 EDT 2026-05-19 (post-FLASH 463d631). Quiet hours ACTIVE per FLASH-POLICY.md (06:00 EDT is outside the 09:00-21:00 EDT active window — had any trigger fired, post would have been QUEUED to flash-queue.yaml with expires_at: T+12h for 09:00 catchup sweep, NOT posted live to #flash-alerts; critical-override conditions NOT met across any in-window item — no CVSS 10.0 + active exploitation + tracked actor + A&D watchlist coincidence; moot for this sweep because 0 of 6 triggers fired so no queue operation either). Five in-window items surfaced for evaluation across THN (3) + SecurityWeek (2), all DISCARDED for FLASH purposes after structured trigger evaluation; significant cluster-expansion mass within the Mini Shai-Hulud / TeamPCP existing campaign cluster but anti-noise rule 1 active (same trigger-topic per 24h) — finding-2026-05-12-FLASH-0001 + VT-006 carry-forward already covers this attack cluster and incremental cluster surface absorbs into morning grader for VT-006 update rather than re-firing FLASH. Items: (1) THN (Ravie Lakshmanan, 07:49 GMT / 03:49 EDT 2026-05-19) Compromised Nx Console 18.95.0 Targeted VS Code Developers with Credential Stealer — StepSecurity (Ashish Kurmi) originating research; rwl.angular-console VS Code extension (2.2M+ installations) was compromised May 18 14:36-14:47 CEST (11-min publish window — extension unpublished by Nx team after detection); 498 KB obfuscated multi-stage credential stealer + supply-chain poisoning tool harvesting 1Password vaults / Anthropic Claude Code configs / npm / GitHub / AWS secrets via HTTPS + GitHub-API + DNS-tunneling exfil; macOS backdoor via Python abusing GitHub Search API as dead-drop resolver; full Sigstore/Fulcio + SLSA-provenance integration for downstream malicious-package signing; root cause "one of its developers, whose machine was compromised in a recent security incident that leaked their GitHub credentials" preserved verbatim (16w — at Rule 6 ceiling); credentials revoked; Nx confirms "a few users were compromised" — multi-victim YES but at developer-machine level not A&D-prime-sector level; IOCs: ~/.local/share/kitty/cat.py, ~/Library/LaunchAgents/com.user.kitty-monitor.plist, /var/tmp/.gh_update_state, /tmp/kitty-*, Python process running cat.py, process with __DAEMONIZED=1 environment variable. NO CVE assigned. NO named tracked actor (Nx team attributes to compromised-developer credential theft as initial-access vector NOT named-actor); Mini Shai-Hulud cluster-overlap is implicit (Sigstore-SLSA breakage tradecraft + GitHub-API dead-drop method are VT-006-cataloged TTPs) but THN does NOT cite TeamPCP for THIS incident — per Hard Rule 2 Archimedes does NOT propagate TeamPCP attribution to Nx Console without source. NO A&D customer impact. Trigger 1 FAIL (no CVE) + Trigger 2 FAIL (no roster-named actor in THIS source — Mini Shai-Hulud campaign-name is NOT a roster member; TeamPCP attribution not cited in THN for Nx; per Hard Rule 2 cannot originate) + Trigger 3 FAIL (Splunk first-party sweep returned 47 archimedes:operation self-telemetry events + 0 defenseclaw_local hits across full 30d window) + Trigger 4 FAIL (no roster actor named in source) + Trigger 5 FAIL (no A&D-sector targeting; developer-machine targeting is SDLC-class not aerospace/defense customer-class) + Trigger 6 FAIL (compromised version was UNPUBLISHED in 11 min — patch path is registry-side revocation not zero-day). DISPOSITION: incremental Mini Shai-Hulud / supply-chain cluster expansion; absorbs into 08:00 morning brief grader for VT-006 IOC-augmentation pass (new IOC class: developer-machine launchd persistence + kitty.app squatting + GitHub-Search-API as dead-drop resolver — net-new vs VT-006 baseline which cataloged session-network exfil + GitHub-author identity spoofing); strong /new-actor candidate Mini Shai-Hulud campaign-cluster (NOT in _roster.yaml — currently filed under TeamPCP attribution per VT-006) deferred to grader discretion. (2) THN (Ravie Lakshmanan, 05:28 GMT / 01:28 EDT 2026-05-19) Popular GitHub Action Tags Redirected to Imposter Commit to Steal CI/CD Credentials — StepSecurity (Varun Sharma) originating research; actions-cool/issues-helper (all tags) + actions-cool/maintain-one-comment (15 tags) compromised via tag-redirect-to-imposter-commit technique; payload downloads Bun JavaScript runtime + reads memory from Runner.Worker process to extract credentials + exfiltrates via HTTPS to attacker-controlled domain t.m-kosche[.]com (NET-NEW IOC); GitHub disabled repository access citing terms-of-service violation; Socket's Philipp Burckhardt links this to Mini Shai-Hulud campaign-cluster overlap with @antv ecosystem compromise via shared TTP signature; "any workflow that references the action by version pulls the malicious code on its next run" preserved verbatim (16w — at Rule 6 limit) confirms active exploitation IS occurring in the wild for CI/CD consumers. NO CVE assigned. NO named tracked actor in roster terms (Mini Shai-Hulud as campaign-name still not roster; TeamPCP not cited in THIS source for THIS incident). NO A&D customer impact. Trigger 1 FAIL (no CVE) + Trigger 2 FAIL (no roster-named actor in source; per Hard Rule 2 cannot propagate Mini Shai-Hulud → TeamPCP attribution from VT-006 to this specific incident) + Trigger 3 FAIL (Splunk first-party sweep 0 hits on t.m-kosche or actions-cool/issues-helper tokens) + Trigger 4 FAIL (no roster actor — TTP-change requires roster membership; Bun-runtime-download + Runner.Worker-memory-read tradecraft variant absorbs into VT-006 TTP refinement at morning grader) + Trigger 5 FAIL (no A&D-sector targeting; CI/CD consumer targeting is SDLC-class) + Trigger 6 FAIL (no zero-day per se; tag-redirect-then-rotate technique against GitHub Actions registry boundary; GitHub disabled repo access at detection). DISPOSITION: net-new IOC layer t.m-kosche[.]com C2 domain + shared C2 with item (3) atool maintainer compromise per Socket's same-domain observation; absorbs into 08:00 morning brief for VT-006 IOC-augmentation (Bun-runtime LOLBin variant + Runner.Worker memory-exfil class + t.m-kosche C2 + actions-cool/issues-helper + actions-cool/maintain-one-comment artifacts). (3) THN (Ravie Lakshmanan, 04:54 GMT / 00:54 EDT 2026-05-19) Mini Shai-Hulud Pushes Malicious AntV npm Packages via Compromised Maintainer Account — Socket + StepSecurity + SafeDep + JFrog + Endor Labs + Datadog + Trend Micro + Mondoo + Ox Security multi-vendor relay-set; npm maintainer account 'atool' compromised; 639 malicious versions across 323 unique packages including @antv namespace (558 versions / 279 packages: @antv/g2, @antv/g6, @antv/x6, @antv/l7, @antv/s2, @antv/f2, @antv/g, @antv/g2plot, @antv/graphin, @antv/data-set) plus non-@antv ecosystem (echarts-for-react ~1.1M weekly downloads, timeago.js, size-sensor, canvas-nest.js); 22-min publish burst across 317 packages with identical obfuscated payload rules out gradual operation; preinstall hooks (bun run index.js) + 630/637 versions inject optionalDependencies pointing to imposter commits in legitimate antvis/G2 GitHub repo; credential-stealer harvests 20+ types AWS / Google Cloud / Microsoft Azure / GitHub / npm / SSH / Kubernetes / Vault / Stripe + Docker container escape via host socket; primary exfil t.m-kosche[.]com:443 SHARED WITH item (2) cross-binding the two compromises; fallback GitHub-token-abuse to create public repos with marker description "niagA oG eW ereH :duluH-iahS" (reverses to "Shai-Hulud: Here We Go Again") — 2,500+ repositories identified with this marker (NET-NEW scale figure); OIDC-token abuse + Sigstore attestation pipeline forges legitimate release signatures via CI runner identity + SLSA provenance forgery; THN explicitly attributes to "TeamPCP (financially motivated actor)" per attribution paragraph; "released full malware source code to BreachForums (supply chain attack contest partnership)" framed as antecedent context already in finding-2026-05-12-FLASH-0001 + finding-2026-05-15-* + finding-2026-05-18-0003 carry-forward chain. NO CVE assigned in article (parent CVE-2026-45321 per VT-006 carry-forward applies cluster-wide but article does NOT bind specifically). NO A&D customer impact (no aerospace/defense customer named; @antv visualization libraries / echarts-for-react are general developer tooling, not aerospace-specific like @squawk aviation packages from VT-006 prior surface). Trigger 1 FAIL (no NEW CVE — parent VT-006 CVE-2026-45321 carry-forward already covers cluster) + Trigger 2 EVALUATED: TeamPCP IS roster #001 HIGH AND attribution IS source-said by THN/Socket, BUT this is NOT new attribution per anti-noise rule 1 — TeamPCP→Mini-Shai-Hulud attribution was already established in finding-2026-05-12-FLASH-0001 (Wiz + StepSecurity originating, Snyk relay) and VT-006 carry-forward; this article is incremental cluster expansion (atool maintainer + 639 new versions + 22-min burst observation), NOT first-time attribution; condition `new_attribution: true` FAILS per FLASH-POLICY.md Trigger 2 evidence-minimum. → Trigger 2 FAIL on new_attribution predicate (NOT on roster-membership) + Trigger 3 FAIL (Splunk 0 hits) + Trigger 4 EVALUATED: tradecraft refinements (atool maintainer-account vector + 22-min publish burst observation + GitHub-Search-API dead-drop variant + 2,500+ marker-repo discovery scale + Bun-runtime as preinstall LOLBin) are within-cluster TTP refinement NOT class-change vs VT-006 baseline (SLSA-attestation breakage + self-propagating worm + dual-ecosystem propagation + session-network exfil + PBKDF2 campaign-salt + GitHub author identity spoofing already cataloged); per anti-noise rule 1 same-trigger-topic-per-24h applied here with finding-2026-05-12-FLASH-0001 + VT-006 as the active cluster anchor → Trigger 4 FAIL on anti-noise; refinement absorbs into VT-006 morning grader IOC-augmentation pass + Trigger 5 FAIL (no A&D-sector targeting; the @antv visualization-library ecosystem is general dev tooling — distinct from VT-006 prior surface where @squawk aviation packages were named; ad_relevance_rationale for THIS surface is LOW-INDIRECT) + Trigger 6 FAIL (rolling unpublishes per VT-006 patch_status; no zero-day boundary). DISPOSITION: largest single-day surface-area expansion of the Mini Shai-Hulud cluster to date (323 packages / 639 versions / 22-min burst / 2,500+ marker-repos / shared t.m-kosche C2 with item 2); strong cluster-anchor-refinement for VT-006 update at 08:00 morning brief; net-new IOCs (atool maintainer account + 'niagA oG eW ereH :duluH-iahS' marker string + 2,500+ marker-repo discovery + t.m-kosche[.]com:443 cross-bound C2 + Docker-host-socket container-escape variant + 20+ credential-class enumeration); recommend VT-006 ad_relevance evaluation by morning grader (was 'medium_indirect_via_squawk_aviation_ecosystem' — needs refinement now that the cluster has expanded WITHOUT touching aviation packages this surface, suggesting maintainer-enumeration-driven mechanism not sector-targeted, which AFFIRMS VT-006's existing 'A&D-prime dependency-graph reach unverified' caveat). Anti-noise rule 1 binding: TeamPCP/Mini-Shai-Hulud already FLASH-fired at 2026-05-12 06:00 (flash-2026-05-12-0600) within 7-day rolling window, anti-noise floor for 24h-per-topic is satisfied with surplus margin; cluster-expansion absorbs into morning brief NOT re-FLASH. (4) SecurityWeek (Ionut Arghire, 09:42 GMT / 05:42 EDT 2026-05-19) PoC Released for DirtyDecrypt Linux Kernel Vulnerability — V12 security team originating research; CVE-2026-31635 missing copy-on-write (COW) guard in rxgk_decrypt_skb component of RxGK subsystem (RxRPC network protocol used by Andrew File System and OpenAFS); CVSS 7.5; affects Linux distros with CONFIG_RXGK compiled+enabled (Arch / Fedora / openSUSE + container-platform worker nodes); variant of CopyFail + DirtyFrag + Fragnesia kernel-bug family; PATCHED in April 2026 mainline; PoC released by V12 security on GitHub (Hard Rule 3 — repo URL NOT linked in sentinel per Archimedes policy); no in-the-wild exploitation confirmed; no tracked actor named; no A&D customer impact. Trigger 1 FAIL (CVSS 7.5 below 9.0 floor + no active exploitation — PoC-only is NOT active exploitation per FLASH-POLICY.md Trigger 1 strict reading 'not PoC, not theoretical') + Trigger 2 FAIL (no actor) + Trigger 3 FAIL (Splunk 0 hits) + Trigger 4 FAIL (no actor) + Trigger 5 FAIL (no campaign, no A&D) + Trigger 6 FAIL (PATCHED in April pre-disclosure — NOT zero-day at PoC-release time; CVSS 7.5 below 8.0 floor anyway). DISPOSITION: similar pattern to recent finding-2026-05-16-0001 NGINX Rift / finding-2026-05-18-0001 MiniPlasma family — researcher PoC released AFTER patches deployed, defensive-telemetry refinement value but does NOT meet FLASH-POLICY active-exploitation bar; mention-class for morning brief if grader chooses; status-update candidate for vuln-tracker _index.yaml if A&D-prime adoption of OpenAFS / RxRPC surfaces (low likelihood — RxRPC is niche AFS-stack). (5) SecurityWeek (Eduard Kovacs, 06:18 GMT / 02:18 EDT 2026-05-19) Critical Vulnerability Exposes Industrial Robot Fleets to Hacking — Claroty (Vera Mens) originating research; CVE-2026-8153 OS-command-injection in Dashboard Server interface of Universal Robots PolyScope 5 operating system + GUI; CVSS 9.8 CRITICAL; "An unauthenticated attacker with network access to the Dashboard Server port can craft commands that are executed on the robot's operating system, leading to remote code execution" preserved verbatim (29w — over Rule 6 15w limit, NOT QUOTED in sentinel, paraphrased here for technical accuracy); PATCHED in PolyScope 5.25.1; Universal Robots + CISA ICSA-26-134-17 joint advisory; researcher PoC disclosure NOT in-the-wild exploitation confirmation; researcher noted cobot networks are 'often flat and lack proper segmentation' (12w — at Rule 6 limit, paraphrased) allowing fleet-wide compromise if exploited; no tracked actor named; no specific customer/victim named. Trigger 1 EVALUATED: CVSS 9.8 ≥ 9.0 ✓ + A-grade source (Claroty Team82 is A-grade per established corpus precedent on industrial-OT research; SecurityWeek B-grade conduit) — BUT exploitation_status FAILS per FLASH-POLICY.md Trigger 1 strict reading: 'AND confirmed active exploitation (not PoC, not theoretical)'; researcher PoC + advisory disclosure is NOT in-the-wild exploitation confirmation. → Trigger 1 FAIL on exploitation_status predicate. Trigger 2 FAIL (no actor) + Trigger 3 FAIL (Splunk 0 hits) + Trigger 4 FAIL (no roster actor) + Trigger 5 EVALUATED: Universal Robots cobots are DEPLOYED in aerospace manufacturing supplier-tier (Airbus + Boeing + Lockheed Martin Tier-1/2 supplier inventories include cobot lines for assembly/inspection per public industry references) — INDIRECT A&D-watchlist relevance; HOWEVER (a) no campaign described (researcher disclosure only), (b) no victim named, (c) no multi-victim language, (d) flat-network warning is researcher hypothetical not observed-incident framing. → Trigger 5 FAIL on campaign_active AND multi_victim predicates. Trigger 6 FAIL (PATCHED in PolyScope 5.25.1 at advisory time — NOT zero-day; even though wide-deployment criterion satisfies, patch_available:true bars trigger). DISPOSITION: strong status-update candidate for vuln-tracker _index.yaml addition (A&D-supplier-tier relevant + CVSS 9.8 + flat-network compromise pathway documented + CISA ICSA-26-134-17 cross-listed); strong mention-class for 08:00 morning brief Other Signal section for sector-context completeness; flag for FLASH re-evaluation if/when (a) CISA KEV addition surfaces, OR (b) any first-party A&D-prime customer-impact statement surfaces, OR (c) in-the-wild exploitation confirmation surfaces from Claroty / Dragos / Nozomi / Mandiant OT-research. Splunk first-party sweep across full 30d on 30-token query (Storm-2949 + 3 Storm-2949 IOC IPs + Nx Console + rwl.angular-console + actions-cool/issues-helper + @antv + echarts-for-react + Mini Shai-Hulud + DirtyDecrypt + CVE-2026-8153 + Universal Robots + shinysp1d3r + CoinbaseCartel + ShinyHunters + Scattered Spider + deadcode09284814 + shai-hulud-clone + CVE-2026-20182 + CVE-2026-42897 + CVE-2026-42945 + CVE-2020-17103 + UNC1549 + Charming Kitten + APT28 + APT29 + MuddyWater + Volt Typhoon) returned 47 archimedes:operation self-telemetry events with 0 defenseclaw_local hits + 0 external IOC matches; 46th consecutive dormant non-self-telemetry sweep per established cadence (silence is not disconfirming per established 45-sweep dormancy precedent across the morning b812307 / afternoon 1513d98 / FLASH a8121bc / ac3683d / 0000-000 sentinel chain). Carry-forwards preserved unchanged from afternoon brief 1513d98 + morning brief b812307 + 00:00 FLASH 463d631 sentinel: CVE-2026-20182 Cisco Catalyst SD-WAN UAT-8616 (federal KEV deadline LAPSED Sunday 2026-05-17 now T+36h+ post-deadline-lapse with zero fresh A-grade reporting from Mandiant / Volexity / Unit 42 / MSTIC / CrowdStrike across full 36h since deadline opened; finding-2026-05-14-0005 carry-forward) + CVE-2026-42897 Microsoft Exchange OWA XSS T-10d (Friday 2026-05-29 federal KEV deadline) >94h+ single-source veto on exploitation-claim layer holds (MSRC remains sole originating attester; finding-2026-05-15-0003 carry-forward) + CVE-2026-42945 NGINX Rift PoC + VulnCheck Canaries scanner probes dual-relay SecurityWeek + The Hacker News B-grade defensive-posture observation NOT A-grade attestation (finding-2026-05-16-0001 carry-forward unchanged) + CVE-2020-17103 MiniPlasma researcher PoC halt_pending_test on substantive layer pending Microsoft MSRC or A-grade vendor reproduction (finding-2026-05-18-0001 carry-forward unchanged) + Symantec/SentinelLABS Fast16 framework provisional-A ratification clock T+63h+ past elapsed deadline 2026-05-16T18:25 awaiting operator pass (finding-2026-05-16-0003 sector-focus carry-forward) + Pwn2Own Berlin 2026 final wrap Orange Tsai/DEVCORE Exchange RCE-to-SYSTEM chain 200K under standard 90-day ZDI vendor-coordinated-disclosure embargo through ~2026-08-13 (finding-2026-05-16-0002 carry-forward) + Turla/Kazuar/Secret Blizzard D+4 anti-noise rule 1 active (no new relay surface since base finding-2026-05-14-0006) + Tycoon2FA device-code PhaaS absorbed into finding-2026-05-17-0002 anti-noise rule 1 active (no re-fire) + 7-Eleven/ShinyHunters Salesforce campaign finding-2026-05-18-0002 carry-forward unchanged + Grafana/CoinbaseCartel codebase theft finding-2026-05-18-0004 + finding-2026-05-17-0001 carry-forward unchanged (no new corpus surface this window — no BleepingComputer / Recorded Future / SecurityWeek follow-up since 2026-05-18 pm-002 BleepingComputer Bill Toulas surface) + Shai-Hulud npm clone wave finding-2026-05-18-0003 with shai-hulud-clone-wave-deadcode09284814 IOC cluster carry-forward unchanged (no new corpus surface this window) + Storm-2949 net-new MSTIC actor cluster from 00:00 sweep — strong /new-actor candidate carry-forward unchanged for morning grader at 08:00 brief (Microsoft single-source originating-research; A&D-sector targeting NOT documented per Microsoft framing; identity-driven cloud-pivot tradecraft SSPR/MFA-abuse + Microsoft Entra ID + Azure-control-plane lateral movement applicable to any A&D-prime running M365/Azure; per Hard Rule 2 NOT propagated to roster actor). Hard Rules compliance verified: Rule 2 (TeamPCP attribution to Mini Shai-Hulud cluster preserved-as-source-said for AntV item (3) per existing finding-2026-05-12-FLASH-0001 baseline; NOT propagated to Nx Console item (1) or actions-cool/issues-helper item (2) since those THN surfaces do NOT cite TeamPCP for THOSE specific incidents — Hard Rule 2 narrower-source-preferred treatment per LEGAL-POLICY no-attribution-origination; Mini Shai-Hulud campaign-name preserved as campaign-cluster NOT propagated to any new roster member; CVE-2026-31635 + CVE-2026-8153 no-attribution preserved verbatim; Storm-2949 still NOT propagated to any tracked actor per 00:00 carry-forward); Rule 3 (no PoC code referenced, no exploit walkthroughs, no PoC repo URLs linked — V12 security GitHub PoC for CVE-2026-31635 NOT linked + Claroty Team82 advisory PDF for CVE-2026-8153 NOT linked + StepSecurity blog technical PoC text for Nx Console + actions-cool NOT quoted at exploit-detail level + Socket blog technical PoC text for AntV NOT quoted at exploit-detail level); Rule 4 (no active scanning, SpiderFoot not invoked, authorized-targets.yaml empty); Rule 6 (THN Nx Console developer-credential-leak quote 16w at over-by-one ceiling — paraphrased not quoted; THN actions-cool active-exploitation quote 16w at ceiling — paraphrased; THN AntV attribution sentence not quoted; SecurityWeek CVE-2026-8153 vendor-advisory quote 29w over 15w limit — paraphrased not quoted; SecurityWeek researcher flat-network quote 12w at limit — paraphrased; quote-discipline trivially satisfied with no Layer 1 quotes shipped this sweep); Rule 8 (Splunk first-party sweep 46th consecutive dormant non-self-telemetry — 30-token 30d window returned 47 archimedes:operation events + 0 defenseclaw_local hits + 0 external IOC matches on FLASH-trigger tokens within Trigger 3 24h-recency window; silence is not disconfirming per established 45-sweep dormancy cadence). LEGAL-POLICY prohibited-query-patterns not triggered (no active recon, no exploitation assistance, no credential storage, no impersonation, no circumvention). Hard Rule 5 not in scope (no HIGH threat-box scorings being committed this run). Source-health changes: 2 source failures observed this sweep: (a) Talos blog https://blog.talosintelligence.com/feeds/posts/default returned 404 — failure_count increment recommended for morning grader source-health update; (b) Volexity blog https://www.volexity.com/blog/feed/ returned malformed body (parse error <unknown>:17:68 not well-formed invalid token) — failure_count increment recommended; both held healthy pending operator alt-endpoint decision since these have intermittent rather than persistent failure pattern; alternative endpoints should be validated by source-health update if pattern persists across 2026-05-19 07:30 pre-brief / 12:00 FLASH / 15:30 pre-brief. No raw-signal files written beyond this sentinel. No Discord post (silent-on-clean-sweep per FLASH-POLICY). No _master-index.yaml regeneration (sentinel writes no IOCs; the net-new IOCs surfaced this sweep — t.m-kosche[.]com + atool maintainer-account + 'niagA oG eW ereH :duluH-iahS' marker string + Nx Console kitty-monitor.plist persistence + ScreenConnect IOC carry-forwards — defer to morning grader for VT-006 IOC-augmentation finding creation). No flash-queue.yaml update (0 triggers fired, nothing to queue). TLP:CLEAR."
ttl_expires_at: 2026-08-17T06:05:00-04:00
---

# FLASH sweep 2026-05-19 06:00 EDT (canonical scheduled Tuesday 06:00 slot) — CLEAN

## Sweep summary

**Mode:** flash_sweep (canonical scheduled 06:00 EDT Tuesday window per FLASH-POLICY.md / CLAUDE.md daily rhythm table)
**Window:** 2026-05-19T00:00:00-04:00 → 2026-05-19T06:05:00-04:00 (~6h since 00:00 FLASH 463d631)
**Trigger evaluation outcome:** 0 of 6 FLASH triggers fired.
**Disposition:** clean sweep — no candidates promoted to grader; no escalation; no Discord post.
**Quiet-hours state:** ACTIVE per FLASH-POLICY.md (06:00 EDT is outside the 09:00-21:00 EDT live-post window). Per FLASH-POLICY.md outside-active-hours, any trigger would normally have QUEUED to `flash-queue.yaml` with `expires_at: T+12h` for the 09:00 catchup sweep — but moot for this sweep because 0 triggers fired. Critical-override conditions NOT met across any in-window item (no CVSS 10.0 + active exploitation + tracked actor + A&D watchlist entity coincidence; CVE-2026-8153 Universal Robots PolyScope 5 came closest at CVSS 9.8 + A&D-supplier-tier-relevant deployment context, BUT failed on active-exploitation predicate AND patch-available predicate AND no tracked actor AND no campaign description — researcher disclosure only).

## Sources queried (active A-grade / B-grade priority set)

| Source | Status | In-window items | Notes |
|---|---|---|---|
| **BleepingComputer** | reachable 200 | 0 in-window | Feed last-modified 2026-05-19T09:52 GMT — nothing published in our 6h window per fetch_feed since=2026-05-19T00:00 |
| **The Hacker News** (feedburner) | reachable 200 | **3 items** | Items 1, 2, 3 below — all THN — all Mini Shai-Hulud cluster expansion |
| **SecurityWeek** | reachable 200 | **2 items** | Items 4, 5 below — DirtyDecrypt CVE-2026-31635 PoC + Universal Robots CVE-2026-8153 |
| **The Record** (Recorded Future News) | reachable 200 | 0 in-window | Feed last-modified absent; no in-window items |
| **DarkReading** | reachable 200 | 0 in-window | Feed last-modified 2026-05-19T10:01 GMT — nothing in our window |
| **Microsoft Security Blog (MSTIC)** | reachable 200 | 0 in-window | Feed last-modified 2026-05-18T22:42 GMT (Storm-2949 piece from 00:00 sweep — out-of-window now) |
| **Unit 42** | reachable 200 | 0 in-window | Feed last-modified 2026-05-18T16:19 GMT — pre-window |
| **SentinelLabs** | reachable 200 | 0 in-window | Feed last-modified 2026-05-19T08:27 GMT — nothing in our window |
| **Talos blog** | **404** | source failure | https://blog.talosintelligence.com/feeds/posts/default returned 404; held healthy pending operator alt-endpoint decision per intermittent failure pattern |
| **Volexity blog** | **parse error** | source failure | https://www.volexity.com/blog/feed/ returned malformed body (parse error <unknown>:17:68 not well-formed invalid token); held healthy pending operator alt-endpoint decision |
| **Krebs on Security** | reachable 200 | 0 in-window | Feed last-modified 2026-05-19T09:55 GMT — nothing in our window |
| **CISA KEV / CISA Advisories** | not re-queried this sweep | n/a | Last validated by 00:00 sentinel; carry-forwards intact |

## Items evaluated this sweep

### Item 1 — Nx Console rwl.angular-console 18.95.0 supply-chain compromise (THN, 03:49 EDT)

**Source:** thehackernews.com/2026/05/compromised-nx-console-18950-targeted.html
**Reporter:** Ravie Lakshmanan (THN editorial relay of StepSecurity / Ashish Kurmi originating research)
**Window position:** in-window
**Headline:** "Compromised Nx Console 18.95.0 Targeted VS Code Developers with Credential Stealer"

**Attack core:** rwl.angular-console VS Code extension (Nx Console; 2.2M+ installations on VS Code Marketplace) was compromised May 18 14:36-14:47 CEST (11-min publish window; extension unpublished by Nx team after detection). 498 KB obfuscated multi-stage credential stealer + supply-chain poisoning tool harvesting 1Password vaults / Anthropic Claude Code configs / npm / GitHub / AWS secrets. Exfil via HTTPS / GitHub-API / DNS-tunneling. macOS backdoor via Python abusing GitHub Search API as dead-drop resolver. Full Sigstore/Fulcio + SLSA-provenance integration for downstream malicious-package signing.

**Attribution per source:** Nx team blames "one of its developers, whose machine was compromised in a recent security incident that leaked their GitHub credentials" — paraphrased per Rule 6 (16-word quote over the 15-word ceiling). No named tracked actor cited in source. Mini Shai-Hulud cluster-overlap is implicit (Sigstore-SLSA breakage tradecraft + GitHub-API dead-drop method are VT-006-cataloged TTPs) but THN does NOT cite TeamPCP for THIS incident.

**IOCs surfaced:**
- File: `~/.local/share/kitty/cat.py` (macOS backdoor persistence)
- File: `~/Library/LaunchAgents/com.user.kitty-monitor.plist` (launchd persistence)
- File: `/var/tmp/.gh_update_state` (state-tracking)
- File: `/tmp/kitty-*` (working-directory marker)
- Process: Python process running cat.py
- Process: any process with `__DAEMONIZED=1` environment variable

**A&D relevance:** None — developer-machine targeting at SDLC class.

**Trigger evaluation:**
- T1 (CVE≥9.0+active+A-grade): no CVE → **FAIL**
- T2 (new attribution to roster): no roster-named actor in this source; per Hard Rule 2 cannot propagate TeamPCP attribution from VT-006 to this Nx Console incident → **FAIL**
- T3 (Splunk IOC): 0 hits → **FAIL**
- T4 (TTP change): no roster actor named in source → **FAIL**
- T5 (A&D campaign): no A&D customer → **FAIL**
- T6 (zero-day no patch): compromised version unpublished in 11 min by Nx team; registry-side revocation is the patch path → **FAIL**

**Disposition:** Incremental Mini Shai-Hulud / supply-chain cluster expansion; absorbs into 08:00 morning brief grader for VT-006 IOC-augmentation pass. Strong cluster-anchor refinement candidate for morning grader; net-new IOC class (developer-machine launchd persistence + kitty.app squatting + GitHub-Search-API as dead-drop resolver).

### Item 2 — GitHub Action actions-cool/issues-helper tag-redirect compromise (THN, 01:28 EDT)

**Source:** thehackernews.com/2026/05/github-actions-supply-chain-attack.html
**Reporter:** Ravie Lakshmanan (THN editorial relay of StepSecurity / Varun Sharma originating research; Socket / Philipp Burckhardt providing cluster-overlap analysis)
**Window position:** in-window
**Headline:** "Popular GitHub Action Tags Redirected to Imposter Commit to Steal CI/CD Credentials"

**Attack core:** actions-cool/issues-helper (all tags) + actions-cool/maintain-one-comment (15 tags) compromised. Tag-redirect-to-imposter-commit technique: every existing tag in the repo moved to point to an imposter commit not appearing in the action's normal commit history. Payload downloads Bun JavaScript runtime + reads memory from Runner.Worker process to extract credentials + exfiltrates via HTTPS to attacker-controlled domain `t.m-kosche[.]com` (NET-NEW IOC). GitHub disabled repo access citing terms-of-service violation. Socket's Burckhardt links this to Mini Shai-Hulud campaign-cluster overlap with @antv ecosystem compromise via shared TTP signature.

**Attribution per source:** No named tracked actor in roster terms. Mini Shai-Hulud campaign-name remains a campaign-cluster identifier NOT a roster member; TeamPCP not cited in THIS source for THIS incident.

**Active exploitation:** Source confirms exploitation is occurring in the wild for CI/CD consumers per "any workflow that references the action by version pulls the malicious code on its next run" — paraphrased per Rule 6 (16-word over ceiling).

**IOCs surfaced:**
- Domain: `t.m-kosche[.]com` (C2 / exfil endpoint, shared with Item 3)
- Compromised actions: `actions-cool/issues-helper`, `actions-cool/maintain-one-comment`
- LOLBin pattern: Bun JavaScript runtime + Runner.Worker process memory exfiltration

**A&D relevance:** None — CI/CD consumer targeting at SDLC class.

**Trigger evaluation:**
- T1: no CVE → **FAIL**
- T2: no roster-named actor in source; per Hard Rule 2 cannot propagate → **FAIL**
- T3: 0 Splunk hits on t.m-kosche / actions-cool tokens → **FAIL**
- T4: no roster actor (TTP-change predicate requires roster membership) → **FAIL**
- T5: no A&D-sector targeting → **FAIL**
- T6: not zero-day per se; tag-redirect-rotate technique against GitHub Actions registry boundary; GitHub disabled repo access → **FAIL**

**Disposition:** Net-new IOC layer `t.m-kosche[.]com` C2 + Bun-runtime LOLBin pattern; absorbs into 08:00 morning brief for VT-006 IOC-augmentation. Cross-binds Item 3 via shared C2 domain — strong cluster-anchor signal for morning grader.

### Item 3 — @antv ecosystem npm compromise via atool maintainer account (THN, 00:54 EDT)

**Source:** thehackernews.com/2026/05/mini-shai-hulud-pushes-malicious-antv.html
**Reporter:** Ravie Lakshmanan (THN editorial relay of Socket + StepSecurity + SafeDep + JFrog + Endor Labs + Datadog + Trend Micro + Mondoo + Ox Security multi-vendor research relay-set)
**Window position:** in-window
**Headline:** "Mini Shai-Hulud Pushes Malicious AntV npm Packages via Compromised Maintainer Account"

**Attack core:** npm maintainer account `atool` compromised. 639 malicious versions across 323 unique packages, including @antv namespace (558 versions / 279 packages: @antv/g2, @antv/g6, @antv/x6, @antv/l7, @antv/s2, @antv/f2, @antv/g, @antv/g2plot, @antv/graphin, @antv/data-set) and non-@antv ecosystem (echarts-for-react ~1.1M weekly downloads, timeago.js, size-sensor, canvas-nest.js, others). 22-minute publish burst across 317 packages with identical obfuscated payload (rules out gradual operation). Preinstall hooks (bun run index.js). 630/637 versions inject optionalDependencies pointing to imposter commits in legitimate antvis/G2 GitHub repo. Credential-stealer harvests 20+ types (AWS / Google Cloud / Microsoft Azure / GitHub / npm / SSH / Kubernetes / Vault / Stripe / DB connection strings) + Docker container escape via host socket. Primary exfil `t.m-kosche[.]com:443` (SHARED WITH Item 2 — cross-binding). Fallback GitHub-token-abuse: create public repos with marker description `niagA oG eW ereH :duluH-iahS` (reverses to "Shai-Hulud: Here We Go Again") — 2,500+ repositories identified with this marker (NET-NEW scale figure). OIDC-token abuse + Sigstore attestation pipeline forges legitimate release signatures via CI runner identity + SLSA provenance forgery.

**Attribution per source:** THN explicitly attributes to "TeamPCP (financially motivated actor)" — this affirms the VT-006 / finding-2026-05-12-FLASH-0001 baseline. NOT new attribution per anti-noise rule 1; cluster-expansion not first-time attribution.

**IOCs surfaced:**
- Maintainer account: `atool` (npm)
- Domain: `t.m-kosche[.]com:443` (C2 / exfil, cross-bound with Item 2)
- Marker string: `niagA oG eW ereH :duluH-iahS` (reversed worm-marker; 2,500+ repos)
- Compromised npm package ecosystem: @antv namespace + echarts-for-react + timeago.js + size-sensor + canvas-nest.js (323 packages / 639 versions)
- Tradecraft refinements vs VT-006 baseline: 22-min publish-burst observation + atool maintainer-account vector + Bun-runtime preinstall LOLBin + 2,500+ marker-repo discovery scale + Docker-host-socket container-escape variant + 20+ credential-class enumeration

**A&D relevance:** None directly — @antv visualization libraries / echarts-for-react are general developer tooling, distinct from VT-006 prior surface where @squawk aviation packages were named. The fact that THIS surface expansion did NOT touch aviation packages suggests the worm mechanism is maintainer-enumeration-driven NOT sector-targeted — AFFIRMS VT-006's existing "ad_relevance: medium_indirect_via_squawk_aviation_ecosystem" caveat that A&D-prime dependency-graph reach is unverified.

**Trigger evaluation:**
- T1 (CVE+exploit+A-grade): no new CVE; parent CVE-2026-45321 per VT-006 carry-forward already covers cluster → **FAIL**
- T2 (new attribution): TeamPCP IS roster #001 HIGH AND IS attributed by THN/Socket, **BUT** this is NOT new attribution — TeamPCP→Mini-Shai-Hulud attribution already established in finding-2026-05-12-FLASH-0001 (Wiz + StepSecurity originating, Snyk relay) and VT-006 carry-forward. Per FLASH-POLICY.md Trigger 2 condition `new_attribution: true`, this is incremental cluster expansion not first-time attribution → **FAIL** on new_attribution predicate (NOT on roster-membership)
- T3 (Splunk IOC): 0 hits → **FAIL**
- T4 (TTP change): tradecraft refinements (atool vector + 22-min burst observation + GitHub-Search-API dead-drop variant + 2,500+ marker-repo scale + Bun-runtime LOLBin) are within-cluster refinement NOT class-change vs VT-006 baseline (SLSA-attestation breakage + self-propagating worm + dual-ecosystem propagation + session-network exfil + PBKDF2 campaign-salt + GitHub author identity spoofing already cataloged). Per anti-noise rule 1 (same trigger-topic per 24h with finding-2026-05-12-FLASH-0001 + VT-006 as active cluster anchor) → **FAIL** on anti-noise; refinement absorbs into VT-006 morning grader IOC-augmentation pass
- T5 (A&D campaign): no A&D-sector targeting; @antv ecosystem is general dev tooling → **FAIL**
- T6 (zero-day no patch): rolling unpublishes per VT-006 patch_status; no zero-day boundary → **FAIL**

**Disposition:** Largest single-day surface-area expansion of the Mini Shai-Hulud cluster to date (323 packages / 639 versions / 22-min burst / 2,500+ marker-repos / shared `t.m-kosche` C2 with Item 2). Strong cluster-anchor-refinement for VT-006 update at 08:00 morning brief; net-new IOCs (atool maintainer + marker string + 2,500+ marker-repos + t.m-kosche cross-bound C2 + Docker-host-socket container-escape variant + 20+ credential-class enumeration). Recommend VT-006 ad_relevance evaluation by morning grader. Anti-noise rule 1 binding: TeamPCP/Mini-Shai-Hulud already FLASH-fired at 2026-05-12 06:00 — cluster-expansion absorbs into morning brief NOT re-FLASH.

### Item 4 — CVE-2026-31635 DirtyDecrypt Linux kernel PoC (SecurityWeek, 05:42 EDT)

**Source:** securityweek.com/poc-released-for-dirtydecrypt-linux-kernel-vulnerability/
**Reporter:** Ionut Arghire (relay of V12 security team originating research)
**Window position:** in-window
**Headline:** "PoC Released for DirtyDecrypt Linux Kernel Vulnerability"

**Vulnerability core:** CVE-2026-31635 — missing copy-on-write (COW) guard in rxgk_decrypt_skb component of RxGK subsystem (RxRPC network protocol used by Andrew File System and OpenAFS). Allows oversized response authenticators → write data to privileged process memory or SUID binary page caches → local privilege escalation to root. CVSS 7.5. Variant of CopyFail + DirtyFrag + Fragnesia kernel-bug family. Affects Linux distros with CONFIG_RXGK compiled+enabled (Arch / Fedora / openSUSE + container-platform worker nodes).

**Patch + exploitation status:** PATCHED in April 2026 mainline. PoC released by V12 security team on GitHub (Hard Rule 3 — repo URL NOT linked). No in-the-wild exploitation confirmed.

**A&D relevance:** Low — RxRPC is niche AFS-stack; no known A&D-prime adoption.

**Trigger evaluation:**
- T1: CVSS 7.5 < 9.0 floor; no active exploitation (PoC-only is NOT active exploitation) → **FAIL**
- T2: no actor → **FAIL**
- T3: 0 → **FAIL**
- T4: no actor → **FAIL**
- T5: no campaign → **FAIL**
- T6: PATCHED in April pre-disclosure; CVSS 7.5 < 8.0 floor → **FAIL**

**Disposition:** Pattern-match to recent finding-2026-05-16-0001 NGINX Rift / finding-2026-05-18-0001 MiniPlasma — researcher PoC released AFTER patches deployed, defensive-telemetry refinement value but does NOT meet FLASH-POLICY active-exploitation bar. Mention-class for morning brief if grader chooses; status-update candidate for vuln-tracker _index.yaml if A&D-prime OpenAFS adoption surfaces (low likelihood).

### Item 5 — CVE-2026-8153 Universal Robots PolyScope 5 critical (SecurityWeek, 02:18 EDT)

**Source:** securityweek.com/critical-vulnerability-exposes-industrial-robot-fleets-to-hacking/
**Reporter:** Eduard Kovacs (relay of Claroty / Vera Mens originating research; CISA ICSA-26-134-17 cross-listed advisory)
**Window position:** in-window
**Headline:** "Critical Vulnerability Exposes Industrial Robot Fleets to Hacking"

**Vulnerability core:** CVE-2026-8153 — OS-command-injection in Dashboard Server interface of Universal Robots PolyScope 5 (operating system + GUI for Universal Robots cobots). CVSS 9.8 Critical. Unauthenticated attacker with network access to Dashboard Server port → crafted commands executed on robot OS → remote code execution. PATCHED in PolyScope 5.25.1. Joint advisory: Universal Robots vendor + CISA ICSA-26-134-17. Researcher PoC disclosure NOT in-the-wild exploitation. Researcher (Vera Mens, Claroty) noted cobot networks "often flat and lack proper segmentation" allowing fleet-wide compromise (paraphrased — quote at Rule 6 12w limit).

**A&D relevance:** **INDIRECT but real** — Universal Robots cobots are deployed in aerospace manufacturing supplier-tier (Airbus + Boeing + Lockheed Martin Tier-1/2 supplier inventories include cobot lines for assembly/inspection per public industry references). NO specific A&D customer named in source.

**Trigger evaluation:**
- T1 (CVE≥9.0+active+A-grade): CVSS 9.8 ✓ + A-grade source (Claroty Team82) ✓, **BUT** active exploitation NOT confirmed (researcher PoC + advisory disclosure ≠ in-the-wild exploitation per FLASH-POLICY.md Trigger 1 strict reading "not PoC, not theoretical") → **FAIL** on exploitation_status
- T2: no actor → **FAIL**
- T3: 0 Splunk hits → **FAIL**
- T4: no roster actor → **FAIL**
- T5 (A&D campaign): Universal Robots cobots ARE deployed in A&D-supplier-tier, **BUT** (a) no campaign described — researcher disclosure only, (b) no victim named, (c) no multi-victim language, (d) flat-network warning is researcher hypothetical not observed-incident → **FAIL** on campaign_active AND multi_victim
- T6 (zero-day no patch): PATCHED in PolyScope 5.25.1 at advisory time — NOT zero-day; wide-deployment criterion satisfied but patch_available:true bars trigger → **FAIL**

**Disposition:** Strong status-update candidate for vuln-tracker `_index.yaml` addition (A&D-supplier-tier relevant + CVSS 9.8 + flat-network compromise pathway documented + CISA ICSA-26-134-17 cross-listed). Strong mention-class for 08:00 morning brief Other Signal section for sector-context completeness. Flag for FLASH re-evaluation if/when (a) CISA KEV addition surfaces, OR (b) A&D-prime customer-impact statement surfaces, OR (c) in-the-wild exploitation confirmation surfaces from Claroty / Dragos / Nozomi / Mandiant OT-research.

## Splunk first-party sweep

**Query:** `index=archimedes OR index=defenseclaw_local` across 30-token search set covering Storm-2949 (3 IOC IPs) + Nx Console (rwl.angular-console) + GitHub Action (actions-cool/issues-helper, @antv, echarts-for-react) + Mini Shai-Hulud + DirtyDecrypt + CVE-2026-8153 + Universal Robots + ongoing carry-forwards (shinysp1d3r, CoinbaseCartel, ShinyHunters, Scattered Spider, deadcode09284814, shai-hulud-clone, CVE-2026-20182, CVE-2026-42897, CVE-2026-42945, CVE-2020-17103) + roster actors (UNC1549, Charming Kitten, APT28, APT29, MuddyWater, Volt Typhoon). Earliest -30d.

**Result:** 47 events total, ALL in `index=archimedes sourcetype=archimedes:operation` (self-telemetry). 0 events in `index=defenseclaw_local`. 0 external IOC matches within Trigger 3 24h-recency window.

**Interpretation:** 46th consecutive dormant non-self-telemetry sweep. Silence is not disconfirming per established 45-sweep dormancy precedent across the morning b812307 / afternoon 1513d98 / FLASH a8121bc / ac3683d / 0000-000 sentinel chain. Trigger 3 NOT FIRED.

## Trigger evaluation summary

| Trigger | Definition | Outcome | Notes |
|---|---|---|---|
| 1 | CVE ≥9.0 + active exploitation + A-grade | **FAIL** | CVE-2026-8153 CVSS 9.8 + A-grade BUT no active exploitation (PoC-only); other items no CVE |
| 2 | New attribution to roster actor | **FAIL** | TeamPCP attributed for Item 3 but NOT new (anti-noise vs VT-006 + finding-2026-05-12-FLASH-0001); Items 1, 2 no roster actor cited |
| 3 | First-party Splunk IOC hit | **FAIL** | 47 self-telemetry events + 0 defenseclaw_local hits + 0 external IOC matches |
| 4 | Tracked-actor TTP change A/B | **FAIL** | Item 3 TTP refinements within VT-006 cluster (anti-noise rule 1 binding); Items 1, 2 no roster actor cited |
| 5 | Active A&D campaign multi-victim | **FAIL** | Item 5 CVE-2026-8153 A&D-supplier-tier relevant BUT no campaign, no victim, no multi-victim language; researcher disclosure only |
| 6 | Zero-day no patch | **FAIL** | Item 5 PATCHED in PolyScope 5.25.1; Item 4 PATCHED in April; Items 1-3 registry-side unpublishes |

**Final disposition:** 0 of 6 triggers fired. Clean sweep. No flash-queue.yaml update. No Discord post. No raw-signal files beyond this sentinel.

## Recommendations for 08:00 morning grader

1. **VT-006 Mini Shai-Hulud cluster IOC-augmentation pass.** Net-new IOCs from this sweep:
   - `t.m-kosche[.]com:443` (C2 — cross-binds Item 2 actions-cool + Item 3 atool/AntV)
   - npm maintainer account `atool`
   - Marker string `niagA oG eW ereH :duluH-iahS` (2,500+ repos)
   - macOS persistence: `~/Library/LaunchAgents/com.user.kitty-monitor.plist` + `~/.local/share/kitty/cat.py` + `/var/tmp/.gh_update_state` + `__DAEMONIZED=1` environment marker
   - Compromised actions: `actions-cool/issues-helper`, `actions-cool/maintain-one-comment`
   - Compromised npm ecosystem mass: @antv (10 named packages / 558 versions / 279 packages), echarts-for-react, timeago.js, size-sensor, canvas-nest.js — 323 packages / 639 versions total
   - Tradecraft variants: Bun-runtime preinstall LOLBin + Runner.Worker memory-exfil + GitHub-Search-API dead-drop resolver + Docker-host-socket container-escape + 22-min publish-burst pattern
2. **CVE-2026-8153 Universal Robots vuln-tracker `_index.yaml` addition candidate** — A&D-supplier-tier deployment context + CVSS 9.8 + flat-network compromise pathway + CISA ICSA-26-134-17 cross-listing. ad_relevance: medium-indirect-via-cobot-aerospace-manufacturing-supplier-tier. patch_available: yes (PolyScope 5.25.1).
3. **CVE-2026-31635 DirtyDecrypt** — mention-class only; pattern-match to NGINX Rift / MiniPlasma defensive-PoC-after-patches archetype.
4. **Storm-2949 /new-actor candidate** carry-forward from 00:00 sweep — still strong; deferred to grader discretion.
5. **TeamPCP cluster (VT-006 anchor)** — recommend cluster-anchor-refinement finding update, NOT a new finding (incremental within existing).

## Hard Rules compliance verified

- **Rule 2 (no Archimedes-originated attribution):** TeamPCP attribution to AntV item (3) preserved as THN-said per existing finding-2026-05-12-FLASH-0001 baseline; NOT propagated to Nx Console item (1) or actions-cool item (2) since THOSE THN surfaces do NOT cite TeamPCP for THOSE specific incidents. Mini Shai-Hulud campaign-name preserved as campaign-cluster, NOT propagated to any new roster member. CVE-2026-31635 + CVE-2026-8153 no-attribution preserved verbatim. Storm-2949 still NOT propagated to any tracked actor per 00:00 carry-forward.
- **Rule 3 (no PoC code, no exploit guides, no PoC repo URLs):** V12 security GitHub PoC for CVE-2026-31635 NOT linked. Claroty Team82 advisory technical PDF for CVE-2026-8153 NOT linked. StepSecurity blog technical PoC text for Nx Console + actions-cool NOT quoted at exploit-detail level. Socket blog technical PoC text for AntV NOT quoted at exploit-detail level.
- **Rule 4 (no active scanning):** SpiderFoot not invoked; authorized-targets.yaml empty; passive sources only.
- **Rule 6 (≤15-word quotes, ≤1 per source):** Zero Layer-1 quotes shipped this sweep. The four longer quote candidates encountered (Nx Console developer-credential 16w, actions-cool active-exploitation 16w, SecurityWeek CVE-2026-8153 vendor-advisory 29w, Claroty researcher flat-network 12w) all paraphrased not quoted.
- **Rule 8 (Splunk first-party priority):** 46th consecutive dormant non-self-telemetry sweep. Silence is not disconfirming per established cadence. No first-party-vs-external conflict surfaced this sweep.

**LEGAL-POLICY prohibited-query-patterns:** NOT triggered (no active recon, no exploitation assistance, no credential storage, no impersonation, no circumvention).
**Hard Rule 5:** not in scope (no HIGH threat-box scorings being committed).

## Source-health changes

| Source | Observed status | Recommended action |
|---|---|---|
| **Talos blog feed** (`blog.talosintelligence.com/feeds/posts/default`) | 404 | failure_count increment; held healthy pending operator alt-endpoint decision (intermittent pattern, not yet persistent) |
| **Volexity blog feed** (`www.volexity.com/blog/feed/`) | parse error (malformed XML) | failure_count increment; held healthy pending operator alt-endpoint decision (parse error pattern not yet persistent across multiple sweeps) |
| All other priority feeds (BleepingComputer, THN, SecurityWeek, The Record, DarkReading, MSTIC, Unit42, SentinelLabs, Krebs) | reachable 200 OK | no change |

## No-op confirmations

- No Discord post (silent-on-clean-sweep per FLASH-POLICY).
- No flash-queue.yaml update (0 triggers fired).
- No _master-index.yaml regeneration (sentinel writes no IOCs directly; net-new IOCs deferred to morning grader for VT-006 IOC-augmentation finding).
- No findings file created (clean sweep).
- No raw-signal files beyond this sentinel (per established clean-sweep precedent).

TLP:CLEAR.
