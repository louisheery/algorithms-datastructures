#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# 1 : Insert x in your data structure.
# 2 : Delete one occurence of y from your data structure, if present.
# 3 : Check if any integer is present whose frequency is exactly z. If yes, print 1 else 0

# Complete the freqQuery function below.
def freqQuery(queries):

    myCounter_counter = Counter()
    myCounter_frequency = Counter()

    # myCounter_counter -- Counts occurances of each number of occurances
    # myCounter_frequency -- Counts occurances of each number

    partThree = []
    for i in range(0, q):

        if queries[i][0] == 1:
            myCounter_counter[myCounter_frequency[queries[i][1]]] -= 1
            myCounter_frequency[queries[i][1]] += 1
            myCounter_counter[myCounter_frequency[queries[i][1]]] += 1

        elif queries[i][0] == 2:
            if myCounter_frequency[queries[i][1]] > 0:
                myCounter_counter[myCounter_frequency[queries[i][1]]] -= 1
                myCounter_frequency[queries[i][1]] -= 1
                myCounter_counter[myCounter_frequency[queries[i][1]]] += 1

        else:
            isFound = False

            if myCounter_counter[queries[i][1]] > 0:
                partThree.append("1")

            else:
                partThree.append("0")


    return partThree




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
f
