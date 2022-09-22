import tsdemo.patch_function
from testscribe.api.mock_api import get_normalized_mock_calls
from unittest.mock import ANY, call, create_autospec
from unittest.mock import patch
from tsdemo.patch_function import call_fixed_func


def test_call_fixed_func():
    m_calculate: tsdemo.patch_function.calculate = create_autospec(spec=tsdemo.patch_function.calculate)
    m_calculate.return_value = 1
    with patch('tsdemo.patch_function.calculate', m_calculate):
        result = call_fixed_func(num=2)
    assert result == 1
    m_calculate_mock_calls = get_normalized_mock_calls(m_calculate, tsdemo.patch_function.calculate)
    assert m_calculate_mock_calls == [
        call(seed=2),
    ]
