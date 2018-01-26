#!/usr/bin/env python

from introduction_of_algorithms import *


def main():
    t = RedBlackTree()
    t.insert(2)
    t.insert(1)
    t.root.right_rotate()
    print(t)

if __name__ == "__main__":
    main()
