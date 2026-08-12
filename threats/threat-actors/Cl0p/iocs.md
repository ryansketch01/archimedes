---
actor_id: "018"
actor_name: Cl0p
last_updated: 2026-08-12
admiralty_grade: A1        # confirmed-campaign indicators; SUSPECTED 2026-Windchill indicators flagged B3 inline
tlp: CLEAR
---

# Cl0p — Known IOCs

**Actor #018.** Indicators are grouped by confidence. **CONFIRMED** indicators come from A-grade primary reporting on Cl0p's established campaigns (CISA AA23-158A, Google Threat Intelligence Group, vendor research). **SUSPECTED** indicators come from the 2026 PTC Windchill/FlexPLM campaign whose Cl0p attribution is **unconfirmed (B3/possibly)** — they are retained for hunting but must NOT be cited as confirmed Cl0p infrastructure. No credentials are stored (Hard Rule 7). All CVEs are recorded by ID only (Hard Rule 3).

> **First-party status (2026-08-12):** Splunk `defenseclaw_local` returned **0 hits** across all queryable Cl0p indicators. Visibility-bounded null (Frank is not a MOVEit/Cleo/Oracle-EBS/Windchill tenant) — neither corroboration nor disconfirmation. No IOC-corroboration bonus applied to scoring.

---

## 1. CVEs Exploited

| CVE | Platform | Campaign | Status |
|---|---|---|---|
| CVE-2021-27101 / -27102 / -27103 / -27104 | Accellion FTA | Accellion 2020–2021 | Confirmed (historical) |
| CVE-2023-0669 | Fortra GoAnywhere MFT | GoAnywhere 2023 | Confirmed (historical) |
| CVE-2023-27350 | PaperCut NG/MF | PaperCut 2023 | Confirmed (Microsoft; Cl0p + LockBit) |
| CVE-2023-34362 | Progress MOVEit Transfer | MOVEit 2023 | Confirmed (CISA AA23-158A) — primary |
| CVE-2023-35036 / CVE-2023-35708 | Progress MOVEit Transfer | MOVEit 2023 (follow-on) | Confirmed (same family) |
| CVE-2024-50623 | Cleo Harmony/VLTrader/LexiCom | Cleo 2024 | Confirmed |
| CVE-2024-55956 | Cleo (Autorun file-write) | Cleo 2024 | Confirmed |
| CVE-2025-61882 | Oracle E-Business Suite | Oracle EBS 2025 | Confirmed (GTIG) — zero-day from ~2025-08-09 |
| CVE-2025-61884 | Oracle E-Business Suite | Oracle EBS 2025 | Confirmed (related) |
| CVE-2020-1472 (ZeroLogon) | Windows Netlogon | South Staffordshire Water | Confirmed (privesc; historical) |
| **CVE-2026-12569** | **PTC Windchill / FlexPLM** | **Windchill 2026** | **Exploitation CONFIRMED (CISA KEV 2026-06-25); Cl0p attribution SUSPECTED-ONLY (B3)** |

---

## 2. Malicious Filenames / Webshells

| Indicator | Type | Campaign | Confidence |
|---|---|---|---|
| `human2.aspx` (and variants) | LEMURLOOT webshell dropped on MOVEit web root | MOVEit 2023 | Confirmed (CISA) |
| LEMURLOOT | C#/ASP.NET webshell (hard-coded-password auth) | MOVEit 2023 | Confirmed |
| DEWMODE | PHP webshell | Accellion 2020–2021 | Confirmed |
| GOLDVEIN.JAVA | Java downloader (fake "TLSv3.1" beacon) | Oracle EBS 2025 | Confirmed (GTIG) |
| SAGEGIFT / SAGELEAF / SAGEWAVE | WebLogic loader / dropper / servlet-filter chain | Oracle EBS 2025 | Confirmed (GTIG) |
| `GW.class`, `payload.bin`, `dpr_*.jsp` | Windchill filesystem artifacts (from CVE-2026-4681 family profile) | Windchill 2026 | **Related family guidance — not re-confirmed as 12569-specific** |

---

## 3. IP Addresses (Oracle EBS 2025 — GTIG, Confirmed)

| IP | Role |
|---|---|
| `200.107.207.26` | Exploitation attempts (UiServlet, SyncServlet) |
| `161.97.99.49` | UiServlet exploitation attempts |
| `162.55.17.215` (:443) | GOLDVEIN.JAVA C2 |
| `104.194.11.200` (:443) | GOLDVEIN.JAVA C2 |

> Network infrastructure rotates per campaign; treat these as campaign-scoped (2025 Oracle EBS) with a network-infrastructure TTL.

---

## 4. Extortion Email Addresses

| Address | Campaign | Confidence |
|---|---|---|
| `support@pubstorm.com` | Oracle EBS 2025 | Confirmed (GTIG) |
| `support@pubstorm.net` | Oracle EBS 2025 | Confirmed (GTIG) |
| `support@cryptohox.com` | PTC Windchill/FlexPLM 2026 | **SUSPECTED (B3)** — ReliaQuest characterizes as "a known Clop address"; NOT independently verified in-corpus |

*(Not credentials — extortion contact addresses. Hard Rule 7 n/a.)*

---

## 5. Exploitation Endpoints / Paths (for detection)

**Oracle EBS 2025 (Confirmed, GTIG):**
- `/OA_HTML/SyncServlet`
- `/OA_HTML/configurator/UiServlet`
- `/OA_HTML/OA.jsp?page=/oracle/apps/xdo/oa/template/webui/TemplatePreviewPG&TemplateCode=<TMP|DEF><16_HEX>&TemplateType=<XSL-TEXT|XML>`
- Malicious templates stored in DB tables `XDO_TEMPLATES_B` and `XDO_LOBS` (template codes prefixed `TMP`/`DEF`)

**MOVEit 2023 (Confirmed, CISA):**
- Unexpected `.aspx` (esp. `human2.aspx`) under the MOVEit Transfer web root

**Windchill 2026 (SUSPECTED campaign; exploitation confirmed):**
- Suspicious requests to `/servlet/WindchillGW/` and `/servlet/WindchillAuthGW/`; unexpected `.jsp` webshells

---

## 6. Detection Queries (Hunt Guidance)

```spl
# Oracle EBS 2025 — Cl0p C2 / exploitation-source IPs
index=* (dest_ip="162.55.17.215" OR dest_ip="104.194.11.200" OR src_ip="200.107.207.26" OR src_ip="161.97.99.49")
| stats count by _time src_ip dest_ip dest_port sourcetype

# Extortion sender addresses (mail gateway / O365 message trace)
index=* (sender="support@pubstorm.com" OR sender="support@pubstorm.net" OR sender="support@cryptohox.com")
| stats count by _time sender recipient subject

# MOVEit webshell hunt — LEMURLOOT / human2.aspx on file-transfer hosts
index=* (host IN (<moveit_hosts>)) (uri_path="*human2.aspx*" OR file_name="human2.aspx")
| stats count by _time host uri_path src_ip

# Oracle EBS — SyncServlet / UiServlet exploitation attempts
index=* (uri_path="/OA_HTML/SyncServlet" OR uri_path="/OA_HTML/configurator/UiServlet")
| stats count by _time host src_ip status uri_path

# Windchill (SUSPECTED campaign) — webshell / gateway servlet abuse
index=* (uri_path="/servlet/WindchillGW/*" OR uri_path="/servlet/WindchillAuthGW/*" OR file_name="*.jsp")
| stats count by _time host uri_path src_ip
```

> EDR/file-integrity: alert on new `.aspx`/`.jsp`/`.php` webshell files in the web roots of internet-facing MFT/ERP/PLM applications; alert on those servers making outbound HTTPS to non-baseline hosts (GOLDVEIN-style C2) or serving anomalously large downloads (bulk exfiltration).

---

## 7. Sources

- **CISA/FBI AA23-158A** — MOVEit / LEMURLOOT / `human2.aspx` / TTPs (A)
- **Google Threat Intelligence Group** — Oracle EBS: CVE-2025-61882/-61884, GOLDVEIN.JAVA, SAGEGIFT/SAGELEAF/SAGEWAVE, C2 IPs, `pubstorm` addresses, endpoints (A)
- **Mandiant/Google** — MOVEit FIN11/UNC4857 attribution (A)
- **Recorded Future/Insikt, SocRadar, ZeroFox** — Cleo CVE-2024-50623/-55956 campaign (B)
- **Archimedes findings** finding-2026-07-24-flash-0600-0001, finding-2026-07-27-0001 — Windchill CVE-2026-12569 exploitation (A1) + Cl0p tie (B3/suspected)
- **Archimedes** raw-2026-07-21-flash-0000-001 (Oracle EBS victim ledger), finding-2026-05-11-0004 (South Staffordshire Water / ZeroLogon)
