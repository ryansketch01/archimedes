---
raw_id: raw-2026-06-16-pm-003-thn-bluevoyant-clickfix-lorem-ipsum-loader-vanilla-tempest-vice-society-attribution-substrate
collected_at: 2026-06-16T15:35:00-04:00
run_id: pre-brief-20260616-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: thehackernews
  source_name: The Hacker News
  source_url: https://thehackernews.com/2026/06/clickfix-campaigns-expand-malware.html
  published_at: 2026-06-16T17:41:28+00:00
match_reason:
  watchlist: []
  actors: [Vice Society, Vanilla Tempest]
  vulnerabilities: []
  keywords: [ClickFix, BabaDeda Loader, Lorem Ipsum Loader, Potemkin, Rapid Brigantine, Vice Spider]
triage_tags: [substrate_strengthening_vice_society_attribution, new_actor_vice_society_candidacy_operator_deferred, multi_vendor_research_cluster, no_a_d_named_victim, single_source_veto_applies_on_bluevoyant_layer]
iocs_extracted: false
iocs_count: 0
text_word_count: 540
promoted: false
rejected: true
rejected_at: 2026-06-16T16:00:00-04:00
rejection_id: reject-2026-06-16-0004
ttl_expires_at: 2026-09-14T15:35:00-04:00
---

# ClickFix Campaigns Expand Malware Delivery With New Loaders and Fake Update Lures

**Source:** The Hacker News (https://thehackernews.com/2026/06/clickfix-campaigns-expand-malware.html)
**Author byline:** Ravie Lakshmanan (The Hacker News)
**Published:** 2026-06-16T17:41:28+00:00 (13:41 EDT, inside pre-brief window)

## Key extracted content

Three independent vendor research streams converge on a ClickFix-themed malware loader cluster:

- **BabaDeda Loader** — discovered by **Morphisec**. Crypter service active since 2021. Attacks observed April 2026 targeted **education** and **financial** organizations.
- **Lorem Ipsum Loader** — identified by **BlueVoyant**. **"Attributed with high confidence to Vanilla Tempest (aka Rapid Brigantine, Vice Society, and Vice Spider)"** [13-word attribution-language quote preserved verbatim per Hard Rule 6].
- **Potemkin** — found by **Huntress**. No threat actor attribution.

Industries targeted across the three campaigns: **education, financial services, architecture, legal services, construction technology**. NO A&D-prime named victim.

No CVEs referenced. Attack techniques: ClickFix social engineering, DLL side-loading, PowerShell execution.

## Extraction notes

- **Language:** en
- **Publisher byline:** Ravie Lakshmanan (THN B-grade publisher independent journalistic relay)
- **Article type:** Trade-press cluster aggregation of three independent vendor research reports (Morphisec / BlueVoyant / Huntress as named primaries)
- **Raw IOC extraction invoked:** no (relay-layer aggregation; specific IOCs not surfaced in THN body — operator-deferred direct retrieval of Morphisec / BlueVoyant / Huntress primaries recommended for IOC enrichment)
- **Hard Rule 2 preservation:** **BlueVoyant** originates the **Vanilla Tempest = Rapid Brigantine = Vice Society = Vice Spider** attribution; Archimedes records the claim with BlueVoyant attribution-language preserved verbatim ("attributed with high confidence"). Vanilla Tempest is MSTIC's naming for the cluster also tracked as Vice Society by other vendors (CrowdStrike / Sophos historical naming). Archimedes does NOT originate the alias cross-walk — BlueVoyant asserts it; Archimedes preserves the asserted alias set verbatim.
- **Hard Rule 6 preservation:** BlueVoyant attribution quote 13 words at-limit-not-exceeded; Morphisec / Huntress contribution language under cap.

## Substrate observation for grader

**Substrate-strengthening on /new-actor-Vice-Society operator-deferred candidacy** from the FLASH-1200 sweep (commit `61eac22`) Dark Reading single-publisher Lorem Ipsum Malware/ClickFix piece by Jai Vijayan, which suggested possible Vice Society linkage at the FLASH-1200 substrate baseline:

- **FLASH-1200 baseline:** Dark Reading single-publisher (Jai Vijayan) on Lorem Ipsum/ClickFix possibly linked to Vice Society.
- **This pre-brief raw-signal:** Dark Reading + THN-Lakshmanan-BlueVoyant-primary dual-publisher independent journalistic relay of BlueVoyant high-confidence attribution explicitly linking Lorem Ipsum Loader to Vanilla Tempest/Vice Society/Vice Spider.

**Substrate effect:** Single-publisher veto on the Vice Society linkage layer has cleared into single-primary-attribution-source (BlueVoyant) + dual-publisher-journalistic-independent-relay (Dark Reading + THN) substrate. The single-vendor-IR-firm-on-actor-attribution-layer single-source veto on BlueVoyant's attribution **still applies** — no independent IR-firm corroboration of the Vanilla Tempest = Vice Society attribution layer in this sweep window; Morphisec on BabaDeda + Huntress on Potemkin are distinct loaders in the cluster, not corroboration of BlueVoyant's Lorem Ipsum attribution.

**A&D relevance:** No A&D-prime named victim. Targeted industries are education / financial / architecture / legal / construction — outside A&D direct scope. ClickFix social-engineering tradecraft layer is broadly applicable across enterprise tenants including A&D primes.

**WEP ceiling:** "likely" on BlueVoyant attribution claim layer (single-IR-vendor on novel-attribution-layer single-source veto). Higher on the multi-vendor-observed loader-existence-layer (Morphisec on BabaDeda / BlueVoyant on Lorem Ipsum / Huntress on Potemkin all independent and converging on the ClickFix loader cluster pattern).

## Grader / briefer cues

- **Possible PM brief Other Signal one-liner** — Vice Society/Vanilla Tempest/Rapid Brigantine/Vice Spider attribution substrate-strengthening watch via BlueVoyant primary + Dark Reading + THN dual-publisher relay; /new-actor-Vice-Society operator-deferred candidacy stands but substrate has shifted from single-publisher veto to single-primary + dual-publisher-relay substrate.
- **/new-actor Vice Society candidacy substrate-strengthening** — BlueVoyant primary attribution-language preserved verbatim; operator-deferred per Hard Rule 5 binding /new-actor-Vice-Society-pathway-requires-operator-invocation.
- **Hard Rule 2 BINDING preserved** — Archimedes does NOT originate alias cross-walk; BlueVoyant's attribution string preserved verbatim with publisher provenance.
- **Single-source veto applies** on BlueVoyant attribution-layer claim until independent IR-vendor corroboration emerges.
- **Provisional source candidates surfaced this sweep** — Morphisec (BabaDeda primary), BlueVoyant (Lorem Ipsum primary), Huntress (Potemkin primary) — none in `source-grades.yaml`. Operator-deferred provisional-grade decision (BlueVoyant is an established mid-market MSSP / threat-intel vendor — likely provisional-B baseline if added; Morphisec endpoint-protection vendor with research arm — likely provisional-B; Huntress MSP-focused MDR with established research output — likely provisional-B). Not promoted this sweep.
