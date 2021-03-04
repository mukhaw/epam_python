from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    i = 0
    while i != len(data) - 2:
        if data[i + 2] == data[i + 1] + data[i]:
            i += 1
        else:
            break
    return True if i == len(data) - 2 else False
