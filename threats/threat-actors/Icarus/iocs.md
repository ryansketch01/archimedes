---
actor_id: "025"
actor_name: Icarus
last_updated: 2026-07-06
admiralty_grade: B2
tlp: CLEAR
source_of_record: true
sidecar: iocs.yaml
---

# Icarus — Indicators of Compromise

> ⚠️ **No IOC values published at time of tracking.** No file hashes, domains,
> IP addresses, or attacker infrastructure appeared in any source for the
> single documented Icarus campaign (finding-2026-06-19-0003). Detection for
> Icarus is **behavioral/TTP-based only** — see Detection Queries below.
> Prioritize OAuth-integration-governance hardening over static IOC matching.

---

## CVEs Actively Exploited

No documented CVE exploitation at this time. The Klue/Salesforce campaign used
an OAuth-integration-abuse pattern (compromised legacy integration credential →
OAuth token harvesting), **not** a CVE-trackable vulnerability. No CVE assigned.

---

## Malicious Delivery Domains

No documented delivery domains at this time.

---

## IP Addresses

No documented attacker IP addresses at this time.

---

## File Hashes

No documented file hashes at this time. No custom malware, loader, or backdoor
has been attributed to Icarus.

---

## Registry Indicators

No documented registry indicators at this time. (Icarus tradecraft is
cloud/SaaS-side OAuth-token abuse, not endpoint persistence.)

---

## Scheduled Task Indicators

No documented scheduled-task indicators at this time.

---

## Cloud C2 Infrastructure

No documented C2 infrastructure at this time. Data exfiltration was performed
directly against victim Salesforce REST API endpoints; no dedicated C2 was
published.

---

## Detection Queries (Hunt Guidance)

Because no indicator values exist, detection is **pattern/behavioral only**. The
following hunt guidance targets the Icarus *tradecraft* (third-party OAuth-
integration abuse against Salesforce tenants), written generically. It contains
**no fabricated indicator values**. Full queries live in `iocs.yaml`
`hunt_queries`.

### Defender-pattern hints (context, NOT extractable IOCs)

- **Python-`urllib` user-agent strings** referenced against the Salesforce REST
  API in vendor disclosures. A pattern hint, not a signature — legitimate
  script-based integrations produce the same user agents.
- **Salesforce REST API endpoint patterns** with high-velocity extraction
  (per SecurityWeek single-publisher: ~1,000 queries in 15 minutes; extraction
  windows >6 hours).

### Hunt guidance summary

| Hunt ID | Platform | What it looks for |
|---|---|---|
| `icarus-hunt-oauth-token-usage-anomaly` | Salesforce / M365 | Anomalous connected-app OAuth API call volume vs. baseline |
| `icarus-hunt-python-urllib-user-agent-salesforce` | Salesforce / M365 | Non-browser (Python-urllib) user agents against the Salesforce REST API |
| `icarus-hunt-legacy-integration-credential-review` | Salesforce / M365 | Audit of stale / over-scoped connected apps and legacy integration credentials |

> All three are tuning-dependent and expect false positives from legitimate
> automation. Correlate the volume-anomaly and user-agent hunts before
> escalating; treat the credential-review query as an audit, not an alert.

---

## First-Party Splunk Status

Splunk first-party check over -90d returned **zero hits** (categorical,
visibility-bounded). Frank is **not** a Salesforce-Klue-integration tenant, so
this is a categorical null — silent Splunk does **not** disconfirm per Hard
Rule 8. No IOC corroboration bonus applied to scoring.

---

## Sources

- finding-2026-06-19-0003 (Archimedes finding — source of record)
- SecurityWeek (Ionut Arghire), 2026-06-19
- The Hacker News (Ravie Lakshmanan), 2026-06-19
- Huntress (IR-vendor primary; primary publication not retrieved at time of tracking)

---

*Created 2026-07-06. Indicator-empty by design — no IOC values were published
for the single documented Icarus campaign. Update when Huntress primary
research or a second IR vendor surfaces indicator values.*
