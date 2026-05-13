# Source Grade Change Log

Ledger of all source reliability grade changes. Every grade change gets an entry here before `infrastructure/source-grades.yaml` is modified.

**Rules per `doctrine/INTEL-GRADING.md`:**
- Downgrades of B→D or worse require human review
- Upgrades of C→B or better require three corroborated hits in a rolling 90-day window
- Automated proposals post to Discord `#actor-review` for sign-off
- Grades reviewed quarterly even when no change is proposed

---

## 2026-04-18 — Initial grades established

**Type:** Initial
**Source:** Session 1 scaffold
**Summary:** Initial grades assigned per `doctrine/INTEL-GRADING.md` v1.0.0. All 42 sources seeded from the C3PO grading doctrine with minor refinements for the enrichment source dual-grade model (facts vs. attribution).
**Reviewer:** Ryan
**Next review:** 2026-07-18

---

## 2026-05-06 — Rapid7 — (none) → A (provisional, awaiting ratification)

**Type:** New source — provisional
**Source ID:** `rapid7`
**Reason:** First Archimedes-corpus citation as the originating source on `finding-2026-05-06-FLASH-0002` (MuddyWater attribution at moderate confidence; Chaos ransomware false-flag tradecraft). Rapid7 Labs / IR practice is widely treated as Tier-1 in industry; peer-reviewed publications, named analyst bylines, IR-engagement-grounded reporting. Proposed grade A by the grader on the assumption it sits with Mandiant / CrowdStrike / Unit 42 / MSTIC peers.
**Supporting findings:** [finding-2026-05-06-FLASH-0002]
**Posted to:** Discord `#actor-review` (message id pending — see librarian Splunk telemetry)
**Reviewer:** Awaiting Ryan ratification via `/approve-source-grade rapid7 A` (or operator downgrade)
**Provisional flag set:** `provisional: true`, `awaiting_ratification: true` in `infrastructure/source-grades.yaml`
**Effect on referencing finding:** Provisional A is treated as A for grading the finding (finding is digraph A2 / WEP likely with single-source-veto already capping); a subsequent operator downgrade to B would not change the FLASH disposition (still single-source-veto load-bearing) but would propagate to the auto-downgrade clock evaluation at 2026-05-09 12:18 EDT.
**Next review:** ratification target 2026-05-13 (7 days; before MuddyWater profile first-pass deadline)

---

## 2026-05-06 — SecurityWeek — (none) → B (provisional, awaiting ratification)

**Type:** New source — provisional
**Source ID:** `securityweek`
**Reason:** First Archimedes-corpus citation as a relay on `finding-2026-05-06-FLASH-0002` (MuddyWater attribution; SecurityWeek added no original reporting, relayed Rapid7). Proposed grade B by the grader as a fast-and-accurate security trade outlet on a par with BleepingComputer. Operator may ratify at B or downgrade to C if context-thin relay-only profile is observed across more findings.
**Supporting findings:** [finding-2026-05-06-FLASH-0002]
**Posted to:** Discord `#actor-review` (combined with Rapid7 ratification request — single message id)
**Reviewer:** Awaiting Ryan ratification via `/approve-source-grade securityweek B` or `/approve-source-grade securityweek C`
**Provisional flag set:** `provisional: true`, `awaiting_ratification: true` in `infrastructure/source-grades.yaml`
**Effect on referencing finding:** SecurityWeek role on this finding is `relay` only; its grade does not load-bear on the WEP cap (single-source veto already pins to "likely" via Rapid7 originating role). Outcome: cosmetic, no FLASH disposition impact.
**Next review:** ratification target 2026-05-13 (7 days; bundled with Rapid7)

**Precedent note:** This is the first time the librarian has surfaced new-source ratification requests via this log. Future grader runs that introduce a not-yet-listed source should follow the same pattern: add provisional entry to `source-grades.yaml`, log here, post `#actor-review`. Doctrine `INTEL-GRADING.md` does not yet describe this flow explicitly — surface in the next doctrine review.

---

## 2026-05-06 — palo-alto-psirt — recommendation pending review (no grade change applied this run)

**Type:** New-source recommendation (not applied)
**Source ID (proposed):** `palo-alto-psirt`
**Proposed grade:** A (category: vendor)
**Reason:** Grader on `finding-2026-05-06-FLASH-0003` recommends adding `palo-alto-psirt` as a dedicated source-grades.yaml id. PSIRT advisories currently graded under `unit42` parent-org id by FLASH-0001 precedent. Dedicated id is cleaner: PSIRT and Unit 42 publish on different cadences and methodologies (PSIRT = product-fact authority; Unit 42 = threat research). Non-blocking — this run continues to grade PAN PSIRT under the unit42 parent-org id per FLASH-0001 precedent.
**Supporting findings:** [finding-2026-05-06-FLASH-0001, finding-2026-05-06-FLASH-0003]
**Action this run:** Logged for human review. NOT added to `source-grades.yaml` and NOT posted to `#actor-review` — non-blocking, deliberate-review item.
**Reviewer:** Awaiting Ryan decision (add as A, add as B, or decline)
**Next review:** Bundle with the 2026-05-13 Rapid7 / SecurityWeek ratification window.

---

## 2026-05-08 — SentinelOne / SentinelLabs — (none) → A (provisional, awaiting ratification)

**Type:** New source — provisional
**Source ID:** `sentinelone`
**Reason:** First Archimedes-corpus citation as the originating source on `finding-2026-05-08-0003` (PCPJack worm research — credential-stealing worm targeting cloud-native dev infrastructure; deterministic TeamPCP-displacement behavior; hedged "could be a former operator" language). Sole primary on the finding; BleepingComputer and SecurityWeek relay. SentinelLabs is widely treated as Tier-1 vendor research alongside Mandiant / CrowdStrike / Unit 42 / MSTIC — peer-reviewed publications, named analyst bylines, deep technical telemetry-grounded reporting. Proposed grade A by the grader on that peer-tier assumption.
**Supporting findings:** [finding-2026-05-08-0003]
**Posted to:** Discord `#actor-review` (message id pending — see librarian Splunk telemetry for this run)
**Reviewer:** Awaiting Ryan ratification via `/approve-source-grade sentinelone A` (or operator downgrade)
**Provisional flag set:** `provisional: true`, `awaiting_ratification: true` in `infrastructure/source-grades.yaml`
**Effect on referencing finding:** Finding 0003 is digraph A2 / WEP likely with single-source-veto active (SentinelOne sole primary on attribution). Provisional A grading is what holds the A2 digraph — operator downgrade to B would re-grade 0003 to B2 and the WEP cap would still apply (single-source-veto load-bearing). Operator decline (no grade) would force grader to re-evaluate 0003 on next sweep with no source-grade resolved.
**Collector follow-up flagged:** SentinelOne primary report URL not surfaced by WebFetch in the 2026-05-08 morning collection cycle — relays cite the SentinelLabs research but the primary URL was not reachable / surfaced. Flag for next collection sweep; PCPJack-specific IOCs (S3 payload URLs, sample hashes, C2 endpoints) deferred until primary fetched.
**Next review:** ratification target 2026-05-15 (7 days; bundled with the next ratification sweep)

---

## 2026-05-08 — LayerX Security — (none) → C (provisional, awaiting ratification)

**Type:** New source — provisional
**Source ID:** `layerx`
**Reason:** First Archimedes-corpus citation as the originating source on `finding-2026-05-08-0004` (ClaudeBleed — trust-boundary flaw in Anthropic's Claude Chrome extension; co-resident hostile-extension prompt injection / DOM-confirmation forgery / authenticated-session pivot). Sole primary; SecurityWeek relay. Unknown vendor — no prior Archimedes-corpus citation, no peer-reviewed-publication track record observed at first surface, browser-security commercial origin creates a structural conflict-of-interest concern with the vulnerability class they research (browser/extension trust-boundary issues are exactly the surface LayerX sells products for). Proposed grade C by the grader as a conservative starting grade pending track-record accumulation. Operator may upgrade to B on observation of consistent technical rigor across multiple findings, or hold at C if a context-thin commercial-research profile emerges.
**Supporting findings:** [finding-2026-05-08-0004]
**Posted to:** Discord `#actor-review` (message id pending — see librarian Splunk telemetry for this run)
**Reviewer:** Awaiting Ryan ratification via `/approve-source-grade layerx C` (or operator upgrade to B)
**Provisional flag set:** `provisional: true`, `awaiting_ratification: true` in `infrastructure/source-grades.yaml`
**Effect on referencing finding:** Finding 0004 is digraph C3 / WEP roughly_even_chance with single-source-veto active (LayerX sole primary, SecurityWeek relay). Provisional C grading is what holds the C3 digraph — this is the floor, no further downgrade path on grade alone. Operator upgrade to B would re-grade 0004 to B3 and lift the WEP slightly (still single-source-veto-capped).
**Next review:** ratification target 2026-05-15 (7 days; bundled with SentinelOne and the open Rapid7 / SecurityWeek window)

---

## 2026-05-08 — Polish Internal Security Agency (ABW) — (none) → B (provisional, awaiting ratification)

**Type:** New source — provisional
**Source ID:** `abw`
**Reason:** First Archimedes-corpus citation as the originating source on `finding-2026-05-08-0009` (Polish water-utility ICS breach attribution to APT28 / APT29 / UNC1151 — five facilities at Jabłonna Lacka, Szczytno, Małdyty, Tolkmicko, Sierakowo; weak password policies and internet-exposed ICS as attack vectors; ICS-modify capability claimed at some sites). Foreign government national security agency — official-body category. Proposed grade B by the briefer/grader, conservative starting grade for a foreign-government source where attribution methodology is not visible to Archimedes (ABW did not publish technical IOCs or methodology with this advisory; relayed via SecurityWeek with no independent corroboration). Operator may ratify at B, upgrade toward A if subsequent ABW outputs include verifiable technical content, or downgrade if attribution patterns prove non-canonical.
**Operational caveat:** the brief and finding flag that Sandworm (GRU Unit 74455) is the canonical GRU ICS-modify actor; APT28 (Unit 26165, SIGINT) and APT29 (SVR, geopolitical espionage) doing ICS-modify is non-canonical. Analyst SAT-ACH on finding 0009 ranks shorthand-naming, cooperative-tasking, and hacktivist-with-cooperative-capability readings collectively more probable than literal direct-GRU/SVR attribution. ABW's grade does not load-bear on the WEP — the procedural fact "ABW publicly attributed" carries at B2/likely; the substantive attribution claim is preserved-with-caveat per Hard Rule 2 (Archimedes does not originate alternative attribution).
**Supporting findings:** [finding-2026-05-08-0009]
**Posted to:** Discord `#actor-review` (message id pending — see librarian Splunk telemetry for this run)
**Reviewer:** Awaiting Ryan ratification via `/approve-source-grade abw B` (or operator upgrade to A / downgrade to C)
**Provisional flag set:** `provisional: true`, `awaiting_ratification: true` in `infrastructure/source-grades.yaml`
**Effect on referencing finding:** Finding 0009 is digraph B2 / WEP likely on the procedural fact only. Provisional B grading is what holds the B2 digraph — operator downgrade to C would re-grade to C2 (still WEP-likely floor on procedural fact). Substantive attribution truth-claim is preserved-with-caveat regardless of ABW grade.
**Next review:** ratification target 2026-05-15 (7 days; bundled with SentinelOne / LayerX / Seqrite Labs and the open Rapid7 / SecurityWeek window)

---

## 2026-05-08 — Seqrite Labs (Quick Heal) — (none) → C (provisional, awaiting ratification)

**Type:** New source — provisional
**Source ID:** `seqrite-labs`
**Reason:** First Archimedes-corpus citation as the originating source on `finding-2026-05-08-0010` (Operation Silent Rotor — Rust malware vs Eurasian UAV sector; Russian-language lures masquerading as Russian Aeronautical Information Center order confirmations; Boeing-aliased decoy content as audience-targeting not Boeing-targeting; C2 on `cdn[.]kleymarket[.]ru` AS48347 MTW-AS Moscow). Sole primary; SecurityWeek In Other News column relay. Tier-2 AV/EDR research firm (Indian-origin, Quick Heal parent). Technical depth-rich primary on this finding (named C2 domain + IPv4 set + SHA-256 hashes + lure-document analysis + AS attribution). No prior Archimedes-corpus track record to assess; provisional C is conservative starting grade per the same precedent as LayerX (2026-05-08). Operator may upgrade to B if subsequent findings show consistent technical rigor and accuracy, or hold at C if context-thin commercial-research profile is observed across more findings.
**Methodological positive:** Seqrite explicitly does NOT attribute the campaign to a tracked actor — campaign-attribution restraint is a positive signal for an unknown vendor's analytical discipline.
**Supporting findings:** [finding-2026-05-08-0010]
**Posted to:** Discord `#actor-review` (message id pending — see librarian Splunk telemetry for this run)
**Reviewer:** Awaiting Ryan ratification via `/approve-source-grade seqrite-labs C` (or operator upgrade to B)
**Provisional flag set:** `provisional: true`, `awaiting_ratification: true` in `infrastructure/source-grades.yaml`
**Effect on referencing finding:** Finding 0010 is digraph C2 / WEP likely with single-source-veto active (Seqrite sole primary). Provisional C grading is what holds the C2 digraph — this is the floor, no further downgrade path on grade alone. Operator upgrade to B would re-grade 0010 to B2 and lift the WEP cap slightly (still single-source-veto-capped).
**Next review:** ratification target 2026-05-15 (7 days; bundled with SentinelOne / LayerX / ABW and the open Rapid7 / SecurityWeek window)

---

## 2026-05-12 — Mini Shai-Hulud cluster (7 new sources) — (none) → A/A/B/B/B/C/C (all provisional, awaiting ratification)

**Type:** New source(s) — provisional (bulk-bundle for one finding)
**Source IDs:** `wiz-research` (A), `snyk` (A), `stepsecurity` (B), `semgrep` (B), `onapsis` (B), `aikido-security` (C), `safedep` (C)
**Reason:** First Archimedes-corpus citation for all seven via `finding-2026-05-12-FLASH-0001` (Mini Shai-Hulud npm + PyPI worm; CVE-2026-45321 / GHSA-g7cv-rxg3-hmpx; TeamPCP attribution per Wiz + StepSecurity, with Snyk relaying StepSecurity; ~172 packages compromised across @tanstack / @uipath / @mistralai / @opensearch-project / @squawk / @tallyui / DraftLab namespaces + PyPI guardrails-ai@0.10.1 / mistralai@2.4.6). Grades anchor on the named-research-firm primaries (Wiz + Snyk) rather than the aggregating relay (The Hacker News). Per INTEL-GRADING independence doctrine, the relay does not contribute independent grade-weight — grading anchors on the underlying research.

  - **Wiz Research (provisional A):** Tier-1 cloud-security research practice with named-research-team bylines, peer-reviewed publications, established methodology. Recent track record on supply-chain attack analysis (SAP CAP Mini Shai-Hulud coverage 2026; ongoing npm ecosystem research). High-confidence TeamPCP attribution language matches the evidentiary standard of Tier-1 vendor research (Mandiant, CrowdStrike, Unit 42 tier). Precedent: SentinelOne (2026-05-08 first surface) / Sophos / ESET / Dragos (Session 11 ratifications).
  - **Snyk (provisional A):** Tier-1 application-security research practice with named-analyst byline (Stephen Thoemmes). CVE coordination role on this surface (originating CVE-2026-45321 + GHSA-g7cv-rxg3-hmpx publication). Cross-references peer analyses with discipline. AppSec research practice with consistent technical rigor and ecosystem visibility.
  - **StepSecurity (provisional B):** CI/CD-security specialist vendor research practice; originating attribution source for TeamPCP on this campaign per Wiz + Snyk citations. Narrower technical scope than Tier-1 vendor research but consistent rigor. Conservative starting grade per Tier-2-vendor-research precedent.
  - **Semgrep (provisional B):** Established code-security vendor with named-engineer bylines; coordinated supply-chain attack analysis on this surface. Conservative starting grade.
  - **Onapsis (provisional B):** SAP-security specialist with published earlier 2026 SAP CAP Mini Shai-Hulud coverage feeding the Shai-Hulud-family lineage. Tier-2 specialist scope. Conservative starting grade.
  - **Aikido Security (provisional C):** Application-security vendor research; first surface. Conservative C per LayerX / Seqrite / Trendyol / Albayrak precedent for vendor-research firms without prior corpus track record.
  - **SafeDep (provisional C):** First-surface npm security vendor; conservative C per same precedent as Aikido above.

**Methodological positive on first surface (cluster-level):** Multiple sources operating with attribution-naming discipline. Wiz's "behind prior SAP, Checkmarx, and other compromises" framing is lineage-pattern reasoning explicitly scoped to TeamPCP per their internal cluster, not Archimedes-origination. Snyk's CVE-coordination role surfaces ecosystem-wide responsiveness. StepSecurity originating the TeamPCP attribution and Wiz citing it (rather than parallel attribution) was correctly identified by the grader as an attribution-independence concern — Snyk's TeamPCP attribution is a relay of StepSecurity's, not independent corroboration. The analyst SAT-ACH analysis flagged this assumption (A5) as Test classification — the load-bearing assumption for the entire attribution layer.
**Supporting findings:** [finding-2026-05-12-FLASH-0001]
**Posted to:** Not posted to Discord `#actor-review` this run — none of the seven are downgrades. The five non-A entries (StepSecurity/Semgrep/Onapsis/Aikido/SafeDep) are first-surface provisional entries at the conservative tier; the two A-grade provisionals (Wiz, Snyk) follow the SentinelOne / Sophos / ESET / Dragos precedent for Tier-1 vendor research with named bylines and don't require sign-off-before-commit (operator ratification window applies).
**Reviewer:** Awaiting Ryan ratification via bundled `/approve-source-grade` calls (target 2026-05-17 with the open SentinelOne / LayerX / ABW / Seqrite Labs / Trendyol-Albayrak / Rapid7 / SecurityWeek window)
**Provisional flag set:** `provisional: true`, `awaiting_ratification: true` in `infrastructure/source-grades.yaml` for all seven
**Effect on referencing finding:** Finding FLASH-0001 is digraph A2 (anchored on Wiz + Unit42 + MSTIC + Snyk A-grade backbone with StepSecurity B-grade redundancy and Aikido/SafeDep C-grade redundancy; credibility 2 for confirmed-by-other-sources at procedural-fact layer, partly-uncorroborated at attribution layer); WEP "likely" cap held by Snyk-relays-StepSecurity attribution-independence concern. Grader-conservative WEP cap survives operator hold of any source at the proposed grade. Operator downgrade of Wiz from A to B would shift the attribution-layer source-mix and could trigger single-source-veto re-evaluation on the TeamPCP claim.
**Next review:** ratification target 2026-05-17 (5 days; bundled with the open provisional-source backlog)

---

## 2026-05-10 — Trendyol Group / Berk Albayrak — (none) → C (provisional, awaiting ratification)

**Type:** New source — provisional
**Source ID:** `trendyol-group-albayrak`
**Reason:** First Archimedes-corpus citation as the originating source on `finding-2026-05-10-0001` (MacSync macOS infostealer surfaced via Google Ads malvertising for "Claude mac download" search query, plus abuse of real Anthropic `claude.ai/share/...` shared-chat URLs as in-lure instruction page; `curl | sh` shell-loader chain through `customroofingcontractors[.]com` → `bernasibutuwqu2[.]com`). Sole primary; BleepingComputer (Ax Sharma) relay. Researcher Berk Albayrak is a security engineer at Trendyol Group (Turkey's largest e-commerce platform). Legitimate corporate security organization with a real security team — rules out F — but not a Tier-1 vendor research practice with peer-reviewed APT/malware track record — rules out A/B. No prior Archimedes-corpus citations; no peer-reviewed APT or malware research history visible at first surface. Provisional C is the conservative starting grade per the same precedent as LayerX (2026-05-08) and Seqrite Labs (2026-05-08). Operator may upgrade to B if subsequent findings show consistent technical rigor and accuracy, or hold at C if context-thin commercial-research profile is observed across more findings.
**Methodological positive on first surface:** Source makes NO threat-actor attribution. Source explicitly flags the "MacSync" family designation as researcher-coined working name, not vendor-consensus naming. Campaign-attribution restraint and naming-discipline are positive signals for analytical maturity on an unknown vendor's first surface.
**Supporting findings:** [finding-2026-05-10-0001]
**Posted to:** Not posted to Discord `#actor-review` this run — provisional C is the LayerX/Seqrite-precedent floor and not a downgrade-path that requires sign-off; operator can review at the bundled 2026-05-15 ratification window.
**Reviewer:** Awaiting Ryan ratification via `/approve-source-grade trendyol-group-albayrak C` (or operator upgrade to B)
**Provisional flag set:** `provisional: true`, `awaiting_ratification: true` in `infrastructure/source-grades.yaml`
**Effect on referencing finding:** Finding 0001 is digraph B3 (BleepingComputer-relay floor at B; credibility 3 for single-source-uncorroborated) / WEP "likely" capped by single-source veto on procedural facts, "roughly even chance" on operational claims (split-WEP per analyst KAC). Trendyol-Albayrak's grade does not load-bear on the finding's WEP — relay floor at BleepingComputer's B is what holds B3. Operator upgrade of Trendyol to B would not change the digraph (BleepingComputer relay floor still B); operator hold at C is the no-op case.
**Detection-engineering caveat (carried verbatim from finding):** the two `claude.ai/share/...` URLs in the IOC set are share-ID-level IOCs ONLY. Wholesale `claude.ai` blocking would break legitimate Anthropic enterprise platform use; attackers can mint new share-IDs at will. Defensive value is share-ID telemetry plus user-education on AI-brand-impersonation social engineering, NOT domain blocklisting.
**Next review:** ratification target 2026-05-17 (7 days; bundled with the open SentinelOne / LayerX / ABW / Seqrite Labs / Rapid7 / SecurityWeek window)

---

## 2026-05-13 — Bitdefender Labs — (none) → A (provisional, awaiting ratification)

**Type:** New source — provisional
**Source ID:** `bitdefender`
**Reason:** First Archimedes-corpus citation as the originating source on `finding-2026-05-13-FLASH-0001` (Bitdefender attributes Azerbaijani oil & gas multi-wave Exchange intrusion December 2025 → February 2026 to **FamousSparrow** at moderate-to-high confidence — a listed alias for Salt Typhoon roster id 010 HIGH, China MSS). Sole primary; The Hacker News (Ravie Lakshmanan) and Dark Reading relay and add no independent evidence basis (both cite Bitdefender as origin; single-source veto applies, WEP capped at "likely"). Bitdefender Labs is widely treated as Tier-1 vendor research practice — named-analyst bylines (Victor Vrabie + Martin Zugec on this surface), first-party EDR telemetry, IntelliZone curated IOC distribution platform, peer-reviewed APT research track record including prior 2023-2024 FamousSparrow → Salt Typhoon attribution work with ESET + Microsoft cross-corroboration. Moderate-to-high confidence attribution language matches the evidentiary standard of Mandiant / CrowdStrike / Unit 42 / MSTIC tier. Proposed grade A by the grader on that peer-tier assumption.
**Supporting findings:** [finding-2026-05-13-FLASH-0001]
**Posted to:** Discord `#actor-review` is NOT posted for this provisional — pattern is "log here, surface in next ratification sweep with the rest" per the precedent established 2026-05-06 (Rapid7 / SecurityWeek) and 2026-05-08 (SentinelOne / LayerX / ABW / Seqrite Labs). Operator can drive `/approve-source-grade bitdefender A` via the established ratification sweep.
**Reviewer:** Awaiting Ryan ratification via `/approve-source-grade bitdefender A` (or operator downgrade)
**Provisional flag set:** `provisional: true`, `awaiting_ratification: true` in `infrastructure/source-grades.yaml`
**Effect on referencing finding:** Finding FLASH-0001 is digraph A2 / WEP "likely" with single-source-veto active (Bitdefender sole effective primary on attribution + TTP-delta; relays fail independence test). Provisional A grading is what holds the A2 digraph — operator downgrade to B would re-grade FLASH-0001 to B2 and the WEP cap would still apply (single-source-veto remains load-bearing on attribution layer). The procedural sub-claims (CVE chain in NVD A1; VT-confirmed C2 domains malicious 2/92 B1) are independent of Bitdefender's grade.
**Recalibration watch (72h):** A second independent IR-grade source (Mandiant / CrowdStrike / Unit 42 / MSTIC / ESET / Cisco Talos — originator of UAT-9244 cluster designation per Bitdefender citation) publishing matching IOCs + cluster cross-walk with own telemetry before 2026-05-16 14:30 EDT lifts finding FLASH-0001 to A1 / WEP "very likely" pending red-team review and increases the defensibility of ratifying Bitdefender at A. Disconfirmation (any A/B-grade source disputing attribution or naming a different actor for the same campaign) triggers retraction-or-amendment per RETRACTION-POLICY.
**Methodological positive:** Bitdefender's attribution language ("moderate-to-high confidence, based on combined weight of observed TTPs, malware families, and execution flow") shows appropriate calibration — does not overclaim certainty for a single-vendor disclosure; documents the basis for the confidence level explicitly.
**Next review:** ratification target 2026-05-20 (7 days; bundled with the open SentinelOne / LayerX / ABW / Seqrite Labs / Trendyol-Albayrak / Rapid7 / SecurityWeek / Wiz / Snyk / StepSecurity / Semgrep / Onapsis / Aikido / SafeDep ratification window)

---

## Entry template

*Copy the format below when logging a grade change.*

```
## YYYY-MM-DD — Source-Name — OLD → NEW

**Type:** Downgrade | Upgrade | New source | Deactivation | Reactivation
**Source ID:** <source-id from source-grades.yaml>
**Reason:** <specific miss/hit, or rationale, with links to evidence>
**Supporting findings:** [finding-IDs that support the change]
**Reviewer:** <human or agent>
**Next review:** YYYY-MM-DD
```
