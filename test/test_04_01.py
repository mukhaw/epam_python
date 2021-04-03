from testfixtures import TempDirectory

from hm_1.tasks.task_04_01 import read_magic_number


def test_read_magic_number_returns_true():
    d = TempDirectory()
    d.write("test.txt", b"123")
    return read_magic_number(d.path)
