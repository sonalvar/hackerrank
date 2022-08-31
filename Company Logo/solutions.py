#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter



if __name__ == '__main__':
    s = input()
    n = 0
    sorted_list = sorted(Counter(s).items(), key=lambda x: (-x[1],x[0]))
    for key, value in sorted_list:
        print(key, value)
        n += 1
        if n == 3:
            break
