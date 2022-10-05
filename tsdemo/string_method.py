"""
Use a wrapper function to test.

The wrapper function normally would be placed under a test folder.
For easy demonstration, it is placed in the same module.
"""


class StringMethod:
    def __init__(self, text: str):
        self.text = text

    def __str__(self):
        return self.text


def str_method_wrapper(text: str):
    return str(StringMethod(text))
