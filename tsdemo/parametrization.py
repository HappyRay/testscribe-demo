"""
Compare using the tool to generate multiple tests for different input sets vs
manually writing tests using pytest's test parametrization support.
The example is modeled after the example at
https://docs.pytest.org/how-to/parametrize.html#parametrize-basics
"""


def eval_expression(expr: str):
    return eval(expr)
