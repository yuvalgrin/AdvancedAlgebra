import unittest

import numpy as np
from models.matrix_convertion import get_matrix, exp, inverse_matrix


class TestMatrixConversion(unittest.TestCase):
    def test_matrix_creation(self):
        x = get_matrix([1,1],[1,0,1])
        self.assertTrue(np.array_equal(x, [[1,-1],[1,1]]))

        w = get_matrix([0,1,0],[1,1,0,1])
        z = get_matrix([1, 0, 0], [1, 1, 0, 1])
        self.assertTrue(np.array_equal(np.matmul(w,w), z))

    def test_exponent_positive(self):
        w = get_matrix([0,1,0],[1,1,0,1])
        z = get_matrix([1, 0, 0], [1, 1, 0, 1])
        self.assertTrue(np.array_equal(exp(w, 2, 61), z))

    def test_exponent_negative(self):
        w = get_matrix([0,1,0],[4,0,6,1])
        exponent_pos = exp(w, 1, 7)
        inv_w = inverse_matrix(w, 7)
        #print(inv_w)
        exponent_neg = exp(w, -1, 7)
        mult = np.matmul(inv_w, exponent_pos)
        #print(mult)
        self.assertTrue(np.array_equal(mult, w))

    def test_inverse_matrix(self):
        w = get_matrix([0, 3, 1], [1, 1, 0, 1])
        p = 7
        inv_w = inverse_matrix(w, p)
        inv_w_int = _cast_prime_field_matrix_to_positive_int(inv_w)
        print(w)
        print(inv_w_int)
        print(np.matmul(w,inv_w_int))
        double_inv_w = inverse_matrix(inv_w_int, p)
        double_inv_w_int = _cast_prime_field_matrix_to_positive_int(double_inv_w)
        self.assertTrue(np.array_equal(double_inv_w_int, _cast_int_matrix_to_positive_int(w, p)))


def _cast_int_matrix_to_positive_int(matrix, p):
    return np.array([[val if val >= 0 else val + p for val in arr] for arr in matrix])


def _cast_prime_field_matrix_to_positive_int(matrix):
    return np.array([[val.a if val.a >= 0 else val.a + val.p for val in arr] for arr in matrix])

# x = get_matrix([1,2,2],[1,1,0,1])
# z = get_matrix([0,1,0],[1,1,0,1])
# w = get_matrix([1,0,0],[1,1,0,1])
# print("z:\n",z)
# print("w:\n",w)
# print("z*z:\n",np.matmul(z,z))
# #print(x)
# #print(int(det(x)*1.01))
# y = get_matrix([4,1],[1,0,1])
# #print(x)
# #print(y)
# #print(x*y)
# #print(exp(x.astype(int),13))
# #print((det(x)*inv(x)))
# print(np.matmul(inverse_matrix(x,5),[[prime_field_element.PrimeFieldElement(a,5) for a in b]for b in x]))
