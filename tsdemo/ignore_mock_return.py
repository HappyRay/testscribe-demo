"""
Ignore the return value of a mock call
"""


class Printer:
    def __init__(self, prefix: str):
        self.prefix = prefix

    def display(self, text) -> str:
        formatted = f"{self.prefix}.{text}"
        print(formatted)
        return formatted


def show(text: str, printer: Printer):
    printer.display(text)

