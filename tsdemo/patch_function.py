"""
Patch a function
"""


def calculate(seed: int) -> int:
    # This is a simplified example. It can do complex calculation, access a remote database etc.
    return seed + 1


def call_fixed_func(num: int):
    return calculate(num)
