---
raw_id: raw-2026-05-30-flash-0000-001-mstic-33-malicious-npm-dependency-confusion-recon-only-mode-oob-moika-tech-c2-no-roster-attribution-no-ad-nexus-am-handoff
collected_at: 2026-05-30T00:20:00-04:00
run_id: flash-sweep-20260530-000000
collection_mode: flash_sweep
source:
  source_yaml_id: mstic
  source_name: Microsoft MSTIC (Microsoft Security Blog)
  source_url: https://www.microsoft.com/en-us/security/blog/2026/05/29/33-malicious-npm-packages-abuse-dependency-confusion-profile-developer-environments/
  source_grade: A
  published_at: 2026-05-29T20:06:20-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [npm, dependency-confusion, supply-chain, recon, postinstall, RECON_ONLY, two-phase, Sberbank, yandex.ru]
triage_tags: [non_flash, am_handoff, npm_supply_chain, fresh_a_grade_research]
candidate_triggers: []
iocs_extracted: true
iocs_count: 23
text_word_count: 1180
promoted: true
promoted_to_finding: finding-2026-05-30-0001-mstic-33-malicious-npm-dependency-confusion-recon-only-mode-oob-moika-tech-c2-three-aliases-no-roster-attribution-no-ad-nexus
promoted_at: 2026-05-30T08:05:00-04:00
ttl_expires_at: 2026-08-28T00:20:00-04:00
test: false
flash_sweep_disposition: |
  Evaluated against all 6 FLASH triggers in 0000 sentinel. Zero triggers fire.
  Trigger 1: no CVE. Trigger 2: MSTIC explicitly declines APT attribution; three new
  aliases not in roster. Trigger 3: Splunk targeted query on full IOC set returned
  zero defenseclaw_local + zero archimedes events. Trigger 4: cannot fire absent
  roster attribution; dependency confusion + postinstall is a well-established TTP
  primitive, not a novel class. Trigger 5: financial services (Sberbank) + general
  dev infrastructure target set; explicit absence of A&D / DIB / ITAR / defense
  contractor scope. Trigger 6: no CVE-class vulnerability.
  Disposition: hand off to 07:30 AM-30 collector for grader evaluation as a
  regular finding candidate. Pre-positioning extraction here so AM collector does
  not re-fetch / re-extract.
---

# Malicious npm packages abuse dependency confusion to profile developer environments

**Microsoft Threat Intelligence (Microsoft Defender Security Research Team) — 2026-05-29T20:06 EDT**

## Source title and byline

Title: "Malicious npm packages abuse dependency confusion to profile developer environments"
Author: Microsoft Defender Security Research Team
Published: 2026-05-29T20:06:20 EDT (= 2026-05-30T00:06:20 UTC)
URL: https://www.microsoft.com/en-us/security/blog/2026/05/29/33-malicious-npm-packages-abuse-dependency-confusion-profile-developer-environments/

## Summary (no quoted material > 15 words per Rule 7)

MSTIC published mid-evening 2026-05-29 a fresh analysis of an active npm supply-chain attack: 33 malicious packages registered under nine spoofed organizational scopes employing dependency confusion to drop an obfuscated reconnaissance payload during npm install. Three maintainer aliases (mr.4nd3r50n, ce-rwb, t-in-one) — all yandex.ru email addresses — published two bursts (May 28 18:47–19:03 UTC and May 29 09:01–09:02 UTC). MSTIC's forensic analysis assesses with high confidence the three accounts are operated by a single individual. All packages ship the same ~7 KB obfuscated postinstall stager that posts to one C2 endpoint (`oob.moika[.]tech`) gated by a hardcoded shared secret (`l95HdDaz3kQx1Zsg3WxH6HvKANf51RY1`). Payload is platform-specific (Windows / macOS / Linux), runs in RECON-ONLY mode currently (a server-side toggle exists for follow-on exploitation), and performs environment fingerprinting + credential reconnaissance via environment variables passed to a detached process. Several scope names target Russian-language enterprise software ecosystems (Sberbank's SberPay, Wildberries shape, Trendyol/Trendyol-Tinkoff-shape). MSTIC + npm team coordinated removal of all packages before publication.

## MSTIC attribution language — verbatim short quote per Rule 7

MSTIC does NOT attribute to a named APT or known group. The attribution is **operator-level only** ("high-confidence evidence that the three accounts are operated by the same individual" — direct quote ~14 words, within Rule-7 limit). No nation-state assessment. No tracked-actor link. No Shai-Hulud or TeamPCP lineage claim despite operating in adjacent territory.

## Why this is novel research and not absorbed

Corpus grep across `threats/` for `moika`, `4nd3r50n`, `ce-rwb`, `t-in-one`, "dependency confusion", "33 malicious" — zero prior mentions. This is a first-Archimedes-corpus surfacing of the cluster. The mr.4nd3r50n account's first npm activity dates to April 2024 (v0.0.0 packages tagged "Bugbounty"), then a ~2-year quiet period, then malicious activity 2026-05-28. The other two accounts are new-2026.

## TTP class — note for analyst downstream

Dependency confusion as a primitive is well-documented since Birsan 2021. Postinstall hooks as a delivery mechanism is documented across Lazarus / Stardust Chollima / Shai-Hulud / TeamPCP / Mini Shai-Hulud npm work since at least 2023. RECON_ONLY + two-phase design (recon now, exploit later) is the methodological signature worth flagging — it is what differentiates a supply-chain campaign that intends quiet long-tail data collection from one that intends immediate compromise. Inflated version numbers (100.100.100, 99.5.7, 99.5.8) as the dependency-confusion winning tactic is also well-established. The novelty here is the **specific cluster + the X-Secret-gated C2 + the bug-bounty-to-malware operator lifecycle**, not a TTP-class shift.

## A&D nexus check — important for grader

**No A&D nexus.** The named or impersonated target ecosystems are:
- @sber-ecom-core (Sberbank — Russian retail bank)
- @capibar.chat (unclear — likely consumer messaging clone)
- @wb-track (likely Wildberries — Russian e-commerce, no A&D scope)
- @data-science, @cloudplatform-single-spa, @payments-widget, @travel-autotests, @ce-rwb, @t-in-one (generic dev infrastructure shapes)

The MSTIC report makes zero defense-contractor / DIB / ITAR / aerospace references. The lure surface is consumer fintech + e-commerce + generic enterprise dev infrastructure with a Russia-speaking inflection. Structural relevance to an A&D prime is **indirect at most** — a defense prime's developer environment IS exposed to dependency confusion class attacks broadly, but this specific cluster is not targeting that surface.

## First-party Splunk check (Trigger 3 pre-check)

`index=defenseclaw_local OR index=archimedes ("oob.moika.tech" OR "moika.tech" OR "mr.4nd3r50n" OR "ce-rwb" OR "t-in-one" OR "ogvanta" OR "l95HdDaz3kQx1Zsg3WxH6HvKANf51RY1" OR "sberpay-widget" OR "capibar.chat" OR "sber-ecom-core") earliest=-24h@h`

Result: **zero events** (last 24h). Zero defenseclaw_local hits. Hard Rule 8: silence is not disconfirming, just absent — but no first-party hit means Trigger 3 does not fire.

## Lineage claim check

MSTIC does not link to Shai-Hulud, TeamPCP, Mini Shai-Hulud, or any prior named supply-chain campaign in this writeup. The cluster is presented as standalone. The grader downstream may want to consider whether the X-Secret-gated C2 architecture, the inflated-version tactic, and the bug-bounty-account-lifecycle constitute a TeamPCP-adjacent or distinct-cluster signal, but **MSTIC does not make that claim and Archimedes per Rule 2 does not originate attribution**.

---

## Extraction notes

- Language: en
- Article type: vendor threat-intel blog (Microsoft Security Blog / Microsoft Threat Intelligence MSTIC)
- Source grade: A (per source-grades.yaml mstic entry; tier-1 vendor research, Defender telemetry-backed nation-state tracking practice)
- Raw IOC extraction invoked: yes (full IOC set captured below)
- Article type: blog
- Publisher byline: Microsoft Defender Security Research Team

## IOCs (full enumeration for AM-30 grader and future ioc-extraction skill invocation)

```yaml
indicators:
  - type: domain
    value: oob.moika.tech
    role: c2
    confidence: high  # MSTIC published as C2 with X-Secret-gated three-platform payload delivery
    first_seen: 2026-05-28
    source: MSTIC 2026-05-29
    notes: "Single C2 host serving /payload/win, /payload/mac, /payload/linux. Coordinated takedown initiated with npm; C2 likely still alive."

  - type: url
    value: https://oob.moika.tech/payload/win
    role: c2_payload_delivery
    confidence: high
    source: MSTIC 2026-05-29

  - type: url
    value: https://oob.moika.tech/payload/mac
    role: c2_payload_delivery
    confidence: high
    source: MSTIC 2026-05-29

  - type: url
    value: https://oob.moika.tech/payload/linux
    role: c2_payload_delivery
    confidence: high
    source: MSTIC 2026-05-29

  - type: email
    value: mr.4nd3r50n@yandex.ru
    role: npm_maintainer_alias
    confidence: high
    source: MSTIC 2026-05-29

  - type: email
    value: ogvanta@yandex.ru
    role: npm_maintainer_alias
    confidence: high
    source: MSTIC 2026-05-29
    notes: "Account name 'ce-rwb' / email 'ogvanta' mismatch — likely deliberate operator OPSEC."

  - type: email
    value: t-in-one@yandex.ru
    role: npm_maintainer_alias
    confidence: high
    source: MSTIC 2026-05-29

  - type: npm_account
    value: mr.4nd3r50n
    role: malicious_publisher
    confidence: high
    activity_window: 2024-04 (Bugbounty v0.0.0 staging) + 2026-05-28 (active malware publishing)
    package_count: 26
    source: MSTIC 2026-05-29

  - type: npm_account
    value: ce-rwb
    role: malicious_publisher
    confidence: high
    activity_window: 2026-05-28 (active malware publishing)
    package_count: 7
    source: MSTIC 2026-05-29

  - type: npm_account
    value: t-in-one
    role: malicious_publisher
    confidence: high
    activity_window: 2026-05-29 (active malware publishing) + pre-staged 2026-05-04 (@capibar.chat/ui-kit 99.0.7 + @sber-ecom-core/sberpay-widget 99.0.7)
    package_count: 12
    source: MSTIC 2026-05-29

  - type: shared_secret
    value: l95HdDaz3kQx1Zsg3WxH6HvKANf51RY1
    role: x_secret_header_gate_on_c2_request
    confidence: high
    source: MSTIC 2026-05-29
    notes: "Hardcoded into postinstall stager; required to receive payload from C2. Defensive detection opportunity: any HTTP request carrying X-Secret: l95HdDaz3kQx1Zsg3WxH6HvKANf51RY1 to any host."

  - type: npm_scope
    value: "@cloudplatform-single-spa"
    role: dependency_confusion_target
    source: MSTIC 2026-05-29

  - type: npm_scope
    value: "@wb-track"
    role: dependency_confusion_target
    source: MSTIC 2026-05-29
    notes: "Likely Wildberries-shaped impersonation."

  - type: npm_scope
    value: "@data-science"
    role: dependency_confusion_target
    source: MSTIC 2026-05-29

  - type: npm_scope
    value: "@ce-rwb"
    role: dependency_confusion_target
    source: MSTIC 2026-05-29

  - type: npm_scope
    value: "@payments-widget"
    role: dependency_confusion_target
    source: MSTIC 2026-05-29

  - type: npm_scope
    value: "@travel-autotests"
    role: dependency_confusion_target
    source: MSTIC 2026-05-29

  - type: npm_scope
    value: "@t-in-one"
    role: dependency_confusion_target
    source: MSTIC 2026-05-29

  - type: npm_scope
    value: "@capibar.chat"
    role: dependency_confusion_target
    source: MSTIC 2026-05-29

  - type: npm_scope
    value: "@sber-ecom-core"
    role: dependency_confusion_target
    source: MSTIC 2026-05-29
    notes: "Direct Sberbank SberPay payment widget impersonation."

  - type: domain
    value: github.cloudplatform-single-spa.io
    role: spoofed_enterprise_metadata
    confidence: high
    source: MSTIC 2026-05-29
    notes: "Fake repository URL in package.json — not an actual GitHub Enterprise instance. Detection opportunity for any environment that resolves or attempts to fetch from this hostname."

  - type: domain
    value: docs.cloudplatform-single-spa.io
    role: spoofed_enterprise_metadata
    confidence: high
    source: MSTIC 2026-05-29

  - type: domain
    value: jira.cloudplatform-single-spa.io
    role: spoofed_enterprise_metadata
    confidence: high
    source: MSTIC 2026-05-29

  - type: detection_pattern
    value: "npm install postinstall hook + HTTPS GET to oob.moika.tech/payload/{win,mac,linux} with X-Secret header"
    role: behavior_signature
    confidence: high
    source: MSTIC 2026-05-29

  - type: filename
    value: "scripts/postinstall.js"
    role: malware_stager
    notes: "Obfuscator.io-style obfuscation, ~7 KB"
    confidence: high
    source: MSTIC 2026-05-29

attribution_claims: []
# MSTIC explicitly declines APT / nation-state attribution. Operator-level
# attribution only ("three accounts operated by the same individual" with
# high confidence per forensic npm registry metadata analysis). No tracked
# actor in roster matches. Per Hard Rule 2 Archimedes does not originate
# attribution; the empty list is the correct record.
```

## Recommendation for AM-30 grader

This is a strong A-grade candidate finding for the 2026-05-30 morning brief. Suggested treatment:
- Source convergence: MSTIC sole primary at this hour. Likely BleepingComputer / The Hacker News / Socket relays land overnight or in the AM collector window — check before publishing.
- WEP candidate: "likely" — MSTIC's high-confidence operator attribution is well-supported; the absence of named-actor attribution rather than weak attribution.
- Defensive priority: HIGH for any organization running npm-based developer environments without scope/maintainer allowlisting. Detection patterns are clean (X-Secret header value is a unique strong signal; oob.moika.tech as a DNS/proxy block is trivial).
- A&D relevance: structural / indirect. The mechanism applies broadly to any dev environment, but this specific cluster targets fintech / e-commerce, not DIB.
- Trigger summary: 0 of 6 FLASH triggers fired. AM-collection-class only.
