from unittest.mock import Mock

import pytest

from hm_1.tasks.task_04_02 import count_dots_on_i


@pytest.mark.parametrize(
    ("url", "expected_result"),
    [
        ("https://example.com/", 59),
        ("https://docs.python.org/3/howto/urllib2.html", 2052),
    ],
)
def test_count_dots_on_i(url: str, expected_result: int):
    mock = Mock(side_effect=count_dots_on_i)
    assert mock(url) == expected_result


def test_count_dots_on_i_return_value_error():
    url = "https://not_exist_url.com/"
    with pytest.raises(ValueError, match=f"Unreachable {url}"):
        count_dots_on_i(url)
