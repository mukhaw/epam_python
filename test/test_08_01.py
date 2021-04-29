from tempfile import NamedTemporaryFile

import pytest

from hm_1.tasks.task_08_01 import KeyValueStorage


def test_class_keyvaluestorage_returns_values_by_key():
    with NamedTemporaryFile(delete=True) as f:
        f.write(b"name=kek\nlast_name=top\npower=9001\nsong=shadilay")
        f.seek(0)
        storage = KeyValueStorage(f.name)
        assert storage["name"] == "kek"
        assert storage["last_name"] == "top"
        assert storage["power"] == 9001
        assert storage["song"] == "shadilay"


def test_class_keyvaluestorage_returns_values_by_attribute():
    with NamedTemporaryFile(delete=True) as f:
        f.write(b"name=kek\nlast_name=top\npower=9001\nsong=shadilay")
        f.seek(0)
        storage = KeyValueStorage(f.name)
        assert storage.name == "kek"
        assert storage.last_name == "top"
        assert storage.power == 9001
        assert storage.song == "shadilay"


def test_class_keyvaluestorage_returns_empty_dict():
    with NamedTemporaryFile(delete=True) as f:
        f.write(b"")
        f.seek(0)
        storage = KeyValueStorage(f.name)
        assert storage == {}


def class_keyvaluestorage_returns_value_error():
    with NamedTemporaryFile(delete=True) as f:
        f.write(b"name=kek=gh\nlast_name=top\npower=9001\nsong=shadilay")
        f.seek(0)
        KeyValueStorage(f.name)


def test_class_keyvaluestorage_returns_value_error():
    with pytest.raises(ValueError, match="Something wrong with your attributes"):
        class_keyvaluestorage_returns_value_error()
