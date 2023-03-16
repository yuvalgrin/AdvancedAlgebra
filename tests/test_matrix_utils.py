import unittest

from algo.matrix_convertion import create_matrix, exponent, inverse_matrix


class TestMatrixConversion(unittest.TestCase):
    def test_matrix_creation(self):
        matrix1 = create_matrix([2, 3], [1, 0, 1])
        matrix2 = create_matrix([4, 1], [1, 0, 1])
        self.assertEqual(matrix1, [0])
        self.assertEqual(matrix2, [0])

    def test_exponent(self):
        matrix = create_matrix([2, 3], [1, 0, 1])
        self.assertEqual(exponent(matrix.astype(int), 13), [0])

    def test_inverse_matrix(self):
        matrix = create_matrix([2, 3], [1, 0, 1])
        inverse = inverse_matrix(matrix, 5)
        self.assertEqual(inverse, [0])
