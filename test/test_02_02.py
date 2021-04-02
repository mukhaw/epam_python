from typing import List, Tuple

import pytest

from hm_1.tasks.task_02_02 import major_and_minor_elem


@pytest.mark.parametrize(
    ("values", "expected_result"),
    [
        ([3], (3, 3)),
        ([3, 2, 3], (3, 2)),
        ([2, 2, 1, 1, 2, 2], (2, 1)),
        ([1, 1, 1, 2, 2, 3], (1, 3)),
        ([1, 1, 1, 1, 2, 2, 2, 3], (1, 3)),
    ],
)
def test_check_major_and_minor_elem(values: List, expected_result: Tuple[int, int]):
    actual_result = major_and_minor_elem(values)

    assert actual_result == expected_result
