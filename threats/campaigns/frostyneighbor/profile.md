---
campaign_id: frostyneighbor
aliases: [FrostyNeighbor, Fresh Mischief, Digital Shenanigans]
status: active
first_observed: 2026-03 (per ESET — "five surges since July 2024" pattern)
last_observed: 2026-05-14 (publication date of ESET reporting; campaign ongoing)
attributed_actors:
  - actor_id: null            # NOT in roster — /new-actor flagged in 2026-05-14 brief
    actor_name: UNC1151 / Ghostwriter
    threat_level: not-tracked
    confidence: per-ESET-single-source
    attribution_source: "ESET (Damien Schaeffer) named-byline analyst. ESET hedges as 'reportedly operating from Belarus' (also uses 'allegedly' and 'apparent' throughout)."
attribution_caveats: |
  Single-source attribution. WEP cap at "likely" per single-source veto.
  ESET's own framing uses hedge vocabulary ("reportedly," "allegedly," "apparent")
  — Archimedes preserves the hedges verbatim per Hard Rule 2.
  Multi-A-grade source coverage spans Mandiant + Microsoft historical (2020-2024,
  pre-Archimedes corpus) + Polish ABW (finding-2026-05-08-0009, B-grade) +
  ESET (A-grade) — UNC1151 is a /new-actor candidate at conservative grade.
sectors_targeted:
  - Ukrainian government
  - Ukrainian military
  - Polish industrial sectors
  - Lithuanian industrial sectors
geographies: [Ukraine, Poland, Lithuania]
named_victims: []               # specific names not in ESET excerpt
ad_relevance: partner-of-partner-exposure
ad_relevance_rationale: |
  Direct A&D-prime relevance LOW. Structural partner-of-partner exposure only —
  Polish + Lithuanian industrial sectors are NATO-adjacent and have downstream
  DIB-supply-chain relationships, but no US A&D-prime named victim. Campaign is
  geopolitically scoped to Eastern European theater.
related_briefs:
  - threats/briefs/2026-05-14-morning.md
  - threats/briefs/2026-05-14-afternoon.md
related_actors_referenced: [UNC1151, Ghostwriter]
related_vulnerabilities:
  - CVE-2023-38831       # WinRAR — patched
  - CVE-2024-42009       # Roundcube XSS — patched
tracked_since: 2026-05-14
last_reviewed: 2026-05-14
next_review_due: 2026-08-14
dossier_version: 1
tlp: CLEAR
---

# Campaign — FrostyNeighbor

## Status

**Active.** First Archimedes-corpus surface 2026-05-14 via ESET (Damien Schaeffer named-byline). Per ESET, campaign window is 2026-03 onward; described as the latest in **five surges since July 2024**.

## Attribution

**UNC1151 / Ghostwriter** per ESET single-source attribution. NOT currently a roster entry — flagged for `/new-actor` consideration in the 2026-05-14 morning brief.

Multi-corpus context: pre-Archimedes (2020-2024) attribution to UNC1151 / Ghostwriter has been published by Mandiant and Microsoft; Polish ABW added a B-grade attestation in finding-2026-05-08-0009. ESET (2026-05-14) is the second A-grade Archimedes-corpus citation, satisfying the **two-distinct-campaigns-in-6-days** /new-actor candidacy criterion noted by the briefer.

Per Hard Rule 2, the hedge vocabulary in the source ("reportedly operating from Belarus," "allegedly," "apparent") is preserved verbatim — Archimedes does not originate Belarusian-state attribution; it relays ESET's source-attested framing.

## Mechanism

- **Ukrtelecom-impersonating PDFs** as the lure vector
- Payload: **JavaScript PicassoLoader variant** — novel for this campaign; prior generations were C-based per Mandiant + Microsoft 2020-2024 baseline
- **Ukrainian-IP geofiltering** — payload delivery restricted to Ukrainian-network egress
- **Cobalt Strike** delivered to validated victims
- ESET characterizes payload delivery as **operator-driven, not automated**
- Exploitation chain reuses **CVE-2023-38831** (WinRAR) and **CVE-2024-42009** (Roundcube XSS) — both patched

## A&D relevance

**Direct relevance LOW; partner-of-partner exposure only.** Polish + Lithuanian industrial sectors have downstream relationships with NATO-aligned DIB suppliers, but no US A&D prime is named as a victim. The campaign's targeting profile is Eastern European theater geopolitical, not A&D-prime.

## Source citations

- ESET (Damien Schaeffer): https://www.welivesecurity.com/en/eset-research/frostyneighbor-fresh-mischief-digital-shenanigans/
- Mandiant + Microsoft historical reporting (2020-2024 baseline; pre-Archimedes corpus)
- Polish ABW B-grade attestation per finding-2026-05-08-0009

## Related Archimedes records

- **Actor:** UNC1151 / Ghostwriter — **NOT in roster**; `/new-actor` flagged
- **Briefs:** see frontmatter `related_briefs:`
- **Related findings (referenced in brief, not yet verified on disk):** finding-2026-05-14-0001 (ESET surface), finding-2026-05-08-0009 (Polish ABW prior-corpus citation)
- **CVEs:** CVE-2023-38831 (WinRAR), CVE-2024-42009 (Roundcube XSS)

## Operator notes

`/new-actor UNC1151` is the next operator action if you want to scaffold this actor. Conservative grade at scoring run; multi-A-grade source coverage now supports MEDIUM-band candidacy.
