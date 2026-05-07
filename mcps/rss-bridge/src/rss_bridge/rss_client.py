"""RSS/Atom feed client.

Synchronous httpx for the network round-trip; feedparser for parsing.
ETag / Last-Modified caching is operator-managed: the caller passes
prior values in, this client sets the conditional headers, and the
fresh ETag / Last-Modified come back in the response so the caller
can store them.

No rate limiting beyond per-request timeout. Public RSS feeds are
expected to be unmetered; if a host returns 429 we surface it as
RssBridgeRateLimitError and the caller decides how to back off
(typically `source-health.yaml` failure_count + 24h stale window).
"""

from __future__ import annotations

import re
from datetime import datetime, timezone
from time import struct_time
from typing import Any
from calendar import timegm

import feedparser
import httpx

from rss_bridge.config import RssBridgeConfig
from rss_bridge.exceptions import (
    RssBridgeConnectionError,
    RssBridgeParseError,
    RssBridgeRateLimitError,
    RssBridgeRequestError,
)
from rss_bridge.models import (
    FeedItem,
    FetchFeedOutput,
    ValidateFeedOutput,
)


SUMMARY_MAX_CHARS = 1000
CONTENT_MAX_CHARS = 5000


# ---------- helpers ----------


def _struct_time_to_iso(st: struct_time | None) -> str | None:
    """feedparser parses dates into time.struct_time (UTC). Convert to ISO 8601."""
    if not st:
        return None
    try:
        ts = timegm(st)
        return datetime.fromtimestamp(ts, tz=timezone.utc).isoformat().replace("+00:00", "+00:00")
    except (ValueError, OverflowError):
        return None


_HTML_TAG_RE = re.compile(r"<[^>]+>")


def _strip_html(value: str | None) -> str | None:
    """Remove HTML tags from feed text. Cheap regex; not a full parser."""
    if not value:
        return None
    return _HTML_TAG_RE.sub("", value).strip() or None


def _truncate(value: str | None, limit: int) -> str | None:
    if not value:
        return None
    if len(value) <= limit:
        return value
    return value[:limit].rstrip() + "..."


def _entry_to_item(entry: Any) -> FeedItem:
    """Map a feedparser entry into our trimmed FeedItem."""
    title = _strip_html(getattr(entry, "title", None))
    link = getattr(entry, "link", None)
    summary = _truncate(_strip_html(getattr(entry, "summary", None)), SUMMARY_MAX_CHARS)

    # `content` is a list of dicts in feedparser. Take the first text/html
    # or text/plain entry and truncate.
    content_value: str | None = None
    contents = getattr(entry, "content", None)
    if contents:
        for c in contents:
            cv = c.get("value") if isinstance(c, dict) else None
            if cv:
                content_value = _truncate(_strip_html(cv), CONTENT_MAX_CHARS)
                break

    author = (
        getattr(entry, "author", None)
        or (getattr(entry, "author_detail", {}) or {}).get("name")
    )

    guid = getattr(entry, "id", None) or getattr(entry, "guid", None) or link

    categories: list[str] = []
    tags = getattr(entry, "tags", None)
    if tags:
        for t in tags:
            if isinstance(t, dict):
                term = t.get("term")
                if term:
                    categories.append(str(term))

    return FeedItem(
        title=title,
        link=link,
        published=_struct_time_to_iso(getattr(entry, "published_parsed", None)),
        updated=_struct_time_to_iso(getattr(entry, "updated_parsed", None)),
        summary=summary,
        content=content_value,
        author=author,
        guid=guid,
        categories=categories,
    )


def _filter_since(items: list[FeedItem], since_iso: str | None) -> list[FeedItem]:
    """Drop items whose published is strictly older than `since`."""
    if not since_iso:
        return items
    try:
        cutoff = datetime.fromisoformat(since_iso.replace("Z", "+00:00"))
        if cutoff.tzinfo is None:
            cutoff = cutoff.replace(tzinfo=timezone.utc)
    except ValueError:
        # Bad `since` value: pass everything through rather than silently drop all.
        return items

    kept: list[FeedItem] = []
    for item in items:
        if not item.published:
            # No timestamp → keep (caller will see undated items)
            kept.append(item)
            continue
        try:
            pub = datetime.fromisoformat(item.published.replace("Z", "+00:00"))
            if pub.tzinfo is None:
                pub = pub.replace(tzinfo=timezone.utc)
        except ValueError:
            kept.append(item)
            continue
        if pub >= cutoff:
            kept.append(item)
    return kept


# ---------- client ----------


class RssBridgeClient:
    """Synchronous RSS/Atom feed client.

    Fetches feeds via httpx (so we get sane TLS, redirects, timeouts) and
    parses with feedparser. Closes its httpx.Client on .close() / __exit__.
    """

    def __init__(self, config: RssBridgeConfig) -> None:
        self._config = config
        self._client = httpx.Client(
            timeout=config.rss_bridge_timeout_seconds,
            follow_redirects=True,
            headers={"User-Agent": config.rss_bridge_user_agent},
        )

    def __enter__(self) -> RssBridgeClient:
        return self

    def __exit__(self, *exc_info: object) -> None:
        self.close()

    def close(self) -> None:
        self._client.close()

    # ---------- transport ----------

    def _get(
        self,
        url: str,
        *,
        etag: str | None = None,
        last_modified: str | None = None,
    ) -> httpx.Response:
        headers: dict[str, str] = {}
        if etag:
            headers["If-None-Match"] = etag
        if last_modified:
            headers["If-Modified-Since"] = last_modified

        try:
            resp = self._client.get(url, headers=headers)
        except httpx.ConnectError as e:
            raise RssBridgeConnectionError(f"Could not connect to {url}: {e}") from e
        except httpx.TimeoutException as e:
            raise RssBridgeConnectionError(f"Feed request timed out for {url}: {e}") from e
        except httpx.RequestError as e:
            raise RssBridgeConnectionError(f"Feed request failed for {url}: {e}") from e

        if resp.status_code == 429:
            retry_after = resp.headers.get("Retry-After")
            raise RssBridgeRateLimitError(
                f"Feed host rate-limited: {url} (Retry-After: {retry_after})"
            )
        if resp.status_code >= 500:
            raise RssBridgeConnectionError(
                f"Feed host server error {resp.status_code}: {url}"
            )
        if 400 <= resp.status_code < 500 and resp.status_code != 304:
            raise RssBridgeRequestError(
                f"Feed host rejected request ({resp.status_code}): {url}"
            )
        return resp

    # ---------- fetch_feed ----------

    def fetch_feed(
        self,
        url: str,
        *,
        since: str | None = None,
        etag: str | None = None,
        last_modified: str | None = None,
        max_items: int | None = None,
    ) -> FetchFeedOutput:
        cap = max_items or self._config.rss_bridge_max_items_default
        fetched_at = datetime.now(timezone.utc).isoformat()

        resp = self._get(url, etag=etag, last_modified=last_modified)

        # 304 Not Modified — caller should reuse cached items
        if resp.status_code == 304:
            return FetchFeedOutput(
                found=True,
                not_modified=True,
                feed_url=url,
                fetched_at=fetched_at,
                status_code=304,
                etag=resp.headers.get("ETag", etag),
                last_modified=resp.headers.get("Last-Modified", last_modified),
                items=[],
                items_total_in_feed=0,
                items_after_since_filter=0,
            )

        body = resp.content
        if not body:
            raise RssBridgeParseError(f"Empty response body from {url}")

        parsed = feedparser.parse(body)
        # feedparser sets bozo=1 for any parse imperfection. Some real-world
        # feeds (e.g., advisories with stray ampersands) bozo but still produce
        # usable entries — recover rather than reject.
        warning: str | None = None
        if getattr(parsed, "bozo", 0) and not parsed.entries:
            exc = getattr(parsed, "bozo_exception", None)
            raise RssBridgeParseError(
                f"Could not parse {url} as RSS/Atom: {exc}"
            )
        if getattr(parsed, "bozo", 0):
            exc = getattr(parsed, "bozo_exception", None)
            warning = f"Recoverable parse issue: {exc}"

        feed_meta = parsed.feed or {}
        all_items = [_entry_to_item(e) for e in (parsed.entries or [])]
        filtered = _filter_since(all_items, since)
        capped = filtered[:cap]

        return FetchFeedOutput(
            found=True,
            not_modified=False,
            feed_url=url,
            feed_title=getattr(feed_meta, "title", None),
            feed_description=_truncate(_strip_html(getattr(feed_meta, "subtitle", None) or getattr(feed_meta, "description", None)), 500),
            feed_language=getattr(feed_meta, "language", None),
            fetched_at=fetched_at,
            status_code=resp.status_code,
            etag=resp.headers.get("ETag"),
            last_modified=resp.headers.get("Last-Modified"),
            items=capped,
            items_total_in_feed=len(all_items),
            items_after_since_filter=len(filtered),
            parse_warning=warning,
        )

    # ---------- validate_feed ----------

    def validate_feed(self, url: str) -> ValidateFeedOutput:
        try:
            resp = self._get(url)
        except (RssBridgeConnectionError, RssBridgeRequestError, RssBridgeRateLimitError) as e:
            return ValidateFeedOutput(
                valid=False,
                feed_url=url,
                status_code=0,
                error=str(e),
            )

        body = resp.content
        if not body:
            return ValidateFeedOutput(
                valid=False,
                feed_url=url,
                status_code=resp.status_code,
                error="empty response body",
            )

        parsed = feedparser.parse(body)
        feed_type: str | None = None
        version = getattr(parsed, "version", None) or ""
        if version.startswith("rss"):
            feed_type = "rss"
        elif version.startswith("atom"):
            feed_type = "atom"
        elif parsed.entries or parsed.feed:
            feed_type = "unknown"

        # Valid = has metadata or entries, not just bozo. A feedparser bozo
        # with zero entries and no feed title is not a feed.
        has_meta = bool((parsed.feed or {}).get("title"))
        has_entries = bool(parsed.entries)
        if (has_meta or has_entries) and feed_type:
            return ValidateFeedOutput(
                valid=True,
                feed_url=url,
                status_code=resp.status_code,
                feed_title=(parsed.feed or {}).get("title"),
                feed_type=feed_type,
                items_total=len(parsed.entries or []),
            )

        bozo_exc = getattr(parsed, "bozo_exception", None)
        return ValidateFeedOutput(
            valid=False,
            feed_url=url,
            status_code=resp.status_code,
            error=f"not a valid feed: {bozo_exc}" if bozo_exc else "not a valid feed",
        )
