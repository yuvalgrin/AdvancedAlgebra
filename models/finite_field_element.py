import numpy as np

from models.finite_field import FiniteField

from typing import List, Union

from models.matrix_convertion import get_matrix, inverse_matrix, convert_matrix_to_coeffs, exp
from models.prime_field_element import PrimeFieldElement
from utils.constructor_utils import construct_coeffs


class FiniteFieldElement:
    def __init__(self, finite_field: FiniteField, coeffs: Union[List[int], List[PrimeFieldElement]]):
        self.field = finite_field
        self.coeffs = construct_coeffs(coeffs, finite_field.p)

    def __hash__(self):
        return hash((self.field, tuple(self.coeffs)))

    def __add__(self, other):
        if self.field != other.field:
            raise ValueError("Cannot add elements from different finite fields")
        new_coeffs = [a + b for a, b in zip(self.coeffs, other.coeffs)]
        return FiniteFieldElement(self.field, new_coeffs)

    def __sub__(self, other):
        if self.field != other.field:
            raise ValueError("Cannot subtract elements from different finite fields")
        new_coeffs = [a - b for a, b in zip(self.coeffs, other.coeffs)]
        return FiniteFieldElement(self.field, new_coeffs)

    def __mul__(self, other):
        if self.field != other.field:
            raise ValueError("Cannot multiply elements from different fields")

        self_matrix = self.embed_in_GLn()
        other_matrix = other.embed_in_GLn()
        product_matrix = self_matrix @ other_matrix

        return self.embed_GLn_to_vector(product_matrix)

    def __pow__(self, other):
        self_matrix = self.embed_in_GLn()
        p = self.field.p
        exp_matrix = exp(self_matrix, other, p)

        return self.embed_GLn_to_vector(exp_matrix)

    def __truediv__(self, other):
        if self.field != other.field:
            raise ValueError("Cannot divide elements from different fields")
        if other.coeffs == [0]:
            raise ZeroDivisionError("Cannot divide by zero")

        self_matrix = self.embed_in_GLn()
        self_matrix = [[PrimeFieldElement(x, self.field.p) for x in y] for y in self_matrix]
        other_matrix = other.embed_in_GLn()
        other_inverse_matrix = inverse_matrix(other_matrix, self.field.p)

        quotient_matrix = np.array(self_matrix) @ np.array(other_inverse_matrix)

        return self.embed_GLn_to_vector(quotient_matrix)

    def embed_in_GLn(self):
        return get_matrix(list(reversed(self._coeffs_ints())), list(reversed(self.field.f)))

    def embed_GLn_to_vector(self, matrix):
        return FiniteFieldElement(self.field, convert_matrix_to_coeffs(matrix))

    def get_multiplicative_order(self):
        e0 = self.get_e0_element(self.field)
        if e0 == self:
            raise Exception('You entered the zero element. Please enter a valid element')
        o = 1
        n = len(self.field.f) - 1
        p = self.field.p
        L = p ** n - 1
        FloorL = L // 2
        e1 = self.get_e1_element(self.field)
        a = self
        while o <= FloorL:
            if a == e1:
                return o
            else:
                o = o + 1
                a = a * self
        o = L
        return o

    def __str__(self):
        return " + ".join(f"{c}*x^{i}" for i, c in enumerate(self.coeffs))

    def __repr__(self):
        return f"FiniteFieldElement({repr(self.field)}, {repr(self.coeffs)})"

    def __eq__(self, other):
        return self.field == other.field and self.coeffs == other.coeffs

    def _coeffs_ints(self):
        return [coeff.a for coeff in self.coeffs]

