from copy import deepcopy

import numpy as np

from models.finite_field import FiniteField

from typing import List, Union

from algo.matrix_convertion import create_matrix, inverse_matrix, convert_matrix_to_coeffs
from models.prime_field_element import PrimeFieldElement
from utils.constructor_utils import construct_coeffs


class FiniteFieldElement:
    def __init__(self, finite_field: FiniteField, coeffs: Union[List[int], List[PrimeFieldElement]], gln_matrix=None):
        self.field = finite_field
        self.coeffs = construct_coeffs(coeffs, finite_field.p)
        if self.field.polyorder <= len(coeffs) - 1:
            raise ValueError(f"The order of the irreducible polynom {self.field.polyorder} has to be smaller than the order of the element polynom {len(coeffs) - 1}")
        self.gln_matrix = gln_matrix

    def embed_in_GLn(self):
        if self.gln_matrix is None:
            self.gln_matrix = create_matrix(self._coeffs_ints(), self.field.f)
        return self.gln_matrix

    def embed_GLn_to_vector(self, matrix):
        return FiniteFieldElement(self.field, convert_matrix_to_coeffs(matrix))

    def get_multiplicative_order(self):
        """Calculate the multiplicative order by multiplying the element with itself,
        until we get to the e1 element or the middle of group to save calculation time.
        (The order of the element must divide the order of the group)."""
        e0 = get_e0_element(self.field)
        if e0 == self:
            raise Exception(f"Cannot find multiplicate order of the zero element {self}")
        o = 1
        field_order = self.field.p ** self.field.polyorder - 1
        floor_field_order = field_order // 2
        e1 = get_e1_element(self.field)

        element = deepcopy(self)
        while o <= floor_field_order:
            if element == e1:  # Next multiplication we'll to (self)
                return o
            else:
                o += 1
                element *= self

        o = field_order
        return o

    def _coeffs_ints(self):
        return [int(coeff) for coeff in self.coeffs]

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

    def __pow__(self, n):
        """Raise by an exponent of n in the prime field p by using the existing multiplication logic"""
        result_element = get_e1_element(self.field)
        element = deepcopy(self)
        if n < 0:
            element = result_element / element
            n *= -1
        while n != 0:
            if n % 2 == 1:
                result_element = element * result_element
            element = element * element
            n = n >> 1
        return result_element

    def __truediv__(self, other):
        if self.field != other.field:
            raise ValueError("Cannot divide elements from different fields")
        if all(int(coeff) == 0 for coeff in other.coeffs):
            raise ZeroDivisionError("Cannot divide by zero")

        self_matrix = self.embed_in_GLn()
        self_matrix = [[PrimeFieldElement(x, self.field.p) for x in y] for y in self_matrix]
        other_matrix = other.embed_in_GLn()
        other_inverse_matrix = inverse_matrix(other_matrix, self.field.p)

        quotient_matrix = np.array(self_matrix) @ np.array(other_inverse_matrix)

        return self.embed_GLn_to_vector(quotient_matrix)

    def __str__(self):
        return " + ".join(f"{c}*x^{i}" for i, c in enumerate(self.coeffs))

    def __repr__(self):
        return f"FiniteFieldElement({repr(self.field)}, {repr(self.coeffs)})"

    def __eq__(self, other):
        return self.field == other.field and self.coeffs == other.coeffs

    def __hash__(self):
        return hash((self.field, tuple(self.coeffs)))


def get_e0_element(field: FiniteField):
    poly_list = [0] * field.polyorder
    result = FiniteFieldElement(field, poly_list)
    return result


def get_e1_element(field: FiniteField):
    poly_list = [1] + [0] * (field.polyorder - 1)
    result = FiniteFieldElement(field, poly_list)
    return result
