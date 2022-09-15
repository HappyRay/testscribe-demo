"""
Create or mock objects in a list
"""
from typing import List

from tsdemo.person import Person


def get_average_age(person_list: List[Person]) -> int:
    total = 0
    for p in person_list:
        total += p.age
    return int(total/len(person_list))
