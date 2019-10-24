#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):

    newArray = []

    lengthOfArray = len(a)

    shiftAmount = d

    arrayLen = len(a)

    completeLoops = arrayLen//d

    remainingLoops = d - (completeLoops * arrayLen)

    if remainingLoops == 0:
        return a
    elif remainingLoops < 0:
        remainingLoops = d
    else:
        remainingLoops = remainingLoops


    for i in range(0, lengthOfArray):
        newLocation = (i + remainingLoops) % lengthOfArray
        print(newLocation)
        newArray.append(a[newLocation])

    return newArray

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
