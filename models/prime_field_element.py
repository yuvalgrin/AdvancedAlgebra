from copy import deepcopy
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
        return PrimeFieldElement(self.a + other.a, self.p)

    def __sub__(self, other):
        if self.p != other.p:
            raise ValueError("Cannot subtract elements from different fields")
        return PrimeFieldElement(self.a - other.a, self.p)

    def __mul__(self, other):
        if self.p != other.p:
            raise ValueError("Cannot multiply elements from different fields")
        return PrimeFieldElement(self.a * other.a, self.p)

    def __truediv__(self, other):
        """Using python's implementation of Extended Euclides algorithm to do division"""
        if self.p != other.p:
            raise ValueError("Cannot divide elements from different fields")
        if math.gcd(other.a, self.p) != 1:
            raise ValueError("Cannot divide by elements without an inverse")
        extended_euclides_inverse = pow(int(other), -1, int(self.p))
        return self * PrimeFieldElement(extended_euclides_inverse, self.p)

    def __pow__(self, n):
        """Raise by an exponent of n in the prime field p by using the existing multiplication logic"""
        prime_element = deepcopy(self)
        if prime_element == PrimeFieldElement(0, prime_element.p):
            raise ValueError("prime element must be in the multiplicative group")
        result_element = PrimeFieldElement(1, prime_element.p)
        if prime_element == result_element: return prime_element
        if n < 0:
            prime_element = result_element / prime_element
            n *= -1
        while n != 0:
            if n % 2 == 1:
                result_element = prime_element * result_element
            prime_element = prime_element * prime_element
            n = n >> 1
        return result_element

    def __repr__(self):
        return f"{self.a} (mod {self.p})"

    def __eq__(self, other):
        return self.a == other.a and self.p == other.p

    def __int__(self):
        return int(self.a)

    def __hash__(self):
        return hash((self.a, self.p))
