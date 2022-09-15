import tsdemo.person
from tsdemo.objects_in_list import get_average_age


def test_get_average_age():
    result = get_average_age(person_list=[tsdemo.person.Person("a", 2), tsdemo.person.Person("b", 3)])
    assert result == 2
