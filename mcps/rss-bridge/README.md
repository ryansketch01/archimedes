# rss-bridge MCP

Direct RSS/Atom feed fetcher for Archimedes. Two read-only tools:

- `fetch_feed(url, since?, etag?, last_modified?, max_items?)` — fetch and
  parse a feed; returns metadata + trimmed items. Supports conditional
  GET caching via ETag / Last-Modified.
- `validate_feed(url)` — parseability check only; returns valid/invalid
  without ingesting items. Used by source-health probes.

## Why "rss-bridge"?

The collector subagent (`.claude/agents/collector.md`) references
`mcp__rss-bridge__fetch` as its canonical RSS path. The name predates this
implementation. **This MCP is NOT a wrapper around the
[RSS-Bridge](https://github.com/RSS-Bridge/rss-bridge) software project** —
it's a direct fetcher. For X/Twitter (which RSS-Bridge software handles
natively), point this MCP at any public bridge URL and it'll fetch
whatever RSS the bridge produces.

## Tools

### `fetch_feed`

```python
fetch_feed(
    url="https://krebsonsecurity.com/feed/",
    since="2026-05-06T00:00:00+00:00",       # optional time filter
    etag='"abc123"',                          # optional cache key
    last_modified="Wed, 07 May 2026 09:00:00 GMT",
    max_items=20,                             # optional cap
)
```

Returns:

```python
{
  "found": True,
  "not_modified": False,
  "feed_url": "...",
  "feed_title": "Krebs on Security",
  "feed_description": "In-depth security news...",
  "feed_language": "en-US",
  "fetched_at": "2026-05-07T14:30:00+00:00",
  "status_code": 200,
  "etag": "...",                              # pass back next time
  "last_modified": "...",
  "items": [
    {
      "title": "...",
      "link": "...",
      "published": "2026-05-07T08:00:00+00:00",
      "updated": None,
      "summary": "Truncated to 1000 chars; HTML stripped",
      "content": "Full content if feed includes it; truncated to 5000",
      "author": "Brian Krebs",
      "guid": "https://krebsonsecurity.com/?p=...",
      "categories": ["a-little-sunshine", "the-coming-storm"]
    },
    ...
  ],
  "items_total_in_feed": 25,
  "items_after_since_filter": 8,
  "parse_warning": None
}
```

If the host returns 304 Not Modified, `not_modified=true` and `items=[]`.
The caller should reuse cached items.

### `validate_feed`

Lightweight parseability check. Returns `valid=true` only if the host
returns 2xx AND the body parses as RSS or Atom AND the feed has metadata
or entries. Returns `valid=false` (with `error` string) on any other
outcome. **Never raises** for connection or parse errors — those are
reported via `valid=false`.

## Configuration

All env vars optional. The MCP works with zero configuration.

| Var | Default | Purpose |
|---|---|---|
| `RSS_BRIDGE_USER_AGENT` | `Archimedes-CTI-Collector/0.1 (+...)` | UA sent on every request. Some hosts (CISA) block default httpx UA. |
| `RSS_BRIDGE_TIMEOUT_SECONDS` | `30.0` | Per-request timeout. |
| `RSS_BRIDGE_MAX_ITEMS_DEFAULT` | `50` | Default cap when `max_items` not passed. |

No API key. RSS feeds are public.

## Behavior notes

- **HTML stripping:** title, summary, content all strip tags via a cheap
  regex. Not a full HTML parser; entity references like `&amp;` are NOT
  decoded. Consumers needing full text should follow the `link` and use
  WebFetch.
- **Time filter (`since`):** items without a `published` timestamp are
  kept. Items with unparseable timestamps are kept. This is defensive —
  better to surface than silently drop.
- **bozo recovery:** feedparser's `bozo=1` flag (set on any parse
  imperfection) is non-fatal. If the feed has at least one entry, we
  return them with `parse_warning` populated. If `bozo=1` AND zero
  entries, we raise `RssBridgeParseError`.
- **Redirects:** httpx `follow_redirects=True`. The reported `feed_url`
  is the URL you passed in, not the post-redirect URL.

## Run locally

```bash
# from repo root
uv sync --all-packages
uv run --directory mcps/rss-bridge rss-bridge   # runs on stdio
```

## Tests

```bash
# unit tests (fast, no network)
uv run --directory mcps/rss-bridge pytest tests/test_config.py tests/test_client.py -v

# live tests against real feeds (network required)
RSS_BRIDGE_LIVE_TEST=1 uv run --directory mcps/rss-bridge pytest tests/test_integration.py -v
```
