---
raw_id: raw-2026-05-04-test-flash-001
collected_at: 2026-05-04T14:00:00-04:00
run_id: session-9-stage-2-flash-test
collection_mode: test_seed
test: true
source:
  source_yaml_id: cisa-kev
  source_name: CISA Known Exploited Vulnerabilities Catalog
  source_url: https://www.cisa.gov/known-exploited-vulnerabilities-catalog/test-cve-2099-88888
  published_at: 2026-05-04T13:00:00-04:00
match_reason:
  watchlist: [aerospace-defense]
  actors: [APT34]
  vulnerabilities: [CVE-2099-88888]
  keywords: [zero-day, RCE, active exploitation, Lockheed, ITAR]
triage_tags: [cve, critical, ad_sector, test_data, flash_candidate]
flash_evaluation:
  cvss_score: 10.0
  exploitation_status: active
  source_grade: A
  tracked_actor_involved: true
  ad_watchlist_targeted: true
  patch_available: false
iocs_extracted: false
iocs_count: 0
text_word_count: 240
promoted: true
promoted_to_finding: finding-2026-05-04-flash-001
promoted_at: 2026-05-04T14:05:00-04:00
ttl_expires_at: 2026-05-11T14:00:00-04:00
---

# [TEST FLASH] CVE-2099-88888: Critical Pre-Auth RCE in Lockheed Skunk Works Avionics Test Bench, Active Exploitation by APT34

> **THIS IS SYNTHETIC TEST DATA.** Created for Session 9 Stage 2 FLASH
> pipeline verification. CVE-2099-88888 is a deliberately impossible CVE
> ID. The "Lockheed Skunk Works Avionics Test Bench" affected product is
> fictitious. The APT34 attribution is a controlled test scenario. Do
> NOT propagate to production channels, do NOT treat as real
> intelligence, do NOT publish to #flash-alerts or #intel-briefs.

CISA added CVE-2099-88888 to the Known Exploited Vulnerabilities Catalog
on 2026-05-04, requiring federal civilian executive branch agencies to
patch by 2026-05-25. The vulnerability is a critical pre-authentication
remote code execution flaw in the Lockheed Martin Skunk Works Avionics
Test Bench (model SKW-ATB-7), software versions 4.1 through 4.7.2,
deployed at multiple ITAR-regulated aircraft programs.

**Severity:** CVSS v4.0 base score 10.0 (Critical Maximum). Network
attack vector, low complexity, no privileges or user interaction. The
test bench's diagnostic API on TCP/9443 fails to validate session
tokens before processing diagnostic-mode escalation requests, granting
the attacker full root on the underlying RHEL system.

**Exploitation status:** Mandiant published a same-day blog attributing
active exploitation to **APT34 (OilRig)** as part of an Iran-aligned
campaign targeting US aerospace primes. The campaign uses CVE-2099-88888
as the initial access vector, followed by the MENORAH backdoor for
persistence. Mandiant attributes with high confidence based on
infrastructure overlap with prior APT34 operations (per Mandiant's
attribution; not originated by Archimedes).

**Patch status:** Lockheed Martin has not yet released a fix. CISA
recommends emergency network isolation of the SKW-ATB-7 management VLAN
and TCP/9443 ingress monitoring until a patch is available.

**FLASH trigger evaluation:**
- `critical-cve-exploited`: cvss 10.0 ≥ 9.0 ✓, active exploitation ✓, source A-grade ✓ → **FIRES**
- `tracked-actor-attribution`: new attribution ✓, tracked actor (APT34, #023) ✓ → **FIRES**
- Override condition (cvss_10 + active + tracked_actor + ad_watchlist): all four ✓ → **bypass quiet hours** (not relevant in active hours)

## Extraction notes

- Language: en
- Publisher byline: CISA + Mandiant (cross-source)
- Article type: KEV catalog entry + vendor blog
- Raw IOC extraction invoked: no (test seed; production extraction would pull MENORAH IOCs from Mandiant report)

## IOCs (from ioc-extraction skill)

(None — synthetic test seed. A production trigger of this kind would
include APT34 infrastructure indicators, MENORAH file hashes, and
Lockheed-specific artifacts.)
