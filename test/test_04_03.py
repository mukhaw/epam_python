from hm_1.tasks.task_04_03 import my_precious_logger


def test_my_precious_logger_returns_error(capsys):
    my_precious_logger("error: file not found")
    assert capsys.readouterr().err == "error: file not found"


def test_my_precious_logger_returns_ok(capsys):
    my_precious_logger("ok")
    assert capsys.readouterr().out == "ok"
