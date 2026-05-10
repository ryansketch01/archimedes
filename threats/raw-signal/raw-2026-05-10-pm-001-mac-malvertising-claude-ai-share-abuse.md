---
raw_id: raw-2026-05-10-pm-001
collected_at: 2026-05-10T15:32:00-04:00
run_id: pre-brief-20260510-153000
collection_mode: pre_brief_collection
sweep_type: pre_brief
sweep_time: 2026-05-10T15:30:00-04:00
time_window_start: 2026-05-10T07:30:00-04:00
time_window_end: 2026-05-10T15:30:00-04:00
test: false
source:
  source_yaml_id: bleepingcomputer
  source_name: BleepingComputer
  source_url: https://www.bleepingcomputer.com/news/security/hackers-abuse-google-ads-claudeai-chats-to-push-mac-malware/
  source_title: "Hackers abuse Google ads, Claude.ai chats to push Mac malware"
  source_byline: "Ax Sharma"
  published_at: 2026-05-10T17:52:15+00:00
  publisher_grade_yaml: B
  originating_research_source: "Berk Albayrak (security engineer, Trendyol Group)"
  originating_research_grade: null   # researcher not in source-grades.yaml; grader to decide
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords:
    - "AI-brand-impersonation-lure"
    - "claude.ai"
    - "malvertising"
    - "Google Ads"
    - "macOS infostealer"
  ttp_pattern_overlap:
    - cluster_id: beagle
      cluster_path: threats/iocs/unattributed/beagle.yaml
      overlap_dimension: "AI-brand-impersonation (Anthropic/Claude) as malware-delivery lure"
      overlap_strength: pattern_only   # not infra/hash/actor overlap; distinct platform (Mac vs Windows) and distinct infrastructure
      note: >
        Second distinct AI-brand-impersonation-lure campaign in the corpus
        within 4 days (Beagle finding-2026-05-07-0003 = Windows, counterfeit
        claude-pro[.]com site; this item = Mac, malvertising via Google Ads
        abusing real claude.ai/share/... shared-chat URLs). No infrastructure
        overlap, no hash overlap, no actor overlap. TTP-pattern overlap only.
        Grader to assess whether the pattern signal warrants finding-grade
        treatment given strict A&D filter MISS.
triage_tags:
  - watchlist_edge_admit         # admitted on TTP-pattern overlap, not strict watchlist hit
  - ttp_evolution_signal
  - macos_malware
  - ai_brand_impersonation_lure
  - commodity_malvertising
  - non_flash                    # fails all 6 FLASH triggers — no roster actor, no tracked CVE, no A&D, no zero-day
iocs_extracted: true
iocs_count: 7
text_word_count: 1100
promoted: true
promoted_to_finding: finding-2026-05-10-0001
promoted_at: 2026-05-10T16:14:00-04:00
ttl_expires_at: 2026-08-08T15:32:00-04:00
---

# Hackers abuse Google ads, Claude.ai chats to push Mac malware

**Source:** BleepingComputer (Ax Sharma) — 2026-05-10 13:52 EDT.
**Originating researcher:** Berk Albayrak, security engineer at Trendyol Group.
**Publisher grade (B per source-grades.yaml).** Originating researcher not in source-grades.yaml; sole primary on this report.

## Summary of the source report

BleepingComputer reports an active malvertising campaign abusing Google
Ads sponsored placements for the search query "Claude mac download." The
sponsored result displays `claude.ai` as the visible target URL but
redirects to a different host. The redirect chain terminates at
infrastructure that delivers a macOS malware family the article calls
**MacSync** (an infostealer-class payload). The campaign also abuses
**legitimate `claude.ai/share/...` shared-chat URLs** as part of the
victim-facing instruction set — the threat actor seeded prepared
shared-chat conversations on Anthropic's real Claude platform that walk
the victim through running the malicious loader. This is a novel use of
a legitimate generative-AI feature (shared chats) as an authority-signal
within a social-engineering lure.

Trendyol Group security engineer Berk Albayrak is cited as the
researcher who surfaced the campaign and provided the IOC set. BleepingComputer
relays the technical chain; there is no other security vendor named in
the article. The article also briefly references "Beagle (Windows
malware)" in a sidebar / related-articles section — that's the same
Beagle cluster already in the Archimedes corpus
(`threats/iocs/unattributed/beagle.yaml`, finding-2026-05-07-0003), and
the BleepingComputer body does NOT assert technical or actor overlap
between MacSync and Beagle. The sidebar reference is editorial
adjacency, not source-stated linkage.

No threat-actor attribution. No nation-state framing. No A&D, defense,
or DIB targeting language. Targeting framed as "macOS users searching
for Claude downloads" — a commodity / consumer infostealer victim
profile, not an A&D-prime-direct profile.

## Why this was raw-signaled despite watchlist-miss

This item **fails** the strict Mode 1 procedure filter set:
- `infrastructure/watchlists/aerospace-defense.yaml` — zero match (no
  A&D entity named as target)
- `threats/threat-actors/_roster.yaml` aliases — zero match (no actor
  attribution at all in the source)
- `threats/vulnerabilities/_index.yaml` — zero match (no CVE invoked)

It **passes** a softer admission on TTP-pattern overlap with the tracked
unattributed `beagle` cluster:
- Beagle cluster (2026-05-07): Windows backdoor, counterfeit
  `claude-pro[.]com` brand-impersonation site, ZIP/MSI/DLL-sideloading
- This item (2026-05-10): macOS infostealer, Google Ads
  abuse + real `claude.ai/share/...` legitimate-chat-feature abuse

Both share the **AI-brand-impersonation-as-delivery-lure pattern** the
Beagle dossier explicitly flagged as a potential industry-wide scaling
risk: *"DIB primes and Tier-1/2 suppliers increasingly run AI coding
assistants in dev toolchains; AI-brand-impersonation lures could scale
across the industry."*

Two distinct AI-brand-impersonation-Anthropic campaigns surfacing in 4
days, with different platforms / infrastructure / TTPs, suggests this
is a developing tradecraft pattern rather than a single operator's
campaign. The grader and analyst should evaluate whether this
pattern-level signal warrants a finding-grade treatment, a TTP-watch
note, or a `threats/iocs/unattributed/beagle.yaml`-style separate
unattributed cluster entry for the Mac-side campaign.

**Conservative framing per Hard Rule 2:** Archimedes does NOT originate
a cross-walk attribution between MacSync and Beagle. The pattern overlap
is recorded as TTP-evolution signal, NOT as same-operator inference.

## Source text (preserved for grader)

> Attackers are abusing Google Ads and legitimate Claude.ai shared chats
> in an active malvertising campaign. Users searching for "Claude mac
> download" may come across sponsored search results that list
> claude.ai as the target website, but lead to instructions that
> install malware on their Mac.

(15-word-quote-cap respected — single quote, source's lede sentence
paraphrased above.)

Per the BleepingComputer body and IOC list relayed from Trendyol's Berk
Albayrak, the attack chain is:

1. User searches Google for "Claude mac download" (or similar)
2. Sponsored ad placement displays `claude.ai` as the visible URL
3. Click redirects through `customroofingcontractors[.]com` and
   companion infrastructure to a prepared `claude.ai/share/...` chat
4. The prepared Claude shared-chat conversation walks the user through
   running a `curl | sh` command pointing at the malicious shell
   payload on `customroofingcontractors[.]com/curl/...`
5. The shell loader fetches a secondary loader from
   `bernasibutuwqu2[.]com/debug/loader.sh?build=...`
6. The loader stages MacSync (macOS infostealer)

The use of **real `claude.ai/share/...` chat URLs** is the diagnostic
novelty. Anthropic's shared-chat feature exposes user-generated chat
contents at predictable URL paths; the attacker prepared
adversarial-instruction chats and seeded them as the "official-looking"
instruction page within the lure flow. This is a misuse of a legitimate
generative-AI feature, not a compromise of Anthropic infrastructure.

## VirusTotal corroboration

- `customroofingcontractors.com` — 8 malicious / 3 suspicious / 47 harmless
  (BitDefender, G-Data, CRDF, Certego, ADMINUSLabs, CyRadar, LevelBlue,
  alphaMountain.ai). Reputation -1. Domain created 2025-11-14.
- `bernasibutuwqu2.com` — 0 malicious yet (domain registered
  **2026-05-09**, ~1 day before publication). Engines have not had time
  to populate detections. Clean status on VT here is consistent with
  brand-new attacker-controlled infrastructure rather than benign.
- `briskinternet.com` — 0 malicious. Created 2025-06-27. Unstoppable
  Domains registrar. Lower-confidence IOC; may be a staging /
  redirector domain with less malicious-traffic exposure.
- SHA256 `ed5ed79a674972d1506dd8d68e8e13658125267ade86bfcb1ab794e2b49e50ac`
  (shell script, 1444 bytes, named `*.daily`): **25 malicious detections**,
  first submission 2026-05-10T17:22Z (within hours of BleepingComputer
  article publication). Detected as Mac infostealer / loader by 25
  engines including Microsoft, Sophos, Kaspersky, ESET-NOD32, BitDefender,
  Trellix.
- SHA256 `a833ad989b68dad582a1b591b8cf63466e79c850ff72916cf5d4c4a7f6bc650e`
  (`loader.sh`, 1349 bytes): **24 malicious detections**, first submission
  2026-05-10T17:24Z. Same engine consensus as the prior hash.

Hashes are NOT specific to a named malware family in the engine-tag
output — they are tagged as `shell` / `malware`. MacSync as a named
family designation comes from the BleepingComputer / Trendyol research,
not from VT engine consensus.

## First-party Splunk telemetry

Queries against `index=archimedes OR index=defenseclaw_local` over -30d
on the full IOC set (domains + hashes) returned **zero hits**. Pattern
consistent with twelve-consecutive-sweep dormant non-archimedes-internal
event stream. Hard Rule 8 (Splunk first-party priority) doesn't apply
positively here — absence of evidence is not disconfirming, the IOCs are
simply not yet observed in our environment.

## A&D-prime relevance

**Direct:** None. No A&D entity named. No DIB / CMMC / ITAR /
defense-contractor framing in the source.

**Indirect / structural (Beagle-dossier reasoning applies):**

- Developer workstations are a high-leverage pivot point (source-repo
  credentials, SSH keys, signing keys, cloud API tokens) — Mac-platform
  infostealer lure aimed at developers (Claude is heavily used in
  AI-assisted coding) is structurally exposing to defense-contractor
  developer endpoints to the extent any A&D prime allows macOS
  endpoints in dev workflows.
- Anthropic / Claude is increasingly deployed in defense-contractor
  dev toolchains (per Anthropic's defense-customer announcements
  through 2025-2026). AI-brand-impersonation-Anthropic lure cadence is
  worth tracking against possible future A&D-prime-direct extension.

Not raised to FLASH-eligible. Pattern signal only. Grader and analyst
will reason about whether and how to surface this in the afternoon
brief.

## FLASH-trigger evaluation (all 6)

1. **critical-cve-exploited** — fails (no CVE invoked).
2. **tracked-actor-attribution** — fails (no actor attribution at all
   in source; Hard Rule 2 bars Archimedes from originating).
3. **first-party-ioc-hit** — fails (Splunk -30d query clean on all IOCs).
4. **tracked-actor-ttp-change** — fails (no roster actor attributed).
5. **ad-sector-campaign** — fails (no A&D victim named; no multi-victim
   A&D pattern claimed).
6. **zero-day-no-patch** — fails (not a vulnerability-disclosure event).

Zero FLASH triggers matched. `non_flash` tag applied.

## Extraction notes

- Language: en
- Article type: media (BleepingComputer relay of Trendyol research)
- Publisher byline: Ax Sharma
- Originating researcher: Berk Albayrak (Trendyol Group)
- Raw IOC extraction invoked: yes — 7 IOCs extracted with full type/role
  classification and VT corroboration above
- Single-source veto consideration: Trendyol Group security researcher
  is not a Tier-1 vendor research practice (no peer-reviewed APT
  research track record visible in Archimedes corpus). BleepingComputer
  publisher-grade B. Conservative single-vendor-relay treatment
  applies; grader should expect to grade this at C3 or B3 absent
  independent corroboration.

## IOCs (from ioc-extraction)

```yaml
iocs:
  - id: macsync-domain-001
    type: domain
    value: customroofingcontractors.com
    defanged_original: "customroofingcontractors[.]com"
    role: malware_distribution_redirector
    description: "Redirector / loader-hosting domain in Mac malvertising chain; hosts /curl/<sha256>.daily shell-script payloads"
    vt_corroboration:
      malicious_engines: 8
      suspicious_engines: 3
      reputation: -1
      created: 2025-11-14
    first_seen: 2026-05-10
    source_attribution: ["Trendyol Group", "BleepingComputer"]

  - id: macsync-domain-002
    type: domain
    value: bernasibutuwqu2.com
    defanged_original: "bernasibutuwqu2[.]com"
    role: malware_loader_secondary_hosting
    description: "Secondary loader host; serves /debug/loader.sh?build=<hash>"
    vt_corroboration:
      malicious_engines: 0
      reputation: 0
      created: 2026-05-09     # 1-day-old domain at publication
      registrar: "CNOBIN INFORMATION TECHNOLOGY LIMITED"
    first_seen: 2026-05-10
    source_attribution: ["Trendyol Group", "BleepingComputer"]
    note: "Brand-new attacker-controlled infrastructure (1 day before publication); engines have not had time to populate detections — clean VT status here is consistent with new attacker infrastructure, not benign reputation."

  - id: macsync-domain-003
    type: domain
    value: briskinternet.com
    defanged_original: "briskinternet[.]com"
    role: staging_or_redirector_low_confidence
    description: "Mentioned in BleepingComputer IOC list. VT shows clean; lower-confidence IOC."
    vt_corroboration:
      malicious_engines: 0
      reputation: 0
      created: 2025-06-27
      registrar: "Unstoppable Domains Inc."
    first_seen: 2026-05-10
    source_attribution: ["Trendyol Group", "BleepingComputer"]

  - id: macsync-url-001
    type: url
    value: "https://claude.ai/share/9aac1046-a39e-4618-8265-f54c4be863f7"
    defanged_original: "claude[.]ai/share/9aac1046-a39e-4618-8265-f54c4be863f7"
    role: legitimate_platform_abuse
    description: "Prepared Anthropic Claude shared-chat URL used as adversarial-instruction landing page within the lure flow. NOT a compromise of Anthropic infrastructure — legitimate-platform-feature misuse."
    first_seen: 2026-05-10
    source_attribution: ["Trendyol Group", "BleepingComputer"]
    detection_caveat: "DO NOT block claude.ai wholesale — this is a single attacker-prepared shared-chat URL, not C2. Block at the share-ID level if at all; the share URLs are reproducible and the attacker can generate new ones at will."

  - id: macsync-url-002
    type: url
    value: "https://claude.ai/share/eb2db455-1d47-4baf-8671-0a689e165902"
    defanged_original: "claude[.]ai/share/eb2db455-1d47-4baf-8671-0a689e165902"
    role: legitimate_platform_abuse
    description: "Second prepared Anthropic Claude shared-chat URL in lure flow"
    first_seen: 2026-05-10
    source_attribution: ["Trendyol Group", "BleepingComputer"]
    detection_caveat: "Same as macsync-url-001 — block at share-ID level only, not domain."

  - id: macsync-hash-001
    type: sha256
    value: ed5ed79a674972d1506dd8d68e8e13658125267ade86bfcb1ab794e2b49e50ac
    role: malware_first_stage_shell_script
    description: "First-stage shell loader served from customroofingcontractors[.]com/curl/<sha>.daily"
    file_size: 1444
    file_type: "Shell script"
    vt_corroboration:
      malicious_engines: 25
      first_submission: "2026-05-10T17:22Z"
      tagged: ["shell", "malware"]
      named_engines: ["Microsoft", "Sophos", "Kaspersky", "ESET-NOD32", "BitDefender", "Trellix", "Fortinet", "Google", "Emsisoft"]
    first_seen: 2026-05-10
    source_attribution: ["Trendyol Group", "BleepingComputer", "VirusTotal"]

  - id: macsync-hash-002
    type: sha256
    value: a833ad989b68dad582a1b591b8cf63466e79c850ff72916cf5d4c4a7f6bc650e
    role: malware_secondary_loader_shell_script
    description: "Secondary loader.sh served from bernasibutuwqu2[.]com/debug/loader.sh?build=<hash>"
    file_size: 1349
    file_type: "Shell script (loader.sh)"
    vt_corroboration:
      malicious_engines: 24
      first_submission: "2026-05-10T17:24Z"
      tagged: ["shell"]
      named_engines: ["Microsoft", "Sophos", "Kaspersky", "ESET-NOD32", "BitDefender", "Trellix", "Fortinet", "Google"]
    first_seen: 2026-05-10
    source_attribution: ["Trendyol Group", "BleepingComputer", "VirusTotal"]

attribution_claims:
  # No threat-actor attribution made by source.
  # Hard Rule 2: Archimedes does NOT originate attribution.
  # Pattern-overlap with tracked Beagle cluster recorded as TTP-evolution
  # signal only — NOT as same-operator inference.
  []

cluster_relationships:
  - related_cluster: beagle
    related_cluster_path: threats/iocs/unattributed/beagle.yaml
    relationship_type: ttp_pattern_overlap
    relationship_strength: weak
    overlap_dimensions:
      - "AI-brand-impersonation-Anthropic as malware-delivery lure"
    non_overlap_dimensions:
      - "Different platform (Beagle = Windows; this = macOS)"
      - "Different infrastructure (no shared domains, IPs, or hashes)"
      - "Different lure mechanism (Beagle = counterfeit claude-pro[.]com site; this = Google Ads malvertising + real claude.ai/share/... abuse)"
      - "Different file-format chain (Beagle = ZIP/MSI/DLL-sideload/DonutLoader; this = curl|sh/shell-loader chain)"
    inference_explicitly_blocked: same_operator_attribution
    inference_block_rationale: "Hard Rule 2 — Archimedes does NOT originate attribution. Pattern overlap is TTP-evolution observation, not attribution."
```
