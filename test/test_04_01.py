from tempfile import NamedTemporaryFile

import pytest

from hm_1.tasks.task_04_01 import read_magic_number


def test_read_magic_number_returns_true():
    with NamedTemporaryFile(delete=True) as f:
        f.write(b"1")
        f.seek(0)
        assert read_magic_number(f.name) is True


def test_read_magic_number_returns_true_():
    with NamedTemporaryFile(delete=True) as f:
        f.write(b"2")
        f.seek(0)
        assert read_magic_number(f.name) is True


def test_read_magic_number_with_wrong_number_returns_false():
    with NamedTemporaryFile(delete=True) as f:
        f.write(b"3")
        f.seek(0)
        assert read_magic_number(f.name) is False


def test_read_magic_number_with_str_returns_false():
    with NamedTemporaryFile(delete=True) as f:
        f.write(b"jkjhkh")
        f.seek(0)
        assert read_magic_number(f.name) is False


def test_read_magic_number_with_empty_str_returns_false():
    with NamedTemporaryFile(delete=True) as f:
        f.write(b"")
        f.seek(0)
        assert read_magic_number(f.name) is False


def test_read_magic_number_returns_value_erorr():
    with pytest.raises(ValueError, match="This is ValueError mistake"):
        read_magic_number("not_exist.txt")
