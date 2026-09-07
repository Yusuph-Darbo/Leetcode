#!/bin/python3

import math
import os
import random
import re
import sys

# Approach:
# Iterate through the array once and count how many elements are
# positive, negative, and zero.
# After counting, divide each count by the total number of elements
# to compute their respective ratios.
# Print the ratios in the required order.
#
# Time Complexity: O(n) — we traverse the array exactly once.
# Space Complexity: O(1) — only three counter variables are used.


def plusMinus(arr):
    # Write your code here
    positive_nums = 0
    negative_nums = 0
    zero_nums = 0
    
    for num in arr:
        # Checking for positive nums
        if num > 0:
            positive_nums += 1 
        
        # Checking for negative nums
        elif num < 0:
            negative_nums += 1
        
        else:
            zero_nums += 1
            
    print(positive_nums / len(arr))
    print(negative_nums / len(arr))
    print(zero_nums / len(arr))
            
            
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
