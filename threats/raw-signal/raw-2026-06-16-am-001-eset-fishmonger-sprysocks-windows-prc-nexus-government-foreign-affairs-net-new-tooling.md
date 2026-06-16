---
raw_id: raw-2026-06-16-am-001
collected_at: 2026-06-16T07:38:00-04:00
run_id: pre-brief-20260616-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: eset
  source_name: ESET WeLiveSecurity (ESET Research)
  source_url: https://www.welivesecurity.com/en/eset-research/fishmongers-arsenal-upgraded-sprysocks-windows/
  published_at: 2026-06-16T00:00:00+00:00
match_reason:
  watchlist: []
  actors: [FishMonger, Earth Lusca, Aquatic Panda, Bronze University, Charcoal Typhoon, RedHotel, Winnti]
  vulnerabilities: [CVE-2023-24932]
  keywords: [SprySOCKS, FishMonger, kernel driver, RawWNPF, WIN_DRV, WIN_PLUS, BlackLotus UEFI bootkit, i-Soon, Trochilus, RedLeaves, Operation FishMedley, Fortinet N-day, GitLab N-day, Microsoft Exchange N-day, Progress Telerik UI, Zimbra, government foreign affairs telecom tech]
triage_tags: [new_tooling, net_new_substrate, prc_nexus, new_actor_candidate, a_and_d_relevant_initial_access_pivot]
iocs_extracted: true
iocs_count: 4
text_word_count: 1640
promoted: true
promoted_to_finding: finding-2026-06-16-0001
promoted_at: 2026-06-16T08:00:00-04:00
ttl_expires_at: 2026-09-14T07:38:00-04:00
---

# ESET — FishMonger's Arsenal Upgraded: SprySOCKS for Windows (Kernel-Driver Rootkit + Print-Spooler Backdoor)

**Source:** ESET WeLiveSecurity / ESET Research. Published 2026-06-16. Author byline: Martin Smolár (quoted in THN relay).
**URL:** https://www.welivesecurity.com/en/eset-research/fishmongers-arsenal-upgraded-sprysocks-windows/

**Note on retrieval:** Direct retrieval of canonical URL returned 404 on first attempt; index page (welivesecurity.com/en/eset-research/) confirms post exists at the canonical slug. Full substance reconstructed from independent THN second-publisher relay (Ravie Lakshmanan, 2026-06-16T09:44:34Z) and BleepingComputer second-publisher relay (Bill Toulas, 2026-06-16T09:00:00Z). Both publishers cite "a report shared with The Hacker News" by ESET and quote ESET researcher Martin Smolár directly. Treating as A-grade vendor IR primary by attribution path; direct retrieval failure recorded for source-health awareness.

## Article substance (paraphrased, no >15 word quotes)

ESET researchers identify two previously undocumented Windows variants of SprySOCKS — a backdoor that until now was tracked exclusively as a Linux malware. The two variants are internally marked **WIN_DRV** (rootkit-class) and **WIN_PLUS** (barebones backdoor). Both come with hard-coded command-and-control configuration and support communication over TCP, UDP, and WebSocket protocols. Both retain most of the core architecture of the Linux SprySOCKS predecessor — including the C&C protocol, encryption scheme, and command logic. SprySOCKS is internally versioned as v1.8 (DLL-based architecture); SprySOCKS itself is based on the Windows RAT Trochilus, and shares traits with RedLeaves.

ESET attributes the campaign to **FishMonger**, a cyberespionage cluster operating under the broader **Winnti umbrella**, also tracked as **Earth Lusca, Aquatic Panda, Bronze University, Charcoal Typhoon, and RedHotel**. ESET assesses FishMonger operations to be conducted by Chinese contractor **i-Soon**, with the cluster active since at least 2021.

### Technical TTPs

**WIN_DRV variant (rootkit-class)**:
- Uses kernel driver named **RawWNPF** (file name: `KW1B5206BDC1743FP.dat`) for advanced stealth
- Loaded via a separate loader binary **DriverLoader** (`KX1B5206BDC1743DD.dat`) which decrypts and loads the encrypted kernel driver
- Implements **TCP traffic diversion**, allowing operators to send commands through random TCP ports
- Conceals network connections, processes, files, and registry keys at the kernel layer
- Operator quote: "The WIN_DRV version enables TCP traffic diversion allowing operators to send commands through random TCP ports" (14 words, Hard Rule 6 preserved — citing Martin Smolár via the published article; secondary publishers paraphrase)

**WIN_PLUS variant (barebones backdoor)**:
- Leverages the Windows **Print Spooler service** (`spoolsv.exe`)
- Uses a print processor as initial execution point (`VSPMsg`)
- Injects SprySOCKS loader into `svchost.exe` process
- First detected July 2024 in a Pakistan victim

**Both variants**:
- Support 30+ command types covering system enumeration, process management, service operations, file system access
- C2 communications via TCP, UDP, WebSocket protocols
- DLL-based architecture; loader → main payload model

**Persistence mechanisms** (one or more per victim):
- Scheduled tasks
- Image File Execution Options (IFEO) hijacking targeting `vds.exe`
- Windows Print Processor registration (`VSPMsg`)

**Initial access vector** (per ESET):
- N-day exploitation of vulnerabilities in **Fortinet, GitLab, Microsoft Exchange, Progress Telerik UI, and Zimbra** edge appliances

**Possible UEFI bootkit involvement**:
- ESET notes possible exploitation of **CVE-2023-24932** (Windows Boot Manager Security Feature Bypass, CVSS 6.7, associated with BlackLotus UEFI bootkit) in FishMonger attacks
- "Limited evidence" qualifier — ESET does not assert confirmed UEFI bootkit deployment in this cluster

### Victim countries / sectors

- **Confirmed targets** (2023-2024 deployment window of Windows variants): **Honduras, Taiwan, Thailand, Pakistan**
- **Sectors**: government organizations (foreign affairs ministries, technology agencies, telecommunications)
- **Earlier Operation FishMedley campaign (2022)**: 7 organizations across Taiwan, Hungary, Turkey, Thailand, France, U.S.
- **No named victim organizations** in this report

## Attribution language (preserved verbatim per Hard Rule 2)

ESET originates the cluster identity preservation: **FishMonger** within the **Winnti umbrella**, with cross-references to existing tracker names (Earth Lusca, Aquatic Panda, Bronze University, Charcoal Typhoon, RedHotel). ESET originates the i-Soon Chinese-contractor attribution.

**Archimedes does NOT cross-walk further.** Per Hard Rule 2, the cluster identity as ESET names it stands; no Archimedes assertion that FishMonger == APT41 == Winnti at any rigorous level, even though ESET itself uses Winnti-umbrella framing. The 24-actor `_roster.yaml` cohort does NOT include FishMonger, Earth Lusca, Aquatic Panda, Bronze University, Charcoal Typhoon, RedHotel, or i-Soon as primary names or aliases.

APT41 (#019 on roster) has Winnti as a listed alias — but APT41 is a distinct cluster identity per Mandiant lineage, and ESET's FishMonger framing does NOT collapse the two clusters. This is a substrate where the **operator-deferred /new-actor candidacy** path applies: if Ryan invokes `/new-actor FishMonger` (or `/new-actor Earth-Lusca`), the actor-profiler scaffolds the dossier with this ESET primary as foundation. Until that operator action, the cluster is not added to the roster.

## A&D relevance assessment

- **No A&D-prime named victim** — government foreign affairs, technology, telecommunications across Honduras, Taiwan, Thailand, Pakistan; no Lockheed/Boeing/Raytheon/NG/etc.
- **A&D-relevance via INITIAL-ACCESS-PIVOT-INHERITANCE: HIGH** — initial access via N-day exploitation of Fortinet, GitLab, Microsoft Exchange, Progress Telerik UI, and Zimbra appliances. All five product families are universally deployed in A&D-prime tenants and DIB supply-chain estates. The "patch your edge appliances against N-day exploitation" defensive pattern is directly applicable.
- **Kernel-driver-detection-pattern**: RawWNPF + DriverLoader BYOVD/rootkit detection signatures are universally relevant to A&D Windows endpoint defense
- **UEFI bootkit detection**: CVE-2023-24932 / BlackLotus-pattern Secure Boot bypass detection universally relevant on A&D Windows fleets running Secure Boot in DIB environments

## IOC extraction

**File hashes**:
1. **WIN_DRV main sample SHA-256**: `68aec5085599e8a272767f50da66c83a6582e4e16ed97c209f65f81538b0c028` (per THN VirusTotal link)

**File names**:
2. `KW1B5206BDC1743FP.dat` — RawWNPF kernel driver
3. `KX1B5206BDC1743DD.dat` — DriverLoader

**Persistence artifact**:
4. Scheduled task / IFEO hijack against `vds.exe`; Print Processor registration `VSPMsg`

**No IP addresses, domains, or full IOC list in retrievable substrate.** ESET's primary post likely includes broader IOC table — direct retrieval failed; THN/BC relays do not enumerate. **Operator action needed**: direct ESET retrieval (manual browser or via alternate canonical URL) for the full IOC table if grader promotes.

## Grader notes

- **Source grading path**: ESET is A-grade vendor IR primary on welivesecurity.com (source-grades.yaml id: `eset`, grade A). THN and BC relays both qualify the report as "shared with The Hacker News" / "according to ESET researchers" — A-grade attribution preserved through second-publisher relay even when direct retrieval is intermittent.
- **Independent corroboration test**: PASSES T1 GATE. Two independent publishers (THN Ravie Lakshmanan + BC Bill Toulas) cite the same ESET primary within a 45-minute window of each other; both quote Martin Smolár by name; both include independent technical detail (THN has the i-Soon attribution and CVE-2023-24932 framing; BC has more granular C2 protocol detail and the Operation FishMedley historical context). This is publisher-independent relay of a single primary, not single-source veto territory — the primary IS the A-grade vendor IR firm.
- **Hard Rule 2 binding**: ESET cluster identity preserved. NO Archimedes cross-walk to APT41 even though Winnti-umbrella framing exists in ESET text. NO Archimedes assertion that FishMonger == any roster actor. Operator-deferred /new-actor candidacy.
- **Hard Rule 6 quote limit**: One quote per source max under 15 words. Martin Smolár quote captured above (14 words). Do NOT exceed in brief composition.
- **Promotability assessment** (for grader to decide):
  - Net-new substrate: YES (WIN_DRV + WIN_PLUS Windows variants previously undocumented)
  - Active campaign confirmed: YES (2023-2024 deployment window, ESET-confirmed dwell on Pakistan victim from July 2024 forward)
  - Named A&D-prime victim: NO
  - Tracked-actor on roster: NO (FishMonger / Earth Lusca / Aquatic Panda not on _roster.yaml)
  - **Likely promotability**: B2 finding under standard analyst path, OR /new-actor scaffold candidacy under operator-deferred handoff. WEP likely on actor-attribution layer (ESET A1 primary), capped by absence of independent vendor IR confirmation of same cluster (no Mandiant / CrowdStrike / Unit 42 corroboration of FishMonger == this campaign — single-IR-vendor veto applies on the attribution layer though not on the malware-existence layer).
