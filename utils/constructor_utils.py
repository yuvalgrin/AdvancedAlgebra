from models.prime_field_element import PrimeFieldElement


def construct_coeffs(coeffs, p):
    if not coeffs:
        raise ValueError("Invalid coeffs value")
    if isinstance(coeffs[0], int):
        return [PrimeFieldElement(coeff, p) for coeff in coeffs]
    elif isinstance(coeffs[0], PrimeFieldElement):
        return coeffs
    else:
        raise ValueError("Invalid coeffs value")