import urllib.request
from collections import Counter


def count_dots_on_i(url: str) -> int:
    with urllib.request.urlopen(url) as response:
        html = str(response.read())
    return Counter(html)["i"]
