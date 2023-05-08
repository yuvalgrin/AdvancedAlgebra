import unittest

from algo.BSGS import get_power_list, BSGS
from models.finite_field import FiniteField
from models.finite_field_element import get_e1_element, FiniteFieldElement
from algo.generator_creation import finite_field_element_generator


class TestFiniteField(unittest.TestCase):
    def test_get_power_list(self):
        finite_field = FiniteField(3, [2, 2, 1])
        e1 = get_e1_element(finite_field)
        power_list = get_power_list(e1, 2)
        self.assertEqual(power_list, {e1: 2})

    def test_bsgs(self):
        finite_field = FiniteField(7, [3, 6, 1])
        gen = finite_field_element_generator(finite_field)
        exp_element = FiniteFieldElement(finite_field, [1, 3])
        self.assertEqual(exp_element.get_multiplicative_order(), 48)
        self.assertEqual(gen, exp_element)

        check_element = FiniteFieldElement(finite_field, [1, 1])
        bsgs = BSGS(gen, check_element)
        self.assertEqual(bsgs, 23)

    def test_bsgs_2(self):
        finite_field = FiniteField(7, [3, 6, 1])
        gen = FiniteFieldElement(finite_field, [0, 1])
        check_element = FiniteFieldElement(finite_field, [0, 4])
        bsgs = BSGS(gen, check_element)
        self.assertEqual(bsgs, 33)

    def test_bsgs_3(self):
        finite_field = FiniteField(7, [3, 6, 1])
        gen = finite_field_element_generator(finite_field)
        t = 40 % finite_field.p
        exp_element = gen ** t
        bsgs = BSGS(gen, exp_element)
        self.assertEqual(t, bsgs)

        prime = finite_field.p
        extenstion_order = len(finite_field.f) - 1
        group_order = (prime ** (extenstion_order))-1
        self.assertEqual(gen.get_multiplicative_order(), group_order)

    def test_bsgs_4(self):
        finite_field = FiniteField(383, [378, 1, 0, 1])
        gen = FiniteFieldElement(finite_field, [0, 1,0])
        check_element = FiniteFieldElement(finite_field, [229, 349, 291])
        bsgs = BSGS(gen, check_element)
        self.assertEqual(200000,bsgs)

    # def test_bsgs5(self):
    #     finite_field = FiniteField(7, [3, 6, 1])
    #     gen = finite_field_element_generator(finite_field)
    #     exp_element = FiniteFieldElement(finite_field, [1, 3])
    #     self.assertEqual(exp_element.get_multiplicative_order(), 48)
    #     self.assertEqual(gen, exp_element)
    #
    #     check_element = FiniteFieldElement(finite_field, [1, 1])
    #     bsgs = BSGS(gen, check_element)
    #     self.assertEqual(bsgs, 23)
