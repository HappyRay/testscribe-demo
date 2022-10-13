"""
Results that contain class instances.
The class doesn't implement a custom __repr__ method.
The result display and generated assertions will be based on member fields.
"""


class SimpleClass:
    str_field: str
    int_field: int

    def __init__(self, s: str, i: int):
        self.str_field = s
        self.int_field = i


def create_simple_class_instance(s: str, i: int):
    return SimpleClass(s=s, i=i)
