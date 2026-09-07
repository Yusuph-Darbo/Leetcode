# Approach:
# Iterate through each grade in the list and apply the rounding rules.
#
# If the grade is less than 38, it cannot be rounded to a passing grade,
# so leave it unchanged.
#
# Otherwise, find the remainder when dividing the grade by 5 to determine
# how far it is from the next multiple of 5.
# Compute the difference between the grade and the next multiple of 5.
#
# If this difference is less than 3, round the grade up by adding the difference.
# Otherwise, leave the grade unchanged.
#
# Store each final grade in a new list and return the updated list.
#
# Time Complexity: O(n) — we process each grade once.
# Space Complexity: O(n) — we store the results in a new list.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    updagedGrades = []
    
    for grade in grades:
        if grade < 37:
            updagedGrades.append(grade)
        else:
            remainder = grade % 5
            difference = 5 - remainder
            
            if difference < 3:
                grade += difference
                
            updagedGrades.append(grade)

        
    return updagedGrades
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
