from hm_1.tasks.task_05_02 import print_result


def test_custom_sum_returns_a_sum(capsys):
    print_result(sum)(1, 2)
    out, _ = capsys.readouterr()
    assert out == "[3]\n"
    assert sum.__name__ == "custom_sum"
