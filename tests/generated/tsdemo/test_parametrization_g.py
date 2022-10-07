from tsdemo.parametrization import eval_expression


def test_eval_expression_multiplication():
    result = eval_expression(expr='6 * 9')
    assert result == 54


def test_eval_expression_addition_1():
    result = eval_expression(expr='2 + 4')
    assert result == 6


def test_eval_expression_addition():
    result = eval_expression(expr='3 + 5')
    assert result == 8
