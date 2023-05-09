import unittest

import numpy as np

from models.finite_field import FiniteField
from models.finite_field_element import FiniteFieldElement, get_e0_element, get_e1_element


class TestFiniteFieldElement(unittest.TestCase):
    def setUp(self):
        self.finite_field = FiniteField(5, [3, 3, 0, 1])

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
        self.assertEqual(z.coeffs, self._create_field([0, 4, 2]).coeffs)

    def test_division(self):
        x = FiniteFieldElement(self.finite_field, [1, 2, 3])
        y = FiniteFieldElement(self.finite_field, [4, 3, 2])
        z = x / y
        self.assertEqual(z.coeffs, self._create_field([4, 0, 0]).coeffs)

    def test_str(self):
        x = FiniteFieldElement(self.finite_field, [1, 2, 3])
        self.assertEqual(str(x), "1 (mod 5)*x^0 + 2 (mod 5)*x^1 + 3 (mod 5)*x^2")

    def test_repr(self):
        x = FiniteFieldElement(self.finite_field, [1, 2, 3])
        self.assertEqual(
            repr(x), "FiniteFieldElement(FiniteField(5, [3, 3, 0, 1]), [1 (mod 5), 2 (mod 5), 3 (mod 5)])"
        )

    def test_equality(self):
        x = FiniteFieldElement(self.finite_field, [1, 2, 3])
        y = FiniteFieldElement(self.finite_field, [1, 2, 3])
        z = FiniteFieldElement(self.finite_field, [3, 2, 1])
        self.assertEqual(x, y)
        self.assertNotEqual(x, z)

    def test_invalid_operations(self):
        x = FiniteFieldElement(self.finite_field, [1, 2])
        y = FiniteFieldElement(FiniteField(7, [3, 6, 1]), [1, 2])
        with self.assertRaises(ValueError):
            x + y
            x - y
            x * y
            x / y

    def test_embed_in_GLn(self):
        element = FiniteFieldElement(self.finite_field, [1, 2])
        matrix = element.embed_in_GLn()
        expected = np.array([[1, -6, -6], [2, 1, 0], [0, 2, 1]])
        self.assertTrue(np.array_equal(matrix, expected))

    def test_multiplicative_order(self):
        field = FiniteField(3, [1, 0, 1])
        with self.assertRaises(Exception):
            e0 = get_e0_element(field)
            e0.get_multiplicative_order()
        e1 = get_e1_element(field)
        e1_order = e1.get_multiplicative_order()
        self.assertEqual(e1_order, 1)

    def test_multiplicative_order_2(self):
        field = FiniteField(7, [3, 6, 1])
        element = FiniteFieldElement(field, [0, 1])
        element_order = element.get_multiplicative_order()
        self.assertEqual(element_order, 48)
        element = FiniteFieldElement(field, [4, 5])
        element_order = element.get_multiplicative_order()
        self.assertEqual(element_order, 16)

    def test_exp_equal_multiply(self):
        field = FiniteField(7, [3, 6, 1])
        element = FiniteFieldElement(field, [1, 3])
        mult_sqr = element ** 1
        self.assertEqual(element, mult_sqr)

        mult_with_self = element * element
        mult_sqr = element ** 2
        self.assertEqual(mult_with_self, mult_sqr)

        mult_with_self = element * element * element
        mult_sqr = element ** 3
        self.assertEqual(mult_with_self, mult_sqr)

        mult_with_self = element * element * element * element * element * \
                         element * element * element * element * element * \
                         element * element * element * element * element * \
                         element * element * element * element * element
        mult_sqr = element ** 20
        self.assertEqual(mult_with_self, mult_sqr)



class TestElementExponent(unittest.TestCase):
    def test_exponent_positive(self):
        field = FiniteField(61, [1, 0, 1, 1])
        element1 = FiniteFieldElement(field, [0, 1, 0])
        element2 = FiniteFieldElement(field, [0, 0, 1])
        self.assertEqual(element1 ** 2, element2)

    def test_exponent_zero(self):
        field = FiniteField(61, [1, 0, 1, 1])
        element1 = FiniteFieldElement(field, [0, 1, 0])
        element2 = FiniteFieldElement(field, [1, 0, 0])
        self.assertEqual(element1 ** 0, element2)

    def test_exponent_negative_p2(self):
        field = FiniteField(2, [1, 1, 1])
        element = FiniteFieldElement(field, [1, 1])
        exponent_pos = element ** 1
        exponent_neg = element ** -1
        mult = exponent_neg * exponent_pos
        expected = FiniteFieldElement(field, [1, 0])
        self.assertEqual(mult, expected)

    def test_exponent_negative_p7(self):
        field = FiniteField(7, [3, 6, 1])
        element = FiniteFieldElement(field, [2, 5])
        exponent_pos = element ** 1
        exponent_neg = element ** -1
        mult = exponent_neg * exponent_pos
        expected = FiniteFieldElement(field, [-6, -7])
        self.assertEqual(mult, expected)

    def test_exp_7(self):
        field = FiniteField(7, [3, 6, 1])
        element = FiniteFieldElement(field, [3, 5])
        exponent_pos = element ** 2
        exponent_neg = element ** -2
        mult = exponent_neg * exponent_pos
        expected = FiniteFieldElement(field, [344, 518])
        self.assertEqual(mult, expected)

    def test_power(self):
        field = FiniteField(7, [3, 6, 1])
        x = FiniteFieldElement(field, [1, 3])
        t = 48
        z = x ** t
        check_element = FiniteFieldElement(field, [1, 0])
        self.assertEqual(check_element, z)
