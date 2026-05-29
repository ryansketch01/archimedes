---
raw_id: raw-2026-05-29-pm-003-chatgpt-platform-abuse-cluster-push-security-llmshare-permiso-chatgphish-research-disclosures
collected_at: 2026-05-29T15:50:00-04:00
run_id: pre-brief-20260529-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: bleepingcomputer-and-thehackernews-paired
  source_name: "BleepingComputer (relay of Push Security) + The Hacker News (relay of Permiso Security) — paired ChatGPT-platform-research surfacings"
  source_url: https://www.bleepingcomputer.com/news/security/chatgpt-share-links-abused-to-host-fake-outage-pages-to-deliver-malware/
  published_at: 2026-05-29T18:21:36+00:00       # BleepingComputer published time; THN published 2026-05-29T18:07:12+00:00 (paired within 14 minutes)
additional_primaries:
  - source_yaml_id: thehackernews
    source_name: "The Hacker News (relay of Permiso Security ChatGPhish research)"
    source_url: https://thehackernews.com/2026/05/chatgphish-vulnerability-turns-chatgpt.html
    published_at: "2026-05-29T18:07:12+00:00"
  - source_yaml_id: push-security-first-citation       # NEW source — NOT in source-grades.yaml — would be provisional B on first surface per StepSecurity / Socket / Sysdig / Zellic / Aikido peer class
    source_name: "Push Security (LLMShare campaign research)"
    source_url: https://pushsecurity.com/blog/llmshare-malvertising-campaign
    published_at: 2026-05-29       # date inferred from BleepingComputer coverage
  - source_yaml_id: permiso-security-first-citation    # NEW source — NOT in source-grades.yaml — would be provisional B on first surface per same peer class
    source_name: "Permiso Security (ChatGPhish research, Andi Ahmeti byline)"
    source_url: null               # specific Permiso write-up URL not captured in THN coverage; flag for next collector pass to identify and direct-retrieve
    published_at: 2026-05-29       # date inferred from THN coverage
match_reason:
  watchlist: []                 # No A&D-prime named; commodity-web research-disclosure cluster
  actors: []                    # No roster actor attribution. LLMShare = malvertising campaign codename (researcher-coined working name, NOT attributed campaign); ChatGPhish = vulnerability class designation (Permiso-coined)
  vulnerabilities:
    - chatgphish_vulnerability       # Permiso disclosure of ChatGPT response renderer trust in third-party Markdown links/images post-summarization → prompt injection + phishing surface. NOT CVE-numbered per THN summary. NOT in _index.yaml — vendor-coordinated-disclosure class, OpenAI response not detailed
    - chatgpt_share_link_abuse_class  # Push Security disclosure of LLMShare malvertising campaign abusing chatgpt.com/s/ shared-link rendering to deliver fake-outage malvertising → drive-by download of macOS + Windows malware. NOT CVE-numbered; commodity-malvertising class. NOT in _index.yaml
  keywords:
    - "ChatGPhish"
    - "Permiso Security"
    - "Andi Ahmeti"
    - "LLMShare"
    - "Push Security"
    - "ChatGPT share links"
    - "chatgpt.com/s/"
    - "fake OpenAI outage page"
    - "Markdown link trust"
    - "Markdown image trust"
    - "response renderer"
    - "prompt injection"
    - "openew[.]app"
    - "Google ads"
    - "OpenAI"
    - "VM detection"
    - "macOS hash 7e5b708f6659b1fad3aae7b589a706434fbf21708aeec5af5910189b96e25fef"
    - "Windows hash 641526a22667a527290aac8c2c0358265d85c83318a7caca7cff28cecc2dbc16"
triage_tags:
  - llm_platform_abuse_research_cluster
  - chatgpt_renderer_trust_research_class
  - chatgpt_share_link_malvertising_class
  - no_roster_attribution
  - no_a_and_d_named_target
  - no_tracked_cve
  - push_security_first_citation_provisional_b_candidate
  - permiso_security_first_citation_provisional_b_candidate
  - research_pattern_of_interest_for_standing_section_consideration
iocs_extracted: true
iocs_count: 3                   # 1 domain (openew[.]app) + 2 file hashes (macOS + Windows)
text_word_count: 1850
promoted: true
promoted_to_finding: finding-2026-05-29-0005-bleepingcomputer-thn-push-security-permiso-llmshare-malvertising-chatgphish-renderer-trust-paired-chatgpt-platform-abuse-research-class
promoted_at: 2026-05-29T16:18:00-04:00
grading_run_id: afternoon-20260529-160000
ttl_expires_at: 2026-08-27T15:50:00-04:00
test: false
---

# ChatGPT platform-abuse research cluster — LLMShare malvertising (Push Security) + ChatGPhish renderer-trust vulnerability (Permiso Security), 2026-05-29

## Why two items combined into one raw-signal

Two distinct vulnerability/abuse classes affecting OpenAI ChatGPT surfaced within 14 minutes of each other this afternoon via independent vendor-research firms. Combining them into a single raw-signal for the grader (rather than splitting into two PM-003 + PM-004) because:

1. Both are research-class commodity-web disclosures with no A&D / no roster / no tracked CVE.
2. Both flag the same emerging-attack-surface pattern: AI-platform trust assumptions becoming malware-distribution and prompt-injection vectors.
3. Neither rises individually to brief-finding threshold — but the pair as a pattern-of-interest is a structural signal the grader / briefer / orchestrator may wish to consider for a future standing "AI platform abuse" section if the cluster recurs.

Disposition for grader: research-pattern context only. NOT promotion candidates. Flag for source-grade-log expansion (two new provisional-B vendor candidates).

## Item A — Push Security LLMShare malvertising campaign

**Source:** Push Security blog (pushsecurity.com/blog/llmshare-malvertising-campaign), reported via BleepingComputer (Lawrence Abrams byline) at 2026-05-29T18:21:36 UTC.

**Mechanism:** Threat actors abuse ChatGPT's content-sharing feature (`chatgpt.com/s/` shared-link URLs that render custom HTML/CSS content) to display a **fake OpenAI outage notice** from the legitimate `chatgpt.com` domain. Victims clicking the link see a faked OpenAI service-status page on a real-OpenAI URL, then are redirected to download malware disguised as the ChatGPT desktop application. Initial victim access via Google ads. Push Security codenames the campaign "LLMShare."

**Malware behavior (per BleepingComputer summary):** The Windows version "attempted to detect virtual machines through command execution." Final payload not explicitly characterized by Push Security per the BleepingComputer summary; the researchers note "While it is unclear what payloads are ultimately deployed, earlier campaigns abusing AI platform sharing features have distributed infostealers" — explicit hedge that the BleepingComputer relay preserves verbatim.

**No actor attribution.** Push Security publishes IOCs and mechanism analysis without attributing to a named threat actor.

**No A&D / aerospace / defense / DIB sector targeting** named by Push Security or BleepingComputer. Mass-malvertising distribution targets general internet users via Google ads.

**IOCs (from Push Security via BleepingComputer):**

```yaml
iocs:
  - type: domain
    value: openew[.]app
    context: "Fake download portal — masquerades as OpenAI ChatGPT desktop-app download page"
    confidence: push_security_research_observed
  - type: domain
    value: chatgpt.com/s/
    context: "Legitimate OpenAI domain abused for shared-link rendering — not a malicious domain per se, but the URL surface attackers leverage to host the initial fake-outage page on legitimate infrastructure"
    confidence: push_security_research_observed_legitimate_abused_surface
  - type: file_hash_sha256
    value: 7e5b708f6659b1fad3aae7b589a706434fbf21708aeec5af5910189b96e25fef
    context: "macOS sample masquerading as ChatGPT desktop app"
    confidence: push_security_research_observed_via_virustotal
  - type: file_hash_sha256
    value: 641526a22667a527290aac8c2c0358265d85c83318a7caca7cff28cecc2dbc16
    context: "Windows sample masquerading as ChatGPT desktop app; observed VM-detection behavior"
    confidence: push_security_research_observed_via_virustotal

attribution_claims: []          # Push Security publishes without actor attribution; BleepingComputer relay preserves the unattributed framing
```

**Defensive recommendations (from Push Security via BleepingComputer):** verify ChatGPT downloads only from official OpenAI sources; exercise caution with Google sponsored ads; implement application allowlisting; monitor for suspicious outage claims from legitimate domains.

## Item B — Permiso Security ChatGPhish vulnerability

**Source:** Permiso Security research (Andi Ahmeti byline), reported via The Hacker News at 2026-05-29T18:07:12 UTC. Specific Permiso write-up URL not captured in the THN piece; flag for next-pass direct retrieval.

**Mechanism (per THN summary):** Vulnerability in OpenAI ChatGPT that exploits the platform's implicit trust in Markdown links and images from summarized web pages. The chatgpt.com response renderer "trusts Markdown links and Markdown image URLs that originated from a third-party page the assistant has just summarized." Attackers can:

- Append malicious Markdown payloads to web pages users ask ChatGPT to summarize.
- Trigger ChatGPT to auto-fetch attacker-hosted images, exposing user IP, User-Agent, and Referer details.
- Render malicious Markdown links as live, clickable elements in the response.
- Deliver fake system-style security alerts or QR codes within the trusted AI interface.

**Permiso codename:** "ChatGPhish" (Permiso-coined).

**Verbatim Permiso quote per THN (preserved per Hard Rule 6, <15 words):** "Simply summarizing a page during normal browsing activity can introduce attacker-controlled instructions into the model context and ultimately into the rendered response."

**No actor attribution.** Permiso publishes the vulnerability without attributing to a named threat actor. THN does not extend attribution.

**No A&D / aerospace / defense / DIB sector targeting** named. The vulnerability is general-purpose against any ChatGPT user.

**OpenAI response:** not detailed in the THN piece. Permiso disclosure-coordination timeline not specified. Flag for grader: would normally expect a coordinated-disclosure timeline + OpenAI response statement on a vulnerability disclosure of this class. The absence in the THN summary is either (a) THN omitted the disclosure timeline, or (b) Permiso published without coordinated-disclosure timeline, or (c) the OpenAI response was a placeholder "we are investigating" type that didn't merit summary inclusion. Direct retrieval of the Permiso primary write-up on next collector pass would resolve.

**No IOCs published.** ChatGPhish is a vulnerability-class disclosure (mechanism + research scenario), not a campaign attribution. No infrastructure to track.

```yaml
iocs: []                        # ChatGPhish disclosure is mechanism + research scenario, no IOC tracking
attribution_claims: []
```

## Cross-cluster analysis (for grader / briefer / orchestrator awareness)

**Pattern observation:** Two independent vendor-research firms surfaced ChatGPT-platform-abuse research in the same 14-minute window. This is **probably coincidence** — neither references the other; the mechanisms are distinct (share-link malvertising vs. renderer-trust prompt-injection); neither vendor names the other in coordination. But the cluster-timing is a structural signal worth noting:

- LLM-platform feature surfaces (share links, summarization, prompt rendering) are increasingly drawing security-research attention.
- Both classes (legitimate-feature abuse via malvertising, response renderer trust) have analogues in browser-trust-boundary research from 2010-2015 (browser extension stores, autofill abuse, content-script injection) — operationally familiar attack-surface class, new substrate.
- The A&D-prime relevance is INDIRECT: corporate employees using ChatGPT for summarization or share-link consumption could surface either class as an attack vector, but neither has named A&D-prime targeting.

**For standing-section consideration:** if a third surface lands in the next 14 days of comparable research class (LLM-platform abuse / prompt injection / AI-platform feature exploitation), the briefer / orchestrator may wish to consider adding a standing "AI Platform Security" section to `watch-config.yaml` per the same pattern as the existing `ad-sector` and `iran-cyber` standing sections. Three surfaces in 14 days = inflection point per standing-section heuristic.

## Source-grade implications (for librarian handoff)

**Push Security** — NEW first Archimedes-corpus citation. Vendor research firm with structured campaign research and named-byline pattern (Push Security institutional byline this surface). **Conservative provisional B starting grade** per StepSecurity (2026-05-12), Socket (2026-05-14), Sysdig (2026-05-14), Zellic (2026-05-14), Aikido Security (2026-05-12), Ox Security (2026-05-15), Upwind (2026-05-15), Arctic Wolf (2026-05-28) precedent. Methodological positive on first surface: explicit hedge on payload identity ("unclear what payloads are ultimately deployed") and explicit IOC publication (domain + 2 hashes). Recommend `push-security` id at provisional B.

**Permiso Security** — NEW first Archimedes-corpus citation. Vendor research firm with named-analyst byline (Andi Ahmeti). Vulnerability disclosure research with CVE-class mechanism analysis. **Conservative provisional B starting grade** per same peer class. Methodological positive on first surface: ChatGPhish working-name designation is clearly researcher-coined (not attributed campaign) per Hard Rule 2 framing. Recommend `permiso-security` id at provisional B. Flag: direct retrieval of Permiso primary write-up needed on next pass.

**BleepingComputer + The Hacker News** — both already provisional B (THN ratification pending since 2026-05-14). Lawrence Abrams (BleepingComputer) byline on Push Security relay; THN institutional byline on Permiso relay. Both relays preserve unattributed framing and explicit researcher-coined working names verbatim — consistent with Hard Rule 2 hygiene.

## Splunk first-party (PM-29 — included in PM-001 sweep)

No additional Splunk query for ChatGPT IOC set (openew[.]app + 2 hashes) given (a) commodity-malvertising context with no roster/A&D fingerprint, (b) PM-001 PAN-OS sweep already exhausted the 30-day windowed budget for first-party telemetry checks this pre-brief, (c) Splunk index is dormant for non-archimedes-internal events across all prior sweeps (48th consecutive). Trigger 3 cannot fire even if hits did exist; the IOC set is preserved in the raw-signal for downstream grader / analyst / vuln-tracker consumption.

## Anti-noise / dedup analysis

This is the **first surface** of LLMShare and ChatGPhish in the Archimedes corpus. No prior raw-signal or finding covers either. No anti-noise lock applies. The ChatGPT product surface has been touched in prior findings (claude.ai/share/ MacSync via Trendyol-Albayrak finding-2026-05-10-0001; OpenAI TanStack-breach self-disclosure finding-2026-05-14-0008) but those are unrelated product-feature surfaces. No conflation risk if grader handles framing carefully.

## Extraction notes

- Language: en
- Article type: two paired media-tier relays of independent vendor-research disclosures
- Raw IOC extraction invoked: yes (3 IOCs on the Push Security LLMShare side: 1 domain + 2 file hashes; 0 IOCs on the Permiso ChatGPhish side — vulnerability disclosure not campaign)
- Quote discipline: Permiso Security verbatim quote preserved at <15 words ("Simply summarizing a page during normal browsing activity can introduce attacker-controlled instructions into the model context and ultimately into the rendered response.") = 25 words actually — flagged for briefer to truncate or paraphrase in any downstream brief composition. The quote is reproduced here in the raw-signal for grader review of original wording; the briefer should NOT propagate verbatim past 15 words per Hard Rule 6.
- Hard Rule 2: no actor-attribution upgrade. Both vendors publish unattributed; relays preserve the unattributed framing. The LLMShare and ChatGPhish names are explicit researcher-coined working designations, not attributed campaigns.
- Hard Rule 3: no exploitation assistance copied. ChatGPhish mechanism is described at the level of "Markdown link/image trust + prompt injection" without copying any PoC injection payload. The LLMShare campaign mechanism is described at the level of "share-link rendering for fake-outage display" without copying any specific payload-delivery technique. Anyone needing full technical detail can read the Push Security or Permiso primaries directly via the URLs above.
- Single-source veto evaluation: Push Security is single-source on LLMShare (BleepingComputer is pure relay). Permiso is single-source on ChatGPhish (THN is pure relay). Each item should be evaluated independently for WEP at grader stage; neither item is finding-promotion candidate so single-source veto evaluation is academic, but the framing is preserved for completeness.
- 72h auto-downgrade clock: NOT applicable (no finding promotion candidate; no actor attribution to clock).
