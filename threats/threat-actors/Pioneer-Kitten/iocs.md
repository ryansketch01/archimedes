---
actor_id: "029"
actor_name: Pioneer Kitten
last_updated: 2026-07-14
admiralty_grade: A2
tlp: CLEAR
---

# Pioneer Kitten — IOC Reference

> **Completeness caveat.** This dossier's atomic network-IOC layer is
> deliberately incomplete. The **AA24-241A network-indicator appendix**
> (IPs/domains/hashes/email accounts) and the **FortiGuard backdoor hashes/C2**
> were not cleanly retrievable for this build (CISA page 403 WAF; IC3 PDF
> corrupted; FortiGuard PDF not rendered). Those values are **pending direct
> retrieval** and must NOT be fabricated. Only CVEs (by ID, Hard Rule 3),
> the access-broker persona handles, and the front-company attribution note are
> folded as confirmed indicators this pass. `iocs.yaml` is the source of truth
> for `_master-index.yaml`.

## 1. CVEs Actively Exploited

Pioneer Kitten's signature is mass-exploitation of internet-facing edge/VPN
appliances. All CVEs recorded by ID only (Hard Rule 3 — no exploit/PoC content).
All are `vuln-tracker` handoff candidates; the four headline current-relevance
CVEs are flagged.

| CVE | Product | Note | Handoff |
|---|---|---|---|
| CVE-2024-24919 | Check Point Security Gateway | Info-disclosure; headline 2024 CVE in AA24-241A (some relays mislabel as F5 — NVD confirms Check Point) | ✅ |
| CVE-2024-3400 | Palo Alto PAN-OS GlobalProtect | Command-injection / RCE | ✅ |
| CVE-2023-3519 | Citrix NetScaler ADC / Gateway | Unauthenticated RCE | ✅ |
| CVE-2019-19781 | Citrix ADC / Gateway (NetScaler) | Long-running access vector since 2019 | |
| CVE-2019-11510 | Pulse Secure / Ivanti Connect Secure | Arbitrary file read; recurs across campaigns (AA24-241A + FortiGuard CNI) | |
| CVE-2020-5902 | F5 BIG-IP TMUI | RCE | |
| CVE-2022-1388 | F5 BIG-IP iControl REST | Auth bypass | |
| CVE-2018-13379 | Fortinet FortiOS SSL VPN | Path traversal; Lemon Sandstorm CNI campaign initial access | ✅ |
| CVE-2019-1579 | Palo Alto GlobalProtect SSL VPN | RCE; Lemon Sandstorm CNI campaign | |

## 2. Malicious Delivery Domains

**Pending direct retrieval.** No confirmed delivery domains folded this build.
The candidate broker-infrastructure domain `gupdate.net` was included in the
Splunk sweep but is **not** confirmed/folded as an IOC. Load domains from the
AA24-241A and FortiGuard appendices on retrieval.

## 3. IP Addresses

**Pending direct retrieval.** The AA24-241A network appendix ships IPs; not
retrieved this build. Do not fabricate.

## 4. File Hashes

**Pending direct retrieval.** FortiGuard's report ships hashes for HanifNet,
HXLibrary, NeoExpressRAT, and Havoc. Family names are recorded as tooling in
[profile.md](profile.md); no atomic hashes folded this build.

## 5. Registry Indicators

No documented registry indicators at this time.

## 6. Scheduled Task Indicators

FortiGuard documents backdoors deployed via **scheduled tasks disguised as
legitimate system jobs** (T1053.005) in the Lemon Sandstorm CNI campaign.
Specific task names are in the pending FortiGuard appendix. Hunt guidance in
Section 8.

## 7. Cloud / C2 Infrastructure

Named C2 tooling (recorded as tooling, not atomic IOCs): **Havoc** (open-source
C2), and living-off-the-land tunnelers (ngrok, Ligolo, FRPC, Chisel,
ReverseSocks5, Glider Proxy). Atomic C2 IPs/domains **pending direct retrieval**.

## 8. Detection Queries (Hunt Guidance)

Three hunt queries are defined in [iocs.yaml](iocs.yaml) `hunt_queries`:

1. **`pioneer-hunt-edge-cve-exploit`** (Splunk) — exploitation attempts against
   the 9 edge/VPN CVEs above. FP note: correlate with successful-exploit
   indicators, not raw CVE-string matches (scanners match too).
2. **`pioneer-hunt-tunneler-remote-access`** (EDR) — unauthorized tunneling /
   remote-access utilities on or behind edge devices (T1572 / T1219).
3. **`pioneer-hunt-masquerading-scheduled-tasks`** (EDR) — scheduled tasks
   masquerading as legitimate system jobs (T1053.005 — the FortiGuard persistence
   pattern for HanifNet/HXLibrary/NeoExpressRAT).

## 9. Persona & Attribution Context (not network IOCs)

- **Br0k3r** — self-identified access-broker persona; sells network access on
  underground marketplaces (AA24-241A). KeyBase / Twitter channels referenced.
- **xplfinder** — 2024 marketplace handle used by the Br0k3r persona.
- **Danesh Novin Sahand** — Iranian IT front company (ID 14007585836), assessed
  "likely" a cover entity (AA24-241A). **Distinct from ASA / Cotton Sandstorm**
  (Hard Rule 2 non-merge — see profile.md Connection Web).

## 10. First-Party Splunk Baseline

-90d sweep across `archimedes` + `defenseclaw_local` for the full indicator/alias/
CVE/persona set = **0 hits**. Index liveness control: archimedes 1,725 events,
defenseclaw_local 6 events over -90d (both live). **Visibility-bounded null** —
no first-party corroboration, no IOC-corroboration bonus applied. Frank is not a
Pioneer Kitten victim environment.

## Sources

- FBI / CISA / DC3 Joint CSA **AA24-241A** (2024-08-28) — CVEs, personas, front
  company, ransomware-affiliate relationships. Network appendix pending retrieval.
- **MITRE ATT&CK G0117** — alias cluster, tooling, sector list.
- **Dragos (PARISITE)** — sector list, non-attribution stance.
- **FortiGuard IR** (2025-05) — Lemon Sandstorm CNI campaign, novel backdoors,
  3 campaign CVEs. IOC appendix pending retrieval.
