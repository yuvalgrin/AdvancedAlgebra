from itertools import product
from typing import Set

from models.finite_field import FiniteField
from models.finite_field_element import get_e0_element, get_e1_element, FiniteFieldElement
from models.prime_field_element import PrimeFieldElement


def find_generator_for_field(field: FiniteField) -> FiniteFieldElement:
    """Find a generator for the finite field.
    Create a set of all the elements in the field,
    Iterate over the elements:
        - calculate the multiplicative order of the element,
        - If it's multiplicative order == p^n -1 then it's the generator -> return the element
        - Else remove it and its multiplications from the set
        (The multiplications of an element which is not the generator cannot be a generator)"""

    field_order = field.p ** field.polyorder - 1
    floor_field_order = field_order // 2

    # o(e0) = inf, o(e1) = 1
    e0 = get_e0_element(field)
    e1 = get_e1_element(field)

    extended_field_set: Set = create_set_of_all_elements_in_field(field)
    extended_field_set.discard(e0)
    extended_field_set.discard(e1)

    while len(extended_field_set) > 1:
        element = extended_field_set.pop()
        alpha = element
        o = 1
        while alpha != e1:
            o += 1
            alpha *= element
            extended_field_set.discard(alpha)
            if o > floor_field_order:
                return element
    return extended_field_set.pop()


def create_set_of_all_elements_in_field(field: FiniteField) -> Set[FiniteFieldElement]:
    """Create a set of all the possible finite field elements.
    Use the cartesian multiplication of the prime field elements and add them to the set."""
    prime_field_elements = [PrimeFieldElement(i, field.p) for i in range(field.p)]
    all_coeffs_combinations = product(prime_field_elements, repeat=field.polyorder)
    all_elements_in_field = {FiniteFieldElement(field, coeffs) for coeffs in all_coeffs_combinations}
    return all_elements_in_field
