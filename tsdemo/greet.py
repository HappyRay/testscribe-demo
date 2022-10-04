"""
test a class method
"""


class Greeter:
    def __init__(self, my_name: str):
        self.my_name = my_name

    def greet(self, to: str) -> str:
        return f"Hello {to}. My name is {self.my_name}"
