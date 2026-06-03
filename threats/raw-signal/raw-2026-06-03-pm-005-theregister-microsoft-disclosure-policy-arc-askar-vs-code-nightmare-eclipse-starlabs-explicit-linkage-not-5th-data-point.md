---
raw_id: raw-2026-06-03-pm-005-theregister-microsoft-disclosure-policy-arc-askar-vs-code-nightmare-eclipse-starlabs-explicit-linkage-not-5th-data-point
collected_at: 2026-06-03T15:37:00-04:00
run_id: pre-brief-20260603-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: theregister
  source_name: The Register — "Another bug hunter leaks Microsoft exploits in defiance of company's handling of vulnerability disclosures"; Askar VS Code zero-day + Nightmare-Eclipse + StarLabs meta-narrative
  source_url: https://www.theregister.com/security/2026/06/03/another-bug-hunter-leaks-microsoft-exploits-in-defiance-of-companys-handling-of-vulnerability-disclosures/5250590
  published_at: 2026-06-03T14:30:00+00:00              # 10:30 EDT, in-window
source_grade: B
additional_sources:
  - related_finding: finding-2026-06-03-0002
    role: "AM brief finding on Askar VS Code zero-day — this PM raw-signal is meta-arc update-on"
  - related_finding: finding-2026-06-02-0010
    role: "Prior-day Bitskrieg / Nightmare-Eclipse watch — referenced for arc continuity"
  - related_watch_signal: microsoft_disclosure_policy_arc_5th_data_point
    role: "AM brief watch_signal; this PM raw-signal documents that arc data-point count remains at 4, NOT lifted to 5 by The Register meta-coverage"
date: 2026-06-03
topic: theregister-microsoft-disclosure-policy-arc-askar-vs-code-zero-day-nightmare-eclipse-six-zero-days-three-itw-starlabs-vs-code-xss-ineligible-mscr-digital-crimes-unit-backdown-meta-narrative-not-fifth-data-point
match_reason:
  watchlist: []                                       # No A&D-watchlist entity. Meta-coverage of disclosure-policy arc.
  actors: []                                          # No tracked-roster actor. "Nightmare Eclipse" is a researcher pseudonym, not a tracked APT.
  vulnerabilities: []                                 # No new CVE; the AM-brief watch_signal is the canonical container.
  keywords:
    - "Microsoft disclosure policy"
    - "MSRC"
    - "Ammar Askar"
    - "VS Code"
    - "github.dev"
    - "OAuth token theft"
    - "Nightmare Eclipse"
    - "six zero-days"
    - "three confirmed ITW"
    - "StarLabs"
    - "VSCode XSS ineligible"
    - "Microsoft Digital Crimes Unit"
    - "DCU backdown"
    - "full disclosure"
    - "responsible disclosure"
    - "watch_signal arc"
triage_tags: [pm_pre_brief, update_on_am_watch_signal, meta_coverage, arc_continuity, not_fifth_data_point, no_actor_attribution, microsoft_disclosure_policy_arc]
iocs_extracted: false                                 # Meta-coverage; no IOCs.
iocs_count: 0
text_word_count: ~600
promoted: false
rejected_at: 2026-06-03T16:28:00-04:00
rejection_id: reject-2026-06-03-0002
rejection_grading_run_id: afternoon-20260603-160000
rejection_reason_short: anti_noise_arc_narrative_meta_coverage_watch_signal_data_point_count_remains_at_4
ttl_expires_at: 2026-09-01T15:37:00-04:00
---

# The Register — "Another bug hunter leaks Microsoft exploits in defiance"; Askar VS Code zero-day + Nightmare-Eclipse + StarLabs explicit-linkage meta-narrative; NOT a fifth Microsoft-disclosure-policy data point (watch_signal arc remains at 4)

## What The Register adds vs. AM brief finding-2026-06-03-0002

The AM brief finding-2026-06-03-0002 covered Ammar Askar's VS Code github.dev OAuth-token-theft zero-day disclosure with full-disclosure-after-1-hour rationale, citing prior MSRC experience. The Register (2026-06-03T14:30 UTC = 10:30 EDT, in-window) adds the following NEW meta-narrative content:

### New meta-narrative content

1. **Nightmare Eclipse explicit count and ITW status:** "The researcher has so far released six zero-days, three of which were quickly confirmed to be exploited by attackers in the wild." This is the most explicit Archimedes-corpus statement of the Nightmare-Eclipse count + ITW ratio to date.
2. **StarLabs VS Code XSS reference as evidence MSRC has NOT improved:** Askar verbatim per The Register, "Taking a look at a recent report by Starlabs on a VSCode XSS bug marked as ineligible and low severity, it doesn't look like MSRC has gotten any better about VSCode bugs." This is the **explicit fourth data point** in the AM-brief watch_signal arc — already counted at 4 in the AM watch_signals_set framing.
3. **Microsoft Digital Crimes Unit backdown:** "After the sixth zero-day, Microsoft vaguely threatened the researcher with its Digital Crimes Unit, which works closely with law enforcement, before quickly backing down after an outpouring of negative responses." This is new framing not in the AM brief — Microsoft's threatened-DCU-then-backed-down posture toward Nightmare Eclipse is now in the open record.
4. **Askar disclosure cycle verbatim:** "To summarize the last time I interacted with MSRC regarding reporting a VSCode bug, it was a horrible experience where they silently fixed the bug I pointed out without any credit. They also marked it as not having any security impact." [verbatim ~30 words — internal note for grader; if quoted in brief, observe Hard Rule 7 15-word limit].
5. **Askar's stated motivation as policy lever:** "this is one of the few levers I have to try to influence MSRC and the security posture of VSCode" — full-disclosure-as-policy-lever framing.

### Why this is NOT a fifth data point

The AM brief watch_signal `microsoft_disclosure_policy_arc_5th_data_point` is defined as: "If a fifth independent decline-to-patch / full-disclosure event surfaces in next 14d → analyst SAT-ACH."

The arc data-point count as of the AM brief:

1. **Bitskrieg / Nightmare Eclipse** — six zero-days, three ITW (AM brief finding-2026-06-02-0010)
2. **Askar VS Code github.dev zero-day** (AM brief finding-2026-06-03-0002)
3. **Windows Search URI NTLMv2 leak — Microsoft declined remediation** (AM brief finding-2026-06-03-0004 via Huntress/Andrew Schwartz)
4. **StarLabs VS Code XSS marked ineligible / low severity** — surfaced explicitly via Askar's complaint, AM brief reflects this implicitly via "Microsoft disclosure-policy current — two new data points in ~30h; arc now at four"

The Register's piece does NOT introduce a fifth independent disclosure event. It is **meta-arc consolidation** — naming the arc explicitly, counting Nightmare-Eclipse zero-days, and adding the DCU-backdown context. **Watch_signal data-point count remains at 4. The 14-day clock from AM brief continues.**

## A&D operator-profile relevance

**Indirect.** A&D primes use VS Code + github.dev extensively for development workflows; the github.dev OAuth-token-theft surface (AM finding-0002) is the direct A&D-prime defensive interest. The disclosure-policy arc itself is a Microsoft-relations / vendor-relationship signal more than an immediate-defensive signal.

**Watch_signal posture:** continue tracking for a fifth independent disclosure event. If a fifth event surfaces in the next ~13 days (watch_signal clock from AM brief 2026-06-03), the analyst SAT-ACH (Analysis of Competing Hypotheses) should be invoked per the AM brief watch_signals_set framing.

## Coverage hierarchy

- **AM brief finding-2026-06-03-0002** is the source of record for the Askar VS Code zero-day in the corpus.
- **AM brief finding-2026-06-03-0004** is the source of record for the Windows Search URI NTLMv2 leak (third disclosure-policy data point).
- **Prior-day finding-2026-06-02-0010** is the source of record for the Nightmare-Eclipse / Bitskrieg watch.
- **This PM raw-signal** is meta-arc update with new framing (Nightmare-Eclipse count + ITW ratio, StarLabs explicit-link, DCU-backdown). Grader can fold into the AM brief watch_signal narrative or roll into a unified "disclosure-policy arc" PM brief surface.

## Sources

- The Register (primary in-window): https://www.theregister.com/security/2026/06/03/another-bug-hunter-leaks-microsoft-exploits-in-defiance-of-companys-handling-of-vulnerability-disclosures/5250590
- AM brief findings: threats/findings/finding-2026-06-03-0002.md, threats/findings/finding-2026-06-03-0004.md
- Prior-day finding: threats/findings/finding-2026-06-02-0010.md (Bitskrieg watch)

## Extraction notes

- Language: en
- Article type: media meta-coverage / framing piece
- Raw IOC extraction invoked: no — meta-coverage; no actor IOCs.
- No PoC code reproduced per Hard Rule 3. (The Register includes detailed technical walkthrough of the VS Code OAuth flow; not reproduced here. AM brief finding-0002 covers the operationally relevant technical detail; further detail at the article URL.)
- Hard Rule 7 quote limit observed: brief should pick ONE short quote (under 15 words) from either Askar OR the Microsoft-DCU-backdown framing if PM brief carries this surface.
- No credentials surfaced.
- No new attribution claims.
