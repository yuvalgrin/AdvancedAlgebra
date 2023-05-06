from models.finite_field import FiniteField
from models.finite_field_element import FiniteFieldElement
from models.finite_field_utils import create_set_of_finite_field_elements


def finite_field_element_generator(field: FiniteField):
    polyorder = len(field.f) - 1
    p = field.p
    L = p ** polyorder - 1
    FloorL = L // 2
    e0 = FiniteFieldElement.get_e0_element(field)
    e1 = FiniteFieldElement.get_e1_element(field)
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
            if o > FloorL:
                return element
    return extended_field_set.pop()
