---
raw_id: raw-2026-06-19-pm-001
collected_at: 2026-06-19T15:33:00-04:00
run_id: pre-brief-20260619-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: thehackernews
  source_name: The Hacker News
  source_url: https://thehackernews.com/2026/06/the-gentlemen-raas-uses-gentlekiller.html
  published_at: 2026-06-19T18:33:07+00:00
match_reason:
  watchlist: [ransomware, edr-killer-tooling]
  actors: []
  vulnerabilities: []
  keywords: [Gentlemen, GentleKiller, EDR killer, BYOVD, ransomware-as-a-service, ESET, Qilin, Yapaev, hastalamuerte, PoisonX.sys, OxideHarvest, HexKiller, ThrottleBlood, HavocKiller, HwAudKiller]
triage_tags: [substrate_strengthening, operator_deferred_new_actor, non_flash, third_publisher_relay, edr_killer_tooling_layer]
iocs_extracted: false
iocs_count: 0
text_word_count: 450
promoted: false
rejected_at: 2026-06-19T16:14:00-04:00
rejection_id: reject-2026-06-19-0004
ttl_expires_at: 2026-09-17T15:33:00-04:00
---

# THN-Lakshmanan: The Gentlemen RaaS Uses GentleKiller EDR Framework Targeting 400 Security Processes

**Source:** The Hacker News (THN) — Ravie Lakshmanan byline
**Published:** 2026-06-19 18:33:07 UTC (~14:33 EDT, within ~1h of this collection sweep)
**URL:** https://thehackernews.com/2026/06/the-gentlemen-raas-uses-gentlekiller.html

## Why captured

Substrate-strengthening signal on **operator-deferred /new-actor Gentlemen candidacy** (carried forward from reject-2026-06-17-0007 + AM raw-2026-06-18-am-010 + reject-2026-06-18-0008 + FLASH-0000 raw-2026-06-19-flash-0000-001 BC-Toulas second-publisher relay).

This is the **THIRD-publisher relay** on ESET-Souček primary research from 2026-06-18 — widening publisher-independence on the EDR-killer-tooling-supply layer from **BC-Toulas + ESET-primary** to **BC-Toulas + THN-Lakshmanan + ESET-primary**.

**Important per Hard Rule 2:** Single-IR-vendor-on-actor-identity-and-tooling-layer veto **persists** — second-IR-vendor-on-actor-identity corroboration from Mandiant/CrowdStrike/Unit-42/MSTIC remains the substrate-that-would-lift-veto. THN is a journalistic second-publisher relay on ESET-primary, NOT a second IR-vendor channel.

## Key content (≤15-word quote ceiling enforced per Hard Rule 6)

- THN attributes Gentlemen RaaS framework to ESET researcher Jakub Souček as primary research source.
- **GentleKiller toolkit (8 EDR-killer variants):** Kaspersky, FACEIT Anti-Cheat, Valorant, Javelin, WatchDog, Network Blocker, Cleaner, G11 — all impersonating legitimate security/anti-cheat products.
- **Technique class:** BYOVD (bring-your-own-vulnerable-driver) — PoisonX.sys exploitation noted (BYOVD previously used against CrowdStrike Falcon).
- **Process targeting scope:** ESET via THN — "looks for 400 processes associated with 48 distinct security programs" (13-word at-cap quote candidate per Hard Rule 6).
- **Third-party EDR-killers integrated into Gentlemen toolkit:** HexKiller, ThrottleBlood, HavocKiller/HwAudKiller (this last is named differently in BC-Toulas FLASH-0000 raw signal — possible naming variant or distinct tool, defer to ESET-primary for canonical naming).
- **UEFI Secure Boot bypass vulnerabilities disclosed** affecting Acer, AMD, ASUS, ECS, Getac, GIGABYTE, Toshiba, Uniwill — vendor-cluster substrate-strengthening on BYOVD layer.
- **OxideHarvest:** Rust-based credential stealer (Chrome, Edge, Firefox, Brave, Opera variants) — adjacent infrastructure, externally developed per BC-Toulas.
- **Leadership attribution (preserved verbatim per ESET):** "Alexander Andreevich Yapaev (36, Russian national; alias: hastalamuerte), previously affiliated with Qilin ransomware" — Hard Rule 2 BINDING, NOT cross-walked to APT roster.
- **Geographic distribution claim:** ESET via THN — "Southeast Asia, South America, and Western Europe" with 504 claimed victims total. No A&D-prime, no defense-contractor, no DIB-supplier, no government-agency named victims.

## Attribution per Hard Rule 2

- **Gentlemen RaaS:** Standalone actor identity preserved per ESET primary research. NOT on _roster.yaml. Operator-deferred /new-actor candidacy continues. NOT cross-walked to APT28/29/Sandworm/Lazarus/Volt Typhoon/UNC1549/Charming Kitten/APT41/Salt Typhoon/Scattered Spider/Cl0p/LockBit/REvil/BlackCat.
- **Alexander Andreevich Yapaev / hastalamuerte:** Named alleged-leadership-figure-name per ESET research — preserved verbatim. NOT cross-walked.
- **Qilin ransomware affiliation:** Preserved per ESET research as prior-affiliation-claim. Qilin is on _roster.yaml watch-pattern but NOT a tracked roster actor (no Qilin dossier). NOT cross-walked.

## T-gate evaluation (FLASH eligibility)

- **T1 critical-CVE-exploited:** NO. No specific CVE assigned to GentleKiller variants. UEFI Secure Boot bypass CVEs are pre-existing and vendor-disclosed; PoisonX.sys exploitation is BYOVD pattern not CVE-specific.
- **T2 tracked-actor-attribution:** **NO.** Gentlemen is NOT on _roster.yaml. Yapaev / hastalamuerte / Qilin-affiliation claims preserved per ESET — NOT cross-walked per Hard Rule 2 BINDING.
- **T3 first-party-IOC-hit:** **NO.** Splunk sentinel clean this sweep (28th consecutive). No IOCs in this article body specific enough for Splunk sweep — process-target names + tooling names + UEFI-bypass CVEs are not network IOCs.
- **T4 tracked-actor-TTP-change:** N/A — no tracked actor; Gentlemen is operator-deferred /new-actor candidate, not tracked.
- **T5 A&D-sector-campaign:** **NO.** No A&D-prime named victim, no defense-contractor named, no DIB-supplier named, no government-agency named. Geographic distribution claim is sector-agnostic (Southeast Asia / South America / Western Europe broad). Romanian energy provider Oltenia from BC-Toulas FLASH-0000 raw signal is NOT A&D-prime (energy sector).
- **T6 zero-day-no-patch:** **NO.** No 0-day disclosure; BYOVD pattern uses already-disclosed vulnerable drivers. UEFI Secure Boot vendor cluster has patches available (multi-vendor).

**Critical-override 0-of-4:** CVSS not 10.0 + no tracked actor + no A&D-prime watchlist entity + Gentlemen attribution NOT crossed to roster per Hard Rule 2 BINDING.

## Substrate handoff to grader / PM-brief composition

- **NOT a FLASH candidate this sweep.** T-gates fail across all six triggers.
- **Substrate-strengthening on operator-deferred /new-actor Gentlemen candidacy.** Triple-publisher status (ESET-primary + BC-Toulas + THN-Lakshmanan) widens publisher-independence layer materially.
- **Single-IR-vendor-on-actor-identity-and-tooling-layer veto STILL PERSISTS.** Mandiant / CrowdStrike / Unit-42 / MSTIC second-IR-vendor-on-actor-identity corroboration of Gentlemen-actor-identity / GentleKiller-tooling-layer / Yapaev-leadership-attribution remains the substrate-that-would-lift-veto. THN is a journalistic relay on ESET-primary, NOT a second IR-vendor channel.
- **Possible afternoon-brief Other-Signal one-liner candidate** IF substrate-pivot absorbed into PM lift on EDR-killer-tooling-supply-pattern layer. Briefer / grader decision per INTEL-BRIEF-STANDARDS.md anti-repetition rules and INTEL-GRADING.md promotion checklist.

## IOC extraction notes

- **Language:** en
- **Publisher byline:** Ravie Lakshmanan (THN-Lakshmanan)
- **Article type:** blog
- **Raw IOC extraction invoked:** no (no network IOCs in article — only process-target names + tooling names + UEFI vendor cluster + leadership-figure-name + 504-claimed-victims-count + 400-process-target-count + 48-vendor-product-count)
- **Substrate IOC notes:** ESET-primary GentleKiller research at security-side ESET-source may carry hash/IP/domain IOCs not surfaced in THN journalistic relay; ESET-primary URL retrieval deferred to operator-discretion (Symantec-enterprise-blogs.security.com DNS resolution failure this sweep precludes direct alt-IR-vendor primary retrieval as substrate-strengthening cross-check)
