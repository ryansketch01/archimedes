📋 **FORMAT PREVIEW** — new Layer 2 format, starts tomorrow's brief. Real 08:00 brief unchanged above.

Good morning. Here's your 0800 brief — Monday, May 11.

🚨 **Active Threats**

• **[Checkmarx Jenkins AST plugin compromised in supply-chain attack](https://www.securityweek.com/checkmarx-jenkins-ast-plugin-compromised-in-supply-chain-attack/)** — Checkmarx warned Friday May 9 of a malicious Jenkins AST plugin on the Marketplace; weekend variants surfaced on GitHub. Remediation `2.0.13-848` is out. **DIB CI/CD:** pin to fix version *now*, capture plugin hashes for IOC backfill.

• **[SailPoint discloses GitHub repository hack](https://www.securityweek.com/sailpoint-discloses-github-repository-hack/)** — SailPoint disclosed an April 20 incident; a third-party app vulnerability exposed a subset of its GitHub repos. No production customer data accessed; some customer info was in the repos, extent undisclosed. SecurityWeek floats a possible TeamPCP link; *Archimedes does not endorse.*

🔓 **Vulnerabilities**

• **CVE-2026-6973 (Ivanti EPMM on-prem):** federal patch deadline expired last night. Unpatched on-prem fleet now in non-compliance + standing exploitation risk.
• **CVE-2026-42208 (BerriAI LiteLLM):** KEV deadline closes *today* (FCEB only). LiteLLM-proxying shops: inventory and patch *by EOD*.

🕵️ **Actor Activity**

• **TeamPCP** — Jenkins AST Marketplace channel is brand-new TTP in the corpus. Actor-profiler picks it up next pass.
• **Lapsus$ / DEV-0537** — second cumulative corpus reference (April 2026 Checkmarx data release). Not in roster; `/new-actor` is your call.

📰 **Other Signal**

• **MONITORING — [SOCRadar's "Operation HookedWing"](https://www.securityweek.com/over-500-organizations-hit-in-years-long-phishing-campaign/):** 4-year, 500+ orgs across 7 sectors, no attribution. Aviation token = commercial travel / airlines / airport authorities — *not* A&D primes. Held pending IOCs.
