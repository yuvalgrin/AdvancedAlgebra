import unittest

from models.finite_field import FiniteField


class TestFiniteField(unittest.TestCase):
    def test_finite_field_initialization(self):
        # Test initialization with prime and irreducible polynomial
        finite_field = FiniteField(3, [2, 2, 1])
        self.assertEqual(finite_field.p, 3)
        self.assertEqual(finite_field.f, [2, 2, 1])

        # Test initialization with non-prime number
        with self.assertRaises(ValueError):
            FiniteField(4, [1, 1, 1])

    def test_finite_field_equality(self):
        finite_field1 = FiniteField(2, [1, 1, 1])
        finite_field2 = FiniteField(2, [1, 1, 1])
        finite_field3 = FiniteField(2, [1, 1, 0, 1])

        self.assertEqual(finite_field1, finite_field2)
        self.assertNotEqual(finite_field1, finite_field3)
