---
raw_id: raw-2026-05-13-flash-1800-000
collected_at: 2026-05-13T18:10:00-04:00
run_id: flash-sweep-20260513-180000
collection_mode: flash_sweep
sweep_type: flash
sweep_time: 2026-05-13T18:00:00-04:00
time_window_start: 2026-05-13T14:00:00-04:00    # extended from standard 6h to 4h to capture wires that broke during afternoon-brief composition (16:00 brief shipped covering 14:00 cut-off)
time_window_end: 2026-05-13T18:00:00-04:00
test: false
quiet_hours_active: false                       # 18:00 EDT inside 09:00-21:00 EDT active window
sources_queried:
  - bleepingcomputer       # RSS via fetch_feed — status 200, last_modified 2026-05-13T21:59:33 GMT (17:59 EDT in-window), 2 items in 4h window. (1) "Iranian hackers targeted major South Korean electronics maker" (Bill Toulas, 17:59 EDT in-window) — Symantec Threat Hunter Team primary relay; MuddyWater attribution; FLASH CANDIDATE matching Trigger 2 + Trigger 4. RAW-SIGNALED at flash-1800-001. (2) "New critical Exim mailer flaw allows remote code execution" (Bill Toulas, 16:23 EDT in-window) — CVE-2026-45185 Exim 4.97-4.99.2 UAF in TLS shutdown during BDAT chunking; PATCHED 2026-05-12 in Exim 4.99.3; XBOW researcher Federico Kirschbaum + AI/LLM tooling narrative; NO in-the-wild exploitation per article ("I don't think LLMs alone are quite ready to write exploits"); CVSS not assigned in article. DISCARDED — Trigger 1 fails on active_exploitation false (PoC-only); Trigger 6 fails on patch_status patched (vendor patch shipped one day before disclosure); also related-but-distinct from CVE-2026-40364 Exim BDAT cohort already in 2026-05-12 corpus (anti-noise consideration secondary; primary discard reason is no qualifying trigger).
  - securityweek           # RSS via fetch_feed — status 200, last_modified 2026-05-13T17:13:41 GMT (13:13 EDT pre-window), 0 items in 4h window after since-filter.
  - the-record             # RSS via fetch_feed — status 200, 1 item in 4h window. (1) "Alleged Dream Market admin arrested in Germany after US indictment" (15:54 EDT in-window) — historical dark-web-marketplace law-enforcement action (Owe Martin Andresen, 2013-2019 Dream Market admin, money laundering charges ~$2M cryptocurrency + gold bars); NO tracked actor, NO A&D, NO CVE, NO threat-intel. DISCARDED per Mode 1.
  - rapid7                 # RSS via fetch_feed (rapid7.com/blog/rss/) — status 200, last_modified 2026-05-13T21:46:30 GMT (17:46 EDT in-window from feed-server activity), 0 items in 4h window after since-filter.
  - krebs                  # RSS via fetch_feed — status 200, last_modified 2026-05-13T21:59:53 GMT (17:59 EDT in-window from feed-server activity), 0 items in 4h window after since-filter.
  - mstic                  # RSS via fetch_feed (microsoft.com/en-us/security/blog/feed/) — status 200, last_modified 2026-05-13T18:30:58 GMT (14:30 EDT in-window from feed-server activity), 0 items in 4h window after since-filter.
  - cisa-advisories        # Implicit via 2026-05-13 14:30 FLASH coverage at +3.5h ago; not re-invoked this 4h-narrow sweep (FLASH-fast scope; CISA advisories all.xml has been zero-in-window for 4+ consecutive sweeps and Wednesday-Thursday CISA cadence typically posts Patch Tuesday batch after 18:00 EDT or next-day).
  - cisa-kev               # Implicit via 2026-05-13 14:30 FLASH coverage; not re-invoked this narrow sweep. KEV ranking unchanged at 14:30; CVE-2026-42208 BerriAI LiteLLM remains most recent KEV entry (2026-05-08).
  - nvd                    # Implicit via 14:30 FLASH coverage; not re-invoked this narrow sweep. KEV-quiet pattern + no fresh A&D-relevant CVE-class indicators surfaced in 4h-window RSS / Hacker News sweeps to warrant NVD lastModified verification.
  - hacker-news            # NOT re-invoked this 4h-narrow sweep — top-of-list rotation cadence on thehackernews.com is roughly 4-8h between new-post additions; 14:30 FLASH already covered the 2026-05-13-dated content surface (Bitdefender FamousSparrow, MDASH AI, Patch Tuesday 138 CVEs, GemStuffer, Android Intrusion Logging). FLASH-fast scope kept to RSS primaries this narrow sweep.
  - sentinelone-labs       # Implicit via 14:30 FLASH coverage; not re-invoked this narrow sweep. SentinelOne Labs zero-in-window across 4 consecutive sweeps today.
  - sophos                 # Implicit via 14:30 FLASH coverage; not re-invoked. Sophos News cadence typically multi-day; no zero-in-window pattern break expected in 4h window after 14:30 sweep zero-in-window result.
  - unit42                 # Implicit via 14:30 FLASH coverage; not re-invoked. Unit42 cadence multi-day.
  - cloud-google-blog-mandiant  # NOT re-invoked this narrow sweep — Mandiant feedburner 22nd-consecutive 404 pattern fully entrenched; cloud.google.com index page WebFetch at 14:30 surfaced same top-8 visible titles as 2026-05-12 sweeps. FLASH-fast scope kept to active RSS primaries; Mandiant alt-endpoint discovery still pending operator action.
  - splunk-archimedes      # search index=archimedes OR index=defenseclaw_local (MuddyWater OR Seedworm OR "Static Kitten" OR "Mango Sandstorm" OR Mercury OR "Earth Vetala" OR "TEMP.Zagros" OR ChromElevator OR fmapp OR sentinelmemoryscanner OR sentinelagentcore OR "timetrakr.cloud" OR "sendit.sh" OR "179.43.177.220" OR "178.128.233.36") NOT sourcetype=archimedes:* over -30d returned ZERO events. TWENTY-SECOND consecutive sweep with dormant non-archimedes-internal stream pattern.
  - splunk-defenseclaw     # same dormant pattern; twenty-second consecutive sweep.
  - virustotal             # mcp__virustotal__lookup_domain timetrakr[.]cloud → 5/92 malicious (ESET + Fortinet + ADMINUSLabs + ArcSight + SOCRadar); creation 2026-01-18 / last-update 2026-01-23 (~1 month before Feb 20 South Korean intrusion onset). mcp__virustotal__lookup_ip 179.43.177.220 → 5/92 malicious (Private Layer INC Switzerland AS51852 — known bulletproof hosting). mcp__virustotal__lookup_ip 178.128.233.36 → 3/92 malicious (DigitalOcean Canada AS14061 — commodity VPS). All three IOCs VT-confirm Symantec's malicious classification. Recorded in raw-2026-05-13-flash-1800-001 IOC block.
sources_skipped_stale:
  - censys                 # MCP not built
  - urlscan                # MCP not built
  - hibp                   # No API key configured
  - x-cisagov              # STALE since 2026-05-10 12:00 FLASH
  - x-gossithedog          # STALE since 2026-05-09 — nitter.net account permanently delisted
  - ars-security           # STALE since 2026-05-09 — feeds.arstechnica.com/arstechnica/security 404
  - dragos                 # STALE since 2026-05-13 14:30 FLASH — third consecutive 404 across 00:00 + 06:00 + 14:30 sweeps; operator-side working RSS path identification still pending
sources_skipped_softfail_this_sweep:
  - threatfox              # CAPTCHA wall via WebFetch; awaiting MCP build
  - malwarebazaar          # awaiting MCP build
  - github-advisories      # 406 on global advisories.atom; per-repo GHSA fallback in use when triggered
  - proofpoint             # /us/threat-insight/blog/feed endpoint 404 since 2026-05-10 12:00 FLASH
  - iran-monitor           # 403 WAF/UA workaround pending
  - crowdstrike            # feedburner.com/crowdstrike 404 from 2026-05-13 06:00 sweep; NOT re-tested this narrow sweep (FLASH-fast scope)
  - mandiant               # feedburner.com/Mandiant 22nd-consecutive 404; held healthy pending operator alt-endpoint decision
  - eset-welivesecurity    # NOT re-invoked this narrow sweep — 14:30 FLASH coverage at +3.5h ago zero-in-window; ESET cadence multi-day
sources_health_changed_this_sweep:
  - bleepingcomputer       # last_successful_fetch 2026-05-13T14:30 → 2026-05-13T18:00; 2 in-window items (1 FLASH-CANDIDATE-PRODUCTIVE = MuddyWater Symantec relay; 1 DISCARDED = Exim CVE-2026-45185 patched-no-ITW). Productive sweep.
  - the-record             # last_successful_fetch 2026-05-13T14:30 → 2026-05-13T18:00; 1 in-window item DISCARDED (Dream Market arrest). Productive second-consecutive-sweep on this source.
  - rapid7                 # last_successful_fetch 2026-05-13T14:30 → 2026-05-13T18:00; 0 in-window items.
  - krebs + mstic + securityweek   # last_successful_fetch updated; 0 in-window items each.
  - splunk-archimedes + splunk-defenseclaw   # 22nd-consecutive dormant sweep; no health change (continued as expected).
  - symantec               # NEW source-grading proposal. First Archimedes-corpus citation as originating research source via raw-2026-05-13-flash-1800-001 (MuddyWater South Korea ChromElevator). Provisional A grade proposed per Tier-1 vendor research precedent. Operator action: add to source-grades.yaml `vendor_sources` and source-health.yaml.
match_reason:
  watchlist: []
  watchlist_match_strength: none_direct       # Industrial Cyber relay's "U.S. defense and aerospace software supplier" claim NOT in Symantec primary; treated as relay conflation with separate March 2026 Symantec Dindoor/Fakeset US-targeting campaign; NOT propagated
  actors:
    - "MuddyWater (Seedworm / Static Kitten / Mango Sandstorm / Mercury / Earth Vetala alias match)"   # FLASH-CANDIDATE attribution via Symantec primary; roster id 022, IR/MOIS
  vulnerabilities: []                          # CVE-2026-45185 Exim DISCARDED per FLASH-trigger evaluation (patched, no ITW); no other CVE-class in-window content
  keywords:
    - flash_candidate_symantec_muddywater_chromelevator_southkorea_electronics_multi_victim
    - exim_cve_2026_45185_patched_no_itw_discarded
    - dream_market_arrest_historical_no_tracked_actor_discarded
    - symantec_first_corpus_citation_provisional_a_proposed
    - industrialcyber_relay_conflation_caveat_logged
    - splunk_dormant_22nd_consecutive
    - mandiant_feedburner_22nd_consecutive_404
triage_tags:
  - sentinel
  - flash_sweep_1800_2026_05_13
  - quiet_hours_inactive
  - one_flash_candidate_matched
  - trigger_2_tracked_actor_attribution_matched_cleanly
  - trigger_4_tracked_actor_ttp_change_matched_cleanly
  - trigger_5_ad_sector_campaign_failed_relay_conflation_industrialcyber
  - critical_override_failed_no_cvss10_no_named_ad_watchlist_victim
  - symantec_first_corpus_citation_provisional_a_proposed
  - splunk_dormant_22nd_consecutive
  - mandiant_feedburner_22nd_consecutive_404
flash_triggers_evaluated:
  trigger_1_critical_cve_exploited:
    matched: false
    notes: |
      CVE-2026-45185 Exim UAF in TLS shutdown during BDAT chunking
      (XBOW researcher Federico Kirschbaum, BleepingComputer relay)
      is a fresh Critical-class CVE BUT:
        - patch_available: TRUE (Exim 4.99.3 shipped 2026-05-12, one
          day BEFORE BleepingComputer disclosure)
        - cvss_score: not assigned in article (CVSS not yet published)
        - exploitation_confirmed_in_wild: FALSE (article explicitly
          frames as theoretical / AI-LLM PoC narrative; XBOW researcher
          quoted "I don't think LLMs alone are quite ready to write
          exploits against real-world software yet")
      Trigger 1 FAILS on exploitation_confirmed false (PoC-only) and
      additionally on the patch having shipped before disclosure
      (no pre-patch active-exploitation window).

  trigger_2_tracked_actor_attribution:
    matched: true
    notes: |
      TRIGGER 2 MATCHES via the Symantec Threat Hunter Team attribution
      to MuddyWater for the Q1 2026 multi-victim espionage campaign
      including a South Korean electronics maker (Feb 20-27 case study)
      and 8 other victims across 4 continents (airport / government /
      industrial manufacturing / financial services / education).
      MuddyWater is roster id 022 per threats/threat-actors/_roster.yaml
      line 322 (aliases: Mango Sandstorm, Static Kitten, Mercury,
      MERCURY, Seedworm, Earth Vetala, TEMP.Zagros, Boggy Serpens).
      Symantec is A-grade Tier-1 vendor research practice (Broadcom-
      owned, Symantec + Carbon Black joint Threat Hunter Team byline),
      coined the Seedworm taxonomy 2018, peer of Mandiant / CrowdStrike
      / Unit 42 / MSTIC / Sophos / ESET / Dragos / Bitdefender / Wiz
      Research / Snyk. Attribution language "widely believed to be
      linked" to Iran MOIS — softer than formal "high confidence" but
      matches established Symantec Seedworm taxonomy primacy.
      Attribution is to a campaign DISTINCT from the 2026-05-06
      Rapid7 MuddyWater FLASH (different victim set, different
      geography, different malware family ChromElevator vs. Rapid7
      tooling). The 24h anti-noise rule does NOT bar this FLASH —
      prior MuddyWater FLASH was 7 days ago and was a different
      trigger-topic. Full detail in raw-2026-05-13-flash-1800-001.

  trigger_3_first_party_ioc_hit:
    matched: false
    notes: |
      Splunk first-party telemetry across both indexes returned 0
      non-archimedes-internal events over -30d on the full MuddyWater
      / Seedworm aliases + ChromElevator + Fortemedia binary names
      + SentinelOne component file names + timetrakr.cloud + sendit.sh
      + 179.43.177.220 + 178.128.233.36 indicator set. Twenty-second
      consecutive dormant sweep across both indexes.

  trigger_4_tracked_actor_ttp_change:
    matched: true
    notes: |
      TRIGGER 4 ALSO MATCHES via the same Symantec disclosure — multiple
      tradecraft delta observations against MuddyWater corpus baseline:
        - NEW malware family ChromElevator (post-exploitation credential
          theft; first Symantec corpus disclosure; not previously in
          threats/threat-actors/MuddyWater/iocs.yaml)
        - NOVEL DLL sideloading pair (Fortemedia fmapp.exe → fmapp.dll)
        - NOVEL DLL sideloading pair (SentinelOne sentinelmemoryscanner.exe
          → sentinelagentcore.dll — brand-impersonation of defensive
          EDR; coincident with Salt Typhoon FamousSparrow sentinelonepro
          C2-domain brand-impersonation in same 12h window — coincidental,
          NOT attribution-linked)
        - Node.js runtime as PowerShell orchestration layer
        - Target-set geographic expansion from MENA-government baseline
          into East Asia electronics manufacturing + Southeast Asia
          industrial manufacturing + Latin America financial services
        - Exfiltration via sendit.sh public file-transfer service
          (living-off-trusted-cloud pattern)
        - C2 beacon cadence ~90s with ~36h mid-intrusion inactivity gap
      Full detail in raw-2026-05-13-flash-1800-001.

  trigger_5_ad_sector_campaign:
    matched: false
    notes: |
      Trigger 5 FAILS on watchlist-targeted condition. Symantec primary
      (security.com/threat-intelligence/iran-seedworm-electronics, 2026-
      05-12) names NO aerospace-defense.yaml victim. The Industrial
      Cyber relay (industrialcyber.co/threats-attacks/symantec-uncovers
      -iran-linked-seedworm-...) introduces a "U.S. defense and aerospace
      software supplier" with Israeli operations as a victim — but this
      claim DOES NOT APPEAR in the Symantec primary. The Industrial Cyber
      relay-introduced claim appears to be a conflation with the separate
      March 2026 Symantec/HelpNetSecurity-relayed Dindoor/Fakeset US-
      critical-infrastructure MuddyWater campaign (different malware
      family, different victim set). Per Hard Rule 2 (never originate
      attribution) and source-primary-precedence, the relay-introduced
      A&D-supplier claim is NOT propagated into Archimedes corpus. If
      Symantec primary is updated or another A-grade source corroborates
      with explicit A&D-prime victim naming in the next 24-72h, this
      candidate gets re-evaluated for Trigger 5 + Critical Override.

  trigger_6_zero_day_no_patch:
    matched: false
    notes: |
      CVE-2026-45185 Exim UAF was PATCHED in Exim 4.99.3 on 2026-05-12,
      one day BEFORE the BleepingComputer disclosure. Not zero-day-
      without-patch. Trigger 6 FAILS on patch_status patched. No other
      zero-day-class disclosures in 4h-window sweep.

critical_override_evaluated:
  cvss_10: false                            # MuddyWater disclosure is intrusion-set (no CVE-class indicator); Exim CVE-2026-45185 CVSS not assigned, irrelevant per Trigger 1 fail
  active_exploitation: partial              # Symantec primary describes Q1 2026 retrospective in past tense; Industrial Cyber relay's "continuing into recent days" claim appears tied to its A&D-supplier conflation, not in Symantec primary; conservative reading is retrospective
  tracked_actor: true                       # MuddyWater roster id 022 (IR/MOIS)
  ad_watchlist_hit: false                   # Symantec primary names no A&D victim; Industrial Cyber relay-introduced claim NOT propagated
  conditions_met: 1_of_4                    # only tracked_actor positive; CVSS-10 floor + ad_watchlist_hit fail; active_exploitation only partial
  bypass_quiet_hours: false                 # moot — quiet hours inactive anyway (18:00 EDT inside 09:00-21:00 EDT active window)
  outcome: not_applicable                   # FLASH posting permitted in active hours regardless of critical-override status

iocs_extracted: false                       # sentinel sweep frontmatter-only; per-item IOCs are in raw-2026-05-13-flash-1800-001
iocs_count: 0
text_word_count: 0                          # sentinel sweep frontmatter-only
promoted: false                              # sentinel files are audit-trail-only by design — not promotable claim clusters
sentinel_disposition: audit_trail_for_flash_candidate_sweep_with_one_candidate_promoted
sentinel_grader_passthrough:
  graded_at: 2026-05-13T18:25:00-04:00
  graded_by: grader
  grading_run_id: flash-grade-20260513-180500
  passthrough_disposition: audit_trail_only_per_sentinel_design
  candidate_promoted: raw-2026-05-13-flash-1800-001
  finding_id: finding-2026-05-13-FLASH-1800-0001
  collector_discards_logged_to_rejection_log:
    - reject-2026-05-13-0001-exim-cve-2026-45185
    - reject-2026-05-13-0002-dream-market-arrest
ttl_expires_at: 2026-08-11T18:10:00-04:00   # 90 days per LEGAL-POLICY retention
---

# Sentinel — 2026-05-13 18:00 EDT FLASH alert sweep (one FLASH candidate)

FLASH alert sweep for the narrow 4h window 2026-05-13T14:00 → 18:00
EDT (extended back from the standard 18:00-2h cadence to capture
wires that broke during 16:00 afternoon-brief composition). Quiet
hours INACTIVE (18:00 EDT inside 09:00-21:00 EDT active window per
`infrastructure/flash-policy.yaml`).

## Sweep outcome — ONE FLASH candidate

**FLASH candidate:** `raw-2026-05-13-flash-1800-001` — **Symantec
Threat Hunter Team attributes Q1 2026 multi-victim espionage
campaign to MuddyWater (Seedworm) including South Korean electronics
maker case study**.

- Trigger 2 (tracked-actor-attribution) MATCHES cleanly
- Trigger 4 (tracked-actor-TTP-change) MATCHES on multiple tradecraft
  observations (ChromElevator new family + two novel DLL sideloading
  pairs + target geographic expansion + Node.js orchestration +
  living-off-trusted-cloud exfil)
- Trigger 5 (A&D-sector campaign) FAILS — Symantec primary names no
  A&D victim; Industrial Cyber relay-introduced "U.S. defense and
  aerospace software supplier" claim is treated as conflation with
  separate March 2026 Symantec Dindoor/Fakeset campaign and is NOT
  propagated into corpus
- Critical override FAILS on CVSS-10 floor + watchlist-NAMED-victim;
  quiet hours inactive anyway

Symantec is a FIRST Archimedes-corpus citation; provisional A grade
proposed per Tier-1 vendor research precedent (SentinelOne 2026-05-
08, Wiz Research + Snyk 2026-05-12, Bitdefender 2026-05-13 morning,
Sophos / ESET / Dragos Session 11 ratifications).

## In-window items surveyed (DISCARDED at Mode 1 or anti-noise)

1. **BleepingComputer — Iranian hackers targeted major South Korean
   electronics maker (Bill Toulas, 17:59 EDT in-window).** Symantec
   Threat Hunter Team primary relay; MuddyWater attribution; multi-
   victim Q1 2026 campaign. **FLASH CANDIDATE.** Raw-signaled at
   flash-1800-001. Full detail there.

2. **BleepingComputer — New critical Exim mailer flaw allows remote
   code execution (Bill Toulas, 16:23 EDT in-window).** CVE-2026-
   45185 Exim 4.97-4.99.2 UAF in TLS shutdown during BDAT chunking.
   PATCHED in Exim 4.99.3 on 2026-05-12 (one day BEFORE disclosure).
   XBOW researcher Federico Kirschbaum + AI/LLM PoC narrative;
   NO in-the-wild exploitation per article; CVSS not assigned.
   Trigger 1 FAILS on active_exploitation false (PoC-only theoretical).
   Trigger 6 FAILS on patch_status patched. Also related-but-distinct
   from CVE-2026-40364 Exim BDAT cohort already in 2026-05-12 corpus.
   DISCARDED per Mode 1 (no qualifying trigger).

3. **The Record — Alleged Dream Market admin arrested in Germany
   after US indictment (15:54 EDT in-window).** Historical dark-web-
   marketplace law-enforcement action (Owe Martin Andresen, 2013-
   2019 Dream Market admin, ~$2M money laundering charges including
   cryptocurrency and gold bars). NO tracked actor, NO A&D, NO CVE,
   NO threat-intel. DISCARDED per Mode 1.

## In-window zero-result sources

- SecurityWeek (last_modified 13:13 EDT pre-window; 0 items in 4h window)
- Rapid7 (last_modified 17:46 EDT in-window from feed-server activity; 0 items)
- Krebs (last_modified 17:59 EDT in-window from feed-server activity; 0 items)
- MSTIC (last_modified 14:30 EDT in-window from feed-server activity; 0 items)

## Anti-noise NOT triggered this sweep

- **MuddyWater FLASH candidate:** prior MuddyWater FLASH was
  2026-05-06 Rapid7 MENA campaign — 7 days ago, well outside 24h
  anti-noise window. Distinct topic (different victim set, geography,
  malware family). Anti-noise does NOT bar this FLASH.

- Carry-forward anti-noise from earlier briefs (NOT re-surfaced
  this sweep): KongTuke ModeloRAT via Teams (afternoon brief
  finding-2026-05-13-PM-0001), BitLocker YellowKey/GreenPlasma PoCs
  (afternoon brief finding-2026-05-13-PM-0002), FamousSparrow
  Azerbaijan Salt Typhoon (14:30 FLASH finding), CVE-2026-40361
  Outlook zero-click (morning brief finding-2026-05-13-0001),
  Foxconn/Nitrogen (morning brief finding-2026-05-13-0002).

## Source-health updates this sweep

See `sources_health_changed_this_sweep` block in frontmatter.
Notable:

- `bleepingcomputer` — productive sweep with 1 FLASH-candidate-
  productive + 1 DISCARDED items.
- `the-record` — productive sweep, 1 DISCARDED item.
- `splunk-archimedes` + `splunk-defenseclaw` — 22nd-consecutive
  dormant sweep across both indexes; pattern continues.
- `symantec` — NEW source-grading proposal. First Archimedes-corpus
  citation via raw-1800-001. Provisional A grade proposed. Operator
  action: add to `source-grades.yaml` and `source-health.yaml`.
- `mandiant` — feedburner 22nd-consecutive 404 (not re-tested this
  narrow sweep; held healthy pending operator alt-endpoint decision).
- `dragos` — STALE since 2026-05-13 14:30 FLASH; no change this sweep.

## Flagged for orchestrator awareness (NOT raw-signaled at FLASH severity)

None this sweep. The Exim CVE-2026-45185 is patched and pre-
exploitation; the Dream Market arrest is historical / non-cyber-
threat-intel. Neither warrants raw-signaling at any severity.

## What did NOT change this sweep

- Splunk first-party non-archimedes-internal stream: 0 events
  6h + 24h + 30d on MuddyWater / Seedworm / ChromElevator / IOC
  set (22nd-consecutive dormant sweep across both indexes).
- KEV catalog: 0 entries dateAdded ≥ 2026-05-13 (CVE-2026-42208
  BerriAI LiteLLM remains most recent at 2026-05-08).
- Mandiant feedburner: 22nd-consecutive 404; held healthy pending
  operator decision.
- Stale sources (x-cisagov, x-gossithedog, ars-security, dragos):
  no recovery attempts this sweep.

---

## Extraction notes

- Sentinel file — per FLASH-POLICY convention for sweeps that
  produce FLASH candidates, this sentinel carries the broader
  sweep audit trail while the per-candidate raw-signal (flash-
  1800-001) carries the full source content + IOC extraction.
- Pre-flight LEGAL-POLICY check: passive RSS/web fetches + own-
  index Splunk reads + VirusTotal domain/IP lookups only;
  `authorized_for_active_recon` remains empty; no prohibited
  query patterns triggered; no credentials surfaced this sweep.
- Anti-noise enforced per FLASH-POLICY §one-flash-per-topic-per-
  24h. Prior 24h FLASH topics carry-forward: FamousSparrow Salt
  Typhoon Azerbaijan (14:30 FLASH today); none overlap with the
  Symantec MuddyWater South Korea ChromElevator candidate. The
  prior MuddyWater FLASH (2026-05-06 Rapid7) is 7 days old, well
  outside the 24h window — anti-noise N/A.
- No raw-signal items marked `test: true` observed in
  `threats/raw-signal/` directory via my survey.
- Quiet hours INACTIVE — FLASH candidate eligible for immediate
  posting if grader / red-team / briefer concur on FLASH-format
  publication.

## IOCs (sentinel level)

This sentinel file carries no body-level IOC extraction. The full
IOC block (18 indicators including 1 VT-confirmed C2 domain + 1
public file-transfer service abused for exfil + 2 VT-confirmed
C2 IPs + 13 SHA256 hashes referenced in Symantec primary + 4
additional IPs in Symantec primary not surfaced in relay + 2 DLL
sideloading pairs + 1 new malware family + 3 URLs + persistence
mechanisms + cadence indicators) is in raw-2026-05-13-flash-
1800-001.

Splunk first-party queries this sweep:

```yaml
splunk_queried_iocs_no_match:
  flash_candidate_actor_aliases:
    - MuddyWater
    - Seedworm
    - "Static Kitten"
    - "Mango Sandstorm"
    - Mercury
    - "Earth Vetala"
    - "TEMP.Zagros"
  flash_candidate_malware_families:
    - ChromElevator
  flash_candidate_legitimate_binary_names_abused:
    - fmapp
    - sentinelmemoryscanner
    - sentinelagentcore
  flash_candidate_c2_domains:
    - "timetrakr.cloud"
    - "sendit.sh"
  flash_candidate_c2_ips:
    - "179.43.177.220"
    - "178.128.233.36"
```

Zero non-pipeline-self-reference matches across all of these
against `archimedes` and `defenseclaw_local` indexes over `-30d`
window. Twenty-second consecutive dormant sweep.
