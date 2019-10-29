#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the countTriplets function below.
def countTriplets(arr, r):

    countDoubletPotentials = Counter() # Counts number of Doublet Potentials, i.e. the frequency of each possible number of values for the 2nd value in the Sequence
    countTripletPotentials = Counter() # Counts number of Triplet Potentials, i.e. the frequency of each possible number of values for the 3rd value in the Sequence

    counter = 0 # Counts number of complete Triplets

    # Loop over the entire Array
    for i in range(0, n):

        # If
        if countTripletPotentials[arr[i]] > 0:
            counter += countTripletPotentials[arr[i]] # Increase Complete Triplets by the number of Triplet Potentials that have now found their 3rd Value (i.e. value required to complete the triplet)

        if countDoubletPotentials[arr[i]] > 0:
            countTripletPotentials[(arr[i] * r)] += countDoubletPotentials[arr[i]] # Increase number of Triplet Potentials by the number of Doublet Potentials that have now found their 2nd Value (i.e. value required to complete the Doublet, so only 1 more value required to make a triplet)

        countDoubletPotentials[(arr[i] * r)] += 1 # Add the required 2nd value to be found to make a Doublet, i.e. counter of Doublet potentials.





    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
