import tsdemo.ignore_mock_return
from testscribe.api.mock_api import get_normalized_mock_calls
from unittest.mock import ANY, call, create_autospec
from tsdemo.ignore_mock_return import show


def test_show():
    m_printer: tsdemo.ignore_mock_return.Printer = create_autospec(spec=tsdemo.ignore_mock_return.Printer)
    result = show(text='a', printer=m_printer)
    assert result is None
    m_printer_mock_calls = get_normalized_mock_calls(m_printer, tsdemo.ignore_mock_return.Printer)
    assert m_printer_mock_calls == [
        call.display(text='a'),
    ]
