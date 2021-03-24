from testfixtures import TempDirectory

from hm_1.tasks.task_04_01 import read_magic_number


def test_read_magic_number_false():
    d = TempDirectory()
    d.write("test.txt", b"some foo thing")
    assert read_magic_number(d.path + "/test.txt") is False
    d.cleanup()


def test_read_magic_number_false_():
    d = TempDirectory()
    d.write("test.txt", b"3")
    assert read_magic_number(d.path + "/test.txt") is False
    d.cleanup()
