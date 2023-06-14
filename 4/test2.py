from task02 import count_dots_on_i
import pytest
@pytest('urllib.request.urlopen')
def test_count_dots_on_i(mock_urlopen):
    mock_urlopen.return_value.read.return_value.decode.return_value = 'iii'
    assert count_dots_on_i('https://example.com/') == 3

    mock_urlopen.return_value.read.return_value.decode.return_value = 'i' * 59
    assert count_dots_on_i('https://example.com/') == 59

    mock_urlopen.side_effect = Exception("Network error")
    try:
        count_dots_on_i('https://example.com/')
    except ValueError as e:
        assert str(e) == "Unreachable https://example.com/"
    else:
        assert False, "Expected ValueError"