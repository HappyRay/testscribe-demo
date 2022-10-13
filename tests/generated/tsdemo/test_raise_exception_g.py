import pytest
from tsdemo.raise_exception import always_raise_exception


def test_always_raise_exception():
    with pytest.raises(Exception) as exception_info:
        always_raise_exception()
    assert 'test exception' == str(exception_info.value)
