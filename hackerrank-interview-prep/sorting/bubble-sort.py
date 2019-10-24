#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):

    counter = 0

    for i in range(0, n):
        for j in range(0, n-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                counter += 1

    print("Array is sorted in", counter, "swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[-1])


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
