from collections import Counter
from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    inp = Counter(inp).most_common()
    return inp[0][0], inp[len(inp) - 1][0]
