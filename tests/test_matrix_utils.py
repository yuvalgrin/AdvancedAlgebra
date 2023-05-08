import unittest
from dataclasses import Field

import numpy as np
from algo.matrix_convertion import create_matrix, inverse_matrix
from models.finite_field import FiniteField
from models.finite_field_element import FiniteFieldElement


class TestMatrixConversion(unittest.TestCase):
    def test_matrix_creation(self):
        x = create_matrix([1, 1], [1, 0, 1])
        self.assertTrue(np.array_equal(x, [[1,-1],[1,1]]))

        w = create_matrix([0, 1, 0], [1, 1, 0, 1])
        z = create_matrix([1, 0, 0], [1, 1, 0, 1])
        self.assertTrue(np.array_equal(np.matmul(w,w), z))

    def test_inverse_matrix(self):
        w = create_matrix([0, 1, 0], [1, 1, 0, 1])
        p = 5
        inv_w = inverse_matrix(w, p)
        inv_w_int = _cast_prime_field_matrix_to_positive_int(inv_w)
        double_inv_w = inverse_matrix(inv_w_int, p)
        double_inv_w_int = _cast_prime_field_matrix_to_positive_int(double_inv_w)
        self.assertTrue(np.array_equal(double_inv_w_int, _cast_int_matrix_to_positive_int(w, p)))


def _cast_int_matrix_to_positive_int(matrix, p):
    return np.array([[val if val >= 0 else val + p for val in arr] for arr in matrix])


def _cast_prime_field_matrix_to_positive_int(matrix):
    return np.array([[val.a if val.a >= 0 else val.a + val.p for val in arr] for arr in matrix])
