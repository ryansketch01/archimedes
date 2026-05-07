---
raw_id: raw-2026-05-07-pm-005
collected_at: 2026-05-07T15:42:00-04:00
run_id: pre-brief-20260507-153000
collection_mode: pre_brief_collection
test: false
sources:
  - source_yaml_id: bleepingcomputer
    source_name: "BleepingComputer (Bill Toulas)"
    source_url: https://www.bleepingcomputer.com/news/security/fake-claude-ai-website-delivers-new-beagle-windows-malware/
    source_grade_estimated: B
    role: originating
    published_at: 2026-05-07T06:02:00-04:00
    note: |
      Sophos research relayed by BleepingComputer. Counterfeit Claude AI
      site (claude-pro[.]com) delivers Beagle Windows backdoor via
      DLL-sideloading chain. Sophos researchers assess: "The same operators
      behind PlugX might be experimenting with a new payload."
      PlugX is historically associated with multiple China-nexus tracked
      actors (APT41 in particular per public reporting). Hard Rule 2:
      Sophos hedges with "might be" — Archimedes does not upgrade to
      attribution. Recorded as defender-actionable IOC set + tooling-overlap
      context only.
match_reason:
  watchlist: []
  actors: ["019"]    # APT41 — historical PlugX overlap context only, NOT current attribution
  vulnerabilities: []
  keywords: [beagle, plugx, donutloader, claude-pro-impersonation, sophos, dll-sideloading, alibaba-cloud-c2, software-developer-targeting]
triage_tags: [malware_family_new, possible_china_nexus_overlap, dll_sideloading, dev_targeted_via_ai_brand_impersonation, sophos_attribution_hedged]
iocs_extracted: true
iocs_count: 6
text_word_count: 360
promoted: true
promoted_to_finding: finding-2026-05-07-0003
promoted_at: 2026-05-07T16:13:00-04:00
promoted_by: grader
promoted_grading_run_id: afternoon-20260507-160000
ttl_expires_at: 2026-08-05T15:42:00-04:00
---

# Fake "Claude AI" website (claude-pro[.]com) delivers new Beagle Windows backdoor — Sophos hedges possible PlugX-operator overlap

## Source summary

BleepingComputer (Bill Toulas, "Fake Claude AI website delivers new 'Beagle' Windows malware," 2026-05-07 06:02 EDT) reports Sophos research on a counterfeit Claude AI distribution site delivering a previously undocumented Windows backdoor named Beagle. Targeting: software developers via AI-brand impersonation. Sophos researchers describe Beagle as "a relatively simple backdoor" and assess: "The same operators behind PlugX might be experimenting with a new payload."

Quote (under 15-word limit, attributed to Sophos): "The same operators behind PlugX might be experimenting with a new payload."

## What this source covers

**Distribution chain:**
1. Fake site `claude-pro[.]com` impersonates Anthropic / Claude branding
2. 505MB malicious archive `Claude-Pro-windows-x64.zip` delivered as download
3. MSI installer drops signed G Data updater binary `NOVupdate.exe` (used for sideloading)
4. Sideloads `avk.dll` (malicious DLL)
5. `avk.dll` loads `NOVupdate.exe.dat` (encrypted payload) — DonutLoader first stage
6. DonutLoader → Beagle backdoor

**Beagle command set:** uninstall, cmd, upload, download, mkdir, rename, ls, rm

**C2 infrastructure:**
- `license[.]claude-pro[.]com` (C2 server, hostname)
- `8.217.190[.]58` (Alibaba Cloud range, C2 hosting)
- TCP port 443, UDP port 8080, AES encryption

**Targeting:** Software developers — specifically those seeking Claude / Claude Code tooling. Article describes the threat actor's lure as: "high-performance relay service designed specifically for Claude-Code developers."

## Attribution context — Hard Rule 2

Sophos hedges: "The same operators behind PlugX **might be** experimenting with a new payload." This is suggestive, not assertive. PlugX is historically associated with multiple China-nexus tracked actors per public reporting (APT41 / roster id 019, plus others outside the Archimedes roster).

**Archimedes does not originate the cross-walk.** Recorded as:
- IOC set (defender-actionable)
- Tooling-overlap context for any future actor-profiler review
- Targeting pattern (developer-focused AI brand impersonation) — relevant because A&D dev environments increasingly use AI coding assistants

## A&D relevance — inferential, not source-stated

No A&D entity named. No defense-contractor targeting claim. Inferential relevance:
- Software developers at A&D primes and Tier-1/2 suppliers are increasingly using AI coding assistants in their toolchains
- AI-brand impersonation lure is a NEW initial-access vector that may scale across the industry
- Beagle's command set is consistent with a foothold-establishment backdoor; downstream actor objectives unclear from this single source

Recommend `vuln-tracker` and `actor-profiler` flag the IOC set for cross-reference if the operator-overlap-with-PlugX claim is later confirmed by a second source.

## Why this is a scheduled-brief item, NOT a FLASH

Trigger evaluation:
- **Trigger-1 (critical-cve-exploited):** No CVE involved. Fails.
- **Trigger-2 (tracked-actor-attribution):** Sophos hedges "might be" — does not meet "article attributes activity to actor" threshold per FLASH-POLICY.md trigger-2 conditions. Fails.
- **Trigger-3 (first-party-ioc-hit):** Splunk recheck recommended on the IOCs below.
- **Trigger-4 (tracked-actor-ttp-change):** Speculative attribution does not establish tracked-actor activity. Fails.
- **Trigger-5 (ad-sector-campaign):** No A&D sector named. Fails.
- **Trigger-6 (zero-day-no-patch):** No CVE involved. Fails.

---

## Extraction notes

- Language: en
- Article type: secondary news reporting (B-grade), citing Sophos research (A-grade vendor)
- Raw IOC extraction invoked: yes
- Quote-discipline: one quote, 11 words, under 15-word limit honored

## IOCs (from ioc-extraction skill)

```yaml
iocs:
  - type: domain
    value: claude-pro[.]com
    confidence: high
    role: distribution_site
    source_attribution: ["Sophos", "BleepingComputer"]
    notes: "Defanged. Counterfeit Claude AI brand impersonation."

  - type: domain
    value: license[.]claude-pro[.]com
    confidence: high
    role: c2
    source_attribution: ["Sophos", "BleepingComputer"]
    notes: "Defanged. Subdomain of fake distribution site."

  - type: ipv4
    value: 8.217.190.58
    confidence: high
    role: c2_hosting
    source_attribution: ["Sophos", "BleepingComputer"]
    notes: "Alibaba Cloud range. Beagle C2."
    asn_context: "Alibaba Cloud (operator-described in source)"

  - type: filename
    value: Claude-Pro-windows-x64.zip
    confidence: high
    role: malware_distribution_archive
    size: "505MB"
    source_attribution: ["Sophos", "BleepingComputer"]

  - type: filename
    value: NOVupdate.exe
    confidence: high
    role: signed_loader_for_sideloading
    source_attribution: ["Sophos", "BleepingComputer"]
    notes: "Legitimate G Data updater binary repurposed for DLL-sideloading."

  - type: filename
    value: avk.dll
    confidence: high
    role: malicious_sideloaded_dll
    source_attribution: ["Sophos", "BleepingComputer"]

  - type: malware_family
    value: Beagle
    confidence: high
    role: backdoor
    source_attribution: ["Sophos"]
    capabilities: ["uninstall", "cmd", "upload", "download", "mkdir", "rename", "ls", "rm"]
    c2_protocols: ["TCP/443", "UDP/8080", "AES-encrypted"]
    notes: "Newly named family per Sophos. Possibly operator-overlap with PlugX (hedged)."

  - type: malware_family
    value: DonutLoader
    confidence: high
    role: first_stage_loader
    source_attribution: ["Sophos"]

attribution_claims:
  - actor_named: "[unspecified — possible PlugX operators]"
    actor_class: "Sophos hedged speculation; not asserted"
    nation_state_named: false
    confidence_language: "might be experimenting with"
    cross_walk_to_roster: null
    archimedes_action: |
      Hard Rule 2 — do not originate cross-walk. Sophos's "might be"
      hedge does not meet attribution threshold. Recorded as
      tooling-overlap context only. APT41 (roster 019) listed in
      match_reason solely because PlugX is historically associated;
      this is NOT a current-campaign attribution.
```

- Authorized-targets check: not applicable
- LEGAL-POLICY check: passed
