from typing import Sequence

import pytest

from hm_1.tasks.task02 import check_fibonacci


@pytest.mark.parametrize(
    ("values", "expected_result"),
    [
        ([1, 1, 2, 3, 5, 8], True),
        ([1, 1, 3, 4], False),
        ([1, 1], True),
        ([1, 1, 2, 3, 5, 8, 13], True),
    ],
)
def test_check_fibonacci(values: Sequence[int], expected_result: bool):
    actual_result = check_fibonacci(values)

    assert actual_result == expected_result
