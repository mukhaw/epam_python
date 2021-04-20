from hm_1.tasks.task_05_02 import custom_sum


def test_custom_sum_():
    custom_sum([1, 2, 3], [4, 5])
    assert (
        custom_sum.__doc__
        == """This function can sum any objects which have __add___"""
    )
    assert custom_sum.__name__ == "custom_sum"
