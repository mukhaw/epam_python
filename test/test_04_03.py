from hm_1.tasks.task_04_03 import my_precious_logger


def test_my_precious_logger():
    my_precious_logger("error: file not found")
    assert my_precious_logger("error: file not found") == "error: file not found"
