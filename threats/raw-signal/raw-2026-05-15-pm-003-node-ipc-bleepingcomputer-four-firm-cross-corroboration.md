---
raw_id: raw-2026-05-15-pm-003
collected_at: 2026-05-15T15:43:00-04:00
run_id: pre-brief-20260515-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: bleepingcomputer
  source_name: "BleepingComputer"
  source_url: https://www.bleepingcomputer.com/news/security/popular-node-ipc-npm-package-compromised-to-steal-credentials/
  published_at: 2026-05-15T17:10:42+00:00
  byline: "Bill Toulas"
secondary_sources:
  - source_yaml_id: socket
    source_name: "Socket"
    relay_type: cited_by_bleepingcomputer
  - source_yaml_id: stepsecurity
    source_name: "StepSecurity"
    relay_type: cited_by_bleepingcomputer_and_yesterday_pm_005
  - source_yaml_id: ox-security
    source_name: "Ox Security"
    relay_type: cited_by_bleepingcomputer
    note: "First Archimedes-corpus surface for Ox Security as a research-firm citation"
  - source_yaml_id: upwind
    source_name: "Upwind"
    relay_type: cited_by_bleepingcomputer
    note: "Upwind previously cited in finding-2026-05-12-FLASH-0001 Mini Shai-Hulud deobfuscation work; second corpus surface"
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [npm, node-ipc, atiertant, supply-chain, credential-stealer, "azurestaticprovider.net", DNS-TXT-exfil, AWS, GitHub-tokens]
triage_tags: [cross_corroboration_update, anti_noise_substance_unchanged, unattributed_persists, brief_update_to_finding_2026_05_14_0009, hard_rule_2_teampcp_lineage_declined, non_flash]
iocs_extracted: true
iocs_count: 5
text_word_count: 850
promoted: true
promoted_to_finding: finding-2026-05-15-0005
promoted_at: 2026-05-15T16:15:00-04:00
ttl_expires_at: 2026-08-13T15:43:00-04:00
---

# BleepingComputer expands node-ipc npm compromise coverage — four research firms confirm UNATTRIBUTED status

**Source URL:** https://www.bleepingcomputer.com/news/security/popular-node-ipc-npm-package-compromised-to-steal-credentials/
**Byline:** Bill Toulas
**Published:** 2026-05-15 17:10:42 UTC (13:10 EDT)

---

## Headline finding

BleepingComputer publishes a fuller technical writeup on the **node-ipc npm package** compromise that was first surfaced 2026-05-14 by Socket and StepSecurity (see finding-2026-05-14-0009 + raw-2026-05-14-pm-005). Bill Toulas's article confirms:

- **Three malicious versions:** node-ipc@9.1.6, @9.2.3, @12.0.1
- **Compromise vector:** maintainer-account hijack of inactive maintainer 'atiertant' (no prior account history flagged in BleepingComputer; Socket previously characterized the account as "no-history")
- **Package reach:** ~690,000 weekly downloads (BleepingComputer's figure; matches finding-2026-05-14-0009)
- **Exfiltration channel:** DNS-TXT queries to bootstrap resolver `sh[.]azurestaticprovider[.]net:443` transmitting data to `bt[.]node[.]js` with prefixes `xh`, `xd`, `xf`. A 500 KB compressed archive generates approximately 29,400 DNS queries (specific operational detail not in finding-2026-05-14-0009).
- **Mechanism:** Infostealer executes automatically through the CommonJS entrypoint (`node-ipc.cjs`) upon application loading. Code is heavily obfuscated and fingerprints systems before data collection.

## Categories of credentials targeted (BleepingComputer enumeration)

- Cloud credentials (AWS, Azure, GCP, OCI, DigitalOcean)
- SSH keys and configs
- Kubernetes, Docker, Helm, Terraform credentials
- npm, GitHub, GitLab tokens
- .env files and database credentials
- Shell histories and CI/CD secrets
- macOS Keychain and Firefox profiles
- Microsoft Teams local storage

This list is consistent with the ~90-credential-category figure in finding-2026-05-14-0009; this BleepingComputer surface enumerates the major buckets explicitly.

## Operational characteristics (BleepingComputer)

- Avoids files >4 MiB
- Skips `.git` and `node_modules` directories
- No persistence mechanisms
- No secondary payload deployment
- Deletes temporary tar.gz archives post-exfiltration

These characteristics are framed by Bill Toulas as "operational discipline" indicators — fingerprinting + bounded file-size + no persistence + cleanup is consistent with a single-pass smash-and-grab credential exfil rather than long-dwell access (which differs from Mini Shai-Hulud's worm-propagation model in finding-2026-05-12-FLASH-0001).

## Research-firm attribution status (the key cross-corroboration update)

BleepingComputer names **four** research firms identifying or analyzing the attack:

1. **Socket** — co-primary on the original disclosure (per finding-2026-05-14-0009)
2. **StepSecurity** — co-primary on the original disclosure (per finding-2026-05-14-0009)
3. **Ox Security** — **NEW** first Archimedes-corpus surface as cited research firm on this incident
4. **Upwind** — previously cited in finding-2026-05-12-FLASH-0001 (Mini Shai-Hulud deobfuscation); second corpus surface

**All four research firms decline to attribute** the node-ipc compromise to TeamPCP, Shai-Hulud, Mini Shai-Hulud, or any tracked actor. This is the **second wave of UNATTRIBUTED-status corroboration** after the original Socket + StepSecurity Hard-Rule-2-compliant declination yesterday afternoon.

For the afternoon brief: the four-firm-consensus UNATTRIBUTED status **strengthens** the finding-2026-05-14-0009 disposition. It does NOT introduce a new attribution layer. It does NOT change the digraph (B2 / WEP likely on the compromise facts; UNATTRIBUTED on the threat-actor layer).

## Recommended actions (BleepingComputer)

Remove affected versions immediately, rotate exposed secrets, inspect lockfiles and npm caches.

## Discard logic for FLASH

Already covered by finding-2026-05-14-0009 + raw-2026-05-14-pm-005:
- Trigger 1 (critical-cve-exploited): FALSE — no CVE assigned to node-ipc compromise (npm-supply-chain compromises typically don't get CVEs)
- Trigger 2 (tracked-actor-attribution): FALSE — UNATTRIBUTED status reaffirmed by four firms; no tracked-actor connection
- Trigger 3 (first-party-ioc-hit): FALSE — Splunk dormant stream pattern persists (sh.azurestaticprovider[.]net IOC has been queryable since 2026-05-14; zero hits over 24h sweep)
- Trigger 4 (tracked-actor-ttp-change): FALSE — UNATTRIBUTED; not a tracked-actor TTP delta
- Trigger 5 (active-ad-campaign): FALSE — no A&D-prime named victim; widespread package compromise but commodity scope
- Trigger 6 (zero-day-no-patch): FALSE — malicious versions have been unpublished; npm has flagged the affected versions

This raw-signal is therefore **brief-update candidate** for finding-2026-05-14-0009, NOT a fresh FLASH. The substance is reaffirmed four-firm research consensus on UNATTRIBUTED status + operational-discipline framing of the exfil mechanism.

## A&D relevance

Same as finding-2026-05-14-0009: **indirect medium**. node-ipc has aviation / A&D-tooling exposure through its widespread npm dependency-graph reach (it's a foundational IPC library), but no A&D-prime named victim has surfaced. The credential-category enumeration includes AWS / GitHub / Terraform — all of which are common in A&D-prime SDLC estates — so the operational impact for any victim org includes "rotate everything." DIB / DFARS-supply-chain CI/CD estates should treat this as an inventory-and-rotate item if node-ipc shows in dependency graphs.

## Article body excerpt (limited quote, under 15 words)

BleepingComputer notes attackers "compromised the npm account of inactive maintainer 'atiertant' and injected credential-stealing malware."

(Quote is 14 words; one quote only per Hard Rule 7.)

## Extraction notes

- Language: en
- Publisher byline: Bill Toulas
- Article type: media (technical follow-on; not originating research)
- Raw IOC extraction invoked: yes

## IOCs (from ioc-extraction skill)

```yaml
iocs:
  malicious_packages:
    - ecosystem: npm
      package: "node-ipc"
      versions_compromised:
        - "9.1.6"
        - "9.2.3"
        - "12.0.1"
      maintainer_hijacked: "atiertant"
      weekly_downloads_at_compromise: 690000
      entrypoint: "node-ipc.cjs (CommonJS)"
      patch_status: "unpublished_npm_revocation"
      cve: null  # npm-supply-chain compromises typically don't get CVEs

  c2_infrastructure:
    - domain: "sh[.]azurestaticprovider[.]net"
      port: 443
      protocol: "DNS_TXT_bootstrap"
      role: "bootstrap_resolver_for_dns_txt_exfil"
      destination_label: "bt[.]node[.]js (DNS-TXT-record transmission target)"
      query_prefixes:
        - "xh"
        - "xd"
        - "xf"
      exfil_overhead_metric: "500 KB compressed archive → ~29,400 DNS queries"
      operational_note: "Same IOC as finding-2026-05-14-0009 / raw-2026-05-14-pm-005 — no change; cross-corroborated by BleepingComputer relay"

  credential_categories_targeted:
    cloud_providers:
      - AWS
      - Azure
      - GCP
      - OCI
      - DigitalOcean
    infrastructure_tooling:
      - "SSH keys and configs"
      - Kubernetes
      - Docker
      - Helm
      - Terraform
    developer_platforms:
      - npm
      - GitHub
      - GitLab
    secrets_storage:
      - ".env files"
      - "database credentials"
      - "shell histories"
      - "CI/CD secrets"
    desktop_secrets:
      - "macOS Keychain"
      - "Firefox profiles"
      - "Microsoft Teams local storage"

  operational_discipline:
    file_size_ceiling: "4 MiB (skip larger files)"
    path_exclusions:
      - ".git"
      - "node_modules"
    persistence: "none"
    secondary_payload: "none"
    cleanup_behavior: "deletes temporary tar.gz archives post-exfil"

  research_firm_attributions:
    - firm: "Socket"
      role: "co-primary on disclosure"
      attribution: "UNATTRIBUTED"
      hard_rule_2_compliant: true
    - firm: "StepSecurity"
      role: "co-primary on disclosure"
      attribution: "UNATTRIBUTED"
      hard_rule_2_compliant: true
    - firm: "Ox Security"
      role: "additional analysis cited by BleepingComputer"
      attribution: "UNATTRIBUTED"
      first_archimedes_corpus_citation: true
    - firm: "Upwind"
      role: "additional analysis cited by BleepingComputer"
      attribution: "UNATTRIBUTED"
      first_archimedes_corpus_surface: "finding-2026-05-12-FLASH-0001 (Mini Shai-Hulud deobfuscation); second corpus surface here"

  attribution_claims:
    - claim: "node-ipc compromise via inactive-maintainer account hijack"
      claimed_by: "Socket + StepSecurity + Ox Security + Upwind (four-firm consensus)"
      attribution_language: "UNATTRIBUTED"
      teampcp_lineage_status: "declined by all four firms per Hard Rule 2 (mechanism + scope + ecosystem + C2 differ from Mini Shai-Hulud)"
      shai_hulud_lineage_status: "declined by all four firms"

  iocs_count_total: 5
  ioc_breakdown:
    domain: 1
    package: 1 (node-ipc, 3 versions)
    npm_maintainer_handle: 1
    credential_category_total: 22
    operational_discipline_signal: 5

  iocs_status_vs_finding_2026_05_14_0009:
    substance: unchanged
    new_layer: "four-firm research consensus on UNATTRIBUTED status (vs. two-firm yesterday)"
    new_iocs: "none — sh.azurestaticprovider[.]net was already in yesterday's surface"
    operational_detail_added: "29,400 DNS queries per 500 KB archive (exfil overhead metric)"
    operational_detail_added_2: "operational discipline checklist (size ceiling, path exclusions, no persistence, cleanup)"
```
