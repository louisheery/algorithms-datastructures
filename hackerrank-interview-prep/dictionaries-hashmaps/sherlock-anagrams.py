#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    count = 0

    for i in range(1,len(s)+1):

        anagramA = ["".join(sorted(s[j:j+i])) for j in range(len(s)-i+1)]

        anagramB = Counter(anagramA)

        for j in anagramB:
            count = count + anagramB[j]*(anagramB[j]-1)/2

    return int(count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
