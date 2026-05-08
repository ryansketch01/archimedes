---
raw_id: raw-2026-05-08-am-002
collected_at: 2026-05-08T07:33:00-04:00
run_id: pre-brief-20260508-073000
collection_mode: pre_brief_collection
test: false
sources:
  - source_yaml_id: sans-isc
    source_name: "SANS Internet Storm Center (Diary)"
    source_url: https://isc.sans.edu/diary/rss/32968
    source_grade_estimated: B
    role: corroborating
    published_at: 2026-05-08T07:50:01+00:00
    note: |
      SANS ISC handler diary published 2026-05-08 07:50 UTC titled
      "Another Universal Linux Local Privilege Escalation (LPE)
      Vulnerability: Dirty Frag." Independent B-grade confirmation
      of the Dirty Frag disclosure also reported by BleepingComputer
      (raw-2026-05-08-am-001). The ISC diary frames it explicitly as
      a follow-up to the recent Copy Fail (CVE-2026-31431) disclosure,
      reaffirms the LPE classification, and promises mitigation
      guidance in the body. Independence test: ISC handler authored
      a fresh diary post (not a relay of BleepingComputer); both
      cite the original disclosure by Hyunwoo Kim (@v4bel). Two
      independent B-grade sources covering the same disclosure-day
      window — meaningful for grader corroboration math.
publish_window: { start: 2026-05-07T17:30:00-04:00, end: 2026-05-08T07:30:00-04:00 }
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: ["dirty-frag-pending-cve"]
  keywords: [linux, lpe, kernel, dirty-frag, copy-fail, cve-2026-31431, sans-isc, mitigation-guidance]
triage_tags: [zero_day_no_patch, corroborating_b_grade, second_b_source_same_day, kernel_vuln, awaiting_cve_assignment]
flash_trigger_evaluation:
  trigger_6_zero_day_no_patch:
    evaluation: |
      Same as raw-2026-05-08-am-001: Trigger 6 not fired because
      no A-grade source has surfaced exploitation. SANS ISC reaches
      B-grade per source-grades.yaml. Two B-grade sources do not
      promote to A under the doctrine. Maintain watch-cadence.
    decision: not_triggered_at_collection
iocs_extracted: true
iocs_count: 0
text_word_count: 90
publication_window_match: in_window
promoted: true
promoted_to_finding: finding-2026-05-08-0001
promoted_at: 2026-05-08T08:08:00-04:00
ttl_expires_at: 2026-08-06T07:33:00-04:00
---

# SANS ISC corroborates Dirty Frag Linux LPE disclosure (independent B-grade)

## Source summary

SANS Internet Storm Center handler diary, 2026-05-08 07:50 UTC,
titled "Another Universal Linux Local Privilege Escalation (LPE)
Vulnerability: Dirty Frag, (Fri, May 8th)." Body excerpt from the
RSS feed:

> Less than two weeks after the public disclosure of the Copy Fail
> vulnerability (CVE-2026-31431), another local privilege escalation
> (LPE) vulnerability in the Linux kernel has been revealed.
> Referred to as "Dirty Frag," this vulnerability was discovered
> and reported by Hyunwoo Kim (@v4bel) [1]. In this diary, I will
> provide a brief background on Dirty Frag, and discuss its
> relationship to Copy Fail. I will then discuss how to mitigate
> Dirty Frag and outline recommended next steps for system owners.

(89 words quoted from the RSS summary; ISC diary intro material —
the full body lives behind the diary URL, not in the RSS summary.
Briefer should re-cite under 15-word rule.)

## Independence assessment

- ISC handler authored a fresh diary post, not a relay of
  BleepingComputer.
- Both BleepingComputer and ISC cite the original disclosure by
  Hyunwoo Kim (@v4bel) — i.e., they share the underlying primary
  source (the researcher's disclosure), but neither is downstream
  of the other.
- This satisfies the grader's "two independent secondary sources"
  bar at B-grade for the underlying procedural facts (existence
  of disclosure, named researcher, LPE classification, kernel
  origin), though it does NOT clear the A-grade bar required for
  Trigger-6 active-exploitation FLASH.

## Significance for grader

1. **Procedural-fact corroboration** — disclosure existence,
   researcher identity, LPE class, no-patch posture: now have two
   independent B-grade sources.
2. **Operational-claim corroboration (exploitation)** — neither
   source claims in-the-wild exploitation. Status remains "public
   PoC, no observed exploitation." No FLASH escalation.
3. **Anti-noise:** treat raw-2026-05-08-am-001 and -am-002 as a
   coupled pair — single morning-brief topic, two-source citation,
   not two separate stories.

---

## Extraction notes

- Language: en
- Publisher byline: SANS ISC handler (RSS does not surface byline
  in the feed item; full diary at the URL would have author)
- Article type: handler diary (technical analysis)
- Raw IOC extraction invoked: yes (RSS summary only — no IOCs
  surfaced; diary body may contain mitigation commands but no
  malicious indicators)

## IOCs (from ioc-extraction skill)

```yaml
iocs:
  - type: cve
    value: CVE-2026-31431
    role: contextual_reference
    note: "Copy Fail — referenced as the prior LPE in the same kernel-vuln cluster, not the Dirty Frag CVE itself. Dirty Frag has no CVE yet."
attribution_claims: []
notes: |
  Disclosure-corroboration item. No threat actor referenced. The
  CVE-2026-31431 reference is contextual — "Dirty Frag follows Copy
  Fail" — and is not the Dirty Frag identifier.
```
