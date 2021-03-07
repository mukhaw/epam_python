from typing import List

import pytest

from hm_1.tasks.task_01_05 import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ("numbers", "k", "expected_result"),
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
        ([1, 19, 0, -9, -7, 0, 5, 10, 11, 4], 4, 30),
        ([1, 2, 3, 4, 5], 1, 5),
        ([1], 1, 1),
        ([1, 2], 2, 3),
        ([1, 2], 1, 2),
        ([0, 1, 2, 3, 4, 5, 6, 7, 8], 8, 36),
        ([0, 1, 2, 3, 4, 5, 6, 7, 8], 7, 35),
        ([], 0, "Your list is empty or size of subarray > length of your list"),
        ([1, 2, 3], 14, "Your list is empty or size of subarray > length of your list"),
    ],
)
def test_check_fibonacci(numbers: List[int], k: int, expected_result: int):
    actual_result = find_maximal_subarray_sum(numbers, k)

    assert actual_result == expected_result
