import math

from algo.extended_euclides_algo import inverse_modulo
from utils.prime_utils import is_prime


class FiniteFieldElement:
    def __init__(self, a, p):
        if not is_prime(p):
            raise ValueError(f"p ({p}) must be prime")
        self.a = a % p
        self.p = p

    def __add__(self, other):
        raise NotImplementedError()

    def __sub__(self, other):
        raise NotImplementedError()

    def __mul__(self, other):
        raise NotImplementedError()

    def __truediv__(self, other):
        raise NotImplementedError()

    def __repr__(self):
        return f"{self.a} (mod {self.p})"

    def __eq__(self, other):
        return self.a == other.a and self.p == other.p
