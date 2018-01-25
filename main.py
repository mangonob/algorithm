#!/usr/bin/env python

from introduction_of_algorithms import *


def main():
    t = BinarySearchTree()
    t.insert(9)
    t.insert(2)
    t.insert(10)
    t.insert(1)
    t.insert(4)
    t.insert(11)
    t.insert(3)
    t.insert(7)
    t.insert(5)
    t.insert(8)
    t.insert(6)

    t.remove(1)
    t.remove(10)
    t.remove(4)
    print(t)

if __name__ == "__main__":
    main()
