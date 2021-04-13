from hm_1.tasks.task_04_03 import my_precious_logger


def test_my_precious_logger_returns_error(capsys):
    my_precious_logger("error: file not found")
    out, err = capsys.readouterr()
    assert out == ""
    assert err == "error: file not found"


def test_my_precious_logger_returns_ok(capsys):
    my_precious_logger("ok")
    out, err = capsys.readouterr()
    assert out == "ok"
    assert err == ""


def test_my_precious_logger_recieve_not_in_start_str_error_returns_stdout_error(capsys):
    my_precious_logger("not start str error")
    out, err = capsys.readouterr()
    assert out == "not start str error"
    assert err == ""
