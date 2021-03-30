import pytest

from hm_1.tasks.task_03_03 import Filter, make_filter, sample_data


@pytest.mark.parametrize(
    ("function", "data", "exepected_result"),
    [
        ((lambda a: a % 3 == 0, lambda a: a > 3), range(0, 20), [6, 9, 12, 15, 18]),
        (
            (lambda a: a & (a - 1) == 0 and a != 0, lambda a: a <= 16),
            range(0, 64),
            [1, 2, 4, 8, 16],
        ),
    ],
)
def test_filter_apply_returns_filtered_list(function, data, exepected_result):
    assert Filter(*function).apply(data) == exepected_result


def test_make_filter_with():
    exepected_result = [
        {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
        {"is_dead": False, "kind": "swallow", "type": "bird", "name": "polly"},
    ]

    assert make_filter(name="polly", type="bird").apply(sample_data) == exepected_result


# ПЕРЕПИШИ ЭТОТ УЖАС
