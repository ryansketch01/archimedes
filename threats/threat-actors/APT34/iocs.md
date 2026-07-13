---
actor_id: "023"
actor_name: APT34
last_updated: 2026-07-12
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
| CVE-2024-30088 | 7.0 | Windows Kernel | Elevation-of-privilege; reported exploited by APT34/OilRig for local privesc in Earth Simnavaz 2024 (Trend Micro). By ID only per Hard Rule 3. *Live-ratified 2026-07-12 (single-source Trend Micro; provisional-A2-confirmed, not multi-A A1).* | Patch — Verify |

**No first-party Splunk observations of these CVEs being exploited against the
defenseclaw_local environment as of the 2026-07-12 refresh** (sentinel sweep over
-90d returned a categorical zero — visibility-bounded null, Frank is not an
Iranian-espionage target-profile org).

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
| StealHook | Backdoor / credential thief (exfils creds as email attachments via compromised Exchange + password-filter DLL) | 2024-10 | Trend Micro Earth Simnavaz 2024 *(family name live-ratified 2026-07-12, single-source; IOC appendix — hashes/C2/emails — still 403-blocked, NOT retrieved)* |
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

### Named file artifacts

| Filename | Role | Technique | Campaign | Source |
|---|---|---|---|---|
| `psgfilter.dll` | Malicious password-filter DLL — registered with LSA to intercept plaintext credentials | T1556.002 | Earth Simnavaz 2024 | Trend Micro (live-ratified 2026-07-12, single-source) |

> `psgfilter.dll` is a **filename-only** artifact — no hash was retrieved this
> pass (Trend Micro's IOC appendix returned HTTP 403). Do not treat the filename
> alone as high-fidelity; pair with the registry-hunt below and confirm against
> the Trend Micro appendix on follow-up retrieval.

**Standing collection gaps (do NOT fabricate to fill):**
- **StealHook IOC appendix** — Trend Micro's full SHA256 hashes, C2 domains, and
  exfil email addresses were 403-blocked and NOT retrieved. Follow-up manual/OTX
  pull of the Trend Micro appendix recommended.
- **2025–2026 OilRig/Crambus A-grade primary + fresh IOCs** — only secondary/
  forecast material found this pass (continued 2025 energy/defense targeting;
  Check Point / The Record 2024–2025 Iraqi-gov 8-month-dwell + Yemen sub-ops).
  No primary URL or fresh hashes/domains pulled. Standing follow-up.

**Recommended next step:** ingest current YARA rules from Trend Micro MENORAH
report and Unit 42 Saitama report into the dossier on next collector pass, and
retrieve the Trend Micro Earth Simnavaz appendix for StealHook hashes/C2.

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

### 4. Unapproved Windows password-filter DLLs (Earth Simnavaz, T1556.002)

**EDR pseudo-logic:**

```
ON HOSTS WHERE role IN (domain_controller, privileged_server):
  READ HKLM\SYSTEM\CurrentControlSet\Control\Lsa\Notification Packages
  FOR EACH package DLL:
    ALERT IF dll NOT IN approved_baseline
    ALERT IF dll IS unsigned OR dll path NOT IN %SystemRoot%\System32
```

False-positive consideration: legitimate password-complexity / PAM products
register notification packages. Allowlist enterprise-approved filter DLLs.
Provenance: tied to Earth Simnavaz 2024 reporting, live-ratified 2026-07-12
(single-source Trend Micro). Concrete artifact: alert specifically on
`psgfilter.dll` registered as a notification package outside the approved
baseline.

---

## Sources

- [Mandiant: APT34 — A previously unidentified Iranian threat actor (2017)](https://www.mandiant.com/resources/blog/apt34-new-targeted-attack-middle-east) — A1
- [Palo Alto Unit 42: OilRig research index](https://unit42.paloaltonetworks.com/tag/oilrig/) — A1
- [Cisco Talos: DNSpionage Brings Out the Karkoff (2019)](https://blog.talosintelligence.com/dnspionage-brings-out-the-karkoff/) — A1
- [Symantec: Crambus — New Campaign in Middle East (2023)](https://symantec-enterprise-blogs.security.com/threat-intelligence/crambus-middle-east-government) — A1
- [Trend Micro: APT34 deploys new MENORAH malware (2023)](https://www.trendmicro.com/en_us/research/23/i/apt34-deploys-phishing-attack-with-new-malware.html) — A1
- [Palo Alto Unit 42: Out to Sea — Saitama Backdoor (2022)](https://unit42.paloaltonetworks.com/saitama-backdoor/) — A1
- [MITRE ATT&CK G0049 — OilRig](https://attack.mitre.org/groups/G0049/) — A1
- [Trend Micro: Earth Simnavaz (APT34/OilRig) — Windows Kernel flaw + StealHook vs. UAE/Gulf gov & energy (Oct 2024)](https://www.trendmicro.com/en_us/research/24/j/earth-simnavaz-cyberattacks.html) — A2 *(live-ratified 2026-07-12; SINGLE-SOURCE — sole A-grade originator, relays not independent corroboration; provisional-A2-confirmed, not multi-A A1. Full IOC appendix 403-blocked, not retrieved.)*
- [Cyber Security News: OilRig hackers exploit Microsoft Exchange (relay of Trend Micro)](https://cybersecuritynews.com/oilrig-hackers-microsoft-exchange-breach/) — C3 *(pure relay of Trend Micro; provided psgfilter.dll detail; NOT independent corroboration)*
- [Check Point Research via The Hacker News: "Cavern Manticore" / Cavern .NET C2 (2026)](https://thehackernews.com/2026/07/iran-linked-hackers-use-new-cavern-c2.html) — A2 *(CPR-noted Lyceum/OilRig overlap = CPR's assessment only; no Archimedes attribution merge — Hard Rule 2)*

---

*First-pass scaffold authored 2026-05-01; refreshed 2026-07-12 (90-day
/update-tracking); ratification fold-in 2026-07-12 (raw-2026-07-12-ratify-003).
The fold-in LIVE-RATIFIED the Earth Simnavaz 2024 campaign, StealHook family
name, CVE-2024-30088 linkage, and psgfilter.dll password-filter DLL against the
Trend Micro primary and cleared the pending flag on those items — under SINGLE-
SOURCE discipline (Trend Micro sole A-grade originator; relays not independent
corroboration; provisional-A2-confirmed, not multi-A A1). Net-new atomic IOC
added: `psgfilter.dll` filename. STILL PENDING: Trend Micro's StealHook IOC
appendix (hashes/C2/emails, 403-blocked) and a 2025-2026 OilRig/Crambus A-grade
primary. No file hashes, IPs, or domains were fabricated. Hard Rule 2 honored:
every attribution and indicator herein traces to a cited public source.*
