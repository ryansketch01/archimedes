# MiniPlasma (CVE-2020-17103) — Executive Summary

**Windows LPE: 2020-Regression Zero-Day | CVSS 7.8 | Full Public PoC | SYSTEM Shell | PATCHED at June 2026 Patch Tuesday**

A Windows local privilege escalation vulnerability in `cldflt.sys` (Cloud Files Mini Filter Driver), originally patched in December 2020 as CVE-2020-17103, was confirmed **fully exploitable on fully patched Windows 11 systems through May 2026** after the original fix regressed. Security researcher Nightmare-Eclipse (also behind RedSun, UnDefend, YellowKey, and GreenPlasma) released a full weaponized PoC dubbed **MiniPlasma** that spawns a SYSTEM shell from a standard user account. BleepingComputer and Will Dormann (Tharros) independently confirmed the exploit worked against the May 2026 Patch Tuesday updates. **Microsoft fixed MiniPlasma at June 2026 Patch Tuesday (2026-06-09/10) under the original CVE-2020-17103** — confirmed by BleepingComputer and The Hacker News, alongside YellowKey (CVE-2026-45585) and GreenPlasma (CVE-2026-45586). No active exploitation was reported prior to the patch; never CISA-KEV-listed. Apply the June 2026 Windows updates to remediate.

*TLP: WHITE | Admiralty: A1 | Created: 2026-05-18 | Updated: 2026-06-10*
