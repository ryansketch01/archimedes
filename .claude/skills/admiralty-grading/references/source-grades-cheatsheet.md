# Source Grades Cheatsheet

> **On-demand reference.** Loaded only when the grader encounters an unfamiliar source or needs to reason about a source's category.
> **Authoritative lookup is `infrastructure/source-grades.yaml`.** This document explains the reasoning.

---

## When to consult this file

1. A source isn't in `source-grades.yaml` and you need to assign a provisional grade
2. You need to justify why a source carries the grade it does
3. You're proposing a grade revision and need to reason about precedent

For routine grading of known sources, go straight to `source-grades.yaml` — don't load this file.

---

## Category reasoning

### Government & Official Bodies (generally A or B)

Official government advisories carry the highest letter grades because they are technically verified before publication and the publishing organization has operational intelligence access.

| Source | Grade | Rationale |
|---|---|---|
| CISA Advisories | A | Official U.S. gov, technically verified pre-publication |
| NSA/CNSA Advisories | A | Authoritative, technically vetted |
| FBI Flash Alerts | A | Law enforcement intel, operationally verified |
| MITRE ATT&CK | A | Curated, community-verified TTP knowledge base |
| DoD/CMMC Bulletins | B | Official but sometimes delayed or sanitized |
| NVD / CVE Database | A | Authoritative for the CVE record itself |

**Watch for:** CISA occasionally re-publishes vendor advisories — when this happens, the grade tracks the *underlying* vendor, not CISA. Also: government sources may be behind on novel threats that private firms catch first.

### Tier-1 Threat Intel Firms (A)

These firms have dedicated threat research teams, extensive telemetry, and consistent track records on APT tracking.

| Source | Grade | Rationale |
|---|---|---|
| Mandiant / Google Threat Intel | A | Industry gold standard, rigorous attribution |
| CrowdStrike | A | Excellent APT naming/tracking, Falcon telemetry |
| Recorded Future | A | Deep OSINT + dark web coverage |
| Microsoft MSTIC | A | Nation-state tracking, Defender telemetry |
| Palo Alto Unit 42 | A | Strong technical research, consistent track record |
| SANS ISC | B | Quality research but community-contributed |

**Watch for:** Tier-1 firms occasionally rush publication on competitive intel. Cross-check timing if a claim seems to precede expected disclosure.

### Security Media & Independent Researchers (B)

These sources have strong track records but are usually secondary — they report on what Tier-1 firms or government publishes.

| Source | Grade | Rationale |
|---|---|---|
| Krebs on Security | B | Strong track record, well-sourced |
| The Record (Recorded Future media) | B | Quality journalism, usually well-sourced |
| BleepingComputer | B | Fast and accurate on CVEs/ransomware |
| Wired / Ars Technica (security) | B | Good journalism, secondary source |
| GitHub Security Advisories | B | Technically vetted, varies by maintainer |

**Watch for:** When a Tier-1 firm and a security media outlet both report the same claim, that may not be independent corroboration — the media outlet may be reporting on the Tier-1 firm's report. Trace to original.

### Technical Enrichment — Dual-Grade (facts/attribution)

These sources are authoritative for observed facts but have no attribution ability. Always dual-grade.

| Source | Facts | Attribution | Rationale |
|---|---|---|---|
| Shodan | A | F | Authoritative on infrastructure state, no attribution |
| Censys | A | F | Same as Shodan |
| VirusTotal detections | B | F | Vendor consensus, false positives happen |
| urlscan.io | B | F | Accurate for what it captures, limited context |
| WHOIS/RDAP | A | F | Authoritative registration data |
| HIBP | A (breach membership) | F (breach attribution) | Pwned Passwords / breach list is authoritative |
| ThreatFox | B | B | Community-contributed, generally solid IOCs |
| MalwareBazaar | B | B | Sample confirmed real, context varies |
| GitHub code search | B | F | Code presence yes, intent no |
| Intelligence X | C | C | Aggregator, depends on original source |
| DeHashed | B | F | Breach data is real, recency/accuracy varies |
| **Archimedes Splunk telemetry** | A | A | First-party observation on your network |

**Key principle:** A Shodan result saying "port 445 open on 1.2.3.4" is **A1** fact. That same result reframed as "1.2.3.4 is APT29 infrastructure" is **F6** attribution unless a separate A/B-graded source confirms the attribution.

### Social Media — Researchers (X/Twitter via RSS bridges)

| Source | Grade | Rationale |
|---|---|---|
| Kevin Beaumont (@GossiTheDog) | B | Well-known, usually right |
| vx-underground | C | Valuable malware content, sensationalized at times |
| SwiftOnSecurity | B | Strong signal, sometimes satirical |
| CISA official account | A | Same as CISA advisories |
| Unknown/new researcher accounts | F | No track record |
| Anonymous threat claims on X | E | Assume unreliable until corroborated |

**Watch for:** Twitter claims can fabricate or misattribute. Even high-reputation researchers post off-the-cuff thoughts that shouldn't be treated as formal intel. Apply source grade only to substantive, sourced threads — not one-liner speculation.

### Video (YouTube channels)

| Source | Grade | Rationale |
|---|---|---|
| Mandiant / Google Cloud Security | A | Same credibility as written reports |
| CISA (@CISAgov) | A | Official government channel |
| CrowdStrike | A | Same as written reports |
| John Hammond | B | Technically strong, educational focus |
| Simply Cyber | B | CTI methodology content |
| Black Hat / DEF CON talks | B | Peer-reviewed conference content |

**Watch for:** YouTube content often re-presents written reports. Check whether the YouTube video is the primary source or summarizing something else. If summarizing, cite the primary.

### OSINT / Open Web (C and below)

| Source | Grade | Rationale |
|---|---|---|
| Iran Monitor (iranmonitor.org) | C | Useful Iran-focused tracking but bias possible |
| CyberWarrior76 (Substack) | C | Structured reports, not primary source |
| Dark web forums / leak sites | D | Occasionally accurate, often exaggerated |
| Pastebin / anonymous dumps | E | Assume unreliable |
| New/unverified Telegram channels | F | Unknown track record |

**Watch for:** OSINT aggregators frequently re-circulate claims from higher-grade sources without citation. Trace to primary before treating as independent.

---

## Provisional grading for unknown sources

When a source doesn't appear in `source-grades.yaml`, assign a provisional grade based on these defaults:

| Source type | Provisional grade | Notes |
|---|---|---|
| Unknown individual researcher (blog, Substack) | F | No track record |
| Unknown industry publication | C | Pending review |
| Newly-created Twitter/X account | F | Suspicious if claiming big scoop |
| Anonymous leak or dump | E | Treat with strong skepticism |
| Academic research paper (peer-reviewed) | B | Methodology usually sound |
| Vendor blog with technical writeup (unknown vendor) | C | Pending review of methodology |
| Government agency not in roster (non-US allied) | B | Official status provisional |
| Vendor self-disclosure (company reporting its own breach) | B | Authoritative on the fact of breach, may understate scope |

**After assigning provisional grade:**
- Flag in the skill output (`provisional: true`)
- Librarian will add to `source-grades.yaml` with a `provisional: true` marker
- Log to `source-grade-log.md` with the assignment reasoning
- Next quarterly review converts provisional → confirmed grade based on track record

---

## Signals that a source's grade should change

Watch for these patterns during grading and flag if they emerge:

### Downgrade signals
- Source reported something contradicted by higher-grade reporting (one miss → note, two misses in 90d → propose downgrade)
- Source is frequently cited by lower-grade aggregators as "confirmation" — suggests laundering, not journalism
- Source has undergone editorial or ownership change affecting methodology
- Source starts making predictive claims without methodology

### Upgrade signals
- Source consistently breaks stories ahead of Tier-1 firms (three hits in 90d → propose upgrade)
- Source develops independent telemetry or research methodology
- Source is cited as primary by A-grade sources

### No-change signals (do not propose)
- Source had a single miss after long good track record
- Source was contradicted by an E-grade rumor that turned out to be wrong
- Source tone is abrasive but claims hold up

All grade revision proposals go through the process in `INTEL-GRADING.md` "Grade Revisions" section — downgrades of B→D or worse require human review via `#actor-review`.

---

*Last updated: Session 2 scaffold*
*Source of truth: `doctrine/INTEL-GRADING.md` and `infrastructure/source-grades.yaml`*
