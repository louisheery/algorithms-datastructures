#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the makeAnagram function below.
def makeAnagram(a, b):

    aCollection = Counter()
    bCollection = Counter()

    for letter in a:
        aCollection[letter] += 1

    for letter in b:
        bCollection[letter] += 1


    print(aCollection)
    print(bCollection)
    symmetric_difference = (aCollection + bCollection) - (aCollection & bCollection) - (aCollection & bCollection)

    return sum(symmetric_difference.values())


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
