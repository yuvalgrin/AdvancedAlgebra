from typing import List


def polynom_mul(pol1: List[int], pol2: List[int]):
    """Multiply two polynoms element by element"""
    new_pol = [0 for _ in range(len(pol1) + len(pol2) - 1)]
    for idx1, i1 in enumerate(pol1):
        for idx2, i2 in enumerate(pol2):
            new_pol[idx1 + idx2] += int(i1) * int(i2)
    return new_pol


def polynom_plus(pol1: List[int], pol2: List[int]):
    """Add two polynoms element by element"""
    new_pol = [0 for _ in range(max(len(pol1), len(pol2)))]
    for idx, i in enumerate(pol2[-1::-1]):
        new_pol[-(idx + 1)] += i
    for idx, i in enumerate(pol1[-1::-1]):
        new_pol[-(idx + 1)] += i
    return new_pol


def polynom_minus(pol: List[int]):
    """Multiply a polynom by -1"""
    return [-x for x in pol]


def polynom_subtract(pol1: List[int], pol2: List[int]):
    """Subtraction of two polynoms (uses the addition and minus operations)"""
    return polynom_plus(pol1, polynom_minus(pol2))


def modulu_polynom(input_polynom: List[int], reduction_polynom: List[int]):
    """Modulu a polynom with a irreducible polynom.
    If the rank(polynom) > rank(reduction polynom):
        # example rank(x^3 + x) > rank(x^2 + 2)
        Reduce every x^n | n>r, where r = rank(reduction polynom), by representing it as x^r * x^(n-r).
        * This is helps us because we know how to reduce x^r.
        Finally, we get somthing like x^(n-r) * (-a_r*x^(r-1)-...- a_1*x -a_0)

    * Reduce x^r: reduction polynom = 0(modulo reduction polynom) = x^r + a_r * x^(r-1) + ... + a_1 * x^0
    Thus, x^r = - (a_r * x^(r-1) + ... + a_1 * x^0) (modulo reduction polynom)
    """
    while len(input_polynom) >= len(reduction_polynom):
        reduction_amplifier = [
            input_polynom[0] if idx == 0 else 0
            for idx, _ in enumerate(
                range(1 + len(input_polynom) - len(reduction_polynom))
            )
        ]
        amplifier_mult = polynom_mul(reduction_amplifier, reduction_polynom[1:])
        input_polynom = polynom_subtract(input_polynom, amplifier_mult)
        input_polynom = input_polynom[1:]
    return input_polynom
