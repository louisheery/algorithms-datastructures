#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):

    mySet = set()

    pairs = 0

    for i in range (0, n):
        if ((ar[i] not in mySet)):
            mySet.add(ar[i])
        else:
            pairs = pairs + 1
            mySet.remove(ar[i])

    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
