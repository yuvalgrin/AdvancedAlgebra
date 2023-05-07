# important note: the less significant bit in the implementation of the polynoms is the most right one
# e.g: [1,0,1,2] = x^3 + x + 2
# x^16+x^15/x^2+x+1 = x^14(-x-1) + x^15 = -x^15 -x^14 +x^15 = -x^14
from typing import List

import numpy as np
from numpy.linalg import inv
from numpy.linalg import det

from models.prime_field_element import PrimeFieldElement


def polynom_mul(pol1: List[int], pol2: List[int]):
    """Multiply two polynoms element by element"""
    new_pol = [0 for _ in range(len(pol1) + len(pol2) - 1)]
    for idx1, i1 in enumerate(pol1):
        for idx2, i2 in enumerate(pol2):
            new_pol[idx1 + idx2] += int(i1) * int(i2)
    return new_pol


def polynom_plus(pol1: List[int], pol2: List[int]):
    """Add two polynoms element by element"""
    new_pol = [0 for _ in range(max(len(pol1), len(pol2)))]
    for idx, i in enumerate(pol2[-1::-1]):
        new_pol[-(idx + 1)] += i
    for idx, i in enumerate(pol1[-1::-1]):
        new_pol[-(idx + 1)] += i
    return new_pol


def polynom_minus(pol: List[int]):
    """Multiply a polynom by -1"""
    return [-x for x in pol]


def polynom_subtract(pol1: List[int], pol2: List[int]):
    """Subtraction of two polynoms (uses the addition and minus operations)"""
    return polynom_plus(pol1, polynom_minus(pol2))


def modulu_polynom(input_polynom: List[int], reduction_polynom: List[int]):
    """Modulu a polynom with a reduction polynom.
    If the rank(polynom) > rank(reduction polynom):
        # example rank(x^3 + x) > rank(x^2 + 2)
        Reduce every x^n | n>r, where r = rank(reduction polynom), by representing it as x^r * x^(n-r).
        * This is helps us because we know how to reduce x^r.
        Finally, we get somthing like x^(n-r) * (-a_r*x^(r-1)-...- a_1*x -a_0)

    * Reduce x^r: reduction polynom = 0(modulo reduction polynom) = x^r + a_r * x^(r-1) + ... + a_1 * x^0
    Thus, x^r = - (a_r * x^(r-1) + ... + a_1 * x^0) (modulo reduction polynom)
    """
    while len(input_polynom) >= len(reduction_polynom):
        reduction_amplifier = [
            input_polynom[0] if idx == 0 else 0
            for idx, _ in enumerate(
                range(1 + len(input_polynom) - len(reduction_polynom))
            )
        ]
        amplifier_mult = polynom_mul(reduction_amplifier, reduction_polynom[1:])
        input_polynom = polynom_subtract(input_polynom, amplifier_mult)
        input_polynom = input_polynom[1:]
    return input_polynom


def create_matrix(polynom: List[int], reduction_polynom: List[int]):
    """Multiply the basis of l that's represented by the unity matrix, with the polynom
    we are trying to represent. Then reduce monomials with high degree using modulu_polynom method"""
    unity_matrix = np.identity(len(reduction_polynom) - 1)
    polynom_dot_unity = [polynom_mul(unity_row, polynom) for unity_row in unity_matrix]
    dot_unity_mod_reduction = [modulu_polynom(row, reduction_polynom) for row in polynom_dot_unity]
    return np.int_(dot_unity_mod_reduction)


def exp(matrix: List[List[int]], n: int, p: int):
    """Raise by an exponent of n in the prime field p.
    Multiply the identity with the matrix n times, convert the negative elements back to positive in the prime field.
    """
    ret = np.identity(len(matrix))
    mat = matrix.copy()
    if n < 0:
        mat = inverse_matrix(mat, p)
        mat = np.array([[int(PrimeFieldElement(val.a, val.p)) for val in arr] for arr in mat])
        n *= -1
    while n != 0:
        if n % 2 == 1:
            ret = np.matmul(mat, ret)
        mat = np.matmul(mat, mat)
        n = n >> 1
    return ret


def inverse_matrix(mat: List[List[int]], p: int):
    """Use numpy inverse matrix method, and multiply by the determinant in order to get the adj matrix.
    Divide again by the determinant but with our division inside the prime field."""
    inverse = (np.round(det(mat) * inv(mat)).astype(int))
    d_inv = PrimeFieldElement(1, p) / PrimeFieldElement(
        np.round(det(mat.astype(int))).astype(int), p
    )
    inverse = [[PrimeFieldElement(x, p) * d_inv for x in y] for y in inverse]
    return inverse


def convert_matrix_to_coeffs(mat: List[List[int]]):
    """Get the relevant line that represents the coefficients"""
    return list(reversed([int(val) for val in mat[-1]]))
