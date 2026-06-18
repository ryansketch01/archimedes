---
raw_id: raw-2026-06-18-am-010-hns-pogorelec-eset-gentlemen-gentlekiller-edr-killer-framework
collected_at: 2026-06-18T07:48:00-04:00
run_id: pre-brief-20260618-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: helpnetsecurity
  source_name: Help Net Security (Anamarija Pogorelec)
  source_url: https://www.helpnetsecurity.com/2026/06/18/eset-gentlemen-edr-killers/
  published_at: 2026-06-18T05:00:58-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [Gentlemen, ransomware, RaaS, GentleKiller, EDR, ESET, HexKiller, ThrottleBlood, HavocKiller, Warlock, MedusaLocker, DragonForce, Qilin, RansomHub, "BYOVD"]
triage_tags: [ransomware_research, edr_killer_tooling_layer, single_ir_vendor_eset, ad_indirect, operator_deferred_new_actor_candidate_substrate_strengthening, anti_noise_check_against_reject_2026_06_17_0007, hard_rule_2_binding]
iocs_extracted: false
iocs_count: 0
text_word_count: 800
promoted: false
rejected_at: 2026-06-18T08:25:00-04:00
rejection_id: reject-2026-06-18-0008
ttl_expires_at: 2026-09-16T07:48:00-04:00
---

# GentleKiller targets more than 400 security processes across 48 products (HNS-Pogorelec relay of ESET primary)

**Publisher:** Help Net Security (Anamarija Pogorelec byline)
**Published:** 2026-06-18T05:00 EDT
**URL:** https://www.helpnetsecurity.com/2026/06/18/eset-gentlemen-edr-killers/

## Article body summary

ESET researchers (Jakub Souček byline on the underlying ESET research) detailed the Gentlemen ransomware-as-a-service operation's GentleKiller framework targeting over 400 security processes across 48 vendor products. Unlike most ransomware gangs that delegate defense-disabling work to affiliates, Gentlemen actively develops and maintains a portfolio of EDR killers, providing them directly to ransomware affiliates that rent the gang's encryptors. The model lowers the barrier to entry for attackers seeking to neutralize enterprise endpoint security.

The analysis drew insights from an **internal data breach Gentlemen suffered in May 2026**, which confirmed the group's business model and exposed leadership discussions about EDR-killer distribution. Gentlemen emerged in late 2025 and rapidly established itself as one of the five most active ransomware operations by Q1 2026, offering affiliates 90% of ransom proceeds. Group-IB traced the operation's founding to **a former Qilin affiliate**, with the gang practicing double extortion.

### Key Technical Components

**GentleKiller framework**: The core toolkit exists in at least eight variants, each impersonating legitimate security products while leveraging vulnerable or malicious kernel drivers. ESET researcher Jakub Souček: "The leak allowed us to confirm the hypothesis we formed in February 2026: that Gentlemen operators actively develop and maintain a portfolio of EDR killers."

The variants share consistent code patterns including process-killing loops operating on timers and identical obfuscation techniques, indicating reused development templates. The framework swiftly adapts to newly published Bring Your Own Vulnerable Driver (BYOVD) proofs-of-concept, with operators integrating UnknownKiller and PoisonKiller within days of public disclosure.

**External tools integration**: The suite incorporates three acquired tools:
- **HexKiller** (previously linked to Warlock)
- **ThrottleBlood** (appeared in MedusaLocker and DragonForce intrusions)
- **HavocKiller** (publicly surfaced March 19, 2026, but ESET telemetry shows usage from January 23, 2026)

**Evasion mechanisms**: All tools employ standardized vendor disguises with filenames mimicking legitimate security companies, fabricated version information, invalid digital signatures from legitimate software, and stolen product icons. Many samples receive commercial packing via Enigma or Themida.

### Targeting Profile

Gentlemen's victim distribution differs from typical top-tier ransomware gangs, concentrating in Southeast Asia, South America, and Western Europe rather than primarily the United States. Targets span countries including Thailand, Brazil, and France. Victim selection criteria center on **FortiGate firewall configurations**, with operators sorting candidates centrally before assigning them to affiliates.

### Operational Implications

The research demonstrates how Gentlemen's in-house development model distinguishes it from competitors like RansomHub, which previously built single EDR killers for affiliates. By maintaining a varied portfolio blending original code with adapted public research, Gentlemen provides ready-to-use defense-circumvention capabilities that reduce technical barriers for affiliate operations. The shared vendor disguises across tools complicate attribution when individual samples are encountered independently.

NO A&D-prime named victims in ESET's reporting.

---

## Extraction notes

- Language: en
- Publisher byline: Anamarija Pogorelec (Help Net Security)
- Article type: trade-press IR-vendor-research relay (ESET primary)
- Substrate role: HNS-Pogorelec is the SECOND-publisher relay (after HNS-Pogorelec PRIOR coverage 2026-06-17 18:00 sweep) of ESET's primary research on Gentlemen / GentleKiller. ESET-primary single-IR-vendor on actor-identity + EDR-killer-tooling-supply layer. NOT lifted to independent IR-vendor corroboration by Mandiant / CrowdStrike / Unit-42 / MSTIC. Operator-deferred /new-actor-Gentlemen candidacy carry-forward (operator-deferred from reject-2026-06-17-0007 PM brief).
- Substrate-strengthening THIS SWEEP: net-new technical depth on GentleKiller variant count (at least 8), BYOVD integration cadence ("within days of public disclosure"), acquired-tooling list (HexKiller / ThrottleBlood / HavocKiller), Group-IB attributed founding lineage to former Qilin affiliate, FortiGate-config-driven victim sorting pattern, May 2026 internal data leak from the gang itself. This is meaningful net-new substrate beyond 2026-06-17 PM brief reject substrate.
- T-gates evaluation: T1/T6 FAIL no CVE; T2 FAIL Gentlemen NOT on _roster.yaml; T4 FAIL not a tracked-actor-TTP-change (this is a new-actor TTP characterization); T5 FAIL no specific A&D-prime named victim; supply-chain via affiliate ecosystem rather than direct campaign-active. Critical-override 0-of-4 — non-FLASH-eligible.
- A&D-relevance: HIGH-indirect. FortiGate-config-driven victim sorting overlaps with FortiBleed substrate (finding-2026-06-17-0002) suggesting potential operational adjacency between FortiBleed credential dataset and Gentlemen affiliate targeting (carry-forward speculation only — NOT cross-walked at this surface). EDR-killer-tooling layer is broadly relevant to A&D defender-side endpoint posture.
- Possible morning brief Other Signal one-liner: EDR-killer-tooling-supply model + 90% affiliate cut + 5-most-active-Q1-2026 ransomware ranking + ~50% Gentlemen / Qilin organizational lineage per Group-IB.
- Attribution discipline: ESET attribution to "Gentlemen" as the ransomware-as-a-service gang preserved verbatim. Group-IB attribution to "former Qilin affiliate" preserved verbatim. Hard Rule 2 BINDING — do NOT cross-walk to Qilin dossier without independent A-grade source making the actor-identity attribution.
- Quote-budget for morning brief: Souček "Gentlemen operators actively develop and maintain a portfolio of EDR killers" 9-word at-cap option (best). NO other ESET-named at-cap quotes surfaced in body.
- IOC extraction: 8 GentleKiller variant + 3 acquired-tool name strings are tool-name-level only, not concrete IOC values. ESET technical primary likely contains hashes / driver names / signature subjects — body retrieval next-cycle priority IF substrate strengthens.
