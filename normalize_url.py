#!/usr/bin/env python3
"""Normalize URLs to their bare domain.

Strips the scheme, "www.", credentials, port, path, query and fragment:

    https://www.vendor.com/about  ->  vendor.com

Usage:
    python normalize_url.py https://www.vendor.com/about http://Example.org:8080/x
    cat urls.txt | python normalize_url.py
"""

import sys
from urllib.parse import urlsplit


def normalize_url(url: str) -> str:
    """Return the bare, lowercase domain for a URL (or "" if none)."""
    url = url.strip()
    if not url:
        return ""

    # urlsplit only finds the host when it follows "//", so add it for
    # inputs like "www.vendor.com/about" that have no scheme.
    if "//" not in url:
        url = "//" + url

    host = urlsplit(url).hostname or ""  # drops user:pass@ and :port, lowercases
    host = host.rstrip(".")
    if host.startswith("www."):
        host = host[4:]
    return host


def main(argv: list[str]) -> int:
    urls = argv[1:] if len(argv) > 1 else sys.stdin
    for url in urls:
        if url.strip():
            print(normalize_url(url))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
