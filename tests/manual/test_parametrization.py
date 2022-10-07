import pytest

from tsdemo.parametrization import eval_expression


@pytest.mark.parametrize("expression,expected", [("3+5", 8), ("2+4", 6), ("6*9", 54)])
def test_eval_expression(expression, expected):
    assert eval_expression(expression) == expected
