---
dossier_id: VT-005
cluster_name: OpenC3-COSMOS-2026-Cluster
title: "OpenC3 COSMOS spacecraft / satellite C2 software — five-CVE cluster (two Critical) in pre-7.0.0 estates"
cluster_keying_principle: >
  Single cluster dossier keyed on the fix-version 7.0.0 boundary, NOT
  five separate per-CVE entries. The operational unit-of-tracking is
  "estate running pre-7.0.0 OpenC3 COSMOS" — which is how an A&D operator
  would scope remediation. All five CVEs share disclosure date
  (vendor GHSAs 2026-04-20), share fix release (7.0.0-rc3 / 7.0.0),
  and share the upgrade-tempo operational variable.

cves:
  - cve_id: CVE-2026-42087
    severity: critical
    cvss_v3_base: 9.6
    cvss_v3_vector: "AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:N"
    cwe: [CWE-89]
    component: "Time-Series Database (cvt_model.rb tsdb_lookup function)"
    class: "SQL injection"
    ghsa_id: GHSA-v529-vhwc-wfc5
  - cve_id: CVE-2026-42088
    severity: critical
    cvss_v3_base: 9.6
    cwe: [CWE-269]
    component: "Script Runner Tool / openc3-COSMOS-script-runner-api container-share network"
    class: "Privilege escalation via container network trust-boundary failure"
    ghsa_id: GHSA-2wvh-87g2-89hr
  - cve_id: CVE-2026-42084
    severity: high
    cvss_v3_base: 8.1
    component: "Password change endpoint"
    class: "Authentication bypass / session token reuse"
    ghsa_id: GHSA-wgx6-g857-jjf7
  - cve_id: CVE-2026-42085
    severity: medium
    cvss_v3_base: 4.3
    component: "save_tool_config()"
    class: "Arbitrary file write to /plugins"
    ghsa_id: GHSA-4jvx-93h3-f45h
  - cve_id: CVE-2026-42086
    severity: medium
    cvss_v3_base: 4.6
    component: "Command Sender UI"
    class: "Self-XSS via unsafe eval()"
    ghsa_id: GHSA-ffq5-qpvf-xq7x

disclosed_at: 2026-04-20             # vendor GHSAs
nvd_published_at: 2026-05-04         # NVD record publication
nvd_last_modified_at: 2026-05-08

affected_products:
  - vendor: OpenC3
    product: COSMOS
    description: "Open-source command-and-control software for spacecraft, satellites, constellations, and embedded systems integration / test / operations"
    versions_affected:
      cluster_wide: "6.7.0 through 7.0.0-rc2"
      per_cve_variations:
        - cve: CVE-2026-42087
          range: "6.7.0 through 7.0.0-rc2"
        - cve: CVE-2026-42088
          range: "6.7.0 through 7.0.0-rc2"
        - cve: CVE-2026-42084
          range: "pre-6.10.5 and 7.0.0-rc1 / -rc2"
        - cve: CVE-2026-42085
          range: "6.7.0 through 7.0.0-rc2"
        - cve: CVE-2026-42086
          range: "6.7.0 through 7.0.0-rc2"
    fixed_in: ["7.0.0-rc3", "7.0.0"]

kev_status:
  any_cve_in_kev: false
  cves_in_kev: []
  last_checked: 2026-06-10
  watch_signal_active: true
  watch_signal_note: >
    Track KEV catalog for addition of any of the five CVEs. KEV addition
    is the primary tripwire that would lift the single-source veto on
    the exploitation-status leg of the source finding via CISA's
    independent determination. None listed as of 2026-05-09 06:01 sweep.

exploitation_status: not_observed
exploitation_status_qualifier: >
  No in-the-wild exploitation reported by any source. None of the five
  CVEs is on the CISA KEV catalog as of 2026-05-09. Splunk first-party
  metadata sweep across archimedes + defenseclaw_local indices over -30d
  returns zero events matching any of the five CVE IDs or "openc3" /
  "cosmos" keywords — but neither index carries OpenC3 COSMOS deployment
  telemetry in scope, so silent Splunk is NOT disconfirming per Hard
  Rule 8. The "no exploitation" claim is bounded by visibility into
  spacecraft-C2 enclaves, which are routinely high-segmentation and
  under-represented in public threat feeds.

public_exploit_available: partial
public_exploit_note: >
  PoC content is embedded in the vendor GHSAs (e.g., the canonical
  `' OR 1=1 --` SQLi pattern for CVE-2026-42087, container-network
  attack-step descriptions for CVE-2026-42088). Per Hard Rule 3 / Rule 6,
  the PoC content is NOT reproduced beyond pointers to the public
  advisory URLs. The disclosure-to-weaponization gap is narrow given
  the detail level of the GHSAs (parameter names, function references).

patch_status: patches_available
patch_release_date: 2026-04-20

mitigation_available: true

related_actors: []
related_actors_note: >
  No actor named by any source. No exploitation reported. No campaign
  reporting. Per Hard Rule 2, Archimedes does not originate attribution.
  Vuln-tracker records vulnerability-disclosure facts only.

related_findings:
  - finding-2026-05-09-0001

related_briefs:
  - 2026-05-09-morning

ad_relevance: high
ad_relevance_rationale: >
  OpenC3 COSMOS is spacecraft / satellite / constellation
  command-and-control software. Vendor positioning page names NASA and
  BAE Systems among COSMOS users alongside Astroscale, AST Space,
  MethaneSAT, and Turion Space. BAE Systems is a Tier-1 prime on the
  Archimedes aerospace-defense watchlist. Software function maps
  directly to the A&D-target profile from CLAUDE.md (aircraft,
  spacecraft, missile, defense systems R&D). SBSS (Space-Based Space
  Surveillance) satellite program heritage is publicly documented in
  vendor materials. Operational risk: COSMOS deployments at A&D primes
  would typically sit in spacecraft-test-and-operations enclaves where
  the C2 instance has reachability — direct or indirect — to live
  mission systems or test articles. The vendor user-base claim is
  single-source self-attestation; deployment density and version
  posture across the named user base are not independently corroborated
  in the current collection window.

digraph: A2
wep_ceiling: likely
single_source_veto_applied: true
single_source_veto_basis: >
  NVD CVE records and OpenC3 vendor GHSAs share a common evidence basis
  via the standard CNA process. Removing the vendor advisory collapses
  NVD's technical content to metadata-only registration. No independent
  third-party technical analysis (Mandiant, Unit 42, CrowdStrike,
  SentinelLabs, Bishop Fox, Praetorian) corroborating the vulnerabilities
  exists yet.

tracked_since: 2026-05-09
last_updated: 2026-06-10
tracking_version: 2
tlp: CLEAR
---

# OpenC3 COSMOS 2026 Cluster — Five CVEs in Pre-7.0.0 Estates

OpenC3 COSMOS — open-source command-and-control software for spacecraft, satellite constellations, and embedded systems integration / test / operations — has five CVEs assigned in a single April 2026 vendor disclosure, two of them Critical (CVSS 9.6). All five are patched in 7.0.0-rc3 and the full 7.0.0 release. The operational unit-of-tracking is "estate running pre-7.0.0 OpenC3 COSMOS" — that is the scope an A&D operator would address with a single upgrade event.

## Summary

The vendor (OpenC3) published five GitHub Security Advisories on 2026-04-20 disclosing vulnerabilities ranging from Critical SQL injection (CVE-2026-42087, CVSS 9.6, in the Time-Series Database `tsdb_lookup` function) through Critical privilege escalation (CVE-2026-42088, CVSS 9.6, via the Script Runner Tool's container-share network), one High-severity authentication bypass (CVE-2026-42084, CVSS 8.1, password reset via session token reuse), and two Medium-severity issues (CVE-2026-42085 arbitrary file write to `/plugins`; CVE-2026-42086 self-XSS in Command Sender via `eval()`). NVD records were published 2026-05-04 and last-modified 2026-05-08, downstream of the vendor GHSAs via the standard CNA process.

The cluster is being tracked because OpenC3 COSMOS is spacecraft / satellite / constellation C2 software with a vendor-attested user base that includes NASA and BAE Systems (Tier-1 prime on the aerospace-defense watchlist) alongside Astroscale, AST Space, MethaneSAT, and Turion Space, with SBSS satellite program heritage. The software function maps directly to the A&D-target profile from CLAUDE.md.

No in-the-wild exploitation is reported by any source. None of the five CVEs is on the CISA KEV catalog as of 2026-05-09. The patch path is straightforward (upgrade to 7.0.0); the operational variable is upgrade tempo in spacecraft-test-and-operations environments where major-version bumps commonly gate behind mission-script regression and change-control boards.

## CVE roster

| CVE | Severity | CVSS | CWE | Component | GHSA |
|---|---|---|---|---|---|
| CVE-2026-42087 | Critical | 9.6 | CWE-89 | Time-Series Database (`cvt_model.rb` `tsdb_lookup`) | GHSA-v529-vhwc-wfc5 |
| CVE-2026-42088 | Critical | 9.6 | CWE-269 | Script Runner Tool / container-share network | GHSA-2wvh-87g2-89hr |
| CVE-2026-42084 | High | 8.1 | — | Password change endpoint | GHSA-wgx6-g857-jjf7 |
| CVE-2026-42085 | Medium | 4.3 | — | `save_tool_config()` | GHSA-4jvx-93h3-f45h |
| CVE-2026-42086 | Medium | 4.6 | — | Command Sender UI (`eval()`) | GHSA-ffq5-qpvf-xq7x |

CWE classifications for CVE-2026-42084 / -42085 / -42086 are not authoritatively populated in the current NVD records pulled for this dossier; the vendor GHSAs describe class-equivalent flaws (auth bypass via token reuse; arbitrary file write via path manipulation; cross-site scripting via unsafe eval). Vuln-tracker should re-pull NVD records on next refresh to capture any analyst-added CWE enrichment.

## Technical detail

### CVE-2026-42087 — SQL Injection in Time-Series Database (Critical 9.6)

- **Component:** `cvt_model.rb` `tsdb_lookup()` — telemetry data store
- **Vulnerability class:** SQL injection (CWE-89). User-supplied input flows into a SQL query without sanitization.
- **Attack vector:** `AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:N` — network-reachable, low complexity, low-privilege required (any account with telemetry permission: Admin, Operator, Viewer, or Runner role qualifies), no user interaction, scope-changed.
- **Attack surface per vendor:** the `start_time` parameter of the `get_tlm_values` RPC endpoint. Vendor describes that an attacker can break out of the initial SQL statement and execute arbitrary SQL commands, including data deletion.
- **Affected:** 6.7.0 through 7.0.0-rc2.
- **Fixed in:** 7.0.0-rc3.

### CVE-2026-42088 — Script Runner Tool Privilege Escalation (Critical 9.6)

- **Component:** Script Runner widget executing Python / Ruby in the `openc3-COSMOS-script-runner-api` Docker container.
- **Vulnerability class:** improper privilege management / container-network trust-boundary failure (CWE-269). Docker containers in the deployment share a network, allowing scripts executed in the Script Runner container to connect directly to backend services (Redis, buckets) bypassing the API authorization layer.
- **Attack surface per vendor:** authenticated Script Runner user can read Redis credentials from container environment, modify Redis state including secrets and COSMOS settings, and read/write configuration / log / plugin files in the buckets service. Vendor stated impact: "Data disclosure/manipulation, privilege escalation."
- **Affected:** 6.7.0 through 7.0.0-rc2.
- **Fixed in:** 7.0.0-rc3.

### CVE-2026-42084 — Password Reset via Session Token (High 8.1)

- **Component:** password change endpoint.
- **Vulnerability class:** authentication bypass via session token reuse — endpoint accepts a valid session token in lieu of the old password.
- **Attack surface per vendor:** in any breach scenario where a session token has been acquired, the holder can change the account password and persist as the legitimate account holder. Admin-account hijacking is in-scope.
- **Affected:** pre-6.10.5 and 7.0.0-rc1 / -rc2.
- **Fixed in:** 7.0.0-rc3.

### CVE-2026-42085 — Arbitrary File Write to /plugins (Medium 4.3)

- **Component:** `save_tool_config()`.
- **Vulnerability class:** arbitrary file write — caller can specify destination path inside the shared `/plugins` directory tree via a crafted configuration filename.
- **Attack surface per vendor:** configuration overwrite or planting in the `/plugins` tree.
- **Fixed in:** 7.0.0-rc3.

### CVE-2026-42086 — Self-XSS in Command Sender (Medium 4.6)

- **Component:** Command Sender UI.
- **Vulnerability class:** cross-site scripting via unsafe `eval()` on array-like command parameters.
- **Attack surface per vendor:** user-supplied payloads execute in the browser session at command-send time.
- **Fixed in:** 7.0.0-rc3.

Vulnerability-class descriptions above are conceptual. PoC content from the GHSAs (parameter values, container-escape script chains, payload structures) is not reproduced here. Defenders should consult the vendor advisories directly under standard read-only research workflows.

## Affected products and versions

- **Vendor:** OpenC3
- **Product:** COSMOS
- **Cluster-wide affected range:** 6.7.0 through 7.0.0-rc2
- **CVE-2026-42084 has a wider range:** also affects pre-6.10.5
- **Patched versions:** 7.0.0-rc3 and the full 7.0.0 release

The operational scope an A&D operator would address: any COSMOS instance not yet upgraded to 7.0.0 carries some subset of the cluster. The full upgrade closes all five.

## Disclosure and exploitation timeline

| Date | Event | Source |
|---|---|---|
| 2026-04-20 | Vendor GHSAs published (all five) | [OpenC3 advisories](https://github.com/OpenC3/cosmos/security/advisories) |
| 2026-04-20 | Patches released (7.0.0-rc3 / 7.0.0) | OpenC3 release notes |
| 2026-05-04 | NVD records published | [NVD CVE-2026-42087](https://nvd.nist.gov/vuln/detail/CVE-2026-42087) |
| 2026-05-08 | NVD records lastModified (in window) | NVD |
| 2026-05-09 | Cluster surfaced via Archimedes morning collection | finding-2026-05-09-0001 |
| 2026-05-09 | Vuln-tracker dossier created | This dossier |

No subsequent exploitation events have been reported.

## Attribution to tracked actors

No Archimedes-tracked actor has been publicly attributed to exploitation of any CVE in this cluster as of 2026-05-09. No source names any actor in connection with the disclosure. No campaign reporting exists.

Per Hard Rule 2, Archimedes does not originate attribution. The vuln-tracker dossier records what sources attribute, not what Archimedes infers. If a future cited source attributes exploitation to a tracked actor, this dossier will be updated with the source-grade and citation; until then, attribution remains empty.

## Mitigations and patches

**Patch:** Upgrade OpenC3 COSMOS to 7.0.0 (or 7.0.0-rc3). All five CVEs are closed by the upgrade.

**Major-version-bump considerations** for spacecraft-test-and-operations environments:

- The 6.x → 7.0 transition is a major-version boundary. Operators should expect breaking changes (mission-script API, telemetry definitions, plugin compatibility) and budget regression-test time accordingly.
- Spacecraft-C2 environments commonly gate major upgrades behind mission-script regression-test campaigns and flight-software change-control boards. NASA-class change control commonly extends to 90+ days; mid-mission baselines may defer indefinitely until next launch / next mission phase.
- The federal-typical 30-day patch envelope may not apply when the patch is a major-version bump in a flight-relevant integration.

**No vendor-published interim mitigations** for pre-7.0.0 estates that cannot complete the upgrade in the federal-typical envelope. Operators in change-controlled environments should evaluate compensating controls under existing risk-management framework processes.

## Defense recommendations

For an A&D operator with potential OpenC3 COSMOS exposure:

1. **Inventory.** Determine whether OpenC3 COSMOS is deployed in any spacecraft-test-and-operations enclave, integration lab, or production C2 path. Vendor user-base claims (NASA, BAE Systems, et al.) are vendor self-attestation; only an inventory query confirms operator-specific exposure.
2. **Version posture.** For each COSMOS instance, identify version. 7.0.0 is the goal state; pre-7.0.0 instances carry some subset of the cluster.
3. **Plan upgrade.** Schedule the 6.x → 7.0 upgrade through normal change-control. Budget regression-test time for mission scripts, telemetry definitions, and plugin compatibility. The fixed release was published 2026-04-20; the longer the gap, the longer the operational risk window.
4. **Compensating controls for pre-upgrade interval** (paraphrased from generic least-privilege guidance, NOT vendor-published mitigations specific to this cluster):
    - Restrict COSMOS web-UI / RPC reachability to operations-network sources only; verify there is no inadvertent public or wider-enterprise reachability.
    - Review COSMOS account roster: any low-privilege account (Viewer / Runner role) is in-scope for the SQLi attack surface (CVE-2026-42087). Confirm account hygiene (rotation, MFA where supported, no shared credentials).
    - Treat Script Runner widget access as a privileged surface. Limit Script Runner to users whose role requires script authoring; the container-network trust-boundary failure (CVE-2026-42088) means any Script Runner user has effective Redis / buckets access until the patch lands.
    - Review the deployment's Docker container network topology. The Script Runner privesc is a shared-network trust-boundary issue; understanding what services are reachable on the shared network informs blast radius if the surface is exploited pre-patch.
5. **Detection priorities.** Log COSMOS API access (especially `get_tlm_values` calls and Script Runner script-execution events). Hunt for anomalous database operations originating from telemetry-RPC paths. Monitor session-token rotation patterns for the password change endpoint.

## Detection opportunities

- **CVE-2026-42087 (SQLi):** Log unusual content in the `start_time` parameter of `get_tlm_values` RPC requests. Anomalous SQL-shaped strings, comment markers, or boolean-tautology patterns in a parameter expected to be timestamp-shaped is investigable.
- **CVE-2026-42088 (Script Runner privesc):** Egress connections from the `openc3-COSMOS-script-runner-api` container to backend services (Redis, buckets) outside expected script execution patterns. Read access to environment variables holding Redis credentials from within Script Runner sessions.
- **CVE-2026-42084 (password reset bypass):** Password-change events on accounts where the requesting session was not preceded by an interactive password re-entry. Correlate with session token issuance / refresh patterns.
- **CVE-2026-42085 (file write):** File creations in `/plugins` outside expected configuration-update workflows.
- **CVE-2026-42086 (self-XSS):** Command Sender UI events with array-shaped parameters containing JavaScript-like content. Self-XSS is lower priority but useful as a tripwire that someone is probing the surface.

These are conceptual hunt sketches, not production detections. Operators should adapt to local logging surfaces and tune for false-positive baseline.

MITRE ATT&CK alignment (paraphrased class-mappings, not vendor-attested):
- T1190 Exploit Public-Facing Application — applies to the SQLi attack surface if COSMOS is reachable beyond a trusted operations network
- T1078 Valid Accounts — applies to the password-reset bypass session-token chain
- T1611 Escape to Host — conceptually relevant to the Script Runner container-network trust boundary, though the bug is escape-to-shared-services rather than escape-to-host

## Tracking notes and watchlist signals

The dossier carries the following watchlist tripwires for re-evaluation. Vuln-tracker should monitor; any of these firing is grounds for state-change update and (for the first three) potential brief inclusion:

1. **CISA KEV addition for any of the five CVEs** — would lift the single-source veto on the source finding's exploitation-status leg via CISA's independent determination. As of 2026-05-09 06:01 sweep, none of the five is KEV-listed.
2. **Independent third-party technical analysis** by Mandiant, Unit 42, CrowdStrike, SentinelLabs, Bishop Fox, Praetorian, or comparable researcher publication — would lift the single-source veto on the technical-detail leg by adding non-CNA-derived analysis.
3. **NASA or BAE Systems public statement on COSMOS deployment posture** — would corroborate the vendor user-base claim independently. The vendor positioning page is single-source self-attestation; an operator-side statement (deployment confirmation, version status, upgrade plan, or affirmative non-use) would resolve the deployment-density assumption (A1 in the finding's KAC).
4. **Public exploit / weaponized PoC published outside the GHSAs** — vendor advisories already contain PoC-equivalent technical detail; standalone weaponized exploit code would broaden the attacker population probing the surface.
5. **In-the-wild exploitation observation** in any source (vendor IR, government bulletin, security firm telemetry, news reporting) — converts the cluster from disclosure-tracking to exploitation-tracking and changes the operational urgency framing materially.

Reanalysis tripwires from finding-2026-05-09-0001 (preserved verbatim from grader handoff):

- KEV addition for any of the five CVEs → rerun KAC with visibility assumption strengthened
- Second-vendor independent technical analysis published → rerun KAC with A4 (NVD/GHSA independence) classification revisited and red-team review threshold check
- NASA or BAE Systems public statement on COSMOS posture → resolve A1 (deployment density) directly and rerun KAC
- Mission-script regression or change-control signal observed in collection → resolve A2 (upgrade tempo) directly

## Related findings

- [finding-2026-05-09-0001](../../findings/finding-2026-05-09-0001.md) — Source disclosure cluster finding. Digraph A2, WEP "likely" (single-source veto applied). Six-assumption KAC review (analyst-20260509-091500); ACH skipped (no source attributes any actor; running ACH would violate Hard Rule 2). No red-team review (below threshold).

## Data gaps

These items could not be resolved from open sources at dossier creation:

- **CWE classifications for CVE-2026-42084 / -42085 / -42086** are not authoritatively populated in the NVD records visible at this dossier creation. Vendor GHSAs describe class-equivalent flaws. Vuln-tracker should re-pull NVD on next refresh to capture analyst-added CWE enrichment if any.
- **CVSS v4 vectors** were not captured for any of the five CVEs in the source materials reviewed; CVSS v3.1 base scores and (for CVE-2026-42087) the v3.1 vector are recorded. NVD may add v4 vectors over time.
- **Per-CVE NVD reference list** (e.g., third-party advisory mirrors, exploit-DB references) was not enumerated; the GHSA URLs are the primary canonical references and are recorded.
- **Independent corroboration of the vendor user-base claim** is not available — no NASA, BAE Systems, Astroscale, AST Space, MethaneSAT, or Turion Space public statement on COSMOS deployment posture exists in the current collection window. Vendor positioning page is single-source self-attestation.
- **Deployment-density estimate** for A&D Tier-1 / Tier-2 estates is not directly observable. No third-party A&D-software survey (Mandiant, Frost & Sullivan, AIA) referencing COSMOS market share is in the collection. SBSS heritage is publicly documented in vendor materials but does not establish current production deployment status.
- **Upgrade tempo evidence** for spacecraft-C2 6.x → 7.0 transitions is not directly observable. General-knowledge prior on spacecraft change-control tempo applies but is not specific to OpenC3 COSMOS deployments.
- **First-party exploitation telemetry** is not in scope — Splunk `archimedes` and `defenseclaw_local` indices do not carry OpenC3 COSMOS deployment instrumentation. Silent Splunk is not disconfirming per Hard Rule 8.
- **NVD/GHSA independence test** (whether NVD adds substantive analyst-derived content beyond the vendor GHSAs) was not performed by direct record-level comparison. The grader's single-source veto is the conservative default; vuln-tracker can perform the comparison as a deferred task and flag for re-grade if NVD enrichment is substantive.

## References

Primary sources (A-grade / vendor primary):

- [NVD CVE-2026-42087](https://nvd.nist.gov/vuln/detail/CVE-2026-42087) — Time-Series Database SQLi
- [NVD CVE-2026-42088](https://nvd.nist.gov/vuln/detail/CVE-2026-42088) — Script Runner privesc
- [NVD CVE-2026-42084](https://nvd.nist.gov/vuln/detail/CVE-2026-42084) — Password reset bypass
- [NVD CVE-2026-42085](https://nvd.nist.gov/vuln/detail/CVE-2026-42085) — Arbitrary file write
- [NVD CVE-2026-42086](https://nvd.nist.gov/vuln/detail/CVE-2026-42086) — Self-XSS
- [GHSA-v529-vhwc-wfc5](https://github.com/OpenC3/cosmos/security/advisories/GHSA-v529-vhwc-wfc5) — vendor advisory CVE-2026-42087
- [GHSA-2wvh-87g2-89hr](https://github.com/OpenC3/cosmos/security/advisories/GHSA-2wvh-87g2-89hr) — vendor advisory CVE-2026-42088
- [GHSA-wgx6-g857-jjf7](https://github.com/OpenC3/cosmos/security/advisories/GHSA-wgx6-g857-jjf7) — vendor advisory CVE-2026-42084
- [GHSA-4jvx-93h3-f45h](https://github.com/OpenC3/cosmos/security/advisories/GHSA-4jvx-93h3-f45h) — vendor advisory CVE-2026-42085
- [GHSA-ffq5-qpvf-xq7x](https://github.com/OpenC3/cosmos/security/advisories/GHSA-ffq5-qpvf-xq7x) — vendor advisory CVE-2026-42086
- [OpenC3 vendor advisories index](https://github.com/OpenC3/cosmos/security/advisories)

Vendor context (treated as B-grade self-attestation, not corroboration):

- [OpenC3 vendor positioning](https://openc3.com/) — names NASA, BAE Systems, Astroscale, AST Space, MethaneSAT, Turion Space among users; SBSS heritage

Internal:

- [finding-2026-05-09-0001](../../findings/finding-2026-05-09-0001.md) — source cluster finding
- [raw-2026-05-09-am-001](../../raw-signal/raw-2026-05-09-am-001-openc3-cosmos-cve-cluster-spacecraft-c2.md) — collector raw signal

## Patch-status re-verification — 2026-06-10

Re-checked against NVD (CVE-2026-42087/42088), CISA KEV, and OpenC3 docs/security-vulnerabilities. **No change to remediation status:** the cluster remains **patched in 7.0.0-rc3 / 7.0.0** — independent reporting (SentinelOne, CIRCL Vulnerability-Lookup, TheHackerWire) confirms the fix-version boundary (versions 6.7.0 up to but excluding 7.0.0-rc3 affected for the two Critical CVEs). **None of the five CVEs is on CISA KEV** as of 2026-06-10, and no in-the-wild exploitation is reported by any source — the watch-signal tripwires (KEV addition, independent third-party technical analysis, NASA/BAE deployment statement, weaponized PoC, ITW observation) remain un-fired. CVSS unchanged (two Criticals at 9.6). First-party Splunk still carries no OpenC3 COSMOS telemetry in scope (silent ≠ disconfirming, Hard Rule 8). The operational unit-of-tracking is unchanged: estates running pre-7.0.0 should complete the major-version upgrade through change control. `tracking_version` → 2; `kev_status.last_checked` and `last_updated` advanced to 2026-06-10.

*Updated: 2026-06-10 | Author: Archimedes (vuln-tracker) | Admiralty Grade: A2 — NVD/GHSA primary; single-source veto still applies | TLP: CLEAR*
