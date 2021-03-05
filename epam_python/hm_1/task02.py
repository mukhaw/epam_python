"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""
from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    i = 0
    while i != len(data) - 2:
        if data[i + 2] == data[i + 1] + data[i]:
            i += 1
        else:
            break
    return True if i == len(data) - 2 else False
