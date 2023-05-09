from typing import List

from utils.prime_utils import is_prime


class FiniteField:
    def __init__(self, p: int, function: List[int]):
        if not is_prime(p):
            raise ValueError(f"p ({p}) must be prime")
        if int(function[-1]) == 0:
            raise ValueError(f"The last coefficient cannot be zero since it represents the highest order of the irreducible polynom: {function}")
        if len(function) <= 3 and not is_irreducible(p, function):
            raise ValueError(f"Function {function} and prime {p} are not irreducible")
        self.p = p
        self.f = function
        self.polyorder = len(function) - 1

    def __hash__(self):
        return hash((self.p, tuple(self.f)))

    def __eq__(self, other):
        return self.f == other.f and self.p == other.p

    def __repr__(self):
        return f'FiniteField({self.p}, {self.f})'


def is_irreducible(p: int, function: List[int]):
    for i in range(0, p):
        sum = 0
        for idx, x in enumerate(function):
            sum += (i ** idx) * x
        if sum % p == 0:
            return False
    return True
