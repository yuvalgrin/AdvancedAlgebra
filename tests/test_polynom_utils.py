import unittest

from algo.polynom_ops import (
    polynom_mul,
    polynom_plus,
    polynom_minus,
    polynom_subtract,
    modulu_polynom,
)


class TestPolynomialUtils(unittest.TestCase):
    def test_poly_mul(self):
        mul = polynom_mul([-1, 4], [4, -6, 5])
        self.assertEqual(mul, [-4, 22, -29, 20])

    def test_poly_mod(self):
        modulu = modulu_polynom([1, 0, 2, 5], [1, 1, 3])
        self.assertEqual(modulu, [0, 8])

    def test_poly_sub(self):
        subtract = polynom_subtract([7, 4, 3], [4, 7, -6, 3])
        self.assertEqual(subtract, [-4, 0, 10, 0])

    def test_poly_minus(self):
        minus = polynom_minus([4, 9, -6, 5])
        self.assertEqual(minus, [-4, -9, 6, -5])

    def test_poly_plus(self):
        plus = polynom_plus([7, 4, 3], [4, 9, -6, 5])
        self.assertEqual(plus, [4, 16, -2, 8])
