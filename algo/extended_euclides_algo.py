def inverse_modulo(a, modulo):
    s = 0
    t = 1
    gcd = a
    p0 = modulo
    while gcd != 1:
        quotient = modulo // gcd
        tmp = gcd
        gcd = modulo - quotient * gcd
        modulo = tmp

        tmp = t
        t = s - quotient * t
        s = tmp
    if s < 0:
        s = s + p0
    return s
