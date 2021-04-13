import urllib.request
from collections import Counter


def count_dots_on_i(url: str) -> int:
    try:
        with urllib.request.urlopen(url) as response:
            html = str(response.read())
        return Counter(html)["i"]
    except Exception:
        raise ValueError(f"Unreachable {url}")
