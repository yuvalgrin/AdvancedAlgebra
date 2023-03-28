from typing import List

from utils.prime_utils import is_prime


class FiniteField:
    def __init__(self, p: int, function: List[int]):
        if not is_prime(p):
            raise ValueError(f"p ({p}) must be prime")
        if len(function) <= 3:
            print('Should check for irreducible')
        self.p = p
        self.f = function

    def __eq__(self, other):
        return self.f == other.f and self.p == other.p

    def __repr__(self):
        return f'FiniteField({self.p}, {self.f})'
