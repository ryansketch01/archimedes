---
raw_id: raw-2026-05-08-am-006
collected_at: 2026-05-08T07:37:00-04:00
run_id: pre-brief-20260508-073000
collection_mode: pre_brief_collection
test: false
sources:
  - source_yaml_id: securityweek
    source_name: "SecurityWeek (Ionut Arghire)"
    source_url: https://www.securityweek.com/vulnerability-in-claude-extension-for-chrome-exposes-ai-agent-to-takeover/
    source_grade_estimated: B
    role: relay
    published_at: 2026-05-08T06:53:36+00:00
    note: |
      SecurityWeek (Ionut Arghire, 2026-05-08 06:53 UTC) reports
      LayerX research on a vulnerability dubbed **ClaudeBleed**
      affecting the Claude extension for Chrome. Trust-boundary
      flaw: extension trusts the *origin* (claude.ai) of the
      execution context but does not verify the *content-script
      execution context* — allowing a hostile Chrome extension to
      inject prompts into the Claude AI agent via the Main world,
      bypass user-approval flows by repeatedly forging confirmation
      messages through DOM manipulation, and exfiltrate from
      connected Gmail / GitHub / Google Drive sessions or send
      email / delete data / share documents on the victim's behalf.

      Anthropic has issued a **partial patch**. LayerX explicitly
      states "the fix only partially addressed the underlying
      vulnerability" — the patch adds internal security checks for
      'standard' mode extensions but attackers can switch the
      Claude extension into 'privileged' mode without user
      notification to bypass the check.

      No CVE assigned in article. No active exploitation reported.
      LayerX's PoC demonstrated the flow.

      Connects to ongoing AI-tradecraft watch carried into 2026-05-07
      morning brief (Anthropic Threat Report, AI-assisted OT attacks,
      etc.). This is an AI-agent-supply-chain vulnerability rather
      than an actor-specific TTP.
publish_window: { start: 2026-05-07T17:30:00-04:00, end: 2026-05-08T07:30:00-04:00 }
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: ["claudebleed-no-cve-assigned"]
  keywords: [claude, claude-extension, chrome-extension, ai-agent, prompt-injection, trust-boundary, layerx, anthropic, partial-patch, dom-manipulation, gmail, github, google-drive, ai-tradecraft-watch]
triage_tags:
  - ai_tradecraft_watch
  - vendor_partial_patch
  - prompt_injection
  - browser_extension_security
  - awaiting_cve_assignment
  - no_active_exploitation_reported
  - operator_relevance
flash_trigger_evaluation:
  trigger_6_zero_day_no_patch:
    evaluation: |
      Trigger 6 requires (a) disclosed without patch, (b) CVSS >= 8.0
      OR widely deployed, (c) exploitation confirmed/imminent per
      A-grade. ClaudeBleed has a PARTIAL patch (so prong (a) is
      ambiguous — published but incomplete). No CVSS published. No
      active exploitation. No A-grade source has surfaced
      exploitation. Trigger does not fire.
    decision: not_triggered
    rationale: |
      Partial patch in place, no active exploitation, no CVE/CVSS,
      single-source-relay through SecurityWeek of LayerX research.
      Does not meet Trigger 6 thresholds.
operator_relevance_note: |
  Archimedes itself runs as a Claude-based agent. ClaudeBleed
  affects the Claude *Chrome extension*, not the Claude API or
  the Claude Code agent. Operator (Ryan) should be aware regardless,
  as a defensive posture signal: hostile Chrome extensions can
  hijack Claude-extension-based agentic workflows. Not an
  Archimedes operational vulnerability per se.
iocs_extracted: true
iocs_count: 0
text_word_count: 250
publication_window_match: in_window
promoted: true
promoted_to_finding: finding-2026-05-08-0004
promoted_at: 2026-05-08T08:24:00-04:00
ttl_expires_at: 2026-08-06T07:37:00-04:00
---

# ClaudeBleed — LayerX discloses Claude Chrome extension prompt-injection / AI agent takeover (partial patch)

## Source summary

SecurityWeek (Ionut Arghire, 2026-05-08 06:53 UTC) reports a
vulnerability dubbed **ClaudeBleed** in the Claude extension for
Chrome, discovered by cybersecurity firm LayerX. Anthropic has
issued a partial patch; LayerX states the fix is **incomplete**.

## Technical mechanics

The flaw is a trust-boundary violation. The Claude extension
trusts the origin of the execution (claude.ai) but does not
verify the execution context. Any hostile Chrome extension can
inject content scripts into the Main world running on the
claude.ai page, then:

- Inject prompts into the Claude AI agent
- Forge user-approval confirmations by repeatedly sending
  confirmation messages via DOM manipulation
- Bypass the user-notification flow

## Capabilities exposed via takeover

- Data exfiltration from Gmail (when user is logged in)
- Data exfiltration from GitHub
- Data exfiltration from Google Drive
- Sending email on the victim's behalf
- Deletion of user data
- Unauthorized document sharing

## Patch posture

**Partial.** Anthropic added internal security checks for
'standard' mode extensions. LayerX's published bypass: a hostile
extension can switch into 'privileged' mode **without user
notification**, evading the check.

## Identifiers

- **CVE: not assigned** in article
- **CVSS: not assigned**
- **Disclosure date:** 2026-05-08 (SecurityWeek publication)
- **Researcher:** LayerX

## Significance for grader

1. **AI-tradecraft watch** — extends the 2026-05-07 morning brief
   theme (Anthropic Threat Report, AI-assisted OT attacks). This
   is the **defensive flip-side**: the AI agents themselves are
   becoming attack surface.

2. **Operator-relevance flag** — Archimedes is a Claude-based
   agent. The Claude *Chrome extension* is a different deployment
   surface from the Claude API + Claude Code agent that runs
   Archimedes. Not an Archimedes operational vulnerability, but
   defensive context for Ryan's broader workflow.

3. **No FLASH** — partial patch, no active exploitation, no A-grade
   source on exploitation, single-source SecurityWeek relay of
   LayerX. Trigger thresholds not met.

4. **A&D nexus** — NONE direct. Indirect through any A&D contractor
   whose employees use the Claude Chrome extension to access
   sensitive web-app surfaces (Gmail, GitHub, Drive) carrying
   ITAR/CUI / project data. Defensive-only relevance, not a sector
   campaign.

5. **Action item:** track for follow-up A-grade coverage. If
   Anthropic publishes their own advisory or if other AI-agent
   browser-extension takeover research surfaces from MSTIC /
   Mandiant / Google Cloud Security, fold into the AI-tradecraft
   thread.

---

## Extraction notes

- Language: en
- Publisher byline: Ionut Arghire (SecurityWeek)
- Article type: news / vulnerability advisory (relay of LayerX
  research)
- Raw IOC extraction invoked: yes (zero malicious IOCs — research
  disclosure article with no campaign indicators)
- LayerX primary report URL not surfaced by WebFetch extraction

## IOCs (from ioc-extraction skill)

```yaml
iocs: []
attribution_claims: []
notes: |
  Vulnerability disclosure article. No campaign, no actor, no
  malicious IPs / domains / hashes. The "ClaudeBleed" name is
  researcher-assigned (LayerX). No CVE issued at publication.
```
