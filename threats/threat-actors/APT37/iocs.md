---
actor_id: "024"
actor_name: APT37
last_updated: 2026-05-09
admiralty_grade: A2
tlp: CLEAR
source_of_record: true
sidecar: iocs.yaml
---

# APT37 — Indicators of Compromise

> **First-pass scaffold (2026-05-09).** This indicator reference is sparse by
> design and grows as collector / grader feed APT37-attributed findings into
> the dossier. The current indicator set is concentrated on the
> BirdCall / Sqgame supply-chain campaign per ESET via The Record
> (finding-2026-05-07-0004); historical IOC appendices from FireEye/Mandiant
> 2018, Kaspersky 2016–2018, Cisco Talos 2017–ongoing, and Volexity 2021
> are NOT yet ingested.
>
> APT37 rotates infrastructure aggressively after public disclosure
> (visible across the 2018 Mandiant and 2021 Volexity cycles). Treat all
> network-tier IOCs as time-bounded and prioritize behavioral / TTP-based
> detection over static IOC matching. Cloud-platform C2 abuse is a
> particularly durable behavioral pattern.

---

## CVEs Historically Exploited

| CVE | CVSS | Product | Description | Status |
|---|---|---|---|---|
| CVE-2018-4878 | 9.8 | Adobe Flash Player | Use-after-free RCE; APT37 zero-day exploited Jan–Feb 2018 against South Korean targets; Adobe issued out-of-band patch | Legacy — Patched (Flash EOL) |
| CVE-2016-4117 | 9.8 | Adobe Flash Player | Type-confusion RCE; Kaspersky Operation Daybreak — APT37 zero-day exploited 2016 | Legacy — Patched (Flash EOL) |

**No first-party Splunk observations of APT37-attributed CVE exploitation against the
defenseclaw_local environment as of 2026-05-09.**

APT37 does not have a documented "zero-day per quarter" pattern at the rate
of APT28 or APT29. Historical zero-day use was concentrated on Adobe Flash
(now EOL); current-generation operations rely more on credential abuse,
spearphishing with weaponized HWP / Office documents, strategic-website
compromise, and supply-chain compromise (Sqgame 2026).

---

## Malicious Delivery Domains

| Domain | Role | Campaign | Source | Status |
|---|---|---|---|---|
| sqgame (exact domain not surfaced) | Compromised legitimate Android-card-game distribution platform | Sqgame supply-chain (Nov 2024–2026) | ESET via The Record (finding-2026-05-07-0004) | Compromised — exact domain redacted in source text |

> **Sqgame domain note:** The Record's article excerpt ingested via
> finding-2026-05-07-0004 identifies "Sqgame" as the compromised gaming
> platform but does not provide the exact domain in the source text excerpt.
> Passive DNS / VirusTotal enrichment is recommended to surface the specific
> domain. Per Hard Rule 4, no active scanning of Sqgame infrastructure has
> been performed; Sqgame is NOT in `authorized-targets.yaml`. Passive-only
> enrichment per LEGAL-POLICY.md.

*No additional Archimedes-tracked APT37 delivery domains as of 2026-05-09.
FireEye 2018, Volexity 2021, Cisco Talos 2017–ongoing, and Kaspersky
2016–2018 reports contain extensive historic domain lists; ingestion deferred
to next collector pass against APT37.*

---

## IP Addresses

*No Archimedes-tracked APT37 IPs as of 2026-05-09. Historic infrastructure
from public reporting will ingest on next collector pass.*

---

## File Hashes

### Backdoor families (no specific hashes ingested yet)

| Family | Type | First Seen | Source |
|---|---|---|---|
| BirdCall (Android) | Android backdoor | Nov 2024 (compromise window opens) | ESET via The Record 2026-05-07 |
| BirdCall (Windows) | Windows backdoor | Nov 2024 (compromise window) | ESET via The Record 2026-05-07 |
| RokRAT | Windows RAT | 2017 (initial Cisco Talos disclosure) | Cisco Talos 2017–ongoing |
| BLUELIGHT | Windows backdoor | 2021 | Volexity InkySquid 2021 |
| KARAE | Backdoor (downloader) | pre-2018 | FireEye/Mandiant 2018 |
| DOGCALL | Backdoor | pre-2018 | FireEye/Mandiant 2018 |
| CORALDECK | Exfiltration tool | pre-2018 | FireEye/Mandiant 2018 |
| POORAIM | Backdoor (AOL IM C2) | pre-2018 | FireEye/Mandiant 2018 |
| RUHAPPY | Wiper (suspected MBR-overwrite) | pre-2018 | FireEye/Mandiant 2018 |
| SLOWDRIFT | Downloader (cloud C2) | pre-2018 | FireEye/Mandiant 2018 |
| HAPPYWORK | Downloader | pre-2018 | FireEye/Mandiant 2018 |
| MILKDROP | Loader | pre-2018 | FireEye/Mandiant 2018 |
| Konni (cluster overlap) | Windows + Android RAT | 2014–ongoing | Multi-vendor; cluster overlap with Kimsuky debated |

**Recommended next step:** ingest current YARA rules and SHA256 hash
appendices from ESET BirdCall report, Volexity InkySquid (2021) appendix,
Cisco Talos RokRAT publications, and FireEye/Mandiant 2018 appendix on next
collector pass against APT37.

---

## Registry Indicators

*No actor-specific registry artifacts catalogued in this scaffold. APT37
persistence via T1547.001 (Run keys), T1547.009 (Shortcut Modification),
and T1053.005 (Scheduled Task) is documented at TTP level in `profile.md`.
RokRAT and adjacent implants have published Run-key indicators in the
underlying vendor reports; ingestion deferred to next collector pass.*

---

## Scheduled Task Indicators

*No specific scheduled-task names catalogued in this scaffold. APT37 uses
T1053.005 generically; defender hunt should be on anomalous task creators
and unusual command lines rather than specific task names (which rotate
per campaign).*

---

## Cloud C2 Infrastructure

| Pattern | Description | Source |
|---|---|---|
| pCloud as bidirectional C2 | RokRAT and adjacent implants use pCloud API as C2 channel | Cisco Talos 2017–ongoing |
| Yandex Disk as bidirectional C2 | RokRAT variants use Yandex Disk for C2 and exfil | Cisco Talos, Kaspersky |
| Dropbox as bidirectional C2 | RokRAT and BLUELIGHT variants documented using Dropbox | Volexity 2021, Cisco Talos |
| Google Drive as exfil | Documented across multiple APT37 campaigns | Multi-vendor |
| Compromised regional web infrastructure | Strategic-website-compromise pattern (Volexity 2021 — South Korean newspaper) | Volexity 2021 |
| Compromised Android distribution platform | Sqgame APK supply-chain (ESET 2026) | ESET via The Record 2026-05-07 |

---

## Targeting and Distribution Patterns

| Pattern | Description | Source |
|---|---|---|
| Ethnic-Korean diaspora targeting (Yanbian) | Sqgame compromise targets ethnic Koreans in Yanbian Korean Autonomous Prefecture, China — likely refugees/defectors per ESET | ESET via The Record 2026-05-07 |
| Android APK web-browser sideload | Compromised APKs delivered via web browser download from compromised gaming platform (NOT Google Play) | ESET via The Record 2026-05-07 |
| Korean-language HWP spearphishing | Hancom Office document-borne lure infrastructure historically primary | Cisco Talos 2017–ongoing, FireEye 2018 |
| South Korean civil-society / journalist targeting | Strategic-website compromise of Korean newspaper (BLUELIGHT) | Volexity 2021 |
| Defense-think-tank targeting (occasional) | A&D-adjacent: research orgs studying DPRK military programs | FireEye/Mandiant 2018 |

---

## Detection Queries (Hunt Guidance)

### 1. Cloud-platform C2 hunt — outbound to pCloud / Yandex Disk

**Splunk SPL:**

```spl
index=defenseclaw_local sourcetype=proxy OR sourcetype=firewall
| search dest_domain IN ("api.pcloud.com", "*.pcloud.com",
                          "cloud-api.yandex.net", "webdav.yandex.com",
                          "*.dropboxapi.com")
| stats count, sum(bytes_out) as exfil_bytes by user, src_ip, dest_domain
| where exfil_bytes > 10485760
| sort - exfil_bytes
```

False-positive consideration: legitimate user use of pCloud, Yandex Disk,
and Dropbox is common. Tune by allowlisting known-business-purpose users
and focusing on non-developer / non-marketing endpoints. Look for high
bidirectional volume from endpoints that don't normally use these services.

### 2. HWP (Hancom Office) execution from email-delivered files

**Splunk SPL:**

```spl
index=defenseclaw_local sourcetype=endpoint
| search (process_name="hwp.exe" OR process_name="Hwp70.exe"
          OR file_extension=".hwp" OR file_extension=".hwpx")
| eval lure_origin = case(parent_process_name="OUTLOOK.EXE", "email",
                           parent_process_name="chrome.exe", "browser",
                           parent_process_name="firefox.exe", "browser",
                           1=1, "other")
| where lure_origin = "email"
| stats count by user, host, file_path
```

False-positive consideration: legitimate business reasons for HWP files
exist for Korea-touching business units. Tune by user role / business unit
allowlist; alert primarily on users without legitimate Korean-document
business purpose.

### 3. Anomalous Korean-language news-site visits with subsequent endpoint
indicator (strategic-website-compromise hunt)

**Pseudo-logic (proxy + EDR correlation):**

```
JOIN proxy_logs WHERE dest_domain IN (<korean-language-news-site-list>)
WITH endpoint_logs WHERE process_create OR file_create
WITHIN 5 minutes of proxy_log.time
GROUP BY user, host
ALERT IF endpoint event includes new persistence (Run key, scheduled task)
       OR new outbound connection to non-news domain
```

False-positive consideration: legitimate Korean-language news consumption
is benign. Hunt for the *combination* of Korean-news-visit + immediate
endpoint persistence event. Tune list of monitored news sites by relevance.

### 4. Mobile-device sideload posture review (Android — for managed devices)

**EDR / MTD pseudo-logic:**

```
ON ANDROID DEVICES under MDM:
  CHECK setting: install_unknown_sources
  ALERT IF install_unknown_sources = enabled for any user
  ENUMERATE installed apps NOT FROM Google Play
  ALERT IF any non-Play app installed in last 90 days
```

False-positive consideration: enterprise app stores and side-loaded LOB
apps are legitimate on managed devices. Tune by allowlisting known-good
enterprise app sources. Hunt primarily on personal-profile or BYOD devices
with corporate-resource access.

### 5. RokRAT / BLUELIGHT process-pattern hunt (legacy but still relevant)

**EDR pseudo-logic:**

```
ON HOSTS:
  ALERT IF process tree:
    - Office product (winword.exe, excel.exe) OR HWP (hwp.exe)
    - spawns powershell.exe with encoded command (T1059.001 + T1027)
    - spawns child process making outbound connection to cloud-storage API
    WITHIN 60 seconds
```

False-positive consideration: legitimate macros that integrate with cloud
services exist (rare in normal corporate use). Tune by user role.

---

## Sources

- [MITRE ATT&CK G0067 — APT37](https://attack.mitre.org/groups/G0067/) — A1
- [FireEye / Mandiant: APT37 (REAPER) — The Overlooked North Korean Actor (Feb 2018)](https://www.mandiant.com/resources/reports/apt37-overlooked-north-korean-actor) — A1
- [Cisco Talos: Korea In The Crosshairs / Group123 (2018)](https://blog.talosintelligence.com/korea-in-crosshairs/) — A1
- [Cisco Talos: ROKRAT Reloaded (2017)](https://blog.talosintelligence.com/rokrat-reloaded/) — A1
- [Kaspersky: Operation Daybreak — ScarCruft (2016)](https://securelist.com/operation-daybreak/75100/) — A1
- [Kaspersky Securelist: ScarCruft continues to evolve (2018)](https://securelist.com/scarcruft-continues-to-evolve-introduces-bluetooth-harvester/90729/) — A1
- [Volexity: InkySquid — North Korean APT exploits browser exploits and BLUELIGHT (2021)](https://www.volexity.com/blog/2021/08/17/north-korean-apt-inkysquid-infects-victims-using-browser-exploits/) — A1
- [ESET via The Record (Jonathan Greig, 2026-05-07): APT37 Sqgame supply-chain — BirdCall Android + Windows backdoor](https://therecord.media/north-korean-hackers-target-ethnic-koreans-in-china) — A2 (B for The Record relay; A for ESET originating research per source-grades.yaml ratification commit `a49c576`)
- finding-2026-05-07-0004 — ingested ESET-via-The-Record finding feeding this dossier
- Adobe Security Bulletin APSB18-03 — out-of-band patch for CVE-2018-4878 — A1

---

*First-pass scaffold authored 2026-05-09. Ingestion of full historical IOC
appendices from FireEye/Mandiant 2018, Kaspersky 2016–2018, Cisco Talos
2017–ongoing, and Volexity 2021 deferred to next collector pass against APT37.
Hard Rule 2 honored: every attribution and indicator herein traces to a cited
public source. Hard Rule 4 honored: no active scanning of Sqgame infrastructure
performed; passive enrichment only per LEGAL-POLICY.md.*
