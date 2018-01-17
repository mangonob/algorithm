#!/usr/bin/env python

import time
import random
import sys
import os
from ch10_base_datastruct import *


@time_profile()
@time_profile()
def main():
    l = LinkedList()

    for _ in range(0, 1000):
        l.insert(1)

    print(len(l))


if __name__ == "__main__":
    main()
