**Morning Brief — 2026-05-08** | TLP:CLEAR | 4 findings

**Lead:** Ivanti EPMM CVE-2026-6973 (A1) — KEV-listed, federal patch deadline **2026-05-10 (T-48h)**. On-prem only. Admin-auth RCE; January-2026 credential rotation is the load-bearing mitigation. Patch to 12.6.1.1 / 12.7.0.1 / 12.8.0.1 by Sunday.

**Other items:**
- Linux kernel "Dirty Frag" LPE (B2 / likely) — public PoC, no CVE, no patch, all major distros. Tripwire 2026-05-22.
- PCPJack worm vs TeamPCP (A2 / likely) — SentinelLabs hedges "could be a former operator"; single-source veto active. Five initial-access CVEs. SentinelOne primary URL flagged for collector follow-up.
- ClaudeBleed Chrome extension (C3 / roughly even chance) — LayerX research; partial Anthropic patch; no Archimedes-operations exposure.

**Patch backlog:** 5 binding deadlines in 20 days (Ivanti 5/10; PAN-OS 10.2/11.1 + IIS 5/13; Linux Copy Fail 5/15; FortiManager 5/25; PAN-OS 11.2/12.1 5/28).

**Iran watch:** No new tracked-actor activity. MuddyWater/Rapid7 auto-downgrade clock: ~28h remaining.

**First-party Splunk:** clean across `archimedes` and `defenseclaw_local` at compose.

Full brief: `threats/briefs/2026-05-08-morning.md` (committed to main).
