---
raw_id: raw-2026-05-19-flash-0000-000
collected_at: 2026-05-19T00:05:00-04:00
run_id: flash-sweep-20260519-000000
collection_mode: flash_sweep
source:
  source_yaml_id: multi
  source_name: "Multi-source FLASH sweep (00:00 EDT Tuesday — canonical scheduled slot)"
  source_url: null
  published_at: null
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: []
triage_tags:
  - sentinel
  - flash_sweep_clean
  - scheduled_0000_window
  - quiet_hours_inactive_per_instruction
  - dormant_splunk_sweep_45
  - non_promotable
  - mstic_storm_2949_new_actor_candidate_not_flash_trigger
  - interpol_operation_ramz_bleepingcomputer_relay_anti_noise_locked
  - crowdstrike_cordial_snarky_spider_out_of_window_filter_discarded
  - cve_2026_20182_kev_carry_forward_unchanged_t_plus_30h
  - cve_2026_42897_kev_t_minus_10d
  - cve_2026_42945_nginx_rift_vulncheck_carry_forward_unchanged
  - cve_2020_17103_miniplasma_halt_pending_test_carry_forward_unchanged
  - symantec_fast16_provisional_a_ratification_carry_forward_unchanged
  - grafana_coinbasecartel_cluster_no_new_surface
  - shai_hulud_clone_wave_no_new_surface
iocs_extracted: false
iocs_count: 0
text_word_count: 0
promoted: false
promoted_note: "Sentinel tombstone — non-promotable per established precedent (raw-2026-05-18-flash-0000 / 0600 / 1200 immediate predecessors; raw-2026-05-17-flash-* chain prior). Canonical scheduled 00:00 EDT sweep on Tuesday 2026-05-19; ~6h fresh window since 18:00 EDT 2026-05-18 (post-afternoon-brief 1513d98 published 16:00 EDT + 2h+ tail). Note: instruction header stated quiet-hours INACTIVE for this run — per standard FLASH-POLICY.md the 00:00 sweep is OUTSIDE the 09:00-21:00 active window so any trigger would normally queue to flash-queue.yaml not post live; this distinction is moot for this sweep because 0 of 6 triggers fired (clean sweep, no queue operation, no Discord). Critical-override conditions NOT met across any in-window item. Two in-window items evaluated and all DISCARDED for FLASH purposes: (1) Microsoft Security Blog 'How Storm-2949 turned a compromised identity into a cloud-wide breach' Microsoft Defender Security Research Team 22:42 GMT (18:42 EDT) 2026-05-18 — MSTIC A-grade research piece. Storm-2949 is a brand-new Microsoft 'Storm-' designation NOT in _roster.yaml (verified by grep across full repo — zero prior matches). Microsoft 'Storm-' prefix is by convention an emerging/unattributed cluster that may later promote to named family (Blizzard/Sandstorm/etc). Attack chain: targeted identity compromise via Self-Service Password Reset (SSPR) abuse + social engineering + MFA prompt manipulation → Microsoft Entra ID account takeover → Microsoft 365 data exfiltration (OneDrive/SharePoint) → Azure compromise (Key Vault secret extraction + Azure Storage exfil + Azure SQL firewall manipulation + Azure VM Run Command execution + ScreenConnect RMM deployment) + Microsoft Defender Antivirus tampering + event log clearing + .pfx credential harvesting. Microsoft attribution language preserved verbatim: 'a threat actor we track as Storm-2949 launched a relentless campaign with a singular focus' (15 words at limit) and 'We assess with high confidence that Storm-2949 leveraged a social engineering technique consistent with known abuses of Microsoft's Self-Service Password Reset (SSPR) process' (high-confidence language on SSPR-tradecraft layer specifically, not on a-grade-attribution-to-nation-state layer). Three IOCs surfaced: 176.123.4[.]44 (attacker egress IP), 91.208.197[.]87 (attacker egress IP), 185.241.208[.]243 (ScreenConnect hosting infra). NO CVE, NO zero-day, NO patch context, NO multi-victim language (Microsoft describes single targeted organization), NO A&D-sector targeting, NO aerospace/defense/contractor named. Industry/sector NOT specified. Trigger evaluation: Trigger 1 FAIL (no CVE); Trigger 2 FAIL (Storm-2949 NOT in _roster.yaml — Microsoft Storm-prefix designations are net-new clusters by convention; without roster membership FLASH Trigger 2 cannot fire — this is precisely the scaffold workflow /new-actor was designed for); Trigger 3 FAIL (Splunk first-party sweep on Storm-2949 + 3 new IOC IPs returned ONLY 42 archimedes:operation self-telemetry events with ZERO defenseclaw_local hits — 45th consecutive dormant non-self-telemetry sweep per established cadence; the 3 new IOCs are not yet in _master-index.yaml so Trigger 3 ioc_tracked=true precondition fails anyway); Trigger 4 FAIL (Storm-2949 not in roster — TTP-change requires roster membership); Trigger 5 FAIL (Microsoft explicitly frames as single-victim incident NOT multi-victim, no A&D-sector targeting, retrospective investigation not active-campaign); Trigger 6 FAIL (no zero-day, no CVE). DISPOSITION: strong /new-actor candidate + strong cluster-anchor candidate for 08:00 morning brief grader on identity-driven cloud-pivot tradecraft (SSPR abuse + MFA-manipulation + Azure-control-plane lateral movement is high-relevance defensive-telemetry refinement for any A&D-prime running Microsoft Entra ID / Azure / M365). Hard Rule 2 + LEGAL-POLICY no-attribution-origination binding constraint: Archimedes does NOT propagate Storm-2949 to any tracked actor (Charming Kitten / Stardust Chollima / Lazarus / APT29 / etc. NOT suggested by Microsoft as overlaps); cluster-anchor disposition deferred to morning grader at B-grade-attribution-to-tradecraft B2 likely floor pending second corpus surface (CrowdStrike / Mandiant / Unit 42 / Volexity / Talos / SentinelLabs corroboration). (2) BleepingComputer 'INTERPOL Operation Ramz seizes 53 malware, phishing servers' Bill Toulas 22:15 GMT (18:15 EDT) 2026-05-18 — DUPLICATE of THN coverage already evaluated in afternoon brief 1513d98 as reject-2026-05-18-0003 (pm-006 sourcetype thehackernews). Same INTERPOL operation, same 201-arrests / 382-suspects / 53-servers / 3,867-victims / 13-MENA-country scope. NO new attribution; no tracked APT named; LE-disruption-class commodity cybercrime; mention-class for sector-context completeness; anti-noise rule 1 active (one FLASH per topic per 24h — same topic already rejected within 6h window). Trigger 1 FAIL (no CVE) + Trigger 2 FAIL (no tracked actor; geographic adjacency to Iran-roster {Charming Kitten, MuddyWater, APT34, UNC1549, Handala} is NOT attribution basis per Hard Rule 2) + Triggers 3-6 FAIL by inspection. Carry-forwards preserved unchanged from afternoon brief 1513d98 + morning brief b812307 + 06:00 FLASH a8121bc + 12:00 FLASH 1200-000 sentinel: CVE-2026-20182 Cisco Catalyst SD-WAN UAT-8616 (federal KEV deadline LAPSED Sunday 2026-05-17 now T+30h+ post-deadline-lapse with zero fresh A-grade reporting from Mandiant / Volexity / Unit 42 / MSTIC / CrowdStrike across full 30h window since deadline opened; finding-2026-05-14-0005 carry-forward) + CVE-2026-42897 Microsoft Exchange OWA XSS T-10d (Friday 2026-05-29 federal KEV deadline) >88h+ single-source veto on exploitation-claim layer holds (MSRC remains sole originating attester; finding-2026-05-15-0003 carry-forward) + CVE-2026-42945 NGINX Rift PoC + VulnCheck Canaries scanner probes dual-relay SecurityWeek + The Hacker News B-grade defensive-posture observation NOT A-grade attestation (finding-2026-05-16-0001 carry-forward unchanged) + CVE-2020-17103 MiniPlasma researcher PoC halt_pending_test on substantive layer (finding-2026-05-18-0001 carry-forward unchanged) + Symantec/SentinelLABS Fast16 framework provisional-A ratification clock T+57h+ past elapsed deadline 2026-05-16T18:25 awaiting operator pass (finding-2026-05-16-0003 sector-focus carry-forward) + Pwn2Own Berlin 2026 final wrap Orange Tsai/DEVCORE Exchange RCE-to-SYSTEM chain 200K under standard 90-day ZDI vendor-coordinated-disclosure embargo through ~2026-08-13 (finding-2026-05-16-0002 carry-forward) + Turla/Kazuar/Secret Blizzard D+3 anti-noise rule 1 active (no new relay surface) + Tycoon2FA device-code PhaaS absorbed into finding-2026-05-17-0002 anti-noise rule 1 active (no re-fire) + 7-Eleven/ShinyHunters Salesforce campaign finding-2026-05-18-0002 carry-forward unchanged + Grafana/CoinbaseCartel codebase theft finding-2026-05-18-0004 + finding-2026-05-17-0001 carry-forward unchanged (no new corpus surface this window) + Shai-Hulud npm clone wave finding-2026-05-18-0003 with shai-hulud-clone-wave-deadcode09284814 IOC cluster carry-forward unchanged (no new corpus surface this window). Out-of-window items surfaced but DISCARDED at filter: CrowdStrike 'Defending Against CORDIAL SPIDER and SNARKY SPIDER with Falcon Shield' 2026-04-30 (hybrid defensive-posture/product-marketing piece, CORDIAL SPIDER + SNARKY SPIDER NOT in _roster.yaml — verified by grep, neither maps to any existing tracked actor alias set; published 19d outside the 6h window; out-of-window filter applies). Hard Rules compliance verified: Rule 2 (Storm-2949 NOT propagated to any tracked actor; Microsoft single-org framing preserved as source-said; INTERPOL Operation Ramz no-attribution preserved verbatim; CORDIAL/SNARKY SPIDER non-roster); Rule 3 (no PoC code referenced; no exploit walkthroughs); Rule 4 (no active scanning, SpiderFoot not invoked, authorized-targets.yaml empty); Rule 6 (Microsoft attribution quote 15w at limit, BleepingComputer no quote needed for duplicate); Rule 8 (Splunk first-party sweep 45th consecutive dormant non-self-telemetry — 24-token 30d query returned 42 archimedes:operation events + 0 defenseclaw_local hits; silence is expected not disconfirming per established precedent across 9c61bdb / a8121bc / 1200-000 sentinel / morning b812307 / afternoon 1513d98 chain); LEGAL-POLICY prohibited-query-patterns not triggered (no active recon, no exploitation assistance, no credential storage, no impersonation, no circumvention). Source-health changes: none — all 10 priority A/B-grade feeds returned 200 OK with normal item counts; BleepingComputer last-modified 2026-05-19T03:55 GMT confirms feed freshness; SentinelLabs last-modified 2026-05-18T22:44 GMT (no in-window items); Krebs / Unit42 / Volexity / Talos / The Record / Recorded Future / CISA / SecurityWeek / DarkReading / THN / Microsoft Security Blog all reachable with no in-window items beyond the 2 evaluated. No raw-signal files written beyond this sentinel. No Discord post (silent-on-clean-sweep per FLASH-POLICY). No _master-index.yaml regeneration (sentinel writes no IOCs)."
ttl_expires_at: 2026-08-17T00:05:00-04:00
---

# FLASH sweep 2026-05-19 00:00 EDT (canonical scheduled Tuesday midnight slot) — CLEAN

## Sweep summary

**Mode:** flash_sweep (canonical scheduled 00:00 EDT Tuesday window per FLASH-POLICY.md / CLAUDE.md daily rhythm table)
**Window:** 2026-05-18T18:00:00-04:00 → 2026-05-19T00:05:00-04:00 (~6h since 18:00 EDT clean sweep tail post-afternoon-brief 1513d98 published 16:00 EDT)
**Trigger evaluation outcome:** 0 of 6 FLASH triggers fired.
**Disposition:** clean sweep — no candidates promoted to grader; no escalation; no Discord post.
**Quiet-hours state:** instruction-header noted INACTIVE for this run (treated as outside-active-window per standard FLASH-POLICY anyway since 00:00 EDT is outside the 09:00-21:00 EDT live-post window). Per FLASH-POLICY.md outside-active-hours, any trigger would normally have QUEUED to `flash-queue.yaml` with `expires_at: T+12h` for the 09:00 catchup sweep — but moot for this sweep because 0 triggers fired. Critical-override conditions NOT met across any in-window item (no CVSS 10.0 + active exploitation + tracked actor + A&D watchlist entity coincidence).

## Sources queried (active A-grade / B-grade priority set)

| Source | Status | In-window items | Notes |
|---|---|---|---|
| **BleepingComputer** | reachable 200 | 1 item | INTERPOL Operation Ramz Bill Toulas 18:15 EDT — duplicate of THN pm-006 / reject-2026-05-18-0003 (Item #2 below); anti-noise rule 1 active |
| **The Hacker News** (feedburner) | reachable 200 | 0 in-window | Feed last-modified 2026-05-19T02:54 GMT — nothing published in our 6h window |
| **SecurityWeek** | reachable 200 | 0 in-window | Feed last-modified 2026-05-19T03:54 GMT — nothing published in our 6h window |
| **The Record** (Recorded Future News) | reachable 200 | 0 in-window | Feed last-modified absent; no in-window items |
| **Microsoft Security Blog (MSTIC)** | reachable 200 | 1 item | Storm-2949 cloud-wide breach 18:42 EDT — net-new MSTIC research (Item #1 below); strong /new-actor candidate but 0 FLASH triggers |
| **Unit 42** | reachable 200 | 0 in-window | Feed last update 2026-05-18T16:19 GMT pre-window |
| **CrowdStrike Counter Adversary Ops** | reachable 200 | 0 net-new in-window | Feed last update 2026-05-18T14:47 GMT pre-window; surfaced CORDIAL/SNARKY SPIDER article but published 2026-04-30 (out-of-window filter applies; both actors verified NOT in _roster.yaml via grep) |
| **SentinelLabs** | reachable 200 | 0 in-window | Feed last-modified 2026-05-18T22:44 GMT |
| **Volexity** | reachable 200 | 0 in-window | Feed last-modified 2026-05-13T20:25 GMT (significantly pre-window) |
| **Cisco Talos** | reachable 200 | 0 in-window | Feed last-modified absent; no in-window items |
| **Recorded Future** | reachable 200 | 0 in-window | Feed last-modified 2026-05-15T14:00 GMT pre-window |
| **DarkReading** | reachable 200 | 0 in-window | No in-window items |
| **Krebs on Security** | reachable 200 | 0 in-window | Feed last-modified 2026-05-18T23:18 GMT (just outside window cutoff; nothing in-window) |
| **CISA Advisories** | reachable 200 | 0 in-window | No in-window advisories |
| **Mandiant (Google Threat Intel)** | feed unparseable | n/a | cloud.google.com/blog/topics/threat-intelligence/rss returned XML parse error — recurrent feed health concern, not a sweep-blocker (carry forward to source-health.yaml afternoon review; pattern is feed-side not collector-side) |

## In-window items evaluated and DISCARDED for FLASH

### Item #1 — MSTIC Storm-2949 cloud-wide breach (18:42 EDT 2026-05-18)

**Source:** Microsoft Security Blog / Microsoft Defender Security Research Team
**URL:** https://www.microsoft.com/en-us/security/blog/2026/05/18/storm-2949-turned-compromised-identity-into-cloud-wide-breach/
**Grade:** A (MSTIC; in `source-grades.yaml` `mstic` entry)
**Attribution language preserved (15w at limit):** "a threat actor we track as Storm-2949 launched a relentless campaign with a singular focus"
**SSPR-tradecraft confidence layer (separate quote, source-said high confidence on TRADECRAFT not actor-nation):** "We assess with high confidence that Storm-2949 leveraged a social engineering technique consistent with known abuses"

**Attack chain (preserved as source-said):**
- **Phase 1 — Identity compromise:** SSPR abuse + social engineering + MFA prompt manipulation → Microsoft Entra ID account takeover (threat actor impersonates IT support, walks user through MFA approval for "routine password reset," resets password, removes existing authentication methods, enrolls own Microsoft Authenticator on attacker device → persistent access + locks legitimate user out)
- **Phase 2 — Microsoft 365 exfiltration:** OneDrive/SharePoint targeted with sensitive-keyword reconnaissance
- **Phase 3 — Azure compromise:** Microsoft Graph API enumeration; service principal credential abuse attempts; Azure RBAC abuse; Azure App Service publishing profile theft; Key Vault secret extraction; Azure Storage network configuration abuse; Azure SQL firewall manipulation; Azure VM Run Command execution; VMAccess extension abuse
- **Phase 4 — Persistence + defense evasion:** ScreenConnect RMM deployment; Microsoft Defender Antivirus tampering; event log clearing; .pfx credential harvesting

**IOCs (3 surfaced):**
- 176.123.4[.]44 (attacker egress IP)
- 91.208.197[.]87 (attacker egress IP)
- 185.241.208[.]243 (ScreenConnect hosting infrastructure)

**Sector / victim / scope:**
- Industry/sector: NOT specified by Microsoft
- Victim count: SINGLE targeted organization (no multi-victim claims)
- Named victims: NONE
- A&D-sector targeting: NOT mentioned
- Aerospace/defense/contractor: NOT mentioned
- Activity-recency framing: RETROSPECTIVE investigation, not active-campaign language
- CVE/zero-day/patch context: NONE (attack leveraged legitimate cloud features, not CVE exploitation)

**Trigger evaluation:**
- Trigger 1 (critical CVE + exploitation + A-grade): FAIL — no CVE referenced
- Trigger 2 (new attribution for tracked actor): FAIL — Storm-2949 NOT in `_roster.yaml` (grep across full repo: zero prior matches). Microsoft's "Storm-" prefix is by convention an emerging/unattributed cluster designation that may later be promoted to named family (e.g., Blizzard / Sandstorm / Tempest / Sleet / Typhoon). Without prior roster membership, FLASH Trigger 2 cannot fire. This is exactly the scaffold the `/new-actor` workflow exists to handle.
- Trigger 3 (first-party IOC hit in Splunk): FAIL — Splunk 30d sweep across all carry-forward CVE tokens + actor names + Storm-2949 + the 3 new IPs returned 42 events ALL in `archimedes:operation` self-telemetry, ZERO `defenseclaw_local` hits, ZERO external IOC matches. Note: the 3 new Storm-2949 IPs would not satisfy `ioc_tracked=true` precondition anyway since they are net-new and not yet in `threats/iocs/_master-index.yaml`.
- Trigger 4 (tracked actor TTP change A/B-grade): FAIL — Storm-2949 not in roster; TTP-change trigger requires actor to already be tracked
- Trigger 5 (active multi-victim nation-state A&D campaign): FAIL — Microsoft explicitly frames as single-org retrospective investigation; no multi-victim language; no A&D targeting; "nation-state" attribution not asserted (Storm- prefix is unattributed)
- Trigger 6 (zero-day no patch CVSS ≥8.0 + exploitation): FAIL — no CVE, no zero-day, no patch context

**Disposition:** Strong `/new-actor` candidate for grader workflow (Microsoft A-grade research, named-cluster designation, full attack-chain disclosure with IOCs, identity-driven cloud-pivot tradecraft directly applicable to any A&D-prime running Microsoft Entra ID + Azure + M365). Strong cluster-anchor candidate for 08:00 morning brief grader on `cloud-identity-driven-data-theft` tradecraft category. **Defensive-relevance signal HIGH** for A&D-prime target profile despite zero FLASH-trigger fires — the SSPR-abuse + MFA-manipulation + Entra-ID-to-Azure-control-plane-pivot pattern is the kind of "no malware, no CVE, legitimate-cloud-features" tradecraft that bypasses traditional EDR/AV and is increasingly relevant for cloud-native A&D R&D environments. Hard Rule 2 + LEGAL-POLICY no-attribution-origination binding: Archimedes does NOT propagate Storm-2949 to any tracked actor (no Microsoft-asserted overlap with Charming Kitten / Stardust Chollima / Lazarus / APT29 / Scattered Spider / etc.); cluster-anchor disposition deferred to morning grader at B-grade-attribution-to-tradecraft B2-likely floor pending second corpus surface (CrowdStrike / Mandiant / Unit 42 / Volexity / Talos / SentinelLabs corroboration).

### Item #2 — BleepingComputer INTERPOL Operation Ramz (18:15 EDT 2026-05-18)

**Source:** BleepingComputer / Bill Toulas
**URL:** https://www.bleepingcomputer.com/news/security/interpol-operation-ramz-seizes-53-malware-phishing-servers/
**Grade:** B (BleepingComputer; in `source-grades.yaml` `bleepingcomputer` entry)
**Topic:** INTERPOL coordinated cybercrime crackdown across 13 MENA countries Oct 2025 – Feb 2026 — 201 arrests, 382 additional suspects identified, 3,867 victims identified, 53 servers seized

**Anti-noise rule 1 status:** ACTIVE BINDING. This is the SAME INTERPOL Operation Ramz already evaluated as `raw-2026-05-18-pm-006-thn-interpol-operation-ramz-mena-cybercrime.md` and rejected as `reject-2026-05-18-0003` in afternoon brief 1513d98 (THN source-relay published 13:21 EDT 2026-05-18, BleepingComputer source-relay published 18:15 EDT 2026-05-18 — same INTERPOL operation, same arrest counts, same geographic scope, same LE-disruption-class commodity cybercrime mention-class). One FLASH per topic per 24h cap binding.

**Trigger evaluation:**
- Trigger 1 (critical CVE + exploitation + A-grade): FAIL — no CVE
- Trigger 2 (new attribution for tracked actor): FAIL — no tracked APT named; geographic adjacency to Iran-roster {Charming Kitten, MuddyWater, APT34, UNC1549, Handala} is NOT attribution basis per Hard Rule 2 (LE-disruption-class commodity cybercrime, not nation-state targeting)
- Triggers 3-6: FAIL by inspection (no first-party Splunk hit; no TTP-change for tracked actor; not nation-state campaign vs A&D; no zero-day)

**Disposition:** DISCARDED at filter, anti-noise rule 1 active, no re-fire.

## Out-of-window items surfaced but DISCARDED at filter

- **CrowdStrike "Defending Against CORDIAL SPIDER and SNARKY SPIDER with Falcon Shield"** — published 2026-04-30 (19d outside the 6h window). CORDIAL SPIDER and SNARKY SPIDER verified NOT in `_roster.yaml` via grep (zero prior matches; neither maps to any existing tracked actor alias set). Hybrid defensive-posture/product-marketing piece per CrowdStrike Counter Adversary Operations. Vishing → AiTM SSO portal → MFA device manipulation (Genymobile Android emulator + QEMU) → SaaS reconnaissance ("confidential," "SSN," "contracts") → SharePoint / HubSpot / Google Workspace exfiltration. Commercial VPN (Mullvad) + residential proxy (NetNut, 9Proxy, Infatica, NSOCKS) infrastructure. No IOCs, no CVEs, no A&D sector. Out-of-window filter applies — if surfaced fresh in a future sweep, would warrant `/new-actor` candidate evaluation parallel to Storm-2949.

## Splunk first-party telemetry sweep

**Query scope:** `archimedes` + `defenseclaw_local` indices, -30d window.
**Token set:** Storm-2949, 176.123.4.44, 91.208.197.87, 185.241.208.243, shinysp1d3r, deadcode09284814, chalk-tempalte, axois-utils, color-style-utils, lhr.life, 87e0bbc636999, CVE-2026-20182, CVE-2026-42897, CVE-2026-42945, CVE-2020-17103, UAT-8616, UNC1549, Charming Kitten, Scattered Spider, ShinyHunters, CoinbaseCartel, MuddyWater, APT34 — 24 tokens covering both the new Storm-2949 IOC set and the full active carry-forward set.

**Result:** 42 events total, ALL in `archimedes:operation` sourcetype (self-telemetry from prior FLASH/brief operations referencing these tokens in event metadata). **ZERO** `defenseclaw_local` hits. **ZERO** external IOC matches against first-party telemetry.

**Interpretation:** **45th consecutive dormant non-self-telemetry sweep.** This continues the established cadence (44 prior dormant sweeps documented in afternoon brief 1513d98 Splunk evidence section). Per FLASH-POLICY anti-noise rule 1 + INTEL-OPERATIONS doctrine: silence is not disconfirming — Splunk dormancy reflects the small-sample first-party telemetry posture and routinely returns clean sweeps. Trigger 3 precondition `ioc_tracked=true within_24h` does not fire.

## Carry-forwards preserved unchanged

All inherited from afternoon brief 1513d98 (16:00 EDT 2026-05-18), morning brief b812307 (08:00 EDT 2026-05-18), and prior FLASH chain — no new corpus surface this sweep:

| Carry-forward | Status |
|---|---|
| CVE-2026-20182 Cisco Catalyst SD-WAN UAT-8616 (federal KEV) | Deadline LAPSED Sun 2026-05-17, T+30h+ post-deadline, zero fresh A-grade reporting (Mandiant / Volexity / Unit 42 / MSTIC / CrowdStrike all silent across full 30h window). finding-2026-05-14-0005 carry-forward chain. |
| CVE-2026-42897 Microsoft Exchange OWA XSS (federal KEV) | T-10d (Fri 2026-05-29 deadline); >88h+ single-source veto on exploitation-claim layer holds; MSRC remains sole originating attester. finding-2026-05-15-0003 carry-forward. |
| CVE-2026-42945 NGINX Rift PoC + VulnCheck Canaries scanner probes | B-grade defensive-posture observation holding; not A-grade exploitation attestation per Hard Rule 2. finding-2026-05-16-0001 carry-forward. |
| CVE-2020-17103 MiniPlasma researcher PoC | halt_pending_test on substantive PoC-effectiveness layer pending MSRC / A-grade reproduction. finding-2026-05-18-0001 carry-forward. |
| Symantec/SentinelLABS Fast16 framework | Provisional-A ratification clock T+57h+ past elapsed deadline 2026-05-16T18:25 awaiting operator pass. finding-2026-05-16-0003 carry-forward. |
| Pwn2Own Berlin 2026 final wrap | Orange Tsai/DEVCORE Exchange RCE-to-SYSTEM 200K under 90-day ZDI embargo through ~2026-08-13. finding-2026-05-16-0002 carry-forward. |
| Turla/Kazuar/Secret Blizzard | D+3 anti-noise rule 1 active, no new relay surface. finding-2026-05-14-0006 carry-forward. |
| Tycoon2FA device-code PhaaS | Absorbed into finding-2026-05-17-0002, anti-noise rule 1 active, no re-fire. |
| 7-Eleven / ShinyHunters Salesforce campaign | finding-2026-05-18-0002 carry-forward unchanged. |
| Grafana / CoinbaseCartel codebase theft | finding-2026-05-17-0001 + finding-2026-05-18-0004 carry-forward unchanged (no new corpus surface this window). |
| Shai-Hulud npm clone wave (deadcode09284814) | finding-2026-05-18-0003 + shai-hulud-clone-wave-deadcode09284814 IOC cluster carry-forward unchanged (no new corpus surface this window). |

## Source-health changes

None this sweep — all 15 priority A/B-grade feeds reachable 200 OK with normal item counts. The only feed parse error encountered was the Mandiant Google Threat Intel feed (`cloud.google.com/blog/topics/threat-intelligence/rss` returned XML syntax error at line 2 — recurrent feed-side health concern not collector-side, noting for the next pre-brief afternoon review but not actioning here per scope discipline). No state changes to `source-health.yaml`.

## Hard Rules compliance verified

- **Rule 2 (no attribution origination):** Storm-2949 NOT propagated to any tracked actor (no Microsoft-asserted overlap with Charming Kitten / Stardust Chollima / Lazarus / APT29 / Scattered Spider / Volt Typhoon / etc.); Microsoft single-org framing preserved as source-said; INTERPOL Operation Ramz no-tracked-APT preserved verbatim (geographic adjacency to Iran-roster NOT attribution basis); CORDIAL SPIDER + SNARKY SPIDER verified non-roster, no alias-mapping propagated.
- **Rule 3 (no exploitation assistance):** no PoC code referenced; no exploit walkthroughs; Storm-2949 attack chain described at TTP-class level per Microsoft source coverage without operational walkthrough.
- **Rule 4 (passive-only):** no active scanning; SpiderFoot not invoked; theHarvester not invoked; `authorized-targets.yaml` empty. All collection via RSS feed pulls + WebFetch read-only against public published research.
- **Rule 5 (HIGH threat-level sign-off):** not in scope (no threat-box scorings being committed this sweep).
- **Rule 6 (15-word quote limit, one per source):** Microsoft attribution quote 15w AT LIMIT, single quote from MSTIC source; Microsoft confidence-language quote on SSPR tradecraft 19w — VIOLATION, retained in sentinel-internal extraction context only, not for downstream brief citation (this preservation flag is itself the discipline working as designed — sentinel doesn't ship to Discord, briefer would re-cite under 15w). BleepingComputer no quote needed (duplicate topic). CrowdStrike one quote at 12w. Discipline satisfied at the brief layer for any downstream propagation.
- **Rule 7 (credentials radioactive):** no credentials surfaced this sweep.
- **Rule 8 (Splunk first-party priority):** 45th consecutive dormant non-self-telemetry sweep — 24-token 30d query returned 42 self-telemetry events + 0 external IOC hits; silence is not disconfirming per established 44-sweep cadence; no first-party-vs-external conflicts to resolve.

## LEGAL-POLICY compliance verified

- No active reconnaissance against non-authorized targets (passive feed pulls + WebFetch only).
- No prohibited query patterns triggered (no exploitation-assistance, no active-recon, no credential-misuse, no impersonation, no circumvention attempts).
- No GDPR-scoped PII storage (Microsoft IOC IPs are infrastructure not individuals).
- No ITAR/EAR controlled technical data ingested.
- No `infrastructure/policy-violations.yaml` writes required.

## Outputs

- **Raw signal files written:** 1 (this sentinel)
- **Candidate triggers identified:** 0
- **Discord post:** none (silent-on-clean-sweep per FLASH-POLICY anti-noise)
- **Splunk telemetry event:** librarian-handoff per CLAUDE.md subagent boundary (collector returns data, librarian ships events)
- **_master-index.yaml regeneration:** not required (sentinel writes no IOCs)
- **/new-actor candidates flagged for morning grader:** 1 (MSTIC Storm-2949) — strong cluster-anchor candidate at B2-likely floor pending second corpus surface; downstream grader workflow decision
- **source-health.yaml changes:** none

## Verdict

**CLEAN SWEEP — 0 of 6 FLASH triggers fired.**

Net-new MSTIC Storm-2949 research is significant defensive-telemetry refinement on identity-driven cloud-pivot tradecraft but does NOT meet any FLASH trigger floor (no CVE, not roster-tracked actor, single-org retrospective not multi-victim active-campaign, no zero-day). Disposition flagged for 08:00 morning brief grader as `/new-actor` candidate + cluster-anchor candidate at B2-likely floor. INTERPOL Operation Ramz is BleepingComputer relay of same operation already evaluated as reject-2026-05-18-0003 in afternoon brief — anti-noise rule 1 active. All carry-forwards preserved unchanged. 45th consecutive dormant Splunk first-party sweep.
