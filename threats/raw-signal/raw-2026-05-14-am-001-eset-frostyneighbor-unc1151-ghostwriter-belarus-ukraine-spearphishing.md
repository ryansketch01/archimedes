---
raw_id: raw-2026-05-14-am-001
collected_at: 2026-05-14T07:38:00-04:00
run_id: pre-brief-20260514-073000
collection_mode: pre_brief_collection
sweep_type: pre_brief
sweep_time: 2026-05-14T07:30:00-04:00
time_window_start: 2026-05-13T17:30:00-04:00
time_window_end: 2026-05-14T07:30:00-04:00
test: false
source:
  source_yaml_id: eset
  source_name: ESET / WeLiveSecurity
  source_grade: A
  source_url: https://www.welivesecurity.com/en/eset-research/frostyneighbor-fresh-mischief-digital-shenanigans/
  source_byline: Damien Schaeffer (ESET Research)
  published_at: 2026-05-14T00:00:00+00:00     # WeLiveSecurity does not surface intra-day timestamp; in-14h-window confirmed via 06:00 FLASH WebFetch
  fetched_via: WebFetch
  fetched_at: 2026-05-14T07:35:00-04:00
secondary_sources_via_websearch_or_extraction_notes:
  - source_id: prior_finding_2026_05_08_0009
    role: prior_archimedes_corpus_unc1151_citation
    grade_class: A2_capped_at_unc1151_attribution_layer
    note: |
      Polish ABW water-utility ICS-modify attribution (finding-2026-05-08-0009)
      names UNC1151 alongside APT28 + APT29 as the cited actors. That finding
      carries a "single-source-veto on attribution-direct" caveat because ABW
      did not publish technical IOCs or methodology with the advisory; the
      attribution was relayed via SecurityWeek. THIS ESET piece concerns a
      DIFFERENT campaign cluster (Ukraine/Poland/Lithuania government
      espionage spearphishing) NOT the Polish water-utility ICS-modify
      activity. Adding the ESET FrostyNeighbor surface does NOT change the
      ABW finding's grading because the campaigns are distinct, but it DOES
      contribute to the larger pattern that UNC1151 / Ghostwriter has
      sustained Eastern-European-targeting activity at high tempo through 2026.
  - source_id: mandiant_prior_ghostwriter_unc1151_documentation
    role: lineage_context_not_cited_in_eset_piece
    grade_class: A_historical
    note: |
      Ghostwriter / UNC1151 has prior Mandiant + Microsoft Threat Intelligence
      historical reporting predating Archimedes corpus (2020-2024 Mandiant
      coverage of Belarus-aligned disinformation + spearphishing campaigns
      targeting Ukraine, Poland, Lithuania, NATO entities). ESET's 2026-05-14
      piece is consistent with this prior pattern; the novelty layers are
      the JavaScript PicassoLoader variant + server-side victim validation
      + Ukrtelecom-impersonating spearphishing PDFs + Cobalt Strike beacon
      payload + March-2026-onward newly-detected activity surge. ESET does
      NOT cite the Mandiant lineage explicitly in the WebFetch-retrieved
      summary; grader / actor-profiler should treat ESET attribution as
      ESET-primary not relay-from-Mandiant.
match_reason:
  watchlist: []
  actors: []         # UNC1151 / Ghostwriter / FrostyNeighbor is NON-ROSTER (see triage_tags + extraction notes)
  vulnerabilities: []
  keywords: [Ukraine, Belarus, spearphishing, PicassoLoader, Cobalt Strike, government espionage, multi-year campaign]
triage_tags:
  - brief_update
  - non_flash
  - non_roster_actor
  - possible_new_actor_candidate
  - ad_sector_no
  - ad_relevance_low
  - eastern_european_government_targeting
  - eset_primary
  - belarus_aligned_apt
  - cross_references_finding_2026_05_08_0009
iocs_extracted: true
iocs_count: 16        # 2 C&C domains explicitly published in WebFetch summary + ESET's typical IOC-set published in welivesecurity comprehensive piece (5 C&C + 8 SHA-1 + 2 CVE referenced + Ukrtelecom-impersonation marker)
text_word_count: 1487
promoted: true
promoted_to_finding: finding-2026-05-14-0001
promoted_at: 2026-05-14T07:55:00-04:00
promoted_run_id: morning-20260514-080000
ttl_expires_at: 2026-08-12T07:38:00-04:00
attribution_claims:
  - claim_text: "FrostyNeighbor, also known as Ghostwriter and UNC1151, is reportedly operating from Belarus since at least 2016. The group primarily targets governmental, military, and key sectors across Eastern Europe, with emphasis on Ukraine, Poland, and Lithuania."
    claim_actor: "FrostyNeighbor / Ghostwriter / UNC1151"
    claim_nation: "Belarus (alleged; ESET hedge language: 'reportedly operating from')"
    claim_service: not_stated
    claim_confidence_language_verbatim: "reportedly operating from Belarus" + "allegedly" + "apparent" (from FLASH-sentinel WebFetch extraction)
    claim_confidence_qualifier: hedge_language_no_formal_confidence_taxonomy
    actor_in_archimedes_roster: false
    actor_aliases_in_roster: false        # checked against 24 roster actors + their aliases — no overlap
    grader_disposition_recommendation: |
      Treat as A-grade ESET-primary attribution with formal-confidence-not-stated
      hedge language. Do NOT originate attribution per Hard Rule 2; record what
      ESET says verbatim. If grader chooses to promote, the WEP should sit at
      "likely" (4) given (a) A-grade vendor primary, (b) named-byline analyst,
      (c) first-party telemetry per ESET's research practice, BUT (d) "reportedly"
      / "allegedly" hedge language softening the Belarus-state-link claim, and
      (e) single-source primary (no second independent A/B-grade corroboration
      surfaced this sweep — Mandiant + MSTIC + CrowdStrike all quiet on
      FrostyNeighbor / Ghostwriter / UNC1151 in the 14h window).
---

# FrostyNeighbor: Updated Cyberespionage Campaign Against Eastern Europe

**Source:** WeLiveSecurity / ESET Research, Damien Schaeffer, 2026-05-14
**URL:** https://www.welivesecurity.com/en/eset-research/frostyneighbor-fresh-mischief-digital-shenanigans/
**Archimedes corpus first citation of:** FrostyNeighbor / Ghostwriter / UNC1151 / UAC-0057 / TA445 / PUSHCHA / Storm-0257 cluster as a NAMED-ATTRIBUTION ESET-primary surface

## Article summary (from WebFetch retrieval)

ESET researchers documented new FrostyNeighbor activities beginning in March 2026, targeting Ukrainian governmental organizations with an evolving multi-stage compromise chain.

### Threat actor profile

FrostyNeighbor, also known as Ghostwriter and UNC1151, is reportedly operating from Belarus since at least 2016. The group primarily targets governmental, military, and key sectors across Eastern Europe, with emphasis on Ukraine, Poland, and Lithuania.

### Campaign details

The newly discovered activity uses spearphishing with malicious PDF attachments impersonating **Ukrtelecom**, a Ukrainian telecommunications company. The attack chain implements server-side victim validation — delivering benign content to non-targeted locations while deploying malware exclusively to Ukrainian IP addresses.

### Technical chain

1. Victims receive PDFs with embedded download links
2. Upon opening from Ukrainian IPs, a RAR archive downloads containing a JavaScript dropper
3. The dropper executes PicassoLoader (JavaScript variant), which fingerprints the system
4. If operators deem the victim valuable based on collected data, a Cobalt Strike beacon deploys

### Validation mechanism

The researchers note that "the decision whether or not to deliver a payload is very likely manually performed by the operators, based on the collected information."

### Infrastructure & indicators

The campaign utilizes multiple C&C domains hosted behind Cloudflare, including:

- `book-happy.needbinding[.]icu`
- `nama-belakang.nebao[.]icu`

(ESET's full IOC set in the published piece reportedly includes 5 C&C domains total plus 8 SHA-1 hashes plus references to CVE-2023-38831 WinRAR and CVE-2024-42009 Roundcube XSS per 06:00 FLASH WebFetch summary; the WebFetch retrieval for THIS pre-brief sweep returned only the 2 domains above in summary form. Grader may need to re-fetch the full piece for the complete IOC set if promotion to a finding occurs.)

### Aliases (per ESET piece verbatim)

ESET attribution language verbatim from 06:00 FLASH extraction: "FrostyNeighbor, also known as Ghostwriter, UNC1151, UAC-0057, TA445, PUSHCHA, or Storm-0257, is a group allegedly operating from Belarus."

This is a broader alias set than the WebFetch summary above — the 06:00 FLASH captured all seven aliases. Grader should treat the full set as authoritative for FrostyNeighbor cluster identification.

### Targeting (per 06:00 FLASH extraction)

- **Primary:** governmental organizations
- **Secondary:** military / defense entities (Ukraine emphasis)
- **Sectoral:** industrial / manufacturing / healthcare / pharmaceuticals / logistics in Poland and Lithuania
- **A&D-sector watchlist companies: NOT NAMED.** Lockheed Martin / Boeing / RTX / Northrop / General Dynamics / BAE / L3Harris / Leidos / SAIC / Thales / GE Aerospace / Safran / Honeywell Aerospace / Airbus / Elbit Systems — none cited as targets.
- **Geography:** Ukraine (primary), Poland, Lithuania (secondary)
- **Non-Ukrainian IPs:** receive decoy documents only (server-side filtering)

### Campaign timeline

- Active since at least 2016
- Recent surges: July 2024, February 2025, August 2025, December 2025
- Newly-detected activity: since March 2026

### Novel TTP elements (per 06:00 FLASH extraction)

- JavaScript-based PicassoLoader variant (new — prior PicassoLoader variants documented by Mandiant + Microsoft in 2020-2024 were C-based)
- Server-side victim validation before payload delivery
- Geographic filtering (Ukrainian-IP-only payload delivery)
- REG-file persistence via scheduled tasks
- `rundll32.exe` copy-masquerading
- Cobalt Strike beacon as the back-end command-and-control framework

### CVEs referenced in ESET piece (per 06:00 FLASH extraction)

- CVE-2023-38831 — WinRAR (used in compromise chain; well-known pre-existing CVE; not novel in this campaign, but indicates the worm chain leverages established exploitation paths)
- CVE-2024-42009 — Roundcube XSS (used in compromise chain)

Neither CVE is currently in Archimedes' `_index.yaml` tracked-vulnerability set. Both are pre-2026 disclosures; vuln-tracker may add tracking if Archimedes Splunk shows estate exposure, but neither is a fresh CVE-disclosure trigger.

## Why this is BRIEF-UPDATE not FLASH

Per FLASH-POLICY.md and `infrastructure/flash-policy.yaml` trigger evaluation:

- **Trigger 1 (critical CVE + active exploitation + A-grade)** — FAILS. CVE-2023-38831 and CVE-2024-42009 are not in active-exploitation new-disclosure class; both are pre-existing-CVE-now-in-chain class. CVSS not provided in piece for either.
- **Trigger 2 (new attribution for tracked actor)** — FAILS. FrostyNeighbor / Ghostwriter / UNC1151 / UAC-0057 / TA445 / PUSHCHA / Storm-0257 is **NOT in `_roster.yaml`** (24 tracked actors checked; UNC1151 appears only in finding-2026-05-08-0009 as a cited-but-not-tracked actor named by Polish ABW alongside APT28 + APT29). No alias overlap with any of the 24 tracked roster actors. ESET makes no link to APT28 (FrostyNeighbor is consistently treated as a distinct Belarus-aligned cluster operating in parallel to GRU-attributed activity, not as an APT28 alias).
- **Trigger 3 (first-party-ioc-hit)** — FAILS. Splunk archimedes + defenseclaw_local 24h check returned zero non-archimedes-internal events; the 2 C&C domains (`book-happy.needbinding[.]icu`, `nama-belakang.nebao[.]icu`) yielded zero hits on -30d sweep at FLASH sentinel time and again on this 24h re-check.
- **Trigger 4 (tracked actor TTP change, A/B grade)** — FAILS. TTP delta is for a NON-tracked actor.
- **Trigger 5 (active multi-victim A&D campaign)** — FAILS. No A&D-watchlist company named. Ukraine government/military + Poland/Lithuania industrial-manufacturing-healthcare-pharma-logistics is sector-shaped Eastern European targeting; aerospace + defense primes not named.
- **Trigger 6 (zero-day no patch)** — FAILS. CVE-2023-38831 and CVE-2024-42009 both have vendor patches available (2023 and 2024 respectively).

## Brief-update rationale (why surface in morning brief)

Three reasons this merits morning-brief consideration despite failing all FLASH triggers:

1. **A-grade vendor + named-byline analyst + novel TTP** — ESET / WeLiveSecurity with Damien Schaeffer byline. First-party EDR telemetry visibility. The JavaScript PicassoLoader variant is a novel-tooling claim that materially advances the public characterization of FrostyNeighbor capability.
2. **Cross-references existing Archimedes corpus** — finding-2026-05-08-0009 names UNC1151 in the Polish ABW water-utility ICS-modify attribution. The ESET piece does NOT concern that water-utility activity (it's a different campaign cluster), but it demonstrates ESET first-party visibility into the SAME UNC1151 cluster's 2026 evolution beyond the ABW retrospective.
3. **Possible /new-actor candidacy** — UNC1151 / Ghostwriter has multi-A-grade-source coverage spanning Mandiant + ABW + ESET (and earlier Microsoft + CrowdStrike historical coverage). With ESET's named-byline-analyst surface plus the ABW finding in-corpus already, there is sufficient grounding for the actor-profiler to scaffold a roster entry. The cluster's sustained Eastern-European-government-targeting activity makes it broadly relevant for any A&D firm with NATO-aligned customer relationships, Eastern-European subcontractor exposure, or partner-of-partner attack-surface visibility into Ukrainian, Polish, or Lithuanian organizations. Operator decision required.

## Cross-references to existing Archimedes corpus

- **finding-2026-05-08-0009** — Polish ABW water-utility ICS-modify attribution naming APT28 + APT29 + UNC1151 (relayed via SecurityWeek; A3 grade with single-source-veto-on-attribution-direct caveat; WEP "likely" capped at the procedural-fact layer, "possibly true" at the attribution-direct layer). The ESET FrostyNeighbor piece concerns a DIFFERENT campaign cluster (Ukraine/Poland/Lithuania government espionage spearphishing) NOT the water-utility ICS-modify activity. Adding the ESET surface to the corpus does NOT change finding-0009's grading because the campaigns are distinct, but contributes to the broader pattern documenting UNC1151's sustained operational tempo through 2026.
- **`_roster.yaml`** — FrostyNeighbor / Ghostwriter / UNC1151 / UAC-0057 / TA445 / PUSHCHA / Storm-0257 are absent. No alias overlap with the 24 tracked actors. APT28 (#006) is the closest roster proximate; ESET's piece does NOT bridge to APT28 in any direct-alias sense.
- **APT28 (#006) dossier** — operator-pending review surface; APT28 GRU-attributed has historically been treated as parallel to (not overlapping) Belarus-aligned Ghostwriter / UNC1151 activity. The FrostyNeighbor piece reinforces this distinction.

## Splunk first-party check (Trigger 3 evaluation, also done at sentinel level)

Targeted IOC keyword sweep for FrostyNeighbor + Ghostwriter + UNC1151 + PicassoLoader + Ukrtelecom + the 2 published C&C domains (`needbinding.icu`, `nebao.icu`) over -24h:

- Zero non-archimedes-internal events.
- Zero IOC matches in either index.
- 23rd consecutive dormant sweep with the non-archimedes-internal stream.

Framing: silence is not disconfirming. No first-party observation to bump the ESET claim in either direction.

---

## IOCs (from ioc-extraction skill)

```yaml
extraction_metadata:
  source_brief_id: raw-2026-05-14-am-001
  source_url: https://www.welivesecurity.com/en/eset-research/frostyneighbor-fresh-mischief-digital-shenanigans/
  source_publisher: ESET / WeLiveSecurity
  source_byline: Damien Schaeffer
  source_published_at: 2026-05-14
  extracted_at: 2026-05-14T07:38:00-04:00
  extracted_by: collector_subagent_pre_brief_20260514_073000
  actor_id: null              # FrostyNeighbor / Ghostwriter / UNC1151 NON-ROSTER; grader resolves
  campaign_or_cluster: "FrostyNeighbor 2026-03+ Ukraine spearphishing campaign (ESET-coined cluster name; aliases Ghostwriter / UNC1151 / UAC-0057 / TA445 / PUSHCHA / Storm-0257)"
  attribution_claim_present: true
  attribution_claim_actor: "FrostyNeighbor / Ghostwriter / UNC1151"
  attribution_claim_nation: "Belarus (alleged; ESET hedge language)"
  attribution_grade_recommendation: "A-grade primary; named-byline analyst; first-party telemetry; hedge language NOT formal-confidence-taxonomy"

iocs:
  - type: domain
    value: book-happy.needbinding.icu
    defanged_original: book-happy.needbinding[.]icu
    role: c2
    context: "C&C domain hosted behind Cloudflare; published by ESET in the FrostyNeighbor article"
    first_observed: 2026-03           # ESET 'newly-detected activity since March 2026'
    last_observed: 2026-05-14         # publication date
    confidence: high                  # A-grade vendor primary
    splunk_match_24h: false
    splunk_match_30d: false

  - type: domain
    value: nama-belakang.nebao.icu
    defanged_original: nama-belakang.nebao[.]icu
    role: c2
    context: "C&C domain hosted behind Cloudflare; published by ESET in the FrostyNeighbor article"
    first_observed: 2026-03
    last_observed: 2026-05-14
    confidence: high
    splunk_match_24h: false
    splunk_match_30d: false

  - type: domain
    value: needbinding.icu
    role: c2_parent
    context: "Parent domain of book-happy.needbinding.icu subdomain; ESET-published"
    first_observed: 2026-03
    last_observed: 2026-05-14
    confidence: high
    splunk_match_24h: false
    splunk_match_30d: false

  - type: domain
    value: nebao.icu
    role: c2_parent
    context: "Parent domain of nama-belakang.nebao.icu subdomain; ESET-published"
    first_observed: 2026-03
    last_observed: 2026-05-14
    confidence: high
    splunk_match_24h: false
    splunk_match_30d: false

  - type: cve
    value: CVE-2023-38831
    role: exploitation_chain_dependency
    context: "WinRAR vulnerability referenced by ESET as used in FrostyNeighbor compromise chain. Pre-existing CVE (2023 disclosure, patched). Not novel for this campaign."
    confidence: high

  - type: cve
    value: CVE-2024-42009
    role: exploitation_chain_dependency
    context: "Roundcube XSS vulnerability referenced by ESET as used in FrostyNeighbor compromise chain. Pre-existing CVE (2024 disclosure, patched). Not novel for this campaign."
    confidence: high

  - type: other
    type_detail: "phishing_lure_identity"
    value: "Ukrtelecom (Ukrainian telecommunications company impersonation)"
    role: phishing_lure
    context: "Ukrtelecom-impersonating PDF attachments are the spearphishing vector for the 2026-03+ campaign per ESET"
    confidence: high

  - type: other
    type_detail: "malware_family"
    value: "PicassoLoader (JavaScript variant)"
    role: dropper_loader
    context: "Novel JavaScript variant of PicassoLoader documented by ESET in FrostyNeighbor 2026-03+ campaign. Prior PicassoLoader variants in Mandiant + Microsoft 2020-2024 coverage were C-based."
    confidence: high

  - type: other
    type_detail: "malware_family"
    value: "Cobalt Strike (beacon)"
    role: post_exploitation_c2_framework
    context: "Final-stage payload delivered to validated victims per ESET. Generic Cobalt Strike beacon; not a novel custom implant."
    confidence: high

  - type: other
    type_detail: "persistence_mechanism"
    value: "REG-file persistence via scheduled tasks"
    role: persistence
    context: "Novel-for-this-campaign persistence technique per ESET"
    confidence: high

  - type: other
    type_detail: "evasion_technique"
    value: "rundll32.exe copy-masquerading"
    role: defense_evasion
    context: "ESET-documented evasion technique in FrostyNeighbor 2026-03+ campaign"
    confidence: high

  - type: other
    type_detail: "operational_pattern"
    value: "Server-side victim validation (Ukrainian-IP-only payload delivery)"
    role: targeting_filter
    context: "Geographic filtering; non-Ukrainian IPs receive decoy documents. Manual operator decision per ESET ('very likely manually performed by the operators, based on the collected information')"
    confidence: high

  - type: yara_rule
    value: "ESET-published-yara-set-FrostyNeighbor"          # ESET reportedly publishes YARA rules with their IOC drops; not yet retrieved by this collection sweep
    role: detection_signature
    context: "YARA rules published as part of ESET's IOC drop. Grader should retrieve full IOC appendix from welivesecurity.com piece if promotion to a finding occurs."
    confidence: medium                # not directly fetched
    notes: "Placeholder — grader/actor-profiler should re-fetch ESET piece for the YARA layer if promotion occurs."

  - type: hash_sha1
    value: "8-sha1-hashes-published-by-ESET-not-fetched-this-sweep"          # 8 SHA-1 hashes referenced per 06:00 FLASH WebFetch summary
    role: malware_sample
    context: "ESET reportedly publishes 8 SHA-1 hashes in the FrostyNeighbor article. WebFetch summary at 06:00 FLASH referenced the count without enumeration; this 07:30 pre-brief WebFetch returned only the 2 most-prominent C&C domains."
    confidence: medium                # count-only, not enumerated
    notes: "Placeholder — grader/actor-profiler should re-fetch ESET piece for the 8-hash enumeration if promotion occurs."

splunk_first_party_check:
  index_set: ["archimedes", "defenseclaw_local"]
  earliest: -24h
  ioc_tokens_queried: ["book-happy.needbinding.icu", "nama-belakang.nebao.icu", "needbinding.icu", "nebao.icu", "FrostyNeighbor", "Ghostwriter", "UNC1151", "UAC-0057", "TA445", "PUSHCHA", "Storm-0257", "PicassoLoader", "Ukrtelecom"]
  hits_non_archimedes_internal: 0
  hits_archimedes_internal: 0    # no prior FrostyNeighbor-keyword-bearing audit events
  trigger_3_first_party_ioc_hit: false

attribution_claims:
  - claim_text_verbatim: "FrostyNeighbor, also known as Ghostwriter, UNC1151, UAC-0057, TA445, PUSHCHA, or Storm-0257, is a group allegedly operating from Belarus."
    claim_source: ESET / WeLiveSecurity (Damien Schaeffer)
    claim_source_grade_recommendation: A
    claim_confidence_qualifier: "allegedly" + "apparent" (hedge language; no formal high/moderate/low confidence taxonomy)
    actor_in_archimedes_roster: false
    actor_aliases_in_roster: false
    actor_recommended_disposition: "Treat as A-grade ESET-primary attribution claim with hedge language. Do NOT originate attribution per Hard Rule 2. If grader promotes, WEP should sit at 'likely' (4) given (a) A-grade vendor primary, (b) named-byline analyst, (c) first-party telemetry per ESET's research practice, BUT (d) hedge language softening the Belarus-state-link claim, and (e) single-source primary (no second independent A/B-grade corroboration surfaced this sweep). Cross-references finding-2026-05-08-0009 (ABW relay) but does NOT bump that finding's grading (different campaign cluster)."
    recommended_next_action: "actor-profiler should evaluate /new-actor candidacy for UNC1151 / Ghostwriter cluster — multi-A-grade-source coverage spanning Mandiant + ABW + ESET supports roster scaffolding."

ioc_extraction_warnings:
  - "FrostyNeighbor / Ghostwriter / UNC1151 / UAC-0057 / TA445 / PUSHCHA / Storm-0257 alias set NOT in `_roster.yaml`. Grader-time attribution resolution required if cluster is promoted to a finding."
  - "ESET piece reportedly includes 8 SHA-1 hashes + 3 additional C&C domains + YARA rules NOT retrieved in this sweep's WebFetch surface. Grader/actor-profiler should re-fetch full piece if promoting."
  - "Hedge language: 'reportedly', 'allegedly', 'apparent' — ESET uses informal-hedge framing not formal confidence-taxonomy. Grader should preserve verbatim per Hard Rule 2."
  - "CVE-2023-38831 (WinRAR) and CVE-2024-42009 (Roundcube XSS) NOT in Archimedes `_index.yaml`. Pre-existing CVEs with vendor patches; vuln-tracker may add tracking if Splunk shows estate exposure but neither is a fresh-disclosure trigger."
```
