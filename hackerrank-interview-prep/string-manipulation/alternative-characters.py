#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):

    counter = 0

    stringList = list(s)

    j = 0

    while (j < len(stringList)-1):
        if stringList[j] == stringList[j + 1]:
            counter += 1
        j = j + 1

    return counter



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
