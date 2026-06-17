---
raw_id: raw-2026-06-17-am-009-mandiant-direct-page-net-new-titles-medical-research-shinyhunters-law-firms
collected_at: 2026-06-17T07:50:00-04:00
run_id: pre-brief-20260617-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: mandiant
  source_name: Mandiant / Google Threat Intel
  source_url: https://cloud.google.com/blog/topics/threat-intelligence
  published_at: null
match_reason:
  watchlist: []
  actors: [UNC6508, ShinyHunters, UNC6692]
  vulnerabilities: [CVE-2026-35273]
  keywords: [Mandiant, GTIG, AI Threat Tracker, China-nexus, medical research, AI, cyber, national defense, ShinyHunters, PeopleSoft, US Law Firms, Snow Flurries, UNC6692, KnowledgeDeliver]
triage_tags: [substrate_strengthening_unc6508_carry_forward, possible_new_finding_scaffold_law_firms, mandiant_rss_canonical_swap_pending, mandiant_direct_page_substrate, net_new_law_firms]
iocs_extracted: false
iocs_count: 0
text_word_count: 380
promoted: true
promoted_to_finding: finding-2026-06-17-0003
promoted_at: 2026-06-17T08:12:00-04:00
ttl_expires_at: 2026-09-15T07:50:00-04:00
---

# Mandiant / Google Threat Intel direct-page index — top 8 visible titles snapshot

**Source:** Mandiant / Google Cloud Blog Threat Intelligence (https://cloud.google.com/blog/topics/threat-intelligence)
**Sweep mode:** Direct HTML index page WebFetch (per source-health canonical-swap pending — feedburner RSS 28th consecutive 404 this sweep)
**Index snapshot at:** 2026-06-17T07:50:00-04:00

## Visible top-8 titles snapshot

Per cloud.google.com/blog/topics/threat-intelligence index page (publication dates NOT displayed on index page; cross-walk required against existing corpus for in-window detection):

1. **GTIG AI Threat Tracker: Adversaries Leverage AI for Vulnerability Exploitation, Augmented Operations, and Initial Access** — 33-min read
2. **Public and Private Medical Community Targeted by China-Nexus Threat Actor Pursuing Artificial Intelligence, Cyber, Medical, and National Defense Research** — 21-min read **[matches UNC6508/INFINITERED carry-forward]**
3. **ShinyHunters Targets Education Sector with Oracle PeopleSoft Exploit** — 12-min read **[CVE-2026-35273 cross-walk]**
4. **Seeking Counsel: Ongoing Targeted Campaign Against US Law Firms** — 19-min read **[possible NEW substrate]**
5. **Exploitation of KnowledgeDeliver via ViewState Deserialization Vulnerability** — 7-min read **[possible NEW CVE]**
6. **2 PhaaS 2 Furious: The Evolution of Chinese-Language Phishing Services** — 7-min read
7. **Welcome to BlackFile: Inside a Vishing Extortion Operation** — 16-min read
8. **Snow Flurries: How UNC6692 Employed Social Engineering to Deploy a Custom Malware Suite** — 26-min read **[UNC6692 not on roster]**

## Extraction notes

- **Language:** en
- **Article type:** vendor IR blog index page (Mandiant direct HTML success-pattern entrenched 8+ consecutive direct-HTML successes against persistent feedburner RSS 404 failure)
- **Source health observation:** Mandiant feedburner RSS canonical-swap **still operator-deferred** — last attempt this sweep 2026-06-17 07:32 feedburner 404 (28th consecutive observation, failure_count tracker advanced 27→28). Direct cloud.google.com/blog/topics/threat-intelligence HTML path SUCCEEDED again. Publication dates remain not visible on index page per Mandiant page design.
- **In-window matching:** No publication dates visible on index — in-window determination requires either (a) WebFetch on individual article URLs OR (b) cross-walk against existing Archimedes corpus + WebSearch triangulation.
- **Cross-walk to existing carry-forward:**
  - **#2 Public and Private Medical Community / China-Nexus** = UNC6508 / INFINITERED PRC-nexus carry-forward (72h FLASH dedup through 2026-06-18 12:00 EDT from FLASH-1200 c48f6fc, T-28h-remaining from 08:00 morning). Title visible on index represents the canonical Mandiant blog substrate for the carry-forward; non-substrate-shifting publisher relay.
  - **#3 ShinyHunters Targets Education Sector with Oracle PeopleSoft Exploit** = cross-walk candidate for CVE-2026-35273 PeopleSoft retrospective-compliance-metrics phase carry-forward. ShinyHunters NOT on 24-actor `_roster.yaml`. Education-sector NOT A&D/DIB/CMMC/ITAR.
  - **#4 Seeking Counsel: Ongoing Targeted Campaign Against US Law Firms** = **possible NEW substrate this sweep** — US-targeted ongoing campaign against legal-sector specifically referenced. Net-new title not in prior corpus carry-forward. Cross-walk pending grader assessment.
  - **#5 Exploitation of KnowledgeDeliver via ViewState Deserialization** = possible NEW CVE substrate. Cross-walk pending — KnowledgeDeliver product not previously in corpus.
  - **#8 Snow Flurries UNC6692** = same UNC6692 flagged as out-of-window in 2026-05-09 15:30 pre-brief sweep (per source-health notes mandiant). NOT on roster. /new-actor candidacy operator-deferred from prior sweep.
- **Hard Rule 6 preservation:** No quotes captured — titles only per direct-HTML index page; titles are not copyrighted quotable material under fair-use heuristic.
- **Hard Rule 2 preservation:** Mandiant cluster identifiers (UNC6508, ShinyHunters, UNC6692, "China-Nexus Threat Actor") preserved verbatim. Archimedes does NOT cross-walk to existing roster actors on title-only substrate. UNC6508 = INFINITERED carry-forward.
- **Raw IOC extraction invoked:** no (index page only; no article bodies retrieved)

## Substrate observation for grader

Operator-deferred direct-WebFetch retrieval recommended for #4 (US Law Firms) and #5 (KnowledgeDeliver ViewState) given net-new substrate potential. Mandiant feedburner RSS canonical-swap operator decision still pending after 8+ consecutive direct-HTML successes against RSS-path failure.

#2 UNC6508/INFINITERED title visibility on index page is non-substrate-shifting (already in 72h FLASH dedup carry-forward). #3 ShinyHunters PeopleSoft Education-sector is operational-template substrate for CVE-2026-35273 carry-forward — A&D-relevance LOW (Education sector NOT A&D). #4 Law Firms is potentially A&D-relevant via supply-chain-adjacent legal counsel for A&D-prime litigation / IP / export-control matters — possible NEW finding scaffold candidate per grader assessment.
