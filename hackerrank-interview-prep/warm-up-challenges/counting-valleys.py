#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):

    altitude = 0
    exitValley = 0

    for i in range(0, n):

        if s[i] == "D":
            altitude = altitude - 1

        if s[i] == "U":
            if altitude == -1:
                exitValley = exitValley + 1
            altitude = altitude + 1

    return exitValley

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
