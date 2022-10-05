"""
Annotate class instance member variables with type information
"""


class Car:
    model: str

    def __init__(self, owner: str, model: str):
        self.owner = owner
        self.model = model


def get_car_info(car: Car) -> str:
    return f"Car model: {car.model}, owner: {car.owner}"
