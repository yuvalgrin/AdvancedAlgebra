import unittest

from models.prime_field_element import PrimeFieldElement


class TestPrimeFieldElement(unittest.TestCase):
    def test_invalid_prime_init(self):
        with self.assertRaises(ValueError):
            PrimeFieldElement(1, 4)
        with self.assertRaises(ValueError):
            PrimeFieldElement(1, 28)
        PrimeFieldElement(1, 7)

    def test_addition(self):
        a = PrimeFieldElement(1, 5)
        b = PrimeFieldElement(2, 5)
        self.assertEqual(a + b, PrimeFieldElement(3, 5))

        a = PrimeFieldElement(6, 5)
        b = PrimeFieldElement(7, 5)
        self.assertEqual(a + b, PrimeFieldElement(3, 5))

    def test_subtraction(self):
        a = PrimeFieldElement(1, 5)
        b = PrimeFieldElement(2, 5)
        self.assertEqual(a - b, PrimeFieldElement(4, 5))

        a = PrimeFieldElement(6, 5)
        b = PrimeFieldElement(7, 5)
        self.assertEqual(a - b, PrimeFieldElement(4, 5))

    def test_multiplication(self):
        a = PrimeFieldElement(2, 5)
        b = PrimeFieldElement(3, 5)
        self.assertEqual(a * b, PrimeFieldElement(1, 5))

        a = PrimeFieldElement(7, 5)
        b = PrimeFieldElement(8, 5)
        self.assertEqual(a * b, PrimeFieldElement(1, 5))

    def test_division(self):
        a = PrimeFieldElement(2, 5)
        b = PrimeFieldElement(3, 5)
        self.assertEqual(a / b, PrimeFieldElement(4, 5))

        a = PrimeFieldElement(7, 5)
        b = PrimeFieldElement(8, 5)
        self.assertEqual(a / b, PrimeFieldElement(4, 5))

        a = PrimeFieldElement(17, 313)
        b = PrimeFieldElement(31, 313)
        self.assertEqual(a / b, PrimeFieldElement(152, 313))

    def test_pow(self):
        a = PrimeFieldElement(2, 5)
        self.assertEqual(a ** 2, PrimeFieldElement(4, 5))

        a = PrimeFieldElement(7, 5)
        self.assertEqual(a ** -1, PrimeFieldElement(3, 5))

        a = PrimeFieldElement(3, 313)
        self.assertEqual(a ** 3, PrimeFieldElement(27, 313))

    def test_division_with_no_inverse(self):
        a = PrimeFieldElement(2, 5)
        b = PrimeFieldElement(5, 5)
        with self.assertRaises(ValueError):
            a / b

    def test_division_with_different_prime(self):
        a = PrimeFieldElement(2, 5)
        b = PrimeFieldElement(5, 7)
        with self.assertRaises(ValueError):
            a / b

    def test_inversion_modulo(self):
        a = PrimeFieldElement(2, 5)
        b = PrimeFieldElement(4, 5)
        self.assertEqual(a / b, PrimeFieldElement(3, 5))
