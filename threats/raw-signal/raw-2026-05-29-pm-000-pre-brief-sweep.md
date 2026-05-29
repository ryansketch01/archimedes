---
raw_id: raw-2026-05-29-pm-000-pre-brief-sweep
collected_at: 2026-05-29T15:35:00-04:00
run_id: pre-brief-20260529-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: archimedes-internal
  source_name: Archimedes pre-brief PM-29 sweep sentinel
  source_url: null
  published_at: 2026-05-29T15:35:00-04:00
sweep_window:
  start: 2026-05-29T12:05:00-04:00
  end: 2026-05-29T15:35:00-04:00
  duration_h: 3.5
prior_sweep_anchor:
  sweep_id: flash-2026-05-29-1200
  anchor_at: 2026-05-29T12:05:00-04:00
  raw_id: raw-2026-05-29-flash-1200-000-sentinel-clean-sweep.md
  commit_sha: a1374d3
  disposition: zero_triggers_fired
  notes: |
    12:00 EDT FLASH sentinel was the fourth consecutive clean sweep in the
    post-PM-28-brief window (18:00, 00:00, 06:00, 12:00 all 0/6). The PM-29
    window since 12:05 EDT is only 3.5h — much shorter than a typical
    pre-brief — but is the standard PM-pre-brief scope per the orchestrator
    instruction. Productive surfacings concentrated in the Rapid7 + CISA
    KEV layer in the final hour pre-15:30.
prior_brief_anchor:
  brief_id: 2026-05-29-morning
  shipped_at: 2026-05-29T08:00:00-04:00
  commit_sha: 5a287de
  notes: |
    AM-29 brief published with 3 findings (A2/A2/A2): MSTIC vpmdhaj
    npm typosquat ShaiWorm-flagged cluster (A2); MSRC Chaotic Eclipse
    state-transition (BlueHammer/RedSun/UnDefend now ITW per MSRC) with
    Security Affairs + The Register paired relays resolving the PM-28
    single-source veto (A2); Oracle CPU May 2026 critical batch
    (CVE-2026-46840 CVSS 10.0 + 9.9/9.8 cohort, A2). Standing absorption
    baseline includes all 7 PM-28 findings + 4 AM-28 + 3 FLASH-1200-28.

match_reason:
  watchlist: []                 # No direct A&D-prime named in any in-window item; PAN-OS GlobalProtect is structurally DIB-relevant but no named prime
  actors:
    - none_direct               # No new roster-actor attribution this window. SecurityWeek's "Russian APT" Treasury 2019 FOIA-release reference is historical (APT29-cluster known activity, not new attribution)
  vulnerabilities:
    - CVE-2026-0257             # NEW critical surface — Palo Alto PAN-OS GlobalProtect authentication bypass. State transition this window: Rapid7 MDR publishes "observed exploitation" since 2026-05-17 with IOCs (104.207.144.154 / 146.19.216.119 / 146.19.216.120 / 146.19.216.125; DESKTOP-GP01 / GP-CLIENT machine names; aa:bb:cc:dd:ee:ff spoofed MAC); CISA KEV adds today with 3-day federal due 2026-06-01; Palo Alto PSIRT confirms "limited exploit attempts" on unpatched devices. NOT YET in _index.yaml — vuln-tracker handoff candidate.
    - none_other                # 23andMe lawsuit (CCPA-2023), VS Code Remote-SSH RCE researcher disclosure (no ITW), Veeam / Notepad++ / Roundcube vendor patches (no ITW), 176 malicious npm packages (TeamPCP-adjacent ecosystem but unattributed, generic credential-stealer post-install pattern — anti-noise to active VT-006 / VT-009 / Mini Shai-Hulud cluster)
  keywords:
    - "CVE-2026-0257"
    - "PAN-OS GlobalProtect"
    - "authentication bypass"
    - "GlobalProtect portal"
    - "GlobalProtect gateway"
    - "Cloud Authentication Service"
    - "Rapid7 MDR"
    - "Jonah Burgess"           # Rapid7 researcher (cross-reference: also reported Gogs zero-day on 2026-05-28 FLASH-1200)
    - "main_DecryptAppAuthCookie"
    - "ChatGPhish"              # Permiso Security THN disclosure
    - "Permiso Security"
    - "Push Security LLMShare"  # BleepingComputer ChatGPT share-link malvertising
    - "openew[.]app"
    - "176 malicious npm packages"
    - "Megalodon attackers"
    - "Trump Mobile data breach"
    - "VS Code Remote-SSH RCE"
    - "Ghost Stadium"           # Carry-forward — already absorbed PM-28-005 finding-2026-05-28-FLASH-1800-0001 cluster

triage_tags:
  - pre_brief_sweep
  - pm29_sweep
  - pan_os_globalprotect_state_transition
  - kev_addition_same_day
  - rapid7_first_party_mdr_observation
  - vuln_tracker_handoff_candidate_cve_2026_0257
  - chatgpt_research_pattern
  - npm_supply_chain_ongoing_cluster_anti_noise
iocs_extracted: deferred_to_per_item_raws
iocs_count: 0                   # this sentinel; per-item raws carry IOC blocks
text_word_count: 1450
promoted: false
ttl_expires_at: 2026-08-27T15:35:00-04:00
test: false
---

# Pre-brief Sentinel — PM-29 Sweep, 2026-05-29

## Window and scope

Window: 2026-05-29T12:05:00-04:00 (FLASH-1200 sentinel commit `a1374d3`) → 2026-05-29T15:35:00-04:00. Duration 3.5h. Quiet hours INACTIVE through end-of-window. Pre-brief sweep scope is wider than FLASH (any watchlist/roster/vuln-index match, not only FLASH triggers).

## Headline finding

**CVE-2026-0257 (PAN-OS GlobalProtect authentication bypass) — state transition.** Three independent A/A-grade signals converged in the same 3-hour window:

1. **Rapid7 (provisional A) — first-party MDR observation.** Rapid7 publishes emergent-threat-response post 2026-05-29T16:49 UTC reporting MDR-observed successful exploitation "across numerous customers" with earliest observed exploitation 2026-05-17 (T+4 days post-Palo Alto advisory). No lateral movement observed. IOCs published.
2. **CISA KEV — same-day addition.** Catalog republished 2026-05-29T19:00:06 UTC with CVE-2026-0257 dateAdded 2026-05-29, federal BOD-22-01 due date 2026-06-01 (3-day aggressive timeline; ransomware-use "Unknown").
3. **Palo Alto PSIRT (provisional A vendor self-disclosure) — vendor confirms ITW.** Advisory updated to "Palo Alto Networks has become aware of limited exploit attempts on unpatched PAN-OS devices without mitigations applied" (last attested 2026-05-29).

Carries to grader-queue as fresh PAN-OS state-transition + vuln-tracker handoff candidate (not yet in `_index.yaml`, distinct from the tracked CVE-2026-0300). Raw-signal written to PM-001.

Configuration prerequisite (per Palo Alto): authentication override enabled in GlobalProtect portal or gateway + Cloud Authentication Service (CAS) disabled + reuse of authentication-override cookie encryption/decryption certificate with another feature (e.g., HTTPS service). The defect is implicit cookie trust after decryption — `main_DecryptAppAuthCookie()` lacks signature verification. Rapid7 urges treating CVSS-medium (v4 7.8 per Palo Alto; CVSS-BT 7.8) as critical given edge-VPN appliance attack surface.

## Sources swept (in-window items beyond FLASH-1200 sentinel scope)

| Source | Status | In-window items | Disposition |
|---|---|---|---|
| **BleepingComputer RSS** | healthy | 2 | 1 raw-signaled (PM-003 ChatGPT-share-links Push Security, paired with THN ChatGPhish); 1 DISCARDED (23andMe lawsuit — civil litigation on 2023 breach, not threat-intel) |
| **SecurityWeek RSS** | healthy | 1 ("In Other News" weekly roundup) | Raw-signaled (PM-002, mixed structural-context items) |
| **The Hacker News RSS** | healthy | 1 (ChatGPhish Permiso disclosure) | Raw-signaled (PM-003, paired with BleepingComputer LLMShare) |
| **The Register security RSS** | healthy | 2 | Both DISCARDED — Gogs zero-day re-coverage (anti-noise lock active, already absorbed FLASH-1200-28) and 23andMe lawsuit (civil litigation) |
| **Security Affairs RSS** | healthy | 1 (GREYVIBE Paganini) | DISCARDED — anti-noise lock (already absorbed PM-28-003 WithSecure originating source) |
| **The Record RSS** | healthy | 0 | n/a |
| **Krebs on Security RSS** | healthy | 0 | last_modified 2026-05-25 pre-window — quiet |
| **Rapid7 RSS** | healthy | 1 | **PM-001 raw-signaled** — Rapid7 MDR observation of PAN-OS CVE-2026-0257 exploitation |
| **MSTIC (Microsoft Security Blog)** | healthy | 0 | last_modified pre-window |
| **Unit 42 (feedburner)** | healthy | 0 | last_modified pre-window |
| **Cisco Talos blog** | healthy | 0 | last_modified pre-window |
| **SentinelOne / SentinelLabs** | healthy | 0 | last_modified 15:50 GMT pre-window |
| **CrowdStrike blog** | healthy | 10 dateless | unchanged from 0000/0600/1200 sweeps — all marketing/MQ content, no threat-intel research class. DISCARDED |
| **SANS ISC** | healthy | 0 | last_modified 19:29 GMT inside-window from feed-server activity but 0 in-window items after since-filter |
| **Check Point Research** | healthy | 0 | last_modified 2026-05-26 pre-window |
| **WeLiveSecurity (ESET)** | healthy | 0 | n/a |
| **Mandiant (feedburner)** | held healthy | 404 | twenty-third consecutive feedburner 404 — operator policy hold continues |
| **Volexity blog feed** | held healthy | parse error | **fourth consecutive parse failure** (0000/0600/1200/15:30 PM); operator stale-flip decision still pending. Volexity homepage WebFetch confirms most-recent visible post dated 2025-12-04 — feed is broken for 2026 content. Recommend stale flip if 18:00 FLASH parse-fails as fifth consecutive |
| **Industrial Cyber** | held healthy | 403 bot-block | persistent Akamai 403 |
| **Sophos news / Ars Technica security** | stale | n/a | endpoints retired, workarounds documented in source-health.yaml |
| **Dark Reading RSS** | healthy | 2 dateless (events listings — Infosec Europe + Name That Toon Contest) | non-threat-intel, DISCARDED |
| **CISA Cybersecurity Advisories all.xml** | healthy | 0 | last_modified null, 0 in-window items |
| **CISA KEV catalog** | healthy | **NEW addition CVE-2026-0257 dateAdded 2026-05-29** | catalogVersion 2026.05.29, dateReleased 2026-05-29T19:00:06Z — PM-001 captures this |
| **NVD critical CVE window** | not invoked PM-29 | n/a | 12:00 FLASH covered the 06:00→12:00 window with 3 results all coordinated-disclosure non-ITW; PM-29 NVD lastModStartDate skipped given fresh Palo Alto / Rapid7 / CISA KEV converged signal already captures the headline tracking surface |
| **abuse.ch ThreatFox** | held healthy via WebFetch | CAPTCHA wall | unauthenticated WebFetch path hits CAPTCHA verification page; MCP not built; 32-roster-tag check deferred to next sweep. Per 12:00 sentinel: zero in-window matches for any roster actor / family |
| **Splunk archimedes + defenseclaw_local** | healthy | 0 non-archimedes-internal events 24h | 25 sourcetype events all archimedes-internal pipeline telemetry (archimedes:scheduler 17, archimedes:operation 4, archimedes:flash 4). Targeted CVE-2026-0257 IOC search across (104.207.144.154 / 146.19.216.119 / 146.19.216.120 / 146.19.216.125 / DESKTOP-GP01 / GP-CLIENT / Vultr / "Dromatics Systems" / PAN-OS / GlobalProtect / CVE-2026-0257) over -30d returned **0 hits**. Trigger 3 cannot fire. 48th consecutive dormant non-self-telemetry sweep |

## NVD critical CVE window

Not invoked PM-29 (12:00 FLASH covered the 06:00→12:00 NVD window; PM-29's 12:05→15:35 window is short and the headline tracking surface already converged on PAN-OS CVE-2026-0257 via vendor + IR-firm + CISA KEV layer). Next NVD lastModStartDate window covered at 18:00 FLASH.

## Sourceing-grade implications

**Push Security** — first Archimedes-corpus citation (BleepingComputer relay of Push Security LLMShare campaign research). NO prior corpus track record. Vendor research firm with named-engineer bylines and consistent technical rigor. **Provisional B is conservative starting grade** per LayerX / Seqrite / Trendyol-Albayrak / Sysdig / Zellic / Aikido precedent (peer class). Flagged for librarian/operator source-grade-log review.

**Permiso Security** — first Archimedes-corpus citation (THN relay of Permiso ChatGPhish research). NO prior corpus track record. Vendor research firm with named-byline (Andi Ahmeti) and CVE-class disclosure pattern. **Provisional B is conservative starting grade** per same peer class. Flagged for source-grade-log review.

**Rapid7** — already provisional A (ratification pending), now SECOND surface in 24h (Gogs zero-day FLASH-1200-28 + PAN-OS CVE-2026-0257 PM-29). Jonah Burgess byline reappears on PAN-OS via the underlying advisory + vendor coordination; not the named researcher on PAN-OS (Rapid7 MDR research team is the byline) but the cross-reference is worth flagging for source-grade-log: consistent Rapid7 IR-firm rigor across two consecutive surfaces.

**Palo Alto PSIRT** — NOT yet in `source-grades.yaml` as a dedicated id (distinct from cisco-psirt / f5 / kernel-org-netdev / openai-self-disclosure / github-blog-self-disclosure / litespeed-blog-self-disclosure first-citation precedent class). PM-001 raw-signal explicitly carries the PSIRT vendor self-disclosure language ("limited exploit attempts on unpatched PAN-OS devices") for grader/source-grade-log handoff: would be provisional A on first surface per the vendor-self-disclosure-on-own-product precedent class.

## Anti-noise locks honored (carry-forward)

Active locks at PM-29 sweep time:
- **MSRC / Chaotic Eclipse six-zero-day saga** — raw-2026-05-29-am-002 + finding-2026-05-29-0002 (within 24h hard lock). Three relays in 12:00 sweep (The Record / SecurityWeek-derived / Security Affairs) — all blocked; no fresh in-window content here.
- **Gogs zero-day RCE** — raw-2026-05-28-flash-1200-002 → finding-2026-05-28-FLASH-1200-0002 A2 (within 24h, lock active through 2026-05-29 12:00 EDT). The Register re-coverage in window blocked.
- **FortiClient EMS CVE-2026-35616 fresh exploitation** — raw-2026-05-28-flash-1200-001 → finding-2026-05-28-FLASH-1200-0001 B2 (within 24h, lock active). Nothing fresh in window.
- **GreyVibe / WithSecure / Russia-AI-Ukraine** — raw-2026-05-28-pm-003 (within 24h, lock active). Security Affairs Paganini re-coverage blocked.
- **VT-008 Exchange CVE-2026-42897** — KEV federal due date 2026-05-29 TODAY = T+0. Five-day quiet carry-forward persists. No fresh in-window content.
- **VT-006 Mini Shai-Hulud + VT-009 Nx Console** — KEV-listed 2026-05-27 absorbed into PM-27 brief; SecurityWeek "In Other News" roundup re-coverage in PM-002 raw-signal is bounded structural-context (Megalodon attackers / 176 npm packages enrichment, no new attribution).
- **Ghost Stadium FIFA WC Chinese cluster** — raw-2026-05-28-pm-005 → finding-2026-05-28-FLASH-1800-0001 cluster (within 24h lock). SecurityWeek "In Other News" mention is bounded restatement in PM-002.

Newly cleared since 0600 sweep — none (window too short).

## Source-health proposed changes

**Volexity blog feed** — **fourth consecutive parse failure** (0000/0600/1200/15:30 PM). Per 2-failure stale threshold, recommend formal stale flip at 18:00 FLASH if pattern persists. The Volexity homepage confirms feed is broken for 2026 content (most recent visible post dated 2025-12-04 — likely feed schema migration). Operator alt-RSS-path discovery for the 2026 Volexity content surface still pending.

**Push Security** — NEW first-citation; recommend top-level source-health.yaml entry creation at `failure_count: 0` if librarian downstream confirms add to source-grades.yaml.

**Permiso Security** — NEW first-citation; recommend top-level source-health.yaml entry creation at `failure_count: 0` if librarian downstream confirms add to source-grades.yaml.

All other A/B-grade priority sources reachable with productive or zero in-window items per normal cadence.

## Trigger evaluation (PM-pre-brief is NOT a FLASH sweep)

PM-29 is a **pre-brief collection**, not a FLASH sweep. Per Mode 1 procedure, we evaluate watchlist/roster/vuln-index match, not FLASH triggers. For situational awareness only (no action — afternoon brief grader will consume):

| Trigger | Condition | Result |
|---|---|---|
| 1 — critical CVE + ITW | CVE-2026-0257 ITW per Rapid7 + Palo Alto + CISA KEV. CVSS v4 7.8 (vendor-assigned) = below 9.0 floor for Trigger 1. Rapid7 explicitly argues for critical-treatment despite numeric medium. **Trigger 1 marginal-fail on CVSS floor — but the convergence is brief-headline material for grader review** | NO FIRE (CVSS floor) |
| 2 — tracked-actor attribution | No new roster-actor attribution. Rapid7 explicitly: "no indication of successful lateral movement" — no actor named. Anti-noise locks block all other in-window roster-touching items | NO FIRE |
| 3 — first-party IOC hit | Splunk 30-day check across full IOC set (4 IPs + 2 machine names + Vultr/Dromatics ASNs + product strings) returned 0 hits. Zero non-archimedes-internal events in 24h | NO FIRE |
| 4 — tracked-actor TTP change | No A/B-grade source documents new tooling/targeting/infra class for any roster actor in window | NO FIRE |
| 5 — A&D-sector campaign | No A&D-prime victim disclosure in window. PAN-OS GlobalProtect is structurally DIB-relevant edge-VPN but Rapid7 declines sector attribution ("no indication of victim sector") | NO FIRE |
| 6 — zero-day no-patch | CVE-2026-0257 patches available since 2026-05-13 (the ITW exploitation is post-patch). MSRC Chaotic Eclipse already absorbed AM-29. No NEW zero-day disclosures in window | NO FIRE |

**Disposition: pre-brief collection productive but no FLASH triggers fire.** The PAN-OS CVE-2026-0257 convergence is a brief-headline candidate via the standard scheduled-brief grader path (not FLASH). The CVSS-floor near-miss on Trigger 1 is documented for grader visibility but does not warrant FLASH-style override.

## Extraction notes

- Language: en
- Article type: sentinel (in-window items captured in per-item raws PM-001/002/003)
- Raw IOC extraction invoked: yes (PM-001 carries full Rapid7 + Palo Alto IOC block + IOC type breakdown)
- Quiet hours active: NO (15:35 EDT is inside 09:00–21:00 active window)
- Critical override evaluated: NO (would require CVSS 10.0 + active exploitation + tracked actor + A&D watchlist named target — only the active-exploitation condition is fully satisfied here, and even that is "limited exploit attempts" vendor-attested rather than mass-campaign disclosure)
- Splunk first-party telemetry: 48th consecutive sweep dormant for non-archimedes-internal events; targeted PAN-OS CVE-2026-0257 IOC sweep over -30d returned 0 hits across both indexes

## Carry-forward state for 18:00 FLASH sweep

1. **PAN-OS CVE-2026-0257 KEV federal due 2026-06-01 (T-3 days, Monday).** Watch for additional IR-firm corroboration (Mandiant / Volexity / Unit 42 / MSTIC / CrowdStrike) and any A&D-prime victim disclosure. If a Tier-1 IR-firm publishes today/tomorrow with named A&D-prime victim, FLASH Trigger 5 fires.
2. **VT-008 Exchange CVE-2026-42897 KEV federal due TODAY (T+0).** Watch for compliance-status updates (KEV pattern: no compliance-status update on the catalog post-deadline). Single-source veto on MSRC "Exploitation Detected" tag persists — no Mandiant / Volexity / Unit 42 / MSTIC / CrowdStrike corroboration in any in-window sweep through PM-29.
3. **Volexity blog feed parse failure cluster** — fifth consecutive failure at 18:00 will trigger stale flip per source-health rule.
4. **176 malicious npm packages (Megalodon-attacker enrichment per SecurityWeek In Other News)** — flagged for vuln-tracker / VT-006 / VT-009 cluster awareness; no fresh attribution but operational cluster-expansion signal. Anti-noise lock prevents repeat coverage absent fresh attribution.
5. **ChatGPT vulnerability cluster (LLMShare / ChatGPhish)** — research-only, no roster, no A&D, no tracked CVE. PM-003 raw-signal flagged for grader awareness as pattern-of-interest (LLM platforms as malware-distribution and prompt-injection-rendering surface). Grader may consider standing AI-platform-abuse section for future briefs.
6. **GREYVIBE WithSecure attribution-cluster** — absorbed; no fresh in-window content.

End of PM-29 sentinel.
