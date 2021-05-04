from tempfile import NamedTemporaryFile

from hm_1.tasks.task_09_01 import merge_sorted_files


def test_merge_sorted_file_return_sorted_list():
    with NamedTemporaryFile(delete=True) as first, NamedTemporaryFile(
        delete=True
    ) as second:
        first.write(b"1\n3\n5\n")
        first.seek(0)
        second.write(b"2\n4\n6\n")
        second.seek(0)
        assert merge_sorted_files([first.name, second.name]) == [1, 2, 3, 4, 5, 6]


def test_merge_sorted_file_with_one_empty_file_return_sotred_second_list():
    with NamedTemporaryFile(delete=True) as first, NamedTemporaryFile(
        delete=True
    ) as second:
        first.write(b"")
        first.seek(0)
        second.write(b"2\n4\n6\n")
        second.seek(0)
        assert merge_sorted_files([first.name, second.name]) == [2, 4, 6]


def test_merge_sorted_file_with_one_empty_file_return_sotred_empty_list():
    with NamedTemporaryFile(delete=True) as first, NamedTemporaryFile(
        delete=True
    ) as second:
        first.write(b"")
        first.seek(0)
        second.write(b"")
        second.seek(0)
        assert merge_sorted_files([first.name, second.name]) == []
