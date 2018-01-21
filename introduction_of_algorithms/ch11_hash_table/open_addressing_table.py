from introduction_of_algorithms.ch11_hash_table.hash_function import *
from introduction_of_algorithms.util.constant import *

import pprint


def create_linear_probing(capacity):
    """ Linear probing function factory. """
    base_hash_function = create_universal_hash_function(capacity)

    def linear_probeing(k, a):
        return (base_hash_function(k) + a) % capacity

    return linear_probeing


class OpenAddressingTable(object):
    def __init__(self, capacity, hash_function_factor=create_linear_probing):
        self.capacity = capacity
        self.hash_function = hash_function_factor(capacity)
        self.table = [None] * capacity

    def insert(self, k):
        for i in range(0, self.capacity):
            hashed = self.hash_function(k, i)
            if self[hashed] == NIL:
                self[hashed] = k
                return hashed
        else:
            raise OverflowError()

    def search(self, k):
        for i in range(0, self.capacity):
            hashed = self.hash_function(k, i)
            if self[hashed] == NIL:
                return NIL
            elif self[hashed] == k:
                return hashed
        else:
            return NIL

    def __str__(self):
        return "<" + ", ".join([str(x) if x != NIL else "NIL"  for x in self.table]) + ">"

    def __getitem__(self, item):
        return self.table[item]

    def __setitem__(self, key, value):
        self.table[key] = value

    def __contains__(self, item):
        for i in range(0, self.capacity):
            hashed = self.hash_function(item, i)
            if self[hashed] == NIL:
                return False
            elif self[hashed] == item:
                return True
        else:
            return False


t = OpenAddressingTable(100)

for i in range(0, 100):
    t.insert(i)

print(t)
