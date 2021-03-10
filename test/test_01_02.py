from typing import Sequence

import pytest

from hm_1.tasks.task_01_02 import check_fibonacci


@pytest.mark.parametrize(
    "value",
    [[0, 1, 1, 2], [0, 1, 1], [0, 1, 1, 2, 3, 5, 8], [0, 1, 1, 2, 3, 5, 8, 13]],
)
def test_sequence_is_fibonacci(value: Sequence[int]):
    assert check_fibonacci(value) is True


@pytest.mark.parametrize(
    "value",
    [[0], [4], [0, 1, 1, 3], [1, 1, 2], [1, 1], [0, 1, 2, 1, 2, 3, 5, 8]],
)
def test_sequence_is_not_fibonacci(value: Sequence[int]):
    assert check_fibonacci(value) is False


def test_empty_sequence_is_fibonacci():
    assert check_fibonacci([]) is False
