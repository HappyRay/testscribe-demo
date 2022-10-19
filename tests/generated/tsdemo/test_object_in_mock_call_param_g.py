import tsdemo.object_in_mock_call_param
from testscribe.api.mock_api import get_normalized_mock_calls
from unittest.mock import ANY, call, create_autospec
from tsdemo.object_in_mock_call_param import call_b_method


def test_call_b_method():
    m_b: tsdemo.object_in_mock_call_param.B = create_autospec(spec=tsdemo.object_in_mock_call_param.B)
    m_b.do.return_value = None
    result = call_b_method(b=m_b)
    assert result is None
    m_b_mock_calls = get_normalized_mock_calls(m_b, tsdemo.object_in_mock_call_param.B)
    assert m_b_mock_calls == [
        call.do(a=ANY),
    ]
    assert isinstance(m_b_mock_calls[0].kwargs['a'], tsdemo.object_in_mock_call_param.A)
    assert repr(m_b_mock_calls[0].kwargs['a']) == 'A(i=1)'
