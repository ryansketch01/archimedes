---
actor_id: "026"
actor_name: Cavern Manticore
last_updated: 2026-07-07
admiralty_grade: A2
tlp: CLEAR
---

# Cavern Manticore — IOC Reference

**Actor #026** · Source of record for the structured sidecar `iocs.yaml`.

All indicators below inherit from a single originating source — Check Point Research (relayed by The Hacker News), CPR primary not directly retrieved. Admiralty A2, WEP "likely," single-source veto applied. Treat as single-source pending independent corroboration. 13 IOCs total.

**First-party Splunk sentinel (2026-07-07):** 0 hits over -90d across `defenseclaw_local` and `archimedes` on the C2 domain and distinctive DLL filenames. Per Hard Rule 8, silent Splunk does NOT disconfirm — Frank is not an Israeli/Egyptian/UAE IT-provider or government org matching the victim profile. Visibility-bounded null, not negative evidence.

---

## 1. CVEs Actively Exploited

Referenced **by ID only** per Hard Rule 3 — no exploitation mechanism, no PoC. Consult vendor advisories for affected products and fixes.

| CVE | Role |
|---|---|
| CVE-2025-52691 | Exploited by actor for initial access |
| CVE-2025-68613 | Exploited by actor for initial access |
| CVE-2025-9316 | Exploited by actor for initial access |
| CVE-2025-34291 | Exploited by actor for initial access |
| CVE-2025-54068 | Exploited by actor for initial access |

---

## 2. Malicious Delivery Domains

| Domain | Role | First Seen |
|---|---|---|
| hospitalinstallation[.]com | Cavern C2 | 2026-07-06 |

*(Network-infrastructure TTL 90 days — re-validate before long-term reliance.)*

---

## 3. IP Addresses

No documented IP indicators at this time.

---

## 4. File Hashes

No file hashes documented at this time. The originating report provides DLL **filenames** (side-load artifacts) but no hashes — see Section 6.

---

## 5. Registry Indicators

No documented registry indicators at this time.

---

## 6. File Artifacts — Sideloaded / Malicious DLLs

DLL filenames used in side-loading (T1574.002). These are **filename/artifact hunt indicators**, not hashes — name-based hunting is lower-fidelity and prone to false positives (esp. `uxtheme.dll`, a legitimate Windows component). Hunt on **path + loading-process context**, not name alone.

| Filename | Role | Note |
|---|---|---|
| uxtheme.dll | Sideloaded/malicious DLL | Name matches a legitimate Windows component — hunt on non-System32 load paths |
| n-HTCommp.dll | Sideloaded/malicious DLL | Non-standard name; higher-fidelity |
| mhm.dll | Sideloaded/malicious DLL | |
| db.dll | Sideloaded/malicious DLL | Common short name — low fidelity alone |
| ode.dll | Sideloaded/malicious DLL | |
| n-ten.dll | Sideloaded/malicious DLL | Non-standard name; higher-fidelity |
| n-sws.dll | Sideloaded/malicious DLL | Non-standard name; higher-fidelity |

---

## 7. Cloud C2 Infrastructure

No documented cloud-service C2 at this time. The single documented C2 is the registered domain in Section 2.

---

## 8. Detection Queries (Hunt Guidance)

### Hunt A — Cavern C2 domain in DNS / proxy / web logs (Splunk)

```spl
index=defenseclaw_local (sourcetype=dns OR sourcetype=proxy OR sourcetype=stream:http)
  hospitalinstallation.com
| stats count min(_time) as first_seen max(_time) as last_seen
        values(query) as queries values(url) as urls by src_ip, host
```

False-positive note: the domain is distinctive; any hit warrants investigation. Confirm resolution to attacker infrastructure before blocking downstream services with similar names.

### Hunt B — Cavern DLL side-load artifacts (EDR / Sysmon)

```spl
index=defenseclaw_local (sourcetype=Sysmon EventCode=7)   # Image Loaded
  (ImageLoaded="*\\n-HTCommp.dll" OR ImageLoaded="*\\n-ten.dll"
   OR ImageLoaded="*\\n-sws.dll" OR ImageLoaded="*\\mhm.dll"
   OR ImageLoaded="*\\ode.dll" OR ImageLoaded="*\\db.dll"
   OR (ImageLoaded="*\\uxtheme.dll" AND NOT ImageLoaded="C:\\Windows\\System32\\uxtheme.dll"
       AND NOT ImageLoaded="C:\\Windows\\SysWOW64\\uxtheme.dll"))
| stats count values(ImageLoaded) as dll_paths values(Image) as loading_process
        min(_time) as first_seen by host, User
```

False-positive note: `uxtheme.dll` and `db.dll` are common names — the query excludes legitimate System32/SysWOW64 `uxtheme.dll` load paths and relies on non-standard load locations. Tune the `db.dll` term against your environment baseline; the `n-*.dll` and `mhm.dll`/`ode.dll` names are higher-fidelity. Tie back to T1574.002 (DLL Side-Loading) and T1036.005 (Masquerading).

---

## 9. Sources

- The Hacker News (2026-07-06), relaying Check Point Research — RELAY, not independent corroboration.
- Check Point Research (CPR) — originating primary; **not directly retrieved** at intake. Provisional-A.
- Originating finding: `finding-2026-07-06-0001`.

*IOC set is single-source and will grow / firm up on direct CPR retrieval or independent second-IR-vendor corroboration.*
