import os
from typing import Tuple

import pytest

from hm_1.tasks.task_01_03 import find_maximum_and_minimum


@pytest.mark.parametrize(
    ("file_name", "expected_result"),
    [
        (os.path.dirname(__file__) + "/sample1.txt", (113, -9)),
        (os.path.dirname(__file__) + "/sample2.txt", (34, -2)),
        (os.path.dirname(__file__) + "/sample3.txt", (1, 1)),
    ],
)
def test_find_maximum_and_minimum(file_name: str, expected_result: Tuple[int, int]):
    actual_result = find_maximum_and_minimum(file_name)

    assert actual_result == expected_result
