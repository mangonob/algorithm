#!/usr/bin/env python

from introduction_of_algorithms.util import *
from random import randint


def mul_hash(k, m):
    """ Hash value for 'k' in the hash table has 'm' solts. """
    return int(k * PHI % 1 * m)


def div_hash(k, m):
    """ Hash value for 'k' in the hash table has 'm' solts. """
    return k % m


def create_universal_hash_function():
    prime = 49999
    a = randint(1, prime)
    b = randint(0, prime)

    def func(k, m):
        print(k, a, b, prime, (a * k + b) % prime)
        if not k < prime: raise ValueError("Key '%s' greater or equal prime %s." % (k, m))
        return (a * k + b) % prime % m

    return func


def test_hash_function(hash_function, number_of_solt, defined_field):
    """ Routine to test hash function. """
    m = number_of_solt
    U = defined_field
    hashed = [hash_function(x, m) for x in range(0, U)]
    counts = [hashed.count(x) for x in range(0, m)]
    print()
    print("Hashed: of", hash_function.__name__, hashed)
    print("Count: of", hash_function.__name__, counts)


def main():
    test_hash_function(mul_hash, 100, 10000)
    test_hash_function(div_hash, 100, 10000)
    test_hash_function(create_universal_hash_function(), 100, 10000)


if __name__ == "__main__":
    main()