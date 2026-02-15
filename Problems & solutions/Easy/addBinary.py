# Approach:
# Use two pointers starting from the end of both binary strings a and b.
# Initialize a carry variable to 0 and an empty list result to store the sum digits.
#
# Loop while either pointer is valid or there is a carry:
# - Add the current digit of a (if exists) to a running total value.
# - Add the current digit of b (if exists) to value.
# - Add the carry from the previous step to value.
# - Append value % 2 to the result list (current binary digit).
# - Update carry as value // 2.
#
# After processing all digits, reverse the result list and join into a string.
# This produces the final binary sum.
#
# Time Complexity: O(len(S)) — where S is the length of the longest string
# Space Complexity: O(max(len(a), len(b))) — for storing the result.


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = []
        # Start from the end of the string
        i = len(a) - 1
        j = len(b) - 1
        carry = 0

        while i >= 0 or j >= 0 or carry == 1:
            value = carry
            if i >= 0:
                # converting to int
                value += int(a[i])
                i -= 1

            if j >= 0:
                value += int(b[j])
                j -= 1

            result.append(str(value % 2))
            carry = value // 2
        
        return ''.join(result[::-1])

        
        