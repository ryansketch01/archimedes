---
raw_id: raw-2026-07-14-pm-008
collected_at: 2026-07-14T15:42:10-04:00
run_id: pre-brief-20260714-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: securityweek
  source_name: SecurityWeek (originating research Manifold)
  source_url: https://www.securityweek.com/unpatched-claude-for-chrome-flaw-lets-extensions-read-gmail-calendar/
  published_at: 2026-07-14T09:00:00-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [ClaudeBleed, Claude for Chrome, browser extension, unpatched, Gmail, Calendar]
triage_tags: [vuln_disclosure, unpatched, tracked_topic_continuation, no_itw, flash_1200_handoff]
iocs_extracted: true
iocs_count: 0
text_word_count: 175
promoted: true
promoted_to_finding: finding-2026-07-14-0011
promoted_at: 2026-07-14T16:05:00-04:00
ttl_expires_at: 2026-10-12T15:42:10-04:00
---

# ClaudeBleed-linked Claude for Chrome flaw persists across eight releases — malicious extensions can read Gmail, Docs, Calendar

Security firm **Manifold** reports that a vulnerability linked to the earlier **ClaudeBleed** issue remains unpatched in Claude for Chrome. (Carried forward from the 12:00 FLASH sweep non-FLASH grader queue; formalized to raw-signal this pre-brief. ClaudeBleed is an ongoing tracked topic in the Archimedes corpus.)

- **Nature:** a malicious browser extension can trigger Claude into performing actions on the user's behalf without genuine user approval. Stems from a weakness in Anthropic's fix for the original ClaudeBleed — Claude was restricted to pre-approved tasks but does not verify whether clicks actually originate from real users.
- **Exposed data:** Gmail messages, Google Docs, Calendar entries.
- **Disclosure timeline:** Manifold reported to Anthropic on 2026-05-21. Per Manifold, "none of the eight versions released since appear to patch the vulnerabilities, including the latest 1.0.80."
- **CVE:** none assigned per the source.
- **Anthropic response:** not yet public; SecurityWeek says it reached out for comment.
- **Exploitation:** no active exploitation reported. A second design gap (URL parameters) is noted but "not something an attacker can currently exploit."

---

## Extraction notes

- Language: en
- Publisher byline: Eduard Kovacs (SecurityWeek); originating research Manifold
- Article type: news
- Raw IOC extraction invoked: yes — no atomic IOCs present; no CVE assigned
- A&D relevance: low / structural — browser-agent data-exposure class; relevant to any enterprise (incl. A&D) piloting AI browser agents on corporate Google Workspace tenants. No A&D-named victim, no exploitation. Continuation of the tracked ClaudeBleed thread.
- No actor attribution (Hard Rule 2). No exploit detail copied (Hard Rule 3). Version string 1.0.80 recorded as affected-product context, not an IOC.

## IOCs (from ioc-extraction skill)

```yaml
extraction_metadata:
  source_brief_id: raw-2026-07-14-pm-008
  source_url: https://www.securityweek.com/unpatched-claude-for-chrome-flaw-lets-extensions-read-gmail-calendar/
  extracted_at: 2026-07-14T15:42:10-04:00
  extracted_by: collector
  target_actor_id: null
  text_word_count: 175

indicators: []

attribution_claims: []

benign_filtered: []

extraction_warnings:
  - type: no_cve_no_iocs
    ioc_id: null
    detail: "No CVE assigned, no atomic IOCs. Tracked-topic continuation (ClaudeBleed). Watch signal: Anthropic patch / CVE assignment / exploitation report."
```
