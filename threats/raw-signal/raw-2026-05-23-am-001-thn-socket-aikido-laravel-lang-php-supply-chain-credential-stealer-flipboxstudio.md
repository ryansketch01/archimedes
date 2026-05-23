---
raw_id: raw-2026-05-23-am-001-thn-socket-aikido-laravel-lang-php-supply-chain-credential-stealer-flipboxstudio
collected_at: 2026-05-23T07:35:00-04:00
run_id: pre-brief-20260523-073000
collection_mode: pre_brief_collection
test: false
source:
  source_yaml_id: thehackernews
  source_name: "The Hacker News (Ravie Lakshmanan byline)"
  source_url: https://thehackernews.com/2026/05/laravel-lang-php-packages-compromised.html
  published_at: 2026-05-23T09:51:13+00:00
corroborating_primaries:
  - source_yaml_id: socket
    source_name: "Socket (npm/supply-chain security vendor, provisional B)"
    notes: "Socket is named originating-research primary in THN coverage; Socket published timing-and-pattern analysis quoted directly. Socket blog primary URL not directly retrieved this sweep."
  - source_yaml_id: aikido-security
    source_name: "Aikido Security (Ilyas Makari byline; provisional C)"
    notes: "Aikido Security named as co-researcher with named-byline analyst Ilyas Makari. Aikido blog primary URL not directly retrieved this sweep."
match_reason:
  watchlist: []                            # Laravel-Lang is generic PHP localization package; not directly A&D-watchlisted, but Laravel-PHP ecosystem is widely deployed in web stacks across sub-tier suppliers
  actors: []                               # NO actor attribution — Socket + Aikido decline attribution per article framing
  vulnerabilities: []                      # NO CVE assigned to this supply-chain compromise
  keywords:
    - laravel_lang_php_supply_chain_compromise
    - 700_versions_four_packages_may_22_23_2026
    - credential_stealer_framework_aes_256_encrypted
    - cloud_metadata_endpoint_harvesting_aws_gcp_azure_kubernetes_digitalocean
    - cryptocurrency_wallet_seed_recovery_electrum_exodus_metamask_ledger_trezor
    - password_manager_targeting_1password_bitwarden_lastpass_keepass_dashlane_nordpass
    - browser_credential_theft_chrome_app_bound_encryption_bypass
    - vpn_config_theft_openvpn_wireguard_nordvpn_expressvpn
    - flipboxstudio_info_c2_vt_malicious_3_engines_kaspersky_forcepoint_adminuslabs
    - composer_packagist_php_ecosystem
triage_tags:
  - non_flash
  - supply_chain_attack
  - php_ecosystem
  - credential_stealer_framework
  - cloud_metadata_targeting
  - cryptocurrency_targeting
  - password_manager_targeting
  - vpn_config_targeting
  - ssh_git_docker_credential_targeting
  - no_actor_attribution_per_socket_and_aikido
  - vt_malicious_c2_confirmed
  - splunk_first_party_zero_hits_30d
  - cross_ecosystem_supply_chain_post_npm_pypi_mini_shai_hulud
splunk_first_party:
  query_run_30d_archimedes_and_defenseclaw_local: true
  query: 'search (index=archimedes OR index=defenseclaw_local) earliest=-30d@d (dest_domain="flipboxstudio.info" OR query="flipboxstudio.info" OR url="*flipboxstudio.info*")'
  results: 0
  notes: "Zero first-party hits across both indexes over -30d window. Indexes remain dormant pattern observed across 60+ consecutive sweeps; absence of hits is not evidence of absence given dormant collection."
critical_override_evaluation:
  cvss_10_0: false
  cvss_value: null                          # no CVE assigned
  active_exploitation: true                 # vendor-confirmed live publication of 700+ malicious package versions on May 22-23
  tracked_actor_involved: false
  ad_watchlist_targeted: false
  result: NOT_CRITICAL_OVERRIDE
text_word_count: 387
iocs_extracted: true
iocs_count: 6
promoted: true
promoted_to_finding: finding-2026-05-23-0001
promoted_at: 2026-05-23T08:14:00-04:00
ttl_expires_at: 2026-08-21T07:35:00-04:00
---

# Laravel-Lang PHP Packages Compromised to Deliver Cross-Platform Credential Stealer

The Hacker News, Ravie Lakshmanan byline, 2026-05-23T09:51:13Z.

## Article Substantive Text (Preserved for Grader Context)

The Hacker News reports cybersecurity researchers have flagged a fresh software supply-chain attack campaign that targeted multiple PHP packages belonging to the Laravel-Lang organization to deliver what is characterized as a "comprehensive credential-stealing framework."

The four affected packages are:

- `laravel-lang/lang`
- `laravel-lang/http-statuses`
- `laravel-lang/attributes`
- `laravel-lang/actions`

Socket (named originating-research primary) characterized the campaign timing: "The timing and pattern of the newly published tags" indicate coordinated mass-publication of 700+ malicious tag versions across the four repositories on May 22-23, 2026, "with many versions appearing only seconds apart."

The malicious payload is delivered via a modified `src/helpers.php` file inside the compromised packages. The credential-stealing framework's documented capabilities (per Socket and Aikido Security via The Hacker News):

**Cloud Metadata & Workload Identity**
- Cloud-metadata endpoint harvesting (AWS IAM roles, instance identity documents)
- Google Cloud, Azure, Kubernetes, and DigitalOcean credential exfiltration

**Cryptocurrency Wallets**
- Wallet seed recovery from Electrum, Exodus, Atomic, Ledger, Trezor, Wasabi, Sparrow
- Browser-extension wallets: MetaMask, Phantom, Trust Wallet

**Browser Credentials**
- Chrome app-bound encryption bypass via Base64-encoded executable

**Password Managers**
- Targets 1Password, Bitwarden, LastPass, KeePass, Dashlane, NordPass

**Developer / Infrastructure Credentials**
- SSH key, Git credential, Docker credential harvesting

**VPN Configurations**
- OpenVPN, WireGuard, NordVPN, ExpressVPN, CyberGhost, Mullvad

**Exfiltration Mechanism**
- AES-256 encryption of collected data before exfiltration
- C2 domain: `flipboxstudio[.]info`

**Attribution Posture**
The article preserves Socket's and Aikido's no-attribution-on-actor stance — no TeamPCP / Shai-Hulud / Mini Shai-Hulud / nation-state attribution claimed despite operational adjacency to other 2026 supply-chain campaigns (npm Mini Shai-Hulud finding-2026-05-12-FLASH-0001, npm node-ipc finding-2026-05-14-0009, TanStack/OpenAI finding-2026-05-14-0008, GitHub-internal-repos finding-2026-05-20-FLASH-0001). Hard Rule 2 compliant.

Researcher byline: Ilyas Makari (Aikido Security).

---

## Extraction Notes

- Language: en
- Publisher byline: Ravie Lakshmanan (The Hacker News)
- Article type: news / supply-chain incident relay
- Raw IOC extraction invoked: yes
- A&D relevance: STRUCTURAL-INDIRECT — Laravel is a major PHP framework; many sub-tier suppliers and small-vendor websites in the A&D supply chain ecosystem run Laravel-based applications. Cloud-metadata credential harvesting (AWS IAM roles, GCP, Azure, Kubernetes, DigitalOcean) directly applies to any A&D sub-tier running cloud-hosted Laravel applications. NOT A&D-direct-victim-named.
- Cross-corpus pattern: Fifth distinct 2026 supply-chain campaign across npm + PyPI + PHP/Composer + GitHub-internal-repos ecosystems in 11 days (Mini Shai-Hulud 2026-05-12 npm+PyPI; node-ipc 2026-05-14 npm; TanStack 2026-05-14 GitHub Actions / OpenAI scope; GitHub-internal-repos 2026-05-20 VS Code marketplace pivot; Laravel-Lang 2026-05-22-23 PHP/Composer). Grader may evaluate whether the cross-ecosystem cluster is itself a brief-worthy pattern given Mini Shai-Hulud + node-ipc were previously raw-signaled as separate findings.

## IOCs (from ioc-extraction skill)

```yaml
iocs:
  - type: package_name
    value: "laravel-lang/lang"
    ecosystem: composer
    notes: "Affected package; 700+ malicious tag versions published May 22-23, 2026"
    confidence: high
    source: socket_via_thn
  - type: package_name
    value: "laravel-lang/http-statuses"
    ecosystem: composer
    confidence: high
    source: socket_via_thn
  - type: package_name
    value: "laravel-lang/attributes"
    ecosystem: composer
    confidence: high
    source: socket_via_thn
  - type: package_name
    value: "laravel-lang/actions"
    ecosystem: composer
    confidence: high
    source: socket_via_thn
  - type: file_path
    value: "src/helpers.php"
    notes: "Payload-delivery file inside compromised packages"
    confidence: high
    source: socket_via_thn
  - type: domain
    value: "flipboxstudio[.]info"
    role: c2
    confidence: high
    source: aikido_security_via_thn
    enrichment:
      virustotal:
        last_analysis_date: 2026-05-23T11:12:24Z
        malicious: 3
        suspicious: 1
        harmless: 52
        undetected: 35
        malicious_engines: [ADMINUSLabs, Forcepoint ThreatSeeker, Kaspersky]
        categories:
          forcepoint_threatseeker: "malicious web sites"
        vt_link: https://www.virustotal.com/gui/domain/flipboxstudio.info
attribution_claims: []
splunk_corroboration:
  archimedes_30d_hits: 0
  defenseclaw_local_30d_hits: 0
  notes: "Indexes dormant; absence not informative."
```
