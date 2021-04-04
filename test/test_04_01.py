from tempfile import NamedTemporaryFile

import pytest

from hm_1.tasks.task_04_01 import read_magic_number


def test_read_magic_number_returns_true():
    f = NamedTemporaryFile(delete=False)
    f.write(b"1\n")
    f.seek(0)
    assert read_magic_number(f.name) is True
    f.close()


def test_read_magic_number_returns_false():
    f = NamedTemporaryFile(delete=False)
    f.write(b"3")
    f.seek(0)
    assert read_magic_number(f.name) is False
    f.close()


def test_read_magic_number_returns_value_erorr():
    with pytest.raises(ValueError, match="This is ValueError mistake"):
        read_magic_number("test.txt")
