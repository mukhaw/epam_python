from typing import Tuple

import pytest

from epam_python.hm_1.tasks.task03 import find_maximum_and_minimum


@pytest.mark.parametrize(
    ("file_name", "expected_result"),
    [
        ("sample1.txt", (112, -9)),
        ("sample2.txt", (3, 0)),
        ("sample3.txt", (0, 0)),
    ],
)
def test_find_maximum_and_minimum(file_name: str, expected_result: Tuple[int, int]):
    actual_result = find_maximum_and_minimum(file_name)

    assert actual_result == expected_result
