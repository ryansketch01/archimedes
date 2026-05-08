---
raw_id: raw-2026-05-08-am-004
collected_at: 2026-05-08T07:35:00-04:00
run_id: pre-brief-20260508-073000
collection_mode: pre_brief_collection
test: false
sources:
  - source_yaml_id: securityweek
    source_name: "SecurityWeek (Ionut Arghire)"
    source_url: https://www.securityweek.com/pcpjack-worm-removes-teampcp-infections-steals-credentials/
    source_grade_estimated: B
    role: relay
    published_at: 2026-05-08T08:32:34+00:00
    note: |
      SecurityWeek (Ionut Arghire, 2026-05-08 08:32 UTC) reports
      SentinelOne research naming **PCPJack** as a worm framework
      that actively removes TeamPCP (roster id 001) tools and
      artifacts before deploying its own malware. SentinelOne
      hypothesizes PCPJack operator "could be a former operator
      who is deeply familiar with the group's tooling," noting
      similarities to early TeamPCP/PCPCat campaigns from December
      2025. Net-new beyond BleepingComputer's 2026-05-07 PCPJack
      coverage (raw-2026-05-07-flash-1800-003): SentinelOne is
      the *originating* research source (BleepingComputer was a
      news relay); SentinelOne adds **CVE list of exploited
      vulnerabilities** (5 CVEs spanning Next.js, React2Shell,
      WPVivid, W3 Total Cache, CentOS Web Panel) and **target
      environment list** (AWS, Docker, Kubernetes, Redis, RayML,
      MongoDB), plus the "former operator" attribution hypothesis.
sentinelone_originating_research:
  vendor: SentinelOne
  source_grade_estimated: A
  note: |
    SecurityWeek explicitly names SentinelOne as the discoverer
    and analyst of PCPJack. SentinelOne is a Tier-1 vendor
    historically in the same A-grade band as CrowdStrike / Unit 42
    / Mandiant (not yet listed in source-grades.yaml — provisional
    flag for librarian / human review). Independence test: SentinelOne
    is the originating researcher; SecurityWeek and BleepingComputer
    are both relays. Need to fetch the SentinelOne primary report
    for grading-grade evidence — attempted at collection but
    SentinelOne URL not surfaced in the SecurityWeek article body
    extracted by WebFetch. Flag for grader: chase the SentinelOne
    primary URL during morning grading run.
publish_window: { start: 2026-05-07T17:30:00-04:00, end: 2026-05-08T07:30:00-04:00 }
match_reason:
  watchlist: []
  actors: ["001"]    # TeamPCP
  vulnerabilities:
    - CVE-2025-29927    # Next.js
    - CVE-2025-55182    # React2Shell
    - CVE-2026-1357     # WPVivid
    - CVE-2025-9501     # W3 Total Cache
    - CVE-2025-48703    # CentOS Web Panel
  keywords: [pcpjack, teampcp, sentinelone, cybercriminal-rivalry, worm, cloud-native-worm, aws, docker, kubernetes, redis, rayml, mongodb, credential-theft, former-operator-hypothesis, linux-shell-script, python-virtualenv, s3-payload-staging]
triage_tags:
  - tracked_actor_activity
  - inter_threat_actor_displacement
  - cybercriminal_rivalry
  - cloud_native_targeting
  - originating_a_grade_vendor_research
  - awaiting_primary_source_url
  - sentinelone_provisional_grade_a
flash_trigger_evaluation:
  trigger_4_tracked_actor_ttp_change:
    evaluation: |
      Trigger 4 requires (a) new tooling/targeting/infrastructure,
      (b) A/B-grade source, (c) attributable to a tracked actor.
      PCPJack is genuinely net-new tooling that *interacts with*
      TeamPCP — but the article's attribution hypothesis ("could
      be a former operator") is exactly that, a hypothesis, not a
      claim that TeamPCP itself shifted TTPs. The actor-on-actor
      displacement story is unusual and grader-relevant, but
      Trigger 4 reads "tracked actor TTP change," and PCPJack is
      a *separate* threat that *removes* TeamPCP infections — not
      TeamPCP changing tools. Strict reading: not triggered.
    decision: not_triggered
    rationale: |
      Inter-actor cybercriminal displacement story; should be
      lead-tier coverage in 08:00 morning brief but does not meet
      Trigger 4 strict construction. Anti-noise also applies — same
      PCPJack/TeamPCP topic was covered in 18:00 FLASH 2026-05-07
      (raw-2026-05-07-flash-1800-003). The SentinelOne attribution
      hypothesis IS net-new beyond that prior coverage and warrants
      an update_history entry on any TeamPCP / PCPJack finding.
  trigger_2_tracked_actor_attribution:
    evaluation: |
      Trigger 2 requires NEW attribution to a tracked actor. The
      "former TeamPCP operator" hypothesis is a SentinelOne-stated
      possibility, not a confirmed attribution. SentinelOne uses
      hedged language ("could be"). Hard Rule 2 (no novel
      attribution origination) means Archimedes cannot upgrade
      "could be" to "is." 
    decision: not_triggered
    rationale: |
      Hedged, source-stated hypothesis — not corroborated, not
      confirmed. Record verbatim with source's confidence
      language; do NOT promote to attribution.
iocs_extracted: true
iocs_count: 5
text_word_count: 290
publication_window_match: in_window
promoted: true
promoted_to_finding: finding-2026-05-08-0003
promoted_at: 2026-05-08T08:18:00-04:00
ttl_expires_at: 2026-08-06T07:35:00-04:00
---

# PCPJack worm — SentinelOne attribution hypothesis names "former TeamPCP operator"; CVE chain disclosed

## Source summary

SecurityWeek (Ionut Arghire, 2026-05-08 08:32 UTC) reports
SentinelOne research on a worm framework named **PCPJack** that
**actively removes TeamPCP infections** from compromised systems
before deploying its own credential-stealing payload.

This is SecurityWeek's relay of SentinelOne's primary research.
SentinelOne (Tier-1 vendor; provisional A-grade pending source
list addition) is the originating analyst. BleepingComputer
covered the story 2026-05-07 (raw-2026-05-07-flash-1800-003) as
a separate news relay.

## Net-new beyond 2026-05-07 BleepingComputer coverage

1. **SentinelOne explicitly named as originating researcher.** Prior
   raw-signal noted "SentinelOne possibly originating" — now
   confirmed.

2. **Attribution hypothesis: "former TeamPCP operator."** SentinelOne
   notes the threat actor "could be a former operator who is deeply
   familiar with the group's tooling," citing similarities to early
   TeamPCP/PCPCat campaigns from December 2025. Hedged language —
   "could be," not "is." Hard Rule 2 applies (Archimedes does not
   originate or upgrade attribution).

3. **Five exploited CVEs disclosed** (the kill-chain initial access
   vectors PCPJack uses):
   - CVE-2025-29927 — Next.js
   - CVE-2025-55182 — React2Shell
   - CVE-2026-1357 — WPVivid (WordPress backup plugin)
   - CVE-2025-9501 — W3 Total Cache (WordPress)
   - CVE-2025-48703 — CentOS Web Panel

4. **Six target environments** (cloud-native focus):
   - AWS, Docker, Kubernetes, Redis, RayML, MongoDB

5. **Detailed kill-chain mechanics:**
   - Linux shell script for initial environment setup
   - Payload fetch from AWS S3 (six modules)
   - Python virtual environment creation
   - TeamPCP infection scan and removal
   - Persistence + orchestrator launch
   - Credential theft (SSH keys, .env files, AWS creds, K8s
     tokens, Docker creds, GitHub, Gmail, Office 365, Slack,
     WordPress)
   - Lateral movement, system recon, self-propagation

## Significance for grader

1. **Inter-threat-actor cybercriminal displacement** is the unusual
   feature. PCPJack actively cleans up rivals before deploying.
   This is a notable evolution of cybercriminal cloud-targeting
   ecosystem behavior.

2. **TeamPCP roster impact:** PCPJack erodes TeamPCP's installed
   base. TeamPCP remains in roster as actor 001, threat_level
   HIGH, but actor-profiler should evaluate whether PCPJack
   displacement reduces TeamPCP's near-term operational footprint.

3. **Source independence:** SecurityWeek (today) + BleepingComputer
   (2026-05-07) both relay SentinelOne. Independence test fails
   for the *attribution hypothesis* — only SentinelOne carries it.
   The procedural facts (PCPJack exists, kills TeamPCP, uses these
   CVEs) are now corroborated across two B-grade relays of one
   A-grade-equivalent originating source.

4. **A&D relevance:** Cloud-native dev/build infrastructure
   targeting (AWS, Docker, K8s) is squarely in scope for any A&D
   contractor running modern DevSecOps pipelines. Five exploited
   CVEs are in widely-deployed open-source components — patch
   posture across the supply chain matters.

5. **Action item for grader:** chase the SentinelOne primary URL
   during morning grading run for full IOC list (the
   SecurityWeek-extracted body did not surface IOCs but the
   SentinelOne primary likely does).

---

## Extraction notes

- Language: en
- Publisher byline: Ionut Arghire (SecurityWeek)
- Article type: blog/news (relay of SentinelOne research)
- Raw IOC extraction invoked: yes
- 5 CVEs extracted; 0 IPs/domains/hashes/URLs of malicious
  nature in the SecurityWeek article body
- SentinelOne primary report URL not surfaced by WebFetch
  extraction — flag for follow-up

## IOCs (from ioc-extraction skill)

```yaml
iocs:
  - type: cve
    value: CVE-2025-29927
    role: initial_access_exploited_by_pcpjack
    affected_product: Next.js
    note: "Listed by SentinelOne as one of five CVEs PCPJack exploits for initial access"
  - type: cve
    value: CVE-2025-55182
    role: initial_access_exploited_by_pcpjack
    affected_product: React2Shell
  - type: cve
    value: CVE-2026-1357
    role: initial_access_exploited_by_pcpjack
    affected_product: WPVivid (WordPress plugin)
  - type: cve
    value: CVE-2025-9501
    role: initial_access_exploited_by_pcpjack
    affected_product: W3 Total Cache (WordPress plugin)
  - type: cve
    value: CVE-2025-48703
    role: initial_access_exploited_by_pcpjack
    affected_product: CentOS Web Panel
attribution_claims:
  - actor: "PCPJack operator (unnamed)"
    actor_id: null
    relationship_to_tracked_actor: TeamPCP (roster 001) — claimed displacement
    confidence_language: '"could be a former operator who is deeply familiar with the group's tooling"'
    originating_source: SentinelOne (vendor research)
    relay_chain: SentinelOne -> SecurityWeek (2026-05-08 08:32 UTC) AND SentinelOne -> BleepingComputer (2026-05-07)
    novel_to_archimedes_corpus: true
    note: |
      Hedged hypothesis. Hard Rule 2 prevents upgrade. Recordable as
      a single-source attribution claim with explicit "could be"
      qualifier. Grader: log per attribution standards in
      LEGAL-POLICY §Attribution Standards.
notes: |
  Initial-access CVE chain captured. PCPJack-specific IOCs (IPs,
  hashes, S3 URLs hosting payload modules) not surfaced in the
  SecurityWeek body — likely present in the SentinelOne primary
  report which the collector could not reach via WebFetch in this
  pass. Recommend re-fetch by grader/morning run.
```
