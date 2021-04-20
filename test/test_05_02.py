from hm_1.tasks.task_05_02 import custom_sum


def test_custom_sum_returns_a_sum(capsys):
    custom_sum([1, 2, 3], [4, 5])
    out, _ = capsys.readouterr()
    assert out == "[1, 2, 3, 4, 5]\n"


def test_custom_sum__doc__returns_a_string():
    assert (
        custom_sum.__doc__
        == """This function can sum any objects which have __add___"""
    )


def test_custom_sum_returns__name__custom_sum():
    assert custom_sum.__name__ == "custom_sum"


def test_custom_sum_returns__original_func__custom_sum():
    assert type(custom_sum.__original_func) == type(custom_sum)
