from testscribe.api.mock_api import patch_with_mock, patch_with_expression

# from tsdemo.patch_function import calculate


def setup():
    print("setup function in tests is called.")
    # patch_with_mock(calculate)
    # patch_with_expression(target_str="tsdemo.patch_string.DB_NAME", expression="'test'")
