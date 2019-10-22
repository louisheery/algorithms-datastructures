#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):

    occuranceList = [i for i in range(len(s)) if s[i] == 'a']

    completeArraysinBigArray = math.floor(n/len(s))

    leftOversinBigArray = n -(math.floor(n/len(s)) * len(s))

    occuranceListCut = [i for i in occuranceList if i < leftOversinBigArray]

    numberOfA = (completeArraysinBigArray * len(occuranceList)) + len(occuranceListCut)

    return numberOfA

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
