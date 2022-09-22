from testscribe.api.mock_api import patch_with_mock

from tsdemo.patch_function import calculate


def setup():
    print("setup function in tests is called.")
    # patch_with_mock(calculate)
