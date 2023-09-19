"""
Results that contain class instances.
The class implements a custom __repr__ method.
The result display and generated assertions will be based on the repr() result.
"""
from dataclasses import dataclass


@dataclass
class ClassWithRepr:
    str_field: str
    int_field: int


def create_class_with_repr_instance():
    return ClassWithRepr(str_field="a", int_field=1)
