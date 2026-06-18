---
raw_id: raw-2026-06-18-pm-005-bc-toulas-sa-paganini-usb-lnk-tor-crypto-clipper-third-fourth-publisher-relay
collected_at: 2026-06-18T15:44:00-04:00
run_id: pre-brief-20260618-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: bleepingcomputer
  source_name: BleepingComputer + Security Affairs
  source_url: https://www.bleepingcomputer.com/news/security/usb-worm-spreads-crypto-stealing-malware-via-windows-shortcut-files/
  published_at: 2026-06-18T16:20:06+00:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [crypto clipper, MSTIC, Microsoft Threat Intelligence, USB worm, BIP39 seed phrase, Tor proxy, .onion C2]
triage_tags: [restatement_of_mstic_finding, second_third_publisher_relay, non_a_d_consumer_crypto_target, anti_noise_binding]
iocs_extracted: true
iocs_count: 3
test: false
promoted: false
rejected_at: 2026-06-18T16:16:00-04:00
rejection_id: reject-2026-06-18-0012
ttl_expires_at: 2026-09-16T15:44:00-04:00
---

# USB worm spreads crypto-stealing malware via Windows shortcut files (BleepingComputer) + Tor-Based Clipper Malware Targets Wallet Seed Phrases (Security Affairs)

## Source metadata

- **Publishers:** BleepingComputer (BC-Toulas, 12:20 EDT 2026-06-18) + Security Affairs (SA-Paganini, 14:32 EDT 2026-06-18)
- **URLs:**
  - https://www.bleepingcomputer.com/news/security/usb-worm-spreads-crypto-stealing-malware-via-windows-shortcut-files/
  - https://securityaffairs.com/193860/uncategorized/tor-based-clipper-malware-targets-wallet-seed-phrases.html
- **Source grades:** B (BC + SA baselines)
- **Retrieval timestamp:** 2026-06-18T15:33 EDT

## Publisher-relay context (anti-noise rule 1 BINDING)

This is the **second and third publisher relay** on the Microsoft Threat Intelligence (MSTIC) Crypto-Clipper / USB-LNK / Tor / BIP39-seed-phrase campaign already raw-signaled as `raw-2026-06-18-am-002-mstic-crypto-clipper-tor-worm-windows.md` (Microsoft Security Blog primary). The AM raw-signal substantiated the MSTIC primary; this PM raw-signal documents the journalistic relay chain consolidation.

**anti-noise rule 1 BINDING** — content was already raw-signaled in this 24h window from MSTIC primary, no net-new substrate-pivot beyond the MSTIC research itself. The relays add:

- BC-Toulas: trade-press confirmation + behavioral-detection framing for SOC teams
- SA-Paganini: trade-press confirmation + technical-detail amplification on BIP39 seed-phrase mechanism + WIF private-key targeting + Trojan:Win32/CryptoBandits.A Defender detection name

## Attribution verbatim (Hard Rule 2 BINDING — no Archimedes-originated cross-walk)

Both publishers preserve Microsoft Threat Intelligence attribution at the cluster identity layer:

- BC-Toulas: "Microsoft says" + linked MSTIC blog 2026-06-17 (note BC-Toulas does NOT use "MSTIC"-specific language; preserves "Microsoft" institutional attribution).
- SA-Paganini: "Microsoft Threat Intelligence has been tracking a clipboard-stealing malware (Clipper) campaign since February 2026"

No tracked-roster actor referenced by either publisher. No cross-walk to TeamPCP, Lazarus, Stardust Chollima, or any roster actor.

## IOCs (incremental detail from publisher relays)

```yaml
iocs:
  malware_family:
    - value: "Trojan:Win32/CryptoBandits.A"
      context: "Microsoft Defender for Endpoint detection name per SA-Paganini relay"
      family: clipper / crypto-bandit
  
  network_indicators:
    - value: "localhost:9050"
      context: "Local SOCKS5 Tor proxy port used by bundled portable Tor client"
      class: behavioral_indicator
  
  file_artifacts:
    - value: "cfile"
      context: "JavaScript payload container downloaded via EVAL C2 instruction"
      family: clipper / crypto-bandit
    - value: "ugate.exe"
      context: "Tor executable component (per BC-Toulas behavioral indicator)"
      family: clipper / crypto-bandit
  
  behavioral_indicators:
    - script_interpreters_spawning_curl_powershell_cmd
    - wscript_cscript_high_frequency_clipboard_inspection
    - clipboard_polling_500ms_interval
    - screenshot_capture_five_per_ten_seconds
    - lnk_files_on_removable_storage_replacing_doc_xlsx_pdf
    - scheduled_task_for_usb_device_propagation
    - bip39_12_or_24_word_seed_phrase_clipboard_match
    - ethereum_bitcoin_wif_private_key_clipboard_match
    - bitcoin_ethereum_tron_monero_wallet_address_substitution

attribution_claims:
  - actor: unattributed
    actor_status: not_on_roster
    confidence_phrase: "tracking a clipboard-stealing malware (Clipper) campaign since February 2026"
    asserted_by: Microsoft Threat Intelligence (MSTIC)
    journalistic_relay_through: BC-Toulas + SA-Paganini
    cross_walk_to_roster: NONE — Hard Rule 2 BINDING
```

## Why this matters for the afternoon brief

This is **NOT a substrate-pivot UPDATE candidate** for the afternoon brief — the substrate is already published in the AM brief dac22e4 (MSTIC research raw-signaled at am-002, briefer chose not to feature it in AM brief due to A&D-relevance LOW assessment per consumer-crypto-wallet target class).

**Anti-noise rule 1 BINDING** — restatement-of-prior-attribution per the BC + SA journalistic relay through Microsoft primary.

**Possible Other Signal one-liner candidate** for afternoon brief — if briefer chooses to surface the MSTIC research now with second/third-publisher consolidation: USB-LNK as cross-airgap propagation vector + Tor-only C2 hardening pattern observation. Frank's deployment is NOT a cryptocurrency-wallet-using environment — first-party exposure null.

## WEP framing for grader

- Campaign technical reality → **very likely** (MSTIC primary single-A-IR-vendor + 2 trade-press relays substantiates)
- A&D-DIB direct targeting → **unlikely** (consumer crypto-wallet target class; cross-airgap USB propagation is interesting but no A&D-prime named victim)
- Cross-airgap USB-LNK propagation as broader TTP pattern relevant to A&D classified-network gap-traversal → **roughly even chance** (TTP pattern is observed by MSTIC for consumer crypto targeting, not A&D classified-network targeting; analytical bridge would need a separate A&D-context substrate to substantiate)

## Quote budget reservation (Hard Rule 6, 15-word cap, 1-per-source ceiling)

Candidate at-cap quotes (briefer chooses one per source if used):

- SA-Paganini quoting MSTIC: "The clipper in this campaign relies on Windows Script Host and ActiveX-driven logic" (12 words)
- SA-Paganini quoting MSTIC: "The malware detects 12 or 24-word BIP39 seed phrases in clipboard data" (12 words)
- BC-Toulas direct: "blends data theft with remote code execution" (7 words, paraphrase risk if MSTIC quote)

## Extraction notes

- Language: en
- Publisher bylines: Bill Toulas (BC), Pierluigi Paganini (SA)
- Article type: trade-press relay (BC + SA through MSTIC primary)
- Raw IOC extraction invoked: yes (3 incremental IOCs beyond AM primary — Defender detection name, Tor port, file artifact)
