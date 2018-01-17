#!/usr/bin/env python

import time
import random
import sys
import os
from ch10_base_datastruct import *


@time_profile()
def test(length):
    l = LinkedList()

    for _ in range(0, length):
        l.insert(42)

def main():
    for i in range(2, 7):
        test(10 ** i)


if __name__ == "__main__":
    main()
