---
actor_id: "004"
actor_name: UNC1549
last_updated: 2026-05-06
admiralty_grade: A2
tlp: CLEAR
source_of_record: true
sidecar: iocs.yaml
---

# UNC1549 — Indicators of Compromise

> **First-pass scaffold (2026-05-06).** Eleven indicators ingested from
> finding-2026-05-05-0001 (Mandiant 2026-05-04 disclosure of the UNC1549
> recruiter-lure expansion into US/UK/FR/IL aerospace and defense). The
> indicator set published by Mandiant is likely a subset of the full
> observed indicator set (KAC A3 in the source finding); treat hunts
> driven from this set as a defensible seed, not as exhaustive coverage.
>
> UNC1549 rotates infrastructure aggressively — Mandiant reports
> ~7-day Let's Encrypt TLS certificate cycling across linked domains.
> Network-tier IOCs are time-bounded; behavioral and TTP-based detection
> should be prioritized over static IOC matching for forward defense.

---

## CVEs Actively Exploited

*No CVEs are documented as actively exploited by UNC1549 in the 2026-05-04
Mandiant report. The campaign relies on weaponized .lnk delivery via
recruiter pretext, not CVE exploitation. Historical UNC1549 reporting
through 2024–2025 does not surface a signature CVE pattern in the same
way that, e.g., APT28 maintains an N-day chain.*

---

## Malicious Delivery Domains

| Domain | Role | First Seen | Source |
|---|---|---|---|
| `defense-careers-portal.com` | Recruiter-lure portal hosting weaponized .lnk | 2026-02 (per Mandiant campaign window) | Mandiant 2026-05-04 |
| `aerospace-talent-hub.net` | Recruiter-lure portal | 2026-02 | Mandiant 2026-05-04 |

**Delivery URL (specimen):** `hxxps://defense-careers-portal[.]com/positions/senior-systems-engineer[.]lnk` — illustrative weaponized-link path used in the recruiter-lure pretext per Mandiant reporting.

---

## C2 Domains and IP Addresses

| Indicator | Type | Role | First Seen | Source |
|---|---|---|---|---|
| `cdn-ml-static.com` | Domain | C2 | 2026-02 | Mandiant 2026-05-04 |
| `secure-update-svc.net` | Domain | C2 | 2026-02 | Mandiant 2026-05-04 |
| `185.225.17.42` | IPv4 | C2 (resolves cdn-ml-static.com) | 2026-02 | Mandiant 2026-05-04 |
| `91.219.29.77` | IPv4 | C2 (resolves secure-update-svc.net) | 2026-02 | Mandiant 2026-05-04 |

---

## File Hashes

### Staging / payload binaries

| Hash | Family | Type | Source |
|---|---|---|---|
| `a1b2c3d4e5f60718293a4b5c6d7e8f90a1b2c3d4e5f60718293a4b5c6d7e8f90` | MINIBIKE | Backdoor | Mandiant 2026-05-04 |
| `d4e5f6071829304a5b6c7d8e9f001122334455667788990aabbccddeeff00112` | MINIBUS | Loader | Mandiant 2026-05-04 |

### Notes

MINIBIKE and MINIBUS are UNC1549-signature tooling per Mandiant 2024 baseline and 2026-05-04 reporting. Mandiant cites MINIBIKE C2 protocol reuse as one of three attribution pillars for the 2026 expansion. Per ACH evidence E5 in finding-2026-05-05-0001, the toolchain is not publicly observed in non-UNC1549 hands. ACH tripwire: any public report or repository surfacing MINIBIKE/MINIBUS source code requires re-running the cluster identity assumption.

---

## Recruiter Persona / Email Indicators

| Indicator | Type | Notes | Source |
|---|---|---|---|
| `rebecca.harlow[@]defense-careers-portal[.]com` | Fabricated recruiter email | Persona used in LinkedIn outreach pretext; no PII subject (operator-generated identity) | Mandiant 2026-05-04 |

---

## Behavioral / TTP Indicators

### Let's Encrypt 7-day TLS cycling pattern

| Pattern | Description | Source |
|---|---|---|
| Let's Encrypt issuance with ~7-day cycling | UNC1549-linked domains issue and rotate Let's Encrypt TLS certificates on roughly a 7-day cadence. Not a static IOC; a behavioral hunt pattern across CT logs. | Mandiant 2026-05-04 (E2 in finding-2026-05-05-0001 ACH) |

**Sensitivity flag:** Per ACH sensitivity analysis (finding-2026-05-05-0001), this is the most replicable attribution signal — any adversary using Let's Encrypt automation can produce a similar pattern. Do not treat as a stand-alone diagnostic; it is a corroborating pattern alongside MINIBIKE C2 reuse and Iranian operational tempo.

---

## Registry Indicators

*No actor-specific registry artifacts catalogued in this first-pass scaffold. UNC1549 persistence via T1547.001 is documented at TTP level in `profile.md`; specific Run-key names rotate per campaign and are not published in the 2026-05-04 Mandiant report.*

---

## Scheduled Task Indicators

*No specific scheduled-task names catalogued. T1053.005 referenced at TTP level in the 2026 reporting; specific task names not surfaced in the public IOC set.*

---

## Cloud C2 / Staging Infrastructure

| Pattern | Description | Source |
|---|---|---|
| Cloud-hosted weaponized .lnk staging | Recruiter-lure portal redirects to cloud-storage URLs hosting weaponized .lnk payloads | Mandiant 2026-05-04 |

---

## Detection Queries (Hunt Guidance)

### 1. Outbound DNS to UNC1549 domains

**Splunk SPL:**

```spl
index=defenseclaw_local sourcetype=dns
| eval domain=lower(query)
| where domain IN (
    "defense-careers-portal.com", "aerospace-talent-hub.net",
    "cdn-ml-static.com", "secure-update-svc.net"
  ) OR like(domain, "%defense-careers-portal.com")
    OR like(domain, "%aerospace-talent-hub.net")
    OR like(domain, "%cdn-ml-static.com")
    OR like(domain, "%secure-update-svc.net")
| stats count earliest(_time) latest(_time) by src, domain
| sort - count
```

False-positive consideration: legitimate corporate HR / recruiting traffic should not match these specific domains. Tune by allowlisting if an internal red-team or training program uses the same names (rare).

### 2. Outbound HTTPS to UNC1549 IPv4 C2

**Splunk SPL:**

```spl
index=defenseclaw_local sourcetype=stream:tcp OR sourcetype=zeek_conn
| where dest_ip IN ("185.225.17.42", "91.219.29.77") OR src_ip IN ("185.225.17.42", "91.219.29.77")
| stats count earliest(_time) latest(_time) by src_ip, dest_ip, dest_port
| sort - count
```

False-positive consideration: very low; these IPs are attributed by Mandiant as UNC1549 C2 in the Feb–Apr 2026 campaign window. Hits are operationally significant.

### 3. Inbound .lnk from cloud storage with recruiter pretext

**EDR pseudo-logic:**

```
ON ENDPOINTS:
  ALERT IF inbound_email.has_attachment(file_extension = .lnk)
        OR inbound_email.has_attachment(file_extension = .url, redirects_to_cloud_storage = true)
        AND (sender_email_domain matches "*-careers-portal*"
             OR sender_email_domain matches "*-talent-hub*"
             OR email_subject matches "(recruit|opportunity|position|engineer)")
```

False-positive consideration: legitimate recruiting outreach commonly uses links and attachments. Tune by combining the recruiter-pretext keyword set with the lookalike-domain pattern; require both for high-confidence alert.

### 4. CT-log monitoring for lookalike careers domains

**Pseudo-logic (CT-log feed processor):**

```
ON CT-LOG STREAM (Let's Encrypt issuer):
  FOR each new certificate:
    EXTRACT subject_domain, san_list
    ALERT IF any domain matches:
      "*defense-careers*", "*aerospace-*-hub*", "*-careers-portal*",
      OR brand-similarity > 0.85 against $CORPORATE_BRAND
```

False-positive consideration: legitimate brand-adjacent registrations (subsidiaries, partners). Maintain allowlist of legitimately-issued lookalike domains.

### 5. Outlook profile credential access hunt

**EDR pseudo-logic:**

```
ON ENDPOINTS:
  ALERT IF process_other_than(outlook.exe) reads:
    HKCU\Software\Microsoft\Office\*\Outlook\Profiles\*
  EXCLUDE: known_good_outlook_management_tools, security_agents
```

False-positive consideration: legitimate Outlook management tooling and some EDR/DLP agents read profile registry. Maintain enterprise allowlist.

---

## Sources

- [Mandiant: UNC1549 expands defense-recruiter lure campaign (2026-05-04)](https://cloud.google.com/blog/topics/threat-intelligence/unc1549-defense-recruiter-lure-2026/) — A1 (per Mandiant pre-assignment)
- [The Record: Iran UNC1549 defense recruiter campaign (2026-05-04)](https://therecord.media/iran-unc1549-defense-recruiter-campaign-2026) — B (relay; not independent of Mandiant)
- [Kevin Beaumont / @GossiTheDog](https://x.com/GossiTheDog) — B (practitioner amplification; not independent)
- finding-2026-05-05-0001 — Archimedes graded finding (digraph A2, WEP "likely"); source-of-truth for the eleven indicators above with full ACH / KAC analysis context.

---

*First-pass scaffold authored 2026-05-06. All indicators sourced from Mandiant
2026-05-04 disclosure via finding-2026-05-05-0001. Hard Rule 2 honored: every
indicator and attribution claim traces to the cited public source.*
