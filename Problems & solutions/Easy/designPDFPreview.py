# Approach:
# Each letter has a height stored in the array h from index 0 to 25.
# Use ASCII conversion to find the index of each letter:
# index = ord(letter) - ord('a')
#
# Iterate through each letter in the word and find its height.
# Keep track of the maximum height.
#
# The highlighted area is:
# maxHeight × length of word
#
# Time Complexity: O(n)
# Space Complexity: O(1)


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    # Write your code here
    
    # iterate thorugh the arr
    # For each letter in the word get its coresponding height
    # Get the max height and multiply by the length of the string
    maxHeight = 0
        
    # Can make a dict where each letter corresponds to its height
    # There might be a better solution
    alaphabet = {}
    
    for i in range(26):
        # ord return the value of a char
        alaphabet[chr(ord('a') + i)] = h[i]
        

    
    for letter in word:
        height = alaphabet[letter]
        if maxHeight < height:
            maxHeight = height
                
    return maxHeight * len(word)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
