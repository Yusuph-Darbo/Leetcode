# Approach:
# First, remove all spaces from the input string to create a continuous sequence of characters.
# Let stringLength be the length of this new string.
#
# Compute the number of rows and columns for the grid:
# - rows = floor(sqrt(stringLength))
# - cols = ceil(sqrt(stringLength))
# If rows * cols is still less than stringLength, increase rows by 1 to ensure the grid can hold all characters.
#
# Conceptually place the characters row-wise into the grid.
# Then, build the encrypted string by reading the grid column-wise.
# For each column, collect characters from top to bottom and append them as a word.
#
# Finally, join all words with spaces to produce the encrypted result.
#
# Time Complexity: O(n) — each character is visited once.
# Space Complexity: O(n) — extra space is used to build the result string.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # Write your code here
    # Removing white space
    newString = s.replace(" ", "")
    
    # Getting length of new string
    stringLength = len(newString)
    
    rows = math.floor(math.sqrt(stringLength))
    cols = math.ceil(math.sqrt(stringLength))
    
    # Adjust if needed
    if rows * cols < stringLength:
        rows += 1
        
    result = []
    
    for col in range(cols):
        word = ""
        for row in range(rows):
            index = row * cols + col
            
            if index < stringLength:
                word += s[index]
        
        result.append(word)
            
    return " ".join(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
