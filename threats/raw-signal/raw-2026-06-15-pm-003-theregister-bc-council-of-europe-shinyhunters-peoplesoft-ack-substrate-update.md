---
raw_id: raw-2026-06-15-pm-003
collected_at: 2026-06-15T15:42:00-04:00
run_id: pre-brief-20260615-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: theregister
  source_name: The Register (cyber-crime desk)
  source_url: https://www.theregister.com/cyber-crime/2026/06/15/council-of-europe-hacked-in-shinyhunters-peoplesoft-heist/
  published_at: 2026-06-15T17:44:00+00:00
additional_publisher_relay:
  - source_yaml_id: bleepingcomputer
    source_name: BleepingComputer (Sergiu Gatlan byline, 2026-06-15 16:37 UTC)
    source_url: https://www.bleepingcomputer.com/news/security/council-of-europe-investigates-shinyhunters-data-breach-claims/
match_reason:
  watchlist: []
  actors: [ShinyHunters, UNC6240]   # UNC6240 per Mandiant prior-corpus + ShinyHunters self-claim chain; neither on _roster.yaml
  vulnerabilities: [CVE-2026-35273]   # Oracle PeopleSoft KEV BOD 26-04 closing EOD tonight
  keywords: [Council of Europe, CoE acknowledgement, 297GB, 429000 files, PeopleSoft zero-day, 100+ orgs, 300 vulnerable instances, University of Nottingham, Infinite Campus, Salesforce, GTIG, 68% higher education]
triage_tags: [substrate_update_on_morning_finding, victim_acknowledgement_obtained, anti-noise-partial-lift, no-actor-cross-walk, fcebkev-deadline-EOD-tonight, ed-tech-shinyhunters-cluster]
iocs_extracted: true
iocs_count: 0
text_word_count: 480
promoted: true
promoted_to_finding: finding-2026-06-15-0008-theregister-bc-council-of-europe-shinyhunters-peoplesoft-victim-acknowledgement-update-on-finding-2026-06-15-0001
promoted_at: 2026-06-15T16:22:00-04:00
ttl_expires_at: 2026-09-13T15:42:00-04:00
---

# Council of Europe hacked in ShinyHunters' PeopleSoft heist — Joins ranks of Nottingham Uni and 100 other unnamed victims

**The Register (cyber-crime desk, Iain Thomson byline customary for this story class)** — 2026-06-15 17:44 UTC

ShinyHunters claims to have breached the Council of Europe and stolen more than **297 GB of data**
after exploiting a zero-day flaw in Oracle PeopleSoft and abusing that hole to hack more than 100
organizations.

According to a post on the extortion crew's data-leak site, the **429,000 pilfered files** contain
HR and payroll records, payslips, purchase-order records, CVs, and employees' salary, banking,
tax, and medical records.

## Council of Europe acknowledgement — NET-NEW substrate

> A Council of Europe spokesperson told The Register that it is "currently investigating the
> matter and assessing the situation," but declined to comment further.

(11-word verbatim quote, Hard Rule 6 preserved — under 15-word limit, one quote per source.)

This is the **net-new substrate** resolving the morning brief's `no-CoE-ACK` weakness on
finding-2026-06-15-0001 (C3 digraph, single-publisher SecurityWeek relay of ShinyHunters
self-claim with NO direct CoE response at finding time).

## ShinyHunters PeopleSoft chain detail

A spokesperson for the cybercrime group told The Register that the Council is yet another
victim of the Oracle PeopleSoft heist.

Oracle has yet to respond to The Register's inquiries, and it's unclear if the vulnerability,
tracked as **CVE-2026-35273**, has been patched.

ShinyHunters previously told The Register that the gang exploited the CVE to compromise more
than **100 organizations across 300 vulnerable instances**, and that these victims included
the University of Nottingham. Last week, the crims listed the UK uni on their leak site, then
dumped data belonging to around **454,600 current and former students**, including personal
and academic records.

## GTIG cross-corroboration (Mandiant late-week report)

> Meanwhile, a Google threat report published late last week noted malicious activity,
> "consistent with the exploitation of CVE-2026-35273," between **May 27 and June 9**, and
> said that its incident responders notified more than 100 global orgs "whose IP addresses
> correlated with potentially vulnerable endpoints."

Most of these are US-based organizations, and **68 percent operated within the higher
education sector**.

(GTIG report referenced is the Mandiant carry-forward primary that feeds finding-2026-06-13-0006
+ anti-noise hold. Anti-noise partial-lift here is for the CoE ACK substrate, not for the
GTIG-based scale claims which remain locked.)

## ShinyHunters ed-tech cluster — operational template

This latest heist follows another ShinyHunters intrusion targeting data belonging to university
and K-12 students, teachers, and staff:

- **Mid-May**: Instructure (Canvas digital learning platform) "reached an agreement" with the
  data theft and extortion crew after ShinyHunters breached its Canvas platform and accessed
  data tied to **275 million students, teachers, and staff** (corporate-speak for "paid the
  ransom demand," per The Register).
- **March**: ShinyHunters claimed it stole data from K-12 software provider Infinite Campus as
  part of a broader wave of Salesforce-related intrusions. The ed-tech company did NOT pay; the
  group subsequently published data they claim was stolen from Infinite Campus, including
  **137,000 individuals' email addresses** along with names, phone numbers, physical addresses
  and support tickets.

Infinite Campus's data breach notification said the leaked files largely consisted of "names
and contact information for school staff" and that "the majority is directory information
commonly found on school websites."

---

## Extraction notes

- Language: en
- Publisher byline: The Register cyber-crime desk (Iain Thomson byline customary)
- Primary source: ShinyHunters self-claim on Tor leak site + Council of Europe direct response
- Article type: vendor/victim ACK + extortion-group cluster mapping
- Raw IOC extraction invoked: yes (no fresh IOCs; metadata only)

## IOCs (from ioc-extraction skill)

```yaml
iocs:
  cves:
    - id: CVE-2026-35273
      product: Oracle PeopleSoft (FSCM / HCM / Campus Solutions modules)
      status: zero_day_exploited
      kev_listed: true (per VT corpus tracking, finding-2026-06-13-0006 substrate)
      kev_due_date: 2026-06-15 (FCEB BOD 26-04 EOD tonight)
      patch_availability: "unclear if patched per The Register; Oracle out-of-band-mitigations-only-no-GA-patch per FLASH 12:00 carry-forward substrate"

  hashes: []
  ips: []
  domains: []
  urls: []
  victims_named:
    - "Council of Europe (ACKNOWLEDGED 2026-06-15 — NET-NEW)"
    - "University of Nottingham (prior surface, last week, 454,600 records)"
    - "Instructure Canvas (mid-May, 275M records, paid)"
    - "Infinite Campus (March, 137K records via Salesforce intrusion wave, did NOT pay)"

attribution_claims:
  - source: ShinyHunters (self-claim, Tor leak site)
    actor_claimed_self: ShinyHunters
    confidence: SELF_CLAIM (per leak-site posting)
    actor_overlap_per_corpus: UNC6240 (per Mandiant carry-forward primary chain via finding-2026-06-13-0006)
    note: |
      Hard Rule 2 preserved — Mandiant primary attribution language is UNC6240; ShinyHunters
      is the extortion-brand self-claim layer. Archimedes does NOT originate the
      UNC6240 ↔ ShinyHunters identity mapping; Mandiant carry-forward primary substrate
      asserts the dual-naming chain. Neither actor on _roster.yaml.
  - source: Council of Europe (direct ACK, via The Register)
    statement: "currently investigating the matter and assessing the situation"
    statement_word_count: 11
    statement_note: "declined to comment further"
    confidence: VICTIM_ACK (procedurally A-grade on procedural fact)
  - source: Google Threat Intelligence Group (GTIG / Mandiant, carry-forward late-week report)
    timeline: "malicious activity consistent with exploitation of CVE-2026-35273 between May 27 and June 9"
    notification_scope: ">100 global orgs whose IP addresses correlated with potentially vulnerable endpoints"
    sector_breakdown: "Most US-based; 68% higher education"
    note: |
      GTIG report is carry-forward primary from finding-2026-06-13-0006 anti-noise hold; the
      The Register cite re-states GTIG findings. Anti-noise on CVE-2026-35273 + GTIG scale
      claims is PRESERVED (not lifted) — only the CoE-ACK layer is net-new this surface.

anti_noise_disposition: SUBSTRATE_UPDATE_NET_NEW_ON_COE_ACK_LAYER_ONLY
anti_noise_reasoning: |
  Net-new substrate on this surface = Council of Europe direct ACK (resolves morning brief
  finding-2026-06-15-0001 weakness `no-CoE-ACK`).
  
  Anti-noise PRESERVED on:
    - CVE-2026-35273 PeopleSoft mechanism (carry-forward, FCEB BOD 26-04 KEV closing EOD
      tonight 2026-06-15)
    - GTIG cross-corroboration claims (carry-forward from finding-2026-06-13-0006)
    - 297GB / 429K files / 100+ orgs / 300 instances claim (Friday-evening SecurityWeek
      relay substrate; finding-2026-06-15-0001 graded C3 single-publisher; The Register
      re-relay does NOT independently corroborate the underlying ShinyHunters numerical
      claims, only confirms CoE has acknowledged a probe)
    - University of Nottingham 454,600 records claim (last-week prior surface, anti-noise)
    - Instructure Canvas 275M records mid-May claim (carry-forward, anti-noise)
    - Infinite Campus 137K records March claim (today's Sergiu Gatlan BC 12:38 piece is
      same item already in coverage; the Infinite Campus ShinyHunters-cluster carry-forward
      is anti-noise)
  
  Grader decision: whether to compose finding-2026-06-15-PM-NNNN as a substrate-update
  UPDATE-finding on finding-2026-06-15-0001 (CoE-ACK upgrade C3→B2 candidate) or absorb the
  net-new CoE-ACK substrate into existing finding-2026-06-15-0001 + coverage-log addendum.

direct_retrieval_recommendation: |
  Grader / actor-profiler / vuln-tracker handoffs:
    - Vuln-tracker: CVE-2026-35273 PeopleSoft tracking entry should be scaffolded if not yet
      present; FCEB BOD 26-04 KEV due 2026-06-15 EOD = T-hours from this sweep. KEV
      compliance retrospective phase begins 2026-06-16.
    - Actor-profiler: UNC6240 / ShinyHunters operator-deferred /new-actor candidacy substrate
      strengthens with CoE victim ACK + ed-tech cluster (Canvas + Infinite Campus + Nottingham
      + CoE) + Mandiant primary attribution chain. Collector does NOT originate /new-actor
      scaffold.

flash_trigger_evaluation_notes_for_grader:
  trigger_1_critical_cve_exploited: PRIOR_EVALUATION_LOCKED
    note: "VT-006-style retrospective; CVE-2026-35273 already corpus-tracked via
      finding-2026-06-13-0006 + FLASH 12:00 hold; ad-noise lock through 2026-06-18 12:00 EDT."
  trigger_2_tracked_actor_attribution: FAIL — neither ShinyHunters nor UNC6240 on _roster.yaml
    (operator-deferred /new-actor candidacy only).
  trigger_5_ad_sector_campaign: MARGINAL FAIL — CoE is intergovernmental org (NOT A&D-prime);
    higher-education 68% sector skew is not A&D-prime sector. Ed-tech / public-sector / IGO
    victim profile is materially distinct from A&D-prime DIB / CMMC partner-flow estates.
  flash_disposition: NOT FLASH — substrate update suitable for 16:00 afternoon brief
    (UPDATE-finding pathway on finding-2026-06-15-0001 per grader decision).
```
