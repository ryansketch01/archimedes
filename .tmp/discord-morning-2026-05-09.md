**Morning Brief — 2026-05-09** · TLP:CLEAR

**Lead:** Ivanti EPMM CVE-2026-6973 federal patch deadline runs to midnight Sunday — **T-40h from compose**. On-prem EPMM operators including any A&D contractors still running on-prem MDM should treat the deadline as binding regardless of FCEB scope. No new exploitation telemetry overnight; deadline urgency is the lead.

**New corpus item:** OpenC3 COSMOS spacecraft C2 software — five-CVE cluster, two Critical 9.6, all patched in 7.0.0. NASA and BAE Systems on the vendor user list (deployment density not independently corroborated). Single-source veto applied (NVD + GHSA share CNA-process basis); WEP capped at likely. Treat 6.x→7.0 as a major-version migration, not a routine patch. Vuln-tracker handoff: open cluster dossier. **Digraph A2 · WEP likely · finding-2026-05-09-0001.**

**Carry / monitoring:**
- **Dirty Frag (CVE-2026-43284 / CVE-2026-43500)** — 72h MSTIC tripwire at T-48h; no second A-grade vendor confirmation overnight.
- **MuddyWater (#022)** Rapid7-attribution auto-downgrade clock evaluates **today 12:18 EDT** (~4h from post). If unbroken, finding re-grades to C3.
- **Patch backlog:** LiteLLM 2026-05-11 (FCEB), IIS HTTP.sys 2026-05-13, PAN-OS 2026-05-13/2026-05-28, Linux Copy Fail 2026-05-15, FortiManager 2026-05-25.
- Polish ABW (APT28/APT29/UNC1151), Operation Silent Rotor, RansomHouse-Trellix, PCPJack — status-only carry.

**First-party Splunk:** clean across `archimedes` and `defenseclaw_local` for in-scope IOCs. Spacecraft-C2 instrumentation not in scope (Hard Rule 8 absence-of-evidence).

Full brief: `threats/briefs/2026-05-09-morning.md` (752 words, 9 findings referenced, pre-flight 12/12).
