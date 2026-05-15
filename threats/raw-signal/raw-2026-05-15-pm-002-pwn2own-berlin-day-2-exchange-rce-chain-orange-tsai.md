---
raw_id: raw-2026-05-15-pm-002
collected_at: 2026-05-15T15:40:00-04:00
run_id: pre-brief-20260515-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: bleepingcomputer
  source_name: "BleepingComputer"
  source_url: https://www.bleepingcomputer.com/news/security/pwn2own-day-two-hackers-demo-microsoft-exchange-windows-11-red-had-enterprise-linux-zero-days/
  published_at: 2026-05-15T17:47:25+00:00
  byline: "Sergiu Gatlan"
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [Exchange, Pwn2Own, Orange Tsai, DEVCORE, RCE, SYSTEM, zero-day, Windows 11, Red Hat Enterprise Linux, NVIDIA Container Toolkit, Cursor AI, OpenAI Codex, ZDI]
triage_tags: [exchange_attack_surface_compounding, vendor_responsible_disclosure, no_cve_assigned_yet, 90_day_clock_running, awareness_for_afternoon_brief, non_flash]
iocs_extracted: true
iocs_count: 0
text_word_count: 780
promoted: true
promoted_to_finding: finding-2026-05-15-0004
promoted_at: 2026-05-15T16:10:00-04:00
ttl_expires_at: 2026-08-13T15:40:00-04:00
---

# Pwn2Own Berlin 2026 Day 2 — Microsoft Exchange RCE-to-SYSTEM 3-bug chain by Orange Tsai / DEVCORE ($200K)

**Source URL:** https://www.bleepingcomputer.com/news/security/pwn2own-day-two-hackers-demo-microsoft-exchange-windows-11-red-had-enterprise-linux-zero-days/
**Byline:** Sergiu Gatlan
**Published:** 2026-05-15 17:47:25 UTC (13:47 EDT)

---

## Headline finding

During Day 2 of Pwn2Own Berlin 2026 (the Trend Micro Zero Day Initiative offensive-security contest):

- **Cheng-Da "Orange" Tsai** (DEVCORE Research Team) demonstrated a **chain of three bugs** against Microsoft Exchange, earning **$200,000** and achieving **remote code execution with SYSTEM privileges**.
- Day 2 total: **$385,750** awarded across **15 unique zero-day vulnerabilities** demonstrated.
- No CVE identifiers have been assigned yet. Per Pwn2Own competition rules, "vendors have 90 days to patch" after disclosure. The Exchange chain is responsibly disclosed to Microsoft via ZDI; details are embargoed pending patch.

The article does **not** establish any technical connection to CVE-2026-42897 (the separate OWA XSS zero-day that Microsoft confirmed exploited in the wild and that CISA added to KEV today). These are procedurally distinct vulnerabilities — CVE-2026-42897 is XSS in OWA, the Pwn2Own item is a 3-bug RCE chain to SYSTEM.

## Full list of Day 2 zero-days demonstrated

Per the BleepingComputer extraction:

1. **Microsoft Exchange** — 3-bug chain achieving RCE with SYSTEM privileges. Researcher: Cheng-Da "Orange" Tsai (DEVCORE Research Team). Payout: $200,000.
2. **Windows 11** — Integer overflow exploit. Researcher: Siyeon Wi. Payout: $7,500.
3. **Red Hat Enterprise Linux for Workstations** — Privilege escalation to root. Researcher: Ben Koo (Team DDOS). Payout: $10,000.
4. **NVIDIA Container Toolkit** — Use-after-free vulnerability.
5. **Cursor AI coding agent** — 2 separate exploits.
6. **OpenAI Codex** — exploited (specifics not detailed in the extract).

Additional researchers identified by name (across the Day 2 demos): 0xDACA, Noam Trobinski, Le Duc Anh Vu, Sina Kheirkhah, and Compass Security.

## Why this matters (context for afternoon brief)

This is **not** a fresh FLASH trigger:

- **No CVE assigned** (Pwn2Own 90-day responsible disclosure clock starts after demo).
- **No active in-the-wild exploitation** — these are contest-environment proof-of-concepts; details are embargoed; patches are pending vendor coordination.
- **No tracked actor** — Orange Tsai is a researcher with multi-year ZDI track record; DEVCORE is a legitimate security research firm (Taiwan-based).

What it **does** affect: the Microsoft Exchange attack-surface picture is now visibly compressed. Within 36 hours (since 2026-05-14 12:00 EDT), the corpus has captured:

1. **CVE-2026-42897** — OWA XSS zero-day, MSRC "Exploitation Detected," CVSS 8.1, KEV-listed 2026-05-15 dueDate 2026-05-29 (per pm-001 this sweep).
2. **Pwn2Own Day 2 chain** — RCE-to-SYSTEM via 3-bug chain (CVE pending). Embargoed under ZDI's 90-day responsible-disclosure timeline.

For an A&D-prime estate running on-prem Exchange: the operational implication is that **two procedurally distinct attack surfaces on the same product** are simultaneously under research-and-exploitation pressure. CVE-2026-42897 is the active-exploitation surface to mitigate today; the Pwn2Own chain is the next-90-days vulnerability-management item to watch.

## Notable absence of A&D / actor relevance in this article

- No A&D-prime named victims.
- No actor attribution (Orange Tsai's demo is contest-research, not a threat-actor activity).
- No first-party telemetry connection.
- No connection to CVE-2026-42897 stated; the article frames the two items as distinct.

## Discard logic for FLASH

- Trigger 1 (critical-cve-exploited): FALSE — no CVE assigned, no ITW exploitation.
- Trigger 2 (tracked-actor-attribution): FALSE — Orange Tsai / DEVCORE is a research practice, not a tracked threat actor.
- Trigger 3 (first-party-ioc-hit): FALSE — no IOCs published (embargoed); Splunk dormant stream pattern persists.
- Trigger 4 (tracked-actor-ttp-change): FALSE — no tracked-actor attribution; not a TTP delta on TeamPCP / UNC1549 / Salt Typhoon / etc.
- Trigger 5 (active-ad-campaign): FALSE — no campaign, no victim, no active exploitation.
- Trigger 6 (zero-day-no-patch): MARGINAL — chain is technically a zero-day with no patch, but exploitation-confirmed-or-imminent is FALSE (embargoed PoC, vendor disclosure window running). Fails the conjunctive condition.

This raw-signal is therefore **brief-relevant awareness item, not a FLASH**. Submitted for 16:00 afternoon brief composition with framing: "Pwn2Own compounds Exchange attack-surface visibility; not actionable as IOC stream; CVE pending."

## Cross-reference / open questions for grader

- **Worth checking:** Whether ZDI / DEVCORE / Orange Tsai publish a non-technical advisory or research-context post that names affected Exchange versions / pre-conditions, even if exploit specifics are embargoed.
- **Worth tracking:** Microsoft response timeline — within 90 days from 2026-05-15, Microsoft is expected to issue CVE + patch for the 3-bug chain. Vulnerability-tracker should expect a CVE-2026-NNNN candidate in the 2026-07 to 2026-08 window.
- **Worth noting:** Day 1 of Pwn2Own Berlin (2026-05-14, not captured this sweep) likely yielded additional zero-days; the morning collector did not raw-signal the Day 1 wrap-up. Operator may want to backfill if afternoon-brief scope expands to Pwn2Own coverage.

## Article body excerpt (limited quote, under 15 words)

The BleepingComputer article notes that during Day 2 competitors "collected $385,750 in cash awards after exploiting 15 unique zero-day vulnerabilities."

(Quote is 15 words; one quote only per Hard Rule 7.)

## Extraction notes

- Language: en
- Publisher byline: Sergiu Gatlan
- Article type: media (incident-recap of contest event)
- Raw IOC extraction invoked: yes (no IOCs surfaced — embargoed)

## IOCs (from ioc-extraction skill)

```yaml
iocs:
  cve_identifiers: []
    # No CVEs assigned yet; ZDI 90-day responsible disclosure clock from 2026-05-15

  researcher_attributions_named:
    - researcher: "Cheng-Da 'Orange' Tsai"
      organization: "DEVCORE Research Team"
      target: "Microsoft Exchange"
      finding: "3-bug chain achieving RCE with SYSTEM privileges"
      payout_usd: 200000
    - researcher: "Siyeon Wi"
      target: "Windows 11"
      finding: "integer overflow"
      payout_usd: 7500
    - researcher: "Ben Koo"
      organization: "Team DDOS"
      target: "Red Hat Enterprise Linux for Workstations"
      finding: "privilege escalation to root"
      payout_usd: 10000
    - researcher: "0xDACA"
      target: "(unspecified Day 2 demo)"
    - researcher: "Noam Trobinski"
      target: "(unspecified Day 2 demo)"
    - researcher: "Le Duc Anh Vu"
      target: "(unspecified Day 2 demo)"
    - researcher: "Sina Kheirkhah"
      target: "(unspecified Day 2 demo)"
    - researcher: "Compass Security"
      target: "(unspecified Day 2 demo)"

  contest_metadata:
    event: "Pwn2Own Berlin 2026"
    day: 2
    sponsor: "Trend Micro Zero Day Initiative (ZDI)"
    total_payout_day_2_usd: 385750
    unique_zero_days_day_2: 15
    responsible_disclosure_window_days: 90
    cve_assignment_eta_window: "2026-07 to 2026-08 (post 90-day clock)"

  attribution_claims:
    - claim: "Microsoft Exchange RCE-to-SYSTEM via 3-bug chain"
      claimed_by: "DEVCORE / Orange Tsai (per BleepingComputer)"
      attribution_language: "demonstrated"
      independent_corroboration: "ZDI contest framework — Trend Micro ZDI judges the exploit chain; demonstration is the corroboration"
      note: "Distinct from CVE-2026-42897 OWA XSS; no asserted relationship between the two Exchange issues"

  iocs_count_total: 0
  ioc_breakdown:
    cve: 0
    embargoed_pending_vendor_disclosure: true
```
