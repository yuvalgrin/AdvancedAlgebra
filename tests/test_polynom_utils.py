import unittest

from algo.polynom_utils import (
    polynom_mul,
    polynom_plus,
    polynom_minus,
    polynom_subtract,
    polynom_modulu,
)


class TestPolynomialUtils(unittest.TestCase):
    def test_poly_mul(self):
        mul = polynom_mul([-1, 4], [4, -6, 5])
        self.assertEqual(mul, [0])

    def test_poly_mod(self):
        modulu = polynom_modulu([1, 0, 2, 5], [1, 1, 3])
        self.assertEqual(modulu, [0])

    def test_poly_sub(self):
        subtract = polynom_subtract([7, 4, 3], [4, 7, -6, 3])
        self.assertEqual(subtract, [0])

    def test_poly_minus(self):
        minus = polynom_minus([4, 9, -6, 5])
        self.assertEqual(minus, [0])

    def test_poly_plus(self):
        plus = polynom_plus([7, 4, 3], [4, 9, -6, 5])
        self.assertEqual(plus, [0])
