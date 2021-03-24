import pytest

from hm_1.tasks.task_03_04 import is_armstrong


@pytest.mark.parametrize("value", [1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407])
def test_is_armstrong_returns_true(value: int):
    assert is_armstrong(value) is True


@pytest.mark.parametrize(
    "value",
    [0, 31, 511, 1023],
)
def test_is_armstrong_returns_false(value: int):
    assert is_armstrong(value) is False
