---
raw_id: raw-2026-05-08-am-001
collected_at: 2026-05-08T07:32:00-04:00
run_id: pre-brief-20260508-073000
collection_mode: pre_brief_collection
test: false
sources:
  - source_yaml_id: bleepingcomputer
    source_name: "BleepingComputer (Sergiu Gatlan)"
    source_url: https://www.bleepingcomputer.com/news/security/new-linux-dirty-frag-zero-day-with-poc-exploit-gives-root-privileges/
    source_grade_estimated: B
    role: originating
    published_at: 2026-05-08T07:45:24+00:00
    note: |
      New Linux kernel local privilege escalation zero-day named
      "Dirty Frag," disclosed by researcher Hyunwoo Kim (@v4bel) on
      2026-05-07. Affects Ubuntu, RHEL, CentOS Stream, AlmaLinux,
      openSUSE Tumbleweed, Fedora — i.e., effectively all major
      enterprise Linux distros. Flaw is approximately nine years old,
      living in the algif_aead cryptographic interface. No CVE
      assigned at publication time. NO PATCH available. Public PoC
      published on github.com/V4bel/dirtyfrag after embargo broken
      by an unrelated third party. NOT yet observed in active
      exploitation. Mitigation by disabling esp4/esp6/rxrpc kernel
      modules breaks IPsec VPNs and AFS file systems — operationally
      painful for many environments.
publish_window: { start: 2026-05-07T17:30:00-04:00, end: 2026-05-08T07:30:00-04:00 }
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: ["dirty-frag-pending-cve"]
  keywords: [linux, lpe, local-privilege-escalation, zero-day, kernel, algif_aead, dirty-frag, public-poc, no-patch, ubuntu, rhel, centos-stream, alma-linux, opensuse, fedora, ipsec]
triage_tags: [zero_day_no_patch, public_poc_available, broad_platform_impact, lpe, kernel_vuln, awaiting_cve_assignment, awaiting_corroboration]
flash_trigger_evaluation:
  trigger_6_zero_day_no_patch:
    evaluation: |
      Disclosure without patch: TRUE (no patches at publication time).
      CVSS >= 8.0 OR widely-deployed product: TRUE on the second prong
      (six major Linux distros — clearly widely-deployed).
      Exploitation confirmed or imminent per A-grade: NOT YET. Article
      explicitly states "not actively exploited in-the-wild at
      publication." However, public deterministic PoC on GitHub +
      no race condition + nine-year-old vulnerable code path = high
      probability of imminent exploitation. SANS ISC (B-grade) has
      independent corroboration in the same window (raw-2026-05-08-am-002).
      No A-grade source has surfaced exploitation yet.
    decision: not_triggered_at_collection
    rationale: |
      Trigger 6 requires "exploitation confirmed OR exploitation imminent
      per A-grade source." We have only B-grade corroboration (BleepingComputer
      + SANS ISC), and neither claims active exploitation. Pre-staged for
      grader morning consideration with high prominence — this is the kind
      of item that should be lead-tier in the 08:00 morning brief regardless
      of FLASH non-trigger, and that warrants a watch-cadence on Trigger 6
      should an A-grade source surface in-the-wild observation.
iocs_extracted: true
iocs_count: 0
text_word_count: 480
publication_window_match: in_window
promoted: true
promoted_to_finding: finding-2026-05-08-0001
promoted_at: 2026-05-08T08:08:00-04:00
ttl_expires_at: 2026-08-06T07:32:00-04:00
---

# Linux "Dirty Frag" zero-day LPE — public PoC, no patch, all major distros

## Source summary

BleepingComputer (Sergiu Gatlan, 2026-05-08 07:45 UTC) reports that
security researcher Hyunwoo Kim (@v4bel) disclosed on 2026-05-07 a
new Linux kernel local privilege escalation flaw named **Dirty Frag**.
The flaw lives in the kernel's `algif_aead` cryptographic algorithm
interface, was introduced approximately nine years ago, and chains
two separate kernel weaknesses to modify protected system files in
memory without authorization. The exploit targets the fragment field
of a kernel data structure (hence "Frag"), distinguishing it from
the conceptually related Dirty Pipe (CVE-2022-0847) and the recently
disclosed Copy Fail (CVE-2026-31431) which BleepingComputer references
as having been disclosed less than two weeks earlier.

## Affected platforms

Per the article, **all major Linux distributions** are affected:

- Ubuntu
- Red Hat Enterprise Linux
- CentOS Stream
- AlmaLinux
- openSUSE Tumbleweed
- Fedora

Effectively the entire enterprise Linux estate. The vulnerable code
path has been present for ~9 years.

## Patch status

**No patches available at time of publication.** Mitigation is
manual: disable `esp4`, `esp6`, and `rxrpc` kernel modules. This
mitigation **breaks IPsec VPNs and AFS file systems** — operationally
painful for any environment using site-to-site IPsec or AFS, which
includes many enterprise and research environments.

## PoC and exploitation status

**Public PoC** is available on GitHub at github.com/V4bel/dirtyfrag.
The article states the embargo was broken by an unrelated third party,
prompting public release.

**NOT yet observed in active in-the-wild exploitation** per the
article. However the article emphasizes the exploit is **deterministic
with high success rate and no race condition required** — which
removes the most common practical barriers to weaponization.

## CVE / CVSS

- **CVE: not yet assigned** at publication time
- **CVSS: not stated** in article

## Significance for grader

1. **Trigger-6 not fired at collection** — A-grade source has not
   surfaced active exploitation. SANS ISC corroboration in same
   window (raw-2026-05-08-am-002) is B-grade independent.
2. **High morning-brief prominence regardless** — public deterministic
   PoC + zero patch + entire enterprise Linux footprint = unusually
   high near-term exploitation probability. This is the lead-tier
   item in this collection window.
3. **Watch signal:** any A-grade source (Mandiant, Unit 42, MSTIC,
   CrowdStrike, CISA, NVD entry with active exploitation indicator)
   surfacing in-the-wild observation flips this to Trigger-6 FLASH.
4. **A&D defensive relevance:** any A&D contractor running Linux
   workstations, build infrastructure, or Linux-based ICS/embedded
   firmware test rigs is exposed. Mitigation cost is high (IPsec
   breakage). Even without explicit A&D-victim signal, defensive
   value of inclusion in the morning brief is high.
5. **Carrier vs novel:** this is a NEW vulnerability disclosure,
   not a re-report of an existing CVE. Distinct from CVE-2026-31431
   (Copy Fail) referenced in same article.

---

## Extraction notes

- Language: en
- Publisher byline: Sergiu Gatlan (BleepingComputer)
- Article type: blog/news
- Raw IOC extraction invoked: yes (zero IOCs to extract; no IPs,
  domains, hashes, or URLs of malicious nature in article)
- One technical reference URL surfaces: github.com/V4bel/dirtyfrag
  (PoC repository — research artifact, not a malicious indicator;
  not promoted as IOC)
- No attribution claims made in article (vulnerability research
  disclosure, not a campaign report)

## IOCs (from ioc-extraction skill)

```yaml
iocs: []
attribution_claims: []
notes: |
  Vulnerability-disclosure article. No threat actor named. No
  malicious IPs, domains, or hashes referenced. The github.com/V4bel/dirtyfrag
  URL is the disclosing researcher's own PoC repo — research
  artifact, not an IOC. Vulnerability identifier "Dirty Frag" is
  the researcher-assigned name; CVE not yet assigned.
```
