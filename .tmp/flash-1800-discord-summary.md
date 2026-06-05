## FLASH — Symantec attributes Q1 2026 multi-victim espionage campaign to MuddyWater (Seedworm)
*2026-05-13 18:10 EDT · A2 · WEP: likely · TLP:CLEAR*

**What.** Symantec attributes a Q1 2026 nine-victim espionage campaign to MuddyWater (#022; Seedworm, Static Kitten) — "widely believed to be linked" to Iran MOIS (Symantec's hedge preserved). Case study: South Korean electronics maker, breached Feb 20 / detected Feb 27. Eight further victims span MENA gov/aviation, SEA industrial, LatAm finance, global education. Three deltas: new credential-theft tool **ChromElevator**; two novel DLL sideloading pairs — Fortemedia `fmapp.exe → fmapp.dll` and SentinelOne `sentinelmemoryscanner.exe → sentinelagentcore.dll` (defensive-EDR brand impersonation); Node.js orchestrating PowerShell. Exfil via `sendit[.]sh`.

**Impact.** Symantec names **no A&D victim**. Industrial Cyber's relay-introduced "U.S. defense/aerospace software supplier" claim absent from primary and **not propagated** (conflation w/ March 2026 Dindoor/Fakeset). Footprint extends beyond MENA gov/telecom anchor into supplier-tier electronics + industrial mfg. Both DLL pairs portable to any Windows fleet running Fortemedia OEM drivers or SentinelOne EDR. Single-source veto caps WEP. Splunk clean both indexes over 30d (22nd consecutive dormant sweep).

**Action.** Sweep mail/proxy/DNS for `timetrakr[.]cloud`, `sendit[.]sh`, `179.43.177.220` (AS51852 Private Layer CH), `178.128.233.36` (DigitalOcean CA). Hunt the two DLL pairs from non-OEM / non-SentinelOne paths. Review Node.js parents of PowerShell on non-dev endpoints (T1059.001/.007).

**Sources.** Symantec (A, prov) · BleepingComputer / Industrial Cyber / The Hacker News (B, relays). IOCs: `finding-2026-05-13-FLASH-1800-0001`.

Cross-cluster note: today's 14:30 FamousSparrow FLASH used `sentinelonepro[.]com` C2 — two clusters impersonating SentinelOne in ~12h. **Coincidental, not attribution-linked.** Watch through 2026-05-16 18:00 EDT.
