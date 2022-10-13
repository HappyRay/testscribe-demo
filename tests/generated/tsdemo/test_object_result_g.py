import tsdemo.object_result
from tsdemo.object_result import create_simple_class_instance


def test_create_simple_class_instance():
    result = create_simple_class_instance()
    assert isinstance(result, tsdemo.object_result.SimpleClass)
    assert result.str_field == 'a'
    assert result.int_field == 1
