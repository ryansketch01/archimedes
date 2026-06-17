---
raw_id: raw-2026-06-17-pm-016
collected_at: 2026-06-17T15:55:00-04:00
run_id: pre-brief-20260617-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: mandiant
  source_name: Mandiant / Google Threat Intelligence Group (blog index)
  source_url: https://cloud.google.com/blog/topics/threat-intelligence
  published_at: 2026-06-17T15:38:00-04:00
match_reason:
  watchlist: [aerospace-defense]
  actors: []
  vulnerabilities: []
  keywords: [Mandiant, GTIG, AI Threat Tracker, vulnerability exploitation, augmented operations, initial access, China-Nexus, medical research, ShinyHunters, PeopleSoft, education]
triage_tags: [mandiant_index_snapshot, title_substrate_only, watch_item_observation, body_retrieval_candidate, ad_supply_chain_adjacent]
iocs_extracted: false
iocs_count: 0
text_word_count: 250
promoted: true
promoted_to_finding: finding-2026-06-17-0003
promoted_at: 2026-06-17T16:00:00-04:00
ttl_expires_at: 2026-09-15T15:55:00-04:00
---

# Mandiant blog index snapshot — recently visible publication titles

Direct retrieval of cloud.google.com/blog/topics/threat-intelligence index page, 2026-06-17 15:38 EDT.

The five most recent visible publication titles on the Mandiant / GTIG threat intelligence blog index:

1. **GTIG AI Threat Tracker: Adversaries Leverage AI for Vulnerability Exploitation, Augmented Operations, and Initial Access**
   - Author: Google Threat Intelligence Group
   - Length: 33-minute read
   - URL: `/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access`
   - Status: NET-NEW since 2026-06-17 AM brief 56cf187 collection — body retrieval candidate for next cycle

2. **Public and Private Medical Community Targeted by China-Nexus Threat Actor**
   - Author: Google Threat Intelligence Group
   - Length: 21-minute read
   - URL: `/blog/topics/threat-intelligence/prc-targets-us-medical-research`
   - Status: Possible UNC6508/INFINITERED carry-forward substrate — UNC6508 PRC-nexus medical/military-health research espionage is under 72h FLASH dedup through 2026-06-18 12:00 EDT. Title surface is consistent with carry-forward but body retrieval deferred under under-24h skip rule.

3. **ShinyHunters Targets Education Sector with Oracle PeopleSoft Exploit**
   - Author: Mandiant
   - Length: 12-minute read
   - URL: `/blog/topics/threat-intelligence/shinyhunters-targets-education-sector-oracle-exploit`
   - Status: ShinyHunters NOT on _roster.yaml (24-actor roster checked); CVE-2026-35273 PeopleSoft is in retrospective-compliance-metrics phase (KEV deadline closed EOD 2026-06-15). Education sector NOT A&D-prime. Possible PM brief Other Signal one-liner.

4. **Seeking Counsel: Ongoing Targeted Campaign Against US Law Firms** (UNC3753)
   - Full body retrieved in raw-2026-06-17-pm-003

5. **Exploitation of KnowledgeDeliver via ViewState Deserialization Vulnerability** (CVE-2026-5426)
   - Full body retrieved in raw-2026-06-17-pm-004

---

## Extraction notes

- Language: en
- Article type: blog-index snapshot for retrieval-prioritization tracking
- Substrate context: Three additional Mandiant publication titles visible on the blog index that may warrant body retrieval next cycle. AI Threat Tracker (#1) and PRC medical research (#2) are highest-priority candidates for A&D-relevance:
  - **AI Threat Tracker** title surface ("AI for Vulnerability Exploitation, Augmented Operations, and Initial Access") connects to the AI-agent-offensive-tradecraft watch-pattern (raw-2026-06-17-pm-012 OALABS Claude/Codex) — possible substrate-strengthening on A&D-relevant defensive posture review
  - **PRC medical research targeting** title surface aligns with carry-forward UNC6508/INFINITERED Iran-Cyber-Watch-adjacent substrate under 72h FLASH dedup; body retrieval deferred under under-24h skip rule on substrate freeze
  - **ShinyHunters PeopleSoft** title surface aligns with carry-forward CVE-2026-35273 PeopleSoft retrospective compliance metrics
- Operator-deferred body-retrieval candidates for next-cycle pre-brief collection
- Raw IOC extraction NOT invoked (title-only substrate; no body retrieval this raw-signal)

## IOCs (from ioc-extraction skill)

```yaml
extracted_iocs:
  ipv4: []
  ipv6: []
  domains: []
  urls: []
  hashes: []
  email_addresses: []
  attribution_claims:
    - actor: ShinyHunters
      hard_rule_2_note: "NOT on _roster.yaml. Title-only substrate; body retrieval deferred."
    - actor: "China-Nexus Threat Actor"
      hard_rule_2_note: "Mandiant title-only — Mandiant has NOT specified named actor in title. Title surface consistent with carry-forward UNC6508/INFINITERED but body retrieval deferred under 72h FLASH dedup substrate freeze through 2026-06-18 12:00 EDT."
  title_only_observations:
    - "Mandiant AI Threat Tracker on adversary-AI-for-offensive — possible substrate connection to OALABS Claude/Codex offensive watch-pattern"
    - "Mandiant PRC medical research targeting title — possible carry-forward substrate"
    - "Mandiant ShinyHunters PeopleSoft education sector — possible carry-forward substrate"
```
