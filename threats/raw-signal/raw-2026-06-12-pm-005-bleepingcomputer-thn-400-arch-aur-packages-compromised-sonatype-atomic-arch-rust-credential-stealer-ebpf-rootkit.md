---
raw_id: raw-2026-06-12-pm-005
collected_at: 2026-06-12T15:55:00-04:00
run_id: pre-brief-20260612-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: bleepingcomputer
  source_name: BleepingComputer (+ The Hacker News relay; Sonatype primary)
  source_url: https://www.bleepingcomputer.com/news/security/over-400-arch-linux-packages-compromised-to-push-rootkit-infostealer/
  published_at: 2026-06-12T17:03:55+00:00
  source_grade: B (provisional)
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [Arch Linux, AUR, supply chain, Sonatype, Atomic Arch, Rust credential stealer, eBPF rootkit, PKGBUILD, developer environment]
triage_tags: [supply_chain_compromise, developer_tier_exposure, structural_ad, iocs_available, no_actor_attribution]
iocs_extracted: true
iocs_count: 5
text_word_count: 480
promoted: true
promoted_to_finding: finding-2026-06-12-0005
promoted_at: 2026-06-12T16:45:00-04:00
ttl_expires_at: 2026-09-10T15:55:00-04:00
---

# 400+ Arch User Repository (AUR) packages hijacked — Sonatype "Atomic Arch" campaign; Rust credential stealer + optional eBPF rootkit; developer-tier credential exposure

## What multiple publishers report (2026-06-12, multiple times)

Two converging publishers this sweep:
- BleepingComputer (Bill Toulas, 13:03 EDT): "Over 400 Arch Linux packages compromised to push rootkit, infostealer."
- The Hacker News (Ravie Lakshmanan, 15:24 EDT): "400+ Arch Linux AUR Packages Hijacked to Install Rust Credential Stealer."

Both source the underlying campaign to **Sonatype** research (campaign name: "Atomic Arch") with reverse-engineering work by an independent researcher tracked as "Whanos."

## Campaign mechanics

- **Compromise method:** new maintainer accounts adopted abandoned/orphaned AUR packages; the actor then modified `PKGBUILD` and `.install` scripts to execute npm and bun install commands during package build, retrieving the weaponized `atomic-lockfile` package. Spoofed git commit metadata used to disguise the maintainer change.
- **Initial count → final count:** initial wave compromised 20+ packages; expanded to **~408 packages** within days across two distinct waves.
- **Scope bounding:** **official Arch repositories were NOT affected** — AUR is the community package repository; the campaign targeted exactly the lower-trust adjacent ecosystem.
- **In-the-wild status:** YES — actively exploited; two waves identified.
- **Actor attribution:** **none.** Sonatype does NOT name a tracked threat actor or nation-state. No Microsoft Storm-/Typhoon-/Sandstorm-/Mantis taxon mentioned by any publisher. Hard Rule 2 binding.

## Malware payload — Rust credential stealer

The payload is a Rust binary explicitly built to harvest developer secrets. With root, it loads an **eBPF rootkit** that hides itself from standard tools.

### Credential categories targeted (8 categories per THN summary)

1. Browser cookies / tokens / local storage (Chromium-based browsers)
2. Electron app session data (Slack, Discord, Teams)
3. GitHub, npm, HashiCorp Vault tokens
4. OpenAI / ChatGPT credentials
5. SSH keys and known_hosts
6. Shell histories
7. Docker / Podman credentials
8. VPN profiles

## Hard Rule 7 — credential discipline

Per LEGAL-POLICY §Data Handling, no credential values are stored in this raw-signal file. The campaign IS a credential-stealer family; the categories enumerated above describe what the malware harvests on victim systems, not credentials that have reached Archimedes' corpus. Counts at the campaign level only.

## IOCs (extraction summary)

### Hashes
- Payload SHA-256: `6144d433f8a0316869877b5f834c801251bbb936e5f1577c5680878c7443c98b`

### Malicious package names
- `atomic-lockfile@1.4.2` (primary npm payload package)
- `js-digest` (second-wave npm payload package)

### C2 / exfiltration
- HTTP exfiltration to `temp.sh`
- Tor onion service accessed via local loopback proxy (specific .onion not enumerated in relay)

### eBPF rootkit telemetry (detection-engineering, not C2 IOCs)
- eBPF map names: `hidden_pids`, `hidden_names`, `hidden_inodes`

### Confidence: B (BleepingComputer + THN B-grade relay; Sonatype primary not directly retrieved this sweep)

## Hard Rule 2 — attribution discipline

No actor attribution. Sonatype names "Atomic Arch" as a campaign / cluster designation only. No nation-state, no tracked threat actor. Archimedes does NOT cross-walk this to existing roster actors.

## A&D-prime relevance

- **Direct:** none — no A&D-prime victim named or implied.
- **Structural:** **HIGH for developer environments.** The credential categories targeted (GitHub tokens, npm tokens, HashiCorp Vault, SSH keys, Docker creds, VPN profiles) are exactly the secrets that A&D-prime developer workstations and build environments carry. Any A&D-prime engineer running Arch Linux on a personal or development machine with AUR enabled is in scope.
- **Cluster-context:** continues the supply-chain-compromise-of-developer-tooling pattern from corpus: Mini Shai-Hulud npm + PyPI worm (finding-2026-05-12-FLASH-0001); Shai-Hulud Microsoft 72-repo compromise (raw-2026-06-10-am-002); node-ipc 90-credential stealer (finding-2026-05-14-0009); Anthropic TanStack (finding-2026-05-14-0008); GitHub 3,800-repo internal compromise (finding-2026-05-20-FLASH-0001).

## Action / brief framing

- Vulnerabilities or Other Signal section — preserve "no actor attribution" framing.
- Detection-engineering callouts: eBPF map names (`hidden_pids`, `hidden_names`, `hidden_inodes`); the payload SHA-256; the two npm payload package names.
- Recommend: audit AUR usage policy on all A&D-prime developer machines; rotate developer-tier credentials if AUR usage is suspected; check for the named eBPF maps on suspect systems.

## Watch items

- Sonatype primary blog direct retrieval at next collector pass.
- Whanos reverse-engineering write-up for any deeper IOCs.
- Second IR-firm corroboration (no Tier-1 vendor cross-corroboration this sweep).
- Any A&D-prime SOC reporting an AUR-package-related compromise.

## Extraction notes

- Language: en
- Article type: security trade press relay of Sonatype vendor research
- IOCs: Yes — 1 payload hash + 2 malicious package names + 1 C2 surface (temp.sh) + Tor onion mention; 3 eBPF detection-engineering map names.
- Direct retrieval: BleepingComputer + THN; Sonatype primary not directly retrieved this sweep.
