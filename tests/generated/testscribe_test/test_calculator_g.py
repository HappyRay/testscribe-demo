from testscribe_test.calculator import add


def test_add():
    result = add(a=1, b=2)
    assert result == 3
