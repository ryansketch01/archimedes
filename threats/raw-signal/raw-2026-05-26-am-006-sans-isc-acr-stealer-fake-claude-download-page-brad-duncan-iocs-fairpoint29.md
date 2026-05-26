---
raw_id: raw-2026-05-26-am-006
collected_at: 2026-05-26T07:34:30-04:00
run_id: pre-brief-20260526-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: sans-isc
  source_name: SANS Internet Storm Center
  source_url: https://isc.sans.edu/diary/rss/33018
  published_at: 2026-05-26T00:01:48-04:00
  author: Brad Duncan
match_reason:
  watchlist: []
  actors: []                     # No attribution per Brad Duncan
  vulnerabilities: []
  keywords:
    - ACR Stealer
    - Windows infostealer
    - fake Claude download page
    - Anthropic brand impersonation
    - malvertising
    - Google Ads
    - sites.google[.]com URL concealment
    - fairpoint29.com
    - primemetricsa.com
    - creativecommunityinfo.art
    - i.ibb.co staging
    - enhanceblabber.cc C2
    - SHA-256 hashes published
triage_tags:
  - defender_tier_ioc_publication
  - ai_brand_impersonation_pattern
  - corpus_relevant_to_ckr_ai_threat_landscape_digest
  - corpus_relevant_to_macsync_claude_share_url_abuse_lineage
  - non_flash_morning_brief_other_signal
  - no_actor_attribution
  - 6_iocs_master_index_candidate
iocs_extracted: true
iocs_count: 6                    # 1 fake-page domain + 3 download/staging domains + 1 C2 domain + 3 SHA-256 hashes (some across overlapping categories, dedup = 6 unique)
text_word_count: 285
promoted: true
promoted_to_finding: finding-2026-05-26-0006-sans-isc-acr-stealer-fake-claude-download-page-fairpoint29-brad-duncan-iocs
promoted_at: 2026-05-26T08:00:00-04:00
ttl_expires_at: 2026-08-24T07:34:30-04:00
---

# Possible ACR Stealer From Page Impersonating Claude

**Source:** SANS Internet Storm Center diary, 2026-05-26 00:02 EDT
**URL:** https://isc.sans.edu/diary/rss/33018
**Handler:** Brad Duncan

## Article summary

SANS Internet Storm Center diary (Brad Duncan, named-handler byline)
documenting an **ACR Stealer** infostealer delivery chain via fake
**Claude (Anthropic)** download landing pages.

## ACR Stealer

- **Family:** Windows malware classified on Malpedia.
- **Capability class:** Information-stealing (infostealer).
- **Specific technical details:** Not elaborated in this Brad Duncan
  diary (cross-reference to Malpedia ACR Stealer canonical record
  for capability detail).

## Delivery chain

1. **Malvertising / Google Ads** — fake Claude download pages
   surfaced via Google Ads malicious advertising delivery.
2. **URL concealment** — "concealed in URLs for `sites.google[.]com`"
   per Brad Duncan diary.
3. **Fake landing page** — hosted on `fairpoint29[.]com`.
4. **OS-aware lure** — fake pages display platform-specific malware
   instructions based on the victim's operating system.

## Infrastructure indicators (IOCs)

**Fake landing page domain:**
- `fairpoint29[.]com`

**Download / staging domains:**
- `primemetricsa[.]com`
- `6ryuefl.creativecommunityinfo[.]art`
- `i.ibb[.]co` (legitimate image-hosting service abused for payload
  staging — defender risk: alert noise vs blocklist false-positive)

**C2 domain:**
- `yw.enhanceblabber[.]cc`

**File hashes (SHA-256):**
- ZIP archive: `70b5ecc110e074dbca92932c0e840ea3492ea0a43c3f215b71392c12b02213b2`
- PowerShell: `a14c3ecf5eb3d2543358482e43dc765dbf9ee7a4bec7571f5ecb8829ca719692`
- Image file: `47fa746422f1bf6b7712dc6803378e6a995488007193a7441d790f70d204728f`

## Threat actor attribution

**No attribution** per Brad Duncan diary. ACR Stealer is a
commodity infostealer family deployed by multiple criminal
operators; no specific cluster attribution attempted.

## Corpus cross-references

1. **CheckPoint Research AI Threat Landscape Digest** (raw-2026-05-26-am-002):
   AI provider credential targeting taxonomy explicitly includes
   Anthropic API keys harvested from `.env` files. ACR Stealer +
   fake Claude landing page is operationally adjacent (Anthropic
   brand impersonation as lure vector, although ACR Stealer is a
   commodity-stealer family rather than AI-provider-key-targeted
   tooling per CKR taxonomy).

2. **MacSync Claude share URL abuse lineage** (finding-2026-05-10-0001):
   Documented TeamPCP-cluster abuse of Anthropic's `claude.ai/share/...`
   shared-chat URL surface for attacker hosting via Berk Albayrak /
   Trendyol Group originating research. ACR Stealer + fake Claude
   landing page is a different mechanism class (Claude brand
   impersonation as lure vector vs `claude.ai/share/` URL trust-
   boundary abuse) but the same Anthropic-brand-misuse pattern.

3. **Imminent corpus cluster:** Across 3 weeks 2026-05-08 → 2026-05-26,
   the Archimedes corpus has documented 4+ surfaces of Anthropic-
   product / Claude-brand abuse — ClaudeBleed Chrome-extension
   (finding-2026-05-08-0004 LayerX), MacSync Claude share URL
   (finding-2026-05-10-0001), GTG-1002 Claude Code persistent
   CLAUDE.md jailbreak (CKR AI Threat Landscape Digest restating
   Anthropic Nov 2025), and now this ACR Stealer fake-Claude-page
   surface. Grader may consider whether this constitutes a
   discrete corpus pattern worth meta-cluster tagging.

## A&D-prime impact analysis

NO A&D-prime named. Commodity infostealer with no targeting profile
visible in this defender-tier IOC publication.

## Defender utility

The 6 IOCs are immediately actionable for blocklist deployment:
- Block: `fairpoint29.com`, `primemetricsa.com`, `enhanceblabber.cc`
  domains
- Block: `6ryuefl.creativecommunityinfo.art` host-specific
- Alert (do NOT block): `i.ibb.co` (legitimate service abused; FP risk)
- Hash-block: 3 SHA-256 hashes for EDR / AV scanning

Recommend grader promote IOCs to `_master-index.yaml` regardless of
whether the surface is promoted to a finding (defender utility on
the IOCs is independent of attribution layer).

---

## Extraction notes

- Language: en
- Publisher byline: Brad Duncan (SANS ISC named-handler; long-standing
  malware-analysis byline)
- Article type: defender diary (B-grade per source-grades.yaml sans-isc)
- Raw IOC extraction invoked: yes (6 IOCs extracted, structured below)
- Grader disposition target: morning brief Other Signal section as
  defender-tier IOC alert. IOC promotion to _master-index.yaml
  RECOMMENDED. Cross-references to CKR AI Threat Landscape Digest
  (am-002) and existing MacSync corpus lineage (finding-2026-05-10-0001)
  appropriate to surface in brief composition.

## IOCs (from ioc-extraction skill)

```yaml
iocs:
  - type: domain
    value: fairpoint29[.]com
    context: |
      Fake Claude (Anthropic) download landing page. Hosts OS-aware
      lure displaying platform-specific malware download instructions.
    confidence: high
    source_attribution: "SANS ISC diary 33018 (Brad Duncan, 2026-05-26 00:02 EDT)"
    first_observed: 2026-05-26 (publication date; observation date pre-publication)
    related_malware: ACR Stealer
    actor_id: null
    defanged: true

  - type: domain
    value: primemetricsa[.]com
    context: |
      Download domain in ACR Stealer delivery chain via fake Claude
      landing page on fairpoint29.com.
    confidence: high
    source_attribution: "SANS ISC diary 33018 (Brad Duncan, 2026-05-26 00:02 EDT)"
    first_observed: 2026-05-26
    related_malware: ACR Stealer
    actor_id: null
    defanged: true

  - type: domain
    value: 6ryuefl.creativecommunityinfo[.]art
    context: |
      Host-specific download domain in ACR Stealer delivery chain.
      Subdomain pattern suggests randomized / per-campaign host
      generation; parent zone creativecommunityinfo.art may be
      operator-controlled.
    confidence: high
    source_attribution: "SANS ISC diary 33018 (Brad Duncan, 2026-05-26 00:02 EDT)"
    first_observed: 2026-05-26
    related_malware: ACR Stealer
    actor_id: null
    defanged: true

  - type: domain
    value: i.ibb[.]co
    context: |
      Legitimate image-hosting service (imgbb.com infrastructure)
      abused for payload staging in ACR Stealer delivery chain.
      DEFENDER ALERT NOTE: do NOT blocklist parent ibb.co — false-
      positive risk against legitimate usage. Alert on download +
      execute-from-i.ibb.co patterns specifically.
    confidence: medium  # legitimate service abuse, not operator-controlled domain
    source_attribution: "SANS ISC diary 33018 (Brad Duncan, 2026-05-26 00:02 EDT)"
    first_observed: 2026-05-26
    related_malware: ACR Stealer
    actor_id: null
    defanged: true

  - type: domain
    value: yw.enhanceblabber[.]cc
    context: |
      C2 domain for ACR Stealer in this campaign. Subdomain pattern
      suggests randomized / per-campaign host generation; parent
      zone enhanceblabber.cc likely operator-controlled.
    confidence: high
    source_attribution: "SANS ISC diary 33018 (Brad Duncan, 2026-05-26 00:02 EDT)"
    first_observed: 2026-05-26
    related_malware: ACR Stealer
    actor_id: null
    defanged: true

  - type: hash_sha256
    value: 70b5ecc110e074dbca92932c0e840ea3492ea0a43c3f215b71392c12b02213b2
    context: "ZIP archive — initial-stage delivery file in ACR Stealer chain"
    confidence: high
    source_attribution: "SANS ISC diary 33018 (Brad Duncan, 2026-05-26 00:02 EDT)"
    first_observed: 2026-05-26
    related_malware: ACR Stealer
    actor_id: null

  - type: hash_sha256
    value: a14c3ecf5eb3d2543358482e43dc765dbf9ee7a4bec7571f5ecb8829ca719692
    context: "PowerShell — execution-stage script in ACR Stealer chain"
    confidence: high
    source_attribution: "SANS ISC diary 33018 (Brad Duncan, 2026-05-26 00:02 EDT)"
    first_observed: 2026-05-26
    related_malware: ACR Stealer
    actor_id: null

  - type: hash_sha256
    value: 47fa746422f1bf6b7712dc6803378e6a995488007193a7441d790f70d204728f
    context: "Image file — masquerading-as-image payload-staging file in ACR Stealer chain"
    confidence: high
    source_attribution: "SANS ISC diary 33018 (Brad Duncan, 2026-05-26 00:02 EDT)"
    first_observed: 2026-05-26
    related_malware: ACR Stealer
    actor_id: null

ttp_keywords:
  - name: Malvertising via Google Ads
    framework_mapping: MITRE T1583.008 / Acquire Infrastructure — Malvertising
    context: "Fake Claude download pages surfaced via Google Ads malicious advertising delivery"
  - name: URL concealment via sites.google.com
    framework_mapping: MITRE T1566.002 / Phishing — Spearphishing Link (loose analog)
    context: "Initial redirect chain concealed in URLs for sites.google.com → fake Claude page on fairpoint29.com"
  - name: AI brand impersonation lure (Anthropic / Claude)
    framework_mapping: MITRE T1036 / Masquerading (loose analog at brand-impersonation layer)
    context: "Fake Claude (Anthropic) download landing page as initial-access lure mechanism"

attribution_claims: []
# Brad Duncan diary does NOT name a specific threat actor. ACR
# Stealer is commodity infostealer with broad operator deployment;
# no attribution to propagate.
```
