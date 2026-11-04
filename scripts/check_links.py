#!/usr/bin/env python3
"""Check the links listed in README.md and report their HTTP status.

Usage:
    python3 scripts/check_links.py

Exit code is 0 when every link answers with a 2xx or 3xx status, and 1 otherwise.
Only the Python standard library is used.
"""

import pathlib
import re
import sys
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
TIMEOUT = 15
USER_AGENT = "free-ai-stack-link-check/1.0 (+https://github.com/Mohsinraza23/free-ai-stack)"


def extract_links(text: str) -> list[str]:
    """Return unique http(s) links found in the README, in order."""
    found = re.findall(r"https?://[^\s\)\"'<>]+", text)
    seen, unique = set(), []
    for link in found:
        link = link.rstrip(".,")
        if link not in seen:
            seen.add(link)
            unique.append(link)
    return unique


def check(url: str) -> tuple[bool, str]:
    """Return (ok, status) for one URL. Uses HEAD first, then GET if HEAD is refused."""
    for method in ("HEAD", "GET"):
        request = urllib.request.Request(url, method=method, headers={"User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
                code = response.status
                return 200 <= code < 400, str(code)
        except urllib.error.HTTPError as error:
            if method == "HEAD" and error.code in (405, 403, 501):
                continue
            return False, str(error.code)
        except (urllib.error.URLError, TimeoutError, OSError) as error:
            return False, f"error: {getattr(error, 'reason', error)}"
    return False, "no response"


def main() -> int:
    links = extract_links(README.read_text(encoding="utf-8"))
    failures = 0
    for url in links:
        ok, status = check(url)
        mark = "OK  " if ok else "FAIL"
        print(f"{mark} {status:>6}  {url}")
        if not ok:
            failures += 1
    print(f"\nChecked {len(links)} links, {failures} failed.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
