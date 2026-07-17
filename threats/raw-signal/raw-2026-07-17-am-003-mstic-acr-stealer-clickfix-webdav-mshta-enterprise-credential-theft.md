---
raw_id: raw-2026-07-17-am-003
collected_at: 2026-07-17T07:39:00-04:00
run_id: pre-brief-20260717-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: mstic
  source_name: Microsoft Security Research / Microsoft Defender Experts (Balaji Venkatesh S)
  source_url: https://www.microsoft.com/en-us/security/blog/2026/07/16/acr-stealer-two-observed-intrusion-chains-amid-increased-threat-activity/
  published_at: 2026-07-16T23:12:02+00:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [ACR Stealer, Amatera Stealer, ClickFix, WebDAV, MSHTA, PowerShell, infostealer, credential theft, blockchain C2, steganography]
  thematic_link: "Borderline / judgment call — NOT a hard watchlist/roster/vuln hit (ACR Stealer is a commodity MaaS infostealer, UNATTRIBUTED, no roster actor). Retained because (1) A-grade MSTIC first-party primary with Defender telemetry + IOCs + hunt guidance, and (2) ClickFix is a corpus-tracked cross-cutting TTP actively proliferating — Sandworm/APT44 ClickFix adoption was just covered in finding-2026-07-16-0003. Enterprise-wide credential-theft relevance (incl. A&D enterprises). Grader to decide scope."
triage_tags: [infostealer, clickfix, ttp_proliferation, mstic, credential_theft, maas, non_flash, borderline_scope]
iocs_extracted: true
iocs_count: 1
text_word_count: 520
promoted: true
promoted_to_finding: finding-2026-07-17-0002
promoted_at: 2026-07-17T08:18:00-04:00
grading_run_id: morning-20260717-080000
ttl_expires_at: 2026-10-15T07:39:00-04:00
---

# ACR Stealer: Two observed intrusion chains amid increased threat activity

**Source:** Microsoft Defender Experts / MSTIC (id: mstic, grade A), published
2026-07-16 23:12 UTC. Full RSS body retrieved this sweep; the MSTIC atomic-IOC
appendix (IPs/domains/hashes) is NOT in the syndicated body and is flagged
`pending_direct_retrieval` below.

## Summary

From late April 2026 to mid-June 2026, Microsoft Defender Experts observed
**increased ACR Stealer activity** across customer environments, using
**ClickFix** lures to steal browser credentials, authentication/session tokens,
and sensitive documents from **enterprise environments**. ACR Stealer is an
information-stealer reportedly offered as **malware-as-a-service (MaaS)** and
associated with the **rebranding of Amatera Stealer**. Attribution is to the
ACR Stealer family based on behavior + post-exploitation tradecraft corroborated
by OSINT infrastructure analysis — **no threat-actor / roster attribution**
(Hard Rule 2 preserved; family-level only).

## Two campaigns (both begin with ClickFix)

**Campaign 1 — WebDAV-based ClickFix with Python loaders + blockchain C2:**
ClickFix prompt (likely malvertising / SEO-poisoned results) → `cmd.exe` →
`rundll32.exe` loads a DLL from a remote **WebDAV** share over HTTPS. WebDAV path
uses GUID-style directories + legit-looking filenames (e.g., `google.ct`). Three
initial-execution variants observed: (1) direct `rundll32`; (2) `pushd`-mounted
WebDAV share; (3) headless/obfuscated `pushd` via `conhost.exe --headless` with
environment-variable obfuscation + delayed expansion. Python-based loaders +
persistence; some intrusions use **blockchain-backed dead-drop C2 resolution**.

**Campaign 2 — MSHTA-initiated PowerShell chain with steganographic delivery:**
more fileless — **MSHTA** + obfuscated **PowerShell** + **steganography**-assisted
in-memory execution. Both campaigns converge on stealing browser-stored
credentials and other sensitive data for exfiltration.

## Defender coverage / hunting

MSTIC provides behavioral coverage + hunting for living-off-the-land execution,
suspicious WebDAV/MSHTA activity, obfuscated PowerShell, scheduled-task
persistence, in-memory execution, and browser-credential-store access. Full IOC
list + hunting queries are in the MSTIC blog (not syndicated to the feed body).

---

## Extraction notes

- Language: en
- Publisher byline: Microsoft Security Research + Balaji Venkatesh S (MSTIC / Defender Experts, grade A)
- Article type: vendor threat-intelligence blog (first-party EDR-telemetry-backed)
- Raw IOC extraction invoked: yes — behavioral/technique observables captured; atomic network IOCs (IPs/domains/hashes) NOT in the syndicated body → `pending_direct_retrieval`.
- Hard Rule 3: execution-chain described at capability level; no runnable commands/payloads reproduced. The `google.ct` masquerade filename + `rundll32`/`pushd`/`conhost --headless`/MSHTA sequence are detection observables.
- A&D-relevance hint for grader (not an assessment): no A&D victim named and no roster actor; relevance is structural (enterprise credential/token theft applies to any org incl. A&D). Primary analytic value is TTP-proliferation tracking — ClickFix as a delivery primitive now spans commodity MaaS (this) and nation-state (Sandworm/APT44 finding-2026-07-16-0003). Likely a monitoring/technique-watch item, not a standalone A&D finding — grader's call.

## IOCs (from ioc-extraction skill)

```yaml
extraction_metadata:
  source_brief_id: raw-2026-07-17-am-003
  source_url: https://www.microsoft.com/en-us/security/blog/2026/07/16/acr-stealer-two-observed-intrusion-chains-amid-increased-threat-activity/
  extracted_at: 2026-07-17T11:39:00Z
  extracted_by: collector
  target_actor_id: null
  text_word_count: 520

indicators:
  - id: raw-filepath-google-ct-webdav-masquerade
    type: file_path
    value: google.ct
    defanged_original: null
    first_seen: 2026-04
    last_seen: 2026-06
    role: delivery
    campaign: "ACR Stealer Campaign 1 (WebDAV/ClickFix)"
    related_malware: [ACR Stealer, Amatera Stealer]
    source_brief: raw-2026-07-17-am-003
    context_excerpt: >
      "The WebDAV path commonly uses a GUID-based directory structure and
      filenames designed to resemble legitimate resources (for example,
      google.ct)" loaded via rundll32 over HTTPS WebDAV.
    attribution_in_text: null
    notes: "Masquerade filename observable, not a full path/hash. Atomic WebDAV host + C2 domains/IPs + payload hashes are in the MSTIC blog IOC appendix — pending_direct_retrieval."

attribution_claims: []

benign_filtered:
  - value: microsoft.com
    reason: reference_site_publisher_and_impersonation_context
  - value: google.com
    reason: brand_impersonated_by_masquerade_filename_not_an_ioc

extraction_warnings:
  - type: atomic_iocs_pending_direct_retrieval
    ioc_id: null
    detail: "MSTIC blog carries an IOC appendix (WebDAV host, C2 domains/IPs, blockchain dead-drop resolver, payload SHA-256 hashes) + KQL hunts not present in the syndicated feed body. Direct retrieval of the blog needed to fold atomic indicators. Behavioral TTP observables (WebDAV+rundll32, pushd, conhost --headless, MSHTA+PowerShell+steganography, browser-cred-store access) captured as detection guidance."
```
