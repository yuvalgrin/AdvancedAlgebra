import unittest

import numpy as np

from models.finite_field import FiniteField
from models.finite_field_element import FiniteFieldElement


class TestFiniteFieldElement(unittest.TestCase):
    def setUp(self):
        self.finite_field = FiniteField(5, [2, 1, 0, 1])

    def _create_field(self, coeffs):
        return FiniteFieldElement(self.finite_field, coeffs)

    def test_addition(self):
        x = FiniteFieldElement(self.finite_field, [1, 2, 3])
        y = FiniteFieldElement(self.finite_field, [4, 3, 2])
        z = x + y
        self.assertEqual(z.coeffs, self._create_field([0, 0, 0]).coeffs)

    def test_subtraction(self):
        x = FiniteFieldElement(self.finite_field, [1, 2, 3])
        y = FiniteFieldElement(self.finite_field, [4, 3, 2])
        z = x - y
        self.assertEqual(z.coeffs, self._create_field([2, 4, 1]).coeffs)

    def test_multiplication(self):
        x = FiniteFieldElement(self.finite_field, [1, 2, 3])
        y = FiniteFieldElement(self.finite_field, [4, 3, 2])
        z = x * y
        self.assertEqual(z.coeffs, self._create_field([4, 1, 4]).coeffs)

    def test_division(self):
        x = FiniteFieldElement(self.finite_field, [1, 2, 3])
        y = FiniteFieldElement(self.finite_field, [4, 3, 2])
        z = x / y
        self.assertEqual(z.coeffs, self._create_field([0, 0, 0]).coeffs)

    def test_str(self):
        x = FiniteFieldElement(self.finite_field, [1, 2, 3])
        self.assertEqual(str(x), "1 (mod 5)*x^0 + 2 (mod 5)*x^1 + 3 (mod 5)*x^2")

    def test_repr(self):
        x = FiniteFieldElement(self.finite_field, [1, 2, 3])
        self.assertEqual(
            repr(x), "FiniteFieldElement(FiniteField(5, [2, 1, 0, 1]), [1 (mod 5), 2 (mod 5), 3 (mod 5)])"
        )

    def test_equality(self):
        x = FiniteFieldElement(self.finite_field, [1, 2, 3])
        y = FiniteFieldElement(self.finite_field, [1, 2, 3])
        z = FiniteFieldElement(self.finite_field, [3, 2, 1])
        self.assertEqual(x, y)
        self.assertNotEqual(x, z)

    def test_invalid_operations(self):
        x = FiniteFieldElement(self.finite_field, [1, 2, 3])
        y = FiniteFieldElement(FiniteField(7, [1, 1, 1]), [1, 2, 3])
        with self.assertRaises(ValueError):
            x + y
            x - y
            x * y
            x / y

    def test_embed_in_GLn(self):
        # Test embedding of element [1, 2] in GF(5^2)
        field = FiniteField(5, [1, 2])
        element = FiniteFieldElement(field, [1, 2])
        matrix = element.embed_in_GLn()
        expected = np.array([[1, 1], [2, 0]])
        self.assertTrue(np.array_equal(matrix, expected))

        # Test embedding of element [2, 1, 3] in GF(7^3)
        field = FiniteField(7, 3)
        element = FiniteFieldElement(field, [2, 1, 3])
        matrix = element.embed_in_GLn()
        expected = np.array([[2, 2, 0], [1, 6, 1], [3, 1, 0]])
        self.assertTrue(np.array_equal(matrix, expected))

        # Test embedding of zero element in GF(2^2)
        field = FiniteField(2, 2)
        element = FiniteFieldElement(field, [0, 0])
        with self.assertRaises(ValueError):
            element.embed_in_GLn()
