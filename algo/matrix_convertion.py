# important note: the less significant bit in the implementation of the polynomials is the most right one
# e.g: [1,0,0,2] = x^3 + 2
from copy import deepcopy

import numpy as np
from numpy.linalg import inv
from numpy.linalg import det

from algo.polynom_utils import polynom_modulu, polynom_mul


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
    identity = np.identity(len(matrix))
    mat = deepcopy(matrix)
    while n != 0:
        if n % 2 == 1:
            identity = np.matmul(mat, identity)
        mat = np.matmul(mat, mat)
        n = n >> 1
    return identity


def inverse_matrix(matrix, p):
    inverse_mat = det(matrix) * inv(matrix)
    determinant = det(matrix)
    inverse_mat = [[x / determinant for x in y] for y in inverse_mat]
    return inverse_mat
