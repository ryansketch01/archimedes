## 📣 Discord Summary

Good afternoon. Here's your 1600 brief — 2026-06-01.

🚨 **Active Threats**

- **[CVE-2026-41089 Netlogon — ITW per Belgian CCB](https://ccb.belgium.be/en)** — CCB observed Netlogon-vector exploitation against unpatched DCs Monday; BleepingComputer and SecurityWeek re-report. Leading hypothesis is authenticated-to-DA escalation, not cold-start cross-domain — both drive the same action. No attribution. *Confirm the May Patch Tuesday rollup is on every DC today.*
- **[Miasma — Shai-Hulud npm wave hits @redhat-cloud-services](https://socket.dev/blog)** — Socket names the wave Monday; novel Anthropic-API-impersonation C2. Tooling-lineage may trace to TeamPCP per Socket; *Archimedes does not extend operator attribution.* *DIB CI/CD: grep manifests for @redhat-cloud-services, pin last-known-good, rotate touched pipeline secrets.*

🔓 **Vulnerabilities**

- **[CVE-2026-0826 HP Poly VVX/Trio unauth RCE zero-day — patched today](https://www.rapid7.com/blog/)** — Rapid7 ships a 5-month coordinated disclosure; RCE reachable when ICE is enabled; Metasploit concurrent. ICE factory default is OFF but provisioning templates / Teams Direct Routing / CUCM / MSP golden-images may enable it. *Verify ICE in provisioning templates, not just device-level.*
- **[CVE-2024-21182 Oracle WebLogic — CISA KEV, FCEB due Thursday June 4](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)** — DFARS / CMMC do not mandate KEV inheritance; treat as elevated-urgency signal. T3/IIOP exposure concentrates in legacy / shadow-IT / acquisition-inherited WebLogic. *Inventory including acquisitions; confirm T3/IIOP not public-exposed.*
- **CVE-2026-0257 PAN-OS** carry-forward — KEV federal deadline closes EOD tonight; no new substance.
