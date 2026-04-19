# INTEL-GRADING.md — Intelligence Source Grading System

> **Archimedes doctrine — grading.**
> This file is authoritative. Every finding's digraph must be justifiable against this document.

---

## Overview

We use a customized version of the **Admiralty Scale (NATO AJP-2.1)** — the gold standard for intelligence source evaluation, used by NATO, Five Eyes, CERT-EU, and major CTI firms worldwide.

Every piece of intel promoted to a finding gets a **two-character digraph** rating:
- **Letter** = Source Reliability (how much do we trust where this came from?)
- **Number** = Information Credibility (how much do we trust this specific piece of info?)

These are assessed **independently** — a reliable source can still report bad info, and an unreliable source can occasionally be right.

---

## Source Reliability (A–F)

| Grade | Label | Description |
|-------|-------|-------------|
| **A** | Completely Reliable | Consistent, verified track record. No meaningful doubt. |
| **B** | Usually Reliable | Strong track record with minor occasional inaccuracies. |
| **C** | Fairly Reliable | Has been right before but enough errors to warrant caution. |
| **D** | Not Usually Reliable | More misses than hits. Treat as a lead, not a finding. |
| **E** | Unreliable | History of false or misleading information. |
| **F** | Cannot Be Judged | New, unknown, or unverified source — no track record yet. |

---

## Information Credibility (1–6)

| Grade | Label | Description |
|-------|-------|-------------|
| **1** | Confirmed | Independently corroborated by at least one separate, unrelated source. |
| **2** | Probably True | Not yet confirmed, but logically consistent with known intel/TTPs. |
| **3** | Possibly True | Somewhat consistent but needs more digging. |
| **4** | Doubtful | Possible but not logical; no corroboration available yet. |
| **5** | Improbable | Contradicts known facts, TTPs, or established patterns. |
| **6** | Cannot Be Judged | Insufficient context to evaluate truth at all. |

---

## Credibility Assessment Checklist

**This is the authoritative rule for assigning a credibility grade.** The grader subagent MUST document which conditions are met for each finding and record them in the finding's `credibility.checklist_passed` frontmatter field.

### 1 — Confirmed — ALL of:
- [ ] At least one independent source (different publisher, different telemetry)
- [ ] Neither source cites the other as its origin
- [ ] Technical artifacts (hashes, IPs, CVEs) match across sources
- [ ] No contradicting higher-grade source exists

### 2 — Probably True — ALL of:
- [ ] Consistent with established TTPs for the named actor, OR consistent with known campaign timing/targeting
- [ ] No contradicting evidence from A/B-grade sources
- [ ] Technical claims are internally coherent (claimed CVE exists, claimed infrastructure is plausible)

### 3 — Possibly True — ANY of:
- [ ] Single-source, uncorroborated, but source is B-grade or better
- [ ] Partially consistent with known TTPs but some elements novel
- [ ] Technical claims plausible but not independently verifiable

### 4 — Doubtful — ANY of:
- [ ] Claim is possible but requires multiple unverified assumptions
- [ ] Source is C/D-grade and claim is extraordinary
- [ ] Timing or targeting inconsistent with known actor behavior

### 5 — Improbable — ANY of:
- [ ] Directly contradicts A-grade reporting
- [ ] Claimed TTPs inconsistent with actor's tradecraft maturity
- [ ] Technical claims violate known constraints (e.g., "exploits Windows 11 via SMBv1 in default config")

### 6 — Cannot Be Judged
Default when none of 1–5 can be established.

---

## What Counts as "Independent Corroboration"

This is the single most-abused term in CTI grading. Apply these rules strictly.

### Two sources are INDEPENDENT if ALL of the following:
- [ ] Different publishing organization
- [ ] Neither source cites the other, or a common upstream source, as its primary origin
- [ ] Different evidence basis (e.g., one has telemetry, one has incident response findings — not both quoting the same leaked doc)

### Two sources are NOT independent if:
- One is a rewrite/aggregation of the other (BleepingComputer summarizing a Mandiant report is NOT corroboration of Mandiant)
- Both trace to the same original leak/dump
- Both quote the same anonymous source
- Both rely on the same vendor's telemetry

**Rule of thumb:** If you remove one source's reporting, does the other still stand independently? If no → they are not independent.

---

## Single-Source Veto

A finding CANNOT be assessed at WEP "very likely" or higher based on a single source, regardless of that source's grade. Even an A1-graded CISA advisory warrants only "likely" until a second independent source confirms.

**Exception:** First-party telemetry from Archimedes's own infrastructure (Splunk `defenseclaw_local` or `archimedes` index) combined with any A/B-grade external source is sufficient for "very likely" on *attribution-to-your-environment* claims.

---

## Our Source Ratings

Pre-assigned source reliability grades based on track record, methodology, and institutional credibility. Information credibility is still assessed per-item.

### 🏛️ Government & Official Bodies

| Source | Grade | Rationale |
|--------|-------|-----------|
| CISA Advisories | **A** | Official U.S. gov, technically verified before publication |
| NSA/CNSA Advisories | **A** | Authoritative, technically vetted |
| FBI Flash Alerts | **A** | Law enforcement intelligence, operationally verified |
| MITRE ATT&CK | **A** | Curated, community-verified TTP knowledge base |
| DoD/CMMC Bulletins | **B** | Official but sometimes delayed or sanitized |
| NVD / CVE Database | **A** | Authoritative for the CVE record itself |

### 🔬 Tier-1 Threat Intel Firms

| Source | Grade | Rationale |
|--------|-------|-----------|
| Mandiant / Google Threat Intel | **A** | Industry gold standard, APT tracking, rigorous attribution |
| CrowdStrike (reports/blog) | **A** | Excellent APT naming/tracking |
| Recorded Future | **A** | Deep OSINT + dark web coverage |
| Microsoft MSTIC | **A** | Nation-state tracking, Defender telemetry-backed |
| Palo Alto Unit 42 | **A** | Strong technical research, consistent track record |
| SANS ISC | **B** | Quality research but community-contributed |

### 📰 Security Media & Researchers

| Source | Grade | Rationale |
|--------|-------|-----------|
| Krebs on Security | **B** | Strong track record, well-sourced |
| The Record (Recorded Future) | **B** | Quality journalism, usually well-sourced |
| BleepingComputer | **B** | Fast and accurate on CVEs/ransomware |
| Wired / Ars Technica (security) | **B** | Good journalism, secondary source |
| GitHub Security Advisories | **B** | Technically vetted, varies by maintainer |

### 🔧 Technical Enrichment Sources

These sources are A-grade for *facts* but F-grade for *interpretation*. Shodan telling you port 445 is open on an IP is A1. Shodan telling you that IP "belongs to APT29" is F6 unless a separate A/B source confirms attribution.

| Source | Facts Grade | Attribution Grade | Rationale |
|--------|-------------|-------------------|-----------|
| Shodan | **A** | **F** | Authoritative on infrastructure state, no attribution ability |
| Censys | **A** | **F** | Same as Shodan |
| VirusTotal detections | **B** | **F** | Vendor consensus, false positives happen |
| urlscan.io | **B** | **F** | Accurate for what it captures, limited context |
| WHOIS/RDAP | **A** | **F** | Authoritative registration data |
| HIBP | **A** (breach membership) | **F** (breach attribution) | Pwned Passwords + breach list is authoritative |
| ThreatFox | **B** | **B** | Community-contributed, generally solid IOCs |
| MalwareBazaar | **B** | **B** | Sample confirmed real, context varies |
| GitHub code search | **B** | **F** | Code presence yes, intent no |
| Intelligence X | **C** | **C** | Aggregator, depends on original source |
| DeHashed | **B** | **F** | Breach data is real, recency/accuracy varies |
| **Archimedes Splunk telemetry** | **A** | **A** | **First-party observation on your network** |

### 🐦 X/Twitter — Security Researchers (via RSS bridges)

| Source | Grade | Rationale |
|--------|-------|-----------|
| Kevin Beaumont (@GossiTheDog) | **B** | Well-known, usually right |
| vx-underground | **C** | Valuable malware content, sensationalized at times |
| SwiftOnSecurity | **B** | Strong signal, sometimes satirical |
| CISA official account | **A** | Same as CISA advisories |
| Unknown/new researcher accounts | **F** | No track record |
| Anonymous threat claims on X | **E** | Assume unreliable until corroborated |

### 📺 YouTube Channels

| Source | Grade | Rationale |
|--------|-------|-----------|
| Mandiant / Google Cloud Security | **A** | Same credibility as written reports |
| CISA (@CISAgov) | **A** | Official government channel |
| CrowdStrike | **A** | Same as written reports |
| John Hammond | **B** | Technically strong, educational focus |
| Simply Cyber | **B** | CTI methodology content |
| Black Hat / DEF CON talks | **B** | Peer-reviewed conference content |

### 🌐 OSINT / Open Web

| Source | Grade | Rationale |
|--------|-------|-----------|
| Iran Monitor (iranmonitor.org) | **C** | Useful Iran-focused tracking but bias possible — cross-reference |
| CyberWarrior76 (Substack) | **C** | Structured reports, not primary source |
| Dark web forums / leak sites | **D** | Occasionally accurate, often exaggerated |
| Pastebin / anonymous dumps | **E** | Assume unreliable |
| New/unverified Telegram channels | **F** | Unknown track record |

---

## Layered Additions

### TLP (Traffic Light Protocol) — Sharing Restrictions

- 🔴 **TLP:RED** — Not for disclosure beyond direct recipients
- 🟠 **TLP:AMBER** — Limited to recipients and their organizations
- 🟢 **TLP:GREEN** — Community-wide sharing OK
- ⚪ **TLP:CLEAR** (formerly WHITE) — Public, no restrictions

Default: TLP:CLEAR. Higher restrictions require source's explicit marking.

### Words of Estimative Probability (WEP) — Forward Assessments

Use when making predictive statements:

- *Almost certainly* (>95%)
- *Very likely* (85–95%)
- *Likely* (55–85%)
- *Roughly even chance* (~50%)
- *Unlikely* (15–45%)
- *Very unlikely* (5–15%)
- *Remote* (<5%)

**Example:** *"UNC1549 will very likely (B2) continue targeting U.S. defense contractors in Q2 2026, consistent with their established TTPs against CMMC-adjacent suppliers."*

---

## Inclusion Thresholds by Output

| Output | Minimum Grade | Rationale |
|--------|--------------|-----------|
| FLASH brief (async, high priority) | B2 | Low tolerance for false alarms |
| Scheduled daily brief (action items) | B2 | Keep brief quality high |
| Scheduled daily brief (monitoring) | C3 | Can carry "watching" items |
| Weekly synthesis | C3 | Patterns can emerge from lower-confidence signal |
| Actor profile updates | B2 | Dossiers are long-lived |
| Raw signal archive | F6 | Capture everything, grade later |

---

## Grade Revisions

Source grades are dynamic. Every grade change gets logged to `infrastructure/source-grade-log.md`.

**Format:**

```
## YYYY-MM-DD: Source-Name — OLD → NEW

**Reason:** <specific miss or pattern of misses, with links>
**Reviewer:** <human or agent>
**Next review:** <date>
```

**Rules:**
- Downgrades of B→D or worse require human review before commit
- Upgrades of C→B or better require three corroborated hits in a rolling 90-day window
- Any automated downgrade proposal posts to Discord `#actor-review` for sign-off
- Grades are reviewed quarterly even when no change is proposed

---

## How to Apply in Briefs

1. **Collect** intel via the `collector` subagent (no grading at this stage)
2. **Promote** clusters to findings via the `grader` subagent — this is when full grading happens
3. **Grade the source** using the table above (or assign F if unknown)
4. **Grade the information** independently — checklist above
5. **Check corroboration** — is this genuinely independent, or re-reporting?
6. **Apply single-source veto** if WEP claim would exceed "likely"
7. **Tag the finding** with its digraph in frontmatter (e.g., `digraph: A2`)
8. **Apply inclusion threshold** to determine `inclusion.eligible_for` array

---

*Last reviewed: Session 1 scaffold*
*Next review: 2026-07-18*
