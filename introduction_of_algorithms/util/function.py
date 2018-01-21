from .decorator import *


def mod_inverse_fermat(a, prime):
    """ Number-theoretic reciprocal of a mod prime. """
    result = 1
    power = prime - 2
    while power:
        if power & 0x1:
            result *= a
            result %= prime
        a *= a
        a %= prime
        power >>= 1

    return result


def mod_inverse_extend_euclidean(a, prime):
    x = [0]
    y = [0]

    def inner_gcd(a, b, x, y):
        if b == 0:
            x[0] = 1
            y[0] = 0
            return a

        result = inner_gcd(b, a % b, y, x)
        y[0] -= a // b * x[0]
        return result

    inner_gcd(a, prime, x, y)

    return x[0] % prime
