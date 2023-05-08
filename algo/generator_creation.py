from itertools import product

from models.finite_field import FiniteField
from models.finite_field_element import get_e0_element, get_e1_element, FiniteFieldElement
from models.prime_field_element import PrimeFieldElement


def finite_field_element_generator(field: FiniteField):
    polyorder = field.polyorder
    p = field.p
    L = p ** polyorder - 1
    floor_L = L // 2
    e0 = get_e0_element(field)
    e1 = get_e1_element(field)
    extended_field_set = create_set_of_finite_field_elements(field)
    extended_field_set.discard(e0)
    extended_field_set.discard(e1)
    while len(extended_field_set) > 1:
        element = extended_field_set.pop()
        a = element
        o = 1
        while a != e1:
            o = o + 1
            a = a * element
            extended_field_set.discard(a)
            if o > floor_L:
                return element
    return extended_field_set.pop()


def create_set_of_finite_field_elements(field: FiniteField):
    p = field.p
    prime_field_elements = [PrimeFieldElement(i, p) for i in range(p)]
    all_coeffs_combinations = list(product(prime_field_elements, repeat=field.polyorder))
    field_elements_set = set()
    for coeffs in all_coeffs_combinations:
        new_field = FiniteFieldElement(field, coeffs)
        field_elements_set.add(new_field)
    return field_elements_set
