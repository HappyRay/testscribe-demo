import tsdemo.annotate_field_type
from testscribe.api.mock_api import get_normalized_mock_calls
from unittest.mock import ANY, call, create_autospec
from tsdemo.annotate_field_type import get_car_info


def test_get_car_info():
    m_car: tsdemo.annotate_field_type.Car = create_autospec(spec=tsdemo.annotate_field_type.Car)
    m_car.model = 'camery'
    m_car.owner = 'Bob'
    result = get_car_info(car=m_car)
    assert result == 'Car model: camery, owner: Bob'
    m_car.assert_not_called()
