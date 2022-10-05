from tsdemo.string_method import str_method_wrapper


def test_str_method_wrapper():
    result = str_method_wrapper(text='a')
    assert result == 'a'
