import tsdemo.person
from tsdemo.create_object import get_person_age


def test_get_person_age():
    result = get_person_age(p=tsdemo.person.Person("Bob", 10))
    assert result == 10
