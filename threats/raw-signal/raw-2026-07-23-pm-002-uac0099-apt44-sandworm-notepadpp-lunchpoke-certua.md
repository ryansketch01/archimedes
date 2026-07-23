---
raw_id: raw-2026-07-23-pm-002
collected_at: 2026-07-23T15:40:00-04:00
run_id: pre-brief-20260723-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: bleepingcomputer
  source_name: "BleepingComputer (Bill Toulas), relaying CERT-UA"
  source_url: https://www.bleepingcomputer.com/news/security/hackers-abuse-notepad-plus-plus-plugins-to-stealthily-install-malware/
  published_at: 2026-07-23T12:32:35-04:00   # 16:32:35 GMT
match_reason:
  watchlist: []
  actors: [Sandworm, APT44, "UAC-0099"]   # Sandworm/APT44 = roster #007; UAC-0099 NOT in _roster.yaml
  vulnerabilities: [CVE-2025-56383]        # Notepad++ DLL-hijacking; disputed by Notepad++ team; not in _index.yaml
  keywords: ["Notepad++", "LunchPoke", "BurnyBear", "MatchBoil V2", "NppExport.dll", "CERT-UA", "DLL hijacking", "scheduled task", Ukraine]
triage_tags: [non_flash, tracked_actor, tracked_actor_ttp_change, new_tooling, cert_ua_source, no_ad_named, ukraine_theater, disputed_cve, splunk_not_swept_no_atomic_iocs]
iocs_extracted: true
iocs_count: 4
text_word_count: 300
promoted: true
promoted_to_finding: finding-2026-07-23-0004    # B2 / likely / single-source veto; single CERT-UA primary via one BleepingComputer B relay (primary not directly retrieved); UAC-0099 -> APT44/Sandworm (#007) access-handoff recorded NOT merged (Hard Rule 2); Ukraine-theater, no named A&D victim (ad_relevance LOW); CVE-2025-56383 disputed
promoted_at: 2026-07-23T16:22:00-04:00
ttl_expires_at: 2026-10-21T15:40:00-04:00
---

# CERT-UA: UAC-0099 abuses Notepad++ plugin DLL-hijack (CVE-2025-56383) to deploy LunchPoke/BurnyBear/MatchBoil V2 — initial access handed to APT44 (Sandworm, #007)

**Window (2026-07-23 07:30 → 15:30 EDT):** BleepingComputer (Bill Toulas) relayed a fresh
**CERT-UA** advisory: attackers distribute a password-protected archive (`updater.rar`)
bundling the **legitimate Notepad++ v8.8.3** with a malicious utility, **LunchPoke**,
disguised as a plugin (`NppExport.dll`) that establishes persistence via a scheduled task.
The chain loads **BurnyBear** (loader) and a final loader **MatchBoil V2** (`InitTest.dll`).
Delivery is a ZIP archive containing a VBS script disguised as a PDF. CERT-UA attributes
the campaign to **UAC-0099**, and notes the activity is **linked to handing initial access
to APT44 (Sandworm)**.

## Why raw-signaled — tracked-actor TTP change (Sandworm #007) via a tracked source (CERT-UA)

- **Roster match:** **APT44 / Sandworm = `_roster.yaml` #007** (RU / GRU Unit 74455). This
  surface documents an **access-handoff relationship** (UAC-0099 → Sandworm) plus **new
  tooling** (LunchPoke, BurnyBear, MatchBoil V2) — a candidate TTP-change / tradecraft
  update against the actor's dossier.
- **UAC-0099** is the primary-attributed cluster and is **not** in `_roster.yaml` — recorded
  as stated; candidate operator review, no Archimedes-originated attribution.
- **Source:** CERT-UA (provisional-A, `cert-ua`, provenance finding-2026-07-16-0003 — the
  prior Sandworm/APT44 ClickFix surface). This continues the CERT-UA → Sandworm tracking
  thread. Reached the corpus via **BleepingComputer B relay**; the **CERT-UA advisory
  primary was NOT directly retrieved** (no advisory reference number in the relay) — atomic
  IOCs (hashes/C2/scheduled-task paths) are a direct-retrieval enrichment todo.

## A&D relevance — LOW / none named

Targeting is **Ukraine / Ukrainian organizations** (a "Ukrainian army" connection is noted
in related reporting). **No A&D prime/DIB victim named.** Structural interest only: the
plugin-DLL-hijack-into-scheduled-task pattern and the "legitimate signed app + malicious
sidecar DLL" packaging are portable tradecraft.

## Attribution — recorded as CERT-UA states it (Hard Rule 2)

CERT-UA: **UAC-0099** primary; activity **linked to providing initial access to APT44
(Sandworm)**. Archimedes originates no attribution and asserts no UAC-0099 ↔ Sandworm merge
— the relationship recorded is the **access-handoff** CERT-UA describes.

## Note on CVE and first-party

- **CVE-2025-56383** (Notepad++ v8.8.3 DLL-hijacking) is **disputed by the Notepad++ team**
  as standard plugin functionality (hedge preserved). Not in `_index.yaml`; low-priority
  candidate given the vendor dispute. CERT-UA remediation guidance: Notepad++ v8.9.7,
  7-Zip v26.02, WinRAR v7.23.
- **Splunk NOT swept this item** — the relay carries **no atomic network IOCs** (hashes/
  IPs/domains), only malware family names and DLL filenames. Sweep deferred to grader after
  direct CERT-UA IOC-appendix retrieval.

## Extraction notes

- Language: en
- Publisher byline: Bill Toulas (BleepingComputer), relaying CERT-UA
- Article type: security news relay of a national-CERT advisory
- Raw IOC extraction invoked: yes

## IOCs (from ioc-extraction skill)

```yaml
extraction_metadata:
  source_brief_id: certua-uac0099-notepadpp-2026-07-23
  source_url: https://www.bleepingcomputer.com/news/security/hackers-abuse-notepad-plus-plus-plugins-to-stealthily-install-malware/
  extracted_at: 2026-07-23T19:40:00Z
  extracted_by: collector
  target_actor_id: "007"   # Sandworm/APT44 — access-handoff recipient per CERT-UA; UAC-0099 primary not in roster
  text_word_count: 300

indicators:
  - id: raw-cve-2025-56383
    type: cve
    value: CVE-2025-56383
    defanged_original: null
    first_seen: 2026-07
    last_seen: 2026-07
    role: delivery
    campaign: "UAC-0099 Notepad++ plugin-hijack (CERT-UA)"
    related_malware: [LunchPoke, BurnyBear, "MatchBoil V2"]
    source_brief: certua-uac0099-notepadpp-2026-07-23
    context_excerpt: "DLL hijacking flaw in Notepad++ v8.8.3; disputed by Notepad++ team as standard plugin functionality."
    attribution_in_text: "UAC-0099 (initial access to APT44/Sandworm)"
    notes: "Disputed CVE; not in _index.yaml. CVSS not stated. Low-priority candidate given vendor dispute."
  - id: raw-file-nppexport-dll-lunchpoke
    type: file_path
    value: NppExport.dll
    defanged_original: null
    first_seen: 2026-07
    last_seen: 2026-07
    role: persistence
    campaign: "UAC-0099 Notepad++ plugin-hijack (CERT-UA)"
    related_malware: [LunchPoke]
    source_brief: certua-uac0099-notepadpp-2026-07-23
    context_excerpt: "LunchPoke malicious utility disguised as a Notepad++ plugin (NppExport.dll); establishes persistence via scheduled task."
    attribution_in_text: "UAC-0099"
    notes: "Filename indicator only; no hash in relay. LunchPoke = malware family name."
  - id: raw-file-inittest-dll-matchboil
    type: file_path
    value: InitTest.dll
    defanged_original: null
    first_seen: 2026-07
    last_seen: 2026-07
    role: staging
    campaign: "UAC-0099 Notepad++ plugin-hijack (CERT-UA)"
    related_malware: ["MatchBoil V2"]
    source_brief: certua-uac0099-notepadpp-2026-07-23
    context_excerpt: "MatchBoil V2 final malware loader embedded as InitTest.dll; BurnyBear serves as loader for the final payload."
    attribution_in_text: "UAC-0099"
    notes: "Filename indicator only; no hash in relay. MatchBoil V2 / BurnyBear = malware family names."
  - id: raw-file-updater-rar
    type: file_path
    value: updater.rar
    defanged_original: null
    first_seen: 2026-07
    last_seen: 2026-07
    role: delivery
    campaign: "UAC-0099 Notepad++ plugin-hijack (CERT-UA)"
    related_malware: []
    source_brief: certua-uac0099-notepadpp-2026-07-23
    context_excerpt: "Password-protected archive updater.rar bundling legitimate Notepad++ v8.8.3 with the malicious plugin; delivered via a ZIP archive containing a VBS script disguised as a PDF."
    attribution_in_text: "UAC-0099"
    notes: "Filename/lure indicator only; no hash in relay."

attribution_claims:
  - claimed_actor: "UAC-0099 (initial access provider to APT44 / Sandworm, roster #007)"
    ioc_ids:
      - raw-cve-2025-56383
      - raw-file-nppexport-dll-lunchpoke
      - raw-file-inittest-dll-matchboil
      - raw-file-updater-rar
    claimed_by_source: certua-uac0099-notepadpp-2026-07-23
    attribution_confidence_in_source: high   # CERT-UA primary attribution to UAC-0099; APT44 handoff noted
    requires_grading: true

benign_filtered:
  - value: notepad-plus-plus.org
    reason: reference_site
  - value: bleepingcomputer.com
    reason: publisher_domain

extraction_warnings:
  - type: relay_sourced_no_atomic_iocs
    ioc_id: null
    detail: "CERT-UA advisory primary not directly retrieved (no reference number in relay). Only malware family names + DLL/archive filenames captured; no hashes/IPs/domains/scheduled-task paths. Direct CERT-UA retrieval is an enrichment todo before Splunk sweep + promotion."
  - type: non_roster_actor
    ioc_id: null
    detail: "UAC-0099 (primary-attributed cluster) not in _roster.yaml. APT44/Sandworm = #007 (access-handoff recipient). No Archimedes-originated merge between the two."
  - type: disputed_cve
    ioc_id: raw-cve-2025-56383
    detail: "CVE-2025-56383 disputed by Notepad++ team as standard plugin functionality — hedge preserved verbatim per Hard Rule 2."
```
