from unittest.mock import patch

from hm_1.tasks.task_04_02 import count_dots_on_i


def test_count_dots_on_i():
    with patch("requests.get") as mock_request:
        url = "https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen"
        mock_request.return_value = 7019
        assert count_dots_on_i(url) == mock_request.return_value
