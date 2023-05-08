import unittest

from models.finite_field import FiniteField
from models.finite_field_element import FiniteFieldElement, get_e0_element, get_e1_element
from algo.generator_creation import finite_field_element_generator, create_set_of_finite_field_elements


class TestFiniteFieldUtils(unittest.TestCase):
    def test_generate_set_of_finite_field_elements(self):
        my_field = FiniteField(3, [1, 0, 1])
        set_of_elements = create_set_of_finite_field_elements(my_field)
        polyorder = my_field.polyorder
        self.assertEqual(len(set_of_elements), my_field.p ** polyorder)

    def test_generate_e0(self):
        my_field = FiniteField(3, [1, 0, 1])
        e0 = get_e0_element(my_field)
        self.assertEqual(e0, FiniteFieldElement(my_field, [0, 0]))

    def test_generate_e1(self):
        my_field = FiniteField(3, [1, 0, 1])
        e1 = get_e1_element(my_field)
        self.assertEqual(e1, FiniteFieldElement(my_field, [1, 0]))

    def test_finite_field_element_generator(self):
        my_field = FiniteField(3, [1, 0, 1])
        gen = finite_field_element_generator(my_field)
        self.assertEqual(gen, FiniteFieldElement(my_field, [1, 2]))

    def test_finite_field_element_generator2(self):
        finite_field = FiniteField(7, [3, 6, 1])
        gen = finite_field_element_generator(finite_field)
        prime = finite_field.p
        extenstion_order = len(finite_field.f) - 1
        group_order = (prime ** (extenstion_order))-1
        self.assertEqual(gen.get_multiplicative_order(), group_order)