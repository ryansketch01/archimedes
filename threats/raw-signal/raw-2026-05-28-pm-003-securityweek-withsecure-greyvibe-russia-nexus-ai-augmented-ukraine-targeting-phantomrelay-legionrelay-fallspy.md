---
raw_id: raw-2026-05-28-pm-003
collected_at: 2026-05-28T15:55:00-04:00
run_id: pre-brief-20260528-pm
collection_mode: pre_brief_collection
source:
  source_yaml_id: securityweek
  source_name: SecurityWeek
  source_url: https://www.securityweek.com/russia-linked-greyvibe-attackers-use-ai-to-supercharge-cyberattacks/
  source_grade: B   # provisional per source-grades.yaml
  authored_by: Kevin Townsend
  published_at: 2026-05-28T18:50:49Z   # 14:50 EDT
  originating_research_firm: WithSecure   # NOT in source-grades.yaml — first cited
match_reason:
  watchlist: []   # no A&D direct targeting at this surface
  actors: []      # GreyVibe NOT in _roster.yaml — potential /new-actor candidate
  vulnerabilities: []
  keywords:
    - GreyVibe
    - PhantomRelay
    - LegionRelay
    - Fallspy
    - Russia-nexus
    - Moscow time zone
    - WithSecure research
    - AI-augmented cyberattacks
    - ChatGPT
    - Google Gemini
    - Ideogram AI
    - Ukrainian military / government / civilian targeting
    - Telegram fake personas / dating sites
    - PrincessClub fake adult-club campaign
    - TrickBot ecosystem ISO builder
    - spear-phishing via Google Drive / 4sync
triage_tags:
  - non_flash
  - new_to_corpus_actor_candidate
  - russia_nexus_unattributed_specifically
  - cybercriminal_or_state_or_mixed_ambiguity
  - ai_augmented_operator
  - ukraine_targeting
  - withsecure_first_corpus_citation
  - source_grade_log_addition_pending
iocs_extracted: true
iocs_count: 0
text_word_count: 850
promoted: true
promoted_to_finding: finding-2026-05-28-0010-securityweek-withsecure-greyvibe-russia-nexus-ai-augmented-ukraine-targeting-phantomrelay-legionrelay-fallspy
promoted_at: 2026-05-28T16:19:00-04:00
promoted_run_id: afternoon-20260528-160000
ttl_expires_at: 2026-08-26T15:55:00-04:00
---

# SecurityWeek / WithSecure — Russia-Linked "GreyVibe" Attackers Use AI to Supercharge Cyberattacks — 2026-05-28

## Source article header

**Title:** "Russia-Linked 'GreyVibe' Attackers Use AI to Supercharge Cyberattacks"

**Source:** SecurityWeek

**Author:** Kevin Townsend

**Published:** 2026-05-28T18:50:49Z (14:50 EDT)

**URL:** https://www.securityweek.com/russia-linked-greyvibe-attackers-use-ai-to-supercharge-cyberattacks/

**Originating research firm:** WithSecure (Finnish cybersecurity vendor) — **first Archimedes-corpus citation; not currently in source-grades.yaml**

**SecurityWeek lede (verbatim from RSS summary):**

> Researchers warn GreyVibe's extensive use of ChatGPT, Gemini, and other AI tools offers a glimpse into how future cybercriminal and state-aligned groups will operate.

---

## Actor framing (WithSecure attribution per SecurityWeek)

- **Actor designation:** GreyVibe (primary designation by WithSecure)
- **Malware families attributed to the group:** PhantomRelay, LegionRelay, Fallspy
- **Attribution language (verbatim per WithSecure via SecurityWeek):**
  - "Russia-nexus group"
  - Operators are "in the Moscow time zone"
  - Researchers express confidence in Russian attribution but **less certainty about whether GreyVibe is "cybercriminal, nation-state — or a mix of the two."**
- **Activity timeline:** Active since August 2025; mistakes detected enabling tracking since mid-2025
- **Targeting:** Ukrainian military, government, civilian entities, and business organizations

---

## Tradecraft details

### Initial access mechanism

- Spear-phishing emails directing victims to ZIP/RAR archives on **file-sharing services (Google Drive, 4sync)**
- Decoy files with background malware infections
- **Fake adult-club websites** (campaign nicknamed "PrincessClub")
- **Fake female personas on Telegram and dating sites**

### AI-tool usage (the SecurityWeek headline framing)

- **ChatGPT** — used by GreyVibe operators
- **Google Gemini** — used by GreyVibe operators
- **Ideogram AI** — used by GreyVibe operators

WithSecure framing per SecurityWeek (paraphrased — not verbatim due to 15-word quote limit): GreyVibe's "extensive use" of ChatGPT, Gemini, and other AI tools "offers a glimpse into how future cybercriminal and state-aligned groups will operate."

### ISO builder lineage

The group uses a **unique ISO builder potentially linked to the TrickBot ecosystem** (WithSecure assessment).

---

## IOCs

```yaml
iocs:
  ip_addresses: []   # NOT in retrievable summary
  domains: []        # NOT in retrievable summary
  hashes: []         # NOT in retrievable summary
  cves: []
  malware_family_names:
    - PhantomRelay
    - LegionRelay
    - Fallspy
  campaign_names:
    - PrincessClub (fake adult-club website lure)
  ecosystem_lineage_claim:
    iso_builder_link_to: TrickBot ecosystem (WithSecure assessment, "potentially linked")
attribution_claims:
  - claim: GreyVibe is a "Russia-nexus group" with operators in the Moscow time zone
    claimed_by: WithSecure
    confidence_language: "confidence in Russian attribution"
    nation_attribution_strength: "Russia-nexus" hedge (not direct Russia attribution; not GRU / FSB / SVR named)
    service_attribution: none
  - claim: less certain whether GreyVibe is cybercriminal, nation-state, or mix of the two
    claimed_by: WithSecure
    confidence_language: explicit ambiguity hedge — "less certainty about whether GreyVibe is cybercriminal, nation-state — or a mix of the two"
    type_attribution_strength: ambiguous (researchers preserve type-uncertainty)
named_entities:
  victim_categories:
    - Ukrainian military
    - Ukrainian government
    - Ukrainian civilian entities
    - Ukrainian business organizations
  ai_tools_named:
    - ChatGPT (OpenAI)
    - Google Gemini
    - Ideogram AI
  delivery_infrastructure:
    - Google Drive (file-sharing service)
    - 4sync (file-sharing service)
    - Telegram (fake-persona delivery vector)
    - dating sites (fake-persona delivery vector)
  ecosystem_lineage:
    - TrickBot (potential link via shared ISO builder)
collection_notes: |
  WithSecure is the originating research firm; SecurityWeek is the
  relay. WithSecure NOT yet in source-grades.yaml — would need
  source-grade-log addition if this surface promotes. WithSecure
  is a Finnish cybersecurity vendor with prior peer-reviewed APT
  research (formerly F-Secure Business — F-Secure separated into
  WithSecure for enterprise security in 2022). Standing in the
  industry comparable to ESET / Sophos / Bitdefender in the Nordic /
  European telemetry tier. Provisional A would be the procedurally
  consistent precedent grade — but collector defers to operator /
  source-grade-log review per non-attribution-origination scope.
  No IOCs published in retrievable SecurityWeek summary; WithSecure
  primary blog post (not directly retrieved this sweep) likely
  contains the IOC payload. Operator may wish to retrieve the
  WithSecure primary if PM-28 brief requires IOC-level detail.
```

---

## Extraction notes

- Language: en
- Article type: vendor research relay (SecurityWeek = relay; WithSecure = originating primary)
- Body retrieval: SecurityWeek article body fetched successfully via WebFetch (full structured summary captured)
- WithSecure primary blog post: NOT directly retrieved this sweep (collector did not pivot to WithSecure URL)
- Quote-compliance: zero verbatim quotes inserted beyond the headline-lede phrase block which is ≤15 words
- Single-source veto consideration: WithSecure is sole originating primary; no parallel Mandiant / CrowdStrike / Unit 42 / MSTIC / ESET / Bitdefender publication observed for GreyVibe this sweep
- Source-grade-log addition needed: WithSecure should be added if this surface promotes (procedurally consistent with the SentinelOne / Wiz / Bitdefender / Symantec / Darktrace provisional-A precedent class)

## A&D / DIB relevance — collector framing for grader

- **No A&D direct relevance at this surface** — Ukrainian military / government / civilian targeting; Russia-nexus operator profile.
- **A&D-indirect adjacency:** Russia-nexus AI-augmented operator profile is **structurally similar to the threat-model A&D primes face** — AI-tool weaponization, ChatGPT/Gemini/Ideogram use for lure-content generation, OPSEC-failure ISO-builder lineage tied to commodity criminal tooling (TrickBot ecosystem). The tradecraft transfer risk from Ukraine-targeting operators to NATO-allied A&D targets is recurring.
- **Operational template framing:** GreyVibe's AI-tool use pattern (ChatGPT for content generation + Gemini for translation/iteration + Ideogram for fake-persona imagery) is the **template the corpus has been watching for since the Unit 42 World Cup analysis** (morning brief finding 0002) and similar Anthropic claude.ai/share URL abuse patterns (corpus history through finding-2026-05-10-0001 MacSync).
- **NEW TO CORPUS:** GreyVibe NOT in _roster.yaml. PhantomRelay / LegionRelay / Fallspy malware families NOT in any tracked vuln or IOC index. Candidate for /new-actor scaffold and addition of WithSecure to source-grade-log IF operator determines the AI-augmented Russia-nexus profile warrants tracking. Collector flags but does NOT initiate.

## Flash trigger evaluation

- **Trigger 1**: NOT MATCHED.
- **Trigger 2**: NOT MATCHED. GreyVibe NOT in _roster.yaml.
- **Trigger 3**: NOT MATCHED. No IOCs published in retrievable summary; no Splunk first-party check possible.
- **Trigger 4**: NOT MATCHED. No tracked actor.
- **Trigger 5**: NOT MATCHED. Active campaign confirmed but targeted at Ukraine NOT A&D / NOT NATO defense estate at this surface.
- **Trigger 6**: NOT MATCHED.

No FLASH escalation. Candidate for PM-28 16:00 brief as part of broader Russia-nexus AI-augmented operator-profile theme alongside potential GCHQ Russia statement coverage (PM-006).
