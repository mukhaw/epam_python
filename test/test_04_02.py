from unittest.mock import patch

import pytest

from hm_1.tasks.task_04_02 import count_dots_on_i


def test_count_dots_on_i():
    with patch("requests.get") as fake:
        fake.return_value = 59
        assert count_dots_on_i("https://example.com/") == fake.return_value


def test_count_dots_on_i_return_value_error():
    url = "https://not_exist_url.com/"
    with pytest.raises(ValueError, match=f"Unreachable {url}"):
        count_dots_on_i(url)
