---
raw_id: raw-2026-06-10-flash-0600-000
collected_at: 2026-06-10T06:10:00-04:00
run_id: flash-sweep-20260610-060000
collection_mode: flash_sweep
sentinel: true
flash_candidate: false
source:
  source_yaml_id: sentinel
  source_name: "FLASH sweep sentinel (1 candidate fired; 8 rule-outs)"
  source_url: null
  published_at: 2026-06-10T06:00:00-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: []
triage_tags: [flash_candidate_sweep, quiet_hours, queue_path, anti_noise_triple_kev_lock_active]
iocs_extracted: false
iocs_count: 0
text_word_count: 0
promoted: false
ttl_expires_at: 2026-09-08T06:10:00-04:00
---

# FLASH sweep 2026-06-10 06:00 EDT — 1 candidate fired; 8 evaluated and ruled out

Window: 00:00 EDT 2026-06-10 → 06:00 EDT 2026-06-10 (6 hours).

## Anti-noise locks active at sweep start

- **`triple-kev-sweep-2026-06-10`** — covers CVE-2026-50751 (Check Point VPN), CVE-2026-11645 (Chrome V8), CVE-2026-42271 (LiteLLM). Lock expires 2026-06-11 01:25 EDT. Per 00:00 sweep `raw-2026-06-10-flash-0000-001/002/003` and `flash-2026-06-10-0125` queued brief. **These three CVEs are NOT re-emitted as new candidates today.** Any new vendor relays or supplemental coverage of any of the three CVEs in the 06:00 window were observed in passing but excluded from candidacy per anti-noise lock.

## Quiet-hours posture

06:00 EDT is OUTSIDE active hours (09:00–21:00 EDT). Any candidate produced FLASH would QUEUE to `infrastructure/flash-queue.yaml` per FLASH-POLICY and ship via 09:00 EDT catchup sweep — UNLESS critical-override fires (CVSS 10.0 + ITW + tracked-actor + A&D-watchlist-target, all four simultaneously). None of today's items hit critical-override.

## Sources queried

A/B-grade primary feeds and one direct Unit 42 vendor fetch:

- **A-grade:** CISA advisories all.xml, Microsoft Security Blog feed (one in-window post — AI-investigation playbook, non-FLASH), Unit 42 RSS (two in-window posts — one matched; see `-001`), Mandiant/Cloud feed (parse error — known stale; no in-window content surfaced), MSRC blog feed (parse error — known stale per `source-health.yaml`).
- **B-grade:** BleepingComputer RSS (2 in-window items), The Hacker News RSS (4 in-window items), SecurityWeek RSS (4 in-window items), The Record (0 in-window items), SANS ISC (1 in-window item — non-threat-relevant framing-headers diary).
- **First-party:** Splunk `archimedes` + `defenseclaw_local` indexes — broad IOC + tracked-actor + CVE keyword query covering Unit 42 PAN-OS IOCs + triple-KEV CVEs + tracked-actor names — zero substantive hits (only Archimedes self-instrumentation events from the 00:00 sweep's own brief commits).

## Triggers evaluated

### Trigger 1 — Critical CVE (CVSS ≥ 9.0) + active exploitation + A-grade source

**1 FIRE (resurface candidate; grader decision required):**

- **CVE-2026-0257 PAN-OS GlobalProtect auth bypass** — Unit 42 first-hand IR threat brief published 2026-06-09 14:05 UTC (Andy Piazza byline, A-grade). Pre-PoC and post-PoC exploitation activity attested. Second A-grade IR-firm confirmation distinct from Rapid7 (prior single-source IR-observation veto lifts). 5 net-new IPv4 IOCs not in prior Rapid7 set. **CVSS 7.8 strict reading FAILS hard-threshold;** corpus-precedent-aligned reading via finding-2026-05-29-0004 (CISA 3-day federal due date treated as critical-tier signal) ELIGIBLE per PAN-OS CVE-2026-0300 FLASH-0007 resurface precedent (2 of 3 resurface conditions PASS — new IOCs + second A-grade IR; condition 3 novel-TTP pending full publication review). → `raw-2026-06-10-flash-0600-001`. **Grader decision required:** promote as FLASH (resurface) vs. absorb as morning-brief UPDATE block.

**Evaluated and ruled out:**

- **Ivanti Sentry CVE-2026-10520 (CVSS 10.0) + CVE-2026-10523 (CVSS 9.9)** — patched at disclosure 2026-06-10. Vendor explicit statement: "not aware of any customers being exploited" (Ivanti, paraphrase ≤ 15 words). **Fails trigger-1 on active-exploitation prong.** High-priority morning-brief CVE; not FLASH.
- **Fortinet FortiSandbox CVE-2026-25089 (CVSS 9.8)** — patched at disclosure 2026-06-10. No ITW exploitation reported by Fortinet PSIRT or third-party. **Fails trigger-1 on active-exploitation prong.** Morning-brief priority.
- **ServiceNow active exploitation disclosure (no CVE assigned)** — active exploitation confirmed by ServiceNow on Australia-platform-release customers; "successful queries of instance tables" (ServiceNow verbatim, ≤ 15 words). Patch applied 2026-06-05; advisory published 2026-06-10. No CVE/CVSS, no actor, no A&D victim. **Fails trigger-1 on CVE assignment prong** (no CVE means no CVSS to evaluate against hard threshold). Notable continuing-coverage candidate for morning brief — ServiceNow reportedly knew since 2026-04-07.

### Trigger 2 — New attribution for tracked actor

**0 FIRE.** No roster actor named in any window content. Unit 42 PAN-OS brief explicitly does not name an actor. Microsoft June Patch Tuesday no actor attribution. ServiceNow no actor attribution. RoguePlanet zero-day: researcher pseudonym Chaotic Eclipse / Nightmare-Eclipse — not in `_roster.yaml`. No Mandiant, MSTIC, CrowdStrike actor-research publications in window.

### Trigger 3 — First-party Splunk IOC hit (last 24h, tracked IOC)

**0 FIRE.** Broad Splunk query against `archimedes` + `defenseclaw_local` indexes covering: Unit 42 PAN-OS 9 net-new IPv4 IOCs (`23.128.228.6`, `104.207.144.154`, `146.19.216.119/120/125`, `179.43.172.213`, `185.195.232.139`, `198.12.106.60`, `202.144.192.47`); triple-KEV CVE identifiers; tracked-actor names (Qilin, UNC1549, APT28, APT29, Volt Typhoon, Lazarus, TeamPCP); Mini Shai-Hulud campaign — returned zero substantive matches. Only events returned were Archimedes self-instrumentation (00:00 sweep brief commits). **Hard Rule 8: silence is not disconfirming.**

### Trigger 4 — Tracked actor TTP change (A/B-grade)

**0 FIRE.** No A/B-grade publication in window documents new tooling/targeting/infrastructure attributable to a roster actor. Unit 42 PAN-OS brief is on a tracked CVE (CVE-2026-0257) but no actor attribution — cannot anchor trigger-4 without actor.

### Trigger 5 — Active A&D-sector campaign (multi-victim, active)

**0 FIRE.** No A&D-prime victim named in any window content. ServiceNow exploitation is single-vendor-scope, no nation-state. Unit 42 PAN-OS exploitation: structural-indirect A&D relevance only (no named A&D-prime victim). Microsoft Patch Tuesday: no A&D-sector framing. No nation-state campaign disclosures in window.

### Trigger 6 — Zero-day without patch (CVSS ≥ 8.0 or widely-deployed) + exploitation confirmed/imminent

**0 FIRE.**

- **Microsoft Defender RoguePlanet zero-day (Chaotic Eclipse / Nightmare-Eclipse PoC)** — disclosed 2026-06-10 05:22 UTC via THN. No CVE assigned, no patch (zero-day status confirmed), no CVSS scored. PoC released but **no confirmed in-the-wild exploitation observed** per source — researcher publication only. Fails trigger-6 on `exploitation_confirmed_or_imminent` prong. Same pattern as Cisco Unified CM CVE-2026-20230 disposition on 2026-06-04 (PoC alone is not ITW). Researcher series tracked separately via finding-2026-06-02-0010; carry to morning brief as continuing-coverage UPDATE (fourth Defender zero-day in researcher series after BlueHammer, UnDefend, RedSun).
- **Arista EOS CVE-2026-7473 (KEV-listed 2026-06-09, vendor refuses to patch)** — Vendor stated "no software upgrade path is planned" (Arista, ≤ 15 words paraphrase). CVSS **6.9**, below the 8.0 trigger-6 hard threshold. "Widely-deployed" qualifier could be argued for Arista 7020R/7280R/7500R series (carrier-class routing in service-provider and large-enterprise networks) but the CVSS hard-threshold reading rules out trigger-6 firing. **Notable as an unusual vendor-refusal-to-patch case**; morning-brief priority for vuln-tracker handoff. Defender mitigation: apply vendor-supplied workarounds or discontinue affected devices per CISA KEV required action.
- **Six protobuf.js vulnerabilities** — patched at disclosure. Not zero-day.

## Notable-but-non-triggering items (carry to next pre-brief / morning)

- **Microsoft June 2026 Patch Tuesday — 200 fixes including 3 zero-days (YellowKey CVE-2026-45585 / GreenPlasma CVE-2026-45586 / MiniPlasma CVE-2020-17103).** Existing corpus tracking: full vuln dossiers for YELLOWKEY, GREENPLASMA, MiniPlasma. **State transition to PATCHED** for these three; carry to morning brief as vuln-tracker handoff for `_index.yaml` state update. Existing ZD-001 BlueHammer (`patch_status: patched`) and ZD-002 RedSun (`patch_status: unpatched`) — BleepingComputer headline link suggested "now exploited in attacks" but verbatim confirmation in source body limited to link-text only, not primary article body. Grader to verify the BleepingComputer source claim on ITW status with direct retrieval of the linked article (`bleepingcomputer.com/news/microsoft/critical-windows-netlogon-remote-code-execution-flaw-now-exploited-in-attacks/` is the only verified "now exploited in attacks" article surfaced — but that refers to **CVE-2026-41089 Netlogon**, already tracked, NOT BlueHammer/RedSun). **No verified state transition** for BlueHammer or RedSun in window.
- **CISA KEV additions 2026-06-09 — three CVEs:**
  - **CVE-2026-7473 Arista EOS** — see Trigger 6 ruling.
  - **CVE-2026-11645 Chrome V8** — already covered by 00:00 anti-noise lock.
  - **CVE-2026-20245 Cisco Catalyst SD-WAN Manager** — already tracked in corpus since 2026-05-15 (vuln dossier scaffolded at `threats/vulnerabilities/SD-Wan-Zero-Day-CVE-2026-20245/`). CVSS 7.8. **State transition to KEV-listed** for already-tracked CVE; vuln-tracker handoff for `_index_entry.yaml` `cisa_kev: false → true` update. CVSS below 9.0 trigger-1 threshold.
- **Cisco/Schneider/Siemens ICS Patch Tuesday — Siemens KACO Blueplanet Inverters + Schneider EcoStruxure Panel Server + Schneider Modicon Network Managed Switches** — ICS-OT vulnerabilities patched 2026-06-09 via CISA ICS-ADVs. No ITW exploitation. No A&D-prime victim. ICS-OT defensive-prioritization for morning brief Other Signal section.
- **Anthropic Claude Fable 5 release with twin Mythos 5 model (cyber safeguards lifted, vetted access only)** — vendor news; not threat-relevant for FLASH; defer to ad-hoc/weekly synthesis if model-misuse risk surfaces.
- **Unit 42 "Blinding the Watchmen" cloud-logging defense-evasion research** — generic research without actor attribution per direct retrieval. Defensive guidance only; not FLASH-tier.

## Source health observations

All A-grade sources successfully queried this sweep returned content within expected operational parameters. Persistent stale-status sources unchanged from prior sweep posture per `source-health.yaml`:

- `msrc` — feed parse error continues (known stale since 2026-05-29).
- `mandiant` — feedburner held stale; cloud.google.com alt-endpoint returns parse error in this sweep (consistent with prior sessions).
- `dragos`, `censys`, `urlscan`, `hibp`, AbuseIPDB/abuse.ch family (MCP-not-built), Twitter bridges — all unchanged stale per known posture.

No status changes proposed by this sweep. **Source-health.yaml not modified by this run.**

## Disposition

**1 FLASH candidate fired** (`raw-2026-06-10-flash-0600-001` — Unit 42 PAN-OS CVE-2026-0257 IR layer with new IOCs). Resurface eligibility evaluated; grader decision required on FLASH-vs-morning-brief-UPDATE disposition. CVSS strict hard-threshold reading FAILS trigger-1; corpus-precedent-aligned reading via FLASH-0007 PAN-OS CVE-2026-0300 precedent ELIGIBLE.

**No critical-override conditions met.** Quiet-hours queue-path applies if grader promotes.

**Recommendation to orchestrator:** *queue grader pass on 1 candidate*. Recommended grader disposition: morning-brief UPDATE block on existing CVE-2026-0257 finding chain unless full Unit 42 publication review reveals novel post-exploitation TTPs (option 1 FLASH-promotion path). The 8 ruled-out items are all morning-brief candidates of varying priority — vuln-tracker handoff queue should receive: (a) CVE-2026-7473 Arista EOS, (b) Microsoft June Patch Tuesday zero-days state transitions (YellowKey/GreenPlasma/MiniPlasma → patched, BlueHammer/RedSun status confirmation pending), (c) CVE-2026-20245 Cisco Catalyst SD-WAN KEV state transition, (d) Ivanti Sentry CVE-2026-10520/10523, (e) Fortinet FortiSandbox CVE-2026-25089, (f) ServiceNow active-exploitation disclosure CVE-pending.

## Operator action items surfaced (carry-over from 00:00 sweep + this sweep)

1. **`/new-actor Qilin`** — still recommended from 00:00 sweep; not actioned this sweep.
2. **Vuln-tracker handoff** — CVE-2026-0257 not yet in `_index.yaml` (full vuln dossier missing); plus new items above.
3. **Pattern note carry-over from 00:00:** 2nd LiteLLM CVE on KEV inside 31 days — still relevant.
4. **New pattern note:** PAN-OS CVE-2026-0257 has now received second A-grade IR-firm confirmation (Rapid7 → Unit 42 over 12 days); anti-noise rule 4 self-review threshold not breached (this is 2nd firing not 3rd), but worth flagging for weekly synthesis pattern observation on resurface velocity.
5. **Arista vendor-refusal-to-patch:** unusual KEV addition where vendor explicitly declines patch path. Defensive-tracking flag for any A&D-prime estate running affected Arista 7020R/7280R/R2/7500R/R2 series carrier-class routers — apply vendor-supplied mitigations or plan device retirement.

Orchestrator: log `flash_candidates_fired: 1` and `flash_candidates_ruled_out: 8` to Splunk; pass single candidate (`raw-2026-06-10-flash-0600-001`) to grader; trigger queue-write for catchup-post path **only if grader promotes**.
