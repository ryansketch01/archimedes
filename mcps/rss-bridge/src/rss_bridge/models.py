"""Pydantic models for RSS Bridge MCP tool inputs and outputs.

Output shape philosophy: trim feed entries to what a CTI collector
actually uses. Drop the entry-level XML noise (extensions, namespaces,
GUID isPermaLink flags, etc.). Truncate `description` and `content`
aggressively — feeds are not the place to fetch full article text;
the collector's WebFetch path is.
"""

from __future__ import annotations

from pydantic import BaseModel, Field


# ---------- shared ----------


class FeedItem(BaseModel):
    """One entry from a parsed RSS or Atom feed."""

    title: str | None = Field(
        default=None,
        description="Item title. Strip HTML if present.",
    )
    link: str | None = Field(
        default=None,
        description="Canonical URL of the item (article, blog post, advisory).",
    )
    published: str | None = Field(
        default=None,
        description="ISO 8601 published timestamp, normalized to UTC. Null if feed omits.",
    )
    updated: str | None = Field(
        default=None,
        description="ISO 8601 last-updated timestamp. Atom-only; null for most RSS.",
    )
    summary: str | None = Field(
        default=None,
        description="Short description from <description> or Atom <summary>. Truncated to 1000 chars.",
    )
    content: str | None = Field(
        default=None,
        description="Full content if feed provides <content:encoded> or Atom <content>. "
        "Truncated to 5000 chars. None if not provided (most security blogs only ship summary).",
    )
    author: str | None = Field(
        default=None,
        description="Author name or email if present.",
    )
    guid: str | None = Field(
        default=None,
        description="Unique identifier from <guid> or Atom <id>. Often equals link.",
    )
    categories: list[str] = Field(
        default_factory=list,
        description="Category tags from <category> elements. Empty list if none.",
    )


# ---------- fetch_feed ----------


class FetchFeedInput(BaseModel):
    """Input for fetch_feed."""

    url: str = Field(
        ...,
        description="Full URL of the RSS or Atom feed.",
        min_length=8,  # http://x
    )
    since: str | None = Field(
        default=None,
        description="ISO 8601 timestamp. Items with `published` strictly older than this "
        "are filtered out before returning. Null = no time filter.",
    )
    etag: str | None = Field(
        default=None,
        description="Prior ETag from a recent fetch. Sent as If-None-Match. "
        "If feed returns 304 Not Modified, output `not_modified=true`, no items.",
    )
    last_modified: str | None = Field(
        default=None,
        description="Prior Last-Modified header. Sent as If-Modified-Since. "
        "Same 304 contract as etag.",
    )
    max_items: int | None = Field(
        default=None,
        ge=1,
        le=500,
        description="Cap on items returned (after `since` filter). Defaults to 50.",
    )


class FetchFeedOutput(BaseModel):
    """Result of fetch_feed."""

    found: bool = Field(
        ...,
        description="True if HTTP fetch succeeded AND body parsed as a feed.",
    )
    not_modified: bool = Field(
        default=False,
        description="True if server returned 304 (etag/last_modified hit). items will be empty.",
    )
    feed_url: str
    feed_title: str | None = None
    feed_description: str | None = None
    feed_language: str | None = None
    fetched_at: str = Field(..., description="ISO 8601 UTC timestamp of this fetch.")
    status_code: int = Field(..., description="HTTP status returned by the host.")
    etag: str | None = Field(
        default=None,
        description="ETag from this response. Pass back on next call for caching.",
    )
    last_modified: str | None = Field(
        default=None,
        description="Last-Modified header. Pass back on next call for caching.",
    )
    items: list[FeedItem] = Field(default_factory=list)
    items_total_in_feed: int = Field(
        default=0,
        description="Total items the feed contained before `since` and `max_items` filters.",
    )
    items_after_since_filter: int = Field(
        default=0,
        description="Items remaining after applying `since` filter; before `max_items` cap.",
    )
    parse_warning: str | None = Field(
        default=None,
        description="Set when feedparser produced bozo=1 (malformed but recoverable). Null on clean parse.",
    )


# ---------- validate_feed ----------


class ValidateFeedInput(BaseModel):
    """Input for validate_feed."""

    url: str = Field(..., description="Full URL of the RSS or Atom feed to validate.", min_length=8)


class ValidateFeedOutput(BaseModel):
    """Result of validate_feed.

    Lighter than fetch_feed: returns whether the URL points at a parseable
    feed without ingesting any items. Used by source-health checks and
    operator triage.
    """

    valid: bool = Field(
        ...,
        description="True if HTTP returned 2xx AND body parsed as a feed with at least metadata.",
    )
    feed_url: str
    status_code: int
    feed_title: str | None = None
    feed_type: str | None = Field(
        default=None,
        description="'rss', 'atom', or 'unknown'. Null if not parseable.",
    )
    items_total: int = Field(default=0, description="Item count in the feed (no filtering).")
    error: str | None = Field(
        default=None,
        description="Short error description if valid=false. Null on success.",
    )
