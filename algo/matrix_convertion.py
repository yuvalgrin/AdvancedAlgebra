# important note: the less significant bit in the implementation of the polynoms is the most right one
# e.g: [1,0,1,2] = x^3 + x + 2
# x^16+x^15/x^2+x+1 = x^14(-x-1) + x^15 = -x^15 -x^14 +x^15 = -x^14
from typing import List

import numpy as np
from numpy.linalg import inv
from numpy.linalg import det

from algo.polynom_ops import polynom_mul, modulu_polynom
from models.prime_field_element import PrimeFieldElement


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
