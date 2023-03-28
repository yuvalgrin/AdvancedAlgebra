import math

from utils.prime_utils import is_prime


class PrimeFieldElement:
    def __init__(self, a, p):
        if not is_prime(p):
            raise ValueError(f"p ({p}) must be prime")
        self.a = a % p
        self.p = p

    def __add__(self, other):
        if self.p != other.p:
            raise ValueError("Cannot add elements from different fields")
        return PrimeFieldElement((self.a + other.a) % self.p, self.p)

    def __sub__(self, other):
        if self.p != other.p:
            raise ValueError("Cannot subtract elements from different fields")
        return PrimeFieldElement((self.a - other.a) % self.p, self.p)

    def __mul__(self, other):
        if self.p != other.p:
            raise ValueError("Cannot multiply elements from different fields")
        return PrimeFieldElement((self.a * other.a) % self.p, self.p)

    def __truediv__(self, other):
        if self.p != other.p:
            raise ValueError("Cannot divide elements from different fields")
        if math.gcd(other.a, self.p) != 1:
            raise ValueError("Cannot divide by elements without an inverse")
        return self * PrimeFieldElement(pow(other.a, -1, self.p), self.p)

    def __repr__(self):
        return f"{self.a} (mod {self.p})"

    def __eq__(self, other):
        return self.a == other.a and self.p == other.p
