import unittest

from models.finite_field import FiniteField
from models.finite_field_element import FiniteFieldElement
from models.finite_field_utils import create_set_of_finite_field_elements, get_e0_element, get_e1_element


class TestFiniteFieldUtils(unittest.TestCase):
    def test_generate_set_of_finite_field_elements(self):
        my_field = FiniteField(3, [1, 0, 1])
        set_of_elements = create_set_of_finite_field_elements(my_field)
        polyorder = len(my_field.f) - 1
        self.assertEqual(len(set_of_elements), my_field.p ** polyorder)

    def test_generate_e0(self):
        my_field = FiniteField(3, [1, 0, 1])
        e0 = get_e0_element(my_field)
        self.assertEqual(e0, FiniteFieldElement(my_field, [0, 0]))

    def test_generate_e1(self):
        my_field = FiniteField(3, [1, 0, 1])
        e1 = get_e1_element(my_field)
        self.assertEqual(e1, FiniteFieldElement(my_field, [1, 0]))
