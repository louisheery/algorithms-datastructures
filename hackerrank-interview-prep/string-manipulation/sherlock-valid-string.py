#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the isValid function below.
def isValid(s):

    freq = Counter(s)
    values = list(freq.values())
    values.sort()

    print(values)

    if values.count(values[0]) == len(values):
        return("YES")
    if values.count(values[0]) == len(values) - 1 and values[-1] + 1 == values[0]:
        return("YES")

    if (values.count(values[0]) == len(values) - 1 and values[-1] - values[-2] == 1):
        return("YES")

    if (values[1:].count(values[1]) == len(values[1:]) and values[0] == 1):
        return("YES")

    return("NO")


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
