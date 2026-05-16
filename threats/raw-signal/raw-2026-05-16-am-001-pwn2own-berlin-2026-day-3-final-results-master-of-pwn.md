---
raw_id: raw-2026-05-16-am-001
collected_at: 2026-05-16T07:32:00-04:00
run_id: pre-brief-20260516-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: zdi-blog
  source_name: "Zero Day Initiative (Trend Micro) — Pwn2Own Berlin 2026 Day 3"
  source_url: "https://www.thezdi.com/blog/2026/5/16/pwn2own-berlin-2026-day-three-results-and-master-of-pwn"
  published_at: 2026-05-16T06:38:50-04:00
  byline: "Dustin Childs"
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [Pwn2Own, Berlin, ZDI, SharePoint, ESXi, Red Hat, Windows, OpenAI Codex, Master of Pwn, embargo]
triage_tags: [carry_forward_update, pwn2own_berlin_2026_lineage, embargo_active, no_flash_trigger]
flash_trigger_evaluation:
  trigger_1_critical_cve_exploited: false
  trigger_1_failure_reason: "Pwn2Own bugs are under 90-day vendor-coordinated-disclosure embargo. No CVEs published, no in-the-wild exploitation reported. Triggers 1 and 6 require explicit CVE / patch-status references; embargoed Pwn2Own results do not meet either condition."
  trigger_6_zero_day_no_patch: false
  trigger_6_failure_reason: "Pwn2Own embargo is the standard coordinated-disclosure pattern; vendors get 90 days to patch. This is NOT 'zero-day-no-patch' in the FLASH-POLICY sense — vendor process is active."
  conclusion: "Pwn2Own Berlin 2026 final results. Day 3 yielded 3 successful exploits ($34,500 in payouts) bringing event total to $943,250 across 42 unique zero-days. NOT a FLASH trigger. Routes to morning brief as carry-forward continuation of 2026-05-15 afternoon brief's Pwn2Own Day 2 Exchange-chain item."
iocs_extracted: false
iocs_count: 0
text_word_count: 720
promoted: true
promoted_to_finding: finding-2026-05-16-0002
promoted_at: 2026-05-16T08:16:00-04:00
ttl_expires_at: 2026-08-14T07:32:00-04:00
---

# Pwn2Own Berlin 2026 — Day 3 Results and Master of Pwn Final Standings

**Publication:** 2026-05-16 06:38 EDT (within pre-brief 14h window 17:30 EDT prior → 07:30 EDT)
**Author:** Dustin Childs (Zero Day Initiative / Trend Micro)
**Outlet:** Trend Micro ZDI Blog
**Source grade:** Currently not separately scored in source-grades.yaml as `zdi-blog` (parent: Trend Micro, vendor-research-tier; ZDI is the canonical Pwn2Own primary). Recommend grader/operator add an entry on next ratification pass — first-cited surface this brief cycle. Provisional A starting grade per same precedent as Bitdefender, Sysdig, Wiz (vendor-research / contest-coordination publication).

## Source-attested facts (per ZDI primary)

### Day 3 attempts (Saturday 2026-05-16)

Three successful exploits, totaling $34,500 in payouts:

1. **Red Hat Linux** — Sina Kheirkhah (Summoning Team)
   - Result: SUCCESS / COLLISION (one bug previously known to vendor)
   - Payout: $7,000 + 1.5 Master of Pwn points
   - Bug class: two-bug chain (not detailed in opening framing)

2. **Windows 11** — Le Tran Hai Tung + dungnm + hieuvd (Viettel Cyber Security)
   - Result: SUCCESS
   - Vulnerability: Integer overflow → privilege escalation
   - Payout: $7,500 + 3 Master of Pwn points
   - Round 5 victory

3. **OpenAI Codex** — Satoki Tsuji (Ikotas Labs)
   - Result: SUCCESS
   - Vulnerability: External control abuse (per ZDI summary)
   - Payout: $20,000 + 4 Master of Pwn points

### Targets attempted but no successful results in published Day 3 text

- **Microsoft SharePoint** — on docket per opening framing, no successful exploitation noted in retrievable text
- **VMware ESXi** — on docket per opening framing, no successful exploitation noted in retrievable text

### Event totals

- Pre-Day-3: **$908,750 across 39 unique zero-days**
- Day-3 additions: $34,500 across 3 exploits
- **Combined total: $943,250 across 42 unique zero-days**
- Master of Pwn final standings: referenced but leaderboard image not text-readable in retrieved content

### Day 2 Exchange chain (Orange Tsai / DEVCORE) status

The Day 3 wrap does **NOT** mention the Day 2 Exchange chain by Orange Tsai / DEVCORE. The 2026-05-15 afternoon brief carry-forward noted this chain as embargoed. The embargo remains active per ZDI's standard 90-day vendor-coordinated-disclosure window. No new disclosure, no CVE assignment, no embargo-lift signal in the 14h pre-brief window.

## Why this surfaces

- **Carry-forward continuation**: 2026-05-15 afternoon brief flagged Pwn2Own Berlin Day 2 Exchange chain (Orange Tsai / DEVCORE, embargoed) as a watch item. Today's Day 3 wrap is the natural next milestone — confirms event conclusion, confirms continued embargo on the Exchange chain, and adds the final event-payout figure.
- **No A&D / no roster actor / no tracked CVE**: Pwn2Own results are vendor-coordinated bugs in Red Hat / Windows / SharePoint / ESXi / OpenAI Codex. None map to tracked actors, none target A&D primes directly. Indirect A&D relevance via Windows (universal exposure) and SharePoint (defense-contractor collaboration platform usage) is structural, not campaign-specific.
- **OpenAI Codex result is the notable new surface**: This is the second 2026 surface where OpenAI is a target (first: TanStack supply-chain breach finding-2026-05-14-0008). Pwn2Own-style external-control-abuse on Codex is a different attack surface than supply-chain compromise, but operator may want to add OpenAI to a future watch-config standing section if AI / coding-assistant attack surfaces become an A&D-prime concern over the coming quarter.

## FLASH evaluation per FLASH-POLICY.md

Walked all 6 triggers:

1. **critical-cve-exploited** — FAILS. No CVE published (embargoed). No in-the-wild exploitation.
2. **tracked-actor-attribution** — FAILS. Contest researchers are not threat actors.
3. **first-party-ioc-hit** — FAILS. Splunk defenseclaw_local dormant; no IOCs to hit on.
4. **tracked-actor-ttp-change** — FAILS. No tracked actor.
5. **ad-sector-campaign** — FAILS. Pwn2Own is research contest, not campaign; no A&D primes targeted.
6. **zero-day-no-patch** — FAILS. Vendor-coordinated disclosure under 90-day embargo IS the patch process; this is the well-known ZDI cadence, not a zero-day-no-patch scenario.

**Conclusion: NOT a FLASH trigger.** Routes to morning brief 2026-05-16 as carry-forward continuation of 2026-05-15 afternoon brief's Pwn2Own Berlin Day 2 watch item. Briefer should note event closure, $943,250 total, Day 2 Exchange chain embargo still active, no SharePoint/ESXi successful exploitation on docket day.

## Extraction notes

- Language: en
- Publisher byline: Dustin Childs (ZDI / Trend Micro)
- Article type: contest-results wrap-up
- Raw IOC extraction invoked: no (no IOCs — embargoed bugs, no CVEs, no infrastructure)
- Hard Rule 3 compliance: No PoC content extracted. ZDI does not publish exploitation detail during embargo.
- Anti-noise check: This is the FIRST raw-signal in the 24h dedup window mentioning Pwn2Own Berlin 2026 Day 3 / final results. The Day 2 Exchange-chain carry-forward is a separate dedup namespace (prior brief).

## IOCs (from ioc-extraction skill)

None. No CVEs, no domains, no IPs, no hashes. Embargoed contest bugs.
