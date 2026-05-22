# Approach:
# First, store all elements of the array in a set for efficient lookup.
# This allows checking whether a value exists in constant time O(1).
#
# Initialize a counter variable numOfPairs to 0.
#
# Iterate through each unique number in the set.
# For each number, check if number + k exists in the set.
# If it exists, it means a valid pair with difference k has been found,
# so increment the counter.
#
# Finally, return the total number of valid pairs.
#
# Time Complexity: O(n) — each element is checked once.
# Space Complexity: O(n) — extra space is used to store the set.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pairs(k, arr):
    # Write your code here
    numOfPairs = 0
    values = set(arr)
    
    for num in values:
        if num + k in values:
            numOfPairs += 1
            
    return numOfPairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
