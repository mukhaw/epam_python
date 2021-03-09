import pytest

from hm_1.tasks.task_01_01 import check_power_of_2


@pytest.mark.parametrize(
    ("value", "expected_result"),
    [
        (65536, True),
        (12, False),
    ],
)
def test_power_of_2(value: int, expected_result: bool):
    actual_result = check_power_of_2(value)

    assert actual_result == expected_result
