#!/usr/bin/env python3
"""Chunk a brief body into <=1900-char parts on blank-line boundaries.

Mirrors scripts/deliver_catchup.py's chunk_text logic so FLASH posts use the
same packing discipline. Writes part files (part-1.md, part-2.md, ...) next to
the input.
"""

import re
import sys
from pathlib import Path

CHUNK_LIMIT = 1900  # headroom under Discord's hard 2000-char cap


def chunk_text(body: str, limit: int, prefix: str = "") -> list[str]:
    paragraphs = re.split(r"\n\s*\n", body.strip())
    chunks: list[str] = []
    current = prefix.rstrip("\n")

    def flush():
        nonlocal current
        if current.strip():
            chunks.append(current.strip("\n"))
        current = ""

    for para in paragraphs:
        para = para.strip("\n")
        if not para:
            continue
        while len(para) > limit:
            head, para = para[:limit], para[limit:]
            if current.strip():
                flush()
            chunks.append(head)
        candidate = f"{current}\n\n{para}".strip("\n") if current.strip() else para
        if len(candidate) <= limit:
            current = candidate
        else:
            flush()
            current = para
    flush()
    return chunks


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print("usage: chunk_brief.py <input_body.md> <out_prefix>", file=sys.stderr)
        return 2
    src = Path(argv[1])
    out_prefix = argv[2]
    body = src.read_text(encoding="utf-8")
    chunks = chunk_text(body, CHUNK_LIMIT)
    if len(chunks) > 1:
        # Add small footer for parts so readers know they're related.
        chunks = [f"{c}\n\n-# (part {i + 1}/{len(chunks)})" for i, c in enumerate(chunks)]
    for c in chunks:
        if len(c) > 2000:
            print(f"ERROR: chunk exceeds 2000 chars after packing: {len(c)}", file=sys.stderr)
            return 3
    out_dir = src.parent
    for i, c in enumerate(chunks):
        out = out_dir / f"{out_prefix}-part-{i + 1}.md"
        out.write_text(c, encoding="utf-8")
        print(f"wrote {out} ({len(c)} chars)")
    print(f"total_parts={len(chunks)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
