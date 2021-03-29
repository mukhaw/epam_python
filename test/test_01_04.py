from typing import List

import pytest

from hm_1.tasks.task_01_04 import check_sum_of_four


@pytest.mark.parametrize(
    ("a", "b", "c", "d", "expected_result"),
    [
        ([1, 1, 1, 1], [1, 1, 1], [-1, -1], [-1], 24),
        ([1, 1], [2, 2], [3, 3], [4, 4], 0),
        ([1], [], [], [], 0),
        ([1], [-1], [], [], 0),
        ([], [], [], [], 0),
    ],
)
def test_check_fibonacci(
    a: List[int], b: List[int], c: List[int], d: List[int], expected_result: int
):
    actual_result = check_sum_of_four(a, b, c, d)

    assert actual_result == expected_result
