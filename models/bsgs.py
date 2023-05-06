import math

from models.finite_field_element import FiniteFieldElement
from models.finite_field_utils import get_e1_element


def get_power_list(element: FiniteFieldElement, i: int):
    if i < 0:
        raise ValueError("List ascends from 0 to i > 0, please provide a positive integer")
    field = element.field
    e1 = get_e1_element(field)
    power_list = []
    power_list.append(e1)
    if i == 0:
        return power_list
    a = element
    power_list.append(a)
    j = 1
    while j < i:
        a = a * element
        power_list.append(a)
        j = j + 1
    return power_list


def BSGS(generator: FiniteFieldElement, element: FiniteFieldElement):
    if generator.field != element.field:
        raise ValueError("Cannot use different different finite fields")
    polyorder = len(generator.field.f) - 1
    p = generator.p
    q = p ** polyorder
    iterator = element
    m = math.ceil(math.sqrt(q-1))
    baby_list = get_power_list(generator, m - 1)
    j = 0
    giant_element = element ** (-m)
    while j < m-1:
        if iterator in baby_list:
            i = baby_list.index(iterator)
            return j+i*m
        iterator = iterator * giant_element
        j = j + 1
