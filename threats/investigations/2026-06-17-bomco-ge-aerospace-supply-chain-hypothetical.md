---
investigation_id: inv-2026-06-17-001
target: "HYPOTHETICAL — supply-chain exposure of GE Aerospace program/technical data via the Bomco, Inc. breach (disclosed May 2026)"
command: /investigate
investigation_type: hypothetical / supply-chain exposure modeling
requested: 2026-06-17
analyst: Archimedes (orchestrator, on-demand)
classification: TLP:CLEAR
status: open / hypothetical — no evidence of partner-data exposure; assessed UNLIKELY at LOW confidence
related_findings: none-promoted
related_actors_in_roster: none (no actor named in any Bomco disclosure)
ad_prime_relevance: STRUCTURAL (Bomco is a qualified jet-engine component supplier holding GE source approval; the breach itself is PII-only as disclosed)
hypothetical_flag: true
hypothetical_note: >
  This note models a HYPOTHESIS — that GE Aerospace program/technical data
  could have been exposed via the Bomco breach. It is NOT a finding, NOT a
  claim by any source, and NOT confirmed reporting. No public or first-party
  evidence supports partner-data exposure. The exercise exists to scope the
  supply-chain risk surface, not to assert it occurred. Hard Rule 2 fully in
  force: Archimedes originates no attribution and no linkage claim.
---

# /investigate (HYPOTHETICAL) — Could GE Aerospace data have been exposed via the Bomco breach?

## ⚠️ Framing — this is a hypothetical

This note answers a *what-if*: **if** an A&D prime's data sat inside Bomco's
environment, **would** the disclosed breach have touched it, and **what does the
public record actually say?** The answer up front: **the public record shows a
PII-only incident and says nothing about partner data.** The supply-chain
exposure of GE Aerospace data is a **hypothesis with no supporting evidence** —
modeled here, not asserted.

## Bottom line up front

**No public or first-party evidence ties GE Aerospace to the Bomco breach.**
Every authoritative record (Vermont AG portal filing + breach aggregators)
describes an **individual-PII incident affecting ~892 people** — names, SSNs,
driver's-license/government IDs, financial-account and card numbers, and health
records. **No partner, customer, OEM, program, technical-data, IP, ITAR, or CUI
exposure is mentioned anywhere.**

A **real GE↔Bomco supplier relationship exists**: Bomco's own site lists
**General Electric** among its OEM source-approval holders for jet-engine
component manufacturing. That is the *enabling condition* that makes the
hypothesis worth modeling — it is **not evidence the data was exposed.**

**Assessment: it is UNLIKELY that GE Aerospace technical/program data was
compromised in the Bomco breach — at LOW confidence.** The low confidence is
driven entirely by a visibility gap (see H3 below), not by any positive
indicator of exposure.

---

## The disclosed incident (what is actually on record)

| Element | Detail | Source / grade |
|---|---|---|
| Subject | Bomco, Inc. — Gloucester, MA precision metal-formed component maker (est. 1958); aerospace, industrial gas turbines, power generation, marine propulsion | bomco.com (A, self-published) |
| Intrusion window | June 14–16, 2025; discovered June 17, 2025 | aggregators — **C3** |
| Review → notification | File review completed ~Apr 20, 2026; notices began ~May 18, 2026 (~11-mo lag) | **C3** |
| **Data exposed** | Names, **SSN, driver's license / gov ID, financial account, credit/debit, health records** | **Vermont AG portal filing — B2** |
| Scale | ~892 individuals (811 MA, 23 NH, 6 VT, 4 ME) | VT AG + aggregators — **C3** |
| Remediation | IDX, 24-mo credit monitoring; enroll by Aug 18, 2026; support line 1-833-788-9712 | **C3** |
| Threat actor | **None named** | — |
| Mechanism | **Not disclosed** (no ransomware claim, no leak-site post, no extortion found) | — |

The **Vermont Attorney General** filing independently corroborates the data
categories as **PII only**. Verbatim notification-letter PDFs sit behind
JS-driven / 403 state portals (Vermont returned HTTP 403; Maine/NH lists are
dynamic) — but the AG record already confirms scope, and consumer notification
letters do not enumerate OEM customers regardless.

---

## The only real GE link: source approval, not breach

Bomco's aerospace page states it holds **source approvals** (fusion welding,
laser beam machining) from a named OEM set:

> Pratt & Whitney, Pratt & Whitney Canada, Pratt & Whitney Rocketdyne, **General
> Electric**, Snecma, Rolls Royce, Parker Aerospace Group, Hamilton Sundstrand,
> Honeywell Aerospace

Bomco builds **jet-engine combustor / engine components** for these primes. So
GE program data *plausibly resides* inside Bomco's environment — the structural
precondition for the hypothesis. **This is a documented business relationship
only; it is not an indicator of compromise of GE data** (bomco.com, A-grade but
self-published/promotional).

---

## Competing hypotheses (ACH-lite)

- **H1 — GE technical/program data was compromised in the breach.**
  *Most inconsistent with the evidence:* disclosures are PII-only, scale is small
  (~892 individuals — an HR/personnel-records footprint), no leak site, no
  extortion claim, no actor. **UNLIKELY.**

- **H2 — Only individual PII was exposed; no partner/GE data involved.**
  *Most consistent:* matches a personnel/individual-records exposure across four
  New England states. **LEADING.**

- **H3 — Partner data was in scope but is not reportable under PII statutes, so
  it does not surface in the records we can see.**
  *Cannot be excluded:* state breach-notification laws are PII-triggered;
  partner/CUI/program-data loss would route through **DoD/DFARS (DIBNet)** and
  prime contractual channels, both invisible to OSINT and to our Splunk. **This
  is the residual uncertainty and the sole reason confidence is LOW, not
  moderate.**

Leading hypothesis is **H2**. H1 carries the most inconsistent evidence. H3 is
unfalsifiable from open sources — which is exactly why the assessment is hedged.

---

## First-party check (Hard Rule 8)

**Splunk: 0 events** across `index=archimedes OR index=defenseclaw_local` for
`bomco`, `bomco.com`, `GE Aerospace`, `geaerospace` (90-day lookback).

No indexed first-party telemetry. **Silence does NOT disconfirm** — Frank is
neither Bomco's nor GE's environment, so we would not observe this incident
regardless of what occurred. Visibility-bounded absence flagged.

---

## ⚠️ Do not conflate with GE Aerospace's own separate breaches

Searches on "GE Aerospace breach" surface **unrelated** prior incidents:

- **2023 — IntelBroker:** alleged sale of GE confidential data, including
  DARPA-related military/aviation documents.
- **2024 — Meow ransomware:** claimed GE Aerospace client data + internal SQL
  databases, offered for ~$100K.

These are **independent GE incidents** — different actors, different years, **no
reported relationship to the Bomco intrusion.** Drawing a line between them would
be originating an attribution chain no source has made. We do not.

---

## Hard Rules check

- **Rule 2 (no origination):** Archimedes makes **zero** new attribution or
  linkage claims. The GE↔Bomco connection is reported only as a documented
  supplier relationship (Bomco's own disclosure). The exposure of GE data is
  framed as an **unsupported hypothesis**, not a claim.
- **Rule 3 (no exploitation content):** none. Mechanism is undisclosed and not
  modeled.
- **Rule 4 (passive only):** OSINT + first-party Splunk only. No active recon
  against Bomco or GE; neither is on `authorized-targets.yaml`.
- **Rule 6 (15-word quote limit):** the source-approval list is a factual
  enumeration, not a quoted opinion; no external opinion-quote exceeds the limit.
- **Rule 7 (credentials radioactive):** the breach involves SSNs/financial data;
  Archimedes does not request, store, or query any of the affected dataset.
- **Rule 8 (Splunk first-party):** executed; 0 hits; visibility-bounded absence
  flagged above.

---

## Recommended disposition

1. **Do NOT promote to a graded finding.** This is a hypothetical with no
   supporting evidence; promoting it would risk implying a partner-data exposure
   the record does not support.

2. **The hypothesis resolves only via channels we cannot see.** If you (or a
   prime's supply-chain security team) have standing, the question of partner-data
   exposure would be answered through **DIB/DFARS incident reporting** or direct
   prime notification — not OSINT. That is where H3 lives.

3. **Carry as a sentinel watch** for any future Bomco leak-site post, extortion
   claim, or actor attribution. If Bomco resurfaces with a ransomware/data-theft
   angle (vs. the current quiet PII notice), re-open this note and re-grade —
   that would materially shift H1.

4. **No defensive-control change at the A&D-prime tier** is warranted by this
   incident alone. The supplier relationship is ordinary; the disclosed breach is
   PII-scoped.

5. **Optional follow-up:** retrieve the verbatim Maine/NH notification-letter PDFs
   to lock the exact disclosure language on record (low value — letters will not
   name OEM customers).

---

## Sources (ordered by weight)

- Vermont Attorney General — Security Breach Notices (Bomco filing; PII data
  categories) — https://ago.vermont.gov/categories/security-breach-notices
- Bomco — Aerospace markets / OEM source approvals (incl. General Electric) —
  http://www.bomco.com/aerospace-markets/
- ClaimDepot — Bomco data breach summary (dates, scale, data elements, IDX
  remediation) — https://www.claimdepot.com/data-breach/bomco-2026
- Maine Attorney General — Data Breach Notices (portal) —
  https://www.maine.gov/ag/news-and-library/data-breach-notices
- Breachsense — GE Aerospace data breach (2024, UNRELATED) —
  https://www.breachsense.com/breaches/ge-aerospace-data-breach/
- CSO Online — GE investigates alleged breach of confidential projects (2023,
  UNRELATED) — https://www.csoonline.com/article/1249233/

*— end of hypothetical investigation note*
