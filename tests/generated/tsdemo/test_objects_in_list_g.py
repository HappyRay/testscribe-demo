import tsdemo.person
from testscribe.api.mock_api import get_normalized_mock_calls
from unittest.mock import ANY, call, create_autospec
from tsdemo.objects_in_list import get_average_age


def test_get_average_age_1():
    m_person: tsdemo.person.Person = create_autospec(spec=tsdemo.person.Person)
    m_person_1: tsdemo.person.Person = create_autospec(spec=tsdemo.person.Person)
    m_person.age = 2
    m_person_1.age = 3
    result = get_average_age(person_list=[m_person, m_person_1])
    assert result == 2
    m_person.assert_not_called()
    m_person_1.assert_not_called()


def test_get_average_age():
    result = get_average_age(person_list=[tsdemo.person.Person("a", 2), tsdemo.person.Person("b", 3)])
    assert result == 2
