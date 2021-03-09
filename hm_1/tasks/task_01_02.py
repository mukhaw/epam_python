"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""
from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    res = 0
    if len(data) <= 1 or (data[0:2] != [0, 1]):
        res = -1
    else:
        [
            res := -1
            for i in range(len(data) - 2)
            if data[i + 2] != data[i + 1] + data[i]
        ]
    return False if res == -1 else True
