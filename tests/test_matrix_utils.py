import unittest

from algo.matrix_convertion import create_matrix, exponent, inverse_matrix
from models.matrix_convertion import get_matrix


class TestMatrixConversion(unittest.TestCase):
    def test_matrix_creation(self):
        matrix1 = create_matrix([2, 3], [1, 0, 1])
        matrix2 = create_matrix([4, 1], [1, 0, 1])
        matrix3 = create_matrix([1, 2, 2], [1, 1, 0, 1])
        matrix3 = get_matrix([1, 2, 2], [1, 1, 0, 1])
        self.assertEqual(matrix1, [0])
        self.assertEqual(matrix2, [0])
        self.assertEqual(matrix3, [0])

    def test_exponent(self):
        matrix = create_matrix([2, 3], [1, 0, 1])
        self.assertEqual(exponent(matrix.astype(int), 13), [0])

    def test_inverse_matrix(self):
        matrix = create_matrix([2, 3], [1, 0, 1])
        inverse = inverse_matrix(matrix, 5)
        self.assertEqual(inverse, [0])


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
