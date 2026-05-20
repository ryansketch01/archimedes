---
raw_id: raw-2026-05-20-pm-003
collected_at: 2026-05-20T15:34:00-04:00
run_id: pre-brief-20260520-153000
collection_mode: pre_brief_collection
test: false
source:
  source_yaml_id: securityweek
  source_name: "SecurityWeek (Eduard Kovacs)"
  source_url: https://www.securityweek.com/anthropic-silently-patches-claude-code-sandbox-bypass/
  published_at: 2026-05-20T09:00:00-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities:
    - CVE-2025-66479
  keywords:
    - Anthropic Claude Code
    - sandbox bypass
    - SOCKS5 hostname null-byte injection
    - network allowlist bypass
    - silent patch
    - Aonan Guan researcher
    - prompt injection chain
    - Comment and Control
    - environment variables credentials tokens infrastructure data exfiltration
    - Claude Code 2.1.88 patched 2026-03-31
    - no CVE assigned to second bypass
    - CVE-2025-66479 first bypass sandbox-runtime library
triage_tags:
  - in_window
  - securityweek_b_grade_provisional_relay
  - anthropic_silent_patch_no_vendor_release_notes
  - claude_code_2_1_88_fix_2026_03_31
  - socks5_null_byte_injection_network_allowlist_bypass
  - prompt_injection_plus_sandbox_bypass_chain_described_by_researcher
  - aonan_guan_independent_researcher_first_corpus_citation_provisional_grade_review_candidate
  - no_in_the_wild_exploitation_observed
  - vendor_silent_patch_pattern_no_cve_for_second_bypass
  - claude_code_supply_chain_sdlc_adjacency_to_teampcp_mini_shai_hulud_am_001_claim
  - ad_relevance_indirect_claude_code_increasingly_in_enterprise_sdlc
  - trigger_1_failed_no_active_exploitation
  - trigger_6_failed_patched_2026_03_31
  - non_flash_morning_brief_grader_awareness_candidate
  - hard_rule_3_no_poc_link_no_exploit_walkthrough_extracted
  - splunk_first_party_zero_hits_49th_consecutive_dormant_sweep
iocs_extracted: false
iocs_count: 0
text_word_count: 720
promoted: true
promoted_to_finding: finding-2026-05-20-0007
promoted_at: 2026-05-20T16:25:00-04:00
ttl_expires_at: 2026-08-18T15:34:00-04:00
---

# Anthropic silently patches Claude Code sandbox bypass (SecurityWeek, 2026-05-20)

SecurityWeek (Eduard Kovacs byline) reports that independent researcher
Aonan Guan disclosed a second sandbox bypass in Anthropic's Claude Code
that was silently patched in Claude Code 2.1.88 (released 2026-03-31)
without an associated CVE identifier or vendor release-note mention.

Source URL: `https://www.securityweek.com/anthropic-silently-patches-claude-code-sandbox-bypass/`

## Researcher and disclosure pattern

- Researcher: Aonan Guan (independent; first Archimedes-corpus citation —
  no prior corpus track record observed in source-grade-log to date; this
  would be a first-surface provisional grade review candidate alongside
  the depthfirst / Berk Albayrak / LayerX precedents if subsequent
  Archimedes-corpus citations occur)
- Researcher reported to Anthropic: 2026-04-03
- Anthropic disposition observed by researcher:
  - Vendor assigned no CVE identifier to the second bypass
  - Vendor did not mention the issue in Claude Code 2.1.88 release notes
  - Vendor did not publicly acknowledge the fix
- Researcher commentary captured in SecurityWeek piece criticizes the
  silent-patch disposition; no public Anthropic statement is referenced.

## Technical mechanism (per SecurityWeek; no PoC reproduction)

Per Hard Rule 3, Archimedes does not reproduce PoC content. What
SecurityWeek published is a high-level mechanism description:

- The bypass leverages SOCKS5 hostname null-byte injection against Claude
  Code's network allowlist filter
- Researcher characterizes the issue: a user policy of "allow only
  *.google.com" can be bypassed by sending a hostname like
  `attacker-host.com\x00.google.com` — the filter sees the trailing
  `.google.com` and approves the connection, then the operating system
  truncates the hostname at the null byte and dials out to
  `attacker-host.com`
- Effect: bypass of the network-restriction sandbox component of Claude
  Code, enabling outbound network connections to attacker-controlled
  hosts that the deployed policy intends to deny.

## Exploitation chain framing per researcher

Per SecurityWeek, the researcher described an exploitation chain
combining a prompt-injection vector ("Comment and Control") with the
SOCKS5 null-byte sandbox bypass. The researcher's stated impact was
exfiltration of "environment variables, credentials, tokens, and
infrastructure data" via attacker-controlled outbound connections from
the Claude Code execution context.

No in-the-wild exploitation observed per SecurityWeek's reporting.

## Related CVE on first bypass (unrelated underlying library)

- CVE-2025-66479 — assigned to the 'sandbox-runtime' library on the first
  sandbox bypass (a separate, unrelated issue surfaced earlier in the
  researcher's coordinated disclosure timeline)
- Per SecurityWeek: the CVE was assigned to the 'sandbox-runtime' library,
  NOT to Claude Code itself
- This first-bypass CVE is configuration-related rather than the SOCKS5
  null-byte mechanism above; collector flags both for grader awareness on
  the disclosure-discipline angle

## Patch timeline

- Vulnerability present in Claude Code: 2025-10-20 → 2026-03-31
- Fix committed: 2026-03-27
- Shipped in Claude Code 2.1.88: 2026-03-31
- Researcher reported to Anthropic: 2026-04-03 (post-patch coordinated
  disclosure; the researcher reported the issue AFTER Anthropic had
  already silently fixed it — observed via independent commit / version
  diff)

## A&D and Archimedes-corpus adjacency

- A&D direct relevance: indirect. Claude Code is an AI coding agent
  increasingly being trialed and adopted inside enterprise SDLCs,
  including organizations with A&D-prime supplier-tier exposure. A
  sandbox bypass in a code-execution agent that exfiltrates "environment
  variables, credentials, tokens, and infrastructure data" is directly
  relevant to enterprise CI/CD threat models, but no A&D-prime is named
  as a deployer or victim in this disclosure.
- Archimedes-corpus adjacency 1: raw-2026-05-20-am-001 (SecurityWeek Mini
  Shai-Hulud @antv 320+ npm packages) explicitly cited TeamPCP TTP delta
  including a "Claude Code backdoor drop" mechanism. The mechanism in
  AM-001 is a Claude Code-related supply-chain mechanism by attacker —
  NOT the same surface as the network-allowlist sandbox bypass in PM-003
  — but the grader / actor-profiler will likely want to track the Claude
  Code attack surface as a coherent operational target across both
  vendor-self-disclosure (Anthropic silent patch) and attacker-leveraged
  use (TeamPCP TTP claim).
- Archimedes-corpus adjacency 2: AI-agent security tooling cluster in
  window — Microsoft RAMPART + Clarity released same day (see PM-005
  awareness file) targeting agentic AI red-team / safety testing in
  enterprise SDLCs. Industry-wide attention is converging on agentic AI
  security in May 2026.

## FLASH trigger evaluation (collector-side)

- **Trigger 1 (critical-cve-exploited):** No CVE assigned to second
  bypass; no in-the-wild exploitation. Does not fire.
- **Trigger 6 (zero-day-no-patch):** Patched in Claude Code 2.1.88 on
  2026-03-31 — fix predates this disclosure by ~7 weeks. Not zero-day
  per Trigger 6 definition. Does not fire.

Non-FLASH morning-brief grader-awareness candidate.

## Citations within Hard Rule 7 budget

- SecurityWeek / researcher Aonan Guan quoted in piece: "environment
  variables, credentials, tokens, and infrastructure data" (8 words —
  within 15-word per-source limit, single quote per source budget).

## Extraction notes

- Language: en
- Publisher byline: Eduard Kovacs (SecurityWeek senior contributor)
- Article type: security media research-disclosure relay
- Raw IOC extraction invoked: no (no actor IOCs in the piece; the SOCKS5
  null-byte mechanism is presented as a researcher PoC, not in-the-wild
  IOC enumeration)

## IOCs

None published in the SecurityWeek surface. No active-exploitation IOCs
to extract.
