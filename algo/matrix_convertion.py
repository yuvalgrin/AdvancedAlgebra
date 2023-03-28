# important note: the less significant bit in the implementation of the polynomials is the most right one
# e.g: [1,0,0,2] = x^3 + 2
from copy import deepcopy

import numpy as np
from numpy.linalg import inv
from numpy.linalg import det

from algo.polynom_utils import polynom_modulu, polynom_mul
from models.prime_field_element import PrimeFieldElement


def create_matrix(polynom, reduction_polynom):
    unity_matrix = [
        [1 if idx2 == idx1 else 0 for idx2 in range(len(reduction_polynom) - 1)]
        for idx1 in range(len(reduction_polynom) - 1)
    ]
    almost_there = [
        polynom_modulu(polynom_mul(I, polynom), reduction_polynom) for I in unity_matrix
    ]
    return np.int_(almost_there)


def exponent(matrix, n):
    value = np.identity(len(matrix))
    mat = deepcopy(matrix)
    while n != 0:
        if n % 2 == 1:
            value = np.matmul(mat, value)
        mat = np.matmul(mat, mat)
        n = n >> 1
    return value


def inverse_matrix(matrix, p):
    inverse = ((det(matrix)*inv(matrix))*1.01).astype(int)
    d_inv = PrimeFieldElement(1, p) / PrimeFieldElement(det(matrix.astype(int)*1.01).astype(int), p)
    inverse = [[PrimeFieldElement(x, p) * d_inv for x in y] for y in inverse]
    return inverse
