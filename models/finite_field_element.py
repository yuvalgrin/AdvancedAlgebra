import numpy as np

from algo.matrix_convertion import create_matrix
from models.finite_field import FiniteField

from typing import List

from models.prime_field_element import PrimeFieldElement


class FiniteFieldElement:
    def __init__(self, finite_field: FiniteField, coeffs: List[int]):
        self.field = finite_field
        self.coeffs = [PrimeFieldElement(coeff, finite_field.p) for coeff in coeffs]

    def _validate_input(self, other):
        if self.field != other.field:
            raise ValueError(
                f"Cannot operate on elements from different finite fields: {self.field.p}!={other.field.p}"
            )

    def __add__(self, other):
        self._validate_input(other)
        new_coeffs = [a + b for a, b in zip(self.coeffs, other.coeffs)]
        return FiniteFieldElement(self.field, new_coeffs)

    def __sub__(self, other):
        self._validate_input(other)
        new_coeffs = [a - b for a, b in zip(self.coeffs, other.coeffs)]
        return FiniteFieldElement(self.field, new_coeffs)

    def __mul__(self, other):
        self._validate_input(other)

        # Compute the GLn matrix representations of self and other
        self_matrix = self.embed_in_GLn()
        other_matrix = other.embed_in_GLn()

        # Compute the product of the matrices
        product_matrix = self_matrix @ other_matrix

        # Convert the resulting matrix back to an element of the field
        product_coeffs = []
        for i in range(self.n):
            product_coeffs.append(product_matrix[i][0])
        return FiniteFieldElement(self.field, product_coeffs)

    def __truediv__(self, other):
        self._validate_input(other)
        if other.coeffs == [0]:
            raise ZeroDivisionError("Cannot divide by zero")

        # Compute the GLn matrix representations of self and other
        self_matrix = self.embed_in_GLn()
        other_matrix = other.embed_in_GLn()

        # Compute the inverse of the other matrix
        try:
            other_inverse_matrix = np.linalg.inv(other_matrix)
        except np.linalg.LinAlgError:
            raise ValueError("Cannot invert singular matrix")

        # Compute the product of the self matrix and the inverse of the other matrix
        quotient_matrix = self_matrix @ other_inverse_matrix

        # Convert the resulting matrix back to an element of the field
        quotient_coeffs = []
        for i in range(self.n):
            quotient_coeffs.append(quotient_matrix[i][0])
        return FiniteFieldElement(self.field, quotient_coeffs)

    def embed_in_GLn(self):
        return create_matrix(self.coeffs, self.field.f)

    def __str__(self):
        return " + ".join(f"{c}*x^{i}" for i, c in enumerate(self.coeffs))

    def __repr__(self):
        return f"FiniteFieldElement({repr(self.field)}, {repr(self.coeffs)})"

    def __eq__(self, other):
        return self.field == other.field and self.coeffs == other.coeffs
