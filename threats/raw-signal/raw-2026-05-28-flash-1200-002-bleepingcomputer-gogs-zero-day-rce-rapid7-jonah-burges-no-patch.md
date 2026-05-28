---
raw_id: raw-2026-05-28-flash-1200-002
collected_at: 2026-05-28T12:19:00-04:00
run_id: flash-sweep-20260528-120000
collection_mode: flash_sweep
source:
  source_yaml_id: bleepingcomputer
  source_name: BleepingComputer
  source_url: https://www.bleepingcomputer.com/news/security/new-gogs-zero-day-flaw-lets-hackers-get-remote-code-execution/
  source_yaml_id_origin: rapid7
  source_origin_attribution: "Jonah Burges, Rapid7 senior security researcher"
  published_at: 2026-05-28T10:25:00-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: [gogs-rce-unassigned]
  keywords: [Gogs, zero-day, argument injection, RCE, no patch, rebase, Rapid7]
triage_tags: [flash_candidate, trigger-6-zero-day-no-patch, vulnerability_disclosure, no_actor_attribution, developer_tooling]
iocs_extracted: true
iocs_count: 1
text_word_count: 380
promoted: true
promoted_to_finding: finding-2026-05-28-FLASH-1200-0002
promoted_at: 2026-05-28T12:40:00-04:00
promoted_digraph: A2
promoted_run_id: flash-grade-20260528-120000
ttl_expires_at: 2026-08-26T12:19:00-04:00
flash_trigger_evaluation:
  trigger_6_zero_day_no_patch:
    matched: borderline
    no_patch: true_confirmed_via_rapid7_disclosure
    cvss_threshold_or_wide_deployment: wide_deployment_2400_plus_exposed_instances_per_shadowserver
    exploitation_confirmed_or_imminent: imminent_per_a_grade
    a_grade_source: rapid7_A
    notes: |
      Rapid7 disclosed; no patch since March 28 maintainer acknowledgment. Exploitation
      pre-condition (auth required) is trivially defeatable on Gogs instances that have
      open registration enabled by default — effectively pre-auth attack surface.
      Shadowserver tracks ~2,400 exposed Gogs instances; Shodan reports ~1,000 IPs
      with Gogs fingerprint (Asia and Europe primary). No confirmed in-wild exploitation
      of THIS specific zero-day per BleepingComputer; relays a previously-active
      CVE-2025-8110 as historical context. Trigger 6 requires
      "exploitation_confirmed_or_imminent per A-grade." Grader to decide whether
      Rapid7's disclosure + maintainer non-response (60+ days) + open-registration
      default qualifies as "imminent" exploitation. Hard Rule 3 — no PoC/exploit
      content extracted to raw-signal.
---

# New Gogs Zero-Day Flaw Lets Hackers Get Remote Code Execution

**Source:** BleepingComputer (relaying Rapid7's disclosure)
**Author:** Sergiu Gatlan
**Published:** 2026-05-28 10:25 EDT
**Originating researcher:** Jonah Burges, Rapid7

## Body

A zero-day argument-injection vulnerability in **Gogs**, the self-hosted Git service, allows registered users to obtain remote code execution on Internet-facing instances.

**Status:** No CVE assigned at disclosure time. No patch available. Rapid7 reported the flaw to Gogs maintainers on **2026-03-17**; maintainers acknowledged on 2026-03-28 but have released no fix. After ~60 days of vendor silence, Rapid7 disclosed.

**Affected versions:** 0.14.2 and 0.15.0+dev.

**Mechanism summary (no PoC):** The bug arises in pull-request rebase handling — malicious branch names are passed to `git rebase` operations during the "Rebase before merging" flow, enabling arbitrary command execution.

**Authentication pre-condition:** A registered Gogs user account is needed to trigger the flaw. **However, Gogs ships with open registration enabled by default**, so any unauthenticated attacker who can reach the instance can create an account and exploit it. Effective attack surface is unauthenticated for any default-config deployment.

**Impact (per Rapid7 via BleepingComputer):** Arbitrary remote code execution; full server compromise; ability to read every hosted repository; credential dump; lateral pivot into the Gogs server's network neighborhood.

**Install base:**
- Shadowserver tracks 2,400+ Internet-exposed Gogs instances
- Shodan finds 1,000+ IPs with Gogs fingerprint
- Geographic skew: Asia and Europe primary

**No confirmed in-wild exploitation of this specific zero-day.** A related Gogs vulnerability — CVE-2025-8110 — was actively exploited in past zero-day attacks; BleepingComputer cites it as historical context but does not claim CVE-2025-8110 = current flaw.

**A&D relevance (collector observation, not assessment):** Gogs is a self-hosted Git platform competitive with Gitea / GitLab / Forgejo in the DIB / engineering-team setting where ITAR / CMMC compliance prefers on-premise SCM. Effective unauthenticated RCE on a SCM is a high-impact developer-tooling exposure.

## Extraction notes

- Language: en
- Publisher byline: Sergiu Gatlan, BleepingComputer
- Article type: vulnerability-news
- Raw IOC extraction invoked: yes (limited — disclosure is product, not infrastructure)
- Hard Rule 3: NO exploit walkthrough or PoC content captured — refer to BleepingComputer URL for full technical detail.

## IOCs (from ioc-extraction skill)

```yaml
iocs:
  - indicator: gogs-argument-injection-rce-unassigned-CVE
    type: cve
    cvss: not_yet_assigned
    kev: false_at_sweep_time
    vendor: Gogs (open source self-hosted Git)
    product: Gogs
    affected_versions: ["0.14.2", "0.15.0+dev"]
    patch_available: false
    disclosure_path: rapid7_to_vendor_2026-03-17_then_public_2026-05-28
    exposure_signal:
      shadowserver_exposed_instances: 2400
      shodan_fingerprint_ips: 1000
    notes: "Effectively pre-auth on default deployments due to open registration."

attribution_claims:
  - source: Rapid7
    language: "Jonah Burges, Rapid7 senior security researcher, discovered and disclosed"
    actor_named: null
    nation_state_named: null
    confidence: vendor_disclosure_not_threat_attribution
    notes: "Disclosure source is the researcher; no threat-actor exploitation attribution."
```
