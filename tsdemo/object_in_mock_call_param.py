from attr import dataclass


@dataclass
class A:
    i: int


class B:
    def do(self, a: A) -> None:
        pass


def call_b_method(b: B):
    b.do(A(1))
