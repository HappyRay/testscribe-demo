from attr import dataclass


@dataclass
class Person:
    name: str = ""
    age: int = 10
