---
raw_id: raw-2026-05-29-am-000-pre-brief-sweep
collected_at: 2026-05-29T07:35:00-04:00
run_id: pre-brief-20260529-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: archimedes-internal
  source_name: Archimedes pre-brief AM-29 sweep sentinel
  source_url: null
  published_at: 2026-05-29T07:35:00-04:00
sweep_window:
  start: 2026-05-28T15:30:00-04:00
  end: 2026-05-29T07:35:00-04:00
  duration_h: 16.08
prior_sweep_anchor:
  sweep_id: flash-2026-05-29-0600
  anchor_at: 2026-05-29T06:05:00-04:00
  raw_id: raw-2026-05-29-flash-0600-000-sentinel-clean-sweep.md
  commit_sha: e416c9f
  disposition: zero_triggers_fired
  notes: |
    06:00 EDT Friday dawn FLASH sentinel was the third consecutive clean
    sweep in the post-PM-28-brief window (18:00, 00:00, 06:00 all 0/6).
    Pre-brief scope is wider than FLASH (any watchlist/roster/vuln-index
    match, not only FLASH triggers), so net-new items beyond what the
    FLASH sentinels evaluated may be promoted to raw-signal here.
prior_brief_anchor:
  brief_id: 2026-05-28-afternoon
  shipped_at: 2026-05-28T16:00:00-04:00
  commit_sha: ed16a5f
  notes: |
    PM-28 brief published with 7 findings, digraphs B1/A2/A1/A2/B2/B3/A2.
    Standing absorption baseline includes: Wired/Reuters Pentagon CENTCOM
    troops-location-data (B1, ad-prime adjacent OPSEC); MSTIC Storm-2697
    "The Gentlemen" Go-encryptor ransomware (A2); SecurityWeek/WithSecure
    GreyVibe Russia-nexus AI-augmented Ukraine campaign (A1, multi-victim
    sector-shaped); CISA Nx Console/Megalodon federal supply-chain alert
    (A2); FBI/Group-IB Ghost Stadium Chinese 2026 FIFA WC domain cluster
    (B2); The Record/GCHQ Keast-Butler Russia "daily" subsea hybrid (B3);
    CISA ICS batch 10 advisories MacGregor/XCharge/Schneider/ABB (A2).
    Plus FLASH-1200 carry-forward: FortiClient EMS CVE-2026-35616 ITW
    (B2), Gogs zero-day RCE (A2, vuln-watch keyword set live), MSRC
    Chaotic Eclipse pushback (FLASH-1200-003).

match_reason:
  watchlist: []
  actors:
    - roster_001_TeamPCP_question    # MSTIC vpmdhaj cluster: Defender detection rule "Trojan:JS/ShaiWorm" hints at Shai-Hulud lineage (May 12 Mini Shai-Hulud was Wiz/Snyk/StepSecurity-attributed to TeamPCP); MSTIC itself does NOT attribute vpmdhaj to TeamPCP or to any tracked actor. Source-fidelity question for grader.
    - roster_010_Salt_Typhoon_historical    # The Register Charter Communications coverage references Charter as among orgs caught up in Salt Typhoon (#010) last year — historical, not new attribution
    - roster_013_Scattered_Spider_cluster_extension    # Charter ShinyHunters vishing→Entra→Salesforce vector overlaps Scattered LAPSUS$ Hunters / Bling Libra cluster (Unit 42 Out of the Crypt PM-28); ShinyHunters/Bling Libra alias was already absorbed PM-28 (Carnival Cruise 5.99M)
  vulnerabilities:
    - ZD-001    # BlueHammer (Windows LPE, CVE-2026-33825) — STATE TRANSITION: Security Affairs + The Register both confirm Nightmare/Chaotic Eclipse-disclosed PoC now actively exploited in the wild; was patched per May Patch Tuesday but exploitation is post-patch
    - ZD-002    # RedSun (Windows LPE, no CVE assigned) — STATE TRANSITION: now confirmed exploited in the wild
    - ZD-003    # UnDefend (Defender update block / DoS, no CVE assigned) — STATE TRANSITION: now confirmed exploited in the wild
    - CVE-2026-45585    # YellowKey — Microsoft "exploitation more likely" classification; PoC public; still unpatched (vuln-tracker handoff candidate, not yet in _index.yaml)
    - CVE-2026-46840    # NEW: Oracle REST Data Services pre-auth full RCE, CVSS 10.0, Oracle CPU May 2026 (published 2026-05-28); BaaS / DBaaS layer used by enterprise + gov customers; structurally DIB-relevant
    - CVE-2026-46775    # NEW: Oracle REST Data Services CVSS 9.9 low-privilege full takeover; same product family as CVE-2026-46840
    - CVE-2026-46817    # NEW: Oracle Payments (E-Business Suite 12.2.3-12.2.15) pre-auth full takeover, CVSS 9.8; EBS deployed broadly in DIB ERP estate
    - CVE-2026-34311    # NEW: Oracle Hospitality OPERA 5 Property Services pre-auth full takeover, CVSS 9.8; hospitality not direct A&D but represents the same Oracle EBS layer surface
    - CVE-2026-46839    # NEW: Oracle REST Data Services CVSS 9.9 — third critical in this product family
    - CVE-2026-46822    # NEW: Oracle iAssets CVSS 9.9
    - CVE-2026-46824    # NEW: Oracle Universal Work Queue CVSS 9.9
    - CVE-2026-46833    # NEW: Oracle Database Net Service CVSS 9.0
    - CVE-2026-46819    # NEW: Oracle Internet Procurement Connector CVSS 9.1
    - CVE-2026-45321    # KEV-listed Mini Shai-Hulud (VT-006) — MSTIC vpmdhaj report may extend lineage; not state-transition itself but the MSTIC analysis is the brief-worthy enrichment
  keywords:
    - "vpmdhaj"
    - "ShaiWorm"
    - "Mini Shai-Hulud"
    - "Bun runtime"
    - "preinstall hook"
    - "AWS IMDSv2"
    - "HashiCorp Vault"
    - "Oracle CPU May 2026"
    - "Critical Patch Update"
    - "Chaotic Eclipse"
    - "Nightmare Eclipse"
    - "BlueHammer exploited"
    - "RedSun exploited"
    - "UnDefend exploited"
    - "ShinyHunters Charter"
    - "Bling Libra Carnival"
    - "vishing Entra Salesforce"

triage_tags:
  - pre_brief_sweep
  - vt006_lineage_question
  - state_transition_zd001_zd002_zd003
  - oracle_cpu_critical_batch
  - shinyhunters_cluster_extension
iocs_extracted: deferred_to_per_item_raws
iocs_count: 0    # this sentinel; per-item raws carry IOC blocks
text_word_count: 1850
promoted: false
ttl_expires_at: 2026-08-27T07:35:00-04:00
test: false
---

# Pre-brief Sentinel — AM-29 Sweep, 2026-05-29

Window: 2026-05-28T15:30:00-04:00 (PM-28 pre-brief baseline) → 2026-05-29T07:35:00-04:00 (now). Three FLASH sentinels in between (18:00, 00:00, 06:00 — all 0/6 triggers). Pre-brief scope is wider: any watchlist / roster / vuln-index match graduates to raw-signal; FLASH-trigger threshold is not required.

## Sources swept (in-window items returned 200 + items)

- **BleepingComputer** — 6 in-window items.
- **The Hacker News** — 3 in-window items.
- **Microsoft Security Blog (MSTIC)** — 1 in-window item (Mini Shai-Hulud / vpmdhaj typosquat campaign).
- **SecurityWeek** — 2 in-window items.
- **Security Affairs** — 3 in-window items.
- **The Register (security)** — 4 in-window items.
- **CrowdStrike blog** — 10 items returned but all `published: null` (parser-incompatible date schema persists from prior sweeps; same pre-existing queue, no in-window net-new — verified by URL pattern match against PM-28 brief absorption).
- **SANS ISC** — 2 in-window items (DShield sensor file analysis + Friday stormcast — operational, not actor / vuln / sector signal).
- **Mandiant feedburner alt endpoint (`mandiant.com/resources/blog/rss.xml`)** — 200, 0 in-window items.
- **Unit 42** — 0 in-window items.
- **The Record** — 0 in-window items.
- **CISA all advisories** — 0 in-window items.
- **Wired (Security Latest)** — 0 in-window items (the Pentagon/CENTCOM coverage was already absorbed PM-28).
- **Krebs on Security** — 0 in-window items.
- **Cisco Talos** — 0 in-window items.
- **SentinelLabs** — 0 in-window items.
- **WeLiveSecurity (ESET)** — 0 in-window items.
- **Rapid7** — 0 in-window items.
- **GitHub Security Blog** — 0 in-window items.
- **Sucuri** — 0 in-window items.
- **Bitdefender Labs** — 0 in-window items.
- **Check Point Blog / Research** — 0 in-window items.
- **Proofpoint** — 0 in-window items.
- **Darktrace** — 0 in-window items.
- **Dark Reading** — 0 in-window items (only future-event RSS placeholders).
- **ZDI blog** — 0 in-window items.

## Sources swept (404 / parse-error / auth-block, recorded for source-health)

- **Volexity blog** — third consecutive parse error (`not well-formed (invalid token)` line 17 col 68). Pattern unchanged from 0000 + 0600 FLASH sentinels. **Recommend source-health flip to stale** at the librarian source-health pass.
- **feeds.arstechnica.com/arstechnica/security** — 404 (first observation this sweep; record for source-health).
- **Industrial Cyber** — 403 (consistent with prior bot-block pattern).
- **socket.dev/blog/rss.xml** — 404 (consistent pre-existing pattern).
- **Patchstack** — 404 (consistent pre-existing pattern).
- **Wiz Research** — not re-attempted (pre-existing 404 pattern; pending alt endpoint).
- **Dragos blog feed** — 404 (pre-existing pattern).
- **Zscaler security research feed** — 404 (first observation; record).
- **F5 K-article atom** — 404 (placeholder URL; no working endpoint indexed in source-grades yet).
- **threatfox-api.abuse.ch** — 401 (POST JSON required; collector standing pattern, deferred to MCP build).

## CISA KEV catalog check

`dateReleased: 2026-05-28` (unchanged from 0000 + 0600 sweeps). Three entries dateAdded 2026-05-28 still listed and already absorbed by PM-27 + PM-28 brief work:
- CVE-2026-48027 Nx Console (VT-009, federal due 2026-06-10)
- CVE-2026-45321 TanStack / Mini Shai-Hulud (VT-006, federal due 2026-06-10)
- CVE-2026-8398 Daemon Tools Lite (consumer, not corpus-tracked, federal due 2026-05-30 = TOMORROW)

**Zero new dateAdded entries for 2026-05-29.**

KEV due-date watch (T-N relative to 2026-05-29):
- VT-008 Exchange CVE-2026-42897 federal due 2026-05-29 = **T+0 TODAY**. MSRC "Exploitation Detected" remains single-source; no Mandiant / Volexity / Unit 42 / CrowdStrike corroboration in this window either. Single-source veto persists.
- VT-006 Mini Shai-Hulud CVE-2026-45321 federal due 2026-06-10 = T-12. **State transition possible** via MSTIC vpmdhaj coverage — see per-item raw-2026-05-29-am-001.
- VT-009 Nx Console CVE-2026-48027 federal due 2026-06-10 = T-12. No new state.
- CVE-2026-8398 Daemon Tools Lite federal due 2026-05-30 = T-1. Consumer, not corpus-tracked.

## NVD critical-CVE check

`pubStartDate=2026-05-28T20:00Z pubEndDate=2026-05-29T11:30Z cvssV3Severity=CRITICAL` — **12 results, almost all Oracle Critical Patch Update May 2026 cluster.**

Top of the batch by score:
- **CVE-2026-46840** — Oracle REST Data Services 24.2.0-26.1.0, **CVSS 10.0** scope-changing pre-auth full RCE.
- **CVE-2026-46775** — Oracle REST Data Services 24.2.0-26.1.0, CVSS 9.9 low-priv full takeover.
- **CVE-2026-46839** — Oracle REST Data Services, CVSS 9.9.
- **CVE-2026-46822** — Oracle iAssets, CVSS 9.9.
- **CVE-2026-46824** — Oracle Universal Work Queue, CVSS 9.9.
- **CVE-2026-46817** — Oracle Payments (E-Business Suite 12.2.3-12.2.15), CVSS 9.8 pre-auth full takeover.
- **CVE-2026-34311** — Oracle Hospitality OPERA 5 Property Services, CVSS 9.8 pre-auth full takeover.
- **CVE-2026-46819** — Oracle Internet Procurement Connector, CVSS 9.1.
- **CVE-2026-46833** — Oracle Database Net Service, CVSS 9.0.
- **CVE-2026-8809** — WordPress Advanced Custom Fields Extended (Deferred status, already noted in 0000 sweep, plugin layer, non-direct DIB).
- **CVE-2026-8732** — WordPress WP Maps Pro 9.8 (noted in 0600 sweep, Wordfence coord-disclosure, no ITW).
- **CVE-2026-3655** — WordPress OTP Login With Phone Number 9.8 (noted in 0600 sweep, Wordfence coord-disclosure, no ITW).

**No NVD references claim active exploitation for any of the 12.** Oracle CPU items are vendor-coordinated patch batch — Oracle's CPU advisory traditionally does not include ITW status in the public document. Will require Mandiant / CrowdStrike / Volexity / Unit 42 / Rapid7 IR-firm corroboration to fire Trigger 1 for any individual Oracle CVE. For now: high-priority enrichment material for the morning brief (the Oracle CPU batch is itself a brief-worthy critical-CVE cluster surface, independent of ITW).

## abuse.ch ThreatFox check

API endpoint requires JSON POST with `auth-key` (ABUSECH_API_KEY in .env per source-health docs). MCP not built; deferred per long-standing source-health policy. The FLASH-0600 sentinel ran the recent-IOC-family filter against the roster keyword set and returned 0 matches — coverage carries forward to AM-29.

## Splunk first-party

`index=defenseclaw_local OR index=archimedes earliest=-24h@h | stats count by index sourcetype` returns:
- archimedes:scheduler — 17 events
- archimedes:operation — 10 events
- archimedes:flash — 3 events

All Archimedes operational telemetry; **zero defenseclaw_local events; zero IOC hits.** Hard Rule 8: silence is not disconfirming, just absent. Trigger 3 not applicable to pre-brief sweep (wider scope), but the corpus IOC carry-forward picture is unchanged.

## In-window items promoted to per-item raws

Three items warrant standalone raw-signal files at pre-brief scope:

1. **`raw-2026-05-29-am-001-mstic-vpmdhaj-npm-typosquat-shaiworm-cloud-cicd-credential-theft-may-28-distinct-or-lineage-question.md`** — MSTIC publishes full analysis of the 14-package vpmdhaj npm cluster (May 28 launch, 4-hour publication window, AWS IMDSv2 + ECS + Vault + GitHub Actions + npm publish token theft, Bun runtime abuse). Defender detection name `Trojan:JS/ShaiWorm` hints at family-lineage with Mini Shai-Hulud (VT-006, May 12 finding, Wiz/Snyk-attributed to TeamPCP), but **MSTIC itself does NOT attribute vpmdhaj to TeamPCP or any tracked actor**. Source-fidelity question for grader: distinct-but-related cluster, or lineage extension? A-grade source, full IOC set, structurally DIB-relevant via cloud/CI/CD credential theft. Multiple corroborating relays: The Hacker News (Sicoob NuGet co-coverage + npm), Microsoft analysis is primary.

2. **`raw-2026-05-29-am-002-security-affairs-the-register-chaotic-eclipse-three-windows-zerodays-now-itw-zd001-002-003-state-transition.md`** — Security Affairs (Pierluigi Paganini) + The Register both confirm **BlueHammer (ZD-001, CVE-2026-33825 Patched), RedSun (ZD-002, no CVE), UnDefend (ZD-003, no CVE) are now actively exploited in the wild**. Quote (The Register): "Attackers began hammering three of the six — BlueHammer, RedSun, and UnDefend — soon after Nightmare published working proof-of-concept exploit code". This is a **state transition for three vuln-tracker dossiers** (`threats/vulnerabilities/BlueHammer/`, `RedSun/`, `UnDefend/`). Microsoft's pushback post (MSRC, already absorbed at PM-28 via raw-2026-05-28-flash-1200-003) framed three of six as "exploited in the wild" + classified YellowKey (CVE-2026-45585) as "exploitation more likely". The Register adds: Microsoft Digital Crimes Unit signal + ZDI Dustin Childs + Luta Security Katie Moussouris commentary critical of Microsoft's response. Researcher's July 14 "bone shattering" threat noted. Both A-grade equivalents; Security Affairs is provisional B-grade-class (Paganini long-running); The Register is B-grade trade press relay of MSRC + researcher posts.

3. **`raw-2026-05-29-am-003-oracle-cpu-may-2026-critical-batch-rest-data-services-payments-cve-2026-46840-cvss-10-46775-46817-34311-no-itw.md`** — Oracle Critical Patch Update May 2026 produced multiple CVSS ≥9.0 CVEs across REST Data Services (3x including CVSS 10.0 CVE-2026-46840 unauth scope-changing full RCE), Oracle Payments / E-Business Suite (CVE-2026-46817 9.8), Oracle Hospitality OPERA 5 (CVE-2026-34311 9.8), Oracle iAssets, Universal Work Queue, Database Net Service, Internet Procurement Connector. **No exploitation-in-the-wild language in any NVD reference.** Oracle CPUs are coordinated quarterly patch batches; ITW status is not part of the public CPU advisory standard. Brief-worthy as a critical-CVE batch surface independent of ITW; structurally DIB-relevant because Oracle EBS, REST Data Services, and Oracle Database are deployed broadly in DIB ERP / financial / data-services estate. NVD A-grade.

Items NOT promoted (background/dilution coverage):

- **Charter Communications ShinyHunters 4.9M breach** (BleepingComputer Gatlan + The Register) — US telecom, not A&D; ShinyHunters is the same actor cluster already absorbed at PM-28 via Carnival Cruise (Bling Libra alias, Unit 42 Out of the Crypt). New TTP detail: vishing → Microsoft Entra compromise → Salesforce internal access → 42M records. The Register references Charter's historical role in **Salt Typhoon** (#010) telecom-sector campaign — historical, not new attribution. Cluster-extension worth a brief mention in the morning brief's ShinyHunters absorption framing, but not its own finding — already-tracked actor + non-A&D victim + Bling Libra/Scattered LAPSUS$ Hunters cluster already covered. **Recommend grader cluster-extend into the existing Carnival/ShinyHunters PM-28 absorption, not a new finding.**

- **Sicoob NuGet (Socket discovery via The Hacker News)** — Brazilian financial / cooperative banking sector, sole vendor relay, no actor attribution, no A&D angle. Background.

- **BTMOB Android RAT-as-a-service** (Security Affairs / BleepingComputer / ESET Daniel Cunha Barbosa) — same item flagged in 0600 FLASH sentinel as commodity criminal tooling, Latin America focus (Argentina AFIP), no actor / nation-state / A&D angle. Background.

- **Anthropic Mythos-class model rollout** (BleepingComputer) — product news, not security signal. Background.

- **Google security engineer Polymarket insider trading** (BleepingComputer) — personnel-misconduct criminal case, not threat intelligence. Background.

- **California sues 23andMe** (SecurityWeek) — civil litigation over 2023 breach, no new technical signal. Background.

- **Chrome 148 patches 151 CVEs / 22 critical** (SecurityWeek Arghire) — large coordinated-disclosure patch batch, **no exploited-in-the-wild language**, no V8 / Mojo IPC critical; CVE-2026-9872 (GPU OOB write), 9873 (Network UAF), 9874 (Dawn UAF), 9875 (WebGL OOB read), 9876 (WebGL UAF) are the named critical items, $43k bounties on 9872/9873. **Trigger 1 NO FIRE** (no ITW). Brief-worthy as critical-CVE batch but lower priority than the Oracle CPU because Chrome browser patching cadence is well-established in DIB endpoint estate and Google's coordinated-disclosure track record is strong. Lower-priority background absorption candidate for morning brief.

- **SANS ISC DShield file-upload analysis** (Guy Bruneau) — methodology / honeypot research, no actor or vuln signal. Background.

- **Microsoft Calls the Zero-Day Dumps Irresponsible** (Security Affairs, Paganini) — same factual core as the per-item raw-2026-05-29-am-002 (Chaotic Eclipse); content folded into that file rather than promoted separately.

- **Snowflake / Natoma acquisition** (The Register) — AI / vendor M&A news, not threat intelligence. Background.

## Anti-noise locks honored

Active 24h locks (would block re-promotion if duplicate content surfaced in window — none did):
- FortiClient EMS CVE-2026-35616 (finding-2026-05-28-FLASH-1200-0001 B2) — within 24h, lock active until 2026-05-29 ~12:00 EDT.
- Gogs zero-day RCE (finding-2026-05-28-FLASH-1200-0002 A2) — within 24h, lock active until 2026-05-29 ~12:00 EDT. Vuln-watch keyword set live (`watch-config.yaml` `gogs-argument-injection-2026-05-28`); no CVE assignment / vendor IR observation in window.
- MSRC Chaotic Eclipse Defender/BitLocker pushback (raw-2026-05-28-flash-1200-003) — within 24h, lock active. **However, the Security Affairs + The Register state-transition for ZD-001/002/003 is NEW signal not in the FLASH-1200-003 absorption** — promote per-item raw, see am-002.
- VT-008 Exchange CVE-2026-42897 — 5-day quiet carry-forward continues; nothing in window.
- VT-006 Mini Shai-Hulud (TanStack) + VT-009 Nx Console — KEV-listed 2026-05-27 absorbed; **MSTIC vpmdhaj coverage is brief-worthy enrichment / possible lineage extension**, see am-001.
- All 7 PM 2026-05-28 brief findings + 4 morning findings + 3 FLASH-1200 findings — implicit absorption.

Cleared since 0600 sweep — none (window too short).

## Trigger evaluation (FLASH-style, applied for context only — pre-brief promotion is not trigger-gated)

| Trigger | Condition | Result |
|---|---|---|
| 1 — critical CVE + ITW | Oracle CPU batch (CVSS 9.0-10.0) but no NVD/Oracle ITW reference; Chrome 148 22 critical no ITW; WordPress trio Wordfence-only coord-disclosure no ITW | **NO FIRE (Trigger 1 standalone)** |
| 2 — tracked-actor attribution | MSTIC vpmdhaj does NOT attribute to tracked actor; Defender `ShaiWorm` detection name is family-suggestive not actor-attribution; ShinyHunters/Bling Libra Charter is cluster-extension not new attribution | **NO FIRE** |
| 3 — first-party IOC hit | Splunk archimedes + defenseclaw_local clean; zero IOC hits in -24h | **NO FIRE** |
| 4 — tracked-actor TTP change | None in window | **NO FIRE** |
| 5 — A&D-sector campaign | None in window (Charter is telecom, Sicoob is Brazilian banking, Carnival was PM-28) | **NO FIRE** |
| 6 — zero-day no-patch | **Three already-tracked CVE-less zero-days transitioned to ITW (ZD-001 patched May, ZD-002/ZD-003 unpatched) — state transition material for existing dossiers, NOT a new no-patch zero-day disclosure.** YellowKey CVE-2026-45585 still unpatched + Microsoft "exploitation more likely" — vuln-tracker scaffold candidate. | **PARTIAL — state transition, not new disclosure (handle via vuln-tracker dossier update in morning pipeline)** |

Pre-brief promotion disposition: **three per-item raws promoted** (am-001 MSTIC vpmdhaj, am-002 Chaotic Eclipse ITW state transition, am-003 Oracle CPU batch). Grader will cluster + apply Admiralty + WEP downstream.

## Source-health proposed changes

(Defer the actual edits to the librarian's source-health pass per file-ownership rule — the collector returns observations, the librarian re-emits health.)

- **Volexity blog** — third consecutive parse error (line 17 col 68 invalid token). **Recommend stale flip** with `last_error: "RSS feed XML well-formedness error at line 17 col 68 — three consecutive failures across 0000 + 0600 + AM-29 sweeps"` and `stale_since: 2026-05-29`. Preserve any operator-set `notes` verbatim.
- **arstechnica.com/arstechnica/security** — 404 on this fetch. First observation; do not flip stale yet (≥2 threshold). `failure_count` increment 0→1, `last_error` describing the 404.
- **Mandiant feedburner** — still 404; alt endpoint `mandiant.com/resources/blog/rss.xml` working (200, 0 in-window). Held healthy per long-standing operator policy.
- **CrowdStrike blog** — 200 but `published: null` parser-incompatibility persists from prior sweeps. Held healthy; no source-health change.
- **Cisco Talos blog** — 200, `last_modified` null this fetch. Held healthy.
- **Dragos / Zscaler / F5 / Patchstack / Industrial Cyber / Socket / Wiz / threatfox-api** — pre-existing failure patterns, no state change.

## Extraction notes

- Language: en
- Article type: sentinel + handoff to three per-item raws
- Raw IOC extraction invoked: deferred to per-item raws (am-001 has the vpmdhaj IOC block, am-002 has the Chaotic Eclipse PoC URLs, am-003 has the Oracle CPU CVE list — each invokes ioc-extraction in its own file)
- Word count this sentinel: ~1850 (under the typical pre-brief sentinel ceiling)
