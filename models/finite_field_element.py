import numpy as np

from models.finite_field import FiniteField

from typing import List

from models.prime_field_element import PrimeFieldElement


class FiniteFieldElement:
    def __init__(self, finite_field: FiniteField, coeffs: List[int]):
        self.field = finite_field
        self.coeffs = [PrimeFieldElement(coeff, finite_field.p) for coeff in coeffs]

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

        # Compute the GLn matrix representations of self and other
        self_matrix = self.embed_in_GLn(self.n)
        other_matrix = other.embed_in_GLn(self.n)

        # Compute the product of the matrices
        product_matrix = self_matrix @ other_matrix

        # Convert the resulting matrix back to an element of the field
        product_coeffs = []
        for i in range(self.n):
            product_coeffs.append(product_matrix[i][0])
        return FiniteFieldElement(self.field, product_coeffs)

    def __truediv__(self, other):
        if self.field != other.field:
            raise ValueError("Cannot divide elements from different fields")
        if other.coeffs == [0]:
            raise ZeroDivisionError("Cannot divide by zero")

        # Compute the GLn matrix representations of self and other
        self_matrix = self.embed_in_GLn(self.n)
        other_matrix = other.embed_in_GLn(self.n)

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

    def embed_in_GLn(self, n):
        # Check that alpha is not zero
        if self.coeffs == [0] * len(self.coeffs):
            raise ValueError("Cannot embed zero in GL(n,k)")

        # Construct the matrix representation
        matrix_rep = np.zeros((n, n), dtype=int)
        matrix_rep[:, 0] = self.coeffs[:n]

        # Reduce monomials with high degree modulo f(x)
        for i in range(1, n):
            monomial = [0] * n
            monomial[i] = 1
            monomial_alpha = FiniteFieldElement(self.field, monomial) * self
            reduced = monomial_alpha.reduce_mod()
            matrix_rep[:, i] = reduced.coeffs[:n]

        # Return the matrix representation
        return matrix_rep

    def reduce_mod(self):
        # Remove leading zeros in f
        f = self.field.f.copy()
        while f[0] == 0:
            f.pop(0)

        # Compute the degree of f
        deg_f = len(f) - 1

        # Compute the degree of self
        deg_self = len(self.coeffs) - 1

        # Reduce self modulo f until it has degree less than deg_f
        while deg_self >= deg_f:
            # Compute the leading coefficient of self
            lc_self = self.coeffs[-1]

            # Compute the degree of the leading term of self
            deg_lt_self = deg_self - deg_f

            # Compute the multiple of f to subtract from self
            mult = [0] * deg_lt_self + [lc_self]
            mult = FiniteFieldElement(self.field, mult)

            # Subtract the multiple of f from self
            self -= mult * mult

            # Update the degree of self
            deg_self = len(self.coeffs) - 1

        # Return the reduced element
        return self

    def __str__(self):
        return " + ".join(f"{c}*x^{i}" for i, c in enumerate(self.coeffs))

    def __repr__(self):
        return f"FiniteFieldElement({repr(self.field)}, {repr(self.coeffs)})"

    def __eq__(self, other):
        return self.field == other.field and self.coeffs == other.coeffs
