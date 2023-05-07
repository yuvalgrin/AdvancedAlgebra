import math

from models.finite_field_element import FiniteFieldElement, get_e1_element


def get_power_list(element: FiniteFieldElement, i: int):
    if i < 0:
        raise ValueError("List ascends from 0 to i > 0, please provide a positive integer")
    field = element.field
    e1 = get_e1_element(field)
    power_list = {}
    power_list[e1] = 0
    if i == 0:
        return power_list
    a = element
    power_list[a] = 1
    j = 1
    while j < i:
        a = a * element
        power_list[a] = j+1
        j = j + 1
    return power_list


def BSGS(generator: FiniteFieldElement, element: FiniteFieldElement):
    if generator.field != element.field:
        raise ValueError("Cannot use different different finite fields")
    polyorder = len(generator.field.f) - 1
    p = generator.field.p
    q = p ** polyorder
    iterator = element
    m = math.ceil(math.sqrt(q-1))
    baby_list = get_power_list(generator, m - 1)
    j = 0
    giant_element = generator ** (-m)
    while j < m-1:
        if iterator in baby_list:
            i = baby_list[iterator]
            return i + j * m
        iterator = iterator * giant_element
        j += 1
    raise RuntimeError("Failed running BSGS algorithm")
