# Approach:
# Compare the returned date with the due date.
#
# If the book is returned before the due year, no fine.
# If returned after the due year, fine is 10000.
#
# If returned in the same year:
#   If returned before the due month, no fine.
#   If returned after the due month, fine is 500 × months late.
#
# If returned in the same month and year:
#   If returned before or on due day, no fine.
#   If returned after due day, fine is 15 × days late.
#
# Time Complexity: O(1)
# Space Complexity: O(1)


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'libraryFine' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d1
#  2. INTEGER m1
#  3. INTEGER y1
#  4. INTEGER d2
#  5. INTEGER m2
#  6. INTEGER y2
#

def libraryFine(d1, m1, y1, d2, m2, y2):
    # Write your code here
    
    # returned before or on due year
    if y1 < y2:
        return 0

    # returned after due year
    if y1 > y2:
        return 10000

    # same year, returned before or on due month
    if m1 < m2:
        return 0

    # same year, returned after due month
    if m1 > m2:
        return 500 * (m1 - m2)

    # same month, returned before or on due day
    if d1 <= d2:
        return 0

    # same month, returned after due day
    return 15 * (d1 - d2)
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    d1 = int(first_multiple_input[0])

    m1 = int(first_multiple_input[1])

    y1 = int(first_multiple_input[2])

    second_multiple_input = input().rstrip().split()

    d2 = int(second_multiple_input[0])

    m2 = int(second_multiple_input[1])

    y2 = int(second_multiple_input[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    fptr.write(str(result) + '\n')

    fptr.close()
