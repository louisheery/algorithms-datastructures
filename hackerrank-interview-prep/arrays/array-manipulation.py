#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):

    myList = [0] * (n + 1)

    for m in queries:

        print(m[0]-1, " ", m[1])
        myList[m[0]-1] = myList[m[0]-1] + m[2]
        myList[m[1]] = myList[m[1]] - m[2]

    for i in range(1, n):
        myList[i] = myList[i] + myList[i - 1]

    return max(myList)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
