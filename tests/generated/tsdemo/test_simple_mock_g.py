import tsdemo.service
from testscribe.api.mock_api import get_normalized_mock_calls
from unittest.mock import ANY, call, create_autospec
from tsdemo.simple_mock import search_name


def test_search_name():
    m_service: tsdemo.service.Service = create_autospec(spec=tsdemo.service.Service)
    m_service.search_a_name.return_value = 'real Bob'
    result = search_name(service=m_service, keyword='Bob')
    assert result == '{"name": "real Bob"}'
    m_service_mock_calls = get_normalized_mock_calls(m_service, tsdemo.service.Service)
    assert m_service_mock_calls == [
        call.search_a_name(keyword='key: Bob'),
    ]
