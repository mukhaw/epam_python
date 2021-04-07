from tempfile import NamedTemporaryFile

import pytest

from hm_1.tasks.task_04_01 import read_magic_number


def test_read_magic_number_returns_true():
    f = NamedTemporaryFile(delete=True)
    f.write(b"1\n")
    f.seek(0)
    actual_result = read_magic_number(f.name)
    f.close()
    assert actual_result is True


def test_read_magic_number_returns_true_():
    f = NamedTemporaryFile(delete=True)
    f.write(b"2\n")
    f.seek(0)
    actual_result = read_magic_number(f.name)
    f.close()
    assert actual_result is True


def test_read_magic_number_with_wrong_number_returns_false():
    f = NamedTemporaryFile(delete=True)
    f.write(b"3")
    f.seek(0)
    actual_result = read_magic_number(f.name)
    f.close()
    assert actual_result is False


def test_read_magic_number_with_str_returns_false():
    f = NamedTemporaryFile(delete=True)
    f.write(b"hkjh\n")
    f.seek(0)
    actual_result = read_magic_number(f.name)
    f.close()
    assert actual_result is False


def test_read_magic_number_with_empty_str_returns_false():
    f = NamedTemporaryFile(delete=True)
    f.write(b"")
    f.seek(0)
    actual_result = read_magic_number(f.name)
    f.close()
    assert actual_result is False


def test_read_magic_number_returns_value_erorr():
    with pytest.raises(ValueError, match="This is ValueError mistake"):
        read_magic_number("test.txt")
