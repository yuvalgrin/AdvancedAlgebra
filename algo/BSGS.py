from typing import Dict

import math

from models.finite_field_element import FiniteFieldElement, get_e1_element


def calculate_baby_steps(element: FiniteFieldElement, i: int) -> Dict[FiniteFieldElement, int]:
    """"""
    if i < 0:
        raise ValueError(f"i: {i} must be positive")
    e1 = get_e1_element(element.field)
    power_list = {e1: 0}
    if i == 0:
        return power_list

    alpha = element
    power_list[alpha] = 1
    j = 1
    while j < i:
        alpha = alpha * element
        power_list[alpha] = j + 1
        j = j + 1
    return power_list


def baby_step_giant_step(generator: FiniteFieldElement, element: FiniteFieldElement):
    if generator.field != element.field:
        raise ValueError("Cannot use different different finite fields")
    p = generator.field.p
    q = p ** generator.field.polyorder
    iterator = element
    m = math.ceil(math.sqrt(q))
    baby_list = calculate_baby_steps(generator, m - 1)
    j = 0
    giant_element = generator ** (-m)
    while j < m-1:
        if iterator in baby_list:
            i = baby_list[iterator]
            return i + j * m
        iterator = iterator * giant_element
        j += 1
    raise RuntimeError(f"Failed running BSGS algorithm on generator: {generator}, and element {element}")
