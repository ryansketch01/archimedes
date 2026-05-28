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

## 2026-05-14 — F5 (PSIRT / K-articles / NGINX advisories) — (none) → A (provisional, awaiting ratification)

**Type:** New source — provisional
**Source ID:** `f5`
**Reason:** First Archimedes-corpus citation as vendor self-disclosure on `finding-2026-05-14-0002` (K000160932 quarterly advisory — 50+ CVEs headlined by CVE-2026-42945 "NGINX Rift" heap overflow in the rewrite module, CVSS v4 9.2, pre-auth RCE ASLR-dependent / DoS otherwise; cohort: CVE-2026-41225 iControl REST authenticated privesc + CVE-2026-41957 / 34176 / 39459 BIG-IP authenticated-RCE family). Vendor-self-disclosure on own products is procedurally A-grade per precedent established with Palo Alto PSIRT (FLASH-0001), Microsoft MSRC, Cisco PSIRT. F5 published K-article series with named-product-version patch matrix (NGINX Plus R32 P6+ / R36 P4+, Open Source 1.30.1 / 1.31.0, Ingress Controller, App Protect WAF), explicit no-in-the-wild-exploitation framing, and explicit ASLR-dependency caveat. Proposed grade A by the grader on the assumption it sits with peer vendor PSIRTs.
**Supporting findings:** [finding-2026-05-14-0002]
**Posted to:** Not posted to Discord `#actor-review` this run — pattern is "log here, surface in next ratification sweep with the rest" per the established precedent (Rapid7 / SecurityWeek / SentinelOne / Bitdefender / Symantec etc.). Operator can drive `/approve-source-grade f5 A` via the established ratification sweep.
**Reviewer:** Awaiting Ryan ratification via `/approve-source-grade f5 A` (or operator downgrade)
**Provisional flag set:** `provisional: true`, `awaiting_ratification: true` in `infrastructure/source-grades.yaml`
**Effect on referencing finding:** Finding 0002 is digraph A2 / WEP "very likely (vendor procedural)" + "likely (no-ITW)". Provisional A grading from F5 holds the A2 digraph; operator downgrade to B would re-grade finding-2026-05-14-0002 to B2 — no change to WEP cap given the procedural-vs-claim WEP split is already explicit.
**Next review:** ratification target 2026-05-21 (7 days; bundled with the open ratification window)

---

## 2026-05-14 — kernel.org netdev — (none) → A (provisional, awaiting ratification)

**Type:** New source — provisional
**Source ID:** `kernel-org-netdev`
**Reason:** First Archimedes-corpus citation as vendor self-disclosure on `finding-2026-05-14-0003` (Fragnesia CVE-2026-46300 XFRM ESP-in-TCP page-cache-corruption kernel patch posted to netdev 2026-05-13; distros rolling same-day). Vendor-self-disclosure on own product is procedurally A-grade per same precedent as F5 (this run), Palo Alto PSIRT, Microsoft MSRC, Cisco PSIRT. kernel.org / Linux netdev is the authoritative upstream maintainer publication channel for the Linux kernel — patches are the canonical fact-of-vulnerability source. Proposed grade A.
**Supporting findings:** [finding-2026-05-14-0003]
**Posted to:** Not posted to Discord `#actor-review` this run — bundled ratification.
**Reviewer:** Awaiting Ryan ratification via `/approve-source-grade kernel-org-netdev A` (or operator downgrade)
**Provisional flag set:** `provisional: true`, `awaiting_ratification: true` in `infrastructure/source-grades.yaml`
**Effect on referencing finding:** Finding 0003 is digraph A2 (Copy Fail KEV-anchored) / B2 (Fragnesia analyst-split). kernel-org-netdev grades the Fragnesia kernel-patch-existence sub-claim; operator downgrade would affect the B2 cap on Fragnesia (analyst split already at "roughly even chance" on weaponization inference). Cosmetic at finding level.
**Next review:** ratification target 2026-05-21 (7 days; bundled)

---

## 2026-05-14 — Sysdig Threat Research Team — (none) → B (provisional, awaiting ratification)

**Type:** New source — provisional
**Source ID:** `sysdig`
**Reason:** First Archimedes-corpus citation as the originating source on `finding-2026-05-14-0004` (PraisonAI CVE-2026-44338 Flask API auth-bypass scanner traffic detected 3h44m post-disclosure; UA `CVE-Detector/1.0`; two passes 8 minutes apart, ~70 requests / ~50s each; characterized as "associated with a scanner, not interactive exploitation" — Sysdig hedge preserved verbatim per Hard Rule 2). Sysdig Threat Research Team has Falco-pedigree (CNCF runtime-security project lineage) and named-analyst-byline cloud-native security research. Conservative provisional B starting grade for unknown-to-corpus vendor research practice per same precedent as SecurityWeek (2026-05-06), LayerX (2026-05-08), Trendyol-Albayrak (2026-05-10).
**Methodological positives on first surface:** Explicit scanner-vs-exploitation hedge in Sysdig's own framing; named UA fingerprint; named patched version (4.6.34); explicit `agents.yaml`-as-bounded-impact framing; SecurityWeek (Eduard Kovacs) relay preserves Sysdig hedge verbatim. Source makes NO threat-actor attribution.
**Supporting findings:** [finding-2026-05-14-0004]
**Posted to:** Not posted to Discord `#actor-review` this run — bundled ratification.
**Reviewer:** Awaiting Ryan ratification via `/approve-source-grade sysdig B` (or operator upgrade to A / hold at C)
**Provisional flag set:** `provisional: true`, `awaiting_ratification: true` in `infrastructure/source-grades.yaml`
**Effect on referencing finding:** Finding 0004 is digraph B2 / WEP "very likely" (KEV-Detector traffic procedurally observed by Sysdig; relay floor at SecurityWeek's B is what holds B2). Operator hold at C would not change the digraph (SecurityWeek B relay floor still B); operator upgrade to A would lift Sysdig-originating sub-claims toward A2 on subsequent surfaces.
**Next review:** ratification target 2026-05-21 (7 days; bundled)

---

## 2026-05-14 — Zellic (William Bowling) — (none) → B (provisional, awaiting ratification)

**Type:** New source — provisional
**Source ID:** `zellic`
**Reason:** First Archimedes-corpus citation as originating-source on `finding-2026-05-14-0003` (Fragnesia CVE-2026-46300 PoC publishing — working PoC corrupting `/usr/bin/su` page cache to root shell). Zellic is a security-research / audit firm; William Bowling is a named-byline researcher with prior public kernel-LPE / browser-exploit track record (vendor-acknowledged across multiple Pwn2Own + browser-vendor security bulletins). Conservative provisional B starting grade for unknown-to-corpus vendor-research firm per same precedent as SecurityWeek, LayerX, Trendyol-Albayrak, Sysdig (this run).
**Methodological positives on first surface:** PoC published with named researcher; vendor-coordinated disclosure timing (post-kernel-patch on netdev 2026-05-13); explicit primitive description in BleepingComputer relay (arbitrary byte writes into kernel page cache; specific `/usr/bin/su` demo as proof-of-concept boundary, not weaponized capability claim).
**Analyst-ACH cross-reference:** Analyst's ACH on the Fragnesia weaponization curve ranks H3 (slow weaponization, Dirty Pipe / Dirty Cow base rate) first with zero inconsistencies; Zellic's controlled PoC publishing posture is consistent with that base rate. No analyst recommendation to escalate.
**Supporting findings:** [finding-2026-05-14-0003]
**Posted to:** Not posted to Discord `#actor-review` this run — bundled ratification.
**Reviewer:** Awaiting Ryan ratification via `/approve-source-grade zellic B` (or operator upgrade to A / hold at C)
**Provisional flag set:** `provisional: true`, `awaiting_ratification: true` in `infrastructure/source-grades.yaml`
**Effect on referencing finding:** Finding 0003 Fragnesia sub-cluster is digraph B2 / WEP "likely (PoC + no-ITW)" / "roughly even chance (30-day weaponization inference)". Zellic's grade holds the B2 floor on the PoC-existence sub-claim; operator upgrade to A would lift PoC-existence sub-claim toward A2 on subsequent Zellic surfaces.
**Next review:** ratification target 2026-05-21 (7 days; bundled)

---

## 2026-05-14 — The Hacker News — (none) → B (provisional, awaiting ratification)

**Type:** New source — provisional (second-cross-corroboration-cycle)
**Source ID:** `thehackernews`
**Reason:** Multiple prior Archimedes-corpus relay surfaces (finding-2026-05-13-FLASH-0001 Bitdefender / FamousSparrow relay; finding-2026-05-13-FLASH-1800-0001 Symantec / MuddyWater relay) without dedicated source-grades.yaml entry; this run is the second-cross-corroboration-cycle threshold per orchestrator librarian handoff. Today's 2026-05-14 morning brief uses The Hacker News as relay on TWO independent findings: finding-2026-05-14-0002 (NGINX Rift relay of SecurityWeek / F5 K000160932) + finding-2026-05-14-0003 (Fragnesia relay of BleepingComputer / Zellic). Fast-cycle security-media outlet on a par with BleepingComputer / SecurityWeek; conservative provisional B starting grade per peer precedent.
**Editorial-amplification observed (flag for ratification review):** On finding-2026-05-14-0002, The Hacker News introduced an "18-year dormancy" framing (citing depthfirst researcher commentary) for CVE-2026-42945 NGINX Rift that is NOT present in F5 K000160932 vendor primary. Briefer flagged this explicitly per Hard Rule 2 as THN + depthfirst editorial, NOT vendor-attested. If editorial-overreach pattern recurs on subsequent surfaces, consider downgrade to C — same trip-wire applied to industrialcyber-co relay-layer-conflation flag on 2026-05-13.
**Supporting findings:** [finding-2026-05-13-FLASH-0001, finding-2026-05-13-FLASH-1800-0001, finding-2026-05-14-0002, finding-2026-05-14-0003]
**Posted to:** Not posted to Discord `#actor-review` this run — bundled ratification.
**Reviewer:** Awaiting Ryan ratification via `/approve-source-grade thehackernews B` (or operator downgrade to C citing editorial-amplification pattern)
**Provisional flag set:** `provisional: true`, `awaiting_ratification: true` in `infrastructure/source-grades.yaml`
**Effect on referencing findings:** All four findings carry The Hacker News as relay only; grade does not load-bear on any WEP cap (primaries — Bitdefender, Symantec, F5, BleepingComputer/Zellic — hold the digraphs). Operator downgrade to C is cosmetic at finding level.
**Next review:** ratification target 2026-05-21 (7 days; bundled)

---

## 2026-05-14 — depthfirst (independent researcher) — (none) → F (provisional, awaiting ratification)

**Type:** New source — provisional
**Source ID:** `depthfirst`
**Reason:** First Archimedes-corpus citation via finding-2026-05-14-0002 commentary chain — cited by The Hacker News on CVE-2026-42945 NGINX Rift "18-year dormancy" editorial framing. Per Hard Rule 2 the dormancy headline is THN + depthfirst editorial, NOT vendor-attested in F5 K000160932 primary. depthfirst is an independent researcher / commentator with no prior Archimedes-corpus track record and no observed first-party vulnerability research or vendor-acknowledged disclosure history at first surface. Conservative provisional F (unknown / unestablished) starting grade per category baseline for unknown independent voices — does not load-bear on any finding's WEP this run; the NGINX Rift finding's A2 digraph rests on F5 vendor-self-disclosure (provisional A) + SecurityWeek relay.
**Why F not C:** F category in INTEL-GRADING.md applies to "unknown / cannot be judged" sources without prior track record. Provisional F is the conservative floor pending observable research history. Operator may upgrade if subsequent surfaces show vendor-acknowledged disclosure or peer-reviewed publication. This is the first time a researcher provisional-F has been logged via this flow — surface in next doctrine review for naming-convention codification.
**Supporting findings:** [finding-2026-05-14-0002]
**Posted to:** Not posted to Discord `#actor-review` this run — bundled ratification.
**Reviewer:** Awaiting Ryan ratification via `/approve-source-grade depthfirst F` (or operator upgrade)
**Provisional flag set:** `provisional: true`, `awaiting_ratification: true` in `infrastructure/source-grades.yaml`
**Effect on referencing finding:** Cosmetic — depthfirst is cited only through THN editorial framing on finding-2026-05-14-0002, which the briefer already flagged as non-vendor-attested per Hard Rule 2. WEP does not depend on this source's grade.
**Next review:** ratification target 2026-05-21 (7 days; bundled)

---

## 2026-05-15 — Ox Security — (none) → B (provisional, awaiting ratification + direct retrieval)

**Type:** New source — provisional
**Source ID:** `ox-security`
**Reason:** First Archimedes-corpus citation via finding-2026-05-15-0005 (node-ipc compromise four-firm UNATTRIBUTED consensus — Socket + StepSecurity + Ox Security + Upwind all decline TeamPCP / Shai-Hulud / Mini Shai-Hulud lineage). Cited via BleepingComputer relay; primary not yet directly retrieved by Archimedes collector — provisional grade is from relay-layer citation only, marked for direct-retrieval verification on next collector pass. Ox Security is an application-security / supply-chain-security vendor with named published research on npm and software-supply-chain attacks. Tier-2 supply-chain-security specialist scope — consistent with the provisional-B grade applied to Socket (2026-05-14, also first-cited on the node-ipc cluster) and StepSecurity (2026-05-12). Strong methodological signal on this surface: explicitly declines TeamPCP / Shai-Hulud / Mini Shai-Hulud attribution despite operational adjacency, consistent with the other three firms in the four-firm consensus — Hard Rule 2 compliant.
**Why B not A:** Tier-2 supply-chain-security specialist scope per same precedent as Socket / StepSecurity peers; first surface in the corpus; relay-only citation pending direct retrieval. Conservative starting grade.
**Why B not C:** Named-vendor research practice with prior publication history on supply-chain attacks (not unknown / unestablished); UNATTRIBUTED-disposition methodological discipline is a positive signal.
**Supporting findings:** [finding-2026-05-15-0005]
**Posted to:** Not posted to Discord `#actor-review` this run — bundled ratification.
**Reviewer:** Awaiting Ryan ratification via `/approve-source-grade ox-security B` (or operator adjustment)
**Provisional flag set:** `provisional: true`, `awaiting_ratification: true`, `awaiting_direct_retrieval: true` in `infrastructure/source-grades.yaml`
**Effect on referencing finding:** Co-corroborator in the four-firm UNATTRIBUTED consensus; load-bears on WEP **very likely** for the UNATTRIBUTED disposition (four firms, four methodologies). Direct retrieval next collector pass will firm up grade.
**Next review:** ratification target 2026-05-22 (7 days; bundled)

---

## 2026-05-15 — Upwind — (none) → B (provisional, awaiting ratification + direct retrieval)

**Type:** New source — provisional
**Source ID:** `upwind`
**Reason:** First Archimedes-corpus citation via finding-2026-05-15-0005 (node-ipc compromise four-firm UNATTRIBUTED consensus — Socket + StepSecurity + Ox Security + Upwind all decline TeamPCP / Shai-Hulud / Mini Shai-Hulud lineage). Cited via BleepingComputer relay; primary not yet directly retrieved by Archimedes collector — provisional grade is from relay-layer citation only, marked for direct-retrieval verification on next collector pass. Upwind is a cloud-native / runtime-security vendor with prior corpus-adjacent visibility via Snyk's Mini Shai-Hulud cross-reference (finding-2026-05-12-FLASH-0001 explicitly cited Upwind Security deobfuscation work) — this is the first surface where Upwind appears as a directly-cited source rather than a Snyk-referenced peer. Tier-2 supply-chain / runtime-security specialist scope — consistent with the provisional-B grade applied to Socket / StepSecurity / Ox Security.
**Why B not A:** Tier-2 supply-chain / runtime-security specialist scope per same precedent as Socket / StepSecurity / Ox Security peers; first directly-cited surface in the corpus; relay-only citation pending direct retrieval.
**Why B not C:** Prior corpus-adjacent visibility via Snyk cross-reference (finding-2026-05-12-FLASH-0001) shows Snyk-tier vendors treat Upwind's deobfuscation work as peer-citable; UNATTRIBUTED-disposition methodological discipline on this surface is a positive signal.
**Supporting findings:** [finding-2026-05-15-0005, finding-2026-05-12-FLASH-0001 (peer-referenced, not directly cited)]
**Posted to:** Not posted to Discord `#actor-review` this run — bundled ratification.
**Reviewer:** Awaiting Ryan ratification via `/approve-source-grade upwind B` (or operator adjustment)
**Provisional flag set:** `provisional: true`, `awaiting_ratification: true`, `awaiting_direct_retrieval: true` in `infrastructure/source-grades.yaml`
**Effect on referencing finding:** Co-corroborator in the four-firm UNATTRIBUTED consensus; load-bears on WEP **very likely** for the UNATTRIBUTED disposition. Direct retrieval next collector pass will firm up grade.
**Next review:** ratification target 2026-05-22 (7 days; bundled)

---

## 2026-05-16 — depthfirst (independent researcher) — F (provisional) → C (provisional, awaiting ratification)

**Type:** Upgrade (provisional → provisional, F → C)
**Source ID:** `depthfirst`
**Reason:** Elevation triggered per source-grade-log.md 2026-05-14 depthfirst entry's documented criteria: "elevate if subsequent surfaces show vendor-acknowledged disclosure or peer-reviewed publication" / "elevate to provisional-C on first technical write-up publication." Today's `finding-2026-05-16-0001` (NGINX Rift CVE-2026-42945 PoC publication) surfaces depthfirst as the named PoC author at the GitHub repository `https://github.com/depthfirstdisclosures/nginx-rift` per SecurityWeek (Ionut Arghire byline, B provisional) primary 2026-05-16 06:02 EDT. depthfirst is the originating researcher credited on CVE-2026-42945 per the F5 K000160932 chain (carry-forward from finding-2026-05-14-0002 — vendor-attested). The GitHub PoC repository constitutes a technical-output publication; depthfirst transitions from "cited researcher via THN editorial framing" (F surface) to "named PoC author with operational artifact at a stated URL with vendor-attested originating-research credit" (C surface). Hard Rule 3 prevents Archimedes from fetching the PoC repository contents — the elevation rests on the vendor-attested originating-research credit (F5 K000160932) plus the SecurityWeek-attested publication act, not on Archimedes' own verification of the artifact. Conservative C is the precedent grade for first-publication independent-researcher surfaces with vendor-acknowledgement context (LayerX-precedent / Seqrite-precedent / Trendyol-Albayrak-precedent class for unknown / single-surface researchers).
**Why C not B:** Tier-2 evidence — single publication, no peer-review yet, no vendor-acknowledgement of the PoC code itself (vs. the CVE credit which IS vendor-attested per F5 K000160932). Operator may upgrade to B on subsequent surfaces showing peer-reviewed publication or vendor coordination on a second CVE / technical write-up.
**Why C not D:** Vendor-attested originating-research credit on CVE-2026-42945 lifts depthfirst above the "unknown / unestablished" floor that justified the prior F surface. F→C is a one-grade elevation per "first technical write-up publication" trigger, NOT a multi-grade jump.
**Supporting findings:** [finding-2026-05-16-0001]; [finding-2026-05-14-0002 carry-forward context]
**Posted to:** Not posted to Discord `#actor-review` this run — non-material per Hard Rule 5 (this is an upgrade not a downgrade, and B→D-or-worse downgrade is the only threshold requiring human review per RETRACTION-POLICY adjacent / source-grade-log.md governance). Bundled with the 2026-05-21 ratification window per depthfirst's 2026-05-14 entry next-review date.
**Reviewer:** Awaiting Ryan ratification via `/approve-source-grade depthfirst C` (or operator adjustment).
**Provisional flag set:** `provisional: true`, `awaiting_ratification: true` in `infrastructure/source-grades.yaml`; provisional_history records the F→C transition with retired_at: 2026-05-16.
**Effect on referencing finding:** `finding-2026-05-16-0001` cluster anchor is B2 with SecurityWeek as B-grade primary on the PoC-publication-event layer; depthfirst is listed as supporting-source carry-forward at the new C grade. WEP cap stays at "likely" on the new operational-delta layer (single-source veto via SecurityWeek single primary; depthfirst grade is not WEP-load-bearing). Operator downgrade to B would not change finding's WEP; upgrade to B in a future cycle would help if combined with an independent second-primary source.
**Next review:** ratification target 2026-05-21 (7 days; bundled with the 2026-05-14 depthfirst entry).

---

## 2026-05-16 — Zero Day Initiative (zdi-blog) — (none) → A (provisional, awaiting ratification)

**Type:** New source — provisional
**Source ID:** `zdi-blog`
**Reason:** First Archimedes-corpus citation via `finding-2026-05-16-0002` (Pwn2Own Berlin 2026 Day 3 final results and Master of Pwn — 3 successful exploits on Day 3 / $34,500 in payouts / bringing event total to $943,250 across 42 unique zero-days; Day 2 Orange Tsai / DEVCORE Microsoft Exchange RCE-to-SYSTEM chain remains under standard ZDI 90-day vendor-coordinated-disclosure embargo with expected CVE assignment window 2026-07 to 2026-08). ZDI / Trend Micro is the canonical Pwn2Own contest coordinator, judge, and exclusive publisher of contest results, payouts, and embargoed-CVE disclosure coordination since 2007. Dustin Childs (Communications Manager, ZDI) is the named byline with multi-decade track record in vendor coordination and Pwn2Own contest reporting. Proposed grade A by the grader on the vendor-authority-on-own-contest principle (analogous to F5 vendor self-disclosure of own-product CVEs in finding-2026-05-14-0002, kernel.org netdev on Linux kernel patches in finding-2026-05-14-0003, OpenAI on own incident in finding-2026-05-14-0008).
**Why A not B:** ZDI is procedurally A-grade on contest-mechanical facts (exploit count, payouts, vendor coordination, Master of Pwn standings) because ZDI is the authoritative knowledge-holder for its own contest — there is no higher-quality evidence basis for those specific claim types. Provisional A is consistent with the same precedent class applied to recent first-citation vendor-research / vendor-self-disclosure publications: Bitdefender (2026-05-13), Sysdig (2026-05-14), Wiz Research (2026-05-12), Symantec (2026-05-13), Cisco Talos (2026-05-14 afternoon), Darktrace (2026-05-14), OpenAI self-disclosure (2026-05-14), F5 + kernel-org-netdev (2026-05-14 morning).
**Caveat on grade scope:** ZDI's A grade applies to contest-mechanical facts and embargo-coordination procedural claims. ZDI's editorial framing on AI / coding-assistant attack-surface implications (e.g., the OpenAI Codex result) is analyst-inference territory and should be cited as analyst-extrapolation in any brief that propagates such framing, NOT as ZDI-attested fact. This is the same scope-discipline that applies to F5 / kernel.org / OpenAI vendor-self-disclosure on own-incident scope (A on procedural facts; not A on speculative inferences beyond the procedural envelope).
**Supporting findings:** [finding-2026-05-16-0002]
**Posted to:** Not posted to Discord `#actor-review` this run — bundled ratification.
**Reviewer:** Awaiting Ryan ratification via `/approve-source-grade zdi-blog A` (or operator downgrade to B).
**Provisional flag set:** `provisional: true`, `awaiting_ratification: true` in `infrastructure/source-grades.yaml`.
**Effect on referencing finding:** `finding-2026-05-16-0002` cluster anchor is A2 with ZDI as sole originating primary; single-source veto applies on contest-event layer but does NOT cap WEP because ZDI is vendor authority on own contest (per the layered single_source_veto_rationale on the finding). Operator downgrade to B would re-grade to B2 — same finding-level WEP treatment, cosmetic at finding level.
**Next review:** ratification target 2026-05-23 (7 days).

---

## 2026-05-20 — Cisco PSIRT (Product Security Incident Response Team) — (none) → A (provisional, awaiting ratification)

**Type:** New source — provisional
**Source ID:** `cisco-psirt`
**Reason:** First Archimedes-corpus citation of Cisco PSIRT as a *dedicated* source-grades.yaml id via `finding-2026-05-20-0006` (CVE-2026-20223 Cisco Secure Workload pre-auth REST API authentication bypass, CVSS 10.0, cross-tenant scope-CHANGED; advisory cisco-sa-csw-pnbsa-g8WEnuy). Cisco PSIRT is the canonical vendor authority on Cisco-product CVE disclosure — advisory text, CWE classification, affected/fixed version matrices, SaaS-mitigation status, workarounds, and explicit no-public-exploitation attestations are all first-party vendor-on-own-product authoritative claims. Proposed grade A by the grader on the vendor-self-disclosure precedent already applied to F5 PSIRT (2026-05-14-0002 — K000160932 NGINX Rift), kernel.org netdev maintainer disclosure (2026-05-14-0003 — Fragnesia), OpenAI self-disclosure (2026-05-14-0008 — TanStack breach), and GitHub self-disclosure (2026-05-20-FLASH-0001). This is the **third vendor PSIRT precedent surface** (F5 + Cisco Talos already provisional A; Cisco PSIRT distinct from Cisco Talos — PSIRT publishes advisories on Cisco-product CVEs; Talos publishes threat research on external actors / campaigns / non-Cisco-product CVEs).
**Why A not B:** Cisco PSIRT is procedurally A-grade on Cisco-product CVE-disclosure facts (CVE existence, CVSS scoring, CWE mapping, affected/fixed versions, SaaS mitigation status, workaround availability, no-ITW attestations) because Cisco is the authoritative knowledge-holder for its own product security state — there is no higher-quality evidence basis for those specific claim types. The "third Cisco-product authentication-bypass CVE of 2026" corpus observation is Archimedes-corpus-internal pattern matching, NOT a Cisco PSIRT attribution claim — Hard Rule 2 preserved on finding 0006.
**Caveat on grade scope:** Cisco PSIRT's A grade applies to Cisco-product CVE-disclosure facts and own-product remediation guidance. Cisco PSIRT does NOT publish attribution claims (those go via Cisco Talos with a separate analyst byline and methodology), so no attribution-confidence layer applies. Cross-tenant impact assessment is procedural-CVSS-vector territory (S:C — scope CHANGED), within the A-grade envelope.
**Supporting findings:** [finding-2026-05-20-0006]
**Posted to:** Not posted to Discord `#actor-review` this run — bundled ratification.
**Reviewer:** Awaiting Ryan ratification via `/approve-source-grade cisco-psirt A` (or operator downgrade to B).
**Provisional flag set:** `provisional: true`, `awaiting_ratification: true` in `infrastructure/source-grades.yaml`.
**Effect on referencing finding:** `finding-2026-05-20-0006` cluster anchor is A2 with Cisco PSIRT as sole originating primary; single-source veto applies on mechanism-detail + no-ITW-attestation layers (capping WEP at "likely" on those layers). Operator downgrade to B would re-grade to B2 — same finding-level WEP treatment, cosmetic at finding level.
**Next review:** ratification target 2026-05-27 (7 days).

---

## 2026-05-20 — Aonan Guan (independent security researcher) — (none) → C (provisional, awaiting ratification)

**Type:** New source — provisional
**Source ID:** `aonan-guan`
**Reason:** First Archimedes-corpus citation via `finding-2026-05-20-0007` (Anthropic Claude Code sandbox bypass — SOCKS5 hostname null-byte mechanism class; patched in Claude Code 2.1.88 on 2026-03-31; no CVE assigned to the second bypass; first bypass got CVE-2025-66479 separately). Aonan Guan is an independent security researcher who disclosed the second-bypass mechanism to Anthropic via HackerOne (vendor marked as duplicate of first-bypass report). Cited via SecurityWeek (Eduard Kovacs byline) which is the sole directly-retrieved primary; Guan's own write-up referenced but not directly retrieved this sweep. Proposed grade C by the grader on the independent-researcher precedent applied to LayerX (2026-05-08), Berk Albayrak (Trendyol Group, 2026-05-10), Seqrite Labs analyst byline (2026-05-08), and depthfirst initial F→C elevation (2026-05-16). Independent researchers without prior corpus track record start at C with upgrade path on subsequent corroborated findings.
**Why C not B:** Conservative starting grade for an unknown independent researcher with no prior Archimedes-corpus track record. Upgrade to B (or higher) requires either: (a) direct retrieval of Guan's own write-up confirming technical rigor; (b) second-source corroboration of the SOCKS5 null-byte mechanism by an independent security-research practice; or (c) accumulation of multiple subsequent findings demonstrating consistent technical accuracy.
**Caveat on grade scope:** Provisional C applies to Aonan Guan as a researcher-source category — distinct from `securityweek` (relay channel) and from `anthropic` (the vendor on whose product the bypass exists; Anthropic's HackerOne dispositioning is itself vendor-self-disclosure-adjacent but Anthropic does NOT have its own source-grades.yaml entry yet — see follow-on flag below).
**Supporting findings:** [finding-2026-05-20-0007]
**Posted to:** Not posted to Discord `#actor-review` this run — bundled ratification.
**Reviewer:** Awaiting Ryan ratification via `/approve-source-grade aonan-guan C` (or operator downgrade to F if researcher rigor turns out inconsistent on retrieval).
**Provisional flag set:** `provisional: true`, `awaiting_ratification: true` in `infrastructure/source-grades.yaml`.
**Effect on referencing finding:** `finding-2026-05-20-0007` cluster anchor is B3 with SecurityWeek as sole directly-retrieved primary; single-source veto applies on the SOCKS5 mechanism layer (Aonan Guan's direct write-up not retrieved). Provisional C on Guan does NOT load-bear on the finding's B3 cluster anchor (SecurityWeek B-provisional is the cluster anchor).
**Follow-on flag:** `anthropic` is not yet a source-grades.yaml id. The 2026-05-20 afternoon sweep is the second corpus surface of Anthropic as vendor-self-disclosure-adjacent (first surface was 2026-05-08 KAC A1 Test in finding-2026-05-20-0001 morning carry-forward context, where Anthropic disabled the actor account). Recommend bundling Anthropic-as-vendor-self-disclosure into next quarterly review.
**Next review:** ratification target 2026-05-27 (7 days; bundled with cisco-psirt).

---

## 2026-05-20 — ESET / WeLiveSecurity — A (ratified) — additional supporting citation noted

**Type:** Citation note (no grade change)
**Source ID:** `eset`
**Reason:** `finding-2026-05-20-0004` (Webworm deploys EchoCreep + GraphWorm backdoors against IT services + aerospace + electric power across 9 countries) cites ESET via The Hacker News relay (Eric Howard byline noted in THN coverage). Direct retrieval of welivesecurity.com primary URL not completed this sweep — finding-0004 single-source veto applied on Webworm-specific claims at the THN-relay layer. ESET grade A (ratified 2026-05-07 per `finding-2026-05-07-0004` APT37 Birdcall Android research) remains unchanged. This entry is logged for traceability of additional supporting citation, NOT as a grade revision proposal.
**Supporting findings:** [finding-2026-05-20-0004]
**Action this run:** No change to `source-grades.yaml`. ESET grade A (ratified) holds.
**Follow-on flag:** Direct welivesecurity.com retrieval pending — collector to attempt on next sweep targeting the Webworm / EchoCreep / GraphWorm research URL. Once retrieved, single-source veto on finding-0004 mechanism layer may relax (still subject to second-vendor corroboration from Mandiant / CrowdStrike / Unit 42 / MSTIC / Symantec / Cisco Talos).

---

## 2026-05-20 — Symantec (Threat Hunter Team / Carbon Black) — A (provisional, awaiting ratification) — additional supporting citation noted

**Type:** Citation note (no grade change)
**Source ID:** `symantec`
**Reason:** `finding-2026-05-20-0004` (Webworm) references Symantec's prior baseline tracking of Webworm as "active since at least 2022" per ESET-via-THN citation. Symantec's own attribution work is not the originating primary for the 2026-05-20 EchoCreep + GraphWorm finding (ESET is) — the Symantec citation is historical-baseline context. Symantec provisional A (since 2026-05-13 first surface on MuddyWater / Seedworm research; 72h ratification clock expired 2026-05-16T18:25:00-04:00) remains in `awaiting_ratification: true` state. This entry is logged for traceability of the cross-cited historical-baseline citation, NOT as a grade revision proposal.
**Supporting findings:** [finding-2026-05-20-0004] (citation only; not originating primary)
**Action this run:** No change to `source-grades.yaml`. Symantec provisional A (awaiting ratification) holds.
**Follow-on flag:** Symantec 72h ratification clock expired 2026-05-16; entry remains `awaiting_ratification: true` past clock. Per source-grade-log.md template and INTEL-GRADING.md doctrine, expired ratification clocks do NOT auto-ratify nor auto-revert — operator decision still pending. Recommend bundling Symantec ratification with cisco-psirt + aonan-guan in the 2026-05-27 ratification window.

---

## 2026-05-28 — Arctic Wolf (Labs / IR research) — (none) → B (provisional, awaiting ratification)

**Type:** New source — provisional
**Source ID:** `arctic-wolf`
**Reason:** First Archimedes-corpus citation as the originating source on `finding-2026-05-28-FLASH-1200-0001` (CVE-2026-35616 FortiClient Endpoint Management Server fresh post-patch exploitation observed May 2026 — pre-auth API access bypass to privilege escalation, CVSS 9.1, Fortinet patched in 7.4.7 early April 2026; attackers weaponize EMS management pipeline to push malicious PowerShell to managed endpoints; payload `FortiEndpoint_Patch.exe` named EKZ Infostealer by Arctic Wolf; exfil to 83.138.53.110). Sole originating vendor — SecurityWeek and The Hacker News both relay Arctic Wolf with no independent observations (single-source veto applied on exploitation-observation layer; WEP capped at "likely" on that layer pending independent telemetry from Mandiant / CrowdStrike / Unit 42 / MSTIC / Microsoft Defender / Fortinet PSIRT / any non-Arctic-Wolf vendor naming the IOC pair). Arctic Wolf is a Tier-2 vendor IR / security operations firm with named-research-team output and an established managed-detection-and-response practice. Proposed grade B by the grader as the conservative starting grade per the vendor-IR-research-firm category precedent (peer class: StepSecurity B 2026-05-12, Socket B 2026-05-14, Sysdig B 2026-05-14, Zellic B 2026-05-14, Ox Security B 2026-05-15, Upwind B 2026-05-15). Operator may upgrade to A on subsequent surfaces showing consistent technical rigor across additional vendor-IR investigations — particularly if Arctic Wolf telemetry coordinates with Tier-1 vendor research (Mandiant / CrowdStrike / Unit 42 / MSTIC) on shared campaigns — or hold at B if context-thin commercial-research profile is observed across more findings.
**Methodological positive on first surface:** Source makes NO threat-actor / nation-state attribution on the FortiClient EMS campaign; SecurityWeek and The Hacker News relays both preserve this attribution-absence verbatim. Hard Rule 2 compliance.
**Trigger-1 fit caveat (carry-forward from finding / brief):** Arctic Wolf's provisional B (not A) creates a procedural marginal fit against FLASH Trigger 1's "A-grade source attesting active exploitation" spec. Disposition is defensible because the substantive threshold — critical CVE plus active exploitation observed by a credible vendor IR firm — is met; the procedural source-grade letter is a half-step below A. Operator may consider re-baselining Trigger 1 wording in a future FLASH-POLICY review if B-grade vendor-IR firms (Arctic Wolf, ReliaQuest, Huntress, Expel) become routine FLASH first-surfaces.
**Supporting findings:** [finding-2026-05-28-FLASH-1200-0001]
**Posted to:** Not posted to Discord `#actor-review` this run — bundled ratification per established precedent (provisional B is not a downgrade requiring human review per Hard Rule 5 / RETRACTION-POLICY adjacent governance).
**Reviewer:** Awaiting Ryan ratification via `/approve-source-grade arctic-wolf B` (or operator upgrade to A / hold at C).
**Provisional flag set:** `provisional: true`, `awaiting_ratification: true` in `infrastructure/source-grades.yaml`.
**Effect on referencing finding:** `finding-2026-05-28-FLASH-1200-0001` cluster anchor is B2 / WEP "likely" with single-source-veto active on the exploitation-observation layer; CVE record + April patch availability sit at A1 procedural fact (independent of Arctic Wolf grade). Operator upgrade of Arctic Wolf to A would re-grade the exploitation-observation layer to A2 on subsequent surfaces but would NOT lift single-source-veto on this finding (the veto rests on Arctic Wolf being the sole originating vendor regardless of grade — independence requires a second vendor's primary observation).
**72h ratification clock:** 2026-05-31T12:35:00-04:00 (72h from FLASH composition). Per established vendor-IR-research-firm precedent class.
**Next review:** ratification target 2026-06-04 (7 days; bundled with the open cisco-psirt / aonan-guan / Symantec / Bitdefender / litespeed / github-blog ratification window).

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
