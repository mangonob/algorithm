#!/usr/bin/env python

from introduction_of_algorithms import *


def main():
    hashed = [mul_hash(x, 100) for x in range(0, 10000)]
    counts = [hashed.count(x) for x in range(0, 100)]
    print(hashed)
    print(counts)


if __name__ == "__main__":
    main()
