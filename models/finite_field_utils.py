from itertools import product

from models.finite_field import FiniteField
from models.finite_field_element import FiniteFieldElement
from models.prime_field_element import PrimeFieldElement


def get_e0_element(field: FiniteField):
    polyorder = len(field.f) - 1
    poly_list = [0] * polyorder
    result = FiniteFieldElement(field, poly_list)
    return result


def get_e1_element(field: FiniteField):
    polyorder = len(field.f) - 1
    poly_list = [1] + [0] * (polyorder - 1)
    result = FiniteFieldElement(field, poly_list)
    return result


def create_set_of_finite_field_elements(field: FiniteField):
    polyorder = len(field.f) - 1
    p = field.p
    prime_field_elements = [PrimeFieldElement(i, p) for i in range(p)]
    all_coeffs_combinations = list(product(prime_field_elements, repeat=polyorder))
    field_elements_set = set()
    for coeffs in all_coeffs_combinations:
        new_field = FiniteFieldElement(field, coeffs)
        field_elements_set.add(new_field)
    return field_elements_set
