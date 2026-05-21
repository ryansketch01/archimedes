---
raw_id: raw-2026-05-21-flash-1200-000-sentinel-sweep
collected_at: 2026-05-21T12:05:00-04:00
run_id: flash-sweep-20260521-120000
collection_mode: flash_sweep
sentinel: true
flash_candidate: false
test: false
source:
  source_yaml_id: archimedes-internal
  source_name: "Archimedes collector sentinel (clean sweep, anti-noise dedup applied)"
  source_url: null
  published_at: 2026-05-21T12:05:00-04:00
sweep_window:
  start: 2026-05-21T06:00:00-04:00
  end: 2026-05-21T12:00:00-04:00
sources_queried:
  - cisa-kev               # WebFetch known_exploited_vulnerabilities.json — 0 entries dated 2026-05-21; most recent KEV adds remain 2026-05-20 batch of 7 (anti-noise lock through 2026-05-21T16:00 EDT)
  - cisa-advisories        # all.xml fetch_feed 200, 30 items in feed, 0 in 6h window since 2026-05-21T06:00 EDT
  - nvd                    # No critical-window query this sweep — adjusted to spot-check approach given prior 6h window query at 00:00 + 06:00 sentinels returned no actionable A&D / tracked-actor CVEs
  - mstic                  # Microsoft Security Blog feed 200, last_modified 2026-05-20T23:01 GMT pre-window, 0 in-window items
  - unit42                 # feedburner 200, last_modified 2026-05-20T21:08 GMT pre-window, 0 in-window items
  - mandiant               # feedburner persistent 404 (now ~18+ consecutive sweeps; held healthy pending operator alt-endpoint decision per source-health.yaml notes)
  - cisco-talos            # blog.talosintelligence.com RSS feed 200, 0 in-window items
  - sentinel-one-labs      # sentinelone.com/labs/feed/ 200, last_modified 2026-05-21T15:09 GMT, 0 in-window items
  - welivesecurity         # ESET WeLiveSecurity feed 200, 0 in-window items
  - bleepingcomputer       # RSS feed 200, last_modified 2026-05-21T15:51 GMT, 6 in-window items — Apple App Store fraud (non-threat-intel, DISCARDED); Crypto Drainer sponsored (DISCARDED); Chinese hackers Calypso/Red Lamassu Showboat/JFMBackdoor telecoms (Bill Toulas 14:00 GMT — NOT a tracked actor, telecoms targeting NOT A&D; evaluated against Trigger 5 → fails; DISCARDED per Mode 1); Cisco Secure Workload CVE-2026-20223 max-severity (Sergiu Gatlan 13:58 GMT — Cisco PSIRT "no evidence of exploitation in the wild," anti-noise dedup'd against 2026-05-20 afternoon brief finding-2026-05-20-0001); First VPN seizure (DISCARDED — law enforcement, no actor attribution to roster); Flipper One hardware (DISCARDED — non-threat-intel)
  - thehackernews          # feedburner 200, last_modified 2026-05-21T15:55 GMT, 4 in-window items — Showboat Linux Telecom (10:55 / 14:17 GMT — Calypso/Red Lamassu via Lumen Black Lotus Labs + Kaspersky EvaRAT + PwC Threat Intelligence; telecoms APAC+Middle East not A&D; DISCARDED); ThreatsDay Bulletin aggregator (DISCARDED — multi-topic synthesis, no single-topic FLASH candidate); Microsoft Defender pair anti-noise dedup (KEV-7 batch lock); Identity-attack-path opinion (DISCARDED — editorial, no specific CVE / actor / IOC)
  - securityweek           # RSS feed 200, last_modified 2026-05-21T12:04 GMT, 5 in-window items — Cisco Secure Workload CVE-2026-20223 (Ionut Arghire 12:04 GMT — anti-noise dedup'd against 2026-05-20 afternoon brief); Ocean email startup (DISCARDED — funding announcement); Apple App Store (DISCARDED — non-threat-intel); Drupal SA-CORE-2026-004 CVE-2026-9082 (Eduard Kovacs 10:58 GMT — anti-noise dedup'd against 2026-05-21 morning brief finding-2026-05-21-0004); Socket funding (DISCARDED — funding announcement)
  - cybersecuritydive      # feeds/news/ 200, last_modified 2026-05-21T15:00 GMT, 2 in-window items — Grafana Labs links GitHub breach to TanStack (David Jones 14:49 GMT — same campaign as morning brief finding-2026-05-21-0002 and finding-2026-05-21-0007; Grafana's own self-disclosure dated 2026-05-19 pre-window; BleepingComputer covered Grafana on 2026-05-20 with TeamPCP attribution; Cybersecurity Dive is media-relay catch-up; anti-noise dedup'd against morning brief TeamPCP/TanStack chain); CISA KEV nomination form (Eric Geller 15:00 GMT — procedural policy article, no new CVE / exploitation, DISCARDED)
  - therecord              # feed 200, 1 in-window item — UK cybercrime law reform critique (14:47 GMT, policy/legislative opinion, DISCARDED — no specific CVE / actor / IOC)
  - sans-isc               # RSS feed 200, last_modified 2026-05-21T15:59 GMT, 1 in-window item — Selective HTTP Proxying in Linux (13:34 GMT, defensive-tooling diary, DISCARDED — no actor / CVE / IOC)
  - krebs                  # feed 200, last_modified 2026-05-19T14:19 GMT pre-window, 0 in-window items
  - lumen-black-lotus-labs # Lumen blog 301 redirect / Wiz / Dragos feeds 404 — Lumen Showboat primary blog URL inferred but not directly retrieved; relayed via BleepingComputer + Hacker News (both retrieved)
  - splunk-first-party     # archimedes + defenseclaw_local indexes -24h, 0 non-self events; only archimedes:scheduler (16 events) + archimedes:flash (1 event) self-telemetry. 52nd consecutive dormant non-self sweep
trigger_evaluation:
  trigger_1_critical_cve_exploited:
    fired: false
    reason: |
      Two evaluated candidates in 6h window — both ANTI-NOISE DEDUP or
      fail active-exploitation prong:

      (a) Cisco Secure Workload CVE-2026-20223 CVSS 10.0 (BleepingComputer
      Sergiu Gatlan 13:58 GMT + SecurityWeek Ionut Arghire 12:04 GMT).
      Cisco PSIRT explicitly states "has not found evidence that the
      vulnerability has been exploited in the wild before publishing this
      week's advisory." FAILS Trigger 1 on active-exploitation prong.
      Additionally, this CVE was already covered in the 2026-05-20
      afternoon brief (finding-2026-05-20-0001) — anti-noise lock active
      on Cisco Secure Workload CVE-2026-20223 topic. Today's coverage is
      media-relay catch-up on yesterday's Cisco PSIRT advisory; no new
      exploitation status change.

      (b) Microsoft Defender pair CVE-2026-41091 (CWE-59 LPE) + CVE-2026-
      45498 (DoS). Three in-window media surfaces continuing yesterday's
      KEV-7 batch coverage. Anti-noise lock active through 2026-05-21T16:
      00:00 EDT per 2026-05-20 afternoon brief frontmatter; also explicitly
      covered in 2026-05-21 morning brief as UPDATE on finding-2026-05-
      20-0005. DEDUP.

      No A-grade source attests active in-the-wild exploitation of any
      CVE in window that is NOT already inside an existing anti-noise
      lock.
  trigger_2_tracked_actor_attribution:
    fired: false
    reason: |
      In-window items mentioning tracked actors:

      (a) Cybersecurity Dive "Grafana Labs links GitHub environment
      breach to TanStack npm supply chain attack" (David Jones 14:49 GMT).
      The article names TeamPCP attribution per the journalist's editorial
      framing: "A threat group tracked as Team PCP is linked to the Mini
      Shai-Hulud attack." HOWEVER, this attribution is carry-forward of
      prior coverage: (1) Grafana Labs' own self-disclosure blog post is
      dated 2026-05-19 (PRE-window) and does NOT name TeamPCP — Grafana
      uses "cybercrime group" / "bad actor" only; (2) BleepingComputer
      covered the Grafana incident on 2026-05-20 with TeamPCP attribution
      framing ("In the ongoing Shai-Hulud malware campaign attributed to
      TeamPCP hackers, dozens of TanStack packages infected..."); (3) the
      2026-05-21 morning brief finding-2026-05-21-0002 (Hard Rule 2
      framing) and finding-2026-05-21-0007 already name Grafana Labs as
      one of three secondary victims (OpenAI, Mistral AI, Grafana Labs)
      in the TanStack supply-chain chain. No NEW TeamPCP attribution
      surface in window — same self-claim on Breached + media-relay
      framing; single-source veto on attribution layer unchanged from
      finding-2026-05-20-FLASH-0001. Anti-noise lock teampcp-github-
      internal-repos-breach-via-vscode-extension-2026-05-20 EXPIRED at
      2026-05-21T06:08:00-04:00 (5h57m before this sweep), but the
      morning brief 2026-05-21 (08:00 EDT) carries the topic forward as
      UPDATE on finding-2026-05-20-FLASH-0001 + creates finding-2026-
      05-21-0002 cluster — establishing a NEW anti-noise lock on the
      same topic through 2026-05-22T08:00 EDT. The Grafana Labs detail
      strengthens the secondary-victim list (now substantiated by
      Grafana's own self-disclosure rather than only Nx Team relay) but
      does NOT introduce a new attribution surface. DEDUP.

      (b) BleepingComputer "Chinese hackers target telcos with new Linux,
      Windows malware" (Bill Toulas 14:00 GMT) + The Hacker News "Showboat
      Linux Malware Hits Middle East Telecom" (14:17 GMT). Both surfaces
      relay Lumen Black Lotus Labs + PwC Threat Intelligence research on
      a China-nexus threat group named **Calypso / Red Lamassu** (with
      Kaspersky tracking the artifact as EvaRAT). Calypso/Red Lamassu is
      NOT in the 24-actor _roster.yaml (TeamPCP, Stardust Chollima,
      Lazarus, UNC1549, GlassWorm, APT28, Sandworm, Volt Typhoon, APT29,
      Salt Typhoon, Charming Kitten, Miyako, Scattered Spider, Handala
      Hack, LockBit, REvil, APT40, Cl0p, APT41, BlackCat/ALPHV, Payouts
      King, MuddyWater, APT34, APT37). The article identifies Chengdu /
      Sichuan-province correlations and a campaign active since at least
      mid-2022. FAILS Trigger 2 on tracked-actor prong — Calypso/Red
      Lamassu is not in the roster. (NOTE: actor-profiler may flag
      Calypso/Red Lamassu for /new-actor consideration based on
      sustained 4-year China-nexus telecoms campaign with multiple
      tracked-vendor corroboration; deferred to roster review, NOT a
      FLASH trigger.)

      No other in-window items mention any of the 24 actors in
      _roster.yaml.
  trigger_3_first_party_ioc_hit:
    fired: false
    reason: |
      Splunk query on archimedes + defenseclaw_local indexes (-24h,
      excluding archimedes:* self-telemetry) returned 0 events. Only
      Archimedes self-telemetry visible in the index (archimedes:
      scheduler 16 events, archimedes:flash 1 event). 52nd consecutive
      dormant non-self sweep at this run. Per Hard Rule 8: silence is
      neither confirming nor disconfirming.
  trigger_4_tracked_actor_ttp_change:
    fired: false
    reason: |
      No A/B-grade source documents new tooling, targeting, or
      infrastructure class attributable to a tracked actor in the 6h
      window beyond what is already inside anti-noise locks. Mandiant
      (feedburner 404 pattern persists), Unit 42 (0 in-window — last
      modified 2026-05-20T21:08 GMT), MSTIC (0 in-window — last
      modified 2026-05-20T23:01 GMT), CrowdStrike (0 in-window),
      SentinelLabs (0 in-window), Cisco Talos (0 in-window), ESET
      WeLiveSecurity (0 in-window). The TanStack/Nx Console/TeamPCP
      campaign-chain morning-brief coverage (finding-2026-05-21-0007
      MSTIC + Unit 42 novel-TTPs cluster) establishes an anti-noise
      lock through 2026-05-22T08:00 EDT covering Bun runtime, /proc
      scanning, Runner.Worker memory scraping, 1Password CLI 2FA
      bypass, K8s SA tokens, AWS Secrets / HashiCorp Vault enumeration,
      npm OIDC abuse, SLSA forgery, PBKDF2 obfuscation. Grafana Labs
      self-disclosure detail (missed workflow token rotation) is within
      this existing campaign chain — not a NEW TTP class. The Showboat
      Linux post-exploitation framework + JFMBackdoor (Calypso/Red
      Lamassu) is a Pastebin-dead-drop SOCKS5 proxy implant — novel
      tooling, but attributed to a non-roster actor; FAILS Trigger 4
      on tracked-actor prong.
  trigger_5_ad_sector_campaign:
    fired: false
    reason: |
      No in-window item describes an active multi-victim campaign
      explicitly targeting A&D primes (Lockheed Martin, Boeing, RTX,
      Northrop Grumman, General Dynamics, BAE Systems, L3Harris, Leidos,
      SAIC, Thales, GE Aerospace, Safran, Honeywell Aerospace, Airbus,
      Elbit Systems). Three near-candidates evaluated and rejected:

      (a) Showboat / JFMBackdoor / Calypso (Red Lamassu) — Chinese-
      nexus campaign documented as multi-victim across telecoms in Asia
      Pacific, Middle East, Afghanistan ISP, Azerbaijan, US, Ukraine.
      FAILS Trigger 5: sector is TELECOMS, not A&D. No A&D-prime named
      victim. (Telecoms is sector-adjacent — A&D primes often rely on
      telecoms providers, but Trigger 5 requires direct A&D-sector or
      watchlist-company victim naming. Structural-indirect telecoms
      exposure does not satisfy.)

      (b) Grafana Labs / TanStack chain — campaign continues to be
      multi-victim (GitHub-corp, OpenAI, Mistral AI, Grafana Labs,
      TanStack maintainers, prior 3,800-internal-repo breach), but no
      A&D-prime named victim. Structural-indirect SDLC exposure across
      Tier-1 / Tier-2 estates is the A&D relevance, NOT direct
      targeting. Already absorbed by morning brief.

      (c) Cisco Secure Workload CVE-2026-20223 — no exploitation in the
      wild, no campaign, no victims. Cisco PSIRT advisory is precautionary
      patch wave. Already in 2026-05-20 afternoon brief.
  trigger_6_zero_day_no_patch:
    fired: false
    reason: |
      All in-window CVE candidates ship WITH patches:

      (a) Cisco Secure Workload CVE-2026-20223 — patched in fixed
      releases 3.10.8.3 + 4.0.3.17 per Cisco PSIRT advisory; cloud
      deployments already patched. Not zero-day-no-patch class.

      (b) Microsoft Defender CVE-2026-41091 + CVE-2026-45498 — both
      patched 2026-05-20 (Engine 1.1.26040.8, Antimalware Platform
      4.18.26040.7). Already inside KEV-7 anti-noise lock.

      (c) Drupal SA-CORE-2026-004 / CVE-2026-9082 — patches available
      at disclosure; already in 2026-05-21 morning brief finding-2026-
      05-21-0004.

      No zero-day-no-patch candidate in window.
match_reason:
  watchlist: []
  actors:
    - TeamPCP                  # dedup'd via morning brief 2026-05-21 finding-0002 / 0007 (anti-noise lock through 2026-05-22T08:00 EDT)
  vulnerabilities:
    - CVE-2026-20223           # dedup'd via 2026-05-20 afternoon brief finding-2026-05-20-0001
    - CVE-2026-41091           # dedup'd via KEV-7 batch lock (expires 2026-05-21T16:00 EDT)
    - CVE-2026-45498           # dedup'd via same KEV-7 batch lock
    - CVE-2026-9082            # dedup'd via 2026-05-21 morning brief finding-2026-05-21-0004
  keywords:
    - cisco_secure_workload
    - max_severity
    - microsoft_defender
    - kev
    - grafana_labs_self_disclosure
    - tanstack
    - npm_supply_chain
    - nx_console
    - showboat_calypso_red_lamassu
    - jfmbackdoor
    - china_nexus_telecoms_apt
triage_tags:
  - flash_sentinel
  - clean_sweep
  - sentinel_log_only
  - anti_noise_absorbed_cisco_workload_cve_2026_20223_2026_05_20_afternoon_lock
  - anti_noise_absorbed_kev_7_batch_microsoft_defender_pair_2026_05_20_afternoon_lock
  - anti_noise_absorbed_teampcp_tanstack_chain_2026_05_21_morning_lock_findings_0002_0007
  - anti_noise_absorbed_drupal_cve_2026_9082_2026_05_21_morning_lock_finding_0004
  - trigger_1_evaluated_failed_cisco_no_itw_plus_dedup_kev_7_batch
  - trigger_2_evaluated_failed_grafana_carry_forward_attribution_calypso_non_roster
  - trigger_4_evaluated_failed_showboat_calypso_non_roster_no_new_roster_ttp
  - trigger_5_evaluated_failed_showboat_telecoms_not_ad_no_ad_prime_named
  - splunk_first_party_zero_hits_52nd_consecutive_dormant_sweep
  - quiet_hours_inactive_post_0900_pre_2100_critical_override_does_not_apply_for_other_reasons
  - calypso_red_lamassu_lumen_pwc_potential_new_actor_candidate_deferred_to_roster_review
iocs_extracted: false
iocs_count: 0
text_word_count: 0
promoted: false
ttl_expires_at: 2026-08-19T12:05:00-04:00
---

# FLASH alert sweep sentinel — 2026-05-21 12:00 EDT cycle (clean, 0 of 6 triggers fired)

Per FLASH-POLICY.md, the 12:00 EDT scheduled sweep fired clean against all
six trigger conditions across a representative source set (CISA KEV +
CISA advisories all.xml + MSTIC + Unit 42 + Mandiant + Cisco Talos +
SentinelLabs + WeLiveSecurity + BleepingComputer + The Hacker News +
SecurityWeek + Cybersecurity Dive + The Record + SANS ISC + Krebs +
Splunk first-party).

Sweep window: 2026-05-21T06:00 → 2026-05-21T12:00 EDT.

## Why no FLASH ships

See `trigger_evaluation` block in frontmatter. Three categorically
distinct candidate items evaluated in window — all dedup'd or
categorically off-filter:

### Candidate A — Cisco Secure Workload CVE-2026-20223 (max-severity / CVSS 10.0)

BleepingComputer (Sergiu Gatlan, 13:58 GMT) and SecurityWeek (Ionut
Arghire, 12:04 GMT) both relay Cisco PSIRT's Wednesday advisory on
the maximum-severity REST API authentication-bypass flaw in Cisco
Secure Workload that grants Site Admin privileges. Two distinct
disqualifications for Trigger 1:

1. **No active exploitation.** Cisco PSIRT explicitly states "has not
   found evidence that the vulnerability has been exploited in the
   wild before publishing this week's advisory." Trigger 1 requires
   "confirmed active exploitation (not PoC, not theoretical)" — this
   CVE fails that prong.

2. **Anti-noise dedup with 2026-05-20 afternoon brief.** Finding
   finding-2026-05-20-0001 in yesterday's afternoon brief is the
   primary Archimedes-corpus surface for CVE-2026-20223; today's
   media-relay coverage is catch-up on yesterday's Cisco PSIRT
   advisory release. No new exploitation-status change, no new IOCs,
   no actor attribution. Resurface conditions per FLASH anti-noise
   rule 1 NOT met.

### Candidate B — Grafana Labs / TanStack / TeamPCP carry-forward (Cybersecurity Dive)

Cybersecurity Dive (David Jones, 14:49 GMT) carries Grafana Labs'
self-disclosure on the GitHub-environment breach linked to the
TanStack npm supply-chain attack. Three sub-disqualifications:

1. **Grafana's own self-disclosure pre-dates the window.** Grafana
   Labs published their security update blog post on 2026-05-19
   (PRE-window — two days before this sweep). Their post does NOT
   name TeamPCP — Grafana uses "cybercrime group" / "bad actor"
   framing only.

2. **TeamPCP attribution is carry-forward, not new.** BleepingComputer
   covered the Grafana incident on 2026-05-20 with TeamPCP framing
   ("In the ongoing Shai-Hulud malware campaign attributed to TeamPCP
   hackers..."). Cybersecurity Dive's "A threat group tracked as Team
   PCP is linked to the Mini Shai-Hulud attack" is editorial framing
   consistent with prior coverage, not Grafana-originated attribution.
   Per INTEL-GRADING independence test, the attribution layer remains
   single-source-veto'd via the TeamPCP self-claim on Breached
   (relayed by multiple B-grade media). No new TeamPCP attribution
   surface.

3. **Anti-noise dedup with 2026-05-21 morning brief.** Findings
   finding-2026-05-21-0002 (GitHub Nx Console confirmation) and
   finding-2026-05-21-0007 (MSTIC + Unit 42 Mini Shai-Hulud @antv
   TTPs) already name Grafana Labs as one of three secondary victims
   (OpenAI, Mistral AI, Grafana Labs) in the same TanStack chain.
   The Grafana detail (missed workflow token rotation enabling the
   GitHub breach) refines the campaign-chain mechanism layer but is
   within the existing anti-noise lock through 2026-05-22T08:00 EDT.

### Candidate C — Showboat / JFMBackdoor / Calypso (Red Lamassu) China-nexus telecoms

BleepingComputer (Bill Toulas, 14:00 GMT) and The Hacker News (14:17
GMT) relay a Lumen Black Lotus Labs + PwC Threat Intelligence
research disclosure on a China-nexus threat group named **Calypso**
(also tracked as Red Lamassu), with Kaspersky tracking the artifact
as EvaRAT. The campaign deploys two implants: **Showboat** (Linux
modular post-exploitation framework, SOCKS5 proxy + reverse shell +
file transfer + Pastebin "dead drop" for process hiding) and
**JFMBackdoor** (Windows DLL-sideloading variant via fltMC.exe +
FLTLIB.dll). Active since at least mid-2022 against telecommunications
providers in Asia Pacific, Middle East, Afghanistan (ISP), Azerbaijan,
US, and Ukraine. Chengdu / Sichuan-province operator correlations.

Two disqualifications for Trigger 5 (A&D-sector campaign):

1. **Wrong sector.** Sustained 4-year campaign explicitly targeting
   TELECOMS, not A&D. Trigger 5 requires "explicitly targeting
   aerospace, defense, or watchlist companies." A&D-prime telecoms
   dependency is structural-indirect (primes consume carrier services)
   but does not satisfy the direct-targeting prong.

2. **Non-roster actor.** Calypso / Red Lamassu is NOT in the 24-actor
   _roster.yaml. Trigger 2 (tracked-actor attribution) fails on this
   prong. Trigger 4 (tracked-actor TTP change) also fails for the same
   reason — even though Showboat's Pastebin-dead-drop SOCKS5-proxy
   architecture is novel tooling per the Lumen research, it is
   attributed to a non-roster actor.

   **Note for actor-profiler review:** Calypso / Red Lamassu meets
   several actor-profiler criteria for /new-actor consideration —
   sustained multi-year campaign (since mid-2022), multi-A-grade
   source corroboration (Lumen Black Lotus Labs + PwC + Kaspersky
   independent tracking), explicit nation-state attribution (China-
   nexus, Chengdu / Sichuan-province correlations), novel tooling.
   Deferred to actor-profiler roster review on next /update-tracking
   cycle, NOT a FLASH trigger.

## Anti-noise lock collisions and current lock state

Four anti-noise locks active at sweep time, all colliding with in-
window candidate material:

1. **Cisco Secure Workload CVE-2026-20223 (2026-05-20 afternoon
   brief, finding-2026-05-20-0001)** — covers the max-severity REST
   API auth bypass. Lock active through 2026-05-21T16:00:00-04:00
   (KEV-7 batch lock anchor). Two in-window items (BleepingComputer,
   SecurityWeek) inside this lock. Dedup.

2. **KEV-7 batch lock (2026-05-20 afternoon brief, finding-2026-05-20-
   0005)** — covers CVE-2026-41091, CVE-2026-45498, CVE-2008-4250,
   CVE-2009-1537, CVE-2009-3459, CVE-2010-0249, CVE-2010-0806. Lock
   active through 2026-05-21T16:00:00-04:00. No in-window items
   crossing this lock today (the morning brief already absorbed all
   yesterday's Defender pair relays).

3. **TeamPCP / TanStack / Nx Console campaign chain (2026-05-21
   morning brief, finding-2026-05-21-0002 + finding-2026-05-21-0007)**
   — supersedes the prior teampcp-github-internal-repos-breach-via-
   vscode-extension-2026-05-20 lock (expired 06:08 EDT today). New
   morning-brief lock active through 2026-05-22T08:00 EDT. Three in-
   window items (Cybersecurity Dive Grafana Labs relay, plus prior-
   day BleepingComputer/Hacker News coverage already absorbed by
   morning brief) inside this lock. Dedup.

4. **Drupal CVE-2026-9082 SA-CORE-2026-004 (2026-05-21 morning brief,
   finding-2026-05-21-0004)** — covers the PostgreSQL-only anonymous-
   attacker SQLi (CVSS 6.5, Drupal Highly Critical 20/25). Lock active
   through 2026-05-22T08:00 EDT. One in-window item (SecurityWeek
   Eduard Kovacs 10:58 GMT) inside this lock. Dedup.

## Items DISCARDED per Mode 1 (not anti-noise dedup — categorically off-filter)

- **Apple App Store fraud blocking ($11B over 6 years)** (BleepingComputer
  Sergiu Gatlan + SecurityWeek Ionut Arghire 15:11 GMT / 11:17 GMT) —
  non-threat-intel feature article, no specific CVE / actor / IOC.
- **Crypto Drainer Lucifer DaaS** (BleepingComputer sponsored content
  by Flare 14:00 GMT) — sponsored content, no FLASH-tier signal.
- **First VPN service seizure** (BleepingComputer Bill Toulas 13:09
  GMT) — law-enforcement takedown, no actor attribution to roster, no
  CVE, structural-context observation only.
- **Flipper One open-Linux platform community project** (BleepingComputer
  Bill Toulas 11:00 GMT) — hardware product development, no threat
  intelligence content.
- **ThreatsDay Bulletin (Linux rootkits, router 0-day, AI intrusions,
  scam kits, 25 stories)** (The Hacker News 11:52 GMT) — multi-topic
  weekly aggregator, no single-topic FLASH candidate; individual
  stories evaluated independently where significant; bulletin format
  not actionable as FLASH.
- **"When Identity is the Attack Path"** (The Hacker News 10:30 GMT) —
  editorial / cloud-IAM hardening commentary, no specific CVE / actor
  / IOC.
- **Ocean agentic email security startup $28M funding** (SecurityWeek
  11:45 GMT) — funding announcement.
- **Socket $60M / $1B valuation** (SecurityWeek Ionut Arghire 10:32 GMT)
  — funding announcement; tangentially relevant (Socket is supply-chain
  security research vendor cited in prior TeamPCP/VT-006 coverage), but
  no new research disclosure.
- **CISA KEV nomination form** (Cybersecurity Dive Eric Geller 15:00 GMT)
  — CISA procedural / policy article on community CVE-exploitation
  nomination workflow; no specific CVE or exploitation surface.
- **UK cybercrime law reform critique** (The Record 14:47 GMT) —
  legislative / policy commentary, no specific CVE / actor / IOC.
- **Selective HTTP Proxying in Linux** (SANS ISC 13:34 GMT) —
  defensive-tooling diary on reverse engineering / debugging
  technique; no actor / CVE / IOC.

## Splunk first-party silence

52nd consecutive dormant non-self sweep. archimedes + defenseclaw_local
indexes returned 0 events for the -24h window (excluding archimedes:*
self-telemetry — 16 archimedes:scheduler events, 1 archimedes:flash
event from automation). Hard Rule 8 framing: this is neither confirming
nor disconfirming.

## Quiet hours posture

Current time 12:05 EDT is OUTSIDE quiet hours (FLASH-POLICY active
hours 09:00–21:00 EDT). If a trigger had fired with WEP ≥ "likely"
and B2+ grade, the FLASH would have been eligible for immediate
posting to `#flash-alerts`. Zero triggers fired → sentinel-log-only
path; no queue entry; no Discord post.

The critical-override path (CVSS 10.0 + active exploitation +
tracked actor + A&D watchlist entity) does NOT apply today regardless
— for the only CVSS 10.0 candidate in window (Cisco Secure Workload
CVE-2026-20223), Cisco PSIRT explicitly disclaims active exploitation
(FAIL condition 2). No A&D watchlist entity named as target across
any in-window item (FAIL condition 4). For the TeamPCP / TanStack /
Grafana surface, no CVE assigned (FAIL condition 1) and no A&D
watchlist entity (FAIL condition 4).

## Source health changes

None observed this sweep. All queried sources behaved consistent with
their entrenched patterns documented in `source-health.yaml`:

- **mandiant feedburner**: 404 pattern persists (now ~18+ consecutive
  sweeps); still held healthy pending operator alt-endpoint decision.
- **mstic, unit42**: both reachable, 0 in-window items (last modified
  pre-window per RSS bridge last_modified headers).
- **sentinelone-labs, cisco-talos, welivesecurity**: all reachable, 0
  in-window items.
- **bleepingcomputer, thehackernews, securityweek**: all reachable,
  multiple in-window items — anti-noise dedup applied or off-filter
  per Mode 1 (see DISCARDED list above).
- **cybersecuritydive**: reachable; 2 in-window items both dedup'd or
  off-filter.
- **therecord, sans-isc**: both reachable, 1 in-window item each, both
  off-filter.
- **krebs**: reachable, 0 in-window items (last modified 2026-05-19 pre-
  window).
- **cisa-kev**: WebFetch JSON 200, 0 entries dated 2026-05-21 (5 most
  recent dateAdded values: 2026-05-20 [7 entries], 2026-05-15 [1],
  2026-05-14 [1], 2026-05-08 [1], 2026-05-07 [1]).
- **cisa-advisories**: all.xml fetch_feed 200, 0 in 6h window.
- **splunk first-party**: reachable, 0 non-self events in -24h window.

No source-health.yaml runtime field updates required this sweep; the
operator-set `notes:` blocks on each entry are preserved.

## Handoff items for 16:00 afternoon brief composer (NOT FLASH; UPDATE-block or fresh-finding candidates)

The briefer for 2026-05-21 16:00 afternoon brief should consider these
as candidates layered onto existing findings or as fresh findings —
not FLASH-tier:

1. **Grafana Labs self-disclosure detail (missed workflow token rotation)**
   — UPDATE on finding-2026-05-21-0002 / finding-2026-05-21-0007. Grafana
   Labs' own May 19 blog post explicitly identifies the missed GitHub
   workflow token rotation as the mechanism that enabled the GitHub-
   environment breach following initial TanStack detection on May 11
   (extortion May 16). Refines the mechanism layer of the secondary-
   victim chain without changing attribution. Grafana refused extortion;
   incident bounded to GitHub source code, no customer production
   systems compromised.

2. **Cisco Secure Workload CVE-2026-20223 media-relay catch-up wave**
   — OPTIONAL UPDATE on finding-2026-05-20-0001. BleepingComputer +
   SecurityWeek same-day catch-up confirms no exploitation-status
   change since yesterday's Cisco PSIRT advisory. Briefer judgment on
   whether to surface as UPDATE block (no new substance) or omit (status
   quo).

3. **Calypso / Red Lamassu (China-nexus telecoms APT) — Showboat +
   JFMBackdoor disclosure** — FRESH FINDING candidate for the afternoon
   brief OR /new-actor candidate for actor-profiler review. A2-class
   research disclosure from Lumen Black Lotus Labs + PwC Threat
   Intelligence on a 4-year-active China-nexus campaign with novel
   Pastebin-dead-drop tooling architecture. A&D relevance is STRUCTURAL-
   INDIRECT (telecoms-provider dependency by A&D primes for carrier
   services + supply-chain considerations), NOT direct A&D targeting.
   Briefer/actor-profiler judgment on inclusion + threshold for
   /new-actor scaffolding.

## Anti-noise distinction from recent FLASHes / briefs / sentinels

- **flash-sweep-20260521-000000 (00:00 sentinel, 0 triggers)** — same
  upstream sentinel pattern; same general dedup posture.
- **flash-sweep-20260521-060000 (06:00 sentinel, 0 triggers)** — covered
  the prior 6h window. KEV-7 batch + TeamPCP/Nx Console anti-noise locks
  documented. Morning brief 2026-05-21 absorbed all candidate material.
- **2026-05-21 morning brief (08:00 EDT)** — covers TeamPCP/TanStack/Nx
  Console campaign chain (findings 0002 + 0007), Drupal CVE-2026-9082
  (0004), Microsoft Defender pair UPDATE (0001), SonicWall CVE-2024-12802
  ReliaQuest single-source ITW claim (0006), Unbound CVE-2026-42960 +
  CVE-2026-33278 dual criticals (0005), NVIDIA TRT-LLM CVE-2025-33255 +
  CVE-2026-24142 deserialization cluster (0003). All locks active
  through 2026-05-22T08:00 EDT.
- **2026-05-20 afternoon brief (16:00 EDT)** — covers Cisco Secure
  Workload CVE-2026-20223 (finding-2026-05-20-0001) + CISA KEV +7
  batch including Microsoft Defender pair (finding-2026-05-20-0005).
  Both locks active through 2026-05-21T16:00 EDT.
- **flash-2026-05-20-1800 (ad-hoc sweep, 0 triggers + 4 handoff items)**
  — distinct window; subsequent 18h period now covered by midnight +
  dawn + this sentinel.

## Extraction notes

- Language: en
- Article type: sentinel
- Raw IOC extraction invoked: no (sentinel — no payload content to extract; all in-window candidate items absorbed by existing anti-noise locks or categorically off-filter, no new IOCs surfaced)
- Run mode: flash_sweep (Mode 2)
- Output mode: sentinel log only (0 of 6 triggers fired)
- Anti-noise lock collisions: 4 active locks (Cisco Workload CVE-2026-20223, KEV-7 batch through 16:00 EDT; TeamPCP/TanStack/Nx Console chain through 2026-05-22T08:00 EDT; Drupal CVE-2026-9082 through 2026-05-22T08:00 EDT)
- Notable non-FLASH actor-profiler handoff: Calypso / Red Lamassu (China-nexus telecoms APT, Lumen Black Lotus Labs + PwC + Kaspersky multi-A-grade corroboration since mid-2022) flagged for actor-profiler /new-actor consideration on next /update-tracking cycle
