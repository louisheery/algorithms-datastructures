#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(n,c):

    numberOfJumps = 0

    i = 0
    while i < n - 1:
        if (i + 2 < n) and (c[i + 2] == 0):
            numberOfJumps = numberOfJumps + 1
            print("Jump Once from ", i, " to ", i + 2, "\n")
            i = i + 2
        else:
            numberOfJumps = numberOfJumps + 1
            print("Jump Once from ", i, " to ", i + 1, "\n")
            i = i + 1

    return numberOfJumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(n,c)

    fptr.write(str(result) + '\n')

    fptr.close()
