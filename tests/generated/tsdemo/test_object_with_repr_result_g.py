import tsdemo.object_with_repr_result
from tsdemo.object_with_repr_result import create_class_with_repr_instance


def test_create_class_with_repr_instance():
    result = create_class_with_repr_instance()
    assert isinstance(result, tsdemo.object_with_repr_result.ClassWithRepr)
    assert repr(result) == "ClassWithRepr(str_field='a', int_field=1)"
