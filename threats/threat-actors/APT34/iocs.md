---
actor_id: "023"
actor_name: APT34
last_updated: 2026-05-01
admiralty_grade: A2
tlp: CLEAR
source_of_record: true
sidecar: iocs.yaml
---

# APT34 — Indicators of Compromise

> **First-pass scaffold (Session 9 pre-work, 2026-05-01).** This indicator
> reference is sparse by design and grows as collector / grader feed APT34-
> attributed findings into the dossier.
>
> APT34 rotates infrastructure aggressively, especially after public
> disclosure events (e.g., 2019 Lab Dookhtegan, 2023 Symantec Crambus
> reporting). Treat all network-tier IOCs as time-bounded and prioritize
> behavioral / TTP-based detection over static IOC matching.

---

## CVEs Historically Exploited

| CVE | CVSS | Product | Description | Status |
|---|---|---|---|---|
| CVE-2017-11882 | 7.8 | Office Equation Editor | Memory-corruption RCE; weaponized in OilRig spearphishing 2017–2019 | Legacy — Patch Now |
| CVE-2017-0199 | 7.8 | Office / WordPad RTF | RTF/HTA RCE used in early OilRig campaigns | Legacy — Patch Now |

**No first-party Splunk observations of these CVEs being exploited against the
defenseclaw_local environment as of 2026-05-01.**

APT34 does not have a documented "zero-day per quarter" pattern like APT28 or
APT29. Their CVE exploitation tends to leverage well-documented N-day Office
vulnerabilities; current-generation operations rely more on credential abuse
and macro-laden documents than on novel CVE chains.

---

## Malicious Delivery Domains

*No Archimedes-tracked delivery domains as of 2026-05-01. Public reporting
contains hundreds of historic OilRig domains; they will be ingested when the
collector pulls Trend Micro MENORAH, Symantec Crambus, and Unit 42 Saitama
IOC appendices into the corpus.*

---

## IP Addresses

*No Archimedes-tracked APT34 IPs as of 2026-05-01.*

---

## File Hashes

### Backdoor families (no specific hashes ingested yet)

| Family | Type | First Seen | Source |
|---|---|---|---|
| MENORAH | C# backdoor (modular, anti-sandbox) | 2023-09 | Trend Micro 2023 |
| Saitama | .NET backdoor (DNS C2, anti-analysis) | 2022-05 | Unit 42 2022 |
| PowerExchange | Backdoor (Exchange transport agent C2) | 2023 | Symantec 2023 |
| SideTwist | C-language backdoor | 2021 | Mandiant tracking |
| MARLIN | Custom C# backdoor | 2023+ | Public reporting |
| Helminth | Original OilRig backdoor (PowerShell/VBScript) | 2016 | Unit 42 2016 |
| BONDUPDATER | DNS-tunneled backdoor | ~2018 | Unit 42 |
| OopsIE | HTTP-C2 trojan | 2018 | Unit 42 |
| RGDoor | IIS backdoor module | 2018 | Unit 42 |
| QUADAGENT | PowerShell backdoor | 2018 | Unit 42 |
| DNSpionage / Karkoff | DNS-tunneled backdoor | 2019 | Cisco Talos |

**Recommended next step:** ingest current YARA rules from Trend Micro MENORAH
report and Unit 42 Saitama report into the dossier on next collector pass.

---

## Registry Indicators

*No actor-specific registry artifacts catalogued in this scaffold. APT34
persistence via T1547.001 (Run keys) and T1546.003 (WMI Event Subscription)
is documented at TTP level in `profile.md`.*

---

## Scheduled Task Indicators

*No specific scheduled-task names catalogued in this scaffold. APT34 uses
T1053.005 generically; defender hunt should be on anomalous task creators
rather than specific names (which rotate).*

---

## Cloud C2 Infrastructure

| Pattern | Description | Source |
|---|---|---|
| Compromised Exchange transport agents | PowerExchange (2023) uses compromised Exchange as covert email-based C2 | Symantec Crambus 2023 |
| Compromised regional web servers | Heavy reuse of compromised regional infrastructure for C2; reduces fresh-registration noise | Unit 42, Mandiant ongoing |
| DNS tunneling to atypical TLDs | Helminth, BONDUPDATER, DNSpionage, Karkoff, Saitama all use DNS C2 | Cisco Talos, Unit 42 |

---

## Detection Queries (Hunt Guidance)

### 1. DNS-tunneling C2 (multiple APT34 toolkits)

**Splunk SPL:**

```spl
index=defenseclaw_local sourcetype=dns
| eval subdomain_label=mvindex(split(query, "."), 0)
| eval label_len=len(subdomain_label)
| where label_len >= 30
| stats count by src, query, label_len
| sort - count
```

False-positive consideration: legitimate CDN, telemetry, AV vendor DNS may
have long subdomain labels — tune by allowlisting known-good resolvers.

### 2. Unsigned or unfamiliar Exchange transport agents (PowerExchange)

**EDR pseudo-logic:**

```
ON HOSTS WHERE role = exchange_server:
  ENUMERATE installed transport agents
  ALERT IF agent.signed = false OR agent.publisher NOT IN allowlist
```

False-positive consideration: legitimate hygiene/anti-spam vendors install
agents. Allowlist enterprise-approved publishers.

### 3. New or modified IIS modules on perimeter web servers (RGDoor)

**EDR pseudo-logic:**

```
ON HOSTS WHERE role = web_server AND service = iis:
  BASELINE installed IIS modules with file hash
  ALERT IF new module added OR module file hash changed
  ALERT IF module is unsigned
```

False-positive consideration: legitimate patching/upgrades. Baseline must be
refreshed during scheduled change windows.

---

## Sources

- [Mandiant: APT34 — A previously unidentified Iranian threat actor (2017)](https://www.mandiant.com/resources/blog/apt34-new-targeted-attack-middle-east) — A1
- [Palo Alto Unit 42: OilRig research index](https://unit42.paloaltonetworks.com/tag/oilrig/) — A1
- [Cisco Talos: DNSpionage Brings Out the Karkoff (2019)](https://blog.talosintelligence.com/dnspionage-brings-out-the-karkoff/) — A1
- [Symantec: Crambus — New Campaign in Middle East (2023)](https://symantec-enterprise-blogs.security.com/threat-intelligence/crambus-middle-east-government) — A1
- [Trend Micro: APT34 deploys new MENORAH malware (2023)](https://www.trendmicro.com/en_us/research/23/i/apt34-deploys-phishing-attack-with-new-malware.html) — A1
- [Palo Alto Unit 42: Out to Sea — Saitama Backdoor (2022)](https://unit42.paloaltonetworks.com/saitama-backdoor/) — A1
- [MITRE ATT&CK G0049 — OilRig](https://attack.mitre.org/groups/G0049/) — A1

---

*First-pass scaffold authored 2026-05-01. Ingestion of full IOC appendices
deferred to next collector pass against APT34. Hard Rule 2 honored: every
attribution and indicator herein traces to a cited public source.*
