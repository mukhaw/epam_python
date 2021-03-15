"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""
from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    if data == [0]:
        return True
    if len(data) <= 1 or (data[0:2] != [0, 1]):
        return False
    else:
        for i in range(len(data) - 2):
            if data[i + 2] != sum(data[i : i + 2]):
                return False
    return True
