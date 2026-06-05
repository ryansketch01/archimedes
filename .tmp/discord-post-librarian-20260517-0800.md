Good morning. Here's your 0800 brief — 2026-05-17.

🚨 **Active Threats**

- **[CVE-2026-20182 (Cisco Catalyst SD-WAN auth bypass) — federal KEV deadline lands TODAY (Sunday)](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)** — CVSS 10.0; Cisco Talos attributes active exploitation to UAT-8616 (2-year track record). Talos is Cisco's threat-intel arm — *visibility-skew caveat carries forward*; no Mandiant / Volexity / Unit 42 / MSTIC / CrowdStrike parallel attribution overnight. **DIB / CMMC partner-flow estates:** confirm patch + ED-26-03 attestation status *by end of day*.

🔓 **Vulnerabilities**

- **CVE-2026-42897 (Exchange OWA XSS):** KEV deadline *Friday May 29 — T-12*. MSRC mitigation unchanged (EEMS or EOMT); no GA patch. >48h from initial KEV listing and Mandiant / Volexity / Unit 42 / MSTIC / CrowdStrike still silent — *single-source veto holds*.
- **CVE-2026-42945 (NGINX Rift):** PoC published Friday May 15/16; no new exploitation signal overnight. ASLR state determines RCE vs DoS. *Per Hard Rule 3 we do not link the PoC repo.*

📰 **Other Signal**

- **[Grafana discloses GitHub-token-enabled codebase download; THN attributes to CoinbaseCartel — fourth software-vendor supply-chain incident in 30 days](https://thehackernews.com/)** — Per The Hacker News, Grafana refused a subsequent extortion attempt per FBI guidance and states no customer data / no customer systems affected. Halcyon and Fortinet have framed CoinbaseCartel as an ecosystem offshoot of ShinyHunters / Scattered Spider / LAPSUS$ — *Archimedes does not propagate this as direct Scattered Spider attribution of the Grafana incident*; CoinbaseCartel is not on roster. **The pattern is the takeaway, not the incident:** SailPoint May 11, Checkmarx May 11, OpenAI/TanStack May 14, Grafana May 17 — different actors, different mechanisms, same incident shape. A&D-exposure depends on repo contents (not yet characterized). Generic GitHub-token-hygiene and secrets-scanning guidance applies.
