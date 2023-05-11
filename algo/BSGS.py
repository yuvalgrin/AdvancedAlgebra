from typing import Dict

import math

from models.finite_field_element import FiniteFieldElement, get_e0_element, get_e1_element


def calculate_baby_steps(element: FiniteFieldElement, i: int) -> Dict[FiniteFieldElement, int]:
    """The function creates a list of baby steps.
    For a given element (element: FiniteFieldElement), it returns the powers of the element (0 to the i-th power)
    The data structure chosen to create the list is "dictionary" to allow quick retrieval of the power index (hashtable).
    The dictionary works as follows: the key contains the element and the value contains the power to which the element has been raised to.
    """
    if i < 0:
        raise ValueError(f"i: {i} must be positive")
    e1 = get_e1_element(element.field)
    power_list = {e1: 0}

    # for i=0, we return the unit element
    if i == 0:
        return power_list

    # Initializing the element as alpha and adding the first power
    alpha = element
    power_list[alpha] = 1
    j = 1
    # Finding the rest of the powers and adding them to the list
    while j < i:
        alpha = alpha * element
        power_list[alpha] = j + 1
        j = j + 1
    return power_list


def baby_step_giant_step(generator: FiniteFieldElement, element: FiniteFieldElement):
    """The function utilizes the Baby Step Giant Step (BSGS) algorithm.
    The user inputs a generator (generator: FiniteFieldElement) and an arbitrary element (element: FiniteFieldElement) from the multiplicative group.
    Since any element can be represented as generator^t, we wish to find the power to which the generator has been raised for which it equals the element.
    The algorithm works as follows:
    1. Generating baby_list: all the powers of the generator up to some value i - this list is in dictionary form to enable quick retrieval of the power index (hashtable).
    2. Constructing the elements using giant steps element * generator^(-j m), such that the first element is just "element", the second is element * generator^(-m),
    the third is element * generator^(-2m) and so on.
    In each creating of en element, we check wheter it is found in the baby_list,
    if it is not there, we find the next element in the sequence, by multiplying our current element by generator^(-m).
    The algorithm stops when we get a "hit", an element created in the giant step is found on baby_list, for which we return i+j*m and conclude the algorithm
    """
    # The input finite field elements must belong to the same field:
    if generator.field != element.field:
        raise ValueError("Cannot use different finite fields")
    e0 = get_e0_element(element.field)
    e1 = get_e1_element(element.field)
    # The input finite field elements belong to the multiplicative group:
    if element == e0:
        raise ValueError("Element must be in the multiplicative group")
    if generator == e0:
        raise ValueError("Generator must be in the multiplicative group")
    # The input generator must be different than the unit element:
    if generator == e1:
        raise ValueError("Generator must be different than the unit element")

    p = generator.field.p  # the prime used in the field k
    q = p ** generator.field.polyorder  # number of field elements
    iterator = element
    m = math.ceil(math.sqrt(q))  # the halting point of the algorithm
    baby_list = calculate_baby_steps(generator, m - 1)
    j = 0  # initializing the construction of giant steps j=0

    # giant_element - represent the giant steps between each giant element;
    # For each progressive step we need to multiply by this element.
    giant_element = generator ** (-m)
    # constructing giant steps
    while j < m - 1:
        # checking if the current element is found in baby_list
        if iterator in baby_list:
            i = baby_list[iterator]
            return i + j * m
        iterator = iterator * giant_element
        j += 1
    # If the algorithm fails for any reason, the function will raise an error
    raise RuntimeError(f"Failed running BSGS algorithm on generator: {generator}, and element {element}")
