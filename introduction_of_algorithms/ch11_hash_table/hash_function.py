#!/usr/bin/env python

from ..util import *
from random import randint

def create_mul_hash_function(capacity):
    def mul_hash(k):
        """ Hash value for 'k' in the hash table has 'm' solts. """
        return int(k * PHI % 1 * capacity)
    return mul_hash


def create_div_hash_function(capacity):
    def div_hash(k):
        """ Hash value for 'k' in the hash table has 'm' solts. """
        return k % capacity
    return div_hash


def create_universal_hash_function(capacity):
    prime = 49999
    a = randint(1, prime)
    b = randint(0, prime)

    def universal_hash_function(k):
        if not k < prime: raise ValueError("Key '%s' greater or equal prime %s." % (k, prime))
        return (a * k + b) % prime % capacity

    return universal_hash_function


def test_hash_function(hash_function, number_of_solt, defined_field):
    """ Routine to test hash function. """
    m = number_of_solt
    U = defined_field
    hashed = [hash_function(x) for x in range(0, U)]
    counts = [hashed.count(x) for x in range(0, m)]
    print()
    print("Hashed: of", hash_function.__name__, hashed)
    print("Count: of", hash_function.__name__, counts)
