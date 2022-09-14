"""
Create a real instance of a class as an input
"""
from tsdemo.person import Person


def get_person_age(p: Person) -> int:
    return p.age
