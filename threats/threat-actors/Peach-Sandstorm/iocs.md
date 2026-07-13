---
actor_id: "027"
actor_name: Peach Sandstorm
last_updated: 2026-07-12
dossier_version: 2
admiralty_grade: A1
tlp: CLEAR
source_of_record: true
sidecar: iocs.yaml
---

# Peach Sandstorm — Indicators of Compromise

> **Fold-in 2026-07-12 (dossier v2).** A collector direct-retrieval pass ratified
> the **FalseFont** (Microsoft Dec 2023 A1 + Unit 42 Mar 2024 A1 + Nextron Jan
> 2024 A2) and **Tickler** (Microsoft Aug 2024 A1) campaigns and populated their
> atomic IOCs below — replacing the earlier scaffold placeholders.
>
> Peach Sandstorm's primary access vector is **identity-plane password spray**,
> and its C2 leans on **legitimate cloud-service abuse** (Azure, Microsoft Graph
> API via ROADtools). Prioritize identity-plane and behavioral detection over
> static network-tier IOC matching. CVEs are referenced **by ID only** per Hard
> Rule 3 — no exploitation mechanism or PoC. **Hard Rule 7:** Unit 42's FalseFont
> page published malware-embedded C2 auth creds; the collector counted+discarded
> them — no credential values are stored here.

---

## CVEs Historically Exploited

Peach Sandstorm exploits public-facing applications (MITRE T1190) for initial
access and historically weaponized N-day Office/RCE vulnerabilities. **No
specific CVE list is asserted in this first-pass scaffold** — CVE-to-campaign
mappings are deferred to the next collector pass against authoritative vendor
advisories, and are recorded by ID only when ingested (Hard Rule 3). Do not
invent CVE claims without a cited source.

**No first-party Splunk observations of Peach Sandstorm CVE exploitation against
`defenseclaw_local` as of 2026-07-12.**

---

## Malicious Delivery / C2 Domains

| Domain (defanged) | Role | Malware | Resolves | First–Last | Source |
|---|---|---|---|---|---|
| `digitalcodecrafters[.]com` | C2 | FalseFont | `64.52.80[.]30` TCP/8080 | 2023-11 → 2024-03 | Unit 42 2024-03-25 (A1) |

*Historic context (not yet ingested as atomic IOCs): FireEye 2017 documented
domains masquerading as aviation/defense companies (Boeing/Alsalam, Northrop/
Vinnell, and similar). The 16 Tickler `*.azurewebsites.net` C2 subdomains are
tabled under **Cloud C2 Infrastructure** below.*

---

## IP Addresses

| IP (defanged) | Role | Malware | Port | First–Last | Source |
|---|---|---|---|---|---|
| `64.52.80[.]30` | C2 | FalseFont | TCP/8080 | 2023-11 → 2024-03 | Unit 42 2024-03-25 (A1) |

---

## File Hashes

### FalseFont (SHA256) — Microsoft Dec 2023 / Unit 42 Mar 2024

| SHA256 | Role | Notes | Source |
|---|---|---|---|
| `364275326bbfc4a3b89233dabdaf3230a3d149ab774678342a40644ad9f8d614` | Delivery | Packed; impersonates Maxar Technologies (`Maxar.dll`); VT 41/71. MD5 `6fd5d31d607a212c6f7651c79e7655a3` | Unit 42 (A1) |
| `4145e792c9e9f3c4e80ca0e290bd7568ebcef678affd68d9b505f02c6acaab12` | Delivery | Unpacked FalseFont executable | Unit 42 (A1) |

Defender detection name: **`Backdoor:MSIL/FalseFont.A!dha`** (Microsoft; signature name, not a filesystem IOC).

### Tickler (SHA256) — Microsoft Aug 2024

*2 samples + 3 payloads + 4 sideloading-chain binaries. The msvcp140.dll /
vcruntime140.dll entries are **legitimate Microsoft binaries abused as sideloading
hosts** — match the exact hash only; a filename match will false-positive.*

| SHA256 | Role | Notes |
|---|---|---|
| `7eb2e9e8cd450fc353323fd2e8b84fbbdfe061a8441fd71750250752c577d198` | Sample | Yahsat-lure `...SECURITY_GUIDE_20240421.pdf.exe` (UAE satellite operator); VT 49/69. MD5 `ea79d9e044c7daff1de15f95f49a0265` |
| `ccb617cc7418a3b22179e00d21db26754666979b4c4f34c7fda8c0082d08cec4` | Sample | Tickler malware sample |
| `fb70ff49411ce04951895977acfc06fa468e4aa504676dedeb40ba5cea76f37f` | Payload | Associated Tickler payload |
| `711d3deccc22f5acfd3a41b8c8defb111db0f2b474febdc7f20a468f67db0350` | Payload | Associated Tickler payload |
| `5df4269998ed79fbc997766303759768ce89ff1412550b35ff32e85db3c1f57b` | Payload | Associated Tickler payload |
| `dad53a78662707d182cdb230e999ef6effc0b259def31c196c51cc3e8c42a9b8` | Sideload host | Abused legit `msvcp140.dll` |
| `56ac00856b19b41bc388ecf749eb4651369e7ced0529e9bf422284070de457b6` | Sideload chain | `LoggingPlatform.dll` (backdoor DLL) |
| `22017c9b022e6f2560fee7d544a83ea9e3d85abee367f2f20b3b0448691fe2d4` | Sideload host | Abused legit `vcruntime140.dll` |
| `e984d9085ae1b1b0849199d883d05efbccc92242b1546aeca8afd4b1868c54f5` | Sideload chain | `Microsoft.SharePoint.NativeMessaging.exe` |

### Other backdoor families (no specific hashes ingested yet)

| Family | Type | First Seen | Source |
|---|---|---|---|
| TURNEDUP | Custom backdoor | 2017 | FireEye 2017 |
| POWERTON | PowerShell backdoor | 2018 | FireEye |
| DROPSHOT / SHAPESHIFT | Dropper / wiper | 2017 | FireEye 2017 (destructive-malware ties) |
| StoneDrill | Wiper | 2017 | Kaspersky 2017 (NewsBeef / APT33-adjacent) |

---

## Registry Indicators

*No actor-specific registry artifacts catalogued in this scaffold. Persistence
via T1547.001 (Run keys) and T1053.005 (Scheduled Task) is documented at TTP
level in `profile.md`.*

---

## Scheduled Task Indicators

*No specific scheduled-task names catalogued in this scaffold. Hunt on anomalous
task creators rather than specific names.*

---

## Cloud C2 Infrastructure

| Pattern | Description | Source |
|---|---|---|
| Azure infrastructure abuse | Tickler backdoor abused fraudulent, attacker-controlled Azure subscriptions (`*.azurewebsites.net`) for C2/staging | Microsoft 2024 |
| Microsoft Graph API / Entra ID enumeration | ROADtools (roadrecon/roadtx) enumerates Entra ID + registers rogue devices post-password-spray | Unit 42 2026 (seed finding-2026-05-22-0002) |
| Password-spray against cloud identity | Distributed low-and-slow auth failures against Entra ID / M365 as primary access vector | Microsoft 2023 |

### Tickler fraudulent Azure C2 subdomains (16, all `*.azurewebsites.net`) — Microsoft Aug 2024

> Match **only** these specific subdomains. Never alert on the bare
> `azurewebsites.net` parent — it is a legitimate shared Azure service domain.

```
subreviews            satellite2              nodetestservers        satellitegardens
softwareservicesupport getservicessuports     getservicessupports    getsupportsservices
satellitespecialists  satservicesdev          servicessupports       websupportprotection
supportsoftwarecenter centersoftwaresupports  softwareservicesupports getsdervicessupoortss
```

*(`softwareservicesupport` and `softwareservicesupports` are distinct entries;
`getsdervicessupoortss` typosquat spelling preserved verbatim from the Microsoft
appendix. Satellite-themed subdomains independently reinforce the satellite-sector
targeting narrative.)*

### Password-spray user agent (LOW fidelity)

| Value | Fidelity | Notes | Source |
|---|---|---|---|
| `go-http-client` | **LOW / contextual only** | Commodity Go HTTP client UA seen in password-spray traffic (since Feb 2023). High false-positive risk — do NOT alert standalone; use only to corroborate an identity-plane spray pattern | Microsoft Aug 2024 |

---

## Detection Queries (Hunt Guidance)

### 1. Password spray against Entra ID / M365 (primary access vector)

**Splunk SPL:**

```spl
index=defenseclaw_local (sourcetype=azure:signin OR sourcetype=m365:signin)
(ResultType=50126 OR status="failure")
| bucket _time span=1h
| stats dc(user) as distinct_users_failed count as fail_count
    values(src_ip) as src_ips by _time, src_asn
| where distinct_users_failed >= 10
| sort - distinct_users_failed
```

False-positive consideration: legitimate bulk auth failures (misconfigured app,
expired service-account credential, VPN egress). Tune the distinct-users
threshold and allowlist known corporate egress ASNs.

### 2. ROADtools Entra ID enumeration user-agent strings

**KQL (Microsoft Sentinel / Graph sign-in logs):**

```kql
SigninLogs
| where UserAgent has_any ("roadtools", "python-requests")
| project TimeGenerated, UserPrincipalName, IPAddress, UserAgent, AppDisplayName
```

False-positive consideration: legitimate python-requests automation may exist;
correlate with anomalous device registration + Graph enumeration volume.

### 3. Rogue Entra ID device registration (T1098.005)

**KQL:**

```kql
AuditLogs
| where OperationName has "Add registered device"
| project TimeGenerated, InitiatedBy, TargetResources, ResultDescription
```

False-positive consideration: legitimate BYOD/onboarding waves. Correlate with a
password-spray precursor, default OS-version artifacts, and off-hours timing.

### 4. Tickler / FalseFont backdoor artifacts

**EDR pseudo-logic:**

```
DEPLOY current Microsoft-published YARA/EDR signatures for Tickler and FalseFont
  across Defense-Industrial-Base-tier hosts.
ALERT on signature match OR anomalous Azure-C2 outbound from implant host.
```

False-positive consideration: signature-based. Keep rules current from Microsoft
publications; pair with the Azure-abuse hunt for corroboration.

### 5. Atomic IOC sweep (ratified FalseFont/Tickler hashes + C2)

**Splunk SPL** (see `iocs.yaml` hunt `peach-hunt-atomic-ioc-match` for the full
hash/domain set):

```spl
index=defenseclaw_local
( file_hash IN (<9 Tickler + 2 FalseFont SHA256>)
  OR dest IN ("digitalcodecrafters.com", "64.52.80.30", <16 Tickler azurewebsites subdomains>) )
| stats count values(dest) as dest values(file_hash) as hashes by host, _time
```

False-positive consideration: match only the 16 specific Tickler subdomains, never
the bare `azurewebsites.net` parent; key the abused msvcp140/vcruntime140 sideload
hosts on exact hash, not filename.

---

## Sources

- [FireEye/Mandiant: APT33 Targets Aerospace and Energy Sectors (2017)](https://www.mandiant.com/resources/blog/apt33-insights-into-iranian-cyber-espionage) — A1
- [Microsoft: Peach Sandstorm password-spray campaigns (Sept 2023)](https://www.microsoft.com/en-us/security/blog/2023/09/14/peach-sandstorm-password-spray-campaigns-enable-intelligence-collection-at-high-value-targets/) — A1
- [Microsoft: FalseFont backdoor vs Defense Industrial Base (Dec 2023)](https://www.microsoft.com/en-us/security/blog/) — A1 (MSTIC advisory)
- [Palo Alto Unit 42: Curious Serpens' FalseFont Backdoor (Mar 2024)](https://unit42.paloaltonetworks.com/curious-serpens-falsefont-backdoor/) — A1 (FalseFont hashes/C2; Maxar impersonation)
- [Nextron Systems: FalseFont Backdoor analysis + YARA/Sigma (Jan 2024)](https://www.nextron-systems.com/2024/01/29/analysis-of-falsefont-backdoor-used-by-peach-sandstorm-threat-actor/) — A2
- [Microsoft: Peach Sandstorm deploys new custom Tickler malware (Aug 2024)](https://www.microsoft.com/en-us/security/blog/2024/08/28/peach-sandstorm-deploys-new-custom-tickler-malware-in-long-running-intelligence-gathering-operations/) — A1 (Microsoft-originated; no standalone Mandiant Tickler advisory located 2026-07-12 — Mandiant co-reporting `pending_direct_retrieval`)
- [Symantec: Elfin — Espionage vs Saudi Arabia and US (2019)](https://symantec-enterprise-blogs.security.com/threat-intelligence/elfin-apt33-espionage) — A1
- [Kaspersky: From Shamoon to StoneDrill (2017)](https://securelist.com/from-shamoon-to-stonedrill/77725/) — A2
- [Palo Alto Unit 42: Paved With Intent — ROADtools (2026)](https://unit42.paloaltonetworks.com/roadtools-cloud-attacks/) — A2 (seed finding-2026-05-22-0002)
- [MITRE ATT&CK G0064 — APT33](https://attack.mitre.org/groups/G0064/) — A1

---

*Authored 2026-07-12; atomic FalseFont/Tickler IOCs folded in same day (dossier
v2) from the collector direct-retrieval pass. Hard Rule 2 honored: every indicator
traces to a cited public source; Tickler is Microsoft-originated (Mandiant
co-reporting pending_direct_retrieval). Hard Rule 3 honored: CVEs by ID only, no
exploitation detail. Hard Rule 7 honored: FalseFont C2 auth creds counted and
discarded, not stored.*
