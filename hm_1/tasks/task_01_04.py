from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    count = 0
    [
        count := count + 1
        for i in d
        for j in c
        for k in b
        for h in a
        if i + j + k + h == 0
    ]
    return count
