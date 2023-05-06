import unittest

from models.bsgs import get_power_list, BSGS
from models.finite_field import FiniteField
from models.finite_field_utils import get_e1_element


class TestFiniteField(unittest.TestCase):
    def test_get_power_list(self):
        finite_field = FiniteField(3, [2, 2, 1])
        e1 = get_e1_element(finite_field)
        power_list = get_power_list(e1, 2)
        self.assertEqual(power_list, [e1, e1, e1])

    def test_bsgs(self):
        pass
        # finite_field = FiniteField(3, [2, 2, 1])
        # e1 = get_e1_element(finite_field)
        # power_list = BSGS(e1, 2)
        # self.assertEqual(power_list, [e1, e1, e1])
