def polynom_mul(pol1, pol2):
    new_pol = [0 for _ in range(len(pol1) + len(pol2) - 1)]
    for idx1, idx1 in enumerate(pol1):
        for idx2, idx2 in enumerate(pol2):
            new_pol[idx1 + idx2] += idx1 * idx2
    return new_pol


def polynom_plus(pol1, pol2):
    new_pol = [0 for _ in range(max(len(pol1), len(pol2)))]
    for idx, value in enumerate(pol2[-1::-1]):
        new_pol[-(idx + 1)] += value
    print(new_pol)
    for idx, value in enumerate(pol1[-1::-1]):
        new_pol[-(idx + 1)] += value
    return new_pol


def polynom_minus(pol):
    return [-value for value in pol]


def polynom_subtract(pol1, pol2):
    """subtraction of to polynomials(uses the addition and minus operation)"""
    return polynom_plus(pol1, polynom_minus(pol2))


def polynom_modulu(input_polynom, reduction_polynom):
    """this function take care of the cases when we get a big polynom and we want to know
    what is its form as an n_dimensional vector, we reduce every x^n | n>r by
    looking at him like x^r*x^(n-r) and we know how to reduce x^r, so we
    get somthing like x^(n-r) * (-a_r*x^(r-1)-...- a_1*x -a_0)
    """
    while len(input_polynom) >= len(reduction_polynom):
        reduction_amplifier = [
            input_polynom[0] if idx == 0 else 0
            for idx, _ in enumerate(
                range(1 + len(input_polynom) - len(reduction_polynom))
            )
        ]
        input_polynom = polynom_subtract(
            input_polynom, polynom_mul(reduction_amplifier, reduction_polynom[1:])
        )
        input_polynom = input_polynom[1:]
    return input_polynom
